# AWS Fundamentals — Khoá tự học AWS để *nhớ lâu*, bằng LocalStack

Khoá tự học thiết kế quanh **khoa học học tập** (nhớ lâu, nắm chắc), dựng từ chính văn bản gốc — không viết theo trí nhớ.

**Sách gốc:** *AWS Fundamentals: AWS For The Real World* — **Tobias Schmidt & Alessandro Volpicella** (2025, 505 trang PDF trong `tai_lieu/`). Sách thực chiến đi theo *từng dịch vụ* (~20 dịch vụ AWS). Khoá này **không tóm tắt sách**, mà biến nó thành một *hệ thống học để nhớ lâu*.

> [!success] Đã hoàn tất **11 bài** (Bài 0 + 1–10) trong `bai_hoc/`.
> Mỗi bài theo vòng lặp: *mô hình tư duy + analogy → cách hoạt động → **bảng quyết định** (chống nhầm dịch vụ na ná) → **lab LocalStack chạy thật** → **thẻ ôn active recall** → nối một mảnh vào capstone*.
> Bảng [Bản đồ khoá học](#bản-đồ-khoá-học--11-bài) bên dưới trỏ tới từng bài.

> [!note] Khoá nền đi kèm — [`cloud-base`](../cloud-base/README.md)
> Khoá này đi **top-down từ dịch vụ**: bạn *dùng được* EC2, DynamoDB, SQS... Nhưng để hiểu *vì sao* chúng hành xử như vậy (cold start? eventually consistent? hot partition? vì sao mỗi GSI tốn tiền ghi?), có khoá nền [`cloud-base`](../cloud-base/README.md) đi **bottom-up từ khoa học máy tính** (OS → Mạng → Distributed → Dữ liệu, curate từ 5 cuốn kinh điển).
> Luận đề nối hai khoá: **mỗi dịch vụ AWS = một khái niệm CS nền tảng được "đóng gói managed"**. Các bài Compute, Database/Storage, Messaging, Networking dưới đây có hộp **"Đào sâu nền tảng"** trỏ thẳng sang bài nền tương ứng. **Cách học hiệu quả nhất: học xen kẽ** — mỗi khi gặp một hành vi AWS khó hiểu, mở bài nền tương ứng; nó sẽ *sáng ra*.

---

## Vì sao khoá này khác — thiết kế để *nhớ lâu*

Kiến thức AWS nổi tiếng khó nhớ: trừu tượng, một núi fact rời rạc, nhiều dịch vụ na ná nhau, và mau cũ. Khoá dùng bốn nguyên lý từ khoa học học tập, mỗi cái khắc chế một điểm yếu:

| Điểm yếu kiến thức AWS | Vũ khí nhớ-lâu | Hiện thực |
| :--- | :--- | :--- |
| Trừu tượng, quên nhanh | **Generation effect** (tự tay tạo) | **lab LocalStack** chạy thật mỗi bài (`awslocal`) |
| Nhầm dịch vụ na ná | **Decision-first + interleaving** | bảng *"khi nào dùng X thay vì Y"* trong mỗi chương |
| Núi fact rời rạc | **Active recall + spaced repetition** | thẻ ôn cuối bài; **master deck Anki (CSV)** ở Bài 9 |
| Học xong rơi rụng | **Cumulative project** | **capstone** ráp dần xuyên khoá |

---

## Vì sao LocalStack

Hands-on là đòn bẩy nhớ-lâu mạnh nhất cho AWS, nhưng AWS thật vướng **tài khoản + chi phí**. [LocalStack](https://localstack.cloud) là bản **giả lập AWS chạy trên máy** (Docker) — miễn phí, reset sạch, và lệnh **giống hệt AWS thật**:

```
awslocal s3 mb s3://my-bucket      # LocalStack
aws      s3 mb s3://my-bucket      # ← AWS THẬT (chỉ bỏ chữ 'local')
```

**Thiết kế lai, trung thực:** dịch vụ LocalStack free chạy tốt thì có **lab chạy thật**; dịch vụ cần Pro thì **lab-giấy + sơ đồ + config mẫu** — không giả vờ chạy được thứ không chạy được.

| Chạy thật trên LocalStack free | Học bằng khái niệm + config (cần Pro) |
| :--- | :--- |
| IAM, **Lambda, DynamoDB, S3, SQS, SNS, EventBridge**, API Gateway (REST), **CloudWatch**, **CloudFormation** | EC2 (mock), ECS/Fargate, RDS, Route 53, VPC, CloudFront, CodeBuild/CodePipeline, HTTP API |

Cài một lần: `brew install localstack/tap/localstack-cli` + `pip install awscli-local`, rồi `localstack start -d`.

---

## Cách đọc & quy ước

| Ký hiệu | Nghĩa |
| :--- | :--- |
| `Ch. 7` | trích theo **chương** của sách |
| `tr. 150` | **số trang in trong sách** (tra tệp PDF thì cộng 4: PDF = `tr. + 4`) |
| `[!quote]` | câu chốt để **nguyên văn tiếng Anh** kèm bản dịch gọn bên dưới |
| ` ```bash ` | **lab chạy thật** với `awslocal`, output thật dán ngay dưới |
| `[!warning]` **Thực tế & cạm bẫy** | chi phí, khác biệt LocalStack-vs-thật, lựa chọn 2026 |
| `[!question]` **Thẻ ôn / Tự thử** | active recall — tự trả lời *trước* khi xem đáp án |

**Chạy lab:** cần **Docker đang chạy** + **LocalStack** (`localstack start -d`) + **awslocal**. Định dạng chuẩn kho: **Obsidian callout**, tiêu đề `##` không kèm emoji.

---

## Bản đồ khoá học — 11 bài

| # | Bài | Chương | Lab chạy thật |
| ---: | :--- | :---: | :--- |
| 0 | [Học AWS nhớ lâu & LocalStack](bai_hoc/bai_00_hoc-aws-nho-lau-va-localstack.md) | 1–3 | S3: `mb`/`cp`/`ls`/`rb` |
| 1 | [Security: IAM](bai_hoc/bai_01_security-iam.md) | 4 | policy + role + trust policy |
| 2 | [Compute: EC2, ECS, Lambda](bai_hoc/bai_02_compute.md) | 5 | deploy & invoke Lambda |
| 3 | [Database & Storage: RDS, DynamoDB, S3](bai_hoc/bai_03_database-storage.md) | 6 | DynamoDB table + query |
| 4 | [Messaging: SQS, SNS, EventBridge](bai_hoc/bai_04_messaging.md) | 7 | SQS + SNS→SQS fan-out |
| 5 | [Networking: API GW, Route53, VPC, CloudFront](bai_hoc/bai_05_networking.md) | 8 | API Gateway → Lambda |
| 6 | [CI/CD: CodeBuild, CodePipeline](bai_hoc/bai_06_cicd.md) | 9 | *(Pro → config mẫu)* |
| 7 | [Observability: CloudWatch](bai_hoc/bai_07_observability-cloudwatch.md) | 10 | logs + metrics + alarm |
| 8 | [Infrastructure as Code](bai_hoc/bai_08_infrastructure-as-code.md) | 11 | CloudFormation deploy stack |
| 9 | [Capstone & tổng ôn](bai_hoc/bai_09_capstone-tong-on.md) | — | **Notes API end-to-end** + master deck Anki |
| 10 | [CloudWatch Logs & Insights](bai_hoc/bai_10_logs-insights.md) | 12 *(bonus)* | structured log + retention + **Logs Insights** query |

**Capstone xuyên khoá:** một **Notes API serverless** — `client → API Gateway → Lambda → DynamoDB + S3`, quan sát bằng CloudWatch, ráp bằng CloudFormation. Mỗi bài thêm một mảnh; Bài 9 chạy end-to-end thật (`POST /notes` → `GET /notes`) trên LocalStack, không một đồng chi phí.

---

## Nguồn

- **Tobias Schmidt & Alessandro Volpicella**, *AWS Fundamentals: AWS For The Real World*, 2025 — `tai_lieu/AWS+Fundamentals.pdf`.
- Phương pháp học dẫn từ ngoài sách: đường cong lãng quên (Ebbinghaus), active recall / testing effect, spaced repetition (SM-2/Anki), generation effect, interleaving, Feynman technique.
- Công cụ: [LocalStack](https://localstack.cloud) (giả lập AWS cục bộ), `awscli-local` (lệnh `awslocal`).
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 4`.
