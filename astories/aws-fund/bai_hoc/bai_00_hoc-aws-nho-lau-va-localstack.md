# Bài 0 — Học AWS sao cho nhớ lâu, và khởi động với LocalStack

> [!info] Về bài này
> Dựng từ **Chương 1 (Introduction)** và **Chương 2 (Getting Started)** của *AWS Fundamentals: AWS For The Real World* — **Tobias Schmidt & Alessandro Volpicella** (2025 — `tai_lieu/`, `tr. 1–14`).
> Trích nguồn theo `Ch. N` + `tr. X` (số trang **in trong sách**; muốn tra tệp PDF thì cộng 4 → PDF = `tr. + 4`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn — vì nguồn là tiếng Anh.
> Đây là khoá **học-để-nhớ-lâu**: mỗi bài đi theo vòng lặp *mô hình tư duy → cách hoạt động → bảng quyết định → **lab LocalStack chạy thật** → thẻ ôn (active recall) → nối vào capstone*. Bài 0 vừa dạy **chính phương pháp học này**, vừa là **Getting Started** (an toàn, chi phí, trách nhiệm chia sẻ) + **cài & chạy LocalStack lần đầu**.
>
> **Chạy lab:** cần **Docker** đang chạy + **LocalStack** (`localstack start -d`) + **awslocal** (`pip install awscli-local`). Lệnh `awslocal <...>` chính là `aws <...> --endpoint-url=http://localhost:4566` — **giống hệt AWS thật, chỉ bỏ chữ "local" là chạy trên AWS thật**.

> [!note] Muốn hiểu *vì sao*, không chỉ *cách dùng*?
> Khoá này đi **top-down từ dịch vụ**. Khoá nền đi kèm [`cloud-base`](../../cloud-base/README.md) đi **bottom-up từ khoa học máy tính** (OS → Mạng → Distributed → Dữ liệu) để trả lời những câu *vì sao* bên dưới AWS: cold start, eventually consistent, hot partition, round-trip của TLS... Các bài **Compute, Database/Storage, Messaging, Networking** có hộp **"Đào sâu nền tảng"** trỏ sang bài nền tương ứng. Học **xen kẽ** hai khoá cho hiệu quả nhất.

## Mục lục

1. [Mở đầu: vì sao kiến thức AWS hay rơi rụng](#1-mở-đầu-vì-sao-kiến-thức-aws-hay-rơi-rụng)
2. [Bốn vũ khí nhớ lâu](#2-bốn-vũ-khí-nhớ-lâu)
3. [Vì sao LocalStack, và cài đặt](#3-vì-sao-localstack-và-cài-đặt)
4. [Lab 0: chạm tay AWS lần đầu với S3](#4-lab-0-chạm-tay-aws-lần-đầu-với-s3)
5. [An toàn tài khoản: root, IAM user, MFA](#5-an-toàn-tài-khoản-root-iam-user-mfa)
6. [Tránh tốn tiền bất ngờ](#6-tránh-tốn-tiền-bất-ngờ)
7. [Shared Responsibility Model & Serverless](#7-shared-responsibility-model--serverless)
8. [Capstone: dự án xuyên khoá](#8-capstone-dự-án-xuyên-khoá)
9. [Thẻ ôn (active recall)](#9-thẻ-ôn-active-recall)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: vì sao kiến thức AWS hay rơi rụng

Bạn đọc một chương về S3, gật gù "hiểu rồi". Một tuần sau, có người hỏi *"S3 khác EBS chỗ nào, khi nào dùng cái nào?"* — và bạn ú ớ. Đó không phải lỗi của bạn; đó là **đường cong lãng quên** (Ebbinghaus): kiến thức học *thụ động* rơi rụng ~80% trong vài ngày nếu không được *chủ động lôi ra lại*.

Kiến thức AWS đặc biệt khó nhớ vì ba lý do:

| Điểm yếu của kiến thức AWS | Hệ quả |
| :--- | :--- |
| **Trừu tượng** cho tới khi chạm tay | đọc "object storage" mãi vẫn mơ hồ; chỉ `put`/`get` thật mới thấm |
| **Một núi fact rời rạc** (~20 dịch vụ, giới hạn, giá) | không có khung để treo → trôi tuột |
| **Nhiều dịch vụ na ná nhau** (SQS/SNS/EventBridge, EC2/ECS/Lambda) | nhớ mang máng, lẫn lộn khi cần *chọn* |

Chính tác giả sách đặt câu này ngay đầu chương Getting Started:

> [!quote] Ch. 2 — Creating Your Own AWS Account (tr. 5)
> "It's important to read about the fundamentals of AWS, but practical hands-on experience is essential to truly learn anything in the field of engineering."
>
> *Đọc về nền tảng AWS là quan trọng, nhưng **kinh nghiệm thực hành** mới là thứ thiết yếu để thực sự học được bất cứ gì trong kỹ thuật.*

Khoá này được thiết kế quanh đúng câu đó: **học bằng cách làm, rồi chủ động ôn lại.**

## 2. Bốn vũ khí nhớ lâu

Khoá dùng bốn nguyên lý từ khoa học học tập, mỗi cái khắc chế một điểm yếu ở trên, và được lồng vào *mọi bài*:

| Vũ khí | Khắc chế | Hiện thực trong khoá |
| :--- | :--- | :--- |
| **Generation effect** (tự tay tạo) | trừu tượng, quên nhanh | **lab LocalStack** chạy thật mỗi bài (`awslocal`) |
| **Decision-first + interleaving** | nhầm dịch vụ na ná | bảng **"khi nào dùng X thay vì Y"** trong mỗi chương |
| **Active recall + spaced repetition** | núi fact rời rạc | **thẻ ôn** cuối bài, tự trả lời trước khi xem; xuất Anki (master deck ở Bài 9) |
| **Cumulative project** | học xong là rơi rụng | **capstone** ráp dần xuyên 10 bài → ôn cái cũ trong ngữ cảnh mới |

> [!note] Cách dùng khoá cho hiệu quả
> - **Đừng chỉ đọc.** Với mỗi lab, *gõ lại lệnh* và quan sát output — đừng copy-paste cả khối. Việc gõ là "generation".
> - **Trả lời thẻ ôn *trước* khi xem đáp án.** Vật lộn nhớ ra (dù sai) khắc kiến thức sâu hơn đọc lại 10 lần.
> - **Giãn cách:** làm 1–2 bài rồi *nghỉ*, hôm sau mở thẻ ôn của bài cũ ra tự hỏi lại. Đừng cày một mạch.
> - **Dạy lại (Feynman):** sau mỗi dịch vụ, thử giải thích nó cho một người không biết gì trong 3 câu. Nói không trôi = chưa thật hiểu.

## 3. Vì sao LocalStack, và cài đặt

"Hands-on" trên AWS thật vướng hai thứ: phải có **tài khoản + thẻ tín dụng**, và rủi ro **tốn tiền thật** nếu quên tắt resource. **LocalStack** gỡ cả hai: nó là một **bản giả lập AWS chạy trên máy bạn** (trong Docker), miễn phí, reset sạch tuỳ thích — bạn tạo/xoá bucket, hàng đợi, Lambda… thoải mái mà không tốn một xu.

Điều hay nhất cho việc *học*: lệnh **giống hệt AWS thật**. `awslocal` chỉ là `aws` trỏ vào LocalStack:

```
awslocal s3 mb s3://my-bucket
   ⇅  (giống hệt, chỉ khác endpoint)
aws      s3 mb s3://my-bucket        # ← chạy trên AWS THẬT
```

Nên kỹ năng bạn luyện ở đây **chuyển thẳng** sang AWS thật — chỉ bỏ chữ "local".

> [!note] Cài đặt một lần
> ```
> # 1) Docker phải đang chạy (Docker Desktop / colima)
> # 2) cài LocalStack CLI + awslocal
> brew install localstack/tap/localstack-cli    # hoặc: pip install localstack
> pip install awscli-local                       # cung cấp lệnh 'awslocal'
> # 3) khởi động LocalStack (chạy nền)
> localstack start -d
> # 4) kiểm tra sức khoẻ
> curl -s http://localhost:4566/_localstack/health
> ```
> Những dịch vụ bản miễn phí chạy **tốt** (và là xương sống khoá này): **Lambda, DynamoDB, S3, SQS, SNS, EventBridge, API Gateway, IAM, CloudFormation**. Vài dịch vụ cần bản Pro (ECS/Fargate, RDS, CloudFront, CodePipeline) — ở những bài đó ta học bằng **sơ đồ + IaC mẫu** thay vì chạy thật, và bài sẽ nói rõ.

## 4. Lab 0: chạm tay AWS lần đầu với S3

Chiến thắng đầu tiên: tạo một **bucket S3** (kho lưu file), bỏ một file vào, đọc lại, rồi dọn. S3 là dịch vụ xuất hiện trong gần như mọi ứng dụng AWS — khởi đầu hoàn hảo.

```bash
# 1) tạo bucket (mb = make bucket)
awslocal s3 mb s3://hoc-aws-lab

# 2) tạo một file rồi upload lên bucket
echo "xin chào AWS từ LocalStack" > /tmp/ghi-chu.txt
awslocal s3 cp /tmp/ghi-chu.txt s3://hoc-aws-lab/ghi-chu.txt --only-show-errors

# 3) liệt kê object trong bucket
awslocal s3 ls s3://hoc-aws-lab/

# 4) đọc lại nội dung (tải object ra stdout bằng dấu '-')
awslocal s3 cp s3://hoc-aws-lab/ghi-chu.txt -

# 5) DỌN DẸP (thói quen sống còn trên AWS thật!)
awslocal s3 rb s3://hoc-aws-lab --force
```

Kết quả chạy thật:

```
make_bucket: hoc-aws-lab
2026-10-07 11:06:44         30 ghi-chu.txt
xin chào AWS từ LocalStack
delete: s3://hoc-aws-lab/ghi-chu.txt
remove_bucket: hoc-aws-lab
```

*(Ngày giờ ở dòng `ls` tùy lúc bạn chạy. `30` là số byte của file — tất định.)*

Bạn vừa làm đúng bốn thao tác cốt lõi với *mọi* kho lưu trữ: **tạo, ghi, đọc, xoá** (create/put/get/delete). Và bước 5 — **dọn dẹp** — là thói quen phải khắc vào xương: trên AWS thật, resource quên xoá = hoá đơn cuối tháng.

> [!question] Tự thử (làm trước khi đọc tiếp)
> 1. Tạo bucket tên khác, upload **hai** file, rồi `awslocal s3 ls` — bạn thấy gì?
> 2. Thử `awslocal s3 cp` một object đã xoá — thông báo lỗi nói gì?
> 3. Chạy lại toàn bộ lab lần hai. Lệnh `mb` cùng tên bucket báo gì? (Gợi ý: tên bucket phải *duy nhất*.)

## 5. An toàn tài khoản: root, IAM user, MFA

Phần này là *kiến thức* cho khi bạn dùng **AWS thật** (LocalStack không tính tiền, nhưng tư duy an toàn phải có sẵn). Tác giả mở đầu bằng một cảnh báo:

> [!quote] Ch. 2 — Account Security (tr. 6)
> "With great power, there comes great responsibility. […] As you are solely responsible for your account, you should make protecting it properly your first major task in your cloud journey."
>
> *Quyền lực lớn đi kèm trách nhiệm lớn. […] Vì bạn **một mình chịu trách nhiệm** cho tài khoản của mình, hãy coi việc bảo vệ nó cho đúng là nhiệm vụ lớn **đầu tiên** trong hành trình cloud.*

Hai khái niệm danh tính phải phân biệt rõ (một **bảng quyết định** mini — khi nào dùng cái nào):

| | **Root user** | **IAM user** |
| :--- | :--- | :--- |
| Là gì | **chủ sở hữu** tài khoản, toàn quyền tuyệt đối | danh tính tạo thêm, cho người/ứng dụng |
| Quyền ban đầu | tất cả (kể cả xoá tài khoản, đổi thanh toán) | **không có gì** — phải cấp tường minh |
| Dùng khi nào | **gần như không bao giờ** — chỉ để tạo IAM user đầu tiên + vài config đặc biệt | **mọi việc hằng ngày** |

> [!quote] Ch. 2 — Root Account (tr. 8, dẫn tài liệu AWS)
> "We strongly recommend that you do not use the root user for your everyday tasks, even the administrative ones. Instead, adhere to the best practice of using the root user only to create your first IAM user."
>
> *Chúng tôi mạnh mẽ khuyến nghị **đừng dùng root user cho việc hằng ngày**, kể cả việc quản trị. Thay vào đó, hãy theo best practice: chỉ dùng root user để **tạo IAM user đầu tiên**.*

Và lớp bảo vệ bắt buộc: **MFA (multi-factor authentication)** — một yếu tố thứ hai vật lý (Google Authenticator, YubiKey) cho *cả* root user lẫn IAM user hằng ngày, vì "credential dễ bị lộ hoặc mất". Sách nhắc một cái bẫy: **đừng lưu MFA trong chính password manager** — làm vậy là vô hiệu hoá ý nghĩa "yếu tố thứ hai".

> [!warning] Thực tế: vì sao an toàn account là việc số 1
> Trên AWS thật, **không có giới hạn chi tiêu** — nên account bị chiếm = thảm hoạ tài chính, không chỉ mất dữ liệu. Kẻ tấn công có thể bật hàng loạt EC2 đào coin. "some EC2 instances can cost up to \$30,000 per month" (tr. 6). MFA + khoá root + IAM quyền tối thiểu là ba lớp chặn cơ bản. (IAM mổ sâu ở [Bài 1](bai_01_security-iam.md).)

## 6. Tránh tốn tiền bất ngờ

> [!quote] Ch. 2 — Avoiding Cost Surprises (tr. 9)
> "there is no enforceable spending limit for your AWS account."
>
> ***không có giới hạn chi tiêu nào cưỡng chế được** cho tài khoản AWS của bạn.*

Đây là điều khiến nhiều người *sợ* không dám học cloud. Ba lớp phòng thủ sách đưa ra:

| Công cụ | Làm gì |
| :--- | :--- |
| **Free Tier** | gần như mọi core service có hạn mức miễn phí (Lambda 400.000 GB-giây, S3 5GB, DynamoDB 25GB, API GW 1 triệu request, EC2/RDS 750 giờ micro) |
| **AWS Budgets** (báo động) | đặt ngưỡng; AWS *ước lượng* chi phí tương lai và **email cảnh báo** khi sắp/đã vượt (không realtime) |
| **IAM quyền tối thiểu** | chặn sẵn các hành động đắt (bật EC2 to) → "ngủ ngon vì biết mình *không thể* vô tình gây tốn" |

Một cạm bẫy đáng nhớ (sẽ gặp lại ở [Bài 7 — CloudWatch](bai_07_observability-cloudwatch.md)): **log cũng tốn tiền**. Ingest log vào CloudWatch tính theo GB — "exploding logs resulting in terabytes of ingested logs" là một trong các "horror story" chi phí mà start-up kể. Và **Lambda tính theo GB-giây** (bộ nhớ × thời gian), không theo số lần gọi — một công thức phản trực giác ta sẽ mổ ở [Bài 2](bai_02_compute.md).

> [!warning] Dùng LocalStack thì *không* lo tiền — nhưng vẫn phải học tư duy này
> Suốt khoá ta chạy trên LocalStack (miễn phí), nên không có hoá đơn. Nhưng mọi bài vẫn chỉ ra *"trên AWS thật, cái này tính tiền ra sao"* — vì ngày bạn deploy thật, tư duy chi phí phải sẵn trong đầu. **Thói quen `rb --force` dọn dẹp** ở Lab 0 chính là bước đầu của tư duy đó.

## 7. Shared Responsibility Model & Serverless

Hai mô hình tư duy nền, treo được rất nhiều kiến thức về sau lên chúng.

**Shared Responsibility Model** — ai lo cái gì:

> [!quote] Ch. 2 — Shared Responsibility Model (tr. 13)
> "AWS separates the responsibility into two categories: 'Security of the Cloud' and 'Security in the Cloud'."
>
> *AWS chia trách nhiệm thành hai loại: **"Security OF the Cloud"** và **"Security IN the Cloud"**.*

| | **Security OF the Cloud** (AWS lo) | **Security IN the Cloud** (BẠN lo) |
| :--- | :--- | :--- |
| Nghĩa | hạ tầng vật lý, phần cứng chạy mọi dịch vụ | cấu hình đúng & an toàn khi *dùng* dịch vụ |
| Ví dụ | datacenter, mạng lõi, host của S3 | ai được đọc bucket S3, mật khẩu DB, IAM policy |
| Mức công sức của bạn | 0 | **tuỳ dịch vụ**: S3 (managed) ít, EC2 (tự quản VM) nhiều |

Điểm then chốt: *càng dùng dịch vụ "managed/serverless", phần "của bạn" càng nhỏ* — bạn bớt phải lo hạ tầng, tập trung vào sản phẩm. Đó là lý do khoá nghiêng về serverless:

> [!quote] Ch. 2 — About going Serverless and Cloud-Native (tr. 14)
> "We strongly believe that the future lies in cloud-native and serverless technologies."
>
> *Chúng tôi tin chắc rằng **tương lai nằm ở công nghệ cloud-native và serverless**.*

*Cloud-native* nghĩa là phát triển ứng dụng và chọn/dùng hạ tầng **đi đôi với nhau**, thay vì tách "viết app" và "lo hosting". Với serverless (như Lambda — không có cả container để quản), bạn tạo/huỷ hạ tầng *trong chớp mắt, chỉ bằng code*, nhân bản cả hệ thống mà gần như không tốn công — và *không dùng thì không tốn tiền*. Đây là nền cho [Bài 8 — IaC](bai_08_infrastructure-as-code.md).

## 8. Capstone: dự án xuyên khoá

Để chống "học xong rơi rụng", cả khoá ráp dần **một ứng dụng serverless nhỏ** — mỗi bài thêm một mảnh, buộc bạn *dùng lại* kiến thức cũ trong ngữ cảnh mới:

```
         (API Gateway)          (Lambda)        (DynamoDB)
người ───► /notes POST ───► hàm xử lý ───► lưu ghi chú
dùng                              │
                                  ├──► (S3)        lưu file đính kèm
                                  └──► (SQS/SNS/EventBridge) xử lý async
                         (CloudWatch quan sát · IaC để deploy)
```

- [Bài 1 IAM] cấp quyền cho các hàm · [Bài 2 Compute] viết Lambda · [Bài 3 DB/Storage] DynamoDB + S3 · [Bài 4 Messaging] thêm xử lý async · [Bài 5 Networking] expose qua API Gateway · [Bài 7 Observability] gắn log/metric · [Bài 8 IaC] gói tất cả thành code deploy được.

Toàn bộ dịch vụ trên đều chạy **tốt trên LocalStack free** — nên capstone chạy thật từ đầu đến cuối trên máy bạn.

## 9. Thẻ ôn (active recall)

Tự trả lời **trước** khi xem. Những thẻ này là hạt giống cho master deck Anki ở [Bài 9](bai_09_capstone-tong-on.md).

> [!question] Thẻ 0.1 — Vì sao đọc thụ động không đủ để học AWS?
> **Đáp:** đường cong lãng quên — kiến thức thụ động rơi ~80% trong vài ngày. AWS còn trừu tượng + nhiều fact rời rạc + dịch vụ na ná → cần active recall, hands-on, giãn cách.

> [!question] Thẻ 0.2 — `awslocal` khác `aws` ở điểm nào?
> **Đáp:** `awslocal` = `aws --endpoint-url=http://localhost:4566` (trỏ vào LocalStack). Lệnh *y hệt* AWS thật, chỉ khác endpoint → kỹ năng chuyển thẳng được.

> [!question] Thẻ 0.3 — Root user vs IAM user: dùng cái nào cho việc hằng ngày?
> **Đáp:** **IAM user** (quyền tối thiểu, có MFA). Root user chỉ để tạo IAM user đầu tiên + vài config đặc biệt, rồi khoá lại.

> [!question] Thẻ 0.4 — AWS có đặt được giới hạn chi tiêu cứng không? Vậy chặn tốn tiền bằng gì?
> **Đáp:** **Không** có giới hạn cứng. Chặn bằng: Free Tier + AWS Budgets (cảnh báo email) + IAM quyền tối thiểu (chặn hành động đắt).

> [!question] Thẻ 0.5 — "Security OF the Cloud" vs "IN the Cloud" — ai lo cái nào?
> **Đáp:** OF = AWS lo (hạ tầng vật lý). IN = BẠN lo (cấu hình đúng/an toàn khi dùng). Càng managed/serverless, phần của bạn càng nhỏ.

## 10. Câu hỏi tự kiểm tra

1. Kể ba lý do kiến thức AWS khó nhớ, và vũ khí khắc chế từng cái. *(mục 1–2)*
2. Vì sao LocalStack hợp để *học* AWS? Nêu một hạn chế của nó. *(mục 3)*
3. Bốn thao tác cốt lõi với kho lưu trữ trong Lab 0 là gì? Vì sao bước 5 (dọn dẹp) quan trọng? *(mục 4)*
4. Khi nào dùng root user? Vì sao đừng lưu MFA trong password manager? *(tr. 6, 8)*
5. Giải thích Shared Responsibility Model bằng một ví dụ S3 và một ví dụ EC2. *(tr. 13)*

## Tóm tắt một trang

```
BÀI 0 — HỌC AWS SAO CHO NHỚ LÂU + LOCALSTACK
─────────────────────────────────────────────────────────
VẤN ĐỀ  đọc thụ động → quên 80%/vài ngày (Ebbinghaus). AWS khó vì
        trừu tượng + núi fact rời rạc + dịch vụ na ná.

4 VŨ KHÍ  generation (lab tự tay) · decision-first + interleaving
        (bảng "khi nào X vs Y") · active recall + spaced repetition
        (thẻ ôn/Anki) · cumulative project (capstone).
        "hands-on experience is essential to truly learn" (tr.5).

LOCALSTACK  giả lập AWS trên máy, MIỄN PHÍ, lệnh GIỐNG HỆT thật.
        awslocal = aws --endpoint-url=localhost:4566.
        Lab 0: s3 mb → cp → ls → cp - → rb (tạo/ghi/đọc/XOÁ).

AN TOÀN  root user = chủ, gần như không dùng; IAM user cho việc
        hằng ngày (quyền tối thiểu + MFA). "no enforceable spending
        limit" (tr.9) → Free Tier + Budgets + IAM chặn.
        EC2 có thể $30k/tháng (tr.6).

MÔ HÌNH  Shared Responsibility: OF the Cloud (AWS) vs IN the Cloud
        (bạn). Serverless = tương lai; app + hạ tầng đi đôi (tr.14).

CAPSTONE  API GW → Lambda → DynamoDB+S3, async SQS/SNS, CloudWatch,
        IaC — ráp dần xuyên 10 bài, chạy thật trên LocalStack.
```

## Nguồn

- **Tobias Schmidt & Alessandro Volpicella**, *AWS Fundamentals: AWS For The Real World* (2025) — **Ch.1 Introduction** (`tr. 1–4`): phạm vi, không tập trung thi chứng chỉ (tr. 4). **Ch.2 Getting Started** (`tr. 5–14`): hands-on là thiết yếu, tạo account (tr. 5); an toàn account, "great power great responsibility", MFA, EC2 $30k (tr. 6); khoá root, dùng IAM, trích tài liệu AWS về root (tr. 7–8); account/root/IAM user/group (tr. 8); tránh tốn tiền, "no enforceable spending limit", Free Tier (tr. 9); billing dashboard, Lambda GB-giây (tr. 10); Budgets & cảnh báo (tr. 11); Cost Explorer, IAM chặn chi phí (tr. 12); Shared Responsibility Model (tr. 13); serverless & cloud-native (tr. 14). `tai_lieu/AWS+Fundamentals.pdf`
- Phương pháp học dẫn từ ngoài sách: đường cong lãng quên (Ebbinghaus), testing effect / active recall, spaced repetition (SM-2/Anki), generation effect, interleaving, Feynman technique.
- Công cụ: [LocalStack](https://localstack.cloud) (giả lập AWS cục bộ), `awscli-local` (lệnh `awslocal`).
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack ← bạn đang ở đây] · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage](bai_03_database-storage.md) · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
