# Zero-Knowledge Proof (Chứng minh không tiết lộ)

> Bài học dựa trên video **"Zero Knowledge Proof – ZKP"** (kênh *Simply Explained – Savjee*, YouTube `OcmvMs4AMbM`).
> Mở rộng phần ZKP đã điểm qua ở [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) (tiết lộ chọn lọc trong danh tính số). Dùng nền tảng từ [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) (logarit rời rạc) và [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md) (secp256k1).
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.

---

## Mục lục

1. [Bài toán: chứng minh mà không tiết lộ](#1-bài-toán-chứng-minh-mà-không-tiết-lộ)
2. [Hang Ali Baba](#2-hang-ali-baba)
3. [Ba tính chất bắt buộc](#3-ba-tính-chất-bắt-buộc)
4. [📚 "Zero-knowledge" được định nghĩa bằng SIMULATOR](#4--zero-knowledge-được-định-nghĩa-bằng-simulator)
5. [📚 Schnorr — một ZKP thật, cài được trong 20 dòng](#5--schnorr--một-zkp-thật-cài-được-trong-20-dòng)
6. [📚 Proof of KNOWLEDGE — và cái máy trích xuất](#6--proof-of-knowledge--và-cái-máy-trích-xuất)
7. [Tương tác và không tương tác](#7-tương-tác-và-không-tương-tác)
8. [📚 Fiat-Shamir — và cú twist: chữ ký số CHÍNH LÀ ZKP](#8--fiat-shamir--và-cú-twist-chữ-ký-số-chính-là-zkp)
9. [zk-SNARK](#9-zk-snark)
10. [zk-STARK](#10-zk-stark)
11. [📚 Trusted setup, chất thải độc hại, và nghi lễ](#11--trusted-setup-chất-thải-độc-hại-và-nghi-lễ)
12. [📚 Bảng so sánh các hệ chứng minh](#12--bảng-so-sánh-các-hệ-chứng-minh)
13. [Ứng dụng](#13-ứng-dụng)
14. [📚 Hiểu nhầm lớn nhất: ZK ≠ riêng tư](#14--hiểu-nhầm-lớn-nhất-zk--riêng-tư)
15. [📚 Hạn chế & rủi ro](#15--hạn-chế--rủi-ro)
16. [Code minh hoạ](#16-code-minh-hoạ)
17. [Từ điển thuật ngữ](#17-từ-điển-thuật-ngữ)
18. [Câu hỏi tự kiểm tra](#18-câu-hỏi-tự-kiểm-tra)

---

## 1. Bài toán: chứng minh mà không tiết lộ

Cách chứng minh thông thường luôn kèm **rò rỉ**:

| Muốn chứng minh   | Cách thường        | Bạn lộ thêm gì                                       |
| ----------------- | ------------------ | ---------------------------------------------------- |
| Tôi đủ 18 tuổi    | Đưa CCCD           | Tên, ngày sinh chính xác, địa chỉ, số định danh, ảnh |
| Tôi có đủ tiền    | Đưa sao kê         | Toàn bộ số dư, mọi giao dịch, nơi làm việc           |
| Tôi biết mật khẩu | Gõ mật khẩu        | **Chính mật khẩu** — server giờ giữ nó               |
| Tôi là chủ ví này | Chuyển một ít tiền | Toàn bộ lịch sử giao dịch của ví                     |

Câu hỏi của ZKP:

> **Làm sao thuyết phục ai đó rằng một mệnh đề là ĐÚNG, mà không tiết lộ bất cứ điều gì ngoài chính sự thật "nó đúng"?**

Nghe như bất khả thi. Nhưng năm 1985, Goldwasser, Micali và Rackoff chứng minh là làm được — công trình sau này đem lại giải Gödel và giải Turing.

### Hai nhân vật quy ước

```
👩 PEGGY  (Prover / người chứng minh)  — biết bí mật, muốn thuyết phục
👨 VICTOR (Verifier / người xác minh)  — hoài nghi, muốn kiểm chứng
```

Peggy có thể **nói dối**. Victor có thể **tọc mạch**. Giao thức phải chống được cả hai.

---

## 2. Hang Ali Baba

Ẩn dụ kinh điển (Quisquater et al., 1989), và cũng là ẩn dụ video dùng.

```
                    ┌─────────────┐
                    │             │
              LỐI A │   🚪 CỬA    │ LỐI B
                    │   MA THUẬT  │
                    │  (cần mật   │
                    │   khẩu)     │
                    └──┬───────┬──┘
                       │       │
                       └───┬───┘
                           │
                      MIỆNG HANG
                       👨 Victor
```

Hang hình vòng, bị chặn giữa bởi một cánh cửa cần mật khẩu. Peggy khẳng định mình biết mật khẩu.

### Giao thức

```
Vòng 1:
  1. Victor quay lưng. Peggy đi vào, chọn LỐI A hoặc B tuỳ ý.
     → Victor KHÔNG biết cô đi lối nào.
  2. Victor tiến tới miệng hang, hô to: "Ra bằng lối B!"
  3. Peggy đi ra bằng lối B.
```

**Phân tích:**

| Peggy có mật khẩu? | Kết quả                                                                     |
| ------------------ | --------------------------------------------------------------------------- |
| **Có**             | Đang ở lối nào cũng mở cửa đi sang được → **luôn** ra đúng lối được yêu cầu |
| **Không**          | Chỉ ra đúng nếu **tình cờ** đã vào đúng lối đó → **50%**                    |

Một vòng thì chưa thuyết phục. Nhưng lặp lại:

```
 1 vòng  → kẻ giả mạo qua được với xác suất  50%
 5 vòng  →                                    3,1%
10 vòng  →                                    0,098%
20 vòng  →                                    0,000095%  (chưa tới 1 phần triệu)
```

> 🧪 [Phần 16](#16-code-minh-hoạ) mô phỏng 20.000 lượt và xác nhận đúng công thức `1/2ⁿ`.

### Ba nhận xét quan trọng

**1. Không bao giờ đạt 100%.** ZKP cho **độ chắc chắn theo xác suất**, không phải chứng minh toán học tuyệt đối. Nhưng `1/2¹²⁸` thì nhỏ hơn xác suất máy chủ của bạn bị thiên thạch rơi trúng ngay lúc đó.

> 💡 Tinh thần này giống hệt [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md): "đợi 6 xác nhận" cũng là độ chắc chắn theo xác suất. Trong mật mã, "đủ chắc chắn" luôn có nghĩa là **xác suất thất bại nhỏ đến mức vô nghĩa**, chứ không phải "không thể".

**2. Thứ tự các bước là bất khả xâm phạm.** Peggy phải **cam kết trước** (đi vào một lối), *rồi* Victor mới ra thử thách. Đảo thứ tự — Victor hô trước rồi Peggy mới vào — là giao thức **sụp đổ hoàn toàn**: kẻ giả mạo chỉ việc đi thẳng vào lối được yêu cầu.

**3. Victor không thể chứng minh lại cho người khác.** Nếu Victor quay video toàn bộ, người xem sẽ nghi ngờ — vì Victor và Peggy **có thể đã dàn xếp** trước các thử thách. Bằng chứng chỉ thuyết phục **người trực tiếp chọn thử thách ngẫu nhiên**. Đây gọi là **deniability** (khả năng chối bỏ), và nó không phải khiếm khuyết mà là **hệ quả trực tiếp** của tính zero-knowledge — xem [phần 4](#4--zero-knowledge-được-định-nghĩa-bằng-simulator).

---

## 3. Ba tính chất bắt buộc

Một hệ thống chỉ được gọi là ZKP khi thoả **cả ba**:

| Tính chất                          | Phát biểu                                                                                   | Bảo vệ ai                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Completeness** (đầy đủ)          | Nếu mệnh đề **đúng** và Peggy trung thực, Victor **sẽ** bị thuyết phục                      | Bảo vệ **Peggy** — người trung thực không bị từ chối oan |
| **Soundness** (đúng đắn)           | Nếu mệnh đề **sai**, Peggy gian dối **không thể** thuyết phục Victor (trừ xác suất cực nhỏ) | Bảo vệ **Victor** — không bị lừa                         |
| **Zero-knowledge** (không tiết lộ) | Victor **không học được gì** ngoài việc mệnh đề đúng                                        | Bảo vệ **bí mật của Peggy**                              |

Đối chiếu với hang Ali Baba:

```
Completeness  : biết mật khẩu → luôn ra đúng lối     → luôn qua
Soundness     : không biết    → đúng 50%/vòng        → 20 vòng gần như chắc chắn lộ
Zero-knowledge: Victor chỉ thấy Peggy bước ra đúng lối
                → KHÔNG học được một chữ nào của mật khẩu
```

> 💡 Hai tính chất đầu dễ hiểu — chúng nói về "đúng/sai". Tính chất thứ ba mới là chỗ toàn bộ cái hay nằm ở đó, và cũng là chỗ khó định nghĩa nhất. Phần tiếp theo giải quyết nó.

---

## 4. 📚 "Zero-knowledge" được định nghĩa bằng SIMULATOR

Đây là ý tưởng sâu sắc nhất của cả lĩnh vực, và video không đề cập.

### Vấn đề: "không học được gì" nghĩa là gì?

Câu này rất khó định nghĩa chặt chẽ. Victor **rõ ràng** học được một điều: *mệnh đề đúng*. Vậy làm sao phát biểu chính xác rằng anh ta không học được gì **thêm**?

### Lời giải thiên tài: định nghĩa qua mô phỏng

> **Một giao thức là zero-knowledge nếu tồn tại một "SIMULATOR" — một thuật toán KHÔNG BIẾT bí mật — có thể tạo ra những đoạn hội thoại (transcript) TRÔNG Y HỆT các đoạn hội thoại thật.**

Lập luận:

```
Nếu tôi tạo được một transcript giả, không phân biệt được với transcript thật,
MÀ KHÔNG HỀ BIẾT bí mật
        ↓
thì transcript đó KHÔNG THỂ chứa thông tin nào về bí mật
        ↓
vì nếu nó có chứa, tôi đã không tạo nổi nó
```

Nói cách khác: **transcript vô dụng, vì bạn tự chế ra được một cái y hệt mà không cần tới bí mật.**

### Cụ thể với Schnorr

Trong giao thức Schnorr ([phần 5](#5--schnorr--một-zkp-thật-cài-được-trong-20-dòng)), transcript là bộ ba `(R, c, s)` với luật kiểm tra `s·G = R + c·X`.

**Peggy thật** làm theo thứ tự: chọn `r` → `R = r·G` → nhận `c` → tính `s = r + c·x`.

**Simulator** làm **ngược thứ tự**, và không cần biết `x`:

```
1. Chọn c và s hoàn toàn NGẪU NHIÊN
2. Tính ngược:  R := s·G − c·X
3. Kiểm tra:    s·G = R + c·X  ✓  (hiển nhiên đúng, do cách xây R)
```

Transcript giả này **hợp lệ hoàn hảo** và có **phân bố xác suất giống hệt** transcript thật.

> 🧪 [Phần 16](#16-code-minh-hoạ) tạo cả hai loại transcript và chứng minh **cả hai đều qua được hàm xác minh** — trong khi cái thứ hai được tạo ra mà không hề chạm vào `x`.

### Vì sao mẹo này không phá vỡ soundness

Câu hỏi tự nhiên: *"nếu chế transcript giả dễ vậy, sao kẻ gian không dùng để lừa Victor?"*

Vì simulator phải **biết trước `c`** để tính ngược `R`. Trong giao thức thật, Victor chọn `c` **sau khi** đã nhận được `R`. Kẻ gian bị kẹt đúng thứ tự đó.

> 💡 **Đây chính là nhận xét #2 ở [phần 2](#2-hang-ali-baba), nói bằng đại số.** Toàn bộ sức mạnh của sigma protocol nằm ở **thứ tự: cam kết → thử thách → phản hồi**. Đảo thứ tự thì soundness biến mất, còn simulator thì sống nhờ đúng việc được phép đảo thứ tự đó.
>
> Và nó cũng giải thích [nhận xét #3](#2-hang-ali-baba): Victor không dùng transcript để thuyết phục người thứ ba được, vì người thứ ba biết rằng **bất kỳ ai** cũng chế ra được một transcript như vậy.

---

## 5. 📚 Schnorr — một ZKP thật, cài được trong 20 dòng

Hang Ali Baba là ẩn dụ. Đây là ZKP **thật**, đang chạy trong sản phẩm thật.

**Mệnh đề cần chứng minh:** *"Tôi biết số `x` sao cho `X = x·G"`* — tức **tôi biết private key ứng với public key này** ([Bài 6](lesson_6_vi_bitcoin.md)) — mà **không tiết lộ `x`**.

### Sigma protocol — ba bước

```
   👩 PEGGY (biết x)                          👨 VICTOR (chỉ biết X)
        │                                              │
   chọn r ngẫu nhiên                                   │
   R = r·G                                             │
        │──────────── COMMIT: R ──────────────────────▶│
        │                                              │  chọn c ngẫu nhiên
        │◀─────────── CHALLENGE: c ────────────────────│
   s = r + c·x                                         │
        │──────────── RESPONSE: s ────────────────────▶│
        │                                       kiểm tra:
        │                                       s·G  ==  R + c·X  ?
```

### Vì sao phép kiểm tra đúng

```
s·G = (r + c·x)·G
    = r·G + c·(x·G)
    = R   + c·X          ✓
```

Chỉ là phân phối phép nhân. Toàn bộ giao thức chỉ có thế.

### Vì sao `x` không bị lộ

`s = r + c·x` — Victor biết `s` và `c`, muốn tìm `x` thì phải biết `r`. Nhưng `r` là **ngẫu nhiên và bí mật**, và Victor chỉ thấy `R = r·G` — muốn lấy `r` từ đó phải giải **logarit rời rạc** ([Bài 2](lesson_2_ma_hoa_bat_doi_xung.md)).

`r` đóng vai một **tấm màn dùng một lần** (one-time mask): nó che `c·x` một cách hoàn hảo.

> ⚠️ **Và vì thế `r` PHẢI mới mỗi lần.** Dùng lại `r` cho hai thử thách khác nhau → lộ `x` ngay. Đây **chính xác** là cái bẫy nonce ECDSA ở [Bài 6](lesson_6_vi_bitcoin.md) — cùng một lỗ hổng, cùng một nguyên nhân toán học. Xem [phần 6](#6--proof-of-knowledge--và-cái-máy-trích-xuất).

---

## 6. 📚 Proof of KNOWLEDGE — và cái máy trích xuất

Có một phân biệt tinh tế mà người mới hay bỏ qua:

| Loại                   | Chứng minh điều gì                               |
| ---------------------- | ------------------------------------------------ |
| **Proof of statement** | *"Mệnh đề này đúng"* (ví dụ: "số này là hợp số") |
| **Proof of knowledge** | *"Tôi **BIẾT** một nhân chứng cho mệnh đề này"*  |

Schnorr thuộc loại thứ hai. Nhưng làm sao **chứng minh** rằng nó thật sự chứng minh được "biết"?

### Định nghĩa qua EXTRACTOR (máy trích xuất)

> **Một giao thức là proof of knowledge nếu tồn tại một "EXTRACTOR" có thể MOI RA bí mật từ bất kỳ prover nào trả lời thành công.**

Lập luận đối xứng với simulator:

```
Nếu tôi moi được bí mật ra từ Peggy
        ↓
thì Peggy CHẮC CHẮN đang giữ nó
        ↓
cô ấy không thể "may mắn" mà trả lời đúng
```

### Extractor của Schnorr

Cho Peggy trả lời **hai thử thách khác nhau** trên **cùng một commit `R`**:

```
s₁ = r + c₁·x
s₂ = r + c₂·x
────────────────  trừ nhau, r triệt tiêu:
s₁ − s₂ = (c₁ − c₂)·x

        s₁ − s₂
   x = ──────────
        c₁ − c₂
```

> 🧪 [Phần 16](#16-code-minh-hoạ) chạy đúng phép này và khôi phục **chính xác** bí mật.

**Hai mặt của cùng một đồng xu:**

| Góc nhìn      | Ý nghĩa                                                                               |
| ------------- | ------------------------------------------------------------------------------------- |
| **Lý thuyết** | Extractor tồn tại ⟹ giao thức thật sự chứng minh "biết"                               |
| **Thực tế**   | Dùng lại nonce ⟹ **mất khoá**. Sony PS3, ví Android ([Bài 6](lesson_6_vi_bitcoin.md)) |

> 💡 Chính cái làm giao thức **đúng về lý thuyết** cũng là cái làm nó **nguy hiểm khi cài sai**. Extractor là một chứng minh toán học; nó cũng là một công cụ tấn công sẵn dùng. Toán không quan tâm bạn ở phe nào.

---

## 7. Tương tác và không tương tác

|                     | **Interactive ZKP**                   | **Non-interactive ZKP (NIZK)**                |
| ------------------- | ------------------------------------- | --------------------------------------------- |
| Cách chạy           | Hỏi–đáp nhiều vòng                    | Gửi **một** bằng chứng, xong                  |
| Peggy và Victor     | Phải **online cùng lúc**              | Không cần gặp nhau                            |
| Thuyết phục được ai | **Chỉ Victor** — người chọn thử thách | **Bất kỳ ai**, bất kỳ lúc nào                 |
| Dùng lại được       | Không                                 | Có — đăng lên blockchain cho cả thế giới kiểm |
| Ví dụ               | Hang Ali Baba, Schnorr tương tác      | zk-SNARK, zk-STARK, chữ ký                    |

**Vì sao blockchain bắt buộc phải dùng loại không tương tác:** một smart contract **không thể hỏi–đáp**. Nó chỉ nhận một giao dịch, kiểm tra, và trả kết quả. Hơn nữa nó phải **tất định** ([Bài 3](lesson_3_smart_contract.md)) — không được sinh thử thách ngẫu nhiên.

---

## 8. 📚 Fiat-Shamir — và cú twist: chữ ký số CHÍNH LÀ ZKP

### Mẹo chuyển đổi

Làm sao bỏ được bước "Victor chọn thử thách ngẫu nhiên"?

**Fiat-Shamir heuristic (1986):**

> **Thay Victor bằng một hàm băm.**

```
   Tương tác:        c = do Victor chọn ngẫu nhiên
   Không tương tác:  c = HASH(R ‖ X ‖ thông_điệp)
```

Vì sao an toàn: Peggy phải cam kết `R` **trước**, mà `c` lại phụ thuộc `R`. Muốn "chọn `c` trước rồi tính ngược `R`" (mẹo của simulator) thì phải tìm được một `R` sao cho `HASH(R‖…)` ra đúng giá trị mình muốn — tức phải phá **preimage resistance** của hàm băm ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md)).

Hàm băm đóng vai một **"Victor không thiên vị, không thể mua chuộc"**, ai cũng mô phỏng lại được.

### Cú twist

Áp Fiat-Shamir vào Schnorr, ta được `(R, s)` gửi một lần, kèm thông điệp. Nhìn kỹ nó là gì:

```
proof = (R, s)   với   c = HASH(R ‖ X ‖ msg)
kiểm tra:  s·G == R + c·X
```

> **Đó chính là chữ ký Schnorr.** Cái mà Bitcoin dùng trong Taproot ([Bài 6](lesson_6_vi_bitcoin.md), phần 10).

Và đó là một nhận thức đảo ngược mọi thứ:

> **Chữ ký số KHÔNG PHẢI là họ hàng xa của ZKP. Chữ ký số CHÍNH LÀ một zero-knowledge proof không tương tác — cụ thể là bằng chứng "tôi biết private key", được gắn chặt vào một thông điệp.**

Nhìn lại [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md) và [Bài 6](lesson_6_vi_bitcoin.md) dưới ánh sáng này: mỗi lần bạn ký một giao dịch Bitcoin, bạn đang tạo một ZKP. Bạn chứng minh mình sở hữu khoá **mà không tiết lộ khoá**. Bạn đã dùng zero-knowledge proof từ đầu khoá học mà không biết.

> ⚠️ **Cảnh báo kỹ thuật:** Fiat-Shamir chỉ được chứng minh an toàn trong **Random Oracle Model** — một mô hình lý thuyết coi hàm băm là ngẫu nhiên hoàn hảo. Hàm băm thật không phải vậy. Trong thực tế chưa ai phá được, nhưng đây là một giả định, không phải định lý.
>
> Và có một cái bẫy cài đặt kinh điển: **quên đưa public key `X` vào phần băm**. Bỏ sót nó mở ra tấn công giả mạo trong ngữ cảnh nhiều khoá. Nhiều thư viện đã dính lỗi này.

---

## 9. zk-SNARK

**zk-SNARK** = *Zero-Knowledge **S**uccinct **N**on-interactive **AR**gument of **K**nowledge*.

Bóc từng chữ:

| Chữ                     | Nghĩa                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Succinct** (súc tích) | Bằng chứng **rất nhỏ** (~200 byte) và **kiểm tra rất nhanh** (mili giây) — **bất kể** phép tính được chứng minh phức tạp đến đâu |
| **Non-interactive**     | Gửi một lần, không hỏi đáp                                                                                                       |
| **ARgument**            | Chỉ an toàn trước kẻ tấn công có **tài nguyên hữu hạn** (khác "proof" tuyệt đối)                                                 |
| **of Knowledge**        | Có extractor ([phần 6](#6--proof-of-knowledge--và-cái-máy-trích-xuất))                                                           |

### Tính chất gây sốc

> Bạn có thể chứng minh *"tôi đã chạy đúng một chương trình mất 10 tiếng"*, và bằng chứng chỉ nặng **200 byte**, kiểm tra hết **10 mili giây**.

Kích thước bằng chứng gần như **không phụ thuộc** vào độ phức tạp của phép tính. Đây là thứ khiến zkRollup khả thi ([phần 13](#13-ứng-dụng)).

### 📚 Bên trong hoạt động thế nào (mức tổng quan)

```
   Chương trình / mệnh đề bạn muốn chứng minh
        │  ① ARITHMETIZATION — biến thành mạch số học
        ▼
   Mạch: chỉ gồm phép + và × trên một trường hữu hạn
        │  ② chuyển thành R1CS (hệ ràng buộc bậc 1)
        ▼
   Hệ phương trình:  (A·w) × (B·w) = (C·w)
        │  ③ QAP — mã hoá toàn bộ hệ thành ĐA THỨC
        ▼
   Một đẳng thức đa thức duy nhất
        │  ④ POLYNOMIAL COMMITMENT + kiểm tra tại MỘT điểm ngẫu nhiên
        ▼
   Bằng chứng ~200 byte
```

**Ý tưởng cốt lõi ở bước ④ — và đây là chỗ phép màu nằm:**

> **Bổ đề Schwartz–Zippel:** hai đa thức bậc `d` **khác nhau** thì cắt nhau tại **nhiều nhất `d` điểm**.
>
> Vậy nếu tôi kiểm tra chúng bằng nhau tại **một điểm ngẫu nhiên** trong một trường khổng lồ (~2²⁵⁶ phần tử), xác suất tôi bị lừa là `d / 2²⁵⁶` — nhỏ đến mức vô nghĩa.

Nói cách khác: thay vì kiểm tra **hàng triệu ràng buộc**, ta gói chúng vào một đa thức và **kiểm tra đúng một điểm**. Đó là toàn bộ nguồn gốc của chữ "succinct".

> 💡 Nhìn lại [phần 2](#2-hang-ali-baba) — cũng đúng ý tưởng ấy: **kiểm tra ngẫu nhiên vài lần thay vì kiểm tra tất cả**, và chấp nhận một xác suất sai nhỏ đến mức không đáng kể. Từ hang Ali Baba tới zk-SNARK, nguyên lý không đổi; chỉ có bộ máy toán học là phức tạp lên.

**Nhược điểm lớn nhất: cần trusted setup** — xem [phần 11](#11--trusted-setup-chất-thải-độc-hại-và-nghi-lễ).

---

## 10. zk-STARK

**zk-STARK** = *Zero-Knowledge **S**calable **T**ransparent **AR**gument of **K**nowledge*.

Hai chữ khác biệt so với SNARK:

| Chữ             | Nghĩa                                                                                  |
| --------------- | -------------------------------------------------------------------------------------- |
| **Scalable**    | Thời gian chứng minh tăng **gần tuyến tính**; thời gian kiểm tra tăng theo **logarit** |
| **Transparent** | **KHÔNG cần trusted setup** — đây là điểm bán hàng lớn nhất                            |

### Vì sao STARK không cần setup

SNARK dựa trên **ghép cặp đường cong elliptic** (elliptic curve pairing), đòi hỏi các tham số bí mật sinh ra từ trước.

STARK chỉ dựa trên **hàm băm**. Không có tham số bí mật nào để mà rò rỉ.

Hệ quả kép:

- ✅ **Không có trusted setup** → không có "chất thải độc hại" ([phần 11](#11--trusted-setup-chất-thải-độc-hại-và-nghi-lễ)).
- ✅ **Kháng lượng tử** — máy tính lượng tử phá được đường cong elliptic (thuật toán Shor, [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md)) nhưng **không phá được hàm băm**. SNARK dựa trên elliptic → **dễ tổn thương**. STARK dựa trên hash → **an toàn**.

### Cái giá

|                           | zk-SNARK            | zk-STARK                           |
| ------------------------- | ------------------- | ---------------------------------- |
| Kích thước bằng chứng     | ~200 byte           | **~40–200 KB** (lớn hơn ~1000 lần) |
| Chi phí kiểm tra on-chain | Rẻ                  | Đắt hơn nhiều                      |
| Trusted setup             | ❌ Cần               | ✅ Không                            |
| Kháng lượng tử            | ❌ Không             | ✅ Có                               |
| Độ trưởng thành           | Cao (Zcash từ 2016) | Mới hơn (StarkNet)                 |

> 💡 Đây là một đánh đổi kinh điển kiểu blockchain: **STARK đổi kích thước lấy sự tin cậy và khả năng chống lượng tử.** Không có bên nào "tốt hơn" — bạn chọn theo cái mình sợ hơn: phí on-chain, hay một nghi lễ setup có thể đã bị phá hoại.

---

## 11. 📚 Trusted setup, chất thải độc hại, và nghi lễ

Đây là điểm yếu nổi tiếng nhất của zk-SNARK, và nó đáng được hiểu cho đúng.

### Vấn đề

Để chạy zk-SNARK, cần sinh ra một bộ **tham số công khai** (Common Reference String). Quá trình sinh dùng một số **bí mật ngẫu nhiên** — thường gọi là **τ (tau)**.

```
   τ bí mật  ──▶  sinh tham số công khai  ──▶  MỌI người dùng
        │
        └── phải bị TIÊU HUỶ ngay lập tức
```

> ⚠️ **Nếu ai đó giữ lại `τ`, họ tạo được bằng chứng GIẢ cho những mệnh đề SAI — mà không ai phát hiện được.**

Trong Zcash, điều đó nghĩa là **in tiền giả vô hạn**, hoàn toàn không thể phát hiện, vì giao dịch được che kín.

`τ` được gọi là **"toxic waste" (chất thải độc hại)** — một cái tên rất đúng: phải tiêu huỷ, và không ai chứng minh được là mình đã tiêu huỷ.

### Lời giải: nghi lễ nhiều bên (MPC ceremony)

```
Người 1 tạo τ₁ → đóng góp → huỷ τ₁
Người 2 tạo τ₂ → đóng góp → huỷ τ₂
        ...
Người N tạo τ_N → đóng góp → huỷ τ_N
        ↓
   τ_cuối = τ₁ × τ₂ × ... × τ_N
```

**Chỉ cần MỘT người trung thực huỷ phần của mình là toàn bộ setup an toàn.** Muốn phá, phải mua chuộc **tất cả** người tham gia.

### Các nghi lễ thật

| Nghi lễ                            | Quy mô             | Chi tiết                                                                                                    |
| ---------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------- |
| **Zcash "The Ceremony"** (2016)    | 6 người            | Máy tính air-gapped, đốt ổ cứng, ghi hình toàn bộ, mua máy tính ngẫu nhiên tại cửa hàng để tránh bị cài sẵn |
| **Powers of Tau** (Ethereum, 2022) | **>140.000 người** | Ai cũng đóng góp được qua trình duyệt. Có người dùng nhiễu từ webcam, có người dùng tiếng ồn đường phố      |

> 💡 Nghi lễ Powers of Tau có lẽ là **thí nghiệm phối hợp tin cậy phi tập trung lớn nhất từng thực hiện**. Với 140.000 người tham gia, giả định "ít nhất một người trung thực" trở nên vững chắc đến mức gần như là hiển nhiên.

### Xu hướng: setup phổ quát

Các hệ mới hơn (**PLONK**, **Halo2**, **Marlin**) dùng **universal setup**: làm nghi lễ **một lần**, dùng cho **mọi** mạch — thay vì mỗi ứng dụng phải làm một nghi lễ riêng. **Halo2** thậm chí bỏ hẳn trusted setup.

---

## 12. 📚 Bảng so sánh các hệ chứng minh

| Hệ                  | Kích thước proof | Thời gian kiểm | Trusted setup            | Kháng lượng tử | Dùng ở                  |
| ------------------- | ---------------- | -------------- | ------------------------ | -------------- | ----------------------- |
| **Schnorr / sigma** | ~64 byte         | Rất nhanh      | Không                    | Không          | Chữ ký, Taproot         |
| **Groth16** (SNARK) | **~200 byte**    | Rất nhanh      | Cần, **riêng từng mạch** | Không          | Zcash, Tornado Cash     |
| **PLONK**           | ~500 byte        | Nhanh          | **Phổ quát**             | Không          | zkSync, Aztec           |
| **Halo2**           | ~1–5 KB          | Nhanh          | **Không cần**            | Không          | Zcash Orchard, Scroll   |
| **Bulletproofs**    | ~1–2 KB          | **Chậm**       | Không                    | Không          | Monero (range proof)    |
| **STARK**           | ~40–200 KB       | Trung bình     | **Không cần**            | **Có**         | StarkNet, Polygon Miden |

> 💡 Đọc bảng theo một trục: **bạn không thể có tất cả.** Proof nhỏ nhất (Groth16) đòi trusted setup riêng cho từng mạch. Không cần setup và kháng lượng tử (STARK) thì proof to gấp ngàn lần. Mỗi dòng là một điểm khác nhau trên cùng một đường đánh đổi.

---

## 13. Ứng dụng

### Giao dịch riêng tư

**Zcash** — chuyển tiền mà giấu **người gửi, người nhận, và số tiền**, nhưng vẫn chứng minh được:

- Người gửi thật sự sở hữu số tiền đó
- Không tiêu hai lần
- Tổng vào = tổng ra (không in tiền từ hư không)

Tất cả **không tiết lộ một con số nào**.

**Monero** dùng cách khác (ring signature + Bulletproofs cho range proof — chứng minh số tiền dương mà không lộ số tiền).

### Mở rộng quy mô — zkRollup

Đây là ứng dụng **có tác động lớn nhất hiện nay**, và nó nối thẳng vào [Bài 4](lesson_4_ung_dung_blockchain.md), phần Layer 2:

```
   L2 xử lý 10.000 giao dịch ngoài chuỗi
        ↓
   Tạo MỘT zk-proof: "tôi đã thực thi đúng cả 10.000 giao dịch này"
        ↓
   Gửi proof ~200 byte xuống L1
        ↓
   L1 kiểm tra trong vài mili giây → chấp nhận toàn bộ lô
```

Ethereum **không cần chạy lại** 10.000 giao dịch — nó chỉ kiểm một bằng chứng bé xíu. Đây là ý nghĩa thật của chữ **succinct**.

**zkSync, StarkNet, Scroll, Polygon zkEVM** đều hoạt động theo nguyên lý này.

### Danh tính & tiết lộ chọn lọc

Đúng như [Bài 4](lesson_4_ung_dung_blockchain.md) đã nêu:

| Chứng minh                      | Không tiết lộ                     |
| ------------------------------- | --------------------------------- |
| "Tôi trên 18 tuổi"              | Ngày sinh, tên, địa chỉ           |
| "Tôi là công dân nước X"        | Số hộ chiếu, nơi ở                |
| "Điểm tín dụng tôi > 700"       | Điểm chính xác, lịch sử tài chính |
| "Tôi trong danh sách được phép" | Tôi là ai trong danh sách đó      |

### Các ứng dụng khác

| Ứng dụng                | Chứng minh gì                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Proof of solvency**   | Sàn chứng minh "tôi có đủ tài sản trả cho mọi khách" mà không lộ sổ sách. **Sau vụ FTX, đây thành yêu cầu bắt buộc trong ngành.** |
| **Bỏ phiếu riêng tư**   | "Phiếu của tôi được đếm" mà không lộ bầu cho ai — giải đúng mâu thuẫn ở [Bài 4](lesson_4_ung_dung_blockchain.md), phần 6          |
| **zkML**                | "Tôi đã chạy đúng mô hình AI này" mà không lộ trọng số mô hình                                                                    |
| **zkEmail**             | "Tôi nhận được email từ domain X" bằng cách chứng minh chữ ký DKIM, mà không lộ nội dung                                          |
| **Proof of personhood** | "Tôi là một con người duy nhất" mà không lộ danh tính                                                                             |

---

## 14. 📚 Hiểu nhầm lớn nhất: ZK ≠ riêng tư

Đây là chỗ **gần như ai cũng hiểu sai**, kể cả người trong ngành.

> **Trong "zkRollup", chữ "zk" KHÔNG dùng cho mục đích riêng tư. Nó dùng cho tính SÚC TÍCH.**

zkRollup như zkSync hay Scroll:

- ✅ Dùng ZKP để **nén** việc kiểm chứng: một proof nhỏ thay cho việc chạy lại 10.000 giao dịch.
- ❌ **KHÔNG** giấu giao dịch. Mọi giao dịch trên zkSync đều **công khai**, ai cũng xem được.

Hai tính chất hoàn toàn tách rời nhau:

| Tính chất                          | Cho ta điều gì                     | Ai dùng nó          |
| ---------------------------------- | ---------------------------------- | ------------------- |
| **Succinctness** (súc tích)        | Kiểm chứng rẻ → **mở rộng quy mô** | zkRollup            |
| **Zero-knowledge** (không tiết lộ) | Giấu dữ liệu → **riêng tư**        | Zcash, Tornado Cash |

> 💡 Nhiều người trong ngành cho rằng đáng lẽ nên gọi là **"validity rollup"** thay vì "zkRollup" — vì cái được dùng là *tính hợp lệ kiểm chứng được*, không phải *tính không tiết lộ*. Cái tên đã lỡ phổ biến nên khó đổi, nhưng bạn nên hiểu đúng bản chất.
>
> Đây cũng là kiểu nhầm lẫn tên gọi giống "smart contract" ở [Bài 3](lesson_3_smart_contract.md): cái tên bám lại, dù nó mô tả sai thứ đang thực sự diễn ra.

---

## 15. 📚 Hạn chế & rủi ro

| Hạn chế                           | Chi tiết                                                                                                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chứng minh rất tốn**            | Tạo proof chậm hơn chạy phép tính gốc **100–1000 lần**. Kiểm thì rẻ — bất đối xứng cực lớn.                                                                            |
| **Bug trong mạch**                | Mạch (circuit) là code. Code có bug. Một ràng buộc thiếu → **under-constrained circuit** → chứng minh được mệnh đề sai. Cực khó phát hiện vì hệ thống vẫn "chạy đúng". |
| **Trusted setup**                 | Nếu bị phá hoại → giả mạo không thể phát hiện ([phần 11](#11--trusted-setup-chất-thải-độc-hại-và-nghi-lễ))                                                             |
| **Rất ít người kiểm được**        | "Moon math" — số người đủ trình audit mạch ZK trên toàn thế giới rất ít. Tập trung rủi ro vào vài chuyên gia.                                                          |
| **Kháng lượng tử không đồng đều** | SNARK dựa elliptic → tổn thương. STARK dựa hash → an toàn.                                                                                                             |
| **Rủi ro pháp lý**                | Công cụ riêng tư bị coi là công cụ rửa tiền. Tornado Cash bị OFAC trừng phạt 2022, lập trình viên bị truy tố.                                                          |

> 💡 **Chú ý dòng thứ hai — nó là mẫu hình quen thuộc.** Toán học của ZKP thì vững; cái vỡ là **cách người ta mã hoá bài toán thành mạch**. Y hệt [Bài 3](lesson_3_smart_contract.md) (bug ở code, không ở EVM), [Bài 4](lesson_4_ung_dung_blockchain.md) (vấn đề chặng cuối), [Bài 6](lesson_6_vi_bitcoin.md) (mất tiền qua giao diện, không qua mật mã).
>
> Bảy bài học, cùng một kết luận: **tầng toán học gần như không bao giờ là chỗ vỡ. Chỗ vỡ luôn nằm ở lớp mà con người viết ra.**

---

## 16. Code minh hoạ

Năm demo, chỉ dùng thư viện chuẩn của Node, chứng minh **cả ba tính chất** bằng code chạy được. Dùng lại secp256k1 từ [Bài 6](lesson_6_vi_bitcoin.md).

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// zkp.ts — Zero-Knowledge Proof: hang Ali Baba, giao thức Schnorr (sigma protocol),
// và Fiat-Shamir. Chứng minh CẢ BA tính chất bằng code. Chỉ dùng thư viện chuẩn Node.
// Chạy: node zkp.ts
import { createHash, randomBytes } from "node:crypto";
import { strict as assert } from "node:assert";

// ---------- nguồn bit ngẫu nhiên (gom lô cho nhanh) ----------
let pool = randomBytes(1 << 16), pi = 0, bit = 0;
function coin(): number {
  if (pi >= pool.length) { pool = randomBytes(1 << 16); pi = 0; bit = 0; }
  const b = (pool[pi] >> bit) & 1;
  if (++bit === 8) { bit = 0; pi++; }
  return b;
}

// ---------- 1. HANG ALI BABA: soundness giảm theo 1/2^n ----------
/** Peggy vào hang, Victor hô ra cửa nào. Trả về true nếu qua HẾT vòng. */
function cave(knowsPassword: boolean, rounds: number): boolean {
  for (let i = 0; i < rounds; i++) {
    const entered = coin();                 // Peggy chọn lối vào (Victor không thấy)
    const asked = coin();                   // Victor yêu cầu ra lối nào
    if (knowsPassword) continue;            // có mật khẩu -> luôn ra đúng cửa
    if (entered !== asked) return false;    // không có -> chỉ đúng khi trúng 50%
  }
  return true;
}

function demoCave(): void {
  console.log("=== 1. HANG ALI BABA ===");
  const N = 20_000;
  for (const rounds of [1, 5, 10, 20]) {
    let pass = 0;
    for (let i = 0; i < N; i++) if (cave(false, rounds)) pass++;
    const cheats = pass / N, theory = 0.5 ** rounds;
    let honest = true;
    for (let i = 0; i < 100; i++) if (!cave(true, rounds)) honest = false;
    console.log(`  ${String(rounds).padStart(2)} vong -> P(ke gia mao qua duoc) = ${cheats.toFixed(5)} (ly thuyet ${theory.toFixed(5)}) | nguoi that qua: ${honest}`);
    assert(honest, "COMPLETENESS: nguoi biet mat khau PHAI luon qua");
    assert(Math.abs(cheats - theory) < 0.02, "SOUNDNESS: phai bang 1/2^n");
  }
  console.log("  => Khong bao gio chac 100%, nhung 1/2^20 < 1 phan trieu la du");
}

// ---------- secp256k1 (dùng lại từ Bài 6) ----------
const mod = (a: bigint, m: bigint): bigint => ((a % m) + m) % m;
function modInv(a: bigint, m: bigint): bigint {
  let [r0, r1] = [mod(a, m), m], [s0, s1] = [1n, 0n];
  while (r1 !== 0n) {
    const q = r0 / r1;
    [r0, r1] = [r1, r0 - q * r1];
    [s0, s1] = [s1, s0 - q * s1];
  }
  return mod(s0, m);
}
const P = 2n ** 256n - 2n ** 32n - 977n;
const N_ = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141n;
type Point = [bigint, bigint] | null;
const G: Point = [
  0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798n,
  0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8n,
];

function padd(p: Point, q: Point): Point {
  if (p === null) return q;
  if (q === null) return p;
  if (p[0] === q[0] && mod(p[1] + q[1], P) === 0n) return null;
  const lam = p[0] === q[0] && p[1] === q[1]
    ? mod(3n * p[0] * p[0] * modInv(2n * p[1], P), P)
    : mod((q[1] - p[1]) * modInv(q[0] - p[0], P), P);
  const x = mod(lam * lam - p[0] - q[0], P);
  return [x, mod(lam * (p[0] - x) - p[1], P)];
}
function pmul(k: bigint, p: Point = G): Point {
  let r: Point = null, cur = p;
  while (k > 0n) {
    if (k & 1n) r = padd(r, cur);
    cur = padd(cur, cur);
    k >>= 1n;
  }
  return r;
}
const neg = (p: Point): Point => p === null ? null : [p[0], mod(-p[1], P)];
const eq = (a: Point, b: Point): boolean =>
  a === null || b === null ? a === b : a[0] === b[0] && a[1] === b[1];

const toBig = (b: Buffer): bigint => BigInt("0x" + b.toString("hex"));
const rand = (max: bigint): bigint => mod(toBig(randomBytes(40)), max);
const hex64 = (n: bigint): string => n.toString(16).padStart(64, "0");

// ---------- 2. SCHNORR: chứng minh biết x sao cho X = x*G ----------
type Transcript = [Point, bigint, bigint];

/** commit -> challenge -> response. Trả về (R, c, s). */
function schnorrProve(x: bigint, c?: bigint): Transcript {
  const r = rand(N_ - 1n) + 1n;
  const R = pmul(r);                            // COMMIT (không lộ gì về x)
  const ch = c ?? rand(N_);                     // CHALLENGE (do Victor chọn)
  return [R, ch, mod(r + ch * x, N_)];          // RESPONSE
}
/** Kiểm: s*G == R + c*X */
const schnorrVerify = (X: Point, R: Point, c: bigint, s: bigint): boolean =>
  eq(pmul(s), padd(R, pmul(c, X)));

function demoSchnorr(): void {
  console.log("\n=== 2. SCHNORR: chung minh 'toi biet private key' ma KHONG lo no ===");
  const x = rand(N_ - 1n) + 1n;                 // bí mật
  const X = pmul(x);                            // công khai
  console.log(`  bi mat x   : ${hex64(x)}  <- KHONG BAO GIO gui di`);
  console.log(`  cong khai X: ${hex64(X![0])}`);

  const [R, c, s] = schnorrProve(x);
  assert(schnorrVerify(X, R, c, s));
  console.log("  COMPLETENESS : nguoi biet x -> chung minh hop le ✓");

  const fakeS = rand(N_);                       // kẻ giả mạo không biết x
  assert(!schnorrVerify(X, R, c, fakeS));
  console.log("  SOUNDNESS    : doan bua s -> ✗ that bai");
}

function demoExtractor(): void {
  console.log("\n=== 3. EXTRACTOR: 'proof of KNOWLEDGE' nghia la gi ===");
  // Nếu Peggy trả lời được HAI challenge khác nhau cho CÙNG một commit R,
  // ta TÍNH RA được x -> chứng tỏ cô ấy THỰC SỰ biết x.
  const x = rand(N_ - 1n) + 1n;
  const r = rand(N_ - 1n) + 1n;
  const [c1, c2] = [11111n, 22222n];
  const s1 = mod(r + c1 * x, N_);
  const s2 = mod(r + c2 * x, N_);
  const xRec = mod((s1 - s2) * modInv(c1 - c2, N_), N_);      // trích xuất bí mật
  console.log(`  2 response cho cung 1 commit -> trich ra x = ${hex64(xRec)}`);
  assert(xRec === x);
  console.log("  ✓ dung bi mat that => giao thuc chung minh Peggy THUC SU BIET x");
  console.log("  ⚠️ cung ly do vi sao KHONG DUOC dung lai nonce (giong Bai 6!)");
}

function demoSimulator(): void {
  console.log("\n=== 4. ZERO-KNOWLEDGE: SIMULATOR — bang chung khong lo gi ===");
  // Mẹo: nếu biết TRƯỚC challenge, ta làm được transcript HỢP LỆ mà KHÔNG biết x.
  const x = rand(N_ - 1n) + 1n;
  const X = pmul(x);

  const real = schnorrProve(x);                 // transcript THẬT (Peggy biết x)
  assert(schnorrVerify(X, ...real));

  const c = rand(N_);                           // transcript GIẢ (không hề biết x!)
  const s = rand(N_);
  const R = padd(pmul(s), neg(pmul(c, X)));     // R := s*G - c*X  (giải ngược)
  const fake: Transcript = [R, c, s];
  assert(schnorrVerify(X, ...fake));

  console.log(`  transcript THAT : hop le = ${schnorrVerify(X, ...real)}`);
  console.log(`  transcript GIA  : hop le = ${schnorrVerify(X, ...fake)}   <- TAO RA MA KHONG BIET x`);
  console.log("  => transcript KHONG chua thong tin gi ve x,");
  console.log("     vi ai cung lam duoc mot cai y het ma khong can biet x.");
  console.log("  => DO CHINH LA dinh nghia hinh thuc cua 'zero-knowledge'.");
}

function demoFiatShamir(): void {
  console.log("\n=== 5. FIAT-SHAMIR: bo tuong tac, thanh NON-INTERACTIVE ===");
  const x = rand(N_ - 1n) + 1n;
  const X = pmul(x);
  const msg = Buffer.from("toi so huu dia chi nay");

  // challenge = HASH thay vì do Victor chọn  <-- MẤU CHỐT
  const chal = (R: Point, X: Point, m: Buffer): bigint =>
    mod(toBig(createHash("sha256").update(Buffer.concat([
      Buffer.from(hex64(R![0]), "hex"), Buffer.from(hex64(X![0]), "hex"), m,
    ])).digest()), N_);

  function proveNi(x: bigint, m: Buffer): [Point, bigint] {
    const r = rand(N_ - 1n) + 1n;
    const R = pmul(r);
    return [R, mod(r + chal(R, pmul(x), m) * x, N_)];
  }
  const verifyNi = (X: Point, m: Buffer, R: Point, s: bigint): boolean =>
    eq(pmul(s), padd(R, pmul(chal(R, X, m), X)));

  const [R, s] = proveNi(x, msg);
  assert(verifyNi(X, msg, R, s));
  console.log(`  proof = (R, s), ${64 + 64} ky tu hex — gui MOT LAN, khong hoi dap`);
  console.log("  xac minh: ✓");
  assert(!verifyNi(X, Buffer.from("thong diep khac"), R, s));
  console.log("  doi thong diep -> ✗ that bai (proof gan chat voi msg)");
  assert(!verifyNi(pmul(rand(N_ - 1n) + 1n), msg, R, s));
  console.log("  doi public key -> ✗ that bai");
  console.log("  => Day CHINH LA chu ky Schnorr. ZKP + Fiat-Shamir = CHU KY SO.");
}

demoCave(); demoSchnorr(); demoExtractor();
demoSimulator(); demoFiatShamir();
console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
=== 1. HANG ALI BABA ===
   1 vong -> P(ke gia mao qua duoc) = 0.49705 (ly thuyet 0.50000) | nguoi that qua: true
   5 vong -> P(ke gia mao qua duoc) = 0.03160 (ly thuyet 0.03125) | nguoi that qua: true
  10 vong -> P(ke gia mao qua duoc) = 0.00070 (ly thuyet 0.00098) | nguoi that qua: true
  20 vong -> P(ke gia mao qua duoc) = 0.00000 (ly thuyet 0.00000) | nguoi that qua: true
  => Khong bao gio chac 100%, nhung 1/2^20 < 1 phan trieu la du

=== 2. SCHNORR: chung minh 'toi biet private key' ma KHONG lo no ===
  bi mat x   : 0aa762edbdef70075f3f1f80819fbe1106fa8406fa2eae81c2bde5a1a02cd3f6  <- KHONG BAO GIO gui di
  cong khai X: 0bd38baefa67c4b02ff84030ec9fff02ee35dacfb79500921099af1e1b2eafd2
  COMPLETENESS : nguoi biet x -> chung minh hop le ✓
  SOUNDNESS    : doan bua s -> ✗ that bai

=== 3. EXTRACTOR: 'proof of KNOWLEDGE' nghia la gi ===
  2 response cho cung 1 commit -> trich ra x = 64a4f9ca7987b81919569999f137fc7c1e0d40e05d1d4dcf09a3d8f083ac6ce2
  ✓ dung bi mat that => giao thuc chung minh Peggy THUC SU BIET x
  ⚠️ cung ly do vi sao KHONG DUOC dung lai nonce (giong Bai 6!)

=== 4. ZERO-KNOWLEDGE: SIMULATOR — bang chung khong lo gi ===
  transcript THAT : hop le = true
  transcript GIA  : hop le = true   <- TAO RA MA KHONG BIET x
  => transcript KHONG chua thong tin gi ve x,
     vi ai cung lam duoc mot cai y het ma khong can biet x.
  => DO CHINH LA dinh nghia hinh thuc cua 'zero-knowledge'.

=== 5. FIAT-SHAMIR: bo tuong tac, thanh NON-INTERACTIVE ===
  proof = (R, s), 128 ky tu hex — gui MOT LAN, khong hoi dap
  xac minh: ✓
  doi thong diep -> ✗ that bai (proof gan chat voi msg)
  doi public key -> ✗ that bai
  => Day CHINH LA chu ky Schnorr. ZKP + Fiat-Shamir = CHU KY SO.

All assertions passed.
```

**Năm điều code này dạy:**

| Demo                 | Bài học                                                                                                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Hang Ali Baba** | Mô phỏng khớp `1/2ⁿ`. Chứng minh **completeness** (người thật luôn qua) và **soundness** (kẻ gian rơi theo hàm mũ) trong cùng một hàm.                                                                                     |
| **2. Schnorr**       | ZKP **thật**, chạy trên đường cong Bitcoin. Bí mật `x` **không bao giờ rời máy**.                                                                                                                                          |
| **3. Extractor**     | Định nghĩa *proof of knowledge*. Và là **cùng một phép toán** với lỗ hổng nonce ở [Bài 6](lesson_6_vi_bitcoin.md).                                                                                                         |
| **4. Simulator**     | 💥 **Điểm sáng nhất.** Tạo ra một transcript **hợp lệ hoàn toàn** mà **không hề biết `x`** → chứng minh transcript không chứa thông tin gì. Đây là *zero-knowledge* được thể hiện bằng code chạy được, không phải bằng lời. |
| **5. Fiat-Shamir**   | Thay Victor bằng hàm băm → NIZK. Và kết quả **chính là chữ ký Schnorr**.                                                                                                                                                   |

> ⚠️ **Code này để HỌC.** Thiếu: kiểm tra điểm hợp lệ, chống tấn công kênh phụ, nonce tất định (RFC 6979), gắn domain separator vào hash. Không dùng cho tiền thật.

**Tự thử nghiệm:**

- Trong `demoSimulator`, in ra phân bố của `c` và `s` trong cả hai transcript — chúng đều là ngẫu nhiên đều. Đó là ý nghĩa của *"không phân biệt được"*.
- Thử phá soundness: cho kẻ gian **biết trước** `c` rồi tự tính `R = s·G − c·X`. Nó qua được! Giờ hiểu vì sao **thứ tự cam kết → thử thách** là bất khả xâm phạm.
- Trong `proveNi`, **bỏ `X` ra khỏi phần băm** rồi thử nghĩ xem tấn công nào mở ra. Bạn vừa tái hiện một lỗi cài đặt Fiat-Shamir có thật.
- Sửa `demoExtractor` để dùng `c1 === c2` — extractor sập (chia cho 0). Đó là lý do phải là **hai thử thách khác nhau**.

---

## 17. Từ điển thuật ngữ

| Thuật ngữ                     | Giải thích                                                                                   |
| ----------------------------- | -------------------------------------------------------------------------------------------- |
| **Zero-Knowledge Proof**      | Chứng minh mệnh đề đúng mà không lộ gì thêm                                                  |
| **Prover / Peggy**            | Người chứng minh, giữ bí mật                                                                 |
| **Verifier / Victor**         | Người xác minh, hoài nghi                                                                    |
| **Witness**                   | Bí mật làm cho mệnh đề đúng                                                                  |
| **Completeness**              | Mệnh đề đúng + prover trung thực → luôn được chấp nhận                                       |
| **Soundness**                 | Mệnh đề sai → không thể thuyết phục (trừ xác suất bé)                                        |
| **Zero-knowledge**            | Verifier không học được gì ngoài "mệnh đề đúng"                                              |
| **Simulator**                 | Thuật toán tạo transcript giả mà không biết bí mật — định nghĩa hình thức của zero-knowledge |
| **Extractor**                 | Thuật toán moi bí mật từ prover — định nghĩa hình thức của *proof of knowledge*              |
| **Sigma protocol**            | Giao thức 3 bước: commit → challenge → response                                              |
| **Commitment**                | Cam kết một giá trị mà chưa tiết lộ nó                                                       |
| **Challenge**                 | Thử thách ngẫu nhiên do verifier đưa ra                                                      |
| **Fiat-Shamir**               | Thay challenge bằng hàm băm → bỏ tương tác                                                   |
| **Random Oracle Model**       | Mô hình coi hàm băm là ngẫu nhiên hoàn hảo                                                   |
| **NIZK**                      | Non-Interactive Zero-Knowledge                                                               |
| **zk-SNARK**                  | Succinct NIZK — proof rất nhỏ, cần trusted setup                                             |
| **zk-STARK**                  | Transparent + scalable — không cần setup, kháng lượng tử                                     |
| **Succinctness**              | Proof nhỏ và kiểm nhanh, bất kể phép tính lớn cỡ nào                                         |
| **Arithmetization**           | Biến chương trình thành mạch số học                                                          |
| **Circuit**                   | Mạch — biểu diễn phép tính bằng cộng và nhân                                                 |
| **R1CS**                      | Rank-1 Constraint System — dạng ràng buộc chuẩn                                              |
| **QAP**                       | Quadratic Arithmetic Program — mã hoá R1CS thành đa thức                                     |
| **Schwartz–Zippel**           | Bổ đề: đa thức khác nhau chỉ trùng ở ít điểm                                                 |
| **Polynomial commitment**     | Cam kết một đa thức, mở tại một điểm                                                         |
| **Trusted setup**             | Nghi lễ sinh tham số công khai từ bí mật                                                     |
| **Toxic waste (τ)**           | Bí mật phải huỷ; giữ lại = giả mạo được                                                      |
| **MPC ceremony**              | Nghi lễ nhiều bên; chỉ cần 1 người trung thực                                                |
| **Powers of Tau**             | Nghi lễ Ethereum, >140.000 người tham gia                                                    |
| **Universal setup**           | Setup một lần, dùng cho mọi mạch (PLONK)                                                     |
| **Groth16 / PLONK / Halo2**   | Các hệ SNARK phổ biến                                                                        |
| **Bulletproofs**              | Proof không cần setup, dùng cho range proof (Monero)                                         |
| **Range proof**               | Chứng minh một số nằm trong khoảng mà không lộ số                                            |
| **zkRollup**                  | L2 gom giao dịch, chứng minh bằng ZKP                                                        |
| **Validity rollup**           | Tên chính xác hơn của zkRollup                                                               |
| **Under-constrained circuit** | Mạch thiếu ràng buộc → chứng minh được điều sai                                              |
| **Deniability**               | Verifier không dùng transcript thuyết phục người khác được                                   |

---

## 18. Câu hỏi tự kiểm tra

1. Nêu 3 ví dụ về "chứng minh thông thường làm rò rỉ thông tin thừa".
2. Mô tả giao thức hang Ali Baba. Vì sao **một** vòng là chưa đủ?
3. Sau 20 vòng, xác suất kẻ giả mạo qua được là bao nhiêu?
4. Vì sao **thứ tự** "Peggy vào hang trước, Victor hô sau" là bất khả xâm phạm?
5. Vì sao Victor **không** dùng video ghi lại để thuyết phục người thứ ba?
6. Phát biểu 3 tính chất của ZKP. Mỗi tính chất bảo vệ **ai**?
7. Zero-knowledge được định nghĩa hình thức bằng cách nào? Trình bày lập luận.
8. Simulator của Schnorr làm gì? Vì sao nó **không** phá vỡ soundness?
9. Viết ba bước của sigma protocol Schnorr và chứng minh phép kiểm tra `s·G = R + c·X` là đúng.
10. Trong Schnorr, `r` đóng vai trò gì? Điều gì xảy ra nếu dùng lại `r`?
11. Phân biệt *proof of statement* và *proof of knowledge*.
12. Extractor của Schnorr hoạt động thế nào? Nó liên quan gì đến lỗ hổng ở [Bài 6](lesson_6_vi_bitcoin.md)?
13. Vì sao blockchain **bắt buộc** phải dùng ZKP không tương tác?
14. Fiat-Shamir thay thế cái gì bằng cái gì? Vì sao vẫn an toàn?
15. **Chữ ký Schnorr và ZKP có quan hệ gì?** Câu trả lời này thay đổi cách bạn nhìn [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md) và [Bài 6](lesson_6_vi_bitcoin.md) ra sao?
16. Bóc nghĩa từng chữ trong "zk-SNARK". Chữ nào quan trọng nhất với zkRollup?
17. Bổ đề Schwartz–Zippel nói gì? Vì sao nó là nguồn gốc của tính "succinct"?
18. Nêu **hai** ưu điểm của STARK so với SNARK, và **một** nhược điểm.
19. "Toxic waste" là gì? Chuyện gì xảy ra nếu ai đó giữ lại nó trong Zcash?
20. MPC ceremony an toàn khi nào? Powers of Tau có bao nhiêu người tham gia?
21. **Trong "zkRollup", chữ "zk" dùng cho tính chất nào?** Vì sao đây là hiểu nhầm phổ biến?
22. "Under-constrained circuit" là gì? Vì sao nó nguy hiểm và khó phát hiện?
23. Nhìn lại cả 8 bài: tầng nào của hệ thống hay vỡ nhất, và tầng nào gần như không bao giờ vỡ?

---

## Tóm tắt một trang

```
BÀI TOÁN: chứng minh mệnh đề ĐÚNG mà KHÔNG lộ gì thêm
   (Goldwasser–Micali–Rackoff 1985)

HANG ALI BABA: cam kết → thử thách → phản hồi, lặp n vòng
   kẻ giả mạo qua được với xác suất 1/2ⁿ  (20 vòng < 1 phần triệu)
   ⚠️ THỨ TỰ cam-kết-trước là bất khả xâm phạm

BA TÍNH CHẤT
   COMPLETENESS   — đúng + trung thực → luôn qua      (bảo vệ Peggy)
   SOUNDNESS      — sai → không lừa được              (bảo vệ Victor)
   ZERO-KNOWLEDGE — không học được gì thêm             (bảo vệ bí mật)

ĐỊNH NGHĨA HÌNH THỨC — bằng hai cỗ máy tưởng tượng
   SIMULATOR : tạo transcript hợp lệ mà KHÔNG biết bí mật
               → transcript không chứa thông tin gì  = ZERO-KNOWLEDGE
   EXTRACTOR : moi được bí mật từ prover thành công
               → prover THỰC SỰ biết               = PROOF OF KNOWLEDGE
   ⚠️ Extractor cũng CHÍNH LÀ tấn công nonce-reuse ở Bài 6

SCHNORR (ZKP thật, 20 dòng): chứng minh biết x với X = x·G
   R = r·G  →  c  →  s = r + c·x     kiểm: s·G == R + c·X
   r = tấm màn dùng MỘT LẦN; dùng lại r = lộ x

FIAT-SHAMIR: c = HASH(R‖X‖msg) thay vì Victor chọn → NON-INTERACTIVE
   💥 KẾT QUẢ CHÍNH LÀ CHỮ KÝ SCHNORR
   => CHỮ KÝ SỐ **LÀ** một ZKP. Bạn đã dùng ZKP từ Bài 2 mà không biết.

zk-SNARK: proof ~200 BYTE, kiểm vài ms, BẤT KỂ phép tính lớn cỡ nào
   Nguồn gốc phép màu: SCHWARTZ–ZIPPEL — kiểm đa thức tại MỘT điểm ngẫu nhiên
   ✗ cần TRUSTED SETUP → toxic waste τ → giữ lại = in tiền giả vô hình
     → MPC ceremony: chỉ cần 1/140.000 người trung thực

zk-STARK: KHÔNG cần setup + KHÁNG LƯỢNG TỬ (chỉ dựa hash)
   ✗ proof to gấp ~1000 lần

⚠️ HIỂU NHẦM LỚN NHẤT: trong "zkRollup", "zk" dùng cho SÚC TÍCH, KHÔNG phải RIÊNG TƯ
   zkSync/Scroll: giao dịch CÔNG KHAI HẾT. Nên gọi là "validity rollup".
   Riêng tư (Zcash) và mở rộng (rollup) là HAI tính chất TÁCH RỜI.

RỦI RO: prover chậm 100–1000x | UNDER-CONSTRAINED CIRCUIT | ít người audit nổi
   💡 Toán vững. Chỗ vỡ luôn ở lớp NGƯỜI VIẾT RA — đúng như Bài 3, 4, 6.
```

---

**Nguồn:**
- Video gốc: [Zero Knowledge Proof – ZKP](https://www.youtube.com/watch?v=OcmvMs4AMbM) (Simply Explained – Savjee)
- Goldwasser, Micali, Rackoff, *The Knowledge Complexity of Interactive Proof-Systems* (1985)
- Quisquater et al., *How to Explain Zero-Knowledge Protocols to Your Children* (1989) — nguồn gốc hang Ali Baba
- Fiat & Shamir, *How To Prove Yourself* (1986)
- Ben-Sasson et al., *Scalable, transparent, and post-quantum secure computational integrity* (2018) — bài báo STARK
- [zkp.science](https://zkp.science) — tổng hợp tài liệu ZKP
- [Powers of Tau ceremony](https://ceremony.ethereum.org)

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md) — private key → địa chỉ, UTXO, seed phrase
7. [Bài 7 – Độ khó đào](lesson_7_do_kho_dao.md) — target, nBits, retarget, phân bố Poisson
8. **Bài 8 – Zero-Knowledge Proof** ← *bạn đang ở đây* — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](../mo_rong/lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](../mo_rong/lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](../mo_rong/lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](../mo_rong/lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
