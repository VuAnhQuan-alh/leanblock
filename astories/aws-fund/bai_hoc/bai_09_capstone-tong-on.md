# Bài 9 — Capstone: Notes API serverless + tổng ôn (master deck)

> [!info] Về bài này
> Bài tổng hợp của khoá *AWS Fundamentals* — ráp mọi mảnh (IAM, Lambda, DynamoDB, S3, API Gateway, CloudFormation, CloudWatch) thành **một app serverless chạy thật end-to-end trên LocalStack**, rồi **tổng ôn** bằng master cheat-sheet + bộ thẻ Anki.
> Đây là lúc *spaced repetition* và *cumulative project* khép lại: bạn gặp lại toàn bộ kiến thức cũ *trong một ngữ cảnh thật*.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. Toàn bộ capstone chạy trên LocalStack free.

## Mục lục

1. [Kiến trúc capstone: Notes API](#1-kiến-trúc-capstone-notes-api)
2. [Code: Lambda handler nói chuyện DynamoDB](#2-code-lambda-handler-nói-chuyện-dynamodb)
3. [Dựng & chạy end-to-end](#3-dựng--chạy-end-to-end)
4. [Master cheat-sheet: chọn dịch vụ nào](#4-master-cheat-sheet-chọn-dịch-vụ-nào)
5. [Master deck: thẻ Anki cho cả khoá](#5-master-deck-thẻ-anki-cho-cả-khoá)
6. [Lịch ôn giãn cách (spaced repetition)](#6-lịch-ôn-giãn-cách-spaced-repetition)
7. [Đi tiếp từ đây](#7-đi-tiếp-từ-đây)
8. [Tự kiểm tra tổng hợp](#8-tự-kiểm-tra-tổng-hợp)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Kiến trúc capstone: Notes API

Một API lưu ghi chú — dùng đúng các dịch vụ free-LocalStack đã học, mỗi mũi tên là một bài:

```
   POST /notes {userId,noteId,text}        GET /notes?userId=an
            │                                      ▲
            ▼                                      │ JSON
   client ─HTTP─► API Gateway ─invoke─► Lambda ─Put/Query─► DynamoDB 'notes'
   (curl)         (Bài 5)              (Bài 2)              (Bài 3)
                                          │
        IAM role cấp quyền (Bài 1) ───────┤
        console.log → CloudWatch (Bài 7) ─┘
        Cả stack dựng bằng CloudFormation (Bài 8)
```

Mỗi dịch vụ đóng đúng vai mô hình tư duy đã học: API Gateway là *cửa trước*, Lambda là *compute chỉ-mang-code*, DynamoDB là *NoSQL theo khoá*, IAM role là *quyền tối thiểu cho Lambda*, CloudFormation *ráp bằng một lệnh*, CloudWatch *mắt và tai*.

## 2. Code: Lambda handler nói chuyện DynamoDB

Đây là "chút TS/JS khi cần" — app code dùng AWS SDK v3 (có sẵn trong runtime `nodejs20.x`). Handler route theo `httpMethod`:

```javascript
// index.js — Lambda handler cho Notes API
const { DynamoDBClient, PutItemCommand, QueryCommand } = require("@aws-sdk/client-dynamodb");
// LocalStack tự set AWS_ENDPOINT_URL cho Lambda → SDK gọi về đúng LocalStack
const client = new DynamoDBClient(
  process.env.AWS_ENDPOINT_URL ? { endpoint: process.env.AWS_ENDPOINT_URL } : {}
);
const TABLE = "notes";

function parseBody(event) {
  let raw = event.body || "{}";
  if (event.isBase64Encoded) raw = Buffer.from(raw, "base64").toString("utf8");
  try { return JSON.parse(raw); }
  catch { return JSON.parse(decodeURIComponent(raw)); } // phòng body bị URL-encode
}

exports.handler = async (event) => {
  const method = event.httpMethod;
  try {
    if (method === "POST") {
      const b = parseBody(event);
      await client.send(new PutItemCommand({ TableName: TABLE,
        Item: { userId:{S:b.userId}, noteId:{S:b.noteId}, text:{S:b.text||""} } }));
      return { statusCode: 201, body: JSON.stringify({ ok:true, noteId:b.noteId }) };
    }
    if (method === "GET") {
      const userId = (event.queryStringParameters||{}).userId || "an";
      const r = await client.send(new QueryCommand({ TableName: TABLE,
        KeyConditionExpression:"userId = :u", ExpressionAttributeValues:{":u":{S:userId}} }));
      return { statusCode:200, body: JSON.stringify({ userId,
        notes:(r.Items||[]).map(i=>({noteId:i.noteId.S,text:i.text.S})) }) };
    }
    return { statusCode:405, body:"method not allowed" };
  } catch (e) { return { statusCode:500, body: JSON.stringify({error:String(e)}) }; }
};
```

## 3. Dựng & chạy end-to-end

Ráp cả stack (bảng + role + Lambda + API Gateway) rồi gọi thật:

```bash
zip -q fn.zip index.js
# bảng DynamoDB (Bài 3)
awslocal dynamodb create-table --table-name notes \
  --attribute-definitions AttributeName=userId,AttributeType=S AttributeName=noteId,AttributeType=S \
  --key-schema AttributeName=userId,KeyType=HASH AttributeName=noteId,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
# role cho Lambda + quyền DynamoDB (Bài 1)
awslocal iam create-role --role-name NotesApiRole --assume-role-policy-document file://trust.json
awslocal iam attach-role-policy --role-name NotesApiRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
# Lambda (Bài 2)
FNARN=$(awslocal lambda create-function --function-name notes-api --runtime nodejs20.x \
  --handler index.handler --role arn:aws:iam::000000000000:role/NotesApiRole \
  --zip-file fileb://fn.zip --timeout 30 --query FunctionArn --output text)
awslocal lambda wait function-active-v2 --function-name notes-api
# API Gateway REST: /notes GET + POST → Lambda (Bài 5)
APIID=$(awslocal apigateway create-rest-api --name notes --query id --output text)
ROOT=$(awslocal apigateway get-resources --rest-api-id "$APIID" --query 'items[0].id' --output text)
RES=$(awslocal apigateway create-resource --rest-api-id "$APIID" --parent-id "$ROOT" --path-part notes --query id --output text)
for M in GET POST; do
  awslocal apigateway put-method --rest-api-id "$APIID" --resource-id "$RES" --http-method $M --authorization-type NONE
  awslocal apigateway put-integration --rest-api-id "$APIID" --resource-id "$RES" --http-method $M \
    --type AWS_PROXY --integration-http-method POST \
    --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/$FNARN/invocations"
done
awslocal apigateway create-deployment --rest-api-id "$APIID" --stage-name dev
BASE="http://localhost:4566/restapis/$APIID/dev/_user_request_/notes"

# GỌI THẬT
curl -s -X POST "$BASE" -H "Content-Type: application/json" --data-raw '{"userId":"an","noteId":"n1","text":"mua sữa"}'
curl -s -X POST "$BASE" -H "Content-Type: application/json" --data-raw '{"userId":"an","noteId":"n2","text":"học AWS"}'
curl -s "$BASE?userId=an"
```

Kết quả chạy thật:

```
{"ok":true,"noteId":"n1"}
{"ok":true,"noteId":"n2"}
{"userId":"an","notes":[{"noteId":"n1","text":"mua sữa"},{"noteId":"n2","text":"học AWS"}]}
```

Bạn vừa deploy **một app serverless hoàn chỉnh** chạy thật: HTTP → API Gateway → Lambda → DynamoDB → JSON về. Không một đồng chi phí, không tài khoản AWS. Mỗi lệnh ở đây bạn đã gặp trong các bài trước — giờ chúng ráp lại thành *một thứ chạy được*.

> [!question] Tự thử (nâng cấp capstone)
> 1. Thêm `DELETE /notes` (xoá note theo `userId`+`noteId`). Cần `DeleteItemCommand` + method mới trên API Gateway.
> 2. Thêm **S3** (Bài 3): `POST /notes` nhận thêm `attachment` (base64) → lưu vào bucket, lưu S3 key vào DynamoDB.
> 3. Thêm **SNS** (Bài 4): mỗi lần tạo note → `publish` sự kiện "note created" để một Lambda khác xử lý nền.
> 4. Chuyển toàn bộ sang **CloudFormation/SAM** (Bài 8): deploy cả stack bằng một `deploy` thay vì chuỗi lệnh.

## 4. Master cheat-sheet: chọn dịch vụ nào

Gom mọi bảng quyết định của khoá — đây là *interleaving tối hậu*, chống nhầm lẫn mọi cặp dịch vụ na ná:

| Nhu cầu | Chọn | Thay vì | Vì |
| :--- | :--- | :--- | :--- |
| Chạy hàm nhỏ, hướng sự kiện, về 0 khi rảnh | **Lambda** | EC2/ECS | không quản hạ tầng, trả theo GB-giây |
| Container chạy liên tục, không lo máy chủ | **Fargate** | EC2 | serverless container |
| Toàn quyền OS, tải nặng/ML | **EC2** | Lambda | kiểm soát + hiệu năng dành riêng |
| Dữ liệu quan hệ, join, ACID | **RDS** | DynamoDB | SQL |
| Tra nhanh theo khoá, quy mô lớn | **DynamoDB** | RDS | NoSQL, serverless |
| File/ảnh/backup | **S3** | DynamoDB | object storage, không phải DB |
| Đệm tải, xử lý nền, 1→1, đảm bảo xử lý | **SQS** | SNS | queue giữ tin, poll |
| Một sự kiện → nhiều nơi phản ứng ngay | **SNS** | SQS | pub/sub, push, 1→N |
| Định tuyến theo nội dung/nhiều nguồn/lịch | **EventBridge** | SNS | event bus + luật |
| Đưa API ra internet, auth/rate-limit | **API Gateway** | — | cửa trước |
| Tên miền → IP, failover | **Route 53** | — | DNS managed |
| Cache nội dung toàn cầu | **CloudFront** | — | CDN |
| Cô lập mạng, giấu DB khỏi internet | **VPC** | — | mạng riêng |
| Log/metric/alarm | **CloudWatch** | — | observability |
| Hạ tầng tái tạo được, rollback | **CloudFormation/SAM/CDK** | gõ tay | IaC declarative |

## 5. Master deck: thẻ Anki cho cả khoá

Copy khối dưới vào một file `aws.csv`, rồi **Anki → Import** (phân tách bằng dấu `;`, 2 cột: Câu hỏi | Đáp án). Ôn mỗi ngày theo lịch ở mục 6.

```csv
Vì sao đọc thụ động không đủ để học AWS?;Đường cong lãng quên — quên ~80%/vài ngày. Cần active recall + hands-on + giãn cách.
awslocal khác aws ở đâu?;awslocal = aws --endpoint-url=http://localhost:4566 (trỏ LocalStack). Lệnh y hệt AWS thật.
Root user vs IAM user dùng cho việc hằng ngày?;IAM user (quyền tối thiểu + MFA). Root chỉ tạo IAM user đầu tiên rồi khoá.
AWS có giới hạn chi tiêu cứng không? Chặn bằng gì?;Không. Chặn bằng Free Tier + AWS Budgets (cảnh báo) + IAM quyền tối thiểu.
Security OF the Cloud vs IN the Cloud?;OF = AWS lo (hạ tầng vật lý). IN = bạn lo (cấu hình đúng/an toàn khi dùng).
IAM đánh giá quyền theo thứ tự nào?;explicit Deny > Allow > implicit deny (mặc định từ chối).
Role khác User ở đâu? Vì sao an toàn hơn?;Role không gắn ai cố định, được assume → credential tạm (STS), hết hạn tự thu. Không key cố định để rò.
Một role cần hai policy nào?;Trust policy (ai được assume) + permission policy (assume rồi làm gì được).
ARN gồm những phần nào?;arn:aws:SVC:REGION:ACCOUNT:resource. (S3 để trống region.)
Trục control↔abstraction của compute?;EC2 (tự quản OS) → ECS/Fargate (container, Fargate bỏ lo máy chủ) → Lambda (chỉ mang code).
Serverless có nghĩa là không có server?;Không — vẫn có server, chỉ bị giấu đi khỏi lập trình viên.
Lambda tính tiền theo gì?;GB-giây (RAM × thời gian) + số request. Tăng RAM có thể KHÔNG tăng tiền (chạy nhanh hơn).
Cold start là gì?;Lần gọi đầu/sau khi container bị thu hồi: tải code + dựng micro-container trước khi chạy → trễ thêm.
Ba hình dạng dữ liệu → ba dịch vụ?;quan hệ(join/ACID)→RDS; key-value/document scale→DynamoDB; file/blob→S3.
Partition key vs sort key?;partition(HASH) phân tán item; sort(RANGE) sắp xếp trong partition. Composite = cả hai định danh duy nhất.
Thuộc tính bắt buộc duy nhất của item DynamoDB?;primary key. Phần còn lại tuỳ ý (không schema).
Vì sao tránh scan trong DynamoDB?;scan đọc cả bảng → tốn capacity + chậm. Thiết kế khoá để dùng query.
SQS vs SNS: kéo/đẩy? một-tới-mấy?;SQS = poll(kéo), 1→1, giữ tin. SNS = push(đẩy), 1→N fan-out, không lưu tin.
Visibility timeout giải quyết gì? Cạm bẫy?;Sau receive tin bị ẩn tạm để không lấy trùng. Quên delete-message → tin hiện lại → xử lý trùng. Viết idempotent.
Khi nào EventBridge thay vì SNS?;Cần định tuyến theo nội dung sự kiện (pattern), nhiều nguồn AWS, hoặc lịch (scheduled).
Hành trình một request qua 4 dịch vụ networking?;Route53(DNS) → CloudFront(CDN) → API Gateway(cửa trước) → backend (có thể trong VPC).
--type AWS_PROXY nghĩa là gì?;API Gateway đẩy nguyên request vào Lambda; Lambda trả {statusCode,headers,body}, API GW tôn trọng statusCode đó.
CI vs CD?;CI = mỗi commit tự build+test môi trường chuẩn. CD = tự đưa bản build tới dev/staging/prod có kiểm soát.
CodeBuild vs CodePipeline?;CodeBuild thực thi bước (buildspec.yml). CodePipeline điều phối nhiều bước thành stage.
Ba trụ observability?;Logs (chuyện gì xảy ra) · Metrics (bao nhiêu/theo thời gian) · Traces (request đi đâu, chậm ở đâu = X-Ray).
console.log trong Lambda đi đâu?;CloudWatch Logs, log group /aws/lambda/<tên-hàm>, tự động.
Cạm bẫy chi phí lớn nhất của CloudWatch?;Log ingest theo GB. Đặt log level + retention; structured logging.
IaC là gì? Lợi ích cốt lõi?;Tạo hạ tầng bằng source code. Nhân bản env · DevOps · reproducible (hết checklist tay).
Declarative vs imperative (IaC)?;declarative khai báo trạng thái cuối (tool tự lo cách làm + rollback); imperative tự viết từng bước.
Template vs Stack (CloudFormation)?;Template = file YAML/JSON mô tả resource. Stack = một lần triển khai, quản resource như một khối.
Drift là gì? Tránh thế nào?;Thực tế lệch khỏi template vì sửa tay. Tránh: chỉ đổi hạ tầng qua IaC, không click console.
```

## 6. Lịch ôn giãn cách (spaced repetition)

Đừng ôn một mạch rồi quên. Theo lịch *giãn dần* (nguyên tắc SM-2 của Anki — nếu dùng Anki thì nó tự lo):

| Thời điểm | Làm gì |
| :--- | :--- |
| Ngay sau mỗi bài | trả lời thẻ ôn của bài đó (không nhìn đáp án trước) |
| +1 ngày | mở lại thẻ của bài hôm qua + master cheat-sheet §4 |
| +3 ngày | ôn thẻ các bài đã học, *xen kẽ* (không theo thứ tự) |
| +1 tuần | tự dựng lại capstone từ đầu *không nhìn bài* (generation effect mạnh nhất) |
| +2 tuần, +1 tháng | lướt master deck; nâng cấp capstone (Tự thử §3) |

Phép thử vàng cho "đã nhớ thật": **dựng lại capstone end-to-end mà không mở bài nào**. Làm được = kiến thức đã thành của bạn.

## 7. Đi tiếp từ đây

- **Lên AWS thật:** mọi lệnh `awslocal` bỏ "local" là chạy trên AWS thật — nhớ Bài 0 (MFA, Budgets, dọn dẹp) để không tốn tiền.
- **Chứng chỉ:** khoá này + *AWS Cloud Practitioner* / *Solutions Architect Associate* là bước tự nhiên (sách cũng nhắm nền tảng đó, không phải luyện-đề).
- **Kiến trúc sâu hơn:** nối sang khoá [`clean-arc`](../../clean-arc/README.md) — Dependency Rule, ranh giới, "database/web là chi tiết" áp thẳng vào thiết kế serverless.

## 8. Tự kiểm tra tổng hợp

1. Vẽ lại kiến trúc capstone và chỉ rõ mỗi dịch vụ học ở bài nào. *(mục 1)*
2. Trong capstone, IAM role của Lambda cần gì để ghi được DynamoDB? *(Bài 1, mục 3)*
3. Vì sao handler phải xử lý `isBase64Encoded`/URL-encode của body? *(mục 2)*
4. Dùng master cheat-sheet: "gửi email + ghi analytics khi có đơn hàng" → dịch vụ nào? "resize 1 triệu ảnh" → ? *(mục 4)*
5. Phép thử vàng để biết "đã nhớ thật" là gì? *(mục 6)*

## Tóm tắt một trang

```
BÀI 9 — CAPSTONE: NOTES API + TỔNG ÔN
─────────────────────────────────────────────────────────
KIẾN TRÚC  client ─HTTP→ API Gateway(B5) → Lambda(B2) → DynamoDB(B3)
   IAM role(B1) cấp quyền · console.log→CloudWatch(B7) · CloudFormation(B8) ráp.

CHẠY THẬT  POST /notes → {"ok":true,"noteId":"n1"} (x2).
   GET /notes?userId=an → {"userId":"an","notes":[{n1,"mua sữa"},{n2,"học AWS"}]}.
   App serverless hoàn chỉnh, 0đ, 0 tài khoản AWS.

MASTER CHEAT-SHEET §4  gom mọi bảng quyết định — chọn dịch vụ nào thay
   vì cái na ná (Lambda/ECS/EC2 · RDS/DynamoDB/S3 · SQS/SNS/EventBridge...).

MASTER DECK §5  ~31 thẻ Anki (CSV import). Ôn giãn cách: +1d/+3d/+1w/+2w/+1m.

PHÉP THỬ VÀNG  dựng lại capstone end-to-end KHÔNG mở bài → đã nhớ thật.

ĐI TIẾP  bỏ "local" → AWS thật (nhớ MFA/Budgets/dọn dẹp) · chứng chỉ
   Cloud Practitioner/SAA · kiến trúc sâu: clean-arc.
```

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals: AWS For The Real World* (2025) — tổng hợp toàn khoá: Compute (Ch.5), Database & Storage (Ch.6), Messaging (Ch.7), Networking (Ch.8), Observability (Ch.10), IaC (Ch.11); định hướng nền tảng cho chứng chỉ Cloud Practitioner/SAA (Ch.1, tr. 4). `tai_lieu/AWS+Fundamentals.pdf`
- Phương pháp học: spaced repetition (SM-2/Anki), active recall, generation effect, interleaving, cumulative project.
- Công cụ: LocalStack + `awslocal` (toàn bộ capstone chạy thật trên free tier).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn ← bạn đang ở đây] · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
