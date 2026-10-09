# Bài 7 — Observability: CloudWatch — mắt và tai của hệ thống

> [!info] Về bài này
> Dựng từ **Chương 10 — Observability** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 345–371`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vòng lặp nhớ-lâu: *mô hình tư duy → cách hoạt động → lab LocalStack → thẻ ôn → capstone*.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **CloudWatch Logs, Metrics, Alarms** chạy tốt trên LocalStack free (lab thật dưới đây).

## Mục lục

1. [Mô hình tư duy: ba trụ observability](#1-mô-hình-tư-duy-ba-trụ-observability)
2. [CloudWatch là trung tâm log và metric](#2-cloudwatch-là-trung-tâm-log-và-metric)
3. [Logs: text output của ứng dụng](#3-logs-text-output-của-ứng-dụng)
4. [Metrics & Alarms: con số theo thời gian, ngưỡng, cảnh báo](#4-metrics--alarms-con-số-theo-thời-gian-ngưỡng-cảnh-báo)
5. [Lab 7: logs, metrics, alarm](#5-lab-7-logs-metrics-alarm)
6. [Cạm bẫy: log tốn tiền, cardinality](#6-cạm-bẫy-log-tốn-tiền-cardinality)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: ba trụ observability

Khi hệ thống chạy trên cloud, bạn *không thấy* nó bằng mắt. **Observability** là khả năng *hiểu bên trong hệ đang xảy ra gì* từ dữ liệu nó phát ra — ba trụ:

| Trụ | Trả lời câu hỏi | Ví dụ |
| :--- | :--- | :--- |
| **Logs** (nhật ký) | "chuyện gì đã xảy ra, chi tiết?" | "Lambda xử lý note n1, lỗi ở dòng X" |
| **Metrics** (số đo) | "bao nhiêu, nhanh/chậm thế nào theo thời gian?" | số lần gọi Lambda, CPU, độ trễ |
| **Traces** (dấu vết) | "một request đi qua những dịch vụ nào, chậm ở đâu?" | API GW → Lambda → DynamoDB: 200ms ở DB |

CloudWatch lo Logs + Metrics + Alarms; traces là **X-Ray** (giới thiệu ngắn ở chương). Nhớ ba trụ thì biết *khi debug nên nhìn vào đâu*.

## 2. CloudWatch là trung tâm log và metric

> [!quote] Ch. 10 — CloudWatch (tr. 347)
> "Amazon CloudWatch is AWS's central logging and metrics service. Each AWS service logs to CloudWatch."
>
> *CloudWatch là dịch vụ **log và metric trung tâm** của AWS. **Mọi** dịch vụ AWS đều log vào CloudWatch.*

Và một lời nhắn thẳng cho người mới:

> [!quote] Ch. 10 — CloudWatch (tr. 347)
> "CloudWatch is one of the most underrated services for beginners to learn. […] It doesn't matter how you develop your application on AWS; you will need to use CloudWatch."
>
> *CloudWatch là một trong những dịch vụ **bị đánh giá thấp nhất** với người mới. […] Dù bạn phát triển app trên AWS kiểu gì, bạn **sẽ phải dùng** CloudWatch.*

CloudWatch gồm nhiều "sản phẩm con": **Logs, Metrics, Alarms** (ta tập trung) và **Synthetics** (giám sát tổng hợp).

## 3. Logs: text output của ứng dụng

> [!quote] Ch. 10 — CloudWatch Logs (tr. 347)
> "This is the centralized logging space in AWS. Services like Lambda, API Gateway, or ECS log directly into CloudWatch Logs."
>
> *Đây là **không gian log tập trung** của AWS. Các dịch vụ như Lambda, API Gateway, ECS log *thẳng* vào CloudWatch Logs.*

> [!quote] Ch. 10 — Logs (tr. 347)
> "Logs are the text output of your application. For example, if you put a print statement (console.log for Node.js) into your Lambda function and run it, you will find the log in CloudWatch."
>
> *Log là **output dạng text** của ứng dụng. Ví dụ: bạn đặt một `console.log` trong hàm Lambda, chạy nó — bạn sẽ thấy log đó trong CloudWatch.*

Cấu trúc: **Log Group** (một "thư mục" log, vd `/aws/lambda/notes-api`) → **Log Stream** (một dòng chảy log, thường một container/lần chạy) → **Log Events** (từng dòng log, có timestamp). Thực hành tốt: **structured logging** (log JSON thay vì text thuần) để *query được* — sách giới thiệu *Powertools for AWS Lambda* với JSON logger.

## 4. Metrics & Alarms: con số theo thời gian, ngưỡng, cảnh báo

**Metrics** là *con số theo thời gian*: số lần Lambda invoke, dung lượng DB còn trống, CPU của ECS… AWS tự phát metric cho mọi dịch vụ; bạn cũng *put custom metric* (vd "số note được tạo"). Metric có **namespace** (nhóm), **tên**, **giá trị**, và **dimension** (nhãn phân loại).

**Alarms** theo dõi một metric và *kích hoạt* khi vượt ngưỡng:

> *"Based on these metrics, you can create alarms for certain thresholds. If your free space falls below a certain threshold, you will be notified."* (Ch.10, tr.347)

Alarm thường bắn vào **SNS** ([Bài 4](bai_04_messaging.md)) → email/SMS/Lambda. Ví dụ capstone: alarm "lỗi 5xx > 1% trong 5 phút" → báo ngay. Alarm có ba trạng thái: `OK`, `ALARM`, `INSUFFICIENT_DATA`.

## 5. Lab 7: logs, metrics, alarm

Dựng *mắt và tai* cho capstone: ghi log, phát metric, đặt alarm — cả ba thật trên LocalStack:

```bash
# === LOGS ===
awslocal logs create-log-group --log-group-name /app/notes
awslocal logs create-log-stream --log-group-name /app/notes --log-stream-name run-1
TS=$(( $(date +%s) * 1000 ))
awslocal logs put-log-events --log-group-name /app/notes --log-stream-name run-1 \
  --log-events timestamp=$TS,message="note n1 đã được tạo" \
               timestamp=$((TS+1)),message="note n2 đã được tạo"
awslocal logs get-log-events --log-group-name /app/notes --log-stream-name run-1 \
  --query 'events[].message' --output text

# === METRICS (custom) ===
awslocal cloudwatch put-metric-data --namespace NotesApp --metric-name NotesCreated --value 1
awslocal cloudwatch put-metric-data --namespace NotesApp --metric-name NotesCreated --value 3
awslocal cloudwatch list-metrics --namespace NotesApp --query 'Metrics[].MetricName' --output text

# === ALARM: cảnh báo khi tổng NotesCreated vượt 100 ===
awslocal cloudwatch put-metric-alarm --alarm-name too-many-notes --namespace NotesApp \
  --metric-name NotesCreated --statistic Sum --period 300 --threshold 100 \
  --comparison-operator GreaterThanThreshold --evaluation-periods 1
awslocal cloudwatch describe-alarms --alarm-names too-many-notes \
  --query 'MetricAlarms[].{Name:AlarmName,Threshold:Threshold,State:StateValue}' --output table

# dọn
awslocal logs delete-log-group --log-group-name /app/notes
awslocal cloudwatch delete-alarms --alarm-names too-many-notes
```

Kết quả chạy thật:

```
# đọc log:
note n1 đã được tạo	note n2 đã được tạo
# metric đã phát:
NotesCreated
# alarm:
------------------------------------------
|             DescribeAlarms             |
+-----------------+--------+-------------+
|      Name       | State  |  Threshold  |
+-----------------+--------+-------------+
|  too-many-notes |  OK    |  100.0      |
+-----------------+--------+-------------+
```

Ba trụ hiện ra: *log* (biết chuyện gì xảy ra), *metric* (`NotesCreated` — đếm được), *alarm* (ngưỡng 100, đang `OK` vì tổng chưa vượt). Trong capstone, Lambda chỉ cần `console.log` là có log; phát `NotesCreated` mỗi lần tạo note; và alarm canh lỗi/chi phí.

> [!question] Tự thử
> 1. Đổi `--threshold` xuống `2` và nghĩ: với tổng metric = 4, alarm nên ở trạng thái nào? (Thử phát thêm metric rồi `describe-alarms`.)
> 2. Thêm `--dimensions Name=env,Value=dev` vào `put-metric-data`. `list-metrics` có thấy dimension không?
> 3. `console.log(JSON.stringify({level:"error", noteId:"n1"}))` trong Lambda — vì sao JSON *query được* còn text thuần thì không?

## 6. Cạm bẫy: log tốn tiền, cardinality

> [!warning] Thực tế & cạm bẫy Observability
> - **Log TỐN TIỀN** (cạm bẫy số 1, đã cảnh báo ở [Bài 0](bai_00_hoc-aws-nho-lau-va-localstack.md)). CloudWatch tính theo **GB ingest**. Log debug/trace bừa, log cả object JSON khổng lồ mỗi request → "terabytes of ingested logs" = hoá đơn sốc (tr.9). Đặt **log level** hợp lý; **retention** (tự xoá log cũ, mặc định *giữ mãi mãi* = tốn mãi mãi).
> - **Structured logging > text.** Log JSON có trường (`level`, `requestId`, `noteId`) để *query/filter* bằng CloudWatch Logs Insights. Text thuần chỉ `grep` thô.
> - **Metric cardinality.** Mỗi tổ hợp dimension là một metric *riêng* tính tiền. Đừng để dimension có giá trị vô hạn (vd `userId` làm dimension) → bùng nổ cardinality + chi phí.
> - **Alarm phải *hành động được*.** Alarm bắn mà không ai làm gì = nhiễu → người ta tắt. Mỗi alarm nên nối SNS tới đúng người + có runbook.
> - **Log ≠ metric ≠ trace.** Debug một lỗi cụ thể → *logs*. Theo dõi sức khoẻ tổng thể → *metrics*. Tìm chặng chậm trong một request xuyên nhiều dịch vụ → *traces (X-Ray)*. Dùng đúng trụ.
> - **LocalStack:** Logs/Metrics/Alarms cơ bản chạy, nhưng *đánh giá alarm theo thời gian thật* và X-Ray thì hạn chế — đừng dựa vào LocalStack để kiểm hành vi alarm production.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — Ba trụ observability và mỗi trụ trả lời gì?
> **Đáp:** Logs (chuyện gì xảy ra, chi tiết) · Metrics (bao nhiêu/nhanh-chậm theo thời gian) · Traces (một request đi qua đâu, chậm ở đâu).

> [!question] Thẻ 7.2 — Cấu trúc CloudWatch Logs?
> **Đáp:** Log Group (thư mục, vd `/aws/lambda/x`) → Log Stream (một dòng chảy/lần chạy) → Log Events (dòng log có timestamp).

> [!question] Thẻ 7.3 — `console.log` trong Lambda đi đâu?
> **Đáp:** vào **CloudWatch Logs** (log group `/aws/lambda/<tên-hàm>`) — tự động, không cần cấu hình gì.

> [!question] Thẻ 7.4 — Alarm hoạt động ra sao? Ba trạng thái?
> **Đáp:** theo dõi một metric, kích hoạt khi vượt ngưỡng → thường bắn SNS. Trạng thái: `OK`, `ALARM`, `INSUFFICIENT_DATA`.

> [!question] Thẻ 7.5 — Cạm bẫy chi phí lớn nhất của CloudWatch?
> **Đáp:** **log ingest theo GB**. Log bừa + giữ mãi mãi = tốn. Đặt log level + retention; dùng structured logging để query hiệu quả.

## 8. Câu hỏi tự kiểm tra

1. Kể ba trụ observability. Khi debug một lỗi 500 cụ thể, bạn nhìn trụ nào? *(mục 1)*
2. Vì sao sách nói CloudWatch "bị đánh giá thấp" nhưng "chắc chắn phải dùng"? *(tr. 347)*
3. Phân biệt Log Group / Log Stream / Log Event. *(mục 3)*
4. Metric vs Alarm khác nhau ra sao? Alarm thường bắn vào đâu? *(mục 4)*
5. Hai cách giảm chi phí CloudWatch Logs? *(mục 6)*

## Tóm tắt một trang

```
BÀI 7 — OBSERVABILITY: CLOUDWATCH
─────────────────────────────────────────────────────────
3 TRỤ  Logs (chuyện gì xảy ra) · Metrics (bao nhiêu/theo thời gian)
       · Traces (request đi đâu, chậm ở đâu = X-Ray).

CLOUDWATCH  "central logging & metrics, MỌI dịch vụ log vào đây" (tr.347).
       "bị đánh giá thấp nhưng CHẮC CHẮN phải dùng" (tr.347).
       Sản phẩm con: Logs, Metrics, Alarms, Synthetics.

LOGS  "text output của app; console.log → thấy ở CloudWatch" (tr.347).
      Log Group → Log Stream → Log Events. Structured (JSON) > text.

METRICS  số theo thời gian (invoke/CPU/latency) + custom. namespace +
      name + value + dimension.
ALARMS  metric vượt ngưỡng → bắn SNS. State: OK/ALARM/INSUFFICIENT_DATA.

LAB  create-log-group → put/get-log-events ("note n1/n2 đã tạo") ·
     put-metric-data NotesApp/NotesCreated · put-metric-alarm (ngưỡng
     100, State OK).

CẠM BẪY  LOG TỐN TIỀN (GB ingest) → log level + retention · structured
     logging · metric cardinality bùng nổ · alarm phải hành-động-được.
```

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.10 Observability** (`tr. 345–371`): CloudWatch "central logging and metrics service, each AWS service logs to CloudWatch", tạo alarm theo ngưỡng, "most underrated... you will need to use CloudWatch", các sản phẩm con Logs/Metrics/Alarms/Synthetics (tr. 347); CloudWatch Logs "centralized logging space, Lambda/API GW/ECS log directly", "logs are text output, console.log → CloudWatch", Powertools JSON logger (tr. 347+); Metrics, custom metrics, dimensions; Alarms & thresholds; X-Ray tracing (tr. 348+). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (Logs/Metrics/Alarms chạy thật).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability ← bạn đang ở đây] · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
