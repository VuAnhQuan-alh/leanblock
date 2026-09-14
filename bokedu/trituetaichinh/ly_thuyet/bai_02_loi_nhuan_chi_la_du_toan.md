# Bài 2 — Lợi nhuận chỉ là dự toán

> [!info] Về bài này
> Bài học dựng từ **Phần II — Những đặc thù của báo cáo kết quả kinh doanh**: chương 4 *Lợi nhuận chỉ
> là dự toán* (PDF tr. 36–40), chương 5 *Phá giải bộ mã của báo cáo kết quả kinh doanh* (PDF tr. 41–48),
> chương 6 *Doanh thu — vấn đề là ở việc ghi nhận* (PDF tr. 49–53).
>
> **Vòng 1.** Chương 4 dạy **khái niệm kế toán duy nhất** mà cả cuốn sách chịu dạy. Chương 6 chỉ ra
> dòng dễ bị bóp méo nhất trên mọi báo cáo tài chính — dòng đầu tiên.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).
>
> **Cần đọc trước:** [Bài 0](bai_00_bat_dau_tu_dau.md) · [Bài 1](bai_01_nghe_thuat_tai_chinh.md) —
> mục 3① của bài 1 đã chạm vào ghi nhận doanh thu; bài này làm kỹ.
> ⚙️ **Code:** [`thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py`](../thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py)

---

## Mục lục

<!-- MUC-LUC -->

- [1. Hiểu lầm cần dọn trước](#1-hiểu-lầm-cần-dọn-trước)
- [2. Nguyên tắc phù hợp — khái niệm kế toán duy nhất của cả cuốn sách](#2-nguyên-tắc-phù-hợp--khái-niệm-kế-toán-duy-nhất-của-cả-cuốn-sách)
- [3. Đọc một báo cáo kết quả kinh doanh](#3-đọc-một-báo-cáo-kết-quả-kinh-doanh)
- [4. Phần trăm doanh thu — công cụ rẻ nhất của cả chương 5](#4-phần-trăm-doanh-thu--công-cụ-rẻ-nhất-của-cả-chương-5)
- [5. Báo cáo "hình thức" — cẩn thận với loại này](#5-báo-cáo-hình-thức--cẩn-thận-với-loại-này)
- [6. Một xu EPS đáng bao nhiêu doanh thu?](#6-một-xu-eps-đáng-bao-nhiêu-doanh-thu)
- [7. Ba tình huống không có đáp án](#7-ba-tình-huống-không-có-đáp-án)
- [8. Tyco — tăng doanh thu mà không tăng một đồng lợi nhuận](#8-tyco--tăng-doanh-thu-mà-không-tăng-một-đồng-lợi-nhuận)
- [9. Nhồi hàng vào kênh](#9-nhồi-hàng-vào-kênh)
- [10. Đối chiếu Việt Nam](#10-đối-chiếu-việt-nam)
- [11. Tự thử](#11-tự-thử)
- [12. Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
- [13. Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Hiểu lầm cần dọn trước

Chương 4 mở bằng cách gỡ một hiểu lầm mà sách cho là *"nghiêm trọng"* và gần như ai cũng mắc:

> [!quote]
> *"Chỉ cần chút ít khả năng tưởng tượng là bạn có thể kết luận, báo cáo kết quả kinh doanh cho biết
> doanh nghiệp đã thu được bao nhiêu tiền mặt trong giai đoạn đó, chi tiêu bao nhiêu, và còn lại bao
> nhiêu… đúng chứ?*
>
> ***Nhưng, không đâu.*** *Ngoại trừ một vài doanh nghiệp rất rất nhỏ làm kế toán theo kiểu ấy — được
> gọi là **kế toán dựa trên tiền mặt** — quan niệm như thế về báo cáo kết quả kinh doanh và lợi nhuận
> là **một sự hiểu sai cơ bản**."* — ch. 4 · PDF tr. 37

Sách dựng luận điểm bằng hai câu trích ở ngay đầu chương. Peter Drucker: *"lợi nhuận là tiêu chí tối
cao của doanh nghiệp."* Rồi Laurence J. Peter, tác giả *The Peter Principle*: *"nếu chúng ta không
biết mình đang đi đâu, rất có thể rốt cuộc chúng ta sẽ dừng lại ở một chốn khác."*

Ghép lại thành lời cảnh báo: lợi nhuận là thứ bạn bị đánh giá theo, nên nếu **không hiểu nó được
tính thế nào**, bạn không thể tác động vào nó một cách có chủ đích.

---

## 2. Nguyên tắc phù hợp — khái niệm kế toán duy nhất của cả cuốn sách

Sách tuyên bố ngay từ chương 3 rằng nó *"sẽ không dạy bạn về kế toán"*. Chương 4 phá lệ đúng một lần:

> [!quote]
> **Nguyên tắc phù hợp** (*matching principle*): *"Hãy khớp doanh thu cho phù hợp với chi phí liên
> quan để xác định lợi nhuận của một kỳ sổ sách — thường là một tháng, một quý hoặc một năm."*
> — ch. 4 · PDF tr. 38

Nói cách khác: **chi phí đi theo doanh thu mà nó tạo ra, không đi theo lúc tiền rời khỏi tài khoản.**

### Chiếc xe tải

Ví dụ của sách: công ty chuyển phát mua xe tải tháng Một, dùng ba năm. Sách nói chi phí *"sẽ được
tính khấu hao trong suốt ba năm sử dụng, với mức khấu hao **1/36** chi phí mua xe"* mỗi tháng.

| Tháng | Kế toán tiền mặt | Nguyên tắc phù hợp |
| ---: | ---: | ---: |
| 1 | **−36.000** | −1.000 |
| 2 | 0 | −1.000 |
| 3 | 0 | −1.000 |
| 36 | 0 | −1.000 |
| 37 | 0 | 0 |
| **Tổng** | **−36.000** | **−36.000** |

⭐ **Hai cách cộng lại bằng nhau.** Chúng chỉ khác ở chỗ đặt chi phí vào **tháng nào**. Nhưng khác biệt
đó đổi cả câu chuyện: kế toán tiền mặt làm tháng Một trông như thảm hoạ và 35 tháng sau trông như
thiên đường.

### Xe hộp mực

Ví dụ thứ hai: công ty mực in mua cả xe hộp mực tháng Sáu để bán dần. Sách nói công ty *"sẽ không ghi
nhận chi phí mua toàn bộ số hộp mực vào tháng Sáu. Thay vào đó, công ty sẽ ghi nhận chi phí của từng
hộp mực **khi hộp mực được bán ra**."*

Đặt số — 1.200 hộp, giá vốn 10, bán 200 hộp/tháng giá 25:

| Tháng | Kế toán tiền mặt | Nguyên tắc phù hợp |
| ---: | ---: | ---: |
| 1 | **−7.000** | **+3.000** |
| 2 | +5.000 | +3.000 |
| 3 | +5.000 | +3.000 |

⭐ Cùng một doanh nghiệp, cùng một tháng. Kế toán tiền mặt báo **lỗ 7.000**; nguyên tắc phù hợp báo
**lãi 3.000**. Con số nào đúng? **Cả hai** — chúng trả lời hai câu hỏi khác nhau. Sách chọn câu thứ
hai, và đó chính là lý do báo cáo kết quả kinh doanh không cho biết tiền mặt
([bài 6](bai_06_loi_nhuan_khac_tien_mat.md)).

Sách mở rộng nguyên tắc này ra ba chỗ nữa (PDF tr. 38–39): **thuế** — trả theo quý nhưng ghi theo
tháng; **công ty dịch vụ** — công ty tư vấn phải khớp chi phí marketing, tài liệu, nghiên cứu với
giờ dịch vụ đã bán; và chính vì thế, **đóng sổ mất hai đến ba tuần** chứ không phải một ngày
(ch. 2 · PDF tr. 17).

Và câu kết luận của chương 4, đáng nhớ nguyên văn:

> [!quote]
> *"**Lợi nhuận luôn là dự toán — và bạn không thể chi tiêu một thứ được dự toán.**"*
> — ch. 4 · PDF tr. 40

---

## 3. Đọc một báo cáo kết quả kinh doanh

Chương 5 mở bằng một trò đùa có mục đích. Sách in một báo cáo *"nho nhỏ dễ thương"*:

```
   Doanh thu           100 đô-la
   Giá vốn hàng bán     50
   Lợi nhuận gộp        50
   Chi phí              30
   Thuế                  5
   Lợi nhuận thuần      15 đô-la
```

> [!quote]
> *"**Một cô bé lớp 4 sáng dạ cũng có thể hiểu ngay bài toán này** mà không cần chỉ bảo quá nhiều…
> Có khi cô bé còn chẳng cần đến máy tính. Nhưng giờ chúng ta hãy cùng xem một báo cáo kết quả kinh
> doanh **thực tế**… Nếu là bản chi tiết, báo cáo đó có thể **kéo dài nhiều trang**."*
> — ch. 5 · PDF tr. 41

Bộ xương thì y hệt — công ty mẫu ở phụ lục cũng chỉ là bảng trên với vài dòng chèn thêm. Và **mỗi
dòng chèn thêm là một chỗ để đặt câu hỏi**.

### Sáu thứ cần kiểm trước khi đọc con số nào

Chương 5 đưa một danh sách rất thực dụng (PDF tr. 42–47):

| Kiểm | Vì sao |
| --- | --- |
| **Nhãn tên** | có thể ghi *báo cáo lãi lỗ*, *báo cáo thu nhập*, *báo cáo hoạt động kinh doanh* — đều là một |
| **Đo cái gì** | cả doanh nghiệp? một bộ phận? một khu vực? |
| **Kỳ báo cáo** | tháng, quý, năm, hay luỹ kế từ đầu năm |
| **Đơn vị** | dò dòng chữ nhỏ ở đầu: *"triệu"* hay *"nghìn"* |
| **Thực tế hay hình thức** | xem mục 5 |
| **Chú thích** | Dell viết ngắn gọn; Tyco viết dài 7 đoạn — cả hai đều quan trọng |

> [!warning]
> Một mẹo nhận dạng của sách, nghe hiển nhiên nhưng hay bị bỏ qua: *"nếu bạn thấy nhãn tên 'bảng cân
> đối kế toán' hay 'báo cáo lưu chuyển tiền tệ' ở dòng trên cùng của một báo cáo bất kỳ, thì tức là
> **bạn đã cầm nhầm tài liệu**."*

Và **quy tắc quan trọng** mà chương 5 kết lại — sách in riêng thành một khối:

> [!quote]
> *"Hãy nhớ rằng nhiều số liệu trên báo cáo kết quả kinh doanh phản ánh **các ước tính và giả định**.
> Kế toán quyết định tính những giao dịch này, và bỏ qua các giao dịch khác…*
>
> *Đó là nghệ thuật tài chính. **Nếu bạn ghi nhớ kỹ điểm này, chúng tôi đảm bảo, trí tuệ tài chính
> của bạn đã vượt nhiều nhà quản lý.**"* — ch. 5 · PDF tr. 48

---

## 4. Phần trăm doanh thu — công cụ rẻ nhất của cả chương 5

Đây là thứ dùng được ngay, và nó là công cụ đọc báo cáo tốt nhất mà Phần II đưa ra.

> [!quote]
> *"'% doanh thu' chỉ đơn giản là một cách thể hiện độ lớn của chi phí xét trong tương quan với doanh
> thu. **Dòng doanh thu được coi như là điểm cho trước — điểm cố định** — và tất cả mọi thứ khác sẽ
> được so sánh với nó."* — ch. 5 · PDF tr. 45

Công ty mẫu, năm 2005:

| Khoản mục | Triệu đô-la | % doanh thu |
| --- | ---: | ---: |
| Doanh thu | 8.689 | 100,0% |
| Giá vốn hàng bán | 6.756 | **77,8%** |
| Lợi nhuận gộp | 1.933 | 22,2% |
| SG&A | 1.061 | 12,2% |
| Khấu hao | 239 | 2,8% |
| EBIT | 652 | 7,5% |
| Trả lãi | 191 | 2,2% |
| Thuế | 213 | 2,5% |
| **Lợi nhuận thuần** | **248** | **2,9%** |

⭐ **Đọc cột phải, không đọc cột giữa.** 77,8 xu trên mỗi đô-la doanh thu đi thẳng vào giá vốn. Còn
lại 22,2 xu để nuôi toàn bộ phần còn lại của doanh nghiệp — và cuối cùng chỉ còn **2,9 xu** là lợi
nhuận.

> [!example]
> Sách ra hẳn một bài tập ở cuối Phần V: *"lấy ba báo cáo kết quả kinh doanh gần đây, và tính toán
> phần trăm doanh thu cho từng khoản mục lớn. Sau đó, theo dõi kết quả theo thời gian."* Nếu một khoản
> mục tăng dần còn khoản khác giảm dần, bạn đang nhìn thấy **áp lực cạnh tranh** hiện ra bằng số.

Sách cũng nêu cách các doanh nghiệp dùng nó để quản trị: *"có thể các nhà điều hành cấp cao của doanh
nghiệp đã quyết định không để chi phí bán hàng vượt quá **12% doanh thu**. Nếu chi phí này vượt ra
khỏi con số 12%, thì bộ phận bán hàng phải cẩn trọng hơn nữa."*

---

## 5. Báo cáo "hình thức" — cẩn thận với loại này

Từ **hình thức** (*pro forma*) có hai nghĩa, và nghĩa thứ hai mới là chỗ sách cảnh báo. Đó là báo cáo
**loại trừ** các khoản phí một lần và bất thường.

Giả sử công ty mẫu phải xử lý một khoản nợ xấu 150 triệu nằm trong SG&A *(con số này do bài học đặt
ra để minh hoạ — sách không nêu)*:

| | Thực tế | Hình thức |
| --- | ---: | ---: |
| SG&A | 1.061 | 911 |
| EBIT | 652 | 802 |
| **Lợi nhuận thuần** | **248** | **329** |
| Biên lợi nhuận thuần | 2,9% | 3,8% |

⭐ Lợi nhuận thuần nhảy **gấp 1,3 lần** — và **không một con số nào ở cột phải là bịa đặt**.

Sách chỉ ra thông điệp ngầm rất chính xác:

> [!quote]
> *"Nhưng thường có một thông điệp ngầm, đi cùng với câu nói 'Này, mọi thứ không đến nỗi tệ như trông
> vậy đâu — chúng ta chỉ mất tiền vì xử lý nợ xấu thôi.' **Tất nhiên, việc xử lý nợ xấu quả thật đã
> diễn ra, và công ty quả thật đã mất tiền.**"* — ch. 5 · PDF tr. 44

Lời khuyên của sách: xem **cả hai**; nếu buộc phải chọn một, chọn **báo cáo thực tế**. Và sách khép
lại bằng một câu châm biếm đáng nhớ — những người hoài nghi mô tả báo cáo hình thức là báo cáo *"bày
ra toàn bộ thứ tệ hại, mà trên thực tế thỉnh thoảng lắm chúng mới xuất hiện."*

---

## 6. Một xu EPS đáng bao nhiêu doanh thu?

Chương 6 kể một tình huống mà sách nói rõ là **hợp pháp**. Một tập đoàn sắp *"thiếu một vài xu so với
con số thu nhập trên cổ phần ước tính"*. Nếu vậy, *"Phố Wall sẽ không hài lòng"*. Nên bộ phận tài
chính nghĩ đến bộ phận phần mềm:

> [!quote]
> *"Giả sử chúng ta thay đổi cách ghi nhận doanh thu của bộ phận này? Giả sử chúng ta **ghi nhận
> trước 75% thay vì 50%**? … Chỉ cần thay đổi — mà ở đây là ghi nhận thêm doanh thu, thế là thu nhập
> trên cổ phần sẽ lập tức được đẩy nhẹ lên mức mà Phố Wall mong muốn.*
>
> ***Điều thú vị là cách thay đổi như vậy không hề phạm pháp.***"* — ch. 6 · PDF tr. 51

Sách dừng ở đó. Câu hỏi nó **không** hỏi: một xu EPS thì bằng bao nhiêu doanh thu?

Công ty mẫu có 74 triệu cổ phiếu, EPS 3,35, thuế suất hiệu dụng 46,2%:

| Muốn đẩy EPS lên | Cần thêm LN thuần | Cần thêm doanh thu | % doanh thu năm |
| --- | ---: | ---: | ---: |
| **+1 xu** | 0,74 | **1,38** | **0,016%** |
| +2 xu | 1,48 | 2,75 | 0,032% |
| +5 xu | 3,70 | 6,88 | 0,079% |
| +10 xu | 7,40 | 13,76 | 0,158% |

*(Bảng giả định doanh thu ghi thêm **không kéo theo chi phí mới** — đúng với một dịch chuyển thời
điểm ghi nhận, vì chi phí đã phát sinh rồi.)*

⭐ **Một xu EPS = 0,016% doanh thu năm.** Một phần sáu nghìn. Nhỏ hơn sai số làm tròn của chính bản
báo cáo. Năm xu cũng chỉ là 0,08%.

> [!warning]
> Đây là lý do chương 6 kết luận rằng ghi nhận doanh thu là *"đấu trường phổ biến cho các gian lận
> tài chính"*, và liệt kê **Sunbeam, Cendant, Xerox, Rite Aid**. Không ai cần bịa ra một hợp đồng không
> tồn tại. **Chỉ cần dịch thời điểm ghi nhận của vài hợp đồng có thật qua ranh giới quý.**

---

## 7. Ba tình huống không có đáp án

Chương 6 nêu ba tình huống rồi tự trả lời: *"Chúng tôi không thể cho bạn đáp án chính xác cho những
câu hỏi trên, vì phương pháp kế toán ở mỗi nơi mỗi khác. **Nhưng đó chính là vấn đề: không hề có câu
trả lời chắc chắn nào.**"*

```
   ①  Tích hợp hệ thống: 6 tháng thiết kế + 12 tháng thực hiện.
      Khách "không nhận được bất kỳ giá trị thực nào cho đến khi hoàn tất".

   ②  Bán cho đại lý theo chính sách "viết hoá đơn mà không giao hàng":
      khách mua trước, bạn giữ kho hộ, giao sau.

   ③  Công ty kiến trúc: phí tính theo phần trăm chi phí xây dựng,
      trải suốt quá trình lên kế hoạch, xin phép và giám sát thi công.
```

Lấy tình huống ① — hợp đồng 1.800, kéo dài 18 tháng:

| Cách ghi nhận | Năm 1 (12 tháng) | Năm 2 (6 tháng) |
| --- | ---: | ---: |
| hoàn thành mới ghi (tháng 18) | **0** | 1.800 |
| theo % hoàn thành, đều 18 tháng | 1.200 | 600 |
| cột mốc: 50% khi duyệt thiết kế | 1.350 | 450 |
| ký hợp đồng là ghi hết | **1.800** | 0 |

⭐ Bốn cách, doanh thu năm 1 chạy từ **0 đến 1.800**. Nhưng **tổng thì luôn bằng 1.800** — không cách
nào "tạo ra" doanh thu. Chúng chỉ **dịch** nó qua lại giữa hai năm. Và đó đúng là đủ để làm vừa lòng
hoặc làm thất vọng Phố Wall một lần.

> [!warning]
> Sách cảnh báo thêm: *"những nguyên tắc này **có thể thay đổi**"*. Nghĩa là bạn có thể đang so sánh
> năm nay với năm ngoái mà không biết cách đếm đã đổi giữa chừng.

---

## 8. Tyco — tăng doanh thu mà không tăng một đồng lợi nhuận

Chương 6 trích **nguyên văn** một đoạn chú thích của Tyco. Đây là ví dụ hay nhất về việc *"đọc chú
thích"* đáng giá đến đâu:

> [!quote]
> *"Trước đây, các chi phí này được coi là 'đã thông qua' và vì vậy **không được tính vào doanh thu
> và giá vốn hàng bán** khai báo của Dịch vụ cơ sở hạ tầng. Có hiệu lực từ ngày 1 tháng Một năm 2004…
> công ty bắt đầu phản ánh các chi phí của hợp đồng phụ vào **cả doanh thu lẫn giá vốn hàng bán**,
> do đó doanh thu tăng và giá vốn hàng bán là **739 triệu đô-la**…"* — ch. 6 · PDF tr. 52

Cả hai dòng cùng tăng 739. Áp lên công ty mẫu:

| | Trước | Sau | Thay đổi |
| --- | ---: | ---: | ---: |
| Doanh thu | 8.689 | 9.428 | **+739** |
| Giá vốn hàng bán | 6.756 | 7.495 | +739 |
| **Lợi nhuận gộp** | 1.933 | 1.933 | **0** |
| Biên lợi nhuận gộp | 22,2% | 20,5% | **−1,7 điểm** |

⭐ Doanh thu tăng **8,5%**. Lợi nhuận gộp tăng **đúng bằng 0**. Biên lợi nhuận gộp **giảm** 1,7 điểm.

> [!example]
> Hai người nhìn cùng một bút toán và rút ra hai kết luận ngược nhau:

- người khoe **"tăng trưởng dòng đầu"** → doanh thu tăng 8,5%, tin tốt;
- người đọc **biên lợi nhuận** → biên gộp tụt 1,7 điểm, tin xấu.

Đó chính là lý do chương 5 dạy đọc **phần trăm doanh thu** chứ không đọc số tuyệt đối (mục 4).

> [!warning]
> Và sách đặt đúng câu hỏi khó: *"Về nguyên tắc, bất kỳ một thay đổi kế toán nào 'quan trọng' với
> kết quả kinh doanh đều phải được chú thích theo cách này. **Nhưng ai mới được quyền quyết định cái
> nào quan trọng, cái nào không?** Bạn đoán ra rồi đó: các kế toán viên."*

---

## 9. Nhồi hàng vào kênh

Trò cuối của chương 6, và nó có cùng cấu trúc với Xerox ở [bài 1](bai_01_nghe_thuat_tai_chinh.md):
**vay của tương lai**.

> [!quote]
> *"Các nhà sản xuất, thường phải chịu áp lực doanh thu từ Phố Wall, thường bị cám dỗ với việc giao
> những phần mềm **chưa được đặt hàng** cho các nhà phân phối vào cuối quý. (Biện pháp này được gọi
> là **nhồi hàng vào kênh**)."* — ch. 6 · PDF tr. 53

Doanh thu thật 1.000/quý, ổn định. Quý 4 nhồi thêm 150, quý 1 năm sau bị trả lại hết:

| Quý | Doanh thu thật | Doanh thu báo cáo | Chênh |
| --- | ---: | ---: | ---: |
| Q3 | 1.000 | 1.000 | 0 |
| Q4 | 1.000 | **1.150** | +150 |
| Q1 sau | 1.000 | **850** | −150 |
| Q2 sau | 1.000 | 1.000 | 0 |

⭐ Bốn quý cộng lại **bằng nhau**. Nhồi hàng không tạo ra một đồng doanh thu nào — nó **vay** doanh
thu của quý sau. Và quý sau phải vay tiếp của quý sau nữa, **mỗi lần một nhiều hơn**. Giống hệt vòng
xoáy của Xerox.

> [!note]
> Sách kể **một** công ty đi ngược lại, và đáng nhớ tên: **Macromedia** *"đã tự nguyện trình báo các
> ước tính về hàng tồn kho hiện đang do nhà phân phối nắm giữ, qua đó cho thấy các kênh phân phối sản
> phẩm của công ty không phải được nhồi nhét khống."* Tức là tự công bố một con số cho phép ai cũng
> kiểm tra được rằng mình không nhồi hàng.

> [!example]
> Cách phát hiện, dành cho người đọc báo cáo: khi doanh thu quý 4 vọt lên bất thường, xem **kỳ thu
> tiền bình quân (DSO)** của quý đó. Hàng nhồi đi ra khỏi kho nhưng tiền không về — nên DSO phình lên.
> Đó đúng là cách Andrew Shore lật tẩy Sunbeam ([bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) và bài 9).

---

## 10. Đối chiếu Việt Nam

Nguyên tắc phù hợp không phải đặc sản của GAAP — nó là **nền tảng của kế toán dồn tích ở mọi khung**,
kể cả VAS. Nên toàn bộ mục 2 đọc thẳng vào bối cảnh Việt Nam mà không cần chỉnh.

Ba chỗ đáng chú ý riêng khi đọc báo cáo Việt Nam:

- **Tên dòng khác nhau.** Báo cáo theo VAS tách *"doanh thu bán hàng và cung cấp dịch vụ"*, *"các
  khoản giảm trừ doanh thu"*, rồi mới đến *"doanh thu thuần"*. Sách chỉ có một dòng "doanh thu". Khi
  tính phần trăm doanh thu (mục 4), phải chốt trước mình dùng **doanh thu thuần**.
- **Chi phí tài chính không phải chỉ là lãi vay.** Báo cáo Việt Nam gộp lỗ chênh lệch tỷ giá và dự
  phòng đầu tư vào cùng dòng *"chi phí tài chính"*. Công ty mẫu của sách tách riêng *"trả lãi"*. Điều
  này quan trọng ở [bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md), khi tính hệ số thanh toán lãi vay.
- **Thuyết minh là nơi cất mọi thứ của mục 7 và mục 8.** Chính sách ghi nhận doanh thu, chính sách
  khấu hao, và mọi thay đổi so với năm trước đều nằm ở đó — không nằm trên bảng.

> [!example]
> Số thật: Vinamilk 2024 có doanh thu 52.576.991 và giá vốn 37.410.722 triệu đồng, tức giá vốn chiếm
> **71,2%** doanh thu, biên lợi nhuận gộp **28,8%**. So với công ty mẫu (77,8% / 22,2%): mỗi đồng doanh
> thu của Vinamilk để lại nhiều hơn **6,6 xu** để nuôi phần còn lại. Đó là toàn bộ giá trị của một dòng
> duy nhất trên báo cáo — và là lý do mục 4 đáng làm cho công ty của chính bạn.

---

## 11. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py`](../thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py) rồi
chạy lại. Không có lời giải.

1. **Xe tải hỏng sớm.** Ở mục 2, công ty ước tính xe dùng 3 năm nhưng nó hỏng sau 2 năm. Chi phí mỗi
   tháng lẽ ra phải là bao nhiêu? Hai năm đầu **lợi nhuận đã bị báo cao hơn thực tế** bao nhiêu?

2. **Hộp mực bán chậm.** Ở mục 2, đổi `BAN_MOI_THANG` xuống 50 hộp. Nguyên tắc phù hợp còn báo lãi
   không? Bao lâu thì bán hết lô? Điều gì xảy ra với **tiền mặt** trong lúc đó?

3. **Ngưỡng 12%.** Sách kể có công ty đặt trần chi phí bán hàng ở 12% doanh thu. Ở mục 4, SG&A của
   công ty mẫu đang là bao nhiêu phần trăm? Nếu trần là 12%, phải cắt bao nhiêu triệu?

4. **Hình thức bao nhiêu thì đủ.** Ở mục 5, tìm khoản "phí một lần" cần loại trừ để lợi nhuận thuần
   **gấp đôi** (496 triệu). Nó bằng bao nhiêu phần trăm SG&A? Con số đó có đáng ngờ không?

5. **EPS ở công ty nhỏ hơn.** Ở mục 6, giảm số cổ phiếu từ 74 xuống 20 triệu. Một xu EPS giờ bằng bao
   nhiêu phần trăm doanh thu? Công ty **ít cổ phiếu** hay **nhiều cổ phiếu** thì dễ bị cám dỗ hơn?

6. **Dự án dài hơn.** Ở mục 7, đổi thành 12 tháng thiết kế + 24 tháng thực hiện. Bốn cách ghi nhận
   giờ chênh nhau bao nhiêu ở năm 1? Vì sao **dự án càng dài thì khoảng trống phán đoán càng rộng**?

7. **Tyco ở doanh nghiệp biên mỏng.** Ở mục 8, thử với một doanh nghiệp có biên lợi nhuận gộp chỉ 10%
   (đổi `gia_von` cho phù hợp). Cùng bút toán 739 làm biên tụt bao nhiêu điểm? Vì sao biên càng mỏng
   thì tác động càng lớn?

8. **Nhồi hàng hai quý liên tiếp.** Ở mục 9, nhồi 150 ở Q4 rồi nhồi tiếp **200** ở Q1 để bù. Doanh
   thu báo cáo bốn quý ra sao? Đến quý nào thì không còn nhồi nổi nữa?

---

## 12. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Nguyên tắc phù hợp | matching principle | chi phí đi theo **doanh thu nó tạo ra**, không theo lúc chi tiền |
| Kế toán dồn tích | accrual accounting | ghi nhận lúc phát sinh — mặc định của mọi doanh nghiệp |
| Kế toán dựa trên tiền mặt | cash basis accounting | ghi nhận lúc tiền đổi tay — chỉ doanh nghiệp **rất** nhỏ |
| Ghi nhận / công nhận doanh thu | revenue recognition | quyết định **khi nào** doanh thu vào sổ |
| Báo cáo hình thức | pro forma statement | ① dự phóng tương lai, hoặc ② báo cáo **loại trừ** phí một lần |
| Phí tính một lần | one-time charge | dồn tin xấu vào một quý để các quý sau đẹp hơn |
| Xử lý nợ xấu | write-off | xoá một khoản không thu được — thường là "phí một lần" |
| Phần trăm doanh thu | percent of sales | mọi dòng chia cho doanh thu; công cụ đọc báo cáo của ch. 5 |
| Chênh lệch | variance | khác biệt giữa thực tế và ngân sách, hoặc giữa hai kỳ |
| Thu nhập trên cổ phần | earnings per share (EPS) | lợi nhuận thuần ÷ số cổ phiếu lưu hành |
| Viết hoá đơn mà không giao hàng | bill-and-hold | ghi doanh thu nhưng hàng vẫn nằm ở kho người bán |
| Nhồi hàng vào kênh | channel stuffing | đẩy hàng chưa đặt cho nhà phân phối cuối quý |
| 💼 Ghi nhận theo % hoàn thành | percentage-of-completion | trải doanh thu theo tiến độ — **cụm từ không có trong sách** |

---

## 13. Câu hỏi tự kiểm tra

1. Hiểu lầm mà chương 4 phải dọn ngay từ đầu là gì? Sách gọi nó là gì? (mục 1)
2. Ghép hai câu trích Drucker và Laurence Peter, sách muốn nói gì? (mục 1)
3. Phát biểu **nguyên tắc phù hợp**. Vì sao đây là khái niệm kế toán duy nhất sách chịu dạy? (mục 2)
4. Xe tải 36.000 dùng 3 năm: hai cách ghi khác nhau thế nào ở tháng Một, và **tổng** thì sao? (mục 2)
5. Xe hộp mực: kế toán tiền mặt báo lỗ 7.000, nguyên tắc phù hợp báo lãi 3.000. Cái nào đúng? (mục 2)
6. Vì sao đóng sổ mất hai đến ba tuần chứ không phải một ngày? (mục 2)
7. *"Lợi nhuận luôn là ___ — và bạn không thể ___ một thứ được ___ ."* Điền. (mục 2)
8. Kể sáu thứ cần kiểm trước khi đọc con số nào trên một báo cáo. (mục 3)
9. Thấy nhãn "bảng cân đối kế toán" ở đầu tài liệu bạn đang cầm để đọc lợi nhuận — nghĩa là gì? (mục 3)
10. Nêu "quy tắc quan trọng" mà chương 5 kết lại. (mục 3)
11. Công ty mẫu: giá vốn chiếm bao nhiêu phần trăm doanh thu? Còn lại bao nhiêu xu là lợi nhuận? (mục 4)
12. Vì sao đọc **phần trăm doanh thu** tốt hơn đọc số tuyệt đối? (mục 4)
13. Hai nghĩa của từ **"hình thức"** là gì? Nghĩa nào bị sách cảnh báo? (mục 5)
14. Loại trừ khoản nợ xấu 150 làm lợi nhuận thuần đổi bao nhiêu? Có con số nào bịa đặt không? (mục 5)
15. Nếu buộc phải chọn một báo cáo, sách khuyên chọn cái nào? (mục 5)
16. Công ty phần mềm đổi ghi nhận từ 50% lên 75%. Việc đó có **phạm pháp** không? (mục 6)
17. Một xu EPS của công ty mẫu bằng bao nhiêu doanh thu, và bằng bao nhiêu **phần trăm** doanh thu năm? (mục 6)
18. Vì sao ghi nhận doanh thu là "đấu trường phổ biến cho các gian lận tài chính"? Kể bốn công ty
    sách nêu tên. (mục 6)
19. Dự án 18 tháng, hợp đồng 1.800: doanh thu năm 1 chạy từ bao nhiêu đến bao nhiêu? **Tổng** thì sao? (mục 7)
20. Bút toán của Tyco làm doanh thu tăng 739 và giá vốn tăng 739. **Lợi nhuận gộp** đổi bao nhiêu?
    **Biên lợi nhuận gộp** đổi bao nhiêu? (mục 8)
21. Hai người nhìn cùng bút toán Tyco rút ra hai kết luận ngược nhau — họ nhìn vào cái gì? (mục 8)
22. *"Ai mới được quyền quyết định cái nào quan trọng, cái nào không?"* Sách trả lời gì? (mục 8)
23. Nhồi hàng vào kênh có tạo ra doanh thu không? Nó làm gì? (mục 9)
24. Macromedia đã làm gì khác với ngành? (mục 9)
25. Doanh thu quý 4 vọt bất thường — nên xem chỉ số nào để kiểm? (mục 9)
26. Khi tính phần trăm doanh thu trên báo cáo Việt Nam, phải chốt trước điều gì? (mục 10)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 2 — LỢI NHUẬN CHỈ LÀ DỰ TOÁN  (ch. 4–6, PDF tr. 36–53)              ║
╠══════════════════════════════════════════════════════════════════════════╣
║  HIỂU LẦM CẦN DỌN: báo cáo KQKD KHÔNG cho biết tiền vào tiền ra          ║
║     "một sự hiểu sai cơ bản"                                             ║
║                                                                          ║
║  ⭐ NGUYÊN TẮC PHÙ HỢP — khái niệm kế toán DUY NHẤT sách chịu dạy        ║
║     chi phí đi theo DOANH THU NÓ TẠO RA, không theo lúc chi tiền         ║
║        xe tải 36.000 / 3 năm    tiền mặt: −36.000 rồi 0                  ║
║                                 phù hợp:  −1.000 × 36 tháng              ║
║        xe hộp mực, tháng 1      tiền mặt: LỖ 7.000                       ║
║                                 phù hợp:  LÃI 3.000                      ║
║     → TỔNG luôn bằng nhau. Chỉ khác chỗ ĐẶT VÀO THÁNG NÀO.               ║
║                                                                          ║
║  ⭐ "LỢI NHUẬN LUÔN LÀ DỰ TOÁN — VÀ BẠN KHÔNG THỂ CHI TIÊU MỘT THỨ       ║
║      ĐƯỢC DỰ TOÁN."                                                      ║
║                                                                          ║
║  ĐỌC BÁO CÁO: nhãn tên · đo cái gì · kỳ · đơn vị · thực tế/hình thức ·   ║
║               chú thích                                                  ║
║                                                                          ║
║  ⭐ PHẦN TRĂM DOANH THU — công cụ rẻ nhất. Đọc CỘT PHẢI.                 ║
║     giá vốn 77,8%  →  còn 22,2 xu nuôi cả doanh nghiệp  →  lãi 2,9 xu    ║
║                                                                          ║
║  ⚠️ HÌNH THỨC (pro forma): loại nợ xấu 150 → LN thuần 248 → 329 (1,3×)   ║
║     không con số nào bịa. Nhưng "công ty quả thật ĐÃ MẤT TIỀN".          ║
║                                                                          ║
║  ⭐ MỘT XU EPS = 1,38 triệu doanh thu = 0,016% doanh thu năm             ║
║     → không ai cần bịa hợp đồng. Chỉ cần dịch vài hợp đồng CÓ THẬT       ║
║       qua ranh giới quý.                                                 ║
║                                                                          ║
║  DỰ ÁN 18 THÁNG, HĐ 1.800:  năm 1 ghi từ 0 đến 1.800 tuỳ cách            ║
║     nhưng TỔNG luôn 1.800 — chỉ DỊCH, không TẠO RA                       ║
║                                                                          ║
║  TYCO +739 vào CẢ doanh thu LẪN giá vốn:                                 ║
║     doanh thu +8,5%  ·  lợi nhuận gộp +0  ·  biên gộp −1,7 điểm          ║
║                                                                          ║
║  NHỒI HÀNG VÀO KÊNH: vay doanh thu của quý sau, mỗi lần phải vay         ║
║     nhiều hơn. Phát hiện bằng DSO.                                       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần II — Những đặc thù của báo cáo kết quả kinh doanh**, PDF tr. 35–73.
    - Ch. 4 *Lợi nhuận chỉ là dự toán*, PDF tr. 36–40
      — Drucker và Laurence J. Peter (tr. 36); **kế toán dựa trên tiền mặt** và *"một sự hiểu sai cơ
      bản"* (tr. 37); định nghĩa **nguyên tắc phù hợp** (tr. 38); ví dụ hộp mực, xe tải **1/36**,
      thuế theo quý, công ty tư vấn (tr. 38–39); mục đích của báo cáo — giám đốc bán hàng, marketing,
      nhân sự (tr. 39–40); *"lợi nhuận luôn là dự toán"* (tr. 40)
    - Ch. 5 *Phá giải bộ mã của báo cáo kết quả kinh doanh*, PDF tr. 41–48
      — bảng *"cô bé lớp 4"* (tr. 41); nhãn tên và *"cầm nhầm tài liệu"* (tr. 42);
      đo cái gì, kỳ báo cáo, đơn vị *"triệu"/"nghìn"* (tr. 43); **báo cáo hình thức** và cảnh báo
      (tr. 44); ba mục chính và trần 12% chi phí bán hàng (tr. 44–45); **dữ liệu so sánh** và
      **phần trăm doanh thu** (tr. 45–46); chú thích **Dell** và **Tyco** (tr. 47);
      **quy tắc quan trọng** (tr. 48)
    - Ch. 6 *Doanh thu — vấn đề là ở việc ghi nhận*, PDF tr. 49–53
      — nhập nhằng *"thu nhập"* và **QuickBooks** (tr. 49); **ba tình huống mù mờ** (tr. 50);
      công ty phần mềm **50% → 75%** và *"không hề phạm pháp"* (tr. 51); chú thích **Tyco 739 triệu**
      (tr. 52); giám đốc bán hàng và tiền thưởng (tr. 52–53); **nhồi hàng vào kênh**, **Macromedia**,
      và **Sunbeam · Cendant · Xerox · Rite Aid** (tr. 53)
  - Ch. 2, PDF tr. 17 — đóng sổ mất hai đến ba tuần
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 3, 4, 5, 6, 8
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 10](#10-đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py`](../thuc_hanh/bai-02-loi-nhuan-chi-la-du-toan.py):
  - bảng *"cô bé lớp 4"* của sách cộng trừ khớp ($100-50=50$; $50-30-5=15$);
  - xe tải: hai cách ghi nhận cộng lại **bằng nhau**, chốt bằng `assert`;
  - dự án 18 tháng: cả bốn cách ghi nhận **cộng lại đúng 1.800**, chốt bằng `assert`;
  - Tyco: lợi nhuận gộp **không đổi** và biên gộp **giảm**, chốt bằng `assert`;
  - nhồi hàng: bốn quý cộng lại bằng nhau, chốt bằng `assert`.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - ⭐ Toàn bộ [mục 6 — một xu EPS](#6-một-xu-eps-đáng-bao-nhiêu-doanh-thu) là **phép tính sách không
    làm**. Sách chỉ nói *"thiếu một vài xu"* mà không lượng hoá. Bảng giả định doanh thu ghi thêm
    không kéo theo chi phí mới — đúng với một dịch chuyển thời điểm ghi nhận, nhưng **là giả định của
    bài này**.
  - Khoản nợ xấu **150 triệu** ở [mục 5](#5-báo-cáo-hình-thức--cẩn-thận-với-loại-này), giá xe tải
    36.000, các thông số xe hộp mực, hợp đồng 1.800 ở [mục 7](#7-ba-tình-huống-không-có-đáp-án), và
    doanh thu 1.000/quý ở [mục 9](#9-nhồi-hàng-vào-kênh) — **do bài này đặt ra**; sách chỉ nêu tình
    huống bằng lời. Riêng **1/36**, **739 triệu**, **50% → 75%** là con số **của sách**.
  - Bảng "sáu thứ cần kiểm" ở [mục 3](#3-đọc-một-báo-cáo-kết-quả-kinh-doanh) do bài này gom lại từ
    văn xuôi rải trong chương 5.
  - [Mục 10 — Đối chiếu Việt Nam](#10-đối-chiếu-việt-nam) hoàn toàn nằm ngoài sách.
- **Liên hệ chéo:**
  - [Bài 1 mục 3①](bai_01_nghe_thuat_tai_chinh.md#3-bảy-chỗ-con-số-có-thể-nhảy--mà-không-ai-phạm-luật) — bốn thời điểm ghi nhận doanh thu và ví dụ máy photocopy.
  - [Bài 6](bai_06_loi_nhuan_khac_tien_mat.md) — vì sao lợi nhuận không phải tiền mặt, hệ quả trực tiếp của nguyên tắc phù hợp.
  - [Bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) — chi phí, ranh giới "trên vạch / dưới vạch",
    và các tầng lợi nhuận.
  - [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) và bài 9 — biên lợi nhuận gộp và DSO, hai thước đo mà mục 8 và mục 9 dựa vào.

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| **2** | **Lợi nhuận chỉ là dự toán** ← *bạn đang ở đây* | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
