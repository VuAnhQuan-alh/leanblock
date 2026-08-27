# Proof of Stake (so với Proof of Work)

> Bài học dựa trên video **"Proof-of-Stake (vs proof-of-work)"** (kênh *Simply Explained – Savjee*, YouTube `M3EFi_POhps`).
> Nối tiếp [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) (phần 6 đã giới thiệu PoW, phần bổ sung có bảng PoW vs PoS sơ lược). Bài này đào sâu.
>
> ⚠️ **Video ra đời trước The Merge.** Lúc đó Ethereum *dự định* chuyển sang PoS. Việc đó **đã xảy ra ngày 15/09/2022**. Phần **📚 Lý thuyết bổ sung** cập nhật toàn bộ những gì đã thay đổi kể từ đó.

---

## Mục lục

1. [Nhắc lại Proof of Work và vấn đề của nó](#1-nhắc-lại-proof-of-work-và-vấn-đề-của-nó)
2. [Proof of Stake — ý tưởng cốt lõi](#2-proof-of-stake--ý-tưởng-cốt-lõi)
3. [Chọn validator thế nào](#3-chọn-validator-thế-nào)
4. [Phần thưởng đến từ đâu](#4-phần-thưởng-đến-từ-đâu)
5. [Tấn công 51% trong PoS](#5-tấn-công-51-trong-pos)
6. [Nothing at Stake và slashing](#6-nothing-at-stake-và-slashing)
7. [📚 The Merge — điều đã xảy ra sau video](#7--the-merge--điều-đã-xảy-ra-sau-video)
8. [📚 Ethereum PoS hoạt động thật sự thế nào](#8--ethereum-pos-hoạt-động-thật-sự-thế-nào)
9. [📚 Các tội bị slashing](#9--các-tội-bị-slashing)
10. [📚 Tấn công tầm xa & tính chủ quan yếu](#10--tấn-công-tầm-xa--tính-chủ-quan-yếu)
11. [📚 Hai mô hình bảo mật kinh tế: dòng chảy vs kho vốn](#11--hai-mô-hình-bảo-mật-kinh-tế-dòng-chảy-vs-kho-vốn)
12. [📚 Phê phán PoS](#12--phê-phán-pos)
13. [📚 Các biến thể](#13--các-biến-thể)
14. [Code minh hoạ](#14-code-minh-hoạ)
15. [Bảng so sánh tổng](#15-bảng-so-sánh-tổng)
16. [Từ điển thuật ngữ](#16-từ-điển-thuật-ngữ)
17. [Câu hỏi tự kiểm tra](#17-câu-hỏi-tự-kiểm-tra)

---

## 1. Nhắc lại Proof of Work và vấn đề của nó

Ôn nhanh từ [Bài 1](lesson_1_blockchain_hoat_dong_ntn.md):

```
Thợ đào ─▶ dò nonce ─▶ hash < target?  ─ không ─▶ thử lại (hàng tỷ lần/giây)
                              │ có
                              ▼
                    Tạo block, nhận phần thưởng
```

Bảo mật đến từ chỗ: **muốn viết lại lịch sử phải đốt lại toàn bộ điện năng đã đốt**.

> 🔗 Cơ chế điều chỉnh độ khó giữ cho việc đốt đó ổn định qua thời gian: [Bài 7 – Độ khó đào](lesson_7_do_kho_dao.md).

### Bốn vấn đề của PoW

| Vấn đề                   | Chi tiết                                                                                                                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tốn điện khủng khiếp** | Bitcoin tiêu thụ ~100–150 TWh/năm — ngang mức tiêu thụ điện của cả một quốc gia tầm trung. Toàn bộ năng lượng đó dùng để **dò số ngẫu nhiên**, không tạo ra giá trị tính toán nào khác. |
| **Rác thải phần cứng**   | ASIC là chip **chỉ làm được một việc**. Đời sống 1,5–3 năm, sau đó thành rác điện tử — không tái dùng cho việc khác được.                                                               |
| **Tập trung hoá**        | Đào cá nhân đã chết từ lâu. Vài **mining pool** kiểm soát phần lớn hashrate. Thợ đào dồn về nơi điện rẻ → tập trung địa lý.                                                             |
| **Rào cản gia nhập**     | Muốn tham gia phải mua ASIC (hàng nghìn USD) + có nguồn điện giá công nghiệp.                                                                                                           |

> 💡 Điểm mấu chốt để hiểu PoS: PoW **cố ý lãng phí** một nguồn lực bên ngoài (điện) để chứng minh cam kết. Câu hỏi PoS đặt ra là: *"tại sao không đặt cọc bằng chính đồng coin của mạng, thay vì đốt điện?"*

---

## 2. Proof of Stake — ý tưởng cốt lõi

**Proof of Stake** thay **công sức tính toán** bằng **vốn bị khoá**.

```
       PROOF OF WORK                    PROOF OF STAKE
   ┌──────────────────────┐        ┌───────────────────────┐
   │ Đặt cọc: ĐIỆN NĂNG   │        │ Đặt cọc: COIN BỊ KHOÁ │
   │ Ai thắng: giải nhanh │        │ Ai thắng: được CHỌN   │
   │           nhất       │        │  ngẫu nhiên theo stake│
   │ Gọi là: THỢ ĐÀO      │        │ Gọi là: VALIDATOR     │
   │ Mất gì nếu gian: tiền│        │ Mất gì nếu gian:      │
   │   điện đã đốt        │        │   BỊ TỊCH THU STAKE   │
   └──────────────────────┘        └───────────────────────┘
```

Không còn cuộc đua tính toán. **Không có câu đố nào để giải.** Thay vào đó:

1. Bạn **khoá** một lượng coin làm **stake** (cổ phần đặt cọc).
2. Thuật toán **chọn giả ngẫu nhiên** một validator để tạo block tiếp theo.
3. Xác suất được chọn **tỷ lệ thuận với stake**.
4. Validator tạo block hợp lệ → nhận thưởng. Gian dối → **mất stake**.

### Vì sao cơ chế này an toàn

Cả PoW và PoS đều dựa trên cùng một nguyên lý:

> **Muốn có quyền tạo block, phải bỏ ra thứ gì đó có giá trị thật, và sẽ mất nó nếu gian dối.**

Khác nhau ở chỗ *thứ có giá trị* đó là gì:

|                   | PoW                                       | PoS                            |
| ----------------- | ----------------------------------------- | ------------------------------ |
| Tài sản đặt cọc   | Điện + phần cứng (**bên ngoài** hệ thống) | Coin (**bên trong** hệ thống)  |
| Cơ chế trừng phạt | Gián tiếp — đốt điện vô ích               | **Trực tiếp** — tịch thu stake |

> 💡 Đây là điểm khác biệt sâu sắc nhất, và [phần 11](#11--hai-mô-hình-bảo-mật-kinh-tế-dòng-chảy-vs-kho-vốn) sẽ khai thác nó. PoS có **đòn trừng phạt trực tiếp** mà PoW không có: PoW chỉ có thể làm bạn *lãng phí*, PoS có thể *lấy tiền của bạn*.

---

## 3. Chọn validator thế nào

Xác suất được chọn tỷ lệ thuận với stake:

```
Alice  stake   100  →  10% cơ hội
Bob    stake   300  →  30% cơ hội
Carol  stake   600  →  60% cơ hội
─────────────────────
Tổng         1.000     100%
```

Giống mua vé số: càng nhiều vé càng dễ trúng, nhưng **không chắc chắn** trúng.

> 🧪 [Phần 14](#14-code-minh-hoạ) có code chạy 100.000 lượt chọn, xác nhận tỉ lệ thực tế khớp kỳ vọng: 10,0% / 29,9% / 60,2%.

### 📚 Lý thuyết bổ sung: "ngẫu nhiên" ở đây là ngẫu nhiên gì?

Nhớ luật tất định ở [Bài 3](lesson_3_smart_contract.md): blockchain **không có** số ngẫu nhiên thật — mọi node phải ra cùng kết quả.

Nên đây là **ngẫu nhiên giả tất định**: một hàm mà đầu vào ai cũng biết, đầu ra ai cũng tính được và ra giống nhau, nhưng **không đoán trước được**.

Đây là bài toán khó. Nếu validator **đoán trước** được khi nào mình được chọn, hoặc tệ hơn — **tác động** được vào kết quả — thì họ thao túng được mạng.

**Chọn ngẫu nhiên ngây thơ đều sai:**

| Cách                     | Vì sao sai                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| Dùng `block.timestamp`   | Người tạo block chỉnh được vài giây → mò để tự chọn mình                         |
| Dùng hash block trước    | Người tạo block trước **chọn** được hash đó (bằng cách bỏ giao dịch) → thao túng |
| Chỉ chọn người giàu nhất | Không còn là ngẫu nhiên, tập trung hoàn toàn                                     |

**Cách thật (Ethereum): RANDAO.**

```
Mỗi validator được chọn đóng góp 1 giá trị bí mật đã cam kết trước
        ↓
   XOR tất cả lại  ──▶  số ngẫu nhiên chung
        ↓
Muốn thao túng phải kiểm soát NGƯỜI CUỐI CÙNG đóng góp
(người cuối chỉ có 1 lựa chọn: đóng góp hoặc bỏ qua — "last revealer bias")
```

RANDAO **không hoàn hảo** — người cuối cùng có một chút ảnh hưởng (bỏ lượt để đổi kết quả, đánh đổi bằng mất phần thưởng). Giải pháp triệt để hơn là **VDF** (Verifiable Delay Function — hàm trễ kiểm chứng được): một hàm **bắt buộc mất thời gian** để tính nhưng kiểm tra tức thì, khiến không ai kịp tính trước kết quả để quyết định có bỏ lượt hay không. VDF vẫn đang trong lộ trình, chưa triển khai.

**Các cách chọn khác (ngoài thuần theo stake):**

- **Coin age** — ưu tiên coin đã khoá lâu, để người ít coin thỉnh thoảng cũng được chọn (Peercoin). Nhược: khuyến khích online ngắt quãng.
- **Randomized block selection** — kết hợp stake và hash của địa chỉ.

---

## 4. Phần thưởng đến từ đâu

Đây là chỗ PoS khác PoW rõ rệt.

```
PoW:  Block reward (coin MỚI phát hành)  +  phí giao dịch
PoS:  chủ yếu là PHÍ GIAO DỊCH  (phát hành mới rất ít hoặc bằng 0)
```

Trong thiết kế PoS gốc, **toàn bộ coin được tạo từ đầu**, không phát hành thêm. Validator kiếm tiền **chỉ từ phí giao dịch**. Vì thế họ thường được gọi là **forger** (người rèn) hoặc **minter** thay vì *miner* (thợ đào) — không có gì được "đào" lên cả.

### 📚 Lý thuyết bổ sung: tác động kinh tế

|                   | Bitcoin (PoW)                                                                            | Ethereum (PoS, sau Merge)                                            |
| ----------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Phát hành mới/năm | ~1,7% (giảm nửa mỗi 4 năm)                                                               | ~0,5%                                                                |
| Vì sao chênh lệch | Thợ đào phải trả tiền điện **bằng tiền pháp định** → phải bán coin → cần phát hành nhiều | Validator gần như không có chi phí vận hành → cần ít phần thưởng hơn |

Ethereum sau Merge còn thêm cơ chế **đốt** của EIP-1559 ([Bài 3](lesson_3_smart_contract.md), phần 5): `base_fee` bị huỷ vĩnh viễn. Khi mạng bận, **lượng đốt > lượng phát hành** → tổng cung **giảm**. Cộng đồng gọi hiện tượng này là *"ultrasound money"*.

> 💡 Đây là một hệ quả ít ai để ý: chuyển sang PoS không chỉ tiết kiệm điện — nó **giảm mạnh áp lực bán**. Thợ đào PoW buộc phải bán coin để trả hoá đơn điện. Validator PoS thì không.

---

## 5. Tấn công 51% trong PoS

Muốn kiểm soát mạng PoS, bạn phải sở hữu **hơn 50% tổng số coin đang được stake**.

Điều này gần như bất khả thi vì **ba** lý do, và lý do thứ ba mới là lý do hay nhất:

**1. Cực đắt.** Với Ethereum ở quy mô hiện tại, cần mua hàng chục tỷ USD ETH.

**2. Không mua nổi.** Đây không phải hàng có sẵn trên kệ. Gom mua lượng lớn như vậy sẽ **đẩy giá lên theo cấp số nhân** — bạn đang tự làm cuộc tấn công của mình đắt lên theo từng lệnh mua.

**3. Tự bắn vào chân.** Đây mới là điểm cốt lõi:

> **Bạn phải trở thành người nắm giữ lớn nhất của chính thứ bạn định phá huỷ.**

Tấn công thành công → niềm tin sụp → giá coin sụp → **tài sản của chính bạn bốc hơi**. Bạn bỏ 50 tỷ USD để phá huỷ giá trị của 50 tỷ USD mà bạn vừa mua.

**Và tệ hơn nữa:** trong PoS hiện đại, stake của bạn sẽ **bị đốt** (slashing). Bạn không chỉ mất do giá giảm — bạn mất luôn cả số vốn gốc.

### 📚 So sánh với PoW

Đây là chỗ PoS thật sự vượt trội, và ít người nhận ra:

|                                    | PoW                                                                  | PoS                              |
| ---------------------------------- | -------------------------------------------------------------------- | -------------------------------- |
| Tấn công xong, tài sản còn không?  | ✅ **Còn** — ASIC vẫn nguyên, đem đi đào chuỗi khác hoặc tấn công lại | ❌ **Mất** — stake bị đốt         |
| Tấn công lại được không?           | ✅ Được, chỉ tốn thêm tiền điện                                       | ❌ Phải mua lại từ đầu            |
| Có thể **thuê** năng lực tấn công? | ✅ Được — thuê hashrate theo giờ (NiceHash)                           | ❌ Không — phải **sở hữu** coin   |
| Mạng phục hồi thế nào              | Khó — kẻ tấn công vẫn còn máy                                        | Dễ — kẻ tấn công đã mất sạch vốn |

> 💡 Dòng thứ ba là chí mạng. Các chuỗi PoW nhỏ **thường xuyên** bị tấn công 51% vì có thể **thuê** hashrate trong vài giờ với giá vài nghìn USD. Trong PoS, không tồn tại "thị trường cho thuê stake" tương đương — bạn phải mua đứt và chịu rủi ro sở hữu.

---

## 6. Nothing at Stake và slashing

Đây là phản biện kinh điển nhất chống lại PoS, và video có nhắc.

### Vấn đề

Khi mạng bị **fork** ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md), phần 7), validator phải chọn theo nhánh nào.

```
                    ┌──▶ nhánh A
   ...──block──fork─┤
                    └──▶ nhánh B
```

- **Trong PoW:** hashrate của bạn **hữu hạn**. Đào nhánh A nghĩa là **không** đào nhánh B. Bạn buộc phải chọn — và bạn sẽ chọn nhánh mình tin sẽ thắng.
- **Trong PoS ngây thơ:** ký một block gần như **miễn phí**. Vậy tại sao không ký **cả hai** nhánh? Nhánh nào thắng bạn cũng có thưởng!

Nếu **mọi** validator đều lý trí và làm vậy, mạng **không bao giờ hội tụ** về một nhánh. Đó là **nothing-at-stake problem** — "chẳng mất gì cả".

Tệ hơn: nó khiến **double-spend rẻ đi**. Kẻ tấn công chỉ cần tạo một nhánh riêng, và các validator sẽ vui vẻ ký cả nhánh đó vì không mất gì.

### Lời giải: Slashing

```
Validator ký hai block mâu thuẫn nhau
        ↓
Bất kỳ ai cũng nộp được BẰNG CHỨNG lên chuỗi
        ↓
Stake của validator đó bị ĐỐT + bị loại khỏi mạng
```

Điều này biến *"chẳng mất gì"* thành *"mất rất nhiều"*. Ký hai nhánh giờ đây không còn miễn phí — nó là **hành vi tự sát tài chính**.

> 🧪 [Phần 14](#14-code-minh-hoạ) có code chạy được: validator ký hai block cùng slot → bị phát hiện → đốt 1.000.000 coin.

Điểm tinh tế của thiết kế này: **bằng chứng phạm tội tự nó nằm trên chuỗi**. Hai chữ ký mâu thuẫn của cùng một validator **là** bằng chứng toán học không thể chối cãi ([Bài 2](lesson_2_ma_hoa_bat_doi_xung.md): chữ ký số cho tính **chống chối bỏ**). Không cần toà án, không cần điều tra — chỉ cần một người nhặt được hai chữ ký đó và nộp lên.

Cơ chế này trong Ethereum gọi là **Casper FFG**, do Vitalik Buterin và Virgil Griffith thiết kế.

---

## 7. 📚 The Merge — điều đã xảy ra sau video

Video kết bằng "Ethereum **dự định** chuyển sang PoS". Cập nhật:

| Mốc            | Sự kiện                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------- |
| **01/12/2020** | **Beacon Chain** khởi động — chuỗi PoS chạy **song song**, chưa xử lý giao dịch               |
| **15/09/2022** | **THE MERGE** — chuỗi PoW cũ hợp nhất vào Beacon Chain. PoW **tắt vĩnh viễn** trên Ethereum   |
| **12/04/2023** | **Shanghai/Capella** — cho phép **rút** stake (trước đó chỉ khoá vào được, không rút ra được) |
| **13/03/2024** | **Dencun** — EIP-4844 (proto-danksharding), giảm mạnh phí cho Layer 2                         |

### Kết quả thật sự

| Chỉ số              | Thay đổi                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Tiêu thụ điện**   | Giảm **~99,95%** — từ ~78 TWh/năm xuống ~0,01 TWh/năm                                                                                                  |
| **Phát hành ETH**   | Giảm ~88% — từ ~4,3%/năm xuống ~0,5%/năm                                                                                                               |
| **Sự cố**           | The Merge diễn ra **không gián đoạn dịch vụ** — có lẽ là ca nâng cấp hạ tầng phức tạp nhất từng thực hiện trên hệ thống đang chạy với hàng trăm tỷ USD |
| **Thời gian block** | Từ ~13 giây biến động → **chính xác 12 giây** cố định                                                                                                  |
| **Tính chung cuộc** | Từ *xác suất* (đợi 6 block) → **chung cuộc kinh tế** sau ~12,8 phút                                                                                    |

> 💡 Điểm cuối cùng đáng chú ý: PoW chỉ cho **chung cuộc xác suất** ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md): càng bị chôn sâu càng khó đảo). Ethereum PoS có khái niệm **finality** thật — sau khi block được *finalized*, đảo ngược nó đòi hỏi **đốt ít nhất 1/3 tổng stake**. Đây không phải "rất khó", mà là "có giá cụ thể, và cái giá đó là hàng chục tỷ USD".

---

## 8. 📚 Ethereum PoS hoạt động thật sự thế nào

Video mô tả PoS ở mức khái niệm. Đây là cơ chế thật.

### Cấu trúc thời gian

```
1 SLOT  = 12 giây     → 1 block (nếu validator được chọn online)
1 EPOCH = 32 slot     = 6,4 phút
Chung cuộc = 2 epoch  ≈ 12,8 phút
```

### Vai trò trong mỗi slot

```
Mỗi slot:
  ├─ 1 PROPOSER  — được RANDAO chọn, tạo block
  └─ ~N ATTESTER — hàng chục nghìn validator BỎ PHIẾU xác nhận block đó hợp lệ
```

Chú ý: phần lớn công việc **không phải** tạo block, mà là **chứng thực** (attest). Mỗi validator được xếp vào một **committee**, mỗi epoch bỏ phiếu đúng một lần.

### Điều kiện tham gia

|                 | Giá trị                                                      |
| --------------- | ------------------------------------------------------------ |
| Stake tối thiểu | **32 ETH** cho một validator                                 |
| Có hơn 32 ETH?  | Chạy nhiều validator, mỗi cái đúng 32 ETH                    |
| Ít hơn 32 ETH?  | Tham gia **staking pool** (xem [phần 12](#12--phê-phán-pos)) |
| Phần cứng       | Máy tính thường + Internet ổn định. **Không cần** ASIC/GPU   |

> 💡 So với PoW: rào cản gia nhập chuyển từ **kỹ thuật** (phải mua ASIC, phải có điện công nghiệp) sang thuần **vốn** (phải có 32 ETH). Tốt hơn hay tệ hơn thì tuỳ góc nhìn — [phần 12](#12--phê-phán-pos) bàn tiếp.

### Gasper — hai thuật toán ghép lại

Ethereum PoS = **LMD-GHOST** + **Casper FFG**:

| Thành phần     | Nhiệm vụ                                                                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LMD-GHOST**  | *Chọn nhánh nào* — luật fork choice, chọn nhánh có nhiều phiếu chứng thực tích luỹ nhất (tương tự "chuỗi dài nhất" ở PoW nhưng đếm phiếu thay vì đếm công) |
| **Casper FFG** | *Chốt vĩnh viễn* — cơ chế chung cuộc: khi ≥ 2/3 stake bỏ phiếu cho một checkpoint, nó được *justified*; hai checkpoint liên tiếp → *finalized*             |

### Inactivity leak — cơ chế tự phục hồi

Nếu > 1/3 validator offline, mạng không thể finalize. Ethereum có một cơ chế tinh tế:

```
Không finalize được trong nhiều epoch
        ↓
Validator OFFLINE bị RÒ RỈ stake dần dần
        ↓
Tỷ trọng stake của họ giảm xuống
        ↓
Số validator online lại vượt 2/3  →  mạng finalize trở lại
```

Nghĩa là mạng **tự chữa lành** ngay cả khi mất một phần ba số validator, mà **không cần** ai can thiệp. Đây là thứ PoW không có tương đương.

---

## 9. 📚 Các tội bị slashing

Ethereum có đúng **ba** hành vi bị phạt tịch thu:

| Tội                 | Mô tả                                              | Vì sao nguy hiểm               |
| ------------------- | -------------------------------------------------- | ------------------------------ |
| **Double proposal** | Đề xuất 2 block khác nhau ở cùng 1 slot            | Cố tình tạo fork               |
| **Double vote**     | Chứng thực 2 block khác nhau ở cùng 1 target epoch | Chính là *nothing at stake*    |
| **Surround vote**   | Bỏ phiếu "bao" quanh phiếu trước của chính mình    | Cố viết lại lịch sử đã cam kết |

### Mức phạt

```
Phạt ban đầu:     ~1 ETH (1/32 stake)
Bị buộc thoát:    validator bị loại khỏi mạng
Correlated penalty: PHẠT THÊM, tỷ lệ với SỐ NGƯỜI cùng bị phạt trong 36 ngày
```

**Correlated penalty (phạt liên đới)** là chi tiết thiết kế xuất sắc nhất:

```
1 validator bị slash một mình     →  mất ~1 ETH  (nhẹ)
1/3 mạng cùng bị slash một lúc    →  mất TOÀN BỘ 32 ETH mỗi người
```

Ý nghĩa: **lỗi cấu hình cá nhân** (chạy nhầm hai máy cùng khoá) bị phạt nhẹ, còn **tấn công có phối hợp** bị phạt huỷ diệt. Hệ thống phân biệt được **bất cẩn** với **cố ý** — không bằng cách đọc ý định, mà bằng cách quan sát **tương quan thống kê**.

> ⚠️ Cũng vì thế mà chạy validator dự phòng "cho chắc" là cách **nhanh nhất** để bị slash: hai máy cùng private key sẽ ký hai lần. Trong staking, **dư thừa không phải an toàn — nó là rủi ro**.

**Phân biệt slashing với inactivity penalty:**

|             | Slashing             | Inactivity penalty                      |
| ----------- | -------------------- | --------------------------------------- |
| Nguyên nhân | Hành vi **gian dối** | Chỉ **offline**                         |
| Mức         | Nặng, bị loại        | Rất nhẹ (mất xấp xỉ số lẽ ra kiếm được) |
| Khôi phục   | Không                | Online lại là hết                       |

> 💡 Thiết kế này nói lên triết lý: **lười thì bị phạt nhẹ, dối trá thì bị huỷ diệt.**

---

## 10. 📚 Tấn công tầm xa & tính chủ quan yếu

Đây là phản biện tinh vi nhất chống PoS, và cũng là điểm mà PoS thật sự **có** một điểm yếu lý thuyết so với PoW.

### Long-range attack

```
Kẻ tấn công mua private key của các validator ĐÃ RÚT STAKE TỪ LÂU
        ↓
Họ không còn gì để mất — stake đã rút hết rồi, slashing vô nghĩa
        ↓
Dùng khoá cũ, viết lại lịch sử TỪ MỘT BLOCK RẤT XA TRONG QUÁ KHỨ
        ↓
Tạo ra một chuỗi thay thế dài, trông hoàn toàn hợp lệ
```

**Trong PoW việc này bất khả thi** — viết lại lịch sử xa đòi hỏi đốt lại toàn bộ điện năng từ điểm đó, không có đường tắt. Đây là ưu điểm thật sự của PoW.

**Trong PoS**, tạo chuỗi giả gần như **miễn phí** — chỉ cần ký, mà ký thì không tốn gì.

### Lời giải: Weak Subjectivity (tính chủ quan yếu)

```
Node MỚI hoặc node offline QUÁ LÂU
        ↓
Phải nhận một "weak subjectivity checkpoint" — một hash block gần đây
   (lấy từ nguồn đáng tin: bạn bè, nhiều website, mã nguồn client)
        ↓
Node từ chối MỌI lịch sử mâu thuẫn với checkpoint đó
```

Trong Ethereum, chu kỳ chủ quan yếu là khoảng **vài tháng**. Node online liên tục **không bị ảnh hưởng** — nó đã tự thấy chuỗi thật diễn ra.

> ⚠️ **Đây là một sự đánh đổi triết học thật sự, đừng bỏ qua nó.**
>
> - **PoW** cho **tính khách quan tuyệt đối**: đưa cho một node hai chuỗi, nó chọn được chuỗi đúng **chỉ bằng cách nhìn vào dữ liệu** — không cần thông tin nào từ bên ngoài. Đây là một tính chất rất mạnh.
> - **PoS** cần một **điểm neo tin cậy ban đầu**. Không nhiều — chỉ một hash, lấy một lần khi đồng bộ.
>
> Phe Bitcoin coi đây là lỗi chí mạng: *"PoS không thực sự phi tập trung, vì vẫn phải tin ai đó ở bước khởi đầu."*
> Phe Ethereum phản biện: *"trong thực tế bạn vẫn phải tin nguồn tải phần mềm client, tin genesis block, tin danh sách peer khởi động. Bạn đã tin những thứ đó rồi — thêm một hash không thay đổi mô hình an ninh."*
>
> Cả hai lập luận đều có lý. Đây không phải câu hỏi đã được giải quyết dứt điểm.

---

## 11. 📚 Hai mô hình bảo mật kinh tế: dòng chảy vs kho vốn

Đây là cách đúng nhất để so sánh PoW và PoS, và nó không có trong video.

```
PoW: bảo mật = CHI PHÍ DÒNG CHẢY (flow)
     Phải LIÊN TỤC đốt tiền để duy trì an toàn.
     Ngừng trả → an toàn biến mất ngay.
     Tấn công = thuê/mua sức tính TRONG một khoảng thời gian.

PoS: bảo mật = KHO VỐN RỦI RO (stock)
     Vốn được KHOÁ VÀO một lần và ở lại đó.
     Tấn công = phải SỞ HỮU vốn, và MẤT nó khi tấn công.
```

### Hệ quả

| Câu hỏi                          | PoW                                   | PoS                                             |
| -------------------------------- | ------------------------------------- | ----------------------------------------------- |
| Chi phí **duy trì** an ninh      | Cao và liên tục (tiền điện hàng ngày) | Gần bằng 0                                      |
| Chi phí **tấn công**             | Chi phí thuê trong vài giờ            | Phải mua toàn bộ vốn                            |
| Sau tấn công, kẻ tấn công còn gì | Phần cứng còn nguyên                  | Mất sạch (bị slash)                             |
| Ai trả tiền cho an ninh          | Người nắm coin, qua **lạm phát**      | Người nắm coin, qua lạm phát **thấp hơn nhiều** |

> 🧪 [Phần 14](#14-code-minh-hoạ) tính cụ thể: tấn công PoS Ethereum cần mua ~17 triệu ETH (~51 tỷ USD, **và mất luôn**); tấn công PoW ở quy mô Bitcoin tốn ~0,5 triệu USD/giờ (**và giữ được phần cứng**).

**Nhận định công bằng cho cả hai phía:**

- **PoS an toàn hơn về mặt kinh tế** — chi phí tấn công cao hơn nhiều bậc, và kẻ tấn công mất sạch vốn.
- **PoW đơn giản hơn và khách quan hơn** — ít giả định, không cần weak subjectivity, đã được kiểm chứng 15+ năm không gián đoạn.
- **PoS phức tạp hơn rất nhiều** — nhiều tham số, nhiều tình huống biên. Độ phức tạp bản thân nó là một rủi ro.

> 💡 Đây không phải chuyện "cái nào tốt hơn". Đó là **hai bộ đánh đổi khác nhau**, phục vụ hai ưu tiên khác nhau. Bitcoin ưu tiên **tính đơn giản và bất biến**; Ethereum ưu tiên **hiệu quả và khả năng tiến hoá**.

---

## 12. 📚 Phê phán PoS

Để học cho đầy đủ, phải biết cả những phản biện chính đáng.

### 1. Tập trung hoá qua staking pool

32 ETH là rào cản cao. Phần lớn người dùng tham gia qua pool, dẫn đến tập trung:

```
Lido            ~28% tổng stake
Coinbase        ~9%
Binance, Kraken ...
```

> ⚠️ Nếu một thực thể vượt **33%**, họ chặn được finality. Vượt **50%**, họ kiểm duyệt được giao dịch. Vượt **66%**, họ finalize được block gian dối. Đây là mối lo có thật, không phải giả định.

> 💡 Nhưng đối chiếu cho công bằng: các **mining pool** PoW cũng tập trung tương đương (từng có lúc GHash.io chạm 51% hashrate Bitcoin năm 2014). Tập trung hoá là **lực hấp dẫn kinh tế**, không phải khiếm khuyết riêng của cơ chế đồng thuận nào.

### 2. "Nhà giàu càng giàu"?

Phản biện phổ biến nhất — và **phần lớn là hiểu sai**.

Phần thưởng **tỷ lệ thuận** với stake, nên **tỷ lệ sở hữu tương đối không đổi**. Ai giữ 10% mạng thì sau 10 năm vẫn giữ xấp xỉ 10%.

> 🧪 [Phần 14](#14-code-minh-hoạ) chạy 10.000 epoch và xác nhận: 10%/30%/60% → 9,3%/31,9%/58,8%. Dao động là do ngẫu nhiên, không có xu hướng tích luỹ.

**Nhưng phản biện vẫn đúng một nửa**, ở hai chỗ:

- **Người KHÔNG stake bị pha loãng.** Phát hành mới chảy về phía người stake. Ai chỉ giữ coin trong ví bị giảm tỷ trọng dần.
- **Lợi thế quy mô.** Người có 32.000 ETH tự chạy validator, giữ 100% phần thưởng. Người có 1 ETH phải qua pool, mất 10% phí. Bất bình đẳng không nằm ở tỷ lệ phần thưởng, mà ở **chi phí tiếp cận**.

> 💡 So sánh cho đúng: PoW cũng có lợi thế quy mô, thậm chí **mạnh hơn** (giá điện sỉ, ASIC đời mới, quy mô làm mát). Không cơ chế nào miễn nhiễm.

### 3. Rủi ro kiểm duyệt và pháp lý

Validator là **thực thể có danh tính**, chạy trên hạ tầng có địa chỉ pháp lý (AWS, exchange). Họ **tuân thủ pháp luật được**, nghĩa là họ **bị ép kiểm duyệt được**.

Sau lệnh trừng phạt Tornado Cash (2022), một tỷ lệ đáng kể block Ethereum tuân thủ danh sách OFAC. Thợ đào PoW nặc danh ở vùng xa khó bị ép hơn nhiều.

> Đây có lẽ là **phê phán mạnh nhất** đối với PoS: nó làm cho **chống kiểm duyệt** — một trong bốn tính chất cốt lõi ở [Bài 4](lesson_4_ung_dung_blockchain.md) — trở nên mong manh hơn.

### 4. Liquid staking derivatives

Stake xong nhận token đại diện (stETH), đem token đó đi dùng tiếp trong DeFi. Tiện lợi, nhưng tạo **rủi ro hệ thống chồng tầng**: một sự cố ở tầng staking lan sang toàn bộ DeFi đang dùng stETH làm tài sản thế chấp.

---

## 13. 📚 Các biến thể

| Cơ chế               | Ý tưởng                                                    | Dùng ở                   | Đánh đổi                                                                |
| -------------------- | ---------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------- |
| **PoS thuần**        | Chọn theo stake                                            | Ethereum                 | Cân bằng                                                                |
| **DPoS** (Delegated) | Người nắm coin **bầu** ra một số ít đại biểu tạo block     | EOS, Tron                | Rất nhanh, nhưng rất tập trung (21–101 node)                            |
| **LPoS** (Leased)    | Cho thuê stake cho validator, coin **không rời ví**        | Waves                    | Giữ được quyền tự quản                                                  |
| **NPoS** (Nominated) | Người đề cử chọn validator và **cùng chịu slashing**       | Polkadot                 | Người đề cử có động cơ chọn kỹ                                          |
| **PoA** (Authority)  | Validator là các thực thể **đã được định danh và tin cậy** | Chuỗi liên minh, testnet | Nhanh, nhưng cần tin ([Bài 4](lesson_4_ung_dung_blockchain.md), phần 9) |
| **PoH** (History)    | Đồng hồ mật mã sắp thứ tự sự kiện, ghép **cùng** PoS       | Solana                   | Rất nhanh, yêu cầu phần cứng cao                                        |
| **PoSpace/Time**     | Đặt cọc bằng **dung lượng ổ cứng**                         | Chia                     | Ít điện hơn PoW, nhưng hao mòn SSD                                      |

> 💡 Nhìn theo một trục duy nhất: **tất cả** đều trả lời cùng một câu hỏi — *"bạn đặt cọc bằng thứ gì?"* Điện năng (PoW), vốn (PoS), danh tiếng (PoA), dung lượng (PoSpace). Và luôn có cùng một đánh đổi: **càng ít bên tham gia thì càng nhanh, càng nhiều bên thì càng khó bị kiểm soát.** Đó chính là [trilemma ở Bài 4](lesson_4_ung_dung_blockchain.md).

### 📚 Ouroboros (Cardano) — cùng từ vựng, khác thiết kế

> Dựa trên video **"Cardano — Simply Explained"** (`Do8rHvr65ZA`, 7:46). Video này ghi đầu 2018, nên phần lớn nội dung của nó là **kế hoạch**, không phải thứ đã chạy. Mục này đối chiếu với 2026.

Cardano dùng **đúng bộ từ vựng** mà [phần 8](#8--ethereum-pos-hoạt-động-thật-sự-thế-nào) đã dựng cho Ethereum — *epoch*, *slot*, người được chọn tạo block — nhưng nội dung khác nhau ở vài chỗ quan trọng.

> `02:09` *"Cardano không cho ai cũng đào block. Mạng lưới **bầu ra một số node** để tạo block tiếp theo. Chúng được gọi là **slot leader**."*
> `02:20` *"Thời gian được chia thành các **epoch**. Mỗi epoch chia thành các **slot** — một khoảng ngắn mà trong đó **đúng một** block được tạo."*

| | **Ethereum (Gasper)** | **Cardano (Ouroboros)** |
|---|---|---|
| Độ dài slot | 12 giây | 1 giây |
| Slot mỗi epoch | 32 (epoch ≈ 6,4 phút) | 432.000 (epoch = 5 ngày) |
| Mỗi slot có block? | gần như luôn có | **không** — phần lớn slot trống, block ra ~20 giây một lần |
| Ai biết mình được chọn | công khai, biết trước cả epoch | **chỉ mình người đó biết**, tới lượt mới công bố |
| Nguồn ngẫu nhiên | RANDAO + VDF ([phần 3](#3-chọn-validator-thế-nào)) | hàm ngẫu nhiên kiểm chứng được, chạy riêng ở từng node |
| **Slashing** | **có** — mất tới toàn bộ cọc ([phần 9](#9--các-tội-bị-slashing)) | **không có** |
| Cọc có bị khoá không | có | **không** — coin ở nguyên trong ví, uỷ quyền không rời tay |

Hai hàng cuối là khác biệt đáng suy nghĩ nhất, và nó đụng thẳng vào [phần 6](#6-nothing-at-stake-và-slashing):

> **Cardano không phạt cắt cọc.** Lập luận của nó: người vận hành pool sống bằng phần thưởng và bằng danh tiếng, làm bậy thì mất người uỷ quyền và mất thu nhập — thế là đủ răn đe, không cần đe doạ tịch thu vốn.
>
> Ethereum thì cho rằng chỉ mất thu nhập là **chưa đủ**, vì kẻ tấn công có động cơ nằm ngoài hệ thống. Nên nó thêm hình phạt phá huỷ vốn, kèm **phạt tương quan** — càng nhiều người cùng phạm một lúc thì mức phạt càng nặng.
>
> Đây là hai câu trả lời khác nhau cho cùng câu hỏi ở [phần 11](#11--hai-mô-hình-bảo-mật-kinh-tế-dòng-chảy-vs-kho-vốn): **an ninh nên đến từ dòng thu nhập hay từ kho vốn?** Không có bên nào hiển nhiên đúng; hãy nhớ hai lựa chọn này khi đánh giá bất kỳ chuỗi PoS nào.

#### Kho bạc on-chain — thứ Cardano làm được và gần như không ai khác làm

Đây là phần đáng giá nhất của video, và là **chủ đề chưa xuất hiện ở bất kỳ bài nào khác trong khoá học**.

Video đặt câu hỏi ở `05:29`: một dự án gọi vốn bằng ICO, tiêu hết tiền sau vài năm — rồi lấy gì phát triển tiếp? *"Bán thêm một đồng nữa và gọi vốn lần nữa à?"* Nó gọi đó là vấn đề **tính bền vững**.

Lời giải ở `06:10`:

```
   Mỗi giao dịch trích một phần rất nhỏ  ──▶  KHO BẠC
                                              │  ví đặc biệt KHÔNG AI kiểm soát
                                              ▼
   Lập trình viên nộp đề xuất: làm gì, cần bao nhiêu tiền
                                              ▼
   Cộng đồng bỏ phiếu  ──▶  đề xuất thắng được cấp tiền tự động
```

> `07:17` Video tự nêu đúng rủi ro: *"nó phụ thuộc vào một hệ thống bỏ phiếu công bằng để ngăn người ta chiếm quyền kiểm soát."*

**Tới 2026:** đây là một trong số ít lời hứa của video **đã thành hiện thực**. Cardano có kho bạc on-chain vận hành thật, có quy trình đề xuất và bỏ phiếu cấp vốn, và sau đó là cả một khung quản trị on-chain hoàn chỉnh. Rất ít chuỗi lớn làm được điều này — phần lớn vẫn dựa vào một quỹ hoặc một công ty đứng sau.

Nhưng rủi ro mà video nêu cũng thành hiện thực đúng như vậy: bỏ phiếu theo token thì **giàu là mạnh**, tỉ lệ tham gia thấp, và chất lượng đề xuất rất chênh lệch. Đây đúng là bài toán ở [Bài 10 §16](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md#16--dao-trong-thực-tế--the-dao-constitutiondao-và-bài-toán-bỏ-phiếu) — một DAO cỡ quốc gia, với mọi ưu và nhược của DAO.

#### Chấm điểm phần còn lại của video

| Video 2018 hứa | Tới 2026 |
|---|---|
| PoS Ouroboros thay PoW | ✅ Chạy thật, ổn định nhiều năm |
| Kho bạc + quản trị on-chain | ✅ Có thật, và là điểm mạnh hiếm |
| **RINA** — chia mạng thành mạng con `03:02` | ❌ **Không bao giờ được triển khai.** Lớp mạng đi hướng khác |
| Xử lý lưu trữ bằng cắt tỉa/nén/phân mảnh `03:39` | ⏸️ Video tự nói *"chưa ưu tiên, để cuối 2018 hoặc đầu 2019"* — vấn đề dữ liệu phình to vẫn còn nguyên ở mọi chuỗi |
| "Internet của các blockchain" `04:41` | 🟡 Liên thông chuỗi vẫn là bài toán chưa giải, và cầu nối là hạng mục bị hack nhiều nhất ([Bài 10 §19](../mo_rong/lesson_10_tai_chinh_phi_tap_trung.md#19--bảo-mật-smart-contract--phân-loại-lỗi-và-bảng-các-vụ-lớn)) |
| Gắn metadata tuỳ chọn cho giao dịch `05:15` | ✅ Có. Nhưng xem [Bài 13](../mo_rong/lesson_13_gdpr_va_blockchain.md) trước khi định gắn dữ liệu cá nhân vào đó |
| "Thế hệ thứ ba" | ⏸️ Cách phân loại này không trụ lại. Smart contract của Cardano mãi 2021 mới có — bốn năm sau khi ra mắt |

> 🔍 **Bài học rút ra không phải về Cardano.** Nó là: **cách một dự án tự mô tả trong video giới thiệu và thứ nó thật sự giao được sau tám năm là hai danh sách khác nhau.** Video này khá trung thực — nó dùng chữ *"muốn"*, *"dự định"*, *"đang cân nhắc"* rất nhiều, và kết bằng `07:24` *"dự án còn rất trẻ và còn một chặng đường dài"*. Khi đọc bất kỳ giới thiệu chuỗi nào, hãy tách hai cột: **cái đang chạy** và **cái đang hứa**.

---

## 14. Code minh hoạ

Chỉ dùng thư viện chuẩn của Node. Kiểm chứng bằng số 4 điều: chọn theo trọng số, "nhà giàu càng giàu", slashing, và chi phí tấn công.

```typescript
// pos.ts — mô phỏng Proof-of-Stake: chọn validator theo trọng số, slashing, và
// kiểm chứng bằng số hai câu hỏi hay bị hiểu sai:
//   (a) 'nhà giàu càng giàu' — đúng hay sai?
//   (b) tấn công 51% có lời không?
// Chạy: node pos.ts
import { createHash } from "node:crypto";
import { strict as assert } from "node:assert";

type Stakes = Record<string, number>;

const sum = (v: Stakes): number => Object.values(v).reduce((a, b) => a + b, 0);
const pct = (x: number): string => (x * 100).toFixed(1) + "%";

/** Chọn validator ngẫu nhiên có trọng số theo stake. Tất định theo seed. */
function pick(validators: Stakes, seed: number): string {
  const total = sum(validators);
  // random tất định từ seed -> mọi node chọn ra CÙNG một validator
  const digest = createHash("sha256").update(String(seed)).digest("hex");
  const r = Number(BigInt("0x" + digest) % BigInt(total));
  let acc = 0;
  for (const v of Object.keys(validators).sort()) {
    acc += validators[v];
    if (r < acc) return v;
  }
  throw new Error("unreachable");
}

function demoWeighted(): void {
  const v: Stakes = { alice: 100, bob: 300, carol: 600 };   // tổng 1000
  const counts: Record<string, number> = { alice: 0, bob: 0, carol: 0 };
  const N = 100_000;
  for (let i = 0; i < N; i++) counts[pick(v, i)]++;
  console.log("(a) Xac suat duoc chon TY LE THUAN voi stake:");
  for (const k of Object.keys(v).sort()) {
    const exp = v[k] / 1000, act = counts[k] / N;
    console.log(`    ${k.padEnd(6)} stake ${String(v[k]).padStart(4)} -> ky vong ${pct(exp)}, thuc te ${pct(act)}`);
    assert(Math.abs(act - exp) < 0.01, `${k} lech qua nhieu`);
  }
}

/** Phần thưởng tỷ lệ thuận với stake -> TỶ LỆ TƯƠNG ĐỐI KHÔNG ĐỔI. */
function demoRichGetRicher(): void {
  const v: Stakes = { alice: 100, bob: 300, carol: 600 };
  const t0 = sum(v);
  const start: Stakes = {};
  for (const k of Object.keys(v)) start[k] = v[k] / t0;
  for (let epoch = 0; epoch < 10_000; epoch++) {
    v[pick(v, epoch)] += 1;                    // phần thưởng cố định cho người tạo block
  }
  const t1 = sum(v);
  console.log("\n(b) 'Nha giau cang giau'? Ty le SO HUU sau 10.000 epoch:");
  for (const k of Object.keys(v).sort()) {
    const end = v[k] / t1;
    console.log(`    ${k.padEnd(6)} ${pct(start[k])} -> ${pct(end)}`);
    assert(Math.abs(end - start[k]) < 0.02, "ty le tuong doi phai gan nhu khong doi");
  }
  console.log("    => Nguoi CO stake giu nguyen ty le. Nguoi KHONG stake bi PHA LOANG.");
}

/** Validator ký hai block ở cùng slot -> bị phát hiện -> mất stake. */
function demoSlashing(): void {
  const stake: Record<string, number> = { mallory: 1_000_000 };
  const signed = new Map<number, string>();     // slot -> block đã ký
  const slashed = new Set<string>();

  function sign(v: string, slot: number, block: string): [string, number] {
    if (slashed.has(v)) throw new Error("da bi loai");
    if (signed.has(slot) && signed.get(slot) !== block) {   // BẰNG CHỨNG double-sign
      const burned = stake[v];                             // đốt toàn bộ (đơn giản hoá)
      stake[v] = 0;
      slashed.add(v);
      return ["SLASHED", burned];
    }
    signed.set(slot, block);
    return ["OK", 0];
  }

  assert(sign("mallory", 5, "blockA")[0] === "OK");
  const [res, burned] = sign("mallory", 5, "blockB");        // ký chuỗi thứ 2 cùng slot
  console.log(`\n(c) Slashing: mallory ky 2 block cung slot -> ${res}, dot ${burned.toLocaleString("en-US")} coin`);
  assert(res === "SLASHED" && stake["mallory"] === 0);
  console.log("    => 'Nothing at stake' bi triet tieu: ky nhieu chuoi = MAT TIEN");
}

/** So chi phí tấn công 51%: PoW = chi phí LUỒNG, PoS = vốn RỦI RO. */
function demoAttackCost(): void {
  const supply = 120_000_000, price = 3_000;                 // ETH
  const stakedRatio = 0.28;
  const staked = supply * stakedRatio;
  const need = staked * 0.51;
  const costPos = need * price;

  const hashrateCostPerDay = 25_000_000;                     // ~chi phí đào BTC toàn mạng/ngày (USD)
  const costPow1h = hashrateCostPerDay / 24 * 0.51;

  console.log("\n(d) Chi phi tan cong 51%:");
  console.log(`    PoS: phai MUA ${need.toLocaleString("en-US")} ETH = $${(costPos / 1e9).toFixed(1)} ty`);
  console.log("         -> tan cong xong bi SLASH -> MAT LUON so von do");
  console.log(`    PoW: thue hashrate ~$${(costPow1h / 1e6).toFixed(1)} trieu/gio`);
  console.log("         -> tan cong xong PHAN CUNG VAN CON -> tan cong lai duoc");
  assert(costPos > costPow1h * 24 * 365, "von PoS phai lon hon nhieu chi phi PoW");
  console.log("    => PoW: bao mat = CHI PHI DONG (flow) | PoS: bao mat = VON RUI RO (stock)");
}

demoWeighted(); demoRichGetRicher(); demoSlashing(); demoAttackCost();
console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
(a) Xac suat duoc chon TY LE THUAN voi stake:
    alice  stake  100 -> ky vong 10.0%, thuc te 10.0%
    bob    stake  300 -> ky vong 30.0%, thuc te 29.9%
    carol  stake  600 -> ky vong 60.0%, thuc te 60.2%

(b) 'Nha giau cang giau'? Ty le SO HUU sau 10.000 epoch:
    alice  10.0% -> 9.3%
    bob    30.0% -> 31.9%
    carol  60.0% -> 58.8%
    => Nguoi CO stake giu nguyen ty le. Nguoi KHONG stake bi PHA LOANG.

(c) Slashing: mallory ky 2 block cung slot -> SLASHED, dot 1,000,000 coin
    => 'Nothing at stake' bi triet tieu: ky nhieu chuoi = MAT TIEN

(d) Chi phi tan cong 51%:
    PoS: phai MUA 17,136,000 ETH = $51.4 ty
         -> tan cong xong bi SLASH -> MAT LUON so von do
    PoW: thue hashrate ~$0.5 trieu/gio
         -> tan cong xong PHAN CUNG VAN CON -> tan cong lai duoc
    => PoW: bao mat = CHI PHI DONG (flow) | PoS: bao mat = VON RUI RO (stock)

All assertions passed.
```

**Bốn điều code này dạy:**

| Kết quả                        | Bài học                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `10.0% / 29.9% / 60.2%`        | Chọn theo trọng số hoạt động đúng. Và chú ý hàm `pick()` là **tất định theo seed** — mọi node chạy ra cùng validator, đúng luật tất định ở [Bài 3](lesson_3_smart_contract.md). |
| `10% → 9.3%`, `60% → 58.8%`    | **"Nhà giàu càng giàu" là hiểu sai** — tỷ lệ tương đối không đổi. Vấn đề thật nằm ở người *không* stake bị pha loãng.                                                           |
| `SLASHED, dot 1,000,000`       | Slashing triệt tiêu nothing-at-stake. Bằng chứng là **hai chữ ký mâu thuẫn** — tự nó là chứng cứ toán học.                                                                      |
| `$51.4 ty` vs `$0.5 trieu/gio` | Hai mô hình bảo mật hoàn toàn khác nhau: **kho vốn** vs **dòng chảy**.                                                                                                          |

**Tự thử nghiệm:**

- Trong `demoRichGetRicher`, đổi phần thưởng từ `+= 1` (cố định) sang `+= v[w] * 0.001` (tỷ lệ với stake) — xem tỷ lệ tương đối có đổi không. Kết quả sẽ cho bạn hiểu **vì sao** thiết kế phần thưởng quyết định chuyện tập trung hoá.
- Thêm một validator thứ 4 **không stake** với số coin cố định, tính tỷ trọng của họ theo thời gian → thấy hiệu ứng **pha loãng** bằng số.
- Sửa `pick()` để dùng `seed = block_truoc.hash` thay vì số đếm, rồi thử để validator cuối cùng "bỏ lượt" nhằm đổi kết quả — bạn vừa tái hiện **last-revealer bias** của RANDAO ở [phần 3](#3-chọn-validator-thế-nào).

---

## 15. Bảng so sánh tổng

|                              | **Proof of Work**                     | **Proof of Stake**                                 |
| ---------------------------- | ------------------------------------- | -------------------------------------------------- |
| Đặt cọc bằng                 | Điện năng + phần cứng                 | Coin bị khoá                                       |
| Người tạo block gọi là       | Miner (thợ đào)                       | Validator / Forger                                 |
| Cách chọn                    | Ai giải câu đố trước                  | Chọn giả ngẫu nhiên theo stake                     |
| Rào cản gia nhập             | ASIC + điện giá rẻ                    | Vốn (Ethereum: 32 ETH)                             |
| Tiêu thụ điện                | Rất cao (~100 TWh/năm)                | Rất thấp (~0,01 TWh/năm)                           |
| Phát hành mới                | Cao (cần bù tiền điện)                | Thấp                                               |
| Trừng phạt gian dối          | Gián tiếp (mất tiền điện)             | **Trực tiếp** (slashing)                           |
| Chi phí tấn công 51%         | Thuê hashrate theo giờ                | Mua > 50% stake                                    |
| Sau tấn công còn tài sản?    | ✅ Có (phần cứng)                      | ❌ Không (bị đốt)                                   |
| Thuê được năng lực tấn công? | ✅ Có                                  | ❌ Không                                            |
| Tính chung cuộc              | Xác suất (đợi N block)                | **Chung cuộc kinh tế** (~12,8 phút)                |
| Tính khách quan              | **Tuyệt đối**                         | Chủ quan yếu (cần checkpoint)                      |
| Điểm yếu riêng               | Lãng phí, rác điện tử, pool tập trung | Long-range attack, staking pool, rủi ro kiểm duyệt |
| Độ phức tạp                  | Đơn giản                              | Phức tạp hơn nhiều                                 |
| Đã kiểm chứng                | 15+ năm                               | Ethereum từ 2022                                   |
| Ví dụ                        | Bitcoin, Litecoin, Monero             | Ethereum, Cardano, Solana, Polkadot                |

---

## 16. Từ điển thuật ngữ

| Thuật ngữ                 | Giải thích                                                 |
| ------------------------- | ---------------------------------------------------------- |
| **Proof of Stake**        | Đồng thuận dựa trên vốn đặt cọc thay vì công sức tính toán |
| **Stake**                 | Lượng coin bị khoá để tham gia làm validator               |
| **Validator / Forger**    | Người tạo và xác nhận block trong PoS                      |
| **Slashing**              | Tịch thu (đốt) stake khi validator gian dối                |
| **Nothing at Stake**      | Vấn đề ký nhiều nhánh vì ký không tốn gì                   |
| **Casper FFG**            | Cơ chế chung cuộc + slashing của Ethereum                  |
| **LMD-GHOST**             | Luật chọn nhánh của Ethereum PoS                           |
| **Gasper**                | LMD-GHOST + Casper FFG ghép lại                            |
| **Slot**                  | Khe 12 giây, mỗi slot 1 block                              |
| **Epoch**                 | 32 slot = 6,4 phút                                         |
| **Proposer**              | Validator được chọn tạo block trong slot đó                |
| **Attester**              | Validator bỏ phiếu xác nhận block hợp lệ                   |
| **Committee**             | Nhóm validator được phân công chứng thực                   |
| **RANDAO**                | Cơ chế sinh ngẫu nhiên chung bằng cách XOR đóng góp        |
| **VDF**                   | Hàm trễ kiểm chứng được — chống thao túng ngẫu nhiên       |
| **Last-revealer bias**    | Người tiết lộ cuối có chút ảnh hưởng lên kết quả RANDAO    |
| **Finality**              | Tính chung cuộc — block không thể bị đảo ngược             |
| **Justified / Finalized** | Hai mức chốt checkpoint trong Casper FFG                   |
| **Inactivity leak**       | Rò rỉ stake của validator offline để mạng tự phục hồi      |
| **Correlated penalty**    | Phạt nặng hơn khi nhiều validator cùng bị slash            |
| **Beacon Chain**          | Chuỗi PoS của Ethereum, khởi động 12/2020                  |
| **The Merge**             | 15/09/2022 — Ethereum chuyển PoW sang PoS                  |
| **Long-range attack**     | Dùng khoá cũ viết lại lịch sử từ rất xa                    |
| **Weak subjectivity**     | Node mới cần một checkpoint tin cậy để khởi đầu            |
| **Staking pool**          | Gộp coin nhiều người để đủ ngưỡng validator                |
| **Liquid staking**        | Nhận token đại diện (stETH) khi stake, dùng tiếp được      |
| **DPoS / LPoS / NPoS**    | Biến thể: uỷ quyền / cho thuê / đề cử                      |
| **PoA / PoH / PoSpace**   | Đặt cọc bằng danh tiếng / thời gian / dung lượng           |
| **Ultrasound money**      | ETH giảm phát khi lượng đốt vượt lượng phát hành           |

---

## 17. Câu hỏi tự kiểm tra

1. Kể 4 vấn đề của PoW.
2. Phát biểu nguyên lý chung mà **cả** PoW và PoS đều dựa vào. Chúng khác nhau ở điểm nào?
3. Vì sao PoS **không** dùng được số ngẫu nhiên thật? Liên hệ với luật tất định ở [Bài 3](lesson_3_smart_contract.md).
4. Vì sao dùng `block.timestamp` hoặc hash block trước để chọn validator là sai?
5. RANDAO hoạt động thế nào? "Last-revealer bias" là gì và VDF sửa nó ra sao?
6. Vì sao PoS phát hành ít coin mới hơn PoW rất nhiều?
7. Nêu **ba** lý do tấn công 51% trong PoS gần như bất khả thi. Lý do nào là mạnh nhất?
8. Vì sao "thuê hashrate" khả thi trong PoW nhưng không có tương đương trong PoS?
9. Giải thích nothing-at-stake. Vì sao PoW **không** gặp vấn đề này?
10. Slashing biến "chẳng mất gì" thành gì? Bằng chứng phạm tội đến từ đâu?
11. The Merge diễn ra khi nào? Ba con số thay đổi lớn nhất là gì?
12. Một slot, một epoch, và thời gian đạt chung cuộc của Ethereum là bao nhiêu?
13. Ba tội bị slashing là gì?
14. "Correlated penalty" phân biệt được điều gì với điều gì? Bằng cách nào?
15. Vì sao chạy validator dự phòng "cho chắc" lại là ý tưởng tồi?
16. Inactivity leak giúp mạng tự phục hồi thế nào?
17. Long-range attack là gì? Vì sao nó bất khả thi trong PoW?
18. Weak subjectivity là gì? Trình bày lập luận của **cả hai** phía về việc nó có phá vỡ tính phi tập trung hay không.
19. Giải thích "bảo mật = dòng chảy" vs "bảo mật = kho vốn".
20. "Nhà giàu càng giàu" trong PoS — đúng hay sai? Trả lời cho **cả hai** trường hợp: người có stake và người không stake.
21. Vì sao rủi ro kiểm duyệt trong PoS cao hơn PoW?
22. DPoS đánh đổi cái gì lấy cái gì?

---

## Tóm tắt một trang

```
PoW: đặt cọc bằng ĐIỆN | PoS: đặt cọc bằng VỐN BỊ KHOÁ
   Nguyên lý CHUNG: muốn tạo block phải bỏ ra thứ có giá trị, MẤT nó nếu gian
   Khác: PoW phạt GIÁN TIẾP (đốt điện vô ích)
         PoS phạt TRỰC TIẾP (SLASHING — tịch thu stake)

CHỌN VALIDATOR: ngẫu nhiên TỶ LỆ THUẬN với stake
   Nhưng phải là NGẪU NHIÊN GIẢ TẤT ĐỊNH (luật tất định!)
   → RANDAO (XOR đóng góp) + VDF (lộ trình)
   ✗ timestamp / hash block trước → thao túng được

TẤN CÔNG 51%: (1) rất đắt (2) mua sẽ đẩy giá (3) TỰ BẮN VÀO CHÂN
   PoW: thuê hashrate theo giờ, xong VẪN CÒN máy → tấn công lại
   PoS: phải MUA đứt, xong bị SLASH → MẤT SẠCH

NOTHING AT STAKE: ký nhiều nhánh vì ký miễn phí
   → SLASHING biến "chẳng mất gì" thành "mất tất cả"
   → bằng chứng = 2 chữ ký mâu thuẫn, tự nó là chứng cứ toán học

THE MERGE 15/09/2022 (video ra TRƯỚC mốc này)
   điện -99,95% | phát hành -88% | block 12s cố định | có FINALITY thật
   Slot 12s → Epoch 32 slot (6,4 phút) → Finalized sau 2 epoch (12,8 phút)
   Gasper = LMD-GHOST (chọn nhánh) + Casper FFG (chốt vĩnh viễn)
   3 tội slashing: double proposal | double vote | surround vote
   Correlated penalty: lỗi cá nhân phạt NHẸ, tấn công phối hợp phạt HUỶ DIỆT

ĐIỂM YẾU THẬT CỦA PoS
   Long-range attack → cần WEAK SUBJECTIVITY (một checkpoint tin cậy)
   → PoW có TÍNH KHÁCH QUAN TUYỆT ĐỐI, PoS thì không. Đánh đổi thật.
   Staking pool tập trung (Lido ~28%) | rủi ro KIỂM DUYỆT (OFAC)
   "Nhà giàu càng giàu" = HIỂU SAI (tỷ lệ không đổi) — nhưng người KHÔNG stake bị pha loãng

MÔ HÌNH BẢO MẬT
   PoW = CHI PHÍ DÒNG CHẢY (flow) — trả liên tục, ngừng là mất an toàn
   PoS = KHO VỐN RỦI RO (stock)  — khoá một lần, mất nếu gian
```

---

**Nguồn:**
- Video gốc: [Proof-of-Stake (vs proof-of-work)](https://www.youtube.com/watch?v=M3EFi_POhps) (Simply Explained – Savjee)
- Buterin & Griffith, *Casper the Friendly Finality Gadget* (2017)
- Buterin et al., *Combining GHOST and Casper* (2020) — bài báo Gasper
- [ethereum.org/en/roadmap](https://ethereum.org/en/roadmap) — tài liệu chính thức về PoS và The Merge
- Vitalik Buterin, *Proof of Stake FAQ* — phần về weak subjectivity và long-range attack

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. **Bài 5 – Proof of Stake** ← *bạn đang ở đây* — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
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
