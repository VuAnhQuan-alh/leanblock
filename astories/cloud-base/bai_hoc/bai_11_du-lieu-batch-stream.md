# Bài 11 — Dữ liệu trụ 4b: Batch và stream (và khép bốn trụ)

> [!info] Về bài này
> **Trụ 4 (Dữ liệu), mảnh 2/2 — bài cuối của khoá.** [Bài 10](bai_10_du-lieu-storage.md) lo *lưu* dữ liệu; bài này lo *xử lý* nó ở quy mô, theo hai kiểu đối ngẫu: **batch** (dữ liệu hữu hạn, xử lý một mẻ) và **stream** (dữ liệu tới dần, xử lý liên tục). Hiểu cặp này là hiểu linh hồn của **Kinesis, SQS/Lambda event-driven, DynamoDB Streams, và S3 + Athena/EMR** ở `aws-fund` — và nó đóng lại mạch "append-log" chạy suốt từ Bài 3.
> Nguồn: **DDIA** (ch. 10 Batch Processing, ch. 11 Stream Processing).
> **Trích:** `DDIA (tr. X)` offset **+22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 10 — storage engine/append-log](bai_10_du-lieu-storage.md), [Bài 3 — journaling](bai_03_os-luu-tru.md).

## Mục lục

1. [Batch: input hữu hạn, một đáp số](#1-batch-input-hữu-hạn-một-đáp-số)
2. [Stream: dữ liệu tới dần, không bao giờ xong](#2-stream-dữ-liệu-tới-dần-không-bao-giờ-xong)
3. [Event: mẩu tin bất biến, chính là một log](#3-event-mẩu-tin-bất-biến-chính-là-một-log)
4. [Demo: batch vs stream trên cùng dữ liệu](#4-demo-batch-vs-stream-trên-cùng-dữ-liệu)
5. [Bảng so sánh: batch vs stream](#5-bảng-so-sánh-batch-vs-stream)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Khép bốn trụ](#khép-bốn-trụ)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Batch: input hữu hạn, một đáp số

Xử lý batch (theo mẻ) — như MapReduce — dựa trên một giả định nền:

> [!quote] DDIA (tr. 438)
> "the input is bounded—i.e., of a known and finite size—so the batch process knows when it has finished reading its input. For example, the sorting operation that is central to MapReduce must read its entire input before it can start producing output."
>
> *input là **bounded (hữu hạn)** — tức có kích thước **biết trước và hữu hạn** — nên tiến trình batch **biết khi nào đã đọc xong** input. Ví dụ, thao tác sắp xếp (trung tâm của MapReduce) phải **đọc toàn bộ input trước** khi bắt đầu sinh output.*

Đặc trưng của batch: nó *chờ gom đủ* rồi mới tính, và cho ra **một đáp số đầy đủ** trên toàn tập. Hợp cho báo cáo cuối ngày, huấn luyện mô hình, tính hoá đơn tháng — nơi độ trễ vài phút/giờ chấp nhận được, đổi lại kết quả *toàn cục và chính xác*. Nhưng rất nhiều dữ liệu thực tế **không** hữu hạn — nó cứ tới mãi.

## 2. Stream: dữ liệu tới dần, không bao giờ xong

> [!quote] DDIA (tr. 439)
> "In this chapter we will look at event streams as a data management mechanism: the unbounded, incrementally processed counterpart to the batch data we saw in the last chapter."
>
> *Chương này nhìn **event stream** như một cơ chế quản lý dữ liệu: bản đối ngẫu **unbounded (vô hạn), xử lý tăng dần** của dữ liệu batch ở chương trước.*

Và định nghĩa gọn của chính "stream":

> [!quote] DDIA (tr. 440)
> "In general, a "stream" refers to data that is incrementally made available over time."
>
> *Nói chung, **"stream" chỉ dữ liệu được làm sẵn (available) một cách tăng dần theo thời gian**.*

Khác biệt cốt tử: stream **không có điểm kết thúc** để chờ. Người dùng hôm qua sinh dữ liệu, hôm nay vẫn sinh, mai vẫn sinh. Vì thế xử lý stream không thể "đọc hết rồi tính" như batch — nó phải xử lý **từng sự kiện khi tới**, giữ một trạng thái chạy, và cho ra kết quả "*tới thời điểm này*". Đổi lại độ trễ thấp (phản ứng gần tức thời) lấy việc mất đi "đáp số toàn cục cuối cùng". Demo mục 4 đặt hai kiểu cạnh nhau trên cùng dữ liệu.

## 3. Event: mẩu tin bất biến, chính là một log

Đơn vị của stream là **event**, và định nghĩa của nó khép lại mạch chạy suốt khoá:

> [!quote] DDIA (tr. 440)
> "In a stream processing context, a record is more commonly known as an event, but it is essentially the same thing: a small, self-contained, immutable object containing the details of something that happened at some point in time."
>
> *Trong ngữ cảnh stream processing, một **record** thường được gọi là **event**, nhưng về bản chất là một thứ: một **đối tượng nhỏ, tự chứa, BẤT BIẾN**, chứa chi tiết của **một việc đã xảy ra tại một thời điểm**.*

Hai chữ **immutable (bất biến)** là chìa khoá. Một event không bị sửa — nó chỉ được *nối thêm*. Nghĩa là một event stream *chính là* một **append-only log** (Bài 10) phát lại theo thời gian — và append-log ấy cũng chính là ý tưởng journaling của Bài 3. Một ý tưởng duy nhất — *ghi thêm, không sửa chỗ cũ* — hoá ra là xương sống của crash recovery (Bài 3), của storage engine LSM (Bài 10), và của stream processing (bài này). Vì event bất biến, ta có thể **phát lại** (replay) cả log để tính lại từ đầu — nền tảng của khả năng tái lập và sửa sai trong hệ dữ liệu.

## 4. Demo: batch vs stream trên cùng dữ liệu

Cùng một dãy "sự kiện đơn hàng" bất biến, xử lý hai kiểu: batch (đọc hết 5 sự kiện rồi tính tổng một lần) và stream (cập nhật tổng sau mỗi sự kiện).

```typescript
// Batch vs stream trên CÙNG dữ liệu (một dãy "sự kiện đơn hàng" bất biến).
//  - BATCH: input BOUNDED (hữu hạn, biết trước) → đọc HẾT rồi mới ra 1 kết quả.
//  - STREAM: input UNBOUNDED → xử lý TỪNG sự kiện khi nó tới, ra kết quả "tới giờ".
// Event = "small, self-contained, immutable object" (DDIA tr.440) → chính là
// một bản ghi append-log (Bài 10) được phát lại.
type Event = { id: number; amount: number };
const events: Event[] = [
  { id: 1, amount: 30 }, { id: 2, amount: 10 }, { id: 3, amount: 50 },
  { id: 4, amount: 20 }, { id: 5, amount: 40 },
];

// --- BATCH: phải có TOÀN BỘ input mới tính được (MapReduce đọc hết rồi sort) ---
function batchTotal(all: Event[]): number {
  let sum = 0;
  for (const e of all) sum += e.amount;   // chỉ đúng khi 'all' đã đầy đủ
  return sum;
}
console.log("BATCH (chờ đủ 5 sự kiện rồi mới tính):");
console.log(`   → tổng doanh thu = ${batchTotal(events)}   (một kết quả, sau khi đọc HẾT)\n`);

// --- STREAM: cập nhật trạng thái sau MỖI sự kiện, phát kết quả "tới thời điểm này" ---
console.log("STREAM (xử lý từng sự kiện khi nó tới):");
let runningTotal = 0;
for (const e of events) {
  runningTotal += e.amount;               // trạng thái tăng dần, không chờ ai
  console.log(`   sự kiện #${e.id} (+${e.amount}) → tổng tới giờ = ${runningTotal}`);
}

// Tính bất biến + phát lại: chạy lại trên cùng log cho cùng kết quả (reproducible)
console.log(`\nPhát lại cùng log → cùng tổng = ${batchTotal(events)} (event bất biến ⇒ tái lập được).`);
console.log("Batch: trễ cao, 1 đáp số đầy đủ. Stream: trễ thấp, đáp số 'tới giờ', không bao giờ 'xong'.");
```

Kết quả chạy thật *(tất định)*:

```
BATCH (chờ đủ 5 sự kiện rồi mới tính):
   → tổng doanh thu = 150   (một kết quả, sau khi đọc HẾT)

STREAM (xử lý từng sự kiện khi nó tới):
   sự kiện #1 (+30) → tổng tới giờ = 30
   sự kiện #2 (+10) → tổng tới giờ = 40
   sự kiện #3 (+50) → tổng tới giờ = 90
   sự kiện #4 (+20) → tổng tới giờ = 110
   sự kiện #5 (+40) → tổng tới giờ = 150

Phát lại cùng log → cùng tổng = 150 (event bất biến ⇒ tái lập được).
Batch: trễ cao, 1 đáp số đầy đủ. Stream: trễ thấp, đáp số 'tới giờ', không bao giờ 'xong'.
```

Cả hai ra `150`, nhưng *khi nào* và *thế nào* thì khác hẳn. Batch chỉ nói được gì **sau khi đọc hết** — nếu dòng sự kiện vô hạn, nó chẳng bao giờ bắt đầu được. Stream cho con số *sau mỗi sự kiện* (30, 40, 90, ...), hữu dụng để cảnh báo/hiển thị tức thời, nhưng mỗi con số chỉ là "tới giờ này". Và vì event **bất biến**, phát lại cùng log luôn ra cùng kết quả — đây là lý do kiến trúc event-sourcing có thể *tính lại* lịch sử khi logic đổi.

> [!note] Tự thử
> - Thêm **cửa sổ (window)**: in tổng của mỗi 2 sự kiện liên tiếp (tumbling window) — khái niệm chỉ có ở stream, batch không cần vì nó thấy toàn tập.
> - Giả lập unbounded: bọc vòng lặp stream trong `setInterval` sinh event ngẫu nhiên (seed cố định) — thấy rõ "không bao giờ xong", và vì sao stream cần quản lý trạng thái cẩn thận.
> - Phát lại log tới *sự kiện #3* rồi dừng: tái hiện trạng thái quá khứ (time-travel) — sức mạnh của log bất biến mà một bảng "cập nhật tại chỗ" (B-tree, Bài 10) không có.

## 5. Bảng so sánh: batch vs stream

| Tiêu chí          | Batch                                | Stream                                   |
| :---------------- | :----------------------------------- | :--------------------------------------- |
| Input             | **bounded** (hữu hạn, biết trước)    | **unbounded** (tới dần, vô hạn)          |
| Khi nào ra kết quả | sau khi đọc **hết** input            | sau **mỗi** sự kiện ("tới giờ này")      |
| Độ trễ            | cao (phút/giờ)                       | thấp (gần tức thời)                      |
| Loại kết quả      | đáp số **toàn cục**, đầy đủ          | trạng thái chạy, **tăng dần**            |
| Hợp cho           | báo cáo, ETL, huấn luyện mô hình     | cảnh báo, dashboard, phản ứng sự kiện    |
| Nền / AWS         | S3 + **Athena/EMR/Glue**             | **Kinesis**, SQS/Lambda, DynamoDB Streams |

Điểm hợp nhất đẹp đẽ (DDIA nhấn mạnh): **batch và stream không đối địch — chúng là hai cách đọc cùng một log sự kiện bất biến.** Batch = đọc toàn bộ log một lần; stream = theo đuôi log khi nó mọc thêm. Chọn theo yêu cầu độ trễ, không phải theo "công nghệ thời thượng". Đây là lần cuối cùng ta gặp chủ đề đánh đổi của khoá: *toàn cục+trễ cao vs cục bộ+trễ thấp*, cùng họ với TCP/UDP (Bài 5) và strong/eventual (Bài 8).

## 6. Nối về AWS

> [!note] Nối về AWS
> Kiến trúc dữ liệu của AWS chia đúng theo trục batch/stream — xem [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md) và [Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **Stream:** **Kinesis Data Streams** là "event stream" của mục 2 ở dạng managed — một log phân mảnh (Bài 9!), nhiều consumer đọc độc lập theo đuôi. **SQS + Lambda** và **DynamoDB Streams** là xử-lý-từng-sự-kiện của demo: mỗi sự kiện kích một hàm, cập nhật trạng thái, độ trễ thấp.
> - **Batch:** **S3 + Athena / EMR / Glue** là MapReduce của mục 1: dữ liệu *bounded* nằm trong S3 (data lake), quét toàn bộ để ra báo cáo. Chấp nhận độ trễ, đổi lấy đáp số toàn cục.
> - **Event bất biến = append-log:** S3 object không sửa tại chỗ (PUT tạo bản mới — Bài 3), DynamoDB Streams/Kinesis chỉ nối thêm. Vì bất biến, bạn **phát lại** được: tái xử lý lịch sử khi logic đổi, hoặc dựng lại trạng thái từ đầu (event sourcing).
> - **Một log, hai cách đọc:** mẫu phổ biến là Kinesis vừa feed xử-lý-thời-gian-thực (stream, Lambda) vừa đổ vào S3 cho phân tích-theo-mẻ (batch, Athena) — đúng "hai cách đọc cùng một log" của mục 5.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 11.1 — Giả định nền của xử lý batch? Hệ quả?
> **Đáp:** input **bounded** (hữu hạn, biết trước) → biết khi nào đọc xong → phải đọc HẾT mới ra kết quả (vd. MapReduce sort). Đáp số toàn cục nhưng trễ cao.

> [!question] Thẻ 11.2 — "Stream" là gì? Khác batch ở điểm cốt tử nào?
> **Đáp:** dữ liệu được làm sẵn **tăng dần theo thời gian**, input **unbounded** — không có điểm kết thúc để chờ. Phải xử lý từng sự kiện khi tới, ra kết quả "tới giờ".

> [!question] Thẻ 11.3 — "Event" theo DDIA là gì? Chữ nào quan trọng nhất?
> **Đáp:** đối tượng **nhỏ, tự chứa, BẤT BIẾN (immutable)** mô tả một việc đã xảy ra tại một thời điểm. "Immutable" là chìa khoá → stream = append-log phát lại được.

> [!question] Thẻ 11.4 — Vì sao event bất biến cho phép "phát lại"? Ích gì?
> **Đáp:** không sửa, chỉ nối → chạy lại cùng log cho cùng kết quả (tái lập). Ích: tính lại khi logic đổi, dựng lại trạng thái (event sourcing), time-travel.

> [!question] Thẻ 11.5 — Batch và stream đối địch nhau? Phát biểu hợp nhất?
> **Đáp:** không — **hai cách đọc cùng một log bất biến**: batch đọc toàn bộ một lần; stream theo đuôi khi log mọc. Chọn theo độ trễ cần.

> [!question] Thẻ 11.6 — Kinesis, S3+Athena, DynamoDB Streams — cái nào batch, cái nào stream?
> **Đáp:** Kinesis & DynamoDB Streams = stream (event, độ trễ thấp); S3+Athena/EMR = batch (bounded, quét toàn bộ, đáp số toàn cục).

## 8. Câu hỏi tự kiểm tra

1. Giả định "bounded input" của batch là gì? Vì sao MapReduce phải đọc hết trước? *(mục 1, tr. 438)*
2. "Stream" là gì? Vì sao không thể xử lý stream kiểu "đọc hết rồi tính"? *(mục 2, tr. 439–440)*
3. Định nghĩa "event". "Immutable" dẫn tới khả năng gì, và nối về Bài 3/Bài 10 ra sao? *(mục 3, tr. 440)*
4. Chạy demo mục 4. Vì sao batch không chạy được trên input vô hạn còn stream thì được? *(mục 4)*
5. Vì sao "batch và stream là hai cách đọc cùng một log"? Chọn giữa chúng dựa vào gì? *(mục 5)*
6. Ánh xạ Kinesis / S3+Athena / DynamoDB Streams vào batch/stream. Mẫu "một log, hai cách đọc" trên AWS? *(mục 6)*

## Khép bốn trụ

Bạn vừa đi hết vòng. Nhìn lại, cả khoá chỉ kể **một câu chuyện**, và nó lặp ở mọi tầng:

- **Trụ 1 (OS):** ảo hoá bán *ảo giác độc chiếm* một tài nguyên khan hiếm; chia sẻ sinh ra race; append-log (journaling) cứu dữ liệu khỏi crash.
- **Trụ 2 (Mạng):** phân tầng là abstraction; mỗi kết nối tốn round-trip; latency (không phải bandwidth) là nút thắt → đưa dữ liệu lại gần.
- **Trụ 3 (Distributed):** mạng sẽ hỏng → không phân biệt được chậm/chết → retry+idempotency; nhiều bản sao → CAP; chia để scale → consensus bằng quorum.
- **Trụ 4 (Dữ liệu):** storage engine đánh đổi đọc/ghi (B-tree/LSM); batch/stream là hai cách đọc cùng một log bất biến.

Và **một sợi chỉ** xuyên cả bốn: *mọi đảm bảo mạnh đều mua bằng phối hợp/chi phí, và nới lỏng đổi lấy tốc độ/sẵn sàng* — atomicity, TCP, strong consistency, B-tree đứng một đầu; eventual, UDP, LSM, stream đứng đầu kia. Thêm một sợi nữa: *append-only, bất biến* — từ journaling (Bài 3) tới LSM (Bài 10) tới event stream (Bài 11). Nắm hai sợi chỉ này, bạn **không** còn học AWS như học thuộc danh mục dịch vụ; bạn *suy ra* được vì sao mỗi dịch vụ hành xử như nó hành xử. Đó là toàn bộ mục đích của khoá nền này — quay lại [`aws-fund`](../../aws-fund/README.md), bạn sẽ thấy nó sáng ra.

## Tóm tắt một trang

```
BÀI 11 — DỮ LIỆU TRỤ 4b: BATCH & STREAM (+ khép 4 trụ)
─────────────────────────────────────────────────────────
BATCH  input BOUNDED (hữu hạn, biết trước, tr.438) → đọc HẾT rồi ra 1 đáp
   số TOÀN CỤC. Trễ cao. MapReduce. Hợp: báo cáo, ETL, train model.

STREAM  input UNBOUNDED, "data incrementally made available over time"
   (tr.440). Không có điểm kết thúc → xử lý TỪNG sự kiện, kết quả "tới giờ".
   Trễ thấp. Hợp: cảnh báo, dashboard, phản ứng sự kiện.

EVENT  "small, self-contained, IMMUTABLE object" (tr.440). Bất biến ⇒
   stream = APPEND-LOG (Bài 3 journaling, Bài 10 LSM) phát lại ⇒ tái lập.

DEMO  cùng 5 sự kiện: batch ra 150 sau khi đọc hết; stream ra 30→40→90→
   110→150 từng bước. Vô hạn thì batch bó tay, stream vẫn chạy.

HỢP NHẤT  batch & stream = HAI CÁCH ĐỌC CÙNG MỘT LOG bất biến. Chọn theo
   độ trễ. Cùng họ đánh đổi TCP/UDP, strong/eventual.

NỐI VỀ AWS  stream = Kinesis/SQS+Lambda/DynamoDB Streams; batch = S3+
   Athena/EMR/Glue; event bất biến = append-log (phát lại); 1 log 2 cách đọc.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 10 (Batch Processing)**: bounded input (tr. 438); **ch. 11 (Stream Processing)**: unbounded counterpart (tr. 439), định nghĩa stream & event bất biến (tr. 440). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md) (Kinesis, SQS, DynamoDB Streams), [Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (S3 data lake).
- **Hết khoá `cloud-base`.** Quay lại [`aws-fund`](../../aws-fund/README.md) để thấy nền vừa học làm mỗi dịch vụ sáng ra, hoặc đọc [Bài 0](bai_00_vi-sao-nen-tang.md) lần nữa với con mắt đã khác.

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · **[Bài 11 — Dữ liệu: batch & stream] ← bạn đang ở đây**

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
