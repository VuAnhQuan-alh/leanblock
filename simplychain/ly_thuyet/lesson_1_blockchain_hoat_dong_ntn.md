# Blockchain hoạt động như thế nào?

> Bài học dựa trên video **"How does a blockchain work – Simply Explained"** (kênh *Simply Explained – Savjee*, YouTube `SSo_EIwHSd4`).
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền mà video lướt qua hoặc bỏ qua — đọc để hiểu *tại sao* chứ không chỉ *cái gì*.

---

## Mục lục

1. [Blockchain là gì](#1-blockchain-là-gì)
2. [Cấu trúc của một block](#2-cấu-trúc-của-một-block)
3. [Hash — dấu vân tay số](#3-hash--dấu-vân-tay-số)
4. [Chuỗi liên kết & tính bất biến](#4-chuỗi-liên-kết--tính-bất-biến)
5. [Tại sao hash thôi là chưa đủ](#5-tại-sao-hash-thôi-là-chưa-đủ)
6. [Proof of Work](#6-proof-of-work)
7. [Mạng ngang hàng P2P & đồng thuận](#7-mạng-ngang-hàng-p2p--đồng-thuận)
8. [Tấn công blockchain cần gì](#8-tấn-công-blockchain-cần-gì)
9. [Smart contract](#9-smart-contract)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
12. [Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)

---

## 1. Blockchain là gì

**Định nghĩa ngắn:** Blockchain là một **chuỗi các block (khối)** chứa dữ liệu, liên kết với nhau bằng mật mã, được sao chép trên nhiều máy tính, và **rất khó sửa đổi sau khi đã ghi**.

### Lịch sử

| Mốc      | Sự kiện                                                                                                                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1991** | Stuart Haber & W. Scott Stornetta mô tả kỹ thuật này trong bài báo *"How to Time-Stamp a Digital Document"*. Mục tiêu: **đóng dấu thời gian** cho tài liệu số sao cho không ai có thể sửa ngày hoặc nội dung — giống một **công chứng viên số** (digital notary). |
| **1992** | Bổ sung Merkle tree để gộp nhiều tài liệu vào một block.                                                                                                                                                                                                          |
| **2009** | Satoshi Nakamoto áp dụng ý tưởng này để tạo ra **Bitcoin** — tiền mã hoá phi tập trung đầu tiên.                                                                                                                                                                  |

> 💡 Ý quan trọng: blockchain **không phải** phát minh của Bitcoin. Bitcoin là **ứng dụng đầu tiên thành công** của blockchain.

### 📚 Lý thuyết bổ sung: vấn đề mà blockchain giải quyết

Blockchain sinh ra để giải một bài toán cũ trong khoa học máy tính:

> **Làm sao để nhiều bên không tin nhau cùng thống nhất một sổ cái chung, mà không cần một bên trung gian đáng tin?**

Trước blockchain, câu trả lời luôn là "dùng trung gian": ngân hàng giữ sổ số dư, công chứng viên giữ sổ giao dịch nhà đất, sàn giao dịch giữ sổ lệnh. Trung gian có 3 điểm yếu:

- **Single point of failure** — trung gian sập thì cả hệ thống sập.
- **Phải tin tuyệt đối** — trung gian có thể sửa sổ, hoặc bị hack, hoặc bị ép sửa.
- **Kiểm duyệt** — trung gian có thể từ chối phục vụ ai đó.

Đặc biệt với tiền số, có bài toán **double-spending** (tiêu hai lần): file số thì copy được vô hạn, làm sao ngăn tôi gửi cùng 1 đồng coin cho hai người? Trung gian giải bằng cách giữ một sổ duy nhất. Blockchain giải bằng cách cho **tất cả mọi người cùng giữ sổ**, và dùng mật mã + kinh tế học để đảm bảo các bản sao khớp nhau.

---

## 2. Cấu trúc của một block

Mỗi block chứa **3 thành phần cốt lõi**:

```
┌─────────────────────────────┐
│ Block #3                    │
├─────────────────────────────┤
│ Data:  Amount: 30 BTC       │  ← 1. DỮ LIỆU
│        From: John           │
│        To:   Kelly          │
├─────────────────────────────┤
│ Prev:  0x0000A1B2...        │  ← 2. HASH CỦA BLOCK TRƯỚC
├─────────────────────────────┤
│ Hash:  0x0000C3D4...        │  ← 3. HASH CỦA CHÍNH BLOCK NÀY
└─────────────────────────────┘
```

**1. Data (dữ liệu)** — Nội dung phụ thuộc vào loại blockchain. Với Bitcoin: người gửi, người nhận, số coin. Với blockchain y tế: hồ sơ bệnh án. Với blockchain logistics: vị trí lô hàng.

**2. Hash** — "Dấu vân tay" của block. Duy nhất cho mỗi block, tính từ toàn bộ nội dung block.

**3. Previous hash** — Hash của block đứng ngay trước. Đây chính là **sợi xích** nối các block thành *chain*.

### Genesis block

Block đầu tiên của chuỗi gọi là **genesis block**. Nó đặc biệt vì **không có block nào đứng trước** → trường `previous hash` để rỗng hoặc bằng 0.

### 📚 Lý thuyết bổ sung: cấu trúc thật của một Bitcoin block

Video đơn giản hoá. Block thật của Bitcoin có **header 80 byte** gồm 6 trường:

| Trường            | Kích thước | Ý nghĩa                                              |
| ----------------- | ---------- | ---------------------------------------------------- |
| `version`         | 4 byte     | Phiên bản luật đồng thuận                            |
| `prev_block_hash` | 32 byte    | Hash block trước (chính là "Previous Hash")          |
| `merkle_root`     | 32 byte    | Gốc cây Merkle của **toàn bộ giao dịch** trong block |
| `timestamp`       | 4 byte     | Thời gian tạo block (Unix time)                      |
| `bits`            | 4 byte     | Độ khó hiện tại (dạng nén của target)                |
| `nonce`           | 4 byte     | Số ngẫu nhiên mà thợ đào dò tìm                      |

Phần "Data" trong video thực chất là **danh sách giao dịch**, nằm *ngoài* header và được nén lại thành **một** giá trị 32 byte: `merkle_root`.

#### Merkle tree — tại sao cần?

```
              ROOT = H(H12 + H34)
             /                  \
      H12 = H(H1+H2)      H34 = H(H3+H4)
       /        \           /        \
   H1=H(TX1) H2=H(TX2)  H3=H(TX3) H4=H(TX4)
```

Lợi ích:

- **Nén**: 3.000 giao dịch → 1 hash 32 byte trong header. Header luôn cố định 80 byte dù block to hay nhỏ.
- **Chống sửa**: đổi 1 giao dịch → đổi H của nó → đổi hash cha → đổi root → đổi hash block. Y hệt hiệu ứng dây chuyền của chuỗi, nhưng theo chiều dọc.
- **Chứng minh gọn (Merkle proof)**: để chứng minh TX1 nằm trong block, bạn chỉ cần đưa `H2` và `H34` (log₂n giá trị) thay vì cả 3.000 giao dịch. Đây là nền tảng của **ví SPV / light client** — điện thoại của bạn kiểm tra được giao dịch mà không cần tải 600 GB blockchain.

---

## 3. Hash — dấu vân tay số

### Hash function là gì

**Hàm băm** nhận đầu vào bất kỳ độ dài, trả về đầu ra **cố định độ dài**. Bitcoin dùng **SHA-256** → luôn ra 256 bit = 64 ký tự hex.

```
SHA-256("Hello")  → 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
SHA-256("hello")  → 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
                     ↑ chỉ đổi 1 chữ H→h, hash khác hoàn toàn
SHA-256(cả bộ Tam Quốc Diễn Nghĩa) → vẫn đúng 64 ký tự hex
```

### 📚 Lý thuyết bổ sung: 5 tính chất bắt buộc của hash mật mã

Blockchain đứng vững được là nhờ **5 tính chất** này. Hiểu chúng là hiểu 80% blockchain.

| #   | Tính chất                                | Nghĩa là                                         | Vai trò trong blockchain                                   |
| --- | ---------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| 1   | **Deterministic** (tất định)             | Cùng input → luôn cùng output                    | Mọi node tính ra cùng một hash → kiểm chứng được           |
| 2   | **Nhanh khi tính xuôi**                  | Tính hash của 1 MB mất micro giây                | Kiểm tra block nhanh, rẻ                                   |
| 3   | **Preimage resistance** (một chiều)      | Biết hash, **không thể** suy ngược ra input      | Không ai "chế" được block khớp một hash cho trước          |
| 4   | **Avalanche effect** (hiệu ứng tuyết lở) | Đổi 1 bit input → ~50% bit output đổi            | Sửa dữ liệu dù nhỏ nhất cũng lộ ngay                       |
| 5   | **Collision resistance** (chống va chạm) | Không tìm được 2 input khác nhau cho cùng 1 hash | Không thể tráo block A bằng block B giả mà giữ nguyên hash |

**Không gian đầu ra của SHA-256:** 2²⁵⁶ ≈ 1.15 × 10⁷⁷ giá trị — nhiều hơn số nguyên tử ước tính trong vũ trụ quan sát được (~10⁸⁰, cùng bậc). Đây là lý do "đoán ngược" là bất khả thi *về mặt vật lý*, không chỉ về mặt lý thuyết.

> ⚠️ **Phân biệt:** Hash **không phải** mã hoá (encryption).
> - Mã hoá: **hai chiều**, có khoá thì giải ngược lại được bản gốc.
> - Hash: **một chiều**, mất thông tin, không bao giờ giải ngược được.

---

## 4. Chuỗi liên kết & tính bất biến

Đây là ý tưởng trung tâm của bài học.

```
  Block 1              Block 2              Block 3
┌──────────┐        ┌──────────┐        ┌──────────┐
│ Data     │        │ Data     │        │ Data     │
│ Prev: 0  │   ┌───▶│ Prev: H1 │   ┌───▶│ Prev: H2 │
│ Hash: H1 │───┘    │ Hash: H2 │───┘    │ Hash: H3 │
└──────────┘        └──────────┘        └──────────┘
  genesis
```

### Điều gì xảy ra khi kẻ xấu sửa Block 2?

1. Sửa `Data` của Block 2 → **hash của Block 2 đổi** (avalanche effect), giả sử `H2 → H2'`.
2. Block 3 vẫn ghi `Prev: H2` — **không còn khớp** với hash thật `H2'` của Block 2.
3. → **Block 3 trở nên không hợp lệ (invalid)**.
4. Và Block 4, 5, 6... cũng vậy, dây chuyền đổ theo.

> 🔗 Cặp khoá và chữ ký số bảo vệ quyền sở hữu được giải thích đầy đủ ở [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) và áp dụng cụ thể vào ví ở [Bài 6 – Ví Bitcoin](lesson_6_vi_bitcoin.md).

**Kết luận:** Sửa **một** block làm hỏng **tất cả** block phía sau. Đây là cơ chế chống giả mạo đầu tiên của blockchain.

### 📚 Lý thuyết bổ sung: "bất biến" nghĩa là gì cho đúng

Blockchain **immutable** không có nghĩa là "về mặt vật lý không sửa được". File trên ổ cứng của bạn thì bạn sửa được. Ý nghĩa thật là:

> **Bất biến = mọi sửa đổi đều bị phát hiện ngay lập tức, và việc làm cho sửa đổi đó được cả mạng chấp nhận thì tốn kém đến mức phi lý.**

Đây là bất biến kiểu **tamper-evident** (lộ dấu vết khi bị động vào), giống niêm phong trên chai thuốc — không ngăn bạn mở, nhưng ai cũng thấy nó đã bị mở.

Blockchain là một **append-only ledger** (sổ cái chỉ ghi thêm): ghi tiếp thì được, sửa/xoá cái đã ghi thì không.

> 💡 Hệ quả thực tế: **không được ghi dữ liệu cá nhân lên blockchain công khai**. Bạn sẽ không xoá được nó, xung đột trực tiếp với "quyền được lãng quên" của GDPR.

---

## 5. Tại sao hash thôi là chưa đủ

Máy tính hiện đại tính hash **cực nhanh** — GPU tầm trung làm được hàng trăm triệu hash mỗi giây.

Vậy kẻ tấn công chỉ cần:

1. Sửa Block 2.
2. Tính lại hash Block 3, Block 4, Block 5... **toàn bộ chuỗi**.
3. Xong trong vài giây → chuỗi giả mạo lại "hợp lệ" hoàn toàn.

→ Cần một cơ chế **cố tình làm chậm** việc tạo block. Đó là **Proof of Work**.

---

## 6. Proof of Work

### Ý tưởng

**Proof of Work (Bằng chứng công việc)** là một câu đố toán học:

> "Hãy tìm một hash của block bắt đầu bằng đúng N số 0."

Vì hash không đảo ngược được, cách duy nhất là **thử — sai — thử lại**: đổi một con số vô nghĩa trong block (gọi là **nonce**), tính hash, kiểm tra, không đạt thì tăng nonce lên 1, lặp lại.

```
nonce = 0     → hash = 7a3f9c...  ❌ không bắt đầu bằng 0000
nonce = 1     → hash = c81e28...  ❌
nonce = 2     → hash = eccbc8...  ❌
...
nonce = 4023876 → hash = 0000ab...  ✅ TÌM ĐƯỢC! Block hợp lệ.
```

Đặc điểm then chốt của câu đố này:

- **Tìm lời giải: rất chậm** (Bitcoin: trung bình ~10 phút cho toàn mạng).
- **Kiểm tra lời giải: tức thì** (1 phép hash, ai cũng làm được trong micro giây).

Sự bất đối xứng "khó làm — dễ kiểm tra" chính là thứ khiến PoW hữu dụng.

### Kết hợp với chuỗi

Giờ nếu kẻ xấu sửa Block 2, nó phải **làm lại Proof of Work cho Block 2 và tất cả block sau đó**. Với chuỗi dài 800.000 block, mỗi block 10 phút → bất khả thi.

> **Bảo mật của blockchain = Hashing + Proof of Work.**

> 🔗 Cơ chế giữ nhịp 10 phút này được đào sâu ở [Bài 7 – Độ khó đào](lesson_7_do_kho_dao.md); cơ chế thay thế nó bằng vốn đặt cọc ở [Bài 5 – Proof of Stake](lesson_5_proof_of_stake.md).

### 📚 Lý thuyết bổ sung: nonce, difficulty, và tại sao đúng 10 phút

#### Difficulty target

"Bắt đầu bằng N số 0" là cách nói đơn giản hoá. Luật thật là:

> `SHA-256(SHA-256(block_header))` **< target**

trong đó `target` là một số 256-bit. Target càng nhỏ → càng ít hash thoả mãn → càng khó. Nhiều số 0 ở đầu chính là hệ quả của target nhỏ.

Mỗi số 0 hex thêm vào làm độ khó **tăng 16 lần**.

#### Difficulty adjustment (điều chỉnh độ khó)

Cứ **2016 block** (~2 tuần), mỗi node tự động tính lại target:

```
target_mới = target_cũ × (thời_gian_thực_tế_của_2016_block / 20160 phút)
```

- Mạng đào nhanh hơn 10 phút/block → target giảm → khó hơn.
- Thợ đào bỏ đi, mạng chậm → target tăng → dễ hơn.

Đây là một **vòng phản hồi âm (negative feedback loop)**, giữ nhịp block ổn định ở 10 phút bất kể tổng sức mạnh đào (hashrate) tăng gấp triệu lần trong 15 năm qua.

#### Tại sao lại là 10 phút?

Đây là một **đánh đổi (trade-off)**, không phải con số thiêng:

- **Quá ngắn** → nhiều node cùng tìm ra block một lúc trước khi tin lan khắp mạng → nhiều **fork tạm thời**, mạng hay bị chia rẽ, giao dịch kém chắc chắn.
- **Quá dài** → xác nhận giao dịch chậm, trải nghiệm tệ.

10 phút đủ lâu để block lan khắp mạng toàn cầu trước khi block tiếp theo xuất hiện. (Ethereum chọn ~12 giây và phải dùng thêm cơ chế xử lý fork phức tạp hơn.)

#### Mining = PoW + phần thưởng

**Mining (đào)** = chạy PoW để tìm nonce. Người thắng nhận:

- **Block reward** — coin mới phát hành (Bitcoin: 50 → 25 → 12.5 → ... halving mỗi 210.000 block).
- **Transaction fees** — phí từ các giao dịch trong block.

Đây là mấu chốt **kinh tế học** mà video không nhắc: PoW tốn điện thật, nên phải có phần thưởng thật để có người làm. Bảo mật của Bitcoin không chỉ là toán học — nó là **toán học + động cơ kinh tế**. Tấn công mạng thì tốn kém hơn là trung thực đào và nhận thưởng.

#### 📚 Ngoài lề: PoW vs Proof of Stake

|                     | Proof of Work           | Proof of Stake                      |
| ------------------- | ----------------------- | ----------------------------------- |
| Tài nguyên đặt cược | Điện năng + phần cứng   | Coin bị khoá (stake)                |
| Ai tạo block        | Người giải câu đố trước | Người được chọn theo tỷ lệ stake    |
| Phạt gian lận       | Mất tiền điện đã đốt    | Bị **slash** — tịch thu stake       |
| Tiêu thụ điện       | Rất cao                 | Thấp hơn ~99.9%                     |
| Ví dụ               | Bitcoin, Litecoin       | Ethereum (từ 2022), Cardano, Solana |

Nguyên lý chung của cả hai: **muốn có quyền tạo block, phải bỏ ra thứ gì đó có giá trị thật và sẽ mất nó nếu gian lận.**

---

## 7. Mạng ngang hàng P2P & đồng thuận

Lớp bảo vệ thứ ba: **phi tập trung**.

Blockchain **không** đặt trên một máy chủ. Nó dùng **mạng ngang hàng (peer-to-peer)** mà **ai cũng được tham gia**.

### Quy trình khi có block mới

```
1. Người dùng tạo block mới
        ↓
2. Block được BROADCAST tới TẤT CẢ node trong mạng
        ↓
3. MỖI node tự kiểm tra độc lập:
   ✓ Hash có đúng không?
   ✓ Proof of Work có hợp lệ không?
   ✓ Previous hash có khớp block cuối trong chuỗi của mình không?
   ✓ Dữ liệu/giao dịch có hợp lệ không?
        ↓
4. Hợp lệ → node THÊM block vào chuỗi của mình
   Không hợp lệ → node TỪ CHỐI, vứt bỏ
        ↓
5. Toàn mạng đạt CONSENSUS (đồng thuận) về chuỗi đúng
```

Mỗi node giữ **một bản sao đầy đủ** của toàn bộ blockchain. Người mới tham gia sẽ tải về toàn bộ chuỗi.

**Consensus = đa số quyết định.** Node nào giữ chuỗi khác với đa số sẽ bị mạng bỏ qua.

### 📚 Lý thuyết bổ sung: fork và luật chuỗi dài nhất

#### Khi hai người cùng tìm ra block một lúc

Mạng tạm thời **fork** (chẽ nhánh) — một nửa mạng thấy block A, nửa kia thấy block B.

**Longest chain rule (luật chuỗi dài nhất)** giải quyết: node luôn theo **nhánh có tổng công việc tích luỹ lớn nhất**. Khi block tiếp theo xuất hiện trên nhánh A, nhánh A dài hơn → cả mạng chuyển sang A, nhánh B bị bỏ (**orphan/stale block**), các giao dịch trong B quay về hàng đợi.

> 💡 Đây là lý do người ta khuyên **đợi 6 xác nhận** (~1 giờ) với giao dịch Bitcoin lớn. Block càng bị chôn sâu, xác suất bị đảo ngược càng nhỏ theo cấp số nhân. Blockchain cho tính chắc chắn **theo xác suất**, không phải tuyệt đối tức thì.

#### Hard fork vs soft fork

- **Soft fork**: luật mới **chặt hơn** luật cũ. Node cũ vẫn chấp nhận block mới → tương thích ngược.
- **Hard fork**: luật mới **không tương thích** luật cũ. Node cũ từ chối block mới → chuỗi tách vĩnh viễn thành 2 mạng. (Ví dụ: Bitcoin → Bitcoin Cash 2017; Ethereum → Ethereum Classic 2016.)

#### 📚 Bài toán Byzantine Generals

Bài toán kinh điển 1982: nhiều vị tướng bao vây một thành, chỉ liên lạc bằng sứ giả, trong đó có **kẻ phản bội** gửi tin sai. Làm sao các tướng trung thành thống nhất được một kế hoạch chung?

Blockchain là một lời giải thực dụng cho bài toán này: thay vì tin lời nói, **tin công việc đã bỏ ra**. Kẻ phản bội muốn nói dối phải trả một cái giá vật lý (điện năng) cao hơn lợi ích thu được. Vì thế Bitcoin được gọi là hệ thống **Byzantine Fault Tolerant (BFT)**.

#### Các loại node

| Loại                 | Giữ gì           | Làm gì                                                       |
| -------------------- | ---------------- | ------------------------------------------------------------ |
| **Full node**        | Toàn bộ chuỗi    | Kiểm chứng mọi luật, độc lập hoàn toàn                       |
| **Mining node**      | Toàn bộ chuỗi    | Full node + chạy PoW tạo block mới                           |
| **Light node (SPV)** | Chỉ block header | Dùng Merkle proof để kiểm tra giao dịch — hợp cho điện thoại |

---


### 📚 Lý thuyết bổ sung: ai quyết định luật? Quản trị và cách kích hoạt soft fork

Ta vừa định nghĩa hard fork và soft fork. Còn một câu hỏi lớn hơn chưa trả lời: **ai quyết định có nâng cấp hay không?**

Bitcoin **không có CEO, không có quỹ, không có hội đồng**. Nhưng luật của nó vẫn thay đổi được. Cơ chế đó vận hành thế nào là một trong những phần thú vị nhất — và ít được kể nhất.

#### Bốn nhóm quyền lực

| Nhóm                                                      | Nắm gì                                                           | KHÔNG nắm gì                                             |
| --------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------- |
| **Lập trình viên**                                        | Viết code, đề xuất thay đổi                                      | Không ép ai chạy code của mình                           |
| **Thợ đào**                                               | Chọn giao dịch, sắp thứ tự block                                 | **Không đổi được luật** — block sai luật bị node từ chối |
| **Node kinh tế** (sàn, ví lớn, người dùng chạy full node) | Quyết định **chuỗi nào là thật** bằng cách chọn phần mềm để chạy | Không tạo được block                                     |
| **Người dùng / thị trường**                               | Quyết định coin nào có **giá trị**                               | Không viết luật trực tiếp                                |

> 💡 **Hiểu nhầm phổ biến nhất: "thợ đào kiểm soát Bitcoin".** Sai. Thợ đào chỉ **sắp thứ tự** giao dịch. Nếu họ tạo block vi phạm luật, mọi full node **vứt bỏ** nó và công đào thành rác. Quyền lực thật nằm ở chỗ **ai chạy phần mềm nào** — thứ nằm trong tay node kinh tế.

#### Quy trình BIP

**BIP** (Bitcoin Improvement Proposal) là văn bản chuẩn hoá đề xuất. Không có bỏ phiếu — chỉ có **đồng thuận thô** (rough consensus): một thay đổi tiến lên khi phản đối kỹ thuật cạn dần, chứ không phải khi đủ số phiếu.

Vì thế Bitcoin thay đổi **rất chậm và rất bảo thủ**. Đó là tính năng, không phải khiếm khuyết — nối vào [Bài 3](lesson_3_smart_contract.md): trong hệ thống mà bug không sửa được, "đi chậm và không làm hỏng gì" là văn hoá kỹ thuật đúng.

#### Kích hoạt soft fork: BIP9 version bits

Vấn đề thực tế: soft fork chỉ an toàn nếu **đa số áp đảo hashrate** đã sẵn sàng. Nếu bật sớm, các block hợp lệ theo luật cũ sẽ bị node mới từ chối → chuỗi tách.

```
1. Thợ đào bật một BIT trong trường version của block  → "tôi sẵn sàng"
2. Đếm trong mỗi cửa sổ 2016 block (nhịp điều chỉnh độ khó — xem Bài 7)
3. Đạt 95% trong một cửa sổ  →  LOCKED IN
4. Qua thêm một cửa sổ nữa   →  ACTIVE, luật mới có hiệu lực
5. Hết hạn (timeout) mà chưa đủ  →  FAILED
```

> ⚠️ **Đây KHÔNG phải bỏ phiếu.** Đó là **điều phối** — cách để cả mạng biết khi nào bật là an toàn. Thợ đào không "phê duyệt" luật; họ chỉ báo hiệu mình đã nâng cấp chưa. Sự nhầm lẫn giữa hai điều này là nguồn gốc của toàn bộ cuộc chiến 2017.

#### UASF — khi người dùng lật ngược thế cờ

Năm 2017, SegWit ([Bài 6](lesson_6_vi_bitcoin.md)) bị kẹt: nhiều thợ đào không báo hiệu, phần vì SegWit làm hỏng một kỹ thuật đào bí mật đang sinh lời.

Cộng đồng đáp trả bằng **BIP148 — UASF** (User-Activated Soft Fork):

```
Node kinh tế tuyên bố: "từ ngày 1/8/2017, chúng tôi TỪ CHỐI
mọi block không báo hiệu SegWit."
```

Đây là một canh bạc: nếu thợ đào phớt lờ, chuỗi tách đôi. Nhưng lập luận kinh tế rất sắc — thợ đào tạo ra block mà **sàn giao dịch không chấp nhận** thì đào ra coin **không bán được cho ai**.

Thợ đào nhượng bộ. SegWit kích hoạt.

> 💡 **Bài học của cuộc chiến kích thước block (2015–2017):** khi lập trình viên, thợ đào và người dùng bất đồng, bên thắng là bên **định nghĩa được đồng coin nào có giá trị**. Đó là **node kinh tế**, không phải hashrate. Nỗ lực tăng kích thước block bằng hard fork (SegWit2x) bị huỷ vào phút chót vì thiếu ủng hộ từ nhóm này.

Taproot (2021) sau đó dùng **Speedy Trial** — thời hạn báo hiệu ngắn hơn, có phương án dự phòng — và kích hoạt êm thấm với gần như không tranh cãi.

#### Ethereum quản trị khác hẳn

|                         | Bitcoin               | Ethereum                                 |
| ----------------------- | --------------------- | ---------------------------------------- |
| Nhịp thay đổi           | Rất chậm, bảo thủ     | Nhanh, chủ động                          |
| Điều phối               | BIP + đồng thuận thô  | **EIP** + họp All Core Devs định kỳ      |
| Kiểu nâng cấp           | Ưu tiên **soft fork** | Chủ yếu **hard fork có lịch trước**      |
| Hard fork có tranh cãi? | Cực kỳ                | Bình thường — cả mạng nâng cấp đồng loạt |
| Nhân vật trung tâm      | Không ai              | Ảnh hưởng lớn từ Ethereum Foundation     |

> 💡 **Đây là hai triết lý, không phải hơn thua.** Bitcoin tối ưu cho **bất biến**: khó đổi luật là chính điều làm nó đáng tin để làm tài sản dự trữ. Ethereum tối ưu cho **tiến hoá**: The Merge ([Bài 5](lesson_5_proof_of_stake.md)) là một cuộc thay động cơ giữa lúc đang bay, việc mà văn hoá quản trị Bitcoin sẽ không bao giờ cho phép.
>
> Và nó khép lại một mạch xuyên suốt cả khoá học: [Bài 3](lesson_3_smart_contract.md) kết luận vụ The DAO cho thấy "dưới lớp toán học vẫn là quản trị của con người"; [Bài 4](lesson_4_ung_dung_blockchain.md) cho thấy các dự án doanh nghiệp chết vì **quản trị**, không phải kỹ thuật. Phần này là chỗ bạn thấy quản trị đó vận hành ra sao khi nó **thành công**.

---

## 8. Tấn công blockchain cần gì

Muốn giả mạo thành công, kẻ tấn công phải làm **đồng thời cả ba**:

1. **Sửa block mục tiêu** → hash đổi.
2. **Làm lại Proof of Work** cho block đó và **mọi block sau nó**.
3. **Kiểm soát trên 50% mạng** để chuỗi giả mạo của mình trở thành chuỗi đa số.

Chỉ khi đó chuỗi giả mới được chấp nhận. Với Bitcoin ở quy mô hiện tại, điều này **cực kỳ khó về mặt kỹ thuật và cực kỳ đắt về mặt tài chính**.

### 📚 Lý thuyết bổ sung: 51% attack — làm được gì và KHÔNG làm được gì

**Làm được:**
- **Double-spend**: tiêu coin, đợi nhận hàng, rồi tung ra nhánh dài hơn không chứa giao dịch đó → coin quay về ví mình.
- **Kiểm duyệt**: từ chối đưa giao dịch của ai đó vào block.

**KHÔNG làm được** (điểm quan trọng nhất, thường bị hiểu nhầm):
- ❌ Không thể **tiêu coin của người khác** — cần **khoá riêng tư (private key)**, PoW không giúp gì.
- ❌ Không thể **tạo coin từ hư không** — vi phạm luật đồng thuận, mọi full node từ chối ngay.
- ❌ Không thể **đảo ngược giao dịch cũ** đã bị chôn sâu — chi phí đào lại tăng theo cấp số nhân.

→ 51% attack tấn công **thứ tự và tính chung cuộc**, không tấn công **quyền sở hữu**. Quyền sở hữu được bảo vệ bởi **chữ ký số**, một lớp hoàn toàn khác.

#### 📚 Chữ ký số — lớp bảo vệ mà video không nhắc

Đây là mảnh ghép còn thiếu để hiểu blockchain đầy đủ.

**Mật mã khoá bất đối xứng (asymmetric cryptography):** mỗi người có một cặp khoá.

```
private key (bí mật tuyệt đối)  ──một chiều──▶  public key  ──hash──▶  địa chỉ ví
     ↓ dùng để KÝ                                   ↓ dùng để XÁC MINH
```

Khi Alice gửi 1 BTC cho Bob:

1. Alice tạo giao dịch: *"chuyển 1 BTC từ địa chỉ Alice sang địa chỉ Bob"*.
2. Alice **ký** giao dịch bằng **private key** của mình → tạo ra chữ ký số (Bitcoin dùng ECDSA trên đường cong secp256k1).
3. Broadcast giao dịch + chữ ký + public key.
4. Mọi node **xác minh** chữ ký bằng public key của Alice.

Điều này đảm bảo:

- **Xác thực (authentication)** — chỉ ai giữ private key mới ký được → chỉ chủ sở hữu tiêu được coin.
- **Toàn vẹn (integrity)** — sửa dù một chữ số trong giao dịch, chữ ký lập tức sai.
- **Chống chối bỏ (non-repudiation)** — Alice không thể phủ nhận đã ký.

> ⚠️ **"Not your keys, not your coins."** Blockchain không có nút "quên mật khẩu". Mất private key = mất coin **vĩnh viễn**. Ước tính ~20% Bitcoin đã bị khoá mãi mãi theo cách này.

**Tóm lại, blockchain có 3 lớp bảo mật độc lập:**

| Lớp                       | Công nghệ             | Bảo vệ điều gì                                |
| ------------------------- | --------------------- | --------------------------------------------- |
| 1. Toàn vẹn dữ liệu       | Hash + chuỗi liên kết | Không ai sửa lịch sử mà không bị phát hiện    |
| 2. Chống viết lại lịch sử | Proof of Work         | Viết lại lịch sử tốn kém phi lý               |
| 3. Quyền sở hữu           | Chữ ký số             | Chỉ chủ sở hữu mới tiêu được tài sản của mình |

### 📚 Lý thuyết bổ sung: tấn công tầng MẠNG — rẻ hơn nhiều so với 51%

Toàn bộ phần trên nói về tấn công vào **chuỗi**: muốn viết lại lịch sử thì phải mua hashrate. Nhưng có một lớp tấn công rẻ hơn hẳn, nhắm vào **mạng lưới** thay vì chuỗi.

> **Ý tưởng cốt lõi:** không cần sửa được chuỗi. Chỉ cần kiểm soát **cái bạn nhìn thấy** về chuỗi.
> Node của bạn vẫn kiểm tra đúng từng luật một. Vấn đề là nó đang kiểm nhầm chuỗi.

#### Sybil — danh tính thì miễn phí

Proof of Work làm cho **việc tạo block** tốn kém. Nó **không** làm cho việc **tạo node** tốn kém. Một kẻ tấn công dựng hàng nghìn node giả với chi phí gần bằng không.

Sybil tự nó chưa ăn được gì — nó là **bước đệm** cho hai cái dưới đây.

#### Eclipse — bao vây một node

Node Bitcoin Core mặc định giữ **8 kết nối đi ra** (là những kết nối nó tự chọn, nên quan trọng nhất). Nếu kẻ tấn công chiếm được cả 8:

```
   BÌNH THƯỜNG                       BỊ ECLIPSE
   ───────────                       ──────────
   node ──┬── peer thật              node ──┬── kẻ tấn công
          ├── peer thật                     ├── kẻ tấn công
          ├── peer thật                     ├── kẻ tấn công
          └── ... (8 hướng)                 └── ... (cả 8 đều là nó)
      thấy chuỗi thật                   thấy ĐÚNG cái nó muốn cho thấy
```

Hệ quả:

| Nạn nhân là ai | Kẻ tấn công làm được gì |
|---|---|
| Người bán hàng | cho xem một chuỗi giả có giao dịch trả tiền → giao hàng → thực tế chưa từng có giao dịch nào |
| Thợ đào | giấu block thật đi → thợ đào phí công đào lên nhánh chết |
| Node Lightning | **giấu giao dịch đóng kênh gian lận** → hết thời hạn phản ứng → mất tiền ([Bài 11](../mo_rong/lesson_11_fork_va_lightning.md)) |

Chi phí không phải hashrate — chỉ là **nhiều địa chỉ IP**. Đó là lý do đây là lớp tấn công đáng sợ với người dùng lẻ hơn là 51%.

**Cách chống** (Bitcoin Core đã làm dần qua nhiều năm): chọn peer phân tán theo dải mạng thay vì ngẫu nhiên đều, giữ một số **kết nối neo** với peer cũ đã tin cậy qua nhiều phiên, thêm các kết nối **chỉ nhận block** tách khỏi kênh thường, và giữ danh sách hạt giống cứng trong mã nguồn.

#### Tấn công định tuyến — chặn ở tầng ISP

Không cần chiếm node nào cả, chỉ cần chiếm **đường đi của gói tin**. Giao thức định tuyến liên mạng (BGP) vốn dựa trên tin tưởng: một nhà mạng có thể tuyên bố "đường tới dải IP này đi qua tôi", và các nhà mạng khác tin.

Chuyện này đã xảy ra thật: năm 2014 một nhà mạng bị lợi dụng để chiếm quyền định tuyến lưu lượng của nhiều mỏ đào, chuyển hướng chúng sang pool của kẻ tấn công. Số tiền bị lấy được báo cáo khoảng **83.000 USD**.

Điều làm nó nguy hiểm ở quy mô lớn: lưu lượng Bitcoin **tập trung qua một số ít nhà mạng lớn**, nên chia đôi mạng không cần chạm tới đa số node — chỉ cần chạm tới một ít đường trục.

#### Ba lớp tấn công, ba thứ tiền khác nhau

| Tấn công | Mua cái gì | Nhắm vào | Phòng thủ |
|---|---|---|---|
| **51%** | hashrate / cổ phần | **chuỗi** | chi phí kinh tế ([phần 8](#8-tấn-công-blockchain-cần-gì)) |
| **Eclipse** | nhiều địa chỉ IP | **một node** | đa dạng hoá peer, kết nối neo |
| **Định tuyến** | quyền công bố BGP | **cả một vùng mạng** | mã hoá kết nối, đa dạng đường đi |

> 💥 **Điều đáng nhớ nhất:** hai lớp dưới **không phá vỡ một phép mật mã nào**, và cũng không cần một watt điện nào. Chúng chỉ cần bạn không nhìn thấy phần còn lại của thế giới. Đây là lần đầu trong khoá học gặp mẫu hình *"mật mã không phải chỗ vỡ"* — nó sẽ lặp lại ở [Bài 10](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md) và [Bài 13](../mo_rong/lesson_13_gdpr_va_blockchain.md).

---

## 9. Smart contract

**Smart contract (hợp đồng thông minh)** là **chương trình được lưu trên blockchain và tự động thực thi** khi điều kiện được thoả mãn.

Ví dụ: *"Nếu đến ngày 01/01 mà A chưa trả tiền, tự động chuyển quyền sở hữu căn nhà cho B."* Không cần luật sư, không cần công chứng, không cần ai bấm nút.

Vì code chạy trên blockchain nên nó thừa hưởng mọi tính chất: minh bạch, bất biến, không thể bị chặn.

> 🔗 Toàn bộ chủ đề này là [Bài 3 – Smart contract](lesson_3_smart_contract.md).

### 📚 Lý thuyết bổ sung

- **Nguồn gốc**: khái niệm do Nick Szabo đặt ra năm 1994 — trước Bitcoin 15 năm. Ví dụ kinh điển của ông: **máy bán nước tự động** — bỏ tiền vào, máy tự nhả hàng, không cần người bán, không cần tin tưởng ai.
- **Nền tảng**: Bitcoin có ngôn ngữ Script rất hạn chế (cố ý, để an toàn). **Ethereum (2015)** đưa vào **EVM** — máy ảo **Turing-complete** cho phép viết chương trình bất kỳ, thường bằng ngôn ngữ **Solidity**.
- **Gas**: mỗi lệnh tốn phí *gas* trả bằng ETH. Điều này (a) trả công cho node chạy code, và (b) ngăn vòng lặp vô hạn làm sập mạng — lời giải thực dụng cho bài toán dừng (halting problem).
- **Ứng dụng**: DeFi (vay/cho vay không ngân hàng), NFT, DAO (tổ chức tự trị), stablecoin, sàn phi tập trung (DEX).

> ⚠️ **"Code is law" là con dao hai lưỡi.** Smart contract bất biến nghĩa là **bug cũng bất biến**. Vụ **The DAO (2016)** bị khai thác lỗ hổng reentrancy, mất 3.6 triệu ETH, buộc Ethereum phải hard fork để hoàn tiền — và làm chuỗi tách đôi thành Ethereum / Ethereum Classic. Bài học: audit smart contract trước khi deploy, vì bạn **không sửa được sau đó**.

---

## 10. Code minh hoạ

Cài đặt tối giản để tự tay kiểm chứng mọi thứ ở trên. Chỉ dùng thư viện chuẩn của Node, không cần gói ngoài.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// simplychain.ts — blockchain tối giản: hash chain + proof of work
// Chạy: node simplychain.ts   (Node 22.6+ chạy .ts trực tiếp, không cần cài gì)
import { createHash } from "node:crypto";
import { strict as assert } from "node:assert";

const sha256 = (s: string): string =>
  createHash("sha256").update(s).digest("hex");

class Block {
  index: number;
  data: string;
  prevHash: string;
  timestamp: number;
  nonce = 0;
  hash: string;

  constructor(index: number, data: string, prevHash: string) {
    this.index = index;
    this.data = data;
    this.prevHash = prevHash;
    this.timestamp = Date.now() / 1000;
    this.hash = this.computeHash();
  }

  computeHash(): string {
    return sha256(
      `${this.index}${this.timestamp}${this.data}${this.prevHash}${this.nonce}`,
    );
  }

  /** Proof of Work: dò nonce cho tới khi hash bắt đầu bằng `difficulty` số 0. */
  mine(difficulty: number): string {
    const target = "0".repeat(difficulty);
    while (!this.hash.startsWith(target)) {
      this.nonce++;
      this.hash = this.computeHash();
    }
    return this.hash;
  }
}

class Blockchain {
  difficulty: number;
  chain: Block[];

  constructor(difficulty = 4) {
    this.difficulty = difficulty;
    const genesis = new Block(0, "Genesis Block", "0".repeat(64));
    genesis.mine(difficulty);
    this.chain = [genesis];
  }

  add(data: string): void {
    const block = new Block(this.chain.length, data, this.chain.at(-1)!.hash);
    block.mine(this.difficulty);
    this.chain.push(block);
  }

  isValid(): boolean {
    const target = "0".repeat(this.difficulty);
    for (let i = 1; i < this.chain.length; i++) {
      const prev = this.chain[i - 1], cur = this.chain[i];
      if (cur.hash !== cur.computeHash()) return false;   // dữ liệu bị sửa?
      if (cur.prevHash !== prev.hash) return false;       // sợi xích bị đứt?
      if (!cur.hash.startsWith(target)) return false;     // PoW hợp lệ?
    }
    return true;
  }
}

// ---------- demo ----------
const bc = new Blockchain(4);
for (const tx of ["Alice -> Bob: 10", "Bob -> Carol: 3", "Carol -> Dave: 1"]) {
  const t = Date.now();
  bc.add(tx);
  const b = bc.chain.at(-1)!;
  console.log(
    `mined #${b.index} nonce=${String(b.nonce).padStart(8)} ` +
    `${b.hash.slice(0, 16)}... (${((Date.now() - t) / 1000).toFixed(2)}s)`,
  );
}

assert(bc.isValid(), "chuỗi mới tạo phải hợp lệ");
console.log("valid:", bc.isValid());

// Kẻ xấu sửa block 1 -> cả chuỗi hỏng
bc.chain[1].data = "Alice -> Mallory: 1000";
assert(!bc.isValid(), "sửa dữ liệu phải làm chuỗi invalid");
console.log("sau khi sửa block 1, valid:", bc.isValid());

// Tính lại hash block 1 vẫn KHÔNG cứu được: block 2 giữ prevHash cũ
bc.chain[1].hash = bc.chain[1].computeHash();
assert(!bc.isValid(), "vá hash một block không đủ — sợi xích vẫn đứt");
console.log("sau khi vá hash block 1, valid:", bc.isValid());
console.log("=> muốn giả mạo phải đào lại TOÀN BỘ block phía sau.");
```

**Kết quả chạy:**

```
mined #1 nonce=   66793 0000567ce44895d0... (0.04s)
mined #2 nonce=    1620 00001638026c5e71... (0.00s)
mined #3 nonce=   77120 0000dc9f39be0223... (0.04s)
valid: true
sau khi sửa block 1, valid: false
sau khi vá hash block 1, valid: false
=> muốn giả mạo phải đào lại TOÀN BỘ block phía sau.
```

**Hãy tự thử nghiệm:**

- Đổi `difficulty` từ 4 → 5 → 6, đo thời gian đào. Mỗi bậc chậm hơn ~16 lần — đó là *cảm giác* của difficulty target.
- In `nonce` ra, xem nó nhảy ngẫu nhiên thế nào — chứng tỏ không có cách nào ngoài dò tìm.
- Bỏ kiểm tra `cur.prevHash !== prev.hash` trong `isValid()`, xem "chain" mất đi thì còn lại gì.

---

## 11. Từ điển thuật ngữ

| Thuật ngữ                | Giải thích                                                  |
| ------------------------ | ----------------------------------------------------------- |
| **Block**                | Khối dữ liệu chứa data + hash + previous hash               |
| **Genesis block**        | Block đầu tiên, không có block trước                        |
| **Hash**                 | Dấu vân tay số, độ dài cố định, một chiều                   |
| **SHA-256**              | Hàm băm Bitcoin dùng, cho ra 256 bit                        |
| **Avalanche effect**     | Đổi 1 bit input → ~50% bit output đổi                       |
| **Merkle root**          | Hash gốc của cây Merkle, nén mọi giao dịch trong block      |
| **Nonce**                | Số vô nghĩa mà thợ đào dò tìm để thoả mãn PoW               |
| **Difficulty / target**  | Ngưỡng quyết định độ khó của PoW                            |
| **Proof of Work**        | Câu đố khó giải – dễ kiểm tra, làm chậm việc tạo block      |
| **Mining**               | Chạy PoW để tạo block mới, đổi lấy phần thưởng              |
| **Node**                 | Máy tính tham gia mạng, giữ bản sao blockchain              |
| **P2P network**          | Mạng ngang hàng, không máy chủ trung tâm                    |
| **Consensus**            | Cơ chế để mạng thống nhất chuỗi nào là chuỗi đúng           |
| **Longest chain rule**   | Theo nhánh có tổng công việc lớn nhất                       |
| **Fork**                 | Chuỗi chẽ nhánh (tạm thời hoặc vĩnh viễn)                   |
| **51% attack**           | Kiểm soát quá nửa hashrate để viết lại lịch sử gần          |
| **Double-spending**      | Tiêu cùng một đồng coin hai lần                             |
| **Private / public key** | Cặp khoá: ký giao dịch / xác minh chữ ký                    |
| **Smart contract**       | Chương trình tự thực thi lưu trên blockchain                |
| **Gas**                  | Phí tính theo lượng tính toán của smart contract (Ethereum) |
| **Immutable**            | Bất biến — sửa được nhưng lộ ngay và tốn kém phi lý         |

---

## 12. Câu hỏi tự kiểm tra

Trả lời được hết là đã nắm bài:

1. Ba thành phần của một block là gì? Thành phần nào tạo nên "chain"?
2. Vì sao sửa Block 3 lại làm hỏng Block 4, 5, 6...?
3. Nếu hash đã chống giả mạo rồi, tại sao còn cần Proof of Work?
4. PoW khó ở chỗ nào mà kiểm tra lại dễ? Sự bất đối xứng đó dùng để làm gì?
5. Bitcoin làm cách nào giữ nhịp 10 phút/block khi hashrate tăng gấp triệu lần?
6. Khi hai thợ đào cùng tìm ra block một lúc, mạng xử lý thế nào?
7. Kẻ nắm 51% hashrate **không** làm được gì? Vì sao?
8. Vì sao tuyệt đối không ghi dữ liệu cá nhân lên blockchain công khai?
9. Merkle tree cho phép điện thoại làm được điều gì mà không cần tải cả blockchain?
10. "Code is law" mang lại lợi ích gì và rủi ro gì?

---

## Tóm tắt một trang

```
BLOCK = data + hash + previous_hash
   └─ previous_hash nối các block thành CHAIN

SỬA 1 BLOCK → hash đổi → mọi block sau INVALID     ← lớp 1: toàn vẹn
   nhưng máy tính tính hash quá nhanh
      → PROOF OF WORK làm chậm lại (~10 phút/block) ← lớp 2: chống viết lại

P2P NETWORK: ai cũng giữ 1 bản sao, ai cũng kiểm tra
   → CONSENSUS: đa số quyết định chuỗi đúng
   → muốn giả mạo phải: sửa block + đào lại tất cả + nắm >50% mạng

CHỮ KÝ SỐ (private key) bảo vệ QUYỀN SỞ HỮU         ← lớp 3: sở hữu
   51% attack không tiêu được coin của người khác

SMART CONTRACT: code tự chạy trên blockchain
   bất biến → bug cũng bất biến → phải audit
```

---

**Nguồn:**
- Video gốc: [How does a blockchain work – Simply Explained](https://www.youtube.com/watch?v=SSo_EIwHSd4) (Simply Explained – Savjee)
- Haber & Stornetta, *How to Time-Stamp a Digital Document* (1991)
- Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008)

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. **Bài 1 – Blockchain hoạt động như thế nào** ← *bạn đang ở đây* — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
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
