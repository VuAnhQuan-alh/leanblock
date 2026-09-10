# Bài 9 — Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm

> Bài học dựa trên **C2 tr. 39–47** — Unit 4, Lesson 1 đến Lesson 3 của *Tài chính cá nhân 101,
> Class 2*. (Lesson 4 về Ponzi bắt đầu ở tr. 47 và thuộc **bài 11**.)
>
> **Cần đọc trước:** [Bài 8](bai_08_vay_va_tra_no.md) — bài này là thứ lẽ ra đã chặn khoản vay
> 13 triệu ở tháng Tết. Và [bài 6](bai_06_thue_thu_nhap_ca_nhan.md), vì mục 6 dùng lại đúng dòng
> **1% bảo hiểm thất nghiệp** đã bị trừ khỏi lương ở đó.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Về phần pháp lý:** mục 6 và mục 12 dẫn văn bản, tra ngày **09/09/2026**. Luật đổi thì con số
> đổi — kiểm lại ngày tra trước khi tin.
>
> **Code:** [`thuc_hanh/bai-09-bao-ve.py`](../thuc_hanh/bai-09-bao-ve.py)
> — Unit 4 định nghĩa nhiều, phân loại nhiều, nhưng gần như không tính gì. Tệp này tính hộ.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Ba lớp bảo vệ — khung mà sách không dựng](#1-ba-lớp-bảo-vệ--khung-mà-sách-không-dựng)
- [2. Lạm phát: định nghĩa, phân loại, nguyên nhân](#2-lạm-phát-định-nghĩa-phân-loại-nguyên-nhân)
- [3. [đính chính] Bát phở của chính sách rơi vào bậc "phi mã"](#3-đính-chính-bát-phở-của-chính-sách-rơi-vào-bậc-phi-mã)
- [4. [bổ sung] Chữ "tự nhiên" che một khoảng rất rộng](#4-bổ-sung-chữ-tự-nhiên-che-một-khoảng-rất-rộng)
- [5. [bổ sung] Lạm phát nối thẳng với bài 8: lãi suất thật](#5-bổ-sung-lạm-phát-nối-thẳng-với-bài-8-lãi-suất-thật)
- [6. Quỹ khẩn cấp, và [đính chính] hai danh sách không cộng lại được](#6-quỹ-khẩn-cấp-và-đính-chính-hai-danh-sách-không-cộng-lại-được)
- [7. [bổ sung] Bạn đã mua bảo hiểm thất nghiệp rồi — 1% ở bài 6](#7-bổ-sung-bạn-đã-mua-bảo-hiểm-thất-nghiệp-rồi--1-ở-bài-6)
- [8. [đính chính] "Gửi kỳ hạn 6 tháng" đá với chính trang 45](#8-đính-chính-gửi-kỳ-hạn-6-tháng-đá-với-chính-trang-45)
- [9. [bổ sung] Xây quỹ mất bao lâu, và giá của việc không có nó](#9-bổ-sung-xây-quỹ-mất-bao-lâu-và-giá-của-việc-không-có-nó)
- [10. Bảo hiểm: phép ẩn dụ áo mưa và ba lợi ích](#10-bảo-hiểm-phép-ẩn-dụ-áo-mưa-và-ba-lợi-ích)
- [11. [bổ sung] Nguyên tắc sách thiếu: chỉ bảo hiểm cái không tự gánh nổi](#11-bổ-sung-nguyên-tắc-sách-thiếu-chỉ-bảo-hiểm-cái-không-tự-gánh-nổi)
- [12. [đính chính] Ba con số ở trang 47 không khớp nhau](#12-đính-chính-ba-con-số-ở-trang-47-không-khớp-nhau)
- [13. [2026] Điều sách không thể biết: cuộc khủng hoảng bancassurance](#13-2026-điều-sách-không-thể-biết-cuộc-khủng-hoảng-bancassurance)
- [14. Tự thử](#14-tự-thử)
- [15. Từ điển thuật ngữ](#15-từ-điển-thuật-ngữ)
- [16. Câu hỏi tự kiểm tra](#16-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Ba lớp bảo vệ — khung mà sách không dựng

Unit 4 đặt ba chủ đề cạnh nhau — lạm phát, quỹ khẩn cấp, bảo hiểm — như ba bài rời. Chúng không
rời. Chúng là **cùng một câu hỏi ở ba quy mô**:

> Có một khoản tiền sắp mất đi. Ai chịu?

| Quy mô tổn thất | Ai chịu | Công cụ |
| --- | --- | --- |
| nhỏ, thường xuyên | bạn, bằng dòng tiền tháng này | ngân sách (bài 7) |
| vừa, thỉnh thoảng | bạn, bằng tiền đã để dành sẵn | **quỹ khẩn cấp** |
| lớn, hiếm | người khác, đổi lại một khoản phí đều | **bảo hiểm** |

Lạm phát thì khác: nó không phải một cú, nó là **rò rỉ liên tục** ăn vào cả ba lớp. Nên nó phải
đứng đầu.

Sách không dựng khung này, và đó là lý do phần bảo hiểm ở tr. 46 kết luận *"Tôi không tìm ra lý do
tại sao để không mua chúng"* — một câu chỉ đúng khi không có khung để hỏi **cái gì đáng bảo hiểm và
cái gì không**. [Mục 11](#11-bổ-sung-nguyên-tắc-sách-thiếu-chỉ-bảo-hiểm-cái-không-tự-gánh-nổi) trả
lời câu đó bằng số.

---

## 2. Lạm phát: định nghĩa, phân loại, nguyên nhân

C2 tr. 39–43. Định nghĩa của sách gọn và đúng: **sự tăng giá liên tục của hàng hoá dịch vụ theo
thời gian và sự mất giá của một loại tiền tệ.** Và câu quan trọng nhất, ở tr. 39:

> *"Bạn trông thấy giá tăng. Thực tế, sức mua của đồng tiền bị giảm xuống theo thời gian."*

Đây là cách nhìn đúng: bạn không nghèo đi vì phở đắt lên, bạn nghèo đi vì **tiền của bạn nhỏ lại**.

**Ba bậc lạm phát**, tr. 39–40:

| Bậc | Khoảng | Sách mô tả |
| --- | --- | --- |
| lạm phát tự nhiên | 0% – dưới 10% | nền kinh tế hoạt động bình thường, đời sống ổn định |
| lạm phát phi mã | 10% – dưới 1000% | nền kinh tế *"bị biến động trầm trọng"* |
| siêu lạm phát | trên 1000% | hậu quả rất lớn, quốc gia rất vất vả để khôi phục |

**Sáu nguyên nhân**, tr. 40–41: cầu kéo, chi phí đẩy, cơ cấu, cầu–cung thay đổi, xuất khẩu, nhập
khẩu. Phần này chép được, không có gì để bắt bẻ.

**Ảnh hưởng**, tr. 42, chia hai phía. Tiêu cực: thu nhập thực tế giảm, mất cân bằng giàu nghèo, ảnh
hưởng các khoản nợ quốc gia. Tích cực: kích thích tiêu dùng và vay nợ nên giảm thất nghiệp, thúc
đẩy quốc gia đầu tư.

Chú ý một chỗ trống ở đây: sách nói lạm phát **ảnh hưởng đến các khoản nợ của quốc gia**, nhưng
không nói điều tương đương với **hộ gia đình** — mà đó mới là thứ người đọc dùng được. Lạm phát ăn
vào giá trị thật của một khoản nợ trả góp lãi cố định. Người có khoản vay mua nhà 20 năm ở lãi cố
định được lạm phát giúp, người gửi tiết kiệm bị lạm phát lấy đi. Đó là kết quả trực tiếp từ công
thức lợi suất thực ở [mục 5](#5-bổ-sung-lạm-phát-nối-thẳng-với-bài-8-lãi-suất-thật).

---

## 3. [đính chính] Bát phở của chính sách rơi vào bậc "phi mã"

tr. 39 mở đầu bằng một ví dụ đời thường:

> *"Năm ngoái bạn ra đầu ngõ ăn bát phở 25 ngàn, thì giờ giá nó lên 35-40 ngàn."*

**Năm ngoái → giờ.** Một năm. Đem chính con số ấy xếp vào chính bảng của sách ở trang sau:

| Giá mới | Mức tăng | Bậc theo bảng tr. 39–40 |
| ---: | ---: | --- |
| 35.000đ | **+40%** | **lạm phát phi mã** |
| 40.000đ | **+60%** | **lạm phát phi mã** |

Sách dùng ví dụ này để minh hoạ lạm phát thường ngày ở Việt Nam, rồi cách đó một trang xếp mọi mức
từ 10% trở lên vào bậc mà chính sách mô tả là *"nền kinh tế của quốc gia đó bị biến động trầm
trọng"*.

Ví dụ hợp lý ngay nếu đọc là **nhiều năm**. Từ 25 lên 37,5 ngàn:

| Qua bao lâu | Lạm phát mỗi năm | Bậc |
| ---: | ---: | --- |
| 1 năm | 50,00% | phi mã |
| 2 năm | 22,47% | phi mã |
| 3 năm | 14,47% | phi mã |
| **5 năm** | **8,45%** | **tự nhiên** |
| 10 năm | 4,14% | tự nhiên |

Phải qua ít nhất **5 năm** thì mức tăng ấy mới về được bậc "tự nhiên".

### Và một chỗ nữa: giá một món không phải lạm phát

Lạm phát đo **cả một rổ hàng hoá**. Một bát phở có thể tăng 40% vì giá thịt bò, vì tiền thuê mặt
bằng, vì quán đổi chủ, vì khu phố lên đời — không con nào trong đó nói được gì về đồng tiền.

Đây không phải bắt bẻ chữ nghĩa: đó chính là cái bẫy khiến người ta tin lạm phát cao hơn thực tế.
Bạn nhớ giá những món bạn mua thường xuyên và nhớ chúng khi chúng tăng, không nhớ những món đứng
yên. Muốn biết lạm phát thì tra chỉ số giá tiêu dùng công bố, đừng ước lượng từ bát phở đầu ngõ.

---

## 4. [bổ sung] Chữ "tự nhiên" che một khoảng rất rộng

Sách phân loại xong rồi thôi, không tính một phép nào về hệ quả. Mà cái nhãn "tự nhiên" cho cả
khoảng 0–10% mới là chỗ cần con số:

| Lạm phát | Sách gọi là | Sức mua còn một nửa sau | 1 triệu sau 20 năm còn |
| ---: | --- | ---: | ---: |
| 2% | tự nhiên | 35,0 năm | 0,67tr |
| 4% | tự nhiên | 17,7 năm | 0,46tr |
| 6% | tự nhiên | 11,9 năm | 0,31tr |
| **9%** | **tự nhiên** | **8,0 năm** | **0,18tr** |
| 10% | phi mã | 7,3 năm | 0,15tr |

Công thức là một dòng: `số năm giảm nửa = ln 2 / ln(1 + lạm phát)`.

**Đầu trên của bậc "tự nhiên" — 9%/năm — làm mất một nửa sức mua trong 8 năm.** Sau 20 năm, một
triệu còn 180 nghìn. Gọi mức đó là "tự nhiên" và xếp nó chung một ô với 2% là làm mờ đi một khác
biệt gần bốn lần về tốc độ.

Đáng chú ý: **9% và 10% gần như giống hệt nhau về hậu quả** (8,0 năm so với 7,3 năm), nhưng bảng
của sách đặt chúng ở hai bậc khác nhau, một bậc "bình thường" và một bậc "biến động trầm trọng".
Đường ranh 10% là quy ước, không phải chỗ có gì thay đổi.

### Ngưỡng "siêu lạm phát" cũng là quy ước

Sách đặt siêu lạm phát ở **trên 1000%/năm**. Định nghĩa được trích dẫn nhiều nhất trong nghiên cứu
kinh tế (Phillip Cagan, 1956) đặt ở **50%/tháng**, tức khoảng **12.875%/năm** — cao gấp 13 lần
ngưỡng của sách.

Không phải cái nào sai; đó là hai quy ước khác nhau. Nhưng con số 1000% nên được đọc như một mốc
của tài liệu phổ thông, không phải một hằng số tự nhiên.

---

## 5. [bổ sung] Lạm phát nối thẳng với bài 8: lãi suất thật

Đây là mối nối mà cả Unit 4 lẫn Unit 3 đều không bắc:

```
lợi suất thực = lợi suất danh nghĩa − lạm phát
```

Gửi tiết kiệm 100 triệu, lạm phát 4%/năm:

| Lãi ngân hàng | Thực | Sau 5 năm sức mua còn | Sau 10 năm |
| ---: | ---: | ---: | ---: |
| 2,0% | −2,0% | 90,39tr | 81,71tr |
| **4,0%** | **0,0%** | **100,00tr** | **100,00tr** |
| 5,0% | +1,0% | 105,10tr | 110,46tr |
| 6,0% | +2,0% | 110,41tr | 121,90tr |
| 8,0% | +4,0% | 121,67tr | 148,02tr |

Ba hệ quả dùng được ngay:

1. **Gửi ngân hàng ở mức lãi bằng lạm phát là giữ nguyên sức mua, không phải sinh lời.** Số dư trên
   sổ tăng, sức mua đứng yên. Đây là điều phải chấp nhận với quỹ khẩn cấp, và
   [mục 9](#9-bổ-sung-xây-quỹ-mất-bao-lâu-và-giá-của-việc-không-có-nó) cho thấy vì sao vẫn đáng.
2. **Lợi suất thực 8% mà cả khoá dùng** (từ [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md), theo giả
   định C1 tr. 31 là 12% danh nghĩa trừ 4% lạm phát) chính là dòng cuối bảng này.
3. **Mảnh đất ở [bài 8 mục 4](bai_08_vay_va_tra_no.md#4-bài-toán-mảnh-đất-cùng-một-khoản-lãi-khi-thì-lãi-khi-thì-lỗ)**
   giữ 5 năm cho lợi suất thực âm — cùng một phép trừ này.

Và chiều ngược lại, thứ sách chỉ nói ở tầm quốc gia: **lạm phát ăn vào giá trị thật của khoản nợ
lãi cố định.** Khoản vay mua nhà 9%/năm với lạm phát 4% là khoản nợ thực 5%. Đó là lý do
[bài 8 mục 9](bai_08_vay_va_tra_no.md#9-bổ-sung-khoản-13-triệu-của-bài-7-trả-nợ-hay-bỏ-vào-ffa) xếp
nợ mua nhà khác hẳn nợ vay nóng.

---

## 6. Quỹ khẩn cấp, và [đính chính] hai danh sách không cộng lại được

C2 tr. 43–45. Định nghĩa tốt: tiền để dành cho *"ốm đau, bệnh tật, thất nghiệp, mất mát/hỏng hóc đồ
dùng thiết yếu trong nhà"*. Và sách phân biệt rất rõ ràng ở tr. 45:

| | Quỹ khẩn cấp (*Emergency Fund*) | Quỹ chi tiêu (*Sinking Fund*) |
| --- | --- | --- |
| Bản chất | khoản **không lường trước** | khoản **đã lên kế hoạch** |
| Kỳ hạn | không cố định, phát sinh bất cứ lúc nào | có kỳ hạn định sẵn |
| Ví dụ của sách | iPhone **rơi vỡ, mất** | iPhone cũ vẫn dùng được, **muốn đổi máy** |

Ví dụ iPhone là ví dụ hay nhất Unit 4: cùng một món hàng, cùng một số tiền, nhưng lấy từ hai chỗ
khác nhau tuỳ theo bạn **có chọn** hay **bị bắt** phải chi.

Sau đó là ba bậc **3 / 6 / 12 tháng chi tiêu thiết yếu**, mỗi bậc một danh sách tiêu chí.

### Hai danh sách đầu không phải hai bậc — chúng là bảy câu hỏi hỏi hai lần

Đọc kỹ danh sách 3 tháng (tr. 43) cạnh danh sách 6 tháng (tr. 44), chúng ghép cặp gần như từng
dòng. Cách ghép dưới đây là của bài học, không phải của sách — sách để hai danh sách rời nhau:

| Trục | Đầu thấp → 3 tháng | Đầu cao → 6 tháng |
| --- | --- | --- |
| sức khoẻ | tương đối khoẻ mạnh, lối sống khoẻ mạnh | thể trạng yếu, bệnh mãn tính, hoạt động mạo hiểm |
| nợ | không có nợ | đang có nợ trả góp hàng tháng |
| chi phí sống | ngoại thành, tỉnh lẻ, ven đô | thành phố lớn, quận nội thành, đông dân cư |
| việc làm | việc khó bị thay thế, hoặc dễ tìm việc mới | thu nhập không ổn định: bán hàng, freelance, dự án |
| người phụ thuộc | không có/không còn người phụ thuộc | có con nhỏ hoặc người phụ thuộc, nhà một nguồn thu |
| mạng lưới | có quan hệ sẵn sàng chu cấp, đang sống cùng bố mẹ | không có bạn bè dư dả, bố mẹ không chu cấp được |
| tài sản phải bảo trì | chỉ thuê ô tô hoặc ô tô còn mới | sở hữu nhà riêng, đặc biệt nhà đã cũ |

Bậc 12 tháng thì thêm **bốn tiêu chí riêng**, không có cặp đối ứng: thu nhập cao (mức sống đã lên
theo, khó thắt lại — lập luận này của sách rất tốt), công việc phải di chuyển và đổi chỗ ở nhiều,
chu cấp cho nhiều người phụ thuộc, và đã hoặc sắp nghỉ hưu.

### Chỗ sách thiếu: không có quy tắc gộp

Người thật khớp tiêu chí ở **cả ba bậc cùng lúc**. Sách không nói phải làm gì khi đó.

Đọc theo chữ, chỉ cần khớp **một** tiêu chí bậc 6 là rơi vào bậc 6. Nghĩa là muốn ở bậc 3 tháng
phải thoả **cả 11 điều kiện** cùng lúc: bảy trục đều ở đầu thấp và không dính tiêu chí 12 tháng
nào. **Chỉ cần đang trả góp một cái điện thoại là văng khỏi bậc 3** — mà trả góp thì rất phổ biến.
Bậc thấp nhất sách đưa ra gần như không với tới được.

Chạy thử hồ sơ người ở [bài 3](bai_03_ghi_chep_chi_tieu.md), dựng từ chính các bài trước:

| Trục | Ở đầu nào | Căn cứ |
| --- | --- | --- |
| sức khoẻ | thấp | không có dữ liệu, giả định khoẻ |
| **nợ** | **CAO** | 13tr vay ở tháng Tết — [bài 8](bai_08_vay_va_tra_no.md) |
| **chi phí sống** | **CAO** | chi thiết yếu 10,37tr/tháng — mức thành phố |
| việc làm | thấp | lương tháng cố định 16tr — bài 3 |
| người phụ thuộc | thấp | bài 6 tính thuế với 0 người phụ thuộc |
| mạng lưới | **không biết** | không bài nào xác lập |
| tài sản phải bảo trì | thấp | đang thuê, chưa mua nhà — bài 2 |

**2/7 trục ở đầu cao.** Hai cách đọc cho hai câu trả lời:

| Cách xác định | Số tháng | Thành tiền |
| --- | ---: | ---: |
| đọc theo chữ của sách (có nợ → bậc 6) | 6,0 | **62,20tr** |
| nội suy 2/7 trục ở đầu cao | 3,9 | **39,99tr** |
| bậc thấp nhất sách cho | 3,0 | 31,10tr |
| bậc cao nhất sách cho | 12,0 | 124,40tr |

Hai cách đọc lệch nhau **hơn 22 triệu** — và sách không nói dùng cách nào.

**[bổ sung] Quy tắc gộp đề nghị:** đếm số trục ở đầu cao trên bảy, rồi nội suy tuyến tính giữa 3 và
6 tháng: `số tháng = 3 + 3 × (số trục cao / 7)`. Dính bất kỳ tiêu chí riêng nào của bậc 12 tháng
thì nhảy thẳng lên 12. Cách này giữ nguyên toàn bộ tiêu chí của sách, chỉ thay quy tắc "khớp một là
xong" bằng một thang liên tục — và nó khiến bậc 3 tháng trở lại thành một khả năng thật.

*(Sàn chi thiết yếu 10,37tr/tháng lấy từ [bài 7 mục 7](bai_07_phan_bo_thu_nhap.md#7-bổ-sung-sàn-chi-thiết-yếu--mỗi-công-thức-có-một-ngưỡng-thu-nhập):
nhóm "thiết yếu" cộng nhóm "bất thường" của 12 tháng ở bài 3.)*

---

## 7. [bổ sung] Bạn đã mua bảo hiểm thất nghiệp rồi — 1% ở bài 6

Sách bảo để dành 3–12 tháng chi tiêu để phòng *"thất nghiệp"*, và không một lần nhắc rằng người đi
làm ở Việt Nam **đã đóng bảo hiểm thất nghiệp bắt buộc**. Đó chính là dòng **1%** trong khối khấu
trừ 10,5% mà [bài 6](bai_06_thue_thu_nhap_ca_nhan.md#3-bảo-hiểm-bắt-buộc-và-cái-bẫy-hai-trần) đã
tính.

Quy định hiện hành (**Luật Việc làm 2025**, hiệu lực 01/01/2026):

- **Điều 39 khoản 1** — trợ cấp hằng tháng bằng **60%** mức bình quân tiền lương tháng đóng BHTN của
  **6 tháng gần nhất**, tối đa không quá **5 lần lương tối thiểu vùng** (vùng I: 5 × 5,31tr =
  **26,55tr/tháng**).
- **Điều 39 khoản 2** — đóng đủ 12 đến đủ 36 tháng: hưởng **3 tháng**; sau đó cứ đóng đủ thêm 12
  tháng thì thêm 1 tháng; **tối đa 12 tháng**.

Áp vào người ở bài 3 — lương gộp 18,10tr (ứng với về tay 16tr theo bài 6):

**Trợ cấp = 60% × 18,10tr = 10,86tr/tháng**, trong khi sàn chi thiết yếu là **10,37tr/tháng**.

> **Trợ cấp thất nghiệp phủ được 105% phần chi thiết yếu.**

| Đã đóng BHTN | Được hưởng | Tổng tiền nhận | Che được mấy tháng chi |
| ---: | ---: | ---: | ---: |
| 11 tháng | 0 tháng | 0,00tr | 0,0 |
| 12 tháng | 3 tháng | 32,58tr | 3,1 |
| 36 tháng | 3 tháng | 32,58tr | 3,1 |
| 60 tháng | 5 tháng | 54,30tr | 5,2 |
| 144 tháng | 12 tháng | 130,32tr | 12,6 |

Người đi làm đủ ba năm **đã có sẵn ba tháng chi tiêu được bảo hiểm**, và đã trả tiền cho nó.

### Nhưng có bốn lỗ hổng — và đó mới là việc của quỹ khẩn cấp

1. **Chỉ che thất nghiệp.** Ốm đau, hỏng máy giặt, tai nạn, việc gia đình — không.
2. **Phải đóng đủ 12 tháng trong 24 tháng** trước khi nghỉ (Điều 38). Người mới đi làm chưa có.
3. **Nghỉ việc do đơn phương chấm dứt hợp đồng trái luật thì mất quyền** (Điều 38). Tự ý bỏ việc
   không đúng thủ tục là mất trắng khoản này.
4. **Tiền về từ ngày làm việc thứ 11** sau khi nộp đủ hồ sơ (Điều 39 khoản 3), không phải ngay —
   nên vẫn cần tiền mặt cho những tuần đầu.

Nên cách dùng đúng không phải "bỏ qua quỹ khẩn cấp", mà là **trừ đi phần đã được che**:

| Mục tiêu | Trừ 3 tháng BHTN | Quỹ thật sự cần |
| ---: | ---: | ---: |
| 6,0 tháng | −3 | **3,0 tháng = 31,10tr** |
| 3,9 tháng (nội suy) | −3 | 0,9 tháng = 8,89tr |

Mục sau cho thấy phép trừ này rút ngắn thời gian xây quỹ đi **một nửa**.

---

## 8. [đính chính] "Gửi kỳ hạn 6 tháng" đá với chính trang 45

tr. 45 khuyên để quỹ ở ngân hàng và nói hai câu, cách nhau vài dòng:

> *"Bạn có thể chọn kỳ hạn 6 tháng và tự động cho số tiền lãi nhập gốc."*
>
> *"vì đây là khoản dự phòng nên tiêu chí tiện lợi, nhanh chóng sẽ được ưu tiên hơn lãi suất"*

Câu thứ hai đúng. Câu thứ nhất mâu thuẫn với nó: **khẩn cấp thì không đợi tới ngày đáo hạn**, mà
rút trước hạn thì toàn bộ kỳ bị tính lại theo lãi **không kỳ hạn**.

Quỹ 62,20tr, giả định lãi kỳ hạn 6 tháng 5,0%/năm và lãi không kỳ hạn 0,5%/năm:

| Rút vào tháng | Lãi đáng lẽ được | Lãi thật nhận | Mất |
| ---: | ---: | ---: | ---: |
| 1 | 0,26tr | 0,03tr | 0,23tr |
| 3 | 0,78tr | 0,08tr | 0,70tr |
| **5** | 1,30tr | 0,13tr | **1,17tr** |
| 6 | 1,55tr | 1,55tr | 0,00tr |

Xấu nhất — cần tiền ở tháng thứ 5 — mất **1,17tr** tiền lãi. Không phải thảm hoạ, nhưng vô ích:
đó là tiền trả cho một ràng buộc mà quỹ khẩn cấp không được phép có.

### [bổ sung] Cách sửa: chia bậc thang

```
  1 tháng chi tiêu (10,37tr)  ->  tài khoản thanh toán, rút tức thì
  5 tháng còn lại (51,83tr)   ->  chia thành 5 sổ kỳ hạn 6 tháng,
                                  mở lệch nhau mỗi tháng một sổ
```

Mỗi tháng có đúng một sổ đáo hạn, nên **luôn có tiền tới hạn trong vòng 30 ngày** mà vẫn ăn lãi kỳ
hạn ở phần lớn số tiền. Cần gấp hơn 30 ngày thì đã có một tháng tiền mặt ở lớp ngoài. Sách không
nhắc cách này, dù nó giải quyết đúng mâu thuẫn mà chính sách vừa tạo ra.

---

## 9. [bổ sung] Xây quỹ mất bao lâu, và giá của việc không có nó

Sách nói **bao nhiêu là đủ** nhưng không một lần nói **mất bao lâu để có**. Đó là con số quyết định
xem lời khuyên có dùng được không.

Dùng tỷ lệ giữ lại **thực tế** mà [bài 7 mục 8](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật)
đo được — 15,5% trên thu nhập ròng 16tr, tức **2,48tr/tháng**:

| Mục tiêu quỹ | Thành tiền | Số tháng để dành | Tức là |
| --- | ---: | ---: | ---: |
| 3 tháng | 31,10tr | 12,5 tháng | 1,0 năm |
| **6 tháng** | 62,20tr | **25,1 tháng** | **2,1 năm** |
| **6 tháng trừ BHTN** (3 tháng) | 31,10tr | **12,5 tháng** | **1,0 năm** |
| 12 tháng | 124,40tr | 50,2 tháng | 4,2 năm |

**Quỹ 6 tháng mất hơn hai năm để xây** — và trong suốt hai năm ấy toàn bộ phần để dành đi vào quỹ,
tức lọ FFA và LTSS của bài 7 **đứng yên**. Đó là cái giá thật của một dòng khuyên ở tr. 43, và sách
không nêu.

Còn nếu trừ đi ba tháng mà bảo hiểm thất nghiệp đã che (mục 7), chỉ còn **12,5 tháng**. **Biết mình
đã có sẵn cái gì rút ngắn được một nửa quãng đường** — và đó là toàn bộ lý do mục 7 tồn tại.

### Giá của việc không có quỹ

[Bài 7](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật) đã cho thấy tháng Tết
người này thiếu **13 triệu** và phải vay. Với một quỹ khẩn cấp, tháng đó không có khoản vay nào.

Nên "lợi suất" của quỹ khẩn cấp không phải lãi ngân hàng 5%. Nó là **lãi suất của khoản vay mà quỹ
giúp bạn không phải vay** — đúng nguyên tắc ở
[bài 8 mục 9](bai_08_vay_va_tra_no.md#9-bổ-sung-khoản-13-triệu-của-bài-7-trả-nợ-hay-bỏ-vào-ffa).
Vay nóng 20%/năm thì quỹ khẩn cấp vừa "sinh lời" 20% ở đúng khoảnh khắc bạn cần nó.

Đó là câu trả lời cho phản đối hiển nhiên nhất ở [mục 5](#5-bổ-sung-lạm-phát-nối-thẳng-với-bài-8-lãi-suất-thật):
đúng, để tiền trong ngân hàng gần như không sinh lời thực. Nhưng nó không ở đó để sinh lời. Nó ở đó
để bạn không phải vay 20%.

---

## 10. Bảo hiểm: phép ẩn dụ áo mưa và ba lợi ích

C2 tr. 45–47. Sách mở bằng hình ảnh hay nhất của cả hai tập: bộ áo mưa trong cốp xe. Không mang vì
biết chắc trời mưa, mang vì *"nhỡ lúc nào đó"*. Rồi câu định nghĩa gọn:

> *"Bảo hiểm là thứ bạn mua và bạn ước rằng không bao giờ mình phải dùng đến."*

Về bảo hiểm nhân thọ, sách nêu bốn ý ở tr. 47, và ba trong bốn ý đều đúng:

1. **Nguyên tắc chia sẻ rủi ro** — mỗi người bù đắp hỗ trợ lẫn nhau khi rủi ro xảy ra. Đúng, và đó
   là bản chất.
2. **Đừng so lãi suất với gửi tiết kiệm hay đầu tư** vì *"bản chất của chúng vốn đã không hề giống
   nhau"*. Đúng — với bảo hiểm thuần bảo vệ. Mục 11 nói vì sao câu này **không** đúng với sản phẩm
   gói kèm tích luỹ.
3. **Việc "lãi" hay không phụ thuộc rủi ro có xảy ra hay không**, và *"Nếu bạn gặp rủi ro sớm, bạn
   rất "lãi" về tiền (nhưng tin tôi đi, bạn không thích kịch bản đó đâu)"*. Câu này rất chính xác
   và rất đáng nhớ.
4. **Ba lợi ích của BHNT**: (1) bảo vệ trước rủi ro, (2) giá trị nhận lại khi đáo hạn, (3) đóng phí
   định kỳ tạo thói quen giữ lại đều đặn một số tiền và đầu tư nó.

Sách cũng thẳng thắn: *"Tôi không thuyết phục bạn mua bảo hiểm, việc đó hãy để những người bán bảo
hiểm làm."* Và nhắc "ba chân kiềng" Tiết kiệm – Bảo hiểm – Đầu tư.

Hai chỗ cần nói lại, ở hai mục sau.

---

## 11. [bổ sung] Nguyên tắc sách thiếu: chỉ bảo hiểm cái không tự gánh nổi

tr. 46 viết: *"Tôi mua các loại bảo hiểm. Tôi không tìm ra lý do tại sao để không mua chúng."*

Có một lý do, và nó nằm ngay trong phép ẩn dụ áo mưa của chính sách. Bạn mang áo mưa vì ướt thì
phiền và áo mưa thì rẻ. Bạn **không** chở theo một cái ô tô dự phòng trong cốp. **Quy mô tổn thất
quyết định.**

Vì sao phải có nguyên tắc này: **phí bảo hiểm luôn cao hơn tổn thất kỳ vọng.** Công ty bảo hiểm
phải trả lương, trả hoa hồng, và có lãi — nếu không thì nó không tồn tại được tới lúc trả tiền cho
bạn. Nên xét trên trung bình, **mua bảo hiểm là cố tình chịu lỗ**. Bạn không mua nó để có lời. Bạn
mua nó để đổi một cú không gượng dậy được lấy một khoản lỗ nhỏ đều đặn.

Từ đó ra quy tắc, áp cho người ở bài 3 (thu nhập ròng 16tr, để dành 2,48tr/tháng, quỹ khẩn cấp mục
tiêu 62,20tr):

| Tổn thất | Tình huống | Gánh bằng gì | Vì sao |
| ---: | --- | --- | --- |
| 2,00tr | hỏng điện thoại | **tự gánh** (dòng tiền) | nhỏ hơn hai tháng để dành |
| 15,00tr | sửa xe lớn, mất việc 1 tháng | **quỹ khẩn cấp** | quỹ hấp thụ được |
| 60,00tr | thất nghiệp 6 tháng | **quỹ khẩn cấp** | quỹ hấp thụ được |
| 300,00tr | phẫu thuật lớn | **BẢO HIỂM** | vượt quỹ; tự gánh mất 10 năm để dành |
| 2.000,00tr | mất khả năng lao động | **BẢO HIỂM** | vượt quỹ; tự gánh mất 67 năm để dành |

**Đừng bảo hiểm cái bạn tự gánh nổi.** Bảo hiểm cái **hiếm và lớn** — bệnh hiểm nghèo, mất khả năng
lao động, trách nhiệm dân sự khi gây tai nạn. Tự gánh cái **thường và nhỏ**.

Đây cũng là chỗ khung ở [mục 1](#1-ba-lớp-bảo-vệ--khung-mà-sách-không-dựng) khép lại: quỹ khẩn cấp
và bảo hiểm không phải hai chủ đề rời nhau. Chúng là **một bài toán ở hai quy mô tổn thất**, và
đường ranh giữa chúng chính là quy mô quỹ khẩn cấp của bạn. Quỹ lớn lên thì đường ranh dịch sang
phải, và bạn cần ít bảo hiểm hơn — một hệ quả thực tế mà không mục nào của sách nói.

### Còn quy tắc "10 năm thu nhập" thì đứng vững

tr. 47: *"giá trị hợp đồng bảo hiểm của bạn nên bằng 10 năm thu nhập"* — thu nhập 10tr/tháng =
120tr/năm thì nên có gói **1,2 tỷ**. Kiểm được:

`1.200tr ÷ 124,40tr (chi thiết yếu một năm) = **9,6 năm sống**`

Đó là con số có nghĩa. Nó mua cho gia đình chừng ấy năm để sắp xếp lại cuộc sống, chứ không phải
mua sự giàu có. Sách đưa quy tắc đúng mà không nói vì sao — nói ra thì nó dễ nhớ và dễ điều chỉnh
hơn nhiều: **con số cần bằng số năm gia đình bạn cần để đứng lại được, nhân với chi phí sống một
năm.**

---

## 12. [đính chính] Ba con số ở trang 47 không khớp nhau

tr. 47 đưa ba con số trong cùng một đoạn:

> *"Nếu bạn đang chu cấp cho gia đình và thu nhập tháng của bạn khoảng 10 triệu trở lên, hãy cân
> nhắc tìm hiểu về Bảo hiểm nhân thọ. Mức đóng định kỳ 1 triệu đồng/tháng không quá khó."*

Đặt cạnh chính kết quả của [bài 7](bai_07_phan_bo_thu_nhap.md#6-bổ-sung-đặt-ba-công-thức-cạnh-nhau-một-đáp-số-duy-nhất) —
cả ba công thức phân bổ của sách đều cho tỷ lệ giữ lại đúng **20%**:

| Chỉ số | Giá trị |
| --- | ---: |
| phí bảo hiểm / thu nhập | 10% |
| tỷ lệ giữ lại của cả ba công thức (bài 7) | 20% |
| tiền để dành được mỗi tháng | 2,00tr |
| **phí bảo hiểm chiếm bao nhiêu phần số đó** | **50%** |

**Phí một triệu ăn đúng một nửa toàn bộ khả năng tích luỹ của người ấy.** Sách gọi mức đó là *"không
quá khó"* mà không đặt nó cạnh bất cứ con số nào khác của chính mình.

Nửa còn lại — 1tr/tháng — phải gánh cả lọ FFA, cả lọ LTSS, **và** quỹ khẩn cấp ở mục 9. Riêng quỹ
khẩn cấp 6 tháng của người này (33,00tr) sẽ mất **33 tháng, tức 2,8 năm**, và trong suốt thời gian
đó chưa đầu tư được đồng nào.

### Vì sao chuyện này quan trọng: ba lợi ích là ba sản phẩm bị gói làm một

Đây không phải lý do để không mua bảo hiểm. Đây là lý do để mua **đúng thứ**.

Ba lợi ích mà tr. 47 liệt kê là ba thứ khác nhau:

| Lợi ích sách nêu | Thật ra là gì | Tự làm được không |
| --- | --- | --- |
| (1) bảo vệ trước rủi ro | **bảo hiểm** đúng nghĩa | **không** — chỉ mua được |
| (2) giá trị nhận lại khi đáo hạn | một khoản **đầu tư** | được — đó là lọ FFA |
| (3) đóng phí đều tạo thói quen giữ lại | một khoản **tiết kiệm ép buộc** | được — đó là lọ LTSS |

Chỉ (1) là thứ bạn không tự làm được. (2) và (3) chính là hai chiếc lọ bạn đã có ở bài 7 — và
**chúng là phần khiến (1) trở nên đắt**, vì tiền đóng vào phải nuôi cả phần tích luỹ lẫn chi phí
bán hàng của sản phẩm gói.

Đó cũng là chỗ ý số 2 của tr. 47 cần nói lại. *"Bạn không nên so sánh lãi suất với việc gửi tiết
kiệm hoặc đầu tư"* là lời khuyên **đúng với bảo hiểm thuần bảo vệ** — so sánh một thứ không có
thành phần tích luỹ với tiết kiệm là so nhầm. Nhưng với sản phẩm **có giá trị đáo hạn**, tức là có
thành phần tích luỹ thật, thì bạn **phải** so — vì phần đó cạnh tranh trực tiếp với lọ FFA của
chính bạn, và bạn có quyền biết nó sinh lời bao nhiêu.

Cách tách rất đơn giản, và là câu hỏi cần hỏi người tư vấn: **cùng số tiền bảo vệ ấy, nếu mua sản
phẩm thuần bảo vệ (bảo hiểm tử kỳ) thì phí bao nhiêu?** Chênh lệch giữa hai con số chính là số tiền
bạn đang đưa cho phần tích luỹ. Rồi so phần đó với lọ FFA. Sách không dạy phép trừ này, và đó là
phép trừ quan trọng nhất trong cả chủ đề.

---

## 13. [2026] Điều sách không thể biết: cuộc khủng hoảng bancassurance

Sách được viết trước một biến động lớn của thị trường bảo hiểm nhân thọ Việt Nam. Với người đọc năm
2026, đây là bối cảnh không thể bỏ qua.

**Con số nói nhiều nhất:** thanh tra của Bộ Tài chính năm 2023 với **4 doanh nghiệp bảo hiểm** phân
phối qua ngân hàng cho thấy **32,4% – 73% hợp đồng bị huỷ ngay sau năm đầu tiên**.

Huỷ trong năm đầu gần như luôn đồng nghĩa **mất phần lớn hoặc toàn bộ số phí đã đóng**. Con số ấy
không mô tả một sản phẩm bị mua nhầm ở vài trường hợp cá biệt — nó mô tả một kênh bán mà phần lớn
người mua không hiểu mình mua gì.

**Phản ứng của cơ quan quản lý — Thông tư 67/2023/TT-BTC** (Bộ Tài chính ban hành 02/11/2023, hướng
dẫn Luật Kinh doanh bảo hiểm 2022 và Nghị định 46/2023/NĐ-CP; 7 chương, 62 điều, thay thế Thông tư
50/2017/TT-BTC). Bốn quy định người mua cần biết:

1. **Quy tắc 60 ngày** (khoản 3 Điều 53) — ngân hàng **không được** tư vấn, giới thiệu, chào bán,
   thu xếp ký hợp đồng **bảo hiểm liên kết đầu tư** trong thời hạn **trước và sau 60 ngày** kể từ
   ngày giải ngân toàn bộ khoản vay. **Luật Các tổ chức tín dụng 2024** (hiệu lực 01/7/2024) cấm
   hẳn việc gắn bán bảo hiểm với cấp tín dụng.
2. **Thời gian cân nhắc 21 ngày** (Điều 9) — với sản phẩm nhân thọ dài hạn có giá trị hoàn lại,
   người mua được **huỷ hợp đồng và hoàn phí** trong 21 ngày kể từ khi xác nhận đã nhận đủ tài
   liệu, sau khi trừ chi phí khám sức khoẻ thực tế.
3. **Bắt buộc ghi âm quá trình tư vấn** với sản phẩm bảo hiểm liên kết đầu tư; bản ghi được lưu tối
   thiểu **5 năm**.
4. **Tách bạch tín dụng và bảo hiểm** — ngân hàng phải nói rõ sản phẩm bảo hiểm **không phải sản
   phẩm của ngân hàng**, và tham gia bảo hiểm **không phải điều kiện bắt buộc** để dùng dịch vụ
   khác.

Ba điều rút ra cho người học:

- **Quy tắc 60 ngày chỉ áp cho bảo hiểm liên kết đầu tư.** Bảo hiểm khoản vay, cháy nổ, tử kỳ, hỗn
  hợp không nằm trong phạm vi cấm đó. Biết ranh giới để nhận ra khi nào mình vẫn có thể bị chào bán.
- **21 ngày là quyền của bạn, không phải ân huệ.** Ký rồi vẫn rút được. Nhưng đồng hồ chạy từ lúc
  bạn **xác nhận đã nhận tài liệu** — nên hãy đọc trước khi ký xác nhận đó.
- **Đây chính là lý do phép trừ ở mục 12 quan trọng.** Phần lớn hợp đồng bị huỷ sớm là hợp đồng gói
  kèm tích luỹ, mua vì tưởng là một khoản gửi tiết kiệm lãi cao. Hỏi đúng một câu — *thuần bảo vệ
  thì phí bao nhiêu* — là đã tách được hai thứ ra.

Câu của sách ở tr. 46–47 — *"Tôi không thuyết phục bạn mua bảo hiểm, việc đó hãy để những người bán
bảo hiểm làm"* — vẫn đúng, và bối cảnh này chỉ làm nó đúng hơn.

---

## 14. Tự thử

Sửa [`thuc_hanh/bai-09-bao-ve.py`](../thuc_hanh/bai-09-bao-ve.py) rồi chạy lại.

1. **Ranh giới 10% có gì đặc biệt không?** In `nam_giam_nua` cho các mức từ 5% tới 15%, bước 1
   điểm. Có chỗ nào con số nhảy đột ngột khi qua mốc 10% không? Điều đó nói gì về bảng phân loại
   tr. 39–40?

2. **Hồ sơ của chính bạn.** Sửa `HO_SO`, đặt bảy trục theo đúng hoàn cảnh của bạn. Đọc theo chữ của
   sách bạn ở bậc nào? Nội suy thì bao nhiêu tháng? Hai con số cách nhau bao nhiêu tiền?

3. **Trục "mạng lưới" đáng giá bao nhiêu?** Trong `HO_SO` nó đang là `None`. Đặt lần lượt `True` và
   `False` rồi chạy lại — con số nội suy đổi bao nhiêu tháng, bao nhiêu tiền? Một câu hỏi bạn chưa
   trả lời được đáng giá chừng ấy.

4. **BHTN che được bao nhiêu ở mức lương khác.** Đổi `LUONG_GOP` thành 12tr, 30tr, 60tr. Ở mức nào
   thì trợ cấp **không** còn phủ nổi sàn chi thiết yếu? Ở mức nào thì trần 26,55tr bắt đầu cắn?
   (Gợi ý: nhớ rằng người lương cao thì sàn chi thiết yếu của họ cũng cao.)

5. **Bậc thang có đáng không?** Viết thêm hàm tính tổng lãi cả năm của hai cách: (a) toàn bộ quỹ
   trong một sổ 6 tháng, (b) 1 tháng tiền mặt + 5 sổ lệch nhau. Giả sử mỗi năm phải rút một lần vào
   một tháng ngẫu nhiên — nhưng **đừng dùng số ngẫu nhiên**, hãy duyệt cả 12 tháng và lấy trung
   bình. Cách nào hơn, hơn bao nhiêu?

6. **Đường ranh bảo hiểm dịch đi đâu?** Trong bảng ba lớp bảo vệ, tăng quỹ khẩn cấp từ 6 lên 12
   tháng. Tổn thất nào chuyển từ cột "BẢO HIỂM" sang cột "quỹ khẩn cấp"? Điều đó có nghĩa gì với số
   tiền bảo hiểm bạn cần mua?

7. **Phí bảo hiểm bao nhiêu thì vừa?** Sách nói 1tr trên thu nhập 10tr. Tìm mức phí lớn nhất mà vẫn
   để quỹ khẩn cấp 6 tháng xây xong trong vòng 18 tháng. Con số đó so với 1tr thế nào?

---

## 15. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Lạm phát | Inflation | Giá chung tăng liên tục, tức sức mua đồng tiền giảm. Đo trên **cả rổ** hàng hoá, không phải một món |
| Siêu lạm phát | Hyperinflation | Sách đặt ở trên 1000%/năm; nghiên cứu thường dùng mốc 50%/tháng (Cagan, 1956) |
| Lợi suất thực | Real return | `danh nghĩa − lạm phát`. Con số duy nhất nói được sức mua đổi thế nào |
| Quỹ khẩn cấp | Emergency fund | Tiền cho khoản chi **không lường trước**, không kỳ hạn |
| Quỹ chi tiêu | Sinking fund | Tiền cho khoản chi **đã lên kế hoạch**, có kỳ hạn định sẵn |
| Bảo hiểm thất nghiệp | Unemployment insurance | 1% lương do người lao động đóng (bài 6); hưởng 60% lương gộp, tối đa 12 tháng |
| Lãi không kỳ hạn | Demand deposit rate | Lãi áp dụng khi rút trước hạn. Thường thấp hơn lãi kỳ hạn cả chục lần |
| Bậc thang tiền gửi | Deposit laddering | Chia tiền thành nhiều sổ đáo hạn lệch nhau, để luôn có sổ sắp tới hạn |
| Bảo hiểm tử kỳ | Term life insurance | Thuần bảo vệ, không có giá trị đáo hạn |
| Bảo hiểm liên kết đầu tư | Unit-linked / investment-linked | Gói bảo vệ chung với đầu tư. Là loại chịu quy tắc 60 ngày của Thông tư 67/2023 |
| Bancassurance | — | Bán bảo hiểm qua kênh ngân hàng |

---

## 16. Câu hỏi tự kiểm tra

1. Ba lớp bảo vệ chia theo tiêu chí gì? Cái gì quyết định đường ranh giữa lớp 2 và lớp 3?
2. Ba bậc lạm phát của sách và khoảng của từng bậc?
3. Ví dụ bát phở ở tr. 39, đọc đúng chữ, rơi vào bậc nào?
4. Vì sao giá một bát phở tăng 40% chưa nói được gì về lạm phát?
5. Lạm phát 9%/năm làm mất một nửa sức mua sau bao lâu? Viết công thức.
6. Gửi tiết kiệm 5%/năm khi lạm phát 4% thì lợi suất thực là bao nhiêu? Sau 10 năm 100tr thành bao
   nhiêu về sức mua?
7. Phân biệt quỹ khẩn cấp và quỹ chi tiêu. Cùng mua một chiếc iPhone, khi nào lấy từ quỹ nào?
8. Vì sao hai danh sách 3 tháng và 6 tháng của sách không phải hai bậc độc lập?
9. Đọc theo đúng chữ của sách, cần thoả bao nhiêu điều kiện để ở bậc 3 tháng?
10. Người lao động đóng bao nhiêu phần trăm lương cho bảo hiểm thất nghiệp, và được hưởng bao nhiêu
    phần trăm lương khi thất nghiệp?
11. Đóng BHTN 36 tháng thì được hưởng mấy tháng? 60 tháng? 144 tháng?
12. Kể bốn lỗ hổng của bảo hiểm thất nghiệp mà quỹ khẩn cấp phải lấp.
13. Vì sao lời khuyên "gửi kỳ hạn 6 tháng" ở tr. 45 mâu thuẫn với chính tr. 45? Cách sửa là gì?
14. Với tỷ lệ giữ lại thực tế 15,5% trên 16tr, xây quỹ 6 tháng mất bao lâu? Biết trừ phần BHTN thì
    còn bao lâu?
15. "Lợi suất" thật của quỹ khẩn cấp là gì?
16. Vì sao trên trung bình, mua bảo hiểm luôn là chịu lỗ? Vậy mua để làm gì?
17. Nguyên tắc chọn cái gì đáng bảo hiểm? Nêu hai ví dụ đáng và hai ví dụ không đáng.
18. Phí 1tr/tháng trên thu nhập 10tr chiếm bao nhiêu phần khả năng tích luỹ của người đó?
19. Ba lợi ích của BHNT mà tr. 47 nêu thật ra là mấy sản phẩm? Cái nào bạn không tự làm được?
20. Câu hỏi nào tách được phần bảo vệ khỏi phần tích luỹ trong một hợp đồng?
21. Quy tắc 60 ngày của Thông tư 67/2023 áp cho loại bảo hiểm nào, và không áp cho loại nào?
22. Thời gian cân nhắc là bao nhiêu ngày, và đồng hồ bắt đầu chạy từ lúc nào?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 9 — BẢO VỆ                                        C2 tr. 39-47      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BA LỚP, MỘT BÀI TOÁN — chia theo QUY MÔ TỔN THẤT                       ║
║     nhỏ & thường  -> dòng tiền tháng này        (ngân sách, bài 7)      ║
║     vừa & thỉnh thoảng -> tiền để dành sẵn      (quỹ khẩn cấp)          ║
║     lớn & hiếm    -> người khác chịu, trả phí   (bảo hiểm)              ║
║     đường ranh giữa lớp 2 và 3 CHÍNH LÀ quy mô quỹ khẩn cấp của bạn     ║
║                                                                          ║
║  LẠM PHÁT   sức mua giảm, không phải giá tăng                           ║
║     sách: tự nhiên 0-<10% · phi mã 10-<1000% · siêu >1000%              ║
║     [đính chính] bát phở tr. 39 "năm ngoái -> giờ": +40% tới +60%       ║
║        = PHI MÃ theo chính bảng của sách. Đọc là 5 năm mới hợp lý.      ║
║     giá MỘT món không phải lạm phát — lạm phát đo cả rổ                 ║
║     [bổ sung] số năm giảm nửa = ln2 / ln(1+i)                           ║
║        9% (sách gọi "tự nhiên") -> mất nửa sức mua sau 8,0 NĂM          ║
║        9% và 10% gần như giống nhau, mà sách xếp hai bậc khác nhau      ║
║     lợi suất thực = danh nghĩa - lạm phát -> nối thẳng bài 1 và bài 8   ║
║                                                                          ║
║  QUỸ KHẨN CẤP  3 / 6 / 12 tháng chi THIẾT YẾU                           ║
║     khẩn cấp = KHÔNG lường trước · quỹ chi tiêu = ĐÃ lên kế hoạch       ║
║     [đính chính] hai danh sách 3 và 6 tháng KHÔNG độc lập — chúng là    ║
║        BẢY trục, mỗi trục hai đầu; bậc 12 thêm 4 tiêu chí riêng         ║
║        đọc theo chữ: phải thoả CẢ 11 điều kiện mới ở bậc 3 tháng        ║
║        chỉ cần trả góp một cái điện thoại là văng khỏi bậc 3            ║
║     người ở bài 3: 2/7 trục cao -> theo chữ 62,20tr, nội suy 39,99tr    ║
║        hai cách đọc lệch hơn 22 triệu, sách không nói dùng cách nào     ║
║     [bổ sung] quy tắc gộp: 3 + 3 × (số trục cao / 7)                    ║
║                                                                          ║
║  [bổ sung] BẠN ĐÃ CÓ BẢO HIỂM THẤT NGHIỆP — dòng 1% của bài 6           ║
║     60% lương gộp, trần 5 × lương tối thiểu vùng = 26,55tr/tháng        ║
║     12-36 tháng đóng -> 3 tháng hưởng; +12 tháng -> +1; tối đa 12       ║
║     lương gộp 18,1tr -> trợ cấp 10,86tr > sàn chi 10,37tr = che 105%    ║
║     BỐN LỖ HỔNG: chỉ che thất nghiệp · cần 12/24 tháng · mất quyền nếu  ║
║        nghỉ trái luật · tiền về từ ngày làm việc thứ 11                 ║
║                                                                          ║
║  [đính chính] tr. 45 khuyên gửi KỲ HẠN 6 THÁNG, đá với chính tr. 45     ║
║     rút trước hạn -> cả kỳ tính lại theo lãi KHÔNG kỳ hạn, mất 1,17tr   ║
║     [bổ sung] sửa bằng BẬC THANG: 1 tháng tiền mặt + 5 sổ lệch nhau     ║
║                                                                          ║
║  [bổ sung] XÂY QUỸ MẤT BAO LÂU — sách không bao giờ nói                 ║
║     giữ lại thực tế 15,5% -> 2,48tr/tháng                               ║
║     quỹ 6 tháng = 62,20tr -> 25 tháng = 2,1 NĂM, FFA và LTSS đứng yên   ║
║     trừ 3 tháng BHTN đã che -> còn 12,5 tháng. Biết mình có gì -> nửa   ║
║     "lợi suất" của quỹ = lãi khoản vay mà nó giúp bạn KHÔNG phải vay    ║
║                                                                          ║
║  BẢO HIỂM   "thứ bạn mua và ước không bao giờ phải dùng đến" (tr. 46)   ║
║     [bổ sung] phí LUÔN cao hơn tổn thất kỳ vọng — hãng phải có lãi      ║
║        nên mua bảo hiểm là CỐ TÌNH chịu lỗ nhỏ để tránh cú chí mạng     ║
║        -> bảo hiểm cái HIẾM và LỚN, tự gánh cái THƯỜNG và NHỎ           ║
║     [đính chính] tr. 47: phí 1tr trên thu nhập 10tr = 10% thu nhập      ║
║        = MỘT NỬA toàn bộ khả năng tích luỹ (tỷ lệ giữ lại 20%, bài 7)   ║
║        sách gọi là "không quá khó" mà không so với số nào của mình      ║
║     ba lợi ích tr. 47 là BA SẢN PHẨM gói làm một:                       ║
║        (1) bảo vệ — KHÔNG tự làm được   (2) đáo hạn = FFA               ║
║        (3) ép để dành = LTSS            (2)+(3) làm (1) đắt lên         ║
║        câu hỏi tách chúng ra: thuần bảo vệ (tử kỳ) thì phí bao nhiêu?   ║
║     "hợp đồng = 10 năm thu nhập" ĐÚNG: 1,2 tỷ = 9,6 năm chi thiết yếu   ║
║                                                                          ║
║  [2026] BANCASSURANCE — điều sách không thể biết                        ║
║     thanh tra 2023, 4 doanh nghiệp: 32,4-73% hợp đồng HUỶ NGAY NĂM ĐẦU  ║
║     Thông tư 67/2023/TT-BTC: quy tắc 60 ngày (chỉ liên kết đầu tư) ·    ║
║        cân nhắc 21 ngày · ghi âm tư vấn, lưu 5 năm · tách bạch tín dụng ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn.
  Unit 4, Lesson 1–3, **tr. 39–47**. Định nghĩa và ba bậc lạm phát, sáu nguyên nhân, hai phía ảnh
  hưởng, ba bậc quỹ khẩn cấp cùng toàn bộ tiêu chí, phân biệt Emergency Fund với Sinking Fund, phép
  ẩn dụ áo mưa và bốn ý về bảo hiểm nhân thọ — đều chép từ đây.
- **Văn bản pháp luật**, tra ngày **09/09/2026**:
  - **Luật Việc làm 2025** (Quốc hội khoá XV thông qua 16/6/2025, hiệu lực 01/01/2026), **Điều 38**
    (điều kiện hưởng) và **Điều 39** (mức hưởng 60%, trần 5 lần lương tối thiểu vùng, thời gian
    hưởng, thời điểm hưởng từ ngày làm việc thứ 11).
  - **Nghị định 293/2025/NĐ-CP** ngày 10/11/2025 — lương tối thiểu vùng từ 01/01/2026, vùng I
    5.310.000đ, dùng để tính trần trợ cấp 26.550.000đ/tháng.
  - **Thông tư 67/2023/TT-BTC** (Bộ Tài chính, 02/11/2023) hướng dẫn **Luật Kinh doanh bảo hiểm
    2022** và **Nghị định 46/2023/NĐ-CP** — quy tắc 60 ngày (khoản 3 Điều 53), thời gian cân nhắc
    21 ngày (Điều 9), ghi âm tư vấn sản phẩm liên kết đầu tư lưu tối thiểu 5 năm, tách bạch hợp
    đồng tín dụng với hợp đồng bảo hiểm.
  - **Luật Các tổ chức tín dụng 2024** (hiệu lực 01/7/2024) — cấm gắn việc bán bảo hiểm với cấp
    tín dụng.

  Các trang tra cứu đã dùng:
  [Quy định trợ cấp thất nghiệp 2026 — Thư viện Pháp luật](https://thuvienphapluat.vn/phap-luat/quy-dinh-tro-cap-that-nghiep-2026-moi-nhat-ra-sao-muc-huong-tro-cap-that-nghiep-nam-2026-toi-da-la--524767-251110.html) ·
  [Mức hưởng trợ cấp thất nghiệp tối đa từ 2026 — Bảo hiểm xã hội Việt Nam](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-xa-hoi.aspx?ItemID=25707&CateID=168) ·
  [Quy định điều kiện và mức hưởng trợ cấp thất nghiệp — Cổng Xây dựng chính sách, Chính phủ](https://xaydungchinhsach.chinhphu.vn/quy-dinh-dieu-kien-va-muc-huong-tro-cap-that-nghiep-119250807095034717.htm) ·
  [Thông tư 67/2023/TT-BTC hạn chế ép khách mua bảo hiểm kèm khoản vay — Tạp chí Tài chính](https://tapchitaichinh.vn/thong-tu-so-67-2023-tt-btc-han-che-tinh-trang-ep-khach-mua-bao-hiem-kem-khoan-vay.html) ·
  [Bán bảo hiểm qua ngân hàng phải ghi âm quá trình tư vấn — Tạp chí Luật sư Việt Nam](https://lsvn.vn/ban-bao-hiem-qua-ngan-hang-phai-ghi-am-qua-trinh-tu-van-san-pham-1699698327-a137502.html) ·
  [Cấm ngân hàng bán bảo hiểm liên kết đầu tư cho khách vay tiền — VietNamNet](https://vietnamnet.vn/cam-ngan-hang-ban-bao-hiem-lien-ket-dau-tu-cho-khach-vay-tien-2213443.html) ·
  [Triệt tận gốc nạn ép mua bảo hiểm khi vay ngân hàng — Tuổi Trẻ](https://tuoitre.vn/triet-tan-goc-nan-ep-mua-bao-hiem-khi-vay-ngan-hang-20231112075531331.htm)
- **Định nghĩa siêu lạm phát 50%/tháng**: Phillip Cagan, *The Monetary Dynamics of Hyperinflation*
  (1956). Bài này **không đọc bản gốc** — nêu ra chỉ để cho thấy ngưỡng 1000% của sách là một quy
  ước trong nhiều quy ước.
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-09-bao-ve.py`](../thuc_hanh/bai-09-bao-ve.py). Mọi
  bảng số trong bài do tệp này tính, chạy hai lần ra giống hệt nhau. Tệp mã hoá **chính bảng phân
  loại lạm phát của sách** thành hàm rồi đưa ví dụ bát phở của sách vào, và tự kiểm cả năm bậc thời
  gian hưởng trợ cấp thất nghiệp.
- **Con số giả định, không phải của sách:** lạm phát 4%/năm (theo giả định C1 tr. 31 đã dùng từ bài
  1); lãi kỳ hạn 6 tháng 5%/năm và lãi không kỳ hạn 0,5%/năm ở mục 8; các mức tổn thất ở bảng ba
  lớp bảo vệ ở mục 11.
- **Số liệu lấy nguyên từ bài trước:** sàn chi thiết yếu 10.366.667đ/tháng và tỷ lệ giữ lại thực tế
  15,5% (bài 7, tính từ bảng 12 tháng của bài 3); lương gộp 18,1tr ứng với về tay 16tr (bài 6);
  khoản vay 13tr (bài 7, bài 8).
- **Liên hệ chéo:**
  - Dòng 1% bảo hiểm thất nghiệp và hai trần đóng:
    [bài 6 mục 3](bai_06_thue_thu_nhap_ca_nhan.md#3-bảo-hiểm-bắt-buộc-và-cái-bẫy-hai-trần).
  - Sàn chi thiết yếu và cách đo nó:
    [bài 7 mục 7](bai_07_phan_bo_thu_nhap.md#7-bổ-sung-sàn-chi-thiết-yếu--mỗi-công-thức-có-một-ngưỡng-thu-nhập).
  - Khoản vay 13 triệu mà quỹ khẩn cấp lẽ ra đã chặn:
    [bài 7 mục 8](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật).
  - Nguyên tắc "trả nợ là khoản đầu tư có lợi suất chắc chắn":
    [bài 8 mục 9](bai_08_vay_va_tra_no.md#9-bổ-sung-khoản-13-triệu-của-bài-7-trả-nợ-hay-bỏ-vào-ffa).
  - Lợi suất thực 8% dùng suốt khoá:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Ponzi, phần còn lại của Unit 4 từ tr. 47: **bài 11**.

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
| **9** | **Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm** ← *bạn đang ở đây* | C2 tr. 39–47 | 1 |
| 10 | **[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai | ngoài sách | 2 |
| 11 | Nhận diện lừa đảo: Ponzi và CFD | C2 tr. 47–57 | 1 |
| 12 | Rủi ro, khẩu vị rủi ro, phân bổ tài sản | C1 tr. 25–33 | 1 |
| 13 | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
