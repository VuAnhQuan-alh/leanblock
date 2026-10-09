# Bài 2 — OS trụ 1b: Concurrency (thread, race condition, atomicity)

> [!info] Về bài này
> **Trụ 1 (OS), mảnh 2/3: concurrency (đồng thời).** [Bài 1](bai_01_os-ao-hoa.md) cho mỗi process một address space riêng — cách ly. Bài này đi ngược lại: khi nhiều **thread** cố ý *chia sẻ* một address space để cùng làm việc, chia sẻ đó sinh ra một lớp lỗi mới — **race condition** — và ta cần **atomicity** để chế ngự. Đây là nền của *mọi* bug "chạy lúc được lúc không" và là gốc của **idempotency / conditional write** bạn gặp ở `aws-fund`.
> Nguồn: **OSTEP** — chương 26 (Concurrency: An Introduction).
> **Trích:** `OSTEP (tr. X)` = trang **in**; **offset PDF = tr. + 25**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 1 — ảo hoá](bai_01_os-ao-hoa.md).

## Mục lục

1. [Thread: nhiều điểm thực thi, chung một address space](#1-thread-nhiều-điểm-thực-thi-chung-một-address-space)
2. [Race condition: khi chia sẻ gặp luân phiên](#2-race-condition-khi-chia-sẻ-gặp-luân-phiên)
3. [Critical section và atomicity: tất cả hoặc không gì](#3-critical-section-và-atomicity-tất-cả-hoặc-không-gì)
4. [Demo: đo lost update bằng con số](#4-demo-đo-lost-update-bằng-con-số)
5. [Bảng so sánh: ba cách chế ngự race](#5-bảng-so-sánh-ba-cách-chế-ngự-race)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Thread: nhiều điểm thực thi, chung một address space

Ở Bài 1, một process có **một** điểm thực thi (một program counter). Một **thread** phá vỡ điều đó: một process có thể có nhiều thread, mỗi thread là một dòng thực thi riêng — nhưng tất cả **dùng chung** address space của process.

> [!quote] OSTEP (tr. 286)
> "Perhaps another way to think of this is that each thread is very much like a separate process, except for one difference: they share the same address space and thus can access the same data."
>
> *Có thể nghĩ thế này: mỗi **thread** rất giống một process riêng, trừ **một khác biệt**: chúng **dùng chung cùng một address space** và do đó truy cập được **cùng dữ liệu**.*

Chính "một khác biệt" đó vừa là sức mạnh vừa là mối nguy. Vì sao ta muốn thread? OSTEP nêu hai lý do, và cả hai đều vang vọng ở tầng cloud:

> [!quote] OSTEP (tr. 288)
> "threads share an address space and thus make it easy to share data, and hence are a natural choice when constructing these types of programs. Processes are a more sound choice for logically separate tasks where little sharing of data structures in memory is needed."
>
> *thread dùng chung address space nên **chia sẻ dữ liệu dễ dàng**, là lựa chọn tự nhiên cho loại chương trình này. Còn **process** hợp hơn cho các tác vụ **tách biệt về mặt logic**, nơi gần như không cần chia sẻ cấu trúc dữ liệu trong bộ nhớ.*

Hai lý do dùng thread: **parallelism** (chia việc cho nhiều lõi — đúng giới hạn time-sharing của Bài 1) và **tránh block vì I/O chậm** (một thread chờ mạng/đĩa thì thread khác vẫn chạy — nối tới trạng thái BLOCKED ở Bài 1 và tới TCP ở Bài 5). Nhưng "truy cập cùng dữ liệu" mở ra cánh cửa cho lỗi khó nhất nghề.

## 2. Race condition: khi chia sẻ gặp luân phiên

Giả sử hai thread cùng chạy `counter = counter + 1`. Trông như *một* thao tác, nhưng CPU thực thi nó bằng **ba** bước: (1) nạp `counter` vào thanh ghi, (2) cộng 1, (3) ghi lại. Nhớ từ Bài 1: OS có thể **context switch** bất kỳ lúc nào — kể cả *giữa* ba bước đó. Nếu thread B chen vào sau khi A đã nạp nhưng chưa ghi, cả hai cùng nạp giá trị cũ, cùng ghi `+1`, và **một lần tăng biến mất**.

> [!quote] OSTEP (tr. 295)
> "What we have demonstrated here is called a race condition (or, more specifically, a data race): the results depend on the timing execution of the code. With some bad luck (i.e., context switches that occur at untimely points in the execution), we get the wrong result."
>
> *Thứ ta vừa thấy gọi là **race condition** (cụ thể hơn: **data race**): kết quả **phụ thuộc vào thời điểm** các lệnh chạy. Gặp xui (context switch rơi vào điểm oái oăm), ta nhận **kết quả sai**.*

Điều đáng sợ nhất không phải "sai", mà là "lúc đúng lúc sai":

> [!quote] OSTEP (tr. 295)
> "we may get a different result each time; thus, instead of a nice deterministic computation (which we are used to from computers), we call this result indeterminate, where it is not known what the output will be and it is indeed likely to be different across runs."
>
> *ta có thể ra **kết quả khác nhau mỗi lần**; thay vì một tính toán **tất định** quen thuộc, kết quả này là **bất định (indeterminate)** — không biết output sẽ ra gì, và rất dễ khác nhau giữa các lần chạy.*

Đây là lý do race condition là loại bug ám ảnh: nó qua được mọi test trên máy bạn, rồi sập lúc 3 giờ sáng trên production dưới tải cao — vì chỉ khi đó context switch mới rơi đúng điểm oái oăm.

## 3. Critical section và atomicity: tất cả hoặc không gì

Đoạn code đụng tới dữ liệu chung ấy có tên riêng, và cách chữa cũng có tên riêng.

> [!quote] OSTEP (tr. 295)
> "A critical section is a piece of code that accesses a shared variable (or more generally, a shared resource) and must not be concurrently executed by more than one thread."
>
> *Một **critical section** (vùng tới hạn) là đoạn code truy cập **biến dùng chung** (tổng quát hơn: **tài nguyên dùng chung**) và **không được** để nhiều hơn một thread chạy đồng thời.*

Cách chế ngự là làm cho critical section trở nên **atomic** — không thể chia cắt:

> [!quote] OSTEP (tr. 296)
> "The idea behind making a series of actions atomic is simply expressed with the phrase "all or nothing"; it should either appear as if all of the actions you wish to group together occurred, or that none of them occurred, with no in-between state visible."
>
> *Ý tưởng làm một chuỗi hành động trở nên **atomic** gói gọn trong "**tất cả hoặc không gì**" (all or nothing): hoặc **trông như cả nhóm đã xảy ra**, hoặc **chẳng cái nào xảy ra** — không để lộ trạng thái dở dang ở giữa.*

Và đây là cây cầu quý giá nhất của bài — OSTEP tự nối "atomicity" sang khái niệm bạn sẽ gặp ở trụ Dữ liệu và ở AWS:

> [!quote] OSTEP (tr. 296)
> "Sometimes, the grouping of many actions into a single atomic action is called a transaction, an idea developed in great detail in the world of databases and transaction processing"
>
> *Đôi khi, gom nhiều hành động thành **một hành động atomic** được gọi là **transaction** — ý tưởng được phát triển rất chi tiết trong thế giới cơ sở dữ liệu và xử lý giao dịch.*

Cùng một ý tưởng — "all or nothing" — chạy xuyên suốt: từ một lệnh CPU, lên tới một transaction DynamoDB, ra tới retry của một hàng đợi phân tán (Bài 7–8). Nắm nó ở đây, ba nơi kia tự sáng.

## 4. Demo: đo lost update bằng con số

Lý thuyết nói "một lần tăng biến mất". Hãy đếm xem mất **bao nhiêu**. 8 thread cùng tăng một biến chung 100.000 lần mỗi thread; kỳ vọng 800.000. Ta chạy hai kiểu: `counter = counter + 1` (ba bước rời, racy) và `Atomics.add` (một thao tác không chia cắt, atomic).

```typescript
// Concurrency: nhiều thread CHIA SẺ address space → cùng ghi một biến →
// race condition. Dòng "counter++" thực ra là 3 bước (đọc-cộng-ghi); OS có
// thể chen context switch vào giữa → mất cập nhật (lost update).
import { Worker, isMainThread, workerData } from "node:worker_threads";

const THREADS = 8;
const PER_THREAD = 100_000;

if (!isMainThread) {
  const view = new Int32Array(workerData.buf as SharedArrayBuffer);
  const mode = workerData.mode as "racy" | "atomic";
  for (let i = 0; i < PER_THREAD; i++) {
    if (mode === "atomic") {
      Atomics.add(view, 0, 1);          // đọc-cộng-ghi KHÔNG thể bị chen
    } else {
      view[0] = view[0] + 1;            // 3 bước rời → có thể mất cập nhật
    }
  }
} else {
  function run(mode: "racy" | "atomic"): Promise<number> {
    const buf = new SharedArrayBuffer(4);
    const view = new Int32Array(buf);
    view[0] = 0;
    return new Promise((resolve) => {
      let left = THREADS;
      for (let i = 0; i < THREADS; i++) {
        const w = new Worker(new URL(import.meta.url), { workerData: { buf, mode } });
        w.on("exit", () => { if (--left === 0) resolve(view[0]); });
      }
    });
  }
  const main = async (): Promise<void> => {
    const expected = THREADS * PER_THREAD;
    const racy = await run("racy");
    const atomic = await run("atomic");
    console.log(`${THREADS} thread, mỗi thread +1 × ${PER_THREAD.toLocaleString("en")} lần`);
    console.log(`Kỳ vọng ĐÚNG                 : ${expected.toLocaleString("en")}`);
    console.log(`"counter = counter + 1" (racy): ${racy.toLocaleString("en")}  ← mất ${(expected - racy).toLocaleString("en")} lần cập nhật!`);
    console.log(`Atomics.add (atomic)         : ${atomic.toLocaleString("en")}  ← đúng`);
    console.log(`\nRace: bước đọc-cộng-ghi bị context switch chen vào giữa.`);
    console.log(`(Số "racy" tuỳ lần chạy — luôn < kỳ vọng. Atomic luôn đúng.)`);
  };
  main();
}
```

Kết quả chạy thật *(con số "racy" **tuỳ lần chạy** — bản chất của indeterminate; điều chắc chắn: nó luôn `<` 800.000, còn atomic luôn đúng 800.000)*:

```
8 thread, mỗi thread +1 × 100,000 lần
Kỳ vọng ĐÚNG                 : 800,000
"counter = counter + 1" (racy): 592,996  ← mất 207,004 lần cập nhật!
Atomics.add (atomic)         : 800,000  ← đúng

Race: bước đọc-cộng-ghi bị context switch chen vào giữa.
(Số "racy" tuỳ lần chạy — luôn < kỳ vọng. Atomic luôn đúng.)
```

Mất hơn **200 nghìn** cập nhật — không phải lỗi hiếm gặp, mà là *mặc định* khi chia sẻ không bảo vệ. Và chạy lại sẽ ra con số khác: đó chính là "indeterminate" của mục 2, sờ được bằng tay. `Atomics.add` sửa triệt để vì nó biến ba bước thành một thao tác "all or nothing" đúng như định nghĩa mục 3.

> [!note] Tự thử
> - Giảm `PER_THREAD` còn `1_000`: race *vẫn* xảy ra nhưng số mất ít hơn và thất thường hơn — đây là lý do race "qua được test nhẹ" rồi sập dưới tải nặng.
> - Đổi `THREADS = 1`: racy và atomic bằng nhau — **không chia sẻ cùng lúc thì không có race**. (Chính là chiến lược "không chia sẻ" ở bảng mục 5.)
> - Thử thay `Atomics.add` bằng đọc rồi `Atomics.store(view,0, view[0]+1)`: race quay lại — vì *đọc* và *ghi* lại tách làm hai thao tác atomic rời, khe hở mở lại.

## 5. Bảng so sánh: ba cách chế ngự race

Khi có dữ liệu chung, có ba chiến lược gốc. Mọi công cụ (mutex, atomic, actor, hàng đợi, conditional write của DB) đều là biến thể của một trong ba:

| Chiến lược            | Ý tưởng                                        | Giá phải trả                        | Ví dụ nền / AWS                               |
| :-------------------- | :--------------------------------------------- | :---------------------------------- | :-------------------------------------------- |
| **Khoá (lock/mutex)** | chỉ 1 thread vào critical section mỗi lúc      | chậm lại, nguy cơ deadlock          | mutex OS; DynamoDB *pessimistic* lock         |
| **Atomic op**         | gộp đọc-sửa-ghi thành 1 thao tác không chia cắt | chỉ hợp thao tác nhỏ, đơn giản      | `Atomics.add`; DynamoDB `ADD` / atomic counter |
| **Không chia sẻ**     | mỗi thread/worker giữ dữ liệu riêng, gộp sau   | phải thiết kế lại luồng dữ liệu     | process tách biệt (Bài 1); sharding (Bài 9)   |

Quy luật ngầm: **race chỉ sinh ra khi có (a) dữ liệu chung + (b) ghi đồng thời.** Bỏ một trong hai là hết race. Khoá và atomic bỏ (b) (tuần tự hoá việc ghi); "không chia sẻ" bỏ (a). Ghi nhớ cặp điều kiện này — ở trụ Distributed, "dữ liệu chung" biến thành *replica trên nhiều máy* và câu chuyện lặp lại y hệt ở quy mô lớn hơn.

## 6. Nối về AWS

> [!note] Nối về AWS
> Trên một máy, race là chuyện giữa các thread. Trên cloud, *mạng + retry* biến **mọi** hệ phân tán thành một bài toán concurrency khổng lồ — xem [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md):
> - **Idempotency** = phiên bản distributed của atomicity. SQS giao **at-least-once** → cùng một message có thể tới *hai lần*; nếu handler "cộng tiền" không idempotent, bạn cộng đôi — đúng kiểu *lost/duplicate update* của mục 2, chỉ là nguyên nhân là *retry mạng* thay vì *context switch*.
> - **DynamoDB conditional write / atomic counter** (`ADD`, `ConditionExpression`) = chính xác "atomic op" ở bảng mục 5, nâng lên mức một hàng trong DB phân tán: đọc-sửa-ghi gói thành một thao tác "all or nothing" phía server, nên hai client đua nhau không ghi đè nhau.
> - **Optimistic concurrency** (version number + conditional update) là cách cả DynamoDB lẫn RDS tránh khoá: thay vì chặn trước (pessimistic lock), cho cả hai thử rồi *từ chối* kẻ đến sau nếu version đã đổi — "race nhưng phát hiện và quay lại".
> - Vì sao OSTEP nối atomicity với **transaction** (tr. 296) đáng nhớ: transaction của DynamoDB/RDS chính là "all or nothing" của mục 3, phóng lên nhiều hàng/nhiều bảng. Một ý tưởng, ba tầng (CPU → DB → distributed).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 2.1 — Thread khác process ở điểm cốt lõi nào?
> **Đáp:** thread giống process nhưng **dùng chung address space** (cùng dữ liệu). Đó vừa là sức mạnh (chia sẻ dễ) vừa là nguồn race condition.

> [!question] Thẻ 2.2 — Vì sao `counter = counter + 1` không an toàn với nhiều thread?
> **Đáp:** nó là **3 bước** (đọc-cộng-ghi); context switch có thể chen vào giữa → hai thread cùng đọc giá trị cũ → mất một lần tăng (lost update).

> [!question] Thẻ 2.3 — "Indeterminate" nghĩa là gì, và vì sao nó làm race khó debug?
> **Đáp:** kết quả **khác nhau mỗi lần chạy**, phụ thuộc thời điểm context switch. Qua được test nhẹ, sập dưới tải nặng → khó tái hiện.

> [!question] Thẻ 2.4 — Critical section là gì? Chữa bằng tính chất gì?
> **Đáp:** đoạn code truy cập tài nguyên chung, không được 2 thread chạy đồng thời. Chữa bằng **atomicity** ("all or nothing": cả nhóm xảy ra, hoặc không gì, không lộ trạng thái giữa).

> [!question] Thẻ 2.5 — Hai điều kiện để có race? Bỏ cái nào thì hết?
> **Đáp:** (a) dữ liệu chung + (b) ghi đồng thời. Khoá/atomic bỏ (b); "không chia sẻ" bỏ (a). Bỏ một trong hai là hết race.

> [!question] Thẻ 2.6 — Idempotency trên AWS nối về khái niệm nền nào, và vì sao cần?
> **Đáp:** = atomicity ở mức distributed. SQS at-least-once → message tới >1 lần; handler idempotent đảm bảo xử lý lặp không gây hiệu ứng kép (giống chống lost/duplicate update).

## 8. Câu hỏi tự kiểm tra

1. Định nghĩa thread theo OSTEP. "Một khác biệt" với process là gì và vì sao nó nguy hiểm? *(mục 1, tr. 286)*
2. Giải thích từng bước vì sao `counter++` của 2 thread có thể mất cập nhật. *(mục 2)*
3. "Race condition" và "indeterminate" khác nhau thế nào? *(mục 2, tr. 295)*
4. Phát biểu "all or nothing". Vì sao OSTEP nối nó với "transaction"? *(mục 3, tr. 296)*
5. Chạy demo mục 4. Vì sao số racy đổi mỗi lần, còn atomic thì không? *(mục 4)*
6. Ánh xạ ba chiến lược (khoá/atomic/không-chia-sẻ) sang ba cơ chế AWS. Vì sao SQS cần handler idempotent? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 2 — OS TRỤ 1b: CONCURRENCY (thread · race · atomicity)
─────────────────────────────────────────────────────────
THREAD  giống process nhưng DÙNG CHUNG address space (cùng dữ liệu).
   Dùng vì: parallelism + tránh block khi I/O chậm (nối BLOCKED Bài 1).

RACE CONDITION  "counter = counter+1" = 3 bước (đọc-cộng-ghi).
   Context switch chen vào giữa → LOST UPDATE. Kết quả INDETERMINATE
   (khác nhau mỗi lần) → bug 3h sáng, qua test nhẹ sập tải nặng.

CRITICAL SECTION  đoạn đụng dữ liệu chung, cấm 2 thread cùng vào.
ATOMICITY  "all or nothing" (OSTEP tr.296). OSTEP tự nối → TRANSACTION.

DEMO  8 thread × 100k: racy mất ~200k cập nhật (tuỳ lần);
   Atomics.add → đúng 800k mọi lần.

2 ĐIỀU KIỆN RACE  (a) dữ liệu chung + (b) ghi đồng thời.
   Khoá/atomic bỏ (b); không-chia-sẻ bỏ (a).

NỐI VỀ AWS  idempotency = atomicity distributed (SQS at-least-once →
   message tới 2 lần); DynamoDB conditional write/atomic counter = atomic
   op phía server; optimistic concurrency = "race nhưng phát hiện".
```

## Nguồn

- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **chương 26 (Concurrency: An Introduction)**: định nghĩa thread (tr. 286, 288), race condition & indeterminate & critical section (tr. 295), atomicity "all or nothing" & transaction (tr. 296). `tai_lieu/Operating systems three easy pieces.pdf` — **offset PDF = tr. + 25**.
- Nối về AWS: [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md) (SQS at-least-once, idempotency, DynamoDB conditional write).
- Tiếp: [Bài 3 — lưu trữ (persistence)](bai_03_os-luu-tru.md) khép lại ba mảnh OS; "all or nothing" sẽ trở lại ở [Bài 8 — nhất quán](bai_08_dist-nhat-quan.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · **[Bài 2 — OS: concurrency] ← bạn đang ở đây** · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
