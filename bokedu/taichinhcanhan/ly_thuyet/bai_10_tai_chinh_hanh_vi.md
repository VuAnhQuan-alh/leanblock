# Bài 10 — [bổ sung] Tài chính hành vi: vì sao biết mà vẫn sai

> [!info] Về bài này
> **Chủ đề này không có trong sách như một chủ đề.** Nhưng sách **chạm vào nó bốn lần, ở bốn chỗ rời
> nhau**, và chỉ một lần gọi đúng tên. Toàn bộ bài này là **[bổ sung]**: nó không thêm kiến thức mới
> vào sách, nó **dựng cái khung** để bốn mảnh rời ấy thành một bức tranh — và để **bài 11**
> có chỗ tựa mà giải thích, chứ không chỉ kể lại.
> **Cần đọc trước:** [Bài 5](bai_05_kiem_tien.md) — chỗ **thiên kiến sống sót** ở quy tắc 3 của Kim
> tứ đồ (C2 tr. 10) là mảnh đầu tiên, và là lần duy nhất sách gọi đúng tên một thiên kiến. Bài này
> nhặt nốt ba mảnh còn lại.
> **Đây là bài vòng 2** — đọc hiểu, nắm ý là đủ; không có công thức pháp lý nào phải nhớ. Nhưng nó
> là bài **quyết định** cho bài 11: gần như mọi cái bẫy tài chính đều là một thiên kiến bị lợi dụng.
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
> **Code:** [`thuc_hanh/bai-10-tai-chinh-hanh-vi.py`](../thuc_hanh/bai-10-tai-chinh-hanh-vi.py)
> — bài này ít số, nhưng ba con số nó có (lạm phát lối sống, phép nhân của "lãi 20%/tháng", và bảng
> bất đối xứng lỗ–lãi) đều do tệp này tính. Mỗi con số kèm một công thức một dòng để tự kiểm bằng tay.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).

---

## Mục lục

<!-- MUC-LUC -->
- [1. Bốn mảnh của một bức tranh, và cái tên sách không gọi](#1-bốn-mảnh-của-một-bức-tranh-và-cái-tên-sách-không-gọi)
- [2. Tài chính hành vi là gì: khoảng cách giữa "biết" và "làm"](#2-tài-chính-hành-vi-là-gì-khoảng-cách-giữa-biết-và-làm)
- [3. Thiên kiến sống sót — cái tên duy nhất sách gọi đúng, ở trang 10](#3-thiên-kiến-sống-sót--cái-tên-duy-nhất-sách-gọi-đúng-ở-trang-10)
- [4. Lạm phát lối sống — vì sao khoản tăng lương biến mất, ở trang 17](#4-lạm-phát-lối-sống--vì-sao-khoản-tăng-lương-biến-mất-ở-trang-17)
- [5. Sự tham lam — khi "quá tốt để là thật" vẫn thắng, ở trang 52](#5-sự-tham-lam--khi-quá-tốt-để-là-thật-vẫn-thắng-ở-trang-52)
- [6. Ẩn dụ Lọ Lem — thiên kiến lạc quan và ảo tưởng kiểm soát, ở trang 53](#6-ẩn-dụ-lọ-lem--thiên-kiến-lạc-quan-và-ảo-tưởng-kiểm-soát-ở-trang-53)
- [7. [bổ sung] Bản đồ thiên kiến: mỗi cái đã xuất hiện ở đâu](#7-bổ-sung-bản-đồ-thiên-kiến-mỗi-cái-đã-xuất-hiện-ở-đâu)
- [8. [bổ sung] Vì sao biết mà vẫn sai — và cách duy nhất chống lại](#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại)
- [9. Cầu sang bài 11: vì sao người có tiền vẫn dính Ponzi](#9-cầu-sang-bài-11-vì-sao-người-có-tiền-vẫn-dính-ponzi)
- [10. Tự thử](#10-tự-thử)
- [11. Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
- [12. Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Bốn mảnh của một bức tranh, và cái tên sách không gọi

Chín bài trước đều là **kiến thức**: tài sản ròng cộng trừ thế nào, thuế tính ra sao, quỹ khẩn cấp
bao nhiêu tháng. Bài này hỏi một câu khác hẳn:

> [!note]
> Nếu biết hết những điều đó rồi, vì sao người ta vẫn làm sai?

Câu trả lời không nằm ở chỗ thiếu kiến thức. Nó nằm ở chỗ **bộ não con người không được thiết kế để
ra quyết định tài chính** — nó được thiết kế để sống sót trong một thế giới không có lãi kép, không
có hợp đồng bảo hiểm, không có Ponzi. Những phản xạ từng cứu mạng tổ tiên ta lại là **sai lệch có hệ
thống** khi đặt trước một bảng lãi suất. Môn học gọi chúng là **thiên kiến nhận thức** (*cognitive
bias*), và ngành nghiên cứu chúng trong tiền bạc là **tài chính hành vi** (*behavioral finance*).

Sách chạm vào chủ đề này đúng **bốn lần**, ở bốn chỗ cách xa nhau, và chỉ **một lần** gọi đúng tên:

| Sách viết | Ở đâu | Tên thật của hiện tượng | Mục |
| --- | --- | --- | :---: |
| *"sai lầm do ảnh hưởng bởi **thiên kiến sống sót**"* | C2 tr. 10, quy tắc 3 Kim tứ đồ | thiên kiến sống sót | [3](#3-thiên-kiến-sống-sót--cái-tên-duy-nhất-sách-gọi-đúng-ở-trang-10) |
| *"nguy cơ **lạm phát lối sống** (lifestyle creep)"* | C2 tr. 17 | lạm phát lối sống | [4](#4-lạm-phát-lối-sống--vì-sao-khoản-tăng-lương-biến-mất-ở-trang-17) |
| *"**Một. Sự tham lam**"* | C2 tr. 52, bài blog phụ lục | chạy theo lợi nhuận, tham lam | [5](#5-sự-tham-lam--khi-quá-tốt-để-là-thật-vẫn-thắng-ở-trang-52) |
| ẩn dụ **Lọ Lem** của Buffett, *"nhảy múa trong một căn phòng với những chiếc đồng hồ không có kim"* | C2 tr. 53 | thiên kiến lạc quan, ảo tưởng kiểm soát | [6](#6-ẩn-dụ-lọ-lem--thiên-kiến-lạc-quan-và-ảo-tưởng-kiểm-soát-ở-trang-53) |

Chỉ dòng đầu được gọi đúng tên. Ba dòng còn lại sách **mô tả đúng hiện tượng nhưng không có chữ để
gọi**, nên chúng nằm rời rạc, mỗi cái một chỗ, không cái nào biết mình là họ hàng của cái kia.

Đó là toàn bộ việc của bài này: **gom bốn mảnh về một chỗ, gọi đúng tên, rồi thêm những thiên kiến
mà sách bỏ sót nhưng đã âm thầm xuất hiện suốt chín bài trước.**

---

## 2. Tài chính hành vi là gì: khoảng cách giữa "biết" và "làm"

Kinh tế học cổ điển giả định con người là **"người kinh tế lý trí"** (*homo economicus*): biết hết
thông tin, tính đúng xác suất, luôn chọn cái có lợi nhất cho mình. Tài chính hành vi ra đời từ một
quan sát đơn giản — **không ai như thế cả**, kể cả người thông minh, kể cả chính các nhà kinh tế.

Cách hình dung gọn nhất là **hai hệ thống tư duy**:

| | Hệ thống 1 | Hệ thống 2 |
| --- | --- | --- |
| Kiểu | nhanh, tự động, cảm tính | chậm, cần gắng sức, logic |
| Ví dụ | *"giá này hời quá"* | ngồi tính lãi suất thật ra giấy |
| Dùng khi | gần như mọi lúc | khi bị bắt buộc, và ta rất lười bật nó |
| Chi phí | không tốn gì | tốn năng lượng, nên não né |

Thiên kiến là chỗ **Hệ thống 1 trả lời một câu mà lẽ ra phải để Hệ thống 2 trả lời** — và trả lời
sai theo một hướng đoán trước được. Điểm mấu chốt, và cũng là tên bài:

> [!note]
> **Biết một thiên kiến không đủ để thoát khỏi nó.** Bạn có thể đọc thuộc lòng chương này rồi vẫn
> tiêu hết khoản thưởng Tết vào đúng cái bẫy vừa đọc. Kiến thức nằm ở Hệ thống 2; quyết định phần lớn
> do Hệ thống 1 bấm nút.

Đây là lý do bài này không kết thúc bằng "hãy tỉnh táo hơn". Lời khuyên đó vô dụng — cũng như bảo
người cận thị hãy nhìn rõ hơn. [Mục 8](#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại)
cho cách chống thật sự, và nó không phải ý chí.

Ba đại lượng lặp lại trong cả chương, đáng nhớ trước khi đi tiếp:

- **Bất đối xứng lỗ–lãi (loss aversion).** Mất 100 nghìn đau hơn nhặt được 100 nghìn vui — chừng
  **gấp đôi**, theo các thí nghiệm gốc. Nó bẻ cong gần như mọi quyết định có rủi ro.
- **Thiên lệch hiện tại (present bias).** Phần thưởng bây giờ hấp dẫn hơn hẳn phần thưởng lớn hơn ở
  tương lai. Đây là kẻ thù trực tiếp của tiết kiệm và lãi kép.
- **Neo (anchoring).** Con số đầu tiên nghe được kéo mọi ước lượng sau về phía nó, dù con số ấy vô
  nghĩa.

---

## 3. Thiên kiến sống sót — cái tên duy nhất sách gọi đúng, ở trang 10

C2 tr. 10, trong quy tắc 3 của Kim tứ đồ, sách viết một đoạn mà [bài 5](bai_05_kiem_tien.md#quy-tắc-3--chỗ-sách-phản-biện-chính-kiyosaki)
đã gọi là sắc sảo nhất cả hai tập:

> [!quote]
> *"Nhiều người cho rằng phải ở nhóm B hoặc nhóm I mới trở nên giàu có… Suy nghĩ vậy là sai lầm do
> ảnh hưởng bởi **thiên kiến sống sót**. Truyền thông cho chúng ta thấy rất nhiều gương doanh nhân –
> nhà đầu tư thành công nhưng đằng sau đó là vô số trường hợp thất bại không hề được nhắc đến."*
> — C2 tr. 10

**Thiên kiến sống sót** (*survivorship bias*): ta ước lượng cơ hội thành công bằng những trường hợp
**còn nhìn thấy được**, mà những trường hợp thành công là những trường hợp còn được nhắc tới. Kẻ
thất bại thì im lặng — đóng cửa, biến mất, không lên báo. Mẫu số bị xoá, chỉ còn tử số.

Sách mô tả rất đúng, chỉ thiếu con số cho thấy méo tới đâu. Giả sử truyền thông kể **100 gương khởi
nghiệp thành công**, và giả định tỷ lệ thành công thực là 1 trên 10:

```
   bạn NHÌN THẤY        100 người thành công
   bạn KHÔNG thấy       900 người thất bại đã đóng cửa
   ─────────────────────────────────────────────
   tưởng xác suất là    100 / 100 = 100%
   thực ra là           100 / 1000 = 10%
```

Cùng một sự thật — 100 người thành công — sinh ra hai ước lượng lệch nhau **mười lần**, chỉ vì một
bên đếm cả mẫu số, một bên không. Người nhìn 100 tấm gương mà không hỏi *"đằng sau họ có bao nhiêu
người đã thử và thua?"* đang tự cho mình một xác suất phóng đại lên mười lần.

Điều đáng nói: đây là chỗ sách dùng thiên kiến để **phản biện chính Robert Kiyosaki** — tác giả của
Kim tứ đồ mà sách đang trình bày. Nó không bảo *"đừng khởi nghiệp"*; nó bảo **đừng ước lượng cơ hội
từ một mẫu đã bị lọc**. Cái quyết định bạn ở phía nào của xác suất ấy là chuyên môn, không phải việc
bạn đứng ở ô nào của Kim tứ đồ — đúng bản hoà giải quy tắc 3 và quy tắc 4 ở
[bài 5 mục 5](bai_05_kiem_tien.md#5-bổ-sung-quy-tắc-3-và-quy-tắc-4-kéo-về-hai-hướng).

Thiên kiến sống sót sẽ trở lại ở bài 11 và bài 13 dưới một lớp áo khác: **quảng cáo lợi nhuận đầu
tư luôn khoe người thắng, không bao giờ khoe người thua** — mà mẫu số của họ mới là điều bạn cần.

---

## 4. Lạm phát lối sống — vì sao khoản tăng lương biến mất, ở trang 17

C2 tr. 17, ngay trong bài về tài sản ròng, sách nhắc một cụm rồi đi tiếp:

> [!quote]
> *"nguy cơ **lạm phát lối sống** (lifestyle creep)"*

**Lạm phát lối sống**: khi thu nhập tăng, chi tiêu **phình lên theo**, gần như tự động, tới mức khoản
tăng thu nhập biến mất mà không để lại gì trong tiết kiệm. Đằng sau nó là hai đại lượng ở mục 2:
**thích nghi hưởng thụ** (quen mức sống mới rất nhanh, niềm vui trở lại vạch cũ) và **thiên lệch hiện
tại** (tiêu bây giờ luôn thắng để dành cho sau).

Đây là chỗ nó nối thẳng với người ở [bài 3](bai_03_ghi_chep_chi_tieu.md): thu nhập ròng 16tr, để dành
thực tế **2,48tr/tháng** tức 15,5% (từ [bài 7 mục 8](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật)),
chi 13,52tr. Nay được **tăng lương ròng 3,2tr/tháng**. Có đúng hai cách xử khoản tăng đó:

| | Để lối sống phình theo | Giữ nguyên chi, dồn hết khoản tăng |
| --- | --- | --- |
| Cách làm | vẫn để dành **15,5%** của thu nhập mới | chi vẫn 13,52tr, phần dư vào tiết kiệm |
| Chi tiêu | 16,22tr | 13,52tr |
| Để dành mỗi tháng | **2,98tr** | **5,68tr** |
| Tỷ lệ giữ lại | 15,5% | **29,6%** |
| Xây xong quỹ khẩn cấp 62,20tr | 20,9 tháng | **11,0 tháng** |

Cùng một khoản tăng lương, hai kết cục cách nhau **gần một nửa thời gian** để có quỹ khẩn cấp — và
khoảng cách ấy chỉ nới rộng thêm qua từng năm nhờ lãi kép ở lọ FFA. Toàn bộ chênh lệch là **2,70tr
mỗi tháng** lẽ ra để dành được nhưng đã lặng lẽ trôi vào mức sống mới.

Hệ quả thực dụng, và là điều [bài 7](bai_07_phan_bo_thu_nhap.md) không nói:

> [!note]
> **Khoảnh khắc tăng lương là thời điểm tốt nhất để nâng tỷ lệ tiết kiệm** — vì bạn chưa kịp quen với
> số tiền đó, nên cắt nó đi không thấy đau. Đợi vài tháng cho lối sống phình lên rồi mới định để dành
> thì đã phải cắt vào cái mình đã quen, và đó là lúc thích nghi hưởng thụ chống lại bạn.

Cách chặn không phải là quyết tâm, mà là **cấu trúc**: hẹn chuyển tự động phần lương tăng thẳng vào
lọ FFA/LTSS **trước khi** nó kịp nằm trong tài khoản chi tiêu. Đây chính là nguyên tắc "trả cho mình
trước" của [bài 7](bai_07_phan_bo_thu_nhap.md), và [mục 8](#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại)
giải thích vì sao tự động hoá thắng ý chí.

---

## 5. Sự tham lam — khi "quá tốt để là thật" vẫn thắng, ở trang 52

Trong bài blog phụ lục cuối C2, tác giả tự nhận từng nghĩ nạn nhân Ponzi là *"ngu ngốc"*, rồi nhận
ra *"Người có tiền thường không ngu ngốc"* (C2 tr. 52), và đặt tên yếu tố đầu tiên:

> [!quote]
> *"**Một. Sự tham lam.**"* — C2 tr. 52

Sách gọi đúng cảm giác nhưng dừng ở mô tả. Cái khung phía sau là **chạy theo lợi nhuận** (*return
chasing*): con số lợi nhuận càng cao, Hệ thống 1 càng khao khát tới mức tắt luôn câu hỏi *"con số này
có thể có thật không?"*. Và có một phép thử một dòng, đủ để bật lại Hệ thống 2:

> [!note]
> **Bất kỳ mức lãi nào, nhân nó lên cả năm bằng lãi kép, rồi hỏi: cả nền kinh tế có làm nổi thế
> không?**

Ponzi kinh điển chào *"lãi 20%/tháng"*. Nghe thì gọn. Nhân lên:

```
   lãi cả năm = (1 + 0,20)^12 − 1 = 791,6%/năm
```

So với con số thật mà cả khoá dùng — lợi suất **thực** dài hạn khoảng **8%/năm** (từ
[bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách)):

| Lời hứa | Quy ra cả năm | So với 8% thực | Đọc ra |
| --- | ---: | ---: | --- |
| 8%/năm | 8% | ×1 | mức thị trường bình thường |
| 3%/tháng | 42,6%/năm | ×5 | đã rất khó tin |
| 5%/tháng | 79,6%/năm | ×10 | gần như chắc chắn là bẫy |
| **20%/tháng** | **791,6%/năm** | **×99** | không một hoạt động kinh tế thật nào bền được ở mức này |

Không ai giữ được 791%/năm bằng đầu tư thật; kẻ trả 20%/tháng chỉ có một nguồn tiền — **tiền của
người vào sau**. Đó chính là định nghĩa Ponzi, và là toàn bộ nội dung **bài 11**.

Cái làm "tham lam" nguy hiểm không phải bản thân lòng tham — ai cũng muốn lời nhiều. Nó nguy hiểm vì
nó **tắt luôn phép nhân một dòng ở trên**. Người bị cuốn không ngu; họ chỉ không bật Hệ thống 2 lên
đúng ba giây cần thiết. Và đây cũng là chỗ [bài 9](bai_09_bao_ve.md#12-đính-chính-ba-con-số-ở-trang-47-không-khớp-nhau)
gặp lại nó: hợp đồng bảo hiểm liên kết đầu tư bị huỷ ngay năm đầu phần lớn vì được mua như một khoản
*"gửi tiết kiệm lãi cao"* — cùng một lòng tham, cùng một phép nhân không ai bấm.

---

## 6. Ẩn dụ Lọ Lem — thiên kiến lạc quan và ảo tưởng kiểm soát, ở trang 53

C2 tr. 53 mượn ẩn dụ của Warren Buffett, và đây là hình ảnh hay nhất của cả phần blog:

> [!quote]
> nhà đầu tư trong cơn sốt giống các vị khách trong buổi tiệc của Lọ Lem — *"nhảy múa trong một căn
> phòng với những chiếc đồng hồ không có kim"*. — C2 tr. 53

Ai cũng biết tiệc sẽ tàn lúc nửa đêm, ai cũng định sẽ về **ngay trước** nửa đêm để vừa vui vừa an
toàn. Nhưng đồng hồ **không có kim** — không ai biết mấy giờ — nên tất cả nán lại thêm một điệu nữa,
và cỗ xe hoá lại thành quả bí. Đằng sau hình ảnh ấy là hai thiên kiến chồng lên nhau:

| Thiên kiến | Nội dung | Câu tự nhủ điển hình |
| --- | --- | --- |
| **Thiên kiến lạc quan** (*optimism bias*) | tin rủi ro xấu xảy ra với người khác, không với mình | *"người khác cháy túi chứ tôi thì kịp rút"* |
| **Ảo tưởng kiểm soát** (*illusion of control*) | tin mình điều khiển được thứ vốn do may rủi | *"tôi canh được đúng đỉnh để bán"* |

Hai cái này là lý do câu *"tôi sẽ rút trước khi sập"* gần như không bao giờ thành. Muốn rút đúng lúc,
bạn phải biết **hai** thời điểm — khi nào vào và khi nào ra — mà cái thứ hai thì chiếc đồng hồ không
có kim. Buffett không nói *"đừng dự tiệc"*; ông nói **đừng tin rằng mình sẽ là người duy nhất nhìn
được kim đồng hồ vô hình**.

Nó nối thẳng sang **bài 12 — khẩu vị rủi ro**: người đánh giá quá cao
khả năng "canh thị trường" của mình thường khai khẩu vị rủi ro cao hơn thực chất, rồi hoảng và bán
tháo đúng đáy — hành vi mà chính bảng câu hỏi rủi ro (bài 12) cố đo trước để chặn.

---

## 7. [bổ sung] Bản đồ thiên kiến: mỗi cái đã xuất hiện ở đâu

Bốn mảnh của sách chỉ là bốn trong số nhiều thiên kiến đã âm thầm đi qua chín bài trước — mỗi lần
một chỗ, không được gọi tên. Bảng này gom chúng về một mối. Cột cuối là chỗ **bạn đã gặp nó rồi mà
chưa biết tên**:

| Thiên kiến | Nghĩa gọn | Trong tiền bạc nó khiến ta | Đã gặp ở |
| --- | --- | --- | --- |
| Sống sót | chỉ đếm kẻ còn nhìn thấy | phóng đại cơ hội thành công | bài 5, mục 3 |
| Lạm phát lối sống | chi phình theo thu nhập | tiêu mất khoản tăng lương | bài 2, mục 4 |
| Chạy theo lợi nhuận | lãi cao làm tắt hoài nghi | lao vào "quá tốt để là thật" | mục 5, bài 11 |
| Lạc quan + ảo tưởng kiểm soát | rủi ro là của người khác | tin mình rút kịp trước khi sập | mục 6, bài 12 |
| **Bất đối xứng lỗ–lãi** | mất đau gấp đôi được vui | ôm khoản lỗ chờ "về bờ", chốt lời quá sớm | bài 8, bài 13 |
| **Thiên lệch hiện tại** | thích phần thưởng ngay | hoãn tiết kiệm, vay để tiêu | bài 7, bài 8 |
| **Neo** | con số đầu tiên kéo phần còn lại | thấy giá "giảm từ 2 triệu còn 1 triệu" là hời | bài 3, bài 4 |
| **Kế toán trong đầu** (*mental accounting*) | chia tiền theo "ngăn" tưởng tượng | tiêu thưởng Tết thoáng tay dù vẫn đang nợ | bài 7, bài 9 |
| **Chi phí chìm** (*sunk cost*) | tiếc cái đã mất, cố theo lao | góp thêm tiền vào khoản đã lỗ | bài 8 |
| **Xác nhận** (*confirmation bias*) | chỉ tìm bằng chứng ủng hộ điều mình tin | chỉ đọc tin tốt về mã mình đã mua | bài 13 |

Hai cái đáng dừng lại vì chúng ngược nhau và cùng gây hại:

- **Bất đối xứng lỗ–lãi** biến một khoản lỗ thành cái bẫy: vì mất đau hơn nên ta **không dám cắt lỗ**,
  cứ ôm chờ "về bờ". Mà toán học của việc về bờ rất phũ — mất càng sâu, phần phải lãi để hoàn vốn
  càng phi thực tế:

  ```
   phần phải lãi để về vốn = 1 / (1 − mức lỗ) − 1
  ```

  | Đã lỗ | Phải lãi bao nhiêu mới về vốn |
  | ---: | ---: |
  | −20% | +25,0% |
  | −30% | +42,9% |
  | −50% | **+100%** |
  | −90% | **+900%** |

  Lỗ 50% không cần lãi 50% để hoàn — cần lãi **100%**. Đây là lý do "cứ giữ, kiểu gì cũng về" là một
  trong những câu tự nhủ tốn tiền nhất, và vì sao nó gặp lại ở **bài 13**.

- **Chi phí chìm** là anh em của nó: tiền đã mất **không** nên có mặt trong quyết định hôm nay, nhưng
  vì tiếc nên ta lại góp thêm để "gỡ". Chỗ này đã có sẵn ở kho —
  [EG13 bài 1](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)
  gọi tên nó là **chi phí chìm** ở tầm nguyên lý kinh tế.

---

## 8. [bổ sung] Vì sao biết mà vẫn sai — và cách duy nhất chống lại

Đây là mục quan trọng nhất bài, vì nó chống lại cái phản xạ sai nhất sau khi học xong danh sách trên:
*"giờ biết rồi thì tôi sẽ tỉnh táo hơn."*

Không. Đọc xong bài này bạn **vẫn** sẽ dính thiên kiến, y như người biết ảo giác thị giác vẫn thấy
hai đường thẳng bằng nhau là dài ngắn khác nhau. Biết không xoá được thiên kiến, vì thiên kiến chạy
ở Hệ thống 1, còn cái biết nằm ở Hệ thống 2 — và Hệ thống 2 thì lười và hay ngủ đúng lúc cần.

Cách chống hiệu quả **không phải ý chí**, mà là **dựng sẵn cấu trúc từ lúc đầu óc còn tỉnh, để lúc
đầu óc mờ thì không cần quyết định nữa**. Cả khoá học này thật ra đã đầy những cấu trúc như vậy —
giờ mới thấy chúng chống thiên kiến gì:

| Cấu trúc đã học | Chống thiên kiến nào | Cơ chế |
| --- | --- | --- |
| Chuyển lương tự động vào các lọ ngay đầu tháng (bài 7) | thiên lệch hiện tại, lạm phát lối sống | quyết định một lần, khỏi quyết định lại mỗi tháng |
| Quỹ khẩn cấp có sẵn (bài 9) | quyết định trong hoảng loạn | có tiền nên không phải vay nóng lúc cùng quẫn |
| Ghi chép chi tiêu (bài 3) | kế toán trong đầu, trí nhớ chọn lọc | thay cảm giác bằng số thật |
| Bảng câu hỏi khẩu vị rủi ro (bài 12) | lạc quan, ảo tưởng kiểm soát | chốt mức chịu đựng **trước** khi thị trường động |
| Phép nhân "lãi ra cả năm" (mục 5) | chạy theo lợi nhuận | bật Hệ thống 2 trong ba giây |

Nguyên tắc chung, và là câu đáng mang ra khỏi cả bài:

> [!note]
> **Đừng sửa người, hãy sửa hệ thống.** Bạn không đáng tin vào lúc 11 giờ đêm trước một lời chào lãi
> cao hay một cơn hoảng loạn thị trường. Nên hãy để **con người tỉnh táo hôm nay** ràng buộc sẵn
> **con người mờ mắt ngày mai** — bằng lệnh tự động, bằng quy tắc viết ra giấy, bằng một khoản đệm có
> sẵn. Ý chí là nguồn lực cạn nhanh; cấu trúc thì không mệt.

Đây đúng là điều mà bài blog của sách (C2 tr. 52–53) **mò ra được nhưng không có chữ để nói**: nó
nhận ra người có tiền vẫn sập bẫy, nhưng không có khung nên chỉ kết được ở lời khuyên tỉnh táo. Có
khung thiên kiến thì lời khuyên đổi hẳn: không phải "tỉnh táo hơn", mà "dựng rào trước khi cần".

---

## 9. Cầu sang bài 11: vì sao người có tiền vẫn dính Ponzi

Cả bài này tồn tại để **bài 11** có chỗ tựa. Câu hỏi mở đầu bài blog của
sách — *"Người có tiền thường không ngu ngốc, vậy vì sao vẫn dính?"* (C2 tr. 52) — bây giờ trả lời
được, và trả lời bằng chính bốn mảnh vừa gom:

| Cái bẫy dùng | Thiên kiến bị lợi dụng | Đã ở mục |
| --- | --- | --- |
| khoe người thắng, giấu người thua | sống sót | 3 |
| lãi hứa cao ngất | chạy theo lợi nhuận | 5 |
| *"anh sẽ rút trước khi nó sập"* | lạc quan, ảo tưởng kiểm soát | 6 |
| đã lỡ bỏ tiền vào, tiếc nên rủ thêm người | chi phí chìm, xác nhận | 7 |
| người quen giới thiệu, ai cũng chơi | bầy đàn | 7 |

Lừa đảo tài chính **không tấn công vào sự thiếu hiểu biết** — nó tấn công vào những phản xạ mà **mọi
người, kể cả người giỏi, đều có sẵn**. Đó là lý do nạn nhân Ponzi thường không phải người kém hiểu
biết, và vì sao câu trả lời không bao giờ là "tại họ ngu". Bài 11 sẽ mổ xẻ cơ chế Ponzi và CFD; bài
này đã đặt sẵn cái tên cho từng cú đánh mà chúng dùng.

---

## 10. Tự thử

Bài vòng 2, không bắt buộc code. Nhưng năm câu này đáng ngồi nghĩ — và ba câu đầu có thể kiểm bằng
[`thuc_hanh/bai-10-tai-chinh-hanh-vi.py`](../thuc_hanh/bai-10-tai-chinh-hanh-vi.py).

1. **Phép nhân của bạn.** Tự đặt ra vài mức lãi nghe hấp dẫn — 4%/tháng, 10%/quý, 2%/tuần — và quy ra
   lãi cả năm bằng lãi kép. Mức nào vượt hẳn 8% thực của cả khoá? Con số nào khiến bạn phải dừng lại?

2. **Khoản tăng lương của chính bạn.** Lấy thu nhập và tiết kiệm hiện tại của bạn, giả sử được tăng
   lương 20%. Tính hai kịch bản như bảng mục 4 với con số của bạn: dồn hết khoản tăng vào tiết kiệm
   rút ngắn được bao nhiêu thời gian đạt một mục tiêu bạn đang nhắm?

3. **Về bờ khó tới đâu.** Với một khoản đang lỗ 40%, tính phần trăm phải lãi để hoàn vốn. So với cảm
   giác trực giác của bạn trước khi tính — bạn có đoán thấp hơn con số thật không? Đó chính là thiên
   kiến đang hoạt động.

4. **Soi lại chín bài trước.** Chọn một quyết định tài chính thật bạn từng làm và tiếc. Nó dính thiên
   kiến nào trong bảng mục 7? Có **cấu trúc** nào ở mục 8 mà nếu dựng sẵn thì đã chặn được nó không?

5. **Rào cho chính mình.** Viết ra **một** lệnh tự động hoặc một quy tắc-viết-ra-giấy mà bạn sẽ dựng
   trong tháng này để "con người tỉnh táo hôm nay" ràng buộc "con người mờ mắt ngày mai". Càng cụ thể
   càng tốt: chuyển bao nhiêu, vào ngày nào, vào đâu.

---

## 11. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Tài chính hành vi | Behavioral finance | Ngành nghiên cứu các sai lệch có hệ thống của con người trong quyết định tiền bạc |
| Thiên kiến nhận thức | Cognitive bias | Lỗi phán đoán lặp lại theo một hướng đoán trước được, do cách não vận hành |
| Hệ thống 1 / Hệ thống 2 | System 1 / System 2 | Tư duy nhanh–cảm tính so với chậm–logic; thiên kiến là chỗ 1 trả lời thay 2 |
| Thiên kiến sống sót | Survivorship bias | Chỉ đếm kẻ còn nhìn thấy được; mẫu số (người thất bại) bị xoá — C2 tr. 10 |
| Lạm phát lối sống | Lifestyle creep | Chi tiêu phình theo thu nhập, làm khoản tăng lương biến mất — C2 tr. 17 |
| Chạy theo lợi nhuận | Return chasing | Lãi hứa càng cao càng làm tắt câu hỏi "có thật không" — C2 tr. 52 |
| Thiên kiến lạc quan | Optimism bias | Tin rủi ro xấu xảy ra với người khác chứ không với mình — C2 tr. 53 |
| Ảo tưởng kiểm soát | Illusion of control | Tin mình điều khiển được thứ vốn do may rủi (canh đỉnh, rút kịp) — C2 tr. 53 |
| Bất đối xứng lỗ–lãi | Loss aversion | Mất đau hơn được vui chừng gấp đôi; khiến ta ngại cắt lỗ |
| Thiên lệch hiện tại | Present bias | Ưu ái phần thưởng ngay hơn phần thưởng lớn hơn ở tương lai; kẻ thù của lãi kép |
| Neo | Anchoring | Con số đầu tiên nghe được kéo mọi ước lượng sau về phía nó |
| Kế toán trong đầu | Mental accounting | Chia tiền theo "ngăn" tưởng tượng, tiêu ngăn này thoáng tay dù ngăn kia đang nợ |
| Chi phí chìm | Sunk cost | Tiếc cái đã mất nên cố theo lao; tiền đã mất không nên có mặt trong quyết định hôm nay |
| Thiên kiến xác nhận | Confirmation bias | Chỉ tìm bằng chứng ủng hộ điều mình đã tin |
| Tâm lý bầy đàn | Herding | Làm theo đám đông vì "ai cũng làm thế" |

---

## 12. Câu hỏi tự kiểm tra

1. Bài này có thêm kiến thức mới nào vào sách không? Nếu không, việc của nó là gì?
2. Sách chạm vào tài chính hành vi mấy lần, ở những trang nào? Lần nào gọi đúng tên?
3. Hệ thống 1 và Hệ thống 2 khác nhau ra sao? Thiên kiến nằm ở đâu trong hai cái đó?
4. Vì sao "biết một thiên kiến" không đủ để thoát khỏi nó?
5. Thiên kiến sống sót là gì? Vì sao 100 tấm gương thành công có thể ứng với xác suất chỉ 10%?
6. Sách dùng thiên kiến sống sót để phản biện ai, về điều gì?
7. Lạm phát lối sống là gì? Hai đại lượng tâm lý nào đứng sau nó?
8. Người ở bài 3 được tăng lương ròng 3,2tr. Dồn hết khoản tăng vào tiết kiệm thì tỷ lệ giữ lại thành
   bao nhiêu, và quỹ khẩn cấp xây nhanh hơn bao nhiêu?
9. Vì sao khoảnh khắc tăng lương là thời điểm tốt nhất để nâng tỷ lệ tiết kiệm?
10. Viết phép thử một dòng cho lời hứa "lãi 20%/tháng". Nó ra bao nhiêu một năm? So với 8% thực thế nào?
11. Ẩn dụ Lọ Lem của Buffett nói về hai thiên kiến nào? Vì sao "tôi sẽ rút trước khi sập" hiếm khi thành?
12. Đang lỗ 50% thì phải lãi bao nhiêu mới về vốn? Viết công thức. Thiên kiến nào khiến người ta ôm lỗ?
13. Phân biệt bất đối xứng lỗ–lãi với chi phí chìm.
14. Vì sao cách chống thiên kiến hiệu quả không phải ý chí mà là cấu trúc? Nêu ba cấu trúc đã học và
    mỗi cái chống thiên kiến gì.
15. Giải thích câu "đừng sửa người, hãy sửa hệ thống" bằng lời của bạn.
16. Vì sao người có tiền, không ngu ngốc, vẫn dính Ponzi? Ghép ít nhất ba thiên kiến vào câu trả lời.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 10 — [bổ sung] TÀI CHÍNH HÀNH VI: vì sao biết mà vẫn sai            ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  VIỆC CỦA BÀI: không thêm kiến thức — DỰNG KHUNG cho 4 mảnh rời của      ║
║     sách, gọi đúng tên, làm chỗ tựa cho bài 11 (Ponzi)                  ║
║     sách chạm 4 lần, chỉ gọi đúng tên 1 lần:                            ║
║        sống sót (tr.10) · lối sống (tr.17) · tham lam (tr.52) ·         ║
║        Lọ Lem (tr.53) — chỉ "sống sót" được gọi tên                    ║
║                                                                          ║
║  HAI HỆ THỐNG: 1 nhanh–cảm tính · 2 chậm–logic                          ║
║     thiên kiến = hệ 1 trả lời thay hệ 2, sai theo hướng đoán trước      ║
║     BIẾT KHÔNG ĐỦ ĐỂ THOÁT — cái biết ở hệ 2, quyết định ở hệ 1         ║
║                                                                          ║
║  SỐNG SÓT (tr.10)  chỉ đếm kẻ còn thấy; mẫu số bị xoá                   ║
║     100 gương thành công có thể ứng xác suất chỉ 10% — lệch 10 lần      ║
║     sách dùng nó phản biện chính Kiyosaki                               ║
║                                                                          ║
║  LỐI SỐNG (tr.17)  chi phình theo lương -> khoản tăng biến mất          ║
║     tăng ròng 3,2tr: để phình -> giữ 15,5%; dồn hết -> giữ 29,6%        ║
║     quỹ khẩn cấp: 20,9 tháng so với 11,0 tháng — nhanh gần gấp đôi      ║
║     tăng lương = thời điểm TỐT NHẤT nâng tiết kiệm (chưa quen tiền)     ║
║                                                                          ║
║  THAM LAM (tr.52)  lãi cao tắt hoài nghi                                ║
║     PHÉP THỬ 1 DÒNG: nhân lãi ra cả năm bằng lãi kép, cả nền KT làm nổi?║
║     "20%/tháng" = (1,2)^12 − 1 = 791,6%/năm = ×99 so với 8% thực        ║
║     -> không hoạt động thật nào bền; nguồn tiền = người vào sau (Ponzi) ║
║                                                                          ║
║  LỌ LEM (tr.53)  lạc quan + ảo tưởng kiểm soát                          ║
║     tiệc tàn lúc 0h nhưng đồng hồ KHÔNG CÓ KIM -> ai cũng nán thêm      ║
║     "tôi rút kịp trước khi sập" cần biết 2 mốc, mốc ra thì không thấy   ║
║                                                                          ║
║  BẤT ĐỐI XỨNG LỖ–LÃI: mất đau gấp đôi -> ngại cắt lỗ                    ║
║     về vốn = 1/(1−lỗ) − 1:  −50% cần +100% · −90% cần +900%             ║
║                                                                          ║
║  CÁCH CHỐNG = CẤU TRÚC, KHÔNG PHẢI Ý CHÍ                                ║
║     "ĐỪNG SỬA NGƯỜI, HÃY SỬA HỆ THỐNG"                                  ║
║     người tỉnh hôm nay ràng buộc người mờ mắt ngày mai:                 ║
║        lệnh tự động (bài 7) · quỹ khẩn cấp (bài 9) ·                    ║
║        ghi chép (bài 3) · bảng khẩu vị rủi ro (bài 12)                  ║
║                                                                          ║
║  CẦU SANG BÀI 11: người có tiền KHÔNG ngu vẫn dính Ponzi — vì lừa đảo   ║
║     đánh vào PHẢN XẠ ai cũng có, không đánh vào sự thiếu hiểu biết      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn. Bốn chỗ sách
  chạm vào chủ đề: **thiên kiến sống sót** ở quy tắc 3 Kim tứ đồ (**tr. 10**), **lạm phát lối sống**
  trong bài tài sản ròng (**tr. 17**), *"Sự tham lam"* và câu *"Người có tiền thường không ngu ngốc"*
  trong bài blog phụ lục (**tr. 52**), ẩn dụ **Lọ Lem** của Buffett (**tr. 53**). Bài này gom bốn chỗ
  ấy lại; mọi câu trong ngoặc kép là trích nguyên từ các trang trên.
- **Toàn bộ khung là [bổ sung]** — hai tập sách **không có** phần tài chính hành vi. Các thuật ngữ
  (hai hệ thống tư duy, bất đối xứng lỗ–lãi, thiên lệch hiện tại, neo, ảo tưởng kiểm soát, chi phí
  chìm…) là kiến thức phổ thông của ngành, đưa vào để **gọi tên** những hiện tượng sách đã mô tả mà
  không đặt tên. Bài này **không dẫn công trình gốc** của từng thuật ngữ — nêu chúng ở mức khái niệm
  đủ dùng, không phải mức học thuật.
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-10-tai-chinh-hanh-vi.py`](../thuc_hanh/bai-10-tai-chinh-hanh-vi.py).
  Ba bảng số của bài (lạm phát lối sống ở mục 4, phép nhân "lãi ra cả năm" ở mục 5, bất đối xứng
  lỗ–lãi ở mục 7) do tệp này tính, chạy hai lần ra giống hệt nhau. Mỗi con số kèm công thức một dòng
  để tự kiểm bằng tay: `(1 + lãi tháng)^12 − 1` và `1 / (1 − mức lỗ) − 1`.
- **Số liệu lấy nguyên từ bài trước:** thu nhập ròng 16tr, tỷ lệ giữ lại thực tế 15,5% (2,48tr/tháng)
  và quỹ khẩn cấp mục tiêu 62,20tr — đều từ [bài 7](bai_07_phan_bo_thu_nhap.md) và
  [bài 9](bai_09_bao_ve.md); lợi suất thực 8%/năm dùng suốt khoá (bài 1). Khoản tăng lương 3,2tr là
  **giả định** của bài này, không phải của sách.
- **Liên hệ chéo:**
  - Thiên kiến sống sót và quy tắc 3 Kim tứ đồ:
    [bài 5 mục 3](bai_05_kiem_tien.md#quy-tắc-3--chỗ-sách-phản-biện-chính-kiyosaki) và
    [mục 5](bai_05_kiem_tien.md#5-bổ-sung-quy-tắc-3-và-quy-tắc-4-kéo-về-hai-hướng).
  - Tỷ lệ giữ lại thực tế và cách đo:
    [bài 7 mục 8](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật).
  - Hợp đồng bảo hiểm liên kết đầu tư bị huỷ sớm vì mua như "gửi tiết kiệm lãi cao":
    [bài 9 mục 12](bai_09_bao_ve.md#12-đính-chính-ba-con-số-ở-trang-47-không-khớp-nhau).
  - Chi phí chìm ở tầm nguyên lý kinh tế:
    [EG13 bài 1](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md).
  - Ponzi và CFD, nơi cả khung này được dùng để giải thích: **bài 11**.
  - Khẩu vị rủi ro, nơi lạc quan và ảo tưởng kiểm soát được đo trước: **bài 12**.

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| 5 | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md) | C2 tr. 4–13 | 1 |
| 6 | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách | 1 |
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| **10** | **[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai ← *bạn đang ở đây* | ngoài sách | 2 |
| 11 | Nhận diện lừa đảo: Ponzi và CFD | C2 tr. 47–57 | 1 |
| 12 | Rủi ro, khẩu vị rủi ro, phân bổ tài sản | C1 tr. 25–33 | 1 |
| 13 | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
