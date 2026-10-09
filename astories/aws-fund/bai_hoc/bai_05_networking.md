# Bài 5 — Networking: API Gateway, Route 53, VPC, CloudFront

> [!info] Về bài này
> Dựng từ **Chương 8 — Networking** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 249–329`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Bốn dịch vụ này không "cạnh tranh" nhau mà là *các lớp khác nhau* trên đường đi của một request — nên bài dùng khung **"hành trình một request"** thay cho bảng "X vs Y".
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **API Gateway (REST API v1)** chạy tốt trên LocalStack free (lab thật). **Route 53, VPC** mock cơ bản; **CloudFront** và **HTTP API (apigatewayv2)** cần Pro → học bằng khái niệm + sơ đồ.

## Mục lục

1. [Mô hình tư duy: hành trình một request](#1-mô-hình-tư-duy-hành-trình-một-request)
2. [API Gateway: cửa trước ra internet](#2-api-gateway-cửa-trước-ra-internet)
3. [Route 53: DNS, tên miền thành địa chỉ](#3-route-53-dns-tên-miền-thành-địa-chỉ)
4. [VPC: mạng riêng, cô lập resource](#4-vpc-mạng-riêng-cô-lập-resource)
5. [CloudFront: CDN, đưa nội dung tới rìa](#5-cloudfront-cdn-đưa-nội-dung-tới-rìa)
6. [Bảng vai trò: dịch vụ nào cho nhu cầu nào](#6-bảng-vai-trò-dịch-vụ-nào-cho-nhu-cầu-nào)
7. [Lab 5: API Gateway → Lambda](#7-lab-5-api-gateway--lambda)
8. [Cạm bẫy networking](#8-cạm-bẫy-networking)
9. [Thẻ ôn (active recall)](#9-thẻ-ôn-active-recall)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: hành trình một request

Bốn dịch vụ networking nằm ở *bốn chặng khác nhau* trên đường một request đi từ người dùng tới code của bạn — nhớ "hành trình" thì nhớ cả bốn cùng lúc:

```
người dùng
   │  gõ api.myapp.com
   ▼
(Route 53)  DNS: tên miền → địa chỉ IP
   │
   ▼
(CloudFront)  CDN: cache ở "rìa" gần người dùng → trả nhanh, giảm tải gốc
   │  (nếu không cache được thì đi tiếp)
   ▼
(API Gateway)  cửa trước: auth, rate-limit, route → gọi backend
   │
   ▼
Lambda / backend  ──► (VPC)  mạng riêng cho DB/cache không lộ ra internet
```

## 2. API Gateway: cửa trước ra internet

> [!quote] Ch. 8 — API Gateway (tr. 251)
> "AWS API Gateway is a crucial component of Serverless applications on AWS. It acts as a fully-managed service that serves as a front door for your application's ecosystem to the internet."
>
> *API Gateway là thành phần **cốt yếu** của ứng dụng serverless. Nó là một dịch vụ managed đóng vai **cửa trước** (front door) đưa hệ sinh thái ứng dụng ra internet.*

Không chỉ *trigger* Lambda, API Gateway còn lo **access control, biến đổi dữ liệu, rate-limiting** và nhiều thứ khác — và nối được với *mọi backend nói HTTP*, không riêng Lambda. Nó "thân thiện người mới" và **không tốn phí lúc rảnh** (chỉ trả theo request). Hai loại chính: **REST API** (đầy đủ tính năng, nhiều nút) và **HTTP API** (gọn, rẻ hơn, nhanh hơn — ra đời sau). Trong capstone, API Gateway là *cửa trước* nhận `POST /notes` rồi gọi Lambda.

## 3. Route 53: DNS, tên miền thành địa chỉ

> [!quote] Ch. 8 — Route 53 (tr. 284)
> "Route 53 is a managed service introduced by Amazon in 2010. It reliably redirects traffic via domain names."
>
> *Route 53 là dịch vụ DNS managed (từ 2010), **điều hướng traffic đáng tin cậy qua tên miền**.*

**DNS** biến tên dễ đọc (`aws.amazon.com`) thành địa chỉ IP mà máy dùng để kết nối — nó là "danh bạ của internet", một hệ **phi tập trung, phân cấp** (root → TLD → authoritative name server). Route 53 không chỉ phân giải tên mà còn có **routing policy** thông minh: theo địa lý (gần người dùng nhất), theo độ trễ, *weighted* (chia tải A/B), và **failover** (chuyển sang bản dự phòng khi *health check* báo gốc hỏng) — chính điều làm ứng dụng **highly available**.

## 4. VPC: mạng riêng, cô lập resource

> [!quote] Ch. 8 — VPC (tr. 300)
> "Amazon Virtual Private Cloud (VPC) allows you to create and deploy AWS resources in a logically isolated virtual network."
>
> *VPC cho phép bạn tạo và triển khai resource AWS trong một **mạng ảo cô lập về mặt logic** — như một datacenter riêng của bạn trên cloud.*

VPC là *hàng rào mạng*: bạn quyết định cái gì lộ ra internet, cái gì **không bao giờ** (database, cache nên nằm trong *private subnet*, không ai từ internet chạm tới). Từ vựng: **Subnet** (chia VPC thành vùng public/private), **Security Group** (tường lửa mức resource — quy định port/IP nào vào/ra), **Route Table**, **NAT Gateway** (cho private subnet ra internet mà không bị truy cập ngược). Với app *thuần serverless* (Lambda + DynamoDB + S3), bạn thường *không cần đụng VPC* — AWS lo; VPC quan trọng khi có EC2/RDS cần cô lập mạng.

## 5. CloudFront: CDN, đưa nội dung tới rìa

> [!quote] Ch. 8 — CloudFront (tr. 312)
> "CloudFront is a Content Delivery Network (CDN) that consists of a set of globally distributed caching..."
>
> *CloudFront là một **mạng phân phối nội dung (CDN)** gồm một tập các **điểm cache phân tán toàn cầu**.*

Thay vì mọi người dùng khắp thế giới phải gọi về *một* server gốc (chậm với người ở xa), CloudFront **cache nội dung ở hàng trăm "edge location"** gần người dùng → trả nhanh hơn, giảm tải gốc, giảm chi phí. Lợi ích: hiệu năng (tối ưu tầng mạng), bảo mật (TLS 1.3, geo-restriction, tích hợp WAF), và *hành vi cache tuỳ biến*. Dùng để phân phối *static asset* (ảnh, JS/CSS, video), *static website* từ S3, hoặc đứng trước API.

## 6. Bảng vai trò: dịch vụ nào cho nhu cầu nào

| Nhu cầu | Dịch vụ | Chặng |
| :--- | :--- | :--- |
| "Tên miền `myapp.com` trỏ về đâu?" | **Route 53** | DNS — đầu tiên |
| "Trả static/content nhanh cho người dùng toàn cầu" | **CloudFront** | CDN — cache ở rìa |
| "Đưa API/Lambda ra internet, có auth + rate-limit" | **API Gateway** | cửa trước API |
| "Giấu database/cache khỏi internet, cô lập mạng" | **VPC** | mạng riêng — sâu bên trong |

Không phải chọn-một: một app production thường dùng *cả bốn* — Route 53 trỏ tên → CloudFront cache → API Gateway nhận request động → backend trong VPC. (Capstone serverless chỉ *bắt buộc* API Gateway; ba cái kia là "khi lên production thật".)

## 7. Lab 5: API Gateway → Lambda

Dựng cửa trước thật của capstone: một **REST API** có route `GET /notes` gọi vào Lambda, rồi gọi qua HTTP:

```bash
# handler Lambda trả JSON theo định dạng proxy integration
cat > index.js <<'JS'
exports.handler = async (event) => ({
  statusCode: 200,
  headers: { "content-type": "application/json" },
  body: JSON.stringify({ message: "Note API đang chạy!", method: event.httpMethod, path: event.path })
});
JS
zip -q fn.zip index.js
# ... tạo role + lambda 'notes-api' (như Bài 2), lấy FNARN ...
FNARN=$(awslocal lambda create-function --function-name notes-api --runtime nodejs20.x \
  --handler index.handler --role arn:aws:iam::000000000000:role/ApiFnRole \
  --zip-file fileb://fn.zip --query 'FunctionArn' --output text)
awslocal lambda wait function-active-v2 --function-name notes-api

# REST API: tạo api → resource /notes → method GET → integration AWS_PROXY → deploy
APIID=$(awslocal apigateway create-rest-api --name notes-rest --query 'id' --output text)
ROOT=$(awslocal apigateway get-resources --rest-api-id "$APIID" --query 'items[0].id' --output text)
RES=$(awslocal apigateway create-resource --rest-api-id "$APIID" --parent-id "$ROOT" \
  --path-part notes --query 'id' --output text)
awslocal apigateway put-method --rest-api-id "$APIID" --resource-id "$RES" \
  --http-method GET --authorization-type NONE
awslocal apigateway put-integration --rest-api-id "$APIID" --resource-id "$RES" --http-method GET \
  --type AWS_PROXY --integration-http-method POST \
  --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/$FNARN/invocations"
awslocal apigateway create-deployment --rest-api-id "$APIID" --stage-name dev

# GỌI endpoint qua HTTP (URL invoke của LocalStack)
curl -s "http://localhost:4566/restapis/$APIID/dev/_user_request_/notes"
```

Kết quả chạy thật:

```
{"message":"Note API đang chạy!","method":"GET","path":"/notes"}
```

*(API id `$APIID` là chuỗi ngẫu nhiên mỗi lần tạo.)* Một request HTTP thật đã đi: **client → API Gateway → Lambda → JSON về**. Đây đúng *cửa trước* capstone; bài sau chỉ cần đổi `GET /notes` thành `POST /notes` và cho Lambda ghi DynamoDB (Bài 3) là có một API thật. Lưu ý `--type AWS_PROXY`: API Gateway đẩy *nguyên request* vào Lambda (event có `httpMethod`, `path`, `body`), và Lambda phải trả đúng `{statusCode, headers, body}`.

> [!question] Tự thử
> 1. Thêm method `POST` cho cùng resource `/notes`. `curl -X POST` trả `method` là gì?
> 2. Bỏ `create-deployment` (không deploy stage). `curl` còn chạy không? Vì sao phải deploy?
> 3. Sửa Lambda trả `statusCode: 404`. API Gateway trả HTTP status nào? (AWS_PROXY *tôn trọng* statusCode của Lambda.)

## 8. Cạm bẫy networking

> [!warning] Thực tế & cạm bẫy Networking
> - **REST API vs HTTP API (cost).** HTTP API rẻ hơn ~70% và nhanh hơn REST API cho đa số ca serverless. Dùng REST API khi cần tính năng nâng cao (API keys, request validation, WAF tích hợp sâu). *(LocalStack free chỉ có REST API — nên lab dùng nó; trên thật, cân nhắc HTTP API.)*
> - **VPC + Lambda = cold start nặng hơn + phức tạp.** Nhét Lambda vào VPC (để chạm RDS private) từng rất chậm; nay đỡ hơn nhưng vẫn thêm phức tạp. App thuần serverless *đừng* đụng VPC nếu không cần.
> - **NAT Gateway đắt âm thầm.** Cho private subnet ra internet qua NAT Gateway tính tiền theo *giờ + GB traffic* — một nguồn "hoá đơn bất ngờ" kinh điển (tr.9 Bài 0).
> - **CloudFront cache invalidation.** Đổi nội dung mà quên *invalidate* cache → người dùng vẫn thấy bản cũ ở edge. Và invalidation nhiều lần cũng tính tiền.
> - **Security Group vs NACL.** Security Group (mức resource, *stateful*) khác Network ACL (mức subnet, *stateless*). Nhầm hai cái là bug mạng kinh điển.
> - **LocalStack:** API Gateway REST chạy tốt; Route53/VPC mock cơ bản (không mô phỏng routing/định tuyến thật); CloudFront cần Pro. Đừng kết luận về hành vi mạng thật từ LocalStack.

## 9. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — Hành trình một request đi qua bốn dịch vụ theo thứ tự nào?
> **Đáp:** Route 53 (DNS: tên→IP) → CloudFront (CDN: cache rìa) → API Gateway (cửa trước API) → backend, và backend có thể nằm trong VPC (mạng riêng).

> [!question] Thẻ 5.2 — API Gateway làm gì ngoài việc trigger Lambda?
> **Đáp:** access control (auth), rate-limiting, biến đổi dữ liệu; nối mọi backend nói HTTP. "front door" ra internet, không tốn phí lúc rảnh.

> [!question] Thẻ 5.3 — Route 53 giúp "high availability" bằng cách nào?
> **Đáp:** routing policy + health check: failover sang bản dự phòng khi gốc hỏng; định tuyến theo địa lý/độ trễ/weighted.

> [!question] Thẻ 5.4 — Khi nào app serverless *cần* VPC?
> **Đáp:** thường *không* cần (Lambda+DynamoDB+S3 do AWS lo mạng). Cần khi có EC2/RDS phải cô lập mạng hoặc tài nguyên private không lộ internet.

> [!question] Thẻ 5.5 — `--type AWS_PROXY` nghĩa là gì?
> **Đáp:** API Gateway đẩy *nguyên request* (method/path/body) vào Lambda làm `event`, và Lambda phải trả `{statusCode, headers, body}` — API Gateway tôn trọng statusCode đó.

## 10. Câu hỏi tự kiểm tra

1. Vẽ hành trình một request từ `myapp.com` tới Lambda, chỉ rõ bốn dịch vụ. *(mục 1)*
2. REST API vs HTTP API: khác nhau gì, khi nào dùng cái nào? *(mục 2, 8)*
3. Vì sao DB nên nằm trong private subnet của VPC? *(tr. 300)*
4. CloudFront giảm độ trễ cho người dùng ở xa bằng cách nào? *(tr. 312)*
5. Trong lab, điều gì xảy ra nếu quên `create-deployment`? *(mục 7)*

## Tóm tắt một trang

```
BÀI 5 — NETWORKING: API GW / ROUTE 53 / VPC / CLOUDFRONT
─────────────────────────────────────────────────────────
HÀNH TRÌNH REQUEST  người dùng → Route53(DNS) → CloudFront(CDN) →
          API Gateway(cửa trước) → backend → VPC(mạng riêng).

API GATEWAY  "front door ra internet" (tr.251). auth + rate-limit +
          transform; nối mọi backend HTTP; không tốn phí lúc rảnh.
          REST API (đầy đủ) vs HTTP API (gọn/rẻ). LAB: GET /notes → Lambda.

ROUTE 53  DNS managed (tr.284): tên → IP. Routing policy (địa lý/latency/
          weighted/failover) + health check → high availability.

VPC  "mạng ảo cô lập về logic" (tr.300). Subnet (public/private), Security
     Group (tường lửa resource), NAT. Serverless thuần thường KHÔNG cần.

CLOUDFRONT  CDN, cache ở edge toàn cầu (tr.312). Nhanh + giảm tải gốc.
          TLS 1.3, geo-restriction. (Cần Pro trên LocalStack.)

LAB  REST API → resource /notes → GET → AWS_PROXY → Lambda → deploy →
     curl → {"message":"Note API đang chạy!","method":"GET"}.

CẠM BẪY  HTTP API rẻ hơn REST · Lambda-trong-VPC phức tạp · NAT Gateway
     đắt âm thầm · quên invalidate CloudFront cache · SG vs NACL.
```

> [!note] Đào sâu nền tảng
> Nền mạng của bài này ở khoá [`cloud-base`](../../cloud-base/README.md) (cả trụ 2 — Mạng):
> - **API Gateway (HTTP) · Route 53 (DNS) · 5 tầng ↔ VPC · stateless = điều kiện auto-scale** → [Bài 4 — phân tầng, HTTP, DNS](../../cloud-base/bai_hoc/bai_04_mang-http-dns.md).
> - **TLS termination · keep-alive/connection pool · vì sao cold start đau khi gọi service khác** → [Bài 5 — TCP & TLS](../../cloud-base/bai_hoc/bai_05_mang-tcp-tls.md).
> - **CloudFront · Global Accelerator · caching (vì sao "mua ống to hơn" không cứu được)** → [Bài 6 — hiệu năng & CDN](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md).

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.8 Networking** (`tr. 249–329`): API Gateway "front door to the internet", access control/transform/rate-limit, không tốn phí lúc rảnh (tr. 251); REST vs HTTP API (tr. 252+); Route 53 managed DNS từ 2010, DNS phi tập trung phân cấp, routing policy & health check (tr. 284–287); VPC "logically isolated virtual network", subnet/security group/NAT (tr. 300–303); CloudFront "CDN globally distributed caching", hiệu năng/TLS/geo-restriction/edge (tr. 312–315). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (API Gateway REST chạy thật).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking ← bạn đang ở đây] · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
