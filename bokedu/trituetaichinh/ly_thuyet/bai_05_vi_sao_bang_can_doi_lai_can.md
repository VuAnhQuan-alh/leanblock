# Bài 5 — Vì sao bảng cân đối lại cân

> Bài học dựng từ **Phần III — Bảng cân đối kế toán, nơi vén mở nhiều điều nhất**: chương 12 *Tại sao
> bảng cân đối kế toán lại cân đối?* (PDF tr. 97–99), chương 13 *Báo cáo kết quả kinh doanh ảnh hưởng
> đến bảng cân đối kế toán* (PDF tr. 100–107).
> 🎯 **Vòng 1.** Bài 4 đã đi hết hai cột của bảng cân đối. Bài này trả lời câu hỏi bài 4 hứa, rồi **nối
> nó với báo cáo kết quả kinh doanh** — và đóng lại Phần III.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 4](bai_04_bang_can_doi_ke_toan.md) — toàn bộ bài này dựng trên phương
> trình và các dòng đã dựng ở đó.
> ⚙️ **Code:** [`thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py`](../thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py)
> — file này **dựng một sổ kép thật**: mọi bút toán đi qua hàm `ghi()`, và hàm đó `assert` lại phương
> trình sau **từng bút toán**. Bảng cân đối không lệch được, không phải vì bài học hứa, mà vì code
> không cho phép.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Ba lý do — và vì sao lý do thứ ba là lý do thật](#1-ba-lý-do--và-vì-sao-lý-do-thứ-ba-là-lý-do-thật)
- [2. Chỉ ba việc chạm được vào vốn chủ sở hữu](#2-chỉ-ba-việc-chạm-được-vào-vốn-chủ-sở-hữu)
- [3. Doanh nghiệp tí hon: nơi hai báo cáo gặp nhau](#3-doanh-nghiệp-tí-hon-nơi-hai-báo-cáo-gặp-nhau)
- [4. Tiền và vốn chủ đi ngược chiều đến bao giờ](#4-tiền-và-vốn-chủ-đi-ngược-chiều-đến-bao-giờ)
- [5. Lỗ liên tiếp — bao lâu thì vốn chủ sở hữu âm](#5-lỗ-liên-tiếp--bao-lâu-thì-vốn-chủ-sở-hữu-âm)
- [6. Ba tình huống nhà quản lý — đặt số vào cả ba](#6-ba-tình-huống-nhà-quản-lý--đặt-số-vào-cả-ba)
- [7. Ba câu hỏi đánh giá sức khoẻ — và câu hỏi thứ tư sắc hơn cả ba](#7-ba-câu-hỏi-đánh-giá-sức-khoẻ--và-câu-hỏi-thứ-tư-sắc-hơn-cả-ba)
- [8. 📚 Hộp công cụ — "nhân viên là tài sản giá trị nhất của chúng ta"](#8--hộp-công-cụ--nhân-viên-là-tài-sản-giá-trị-nhất-của-chúng-ta)
- [9. WorldCom — vốn hoá chi phí, nhìn từ bảng cân đối](#9-worldcom--vốn-hoá-chi-phí-nhìn-từ-bảng-cân-đối)
- [10. 🇻🇳 Đối chiếu Việt Nam](#10--đối-chiếu-việt-nam)
- [11. Tự thử](#11-tự-thử)
- [12. Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
- [13. Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Ba lý do — và vì sao lý do thứ ba là lý do thật

Chương 12 mở bằng cách gạt bỏ câu trả lời mà ai cũng thuộc:

> *"Nếu ở trường bạn đã được học về phương trình kế toán cơ bản, có lẽ giáo viên của bạn đã nói điều gì
> đó đại loại như: 'Nó được gọi là bảng cân đối kế toán **bởi vì nó cân đối**.' Nhưng ngay cả khi bạn
> viết đáp án đó vào bài thi với một ý thức cực cao, **chưa chắc bạn đã hiểu hết lý do**."*
> — ch. 12 · PDF tr. 97

Rồi đưa **ba cách** hiểu:

**① Vì định nghĩa.** *"Vốn chủ sở hữu được xác định là hiệu số tài sản trừ đi nợ phải trả"* — và sách
nói thẳng lý do: *"bởi đó là cách mà chúng ta **định nghĩa các hạn từ**."* Đúng nhưng rỗng: nó cân vì
bị bắt phải cân.

**② Vì hai bên là hai câu hỏi khác nhau về cùng một thứ.** Một bên là *những gì doanh nghiệp sở hữu*;
bên kia là *"**cách thức** mà doanh nghiệp thu được những gì đang sở hữu"*.

> *"Vì bạn **không thể có thứ này mà không mất đi thứ kia**, nên phần 'có' và phần 'cách chúng ta có'
> sẽ luôn cân đối. **Chúng buộc phải như thế.**"* — ch. 12 · PDF tr. 97

**③ Vì đi theo thời gian thì thấy.** Đây là lý do dùng được, vì nó kiểm được. Sách dẫn ba giao dịch đầu
đời của một doanh nghiệp mới:

| giao dịch | tiền | PPE | vay | vốn chủ | cân? |
| --- | ---: | ---: | ---: | ---: | :---: |
| chủ sở hữu góp 50.000 tiền mặt | 50.000 | 0 | 0 | **50.000** | ✓ |
| mua xe tải 36.000 bằng tiền | 14.000 | 36.000 | 0 | **50.000** | ✓ |
| vay ngân hàng 10.000 | 24.000 | 36.000 | 10.000 | **50.000** | ✓ |

⭐ **Cột vốn chủ không nhúc một li** qua cả ba giao dịch, trong khi tổng tài sản chạy từ 50.000 lên
60.000 và cơ cấu đổi hoàn toàn. Đó là gợi ý cho mục 2.

Hai giao dịch nữa sách nêu, cùng đi qua sổ kép:

| giao dịch | tổng tài sản | tổng nợ | vốn chủ |
| --- | ---: | ---: | ---: |
| *(đầu kỳ)* | 200.000 | 100.000 | 100.000 |
| dùng 100.000 tiền trả hết nợ vay | 100.000 | 0 | 100.000 |
| mua thiết bị 100.000, trả trước 50.000 | 150.000 | 50.000 | 100.000 |

> *"Bạn chỉ cần nhớ rõ một thực tế căn bản rằng **các giao dịch ảnh hưởng đến cả hai phần** của bảng
> cân đối, thế là đủ. Đó là lý do bảng cân đối kế toán luôn cân đối… **nếu tài sản không cân bằng với
> nợ phải trả và vốn chủ sở hữu, ta sẽ không thể có bảng cân đối kế toán.**"* — ch. 12 · PDF tr. 99

⭐ Câu cuối là câu đắt nhất chương: cân đối **không phải một tính chất cần chứng minh**, nó là **điều
kiện để vật ấy tồn tại**. Một bảng lệch không phải "bảng cân đối bị sai" — nó không phải bảng cân đối.

---

## 2. Chỉ ba việc chạm được vào vốn chủ sở hữu

Câu kỹ thuật nhất của chương 12 nằm lọt giữa hai ví dụ và rất dễ đọc lướt qua:

> *"Vốn chủ sở hữu **chỉ** bị ảnh hưởng khi doanh nghiệp ① **lấy vốn đầu tư từ chủ sở hữu**, ② **chi
> tiền mặt cho chủ sở hữu**, hay ③ **ghi nhận một khoản lãi hoặc lỗ**."* — ch. 12 · PDF tr. 98

Đó là một phát biểu **kiểm được**. Cho một loạt giao dịch chạy qua sổ kép:

| giao dịch | loại | vốn chủ trước | sau | đổi |
| --- | :---: | ---: | ---: | ---: |
| Chủ sở hữu góp thêm vốn | ① | 6.000 | 7.000 | +1.000 |
| Chia cổ tức bằng tiền | ② | 7.000 | 6.700 | −300 |
| Bán hàng chịu 500 (doanh thu) | ③ | 6.700 | 7.200 | +500 |
| Ghi nhận giá vốn 300 | ③ | 7.200 | 6.900 | −300 |
| Trả lương 200 bằng tiền | ③ | 6.900 | 6.700 | −200 |
| Vay ngân hàng 800 | — | 6.700 | 6.700 | **0** |
| Trả bớt nợ vay 400 | — | 6.700 | 6.700 | **0** |
| Mua nguyên vật liệu chịu 600 | — | 6.700 | 6.700 | **0** |
| Trả tiền nhà cung cấp 600 | — | 6.700 | 6.700 | **0** |
| Khách hàng trả tiền 500 | — | 6.700 | 6.700 | **0** |
| Mua máy bằng tiền 700 | — | 6.700 | 6.700 | **0** |

⭐ **5 giao dịch đổi vốn chủ sở hữu — tất cả đều thuộc ba loại sách nêu. 6 giao dịch còn lại không đổi
một li nào**, dù chúng làm tổng tài sản chạy từ 6.000 lên 7.100. Cả hai chiều đều chốt bằng `assert`:
thêm một giao dịch phá luật thì file sẽ đổ.

💼 **Vì sao đáng nhớ:** nó cho biết bạn **có thể** và **không thể** làm gì. Vay thêm tiền, trả bớt nợ,
mua máy, đổi kỳ hạn với nhà cung cấp — **không việc nào trong số đó làm doanh nghiệp giàu hơn một xu**.
Chúng chỉ đổi hình dạng bảng cân đối. Chỉ **lãi** và **lỗ** mới dịch được giá trị sổ sách.

📌 Đó chính là nội dung của [bài 4](bai_04_bang_can_doi_ke_toan.md) mục 3 — phép so sánh GPA — viết lại
dưới dạng một quy tắc chặn.

---

## 3. Doanh nghiệp tí hon: nơi hai báo cáo gặp nhau

Chương 13 mở bằng một câu mà sách tự gọi là bí mật:

> *"Xin tiết lộ với bạn **một trong những bí mật được giữ kín nhất** của thế giới báo cáo tài chính:
> **một thay đổi trong báo cáo này gần như luôn ảnh hưởng đến báo cáo kia.** Vì vậy, khi quản lý báo
> cáo kết quả kinh doanh, cũng là lúc bạn **đồng thời tác động đến bảng cân đối kế toán**."*
> — ch. 13 · PDF tr. 100

Rồi chứng minh bằng một doanh nghiệp *"mới toanh (và rất nhỏ!)"*. Đầu tháng: tiền 25, phải thu 0 →
tổng 25; phải trả 0, vốn chủ 25.

Trong tháng: mua 50 nguyên vật liệu, sản xuất và bán được 100 thành phẩm, chịu thêm 25 chi phí khác.

| bút toán | tiền | phải thu | phải trả | vốn chủ |
| --- | ---: | ---: | ---: | ---: |
| mua 50 nguyên vật liệu (chịu) | 25 | 0 | 50 | 25 |
| bán 100 (khách chưa trả) | 25 | 100 | 50 | 125 |
| ghi nhận giá vốn 50 | 25 | 100 | 50 | 75 |
| trả 25 chi phí khác bằng tiền | **0** | **100** | **50** | **50** |

Báo cáo kết quả kinh doanh tháng đó: doanh thu 100 − giá vốn 50 = lợi nhuận gộp 50 − chi phí 25 =
**lợi nhuận thuần 25**.

Bảng cân đối cuối tháng: tiền **0**, phải thu **100** → tổng **100**; phải trả **50**, vốn chủ **50**.
Cả bốn con số khớp từng số với sách (PDF tr. 101), chốt bằng `assert`.

> *"Như bạn thấy, khoản lợi nhuận thuần 25 đô-la **đã trở thành vốn chủ sở hữu**… Đây là thực tế ở tất
> cả các doanh nghiệp: lãi ròng sẽ được cộng vào vốn, trừ khi nó được dùng làm cổ tức."*
> — ch. 13 · PDF tr. 101

### Nhưng câu quan trọng nhất nằm ở dòng sau đó

> *"Hãy lưu ý thêm một điều nữa ở ví dụ đơn giản này: **doanh nghiệp đã phải gồng cả tháng vì không có
> tiền!** Họ làm ra tiền, và vốn chủ sở hữu tăng, **nhưng họ không có đồng nào trong ngân hàng**."*
> — ch. 13 · PDF tr. 101

| | đầu tháng | cuối tháng |
| --- | ---: | ---: |
| **tiền** | 25 | **0** |
| **vốn chủ sở hữu** | 25 | **50** |

Hai con số đi **ngược chiều nhau** trong cùng một tháng có lãi. Đó là toàn bộ Phần IV, và là
[bài 6](bai_06_loi_nhuan_khac_tien_mat.md).

---

## 4. Tiền và vốn chủ đi ngược chiều đến bao giờ

Sách dừng ở đó. Câu chưa hỏi: *nếu tháng sau cũng thế, và tháng sau nữa cũng thế?*

Giữ nguyên cơ cấu của sách — giá vốn 50% doanh thu, chi phí khác 25% doanh thu trả ngay bằng tiền;
khách trả sau một tháng; nhà cung cấp được trả sau một tháng — và cho doanh thu tăng 20% mỗi tháng
*(các giả định này là của bài học)*:

| tháng | doanh thu | VỐN CHỦ | TIỀN MẶT | khoảng cách |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 100 | 50 | 0 | 50 |
| 3 | 144 | 116 | 44 | 72 |
| 6 | 249 | 273 | 149 | 124 |
| 9 | 430 | 545 | 330 | 215 |
| 12 | 743 | **1.015** | **643** | **372** |

⭐ **Cả hai cột đều tăng** — với kỳ hạn của sách thì doanh nghiệp này không chết đói. Nhưng cột *khoảng
cách* nở ra theo doanh thu, và nó có công thức chính xác:

> **khoảng cách = phải thu − phải trả = 0,5 × doanh thu tháng đó**

Tháng 12: 372 = 0,5 × 743. Mỗi đồng doanh thu tăng thêm **khoá lại 0,5 đồng** trong vốn lưu động, và
không nhả ra chừng nào còn bán được.

### ⚠️ Vậy khi nào thì nó chết đói? Khi kỳ hạn lệch

Sách cho khách trả sau **đúng một tháng** — bằng y kỳ hạn của nhà cung cấp. Nới kỳ hạn thu tiền ra,
giữ nguyên mọi thứ khác, và đo **tiền thấp nhất trong 12 tháng**:

| khách trả sau | g = 0% | g = 10% | g = 20% | g = 40% |
| --- | ---: | ---: | ---: | ---: |
| **1 tháng** *(như sách)* | 0 | 0 | 0 | 0 |
| **2 tháng** | −75 | −78 | −80 | −1.411 |
| **3 tháng** | −150 | −163 | −492 | −3.478 |

⭐ Đọc theo **chiều dọc**: kéo kỳ hạn thu tiền từ 1 lên 2 tháng là đủ để doanh nghiệp cạn tiền **ngay
cả khi không tăng trưởng một đồng nào** (cột g=0%). Đọc theo **chiều ngang** ở hàng 2 và 3: càng tăng
trưởng nhanh càng cần nhiều tiền. Nhưng hàng 1 thì **phẳng** — tăng trưởng không làm gì cả.

⭐ Kết luận **không phải** "tăng trưởng nguy hiểm". Kết luận là: **độ lệch kỳ hạn quyết định, còn tăng
trưởng chỉ khuếch đại cái độ lệch sẵn có.** Bài 6 và bài 11 sẽ đo chính xác độ lệch ấy bằng DSO và DPO.

💼 Và đây là đẳng thức nối hai cột — chính là báo cáo lưu chuyển tiền tệ thu nhỏ, trước khi
[bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) gọi tên nó:

> **tiền = tiền đầu kỳ + lợi nhuận luỹ kế − Δphải thu + Δphải trả − Δtồn kho**
>
> 25 + 990 − 743 + 372 = **643** — đúng bằng tiền thực tế tháng 12. Chốt bằng `assert`.

---

## 5. Lỗ liên tiếp — bao lâu thì vốn chủ sở hữu âm

> *"Nếu một doanh nghiệp chịu lỗ mỗi tháng, thì cuối cùng nợ phải trả của doanh nghiệp đó sẽ **vượt quá
> tài sản, vốn chủ sở hữu sẽ âm**. Doanh nghiệp đứng trên **bờ vực phá sản**."* — ch. 13 · PDF tr. 101

Sách không đặt số. Công ty mẫu có vốn chủ sở hữu 2.457 triệu, và năm 2005 lãi 248 triệu:

| mức lỗ mỗi năm | số năm đến khi vốn chủ = 0 |
| --- | ---: |
| 248 *(bằng đúng mức lãi hiện tại)* | **9,9 năm** |
| 496 | 5,0 năm |
| 992 | 2,5 năm |

⭐ Lỗ đúng bằng mức lãi hiện tại thì mất gần **mười năm**. Đó là nét đẹp của một bảng cân đối dày: nó
chịu được một chuỗi năm tệ hại rất dài. Doanh nghiệp tí hon ở mục 3 chỉ có vốn chủ 50 — nó chịu được
**đúng hai tháng** lỗ 25.

⚠️ Nhưng **"vốn chủ sở hữu âm" không phải là ngày doanh nghiệp chết. Nó chết khi hết tiền.** Hai mốc đó
khác nhau, và thường mốc **tiền** đến trước — đúng như mục 4 vừa chỉ ra. Sách viết *"đứng trên bờ vực
phá sản"*, không viết *"đã phá sản"*.

---

## 6. Ba tình huống nhà quản lý — đặt số vào cả ba

Chương 13 nêu ba tình huống *"tăng lợi nhuận nhưng hại bảng cân đối"*, mỗi tình huống kết bằng một câu
hỏi bỏ ngỏ. Cả ba đều cần một con số: **giá của tiền**. Suy từ chính báo cáo công ty mẫu — trả lãi 191
trên 1.714 nợ có lãi = **11,1%/năm** *(cách gộp nợ có lãi là của bài học)*.

### ① Giám đốc nhà máy mua nguyên liệu số lượng lớn vì có "mối tốt"

> *"Rất hợp lý đúng không? **Không hẳn.** Dòng hàng tồn kho trên bảng cân đối kế toán sẽ tăng lên.
> Khoản phải trả cũng sẽ tăng theo tương ứng. Cuối cùng, nhà máy sẽ phải rút tiền mặt ra để thanh toán
> những khoản phải trả − **có thể là rất sớm trước khi nguyên vật liệu được dùng để tạo ra doanh
> thu**."* — ch. 13 · PDF tr. 102

Giá vốn cả năm 6.756 → 563 mỗi tháng. Mua 6 tháng một lần thay vì 1 tháng một lần, tồn kho bình quân
tăng từ 0,5 lên 3,0 tháng, tức **+1.408 triệu**:

| chi phí lưu kho/năm | chiết khấu hoà vốn |
| --- | ---: |
| 0% giá trị tồn kho | 2,32% |
| **5%** | **3,36%** |
| 10% | 4,40% |
| 15% | 5,45% |

⭐ Với chi phí lưu kho 5%, "mối tốt" phải giảm giá **ít nhất 3,36%** mới hoà vốn. Dưới ngưỡng đó thì
đây không phải một mối tốt — **đó là một khoản vay trả lãi bằng hàng tồn kho.**

### ② Giám đốc bán hàng nhắm vào khách hàng nhỏ hơn

> *"Có lẽ không. Khách hàng nhỏ hơn không thể có cấp rủi ro tín dụng tốt như các khách hàng lớn. Các
> khoản phải thu có thể tăng mạnh… Một giám đốc bán hàng có trí tuệ tài chính sẽ phải điều tra các khả
> năng định giá: **anh ta có thể tăng thêm lợi nhuận gộp để bù đắp cho những rủi ro ngày càng tăng
> không?**"* — ch. 13 · PDF tr. 103

**Sách hỏi và không trả lời.** Trả lời — trên mỗi 100 đô-la doanh thu mới:

| nhóm khách | DSO (ngày) | nợ xấu | phí vốn | TỔNG PHÍ | cần thêm biên gộp |
| --- | ---: | ---: | ---: | ---: | ---: |
| hiện tại | 54,4 | 0,5% | 1,68 | 2,18 | — *(gốc)* |
| nhỏ — 75 ngày | 75,0 | 2,0% | 2,32 | 4,32 | 2,14 điểm |
| **nhỏ — 90 ngày** | 90,0 | 3,0% | 2,79 | 5,79 | **3,60 điểm** |
| nhỏ — 120 ngày | 120,0 | 5,0% | 3,71 | 8,71 | 6,53 điểm |

⭐ Nhóm *"90 ngày, nợ xấu 3%"* cần biên gộp cao hơn nhóm hiện tại **3,60 điểm**. Biên gộp đang là 22,2%,
nên nhóm mới phải bán được với biên **25,8% mới chỉ là hoà vốn** so với khách cũ. Nếu phòng bán hàng
không đẩy được giá lên ngần ấy, thương vụ này **làm doanh thu tăng và làm công ty nghèo đi**.

*(Các mức DSO và tỷ lệ nợ xấu trong bảng là giả định của bài học để đo độ nhạy; sách không nêu.)*

### ③ Giám đốc CNTT mua hệ thống máy tính mới

> *"Doanh nghiệp sẽ trông vào đâu để thanh toán cho dàn thiết bị mới? Nếu doanh nghiệp được **tạo đòn
> bẩy quá đà**… việc vay tiền để chi trả cho hệ thống mới có lẽ **không phải là ý hay**."*
> — ch. 13 · PDF tr. 103

Hệ thống giá 200 triệu:

| | tổng tài sản | tổng nợ | vốn chủ | nợ/vốn chủ |
| --- | ---: | ---: | ---: | ---: |
| hiện tại | 5.193 | 2.736 | 2.457 | 1,11 lần |
| **vay để mua** | 5.393 | 2.936 | 2.457 | **1,19 lần** |
| **phát hành cổ phiếu** | 5.393 | 2.736 | 2.657 | **1,03 lần** |

⭐ Vay thì tỷ lệ nợ/vốn chủ **tăng**; phát hành cổ phiếu thì nó **tụt xuống dưới mức hiện tại**. Và nếu
vay, tiền lãi thêm là **22,3 triệu/năm** — hệ thống phải làm ra hơn ngần ấy EBIT **mỗi năm** thì mới
bắt đầu có lãi. So với EBIT hiện tại 652, đó là **3,4%**.

💼 Sách nói thẳng đây không phải việc của giám đốc CNTT: *"Đưa ra các quyết định huy động lượng vốn cần
thiết để vận hành doanh nghiệp là công việc của **giám đốc tài chính và thủ quỹ**."* Nhưng hiểu bảng
trên giúp ông ta chọn **đúng lúc** để đề nghị mua.

---

## 7. Ba câu hỏi đánh giá sức khoẻ — và câu hỏi thứ tư sắc hơn cả ba

> *"Bảng cân đối kế toán **giải đáp rất nhiều câu hỏi**."* — ch. 13 · PDF tr. 104

| # | câu hỏi của sách | công ty mẫu |
| ---: | --- | --- |
| ① | *"Doanh nghiệp có **khả năng thanh toán** không? Tài sản có lớn hơn nợ phải trả, để vốn chủ sở hữu có thể **dương** không?"* | 5.193 − 2.736 = **2.457** ✓ |
| ② | *"Doanh nghiệp có **khả năng thanh toán hoá đơn** không? Các số liệu quan trọng ở đây là tài sản ngắn hạn, **đặc biệt là tiền mặt**, so với nợ ngắn hạn."* | TSNH/NNH = **2,34 lần** ✓<br>nhưng riêng **tiền** chỉ 83 trên 1.174 = **7,1%** ⚠️ |
| ③ | *"**Vốn chủ sở hữu có tăng** theo thời gian không?"* | 2.375 → 2.457, tăng **82** ✓ |

⚠️ Chú ý chỗ sách nhấn *"đặc biệt là tiền mặt"*. Hệ số 2,34 lần trông rất an toàn, nhưng phần lớn tài
sản ngắn hạn là **phải thu và tồn kho**, không phải tiền. [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) tách hai con số này ra.

### Rồi sách hỏi thêm một câu sắc hơn hẳn ba câu trên

> *"**Nếu vốn chủ sở hữu tăng, thì nguyên nhân là vì doanh nghiệp đang huy động vốn, hay là vì doanh
> nghiệp đã tự làm ra tiền?**"* — ch. 13 · PDF tr. 104

| nguồn làm vốn chủ sở hữu tăng | triệu $ | tỷ trọng |
| --- | ---: | ---: |
| Huy động vốn (phát hành cổ phiếu) | **0** | 0,0% |
| Tự làm ra (lợi nhuận giữ lại) | **82** | **100,0%** |

⭐ **100% mức tăng là tự làm ra.** Công ty mẫu không phát hành thêm một cổ phiếu nào năm 2005 — 74 triệu
cổ phiếu và 1.110 vốn bổ sung y nguyên cả hai năm. Đó là câu trả lời tốt nhất có thể có, và nó **đọc
được trong một phút** chỉ bằng cách đặt hai bảng cân đối cạnh nhau.

Sách đóng Phần III:

> *"Bảng cân đối kế toán − giống như **bảng điểm bình quân tích luỹ** của doanh nghiệp − có lẽ là loại
> **báo cáo quan trọng nhất**."* — ch. 13 · PDF tr. 104

---

## 8. 📚 Hộp công cụ — "nhân viên là tài sản giá trị nhất của chúng ta"

Sách mở hộp công cụ bằng một câu hỏi khó chịu:

> *"Bạn nghe các CEO nói điều này suốt… Nhưng bạn cũng thấy một số CEO **hành xử như thể các nhân viên
> không phải là tài sản**. Bạn có tưởng tượng ra một doanh nghiệp giảm biên chế hoặc sa thải **món tài
> sản nào khác** − đơn giản là tống thứ đó ra đường với hi vọng rằng nó sẽ tự biết bỏ đi – không?"*
> — ch. 13 · PDF tr. 105

Hai lý do nhân viên **không** lên bảng cân đối:

1. **Không ai biết định giá.** *"Giá trị của kiến thức là bao nhiêu? Không có một kế toán viên nào muốn
   giải quyết dứt điểm vấn đề đó."*
2. **Doanh nghiệp không sở hữu nhân viên.** *"Thế nên ta không thể xem họ như là tài sản theo thuật ngữ
   kế toán."*

Ngoại lệ duy nhất: khi mua lại một doanh nghiệp, *"giá trị của nhân viên được nhìn nhận như một phần
của **lợi thế thương mại**"* — đúng dòng mà [bài 4](bai_04_bang_can_doi_ke_toan.md) mục 8 mổ xẻ.

Sách kết luận thẳng thắn về giới hạn của chính lập luận mình: đối đãi tốt với nhân viên *"sẽ thúc đẩy
lợi nhuận gia tăng trong thời gian dài"*, nhưng *"**hiếm khi có một tương quan một-đối-một** giữa một
bên là văn hoá và quan điểm của doanh nghiệp và một bên là hoạt động tài chính."*

---

## 9. WorldCom — vốn hoá chi phí, nhìn từ bảng cân đối

Hộp công cụ thứ hai đặt ranh giới quan trọng nhất của cả Phần III:

> *"Bạn có thể thấy sự khác biệt giữa 'chi phí hoạt động' (trên báo cáo kết quả kinh doanh) và 'chi phí
> đầu tư cơ bản' (trên bảng cân đối kế toán) rất rõ ràng và dễ hiểu. **Nhưng rõ ràng là không phải
> vậy. Thực tế là đây là tấm vải để vẽ nên bức tranh nghệ thuật tài chính.**"* — ch. 13 · PDF tr. 106

> *"Chi phí đường dây [của WorldCom] được xử lý như những khoản chi phí hoạt động thông thường, nhưng
> bạn có thể lý luận (**dù lập luận này không chính xác**) rằng một số trong đó thực ra là những khoản
> đầu tư… Logic này đã thuyết phục được **Scott Sullivan**, giám đốc tài chính của công ty, người bắt
> đầu **'vốn hoá'** chi phí đường dây vào cuối thập niên 1990. Chuẩn xác: những khoản chi phí này **biến
> mất khỏi báo cáo**, và lợi nhuận của công ty **tăng lên hàng tỷ đô-la**."* — ch. 13 · PDF tr. 106

[Bài 1](bai_01_nghe_thuat_tai_chinh.md) mục 3③ đã đo tác động lên báo cáo KQKD. Đây đo tác động lên
**bảng cân đối** — chỗ thủ thuật này để lại dấu vết. Vốn hoá 100 triệu chi phí mỗi năm, khấu hao 10 năm:

| năm | đã vốn hoá | khấu hao năm | LN khai khống | luỹ kế | TÀI SẢN ẢO |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100 | 10 | 90 | **90** | **90** |
| 2 | 200 | 20 | 80 | **170** | **170** |
| 3 | 300 | 30 | 70 | **240** | **240** |
| 4 | 400 | 40 | 60 | **300** | **300** |
| 5 | 500 | 50 | 50 | **350** | **350** |

⭐ Hai cột cuối **giống hệt nhau**, và đó là đẳng thức đáng nhớ:

> **tài sản ảo trên bảng cân đối = luỹ kế lợi nhuận đã khai khống**

Chốt bằng `assert` ở mọi năm. **Bảng cân đối vẫn cân hoàn hảo suốt cả năm năm** — nó không hề "phát
hiện" ra gian lận. Nó chỉ **phình ra ở một dòng**.

### ⚠️ Và đây là chỗ phải cẩn thận

Vốn hoá một khoản chi phí làm tiền chuyển từ **hoạt động kinh doanh** sang **hoạt động đầu tư** trên
báo cáo lưu chuyển tiền tệ. Tổng tiền **không đổi**, nhưng dòng *"tiền từ HĐKD"* lại **đẹp hơn**:

| | THỰC TẾ | SAU KHI VỐN HOÁ |
| --- | ---: | ---: |
| Tiền từ HĐKD | 498 | **598** |
| Tiền từ đầu tư | −185 | **−285** |
| **Thay đổi trong tiền** | **11** | **11** |

⭐ **Cả lợi nhuận lẫn tiền từ hoạt động kinh doanh đều đẹp lên.** Đó là lý do thủ thuật này chạy được
lâu đến vậy: *"Đối với Phố Wall, có vẻ như WorldCom **đột nhiên làm ra được lợi nhuận trong một ngành
suy thoái** và mọi chuyện không bị ai phát hiện cho đến mãi sau này."*

💼 Vậy bắt bằng gì? Bằng cái **không đổi được**: **tổng tiền**, và **tốc độ phình của dòng tài sản**.
Nếu một dòng tài sản lớn nhanh hơn doanh thu năm này qua năm khác mà tổng tiền không nhúc — đó là chỗ
cần hỏi. [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) sẽ dựng công cụ đó.

Sách kết hộp công cụ bằng một câu hỏi, và nó không dành cho WorldCom:

> *"Một số công ty sẽ xử lý những khoản gây bàn cãi không thường xuyên này như là chi phí đầu tư cơ bản
> hòng đẩy thu nhập của mình tăng lên chút ít. **Công ty của bạn có như vậy không?**"* — ch. 13 · PDF tr. 107

---

## 10. 🇻🇳 Đối chiếu Việt Nam

**① Phương trình này không có gì để đối chiếu — nó phổ quát.** Kế toán Việt Nam cũng là **ghi sổ kép**
(Nợ / Có), và đẳng thức *tài sản = nguồn vốn* đúng y hệt. Khác biệt duy nhất là **cách bày**: mẫu B01-DN
in hai khối **"TÀI SẢN"** và **"NGUỒN VỐN"**, mỗi khối kết bằng một dòng **"TỔNG CỘNG"**, và hai dòng ấy
phải bằng nhau. Bảng của Mỹ để người đọc tự cộng; bảng Việt Nam in sẵn hai tổng cạnh nhau — dễ kiểm hơn.

**② Ba câu hỏi sức khoẻ chạy trên Vinamilk.** Cùng ba câu của mục 7:

| | công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024, IFRS) |
| --- | ---: | ---: |
| ① vốn chủ sở hữu dương? | ✓ 2.457 | ✓ 37.165.930 |
| ② tài sản ngắn hạn / nợ ngắn hạn | 2,34 lần | 2,03 lần |
| ② **riêng tiền** / nợ ngắn hạn | **7,1%** | **12,0%** |
| ② **tiền + đầu tư ngắn hạn** / nợ ngắn hạn | — | **137,8%** |

⭐ Dòng cuối là chỗ hai doanh nghiệp khác hẳn nhau. Hệ số thanh toán ngắn hạn của hai bên gần bằng nhau
(2,34 và 2,03), nhưng **Vinamilk có thể trả hết toàn bộ nợ ngắn hạn chỉ bằng tiền và tiền gửi, còn dư
38%**. Công ty mẫu thì phải bán được hàng và thu được nợ mới trả nổi. **Cùng một hệ số, hai tình trạng
hoàn toàn khác nhau** — đúng lý do sách nhấn *"đặc biệt là tiền mặt"*.

⚠️ Câu ③ *"vốn chủ sở hữu tăng vì huy động vốn hay tự làm ra?"* **chưa trả lời được cho Vinamilk** trong
kho này: bộ số liệu đang có chỉ gồm bảng cân đối 2024, không có vốn chủ sở hữu 2023 để so. Đây là một
lỗ hổng dữ liệu **có thật**, không phải kết luận — muốn trả lời thì phải lấy thêm cột so sánh từ chính
báo cáo gốc.

**③ Câu hỏi của mục 9 có một địa chỉ cụ thể trong báo cáo Việt Nam.** Ranh giới *"chi phí hoạt động hay
chi phí đầu tư cơ bản"* ở Việt Nam nằm giữa việc ghi thẳng vào chi phí và việc treo ở **"chi phí trả
trước dài hạn"** hoặc vốn hoá vào **tài sản cố định vô hình**. Điều kiện ghi nhận nằm ở **VAS 03** (tài
sản cố định hữu hình) và **VAS 04** (tài sản cố định vô hình) — và như mọi điều kiện ghi nhận, chúng
đòi một **phán đoán** về việc khoản chi có mang lại lợi ích kinh tế tương lai hay không.

💼 Nên khi đọc một báo cáo Việt Nam, câu hỏi mà sách để lại — *"công ty của bạn có như vậy không?"* — có
một cách kiểm cụ thể: **so tốc độ tăng của dòng "chi phí trả trước dài hạn" với tốc độ tăng doanh thu**.
Nếu nó phình nhanh hơn nhiều mà không có giải thích trong thuyết minh, đó là chỗ đáng hỏi.

---

## 11. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py`](../thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py)
rồi chạy lại. Không có lời giải.

1. **Phá sổ kép.** Ở mục 1, thêm một bút toán chỉ động vào **một** dòng — ví dụ `ghi(tien=1_000)`. Điều
   gì xảy ra? Thông báo lỗi nói gì? Vì sao đó là hành vi **đúng** của file này?

2. **Giao dịch thứ mười hai.** Ở mục 2, nghĩ ra ba giao dịch mới và tự gán nhãn ①②③ hay —. Chạy lại. Có
   cái nào bạn gán sai không?

3. **Mua tài sản bằng cổ phiếu.** Vẫn mục 2: doanh nghiệp phát hành cổ phiếu để **trả cho một thương vụ
   mua lại**, không nhận đồng tiền nào. Vốn chủ sở hữu có đổi không? Nó thuộc loại nào trong ba loại?

4. **Doanh nghiệp tí hon thu tiền ngay.** Ở mục 3, đổi bút toán bán hàng thành thu tiền ngay
   (`tien=100` thay vì `phai_thu=100`). Tiền cuối tháng là bao nhiêu? Vốn chủ sở hữu có đổi không? Điều
   này nói gì về quan hệ giữa hai con số ấy?

5. **Nhà cung cấp đòi trả ngay.** Ở mục 4, đổi kỳ hạn trả nhà cung cấp từ 1 tháng xuống **0 tháng** (trả
   ngay). Bảng "tiền thấp nhất" đổi thế nào? So sánh với việc kéo dài kỳ hạn thu tiền — cái nào hại hơn?

6. **Biên mỏng hơn.** Vẫn mục 4, đổi giá vốn từ 50% lên **70%** doanh thu. Công thức "khoảng cách =
   0,5 × doanh thu" giờ thành gì? Doanh nghiệp biên mỏng cần nhiều hay ít vốn lưu động hơn?

7. **Bao lâu thì hết tiền.** Ở mục 5, thay vì hỏi bao lâu thì vốn chủ sở hữu âm, hãy hỏi: với 83 triệu
   tiền mặt và lỗ 248 triệu/năm, bao lâu thì **hết tiền**? So hai con số. Cái nào là hạn chót thật?

8. **Mối tốt bao nhiêu mới đáng.** Ở mục 6①, đổi từ mua 6 tháng xuống mua **3 tháng** một lần. Chiết
   khấu hoà vốn giờ là bao nhiêu? Vẽ quan hệ giữa "số tháng mua một lần" và "chiết khấu cần có".

9. **Khách hàng nhỏ ở doanh nghiệp biên dày.** Ở mục 6②, thử với doanh nghiệp có biên gộp **45%**. Số
   điểm cần thêm có đổi không? Vì sao doanh nghiệp biên dày **dễ** chấp nhận khách rủi ro hơn?

10. **Vốn hoá rồi dừng.** Ở mục 9, cho vốn hoá 100/năm trong 3 năm rồi **dừng hẳn** từ năm 4. Lợi nhuận
    năm 4 và năm 5 ra sao? Vì sao thủ thuật này **không thể dừng lại** một khi đã bắt đầu?

---

## 12. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Ghi sổ kép | double-entry bookkeeping | mỗi bút toán chạm **cả hai** vế của phương trình |
| Bút toán | journal entry | một lần ghi sổ |
| Nguồn vốn | sources of funds | nửa dưới bảng cân đối — **gồm cả nợ** |
| Lợi nhuận giữ lại | retained earnings | nơi lợi nhuận thuần **chảy vào** bảng cân đối |
| Vốn lưu động | working capital | tài sản ngắn hạn − nợ ngắn hạn; nơi tiền bị **khoá lại** |
| Vốn hoá | capitalize | ghi một khoản chi thành **tài sản** thay vì chi phí |
| Chi phí đầu tư cơ bản | capital expenditure | khoản chi tạo ra tài sản dài hạn |
| Đòn bẩy quá đà | over-leveraged | nợ quá nặng so với vốn chủ sở hữu |
| Hệ số thanh toán ngắn hạn | current ratio | tài sản ngắn hạn / nợ ngắn hạn |
| Dự phòng nợ xấu | allowance for bad debt | ước tính phần khách sẽ không trả |
| 💼 Kỳ thu tiền bình quân | days sales outstanding (DSO) | phải thu ÷ doanh thu mỗi ngày — **cụm từ chưa xuất hiện ở ch. 12–13** |
| 💼 Độ lệch kỳ hạn | payment-terms mismatch | thu chậm hơn trả — **cụm từ không có trong sách** |

---

## 13. Câu hỏi tự kiểm tra

1. Kể ba lý do sách đưa ra cho việc bảng cân đối luôn cân. Lý do nào **kiểm được**? (mục 1)
2. Vì sao lý do ① tuy đúng nhưng rỗng? (mục 1)
3. Phát biểu lý do ② bằng lời của bạn. Vì sao *"chúng buộc phải như thế"*? (mục 1)
4. Trong ba giao dịch đầu đời, tổng tài sản đổi từ bao nhiêu đến bao nhiêu? Vốn chủ sở hữu thì sao? (mục 1)
5. *"Nếu tài sản không cân bằng với nợ phải trả và vốn chủ sở hữu, ta sẽ ___."* Điền và giải thích vì
   sao câu này khác hẳn "bảng bị sai". (mục 1)
6. Kể **ba** việc — và chỉ ba — chạm được vào vốn chủ sở hữu. (mục 2)
7. Vay ngân hàng 800 rồi trả bớt 400: vốn chủ sở hữu đổi bao nhiêu? Vì sao? (mục 2)
8. Doanh nghiệp tí hon: liệt kê bốn bút toán trong tháng và bảng cân đối cuối tháng. (mục 3)
9. Lợi nhuận thuần 25 đi đâu trên bảng cân đối? Dòng nào? (mục 3)
10. Tiền và vốn chủ sở hữu của doanh nghiệp tí hon đi theo chiều nào trong tháng đó? (mục 3)
11. Viết công thức "khoảng cách" giữa vốn chủ sở hữu và tiền mặt ở mục 4. Nó bằng gì? (mục 4)
12. Với kỳ hạn của sách (khách trả sau 1 tháng), tăng trưởng 40%/tháng có làm doanh nghiệp cạn tiền
    không? Vì sao? (mục 4)
13. Kéo kỳ hạn thu tiền từ 1 lên 2 tháng: doanh nghiệp cạn tiền ở mức tăng trưởng nào? (mục 4)
14. *"Không phải ___ giết doanh nghiệp. Là ___."* Điền. (mục 4)
15. Viết đẳng thức nối tiền với lợi nhuận luỹ kế. Báo cáo nào sẽ dùng đúng đẳng thức này? (mục 4)
16. Công ty mẫu lỗ đúng bằng mức lãi hiện tại thì bao lâu vốn chủ sở hữu về 0? Doanh nghiệp tí hon thì
    bao lâu? (mục 5)
17. *"Vốn chủ sở hữu âm"* có phải là ngày doanh nghiệp chết không? Mốc nào thường đến trước? (mục 5)
18. "Mối tốt" mua sỉ phải chiết khấu bao nhiêu mới hoà vốn, với chi phí lưu kho 5%? Nếu ít hơn thì thực
    chất đó là gì? (mục 6①)
19. Nhóm khách 90 ngày / nợ xấu 3% cần biên gộp bao nhiêu mới hoà vốn so với khách hiện tại? (mục 6②)
20. Sách hỏi câu gì ở tình huống ② và có trả lời không? (mục 6②)
21. Mua hệ thống 200 triệu bằng vay và bằng phát hành cổ phiếu: tỷ lệ nợ/vốn chủ đổi ra sao? (mục 6③)
22. Nếu vay, hệ thống phải sinh ra bao nhiêu EBIT mỗi năm mới bắt đầu có lãi? (mục 6③)
23. Kể ba câu hỏi sức khoẻ của chương 13. Công ty mẫu trả lời thế nào cho từng câu? (mục 7)
24. Hệ số thanh toán ngắn hạn 2,34 lần, nhưng riêng tiền chỉ bằng bao nhiêu phần trăm nợ ngắn hạn? Vì
    sao chi tiết đó quan trọng? (mục 7)
25. Câu hỏi thứ tư — sắc hơn cả ba câu trên — là gì? Công ty mẫu trả lời ra sao? (mục 7)
26. Hai lý do nhân viên **không** lên bảng cân đối là gì? Ngoại lệ duy nhất? (mục 8)
27. Sách tự nhận giới hạn nào cho lập luận "đối đãi tốt với nhân viên thì lợi nhuận tăng"? (mục 8)
28. Ai là người bắt đầu vốn hoá chi phí đường dây ở WorldCom, và vào lúc nào? (mục 9)
29. Viết đẳng thức nối **tài sản ảo** với **lợi nhuận khai khống**. (mục 9)
30. Bảng cân đối có "phát hiện" ra gian lận WorldCom không? Nó làm gì? (mục 9)
31. Vốn hoá chi phí làm dòng "tiền từ HĐKD" đẹp lên hay xấu đi? Tổng tiền thì sao? (mục 9)
32. Vậy phát hiện thủ thuật này bằng cách nào? (mục 9)
33. Câu hỏi sách kết hộp công cụ là gì? (mục 9)
34. Mẫu B01-DN của Việt Nam bày bảng cân đối khác cách của Mỹ ở chỗ nào? (mục 10)
35. Vinamilk và công ty mẫu có hệ số thanh toán ngắn hạn gần bằng nhau. Vì sao tình trạng của hai bên
    vẫn rất khác? (mục 10)
36. Câu hỏi nào ở mục 7 **chưa trả lời được** cho Vinamilk, và vì sao? (mục 10)
37. Ở báo cáo Việt Nam, dòng nào là địa chỉ cụ thể của câu hỏi mục 9? Kiểm nó bằng cách nào? (mục 10)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 5 — VÌ SAO BẢNG CÂN ĐỐI LẠI CÂN  (ch. 12–13, PDF tr. 97–107)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  BA LÝ DO:  ① vì ĐỊNH NGHĨA (đúng nhưng rỗng)                            ║
║             ② vì hai bên là HAI CÂU HỎI về CÙNG MỘT THỨ                  ║
║             ③ vì MỌI GIAO DỊCH chạm CẢ HAI VẾ  ← lý do dùng được         ║
║                                                                          ║
║  "Nếu tài sản không cân bằng với nợ và vốn chủ, ta SẼ KHÔNG THỂ CÓ       ║
║   bảng cân đối kế toán."  → cân KHÔNG phải tính chất, là ĐIỀU KIỆN       ║
║   để vật ấy tồn tại.                                                     ║
║                                                                          ║
║  ⭐ CHỈ BA VIỆC CHẠM ĐƯỢC VÀO VỐN CHỦ SỞ HỮU:                            ║
║     ① chủ góp vốn   ② chi tiền cho chủ   ③ ghi nhận LÃI hoặc LỖ          ║
║     Vay tiền · trả nợ · mua máy · đổi kỳ hạn — KHÔNG việc nào            ║
║     làm doanh nghiệp giàu hơn một xu. Chỉ đổi HÌNH DẠNG.                 ║
║                                                                          ║
║  ⭐ DOANH NGHIỆP TÍ HON — nơi hai báo cáo gặp nhau                       ║
║     lãi 25  →  vốn chủ 25 → 50   NHƯNG  tiền 25 → 0                      ║
║     "Họ làm ra tiền, và vốn chủ sở hữu tăng, NHƯNG HỌ KHÔNG CÓ           ║
║      ĐỒNG NÀO TRONG NGÂN HÀNG."                                          ║
║                                                                          ║
║  ⭐ KHOẢNG CÁCH GIỮA VỐN CHỦ VÀ TIỀN CÓ CÔNG THỨC:                       ║
║       khoảng cách = phải thu − phải trả = 0,5 × doanh thu tháng đó       ║
║     mỗi đồng doanh thu tăng thêm KHOÁ LẠI 0,5 đồng vốn lưu động          ║
║                                                                          ║
║  ⭐ TIỀN THẤP NHẤT trong 12 tháng, theo kỳ hạn thu tiền:                 ║
║       khách trả sau 1 tháng:     0    0    0    0   ← tăng trưởng vô hại ║
║       khách trả sau 2 tháng:   −75  −78  −80 −1.411                      ║
║       khách trả sau 3 tháng:  −150 −163 −492 −3.478                      ║
║                     (g=)       0%  10%  20%  40%                         ║
║     → KHÔNG PHẢI tăng trưởng giết doanh nghiệp. Là ĐỘ LỆCH KỲ HẠN.       ║
║       Tăng trưởng chỉ KHUẾCH ĐẠI cái độ lệch sẵn có.                     ║
║                                                                          ║
║  LỖ LIÊN TIẾP: công ty mẫu chịu được 9,9 NĂM lỗ bằng mức lãi.            ║
║     Doanh nghiệp tí hon chịu được ĐÚNG HAI THÁNG.                        ║
║     Nhưng vốn chủ âm ≠ chết. Chết khi HẾT TIỀN — mốc đó đến trước.       ║
║                                                                          ║
║  ⭐ BA CÂU HỎI SÁCH BỎ NGỎ, ĐÃ TRẢ LỜI:                                  ║
║     ① mua sỉ: phải chiết khấu ≥ 3,36% mới hoà vốn — dưới mức đó          ║
║        đó là KHOẢN VAY TRẢ LÃI BẰNG HÀNG TỒN KHO                         ║
║     ② khách nhỏ (90 ngày, nợ xấu 3%): cần thêm 3,60 ĐIỂM biên gộp        ║
║        → 22,2% phải thành 25,8% mới CHỈ LÀ HOÀ VỐN                       ║
║     ③ mua hệ thống 200 bằng vay: nợ/vốn chủ 1,11 → 1,19, lãi thêm        ║
║        22,3 triệu/năm = 3,4% EBIT hiện tại                               ║
║                                                                          ║
║  BA CÂU HỎI SỨC KHOẺ — và câu thứ tư SẮC HƠN CẢ BA:                      ║
║     "Vốn chủ sở hữu tăng vì HUY ĐỘNG VỐN hay vì TỰ LÀM RA TIỀN?"         ║
║     công ty mẫu: 0% huy động, 100% tự làm ra                             ║
║                                                                          ║
║  ⭐ WORLDCOM — vốn hoá chi phí, nhìn từ bảng cân đối                     ║
║       TÀI SẢN ẢO = LUỸ KẾ LỢI NHUẬN ĐÃ KHAI KHỐNG   (90/170/240/…)       ║
║     Bảng cân đối VẪN CÂN HOÀN HẢO — nó không phát hiện gì cả.            ║
║     Tệ hơn: vốn hoá làm "tiền từ HĐKD" 498 → 598 (ĐẸP LÊN),              ║
║     vì tiền chỉ chuyển sang mục đầu tư. TỔNG tiền không đổi: 11.         ║
║     → bắt bằng TỔNG tiền và TỐC ĐỘ PHÌNH của dòng tài sản.               ║
║                                                                          ║
║  🇻🇳 Vinamilk và công ty mẫu: hệ số ngắn hạn 2,03 vs 2,34 — gần bằng.     ║
║     Nhưng tiền + tiền gửi / nợ ngắn hạn: 137,8% vs 7,1%.                 ║
║     CÙNG MỘT HỆ SỐ, HAI TÌNH TRẠNG KHÁC HẲN.                             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần III — Bảng cân đối kế toán, nơi vén mở nhiều điều nhất**, PDF tr. 74–107.
    - Ch. 12 *Tại sao bảng cân đối kế toán lại cân đối?*, PDF tr. 97–99
      — *"bởi vì nó cân đối"* và *"chưa chắc bạn đã hiểu hết lý do"* (tr. 97); **ba cách hiểu**, lý do
      ① định nghĩa và ② *"chúng buộc phải như thế"* (tr. 97); ③ **doanh nghiệp mới — 50.000 / xe tải
      36.000 / vay 10.000** (tr. 97–98); ⭐ **ba việc chạm được vào vốn chủ sở hữu** (tr. 98); hai giao
      dịch — trả nợ 100.000 và mua thiết bị 100.000 trả trước 50.000 (tr. 98–99); *"nếu tài sản không
      cân bằng… ta sẽ không thể có bảng cân đối kế toán"* (tr. 99)
    - Ch. 13 *Báo cáo kết quả kinh doanh ảnh hưởng đến bảng cân đối kế toán*, PDF tr. 100–107
      — ⭐ *"một trong những bí mật được giữ kín nhất"* (tr. 100); **doanh nghiệp tí hon** — bảng cân
      đối đầu tháng, báo cáo KQKD, bảng cân đối cuối tháng (tr. 100–101); *"lợi nhuận thuần 25 đô-la đã
      trở thành vốn chủ sở hữu"* và **lỗ liên tiếp → vốn chủ âm** (tr. 101); ⭐⭐ *"đã phải gồng cả
      tháng vì không có tiền!"* (tr. 101); **và nhiều tác động khác** (tr. 102); ⭐ **ba tình huống nhà
      quản lý** — giám đốc nhà máy mua sỉ (tr. 102), giám đốc bán hàng và khách hàng nhỏ (tr. 102–103),
      giám đốc CNTT và đòn bẩy (tr. 103); **ba câu hỏi sức khoẻ** và câu hỏi *"huy động vốn hay tự làm
      ra tiền?"* (tr. 104); *"bảng điểm bình quân tích luỹ… báo cáo quan trọng nhất"* (tr. 104);
      hộp công cụ **"nhân viên là tài sản giá trị nhất"** (tr. 105–106); hộp công cụ **chi phí hoạt
      động hay chi phí đầu tư cơ bản** và **WorldCom / Scott Sullivan** (tr. 106–107)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 5, 6, 7, 9
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 10](#10--đối-chiếu-việt-nam).
- **Chuẩn mực kế toán Việt Nam số 03 và số 04 (VAS 03, VAS 04)** — điều kiện ghi nhận tài sản cố định
  hữu hình và vô hình. Nhắc ở [mục 10](#10--đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py`](../thuc_hanh/bai-05-vi-sao-bang-can-doi-lai-can.py):
  - **sổ kép `assert` phương trình sau TỪNG bút toán** — 20 bút toán trong ba mục đầu, không cái nào
    được phép làm lệch;
  - **quy tắc ba loại**: mọi giao dịch đổi vốn chủ đều thuộc ①②③, và mọi giao dịch ngoài ba loại đều
    **không** đổi vốn chủ — chốt cả hai chiều bằng `assert`;
  - doanh nghiệp tí hon: bốn con số cuối tháng khớp **từng số** với PDF tr. 101, chốt bằng `assert`;
  - khoảng cách vốn chủ − tiền **đúng bằng 0,5 × doanh thu**, chốt bằng `assert`;
  - đẳng thức tiền = tiền đầu kỳ + lợi nhuận luỹ kế − Δphải thu + Δphải trả **đóng**, chốt bằng `assert`;
  - kéo dài kỳ hạn thu tiền **luôn** làm tiền thấp nhất giảm, ở mọi mức tăng trưởng — chốt bằng `assert`;
  - WorldCom: **tài sản ảo = luỹ kế lợi nhuận khai khống** ở mọi năm, và **tổng tiền không đổi** sau khi
    vốn hoá — chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** toàn bộ tham số mô phỏng ở mục 4 (tăng trưởng,
  kỳ hạn thu/trả, cơ cấu chi phí); lãi suất 11,1% suy từ báo cáo và cách gộp "nợ có lãi" ở mục 6; chu kỳ
  mua 6 tháng và dải chi phí lưu kho 0–15% ở mục 6①; các mức DSO và tỷ lệ nợ xấu ở mục 6②; giá hệ thống
  200 triệu ở mục 6③; mức vốn hoá 100 triệu/năm và kỳ khấu hao 10 năm ở mục 9. Mọi con số **của sách**
  đều được trích kèm mốc `ch. N · PDF tr. M`.

---

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| **5** | **Vì sao bảng cân đối lại cân** ← *bạn đang ở đây* | ch. 12–13 | 🎯 |
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
