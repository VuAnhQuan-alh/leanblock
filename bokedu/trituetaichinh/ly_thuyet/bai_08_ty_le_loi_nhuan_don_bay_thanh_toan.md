# Bài 8 — Tỷ lệ lợi nhuận, đòn bẩy, thanh toán

> Bài học dựng từ **Phần V — Tỷ lệ: tìm hiểu ý nghĩa thật sự của các con số**: chương 19 *Sức mạnh của
> các con số tỷ lệ* (PDF tr. 142–147), chương 20 *Các tỷ lệ lợi nhuận* (PDF tr. 148–154), chương 21
> *Các tỷ lệ đòn bẩy* (PDF tr. 155–158), chương 22 *Các hệ số thanh toán* (PDF tr. 159–161).
> 🎯 **Vòng 1.** Bảy bài trước dựng **ba báo cáo**. Bài này bắt đầu **dùng** chúng — và chỉ ra rằng con
> số tuyệt đối không trả lời được câu hỏi nào cả.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) ·
> [Bài 4](bai_04_bang_can_doi_ke_toan.md) · [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) — mọi tỷ lệ
> ở đây lấy tử số từ bài 3 và mẫu số từ bài 4.
> ⚙️ **Code:** [`thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py`](../thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py)
> — sách đưa **công thức và một phép tính mẫu** cho từng tỷ lệ rồi dừng. File này làm phần sách để ngỏ:
> đo **độ nhạy**, tìm **ngưỡng**, và dựng lại bằng số những câu chuyện sách chỉ kể bằng lời.

---

## Mục lục

<!-- MUC-LUC -->

- [1. "So với cái gì kia?"](#1-so-với-cái-gì-kia)
- [2. Andrew Shore và DSO — tỷ lệ bắt được cái mà số tuyệt đối không bắt](#2-andrew-shore-và-dso--tỷ-lệ-bắt-được-cái-mà-số-tuyệt-đối-không-bắt)
- [3. Năm tỷ lệ lợi nhuận](#3-năm-tỷ-lệ-lợi-nhuận)
- [4. ROA có thể QUÁ CAO — dựng lại Enron](#4-roa-có-thể-quá-cao--dựng-lại-enron)
- [5. Công ty A và Công ty B — ROE cao hơn chỉ vì vay nhiều hơn](#5-công-ty-a-và-công-ty-b--roe-cao-hơn-chỉ-vì-vay-nhiều-hơn)
- [6. Hai loại đòn bẩy, và vì sao hãng hàng không chết](#6-hai-loại-đòn-bẩy-và-vì-sao-hãng-hàng-không-chết)
- [7. Hai tỷ lệ đòn bẩy, và giá của việc làm đẹp chúng](#7-hai-tỷ-lệ-đòn-bẩy-và-giá-của-việc-làm-đẹp-chúng)
- [8. Ba hệ số thanh toán — và cái "kiểm thử vàng" chưa đủ vàng](#8-ba-hệ-số-thanh-toán--và-cái-kiểm-thử-vàng-chưa-đủ-vàng)
- [9. ⚠️ Năm chỗ sách in sai trong Phần V](#9--năm-chỗ-sách-in-sai-trong-phần-v)
- [10. 🇻🇳 Đối chiếu Việt Nam](#10--đối-chiếu-việt-nam)
- [11. Tự thử](#11-tự-thử)
- [12. Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
- [13. Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. "So với cái gì kia?"

Chương 19 đặt toàn bộ Phần V lên một câu chuyện cười:

> *"Đối với một doanh nghiệp cụ thể, con số lợi nhuận thuần 10 triệu đô-la có phải là kết quả kinh doanh
> tốt không? **Ai mà biết được?** Nó tuỳ thuộc vào quy mô doanh nghiệp, vào lợi nhuận thuần trong năm
> trước đó và vào nhiều biến khác nữa. Nếu bạn hỏi liệu con số lợi nhuận 10 triệu đô-la là tốt hay tệ,
> câu trả lời duy nhất có lẽ là lời của một cô nàng trong một câu chuyện cười quen thuộc. Hỏi: 'Chồng cô
> thế nào?' Trả lời: **'So với cái gì kia?'**"* — ch. 19 · PDF tr. 146

Đó là một luận điểm **kiểm được**. Cho đúng một con số — lợi nhuận thuần **248** — đi qua bốn mẫu số:

| chia cho | mẫu số | ra tỷ lệ | giá trị |
| --- | ---: | --- | ---: |
| Doanh thu | 8.689 | biên lợi nhuận thuần | **2,85%** |
| Tổng tài sản | 5.193 | ROA | **4,78%** |
| Vốn chủ sở hữu | 2.457 | ROE | **10,09%** |
| Số cổ phiếu (triệu) | 74 | thu nhập trên cổ phần | **3,35 đô-la** |

⭐ Cùng một tử số, bốn câu trả lời khác hẳn nhau:

- so với **doanh thu** → 2,85%: **mỏng**. Mỗi đô-la bán được chỉ giữ lại gần ba xu.
- so với **vốn chủ** → 10,1%: **khá**. Cao hơn hẳn lãi trái phiếu 3–4%.
- so với **tài sản** → 4,8%: **tạm**. Nằm giữa hai con số trên.
- so với **cổ phiếu** → 3,35 đô-la: **chưa nói lên gì** khi chưa biết giá cổ phiếu — cần thêm một tỷ lệ
  nữa (giá/thu nhập).

Và đó là lý do tồn tại của cả Phần V:

> *"Mỗi công thức sẽ mở ra cho bạn **một góc nhìn khác** – giống như khi ta nhìn vào **một ngôi nhà qua
> những ô cửa ở cả bốn mặt**."* — ch. 19 · PDF tr. 147

📚 **Ba trục so sánh**, theo đúng thứ tự hữu dụng: ① với **chính nó theo thời gian** · ② với **dự kiến**
· ③ với **bình quân ngành**. Và một câu rào quan trọng: *"Hầu như sẽ có **một khoảng hợp lý**. **Chỉ khi**
tỷ lệ vượt ra khỏi khoảng đó, như tỷ lệ DSO của Sunbeam, thì nó mới đáng chú ý."*

📚 Bốn nhóm người, bốn tỷ lệ khác nhau: ngân hàng xem **nợ/vốn chủ**; quản lý cấp cao xem **biên gộp**;
giám đốc tín dụng xem **thanh toán nhanh** của khách hàng; cổ đông xem **giá/thu nhập**.

---

## 2. Andrew Shore và DSO — tỷ lệ bắt được cái mà số tuyệt đối không bắt

Sách kể câu chuyện này kỹ hơn nhiều so với lần nhắc ở Phần II.

Al Dunlap về Sunbeam đầu 1997 với "phương thức hành động chuẩn mực": sa thải đội quản lý, đóng cửa nhà
máy, cắt quân số **12.000 → 6.000**. Cổ phiếu tăng 50% ngay khi có tin ông ta được mời về. Rồi lên tiếp
— và **đó chính là rắc rối**:

> *"Khi các ngân hàng đầu tư quyết định bán công ty, giá công ty **cao đến độ họ khó xác định được đâu là
> khách hàng triển vọng**. Hi vọng duy nhất của Dunlap là đẩy doanh thu và thu nhập lên tới mức có thể
> biện minh cho mức giá cao."* — ch. 19 · PDF tr. 142–143

**Phát hoá đơn và giữ lại** (*bill-and-hold*) vốn là một kỹ thuật hợp pháp. Sách giải thích bằng ví dụ
sạch: chuỗi cửa hàng đồ chơi đặt búp bê Barbie từ mùa xuân, Mattel giao và xuất hoá đơn, nhưng chỉ thu
tiền khi Giáng sinh đến. **Cả hai bên đều lợi.**

Sunbeam bóp méo nó. Quý IV là lúc họ sản xuất hàng mùa hè — lò nướng gas. Họ đề nghị Wal-Mart và Kmart
đặt hàng từ **mùa đông**, xuất hoá đơn ngay, khách trả vào **mùa xuân** — và Sunbeam còn **thuê kho gần
cơ sở của khách và chịu mọi chi phí lưu kho**.

> *"Sunbeam đã chạy trước và ghi nhận thêm **36 triệu đô-la** doanh thu vào quý IV… Mánh khoé gian lận
> này phát huy tác dụng đến độ nó **dễ dàng qua mặt hầu hết các nhà phân tích, đầu tư và thậm chí cả ban
> giám đốc của Sunbeam**."* Đầu 1998 hội đồng quản trị thưởng Dunlap và ban điều hành gói cổ phiếu **38
> triệu đô-la** vì "một quý IV xuất sắc". — ch. 19 · PDF tr. 144

Andrew Shore, chuyên gia phân tích hàng tiêu dùng của Paine Webber, tính **DSO** và thấy nó *"quá lớn,
vượt xa mức thông thường"*. Ông gọi cho một kế toán viên của Sunbeam, biết được chiến lược bill-and-hold,
và **hạ điểm cổ phiếu ngay lập tức**.

**Sách dừng ở đó** — không nói bao nhiêu là "vượt xa". Dựng cơ chế ấy lên công ty mẫu. DSO hiện tại =
1.312 / (8.689/360) = **54,4 ngày**. Ghi thêm X doanh thu **chưa thu tiền** → cộng X vào cả doanh thu lẫn
phải thu:

| ghi thêm | % doanh thu | phải thu | doanh thu | DSO |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0,0% | 1.312 | 8.689 | 54,4 |
| 36 | 0,4% | 1.348 | 8.725 | 55,6 |
| **163** | **1,9%** | 1.475 | 8.852 | **60,0** |
| 400 | 4,6% | 1.712 | 9.089 | 67,8 |
| 869 | 10,0% | 2.181 | 9.558 | 82,1 |

⭐ Giả sử "khoảng hợp lý" của ngành là 45–60 ngày *(giả định của bài học để đo)*. Chỉ cần ghi thêm **163
triệu — 1,9% doanh thu — là DSO vượt 60 ngày.** Dưới hai phần trăm.

Đó là lý do Shore bắt được còn hội đồng quản trị của chính Sunbeam thì không: **họ nhìn con số tuyệt đối**
(doanh thu quý IV đẹp), **còn Shore nhìn tỷ lệ**.

💼 Dấu vết mà thủ thuật này không xoá được: doanh thu và phải thu cùng tăng, còn **tiền** thì không. Đúng
mẫu hình mà [bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) mục 9 đã chỉ ra ở phía nhà cung cấp.

---

## 3. Năm tỷ lệ lợi nhuận

Tiêu đề chương 20: ***"(Hầu hết) cao hơn thì tốt hơn"***. Hai chữ trong ngoặc là cả nội dung
[mục 4](#4-roa-có-thể-quá-cao--dựng-lại-enron).

Nhưng trước đó sách rào một câu quan trọng:

> *"Lợi nhuận được ghi nhận trên báo cáo kết quả kinh doanh là **sản phẩm của nghệ thuật tài chính**, và
> bất kỳ tỷ lệ nào được tính toán dựa trên những con số này cũng **tự nó phản ánh** tất cả những ước tính
> và giả định đó."* — ch. 20 · PDF tr. 148

| tỷ lệ | tử số | mẫu số | kết quả | công thức |
| --- | ---: | ---: | ---: | --- |
| Biên lợi nhuận gộp | 1.933 | 8.689 | **22,2%** | LN gộp / doanh thu |
| Biên lợi nhuận hoạt động | 652 | 8.689 | **7,5%** | EBIT / doanh thu |
| Biên lợi nhuận thuần | 248 | 8.689 | **2,9%** | LN thuần / doanh thu |
| ROA | 248 | **5.193** | **4,8%** | LN thuần / tổng tài sản |
| ROE | 248 | 2.457 | **10,1%** | LN thuần / vốn chủ sở hữu |

⭐ Ba con số đầu dùng **chung mẫu số** nên so sánh trực tiếp được — đó là ba tầng của
[bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md). Hai con số cuối **đổi mẫu số**, nên chúng trả lời
**câu hỏi khác**.

### Vì sao biên hoạt động mới là con số của nhà quản lý

> *"Các nhà quản lý không thuộc bộ phận tài chính **không có nhiều quyền kiểm soát** đối với những khoản
> mục mà cuối cùng sẽ được trừ đi để tính tỷ lệ lợi nhuận thuần, **như lãi vay và thuế**. Vì vậy, tỷ lệ
> lợi nhuận hoạt động là **một chỉ báo tốt cho biết hiệu quả làm việc của các nhà quản lý**."*
> — ch. 20 · PDF tr. 150

Lãi vay 191 + thuế 213 = **404 triệu**, tức **62% của EBIT**, biến mất ở những dòng mà không nhà quản lý
nào động đến được.

### ⚠️ IBM — doanh thu vượt kỳ vọng mà cổ phiếu vẫn rớt

> *"Trong một quý cách đây không lâu, IBM đã công bố con số doanh thu **khổng lồ** − lớn hơn nhiều so với
> dự đoán – **nhưng cổ phiếu của công ty lại giảm giá**. Tại sao? Các chuyên gia phân tích để ý thấy rằng
> tỷ lệ lợi nhuận gộp của công ty **đang lao đầu đi xuống**, và giả định IBM chắc hẳn đã **mạnh tay chiết
> khấu**."* — ch. 20 · PDF tr. 149

Xu hướng biên gộp đi xuống chỉ báo một trong hai, đôi khi cả hai: ① **áp lực giá** → nhân viên kinh doanh
phải chiết khấu; ② **chi phí lao động và nguyên vật liệu tăng** → COGS lên.

---

## 4. ROA có thể QUÁ CAO — dựng lại Enron

Đây là chỗ chương 20 khác hẳn mọi chương khác:

> *"Tỷ lệ lợi nhuận gộp hay tỷ lệ lợi nhuận thuần **rất khó đạt mức cao**; bạn thường muốn chúng đạt đến
> mức cao nhất có thể. **Nhưng ROA thì lại có thể quá cao.**"* — ch. 20 · PDF tr. 152

Sách nêu **hai** nguyên nhân. Nguyên nhân thứ hai có tên:

> *"**Enron** đã thành lập nhiều liên doanh thuộc sở hữu một phần của CFO **Andrew Fastow** và nhiều nhà
> điều hành khác, sau đó 'bán lại' tài sản cho các công ty đó. Cổ phần của công ty trong lợi nhuận của
> các liên doanh **xuất hiện trên báo cáo kết quả kinh doanh**, nhưng **tài sản thì không thể tìm thấy
> trên bảng cân đối kế toán**. ROA của Enron **rất cao**, nhưng Enron **không phải là doanh nghiệp có sức
> khoẻ ổn định**."* — ch. 20 · PDF tr. 152

Sách không đặt số. Đẩy tài sản ra khỏi bảng cân đối, giữ nguyên lợi nhuận:

| đẩy ra khỏi bảng | % tổng tài sản | tài sản còn lại | ROA | vòng quay TS |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0,0% | 5.193 | **4,8%** | 1,67 lần |
| 500 | 9,6% | 4.693 | 5,3% | 1,85 lần |
| 1.000 | 19,3% | 4.193 | 5,9% | 2,07 lần |
| 2.000 | 38,5% | 3.193 | 7,8% | 2,72 lần |
| **2.597** | **50,0%** | 2.596 | **9,6%** | 3,35 lần |

⭐ Đẩy **đúng một nửa** bảng cân đối ra ngoài thì ROA **gấp đôi**, từ 4,8% lên 9,6% — chốt bằng `assert`.
**Không một đồng doanh thu hay chi phí nào thay đổi.**

⚠️ **Và đây là chỗ nguy hiểm: cột cuối cùng tăng theo.** Vòng quay tổng tài sản là thước đo **hiệu suất**
— nó cao thì trông như doanh nghiệp đang dùng tài sản rất giỏi. Phân rã DuPont (bài 9) sẽ đọc cả hai cột
và kết luận *"hiệu suất tuyệt vời"*. **Cả hai đều bị lừa bởi cùng một bút toán.**

⭐ Nguyên nhân thứ nhất sách nêu còn âm thầm hơn Enron: ROA cao có thể chỉ là *"doanh nghiệp **không gia
cố tài sản** để dự phòng cho tương lai — tức là không đầu tư vào máy móc và thiết bị mới"*.
[Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) mục 6 đã đo điều đó trên chính công ty mẫu: capex 205 so
với khấu hao 239. **ROA của nó đẹp lên một phần vì thế.**

📚 **Vì sao ROI không có trong danh sách này?** Vì thuật ngữ có nhiều nghĩa: *"Trước đây, ROI và ROA là
một… Nhưng hiện nay, nó còn có thể có nghĩa là tỷ lệ hoàn vốn của **một khoản đầu tư cụ thể**."* → bài 10.

---

## 5. Công ty A và Công ty B — ROE cao hơn chỉ vì vay nhiều hơn

Sách đặt câu hỏi rồi bỏ đó:

> *"Công ty A có ROE cao hơn Công ty B **vì vay mượn nhiều tiền hơn** – tức là, công ty này có khoản nợ
> phải trả lớn hơn và tỷ lệ vốn chủ sở hữu được đầu tư vào công ty cũng thấp hơn tương ứng. **Điều này là
> tốt hay xấu?** Câu trả lời phụ thuộc vào việc liệu Công ty A đang **lao đầu vào rủi ro**, hay liệu,
> ngược lại, công ty đang **sử dụng số tiền vay mượn một cách khôn ngoan**."* — ch. 20 · PDF tr. 153

Trả lời bằng số. Hai công ty **giống hệt nhau về hoạt động** — tài sản 1.000, EBIT 150 — chỉ khác cơ cấu
vốn. Lãi suất 10%, thuế 40% *(các con số này là của bài học)*:

| nợ / tài sản | **NĂM BÌNH THƯỜNG** (EBIT 150)<br>ROA | ROE | **NĂM XẤU** (EBIT 50)<br>ROA | ROE |
| --- | ---: | ---: | ---: | ---: |
| 0% | 9,0% | **9,0%** | 3,0% | **3,0%** |
| 30% | 7,2% | 10,3% | 1,2% | 1,7% |
| 50% | 6,0% | 12,0% | 0,0% | 0,0% |
| 70% | 4,8% | 16,0% | −2,0% | −6,7% |
| 80% | 4,2% | **21,0%** | −3,0% | **−15,0%** |

⭐ **Năm bình thường:** đòn bẩy đẩy ROE từ 9,0% lên 21,0% — **gấp 2,3 lần**, trong khi doanh nghiệp không
đổi một li nào. Cột ROA thì đi **ngược lại**, vì tiền lãi ăn vào lợi nhuận.

⭐ **Năm xấu:** đúng cái đòn bẩy ấy kéo ROE từ 3,0% xuống **−15,0%**.

Đó là câu trả lời cho câu hỏi sách bỏ ngỏ: **đòn bẩy không tốt cũng không xấu, nó KHUẾCH ĐẠI.** Cùng một
hệ số, hai chiều.

### Và có một điểm xoay chính xác

Khi **EBIT = tài sản × lãi suất** = 100, mọi mức nợ đều cho **cùng một ROE** (6,0%) — chốt bằng `assert`:

| nợ | ROE |
| ---: | ---: |
| 0% | 6,0% |
| 50% | 6,0% |
| 80% | 6,0% |

**Trên** điểm đó vay nợ làm lợi; **dưới** điểm đó vay nợ làm hại. Cả câu chuyện "đòn bẩy" gọn trong một
phép so sánh: **doanh nghiệp kiếm được nhiều hơn hay ít hơn lãi suất nó phải trả?**

---

## 6. Hai loại đòn bẩy, và vì sao hãng hàng không chết

Chương 21 tách rõ hai khái niệm mà cả tiếng Việt lẫn tiếng Anh đều gọi chung một tên:

| | định nghĩa của sách | ví dụ |
| --- | --- | --- |
| **Đòn bẩy hoạt động** | *"tỷ lệ giữa chi phí cố định và chi phí biến đổi"* | nhà bán lẻ mở cửa hàng to hơn; nhà sản xuất xây nhà máy lớn hơn |
| **Đòn bẩy tài chính** | *"mức độ mà tài sản của doanh nghiệp được rót vốn mua sắm bằng nợ"* | vay ngân hàng để mua thiết bị |

> *"**Ngành hàng không** là một ví dụ về một doanh nghiệp có **đòn bẩy hoạt động cao** – tất cả những
> chiếc máy bay đó! – và **đòn bẩy tài chính cao**, bởi hầu hết các máy bay đều được rót vốn mua qua các
> khoản nợ. **Sự kết hợp này tạo ra rủi ro lớn**, bởi nếu vì một lý do nào đó mà doanh thu giảm, các
> doanh nghiệp **sẽ không thể dễ dàng cắt giảm chi phí cố định**."* — ch. 21 · PDF tr. 156

Đo độ lớn. Bốn doanh nghiệp, doanh thu 1.000, **EBIT đều bằng 100** *(cấu trúc chi phí là của bài học)*:

| đòn bẩy hoạt động | đòn bẩy tài chính | lợi nhuận gốc | **doanh thu giảm bao nhiêu thì về 0** |
| --- | --- | ---: | ---: |
| thấp | không nợ | 100 | **33,3%** |
| thấp | vay nhiều | 20 | 6,7% |
| cao | không nợ | 100 | 14,3% |
| **cao** | **vay nhiều** | 20 | **2,9%** |

⭐ Doanh nghiệp đòn bẩy **thấp + không nợ** chịu được doanh thu giảm **33%** rồi mới lỗ. Doanh nghiệp có
**cả hai** chỉ chịu được **2,9%**.

Đó là con số giải thích tháng 9/2001: *"Các hãng hàng không buộc phải **đóng cửa 1–2 tuần**, và chỉ trong
một thời gian ngắn, ngành hàng không **đã mất hàng tỷ đô-la**."* Một hai tuần đóng cửa là hơn 3% doanh
thu năm — **vừa đúng ngưỡng**.

⚠️ **Hai loại đòn bẩy không làm cùng một việc:**

- đòn bẩy **hoạt động** đổi **độ nhạy** — mỗi phần trăm doanh thu mất đi ăn sâu hơn;
- đòn bẩy **tài chính** đổi **mức nền** — nó trừ một số cố định, bất kể doanh thu.

Cộng lại thì điểm hoà vốn bị đẩy lên **sát mức doanh thu hiện tại**. Đó là lý do sách gọi chương này là
***"Tiết mục giữ thăng bằng"***.

📌 [Bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) mục 4 đã đo riêng đòn bẩy hoạt động trên một doanh
nghiệp sản xuất: tin rằng COGS là biến phí 100% làm dẹp bẹp độ nhạy 22,5%. Đây là nửa còn lại.

📚 Sách cũng nói rõ **nợ không phải điều xấu**: như vay thế chấp mua nhà, *"miễn là gia đình vay thế chấp
trong khả năng chi trả"*. Và lãi vay được **trừ khỏi thu nhập chịu thuế** — đó là lý do *"có nhiều, rất
nhiều doanh nghiệp có tỷ lệ nợ trên vốn chủ sở hữu cao hơn 1"*. Ngược lại, tỷ lệ **đặc biệt thấp** có thể
biến bạn thành mục tiêu của một cuộc **mua đứt có đòn bẩy**.

---

## 7. Hai tỷ lệ đòn bẩy, và giá của việc làm đẹp chúng

| | | |
| --- | --- | ---: |
| **Nợ trên vốn chủ sở hữu** | 2.736 / 2.457 | **1,11 lần** |
| **Hệ số thanh toán lãi vay** | 652 / 191 | **3,41 lần** |

> *"Nếu tỷ lệ này **tiến quá gần đến 1**, rõ ràng đây là dấu hiệu xấu: **hầu hết lợi nhuận của doanh
> nghiệp sẽ chỉ đủ để trả lãi vay!**"* — ch. 21 · PDF tr. 157

Rồi sách đặt câu hỏi thật: khi cả hai chệch hướng thì ban điều hành làm gì? Câu trả lời **không** phải
"trả bớt nợ":

> *"Các nghệ sĩ tài chính lại có quan điểm **hoàn toàn khác**. Chẳng hạn, họ sáng tạo ra một hình thức
> mới, rất tuyệt là **thuê tài sản hoạt động**… Việc trả tiền thuê sẽ được tính như **một khoản chi** trên
> báo cáo kết quả kinh doanh, nhưng **không có tài sản hay khoản nợ nào** liên quan đến tài khoản này
> trong sổ sách."* — ch. 21 · PDF tr. 158

**Đo giá của việc đó.** Muốn đưa nợ/vốn chủ từ 1,11 xuống 0,80:

| | triệu $ |
| --- | ---: |
| nợ phải trả hiện tại | 2.736 |
| nợ mục tiêu (0,80 × vốn chủ) | 1.966 |
| **→ phải đưa ra khỏi bảng** | **770** |

Lãi suất vay hiện tại = 191/1.714 = **11,1%/năm**, nên bỏ 770 nợ thì bớt **86** lãi mỗi năm. Nhưng phải
**trả tiền thuê** cho đúng 770 thiết bị ấy:

| phí thuê/năm | trả tiền thuê | lãi đã bớt | **đắt thêm** |
| ---: | ---: | ---: | ---: |
| 12% | 92 | 86 | **7** |
| 14% | 108 | 86 | **22** |
| 16% | 123 | 86 | **37** |

⭐ Tỷ lệ trông đẹp hơn, nhưng doanh nghiệp **trả thêm tiền thật mỗi năm** để mua cái vẻ đẹp đó. Sách nói
thẳng: *"Một số doanh nghiệp sử dụng đòn bẩy quá mức **sẵn lòng chi mạnh tay** để thuê thiết bị **chỉ với
mục đích** giữ hai tỷ lệ này nằm trong khoảng mà các ngân hàng và nhà đầu tư ưa thích."*

### ⚠️ Chỗ này sách đã cũ

Kể từ **IFRS 16** (hiệu lực 2019) và **ASC 842** ở Mỹ, gần như **mọi** hợp đồng thuê đều phải lên bảng cân
đối thành *"quyền sử dụng tài sản"* và một khoản nợ thuê tương ứng. **Lỗ hổng mà chương 21 mô tả về cơ bản
đã bị bịt.**

Nhưng **lời khuyên** của sách thì còn nguyên giá trị: *"hãy **hỏi thêm phòng tài chính**, liệu công ty có
dùng bất kỳ **công cụ nào giống nợ** như hợp đồng thuê tài sản hoạt động không."* Chỉ là ngày nay câu hỏi
đổi thành: **còn công cụ nào khác đang nằm ngoài bảng không?**

---

## 8. Ba hệ số thanh toán — và cái "kiểm thử vàng" chưa đủ vàng

Sách cho hai hệ số. Chúng khác nhau ở **đúng một dòng** — trừ tồn kho ra:

| hệ số | tử số | mẫu số | kết quả |
| --- | ---: | ---: | ---: |
| Thanh toán ngắn hạn | 2.750 | 1.174 | **2,34 lần** |
| Thanh toán nhanh *(kiểm thử vàng)* | 1.480 | 1.174 | **1,26 lần** |
| 💼 Tiền / nợ ngắn hạn | 83 | 1.174 | **0,07 lần** |

> *"Gần như **mọi khoản mục khác** trong hạng mục tài sản ngắn hạn hoặc là tiền mặt, hoặc **có thể dễ dàng
> chuyển thành tiền mặt**. Chẳng hạn, hầu hết các khoản phải thu sẽ được thanh toán **trong vòng 1–2
> tháng**, vì vậy **chúng chẳng kém gì tiền mặt**."* — ch. 22 · PDF tr. 160

⚠️ **Kiểm lại chính câu đó trên số liệu của sách:** DSO = 54,4 ngày = **1,8 tháng**. Vừa khớp mép trên của
"1–2 tháng" — **nhưng vừa khớp thôi**. Nếu DSO trôi lên 90 ngày thì câu *"chẳng kém gì tiền mặt"* không
còn đúng, mà **hệ số thanh toán nhanh vẫn không đổi**. Nó không nhìn thấy DSO.

⭐ Nên dòng thứ ba đáng thêm vào. Công ty mẫu có **83 triệu** tiền mặt, trong khi chi phí hoạt động bằng
tiền là **21,71 triệu mỗi ngày**:

> 83 / 21,71 = **3,8 ngày** chi tiêu

*(nếu không thu được đồng nào — một giả định khắc nghiệt và cố ý như thế)*

⭐ **Ba hệ số, ba bức tranh:** 2,34 lần trông **rất an toàn**; 1,26 lần trông **ổn**; 0,07 lần trông **đáng
lo**. Chúng không mâu thuẫn — chúng trả lời ba câu hỏi khác nhau về **ba khung thời gian** khác nhau.

💼 Sách cũng cảnh báo đầu kia: hệ số thanh toán ngắn hạn *"**quá cao** khi nó cho các cổ đông thấy rằng
doanh nghiệp **đang ngồi trên đống tiền mặt** của mình"*. **Microsoft** tích gần **60 tỷ đô-la**, đến 2004
mới *"tuyên bố trả **cổ tức một lần là 32 tỷ đô-la** cho các cổ đông"*. **Tỷ lệ cao không phải lúc nào
cũng là lời khen.**

⚠️ Còn đầu thấp thì dứt khoát: *"Thấp hơn 1, tất nhiên, là mức quá thấp… bạn hiểu rõ, mình sẽ **sớm hết
tiền** vào một thời điểm nào đó trong năm tới."* Và *"hầu hết các ngân hàng sẽ **không duyệt** đơn vay vốn
của một doanh nghiệp có hệ số thanh toán ngắn hạn gần bằng 1."*

---

## 9. ⚠️ Năm chỗ sách in sai trong Phần V

Phần V in một **ô công thức** cho từng tỷ lệ. Các ô đó có nhiều lỗi hơn phần chữ.

| chỗ | sách in | đúng ra |
| --- | --- | --- |
| tr. 144 | *"khoản **phải trả** của công ty đã phá tung trần"* | **phải thu** — DSO đo khoản phải thu, không đo phải trả |
| tr. 150 | nhãn ô công thức: *"Lợi nhuận **gộp** (EBIT)"* | EBIT là lợi nhuận **hoạt động**. Chính đoạn văn ngay trên đó nói đúng |
| tr. 152 | ROA = 248 / **8.689** | mẫu số đó là **doanh thu**. Phải là tổng tài sản **5.193** *(kết quả 4,8% thì vẫn đúng)* |
| tr. 156 | nhãn ô công thức: *"Tỷ lệ **lợi nhuận** trên vốn chủ sở hữu"* | tiêu đề mục ngay trên là *"**TỶ LỆ NỢ** TRÊN VỐN CHỦ SỞ HỮU"* |
| tr. 156 | *"= 1,11**%**"* | có dấu %, trong khi **câu ngay sau đó** viết tỷ lệ này *"không thường được biểu diễn dưới dạng tỷ lệ phần trăm"* |

⭐ **Bốn trong năm chỗ là lỗi NHÃN, không phải lỗi số** — một lớp khác hẳn với các lỗi số mà
[bài 0](bai_00_bat_dau_tu_dau.md) đo được. Chúng không làm phép tính sai, nhưng chúng **dạy người đọc gọi
tên sai cho công thức** — và đó mới là thứ cần nhớ lâu.

⚠️ Còn một chỗ nữa ở ranh giới: tr. 151 in biên lợi nhuận thuần là **2,8%**, trong khi 248/8.689 =
**2,854%**, làm tròn đúng phải là **2,9%**. Cắt chữ số thay vì làm tròn. Nhỏ, nhưng cả khoá học này dùng
**2,9%**.

---

## 10. 🇻🇳 Đối chiếu Việt Nam

Cùng chín công thức, hai doanh nghiệp cách nhau 19 năm và một đại dương:

| | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| --- | ---: | ---: |
| Biên lợi nhuận gộp | 22,2% | 28,8% |
| Biên lợi nhuận hoạt động | 7,5% | 18,4% |
| Biên lợi nhuận thuần | 2,9% | 16,5% |
| ROA | 4,8% | 15,2% |
| ROE | 10,1% | 23,4% |
| Nợ trên vốn chủ sở hữu | 1,11 lần | 0,53 lần |
| **Hệ số thanh toán lãi vay** | **3,41 lần** | **30,28 lần** |
| Hệ số thanh toán ngắn hạn | 2,34 lần | 2,03 lần |
| Hệ số thanh toán nhanh | 1,26 lần | 1,72 lần |

⭐ Chỗ lệch nhiều nhất là **hệ số thanh toán lãi vay**: 3,4 so với 30,3. Sách nói tỷ lệ *"tiến quá gần đến
1"* là dấu hiệu xấu — 3,4 thì không nguy, nhưng **30 thì là một hạng khác hẳn**: Vinamilk gần như không
vay để vận hành.

⭐ **Và đó là lý do ROE của hai bên gần nhau hơn ROA rất nhiều:**

| | công ty mẫu | Vinamilk | chênh |
| --- | ---: | ---: | ---: |
| ROA | 4,8% | 15,2% | **3,2 lần** |
| ROE | 10,1% | 23,4% | **2,3 lần** |

Công ty mẫu dùng **đòn bẩy** để kéo ROE lên gần Vinamilk, dù hoạt động kém hơn hẳn. Đó đúng là cơ chế của
[mục 5](#5-công-ty-a-và-công-ty-b--roe-cao-hơn-chỉ-vì-vay-nhiều-hơn), gặp ngoài đời thực — chốt bằng
`assert`.

📚 **Ba lưu ý khi tính các tỷ lệ này trên báo cáo Việt Nam:**

- **Không có dòng EBIT.** Như [bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) mục 12 đã nêu, *"lợi nhuận
  thuần từ hoạt động kinh doanh"* của VAS đã trừ chi phí tài chính. Muốn tính **biên hoạt động** và **hệ
  số thanh toán lãi vay** thì phải dựng lại EBIT — mẫu số lãi vay cũng phải lấy từ thuyết minh.
- **"Nợ phải trả" của VAS gồm cả khoản không chịu lãi.** Tỷ lệ nợ/vốn chủ tính theo tổng nợ (như sách) sẽ
  khác hẳn tính theo **nợ vay có lãi**. Chốt trước dùng cái nào.
- **Tồn kho ghi theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được.** Điều này ảnh
  hưởng cả **hệ số thanh toán ngắn hạn** lẫn **hệ số thanh toán nhanh** — và là một trong những lý do hai
  hệ số đó của Vinamilk gần nhau hơn của công ty mẫu.

---

## 11. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py`](../thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py)
rồi chạy lại. Không có lời giải.

1. **Mẫu số thứ năm.** Ở mục 1, thêm một mẫu số nữa mà bạn thấy có ý nghĩa. Nó trả lời câu hỏi gì mà bốn
   cái kia không trả lời?

2. **Shore ở doanh nghiệp thu tiền nhanh.** Ở mục 2, thử với doanh nghiệp có DSO gốc chỉ **20 ngày**. Cần
   ghi thêm bao nhiêu phần trăm doanh thu để DSO vượt 60? Doanh nghiệp nào **dễ giấu** hơn?

3. **Ngưỡng hẹp hơn.** Vẫn mục 2, đổi "khoảng hợp lý" thành 50–58 ngày. Ngưỡng phát hiện dịch bao nhiêu?
   Điều này nói gì về giá trị của việc **biết chuẩn ngành**?

4. **ROA gấp ba.** Ở mục 4, tìm số tài sản phải đẩy ra khỏi bảng để ROA **gấp ba**. Nó bằng bao nhiêu phần
   trăm bảng cân đối? Ở mức nào thì con số trở nên không thể giấu?

5. **Enron nhìn từ vòng quay.** Vẫn mục 4: nếu bạn chỉ được xem **một** trong hai cột (ROA hay vòng quay
   tài sản), cột nào giúp bạn nghi ngờ sớm hơn? Vì sao cả hai cùng tăng lại là **dấu hiệu** chứ không phải
   sự trùng hợp?

6. **Đòn bẩy ở lãi suất cao.** Ở mục 5, đổi lãi suất từ 10% lên **15%**. Điểm xoay dịch đến đâu? Ở mức nợ
   80%, ROE năm bình thường còn cao hơn công ty không nợ không?

7. **Năm rất xấu.** Vẫn mục 5, đặt EBIT năm xấu bằng **0**. ROE ở từng mức nợ là bao nhiêu? Mức nợ nào
   làm vốn chủ sở hữu bốc hơi nhanh nhất?

8. **Hãng hàng không sau khủng hoảng.** Ở mục 6, giả sử hãng bán bớt máy bay để hạ chi phí cố định từ 600
   xuống **400** nhưng chi phí biến đổi tăng lên 45% doanh thu. Nó chịu được doanh thu giảm bao nhiêu?
   Đánh đổi này có đáng không?

9. **Thuê ở lãi suất thấp.** Ở mục 7, nếu doanh nghiệp vay được với **6%** thay vì 11,1%, phí thuê phải
   bao nhiêu mới hoà vốn? Vì sao doanh nghiệp **vay rẻ** ít có động cơ dùng thủ thuật này?

10. **Bao nhiêu ngày là đủ.** Ở mục 8, tìm mức tiền mặt để công ty mẫu trụ được **30 ngày** không thu được
    đồng nào. Nó bằng bao nhiêu phần trăm tài sản ngắn hạn? Hệ số thanh toán nhanh khi đó là bao nhiêu?

---

## 12. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Tỷ lệ | ratio | *"mối tương quan giữa các con số"* — chia hai số cho nhau |
| Biên lợi nhuận gộp | gross margin | lợi nhuận gộp / doanh thu |
| Biên lợi nhuận hoạt động | operating margin | EBIT / doanh thu — **con số của nhà quản lý** |
| Biên lợi nhuận thuần | net margin / ROS | lợi nhuận thuần / doanh thu |
| ROA | return on assets | lợi nhuận thuần / **tổng tài sản** — có thể **quá cao** |
| ROE | return on equity | lợi nhuận thuần / vốn chủ sở hữu |
| ROI | return on investment | *"thuật ngữ này có nhiều ý nghĩa khác nhau"* → bài 10 |
| Đòn bẩy hoạt động | operating leverage | tỷ lệ chi phí **cố định** / chi phí **biến đổi** — đổi **độ nhạy** |
| Đòn bẩy tài chính | financial leverage | mức độ tài sản được mua bằng **nợ** — đổi **mức nền** |
| Nợ trên vốn chủ sở hữu | debt-to-equity | tổng nợ / vốn chủ sở hữu. **Không** biểu diễn bằng % |
| Hệ số thanh toán lãi vay | interest coverage | EBIT / lãi vay hằng năm. Gần 1 = xấu |
| Hệ số thanh toán ngắn hạn | current ratio | tài sản ngắn hạn / nợ ngắn hạn |
| Hệ số thanh toán nhanh | quick ratio / acid test | *(TSNH − tồn kho)* / nợ ngắn hạn — **kiểm thử vàng** |
| Kỳ thu tiền bình quân | days sales outstanding (DSO) | phải thu / doanh thu mỗi ngày — tỷ lệ lật tẩy Sunbeam |
| Phát hoá đơn và giữ lại | bill-and-hold | ghi doanh thu, hàng còn ở kho người bán |
| Thuê tài sản hoạt động | operating lease | thuê thay vì mua — **trước 2019** không lên bảng cân đối |
| Mua đứt có đòn bẩy | leveraged buyout | vay tiền để mua cổ phiếu doanh nghiệp |
| 💼 Tiền / nợ ngắn hạn | cash ratio | hệ số khắc nghiệt nhất — **không có trong sách** |

---

## 13. Câu hỏi tự kiểm tra

1. Kể câu chuyện cười mà chương 19 dùng làm luận điểm. Nó nói gì về con số tuyệt đối? (mục 1)
2. Cho lợi nhuận thuần 248 đi qua bốn mẫu số — bốn kết quả là gì? (mục 1)
3. Sách ví bốn công thức với hình ảnh nào? (mục 1)
4. Kể ba trục so sánh, và câu rào quan trọng về "khoảng hợp lý". (mục 1)
5. Bốn nhóm người dùng bốn tỷ lệ nào? (mục 1)
6. **Phát hoá đơn và giữ lại** hợp pháp là gì? Kể ví dụ Barbie. (mục 2)
7. Sunbeam bóp méo nó thế nào? Ba chi tiết cụ thể. (mục 2)
8. Bao nhiêu doanh thu được ghi thêm vào quý IV? Hội đồng quản trị thưởng Dunlap bao nhiêu? (mục 2)
9. Andrew Shore tính tỷ lệ nào? Ông làm gì tiếp theo? (mục 2)
10. Cần ghi thêm bao nhiêu phần trăm doanh thu để DSO của công ty mẫu vượt 60 ngày? (mục 2)
11. Vì sao Shore bắt được mà hội đồng quản trị Sunbeam thì không? (mục 2)
12. Tiêu đề chương 20 là gì? Hai chữ trong ngoặc chỉ điều gì? (mục 3)
13. Kể năm tỷ lệ lợi nhuận và công thức từng cái. (mục 3)
14. Ba tỷ lệ nào so sánh trực tiếp được với nhau? Vì sao? (mục 3)
15. Vì sao **biên hoạt động** mới là con số của nhà quản lý? Bao nhiêu phần trăm EBIT nằm ngoài tầm với
    của họ? (mục 3)
16. IBM công bố doanh thu vượt kỳ vọng mà cổ phiếu vẫn rớt — vì sao? (mục 3)
17. Xu hướng biên gộp đi xuống chỉ báo hai điều gì? (mục 3)
18. Vì sao ROA có thể **quá cao**? Nêu **hai** nguyên nhân sách đưa ra. (mục 4)
19. Enron làm gì với tài sản? Ai đứng tên các liên doanh? (mục 4)
20. Đẩy bao nhiêu tài sản ra khỏi bảng thì ROA gấp đôi? (mục 4)
21. Vì sao **vòng quay tài sản** tăng theo lại nguy hiểm? (mục 4)
22. Vì sao ROI không nằm trong danh sách năm tỷ lệ? (mục 4)
23. Công ty A có ROE cao hơn Công ty B vì vay nhiều hơn. Tốt hay xấu? (mục 5)
24. Ở mức nợ 80%, ROE năm bình thường và năm xấu lần lượt là bao nhiêu? (mục 5)
25. Viết điểm xoay của đòn bẩy bằng một công thức. Trên và dưới nó thì sao? (mục 5)
26. Phân biệt **đòn bẩy hoạt động** và **đòn bẩy tài chính**. Mỗi cái đổi thứ gì? (mục 6)
27. Vì sao ngành hàng không có cả hai đều cao? (mục 6)
28. Doanh nghiệp có cả hai chịu được doanh thu giảm bao nhiêu phần trăm? Liên hệ 11/9/2001. (mục 6)
29. Sách nói gì về việc nợ **không** phải điều xấu? Kể hai lý do. (mục 6)
30. Nợ trên vốn chủ **đặc biệt thấp** có thể dẫn tới rủi ro gì? (mục 6)
31. Hệ số thanh toán lãi vay tiến gần đến 1 nghĩa là gì? (mục 7)
32. Khi hai tỷ lệ đòn bẩy chệch hướng, "nghệ sĩ tài chính" làm gì? (mục 7)
33. Để đưa nợ/vốn chủ từ 1,11 xuống 0,80 phải đưa bao nhiêu ra khỏi bảng? Đắt thêm bao nhiêu mỗi năm ở
    phí thuê 14%? (mục 7)
34. IFRS 16 và ASC 842 đã thay đổi điều gì? Lời khuyên nào của sách vẫn còn giá trị? (mục 7)
35. Hai hệ số thanh toán khác nhau ở đúng cái gì? Vì sao trừ tồn kho? (mục 8)
36. Kiểm câu *"phải thu chẳng kém gì tiền mặt"* trên số liệu của sách — nó đúng ở mức nào? (mục 8)
37. Công ty mẫu trụ được bao nhiêu ngày bằng tiền mặt nếu không thu được đồng nào? (mục 8)
38. Hệ số thanh toán ngắn hạn **quá cao** nghĩa là gì? Microsoft đã làm gì năm 2004? (mục 8)
39. Kể năm chỗ sách in sai trong Phần V. Bốn trong số đó thuộc loại lỗi gì? (mục 9)
40. Chỗ lệch nhiều nhất giữa công ty mẫu và Vinamilk là tỷ lệ nào? Nó nói lên điều gì? (mục 10)
41. Vì sao ROE của hai bên gần nhau hơn ROA? (mục 10)
42. Kể ba lưu ý khi tính các tỷ lệ này trên báo cáo Việt Nam. (mục 10)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 8 — TỶ LỆ LỢI NHUẬN, ĐÒN BẨY, THANH TOÁN                            ║
║           (ch. 19–22, PDF tr. 142–161)                                   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⭐ "CHỒNG CÔ THẾ NÀO?" — "SO VỚI CÁI GÌ KIA?"                           ║
║     cùng một số 248, bốn câu trả lời:                                    ║
║       / doanh thu   2,85%  mỏng   ·  / tài sản  4,78%  tạm               ║
║       / vốn chủ    10,09%  khá    ·  / cổ phiếu  3,35 $  chưa nói gì     ║
║     "mỗi công thức mở ra MỘT GÓC NHÌN KHÁC — như nhìn MỘT NGÔI NHÀ       ║
║      QUA NHỮNG Ô CỬA Ở CẢ BỐN MẶT"                                       ║
║                                                                          ║
║  ⭐ ANDREW SHORE LẬT TẨY SUNBEAM BẰNG ĐÚNG MỘT TỶ LỆ                     ║
║     Dunlap cắt 12.000 → 6.000 người; bill-and-hold bơm 36 TRIỆU vào Q4;  ║
║     hội đồng thưởng ông ta 38 TRIỆU cổ phiếu.                            ║
║     Shore tính DSO → thấy vượt khoảng bình thường → hạ điểm.             ║
║     Trên công ty mẫu: ghi thêm 1,9% DOANH THU là DSO vượt 60 ngày.       ║
║     → hội đồng nhìn SỐ TUYỆT ĐỐI, Shore nhìn TỶ LỆ.                      ║
║                                                                          ║
║  NĂM TỶ LỆ LỢI NHUẬN:  22,2% → 7,5% → 2,9%  (chung mẫu số)               ║
║                        ROA 4,8%  ·  ROE 10,1%  (đổi mẫu số)              ║
║     biên HOẠT ĐỘNG là con số của nhà quản lý: lãi vay + thuế = 404       ║
║     = 62% EBIT, nằm ngoài tầm với của họ.                                ║
║     IBM: doanh thu vượt kỳ vọng mà cổ phiếu RỚT — biên gộp lao dốc.      ║
║                                                                          ║
║  ⭐ ROA CÓ THỂ QUÁ CAO — và đó là điều duy nhất trong nhóm này           ║
║     đẩy 2.597 (MỘT NỬA bảng cân đối) ra ngoài → ROA GẤP ĐÔI 4,8→9,6%     ║
║     mà không một đồng doanh thu nào đổi. Enron / Andrew Fastow.          ║
║     ⚠️ VÒNG QUAY TÀI SẢN CŨNG TĂNG THEO → DuPont (bài 9) cũng bị lừa     ║
║        bởi CÙNG MỘT bút toán.                                            ║
║                                                                          ║
║  ⭐ ĐÒN BẨY KHÔNG TỐT CŨNG KHÔNG XẤU — NÓ KHUẾCH ĐẠI                     ║
║     cùng doanh nghiệp, chỉ đổi cơ cấu vốn:                               ║
║        nợ 0%  → ROE  9,0% (năm thường)   3,0% (năm xấu)                  ║
║        nợ 80% → ROE 21,0%              −15,0%                            ║
║     ĐIỂM XOAY: khi EBIT = tài sản × lãi suất, mọi mức nợ cho CÙNG ROE.   ║
║     Trên nó vay LÀM LỢI, dưới nó vay LÀM HẠI.                            ║
║                                                                          ║
║  ⭐ HAI LOẠI ĐÒN BẨY — hoạt động đổi ĐỘ NHẠY, tài chính đổi MỨC NỀN      ║
║     doanh thu giảm bao nhiêu thì về 0:                                   ║
║        thấp + không nợ  33,3%   ·   cao + không nợ  14,3%                ║
║        thấp + vay nhiều  6,7%   ·   CAO + VAY NHIỀU  2,9%  ← hàng không  ║
║     11/9/2001: đóng cửa 1–2 tuần ≈ hơn 3% doanh thu năm. Vừa đúng.       ║
║                                                                          ║
║  ⭐ GIÁ CỦA VIỆC LÀM ĐẸP TỶ LỆ                                           ║
║     đưa nợ/vốn chủ 1,11 → 0,80 cần bỏ 770 ra khỏi bảng                   ║
║     thuê ở 14%: trả 108 thay vì 86 lãi → ĐẮT THÊM 22 TRIỆU/NĂM           ║
║     ⚠️ IFRS 16 / ASC 842 (2019) đã BỊT lỗ hổng này. Lời khuyên còn:      ║
║        "công ty có dùng công cụ nào GIỐNG NỢ không?"                     ║
║                                                                          ║
║  ⭐ BA HỆ SỐ THANH TOÁN, BA BỨC TRANH                                    ║
║     ngắn hạn 2,34 RẤT AN TOÀN · nhanh 1,26 ỔN · tiền 0,07 ĐÁNG LO        ║
║     83 triệu tiền / 21,71 mỗi ngày = 3,8 NGÀY chi tiêu                   ║
║     ⚠️ "phải thu chẳng kém gì tiền mặt" — DSO 1,8 tháng, VỪA KHỚP thôi.  ║
║        Quick ratio KHÔNG NHÌN THẤY DSO.                                  ║
║     Microsoft: 60 tỷ tiền mặt → cổ tức một lần 32 tỷ (2004).             ║
║                                                                          ║
║  ⚠️ NĂM CHỖ SÁCH IN SAI TRONG PHẦN V — BỐN LÀ LỖI NHÃN:                  ║
║     tr.144 "phải trả" → phải THU  ·  tr.150 "LN gộp (EBIT)" → hoạt động  ║
║     tr.152 ROA mẫu số 8.689 → 5.193                                      ║
║     tr.156 "lợi nhuận trên vốn chủ" → NỢ  ·  "1,11%" → bỏ dấu %          ║
║                                                                          ║
║  🇻🇳 thanh toán lãi vay 3,41 vs 30,28 — Vinamilk gần như không vay.       ║
║     ROA chênh 3,2 lần nhưng ROE chỉ chênh 2,3 lần: công ty mẫu dùng      ║
║     ĐÒN BẨY kéo ROE lên, dù hoạt động kém hơn hẳn. Mục 5 ngoài đời.      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần V — Tỷ lệ: tìm hiểu ý nghĩa thật sự của các con số**, PDF tr. 141–161.
    - Ch. 19 *Sức mạnh của các con số tỷ lệ*, PDF tr. 142–147
      — ⭐ **Al Dunlap về Sunbeam**, cắt 12.000 → 6.000, cổ phiếu tăng 50% (tr. 142); **phát hoá đơn và
      giữ lại** — ví dụ Barbie/Mattel và cách Sunbeam bóp méo với Wal-Mart, Kmart (tr. 143–144);
      **36 triệu doanh thu**, gói thưởng **38 triệu** (tr. 144); ⭐ **Andrew Shore và DSO** (tr. 144–145);
      **phân tích tỷ lệ** — bóng chày, xổ số, bốn nhóm người dùng (tr. 145); ⭐ *"So với cái gì kia?"*
      (tr. 146); **ba trục so sánh** và *"khoảng hợp lý"* (tr. 146–147); **bốn nhóm tỷ lệ** và
      *"ngôi nhà qua những ô cửa ở cả bốn mặt"* (tr. 147)
    - Ch. 20 *Các tỷ lệ lợi nhuận*, PDF tr. 148–154
      — *"(Hầu hết) cao hơn thì tốt hơn"* và cảnh báo về nghệ thuật tài chính (tr. 148); **biên lợi nhuận
      gộp** và **IBM** (tr. 148–149); **biên lợi nhuận hoạt động** và lý do nó là con số của nhà quản lý
      (tr. 149–150); **biên lợi nhuận thuần / ROS** (tr. 150–151); **ROA** (tr. 151–152); ⭐ **ROA có thể
      quá cao** và **Enron / Andrew Fastow** (tr. 152); hộp **ROI** (tr. 153); **ROE** và ⭐ **Công ty A
      vs Công ty B** (tr. 153–154); cảnh báo đóng chương (tr. 154)
    - Ch. 21 *Các tỷ lệ đòn bẩy*, PDF tr. 155–158
      — *"Tiết mục giữ thăng bằng"*, nợ và ẩn dụ vay thế chấp mua nhà (tr. 155); ⭐ **đòn bẩy hoạt động vs
      đòn bẩy tài chính** (tr. 155–156); ⭐ **ngành hàng không** và **11/9/2001** (tr. 156); **nợ trên vốn
      chủ sở hữu** và **mua đứt có đòn bẩy** (tr. 156–157); **hệ số thanh toán lãi vay** (tr. 157); ⭐
      **thuê tài sản hoạt động** và lời khuyên hỏi phòng tài chính (tr. 158)
    - Ch. 22 *Các hệ số thanh toán*, PDF tr. 159–161
      — hệ số thanh toán và ngành hàng không sau 2001 (tr. 159); **hệ số thanh toán ngắn hạn** (tr. 159);
      quá thấp / quá cao và **Microsoft 60 tỷ → cổ tức 32 tỷ năm 2004** (tr. 160); **hệ số thanh toán
      nhanh** — *"công cụ kiểm thử vàng"* và lý do trừ tồn kho (tr. 160–161)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mọi mục
- **IFRS 16 *Leases*** (IASB, hiệu lực 01/01/2019) và **ASC 842 *Leases*** (FASB, hiệu lực 2019 với công
  ty đại chúng Mỹ) — đưa hợp đồng thuê lên bảng cân đối. Nhắc ở
  [mục 7](#7-hai-tỷ-lệ-đòn-bẩy-và-giá-của-việc-làm-đẹp-chúng).
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 10](#10--đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py`](../thuc_hanh/bai-08-ty-le-loi-nhuan-don-bay-thanh-toan.py):
  - ngưỡng bill-and-hold: mức ghi thêm làm DSO chạm đúng 60 ngày **dưới 2% doanh thu** — chốt bằng `assert`;
  - Enron: đẩy 2.597 ra khỏi bảng làm ROA **gấp đúng hai lần** — chốt bằng `assert`;
  - đòn bẩy: ROE ở nợ 80% **hơn gấp đôi** ROE ở nợ 0% trong năm thường, và **thấp hơn** trong năm xấu —
    chốt bằng `assert`;
  - **điểm xoay**: khi EBIT = tài sản × lãi suất, mọi mức nợ cho ROE **bằng đúng** *(1 − thuế) × lãi suất*
    — chốt bằng `assert`;
  - hãng hàng không: thứ tự sức chịu đựng **cao+vay < cao+không nợ < thấp+không nợ**, và trường hợp xấu
    nhất **dưới 5%** — chốt bằng `assert`;
  - DSO của công ty mẫu nằm **trong khoảng 1–2 tháng** mà sách khẳng định — chốt bằng `assert`;
  - biên lợi nhuận thuần làm tròn đúng là **2,9%**, không phải 2,8% như sách in — chốt bằng `assert`;
  - Vinamilk: **chênh lệch ROA lớn hơn chênh lệch ROE** — bằng chứng công ty mẫu đang dùng đòn bẩy —
    chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** khoảng hợp lý 45–60 ngày ở mục 2; các mức đẩy tài
  sản ở mục 4; toàn bộ tham số hai công ty (1.000 / 150 / 10% / 40%) ở mục 5; cấu trúc chi phí bốn doanh
  nghiệp ở mục 6; mục tiêu nợ/vốn chủ 0,80 và dải phí thuê 12–16% ở mục 7; hệ số **tiền / nợ ngắn hạn** và
  cách quy chi phí tiền mặt mỗi ngày ở mục 8. Mọi con số **của sách** đều được trích kèm mốc
  `ch. N · PDF tr. M`.

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
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| **8** | **Tỷ lệ lợi nhuận, đòn bẩy, thanh toán** ← *bạn đang ở đây* | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
