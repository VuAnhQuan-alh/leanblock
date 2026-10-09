# cloud-base — Nền tảng Khoa học Máy tính cho Cloud

> Khoá tự học **nền tảng cho cloud**: hiểu *sâu* điều mà [`aws-fund`](../aws-fund/README.md) chỉ dùng được ở *bề mặt*. Luận đề: **mỗi dịch vụ AWS = một khái niệm CS nền tảng được "đóng gói managed"** — nguyên tắc nền (TCP, CAP, scheduling, log) *trường tồn* bất kể AWS đổi gì.

## Vì sao có khoá này

Bạn *dùng* được DynamoDB, S3, Lambda sau `aws-fund`. Nhưng vì sao Lambda có cold start? Vì sao DynamoDB read mặc định "eventually consistent"? Vì sao thêm index tốn tiền ghi? Những câu "vì sao" đó nằm **dưới** AWS — ở khoa học máy tính kinh điển. Khoá này curate 5 cuốn sách nền để trả lời chúng, tổ chức **bottom-up theo bốn trụ**.

## Bốn trụ (bottom-up — càng xuống càng bền)

```
   Ứng dụng cloud  —  mỗi dịch vụ AWS = "managed [khái niệm nền]"
   ═══════════════════════════════════════════════════════════════════
   trụ 4 · DỮ LIỆU         storage engine, batch/stream                 (DDIA)
   trụ 3 · DISTRIBUTED     thất bại, nhân bản/CAP, phân mảnh/consensus   (DDIA, UDS)
   trụ 2 · MẠNG            phân tầng/HTTP/DNS, TCP/TLS, hiệu năng/CDN    (Kurose, HPBN)
   trụ 1 · OS & ẢO HOÁ     ảo hoá, concurrency, lưu trữ bền             (OSTEP)
   ═══════════════════════════════════════════════════════════════════
            ▲ càng xuống BỀN hơn (TCP/CAP 20 năm nữa vẫn đúng)
```

## Danh sách bài

| # | Bài | Trụ | Nội dung lõi |
| :-- | :-- | :-- | :-- |
| 0 | [Vì sao cần nền + bản đồ bốn trụ](bai_hoc/bai_00_vi-sao-nen-tang.md) | — | luận đề, bậc thang độ trễ, phương pháp học |
| 1 | [OS: ảo hoá](bai_hoc/bai_01_os-ao-hoa.md) | 1 | process, ảo hoá CPU (time-sharing), address space |
| 2 | [OS: concurrency](bai_hoc/bai_02_os-concurrency.md) | 1 | thread, race condition, atomicity |
| 3 | [OS: lưu trữ bền](bai_hoc/bai_03_os-luu-tru.md) | 1 | file system, crash consistency, journaling |
| 4 | [Mạng: phân tầng, HTTP, DNS](bai_hoc/bai_04_mang-http-dns.md) | 2 | 5 tầng, HTTP stateless, DNS phân tán |
| 5 | [Mạng: TCP, TLS](bai_hoc/bai_05_mang-tcp-tls.md) | 2 | reliable, bắt tay 3 bước, round-trip |
| 6 | [Mạng: hiệu năng, CDN](bai_hoc/bai_06_mang-hieu-nang.md) | 2 | latency vs bandwidth, CDN |
| 7 | [Distributed: giao tiếp & thất bại](bai_hoc/bai_07_dist-giao-tiep.md) | 3 | partial failure, timeout, idempotency |
| 8 | [Distributed: nhân bản & nhất quán](bai_hoc/bai_08_dist-nhat-quan.md) | 3 | replication lag, eventual, CAP |
| 9 | [Distributed: phân mảnh & consensus](bai_hoc/bai_09_dist-phan-manh.md) | 3 | sharding, hot spot, quorum |
| 10 | [Dữ liệu: storage engine](bai_hoc/bai_10_du-lieu-storage.md) | 4 | append-log, index trade-off, B-tree vs LSM |
| 11 | [Dữ liệu: batch & stream](bai_hoc/bai_11_du-lieu-batch-stream.md) | 4 | bounded/unbounded, event bất biến |

**Chuyên đề nâng cao** (mở rộng từng trụ — đọc sau khi nắm lõi 0–11):

| # | Bài | Trụ | Nội dung lõi |
| :-- | :-- | :-- | :-- |
| 12 | [OS: bộ nhớ ảo & paging](bai_hoc/bai_12_os-bo-nho-ao.md) | 1 | page/frame, swap, page fault, OOM |
| 13 | [OS: scheduling & locks](bai_hoc/bai_13_os-scheduling-locks.md) | 1 | turnaround/response, mutex, deadlock (4 điều kiện) |
| 14 | [Mạng: bảo mật & mật mã](bai_hoc/bai_14_mang-bao-mat.md) | 2 | đối xứng/công khai, chữ ký số, CA/PKI |
| 15 | [Distributed: đồng hồ & thứ tự](bai_hoc/bai_15_dist-dong-ho.md) | 3 | clock skew, LWW mất ghi, logical clock |
| 16 | [Distributed: transaction & saga](bai_hoc/bai_16_dist-transaction-saga.md) | 3–4 | ACID, atomic commit = consensus, 2PC vs saga |
| 17 | [Dữ liệu: data models](bai_hoc/bai_17_du-lieu-data-models.md) | 4 | quan hệ / document / graph, chọn theo quan hệ |
| 18 | [Dữ liệu: encoding & schema evolution](bai_hoc/bai_18_du-lieu-encoding.md) | 4 | backward/forward compat, breaking change |

## Nguồn (5 cuốn kinh điển)

Mọi câu chốt trích **nguyên văn tiếng Anh** trong `[!quote]` (Luật số 1: không viết theo trí nhớ), theo `[Mã sách] (tr. X)` — số trang **in trong sách**; mỗi cuốn một offset PDF:

| Mã | Sách | Trụ dùng | Offset (PDF = tr. +) |
| :-- | :-- | :-- | :-- |
| **OSTEP** | *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau) | 1 | +25 |
| **Kurose** | *Computer Networking: A Top-Down Approach, 8th* (Kurose & Ross) | 2 | +28 |
| **HPBN** | *High Performance Browser Networking* (Ilya Grigorik) | 2 | +18 |
| **UDS** | *Understanding Distributed Systems, 2nd* (Roberto Vitillo) | 3 | +18 |
| **DDIA** | *Designing Data-Intensive Applications* (Martin Kleppmann) | 3, 4 | +22 |

File PDF nằm trong `tai_lieu/`.

## Phương pháp học (nhớ lâu)

Giữ bộ công cụ nhớ-lâu của [`aws-fund` Bài 0](../aws-fund/bai_hoc/bai_00_hoc-aws-nho-lau-va-localstack.md): **active recall** (thẻ ôn), **spaced repetition**, **generation effect** (demo chạy được), **so-sánh tables**, và điểm nhấn riêng của khoá — hộp **"Nối về AWS"** cuối mỗi khái niệm (elaboration: neo kiến thức nền trừu tượng vào một hiện tượng AWS cụ thể bạn đã gặp).

Cách đọc hiệu quả: **học xen kẽ với `aws-fund`** (mỗi "Nối về AWS" mở lại bài AWS tương ứng); **gõ lại demo**, đừng chỉ đọc; đừng cố nhớ hết 5 cuốn — khoá đã curate phần *làm cloud sáng ra*.

## Chạy demo

Mọi demo là **TypeScript chạy thẳng** bằng **Node 22.6+** (Node tự bỏ phần kiểu). Lưu khối code vào một file `.ts` rồi:

```bash
node tên-file.ts
```

Không cần cài gói, không cần `tsc`. Output trong bài là **output chạy thật** (một số demo đo thời gian/race nên con số tuỳ máy — bài ghi chú rõ chỗ nào tất định, chỗ nào tuỳ máy).

## Sợi chỉ xuyên khoá

Hai mô-típ lặp ở cả bốn trụ (xem [Bài 11 — Khép bốn trụ](bai_hoc/bai_11_du-lieu-batch-stream.md#khép-bốn-trụ)):

1. **Đảm bảo mạnh mua bằng phối hợp/chi phí; nới lỏng đổi lấy tốc độ/sẵn sàng.** (atomicity/TCP/strong consistency/B-tree ↔ eventual/UDP/LSM/stream)
2. **Append-only, bất biến.** (journaling → LSM-tree → event stream)

Nắm hai sợi chỉ này, bạn *suy ra* được hành vi của dịch vụ AWS thay vì học thuộc danh mục.
