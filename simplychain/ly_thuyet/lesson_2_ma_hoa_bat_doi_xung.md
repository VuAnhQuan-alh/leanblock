# Mã hoá bất đối xứng (Asymmetric Encryption)

> Bài học dựa trên video **"Asymmetric Encryption – Simply explained"** (kênh *Simply Explained – Savjee*, YouTube `AQDCe585Lnc`).
> Nối tiếp [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md), phần *"Chữ ký số – lớp bảo vệ mà video không nhắc"*. Bài này giải thích chính xác cái cặp khoá đó là gì và vì sao nó hoạt động.
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.

---

## Mục lục

1. [Mã hoá đối xứng và vấn đề của nó](#1-mã-hoá-đối-xứng-và-vấn-đề-của-nó)
2. [Bài toán trao khoá](#2-bài-toán-trao-khoá)
3. [Ý tưởng mã hoá bất đối xứng](#3-ý-tưởng-mã-hoá-bất-đối-xứng)
4. [Cặp khoá hoạt động thế nào](#4-cặp-khoá-hoạt-động-thế-nào)
5. [Toán học đằng sau: hàm một chiều có cửa sập](#5-toán-học-đằng-sau-hàm-một-chiều-có-cửa-sập)
6. [Diffie–Hellman: trao khoá mà không gửi khoá](#6-diffiehellman-trao-khoá-mà-không-gửi-khoá)
7. [RSA: mổ xẻ từng bước](#7-rsa-mổ-xẻ-từng-bước)
8. [Chiều ngược lại: chữ ký số](#8-chiều-ngược-lại-chữ-ký-số)
9. [Vấn đề còn lại: làm sao biết public key là của đúng người](#9-vấn-đề-còn-lại-làm-sao-biết-public-key-là-của-đúng-người)
10. [Mã hoá lai và HTTPS](#10-mã-hoá-lai-và-https)
11. [Đường cong elliptic & mối đe doạ lượng tử](#11-đường-cong-elliptic--mối-đe-doạ-lượng-tử)
12. [Code minh hoạ](#12-code-minh-hoạ)
13. [Sai lầm thường gặp](#13-sai-lầm-thường-gặp)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Mã hoá đối xứng và vấn đề của nó

**Mã hoá đối xứng (symmetric encryption)** = dùng **cùng một khoá** để mã hoá và giải mã.

```
   "Xin chào"  ──[ mã hoá với KHOÁ K ]──▶  "8f2a9c1d..."
   "8f2a9c1d..." ──[ giải mã với KHOÁ K ]──▶  "Xin chào"
                                 ↑
                          CÙNG MỘT KHOÁ
```

Ví dụ đơn giản nhất là **mật mã Caesar**: dịch mỗi chữ cái đi N vị trí. Khoá là N.

```
Khoá = 3
HELLO  →  KHOOR
KHOOR  →  HELLO   (dịch ngược 3)
```

Mã hoá đối xứng hiện đại (**AES**) thì mạnh hơn Caesar hàng tỷ lần, nhưng **bản chất vẫn y hệt**: một khoá duy nhất, ai có khoá thì đọc được.

### 📚 Lý thuyết bổ sung: mã hoá đối xứng thật trông thế nào

**AES (Advanced Encryption Standard)** — chuẩn từ 2001, thay thế DES. Là một **block cipher**: mã hoá từng khối 128 bit một, với khoá 128 / 192 / 256 bit.

| Khái niệm             | Giải thích                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Block cipher**      | Mã từng khối cố định (AES: 16 byte). Cần **mode** để xử lý dữ liệu dài hơn.                                                          |
| **Stream cipher**     | Sinh dòng khoá giả ngẫu nhiên rồi XOR với dữ liệu (ChaCha20).                                                                        |
| **Mode of operation** | Cách nối các khối: ECB (❌ **không bao giờ dùng**), CBC, CTR, **GCM** (khuyến nghị).                                                  |
| **IV / nonce**        | Giá trị ngẫu nhiên đi kèm mỗi lần mã hoá, để cùng một bản rõ + cùng khoá vẫn ra bản mã khác nhau.                                    |
| **AEAD**              | *Authenticated Encryption with Associated Data* — vừa mã hoá vừa chống sửa (AES-GCM, ChaCha20-Poly1305). Mặc định nên dùng loại này. |

> ⚠️ **Vì sao ECB tệ:** ECB mã mỗi khối độc lập → khối giống nhau ra bản mã giống nhau → **lộ hình dạng dữ liệu**. Ảnh chim cánh cụt Tux mã bằng ECB vẫn nhìn ra con chim — ví dụ kinh điển trong sách giáo khoa mật mã.

**Điểm mạnh của đối xứng:** rất **nhanh**. CPU hiện đại có lệnh phần cứng `AES-NI`, đạt hàng GB/giây. Đây là lý do nó không bao giờ bị thay thế — xem [phần 10](#10-mã-hoá-lai-và-https).

---

## 2. Bài toán trao khoá

Đây là **vấn đề trung tâm** mà cả bài học xoay quanh.

Bob muốn gửi tin nhắn mã hoá cho Alice. Cả hai cần **cùng một khoá**. Nhưng:

> **Làm sao gửi khoá cho nhau qua Internet — một kênh mà kẻ nghe lén có thể đọc mọi thứ?**

```
Bob ──"khoá là 12345"──▶ Alice
          ↑
      😈 Eve nghe được luôn
      → Eve giải mã được mọi tin nhắn sau đó
```

Vòng luẩn quẩn: muốn gửi khoá an toàn thì phải mã hoá nó — nhưng mã hoá bằng khoá nào?

**Giải pháp cũ:** gặp mặt trực tiếp trao khoá. Thời chiến tranh, quân đội in **sổ khoá (code book)** rồi chuyển bằng người tin cẩn. Không khả thi trên Internet — bạn không thể bay sang Mỹ để bắt tay Amazon trước khi mua hàng.

### 📚 Lý thuyết bổ sung: vấn đề còn tệ hơn bạn tưởng

Với **n** người muốn liên lạc riêng tư đôi một, số khoá đối xứng cần là:

```
n(n − 1) / 2
```

| Số người | Số khoá cần |
| -------- | ----------- |
| 10       | 45          |
| 100      | 4.950       |
| 1.000    | 499.500     |
| 1 triệu  | ~500 tỷ     |

Đây gọi là **key distribution problem** — bài toán bùng nổ tổ hợp. Internet có hàng tỷ thiết bị chưa từng "gặp" nhau. Nếu chỉ có mã hoá đối xứng thì **thương mại điện tử không thể tồn tại**.

---

## 3. Ý tưởng mã hoá bất đối xứng

Năm 1976, Whitfield Diffie và Martin Hellman công bố một ý tưởng lật ngược mọi thứ:

> **Dùng HAI khoá khác nhau thay vì một.**

```
        ┌─────────────────┐          ┌─────────────────┐
        │  PUBLIC KEY     │          │  PRIVATE KEY    │
        │  🔓 khoá công   │  cặp đôi │  🔑 khoá riêng  │
        │  Chia sẻ tự do  │◀────────▶│  Giữ bí mật     │
        │  Đăng lên web   │          │  KHÔNG BAO GIỜ  │
        │  cũng không sao │          │  gửi cho ai     │
        └─────────────────┘          └─────────────────┘
              MÃ HOÁ                       GIẢI MÃ
```

Hai khoá liên kết với nhau **về mặt toán học**, nhưng:

- Biết public key → **không thể** suy ra private key.
- Cái gì mã hoá bằng public key → **chỉ** private key mở được.

### Ẩn dụ: ổ khoá và chìa

Cách dễ hình dung nhất:

> Alice mua một đống **ổ khoá đang mở** và phát cho cả thế giới — vứt ngoài đường cũng được. Chìa mở ổ khoá đó thì **chỉ mình Alice giữ**.
>
> Bob muốn gửi thư bí mật: bỏ thư vào hộp, lấy ổ khoá của Alice **bấm khoá lại**. Từ giây phút đó, **kể cả Bob cũng không mở lại được**. Chỉ Alice mở được.

Điểm mấu chốt: **hành động khoá không cần bí mật; hành động mở mới cần.**

### 📚 Lý thuyết bổ sung: lịch sử

| Năm           | Sự kiện                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1970–1974** | James Ellis, Clifford Cocks, Malcolm Williamson tại **GCHQ** (tình báo Anh) phát minh ra ý tưởng này trước — nhưng bị đóng dấu **tuyệt mật**, mãi 1997 mới công bố. |
| **1976**      | **Diffie–Hellman** công bố *"New Directions in Cryptography"* — công khai đầu tiên. Giải Turing 2015.                                                               |
| **1977**      | **RSA** (Rivest, Shamir, Adleman) — hệ mã bất đối xứng thực dụng đầu tiên. Giải Turing 2002.                                                                        |
| **1985**      | **ECC** (Koblitz, Miller) — mật mã đường cong elliptic, khoá ngắn hơn nhiều.                                                                                        |
| **2024**      | **NIST** chuẩn hoá thuật toán hậu lượng tử: ML-KEM, ML-DSA.                                                                                                         |

Đây được coi là **bước đột phá lớn nhất lịch sử mật mã học 2000 năm** — lần đầu tiên hai người xa lạ có thể nói chuyện bí mật mà chưa từng gặp nhau.

---

## 4. Cặp khoá hoạt động thế nào

Kịch bản đầy đủ: Bob gửi tin nhắn cho Alice.

```
BƯỚC 1: Alice tạo cặp khoá
   Alice: 🔓 public_A   +   🔑 private_A (giữ trong máy, không đi đâu)

BƯỚC 2: Alice gửi PUBLIC key cho Bob qua kênh công khai
   Alice ──── 🔓 public_A ────▶ Bob
                  ↑
              😈 Eve chép lại — KHÔNG SAO CẢ

BƯỚC 3: Bob mã hoá
   "Chuyển 100 triệu"  --[mã hoá bằng 🔓 public_A]-->  "a3f9d2c8..."

BƯỚC 4: Bob gửi bản mã
   Bob ──── "a3f9d2c8..." ────▶ Alice
                  ↑
              😈 Eve chép lại — vô dụng, Eve chỉ có public_A
                 mà public_A KHÔNG giải mã được

BƯỚC 5: Alice giải mã bằng 🔑 private_A
   "a3f9d2c8..."  -->  "Chuyển 100 triệu"  ✓
```

**Kết quả:** Bob và Alice liên lạc bí mật **mà chưa bao giờ trao đổi bí mật nào**. Bài toán trao khoá ở [phần 2](#2-bài-toán-trao-khoá) đã được giải.

### 📚 Lý thuyết bổ sung: hai chiều, hai mục đích

Cặp khoá dùng được theo **cả hai chiều**, và mỗi chiều cho một mục đích hoàn toàn khác:

| Chiều      | Mã bằng                     | Mở bằng                      | Mục đích                     | Trả lời câu hỏi               |
| ---------- | --------------------------- | ---------------------------- | ---------------------------- | ----------------------------- |
| **Mã hoá** | 🔓 public của **người nhận** | 🔑 private của **người nhận** | **Bí mật** (confidentiality) | *"Chỉ đúng người đọc được?"*  |
| **Chữ ký** | 🔑 private của **người gửi** | 🔓 public của **người gửi**   | **Xác thực** (authenticity)  | *"Đúng người này gửi không?"* |

> 💡 **Mẹo nhớ:** Muốn **giấu** → dùng khoá của **người nhận**. Muốn **chứng minh mình là ai** → dùng khoá của **chính mình**.

Muốn cả hai thì làm cả hai: **ký trước bằng private của mình, rồi mã hoá bằng public của người nhận** (thứ tự *sign-then-encrypt*).

---

## 5. Toán học đằng sau: hàm một chiều có cửa sập

Video nói "hai khoá liên kết toán học nhưng không suy ngược được". Đây là *cái gì* đằng sau câu đó.

### Trapdoor one-way function

Toàn bộ mật mã bất đối xứng đứng trên một khái niệm: **hàm một chiều có cửa sập**.

```
  f(x)  DỄ  ────────────────────▶  y
  x  ◀──── f⁻¹(y) CỰC KHÓ ────────  y
  x  ◀──── nhưng DỄ nếu biết CỬA SẬP (private key)
```

Ba tính chất:
1. Tính **xuôi** rất dễ (mili giây).
2. Tính **ngược** cực khó (hàng tỷ năm).
3. **Trừ khi** bạn có một mẩu thông tin bí mật — **cửa sập** → tính ngược lại dễ ngay.

**Private key chính là cửa sập đó.**

### Hai bài toán khó được dùng nhiều nhất

**1. Phân tích thừa số nguyên tố (integer factorization)** — nền của **RSA**

```
Nhân:      61 × 53 = 3233                    ← tức thì
Phân tích: 3233 = ? × ?                      ← phải dò
```

Với số nhỏ thì dễ. Nhưng với hai số nguyên tố 1024 bit:

```
p × q = n   (n dài 2048 bit ≈ 617 chữ số)
```

Nhân ra `n` mất micro giây. Phân tích `n` ngược về `p, q` — **mọi siêu máy tính trên Trái Đất chạy đến khi Mặt Trời tắt cũng không xong**.

**2. Logarit rời rạc (discrete logarithm)** — nền của **Diffie–Hellman** và **ECC**

```
Tính:       g^a mod p = A          ← dễ (thuật toán bình phương liên tiếp)
Tìm ngược:  a = log_g(A) mod p     ← cực khó
```

Phép `mod` (chia lấy dư) là thứ phá huỷ thông tin. Với số thực, `log` giải được dễ dàng. Nhưng trong **số học đồng dư**, kết quả nhảy lung tung không theo thứ tự nào → không có cách nào ngoài dò từng giá trị.

```
Ví dụ nhỏ, p = 23, g = 5:
  5^1 mod 23 = 5      5^5  mod 23 = 20
  5^2 mod 23 = 2      5^6  mod 23 = 8
  5^3 mod 23 = 10     5^7  mod 23 = 17
  5^4 mod 23 = 4      5^8  mod 23 = 16
                      ↑ nhảy loạn xạ, không tăng dần → không thể "đoán hướng"
```

> 💡 **Chú ý điều này:** Mật mã bất đối xứng **không được chứng minh là an toàn**. Nó an toàn vì **chưa ai tìm ra cách giải nhanh** cho các bài toán trên. Nếu mai có người công bố thuật toán phân tích thừa số trong thời gian đa thức, RSA sụp đổ trong một đêm. An toàn ở đây là **niềm tin dựa trên hàng chục năm nỗ lực thất bại của cả giới toán học** — không phải định lý.

---

## 6. Diffie–Hellman: trao khoá mà không gửi khoá

Đây là thuật toán giải bài toán trao khoá đầu tiên, và **vẫn được dùng trong mọi kết nối HTTPS hôm nay**.

### Ẩn dụ trộn sơn

```
                CÔNG KHAI: ai cũng thấy màu VÀNG
                              │
        ┌─────────────────────┴─────────────────────┐
     ALICE                                        BOB
  bí mật: ĐỎ                                  bí mật: XANH
        │                                          │
  VÀNG + ĐỎ = CAM                          VÀNG + XANH = LỤC
        │                                          │
        └──── gửi CAM ────▶ 😈 ◀──── gửi LỤC ──────┘
                            Eve thấy: VÀNG, CAM, LỤC
        │                                          │
  CAM + XANH? Không —                       LỤC + ĐỎ
  ALICE: LỤC + ĐỎ = NÂU                     BOB: CAM + XANH = NÂU
        │                                          │
        └──────────── BÍ MẬT CHUNG: NÂU ───────────┘

  Eve có VÀNG, CAM, LỤC nhưng KHÔNG tách ngược được sơn
  → không tạo được NÂU.
```

**Tách sơn đã trộn** chính là ẩn dụ cho **logarit rời rạc**: trộn dễ, tách khó.

### Bản thật bằng toán

Công khai: số nguyên tố lớn `p` và cơ sở `g`.

| Bước | Alice           | Kênh công khai | Bob             |
| ---- | --------------- | -------------- | --------------- |
| 1    | chọn bí mật `a` |                | chọn bí mật `b` |
| 2    | `A = gᵃ mod p`  | `A ──▶  ◀── B` | `B = gᵇ mod p`  |
| 3    | `s = Bᵃ mod p`  |                | `s = Aᵇ mod p`  |

Hai bên ra **cùng một `s`**, vì:

```
Bᵃ = (gᵇ)ᵃ = g^(ab)   ≡   (gᵃ)ᵇ = Aᵇ   (mod p)
```

Eve có `p, g, A, B` nhưng để tính `s` phải tìm được `a` hoặc `b` → phải giải logarit rời rạc → bó tay.

**Ví dụ số nhỏ** (`p = 23`, `g = 5`):

```
Alice: a = 6  →  A = 5⁶ mod 23 = 8
Bob:   b = 15 →  B = 5¹⁵ mod 23 = 19
Alice: s = 19⁶ mod 23 = 2
Bob:   s = 8¹⁵ mod 23 = 2      ✓ khớp
```

### 📚 Lý thuyết bổ sung: Perfect Forward Secrecy

DH có một biến thể cực quan trọng: **DHE / ECDHE** (chữ **E** = *Ephemeral*, phù du).

Ý tưởng: **sinh cặp `a, b` mới cho MỖI phiên kết nối, dùng xong vứt**.

Lợi ích gọi là **Perfect Forward Secrecy (PFS)**:

> Nếu 10 năm sau private key dài hạn của server bị lộ, kẻ tấn công **vẫn không giải mã được** những phiên đã ghi lại trong quá khứ — vì khoá phiên đã bị xoá và không thể tái tạo.

Không có PFS thì mô hình tấn công **"harvest now, decrypt later"** (thu thập hôm nay, giải mã sau) rất hiệu quả: cứ ghi lại toàn bộ traffic mã hoá, chờ ngày lấy được khoá. TLS 1.3 **bắt buộc** PFS — mọi bộ mã không hỗ trợ đã bị loại bỏ khỏi chuẩn.

> ⚠️ **DH thuần chống nghe lén, KHÔNG chống MITM.** Eve có thể tự làm DH với Alice và một DH riêng với Bob, ngồi giữa dịch qua dịch lại. Cần **xác thực** để chặn — xem [phần 9](#9-vấn-đề-còn-lại-làm-sao-biết-public-key-là-của-đúng-người).

---

## 7. RSA: mổ xẻ từng bước

RSA khác DH: nó **mã hoá trực tiếp** được, và **ký** được.

### Sinh khoá

```
1. Chọn 2 số nguyên tố lớn bí mật:      p, q
2. Tính modulus:                        n = p × q
3. Tính hàm Euler:                      φ(n) = (p−1)(q−1)
4. Chọn số mũ công khai e:              gcd(e, φ(n)) = 1   (thường e = 65537)
5. Tính số mũ riêng d:                  d × e ≡ 1  (mod φ(n))

   🔓 PUBLIC KEY  = (n, e)
   🔑 PRIVATE KEY = (n, d)
   → Vứt bỏ p, q, φ(n) — chúng là "cửa sập"
```

### Mã hoá / giải mã

```
Mã hoá:   c = mᵉ mod n        (dùng public)
Giải mã:  m = c^d mod n       (dùng private)
```

### Ví dụ chạy tay được

```
p = 61, q = 53
n = 61 × 53 = 3233
φ = 60 × 52 = 3120
e = 17
d = 2753        (vì 17 × 2753 = 46801 = 15 × 3120 + 1 ✓)

🔓 public  = (3233, 17)
🔑 private = (3233, 2753)

Mã hoá m = 65:
  c = 65¹⁷ mod 3233 = 2790

Giải mã:
  m = 2790²⁷⁵³ mod 3233 = 65   ✓
```

### Vì sao Eve không phá được?

Eve có `(n=3233, e=17)`. Muốn tính `d`, Eve cần `φ(n)`. Muốn có `φ(n)`, Eve cần `p` và `q`. Muốn có `p, q`, Eve phải **phân tích thừa số** `n`.

Với `n = 3233` thì Eve làm được trong 1 giây. Với `n` dài **2048 bit** thì đó là bài toán chưa ai giải nổi.

> 💡 **Đây là chỗ "liên kết toán học" trở nên cụ thể:** public key và private key nối với nhau qua `φ(n)`. Nhưng `φ(n)` bị **khoá sau bức tường phân tích thừa số**. Public key ở ngay đó, private key ở ngay đó, và giữa chúng là một bài toán bất khả thi.

### 📚 Lý thuyết bổ sung: RSA "sách giáo khoa" là RSA HỎNG

Công thức `c = mᵉ mod n` ở trên gọi là **textbook RSA** — **không bao giờ được dùng trong thực tế**:

| Lỗ hổng          | Vì sao                                                                    |
| ---------------- | ------------------------------------------------------------------------- |
| **Tất định**     | Cùng `m` → cùng `c`. Eve mã thử "YES"/"NO" rồi so sánh là biết nội dung.  |
| **Malleability** | `c₁ × c₂ mod n` giải ra `m₁ × m₂`. Sửa được bản mã mà không cần khoá.     |
| **`m` nhỏ**      | Nếu `mᵉ < n` thì `mod` không có tác dụng → chỉ cần lấy căn bậc `e` là ra. |

**Lời giải: padding.** Thêm dữ liệu ngẫu nhiên có cấu trúc vào `m` trước khi mã:

- **OAEP** (Optimal Asymmetric Encryption Padding) — dùng cho mã hoá.
- **PSS** (Probabilistic Signature Scheme) — dùng cho chữ ký.
- ~~PKCS#1 v1.5~~ — cũ, dính tấn công Bleichenbacher, tránh dùng.

Đây là ví dụ điển hình cho câu **"đừng tự viết mật mã"**: toán đúng nhưng cài đặt sai thì vẫn vỡ.

---

## 8. Chiều ngược lại: chữ ký số

Đảo ngược thứ tự dùng khoá, ta được một công cụ hoàn toàn khác.

```
KÝ (Alice, dùng 🔑 private_A):
   tài liệu ──▶ HASH ──▶ h ──[mã bằng private_A]──▶ chữ ký

XÁC MINH (bất kỳ ai, dùng 🔓 public_A):
   chữ ký ──[giải bằng public_A]──▶ h'
   tài liệu ──▶ HASH ──▶ h
   h == h' ?  →  ✓ đúng Alice ký, và tài liệu chưa bị sửa
```

### Vì sao phải hash trước khi ký?

Ba lý do:

1. **Tốc độ** — RSA rất chậm. Ký 1 hash 32 byte thay vì ký file 1 GB.
2. **Giới hạn kích thước** — RSA chỉ ký được dữ liệu nhỏ hơn `n`.
3. **An toàn** — chặn tấn công malleability đã nói ở trên.

### Chữ ký số cho ta 3 đảm bảo

| Đảm bảo             | Nghĩa là                                         |
| ------------------- | ------------------------------------------------ |
| **Authentication**  | Đúng người đó ký — vì chỉ họ có private key      |
| **Integrity**       | Nội dung chưa bị sửa — vì hash sẽ lệch ngay      |
| **Non-repudiation** | Không thể chối — họ không thể nói "tôi không ký" |

> 🔗 [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md) cho thấy chính xác cách Bitcoin dùng cặp khoá này, đến từng byte. Còn [Bài 8 – Zero-Knowledge Proof](lesson_8_zero_knowledge_proof.md) tiết lộ một điều bất ngờ: **chữ ký số bản chất LÀ một zero-knowledge proof**.

> 🔗 **Đây chính là thứ bảo vệ coin của bạn trong [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md).** Giao dịch Bitcoin được ký bằng private key. Kẻ nắm 51% hashrate không tiêu được coin người khác vì hắn **không có private key** — hắn kiểm soát được *thứ tự* các giao dịch, nhưng không tạo nổi một chữ ký hợp lệ.

### 📚 Lý thuyết bổ sung: các hệ chữ ký

| Thuật toán          | Nền tảng                                | Dùng ở đâu                                          |
| ------------------- | --------------------------------------- | --------------------------------------------------- |
| **RSA-PSS**         | Phân tích thừa số                       | Chứng chỉ TLS, ký code                              |
| **ECDSA**           | Đường cong elliptic (secp256k1 / P-256) | **Bitcoin**, Ethereum, TLS                          |
| **EdDSA / Ed25519** | Đường cong Edwards                      | SSH, Signal, Tor — nhanh và khó cài sai hơn ECDSA   |
| **Schnorr**         | Elliptic                                | Bitcoin Taproot (2021) — gộp nhiều chữ ký thành một |
| **ML-DSA**          | Lattice                                 | Chuẩn hậu lượng tử của NIST (2024)                  |

> ⚠️ **ECDSA có một cái bẫy chết người:** mỗi lần ký phải dùng một số ngẫu nhiên `k` **mới toanh**. Dùng lại `k` cho hai chữ ký khác nhau → **private key bị tính ra bằng đại số cấp 2**. Sony dính đúng lỗi này ở PlayStation 3 năm 2010, làm lộ khoá ký firmware. Ed25519 sinh ra để loại bỏ hẳn cái bẫy này (nó tính `k` một cách tất định từ thông điệp).

---

## 9. Vấn đề còn lại: làm sao biết public key là của đúng người

Mã hoá bất đối xứng giải xong bài toán trao khoá, nhưng đẻ ra một bài toán mới:

> **Cái public key bạn vừa nhận — làm sao chắc nó của Alice chứ không phải của kẻ giả mạo?**

### Tấn công Man-in-the-Middle (MITM)

```
Bob nghĩ đang nói với Alice:

Bob ──▶ 😈 Mallory ──▶ Alice
        │
        ├─ Mallory chặn public_A của Alice, thay bằng public_M của mình
        ├─ Bob mã hoá bằng public_M (tưởng là của Alice)
        ├─ Mallory GIẢI MÃ được, đọc thoải mái, sửa nếu muốn
        └─ Mallory mã lại bằng public_A thật rồi chuyển tiếp cho Alice

  Cả Bob và Alice đều KHÔNG BIẾT GÌ. Mã hoá vẫn "hoạt động".
```

**Bản thân mã hoá không cứu được.** Cần một cơ chế **ràng buộc danh tính với public key**.

### Chứng chỉ số & PKI

**Chứng chỉ (certificate)** = public key + danh tính, **được một bên thứ ba tin cậy ký**.

```
┌─────────────────────────────────────┐
│ CERTIFICATE                         │
│ Subject:    google.com              │  ← danh tính
│ PublicKey:  🔓 04a3f9...            │  ← khoá
│ Issuer:     DigiCert                │  ← ai bảo chứng
│ Valid:      2026-01 → 2026-12       │
│ ─────────────────────────────────── │
│ Signature:  9c2f8a...               │  ← DigiCert KÝ bằng private của họ
└─────────────────────────────────────┘
```

Trình duyệt xác minh chữ ký này bằng **public key của DigiCert** — thứ đã được **cài sẵn trong hệ điều hành/trình duyệt** từ nhà máy. Đó là **neo tin cậy (trust anchor)**.

**Chuỗi tin cậy:**

```
Root CA (cài sẵn trong máy bạn)
   └─ ký ─▶ Intermediate CA
              └─ ký ─▶ Chứng chỉ của google.com
```

Hệ thống này gọi là **PKI (Public Key Infrastructure)**.

### 📚 Lý thuyết bổ sung: PKI không hoàn hảo

- **CA bị hack là thảm hoạ.** DigiNotar (Hà Lan, 2011) bị xâm nhập, kẻ tấn công phát hành chứng chỉ giả cho `*.google.com` và dùng để nghe lén 300.000 người dùng Iran. CA đó phá sản.
- **Bạn phải tin ~150 CA.** Chỉ cần **một** CA gian dối hoặc bị ép buộc là đủ phá vỡ toàn bộ.
- **Certificate Transparency (CT)** — biện pháp vá: mọi chứng chỉ phải được ghi vào log công khai chỉ-ghi-thêm (nghe quen không? đúng, ý tưởng y hệt blockchain). Chủ sở hữu domain có thể giám sát xem có ai phát hành chứng chỉ trái phép cho mình không.

### Mô hình thay thế PKI

| Mô hình              | Cách tin                                                   | Ví dụ                 |
| -------------------- | ---------------------------------------------------------- | --------------------- |
| **PKI / CA**         | Tin bên thứ ba tập trung                                   | HTTPS                 |
| **Web of Trust**     | Bạn bè ký khoá cho nhau, tin lan truyền                    | PGP / GPG             |
| **TOFU**             | *Trust On First Use* — tin lần đầu, cảnh báo nếu đổi       | SSH (`known_hosts`)   |
| **Safety number**    | Người dùng tự so mã ngoài kênh                             | Signal, WhatsApp      |
| **Khoá = danh tính** | Không cần tin ai; địa chỉ **chính là** hash của public key | **Bitcoin, Ethereum** |

> 💡 **Blockchain né được toàn bộ bài toán PKI.** Địa chỉ ví của bạn **được suy ra từ chính public key** (`address = hash(public_key)`). Không cần ai chứng nhận "khoá này thuộc về John" — vì địa chỉ *chính là* khoá. Đây là một trong những ý tưởng đẹp nhất của thiết kế Bitcoin: **loại bỏ trung gian tin cậy ở cả tầng mật mã**, không chỉ tầng tài chính.

---

## 10. Mã hoá lai và HTTPS

### Vấn đề: bất đối xứng CHẬM

| Thuật toán              | Tốc độ tương đối          |
| ----------------------- | ------------------------- |
| AES-256 (đối xứng)      | ~1–10 GB/giây (có AES-NI) |
| RSA-2048 (bất đối xứng) | ~vài trăm KB/giây         |

Chênh nhau **hàng nghìn lần**. Mã cả video Netflix bằng RSA là bất khả thi.

### Lời giải: mã hoá lai (hybrid encryption)

> **Dùng bất đối xứng để trao đổi một khoá đối xứng ngắn. Rồi dùng đối xứng để mã toàn bộ dữ liệu.**

```
[ CHẬM, chỉ 1 lần ]              [ NHANH, cho toàn bộ phiên ]
Bất đối xứng                     Đối xứng
(RSA / ECDHE)     ───────▶       (AES-GCM / ChaCha20)
   trao khoá phiên                mã hoá dữ liệu thật
```

Quay lại ẩn dụ ổ khoá: bạn không nhét cả kiện hàng vào hộp có ổ khoá — bạn chỉ nhét **chiếc chìa của kho hàng** vào đó.

### TLS 1.3 handshake — rút gọn

```
1. Client → Server:  "Chào, tôi hỗ trợ các bộ mã X, Y, Z"
                     + phần công khai ECDHE của client
2. Server → Client:  chọn bộ mã
                     + phần công khai ECDHE của server
                     + CHỨNG CHỈ (public key + chữ ký của CA)
                     + chữ ký lên toàn bộ handshake  ← chống MITM
3. Client:           - xác minh chứng chỉ qua chuỗi CA
                     - tính khoá phiên chung bằng ECDHE
4. Cả hai:           chuyển sang AES-GCM cho toàn bộ dữ liệu còn lại
```

Nhìn kỹ, bạn thấy **cả ba mảnh ghép** của bài học nằm chung một chỗ:

| Mảnh                     | Vai trò trong TLS                            |
| ------------------------ | -------------------------------------------- |
| **ECDHE** (bất đối xứng) | Trao khoá phiên, cho Perfect Forward Secrecy |
| **Chữ ký + chứng chỉ**   | Xác thực server, chặn MITM                   |
| **AES-GCM** (đối xứng)   | Mã hoá tốc độ cao dữ liệu thật               |

> 💡 **Cái ổ khoá 🔒 trên thanh địa chỉ trình duyệt = toàn bộ bài học này đang chạy.** Mỗi lần bạn mở một trang web.

---

## 11. Đường cong elliptic & mối đe doạ lượng tử

### ECC — cùng độ an toàn, khoá ngắn hơn nhiều

**Elliptic Curve Cryptography** dùng logarit rời rạc trên **nhóm điểm của đường cong elliptic** thay vì trên số nguyên. Bài toán này khó hơn nhiều với cùng độ dài khoá:

| Mức an toàn | Khoá RSA     | Khoá ECC    | Tỷ lệ   |
| ----------- | ------------ | ----------- | ------- |
| 80 bit      | 1024 bit     | 160 bit     | 6×      |
| 112 bit     | 2048 bit     | 224 bit     | 9×      |
| 128 bit     | **3072 bit** | **256 bit** | **12×** |
| 256 bit     | 15360 bit    | 512 bit     | 30×     |

→ Khoá ngắn hơn = ít băng thông, ít pin, ít RAM. Vì thế ECC thống trị di động, IoT, và **mọi blockchain**.

Các đường cong hay gặp:
- **secp256k1** — Bitcoin, Ethereum
- **P-256 / secp256r1** — TLS, chứng chỉ (đường cong của NIST)
- **Curve25519** — Signal, SSH, WireGuard (thiết kế bởi Daniel J. Bernstein, được tin hơn vì tham số minh bạch)

### 📚 Lý thuyết bổ sung: máy tính lượng tử phá được cái gì

**Thuật toán Shor (1994)** giải được **cả** bài toán phân tích thừa số **và** logarit rời rạc trong thời gian đa thức trên máy tính lượng tử.

| Thuật toán         | Lượng tử                                         |
| ------------------ | ------------------------------------------------ |
| RSA                | ☠️ **Vỡ hoàn toàn**                               |
| Diffie–Hellman     | ☠️ **Vỡ hoàn toàn**                               |
| ECC / ECDSA        | ☠️ **Vỡ hoàn toàn**                               |
| AES-256 (đối xứng) | ⚠️ Yếu đi còn ~128 bit (Grover) — **vẫn an toàn** |
| SHA-256 (hash)     | ⚠️ Yếu đi còn ~128 bit — **vẫn an toàn**          |

> Điểm quan trọng: **mã hoá đối xứng và hash gần như không hề hấn gì** — chỉ cần tăng gấp đôi độ dài khoá. Chỉ **mật mã bất đối xứng** là bị xoá sổ.

**Máy tính lượng tử đủ mạnh chưa tồn tại** (cần hàng triệu qubit ổn định lỗi; hiện tại mới ở mức hàng nghìn qubit nhiễu). Nhưng mối lo **"harvest now, decrypt later"** là có thật — dữ liệu bị ghi lại hôm nay có thể bị giải mã sau 15 năm.

**Mật mã hậu lượng tử (PQC)** — chuẩn NIST 2024:
- **ML-KEM** (Kyber) — trao khoá, dựa trên lattice
- **ML-DSA** (Dilithium) — chữ ký, lattice
- **SLH-DSA** (SPHINCS+) — chữ ký, chỉ dựa trên hash (bảo thủ nhất)

Chrome và Cloudflare đã bật **hybrid X25519 + ML-KEM** trong TLS từ 2024 — dùng đồng thời cả cũ lẫn mới, an toàn nếu **một trong hai** còn đứng vững.

---

## 12. Code minh hoạ

Chỉ dùng **thư viện chuẩn của Node**, chạy được ngay, không cài gì thêm. Toàn bộ assert đã chạy pass.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// cryptodemo.ts — Diffie-Hellman + RSA đồ chơi. Chỉ dùng thư viện chuẩn Node.
// Chạy: node cryptodemo.ts
import { createHash, randomBytes } from "node:crypto";
import { strict as assert } from "node:assert";

// ---------- tiện ích số học modulo (BigInt không có sẵn) ----------
/** Luôn trả về kết quả KHÔNG ÂM — TS khác Python ở chỗ này! (-5n % 3n === -2n) */
const mod = (a: bigint, m: bigint): bigint => ((a % m) + m) % m;

/** Luỹ thừa modulo: tương đương pow(b, e, m) của Python. */
function modPow(b: bigint, e: bigint, m: bigint): bigint {
  let r = 1n;
  b = mod(b, m);
  while (e > 0n) {
    if (e & 1n) r = (r * b) % m;
    b = (b * b) % m;
    e >>= 1n;
  }
  return r;
}

/** Nghịch đảo modulo bằng Euclid mở rộng: tương đương pow(a, -1, m). */
function modInv(a: bigint, m: bigint): bigint {
  let [old_r, r] = [mod(a, m), m];
  let [old_s, s] = [1n, 0n];
  while (r !== 0n) {
    const q = old_r / r;
    [old_r, r] = [r, old_r - q * r];
    [old_s, s] = [s, old_s - q * s];
  }
  assert(old_r === 1n, "không tồn tại nghịch đảo modulo");
  return mod(old_s, m);
}

/** Số ngẫu nhiên an toàn mật mã trong [0, max). Lấy đúng số bit rồi loại phần dư. */
function randBelow(max: bigint): bigint {
  const bits = max.toString(2).length;
  const bytes = Math.ceil(bits / 8);
  const excess = BigInt(bytes * 8 - bits);
  while (true) {
    const n = BigInt("0x" + randomBytes(bytes).toString("hex")) >> excess;
    if (n < max) return n;            // xác suất loại < 50% -> dừng nhanh
  }
}

// ---------- 1. Diffie-Hellman: hai bên tạo chung 1 bí mật qua kênh công khai ----------
const P = BigInt("0x" + [
  "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1",
  "29024E088A67CC74020BBEA63B139B22514A08798E3404DD",
  "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245",
  "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED",
  "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381",
  "FFFFFFFFFFFFFFFF",
].join(""));                                  // nhóm 1536-bit RFC 3526
const G = 2n;

function dhDemo(): void {
  const a = randBelow(P - 2n) + 2n;           // bí mật của Alice
  const b = randBelow(P - 2n) + 2n;           // bí mật của Bob
  const A = modPow(G, a, P), B = modPow(G, b, P);   // gửi công khai
  const sAlice = modPow(B, a, P);             // B^a = g^(ba)
  const sBob = modPow(A, b, P);               // A^b = g^(ab)   → bằng nhau
  assert(sAlice === sBob, "DH phải ra cùng một bí mật chung");
  const key = createHash("sha256").update(sAlice.toString()).digest("hex");
  console.log(`DH  A gửi công khai : ${A.toString().slice(0, 40)}...`);
  console.log(`DH  B gửi công khai : ${B.toString().slice(0, 40)}...`);
  console.log(`DH  khoá chung      : ${key.slice(0, 32)}...  (khớp cả hai bên ✓)`);
}

// ---------- 2. RSA đồ chơi: số nhỏ để nhìn thấy toán ----------
function rsaToy(): void {
  const p = 61n, q = 53n;
  const n = p * q;                            // 3233
  const phi = (p - 1n) * (q - 1n);            // 3120
  const e = 17n;
  const d = modInv(e, phi);                   // 2753
  console.log(`\nRSA public  = (n=${n}, e=${e})`);
  console.log(`RSA private = (n=${n}, d=${d})   [suy ra từ p=${p}, q=${q}]`);

  const m = 65n;
  const c = modPow(m, e, n);                  // mã hoá bằng PUBLIC key
  const m2 = modPow(c, d, n);                 // giải mã bằng PRIVATE key
  console.log(`  m=${m} --public--> c=${c} --private--> m'=${m2}`);
  assert(m2 === m, "giải mã phải ra bản gốc");

  // Chiều ngược lại = CHỮ KÝ SỐ
  const sig = modPow(m, d, n);                // ký bằng PRIVATE key
  const ver = modPow(sig, e, n);              // xác minh bằng PUBLIC key
  console.log(`  m=${m} --private--> sig=${sig} --public--> ${ver}  (chữ ký hợp lệ ✓)`);
  assert(ver === m);

  // Kẻ giả mạo không có d thì ký sai
  const fake = modPow(m, 999n, n);
  assert(modPow(fake, e, n) !== m, "chữ ký giả phải bị phát hiện");
  console.log(`  chữ ký giả ${fake} -> xác minh ra ${modPow(fake, e, n)} ≠ ${m} ✗ bị từ chối`);
}

dhDemo();
rsaToy();
console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
DH  A gửi công khai : 7594322078209116598121533857072554636669...
DH  B gửi công khai : 5848901131515616636994360223500415903915...
DH  khoá chung      : 2a0332c061e4d5c200ed50f86e130cda...  (khớp cả hai bên ✓)

RSA public  = (n=3233, e=17)
RSA private = (n=3233, d=2753)   [suy ra từ p=61, q=53]
  m=65 --public--> c=2790 --private--> m'=65
  m=65 --private--> sig=588 --public--> 65  (chữ ký hợp lệ ✓)
  chữ ký giả 1857 -> xác minh ra 3 ≠ 65 ✗ bị từ chối

All assertions passed.
```

> ⚠️ **Code này để HỌC, không để DÙNG.** Thiếu padding OAEP/PSS, khoá RSA bé như hạt đậu, không chống tấn công kênh phụ. Sản phẩm thật thì dùng `node:crypto`, `libsodium`, hoặc thư viện chuẩn của hệ điều hành.

**Tự thử nghiệm:**

- Trong `rsaToy`, in thử `modPow(c, d2, n)` với `d2` sai một đơn vị — xem kết quả loạn hoàn toàn (avalanche).
- Thử `m = 2` với `e = 17`: `2¹⁷ = 131072 > 3233` nên `mod` có tác dụng. Giờ đổi `e = 3` và `m = 5`: `5³ = 125 < 3233` → bản mã **chính là** `125`, chỉ cần lấy căn bậc 3 là ra `m`. **Đó chính là lỗ hổng "m nhỏ"** ở [phần 7](#7-rsa-mổ-xẻ-từng-bước) — bạn vừa tự phá được RSA không padding.
- Trong `dhDemo`, thay `P` bằng một số nhỏ như `23` rồi viết vòng lặp brute-force tìm `a` từ `A` — thấy ngay vì sao `p` phải lớn.

---

## 13. Sai lầm thường gặp

| Sai lầm                         | Vì sao sai                                                                                           |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| ❌ Tự viết thuật toán mã hoá     | Toán đúng ≠ cài đặt đúng. Padding, timing, RNG — mỗi cái là một hố. Dùng thư viện đã được kiểm định. |
| ❌ Gửi private key "cho an toàn" | Private key **không bao giờ** rời khỏi máy. Không email, không Git, không Slack.                     |
| ❌ Dùng RSA mã hoá file lớn      | Chậm và có giới hạn kích thước. Dùng mã hoá lai.                                                     |
| ❌ Textbook RSA (không padding)  | Tất định + malleable → vỡ. Luôn dùng OAEP/PSS.                                                       |
| ❌ Dùng lại nonce/IV/`k`         | Với ECDSA: lộ private key. Với AES-GCM: lộ bản rõ.                                                   |
| ❌ Bỏ qua cảnh báo chứng chỉ     | Đó chính xác là dấu hiệu MITM đang xảy ra.                                                           |
| ❌ `random` thay vì `secrets`    | `random` là PRNG tất định, đoán được. Mật mã phải dùng CSPRNG.                                       |
| ❌ Nghĩ mã hoá = xác thực        | Mã hoá giấu nội dung, không chứng minh người gửi. Cần AEAD hoặc chữ ký.                              |
| ❌ Nghĩ "mã hoá rồi là an toàn"  | Metadata (ai nói với ai, khi nào, dài bao nhiêu) vẫn lộ hết.                                         |

---

## 14. Từ điển thuật ngữ

| Thuật ngữ                    | Giải thích                                                    |
| ---------------------------- | ------------------------------------------------------------- |
| **Symmetric encryption**     | Một khoá cho cả mã và giải mã (AES)                           |
| **Asymmetric encryption**    | Cặp khoá public/private (RSA, ECC)                            |
| **Public key**               | Khoá công khai, chia sẻ tự do, dùng để mã hoá / xác minh      |
| **Private key**              | Khoá riêng, giữ tuyệt mật, dùng để giải mã / ký               |
| **Key distribution problem** | Bài toán trao khoá an toàn qua kênh không an toàn             |
| **Trapdoor function**        | Hàm dễ tính xuôi, khó tính ngược, trừ khi biết bí mật         |
| **Integer factorization**    | Phân tích `n` thành `p × q` — nền của RSA                     |
| **Discrete logarithm**       | Tìm `a` từ `gᵃ mod p` — nền của DH và ECC                     |
| **Diffie–Hellman**           | Giao thức tạo bí mật chung mà không gửi bí mật                |
| **PFS**                      | Perfect Forward Secrecy — lộ khoá dài hạn không lộ phiên cũ   |
| **RSA**                      | Hệ mã bất đối xứng dựa trên phân tích thừa số                 |
| **ECC**                      | Mật mã đường cong elliptic — khoá ngắn, cùng độ an toàn       |
| **Padding (OAEP/PSS)**       | Thêm ngẫu nhiên có cấu trúc trước khi mã/ký                   |
| **Digital signature**        | Ký bằng private, xác minh bằng public                         |
| **MITM**                     | Man-in-the-Middle — kẻ ngồi giữa tráo public key              |
| **Certificate**              | Public key + danh tính, được CA ký                            |
| **CA**                       | Certificate Authority — bên thứ ba phát hành chứng chỉ        |
| **PKI**                      | Hạ tầng khoá công khai — hệ thống CA + chứng chỉ              |
| **Chain of trust**           | Root CA → Intermediate CA → chứng chỉ lá                      |
| **TOFU**                     | Trust On First Use — tin lần đầu, cảnh báo khi đổi (SSH)      |
| **Hybrid encryption**        | Bất đối xứng trao khoá + đối xứng mã dữ liệu                  |
| **TLS**                      | Giao thức bảo mật của HTTPS                                   |
| **AEAD**                     | Mã hoá kèm xác thực (AES-GCM, ChaCha20-Poly1305)              |
| **CSPRNG**                   | Bộ sinh ngẫu nhiên an toàn mật mã (`secrets`, `/dev/urandom`) |
| **Shor's algorithm**         | Thuật toán lượng tử phá RSA/DH/ECC                            |
| **PQC**                      | Post-Quantum Cryptography — ML-KEM, ML-DSA, SLH-DSA           |

---

## 15. Câu hỏi tự kiểm tra

1. Vì sao mã hoá đối xứng không đủ cho Internet? Nêu con số cụ thể.
2. Public key làm được gì, **không** làm được gì?
3. Giải thích ẩn dụ ổ khoá — ai giữ ổ, ai giữ chìa, ai bấm khoá?
4. "Hàm một chiều có cửa sập" là gì? Cửa sập trong RSA là thông tin nào?
5. Trong Diffie–Hellman, Eve nghe được `p, g, A, B`. Vì sao vẫn không tính được bí mật chung?
6. Perfect Forward Secrecy bảo vệ bạn khỏi tình huống nào?
7. Với `p=61, q=53, e=17`, tính `n`, `φ(n)`, `d`. Mã hoá `m=42` rồi giải mã lại.
8. Vì sao textbook RSA không dùng được? Kể 2 lỗ hổng.
9. Mã hoá và ký khác nhau chỗ nào — dùng khoá của **ai**, và trả lời câu hỏi gì?
10. Vì sao phải hash tài liệu trước khi ký?
11. Mã hoá bất đối xứng **không** chặn được MITM. Vì sao? Cần thêm gì?
12. Vì sao HTTPS không mã hoá toàn bộ traffic bằng RSA?
13. Vì sao blockchain **không cần** CA, trong khi HTTPS thì cần?
14. Máy tính lượng tử phá được thuật toán nào, không phá được thuật toán nào? Vì sao?
15. Dùng lại `k` trong ECDSA thì hậu quả là gì?

---

## Tóm tắt một trang

```
ĐỐI XỨNG (AES): 1 khoá, rất nhanh
   ✗ nhưng làm sao gửi khoá qua kênh công khai?
   ✗ n người → n(n-1)/2 khoá → không khả thi

BẤT ĐỐI XỨNG: 2 khoá liên kết toán học
   🔓 public  — phát tự do — MÃ HOÁ / XÁC MINH
   🔑 private — giữ tuyệt mật — GIẢI MÃ / KÝ
   Nền tảng: TRAPDOOR ONE-WAY FUNCTION
      RSA → phân tích thừa số   |   DH & ECC → logarit rời rạc

HAI CHIỀU, HAI MỤC ĐÍCH:
   mã bằng public NGƯỜI NHẬN   → BÍ MẬT
   ký  bằng private NGƯỜI GỬI  → XÁC THỰC + TOÀN VẸN + CHỐNG CHỐI

VẤN ĐỀ MỚI: public key này của ai?  → MITM
   HTTPS giải bằng CHỨNG CHỈ + CA + PKI
   Blockchain né hẳn: địa chỉ = hash(public key)

BẤT ĐỐI XỨNG CHẬM → MÃ HOÁ LAI
   ECDHE trao khoá phiên (+ PFS)
   → AES-GCM mã toàn bộ dữ liệu
   → chính là cái 🔒 trên trình duyệt

LƯỢNG TỬ: phá RSA/DH/ECC (Shor), KHÔNG phá AES/SHA
   → PQC: ML-KEM, ML-DSA
```

---

**Nguồn:**
- Video gốc: [Asymmetric Encryption – Simply explained](https://www.youtube.com/watch?v=AQDCe585Lnc) (Simply Explained – Savjee)
- Diffie & Hellman, *New Directions in Cryptography* (1976)
- Rivest, Shamir, Adleman, *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems* (1977)
- RFC 8446 — *The Transport Layer Security (TLS) Protocol Version 1.3*
- NIST FIPS 203/204/205 — chuẩn mật mã hậu lượng tử (2024)

**Bài liên quan:** [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md)

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. **Bài 2 – Mã hoá bất đối xứng** ← *bạn đang ở đây* — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md) — private key → địa chỉ, UTXO, seed phrase
7. [Bài 7 – Độ khó đào](lesson_7_do_kho_dao.md) — target, nBits, retarget, phân bố Poisson
8. [Bài 8 – Zero-Knowledge Proof](lesson_8_zero_knowledge_proof.md) — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](../mo_rong/lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](../mo_rong/lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](../mo_rong/lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](../mo_rong/lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
