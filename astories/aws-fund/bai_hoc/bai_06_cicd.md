# Bài 6 — CI/CD: CodeBuild & CodePipeline — tự động hoá đường ship

> [!info] Về bài này
> Dựng từ **Chương 9 — Continuous Integration & Continuous Delivery** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 330–344`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
>
> **Lưu ý LocalStack:** **CodeBuild & CodePipeline cần bản Pro** → bài này học bằng **khái niệm + config mẫu (buildspec) + sơ đồ**, *không chạy lab thật*. Việc *thực sự deploy* hạ tầng ta làm ở [Bài 8 — IaC](bai_08_infrastructure-as-code.md) với CloudFormation (chạy được trên LocalStack free).

## Mục lục

1. [Mô hình tư duy: vì sao cần CI/CD](#1-mô-hình-tư-duy-vì-sao-cần-cicd)
2. [Năm yêu cầu một pipeline phải đáp ứng](#2-năm-yêu-cầu-một-pipeline-phải-đáp-ứng)
3. [CodeBuild: môi trường build ổn định](#3-codebuild-môi-trường-build-ổn-định)
4. [CodePipeline: điều phối thành các stage](#4-codepipeline-điều-phối-thành-các-stage)
5. [Config mẫu: buildspec và pipeline](#5-config-mẫu-buildspec-và-pipeline)
6. [Bảng vai trò & so sánh 2026](#6-bảng-vai-trò--so-sánh-2026)
7. [Cạm bẫy CI/CD](#7-cạm-bẫy-cicd)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: vì sao cần CI/CD

Ship thủ công = lập trình viên tự build trên máy mình rồi tự đẩy lên production. Vấn đề: *"chạy ngon trên máy tôi"* (môi trường mỗi người khác nhau), con người bấm nhầm, không ai dám đổi vì sợ hỏng, và khi hỏng thì không rollback được. **CI/CD** tự động hoá đường từ *commit* tới *production*:

> [!quote] Ch. 9 — CodeBuild & CodePipeline (tr. 332)
> "CodeBuild and CodePipeline help you build your deployment package and can also create and manage infrastructure via Infrastructure as Code tools such as Terraform, CloudFormation, Serverless Framework, CDK, and others."
>
> *CodeBuild và CodePipeline giúp bạn **build gói triển khai** và cũng có thể **tạo/quản lý hạ tầng** qua các công cụ IaC như Terraform, CloudFormation, Serverless Framework, CDK…*

- **CI** (Continuous Integration): mỗi commit → tự động build + chạy test trong *môi trường chuẩn*, bắt lỗi sớm.
- **CD** (Continuous Delivery): build xong → tự động đưa tới các môi trường (dev/staging/prod), có kiểm soát.

## 2. Năm yêu cầu một pipeline phải đáp ứng

Sách gói nhu cầu CI/CD thành năm điều — nhớ chúng là nhớ *vì sao* pipeline tồn tại:

| Yêu cầu | Giải thích |
| :--- | :--- |
| **Toolchain ổn định** | môi trường build có sẵn ngôn ngữ/công cụ/framework cần thiết |
| **Rollout đều đặn** | đưa thay đổi ra thường xuyên, bản test không lệch xa bản dev |
| **Không phụ thuộc máy dev** | môi trường mỗi dev khác nhau → build phải *reproducible*, không "chạy trên máy tôi" |
| **Hạn chế tay người chạm prod** | giảm lỗi người + đáp ứng compliance |
| **Rollback được** | có sự cố thì quay về bản lành nhanh chóng |

## 3. CodeBuild: môi trường build ổn định

> [!quote] Ch. 9 — CodeBuild (tr. 333)
> "CodeBuild is the service that actually builds. But don't get too caught up in this phrase, as you can execute anything with CodeBuild."
>
> *CodeBuild là dịch vụ **thực sự build**. Nhưng đừng bám chữ "build" — bạn **chạy được bất cứ gì** với CodeBuild.*

CodeBuild chạy công việc của bạn trong một **container** (image tuỳ chọn) với toolchain định sẵn — nên "build" ở đây có thể là compile, chạy test, lint, đóng gói, hay *bất kỳ script nào*. Cái gì chạy được trong container thì CodeBuild chạy được. Nó đọc file **`buildspec.yml`** để biết các bước.

## 4. CodePipeline: điều phối thành các stage

> [!quote] Ch. 9 — CodePipeline (tr. 334)
> "it is your CodeBuild orchestration tool. With CodePipeline, you can create pipelines that connect jobs into stages to create a multi-step rollout"
>
> *CodePipeline là **công cụ điều phối** CodeBuild. Với nó, bạn tạo pipeline **nối các job thành các stage** để dựng một quy trình rollout nhiều bước.*

Một pipeline điển hình gồm các **stage** nối tiếp, mỗi stage có thể chặn/duyệt trước khi sang stage sau:

```
┌────────────┐  ┌───────────┐  ┌────────┐  ┌─────────────┐  ┌───────────────────┐
│ Source     │─►│ Build     │─►│ Test   │─►│ Approve     │─►│ Deploy            │
│ (git push) │  │ (compile) │  │ (test) │  │ (duyệt tay) │  │ (IaC: CFN/CDK/TF) │
└────────────┘  └───────────┘  └────────┘  └─────────────┘  └───────────────────┘
   trigger          gói           kiểm        cổng người         ra prod
                artifact        tra             (compliance)
```

Nguồn (Source) thường là CodeCommit/GitHub; triển khai (Deploy) thường gọi một **IaC tool** để tạo/cập nhật hạ tầng (nối [Bài 8](bai_08_infrastructure-as-code.md)). CodeBuild *bắt buộc* nếu muốn ở trong AWS; CodePipeline thì tuỳ chọn nhưng "mở rộng hoàn hảo" cho CodeBuild.

## 5. Config mẫu: buildspec và pipeline

Vì không chạy được trên LocalStack free, ta *đọc hiểu* config — thứ bạn sẽ viết thật trên AWS. **`buildspec.yml`** (CodeBuild đọc) cho app Lambda Node:

```yaml
# buildspec.yml — CodeBuild đọc file này
version: 0.2
phases:
  install:
    runtime-versions:
      nodejs: 20
  pre_build:
    commands:
      - npm ci                      # cài dependency (reproducible, từ lockfile)
  build:
    commands:
      - npm test                    # chạy test (CI — bắt lỗi sớm)
      - npm run build               # đóng gói
  post_build:
    commands:
      - zip -r fn.zip dist node_modules   # tạo artifact deploy
artifacts:
  files:
    - fn.zip                        # artifact chuyển sang stage Deploy
```

Mỗi *phase* chạy tuần tự; thất bại ở bất kỳ phase nào → pipeline dừng (fail fast). `artifacts` là thứ được *chuyển tiếp* sang stage sau. Pipeline nối các stage này lại và thêm Source + Deploy.

> [!note] Thay vì CodePipeline, ta sẽ *thực sự deploy* ở Bài 8
> CodeBuild/CodePipeline cần LocalStack Pro. Nhưng *đích* của chúng — **tạo hạ tầng từ code** — thì làm được trên LocalStack free bằng **CloudFormation** ([Bài 8](bai_08_infrastructure-as-code.md)): ta sẽ viết một template và `deploy` thật (tạo Lambda + DynamoDB + API GW bằng một lệnh). Hãy coi Bài 6 là *vì sao/cái gì* của CI/CD, Bài 8 là *làm thật* phần deploy.

## 6. Bảng vai trò & so sánh 2026

| | **CodeBuild** | **CodePipeline** |
| :--- | :--- | :--- |
| Vai trò | *thực thi* các bước (build/test/script) | *điều phối* nhiều bước thành stage |
| Đọc | `buildspec.yml` | định nghĩa pipeline (stage/action) |
| Bắt buộc? | gần như, nếu ở trong AWS | tuỳ chọn (có thể dùng tool khác) |

> [!warning] Thực tế & lựa chọn 2026
> - **CodeBuild/CodePipeline không phải lựa chọn duy nhất, và thường không phải phổ biến nhất.** Năm 2026, rất nhiều đội dùng **GitHub Actions** / **GitLab CI** làm CI/CD rồi deploy lên AWS — quen thuộc, hệ sinh thái lớn, không khoá vào AWS. CodePipeline hợp khi *muốn ở trọn trong AWS* (compliance, IAM tích hợp sâu).
> - **CI/CD cho serverless thường đi qua IaC framework**, không phải CodePipeline trần: **AWS SAM**, **Serverless Framework**, **AWS CDK** sinh sẵn pipeline + deploy. Nối [Bài 8](bai_08_infrastructure-as-code.md).
> - **Build phải reproducible.** Dùng lockfile (`npm ci` chứ không `npm install`), pin version runtime/image — nếu không, "build xanh hôm qua, đỏ hôm nay" mà không đổi code.
> - **Đừng cho pipeline quyền quá rộng.** Role của CodeBuild/pipeline hay bị cấp `AdministratorAccess` cho "tiện" — đó là bề mặt tấn công lớn. Least privilege (Bài 1) áp cả cho CI/CD.

## 7. Cạm bẫy CI/CD

> [!warning] Cạm bẫy thường gặp
> - **"Chạy trên máy tôi".** Chính thứ CI sinh ra để diệt — build trong môi trường chuẩn, không phải laptop ai đó.
> - **Test chậm → bị tắt.** Nếu CI chạy 30 phút, người ta sẽ bỏ qua/tắt test. Giữ pipeline nhanh (song song hoá, cache dependency).
> - **Deploy không rollback được.** Luôn thiết kế để quay về bản trước (giữ artifact cũ, blue/green, hoặc IaC có thể revert).
> - **Secret trong buildspec.** Đừng hardcode credential trong `buildspec.yml`; dùng Secrets Manager / SSM Parameter Store, tiêm lúc chạy.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — CI vs CD là gì?
> **Đáp:** CI = mỗi commit tự build + test trong môi trường chuẩn (bắt lỗi sớm). CD = tự động đưa bản build tới các môi trường (dev/staging/prod), có kiểm soát.

> [!question] Thẻ 6.2 — CodeBuild vs CodePipeline: ai làm gì?
> **Đáp:** CodeBuild *thực thi* bước (build/test/script, đọc `buildspec.yml`); CodePipeline *điều phối* nhiều bước thành **stage** nối tiếp.

> [!question] Thẻ 6.3 — Vì sao build phải "reproducible"?
> **Đáp:** môi trường mỗi dev khác nhau → "chạy trên máy tôi". Build chuẩn hoá (lockfile, pin version) để kết quả nhất quán, không phụ thuộc máy ai.

> [!question] Thẻ 6.4 — Stage điển hình của một pipeline?
> **Đáp:** Source → Build → Test → (Approve) → Deploy. Deploy thường gọi IaC (CloudFormation/CDK/Terraform).

> [!question] Thẻ 6.5 — Năm 2026, lựa chọn CI/CD nào phổ biến ngoài CodePipeline?
> **Đáp:** GitHub Actions / GitLab CI (quen thuộc, không khoá AWS); và IaC framework (SAM/Serverless/CDK) sinh sẵn pipeline cho serverless.

## 9. Câu hỏi tự kiểm tra

1. Kể năm yêu cầu một pipeline phải đáp ứng. *(tr. 332)*
2. "Bạn chạy được bất cứ gì với CodeBuild" nghĩa là gì? *(tr. 333)*
3. Vẽ các stage của một pipeline. Stage Deploy thường gọi gì? *(mục 4)*
4. `buildspec.yml`: `phases` và `artifacts` để làm gì? *(mục 5)*
5. Khi nào chọn CodePipeline thay vì GitHub Actions? *(mục 6)*

## Tóm tắt một trang

```
BÀI 6 — CI/CD: CODEBUILD & CODEPIPELINE
─────────────────────────────────────────────────────────
VẤN ĐỀ  ship tay = "chạy trên máy tôi" + lỗi người + không rollback.
CI  commit → build + test môi trường chuẩn (bắt lỗi sớm).
CD  build xong → tự đưa tới dev/staging/prod có kiểm soát.

5 YÊU CẦU (tr.332): toolchain ổn định · rollout đều · không phụ
   thuộc máy dev (reproducible) · hạn chế tay chạm prod · rollback được.

CODEBUILD  "thực sự build, nhưng CHẠY ĐƯỢC BẤT CỨ GÌ" (tr.333).
   Container + buildspec.yml (phases: install/pre_build/build/post_build).

CODEPIPELINE  "điều phối CodeBuild, nối job thành STAGE" (tr.334).
   Source → Build → Test → Approve → Deploy (gọi IaC).

LOCALSTACK  CodeBuild/CodePipeline cần Pro → học config mẫu. Deploy
   THẬT làm ở Bài 8 với CloudFormation (free).

2026  GitHub Actions/GitLab CI phổ biến (không khoá AWS); serverless
   dùng SAM/Serverless/CDK. Build reproducible (npm ci + pin version).
   Đừng cấp pipeline AdministratorAccess. Đừng hardcode secret.
```

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.9 CI/CD** (`tr. 330–344`): CodeBuild/CodePipeline "fully-managed", build gói + quản hạ tầng qua IaC (Terraform/CloudFormation/CDK…) (tr. 332); năm yêu cầu pipeline (reproducible, decouple dev/release, restrict prod access, rollback) (tr. 332); CodeBuild "actually builds, execute anything", container + buildspec (tr. 333); CodePipeline "orchestration tool, connect jobs into stages, multi-step rollout", CodeBuild bắt buộc/CodePipeline tuỳ chọn (tr. 334). `tai_lieu/AWS+Fundamentals.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: GitHub Actions/GitLab CI; AWS SAM/Serverless Framework/CDK; reproducible builds.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD ← bạn đang ở đây] · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
