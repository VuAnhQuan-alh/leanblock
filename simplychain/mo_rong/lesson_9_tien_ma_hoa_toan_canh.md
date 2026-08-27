# Tiền mã hoá — toàn cảnh (và mặt tối)

> Bài học dựa trên video **"Introduction to Cryptocurrencies"** (kênh *Simply Explained – Savjee*, YouTube `vJfdO9QuroY`) — bài nói tại **CatholicCryptoConference 2022**, dài 35 phút.
> Đây là **bài đầu tiên của phần mở rộng**. Tám bài [lý thuyết](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) đi từ dưới lên: hash, chữ ký, đồng thuận, ví, ZKP. Bài này đi **ngược lại** — từ trên xuống: tiền là gì, người dùng thật đụng vào hệ thống ở đâu, và **nó hỏng ở đâu**.
> Phần **📚 Lý thuyết bổ sung** là kiến thức nền video lướt qua — đọc để hiểu *tại sao*, không chỉ *cái gì*.
>
> ⚠️ **Video là bài nói năm 2022.** Nó được ghi **trước** khi FTX sụp (11/2022) và trước MiCA, trước ETF giao ngay. Phần bổ sung cập nhật tới **2026** — và những gì xảy ra sau đó **chứng minh chính xác điều video cảnh báo**.

---

## Mục lục

1. [Vì sao cần một bài "toàn cảnh" sau 8 bài kỹ thuật](#1-vì-sao-cần-một-bài-toàn-cảnh-sau-8-bài-kỹ-thuật)
2. [Tiền là gì — và tiền mã hoá là loại tiền nào](#2-tiền-là-gì--và-tiền-mã-hoá-là-loại-tiền-nào)
3. [📚 Sáu tính chất của tiền — chấm điểm sòng phẳng](#3--sáu-tính-chất-của-tiền--chấm-điểm-sòng-phẳng)
4. [📚 Tiền pháp định đến từ đâu, và vì sao Bitcoin ra đời năm 2008](#4--tiền-pháp-định-đến-từ-đâu-và-vì-sao-bitcoin-ra-đời-năm-2008)
5. [Blockchain trong 8 phút — bản tóm của video](#5-blockchain-trong-8-phút--bản-tóm-của-video)
6. [📚 Coin và token — thứ bản tóm nào cũng bỏ qua](#6--coin-và-token--thứ-bản-tóm-nào-cũng-bỏ-qua)
7. [Mua ở đâu, và nó nằm ở đâu](#7-mua-ở-đâu-và-nó-nằm-ở-đâu)
8. [📚 Sàn tập trung là một cuốn sổ nợ, không phải blockchain](#8--sàn-tập-trung-là-một-cuốn-sổ-nợ-không-phải-blockchain)
9. [📚 Proof of Reserves — và vì sao nó gần như vô nghĩa](#9--proof-of-reserves--và-vì-sao-nó-gần-như-vô-nghĩa)
10. [Ví và khoá riêng](#10-ví-và-khoá-riêng)
11. [📚 Bốn mô hình lưu ký — bảng quyết định](#11--bốn-mô-hình-lưu-ký--bảng-quyết-định)
12. [📚 Không có nút "quên mật khẩu": sống với tính bất khả đảo](#12--không-có-nút-quên-mật-khẩu-sống-với-tính-bất-khả-đảo)
13. [Chỉ có một blockchain? Vì sao nhiều đồng đến thế](#13-chỉ-có-một-blockchain-vì-sao-nhiều-đồng-đến-thế)
14. [📚 Phân loại: fork, chain mới, token, meme, stablecoin](#14--phân-loại-fork-chain-mới-token-meme-stablecoin)
15. [📚 Stablecoin: ba cơ chế neo giá, và cái đã nổ](#15--stablecoin-ba-cơ-chế-neo-giá-và-cái-đã-nổ)
16. [Nhược điểm — phần thẳng thắn nhất của video](#16-nhược-điểm--phần-thẳng-thắn-nhất-của-video)
17. [📚 Biến động giá: con số, và vì sao nó giết vai trò "đơn vị tính toán"](#17--biến-động-giá-con-số-và-vì-sao-nó-giết-vai-trò-đơn-vị-tính-toán)
18. [📚 Năng lượng: con số thật và hai phía tranh luận](#18--năng-lượng-con-số-thật-và-hai-phía-tranh-luận)
19. [📚 Bảng phân loại 8 kiểu lừa đảo](#19--bảng-phân-loại-8-kiểu-lừa-đảo)
20. [📚 Pháp lý và thuế — trạng thái 2026](#20--pháp-lý-và-thuế--trạng-thái-2026)
21. [📚 Khung quyết định: tôi có nên đụng vào không](#21--khung-quyết-định-tôi-có-nên-đụng-vào-không)
22. [Code minh hoạ](#22-code-minh-hoạ)
23. [Từ điển thuật ngữ](#23-từ-điển-thuật-ngữ)
24. [Câu hỏi tự kiểm tra](#24-câu-hỏi-tự-kiểm-tra)

---

## 1. Vì sao cần một bài "toàn cảnh" sau 8 bài kỹ thuật

Tám bài lý thuyết dựng hệ thống **từ dưới lên**. Bạn biết block nối nhau bằng hash, biết chữ ký chứng minh quyền sở hữu mà không lộ khoá, biết vì sao 51% là con số ma thuật, biết seed phrase 12 từ mã hoá cái gì.

Nhưng có một khoảng trống to:

```
   BẠN ĐÃ BIẾT                       BẠN CHƯA BIẾT
   ───────────                       ─────────────
   Chuỗi hoạt động thế nào     ↔    Tiền là gì, và cái này có phải tiền không
   Khoá riêng ký giao dịch     ↔    99% người dùng KHÔNG giữ khoá riêng của họ
   PoW/PoS bảo vệ đồng thuận   ↔    Chỗ mất tiền nhiều nhất KHÔNG PHẢI đồng thuận
   Có nhiều blockchain         ↔    Vì sao có 20.000 đồng, và bao nhiêu cái là rác
```

Đây là bài nói cho **khán giả không kỹ thuật**. Nó có giá trị riêng vì hai lý do:

1. Nó bắt đầu từ **tiền**, không từ hash. Câu hỏi "cái này có phải tiền không" là câu hỏi đúng và ít người kỹ thuật chịu trả lời.
2. **Một phần ba thời lượng dành cho nhược điểm.** Với một video giới thiệu crypto, đó là tỷ lệ hiếm. Chương `28:31 Downsides` dài gần bằng chương giải thích blockchain.

> 💡 **Luận điểm xuyên suốt bài này:** mật mã trong 8 bài trước gần như chưa bao giờ vỡ. Chỗ vỡ luôn nằm ở **lớp người** dựng quanh nó — sàn giao dịch, cầu nối, lời hứa lợi nhuận, và chính bạn lúc 2 giờ sáng. Đúng kết luận của [Bài 3](../ly_thuyet/lesson_3_smart_contract.md), [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) và [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md), lần này ở quy mô tiền thật.

### Bản đồ video

| Thời điểm | Chương                                                    | Bài này xử lý ở |
| --------- | --------------------------------------------------------- | --------------- |
| 00:00     | Introduction                                              | §1              |
| 01:43     | What is a (crypto)currency?                               | §2, §3, §4      |
| 06:42     | How a blockchain works                                    | §5, §6          |
| 15:26     | How to buy crypto and where is it stored?                 | §7, §8, §9      |
| 17:54     | Wallets and private keys                                  | §10, §11, §12   |
| 23:50     | Is there only 1 blockchain? Why so many cryptocurrencies? | §13, §14, §15   |
| 28:31     | Downsides of cryptocurrencies                             | §16–§20         |
| 34:00     | Outro                                                     | §21             |

---

## 2. Tiền là gì — và tiền mã hoá là loại tiền nào

Trước khi hỏi "Bitcoin có phải tiền không", phải biết tiền **làm gì**. Kinh tế học cổ điển: tiền có **ba chức năng**.

```
        ┌─────────────────────────────────────────────────┐
        │  1. PHƯƠNG TIỆN TRAO ĐỔI                        │
        │     Ai cũng nhận → không cần trùng khớp nhu cầu │
        ├─────────────────────────────────────────────────┤
        │  2. ĐƠN VỊ TÍNH TOÁN                            │
        │     Đo giá trị mọi thứ bằng cùng một thước      │
        ├─────────────────────────────────────────────────┤
        │  3. LƯU TRỮ GIÁ TRỊ                             │
        │     Bán hôm nay, mua ngày mai, vẫn còn giá trị  │
        └─────────────────────────────────────────────────┘
```

Chức năng 1 giải bài toán **trùng khớp nhu cầu kép**: hàng đổi hàng chỉ chạy được khi tôi có thứ bạn cần **và** bạn có thứ tôi cần, **cùng lúc**. Xác suất đó thấp thảm hại. Tiền cắt bài toán làm hai nửa: bán cho ai đó, mua từ người khác.

### Ba loại tiền trong lịch sử

| Loại               | Giá trị đến từ đâu                     | Ví dụ                              |
| ------------------ | -------------------------------------- | ---------------------------------- |
| **Tiền hàng hoá**  | Bản thân vật đó có giá trị dùng được   | Vàng, bạc, muối, gia súc           |
| **Tiền đại diện**  | Giấy đổi được ra hàng hoá đang gửi     | Giấy bạc bản vị vàng (tới 1971)    |
| **Tiền pháp định** | **Không có gì** ngoài luật và niềm tin | USD, EUR, VND — mọi đồng hiện hành |

> Năm 1971, Mỹ chấm dứt việc đổi USD ra vàng. Từ đó, **toàn bộ tiền trên thế giới là tiền pháp định** — giá trị của nó là một thoả thuận xã hội được luật chống lưng, không hơn.

### Tiền mã hoá nằm ở đâu

Nó không thuộc ô nào cả, nên video mô tả nó bằng **thuộc tính**, không bằng chủng loại:

```
 TIỀN PHÁP ĐỊNH                    TIỀN MÃ HOÁ
 ──────────────                    ───────────
 Ngân hàng trung ương phát hành →  Thuật toán phát hành, lịch cố định
 Nguồn cung do chính sách       →  Nguồn cung do CODE (21tr BTC)
 Ngân hàng giữ sổ               →  Mạng ngang hàng giữ sổ (Bài 1)
 Đảo được giao dịch             →  KHÔNG đảo được (Bài 1 §7)
 Cần danh tính để mở tài khoản  →  Cần một cặp khoá (Bài 2, Bài 6)
 Chặn được, đóng băng được      →  Không chặn được ở lớp giao thức
```

Câu trả lời trung thực nhất, và cũng là câu video ngụ ý: **nó làm rất tốt chức năng 1, chấp nhận được chức năng 3 nếu bạn nhìn theo thang 10 năm, và làm rất tệ chức năng 2.** Xem [§17](#17--biến-động-giá-con-số-và-vì-sao-nó-giết-vai-trò-đơn-vị-tính-toán).

---

## 3. 📚 Sáu tính chất của tiền — chấm điểm sòng phẳng

Ba chức năng ở trên là *cái tiền làm được*. Muốn làm được, một vật phải có **sáu tính chất**. Đây là bộ tiêu chí kinh tế học đã dùng từ thế kỷ 19 (Jevons), và nó là cách công bằng nhất để so ba thứ: vàng, USD, Bitcoin.

| Tính chất          | Nghĩa                                |       🥇 Vàng       |          💵 USD          |        ₿ Bitcoin         |
| ------------------ | ------------------------------------ | :----------------: | :---------------------: | :----------------------: |
| **Bền**            | Không hỏng, không mục theo thời gian |         ✅          | ⚠️ giấy rách, số thì bền |        ✅ dữ liệu         |
| **Chia nhỏ được**  | Cắt ra để mua thứ rẻ                 |  ⚠️ khó cắt vật lý  |        ✅ tới xu         |   ✅ tới 10⁻⁸ (satoshi)   |
| **Dễ mang**        | Chuyển giá trị lớn đi xa             | ❌ 1 tấn = 1 xe tải |            ✅            | ✅ 1 tỷ USD = 1 giao dịch |
| **Đồng nhất**      | Đơn vị nào cũng như đơn vị nào       |         ✅          |            ✅            |       ⚠️ *xem dưới*       |
| **Khan hiếm**      | Không ai in thêm tuỳ ý               |    ✅ ~1,5%/năm     |    ❌ in được vô hạn     |     ✅ trần 21 triệu      |
| **Được chấp nhận** | Người khác chịu nhận                 |     ✅ toàn cầu     |     ✅ **cao nhất**      |      ❌ rất hạn chế       |

Đọc bảng này kỹ thì thấy hai điều mà cả phe ủng hộ lẫn phe phản đối đều hay giấu:

**1. Bitcoin thắng ở "khan hiếm" và "dễ mang", thua nặng ở "được chấp nhận".** Đó không phải chi tiết nhỏ — *được chấp nhận* là tính chất **duy nhất không do bản thân vật đó quyết định**. Nó là hiệu ứng mạng. Bạn không thể lập trình ra nó.

**2. "Đồng nhất" là điểm gây tranh cãi nhất.** Về kỹ thuật, 1 BTC = 1 BTC. Nhưng chuỗi **công khai**, nên mỗi đồng mang theo **toàn bộ lý lịch** của nó. Sàn tuân thủ pháp luật có thể từ chối coin từng đi qua một địa chỉ bị cấm vận. Coin "bẩn" và coin "sạch" cùng mệnh giá nhưng **không cùng giá trị thực tế**.

> 💡 Đây chính là chỗ [Bài 8 – ZKP](../ly_thuyet/lesson_8_zero_knowledge_proof.md) trở thành vấn đề **kinh tế**, không chỉ vấn đề riêng tư. Một hệ có tính riêng tư thật (Zcash, Monero) thì đồng nhất hoàn hảo — và chính vì thế mà bị nhiều sàn gỡ niêm yết. **Tính đồng nhất và tính tuân thủ kéo nhau ngược chiều.** Không có lời giải kỹ thuật cho mâu thuẫn này; nó là một lựa chọn chính trị.

### Khan hiếm không phải lúc nào cũng tốt

Phe kinh tế học chính thống phản đối nguồn cung cố định bằng một lập luận cụ thể: nếu tiền **tăng giá** theo thời gian, người ta **trì hoãn tiêu dùng** — thứ gì hôm nay giá 10 đồng, năm sau chỉ còn 8 đồng thì tội gì mua bây giờ. Nhu cầu giảm → sản xuất giảm → giảm phát xoáy trôn ốc.

Phe Bitcoin phản bác: người ta vẫn mua điện thoại dù biết năm sau rẻ hơn và tốt hơn.

Không có bên nào chứng minh được, vì **chưa từng có nền kinh tế lớn nào chạy trên tiền có nguồn cung cố định tuyệt đối**. Đây là câu hỏi thực nghiệm chưa có dữ liệu. Ai nói chắc chắn thì người đó đang bán cái gì đó.

---

## 4. 📚 Tiền pháp định đến từ đâu, và vì sao Bitcoin ra đời năm 2008

Video chỉ nói lướt rằng ngân hàng trung ương có thể in thêm tiền. Cơ chế thật đáng biết, vì nó là **lý do tồn tại** của Bitcoin.

### Phần lớn tiền không do ngân hàng trung ương in

Ngân hàng trung ương phát hành **tiền cơ sở** (tiền mặt + dự trữ). Nhưng phần lớn tiền trong nền kinh tế do **ngân hàng thương mại tạo ra khi cho vay**:

```
Bạn gửi 1.000    ──▶  Ngân hàng giữ lại  100  (dự trữ 10%)
                      Ngân hàng cho vay   900  ──▶  người vay gửi vào NH khác
                                                     ──▶ NH đó giữ 90, cho vay 810
                                                          ──▶ ... lặp lại

Tiền cơ sở ban đầu:  1.000
Tổng "tiền gửi" trong hệ thống:  1.000 + 900 + 810 + ... ≈ 10.000
```

Đây là **dự trữ một phần** (fractional reserve). Nó có nghĩa là: **tiền trong tài khoản của bạn phần lớn không tồn tại dưới dạng vật chất ở đâu cả.** Nó là một khoản **nợ** ngân hàng ghi cho bạn.

Hệ thống này ổn định chừng nào **không phải ai cũng đòi rút cùng lúc**. Khi điều đó xảy ra, gọi là **bank run**, và ngân hàng **luôn** sập — không phải vì gian lận, mà vì đó là toán học. [Demo 2 ở §22](#22-code-minh-hoạ) cho chạy đúng phép toán ấy.

> ⚠️ **Nhớ kỹ đoạn này.** Sàn giao dịch crypto cũng chạy đúng mô hình này, nhưng **không có bảo hiểm tiền gửi, không có người cho vay cuối cùng, không có cơ quan giám sát**. §8 và §9 nói tiếp.

### Vì sao là năm 2008

Whitepaper Bitcoin công bố tháng 10/2008 — giữa khủng hoảng tài chính toàn cầu. Block đầu tiên (**genesis block**, 03/01/2009) nhúng vào phần dữ liệu tuỳ ý một dòng chữ: tiêu đề trang nhất tờ *The Times* ngày hôm đó, về việc chính phủ Anh chuẩn bị gói cứu trợ thứ hai cho các ngân hàng.

Đó vừa là **dấu thời gian** (chứng minh chuỗi không được đào trước ngày đó), vừa là **tuyên ngôn**. Satoshi nói rõ Bitcoin sinh ra để trả lời một câu hỏi cụ thể:

> **Làm sao có một hệ thống tiền tệ không cần tin vào bất kỳ tổ chức nào?**

Toàn bộ 8 bài lý thuyết là **câu trả lời kỹ thuật** cho câu hỏi đó. Toàn bộ phần còn lại của bài này là **kiểm chứng thực tế** xem câu trả lời ấy giữ được đến đâu.

---

## 5. Blockchain trong 8 phút — bản tóm của video

Chương `06:42` gói toàn bộ [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) vào 8 phút. Bạn đã học kỹ rồi, nên phần này chỉ là **đối chiếu**: cái gì bản tóm giữ, cái gì nó bỏ.

```
     GIAO DỊCH            KHỐI                    CHUỖI
     ─────────            ────                    ─────
   An ─20→ Bình      ┌──────────────┐      ┌────┐ ┌────┐ ┌────┐
   Chi ─5→ Dũng  ──▶ │ #124         │  ──▶ │#123│◀│#124│◀│#125│
   Em ─1→ Phúc       │ prev: 0000a3 │      └────┘ └────┘ └────┘
                     │ nonce: 88213 │        ▲ đổi 1 bit ở đây
                     │ hash: 0000f7 │        └─ mọi hash phía sau vỡ
                     └──────────────┘

   Ai giữ sổ? ──▶ HÀNG NGHÌN MÁY, mỗi máy một bản đầy đủ
   Ai được ghi? ─▶ Ai giải xong bài toán PoW (Bài 1 §5, Bài 7)
   Ai ký? ───────▶ Chủ khoá riêng, không ai khác (Bài 2, Bài 6)
```

| Bản tóm 8 phút nói        | Chỗ học đầy đủ                                                                                              | Điều nó **bỏ qua**                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Hash nối khối thành chuỗi | [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) §2–4                                             | Merkle tree, cấu trúc header                 |
| Thợ đào dò nonce          | [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) §5, [Bài 7](../ly_thuyet/lesson_7_do_kho_dao.md) | target/nBits, retarget 2016 block            |
| Mạng ngang hàng đồng bộ   | [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) §6                                               | Fork tạm, chọn chuỗi nặng nhất, block mồ côi |
| Chữ ký chứng minh sở hữu  | [Bài 2](../ly_thuyet/lesson_2_ma_hoa_bat_doi_xung.md), [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md)         | ECDSA, nonce, UTXO                           |
| Sửa lịch sử là bất khả    | [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) §7                                               | 51% **không** phải bất khả — chỉ là đắt      |

> ⚠️ **Một điểm bản tóm nào cũng nói sai theo cùng một kiểu.** "Blockchain không thể bị sửa" là **sai**. Đúng phải là: *sửa được, nhưng phải đào lại toàn bộ công việc từ điểm sửa trở đi, nhanh hơn cả mạng còn lại cộng lại.* Với Bitcoin thì đắt tới mức vô lý. Với một chain nhỏ hashrate thấp thì **rẻ, và đã xảy ra nhiều lần** — Ethereum Classic bị tổ chức lại chuỗi năm 2019 và 2020, Bitcoin Gold năm 2018 và 2020. [Bài 1 §7](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) và [Bài 5](../ly_thuyet/lesson_5_proof_of_stake.md) nói chi tiết. "Bất biến" là **tính chất kinh tế**, không phải tính chất toán học.

---

## 6. 📚 Coin và token — thứ bản tóm nào cũng bỏ qua

Chỗ này gây nhầm nhiều nhất cho người mới, và video không tách bạch.

```
   COIN (đồng bản địa)                    TOKEN (phát hành trên chain khác)
   ───────────────────                    ────────────────────────────────
   BTC trên Bitcoin                       USDT, USDC, UNI, hàng chục nghìn cái
   ETH trên Ethereum                      chạy trên Ethereum / Solana / Tron...
   SOL trên Solana
                                          ⚠️ Token KHÔNG có blockchain riêng.
   ▸ Có chuỗi riêng                       Nó chỉ là một dòng trong một
   ▸ Trả phí giao dịch bằng nó            SMART CONTRACT (Bài 3).
   ▸ Thợ đào/validator được trả bằng nó
                                          ▸ Muốn chuyển token vẫn phải có
   ▸ Bảo mật = bảo mật của chain đó          COIN của chain đó để trả gas
                                          ▸ Bảo mật = bảo mật của contract
```

Hệ quả thực tế mà người mới hay vấp:

1. **Bạn có 1000 USDT trên ví Ethereum nhưng không có ETH → bạn không chuyển đi được.** Phí gas phải trả bằng ETH. Tiền của bạn bị kẹt cho tới khi ai đó gửi ETH vào.
2. **Cùng một tên token tồn tại trên nhiều chain và chúng KHÔNG phải một thứ.** USDT trên Ethereum ≠ USDT trên Tron. Gửi nhầm mạng → mất tiền, và đây là kiểu mất tiền phổ biến nhất với người mới.
3. **Tạo một token mất 5 phút và vài đô.** Đây là lý do có hàng chục nghìn token. Việc một thứ "có trên blockchain" không nói gì về giá trị của nó — [Bài 3](../ly_thuyet/lesson_3_smart_contract.md) và [Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md) đã dựng khung để đánh giá.

> 💡 Chuẩn token phổ biến: **ERC-20** (token thay thế được — tiền), **ERC-721/1155** (NFT — mỗi cái một khác). Cả hai chỉ là **giao diện quy ước**: một smart contract có các hàm tên `transfer`, `balanceOf`... Không có gì thần bí. Bạn có thể tự viết một cái sau khi đọc [Bài 3](../ly_thuyet/lesson_3_smart_contract.md).

---

## 7. Mua ở đâu, và nó nằm ở đâu

Chương `15:26` đặt câu hỏi mà mọi người mới đều hỏi và ít ai trả lời đúng.

### Ba đường mua

| Đường                       | Cách chạy                                          | Đánh đổi                                  |
| --------------------------- | -------------------------------------------------- | ----------------------------------------- |
| **Sàn tập trung (CEX)**     | Nạp tiền pháp định, mua, sàn ghi vào sổ **nội bộ** | Dễ nhất. **Bạn không giữ coin.**          |
| **Sàn phi tập trung (DEX)** | Ví của bạn nói chuyện thẳng với smart contract     | Bạn giữ khoá. Phải đã có coin để trả gas. |
| **P2P / máy ATM crypto**    | Giao dịch với cá nhân, hoặc máy                    | Phí cao, rủi ro lừa đảo cao               |

### Và đây là chỗ hầu hết người dùng hiểu sai

> **Khi bạn "mua Bitcoin" trên một sàn tập trung, thường KHÔNG có giao dịch nào lên blockchain cả.**

Sàn chỉ sửa một con số trong cơ sở dữ liệu của nó:

```
   TRÊN SÀN (sổ nội bộ)                    TRÊN BLOCKCHAIN
   ────────────────────                    ───────────────
   An mua 0,5 BTC  ──▶ UPDATE users        (không có gì xảy ra)
                       SET btc = btc + 0.5
                       WHERE id = 'an'

   An gửi 0,5 BTC cho Bình (cùng sàn)      (không có gì xảy ra)
        ──▶ hai dòng UPDATE

   An RÚT 0,5 BTC ra ví riêng          ──▶ ✅ MỘT giao dịch thật,
                                            có chữ ký, có phí, có xác nhận
```

Nghĩa là: cho tới lúc bạn bấm **rút**, thứ bạn sở hữu **không phải Bitcoin**. Đó là **một lời hứa sẽ trả Bitcoin**, do một công ty phát hành. Một tờ giấy nợ — bản chất giống hệt cái mà bản vị vàng đã có, và chính là thứ Bitcoin sinh ra để thay thế.

> 💥 Đây là **nghịch lý trung tâm** của bài này: một hệ thống được thiết kế để không cần tin ai, trên thực tế lại được đa số người dùng tiếp cận thông qua **những trung gian phải tin tuyệt đối** — và những trung gian đó còn ít chịu giám sát hơn cả ngân hàng.

---

## 8. 📚 Sàn tập trung là một cuốn sổ nợ, không phải blockchain

Đặt mô hình sàn cạnh mô hình ngân hàng ở [§4](#4--tiền-pháp-định-đến-từ-đâu-và-vì-sao-bitcoin-ra-đời-năm-2008):

|                                  | Ngân hàng                 | Sàn crypto                        |
| -------------------------------- | ------------------------- | --------------------------------- |
| Giữ hết tiền khách?              | Không (dự trữ một phần)   | **Thường là không**               |
| Bảo hiểm tiền gửi                | Có (nhiều nước)           | **Không**                         |
| Người cho vay cuối cùng          | Ngân hàng trung ương      | **Không có**                      |
| Giám sát vốn, kiểm toán bắt buộc | Có                        | **Rất ít, tuỳ nước**              |
| Tách bạch tài sản khách hàng     | Bắt buộc theo luật        | **Nhiều nơi không**               |
| Khi sập, khách được gì           | Được bảo hiểm tới hạn mức | **Xếp hàng chủ nợ không bảo đảm** |

Cái ô cuối cùng là ô tàn nhẫn nhất và ít người biết nhất. Trong nhiều vụ phá sản, coin gửi trên sàn được toà xử là **tài sản của sàn**, không phải của bạn. Bạn trở thành chủ nợ không có bảo đảm — đứng gần cuối hàng.

### Mẫu chung của mọi vụ sập

Nhìn danh sách này, để ý nó **lặp lại cùng một kịch bản**:

| Năm  | Vụ             | Quy mô              | Nguyên nhân gốc                                                               |
| ---- | -------------- | ------------------- | ----------------------------------------------------------------------------- |
| 2014 | **Mt.Gox**     | ~850.000 BTC        | Bị rút ruột nhiều năm, sổ sách không khớp                                     |
| 2019 | **QuadrigaCX** | ~190 triệu CAD      | Nhà sáng lập chết, **không ai khác biết khoá riêng**                          |
| 2022 | **Celsius**    | ~4,7 tỷ USD         | Hứa lợi nhuận cao, đem tiền khách đi đầu tư                                   |
| 2022 | **Terra/Luna** | ~40 tỷ USD          | Stablecoin thuật toán ([§15](#15--stablecoin-ba-cơ-chế-neo-giá-và-cái-đã-nổ)) |
| 2022 | **FTX**        | ~8 tỷ USD thiếu hụt | Dùng tiền khách cho công ty liên quan                                         |

```
   MẪU CHUNG (đúng cho cả 5 vụ):

   1. Sàn/nền tảng giữ tài sản khách
   2. Đem đi dùng vào việc khác (cho vay, đầu tư, bù lỗ)   ← điểm chết
   3. Chạy êm nhiều năm, ai cũng nghĩ nó an toàn
   4. Một cú sốc → nhiều người đòi rút cùng lúc
   5. TẠM DỪNG RÚT TIỀN                                     ← luôn là dấu hiệu này
   6. Phá sản. Khách xếp hàng chủ nợ.

   ⚠️ KHÔNG CÓ VỤ NÀO trong số này là do phá vỡ mật mã.
      Mật mã chưa từng thua. Cái thua là mô hình LƯU KÝ.
```

> 💡 **"Tạm dừng rút tiền" là tín hiệu sớm gần như hoàn hảo.** Một nơi thật sự giữ đủ tài sản khách thì rút bao nhiêu cũng trả được — nó không cần dừng. Hễ thấy dòng chữ đó, cửa sổ để thoát đã đóng.

---

## 9. 📚 Proof of Reserves — và vì sao nó gần như vô nghĩa

Sau FTX (11/2022), các sàn đua nhau công bố **Proof of Reserves** (PoR). Nghe rất thuyết phục, và **phần lớn là diễn**. Đáng phân tích vì nó là bài học đẹp về việc **một bằng chứng mật mã đúng vẫn có thể chẳng chứng minh điều gì**.

PoR chuẩn có hai nửa:

```
   NỬA 1 — TÀI SẢN (dễ, sàn nào cũng làm)
   Sàn ký một thông điệp bằng khoá riêng của các địa chỉ nó nắm
      → "tôi kiểm soát 100.000 BTC ở các địa chỉ này"

   NỬA 2 — NỢ (khó, ít sàn làm tử tế)
   Sàn xây CÂY MERKLE (Bài 1) từ số dư mọi khách hàng, công bố ROOT
      → mỗi khách tự kiểm tra số dư của mình có trong cây không
```

Nghe kín kẽ. Bốn lỗ hổng, xếp theo mức nghiêm trọng:

| Lỗ hổng                        | Vì sao chí mạng                                                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bỏ sót khách hàng**          | Sàn **xoá vài tài khoản lớn** khỏi cây → nợ công bố giảm, mà **mọi khách còn lại vẫn verify OK**. Không ai phát hiện được, trừ chính người bị xoá.                |
| **Vay mượn đúng lúc chụp ảnh** | PoR là **một tấm ảnh tại một thời điểm**. Vay coin ngày hôm đó, ký, trả lại hôm sau. Đã có sàn làm đúng thế.                                                      |
| **Số dư âm**                   | Nếu sàn được phép nhét lá có số dư âm vào cây, tổng nợ tụt xuống. Cần một ZKP về khoảng giá trị ([Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md)) để chặn. |
| **Không tính nợ ngoài chuỗi**  | Sàn nợ ngân hàng, nợ trái chủ, đang bị kiện — PoR **không thấy** những khoản đó.                                                                                  |

Kết luận sắc gọn:

> **Proof of Reserves không có Proof of Liabilities thì vô nghĩa. Và cả hai cộng lại vẫn không bằng một cuộc kiểm toán thật.**

[Demo 1 ở §22](#22-code-minh-hoạ) cài đúng cây Merkle này, cho khách verify thành công, rồi **xoá một khách giấu 40 BTC nợ** — và chứng minh bằng `assert` rằng mọi khách còn lại **vẫn verify OK**. Bạn thấy tận mắt một bằng chứng mật mã hoàn toàn hợp lệ đang che một lỗ thủng.

> 💡 Cách làm đúng đã có: chứng minh **tổng nợ** bằng zk-SNARK, kèm range proof để chặn số dư âm ([Bài 8 §12](../ly_thuyet/lesson_8_zero_knowledge_proof.md)). Vài sàn đã triển khai. Nó tốt hơn hẳn — nhưng vẫn không giải quyết được lỗ "vay mượn đúng lúc chụp ảnh", vì lỗ đó nằm ở **thời gian**, không nằm ở mật mã.

---

## 10. Ví và khoá riêng

Chương `17:54` là chương quan trọng nhất của video với người dùng thật. Nó nói đúng một câu, và câu đó đáng cả 35 phút:

> ### **Not your keys, not your coins.**
> **Không phải khoá của bạn, thì không phải coin của bạn.**

### "Ví" là cái tên sai

Đây là hiểu nhầm nền tảng, [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) đã dựng đầy đủ, nhắc lại vì nó quyết định mọi thứ phía sau:

```
   ❌ SAI: ví chứa coin của bạn

   ✅ ĐÚNG:  Coin nằm TRÊN CHUỖI, ở mọi node, luôn luôn.
             Ví chỉ chứa KHOÁ RIÊNG — thứ cho phép ký lệnh chuyển chúng.

   khoá riêng ──(nhân điểm)──▶ khoá công ──(băm)──▶ ĐỊA CHỈ
      256 bit                                        thứ bạn đưa người khác

   ⚠️ Mũi tên chỉ đi MỘT CHIỀU. Mất khoá riêng = mất vĩnh viễn.
      Không có ai để gọi. Không có nút khôi phục. Không có ngoại lệ.
```

Mất ví ≠ mất coin. Coin vẫn nằm y nguyên trên chuỗi, ai cũng nhìn thấy nó, **mãi mãi**, và không ai mở được nữa. Ước tính có **hàng triệu BTC** đang ở trạng thái đó.

### Seed phrase

12 hoặc 24 từ tiếng Anh. Chúng **không phải mật khẩu** — chúng là **chính khoá riêng của bạn, viết dưới dạng đọc được** ([Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) giải thích BIP-39 và checksum).

```
   Ai đọc được 12 từ này = người đó SỞ HỮU toàn bộ số coin. Ngay lập tức.
   Không cần thiết bị của bạn. Không cần mật khẩu của bạn. Không dấu vết.

   ⛔ KHÔNG chụp ảnh          ⛔ KHÔNG lưu Google Drive / iCloud / email
   ⛔ KHÔNG gõ vào máy tính   ⛔ KHÔNG đọc cho ai, kể cả "nhân viên hỗ trợ"
   ✅ Viết tay lên giấy, hoặc dập lên tấm kim loại
   ✅ Cất ≥2 bản ở ≥2 nơi vật lý khác nhau
```

> ⚠️ **Không tồn tại một tình huống hợp lệ nào mà người khác cần seed phrase của bạn.** Không có ngoại lệ. Hễ ai hỏi — hỗ trợ khách hàng, sàn, "đội kỹ thuật ví", bạn trên Telegram — thì đó là **lừa đảo, 100%**. Đây là câu duy nhất trong bài này không có chữ "thường" hay "hầu hết".

---

## 11. 📚 Bốn mô hình lưu ký — bảng quyết định

Video chia hai ("sàn giữ" vs "bạn giữ"). Thực tế có bốn nấc, và chọn sai nấc là cách mất tiền phổ biến nhất.

| Mô hình                                  | Ai giữ khoá                              | Rủi ro chính                                                    | Hợp với                                        |
| ---------------------------------------- | ---------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| **Sàn (custodial)**                      | Sàn                                      | Sàn sập, bị đóng băng, bị hack                                  | Đang giao dịch chủ động, số tiền chấp nhận mất |
| **Ví nóng** (app điện thoại/trình duyệt) | Bạn, trên máy nối mạng                   | Malware, ví giả, lừa ký nhầm                                    | Chi tiêu hằng ngày, số nhỏ                     |
| **Ví lạnh** (thiết bị phần cứng)         | Bạn, khoá **không bao giờ** rời thiết bị | Mất/hỏng thiết bị (còn seed thì khôi phục được), lừa đảo vật lý | Tiết kiệm dài hạn                              |
| **Đa chữ ký** (2-of-3, 3-of-5)           | Chia cho nhiều khoá/nhiều nơi            | Phức tạp, dễ tự khoá mình ra ngoài                              | Số tiền lớn, quỹ chung, kế thừa                |

Quy tắc gọn, mượn từ tiền mặt:

```
   VÍ NÓNG  = cái ví trong túi quần   → để đủ tiêu, mất thì tiếc chứ không chết
   VÍ LẠNH  = két sắt ở nhà           → phần lớn tài sản
   ĐA CHỮ KÝ = két ngân hàng cần 2 chìa → tài sản lớn, cần chống cả TRỘM lẫn chính mình
   SÀN      = tiền đưa người khác giữ  → chỉ để lúc đang thật sự cần dùng nó
```

> 💡 **Ví lạnh không chống lừa đảo.** Thiết bị bảo vệ khoá khỏi malware — nó **không** bảo vệ bạn khỏi việc tự tay bấm "xác nhận" trên một giao dịch độc hại. Kiểu mất tiền phổ biến nhất với người dùng ví lạnh là **ký một `approve` cho phép contract lạ rút sạch token**, chứ không phải bị trích xuất khoá. Đây đúng là lỗ hổng **lớp người** mà [Bài 3](../ly_thuyet/lesson_3_smart_contract.md) đã cảnh báo. Thiết bị làm đúng việc của nó; con người mới là chỗ vỡ.

---

## 12. 📚 Không có nút "quên mật khẩu": sống với tính bất khả đảo

[Bài 1 §7](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) trình bày tính bất khả đảo như một **tính năng**. Với người dùng, nó đồng thời là **rủi ro vận hành lớn nhất**, và không ai chuẩn bị cho nó.

| Chuyện xảy ra                        | Ngân hàng                          | Blockchain                              |
| ------------------------------------ | ---------------------------------- | --------------------------------------- |
| Quên mật khẩu                        | Đặt lại qua email                  | **Mất sạch**                            |
| Gõ nhầm số tài khoản                 | Gọi ngân hàng, thường lấy lại được | **Mất sạch**                            |
| Gửi nhầm mạng (USDT sang chain khác) | —                                  | **Thường mất sạch**                     |
| Bị lừa chuyển tiền                   | Có cơ hội đảo, có điều tra         | **Không đảo được**                      |
| Chủ tài khoản qua đời                | Thủ tục thừa kế                    | **Không ai vào được nếu không có seed** |

Ba biện pháp thật sự đáng làm, xếp theo tỷ lệ lợi ích/công sức:

**1. Gửi thử số nhỏ trước.** Địa chỉ mới, mạng mới, sàn mới → gửi một khoản bé, xác nhận đến nơi, rồi mới gửi phần còn lại. Mất vài phút và một khoản phí. Cứu được toàn bộ số tiền. Bitcoin có **checksum trong địa chỉ** nên gõ sai một ký tự thường bị ví chặn — nhưng checksum không cứu bạn khỏi một địa chỉ **hợp lệ nhưng sai người**.

**2. Kiểm tra sao chép — malware tráo clipboard là có thật.** Một họ mã độc phổ biến ngồi im, phát hiện bạn copy địa chỉ ví, và **thay bằng địa chỉ của kẻ tấn công** — trông na ná vì cùng độ dài. Luôn đối chiếu **4 ký tự đầu và 4 ký tự cuối** trên màn hình xác nhận, tốt nhất là trên màn hình của **ví lạnh**, vì màn hình máy tính có thể đang nói dối.

**3. Kế hoạch thừa kế — bài toán không ai làm.** Nếu bạn chết hôm nay, người nhà có vào được không? Nếu **có** thì hôm nay bảo mật của bạn đang yếu. Nếu **không** thì tiền biến mất cùng bạn. Vụ QuadrigaCX ([§8](#8--sàn-tập-trung-là-một-cuốn-sổ-nợ-không-phải-blockchain)) là bản phóng đại của chính bài toán này ở quy mô công ty.

```
   Lời giải chuẩn: ĐA CHỮ KÝ 2-of-3
      khoá 1: bạn giữ
      khoá 2: két/luật sư/người thân
      khoá 3: nơi lưu trữ độc lập

   Sống  → bạn dùng khoá 1 + khoá 3, chạy bình thường
   Chết  → người thừa kế dùng khoá 2 + khoá 3
   Trộm lấy 1 khoá → KHÔNG lấy được gì
```

> 💡 Chú ý cấu trúc: đây **đúng là ngưỡng t-of-n** bạn đã gặp ở đồng thuận ([Bài 5](../ly_thuyet/lesson_5_proof_of_stake.md)) và ở chia sẻ bí mật. Cùng một ý tưởng — **không để bất kỳ điểm đơn lẻ nào quyết định** — áp lên tủ đựng tiền của một người.

---

## 13. Chỉ có một blockchain? Vì sao nhiều đồng đến thế

Chương `23:50`. Câu trả lời ngắn: **không**, và số lượng thì phi lý.

```
   2009  ▏ 1 đồng
   2013  ▎ ~50
   2017  ██ ~1.500        ← bong bóng ICO
   2021  ████ ~10.000
   2026  ███████████ >20.000 đồng đang niêm yết ở đâu đó

   Trong đó, số chain có bảo mật + hệ sinh thái + người dùng thật:
   ▏ khoảng vài chục.
```

### Bốn lý do có nhiều đến thế, xếp theo mức chính đáng

| Lý do                               | Chính đáng? | Ví dụ                                                          |
| ----------------------------------- | ----------- | -------------------------------------------------------------- |
| **Đánh đổi kỹ thuật khác nhau**     | ✅ Có        | Bitcoin chọn bảo mật; Solana chọn tốc độ; Monero chọn riêng tư |
| **Bất đồng trong cộng đồng → fork** | ✅ Có        | Bitcoin Cash tách khỏi Bitcoin vì tranh cãi kích thước block   |
| **Thử nghiệm thật**                 | ✅ Có        | Chain mới thử mô hình đồng thuận, mô hình phí, ZK              |
| **Kiếm tiền từ người mới**          | ❌ Không     | Phần lớn 20.000 cái. Tạo token mất vài phút.                   |

### Tam giác bất khả — cái khung giải thích tất cả

Đây là lý do **kỹ thuật** khiến không thể chỉ có một chain:

```
                    PHI TẬP TRUNG
                   (ai cũng chạy node được)
                        /\
                       /  \
                      /    \    Chọn được 2,
                     /      \   nhượng bộ cái thứ 3
                    /________\
             BẢO MẬT          MỞ RỘNG
        (tấn công cực đắt)   (nhiều giao dịch/giây)

   Bitcoin  : phi tập trung + bảo mật   → ~7 giao dịch/giây
   Solana   : bảo mật + mở rộng          → node cần phần cứng đắt
   Sidechain: phi tập trung + mở rộng    → bảo mật thấp hơn chain chính
```

Không ai "giải" được tam giác này. Cái mà lớp 2 (Lightning, rollup) làm là **dời điểm đánh đổi sang một tầng khác** — giao dịch chạy ngoài chuỗi chính, chỉ neo kết quả xuống. Chain nền vẫn giữ nguyên tính chất của nó. Nếu bạn đã đọc [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md), zkRollup chính là hình thái tinh vi nhất của thủ thuật này.

---

## 14. 📚 Phân loại: fork, chain mới, token, meme, stablecoin

"Đồng coin mới" là bốn thứ hoàn toàn khác nhau bị gọi chung một tên. Phân biệt được là bước đầu để không bị lừa.

| Loại           | Cách sinh ra                               | Kế thừa bảo mật?                                                                 | Ví dụ                          |
| -------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------ |
| **Hard fork**  | Tách khỏi chuỗi cũ tại một block, luật mới | Chép lịch sử, **KHÔNG chép hashrate**                                            | Bitcoin Cash, Ethereum Classic |
| **Chain mới**  | Viết từ đầu, genesis riêng                 | Không, phải tự gây dựng                                                          | Solana, Avalanche, Cardano     |
| **Token**      | Một smart contract trên chain có sẵn       | Kế thừa **chain**, nhưng không kế thừa contract                                  | USDC, UNI, ~90% số coin        |
| **Meme coin**  | Thường là token, giá trị = sự chú ý        | —                                                                                | *(đa số về 0)*                 |
| **Stablecoin** | Token neo giá vào tài sản khác             | Phụ thuộc **cơ chế neo** ([§15](#15--stablecoin-ba-cơ-chế-neo-giá-và-cái-đã-nổ)) | USDT, USDC, DAI                |

### Ô nguy hiểm nhất: "chép lịch sử, không chép hashrate"

Khi một chain fork ra, nó thừa hưởng toàn bộ số dư — nhưng **không** thừa hưởng thợ đào. Bảo mật của nó tụt xuống bằng phần hashrate thật sự đi theo nó, có thể chỉ vài phần trăm.

```
   Bitcoin      : hashrate 100%  → tấn công 51% ≈ bất khả về kinh tế
   Fork nhỏ     : hashrate   1%  → thuê đủ máy trong VÀI GIỜ, giá vài chục nghìn đô

   ⚠️ Người dùng nhìn thấy "cùng lịch sử, cùng số dư, giao diện y hệt"
      và tưởng nó cùng mức an toàn. Không hề. Bài 1 §7 giải thích vì sao.
```

Chuyện này **đã xảy ra nhiều lần**: Bitcoin Gold (2018, 2020) và Ethereum Classic (2019, 2020) đều bị tổ chức lại chuỗi và chi tiêu hai lần. Không có gì bị phá về mật mã cả — chỉ là **thuê hashrate rẻ hơn số tiền lấy được**. Đúng công thức kinh tế trong [Bài 1 §7](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md).

### Bộ lọc 5 câu hỏi cho một đồng bất kỳ

Trước khi tin bất cứ đồng nào, hỏi năm câu. Đa số rụng ở câu 1 hoặc 2:

1. **Nó giải bài toán gì mà chain có sẵn không giải được?** (Đây là [khung quyết định của Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md), áp cho coin.)
2. **Ai đang giữ nguồn cung?** Đội ngũ giữ 60% thì đó không phải hệ phi tập trung, đó là một công ty có token.
3. **Bảo mật đến từ đâu?** Hashrate/stake thật là bao nhiêu? Tấn công tốn bao nhiêu?
4. **Ai vá được nó?** Có khoá quản trị nào đổi luật được không? ([Bài 3](../ly_thuyet/lesson_3_smart_contract.md))
5. **Lợi nhuận hứa hẹn đến từ đâu?** Nếu không trả lời được bằng một câu, thì nguồn tiền là **người vào sau** ([§19](#19--bảng-phân-loại-8-kiểu-lừa-đảo)).

---

## 15. 📚 Stablecoin: ba cơ chế neo giá, và cái đã nổ

Stablecoin là mảnh ghép mà [§2](#2-tiền-là-gì--và-tiền-mã-hoá-là-loại-tiền-nào) đòi hỏi: một thứ **giữ được vai trò đơn vị tính toán**. Nó cũng là nơi tiền thật nằm nhiều nhất. Có ba cách neo giá, và độ an toàn **khác nhau một trời một vực**.

| Cơ chế                             | Cách chạy                                     | Rủi ro                                               | Ví dụ           |
| ---------------------------------- | --------------------------------------------- | ---------------------------------------------------- | --------------- |
| **Bảo chứng bằng tiền pháp định**  | Mỗi 1 token = 1 USD gửi ở ngân hàng           | Tin vào tổ chức phát hành; ngân hàng đó có sập không | USDC, USDT      |
| **Bảo chứng vượt mức bằng crypto** | Khoá 150 USD ETH để đúc 100 USD               | Giá sập nhanh → thanh lý dây chuyền                  | DAI             |
| **Thuật toán**                     | Không bảo chứng. Đúc/đốt token phụ để giữ giá | **Vòng xoáy tử thần**                                | UST *(đã chết)* |

### Cái đã nổ: UST/LUNA, tháng 5/2022

Luật rất gọn: **đốt 1 UST luôn được đúc lượng LUNA trị giá đúng 1 USD**, và ngược lại. Khi UST rớt xuống 0,98 USD, người kinh doanh chênh lệch mua UST giá rẻ, đổi lấy 1 USD LUNA, ăn 2 xu. Sức mua đó đẩy giá UST về 1 USD.

Cơ chế này chạy hoàn hảo — **chừng nào vốn hoá LUNA còn lớn hơn lượng UST lưu hành**. Khi niềm tin gãy:

```
   UST rớt neo
        │
        ▼
   Người ta đốt UST để lấy LUNA        ← đúng như luật cho phép
        │
        ▼
   LUNA MỚI được đúc ra, bán ngay
        │
        ▼
   Giá LUNA giảm
        │
        ▼
   Cùng lượng UST giờ đúc ra NHIỀU LUNA HƠN  ← vì đúc theo giá hiện tại
        │
        ▼
   Bán nhiều hơn nữa → giá giảm sâu hơn nữa
        │
        └──────────▶ QUAY LẠI BƯỚC 3, mỗi vòng một tệ hơn

   Kết quả trong ~3 ngày: ~40 tỷ USD bốc hơi.
   Cung LUNA phình khoảng 18 TRIỆU lần. Giá về gần 0.
```

**Điểm chết nằm ngay trong thiết kế:** tài sản dùng để bảo chứng (LUNA) **chính là tài sản mà đám đông đang bán tháo**. Đây là một vòng phản hồi dương — hệ càng cần LUNA đắt thì LUNA càng rẻ. Không có tham số nào chỉnh được nó; sai từ kiến trúc.

[Demo 3 ở §22](#22-code-minh-hoạ) cho chạy đúng vòng lặp này bằng số và `assert` rằng nó phải kết thúc trong sụp đổ.

> ⚠️ Ngay cả stablecoin bảo chứng bằng tiền thật cũng **không phải không rủi ro**. Tháng 3/2023, USDC rớt xuống ~0,87 USD vì một phần dự trữ nằm ở Silicon Valley Bank lúc ngân hàng đó sập. Nó hồi lại khi tiền được bảo đảm. Bài học: **stablecoin bảo chứng bằng fiat kế thừa nguyên vẹn rủi ro của hệ thống ngân hàng** — đúng cái hệ thống mà [§4](#4--tiền-pháp-định-đến-từ-đâu-và-vì-sao-bitcoin-ra-đời-năm-2008) nói Bitcoin sinh ra để tránh.

---

## 16. Nhược điểm — phần thẳng thắn nhất của video

Chương `28:31` chiếm gần một phần sáu thời lượng. Bảng dưới là danh sách của video, cộng thêm mức độ "đã cải thiện tới 2026 chưa".

| Nhược điểm           | Video (2022) nói                   | Tới 2026                                                                                                      |
| -------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Biến động giá**    | Không dùng làm tiền hằng ngày được | ⏸️ Gần như không đổi. [§17](#17--biến-động-giá-con-số-và-vì-sao-nó-giết-vai-trò-đơn-vị-tính-toán)              |
| **Trải nghiệm khó**  | Địa chỉ dài, phí, gas, khó hiểu    | 🟡 Khá hơn (tên miền ví, ví thông minh) nhưng vẫn tệ                                                           |
| **Bất khả đảo**      | Gửi nhầm là mất                    | ⏸️ Không đổi. Bản chất thiết kế. [§12](#12--không-có-nút-quên-mật-khẩu-sống-với-tính-bất-khả-đảo)              |
| **Lừa đảo tràn lan** | Rất nhiều dự án là bẫy             | 🔴 **Tệ hơn.** [§19](#19--bảng-phân-loại-8-kiểu-lừa-đảo)                                                       |
| **Năng lượng**       | PoW tốn điện khủng khiếp           | 🟢 Ethereum PoS giảm ~99,95%. Bitcoin thì không đổi. [§18](#18--năng-lượng-con-số-thật-và-hai-phía-tranh-luận) |
| **Mở rộng**          | Vài giao dịch/giây                 | 🟡 Lớp 2 giúp nhiều; chain nền vẫn vậy                                                                         |
| **Pháp lý mơ hồ**    | Chưa rõ luật                       | 🟢 Rõ hơn hẳn (MiCA, ETF). [§20](#20--pháp-lý-và-thuế--trạng-thái-2026)                                        |

Đọc cột cuối theo hàng dọc thì thấy một quy luật:

> **Những gì cải thiện được là chuyện kỹ thuật và thể chế (năng lượng, mở rộng, pháp lý). Những gì không nhúc nhích là chuyện bản chất (biến động, bất khả đảo) và chuyện con người (lừa đảo).** Đúng luận điểm mở đầu bài: mật mã không phải chỗ vỡ.

---

## 17. 📚 Biến động giá: con số, và vì sao nó giết vai trò "đơn vị tính toán"

Video nói "biến động mạnh". Con số cụ thể:

| Chỉ số                           | Bitcoin                  | S&P 500             | Vàng         |
| -------------------------------- | ------------------------ | ------------------- | ------------ |
| Biến động năm (ước tính lịch sử) | **~50–80%**              | ~15%                | ~15%         |
| Sụt sâu nhất từng có             | **~-85%**                | ~-57% (2008)        | ~-45% (1980) |
| Số lần sụt trên 50%              | **Nhiều lần** kể từ 2011 | 3 lần trong 100 năm | Vài lần      |

Ba chu kỳ sụt sâu đã xảy ra: 2013–2015 (~-85%), 2017–2018 (~-84%), 2021–2022 (~-77%). Mỗi lần đều kèm dự đoán "lần này là chết hẳn", và mỗi lần đều hồi. Điều đó **không bảo đảm** lần sau cũng thế — nhưng nó nói rằng biến động cỡ này là **đặc tính thường trực**, không phải sự cố.

### Vì sao điều này giết chức năng số 2

Quay lại [§2](#2-tiền-là-gì--và-tiền-mã-hoá-là-loại-tiền-nào). Một **đơn vị tính toán** phải là **cái thước không co giãn**:

```
   Bạn ký hợp đồng thuê nhà 0,1 BTC/tháng.

   Tháng 1: BTC = 40.000 USD  →  bạn trả 4.000 USD
   Tháng 6: BTC = 90.000 USD  →  bạn trả 9.000 USD  ← chủ nhà rất vui
   Tháng 9: BTC = 25.000 USD  →  bạn trả 2.500 USD  ← chủ nhà rất không vui

   Không ai ký nổi hợp đồng dài hạn bằng một cái thước co giãn 2 lần trong 6 tháng.
```

Vì thế trong thực tế, **gần như mọi hợp đồng "bằng crypto" đều định giá bằng USD** rồi quy đổi lúc thanh toán. Nghĩa là: USD vẫn đang làm chức năng đơn vị tính toán; crypto chỉ làm chức năng **phương tiện chuyển giao**.

> 💡 Đây cũng chính là lý do stablecoin ([§15](#15--stablecoin-ba-cơ-chế-neo-giá-và-cái-đã-nổ)) là mảng có khối lượng giao dịch lớn nhất. Thị trường đã tự trả lời: nó muốn **đường ray của blockchain** với **cái thước của USD**. Nhìn thẳng, đó là một sự thừa nhận — thứ được dùng nhiều nhất trong hệ sinh thái này là một token đại diện cho **chính đồng tiền pháp định** mà [§4](#4--tiền-pháp-định-đến-từ-đâu-và-vì-sao-bitcoin-ra-đời-năm-2008) nói Bitcoin sinh ra để thay thế.

---

## 18. 📚 Năng lượng: con số thật và hai phía tranh luận

Chủ đề bị bóp méo từ cả hai phía. Số liệu trước, tranh luận sau.

```
   Bitcoin (PoW), ước tính khoảng 2024–2026:  ~150–180 TWh/năm
      ≈ mức tiêu thụ điện của một nước cỡ trung
      ≈ 0,5–0,7% điện toàn cầu

   Ethereum TRƯỚC The Merge (PoW):  ~75–80 TWh/năm
   Ethereum SAU  The Merge (PoS) :  ~0,01 TWh/năm     ← giảm ~99,95%
                                     (Bài 5 nói vì sao)
```

Con số Ethereum là dữ kiện quan trọng nhất trong cả mục này: nó chứng minh **mức tiêu thụ điện là hệ quả của LỰA CHỌN đồng thuận, không phải của blockchain**. Sau 15/09/2022, chain lớn thứ hai chạy hết công suất với lượng điện gần bằng không.

| Phe phản đối                            | Phe ủng hộ                                                |
| --------------------------------------- | --------------------------------------------------------- |
| Tốn điện bằng cả một quốc gia           | Ngành ngân hàng, khai thác vàng cũng tốn rất nhiều        |
| Phát thải trong lúc khủng hoảng khí hậu | Tỷ lệ năng lượng tái tạo/thải bỏ trong đào coin đang tăng |
| Sản lượng "hữu ích" bằng 0              | "Hữu ích" là phán xét giá trị, không phải phép đo         |
| ASIC thành rác điện tử nhanh            | Thợ đào tiêu thụ điện dư thừa, khí đồng hành bị đốt bỏ    |

**Chỗ tranh luận thường bị lái sai:** câu hỏi đúng không phải "Bitcoin dùng bao nhiêu điện" mà là **"số điện đó mua được cái gì"**. Trong PoW, điện **chính là** bảo mật — [Bài 7](../ly_thuyet/lesson_7_do_kho_dao.md) cho thấy chi phí tấn công tỷ lệ thuận với hashrate, mà hashrate tỷ lệ thuận với điện. Giảm điện = giảm bảo mật, không có bữa trưa miễn phí.

> 💡 Vì thế lập luận trung thực nhất là: *"Bitcoin mua bảo mật bằng điện. Ethereum chuyển sang mua bảo mật bằng vốn bị khoá."* Cả hai đều tốn. Cái sau **rẻ hơn nhiều về năng lượng** và đánh đổi bằng một mô hình bảo mật khác — với những phê phán riêng mà [Bài 5 §12](../ly_thuyet/lesson_5_proof_of_stake.md) đã liệt kê. Không có bên nào thắng tuyệt đối, nhưng nói "blockchain nhất thiết phải tốn điện" là **sai kể từ 2022**.

---

## 19. 📚 Bảng phân loại 8 kiểu lừa đảo

Video cảnh báo chung. Đây là bản chi tiết — **mục thực dụng nhất của bài này**. Đọc kỹ tám dòng dưới thì bạn tránh được đại đa số trường hợp mất tiền trong thực tế.

| #   | Kiểu                          | Cách chạy                                                  | Dấu hiệu nhận biết                                              |
| --- | ----------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| 1   | **Rút thảm** (rug pull)       | Đội ngũ gom tiền rồi biến mất                              | Đội ẩn danh, thanh khoản không bị khoá, hợp đồng chưa kiểm toán |
| 2   | **Ponzi / lợi nhuận cố định** | Trả người cũ bằng tiền người mới                           | "Lãi 1%/ngày", "bảo đảm không lỗ", có hoa hồng giới thiệu       |
| 3   | **Bơm xả**                    | Nhóm kín gom hàng, hô hào, xả lên đầu người mua            | Coin vô danh bỗng lên xu hướng, kêu gọi "mua ngay kẻo lỡ"       |
| 4   | **Lừa tình / mổ lợn**         | Làm quen nhiều tuần, rồi dụ đầu tư qua nền tảng giả        | Người lạ nhắn tin, quan hệ ấm dần, luôn dẫn tới đầu tư          |
| 5   | **Web/ví giả**                | Trang chép y hệt, đánh cắp seed phrase                     | URL lệch một ký tự, quảng cáo trên máy tìm kiếm, hỏi seed       |
| 6   | **Lừa ký giao dịch**          | Bạn tự ký một `approve` cho contract rút sạch token        | Yêu cầu ký thứ bạn không đọc hiểu, "mint miễn phí"              |
| 7   | **Giả mạo hỗ trợ**            | "Nhân viên hỗ trợ" nhắn riêng khi bạn than phiền công khai | **Chủ động nhắn trước**, xin seed hoặc màn hình                 |
| 8   | **Tặng quà giả**              | "Gửi 1 ETH, nhận lại 2 ETH", mạo danh người nổi tiếng      | Toán học tự nó vô lý                                            |

### Ba câu hỏi lọc được gần hết

```
   1. "Lợi nhuận này đến từ đâu?"
      Không giải thích được bằng MỘT câu → nguồn tiền là người vào sau.

   2. "Vì sao họ cần TÔI?"
      Ai có máy in tiền thật thì không đi tìm bạn trên Telegram.

   3. "Có gấp không?"
      Sự gấp gáp là công cụ, không phải tình huống. Nó tồn tại để bạn
      không kịp làm bước 1 và 2.
```

> ⚠️ **Bất khả đảo biến lừa đảo crypto thành một loại tội phạm khác hẳn.** Bị lừa qua thẻ tín dụng thì còn cơ chế đòi lại. Ở đây, giao dịch đã xác nhận là **chung cuộc trên toàn cầu trong vài giây**. Không có ai để kháng nghị. Chính tính chất mà [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) ca ngợi là bảo vệ bạn khỏi kiểm duyệt, cũng là tính chất bảo vệ **kẻ lừa bạn**. Cùng một tính chất, không tách rời được.

---

## 20. 📚 Pháp lý và thuế — trạng thái 2026

Video (2022) nói pháp lý còn mơ hồ. Đây là mục thay đổi nhiều nhất kể từ đó.

| Khu vực      | Trạng thái                                                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EU**       | **MiCA** — khung pháp lý toàn diện đầu tiên, áp dụng đầy đủ từ cuối 2024: cấp phép nhà cung cấp dịch vụ, quy định riêng cho stablecoin, minh bạch dự trữ |
| **Mỹ**       | ETF Bitcoin giao ngay được duyệt 01/2024. Thẩm quyền giữa các cơ quan quản lý vẫn còn giằng co                                                           |
| **Toàn cầu** | **Travel Rule** (FATF): giao dịch trên ngưỡng phải kèm thông tin người gửi/nhận giữa các tổ chức                                                         |
| **Việt Nam** | Khung pháp lý cho tài sản mã hoá đang trong quá trình hình thành — **tự tra cứu quy định hiện hành trước khi làm gì**, đừng tin bài viết cũ              |

### Thuế — chỗ người ta hay bị bất ngờ

Ở nhiều nước, những việc sau **đều là sự kiện chịu thuế**, kể cả khi bạn không hề rút ra tiền mặt:

```
   ✓ Bán crypto lấy tiền pháp định
   ✓ ĐỔI coin này lấy coin khác          ← rất nhiều người không biết
   ✓ Dùng crypto để mua hàng             ← cũng là một lần bán
   ✓ Nhận thưởng đào / staking / airdrop ← thường tính là thu nhập
   ✗ Mua và giữ nguyên
   ✗ Chuyển giữa các ví của chính mình
```

> ⚠️ Hệ quả vận hành: **bạn phải lưu lại lịch sử**. Ngày, số lượng, giá quy đổi tại thời điểm giao dịch, phí. Sàn có thể ngừng hoạt động và mang theo toàn bộ lịch sử của bạn — chuyện đã xảy ra nhiều lần. Xuất dữ liệu định kỳ. Đây là lời khuyên nhàm chán nhất trong bài và cũng là lời khuyên nhiều người ước gì đã nghe theo. Luật thuế khác nhau theo nước và thay đổi liên tục — mục này để bạn **biết mà đi hỏi**, không phải để thay tư vấn thuế.

---

## 21. 📚 Khung quyết định: tôi có nên đụng vào không

[Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md) cho bạn khung "dự án này có cần blockchain không". Đây là khung tương ứng cho **cá nhân**, chưng cất từ toàn bộ những gì ở trên.

```
   ┌─ Bạn muốn dùng nó để LÀM GÌ? ────────────────────────────────┐
   │                                                                │
   │  "Chuyển tiền quốc tế, nhanh và rẻ"                            │
   │      → ✅ Chính đáng. Dùng stablecoin. Gửi thử số nhỏ trước.   │
   │      → Nhớ: bạn đang tin tổ chức phát hành stablecoin. (§15)   │
   │                                                                │
   │  "Tôi ở nước có siêu lạm phát / bị chặn tài chính"             │
   │      → ✅ Đây là trường hợp dùng MẠNH NHẤT. Tự lưu ký. (§11)   │
   │                                                                │
   │  "Học công nghệ"                                               │
   │      → ✅ Số tiền nhỏ, ví riêng, mạng thử nghiệm. Xem thuc_hanh/│
   │                                                                │
   │  "Đầu tư dài hạn, tôi hiểu là có thể mất phần lớn"             │
   │      → 🟡 Được, nếu ĐÚNG là tiền bạn mất được. Ví lạnh. (§17)  │
   │                                                                │
   │  "Kiếm lời nhanh" / "ai cũng đang giàu lên"                    │
   │      → 🔴 DỪNG. Đọc lại §19. Bạn chính là nguồn tiền.          │
   │                                                                │
   │  "Có người hướng dẫn tôi và đang lãi đều"                      │
   │      → 🔴 DỪNG NGAY. §19 dòng 2 và dòng 4.                     │
   └────────────────────────────────────────────────────────────────┘
```

Bốn quy tắc, nếu chỉ nhớ được bốn câu từ cả bài:

1. **Không phải khoá của bạn thì không phải coin của bạn.** ([§10](#10-ví-và-khoá-riêng))
2. **Chỉ bỏ vào số tiền mà mất hết cũng không đổi cuộc sống của bạn.** ([§17](#17--biến-động-giá-con-số-và-vì-sao-nó-giết-vai-trò-đơn-vị-tính-toán))
3. **Lợi nhuận không giải thích được bằng một câu thì nguồn tiền là bạn.** ([§19](#19--bảng-phân-loại-8-kiểu-lừa-đảo))
4. **Gửi thử số nhỏ trước. Luôn luôn.** ([§12](#12--không-có-nút-quên-mật-khẩu-sống-với-tính-bất-khả-đảo))

---

## 22. Code minh hoạ

Ba thứ ở trên video nói bằng lời, ở đây cho **chạy bằng số**. Chỉ dùng thư viện chuẩn của Node.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node crypto101.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
// crypto101.ts — Ba thứ video nói bằng lời, ở đây cho chạy bằng số:
//   1. Proof of Reserves bằng cây Merkle — và VÌ SAO nó không chứng minh được gì
//   2. Dự trữ một phần: sàn "vẫn khoẻ" cho tới đúng một ngày
//   3. Vòng xoáy tử thần của stablecoin thuật toán (UST/LUNA, 05/2022)
// Chạy: node crypto101.ts
import { strict as assert } from "node:assert";
import { createHash } from "node:crypto";

const sha = (s: string): string => createHash("sha256").update(s).digest("hex");
const usd = (n: number): string =>
  n.toLocaleString("en-US", { maximumFractionDigits: 0 });

/** PRNG tất định — cùng seed, cùng kết quả, mọi máy. */
function seeded(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ─────────────────────────────────────────────────────────────
// 1. PROOF OF RESERVES — cây Merkle của số dư khách hàng
// ─────────────────────────────────────────────────────────────

type Account = { id: string; balance: number };

/** Lá = băm của (id, số dư). Muối để hai người cùng số dư không lộ nhau. */
const leafHash = (a: Account): string => sha(`${a.id}|${a.balance}|salt`);

/** Trả về [gốc, các tầng] — tầng 0 là lá. Lẻ thì nhân đôi phần tử cuối. */
function merkle(accounts: Account[]): { root: string; levels: string[][] } {
  const levels: string[][] = [accounts.map(leafHash)];
  while (levels[levels.length - 1].length > 1) {
    const cur = levels[levels.length - 1];
    const next: string[] = [];
    for (let i = 0; i < cur.length; i += 2)
      next.push(sha(cur[i] + (cur[i + 1] ?? cur[i])));
    levels.push(next);
  }
  return { root: levels[levels.length - 1][0], levels };
}

/** Đường đi từ lá lên gốc: [hash anh em, nó nằm bên phải?]. */
function proof(levels: string[][], index: number): [string, boolean][] {
  const path: [string, boolean][] = [];
  let i = index;
  for (let d = 0; d < levels.length - 1; d++) {
    const cur = levels[d];
    const sib = i % 2 === 0 ? (cur[i + 1] ?? cur[i]) : cur[i - 1];
    path.push([sib, i % 2 === 0]);
    i = i >> 1;
  }
  return path;
}

function verify(a: Account, path: [string, boolean][], root: string): boolean {
  let h = leafHash(a);
  for (const [sib, isLeft] of path) h = sha(isLeft ? h + sib : sib + h);
  return h === root;
}

function demoProofOfReserves(): void {
  console.log("=== 1. Proof of Reserves: cai no chung minh va cai no KHONG ===");

  const users: Account[] = [
    { id: "an", balance: 2.5 },
    { id: "binh", balance: 0.8 },
    { id: "chi", balance: 12.0 },
    { id: "dung", balance: 0.05 },
    { id: "em", balance: 40.0 },
    { id: "phuc", balance: 1.2 },
  ];
  const { root, levels } = merkle(users);
  const liabilities = users.reduce((s, u) => s + u.balance, 0);   // tổng NỢ

  console.log(`  So khach       : ${users.length}`);
  console.log(`  Merkle root    : ${root.slice(0, 24)}...`);
  console.log(`  Tong NO (BTC)  : ${liabilities.toFixed(2)}`);

  // Khách tự kiểm tra: "số dư của tôi có nằm trong cái root đã công bố không?"
  const i = 2;
  const p = proof(levels, i);
  assert(verify(users[i], p, root), "chi phai chung minh duoc");
  console.log(`  ✓ 'chi' chung minh duoc 12 BTC nam trong root (${p.length} hash)`);

  // Đổi một chữ số → hỏng ngay. Sàn không khai thiếu số dư của ai được...
  assert(!verify({ id: "chi", balance: 11.0 }, p, root));
  console.log("  ✓ Khai thieu so du cua 'chi' -> proof gay");

  // ...nhưng sàn XOÁ HẲN một khách thì cây vẫn hợp lệ với mọi khách còn lại.
  const trimmed = users.filter((u) => u.id !== "em");     // giấu 40 BTC nợ
  const cheatTree = merkle(trimmed);
  const j = trimmed.findIndex((u) => u.id === "chi");
  assert(verify(trimmed[j], proof(cheatTree.levels, j), cheatTree.root));
  console.log("  ⚠ Xoa han khach 'em' (40 BTC) -> 'chi' VAN verify OK");
  console.log(`    -> no cong bo tut ${liabilities.toFixed(2)} -> ${(liabilities - 40).toFixed(2)} BTC, khong ai thay`);

  // Và phía tài sản: ký một địa chỉ chỉ chứng minh "lúc này tôi chạm được coin".
  const reserves = 40;
  console.log(`\n  Du tru chung minh on-chain : ${reserves} BTC`);
  console.log(`  No that                    : ${liabilities.toFixed(2)} BTC`);
  console.log(`  -> Ty le du tru            : ${((reserves / liabilities) * 100).toFixed(0)}%  (MAT KHA NANG CHI TRA)`);
  assert(reserves < liabilities);
  console.log("  => Proof of Reserves khong co PROOF OF LIABILITIES thi vo nghia.");
}

// ─────────────────────────────────────────────────────────────
// 2. DỰ TRỮ MỘT PHẦN — sàn khoẻ mạnh cho tới đúng một ngày
// ─────────────────────────────────────────────────────────────

function demoBankRun(): void {
  console.log("\n=== 2. Du tru mot phan: 'chua bao gio co su co' ===");

  const deposits = 1000;           // BTC khách gửi
  const reserveRatio = 0.15;       // sàn giữ 15%, 85% đem đi cho vay/đầu tư
  let reserves = deposits * reserveRatio;
  let liabilities = deposits;      // nợ khách
  const rand = seeded(2022);

  console.log(`  Khach gui ${deposits} BTC, san giu lai ${reserveRatio * 100}% = ${reserves} BTC`);
  console.log("  Ngay | Rut ra | Du tru con | Trang thai");

  let collapseDay = 0;
  for (let day = 1; day <= 12; day++) {
    // Tin xấu lan ra: tỷ lệ rút mỗi ngày tăng dần (hoảng loạn có phản hồi dương).
    const withdrawRate = 0.01 * Math.pow(1.7, day - 1) * (0.8 + 0.4 * rand());
    const requested = liabilities * withdrawRate;
    const paid = Math.min(requested, reserves);
    reserves -= paid;
    liabilities -= paid;
    const solvent = paid >= requested - 1e-9;
    console.log(
      `   ${String(day).padStart(2)}  | ${requested.toFixed(1).padStart(6)} | ` +
        `${reserves.toFixed(1).padStart(10)} | ${solvent ? "OK" : "⛔ TAM DUNG RUT TIEN"}`,
    );
    if (!solvent) { collapseDay = day; break; }
  }

  assert(collapseDay > 0, "voi du tru mot phan, bank run luon ket thuc o day");
  console.log(`  => San sap ngay thu ${collapseDay}. No con lai chua tra: ${liabilities.toFixed(1)} BTC.`);
  console.log("  => Khong phai vi hack. Chi vi khach doi lay thu ma san khong giu.");
}

// ─────────────────────────────────────────────────────────────
// 3. VÒNG XOÁY TỬ THẦN — stablecoin thuật toán
// ─────────────────────────────────────────────────────────────

function demoDeathSpiral(): void {
  console.log("\n=== 3. Stablecoin thuat toan: vong xoay tu than (UST/LUNA 05/2022) ===");

  // Luật: đốt 1 UST -> đúc lượng LUNA trị giá 1 USD (theo giá HIỆN TẠI). Và ngược lại.
  // Neo giá đứng vững KHI VÀ CHỈ KHI vốn hoá LUNA còn lớn hơn lượng UST đang lưu hành.
  let ustSupply = 18_000_000_000;       // 18 tỷ UST đang lưu hành
  let lunaSupply = 350_000_000;         // 350 triệu LUNA
  let lunaPrice = 80;                   // 80 USD
  const depth = 800_000_000;            // thanh khoản: bán $800tr -> giá còn 1/2

  const lunaSupply0 = lunaSupply;
  console.log(`  Bat dau: ${ustSupply / 1e9} ty UST | LUNA ${usd(lunaSupply / 1e6)}tr x $${lunaPrice}`
    + ` = $${usd((lunaSupply * lunaPrice) / 1e9)} ty von hoa`);
  console.log("  Vong | UST con lai | LUNA cung   | Gia LUNA  | Bao chung | % chay");

  for (let round = 1; round <= 8; round++) {
    const backing = (lunaSupply * lunaPrice) / ustSupply;   // tỷ lệ bảo chứng
    // Bảo chứng càng mỏng, càng nhiều người tháo chạy. Đây là phản hồi DƯƠNG.
    const exitRate = Math.min(1, Math.max(0.08, 0.08 / Math.max(backing, 0.02)));

    console.log(
      `   ${String(round).padStart(2)}  | ${(ustSupply / 1e9).toFixed(2).padStart(8)} ty | ` +
        `${usd(lunaSupply / 1e6).padStart(7)} tr | ${lunaPrice.toExponential(2).padStart(9)} | ` +
        `${backing.toFixed(2).padStart(6)}x   | ${(exitRate * 100).toFixed(0)}%`,
    );

    const redeemed = ustSupply * exitRate;        // đốt UST...
    const lunaMinted = redeemed / lunaPrice;      // ...đúc LUNA theo giá hiện tại, bán ngay
    ustSupply -= redeemed;
    lunaSupply += lunaMinted;
    lunaPrice *= depth / (depth + redeemed);      // sức bán ép giá xuống
  }

  console.log(`  => LUNA: $80 -> $${lunaPrice.toFixed(4)} (-${(100 - (lunaPrice / 80) * 100).toFixed(2)}%),`
    + ` cung phinh ${(lunaSupply / lunaSupply0).toFixed(0)} lan.`);
  console.log(`  => UST luu hanh: 18 ty -> ${(ustSupply / 1e9).toFixed(2)} ty.`);
  assert(lunaPrice < 0.05 && lunaSupply > 100 * lunaSupply0 && ustSupply < 0.1 * 18e9);
  console.log("  => Tai san BAO CHUNG chinh la thu dam dong dang BAN. Do la vong xoay tu than.");
  console.log("     (Mo hinh tho. Thuc te 05/2022 con te hon: cung LUNA phinh ~18 trieu lan.)");
}

demoProofOfReserves();
demoBankRun();
demoDeathSpiral();
console.log("\n✓ Tat ca assert deu qua.");
```

### Kết quả

```
=== 1. Proof of Reserves: cai no chung minh va cai no KHONG ===
  So khach       : 6
  Merkle root    : efc9418768cf34173c63b737...
  Tong NO (BTC)  : 56.55
  ✓ 'chi' chung minh duoc 12 BTC nam trong root (3 hash)
  ✓ Khai thieu so du cua 'chi' -> proof gay
  ⚠ Xoa han khach 'em' (40 BTC) -> 'chi' VAN verify OK
    -> no cong bo tut 56.55 -> 16.55 BTC, khong ai thay

  Du tru chung minh on-chain : 40 BTC
  No that                    : 56.55 BTC
  -> Ty le du tru            : 71%  (MAT KHA NANG CHI TRA)
  => Proof of Reserves khong co PROOF OF LIABILITIES thi vo nghia.

=== 2. Du tru mot phan: 'chua bao gio co su co' ===
  Khach gui 1000 BTC, san giu lai 15% = 150 BTC
  Ngay | Rut ra | Du tru con | Trang thai
    1  |    8.3 |      141.7 | OK
    2  |   20.1 |      121.6 | OK
    3  |   26.1 |       95.5 | OK
    4  |   53.2 |       42.2 | OK
    5  |   81.8 |        0.0 | ⛔ TAM DUNG RUT TIEN
  => San sap ngay thu 5. No con lai chua tra: 850.0 BTC.
  => Khong phai vi hack. Chi vi khach doi lay thu ma san khong giu.

=== 3. Stablecoin thuat toan: vong xoay tu than (UST/LUNA 05/2022) ===
  Bat dau: 18 ty UST | LUNA 350tr x $80 = $28 ty von hoa
  Vong | UST con lai | LUNA cung   | Gia LUNA  | Bao chung | % chay
    1  |    18.00 ty |     350 tr |   8.00e+1 |   1.56x   | 8%
    2  |    16.56 ty |     368 tr |   2.86e+1 |   0.63x   | 13%
    3  |    14.47 ty |     441 tr |   7.92e+0 |   0.24x   | 33%
    4  |     9.67 ty |   1,047 tr |   1.13e+0 |   0.12x   | 65%
    5  |     3.35 ty |   6,633 tr |   1.27e-1 |   0.25x   | 32%
    6  |     2.29 ty |  15,030 tr |   5.45e-2 |   0.36x   | 22%
    7  |     1.78 ty |  24,414 tr |   3.32e-2 |   0.46x   | 18%
    8  |     1.46 ty |  33,771 tr |   2.39e-2 |   0.55x   | 15%
  => LUNA: $80 -> $0.0189 (-99.98%), cung phinh 122 lan.
  => UST luu hanh: 18 ty -> 1.25 ty.
  => Tai san BAO CHUNG chinh la thu dam dong dang BAN. Do la vong xoay tu than.
     (Mo hinh tho. Thuc te 05/2022 con te hon: cung LUNA phinh ~18 trieu lan.)

✓ Tat ca assert deu qua.
```

| Demo                     | Bài học                                                                                                                                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Proof of Reserves** | 💥 **Điểm sắc nhất.** Cây Merkle **đúng tuyệt đối** về toán, mọi proof đều verify — mà vẫn giấu được 40 BTC nợ. Một bằng chứng mật mã hợp lệ **không** đảm bảo mệnh đề bạn đang quan tâm là đúng. Chỗ vỡ nằm ở **cái được đưa vào cây**, không ở thuật toán. |
| **2. Dự trữ một phần**   | Sàn chạy êm 4 ngày rồi sập ngày thứ 5 — bằng phép toán, không cần gian lận thêm. Đây là mô hình của **mọi** vụ ở [§8](#8--sàn-tập-trung-là-một-cuốn-sổ-nợ-không-phải-blockchain).                                                                           |
| **3. Vòng xoáy tử thần** | Cơ chế neo giá **hoạt động đúng như thiết kế** trong lúc phá huỷ chính nó. Không có bug. Kiến trúc sai.                                                                                                                                                     |

**Tự thử nghiệm:**

- Trong demo 1, thêm một khách có `balance` **âm** rồi tính lại tổng nợ. Bạn vừa tái hiện lỗ hổng thứ ba ở [§9](#9--proof-of-reserves--và-vì-sao-nó-gần-như-vô-nghĩa) — và hiểu vì sao PoR nghiêm túc cần range proof của [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md).
- Trong demo 2, đổi `reserveRatio` thành `1.0` (dự trữ toàn phần) và chạy lại. `assert` sẽ **gãy** — vì sàn không còn sập được nữa. Đó chính xác là ý nghĩa của "not your keys, not your coins" phát biểu ngược lại.
- Trong demo 3, tăng `depth` lên 50 tỷ (thanh khoản vô hạn) rồi chạy. Neo giá giữ được. Giờ giảm xuống 200 triệu. Thanh khoản **chính là** thứ quyết định, và nó là thứ **bốc hơi đúng lúc bạn cần nhất**.
- Ghép demo 2 và 3: một sàn giữ dự trữ bằng chính token do nó phát hành. Bạn vừa mô hình hoá vụ FTX/FTT.

> ⚠️ **Code này để HỌC.** Các mô hình thị trường ở demo 2 và 3 là **thô có chủ ý** — đủ đúng về hướng để thấy vòng phản hồi, không đủ đúng về lượng để định giá bất cứ thứ gì.

---

## 23. Từ điển thuật ngữ

| Thuật ngữ                         | Giải thích                                                         |
| --------------------------------- | ------------------------------------------------------------------ |
| **Phương tiện trao đổi**          | Chức năng 1 của tiền: ai cũng chịu nhận                            |
| **Đơn vị tính toán**              | Chức năng 2: thước đo giá trị chung                                |
| **Lưu trữ giá trị**               | Chức năng 3: giữ được giá trị qua thời gian                        |
| **Trùng khớp nhu cầu kép**        | Vấn đề của hàng đổi hàng mà tiền sinh ra để giải                   |
| **Tiền pháp định (fiat)**         | Tiền có giá trị nhờ luật và niềm tin, không có bảo chứng           |
| **Dự trữ một phần**               | Chỉ giữ một phần tiền gửi; phần còn lại đem cho vay                |
| **Bank run**                      | Nhiều người đòi rút cùng lúc → tổ chức lưu ký sập                  |
| **Tính đồng nhất (fungibility)**  | Đơn vị nào cũng như đơn vị nào, không phân biệt lý lịch            |
| **Coin**                          | Đồng bản địa của một blockchain, dùng trả phí                      |
| **Token**                         | Tài sản do smart contract phát hành trên chain có sẵn              |
| **ERC-20 / ERC-721**              | Chuẩn giao diện cho token thay thế được / NFT                      |
| **CEX**                           | Sàn tập trung — giữ khoá hộ bạn                                    |
| **DEX**                           | Sàn phi tập trung — bạn giữ khoá, giao dịch qua contract           |
| **Lưu ký (custody)**              | Ai đang thật sự giữ khoá riêng                                     |
| **Not your keys, not your coins** | Không giữ khoá thì bạn chỉ đang giữ một lời hứa                    |
| **Ví nóng / ví lạnh**             | Khoá nằm trên máy nối mạng / trên thiết bị tách mạng               |
| **Đa chữ ký (multisig)**          | Cần t trong n khoá mới chi tiêu được                               |
| **Seed phrase**                   | 12–24 từ mã hoá khoá riêng (BIP-39)                                |
| **Proof of Reserves**             | Sàn chứng minh nắm tài sản — **không** chứng minh khả năng chi trả |
| **Proof of Liabilities**          | Nửa còn lại, khó hơn, ít ai làm tử tế                              |
| **Tam giác bất khả**              | Phi tập trung / bảo mật / mở rộng — chọn 2                         |
| **Hard fork**                     | Tách chuỗi theo luật mới; chép lịch sử, không chép hashrate        |
| **Tổ chức lại chuỗi (reorg)**     | Chuỗi dài hơn thay thế chuỗi đang có; công cụ của tấn công 51%     |
| **Stablecoin**                    | Token neo giá vào tài sản khác, thường là USD                      |
| **Vòng xoáy tử thần**             | Vòng phản hồi dương phá huỷ stablecoin thuật toán                  |
| **Bảo chứng vượt mức**            | Khoá tài sản trị giá lớn hơn lượng token đúc ra                    |
| **Rug pull**                      | Đội ngũ gom tiền rồi biến mất                                      |
| **Ponzi**                         | Trả người cũ bằng tiền người mới                                   |
| **Bơm xả (pump and dump)**        | Thổi giá rồi xả lên người mua sau                                  |
| **Lừa ký giao dịch**              | Dụ bạn ký `approve` cho contract rút sạch token                    |
| **Travel Rule**                   | Quy định FATF: kèm thông tin người gửi/nhận khi chuyển             |
| **MiCA**                          | Khung pháp lý tài sản mã hoá của EU                                |
| **Sự kiện chịu thuế**             | Hành động làm phát sinh nghĩa vụ thuế — gồm cả đổi coin lấy coin   |

---

## 24. Câu hỏi tự kiểm tra

1. Nêu ba chức năng của tiền. Tiền mã hoá làm tốt chức năng nào, tệ chức năng nào?
2. "Trùng khớp nhu cầu kép" là gì, và tiền giải nó bằng cách nào?
3. Phân biệt tiền hàng hoá, tiền đại diện, tiền pháp định. Năm 1971 có gì đặc biệt?
4. Liệt kê 6 tính chất của tiền. Bitcoin thua ở tính chất nào, và vì sao **không lập trình ra được** tính chất đó?
5. Vì sao tính đồng nhất và tính tuân thủ pháp luật kéo nhau ngược chiều? Liên hệ [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md).
6. Giải thích dự trữ một phần. Vì sao bank run **luôn** thắng?
7. Genesis block nhúng gì, và tại sao chi tiết đó vừa là dấu thời gian vừa là tuyên ngôn?
8. "Blockchain không thể bị sửa" sai ở chỗ nào? Phát biểu lại cho đúng.
9. Phân biệt coin và token. Có 1000 USDT trên Ethereum mà không có ETH thì chuyện gì xảy ra?
10. Khi bạn mua BTC trên một sàn tập trung, có giao dịch nào lên chuỗi không? Bạn thật sự đang sở hữu cái gì?
11. So sánh ngân hàng và sàn crypto theo 6 tiêu chí ở [§8](#8--sàn-tập-trung-là-một-cuốn-sổ-nợ-không-phải-blockchain). Ô nào tàn nhẫn nhất với người dùng?
12. Mẫu chung của Mt.Gox, Celsius, FTX là gì? **Có vụ nào do phá vỡ mật mã không?**
13. Vì sao "tạm dừng rút tiền" là tín hiệu gần như hoàn hảo?
14. Proof of Reserves gồm hai nửa nào? Nêu **bốn** lỗ hổng.
15. Trong demo 1, vì sao xoá hẳn một khách mà mọi khách còn lại vẫn verify OK? Điều này nói gì về giới hạn của bằng chứng mật mã?
16. "Not your keys, not your coins" nghĩa là gì? Vì sao "ví" là cái tên sai?
17. Nêu 4 mô hình lưu ký và trường hợp dùng của mỗi cái. Ví lạnh **không** chống được kiểu tấn công nào?
18. Ba biện pháp sống chung với tính bất khả đảo. Vì sao đa chữ ký 2-of-3 giải được bài toán thừa kế?
19. Phát biểu tam giác bất khả. Lớp 2 "giải" nó hay chỉ dời điểm đánh đổi?
20. Vì sao một hard fork "chép lịch sử nhưng không chép hashrate" là nguy hiểm? Cho ví dụ thật.
21. Năm câu hỏi lọc một đồng coin. Câu nào loại được nhiều nhất?
22. Ba cơ chế neo giá stablecoin. Cái nào đã nổ, và **điểm chết nằm ở đâu trong thiết kế**?
23. Vì sao ngay cả stablecoin bảo chứng bằng tiền thật cũng có rủi ro? Kể vụ tháng 3/2023.
24. Từ 2022 tới 2026, nhược điểm nào cải thiện, nhược điểm nào không? Quy luật là gì?
25. Vì sao biến động giá giết chức năng "đơn vị tính toán"? Vì sao stablecoin là mảng có khối lượng lớn nhất, và điều đó thừa nhận điều gì?
26. Ethereum sau The Merge tốn bao nhiêu điện so với trước? Dữ kiện đó **bác bỏ** lập luận nào?
27. Trong PoW, số điện tiêu thụ mua được cái gì? Vì sao "giảm điện" không miễn phí?
28. Kể 8 kiểu lừa đảo và dấu hiệu của mỗi kiểu. Ba câu hỏi lọc là gì?
29. Vì sao tính bất khả đảo làm lừa đảo crypto khác hẳn lừa đảo thẻ tín dụng?
30. Những hành động nào là sự kiện chịu thuế dù bạn chưa rút ra tiền mặt?
31. **Câu tổng kết:** nhìn lại cả 9 bài — mật mã đã thua bao nhiêu lần, và lớp nào thua nhiều nhất? Điều đó nên đổi cách bạn phân bổ sự cẩn trọng như thế nào?

---

## Tóm tắt một trang

```
TIỀN = 3 chức năng: TRAO ĐỔI | ĐƠN VỊ TÍNH TOÁN | LƯU TRỮ GIÁ TRỊ
   Crypto: tốt #1, tạm #3, TỆ #2  → vì thế stablecoin thống trị khối lượng

6 TÍNH CHẤT: bền | chia nhỏ | dễ mang | ĐỒNG NHẤT | KHAN HIẾM | ĐƯỢC CHẤP NHẬN
   Bitcoin thắng khan hiếm + dễ mang, THUA nặng "được chấp nhận"
   → tính chất DUY NHẤT không lập trình ra được (hiệu ứng mạng)

TIỀN PHÁP ĐỊNH: phần lớn do NH THƯƠNG MẠI tạo ra khi cho vay (dự trữ một phần)
   → bank run LUÔN thắng. Genesis block 03/01/2009 chỉ thẳng vào việc này.

COIN ≠ TOKEN
   coin  = đồng bản địa, trả phí gas, bảo mật = bảo mật của chain
   token = một dòng trong smart contract; ~90% số "coin" là token
   ⚠️ cùng tên trên hai chain KHÔNG phải một thứ → gửi nhầm mạng = mất

💥 NGHỊCH LÝ TRUNG TÂM
   Hệ thống sinh ra để KHÔNG CẦN TIN AI, được đa số dùng qua
   TRUNG GIAN PHẢI TIN TUYỆT ĐỐI — và ít bị giám sát hơn cả ngân hàng.
   Mua trên sàn = KHÔNG có giao dịch on-chain. Bạn giữ một GIẤY NỢ.

MẪU SẬP (Mt.Gox 2014 | Quadriga 2019 | Celsius, Terra, FTX 2022)
   giữ tài sản khách → đem đi dùng → êm nhiều năm → cú sốc
   → ⛔ TẠM DỪNG RÚT TIỀN ← tín hiệu gần như hoàn hảo → phá sản
   ⚠️ KHÔNG VỤ NÀO do phá vỡ mật mã. Mật mã chưa từng thua.

PROOF OF RESERVES = nửa TÀI SẢN (dễ) + nửa NỢ (khó, ít ai làm thật)
   4 lỗ: BỎ SÓT KHÁCH | vay đúng lúc chụp ảnh | số dư âm | nợ ngoài chuỗi
   💥 Demo 1: cây Merkle đúng tuyệt đối, mọi proof verify — vẫn giấu được nợ
   => PoR không có PoL thì vô nghĩa. Cả hai vẫn không bằng kiểm toán thật.

NOT YOUR KEYS, NOT YOUR COINS
   "Ví" không chứa coin — nó chứa KHOÁ. Coin luôn nằm trên chuỗi.
   nóng = ví trong túi | lạnh = két ở nhà | multisig = két 2 chìa | sàn = đưa người khác giữ
   ⚠️ Ví lạnh KHÔNG chống lừa ký. Chỗ vỡ là NGƯỜI, không phải thiết bị.
   ⛔ Không tồn tại lý do hợp lệ nào để ai đó cần seed phrase của bạn. Không ngoại lệ.

BẤT KHẢ ĐẢO: không có nút quên mật khẩu, không có ai để gọi
   → gửi thử số nhỏ | đối chiếu 4 ký tự đầu-cuối (malware tráo clipboard)
   → multisig 2-of-3 giải bài toán THỪA KẾ (Quadriga là bản phóng đại)

TAM GIÁC BẤT KHẢ: phi tập trung | bảo mật | mở rộng — chọn 2
   Lớp 2 không giải nó, chỉ DỜI điểm đánh đổi sang tầng khác
   Hard fork chép LỊCH SỬ nhưng KHÔNG chép HASHRATE → 51% giá vài chục nghìn đô
   (ETC 2019/2020, BTG 2018/2020 — đã xảy ra thật)

STABLECOIN: fiat-backed | crypto-overcollateralized | THUẬT TOÁN (đã chết)
   UST/LUNA 05/2022: đốt UST → đúc LUNA theo GIÁ HIỆN TẠI → bán → giá giảm
   → cùng lượng UST đúc ra NHIỀU LUNA HƠN → vòng lặp → ~40 tỷ USD, 3 ngày
   💀 ĐIỂM CHẾT: tài sản bảo chứng CHÍNH LÀ thứ đám đông đang bán.
   ⚠️ USDC rớt xuống ~0,87 (03/2023) vì SVB → fiat-backed kế thừa rủi ro NGÂN HÀNG

2022 → 2026: năng lượng 🟢 (PoS -99,95%) | pháp lý 🟢 (MiCA, ETF) | mở rộng 🟡
             biến động ⏸️ | bất khả đảo ⏸️ | LỪA ĐẢO 🔴 TỆ HƠN
   => Cải thiện được: kỹ thuật + thể chế. Không nhúc nhích: bản chất + CON NGƯỜI.

BA CÂU HỎI LỌC HẾT LỪA ĐẢO
   1. Lợi nhuận này đến từ đâu?  (không trả lời được bằng 1 câu → nguồn tiền là BẠN)
   2. Vì sao họ cần TÔI?         (ai có máy in tiền không đi tìm bạn trên Telegram)
   3. Có gấp không?              (gấp gáp là CÔNG CỤ, tồn tại để bạn không kịp hỏi 1 và 2)

BỐN QUY TẮC, nếu chỉ nhớ được bốn câu
   1. Không phải khoá của bạn thì không phải coin của bạn
   2. Chỉ bỏ vào số tiền mất hết cũng không đổi cuộc sống
   3. Lợi nhuận không giải thích được bằng một câu → nguồn tiền là bạn
   4. Gửi thử số nhỏ trước. Luôn luôn.
```

---

**Nguồn:**
- Video gốc: [Introduction to Cryptocurrencies](https://www.youtube.com/watch?v=vJfdO9QuroY) (Simply Explained – Savjee, CatholicCryptoConference 2022)
- Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008)
- Jevons, *Money and the Mechanism of Exchange* (1875) — nguồn gốc 6 tính chất của tiền
- [Cambridge Bitcoin Electricity Consumption Index](https://ccaf.io/cbnsi/cbeci) — số liệu năng lượng
- [Ethereum Foundation — The Merge](https://ethereum.org/en/roadmap/merge/) — số liệu giảm năng lượng
- EU **MiCA** (Regulation 2023/1114) — khung pháp lý tài sản mã hoá
- FATF — khuyến nghị **Travel Rule** cho nhà cung cấp dịch vụ tài sản ảo

> ⚠️ Số liệu định lượng trong bài (năng lượng, biến động, quy mô các vụ sập) là **ước tính từ nguồn công khai** và thay đổi theo thời gian. Dùng để hiểu **bậc độ lớn**, không dùng để trích dẫn chính xác. Bài này **không phải tư vấn tài chính hay thuế**.

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

9. **Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)** ← *bạn đang ở đây* — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
