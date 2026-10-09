# Bài 10 — CloudWatch Logs & Insights: tìm kim trong đống log

> [!info] Về bài này
> Dựng từ **Chương 12 — CloudWatch Bonus: Central Logs Management and Analysis with Logs & Insights** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 444–499`).
> [Bài 7](bai_07_observability-cloudwatch.md) đã lo *metric & alarm* (Chương 10 — "có sự cố không?"). Bài này lo nửa còn lại của observability: **log** — "sự cố *là gì*?". Nắm cách log được tổ chức (group/stream), vì sao **log JSON có cấu trúc**, **retention để khỏi đốt tiền**, và **Logs Insights** — truy vấn hàng triệu dòng log như một database.
> Trích theo `Ch. 12` + `tr. X` (số trang **in**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **CloudWatch Logs *và* Logs Insights chạy thật trên LocalStack free** (lab §6 chạy được cả truy vấn Insights).

## Mục lục

1. [Mô hình tư duy: metric báo có sự cố, log kể sự cố gì](#1-mô-hình-tư-duy-metric-báo-có-sự-cố-log-kể-sự-cố-gì)
2. [Log group, stream, event: ba tầng chứa log](#2-log-group-stream-event-ba-tầng-chứa-log)
3. [Structured logging: log JSON để query được](#3-structured-logging-log-json-để-query-được)
4. [Retention: log tốn tiền, đặt hạn lưu](#4-retention-log-tốn-tiền-đặt-hạn-lưu)
5. [Logs Insights: truy vấn log như database](#5-logs-insights-truy-vấn-log-như-database)
6. [Lab 10: structured log, retention, Logs Insights](#6-lab-10-structured-log-retention-logs-insights)
7. [Live Tail và che dữ liệu nhạy cảm](#7-live-tail-và-che-dữ-liệu-nhạy-cảm)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: metric báo có sự cố, log kể sự cố gì

Observability có ba trụ (Bài 7): **metric** (con số theo thời gian — "lỗi tăng vọt lúc 3h"), **log** (sự kiện rời rạc — "request X trả 500 vì Y"), **trace** (đường đi một request qua nhiều service). Metric giỏi báo *có chuyện*; nhưng để biết *chuyện gì*, bạn phải lặn vào log. Bài 7 lo metric/alarm; bài này lo log — và thách thức của log không phải *ghi* (dễ) mà là **tìm lại** đúng dòng cần giữa hàng triệu dòng. Đó là lý do CloudWatch tách riêng một bộ công cụ cho log, với ngôi sao là **Logs Insights**.

## 2. Log group, stream, event: ba tầng chứa log

Mọi `console.log` của Lambda, mọi dòng stdout của container, đều chảy vào CloudWatch Logs — và được tổ chức ba tầng:

> [!quote] Ch. 12 (tr. 445)
> "Logs in CloudWatch reside in Streams, and Streams reside in Log Groups."
>
> *Log trong CloudWatch nằm trong các **Stream**, và Stream nằm trong các **Log Group**.*

Hình dung: **Log Group** = một ứng dụng/dịch vụ (vd `/aws/lambda/notes-api`); **Log Stream** = một nguồn cụ thể trong đó (một phiên bản Lambda, một container instance); **Log Event** = một dòng log (timestamp + message). Một Log Group gom log từ *nhiều* stream — nên khi gỡ lỗi, bạn thường không muốn đọc từng stream mà muốn *truy vấn ngang* cả Group. Đó chính là việc Logs Insights sinh ra để làm.

## 3. Structured logging: log JSON để query được

Đây là quyết định quan trọng nhất về log, và nên lấy *trước* khi viết dòng log đầu tiên:

> [!quote] Ch. 12 (tr. 451)
> "Using structured logging is the basic building block for observability. It is highly recommended to create your logs in a structured format like JSON."
>
> ***Structured logging (log có cấu trúc)** là viên gạch nền của observability. Rất nên tạo log ở **định dạng có cấu trúc như JSON**.*

Khác biệt sống còn: `console.log("note n1 created in 12ms")` là *text thuần* — muốn lọc "request chậm > 50ms" phải regex mò mẫm. Còn `console.log(JSON.stringify({route:"/notes", status:200, ms:12}))` là *dữ liệu* — Logs Insights hiểu các trường `status`, `ms` và cho bạn `filter ms > 50`. Nối thẳng về nền: đây là *encoding có schema* của [cloud-base Bài 18](../../cloud-base/bai_hoc/bai_18_du-lieu-encoding.md) áp vào log — log JSON là một "sự kiện" (event) query được, không phải chuỗi chết. Chọn text thuần = tự trói tay mình khi sự cố ập tới lúc 3h sáng.

## 4. Retention: log tốn tiền, đặt hạn lưu

Log không miễn phí, và cái bẫy nằm ở mặc định:

> [!quote] Ch. 12 (tr. 457)
> "While the main cost driver of CloudWatch Logs is ingestion (by far), it is still important to handle storage."
>
> *Dù **động lực chi phí chính của CloudWatch Logs là ingestion (nạp log vào — áp đảo)**, việc quản lý lưu trữ vẫn quan trọng.*

Và cái bẫy mặc định:

> [!quote] Ch. 12 (tr. 457)
> "If you omit the retention period, logs are stored indefinitely."
>
> *Nếu bạn **bỏ trống thời hạn lưu (retention)**, log được **lưu vô thời hạn**.*

Mặc định "lưu mãi mãi" nghĩa là hoá đơn lưu trữ *tăng không ngừng* với log cũ chẳng ai đọc. Bài học: **luôn đặt retention** cho mỗi Log Group (1 ngày tới 10 năm) theo nhu cầu thật — debug thì vài tuần đủ, tuân thủ/kiểm toán thì lâu hơn. Đây là cùng tư duy "storage có giá" của Bài 3 (S3 storage classes), nhưng nhiều đội quên vì Log Group được tạo *tự động* khi Lambda chạy — tạo ra mà không ai đặt hạn. Lab §6 đặt retention và kiểm.

## 5. Logs Insights: truy vấn log như database

Vũ khí trung tâm của chương:

> [!quote] Ch. 12 (tr. 445)
> "Logs Insights lets you query your different Log Groups like a database with a SQL-like query language."
>
> ***Logs Insights** cho phép bạn **truy vấn các Log Group như một database** bằng một **ngôn ngữ truy vấn kiểu SQL**.*

Thay vì cuộn tay qua từng stream, bạn viết một truy vấn: `fields @message | filter status >= 500 | stats count() as errors`. Cú pháp pipe (`|`) gồm các động từ quen thuộc: `fields` (chọn trường), `filter` (lọc điều kiện), `stats` (gộp: `count`, `avg`, `max`), `sort`, `limit`. Và đây là lúc structured logging (mục 3) trả cổ tức: vì log là JSON, bạn lọc được `filter ms > 50` hay gộp `avg(ms)` — điều bất khả với text thuần. Lab §6 chạy đúng những truy vấn này *thật* trên LocalStack.

## 6. Lab 10: structured log, retention, Logs Insights

Ghi log JSON có cấu trúc cho capstone, đặt retention, rồi truy vấn bằng Logs Insights — tất cả thật trên LocalStack:

```bash
# === LOG GROUP + RETENTION (chống lưu vô thời hạn) ===
awslocal logs create-log-group --log-group-name /app/notes-logs
awslocal logs put-retention-policy --log-group-name /app/notes-logs --retention-in-days 7
awslocal logs describe-log-groups --log-group-name-prefix /app/notes-logs \
  --query 'logGroups[0].retentionInDays' --output text          # -> 7

# === GHI LOG JSON CÓ CẤU TRÚC (status, ms là TRƯỜNG, không phải text) ===
awslocal logs create-log-stream --log-group-name /app/notes-logs --log-stream-name run-1
NOW=$(( $(date +%s) * 1000 ))
cat > ev.json <<EOF
[
 {"timestamp": $NOW,       "message": "{\"level\":\"INFO\",\"route\":\"/notes\",\"status\":200,\"ms\":12}"},
 {"timestamp": $((NOW+1)), "message": "{\"level\":\"ERROR\",\"route\":\"/notes\",\"status\":500,\"ms\":87}"},
 {"timestamp": $((NOW+2)), "message": "{\"level\":\"INFO\",\"route\":\"/health\",\"status\":200,\"ms\":3}"},
 {"timestamp": $((NOW+3)), "message": "{\"level\":\"ERROR\",\"route\":\"/notes\",\"status\":502,\"ms\":40}"}
]
EOF
awslocal logs put-log-events --log-group-name /app/notes-logs \
  --log-stream-name run-1 --log-events file://ev.json

# === LOGS INSIGHTS: truy vấn như database ===
# (1) đếm request lỗi
QID=$(awslocal logs start-query --log-group-name /app/notes-logs \
  --start-time $(( (NOW/1000)-3600 )) --end-time $(( (NOW/1000)+3600 )) \
  --query-string 'fields @message | filter status >= 500 | stats count() as errors' \
  --query 'queryId' --output text)
sleep 2
awslocal logs get-query-results --query-id "$QID" \
  --query 'results[0][?field==`errors`].value' --output text    # -> 2

# (2) độ trễ trung bình & lớn nhất
QID2=$(awslocal logs start-query --log-group-name /app/notes-logs \
  --start-time $(( (NOW/1000)-3600 )) --end-time $(( (NOW/1000)+3600 )) \
  --query-string 'fields ms | stats avg(ms) as avg_ms, max(ms) as max_ms' \
  --query 'queryId' --output text)
sleep 2
awslocal logs get-query-results --query-id "$QID2" --query 'results[0][].value' --output text

# dọn
awslocal logs delete-log-group --log-group-name /app/notes-logs
```

Kết quả chạy thật *(queryId & timestamp tuỳ lần chạy; các con số là tất định)*:

```
# retention (ngày):
7
# Logs Insights — đếm request lỗi (status >= 500):
2
# Logs Insights — độ trễ trung bình & lớn nhất (avg_ms, max_ms):
35.5	87
```

Ba việc hiện ra, và cái thứ ba là điểm nhấn: `filter status >= 500 | stats count()` trả về **2** (hai request 500 và 502), còn `avg(ms)`/`max(ms)` ra **35.5 / 87** — tính *trực tiếp* trên các trường trong log JSON, không regex dòng nào. Đó là sức mạnh structured logging + Logs Insights: log thôi là "chuỗi để đọc", trở thành "dữ liệu để hỏi". Và `retention=7` đảm bảo capstone không âm thầm tích log tới vô cực.

> [!question] Tự thử
> 1. Đổi truy vấn thành `stats count() by route` — đếm request theo từng route. Vì sao điều này bất khả nếu log là text thuần `"GET /notes 200"`?
> 2. Bỏ `put-retention-policy` rồi `describe-log-groups`: trường `retentionInDays` ra gì? (Gợi ý: tr. 457 — "stored indefinitely".)
> 3. Thêm một event `status":404` rồi truy vấn `filter status >= 400 | stats count() by status`: phân biệt lỗi client (4xx) và server (5xx).

## 7. Live Tail và che dữ liệu nhạy cảm

Hai tính năng CloudWatch Logs đáng biết nhưng là **LocalStack Pro / console** (ở đây học bằng khái niệm + cấu hình, không lab free):

> [!quote] Ch. 12 (tr. 483)
> "CloudWatch Live Tail allows you to stream your logs in real time."
>
> ***CloudWatch Live Tail** cho phép bạn **xem log theo thời gian thực (stream)**.*

Live Tail giải nỗi đau "đang dev Lambda, phải mở từng Log Stream mò dòng mới nhất" — nó đổ log *đang chảy* ra màn hình ngay, có highlight/filter theo từ khoá. Hợp lúc đang gỡ lỗi trực tiếp (ngược với Logs Insights hợp điều tra *sau sự cố*).

> [!quote] Ch. 12 (tr. 485)
> "CloudWatch can automatically detect sensitive data and mask it."
>
> *CloudWatch có thể **tự phát hiện dữ liệu nhạy cảm và che (mask)** nó.*

Cạm bẫy số một của log là *lỡ ghi dữ liệu nhạy cảm* (số thẻ, email, địa chỉ) — rồi kỹ sư dev/prod đều đọc được. **Data Protection Policy** của CloudWatch dò các mẫu (credit card, email...) và che chúng ngay khi nạp. Nối về nền: đây là một mặt của *bảo mật* ([cloud-base Bài 14](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md)) — bí mật không chỉ ở lúc truyền mà cả ở nơi dữ liệu *nằm lại* (log).

> [!note] Đào sâu nền tảng
> Bản chất CS của bài này ở khoá [`cloud-base`](../../cloud-base/README.md):
> - **Log = một event stream append-only** → [Bài 11 — batch & stream](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md): Logs Insights "đọc toàn bộ" (batch) còn Live Tail "theo đuôi" (stream) — hai cách đọc cùng một log bất biến.
> - **Structured logging = encoding có schema** → [Bài 18 — encoding & schema evolution](../../cloud-base/bai_hoc/bai_18_du-lieu-encoding.md): log JSON là dữ liệu query được, và đổi "schema log" cũng cần kỷ luật như đổi schema event.
> - **Masking = bí mật ở nơi dữ liệu nằm lại** → [Bài 14 — bảo mật & mật mã](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md).

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 10.1 — Ba tầng chứa log của CloudWatch, từ nhỏ tới lớn?
> **Đáp:** Log **Event** (một dòng) → Log **Stream** (một nguồn: một phiên bản Lambda/container) → Log **Group** (một ứng dụng/dịch vụ). Group gom nhiều stream.

> [!question] Thẻ 10.2 — Vì sao nên log JSON thay vì text thuần?
> **Đáp:** JSON là **dữ liệu có trường** → Logs Insights `filter`/`stats` theo `status`, `ms`... Text thuần phải regex mò mẫm, không gộp/lọc theo trường được.

> [!question] Thẻ 10.3 — Cái bẫy mặc định của retention là gì? Cách tránh?
> **Đáp:** bỏ trống retention → log **lưu vô thời hạn** → hoá đơn lưu trữ tăng mãi. Luôn **đặt retention** (1 ngày–10 năm) cho mỗi Log Group, nhất là Group Lambda tạo tự động.

> [!question] Thẻ 10.4 — Logs Insights là gì? Một truy vấn mẫu?
> **Đáp:** truy vấn Log Group như database bằng cú pháp SQL-like + pipe. VD: `fields @message | filter status >= 500 | stats count() as errors`.

> [!question] Thẻ 10.5 — Live Tail vs Logs Insights dùng khi nào?
> **Đáp:** Live Tail = xem log **realtime** lúc đang gỡ lỗi trực tiếp. Logs Insights = **điều tra sau sự cố** trên khối log đã có (truy vấn/gộp).

> [!question] Thẻ 10.6 — Vì sao masking quan trọng? Nối về khái niệm nền nào?
> **Đáp:** tránh lỡ ghi dữ liệu nhạy cảm (thẻ/email) mà mọi kỹ sư đọc được. Là *bí mật ở nơi dữ liệu nằm lại* — mặt khác của bảo mật (cloud-base Bài 14).

## 9. Câu hỏi tự kiểm tra

1. Ba tầng group/stream/event là gì? Vì sao gỡ lỗi thường muốn truy vấn *ngang* cả Group? *(mục 2, tr. 445)*
2. Structured logging là gì, vì sao là "viên gạch nền"? Cho ví dụ text vs JSON. *(mục 3, tr. 451)*
3. Động lực chi phí chính của Logs là gì? Cái bẫy retention mặc định? *(mục 4, tr. 457)*
4. Logs Insights cho làm gì? Viết một truy vấn đếm lỗi theo route. *(mục 5, tr. 445)*
5. Chạy lab §6. Vì sao `filter status >= 500` đếm được 2 và `avg(ms)` tính được — mà text thuần thì không? *(mục 6)*
6. Live Tail vs Logs Insights khác dụng. Masking giải cạm bẫy log nào? *(mục 7, tr. 483, 485)*

## Tóm tắt một trang

```
BÀI 10 — CLOUDWATCH LOGS & INSIGHTS (Ch.12)
─────────────────────────────────────────────────────────
VAI TRÒ  metric (Bài 7) báo "CÓ sự cố"; log kể "sự cố LÀ GÌ". Khó không ở
   ghi log mà ở TÌM LẠI đúng dòng giữa hàng triệu dòng.

BA TẦNG  Event (1 dòng) → Stream (1 nguồn) → Log Group (1 app) (tr.445).

STRUCTURED LOGGING  log JSON, không text thuần (tr.451): status/ms là TRƯỜNG
   → query được. = encoding có schema (cloud-base Bài 18).

RETENTION  chi phí chính = ingestion; bỏ trống retention → lưu VÔ THỜI HẠN
   (tr.457) → luôn đặt hạn (1d–10y), nhất là Log Group Lambda tạo tự động.

LOGS INSIGHTS  truy vấn Log Group như DATABASE, cú pháp SQL-like + pipe
   (tr.445): fields | filter status>=500 | stats count() / avg(ms).

LAB  retention=7; filter status>=500 → 2 lỗi; avg_ms/max_ms = 35.5/87 —
   tính trực tiếp trên trường JSON, chạy THẬT trên LocalStack.

LIVE TAIL  xem log realtime lúc dev (tr.483). MASKING  tự che dữ liệu nhạy
   cảm thẻ/email (tr.485) = bí mật ở nơi dữ liệu nằm lại (cloud-base Bài 14).
```

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.12 CloudWatch Logs & Insights** (`tr. 444–499`): Stream/Log Group & "query like a database with SQL-like language" (tr. 445); structured logging/JSON "basic building block" (tr. 451); ingestion là cost driver chính & "stored indefinitely" nếu bỏ retention (tr. 457); Live Tail "stream in real time" (tr. 483); "automatically detect sensitive data and mask it" (tr. 485). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (CloudWatch Logs **và Logs Insights** chạy thật).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.
- Đào sâu nền: [`cloud-base` Bài 11 (batch/stream)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md), [Bài 18 (encoding)](../../cloud-base/bai_hoc/bai_18_du-lieu-encoding.md), [Bài 14 (bảo mật)](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md).

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights ← bạn đang ở đây]

Xem thêm [README khoá học](../README.md).
