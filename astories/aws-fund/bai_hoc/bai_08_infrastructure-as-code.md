# Bài 8 — Infrastructure as Code: hạ tầng là source code

> [!info] Về bài này
> Dựng từ **Chương 11 — Infrastructure as Code** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 372–400+`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vòng lặp nhớ-lâu: *mô hình tư duy → tiến hoá → **bảng quyết định** → lab LocalStack → thẻ ôn → capstone*.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **CloudFormation chạy tốt trên LocalStack free** — bài này *deploy thật* một stack, và chính là bước ráp hạ tầng cho capstone.

## Mục lục

1. [Mô hình tư duy: vì sao hạ tầng phải là code](#1-mô-hình-tư-duy-vì-sao-hạ-tầng-phải-là-code)
2. [Tiến hoá: tay → script → declarative → lập trình](#2-tiến-hoá-tay--script--declarative--lập-trình)
3. [Declarative: khai báo *trạng thái cuối*](#3-declarative-khai-báo-trạng-thái-cuối)
4. [CloudFormation: template, stack, rollback](#4-cloudformation-template-stack-rollback)
5. [Bảng quyết định: CloudFormation vs CDK vs Terraform vs SAM](#5-bảng-quyết-định-cloudformation-vs-cdk-vs-terraform-vs-sam)
6. [Lab 8: deploy stack capstone bằng một lệnh](#6-lab-8-deploy-stack-capstone-bằng-một-lệnh)
7. [Cạm bẫy IaC](#7-cạm-bẫy-iac)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: vì sao hạ tầng phải là code

Suốt các bài, ta tạo resource bằng *lệnh `awslocal` gõ tay*. Ổn để học, nhưng để *vận hành thật* thì không: gõ tay thì không ai nhớ đủ bước, không tái tạo được môi trường, không version control, không rollback. **IaC** là: *mô tả toàn bộ hạ tầng bằng source code*, commit vào Git, deploy bằng một lệnh.

> [!quote] Ch. 11 — IaC (tr. 372)
> "There are almost no professional Cloud Developers who don't use IaC tools."
>
> *Gần như **không có** Cloud Developer chuyên nghiệp nào không dùng công cụ IaC.*

> [!quote] Ch. 11 — What is IaC (tr. 373)
> "Infrastructure as Code describes the practice of provisioning your infrastructure with source code."
>
> *Infrastructure as Code là thực hành **tạo hạ tầng bằng source code**.*

Ba lợi ích cốt lõi (sách, tr.373): **nhân bản** môi trường (sang account/region khác), theo **DevOps best practice** (test tự động, review), và **reproducible** — "không còn checklist thủ công hay bước phải nhớ".

## 2. Tiến hoá: tay → script → declarative → lập trình

IaC tiến hoá qua bốn nấc — nhớ "lịch sử" này thì hiểu *vì sao* mỗi công cụ tồn tại:

| Nấc | Cách làm | Vấn đề giải quyết / còn lại |
| :--- | :--- | :--- |
| **Manual** | click trong Console | dễ lúc đầu; *không tái tạo được*, phải chụp màn hình + checklist |
| **Scripted** | script gọi AWS CLI | bán tự động; nhưng **không có state, không rollback** — *cập nhật* hạ tầng rất khó |
| **Declarative** | khai báo *trạng thái cuối* (CloudFormation, Terraform) | tool tự lo tạo/sửa/xoá + rollback |
| **Programmatic** | viết bằng ngôn ngữ lập trình (CDK) | dùng vòng lặp/hàm/type; sinh ra template declarative |

> [!quote] Ch. 11 — Scripted (tr. 374)
> "The issue with the CLI is that there is no rollback logic or any concrete state."
>
> *Vấn đề của CLI: **không có logic rollback hay state cụ thể** nào.* (Nên *cập nhật* hạ tầng đã có rất khó.)

## 3. Declarative: khai báo *trạng thái cuối*

> [!quote] Ch. 11 — Declarative (tr. 375)
> "A declarative approach defines what the final state looks like. We don't care how it will be done; we only define the final state."
>
> *Lối **declarative** định nghĩa **trạng thái cuối** trông như thế nào. Ta **không quan tâm** nó được làm ra sao; chỉ khai báo trạng thái cuối.*

Bạn nói *"tôi cần một bảng DynamoDB `notes` và một bucket S3"* — tool tự tính ra phải gọi API nào, theo thứ tự nào, và nếu một bước hỏng thì *rollback*. Đây là điểm mạnh so với script imperative (bạn phải tự viết "nếu đã tồn tại thì…"). Đây cũng là tư duy của [Clean Architecture Dependency Rule](../../clean-arc/README.md) ở tầng vận hành: *mô tả cái gì, không phải cái như thế nào*.

## 4. CloudFormation: template, stack, rollback

> [!quote] Ch. 11 — Declarative (tr. 375)
> "AWS introduced the service CloudFormation. CloudFormation allows you to provision resources, handle errors, and roll back states. A CloudFormation template is a configuration file in a YAML or JSON format."
>
> *AWS giới thiệu **CloudFormation**. Nó cho phép **tạo resource, xử lý lỗi, và rollback**. Một **template** CloudFormation là file cấu hình định dạng **YAML hoặc JSON**.*

Từ vựng: **Template** (file YAML/JSON mô tả resource) → **Stack** (một lần triển khai template — tập resource được quản *như một khối*). Deploy stack: CloudFormation tạo mọi resource; xoá stack: nó gỡ *tất cả* (đúng thứ tự phụ thuộc). Nếu deploy lỗi giữa chừng, nó *rollback* về trạng thái trước — không để lại mớ hỗn độn nửa vời.

## 5. Bảng quyết định: CloudFormation vs CDK vs Terraform vs SAM

| Công cụ | Kiểu | Khoá vào AWS? | Hợp khi |
| :--- | :--- | :--- | :--- |
| **CloudFormation** | declarative (YAML/JSON) | có (AWS-only) | ở trọn trong AWS, nền tảng cho SAM/CDK |
| **AWS CDK** | programmatic (TS/Python/…) | có (sinh ra CloudFormation) | muốn dùng *ngôn ngữ lập trình* (vòng lặp/type) thay vì YAML |
| **AWS SAM** | declarative, *tối giản cho serverless* | có | app serverless (Lambda/API GW/DynamoDB) — cú pháp gọn hơn CFN |
| **Terraform** | declarative (HCL) | **không** (đa cloud) | đa cloud, hoặc muốn tool độc lập AWS; state riêng |

Quy tắc: *serverless, ở trong AWS* → **SAM** (hoặc CDK nếu thích code). *Đa cloud / không khoá AWS* → **Terraform**. *Nền tảng chung* → **CloudFormation** (SAM/CDK đều biên dịch xuống nó).

### Ba framework khác trong sách (Pulumi, Serverless Framework, SST)

Chương 11 còn giới thiệu ba công cụ nữa — biết để nhận ra khi gặp, không cần thạo hết:

> [!quote] Ch. 11 (tr. 416)
> "Pulumi is a modern Infrastructure as Code platform. Like other tools like Terraform, you can define your whole infrastructure in code. The main difference is that Pulumi is not limited to a specific cloud provider."
>
> ***Pulumi** là một nền tảng IaC hiện đại. Như Terraform, bạn định nghĩa toàn bộ hạ tầng bằng code; **khác biệt chính là Pulumi không giới hạn ở một nhà cung cấp cloud** — và cho dùng ngôn ngữ lập trình quen thuộc (TS/Python/Go...).*

> [!quote] Ch. 11 (tr. 427)
> "And that's what the Serverless Framework does, beautifully. It abstracts away much of the boilerplate configuration needed for Lambda, API Gateway, and other native integrations with AWS services."
>
> ***Serverless Framework** làm đúng điều này một cách đẹp đẽ: **giấu đi phần lớn cấu hình lặp đi lặp lại** cho Lambda, API Gateway và các tích hợp AWS — tập trung hẳn vào app Lambda-centric.*

> [!quote] Ch. 11 (tr. 438)
> "Imagine you could define the entire AWS infrastructure for your application in code and, on top of that, highly abstracted. That is exactly what Serverless Stack (SST) enables you to do."
>
> ***SST (Serverless Stack)** cho định nghĩa toàn bộ hạ tầng AWS bằng code ở mức **trừu tượng rất cao**, kèm trải nghiệm dev tốt như **live debugging Lambda**.*

| Công cụ | Kiểu | Điểm nhấn | Hợp khi |
| :--- | :--- | :--- | :--- |
| **Pulumi** | programmatic (nhiều ngôn ngữ) | **đa cloud** + ngôn ngữ thật | như Terraform nhưng muốn code, và/hoặc đa cloud |
| **Serverless Framework** | khai báo, Lambda-centric | giấu boilerplate Lambda/API GW | app *thuần serverless*, lên nhanh |
| **SST** | programmatic, trừu tượng cao | DX tốt, **live Lambda debugging** | đội serverless muốn vòng lặp dev nhanh |

Gộp lại: **CloudFormation** là nền (SAM/CDK biên dịch xuống nó); **CDK/Pulumi/SST** cho ai thích *code* hơn YAML (Pulumi/SST đa dạng hơn về cloud/DX); **Terraform/Pulumi** cho đa cloud; **Serverless Framework/SST** chuyên serverless. Không có "đúng nhất" — chọn theo *khoá-vào-AWS hay không* và *khai báo hay lập trình*.

## 6. Lab 8: deploy stack capstone bằng một lệnh

Đây là bước *ráp hạ tầng* capstone — thay vì gõ tay từng resource (Bài 3), ta khai báo *cả stack* trong một template rồi deploy một lệnh:

```yaml
# notes-stack.yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: Capstone - bảng notes + bucket đính kèm
Resources:
  NotesTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: notes
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - { AttributeName: userId, AttributeType: S }
        - { AttributeName: noteId, AttributeType: S }
      KeySchema:
        - { AttributeName: userId, KeyType: HASH }
        - { AttributeName: noteId, KeyType: RANGE }
  AttachmentsBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: notes-attachments-lab
Outputs:
  TableName:  { Value: !Ref NotesTable }
  BucketName: { Value: !Ref AttachmentsBucket }
```

```bash
# MỘT lệnh tạo CẢ HAI resource
awslocal cloudformation deploy --template-file notes-stack.yaml --stack-name capstone

# kiểm resource thật đã được tạo
awslocal dynamodb list-tables --query 'TableNames' --output text
awslocal s3 ls | grep notes-attachments
awslocal cloudformation describe-stacks --stack-name capstone \
  --query 'Stacks[0].Outputs[].{Key:OutputKey,Value:OutputValue}' --output table

# MỘT lệnh gỡ CẢ HAI
awslocal cloudformation delete-stack --stack-name capstone
```

Kết quả chạy thật:

```
Successfully created/updated stack - capstone
notes                              # ← DynamoDB table đã tạo
2026-10-07 11:35:12 notes-attachments-lab   # ← S3 bucket đã tạo
-----------------------------------------
|            DescribeStacks             |
+-------------+-------------------------+
|     Key     |          Value          |
+-------------+-------------------------+
|  BucketName |  notes-attachments-lab  |
|  TableName  |  notes                  |
+-------------+-------------------------+
```

Một `deploy` tạo *cả bảng lẫn bucket*; một `delete-stack` gỡ *cả hai*. Đây là toàn bộ sức mạnh IaC: hạ tầng capstone giờ là **một file commit được**, tái tạo ở bất cứ đâu bằng một lệnh, và không để lại rác khi xoá. So với việc gõ tay 6 lệnh `create-table`/`mb`/… ở các bài trước — giờ *reproducible* và *rollback-able*.

> [!question] Tự thử
> 1. Thêm một resource `AWS::SQS::Queue` vào template, `deploy` lại. CloudFormation tạo *thêm* queue mà không đụng hai resource cũ — vì sao? (Gợi ý: nó so *trạng thái cuối*.)
> 2. Đổi `BucketName` thành tên đã tồn tại ở nơi khác rồi deploy — chuyện gì xảy ra? (rollback.)
> 3. Viết lại chính template này bằng **AWS SAM** (`AWS::Serverless::*`) — cú pháp gọn hơn ra sao?

## 7. Cạm bẫy IaC

> [!warning] Thực tế & cạm bẫy IaC
> - **Drift (lệch trạng thái).** Nếu ai đó sửa resource *bằng tay* trong console sau khi deploy, template và thực tế *lệch nhau* → lần deploy sau có thể ghi đè/hỏng. Quy tắc: *đổi hạ tầng CHỈ qua IaC*, không click tay.
> - **State là thiêng liêng (Terraform).** Terraform giữ *state file* riêng; mất/hỏng state = tai hoạ. CloudFormation giữ state *phía AWS* nên đỡ lo hơn.
> - **Xoá stack = xoá *dữ liệu*.** `delete-stack` gỡ cả bảng DynamoDB/bucket S3 *kèm dữ liệu trong đó*. Dùng `DeletionPolicy: Retain` cho resource chứa dữ liệu production, kẻo xoá nhầm.
> - **Idempotent.** Deploy lại cùng template nhiều lần phải ra *cùng kết quả* — đó là bản chất declarative. Đừng viết IaC phụ thuộc "lần chạy thứ mấy".
> - **Secret không nhét vào template.** Template thường commit vào Git → *không* hardcode mật khẩu/key; tham chiếu Secrets Manager/SSM.
> - **CloudFormation chạy trên LocalStack free**, nhưng vài loại resource (ECS/RDS/CloudFront) vẫn cần Pro — template có chúng sẽ lỗi. Capstone chỉ dùng resource free-friendly.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — IaC là gì? Ba lợi ích cốt lõi?
> **Đáp:** tạo hạ tầng bằng **source code**. Lợi ích: nhân bản môi trường · DevOps (test/review) · **reproducible** (không checklist tay).

> [!question] Thẻ 8.2 — Bốn nấc tiến hoá IaC?
> **Đáp:** manual (click) → scripted (CLI, không state/rollback) → declarative (CloudFormation/Terraform) → programmatic (CDK).

> [!question] Thẻ 8.3 — Declarative vs imperative khác gì?
> **Đáp:** declarative khai báo *trạng thái cuối* (tool tự tính cách làm + rollback); imperative (script) bạn phải tự viết *từng bước* và xử lý "đã tồn tại".

> [!question] Thẻ 8.4 — Template vs Stack trong CloudFormation?
> **Đáp:** Template = file YAML/JSON mô tả resource. Stack = một lần triển khai template — tập resource quản *như một khối* (deploy/xoá/rollback cùng nhau).

> [!question] Thẻ 8.5 — "Drift" là gì? Tránh thế nào?
> **Đáp:** thực tế lệch khỏi template vì ai đó sửa tay. Tránh: *chỉ* đổi hạ tầng qua IaC, không click console.

## 9. Câu hỏi tự kiểm tra

1. Vì sao gõ `awslocal` tay không đủ cho vận hành thật? IaC giải quyết gì? *(mục 1)*
2. Kể bốn nấc tiến hoá IaC và vấn đề của "scripted". *(tr. 374, mục 2)*
3. "Khai báo trạng thái cuối, không quan tâm cách làm" nghĩa là gì? *(tr. 375)*
4. Trong lab, một `deploy`/`delete-stack` làm gì với hai resource? *(mục 6)*
5. Khi nào chọn SAM, khi nào Terraform, khi nào CDK? *(mục 5)*

## Tóm tắt một trang

```
BÀI 8 — INFRASTRUCTURE AS CODE
─────────────────────────────────────────────────────────
IaC  "tạo hạ tầng bằng SOURCE CODE" (tr.373). "gần như không
     Cloud Dev chuyên nghiệp nào không dùng IaC" (tr.372).
     Lợi: nhân bản env · DevOps · REPRODUCIBLE (hết checklist tay).

TIẾN HOÁ  manual (click) → scripted (CLI: "không rollback/state", tr.374)
     → DECLARATIVE (CloudFormation/Terraform) → programmatic (CDK).

DECLARATIVE  "khai báo TRẠNG THÁI CUỐI, không quan tâm cách làm" (tr.375).
CLOUDFORMATION  "provision + handle errors + ROLLBACK; template YAML/JSON"
     (tr.375). Template → Stack (quản như một khối).

QUYẾT ĐỊNH  serverless trong AWS → SAM/CDK. Đa cloud → Terraform.
     Nền tảng chung → CloudFormation (SAM/CDK biên dịch xuống nó).

LAB  notes-stack.yaml → deploy (1 lệnh) tạo DynamoDB 'notes' + S3
     'notes-attachments-lab' → describe outputs → delete-stack gỡ cả hai.

CẠM BẪY  DRIFT (sửa tay → lệch) · delete-stack XOÁ DỮ LIỆU (DeletionPolicy
     Retain) · idempotent · không hardcode secret · vài resource cần Pro.
```

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.11 Infrastructure as Code** (`tr. 372–400+`): "almost no professional Cloud Developers who don't use IaC" (tr. 372); "IaC = provisioning infrastructure with source code", lợi ích duplicate/DevOps/reproducible (tr. 373); lịch sử — manual provisioning, scripted CLI "no rollback logic or concrete state" (tr. 373–374); declarative "defines what the final state looks like", CloudFormation "provision, handle errors, roll back, template YAML/JSON" (tr. 375); giới thiệu Terraform, CDK (tr. 372, 375+). `tai_lieu/AWS+Fundamentals.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: AWS SAM, CDK, Terraform; drift detection; `DeletionPolicy`.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code ← bạn đang ở đây] · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
