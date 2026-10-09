# Bài 14 — Mạng nâng cao: Bảo mật và mật mã

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 2 (Mạng).** [Bài 5](bai_05_mang-tcp-tls.md) nói TLS "mã hoá + xác thực" nhưng chưa mở nắp *mã hoá là gì*. Bài này nắm bốn viên gạch nền: **bí mật/toàn vẹn/xác thực**, **mã đối xứng vs khoá công khai**, **chữ ký số**, **chứng chỉ & CA (PKI)**. Đây là nền để hiểu **IAM ký request (SigV4), S3 presigned URL, KMS, JWT, và chuỗi chứng chỉ TLS/ACM** ở `aws-fund` — những thứ bạn dùng hằng ngày mà hiếm khi thấy bên dưới.
> Nguồn: **Kurose & Ross** — ch. 8 (Security in Computer Networks).
> **Trích:** `Kurose (tr. X)` = trang **in**; **offset PDF = tr. + 28**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`; dùng `node:crypto` có sẵn).
> Nên đọc trước: [Bài 5 — TCP & TLS](bai_05_mang-tcp-tls.md).

## Mục lục

1. [Ba điều bảo mật muốn: bí mật, toàn vẹn, xác thực](#1-ba-điều-bảo-mật-muốn-bí-mật-toàn-vẹn-xác-thực)
2. [Đối xứng vs khoá công khai](#2-đối-xứng-vs-khoá-công-khai)
3. [Chữ ký số và chứng chỉ (PKI)](#3-chữ-ký-số-và-chứng-chỉ-pki)
4. [Demo: hash và chữ ký số bằng node crypto](#4-demo-hash-và-chữ-ký-số-bằng-node-crypto)
5. [Bảng so sánh: hash vs mã hoá vs chữ ký](#5-bảng-so-sánh-hash-vs-mã-hoá-vs-chữ-ký)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Ba điều bảo mật muốn: bí mật, toàn vẹn, xác thực

"Bảo mật" không phải một thứ mà là ba yêu cầu tách biệt — và nhầm lẫn chúng là nguồn của vô số lỗ hổng. **Bí mật (confidentiality)**: chỉ người nhận đọc được. **Toàn vẹn (integrity)**: thông điệp không bị sửa trên đường. **Xác thực (authentication)**: đúng là người gửi đó, không phải kẻ mạo danh. Kurose đặt hai cái sau cạnh nhau:

> [!quote] Kurose (tr. 624)
> "we turn to the equally important cryptography topic of providing message integrity (also known as message authentication). [...] To authenticate this message, Bob needs to verify: 1. The message indeed originated from Alice. 2. The message was not tampered with on its way to Bob."
>
> *ta chuyển sang chủ đề mật mã **quan trọng không kém là message integrity (cũng gọi là message authentication)**. [...] Để xác thực thông điệp, Bob cần kiểm: (1) thông điệp **thực sự đến từ Alice**, và (2) thông điệp **không bị sửa** trên đường tới Bob.*

Để ý: *mã hoá* (bí mật) và *toàn vẹn/xác thực* là hai việc **khác nhau**. Một thông điệp có thể được mã hoá mà vẫn bị sửa (kẻ gian đổi vài byte ciphertext); ngược lại một thông điệp công khai (plaintext) vẫn cần chứng minh không bị sửa và đúng người gửi. Phần lớn giao thức an toàn cần *cả ba*, và mỗi cái dùng một công cụ mật mã khác nhau — mục 2–3.

## 2. Đối xứng vs khoá công khai

Có hai họ mật mã, khác nhau ở *chìa khoá*. **Đối xứng (symmetric)**: hai bên chia sẻ *cùng một* khoá bí mật. Vấn đề nan giải: làm sao trao khoá đó cho nhau một cách an toàn khi chưa có kênh an toàn? Lời giải là khoá công khai:

> [!quote] Kurose (tr. 619)
> "rather than Bob and Alice sharing a single secret key (as in the case of symmetric key systems), Bob (the recipient of Alice's messages) instead has two keys—a public key that is available to everyone in the world (including Trudy the intruder) and a private key that is known only to Bob."
>
> *thay vì Bob và Alice **chia sẻ một khoá bí mật duy nhất** (như hệ đối xứng), Bob có **hai khoá** — một **khoá công khai (public key)** ai cũng biết (kể cả kẻ gian Trudy) và một **khoá riêng (private key)** chỉ mình Bob biết.*

Phép màu của cặp khoá: thứ mã hoá bằng khoá *công khai* chỉ giải được bằng khoá *riêng* (→ bí mật: ai cũng gửi được cho Bob, chỉ Bob đọc), và thứ ký bằng khoá *riêng* ai cũng kiểm được bằng khoá *công khai* (→ xác thực: chỉ Bob ký được, ai cũng xác nhận là Bob — mục 3). Đối xứng nhanh nên dùng mã hoá khối lượng lớn; khoá công khai chậm nên dùng để *trao khoá đối xứng* và *ký*. TLS (Bài 5) dùng *cả hai*: bắt tay bằng khoá công khai để thống nhất một khoá đối xứng phiên, rồi mã hoá dữ liệu bằng khoá đối xứng đó.

## 3. Chữ ký số và chứng chỉ (PKI)

Chữ ký số đạt *toàn vẹn + xác thực* bằng cách kết hợp hash với khoá riêng:

> [!quote] Kurose (tr. 631)
> "To create a digital signature, we first take the hash of the message and then encrypt the message with our private key (using public key cryptography). Thus, a digital signature is a "heavier" technique, since it requires an underlying Public Key Infrastructure (PKI) with certification authorities as described below."
>
> *Để tạo **chữ ký số**, ta **băm (hash) thông điệp trước**, rồi **mã hoá bằng khoá riêng** (dùng mật mã khoá công khai). Chữ ký số là kỹ thuật "nặng" hơn vì cần một **hạ tầng khoá công khai (PKI)** với các **certification authority** bên dưới.*

Nhưng còn một lỗ hổng niềm tin: làm sao biết "khoá công khai này *đúng* là của Bob", không phải của kẻ mạo danh? Lời giải là một bên thứ ba đáng tin:

> [!quote] Kurose (tr. 632)
> "Binding a public key to a particular entity is typically done by a Certification Authority (CA), whose job is to validate identities and issue certificates."
>
> ***Gắn một khoá công khai với một thực thể cụ thể** thường do một **Certification Authority (CA)** làm — CA có nhiệm vụ **xác minh danh tính và cấp chứng chỉ (certificate)**.*

Đây là mắt xích cuối: một **certificate** là "khoá công khai của X, được CA ký". Vì bạn tin CA, và CA ký xác nhận khoá này là của X, bạn tin khoá đó là của X. Đây chính là *chuỗi chứng chỉ* mà trình duyệt kiểm khi bạn vào HTTPS (Bài 5): cert của website được ký bởi CA, cert của CA được ký bởi CA gốc mà máy bạn đã tin sẵn. Demo mục 4 dựng hai mảnh gạch đầu — hash và chữ ký — bằng thư viện thật.

## 4. Demo: hash và chữ ký số bằng node crypto

Dùng `node:crypto` (có sẵn). Phần (1): hash phát hiện sửa đổi — đổi "100$" thành "900$" làm digest khác hẳn. Phần (2): ký bằng khoá riêng, verify bằng khoá công khai — thông điệp gốc verify đúng, thông điệp bị sửa verify sai.

```typescript
// Mật mã nền: (1) HASH phát hiện sửa đổi (integrity); (2) CHỮ KÝ bất đối xứng
// chứng minh "đúng người gửi + không bị sửa" mà không cần chia sẻ bí mật.
// Dùng node:crypto THẬT (có sẵn secp/ed trong Node, không cần gói ngoài).
import { createHash, generateKeyPairSync, sign, verify } from "node:crypto";

const msg = Buffer.from("chuyển 100$ cho Alice");
const tampered = Buffer.from("chuyển 900$ cho Alice");   // kẻ gian đổi 1→9

// --- (1) HASH: một thay đổi nhỏ → digest khác hẳn (avalanche) ---
const h = (b: Buffer) => createHash("sha256").update(b).digest("hex");
console.log("(1) SHA-256 (integrity):");
console.log(`    gốc     : ${h(msg).slice(0, 24)}…`);
console.log(`    bị sửa  : ${h(tampered).slice(0, 24)}…  ← khác hẳn ⇒ phát hiện sửa`);

// --- (2) CHỮ KÝ số: ký bằng PRIVATE key, ai cũng verify bằng PUBLIC key ---
const { publicKey, privateKey } = generateKeyPairSync("ed25519");
const signature = sign(null, msg, privateKey);          // chỉ người có private key ký được
console.log("\n(2) Chữ ký ed25519 (authenticity + integrity):");
console.log(`    verify(thông điệp GỐC, chữ ký)   : ${verify(null, msg, publicKey, signature)}`);
console.log(`    verify(thông điệp BỊ SỬA, chữ ký): ${verify(null, tampered, publicKey, signature)}`);
console.log("\nHash bắt được sửa đổi; chữ ký còn chứng minh AI gửi — nền của");
console.log("SigV4, S3 presigned URL, JWT, và chuỗi chứng chỉ TLS (CA ký public key).");
```

Kết quả chạy thật *(hash tất định — cùng input luôn cùng digest; verify trả true/false tất định dù khoá sinh ngẫu nhiên)*:

```
(1) SHA-256 (integrity):
    gốc     : df4a8aeb970ea383aa1d580f…
    bị sửa  : bd459337b9de6db856b30209…  ← khác hẳn ⇒ phát hiện sửa

(2) Chữ ký ed25519 (authenticity + integrity):
    verify(thông điệp GỐC, chữ ký)   : true
    verify(thông điệp BỊ SỬA, chữ ký): false

Hash bắt được sửa đổi; chữ ký còn chứng minh AI gửi — nền của
SigV4, S3 presigned URL, JWT, và chuỗi chứng chỉ TLS (CA ký public key).
```

Phần (1): đổi đúng *một* ký tự (1→9) làm digest đảo lộn hoàn toàn (avalanche) — nên chỉ cần so digest là biết có bị sửa hay không, mà không cần so cả thông điệp. Phần (2): chữ ký làm *nhiều hơn* hash — nó verify `true` cho thông điệp gốc (chứng minh đúng người ký *và* chưa bị sửa) và `false` ngay khi thông điệp đổi. Mấu chốt: người xác minh **chỉ cần khoá công khai**, không cần biết khoá riêng — nên server công bố khoá công khai cho cả thế giới mà vẫn an toàn. Đây đúng là cơ chế đằng sau mọi chữ ký bạn gặp trên AWS (mục 6).

> [!note] Tự thử
> - Ký `tampered` bằng *đúng* private key rồi verify `tampered` → `true`: chữ ký chỉ chứng minh "ai đó có private key đã ký *nội dung này*"; đổi nội dung thì phải ký lại. Nó không ngăn người có khoá nói dối — chỉ ràng danh tính vào nội dung.
> - Tạo *hai* keypair, ký bằng key A nhưng verify bằng public key B → `false`: minh hoạ "chỉ đúng khoá công khai cặp đôi mới verify được" — nền của việc CA gắn đúng khoá với đúng danh tính.
> - Thay `createHash("sha256")` bằng `"sha1"`: vẫn chạy, nhưng SHA-1 đã bị phá (va chạm) — vì sao AWS/TLS hiện đại cấm SHA-1.

## 5. Bảng so sánh: hash vs mã hoá vs chữ ký

Ba công cụ hay bị gộp làm một, nhưng đạt ba mục tiêu khác nhau:

| Công cụ               | Cho tính chất nào       | Cần khoá gì            | Ví dụ AWS                               |
| :-------------------- | :---------------------- | :--------------------- | :-------------------------------------- |
| **Hash** (SHA-256)    | toàn vẹn (phát hiện sửa) | không khoá             | ETag/checksum S3, content-hash          |
| **Mã hoá đối xứng**   | bí mật (khối lượng lớn) | 1 khoá chung bí mật    | mã hoá dữ liệu TLS phiên, SSE-S3/KMS data key |
| **Mã hoá khoá công khai** | bí mật + trao khoá  | công khai + riêng      | bắt tay TLS, KMS envelope encryption    |
| **Chữ ký số**         | toàn vẹn + **xác thực** | riêng (ký) / công khai (verify) | SigV4, JWT, chứng chỉ TLS (CA ký)  |

Quy luật: **chọn công cụ theo tính chất cần, đừng mặc định "mã hoá là xong".** Cần biết dữ liệu có bị sửa không → hash. Cần giấu nội dung → mã hoá. Cần chứng minh *ai gửi* và *chưa bị sửa* → chữ ký. HTTPS (Bài 5) dùng *cả bốn* cùng lúc: khoá công khai để bắt tay + verify cert (CA ký), đối xứng để mã hoá dữ liệu, hash để kiểm toàn vẹn từng record.

## 6. Nối về AWS

> [!note] Nối về AWS
> Mọi lần bạn gọi AWS là một bài mật mã chạy ngầm — xem [`aws-fund` Bài 1 — Security: IAM](../../aws-fund/bai_hoc/bai_01_security-iam.md) và [Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md):
> - **SigV4 — AWS ký *mọi* request.** Access key của bạn không gửi lên mạng; SDK dùng nó để **ký** request (HMAC + hash — chữ ký của mục 3), server ký lại và so. Nên dù ai chặn được request cũng không giả mạo được (toàn vẹn + xác thực), và khoá bí mật không bao giờ bay qua dây.
> - **S3 presigned URL = một chữ ký có hạn.** URL chứa chữ ký của *bạn* cho phép người khác (không có khoá) truy cập một object trong thời hạn — đúng "chữ ký ràng danh tính vào nội dung + thời hạn" của mục 3/Tự thử.
> - **KMS = envelope encryption.** KMS giữ khoá gốc, cấp *data key* để mã hoá dữ liệu (đối xứng, nhanh) rồi mã hoá chính data key bằng khoá gốc — đúng mô hình "khoá công khai trao khoá đối xứng" của mục 2, phóng lên dịch vụ quản lý.
> - **ACM / chứng chỉ TLS = PKI của mục 3.** CloudFront/ALB dùng cert do CA ký; trình duyệt tin vì tin CA. "Certificate expired/invalid" nghĩa là chuỗi tin cậy CA→cert bị đứt.
> - **JWT (Cognito)** = payload + chữ ký; service verify bằng khoá công khai của issuer — stateless auth (Bài 4), xác thực không cần hỏi lại server phát hành.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 14.1 — Ba yêu cầu bảo mật tách biệt? Mã hoá lo cái nào?
> **Đáp:** bí mật (confidentiality), toàn vẹn (integrity), xác thực (authentication). Mã hoá lo **bí mật**; toàn vẹn + xác thực cần hash/chữ ký — là việc khác.

> [!question] Thẻ 14.2 — Đối xứng vs khoá công khai khác nhau gì? Mỗi loại dùng khi nào?
> **Đáp:** đối xứng = 1 khoá chung (nhanh, nhưng khó trao khoá); khoá công khai = cặp public/private (chậm, nhưng giải bài toán trao khoá + ký). Thực tế: dùng công khai để *trao khoá đối xứng* + ký, đối xứng để mã dữ liệu lớn.

> [!question] Thẻ 14.3 — Chữ ký số tạo ra sao? Cho tính chất gì?
> **Đáp:** hash thông điệp rồi "mã hoá hash bằng khoá riêng". Cho **toàn vẹn + xác thực**: verify bằng khoá công khai, sai nếu bị sửa hoặc không đúng người ký.

> [!question] Thẻ 14.4 — CA giải quyết lỗ hổng niềm tin nào?
> **Đáp:** "khoá công khai này có *thật* là của X không?". CA xác minh danh tính và **ký (cấp certificate)** gắn khoá với danh tính; bạn tin CA → tin khoá là của X.

> [!question] Thẻ 14.5 — Vì sao người verify chỉ cần khoá công khai là an toàn?
> **Đáp:** khoá công khai không giải/ký được gì bí mật — nó chỉ *kiểm* chữ ký. Nên công bố cho cả thế giới vẫn an toàn; chỉ khoá riêng (giữ kín) mới ký được.

> [!question] Thẻ 14.6 — SigV4 và S3 presigned URL dùng khái niệm nền nào?
> **Đáp:** **chữ ký số**: access key ký request (không gửi khoá qua mạng); presigned URL là chữ ký có hạn cho phép truy cập object mà không cần khoá.

## 8. Câu hỏi tự kiểm tra

1. Phân biệt bí mật / toàn vẹn / xác thực. Vì sao "mã hoá rồi" chưa chắc đủ? *(mục 1, tr. 624)*
2. Đối xứng vs khoá công khai: khác nhau và dùng khi nào? TLS dùng loại nào? *(mục 2, tr. 619)*
3. Chữ ký số tạo thế nào, cho tính chất gì? Vì sao "nặng" hơn hash? *(mục 3, tr. 631)*
4. CA làm gì? Chuỗi chứng chỉ TLS hoạt động ra sao? *(mục 3, tr. 632)*
5. Chạy demo mục 4. Vì sao đổi 1 ký tự làm hash khác hẳn? Vì sao verify thông điệp bị sửa ra false? *(mục 4)*
6. Ánh xạ SigV4 / presigned URL / KMS / ACM vào khái niệm nền. Vì sao access key không bay qua mạng? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 14 — MẠNG NÂNG CAO: BẢO MẬT & MẬT MÃ
─────────────────────────────────────────────────────────
BA YÊU CẦU  bí mật (chỉ người nhận đọc) · toàn vẹn (không bị sửa) · xác thực
   (đúng người gửi) (Kurose tr.624). Mã hoá lo BÍ MẬT; integrity+auth là việc khác.

ĐỐI XỨNG vs KHOÁ CÔNG KHAI  đối xứng = 1 khoá chung (nhanh, khó trao khoá);
   công khai = cặp public/private (tr.619). Thực tế dùng CẢ HAI: công khai trao
   khoá đối xứng + ký, đối xứng mã dữ liệu lớn. (TLS Bài 5 = cả hai.)

CHỮ KÝ SỐ  hash thông điệp rồi mã bằng PRIVATE key (tr.631) → toàn vẹn+xác
   thực; verify bằng PUBLIC key. CA gắn public key với danh tính bằng CERTIFICATE
   (tr.632) → chuỗi tin cậy của HTTPS.

DEMO  đổi "100$"→"900$": SHA-256 khác hẳn (phát hiện sửa). ed25519: verify
   gốc=true, verify bị sửa=false. Người verify chỉ cần PUBLIC key.

BẢNG  hash=toàn vẹn(không khoá); đối xứng=bí mật(1 khoá); công khai=bí mật+
   trao khoá; chữ ký=toàn vẹn+xác thực. Chọn theo TÍNH CHẤT cần.

NỐI VỀ AWS  SigV4 ký mọi request (khoá không qua dây); S3 presigned=chữ ký có
   hạn; KMS=envelope (công khai trao khoá đối xứng); ACM=PKI/CA; JWT=payload+ký.
```

## Nguồn

- **James F. Kurose & Keith W. Ross**, *Computer Networking: A Top-Down Approach, 8th* — **ch. 8 (Security in Computer Networks)**: public vs symmetric key (tr. 619), message integrity/authentication (tr. 624), chữ ký số & PKI (tr. 631), Certification Authority (tr. 632). `tai_lieu/Computer Networking A Top-Down Approach 8th Edition by James W. Kurose, Keith W. Ross.pdf` — **offset PDF = tr. + 28**.
- Nối về AWS: [`aws-fund` Bài 1 — Security: IAM](../../aws-fund/bai_hoc/bai_01_security-iam.md), [Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md).
- Mở rộng của [Bài 5 — TCP & TLS](bai_05_mang-tcp-tls.md) (TLS dùng chính các viên gạch này).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · **[Bài 14 — Mạng nâng cao: bảo mật & mật mã] ← bạn đang ở đây** · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
