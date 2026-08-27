# Smart Contract (Hợp đồng thông minh)

> Bài học dựa trên video **"Smart contracts – Simply Explained"** (kênh *Simply Explained – Savjee*, YouTube `ZE2HxTmxfrI`).
> Nối tiếp [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) (phần 9 mới chỉ điểm danh smart contract) và [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) (chữ ký số — thứ cho phép bạn gọi được contract).
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.

---

## Mục lục

1. [Máy bán nước tự động — ẩn dụ gốc](#1-máy-bán-nước-tự-động--ẩn-dụ-gốc)
2. [Smart contract là gì](#2-smart-contract-là-gì)
3. [Ví dụ: gọi vốn cộng đồng](#3-ví-dụ-gọi-vốn-cộng-đồng)
4. [Chạy ở đâu — Ethereum & EVM](#4-chạy-ở-đâu--ethereum--evm)
5. [Gas — vì sao phải trả tiền cho mỗi phép tính](#5-gas--vì-sao-phải-trả-tiền-cho-mỗi-phép-tính)
6. [Tính tất định — luật sắt của smart contract](#6-tính-tất-định--luật-sắt-của-smart-contract)
7. [Hạn chế 1: không sửa được sau khi deploy](#7-hạn-chế-1-không-sửa-được-sau-khi-deploy)
8. [Hạn chế 2: không thấy thế giới bên ngoài — Oracle](#8-hạn-chế-2-không-thấy-thế-giới-bên-ngoài--oracle)
9. [Hạn chế 3: mọi thứ đều công khai](#9-hạn-chế-3-mọi-thứ-đều-công-khai)
10. [Hạn chế 4: pháp lý](#10-hạn-chế-4-pháp-lý)
11. [Lỗ hổng bảo mật kinh điển](#11-lỗ-hổng-bảo-mật-kinh-điển)
12. [Ứng dụng thực tế](#12-ứng-dụng-thực-tế)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Máy bán nước tự động — ẩn dụ gốc

Năm 1994, **Nick Szabo** — nhà khoa học máy tính kiêm luật gia — đặt ra thuật ngữ *smart contract*. Ẩn dụ của ông là **máy bán nước tự động**:

```
   Bạn                          Máy bán nước
    │                                │
    ├──── bỏ 10.000đ ───────────────▶│
    ├──── bấm nút "Coca" ───────────▶│
    │                                │ ĐIỀU KIỆN: đủ tiền + còn hàng?
    │◀─────── nhả lon Coca ──────────┤ → TỰ ĐỘNG thực thi
    │◀─────── trả lại 2.000đ ────────┤
```

Điều đặc biệt nằm ở chỗ **không có ai** trong giao dịch này:

- Không người bán, không thu ngân.
- Không cần bạn **tin** máy, cũng không cần máy **tin** bạn.
- Điều khoản ("bỏ đủ tiền thì được lon nước") được **nhúng vào phần cứng**, không nằm trên giấy.
- Không thể thương lượng, không thể lật lọng, không cần ra toà.

> **Smart contract = đưa logic "máy bán nước" đó lên blockchain, cho tài sản số.**

Chi tiết quan trọng: máy bán nước ra đời **trước** ý tưởng của Szabo hàng chục năm. Szabo không phát minh cơ chế — ông chỉ ra rằng **cơ chế đó tổng quát hoá được**, và với máy tính + mật mã, ta áp dụng được nó cho *mọi loại thoả thuận*, không chỉ nước ngọt.

---

## 2. Smart contract là gì

**Định nghĩa:** Smart contract là một **chương trình được lưu trữ trên blockchain**, tự động thực thi khi các điều kiện định trước được thoả mãn.

Ba từ khoá:

| Từ khoá              | Nghĩa                                                                            |
| -------------------- | -------------------------------------------------------------------------------- |
| **Chương trình**     | Là **code** — `if / else`, biến, hàm. Không phải văn bản pháp lý.                |
| **Trên blockchain**  | Thừa hưởng mọi tính chất: bất biến, minh bạch, phi tập trung, không thể bị chặn. |
| **Tự động thực thi** | Không ai phải bấm nút, không ai "cho phép". Điều kiện đúng → chạy.               |

### So sánh với hợp đồng truyền thống

|                    | Hợp đồng truyền thống               | Smart contract                                 |
| ------------------ | ----------------------------------- | ---------------------------------------------- |
| **Viết bằng**      | Ngôn ngữ tự nhiên (mơ hồ được)      | Code (chính xác tuyệt đối)                     |
| **Thực thi bởi**   | Con người + toà án                  | Máy — tự động                                  |
| **Cần trung gian** | Luật sư, công chứng, ngân hàng, sàn | Không                                          |
| **Thời gian**      | Ngày → tháng → năm                  | Giây                                           |
| **Chi phí**        | Phí luật sư, phí sàn (5–10%)        | Phí gas                                        |
| **Tranh chấp**     | Kiện ra toà                         | Không có khái niệm "tranh chấp" — code đã chạy |
| **Sửa đổi**        | Ký phụ lục                          | **Không sửa được**                             |
| **Diễn giải**      | Toà diễn giải "ý định các bên"      | Không diễn giải — code làm đúng cái nó viết    |

> 💡 **Điểm mấu chốt của cả bài học:** hợp đồng truyền thống nói *"nếu A thì B **phải** xảy ra"* — và cần toà án để cưỡng chế cái "phải" đó. Smart contract nói *"nếu A thì B **sẽ** xảy ra"* — không cần cưỡng chế, vì nó là quy luật vận hành của hệ thống. **Chuyển từ cưỡng chế sang tất yếu.**

### 📚 Lý thuyết bổ sung: "smart contract" là cái tên gây hiểu nhầm

Cả hai từ đều sai:

- **Không "smart"** — không có AI, không có trí tuệ. Chỉ là `if/else` tất định. Vitalik Buterin (người sáng lập Ethereum) từng nói tiếc là đã không gọi nó là **"persistent scripts"** (kịch bản dai dẳng).
- **Không hẳn "contract"** — về mặt pháp lý, phần lớn smart contract không phải hợp đồng. Nó là **cơ chế thực thi**, không phải thoả thuận có hiệu lực pháp luật.

Cách hiểu chính xác nhất:

> **Smart contract = một đối tượng (object) sống trên máy tính toàn cầu, có state riêng, có phương thức public, và có tài khoản ngân hàng riêng.**

---

## 3. Ví dụ: gọi vốn cộng đồng

Đây là ví dụ trung tâm của video. Hãy so sánh hai cách làm.

### Cách cũ: Kickstarter

```
Người ủng hộ ──tiền──▶ 🏢 KICKSTARTER ──tiền──▶ Nhà sáng lập
                            │
                     Giữ toàn bộ tiền
                     Quyết định khi nào giải ngân
                     Thu 5–8% phí
```

Cả **hai bên** đều phải tin nền tảng:

- Người ủng hộ phải tin Kickstarter sẽ hoàn tiền nếu dự án thất bại.
- Nhà sáng lập phải tin Kickstarter sẽ chuyển tiền nếu thành công.
- Cả hai phải tin Kickstarter không ôm tiền bỏ trốn, không phá sản, không bị hack.
- Cả hai trả phí cho **đặc quyền được tin tưởng** đó.

### Cách mới: smart contract

```
Người ủng hộ ──tiền──▶ 📜 SMART CONTRACT ──tiền──▶ Nhà sáng lập
                            │
                   Giữ tiền theo LUẬT CODE
                   Ai cũng đọc được code
                   Không ai can thiệp được
```

Luật được viết vào code:

```
NẾU  tổng góp ≥ mục tiêu  KHI  hết hạn
     →  chuyển toàn bộ cho nhà sáng lập
NGƯỢC LẠI
     →  mỗi người ủng hộ tự rút lại đúng phần mình đã góp
```

**Điều gì thay đổi:**

|                    | Kickstarter                           | Smart contract                    |
| ------------------ | ------------------------------------- | --------------------------------- |
| Ai giữ tiền        | Công ty                               | Code                              |
| Ai quyết giải ngân | Công ty                               | Điều kiện định sẵn                |
| Kiểm tra luật chơi | Đọc Terms of Service, tin họ làm đúng | **Đọc code**, nó *là* cái sẽ chạy |
| Nền tảng sập       | Mất tiền                              | Không có "nền tảng" để sập        |
| Nền tảng đổi luật  | Có thể                                | Không thể                         |

> 💡 Thay vì **tin một công ty**, bạn **kiểm chứng một đoạn code**. Đây là ý nghĩa thật của khẩu hiệu *"Don't trust, verify"*.

### 📚 Lý thuyết bổ sung: escrow không cần bên thứ ba

Kỹ thuật này gọi là **escrow** (ký quỹ). Trong đời thực, escrow luôn cần **bên thứ ba đáng tin** giữ tiền: ngân hàng, công chứng viên, sàn giao dịch.

Smart contract là **escrow đầu tiên trong lịch sử không có bên thứ ba** — bên giữ tiền là một chương trình mà **cả hai phía đều đọc được và không ai sửa được**.

Cùng khuôn mẫu này chạy khắp nơi: sàn phi tập trung (DEX), cầu nối chuỗi (bridge), vay có thế chấp, thị trường dự đoán, đấu giá. Tất cả đều là *"giữ tài sản, giải phóng theo điều kiện"*.

---

## 4. Chạy ở đâu — Ethereum & EVM

Bitcoin **có** khả năng script, nhưng cố ý làm rất hạn chế (không có vòng lặp, không lưu state phức tạp) — để an toàn và dễ kiểm chứng.

**Ethereum (2015)** sinh ra để làm điều Bitcoin cố tình không làm: chạy chương trình **bất kỳ**.

```
┌───────────────────────────────────────────────┐
│  Solidity  (ngôn ngữ giống JavaScript)        │  ← bạn viết ở đây
├───────────────────────────────────────────────┤
│  ↓ trình biên dịch (solc)                     │
├───────────────────────────────────────────────┤
│  EVM bytecode  (60806040...)                  │  ← thứ được lưu on-chain
├───────────────────────────────────────────────┤
│  EVM — Ethereum Virtual Machine               │  ← MỌI node đều chạy
├───────────────────────────────────────────────┤
│  Blockchain — hàng nghìn node đồng thuận      │
└───────────────────────────────────────────────┘
```

**EVM (Ethereum Virtual Machine)** là một máy ảo stack-based, **Turing-complete**, chạy giống hệt nhau trên mọi node trên thế giới.

### 📚 Lý thuyết bổ sung: blockchain là một máy trạng thái nhân bản

Đây là mô hình tư duy quan trọng nhất để hiểu smart contract:

```
    State S₀  ──[ giao dịch T₁ ]──▶  State S₁  ──[ T₂ ]──▶  State S₂ ...
```

Blockchain **không phải** chỉ là "sổ cái ghi giao dịch". Nó là một **replicated state machine** (máy trạng thái nhân bản):

- **State** = toàn bộ số dư, biến của mọi contract, code của mọi contract.
- **Transaction** = một hàm chuyển state: `S_mới = f(S_cũ, tx)`.
- **Block** = một lô transaction được áp dụng theo thứ tự.
- **Đồng thuận** = tất cả node phải ra **cùng một** `S_mới`.

> Bitcoin cũng là state machine, nhưng state của nó rất đơn giản (tập UTXO). Ethereum mở rộng state thành *bộ nhớ có thể lập trình được*.

### Hai loại tài khoản trên Ethereum

|                    | **EOA** (tài khoản người dùng)                                 | **Contract Account**              |
| ------------------ | -------------------------------------------------------------- | --------------------------------- |
| Điều khiển bởi     | **Private key** (xem [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md)) | **Code**                          |
| Có code không      | Không                                                          | Có                                |
| Có storage không   | Không                                                          | Có                                |
| Khởi tạo giao dịch | ✅ Được                                                         | ❌ Không — chỉ phản ứng khi bị gọi |

> 🔗 **Đây là chỗ [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md) nối vào.** Smart contract **không tự chạy** — nó ngủ cho tới khi có ai đó gọi. Và để gọi, bạn phải gửi một giao dịch **được ký bằng private key**. Không có chữ ký số thì không có smart contract.

Hệ quả bị hiểu nhầm nhiều nhất: **contract không thể tự hẹn giờ**. Muốn contract chạy lúc 0h ngày mai, phải có **ai đó** gửi giao dịch gọi nó lúc đó (dịch vụ như Chainlink Automation làm chính việc này, và có thu phí).

---

## 5. Gas — vì sao phải trả tiền cho mỗi phép tính

Mỗi lệnh EVM tốn một lượng **gas** nhất định:

| Thao tác                       | Gas (xấp xỉ)        |
| ------------------------------ | ------------------- |
| `ADD` (cộng)                   | 3                   |
| `MUL` (nhân)                   | 5                   |
| `SLOAD` (đọc storage)          | 2.100               |
| `SSTORE` (ghi storage lần đầu) | 20.000              |
| Chuyển ETH thường              | 21.000              |
| Deploy contract                | 100.000 – vài triệu |

Người gửi giao dịch trả phí bằng ETH:

```
Phí = gas_đã_dùng × giá_gas
```

### Vì sao phải có gas — hai lý do

**1. Trả công cho mạng.** Hàng nghìn node phải chạy code của bạn và lưu kết quả **vĩnh viễn**. Gas là tiền thuê tài nguyên đó. Chú ý `SSTORE` đắt gấp ~6.600 lần `ADD` — vì ghi vào storage nghĩa là **mọi node trên thế giới phải lưu con số đó mãi mãi**.

**2. Chặn vòng lặp vô hạn.** Đây mới là lý do sâu sắc.

### 📚 Lý thuyết bổ sung: gas giải bài toán dừng

EVM là **Turing-complete** → có thể viết vòng lặp vô hạn:

```solidity
while (true) { }   // node nào chạy cái này cũng treo mãi mãi
```

**Bài toán dừng (halting problem)** — Alan Turing chứng minh năm 1936:

> **Không tồn tại** thuật toán tổng quát nào có thể xác định một chương trình bất kỳ sẽ dừng hay chạy mãi.

Nghĩa là EVM **không thể** kiểm tra trước xem code có kết thúc không. Đây là bất khả thi về mặt toán học, không phải hạn chế kỹ thuật.

**Gas là lời giải thực dụng, né hẳn bài toán:** thay vì hỏi *"code này có dừng không?"*, ta nói:

> **"Code này sẽ dừng, vì mày chỉ mua được ngần này bước tính."**

Mỗi giao dịch có **gas limit**. Hết gas → EVM **revert** ngay:

```
Hết gas  →  ✗ mọi thay đổi state bị huỷ (như chưa từng chạy)
         →  ✓ nhưng phí VẪN BỊ TRỪ (nếu không thì spam miễn phí)
```

Cơ chế "trừ phí nhưng huỷ kết quả" là điểm tinh tế: kẻ tấn công muốn làm nghẽn mạng phải **trả tiền thật** cho mỗi lần thử.

### Tính nguyên tử (atomicity)

Giao dịch Ethereum là **all-or-nothing**, giống transaction trong cơ sở dữ liệu:

```
Thành công  →  TẤT CẢ thay đổi được ghi
Revert      →  KHÔNG thay đổi nào được ghi (kể cả những cái đã chạy xong)
```

Không có trạng thái "làm được nửa chừng". Đây là lý do một giao dịch DeFi có thể vay → hoán đổi → trả nợ qua 5 contract khác nhau, và nếu bước cuối thất bại thì cả 5 bước đều bị xoá sạch. **Flash loan** — vay hàng triệu đô không cần thế chấp — tồn tại được *chỉ nhờ* tính chất này.

### 📚 EIP-1559: cơ chế phí hiện tại

Từ 2021, phí Ethereum tách làm hai phần:

```
Phí = gas_dùng × (base_fee + priority_fee)
                     │           │
                     │           └─ tiền tip cho validator
                     └─ tự động điều chỉnh theo mức tải,
                        và bị ĐỐT (burn) — biến mất khỏi lưu thông
```

`base_fee` tự tăng khi block đầy, tự giảm khi block vắng — một **vòng phản hồi âm** y hệt difficulty adjustment ở [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md).

---

## 6. Tính tất định — luật sắt của smart contract

Đây là ràng buộc mà video không nhắc, nhưng nó **giải thích gần như mọi hạn chế** ở các phần sau.

> **Mọi node phải tính ra CÙNG MỘT kết quả. Nếu không, mạng không đồng thuận được và blockchain vỡ.**

Vì thế smart contract **bị cấm** làm những việc sau:

| ❌ Không được               | Vì sao                                                 |
| -------------------------- | ------------------------------------------------------ |
| Gọi HTTP / API             | Mỗi node gọi ở thời điểm khác nhau → kết quả khác nhau |
| Đọc file, đọc DB           | Mỗi node có ổ cứng khác nhau                           |
| Sinh số ngẫu nhiên thật    | Mỗi node ra số khác nhau                               |
| Đọc đồng hồ hệ thống       | Mỗi node có giờ khác nhau                              |
| Dùng đa luồng              | Thứ tự thực thi không xác định                         |
| Dùng số thực dấu phẩy động | Sai số làm tròn khác nhau giữa các kiến trúc CPU       |

> 💡 Chú ý dòng cuối: **Solidity không có kiểu `float`**. Mọi thứ là số nguyên. Tiền được biểu diễn bằng đơn vị nhỏ nhất (`wei` = 10⁻¹⁸ ETH) để không bao giờ phải chia lẻ. Đây cũng là cách đúng để xử lý tiền tệ trong **mọi** phần mềm tài chính, không riêng blockchain.

Contract chỉ được đọc **những gì nằm trong blockchain**: state của chính nó, state của contract khác, `block.timestamp`, `block.number`, dữ liệu giao dịch.

> ⚠️ `block.timestamp` **không phải** giờ chính xác — đó là con số do người tạo block khai báo, và họ **thao túng được vài giây**. Đừng bao giờ dùng nó làm nguồn ngẫu nhiên hay làm mốc thời gian chính xác đến giây.

---

## 7. Hạn chế 1: không sửa được sau khi deploy

Video nêu đây là nhược điểm lớn nhất, và đúng vậy.

```
Deploy contract  ──▶  code nằm on-chain VĨNH VIỄN
                      │
                      ├─ ✓ Không ai (kể cả bạn) đổi luật chơi được
                      └─ ✗ Bug cũng VĨNH VIỄN
```

**Bất biến vừa là tính năng vừa là bug.** Chính cái làm bạn tin tưởng contract cũng làm bạn không vá được nó.

Với phần mềm thường: phát hiện lỗi → vá → deploy → xong trong 1 giờ.
Với smart contract: phát hiện lỗi → **nhìn tiền bốc hơi theo thời gian thực**.

### 📚 Lý thuyết bổ sung: cách người ta lách

Vì bất biến là một ràng buộc quá gắt, ngành công nghiệp đã nghĩ ra các lối thoát:

**1. Proxy pattern (mẫu uỷ nhiệm)** — cách phổ biến nhất

```
Người dùng ──▶ PROXY (địa chỉ cố định, giữ toàn bộ STATE)
                 │
                 └─ delegatecall ─▶ LOGIC v1  (chỉ chứa code)
                                       ↓ nâng cấp
                                    LOGIC v2
```

`delegatecall` chạy code của contract khác **nhưng trên storage của mình**. Đổi con trỏ từ v1 sang v2 là "nâng cấp" xong, địa chỉ và dữ liệu người dùng giữ nguyên.

> ⚠️ **Đánh đổi:** nâng cấp được nghĩa là **ai đó có quyền nâng cấp** — thường là một khoá admin. Bạn vừa mời **trust** quay lại cửa sau. Người dùng giờ phải tin cái admin key đó không đổi contract thành "chuyển hết tiền cho tao". Nhiều vụ mất tiền lớn nhất DeFi đến từ **admin key bị lộ**, không phải lỗi logic.
>
> Giải pháp giảm nhẹ: giao quyền admin cho **multisig** (cần nhiều chữ ký) + **timelock** (thông báo trước 48h mới được nâng cấp), để người dùng kịp rút tiền nếu thấy bản nâng cấp đáng ngờ.

**2. Nút dừng khẩn cấp (circuit breaker)** — hàm `pause()` đóng băng contract khi phát hiện tấn công.

**3. Chấp nhận bất biến** — deploy contract mới, khuyến khích người dùng di cư sang. Cách "thuần khiết" nhất, và cũng chậm nhất.

**4. Audit + formal verification** — cách đúng đắn nhất: **đừng để có bug ngay từ đầu**. Audit chuyên nghiệp cho contract lớn tốn 50.000–500.000 USD. Formal verification dùng toán học **chứng minh** code thoả mãn đặc tả.

> 💡 Đây là ngành phần mềm duy nhất mà chi phí sửa lỗi sau khi phát hành gần như **vô hạn**. Nó đẩy văn hoá kỹ thuật về gần với **hàng không vũ trụ**: chậm, kỹ, kiểm thử ám ảnh — chứ không phải "move fast and break things".

---

## 8. Hạn chế 2: không thấy thế giới bên ngoài — Oracle

Smart contract sống trong một cái hộp kín. Nó **không biết**:

- Giá ETH hôm nay bao nhiêu USD
- Đội nào thắng trận bóng đá
- Chuyến bay có bị huỷ không
- Nhiệt độ ở Hà Nội
- Bất cứ thứ gì không nằm trên blockchain

Nhưng **hầu hết hợp đồng thực tế đều cần thông tin bên ngoài**. Bảo hiểm chuyến bay cần biết chuyến bay có huỷ. Cho vay thế chấp cần biết giá tài sản.

### Oracle

**Oracle** = cầu nối đưa dữ liệu ngoài đời vào blockchain.

```
🌍 Thế giới thực  ──▶  🔮 ORACLE  ──▶  📜 Smart contract
   (API, cảm biến,      ghi dữ liệu       đọc từ on-chain
    sàn giao dịch)      lên chuỗi
```

### 📚 Lý thuyết bổ sung: bài toán oracle

Đây là **vấn đề chưa được giải triệt để** của cả ngành:

> **Bạn xây một hệ thống phi tập trung, không cần tin ai — rồi cắm vào nó một nguồn dữ liệu mà bạn PHẢI TIN.**

Nếu oracle nói dối, contract vẫn thực thi **hoàn hảo** — trên dữ liệu sai. Blockchain đảm bảo *"chương trình chạy đúng"*, **không** đảm bảo *"đầu vào là sự thật"*. Cả chuỗi bảo mật rút về mắt xích yếu nhất là oracle.

**Cách giảm thiểu:**

| Cách                     | Ý tưởng                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Oracle phi tập trung** | Nhiều node độc lập báo giá, lấy **trung vị** (Chainlink). Muốn nói dối phải mua chuộc đa số.                 |
| **Đặt cọc + phạt**       | Node oracle phải khoá tiền, báo sai bị tịch thu — giống PoS ở [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md). |
| **TWAP**                 | Dùng giá trung bình theo thời gian, không dùng giá tức thời — làm thao túng tốn kém hơn nhiều.               |
| **Nhiều nguồn**          | Đối chiếu vài oracle độc lập, lệch quá ngưỡng thì tạm dừng.                                                  |

**Tấn công oracle là dạng tấn công DeFi phổ biến nhất.** Khuôn mẫu điển hình:

```
1. Flash loan vay 100 triệu USD (không cần thế chấp, trả trong cùng 1 giao dịch)
2. Đổ hết vào một pool thanh khoản mỏng → giá token X nhảy vọt
3. Contract nạn nhân đọc giá tức thời từ pool đó → tưởng X rất đắt
4. Thế chấp một ít X, vay ra thật nhiều tài sản thật
5. Trả flash loan, ôm phần chênh lệch
   → Toàn bộ diễn ra trong MỘT giao dịch, MỘT block, vài giây
```

Vụ Mango Markets (2022) mất 114 triệu USD đúng theo kịch bản này. Lỗi không nằm ở blockchain, không nằm ở mật mã — mà ở việc **tin một nguồn giá có thể thao túng**.

---

## 9. Hạn chế 3: mọi thứ đều công khai

Trên blockchain công khai:

- **Code contract** — ai cũng đọc được (nếu chưa verify source thì vẫn dịch ngược bytecode được).
- **Toàn bộ state** — mọi biến, kể cả biến khai báo `private`.
- **Mọi giao dịch** — ai gọi, gọi lúc nào, tham số gì.

> ⚠️ **`private` trong Solidity KHÔNG có nghĩa là bí mật.** Nó chỉ ngăn *contract khác* đọc trực tiếp. Bất kỳ ai cũng đọc được nó từ storage bằng `eth_getStorageAt`. **Không bao giờ lưu mật khẩu, khoá, hay dữ liệu nhạy cảm trong contract.**

Không thể làm: hồ sơ y tế, lương nhân viên, đấu thầu kín, ván bài giấu quân.

### 📚 Lý thuyết bổ sung

**Ẩn danh giả (pseudonymity):** địa chỉ ví không mang tên bạn, nhưng **mọi hành vi của nó công khai vĩnh viễn**. Chỉ cần **một lần** liên kết địa chỉ với danh tính (rút tiền qua sàn có KYC, khoe địa chỉ trên Twitter) là **toàn bộ lịch sử** của bạn — quá khứ lẫn tương lai — bị lộ. Phân tích chuỗi là cả một ngành công nghiệp (Chainalysis, Elliptic).

**Mempool là công khai:** giao dịch của bạn nằm trong hàng chờ vài giây trước khi vào block, và **ai cũng thấy**. Đây là nguồn gốc của **MEV** (Maximal Extractable Value):

- **Front-running** — thấy bạn sắp mua token, bot chen lên mua trước, bán lại cho bạn giá cao hơn.
- **Sandwich attack** — bot mua ngay trước và bán ngay sau giao dịch của bạn, ăn phần chênh lệch giá mà chính bạn tạo ra.

Đây không phải bug — nó là hệ quả trực tiếp của việc *"ai trả phí cao hơn thì được xếp trước"*. Chống bằng cách gửi qua mempool riêng tư (Flashbots) hoặc đặt giới hạn trượt giá.

**Hướng giải quyết riêng tư:**

| Công nghệ                  | Ý tưởng                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| **Zero-Knowledge Proof**   | Chứng minh *"tôi biết X"* mà không tiết lộ X. Nền của Zcash, zkRollup.                        |
| **Homomorphic encryption** | Tính toán trực tiếp trên dữ liệu đã mã hoá. Còn rất chậm.                                     |
| **Blockchain riêng tư**    | Hyperledger Fabric — chỉ thành viên được duyệt mới thấy dữ liệu. Đánh đổi bằng phi tập trung. |

---

## 10. Hạn chế 4: pháp lý

Video kết bằng câu hỏi để ngỏ: **smart contract có giá trị pháp lý không?**

Vấn đề:

- **Không biết luật nước nào áp dụng** — code chạy trên hàng nghìn node ở hàng chục quốc gia.
- **Không biết kiện ai** — nếu contract có bug và bạn mất tiền, bị đơn là ai? Người viết code? Người deploy? Các thợ đào? Không ai cả?
- **"Bên tham gia" là một chuỗi hex** — không có tên, không có quốc tịch, có thể là bot.
- **Luật cho phép huỷ hợp đồng** khi có ép buộc, gian dối, hoặc nhầm lẫn. Code thì không — nó đã chạy rồi.
- **GDPR "quyền được lãng quên"** xung đột trực tiếp với tính bất biến (đã nêu ở [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md)).

### 📚 Lý thuyết bổ sung: "code is law" gặp luật thật

Khẩu hiệu **"Code is law"** (Lawrence Lessig, 1999) nói rằng trong không gian số, kiến trúc kỹ thuật điều chỉnh hành vi mạnh hơn luật pháp.

Nhưng **The DAO (2016)** cho thấy giới hạn của nó rất rõ. Kẻ tấn công rút 3,6 triệu ETH bằng cách khai thác lỗi reentrancy. Câu hỏi trở thành triết học:

- **Phe "code is law":** hắn chỉ dùng contract **đúng như code cho phép**. Không trộm, không hack — hắn chơi theo luật đã công bố. Bất biến nghĩa là bất biến.
- **Phe thực dụng:** ai cũng biết đó không phải **ý định** của những người bỏ tiền. Để nguyên là giết chết Ethereum khi còn trứng nước.

Cộng đồng chọn **hard fork** để hoàn tiền. Thiểu số phản đối tách ra giữ chuỗi cũ, thành **Ethereum Classic** — chuỗi mà "code is law" thật sự tuyệt đối.

> 💡 **Bài học sâu nhất của cả lĩnh vực này:** tính bất biến của blockchain là **bất biến trong khuôn khổ luật đồng thuận**. Nhưng luật đồng thuận do **con người** viết, và con người **đổi ý được** nếu đủ đông đồng thuận. Cuối cùng, dưới lớp toán học, vẫn là **quản trị của con người**. Không có hệ thống nào thoát khỏi chính trị — nó chỉ chuyển chính trị sang một tầng khác.

**Xu hướng hiện tại:** hợp đồng lai — văn bản pháp lý truyền thống, kèm smart contract để tự động hoá phần thực thi (**Ricardian contract**). Một số bang Mỹ (Arizona, Tennessee, Wyoming) đã công nhận chữ ký blockchain có giá trị pháp lý; EU có khung MiCA từ 2024.

---

## 11. Lỗ hổng bảo mật kinh điển

📚 *Phần này hoàn toàn là bổ sung — video không đề cập, nhưng đây là kiến thức bắt buộc nếu bạn định viết contract.*

### Reentrancy — vụ The DAO

Lỗ hổng nổi tiếng nhất lịch sử blockchain.

**Nguyên nhân:** contract gửi tiền cho một địa chỉ **trước khi** cập nhật sổ sách. Nếu người nhận là một contract, nó có thể **gọi ngược lại** ngay trong lúc chưa cập nhật xong.

```
BẢN LỖI:                              KẺ TẤN CÔNG:
refund():
  1. gửi tiền cho người gọi  ────────▶ nhận tiền
                                       gọi lại refund() ngay!  ──┐
                              ◀────────────────────────────────┘
  1. gửi tiền (LẦN 2)        ────────▶ nhận tiếp...  (lặp lại)
  ...
  2. đặt số dư = 0   ← không bao giờ tới được cho đến khi quỹ CẠN
```

**Cách sửa — Checks-Effects-Interactions:**

```
1. CHECKS       — kiểm tra điều kiện
2. EFFECTS      — cập nhật state của MÌNH trước
3. INTERACTIONS — gọi ra ngoài SAU CÙNG
```

Chỉ cần đổi thứ tự hai dòng. Ba triệu sáu trăm nghìn ETH.

> 🧪 [Phần 13](#13-code-minh-hoạ) có code chạy được mô phỏng chính xác vụ này — kẻ tấn công góp 50, rút về 150.

Ngoài ra dùng **reentrancy guard** (một cờ khoá trong lúc hàm đang chạy) cho chắc.

### Các lỗ hổng khác

| Lỗ hổng                     | Mô tả                                                                                 | Cách chặn                                        |
| --------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Integer overflow**        | `uint8` 255 + 1 = 0 → số dư nhảy loạn                                                 | Solidity ≥ 0.8 tự revert. Cũ hơn: dùng SafeMath  |
| **Access control**          | Quên `onlyOwner` → ai cũng gọi được hàm quản trị                                      | Modifier phân quyền, kiểm thử kỹ                 |
| **Front-running / MEV**     | Bot chen lên trước giao dịch của bạn                                                  | Commit-reveal, giới hạn trượt giá, mempool riêng |
| **Thao túng oracle**        | Flash loan bóp méo giá ([phần 8](#8-hạn-chế-2-không-thấy-thế-giới-bên-ngoài--oracle)) | Oracle phi tập trung, TWAP                       |
| **`tx.origin` để xác thực** | Bị lừa qua contract trung gian                                                        | Luôn dùng `msg.sender`                           |
| **DoS bằng vòng lặp**       | Lặp qua mảng vô hạn → hết gas, contract chết cứng                                     | Rút theo mẫu pull, không push hàng loạt          |
| **Ngẫu nhiên yếu**          | Dùng `block.timestamp` làm random → thợ đào thao túng                                 | Chainlink VRF                                    |
| **Bỏ qua giá trị trả về**   | `send()` thất bại nhưng code chạy tiếp                                                | Kiểm tra kết quả, hoặc dùng `call` + require     |

### 📚 Nguyên tắc viết contract an toàn

1. **Checks → Effects → Interactions.** Luôn luôn.
2. **Pull over push** — để người dùng tự rút, đừng chủ động gửi hàng loạt.
3. **Ít state, ít code** — mỗi dòng là một chỗ có thể sai (đúng tinh thần "code không viết là code không lỗi").
4. **Dùng thư viện đã kiểm định** — OpenZeppelin, đừng tự viết ERC-20.
5. **Kiểm thử ám ảnh** — unit test, fuzzing (Echidna), formal verification.
6. **Audit trước khi cầm tiền thật.**
7. **Triển khai từ từ** — đặt trần số tiền tối đa lúc đầu, nâng dần khi đã tin.

### 📚 Lý thuyết bổ sung: contract đúng, người dùng vẫn mất tiền

Toàn bộ phần trên soi vào **mã của contract**. Nhưng người dùng không tương tác với contract bằng tay — họ đi qua **một trang web, một ví, và một núi thư viện npm**. Ba thứ đó không nằm trên chuỗi, không ai kiểm toán, và **thay đổi được bất cứ lúc nào**.

```
   NGƯỜI DÙNG ──▶ trang web ──▶ thư viện JS ──▶ ví ──▶ [ CONTRACT ]
                     ▲             ▲            ▲          ▲
                     │             │            │          └─ được kiểm toán
                     └─────────────┴────────────┘             bất biến
                        BA CHỖ NÀY: không kiểm toán,
                        đổi được bất cứ lúc nào
```

#### Tấn công chuỗi cung ứng phụ thuộc

Dự án của bạn `npm install` vài trăm gói. Mỗi gói có gói con. Chiếm được **một** gói ở tầng sâu là chiếm được mọi ứng dụng dùng nó.

Đây không phải giả thuyết — và ví dụ kinh điển nhất nhắm thẳng vào tiền mã hoá:

> **`event-stream` (2018).** Một gói npm rất phổ biến bị người bảo trì mới chèn mã độc. Mã đó **chỉ kích hoạt bên trong một ứng dụng ví Bitcoin cụ thể**, và việc nó làm là **lấy trộm khoá riêng**. Hàng triệu lượt tải mỗi tuần; gần như không ai đọc mã của gói phụ thuộc cấp ba.

Mẫu hình lặp lại nhiều lần từ đó: gói bị chiếm để đào tiền, để trộm biến môi trường, để lấy khoá. Bài học không phải "đừng dùng thư viện" — mà là:

- **Ghim phiên bản chính xác** (`package-lock.json`, không dùng `^`), và xem lại mọi lần nâng.
- **Đọc `diff` khi nâng gói**, đặc biệt các gói đụng tới khoá, mạng, hoặc biến môi trường.
- **Máy ký giao dịch tách khỏi máy phát triển.** Ví lạnh tồn tại chính vì lý do này ([Bài 6](lesson_6_vi_bitcoin.md)).

#### Chiếm giao diện — contract không hề bị đụng

Nguy hiểm hơn, vì nó không cần lỗi lập trình nào cả:

```
   1. Kẻ tấn công chiếm tài khoản DNS / CDN của dự án
   2. Chèn một đoạn mã vào trang web
   3. Đoạn mã đó đổi giao dịch mà ví hiển thị cho bạn ký
   4. Bạn bấm "Xác nhận" — CHÍNH BẠN ký, chữ ký hoàn toàn hợp lệ
   5. Contract chạy đúng như đã viết. Tiền đi mất.
```

Năm 2021, một giao thức DeFi bị mất khoảng **120 triệu USD** theo đúng kịch bản này: hệ thống hạ tầng web bị chiếm, một đoạn mã được chèn vào giao diện, và nó lừa người dùng **duyệt hạn mức** cho địa chỉ của kẻ tấn công. Smart contract không có một lỗi nào. Kiểm toán contract không thể phát hiện ra chuyện này, vì chuyện xảy ra bên ngoài contract.

> 💥 Cơ chế bị lợi dụng ở đây chính là `approve` của ERC-20 — [Bài 12 §8](../mo_rong/lesson_12_erc20_va_token.md#8--hai-cách-mất-tiền-qua-approve) mổ xẻ vì sao **một chữ ký duyệt vô hạn** có thể được dùng lại nhiều tháng sau.

**Rút ra:** "contract đã được audit" trả lời được đúng **một** câu hỏi trong năm. Khi đọc [bảng phân loại rủi ro ở Bài 10 §22](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md#22--xếp-rủi-ro-defi-theo-tầng), nhớ rằng còn một tầng nữa nằm **trên** cả sáu tầng đó: cái trình duyệt của bạn đang hiển thị.

---

## 12. Ứng dụng thực tế

| Lĩnh vực           | Ứng dụng             | Smart contract làm gì                                                         |
| ------------------ | -------------------- | ----------------------------------------------------------------------------- |
| **DeFi**           | Aave, Compound       | Cho vay/đi vay tự động, thanh lý khi thiếu thế chấp                           |
|                    | Uniswap              | Sàn hoán đổi bằng công thức toán (AMM), không sổ lệnh                         |
|                    | MakerDAO             | Phát hành stablecoin DAI dựa trên thế chấp                                    |
| **NFT**            | ERC-721              | Sở hữu duy nhất tài sản số, tự trả tiền bản quyền cho tác giả mỗi lần bán lại |
| **DAO**            | Tổ chức tự trị       | Bỏ phiếu quản trị, quản lý ngân quỹ chung on-chain                            |
| **Game**           | Axie, Gods Unchained | Vật phẩm game thuộc sở hữu người chơi, giao dịch tự do                        |
| **Bảo hiểm**       | Etherisc             | Chuyến bay trễ → oracle xác nhận → tự động bồi thường                         |
| **Chuỗi cung ứng** | VeChain              | Truy xuất nguồn gốc, tự thanh toán khi hàng tới                               |
| **Danh tính**      | ENS                  | Tên miền `.eth` thay cho địa chỉ hex                                          |

### 📚 Các chuẩn token

Chuẩn (standard) là **giao diện chung** để mọi ví và sàn nói chuyện được với contract của bạn:

| Chuẩn        | Loại                     | Dùng cho                                       |
| ------------ | ------------------------ | ---------------------------------------------- |
| **ERC-20**   | Fungible (thay thế được) | Token thường — mọi đơn vị như nhau             |
| **ERC-721**  | Non-fungible             | NFT — mỗi cái là duy nhất                      |
| **ERC-1155** | Đa token                 | Cả hai loại trong một contract (vật phẩm game) |
| **ERC-4626** | Kim khố (vault)          | Chuẩn hoá contract sinh lời                    |

> 💡 **Vì sao chuẩn quan trọng đến vậy:** nhờ ERC-20 mà MetaMask hiển thị được **mọi** token dù nó ra đời sau MetaMask. Đây là **khả năng kết hợp (composability)** — thường gọi là *"money lego"*. Contract A gọi contract B gọi contract C, tất cả trong một giao dịch nguyên tử, không cần xin phép ai. Đây là năng lực mà tài chính truyền thống **không có**, và là lý do DeFi phát triển nhanh đến vậy.

---

## 13. Code minh hoạ

### 13.1 Solidity — contract crowdfunding trong video

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;   // >=0.8 tự động revert khi tràn số

contract Crowdfunding {
    address public immutable owner;    // immutable: rẻ gas, không đổi được
    uint256 public immutable goal;
    uint256 public immutable deadline;

    mapping(address => uint256) public pledges;   // ai góp bao nhiêu
    uint256 public totalPledged;
    bool    public claimed;

    event Pledged(address indexed backer, uint256 amount);
    event Claimed(uint256 amount);
    event Refunded(address indexed backer, uint256 amount);

    constructor(uint256 _goal, uint256 _durationSeconds) {
        owner    = msg.sender;
        goal     = _goal;
        deadline = block.timestamp + _durationSeconds;
    }

    /// Góp vốn. `payable` = hàm này nhận được ETH.
    function pledge() external payable {
        require(block.timestamp < deadline, "da het han");
        require(msg.value > 0, "phai gui > 0");

        pledges[msg.sender] += msg.value;
        totalPledged        += msg.value;
        emit Pledged(msg.sender, msg.value);
    }

    /// Đạt mục tiêu -> chủ dự án rút tiền.
    function claim() external {
        // --- CHECKS ---
        require(msg.sender == owner,      "chi owner");
        require(block.timestamp >= deadline, "chua het han");
        require(totalPledged >= goal,     "khong dat muc tieu");
        require(!claimed,                 "da rut roi");

        // --- EFFECTS ---
        claimed = true;
        uint256 amount = totalPledged;

        // --- INTERACTIONS ---
        (bool ok, ) = owner.call{value: amount}("");
        require(ok, "chuyen tien that bai");
        emit Claimed(amount);
    }

    /// Không đạt mục tiêu -> người góp tự rút lại (mẫu PULL, không PUSH).
    function refund() external {
        // --- CHECKS ---
        require(block.timestamp >= deadline, "chua het han");
        require(totalPledged < goal,      "da dat muc tieu");
        uint256 amount = pledges[msg.sender];
        require(amount > 0,               "khong co gi de hoan");

        // --- EFFECTS ---  (zero hoá TRƯỚC khi gửi => chặn reentrancy)
        pledges[msg.sender] = 0;

        // --- INTERACTIONS ---
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "hoan tien that bai");
        emit Refunded(msg.sender, amount);
    }
}
```

**Đọc kỹ 4 chi tiết:**

| Dòng                                        | Vì sao quan trọng                                                                                     |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `pledges[msg.sender] = 0;` **trước** `call` | Đúng thứ tự Checks-Effects-Interactions → chặn reentrancy. Đảo hai dòng này là tái hiện vụ The DAO.   |
| `refund()` để người dùng **tự gọi**         | Mẫu **pull**. Nếu contract tự lặp gửi cho 10.000 người thì sẽ hết gas và **kẹt cứng vĩnh viễn**.      |
| `require(...)`                              | Sai điều kiện → revert → **toàn bộ** giao dịch bị huỷ như chưa từng xảy ra.                           |
| `emit Event`                                | Log rẻ hơn storage rất nhiều, dùng cho frontend theo dõi. Nhưng contract khác **không đọc được** log. |

> ⚠️ Contract này để **học**. Thiếu: reentrancy guard, xử lý người góp huỷ giữa chừng, cơ chế khẩn cấp. Đừng deploy với tiền thật.

### 13.2 TypeScript — mô phỏng chạy được, kèm demo reentrancy

Không cần cài Ethereum, không cần Solidity toolchain. Chạy trực tiếp bằng Node để **tự tay thấy** lỗ hổng.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// smartcontract.ts — mô phỏng smart contract crowdfunding + demo lỗ hổng reentrancy
// Chạy: node smartcontract.ts
import { strict as assert } from "node:assert";

/** Tương đương revert() trong Solidity: huỷ toàn bộ thay đổi state. */
class Revert extends Error {}

type Account = string | { onReceive?: () => void };

class Chain {
  /** Sổ số dư. Map để dùng được cả chuỗi lẫn object làm khoá. */
  balances = new Map<Account, number>();

  constructor(init: [Account, number][]) {
    for (const [k, v] of init) this.balances.set(k, v);
  }

  bal(who: Account): number {
    return this.balances.get(who) ?? 0;
  }

  transfer(from: Account, to: Account, amount: number): void {
    if (this.bal(from) < amount) throw new Revert("khong du so du");
    this.balances.set(from, this.bal(from) - amount);
    this.balances.set(to, this.bal(to) + amount);
    if (typeof to === "object" && to.onReceive) to.onReceive();  // fallback() của contract nhận
  }
}

/** Bản TypeScript của contract Solidity ở trên. State = thuộc tính của object. */
class Crowdfunding {
  pledges = new Map<Account, number>();     // mapping(address => uint)
  total = 0;
  claimed = false;
  chain: Chain; owner: Account; goal: number; deadline: number;

  constructor(chain: Chain, owner: Account, goal: number, deadline: number) {
    this.chain = chain; this.owner = owner; this.goal = goal; this.deadline = deadline;
  }

  // --- payable ---
  pledge(sender: Account, amount: number, now: number): void {
    if (now >= this.deadline) throw new Revert("het han");
    if (amount <= 0) throw new Revert("phai gui > 0");
    this.chain.transfer(sender, this, amount);
    this.pledges.set(sender, (this.pledges.get(sender) ?? 0) + amount);
    this.total += amount;
  }

  claim(sender: Account, now: number): void {
    if (sender !== this.owner) throw new Revert("chi owner");
    if (now < this.deadline) throw new Revert("chua het han");
    if (this.total < this.goal) throw new Revert("khong dat muc tieu");
    if (this.claimed) throw new Revert("da rut roi");
    this.claimed = true;                                 // effect TRƯỚC
    this.chain.transfer(this, sender, this.total);       // interaction SAU
  }

  refund(sender: Account, now: number): void {
    if (now < this.deadline) throw new Revert("chua het han");
    if (this.total >= this.goal) throw new Revert("da dat muc tieu");
    const amount = this.pledges.get(sender) ?? 0;
    if (amount === 0) throw new Revert("khong co gi de hoan");
    this.pledges.set(sender, 0);                  // effect TRƯỚC  <-- CHECKS-EFFECTS-INTERACTIONS
    this.chain.transfer(this, sender, amount);    // interaction SAU
  }
}

/** Y hệt, nhưng đảo thứ tự: gọi transfer TRƯỚC khi zero hoá số dư. */
class VulnerableRefund extends Crowdfunding {
  refund(sender: Account, now: number): void {
    const amount = this.pledges.get(sender) ?? 0;
    if (amount === 0) throw new Revert("khong co gi de hoan");
    this.chain.transfer(this, sender, amount);    // interaction TRƯỚC  <-- BUG
    this.pledges.set(sender, 0);                  // effect SAU (quá muộn)
  }
}

/** Contract độc: mỗi lần nhận tiền lại gọi ngược refund(). */
class Attacker {
  target: Crowdfunding | null = null;
  depth = 0;
  onReceive = (): void => {
    if (this.depth < 3) {
      this.depth++;
      try { this.target!.refund(this, 100); } catch (e) { if (!(e instanceof Revert)) throw e; }
    }
  };
}

const expectRevert = (fn: () => void): string => {
  try { fn(); } catch (e) { if (e instanceof Revert) return e.message; throw e; }
  throw new Error("phai revert");
};

// ---------- demo ----------
const alice = "alice", bob = "bob";

// 1. Đạt mục tiêu -> owner rút được
const ch = new Chain([[alice, 100], [bob, 100]]);
const c = new Crowdfunding(ch, "creator", 150, 100);
c.pledge(alice, 100, 10);
c.pledge(bob, 100, 20);
assert(c.total === 200 && ch.bal(c) === 200);
c.claim("creator", 100);
assert(ch.bal("creator") === 200 && ch.bal(c) === 0);
console.log(`✓ dat muc tieu 200/150 -> creator nhan ${ch.bal("creator")}`);

// 2. Không đạt -> backer đòi lại được, owner KHÔNG rút được
const ch2 = new Chain([[alice, 100]]);
const c2 = new Crowdfunding(ch2, "creator", 500, 100);
c2.pledge(alice, 100, 10);
console.log(`✓ khong dat muc tieu -> claim revert: ${expectRevert(() => c2.claim("creator", 100))}`);
c2.refund(alice, 100);
assert(ch2.bal(alice) === 100 && ch2.bal(c2) === 0);
console.log(`✓ alice duoc hoan ${ch2.bal(alice)}`);

// 3. Người ngoài không rút được
const ch3 = new Chain([[alice, 100]]);
const c3 = new Crowdfunding(ch3, "creator", 50, 100);
c3.pledge(alice, 100, 10);
console.log(`✓ nguoi la claim -> revert: ${expectRevert(() => c3.claim("mallory", 100))}`);

// 4. REENTRANCY: bản lỗi bị rút cạn quỹ
const m = new Attacker();
const ch4 = new Chain([[m, 50], [bob, 100]]);
const bad = new VulnerableRefund(ch4, "creator", 999, 100);
m.target = bad;
bad.pledge(m, 50, 10);
bad.pledge(bob, 100, 10);
assert(ch4.bal(bad) === 150);
bad.refund(m, 100);
console.log(`✗ BAN LOI : mallory gop 50, rut ve ${ch4.bal(m)}, quy con ${ch4.bal(bad)}`);
assert(ch4.bal(m) > 50, "reentrancy phai rut duoc nhieu hon so da gop");

// 5. Bản đúng (checks-effects-interactions) chặn được
const m2 = new Attacker();
const ch5 = new Chain([[m2, 50], [bob, 100]]);
const good = new Crowdfunding(ch5, "creator", 999, 100);
m2.target = good;
good.pledge(m2, 50, 10);
good.pledge(bob, 100, 10);
good.refund(m2, 100);
console.log(`✓ BAN DUNG: mallory gop 50, rut ve ${ch5.bal(m2)}, quy con ${ch5.bal(good)}`);
assert(ch5.bal(m2) === 50, "chi duoc rut dung phan da gop");
assert(ch5.bal(good) === 100);

console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
✓ dat muc tieu 200/150 -> creator nhan 200
✓ khong dat muc tieu -> claim revert: khong dat muc tieu
✓ alice duoc hoan 100
✓ nguoi la claim -> revert: chi owner
✗ BAN LOI : mallory gop 50, rut ve 150, quy con 0
✓ BAN DUNG: mallory gop 50, rut ve 50, quy con 100

All assertions passed.
```

> 💥 Nhìn dòng thứ 5. Mallory góp **50**, rút về **150** — vét sạch cả tiền của Bob. Khác biệt giữa dòng đó và dòng cuối là **đúng hai dòng code bị đảo thứ tự**. Đó chính xác là vụ The DAO, 3,6 triệu ETH.

**Tự thử nghiệm:**

- Đổi `this.depth < 3` thành `< 10` trong `Attacker` — thấy nó chỉ rút được đến khi quỹ cạn thì `transfer` revert.
- Trong `Crowdfunding.refund`, đảo hai dòng `pledges.set(sender, 0)` và `chain.transfer(...)` → assert ở bước 5 sẽ **fail**. Bạn vừa tự tạo lại lỗ hổng.
- Thêm một cờ `this.locked` (reentrancy guard) vào `VulnerableRefund` → chặn được mà **không** cần đổi thứ tự. Hai cách phòng thủ độc lập.

---

## 14. Từ điển thuật ngữ

| Thuật ngữ                       | Giải thích                                                       |
| ------------------------------- | ---------------------------------------------------------------- |
| **Smart contract**              | Chương trình lưu trên blockchain, tự thực thi khi điều kiện đúng |
| **Nick Szabo**                  | Người đặt ra thuật ngữ (1994), ẩn dụ máy bán nước                |
| **Ethereum**                    | Blockchain đầu tiên hỗ trợ smart contract tổng quát (2015)       |
| **EVM**                         | Ethereum Virtual Machine — máy ảo chạy bytecode contract         |
| **Solidity**                    | Ngôn ngữ phổ biến nhất để viết smart contract                    |
| **Bytecode**                    | Mã máy EVM được lưu on-chain sau khi biên dịch                   |
| **ABI**                         | Giao diện mô tả cách gọi hàm của contract từ bên ngoài           |
| **EOA**                         | Externally Owned Account — ví do private key điều khiển          |
| **Contract account**            | Tài khoản do code điều khiển, không có private key               |
| **Gas**                         | Đơn vị đo công tính toán; trả bằng ETH                           |
| **Gas limit**                   | Trần gas của một giao dịch — cơ chế chặn vòng lặp vô hạn         |
| **Revert**                      | Huỷ toàn bộ thay đổi state, nhưng vẫn mất phí                    |
| **Atomicity**                   | All-or-nothing — giao dịch thành công toàn bộ hoặc không gì cả   |
| **Halting problem**             | Bài toán không thể biết trước chương trình có dừng hay không     |
| **Deterministic**               | Tất định — mọi node phải ra cùng kết quả                         |
| **State machine**               | Mô hình blockchain: `S_mới = f(S_cũ, tx)`                        |
| **Oracle**                      | Cầu nối đưa dữ liệu ngoài đời vào blockchain                     |
| **Oracle problem**              | Hệ thống không cần tin ai lại phải tin nguồn dữ liệu             |
| **TWAP**                        | Giá trung bình theo thời gian — chống thao túng giá              |
| **Flash loan**                  | Vay không thế chấp, phải trả trong cùng một giao dịch            |
| **Reentrancy**                  | Lỗ hổng gọi ngược khi state chưa cập nhật xong                   |
| **Checks-Effects-Interactions** | Thứ tự viết hàm để chặn reentrancy                               |
| **Pull over push**              | Để người dùng tự rút, đừng gửi hàng loạt                         |
| **Proxy pattern**               | Tách state và logic để nâng cấp được contract                    |
| **delegatecall**                | Chạy code contract khác trên storage của mình                    |
| **Timelock**                    | Bắt buộc chờ N giờ trước khi thay đổi có hiệu lực                |
| **MEV**                         | Giá trị bot rút được nhờ sắp xếp lại thứ tự giao dịch            |
| **Front-running**               | Chen giao dịch lên trước giao dịch của người khác                |
| **Mempool**                     | Hàng chờ giao dịch chưa vào block — công khai                    |
| **ERC-20 / 721 / 1155**         | Chuẩn token: thay thế được / duy nhất / hỗn hợp                  |
| **Composability**               | Contract gọi contract — "money lego"                             |
| **DAO**                         | Tổ chức tự trị phi tập trung                                     |
| **The DAO hack**                | Vụ 2016 mất 3,6 triệu ETH → hard fork → Ethereum Classic         |
| **Code is law**                 | Quan điểm code đã chạy là chung cuộc, không kháng cáo            |

---

## 15. Câu hỏi tự kiểm tra

1. Vì sao máy bán nước tự động là ẩn dụ tốt cho smart contract? "Không cần tin" nghĩa là gì ở đây?
2. So với Kickstarter, smart contract loại bỏ được **chính xác** rủi ro nào?
3. Vì sao tên gọi "smart contract" bị coi là gây hiểu nhầm ở **cả hai** từ?
4. Smart contract có thể tự chạy lúc 0h ngày mai không? Vì sao?
5. Kể tên hai lý do phải có gas. Lý do nào liên quan đến bài toán dừng?
6. Hết gas thì thay đổi state có được ghi không? Phí có bị trừ không? Vì sao thiết kế như vậy?
7. Vì sao Solidity không có kiểu số thực `float`?
8. Vì sao smart contract không gọi được API? Trả lời bằng từ "tất định".
9. Oracle giải quyết vấn đề gì, và đẻ ra vấn đề gì?
10. Mô tả tấn công thao túng oracle bằng flash loan theo 5 bước.
11. Biến `private` trong Solidity có bí mật không? Giải thích.
12. Proxy pattern cho phép nâng cấp contract — cái giá phải trả là gì?
13. Viết ba bước Checks-Effects-Interactions. Vì sao đúng thứ tự đó thì chặn được reentrancy?
14. Vì sao `refund()` để người dùng tự gọi thay vì contract chủ động gửi cho tất cả?
15. Vụ The DAO: phe "code is law" lập luận thế nào? Phe hard fork lập luận thế nào? Kết cục ra sao?
16. Vì sao khả năng kết hợp (composability) là thứ tài chính truyền thống không có?

---

## Tóm tắt một trang

```
SMART CONTRACT = chương trình trên blockchain, tự chạy khi điều kiện đúng
   Ẩn dụ: MÁY BÁN NƯỚC (Nick Szabo, 1994) — không cần tin ai
   Ví dụ: crowdfunding — đủ tiền → chuyển creator | thiếu → backer tự rút
   → Thay TIN MỘT CÔNG TY bằng KIỂM CHỨNG MỘT ĐOẠN CODE

CHẠY Ở ĐÂU
   Solidity → bytecode → EVM (Turing-complete) → mọi node chạy giống nhau
   Blockchain = MÁY TRẠNG THÁI NHÂN BẢN: S_mới = f(S_cũ, tx)
   EOA (private key) khởi tạo → Contract account (code) phản ứng
   ⚠️ Contract KHÔNG tự chạy, phải có người gọi

GAS = giá của mỗi phép tính
   (1) trả công cho mạng   (2) chặn vòng lặp vô hạn ← né BÀI TOÁN DỪNG
   Hết gas → revert (huỷ hết) nhưng VẪN MẤT PHÍ
   Giao dịch NGUYÊN TỬ: all-or-nothing → nền tảng của flash loan

LUẬT SẮT: TẤT ĐỊNH — mọi node phải ra cùng kết quả
   → cấm HTTP, file, random, đồng hồ, đa luồng, số thực
   → đây là NGUỒN GỐC của mọi hạn chế bên dưới

4 HẠN CHẾ
   1. Không sửa được  → bug vĩnh viễn → proxy pattern (nhưng mời trust quay lại)
   2. Không thấy bên ngoài → ORACLE → nhưng lại phải tin oracle
   3. Mọi thứ công khai → `private` KHÔNG bí mật; mempool lộ → MEV
   4. Pháp lý mơ mịt → kiện ai? luật nước nào?

BẢO MẬT
   REENTRANCY (The DAO, 3.6M ETH) ← gửi tiền TRƯỚC khi cập nhật sổ
   Sửa: CHECKS → EFFECTS → INTERACTIONS  (đảo đúng 2 dòng code)
   Khác: overflow, access control, front-running, oracle, DoS vòng lặp
   Quy tắc: pull-over-push, OpenZeppelin, audit, đừng tự viết

CODE IS LAW gặp giới hạn ở The DAO
   → bất biến chỉ bất biến TRONG KHUÔN KHỔ luật đồng thuận
   → luật đồng thuận do CON NGƯỜI viết, và con người đổi ý được
```

---

**Nguồn:**
- Video gốc: [Smart contracts – Simply Explained](https://www.youtube.com/watch?v=ZE2HxTmxfrI) (Simply Explained – Savjee)
- Nick Szabo, *Smart Contracts: Building Blocks for Digital Markets* (1996)
- Vitalik Buterin, *Ethereum Whitepaper* (2013)
- Gavin Wood, *Ethereum Yellow Paper* — đặc tả hình thức của EVM
- [docs.soliditylang.org](https://docs.soliditylang.org) — tài liệu Solidity chính thức
- [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) — thư viện chuẩn đã audit

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. **Bài 3 – Smart contract** ← *bạn đang ở đây* — EVM, gas, oracle, reentrancy
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
