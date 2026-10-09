# Bài 0 — Phương pháp system design trên AWS, và bản đồ khoá

> [!info] Về khoá này
> Khoá **`aws-design`** là **tầng đỉnh** của ba khoá: học **giải bài toán thiết kế hệ thống thật trên AWS**. Khác hai khoá trước (bám *chương sách*), khoá này bám **VẤN ĐỀ**: mỗi bài là một *archetype* ("thiết kế X ở quy mô") — ước lượng → kiến trúc → đào sâu một sub-problem khó → lab → soi qua Well-Architected.
> Ba tầng: [`cloud-base`](../../cloud-base/README.md) (*vì sao* — nền CS) → [`aws-fund`](../../aws-fund/README.md) (*cái gì* — dịch vụ) → **`aws-design`** (*làm sao cho đúng* — bài toán thật).
> Nguồn (Luật số 1 — không viết theo trí nhớ):
> - **WA** — *AWS Well-Architected Framework* (whitepaper chính thức, `tai_lieu/`, trích `WA (tr. X)`, PDF = tr. + 5) — lăng kính đánh đổi.
> - **BL** — *Amazon Builders' Library* (bài kỹ thuật thật của kỹ sư Amazon, lưu `tai_lieu/bl_*.txt`, trích `BL: <slug>`) — deep-dive problem-solving.
> **Chạy lab:** cần **Docker + LocalStack + awslocal** (như `aws-fund`); demo khái niệm bằng **Node 22+** chạy thẳng `.ts`.

## Mục lục

1. [Vì sao system design trên AWS khó](#1-vì-sao-system-design-trên-aws-khó)
2. [Quy trình sáu bước](#2-quy-trình-sáu-bước)
3. [Demo: ước lượng back-of-envelope](#3-demo-ước-lượng-back-of-envelope)
4. [Well-Architected: lăng kính sáu trụ](#4-well-architected-lăng-kính-sáu-trụ)
5. [Cách học khoá này và bản đồ 8 archetype](#5-cách-học-khoá-này-và-bản-đồ-8-archetype)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Vì sao system design trên AWS khó

> [!example] Buổi phỏng vấn (hoặc buổi họp sáng thứ Hai)
> Người phỏng vấn nói: *"Thiết kế cho tôi một dịch vụ rút gọn URL cho 100 triệu người dùng."* Một câu, không thêm gì. Bạn biết EC2, DynamoDB, S3, Lambda... nhưng *bắt đầu từ đâu*? Vẽ ngay sơ đồ hộp-mũi-tên? Chọn DynamoDB vì "nghe nói nó scale tốt"? Đó là **thiết kế bằng cảm giác** — và nó sập ngay khi người phỏng vấn hỏi "100 triệu user thì bao nhiêu request mỗi giây?". Khoá này dạy bạn trả lời câu đó *trước*, rồi để con số chọn kiến trúc giùm.

Biết *có dịch vụ gì* (aws-fund) và *vì sao nó thế* (cloud-base) chưa đủ để thiết kế một hệ thật. Thiết kế là **ghép** chúng dưới ràng buộc mâu thuẫn (nhanh vs rẻ vs bền vs đơn giản) — và nền của mọi ràng buộc là: hệ phân tán vốn khó:

> [!quote] BL: challenges-with-distributed-systems
> "Developing distributed utility computing services, such as reliable long-distance telephone networks, or Amazon Web Services (AWS) services, is hard. Distributed computing is also weirder and less intuitive than other forms of computing because of two interrelated problems."
>
> *Xây các dịch vụ điện toán phân tán — như mạng điện thoại đường dài tin cậy, hay các dịch vụ AWS — là **khó**. Điện toán phân tán còn **kỳ quặc và kém trực giác** hơn các dạng tính toán khác, vì hai vấn đề đan nhau* (thất bại độc lập và tính bất định — chính là [cloud-base Bài 7](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md)).

Vì khó và phản trực giác, "thiết kế bằng cảm giác" thất bại. Cần một *quy trình* biến bài toán mơ hồ thành quyết định có cơ sở — mục 2.

## 2. Quy trình sáu bước

Mọi bài trong khoá đi theo đúng sáu bước này (và đây cũng là khung trả lời một câu hỏi system-design interview):

```
1. LÀM RÕ YÊU CẦU   chức năng (làm gì) + phi chức năng (QPS, p99, nhất quán, chi phí)
2. ƯỚC LƯỢNG        back-of-envelope: writes/s, reads/s, dung lượng, băng thông
3. VẼ KIẾN TRÚC     API → compute → data; ghép dịch vụ AWS (aws-fund)
4. TÌM NÚT THẮT     chỗ nào vỡ trước khi scale? (thường: hot partition, 1 DB, đồng bộ)
5. ĐÀO SÂU 1 VẤN ĐỀ giải sub-problem khó nhất (trích BL) — nền ở cloud-base
6. SOI ĐÁNH ĐỔI     review qua 6 trụ Well-Architected; nêu rõ cái được/mất
```

Bước **2 (ước lượng)** là bản lề mà người mới hay bỏ: không có con số thì không biết "cache có cần không", "một DB đủ không". Demo mục 3 cho thấy con số *tự quyết* phần lớn kiến trúc.

## 3. Demo: ước lượng back-of-envelope

> [!example] Như kỹ sư cầu đường tính nhẩm trước khi vẽ
> Trước khi vẽ bản thiết kế chi tiết, kỹ sư cầu đường *nhẩm nhanh*: cầu dài bao nhiêu, bao nhiêu xe/ngày, mỗi xe nặng cỡ nào → ra tải trọng cần chịu → loại ngay các vật liệu không kham nổi. Họ không cần con số chính xác tới kg, chỉ cần **đúng bậc độ lớn** để khỏi vẽ một cây cầu gỗ cho xe tải. Back-of-envelope trong system design y hệt: vài phép nhân trên "mảnh giấy" loại bỏ các kiến trúc sai *trước khi* tốn công vẽ.

Biến yêu cầu mơ hồ ("làm URL shortener cho 100 triệu user") thành con số, rồi đọc kiến trúc *ra từ* con số:

```typescript
// System design bắt đầu bằng ƯỚC LƯỢNG back-of-envelope: biến yêu cầu mơ hồ
// thành CON SỐ (QPS, dung lượng, băng thông) để chọn kiến trúc có cơ sở.
// Ví dụ: một dịch vụ rút gọn URL.
const DAU = 100_000_000;          // người dùng hoạt động/ngày
const WRITES_PER_USER_DAY = 0.1;  // mỗi người tạo 0.1 link/ngày
const READ_WRITE_RATIO = 100;     // đọc nhiều gấp 100 lần ghi
const PEAK_FACTOR = 3;            // giờ cao điểm gấp 3 trung bình
const BYTES_PER_RECORD = 500;     // mỗi bản ghi ~500 byte
const YEARS = 5;

const SEC_PER_DAY = 86_400;
const writesDay = DAU * WRITES_PER_USER_DAY;
const writesSec = writesDay / SEC_PER_DAY;
const readsSec = writesSec * READ_WRITE_RATIO;
const peakReadsSec = readsSec * PEAK_FACTOR;
const records5yr = writesDay * 365 * YEARS;
const storageTB = (records5yr * BYTES_PER_RECORD) / 1e12;
const readBwMBs = (peakReadsSec * BYTES_PER_RECORD) / 1e6;

const f = (n: number) => n.toLocaleString("en", { maximumFractionDigits: 1 });
console.log("URL shortener — ước lượng back-of-envelope:");
console.log(`  ghi:            ${f(writesSec)} writes/s  (trung bình)`);
console.log(`  đọc:            ${f(readsSec)} reads/s  →  cao điểm ${f(peakReadsSec)} reads/s`);
console.log(`  dung lượng 5 năm: ${f(records5yr/1e9)} tỷ bản ghi ≈ ${f(storageTB)} TB`);
console.log(`  băng thông đọc đỉnh: ${f(readBwMBs)} MB/s`);
console.log(`\nKết luận thiết kế rút ra TỪ số:`);
console.log(`  • đọc >> ghi (${READ_WRITE_RATIO}:1) → CACHE là bắt buộc (tầng đọc).`);
console.log(`  • ${f(peakReadsSec)} reads/s → KV store scale ngang (DynamoDB), không RDBMS đơn.`);
console.log(`  • ${f(storageTB)} TB → phải phân mảnh (partition key rải đều).`);
```

Kết quả chạy thật *(tất định)*:

```
URL shortener — ước lượng back-of-envelope:
  ghi:            115.7 writes/s  (trung bình)
  đọc:            11,574.1 reads/s  →  cao điểm 34,722.2 reads/s
  dung lượng 5 năm: 18.3 tỷ bản ghi ≈ 9.1 TB
  băng thông đọc đỉnh: 17.4 MB/s

Kết luận thiết kế rút ra TỪ số:
  • đọc >> ghi (100:1) → CACHE là bắt buộc (tầng đọc).
  • 34,722.2 reads/s → KV store scale ngang (DynamoDB), không RDBMS đơn.
  • 9.1 TB → phải phân mảnh (partition key rải đều).
```

Để ý: ba kết luận kiến trúc *không phải ý kiến* mà **suy ra từ con số**. Tỉ lệ đọc/ghi 100:1 ép tầng cache (Bài 1); 35k reads/s đỉnh loại RDBMS đơn, đòi KV scale ngang (Bài 1); 9 TB đòi phân mảnh (Bài 1–2). Ước lượng không cần chính xác — nó cần đúng *bậc độ lớn* để loại các lựa chọn sai. Đây là kỹ năng số một của system design, và mọi archetype sau đều mở đầu bằng nó.

> [!note] Tự thử
> - Đổi `READ_WRITE_RATIO` về `2` (đọc ít): cache còn bắt buộc không? Thấy ước lượng *đổi kết luận* ra sao.
> - Tăng `BYTES_PER_RECORD` lên `50_000` (lưu cả ảnh preview): dung lượng vọt → gợi ý tách blob sang S3 (Bài 6). Số dẫn dắt quyết định.
> - Thêm `p99 < 50ms` vào yêu cầu phi chức năng: kết hợp với "mạng ~triệu lần chậm hơn RAM" (cloud-base Bài 0) → vì sao cache gần người dùng.

## 4. Well-Architected: lăng kính sáu trụ

Sau khi có một thiết kế, cần soi nó qua một khung chuẩn để lộ chỗ đánh đổi dở. AWS có khung chính thức:

> [!quote] WA (tr. 1)
> "The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS."
>
> *Khung **AWS Well-Architected** giúp bạn **hiểu được cái được và cái mất** của những quyết định khi xây hệ trên AWS.*

Nó gồm sáu trụ — sáu góc nhìn để chất vấn mọi thiết kế:

> [!quote] WA (tr. 2)
> "The AWS Well-Architected Framework is based on six pillars — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability."
>
> *Khung dựa trên **sáu trụ**: xuất sắc vận hành, bảo mật, **độ tin cậy**, **hiệu năng**, **tối ưu chi phí**, và bền vững.*

Khoá dùng sáu trụ như **checklist cuối mỗi bài**: thiết kế này *reliable* chưa (chịu lỗi vùng?), *performant* chưa (p99?), *cost-optimized* chưa (có trả thừa?), *secure* chưa (ai truy cập được?). Một thiết kế "chạy được" mà trượt vài trụ là một thiết kế sẽ gây sự cố production. Mỗi archetype sẽ chỉ rõ nó mạnh/yếu ở trụ nào.

## 5. Cách học khoá này và bản đồ 8 archetype

Tám bài, mỗi bài một archetype kinh điển. Mỗi bài đào sâu **một** sub-problem khó (trích Builders' Library), neo vào nền cloud-base và dịch vụ aws-fund, và chạy lab LocalStack nơi được:

| # | Thiết kế | Sub-problem đào sâu | Nguồn deep-dive |
| :-- | :-- | :-- | :-- |
| 1 | [URL shortener](bai_01_url-shortener.md) | partition key, hot key, cache | WA Performance |
| 2 | [Rate limiter](bai_02_rate-limiter.md) | token bucket, **load shedding** | BL: load-shedding |
| 3 | [Newsfeed / fan-out](bai_03_newsfeed-fanout.md) | fan-out-on-write vs read | WA + aws-fund |
| 4 | [Hệ thông báo tin cậy](bai_04_he-thong-bao.md) | **retry + backoff + jitter**, DLQ | BL: timeouts-retries |
| 5 | [Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) | **idempotent API**, conditional write | BL: idempotent-apis |
| 6 | [Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) | presigned URL, event-driven, **queue backlog** | BL: queue-backlogs |
| 7 | [Chịu traffic spike](bai_07_chiu-tai-overload.md) | **shuffle sharding**, tránh fallback | BL: shuffle-sharding |
| 8 | [Đa vùng & DR](bai_08_da-vung-dr.md) | static stability, failover, RTO/RPO | WA Reliability |

Cách học hiệu quả: **tự ước lượng trước khi đọc đáp án**; **gõ lại lab**; và mỗi khi gặp "nối về nền", mở lại bài cloud-base/aws-fund tương ứng — đó là lúc ba khoá khớp thành một.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 0.1 — Khoá aws-design khác hai khoá trước ở trục tổ chức nào?
> **Đáp:** bám **VẤN ĐỀ** (archetype "thiết kế X"), không bám chương sách. Là tầng đỉnh: cloud-base (vì sao) → aws-fund (cái gì) → aws-design (làm sao cho đúng).

> [!question] Thẻ 0.2 — Sáu bước của quy trình system design?
> **Đáp:** làm rõ yêu cầu → ước lượng → vẽ kiến trúc → tìm nút thắt → đào sâu 1 vấn đề → soi đánh đổi (Well-Architected).

> [!question] Thẻ 0.3 — Vì sao bước ước lượng quan trọng? Cần chính xác không?
> **Đáp:** con số *tự quyết* kiến trúc (cache? scale ngang? phân mảnh?). Chỉ cần đúng **bậc độ lớn** để loại lựa chọn sai, không cần chính xác.

> [!question] Thẻ 0.4 — Well-Architected là gì, gồm mấy trụ?
> **Đáp:** khung hiểu **pros/cons** của quyết định trên AWS; **sáu trụ**: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability.

> [!question] Thẻ 0.5 — Trong demo, vì sao kết luận "cần cache" không phải ý kiến?
> **Đáp:** suy ra từ tỉ lệ đọc/ghi 100:1 — đọc áp đảo nên phải có tầng đọc nhanh (cache). Con số dẫn dắt, không phải cảm tính.

## 7. Câu hỏi tự kiểm tra

1. Vì sao "biết dịch vụ" chưa đủ để thiết kế hệ? Distributed khó vì hai vấn đề gì? *(mục 1, BL)*
2. Liệt kê sáu bước. Bước nào người mới hay bỏ, hậu quả? *(mục 2)*
3. Chạy demo mục 3. Đổi read/write ratio và giải thích kết luận kiến trúc đổi theo. *(mục 3)*
4. Well-Architected để làm gì? Kể sáu trụ và một câu hỏi mỗi trụ đặt ra. *(mục 4, WA tr. 1–2)*
5. Vì sao ước lượng chỉ cần đúng bậc độ lớn? *(mục 3)*

## Tóm tắt một trang

```
BÀI 0 — PHƯƠNG PHÁP SYSTEM DESIGN TRÊN AWS
─────────────────────────────────────────────────────────
TẦNG ĐỈNH  cloud-base (vì sao) → aws-fund (cái gì) → aws-design (làm sao).
   Bám VẤN ĐỀ (archetype), không bám chương. Distributed vốn KHÓ (BL).

6 BƯỚC  1 làm rõ yêu cầu (chức năng + phi chức năng: QPS/p99/nhất quán/chi phí)
   2 ƯỚC LƯỢNG (bản lề!) 3 vẽ kiến trúc 4 tìm nút thắt 5 đào sâu 1 vấn đề
   6 soi 6 trụ Well-Architected.

ƯỚC LƯỢNG  con số TỰ QUYẾT kiến trúc. Demo URL shortener: đọc/ghi 100:1 →
   cache bắt buộc; 35k reads/s → KV scale ngang; 9TB → phân mảnh. Chỉ cần
   đúng BẬC ĐỘ LỚN.

WELL-ARCHITECTED  khung hiểu PROS/CONS (WA tr.1); 6 trụ: operational
   excellence, security, reliability, performance, cost, sustainability (tr.2).
   Dùng làm checklist cuối mỗi bài.

8 ARCHETYPE  URL shortener · rate limiter · newsfeed · hệ thông báo · thanh
   toán idempotent · upload ảnh · chịu spike · đa vùng DR.
```

## Nguồn

- **AWS Well-Architected Framework** (whitepaper, AWS, bản 2024-11) — pros/cons (tr. 1), sáu trụ (tr. 2). `tai_lieu/AWS-Well-Architected-Framework.pdf` — **offset PDF = tr. + 5**.
- **Amazon Builders' Library** — *Challenges with distributed systems* (Jacob Gabrielson): distributed là hard, weirder, less intuitive. `tai_lieu/bl_challenges-with-distributed-systems.txt`.
- Ba tầng: [`cloud-base`](../../cloud-base/README.md), [`aws-fund`](../../aws-fund/README.md), và README khoá này.

---

**Bản đồ khoá học:** **[Bài 0 — Phương pháp system design] ← bạn đang ở đây** · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
