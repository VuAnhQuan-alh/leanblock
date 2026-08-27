# ERC-20 — chuẩn token và những gì nó không chặn được

> Bài học dựa trên video **"ERC20 tokens — Simply Explained"** (kênh *Simply Explained – Savjee*, YouTube `cqZhNzZoMh8`, 6:04).
>
> Bài này nối [Bài 3](../ly_thuyet/lesson_3_smart_contract.md) — nơi đã có bảng ERC-20/721/1155 nhưng chưa mở ra bên trong — với [Bài 10](lesson_10_tai_chinh_phi_tap_trung.md), nơi mọi giao thức DeFi đều đứng trên chuẩn này.
> Phần **📚 Lý thuyết bổ sung** đặc biệt quan trọng ở bài này, vì **video mô tả sai ba trong sáu hàm bắt buộc** — xem [§6](#6--video-mô-tả-sai-ba-trong-sáu-hàm).
>
> ⚠️ **Video ghi đầu 2018**, giữa cơn sốt ICO. [§10](#10--thời-ico--4-tỷ-usd-và-cái-kết) và [§12](#12--erc-223-và-erc-777--bản-vá-hỏng-và-bản-vá-chạy-được) đối chiếu với 2026.
>
> 📌 **Cần đọc trước:** [Bài 3 – Smart contract](../ly_thuyet/lesson_3_smart_contract.md).

---

## Mục lục

1. [Token là gì — và nó không phải cái gì](#1-token-là-gì--và-nó-không-phải-cái-gì)
2. [📚 Coin và token — ranh giới video vẽ đúng nhưng vẽ nhanh](#2--coin-và-token--ranh-giới-video-vẽ-đúng-nhưng-vẽ-nhanh)
3. [Token ra đời từ một smart contract](#3-token-ra-đời-từ-một-smart-contract)
4. [Vì sao cần một chuẩn](#4-vì-sao-cần-một-chuẩn)
5. [Sáu hàm bắt buộc, ba thứ tuỳ chọn](#5-sáu-hàm-bắt-buộc-ba-thứ-tuỳ-chọn)
6. [📚 Video mô tả sai ba trong sáu hàm](#6--video-mô-tả-sai-ba-trong-sáu-hàm)
7. [📚 approve và transferFrom — vì sao phải hai bước](#7--approve-và-transferfrom--vì-sao-phải-hai-bước)
8. [📚 Hai cách mất tiền qua approve](#8--hai-cách-mất-tiền-qua-approve)
9. [Dễ tới mức nào](#9-dễ-tới-mức-nào)
10. [📚 Thời ICO — 4 tỷ USD và cái kết](#10--thời-ico--4-tỷ-usd-và-cái-kết)
11. [Token gửi nhầm là mất vĩnh viễn](#11-token-gửi-nhầm-là-mất-vĩnh-viễn)
12. [📚 ERC-223 và ERC-777 — bản vá hỏng, và bản vá chạy được](#12--erc-223-và-erc-777--bản-vá-hỏng-và-bản-vá-chạy-được)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Token là gì — và nó không phải cái gì

Video mở bằng đúng câu hỏi cần hỏi: *"ERC-20 token là gì, và quan trọng hơn: nó **không** phải cái gì?"* `00:00`

> `00:22` **"Token sống trên blockchain Ethereum. Chúng hưởng lợi từ công nghệ của Ethereum. Chúng KHÔNG độc lập — chúng dựa vào blockchain và nền tảng của Ethereum."**

Đây là câu quan trọng nhất của cả video và cũng là hiểu nhầm phổ biến nhất trong giới mới:

```
   NGƯỜI TA TƯỞNG                      THỰC TẾ
   ──────────────                      ───────
   "Đồng XYZ có blockchain riêng"      XYZ là một DÒNG trong bảng số dư
                                       của MỘT smart contract trên Ethereum

   "Ví tôi đang chứa 500 XYZ"          Ví bạn không chứa gì cả.
                                       Contract XYZ ghi: địa-chỉ-của-bạn → 500

   "XYZ có thợ đào riêng"              XYZ không có thợ đào, không có đồng thuận
                                       riêng. An ninh của nó = an ninh Ethereum.
```

Hệ quả rất cụ thể: **để chuyển token bạn vẫn phải trả phí bằng ETH.** Có một triệu token XYZ mà không có ETH thì không nhúc nhích được — đây là tình huống người mới gặp suốt.

Video cũng nêu đúng phổ ứng dụng ở `00:41`: token có thể hoạt động như tiền tệ, nhưng cũng có thể đại diện cho **cổ phần công ty, điểm thưởng khách hàng, chứng chỉ vàng**…

---

## 2. 📚 Coin và token — ranh giới video vẽ đúng nhưng vẽ nhanh

|                | **Coin**                | **Token**                              |
| -------------- | ----------------------- | -------------------------------------- |
| Sống ở đâu     | có blockchain riêng     | là trạng thái trong một smart contract |
| An ninh đến từ | đồng thuận của chính nó | đồng thuận của chuỗi mẹ                |
| Trả phí bằng   | chính nó                | **đồng gốc của chuỗi mẹ**              |
| Tạo mới tốn gì | dựng cả một mạng lưới   | vài phút, vài đô phí                   |
| Ví dụ          | BTC, ETH, SOL           | USDT, USDC, UNI, hầu hết mọi thứ       |

> 💡 **Đây là chỗ [Bài 9](lesson_9_tien_ma_hoa_toan_canh.md) từng đính chính video khác của cùng tác giả:** trong bài nói năm 2022, diễn giả chiếu sáu token phổ biến gồm **Dogecoin** rồi nói *"tôi tin tất cả đều dựng trên Ethereum"*. Sai — Dogecoin có blockchain riêng (nhánh từ Litecoin), nó là **coin**, không phải token. Bảng trên là cách kiểm tra: Dogecoin có thợ đào riêng, có phí trả bằng chính DOGE → coin.

Ranh giới này quyết định **rủi ro bạn đang gánh**. Cầm token nghĩa là bạn tin **hai** thứ: chuỗi mẹ, *và* đoạn code của contract token. Cầm coin thì chỉ tin một.

---

## 3. Token ra đời từ một smart contract

> `00:52` **"Token có thể được tạo ra bởi một smart contract. Contract này không chỉ tạo token mà còn quản lý các giao dịch của token và theo dõi số dư của từng người giữ."**

Ba việc trong một câu, và nó chính xác. Toàn bộ "token" chỉ là:

```
   contract HocCoin {
       tổng cung                          <- một con số
       số dư: map( địa chỉ -> số lượng )  <- một cuốn sổ
       + vài hàm để sửa cuốn sổ đó
   }
```

Không có gì hơn. Không có tệp tin, không có tài sản, không có mỏ. Chỉ là một cuốn sổ kế toán mà ai cũng đọc được và chỉ sửa được theo luật đã viết.

Video mô tả cách phát hành ở `01:05`: *bạn gửi Ether vào contract, contract trả lại cho bạn một lượng token*. Đây đúng là mô hình bán token thời 2017 — và nó cũng chính là cái bẫy ở [§11](#11-token-gửi-nhầm-là-mất-vĩnh-viễn).

Rồi video cảnh báo hai chuyện, cả hai đều đúng:

| Rủi ro                     | Video nói ở | Nội dung                                                                           |
| -------------------------- | ----------- | ---------------------------------------------------------------------------------- |
| **Không sửa được**         | `01:23`     | contract triển khai xong là bất biến — có lỗi cũng chịu. *"Có thể rất thảm khốc."* |
| **Không tương thích nhau** | `01:40`     | mỗi contract token một kiểu → sàn và ví phải viết mã riêng cho từng cái            |

Rủi ro thứ hai dẫn thẳng tới lý do ERC-20 tồn tại.

### 📚 Lý thuyết bổ sung: người ta làm token thế nào TRƯỚC khi có smart contract

Token không sinh ra cùng Ethereum. Từ **2012–2013**, khi Ethereum còn chưa tồn tại, người ta đã phát hành tài sản trên **Bitcoin** bằng một thủ thuật gọi là **colored coins** — "đồng có màu".

Cách làm rất đơn giản và cũng rất mong manh:

```
   1. Chọn một UTXO cụ thể, ví dụ 0,001 BTC ở giao dịch abc123 đầu ra số 0
   2. Tuyên bố: "0,001 BTC NÀY đại diện cho 1 cổ phần công ty X"
   3. Ghi tuyên bố đó lên chuỗi qua OP_RETURN (ô dữ liệu tuỳ ý của Bitcoin)
   4. Từ đó, ai cầm UTXO đó thì cầm cổ phần
```

Nghe hợp lý. Nhưng nó có một lỗ thủng không vá được:

> **Bitcoin không hề biết gì về "màu".**
> Chuỗi chỉ nhìn thấy satoshi. Toàn bộ luật về màu nằm trong **phần mềm ví**, tức là **ngoài chuỗi**.

Ba hệ quả, và cả ba đều chí mạng:

| Vấn đề | Chuyện gì xảy ra |
|---|---|
| **Ví không biết màu** | tiêu UTXO đó như satoshi thường → **tài sản bị huỷ vĩnh viễn**, không ai cản được |
| **Hai ví bất đồng** | mỗi bên cài luật màu hơi khác → hai bên tính ra hai chủ sở hữu khác nhau |
| **Không có trọng tài** | chuỗi không thể từ chối một giao dịch "sai màu", vì nó không biết màu là gì |

Đây chính xác là chỗ ERC-20 giải quyết được, và giải bằng một cách rất khác:

```
   COLORED COINS trên Bitcoin          ERC-20 trên Ethereum
   ──────────────────────────          ────────────────────
   kế toán nằm NGOÀI chuỗi             kế toán nằm TRONG chuỗi
   mỗi ví tự diễn giải                 contract là TRỌNG TÀI DUY NHẤT
   ví dốt phá được tài sản             không ví nào phá được sổ
   -> luật là một THOẢ THUẬN            -> luật là MÃ ĐANG CHẠY
```

Nói cách khác: **ERC-20 không phát minh ra token — nó phát minh ra chỗ để cất luật của token.**

> 🔄 **Và lịch sử lặp lại.** Năm 2023, Bitcoin quay lại trò này với Ordinals và chuẩn token BRC-20: ghi dữ liệu lên chuỗi rồi nhờ **các bộ đánh chỉ mục ngoài chuỗi** diễn giải xem ai sở hữu gì. Cùng một kiến trúc, và vì thế cùng một điểm yếu — số dư BRC-20 không do Bitcoin quyết định, mà do các indexer đồng ý với nhau. Ai đọc xong mục này sẽ biết chính xác phải hỏi câu gì về nó.

---

## 4. Vì sao cần một chuẩn

> `01:47` *"Mỗi contract token có thể khác nhau hoàn toàn. Nên nếu bạn muốn token của mình lên sàn, sàn phải viết mã riêng để nói chuyện được với contract của bạn. Ví cũng vậy. Hỗ trợ hàng trăm token sẽ vô cùng phức tạp và tốn thời gian."*

```
   KHÔNG CÓ CHUẨN                        CÓ CHUẨN
   ──────────────                        ────────
   sàn ──mã riêng──▶ token A             sàn ──┐
   sàn ──mã riêng──▶ token B                   ├─▶ CHUẨN ERC-20 ──▶ mọi token
   sàn ──mã riêng──▶ token C             ví ───┘
   ...  n token = n lần công việc        n token = 1 lần công việc
```

**ERC** = *Ethereum Request for Comments*, **20** là số hiệu của đề xuất `02:07`. Cái tên mượn từ RFC của internet — cùng một tinh thần: không ai ép, nhưng ai cũng theo vì theo thì có lợi.

Và video đưa ra phép so sánh hay nhất của nó ở `03:29`:

> **"Nếu bạn biết lập trình hướng đối tượng thì ERC-20 giống một *interface*. Muốn token của bạn là ERC-20 thì bạn phải cài đặt interface đó, và điều đó buộc bạn phải viết đủ 6 phương thức."**

Đó chính xác là bản chất: **ERC-20 không phải thư viện, không phải mã nguồn, không phải contract mẹ.** Nó là một bản hợp đồng về *hình dạng* — danh sách các hàm phải có, tên gì, nhận gì, trả gì. Ai cài thế nào là việc của người đó. [§6](#6--video-mô-tả-sai-ba-trong-sáu-hàm) và [§11](#11-token-gửi-nhầm-là-mất-vĩnh-viễn) cho thấy đó vừa là sức mạnh vừa là điểm yếu.

Kết quả thực tế, video nêu ở `04:03`: sàn và ví chỉ phải viết mã **một lần**. *"Đó là lý do sàn thêm token mới nhanh đến vậy, và vì sao các ví hỗ trợ mọi token ERC-20 mà không cần cập nhật."*

---

## 5. Sáu hàm bắt buộc, ba thứ tuỳ chọn

`02:22`. Đây là toàn bộ chuẩn.

### Ba thứ tuỳ chọn `02:28`

|            | Là gì                  | Ví dụ        |
| ---------- | ---------------------- | ------------ |
| `name`     | tên đầy đủ             | `"Hoc Coin"` |
| `symbol`   | mã ngắn                | `"HOC"`      |
| `decimals` | token chia nhỏ tới đâu | `18`         |

> ⚠️ **`decimals` là thứ tuỳ chọn nguy hiểm nhất trong toàn chuẩn.** Blockchain chỉ lưu **số nguyên**. Một token có `decimals = 18` nghĩa là "1 token" được ghi trong sổ là `1000000000000000000`. Nếu ứng dụng của bạn quên nhân, người dùng gửi 1 token sẽ chỉ chuyển đi **một phần tỉ tỉ** của một token.
>
> Và không phải token nào cũng dùng 18: USDT và USDC dùng **6**, WBTC dùng **8**. Hardcode số 18 là một lớp bug cả ngành từng dính.

### Sáu hàm bắt buộc

| Hàm                         | Làm gì                                          |
| --------------------------- | ----------------------------------------------- |
| `totalSupply()`             | tổng số token đang tồn tại                      |
| `balanceOf(chủ)`            | số dư của một địa chỉ                           |
| `transfer(đến, số)`         | **tôi** chuyển token **của tôi**                |
| `approve(người, số)`        | tôi **cho phép** người khác tiêu hộ tối đa `số` |
| `allowance(chủ, người)`     | người đó còn được tiêu hộ bao nhiêu             |
| `transferFrom(từ, đến, số)` | người được phép **rút** token của chủ           |

Video giới thiệu đủ sáu tên. Nhưng phần giải thích thì có vấn đề.

---

## 6. 📚 Video mô tả sai ba trong sáu hàm

Đây là lý do bài này tồn tại. Ba đoạn dưới đây là lời video, và cả ba đều không đúng.

### Sai 1 — `transfer` `02:57`

> ❌ *"`transfer` lấy một lượng token **từ tổng cung** rồi đưa cho người dùng."*

**Đúng:** `transfer` chuyển token **từ số dư của người gọi** sang người nhận. Nó **không đụng tới tổng cung** — tổng cung không đổi một chút nào. Cái mô tả sai kia thực ra là hành vi của hàm **đúc thêm** (`mint`), và `mint` **không** nằm trong chuẩn ERC-20.

Demo 1 xác nhận: sau khi chuyển 250 token, tổng cung vẫn y nguyên, chỉ hai số dư đổi chỗ.

### Sai 2 — `transferFrom` `03:01`

> ❌ *"`transferFrom` dùng để chuyển token **giữa hai người dùng bất kỳ** đang có token."*

**Đúng:** không phải "bất kỳ". `transferFrom` chỉ chạy được nếu người gọi **đã được chủ sở hữu cấp hạn mức** qua `approve`, và số rút không vượt hạn mức đó. Bỏ mất vế này là bỏ mất toàn bộ mô hình bảo mật của ERC-20 — nếu "bất kỳ ai chuyển token của bất kỳ ai" thì chuẩn này vô nghĩa.

### Sai 3 — `approve` và `allowance` `03:10`

> ❌ *"`approve` xác minh rằng contract của bạn có thể đưa một lượng token cho người dùng, **có tính tới tổng cung**. `allowance` gần như y hệt, chỉ khác là nó kiểm tra một người dùng có **đủ số dư** để gửi cho người khác không."*

**Đúng:** cả hai đều không liên quan gì tới tổng cung hay kiểm tra số dư.

```
   approve(nguoiDuocPhep, soTien)
       GHI vào sổ: "tôi cho phép <người đó> rút tối đa <số tiền> của tôi"
       Chỉ ghi một con số. Không kiểm tra gì. Không chuyển gì.

   allowance(chuSoHuu, nguoiDuocPhep)
       ĐỌC con số đó ra. Chỉ là một hàm tra cứu.
```

Đây không phải bắt bẻ chữ nghĩa. `approve` là **hàm nguy hiểm nhất của toàn bộ ERC-20** — gần như mọi vụ ví bị rút sạch token trong DeFi đều đi qua nó ([§8](#8--hai-cách-mất-tiền-qua-approve)). Hiểu nó là "một phép xác minh" thay vì "một sự uỷ quyền vô thời hạn" là hiểu ngược hoàn toàn mức rủi ro.

### Và một thứ video không nhắc: sự kiện

Chuẩn ERC-20 còn bắt buộc **hai sự kiện** (`event`) mà video bỏ qua:

```
   Transfer(từ, đến, số)      phát ra mỗi lần token đổi chủ
   Approval(chủ, người, số)   phát ra mỗi lần cấp hạn mức
```

Nghe như chi tiết vặt, nhưng **đây là cách cả thế giới nhìn thấy token của bạn**. Ví, sàn, trình duyệt chuỗi không đọc trực tiếp bảng số dư trong contract — chúng nghe các sự kiện này rồi tự dựng lại lịch sử. Token không phát sự kiện đúng chuẩn thì số dư hiển thị sai ở khắp nơi, dù logic bên trong hoàn toàn đúng.

---

## 7. 📚 approve và transferFrom — vì sao phải hai bước

Câu hỏi tự nhiên: đã có `transfer` rồi, thêm hai hàm nữa làm gì cho rối?

Vì **smart contract không tự lấy được token của bạn**.

```
   Token của An KHÔNG nằm trong ví An.
   Nó nằm trong sổ của contract HOC, ở dòng "An → 1000".

   Contract sàn muốn lấy 100 token đó thì phải GỌI contract HOC.
   Mà contract HOC chỉ nghe lời chủ sở hữu.
   -> An phải NÓI TRƯỚC với HOC rằng "cho sàn rút hộ tôi 100".
```

Nên mọi giao dịch DeFi đầu tiên với một token mới đều bắt bạn ký **hai lần** — demo 2:

```
  [buoc 1] An goi HOC.approve(san, 100)
           han muc san duoc rut: 100.0000
  [buoc 2] An goi san.swap() -> san goi HOC.transferFrom(An, san, 100)
           An   = 900.0000
           San  = 100.0000
           han muc con lai: 0.0000
```

Bây giờ thì cái hộp thoại *"Approve HOC"* rồi mới tới *"Confirm swap"* không còn là phiền phức vô cớ nữa — nó là hệ quả trực tiếp của việc token sống trong contract của nó chứ không trong ví bạn.

---

## 8. 📚 Hai cách mất tiền qua approve

### Cách 1 — Duyệt vô hạn

Vì mỗi lần `approve` là một giao dịch tốn phí, gần như mọi ứng dụng đều mặc định xin hạn mức **tối đa** (`2^256 − 1`) để bạn khỏi phải ký lại. Tiện. Và:

```
   Duyệt KHÔNG có hạn sử dụng.
   Bạn ký một lần năm 2021 → tới 2026 nó vẫn còn hiệu lực.
   Nó chỉ mất đi khi bạn CHỦ ĐỘNG gọi approve(..., 0).
```

Demo 3 diễn lại: An duyệt vô hạn cho một ứng dụng; sáu tháng sau ứng dụng bị chiếm quyền nâng cấp; kẻ tấn công gọi `transferFrom` và quét sạch.

```
    An        = 0.0000
    KeTanCong = 10000.0000
```

**An không hề ký thêm gì cả.** Chữ ký duy nhất là chữ ký từ sáu tháng trước.

> 🛡️ **Việc nên làm định kỳ:** rà soát và thu hồi các hạn mức cũ. Trình duyệt chuỗi và một số công cụ chuyên dụng liệt kê được toàn bộ hạn mức một địa chỉ đã cấp. Ví đang có nhiều token thì đây là việc bảo trì bắt buộc, không phải tuỳ chọn.

### Cách 2 — Chạy đua khi sửa hạn mức

Lỗi thiết kế kinh điển, có ngay trong bản chuẩn gốc. An đã duyệt cho Bob 100, giờ muốn hạ xuống 50. An gửi `approve(Bob, 50)` — giao dịch nằm chờ trong mempool, **ai cũng nhìn thấy**. Demo 4:

```
  Bob nhin thay giao dich do va CHEN LEN TRUOC:
    Bob rut 100 theo han muc CU  -> Bob = 100.0000
    giao dich cua An duoc dao -> han muc gio la 50
    Bob rut them 50              -> Bob = 150.0000

  -> An dinh cho toi da 100, Bob lay duoc 150.
```

Nguyên nhân: `approve` **đặt lại** hạn mức thành giá trị mới chứ không cộng/trừ, và giữa lúc bạn quyết định giảm với lúc giao dịch được đào có một khoảng trống mà đối phương chen vào được. Đây là một dạng của **MEV** ([Bài 3](../ly_thuyet/lesson_3_smart_contract.md)).

Cách né được khuyến nghị từ lâu: **đặt về 0 trước, xác nhận, rồi mới đặt giá trị mới.** Nhiều token bổ sung thêm `increaseAllowance`/`decreaseAllowance` để tránh hẳn khoảng trống này — nhưng chúng **không nằm trong chuẩn**, nên không phải token nào cũng có.

---

## 9. Dễ tới mức nào

Video kể ở `04:13` về một trang web tạo token: điền tổng cung, tên, số chữ số thập phân, ký hiệu — bấm nút, xong, contract được đưa lên blockchain.

> `04:33` *"Cực kỳ dễ và gần như không tốn công sức."*

Rồi đưa hệ quả `04:36`: trình duyệt chuỗi khi đó liệt kê **36.000** token ERC-20, và năm 2017 hơn **4 tỷ USD** được gọi vốn qua bán token.

```
   Chi phí tạo một token ERC-20 ≈ vài phút + vài đô phí
   Chi phí để token đó có GIÁ TRỊ ≈ vô cùng lớn
   -> khoảng cách giữa hai con số này là toàn bộ ngành lừa đảo token
```

Video thẳng thắn ở `04:51`: *"những token này không phải lúc nào cũng sạch. Một số bị thổi phồng quá mức, và rất nhiều người bị lừa mua những token về cơ bản là vô giá trị."*

> **Tới 2026 con số 36.000 đã lạc hậu tới mức vô nghĩa** — số contract token trên Ethereum lớn hơn nhiều lần, và nếu tính cả các chuỗi tương thích EVM khác thì không còn ai buồn đếm. Nhưng con số đó chưa bao giờ có ý nghĩa: nó đo *số lần có người bấm nút*, không đo cái gì khác. Đây đúng là chuyện [Bài 10 §20](lesson_10_tai_chinh_phi_tap_trung.md#20--kiểm-lại-bốn-con-số-của-video) đã nói với con số *"97% token trên sàn phi tập trung là bẫy"*: **đếm theo số token thì gần như tất cả là rác; đếm theo khối lượng giao dịch thì tập trung ở một nhúm.**

---

## 10. 📚 Thời ICO — 4 tỷ USD và cái kết

Video ghi hình ngay đỉnh sóng, nên nó nói về ICO như một hiện tượng đang diễn ra. Đây là phần kết mà video không thể biết.

**ICO** — *Initial Coin Offering* — hoạt động thế này:

```
   1. Viết một whitepaper mô tả dự án
   2. Tạo token ERC-20 (vài phút)
   3. Bán token lấy ETH, hứa rằng token sẽ dùng được trong sản phẩm tương lai
   4. Sản phẩm tương lai... tuỳ
```

Điểm mấu chốt: bước 2 gần như miễn phí, còn bước 3 thì **không cần xin phép ai**. Cả một thị trường vốn mọc lên bên ngoài mọi khuôn khổ chứng khoán — trong khoảng hai năm.

Diễn biến sau đó:

| Giai đoạn   | Chuyện gì xảy ra                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| 2017–2018   | Đỉnh sóng. Số tiền gọi được năm 2018 còn lớn hơn 2017                                                                     |
| 2018–2019   | Cơ quan quản lý Mỹ bắt đầu coi phần lớn token bán ra là **chứng khoán chưa đăng ký**; hàng loạt vụ phạt và buộc hoàn tiền |
| 2019 trở đi | Mô hình ICO chết. Thay bằng bán qua sàn, bán trên sàn phi tập trung, và **airdrop**                                       |
| Tới 2026    | Phát token vẫn sống khoẻ, nhưng gần như không ai gọi nó là ICO nữa                                                        |

> 📌 **Bài học không nằm ở chỗ "ICO là lừa đảo".** Nó nằm ở chỗ: **một chuẩn kỹ thuật đủ tốt có thể tạo ra một thị trường tài chính mới nhanh hơn tốc độ luật pháp phản ứng.** ERC-20 chỉ là sáu hàm và hai sự kiện. Nó không có ý định làm ra chuyện đó. [Bài 9 §20](lesson_9_tien_ma_hoa_toan_canh.md#20--pháp-lý-và-thuế--trạng-thái-2026) nói tiếp về phần pháp lý.

---

## 11. Token gửi nhầm là mất vĩnh viễn

Từ `05:06`, video quay lại phê bình chính chuẩn nó vừa khen:

> *"ERC-20 chỉ là một **hướng dẫn**, và người ta tự do cài đặt các hàm bắt buộc theo cách họ muốn. Điều đó dẫn tới vài vấn đề thú vị."*

Vấn đề cụ thể `05:17`: để mua token bạn phải gửi **ether** vào contract token. Nhưng có người gửi nhầm **token ERC-20 khác** vào đó. Contract không được thiết kế để xử lý chuyện này → **token bị mất**.

> `05:31` *"Ước tính tới tháng 12/2017, hơn **3 triệu USD** đã mất vì lỗi này."*

Demo 5 diễn lại và giải thích **vì sao chuẩn không thể chặn**:

```
  So sach token: contract dang giu 500.0000 HOC
  Contract co ham nao goi HOC.transfer(...) khong?  KHONG.
  -> So token do nam trong so mai mai. Khong ai lay ra duoc.
```

Cơ chế gốc rễ:

```
   Gửi ETH cho contract   -> MỘT HÀM của contract đó ĐƯỢC GỌI
                             -> contract biết, và có thể TỪ CHỐI

   Gửi token cho contract -> chỉ là contract TOKEN sửa hai con số trong sổ
                             -> contract nhận KHÔNG HỀ BIẾT
                             -> không có gì để từ chối
```

Contract nhận không được thông báo, không chạy dòng mã nào, không có cơ hội nói "tôi không nhận thứ này". Và vì nó không có hàm nào gọi `transfer` của token đó, số token ấy nằm trong sổ **vĩnh viễn**.

> 💥 **Đây không phải lỗi cài đặt của một ai — đây là lỗ hổng trong chính thiết kế chuẩn.** Nó vẫn tồn tại tới 2026, và số tiền kẹt trong các contract token đã lớn hơn con số 3 triệu của năm 2017 rất nhiều lần.

---

## 12. 📚 ERC-223 và ERC-777 — bản vá hỏng, và bản vá chạy được

Video kết ở `05:39`: cộng đồng đang làm **ERC-223** để mở rộng ERC-20, *"cảnh báo người tạo token về rủi ro này và đưa ra vài cách né"*.

Gần một thập kỷ sau, đây là kết cục — và nó không đi theo hướng video nghĩ.

### ERC-223 — chưa bao giờ được dùng

Ý tưởng: khi token được gửi tới một địa chỉ **là contract**, bắt buộc gọi một hàm "báo nhận" ở phía người nhận. Contract không cài hàm đó thì **giao dịch bị huỷ** — tiền quay về, không mất.

Đúng về kỹ thuật. Nhưng nó **phá tương thích ngược**: hàng nghìn contract đã tồn tại không có hàm báo nhận, và ERC-20 thì đã cắm rễ quá sâu vào mọi ví, mọi sàn. ERC-223 không bao giờ vượt qua được ngưỡng đó.

### ERC-777 — được duyệt, rồi hoá ra tệ hơn

Chuẩn kế tiếp cùng ý tưởng, có thêm cơ chế móc nối (*hook*) gọi vào cả người gửi lẫn người nhận, và **có tương thích ngược** với ERC-20. Nó được chuẩn hoá chính thức.

Vấn đề: cái móc nối đó **trao quyền điều khiển cho một contract khác ngay giữa chừng một lần chuyển token**. Nghe quen chưa? Đó chính là điều kiện của **reentrancy** — lỗi đã hạ The DAO năm 2016 ([Bài 3](../ly_thuyet/lesson_3_smart_contract.md), [Bài 10 §16](lesson_10_tai_chinh_phi_tap_trung.md#16--dao-trong-thực-tế--the-dao-constitutiondao-và-bài-toán-bỏ-phiếu)).

Năm 2020, một sàn phi tập trung bị rút mất tiền qua đúng đường này: token dạng ERC-777 được nạp vào một hồ thanh khoản viết theo giả định của ERC-20, cái móc nối cho phép kẻ tấn công gọi ngược vào hồ trước khi sổ sách kịp cập nhật.

```
   ERC-20  : an toàn nhưng câm  -> token gửi nhầm thì mất
   ERC-223 : chữa được, nhưng phá tương thích -> không ai dùng
   ERC-777 : chữa được, giữ tương thích -> MỞ CỬA CHO REENTRANCY

   -> Tới 2026, ERC-20 vẫn là chuẩn thống trị, kèm nguyên lỗ hổng cũ.
```

> 🔍 **Bài học kiến trúc, đáng nhớ hơn cả chi tiết kỹ thuật:** một chuẩn đã có hiệu ứng mạng đủ lớn thì **gần như không thể thay thế, kể cả khi ai cũng biết nó có lỗi**. Cách duy nhất còn lại là xây thêm ở bên cạnh, không phải thay thế.

### Cái thật sự được dùng: duyệt bằng chữ ký

Bản mở rộng thành công nhất của ERC-20 không nhắm vào lỗ hổng gửi nhầm, mà nhắm vào **phiền toái hai bước** ở [§7](#7--approve-và-transferfrom--vì-sao-phải-hai-bước).

Ý tưởng: thay vì gửi một giao dịch `approve` tốn phí, chủ sở hữu **ký một thông điệp ngoài chuỗi** cho phép rút, kèm hạn dùng. Ứng dụng cầm chữ ký đó nộp kèm luôn trong giao dịch chính.

```
   CŨ:  ký giao dịch approve (tốn phí, chờ đào)  →  ký giao dịch swap
   MỚI: ký một thông điệp (miễn phí, tức thì)    →  ký giao dịch swap
        + chữ ký CÓ HẠN SỬ DỤNG -> chữa luôn bệnh duyệt vô hạn ở §8
```

Đây là hướng đi đúng, và nó minh hoạ lại nhận xét ở trên: người ta không sửa ERC-20, người ta **bọc thêm một lớp bên ngoài nó**.

---

## 13. Code minh hoạ

Cài đủ sáu hàm bắt buộc, rồi phá ba chỗ chuẩn không chặn được.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
/**
 * Bài 12 — ERC-20: cài đúng 6 hàm bắt buộc, rồi phá từng chỗ.
 * Chạy: node demo.ts   (Node 22.6+, không cần cài gì)
 */
import { strict as assert } from "node:assert";

/** Token có 18 chữ số thập phân -> mọi phép tính dùng BigInt, không dùng number. */
const E18 = 10n ** 18n;
const fmt = (n: bigint): string => {
  const whole = n / E18, frac = (n % E18).toString().padStart(18, "0").slice(0, 4);
  return `${whole}.${frac}`;
};

/* ===========================================================================
 * 1. Sáu hàm bắt buộc của ERC-20 — toàn bộ chuẩn nằm gọn ở đây
 * ======================================================================== */
class ERC20 {
  readonly name: string;
  readonly symbol: string;
  readonly decimals = 18;
  private supply: bigint;
  private balances = new Map<string, bigint>();
  private allowances = new Map<string, Map<string, bigint>>();
  eventLog: string[] = [];

  constructor(name: string, symbol: string, initialSupply: bigint, owner: string) {
    this.name = name;
    this.symbol = symbol;
    this.supply = initialSupply;
    this.balances.set(owner, initialSupply);
  }

  /* --- 6 hàm BẮT BUỘC ------------------------------------------------- */
  totalSupply(): bigint {
    return this.supply;
  }

  balanceOf(account: string): bigint {
    return this.balances.get(account) ?? 0n;
  }

  /** Tôi tự chuyển tiền của tôi. */
  transfer(caller: string, to: string, amount: bigint): boolean {
    assert(this.balanceOf(caller) >= amount, "khong du so du");
    this.balances.set(caller, this.balanceOf(caller) - amount);
    this.balances.set(to, this.balanceOf(to) + amount);
    this.eventLog.push(`Transfer ${caller} -> ${to}: ${fmt(amount)}`);
    return true;
  }

  /** Tôi CHO PHÉP người khác tiêu hộ tối đa `amount`. */
  approve(owner: string, spender: string, amount: bigint): boolean {
    if (!this.allowances.has(owner)) this.allowances.set(owner, new Map());
    this.allowances.get(owner)!.set(spender, amount);
    this.eventLog.push(`Approval ${owner} cho ${spender}: ${fmt(amount)}`);
    return true;
  }

  /** Còn được tiêu hộ bao nhiêu. */
  allowance(owner: string, spender: string): bigint {
    return this.allowances.get(owner)?.get(spender) ?? 0n;
  }

  /** Người được phép rút tiền của chủ sở hữu. */
  transferFrom(caller: string, from: string, to: string, amount: bigint): boolean {
    const remaining = this.allowance(from, caller);
    assert(remaining >= amount, `han muc khong du: con ${fmt(remaining)}, can ${fmt(amount)}`);
    assert(this.balanceOf(from) >= amount, "chu so huu khong du so du");
    this.allowances.get(from)!.set(caller, remaining - amount);
    this.balances.set(from, this.balanceOf(from) - amount);
    this.balances.set(to, this.balanceOf(to) + amount);
    this.eventLog.push(`TransferFrom ${caller} rut ${fmt(amount)} tu ${from} -> ${to}`);
    return true;
  }
}

console.log("=== 1. Sau ham bat buoc ===");
{
  const token = new ERC20("Hoc Coin", "HOC", 1_000_000n * E18, "An");
  console.log(`  ${token.name} (${token.symbol}), ${token.decimals} chu so thap phan`);
  console.log(`  totalSupply()        = ${fmt(token.totalSupply())}`);
  console.log(`  balanceOf("An")      = ${fmt(token.balanceOf("An"))}`);
  token.transfer("An", "Binh", 250n * E18);
  console.log(`  sau transfer 250:`);
  console.log(`    An   = ${fmt(token.balanceOf("An"))}`);
  console.log(`    Binh = ${fmt(token.balanceOf("Binh"))}`);
  console.log(`  Tong cung KHONG doi  = ${fmt(token.totalSupply())}  <- transfer chi DOI CHO`);
  assert(token.balanceOf("An") + token.balanceOf("Binh") === token.totalSupply());
}

/* ===========================================================================
 * 2. Vì sao cần approve + transferFrom, thay vì chỉ transfer
 * ======================================================================== */
console.log("\n=== 2. approve + transferFrom: vi sao phai HAI buoc ===");
{
  const token = new ERC20("Hoc Coin", "HOC", 1_000n * E18, "An");
  console.log("  An muon doi 100 HOC lay ETH tren mot san phi tap trung.");
  console.log("  Van de: smart contract KHONG TU LAY duoc token cua An.");
  console.log("          Token nam trong so cua contract HOC, khong nam trong vi An.\n");
  console.log("  [buoc 1] An goi HOC.approve(san, 100)");
  token.approve("An", "SanDEX", 100n * E18);
  console.log(`           han muc san duoc rut: ${fmt(token.allowance("An", "SanDEX"))}`);
  console.log("  [buoc 2] An goi san.swap() -> san goi HOC.transferFrom(An, san, 100)");
  token.transferFrom("SanDEX", "An", "SanDEX", 100n * E18);
  console.log(`           An   = ${fmt(token.balanceOf("An"))}`);
  console.log(`           San  = ${fmt(token.balanceOf("SanDEX"))}`);
  console.log(`           han muc con lai: ${fmt(token.allowance("An", "SanDEX"))}\n`);
  console.log("  -> Day la ly do moi giao dich DeFi dau tien luon bat ban ky HAI lan.");
  assert(token.allowance("An", "SanDEX") === 0n);
}

/* ===========================================================================
 * 3. Duyệt vô hạn — tiện, và là cửa sau mở sẵn
 * ======================================================================== */
console.log("\n=== 3. Duyet VO HAN: tien loi doi lay rui ro ===");
{
  const token = new ERC20("Hoc Coin", "HOC", 10_000n * E18, "An");
  const MAX_UINT256 = 2n ** 256n - 1n;
  console.log("  De khoi phai ky lai moi lan, ung dung xin duyet VO HAN:");
  token.approve("An", "UngDung", MAX_UINT256);
  console.log(`  han muc = 2^256-1  (~${MAX_UINT256.toString().length} chu so)\n`);
  console.log("  Sau 6 thang, ung dung bi chiem quyen nang cap / doi chu:");
  token.transferFrom("UngDung", "An", "KeTanCong", token.balanceOf("An"));
  console.log(`    An        = ${fmt(token.balanceOf("An"))}`);
  console.log(`    KeTanCong = ${fmt(token.balanceOf("KeTanCong"))}`);
  console.log("\n  -> Duyet KHONG HET HAN. Ban ky mot lan nam 2021, no van song nam 2026.");
  console.log("     Han muc chi mat di khi ban chu dong goi approve(..., 0).");
  assert(token.balanceOf("An") === 0n);
}

/* ===========================================================================
 * 4. Lỗi kinh điển của approve — chạy đua sửa hạn mức
 * ======================================================================== */
console.log("\n=== 4. Loi chay dua khi SUA han muc ===");
{
  const token = new ERC20("Hoc Coin", "HOC", 1_000n * E18, "An");
  token.approve("An", "Bob", 100n * E18);
  console.log("  An da duyet cho Bob 100. Gio An muon HA xuong 50.");
  console.log("  An gui giao dich approve(Bob, 50) -> no nam CHO trong mempool.\n");
  console.log("  Bob nhin thay giao dich do va CHEN LEN TRUOC:");
  token.transferFrom("Bob", "An", "Bob", 100n * E18);
  console.log(`    Bob rut 100 theo han muc CU  -> Bob = ${fmt(token.balanceOf("Bob"))}`);
  token.approve("An", "Bob", 50n * E18);
  console.log("    giao dich cua An duoc dao -> han muc gio la 50");
  token.transferFrom("Bob", "An", "Bob", 50n * E18);
  console.log(`    Bob rut them 50              -> Bob = ${fmt(token.balanceOf("Bob"))}`);
  console.log("\n  -> An dinh cho toi da 100, Bob lay duoc 150.");
  console.log("     Vi vay chuan khuyen: dat ve 0 truoc, roi moi dat gia tri moi.");
  assert(token.balanceOf("Bob") === 150n * E18);
}

/* ===========================================================================
 * 5. Gửi token vào một contract không biết nhận -> mất vĩnh viễn
 *    Đây là lỗ hổng video nêu (~3 triệu USD tính tới 12/2017).
 * ======================================================================== */
console.log("\n=== 5. Token gui nham vao contract = mat vinh vien ===");
{
  const token = new ERC20("Hoc Coin", "HOC", 1_000_000n * E18, "An");
  // Contract nay chi biet nhan ETH. No khong he co ham nao dong toi token HOC.
  const CONTRACT = "0xContractWithNoTokenSupport";
  console.log("  Nguoi dung muon MUA token, dang le phai gui ETH vao contract.");
  console.log("  Nhung ho lai goi HOC.transfer(contract, 500) — gui thang TOKEN.\n");
  token.transfer("An", CONTRACT, 500n * E18);
  console.log(`  So sach token: contract dang giu ${fmt(token.balanceOf(CONTRACT))} HOC`);
  console.log("  Contract co ham nao goi HOC.transfer(...) khong?  KHONG.");
  console.log("  -> So token do nam trong so mai mai. Khong ai lay ra duoc.\n");
  console.log("  Vi sao ERC-20 khong chan duoc:");
  console.log("    transfer() chi la SUA HAI CON SO trong so cua contract token.");
  console.log("    Contract nhan KHONG HE BIET co chuyen gi vua xay ra —");
  console.log("    khong co ham nao cua no duoc goi. Khong the tu choi thu minh khong thay.");
  console.log("\n  Ban va: ERC-223/ERC-777 goi mot ham 'bao nhan' o phia nguoi nhan,");
  console.log("  contract khong cai ham do thi giao dich BI HUY thay vi mat tien.");
  const lockedForever = token.balanceOf(CONTRACT);
  console.log(`\n  Ty le cung bi khoa cung: ${(Number(lockedForever * 10000n / token.totalSupply()) / 100).toFixed(2)}%`);
  assert(lockedForever === 500n * E18);
}

console.log("\nXong. 6 ham chuan + 3 cach mat tien ma chuan khong chan duoc.");
```

Kết quả chạy thật:

```
=== 1. Sau ham bat buoc ===
  Hoc Coin (HOC), 18 chu so thap phan
  totalSupply()        = 1000000.0000
  balanceOf("An")      = 1000000.0000
  sau transfer 250:
    An   = 999750.0000
    Binh = 250.0000
  Tong cung KHONG doi  = 1000000.0000  <- transfer chi DOI CHO

=== 2. approve + transferFrom: vi sao phai HAI buoc ===
  An muon doi 100 HOC lay ETH tren mot san phi tap trung.
  Van de: smart contract KHONG TU LAY duoc token cua An.
          Token nam trong so cua contract HOC, khong nam trong vi An.

  [buoc 1] An goi HOC.approve(san, 100)
           han muc san duoc rut: 100.0000
  [buoc 2] An goi san.swap() -> san goi HOC.transferFrom(An, san, 100)
           An   = 900.0000
           San  = 100.0000
           han muc con lai: 0.0000

  -> Day la ly do moi giao dich DeFi dau tien luon bat ban ky HAI lan.

=== 3. Duyet VO HAN: tien loi doi lay rui ro ===
  De khoi phai ky lai moi lan, ung dung xin duyet VO HAN:
  han muc = 2^256-1  (~78 chu so)

  Sau 6 thang, ung dung bi chiem quyen nang cap / doi chu:
    An        = 0.0000
    KeTanCong = 10000.0000

  -> Duyet KHONG HET HAN. Ban ky mot lan nam 2021, no van song nam 2026.
     Han muc chi mat di khi ban chu dong goi approve(..., 0).

=== 4. Loi chay dua khi SUA han muc ===
  An da duyet cho Bob 100. Gio An muon HA xuong 50.
  An gui giao dich approve(Bob, 50) -> no nam CHO trong mempool.

  Bob nhin thay giao dich do va CHEN LEN TRUOC:
    Bob rut 100 theo han muc CU  -> Bob = 100.0000
    giao dich cua An duoc dao -> han muc gio la 50
    Bob rut them 50              -> Bob = 150.0000

  -> An dinh cho toi da 100, Bob lay duoc 150.
     Vi vay chuan khuyen: dat ve 0 truoc, roi moi dat gia tri moi.

=== 5. Token gui nham vao contract = mat vinh vien ===
  Nguoi dung muon MUA token, dang le phai gui ETH vao contract.
  Nhung ho lai goi HOC.transfer(contract, 500) — gui thang TOKEN.

  So sach token: contract dang giu 500.0000 HOC
  Contract co ham nao goi HOC.transfer(...) khong?  KHONG.
  -> So token do nam trong so mai mai. Khong ai lay ra duoc.

  Vi sao ERC-20 khong chan duoc:
    transfer() chi la SUA HAI CON SO trong so cua contract token.
    Contract nhan KHONG HE BIET co chuyen gi vua xay ra —
    khong co ham nao cua no duoc goi. Khong the tu choi thu minh khong thay.

  Ban va: ERC-223/ERC-777 goi mot ham 'bao nhan' o phia nguoi nhan,
  contract khong cai ham do thi giao dich BI HUY thay vi mat tien.

  Ty le cung bi khoa cung: 0.05%

Xong. 6 ham chuan + 3 cach mat tien ma chuan khong chan duoc.
```

**Tự thử:**

1. Thêm `increaseAllowance` / `decreaseAllowance` vào lớp `ERC20`, rồi viết lại demo 4 dùng chúng. Lỗi chạy đua còn không?
2. Thêm hai sự kiện `Transfer` và `Approval` (đẩy vào `eventLog`), rồi viết hàm dựng lại số dư **chỉ từ nhật ký sự kiện**. Đó chính là cách ví và trình duyệt chuỗi làm việc.
3. Đổi `decimals` thành 6 (như USDT) nhưng giữ nguyên `E18` trong phần tính toán. Xem số dư sai lệch bao nhiêu lần — đây là bug thật của cả một thế hệ ứng dụng.
4. Cài một biến thể ERC-223: `transfer` kiểm tra người nhận có nằm trong danh sách "contract biết nhận token" không, không có thì `assert` cho hỏng. Demo 5 giờ ra kết quả gì?

---

## 14. Từ điển thuật ngữ

| Tiếng Anh         | Tiếng Việt                    | Nghĩa gọn                                                |
| ----------------- | ----------------------------- | -------------------------------------------------------- |
| Token             | token                         | tài sản là trạng thái trong một smart contract           |
| Coin              | đồng gốc                      | tài sản có blockchain riêng                              |
| ERC               | Ethereum Request for Comments | quy trình đề xuất chuẩn của Ethereum                     |
| ERC-20            | chuẩn token thay thế được     | 6 hàm + 2 sự kiện bắt buộc                               |
| Interface         | giao diện                     | bản hợp đồng về *hình dạng*, không phải mã cài sẵn       |
| `totalSupply`     | tổng cung                     | tổng token đang tồn tại                                  |
| `balanceOf`       | số dư                         | token của một địa chỉ                                    |
| `transfer`        | chuyển                        | tôi chuyển token của tôi                                 |
| `approve`         | duyệt hạn mức                 | cho phép người khác rút hộ                               |
| `allowance`       | hạn mức còn lại               | tra cứu số còn được rút                                  |
| `transferFrom`    | rút theo uỷ quyền             | người được duyệt rút token của chủ                       |
| `decimals`        | số chữ số thập phân           | 18 với đa số, 6 với USDT/USDC, 8 với WBTC                |
| Event             | sự kiện                       | thứ ví và trình duyệt chuỗi thật sự đọc                  |
| Infinite approval | duyệt vô hạn                  | hạn mức `2^256−1`, không hết hạn                         |
| Front-running     | chen lệnh                     | thấy giao dịch trong mempool rồi chèn lên trước          |
| ICO               | phát hành token lần đầu       | bán token gọi vốn, không xin phép ai                     |
| Rug pull          | rút thảm                      | bán token xong ôm tiền biến mất                          |
| Reentrancy        | gọi ngược                     | contract bị gọi lại giữa chừng khi sổ sách chưa cập nhật |

---

## 15. Câu hỏi tự kiểm tra

1. Token ERC-20 "sống" ở đâu? Vì sao có một triệu token mà không có ETH thì không chuyển được?
2. Nêu ba khác biệt giữa coin và token. Dogecoin thuộc loại nào, và làm sao kiểm tra?
3. Cầm token nghĩa là bạn tin bao nhiêu thứ? Cầm coin thì bao nhiêu?
4. Trước khi có ERC-20, một sàn muốn hỗ trợ 100 token phải làm gì?
5. Vì sao nói ERC-20 giống *interface* chứ không phải thư viện?
6. Video nói `transfer` "lấy token từ tổng cung". Sai ở đâu? Hàm nào mới làm việc đó, và nó có trong chuẩn không?
7. Video nói `transferFrom` chuyển được token "giữa hai người bất kỳ". Thiếu điều kiện gì?
8. `approve` thật sự làm gì? Nó có kiểm tra số dư hay tổng cung không?
9. ERC-20 bắt buộc hai sự kiện nào? Vì sao thiếu chúng thì số dư hiển thị sai khắp nơi dù logic đúng?
10. Vì sao smart contract không tự lấy được token của bạn, dẫn tới phải có `approve` + `transferFrom`?
11. Duyệt vô hạn tiện ở chỗ nào và nguy hiểm ở chỗ nào? Nó hết hạn khi nào?
12. Mô tả lỗi chạy đua khi sửa hạn mức. An định cho tối đa 100, Bob lấy được bao nhiêu, bằng cách nào?
13. Cách né lỗi đó là gì? Vì sao `increaseAllowance` không giải quyết được cho *mọi* token?
14. `decimals` của USDT là bao nhiêu? Ứng dụng hardcode 18 sẽ hỏng thế nào?
15. Vì sao gửi ETH vào contract thì contract từ chối được, còn gửi token thì không?
16. Số token gửi nhầm vào contract có mất khỏi `totalSupply` không? Nếu không thì nó ở đâu?
17. ERC-223 đúng về kỹ thuật nhưng không ai dùng. Vì sao?
18. ERC-777 chữa được lỗi và giữ tương thích ngược, nhưng lại tạo ra lỗ hổng gì? Lỗ hổng đó đã hạ tổ chức nào năm 2016?
19. Phát biểu bài học kiến trúc rút ra từ ba chuẩn 20/223/777.
20. Duyệt bằng chữ ký ngoài chuỗi giải quyết được hai vấn đề nào cùng lúc?
21. Tạo một token ERC-20 tốn bao nhiêu? Vì sao con số "36.000 token" trong video không nói lên điều gì?
22. Mô hình ICO chết vì lý do gì, và bị thay bằng gì?
23. Câu "một chuẩn kỹ thuật có thể tạo ra thị trường tài chính mới nhanh hơn tốc độ luật pháp phản ứng" — minh hoạ bằng đúng trường hợp ERC-20.

---

## Tóm tắt một trang

```
 ┌──────────────────────────────────────────────────────────────────────┐
 │  ERC-20 = 6 hàm + 2 sự kiện. Chỉ có thế. Và nó đỡ gần như cả DeFi.  │
 └──────────────────────────────────────────────────────────────────────┘

  TOKEN KHÔNG PHẢI COIN
    token = một DÒNG trong sổ của một smart contract
    không có chuỗi riêng, không thợ đào riêng, phí trả bằng ETH
    -> cầm token = tin HAI thứ: chuỗi mẹ + code của contract

  SÁU HÀM BẮT BUỘC
    totalSupply()              tổng token đang tồn tại
    balanceOf(chủ)             số dư một địa chỉ
    transfer(đến, số)          tôi chuyển token CỦA TÔI
    approve(người, số)         cho phép người khác rút hộ
    allowance(chủ, người)      tra cứu hạn mức còn lại
    transferFrom(từ,đến,số)    người được duyệt đi rút
  + 2 SỰ KIỆN  Transfer, Approval   <- thứ ví/explorer thật sự đọc
  + 3 TUỲ CHỌN name, symbol, decimals

  ⚠️ VIDEO MÔ TẢ SAI 3/6 HÀM
    transfer     KHÔNG lấy từ tổng cung (đó là mint, không có trong chuẩn)
    transferFrom KHÔNG dùng cho "hai người bất kỳ" — phải có hạn mức trước
    approve      KHÔNG xác minh gì cả — nó GHI một sự uỷ quyền VÔ THỜI HẠN

  BA CÁCH MẤT TIỀN CHUẨN KHÔNG CHẶN
    1 duyệt vô hạn   ký 1 lần năm 2021, kẻ tấn công dùng năm 2026
    2 chạy đua sửa   định cho 100, đối phương lấy 150
    3 gửi nhầm token vào contract -> khoá cứng vĩnh viễn
      lý do: contract nhận KHÔNG HỀ BIẾT — không hàm nào của nó được gọi

  BA CHUẨN, MỘT BÀI HỌC
    ERC-20   an toàn nhưng câm      -> vẫn thống trị tới 2026
    ERC-223  phá tương thích        -> không ai dùng
    ERC-777  mở cửa reentrancy      -> gây hack năm 2020
    -> chuẩn đã có hiệu ứng mạng thì không thay được, chỉ bọc thêm bên ngoài
```

---

## Nguồn

- Video gốc: [ERC20 tokens — Simply Explained](https://www.youtube.com/watch?v=cqZhNzZoMh8) (6:04)
- [EIP-20 — bản chuẩn gốc](https://eips.ethereum.org/EIPS/eip-20) — đọc thẳng, chỉ khoảng hai trang
- [EIP-777](https://eips.ethereum.org/EIPS/eip-777) và [EIP-2612 — duyệt bằng chữ ký](https://eips.ethereum.org/EIPS/eip-2612)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts) — bản cài đặt được dùng nhiều nhất; đừng tự viết
- [Etherscan Token Approvals](https://etherscan.io/tokenapprovalchecker) — công cụ rà và thu hồi hạn mức cũ

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
10. [Bài 10 – DeFi: tài chính phi tập trung](lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. [Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning](lesson_11_fork_va_lightning.md) — fork, kênh thanh toán, HTLC, thanh khoản
12. **Bài 12 – ERC-20: chuẩn token** ← *bạn đang ở đây* — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
