# Bài 15 — Distributed nâng cao: Đồng hồ và thứ tự sự kiện

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 3 (Distributed).** [Bài 7](bai_07_dist-giao-tiep.md) nói mạng không đáng tin; bài này nói *thời gian* cũng không. Mỗi máy có đồng hồ riêng và chúng **lệch nhau** — nên dùng timestamp để quyết "ghi nào mới hơn" giữa nhiều máy là cái bẫy nuốt dữ liệu trong im lặng. Đây là nền để hiểu **vì sao DynamoDB/Cassandra LWW có thể mất ghi, vì sao Kinesis chỉ bảo đảm thứ tự *trong một shard*, và vì sao idempotency-key đáng tin hơn timestamp** ở `aws-fund`.
> Nguồn: **DDIA** — ch. 8 (Unreliable Clocks).
> **Trích:** `DDIA (tr. X)` = trang **in**; **offset PDF = tr. + 22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 7 — giao tiếp & thất bại](bai_07_dist-giao-tiep.md), [Bài 8 — nhân bản & nhất quán](bai_08_dist-nhat-quan.md).

## Mục lục

1. [Mỗi máy một đồng hồ, và nó lệch](#1-mỗi-máy-một-đồng-hồ-và-nó-lệch)
2. [Dùng timestamp để xếp thứ tự: cám dỗ nguy hiểm](#2-dùng-timestamp-để-xếp-thứ-tự-cám-dỗ-nguy-hiểm)
3. [Logical clock: đếm nhân quả thay vì đo giờ](#3-logical-clock-đếm-nhân-quả-thay-vì-đo-giờ)
4. [Demo: clock skew nuốt mất ghi mới](#4-demo-clock-skew-nuốt-mất-ghi-mới)
5. [Bảng so sánh: đồng hồ vật lý vs logical](#5-bảng-so-sánh-đồng-hồ-vật-lý-vs-logical)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mỗi máy một đồng hồ, và nó lệch

Trên một máy, "bây giờ" là một con số rõ ràng. Qua nhiều máy, không có "bây giờ" chung:

> [!quote] DDIA (tr. 287)
> "each machine on the network has its own clock, which is an actual hardware device: usually a quartz crystal oscillator. These devices are not perfectly accurate, so each machine has its own notion of time."
>
> *mỗi máy trên mạng có **đồng hồ riêng**, là một thiết bị phần cứng thật — thường là **bộ dao động thạch anh (quartz)**. Các thiết bị này **không chính xác tuyệt đối**, nên **mỗi máy có khái niệm thời gian riêng** (có thể nhanh/chậm hơn máy khác một chút).*

Quartz "trôi" (drift) — nhanh/chậm theo nhiệt độ, tuổi linh kiện. NTP (Network Time Protocol) kéo các đồng hồ về gần nhau, nhưng — nối thẳng Bài 5 — độ chính xác của NTP *bị chặn bởi round-trip time của mạng*: bạn không thể đồng bộ chính xác hơn độ trễ của chính cái mạng đang đo. Kết quả: hai máy luôn lệch nhau một ít, thường vài mili-giây, đôi khi hơn. Vài mili-giây nghe nhỏ, nhưng nó lớn hơn *nhiều* khoảng cách giữa hai sự kiện xảy ra "gần như đồng thời" — và đó là nơi tai hoạ bắt đầu.

## 2. Dùng timestamp để xếp thứ tự: cám dỗ nguy hiểm

> [!quote] DDIA (tr. 291)
> "Let's consider one particular situation in which it is tempting, but dangerous, to rely on clocks: ordering of events across multiple nodes. For example, if two clients write to a distributed database, who got there first? Which write is the more recent one?"
>
> *Hãy xét một tình huống **hấp dẫn nhưng nguy hiểm** khi dựa vào đồng hồ: **xếp thứ tự các sự kiện trên nhiều node**. Ví dụ, nếu hai client cùng ghi vào một database phân tán, ai tới trước? Ghi nào mới hơn?*

Cách "tự nhiên" là gắn timestamp cho mỗi ghi và giữ cái có timestamp lớn hơn — gọi là **last write wins (LWW)**. Nhưng vì đồng hồ lệch (mục 1), "timestamp lớn hơn" **không** đồng nghĩa "xảy ra sau":

> [!quote] DDIA (tr. 292)
> "Database writes can mysteriously disappear: a node with a lagging clock is unable to overwrite values previously written by a node with a fast clock until the clock skew between the nodes has elapsed [...] This scenario can cause arbitrary amounts of data to be silently dropped without any error being reported to the application."
>
> *Ghi vào database có thể **biến mất một cách bí ẩn**: một node có **đồng hồ chậm** không thể ghi đè giá trị mà một node có **đồng hồ nhanh** đã ghi trước đó, cho tới khi độ lệch đồng hồ giữa hai node trôi qua. Kịch bản này có thể khiến **một lượng dữ liệu tuỳ ý bị âm thầm vứt đi — không một lỗi nào báo cho ứng dụng**.*

Đây là loại lỗi tệ nhất: *im lặng*. Không exception, không log lỗi — chỉ là một ghi bạn tưởng đã thành công bỗng không còn, vì một node khác có đồng hồ nhanh hơn đã "thắng" dù nó ghi *trước* trong thời gian thực. Demo mục 4 dựng đúng kịch bản này.

## 3. Logical clock: đếm nhân quả thay vì đo giờ

Nếu đồng hồ vật lý không đáng tin để xếp thứ tự, dùng gì? Bỏ hẳn việc *đo giờ*, chuyển sang *đếm nhân quả*:

> [!quote] DDIA (tr. 293)
> "So-called logical clocks [...] which are based on incrementing counters rather than an oscillating quartz crystal, are a safer alternative for ordering events."
>
> *Cái gọi là **logical clock (đồng hồ logic)** — dựa trên **bộ đếm tăng dần** thay vì tinh thể thạch anh dao động — là lựa chọn **an toàn hơn để xếp thứ tự sự kiện**.*

Ý tưởng (Lamport): mỗi sự kiện tăng một bộ đếm; khi một node *nhận tin* từ node khác, nó đặt bộ đếm = `max(của mình, nhận được) + 1`. Nhờ đó, nếu sự kiện B *nhân quả sau* A (B xảy ra vì đã thấy A), thì counter của B **luôn** lớn hơn A — bất kể đồng hồ vật lý nói gì. Logical clock không trả lời "lúc mấy giờ" (nó vô nghĩa về thời gian thực), nhưng trả lời đúng câu ta *thật sự* cần: "cái nào nhân quả trước cái nào". Đây chính là nền của version vector / "detecting concurrent writes" mà DynamoDB và các DB leaderless dùng thay cho LWW thuần.

## 4. Demo: clock skew nuốt mất ghi mới

Dựng đúng kịch bản DDIA: node1 đồng hồ *nhanh* (+100), node2 *chậm* (−100). Thực tế ghi `x=1` (t=1) *trước*, rồi `x=2` (t=2) *sau* (và B đã thấy A → nhân quả sau). LWW theo đồng hồ vật lý vs theo Lamport.

```typescript
// Đồng hồ phân tán nói dối: mỗi máy một quartz lệch (DDIA tr.287). Dùng
// timestamp vật lý để XẾP THỨ TỰ ghi là "tempting but dangerous" (tr.291):
// last-write-wins theo đồng hồ lệch có thể IM LẶNG vứt mất ghi mới (tr.292).
// Logical clock (bộ đếm Lamport) xếp theo NHÂN QUẢ nên an toàn (tr.293).
type Write = { value: number; physicalTs: number; lamport: number };

// hai node, đồng hồ lệch nhau: node1 CHẠY NHANH (+100), node2 CHẠY CHẬM (-100)
const skew: Record<string, number> = { node1: +100, node2: -100 };
function physicalClock(node: string, realTime: number): number { return realTime + skew[node]; }

// Lamport: mỗi sự kiện tăng bộ đếm; nhận tin thì lấy max(local, nhận)+1
let lamport = 0;
function tick(observed = 0): number { lamport = Math.max(lamport, observed) + 1; return lamport; }

// real-time: A ghi x=1 TRƯỚC (t=1); sau khi thấy A, B ghi x=2 SAU (t=2)
const wA: Write = { value: 1, physicalTs: physicalClock("node1", 1), lamport: tick() };
const wB: Write = { value: 2, physicalTs: physicalClock("node2", 2), lamport: tick(wA.lamport) }; // B thấy A

const pick = (by: (w: Write) => number, label: string) => {
  const winner = [wA, wB].reduce((a, b) => (by(a) >= by(b) ? a : b));
  console.log(`  LWW theo ${label.padEnd(16)} → giữ x=${winner.value}`);
  return winner.value;
};
console.log(`Thực tế: ghi x=1 (t=1) TRƯỚC, rồi ghi x=2 (t=2) SAU. Đáp án đúng = 2.\n`);
console.log(`  ts vật lý: x=1 → ${wA.physicalTs}, x=2 → ${wB.physicalTs}  (x=2 nhỏ hơn vì node2 chậm!)`);
console.log(`  lamport : x=1 → ${wA.lamport}, x=2 → ${wB.lamport}\n`);
const byPhysical = pick(w => w.physicalTs, "ĐỒNG HỒ VẬT LÝ");
const byLamport  = pick(w => w.lamport,    "LAMPORT");
console.log(`\n  đồng hồ vật lý: ${byPhysical === 2 ? "đúng" : "SAI → mất ghi x=2 (im lặng!)"}`);
console.log(`  lamport       : ${byLamport === 2 ? "đúng (tôn trọng nhân quả)" : "sai"}`);
```

Kết quả chạy thật *(tất định)*:

```
Thực tế: ghi x=1 (t=1) TRƯỚC, rồi ghi x=2 (t=2) SAU. Đáp án đúng = 2.

  ts vật lý: x=1 → 101, x=2 → -98  (x=2 nhỏ hơn vì node2 chậm!)
  lamport : x=1 → 1, x=2 → 2

  LWW theo ĐỒNG HỒ VẬT LÝ   → giữ x=1
  LWW theo LAMPORT          → giữ x=2

  đồng hồ vật lý: SAI → mất ghi x=2 (im lặng!)
  lamport       : đúng (tôn trọng nhân quả)
```

`x=2` xảy ra *sau* trong thời gian thực và *nhân quả sau* (B đã thấy A), nhưng vì node2 có đồng hồ chậm, timestamp vật lý của nó (−98) *nhỏ hơn* của `x=1` (101). LWW theo đồng hồ vật lý giữ `x=1` và **vứt mất `x=2`** — đúng "silently dropped without any error" của mục 2. Logical clock đếm nhân quả nên `x=2` có lamport `2 > 1` → giữ đúng. Bài học: **đừng dùng timestamp của đồng hồ tường để quyết thứ tự nhân quả giữa các máy** — dùng bộ đếm logic, version, hoặc một nguồn thứ tự tập trung (một leader, một shard).

> [!note] Tự thử
> - Đặt `skew` của hai node bằng 0 (đồng hồ hoàn hảo): đồng hồ vật lý *tình cờ* ra đúng. Đó là bẫy — nó "chạy đúng trên máy bạn" rồi sập khi đồng hồ production lệch (giống race condition Bài 2!).
> - Cho B *không* thấy A (ghi `lamport: tick()` không truyền `wA.lamport`): hai ghi thành *concurrent* theo Lamport (không ai nhân quả trước) — đúng lúc cần version vector để phát hiện xung đột thay vì chọn bừa.
> - Đổi skew để node2 nhanh hơn: giờ đồng hồ vật lý *tình cờ* đúng — minh hoạ kết quả phụ thuộc may rủi của độ lệch, tức là *bất định* (Bài 7).

## 5. Bảng so sánh: đồng hồ vật lý vs logical

| Tiêu chí              | Đồng hồ vật lý (time-of-day)       | Logical clock (Lamport/version)       |
| :-------------------- | :--------------------------------- | :------------------------------------ |
| Đo cái gì             | thời gian thực (giờ, phút)         | **thứ tự nhân quả** (ai trước ai)     |
| Nguồn                 | quartz + NTP (lệch, drift)         | bộ đếm tăng dần                       |
| Xếp thứ tự giữa máy   | **KHÔNG đáng tin** (skew)          | đáng tin cho quan hệ nhân quả         |
| Dùng đúng cho         | hiển thị giờ, TTL, log người đọc   | giải xung đột ghi, versioning         |
| Cạm bẫy               | LWW mất ghi im lặng                | không cho biết "mấy giờ", concurrent phải xử lý riêng |

Quy luật: **đồng hồ tường trả lời "mấy giờ", logical clock trả lời "cái nào trước" — đừng lẫn hai câu hỏi.** Dùng timestamp vật lý để *hiển thị* và *hết hạn (TTL)* thì ổn; dùng nó để *quyết ai thắng* giữa các máy thì nguy hiểm. Đây là một mặt khác của cùng bài học Bài 7: trong hệ phân tán, thứ bạn tưởng chắc chắn (thời gian, "đồng thời") lại là thứ bất định nhất.

## 6. Nối về AWS

> [!note] Nối về AWS
> "Đừng tin timestamp phân tán" là bài học ngầm sau nhiều hành vi AWS — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) và [Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md):
> - **DynamoDB & LWW:** ghi có điều kiện (conditional write, Bài 2) và version number an toàn hơn "ghi đè theo giờ". Nếu bạn tự làm "last write wins" bằng một thuộc tính timestamp *client sinh*, bạn đang đặt bom hẹn giờ đúng mục 2 — hai client lệch đồng hồ sẽ nuốt ghi của nhau.
> - **Kinesis chỉ bảo đảm thứ tự *trong một shard*.** Vì không có đồng hồ toàn cục, thứ tự tổng trên nhiều shard là *không xác định*. Muốn thứ tự cho một thực thể → dùng cùng **partition key** để nó rơi vào một shard (một "nguồn thứ tự" tập trung — mục 5).
> - **Idempotency-key > timestamp.** Khi khử trùng lặp (Bài 7), dùng **khoá định danh** (order-id) chứ đừng dùng "cùng timestamp" — hai sự kiện có thể trùng giờ, hoặc một sự kiện mang giờ sai.
> - **Đừng xếp log theo timestamp xuyên host.** CloudWatch gộp log từ nhiều máy; sắp theo timestamp để suy luận nhân quả "A gây ra B" là sai nếu hai máy lệch đồng hồ. Dùng trace-id / request-id (một dạng thứ tự nhân quả) để nối sự kiện.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 15.1 — Vì sao không có "bây giờ" chung giữa các máy?
> **Đáp:** mỗi máy có đồng hồ quartz riêng, không chính xác tuyệt đối, **trôi (drift)**; NTP chỉ kéo gần nhau nhưng bị chặn bởi round-trip của mạng → luôn lệch một ít.

> [!question] Thẻ 15.2 — Vì sao LWW theo timestamp vật lý nguy hiểm?
> **Đáp:** "timestamp lớn hơn" ≠ "xảy ra sau" vì đồng hồ lệch. Node đồng hồ nhanh "thắng" node chậm dù ghi trước → ghi mới bị **vứt im lặng, không báo lỗi**.

> [!question] Thẻ 15.3 — Logical clock đo gì? Vì sao an toàn hơn để xếp thứ tự?
> **Đáp:** đo **thứ tự nhân quả** bằng bộ đếm tăng dần (không đo giờ). Nếu B nhân quả sau A thì counter B > A luôn đúng, bất kể đồng hồ vật lý.

> [!question] Thẻ 15.4 — Dùng đồng hồ vật lý cho việc gì thì ổn, việc gì thì không?
> **Đáp:** ổn: hiển thị giờ, TTL/hết hạn, log cho người đọc. KHÔNG ổn: quyết "ghi nào thắng" / thứ tự nhân quả giữa nhiều máy.

> [!question] Thẻ 15.5 — Trong demo, vì sao x=2 bị mất dù ghi sau?
> **Đáp:** node2 (ghi x=2) có đồng hồ chậm → ts vật lý −98 < 101 của x=1 → LWW giữ x=1. Lamport (2>1) giữ đúng x=2.

> [!question] Thẻ 15.6 — Vì sao Kinesis chỉ bảo đảm thứ tự trong một shard? Cách lấy thứ tự cho một thực thể?
> **Đáp:** không có đồng hồ toàn cục nên thứ tự xuyên shard không xác định. Dùng cùng **partition key** để các sự kiện của một thực thể vào cùng một shard (nguồn thứ tự tập trung).

## 8. Câu hỏi tự kiểm tra

1. Vì sao mỗi máy có "khái niệm thời gian riêng"? NTP giới hạn bởi gì? *(mục 1, tr. 287)*
2. Vì sao xếp thứ tự sự kiện bằng đồng hồ là "tempting but dangerous"? *(mục 2, tr. 291)*
3. LWW theo timestamp vật lý gây hại ra sao? Vì sao "im lặng" là tệ nhất? *(mục 2, tr. 292)*
4. Logical clock là gì? Vì sao đáng tin hơn cho thứ tự? *(mục 3, tr. 293)*
5. Chạy demo mục 4. Giải thích vì sao x=2 mất với đồng hồ vật lý nhưng được giữ với Lamport. *(mục 4)*
6. Ba hệ quả AWS của "đừng tin timestamp phân tán" (DynamoDB LWW, Kinesis shard, idempotency-key)? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 15 — DISTRIBUTED NÂNG CAO: ĐỒNG HỒ & THỨ TỰ SỰ KIỆN
─────────────────────────────────────────────────────────
ĐỒNG HỒ LỆCH  mỗi máy một quartz riêng, không chính xác, TRÔI (DDIA tr.287).
   NTP kéo gần nhưng bị chặn bởi round-trip mạng (Bài 5) → luôn lệch.

XẾP THỨ TỰ BẰNG TIMESTAMP  "tempting but dangerous" (tr.291). LWW: node
   đồng hồ NHANH thắng node chậm dù ghi trước → ghi mới bị VỨT IM LẶNG,
   không báo lỗi (tr.292). Lỗi tệ nhất vì không thấy.

LOGICAL CLOCK  bộ đếm tăng dần, đo NHÂN QUẢ không đo giờ (tr.293). B nhân
   quả sau A ⇒ counter B > A luôn đúng. Nền của version vector / DynamoDB.

DEMO  node2 (x=2, ghi SAU) đồng hồ chậm → ts −98 < 101 của x=1 → LWW vật lý
   giữ x=1 (SAI, mất x=2). Lamport 2>1 → giữ x=2 (đúng).

QUY LUẬT  đồng hồ tường = "mấy giờ" (hiển thị/TTL ok); logical = "cái nào
   trước" (giải xung đột). ĐỪNG LẪN hai câu hỏi.

NỐI VỀ AWS  DynamoDB: version/conditional write > LWW-theo-giờ; Kinesis thứ
   tự chỉ TRONG shard (cùng partition key); idempotency-KEY > timestamp;
   đừng xếp log xuyên-host theo timestamp (dùng trace-id).
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 8 (The Trouble with Distributed Systems → Unreliable Clocks)**: mỗi máy đồng hồ riêng & drift (tr. 287), "tempting but dangerous" xếp thứ tự (tr. 291), LWW mất ghi im lặng (tr. 292), logical clocks (tr. 293). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md), [Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md).
- Mở rộng của [Bài 7 — thất bại](bai_07_dist-giao-tiep.md) và [Bài 8 — nhất quán](bai_08_dist-nhat-quan.md); idempotency nối [Bài 2](bai_02_os-concurrency.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · **[Bài 15 — Distributed nâng cao: đồng hồ] ← bạn đang ở đây** · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
