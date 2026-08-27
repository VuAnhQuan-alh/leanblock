# Ví Bitcoin hoạt động thế nào (Public & Private Key)

> Bài học dựa trên video **"How Bitcoin Wallets Work (Public & Private Key Explained)"** (kênh *Simply Explained – Savjee*, YouTube `GSTiKjnBaes`).
> Nối tiếp trực tiếp [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md). Bài 2 dạy cặp khoá và chữ ký số ở mức lý thuyết. Bài này cho thấy Bitcoin **dùng chúng cụ thể ra sao, đến từng byte**.
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.

---

## Mục lục

1. [Ví không chứa coin](#1-ví-không-chứa-coin)
2. [Private key — một con số 256 bit](#2-private-key--một-con-số-256-bit)
3. [Public key — nhân điểm trên đường cong](#3-public-key--nhân-điểm-trên-đường-cong)
4. [Address — băm public key](#4-address--băm-public-key)
5. [Ký giao dịch](#5-ký-giao-dịch)
6. [📚 Ống dẫn đầy đủ, từng byte một](#6--ống-dẫn-đầy-đủ-từng-byte-một)
7. [📚 UTXO — vì sao ví không có "số dư"](#7--utxo--vì-sao-ví-không-có-số-dư)
8. [📚 Seed phrase & ví HD](#8--seed-phrase--ví-hd)
9. [📚 Entropy — vì sao 2^256 là không thể đoán](#9--entropy--vì-sao-2256-là-không-thể-đoán)
10. [📚 Các loại địa chỉ Bitcoin](#10--các-loại-địa-chỉ-bitcoin)
11. [Các loại ví](#11-các-loại-ví)
12. [📚 Mô hình đe doạ & sai lầm chết người](#12--mô-hình-đe-doạ--sai-lầm-chết-người)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Ví không chứa coin

Đây là hiểu nhầm phổ biến nhất, và video mở đầu bằng chính nó.

> **Ví Bitcoin KHÔNG chứa bitcoin. Nó chứa KHOÁ.**

```
        ❌ HIỂU SAI                    ✅ ĐÚNG
   ┌──────────────────┐        ┌──────────────────┐
   │   👛 VÍ          │        │   👛 VÍ          │
   │  ┌──────────┐    │        │  🔑 private key  │
   │  │ 2.5 BTC  │    │        │  🔓 public key   │
   │  └──────────┘    │        │  (chỉ có vậy)    │
   └──────────────────┘        └──────────────────┘
                                        │
                                        │ mở khoá
                                        ▼
                               ⛓️ BLOCKCHAIN
                               nơi coin THẬT SỰ nằm
```

Coin **không bao giờ rời khỏi blockchain**. Không có file nào chứa bitcoin, không có gì để "chuyển vào USB". Cái bạn cầm là **quyền chi tiêu** — và quyền đó chính là **private key**.

**Ẩn dụ chính xác hơn "ví":**

| Ẩn dụ                  | Vì sao đúng                                           |
| ---------------------- | ----------------------------------------------------- |
| **Chùm chìa khoá**     | Ví giữ chìa, tiền nằm trong két ở nơi khác            |
| **Ứng dụng ngân hàng** | App không chứa tiền, nó chứa quyền truy cập tài khoản |
| **Chữ ký + con dấu**   | Công cụ để ra lệnh, không phải bản thân tài sản       |

> 💡 Hệ quả trực tiếp: **mất điện thoại ≠ mất coin** (nếu bạn có seed phrase, khôi phục được). **Lộ private key = mất coin ngay lập tức**, dù điện thoại vẫn trong túi bạn. Thứ cần bảo vệ không phải thiết bị — mà là khoá.

---

## 2. Private key — một con số 256 bit

Private key của Bitcoin chỉ đơn giản là **một số nguyên ngẫu nhiên 256 bit**.

```
Dạng hex (64 ký tự):
  2d8f2d02bd8ee7512e9e7b074c92610834b6796c0fbfdcc609694b1ed8d4a396

Dạng thập phân:
  20588478...  (một số có 77 chữ số)
```

Không có gì đặc biệt hơn thế. Không cấu trúc, không định dạng, không cần đăng ký ở đâu.

> 💡 **Điều này có một hệ quả kỳ lạ và quan trọng:** bạn tạo ví Bitcoin **hoàn toàn offline**, không cần Internet, không cần xin phép ai, không cần thông báo cho mạng. Bạn chỉ cần **nghĩ ra một số ngẫu nhiên**. Địa chỉ đó đã tồn tại sẵn trên blockchain từ trước rồi — bạn chỉ vừa trở thành người đầu tiên biết chìa khoá của nó.
>
> Đây là hiện thân cụ thể nhất của tính **không cần xin phép (permissionless)**: không có bước "mở tài khoản", vì không có ai để xin.

### Điều kiện hợp lệ

Không phải mọi số 256 bit đều dùng được. Private key phải nằm trong khoảng:

```
1  ≤  private key  <  N

N = 0xFFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141
```

`N` là **bậc (order)** của đường cong secp256k1 — số điểm trên đường cong. Nó nhỏ hơn 2²⁵⁶ một chút, nên xác suất bốc trúng số không hợp lệ là **cực kỳ nhỏ** (~1 phần 2¹²⁸).

> ⚠️ **Tuyệt đối không tự "nghĩ ra" private key.** Không dùng ngày sinh, không dùng câu thơ, không gõ bừa bàn phím. Xem [phần 9](#9--entropy--vì-sao-2256-là-không-thể-đoán) để biết vì sao "brainwallet" luôn bị rút cạn.

---

## 3. Public key — nhân điểm trên đường cong

Từ private key, ta suy ra public key bằng **phép nhân điểm trên đường cong elliptic**:

```
   public_key  =  private_key  ×  G
                                   ↑
                        điểm gốc (generator point) — hằng số công khai,
                        ai cũng biết, giống nhau cho toàn mạng
```

Đây là phép **một chiều** đã học ở [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md):

| Chiều            | Độ khó                                                     |
| ---------------- | ---------------------------------------------------------- |
| `priv × G = pub` | **Dễ** — vài chục phép cộng điểm, xong trong micro giây    |
| `pub ÷ G = priv` | **Bất khả thi** — bài toán logarit rời rạc trên đường cong |

Bitcoin dùng đường cong **secp256k1**, phương trình:

```
y² = x³ + 7   (mod p),  với p = 2²⁵⁶ − 2³² − 977
```

> 💡 Chú ý cái tên: `secp256k1`. Ethereum cũng dùng chính đường cong này. Nhưng TLS/HTTPS lại dùng `secp256r1` (còn gọi P-256) — đường cong của NIST. Satoshi cố ý **tránh** đường cong NIST, vì tham số của nó do NSA đề xuất mà không giải thích cách chọn. secp256k1 có tham số được sinh theo cách minh bạch, kiểm chứng được.

### Hai dạng public key

```
Dạng ĐẦY ĐỦ (65 byte):    04 || x (32 byte) || y (32 byte)
Dạng NÉN    (33 byte):    02 hoặc 03 || x (32 byte)
                          ↑
                     02 nếu y chẵn, 03 nếu y lẻ
```

Vì `y² = x³ + 7`, biết `x` thì tính được `y` — chỉ còn mơ hồ ở chỗ **dấu**. Một byte tiền tố giải quyết chuyện đó, tiết kiệm 32 byte mỗi lần.

> ⚠️ **Hệ quả bất ngờ và rất thực tế:** cùng một private key, dạng nén và dạng đầy đủ cho ra **hai địa chỉ khác nhau**. Đây là nguyên nhân của rất nhiều vụ "tôi khôi phục ví nhưng số dư bằng 0" — coin nằm ở địa chỉ dạng kia. Code ở [phần 13](#13-code-minh-hoạ) minh hoạ chính xác điều này.

---

## 4. Address — băm public key

Địa chỉ **không phải** public key. Nó là public key đã qua **hai lớp băm**:

```
public key (33 byte)
      │
      ├── SHA-256      ──▶ 32 byte
      │
      ├── RIPEMD-160   ──▶ 20 byte     ← gọi chung là HASH160
      │
      ├── thêm version byte (0x00 cho mainnet)
      │
      ├── thêm 4 byte checksum = SHA256(SHA256(...))[:4]
      │
      └── mã hoá Base58Check
              ▼
      1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
```

### 📚 Lý thuyết bổ sung: vì sao lại băm, và vì sao **hai** lần

**Vì sao không dùng thẳng public key làm địa chỉ?**

| Lý do                         | Giải thích                                                                                                                                                                                                              |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ngắn hơn**                  | 33 byte → 20 byte. Địa chỉ ngắn hơn, dễ chép, tốn ít dung lượng chuỗi hơn.                                                                                                                                              |
| **Thêm một lớp bảo vệ**       | Nếu đường cong elliptic bị phá, public key **chưa từng lộ** vẫn được hash che chắn.                                                                                                                                     |
| **Chống lượng tử (một phần)** | Máy tính lượng tử phá được ECDSA ([Bài 2](lesson_2_ma_hoa_bat_doi_xung.md), thuật toán Shor), nhưng **không** phá được hash. Chừng nào bạn **chưa tiêu** từ một địa chỉ, public key chưa lộ ra chuỗi → còn được bảo vệ. |

> ⚠️ Chú ý điểm cuối cùng: **public key chỉ lộ ra khi bạn tiêu tiền lần đầu** từ địa chỉ đó. Đây là một trong những lý do kỹ thuật (không phải chỉ riêng tư) để **không dùng lại địa chỉ**: địa chỉ đã tiêu rồi thì public key đã công khai, mất đi lớp bảo vệ bằng hash.

**Vì sao SHA-256 rồi RIPEMD-160, không phải một cái?** Dùng hai họ hàm băm được thiết kế độc lập. Nếu một cái bị phá về mặt toán học, cái kia vẫn đứng. Đây là nguyên tắc **phòng thủ theo lớp** (defense in depth).

**Vì sao Base58 chứ không phải Base64?** Base58 **bỏ đi** các ký tự dễ nhìn nhầm:

```
Bỏ:  0 (số không)   O (chữ O hoa)
     I (i hoa)      l (L thường)
     + và /  (gây rắc rối khi nhấp đúp chọn, khi đưa vào URL)
```

**Vì sao có checksum?** 4 byte checksum bắt được gần như **mọi** lỗi gõ nhầm. Ví chối bỏ địa chỉ sai **trước khi** gửi, thay vì để bạn gửi tiền vào hư không vĩnh viễn.

> 🧪 [Phần 13](#13-code-minh-hoạ) có code chứng minh: đổi **một ký tự** trong địa chỉ → checksum sai → ví từ chối.

---

## 5. Ký giao dịch

Đây là lúc private key thực sự làm việc — và nó **không bao giờ rời khỏi ví**.

```
1. Bạn tạo giao dịch:  "gửi 1.5 BTC từ địa chỉ A sang địa chỉ B"
                    ↓
2. Ví KÝ bằng 🔑 private key   →  chữ ký (r, s)
                    ↓
3. Broadcast lên mạng:  giao dịch + chữ ký + 🔓 public key
                    ↓
4. MỌI node xác minh bằng 🔓 public key:
      ✓ chữ ký hợp lệ?          → đúng chủ sở hữu
      ✓ nội dung khớp chữ ký?   → chưa bị sửa
      ✓ HASH160(pubkey) == địa chỉ đang tiêu?  → đúng khoá của địa chỉ đó
```

**Điểm cốt lõi:** private key **không bao giờ được gửi đi đâu**. Nó chỉ dùng để tạo ra chữ ký, và chữ ký đó không tiết lộ gì về nó.

> 🔗 Chữ ký này còn là một **zero-knowledge proof** — xem [Bài 8](lesson_8_zero_knowledge_proof.md), phần 8.

> 🔗 Đây chính xác là **chiều thứ hai** của cặp khoá ở [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md): ký bằng private của **chính mình** → chứng minh danh tính. Không phải mã hoá — thực tế **không có gì được mã hoá** trong một giao dịch Bitcoin. Toàn bộ nội dung là công khai. Mật mã ở đây dùng cho **xác thực**, không phải **bí mật**.

### 📚 Lý thuyết bổ sung: nonce `k` — cái bẫy chết người

Mỗi lần ký ECDSA cần một số ngẫu nhiên `k` (gọi là nonce):

```
r = (k × G).x  mod N
s = k⁻¹ (z + r × priv)  mod N
```

> ⚠️ **Ký hai giao dịch khác nhau bằng CÙNG một `k` → private key bị tính ra bằng đại số cấp hai.**

Từ hai chữ ký `(r, s₁)` và `(r, s₂)` với cùng `k`:

```
k    = (z₁ − z₂) / (s₁ − s₂)     mod N
priv = (s₁ × k − z₁) / r          mod N
```

Không cần siêu máy tính. Không cần thuật toán tinh vi. **Vài phép chia.**

**Đã xảy ra trong thực tế:**

| Vụ                            | Chuyện gì                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Sony PlayStation 3 (2010)** | Sony dùng `k` **cố định** cho mọi chữ ký firmware. Nhóm fail0verflow tính ra khoá ký chính của Sony. Toàn bộ chuỗi tin cậy của PS3 sụp. |
| **Ví Android (2013)**         | Lỗi bộ sinh ngẫu nhiên của Android khiến `k` lặp lại. Nhiều ví Bitcoin bị rút cạn.                                                      |

**Cách chặn: RFC 6979 — nonce tất định.** Thay vì bốc `k` ngẫu nhiên, tính:

```
k = HMAC-SHA256(private_key, message_hash)
```

Vẫn không đoán được (vì phụ thuộc private key), nhưng **không bao giờ lặp** cho hai thông điệp khác nhau, và **không phụ thuộc vào chất lượng bộ sinh ngẫu nhiên** của thiết bị. Mọi ví Bitcoin nghiêm túc đều dùng cách này.

> 🧪 [Phần 13](#13-code-minh-hoạ) có code **thực sự khôi phục private key** từ hai chữ ký dùng chung nonce. Chạy được, không phải mô tả suông.

---

## 6. 📚 Ống dẫn đầy đủ, từng byte một

Tổng hợp lại toàn bộ, kèm số byte cụ thể:

```
┌─────────────────────────────────────────────────────────────┐
│ 🎲 ENTROPY  (256 bit ngẫu nhiên từ CSPRNG)                  │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│ 🔑 PRIVATE KEY   32 byte   1 ≤ k < N                        │
│    2d8f2d02bd8ee7512e9e7b074c92610834b6796c0fbfdcc60969...  │
└───────────────────────────┬─────────────────────────────────┘
                            │  × G   (nhân điểm elliptic — MỘT CHIỀU)
┌───────────────────────────▼─────────────────────────────────┐
│ 🔓 PUBLIC KEY    33 byte nén / 65 byte đầy đủ               │
│    0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d95...   │
└───────────────────────────┬─────────────────────────────────┘
                            │  SHA-256 → RIPEMD-160  (MỘT CHIỀU)
┌───────────────────────────▼─────────────────────────────────┐
│ 🏷️  HASH160      20 byte                                    │
└───────────────────────────┬─────────────────────────────────┘
                            │  + version byte + checksum + Base58
┌───────────────────────────▼─────────────────────────────────┐
│ 📬 ADDRESS       ~34 ký tự                                  │
│    1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH                       │
└─────────────────────────────────────────────────────────────┘

   ĐI XUỐNG: dễ, tức thì, ai cũng làm được
   ĐI LÊN:   BẤT KHẢ THI ở CẢ HAI chặng (elliptic + hash)
```

> 💡 Chú ý có **hai** bức tường một chiều chồng lên nhau, dựa trên **hai bài toán khó khác nhau**: logarit rời rạc (elliptic) và preimage resistance (hash). Muốn từ địa chỉ suy ngược ra private key, bạn phải phá **cả hai**. Đây là thiết kế phòng thủ nhiều lớp rất đẹp.

---

## 7. 📚 UTXO — vì sao ví không có "số dư"

Đây là phần quan trọng nhất mà video không đi sâu, và nó giải thích rất nhiều hành vi kỳ lạ của ví Bitcoin.

### Bitcoin không có tài khoản, không có số dư

Trong ngân hàng: có một dòng `balance = 5.000.000` trong database.

Trong Bitcoin: **không tồn tại con số đó ở đâu cả.** Chỉ có các **UTXO** — *Unspent Transaction Output*, tức các khoản tiền chưa tiêu.

```
Ví của bạn quét toàn bộ blockchain, tìm mọi output khoá bằng khoá của bạn
và chưa bị tiêu:

   UTXO #1: 30.000 sat   ← từ giao dịch a1
   UTXO #2: 50.000 sat   ← từ giao dịch b2
   UTXO #3: 12.000 sat   ← từ giao dịch c3
   ─────────────────────
   "Số dư" = 92.000 sat   ← ví TỰ CỘNG, không đọc từ đâu
```

Cách hình dung đúng: bạn có một **nắm tờ tiền mệnh giá lẻ**, không phải một tài khoản.

### Hệ quả: tiền thừa (change)

Giống tiền mặt: **không xé đôi tờ tiền được**. Muốn tiêu một UTXO thì phải tiêu **toàn bộ** nó.

```
Gửi 60.000 sat, phí 1.000 sat:

  ĐẦU VÀO:  UTXO #2 (50.000) + UTXO #1 (30.000)  =  80.000
  ĐẦU RA:   60.000  ──▶ địa chỉ của Bob
            19.000  ──▶ ĐỊA CHỈ CỦA CHÍNH BẠN  (tiền thừa)
            ──────
             1.000  ──▶ phí (phần chênh lệch, không cần ghi rõ)
```

> 🧪 [Phần 13](#13-code-minh-hoạ) chạy chính xác ví dụ này bằng code.

### Điều này giải thích ba chuyện

| Hiện tượng bạn từng thấy                           | Nguyên nhân                                                                                                                        |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Ví liên tục sinh địa chỉ mới**                   | Tiền thừa cần một địa chỉ để về. Ví dùng địa chỉ mới để bảo vệ riêng tư.                                                           |
| **Phí phụ thuộc số UTXO, không phụ thuộc số tiền** | Phí tính theo **kích thước byte** của giao dịch. Gộp 50 UTXO nhỏ tốn hơn nhiều so với tiêu 1 UTXO to — kể cả khi số tiền như nhau. |
| **"Bụi" (dust) không tiêu được**                   | UTXO quá nhỏ, phí để tiêu nó còn lớn hơn chính nó. Nó mắc kẹt vĩnh viễn.                                                           |

### 📚 So sánh: UTXO vs Account model

|                       | **UTXO** (Bitcoin)                | **Account** (Ethereum)            |
| --------------------- | --------------------------------- | --------------------------------- |
| Trạng thái            | Tập các output chưa tiêu          | `mapping(address => balance)`     |
| Số dư                 | Ví tự tính bằng cách cộng         | Đọc trực tiếp từ state            |
| Xử lý song song       | ✅ Dễ — các UTXO độc lập nhau      | ❌ Khó — cùng chạm vào một biến    |
| Riêng tư              | ✅ Tốt hơn — địa chỉ mới mỗi lần   | ❌ Kém — một địa chỉ dùng mãi      |
| Chống replay          | ✅ Tự nhiên — UTXO tiêu rồi là hết | ❌ Cần **nonce** cho mỗi tài khoản |
| Smart contract        | ❌ Khó biểu diễn trạng thái        | ✅ Tự nhiên                        |
| Dễ hiểu với người mới | ❌ Khó                             | ✅ Dễ                              |

> 💡 Đây là một đánh đổi thiết kế nền tảng, không phải chuyện hơn thua. UTXO tối ưu cho **tiền tệ**: song song, riêng tư, kiểm chứng đơn giản. Account model tối ưu cho **tính toán có trạng thái**: chính là thứ smart contract cần ([Bài 3](lesson_3_smart_contract.md)). Mỗi bên chọn mô hình khớp với mục tiêu của mình.

---


### 📚 Lý thuyết bổ sung: UTXO thực sự bị khoá bằng gì — Bitcoin Script

Đến đây có một mắt xích còn thiếu. Ta đã biết UTXO là "khoản tiền chưa tiêu", nhưng **cái gì khoá nó lại?**

Câu trả lời gây bất ngờ: **không phải địa chỉ.** Mỗi UTXO bị khoá bằng **một đoạn chương trình nhỏ**.

```
UTXO = { số tiền, scriptPubKey }
                      ↑
              "câu đố khoá" — điều kiện để tiêu

Muốn tiêu, bạn cung cấp scriptSig — "lời giải"
                      ↓
     Node nối hai thứ lại và CHẠY. Kết quả cuối = TRUE thì mở khoá.
```

Địa chỉ chỉ là **cách viết gọn cho người dùng** của một `scriptPubKey` chuẩn. Trên chuỗi không hề có trường "địa chỉ" — ví đọc ngược script ra để hiển thị cho bạn.

#### P2PKH — đoạn script mà địa chỉ `1...` thật sự tạo ra

```
scriptPubKey (khoá, do NGƯỜI GỬI đặt):
    OP_DUP  OP_HASH160  <hash160 20 byte>  OP_EQUALVERIFY  OP_CHECKSIG

scriptSig (mở, do NGƯỜI TIÊU cung cấp):
    <chữ ký>  <public key>
```

Bitcoin Script là **máy ngăn xếp (stack)**. Chạy từ trái sang phải:

| Bước | Lệnh               | Ngăn xếp sau đó                                 |
| ---- | ------------------ | ----------------------------------------------- |
| 1    | `<sig>` `<pubkey>` | `sig, pubkey`                                   |
| 2    | `OP_DUP`           | `sig, pubkey, pubkey`                           |
| 3    | `OP_HASH160`       | `sig, pubkey, hash160(pubkey)`                  |
| 4    | `<hash160>`        | `sig, pubkey, hash160(pubkey), hash160_yêu_cầu` |
| 5    | `OP_EQUALVERIFY`   | `sig, pubkey` — dừng ngay nếu hai hash lệch     |
| 6    | `OP_CHECKSIG`      | `TRUE` — kiểm chữ ký bằng pubkey                |

> 💡 **Giờ ba mảnh của [phần 6](#6--ống-dẫn-đầy-đủ-từng-byte-một) mới khớp vào nhau.** `OP_EQUALVERIFY` là chỗ HASH160 được dùng; `OP_CHECKSIG` là chỗ chữ ký ECDSA được dùng. Địa chỉ không "sở hữu" gì cả — nó chỉ là bản mã hoá của **một dòng điều kiện trong script**.

#### Vì sao Script cố ý bị làm yếu

[Bài 3](lesson_3_smart_contract.md) nói "Bitcoin có ngôn ngữ Script rất hạn chế". Cụ thể là:

- **Không vòng lặp.** Không `for`, không `while`, không đệ quy.
- **Không Turing-complete.** Cố ý.
- Bị giới hạn số lệnh, kích thước stack, và nhiều opcode bị Satoshi **vô hiệu hoá vĩnh viễn** (`OP_CAT`, `OP_MUL`…) sau khi phát hiện lỗi năm 2010.

Hệ quả rất đẹp: **chi phí thực thi biết trước từ chính độ dài script.**

> 💡 **Đây là lý do Bitcoin KHÔNG cần gas.** Nhớ [Bài 3](lesson_3_smart_contract.md) phần 5: Ethereum cần gas vì EVM Turing-complete nên vướng bài toán dừng. Bitcoin **né bài toán đó ngay từ thiết kế ngôn ngữ** — không có vòng lặp thì không có chương trình chạy mãi, khỏi cần đo đếm. Hai triết lý đối lập: Ethereum mua sức mạnh biểu đạt bằng gas; Bitcoin mua tính đơn giản kiểm chứng được bằng cách từ bỏ sức mạnh biểu đạt.

#### Các kiểu script thông dụng

| Kiểu          | Điều kiện mở                                    | Địa chỉ          |
| ------------- | ----------------------------------------------- | ---------------- |
| **P2PK**      | Ký đúng public key (lộ pubkey ngay)             | — (thời sơ khai) |
| **P2PKH**     | Ký đúng + pubkey khớp hash                      | `1...`           |
| **P2MS**      | m trong n chữ ký (multisig)                     | —                |
| **P2SH**      | Cung cấp script khớp hash, rồi thoả script đó   | `3...`           |
| **P2WPKH**    | Như P2PKH nhưng chữ ký nằm ở vùng witness       | `bc1q...`        |
| **P2TR**      | Chữ ký Schnorr, hoặc một nhánh trong cây script | `bc1p...`        |
| **OP_RETURN** | **Không thể tiêu** — dùng để nhúng dữ liệu      | —                |

> 💡 `OP_RETURN` chính là cách **neo hash** ở [Bài 4](lesson_4_ung_dung_blockchain.md) được thực hiện trên Bitcoin: ghi 80 byte dữ liệu vào một output cố tình không tiêu được.

#### Timelock — mảnh ghép dẫn tới Lightning

Hai opcode cho phép khoá theo **thời gian**:

- `OP_CHECKLOCKTIMEVERIFY` (CLTV) — "không tiêu được trước block/thời điểm X"
- `OP_CHECKSEQUENCEVERIFY` (CSV) — "không tiêu được trước khi trôi qua N block kể từ lúc được xác nhận"

Ghép timelock với hashlock, ta được **HTLC** (Hashed Timelock Contract): *"ai biết nghịch ảnh của hash này thì lấy tiền ngay; nếu sau N block không ai lấy, tiền trả về người gửi."*

> 💡 HTLC là **viên gạch nền của Lightning Network** và của mọi giao dịch hoán đổi xuyên chuỗi (atomic swap). Nói cách khác: Bitcoin **có** smart contract — chỉ là loại rất hẹp, có chủ đích.

---

### 📚 Lý thuyết bổ sung: transaction malleability và lý do thật sự SegWit ra đời

[Phần 10](#10--các-loại-địa-chỉ-bitcoin) mô tả địa chỉ `bc1q` là "rẻ hơn ~16%". Đó chỉ là **tác dụng phụ**. Đây là lý do thật.

#### Vấn đề: txid có thể bị đổi mà giao dịch vẫn hợp lệ

```
txid = SHA256(SHA256(toàn bộ giao dịch))
                        ↑
                  BAO GỒM CẢ scriptSig — tức là bao gồm CHỮ KÝ
```

Mà chữ ký ECDSA lại **có thể biến hình (malleable)**: với mọi chữ ký hợp lệ `(r, s)`, giá trị `(r, −s mod N)` **cũng hợp lệ y hệt**.

> 🧪 Nhìn lại code ở [phần 13](#13-code-minh-hoạ): hàm `sign()` có dòng `s < N - s ? s : N - s` kèm chú thích *low-s (BIP-62)*. **Đó chính là biện pháp chống malleability** — luôn chọn giá trị `s` nhỏ hơn trong hai giá trị hợp lệ, để chữ ký chỉ có một dạng chuẩn duy nhất.

Hậu quả: **bất kỳ ai** trên đường truyền — không cần private key — cũng có thể lật dấu `s`, phát tán lại, và giao dịch mới:

- ✅ Vẫn hợp lệ
- ✅ Vẫn chuyển đúng số tiền, đúng người nhận
- ❌ Nhưng **có txid khác**

Không ai mất tiền. Nhưng **mọi thứ tham chiếu tới txid cũ đều gãy**.

#### Vì sao điều đó nghiêm trọng

| Hậu quả                       | Chi tiết                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Chặn đứng payment channel** | Muốn mở kênh Lightning, bạn phải ký trước một giao dịch "hoàn tiền" **tham chiếu tới một giao dịch chưa được xác nhận**. Nếu txid của giao dịch đó đổi được, bản hoàn tiền thành vô giá trị → **tiền có thể bị khoá vĩnh viễn**. Lightning **không thể tồn tại** trước khi malleability được sửa |
| **Ví và sàn bị rối**          | Hệ thống theo dõi giao dịch bằng txid tưởng lệnh rút "biến mất", có nơi tự động gửi lại → chi hai lần                                                                                                                                                                                            |
| **Mt. Gox**                   | Sàn này viện dẫn malleability làm nguyên nhân mất coin (2014). Điều tra sau đó cho thấy phần lớn thất thoát đến từ chỗ khác, nhưng vụ việc khiến cả ngành chú ý tới lỗ hổng này                                                                                                                  |

#### SegWit sửa thế nào

**Segregated Witness** (tách nhân chứng, kích hoạt 2017) làm đúng một việc về mặt cấu trúc:

```
TRƯỚC:  [ inputs | scriptSig (chữ ký) | outputs ]  ──hash toàn bộ──▶ txid
                        ↑ sửa được → txid đổi

SAU:    [ inputs | outputs ]  ──hash──▶ txid   ← chữ ký KHÔNG còn ở đây
        [ witness (chữ ký) ]  ──────────────────▶ để riêng, hash riêng (wtxid)
```

Chữ ký bị **dời ra khỏi phần được dùng để tính txid**. Giờ txid chỉ phụ thuộc vào *ai gửi gì cho ai* — thứ không ai sửa được nếu không có private key.

**Kết quả: txid trở nên bất biến → Lightning Network khả thi.**

#### Bốn lợi ích kèm theo

| Lợi ích                       | Cơ chế                                                                                                                                   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Phí rẻ hơn**                | Dữ liệu witness được tính với **chiết khấu 75%** khi tính kích thước → chính là "rẻ hơn ~16%" ở [phần 10](#10--các-loại-địa-chỉ-bitcoin) |
| **Block chứa được nhiều hơn** | Giới hạn đổi từ 1 MB sang **4 triệu weight unit** — tăng dung lượng hiệu dụng mà **không cần hard fork**                                 |
| **Sửa lỗi bậc hai**           | Trước SegWit, chi phí kiểm chữ ký tăng theo **bình phương** số input → một giao dịch độc hại có thể làm cả mạng nghẽn khi kiểm chứng     |
| **Mở đường nâng cấp**         | Đánh phiên bản witness → thêm được Taproot (v1) về sau mà không phá gì                                                                   |

> 💡 **Và đây là một minh chứng kỹ thuật xuất sắc cho [phần 7 của Bài 1](lesson_1_blockchain_hoat_dong_ntn.md):** SegWit là một **soft fork**. Node cũ nhìn giao dịch SegWit thấy *"ai cũng tiêu được"* nên vẫn coi là hợp lệ — trong khi node mới áp luật chặt hơn và đòi chữ ký thật. Tương thích ngược được giữ, chuỗi không tách. Toàn bộ nâng cấp đó luồn lọt qua một khe hở được thiết kế sẵn trong luật cũ.

---

## 8. 📚 Seed phrase & ví HD

Nếu mỗi địa chỉ cần một private key riêng, và ví sinh địa chỉ mới liên tục — thì phải sao lưu **hàng nghìn** khoá? Không. Đây là lời giải.

### BIP-39: seed phrase (cụm từ khôi phục)

```
🎲 128 hoặc 256 bit entropy
        │
        ├── thêm checksum (entropy/32 bit)
        │
        ├── cắt thành từng đoạn 11 bit
        │
        └── mỗi 11 bit → tra bảng 2048 từ  (2¹¹ = 2048)
                ▼
   witch collapse practice feed shame open
   despair creek road again ice least
```

| Số từ | Entropy | Checksum |
| ----- | ------- | -------- |
| 12 từ | 128 bit | 4 bit    |
| 24 từ | 256 bit | 8 bit    |

**Vì sao dùng từ thay vì hex:**

- Người **chép tay** được mà không sai — chép 64 ký tự hex thì sai gần như chắc chắn.
- **Checksum bắt lỗi** — chép sai một từ, ví báo lỗi ngay thay vì mở ra một ví rỗng.
- Bảng từ được chọn kỹ: **4 chữ cái đầu là đủ để phân biệt** mọi từ; không có từ nào gần giống nhau.

### BIP-32: ví phân cấp tất định (HD Wallet)

```
   seed phrase (12/24 từ)
        │  PBKDF2 (2048 vòng)
        ▼
   master seed (512 bit)
        │
        ▼
   master private key + chain code
        │
        ├──▶ khoá con 0 ──▶ khoá cháu 0, 1, 2, ...
        ├──▶ khoá con 1 ──▶ ...
        └──▶ khoá con 2 ──▶ ...   (không giới hạn)
```

**"Tất định" (deterministic)** nghĩa là: cùng seed → **luôn** sinh ra đúng dãy khoá đó, theo đúng thứ tự đó, trên **bất kỳ** phần mềm ví nào tuân chuẩn.

> 💡 Đây là lý do bạn **chỉ cần sao lưu 12 từ, một lần, mãi mãi** — dù về sau ví sinh ra 10.000 địa chỉ. Và bạn khôi phục được sang ví của hãng khác, vì đây là **chuẩn mở**.

### BIP-44: đường dẫn dẫn xuất

```
m / 44' / 0' / 0' / 0 / 0
│    │     │    │    │   └── index địa chỉ (0, 1, 2, ...)
│    │     │    │    └────── 0 = địa chỉ nhận, 1 = địa chỉ tiền thừa
│    │     │    └─────────── tài khoản số mấy
│    │     └──────────────── coin type: 0 = Bitcoin, 60 = Ethereum
│    └────────────────────── theo chuẩn BIP-44
└─────────────────────────── master key

Dấu ' = hardened (dẫn xuất cứng)
```

> 💡 Chính vì `coin type` mà **cùng một seed phrase** dùng được cho Bitcoin, Ethereum, và hàng chục chuỗi khác. Ví đa chuỗi không giữ nhiều seed — nó dẫn xuất các nhánh khác nhau từ cùng một gốc.

### 📚 Extended public key và dẫn xuất cứng

BIP-32 có một tính năng rất mạnh: từ **extended public key** (`xpub`), bạn sinh được **mọi địa chỉ con** mà **không cần private key**.

Ứng dụng: một cửa hàng online cài `xpub` lên server để sinh địa chỉ nhận tiền mới cho từng đơn hàng. Server bị hack → kẻ tấn công thấy được toàn bộ địa chỉ và giao dịch, nhưng **không tiêu được đồng nào**.

> ⚠️ **Nhưng có một cái bẫy:** với dẫn xuất **không cứng**, nếu kẻ tấn công có `xpub` **và** một private key con bất kỳ, hắn tính ngược ra được **master private key** → mất toàn bộ ví.
>
> **Dẫn xuất cứng (hardened, ký hiệu `'`)** chặn điều này bằng cách đưa private key cha vào hàm dẫn xuất. Đánh đổi: nhánh hardened **không** sinh địa chỉ từ `xpub` được nữa. Đó chính là lý do đường dẫn BIP-44 hardened ở ba cấp đầu và **không** hardened ở hai cấp cuối — bạn được cả bảo mật lẫn tiện lợi, ở đúng chỗ cần mỗi thứ.

### Passphrase — "từ thứ 25"

BIP-39 cho phép thêm một mật khẩu tuỳ chọn vào seed:

```
12 từ + passphrase "abc"  →  ví A
12 từ + passphrase "xyz"  →  ví B  (hoàn toàn khác)
12 từ + không passphrase  →  ví C  (hoàn toàn khác)
```

Ứng dụng: **ví mồi (plausible deniability)**. Bị ép giao seed phrase, bạn giao 12 từ — chúng mở ra một ví thật có ít tiền. Ví chính nằm sau passphrase, và **không có cách nào chứng minh nó tồn tại**.

> ⚠️ Quên passphrase = mất sạch. Không có cơ chế khôi phục, và không có cách nào biết mình gõ đúng hay sai (mọi passphrase đều mở ra một ví hợp lệ, chỉ là ví rỗng).

---

## 9. 📚 Entropy — vì sao 2^256 là không thể đoán

Câu hỏi tự nhiên: *"nếu private key chỉ là một số ngẫu nhiên, sao không cứ dò hết?"*

```
Số private key khả dĩ ≈ 2²⁵⁶ ≈ 1,16 × 10⁷⁷
```

Để hình dung con số này:

| Đại lượng                               | Số lượng  |
| --------------------------------------- | --------- |
| Số hạt cát trên Trái Đất                | ~10¹⁹     |
| Số ngôi sao trong vũ trụ quan sát được  | ~10²⁴     |
| Số nguyên tử trên Trái Đất              | ~10⁵⁰     |
| **Số private key Bitcoin**              | **~10⁷⁷** |
| Số nguyên tử trong vũ trụ quan sát được | ~10⁸⁰     |

Nếu **mọi** người trên Trái Đất có **một tỷ** máy tính, mỗi máy thử **một nghìn tỷ** khoá mỗi giây, chạy suốt từ Big Bang đến nay — bạn mới dò được một phần **không đáng kể** của không gian khoá.

> 💡 Đây là điểm then chốt: **bảo mật Bitcoin không đến từ độ phức tạp, mà đến từ quy mô con số.** Thuật toán thì công khai, đơn giản, ai cũng cài đặt được (xem [phần 13](#13-code-minh-hoạ) — hết vài chục dòng TypeScript). Thứ không thể vượt qua là **kích thước không gian tìm kiếm**.

### Nhưng entropy phải THẬT

Toàn bộ lập luận trên **sụp đổ** nếu số của bạn không thật sự ngẫu nhiên.

| ❌ Không bao giờ                            | Vì sao                                                                                                                                                           |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Brainwallet** — hash một câu bạn nghĩ ra | Kẻ tấn công hash sẵn **mọi** câu trong mọi cuốn sách, mọi lời bài hát, mọi câu thoại phim. Bot dò brainwallet rút cạn ví trong **vài giây** sau khi có tiền vào. |
| Gõ bừa bàn phím                            | Con người **rất tệ** ở việc tạo ngẫu nhiên. Entropy thật chỉ vài chục bit.                                                                                       |
| `random.random()`                          | PRNG tất định, đoán được từ vài đầu ra. Phải dùng **CSPRNG**.                                                                                                    |
| Ví tự viết                                 | Xem [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md), phần "sai lầm thường gặp".                                                                                         |

**Nguồn entropy đúng:** `/dev/urandom`, `crypto.randomBytes` (Node), `crypto.getRandomValues` (trình duyệt), hoặc **bộ sinh ngẫu nhiên phần cứng** trong ví lạnh (thường lấy nhiễu từ mạch điện).

> ⚠️ **Ví "não" (brainwallet) là cách mất tiền nhanh nhất trong Bitcoin.** Đã có hàng nghìn ví bị rút sạch theo cách này. Một địa chỉ nổi tiếng dùng khoá là hash của `"password"` — tiền gửi vào bị lấy đi trong **cùng một block**.

---

## 10. 📚 Các loại địa chỉ Bitcoin

Bitcoin đã đổi định dạng địa chỉ vài lần. Đây là bảng để bạn nhận diện:

| Bắt đầu bằng | Tên                    | Chuẩn      | Đặc điểm                                          |
| ------------ | ---------------------- | ---------- | ------------------------------------------------- |
| `1...`       | **P2PKH** (Legacy)     | Nguyên bản | Base58Check, phí cao nhất                         |
| `3...`       | **P2SH**               | BIP-16     | Địa chỉ script — dùng cho multisig, SegWit bọc    |
| `bc1q...`    | **P2WPKH** (SegWit v0) | BIP-173    | **Bech32**, phí rẻ hơn ~16%, có checksum mạnh     |
| `bc1p...`    | **P2TR** (Taproot)     | BIP-341    | Chữ ký **Schnorr**, riêng tư hơn, gộp chữ ký được |

### Vì sao Bech32 tốt hơn Base58

|                | Base58Check   | Bech32                                                    |
| -------------- | ------------- | --------------------------------------------------------- |
| Chữ hoa/thường | Lẫn lộn       | **Chỉ một kiểu** — dễ đọc, dễ đọc chính tả qua điện thoại |
| Checksum       | Phát hiện lỗi | **Phát hiện VÀ chỉ ra vị trí lỗi** (mã BCH)               |
| Mã QR          | To hơn        | Nhỏ hơn (chỉ chữ thường → chế độ alphanumeric)            |

### Taproot & Schnorr

Nâng cấp Taproot (2021) thay ECDSA bằng **chữ ký Schnorr**, đem lại:

- **Gộp chữ ký (key aggregation)** — một ví multisig 3-trong-5 trông y hệt một ví thường trên chuỗi. Riêng tư hơn hẳn.
- **Rẻ hơn** — một chữ ký thay vì nhiều.
- **Chứng minh tuyến tính** — mở đường cho các giao thức phức tạp hơn.

> 💡 Vì sao Satoshi không dùng Schnorr ngay từ đầu dù nó tốt hơn? Vì năm 2008 Schnorr **vẫn còn trong thời hạn bằng sáng chế** (hết hạn 2008), còn ECDSA đã được chuẩn hoá rộng rãi và có thư viện kiểm chứng. Một quyết định kỹ thuật bị chi phối bởi pháp lý.

---

## 11. Các loại ví

| Loại                   | Khoá nằm ở đâu            | An toàn                 | Tiện | Dùng cho                   |
| ---------------------- | ------------------------- | ----------------------- | ---- | -------------------------- |
| **Ví sàn** (custodial) | **Người khác giữ**        | ⚠️ Không phải ví của bạn | ⭐⭐⭐  | Giao dịch ngắn hạn         |
| **Ví nóng** (hot)      | App trên máy có mạng      | ⭐⭐                      | ⭐⭐⭐  | Chi tiêu hàng ngày, số nhỏ |
| **Ví lạnh** (hardware) | Chip chuyên dụng, offline | ⭐⭐⭐⭐                    | ⭐⭐   | Tiết kiệm dài hạn          |
| **Ví giấy**            | In ra giấy                | ⭐⭐⭐                     | ⭐    | Lưu trữ rất dài, hiếm dùng |
| **Multisig**           | Nhiều khoá, cần m-trong-n | ⭐⭐⭐⭐⭐                   | ⭐    | Số tiền lớn, quỹ tổ chức   |

### Ví cứng hoạt động thế nào

```
   💻 Máy tính (có thể đã nhiễm mã độc)
        │  gửi giao dịch CHƯA KÝ
        ▼
   🔒 VÍ CỨNG
        ├── private key nằm trong SECURE ELEMENT, KHÔNG BAO GIỜ đi ra
        ├── HIỂN THỊ nội dung giao dịch lên MÀN HÌNH CỦA CHÍNH NÓ
        ├── bạn ĐỌC TRÊN MÀN HÌNH ĐÓ và bấm nút xác nhận vật lý
        └── ký bên trong chip
        │  trả về CHỮ KÝ
        ▼
   💻 Máy tính broadcast lên mạng
```

> 💡 **Cái màn hình nhỏ đó mới là tính năng quan trọng nhất**, không phải con chip. Nếu bạn xác nhận địa chỉ trên **màn hình máy tính**, mã độc tráo địa chỉ được. Màn hình ví cứng là một **kênh tin cậy độc lập** — nó hiển thị đúng cái sắp được ký, không phải cái máy tính nói. **Luôn đối chiếu địa chỉ trên màn hình thiết bị.**

### "Not your keys, not your coins"

Để coin trên sàn = bạn **không** sở hữu coin, bạn có một **lời hứa** của sàn. Bạn quay lại đúng mô hình tin cậy mà blockchain sinh ra để loại bỏ.

Mt. Gox (2014, 850.000 BTC), QuadrigaCX (2019), FTX (2022) — mỗi vụ là hàng tỷ USD người dùng mất, và mỗi vụ đều là cùng một bài học.

---

## 12. 📚 Mô hình đe doạ & sai lầm chết người

### Hai rủi ro đối nghịch nhau

```
        MẤT KHOÁ                    LỘ KHOÁ
   (quên, hỏng, chết)         (hack, lừa đảo, trộm)
           │                          │
           ▼                          ▼
   Cần NHIỀU bản sao          Cần ÍT bản sao
           └──────────┬───────────────┘
                      ▼
          Mọi thiết kế bảo mật ví là
          một điểm CÂN BẰNG giữa hai cái này
```

Đây là lý do không có "cách sao lưu tốt nhất" — chỉ có cách phù hợp với **mô hình đe doạ của bạn**. Người sợ hoả hoạn và người sợ bị trộm cần hai giải pháp khác nhau.

### Bảng sai lầm

| Sai lầm                                       | Hậu quả                                               | Cách đúng                                            |
| --------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| Chụp ảnh seed phrase                          | Tự động đồng bộ lên cloud → cloud bị hack → mất sạch  | Chép **tay** lên giấy, hoặc khắc lên thép            |
| Gõ seed vào máy tính                          | Keylogger, clipboard malware                          | Chỉ nhập trên **thiết bị ví cứng**                   |
| Nhập seed vào web "khôi phục ví"              | **Lừa đảo 100%** — không có ngoại lệ                  | Ví thật **không bao giờ** hỏi seed qua web           |
| Chỉ có 1 bản sao seed                         | Cháy, lụt, mất → mất vĩnh viễn                        | 2–3 bản, cất ở **nơi địa lý khác nhau**              |
| Cất seed cùng chỗ với ví cứng                 | Trộm lấy được cả hai                                  | Tách riêng                                           |
| Mua ví cứng từ chợ mạng                       | Thiết bị bị can thiệp, seed đã được kẻ bán biết trước | Mua **trực tiếp từ hãng**                            |
| Không đối chiếu địa chỉ trên màn hình ví cứng | Clipboard malware tráo địa chỉ                        | **Luôn** đọc trên màn hình thiết bị                  |
| Dùng lại một địa chỉ mãi                      | Lộ toàn bộ lịch sử tài chính; lộ public key           | Để ví tự sinh địa chỉ mới                            |
| Không có kế hoạch thừa kế                     | Bạn chết → coin biến mất vĩnh viễn                    | Multisig, hoặc di chúc có hướng dẫn (không kèm seed) |

### 📚 Những mối đe doạ mà mật mã không cứu được

| Đe doạ                  | Mô tả                                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clipboard malware**   | Bạn copy địa chỉ, mã độc dán vào địa chỉ của kẻ tấn công. Địa chỉ dài nên bạn không để ý.                                                         |
| **App ví giả**          | App trên store trông y hệt ví thật, gửi seed về server kẻ tấn công.                                                                               |
| **Phishing**            | "Ví của bạn có vấn đề, nhập seed để khôi phục."                                                                                                   |
| **Address poisoning**   | Kẻ tấn công gửi giao dịch 0 đồng từ một địa chỉ **có vài ký tự đầu/cuối giống** địa chỉ bạn hay dùng, hy vọng bạn copy nhầm từ lịch sử giao dịch. |
| **Tấn công cờ lê 5 đô** | Không hack gì cả — chỉ dùng bạo lực bắt bạn giao khoá. Chống bằng multisig + passphrase + không khoe tài sản.                                     |

> 💡 **Nhận xét quan trọng:** không mối đe doạ nào ở trên tấn công vào **mật mã**. ECDSA chưa từng bị phá. Tiền bị mất luôn qua **con người, giao diện, và quy trình** — chưa bao giờ qua toán học.
>
> Đây là chủ đề lặp lại suốt cả khoá học: [Bài 3](lesson_3_smart_contract.md) — bug ở code, không ở EVM; [Bài 4](lesson_4_ung_dung_blockchain.md) — vấn đề chặng cuối, không ở chuỗi; [Bài 5](lesson_5_proof_of_stake.md) — rủi ro ở staking pool, không ở thuật toán. **Phần toán học luôn là phần vững nhất của hệ thống. Mắt xích yếu luôn nằm ở chỗ con người chạm vào.**

---

## 13. Code minh hoạ

Toàn bộ ống dẫn của ví Bitcoin — ECDSA trên secp256k1 viết từ đầu — bằng **thư viện chuẩn của Node**. Không gói ngoài. Đã chạy, khớp **test vector công khai** của Bitcoin.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// wallet.ts — Ví Bitcoin từ số 0: private key -> public key -> address,
// ký & xác minh, và mô hình UTXO. Chỉ dùng thư viện chuẩn Node.
// KHÔNG DÙNG CHO TIỀN THẬT.   Chạy: node wallet.ts
import { createHash, randomBytes } from "node:crypto";
import { strict as assert } from "node:assert";

// ---------- số học modulo ----------
/** Luôn trả về KHÔNG ÂM. TS khác Python: (-5n % 3n) === -2n, còn Python ra 1. */
const mod = (a: bigint, m: bigint): bigint => ((a % m) + m) % m;

/** Nghịch đảo modulo (Euclid mở rộng) = pow(a, -1, m) của Python. */
function modInv(a: bigint, m: bigint): bigint {
  let [r0, r1] = [mod(a, m), m], [s0, s1] = [1n, 0n];
  while (r1 !== 0n) {
    const q = r0 / r1;
    [r0, r1] = [r1, r0 - q * r1];
    [s0, s1] = [s1, s0 - q * s1];
  }
  assert(r0 === 1n, "khong ton tai nghich dao");
  return mod(s0, m);
}

// ---------- Đường cong secp256k1 (Bitcoin) ----------
const P = 2n ** 256n - 2n ** 32n - 977n;
const N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141n;
const G: Point = [
  0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798n,
  0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8n,
];
type Point = [bigint, bigint] | null;

function add(p: Point, q: Point): Point {
  if (p === null) return q;
  if (q === null) return p;
  if (p[0] === q[0] && mod(p[1] + q[1], P) === 0n) return null;
  const lam = p[0] === q[0] && p[1] === q[1]
    ? mod(3n * p[0] * p[0] * modInv(2n * p[1], P), P)
    : mod((q[1] - p[1]) * modInv(q[0] - p[0], P), P);
  const x = mod(lam * lam - p[0] - q[0], P);
  return [x, mod(lam * (p[0] - x) - p[1], P)];
}

/** Nhân điểm — phép MỘT CHIỀU: dễ tính k*G, không tìm ngược được k. */
function mul(k: bigint, p: Point = G): Point {
  let r: Point = null, cur = p;
  while (k > 0n) {
    if (k & 1n) r = add(r, cur);
    cur = add(cur, cur);
    k >>= 1n;
  }
  return r;
}

// ---------- Băm & mã hoá ----------
const sha256 = (b: Buffer): Buffer => createHash("sha256").update(b).digest();
const hash160 = (b: Buffer): Buffer =>
  createHash("ripemd160").update(sha256(b)).digest();

const toBuf = (n: bigint, len: number): Buffer =>
  Buffer.from(n.toString(16).padStart(len * 2, "0"), "hex");
const toBig = (b: Buffer): bigint =>
  b.length ? BigInt("0x" + b.toString("hex")) : 0n;

const B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
function b58check(payload: Buffer): string {
  const data = Buffer.concat([payload, sha256(sha256(payload)).subarray(0, 4)]); // 4 byte CHECKSUM
  let n = toBig(data), out = "";
  while (n > 0n) { out = B58[Number(n % 58n)] + out; n /= 58n; }
  let zeros = 0;
  while (zeros < data.length && data[zeros] === 0) zeros++;
  return "1".repeat(zeros) + out;
}

// ---------- Ống dẫn của ví ----------
function pubkey(priv: bigint, compressed = true): Buffer {
  const [x, y] = mul(priv)!;
  return compressed
    ? Buffer.concat([Buffer.from([2 + Number(y & 1n)]), toBuf(x, 32)])
    : Buffer.concat([Buffer.from([4]), toBuf(x, 32), toBuf(y, 32)]);
}
const address = (pub: Buffer, version = 0x00): string =>
  b58check(Buffer.concat([Buffer.from([version]), hash160(pub)]));

// ---------- Chữ ký ECDSA ----------
type Sig = [bigint, bigint];
function sign(priv: bigint, msg: Buffer, k: bigint): Sig {
  const z = toBig(sha256(msg));
  const r = mod(mul(k)![0], N);
  const s = mod(modInv(k, N) * (z + r * priv), N);
  return [r, s < N - s ? s : N - s];            // low-s (BIP-62)
}
function verify(pub: Point, msg: Buffer, [r, s]: Sig): boolean {
  if (!(r >= 1n && r < N && s >= 1n && s < N)) return false;
  const z = toBig(sha256(msg));
  const w = modInv(s, N);
  const pt = add(mul(mod(z * w, N)), mul(mod(r * w, N), pub));
  return pt !== null && mod(pt[0], N) === r;
}

/** Số ngẫu nhiên mật mã trong [1, N). */
const randKey = (): bigint => mod(toBig(randomBytes(32)), N - 1n) + 1n;

// ---------- demo ----------
function demoPipeline(): void {
  console.log("=== 1. ONG DAN: private -> public -> address ===");
  const priv = 1n;                                     // test vector nổi tiếng
  const pc = pubkey(priv, true), pu = pubkey(priv, false);
  const aC = address(pc), aU = address(pu);
  console.log(`  priv (hex)      : ${priv.toString(16).padStart(64, "0")}`);
  console.log(`  pub  nen  (33B) : ${pc.toString("hex")}`);
  console.log(`  pub  day  (65B) : ${pu.toString("hex").slice(0, 32)}...`);
  console.log(`  address nen     : ${aC}`);
  console.log(`  address day     : ${aU}`);
  assert.equal(aC, "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH");
  assert.equal(aU, "1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm");
  console.log("  ✓ khop test vector cong khai cua Bitcoin");
  console.log("  => CUNG 1 private key -> 2 DIA CHI KHAC NHAU (nen / khong nen)");
}

function demoOneway(): void {
  console.log("\n=== 2. MOT CHIEU: khong suy nguoc duoc ===");
  const priv = randKey();
  console.log(`  priv ngau nhien : ${priv.toString(16).padStart(64, "0")}`);
  console.log(`  -> address      : ${address(pubkey(priv))}`);
  const a2 = address(pubkey(priv ^ 1n));               // đổi 1 bit của private key
  console.log(`  doi 1 BIT priv  : ${a2}`);
  assert(a2 !== address(pubkey(priv)));
  console.log("  ✓ doi 1 bit -> dia chi khac hoan toan (khong the do dan)");
}

function demoChecksum(): void {
  console.log("\n=== 3. CHECKSUM: go nham 1 ky tu -> vi tu choi ===");
  const a = address(pubkey(1n));
  const typo = a.slice(0, 10) + (a[10] !== "X" ? "X" : "Y") + a.slice(11);
  const valid = (addr: string): boolean => {
    let n = 0n;
    for (const ch of addr) {
      const i = B58.indexOf(ch);
      if (i < 0) return false;
      n = n * 58n + BigInt(i);
    }
    const raw = toBuf(n, 25);
    return sha256(sha256(raw.subarray(0, 21))).subarray(0, 4).equals(raw.subarray(21));
  };
  assert(valid(a) && !valid(typo));
  console.log(`  dung : ${a}      -> hop le ✓`);
  console.log(`  nham : ${typo}      -> TU CHOI ✗ (checksum sai)`);
  console.log("  => 4 byte checksum chan ~99.999999% loi go nham");
}

function demoSign(): void {
  console.log("\n=== 4. KY & XAC MINH giao dich ===");
  const priv = randKey();
  const pub = mul(priv);
  const tx = Buffer.from("gui 1.5 BTC tu alice sang bob");
  const k = randKey();                                  // nonce PHẢI mới mỗi lần!
  const sig = sign(priv, tx, k);
  assert(verify(pub, tx, sig));
  console.log(`  tx        : ${tx.toString()}`);
  console.log(`  chu ky r  : ${sig[0].toString(16)}`);
  console.log("  xac minh bang PUBLIC key -> ✓ hop le");
  assert(!verify(pub, Buffer.from("gui 15 BTC tu alice sang mallory"), sig));
  console.log("  sua noi dung tx -> xac minh ✗ THAT BAI");
  assert(!verify(mul(randKey()), tx, sig));
  console.log("  public key khac -> xac minh ✗ THAT BAI");
}

function demoNonceReuse(): void {
  console.log("\n=== 5. BAY CHET NGUOI: dung lai nonce k ===");
  const priv = randKey();
  const k = randKey();
  const m1 = Buffer.from("giao dich A"), m2 = Buffer.from("giao dich B");
  const [r1, s1] = sign(priv, m1, k);
  const [r2, s2] = sign(priv, m2, k);
  const z1 = toBig(sha256(m1)), z2 = toBig(sha256(m2));
  assert(r1 === r2, "cung k -> cung r");
  // low-s có thể đã lật dấu => thử cả 4 tổ hợp
  for (const a of [s1, mod(-s1, N)]) {
    for (const b of [s2, mod(-s2, N)]) {
      if (mod(a - b, N) === 0n) continue;
      const kRec = mod((z1 - z2) * modInv(a - b, N), N);
      const cand = mod((a * kRec - z1) * modInv(r1, N), N);
      if (cand === priv) {
        console.log(`  ky 2 tx cung nonce -> TINH RA private key: ${cand.toString(16).padStart(64, "0")}`);
        console.log("  ✓ dung private key that. (Sony PS3, 2010)");
        return;
      }
    }
  }
  throw new Error("phai khoi phuc duoc private key");
}

function demoUtxo(): void {
  console.log("\n=== 6. UTXO: vi KHONG luu so du ===");
  // Ví chỉ có khoá. "Số dư" = tổng các output chưa tiêu trên chuỗi.
  const utxos = [
    { txid: "a1", vout: 0, sat: 30_000 },
    { txid: "b2", vout: 1, sat: 50_000 },
    { txid: "c3", vout: 0, sat: 12_000 },
  ];
  const bal = utxos.reduce((a, u) => a + u.sat, 0);
  console.log(`  3 UTXO -> so du = ${bal.toLocaleString("en-US")} sat  (tinh bang cach QUET CHUOI)`);
  assert(bal === 92_000);

  const send = 60_000, fee = 1_000;
  const chosen: typeof utxos = [];
  let acc = 0;
  for (const u of [...utxos].sort((x, y) => y.sat - x.sat)) {
    chosen.push(u); acc += u.sat;
    if (acc >= send + fee) break;
  }
  const change = acc - send - fee;
  console.log(`  gui ${send.toLocaleString("en-US")} + phi ${fee.toLocaleString("en-US")} -> chon ${chosen.length} UTXO = ${acc.toLocaleString("en-US")}`);
  console.log(`  -> output: ${send.toLocaleString("en-US")} cho bob + ${change.toLocaleString("en-US")} TRA LAI (change) cho chinh minh`);
  assert(acc === 80_000 && change === 19_000);
  console.log("  => UTXO khong 'tru bot' duoc, phai tieu HET roi tra lai tien thua");
  console.log("  => day la ly do vi tu sinh DIA CHI MOI lien tuc");
}

demoPipeline(); demoOneway(); demoChecksum();
demoSign(); demoNonceReuse(); demoUtxo();
console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
=== 1. ONG DAN: private -> public -> address ===
  priv (hex)      : 0000000000000000000000000000000000000000000000000000000000000001
  pub  nen  (33B) : 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
  pub  day  (65B) : 0479be667ef9dcbbac55a06295ce870b...
  address nen     : 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
  address day     : 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm
  ✓ khop test vector cong khai cua Bitcoin
  => CUNG 1 private key -> 2 DIA CHI KHAC NHAU (nen / khong nen)

=== 2. MOT CHIEU: khong suy nguoc duoc ===
  priv ngau nhien : 831110a4ce17201e274dd37b2a214eb49e786b645e4d315e75d3b78bd43a0fdd
  -> address      : 14wDzuZ72jQTDsTeh3BB9TrRuyJpU5RW3t
  doi 1 BIT priv  : 1Hy6gYf2nHdMD7AnxFrcjjLLQfsDPXhyiS
  ✓ doi 1 bit -> dia chi khac hoan toan (khong the do dan)

=== 3. CHECKSUM: go nham 1 ky tu -> vi tu choi ===
  dung : 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH      -> hop le ✓
  nham : 1BgGZ9tcN4Xm9KBzDn7KprQz87SZ26SAMH      -> TU CHOI ✗ (checksum sai)
  => 4 byte checksum chan ~99.999999% loi go nham

=== 4. KY & XAC MINH giao dich ===
  tx        : gui 1.5 BTC tu alice sang bob
  chu ky r  : 399b454dc1687889f97d2181f7ac962bf0b596dbf875c820b2a672377c5c1509
  xac minh bang PUBLIC key -> ✓ hop le
  sua noi dung tx -> xac minh ✗ THAT BAI
  public key khac -> xac minh ✗ THAT BAI

=== 5. BAY CHET NGUOI: dung lai nonce k ===
  ky 2 tx cung nonce -> TINH RA private key: a15310f25d94cc8d3993ba3672bd8031ad6b7b974d7680b99986b0572f8353fe
  ✓ dung private key that. (Sony PS3, 2010)

=== 6. UTXO: vi KHONG luu so du ===
  3 UTXO -> so du = 92,000 sat  (tinh bang cach QUET CHUOI)
  gui 60,000 + phi 1,000 -> chon 2 UTXO = 80,000
  -> output: 60,000 cho bob + 19,000 TRA LAI (change) cho chinh minh
  => UTXO khong 'tru bot' duoc, phai tieu HET roi tra lai tien thua
  => day la ly do vi tu sinh DIA CHI MOI lien tuc

All assertions passed.
```

**Sáu điều code này dạy:**

| Demo                  | Bài học                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| **1. Ống dẫn**        | Khớp test vector thật của Bitcoin → cài đặt đúng. Và cùng 1 khoá → **2 địa chỉ khác nhau** tuỳ dạng nén. |
| **2. Một chiều**      | Đổi **một bit** private key → địa chỉ khác hoàn toàn. Không có "gần đúng", không dò dần được.            |
| **3. Checksum**       | Sai một ký tự → ví từ chối **trước khi** gửi tiền.                                                       |
| **4. Ký/xác minh**    | Private key **không rời ví**. Sửa tx hoặc sai khoá → xác minh thất bại.                                  |
| **5. Dùng lại nonce** | **Thực sự tính ra private key** từ hai chữ ký. Đây là vụ Sony PS3, tái hiện trong 10 dòng.               |
| **6. UTXO**           | Ví **không lưu số dư**. Tiền thừa giải thích vì sao địa chỉ cứ sinh mới liên tục.                        |

> ⚠️ **Code này để HỌC.** Thiếu: RFC 6979 (nonce tất định), chống tấn công kênh phụ (thời gian thực thi phụ thuộc bit của khoá), kiểm tra điểm hợp lệ, xử lý mã hoá giao dịch thật. **Không bao giờ dùng cho tiền thật.**

**Tự thử nghiệm:**

- Thử `priv = 0` và `priv = N` — xem vì sao chúng không hợp lệ.
- Cài `k = HMAC-SHA256(priv, sha256(msg))` (RFC 6979) rồi ký cùng một tin nhắn hai lần — thấy chữ ký **giống hệt nhau**, và demo 5 không còn khai thác được.
- Trong `demoUtxo`, thêm 20 UTXO nhỏ 500 sat rồi thử gửi 60.000 — đếm số UTXO phải gộp, và nghĩ xem phí sẽ tăng thế nào. Bạn vừa gặp bài toán **coin selection** thật.
- Thử đổi `version = 0x00` thành `0x6f` — bạn vừa tạo địa chỉ **testnet** (bắt đầu bằng `m` hoặc `n`).

---

## 14. Từ điển thuật ngữ

| Thuật ngữ                        | Giải thích                                                |
| -------------------------------- | --------------------------------------------------------- |
| **Private key**                  | Số ngẫu nhiên 256 bit — quyền chi tiêu tuyệt đối          |
| **Public key**                   | `priv × G` trên đường cong; 33 byte (nén) hoặc 65 byte    |
| **Address**                      | Base58Check(version + HASH160(pubkey))                    |
| **secp256k1**                    | Đường cong elliptic Bitcoin dùng, `y² = x³ + 7`           |
| **Generator point (G)**          | Điểm gốc công khai của đường cong                         |
| **N (order)**                    | Bậc của đường cong — giới hạn trên của private key        |
| **HASH160**                      | RIPEMD-160(SHA-256(x)) — 20 byte                          |
| **Base58Check**                  | Mã hoá địa chỉ, bỏ ký tự dễ nhầm, kèm checksum            |
| **Bech32**                       | Định dạng địa chỉ SegWit (`bc1...`), checksum mạnh hơn    |
| **Compressed pubkey**            | Dạng nén 33 byte, chỉ lưu `x` + dấu của `y`               |
| **ECDSA**                        | Thuật toán chữ ký số trên đường cong elliptic             |
| **Schnorr**                      | Chữ ký của Taproot — gộp được, riêng tư hơn               |
| **Nonce (k)**                    | Số ngẫu nhiên mỗi lần ký — **không bao giờ dùng lại**     |
| **RFC 6979**                     | Sinh nonce tất định từ khoá + thông điệp                  |
| **UTXO**                         | Unspent Transaction Output — khoản tiền chưa tiêu         |
| **Change output**                | Tiền thừa trả về địa chỉ của chính mình                   |
| **Dust**                         | UTXO quá nhỏ, phí tiêu còn lớn hơn giá trị                |
| **Coin selection**               | Bài toán chọn UTXO nào để tiêu                            |
| **Satoshi (sat)**                | Đơn vị nhỏ nhất, 1 BTC = 100.000.000 sat                  |
| **Seed phrase**                  | 12/24 từ khôi phục toàn bộ ví (BIP-39)                    |
| **HD wallet**                    | Ví phân cấp tất định (BIP-32)                             |
| **Derivation path**              | Đường dẫn dẫn xuất khoá, vd `m/44'/0'/0'/0/0`             |
| **Hardened derivation**          | Dẫn xuất cứng (`'`) — chặn tấn công xpub + khoá con       |
| **xpub**                         | Extended public key — sinh địa chỉ mà không tiêu được     |
| **Passphrase**                   | "Từ thứ 25" — tạo ví ẩn từ cùng seed                      |
| **Entropy**                      | Độ ngẫu nhiên thật của nguồn sinh khoá                    |
| **CSPRNG**                       | Bộ sinh ngẫu nhiên an toàn mật mã                         |
| **Brainwallet**                  | Khoá từ câu tự nghĩ — **luôn bị rút cạn**                 |
| **Hot / cold wallet**            | Ví có mạng / ví offline                                   |
| **Custodial**                    | Người khác giữ khoá hộ bạn (sàn)                          |
| **Multisig**                     | Cần m trong n chữ ký mới tiêu được                        |
| **Secure element**               | Chip chống can thiệp trong ví cứng                        |
| **Address poisoning**            | Gửi tx 0 đồng từ địa chỉ nhìn giống, để bạn copy nhầm     |
| **P2PKH / P2SH / P2WPKH / P2TR** | Các loại địa chỉ: `1...` / `3...` / `bc1q...` / `bc1p...` |

---

## 15. Câu hỏi tự kiểm tra

1. Ví Bitcoin chứa gì? Coin nằm ở đâu?
2. Vì sao tạo ví Bitcoin không cần Internet và không cần xin phép ai?
3. Private key phải nằm trong khoảng nào? `N` là gì?
4. Viết công thức suy public key từ private key. Chiều nào dễ, chiều nào bất khả thi, và vì sao?
5. Vì sao Satoshi chọn secp256k1 thay vì đường cong NIST?
6. Public key nén và đầy đủ khác nhau thế nào? Vì sao điều này gây ra lỗi "ví rỗng sau khi khôi phục"?
7. Nêu **ba** lý do băm public key thành địa chỉ thay vì dùng thẳng.
8. Public key lộ ra chuỗi khi nào? Điều đó liên quan gì đến máy tính lượng tử?
9. Vì sao Base58 bỏ đi `0`, `O`, `I`, `l`?
10. Private key có được gửi lên mạng khi ký giao dịch không? Giải thích.
11. Chuyện gì xảy ra nếu ký hai giao dịch bằng cùng nonce `k`? Kể một vụ thật.
12. RFC 6979 chặn lỗi trên bằng cách nào?
13. Bitcoin lưu "số dư" ở đâu? Ví tính số dư thế nào?
14. Vì sao giao dịch Bitcoin luôn có "change output"? Nó giải thích hiện tượng gì bạn thấy trong ví?
15. Vì sao phí giao dịch phụ thuộc **số UTXO** chứ không phụ thuộc số tiền gửi?
16. So sánh UTXO và account model — mỗi cái tối ưu cho việc gì?
17. Vì sao seed phrase dùng **từ** thay vì hex? Nêu 3 lý do.
18. Vì sao chỉ cần sao lưu 12 từ một lần, dù ví sinh ra 10.000 địa chỉ?
19. `xpub` cho phép làm gì mà không tiêu được tiền? Tại sao dẫn xuất **cứng** lại cần thiết?
20. Passphrase BIP-39 tạo ra khả năng gì? Rủi ro là gì?
21. Vì sao brainwallet luôn bị rút cạn?
22. Tính năng quan trọng nhất của ví cứng là gì — con chip hay cái màn hình? Vì sao?
23. Nêu hai rủi ro **đối nghịch** trong việc sao lưu khoá. Vì sao không có "cách tốt nhất"?
24. Trong tất cả mối đe doạ ở [phần 12](#12--mô-hình-đe-doạ--sai-lầm-chết-người), có cái nào tấn công vào mật mã không? Điều đó nói lên gì?

---

## Tóm tắt một trang

```
VÍ KHÔNG CHỨA COIN — ví chứa KHOÁ. Coin luôn nằm trên blockchain.

ỐNG DẪN (một chiều ở CẢ HAI chặng)
   🎲 entropy 256 bit (CSPRNG!)
      → 🔑 PRIVATE KEY  32B,  1 ≤ k < N
      → × G (elliptic, MỘT CHIỀU)
      → 🔓 PUBLIC KEY  33B nén / 65B đầy đủ
      → SHA-256 → RIPEMD-160 (MỘT CHIỀU)
      → 🏷️ HASH160 20B
      → + version + checksum + Base58
      → 📬 ADDRESS  1BgGZ9tc...
   ⚠️ nén vs không nén = HAI ĐỊA CHỈ KHÁC NHAU từ cùng 1 khoá

KÝ GIAO DỊCH: private key KHÔNG BAO GIỜ rời ví
   ký bằng private của MÌNH → ai cũng xác minh bằng public
   ⚠️ NONCE k DÙNG LẠI = LỘ PRIVATE KEY (đại số cấp 2 — Sony PS3 2010)
      → RFC 6979: k = HMAC(priv, msg), tất định, không bao giờ lặp

UTXO — BITCOIN KHÔNG CÓ SỐ DƯ
   "số dư" = ví tự CỘNG các output chưa tiêu
   tiêu UTXO phải tiêu NGUYÊN VẸN → sinh CHANGE OUTPUT
   → giải thích: vì sao ví sinh địa chỉ mới liên tục
                 vì sao phí theo SỐ UTXO chứ không theo SỐ TIỀN
                 vì sao có "dust" không tiêu được

SEED PHRASE (BIP-39) + HD WALLET (BIP-32) + PATH (BIP-44)
   12/24 từ → master seed → vô hạn khoá con, TẤT ĐỊNH
   → sao lưu MỘT LẦN cho MÃI MÃI, khôi phục được sang ví hãng khác
   xpub: sinh địa chỉ mà không tiêu được | hardened: chặn xpub+child → master
   passphrase = "từ thứ 25" → ví ẩn, chối bỏ hợp lý

ENTROPY: 2²⁵⁶ ≈ 10⁷⁷ ≈ số nguyên tử trên Trái Đất × 10²⁷
   Bảo mật đến từ QUY MÔ CON SỐ, không phải độ phức tạp thuật toán
   ⚠️ BRAINWALLET LUÔN BỊ RÚT CẠN

VÍ CỨNG: quan trọng nhất là CÁI MÀN HÌNH (kênh tin cậy độc lập), không phải chip
"NOT YOUR KEYS, NOT YOUR COINS" — Mt.Gox, QuadrigaCX, FTX

💡 Không mối đe doạ thực tế nào tấn công vào MẬT MÃ.
   Tiền mất qua CON NGƯỜI, GIAO DIỆN, QUY TRÌNH.
   Toán học luôn là phần vững nhất của hệ thống.
```

---

**Nguồn:**
- Video gốc: [How Bitcoin Wallets Work (Public & Private Key Explained)](https://www.youtube.com/watch?v=GSTiKjnBaes) (Simply Explained – Savjee)
- Andreas Antonopoulos, *Mastering Bitcoin* — chương 4 (Keys & Addresses) và chương 5 (Wallets)
- BIP-32 (HD wallets), BIP-39 (mnemonic), BIP-44 (derivation path), BIP-173 (bech32), BIP-341 (Taproot)
- RFC 6979 — *Deterministic Usage of DSA and ECDSA*

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. **Bài 6 – Ví Bitcoin** ← *bạn đang ở đây* — private key → địa chỉ, UTXO, seed phrase
7. [Bài 7 – Độ khó đào](lesson_7_do_kho_dao.md) — target, nBits, retarget, phân bố Poisson
8. [Bài 8 – Zero-Knowledge Proof](lesson_8_zero_knowledge_proof.md) — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](../mo_rong/lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](../mo_rong/lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](../mo_rong/lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](../mo_rong/lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
