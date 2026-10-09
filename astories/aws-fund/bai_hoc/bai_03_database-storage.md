# Bài 3 — Database & Storage: RDS, DynamoDB, S3 — ba cách lưu dữ liệu

> [!info] Về bài này
> Dựng từ **Chương 6 — Database & Storage** của *AWS Fundamentals* (Schmidt & Volpicella, 2025 — `tai_lieu/`, `tr. 117–188`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 4`). Câu chốt **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vòng lặp nhớ-lâu: *mô hình tư duy → cách hoạt động → **bảng quyết định** → lab LocalStack → thẻ ôn → capstone*.
>
> **Chạy lab:** cần **Docker + LocalStack** + **awslocal**. **DynamoDB** và **S3** chạy tốt trên LocalStack free (lab thật). **RDS** cần Pro → học bằng khái niệm + bảng quyết định.

## Mục lục

1. [Mô hình tư duy: ba cách lưu dữ liệu](#1-mô-hình-tư-duy-ba-cách-lưu-dữ-liệu)
2. [RDS: SQL được quản lý trọn gói](#2-rds-sql-được-quản-lý-trọn-gói)
3. [DynamoDB: NoSQL không schema, khoá tổ hợp](#3-dynamodb-nosql-không-schema-khoá-tổ-hợp)
4. [S3: kho object bền bỉ](#4-s3-kho-object-bền-bỉ)
5. [Bảng quyết định: RDS vs DynamoDB vs S3](#5-bảng-quyết-định-rds-vs-dynamodb-vs-s3)
6. [Lab 3: DynamoDB cho capstone](#6-lab-3-dynamodb-cho-capstone)
7. [Cạm bẫy: hot partition, cost, schema](#7-cạm-bẫy-hot-partition-cost-schema)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mô hình tư duy: ba cách lưu dữ liệu

Ba dịch vụ, ba *hình dạng dữ liệu* khác nhau — chọn theo *dữ liệu của bạn trông như thế nào*:

| Dịch vụ | Lưu cái gì | Hình dạng |
| :--- | :--- | :--- |
| **RDS** | dữ liệu **quan hệ** (bảng, cột, join) | SQL — schema cứng |
| **DynamoDB** | dữ liệu **key-value / document** | NoSQL — không schema |
| **S3** | **file/blob** (ảnh, video, backup) | object — không phải database |

Treo ba cái lên câu hỏi: *"dữ liệu của tôi có quan hệ phức tạp, cần join?"* → RDS. *"cần tra cực nhanh theo khoá, quy mô lớn?"* → DynamoDB. *"là file lớn phi cấu trúc?"* → S3.

## 2. RDS: SQL được quản lý trọn gói

> [!quote] Ch. 6 — RDS (tr. 119)
> "Amazon Relational Database Service (RDS) is the fully-managed SQL database offered by AWS. […] You don't need to manage the infrastructure or operating system."
>
> *RDS là **cơ sở dữ liệu SQL được AWS quản lý trọn gói**. […] Bạn không phải quản hạ tầng hay hệ điều hành.*

Trước RDS, bạn phải tự dựng VM rồi lo OS, cập nhật, bảo mật, mạng… RDS gánh hết: chọn engine (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora), bấm vài nút, nhận *connection string*, xong. Các tính năng "managed" quan trọng: **Multi-AZ** (bản sao dự phòng ở vùng khả dụng khác, tự chuyển khi hỏng) và **Read Replica** (bản sao chỉ-đọc để chia tải đọc). Đây là lựa chọn khi dữ liệu *quan hệ*, cần **join, transaction ACID, truy vấn phức tạp**.

## 3. DynamoDB: NoSQL không schema, khoá tổ hợp

> [!quote] Ch. 6 — DynamoDB (tr. 134)
> "DynamoDB is a fully-managed NoSQL database that can handle any scale."
>
> *DynamoDB là **CSDL NoSQL được quản lý trọn gói**, chịu được **mọi quy mô**.*

Khác biệt lớn nhất với SQL là **schema**:

> [!quote] Ch. 6 — DynamoDB NoSQL (tr. 135)
> "You can write anything to your database, with the only required attribute being the primary key."
>
> *Bạn có thể ghi **bất cứ gì** vào CSDL, thuộc tính **bắt buộc duy nhất là primary key**.*

Nghĩa là mỗi item có thể có tập thuộc tính khác nhau (user pro có `subscription`, user free thì không). **Primary key** có hai kiểu:

> [!quote] Ch. 6 — Primary Key (tr. 135)
> "A composite key is composed of two keys. A partition and a sort key. The combination of these two keys uniquely identifies your item."
>
> *Khoá tổ hợp gồm hai khoá: **partition key** và **sort key**. **Kết hợp** cả hai mới định danh duy nhất một item.*

- **Partition key** (HASH): quyết định item nằm ở "ngăn" nào — DynamoDB băm nó để phân tán dữ liệu.
- **Sort key** (RANGE): trong cùng một partition, các item được *sắp xếp* theo khoá này → cho phép query kiểu "mọi note của user `an`, mới nhất trước".

Giá có hai chế độ: **On-Demand** (trả theo mỗi read/write thật — hợp tải khó đoán) và **Provisioned** (đặt sẵn capacity — rẻ hơn nếu tải ổn định). Capstone dùng On-Demand (`PAY_PER_REQUEST`).

## 4. S3: kho object bền bỉ

> [!quote] Ch. 6 — S3 (tr. 172)
> "S3 is not a database, but a BLOB (Binary Large Object Files) storage for saving large amounts of unstructured data. S3 is also one of the safest places in the world to store data due to its exceptionally high durability."
>
> *S3 **không phải database**, mà là kho **BLOB** (file nhị phân lớn) để lưu dữ liệu phi cấu trúc. S3 cũng là một trong những nơi **an toàn nhất thế giới** để lưu dữ liệu nhờ **độ bền (durability) cực cao**.*

S3 nổi tiếng với độ bền **"11 số 9"** (99.999999999% — gần như không bao giờ mất dữ liệu). Đơn vị là **bucket** (như thư mục) chứa **object** (file + metadata). Tên bucket phải **duy nhất toàn cầu** vì nó thành một URL. S3 có nhiều **storage class** đánh đổi giá ↔ tốc độ truy cập: `Standard` (nóng), `Infrequent Access` (ít dùng, rẻ hơn), `Glacier` (lưu trữ lạnh, rất rẻ, lấy ra chậm). Bạn đã làm `mb/cp/ls/rb` ở [Bài 0](bai_00_hoc-aws-nho-lau-va-localstack.md); capstone dùng S3 để lưu *file đính kèm* của note.

## 5. Bảng quyết định: RDS vs DynamoDB vs S3

| Tiêu chí | **RDS** | **DynamoDB** | **S3** |
| :--- | :--- | :--- | :--- |
| Mô hình | SQL quan hệ | NoSQL key-value/document | object/blob |
| Schema | **cứng** (định trước) | **không** (chỉ cần primary key) | không áp dụng |
| Truy vấn | join, transaction, SQL phức tạp | theo **khoá** (partition/sort), rất nhanh | theo **key** của object |
| Co giãn | dọc (máy to hơn) + read replica | **mọi quy mô**, tự động | gần như vô hạn |
| Serverless | không (Aurora Serverless có) | **có** | **có** |
| Hợp khi | dữ liệu quan hệ, cần join/ACID | tra nhanh theo khoá, quy mô lớn, tải bùng nổ | file lớn, ảnh, backup, static web |
| LocalStack free | cần Pro | **chạy tốt** | **chạy tốt** |

Quy tắc: *quan hệ + join* → RDS. *Khoá + tốc độ + quy mô* → DynamoDB. *File* → S3. (Và thường một app dùng **cả ba**: capstone dùng DynamoDB cho metadata note + S3 cho file đính kèm.)

## 6. Lab 3: DynamoDB cho capstone

Tạo bảng `notes` với **khoá tổ hợp** (`userId` + `noteId`), ghi item schema linh hoạt, rồi query:

```bash
# 1) tạo bảng: partition key userId (HASH) + sort key noteId (RANGE)
awslocal dynamodb create-table --table-name notes \
  --attribute-definitions AttributeName=userId,AttributeType=S AttributeName=noteId,AttributeType=S \
  --key-schema AttributeName=userId,KeyType=HASH AttributeName=noteId,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST \
  --query 'TableDescription.{Table:TableName,Status:TableStatus,Keys:KeySchema[].AttributeName}' --output table

# 2) put 2 item — item thứ 2 có THÊM thuộc tính 'pinned' (schema linh hoạt)
awslocal dynamodb put-item --table-name notes \
  --item '{"userId":{"S":"an"},"noteId":{"S":"n1"},"text":{"S":"mua sữa"}}'
awslocal dynamodb put-item --table-name notes \
  --item '{"userId":{"S":"an"},"noteId":{"S":"n2"},"text":{"S":"học AWS"},"pinned":{"BOOL":true}}'

# 3) get-item theo khoá ĐẦY ĐỦ (partition + sort)
awslocal dynamodb get-item --table-name notes \
  --key '{"userId":{"S":"an"},"noteId":{"S":"n2"}}' --query 'Item' --output json

# 4) query: MỌI note của user 'an' (chỉ cần partition key)
awslocal dynamodb query --table-name notes \
  --key-condition-expression "userId = :u" \
  --expression-attribute-values '{":u":{"S":"an"}}' \
  --query 'Items[].{note:noteId.S,text:text.S}' --output table

# 5) dọn
awslocal dynamodb delete-table --table-name notes
```

Kết quả chạy thật (bước 3 và 4):

```
{
    "noteId": { "S": "n2" },
    "pinned": { "BOOL": true },
    "text": { "S": "học AWS" },
    "userId": { "S": "an" }
}
```
```
---------------------
|       Query       |
+-------+-----------+
| note  |   text    |
+-------+-----------+
|  n1   |  mua sữa  |
|  n2   |  học AWS  |
+-------+-----------+
```

Hai điều cần thấy: (1) item `n1` *không có* `pinned`, item `n2` *có* — **không schema**, ghi gì cũng được miễn có primary key. (2) `query` chỉ với `userId` lấy *mọi* note của user đó — vì chúng chung một partition; sort key `noteId` cho phép lọc/sắp trong partition. Đây đúng là truy vấn capstone sẽ dùng: "lấy mọi note của user X".

> [!question] Tự thử
> 1. `get-item` chỉ với `userId` (thiếu `noteId`) — lỗi gì? (Gợi ý: khoá tổ hợp cần *cả hai*.)
> 2. Thêm sort key vào query: `userId = :u AND begins_with(noteId, :p)`. Nó lọc gì?
> 3. `scan` khác `query` ra sao? Vì sao `scan` tốn kém và nên tránh? (Gợi ý: scan đọc *cả bảng*.)

## 7. Cạm bẫy: hot partition, cost, schema

> [!warning] Thực tế & cạm bẫy Database/Storage
> - **Hot partition (DynamoDB).** Nếu partition key kém phân tán (vd mọi item cùng `userId="admin"`), mọi traffic dồn vào một partition → bị *throttle*. Chọn partition key *phân tán đều*.
> - **`scan` là kẻ thù chi phí.** `scan` đọc *toàn bảng* (tốn RCU + chậm). Luôn thiết kế để dùng `query` theo khoá. Đây là lý do "single-table design" của DynamoDB khó mà mạnh.
> - **NoSQL không phải "tốt hơn" SQL.** DynamoDB bắt bạn *biết trước access pattern* để thiết kế khoá; đổi pattern sau rất đau. SQL linh hoạt truy vấn hơn nhưng khó co giãn ngang. Dev nền SQL thường *vật lộn* với tư duy "không normalize" (tr.135).
> - **S3 cost = lưu + request + lấy ra.** Lưu `Standard` rẻ, nhưng `GET`/`PUT` nhiều và *data transfer ra ngoài* tính tiền. Chọn sai storage class (để file nóng ở Glacier) → lấy ra chậm + phí retrieval.
> - **S3 không phải file system.** Không có "thư mục" thật — `a/b/c.txt` chỉ là *key* phẳng; "folder" là ảo. Và S3 *không* sửa-tại-chỗ: ghi object là ghi đè cả object.
> - **LocalStack:** DynamoDB/S3 rất sát thật; RDS cần Pro nên không chạy ở đây — nhưng tư duy "khi nào SQL" phải có.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — Ba hình dạng dữ liệu → ba dịch vụ?
> **Đáp:** quan hệ (join/ACID) → **RDS** (SQL); key-value/document quy mô lớn → **DynamoDB** (NoSQL); file/blob → **S3** (object).

> [!question] Thẻ 3.2 — Partition key vs sort key trong DynamoDB?
> **Đáp:** partition key (HASH) phân tán item vào các ngăn; sort key (RANGE) sắp xếp trong một partition. Khoá tổ hợp = *cả hai* mới định danh duy nhất.

> [!question] Thẻ 3.3 — Thuộc tính bắt buộc duy nhất của một item DynamoDB?
> **Đáp:** **primary key**. Mọi thuộc tính khác tuỳ ý (không schema) — item này có, item kia không, đều được.

> [!question] Thẻ 3.4 — Vì sao tránh `scan` trong DynamoDB?
> **Đáp:** `scan` đọc *cả bảng* → tốn capacity + chậm. Thiết kế khoá để dùng `query` theo partition/sort.

> [!question] Thẻ 3.5 — S3 "11 số 9" nghĩa là gì? S3 có phải database không?
> **Đáp:** durability 99.999999999% — gần như không bao giờ mất object. **Không** phải database — là kho blob/object cho file phi cấu trúc.

## 9. Câu hỏi tự kiểm tra

1. Với mỗi loại dữ liệu, chọn dịch vụ: "hồ sơ user + đơn hàng có join", "đếm lượt xem mỗi video realtime", "ảnh đại diện". *(mục 5)*
2. SQL vs NoSQL khác nhau ở schema thế nào? *(tr. 135)*
3. Giải thích partition key + sort key qua bảng `notes` của lab. *(tr. 135, mục 6)*
4. Multi-AZ và Read Replica của RDS giải quyết vấn đề gì? *(mục 2)*
5. Kể ba cạm bẫy chi phí: một ở DynamoDB, một ở S3. *(mục 7)*

## Tóm tắt một trang

```
BÀI 3 — DATABASE & STORAGE: RDS / DYNAMODB / S3
─────────────────────────────────────────────────────────
HÌNH DẠNG DỮ LIỆU → DỊCH VỤ
   quan hệ (join/ACID)        → RDS (SQL, managed, tr.119)
   key-value/document, scale  → DynamoDB (NoSQL, tr.134)
   file/blob                  → S3 (object, KHÔNG database, tr.172)

RDS  SQL trọn gói, không lo OS (tr.119). Multi-AZ (dự phòng) +
     Read Replica (chia tải đọc). Engine: MySQL/Postgres/Aurora...

DYNAMODB  "ghi bất cứ gì, chỉ cần PRIMARY KEY" (tr.135) — KHÔNG schema.
     Composite key = partition(HASH, phân tán) + sort(RANGE, sắp xếp)
     (tr.135). On-Demand vs Provisioned.
     LAB: create-table (userId+noteId) → put (schema linh hoạt) →
     query theo userId → mọi note của 'an'.

S3  "11 số 9" durability (tr.172). bucket (duy nhất toàn cầu) chứa
     object. Storage class: Standard/IA/Glacier. KHÔNG file system thật.

CẠM BẪY  hot partition · SCAN tốn kém (dùng query) · NoSQL cần biết
     trước access pattern · S3 cost = lưu+request+transfer.
```

> [!note] Đào sâu nền tảng
> Khoá nền [`cloud-base`](../../cloud-base/README.md) giải thích *vì sao* mỗi lựa chọn Database/Storage lại hành xử như vậy:
> - **Độ bền S3 "11 nines" · EBS · WAL của Aurora** → [cloud-base Bài 3 — lưu trữ bền (journaling)](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md).
> - **Eventually vs strongly consistent read · Multi-AZ** → [Bài 8 — nhân bản & CAP](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md).
> - **Hot partition & cách chọn partition key** → [Bài 9 — phân mảnh & consensus](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md).
> - **RDS (B-tree) vs DynamoDB (LSM) · vì sao mỗi GSI tốn WCU** → [Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md).
> - **RDS vs DynamoDB vs Neptune = chọn data model** → [Bài 17 — data models](../../cloud-base/bai_hoc/bai_17_du-lieu-data-models.md): vì sao DynamoDB ép "single-table / access-pattern-first".
> - **DynamoDB Transactions (atomic commit)** → [Bài 16 — transaction & saga](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md): all-or-nothing qua nhiều item là một dạng consensus.

## Nguồn

- **Schmidt & Volpicella**, *AWS Fundamentals* (2025) — **Ch.6 Database & Storage** (`tr. 117–188`): RDS "fully-managed SQL database", không lo OS, trước RDS phải tự dựng VM (tr. 119); Multi-AZ, read replica, engines (tr. 119–133); DynamoDB "fully-managed NoSQL, any scale" (tr. 134); không schema, "chỉ cần primary key", partition + sort key (tr. 134–136); on-demand vs provisioned (tr. 136+); S3 "BLOB storage, not a database, exceptionally high durability", bucket/object, tên duy nhất toàn cầu (tr. 172); storage classes (tr. 173+). `tai_lieu/AWS+Fundamentals.pdf`
- Công cụ: LocalStack + `awslocal` (DynamoDB, S3 chạy thật).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 4`.

---

**Bản đồ khoá học:** [Bài 0 — Học AWS & LocalStack](bai_00_hoc-aws-nho-lau-va-localstack.md) · [Bài 1 — Security: IAM](bai_01_security-iam.md) · [Bài 2 — Compute](bai_02_compute.md) · [Bài 3 — Database & Storage ← bạn đang ở đây] · [Bài 4 — Messaging](bai_04_messaging.md) · [Bài 5 — Networking](bai_05_networking.md) · [Bài 6 — CI/CD](bai_06_cicd.md) · [Bài 7 — Observability](bai_07_observability-cloudwatch.md) · [Bài 8 — Infrastructure as Code](bai_08_infrastructure-as-code.md) · [Bài 9 — Capstone & tổng ôn](bai_09_capstone-tong-on.md) · [Bài 10 — Logs & Insights](bai_10_logs-insights.md)

Xem thêm [README khoá học](../README.md).
