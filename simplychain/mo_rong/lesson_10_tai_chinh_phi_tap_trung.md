# DeFi — tài chính phi tập trung

> Bài học dựa trên video **"Introduction to DeFi (Decentralized Finance)"** (kênh *Simply Explained – Savjee*, YouTube `vocM1bRVZmg`) — bài nói tại **CatholicCryptoConference 2022**, dài **31:38**.
> Đây là **bài thứ hai của phần mở rộng**, nối thẳng từ [Bài 9](lesson_9_tien_ma_hoa_toan_canh.md). Bài 9 hỏi *"tiền mã hoá là gì và nó hỏng ở đâu"*. Bài này hỏi tiếp: *"nếu đã có tiền phi tập trung rồi, thì cho vay, sàn, quỹ đầu tư — phi tập trung hoá được nốt không?"*
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua hoặc nói không chính xác. Đọc để hiểu *tại sao*, không chỉ *cái gì*.
>
> ⚠️ **Bài nói ghi tháng 11/2022, ngay sau khi FTX sụp** — diễn giả nhắc thẳng tên FTX ở phút `11:12`. Mọi con số trong video là con số của thời điểm đó. Phần bổ sung cập nhật tới **2026**, và [§20](#20--kiểm-lại-bốn-con-số-của-video) kiểm lại từng con số một.
>
> 📌 **Cần đọc trước:** [Bài 3 – Smart contract](../ly_thuyet/lesson_3_smart_contract.md) là nền bắt buộc. [Bài 9](lesson_9_tien_ma_hoa_toan_canh.md) nên đọc trước để có bối cảnh sàn tập trung.

---

## Mục lục

1. [DeFi là gì — và nó muốn thay thế cái gì](#1-defi-là-gì--và-nó-muốn-thay-thế-cái-gì)
2. [📚 Ngân hàng thật ra làm bốn việc — DeFi tách rời từng việc](#2--ngân-hàng-thật-ra-làm-bốn-việc--defi-tách-rời-từng-việc)
3. [Vì sao blockchain một mình là không đủ](#3-vì-sao-blockchain-một-mình-là-không-đủ)
4. [Smart contract — mảnh ghép làm chuỗi động đậy được](#4-smart-contract--mảnh-ghép-làm-chuỗi-động-đậy-được)
5. [📚 Bốn tính chất smart contract thừa hưởng — và mặt trái của từng cái](#5--bốn-tính-chất-smart-contract-thừa-hưởng--và-mặt-trái-của-từng-cái)
6. [Ví dụ 1 — Gọi vốn cộng đồng](#6-ví-dụ-1--gọi-vốn-cộng-đồng)
7. [Ví dụ 2 — Sàn phi tập trung](#7-ví-dụ-2--sàn-phi-tập-trung)
8. [📚 AMM — sàn phi tập trung thật sự khớp lệnh thế nào](#8--amm--sàn-phi-tập-trung-thật-sự-khớp-lệnh-thế-nào)
9. [Ví dụ 3 — Cho vay phi tập trung](#9-ví-dụ-3--cho-vay-phi-tập-trung)
10. [📚 Thế chấp vượt mức, thanh lý, và lãi suất tự nổi](#10--thế-chấp-vượt-mức-thanh-lý-và-lãi-suất-tự-nổi)
11. [📚 Vay chớp nhoáng — thứ chỉ tồn tại được nhờ tính nguyên tử](#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử)
12. [Ví dụ 4 — Tài chính thời gian thực](#12-ví-dụ-4--tài-chính-thời-gian-thực)
13. [Ví dụ 5 — NFT](#13-ví-dụ-5--nft)
14. [📚 NFT sở hữu cái gì, và không sở hữu cái gì](#14--nft-sở-hữu-cái-gì-và-không-sở-hữu-cái-gì)
15. [Ví dụ 6 — DAO](#15-ví-dụ-6--dao)
16. [📚 DAO trong thực tế — The DAO, ConstitutionDAO, và bài toán bỏ phiếu](#16--dao-trong-thực-tế--the-dao-constitutiondao-và-bài-toán-bỏ-phiếu)
17. [Ưu điểm — theo video](#17-ưu-điểm--theo-video)
18. [Nhược điểm — theo video](#18-nhược-điểm--theo-video)
19. [📚 Bảo mật smart contract — phân loại lỗi và bảng các vụ lớn](#19--bảo-mật-smart-contract--phân-loại-lỗi-và-bảng-các-vụ-lớn)
20. [📚 Kiểm lại bốn con số của video](#20--kiểm-lại-bốn-con-số-của-video)
21. [DeFi chạy trên chain nào, và to cỡ nào](#21-defi-chạy-trên-chain-nào-và-to-cỡ-nào)
22. [📚 Xếp rủi ro DeFi theo tầng](#22--xếp-rủi-ro-defi-theo-tầng)
23. [Code minh hoạ](#23-code-minh-hoạ)
24. [Từ điển thuật ngữ](#24-từ-điển-thuật-ngữ)
25. [Câu hỏi tự kiểm tra](#25-câu-hỏi-tự-kiểm-tra)

---

## 1. DeFi là gì — và nó muốn thay thế cái gì

Chương `01:47`. Diễn giả đưa hai định nghĩa, và cái thứ hai mới là cái đáng nhớ.

> **Định nghĩa khô:** DeFi = *decentralized finance*, thuật ngữ ô dù cho **mọi ứng dụng tài chính dựng trên blockchain**.
>
> **Định nghĩa video thích hơn:** *"một hệ thống tài chính toàn cầu được xây cho thời đại internet"* — mục tiêu là **đưa quyền kiểm soát tài chính về lại tay người dùng**.

Câu hỏi phản xạ của người nghe: *chẳng phải tôi đang kiểm soát tiền của tôi rồi sao?* Video trả lời: **đại khái thôi** — và liệt kê những gì ngân hàng làm được với tiền của bạn mà bạn không cản được:

```
   NGÂN HÀNG CÓ THỂ, BẤT KỲ LÚC NÀO:
   ────────────────────────────────────────────────────────
   ▸ Khoá tài khoản          "tạm thời chưa rút được"
   ▸ Chặn rút tiền           "rút nhiều thế phải báo trước"
   ▸ Thu phí cao             đổi ngoại tệ, chuyển quốc tế
   ▸ Từ chối giao dịch       "chúng tôi không chuyển tiền sang sàn crypto"
```

Cái cuối cùng không phải giả định. Đó là chuyện có thật ở rất nhiều nước, và chính nó là động cơ cảm xúc của cả phong trào DeFi.

Nhưng lưu ý cách video đóng khung vấn đề: nó **không** nói ngân hàng vô dụng. Nó nói bạn **phải tin** ngân hàng, và niềm tin đó thỉnh thoảng bị phản bội. Đây đúng là luận điểm của [Bài 9 §7](lesson_9_tien_ma_hoa_toan_canh.md#7-mua-ở-đâu-và-nó-nằm-ở-đâu) — chỉ là dời từ *giữ tiền* sang *dịch vụ tài chính*.

---

## 2. 📚 Ngân hàng thật ra làm bốn việc — DeFi tách rời từng việc

Video gộp "ngân hàng" thành một khối. Muốn hiểu DeFi thay được gì và không thay được gì thì phải tách ra. Một ngân hàng thương mại làm **bốn việc khác hẳn nhau**, và DeFi tấn công chúng ở bốn mức độ thành công rất khác nhau:

| Việc ngân hàng làm     | Bản chất                               | DeFi thay bằng              | Thay được chưa?                                                         |
| ---------------------- | -------------------------------------- | --------------------------- | ----------------------------------------------------------------------- |
| **Giữ hộ tài sản**     | lưu ký                                 | ví tự quản + smart contract | ✅ Thay hẳn — [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md)               |
| **Chuyển tiền**        | thanh toán                             | giao dịch trên chuỗi        | ✅ Thay hẳn — [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) |
| **Chuyển đổi kỳ hạn**  | nhận gửi ngắn hạn, cho vay dài hạn     | ❌ chưa có tương đương       | ⛔ **Không**                                                             |
| **Thẩm định tín dụng** | đánh giá khả năng trả nợ của người vay | thế chấp vượt mức           | ⚠️ **Né, chứ không giải**                                                |

Hai hàng cuối là chỗ đáng dừng lại.

**Chuyển đổi kỳ hạn** là phép màu trung tâm của ngân hàng: bạn gửi tiền rút bất cứ lúc nào, ngân hàng đem cho vay mua nhà 20 năm. Nó chạy được vì không phải ai cũng rút cùng lúc — và khi điều đó xảy ra thì gọi là *tháo chạy ngân hàng*, phải có ngân hàng trung ương đứng ra cứu. DeFi **không làm việc này**. Mọi khoản vay DeFi đều có thể bị đóng ngay lập tức.

**Thẩm định tín dụng** thì DeFi né sạch. Ngân hàng cho bạn vay vì họ tin bạn trả được. Giao thức DeFi không biết bạn là ai, nên nó bắt bạn **thế chấp nhiều hơn số vay**. Hệ quả nghe rất phản trực giác:

> **DeFi không thể cho vay tiêu dùng.**
> Ai cần vay 200 triệu để mua xe thì đúng là người **không có** 300 triệu để đặt cọc. Toàn bộ mảng cho vay DeFi vì thế không phục vụ nhu cầu vay của người thường — nó phục vụ **đòn bẩy đầu cơ**.

Ghi nhớ điều này khi đọc [§9](#9-ví-dụ-3--cho-vay-phi-tập-trung). Video mô tả cơ chế rất chuẩn nhưng không nói ra hệ quả này.

---

## 3. Vì sao blockchain một mình là không đủ

Chương `04:41`. Đây là bản lề của cả bài nói, và diễn giả diễn đạt nó rất gọn:

> **"Blockchains are static."**
> Blockchain ghi giao dịch rất giỏi. Nhưng nó **không tự hành động được**. Nó hoàn toàn phụ thuộc vào việc người dùng gửi lệnh vào.

Ví dụ video dùng: hai vợ chồng, hoặc hai đối tác làm ăn, muốn mở một **tài khoản chung** với quy tắc *chỉ chi tiền khi cả hai đồng ý*.

```
   TRÊN BLOCKCHAIN TRẦN                    CÁI TA CẦN
   ────────────────────                    ──────────
   ✅ An gửi 10 ETH cho địa chỉ X          ✅ như bên
   ✅ Ai cũng thấy 10 ETH nằm ở X          ✅ như bên
   ❌ "chỉ chi khi CẢ HAI ký"              ← chuỗi không biểu diễn nổi
   ❌ "sau 90 ngày tự hoàn tiền"           ← không có ai bấm nút
```

Blockchain trần chỉ có một luật chi tiêu: *ai cầm khoá riêng thì được chi*. Không có chỗ nào để cài thêm điều kiện. Muốn có điều kiện thì phải có **một chương trình sống trong chuỗi**.

> 🔍 **Nói cho chính xác hơn video một chút.** Bitcoin *có* ngôn ngữ điều kiện chi tiêu — Bitcoin Script — và làm được đa chữ ký lẫn khoá thời gian. Cái nó cố tình không có là **vòng lặp và trạng thái tuỳ ý**, tức là không Turing-đầy-đủ. Nên câu "blockchain tĩnh" đúng với tinh thần nhưng không đúng tuyệt đối; chính xác hơn là *hạn chế những gì lập trình được, để đổi lấy tính dự đoán được*. Chi tiết ở [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) phần Bitcoin Script.

---

## 4. Smart contract — mảnh ghép làm chuỗi động đậy được

Chương `05:28`. Định nghĩa của video:

> **Smart contract là một đoạn mã máy tính sống bên trong blockchain.**

Và vì sống trong chuỗi, nó **thừa hưởng mọi tính chất của chuỗi**: ai cũng gọi được, không có trung gian, bất biến sau khi triển khai, và chạy y hệt nhau với mọi người.

Video liệt kê nó làm được gì:

```
   ▸ Nhận và gửi coin        contract có ĐỊA CHỈ RIÊNG, giữ tiền được
   ▸ Lưu dữ liệu             vd: ai đã góp bao nhiêu vào tài khoản chung
   ▸ Gọi contract khác       ghép nhiều contract đơn thành ứng dụng phức tạp
   ▸ Tự động thi hành        không cần ai bấm nút để nó làm đúng luật đã viết
```

Câu tổng kết của diễn giả: *smart contract làm được gần như mọi thứ một người dùng làm được với blockchain, chỉ khác là hoàn toàn tự động.*

Điểm thứ ba — **contract gọi được contract khác** — nghe nhàm nhưng là thứ sinh ra toàn bộ DeFi. Nó cho phép **ghép nối như đồ Lego**: một sàn phi tập trung có thể gọi một giao thức cho vay, giao thức đó gọi một oracle giá, tất cả trong **một** giao dịch. Cái tên trong ngành là *money legos*. Nó cũng chính là thứ làm [vay chớp nhoáng](#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử) khả thi — và làm các vụ hack lan truyền qua nhiều giao thức cùng lúc.

---

## 5. 📚 Bốn tính chất smart contract thừa hưởng — và mặt trái của từng cái

Video liệt kê các tính chất ở dạng ưu điểm. Mỗi cái đều có mặt sau, và mặt sau mới là thứ giải thích các vụ mất tiền ở [§19](#19--bảo-mật-smart-contract--phân-loại-lỗi-và-bảng-các-vụ-lớn).

| Tính chất            | Mặt sáng                                          | Mặt tối                                                                                                                        |
| -------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Ai cũng gọi được** | không cần xin phép, không phân biệt đối xử        | **kẻ tấn công cũng không cần xin phép**; mọi hàm là bề mặt tấn công công khai                                                  |
| **Bất biến**         | không ai đổi luật giữa chừng                      | **phát hiện lỗi cũng không vá được**; video có nói ý này ở `27:00`                                                             |
| **Tất định**         | cùng đầu vào → cùng đầu ra, "code luôn công bằng" | công bằng **theo đúng những gì đã viết**, kể cả khi cái đã viết là sai                                                         |
| **Minh bạch**        | ai cũng kiểm toán được                            | **kẻ tấn công đọc mã trước bạn**; và giao dịch chờ trong mempool bị nhìn thấy → [MEV](../ly_thuyet/lesson_3_smart_contract.md) |

> ⚠️ **"Computer code is always fair"** — câu này của video ở `06:02` đúng về mặt kỹ thuật và gây hiểu nhầm về mặt thực tế. Mã nguồn không thiên vị **so với những gì nó được viết ra để làm**. Nhưng ai viết nó, viết cho ai có lợi, và ai giữ khoá nâng cấp — thì hoàn toàn là chuyện con người. Rất nhiều "giao thức phi tập trung" có một ví quản trị đơn lẻ đủ quyền rút sạch tiền. Xem [§22](#22--xếp-rủi-ro-defi-theo-tầng).

**Về tính bất biến,** thực tế 2026 đã lệch khá xa so với mô tả trong video. Hầu hết giao thức DeFi lớn triển khai theo **mẫu proxy**: một contract vỏ giữ tiền và chuyển lệnh sang một contract lõi thay được. Nghĩa là:

```
   Người dùng ──▶ [PROXY]  ──delegatecall──▶ [LÕI v1]
                     │                          ↓ nâng cấp
                     └──────────────────────▶ [LÕI v2]
   Địa chỉ không đổi. Tiền không đổi chỗ. LUẬT CHƠI thì đổi.
```

Sửa được lỗi — nhưng **ai bấm nút nâng cấp thì người đó có toàn quyền viết lại luật**, kể cả luật "chuyển hết tiền cho tôi". Bất biến đã bị đánh đổi lấy khả năng vá lỗi, và đánh đổi đó ít khi được nói rõ với người dùng. [Bài 3](../ly_thuyet/lesson_3_smart_contract.md) mô tả kỹ mẫu proxy và `delegatecall`.

---

## 6. Ví dụ 1 — Gọi vốn cộng đồng

Chương `07:17`. Ví dụ đầu tiên, và là ví dụ dễ hiểu nhất trong cả bài nói.

Kickstarter có **ba bên**, và hai bên đầu đều phải tin bên thứ ba:

```
   NGƯỜI ỦNG HỘ ──tiền──▶ [ KICKSTARTER ] ──tiền──▶ ĐỘI LÀM SẢN PHẨM
                            ▲
                            │ cả hai phía phải TIN chỗ này:
                            │  · gọi vốn đủ  -> sẽ giao tiền cho đội
                            │  · dự án hỏng  -> sẽ hoàn tiền người ủng hộ
```

Thay Kickstarter bằng một smart contract. Tiền nằm khoá trong contract, và luật giải ngân được viết sẵn:

```
   khi NHẬN ĐƯỢC TIỀN:
       nếu đã đạt mục tiêu     -> chuyển toàn bộ cho đội làm sản phẩm
       nếu chưa                -> giữ tiếp
   khi HẾT 90 NGÀY mà chưa đạt -> hoàn tiền từng người ủng hộ
```

Video nói thẳng đây là bản giản lược, và bản thật cần **yếu tố thời gian** — chính là dòng cuối. Đúng: thiếu nó thì tiền kẹt vĩnh viễn trong contract, vì [không ai bấm nút được](#3-vì-sao-blockchain-một-mình-là-không-đủ).

> 📌 **Cái ví dụ này giải, và cái nó không giải.** Nó giải **rủi ro người giữ tiền**: Kickstarter không thể ôm tiền bỏ chạy nữa. Nó **không** giải **rủi ro thực thi**: đội làm sản phẩm nhận tiền xong vẫn có thể không giao hàng. Không có smart contract nào ép được người ta hàn xong cái xe đạp. Đây là mặt khác của **bài toán oracle** ở [Bài 3](../ly_thuyet/lesson_3_smart_contract.md) — chuỗi không biết gì về thế giới thật.

---

## 7. Ví dụ 2 — Sàn phi tập trung

Chương `09:42`. Video mô tả cơ chế như sau:

> Bạn gửi coin kèm lệnh vào smart contract. Contract nhìn tất cả lệnh nó nhận được và **ghép những người muốn làm điều ngược nhau lại với nhau**. Ví dụ: tôi muốn đổi 100 Litecoin lấy 1 Bitcoin; ai đó muốn làm điều ngược lại; contract khớp hai bên.

Ưu điểm video nêu:

| Ưu điểm                       | Lý do                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Phí thấp hơn**              | không văn phòng, không nhân viên, không chi phí vận hành                                                                       |
| **Hỗ trợ nhiều token hơn**    | không cần ai duyệt niêm yết                                                                                                    |
| **Không thể ôm tiền bỏ chạy** | *"Just last week we saw a major cryptocurrency exchange go bankrupt — FTX... A decentralized exchange cannot do that"* `11:09` |

Câu cuối là luận điểm mạnh nhất, và bối cảnh thời điểm làm nó rất sắc: bài nói diễn ra **tám ngày sau khi FTX nộp đơn phá sản**.

> ⚠️ **Nhưng mô tả cơ chế thì đã lỗi thời ngay lúc video ghi hình.** Sàn phi tập trung theo kiểu **sổ lệnh khớp đôi** như video mô tả là mô hình 2017 (EtherDelta, 0x). Nó thất bại vì trên chuỗi thì đặt lệnh và huỷ lệnh đều tốn phí, và sổ lệnh mỏng thì gần như không bao giờ có ai muốn làm đúng điều ngược lại với bạn.
>
> Từ 2018 tới nay, **gần như toàn bộ khối lượng DEX chạy trên một cơ chế khác hẳn: AMM.** Không có sổ lệnh, không có bên đối ứng. Bạn giao dịch với **một cái hồ**. Xem mục tiếp theo.

---

## 8. 📚 AMM — sàn phi tập trung thật sự khớp lệnh thế nào

Đây là mục bổ sung quan trọng nhất của bài. Hiểu **một công thức** này là hiểu được phần lớn DeFi.

### Ý tưởng: bỏ luôn bên đối ứng

Thay vì tìm người muốn bán, bạn giao dịch với một **hồ thanh khoản** — một contract giữ sẵn hai loại token. Nó định giá bằng đúng một ràng buộc:

```
                        x · y = k

   x = lượng token A trong hồ        k = hằng số (không đổi khi swap)
   y = lượng token B trong hồ        giá A = y / x

   Bạn bỏ token A vào  -> x tăng -> để giữ k, y phải giảm -> bạn nhận token B
   Và giá A = y/x LẬP TỨC RẺ ĐI, vì chính bạn vừa làm hồ nhiều A hơn.
```

Không có ai "đồng ý bán cho bạn". Chỉ có một đường cong. Đây là phát minh làm nên Uniswap (2018) và là lý do DEX sống được.

### Hệ quả 1: trượt giá, và nó không tuyến tính

Chạy [code §23](#23-code-minh-hoạ) demo 1, hồ 100 ETH / 200.000 USDC (giá niêm yết 2.000):

```
   bán       nhận được     giá thực tế   trượt giá
   0,1 ETH        199,2      1.992,01       0,40%
     1 ETH     1.974,32      1.974,32       1,28%
     5 ETH     9.496,59      1.899,32       5,03%
    10 ETH    18.132,22      1.813,22       9,34%
    25 ETH    39.903,94      1.596,16      20,19%
```

Bán 25% kích thước hồ thì mất **một phần năm giá trị**. Đây không phải phí — phí chỉ 0,3%. Đây là hình dạng của đường cong.

> 💡 **Nhớ con số này.** Nó vừa là giới hạn của DEX với lệnh lớn, vừa là **vũ khí** ở [§11](#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử): nếu tiền của bạn đủ lớn, bạn *tự quyết định* giá trong hồ.

### Hệ quả 2: tổn thất tạm thời

Video gọi người gửi tiền vào giao thức là *"liquidity provider"* và coi đó đơn giản là kiếm lãi. Nó bỏ qua rủi ro đặc trưng nhất của vai trò này.

Gửi 1 ETH + 2.000 USDC (tổng 4.000 USD) vào hồ. Giá ETH đổi. So sánh **để trong hồ** với **cứ giữ nguyên trong ví**:

```
   giá mới    giữ nguyên ví    để trong hồ    chênh lệch
    1.000            3.000       2.828,43       −5,72%
    1.500            3.500       3.464,10       −1,03%
    2.000            4.000       4.000,00        0,00%
    3.000            5.000       4.898,98       −2,02%
    4.000            6.000       5.656,85       −5,72%
    8.000           10.000       8.000,00      −20,00%
```

**Giá đi lên hay đi xuống đều lỗ.** Chỉ hoà đúng khi giá quay về chỗ cũ — nên mới gọi là *tạm thời*, một cái tên gây hiểu nhầm: nếu giá không quay lại, khoản lỗ vĩnh viễn.

Lý do: hồ luôn tự cân lại theo `x·y=k`, nên nó **tự động bán tài sản đang lên và mua tài sản đang xuống**. Bạn đang bán rẻ cho những người kinh doanh chênh lệch giá — và chính họ là người kéo giá hồ khớp với giá thị trường. Phí giao dịch 0,3% là khoản đền bù cho việc đó. Có đủ đền hay không thì tuỳ cặp token.

> ⚠️ Đây là lý do các quảng cáo *"gửi tiền vào hồ, lãi 40%/năm"* thường không nói gì về việc số vốn gốc tính bằng USD có thể bốc hơi nhanh hơn số lãi.

---

## 9. Ví dụ 3 — Cho vay phi tập trung

Chương `11:27`. Video mô tả ngân hàng ngồi giữa **người gửi** và **người vay**, ăn phần chênh lãi suất — rồi thay chỗ ngồi đó bằng một smart contract.

```
   NGÂN HÀNG                          GIAO THỨC DEFI
   ─────────                          ──────────────
   người gửi ──▶ [ NGÂN HÀNG ] ──▶    người cấp thanh khoản ──▶ [ CONTRACT ] ──▶
                       │  người vay                                   │  người vay
                       ▼                                              ▼
              thẩm định + thế chấp                        thế chấp bằng CRYPTO
              (nhà, lương, lịch sử)                       (không hỏi bạn là ai)
```

Video nêu **AAVE** đang cho vay **6,5 tỷ USD** tại thời điểm ghi hình, và chỉ ra một điểm ngôn ngữ đáng chú ý: người gửi giờ được gọi là *"liquidity provider"* — *"nhưng bản chất y hệt nhau"*.

Câu hỏi video tự đặt ra và tự trả lời rất hay:

> **"Vay crypto mà phải thế chấp bằng crypto thì để làm gì?"**
> Trả lời: bạn đang có nhiều Bitcoin và **không muốn bán**, nhưng lại muốn có Ether. Thế chấp BTC, vay ETH, sau đó trả nợ và lấy lại BTC — giữ được cả hai.

Đây là câu trả lời đúng, và cũng là câu tự tố cáo: nhu cầu này là nhu cầu **giữ vị thế đầu cơ mà vẫn có thanh khoản**, không phải nhu cầu vay của đời sống. Nối lại với [§2](#2--ngân-hàng-thật-ra-làm-bốn-việc--defi-tách-rời-từng-việc).

---

## 10. 📚 Thế chấp vượt mức, thanh lý, và lãi suất tự nổi

Video dừng lại ở "bạn thế chấp, bạn vay, sau đó bạn trả". Nó không nói **chuyện gì xảy ra khi giá tài sản thế chấp rơi** — mà đó chính là toàn bộ phần rủi ro.

### Ba con số của một khoản vay

| Tham số             | Nghĩa                                   | Giá trị điển hình |
| ------------------- | --------------------------------------- | ----------------- |
| **LTV**             | vay tối đa bao nhiêu % giá trị thế chấp | 50–80%            |
| **Ngưỡng thanh lý** | vượt mức này là bị bán tài sản          | 75–85%            |
| **Thưởng thanh lý** | phần người thanh lý được ăn             | 5–10%             |

**Hệ số sức khoẻ** = (giá trị thế chấp × ngưỡng thanh lý) ÷ dư nợ. Xuống dưới **1** là bị thanh lý.

Chạy [code §23](#23-code-minh-hoạ) demo 3: thế chấp 10 ETH lúc giá 2.000 (tổng 20.000 USD), vay tối đa 15.000 USDC ở LTV 75%:

```
   giá ETH    hệ số sức khoẻ   trạng thái
    2.000              1,067   an toàn
    1.800              0,960   >>> BỊ THANH LÝ
    1.400              0,747   >>> BỊ THANH LÝ
    1.000              0,533   >>> BỊ THANH LÝ

   Ngưỡng vỡ: 1.875 USD/ETH — chỉ cần giá giảm 6,25%.
```

> 💥 **Vay kịch trần LTV nghĩa là bạn cách chỗ bị thanh lý đúng 6,25%.** Với một tài sản dao động 5%/ngày là chuyện thường. Không ai gọi điện nhắc bạn; bot quét liên tục và ai bắt được thì nuốt phần thưởng. Đây là lý do **các đợt sập giá crypto luôn có dạng thác đổ**: thanh lý ép bán → giá giảm tiếp → thanh lý tiếp.

### Lãi suất không do ai đặt ra

Đây là chỗ DeFi thật sự khác ngân hàng, và video hoàn toàn không nhắc. Lãi suất là **một hàm của tỉ lệ sử dụng vốn**:

```
   tỉ lệ sử dụng = (đang cho vay) / (tổng gửi vào)

   lãi suất
      ▲                                    ┌── dốc đứng
      │                                   ╱   (bảo vệ thanh khoản)
      │                              ____╱
      │      _______________________╱
      └──────────────────────────────┴─────────▶  tỉ lệ sử dụng
      0%                            80%       100%
                                "điểm gãy"
```

Vốn được vay càng nhiều thì lãi càng cao → hút thêm người gửi, đẩy bớt người vay. Sau **điểm gãy** (thường 80%) đường lãi dựng đứng, để luôn còn tiền cho người gửi rút. Không hội đồng nào họp, không ai bỏ phiếu. Đây là ví dụ hiếm hoi mà cụm *"code is law"* thật sự có nghĩa.

---

## 11. 📚 Vay chớp nhoáng — thứ chỉ tồn tại được nhờ tính nguyên tử

Video không nhắc tới **flash loan**, và đó là một khoảng trống lớn: nó vừa là phát minh độc đáo nhất của DeFi, vừa là công cụ đứng sau phần lớn các vụ hack lớn.

### Ý tưởng

> **Vay bao nhiêu tuỳ thích, không cần thế chấp gì cả — miễn là trả lại trong cùng một giao dịch.**

Nghe như đùa, nhưng nó chạy được nhờ đúng một tính chất đã học ở [Bài 3](../ly_thuyet/lesson_3_smart_contract.md): **tính nguyên tử**. Một giao dịch trên EVM hoặc thành công trọn vẹn, hoặc bị quay lui sạch như chưa từng xảy ra.

```
   TRONG MỘT GIAO DỊCH:
   ┌──────────────────────────────────────────────────┐
   │ 1. vay 50 triệu USDC       (không thế chấp)      │
   │ 2. làm gì đó với 50 triệu                        │
   │ 3. trả 50 triệu + phí                            │
   └──────────────────────────────────────────────────┘
     nếu tới bước 3 mà không đủ tiền -> TOÀN BỘ bị huỷ,
     như thể bước 1 chưa bao giờ diễn ra. Nên rủi ro cho
     bên cho vay bằng KHÔNG.
```

Công dụng lành mạnh: kinh doanh chênh lệch giá giữa hai sàn, đảo tài sản thế chấp, tự thanh lý để tránh mất phí phạt. Nhưng nó cũng xoá sạch rào cản vốn của kẻ tấn công: **để bẻ một thị trường, giờ bạn không cần giàu nữa.**

### Bẻ oracle bằng flash loan

Ghép [đường cong AMM ở §8](#8--amm--sàn-phi-tập-trung-thật-sự-khớp-lệnh-thế-nào) với [giao thức cho vay ở §10](#10--thế-chấp-vượt-mức-thanh-lý-và-lãi-suất-tự-nổi). Giả sử giao thức cho vay lấy giá tài sản **từ chính giá giao ngay của hồ**. Chạy demo 4:

```
   Hồ XYZ/USDC: 10.000 XYZ / 1.000.000 USDC  ->  giá 100 USD
   Kẻ tấn công: vốn riêng 200.000, vay chớp nhoáng 5.000.000

   [1] Mua 8.329,2 XYZ  -> giá giao ngay nhảy lên 3.591 USD  (×35,9)
   [2] Thế chấp 500 XYZ -> giao thức định giá 1.795.500 -> cho vay 1.346.625 USDC
   [3] Bán lại 8.329,2 XYZ -> thu về 4.994.982 USDC, giá về 100,5
   [4] Trả 5.000.000 vay chớp nhoáng

   Kẻ tấn công lãi : 1.341.607 USD
   Giao thức còn   : 500 XYZ (giá thật 50.000 USD) đổi lấy khoản nợ 1.346.625 USD
   -> Nợ xấu 1.296.625 USD.
```

**Không có thuật toán mật mã nào bị bẻ.** Chữ ký vẫn đúng, hash vẫn đúng, contract chạy đúng từng dòng như đã viết. Cái sai nằm ở một giả định không được nói ra: *"giá giao ngay trong hồ phản ánh giá thị trường"*. Trong một giao dịch duy nhất, giả định đó sai hoàn toàn.

### Bản vá

```
   ❌ giá giao ngay của một hồ   -> bẻ được trong 1 giao dịch
   ⚠️ TWAP (trung bình 30 phút)  -> muốn bẻ phải giữ giá lệch suốt 30 phút,
                                    tốn kém và bị kinh doanh chênh lệch ăn
   ✅ oracle ngoài chuỗi nhiều nguồn (Chainlink)  -> phải mua chuộc nhiều bên báo giá
```

Demo in ra kết quả khi thay bằng TWAP: cùng 500 XYZ thế chấp chỉ vay được **37.500 USD** — dưới cả vốn riêng bỏ ra, tấn công lỗ.

> 📌 Đây đúng là **bài toán oracle** của [Bài 3](../ly_thuyet/lesson_3_smart_contract.md), gặp lại ở dạng đắt tiền nhất. Vụ **Mango Markets** (10/2022, ~114 triệu USD) và **Beanstalk** (04/2022, ~182 triệu USD) đều là biến thể của đúng kịch bản trên.

---

## 12. Ví dụ 4 — Tài chính thời gian thực

Chương `13:37`. Ví dụ ngắn nhất, và là ví dụ dễ thương nhất trong bài nói.

> Người làm công ăn lương nhận tiền **một lần mỗi tháng**. Vì sao không phải mỗi ngày? Mỗi giờ? **Mỗi giây?**

Video nêu giao thức **Sablier**: chủ lao động nạp một cục tiền vào contract, contract được lập trình để **nhỏ giọt** ra theo thời gian hoặc theo điều kiện — ví dụ trả theo từng giờ có mặt tại nơi làm.

```
   TRẢ LƯƠNG THÁNG               DÒNG TIỀN LIÊN TỤC
   ───────────────               ──────────────────
   ▐                             ▁▂▃▄▅▆▇█▇▆▅▄▃▂▁ chảy đều
   ▐  một cục, ngày 30           mỗi giây một chút
   ▐                             rút lúc nào cũng được
```

Lý do trả lương theo tháng vốn là **chi phí xử lý**: mỗi lần chạy bảng lương đều tốn tiền và tốn người. Khi chi phí đó tiến về 0 thì kỳ hạn một tháng mất lý do tồn tại.

> 🔍 **Vì sao 2026 vẫn chưa thấy ai trả lương kiểu này?** Không phải vì công nghệ. Vì thuế khấu trừ tại nguồn, bảo hiểm xã hội, luật lao động và kế toán đều được xây quanh **kỳ lương**. Đây là mẫu hình lặp lại khắp bài: *rào cản không nằm ở mật mã*.

---

## 13. Ví dụ 5 — NFT

Chương `14:37`.

**Fungible** (thay thế được) vs **non-fungible** (không thay thế được) — video giải thích bằng tờ đô la:

```
   THAY THẾ ĐƯỢC                    KHÔNG THAY THẾ ĐƯỢC
   ─────────────                    ───────────────────
   Tôi có 1 đô, bạn có 1 đô,        Bức tranh A ≠ bức tranh B.
   đổi cho nhau -> không có gì      Đổi cho nhau là chuyện khác hẳn.
   xảy ra. Cả hai vẫn có 1 đô.
   Tờ nào không quan trọng.
```

Vấn đề video đặt ra: **file số sao chép được vô hạn, bản nào cũng giống hệt bản nào**. Vậy làm sao biết ai sở hữu *bản gốc*? Câu trả lời của video:

> Lấy dấu vân tay của file, đặt tên cho nó, ghi vào một smart contract — **gần giống như tạo ra một loại tiền mã hoá chỉ có đúng một đồng**.

Đó là cách diễn đạt chuẩn nhất về mặt kỹ thuật trong cả bài nói. Sau đó chuỗi làm việc nó giỏi nhất: ghi lại token được tạo lúc nào, và mỗi lần đổi chủ thì ai bán cho ai, giá bao nhiêu.

Video liệt kê ứng dụng: tranh số, **tweet** (nhắc vụ nhà sáng lập Twitter bán dòng tweet đầu tiên), vé xem nhạc (mỗi vé gắn với ban nhạc + ngày + số ghế nên vốn dĩ độc nhất), vật phẩm hiếm trong game (skin Fortnite, item Minecraft).

---

## 14. 📚 NFT sở hữu cái gì, và không sở hữu cái gì

Đây là chỗ mọi giải thích ngắn về NFT đều để lại hiểu nhầm, kể cả video này.

```
   NGƯỜI TA TƯỞNG                    THỰC TẾ TRÊN CHUỖI
   ──────────────                    ──────────────────
   "Tôi sở hữu bức tranh"            Bạn sở hữu một DÒNG trong smart contract
                                     ghi rằng địa chỉ của bạn gắn với token #1234

   "File nằm trên blockchain"        Gần như không bao giờ. Chuỗi chỉ giữ một
                                     ĐƯỜNG DẪN. File nằm trên IPFS, hoặc tệ hơn,
                                     trên máy chủ web của dự án.

   "Tôi có bản quyền"                Không, trừ khi hợp đồng ngoài đời cho bạn.
                                     Bản quyền là chuyện của luật, không phải chuỗi.
```

Ba hệ quả rất cụ thể:

1. **Đường dẫn chết là hết.** Nếu metadata trỏ tới một máy chủ web và dự án ngừng trả tiền hosting, NFT của bạn còn nguyên trên chuỗi và trỏ vào hư không. IPFS đỡ hơn vì địa chỉ nội dung chính là hash, nhưng vẫn cần ai đó ghim file lại.
2. **Không có gì ngăn "đúc" lại cùng một file.** Bất kỳ ai cũng tạo được NFT khác trỏ vào đúng bức tranh đó. Chuỗi không biết ai là tác giả. Tính khan hiếm hoàn toàn đến từ **việc xã hội công nhận contract nào là contract thật**.
3. **Tính thanh khoản là ảo tưởng.** Chính ví dụ video dùng là minh chứng đắt giá nhất — xem [§20](#20--kiểm-lại-bốn-con-số-của-video).

> ✅ **Chỗ NFT thật sự hợp lý:** khi vật phẩm **sinh ra trên chuỗi** và **chỉ có ý nghĩa trên chuỗi** — vé sự kiện kiểm bằng ví, thành tựu trong game blockchain, tên miền ENS, chứng nhận thành viên. Lúc đó không có khoảng cách giữa token và vật, vì token **chính là** vật.

---

## 15. Ví dụ 6 — DAO

Chương `17:56`. **DAO** = *decentralized autonomous organization* — tổ chức được quản trị bằng blockchain.

> **Không có sếp, không có quản lý.** Cấu trúc phẳng, mọi người ngang nhau. Cổ đông có phiếu bầu, đề xuất nào nhiều phiếu nhất thì thắng — và **smart contract tự động thi hành** kết quả đó.

Contract của một DAO làm bốn việc:

```
   1. GIỮ TIỀN        toàn bộ ngân quỹ khoá trong contract
   2. GIỮ SỔ CỔ ĐÔNG  ai có bao nhiêu phiếu
   3. TỔ CHỨC BỎ PHIẾU ai cũng đề xuất được, ai cũng bỏ phiếu được
   4. THI HÀNH        đề xuất thắng -> contract TỰ chuyển tiền, không ai ký duyệt
```

Và nó **mã hoá luôn luật chơi**: *"mọi đề xuất cần tối thiểu 60% đồng thuận"*, hoặc *"tổ chức luôn phải giữ một mức tiền mặt dự phòng"*. Video nhấn mạnh: vì là chương trình, các luật này **được thi hành nghiêm ngặt, không có ngoại lệ**.

Ba ứng dụng video nêu: **quỹ từ thiện** (người góp bỏ phiếu chọn dự án), **sở hữu tập thể** (góp tiền mua nhà cho thuê Airbnb), **quỹ đầu tư mạo hiểm** (nhà đầu tư bỏ phiếu chọn startup).

> 😄 **Ghi chú vui của video ở `21:44`:** đọc lại whitepaper Ethereum của Vitalik Buterin năm **2013**, diễn giả phát hiện gần như **toàn bộ sáu ví dụ này đã có sẵn trong đó** — nên kết luận nửa đùa rằng Vitalik là người du hành thời gian. Chi tiết này đáng nhớ: DeFi không phải trào lưu 2020, nó là **bản thiết kế gốc** của Ethereum, chỉ mất bảy năm để hạ tầng đủ chín.

---

## 16. 📚 DAO trong thực tế — The DAO, ConstitutionDAO, và bài toán bỏ phiếu

Video mô tả DAO ở dạng lý tưởng. Lịch sử thì gồ ghề hơn nhiều, và ba câu chuyện dưới đây dạy ba bài học khác nhau.

### The DAO (2016) — "code is law" va vào thực tế

Quỹ đầu tư mạo hiểm phi tập trung, gọi được ~150 triệu USD, quy mô lớn nhất thời điểm đó. Tháng 6/2016 một lỗi **reentrancy** ([Bài 3](../ly_thuyet/lesson_3_smart_contract.md)) bị khai thác, ~3,6 triệu ETH bị rút ra.

Cộng đồng Ethereum đứng trước lựa chọn không có đáp án đẹp:

```
   ┌─ "Code is law" ────────────┐   ┌─ "Đây là trộm cắp" ─────────┐
   │ Contract chạy đúng như viết│   │ Ý định của mọi người rất rõ  │
   │ Mất tiền là bài học        │   │ Cứu, nếu không Ethereum chết │
   └────────────────────────────┘   └──────────────────────────────┘
              ↓                                    ↓
      Ethereum Classic (ETC)              Ethereum (ETH) — hard fork
```

**Bài học:** *bất biến là một lựa chọn xã hội, không phải một sự thật kỹ thuật.* Khi đủ đau, con người sẽ fork. Nối thẳng với [Bài 1 §7](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md).

### ConstitutionDAO (2021) — thắng ở phần dễ, thua ở phần khó

Hàng nghìn người góp ~47 triệu USD trong **một tuần** để đấu giá một bản in gốc Hiến pháp Mỹ tại Sotheby's. Phối hợp: xuất sắc. Kết quả: **thua** một tỷ phú đấu giá cao hơn. Rồi đến phần hoàn tiền — phí gas trên Ethereum lúc đó khiến nhiều người góp ít **tốn phí hoàn tiền gần bằng số đã góp**.

**Bài học:** DAO gom vốn và phối hợp cực giỏi. Nhưng **giao diện với thế giới thật** — ai cầm búa đấu giá, ai đứng tên tài sản, ai đóng thuế — thì không có smart contract nào giải.

### Bài toán bỏ phiếu theo token

Câu *"mọi người ngang nhau"* trong video cần một dấu sao to.

| Vấn đề                | Nội dung                                                                                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Giàu = quyền lực**  | một token một phiếu, nên đây là *cổ đông*, không phải *dân chủ*                                                                                                      |
| **Cử tri thờ ơ**      | tỉ lệ bỏ phiếu ở đa số DAO thấp thảm hại; vài ví lớn quyết định tất cả                                                                                               |
| **Mua phiếu**         | có cả thị trường cho thuê quyền bỏ phiếu                                                                                                                             |
| **Tấn công quản trị** | vay chớp nhoáng đủ token → tự bỏ phiếu chuyển hết ngân quỹ cho mình → trả nợ. Đúng kịch bản **Beanstalk 04/2022, ~182 triệu USD**, hoàn tất trong **một giao dịch**. |

Hàng cuối là chỗ [§11](#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử) và [§15](#15-ví-dụ-6--dao) đâm vào nhau: *"contract tự động thi hành đề xuất thắng phiếu"* là ưu điểm, cho tới khi ai đó mua được đa số phiếu bằng tiền đi vay trong 12 giây. Bản vá là **thời gian chờ** — đề xuất thắng phải đợi vài ngày mới thi hành, mà khoản vay chớp nhoáng thì không sống quá một giao dịch.

---

## 17. Ưu điểm — theo video

Chương `22:27`. Video gom thành ba nhóm:

| Nhóm                     | Nội dung                                                                       |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Phi tập trung, mở**    | ai cũng tham gia được, không điều kiện, không kiểm duyệt, mọi người ngang nhau |
| **Toàn quyền kiểm soát** | không trung gian, không ai chặn được bạn chuyển tiền cho ai                    |
| **Tốc độ và hiệu quả**   | không hạ tầng cũ kỹ, không thao tác thủ công, không con người ở giữa           |

Về nhóm thứ ba, diễn giả đưa đúng một phép thử rất sắc:

> *"Thử gửi tiền cho nhiều người cùng lúc qua hệ thống tài chính truyền thống mà xem."*

Đây là ưu điểm ít bị tranh cãi nhất: với **thanh toán lập trình được**, DeFi thắng rõ rệt. Trả tiền cho 10.000 địa chỉ theo một điều kiện tính toán được là chuyện vặt trên chuỗi, và là một dự án nhiều tháng trong ngân hàng.

---

## 18. Nhược điểm — theo video

Chương `23:56`. Video nêu **năm** nhược điểm, và mở đầu bằng một nhận xét rất đáng chú ý: *một số ưu điểm vừa kể cũng chính là nhược điểm.*

| #   | Nhược điểm                 | Video nói gì                                                                                          | Tới 2026                                                                                               |
| --- | -------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1   | **Toàn quyền kiểm soát**   | *"users aren't always clever"* — mất khoá riêng là mất sạch; chuyện người bới bãi rác tìm ổ cứng      | ⏸️ Không đổi. Ví thông minh + khôi phục xã hội có giúp, nhưng chưa phổ cập                              |
| 2   | **Mở rộng và tốc độ**      | Bitcoin 7 giao dịch/giây, Ethereum 20 — *"quá chậm để dựng một hệ thống tài chính"*                   | 🟡 Chain nền vẫn vậy; lớp 2 làm hàng nghìn/giây. Xem [§20](#20--kiểm-lại-bốn-con-số-của-video)          |
| 3   | **Trải nghiệm người dùng** | nhiều thuật ngữ, phải cài tiện ích trình duyệt, đầy lừa đảo giả mạo                                   | 🟡 Khá hơn, vẫn tệ                                                                                      |
| 4   | **Bảo mật**                | chuỗi thì an toàn, nhưng **smart contract do người viết** → có bug; và **bất biến nên không vá được** | 🔴 Vẫn là nguồn mất tiền lớn nhất. [§19](#19--bảo-mật-smart-contract--phân-loại-lỗi-và-bảng-các-vụ-lớn) |
| 5   | **Không có ai quản**       | không cơ quan quản lý, không bảo đảm; dẫn nghiên cứu nói 97% token trên Uniswap là *rug pull*         | 🟡 MiCA áp dụng ở EU, nhưng DeFi thuần vẫn nằm ngoài                                                    |

Nhược điểm số 4 là chỗ video nói chính xác và quan trọng nhất:

> **"Tôi nói blockchain rất an toàn, và tôi không nói dối. Nhưng các smart contract dựng trên nó thì khác — chúng là mã do con người viết."**

Đây đúng là luận điểm xuyên suốt cả khoá học: **mật mã không phải chỗ vỡ**. Chỗ vỡ là mọi thứ dựng bên trên nó.

---

## 19. 📚 Bảo mật smart contract — phân loại lỗi và bảng các vụ lớn

Video nói "có bug" nhưng không phân loại. Các vụ mất tiền lớn rơi vào một số khuôn mẫu lặp đi lặp lại, và biết mặt chúng thì đọc tin tức mới có ích.

| Loại lỗi                     | Cơ chế                                                                    | Ví dụ tiêu biểu                                            |
| ---------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Reentrancy**               | contract gọi ra ngoài trước khi cập nhật sổ sách; bên ngoài gọi ngược vào | The DAO 2016                                               |
| **Thao túng oracle**         | bẻ nguồn giá mà contract tin, thường bằng flash loan                      | Mango Markets 2022 (~114 tr), Cream Finance 2021 (~130 tr) |
| **Tấn công quản trị**        | mua/vay đủ phiếu rồi tự bỏ phiếu rút ngân quỹ                             | Beanstalk 2022 (~182 tr)                                   |
| **Lỗi kiểm chứng ở cầu nối** | cầu nối chấp nhận bằng chứng giả về tài sản ở chuỗi kia                   | Wormhole 2022 (~326 tr), BNB Chain 2022 (~570 tr)          |
| **Khoá riêng bị chiếm**      | không phải lỗi contract — lỗi con người giữ khoá                          | Ronin 2022 (~624 tr)                                       |
| **Kiểm soát truy cập sai**   | hàm quan trọng quên đặt điều kiện, ai gọi cũng được                       | Parity multisig 2017                                       |

Hai điều đáng rút ra từ bảng này:

1. **Hai vụ lớn nhất không phải lỗi DeFi.** Ronin là chiếm khoá riêng (kỹ thuật xã hội — một nhân viên nhận file tuyển dụng có mã độc); BNB Chain là lỗi ở cầu nối liên chuỗi. Cầu nối là mắt xích yếu nhất của cả ngành vì nó phải **tin một thứ gì đó ở ngoài chuỗi mình**.
2. **Bất biến cắt cả hai chiều.** Video nói đúng ở `27:00`: phát hiện lỗi cũng không sửa được. Ngành trả lời bằng **mẫu proxy** — nhưng đó là đánh đổi lấy rủi ro quản trị, như [§5](#5--bốn-tính-chất-smart-contract-thừa-hưởng--và-mặt-trái-của-từng-cái) đã nói.

> 📌 Nhớ lại demo 4 ở [§11](#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử): trong toàn bộ cuộc tấn công đó, **không có phép mật mã nào bị phá**. SHA-256 vẫn nguyên, ECDSA vẫn nguyên. Chỉ có một giả định về giá là sai.

---

## 20. 📚 Kiểm lại bốn con số của video

Bài này viết sau khi tải phụ đề gốc về, nên kiểm được từng con số. Bốn chỗ đáng đính chính.

### 1. Dòng tweet đầu tiên của Jack Dorsey

Video `17:01`: *"bán được vài triệu đô, tôi nghĩ khoảng 20 triệu gì đó."*

|                         |                                                                         |
| ----------------------- | ----------------------------------------------------------------------- |
| **Thực tế**             | Bán 3/2021 với **1.630 ETH ≈ 2,9 triệu USD** — không phải 20 triệu      |
| **Phần video không kể** | 4/2022 người mua rao bán lại. Giá chào cao nhất khoảng **vài trăm đô**. |

Đây là ví dụ tự nó phản bác chính nó, và là minh hoạ sống động nhất cho luận điểm *"tính thanh khoản là ảo tưởng"* ở [§14](#14--nft-sở-hữu-cái-gì-và-không-sở-hữu-cái-gì): một tài sản chỉ có giá bằng số tiền **người tiếp theo** sẵn sàng trả, và với NFT thì người tiếp theo hay biến mất.

### 2. "570 triệu USD bị lấy từ Binance"

Video `26:53` xếp vụ này vào nhóm lỗi smart contract. Chính xác hơn: đó là **cầu nối liên chuỗi của BNB Chain** (10/2022), lỗi ở khâu kiểm chứng bằng chứng Merkle, cho phép đúc khống ~2 triệu BNB. Phần thoát ra ngoài được nhỏ hơn nhiều con số danh nghĩa vì mạng bị dừng khẩn cấp.

Không phải sàn Binance bị hack, và không phải một ứng dụng DeFi thông thường. Phân biệt này quan trọng vì **cầu nối là hạng mục rủi ro riêng** ([§22](#22--xếp-rủi-ro-defi-theo-tầng)).

### 3. "97% token trên Uniswap là rug pull"

Con số này đến từ nghiên cứu học thuật thật, nhưng **mẫu số mới là chỗ đáng nhìn**:

```
   ĐẾM THEO SỐ TOKEN NIÊM YẾT           ĐẾM THEO KHỐI LƯỢNG GIAO DỊCH
   ─────────────────────────            ─────────────────────────────
   ~97% là bẫy                          đại đa số khối lượng nằm ở
   Nhưng phần lớn trong số đó           một nhúm cặp lớn (ETH/USDC...)
   có thanh khoản gần bằng 0
   và chưa từng có ai mua
```

Cả hai cách đếm đều đúng và nói hai chuyện khác nhau. Đúng là **niêm yết trên DEX không có nghĩa gì cả** — không ai duyệt, ai cũng tạo cặp được. Nhưng con số 97% không có nghĩa là 97% tiền của người dùng rơi vào bẫy.

### 4. "58 tỷ USD trong DeFi, tức 0,05% của cải thế giới"

Video `29:29` đưa ba con số: 58 tỷ (hiện tại), 244 tỷ (đỉnh cuối 2021), và 0,05% của cải toàn cầu. **Ba con số này không khớp nhau.**

```
   Của cải toàn cầu cuối 2021 ≈ 464 nghìn tỷ USD

    58 tỷ / 464 nghìn tỷ = 0,0125%     ← con số hiện tại
   244 tỷ / 464 nghìn tỷ = 0,053%      ← con số ĐỈNH
```

Tức là **0,05% được tính từ mốc đỉnh, rồi đặt cạnh mốc hiện tại**. Chênh **bốn lần**. Kết luận của video — *"vẫn còn rất sớm"* — không thay đổi, nhưng cách trình bày làm quy mô DeFi trông to gấp bốn thực tế lúc đó.

Ngoài ra con số TVL đỉnh khác nhau tuỳ nguồn (nguồn phổ biến nhất ghi khoảng 180 tỷ) vì mỗi bên đếm staking, chain phụ và tài sản tính hai lần theo cách khác nhau. Khi đọc TVL, luôn hỏi **ai đếm và đếm cái gì**.

---

## 21. DeFi chạy trên chain nào, và to cỡ nào

Chương `28:27`. Video trả lời hai câu hỏi hay gặp.

**Chạy trên chain nào?** Nhiều chain, nhưng lớn nhất là **Ethereum** — nhờ **lợi thế người đi trước**: nó là chuỗi đầu tiên có smart contract. Video dự đoán các chain khác sẽ đuổi theo bằng **tốc độ cao hơn và phí thấp hơn**, và Ethereum chỉ giữ được ngôi đầu nếu cải thiện hai thứ đó.

Dự đoán này về cơ bản **đã đúng**, chỉ khác đường đi:

```
   VIDEO 2022 HÌNH DUNG              THỰC TẾ TỚI 2026
   ────────────────────              ────────────────
   Ethereum tự nhanh lên             Ethereum KHÔNG tự nhanh lên.
   ("Ethereum 2.0, hàng trăm         Chain nền vẫn khoảng 15–20 giao dịch/giây.
    nghìn giao dịch/giây,            Thay vào đó nó đẩy tốc độ sang LỚP 2,
    hy vọng là năm sau")             và tự nhận vai trò lớp thanh toán + dữ liệu.
```

Hai điều chỉnh cần thiết cho người xem video hôm nay:

- **"Ethereum 2.0"** là tên gọi đã bị chính Ethereum Foundation bỏ từ đầu 2022. Phần chuyển sang Proof of Stake — *The Merge* — đã hoàn tất **9/2022**, tức là **trước** bài nói này ([Bài 5](../ly_thuyet/lesson_5_proof_of_stake.md)). Cái diễn giả nói "hy vọng năm sau" là phần **mở rộng quy mô**, và phần đó đã đi hướng khác.
- **Sharding kiểu chia nhỏ chuỗi đã bị bỏ**, thay bằng lộ trình lấy rollup làm trung tâm: chuỗi chính không xử lý nhiều giao dịch hơn, nó chỉ cung cấp **chỗ chứa dữ liệu rẻ** cho các lớp 2 làm việc đó. Bản nâng cấp đưa "blob" dữ liệu giá rẻ vào (2024) là bước quyết định. Nếu bạn đã đọc [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md), zkRollup chính là nhánh tinh vi nhất của hướng này.

**To cỡ nào?** Video: 58 tỷ USD đang khoá trong DeFi, từng đạt 244 tỷ cuối 2021, và *"chỉ bằng 0,05% của cải thế giới"* → kết luận **vẫn còn rất sớm**. Số học của ba con số này đã kiểm ở [§20](#20--kiểm-lại-bốn-con-số-của-video); kết luận thì vẫn đứng vững.

---

## 22. 📚 Xếp rủi ro DeFi theo tầng

Cách hữu ích nhất để nghĩ về rủi ro DeFi không phải "an toàn hay không", mà là **tiền có thể bốc hơi ở tầng nào**. Mỗi tầng có xác suất và cách phòng khác nhau.

```
   ┌─────────────────────────────────────────────────────────┐
   │ 6. PHÁP LÝ      giao thức bị chặn, ví bị đưa vào sổ đen │
   ├─────────────────────────────────────────────────────────┤
   │ 5. QUẢN TRỊ     ai giữ khoá nâng cấp? ai bỏ phiếu?      │
   ├─────────────────────────────────────────────────────────┤
   │ 4. KINH TẾ      thanh lý dây chuyền, tổn thất tạm thời, │
   │                 mô hình lãi suất sai                     │
   ├─────────────────────────────────────────────────────────┤
   │ 3. ORACLE       giá contract tin có bẻ được không?      │
   ├─────────────────────────────────────────────────────────┤
   │ 2. HỢP ĐỒNG     bug trong mã. Có kiểm toán không?        │
   ├─────────────────────────────────────────────────────────┤
   │ 1. CHUỖI NỀN    51%, chuỗi ngừng chạy — HIẾM NHẤT       │
   └─────────────────────────────────────────────────────────┘
        ▲ tầng càng cao, càng hay mất tiền ở đó
```

> **Quy luật của cả khoá học, phát biểu lần cuối:** tầng dưới cùng — thứ mà tám bài lý thuyết dành toàn bộ thời lượng để dựng — là tầng **ít khi hỏng nhất**. Gần như toàn bộ tiền mất mát trong lịch sử DeFi rơi ở tầng 2 tới tầng 5.

### Bảng câu hỏi trước khi bỏ tiền vào một giao thức

| Tầng     | Câu phải hỏi                                        | Dấu hiệu xấu                                                          |
| -------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| Hợp đồng | Đã kiểm toán chưa, bởi ai, báo cáo công khai không? | "sắp kiểm toán", hoặc chỉ có tên đơn vị kiểm toán mà không có báo cáo |
| Oracle   | Giá lấy từ đâu?                                     | giá giao ngay từ một hồ duy nhất                                      |
| Kinh tế  | Lợi nhuận đến từ đâu?                               | không giải thích được nguồn, hoặc trả bằng chính token của dự án      |
| Quản trị | Ai nâng cấp được contract? Có thời gian chờ không?  | một ví đơn lẻ, nâng cấp có hiệu lực tức thì                           |
| Pháp lý  | Ai đứng sau?                                        | ẩn danh hoàn toàn **và** giữ quyền nâng cấp                           |

Câu hàng thứ ba đáng nhấn: **lợi nhuận luôn phải đến từ một chỗ nào đó.** Trong DeFi, nguồn hợp lệ chỉ có mấy loại — phí giao dịch trả cho hồ, lãi người vay trả, phần thưởng đồng thuận. Nếu lãi suất công bố cao hơn hẳn ba nguồn đó, thì phần dôi ra đang đến từ **việc phát hành thêm token của chính dự án**, tức là từ túi người vào sau.

---

## 23. Code minh hoạ

Bốn cơ chế mà video nhắc tới nhưng không mở ra. Tất cả số liệu ở các mục trên đều là kết quả chạy thật của đoạn mã này.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
/**
 * Bài 10 — DeFi: bốn cơ chế mà video nói tới nhưng không mở ra.
 * Chạy: node demo.ts   (Node 22.6+, không cần cài gì)
 */
import { strict as assert } from "node:assert";

const usd = (n: number): string =>
  n.toLocaleString("en-US", { maximumFractionDigits: 2 });
const pct = (n: number): string => (n * 100).toFixed(2) + "%";

/* ===========================================================================
 * 1. AMM — sàn phi tập trung KHÔNG khớp lệnh mua/bán như video mô tả.
 *    Nó dùng một công thức: x * y = k. Giá do tỉ lệ hai kho quyết định.
 * ======================================================================== */
class Pool {
  x: number; // kho token (vd ETH)
  y: number; // kho stablecoin (vd USDC)
  readonly feeBps: number; // phí, đơn vị 1/10000. Uniswap v2 = 30 (0,3%)

  constructor(x: number, y: number, feeBps = 30) {
    this.x = x;
    this.y = y;
    this.feeBps = feeBps;
  }

  get k(): number {
    return this.x * this.y;
  }

  /** Giá giao ngay = tỉ lệ hai kho. KHÔNG phải giá thị trường thật. */
  spotPrice(): number {
    return this.y / this.x;
  }

  /** Bán dx token, nhận về bao nhiêu stablecoin. Công thức Uniswap v2. */
  sellX(dx: number): number {
    const dxAfterFee = dx * (1 - this.feeBps / 10_000);
    const dy = (this.y * dxAfterFee) / (this.x + dxAfterFee);
    this.x += dx;
    this.y -= dy;
    return dy;
  }

  /** Mua token bằng dy stablecoin. */
  buyX(dy: number): number {
    const dyAfterFee = dy * (1 - this.feeBps / 10_000);
    const dx = (this.x * dyAfterFee) / (this.y + dyAfterFee);
    this.y += dy;
    this.x -= dx;
    return dx;
  }
}

console.log("=== 1. Truot gia: vi sao lenh cang to cang lo ===");
{
  console.log("  Ho: 100 ETH / 200.000 USDC  ->  gia niem yet 2.000 USDC/ETH\n");
  console.log("  ban      nhan duoc      gia thuc te   truot gia");
  for (const dx of [0.1, 1, 5, 10, 25]) {
    const pool = new Pool(100, 200_000);
    const priceBefore = pool.spotPrice();
    const received = pool.sellX(dx);
    const executionPrice = received / dx;
    console.log(
      `  ${String(dx).padStart(5)} ETH  ${usd(received).padStart(11)}  ` +
        `${usd(executionPrice).padStart(9)}  ${pct(1 - executionPrice / priceBefore).padStart(9)}`,
    );
  }
  console.log("\n  -> Khong co so lenh. Khong co nguoi ban doi ung.");
  console.log("     Gia CHINH LA ti le hai kho, va lenh cua ban tu lam no lech.");
}

/* ===========================================================================
 * 2. Tổn thất tạm thời — cái giá của việc làm "nhà cung cấp thanh khoản"
 *    mà video gọi là saver nhưng không nói tới rủi ro.
 * ======================================================================== */
console.log("\n=== 2. Ton that tam thoi (impermanent loss) ===");
{
  const priceAtDeposit = 2_000;
  console.log("  Gui vao ho: 1 ETH + 2.000 USDC (tong 4.000 USD)\n");
  console.log("  gia moi   giu nguyen vi   de trong ho    chenh lech");
  for (const newPrice of [1_000, 1_500, 2_000, 3_000, 4_000, 8_000]) {
    const priceRatio = newPrice / priceAtDeposit;
    const valueIfHeld = 1 * newPrice + 2_000;
    // Trong ho: x*y=k không đổi, kho tự cân lại theo giá mới.
    const valueInPool = 2 * Math.sqrt(priceRatio) * 2_000;
    console.log(
      `  ${usd(newPrice).padStart(7)}  ${usd(valueIfHeld).padStart(13)}  ` +
        `${usd(valueInPool).padStart(12)}  ${pct(valueInPool / valueIfHeld - 1).padStart(10)}`,
    );
  }
  console.log("\n  -> Gia di theo huong nao cung lo so voi viec cu giu.");
  console.log("     Chi hoa khi gia quay ve cho cu. Phi giao dich la thu bu lai.");
  assert(2 * Math.sqrt(1) * 2_000 === 4_000, "gia khong doi thi khong lo");
}

/* ===========================================================================
 * 3. Cho vay thế chấp vượt mức + thanh lý.
 *    Video nói "bạn thế chấp Bitcoin để vay Ether". Nó không nói: nếu giá
 *    tài sản thế chấp rơi thì chuyện gì xảy ra.
 * ======================================================================== */
class LendingPosition {
  readonly maxLtv = 0.75; // vay tối đa 75% giá trị thế chấp
  readonly liquidationThreshold = 0.8; // vượt 80% là bị thanh lý
  readonly liquidationBonus = 0.05; // người thanh lý ăn 5%
  collateral: number; // số ETH đang thế chấp
  debt: number; // số USDC đang nợ

  constructor(collateral = 0, debt = 0) {
    this.collateral = collateral;
    this.debt = debt;
  }

  /** Dưới 1 là bị thanh lý. */
  healthFactor(ethPrice: number): number {
    if (this.debt === 0) return Infinity;
    return (this.collateral * ethPrice * this.liquidationThreshold) / this.debt;
  }
}

console.log("\n=== 3. Vay the chap va nguong thanh ly ===");
{
  const position = new LendingPosition(10, 0); // gửi 10 ETH
  const initialPrice = 2_000;
  const maxBorrow = position.collateral * initialPrice * position.maxLtv;
  position.debt = maxBorrow;
  console.log(`  The chap : 10 ETH @ ${usd(initialPrice)} = ${usd(10 * initialPrice)} USD`);
  console.log(`  Vay ra   : ${usd(maxBorrow)} USDC (LTV 75%)\n`);
  console.log("  gia ETH    he so suc khoe   trang thai");
  for (const price of [2_000, 1_800, 1_400, 1_250, 1_200, 1_000]) {
    const health = position.healthFactor(price);
    const status = health >= 1 ? "an toan" : ">>> BI THANH LY";
    console.log(
      `  ${usd(price).padStart(7)}  ${health.toFixed(3).padStart(14)}   ${status}`,
    );
  }
  const breakEvenPrice = position.debt / (position.collateral * position.liquidationThreshold);
  console.log(`\n  -> Nguong vo: ${usd(breakEvenPrice)} USD/ETH, tuc chi can giam ${pct(1 - breakEvenPrice / initialPrice)}.`);
  console.log("     Khong ai goi dien bao truoc. Bot quet lien tuc, thay la nuot.");
  assert(position.healthFactor(breakEvenPrice) < 1.0000001 && position.healthFactor(breakEvenPrice) > 0.9999999);
}

/* ===========================================================================
 * 4. Vay chớp nhoáng + thao túng oracle.
 *    Video nói smart contract "luôn chạy đúng như đã viết". Đúng. Vấn đề là
 *    cái nó ĐỌC có thể bị bẻ trong đúng một giao dịch.
 * ======================================================================== */
console.log("\n=== 4. Vay chop nhoang be gia oracle ===");
{
  // Ho nho cua mot token von hoa thap. Giao thuc cho vay lay gia tu chinh ho nay.
  const pool = new Pool(10_000, 1_000_000); // 1 XYZ = 100 USDC
  console.log(`  Ho XYZ/USDC: 10.000 XYZ / 1.000.000 USDC -> gia ${usd(pool.spotPrice())} USD`);

  const ownCapital = 200_000; // tiền túi kẻ tấn công
  const flashLoan = 5_000_000; // vay trong 1 giao dich, phai tra ngay cuoi
  console.log(`  Ke tan cong: von rieng ${usd(ownCapital)}, vay chop nhoang ${usd(flashLoan)}\n`);

  // Bước 1: mua sạch XYZ bằng tiền vay -> đẩy giá giao ngay lên trời.
  const boughtXyz = pool.buyX(flashLoan);
  const pumpedPrice = pool.spotPrice();
  console.log(`  [1] Mua ${boughtXyz.toFixed(1)} XYZ  -> gia giao ngay nhay len ${usd(pumpedPrice)} USD (x${(pumpedPrice / 100).toFixed(1)})`);

  // Bước 2: thế chấp một ít XYZ, giao thức định giá theo giá vừa bị bơm.
  const collateral = 500; // XYZ mua san tu truoc bang von rieng
  const borrowed = collateral * pumpedPrice * 0.75;
  console.log(`  [2] The chap ${collateral} XYZ -> giao thuc dinh gia ${usd(collateral * pumpedPrice)} -> cho vay ${usd(borrowed)} USDC`);

  // Bước 3: bán XYZ trả lại, giá về gần cũ.
  const soldBack = pool.sellX(boughtXyz);
  console.log(`  [3] Ban lai ${boughtXyz.toFixed(1)} XYZ -> thu ve ${usd(soldBack)} USDC, gia ve ${usd(pool.spotPrice())}`);

  const profit = soldBack + borrowed - flashLoan;
  console.log(`  [4] Tra ${usd(flashLoan)} vay chop nhoang.`);
  console.log(`\n  Ket qua ke tan cong: ${usd(profit)} USD (chua tru phi)`);
  console.log(`  Giao thuc con lai  : ${collateral} XYZ, gia that ${usd(collateral * 100)} USD, doi lai khoan no ${usd(borrowed)} USD`);
  console.log(`  -> No xau ${usd(borrowed - collateral * 100)} USD. Khong ai be duoc mat ma nao ca.`);

  console.log("\n  Ban va: lay gia trung binh theo thoi gian (TWAP) hoac oracle ngoai chuoi.");
  const twapPrice = 100; // giá trung bình 30 phút — không kịp nhúc nhích trong 1 giao dịch
  console.log(`  Voi TWAP = ${usd(twapPrice)}: the chap ${collateral} XYZ chi vay duoc ${usd(collateral * twapPrice * 0.75)} USD -> tan cong lo von.`);
  assert(collateral * twapPrice * 0.75 < ownCapital, "voi TWAP thi khong con loi nhuan");
}

console.log("\nXong. Bon co che: AMM, ton that tam thoi, thanh ly, thao tung oracle.");
```

Kết quả chạy thật:

```
=== 1. Truot gia: vi sao lenh cang to cang lo ===
  Ho: 100 ETH / 200.000 USDC  ->  gia niem yet 2.000 USDC/ETH

  ban      nhan duoc      gia thuc te   truot gia
    0.1 ETH        199.2   1,992.01      0.40%
      1 ETH     1,974.32   1,974.32      1.28%
      5 ETH     9,496.59   1,899.32      5.03%
     10 ETH    18,132.22   1,813.22      9.34%
     25 ETH    39,903.94   1,596.16     20.19%

  -> Khong co so lenh. Khong co nguoi ban doi ung.
     Gia CHINH LA ti le hai kho, va lenh cua ban tu lam no lech.

=== 2. Ton that tam thoi (impermanent loss) ===
  Gui vao ho: 1 ETH + 2.000 USDC (tong 4.000 USD)

  gia moi   giu nguyen vi   de trong ho    chenh lech
    1,000          3,000      2,828.43      -5.72%
    1,500          3,500       3,464.1      -1.03%
    2,000          4,000         4,000       0.00%
    3,000          5,000      4,898.98      -2.02%
    4,000          6,000      5,656.85      -5.72%
    8,000         10,000         8,000     -20.00%

  -> Gia di theo huong nao cung lo so voi viec cu giu.
     Chi hoa khi gia quay ve cho cu. Phi giao dich la thu bu lai.

=== 3. Vay the chap va nguong thanh ly ===
  The chap : 10 ETH @ 2,000 = 20,000 USD
  Vay ra   : 15,000 USDC (LTV 75%)

  gia ETH    he so suc khoe   trang thai
    2,000           1.067   an toan
    1,800           0.960   >>> BI THANH LY
    1,400           0.747   >>> BI THANH LY
    1,250           0.667   >>> BI THANH LY
    1,200           0.640   >>> BI THANH LY
    1,000           0.533   >>> BI THANH LY

  -> Nguong vo: 1,875 USD/ETH, tuc chi can giam 6.25%.
     Khong ai goi dien bao truoc. Bot quet lien tuc, thay la nuot.

=== 4. Vay chop nhoang be gia oracle ===
  Ho XYZ/USDC: 10.000 XYZ / 1.000.000 USDC -> gia 100 USD
  Ke tan cong: von rieng 200,000, vay chop nhoang 5,000,000

  [1] Mua 8329.2 XYZ  -> gia giao ngay nhay len 3,591 USD (x35.9)
  [2] The chap 500 XYZ -> giao thuc dinh gia 1,795,500 -> cho vay 1,346,625 USDC
  [3] Ban lai 8329.2 XYZ -> thu ve 4,994,982.45 USDC, gia ve 100.5
  [4] Tra 5,000,000 vay chop nhoang.

  Ket qua ke tan cong: 1,341,607.45 USD (chua tru phi)
  Giao thuc con lai  : 500 XYZ, gia that 50,000 USD, doi lai khoan no 1,346,625 USD
  -> No xau 1,296,625 USD. Khong ai be duoc mat ma nao ca.

  Ban va: lay gia trung binh theo thoi gian (TWAP) hoac oracle ngoai chuoi.
  Voi TWAP = 100: the chap 500 XYZ chi vay duoc 37,500 USD -> tan cong lo von.

Xong. Bon co che: AMM, ton that tam thoi, thanh ly, thao tung oracle.
```

**Tự thử:**

1. Đổi `feeBps` từ 30 thành 100 (1%) rồi chạy lại demo 2 — phí có bù nổi tổn thất tạm thời không?
2. Trong demo 4, giảm `flashLoan` xuống 500.000. Hồ càng sâu so với số tiền tấn công thì đòn bẩy càng yếu — bao nhiêu là đủ để tấn công không còn lời?
3. Ghép demo 3 và 4: dùng giá bị bơm để **thanh lý oan** một người vay hoàn toàn khoẻ mạnh. Đây chính là kịch bản Mango Markets.

---

## 24. Từ điển thuật ngữ

| Tiếng Anh               | Tiếng Việt                    | Nghĩa gọn                                                 |
| ----------------------- | ----------------------------- | --------------------------------------------------------- |
| DeFi                    | tài chính phi tập trung       | ứng dụng tài chính dựng trên blockchain                   |
| Smart contract          | hợp đồng thông minh           | chương trình sống trong chuỗi, tự thi hành                |
| AMM                     | tạo lập thị trường tự động    | định giá bằng công thức `x·y=k` thay vì sổ lệnh           |
| Liquidity pool          | hồ thanh khoản                | kho hai token mà AMM giao dịch với bạn                    |
| Liquidity provider (LP) | người cấp thanh khoản         | người gửi token vào hồ, ăn phí, chịu tổn thất tạm thời    |
| Slippage                | trượt giá                     | chênh giữa giá niêm yết và giá thực tế nhận được          |
| Impermanent loss        | tổn thất tạm thời             | lỗ so với việc cứ giữ nguyên tài sản trong ví             |
| Overcollateralization   | thế chấp vượt mức             | phải khoá nhiều hơn số vay                                |
| LTV                     | tỉ lệ vay trên giá trị        | vay tối đa bao nhiêu % giá trị thế chấp                   |
| Health factor           | hệ số sức khoẻ                | dưới 1 là bị thanh lý                                     |
| Liquidation             | thanh lý                      | bán tài sản thế chấp để trả nợ                            |
| Flash loan              | vay chớp nhoáng               | vay không thế chấp, phải trả trong cùng giao dịch         |
| Atomicity               | tính nguyên tử                | giao dịch hoặc trọn vẹn, hoặc quay lui sạch               |
| Oracle                  | nguồn dữ liệu ngoài chuỗi     | thứ cho contract biết giá; điểm yếu kinh điển             |
| TWAP                    | giá trung bình theo thời gian | giá lấy trung bình một khoảng, chống bẻ trong 1 giao dịch |
| NFT                     | token không thay thế được     | token độc nhất, dùng để theo dõi quyền sở hữu             |
| Fungible                | thay thế được                 | mọi đơn vị như nhau (tiền)                                |
| DAO                     | tổ chức tự trị phi tập trung  | tổ chức quản trị bằng bỏ phiếu on-chain                   |
| Governance attack       | tấn công quản trị             | mua/vay đủ phiếu rồi tự bỏ phiếu rút ngân quỹ             |
| Rug pull                | rút thảm                      | đội dự án ôm tiền biến mất                                |
| TVL                     | tổng giá trị khoá             | thước đo quy mô DeFi; tuỳ nguồn đếm khác nhau             |
| Proxy pattern           | mẫu uỷ nhiệm                  | cách nâng cấp contract "bất biến"                         |
| Money legos             | ghép nối như Lego             | contract gọi contract, ghép thành ứng dụng phức tạp       |

---

## 25. Câu hỏi tự kiểm tra

1. Video nói *"blockchains are static"*. Nói chính xác hơn thì Bitcoin thiếu cái gì mà Ethereum có?
2. Ngân hàng làm bốn việc. DeFi thay được hai, né một, và không làm được một. Kể tên từng cái.
3. Vì sao DeFi **không thể** cho vay tiêu dùng?
4. Trong ví dụ gọi vốn cộng đồng, smart contract giải được rủi ro nào và **không** giải được rủi ro nào?
5. Video mô tả DEX là "ghép người muốn làm điều ngược nhau". Mô hình thực tế khác thế nào, và vì sao mô hình video mô tả đã thất bại?
6. Viết công thức AMM. Vì sao lệnh càng lớn giá thực tế càng tệ?
7. Bán 25 ETH vào hồ 100 ETH trượt giá 20%, trong khi phí chỉ 0,3%. 19,7% còn lại đi đâu?
8. Tổn thất tạm thời xảy ra khi giá **tăng**, giá **giảm**, hay cả hai? Khi nào nó bằng 0?
9. Vì sao gọi là "tạm thời" mà lại có thể vĩnh viễn?
10. Thế chấp 10 ETH giá 2.000, vay kịch trần LTV 75%, ngưỡng thanh lý 80%. Giá phải rơi bao nhiêu phần trăm thì bị thanh lý? Tự tính, đừng nhìn lại §10.
11. Vì sao các đợt sập giá crypto luôn có dạng thác đổ?
12. Lãi suất trong giao thức cho vay DeFi do ai quyết định?
13. Vay chớp nhoáng không cần thế chấp mà bên cho vay vẫn **không có rủi ro**. Tính chất nào của EVM làm điều đó khả thi?
14. Trong demo 4, kẻ tấn công lãi 1,34 triệu USD. Có phép mật mã nào bị bẻ không? Giả định sai nằm ở đâu?
15. Vì sao TWAP chặn được kịch bản đó, còn giá giao ngay thì không?
16. NFT của bạn trỏ tới một file. File đó nằm ở đâu? Chuyện gì xảy ra nếu dự án ngừng trả tiền máy chủ?
17. Có gì ngăn người khác tạo NFT khác trỏ vào đúng bức tranh của bạn không?
18. Vụ The DAO 2016 kết thúc bằng một hard fork. Điều đó nói gì về câu "blockchain là bất biến"?
19. ConstitutionDAO gom được 47 triệu USD trong một tuần rồi vẫn thất bại. Nó thắng ở phần nào và thua ở phần nào?
20. Tấn công quản trị Beanstalk hoàn tất trong một giao dịch. Bản vá đơn giản nhất là gì, và vì sao nó hiệu quả?
21. Video nói *"computer code is always fair"*. Nêu hai lý do câu đó gây hiểu nhầm.
22. Mẫu proxy giải quyết vấn đề gì của tính bất biến, và tạo ra rủi ro mới nào?
23. Trong sáu tầng rủi ro ở §22, tầng nào ít khi hỏng nhất? Vì sao điều đó lại quan trọng với người học xong tám bài lý thuyết?
24. Một giao thức quảng cáo lãi 40%/năm. Ba câu hỏi đầu tiên bạn phải hỏi là gì?
25. Con số "97% token trên Uniswap là rug pull" đúng theo cách đếm nào và gây hiểu nhầm theo cách đếm nào?
26. Ba con số của video ở `29:29` — 58 tỷ, 244 tỷ, 0,05% — mâu thuẫn nhau ở đâu?
27. Video dự đoán Ethereum phải nhanh hơn và rẻ hơn mới giữ được ngôi đầu. Thực tế tới 2026 đã đi hướng nào?
28. Vitalik mô tả gần hết sáu ví dụ này từ **2013**, mà tới 2020 DeFi mới bùng nổ. Bảy năm đó dùng để làm gì?

---

## Tóm tắt một trang

```
 ┌──────────────────────────────────────────────────────────────────────┐
 │  DeFi = ứng dụng tài chính dựng trên blockchain                      │
 │  Mục tiêu: bỏ trung gian bắt buộc phải tin                           │
 └──────────────────────────────────────────────────────────────────────┘

  VÌ SAO CẦN SMART CONTRACT
    Blockchain trần chỉ có một luật: ai cầm khoá thì được chi.
    Không cài thêm điều kiện được -> cần chương trình sống trong chuỗi.

  SÁU VÍ DỤ CỦA VIDEO
    1 Gọi vốn cộng đồng   thay Kickstarter bằng contract giữ tiền
    2 Sàn phi tập trung   (video mô tả mô hình cũ; thực tế là AMM)
    3 Cho vay             thế chấp vượt mức, không thẩm định tín dụng
    4 Tài chính thời gian thực   lương chảy theo giây
    5 NFT                 token độc nhất, theo dõi quyền sở hữu
    6 DAO                 tổ chức bỏ phiếu on-chain, contract tự thi hành

  BỐN CƠ CHẾ PHẢI HIỂU (video không mở ra)
    AMM          x·y=k. Không có bên đối ứng, chỉ có đường cong.
                 Bán 25% kích thước hồ -> trượt giá 20%.
    IL           Giá đi hướng nào cũng lỗ so với giữ nguyên ví.
    Thanh lý     Vay kịch LTV = cách chỗ bị bán đúng 6,25%.
    Flash loan   Vay không thế chấp nhờ tính nguyên tử.
                 -> bẻ oracle giá giao ngay trong 1 giao dịch.

  SÁU TẦNG RỦI RO — tiền mất ở tầng nào
    6 pháp lý  5 quản trị  4 kinh tế  3 oracle  2 hợp đồng  1 chuỗi nền
    ▲ hay hỏng                                          ít hỏng nhất ▲

  BỐN CON SỐ CẦN ĐÍNH CHÍNH
    tweet Dorsey       video: "20 triệu"    thật: 2,9 triệu, bán lại ~vài trăm
    "570tr từ Binance" thật: cầu nối BNB Chain, không phải sàn
    "97% rug pull"     đúng theo SỐ TOKEN, không đúng theo KHỐI LƯỢNG
    "0,05% của cải"    tính từ mốc đỉnh 244 tỷ, đặt cạnh mốc hiện tại 58 tỷ

  CÂU CỦA CẢ KHOÁ HỌC
    "Blockchain rất an toàn — nhưng smart contract dựng trên nó
     là mã do con người viết."     -> mật mã không phải chỗ vỡ
```

---

## Nguồn

- Video gốc: [Introduction to DeFi — Simply Explained](https://www.youtube.com/watch?v=vocM1bRVZmg) (CatholicCryptoConference 2022, 31:38)
- [Ethereum whitepaper](https://ethereum.org/en/whitepaper/) — Vitalik Buterin, 2013; chứa gần hết sáu ví dụ trong video
- [Uniswap docs](https://docs.uniswap.org) — công thức tích không đổi, phí, oracle TWAP
- [Aave docs](https://docs.aave.com) — LTV, ngưỡng thanh lý, mô hình lãi suất, flash loan
- [DefiLlama](https://defillama.com) — TVL theo giao thức và theo chain, có ghi rõ cách đếm
- [rekt.news](https://rekt.news) — nhật ký các vụ mất tiền DeFi, xếp theo quy mô
- [Ethereum roadmap](https://ethereum.org/en/roadmap/) — vì sao sharding bị thay bằng lộ trình lấy rollup làm trung tâm

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](../ly_thuyet/lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](../ly_thuyet/lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](../ly_thuyet/lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](../ly_thuyet/lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. [Bài 6 – Ví Bitcoin](../ly_thuyet/lesson_6_vi_bitcoin.md) — private key → địa chỉ, UTXO, seed phrase
7. [Bài 7 – Độ khó đào](../ly_thuyet/lesson_7_do_kho_dao.md) — target, nBits, retarget, phân bố Poisson
8. [Bài 8 – Zero-Knowledge Proof](../ly_thuyet/lesson_8_zero_knowledge_proof.md) — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. **Bài 10 – DeFi: tài chính phi tập trung** ← *bạn đang ở đây* — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
