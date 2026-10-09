# aws-design — System Design trên AWS (problem-first)

> Khoá **tầng đỉnh**: học **giải bài toán thiết kế hệ thống thật trên AWS**. Khác hai khoá nền (bám *chương sách*), khoá này bám **VẤN ĐỀ** — mỗi bài là một *archetype* ("thiết kế X ở quy mô"), đi từ ước lượng tới kiến trúc tới đào sâu sub-problem khó nhất.

## Ba tầng — kim tự tháp

```
   aws-design   —  "làm sao cho đúng dưới ràng buộc thật"  (problem-first)   ← bạn ở đây
   ─────────────────────────────────────────────────────────────
   aws-fund     —  "có dịch vụ gì"   (what)
   cloud-base   —  "vì sao nó thế"   (why)
```

Mỗi bài *gọi lại* [`cloud-base`](../cloud-base/README.md) (nền CS) và [`aws-fund`](../aws-fund/README.md) (dịch vụ) qua cross-link — đây là nơi ba khoá hội tụ.

## Quy trình sáu bước (mọi bài theo đúng khung này)

```
1. LÀM RÕ YÊU CẦU   chức năng + phi chức năng (QPS, p99, nhất quán, chi phí)
2. ƯỚC LƯỢNG        back-of-envelope: writes/s, reads/s, dung lượng, băng thông
3. VẼ KIẾN TRÚC     ghép dịch vụ AWS
4. TÌM NÚT THẮT     chỗ nào vỡ trước khi scale?
5. ĐÀO SÂU 1 VẤN ĐỀ sub-problem khó nhất (trích Builders' Library) — nền ở cloud-base
6. SOI ĐÁNH ĐỔI     review qua 6 trụ Well-Architected
```

## Danh sách bài (9 bài)

| # | Archetype | Sub-problem đào sâu | Lab LocalStack |
| :-- | :-- | :-- | :-- |
| 0 | [Phương pháp system design](bai_hoc/bai_00_phuong-phap-system-design.md) | ước lượng, 6 trụ WA | demo ước lượng (TS) |
| 1 | [URL shortener](bai_hoc/bai_01_url-shortener.md) | partition key, hot key, cache | DynamoDB KV + atomic |
| 2 | [Rate limiter](bai_hoc/bai_02_rate-limiter.md) | token bucket, **load shedding**, goodput | DynamoDB conditional |
| 3 | [Newsfeed / fan-out](bai_hoc/bai_03_newsfeed-fanout.md) | fan-out-on-write vs read, celebrity | SNS→SQS fan-out |
| 4 | [Hệ thông báo tin cậy](bai_hoc/bai_04_he-thong-bao.md) | **retry + backoff + jitter**, DLQ | SQS + DLQ |
| 5 | [Thanh toán idempotent](bai_hoc/bai_05_thanh-toan-idempotent.md) | **idempotency key**, ACID token | DynamoDB conditional |
| 6 | [Upload & xử lý ảnh](bai_hoc/bai_06_upload-xu-ly-anh.md) | presigned URL, event-driven, backpressure | S3 presign + event |
| 7 | [Chịu traffic spike](bai_hoc/bai_07_chiu-tai-overload.md) | **shuffle sharding**, tránh fallback | shuffle sharding (TS) |
| 8 | [Đa vùng & DR](bai_hoc/bai_08_da-vung-dr.md) | static stability, RTO/RPO | DR calculator (TS) |
| — | [Phụ lục — Từ điển pattern (Wilder)](bai_hoc/phu-luc-cloud-patterns.md) | 11 pattern có-tên ↔ bài đã học | — |

## Nguồn (Luật số 1 — không viết theo trí nhớ)

| Mã | Nguồn | Dùng làm |
| :-- | :-- | :-- |
| **WA** | *AWS Well-Architected Framework* (whitepaper chính thức, PDF trong `tai_lieu/`, trích `WA (tr. X)`, PDF = tr. + 5) | lăng kính 6 trụ + đánh đổi |
| **BL** | *Amazon Builders' Library* (bài kỹ thuật thật của kỹ sư Amazon, lưu `tai_lieu/bl_*.txt`, trích `BL: <slug>`) | deep-dive problem-solving |

Bài Builders' Library đã dùng: timeouts-retries-and-backoff-with-jitter, using-load-shedding-to-avoid-overload, avoiding-insurmountable-queue-backlogs, challenges-with-distributed-systems, making-retries-safe-with-idempotent-apis, workload-isolation-using-shuffle-sharding, avoiding-fallback-in-distributed-systems, fairness-in-multi-tenant-systems.

## Chạy lab / demo

Lab AWS chạy thật trên **LocalStack + awslocal** (như `aws-fund`); demo khái niệm là **TypeScript chạy thẳng** bằng **Node 22.6+** (`node file.ts`). Output trong bài là **output chạy thật** (bash lab stateful → chạy tay; demo TS → tất định hoặc seed cố định).

## Sợi chỉ xuyên khoá

Tám archetype chỉ là vài nguyên lý nền lặp lại (xem [Bài 8 — Khép khoá](bai_hoc/bai_08_da-vung-dr.md#7-khép-khoá-tám-archetype-ba-tầng)):

- **Hot key / sharding** → URL shortener (1), celebrity (3), shuffle sharding (7).
- **Atomic / idempotency** → counter (1,2), payment (5), retry an toàn (4).
- **Decouple async + queue** → fan-out (3), thông báo (4), upload (6).
- **Đánh đổi mạnh↔nới** → goodput (2), eventual read (1), RTO/RPO (8), CAP (8).
- **Cô lập + fail rõ** → load shedding (2), shuffle sharding (7), tránh fallback (7), static stability (8).

Mục đích khoá: **không học thuộc kiến trúc, mà suy ra kiến trúc** từ con số (ước lượng) và nguyên lý (nền).
