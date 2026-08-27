# GDPR có giết blockchain không

> Bài học dựa trên video **"Will GDPR kill blockchains?"** (kênh *Simply Explained – Savjee*, YouTube `5I3wYAwbKMM`, 9:15).
>
> Đây là bài **duy nhất trong cả khoá học không nói về kỹ thuật blockchain**, mà nói về chỗ blockchain va vào luật. Nó cũng là bài kiểm tra cuối cùng cho một luận điểm chạy suốt 12 bài trước: *mật mã không phải chỗ vỡ.*
> Phần **📚 Lý thuyết bổ sung** làm hai việc: **chứng minh bằng code** rằng giải pháp trung tâm mà video đề xuất có một lỗ thủng, và cập nhật câu hỏi pháp lý tới 2026.
>
> ⚠️ **Video ghi giữa 2018**, ngay sau khi GDPR có hiệu lực, khi chưa có án lệ nào. [§10](#10--câu-hỏi-đó-được-trả-lời-ra-sao-tới-2026) đối chiếu.
>
> 📌 **Cần đọc trước:** [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) (tính bất biến), [Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md) (khung quyết định), [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md) (ZKP — chính là video mà tác giả hứa làm ở cuối bài này).

---

## Mục lục

1. [GDPR là gì, và vì sao nó đụng blockchain](#1-gdpr-là-gì-và-vì-sao-nó-đụng-blockchain)
2. [Ba khái niệm phải nắm trước](#2-ba-khái-niệm-phải-nắm-trước)
3. [Dữ liệu cá nhân rộng hơn bạn nghĩ — kể cả địa chỉ ví](#3-dữ-liệu-cá-nhân-rộng-hơn-bạn-nghĩ--kể-cả-địa-chỉ-ví)
4. [📚 Chứng minh: địa chỉ ví liên kết được tới người thật](#4--chứng-minh-địa-chỉ-ví-liên-kết-được-tới-người-thật)
5. [Ba điều luật đụng thẳng vào blockchain](#5-ba-điều-luật-đụng-thẳng-vào-blockchain)
6. [Bốn giải pháp video đề xuất](#6-bốn-giải-pháp-video-đề-xuất)
7. [📚 "Băm rồi thì hết là dữ liệu cá nhân" — chỗ giải pháp 3 gãy](#7--băm-rồi-thì-hết-là-dữ-liệu-cá-nhân--chỗ-giải-pháp-3-gãy)
8. [📚 Chấm điểm lại bốn giải pháp](#8--chấm-điểm-lại-bốn-giải-pháp)
9. [Ai là người chịu trách nhiệm](#9-ai-là-người-chịu-trách-nhiệm)
10. [📚 Câu hỏi đó được trả lời ra sao tới 2026](#10--câu-hỏi-đó-được-trả-lời-ra-sao-tới-2026)
11. [📚 Việt Nam — Nghị định 13/2023](#11--việt-nam--nghị-định-132023)
12. [📚 Nghịch lý cuối: ZKP vừa là lời giải vừa là vấn đề](#12--nghịch-lý-cuối-zkp-vừa-là-lời-giải-vừa-là-vấn-đề)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. GDPR là gì, và vì sao nó đụng blockchain

> `00:00` Ngày **25/5/2018**, một luật riêng tư mới có hiệu lực ở châu Âu: **GDPR** — Quy định chung về bảo vệ dữ liệu. Nó trao cho công dân EU quyền kiểm soát **ai được thu thập dữ liệu cá nhân của họ** và **chuyện gì xảy ra với dữ liệu đó**.

Video chỉ ra ba thứ ai cũng thấy hằng ngày mà không biết nguyên nhân: các hộp thoại xin phép cookie, các email hỏi *"bạn còn muốn nhận bản tin không"*, và việc các công ty đột nhiên cho bạn tải về dữ liệu của chính mình.

Rồi đặt câu hỏi của bài `00:38`:

> **"Thế còn công nghệ blockchain thì sao?"**

Vì hai tính chất làm nên blockchain lại là đúng hai tính chất GDPR không ưa `00:48`:

```
   THỨ LÀM BLOCKCHAIN CÓ GIÁ TRỊ        THỨ GDPR ĐÒI HỎI
   ─────────────────────────────        ─────────────────
   Dữ liệu ghi CÔNG KHAI, minh bạch  ↔  bạn kiểm soát ai xử lý dữ liệu của bạn
   Dữ liệu KHÔNG sửa, KHÔNG xoá được ↔  bạn có quyền sửa và quyền xoá
```

Và video nói thẳng ở `00:58`: *"chính hai tính chất này cho phép blockchain phân tán hoàn toàn mà không cần cơ quan trung ương. Nhưng cũng chính chúng nghe không hay chút nào khi nói tới quyền riêng tư."*

> `01:08` **"Vậy GDPR có giết blockchain không?"**

---

## 2. Ba khái niệm phải nắm trước

`01:17`. Video làm phần này rất gọn và chính xác.

| Khái niệm                                   | Là ai                                       | Ghi chú                                                      |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| **Data controller** — bên kiểm soát dữ liệu | bên **lưu trữ** dữ liệu của bạn             | **đây là bên chịu trách nhiệm tuân thủ** `01:33`             |
| **Data processor** — bên xử lý dữ liệu      | bên **làm việc** với dữ liệu (phân tích…)   | thường trùng với bên kiểm soát, nhưng có thể là công ty khác |
| **Phạm vi áp dụng**                         | dữ liệu cá nhân của **công dân EU** `01:37` | công ty nước ngoài cũng phải theo nếu có người dùng châu Âu  |

Hàng đầu tiên là hàng sẽ gây rắc rối lớn nhất — giữ lấy nó cho tới [§9](#9-ai-là-người-chịu-trách-nhiệm).

---

## 3. Dữ liệu cá nhân rộng hơn bạn nghĩ — kể cả địa chỉ ví

`01:55`. Định nghĩa trong luật:

> **"bất kỳ thông tin nào liên quan tới một thể nhân đã được nhận dạng hoặc **có thể nhận dạng được**."**

Video nhấn đúng chỗ: *"và cái đó thật ra rất rộng!"* Rồi dẫn dắt bằng một chuỗi ví dụ tăng dần độ khó `02:17`:

```
   Tên, tuổi, giới tính        -> rõ ràng là dữ liệu cá nhân
   Số điện thoại               -> ừ, cũng là
   Số thẻ tín dụng             -> vẫn là
   Địa chỉ IP máy tính         -> đây chỉ là mấy con số ngẫu nhiên mà?
                                  NHƯNG nhà mạng biết IP nào của khách nào
                                  -> LÀ dữ liệu cá nhân
```

Và cú đánh chính `02:35`:

> **"Điều tương tự áp dụng cho địa chỉ ví Bitcoin của bạn. Nó là một chuỗi chữ và số ngẫu nhiên không liên kết trực tiếp tới một con người. Nhưng nó **có thể liên kết gián tiếp** tới bạn nếu bạn từng mua Bitcoin bằng thẻ tín dụng hoặc qua một sàn giao dịch."**

> `02:49` **"Nói ngắn gọn: ngay cả những con số và chữ cái ngẫu nhiên cũng có thể là dữ liệu cá nhân, nếu chúng liên kết được tới một người cụ thể."**

Đây là điểm quan trọng nhất của cả video, và nó **đúng hoàn toàn**. Hệ quả rất nặng: nếu địa chỉ ví là dữ liệu cá nhân, thì **toàn bộ blockchain Bitcoin là một cơ sở dữ liệu chứa dữ liệu cá nhân**, không xoá được, được sao chép trên hàng chục nghìn máy khắp thế giới.

Mục sau chứng minh vế "liên kết gián tiếp" bằng code, vì nó dễ hơn nhiều so với cảm giác của người mới.

---

## 4. 📚 Chứng minh: địa chỉ ví liên kết được tới người thật

Video nói *"có thể liên kết gián tiếp"* rồi đi tiếp. Đây là cách nó thật sự diễn ra, và nó chỉ cần một suy luận duy nhất.

### Suy luận sở hữu đầu vào chung

Trong mô hình UTXO ([Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md)), một giao dịch có thể tiêu **nhiều đầu vào cùng lúc**. Muốn làm được thế thì phải **ký được tất cả chúng** — nghĩa là phải có khoá riêng của tất cả.

```
   Giao dịch: [ ví_A , ví_B ] ──▶ [ ví_shop ]
                 └──┬──┘
      cùng một người ký cả hai -> ví_A và ví_B CÙNG MỘT CHỦ
```

Cứ thế gom dần, các ví dính vào nhau thành **cụm**. Chạy demo 3:

```
  Cac cum suy ra duoc (moi cum = mot chu so huu):
    { wallet_A, wallet_B, wallet_C, wallet_G }
    { wallet_D }
    { wallet_E, wallet_F }
```

Chú ý: `wallet_A` và `wallet_G` **chưa bao giờ xuất hiện chung trong một giao dịch nào**. Chúng vẫn bị gom vào một cụm, qua `wallet_B` và `wallet_C`. Quan hệ này lan truyền.

### Một điểm rò là đủ

```
  Gia su san giao dich bi ro du lieu KYC: 'wallet_A thuoc ve Nguyen Van An'.
  -> Lo luon ca cum: wallet_A, wallet_B, wallet_C, wallet_G
     cung toan bo lich su giao dich cua chung, VINH VIEN, cong khai.
```

Chỉ cần **một** mối nối giữa danh tính thật và một địa chỉ trong cụm — một lần rút tiền từ sàn có KYC, một lần đăng địa chỉ nhận quyên góp lên mạng xã hội, một lần mua hàng có giao hàng tận nhà — là cả cụm lộ.

> 💥 **Và điểm khác biệt then chốt so với mọi vụ rò dữ liệu khác: bạn không thể xoá.** Cơ sở dữ liệu của một công ty bị rò thì công ty đó còn xoá được, còn thông báo được. Blockchain thì bản sao nằm trên hàng chục nghìn máy, vĩnh viễn, và **bất kỳ ai trong tương lai** cũng chạy lại được phân tích này trên toàn bộ lịch sử.
>
> Đây chính là thứ [Bài 9 §12](lesson_9_tien_ma_hoa_toan_canh.md#12--không-có-nút-quên-mật-khẩu-sống-với-tính-bất-khả-đảo) gọi là tính bất khả đảo, nhìn từ phía quyền riêng tư thay vì phía tiền bạc.

### 📚 Lý thuyết bổ sung: dust attack — buộc bạn tự khai ra cụm của mình

Cách gộp cụm ở trên là **bị động**: kẻ phân tích chỉ đọc chuỗi và chờ bạn tự để lộ. Có một cách **chủ động** rẻ hơn nhiều, và nó bẻ gãy đúng lời khuyên bảo mật phổ biến nhất.

Lời khuyên đó là: *"dùng một địa chỉ mới cho mỗi lần nhận tiền."* Đúng — nhưng chưa đủ.

```
   1. Kẻ tấn công gửi một khoản CỰC NHỎ (vài trăm satoshi — gọi là "bụi")
      tới hàng nghìn địa chỉ. Rẻ như cho.
      -> nó BIẾT nó đã gửi bụi vào địa chỉ nào

   2. Chờ.

   3. Ví của bạn gom UTXO để trả một khoản gì đó. Thuật toán chọn coin
      thường ưu tiên nhặt các UTXO nhỏ cho gọn sổ -> nó nhặt luôn hạt bụi.

      giao dịch: [ ví_thật_của_bạn , hạt_bụi_của_kẻ_tấn_công ] ──▶ ...
                        └────────────┬────────────┘
                     suy luận đầu vào chung -> CÙNG MỘT CHỦ

   4. Kẻ tấn công vừa nối được cụm của bạn vào một địa chỉ NÓ TỰ TẠO
      và đã dán nhãn sẵn.
```

Điểm tinh vi: **bạn không làm gì sai cả.** Ví của bạn hành xử hoàn toàn bình thường — nó tối ưu phí. Chính hành vi bình thường đó là thứ bị lợi dụng.

**Cách chống:** dùng chức năng *coin control* để đánh dấu UTXO lạ là **không được tiêu**. Ví tốt ngày nay tự cảnh báo khi có khoản bụi lạ chuyển vào. Nhưng phải chủ động — mặc định thì không.

#### Và đây là chỗ nó đụng thẳng vào GDPR

Đọc lại định nghĩa dữ liệu cá nhân ở [§3](#3-dữ-liệu-cá-nhân-rộng-hơn-bạn-nghĩ--kể-cả-địa-chỉ-ví) rồi nghĩ về chuỗi sự kiện trên:

> **Một bên thứ ba hoàn toàn xa lạ vừa tạo ra dữ liệu cá nhân về bạn, ghi vĩnh viễn lên một sổ cái công khai, mà bạn không hề đồng ý — và không ai xoá được.**

Toàn bộ khung GDPR giả định có một **bên kiểm soát dữ liệu** đi *thu thập* dữ liệu của bạn. Ở đây không ai thu thập gì cả: kẻ tấn công chỉ **gửi tiền cho bạn**, còn cái liên kết thì do **chính bạn** tạo ra khi tiêu tiền, và do **cả mạng lưới** ghi lại.

Hỏi lại ba câu ở [§9](#9-ai-là-người-chịu-trách-nhiệm) với tình huống này: ai là bên kiểm soát? Kẻ gửi bụi? Ví của bạn? Thợ đào ghi giao dịch? Không câu trả lời nào ổn.

> 💥 Đây là ví dụ sắc nhất trong cả bài cho thấy vì sao *"đừng đưa dữ liệu cá nhân lên chuỗi"* là **chưa đủ**: bạn không kiểm soát được việc người khác đưa dữ liệu về bạn lên đó.

---

## 5. Ba điều luật đụng thẳng vào blockchain

`03:04`. Video chỉ ra ba điều khoản có vấn đề.

| Điều                           | Quyền của bạn                              | Blockchain làm được không                              |
| ------------------------------ | ------------------------------------------ | ------------------------------------------------------ |
| **16** — chỉnh sửa `03:08`     | sửa dữ liệu sai, bổ sung dữ liệu thiếu     | ❌ **thêm** dữ liệu mới thì được, **sửa** thì không     |
| **17** — được quên `03:25`     | yêu cầu xoá dữ liệu của mình               | ❌ không xoá được, chấm hết                             |
| **18** — hạn chế xử lý `03:43` | cấm bên khác làm gì đó với dữ liệu của bạn | ❌ chuỗi công khai → ai cũng tải về và làm gì tuỳ thích |

Video rút ra kết luận thẳng thừng ở `03:36`:

> **"Nghĩa là blockchain không thể tuân thủ GDPR, và do đó chúng không được lưu dữ liệu cá nhân của công dân EU."**

Câu này đúng **với blockchain công khai, không sửa được, lưu dữ liệu cá nhân ở dạng thô**. Nó không có nghĩa là blockchain bị cấm — nó có nghĩa là **thiết kế phải tránh đưa dữ liệu cá nhân lên chuỗi**. Đó là điều bốn giải pháp tiếp theo cố làm.

---

## 6. Bốn giải pháp video đề xuất

`04:07`. Video đưa ra bốn hướng và tự chấm điểm khá công bằng.

### Giải pháp 1 — Mã hoá trước khi ghi lên chuỗi `04:11`

Ý tưởng: chỉ ai có khoá giải mã mới dùng được dữ liệu. Muốn "xoá" thì **huỷ khoá**, dữ liệu mã hoá coi như vô dụng.

Video tự phản biện ngay `04:33`:

> *"Ít nhất đó là cách người ta nhìn nhận ở Anh. Người khác lập luận rằng mã hoá mạnh vẫn **đảo ngược được** — máy tính ngày càng nhanh thì khả năng bẻ được mã và lộ lại dữ liệu càng cao. Có lẽ đây không phải giải pháp tốt lắm."*

> 🔍 Lập luận phản biện này còn nặng hơn video nghĩ, vì nó có tên riêng: **"thu hoạch bây giờ, giải mã sau"**. Kẻ tấn công tải về dữ liệu mã hoá hôm nay và chờ. Với dữ liệu bình thường thì chờ vô ích. Với **dữ liệu ghi vĩnh viễn trên một blockchain công khai** thì thời gian đứng về phía kẻ tấn công. Máy tính lượng tử là biến số dài hạn ở đây — [Bài 2](../ly_thuyet/lesson_2_ma_hoa_bat_doi_xung.md) phần hậu lượng tử.

### Giải pháp 2 — Blockchain có phép `04:50`

|             | Chuỗi công khai | Chuỗi có phép                   |
| ----------- | --------------- | ------------------------------- |
| Ai đọc được | ai cũng         | chỉ vài bên đã biết và được tin |
| Ai ghi được | ai cũng         | chỉ bên được cấp quyền          |

Video chấm: **giải quyết được Điều 18** (kiểm soát ai xử lý dữ liệu) `05:10`. Nhưng `05:17`: *"chuỗi có phép vẫn bất biến, nghĩa là vẫn không sửa và không xoá được, nên vẫn không tuân thủ Điều 16 và 17. Cũng không phải giải pháp thật sự."*

Đúng. Và có một câu hỏi khó chịu hơn mà video không hỏi: **nếu chỉ vài bên được tin đọc và ghi, thì vì sao cần blockchain thay vì một cơ sở dữ liệu có nhật ký kiểm toán?** [Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md) dựng hẳn một khung quyết định cho câu này.

### Giải pháp 3 — Dữ liệu để ngoài chuỗi, chỉ ghi con trỏ `05:30`

Đây là giải pháp video cho là tốt nhất, và cũng là giải pháp được dùng nhiều nhất ngoài đời:

```
   MÁY CHỦ (xoá được)                 BLOCKCHAIN (không xoá được)
   ──────────────────                 ───────────────────────────
   hồ sơ đầy đủ của An      ──băm──▶  hash: 7f3a9c...
                                      ↑ chống sửa: đối chiếu lại là biết
                                        máy chủ có bị đụng vào không

   Muốn "được quên"?  -> XOÁ hồ sơ trên máy chủ
                      -> hash trên chuỗi trỏ vào hư không, thành vô nghĩa
```

Video giải thích rất đúng vì sao dùng hash `05:52`: nó **một chiều**, và nó cho phép **kiểm tra máy chủ có bị sửa trộm không**.

Và điều đáng khen nhất: video **nhận ra rằng bản thân cái hash cũng là dữ liệu cá nhân** `06:15`:

> *"Cái hash lưu trong blockchain chỉ là một chuỗi chữ và số ngẫu nhiên, nhưng nó **được coi là dữ liệu cá nhân** vì nó liên kết được tới dữ liệu trên máy chủ."*

Rồi kết `06:25`: xoá dữ liệu gốc đi thì hash *"trở nên vô dụng và không còn được coi là dữ liệu cá nhân, vì nó trỏ vào hư không."*

**Đây là chỗ có lỗ thủng.** [§7](#7--băm-rồi-thì-hết-là-dữ-liệu-cá-nhân--chỗ-giải-pháp-3-gãy) chứng minh bằng code.

Video cũng tự nêu nhược điểm còn lại ở `06:39`: làm thế là **tập trung hoá lại một phần** hệ thống vốn được thiết kế để phi tập trung.

### Giải pháp 4 — Zero-knowledge proof `06:49`

> *"Công nghệ cho phép bạn chứng minh một điều là đúng mà không tiết lộ dữ liệu thật."*

Ví dụ của video: vào quán bar phải chứng minh trên 21 tuổi. Đưa chứng minh thư ra thì **lộ nhiều hơn mức cần** — ngày sinh chính xác, họ tên, số giấy tờ, địa chỉ. Với ZKP bạn chứng minh được đúng mệnh đề *"tôi trên 21"* và không gì hơn `07:25`.

> 😄 Video kết phần này bằng `07:39`: *"để lại bình luận nếu bạn muốn tôi làm một video về Zero Knowledge Proof!"* — **tác giả đã làm thật**, và đó chính là [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md) của khoá học này.

---

## 7. 📚 "Băm rồi thì hết là dữ liệu cá nhân" — chỗ giải pháp 3 gãy

Video lập luận: hàm băm là một chiều, nên từ hash không lấy lại được dữ liệu; xoá dữ liệu gốc là hash thành vô nghĩa.

**Vế đầu đúng. Vế sau chỉ đúng có điều kiện.** Vì kẻ tấn công **không cần đảo ngược hàm băm** — chỉ cần **thử hết mọi khả năng**.

### Đo thử

Demo 1 băm ngày sinh và số điện thoại rồi dò ngược, trên một luồng đơn, không tối ưu gì:

```
  (a) Ngay sinh
      luu tren chuoi : f55c48e48150b9cd66f09acfe616d01b...
      pha ra         : 1991-04-17  sau 24,662 lan thu, 26ms
  (b) So dien thoai (dau so 0912 doan duoc)
      luu tren chuoi : 20faf05baccf8a477fa337b77c0acb0e...
      pha ra         : 0912345678  sau 345,679 lan thu, 168ms
```

Một phần tư giây. Trên laptop. Bằng JavaScript.

> **Quy tắc:** thời gian phá = kích thước không gian ÷ tốc độ băm.
> Họ tên, ngày sinh, số điện thoại, số căn cước, biển số xe, email công ty — **tất cả đều là không gian nhỏ**. Băm chúng rồi ghi lên chuỗi công khai **chính là công bố chúng**, chỉ chậm hơn vài giây.

### Thêm muối có cứu được không

Không, nếu muối được ghi công khai kèm theo — mà nó buộc phải thế thì mới đối chiếu lại được. Demo 2:

```
  Ban ghi tren chuoi: hash=4dd77dfc9623613d716b2e6d... muoi=a3f9c1
  Pha ra: 0912345678 sau 196ms  <- muoi cong khai KHONG can tro gi
```

Muối chỉ chặn được **bảng tra cứu dựng sẵn** (mỗi bản ghi phải dò riêng), chứ không chặn được việc dò từng bản ghi một.

### Vậy khi nào mẫu con trỏ hash mới an toàn

Demo 4 xếp theo entropy, giả định kẻ tấn công có 5 tỷ phép băm/giây:

```
  truong du lieu           khong gian      thoi gian do het
  Ho ten + ngay sinh       10^ 8        < 1 giay   <-- KHONG AN TOAN
  So dien thoai VN         10^ 7        < 1 giay   <-- KHONG AN TOAN
  So CCCD 12 chu so        10^12        200 giay   <-- KHONG AN TOAN
  File PDF 100KB           10^77     7.3e+59 nam   AN TOAN
```

Kết luận thay cho lời video:

> ❌ *"Xoá dữ liệu gốc thì hash không còn là dữ liệu cá nhân."*
> ✅ **"Xoá dữ liệu gốc thì hash không còn là dữ liệu cá nhân — CHỈ KHI dữ liệu gốc có đủ entropy. Với các trường hồ sơ cá nhân thông thường thì hash vẫn là dữ liệu cá nhân, và nó thì không xoá được."**

### Cách làm đúng

```
   ❌  sha256("0912345678")
   ❌  sha256(muối_công_khai + "0912345678")
   ✅  sha256("0912345678" + BÍ_MẬT_256_BIT_LƯU_NGOÀI_CHUỖI)

   Muốn "được quên" -> xoá bí mật đó.
   Không gian dò lúc này là 2^256 -> vô vọng, kể cả với mọi máy tính trên đời.
```

Chú ý cái giá phải trả: an ninh giờ đến từ **việc xoá được bí mật ngoài chuỗi**, không đến từ hàm băm. Nghĩa là hệ thống lại có một điểm tin cậy tập trung — đúng nhược điểm video đã nêu ở `06:39`, chỉ là nó nghiêm trọng hơn video nghĩ.

---

## 8. 📚 Chấm điểm lại bốn giải pháp

| Giải pháp                | Điều 16 sửa                   | Điều 17 xoá                                | Điều 18 hạn chế xử lý        | Cái giá thật                                                                                                    |
| ------------------------ | ----------------------------- | ------------------------------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **1. Mã hoá trên chuỗi** | ❌                             | ⚠️ chỉ khi huỷ khoá được chấp nhận là "xoá" | ❌ ai cũng tải bản mã về được | dữ liệu mã hoá tồn tại **vĩnh viễn** để bẻ dần                                                                  |
| **2. Chuỗi có phép**     | ❌                             | ❌                                          | ✅                            | mất phần lớn lý do dùng blockchain                                                                              |
| **3. Con trỏ hash**      | ✅                             | ✅ **nếu dữ liệu đủ entropy**               | ✅                            | tập trung hoá một phần; sai entropy là hỏng ([§7](#7--băm-rồi-thì-hết-là-dữ-liệu-cá-nhân--chỗ-giải-pháp-3-gãy)) |
| **4. ZKP**               | ✅ không ghi dữ liệu lên chuỗi | ✅                                          | ✅                            | phức tạp, tốn kém, và [§12](#12--nghịch-lý-cuối-zkp-vừa-là-lời-giải-vừa-là-vấn-đề)                              |

Đọc bảng theo cột thì thấy một quy luật gọn:

> **Không có giải pháp nào "làm cho blockchain tuân thủ GDPR".** Cả bốn đều là biến thể của cùng một chiến lược: **đừng đưa dữ liệu cá nhân lên chuỗi**. Chỉ đưa lên thứ chứng minh được điều gì đó về dữ liệu — một hash có đủ entropy, hoặc một bằng chứng zero-knowledge.

Đây cũng đúng là kết luận của [Bài 4](../ly_thuyet/lesson_4_ung_dung_blockchain.md): blockchain giỏi việc **chứng minh một dữ liệu tồn tại và không bị sửa**, và dở mọi việc còn lại liên quan tới lưu trữ.

---

## 9. Ai là người chịu trách nhiệm

`07:53`. Đây là phần hay nhất của video, và nó kết thúc bằng một câu hỏi bỏ ngỏ.

Luật quy định **bên kiểm soát dữ liệu** phải tuân thủ. Nhưng trên một blockchain phi tập trung thì ai là bên kiểm soát? Video thử ba ứng viên và loại cả ba:

```
   ỨNG VIÊN 1: mọi người tham gia mạng lưới          08:16
      -> Không được. Họ không kiểm soát được người khác ghi gì lên chuỗi.

   ỨNG VIÊN 2: người tạo và xác minh khối            08:22
      -> Không được. Họ có thể không hề biết dữ liệu đó là dữ liệu cá nhân.

   ỨNG VIÊN 3: người viết giao thức                  08:36
      -> Không được. Họ chỉ làm ra một công cụ.
         "Phạt họ thì chẳng khác gì đóng cửa nhà máy búa
          vì búa có thể dùng để gây án."
```

> `08:46` **"Rõ ràng là chúng ta còn khá nhiều việc phải làm."**

Phép so sánh cái búa rất đắt, và nó chạm tới một câu hỏi rộng hơn nhiều GDPR: **luật vốn được xây quanh giả định luôn có một pháp nhân chịu trách nhiệm.** Blockchain được thiết kế chính xác để không có pháp nhân đó. Đây không phải khe hở kỹ thuật — đây là **hai thế giới quan không khớp nhau**.

---

## 10. 📚 Câu hỏi đó được trả lời ra sao tới 2026

Video hỏi năm 2018, khi chưa có án lệ nào. Gần một thập kỷ sau, câu trả lời đã hình thành — và nó không phải một trong ba ứng viên của video.

### Cơ quan quản lý chọn cách khác: nhắm vào ai dùng được

Thay vì tìm "bên kiểm soát" trong lòng mạng lưới, hướng tiếp cận thực tế là nhắm vào **bên có thể nhận dạng được và có quyền quyết định**:

```
   ❌ node bất kỳ, thợ đào bất kỳ, lập trình viên giao thức
   ✅ doanh nghiệp QUYẾT ĐỊNH đưa dữ liệu cá nhân lên chuỗi
   ✅ bên vận hành ứng dụng mà người dùng thật sự tương tác
   ✅ bên vận hành chuỗi có phép (ở đây thì rõ ràng, có hợp đồng hẳn hoi)
```

Nói cách khác: **trách nhiệm bám theo người quyết định, không bám theo hạ tầng.** Nếu công ty bạn ghi mã băm hồ sơ khách hàng lên Ethereum, công ty bạn là bên kiểm soát — không phải thợ đào Ethereum. Cách này giữ được logic của luật mà không phải đóng cửa nhà máy búa.

### Ba điều đã rõ hơn

|                                              | Trạng thái 2026                                                                                                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Huỷ khoá có được coi là "xoá" không**      | Được chấp nhận rộng rãi trong thực hành, nhưng chưa có gì bảo đảm tuyệt đối, và nó yếu dần theo thời gian ([§6](#6-bốn-giải-pháp-video-đề-xuất) giải pháp 1) |
| **Mẫu con trỏ hash**                         | Trở thành cách làm mặc định của ngành. Kèm theo là yêu cầu về entropy mà [§7](#7--băm-rồi-thì-hết-là-dữ-liệu-cá-nhân--chỗ-giải-pháp-3-gãy) chỉ ra            |
| **Chuỗi công khai chứa dữ liệu cá nhân thô** | Vẫn không có cách nào hợp lệ. Câu kết luận của video ở `03:36` vẫn đúng nguyên                                                                               |

### Và một thứ video không đoán được

GDPR không giết blockchain. Cái đến sau nó — **các quy định dành riêng cho tài sản mã hoá** — mới là thứ định hình lại ngành, bằng cách đặt nghĩa vụ lên **các nhà cung cấp dịch vụ** (sàn, ví lưu ký, đơn vị phát hành stablecoin) thay vì lên giao thức. Cùng một nguyên tắc: nhắm vào chỗ có người chịu trách nhiệm. [Bài 9 §20](lesson_9_tien_ma_hoa_toan_canh.md#20--pháp-lý-và-thuế--trạng-thái-2026) nói tiếp phần này.

---

## 11. 📚 Việt Nam — Nghị định 13/2023

Video chỉ nói về EU. Nhưng nếu bạn làm sản phẩm ở Việt Nam thì đây mới là văn bản áp vào đầu bạn.

**Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân, có hiệu lực **1/7/2023**. Cấu trúc rất giống GDPR, và **đụng vào blockchain theo đúng cùng một kiểu**:

| Khái niệm GDPR            | Tương ứng ở Nghị định 13                |
| ------------------------- | --------------------------------------- |
| Data controller           | **Bên Kiểm soát dữ liệu cá nhân**       |
| Data processor            | **Bên Xử lý dữ liệu cá nhân**           |
| Quyền chỉnh sửa (Điều 16) | **quyền chỉnh sửa** dữ liệu của mình    |
| Quyền được quên (Điều 17) | **quyền xoá** dữ liệu                   |
| Hạn chế xử lý (Điều 18)   | **quyền hạn chế xử lý**, quyền phản đối |

Nghị định 13 còn phân biệt **dữ liệu cá nhân cơ bản** và **dữ liệu cá nhân nhạy cảm** (sức khoẻ, sinh trắc, tài chính, xu hướng…), với yêu cầu chặt hơn hẳn cho nhóm sau — và yêu cầu **sự đồng ý phải rõ ràng, tách bạch, có thể rút lại**.

> ⚠️ **Ba điều cần nhớ khi thiết kế hệ thống blockchain ở Việt Nam:**
>
> 1. **Quyền xoá tồn tại ở đây y như ở EU.** Mọi lập luận trong bài này áp dụng nguyên vẹn: đừng ghi dữ liệu cá nhân lên chuỗi, kể cả ở dạng băm nếu entropy thấp.
> 2. **Dữ liệu tài chính thuộc nhóm nhạy cảm.** Mà lịch sử giao dịch chính là dữ liệu tài chính. Một chuỗi công khai gắn được với danh tính là bài toán khó gấp đôi.
> 3. **Quy định về chuyển dữ liệu ra nước ngoài.** Một blockchain công khai thì dữ liệu nằm trên node ở **mọi nước cùng lúc** — không có cách nào kiểm soát nơi lưu trú. Đây là vấn đề gần như không thể xử lý nếu đã trót đưa dữ liệu cá nhân lên chuỗi.

Khung pháp lý về dữ liệu cá nhân ở Việt Nam đang tiếp tục được nâng cấp lên mức luật, nên nếu bạn làm sản phẩm thật thì kiểm tra lại văn bản hiện hành tại thời điểm triển khai — nhưng **các nguyên tắc thiết kế trong bài này không đổi**, vì chúng đến từ tính chất của blockchain chứ không từ câu chữ của luật.

---

## 12. 📚 Nghịch lý cuối: ZKP vừa là lời giải vừa là vấn đề

Video kết thúc lạc quan: ZKP giải được bài toán, vì nó cho phép **chứng minh mà không tiết lộ**. Về kỹ thuật, đúng — và [Bài 8](../ly_thuyet/lesson_8_zero_knowledge_proof.md) cho thấy nó còn mạnh hơn nhiều so với ví dụ "trên 21 tuổi".

Nhưng có một chuyện video không thể lường trước.

```
   LOGIC RIÊNG TƯ                      LOGIC CHỐNG RỬA TIỀN
   ──────────────                      ─────────────────────
   Người dùng có quyền                 Cơ quan quản lý có nghĩa vụ
   không tiết lộ dữ liệu           ↔   truy vết dòng tiền

   Công cụ để làm điều đó:             Cùng một công cụ đó
   ZKP, giao dịch ẩn                   che giấu được tội phạm
```

Thực tế đã xảy ra: các công cụ trộn giao dịch bị đưa vào danh sách trừng phạt; các đồng tiền riêng tư bị nhiều sàn lớn huỷ niêm yết vì không đáp ứng được yêu cầu truy vết. **Cùng một tính chất kỹ thuật** — không truy được nguồn gốc — vừa là thứ GDPR đòi hỏi, vừa là thứ luật chống rửa tiền cấm.

> 💡 **Chỗ thoát hiểm cũng chính là ZKP, chỉ dùng theo hướng ngược lại.** Thay vì chứng minh *"tôi trên 21 tuổi"*, ta chứng minh *"số tiền này không đến từ một địa chỉ trong danh sách đen"* — mà không tiết lộ nó đến từ đâu. Đây là hướng nghiên cứu đang đi tới: **chứng minh sự tuân thủ mà không tiết lộ dữ liệu**.
>
> Nếu nó thành công thì bài học của cả khoá học được viết lại một lần cuối: mật mã không giải được vấn đề *pháp lý*, nhưng đôi khi nó tạo ra một lựa chọn thứ ba mà trước đó không ai thấy — thay vì phải chọn giữa *riêng tư* và *tuân thủ*.

---

## 13. Code minh hoạ

Bốn phép kiểm chứng: băm có phải ẩn danh không, muối có cứu được không, ví có liên kết được tới người thật không, và mẫu con trỏ hash an toàn tới đâu.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.
>
> 📌 Các con số **mili giây** phụ thuộc máy — máy bạn sẽ ra khác. Điều cần nhìn là **bậc độ lớn**, không phải con số cụ thể.

```typescript
/**
 * Bài 13 — GDPR & blockchain: kiểm chứng ba giả định mà video đưa ra.
 * Chạy: node demo.ts   (Node 22.6+, không cần cài gì)
 */
import { strict as assert } from "node:assert";
import { createHash } from "node:crypto";

const sha256 = (s: string): string =>
  createHash("sha256").update(s).digest("hex");

/* ===========================================================================
 * 1. "Băm là ẩn danh" — SAI khi không gian dữ liệu nhỏ
 *    Video nói hàm băm một chiều nên không lấy lại được dữ liệu.
 *    Đúng về toán. Nhưng KHÔNG CẦN đảo ngược — chỉ cần thử hết.
 * ======================================================================== */
console.log("=== 1. Bam mot chieu KHONG co nghia la an danh ===");
{
  function bruteForce(targetHash: string, candidates: () => Generator<string>): [string | null, number] {
    let tried = 0;
    for (const candidate of candidates()) {
      tried++;
      if (sha256(candidate) === targetHash) return [candidate, tried];
    }
    return [null, tried];
  }

  // (a) Ngày sinh — không gian ~36.500
  function* everyBirthDate(): Generator<string> {
    for (let year = 1925; year <= 2025; year++)
      for (let month = 1; month <= 12; month++)
        for (let day = 1; day <= 31; day++)
          yield `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
  }
  const birthDateHash = sha256("1991-04-17");
  let t0 = performance.now();
  const [crackedBirthDate, tries1] = bruteForce(birthDateHash, everyBirthDate);
  console.log(`  (a) Ngay sinh`);
  console.log(`      luu tren chuoi : ${birthDateHash.slice(0, 32)}...`);
  console.log(`      pha ra         : ${crackedBirthDate}  sau ${tries1.toLocaleString("en-US")} lan thu, ${(performance.now() - t0).toFixed(0)}ms`);

  // (b) Số điện thoại có đầu số biết trước — không gian 10^6
  function* everyPhoneNumber(): Generator<string> {
    for (let i = 0; i < 1_000_000; i++) yield "0912" + String(i).padStart(6, "0");
  }
  const phoneHash = sha256("0912345678");
  t0 = performance.now();
  const [crackedPhone, tries2] = bruteForce(phoneHash, everyPhoneNumber);
  console.log(`  (b) So dien thoai (dau so 0912 doan duoc)`);
  console.log(`      luu tren chuoi : ${phoneHash.slice(0, 32)}...`);
  console.log(`      pha ra         : ${crackedPhone}  sau ${tries2.toLocaleString("en-US")} lan thu, ${(performance.now() - t0).toFixed(0)}ms`);

  const msPerMillion = (performance.now() - t0) / tries2 * 1_000_000;
  console.log(`\n  Toc do may nay: ~${(1_000_000 / (msPerMillion / 1000) / 1_000_000).toFixed(1)} trieu bam/giay (1 luong, khong toi uu)`);
  console.log("  Quy tac: thoi gian pha = KICH THUOC KHONG GIAN / toc do bam.");
  console.log("  Ho ten, ngay sinh, so dien thoai, so CCCD deu la khong gian NHO.");
  console.log("  -> Bam chung roi ghi len chuoi = CONG KHAI chung, chi cham hon vai giay.");
  assert(crackedBirthDate === "1991-04-17" && crackedPhone === "0912345678");
}

/* ===========================================================================
 * 2. Thêm muối thì sao? Muối công khai KHÔNG cứu được gì.
 * ======================================================================== */
console.log("\n=== 2. Them muoi: chi giup neu muoi la BI MAT ===");
{
  const publicSalt = "a3f9c1"; // ghi kèm trên chuỗi để verify được
  const onChainRecord = sha256(publicSalt + "0912345678");
  console.log(`  Ban ghi tren chuoi: hash=${onChainRecord.slice(0, 24)}... muoi=${publicSalt}`);
  console.log("  Ke tan cong DOC DUOC muoi (no nam ngay do), chi viec them vao roi thu lai:\n");
  const t0 = performance.now();
  let cracked: string | null = null;
  for (let i = 0; i < 1_000_000; i++) {
    const candidate = "0912" + String(i).padStart(6, "0");
    if (sha256(publicSalt + candidate) === onChainRecord) { cracked = candidate; break; }
  }
  console.log(`  Pha ra: ${cracked} sau ${(performance.now() - t0).toFixed(0)}ms  <- muoi cong khai KHONG can tro gi`);
  console.log("\n  Muoi chi chong duoc bang tra cuu dung san, KHONG chong duoc do thu vet.");
  console.log("  Muon vo hieu that su thi bi mat phai NAM NGOAI CHUOI va XOA duoc.");
  console.log("  -> Nhung luc do an ninh den tu VIEC XOA, khong den tu ham bam.");
  assert(cracked === "0912345678");
}

/* ===========================================================================
 * 3. Địa chỉ ví CÓ PHẢI dữ liệu cá nhân — gộp cụm bằng suy luận đầu vào chung
 *    Video nói đúng là "có thể liên kết gián tiếp". Đây là cách làm thật.
 * ======================================================================== */
console.log("\n=== 3. Vi la du lieu ca nhan: gop cum dia chi ===");
{
  // Giao dịch tiêu nhiều đầu vào cùng lúc -> mọi đầu vào đó cùng một chủ,
  // vì phải ký được TẤT CẢ chúng. Đây là suy luận sở hữu đầu vào chung.
  const transactions = [
    { inputs: ["wallet_A", "wallet_B"], outputs: ["wallet_shop1"] },
    { inputs: ["wallet_B", "wallet_C"], outputs: ["wallet_shop2"] },
    { inputs: ["wallet_D"], outputs: ["wallet_E"] },
    { inputs: ["wallet_E", "wallet_F"], outputs: ["wallet_shop3"] },
    { inputs: ["wallet_C", "wallet_G"], outputs: ["wallet_shop1"] },
  ];

  const parent = new Map<string, string>();
  const findRoot = (x: string): string => {
    if (!parent.has(x)) parent.set(x, x);
    while (parent.get(x) !== x) { parent.set(x, parent.get(parent.get(x)!)!); x = parent.get(x)!; }
    return x;
  };
  const union = (a: string, b: string): void => { parent.set(findRoot(a), findRoot(b)); };

  for (const tx of transactions)
    for (let i = 1; i < tx.inputs.length; i++) union(tx.inputs[0], tx.inputs[i]);

  const clusters = new Map<string, string[]>();
  for (const tx of transactions)
    for (const wallet of tx.inputs) {
      const root = findRoot(wallet);
      if (!clusters.has(root)) clusters.set(root, []);
      if (!clusters.get(root)!.includes(wallet)) clusters.get(root)!.push(wallet);
    }

  console.log("  Cac cum suy ra duoc (moi cum = mot chu so huu):");
  for (const [, wallets] of clusters) console.log(`    { ${wallets.sort().join(", ")} }`);

  console.log("\n  Gia su san giao dich bi ro du lieu KYC: 'wallet_A thuoc ve Nguyen Van An'.");
  const clusterOfWalletA = clusters.get(findRoot("wallet_A"))!;
  console.log(`  -> Lo luon ca cum: ${clusterOfWalletA.sort().join(", ")}`);
  console.log("     cung toan bo lich su giao dich cua chung, VINH VIEN, cong khai.");
  console.log("\n  -> Dia chi vi la 'du lieu ca nhan' theo dinh nghia GDPR:");
  console.log("     mot chuoi ngau nhien LIEN KET GIAN TIEP duoc toi mot con nguoi.");
  assert(clusterOfWalletA.length === 4);
}

/* ===========================================================================
 * 4. Giải pháp video đề xuất: lưu dữ liệu ngoài chuỗi, chỉ ghi hash.
 *    Nó CHẠY ĐƯỢC — nhưng chỉ với dữ liệu đủ entropy.
 * ======================================================================== */
console.log("\n=== 4. Mau 'con tro hash': khi nao chay, khi nao khong ===");
{
  const fields = [
    { label: "Ho ten + ngay sinh", searchSpace: 36_500 * 1000, note: "1000 ho ten pho bien x ngay sinh" },
    { label: "So dien thoai VN", searchSpace: 10 ** 7, note: "dau so biet truoc" },
    { label: "So CCCD 12 chu so", searchSpace: 10 ** 12, note: "biet tinh + nam sinh thi con it hon" },
    { label: "File PDF 100KB", searchSpace: 2 ** 256, note: "noi dung tuy y" },
  ];
  const hashesPerSecond = 5_000_000_000; // giàn GPU khiêm tốn, ~5 tỷ hash/giây
  console.log(`  Gia dinh ke tan cong co ${(hashesPerSecond / 1e9).toFixed(0)} ty bam/giay:\n`);
  console.log("  truong du lieu           khong gian      thoi gian do het");
  for (const field of fields) {
    const seconds = field.searchSpace / hashesPerSecond;
    const readable = seconds < 1 ? "< 1 giay"
      : seconds < 3600 ? `${seconds.toFixed(0)} giay`
      : seconds < 86400 * 365 ? `${(seconds / 3600).toFixed(1)} gio`
      : `${(seconds / 86400 / 365).toExponential(1)} nam`;
    const isSafe = seconds > 86400 * 365 * 1e6;
    console.log(`  ${field.label.padEnd(24)} 10^${Math.log10(field.searchSpace).toFixed(0).padStart(2)}  ${readable.padStart(14)}   ${isSafe ? "AN TOAN" : "<-- KHONG AN TOAN"}`);
  }
  console.log("\n  -> Mau 'ghi hash len chuoi, xoa du lieu de duoc quen' CHI dung");
  console.log("     khi du lieu co du entropy. Voi truong ho so ca nhan thong thuong,");
  console.log("     hash tren chuoi VAN LA du lieu ca nhan — va no khong xoa duoc.");
  console.log("\n  Cach lam dung: bam (du lieu + BI MAT ngau nhien 256 bit luu NGOAI chuoi).");
  console.log("  Muon 'quen' -> xoa bi mat do. Luc nay khong gian tro thanh 2^256.");
  const offChainSecret = "K7f3" + "x".repeat(60); // 256 bit
  console.log(`  Vi du: sha256("0912345678" + bimat) = ${sha256("0912345678" + offChainSecret).slice(0, 32)}...`);
  console.log("  Xoa bimat -> khong con duong nao noi hash nay voi so dien thoai do.");
}

console.log("\nXong. Bam khong phai an danh; vi la du lieu ca nhan; con tro hash can entropy.");
```

Kết quả chạy thật:

```
=== 1. Bam mot chieu KHONG co nghia la an danh ===
  (a) Ngay sinh
      luu tren chuoi : f55c48e48150b9cd66f09acfe616d01b...
      pha ra         : 1991-04-17  sau 24,662 lan thu, 26ms
  (b) So dien thoai (dau so 0912 doan duoc)
      luu tren chuoi : 20faf05baccf8a477fa337b77c0acb0e...
      pha ra         : 0912345678  sau 345,679 lan thu, 168ms

  Toc do may nay: ~2.1 trieu bam/giay (1 luong, khong toi uu)
  Quy tac: thoi gian pha = KICH THUOC KHONG GIAN / toc do bam.
  Ho ten, ngay sinh, so dien thoai, so CCCD deu la khong gian NHO.
  -> Bam chung roi ghi len chuoi = CONG KHAI chung, chi cham hon vai giay.

=== 2. Them muoi: chi giup neu muoi la BI MAT ===
  Ban ghi tren chuoi: hash=4dd77dfc9623613d716b2e6d... muoi=a3f9c1
  Ke tan cong DOC DUOC muoi (no nam ngay do), chi viec them vao roi thu lai:

  Pha ra: 0912345678 sau 196ms  <- muoi cong khai KHONG can tro gi

  Muoi chi chong duoc bang tra cuu dung san, KHONG chong duoc do thu vet.
  Muon vo hieu that su thi bi mat phai NAM NGOAI CHUOI va XOA duoc.
  -> Nhung luc do an ninh den tu VIEC XOA, khong den tu ham bam.

=== 3. Vi la du lieu ca nhan: gop cum dia chi ===
  Cac cum suy ra duoc (moi cum = mot chu so huu):
    { wallet_A, wallet_B, wallet_C, wallet_G }
    { wallet_D }
    { wallet_E, wallet_F }

  Gia su san giao dich bi ro du lieu KYC: 'wallet_A thuoc ve Nguyen Van An'.
  -> Lo luon ca cum: wallet_A, wallet_B, wallet_C, wallet_G
     cung toan bo lich su giao dich cua chung, VINH VIEN, cong khai.

  -> Dia chi vi la 'du lieu ca nhan' theo dinh nghia GDPR:
     mot chuoi ngau nhien LIEN KET GIAN TIEP duoc toi mot con nguoi.

=== 4. Mau 'con tro hash': khi nao chay, khi nao khong ===
  Gia dinh ke tan cong co 5 ty bam/giay:

  truong du lieu           khong gian      thoi gian do het
  Ho ten + ngay sinh       10^ 8        < 1 giay   <-- KHONG AN TOAN
  So dien thoai VN         10^ 7        < 1 giay   <-- KHONG AN TOAN
  So CCCD 12 chu so        10^12        200 giay   <-- KHONG AN TOAN
  File PDF 100KB           10^77     7.3e+59 nam   AN TOAN

  -> Mau 'ghi hash len chuoi, xoa du lieu de duoc quen' CHI dung
     khi du lieu co du entropy. Voi truong ho so ca nhan thong thuong,
     hash tren chuoi VAN LA du lieu ca nhan — va no khong xoa duoc.

  Cach lam dung: bam (du lieu + BI MAT ngau nhien 256 bit luu NGOAI chuoi).
  Muon 'quen' -> xoa bi mat do. Luc nay khong gian tro thanh 2^256.
  Vi du: sha256("0912345678" + bimat) = 61433cacebd04ba8a30ca45e54248d65...
  Xoa bimat -> khong con duong nao noi hash nay voi so dien thoai do.

Xong. Bam khong phai an danh; vi la du lieu ca nhan; con tro hash can entropy.
```

**Tự thử:**

1. Băm **email công ty** theo mẫu `ho.ten@congty.vn`. Với một danh sách 5.000 nhân viên thì không gian là bao nhiêu? Bao lâu dò hết?
2. Trong demo 3, thêm suy luận thứ hai: **đầu ra tiền thừa** (giao dịch có 2 đầu ra, một cái số lẻ → thường là tiền thừa quay về chính chủ). Cụm phình ra bao nhiêu?
3. Sửa demo 4 để tính ngược: **cần bao nhiêu bit entropy** thì mới an toàn trong 100 năm với 5 tỷ phép băm/giây? So với 256 bit.
4. Cài một hàm băm cố tình chậm (lặp SHA-256 vài trăm nghìn lần). Nó nâng chi phí dò lên bao nhiêu — và vì sao **vẫn không đủ** cho dữ liệu ghi vĩnh viễn lên chuỗi công khai?

---

## 14. Từ điển thuật ngữ

| Tiếng Anh                 | Tiếng Việt                       | Nghĩa gọn                                                            |
| ------------------------- | -------------------------------- | -------------------------------------------------------------------- |
| GDPR                      | Quy định chung về bảo vệ dữ liệu | luật riêng tư EU, hiệu lực 25/5/2018                                 |
| Data controller           | bên kiểm soát dữ liệu            | bên quyết định thu thập và lưu — **chịu trách nhiệm**                |
| Data processor            | bên xử lý dữ liệu                | bên làm việc trên dữ liệu theo yêu cầu bên kiểm soát                 |
| Personal data             | dữ liệu cá nhân                  | mọi thông tin **nhận dạng được** một con người, kể cả gián tiếp      |
| Right to rectification    | quyền chỉnh sửa                  | Điều 16                                                              |
| Right to be forgotten     | quyền được quên                  | Điều 17                                                              |
| Restriction of processing | hạn chế xử lý                    | Điều 18                                                              |
| Pseudonymisation          | giả danh hoá                     | thay danh tính bằng mã — **vẫn là dữ liệu cá nhân**                  |
| Anonymisation             | ẩn danh hoá                      | không còn liên kết được — mới thoát khỏi luật                        |
| Brute force               | dò thử vét cạn                   | thử hết mọi khả năng thay vì đảo ngược hàm băm                       |
| Entropy                   | độ ngẫu nhiên                    | kích thước không gian khả năng — thứ quyết định băm có an toàn không |
| Salt                      | muối                             | chuỗi thêm vào trước khi băm; công khai thì vô dụng với dò vét       |
| Crypto-erasure            | xoá bằng huỷ khoá                | "xoá" dữ liệu bằng cách huỷ khoá giải mã                             |
| Common-input-ownership    | sở hữu đầu vào chung             | suy luận: mọi đầu vào của một giao dịch cùng một chủ                 |
| Address clustering        | gộp cụm địa chỉ                  | gom các ví về cùng chủ sở hữu                                        |
| Permissioned blockchain   | blockchain có phép               | chỉ bên được cấp quyền mới đọc/ghi                                   |
| Off-chain                 | ngoài chuỗi                      | dữ liệu để nơi khác, chuỗi chỉ giữ con trỏ                           |

---

## 15. Câu hỏi tự kiểm tra

1. Hai tính chất nào của blockchain đụng thẳng vào GDPR?
2. Bên kiểm soát và bên xử lý dữ liệu khác nhau thế nào? Bên nào chịu trách nhiệm tuân thủ?
3. Địa chỉ IP có phải dữ liệu cá nhân không? Giải thích bằng lập luận "liên kết gián tiếp".
4. Vì sao địa chỉ ví Bitcoin là dữ liệu cá nhân dù nó chỉ là chuỗi ngẫu nhiên?
5. Mô tả suy luận sở hữu đầu vào chung. Vì sao nó đúng?
6. Trong demo 3, `wallet_A` và `wallet_G` chưa từng xuất hiện chung một giao dịch nào. Vì sao vẫn gom được vào một cụm?
7. Một điểm rò KYC làm lộ bao nhiêu? Vì sao chuyện này khác hẳn một vụ rò cơ sở dữ liệu thông thường?
8. Điều 16, 17, 18 đòi hỏi gì, và blockchain hỏng ở từng điều thế nào?
9. Câu "blockchain không được lưu dữ liệu cá nhân của công dân EU" đúng với loại blockchain nào? Nó có nghĩa là blockchain bị cấm không?
10. Giải pháp mã hoá trên chuỗi: huỷ khoá có phải là xoá không? Lập luận phản đối là gì, và vì sao nó nặng hơn với dữ liệu ghi vĩnh viễn?
11. Blockchain có phép tuân thủ được điều nào, không tuân thủ được điều nào? Và câu hỏi khó chịu nào còn lại?
12. Mẫu con trỏ hash hoạt động thế nào? Vì sao bản thân cái hash cũng là dữ liệu cá nhân?
13. Video nói xoá dữ liệu gốc thì hash "trỏ vào hư không". Vế nào của câu này sai, và sai trong trường hợp nào?
14. Vì sao dò vét cạn không cần đảo ngược hàm băm? Viết công thức thời gian phá.
15. Muối công khai chặn được kiểu tấn công nào và không chặn được kiểu nào?
16. Cách băm đúng để dữ liệu thật sự "quên" được là gì? An ninh lúc đó đến từ đâu?
17. Ba ứng viên làm "bên kiểm soát dữ liệu" trong video là ai, và vì sao cả ba đều bị loại?
18. Phép so sánh "nhà máy búa" nói lên điều gì về quan hệ giữa luật và hệ thống phi tập trung?
19. Tới 2026, trách nhiệm được quy về đâu? Nguyên tắc chung là gì?
20. Nghị định 13/2023 của Việt Nam tương ứng với GDPR ở những khái niệm nào? Ba điều cần nhớ khi thiết kế là gì?
21. Vì sao quy định chuyển dữ liệu ra nước ngoài gần như không xử lý được nếu đã đưa dữ liệu cá nhân lên chuỗi công khai?
22. ZKP giải được bài toán riêng tư nhưng tạo ra xung đột pháp lý nào?
23. "Chứng minh sự tuân thủ mà không tiết lộ dữ liệu" nghĩa là gì? Cho một ví dụ cụ thể.
24. Sau 13 bài, phát biểu lại luận điểm xuyên suốt khoá học bằng lời của bạn — và chỉ ra bài này bổ sung gì cho nó.

---

## Tóm tắt một trang

```
 ┌──────────────────────────────────────────────────────────────────────┐
 │  GDPR có giết blockchain không?                                       │
 │  KHÔNG — nhưng nó cấm hẳn một cách dùng: đưa dữ liệu cá nhân lên chuỗi│
 └──────────────────────────────────────────────────────────────────────┘

  VA CHẠM
    blockchain: công khai + không xoá được
    GDPR:       quyền sửa (Đ.16) + quyền xoá (Đ.17) + hạn chế xử lý (Đ.18)
    -> không có cách nào dung hoà nếu dữ liệu cá nhân nằm THÔ trên chuỗi

  DỮ LIỆU CÁ NHÂN RỘNG HƠN BẠN NGHĨ
    tên, tuổi -> rõ rồi
    IP, số thẻ -> vẫn là, vì LIÊN KẾT GIÁN TIẾP được
    ĐỊA CHỈ VÍ -> cũng là. Một lần KYC là lộ cả cụm, VĨNH VIỄN.
    (demo: gộp cụm bằng suy luận sở hữu đầu vào chung)

  BỐN GIẢI PHÁP — chấm điểm lại
    1 mã hoá trên chuỗi   ✗ bản mã sống mãi để bẻ dần
    2 chuỗi có phép       ✗ vẫn không xoá được; mà thế thì dùng CSDL cho xong
    3 con trỏ hash        ✓ NHƯNG chỉ khi dữ liệu ĐỦ ENTROPY
    4 ZKP                 ✓ đắt, phức tạp, và vướng luật chống rửa tiền

  ⚠️ LỖ THỦNG CỦA GIẢI PHÁP 3  (video không thấy)
    "băm một chiều nên an toàn" -> kẻ tấn công KHÔNG đảo ngược, nó DÒ VÉT
    ngày sinh    -> phá trong 26ms
    số điện thoại-> phá trong 168ms
    muối công khai-> không cản được gì
    ✅ cách đúng: sha256(dữ liệu + BÍ MẬT 256 bit lưu NGOÀI chuỗi)
                  xoá bí mật = xoá thật

  AI CHỊU TRÁCH NHIỆM
    video 2018: node? thợ đào? lập trình viên? — loại cả ba, bỏ ngỏ
    tới 2026  : trách nhiệm bám theo NGƯỜI QUYẾT ĐỊNH đưa dữ liệu lên chuỗi,
                không bám theo hạ tầng

  VIỆT NAM — Nghị định 13/2023/NĐ-CP (hiệu lực 1/7/2023)
    có đủ quyền chỉnh sửa / xoá / hạn chế xử lý
    dữ liệu tài chính = NHẠY CẢM, mà lịch sử giao dịch chính là thứ đó
    + quy định chuyển dữ liệu ra nước ngoài — chuỗi công khai thì bó tay

  CÂU CỦA CẢ KHOÁ HỌC, LẦN CUỐI
    Mật mã không phải chỗ vỡ.
    Ở bài này thậm chí mật mã hoạt động HOÀN HẢO — và chính vì thế
    mà không xoá được. Tính chất tốt nhất của nó là vấn đề pháp lý của nó.
```

---

## Nguồn

- Video gốc: [Will GDPR kill blockchains? — Simply Explained](https://www.youtube.com/watch?v=5I3wYAwbKMM) (9:15)
- [Toàn văn GDPR](https://gdpr-info.eu) — Điều 16, 17, 18 rất ngắn, nên đọc thẳng
- [Nghị định 13/2023/NĐ-CP](https://vanban.chinhphu.vn) — bảo vệ dữ liệu cá nhân tại Việt Nam
- [Nghiên cứu của Nghị viện châu Âu về blockchain và GDPR](https://www.europarl.europa.eu/thinktank/en/document/EPRS_STU(2019)634445) — bản phân tích đầy đủ nhất về đúng câu hỏi của video
- [Bitcoin Wiki — Privacy](https://en.bitcoin.it/wiki/Privacy) — danh mục các suy luận gộp cụm địa chỉ

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
12. [Bài 12 – ERC-20: chuẩn token](lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. **Bài 13 – GDPR có giết blockchain không** ← *bạn đang ở đây* — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
