# Bài 4 — Thiết kế hệ thông báo tin cậy

> [!info] Về bài này
> **Archetype 4 — giao việc bất đồng bộ cho đáng tin.** Bài 3 đẩy phát tán vào hàng đợi; bài này hỏi: làm sao giao **không mất, không kẹt** khi downstream (gửi email/SMS/push) *sẽ* hỏng tạm thời? Ba công cụ nền: **timeout, retry, backoff + jitter**; cộng **DLQ** (cô lập message độc) và cách chống **backlog** phình. Đây là nơi lý thuyết partial failure (cloud-base Bài 7) thành cấu hình SQS cụ thể.
> Nguồn: **BL** *Timeouts, retries, and backoff with jitter* + *Avoiding insurmountable queue backlogs*. Nền: [cloud-base Bài 7 (thất bại/idempotency)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md); dịch vụ: [aws-fund Bài 4 (SQS/DLQ)](../../aws-fund/bai_hoc/bai_04_messaging.md).
> **Lab:** SQS + DLQ trên LocalStack; demo backoff+jitter bằng Node 22.
> Nên đọc trước: [Bài 3 — fan-out](bai_03_newsfeed-fanout.md), [cloud-base Bài 7](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: hàng đợi, worker, DLQ](#2-kiến-trúc-hàng-đợi-worker-dlq)
3. [Đào sâu: timeout, retry, backoff, jitter](#3-đào-sâu-timeout-retry-backoff-jitter)
4. [Lab: DLQ cô lập poison và backoff jitter](#4-lab-dlq-cô-lập-poison-và-backoff-jitter)
5. [Soi Well-Architected](#5-soi-well-architected)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] Nhà cung cấp email "chập chờn" lúc nửa đêm
> Hệ của bạn gửi email xác nhận đơn hàng qua một dịch vụ bên ngoài (SendGrid/SES). 11 giờ đêm, dịch vụ đó *quá tải tạm thời*, trả 503 cho 20% request. Cách làm ngây thơ: *try/catch, hỏng thì gửi lại ngay trong vòng lặp*. Hậu quả: hàng nghìn server của bạn **cùng** gửi lại **cùng lúc**, dồn thêm tải lên dịch vụ đang ngắc ngoải → nó sập hẳn (bạn vừa tự DDoS đối tác). Và một email có payload hỏng thì lặp vô hạn, ngốn hết worker. Bài này là cách retry *tử tế*.

**Chức năng:** nhận yêu cầu gửi thông báo (email/SMS/push), giao tới nhà cung cấp bên ngoài. **Phi chức năng:** **không mất** thông báo (ít nhất một lần), chịu được downstream hỏng tạm thời, không để một message hỏng chặn cả dòng, không tự gây bão lên downstream khi nó đang yếu.

Ràng buộc then chốt đến từ cloud-base Bài 7: nhà cung cấp bên ngoài *sẽ* timeout/5xx lúc này lúc khác, và mạng *sẽ* nuốt hồi đáp. Vậy hệ phải **retry** — nhưng retry *mù* lại là con dao hai lưỡi (mục 3). Và vì giao "ít nhất một lần", consumer **phải idempotent** (Bài 5).

## 2. Kiến trúc: hàng đợi, worker, DLQ

```
   producer ─▶ SQS "notif-main" ─▶ worker (Lambda) ─▶ nhà cung cấp (email/SMS)
                   │                     │ lỗi → KHÔNG xoá message
                   │                     │ (SQS giao lại sau visibility timeout)
                   │  sau maxReceiveCount lần lỗi
                   └────────────────────▶ SQS "notif-dlq"  (dead-letter: cô lập)
```

SQS giữ message tới khi worker *xoá* (xử lý thành công) — hỏng thì message tự *quay lại* để thử lần sau (at-least-once). Nhưng một message **độc** (payload hỏng, mãi mãi fail) sẽ lặp vô hạn, ngốn worker — nên sau `maxReceiveCount` lần, SQS đẩy nó sang **DLQ** để cô lập, điều tra riêng, không chặn dòng chính. Phần tinh tế — retry *thế nào* — ở mục 3.

## 3. Đào sâu: timeout, retry, backoff, jitter

> [!quote] BL: timeouts-retries-and-backoff-with-jitter
> "To build resilient systems, we employ three essential tools: timeouts, retries, and backoff."
>
> *Để xây hệ kiên cường, ta dùng ba công cụ cốt yếu: **timeout, retry, và backoff**.*

> [!example] Ba ẩn dụ
> **Backoff** = gõ cửa mà không ai mở thì đừng gõ dồn mỗi giây; chờ 1s, rồi 2s, rồi 4s... (để người ta kịp ra). **Jitter** = một đám đông đừng *cùng* bấm chuông đúng giây thứ 2; mỗi người lệch một chút để không dồn cục. **DLQ (dead-letter queue)** = cái *rổ "hàng lỗi"*: thư nào thử mãi không gửi được thì bỏ sang rổ riêng để xem sau, không để nó chắn cả dây chuyền.

Timeout (Bài 7): bỏ chờ sau một khoảng — vì "chậm" không phân biệt được "chết". Retry: thử lại vì phần lớn lỗi là *tạm thời*. Nhưng retry ngay và đồng loạt thì tai hoạ:

> [!quote] BL: timeouts-retries-and-backoff-with-jitter
> "If errors are caused by load, retries can be ineffective if all clients retry at the same time."
>
> *Nếu lỗi do **tải**, retry sẽ **vô dụng nếu mọi client cùng retry một lúc** (dồn thêm tải lên hệ đang yếu — bão retry).*

Hai liều thuốc. **Backoff** — chờ lâu dần:

> [!quote] BL: timeouts-retries-and-backoff-with-jitter
> "The most common pattern is an exponential backoff, where the wait time is increased exponentially after every attempt."
>
> *Mẫu phổ biến nhất là **exponential backoff**: thời gian chờ **tăng theo cấp số nhân** sau mỗi lần thử* (và *cap* lại ở một trần, vì hàm mũ lớn rất nhanh).

Và **jitter** — phá sự đồng loạt:

> [!quote] BL: timeouts-retries-and-backoff-with-jitter
> "Jitter adds some amount of randomness to the backoff to spread the retries around in time."
>
> ***Jitter** thêm một lượng **ngẫu nhiên** vào backoff để **trải các lần retry ra theo thời gian**.*

Thiếu jitter, mọi client backoff *cùng* một lịch → chúng dồn lại đập downstream theo từng đợt đồng bộ (thundering herd). Có jitter, chúng rải đều, cho downstream thở để hồi phục. Còn khi message *dồn* vì downstream chậm lâu, ta sang bài toán backlog:

> [!quote] BL: avoiding-insurmountable-queue-backlogs
> "I discuss strategies we use at Amazon to deal with queue backlog scenarios – design approaches we take to drain queues quickly and to prioritize workloads. Most importantly, I describe how to prevent queue backlogs from building up in the first place."
>
> *... các chiến lược xử lý **backlog hàng đợi**: cách **rút cạn (drain) queue nhanh** và **ưu tiên** công việc; quan trọng nhất là cách **ngăn backlog hình thành ngay từ đầu**.*

DLQ chính là một phần của chống backlog: tách message độc (mãi fail) ra khỏi dòng chính để chúng không giữ chỗ và kéo tụt tốc độ rút queue.

## 4. Lab: DLQ cô lập poison và backoff jitter

**(a)** DLQ: sau `maxReceiveCount=2` lần nhận-mà-không-xoá, SQS tự đẩy message độc sang DLQ. Chạy thật trên LocalStack:

```bash
DLQ=$(awslocal sqs create-queue --queue-name notif-dlq --query 'QueueUrl' --output text)
DLQ_ARN=$(awslocal sqs get-queue-attributes --queue-url $DLQ --attribute-names QueueArn \
          --query 'Attributes.QueueArn' --output text)
MAIN=$(awslocal sqs create-queue --queue-name notif-main \
  --attributes "{\"RedrivePolicy\":\"{\\\"deadLetterTargetArn\\\":\\\"$DLQ_ARN\\\",\\\"maxReceiveCount\\\":\\\"2\\\"}\",\"VisibilityTimeout\":\"0\"}" \
  --query 'QueueUrl' --output text)
awslocal sqs send-message --queue-url $MAIN --message-body '{"to":"bob","msg":"poison"}'
for i in 1 2 3; do                       # consumer lỗi liên tục: nhận mà không xoá
  got=$(awslocal sqs receive-message --queue-url $MAIN --query 'length(Messages)' --output text)
  echo "lần $i: main trả ${got:-0} message"
done
awslocal sqs receive-message --queue-url $DLQ --query 'Messages[0].Body' --output text  # đã sang DLQ
```

Kết quả chạy thật:

```
lần 1: main trả 1 message
lần 2: main trả 1 message
lần 3: main trả 0 message
{"to":"bob","msg":"poison"}
```

Lần 1–2 message quay lại main (retry); lần 3 main trống vì nó đã bị đẩy sang DLQ (vượt maxReceiveCount=2) — nằm chờ điều tra, không còn chặn dòng chính.

**(b)** Backoff + jitter (vì sao jitter cần thiết), tất định bằng PRNG seed cố định:

```typescript
// Retry an toàn = exponential backoff + JITTER. Backoff giãn thời gian giữa các
// lần thử; jitter thêm ngẫu nhiên để các client KHÔNG retry cùng lúc (tránh bão
// retry đồng loạt). PRNG seed cố định → output tất định để minh hoạ.
function mulberry32(seed: number): () => number {
  let a = seed;
  return () => { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}
const BASE = 100, CAP = 2000;                 // ms
const cappedExp = (n: number) => Math.min(CAP, BASE * 2 ** n);

console.log("attempt | backoff thuần | full jitter (3 client khác seed)");
console.log("--------+---------------+-----------------------------------");
const rngs = [mulberry32(1), mulberry32(2), mulberry32(3)];
for (let n = 0; n < 6; n++) {
  const b = cappedExp(n);
  const jit = rngs.map(r => Math.round(r() * b));   // full jitter: random trong [0, backoff]
  console.log(`   ${n}    |   ${String(b).padStart(5)} ms    | ${jit.map(j => String(j).padStart(5)+"ms").join("  ")}`);
}
console.log("\nBackoff thuần: mọi client chờ ĐÚNG một khoảng → retry CÙNG LÚC (bão).");
console.log("Full jitter: mỗi client chờ ngẫu nhiên trong [0, backoff] → TRẢI ĐỀU.");
console.log("Cap 2000ms: backoff không phình vô hạn (exponential grows quickly).");
```

Kết quả chạy thật *(tất định nhờ seed)*:

```
attempt | backoff thuần | full jitter (3 client khác seed)
--------+---------------+-----------------------------------
   0    |     100 ms    |    63ms     73ms     72ms
   1    |     200 ms    |     1ms     65ms      8ms
   2    |     400 ms    |   211ms    114ms    182ms
   3    |     800 ms    |   785ms    430ms     60ms
   4    |    1600 ms    |  1549ms   1400ms   1221ms
   5    |    2000 ms    |   562ms   1262ms    962ms

Backoff thuần: mọi client chờ ĐÚNG một khoảng → retry CÙNG LÚC (bão).
Full jitter: mỗi client chờ ngẫu nhiên trong [0, backoff] → TRẢI ĐỀU.
Cap 2000ms: backoff không phình vô hạn (exponential grows quickly).
```

Cột "backoff thuần": cả ba client chờ *đúng* 100/200/400... → chúng retry **cùng khoảnh khắc**, đập downstream theo đợt đồng bộ. Cột jitter: mỗi client một số ngẫu nhiên trong `[0, backoff]` → các lần retry **rải đều**, downstream không bị dồn. Đây là lý do AWS SDK bật exponential backoff + jitter mặc định. Lưu ý mắt xích: retry chỉ an toàn nếu consumer **idempotent** (Bài 5) — vì at-least-once nghĩa là một thông báo có thể gửi hai lần khi retry trúng khe "hồi đáp bị mất" (cloud-base Bài 7).

> [!note] Tự thử
> 1. Trong (a), đổi `maxReceiveCount` lên `5`: message độc lặp 5 lần mới vào DLQ. Trade-off giữa "thử đủ nhiều" và "không phí worker vào message chết"?
> 2. Trong (b), cho cả 3 client *cùng* seed: jitter mất tác dụng (giống nhau). Vì sao mỗi client cần nguồn ngẫu nhiên riêng?
> 3. Bỏ cap (CAP=∞): attempt 10 chờ bao lâu? Vì sao phải cap?

## 5. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | at-least-once + retry + DLQ → không mất, không kẹt | consumer phải idempotent (Bài 5) |
| Performance | backoff+jitter tránh bão retry; worker scale theo queue depth | — |
| Cost | DLQ ngừng đốt worker vào message chết | theo dõi để không trả cho retry vô ích |
| Security | IAM giới hạn ai gửi/nhận queue | — |
| Operational | alarm trên **DLQ depth** + **queue age** (backlog) | DLQ có message = cần điều tra (aws-fund Bài 7) |

Nguyên tắc đọng lại: **retry tử tế** (backoff+jitter) + **cô lập cái chết** (DLQ) + **đo backlog**. Nhưng "at-least-once" đẩy một bài toán mới sang người dùng: nếu thông báo-trùng-lặp là *tính tiền* thì sao? Đó là Bài 5 (idempotency).

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — Ba công cụ nền của hệ kiên cường (BL)?
> **Đáp:** **timeout, retry, backoff**. (Cộng jitter để trải retry, DLQ để cô lập message độc.)

> [!question] Thẻ 4.2 — Vì sao retry đồng loạt phản tác dụng?
> **Đáp:** nếu lỗi do *tải*, mọi client cùng retry một lúc **dồn thêm tải** lên hệ đang yếu → bão retry, kéo dài sự cố.

> [!question] Thẻ 4.3 — Backoff và jitter mỗi cái chữa gì?
> **Đáp:** **backoff** (exponential, có cap): chờ lâu dần để downstream hồi phục. **Jitter**: thêm ngẫu nhiên để các client không retry cùng khoảnh khắc (phá thundering herd).

> [!question] Thẻ 4.4 — DLQ giải quyết vấn đề gì? Khi nào một message vào DLQ?
> **Đáp:** cô lập **message độc** (mãi fail) khỏi dòng chính để không lặp vô hạn + chặn queue. Vào DLQ sau khi nhận quá `maxReceiveCount` lần mà không xử lý xong.

> [!question] Thẻ 4.5 — "At-least-once" ép buộc điều gì ở consumer? Vì sao?
> **Đáp:** consumer phải **idempotent** — vì retry khi "hồi đáp bị mất" (cloud-base Bài 7) khiến một message được xử lý >1 lần.

## 7. Câu hỏi tự kiểm tra

1. Vì sao hệ thông báo *phải* retry? Ràng buộc nào đến từ cloud-base Bài 7? *(mục 1)*
2. SQS giao at-least-once ra sao? Vai trò visibility timeout + maxReceiveCount? *(mục 2, 4)*
3. Backoff vs jitter: mỗi cái chống gì? Vì sao cần cả hai? *(mục 3, BL)*
4. Chạy lab (a). Vì sao lần 3 main trống? DLQ phục vụ chống backlog thế nào? *(mục 4)*
5. Chạy lab (b). Giải thích vì sao cột jitter "trải đều" còn backoff thuần thì "dồn đợt". *(mục 4)*

## Tóm tắt một trang

```
BÀI 4 — HỆ THÔNG BÁO TIN CẬY
─────────────────────────────────────────────────────────
VẤN ĐỀ  giao thông báo KHÔNG MẤT, downstream SẼ hỏng tạm (cloud-base Bài 7).
   → phải retry; at-least-once → consumer phải IDEMPOTENT (Bài 5).

KIẾN TRÚC  producer → SQS main → worker → nhà cung cấp. Lỗi → message quay
   lại (retry). Quá maxReceiveCount → DLQ (cô lập message độc).

ĐÀO SÂU  3 công cụ: timeout+retry+backoff (BL). Retry đồng loạt = BÃO (dồn
   tải lên hệ yếu). Chữa: exponential backoff CÓ CAP + JITTER (ngẫu nhiên để
   TRẢI retry). Backlog: drain nhanh + ưu tiên + NGĂN hình thành (BL).

LAB  (a) SQS DLQ: nhận 2 lần → lần 3 main trống, message sang DLQ (cô lập).
   (b) backoff thuần = retry cùng lúc; full jitter = rải đều [0,backoff].

6 TRỤ  reliability (không mất/không kẹt); alarm DLQ depth + queue age.
   Tiếp: at-least-once → thông báo-trùng nếu là TÍNH TIỀN? → idempotency (Bài 5).
```

## Nguồn

- **Amazon Builders' Library** — *Timeouts, retries, and backoff with jitter*: ba công cụ, retry đồng loạt vô dụng, exponential backoff, jitter. `tai_lieu/bl_timeouts-retries-and-backoff-with-jitter.txt`. — *Avoiding insurmountable queue backlogs*: drain/ưu tiên/ngăn backlog. `tai_lieu/bl_avoiding-insurmountable-queue-backlogs.txt`.
- Nền: [cloud-base Bài 7 — thất bại & idempotency](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md).
- Dịch vụ: [aws-fund Bài 4 — SQS/SNS/DLQ](../../aws-fund/bai_hoc/bai_04_messaging.md), [Bài 7 — alarm DLQ](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · **[Bài 4 — Hệ thông báo tin cậy] ← bạn đang ở đây** · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
