# Bài 1 — Thiết kế URL shortener ở quy mô

> [!info] Về bài này
> **Archetype 1 — key-value đọc-nặng.** Bài toán kinh điển nhất: rút gọn URL (`a1B2c3` → URL dài). Đơn giản bề mặt, nhưng ở quy mô nó dạy ba quyết định cốt lõi của mọi hệ KV: **chọn data store theo access pattern**, **partition key để tránh hot key**, và **cache cho đường đọc**.
> Nguồn: **WA** (Performance Efficiency — data store, caching). Nền: [cloud-base Bài 9 (sharding/hot partition)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 6 (latency/CDN)](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md); dịch vụ: [aws-fund Bài 3 (DynamoDB)](../../aws-fund/bai_hoc/bai_03_database-storage.md).
> **Trích:** `WA (tr. X)` = trang **in** (PDF = tr. + 5). **Lab:** DynamoDB chạy thật trên LocalStack.
> Nên đọc trước: [Bài 0 — phương pháp](bai_00_phuong-phap-system-design.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: API, KV store, cache](#2-kiến-trúc-api-kv-store-cache)
3. [Đào sâu: partition key, hot key, cache](#3-đào-sâu-partition-key-hot-key-cache)
4. [Lab: DynamoDB KV và atomic counter](#4-lab-dynamodb-kv-và-atomic-counter)
5. [Soi Well-Architected](#5-soi-well-architected)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] Bạn vừa nhận việc
> Sếp: *"Làm cho tôi cái như bit.ly — dán URL dài vào, trả về link ngắn `short.ly/a1B2c3`; ai bấm link ngắn thì nhảy tới URL gốc."* Bạn mở editor, định tạo một bảng MySQL `(id tự tăng, url)` và dùng `id` làm code. Dừng lại — ở quy mô 100 triệu user, lựa chọn "hiển nhiên" đó vấp hai bẫy (code tuần tự gây điểm nóng; một DB SQL không gánh nổi lượt đọc). Hãy để **ước lượng** chỉ đường trước.

**Chức năng:** `POST /urls {url}` → trả về code ngắn; `GET /{code}` → redirect tới URL gốc. **Phi chức năng:** đọc nặng, p99 redirect < 50ms, không được mất mapping, rẻ.

Ước lượng (Bài 0): 100M DAU, ~0.1 ghi/người/ngày, đọc/ghi 100:1 → **~116 writes/s, ~35k reads/s đỉnh, ~9 TB/5 năm**. Ba con số này quyết gần hết kiến trúc, dựa trên đúng các yếu tố WA bảo phải cân khi chọn data store:

> [!quote] WA (tr. 736)
> "Data access patterns (read-heavy or write-heavy) • Latency • Throughput • IOPS (input/output operations per second) • Data retention period"
>
> *Các yếu tố chọn data store: **mẫu truy cập (đọc-nặng hay ghi-nặng)**, độ trễ, throughput, IOPS, thời gian lưu giữ.*

Đọc-nặng + 35k reads/s + truy vấn *chỉ theo khoá* (code) → **key-value store scale ngang (DynamoDB)**, không RDBMS đơn; và đọc áp đảo → **phải có cache**.

## 2. Kiến trúc: API, KV store, cache

```
   WRITE  POST /urls
      client ─▶ API Gateway ─▶ Lambda ─▶ DynamoDB  (put: code → url)

   READ   GET /{code}   (đường nóng, 35k/s)
      client ─▶ API Gateway ─▶ Lambda ─┬─▶ ElastiCache  (hit: trả ngay)
                                       └─▶ DynamoDB      (miss: đọc rồi nạp cache)
      code sinh từ HASH (base62) → rải đều partition  ·  hits tăng bằng atomic ADD
```

Hai đường tách bạch: *write* hiếm, đi thẳng DynamoDB; *read* nhiều, qua cache trước. DynamoDB lo KV + độ bền + scale ngang; ElastiCache (hoặc DAX) cắt độ trễ đường đọc. Hai quyết định tinh tế nằm ở mục 3.

Lần theo **một cú bấm link** `short.ly/a1B2c3` để thấy đường đọc hoạt động:

```
   lượt 1 (cache lạnh):  GET /a1B2c3
      → ElastiCache: không có "a1B2c3"  (MISS)
      → DynamoDB: get-item code=a1B2c3  → url (vài ms)
      → nạp vào cache  → trả 301 redirect
   lượt 2..1.000.000 (cache ấm):  GET /a1B2c3
      → ElastiCache: có "a1B2c3"  (HIT, ~microsecond)  → trả ngay, KHÔNG đụng DynamoDB
```

Một URL viral được bấm một triệu lần: *một* lần chạm DynamoDB (miss đầu), 999.999 lần còn lại cache nuốt trọn. Đây là lý do cache không phải "tối ưu thêm" mà là *trụ chịu tải chính* của đường đọc.

## 3. Đào sâu: partition key, hot key, cache

> [!example] Hai ẩn dụ
> **Hot partition** = siêu thị mở 10 quầy tính tiền nhưng bắt *mọi* khách xếp đúng *một* hàng: 9 quầy ngồi chơi, 1 quầy quá tải. Code tuần tự ép mọi ghi mới vào "quầy mới nhất". Code hash rải khách đều 10 quầy.
> **Cache** = cuốn sổ ghi sẵn vài số điện thoại hay gọi: khỏi tra danh bạ dày mỗi lần. Vì số ít đổi, sổ gần như luôn đúng — y như mapping code→url gần bất biến.

**(a) Partition key chọn sai = hot key.** DynamoDB băm partition key để rải dữ liệu (cloud-base Bài 9). Nếu code sinh *tuần tự* (`1, 2, 3...`), mọi ghi mới dồn vào partition "mới nhất" → **hot partition**, throttle dù bảng còn thừa capacity. Lời giải: sinh code từ **hash/random base62** (vd `a1B2c3`) → phân bố đều, không điểm nóng. Đây đúng là cột `[12,0,0]` vs `[5,5,2]` của [cloud-base Bài 9](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md).

**(b) Cache cho đường đọc.** 35k reads/s mà mỗi đọc đập DynamoDB thì đắt và chạm trần độ trễ (cloud-base Bài 6: "round-trip rẻ nhất là round-trip không làm"):

> [!quote] WA (tr. 755)
> "A cache is a software or hardware component aimed at storing data so that future requests for the same data can be served faster or more efficiently."
>
> *Một **cache** là thành phần phần mềm/phần cứng nhằm **lưu dữ liệu để các yêu cầu sau cho cùng dữ liệu được phục vụ nhanh hơn**.*

Vì mapping code→url **gần như bất biến** (tạo xong hiếm đổi), cache cực hiệu quả: tỉ lệ hit cao, không lo invalidation phức tạp. Với URL "viral" (một code được đọc hàng triệu lần), cache hấp thụ toàn bộ tải nóng — đây là lý do cache *bắt buộc* chứ không phải tối ưu thêm. Lựa chọn nhất quán: eventual-consistent read của DynamoDB (cloud-base Bài 8) là đủ, vì đọc URL cũ vài giây vô hại.

## 4. Lab: DynamoDB KV và atomic counter

Dựng bảng `code → url`, đọc theo khoá (đường nóng), và đếm hit bằng **atomic ADD** (chống race — cloud-base Bài 2), tất cả thật trên LocalStack:

```bash
awslocal dynamodb create-table --table-name Urls \
  --attribute-definitions AttributeName=code,AttributeType=S \
  --key-schema AttributeName=code,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST --query 'TableDescription.TableStatus' --output text

# WRITE: mapping code -> url (code là HASH key → rải đều)
awslocal dynamodb put-item --table-name Urls \
  --item '{"code":{"S":"a1B2c3"},"url":{"S":"https://example.com/very/long/path"},"hits":{"N":"0"}}'

# READ (đường nóng): GET theo partition key — O(1) theo khoá
awslocal dynamodb get-item --table-name Urls --key '{"code":{"S":"a1B2c3"}}' \
  --query 'Item.url.S' --output text

# đếm hit bằng ATOMIC ADD (nhiều Lambda tăng đồng thời không mất cập nhật)
awslocal dynamodb update-item --table-name Urls --key '{"code":{"S":"a1B2c3"}}' \
  --update-expression 'ADD hits :one' --expression-attribute-values '{":one":{"N":"1"}}' \
  --return-values UPDATED_NEW --query 'Attributes.hits.N' --output text

awslocal dynamodb delete-table --table-name Urls   # dọn
```

Kết quả chạy thật:

```
CREATING
# GET theo partition key (đường đọc nóng — O(1) theo key):
https://example.com/very/long/path
# tăng hits bằng atomic ADD (không race — cloud-base Bài 2):
1
```

GET theo `code` trả URL trong một thao tác theo khoá — đây là lý do KV hợp bài toán này hơn SQL (không join, không scan). `ADD hits :one` tăng đếm *phía server* atomic: mười Lambda cùng tăng không mất cập nhật (đúng demo race của cloud-base Bài 2, giờ giải bằng atomic op của DynamoDB). Trong thật, thêm ElastiCache trước GET để hấp thụ 35k reads/s — LocalStack free không chạy ElastiCache nên phần cache học bằng kiến trúc mục 3.

> [!note] Tự thử
> 1. `put-item` với `code` tuần tự `000001, 000002...` rồi nghĩ: vì sao điều này gây hot partition còn `a1B2c3` thì không? (cloud-base Bài 9)
> 2. Thêm `ConditionExpression attribute_not_exists(code)` vào put-item: chống ghi đè code trùng — chạy hai lần, lần hai lỗi. Vì sao đây là "tạo an toàn"?
> 3. Đọc bằng `--consistent-read`: đắt gấp đôi RCU. Với URL shortener, eventual read có chấp nhận được không? (cloud-base Bài 8)

## 5. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | DynamoDB multi-AZ; mapping không mất | eventual read OK vì dữ liệu gần bất biến |
| Performance | cache + KV O(1) theo khoá | hot key chặn bằng code hash |
| Cost | cache cắt RCU; PAY_PER_REQUEST hợp traffic thất thường | cache giảm mạnh chi phí đọc |
| Security | chống enumeration (đoán code), rate-limit tạo link | → Bài 2 |
| Operational | serverless, ít vận hành | theo dõi hit/miss cache, hot key |

Nút thắt đã xử: hot partition (code hash), độ trễ đọc (cache). Nút thắt *còn lại* — ai đó spam `POST /urls` hoặc đoán code hàng loạt — là bài toán **rate limiting** (Bài 2).

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — Vì sao URL shortener chọn KV (DynamoDB) chứ không RDBMS?
> **Đáp:** truy vấn *chỉ theo khoá* (code), đọc-nặng, 35k reads/s đỉnh → cần KV scale ngang O(1) theo khoá; không cần join/scan của SQL.

> [!question] Thẻ 1.2 — Code tuần tự gây vấn đề gì? Cách tránh?
> **Đáp:** **hot partition** — mọi ghi dồn một partition → throttle. Tránh bằng code **hash/random base62** để rải đều (cloud-base Bài 9).

> [!question] Thẻ 1.3 — Vì sao cache *bắt buộc* ở đây, và vì sao dễ (ít lo invalidation)?
> **Đáp:** đọc/ghi 100:1 + URL viral → cache hấp thụ tải nóng. Dễ vì mapping code→url **gần bất biến** → hit cao, hiếm phải invalidate.

> [!question] Thẻ 1.4 — Mức nhất quán nào đủ cho đọc URL? Vì sao?
> **Đáp:** **eventual consistent** (rẻ gấp đôi so với strong) — đọc URL "cũ" vài giây vô hại; mapping hiếm đổi (cloud-base Bài 8).

> [!question] Thẻ 1.5 — `ADD hits :one` giải vấn đề gì so với đọc-cộng-ghi?
> **Đáp:** **atomic counter phía server** — nhiều client tăng đồng thời không mất cập nhật (race của cloud-base Bài 2 giải bằng atomic op).

## 7. Câu hỏi tự kiểm tra

1. Từ ước lượng (35k reads/s, 9TB, đọc/ghi 100:1), suy ra ba quyết định kiến trúc. *(mục 1–2)*
2. Giải thích hot partition với code tuần tự. Vì sao hash base62 chữa được? *(mục 3, cloud-base Bài 9)*
3. Vì sao cache đặc biệt hiệu quả cho URL shortener? Mức nhất quán đọc? *(mục 3, WA tr. 755)*
4. Chạy lab §4. Vì sao GET theo key hợp KV hơn SQL? `ADD` giải race ra sao? *(mục 4)*
5. Soi 6 trụ: thiết kế mạnh/yếu ở đâu? Nút thắt còn lại dẫn sang bài nào? *(mục 5)*

## Tóm tắt một trang

```
BÀI 1 — URL SHORTENER (KV đọc-nặng)
─────────────────────────────────────────────────────────
ƯỚC LƯỢNG  100M DAU, đọc/ghi 100:1 → ~116 writes/s, ~35k reads/s đỉnh, ~9TB.
   → KV scale ngang (DynamoDB) + CACHE bắt buộc (WA tr.736: chọn store theo
     access pattern).

KIẾN TRÚC  write: API GW→Lambda→DynamoDB. read(nóng): →cache→(miss)DynamoDB.

ĐÀO SÂU  (a) HOT KEY: code tuần tự → hot partition; dùng hash base62 rải đều
   (cloud-base Bài 9). (b) CACHE: "served faster for future requests" (WA tr.755);
   mapping gần bất biến → hit cao, ít invalidation; eventual read đủ.

LAB  DynamoDB thật: create-table (code HASH) → put → get-by-key → url;
   ADD hits atomic → không race (cloud-base Bài 2).

6 TRỤ  reliability/performance/cost; security (enumeration + spam tạo
   link) → nút thắt còn lại = RATE LIMITING (Bài 2).
```

## Nguồn

- **AWS Well-Architected Framework** — Performance Efficiency: yếu tố chọn data store theo access pattern (tr. 736), định nghĩa cache (tr. 755). `tai_lieu/AWS-Well-Architected-Framework.pdf` (offset +5).
- Nền: [cloud-base Bài 9 (sharding/hot partition)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 6 (cache/latency)](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md), [Bài 8 (eventual read)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md), [Bài 2 (atomic)](../../cloud-base/bai_hoc/bai_02_os-concurrency.md).
- Dịch vụ: [aws-fund Bài 3 — DynamoDB](../../aws-fund/bai_hoc/bai_03_database-storage.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · **[Bài 1 — URL shortener] ← bạn đang ở đây** · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
