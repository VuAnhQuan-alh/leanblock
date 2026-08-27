# Blockchain dùng để làm gì? (Use cases)

> Bài học dựa trên video **"Blockchains: how can they be used? (Use cases for Blockchains)"** (kênh *Simply Explained – Savjee*, YouTube `aQWflNQuP_o`).
> Nối tiếp [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md), [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md), [Bài 3 – Smart contract](lesson_3_smart_contract.md).
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua. Bài này **bổ sung nặng phần phản biện** — vì video use-case là loại dễ nghe thành quảng cáo nhất. Học xong bài này bạn phải biết cả **khi nào KHÔNG dùng** blockchain.

---

## Mục lục

1. [Blockchain không chỉ là tiền mã hoá](#1-blockchain-không-chỉ-là-tiền-mã-hoá)
2. [Chuỗi cung ứng & truy xuất nguồn gốc](#2-chuỗi-cung-ứng--truy-xuất-nguồn-gốc)
3. [Hồ sơ y tế](#3-hồ-sơ-y-tế)
4. [Danh tính số](#4-danh-tính-số)
5. [Công chứng & sở hữu trí tuệ](#5-công-chứng--sở-hữu-trí-tuệ)
6. [Bầu cử — và vì sao giới chuyên môn phản đối](#6-bầu-cử--và-vì-sao-giới-chuyên-môn-phản-đối)
7. [Các ứng dụng khác](#7-các-ứng-dụng-khác)
8. [📚 Khung quyết định: có thật sự cần blockchain không?](#8--khung-quyết-định-có-thật-sự-cần-blockchain-không)
9. [📚 Công khai, riêng tư, hay liên minh?](#9--công-khai-riêng-tư-hay-liên-minh)
10. [📚 Vấn đề chặng cuối — giới hạn nền tảng](#10--vấn-đề-chặng-cuối--giới-hạn-nền-tảng)
11. [📚 Chi phí & khả năng mở rộng](#11--chi-phí--khả-năng-mở-rộng)
12. [📚 Thực tế phũ phàng: những dự án đã chết](#12--thực-tế-phũ-phàng-những-dự-án-đã-chết)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Blockchain không chỉ là tiền mã hoá

Bitcoin là **ứng dụng đầu tiên** của blockchain, không phải ứng dụng duy nhất. Bản thân blockchain chỉ là một **cấu trúc dữ liệu** với 4 tính chất — và mỗi tính chất mở ra một nhóm ứng dụng khác nhau.

| Tính chất                | Nghĩa là                                     | Mở ra ứng dụng gì                          |
| ------------------------ | -------------------------------------------- | ------------------------------------------ |
| **Bất biến**             | Ghi rồi không sửa được mà không bị phát hiện | Kiểm toán, công chứng, truy xuất nguồn gốc |
| **Minh bạch**            | Ai cũng kiểm chứng được                      | Từ thiện, bầu cử, chi tiêu công            |
| **Phi tập trung**        | Không có bên nào kiểm soát                   | Danh tính, chống kiểm duyệt                |
| **Không cần trung gian** | Hai bên xa lạ giao dịch trực tiếp            | Thanh toán, chuyển tài sản, DeFi           |

> 💡 **Cách đọc đúng một use case:** hỏi ngay *"ứng dụng này khai thác tính chất nào trong 4 cái trên?"* Nếu không trả lời được, hoặc câu trả lời là "ừm... nó hiện đại", thì đó là **blockchain gắn mác**, không phải blockchain giải quyết vấn đề.

### Bài toán chung mà mọi use case dưới đây đều thuộc về

> **Nhiều bên không tin nhau cần chia sẻ chung một bộ dữ liệu, và không bên nào chấp nhận để bên kia làm chủ bộ dữ liệu đó.**

Giữ trong đầu định nghĩa này. Nó là **thước đo** để bạn tự đánh giá bất kỳ dự án blockchain nào bạn gặp sau này — kể cả những dự án chưa tồn tại.

---

## 2. Chuỗi cung ứng & truy xuất nguồn gốc

Đây là use case phi tài chính được nhắc nhiều nhất.

### Vấn đề

Một quả xoài đi từ nông trại tới siêu thị qua **hàng chục** khâu: nông dân → thu mua → sơ chế → đóng gói → vận tải → nhập khẩu → phân phối → siêu thị. Mỗi khâu là một công ty khác nhau, mỗi công ty có **hệ thống dữ liệu riêng**, và họ **không cho nhau xem sổ**.

Hệ quả: khi có lô hàng nhiễm khuẩn, truy ngược nguồn gốc mất **nhiều ngày đến vài tuần**. Trong thời gian đó, siêu thị phải thu hồi **toàn bộ** mặt hàng đó — kể cả 99% lô hàng sạch.

### Blockchain giải thế nào

```
Nông dân   →  ghi: "thu hoạch lô MG-08, Tiền Giang, 01/08"
Nhà máy    →  ghi: "đóng gói lô MG-08, Long An, 03/08"
Vận tải    →  ghi: "nhiệt độ tối đa 6°C, 05/08"
Siêu thị   →  ghi: "lên kệ Hà Nội, 07/08"
              ↓
     Tất cả trên MỘT sổ chung, không ai sửa được của ai
     Truy xuất: quét mã QR → toàn bộ hành trình trong 2 giây
```

**Vì sao dùng blockchain thay vì một cơ sở dữ liệu chung:** vì **không bên nào chịu để bên khác làm chủ cái database đó**. Nếu Walmart giữ database, nhà cung cấp sợ Walmart sửa số liệu để ép giá. Nếu nhà cung cấp giữ, Walmart không tin. Blockchain là **giải pháp chính trị** cho bài toán "ai giữ sổ", nhiều hơn là giải pháp kỹ thuật.

Ứng dụng tương tự: **kim cương** (Everledger — chống kim cương máu), **thuốc** (chống thuốc giả), **hàng xa xỉ** (chống hàng nhái), **gỗ** (chống khai thác trái phép).

### 📚 Lý thuyết bổ sung: đừng lưu dữ liệu lên chuỗi

Sai lầm phổ biến nhất của người mới: định đẩy cả ảnh, PDF, chứng nhận lên blockchain.

**Chi phí lưu 1 KB lên Ethereum:** khoảng vài chục USD. Lưu 1 MB: **hàng chục nghìn USD**. Và **mọi node trên thế giới** phải lưu bản sao đó **vĩnh viễn**.

**Cách đúng — neo bằng hash (anchoring):**

```
📄 Tài liệu thật (2 MB)  ──lưu ở──▶  IPFS / S3 / server công ty
        │
        └── SHA-256 ──▶ 32 byte hash ──ghi lên──▶ ⛓️ Blockchain
```

Bạn được cả hai:

- **Rẻ** — chỉ 32 byte lên chuỗi thay vì 2 MB. Tỉ lệ ~1:62.500 (xem [phần 13](#13-code-minh-hoạ)).
- **Vẫn chống sửa** — ai sửa file gốc, hash lệch ngay, đối chiếu với chuỗi là lộ.
- **Riêng tư** — dữ liệu nhạy cảm nằm off-chain, chỉ hash là công khai. Hash không tiết lộ nội dung ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md), tính chất một chiều).

> 💡 **IPFS** dùng **định địa chỉ theo nội dung (content addressing)**: địa chỉ file *chính là* hash của nó. Nghĩa là bản thân địa chỉ đã tự chứng minh tính toàn vẹn — bạn tải về, hash lại, khớp thì đúng file. Cùng ý tưởng với việc địa chỉ ví = hash(public key) ở [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md).

---

## 3. Hồ sơ y tế

### Vấn đề

Hồ sơ bệnh án của bạn **nằm rải rác** ở từng bệnh viện, và **bệnh viện sở hữu nó, không phải bạn**. Đổi bệnh viện → phải xin sao lục, chờ, có khi làm lại toàn bộ xét nghiệm. Cấp cứu ở tỉnh khác → bác sĩ không biết bạn dị ứng thuốc gì.

### Blockchain giải thế nào

Đảo ngược quyền sở hữu: **bệnh nhân giữ chìa khoá**.

```
Hồ sơ (mã hoá)  →  lưu off-chain
Trên chuỗi      →  hash của hồ sơ + nhật ký cấp quyền

Bệnh nhân cấp quyền cho bác sĩ X trong 24h  → ghi lên chuỗi
Bác sĩ X đọc hồ sơ                          → ghi lên chuỗi
Bệnh nhân thu hồi quyền                     → ghi lên chuỗi
```

Được gì:

- **Bệnh nhân kiểm soát** ai xem được gì, trong bao lâu.
- **Nhật ký truy cập không thể sửa** — bệnh viện không thể xoá dấu vết đã xem trộm hồ sơ.
- **Liên thông** giữa các cơ sở mà không cần một cơ quan trung ương ôm hết dữ liệu.

### 📚 Lý thuyết bổ sung: cảnh báo GDPR

> ⚠️ **Tuyệt đối không ghi dữ liệu y tế lên blockchain**, kể cả đã mã hoá.

Ba lý do:

1. **Quyền được xoá (GDPR Điều 17)** xung đột trực tiếp với tính bất biến. Bạn **không xoá được**.
2. **"Mã hoá hôm nay" không phải "an toàn mãi mãi"** — mô hình *harvest now, decrypt later* ở [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md). Dữ liệu mã hoá ghi lên chuỗi năm 2026 vẫn nằm đó năm 2050, khi thuật toán có thể đã bị phá.
3. **Ngay cả hash cũng rủi ro** nếu không gian đầu vào nhỏ. Hash của "nhóm máu: O" chỉ có 4 khả năng — dò hết trong 1 mili giây. Phải thêm **salt** ngẫu nhiên.

**Kiến trúc đúng:** chuỗi chỉ giữ **con trỏ, hash và quyền truy cập**. Dữ liệu thật nằm off-chain, mã hoá, xoá được.

---

## 4. Danh tính số

### Vấn đề

Danh tính số của bạn hiện đang bị **thuê** từ các tập đoàn: đăng nhập bằng Google, xác minh bằng Facebook, điểm tín dụng do một công ty chấm. Họ có thể khoá tài khoản bạn bất cứ lúc nào, và họ bị hack thì bạn lãnh hậu quả.

Đồng thời, mỗi lần chứng minh **một** điều, bạn phải lộ **rất nhiều** điều: muốn chứng minh đủ 18 tuổi → đưa CCCD → lộ luôn tên, địa chỉ, số định danh, ngày sinh chính xác.

### Self-Sovereign Identity (SSI)

Mô hình "danh tính tự chủ": **bạn** giữ danh tính, không tổ chức nào giữ hộ.

```
   ┌─────────────┐   cấp bằng chứng   ┌───────────────┐
   │ Bên cấp     │──────────────────▶ │  BẠN          │
   │ (Bộ Công an,│   đã ký số         │  ví danh tính │
   │  trường ĐH) │                    └───────┬───────┘
   └─────────────┘                            │ xuất trình
          │ đăng public key lên chuỗi         ▼
          └──────────▶ ⛓️ ◀──────── ┌─────────────────────┐
                     kiểm chữ ký    │ Bên xác minh        │
                                    │ (quán bar, chủ nhà) │
                                    └─────────────────────┘
```

Ba vai: **bên cấp** (issuer) — **người giữ** (holder) — **bên xác minh** (verifier). Blockchain chỉ đóng vai **sổ đăng ký public key**, để bên xác minh kiểm được chữ ký mà không cần gọi điện hỏi bên cấp.

> 🔗 Nhìn kỹ: đây **chính là** chữ ký số ở [Bài 2](lesson_2_ma_hoa_bat_doi_xung.md), cộng với một sổ đăng ký khoá phi tập trung thay cho hệ thống CA.

### 📚 Lý thuyết bổ sung: tiết lộ chọn lọc bằng ZKP

Phần đẹp nhất của SSI là **zero-knowledge proof** (chứng minh không tiết lộ):

> Chứng minh *"tôi trên 18 tuổi"* mà **không** tiết lộ ngày sinh, tên, hay bất cứ thứ gì khác.

Bên xác minh nhận được **một** bit thông tin: đúng/sai. Không hơn.

Đối chiếu:

|                        | Đưa CCCD                            | ZKP                |
| ---------------------- | ----------------------------------- | ------------------ |
| Bên xác minh biết được | Tên, ngày sinh, địa chỉ, số ID, ảnh | Chỉ: "≥ 18 tuổi" ✓ |
| Rò rỉ nếu họ bị hack   | Toàn bộ                             | Không có gì        |

Chuẩn liên quan: **DID** (Decentralized Identifier — định danh phi tập trung) và **Verifiable Credentials** của W3C. EU đang triển khai **eIDAS 2.0 / EU Digital Identity Wallet** theo hướng này.

> 💡 ZKP là một trong số ít công nghệ blockchain có giá trị **độc lập** với blockchain — nó hữu ích cho bất kỳ hệ thống danh tính nào.

> 🔗 Cơ chế bên trong ZKP là [Bài 8 – Zero-Knowledge Proof](lesson_8_zero_knowledge_proof.md).

---

## 5. Công chứng & sở hữu trí tuệ

Đây là ứng dụng **gần với mục đích gốc năm 1991 nhất** ([Bài 1](lesson_1_blockchain_hoat_dong_ntn.md): Haber & Stornetta làm blockchain chính là để đóng dấu thời gian tài liệu).

### Proof of Existence

```
Bạn viết một bài hát / thiết kế / hợp đồng
        ↓
   SHA-256 → hash
        ↓
   ghi hash lên blockchain, kèm timestamp
        ↓
   ✓ Chứng minh được: "tài liệu này ĐÃ TỒN TẠI trước thời điểm T"
   ✓ Chứng minh được: "nó chưa bị sửa kể từ đó"
   ✗ KHÔNG chứng minh: "tôi là tác giả"
```

Chú ý kỹ dòng cuối. Blockchain chứng minh **thời điểm và tính toàn vẹn**, không chứng minh **quyền tác giả**. Ai cũng có thể hash một tài liệu của người khác rồi neo lên chuỗi. Nó chỉ hữu ích khi tranh chấp *ai làm ra trước*, không phải *ai làm ra*.

Ứng dụng: bản quyền, bằng sáng chế (mốc ưu tiên), chứng chỉ học vấn (chống bằng giả), hợp đồng, bằng chứng pháp lý, thời điểm chụp ảnh.

### 📚 Lý thuyết bổ sung: tại sao đây là use case *tốt*

Đối chiếu với [khung quyết định ở phần 8](#8--khung-quyết-định-có-thật-sự-cần-blockchain-không), công chứng đạt gần như **mọi tiêu chí**:

- ✅ Cần bất biến — đúng bản chất vấn đề.
- ✅ Nhiều bên không tin nhau (nguyên đơn, bị đơn, toà).
- ✅ Không muốn phụ thuộc một trung gian (mà trung gian truyền thống — công chứng viên — chính là thứ đang bị thay).
- ✅ Dữ liệu ghi lên chỉ là **hash** → rẻ, riêng tư, không dính GDPR.
- ✅ Tần suất ghi thấp → không cần thông lượng cao.

> 💡 Chú ý mẫu hình: **những use case blockchain hoạt động tốt nhất đều là những use case chỉ ghi HASH lên chuỗi.** Càng muốn đẩy nhiều dữ liệu thật lên, càng đuối.

---

## 6. Bầu cử — và vì sao giới chuyên môn phản đối

Video nêu bầu cử như một ứng dụng hứa hẹn. Ý tưởng nghe rất thuyết phục:

```
Mỗi phiếu = một giao dịch
   ✓ Không sửa được sau khi bỏ
   ✓ Ai cũng đếm lại được
   ✓ Kết quả tức thì
   ✓ Không cần tin ban kiểm phiếu
```

### 📚 Lý thuyết bổ sung: nhưng phần lớn chuyên gia an ninh bầu cử phản đối

Đây là chỗ bạn cần biết mặt sau, vì nó dạy một bài học tổng quát.

**1. Minh bạch và bỏ phiếu kín mâu thuẫn nhau.**

Bầu cử đòi hỏi hai thứ **đối nghịch**: ai cũng kiểm được kết quả, **nhưng** không ai biết được ai bầu cho ai. Blockchain giỏi cái đầu và **tệ** cái sau ([Bài 3](lesson_3_smart_contract.md), phần 9: mọi thứ đều công khai vĩnh viễn).

**2. Vấn đề cưỡng ép và mua phiếu (receipt-freeness).**

Bỏ phiếu tại phòng kín có một tính chất tinh tế: bạn **không thể chứng minh** mình đã bầu cho ai. Đó không phải khiếm khuyết — **đó là tính năng cốt lõi**. Nó khiến việc mua phiếu và ép buộc trở nên vô nghĩa, vì người mua không kiểm chứng được.

Bỏ phiếu online phá huỷ tính chất này: chồng đứng sau lưng vợ, ông chủ đứng sau lưng nhân viên, người mua phiếu xem màn hình.

**3. Blockchain không giải quyết khâu yếu nhất.**

```
Cử tri → 📱 THIẾT BỊ ĐẦU CUỐI → mạng → ⛓️ blockchain
              ↑
     Điện thoại/máy tính dính malware
     → sửa phiếu TRƯỚC khi ký
     → blockchain lưu lại phiếu đã bị sửa một cách HOÀN HẢO
```

Blockchain đảm bảo phiếu **không bị sửa sau khi ghi**. Nó **không** đảm bảo phiếu **đúng lúc ghi**. Đây chính xác là [vấn đề chặng cuối ở phần 10](#10--vấn-đề-chặng-cuối--giới-hạn-nền-tảng).

**4. Không kiểm phiếu lại được bằng vật lý.** Phiếu giấy có một ưu điểm mà không phần mềm nào có: **kiểm lại bằng tay được**. Một hệ thống điện tử bị nghi ngờ thì không có "bản gốc" nào để đối chiếu.

**5. Danh tính vẫn cần một cơ quan trung ương.** Ai xác định người này đủ điều kiện bầu cử? Nhà nước. Vậy bạn vẫn có một điểm tin cậy tập trung — chỉ là đã dịch chỗ.

> 💡 **Bài học tổng quát, quan trọng hơn cả chuyện bầu cử:** blockchain giải bài toán **toàn vẹn của bản ghi**. Nó không giải bài toán **danh tính**, **riêng tư**, hay **dữ liệu đầu vào có đúng không**. Khi một use case thất bại, gần như luôn là vì thất bại ở ba thứ sau — chứ không phải ở thứ đầu.

Tổ chức như MIT CSAIL, National Academies of Sciences (Mỹ) đã ra khuyến nghị chính thức **không dùng bỏ phiếu qua Internet** cho bầu cử công, kể cả có blockchain. Một số nước vẫn thử nghiệm quy mô nhỏ (Estonia — nhưng dùng hạ tầng eID quốc gia, không phải blockchain).

---

## 7. Các ứng dụng khác

| Lĩnh vực                | Vấn đề                                     | Blockchain giúp gì                                     | Đánh giá                                                                    |
| ----------------------- | ------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Đất đai**             | Sổ đỏ giả, tranh chấp, quan liêu           | Sổ đăng ký bất biến, chuyển nhượng bằng smart contract | ⚠️ Cần nhà nước công nhận thì mới có giá trị pháp lý                         |
| **Bảo hiểm**            | Bồi thường chậm, tranh cãi                 | Chuyến bay trễ → oracle xác nhận → tự chi trả          | ✅ Tốt nếu sự kiện **khách quan, đo được**                                   |
| **Từ thiện**            | Không biết tiền đi đâu                     | Theo dõi từng đồng đến tận nơi                         | ✅ Khai thác đúng tính minh bạch                                             |
| **Năng lượng**          | Bán điện mặt trời dư cho hàng xóm          | Giao dịch P2P vi mô, tự động                           | ⚠️ Vướng quy định ngành điện                                                 |
| **Âm nhạc / bản quyền** | Trung gian ăn phần lớn                     | Smart contract chia tiền tự động cho tác giả           | ⚠️ Khó ở khâu **phát hiện** sử dụng, không phải khâu chia tiền               |
| **Bằng cấp**            | Bằng giả                                   | Trường neo hash bằng lên chuỗi                         | ✅ Đơn giản, hiệu quả, rẻ                                                    |
| **Game**                | Vật phẩm thuộc về nhà phát hành            | Người chơi thật sự sở hữu, bán được                    | ⚠️ Chỉ có ý nghĩa nếu vật phẩm dùng được **liên game**                       |
| **RWA**                 | Bất động sản khó chia nhỏ, kém thanh khoản | Token hoá tài sản thật, chia nhỏ quyền sở hữu          | ⚠️ Token chỉ có giá trị nếu **luật công nhận**                               |
| **CBDC**                | Tiền số do ngân hàng trung ương phát hành  | Thanh toán nhanh, truy vết                             | ❗ Thường **không** thật sự dùng blockchain — vì đã có bên tin cậy trung tâm |

> 💡 Đọc cột "Đánh giá" theo một mẫu hình: use case **✅** đều là loại chỉ cần **ghi hash / theo dõi sự kiện khách quan**. Use case **⚠️** đều vướng ở **thế giới thật** — pháp lý, dữ liệu đầu vào, hoặc sự chấp nhận của con người. **Không cái nào vướng ở kỹ thuật blockchain.**

---

## 8. 📚 Khung quyết định: có thật sự cần blockchain không?

*Phần này hoàn toàn là bổ sung — và là phần giá trị nhất của bài.*

Phần lớn dự án "blockchain" thất bại vì bắt đầu sai câu hỏi: *"làm sao dùng blockchain?"* thay vì *"vấn đề của tôi là gì?"*.

### Cây quyết định

```
┌─ Bạn có cần lưu trữ state chung không?
│     KHÔNG → không cần database, càng không cần blockchain
│     CÓ ↓
├─ Có NHIỀU BÊN cùng ghi dữ liệu không?
│     KHÔNG (chỉ 1 bên ghi) → dùng DATABASE THƯỜNG
│     CÓ ↓
├─ Có một BÊN TRUNG GIAN được tất cả tin tưởng không?
│     CÓ, và họ luôn online → dùng DATABASE THƯỜNG (nhanh hơn 1000 lần, rẻ hơn)
│     KHÔNG ↓
├─ Các bên ghi dữ liệu có tin nhau không?
│     CÓ → dùng DATABASE PHÂN TÁN thường (Postgres nhân bản, Kafka)
│     KHÔNG ↓
├─ Bạn có cần KIỂM SOÁT ai được tham gia không?
│     CÓ  → BLOCKCHAIN LIÊN MINH (permissioned)
│     KHÔNG ↓
└─────▶ BLOCKCHAIN CÔNG KHAI (Bitcoin, Ethereum)
```

Khung này dựa trên bài báo học thuật **Wüst & Gervais, *"Do you need a blockchain?"* (2018)** và hướng dẫn **NISTIR 8202** của NIST.

### Bảng dấu hiệu nhận biết

| ✅ Blockchain **hợp lý** khi                   | ❌ Blockchain **thừa** khi             |
| --------------------------------------------- | ------------------------------------- |
| Nhiều bên không tin nhau cùng ghi             | Chỉ một tổ chức kiểm soát dữ liệu     |
| Không có trung gian được cả hai bên chấp nhận | Đã có trung gian và ai cũng ổn với họ |
| Cần chứng minh dữ liệu không bị sửa           | Không ai quan tâm chuyện sửa          |
| Cần chống kiểm duyệt                          | Cần xoá dữ liệu (GDPR!)               |
| Tần suất ghi thấp, giá trị mỗi bản ghi cao    | Cần hàng chục nghìn giao dịch/giây    |
| Ghi hash / sự kiện nhỏ                        | Cần lưu file lớn                      |
| Kiểm chứng công khai là yêu cầu bắt buộc      | Dữ liệu phải bí mật                   |

### Câu hỏi kiểm tra nhanh

Trước bất kỳ dự án blockchain nào, hỏi:

> **"Nếu tôi thay blockchain bằng một cái database Postgres do một bên tin cậy quản lý, hệ thống này có còn chạy được không?"**

- **Còn** → bạn không cần blockchain. Postgres nhanh hơn, rẻ hơn, dễ tuyển người hơn, và **xoá được dữ liệu**.
- **Không, vì không tìm được bên nào cả hai phía chấp nhận** → giờ mới đến lượt blockchain.

> ⚠️ **Blockchain đắt.** Bạn đánh đổi tốc độ, chi phí, và sự đơn giản **để mua lấy một thứ duy nhất: không cần tin ai.** Nếu bạn không thật sự cần thứ đó, bạn đang trả một cái giá rất cao cho hư không.

---

## 9. 📚 Công khai, riêng tư, hay liên minh?

Phần lớn dự án doanh nghiệp không dùng Bitcoin/Ethereum công khai.

|               | **Công khai**     | **Liên minh** (consortium) | **Riêng tư**                   |
| ------------- | ----------------- | -------------------------- | ------------------------------ |
| Ai đọc được   | Tất cả            | Thành viên                 | Trong tổ chức                  |
| Ai ghi được   | Tất cả            | Thành viên được duyệt      | Được cấp quyền                 |
| Đồng thuận    | PoW / PoS         | Raft, PBFT, IBFT           | Thường không cần               |
| Tốc độ        | 15–3.000 TPS      | Hàng nghìn TPS             | Rất nhanh                      |
| Phi tập trung | Cao               | Trung bình                 | ~Không                         |
| Ví dụ         | Bitcoin, Ethereum | Hyperledger Fabric, Corda  | Chuỗi nội bộ công ty           |
| Dùng cho      | Tiền, DeFi, NFT   | Chuỗi cung ứng, ngân hàng  | Hầu như: **nên dùng database** |

> ⚠️ **Blockchain riêng tư gần như luôn là câu trả lời sai.** Nếu một tổ chức kiểm soát mọi node, họ **viết lại lịch sử được** — chỉ cần bảo tất cả node của mình làm thế. Bạn mất hết tính bất biến, mà vẫn phải chịu toàn bộ chi phí và độ phức tạp. Thứ bạn thật sự muốn là một **database có nhật ký kiểm toán** (append-only audit log) — thứ đã có sẵn từ hàng chục năm nay.

**Blockchain liên minh thì có lý** trong một số trường hợp: vài chục công ty cạnh tranh nhau nhưng cần chung dữ liệu, không ai chịu để đối thủ giữ sổ, và tất cả đều đã được định danh pháp lý.

### 📚 Đồng thuận không cần PoW

Khi mọi người tham gia đã được định danh, bạn **không cần** Proof of Work. Không cần chống Sybil (kẻ tạo hàng nghìn danh tính giả) vì danh tính đã bị kiểm soát ở cửa vào.

| Thuật toán       | Chịu được                    | Đặc điểm                                          |
| ---------------- | ---------------------------- | ------------------------------------------------- |
| **Raft / Paxos** | Node chết (crash fault)      | Nhanh, nhưng **không** chịu được node nói dối     |
| **PBFT / IBFT**  | Node nói dối (Byzantine)     | Chịu được < 1/3 node phản bội, chung cuộc tức thì |
| **PoW / PoS**    | Node nói dối + môi trường mở | Chậm, tốn, nhưng **ai cũng tham gia được**        |

> 💡 Đây là chỗ thấy rõ **PoW đắt để mua cái gì**: nó cho phép **người lạ không cần xin phép** tham gia. Nếu bạn đã có danh sách thành viên, bạn đang trả tiền cho một tính năng bạn không dùng.

### 📚 Lý thuyết bổ sung: một chuỗi liên minh thật sự trông ra sao

Bảng trên xếp loại chuỗi liên minh về mặt khái niệm. Nhưng "chuỗi có phép" nghe rất trừu tượng cho tới khi nhìn một cái cụ thể. Hyperledger Fabric là nền tảng liên minh được dùng nhiều nhất, và nó **khác Ethereum gần như ở mọi điểm**:

| | **Ethereum (công khai)** | **Fabric (liên minh)** |
|---|---|---|
| Danh tính | một cặp khoá vô danh | **chứng chỉ số do một CA cấp** — bạn là "Công ty A, phòng B", có giấy tờ |
| Tham gia | ai cũng được | phải được kết nạp |
| Đồng thuận | PoW/PoS toàn mạng | **dịch vụ sắp thứ tự** (Raft) — chịu được node *chết*, **không** chịu được node *nói dối* |
| Ai phải đồng ý | đa số toàn mạng | **chính sách chứng thực**: "giao dịch này cần chữ ký của A **và** B" |
| Đồng tiền | có, bắt buộc | **không có** |
| Phí | gas | không |
| Hợp đồng | Solidity, chạy trong EVM | **chaincode** Go/Java/Node, chạy trong container |
| Ai thấy dữ liệu | tất cả | chỉ các bên trong **kênh** đó |

Hai thứ đáng dừng lại:

**Kênh (channel)** — mỗi kênh là một **sổ cái riêng biệt**. Hai đối thủ cạnh tranh có thể cùng nằm trên một mạng lưới mà không bên nào thấy giao dịch của bên kia. Đây là câu trả lời của Fabric cho vấn đề *"mọi thứ đều công khai"* ở [Bài 3](lesson_3_smart_contract.md), và cũng là thứ khiến nó hợp với dữ liệu doanh nghiệp hơn hẳn chuỗi công khai.

**Không có đồng tiền, không có đào.** Nghe như mất mát, nhưng nghĩ kỹ thì đồng tiền trên chuỗi công khai tồn tại để **trả công cho những người lạ giữ sổ**. Khi những người giữ sổ đã là các công ty ký hợp đồng với nhau, động cơ đó đến từ hợp đồng chứ không từ token. Bỏ đồng tiền đi là bỏ luôn phần lớn độ phức tạp.

#### Câu hỏi phải hỏi ngay sau đó

> Bạn vừa thay **"không cần tin ai"** bằng **"tin một liên minh đã biết mặt nhau"**.
> Nếu các bên đó đã tin nhau đủ để cùng vận hành một hạ tầng chung, thì **một cơ sở dữ liệu sao chép có nhật ký ký số** có làm được việc đó không?

Rất nhiều dự án chuỗi liên minh chết vì không ai hỏi câu này trước. Quay lại [khung quyết định ở phần 8](#8--khung-quyết-định-có-thật-sự-cần-blockchain-không) và chạy lại: chuỗi liên minh chỉ thắng khi **không bên nào chấp nhận để bên kia làm chủ cơ sở dữ liệu**, mà cả nhóm vẫn cần chung một trạng thái và một dấu vết kiểm toán.

> ⚠️ **Cảnh báo cho ai đọc tài liệu cũ:** rất nhiều sách và khoá học 2018–2019 dạy Fabric qua công cụ **Hyperledger Composer**. Composer bị **khai tử từ tháng 8/2019**. Nếu tài liệu bạn đang cầm dạy Composer, phần công cụ của nó đã chết hoàn toàn — chỉ giữ lại phần khái niệm ở bảng trên.

---

## 10. 📚 Vấn đề chặng cuối — giới hạn nền tảng

Đây là hạn chế **quan trọng nhất** của mọi use case đời thực, và là lý do phần lớn dự án chuỗi cung ứng thất bại.

> **Blockchain đảm bảo dữ liệu KHÔNG BỊ SỬA sau khi ghi.**
> **Blockchain KHÔNG đảm bảo dữ liệu ĐÚNG lúc ghi.**

```
🌍 Thế giới thực ──▶ 👤 người/cảm biến nhập ──▶ ⛓️ blockchain
                            ↑
                    ĐÂY là mắt xích yếu
                    Nhập sai/gian dối ở đây
                    → blockchain bảo vệ điều DỐI TRÁ đó vĩnh viễn,
                      hoàn hảo như bảo vệ sự thật
```

Ví dụ cụ thể: nông dân dán nhãn "hữu cơ" cho rau mua ngoài chợ, rồi ghi lên blockchain. Chuỗi ghi nhận hoàn hảo. Truy xuất ra "hữu cơ, Đà Lạt, chứng nhận đầy đủ". **Bất biến, minh bạch, và hoàn toàn sai sự thật.**

> 🧪 [Phần 13](#13-code-minh-hoạ) có code chứng minh chính xác điều này: một bản ghi gian dối vẫn cho `verify_chain() = True`.

Đây là biến thể của **bài toán oracle** ở [Bài 3](lesson_3_smart_contract.md) — nhưng cho **vật thể** thay vì dữ liệu, nên khó hơn nhiều.

### Cách giảm thiểu (không cái nào giải triệt để)

| Cách                        | Ý tưởng                                        | Hạn chế                             |
| --------------------------- | ---------------------------------------------- | ----------------------------------- |
| **Cảm biến IoT**            | Máy ghi thay người                             | Ai đảm bảo cảm biến gắn đúng chỗ?   |
| **Định danh vật lý**        | Chip NFC, mã QR chống giả, "vân tay" kim cương | Chip tháo ra gắn sang hàng giả được |
| **Nhiều bên xác nhận chéo** | Nhiều bên độc lập cùng ghi, đối chiếu          | Thông đồng vẫn được                 |
| **Kiểm toán ngẫu nhiên**    | Kiểm tra thực địa bất chợt                     | Vẫn cần con người và niềm tin       |
| **Đặt cọc + phạt**          | Ghi sai bị tịch thu tiền cọc                   | Chỉ hiệu quả nếu bị phát hiện       |

> 💡 **Kết luận trung thực:** blockchain **dịch chuyển** niềm tin chứ không **loại bỏ** niềm tin. Trong tài chính thuần số, nó dịch niềm tin đi hết sạch (vì mọi thứ đều là dữ liệu). Trong ứng dụng vật lý, nó chỉ dịch niềm tin từ *"tin bên giữ sổ"* sang *"tin bên nhập liệu"* — vẫn tốt hơn, nhưng **không phải phép màu**.

---

## 11. 📚 Chi phí & khả năng mở rộng

### Bộ ba bất khả thi (blockchain trilemma)

Vitalik Buterin: một blockchain khó đạt đồng thời cả ba:

```
              Phi tập trung
                   ▲
                  ╱ ╲
                 ╱   ╲     Chọn 2 trong 3
                ╱     ╲
         Bảo mật ───── Khả năng mở rộng
```

- **Bitcoin/Ethereum L1** — chọn phi tập trung + bảo mật, hy sinh tốc độ.
- **Blockchain liên minh** — chọn bảo mật + tốc độ, hy sinh phi tập trung.

### Đối chiếu thông lượng

| Hệ thống               | TPS (giao dịch/giây) |
| ---------------------- | -------------------- |
| Bitcoin                | ~7                   |
| Ethereum L1            | ~15–30               |
| Visa                   | ~1.700 (đỉnh 65.000) |
| Ethereum + rollup (L2) | ~2.000–10.000        |
| Postgres trên một máy  | ~50.000+             |

> Nhìn dòng cuối. Đó là lý do câu hỏi ở [phần 8](#8--khung-quyết-định-có-thật-sự-cần-blockchain-không) quan trọng đến thế: nếu bạn **có** một bên tin cậy, bạn đang bỏ đi hiệu năng gấp hàng nghìn lần để đổi lấy thứ bạn không cần.

### Layer 2 — cách mở rộng hiện tại

```
  L2 (Rollup)  →  gom hàng nghìn giao dịch, xử lý ngoài chuỗi
       ↓            rồi ghi 1 bằng chứng gọn xuống L1
  L1 (Ethereum) →  đảm bảo bảo mật cho toàn bộ lô đó
```

- **Optimistic rollup** (Arbitrum, Optimism) — mặc định tin là đúng, ai phát hiện sai thì gửi *fraud proof* trong 7 ngày.
- **ZK rollup** (zkSync, StarkNet) — kèm **bằng chứng toán học** rằng lô giao dịch hợp lệ. Chung cuộc nhanh hơn, toán nặng hơn.

> 💡 Ý tưởng cốt lõi giống hệt việc **neo hash** ở [phần 2](#2-chuỗi-cung-ứng--truy-xuất-nguồn-gốc): làm việc nặng ở ngoài, chỉ ghi thứ **nhỏ mà kiểm chứng được** lên chuỗi. Đây là mẫu hình lặp lại khắp mọi thiết kế blockchain tốt.

---

## 12. 📚 Thực tế phũ phàng: những dự án đã chết

Video ra đời trong giai đoạn lạc quan. Đã đủ thời gian để xem kết quả thật.

| Dự án                               | Tham vọng                                  | Kết cục                                                                                 |
| ----------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------- |
| **TradeLens** (Maersk + IBM)        | Blockchain cho vận tải biển toàn cầu       | **Đóng cửa 2022** — các hãng tàu đối thủ không chịu tham gia nền tảng do Maersk dẫn dắt |
| **IBM Food Trust**                  | Truy xuất thực phẩm                        | Thu hẹp mạnh, IBM giải tán phần lớn đội blockchain 2021                                 |
| **We.trade**                        | Tài chính thương mại cho ngân hàng châu Âu | **Phá sản 2022**                                                                        |
| **Nhiều thử nghiệm sổ đỏ quốc gia** | Đăng ký đất đai                            | Phần lớn dừng ở thí điểm                                                                |

### Vì sao thất bại — và bài học

| Nguyên nhân                                                                  | Bài học                                                                                                                                                                    |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vấn đề quản trị, không phải kỹ thuật**                                     | Đối thủ không chịu chung nền tảng do một bên dẫn dắt. Blockchain giải bài toán *"ai giữ sổ"* về mặt kỹ thuật, nhưng **ai vận hành mạng** lại quay về là câu hỏi chính trị. |
| **Vấn đề chặng cuối** ([phần 10](#10--vấn-đề-chặng-cuối--giới-hạn-nền-tảng)) | Dữ liệu vào vẫn do người nhập. Chuỗi bất biến không cứu được dữ liệu rác.                                                                                                  |
| **Hiệu ứng mạng**                                                            | Sổ chung chỉ có giá trị khi **mọi người** dùng. Có 3/20 bên tham gia thì gần như vô dụng.                                                                                  |
| **Database vốn đã đủ**                                                       | Nhiều bài toán không thật sự cần loại bỏ niềm tin.                                                                                                                         |
| **Chi phí tích hợp**                                                         | Nối blockchain vào hệ thống ERP có sẵn tốn hơn nhiều so với chạy chính blockchain.                                                                                         |

> 💡 **Đây không phải lý do để bỏ qua blockchain.** Đây là lý do để **áp dụng đúng chỗ**. Những chỗ blockchain đã chứng minh giá trị bền vững đều là nơi **niềm tin thật sự không tồn tại** và **tài sản là thuần số**: Bitcoin (14+ năm chưa từng bị hack ở tầng giao thức), stablecoin, DeFi, ổn định giá trị ở các nước siêu lạm phát, chuyển tiền xuyên biên giới.
>
> Mẫu hình: **blockchain thắng ở nơi tài sản vốn đã là bit; nó chật vật ở nơi tài sản là nguyên tử.**

---

## 13. Code minh hoạ

Hệ thống truy xuất nguồn gốc: **neo hash lên chuỗi, dữ liệu để off-chain**. Chỉ dùng thư viện chuẩn của Node.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

Code này chứng minh cả **sức mạnh** lẫn **giới hạn nền tảng** ở [phần 10](#10--vấn-đề-chặng-cuối--giới-hạn-nền-tảng).

```typescript
// provenance.ts — truy xuất nguồn gốc: neo dữ liệu off-chain bằng hash.
// Demo 3 điều: (1) neo rẻ, (2) phát hiện sửa dữ liệu, (3) GIỚI HẠN garbage-in.
// Chạy: node provenance.ts
import { createHash } from "node:crypto";
import { strict as assert } from "node:assert";

type Doc = Record<string, string | number>;

/** JSON tất định: JSON.stringify KHÔNG sắp khoá, nên phải tự sắp. */
function canonical(o: Record<string, unknown>): string {
  return JSON.stringify(Object.keys(o).sort().map((k) => [k, o[k]]));
}

const h = (x: string): string => createHash("sha256").update(x).digest("hex");

interface Record_ {
  seq: number; docHash: string; actor: string; prev: string; recordHash?: string;
}

/** Sổ chỉ-ghi-thêm, hash-chained. Mỗi bản ghi chỉ 32 byte hash + metadata. */
class Ledger {
  records: Record_[] = [];

  /** Ghi HASH của tài liệu lên chuỗi, KHÔNG ghi tài liệu. */
  anchor(doc: Doc, actor: string): string {
    const digest = h(canonical(doc));
    const prev = this.records.at(-1)?.recordHash ?? "0".repeat(64);
    const rec: Record_ = { seq: this.records.length, docHash: digest, actor, prev };
    rec.recordHash = h(canonical(rec as unknown as Record<string, unknown>));
    this.records.push(rec);
    return digest;
  }

  verifyChain(): boolean {
    for (let i = 0; i < this.records.length; i++) {
      const r = this.records[i];
      const body = { seq: r.seq, docHash: r.docHash, actor: r.actor, prev: r.prev };
      if (r.recordHash !== h(canonical(body))) return false;
      const expectedPrev = i ? this.records[i - 1].recordHash : "0".repeat(64);
      if (r.prev !== expectedPrev) return false;
    }
    return true;
  }

  /** Tài liệu này có khớp với thứ đã được neo không? */
  proves(doc: Doc): boolean {
    const d = h(canonical(doc));
    return this.records.some((r) => r.docHash === d);
  }
}

// ---------- demo ----------
const L = new Ledger();
const offchain = new Map<string, Doc & { _blob?: string }>();  // kho thật NGOÀI chuỗi

const steps: [string, Doc][] = [
  ["nong_dan", { buoc: "thu hoach", lo: "MG-2026-08", noi: "Tien Giang", ngay: "2026-08-01" }],
  ["nha_may", { buoc: "dong goi", lo: "MG-2026-08", noi: "Long An", ngay: "2026-08-03" }],
  ["van_tai", { buoc: "van chuyen", lo: "MG-2026-08", nhiet_do_max: 6, ngay: "2026-08-05" }],
  ["sieu_thi", { buoc: "len ke", lo: "MG-2026-08", noi: "Ha Noi", ngay: "2026-08-07" }],
];
for (const [actor, doc] of steps) offchain.set(L.anchor(doc, actor), { ...doc });

// Tài liệu thực tế có cả ảnh + PDF chứng nhận: mô phỏng 2 MB mỗi bước
for (const d of offchain.values()) d._blob = "x".repeat(2_000_000);
assert(L.verifyChain());
const onchain = 32 * L.records.length;                       // chỉ 32 byte hash / bước
let offchainBytes = 0;
for (const d of offchain.values()) offchainBytes += d._blob!.length;
console.log(
  `✓ neo ${L.records.length} buoc | on-chain ${onchain}B hash, ` +
  `off-chain ${(offchainBytes / 1e6).toFixed(0)}MB -> ti le 1:${Math.floor(offchainBytes / onchain).toLocaleString("en-US")}`,
);

// 1. Truy xuất: từ lô hàng ra toàn bộ hành trình, trong mili giây
console.log("✓ truy xuat:", L.records.map((r) => r.actor).join(" -> "));

// 2. Ai đó sửa dữ liệu off-chain -> hash lệch -> lộ ngay
const d3 = [...offchain.keys()][2];
const { _blob, ...orig } = offchain.get(d3)!;
const faked = { ...orig, nhiet_do_max: 4 };                  // giấu việc đứt lạnh
assert(L.proves(orig as Doc), "ban goc phai khop");
assert(!L.proves(faked as Doc), "ban sua phai bi phat hien");
console.log("✓ sua nhiet_do 6->4 sau khi neo: bi phat hien (hash lech)");

// 3. Sửa chính sổ cái -> đứt xích
L.records[1].actor = "nha_may_gia";
assert(!L.verifyChain(), "sua so cai phai lam dut xich");
console.log("✓ sua so cai: verifyChain() = false");
L.records[1].actor = "nha_may";                              // khôi phục

// 4. GIỚI HẠN: dữ liệu SAI ngay từ đầu vẫn được neo hoàn hảo
const L2 = new Ledger();
const doiTra: Doc = { buoc: "thu hoach", lo: "FAKE-01", noi: "Da Lat", chung_nhan: "huu co" };
L2.anchor(doiTra, "nong_dan_gian_doi");        // thực tế: rau chợ, dán nhãn hữu cơ
assert(L2.verifyChain() && L2.proves(doiTra));
console.log("✗ GIOI HAN: ban ghi GIAN DOI van verifyChain()=true, proves()=true");
console.log("           blockchain dam bao 'khong ai SUA', KHONG dam bao 'dung SU THAT'");

console.log("\nAll assertions passed.");
```

**Kết quả chạy:**

```
✓ neo 4 buoc | on-chain 128B hash, off-chain 8MB -> ti le 1:62,500
✓ truy xuat: nong_dan -> nha_may -> van_tai -> sieu_thi
✓ sua nhiet_do 6->4 sau khi neo: bi phat hien (hash lech)
✓ sua so cai: verifyChain() = false
✗ GIOI HAN: ban ghi GIAN DOI van verifyChain()=true, proves()=true
           blockchain dam bao 'khong ai SUA', KHONG dam bao 'dung SU THAT'

All assertions passed.
```

**Ba điều code này dạy:**

| Dòng                                       | Bài học                                                                                                    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `1:62,500`                                 | Neo hash rẻ hơn lưu dữ liệu **bốn bậc độ lớn**. Đây là lý do mọi thiết kế blockchain tốt đều chỉ ghi hash. |
| `sua nhiet_do 6->4 ... bi phat hien`       | Đây là **giá trị thật**: nhà vận tải không thể xoá dấu vết đứt lạnh sau khi đã ghi.                        |
| `ban ghi GIAN DOI van verify_chain()=True` | Đây là **giới hạn thật**. Cùng một cơ chế bảo vệ sự thật cũng bảo vệ điều dối trá — hoàn hảo như nhau.     |

**Tự thử nghiệm:**

- Thêm cảm biến IoT: cho mỗi bản ghi kèm chữ ký số của thiết bị ([Bài 2](lesson_2_ma_hoa_bat_doi_xung.md)). Bạn nâng được từ *"ai đó đã ghi"* lên *"thiết bị X đã ghi"* — nhưng **vẫn không** lên được *"và đó là sự thật"*.
- Thêm `salt` ngẫu nhiên vào mỗi doc trước khi hash, xem vì sao nó cần thiết khi không gian đầu vào nhỏ ([phần 3](#3-hồ-sơ-y-tế)).
- Bỏ trường `prev` đi — thấy ngay sổ mất khả năng phát hiện chèn/xoá bản ghi ở giữa.

---

## 14. Từ điển thuật ngữ

| Thuật ngữ                   | Giải thích                                                     |
| --------------------------- | -------------------------------------------------------------- |
| **Use case**                | Trường hợp ứng dụng cụ thể của công nghệ                       |
| **Anchoring**               | Neo hash của dữ liệu off-chain lên blockchain                  |
| **On-chain / off-chain**    | Nằm trên chuỗi / nằm ngoài chuỗi                               |
| **IPFS**                    | Lưu trữ phân tán, địa chỉ file = hash của nội dung             |
| **Content addressing**      | Định địa chỉ theo nội dung — địa chỉ tự chứng minh toàn vẹn    |
| **Proof of Existence**      | Chứng minh tài liệu tồn tại trước thời điểm T                  |
| **SSI**                     | Self-Sovereign Identity — danh tính tự chủ                     |
| **DID**                     | Decentralized Identifier — định danh phi tập trung (chuẩn W3C) |
| **Verifiable Credential**   | Bằng chứng số đã được bên cấp ký                               |
| **ZKP**                     | Zero-Knowledge Proof — chứng minh mà không tiết lộ             |
| **Selective disclosure**    | Tiết lộ chọn lọc, chỉ lộ đúng thứ cần                          |
| **Receipt-freeness**        | Không thể chứng minh mình bầu cho ai — chống mua phiếu         |
| **Last-mile problem**       | Vấn đề chặng cuối — dữ liệu vào chuỗi có đúng không            |
| **Garbage in, garbage out** | Đầu vào rác thì đầu ra rác, dù xử lý hoàn hảo                  |
| **Permissioned blockchain** | Chuỗi cần được cấp quyền mới tham gia                          |
| **Consortium blockchain**   | Chuỗi liên minh — nhiều tổ chức cùng vận hành                  |
| **Hyperledger Fabric**      | Nền tảng blockchain liên minh phổ biến nhất                    |
| **Sybil attack**            | Tạo hàng loạt danh tính giả để chiếm đa số                     |
| **Raft / PBFT**             | Thuật toán đồng thuận cho mạng đã định danh                    |
| **Blockchain trilemma**     | Phi tập trung – bảo mật – mở rộng: chọn 2                      |
| **TPS**                     | Transactions Per Second — giao dịch mỗi giây                   |
| **Layer 2 / Rollup**        | Xử lý ngoài chuỗi, neo bằng chứng xuống L1                     |
| **Optimistic / ZK rollup**  | Hai kiểu rollup: mặc định tin / kèm bằng chứng toán            |
| **RWA**                     | Real World Asset — token hoá tài sản thật                      |
| **CBDC**                    | Tiền số do ngân hàng trung ương phát hành                      |
| **Network effect**          | Hiệu ứng mạng — càng đông người dùng càng có giá trị           |
| **Audit log**               | Nhật ký chỉ-ghi-thêm — giải pháp thay thế blockchain riêng tư  |

---

## 15. Câu hỏi tự kiểm tra

1. Kể 4 tính chất của blockchain và mỗi tính chất mở ra nhóm ứng dụng nào.
2. Phát biểu "bài toán chung" mà mọi use case blockchain đều thuộc về.
3. Vì sao chuỗi cung ứng dùng blockchain thay vì một database chung? Câu trả lời là kỹ thuật hay chính trị?
4. Vì sao **không** nên lưu dữ liệu thật lên chuỗi? Kiến trúc đúng là gì?
5. Vì sao ghi hồ sơ y tế lên blockchain là ý tưởng tồi? Nêu 3 lý do.
6. Vì sao hash của "nhóm máu: O" là không an toàn? Sửa thế nào?
7. SSI có 3 vai nào? Blockchain đóng vai gì trong đó?
8. ZKP cho phép làm gì mà đưa CCCD không làm được?
9. Proof of Existence chứng minh được gì và **không** chứng minh được gì?
10. Nêu 3 lý do giới chuyên môn phản đối bỏ phiếu qua blockchain.
11. Vì sao "receipt-freeness" là **tính năng** chứ không phải khiếm khuyết của phòng bỏ phiếu kín?
12. Đọc thuộc câu hỏi kiểm tra nhanh ở [phần 8](#8--khung-quyết-định-có-thật-sự-cần-blockchain-không). Áp dụng nó cho một dự án blockchain bạn từng nghe.
13. Vì sao blockchain riêng tư gần như luôn là câu trả lời sai?
14. Nếu mọi thành viên đã được định danh, vì sao không cần PoW nữa?
15. Phát biểu vấn đề chặng cuối trong đúng hai câu.
16. Blockchain **dịch chuyển** niềm tin hay **loại bỏ** niềm tin? Trả lời riêng cho tài sản số và tài sản vật lý.
17. Vì sao TradeLens thất bại? Nguyên nhân là kỹ thuật hay quản trị?
18. Nêu mẫu hình chung giữa "neo hash" và "Layer 2 rollup".

---

## Tóm tắt một trang

```
BLOCKCHAIN ≠ CHỈ TIỀN MÃ HOÁ
   4 tính chất → 4 nhóm ứng dụng
   bất biến | minh bạch | phi tập trung | không trung gian
   Bài toán chung: NHIỀU BÊN KHÔNG TIN NHAU cần CHUNG DỮ LIỆU
                   và không ai chịu để bên kia làm chủ

USE CASE
   ✅ Công chứng / bằng cấp / IP  — chỉ ghi HASH, rẻ, riêng tư, đúng bản chất
   ✅ Chuỗi cung ứng             — nhưng vướng CHẶNG CUỐI
   ✅ Từ thiện, bảo hiểm tham số — sự kiện khách quan, đo được
   ⚠️ Y tế                       — GDPR! chỉ ghi con trỏ + quyền truy cập
   ⚠️ Danh tính (SSI + ZKP)      — hay, nhưng ZKP mới là phần giá trị
   ❌ Bầu cử                     — minh bạch >< bỏ phiếu kín; thiết bị đầu cuối là mắt xích yếu

KIẾN TRÚC ĐÚNG: dữ liệu OFF-CHAIN, chỉ neo HASH lên chuỗi
   → rẻ hơn ~62.500 lần, vẫn chống sửa, không dính GDPR
   → cùng mẫu hình với LAYER 2 ROLLUP

CÂU HỎI KIỂM TRA NHANH
   "Thay bằng Postgres do một bên tin cậy quản lý, còn chạy được không?"
      CÒN     → không cần blockchain (nhanh hơn 1000x, xoá được dữ liệu)
      KHÔNG   → giờ mới đến lượt blockchain
   Blockchain riêng tư ~ luôn sai → thứ bạn cần là AUDIT LOG

GIỚI HẠN NỀN TẢNG — VẤN ĐỀ CHẶNG CUỐI
   Đảm bảo: KHÔNG AI SỬA sau khi ghi
   KHÔNG đảm bảo: ĐÚNG SỰ THẬT lúc ghi
   → blockchain DỊCH CHUYỂN niềm tin, không LOẠI BỎ niềm tin

THỰC TẾ: TradeLens, We.trade, IBM Food Trust đều chết
   Nguyên nhân: QUẢN TRỊ + hiệu ứng mạng, không phải kỹ thuật
   Mẫu hình: thắng ở nơi tài sản là BIT, chật vật ở nơi tài sản là NGUYÊN TỬ
```

---

**Nguồn:**
- Video gốc: [Blockchains: how can they be used?](https://www.youtube.com/watch?v=aQWflNQuP_o) (Simply Explained – Savjee)
- Wüst & Gervais, *Do you need a blockchain?* (2018)
- NIST, *NISTIR 8202 — Blockchain Technology Overview* (2018)
- National Academies of Sciences, *Securing the Vote* (2018)
- W3C, *Decentralized Identifiers (DIDs)* & *Verifiable Credentials* — chuẩn chính thức

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. **Bài 4 – Ứng dụng blockchain** ← *bạn đang ở đây* — use case + khung quyết định *có cần blockchain không*
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
