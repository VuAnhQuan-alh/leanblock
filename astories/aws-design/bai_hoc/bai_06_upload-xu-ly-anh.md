# Bài 6 — Thiết kế upload và xử lý ảnh/video

> [!info] Về bài này
> **Archetype 6 — dữ liệu lớn không đi qua API.** Ảnh/video hàng MB–GB mà nhét qua `POST` tới Lambda thì đập trần payload, tốn băng thông API, chặn compute. Lời giải: **client upload THẲNG lên S3 bằng presigned URL** (không qua server), rồi **S3 phát event** kích pipeline xử lý **bất đồng bộ** (resize, quét virus, trích metadata). Hai kỹ thuật: *presigned URL* (offload + chữ ký) và *event-driven + backpressure*.
> Nguồn: **WA** (S3 durability) + **BL** *Avoiding insurmountable queue backlogs*. Nền: [cloud-base Bài 14 (chữ ký/SigV4)](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md), [Bài 11 (event stream)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md), [Bài 3 (durability)](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md); dịch vụ: [aws-fund Bài 3 (S3)](../../aws-fund/bai_hoc/bai_03_database-storage.md).
> **Lab:** presigned URL + S3 event trên LocalStack.
> Nên đọc trước: [Bài 5 — thanh toán](bai_05_thanh-toan-idempotent.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: upload thẳng S3, xử lý event-driven](#2-kiến-trúc-upload-thẳng-s3-xử-lý-event-driven)
3. [Đào sâu: presigned URL và backpressure](#3-đào-sâu-presigned-url-và-backpressure)
4. [Lab: presigned upload và S3 event trigger](#4-lab-presigned-upload-và-s3-event-trigger)
5. [Soi Well-Architected](#5-soi-well-architected)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] Người dùng kéo-thả một video 500 MB
> App ảnh của bạn: user chọn ảnh/video, bấm Upload. Cách làm ngây thơ: `POST /upload` gửi file qua API Gateway → Lambda → Lambda ghi vào S3. Vấn đề ập tới ngay: API Gateway **chặn payload ở 10 MB** (video 500MB tạch), Lambda bị *giữ chạy* suốt lúc nhận byte (trả tiền để... chuyển byte), và 1000 người upload cùng lúc thì 2 GB/s chảy qua compute. Byte lớn **không nên đi qua API**. Bài này tách đường đi của byte ra khỏi đường điều khiển.

**Chức năng:** user upload ảnh; hệ lưu bền + sinh thumbnail + trích metadata. **Phi chức năng:** không chặn API bằng byte lớn, lưu không mất, xử lý chịu được *spike* (viral upload), và xử lý hỏng thì không mất ảnh gốc.

Ước lượng: ảnh trung bình 2 MB; nếu 1000 upload/s qua API Gateway→Lambda thì **2 GB/s** chảy qua compute — đập giới hạn payload (API GW: 10 MB) và đốt Lambda vào việc *chuyển byte* thay vì *logic*. Kết luận ép ngay: **tách đường dữ liệu khỏi đường điều khiển** — byte đi thẳng S3, API chỉ cấp phép.

## 2. Kiến trúc: upload thẳng S3, xử lý event-driven

```
   (1) xin phép:  client ─▶ API GW ─▶ Lambda ─▶ trả PRESIGNED URL (ký, có hạn)
   (2) upload:    client ─ PUT bytes ───────────────────────────▶ S3  (KHÔNG qua server)
   (3) kích xử lý: S3 ─ ObjectCreated event ─▶ SQS ─▶ worker (resize/scan/metadata)
                                                 │ lỗi → retry → DLQ (Bài 4)
```

Ba bước tách bạch: API chỉ cấp một **presigned URL** (một chữ ký cho phép PUT đúng object đó, trong thời hạn) — byte không chạm server. S3 lưu bền (mục 3) và **phát event** khi có object mới; event vào SQS → worker xử lý *bất đồng bộ*. S3 lưu *ảnh gốc* bất biến, nên worker hỏng thì chỉ cần phát lại event, không mất gì (nối cloud-base Bài 11: object = sự kiện bất biến).

## 3. Đào sâu: presigned URL và backpressure

> [!example] Hai ẩn dụ
> **Presigned URL** = tấm *phiếu gửi hàng có chữ ký kho + hết hạn*. Kho (server) ký một phiếu: "cho phép bỏ đúng kiện này vào ô A-12, trong 15 phút". Bạn cầm phiếu tới cửa kho bỏ hàng *thẳng* — không cần qua văn phòng (API), không cần chìa khoá kho (khoá AWS). Hết 15 phút phiếu vô giá trị.
> **Backpressure (đệm bằng queue)** = cái *phễu*: đổ nước ào ạt (spike upload) vào miệng phễu, nước chảy ra cổ phễu *đều đặn* bằng tốc độ worker kham nổi. Phễu chịu được *đợt* nước to; nhưng nếu đổ liên tục nhanh hơn cổ phễu thoát, phễu vẫn tràn (backlog).

**(a) Presigned URL = chữ ký uỷ quyền có hạn.** Server không cầm byte; nó *ký* một URL cho phép client PUT đúng một object, hết hạn sau N phút. Chữ ký đó là **SigV4** — đúng "chữ ký số" của [cloud-base Bài 14](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md): client không có khoá AWS vẫn upload được, vì URL *đã mang* chữ ký của server (bạn sẽ thấy `X-Amz-Algorithm=AWS4-HMAC-SHA256` trong URL ở lab). Ảnh gốc nằm trên S3 — nơi bền nhất:

> [!quote] WA (tr. 43)
> "Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications for companies all around the world."
>
> *Amazon S3 được thiết kế cho độ bền **99.999999999% (11 số 9)**, lưu dữ liệu cho hàng triệu ứng dụng.* (nền: nhân bản đa-AZ — [cloud-base Bài 3/8](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md).)

**(b) Event-driven + backpressure.** Dùng SQS giữa S3-event và worker để *đệm* spike — đây là lý do queue mạnh, nhưng phải tỉnh táo:

> [!quote] BL: avoiding-insurmountable-queue-backlogs
> "Queues are powerful tools for building reliable asynchronous systems."
>
> *Queue là **công cụ mạnh để xây hệ bất đồng bộ tin cậy**.*

> [!quote] BL: avoiding-insurmountable-queue-backlogs
> "While it may be easy to see the benefits of a queue for processing messages asynchronously, the risks of using a queue are more subtle."
>
> *Lợi ích của queue cho xử lý bất đồng bộ thì dễ thấy, nhưng **rủi ro của việc dùng queue lại tinh vi hơn**.*

Rủi ro tinh vi: khi upload spike (viral), event dồn vào queue nhanh hơn worker xử lý → **backlog** phình, thumbnail trễ hàng giờ. Queue hấp thụ spike (*backpressure* — biến đỉnh nhọn thành dòng đều mà worker kham nổi), nhưng nếu tốc độ *trung bình* vượt công suất worker thì queue chỉ *trì hoãn* sập, không tránh. Lời chữa (BL Bài 4): autoscale worker theo queue depth, ưu tiên, và quan trọng nhất *ngăn* backlog (giới hạn tốc độ nhận — Bài 2). Queue là cái đệm, không phải phép màu.

## 4. Lab: presigned upload và S3 event trigger

Client upload **thẳng S3** bằng presigned URL (không qua server), rồi S3 phát event kích xử lý. Chạy thật trên LocalStack:

```bash
awslocal s3 mb s3://uploads-demo
echo "hello-image-bytes" > pic.jpg

# (1) server CẤP presigned URL (ký SigV4, hết hạn 300s)
URL=$(awslocal s3 presign s3://uploads-demo/user1/pic.jpg --expires-in 300)
echo "URL: ${URL:0:80}..."          # chú ý X-Amz-Algorithm=AWS4-HMAC-SHA256 (chữ ký)

# (2) client PUT bytes THẲNG lên S3 bằng URL đó — KHÔNG qua API server
curl -s -X PUT --upload-file pic.jpg "$URL" -o /dev/null -w "PUT status=%{http_code}\n"
awslocal s3 ls s3://uploads-demo/user1/ --recursive

# (3) nối event: object mới → gửi sang SQS để worker xử lý
PROC=$(awslocal sqs create-queue --queue-name img-process --query 'QueueUrl' --output text)
ARN=$(awslocal sqs get-queue-attributes --queue-url $PROC --attribute-names QueueArn --query 'Attributes.QueueArn' --output text)
awslocal s3api put-bucket-notification-configuration --bucket uploads-demo \
  --notification-configuration "{\"QueueConfigurations\":[{\"QueueArn\":\"$ARN\",\"Events\":[\"s3:ObjectCreated:*\"]}]}"
awslocal s3 cp pic.jpg s3://uploads-demo/user1/pic2.jpg      # upload mới → sinh event
sleep 1
awslocal sqs receive-message --queue-url $PROC --query 'length(Messages)' --output text   # >0: event đã tới
```

Kết quả chạy thật *(thời gian/ID tuỳ máy; điều cần nhìn: PUT 200 không-qua-server và object lên S3)*:

```
URL: http://localhost:4566/uploads-demo/user1/pic.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA25...
PUT status=200
2026-10-07 ...   18 user1/pic.jpg
```

PUT trả **200** — client đẩy byte *thẳng* vào S3 bằng URL đã ký, server không hề nhận byte nào (chỉ cấp chữ ký ở bước 1). `X-Amz-Algorithm=AWS4-HMAC-SHA256` trong URL là chữ ký SigV4 (cloud-base Bài 14): nó *là* uỷ quyền, nên dù client không có khoá AWS vẫn upload đúng object được phép, trong hạn. Bước (3) nối S3→SQS: mỗi object mới sinh một event vào queue xử lý — upload và xử lý *tách rời*, worker chạy nền và chịu được spike nhờ queue đệm.

> [!note] Tự thử
> 1. Thử PUT lên *key khác* bằng cùng URL (`.../pic.jpg` nhưng upload vào `pic99.jpg`): vì sao bị từ chối? (chữ ký gắn với *đúng* object + method — cloud-base Bài 14).
> 2. Đợi quá `--expires-in` rồi PUT: 403. Vì sao presigned URL phải có hạn?
> 3. Upload 100 object liên tiếp: queue xử lý dồn lên — đây là backlog (mục 3). Worker nên autoscale theo gì?

## 5. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | S3 11 9's giữ ảnh gốc; worker hỏng → phát lại event | ảnh gốc bất biến = nguồn chân lý |
| Performance | byte không qua compute; xử lý async không chặn upload | queue đệm spike (backpressure) |
| Cost | không trả Lambda cho việc chuyển byte; S3 storage class | lifecycle: ảnh cũ → IA/Glacier |
| Security | presigned = uỷ quyền hẹp, có hạn; không lộ khoá | validate content-type/size; quét virus |
| Operational | theo dõi backlog queue xử lý + tỉ lệ fail | DLQ cho ảnh xử lý lỗi (Bài 4) |

Nguyên tắc đọng lại: **tách đường dữ liệu (byte → S3) khỏi đường điều khiển (API ký), rồi xử lý event-driven có đệm.** Cho tới giờ các bài giả định hệ *khoẻ*. Khi lưu lượng *vọt đột ngột* vượt mọi dự phòng thì sao — làm sao không sập dây chuyền? Đó là Bài 7.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — Vì sao không cho ảnh đi qua API→Lambda?
> **Đáp:** byte lớn đập trần payload (API GW 10MB), đốt băng thông + compute vào *chuyển byte*. Tách đường dữ liệu: byte thẳng S3, API chỉ cấp phép.

> [!question] Thẻ 6.2 — Presigned URL là gì? Nối về khái niệm nền nào?
> **Đáp:** URL **đã ký (SigV4)** cho phép client PUT/GET đúng một object, có hạn — client không cần khoá AWS. Chính là **chữ ký số** của cloud-base Bài 14.

> [!question] Thẻ 6.3 — Vì sao lưu ảnh gốc trên S3 làm pipeline chịu lỗi tốt?
> **Đáp:** S3 11 9's + ảnh gốc **bất biến** = nguồn chân lý; worker hỏng chỉ cần **phát lại event**, không mất gì (cloud-base Bài 11).

> [!question] Thẻ 6.4 — Queue đệm spike (backpressure) — nhưng "rủi ro tinh vi" là gì?
> **Đáp:** queue hấp thụ *đỉnh nhọn*, nhưng nếu tốc độ **trung bình** vượt công suất worker thì backlog phình → chỉ trì hoãn sập. Phải autoscale + ngăn backlog.

> [!question] Thẻ 6.5 — Hai lý do presigned URL phải có hạn + gắn đúng object?
> **Đáp:** chữ ký gắn method+key cụ thể → không dùng upload chỗ khác; có hạn → URL rò rỉ không bị lạm dụng mãi (cloud-base Bài 14).

## 7. Câu hỏi tự kiểm tra

1. Từ ước lượng (2MB/ảnh, 1000/s), vì sao phải tách đường dữ liệu khỏi API? *(mục 1)*
2. Vẽ 3 bước: cấp phép → upload thẳng → event xử lý. Vai trò mỗi bước? *(mục 2)*
3. Presigned URL hoạt động ra sao? SigV4 ở đâu trong đó? *(mục 3, cloud-base Bài 14)*
4. Queue cho backpressure gì, và rủi ro tinh vi gì? *(mục 3, BL)*
5. Chạy lab §4. Vì sao PUT 200 mà server không nhận byte? Thử key sai → gì? *(mục 4)*

## Tóm tắt một trang

```
BÀI 6 — UPLOAD & XỬ LÝ ẢNH
─────────────────────────────────────────────────────────
VẤN ĐỀ  ảnh MB-GB không qua API→Lambda (trần payload, đốt compute chuyển byte).
   → TÁCH đường dữ liệu (byte→S3) khỏi đường điều khiển (API ký).

KIẾN TRÚC  (1) API cấp PRESIGNED URL; (2) client PUT thẳng S3; (3) S3 event →
   SQS → worker xử lý async (resize/scan). Lỗi → retry → DLQ (Bài 4).

ĐÀO SÂU  (a) presigned = chữ ký SigV4 có hạn, gắn đúng object (cloud-base Bài
   14); client không cần khoá AWS. S3 11 9's giữ ảnh gốc (WA tr.43). (b) queue
   mạnh nhưng "rủi ro tinh vi" (BL): đệm ĐỈNH nhọn, nhưng trung bình>công suất
   → backlog phình. Queue là đệm, không phải phép màu.

LAB  presign → PUT thẳng S3 (200, server không nhận byte, URL mang
   AWS4-HMAC-SHA256) → S3 event → SQS. Upload & xử lý tách rời.

6 TRỤ  reliability (ảnh gốc bất biến, phát lại event) + performance + cost;
   security (uỷ quyền hẹp có hạn). Tiếp: lưu lượng VỌT bất ngờ → Bài 7.
```

## Nguồn

- **AWS Well-Architected Framework** — Reliability: S3 11 9's durability (tr. 43). `tai_lieu/AWS-Well-Architected-Framework.pdf` (offset +5).
- **Amazon Builders' Library** — *Avoiding insurmountable queue backlogs*: queue mạnh nhưng rủi ro tinh vi. `tai_lieu/bl_avoiding-insurmountable-queue-backlogs.txt`.
- Nền: [cloud-base Bài 14 (chữ ký/SigV4)](../../cloud-base/bai_hoc/bai_14_mang-bao-mat.md), [Bài 11 (event bất biến)](../../cloud-base/bai_hoc/bai_11_du-lieu-batch-stream.md), [Bài 3 (durability)](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md).
- Dịch vụ: [aws-fund Bài 3 — S3](../../aws-fund/bai_hoc/bai_03_database-storage.md), [Bài 4 — SQS/DLQ](../../aws-fund/bai_hoc/bai_04_messaging.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · **[Bài 6 — Upload & xử lý ảnh] ← bạn đang ở đây** · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
