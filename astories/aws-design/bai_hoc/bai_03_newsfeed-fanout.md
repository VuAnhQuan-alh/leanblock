# Bài 3 — Thiết kế newsfeed và bài toán fan-out

> [!info] Về bài này
> **Archetype 3 — phân phát một sự kiện cho nhiều người.** Khi alice đăng một post, nó phải hiện trong feed của hàng triệu follower. Đây là bài toán **fan-out**, và quyết định cốt lõi — **fan-out-on-write vs fan-out-on-read** — cùng *bài toán người nổi tiếng* (celebrity problem) là thứ phân biệt một feed chạy được với một feed sập khi một KOL đăng bài.
> Nguồn: **WA** (Reliability — kiến trúc async/event-driven). Nền: [cloud-base Bài 9 (hot key)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 11 (stream)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md); dịch vụ: [aws-fund Bài 4 (SNS/SQS)](../../aws-fund/bai_hoc/bai_04_messaging.md).
> **Lab:** fan-out SNS→nhiều SQS trên LocalStack.
> Nên đọc trước: [Bài 2 — rate limiter](bai_02_rate-limiter.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: fan-out qua pub/sub](#2-kiến-trúc-fan-out-qua-pubsub)
3. [Đào sâu: fan-out-on-write vs on-read](#3-đào-sâu-fan-out-on-write-vs-on-read)
4. [Lab: fan-out một SNS tới nhiều SQS](#4-lab-fan-out-một-sns-tới-nhiều-sqs)
5. [Soi Well-Architected](#5-soi-well-architected)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] Một ngôi sao vừa đăng bài
> Bạn làm feed cho mạng xã hội. `alice` — 200 follower — đăng một post, hiện trong feed 200 người: nhẹ nhàng. Rồi một ca sĩ **10 triệu follower** đăng. Cách làm hiển nhiên (*"đăng xong thì chèn post vào feed của từng follower"*) giờ phải làm **10 triệu lần ghi cho một post** — server khựng, feed mọi người trễ. Cùng một tính năng, nhưng `alice` và ca sĩ là hai bài toán khác hẳn. Thiết kế phải xử được *cả hai*.

**Chức năng:** user đăng post; follower thấy post mới trong feed (thứ tự thời gian). **Phi chức năng:** đọc feed nhanh (p99 thấp — đường nóng), chịu được user có *rất nhiều* follower, viết post không chặn.

Ước lượng cho thấy sự bất đối xứng quyết định mọi thứ: giả sử 1 post trung bình 200 follower → mỗi lần đăng sinh 200 "feed insert". Nhưng phân bố follower **lệch cực mạnh** (power law): đa số user vài trăm follower, một số ít có *hàng chục triệu*. Chính cái đuôi lệch này — không phải trung bình — là bài toán (mục 3).

## 2. Kiến trúc: fan-out qua pub/sub

Tách *viết post* khỏi *phát tán* bằng một tầng trung gian bất đồng bộ (đúng tinh thần WA):

> [!quote] WA (tr. 515)
> "Asynchronous systems communicate with each other by exchanging data asynchronously through an intermediary service without coupling individual systems."
>
> *Các hệ **bất đồng bộ** giao tiếp bằng cách **trao đổi dữ liệu qua một dịch vụ trung gian**, mà **không ghép cứng** các hệ với nhau.*

```
   POST  alice đăng
     ─▶ API GW ─▶ Lambda ─▶ lưu post (DynamoDB) ─▶ SNS "new-post" (publish 1 lần)
                                                        │ fan-out
                              ┌─────────────────────────┼─────────────────────────┐
                              ▼                          ▼                          ▼
                         SQS→Lambda                 SQS→Lambda                 SQS→Lambda
                         (chèn feed                 (chèn feed                 (chèn feed
                          nhóm follower A)           nhóm B)                    nhóm C)
```

Lambda viết post *trả về ngay* sau khi publish một message lên SNS — không chờ phát tán. SNS **fan-out** message đó tới nhiều SQS, mỗi queue được một nhóm worker tiêu thụ để chèn vào feed từng follower. Việc nặng (phát tán) chạy *nền*, bất đồng bộ:

> [!quote] WA (tr. 528)
> "These architectures are typically backed by a message queue such as Amazon SQS, Amazon MQ, Amazon Kinesis Streams, or Amazon Managed Streaming for Apache Kafka (MSK)."
>
> *Các kiến trúc này thường **dựa trên một message queue** như Amazon SQS, Amazon MQ, Amazon Kinesis Streams, hoặc Amazon MSK.*

## 3. Đào sâu: fan-out-on-write vs on-read

> [!example] Ẩn dụ: báo giao tận nhà vs ra sạp mua
> **Fan-out-on-write (push)** = toà soạn *in một bản cho mỗi người đặt báo và giao tận hòm thư*. Người đọc chỉ việc mở hòm thư (feed dựng sẵn — đọc cực nhanh). Nhưng nếu một tờ có 10 triệu người đặt, toà soạn phải in+giao 10 triệu bản cho *một* số báo.
> **Fan-out-on-read (pull)** = toà soạn in *một* bản gốc; muốn đọc thì bạn *ghé sạp* gom tin từ những nguồn mình theo. In rẻ (một bản), nhưng mỗi lần đọc tốn công đi gom.

Hai chiến lược đối ngẫu — và chọn sai làm feed sập:

**Fan-out-on-write (push):** khi đăng, *ngay lập tức* chèn post vào feed-cache của **mọi** follower. Đọc feed cực nhanh (đã dựng sẵn). Giá: một post của người có 10M follower = **10M lần ghi** — một cơn bão ghi (write storm), và lãng phí nếu phần lớn follower không online.

**Fan-out-on-read (pull):** khi đăng chỉ ghi *một* bản post. Đọc feed thì *gộp tại chỗ* post mới nhất của những người mình theo. Viết rẻ; giá: đọc đắt (phải truy vấn nhiều nguồn mỗi lần mở feed) — tệ cho đường nóng.

**Bài toán người nổi tiếng:** fan-out-on-write chết với KOL (10M ghi/post); fan-out-on-read chết với user bình thường (đọc chậm). Lời giải thực tế là **lai**: fan-out-on-write cho user thường; **fan-out-on-read cho số ít "celebrity"** (đánh dấu riêng), rồi *trộn* lúc đọc. Đây chính là **hot key** của [cloud-base Bài 9](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md) đội lốt: một "khoá" (celebrity) nhận lượng tải khổng lồ lệch hẳn phần còn lại, nên phải xử lý *khác* phần còn lại. Nhận ra celebrity = một dạng tránh hot partition.

## 4. Lab: fan-out một SNS tới nhiều SQS

Chứng minh cơ chế fan-out: **một** publish lên SNS → **mọi** SQS subscriber nhận. Mỗi queue đại diện một nhóm worker phát tán feed. Chạy thật trên LocalStack:

```bash
TOPIC=$(awslocal sns create-topic --name new-post --query 'TopicArn' --output text)
QA=$(awslocal sqs create-queue --queue-name feed-shard-A --query 'QueueUrl' --output text)
QB=$(awslocal sqs create-queue --queue-name feed-shard-B --query 'QueueUrl' --output text)
for Q in $QA $QB; do
  ARN=$(awslocal sqs get-queue-attributes --queue-url $Q --attribute-names QueueArn \
        --query 'Attributes.QueueArn' --output text)
  awslocal sns subscribe --topic-arn $TOPIC --protocol sqs --notification-endpoint $ARN
done

# publish MỘT post → SNS fan-out tới MỌI queue
awslocal sns publish --topic-arn $TOPIC --message '{"postId":"p1","author":"alice"}'
sleep 1
for Q in "A:$QA" "B:$QB"; do
  cnt=$(awslocal sqs receive-message --queue-url "${Q#*:}" --max-number-of-messages 5 \
        --query 'length(Messages)' --output text)
  echo "feed-shard-${Q%%:*} nhận: ${cnt:-0} message"
done
```

Kết quả chạy thật:

```
# publish MỘT post → fan-out tới mọi shard queue:
   feed-shard-A nhận: 1 message
   feed-shard-B nhận: 1 message
```

Một publish, hai queue cùng nhận — đó *là* fan-out. Thêm một subscriber (một nhóm follower nữa) không đụng gì tới publisher: alice vẫn publish *một* lần, SNS lo nhân bản. Đây là sức mạnh của **ghép nối rời** (WA tr.515): người đăng không biết, không chờ, không phụ thuộc số lượng người nhận — chính là điều kiện để scale fan-out. Trong thật, giữa SNS và worker đặt SQS (có trong lab) để *đệm* bão ghi và cho retry (Bài 4).

> [!note] Tự thử
> 1. Thêm queue thứ ba rồi publish lại: publisher có đổi gì không? Vì sao "thêm người nhận" là thao tác zero-cost với publisher?
> 2. Nếu alice là celebrity (10M follower): vì sao fan-out-on-write qua cơ chế này vẫn là "10M ghi"? Lai với fan-out-on-read chữa ra sao? (mục 3)
> 3. Bỏ SQS, subscribe Lambda thẳng vào SNS: mất khả năng *đệm* + *retry* gì? (Bài 4)

## 5. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | decouple: viết post không phụ thuộc phát tán; SQS đệm + retry | celebrity cần nhánh riêng |
| Performance | đọc feed nhanh (fan-out-on-write dựng sẵn) | lai để p99 ổn cho cả 2 loại user |
| Cost | fan-out-on-write phí ghi cho follower không online | lai + chỉ push user "active" |
| Security | chỉ service được publish/subscribe (IAM) | — |
| Operational | theo dõi độ trễ phát tán & backlog queue | backlog là triệu chứng bão ghi (Bài 6) |

Nút thắt chuyển tiếp: phát tán là *khối lớn công việc bất đồng bộ* — nếu worker chậm/hỏng, queue dồn lại. Làm sao giao **tin cậy** (không mất, không kép) và xử lý **backlog**? Đó là Bài 4.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — Vì sao tách "viết post" khỏi "phát tán" bằng pub/sub?
> **Đáp:** phát tán là việc nặng; đẩy nền bất đồng bộ để viết post trả về ngay. Decouple (WA tr.515): publisher không chờ, không phụ thuộc số người nhận.

> [!question] Thẻ 3.2 — Fan-out-on-write vs on-read: mỗi cái nhanh/chậm ở đâu?
> **Đáp:** on-write: đọc nhanh (dựng sẵn), viết đắt (chèn vào mọi follower). on-read: viết rẻ (1 bản), đọc đắt (gộp lúc đọc).

> [!question] Thẻ 3.3 — "Bài toán người nổi tiếng" là gì? Giải thế nào?
> **Đáp:** on-write chết với KOL (10M ghi/post), on-read chết với user thường (đọc chậm). Giải: **lai** — on-write cho user thường, on-read cho celebrity, trộn lúc đọc.

> [!question] Thẻ 3.4 — Celebrity là biến thể của khái niệm nền nào?
> **Đáp:** **hot key / hot partition** (cloud-base Bài 9): một khoá nhận tải lệch khổng lồ → phải xử lý khác phần còn lại.

> [!question] Thẻ 3.5 — Vì sao thêm một SQS subscriber là zero-cost với publisher?
> **Đáp:** publisher vẫn publish *một* lần lên SNS; SNS lo nhân bản tới mọi subscriber. Ghép nối rời → publisher không biết/không phụ thuộc người nhận.

## 7. Câu hỏi tự kiểm tra

1. Vì sao phân bố follower lệch (power law) mới là bài toán, không phải trung bình? *(mục 1, 3)*
2. Vẽ kiến trúc fan-out qua SNS→SQS. Vai trò SQS giữa SNS và worker? *(mục 2, 4)*
3. So sánh fan-out-on-write vs on-read. Khi nào mỗi cái chết? *(mục 3)*
4. Giải pháp lai cho celebrity. Nối về hot key ra sao? *(mục 3, cloud-base Bài 9)*
5. Chạy lab §4. Vì sao thêm subscriber không đụng publisher? *(mục 4, WA tr. 515)*

## Tóm tắt một trang

```
BÀI 3 — NEWSFEED & FAN-OUT
─────────────────────────────────────────────────────────
VẤN ĐỀ  1 post → feed của hàng triệu follower. Phân bố follower LỆCH (power
   law) — cái đuôi (celebrity) là bài toán, không phải trung bình.

KIẾN TRÚC  viết post → publish 1 lần lên SNS → FAN-OUT tới nhiều SQS → worker
   chèn feed. Decouple async (WA tr.515): publisher không chờ/không phụ thuộc
   số người nhận. Event-driven backed by queue (WA tr.528).

ĐÀO SÂU  fan-out-on-WRITE (push): đọc nhanh, viết đắt (chết với KOL 10M ghi).
   fan-out-on-READ (pull): viết rẻ, đọc đắt (chết với user thường).
   → LAI: on-write cho user thường + on-read cho celebrity, trộn lúc đọc.
   Celebrity = HOT KEY (cloud-base Bài 9) đội lốt.

LAB  1 publish SNS → 2 SQS cùng nhận. Thêm subscriber = zero-cost với publisher.

6 TRỤ  reliability/performance; cost (phí ghi follower offline → lai).
   Tiếp: phát tán = khối async lớn → giao TIN CẬY + backlog (Bài 4).
```

## Nguồn

- **AWS Well-Architected Framework** — Reliability: hệ bất đồng bộ qua trung gian không ghép cứng (tr. 515), event-driven dựa trên message queue (tr. 528). `tai_lieu/AWS-Well-Architected-Framework.pdf` (offset +5).
- Nền: [cloud-base Bài 9 (hot key/celebrity)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 11 (stream)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md).
- Dịch vụ: [aws-fund Bài 4 — SNS/SQS fan-out](../../aws-fund/bai_hoc/bai_04_messaging.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · **[Bài 3 — Newsfeed & fan-out] ← bạn đang ở đây** · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
