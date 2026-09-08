# Bài 4 — Bảng cân đối kế toán

> Bài học dựng từ **Phần III — Bảng cân đối kế toán, nơi vén mở nhiều điều nhất**: chương 9 *Hiểu
> những điều căn bản về bảng cân đối kế toán* (PDF tr. 75–80), chương 10 *Tài sản* (PDF tr. 81–91),
> chương 11 *Phía bên kia* (PDF tr. 92–96).
> 🎯 **Vòng 1.** Bài 2 và 3 đã đi hết báo cáo kết quả kinh doanh. Bài này chuyển sang báo cáo mà
> **chuyên gia đọc trước** — và cho thấy mọi ước tính của hai bài trước cuối cùng đều đổ vào đây.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) ·
> [Bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) — mục 5 của bài 3 (khấu hao) là đầu vào trực tiếp
> của mục 7 bài này.
> ⚙️ **Code:** [`thuc_hanh/bai-04-bang-can-doi-ke-toan.py`](../thuc_hanh/bai-04-bang-can-doi-ke-toan.py)

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vì sao chuyên gia đọc bảng này trước, còn nhà quản lý thì không](#1-vì-sao-chuyên-gia-đọc-bảng-này-trước-còn-nhà-quản-lý-thì-không)
- [2. Phương trình kế toán cơ bản](#2-phương-trình-kế-toán-cơ-bản)
- [3. GPA — lợi nhuận là điểm số, vốn chủ sở hữu là điểm trung bình](#3-gpa--lợi-nhuận-là-điểm-số-vốn-chủ-sở-hữu-là-điểm-trung-bình)
- [4. Cột tài sản — đi từ trên xuống](#4-cột-tài-sản--đi-từ-trên-xuống)
- [5. Dự phòng nợ xấu — ước tính rẻ nhất để đổi EPS](#5-dự-phòng-nợ-xấu--ước-tính-rẻ-nhất-để-đổi-eps)
- [6. Chi phí lịch sử — mảnh đất Los Angeles](#6-chi-phí-lịch-sử--mảnh-đất-los-angeles)
- [7. Khấu hao luỹ kế — chiếc xe tải của bài 3 đi sang bảng cân đối](#7-khấu-hao-luỹ-kế--chiếc-xe-tải-của-bài-3-đi-sang-bảng-cân-đối)
- [8. Lợi thế thương mại — MJQ Storage và động cơ định giá thấp](#8-lợi-thế-thương-mại--mjq-storage-và-động-cơ-định-giá-thấp)
- [9. Tyco — bóc lợi thế thương mại ra thì còn gì](#9-tyco--bóc-lợi-thế-thương-mại-ra-thì-còn-gì)
- [10. Tài sản trả trước — chiến dịch quảng cáo](#10-tài-sản-trả-trước--chiến-dịch-quảng-cáo)
- [11. Phía bên kia — nợ phải trả và vốn chủ sở hữu](#11-phía-bên-kia--nợ-phải-trả-và-vốn-chủ-sở-hữu)
- [12. Giá trị sổ sách không bao giờ là giá trị thị trường](#12-giá-trị-sổ-sách-không-bao-giờ-là-giá-trị-thị-trường)
- [13. 🇻🇳 Đối chiếu Việt Nam](#13--đối-chiếu-việt-nam)
- [14. Tự thử](#14-tự-thử)
- [15. Từ điển thuật ngữ](#15-từ-điển-thuật-ngữ)
- [16. Câu hỏi tự kiểm tra](#16-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vì sao chuyên gia đọc bảng này trước, còn nhà quản lý thì không

Chương 9 mở bằng một quan sát về hành vi, không phải về kế toán:

> *"Nếu trao cho một nhà quản lý giàu kinh nghiệm một tập tài liệu tài chính, thì thứ đầu tiên mà
> ông ta sẽ tìm đến là **báo cáo kết quả kinh doanh**… Bây giờ, ta hãy thử đưa tập tài liệu tài chính
> tương tự cho một chuyên viên ngân hàng, hay một nhà đầu tư có kinh nghiệm ở Phố Wall, hay một thành
> viên kỳ cựu có chân trong hội đồng quản trị. Báo cáo đầu tiên mà những người này luôn tìm xem sẽ là
> **bảng cân đối kế toán**. Thực tế là họ sẽ **săm soi nó một lúc lâu**. Sau đó, họ mới bắt đầu lật
> giở các trang khác… **nhưng họ luôn trở lại bảng cân đối kế toán**."* — ch. 9 · PDF tr. 75

Sách đưa ba lý do cho khoảng cách đó:

| # | lý do | hệ quả |
| ---: | --- | --- |
| 1 | *"Bảng cân đối kế toán có phần hơi khó hiểu"*; báo cáo KQKD *"dù gì cũng khá trực quan"* | người ta né cái khó |
| 2 | Ngân sách được lập theo **doanh thu và chi phí** — tức theo báo cáo KQKD. *"Các dữ liệu trên bảng cân đối kế toán hiếm khi có trong bảng dự toán của vị giám đốc điều hành"* | nhà quản lý **không được giao chỉ tiêu** trên bảng này |
| 3 | Kiểm soát nó *"đòi hỏi những hiểu biết tài chính sâu hơn… không chỉ buộc phải hiểu các hạng mục khác nhau cho thấy điều gì, mà còn phải biết **chúng phù hợp với nhau như thế nào**"* | phải hiểu cả ba báo cáo cùng lúc |

Lý do 2 là lý do thật, và nó có tính hệ thống: **bạn không đo cái mà không ai giao chỉ tiêu cho bạn.**
Còn người cho vay tiền thì đo đúng cái đó.

---

## 2. Phương trình kế toán cơ bản

Sách xây khái niệm từ một cá nhân trước khi sang doanh nghiệp:

> *"Cộng tất cả những gì sở hữu, rồi trừ đi mọi khoản nợ, và bạn sẽ thu được giá trị thuần của người
> đó:* **có − nợ = giá trị thuần** *… Một cách phát biểu khác cho công thức trên là:*
> **có = nợ + giá trị thuần**"* — ch. 9 · PDF tr. 77–78

Sang doanh nghiệp thì chỉ đổi tên:

| cá nhân | doanh nghiệp |
| --- | --- |
| những gì **có** | **tài sản** |
| những gì **nợ** | **nợ phải trả** |
| **giá trị thuần** | **vốn chủ sở hữu** (hay vốn cổ đông) |

> **Tài sản − nợ phải trả = vốn chủ sở hữu**, hay **tài sản = nợ phải trả + vốn chủ sở hữu**
> — *"phương trình kế toán cơ bản"* · ch. 9 · PDF tr. 78

Trên công ty mẫu, ngày 31/12/2005 (triệu đô-la):

| | | % tổng tài sản |
| --- | ---: | ---: |
| **TÀI SẢN** | **5.193** | 100,0% |
| · tài sản ngắn hạn | 2.750 | 53,0% |
| · tài sản dài hạn | 2.443 | 47,0% |
| **NỢ PHẢI TRẢ** | **2.736** | 52,7% |
| **VỐN CHỦ SỞ HỮU** | **2.457** | 47,3% |
| **NỢ + VỐN CHỦ** | **5.193** | 100,0% |

Hai bên bằng nhau. Sách hứa sẽ giải thích vì sao trước khi hết Phần III — đó là
[bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md).

⚠️ **Khác biệt lớn nhất so với báo cáo kết quả kinh doanh: bảng này có một NGÀY trên đầu, không phải
một khoảng thời gian.** Sách nói rõ nó là *"một báo cáo về những gì doanh nghiệp có và nợ **tại một
thời điểm cụ thể**"* (PDF tr. 76). Báo cáo KQKD là đoạn phim; bảng cân đối là ảnh chụp.

📚 Hai chi tiết kỹ thuật đáng nhớ:

- **Bảng cân đối gần như luôn lập cho toàn bộ tổ chức**, hiếm khi cho từng cơ sở (PDF tr. 79). Nên
  đừng đi tìm bảng cân đối cho phòng ban của bạn — nó thường không tồn tại.
- **Năm tài khoá** (*fiscal year*) không nhất thiết trùng năm dương lịch. *"Một số nhà bán lẻ dùng một
  ngày cuối tuần cụ thể, chẳng hạn như ngày Chủ nhật cuối cùng trong năm"* (PDF tr. 79–80). Không biết
  năm tài khoá thì không biết con số đang cập nhật đến đâu.

---

## 3. GPA — lợi nhuận là điểm số, vốn chủ sở hữu là điểm trung bình

Đây là phép so sánh hay nhất của cả chương, và nó trả lời câu hỏi *"hai báo cáo nối với nhau thế nào"*:

> *"Khả năng sinh lời giống như **điểm số** mà bạn nhận được sau khoá học ở trường đại học… Vốn chủ sở
> hữu giống như **tổng điểm trung bình (GPA)**. GPA luôn phản ánh kết quả học tập tích luỹ của bạn,
> nhưng chỉ tại một thời điểm nhất định. **Bất kỳ một điểm số nào cũng ảnh hưởng đến nó, nhưng không
> thể quyết định được nó.**"* — ch. 9 · PDF tr. 77

Cơ chế nối là dòng **lợi nhuận giữ lại**:

| | triệu đô-la |
| --- | ---: |
| vốn chủ sở hữu 31/12/2004 | 2.375 |
| + lợi nhuận thuần cả năm 2005 | 248 |
| − cổ tức đã trả | −166 |
| **= vốn chủ sở hữu 31/12/2005** | **2.457** |

**Sách không đo câu "không quyết định được".** Đo thử: cả một năm kinh doanh dịch được **82 triệu**,
tức **3,45%** vốn chủ sở hữu đầu kỳ. Muốn **gấp đôi** vốn chủ sở hữu với nhịp độ này thì cần **30 năm**.

⭐ Đó là ý nghĩa định lượng của câu trích: **bảng cân đối là tích luỹ của nhiều năm, còn báo cáo KQKD
chỉ là một năm.** Một năm tệ hại không giết được bảng cân đối; một năm rực rỡ cũng không cứu được nó.

💼 Ba con số đi kèm, và tích của hai con số cuối:

| | |
| --- | ---: |
| ROE (lợi nhuận thuần / vốn chủ sở hữu) | 10,1% |
| tỷ lệ chia cổ tức | 66,9% |
| tỷ lệ giữ lại | 33,1% |
| **10,1% × 33,1% =** | **3,34%** |

Con số cuối là **tốc độ tăng trưởng tự thân** — mức tăng công ty tự nuôi được, không cần gọi thêm vốn.
*(Cụm từ này không có trong sách.)* Muốn tăng nhanh hơn thì phải vay, phát hành thêm cổ phiếu, hoặc
cắt cổ tức. Không có đường thứ tư. Nó cũng gần như trùng đúng con số 3,45% tính ở trên — đó không phải
trùng hợp, mà là cùng một phép tính nhìn từ hai phía.

---

## 4. Cột tài sản — đi từ trên xuống

> **Tài sản ngắn hạn** (*current asset*): *"bao gồm bất kỳ thứ gì có thể chuyển đổi thành tiền mặt
> trong thời gian lâu nhất là **một năm**."* **Tài sản dài hạn**: *"tuổi đời sử dụng lâu hơn một năm."*
> — ch. 10 · PDF tr. 81

### Tiền — dòng duy nhất không phải ước tính

> *"Đây là một trong số ít những khoản mục **không phụ thuộc vào quyền tự quyết của kế toán viên**.
> Khi Microsoft cho biết mình có 56 tỷ đô-la… thì điều đó có nghĩa là họ **thật sự có chừng đó tiền**."*
> — ch. 10 · PDF tr. 81

Chú ý tiêu đề phụ mà sách đặt cho cả chương 10: *"Thêm các ước tính và giả định **(Trừ tiền mặt)**"*.
Toàn bộ chương là danh sách những dòng **có thể tranh cãi được**, và tiền là ngoại lệ duy nhất.

⚠️ Ngoại lệ của ngoại lệ: *"Dĩ nhiên, các doanh nghiệp cũng có thể **khai khống**. Công ty **Parmalat**
khổng lồ của Ý đã báo cáo khống trên bảng cân đối kế toán rằng họ có hàng tỷ đô-la trong một tài khoản
ở Ngân hàng Mỹ."* Không thể ước tính sai một con số tiền mặt — chỉ có thể bịa nó.

### Các khoản phải thu (A/R)

> *"Đây là số tiền mà khách hàng nợ doanh nghiệp… Nó giống như một khoản mà doanh nghiệp **cho khách
> hàng vay** − và doanh nghiệp sở hữu các khoản nợ phải trả của khách hàng."* — ch. 10 · PDF tr. 81–82

Trừ vào đó là **dự phòng nợ xấu** — mục 5 dành riêng cho dòng này.

### Hàng tồn kho

Ba loại: **thành phẩm**, **hàng đang sản xuất** (WIP — *work-in-process*), và **nguyên vật liệu thô**.
Sách cố tình bỏ qua tranh luận định giá — *"Kế toán viên có thể (và quả thật!) dành nhiều ngày nói
không dứt về những cách thức định giá hàng tồn kho"* — nhưng vẫn cảnh báo rằng *"các phương thức định
giá hàng tồn kho khác nhau có thể làm **thay đổi đáng kể** phía tài sản của bảng cân đối kế toán"* và
mọi thay đổi phương pháp **phải ghi trong chú thích** (PDF tr. 83).

Sách trích nguyên văn chú thích của **Barnes & Noble**, báo cáo thường niên 2004, làm ví dụ cho việc
một doanh nghiệp trình bày tỉ mỉ đến đâu: **92%** hàng tồn kho theo FIFO tính đến 29/01/2005 và **90%**
tính đến 31/01/2004, phần còn lại theo LIFO.

Điều duy nhất sách yêu cầu nhà quản lý nhớ:

> *"Tất cả hàng tồn kho đều **tốn kém**… Nếu các yếu tố khác không đổi, việc **giảm lượng hàng tồn kho
> sẽ giúp bạn nâng mức tiền mặt** của công ty mình."* — ch. 10 · PDF tr. 83

📌 Đây là hạt giống của [bài 6](bai_06_loi_nhuan_khac_tien_mat.md) và bài 11.

---

## 5. Dự phòng nợ xấu — ước tính rẻ nhất để đổi EPS

Sách mô tả cơ chế bằng lời, rất rõ:

> *"Khi **tăng** khoản dự phòng nợ xấu trên bảng cân đối kế toán, bạn sẽ phải ghi nhận một khoản phải
> chi trừ vào lợi nhuận trên báo cáo kết quả kinh doanh. Việc làm này **làm giảm** con số thu nhập…
> Tương tự như vậy, nếu bạn **kê giảm** khoản dự phòng nợ xấu, thì điều chỉnh này sẽ **làm tăng lợi
> nhuận**… Vì khoản dự phòng nợ xấu **luôn là ước tính**, nên ở đây luôn có chỗ cho phán đoán chủ
> quan."* — ch. 10 · PDF tr. 82

Khoản phải thu của công ty mẫu là **1.312 triệu** đô-la; EPS đang là 3,35 đô-la:

| chỉnh dự phòng | ảnh hưởng trước thuế | sau thuế | đổi EPS |
| --- | ---: | ---: | ---: |
| +0,1 điểm | −1,31 | −0,71 | −0,010 $ |
| +0,5 điểm | −6,56 | −3,53 | −0,048 $ |
| +1,0 điểm | −13,12 | −7,06 | −0,095 $ |
| +2,0 điểm | −26,24 | −14,12 | −0,191 $ |

⭐ Đi ngược lại: muốn EPS đổi **đúng một xu**, chỉ cần chỉnh dự phòng nợ xấu **0,105 điểm phần trăm**
của khoản phải thu — tức **1,38 triệu** đô-la trên 1.312 triệu. Không kiểm toán viên nào bác bỏ nổi
một con số nhỏ như thế.

⭐ **Đối chiếu với [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) mục 6:** ở đó, một xu EPS cần **1,38
triệu đô-la doanh thu ghi thêm** — tức một hợp đồng có thật, một khách hàng có thật. Ở đây nó chỉ cần
một con số ước tính nhích 0,105 điểm. **Cùng một kết quả; một bên cần khách hàng, một bên chỉ cần một
ý kiến.**

📚 Sách giải thích vì sao doanh nghiệp muốn **"chuốt"** thu nhập chứ không phải bơm nó:

> *"Bạn ắt sẽ cho rằng Phố Wall thích những cú hích lớn trong lợi nhuận… Nhưng nếu cú hích ấy xảy đến
> **ngoài dự đoán và khó lý giải**… thì các nhà đầu tư nhiều khả năng sẽ phản ứng **tiêu cực**, xem đó
> như một dấu hiệu cảnh báo rằng ban quản lý **mất khả năng kiểm soát** tình hình của doanh nghiệp."*
> — ch. 10 · PDF tr. 82

Mục tiêu không phải một đường **cao**. Mục tiêu là một đường **thẳng**.

---

## 6. Chi phí lịch sử — mảnh đất Los Angeles

**PPE** (*Property, Plant, and Equipment* — đất đai, nhà xưởng và thiết bị) được ghi theo **giá mua**,
không phải giá thị trường. Sách đưa hai lý do:

1. **Không ai biết giá thị trường.** *"Nếu không đánh giá liên tục, sẽ không ai thực sự biết bất động
   sản và thiết bị của doanh nghiệp có giá bao nhiêu trên thị trường mở."* Nên kế toán viên, *"vốn bị
   chi phối bởi các nguyên tắc thận trọng"*, nói: *"Cứ sử dụng những gì chúng ta biết rõ."*
2. **Để chặn một cửa gian lận.** Đánh giá tăng giá trị đất đòi phải ghi nhận một khoản lợi nhuận —
   *"nhưng khoản lợi nhuận đó sẽ không chỉ đơn thuần dựa trên **ý kiến của một ai đó**… Đó không phải
   là một ý hay."* Và sách nêu tên: **Enron** dựng các vỏ bọc do chính lãnh đạo sở hữu rồi bán tài sản
   cho chúng, để ghi nhận lợi nhuận *"cứ như thể họ đã thực sự bán các tài sản"* (PDF tr. 84).

Cái giá của sự thận trọng đó:

> *"Bạn làm việc cho một công ty giải trí 30 năm trước mua được một số đất đai quanh thành phố Los
> Angeles với giá **500.000 đô-la**. Đến nay số đất đai đó có thể trị giá **5 triệu đô-la** − nhưng nó
> sẽ **vẫn được định giá là 500.000 đô-la** trên bảng cân đối kế toán."* — ch. 10 · PDF tr. 84

| tăng giá mỗi năm | giá trị sau 30 năm | sổ sách giấu đi |
| --- | ---: | ---: |
| 3%/năm | 1.213.631 | 58,8% |
| 5%/năm | 2.160.971 | 76,9% |
| **8%/năm** | **5.031.328** | **90,1%** |
| 10%/năm | 8.724.701 | 94,3% |

⭐ Con số 5 triệu của sách ứng với mức tăng **8,0%/năm** — không hề kỳ lạ với bất động sản đô thị.
Nhưng bảng cân đối đang giấu đi **90%** giá trị. Sách nói đó là cơ hội: *"Các nhà đầu tư sành sỏi thích
sục sạo quanh bảng cân đối kế toán của doanh nghiệp, với hi vọng tìm thấy những **tài sản bị định giá
thấp** kiểu như thế."*

💼 **Cái bóng ngược lại mà sách không nói:** tài sản bị ghi thấp thì **mẫu số của ROA cũng thấp**, nên
ROA trông đẹp hơn thực tế.

| PPE thật sự đáng giá | tổng tài sản | ROA |
| --- | ---: | ---: |
| 1,0 lần sổ sách *(như công bố)* | 5.193 | **4,78%** |
| 1,5 lần sổ sách | 6.308 | 3,93% |
| 2,0 lần sổ sách | 7.423 | 3,34% |
| 3,0 lần sổ sách | 9.653 | **2,57%** |

⚠️ ROA công bố 4,78%; nếu PPE đáng giá gấp ba lần sổ sách thì ROA thật chỉ 2,57% — chênh **1,86 lần**.
*(Bội số 1,5–3,0 là giả định của bài học để đo độ nhạy; sách không nêu.)* **Doanh nghiệp càng lâu đời,
tài sản càng cũ, thì ROA công bố càng dễ gây hiểu lầm** — điều cần nhớ khi đến
[bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) và bài 9.

---

## 7. Khấu hao luỹ kế — chiếc xe tải của bài 3 đi sang bảng cân đối

Đây là chỗ hai bài nối liền, và sách nói thẳng ra:

> *"Trong chương trước, chúng tôi đã chỉ cho các bạn thấy cách thức một doanh nghiệp có thể 'hô biến'
> từ không có lợi nhuận thành có lợi nhuận, chỉ bằng việc thay đổi phương thức khấu hao tài sản. **Trò
> ảo thuật nghệ-thuật-tài-chính này đã lan cả sang bảng cân đối kế toán.** Nếu một doanh nghiệp quyết
> định đội xe tải của mình có thể hoạt động đến tận sáu năm thay vì ba năm… khoản khấu hao luỹ kế trên
> bảng cân đối kế toán sẽ giảm, PPE thuần sẽ cao hơn, và do vậy **tài sản của doanh nghiệp sẽ nhiều
> hơn**. Và theo phương trình kế toán cơ bản, **nhiều tài sản hơn đồng nghĩa với việc nhiều vốn chủ sở
> hữu hơn**."* — ch. 10 · PDF tr. 85

Sách không đặt số. Lấy đúng chiếc xe tải 36.000 đô-la của bài 3:

| tháng | KH luỹ kế 3 năm | KH luỹ kế 6 năm | chênh PPE thuần |
| ---: | ---: | ---: | ---: |
| 12 | 12.000 | 6.000 | 6.000 |
| 24 | 24.000 | 12.000 | 12.000 |
| **36** | **36.000** | **18.000** | **18.000** |
| 48 | 36.000 | 24.000 | 12.000 |
| 72 | 36.000 | 36.000 | **0** |

⭐ Ở tháng 36, hai bảng cân đối lệch nhau **18.000 đô-la**, và toàn bộ khoản lệch ấy nằm ở **vốn chủ sở
hữu**. Cùng một chiếc xe, cùng một số tiền đã chi, hai "giá trị sổ sách" cách nhau 18.000. Đẳng thức
được chốt bằng `assert` ở mọi mốc tháng:

> **Δ tài sản = Δ vốn chủ sở hữu = Δ khấu hao luỹ kế**

Và ở tháng 72 thì cả hai về 0: chênh lệch **biến mất**. Nó chỉ là vay mượn thời gian — đúng mẫu hình
của bài 2 và bài 3.

⚠️ Con số 18.000 là **trước thuế**; sách bỏ qua thuế ở chỗ này. Lợi nhuận cao hơn thì thuế cũng cao
hơn: với thuế suất 46,2%, 18.000 lợi nhuận thêm kéo theo **8.317** thuế, nên vốn chủ sở hữu thật sự chỉ
tăng **9.683**, phần còn lại thành một khoản **nợ thuế**. Bảng cân đối vẫn cân — chỉ là cân ở chỗ khác.

---

## 8. Lợi thế thương mại — MJQ Storage và động cơ định giá thấp

> **Lợi thế thương mại** (*goodwill*): *"con số chênh lệch giữa **giá mua** doanh nghiệp và **giá trị
> tài sản thuần** mà bên mua nhận được."* — ch. 10 · PDF tr. 85

Ví dụ của sách — bạn mua MJQ Storage:

| | đô-la |
| --- | ---: |
| giá mua | 5.000.000 |
| − tài sản hữu hình thuần *(công trình, kệ hàng, xe nâng, máy tính, sau khi trừ nợ)* | −2.000.000 |
| **= lợi thế thương mại** | **3.000.000** |

Sách nói rõ 3 triệu đó không phải tiền vứt đi: *"Bạn đang mua một doanh nghiệp hoạt động, có tên tuổi,
danh sách khách hàng, những nhân viên tài năng… **Bạn sẽ trả bao nhiêu để có thể sở hữu thương hiệu
Coca-Cola? Hay danh sách khách hàng của hãng Dell?**"* (PDF tr. 86).

### Quy tắc đã đổi, và động cơ đổi theo

| | lợi thế thương mại | tài sản khác |
| --- | --- | --- |
| **quy tắc cũ** | khấu hao, **tối đa 40 năm** | thường 2–5 năm |
| **quy tắc mới** (FASB) | **không khấu hao** — *"giống đất đai hơn là trang thiết bị"* | không đổi |

Sách kết luận bằng lời:

> *"Bạn có động cơ tìm mua các doanh nghiệp, mà trong đó thứ được mua chủ yếu là lợi thế thương mại, và
> bạn có động cơ để **định giá thấp tài sản vật chất** của doanh nghiệp định mua. (Đừng quên, **chính
> bạn và người của mình là người định giá cho những tài sản ấy!**)… Giờ thì thậm chí bạn còn có **động
> cơ lớn hơn**… và **động cơ lớn hơn nữa** cho việc định giá thấp các tài sản ấy."*
> — ch. 10 · PDF tr. 88

Đo độ lớn của động cơ đó. Khấu hao hữu hình 4 năm, lợi thế thương mại 30 năm, chi phí mỗi năm:

| định giá hữu hình | QUY TẮC CŨ<br>(LTTM 30 năm) | QUY TẮC MỚI<br>(LTTM không KH) | mới bớt được |
| --- | ---: | ---: | ---: |
| 2.000.000 *(thẩm định trung thực)* | 600.000 | 500.000 | 100.000 |
| 1.500.000 | 491.667 | 375.000 | 116.667 |
| 1.000.000 | 383.333 | 250.000 | 133.333 |
| 500.000 | 275.000 | 125.000 | 150.000 |

⭐ Hạ định giá hữu hình từ 2 triệu xuống 1 triệu — **chỉ bằng một ý kiến thẩm định**:

- quy tắc **cũ** tiết kiệm **216.667** đô-la chi phí mỗi năm;
- quy tắc **mới** tiết kiệm **250.000** đô-la mỗi năm.

Quy tắc mới làm động cơ **mạnh hơn** — đúng như sách nói, và điều đó được chốt bằng `assert`.

⚠️ Riêng việc đổi quy tắc, không động đến một con số thẩm định nào, đã bớt **100.000** đô-la chi phí
mỗi năm.

---

## 9. Tyco — bóc lợi thế thương mại ra thì còn gì

> *"Trong riêng hai năm liên tiếp, năm 2000 và 2001, Tyco đã tiến hành mua lại với tốc độ chóng mặt −
> **hơn 600 công ty**. Nhiều nhà phân tích nhận thấy Tyco thường xuyên **định giá thấp tài sản** của
> những công ty mua lại. Việc làm này gia tăng lợi thế thương mại của tất cả các giao dịch mua lại, và
> **làm giảm khoản khấu hao** mà Tyco phải chịu mỗi năm. Đến lượt, điều này khiến lợi nhuận tăng thêm
> và **đẩy giá cổ phiếu của Tyco lên cao**."* — ch. 10 · PDF tr. 88

Rồi câu chốt:

> *"…nếu bạn **gạt lợi thế thương mại ra khỏi** phương trình của bảng cân đối kế toán, thì các khoản nợ
> của công ty **thực chất lại lớn hơn tài sản**."* — ch. 10 · PDF tr. 88

Sách không đưa số. Dựng cơ chế ấy lên công ty mẫu: mỗi thương vụ 200 triệu, trả bằng tiền vay, 80% giá
mua thành lợi thế thương mại *(các tham số này là của bài học)*:

| số thương vụ | tổng tài sản | LTTM | LTTM/TS | LTTM/vốn chủ | vốn chủ sau khi bóc |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 5.193 | 0 | 0,0% | 0,00 lần | 2.457 |
| 5 | 6.193 | 800 | 12,9% | 0,33 lần | 1.657 |
| 10 | 7.193 | 1.600 | 22,2% | 0,65 lần | 857 |
| 15 | 8.193 | 2.400 | 29,3% | 0,98 lần | 57 |
| **16** | 8.393 | 2.560 | 30,5% | **1,04 lần** | **−103** |
| 20 | 9.193 | 3.200 | 34,8% | 1,30 lần | −743 |

⭐ Vốn chủ sở hữu **âm từ thương vụ thứ 16** — đúng lúc lợi thế thương mại vượt vốn chủ sở hữu. Toàn bộ
cảnh báo của sách viết được thành một tỷ lệ đọc trong ba giây:

> **lợi thế thương mại / vốn chủ sở hữu > 1**

⚠️ Chú ý cột **LTTM/TS**: ở thương vụ thứ 16 nó mới là **30,5%** tổng tài sản. Nhìn cột đó thì không
thấy gì đáng sợ. Tỷ lệ nguy hiểm là tỷ lệ với **vốn chủ sở hữu**, không phải với tổng tài sản — vì lợi
thế thương mại bị xoá thì nó ăn thẳng vào vốn chủ, không ăn vào nợ phải trả.

💼 Công ty mẫu không có đồng lợi thế thương mại nào nên an toàn tuyệt đối ở phép thử này. Nhưng với bất
kỳ doanh nghiệp nào lớn lên bằng **mua lại**, đây là dòng đầu tiên cần tìm trên bảng cân đối của họ.

📚 **Sở hữu trí tuệ và R&D** có cùng cấu trúc rủi ro. GAAP cho phép vốn hoá chi phí R&D *"nếu sản phẩm
phát triển **khả thi về mặt công nghệ**"* — nhưng sách hỏi ngay: *"**ai sẽ xác định** tính khả thi công
nghệ đó?"* Vốn hoá thì lợi nhuận đẹp hơn; ghi thẳng vào chi phí là *"cách tiếp cận thận trọng hơn"*.
**Computer Associates** *"đã tự chuốc lấy rắc rối khi khấu hao chi phí R&D của những sản phẩm không có
tương lai chắc chắn"* (PDF tr. 89).

---

## 10. Tài sản trả trước — chiến dịch quảng cáo

Ví dụ dẫn nhập của sách rất sạch: công ty sản xuất xe đạp trả trước **60.000 đô-la** tiền thuê mặt bằng
cả năm. Nguyên tắc phù hợp buộc ghi 5.000/tháng vào báo cáo KQKD. *"Vậy 55.000 đô-la còn lại sẽ đi
đâu? **Bạn phải theo dõi nó ở đâu đó.**"* — và chỗ đó là dòng **tài sản trả trước** trên bảng cân đối
(PDF tr. 89–90).

Nhưng ví dụ đắt hơn là cái thứ hai — chiến dịch quảng cáo 1 triệu đô-la hoàn tất tháng Một:

| | GHI HẾT THÁNG MỘT | RẢI 1/24 MỖI THÁNG |
| --- | ---: | ---: |
| chi phí tháng 1 | −1.000.000 | −41.667 |
| chi phí tháng 2 | 0 | −41.667 |
| chi phí tháng 24 | 0 | −41.667 |
| *tài sản trả trước cuối tháng 1* | *0* | *958.333* |
| *tài sản trả trước cuối tháng 12* | *0* | *500.000* |
| *tài sản trả trước cuối tháng 24* | *0* | *0* |
| **TỔNG CHI PHÍ 24 THÁNG** | **−1.000.000** | **−1.000.000** |

⭐ Lại là mẫu hình của bài 2 và bài 3: **tổng bằng nhau, chỉ khác chỗ đặt vào tháng nào**. Cái mới ở
đây là khoản chưa ghi nhận **phải nằm ở đâu đó** — và chỗ đó là bảng cân đối. **Báo cáo KQKD và bảng
cân đối là hai đầu của cùng một bút toán.**

⚠️ Sách chỉ thẳng ra động cơ, và nó phụ thuộc vào… tháng đó làm ăn thế nào:

- tháng Một **khó khăn** → *"trừ dần 1/24 của 1 triệu đô-la khỏi lợi nhuận vẫn tốt hơn là trừ một lần
  cả 1 triệu đô-la"*;
- tháng Một **tuyệt vời** → *"'ghi chi phí' của cả chiến dịch… vì, thì đấy, **họ không biết chắc** chiến
  dịch có giúp tạo ra doanh thu trong hai năm tới không."*

Cùng một chiến dịch, cùng một hoá đơn. Chỉ khác kết quả tháng đó.

---

## 11. Phía bên kia — nợ phải trả và vốn chủ sở hữu

Chương 11 mở bằng một cách đọc lại rất đáng giá:

> *"Có một cách khác − chỉ đôi chút − để đọc phần này của bảng cân đối kế toán, đó là phần này cho ta
> thấy **các tài sản đã được thu về như thế nào**. Nếu một doanh nghiệp vay vốn… thì khoản vốn vay sẽ
> được thể hiện trên một dòng nợ phải trả. Nếu doanh nghiệp bán cổ phiếu để mua tài sản, thực tế này sẽ
> được phản ánh trên một dòng thuộc hạng mục vốn chủ sở hữu."* — ch. 11 · PDF tr. 92

Đọc lại 5.193 triệu tài sản của công ty mẫu theo câu hỏi **"ai trả tiền"**:

| nguồn | triệu đô-la | % tổng tài sản |
| --- | ---: | ---: |
| Nhà cung cấp (khoản phải trả) | 1.022 | 19,7% |
| Ngân hàng — hạn mức + nợ đến hạn | 152 | 2,9% |
| Chủ nợ dài hạn | 1.562 | 30,1% |
| Cổ đông góp vốn | 1.184 | 22,8% |
| Lợi nhuận giữ lại qua các năm | 1.273 | 24,5% |
| **TỔNG** | **5.193** | **100,0%** |

⭐ Hai chỗ đáng đọc lại:

- **Nhà cung cấp đang tài trợ 19,7% tổng tài sản — và không tính lãi.** Sách: *"Doanh nghiệp nhận hàng
  hoá và dịch vụ từ các nhà cung cấp mỗi ngày, và chỉ thanh toán hoá đơn sau 30 ngày. **Thực chất, các
  nhà cung cấp đã cho doanh nghiệp vay nợ.**"* (PDF tr. 93). Bài 11 sẽ đo kỹ dòng này.
- Trong 2.457 vốn chủ sở hữu, **cổ đông chỉ thực sự bỏ ra 1.184**; 1.273 còn lại (**51,8%**) là lợi
  nhuận chính công ty tự kiếm qua các năm.

📚 Các dòng còn lại, gọn:

| dòng | ý chính | trích |
| --- | --- | --- |
| **Khoản phải trả của nợ dài hạn** | vay 100.000, năm nay đến hạn 10.000 → 10.000 vào **nợ ngắn hạn**, 90.000 ở dài hạn | ch. 11 · PDF tr. 92 |
| **Vay ngắn hạn** | hạn mức tín dụng, *"thường được bảo đảm bằng các tài sản ngắn hạn như khoản phải thu và hàng tồn kho"* | PDF tr. 92 |
| **Nợ trả trước** | lương trả 1/10 cho việc làm trong tháng Chín → ghi vào tháng Chín. *"Giống như một hoá đơn nội bộ của tháng Chín được thanh toán vào tháng Mười"* | PDF tr. 93 |
| **Nợ dài hạn** | vay, cộng thưởng trả chậm, **thuế trả chậm**, **nợ tiền lương hưu**. *"Nếu những khoản này lớn, ta cần theo dõi sát sao"* | PDF tr. 93 |
| **Cổ phiếu ưu đãi** | cổ tức **cố định**, thường **không có quyền biểu quyết** — *"giống trái phiếu hơn là cổ phiếu phổ thông"* | PDF tr. 94 |
| **Cổ phiếu phổ thông** | có quyền biểu quyết; ghi theo **mệnh giá** — *"một khoản tiền rất nhỏ và **không liên quan đến giá thị trường**"*. Công ty mẫu: mệnh giá 1 đô-la | PDF tr. 95 |
| **Vốn góp thêm** | phần vượt mệnh giá: bán 5 đô-la, mệnh giá 1 → góp thêm 4 đô-la/cổ phiếu | PDF tr. 95 |
| **Thu nhập giữ lại** | *"phần lợi nhuận được tái đầu tư… thay vì dùng để trả cổ tức"*; có thể âm — **thâm hụt tích luỹ** | PDF tr. 95 |

⚠️ Một khác biệt pháp lý đáng nhớ giữa trái phiếu và cổ phiếu ưu đãi: *"Nếu một doanh nghiệp không thể
thanh toán lợi tức trên trái phiếu, người nắm giữ trái phiếu có thể **yêu cầu doanh nghiệp tuyên bố phá
sản**. Trong khi đó, người nắm giữ cổ phiếu ưu đãi thì **không**."* (PDF tr. 94). Đó là toàn bộ lý do
doanh nghiệp chịu trả cổ tức ưu đãi thay vì đi vay.

---

## 12. Giá trị sổ sách không bao giờ là giá trị thị trường

Phần III đóng lại bằng một câu hỏi tự đặt và một câu trả lời dứt khoát:

> *"Như vậy, vốn chủ sở hữu là những gì mà các cổ đông sẽ nhận khi doanh nghiệp được bán? **Tất nhiên
> là không!**"* — ch. 11 · PDF tr. 96

Sách liệt kê đúng ba lý do, và cả ba đều là các mục ở trên:

| # | lý do | mục |
| ---: | --- | --- |
| ① | tài sản ghi theo **giá mua** trừ khấu hao luỹ kế | [mục 6](#6-chi-phí-lịch-sử--mảnh-đất-los-angeles), [mục 7](#7-khấu-hao-luỹ-kế--chiếc-xe-tải-của-bài-3-đi-sang-bảng-cân-đối) |
| ② | lợi thế thương mại dồn tích và **không bao giờ bị khấu hao** | [mục 8](#8-lợi-thế-thương-mại--mjq-storage-và-động-cơ-định-giá-thấp) |
| ③ | tài sản vô hình **của chính doanh nghiệp** — thương hiệu, danh sách khách hàng — *"những thứ **không hề xuất hiện** trên bảng cân đối kế toán"* | — |

Giá trị sổ sách một cổ phiếu của công ty mẫu = 2.457 / 74 = **33,20 đô-la**. Còn giá thị trường thì tuỳ
thị trường:

| nếu thị trường trả P/E | giá cổ phiếu | vốn hoá | giá / giá trị sổ sách |
| ---: | ---: | ---: | ---: |
| 10 | 33,50 $ | 2.479 | 1,01 lần |
| 15 | 50,25 $ | 3.718 | 1,51 lần |
| 20 | 67,00 $ | 4.958 | 2,02 lần |
| 25 | 83,75 $ | 6.198 | 2,52 lần |

> *"Giá trị thị trường của một doanh nghiệp trên thực tế là **số tiền mà người mua muốn bỏ ra**."*
> — ch. 11 · PDF tr. 96

Đó đúng là câu kết của [bài 1](bai_01_nghe_thuat_tai_chinh.md) mục 3⑥, quay lại ở cuối Phần III. Ba
phương pháp định giá của bài 1 cho cùng một doanh nghiệp ba con số cách nhau 2,0 lần; bảng này cho thấy
cả ba đều không phải giá trị sổ sách.

---

## 13. 🇻🇳 Đối chiếu Việt Nam

**① Tên tiếng Việt nói thẳng ra điều mà tiếng Anh phải giải thích.** Mẫu B01-DN của Việt Nam đặt tên
hai nửa là **"TÀI SẢN"** và **"NGUỒN VỐN"**. Cái tên *nguồn vốn* chính là câu mà chương 11 phải viết cả
đoạn để nói: nửa dưới cho biết **tài sản đã được thu về như thế nào**. Người đọc báo cáo Việt Nam được
tặng sẵn cách đọc mà mục 11 phải đi tìm.

⚠️ Nhưng cũng vì thế mà dễ nhầm: **"nguồn vốn"** trong tiếng Việt gồm **cả nợ phải trả**, không phải chỉ
vốn chủ sở hữu.

**② Tên báo cáo khác nhau giữa hai khung.** VAS gọi là **"Bảng cân đối kế toán"**; IFRS gọi là **"Báo
cáo tình hình tài chính"** (*statement of financial position*). Báo cáo IFRS của Vinamilk dùng tên thứ
hai. Cùng một bảng, và cái tên thứ hai mô tả đúng hơn — nó là ảnh chụp tình hình, không phải một phép
cân đối.

**③ Lợi thế thương mại: chỗ khác biệt lớn nhất của cả bài.** Mục 8 dựng trên việc US GAAP đã **bỏ khấu
hao** lợi thế thương mại. **VAS 11** *(Hợp nhất kinh doanh)* thì ngược lại: lợi thế thương mại phải được
**phân bổ dần, thời gian tối đa 10 năm**.

| | lợi thế thương mại | hệ quả |
| --- | --- | --- |
| Sách (US GAAP hiện hành) | không khấu hao | động cơ định giá thấp tài sản hữu hình **mạnh nhất** |
| VAS 11 | phân bổ, **tối đa 10 năm** | định giá thấp hữu hình lại **tăng** chi phí phân bổ hằng năm |
| IFRS 3 | không khấu hao, chỉ đánh giá tổn thất | giống sách |

⭐ Kết quả là **động cơ ở mục 8 đảo chiều dưới VAS**. Với thời gian phân bổ lợi thế thương mại (≤10 năm)
**ngắn hơn** thời gian khấu hao nhiều tài sản hữu hình, đẩy giá trị sang lợi thế thương mại làm chi phí
hằng năm **tăng**, không giảm. Đây là ví dụ sạch nhất trong cả khoá học cho thấy *"nghệ thuật tài
chính"* không phải một danh sách thủ thuật cố định — nó là **hàm số của bộ quy tắc đang áp dụng**.

⚠️ Và vì Vinamilk công bố **song song hai bộ báo cáo**, cùng một thương vụ mua lại sẽ cho hai con số lợi
nhuận khác nhau ở hai bộ. Không bộ nào sai.

**④ Cấu trúc nguồn vốn khác hẳn.** Cùng phép đọc "ai trả tiền":

| | công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024, IFRS) |
| --- | ---: | ---: |
| Nợ phải trả | **52,7%** | **34,8%** |
| — trong đó khoản phải trả | 19,7% | 14,3% |
| Vốn chủ sở hữu | **47,3%** | **65,2%** |
| Đầu tư ngắn hạn / tổng tài sản | — *(không có dòng này)* | **40,8%** |

Vinamilk có **hai phần ba** tài sản là vốn chủ sở hữu, và **40,8%** tổng tài sản nằm ở **đầu tư ngắn
hạn** — chủ yếu là tiền gửi. Công ty mẫu thì hơn nửa tài sản đi vay mà có. Hai bảng cân đối này kể hai
câu chuyện khác nhau về rủi ro trước khi ta xem một dòng lợi nhuận nào — và đó chính là lý do chương 9
nói chuyên gia đọc bảng này trước.

---

## 14. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-04-bang-can-doi-ke-toan.py`](../thuc_hanh/bai-04-bang-can-doi-ke-toan.py) rồi chạy lại.
Không có lời giải.

1. **Cắt cổ tức.** Ở mục 3, nếu công ty mẫu **không trả cổ tức** thì vốn chủ sở hữu tăng bao nhiêu phần
   trăm một năm? Bao nhiêu năm thì gấp đôi? Tốc độ tăng trưởng tự thân giờ là bao nhiêu?

2. **Một năm lỗ.** Vẫn mục 3, thay lợi nhuận thuần 248 bằng **−248** nhưng vẫn trả cổ tức 166. Vốn chủ
   sở hữu đổi bao nhiêu? Mất mấy năm lỗ liên tiếp thì vốn chủ sở hữu về 0?

3. **Xe tải hai chiều.** Ở mục 7, thay vì kéo dài từ 3 lên 6 năm, hãy **rút ngắn** từ 3 xuống 2 năm.
   Bảng cân đối lệch bao nhiêu ở tháng 24? Vì sao gần như không ai làm chiều này?

4. **Dự phòng ở doanh nghiệp bán lẻ.** Ở mục 5, doanh nghiệp bán lẻ thu tiền ngay nên khoản phải thu
   rất nhỏ — thử `AR = 100`. Chỉnh một điểm dự phòng giờ đổi EPS bao nhiêu? Doanh nghiệp nào **dễ dùng**
   thủ thuật này hơn?

5. **Đất Los Angeles ở Việt Nam.** Ở mục 6, đổi thành mảnh đất mua năm 1995 với giá 1 tỷ đồng, nay 30
   năm sau. Ở mức tăng nào thì sổ sách giấu đi hơn 95% giá trị?

6. **ROA của một doanh nghiệp trẻ.** Vẫn mục 6, nếu PPE mới mua nên **đúng bằng** giá thị trường (bội
   số 1,0), ROA công bố có đáng tin không? Vậy khi so ROA hai doanh nghiệp, cần hỏi thêm điều gì?

7. **MJQ dưới VAS.** Ở mục 8, đổi thời gian phân bổ lợi thế thương mại từ 30 năm xuống **10 năm** (theo
   VAS 11) và giữ hữu hình 4 năm. Bảng chi phí đổi thế nào? Định giá thấp tài sản hữu hình giờ **có
   lợi** hay **có hại**?

8. **Tyco mua bằng cổ phiếu.** Ở mục 9, giả sử các thương vụ được trả bằng **phát hành cổ phiếu** thay
   vì tiền vay — tức vốn chủ sở hữu cũng tăng 200 mỗi thương vụ. Ngưỡng vốn chủ sở hữu âm giờ ở đâu?
   Vì sao trả bằng cổ phiếu lại **an toàn hơn** ở phép thử này?

9. **Tỷ lệ lợi thế thương mại cao hơn.** Vẫn mục 9, đổi tỷ lệ từ 80% lên **95%** giá mua. Ngưỡng dịch
   về thương vụ thứ mấy? Vì sao "định giá thấp tài sản hữu hình" và "vỡ ở phép thử này" là **cùng một
   việc**?

10. **Quảng cáo dài hơn.** Ở mục 10, đổi thời gian rải từ 24 tháng xuống **6 tháng**. Tài sản trả trước
    cuối tháng 1 giờ là bao nhiêu? Kỳ nào **khó biện minh** hơn — 24 tháng hay 6 tháng?

---

## 15. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Bảng cân đối kế toán | balance sheet | ảnh chụp tài sản và nợ **tại một ngày** |
| Báo cáo tình hình tài chính | statement of financial position | tên IFRS của cùng bảng đó |
| Phương trình kế toán cơ bản | basic accounting equation | tài sản = nợ phải trả + vốn chủ sở hữu |
| Vốn chủ sở hữu | equity / shareholders' equity | tài sản − nợ phải trả; còn gọi **giá trị sổ sách** |
| Tài sản ngắn hạn | current asset | chuyển được thành tiền trong **≤ 1 năm** |
| Tài sản dài hạn | long-term asset | tuổi đời sử dụng **> 1 năm** |
| Tài sản lưu động | liquid asset | tiền và thứ đổi ra tiền trong chưa đầy một ngày |
| Khoản phải thu | accounts receivable (A/R) | khách hàng nợ doanh nghiệp |
| Dự phòng nợ xấu | allowance for bad debt | **ước tính** phần khách sẽ không trả |
| "Chuốt" thu nhập | smoothing earnings | ép lợi nhuận thành đường **thẳng**, không phải đường cao |
| Tồn kho thành phẩm / WIP / nguyên vật liệu | finished / work-in-process / raw materials | ba lớp của hàng tồn kho |
| PPE | property, plant, and equipment | đất đai, nhà xưởng, thiết bị — ghi theo **giá mua** |
| Khấu hao luỹ kế | accumulated depreciation | tổng mọi khoản khấu hao từ ngày mua |
| Lợi thế thương mại | goodwill | giá mua − giá trị tài sản thuần nhận được |
| Mua lại | acquisition | *"sáp nhập"* và *"hợp nhất"* chỉ là tên nghe êm hơn |
| Tài sản vô hình | intangible asset | có giá trị nhưng **không cầm nắm được** |
| Tài sản trả trước | prepaid asset | đã trả tiền, chưa dùng hết |
| Nợ trả trước | accrued liability | đã dùng, chưa trả tiền |
| Cổ phiếu ưu đãi | preferred share | cổ tức cố định, thường **không** quyền biểu quyết |
| Mệnh giá | par value | số danh nghĩa, **không liên quan** giá thị trường |
| Vốn góp thêm | additional paid-in capital | phần nhà đầu tư trả **vượt** mệnh giá |
| Thu nhập giữ lại | retained earnings | lợi nhuận tái đầu tư thay vì chia cổ tức |
| Thâm hụt tích luỹ | accumulated deficit | thu nhập giữ lại **âm** |
| Vốn hoá thị trường | market capitalization | số cổ phiếu × giá cổ phiếu |
| Năm tài khoá | fiscal year | 12 tháng bất kỳ dùng cho kế toán |
| 💼 Tốc độ tăng trưởng tự thân | sustainable growth rate | ROE × tỷ lệ giữ lại — **cụm từ không có trong sách** |

---

## 16. Câu hỏi tự kiểm tra

1. Nhà quản lý đọc báo cáo nào trước? Chuyên viên ngân hàng đọc báo cáo nào trước? (mục 1)
2. Kể ba lý do sách đưa ra cho việc nhà quản lý né bảng cân đối. Lý do nào có tính hệ thống nhất? (mục 1)
3. Viết phương trình kế toán cơ bản theo cả hai cách. (mục 2)
4. Công ty mẫu: nợ phải trả và vốn chủ sở hữu chiếm bao nhiêu phần trăm tổng tài sản? (mục 2)
5. Khác biệt lớn nhất giữa bảng cân đối và báo cáo KQKD về mặt **thời gian** là gì? (mục 2)
6. Vì sao không nên đi tìm bảng cân đối cho riêng phòng ban của bạn? (mục 2)
7. Giải thích phép so sánh **GPA**. Câu nào trong đó là câu quan trọng nhất? (mục 3)
8. Vốn chủ sở hữu của công ty mẫu tăng bao nhiêu trong năm 2005? Bằng bao nhiêu phần trăm? (mục 3)
9. Với nhịp độ đó, bao nhiêu năm thì vốn chủ sở hữu gấp đôi? (mục 3)
10. **Tốc độ tăng trưởng tự thân** tính thế nào? Muốn tăng nhanh hơn thì có mấy đường? (mục 3)
11. Dòng nào trên bảng cân đối **không** phụ thuộc quyền tự quyết của kế toán? Ngoại lệ của nó là gì? (mục 4)
12. Ba lớp của hàng tồn kho là gì? Sách yêu cầu nhà quản lý nhớ **một** điều gì về tồn kho? (mục 4)
13. Tăng dự phòng nợ xấu thì lợi nhuận đổi thế nào? Giảm thì sao? (mục 5)
14. Cần chỉnh dự phòng nợ xấu **bao nhiêu điểm** để EPS đổi một xu? So với bài 2, cái nào dễ hơn? (mục 5)
15. Vì sao doanh nghiệp muốn **"chuốt"** thu nhập chứ không phải bơm nó lên? (mục 5)
16. Hai lý do sách đưa ra cho việc ghi PPE theo **giá mua** là gì? (mục 6)
17. Mảnh đất Los Angeles: mua bao nhiêu, nay đáng bao nhiêu, trên sổ sách bao nhiêu? Ứng với mức tăng
    mấy phần trăm một năm? (mục 6)
18. Tài sản bị ghi thấp làm **ROA** trông thế nào? Doanh nghiệp loại nào dễ gây hiểu lầm nhất? (mục 6)
19. Đổi giả định khấu hao xe tải từ 3 lên 6 năm: ở tháng 36 hai bảng cân đối lệch bao nhiêu, và khoản
    lệch ấy nằm ở dòng nào? (mục 7)
20. Viết đẳng thức nối khấu hao luỹ kế với vốn chủ sở hữu. Ở tháng 72 thì chênh lệch còn bao nhiêu? (mục 7)
21. Thuế làm khoản chênh 18.000 đó đổi thế nào? (mục 7)
22. **Lợi thế thương mại** định nghĩa ra sao? Tính nó cho thương vụ MJQ. (mục 8)
23. Quy tắc cũ và quy tắc mới về khấu hao lợi thế thương mại khác nhau thế nào? FASB lập luận gì? (mục 8)
24. Hạ định giá tài sản hữu hình từ 2 triệu xuống 1 triệu tiết kiệm bao nhiêu mỗi năm dưới **mỗi** quy
    tắc? Quy tắc nào cho động cơ mạnh hơn? (mục 8)
25. Tyco mua bao nhiêu công ty trong 2000–2001? Họ làm gì với giá trị tài sản mua lại, và để làm gì? (mục 9)
26. Viết phép thử một dòng để biết một doanh nghiệp mua lại có nguy hiểm không. (mục 9)
27. Vì sao tỷ lệ **LTTM/tổng tài sản** che mất nguy hiểm mà tỷ lệ **LTTM/vốn chủ sở hữu** thì không? (mục 9)
28. GAAP cho vốn hoá R&D với điều kiện gì? Sách hỏi lại câu gì? Ai bị nêu tên? (mục 9)
29. Chiến dịch quảng cáo 1 triệu: hai cách ghi khác nhau ở đâu, và **tổng** thì sao? (mục 10)
30. Sách nói động cơ chọn cách nào phụ thuộc vào điều gì? (mục 10)
31. Cách đọc lại nửa dưới bảng cân đối mà chương 11 đề xuất là gì? (mục 11)
32. Công ty mẫu: nhà cung cấp tài trợ bao nhiêu phần trăm tổng tài sản, và với lãi suất bao nhiêu? (mục 11)
33. Trong vốn chủ sở hữu, bao nhiêu là tiền cổ đông bỏ ra và bao nhiêu là lợi nhuận tự kiếm? (mục 11)
34. **Mệnh giá** có liên quan gì đến giá thị trường không? Công ty mẫu mệnh giá bao nhiêu? (mục 11)
35. Khác biệt pháp lý giữa người giữ **trái phiếu** và người giữ **cổ phiếu ưu đãi** khi doanh nghiệp
    không trả được là gì? (mục 11)
36. Vốn chủ sở hữu có phải là thứ cổ đông nhận khi bán doanh nghiệp không? Nêu **ba** lý do. (mục 12)
37. Giá trị sổ sách một cổ phiếu của công ty mẫu là bao nhiêu? (mục 12)
38. Sách định nghĩa **giá trị thị trường** thế nào? (mục 12)
39. Tên tiếng Việt **"nguồn vốn"** nói ra điều gì mà tiếng Anh phải giải thích? Nó có bao gồm nợ không? (mục 13)
40. VAS 11 xử lý lợi thế thương mại khác US GAAP thế nào? Điều đó làm động cơ ở mục 8 đổi ra sao? (mục 13)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 4 — BẢNG CÂN ĐỐI KẾ TOÁN  (ch. 9–11, PDF tr. 75–96)                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  CHUYÊN GIA ĐỌC BẢNG NÀY TRƯỚC, "săm soi nó một lúc lâu".                ║
║     Nhà quản lý thì không — vì KHÔNG AI GIAO CHỈ TIÊU trên bảng này.     ║
║                                                                          ║
║  TÀI SẢN = NỢ PHẢI TRẢ + VỐN CHỦ SỞ HỮU                                  ║
║     công ty mẫu:  5.193  =  2.736 (52,7%)  +  2.457 (47,3%)              ║
║     Bảng KQKD là ĐOẠN PHIM. Bảng cân đối là ẢNH CHỤP (có một NGÀY).      ║
║                                                                          ║
║  ⭐ GPA: lợi nhuận là ĐIỂM SỐ, vốn chủ sở hữu là ĐIỂM TRUNG BÌNH         ║
║     2.375 + 248 − 166 = 2.457     một năm dịch được 82 = 3,45%           ║
║     → gấp đôi vốn chủ sở hữu cần 30 NĂM                                  ║
║     ROE 10,1% × giữ lại 33,1% = tăng trưởng tự thân 3,34%                ║
║                                                                          ║
║  ⭐ DỰ PHÒNG NỢ XẤU — ước tính rẻ nhất để đổi EPS                        ║
║     chỉnh 0,105 ĐIỂM của khoản phải thu = MỘT XU EPS                     ║
║     bài 2 cần 1,38 triệu DOANH THU THẬT cho cùng một xu đó               ║
║     → mục tiêu là đường THẲNG, không phải đường CAO                      ║
║                                                                          ║
║  ⭐ CHI PHÍ LỊCH SỬ: đất LA 500.000 → 5 triệu, sổ sách vẫn 500.000       ║
║     ứng với 8,0%/năm suốt 30 năm — sổ sách giấu 90% giá trị              ║
║     mặt trái: ROA công bố 4,78% có thể thật ra chỉ 2,57% (1,86 lần)      ║
║                                                                          ║
║  ⭐ XE TẢI CỦA BÀI 3 ĐI SANG ĐÂY:  3 năm hay 6 năm?                      ║
║     tháng 36: KH luỹ kế 36.000 hay 18.000 → lệch 18.000                  ║
║     Δ TÀI SẢN = Δ VỐN CHỦ SỞ HỮU = Δ KHẤU HAO LUỸ KẾ                     ║
║     tháng 72: chênh lệch VỀ 0. Chỉ là vay mượn thời gian.                ║
║                                                                          ║
║  ⭐ LỢI THẾ THƯƠNG MẠI: MJQ 5 triệu − 2 triệu hữu hình = 3 triệu         ║
║     hạ định giá hữu hình 2 → 1 triệu, chỉ bằng MỘT Ý KIẾN THẨM ĐỊNH:     ║
║        quy tắc CŨ (KH 30 năm) tiết kiệm 216.667/năm                      ║
║        quy tắc MỚI (không KH)  tiết kiệm 250.000/năm  ← MẠNH HƠN         ║
║                                                                          ║
║  ⭐ TYCO — hơn 600 công ty trong 2 năm. Phép thử một dòng:               ║
║        LỢI THẾ THƯƠNG MẠI / VỐN CHỦ SỞ HỮU > 1  →  bóc ra là ÂM          ║
║     ở ngưỡng đó, LTTM mới chiếm 30,5% tổng tài sản — nhìn cột đó         ║
║     thì KHÔNG THẤY GÌ ĐÁNG SỢ.                                           ║
║                                                                          ║
║  QUẢNG CÁO 1 TRIỆU: ghi hết hay rải 1/24? Tổng luôn 1 triệu.             ║
║     Chỗ chưa ghi nhận phải NẰM Ở ĐÂU ĐÓ → tài sản trả trước.             ║
║     Chọn cách nào tuỳ... tháng đó làm ăn thế nào.                        ║
║                                                                          ║
║  AI TRẢ TIỀN CHO 5.193 TÀI SẢN?                                          ║
║     nhà cung cấp 19,7% (KHÔNG LÃI) · ngân hàng 2,9% · chủ nợ 30,1%       ║
║     cổ đông góp 22,8% · lợi nhuận tự kiếm 24,5%                          ║
║     → 51,8% vốn chủ sở hữu là tiền CÔNG TY TỰ KIẾM, không phải góp vào   ║
║                                                                          ║
║  ⭐ "VỐN CHỦ SỞ HỮU LÀ THỨ CỔ ĐÔNG NHẬN KHI BÁN? TẤT NHIÊN LÀ KHÔNG!"    ║
║     ① giá mua trừ khấu hao  ② goodwill không bao giờ khấu hao            ║
║     ③ thương hiệu của CHÍNH MÌNH không bao giờ lên bảng                  ║
║     giá trị sổ sách 33,20 $/cp — thị trường trả gì thì tuỳ thị trường    ║
║                                                                          ║
║  🇻🇳 VAS 11: goodwill PHẢI phân bổ, tối đa 10 NĂM → động cơ ở mục 8       ║
║     ĐẢO CHIỀU. "Nghệ thuật tài chính" là hàm số của BỘ QUY TẮC.          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần III — Bảng cân đối kế toán, nơi vén mở nhiều điều nhất**, PDF tr. 74–96.
    - Ch. 9 *Hiểu những điều căn bản về bảng cân đối kế toán*, PDF tr. 75–80
      — nhà quản lý vs chuyên viên ngân hàng, *"săm soi nó một lúc lâu"* (tr. 75); **ba lý do**
      (tr. 75–76); định nghĩa bảng cân đối và **vốn chủ sở hữu** (tr. 76); ⭐ **phép so sánh GPA**
      (tr. 77); **có − nợ = giá trị thuần** (tr. 77–78); **phương trình kế toán cơ bản** (tr. 78);
      bảng cân đối lập cho **toàn bộ tổ chức**, hai dạng trình bày (tr. 79); **năm tài khoá** và
      nhà bán lẻ (tr. 79–80); **Ford Motor 30 trang chú thích** và tuyên bố *"Việc sử dụng các ước
      tính"* (tr. 80)
    - Ch. 10 *Tài sản*, PDF tr. 81–91
      — tài sản ngắn hạn / dài hạn (tr. 81); **tiền — dòng duy nhất không phụ thuộc quyền tự quyết**,
      **Microsoft 56 tỷ**, **Parmalat** (tr. 81); **khoản phải thu** và **dự phòng nợ xấu** như công
      cụ *"chuốt"* thu nhập (tr. 82); hộp **"Chuốt thu nhập"** (tr. 82); **hàng tồn kho** ba lớp,
      chú thích **Barnes & Noble 2004** (tr. 83); *"tất cả hàng tồn kho đều tốn kém"* (tr. 83);
      **PPE ghi theo giá mua**, **Enron** (tr. 84); ⭐ **đất Los Angeles 500.000 → 5 triệu** (tr. 84);
      ⭐ **khấu hao luỹ kế lan sang bảng cân đối** (tr. 85); **lợi thế thương mại** và **MJQ Storage**
      (tr. 85–86); hộp **"Mua lại"** (tr. 86); **40 năm → FASB bỏ khấu hao** (tr. 87); ⭐ **phân tích
      động cơ** và **Tyco hơn 600 công ty** (tr. 88); **R&D, tính khả thi công nghệ, Computer
      Associates** (tr. 89); **tài sản trả trước** — thuê mặt bằng 60.000 và **chiến dịch quảng cáo
      1 triệu** (tr. 89–91)
    - Ch. 11 *Phía bên kia*, PDF tr. 92–96
      — ⭐ *"cho ta thấy các tài sản đã được thu về như thế nào"* (tr. 92); nợ ngắn hạn / dài hạn,
      **khoản phải trả của nợ dài hạn 100.000 / 10.000**, vay ngắn hạn (tr. 92); **khoản phải trả** —
      *"các nhà cung cấp đã cho doanh nghiệp vay nợ"*, **nợ trả trước** ví dụ tiền lương (tr. 93);
      nợ dài hạn (tr. 93); **cổ phiếu ưu đãi** và khác biệt pháp lý với trái phiếu (tr. 94); hộp
      **"Vốn"** (tr. 94); **cổ phiếu phổ thông**, **mệnh giá 1 đô-la**, **vốn góp thêm** (tr. 95);
      **cổ tức**, **thu nhập giữ lại**, **thâm hụt tích luỹ** (tr. 95); ⭐ *"Tất nhiên là không!"* và
      **ba lý do**, **vốn hoá thị trường** (tr. 96)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 2, 3, 5, 6, 7, 9, 11, 12
- **Chuẩn mực kế toán Việt Nam số 11 — Hợp nhất kinh doanh (VAS 11)**, và hướng dẫn tại
  **Thông tư 202/2014/TT-BTC** — phân bổ lợi thế thương mại, thời gian tối đa 10 năm.
  Nhắc ở [mục 13](#13--đối-chiếu-việt-nam).
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 13](#13--đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-04-bang-can-doi-ke-toan.py`](../thuc_hanh/bai-04-bang-can-doi-ke-toan.py):
  - bảng cân đối **cân** và cuộn chiếu vốn chủ sở hữu 2.375 + 248 − 166 = 2.457, chốt bằng `assert`;
  - xe tải: **Δ tài sản = Δ khấu hao luỹ kế** ở **mọi mốc tháng**, chốt bằng `assert`;
  - dự phòng nợ xấu: mức chỉnh cho một xu EPS **nhỏ hơn 0,2 điểm**, chốt bằng `assert`;
  - đất Los Angeles: con số 5 triệu của sách ứng với **8%/năm**, chốt bằng `assert`;
  - MJQ: quy tắc mới cho động cơ định giá thấp **mạnh hơn** quy tắc cũ, chốt bằng `assert`;
  - Tyco: ngưỡng vốn chủ sở hữu âm rơi đúng **thương vụ thứ 16**, chốt bằng `assert`;
  - "ai trả tiền": năm nguồn cộng lại **đúng bằng tổng tài sản**, chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** bội số 1,5–3,0 cho PPE ở mục 6; thuế suất áp
  vào khoản chênh 18.000 ở mục 7; thời gian khấu hao 4 năm / 30 năm và các mức định giá 1,5 / 1,0 /
  0,5 triệu ở mục 8; toàn bộ tham số thương vụ (200 triệu, 80%) ở mục 9; dải P/E 10–25 ở mục 12. Mọi
  con số **của sách** đều được trích kèm mốc `ch. N · PDF tr. M`.

---

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| **4** | **Bảng cân đối kế toán** ← *bạn đang ở đây* | ch. 9–11 | 🎯 |
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
