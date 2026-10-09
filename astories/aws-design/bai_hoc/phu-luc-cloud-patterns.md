# Phụ lục — Từ điển pattern kiến trúc cloud (Wilder)

> [!info] Về phụ lục này
> *Cloud Architecture Patterns* (Bill Wilder, O'Reilly 2012) đặt **tên gọi chuẩn** cho 11 pattern kiến trúc cloud — những pattern mà khoá này đã *dùng và mô tả* nhưng chưa *gọi tên chính thức*. Phụ lục này **ánh xạ 11 pattern ↔ bài/khái niệm đã học**, kèm **định nghĩa nguyên văn** của tác giả cho từng pattern, để bạn có từ vựng chung khi đọc tài liệu/phỏng vấn.
> Điểm đắt: sách **platform-agnostic** (ví dụ gốc bằng Windows **Azure, 2012**) mà các pattern vẫn trùng khít với AWS 2026 — bằng chứng sống cho luận điểm xuyên khoá: **nguyên lý bền hơn công cụ**.
> **Trích:** `Wilder` → đối chiếu toàn văn sách (`tai_lieu/Cloud Architecture Patterns.pdf`). Câu định nghĩa mỗi pattern lấy **nguyên văn** từ phần tóm tắt chương trong Lời tựa.
> Đọc sau khi xong [Bài 0–8](bai_00_phuong-phap-system-design.md).

## Mục lục

1. [Vì sao có phụ lục: pattern có tên gọi](#1-vì-sao-có-phụ-lục-pattern-có-tên-gọi)
2. [Nhóm Scalability (3 pattern)](#2-nhóm-scalability-3-pattern)
3. [Nhóm Eventual Consistency (2 pattern)](#3-nhóm-eventual-consistency-2-pattern)
4. [Nhóm Multitenancy và commodity hardware (2 pattern)](#4-nhóm-multitenancy-và-commodity-hardware-2-pattern)
5. [Nhóm Network latency (4 pattern)](#5-nhóm-network-latency-4-pattern)
6. [Bảng tra nhanh: 11 pattern và bài đã học](#6-bảng-tra-nhanh-11-pattern-và-bài-đã-học)
7. [Nguồn](#nguồn)

---

## 1. Vì sao có phụ lục: pattern có tên gọi

Suốt khoá, bạn đã *giải* các bài toán và *gặp* các giải pháp lặp lại (tách async bằng queue, chữ ký uỷ quyền để upload thẳng, cô lập tenant...). Ngành đặt **tên gọi chuẩn** cho chúng — biết tên giúp bạn *gọi ra* đúng công cụ khi gặp bài toán, và *nói chung ngôn ngữ* với kỹ sư khác. Wilder định nghĩa đích ngắm chung của mọi pattern:

> [!quote] Wilder — Preface
> "Concisely stated, cloud-native applications leverage cloud-platform services to cost-efficiently and automatically allocate resources horizontally to match current needs, handle transient and hardware failures without downtime, and minimize network latency."
>
> *Nói gọn, **ứng dụng cloud-native** tận dụng dịch vụ cloud để: **cấp phát tài nguyên theo chiều ngang một cách tự động và tiết kiệm** khớp nhu cầu hiện tại, **chịu lỗi tạm thời và lỗi phần cứng mà không downtime**, và **giảm độ trễ mạng**.*

Ba vế đó chính là bốn nhóm pattern của sách: *scale ngang* (Scalability + Eventual Consistency), *chịu lỗi commodity* (Multitenancy & Commodity Hardware), *giảm latency* (Network Latency). Và điểm mấu chốt cho cả thư viện khoá học:

> [!quote] Wilder — Preface
> "The architecture patterns described in this book were selected because they are useful for building cloud-native applications. None are specific to the cloud. All are relevant to the cloud."
>
> *Các pattern trong sách được chọn vì hữu ích cho ứng dụng cloud-native. **Không cái nào riêng của một cloud cụ thể. Tất cả đều liên quan tới cloud.*** (= platform-agnostic: Azure 2012 hay AWS 2026 đều đúng.)

Dưới đây 11 pattern theo bốn nhóm, mỗi cái kèm **định nghĩa nguyên văn của tác giả** và *bạn đã học nó ở đâu*.

## 2. Nhóm Scalability (3 pattern)

Nền: *scale ngang* (thêm nhiều máy rẻ) thay vì *scale dọc* (một máy to) — [cloud-base Bài 1](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md), [Bài 9](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md).

**Horizontally Scaling Compute Pattern** (ch.2)
> [!quote] Wilder — Preface
> "This fundamental pattern focuses on horizontally scaling compute nodes."
>
> *Pattern nền tảng: **scale ngang các compute node** (thêm/bớt nhiều instance giống nhau).*
→ đã học: [aws-fund Bài 2](../../aws-fund/bai_hoc/bai_02_compute.md) + [cloud-base Bài 4 (stateless = điều kiện auto-scale)](../../cloud-base/bai_hoc/bai_04_mang-http-dns.md); dùng ở [Bài 7](bai_07_chiu-tai-overload.md).

**Queue-Centric Workflow Pattern** (ch.3)
> [!quote] Wilder — Preface
> "This essential pattern for loose coupling focuses on asynchronous delivery of command requests sent from the user interface to a processing service."
>
> *Pattern cốt yếu cho **ghép nối lỏng**: giao **bất đồng bộ** các lệnh từ giao diện người dùng tới một dịch vụ xử lý (qua hàng đợi).*
→ xương sống của [Bài 3 (fan-out)](bai_03_newsfeed-fanout.md) và [Bài 4 (hệ thông báo)](bai_04_he-thong-bao.md); nền [cloud-base Bài 11](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md).

**Auto-Scaling Pattern** (ch.4)
> [!quote] Wilder — Preface
> "This essential pattern for automating operations makes horizontal scaling more practical and cost-efficient."
>
> *Pattern cốt yếu để **tự động hoá vận hành**: làm cho scale ngang **thực dụng và tiết kiệm** hơn (tự thêm/bớt theo tải).*
→ [Bài 7](bai_07_chiu-tai-overload.md) + [aws-fund Bài 2](../../aws-fund/bai_hoc/bai_02_compute.md).

## 3. Nhóm Eventual Consistency (2 pattern)

Nền: giữ dữ liệu nhất quán trên hệ phân tán, chấp nhận *eventual* để scale — [cloud-base Bài 8 (CAP)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md).

**MapReduce Pattern** (ch.6)
> [!quote] Wilder — Preface
> "This pattern focuses on applying the MapReduce data processing pattern."
>
> *Áp dụng mô hình xử lý dữ liệu **MapReduce** (chia việc song song rồi gộp).*
→ [cloud-base Bài 11 (batch processing)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md).

**Database Sharding Pattern** (ch.7)
> [!quote] Wilder — Preface
> "This advanced pattern focuses on horizontally scaling data through sharding."
>
> *Pattern nâng cao: **scale ngang dữ liệu bằng sharding** (chia dữ liệu quá lớn cho nhiều node theo khoá).*
→ [cloud-base Bài 9 (hot partition)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md); dùng ở [Bài 1 (partition key)](bai_01_url-shortener.md).

## 4. Nhóm Multitenancy và commodity hardware (2 pattern)

Nền: phần cứng cloud là *commodity* (rẻ, *sẽ hỏng*); coi lỗi là bình thường — [cloud-base Bài 7](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md).

**Busy Signal Pattern** (ch.9)
> [!quote] Wilder — Preface
> "This pattern focuses on how an application should respond when a cloud service responds to a programmatic request with a busy signal rather than success."
>
> *Ứng dụng nên phản ứng thế nào khi dịch vụ cloud trả về **"tín hiệu bận"** (throttle/429/503) thay vì thành công — tức **lùi lại và thử lại tử tế**.*
→ [Bài 2 (rate limit/429)](bai_02_rate-limiter.md) + [Bài 4 (retry + backoff + jitter)](bai_04_he-thong-bao.md).

**Node Failure Pattern** (ch.10)
> [!quote] Wilder — Preface
> "This pattern focuses on how an application should respond when the compute node on which it is running shuts down or fails."
>
> *Ứng dụng nên phản ứng thế nào khi **chính node đang chạy nó tắt hoặc hỏng** (vì node sẽ hỏng bất kỳ lúc nào).*
→ [cloud-base Bài 7 (thất bại)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md); dùng ở [Bài 7](bai_07_chiu-tai-overload.md), [Bài 8 (static stability)](bai_08_da-vung-dr.md).

## 5. Nhóm Network latency (4 pattern)

Nền: round-trip mạng chậm hơn RAM ~triệu lần — [cloud-base Bài 0](../../cloud-base/bai_hoc/bai_00_vi-sao-nen-tang.md), [Bài 6](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md).

**Colocate Pattern** (ch.12)
> [!quote] Wilder — Preface
> "This basic pattern focuses on avoiding unnecessary network latency."
>
> *Pattern cơ bản: **tránh độ trễ mạng không cần thiết** bằng cách đặt các thành phần hay nói chuyện gần nhau (cùng region/AZ).*
→ [Bài 8 (đa-AZ trước)](bai_08_da-vung-dr.md); nền [cloud-base Bài 6](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md).

**Valet Key Pattern** (ch.13)
> [!quote] Wilder — Preface
> "This pattern focuses on efficiently using cloud storage services with untrusted clients."
>
> *Dùng kho lưu trữ cloud hiệu quả với **client không tin cậy**: phát một "chìa khoá có hạn" để client truy cập **thẳng** kho, không qua tầng ứng dụng.*
→ **đây chính là presigned URL** của [Bài 6 (upload ảnh)](bai_06_upload-xu-ly-anh.md)! Nền chữ ký: [cloud-base Bài 14 (SigV4)](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md). *(Bìa sách gọi là "Direct-to-Storage".)*

**CDN Pattern** (ch.14)
> [!quote] Wilder — Preface
> "This pattern focuses on reducing network latency for commonly accessed files through globally distributed edge caching."
>
> *Giảm độ trễ mạng cho các file hay truy cập bằng **cache ở rìa (edge) phân tán toàn cầu** (CloudFront).*
→ [cloud-base Bài 6 (CDN)](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md) + [aws-fund Bài 5 (CloudFront)](../../aws-fund/bai_hoc/bai_05_networking.md).

**Multisite Deployment Pattern** (ch.15)
> [!quote] Wilder — Preface
> "This advanced pattern focuses on deploying a single application to more than one data center."
>
> *Pattern nâng cao: **triển khai một ứng dụng ra nhiều trung tâm dữ liệu** (gần người dùng + chịu mất một vùng).*
→ [Bài 8 (đa vùng & DR)](bai_08_da-vung-dr.md).

## 6. Bảng tra nhanh: 11 pattern và bài đã học

| Pattern (Wilder, 2012) | Nhóm | Đã học / dùng ở |
| :-- | :-- | :-- |
| Horizontally Scaling Compute | Scalability | aws-fund B2 · aws-design B7 · cloud-base B4 |
| Queue-Centric Workflow | Scalability | aws-design B3, B4 · cloud-base B11 |
| Auto-Scaling | Scalability | aws-design B7 · aws-fund B2 |
| MapReduce | Eventual Consistency | cloud-base B11 |
| Database Sharding | Eventual Consistency | cloud-base B9 · aws-design B1 |
| Busy Signal | Multitenancy & commodity | aws-design B2, B4 · cloud-base B7 |
| Node Failure | Multitenancy & commodity | cloud-base B7 · aws-design B7, B8 |
| Colocate | Network latency | aws-design B8 · cloud-base B6 |
| **Valet Key** (= presigned URL) | Network latency | **aws-design B6** · cloud-base B14 |
| CDN | Network latency | cloud-base B6 · aws-fund B5 |
| Multisite Deployment | Network latency | aws-design B8 |

Đọc bảng này theo chiều ngược cũng hay: mỗi bài aws-design là *một hoặc vài* pattern có tên của Wilder ghép lại để giải một bài toán thật. Biết cả hai — *tên pattern* (từ vựng) và *cách ghép chúng dưới ràng buộc* (khoá này) — là đủ bộ đồ nghề thiết kế. Và việc một cuốn sách **Azure 2012** mô tả đúng những gì ta làm trên **AWS 2026** là lời nhắc: học *pattern*, đừng chỉ học *dịch vụ*.

## Nguồn

- **Bill Wilder**, *Cloud Architecture Patterns* (O'Reilly, 2012) — **Preface**: định nghĩa cloud-native, "none are specific to the cloud", và câu tóm tắt nguyên văn của cả 11 pattern. `tai_lieu/Cloud Architecture Patterns.pdf` (182 trang).
- Ánh xạ tới: [`cloud-base`](../../cloud-base/README.md), [`aws-fund`](../../aws-fund/README.md), và các [Bài 0–8](bai_00_phuong-phap-system-design.md) của khoá này.

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · **[Phụ lục — Pattern (Wilder)] ← bạn đang ở đây**

Xem thêm [README khoá học](../README.md).
