# Bài 1 — Security: IAM, chất keo kiểm soát mọi truy cập

> [!info] Về bài này
> Dựng từ **Chương 4 — Security (IAM)** của *AWS Fundamentals: AWS For The Real World* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 19–38`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vòng lặp nhớ-lâu: *mô hình tư duy → cách hoạt động → bảng quyết định → lab LocalStack → thẻ ôn → capstone*.
>
> **Chạy lab:** cần **Docker + LocalStack** (`localstack start -d`) + **awslocal**. `awslocal <...>` = `aws <...> --endpoint-url=http://localhost:4566`. LocalStack free tạo/sửa IAM (user/role/policy) tốt; *cưỡng chế* quyền thì hạn chế — nhưng ta học ở đây là **cấu trúc policy & role**, cái đó chuẩn.

## Mục lục

1. [Mô hình tư duy: IAM là chất keo](#1-mô-hình-tư-duy-iam-là-chất-keo)
2. [ARN: cách AWS gọi tên mọi resource](#2-arn-cách-aws-gọi-tên-mọi-resource)
3. [Ba danh tính: user, group, role](#3-ba-danh-tính-user-group-role)
4. [Giải phẫu một policy](#4-giải-phẫu-một-policy)
5. [Identity-based vs resource-based; trust policy](#5-identity-based-vs-resource-based-trust-policy)
6. [Lab 1: policy, role, trust policy trên LocalStack](#6-lab-1-policy-role-trust-policy-trên-localstack)
7. [Least privilege và cạm bẫy](#7-least-privilege-và-cạm-bẫy)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: IAM là chất keo

Mọi lời gọi tới AWS — từ console, CLI, SDK, hay một dịch vụ gọi dịch vụ khác — đều đi qua **IAM** (Identity and Access Management) để hỏi: *"danh tính này có được phép làm hành động này lên resource này không?"*. Sách gọi nó là **chất keo**:

> [!quote] Ch. 2 — AWS IAM (tr. 8)
> "AWS Identity and Access Management, or short AWS IAM, is the glue that connects everything in your AWS accounts. It also manages how you can access your account and what permissions are available."
>
> *AWS IAM là **chất keo** nối mọi thứ trong tài khoản AWS. Nó quản lý cách bạn truy cập tài khoản và những quyền nào khả dụng.*

Ví như **người gác cổng toà nhà**: mỗi lần ai đó muốn vào phòng nào, gác cổng tra *thẻ* (danh tính) và *nội quy* (policy) để cho qua hay chặn. Analogy này treo được toàn bộ phần còn lại: *thẻ* = user/role, *nội quy* = policy, *tên phòng* = ARN.

## 2. ARN: cách AWS gọi tên mọi resource

Trước khi cấp quyền "lên resource nào", phải gọi tên được resource đó. AWS dùng **ARN** (Amazon Resource Name):

> [!quote] Ch. 4 — ARNs (tr. 20)
> "Each ARN string consists of several parts, including the resource type, AWS region, and the account ID of the resource."
>
> *Mỗi chuỗi ARN gồm nhiều phần: **loại resource, region, và account ID**.*

```
arn:aws:s3      :              ::my-bucket            ← S3 không gắn region
arn:aws:dynamodb: eu-west-1 : 123456789012 : table/mytable
   │    │  │          │             │            │
 prefix svc        region       account      resource cụ thể
```

ARN xuất hiện *khắp nơi*: trong policy (`Resource`), CloudFormation, API. Nhớ cấu trúc này một lần, dùng cả khoá. (S3 để trống region vì không gắn một region cụ thể.)

## 3. Ba danh tính: user, group, role

| Danh tính | Là gì | Dùng khi nào |
| :--- | :--- | :--- |
| **User** | một người/ứng dụng cụ thể, có credential cố định | người đăng nhập console; (sách lưu ý: user dần là *legacy*, nên ưu tiên role/SSO) |
| **Group** | một *tập user* để quản quyền chung | gán quyền một lần cho nhiều user (vd group "Developers") |
| **Role** | danh tính **không gắn ai cố định**, ai cần thì "assume" | **dịch vụ** (Lambda, ECS) cần quyền; cấp quyền tạm; cross-account |

Điểm phân biệt cốt lõi — role khác user ở chữ "assume":

> [!quote] Ch. 4 — Role (tr. 24)
> "roles are not associated with a single person but can be assumed by anyone or anything that needs it. This includes AWS service principals that are used, for example, for Lambda functions or container agents at ECS."
>
> *role **không gắn với một người cụ thể** mà có thể được **assume (mượn quyền)** bởi bất cứ ai/cái gì cần — kể cả các *service principal* như Lambda hay container agent của ECS.*

Role phát credential **tạm thời** qua **STS** (Security Token Service) — sống vài phút tới vài giờ rồi hết hạn. Đây là *lý do role an toàn hơn user*: không có credential cố định để rò rỉ. Trong capstone, hàm Lambda của ta sẽ *assume một role* để được quyền ghi DynamoDB — không ai nhét access key vào code cả.

## 4. Giải phẫu một policy

Policy là một tài liệu JSON mô tả *được/không được làm gì*. Các phần (sách, tr. 26):

| Phần | Ý nghĩa |
| :--- | :--- |
| `Version` | phiên bản ngôn ngữ policy — luôn dùng `"2012-10-17"` |
| `Statement` | danh sách các mệnh đề quyền |
| `Effect` | `Allow` hoặc `Deny` |
| `Principal` | *ai* (dùng trong resource-based & trust policy) |
| `Action` | danh sách API được/bị cấm (vd `s3:GetObject`) |
| `Resource` | ARN resource áp dụng |
| `Condition` | điều kiện (tuỳ chọn): theo IP, tag, thời gian… |

Và luật đánh giá quan trọng nhất phải khắc vào đầu:

> [!quote] Ch. 4 — Policy Elements (tr. 26)
> "A deny statement always overwrites allow statements."
>
> *Một mệnh đề **deny luôn luôn ghi đè** mọi mệnh đề allow.*

Nghĩa là: mặc định mọi thứ *bị từ chối ngầm*; `Allow` mở quyền; nhưng một `Deny` tường minh ở *bất kỳ đâu* sẽ thắng tất cả. (Explicit deny > allow > implicit deny.)

## 5. Identity-based vs resource-based; trust policy

Hai loại policy bạn gặp hằng ngày — khác nhau ở chỗ *gắn vào đâu*:

| | **Identity-based** | **Resource-based** |
| :--- | :--- | :--- |
| Gắn vào | identity (user/group/role) | resource (vd bucket S3) |
| Trả lời | "*danh tính này* làm được gì?" | "*ai* được đụng vào resource này?" |
| `Principal` | không cần (đã là chủ identity) | **bắt buộc** (chỉ rõ ai) |
| Dạng con | Managed (AWS-managed / customer-managed), Inline | luôn là inline của resource |

**Trust policy** là một loại đặc biệt — nó *không* cấp quyền làm gì, mà quy định **ai được assume một role**:

> [!quote] Ch. 4 — Trust Policies (tr. 27)
> "Trust policies define which principal is allowed to use a role."
>
> *Trust policy quy định **principal nào được phép dùng (assume) một role**.*

Trust policy cho Lambda (bạn sẽ chạy ở lab) nói: "cho phép `lambda.amazonaws.com` thực hiện `sts:AssumeRole`" — tức *dịch vụ Lambda* được mượn role này. Đây là cặp đôi quyết định của mọi role: **trust policy** (ai mượn được) + **permission policy** (mượn rồi làm được gì).

## 6. Lab 1: policy, role, trust policy trên LocalStack

Tạo một policy đọc S3 (least privilege — chỉ `GetObject` trên đúng một bucket), một role với trust policy cho Lambda, rồi gắn policy vào role:

```bash
# policy: CHỈ cho đọc object trong bucket hoc-aws-lab (least privilege)
cat > /tmp/s3-read.json <<'JSON'
{ "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::hoc-aws-lab/*" }
  ] }
JSON

# trust policy: cho DỊCH VỤ Lambda được assume role này
cat > /tmp/trust-lambda.json <<'JSON'
{ "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" }
  ] }
JSON

# 1) tạo customer-managed policy
awslocal iam create-policy --policy-name DocsS3Read --policy-document file:///tmp/s3-read.json \
  --query 'Policy.{Name:PolicyName,Arn:Arn}' --output table

# 2) tạo role + trust policy
awslocal iam create-role --role-name NoteFnRole --assume-role-policy-document file:///tmp/trust-lambda.json \
  --query 'Role.{Name:RoleName,Arn:Arn}' --output table

# 3) gắn policy vào role, rồi liệt kê
awslocal iam attach-role-policy --role-name NoteFnRole \
  --policy-arn arn:aws:iam::000000000000:policy/DocsS3Read
awslocal iam list-attached-role-policies --role-name NoteFnRole \
  --query 'AttachedPolicies[].PolicyName' --output text

# 4) dọn dẹp
awslocal iam detach-role-policy --role-name NoteFnRole --policy-arn arn:aws:iam::000000000000:policy/DocsS3Read
awslocal iam delete-role --role-name NoteFnRole
awslocal iam delete-policy --policy-arn arn:aws:iam::000000000000:policy/DocsS3Read
```

Kết quả chạy thật:

```
---------------------------------------------------------------
|                        CreatePolicy                         |
+-----------------------------------------------+-------------+
|                      Arn                      |    Name     |
+-----------------------------------------------+-------------+
|  arn:aws:iam::000000000000:policy/DocsS3Read  |  DocsS3Read |
+-----------------------------------------------+-------------+
-------------------------------------------------------------
|                        CreateRole                         |
+---------------------------------------------+-------------+
|                     Arn                     |    Name     |
+---------------------------------------------+-------------+
|  arn:aws:iam::000000000000:role/NoteFnRole  |  NoteFnRole |
+---------------------------------------------+-------------+
DocsS3Read
```

*(Account ID `000000000000` là account cố định của LocalStack. Trên AWS thật, nó là 12 số của bạn.)* Bạn vừa dựng xong *bộ đồ nghề quyền* cho một hàm Lambda: role `NoteFnRole` mà *chỉ Lambda* assume được (trust policy), và khi assume thì *chỉ đọc được* bucket `hoc-aws-lab` (permission policy). Đây đúng mảnh IAM cho capstone.

> [!question] Tự thử
> 1. Thêm action `s3:PutObject` vào `s3-read.json`, tạo lại policy. Role giờ ghi được bucket chưa?
> 2. Đổi `Effect` của trust policy thành `Deny` rồi tạo role — chuyện gì xảy ra? (Lambda còn assume được không?)
> 3. Đổi `Resource` thành `"*"` (mọi bucket). Vì sao đó là *vi phạm least privilege*?

## 7. Least privilege và cạm bẫy

Nguyên tắc vàng của IAM:

> [!quote] Ch. 4 — Custom Policies (tr. 27)
> "Roles help us adhere to sound security protocols by assigning only the necessary permissions to users or services to carry out their functions. This is commonly known as the principle of least privilege."
>
> *Role giúp ta tuân thủ an ninh bằng cách chỉ cấp **đúng những quyền cần thiết** để hoàn thành nhiệm vụ — gọi là **nguyên tắc đặc quyền tối thiểu** (least privilege).*

> [!warning] Thực tế & cạm bẫy IAM
> - **AWS-managed policy tiện nhưng rủi ro thừa quyền.** Chúng do AWS cập nhật — có thể âm thầm *nới rộng* quyền. Với production, ưu tiên **customer-managed, đo ni** (tr. 28).
> - **`"Resource": "*"` và `"Action": "*"` là mùi nguy hiểm.** Cấp "mọi quyền trên mọi thứ" (như `AdministratorAccess`) cho một hàm nhỏ là vé mời thảm hoạ nếu hàm bị chiếm.
> - **Explicit deny thắng tất cả** — dùng `Deny` + `Condition` (vd chặn theo IP) làm rào chắn cứng, nhưng cẩn thận deny quá tay khoá luôn chính mình.
> - **LocalStack free không *cưỡng chế* IAM chặt** như AWS thật (thường cho qua) — nên lab ở đây dạy *viết đúng cấu trúc*, còn kiểm "bị chặn thật" thì phải trên AWS thật. Đừng nhầm "chạy được trên LocalStack" = "an toàn trên thật".
> - **Credential tạm (STS/role) > access key cố định.** Nhét access key vào code/CI là cách rò rỉ phổ biến nhất; dùng role để máy tự lấy credential ngắn hạn.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — IAM trả lời câu hỏi gì cho mỗi request?
> **Đáp:** "*danh tính này* có được làm *action này* lên *resource này* không?" (identity + action + resource).

> [!question] Thẻ 1.2 — Role khác User ở điểm cốt lõi nào? Vì sao an toàn hơn?
> **Đáp:** role **không gắn ai cố định**, được *assume* → phát credential **tạm thời** (STS), hết hạn tự thu hồi. Không có key cố định để rò rỉ.

> [!question] Thẻ 1.3 — Thứ tự đánh giá quyền trong IAM?
> **Đáp:** **explicit Deny > Allow > implicit deny** (mặc định từ chối). Một Deny ở bất kỳ đâu ghi đè mọi Allow.

> [!question] Thẻ 1.4 — Một role cần hai policy nào để hoạt động?
> **Đáp:** **trust policy** (ai được assume) + **permission policy** (assume rồi làm được gì).

> [!question] Thẻ 1.5 — Identity-based vs resource-based policy khác nhau ra sao?
> **Đáp:** identity-based gắn vào user/role ("identity này làm gì được"); resource-based gắn vào resource + **bắt buộc `Principal`** ("ai đụng được resource này").

## 9. Câu hỏi tự kiểm tra

1. Giải thích analogy "IAM là người gác cổng". Thẻ, nội quy, tên phòng tương ứng gì? *(mục 1)*
2. Đọc ARN `arn:aws:dynamodb:eu-west-1:123456789012:table/mytable` — chỉ ra svc/region/account/resource. *(tr. 20)*
3. Khi nào dùng role thay vì user? Cho một ví dụ trong capstone. *(tr. 24)*
4. Liệt kê 7 phần của một policy. "Deny ghi đè allow" nghĩa là gì? *(tr. 26)*
5. Vì sao `"Action":"*", "Resource":"*"` vi phạm least privilege? *(tr. 27, mục 7)*

## Tóm tắt một trang

```
BÀI 1 — SECURITY: IAM, CHẤT KEO KIỂM SOÁT TRUY CẬP
─────────────────────────────────────────────────────────
MÔ HÌNH  IAM = "chất keo" / người gác cổng (tr.22): mỗi request
         hỏi "identity + action + resource -> cho qua?".

ARN  arn:aws:SVC:REGION:ACCOUNT:resource (tr.20). Xuất hiện khắp
     policy/CFN/API. S3 để trống region.

3 DANH TÍNH  user (người, có key cố định, dần legacy) · group (tập
     user) · ROLE (không gắn ai, được ASSUME, phát credential tạm
     qua STS) — role cho Lambda/ECS (tr.24).

POLICY  Version/Statement/Effect/Principal/Action/Resource/Condition.
     "DENY luôn ghi đè ALLOW" (tr.26). explicit deny > allow > implicit.

LOẠI  identity-based (gắn identity) vs resource-based (gắn resource,
     cần Principal). TRUST POLICY = ai được assume role (tr.27).

LAB  create-policy (s3:GetObject least-privilege) + create-role
     (trust Lambda) + attach-role-policy. = bộ quyền cho Lambda capstone.

LEAST PRIVILEGE (tr.27): chỉ cấp đúng quyền cần. Tránh "*".
     AWS-managed tiện nhưng dễ thừa quyền. Credential tạm > key cố định.
```

> [!note] Đào sâu nền tảng
> IAM đứng trên nền **mật mã** — xem khoá [`cloud-base`](../../cloud-base/README.md):
> - **SigV4 ký mọi request · chữ ký số · chứng chỉ & PKI** → [cloud-base Bài 14 — bảo mật & mật mã](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md): vì sao access key *không* bay qua mạng (ký thay vì gửi), **presigned URL** là một chữ ký có hạn, và chuỗi tin cậy **CA** đằng sau TLS/ACM. Phân biệt bí mật / toàn vẹn / xác thực để thiết kế quyền đúng.

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.4 Security (IAM)** (`tr. 19–38`): IAM là chất keo (tr. 22); ARN cấu trúc & ví dụ (tr. 20–21); ba danh tính user/group/role, STS credential tạm (tr. 22–25); kiểm soát qua policy, các phần tử policy, "deny overwrites allow" (tr. 26); identity vs resource-based, managed/inline, AWS-managed vs custom, least privilege, trust policy cho Lambda (tr. 27–28); permission boundary, tag-based access (tr. 29+). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (IAM CRUD).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM ← bạn đang ở đây] · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
