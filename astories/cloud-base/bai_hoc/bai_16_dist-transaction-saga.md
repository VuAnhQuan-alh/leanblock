# Bài 16 — Distributed nâng cao: Transaction và saga

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 3–4 (Distributed ↔ Dữ liệu).** [Bài 2](bai_02_os-concurrency.md) gặp "all or nothing" ở mức một lệnh; bài này nâng nó lên mức **transaction** (nhiều thao tác, nhiều hàng) và rồi mức **nhiều node** — nơi nó hoá thành một bài toán consensus (Bài 9). Khi distributed transaction quá đắt/mong manh, ngành chuyển sang **saga** (bù trừ). Đây là nền để hiểu **DynamoDB Transactions, Step Functions/saga, và nhất quán chéo-service** ở `aws-fund`.
> Nguồn: **DDIA** — ch. 7 (Transactions), ch. 9 (Atomic Commit & 2PC).
> **Trích:** `DDIA (tr. X)` = trang **in**; **offset PDF = tr. + 22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 2 — atomicity](bai_02_os-concurrency.md), [Bài 9 — consensus](bai_09_dist-phan-manh.md), [Bài 7 — thất bại](bai_07_dist-giao-tiep.md).

## Mục lục

1. [Transaction và ACID](#1-transaction-và-acid)
2. [Atomicity: quyền huỷ bỏ](#2-atomicity-quyền-huỷ-bỏ)
3. [Giao dịch trải nhiều node: atomic commit là consensus](#3-giao-dịch-trải-nhiều-node-atomic-commit-là-consensus)
4. [Demo: 2PC vs saga](#4-demo-2pc-vs-saga)
5. [Bảng so sánh: 2PC vs saga](#5-bảng-so-sánh-2pc-vs-saga)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Transaction và ACID

Khi một thao tác nghiệp vụ cần *nhiều* thay đổi (trừ tài khoản này, cộng tài khoản kia), ta muốn chúng hoặc *cùng* xảy ra, hoặc *không gì cả* — gói lại thành một **transaction**. Bảo đảm an toàn của transaction có một cái tên ai cũng nghe:

> [!quote] DDIA (tr. 223)
> "The safety guarantees provided by transactions are often described by the well-known acronym ACID, which stands for Atomicity, Consistency, Isolation, and Durability."
>
> *Các bảo đảm an toàn mà transaction cung cấp thường được mô tả bằng từ viết tắt nổi tiếng **ACID**: **Atomicity (nguyên tử), Consistency (nhất quán), Isolation (cô lập), Durability (bền)**.*

Bốn chữ, bốn bảo đảm khác nhau — và chúng ta đã gặp từng mảnh rải rác trong khoá: **Durability** là Bài 3 (ghi bền qua crash); **Isolation** là Bài 2 (các giao dịch đồng thời không giẫm lên nhau — chống race ở mức transaction); còn **Atomicity** là linh hồn, mục 2.

## 2. Atomicity: quyền huỷ bỏ

Atomicity trong ACID *không* phải "không thể chia nhỏ" như thường hiểu — DDIA định nghĩa nó theo *khả năng huỷ*:

> [!quote] DDIA (tr. 224)
> "The ability to abort a transaction on error and have all writes from that transaction discarded is the defining feature of ACID atomicity."
>
> ***Khả năng huỷ (abort) một transaction khi có lỗi và vứt bỏ toàn bộ các ghi** của transaction đó chính là **đặc trưng định nghĩa** của atomicity trong ACID.*

Nói cách khác: nếu giữa chừng có lỗi, database *dọn sạch* mọi thứ transaction đã làm, như thể nó chưa từng bắt đầu — nên ứng dụng **an toàn thử lại** (retry, Bài 7). Đây là "all or nothing" của Bài 2, nâng từ một lệnh CPU lên cả một nhóm thao tác database. Trên *một* node, storage engine (Bài 10) hiện thực nó dễ dàng bằng write-ahead log (Bài 3). Nhưng khi giao dịch trải *nhiều* node, mọi thứ vỡ ra.

## 3. Giao dịch trải nhiều node: atomic commit là consensus

> [!quote] DDIA (tr. 353)
> "In a database that supports transactions spanning several nodes or partitions, we have the problem that a transaction may fail on some nodes but succeed on others."
>
> *Trong một database hỗ trợ transaction **trải nhiều node hoặc partition**, ta gặp vấn đề: một transaction có thể **hỏng ở vài node nhưng thành công ở node khác**.*

Nửa thành công = vi phạm atomicity (có node đã ghi, có node chưa). Muốn giữ "all or nothing" qua nhiều máy, phải làm điều quen thuộc từ Bài 9:

> [!quote] DDIA (tr. 353)
> "we have to get all nodes to agree on the outcome of the transaction: either they all abort/roll back (if anything goes wrong) or they all commit (if nothing goes wrong). This instance of consensus is known as the atomic commit problem."
>
> *ta phải **bắt mọi node đồng ý về kết quả** của transaction: **hoặc tất cả cùng abort/roll back** (nếu có gì sai), **hoặc tất cả cùng commit** (nếu mọi thứ ổn). Trường hợp consensus này gọi là **bài toán atomic commit**.*

Giải pháp kinh điển là **two-phase commit (2PC)**: pha 1 (*prepare*) điều phối hỏi mọi node "sẵn sàng commit chưa?"; chỉ khi *tất cả* bỏ phiếu yes thì pha 2 mới ra lệnh commit — một node nói no là tất cả abort. Nó đạt atomicity, nhưng trả giá đắt: chậm (hai vòng + ghi bền), và **kẹt nếu điều phối chết** giữa chừng (các node đã prepare phải *giữ khoá chờ* — gặp lại deadlock/blocking của Bài 13 + partial failure của Bài 7). Chính vì đắt và mong manh mà nhiều hệ microservice *tránh* distributed transaction, chọn **saga** — demo mục 4 đặt hai cái cạnh nhau.

## 4. Demo: 2PC vs saga

Chuyển 30 từ A sang B, bất biến "tổng luôn = 100". **2PC**: hai node bỏ phiếu prepare, chỉ commit nếu cả hai yes. **Saga**: làm từng bước ngay (debit A rồi credit B); nếu bước sau hỏng thì chạy *bước bù* (refund A).

```typescript
// Transaction phân tán: giao dịch trải nhiều node có thể fail chỗ này được chỗ
// kia (DDIA tr.353). Giữ atomicity ("all or nothing", Bài 2) đòi MỌI node đồng
// ý outcome = atomic commit = một dạng CONSENSUS (Bài 9).
//  - 2PC: prepare (bỏ phiếu) → chỉ commit nếu TẤT CẢ yes, ngược lại abort hết.
//  - SAGA: làm từng bước ngay; bước sau fail → chạy BÙ (compensating) bước trước.
type Acct = { name: string; bal: number };
const reset = (): [Acct, Acct] => [{ name: "A", bal: 100 }, { name: "B", bal: 0 }];

// ---- 2PC: hai "node" bỏ phiếu prepare; điều phối commit/abort theo đa số-tuyệt-đối ----
function twoPC(amount: number, bWillAccept: boolean): string {
  const [a, b] = reset();
  const voteA = a.bal >= amount;          // A sẵn sàng trừ?
  const voteB = bWillAccept;              // B sẵn sàng nhận? (giả lập fail)
  if (voteA && voteB) { a.bal -= amount; b.bal += amount; return `COMMIT → A=${a.bal} B=${b.bal}`; }
  return `ABORT (voteA=${voteA}, voteB=${voteB}) → A=${a.bal} B=${b.bal} (không đổi)`;
}

// ---- SAGA: thực hiện ngay từng bước, fail thì chạy bước BÙ ----
function saga(amount: number, creditWillFail: boolean): string {
  const [a, b] = reset();
  const log: string[] = [];
  a.bal -= amount; log.push(`debit A (-${amount})`);           // bước 1: commit ngay
  if (creditWillFail) {
    a.bal += amount; log.push(`BÙ: refund A (+${amount})`);    // bù vì bước 2 hỏng
    return `[${log.join(" → ")}] → A=${a.bal} B=${b.bal} (đã hoàn nguyên)`;
  }
  b.bal += amount; log.push(`credit B (+${amount})`);
  return `[${log.join(" → ")}] → A=${a.bal} B=${b.bal}`;
}

console.log("Chuyển 30 từ A(100) sang B(0). Giữ bất biến: tổng LUÔN = 100.\n");
console.log("2PC — cả hai sẵn sàng :", twoPC(30, true));
console.log("2PC — B từ chối        :", twoPC(30, false));
console.log("SAGA — bước 2 OK       :", saga(30, false));
console.log("SAGA — bước 2 FAIL     :", saga(30, true));
console.log("\n2PC: atomic nhờ khoá+bỏ phiếu (chậm, kẹt nếu điều phối chết).");
console.log("SAGA: không khoá toàn cục, bù khi hỏng — nhanh/co giãn nhưng có");
console.log("cửa sổ KHÔNG nhất quán giữa bước 1 và bù (phải idempotent — Bài 7).");
```

Kết quả chạy thật *(tất định)*:

```
Chuyển 30 từ A(100) sang B(0). Giữ bất biến: tổng LUÔN = 100.

2PC — cả hai sẵn sàng : COMMIT → A=70 B=30
2PC — B từ chối        : ABORT (voteA=true, voteB=false) → A=100 B=0 (không đổi)
SAGA — bước 2 OK       : [debit A (-30) → credit B (+30)] → A=70 B=30
SAGA — bước 2 FAIL     : [debit A (-30) → BÙ: refund A (+30)] → A=100 B=0 (đã hoàn nguyên)

2PC: atomic nhờ khoá+bỏ phiếu (chậm, kẹt nếu điều phối chết).
SAGA: không khoá toàn cục, bù khi hỏng — nhanh/co giãn nhưng có
cửa sổ KHÔNG nhất quán giữa bước 1 và bù (phải idempotent — Bài 7).
```

Cả hai giữ được bất biến "tổng = 100", nhưng theo hai triết lý trái ngược. **2PC** không cho ai thấy trạng thái dở: hoặc commit (A=70, B=30) hoặc abort (không đổi) — atomicity thật, trả bằng khoá và một vòng bỏ phiếu. **Saga** *không khoá*: nó cứ debit A ngay (A=70 tức thì), và nếu credit B hỏng thì *bù lại* (refund → A=100). Khác biệt sống còn: giữa bước debit và bước bù, có một **cửa sổ** mà A đã bị trừ nhưng B chưa được cộng — hệ *tạm thời không nhất quán* (eventual, Bài 8). Vì bước bù có thể bị retry (Bài 7), mỗi bước saga **phải idempotent**. Đổi lại, saga không cần khoá toàn cục nên co giãn tốt ở quy mô microservice — nơi 2PC quá đắt hoặc bất khả.

> [!note] Tự thử
> - Cho `twoPC` có node thứ ba: chỉ cần *một* node vote no là abort tất cả — minh hoạ "all nodes must agree" (consensus). Thêm node = thêm xác suất abort + chậm hơn.
> - Trong `saga`, làm bước *bù* cũng fail: giờ bạn thấy vì sao saga thực tế phải retry bù đến cùng (hoặc báo người) — không có "roll back" tự động như 2PC.
> - Thêm bước 3 vào saga (credit phí cho C): fail ở bước 3 phải bù *cả* bước 2 và 1 theo thứ tự ngược — saga dài = chuỗi bù dài.

## 5. Bảng so sánh: 2PC vs saga

| Tiêu chí              | Two-phase commit (2PC)              | Saga (compensating)                      |
| :-------------------- | :---------------------------------- | :--------------------------------------- |
| Nguyên tắc            | khoá + bỏ phiếu, **atomic thật**    | làm ngay từng bước, **bù khi hỏng**      |
| Nhất quán             | mạnh (không ai thấy dở dang)        | eventual (có cửa sổ không nhất quán)     |
| Khoá                  | giữ khoá suốt giao dịch             | không khoá toàn cục                      |
| Điểm yếu              | chậm; **kẹt nếu điều phối chết**    | phải viết bước bù; cần idempotent (Bài 7) |
| Hợp cho               | vài node, cùng tin cậy, cần đúng tuyệt đối | microservice, nhiều service, quy mô lớn |
| Nền / AWS             | DynamoDB `TransactWriteItems`       | Step Functions / SQS+Lambda saga         |

Quy luật chọn (lại là đánh đổi quen thuộc của khoá): **2PC mua nhất quán mạnh bằng khoá + phối hợp; saga đổi nhất quán tức thời lấy co giãn và chịu lỗi.** Cùng họ với TCP/UDP (Bài 5), strong/eventual (Bài 8). Và cả hai đều dựng trên nền cũ: 2PC *là* consensus (Bài 9); saga *cần* idempotency (Bài 7) vì mỗi bước bù có thể bị retry.

## 6. Nối về AWS

> [!note] Nối về AWS
> "Nhất quán chéo-service" là một trong những bài toán khó nhất khi dựng hệ trên AWS — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) và [Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md):
> - **DynamoDB `TransactWriteItems` = 2PC trong một dịch vụ.** Ghi atomic tối đa 100 item: hoặc tất cả thành công, hoặc tất cả hỏng — đúng "atomic commit" của mục 3, DynamoDB lo consensus bên dưới. Giá: đắt gấp đôi WCU và giới hạn phạm vi (một region, một bảng-nhóm).
> - **Step Functions = saga orchestration.** Một state machine điều phối nhiều bước (gọi Lambda/service), và mỗi bước khai báo *Catch/bước bù* khi lỗi — đúng mô hình saga của demo: không khoá toàn cục, bù khi hỏng.
> - **SQS + Lambda = saga choreography.** Thay vì một điều phối trung tâm, các service phát/nghe event để tự chạy bước kế và bù — co giãn hơn nhưng khó theo dõi hơn. Vì at-least-once (Bài 7), **mỗi bước và mỗi bù phải idempotent**.
> - **Vì sao không "distributed transaction xuyên mọi service"?** Vì 2PC qua nhiều service/nhiều region quá chậm và dễ kẹt (điều phối chết → khoá treo). AWS đẩy bạn về saga đúng vì lý do DDIA nêu: distributed transaction mong manh ở quy mô lớn.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 16.1 — ACID là gì? Bốn chữ nối về bài nào trong khoá?
> **Đáp:** Atomicity, Consistency, Isolation, Durability. Durability = Bài 3 (ghi bền qua crash); Isolation = Bài 2 (chống race mức transaction); Atomicity = "all or nothing".

> [!question] Thẻ 16.2 — Atomicity theo DDIA định nghĩa bằng gì? Vì sao quan trọng cho retry?
> **Đáp:** **khả năng abort và vứt bỏ mọi ghi** của transaction khi lỗi. Vì vứt sạch "như chưa làm" nên ứng dụng **an toàn retry** (Bài 7).

> [!question] Thẻ 16.3 — Vì sao transaction trải nhiều node hoá thành bài toán consensus?
> **Đáp:** giao dịch có thể hỏng ở node này, thành công ở node kia. Giữ atomicity đòi **mọi node đồng ý** cùng commit hoặc cùng abort = atomic commit = consensus (Bài 9).

> [!question] Thẻ 16.4 — 2PC hoạt động ra sao? Điểm yếu chí mạng?
> **Đáp:** pha prepare (bỏ phiếu) → chỉ commit nếu *tất cả* yes, không thì abort hết. Yếu: chậm + giữ khoá + **kẹt nếu điều phối chết** giữa chừng.

> [!question] Thẻ 16.5 — Saga khác 2PC thế nào? Phải trả giá gì?
> **Đáp:** làm từng bước ngay, hỏng thì chạy **bước bù (compensating)** thay vì khoá toàn cục. Giá: có **cửa sổ không nhất quán** (eventual) và mỗi bước phải **idempotent**.

> [!question] Thẻ 16.6 — DynamoDB TransactWriteItems vs Step Functions saga: dùng khi nào?
> **Đáp:** TransactWriteItems = atomic trong một dịch vụ (vài item, cần đúng tuyệt đối). Step Functions saga = nhiều service/bước, co giãn, chấp nhận eventual + viết bước bù.

## 8. Câu hỏi tự kiểm tra

1. ACID gồm gì? Mỗi chữ nối về bài nào trong khoá? *(mục 1, tr. 223)*
2. DDIA định nghĩa atomicity thế nào? Vì sao nó cho phép retry an toàn? *(mục 2, tr. 224)*
3. Vì sao transaction nhiều node = atomic commit = consensus? *(mục 3, tr. 353)*
4. Mô tả 2PC. Vì sao "điều phối chết" là ác mộng? Liên hệ Bài 7/13. *(mục 3)*
5. Chạy demo mục 4. So cách 2PC và saga giữ bất biến "tổng = 100". Cửa sổ không nhất quán của saga nằm ở đâu? *(mục 4)*
6. Ánh xạ TransactWriteItems / Step Functions / SQS+Lambda vào 2PC/saga. Vì sao AWS đẩy về saga ở quy mô lớn? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 16 — DISTRIBUTED NÂNG CAO: TRANSACTION & SAGA
─────────────────────────────────────────────────────────
ACID  Atomicity·Consistency·Isolation·Durability (DDIA tr.223). Durability=
   Bài 3; Isolation=Bài 2; Atomicity="all or nothing".

ATOMICITY  = khả năng ABORT và vứt bỏ mọi ghi khi lỗi (tr.224) → retry an
   toàn (Bài 7). Một node: WAL (Bài 3) lo. Nhiều node: vỡ ra.

ATOMIC COMMIT = CONSENSUS  giao dịch có thể fail node này được node kia
   (tr.353) → phải bắt MỌI node đồng ý: cùng commit hoặc cùng abort (Bài 9).
   2PC: prepare(bỏ phiếu)→commit nếu tất cả yes. Chậm, KẸT nếu điều phối chết.

SAGA  làm từng bước ngay; hỏng → chạy bước BÙ (compensating). Không khoá
   toàn cục → co giãn, nhưng có CỬA SỔ không nhất quán (eventual) + mỗi bước
   phải idempotent (Bài 7).

DEMO  chuyển 30, tổng=100: 2PC commit(70/30) hoặc abort(không đổi). Saga
   debit→credit, bước 2 fail → refund (hoàn nguyên 100/0).

NỐI VỀ AWS  DynamoDB TransactWriteItems=2PC-trong-1-dịch-vụ; Step Functions
   =saga orchestration; SQS+Lambda=saga choreography (idempotent!). AWS đẩy
   về saga vì 2PC xuyên-service quá đắt/mong manh.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 7 (Transactions)**: ACID (tr. 223), atomicity = khả năng abort (tr. 224); **ch. 9 (Consistency and Consensus → Atomic Commit and Two-Phase Commit)**: atomic commit là consensus (tr. 353). Offset **PDF = tr. + 22**. *(Thuật ngữ "saga" là mẫu kiến trúc công nghiệp, không phải thuật ngữ nguyên văn DDIA — ở đây trình bày như hệ quả thực tiễn khi distributed transaction quá đắt.)*
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md), [Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md).
- Mở rộng của [Bài 2 — atomicity](bai_02_os-concurrency.md), [Bài 9 — consensus](bai_09_dist-phan-manh.md); saga cần [Bài 7 — idempotency](bai_07_dist-giao-tiep.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · **[Bài 16 — Distributed nâng cao: transaction & saga] ← bạn đang ở đây** · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
