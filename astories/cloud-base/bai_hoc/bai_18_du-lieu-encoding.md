# Bài 18 — Dữ liệu nâng cao: Encoding và schema evolution

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 4 (Dữ liệu) — bài cuối của nhóm nâng cao.** [Bài 11](bai_11_du-lieu-batch-stream.md) nói event là "đối tượng bất biến"; nhưng *định dạng* của event thì **đổi theo thời gian** khi code tiến hoá. Bài này nắm cách dữ liệu được **encode** thành byte và — quan trọng hơn — làm sao **đổi schema mà không làm sập** những bên đang chạy phiên bản cũ. Đây là nền của **versioning API/event, EventBridge/Glue Schema Registry, và vì sao một breaking change âm thầm làm hỏng consumer** ở `aws-fund`.
> Nguồn: **DDIA** — ch. 4 (Encoding and Evolution).
> **Trích:** `DDIA (tr. X)` = trang **in**; **offset PDF = tr. + 22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 11 — batch & stream](bai_11_du-lieu-batch-stream.md), [Bài 4 — HTTP](bai_04_mang-http-dns.md).

## Mục lục

1. [Encoding: từ bộ nhớ ra byte](#1-encoding-từ-bộ-nhớ-ra-byte)
2. [Rolling upgrade: cũ và mới sống chung](#2-rolling-upgrade-cũ-và-mới-sống-chung)
3. [Backward và forward compatibility](#3-backward-và-forward-compatibility)
4. [Demo: thêm field an toàn, đổi tên thì gãy](#4-demo-thêm-field-an-toàn-đổi-tên-thì-gãy)
5. [Bảng so sánh: JSON vs Avro vs Protobuf](#5-bảng-so-sánh-json-vs-avro-vs-protobuf)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Encoding: từ bộ nhớ ra byte

Dữ liệu trong RAM là con trỏ, object, mảng — gắn với tiến trình đang chạy. Để *gửi qua mạng* (Bài 4–5) hay *lưu xuống đĩa* (Bài 3), phải dịch nó thành một chuỗi byte:

> [!quote] DDIA (tr. 113)
> "The translation from the in-memory representation to a byte sequence is called encoding (also known as serialization or marshalling), and the reverse is called decoding (parsing, deserialization, unmarshalling)."
>
> *Việc dịch từ **biểu diễn trong bộ nhớ** sang một **chuỗi byte** gọi là **encoding** (cũng gọi là serialization, marshalling); chiều ngược lại gọi là **decoding** (parsing, deserialization, unmarshalling).*

Mọi request HTTP (Bài 4), mọi message SQS (Bài 7), mọi event stream (Bài 11), mọi dòng ghi xuống đĩa (Bài 3) đều qua bước encode/decode này. Định dạng phổ biến: **JSON** (text, người đọc được, phổ cập) và các dạng nhị phân nhỏ-gọn-nhanh như **Protocol Buffers, Avro, Thrift**. Nhưng câu hỏi khó nhất của encoding không phải "định dạng nào" — mà là *điều gì xảy ra khi schema đổi*.

## 2. Rolling upgrade: cũ và mới sống chung

Phần mềm sống thì tiến hoá — thêm field, đổi cấu trúc. Nhưng bạn *không* nâng cấp mọi máy cùng một giây:

> [!quote] DDIA (tr. 112)
> "This means that old and new versions of the code, and old and new data formats, may potentially all coexist in the system at the same time. In order for the system to continue running smoothly, we need to maintain compatibility in both directions."
>
> *Điều này nghĩa là **code cũ và mới, định dạng dữ liệu cũ và mới, có thể cùng tồn tại trong hệ thống cùng lúc**. Để hệ tiếp tục chạy trơn tru, ta cần **giữ tương thích theo cả hai chiều**.*

Vì sao "cùng lúc"? Vì **rolling upgrade** (triển khai cuốn chiếu): deploy bản mới lên vài node một, trong khi các node khác còn chạy bản cũ — để không gián đoạn dịch vụ. Trong khoảnh khắc đó (có thể kéo dài nhiều phút tới nhiều giờ), một message do node *mới* ghi có thể bị node *cũ* đọc, và ngược lại. Nếu định dạng không tương thích hai chiều, bạn vừa deploy vừa làm sập chính mình. Đây là lý do "đổi schema" là một trong những thao tác dễ gây sự cố production nhất.

## 3. Backward và forward compatibility

Hai chiều tương thích, hai cái tên — và forward khó hơn nhiều:

> [!quote] DDIA (tr. 112)
> "Backward compatibility: Newer code can read data that was written by older code. Forward compatibility: Older code can read data that was written by newer code."
>
> ***Backward compatibility (tương thích ngược):** code **mới** đọc được dữ liệu do code **cũ** ghi. **Forward compatibility (tương thích xuôi):** code **cũ** đọc được dữ liệu do code **mới** ghi.*

Mẹo nhớ: *backward* = nhìn về quá khứ (mới đọc cũ) — dễ, vì khi viết code mới bạn *biết* định dạng cũ. *Forward* = nhìn về tương lai (cũ đọc mới) — khó, vì code cũ phải *bỏ qua một cách duyên dáng* những thứ nó chưa từng biết (field mới mà phiên bản tương lai thêm vào). Quy tắc thực chiến rút ra: **thêm field tuỳ chọn là an toàn cả hai chiều; đổi tên/xoá field bắt buộc, hoặc đổi kiểu, là breaking.** Demo mục 4 cho thấy ranh giới đó bằng tay.

## 4. Demo: thêm field an toàn, đổi tên thì gãy

v1 có `{name, email}`; v2 *thêm* `phone` (tuỳ chọn). Kiểm cả hai chiều. Rồi v3 *đổi tên* `email → contactEmail` (breaking) và xem code v1 gãy ra sao.

```typescript
// Encoding = dịch dữ liệu trong-bộ-nhớ ↔ chuỗi byte (DDIA tr.113). Khi deploy
// cuốn chiếu (rolling upgrade), code CŨ và MỚI chạy song song → cần tương thích
// HAI CHIỀU (tr.112): backward (code mới đọc dữ liệu cũ), forward (code cũ đọc
// dữ liệu mới). Thêm field tuỳ chọn = an toàn; đổi tên/bỏ field bắt buộc = gãy.
type V1 = { name: string; email: string };
type V2 = { name: string; email: string; phone?: string };  // v2 THÊM field tuỳ chọn

const encode = (o: object) => JSON.stringify(o);
const decode = (s: string) => JSON.parse(s);

// reader v1 chỉ cần name+email; reader v2 đọc cả phone nếu có
const readV1 = (s: string): string => { const o = decode(s); return `${o.name} <${o.email}>`; };
const readV2 = (s: string): string => { const o = decode(s); return `${o.name} <${o.email}>${o.phone ? ""+o.phone : ""}`; };

const dataV1 = encode({ name: "Alice", email: "a@x.io" } satisfies V1);
const dataV2 = encode({ name: "Alice", email: "a@x.io", phone: "123" } satisfies V2);

console.log("THÊM field tuỳ chọn 'phone' (v1 → v2):");
console.log(`  backward: code v2 đọc dữ liệu v1 → ${readV2(dataV1)}   (thiếu phone, vẫn OK)`);
console.log(`  forward : code v1 đọc dữ liệu v2 → ${readV1(dataV2)}   (bỏ qua phone, vẫn OK)`);

// --- BREAKING: v3 ĐỔI TÊN email → contactEmail ---
const dataV3 = encode({ name: "Alice", contactEmail: "a@x.io" });
console.log("\nĐỔI TÊN field email → contactEmail (breaking):");
console.log(`  code v1 (đòi 'email') đọc dữ liệu v3 → ${readV1(dataV3)}   ← GÃY: email mất!`);
console.log("\nThêm field tuỳ chọn: tương thích 2 chiều. Đổi tên/bỏ field bắt buộc,");
console.log("đổi kiểu: phá vỡ — vì sao API/event cần versioning & schema registry.");
```

Kết quả chạy thật *(tất định)*:

```
THÊM field tuỳ chọn 'phone' (v1 → v2):
  backward: code v2 đọc dữ liệu v1 → Alice <a@x.io>   (thiếu phone, vẫn OK)
  forward : code v1 đọc dữ liệu v2 → Alice <a@x.io>   (bỏ qua phone, vẫn OK)

ĐỔI TÊN field email → contactEmail (breaking):
  code v1 (đòi 'email') đọc dữ liệu v3 → Alice <undefined>   ← GÃY: email mất!

Thêm field tuỳ chọn: tương thích 2 chiều. Đổi tên/bỏ field bắt buộc,
đổi kiểu: phá vỡ — vì sao API/event cần versioning & schema registry.
```

Thêm `phone` tuỳ chọn an toàn cả hai chiều: code v2 đọc dữ liệu v1 thấy thiếu phone nhưng vẫn chạy (backward); code v1 đọc dữ liệu v2 *bỏ qua* phone nó không biết (forward). Nhưng đổi tên `email → contactEmail` làm code v1 đọc ra `undefined` — một lỗi **âm thầm**: không exception, chỉ là email biến mất khỏi mọi bản ghi v3 mà v1 xử lý (gợi nhớ "silently dropped" của Bài 15). Đây là vì sao kỷ luật schema quan trọng: **thay đổi phải cộng dồn (thêm tuỳ chọn), không phá vỡ (đổi tên/xoá)** — và nếu buộc phải breaking, thì phải *versioning* (một endpoint/topic mới) để cũ-mới không gặp nhau.

> [!note] Tự thử
> - Làm `phone` thành *bắt buộc* ở v2 rồi để v2 đọc dữ liệu v1 (thiếu phone): nếu code v2 *giả định* phone luôn có (vd `o.phone.length`) → nổ. Thêm field *bắt buộc* phá backward compat.
> - Đổi *kiểu* `email` từ string sang mảng `["a@x.io"]`: code v1 nối chuỗi ra kết quả lạ — đổi kiểu cũng là breaking dù tên giữ nguyên.
> - Mô phỏng Avro: tách *schema* ra khỏi *dữ liệu* (gửi riêng schema id), reader tra schema để đọc — thấy vì sao schema registry cho phép tiến hoá kỷ luật hơn JSON tự do.

## 5. Bảng so sánh: JSON vs Avro vs Protobuf

| Tiêu chí              | JSON (text)                  | Protocol Buffers / Thrift     | Avro                              |
| :-------------------- | :--------------------------- | :---------------------------- | :-------------------------------- |
| Kích thước / tốc độ   | lớn, chậm hơn                | nhỏ gọn, nhanh (nhị phân)     | nhỏ gọn, nhanh                    |
| Người đọc được        | **có** (debug dễ)            | không                         | không                             |
| Schema                | ngầm (không bắt buộc)        | tag số cho mỗi field          | schema tách rời, so writer↔reader |
| Tiến hoá              | tuỳ kỷ luật tay              | thêm field mới = tag mới      | **thiết kế cho evolution**        |
| Nền / AWS             | API/event mặc định, EventBridge | gRPC nội bộ                | Kinesis/MSK + Glue Schema Registry |

Quy luật: **JSON cho ranh giới công khai/debug (dễ, phổ cập); nhị phân có schema (Avro/Protobuf) cho luồng nội bộ khối lượng lớn (nhỏ, nhanh, tiến hoá kỷ luật).** Dù định dạng nào, *luật tương thích hai chiều* ở mục 3 vẫn đúng — Avro chỉ *ép* bạn tuân thủ bằng cách kiểm schema writer↔reader, còn JSON để bạn tự do (và tự chịu trách nhiệm). Đây là tầng cuối của trụ Dữ liệu: dữ liệu không chỉ được *lưu* (Bài 10) và *xử lý* (Bài 11) mà còn phải *tiến hoá* an toàn theo thời gian.

## 6. Nối về AWS

> [!note] Nối về AWS
> "Đổi schema mà không làm sập consumer" là bài toán vận hành hằng ngày trên AWS — xem [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md):
> - **EventBridge Schema Registry & Glue Schema Registry** = hiện thực của mục 5: đăng ký schema cho event/stream, *kiểm tra tương thích* khi publisher đổi schema — chặn breaking change trước khi nó xuống consumer. Đây là "ép kỷ luật Avro" của bảng mục 5 ở dạng managed.
> - **Rolling upgrade của Lambda/ECS = kịch bản mục 2.** Khi bạn deploy hàm/dịch vụ mới, bản cũ và mới *cùng xử lý* message trong hàng đợi một lúc — nên event schema phải tương thích hai chiều, nếu không message đang bay sẽ làm sập bản không khớp.
> - **Versioning API Gateway.** Breaking change (đổi tên/bỏ field bắt buộc — mục 3/demo) thì phải ra **version mới** (`/v2`) để client cũ không gãy — đúng "buộc breaking thì versioning" của mục 4.
> - **SQS/SNS message là contract.** Producer và consumer deploy độc lập (Bài 4 — ghép nối rời) nên *không bao giờ* đổi cùng lúc. Chỉ **thêm field tuỳ chọn**; muốn bỏ/đổi thì thêm mới + chuyển dần + mới xoá cũ — ba bước, không một bước.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 18.1 — Encoding/decoding là gì? Ở đâu trong hệ cần nó?
> **Đáp:** encode = dịch bộ nhớ → chuỗi byte (serialization); decode = ngược lại. Cần ở mọi ranh giới: gửi mạng (Bài 4), lưu đĩa (Bài 3), message/event (Bài 7, 11).

> [!question] Thẻ 18.2 — Vì sao code cũ và mới "cùng tồn tại một lúc"?
> **Đáp:** **rolling upgrade** (deploy cuốn chiếu) — vài node mới trong khi node khác còn cũ, để không gián đoạn. Trong khoảng đó, dữ liệu cũ/mới và code cũ/mới gặp nhau.

> [!question] Thẻ 18.3 — Backward vs forward compatibility? Cái nào khó hơn, vì sao?
> **Đáp:** backward = code mới đọc dữ liệu cũ (dễ, vì biết định dạng cũ); forward = code cũ đọc dữ liệu mới (khó, vì cũ phải *bỏ qua* field tương lai chưa biết).

> [!question] Thẻ 18.4 — Thay đổi schema nào an toàn, nào breaking?
> **Đáp:** an toàn (2 chiều): **thêm field tuỳ chọn**. Breaking: đổi tên / xoá field bắt buộc / đổi kiểu. Buộc breaking → phải versioning.

> [!question] Thẻ 18.5 — Trong demo, vì sao đổi tên email→contactEmail "gãy âm thầm"?
> **Đáp:** code v1 vẫn đọc field `email`, nay không có → `undefined`, không lỗi/exception. Email biến mất lặng lẽ khỏi mọi bản ghi v3 mà v1 xử lý.

> [!question] Thẻ 18.6 — Schema Registry (EventBridge/Glue) làm gì? SQS message nên đổi thế nào?
> **Đáp:** đăng ký schema + kiểm tương thích trước khi publish → chặn breaking. SQS/SNS: chỉ **thêm field tuỳ chọn**; bỏ/đổi thì thêm-mới → chuyển dần → mới xoá (ba bước).

## 8. Câu hỏi tự kiểm tra

1. Encoding/decoding là gì? Kể ba nơi trong hệ phải encode/decode. *(mục 1, tr. 113)*
2. Vì sao "old and new versions coexist"? Rolling upgrade là gì? *(mục 2, tr. 112)*
3. Định nghĩa backward và forward compatibility. Vì sao forward khó hơn? *(mục 3, tr. 112)*
4. Thay đổi schema nào an toàn, nào breaking? Buộc breaking thì làm gì? *(mục 3–4)*
5. Chạy demo mục 4. Vì sao thêm phone an toàn hai chiều mà đổi tên email gãy âm thầm? *(mục 4)*
6. Schema Registry giải quyết gì? Quy trình ba bước để bỏ một field khỏi SQS message? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 18 — DỮ LIỆU NÂNG CAO: ENCODING & SCHEMA EVOLUTION
─────────────────────────────────────────────────────────
ENCODING  dịch bộ nhớ ↔ chuỗi byte (serialization, DDIA tr.113). Ở MỌI ranh
   giới: mạng (Bài 4), đĩa (Bài 3), message/event (Bài 7,11).

ROLLING UPGRADE  deploy cuốn chiếu → code CŨ+MỚI, dữ liệu CŨ+MỚI cùng tồn
   tại một lúc (tr.112) → cần tương thích HAI CHIỀU.

BACKWARD  code mới đọc dữ liệu cũ (DỄ: biết định dạng cũ).
FORWARD   code cũ đọc dữ liệu mới (KHÓ: phải bỏ qua field tương lai). (tr.112)
   An toàn: THÊM field tuỳ chọn. Breaking: đổi tên/xoá bắt buộc/đổi kiểu.

DEMO  thêm phone tuỳ chọn: v2 đọc v1 OK (backward), v1 đọc v2 OK (forward).
   Đổi tên email→contactEmail: v1 đọc ra undefined → GÃY ÂM THẦM (như Bài 15).

ĐỊNH DẠNG  JSON (text, debug, công khai) vs Avro/Protobuf (nhị phân, nhỏ-nhanh,
   schema ép tiến hoá kỷ luật). Luật 2-chiều đúng với mọi định dạng.

NỐI VỀ AWS  EventBridge/Glue Schema Registry (kiểm tương thích); rolling
   upgrade Lambda/ECS (event phải 2 chiều); versioning API (/v2 khi breaking);
   SQS message là contract (thêm tuỳ chọn; bỏ field = quy trình 3 bước).
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 4 (Encoding and Evolution)**: rolling upgrade & tương thích hai chiều, backward/forward compatibility (tr. 112), định nghĩa encoding/decoding (tr. 113). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md) (Schema Registry, message contract).
- Mở rộng của [Bài 11 — batch & stream](bai_11_du-lieu-batch-stream.md) (event bất biến nhưng *định dạng* tiến hoá); gãy âm thầm nối [Bài 15 — đồng hồ](bai_15_dist-dong-ho.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · **[Bài 18 — Dữ liệu nâng cao: encoding & schema] ← bạn đang ở đây**

Xem thêm [README khoá học](../README.md).
