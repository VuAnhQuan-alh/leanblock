# Bài 4 — Messaging: SQS, SNS, EventBridge — ba cách ghép nối rời

> [!info] Về bài này
> Dựng từ **Chương 7 — Messaging** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 189–248`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Bộ ba này là **nơi nhầm lẫn nhiều nhất** của AWS — nên bài nhấn *bảng quyết định* (vũ khí interleaving chống nhầm) và lab chạy thật cả ba cơ chế.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **SQS, SNS, EventBridge** đều chạy tốt trên LocalStack free.

## Mục lục

1. [Mô hình tư duy: vì sao cần ghép nối rời](#1-mô-hình-tư-duy-vì-sao-cần-ghép-nối-rời)
2. [SQS: hàng đợi, kéo (poll), một-tới-một](#2-sqs-hàng-đợi-kéo-poll-một-tới-một)
3. [SNS: pub/sub, đẩy (push), một-tới-nhiều](#3-sns-pubsub-đẩy-push-một-tới-nhiều)
4. [EventBridge: event bus, định tuyến theo luật](#4-eventbridge-event-bus-định-tuyến-theo-luật)
5. [Bảng quyết định: SQS vs SNS vs EventBridge](#5-bảng-quyết-định-sqs-vs-sns-vs-eventbridge)
6. [Lab 4: SQS và SNS→SQS fan-out](#6-lab-4-sqs-và-snssqs-fan-out)
7. [Cạm bẫy: poll/push, at-least-once, DLQ](#7-cạm-bẫy-pollpush-at-least-once-dlq)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: vì sao cần ghép nối rời

Nếu dịch vụ A *gọi thẳng* dịch vụ B rồi chờ trả lời, thì B chết là A kẹt, B chậm là A chậm, B quá tải là mất request. **Messaging** chèn một *lớp trung gian* để A và B **tách rời** (decouple): A gửi tin đi rồi *làm việc khác*, B xử lý khi rảnh. Ba dịch vụ = ba *kiểu* trung gian:

```
  SQS:  A ──► [hàng đợi] ◄── B      (1 tin → 1 người xử lý; kéo/poll)
  SNS:  A ──► (topic) ──┬──► B1     (1 tin → MỌI subscriber; đẩy/push)
                        ├──► B2     (fan-out)
                        └──► B3
  EventBridge: A ──► (event bus) ──[luật]──► target   (định tuyến theo nội dung)
```

## 2. SQS: hàng đợi, kéo (poll), một-tới-một

> [!quote] Ch. 7 — SQS (tr. 191)
> "SQS decouples your architecture by introducing a message queue. Your message remains in the queue until a consumer picks it up and removes it."
>
> *SQS **tách rời** kiến trúc bằng cách chèn một **hàng đợi**. Tin của bạn **nằm trong hàng đợi** cho tới khi một consumer *lấy nó ra và xoá*.*

Đặc tính cốt lõi phải nhớ — **SQS là kéo, không phải đẩy**:

> [!quote] Ch. 7 — SQS is Poll-Based (tr. 191)
> "One common misconception about SQS is that it is a push-based system."
>
> *Một hiểu lầm phổ biến: tưởng SQS là hệ **push (đẩy)**.* (Thực ra consumer phải **poll — chủ động hỏi** hàng đợi xem có tin không.)

Mô hình **một-tới-một** (point-to-point): mỗi tin được *đúng một* consumer lấy và xử lý. SQS hợp để **đệm tải** (buffer) và **xử lý nền**: ví dụ "có 1000 ảnh cần resize" → nhét 1000 tin vào queue, các worker kéo về xử lý dần, không ai bị quá tải. Hai loại: **Standard** (thông lượng gần vô hạn, có thể trùng/lệch thứ tự) và **FIFO** (đúng thứ tự, không trùng, nhưng chậm hơn). (Fun fact: SQS là *dịch vụ AWS đầu tiên*, ra trước cả S3 và EC2, tr.191.)

## 3. SNS: pub/sub, đẩy (push), một-tới-nhiều

> [!quote] Ch. 7 — SNS (tr. 210)
> "A publisher sends messages to topics, and subscribers subscribe to those topics. The topic is the distributor of messages in SNS, forwarding all messages to the subscribers."
>
> *Một **publisher** gửi tin tới **topic**, và các **subscriber** đăng ký topic đó. Topic là **nơi phân phối**, chuyển **mọi** tin tới **tất cả** subscriber.*

Khác SQS, SNS là **đẩy (push)** và **một-tới-nhiều** (fan-out):

> [!quote] Ch. 7 — SNS Pub/Sub (tr. 210)
> "SNS publishes messages to subscribers with a push-based model."
>
> *SNS **đẩy** tin tới subscriber theo mô hình **push**.*

Một tin publish lên topic → *đồng thời* tới mọi subscriber (email, SMS, Lambda, HTTP, hoặc **SQS queue**). Hợp khi *một sự kiện cần nhiều nơi phản ứng*: "đơn hàng mới" → gửi email khách + ghi analytics + cập nhật kho, cùng lúc. Mẫu kinh điển: **SNS + SQS fan-out** — topic đẩy vào *nhiều queue*, mỗi queue một worker xử lý độc lập (bạn sẽ chạy ở lab).

## 4. EventBridge: event bus, định tuyến theo luật

> [!quote] Ch. 7 — EventBridge (tr. 223)
> "EventBridge is the ultimate service for implementing your event-driven architecture (EDA)."
>
> *EventBridge là dịch vụ **tối hậu** để xây **kiến trúc hướng sự kiện** (EDA).*

Khác biệt tư duy giữa "API-driven" và "event-driven":

> [!quote] Ch. 7 — Event-Driven (tr. 224)
> "In an event-driven way, the endpoint informs the router that something happened without caring about what happens next: 'Hey, I just published a post.'"
>
> *Theo lối event-driven, endpoint **báo cho router rằng có chuyện gì đó xảy ra** mà **không bận tâm** điều gì diễn ra tiếp: "Này, tôi vừa đăng một bài."*

Nguồn chỉ *phát sự kiện*; EventBridge *quyết định* ai nhận, dựa trên **luật (rule)** khớp **mẫu (event pattern)** theo *nội dung* sự kiện. Ba thành phần: **Event Bus** (nơi sự kiện chảy qua) → **Rule** (lọc theo pattern) → **Target** (nơi nhận: Lambda, SQS, SNS…). Nó cũng làm *lịch* (scheduled events, thay cho cron). EventBridge **linh hoạt nhất** — và cũng *phức tạp nhất* trong ba.

## 5. Bảng quyết định: SQS vs SNS vs EventBridge

Bảng này là *trái tim* của bài — biết **chọn** là chống được nhầm lẫn:

| Tiêu chí | **SQS** | **SNS** | **EventBridge** |
| :--- | :--- | :--- | :--- |
| Mô hình | hàng đợi (queue) | pub/sub (topic) | event bus + luật |
| Chiều | **1 → 1** (point-to-point) | **1 → N** (fan-out) | **1 → N** theo *luật khớp* |
| Kéo hay đẩy | **poll** (consumer hỏi) | **push** (SNS đẩy) | **push** tới target |
| Tin lưu lại? | **có** — tới khi được xoá (đệm tải) | **không** — không ai nghe thì mất | không (nhưng có archive/replay) |
| Định tuyến theo nội dung | không | lọc cơ bản (filter policy) | **mạnh** (event pattern) |
| Hợp khi | đệm tải, xử lý nền, đảm bảo *được xử lý* | một sự kiện → nhiều nơi phản ứng ngay | định tuyến phức tạp, tích hợp nhiều nguồn, lịch |
| LocalStack free | chạy tốt | chạy tốt | chạy tốt |

Quy tắc: cần **đệm + đảm bảo xử lý từng việc** → SQS. cần **báo cho nhiều bên cùng lúc** → SNS. cần **định tuyến thông minh theo loại sự kiện / từ nhiều nguồn AWS / lịch** → EventBridge. (Và chúng *kết hợp*: SNS→nhiều SQS, hay EventBridge→SQS→Lambda.)

## 6. Lab 4: SQS và SNS→SQS fan-out

Phần 1 — hàng đợi SQS (gửi rồi kéo về):

```bash
QURL=$(awslocal sqs create-queue --queue-name jobs --query QueueUrl --output text)
awslocal sqs send-message --queue-url "$QURL" --message-body "xử lý note n1"
# consumer KÉO (poll) tin về:
awslocal sqs receive-message --queue-url "$QURL" --query 'Messages[0].Body' --output text
```

Phần 2 — SNS fan-out: một `publish` → queue `audit` (đã subscribe) nhận được qua push:

```bash
TOPIC=$(awslocal sns create-topic --name note-events --query TopicArn --output text)
Q2=$(awslocal sqs create-queue --queue-name audit --query QueueUrl --output text)
Q2ARN=$(awslocal sqs get-queue-attributes --queue-url "$Q2" \
  --attribute-names QueueArn --query 'Attributes.QueueArn' --output text)
awslocal sns subscribe --topic-arn "$TOPIC" --protocol sqs --notification-endpoint "$Q2ARN"
awslocal sns publish --topic-arn "$TOPIC" --message "note n2 vừa được tạo"
sleep 1
awslocal sqs receive-message --queue-url "$Q2" --query 'Messages[0].Body' --output text
# dọn
awslocal sqs delete-queue --queue-url "$QURL"; awslocal sqs delete-queue --queue-url "$Q2"
awslocal sns delete-topic --topic-arn "$TOPIC"
```

Kết quả chạy thật (phần cốt lõi):

```
# Phần 1 (SQS) — consumer kéo về:
xử lý note n1

# Phần 2 (SNS→SQS) — queue 'audit' nhận tin publish (lấy field Message trong envelope SNS):
note n2 vừa được tạo
```

*(MessageId mỗi lần chạy là UUID khác nhau — bỏ qua. Tin SNS tới SQS được bọc trong một "envelope" JSON; nội dung thật nằm ở field `Message`.)* Phần 2 chính là *fan-out*: nếu subscribe thêm queue `analytics` nữa, **cùng một `publish`** sẽ tới *cả hai* queue — đó là sức mạnh "1 → N" của SNS mà SQS không có. Trong capstone: tạo note → `publish` sự kiện → một queue cho xử lý ảnh, một cho ghi log.

> [!question] Tự thử
> 1. Phần 1: gọi `receive-message` *lần hai* ngay sau lần một. Có còn tin không? Vì sao? (Gợi ý: *visibility timeout* — tin bị "ẩn" tạm thời, chưa bị xoá hẳn trừ khi bạn `delete-message`.)
> 2. Phần 2: subscribe thêm queue thứ hai rồi publish một lần. Cả hai queue có nhận không?
> 3. Thử `publish` lên topic *không có subscriber nào*. Tin đi đâu? (SNS vs SQS khác nhau ở đây.)

## 7. Cạm bẫy: poll/push, at-least-once, DLQ

> [!warning] Thực tế & cạm bẫy Messaging
> - **SQS là poll, không push.** Consumer phải *chủ động hỏi*. Lambda nối SQS qua "event source mapping" (AWS poll hộ rồi gọi Lambda). Đừng tưởng tin tự "nhảy" vào consumer.
> - **Visibility timeout.** Khi một consumer `receive` một tin, tin bị *ẩn* (không biến mất) trong một khoảng; nếu consumer không `delete-message` trong thời gian đó, tin *hiện lại* cho người khác → **xử lý trùng**. Phải xoá sau khi xử lý xong.
> - **At-least-once + Standard queue có thể trùng/lệch thứ tự.** Hãy viết xử lý **idempotent** (chạy lại nhiều lần vẫn đúng). Cần đúng-thứ-tự/không-trùng → FIFO (đánh đổi thông lượng).
> - **Dead-Letter Queue (DLQ).** Tin xử lý thất bại nhiều lần nên được đẩy sang DLQ để điều tra, thay vì kẹt mãi làm nghẽn queue.
> - **SNS không lưu tin.** Publish lúc không ai subscribe → tin **mất**. Cần đảm bảo nhận → SNS→**SQS** (queue giữ tin lại). Đây là lý do mẫu SNS+SQS phổ biến.
> - **EventBridge mạnh nhưng dễ over-engineer.** Với nhu cầu đơn giản "A báo B", SQS/SNS đủ; đừng kéo cả event bus + rule + pattern vào khi chưa cần định tuyến phức tạp.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — SQS vs SNS: kéo/đẩy? một-tới-mấy?
> **Đáp:** SQS = **poll (kéo)**, **1→1** (point-to-point). SNS = **push (đẩy)**, **1→N** (fan-out).

> [!question] Thẻ 4.2 — SQS có lưu tin không? SNS có không?
> **Đáp:** SQS **giữ tin** tới khi được xoá (đệm tải). SNS **không lưu** — không ai subscribe thì tin mất.

> [!question] Thẻ 4.3 — Visibility timeout giải quyết gì? Cạm bẫy?
> **Đáp:** sau `receive`, tin bị *ẩn* tạm để consumer khác không lấy trùng. Cạm bẫy: quên `delete-message` → tin hiện lại → xử lý trùng. Viết idempotent.

> [!question] Thẻ 4.4 — Khi nào chọn EventBridge thay vì SNS?
> **Đáp:** khi cần **định tuyến theo nội dung sự kiện** (event pattern), tích hợp *nhiều nguồn AWS*, hoặc **lịch (scheduled)**. SNS chỉ fan-out đơn giản tới subscriber của topic.

> [!question] Thẻ 4.5 — Mẫu SNS+SQS fan-out giải quyết điểm yếu nào của SNS?
> **Đáp:** SNS không lưu tin; nối SNS→SQS để **queue giữ tin lại** → mỗi consumer xử lý độc lập, không mất tin dù tạm offline.

## 9. Câu hỏi tự kiểm tra

1. Vì sao messaging giúp "tách rời" kiến trúc? Điều gì xảy ra nếu A gọi thẳng B? *(mục 1)*
2. SQS poll vs push — hiểu lầm phổ biến là gì? *(tr. 191)*
3. Giải thích fan-out qua lab phần 2. Nếu thêm một subscriber thì sao? *(mục 6)*
4. Standard vs FIFO queue khác nhau ra sao? Khi nào cần FIFO? *(mục 2, 7)*
5. Điền: "đơn hàng mới cần gửi email + ghi analytics + trừ kho cùng lúc" → dịch vụ nào? "1 triệu ảnh cần resize dần" → dịch vụ nào? *(mục 5)*

## Tóm tắt một trang

```
BÀI 4 — MESSAGING: SQS / SNS / EVENTBRIDGE
─────────────────────────────────────────────────────────
TÁCH RỜI  chèn trung gian để A gửi rồi làm việc khác, B xử lý khi
          rảnh. A gọi thẳng B → B chết/chậm/quá tải là A dính.

SQS  hàng đợi, "tin nằm đó tới khi consumer lấy & xoá" (tr.191).
     POLL (kéo), KHÔNG push (tr.191). 1→1. Giữ tin (đệm tải).
     Standard (nhanh, có thể trùng) vs FIFO (thứ tự, không trùng).

SNS  pub/sub: publisher→topic→MỌI subscriber (tr.210). PUSH (đẩy),
     1→N fan-out. KHÔNG lưu tin (không ai nghe = mất).

EVENTBRIDGE  "dịch vụ tối hậu cho EDA" (tr.223). Endpoint báo router
     "có chuyện xảy ra", không quan tâm tiếp theo (tr.224). Event Bus
     → Rule (pattern) → Target. Định tuyến theo nội dung + lịch.

LAB  SQS send→receive "xử lý note n1". SNS→SQS fan-out: publish →
     queue audit nhận "note n2 vừa được tạo".

CẠM BẪY  SQS poll không push · visibility timeout → xử lý trùng nếu
     quên delete · at-least-once → viết IDEMPOTENT · DLQ cho tin lỗi ·
     SNS không lưu → nối SNS+SQS · EventBridge dễ over-engineer.
```

> [!note] Đào sâu nền tảng
> Nền của messaging & event-driven ở khoá [`cloud-base`](../../cloud-base/README.md):
> - **SQS at-least-once ⇒ consumer BẮT BUỘC idempotent** → [Bài 2 — concurrency & atomicity](../../cloud-base/bai_hoc/bai_02_os-concurrency.md) và [Bài 7 — giao tiếp & thất bại](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md) (vì mạng không phân biệt được "chậm" với "chết" nên buộc retry + idempotency).
> - **Kinesis / DynamoDB Streams (stream) vs S3+Athena (batch)** → [Bài 11 — batch & stream](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md): cùng một log sự kiện bất biến, hai cách đọc.
> - **Thứ tự chỉ trong một shard · idempotency-key > timestamp** → [Bài 15 — đồng hồ & thứ tự](../../cloud-base/bai_hoc/bai_15_dist-dong-ho.md): vì sao không có đồng hồ toàn cục để xếp thứ tự.
> - **Step Functions / saga điều phối nhiều service** → [Bài 16 — transaction & saga](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md): bù trừ thay cho khoá toàn cục.
> - **Schema Registry · message là contract** → [Bài 18 — encoding & schema evolution](../../cloud-base/bai_hoc/bai_18_du-lieu-encoding.md): chỉ thêm field tuỳ chọn; breaking change làm sập consumer cũ.

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.7 Messaging** (`tr. 189–248`): SQS "fully-managed message queue", "decouples... message remains until a consumer picks it up and removes it", SQS là dịch vụ đầu tiên của AWS (tr. 191); "SQS is poll-based not push-based" (tr. 191); Standard vs FIFO, visibility timeout, DLQ (tr. 192+); SNS "publisher→topics→subscribers, topic is the distributor", push-based, 12.5M subscriber/topic (tr. 210); SNS+SQS fan-out (tr. 211+); EventBridge "ultimate service for EDA", API-driven vs event-driven "informs the router... without caring what happens next", Event Bus/Rules/Targets (tr. 223–227). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (SQS, SNS chạy thật).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging ← bạn đang ở đây] · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
