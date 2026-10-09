# Bài 2 — Thiết kế rate limiter và load shedding

> [!info] Về bài này
> **Archetype 2 — bảo vệ hệ khỏi quá tải.** Nút thắt còn lại của Bài 1 (ai đó spam API) dẫn tới đây: **giới hạn tần suất (rate limiting)** và người anh em của nó — **load shedding** (chủ động từ chối tải thừa). Insight phản trực giác cốt lõi: khi quá tải, nhận *thêm* việc làm hệ **chậm đi**, không nhanh hơn — nên từ chối bớt lại *cứu* được phần còn lại.
> Nguồn: **BL** *Using load shedding to avoid overload*. Nền: [cloud-base Bài 1 (context switch/time-sharing)](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md), [Bài 2 (atomic)](../../cloud-base/bai_hoc/bai_02_os-concurrency.md); pattern: [release-it](../../release-it/README.md); dịch vụ: [aws-fund Bài 5 (API Gateway)](../../aws-fund/bai_hoc/bai_05_networking.md).
> **Lab:** rate limiter atomic trên DynamoDB (LocalStack).
> Nên đọc trước: [Bài 1 — URL shortener](bai_01_url-shortener.md).

## Mục lục

1. [Tình huống: user42 làm nghẽn API](#1-tình-huống-user42-làm-nghẽn-api)
2. [Cách ngây thơ: đếm trong RAM mỗi server](#2-cách-ngây-thơ-đếm-trong-ram-mỗi-server)
3. [Giải pháp: đếm chia sẻ, tăng atomic](#3-giải-pháp-đếm-chia-sẻ-tăng-atomic)
4. [Vì sao từ chối tốt hơn cố phục vụ: goodput](#4-vì-sao-từ-chối-tốt-hơn-cố-phục-vụ-goodput)
5. [Token bucket: cái xô cho phép burst](#5-token-bucket-cái-xô-cho-phép-burst)
6. [Lab: rate limiter atomic trên DynamoDB](#6-lab-rate-limiter-atomic-trên-dynamodb)
7. [Soi Well-Architected](#7-soi-well-architected)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Tình huống: user42 làm nghẽn API

> [!example] 2 giờ sáng, điện thoại bạn réo
> API của bạn phục vụ 10.000 khách hàng êm ả. Rồi một khách — `user42`, một script viết lỗi (hoặc một kẻ xấu) — bắt đầu gọi API **10.000 lần mỗi giây**. Server của bạn vốn kham được ~5.000 req/s cho *toàn bộ* khách. Giờ một mình `user42` ngốn sạch. Dashboard đỏ rực, 9.999 khách còn lại nhận lỗi, điện thoại bạn réo lúc 2 giờ sáng.

Vấn đề không phải "server yếu" — mà là **một khách lấn át tất cả**. Bạn cần một cái van: *mỗi khách tối đa N request mỗi phút; vượt thì trả **429 Too Many Requests** và kệ họ*. Nghe đơn giản. Nhưng làm đúng ở quy mô có hai cái bẫy, và ta sẽ vấp cái bẫy thứ nhất ngay ở cách làm hiển nhiên nhất (mục 2).

Yêu cầu cho cái van này: quyết định **nhanh** (nó nằm trên đường mọi request đi qua), **đúng** kể cả khi bạn có nhiều server, và bản thân nó **không được là điểm nghẽn** mới.

## 2. Cách ngây thơ: đếm trong RAM mỗi server

Cách đầu tiên ai cũng nghĩ ra: *trong mỗi server, giữ một bộ đếm `Map<user, số-request>`; mỗi request tăng đếm; vượt 100 thì trả 429.* Gọn, nhanh, không cần gì thêm. Và nó **sai** — theo hai cách.

**Bẫy 1 — nhiều server, mỗi cái đếm riêng.** Thực tế bạn không chạy một server mà, giả sử, **50 server** sau một load balancer. Request của `user42` được rải *ngẫu nhiên* ra 50 server đó. Mỗi server thấy riêng phần của mình và cho tới 100 — nên tổng cộng `user42` được:

```
50 server × 100 req/server = 5.000 req/phút   ← gấp 50 lần giới hạn ta ĐỊNH đặt!
```

Giới hạn "100/phút" trên giấy biến thành "5.000/phút" trên thực tế. Bộ đếm phải là **một chỗ dùng chung** (shared), không phải 50 bản rời.

**Bẫy 2 — đếm sai dưới tải đồng thời.** Kể cả nếu chỉ một server: hai request của `user42` tới *cùng lúc*, cả hai đọc đếm = 99, cả hai thấy "99 < 100, cho qua", cả hai ghi 100. Hai request lọt nhưng đếm chỉ tăng 1 → lâu dài đếm *tụt lại* so với thực, giới hạn rò rỉ. Đây đúng là **race condition** của [cloud-base Bài 2](../../cloud-base/bai_hoc/bai_02_os-concurrency.md): bước "đọc rồi ghi" có khe hở. Việc tăng đếm phải **atomic** — kiểm-tra-và-tăng trong một thao tác không thể chia cắt.

Hai bẫy này dẫn thẳng tới hai yêu cầu của giải pháp đúng: **bộ đếm chia sẻ** + **tăng atomic**.

## 3. Giải pháp: đếm chia sẻ, tăng atomic

Đặt bộ đếm ở **một store trung tâm nhanh** (DynamoDB), khoá theo `client#cửa-sổ-thời-gian`. Mọi server chung một bộ đếm (hết bẫy 1). Và dùng **conditional atomic update** của DynamoDB: tăng đếm *chỉ khi* còn dưới giới hạn, cả kiểm-tra lẫn tăng trong một thao tác phía server (hết bẫy 2).

Chặn theo **hai tầng** — thô ở rìa, tinh ở ứng dụng. Theo chân một request cụ thể để thấy rõ:

```
  user42 gửi request — đang là request thứ 101 của phút này
    │
    ▼  [Tầng 1 — API Gateway usage plan]  chặn THÔ: toàn API vượt X req/s chưa?
    │      chưa vượt trần thô → cho đi tiếp        (nếu vượt → 429 ngay, rẻ)
    │
    ▼  [Tầng 2 — Lambda → DynamoDB]  đếm TINH theo client:
    │      key = "user42#2026-10-07T17:30"
    │      SET c = c + 1   IF c < 100
    │         c đang = 100  →  điều kiện (100 < 100) SAI
    │         →  ConditionalCheckFailed  (DynamoDB từ chối ghi)
    │
    ▼  Lambda bắt lỗi đó  →  trả về  429 Too Many Requests
```

Lần theo con số: request #1 tới #100 trong phút này đều ghi được (`c` lên dần 1→100). Request **#101**: điều kiện `c < 100` là `100 < 100` → **sai** → DynamoDB *từ chối* ghi → Lambda trả 429. Sang phút mới, khoá đổi thành `...T17:31`, `c` bắt đầu lại từ 0 — cửa sổ tự reset.

Hai tầng chia việc: tầng rìa (API Gateway) chặn *lũ thô* cực rẻ, càng gần client càng tốt (đỡ cho downstream); tầng ứng dụng đếm *chính xác theo từng client*. Vì sao "từ chối thẳng" (429) lại là hành vi *đúng*, chứ không phải "cố phục vụ hết"? Mục 4.

## 4. Vì sao từ chối tốt hơn cố phục vụ: goodput

Trực giác bảo "khách đã tới thì cố phục vụ cho hết". Với hệ máy tính, trực giác đó **sai** — và một ẩn dụ cho thấy vì sao:

> [!example] Quán phở 20 bàn
> Quán bạn có 20 bàn, phục vụ ngon 20 khách cùng lúc. Giờ cao điểm 200 người ùa vào, chen nhau đứng cả lối đi. Bếp rối loạn, bồi bàn không chen qua được, **không ai** được ăn tử tế — kể cả 20 người lẽ ra phục vụ được. Nếu quán **treo biển "hết chỗ"** với 180 người (họ đi quán khác) và phục vụ ngon 20 người, tổng số khách *được ăn* cao hơn hẳn. Từ chối bớt = cứu phần còn lại.

Máy tính y hệt cái quán. Khi quá tải, nhận thêm việc không làm xong nhanh hơn — nó làm *chậm tất cả*:

> [!quote] BL: using-load-shedding-to-avoid-overload
> "Unfortunately, not only is throughput bounded by a system's resources, throughput typically degrades when the system is overloaded."
>
> *Đáng tiếc, throughput không chỉ bị chặn bởi tài nguyên — nó **thường suy giảm khi hệ quá tải**.*

Vì sao *suy giảm* (chứ không chỉ chạm trần)? Lý do rất quen từ nền OS — chính là "bồi bàn không chen qua được":

> [!quote] BL: using-load-shedding-to-avoid-overload
> "Computers take on work even when they're overloaded, but they spend increasing amounts of their time context switching and become too slow to be useful."
>
> *Máy tính vẫn **nhận việc kể cả khi quá tải**, nhưng tiêu ngày càng nhiều thời gian cho **context switch** và trở nên **quá chậm để còn hữu ích**.*

Nhận quá nhiều "process" thì việc juggling (chuyển qua lại) nuốt hết CPU — đúng [cloud-base Bài 1](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md). Nên thước đo đúng không phải "nhận bao nhiêu" (throughput) mà "phục vụ *tốt* được bao nhiêu" (**goodput** = số khách *được ăn ngon*):

> [!quote] BL: using-load-shedding-to-avoid-overload
> "Throughput is the total number of requests per second that is being sent to the server. Goodput is the subset of the throughput that is handled without errors and with low enough latency for the client to make use of the response."
>
> ***Throughput** là tổng số request/giây gửi tới server. **Goodput** là phần con được xử lý **không lỗi và đủ nhanh** để client dùng được kết quả.*

Bằng số: nhận 100% rồi làm chậm *tất cả* → goodput ≈ 0 (như quán 200 khách). Nhận 70%, từ chối 30% → goodput = 70%. **Load shedding** = chủ động vứt tải thừa để bảo vệ goodput. Rate limiter chính là load shedding *có chủ đích theo client* — nó chọn *ai* bị từ chối (`user42` tham lam) thay vì để hệ sập ngẫu nhiên cho mọi người.

## 5. Token bucket: cái xô cho phép burst

Còn một câu hỏi: giới hạn "100/phút" có nghĩa "đúng mỗi 0,6 giây một request" không? Cứng vậy thì khó chịu — người dùng thật hay gửi *một cụm* (mở app, tải 20 thứ một lúc) rồi im. Thuật toán kinh điển giải quyết đúng điều này là **token bucket**:

> [!example] Cái xô vé
> Hình dung một cái **xô chứa tối đa 100 cái vé**. Mỗi phút có người đổ thêm vé vào cho đầy lại. Mỗi request lấy ra **một vé**; hết vé thì phải chờ (429). Nếu bạn im một lúc, vé *tích đầy xô* → bạn được phép **gửi một cụm 100 request liền** (burst). Nhưng *trung bình* vẫn không vượt tốc độ đổ vé. Vừa cho burst tự nhiên, vừa chặn lạm dụng kéo dài.

API Gateway usage plan chính là một token bucket với hai núm: **rate** (tốc độ đổ vé lại) và **burst** (kích cỡ xô). Đây là tầng 1 trong sơ đồ mục 3 — nó dùng token bucket để chặn thô; tầng 2 (DynamoDB) đếm chính xác theo client.

## 6. Lab: rate limiter atomic trên DynamoDB

Giới hạn 3 request/cửa sổ cho `user42` bằng **conditional atomic update**: tăng đếm chỉ khi `c < 3`; vượt → `ConditionalCheckFailed` → 429. Chạy thật trên LocalStack:

```bash
awslocal dynamodb create-table --table-name RateLimit \
  --attribute-definitions AttributeName=key,AttributeType=S \
  --key-schema AttributeName=key,KeyType=HASH --billing-mode PAY_PER_REQUEST

# mỗi request: tăng đếm NẾU còn dưới giới hạn (atomic, phía server)
for i in 1 2 3 4 5; do
  c=$(awslocal dynamodb update-item --table-name RateLimit --key '{"key":{"S":"user42#win1"}}' \
      --update-expression 'SET c = if_not_exists(c, :z) + :one' \
      --condition-expression 'attribute_not_exists(c) OR c < :lim' \
      --expression-attribute-values '{":z":{"N":"0"},":one":{"N":"1"},":lim":{"N":"3"}}' \
      --return-values UPDATED_NEW --query 'Attributes.c.N' --output text 2>/dev/null)
  if [ -n "$c" ]; then echo "request $i → 200 OK   (đã dùng $c/3)"; else echo "request $i → 429 Too Many Requests (load shed)"; fi
done
awslocal dynamodb delete-table --table-name RateLimit
```

Kết quả chạy thật *(tất định)*:

```
request 1 → 200 OK   (đã dùng 1/3)
request 2 → 200 OK   (đã dùng 2/3)
request 3 → 200 OK   (đã dùng 3/3)
request 4 → 429 Too Many Requests (load shed)
request 5 → 429 Too Many Requests (load shed)
```

Đây là phiên bản thu nhỏ của sơ đồ mục 3 (giới hạn 3 thay vì 100). Mấu chốt: cả *kiểm tra* (`c < 3`) và *tăng* (`SET c = c+1`) nằm trong **một** thao tác atomic phía server. Nhớ bẫy 2 ở mục 2 — nếu tách thành "đọc đếm → nếu nhỏ hơn giới hạn thì ghi+1" (hai bước), hai request đồng thời cùng đọc 2 rồi cùng ghi 3 → lọt một request lố. `condition-expression` + `SET` gộp hai bước thành một "all or nothing", nên giới hạn *chính xác* ngay cả dưới tải đồng thời. Khoá `user42#win1` đổi theo cửa sổ thời gian thật (vd `user42#2026-10-07T17:30`) để tự reset mỗi phút.

> [!note] Tự thử
> 1. Bỏ `condition-expression`, chuyển thành đọc-rồi-ghi hai bước, chạy nhiều tiến trình song song: thấy lọt request lố (đúng bẫy 2). Vì sao atomic conditional chữa được? (cloud-base Bài 2)
> 2. Đổi khoá `#win1 → #win2`: cửa sổ mới, đếm reset về 0. Vì sao nên nhúng timestamp cửa sổ vào khoá?
> 3. Thêm TTL cho item (DynamoDB TTL) để tự xoá cửa sổ cũ: vì sao quan trọng cho chi phí? (aws-fund Bài 10 retention)

## 7. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | bảo vệ goodput khi quá tải; chống 1 client hại cả hệ | load shed chủ động, không để sập |
| Performance | atomic 1 thao tác; throttle thô ở rìa rẻ | bộ đếm không được thành nghẽn (DynamoDB scale) |
| Cost | TTL xoá cửa sổ cũ; chặn sớm tiết kiệm downstream | 429 rẻ hơn xử lý rồi hỏng |
| Security | chống brute-force/abuse theo client | kết hợp WAF cho tầng IP |
| Operational | theo dõi tỉ lệ 429 (quá nhiều = giới hạn sai/bị tấn công) | alarm trên 429 (aws-fund Bài 7) |

Nguyên tắc đọng lại: **từ chối sớm và rẻ** bảo vệ goodput. Nhưng rate-limit chỉ bảo vệ *điểm vào*; khi tải thật vẫn phải xử lý một khối lớn không đồng bộ → cần hàng đợi và fan-out (Bài 3–4).

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 2.1 — Vì sao đếm trong RAM mỗi server là sai? (hai bẫy)
> **Đáp:** (1) 50 server đếm riêng → client lách được 50×giới-hạn → phải bộ đếm **chia sẻ**. (2) hai request đồng thời cùng đọc-rồi-ghi → lọt request lố (race) → phải tăng **atomic**.

> [!question] Thẻ 2.2 — Hai tầng throttle lo gì khác nhau?
> **Đáp:** tầng rìa (API Gateway usage plan) chặn **lũ thô** cực rẻ, gần client. Tầng ứng dụng (DynamoDB) đếm **chính xác theo từng client**.

> [!question] Thẻ 2.3 — Vì sao quá tải làm hệ CHẬM đi? Nối về nền nào?
> **Đáp:** nhận việc vẫn nhận nhưng tốn ngày càng nhiều cho **context switch** → quá chậm để hữu ích. Như quán phở 200 khách; = juggling CPU của cloud-base Bài 1.

> [!question] Thẻ 2.4 — Goodput khác throughput? Vì sao load shed *tăng* goodput?
> **Đáp:** throughput = tổng req/s gửi tới; goodput = phần xử lý *không lỗi + đủ nhanh* (số khách *được ăn ngon*). Nhận 100% rồi chậm hết → goodput≈0; vứt tải thừa → phục vụ phần còn lại tốt.

> [!question] Thẻ 2.5 — Token bucket cho phép gì mà "giới hạn cứng mỗi giây" không?
> **Đáp:** **burst** — im một lúc thì vé tích đầy xô, được gửi một cụm; nhưng *trung bình* vẫn trong giới hạn. API Gateway usage plan = rate (đổ vé) + burst (cỡ xô).

> [!question] Thẻ 2.6 — Vì sao gộp "kiểm tra + tăng" vào conditional update, không tách hai bước?
> **Đáp:** hai bước (đọc rồi ghi) có khe race → lọt request lố (bẫy 2). Conditional atomic = một "all or nothing" → giới hạn chính xác dưới tải đồng thời.

## 9. Câu hỏi tự kiểm tra

1. Kể lại tình huống `user42`. Vì sao "server yếu" không phải vấn đề thật? *(mục 1)*
2. Hai bẫy của "đếm trong RAM mỗi server" là gì? Mỗi bẫy dẫn tới yêu cầu nào? *(mục 2)*
3. Lần theo request #101 trong sơ đồ mục 3: nó bị 429 ở đâu, vì điều kiện nào sai? *(mục 3)*
4. Giải thích "throughput suy giảm khi quá tải" bằng ẩn dụ quán phở + context switch. *(mục 4, BL + cloud-base Bài 1)*
5. Goodput vs throughput. Vì sao từ chối sớm *tăng* goodput? *(mục 4, BL)*
6. Token bucket cho burst ra sao? Chạy lab §6: vì sao conditional update chính xác còn đọc-rồi-ghi thì race? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 2 — RATE LIMITER & LOAD SHEDDING
─────────────────────────────────────────────────────────
TÌNH HUỐNG  user42 gọi 10k req/s làm nghẽn API → 1 khách lấn át 9.999 khách.
   Cần cái van: mỗi khách tối đa N/phút, vượt → 429.

CÁCH NGÂY THƠ (đếm RAM mỗi server) SAI 2 cách:
   (1) 50 server đếm riêng → client lách 50×N → cần bộ đếm CHIA SẺ.
   (2) đọc-rồi-ghi đồng thời → lọt request lố (race) → cần tăng ATOMIC.

GIẢI PHÁP  DynamoDB (shared) + conditional atomic: SET c=c+1 IF c<N.
   2 tầng: API Gateway (thô ở rìa) + DynamoDB (tinh theo client).
   request #101: c=100, điều kiện 100<100 SAI → ConditionalCheckFailed → 429.

VÌ SAO TỪ CHỐI  quán phở 200 khách → KHÔNG AI ăn ngon (goodput≈0). Quá tải
   → context switch nuốt CPU (cloud-base Bài 1), throughput SUY GIẢM (BL).
   Thước đo đúng = GOODPUT (xử lý tốt), không phải throughput. Load shed = vứt
   tải thừa để bảo vệ goodput.

TOKEN BUCKET  xô 100 vé, đổ đầy lại mỗi phút; request lấy 1 vé. Im lúc → vé
   tích → cho BURST; trung bình vẫn trong giới hạn. = API GW usage plan.

LAB  limit 3: request 1-3 OK, 4-5 = 429. Kiểm-tra+tăng trong 1 thao tác atomic.
```

## Nguồn

- **Amazon Builders' Library** — *Using load shedding to avoid overload*: throughput suy giảm khi quá tải, context switch, goodput vs throughput. `tai_lieu/bl_using-load-shedding-to-avoid-overload.txt`.
- Nền: [cloud-base Bài 1 (context switch)](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md), [Bài 2 (atomic/race)](../../cloud-base/bai_hoc/bai_02_os-concurrency.md); pattern chung: [release-it](../../release-it/README.md).
- Dịch vụ: [aws-fund Bài 5 — API Gateway](../../aws-fund/bai_hoc/bai_05_networking.md), [Bài 7 — alarm trên 429](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · **[Bài 2 — Rate limiter & load shedding] ← bạn đang ở đây** · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
