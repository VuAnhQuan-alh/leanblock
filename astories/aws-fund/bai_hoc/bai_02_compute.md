# Bài 2 — Compute: EC2, ECS/Fargate, Lambda — ba cách chạy code

> [!info] Về bài này
> Dựng từ **Chương 5 — Compute** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 39–116`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vòng lặp nhớ-lâu: *mô hình tư duy → cách hoạt động → **bảng quyết định** → lab LocalStack → thẻ ôn → capstone*.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. LocalStack free chạy **Lambda** rất tốt (lab thật dưới đây). **EC2** chỉ mock cơ bản, **ECS/Fargate** cần Pro → hai cái này ta học bằng *khái niệm + bảng quyết định*, không chạy thật.

## Mục lục

1. [Mô hình tư duy: trục control ↔ abstraction](#1-mô-hình-tư-duy-trục-control--abstraction)
2. [EC2: máy ảo, toàn quyền kiểm soát](#2-ec2-máy-ảo-toàn-quyền-kiểm-soát)
3. [ECS & Fargate: chạy container, Fargate bỏ lo hạ tầng](#3-ecs--fargate-chạy-container-fargate-bỏ-lo-hạ-tầng)
4. [Lambda: chỉ mang code, AWS lo phần còn lại](#4-lambda-chỉ-mang-code-aws-lo-phần-còn-lại)
5. [Bảng quyết định: EC2 vs ECS/Fargate vs Lambda](#5-bảng-quyết-định-ec2-vs-ecsfargate-vs-lambda)
6. [Lab 2: deploy & invoke một Lambda](#6-lab-2-deploy--invoke-một-lambda)
7. [Cold start & GB-giây: hai thứ phản trực giác](#7-cold-start--gb-giây-hai-thứ-phản-trực-giác)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: trục control ↔ abstraction

Ba dịch vụ compute AWS là ba điểm trên **một trục**: càng sang phải, bạn càng *giao* việc quản hạ tầng cho AWS và càng *bớt* quyền kiểm soát.

```
  NHIỀU kiểm soát                                     ÍT kiểm soát
  NHIỀU việc tự quản                                  AWS lo gần hết
        │                                                   │
      EC2  ───────────►  ECS/Fargate  ───────────►  Lambda
   (máy ảo,            (container,                (hàm, chỉ
    tự quản OS)         Fargate = không            mang code)
                        lo máy chủ)
```

Nhớ *trục* này thì nhớ được cả ba dịch vụ cùng lúc — và quan trọng hơn, biết *khi nào chọn cái nào*.

## 2. EC2: máy ảo, toàn quyền kiểm soát

> [!quote] Ch. 5 — EC2 (tr. 41)
> "Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable computing capacity in the cloud."
>
> *Amazon EC2 là dịch vụ cung cấp **năng lực tính toán co giãn được** trên cloud.*

Bạn *thuê máy ảo* (instance) — toàn quyền với OS, thư viện, mọi phần mềm. EC2 có **hơn 500 loại instance** (tối ưu bộ nhớ, CPU, GPU…). Dù tương lai là serverless, sách nêu *lý do chính đáng* vẫn chọn EC2:

| Lý do chọn EC2/container thay vì Lambda | Chi tiết |
| :--- | :--- |
| **Computation** | hiệu năng cao cho tải nặng (ML, tính song song); máy dành riêng, không chia sẻ |
| **Flexibility & Control** | toàn quyền OS/runtime; Lambda giới hạn runtime & giấu hạ tầng |
| **Cost Control** | tải *ổn định, cao* lâu dài thì trả theo instance rẻ hơn trả theo request |

> [!quote] Ch. 5 — EC2 (tr. 41)
> "EC2 is well-suited for steady and high computing demands, while Lambda offers the best approach for small, often event-driven workloads that can benefit from the rapid scaling"
>
> *EC2 hợp với tải **ổn định và cao**, còn Lambda hợp nhất với tải **nhỏ, hướng sự kiện** cần co giãn nhanh.*

Về giá, EC2 có ba kiểu mua: **On-Demand** (trả theo giờ, linh hoạt), **Reserved** (cam kết 1–3 năm, rẻ hơn nhiều), **Spot** (đấu giá công suất dư, rẻ nhất nhưng có thể bị thu hồi).

## 3. ECS & Fargate: chạy container, Fargate bỏ lo hạ tầng

> [!quote] Ch. 5 — ECS & Fargate (tr. 60)
> "Amazon Elastic Container Service (ECS) is a highly scalable and fast container management service. It offers a management plane to orchestrate containers in your cluster."
>
> *Amazon ECS là dịch vụ **quản lý/điều phối container** co giãn nhanh — một *control plane* để run/stop/manage container trong cluster.*

ECS có hai "launch type": **EC2** (bạn tự quản các máy chạy container) và **Fargate** (serverless — không lo máy chủ):

> [!quote] Ch. 5 — ECS & Fargate (tr. 60)
> "Don't worry about the underlying infrastructure with the Fargate launch type. You'll only need to determine which container image you want to run and what workload capabilities you require in terms of memory or virtual CPUs."
>
> *Với launch type **Fargate**, đừng bận tâm hạ tầng bên dưới. Bạn chỉ cần chọn **image container** muốn chạy và **bao nhiêu RAM/vCPU**.*

Từ vựng ECS (treo lên để nhớ): **Container** (app đóng gói) → **Task Definition** (bản thiết kế: image + RAM/CPU + biến môi trường) → **Task** (một lần chạy task definition) → **Service** (giữ N task luôn chạy, tự thay task chết) → **Cluster** (nhóm tài nguyên). Fargate = "ECS nhưng AWS lo máy chủ".

## 4. Lambda: chỉ mang code, AWS lo phần còn lại

> [!quote] Ch. 5 — Lambda (tr. 88)
> "With Lambda, launched in 2014, AWS took this one step further by completely removing customers' liabilities for the underlying infrastructure. The only thing you need to bring is the actual code you want to run."
>
> *Với Lambda (2014), AWS đi thêm một bước: **gỡ bỏ hoàn toàn** trách nhiệm hạ tầng của khách. Thứ duy nhất bạn cần mang là **code**.*

Nhưng đừng hiểu lầm "serverless":

> [!quote] Ch. 5 — Lambda (tr. 88)
> "serverless does not mean that there are no servers. They are simply abstracted away and opaque to the application developer."
>
> *serverless **không** có nghĩa là không có server. Chúng chỉ được **giấu đi** và trở nên vô hình với lập trình viên.*

Khi có request tới, AWS hoặc (1) dựng một *micro-container* mới nạp code của bạn, hoặc (2) tái dùng container cũ còn rảnh. Code chạy theo mô hình **handler**: phần ngoài handler (global) chạy một lần khi khởi tạo container; phần trong handler chạy mỗi request. Lambda **hướng sự kiện** — nó được *trigger* bởi API Gateway, S3, SQS, EventBridge… (các bài sau sẽ nối vào).

## 5. Bảng quyết định: EC2 vs ECS/Fargate vs Lambda

Đây là *vũ khí nhớ-lâu* quan trọng nhất của bài — biết **chọn** mới là hiểu:

| Tiêu chí | **EC2** | **ECS/Fargate** | **Lambda** |
| :--- | :--- | :--- | :--- |
| Đơn vị | máy ảo (OS) | container | hàm |
| Bạn quản | OS + runtime + app | image + RAM/CPU | **chỉ code** |
| Trả tiền | theo giờ instance (on-demand/reserved/spot) | theo task chạy | **theo GB-giây + số request** |
| Co giãn | tự cấu hình (Auto Scaling) | theo task | **tức thì, tới 0** |
| Hợp nhất với | tải **ổn định, nặng**, cần kiểm soát OS (ML, app legacy) | app đóng gói container, chạy lâu/liên tục | tải **nhỏ, hướng sự kiện, bùng nổ** (API, xử lý file, cron) |
| Chạy khi rảnh | vẫn tốn tiền (máy bật) | vẫn tốn tiền (task chạy) | **không request = không tiền** |
| LocalStack free | mock cơ bản | cần Pro | **chạy tốt** |

Quy tắc ngón tay cái: *bắt đầu bằng Lambda* (rẻ, nhanh, không quản gì); *lên ECS/Fargate* khi tải chạy liên tục/đóng gói container; *dùng EC2* khi cần toàn quyền OS hoặc tải tính toán nặng dành riêng.

## 6. Lab 2: deploy & invoke một Lambda

Đây là mảnh *lõi* của capstone — một hàm xử lý. Ta viết handler Node, đóng gói, deploy lên LocalStack, rồi gọi nó:

```bash
mkdir lamb && cd lamb
# 1) handler Node (CommonJS)
cat > index.js <<'JS'
exports.handler = async (event) => {
  const name = event.name || "khách";
  return { statusCode: 200, message: `Xin chào ${name} từ Lambda!` };
};
JS
zip -q fn.zip index.js

# 2) role cho Lambda (trust policy — xem Bài 1)
cat > trust.json <<'JSON'
{ "Version":"2012-10-17","Statement":[{"Effect":"Allow",
  "Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}] }
JSON
awslocal iam create-role --role-name HelloFnRole \
  --assume-role-policy-document file://trust.json --query 'Role.Arn' --output text

# 3) tạo function
awslocal lambda create-function --function-name hello --runtime nodejs20.x \
  --handler index.handler --role arn:aws:iam::000000000000:role/HelloFnRole \
  --zip-file fileb://fn.zip --query '{Name:FunctionName,Runtime:Runtime,State:State}' --output table

# 4) chờ active rồi invoke với payload
awslocal lambda wait function-active-v2 --function-name hello
awslocal lambda invoke --function-name hello --payload '{"name":"An"}' \
  --cli-binary-format raw-in-base64-out out.json
cat out.json

# 5) dọn
awslocal lambda delete-function --function-name hello
awslocal iam delete-role --role-name HelloFnRole
```

Kết quả chạy thật:

```
------------------------------------
|          CreateFunction          |
+-------+--------------+-----------+
| Name  |   Runtime    |   State   |
+-------+--------------+-----------+
|  hello|  nodejs20.x  |  Pending  |
+-------+--------------+-----------+
```
```
{"statusCode":200,"message":"Xin chào An từ Lambda!"}
```

Chú ý `State: Pending` ngay sau khi tạo — Lambda cần chút thời gian "active" (đây là họ hàng của *cold start*). Bạn đưa code vào `event` qua `--payload`, và handler trả JSON. Capstone sau này: API Gateway sẽ *trigger* chính hàm kiểu này, và hàm sẽ ghi DynamoDB.

> [!question] Tự thử
> 1. Invoke không truyền `--payload`. Handler trả gì? (Nhánh `|| "khách"`.)
> 2. Sửa handler cho nó *ném lỗi* (`throw new Error("x")`), update code, invoke lại. `out.json` chứa gì? (Lambda bắt lỗi ra sao.)
> 3. Đổi `--runtime` sang `python3.12` và viết handler Python tương đương. Lệnh tạo/invoke có đổi không? (Chỉ handler + runtime.)

## 7. Cold start & GB-giây: hai thứ phản trực giác

> [!warning] Thực tế & cạm bẫy Compute
> - **Cold start.** Lần gọi đầu (hoặc sau khi container bị thu hồi), Lambda phải tải code + dựng micro-container trước khi chạy → độ trễ thêm. Code *global* (ngoài handler) chạy một lần và được giữ trong container "như một cache rất dễ bay hơi" — đặt khởi tạo tốn kém (kết nối DB, SDK client) ở global để tái dùng.
> - **Giá Lambda = GB-giây, không phải số lần gọi.** Bạn trả theo *bộ nhớ cấp phát × thời gian chạy*. Free Tier 400.000 GB-giây: hàm 1GB chạy được ~111 giờ, nhưng hàm 10GB chỉ ~11 giờ (tr. 10). Phản trực giác: *tăng bộ nhớ không nhất thiết tăng hoá đơn* — vì nhiều RAM thường chạy *nhanh hơn*, bù lại thời gian.
> - **Lambda đệ quy = bom tiền.** Một Lambda tự trigger chính nó (qua S3/SQS) không có điểm dừng là "horror story" tốn tiền kinh điển (tr. 9). Luôn có điều kiện thoát.
> - **EC2/ECS vẫn tính tiền khi rảnh.** Máy bật/task chạy = đồng hồ chạy, dù không ai dùng. Lambda thì về 0. Đây là lý do capstone chọn serverless.
> - **LocalStack:** Lambda chạy thật (cần Docker); EC2 mock không phản ánh hiệu năng/giá thật; ECS/Fargate cần Pro. Đừng đo hiệu năng trên LocalStack.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 2.1 — Trục control↔abstraction: xếp EC2, ECS/Fargate, Lambda.
> **Đáp:** EC2 (nhiều kiểm soát, tự quản OS) → ECS/Fargate (container, Fargate bỏ lo máy chủ) → Lambda (ít kiểm soát, chỉ mang code).

> [!question] Thẻ 2.2 — Ba lý do chính đáng chọn EC2 thay vì Lambda?
> **Đáp:** computation (tải nặng/ML, máy dành riêng) · flexibility & control (toàn quyền OS/runtime) · cost control (tải ổn định cao trả theo instance rẻ hơn).

> [!question] Thẻ 2.3 — "Serverless" có nghĩa là không có server?
> **Đáp:** Không — vẫn có server, chỉ *được giấu đi* khỏi lập trình viên (tr.88). Lambda chạy trong micro-container do AWS dựng/tái dùng.

> [!question] Thẻ 2.4 — Lambda tính tiền theo gì? Vì sao tăng RAM có thể *không* tăng hoá đơn?
> **Đáp:** theo **GB-giây** (RAM × thời gian) + số request. Nhiều RAM thường chạy nhanh hơn → ít giây hơn → bù lại.

> [!question] Thẻ 2.5 — Khi nào chọn Fargate thay vì Lambda, và thay vì EC2?
> **Đáp:** Fargate khi app đã đóng gói **container** chạy lâu/liên tục. Thay EC2 khi *không muốn tự quản máy chủ*. Thay Lambda khi tải không phải "nhỏ/hướng sự kiện" hoặc cần container đầy đủ.

## 9. Câu hỏi tự kiểm tra

1. Vẽ trục control↔abstraction cho ba dịch vụ compute. *(mục 1)*
2. EC2 có ba kiểu mua nào? Mỗi kiểu hợp lúc nào? *(mục 2)*
3. Phân biệt Task Definition, Task, Service trong ECS. Fargate khác launch type EC2 ra sao? *(tr. 60)*
4. Mô hình handler của Lambda: code global vs code trong handler chạy khi nào? *(tr. 88, mục 7)*
5. Điền bảng quyết định: với "xử lý ảnh khi upload lên S3" bạn chọn gì? Với "train model ML"? *(mục 5)*

## Tóm tắt một trang

```
BÀI 2 — COMPUTE: EC2 / ECS-FARGATE / LAMBDA
─────────────────────────────────────────────────────────
TRỤC  control↔abstraction: EC2 (tự quản OS) → ECS/Fargate
      (container, Fargate bỏ lo máy chủ) → LAMBDA (chỉ mang code).

EC2  "resizable computing capacity" (tr.41). 500+ instance type.
     Mua: On-Demand/Reserved/Spot. Chọn EC2: tải nặng/ML, toàn quyền
     OS, tải ổn định cao. Hợp tải "steady & high" (tr.41).

ECS/FARGATE  điều phối container (tr.60). Fargate = "đừng lo hạ tầng,
     chỉ chọn image + RAM/vCPU" (tr.60). Container→TaskDef→Task→
     Service→Cluster.

LAMBDA  "chỉ mang code, AWS lo phần còn lại" (tr.88). "serverless
     KHÔNG phải không có server — chỉ bị giấu đi" (tr.88). Handler:
     global chạy 1 lần, handler chạy mỗi request. Hướng sự kiện.
     LAB: zip handler → create-function → invoke → "Xin chào An".

QUYẾT ĐỊNH  bắt đầu Lambda (rẻ, về 0) → Fargate (container lâu dài)
     → EC2 (toàn quyền OS/tải nặng).

CẠM BẪY  cold start · giá = GB-giây (tăng RAM ≠ tăng tiền) · Lambda
     đệ quy = bom tiền · EC2/ECS tính tiền cả khi rảnh.
```

> [!note] Đào sâu nền tảng
> *Vì sao* Compute hành xử như vậy nằm ở khoá nền [`cloud-base`](../../cloud-base/README.md) (đi bottom-up từ khoa học máy tính, gặp khoá này ở giữa):
> - **EC2 · Lambda · Fargate đều là ảo hoá** đẩy lên các tầng khác nhau → [cloud-base Bài 1 — ảo hoá (process, CPU, bộ nhớ)](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md): "vCPU" chỉ là một *lát time-share*, còn **cold start** là cái giá dựng process + address space mới toanh.
> - **Memory sizing & OOM-kill** → [Bài 12 — bộ nhớ ảo & paging](../../cloud-base/bai_hoc/bai_12_os-bo-nho-ao.md): vì sao vượt RAM là *kill ngay* (không swap), và chọn RAM = hiểu working set.
> - **CPU credit của T-instances · Lambda concurrency** → [Bài 13 — scheduling & locks](../../cloud-base/bai_hoc/bai_13_os-scheduling-locks.md): chia CPU theo chính sách, turnaround vs response.

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.5 Compute** (`tr. 39–116`): EC2 "resizable computing capacity", 500+ instance types, lý do chọn EC2 vs Lambda, "steady & high" vs "event-driven" (tr. 41–42); pricing on-demand/reserved/spot (tr. 42+); ECS "container management service", Fargate "don't worry about infrastructure", container/task/service/cluster (tr. 60–64); Lambda "only thing you need to bring is the code", "serverless does not mean no servers", micro-container, cold start, handler & global code (tr. 88+); GB-giây (tr. 10). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (Lambda chạy thật qua Docker).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute ← bạn đang ở đây] · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
