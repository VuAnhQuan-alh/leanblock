# Bài 5 — Thiết kế thanh toán idempotent

> [!info] Về bài này
> **Archetype 5 — khi "làm hai lần" là thảm hoạ.** Bài 4 giao at-least-once → một message có thể tới hai lần. Vô hại với "gửi email", nhưng *chết người* với "trừ tiền". Bài này giải bài toán **exactly-once *hiệu lực*** (dù giao nhiều lần) bằng **idempotency key** + ghi atomic — nền của mọi API thanh toán/đặt chỗ nghiêm túc.
> Nguồn: **BL** *Making retries safe with idempotent APIs*. Nền: [cloud-base Bài 7 (partial failure — demo trừ tiền 2 lần)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md), [Bài 16 (transaction/ACID)](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md), [Bài 2 (atomic)](../../cloud-base/bai_hoc/bai_02_os-concurrency.md); dịch vụ: [aws-fund Bài 3 (DynamoDB)](../../aws-fund/bai_hoc/bai_03_database-storage.md).
> **Lab:** idempotent payment bằng conditional write (LocalStack).
> Nên đọc trước: [Bài 4 — hệ thông báo](bai_04_he-thong-bao.md), [cloud-base Bài 7](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: idempotency key và ghi có điều kiện](#2-kiến-trúc-idempotency-key-và-ghi-có-điều-kiện)
3. [Đào sâu: idempotent API và token ACID](#3-đào-sâu-idempotent-api-và-token-acid)
4. [Lab: conditional write chống trừ tiền kép](#4-lab-conditional-write-chống-trừ-tiền-kép)
5. [Soi Well-Architected](#5-soi-well-architected)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] Khách bị trừ tiền hai lần
> Khách bấm "Thanh toán $100". App quay quay... rồi báo *"Lỗi mạng, thử lại"*. Khách bấm lại. Lần này thành công. Sáng hôm sau khách gọi tổng đài: **thẻ bị trừ $200**. Chuyện gì xảy ra? Lần đầu server *đã* trừ tiền xong, nhưng **hồi đáp bị mất trên đường về** (cloud-base Bài 7) — client tưởng thất bại nên gửi lại, server trừ lần hai. Cách làm ngây thơ ("nhận request thì cứ trừ") *bảo đảm* lỗi này dưới retry. Bài này làm cho "trừ tiền" **an toàn khi lặp**.

**Chức năng:** `POST /charge {amount}` trừ tiền tài khoản đúng **một lần**, kể cả khi client/SQS retry. **Phi chức năng:** không bao giờ trừ kép (tiền thật!), retry an toàn, chịu được client timeout rồi gửi lại.

Ràng buộc đến thẳng từ cloud-base Bài 7: khi client gửi `POST /charge` rồi *không nhận được hồi đáp*, nó **không biết** request đã xử lý chưa (ba khả năng: mất request / server chết / mất hồi đáp). Nó buộc phải retry — và nếu server xử lý *cả hai* lần, khách bị trừ `$200` thay vì `$100`. Đây chính là demo `$200 vs $100` của [cloud-base Bài 7](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md), giờ phải giải bằng cơ chế AWS cụ thể.

## 2. Kiến trúc: idempotency key và ghi có điều kiện

```
   client ─ gửi POST /charge + Idempotency-Key: pay-abc  (do CLIENT sinh, cố định qua các retry)
      ─▶ API GW ─▶ Lambda ─▶ DynamoDB.put({reqId: "pay-abc", ...})
                              condition: attribute_not_exists(reqId)
                                 ├─ thành công → đây là LẦN ĐẦU → trừ tiền
                                 └─ ConditionalCheckFailed → ĐÃ xử lý → trả kết quả cũ, KHÔNG trừ lại
```

Chìa khoá: **client sinh một khoá định danh duy nhất** cho *ý định* thanh toán (không phải mỗi lần gửi) và gắn vào mọi lần retry. Server dùng khoá đó làm *điểm chốt*: ghi bản ghi payment với điều kiện "khoá này chưa tồn tại". Lần đầu ghi được → xử lý; retry → điều kiện fail → nhận ra "đã làm rồi", trả lại kết quả cũ mà không trừ thêm. Mục 3 giải thích vì sao bước ghi-token và trừ-tiền phải *cùng* atomic.

## 3. Đào sâu: idempotent API và token ACID

> [!example] Ẩn dụ: vé giữ xe
> **Idempotency-Key** = tấm vé giữ xe có số in sẵn. Bạn đưa vé số `pay-abc`, bảo vệ *đánh dấu đã nhận xe này*. Đưa lại đúng vé `pay-abc` mười lần nữa, bảo vệ chỉ cười "xe anh nhận rồi" — không thu phí lần nữa. Nhưng nếu mỗi lần bạn *tự in vé mới* (`pay-1`, `pay-2`...), bảo vệ coi là mười lượt gửi khác nhau → thu mười lần. Mấu chốt: **số vé do client giữ cố định**, không đổi qua mỗi lần thử.

Mục tiêu có tên chính xác:

> [!quote] BL: making-retries-safe-with-idempotent-apis
> "An idempotent operation is one where a request can be retransmitted or retried with no additional side effects, a property that is very beneficial in distributed systems."
>
> *Một thao tác **idempotent** là thao tác mà một request có thể **gửi lại/retry mà không gây thêm tác dụng phụ** — một tính chất rất quý trong hệ phân tán.*

Làm sao đạt? Bằng một khoá do client cấp:

> [!quote] BL: making-retries-safe-with-idempotent-apis
> "A unique caller-provided client request identifier for idempotent operations meets this need."
>
> *Một **định danh request do bên gọi cấp, duy nhất** cho thao tác idempotent đáp ứng nhu cầu này* (chính là "Idempotency-Key").

Và đây là phần tinh tế nhất — ghi token và thực hiện thay đổi phải là **một** đơn vị atomic:

> [!quote] BL: making-retries-safe-with-idempotent-apis
> "the process that combines recording the idempotent token and all mutating operations related to servicing the request must meet the properties for an atomic, consistent, isolated, and durable (ACID) operation."
>
> *quá trình **gộp việc ghi token idempotent và mọi thao tác thay đổi** phục vụ request phải thoả tính chất **ACID** (atomic, consistent, isolated, durable).*

Vì sao ACID bắt buộc (cloud-base Bài 16): nếu ghi-token và trừ-tiền là *hai* bước rời, crash ở giữa để lại trạng thái hỏng — ghi token mà chưa trừ (mất tiền của nhà), hoặc trừ mà chưa ghi token (retry sẽ trừ lại). Gộp cả hai vào **một** thao tác atomic (DynamoDB conditional write một item, hoặc `TransactWriteItems` nhiều item) khép khe hở đó. Đây là "all or nothing" của cloud-base Bài 2/16, áp vào bài toán tiền thật.

## 4. Lab: conditional write chống trừ tiền kép

Client retry **cùng** `reqId` ba lần (do hồi đáp mất); conditional put đảm bảo chỉ trừ một lần. Chạy thật trên LocalStack:

```bash
awslocal dynamodb create-table --table-name Payments \
  --attribute-definitions AttributeName=reqId,AttributeType=S \
  --key-schema AttributeName=reqId,KeyType=HASH --billing-mode PAY_PER_REQUEST

charge() {   # idempotent: ghi bản ghi CHỈ khi reqId chưa tồn tại
  if awslocal dynamodb put-item --table-name Payments \
     --item "{\"reqId\":{\"S\":\"$1\"},\"amount\":{\"N\":\"100\"}}" \
     --condition-expression 'attribute_not_exists(reqId)' 2>/dev/null; then
    echo "   reqId=$1 → TÍNH TIỀN \$100 (lần đầu)"
  else
    echo "   reqId=$1 → đã xử lý rồi, BỎ QUA (không trừ lại)"
  fi
}
charge pay-abc; charge pay-abc; charge pay-abc        # retry cùng key 3 lần
awslocal dynamodb scan --table-name Payments --select COUNT --query 'Count' --output text
```

Kết quả chạy thật:

```
Client retry CÙNG reqId 'pay-abc' 3 lần (do hồi đáp mất — cloud-base Bài 7):
   reqId=pay-abc → TÍNH TIỀN $100 (lần đầu)
   reqId=pay-abc → đã xử lý rồi, BỎ QUA (không trừ lại)
   reqId=pay-abc → đã xử lý rồi, BỎ QUA (không trừ lại)
Tổng số lần thực trừ tiền:
1
```

Ba lần retry, **trừ đúng một lần** (count=1). `attribute_not_exists(reqId)` biến "ghi payment" thành thao tác idempotent: lần đầu ghi được (và chỉ lúc đó mới trừ tiền), các lần sau điều kiện fail → nhận ra trùng, bỏ qua. Mấu chốt: khoá `pay-abc` do *client* sinh và *giữ nguyên* qua mọi retry — nếu client sinh khoá mới mỗi lần (như demo "không idempotency" của cloud-base Bài 7), cơ chế này vô dụng. Trong thật, dùng `TransactWriteItems` để ghi token + cập nhật số dư trong một giao dịch ACID (mục 3).

> [!note] Tự thử
> 1. Đổi `charge pay-abc` lần hai thành `charge pay-xyz` (khoá khác): vì sao giờ nó trừ *thêm*? Minh hoạ "khoá phải do client giữ nguyên".
> 2. Tách thành hai bước (ghi token rồi update balance riêng) và "crash" giữa: liệt kê trạng thái hỏng. Vì sao cần ACID/TransactWriteItems? (cloud-base Bài 16)
> 3. So với rate limiter (Bài 2): cả hai dùng conditional write của DynamoDB — khác nhau ở *ý nghĩa* điều kiện thế nào?

## 5. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | exactly-once hiệu lực dù retry; không trừ kép | ghi token + mutate trong 1 ACID op |
| Performance | 1 conditional write, không khoá bi quan | DynamoDB conditional = optimistic |
| Cost | TransactWriteItems đắt gấp đôi WCU — chỉ dùng chỗ cần | token store nhỏ, TTL dọn key cũ |
| Security | chống replay (khoá dùng một lần) | xác thực người gọi (IAM/JWT) |
| Operational | idempotent → retry/replay an toàn khi vận hành | theo dõi tỉ lệ "trùng bị chặn" |

Nguyên tắc đọng lại: **ở biên giới "làm nhiều lần" của hệ phân tán, biến thao tác thành idempotent bằng khoá client + ghi atomic.** Đây là mảnh ghép cuối của bộ ba độ-tin-cậy: retry (Bài 4) an toàn *chỉ khi* idempotent (bài này). Tiếp theo: dữ liệu lớn (ảnh/video) không thể nhét qua API — cần đường upload riêng (Bài 6).

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — "Idempotent" nghĩa là gì? Vì sao quý trong hệ phân tán?
> **Đáp:** retry/gửi-lại **không gây thêm tác dụng phụ**. Quý vì at-least-once (Bài 4) + partial failure (cloud-base Bài 7) khiến request *sẽ* bị gửi nhiều lần.

> [!question] Thẻ 5.2 — Idempotency-Key là gì, ai sinh, khi nào đổi?
> **Đáp:** định danh **duy nhất do client cấp** cho một *ý định* thao tác; **giữ nguyên qua mọi retry**, chỉ đổi cho ý định mới. Server dùng nó làm điểm chốt khử trùng.

> [!question] Thẻ 5.3 — Vì sao ghi-token và trừ-tiền phải cùng ACID?
> **Đáp:** nếu hai bước rời, crash giữa → ghi token chưa trừ (mất tiền) hoặc trừ chưa ghi token (retry trừ lại). Gộp atomic (conditional write / TransactWriteItems) khép khe hở (cloud-base Bài 16).

> [!question] Thẻ 5.4 — `attribute_not_exists(reqId)` biến ghi thành idempotent ra sao?
> **Đáp:** lần đầu ghi được → xử lý; retry → điều kiện fail → nhận ra trùng, bỏ qua. Kiểm-tra + ghi trong một thao tác atomic.

> [!question] Thẻ 5.5 — Nếu client sinh khoá MỚI mỗi lần retry thì sao?
> **Đáp:** cơ chế vô dụng — server coi mỗi lần là thao tác mới → trừ kép (đúng demo "không idempotency" của cloud-base Bài 7).

## 7. Câu hỏi tự kiểm tra

1. Vì sao client *buộc* retry POST /charge? Hậu quả nếu server xử lý cả hai lần? *(mục 1, cloud-base Bài 7)*
2. Idempotency-Key do ai sinh, vòng đời thế nào? *(mục 2–3, BL)*
3. Vì sao ghi token + mutate phải ACID? Liệt kê trạng thái hỏng nếu tách rời. *(mục 3, cloud-base Bài 16)*
4. Chạy lab §4. Vì sao 3 retry chỉ trừ 1 lần? Điều gì xảy ra nếu đổi khoá mỗi lần? *(mục 4)*
5. So sánh conditional write ở đây và ở rate limiter (Bài 2). *(mục 4, Bài 2)*

## Tóm tắt một trang

```
BÀI 5 — THANH TOÁN IDEMPOTENT
─────────────────────────────────────────────────────────
VẤN ĐỀ  at-least-once (Bài 4) + partial failure (cloud-base Bài 7) → client
   retry POST /charge → trừ KÉP ($200 thay vì $100). Cần exactly-once HIỆU LỰC.

IDEMPOTENT  retry "không thêm tác dụng phụ" (BL). Đạt bằng IDEMPOTENCY-KEY —
   định danh DUY NHẤT do CLIENT sinh, giữ nguyên qua mọi retry.

ACID  ghi-token + trừ-tiền phải trong MỘT thao tác atomic (BL): conditional
   write 1 item hoặc TransactWriteItems. Tách rời → crash giữa = trạng thái hỏng
   (cloud-base Bài 16).

LAB  DynamoDB put IF attribute_not_exists(reqId): 3 retry cùng key → trừ 1 lần
   (count=1). Đổi key mỗi lần → trừ kép (vô hiệu cơ chế).

6 TRỤ  reliability (exactly-once hiệu lực); TransactWriteItems đắt 2x WCU →
   dùng đúng chỗ; TTL dọn key cũ. Retry (Bài 4) an toàn CHỈ KHI idempotent.
   Tiếp: dữ liệu lớn (ảnh) không qua API được → Bài 6.
```

## Nguồn

- **Amazon Builders' Library** — *Making retries safe with idempotent APIs*: định nghĩa idempotent, client request identifier, token + mutate phải ACID. `tai_lieu/bl_making-retries-safe-with-idempotent-apis.txt`.
- Nền: [cloud-base Bài 7 (partial failure, demo trừ kép)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md), [Bài 16 (transaction/ACID)](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md), [Bài 2 (atomic)](../../cloud-base/bai_hoc/bai_02_os-concurrency.md).
- Dịch vụ: [aws-fund Bài 3 — DynamoDB conditional write/Transactions](../../aws-fund/bai_hoc/bai_03_database-storage.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · **[Bài 5 — Thanh toán idempotent] ← bạn đang ở đây** · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
