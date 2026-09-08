# Bài 12 — Tổ chức có trí tuệ tài chính

> Bài học dựng từ **Phần VIII — Xây dựng bộ phận (và tổ chức) có trí tuệ tài chính**: chương 29 *Xoá mù tài
> chính và hiệu quả hoạt động của doanh nghiệp* (PDF tr. 210–215), chương 30 *Các chiến lược xoá mù tài
> chính* (PDF tr. 216–220), chương 31 *Minh bạch tài chính: mục tiêu tối thượng* (PDF tr. 221–222), và hộp
> công cụ *Hiểu đạo luật Sarbanes-Oxley* (PDF tr. 222–223).
> ⚠️ **Bản dịch in phần này là "PHẦN VII"** — hệ quả của lỗi đánh số phần đã nêu ở
> [bài 9 mục 10](bai_09_ty_le_hieu_suat_va_dupont.md#10--chỗ-sách-in-sai-trong-chương-23). Bản gốc có 8
> phần; đây là **phần VIII**.
> 🔸 **Vòng 2 — và là bài ĐÓNG CẢ KHOÁ.** Ba chương cuối gần như **không có số**: chúng là lập luận về
> **văn hoá**. Nên bài này làm hai việc thêm mà các bài trước không làm:
> [mục 9](#9-sổ-tổng-kết--mọi-chỗ-sách-in-sai) tổng kết **mọi chỗ sách in sai** mà 12 bài đã tìm ra, và
> [mục 10](#10-kiểm-toàn-khoá--dựng-lại-mọi-khẳng-định) **dựng lại toàn bộ số liệu** để chốt lại mọi
> khẳng định đầu mục của cả môn.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [bài 0](bai_00_bat_dau_tu_dau.md) *(mục 9 khép lại đúng bài tập mà bài 0 mở ra)*.
> Mọi bài còn lại đều được nhắc tới ở đây.
> ⚙️ **Code:** [`thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py`](../thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py)
> — quy những chỗ **đo được** ra số *(chi phí tuân thủ SOX, ba buổi dạy của Joe)*, đếm và phân loại **28 chỗ
> sách in sai**, và chạy **bài kiểm hồi quy** cho cả môn học.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vì sao đọc được báo cáo tài chính lại đổi cách làm việc](#1-vì-sao-đọc-được-báo-cáo-tài-chính-lại-đổi-cách-làm-việc)
- [2. Câu chuyện nhân viên bán hàng — một mẫu hình, không phải một giai thoại](#2-câu-chuyện-nhân-viên-bán-hàng--một-mẫu-hình-không-phải-một-giai-thoại)
- [3. Warfighting — trí tuệ tài chính là chuyện tốc độ](#3-warfighting--trí-tuệ-tài-chính-là-chuyện-tốc-độ)
- [4. "Xuống hàng ngũ quân lính" — bằng chứng sách viện dẫn](#4-xuống-hàng-ngũ-quân-lính--bằng-chứng-sách-viện-dẫn)
- [5. Ba phương pháp xoá mù tài chính, và bản đồ sang khoá này](#5-ba-phương-pháp-xoá-mù-tài-chính-và-bản-đồ-sang-khoá-này)
- [6. Quy tắc học của người trưởng thành — và khoá này dùng sai chỗ nào](#6-quy-tắc-học-của-người-trưởng-thành--và-khoá-này-dùng-sai-chỗ-nào)
- [7. Minh bạch tài chính — Enron nhìn từ phía nhân viên](#7-minh-bạch-tài-chính--enron-nhìn-từ-phía-nhân-viên)
- [8. 📚 Hộp công cụ — Sarbanes-Oxley, và cái giá quy ra tỷ lệ](#8--hộp-công-cụ--sarbanes-oxley-và-cái-giá-quy-ra-tỷ-lệ)
- [9. Sổ tổng kết — mọi chỗ sách in sai](#9-sổ-tổng-kết--mọi-chỗ-sách-in-sai)
- [10. Kiểm toàn khoá — dựng lại mọi khẳng định](#10-kiểm-toàn-khoá--dựng-lại-mọi-khẳng-định)
- [11. 🎓 Đi tiếp từ đây](#11--đi-tiếp-từ-đây)
- [12. Tự thử](#12-tự-thử)
- [13. Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
- [14. Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vì sao đọc được báo cáo tài chính lại đổi cách làm việc

Sách mở chương cuối bằng một phép so sánh rất gọn:

> *"Bạn sẽ **không bao giờ chơi bóng rổ hay cờ thỏ cáo** mà trước tiên không tìm hiểu trò đó được chơi như
> thế nào; **vậy thì tại sao công việc kinh doanh lại khác?**"* — ch. 29 · PDF tr. 210

Ba thứ bạn có được khi nắm luật chơi:

1. nhìn công việc của mình trong **bức tranh toàn cảnh** của doanh nghiệp;
2. đánh giá **hiệu quả làm việc của chính mình** chính xác hơn trước;
3. hiểu **tại sao** các con số trọng yếu đang đi theo hướng này hay hướng kia.

⭐ Rồi sách quay lại **luận điểm trung tâm của cả cuốn — lần cuối**:

> *"các thẻ báo cáo tài chính **phần nào phản ánh hiện thực**. Nhưng chúng cũng — và **đôi khi chủ yếu** —
> phản ánh cả những **ước tính, giả định, phỏng đoán** và tất cả các **định kiến** từ đó mà ra. (Cũng có lúc
> chúng phản ánh **hành vi giả mạo** không lẫn đi đâu được)."* — ch. 29 · PDF tr. 210

Và biến nó thành một việc **làm được** — ba câu hỏi mang đi hỏi phòng tài chính:

| câu hỏi của sách | bài trong khoá này |
| --- | --- |
| *"Họ **công nhận** một khoản mục doanh thu cụ thể **như thế nào**?"* | [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) |
| *"Tại sao họ lại **chọn khung thời gian cụ thể đó** để khấu hao?"* | [bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md), [bài 4](bai_04_bang_can_doi_ke_toan.md) |
| *"Tại sao **DII** lại tăng?"* | [bài 9](bai_09_ty_le_hieu_suat_va_dupont.md), [bài 11](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) |

⭐ **Ba câu hỏi này là cả cuốn sách nén thành ba dòng.** Và sách dự đoán phản ứng:

> *"sau khi qua được **cơn choáng váng** khi nghe thấy những đồng nghiệp **ngoài lĩnh vực tài chính** nói
> **thứ ngôn ngữ của mình**, gần như chắc chắn họ sẽ **sẵn lòng trình bày cơ sở** cho các giả định và ước
> tính, **và điều chỉnh chúng cho phù hợp**."* — ch. 29 · PDF tr. 210

Vế cuối là phần thưởng thật: **giả định bị hỏi đến thì giả định sẽ đổi.**

---

## 2. Câu chuyện nhân viên bán hàng — một mẫu hình, không phải một giai thoại

Các tác giả dạy một nhóm chuyên viên bán hàng đọc báo cáo của chính công ty họ. Đến phần báo cáo lưu chuyển
tiền tệ — *"chỉ cho họ thấy **két tiền mặt của công ty đã cạn kiệt ra sao** khi theo đuổi chiến lược **tăng
trưởng qua mua lại**"* — một người bật cười:

> *"Tôi đang phải **đấu tranh** với ông phó tổng giám đốc phụ trách bán hàng đến **gần cả năm nay**. Lý do
> là, họ **thay đổi kế hoạch trả hoa hồng** của chúng tôi. Trước đây, chúng tôi thường trả **vào thời điểm
> bán hàng**, còn bây giờ chúng tôi chỉ được trả **sau khi thu xong công nợ**. **Cuối cùng tôi cũng hiểu lý
> do thay đổi.**"* — ch. 29 · PDF tr. 211

⭐ Đọc lại câu chuyện đó bằng công cụ của khoá này thì nó **không còn là giai thoại**:

| chi tiết trong chuyện | là cái gì trong khoá này |
| --- | --- |
| tăng trưởng qua mua lại | tiền ra ở mục **đầu tư** — [bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) |
| két tiền cạn kiệt | dòng *"Thay đổi trong tiền mặt"* — [bài 6](bai_06_loi_nhuan_khac_tien_mat.md)–7 |
| trả hoa hồng khi **BÁN** | thưởng theo **doanh thu** — [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md): ghi nhận |
| trả hoa hồng khi **THU ĐƯỢC TIỀN** | thưởng theo **DSO** — [bài 9](bai_09_ty_le_hieu_suat_va_dupont.md), [bài 11](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) |

Công ty đã đổi **cơ sở trả thưởng** từ một con số **kế toán** sang một con số **tiền mặt**. Và
[bài 11 mục 4](bai_11_von_luu_dong_va_chu_ky_tien_mat.md#4-ba-đòn-bẩy--và-chúng-không-bằng-nhau) đã đo giá
trị của việc đó: **một ngày DSO của công ty mẫu đáng 24,14 triệu đô-la.**

⚠️ **Cái đắt nhất trong câu chuyện không phải là kế hoạch mới. Là việc nó chạy một năm mà không ai giải
thích.** Sách kết: *"ông **thật sự không để tâm** tới việc ban quản lý đã thay đổi kế hoạch… Tuy nhiên,
**trước đó ông không hề hiểu tại sao**."* Chi phí của việc không giải thích là **một năm đối đầu**, và nó
không nằm ở dòng nào trên báo cáo tài chính cả.

📚 Sách cũng chỉ ra mặt trái khi thiếu minh bạch: ở một công ty, nhân viên tin rằng chia sẻ lợi nhuận *"chỉ
được thực hiện trong những năm họ ca thán"*. Thực tế công ty có một kế hoạch thẳng thắn — nhưng *"những
hoạt động chính trị như vậy om xòm đến độ các nhân viên **chẳng bao giờ tin kế hoạch đó là thật**"*. Liều
thuốc giải mà sách kê: ***"ánh sáng mặt trời, sự minh bạch và truyền thông mở"*** (tr. 212).

---

## 3. Warfighting — trí tuệ tài chính là chuyện tốc độ

Sách mượn một lập luận từ cuốn ***Warfighting*** của Thuỷ Quân Lục Chiến Hoa Kỳ (1989):

> *"lính thuỷ luôn phải đối mặt với **sự bất ổn định** và những điều kiện **thay đổi nhanh chóng**. Họ
> **hiếm khi có thể dựa vào những chỉ dẫn từ cấp trên**; thay vào đó, họ phải **tự mình ra quyết định**. Vì
> vậy có một quy định là các chỉ huy phải **nói rõ mục tiêu chung**, và sau đó để các sĩ quan cấp thấp hơn
> và binh lính **tự ra quyết định thi hành**."* — ch. 29 · PDF tr. 212–213

⭐ Đó là lập luận **mạnh nhất** của cả chương, và nó **không phải về đạo đức — nó về tốc độ**:

> *"Các nhà quản lý phải đưa ra nhiều quyết định **hằng ngày** mà **không thể tham vấn cấp cao hơn**. Nếu họ
> hiểu các **thông số tài chính đang gây áp lực** cho mình, họ có thể ra quyết định **nhanh và hiệu quả
> hơn**."* — ch. 29 · PDF tr. 213

💼 Đổi ra ngôn ngữ của khoá này: một người **biết chỉ số nào đang bị siết** thì tự ra được quyết định đúng
mà không cần hỏi.

| nếu chỉ số bị siết là… | thì người ở tuyến đầu tự biết… |
| --- | --- |
| **DSO** | gọi khách đòi hạn trước khi giao lô tiếp theo |
| **ngày tồn kho (DII)** | không chạy máy khi đơn hàng đang xuống |
| **hệ số thanh toán nhanh** | hoãn mua sắm không gấp sang quý sau |
| **biên lợi nhuận gộp** | không chiết khấu thêm để đóng đơn hàng |

**Không quyết định nào trong bốn dòng trên cần đến một cuộc họp.** Đó là toàn bộ ý nghĩa của phép so sánh
với thuỷ quân lục chiến.

---

## 4. "Xuống hàng ngũ quân lính" — bằng chứng sách viện dẫn

Đến đây sách đổi đối tượng: không còn là nhà quản lý, mà là **tất cả mọi người**.

> *"nếu việc các nhà quản lý hiểu tài chính có thể làm nên sự khác biệt, hãy tưởng tượng sự khác biệt đó sẽ
> **lớn đến dường nào** nếu **tất cả mọi người** trong một bộ phận — đúng ra là tất cả mọi người trong một
> công ty — **đều hiểu nó**."* — ch. 29 · PDF tr. 213

⭐ Và sách **đưa bằng chứng, không chỉ đưa niềm tin.** Trung tâm **Effective Organizations** đo hai thước đo
về sự tham gia của nhân viên:

1. *"chia sẻ thông tin về hiệu quả hoạt động kinh doanh, các kế hoạch và mục tiêu"*;
2. đào tạo nhân viên *"các kỹ năng hiểu công việc kinh doanh"*.

> *"**Cả hai** thước đo này đều có **mối quan hệ tỷ lệ thuận** với **năng suất, sự hài lòng của khách hàng,
> chất lượng, tốc độ, khả năng sinh lời, sức cạnh tranh** và **sự hài lòng của nhân viên**."*
> — ch. 29 · PDF tr. 214

Kèm ba tên khác: **Daniel R. Denison, Peter Drucker, Jeffrey Pfeffer**.

⚠️ **Đọc cho đúng: đây là TƯƠNG QUAN, không phải NHÂN QUẢ.** Sách viết *"mối quan hệ tỷ lệ thuận"* và dừng ở
đó — **đúng**. Doanh nghiệp khoẻ mạnh có thể vừa đủ sức đào tạo **vừa** có năng suất cao, mà đào tạo không
phải nguyên nhân. **Sách không khẳng định quá mức, nhưng người đọc rất dễ đọc quá mức.**

Chuỗi nhân quả mà sách **thực sự** đề xuất thì hợp lý và kiểm được từng mắt xích:

> hiểu số → **tin tưởng** tăng → **biến động nhân sự** giảm → **động lực và cam kết** tăng

💼 Câu chuyện **Setpoint** đóng chương, và nó là một nhân chứng không ngờ: kế toán viên của công ty — người
*"hơn một lần nói với Joe rằng công ty sẽ **không thể trụ được** qua giai đoạn biến động này"* — cuối cùng
thú nhận:

> *"tôi nghĩ **lý do tại sao các anh vượt qua được** những khó khăn đó là vì các anh **đã đào luyện nhân
> viên** của mình và **chia sẻ thông tin tài chính** với họ. Khi rơi vào khó khăn, **cả công ty sát cánh bên
> nhau** và tìm ra cách chiến đấu, vượt qua nó."* — ch. 29 · PDF tr. 215

⭐ Và một câu phụ nhưng sắc: *"người ta sẽ **khó có thể 'xào nấu' sổ sách** khi nó **mở cho tất cả mọi
người**."* **Minh bạch không chỉ là động lực — nó là một cơ chế kiểm soát.**

---

## 5. Ba phương pháp xoá mù tài chính, và bản đồ sang khoá này

Sách rào trước rằng đây **không phải việc làm một lần**:

> *"Bạn **không thể** chỉ tổ chức khoá đào tạo **một lần rồi thôi**, hay phát một cuốn sách hướng dẫn và chờ
> đợi mọi người được khai thông… **Xoá mù tài chính cần trở thành một phần của văn hoá doanh nghiệp.**"*
> — ch. 30 · PDF tr. 216

### ① Đào tạo (đi đào tạo lại)

*"Ba buổi ngắn, mỗi buổi **30–50 phút**, tập trung vào **một khái niệm tài chính**."* Joe đã làm đúng thế ở
Setpoint:

| buổi của Joe ở Setpoint | bài trong khoá này |
| --- | --- |
| ① báo cáo kết quả kinh doanh | [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) và [bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) |
| ② báo cáo lưu chuyển tiền tệ + tài chính dự án | [bài 6](bai_06_loi_nhuan_khac_tien_mat.md), [bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) và [bài 10](bai_10_tinh_ty_le_hoan_von_dau_tu.md) |
| ③ bảng cân đối kế toán | [bài 4](bai_04_bang_can_doi_ke_toan.md) và [bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md) |

⭐ **Ba buổi của Joe phủ đúng sáu bài đầu tiên của khoá này.** Sách coi đây là **mức tối thiểu** để một đội
nhóm làm việc được — còn lại (tỷ lệ, ROI, vốn lưu động) là phần cho người muốn đi sâu. Đó cũng là lý do
[bài 0](bai_00_bat_dau_tu_dau.md) xếp vòng ưu tiên 🎯 / 🔸.

📚 Sách còn thêm: cho **mọi người tham dự nhiều lần** *("mọi người thường phải mất nhiều thời gian mới lĩnh
hội được vấn đề")*, và **đề nghị thành viên khác đứng lớp** — *"phong cách giảng dạy của họ có thể khác bạn
đủ để họ có thể tiếp cận những người mà bạn không thể"*.

### ② Họp hằng tuần với "các con số"

> *"**Hai, ba con số** đo lường hiệu quả hoạt động của **đơn vị bạn** giữa các tuần và giữa các tháng là
> gì?"* — ch. 30 · PDF tr. 217

Sách gợi ý: hàng hoá gửi đi, doanh thu, số giờ tính phí, hiệu quả theo ngân sách. Rồi nâng cấp:

> *"**Dự đoán** những con số này sẽ ở đâu trong tháng hoặc quý tiếp theo. Bạn sẽ ngạc nhiên khi thấy mọi
> người bắt đầu **giữ quyền sở hữu một con số** như thế nào khi họ **đặt cược uy tín** của mình vào dự
> đoán."* — ch. 30 · PDF tr. 217

### ③ Bảng điểm và phương tiện nghe nhìn

> *"Chúng tôi luôn thắc mắc tại sao các đơn vị điều hành **không sử dụng bảng điểm đó và công khai** cho tất
> cả mọi nhân viên."* — ch. 30 · PDF tr. 217

Kèm một cảnh báo rất cụ thể: *"những **đồ thị nhỏ** có thể **dễ bị phớt lờ** hơn — và nếu có thể, tức là
chúng **sẽ bị**. Cũng như với bảng đồng hồ trên xe, hãy đảm bảo rằng bảng điểm **rõ ràng, trực diện và nằm
ngay trước mắt** bạn."* (tr. 218)

💼 Một chi tiết đáng chú ý: một công ty làm **hai** sơ đồ dòng tiền — một ghi *"con số **mục tiêu**… những
gì mà **chi nhánh tốt nhất** của công ty sẽ làm"*, một để quản lý điền *"những con số **thật sự** của chi
nhánh"*. Đó là **bình quân ngành nội bộ** — đúng trục so sánh thứ ba mà
[bài 8 mục 1](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md#1-so-với-cái-gì-kia) đã nêu, nhưng đặt trong
cùng một công ty.

📚 **Và một câu chuyện về đổi ngôn ngữ** (tr. 220): một giám đốc vùng bắt đầu gọi nhân viên của mình là
***đối tác kinh doanh***. Họ đổi cả **biển hiệu bãi đậu xe** để chữ *"nhân viên"* biến mất. Các vùng khác
học theo, rồi chủ tịch toàn quốc dùng từ đó trong bản tin nội bộ. Sách ghi nhận điều kiện đủ, không chỉ điều
kiện cần: nhân viên tin là vì *"cũng có **nhiều điều khác nữa** cho thấy ban quản lý thật sự coi họ là đối
tác"*.

---

## 6. Quy tắc học của người trưởng thành — và khoá này dùng sai chỗ nào

Sách đưa năm quy tắc (tr. 219–220). Chúng áp thẳng được vào chính cách khoá học này được dựng:

| quy tắc của sách | khoá này làm gì |
| --- | --- |
| **Lôi kéo họ tham gia** — *"học được ít nhất khi họ **bị dạy dỗ**; họ học được nhiều nhất khi **tự mình thực hiện**"* | mục **Tự thử** ở cuối mỗi bài: sửa tham số rồi chạy lại, **không có lời giải** |
| Cho họ **tự tính**, thảo luận tác động và giải thích ý nghĩa | mỗi bài có một tệp `.py` chạy được, đọc số từ **cùng một** bộ dữ liệu |
| Họ học nhanh khi **thấy có lý do** — thấy liên quan đến công việc | mỗi mục mở bằng một câu hỏi thật, và 🇻🇳 nối sang doanh nghiệp Việt Nam |
| **Chớ giả định** về những gì họ đã biết | [bài 0](bai_00_bat_dau_tu_dau.md) đo nền trước; mỗi bài có 📌 *"cần đọc trước"* |
| **Đừng cố biến họ thành kế toán viên** | không dạy bút toán; cả khoá **đọc** báo cáo chứ không **lập** báo cáo |

⚠️ **Và đây là chỗ khoá này đi ngược quy tắc của sách — có ý.** Sách bảo *"để bài giảng thật tập trung"*, mỗi
buổi **30–50 phút**, **một** khái niệm. Các bài ở đây dài gấp nhiều lần thế.

Lý do: **sách viết cho người đứng lớp, còn đây là tài liệu tra cứu** — đọc một lần rồi quay lại từng mục.
Hai định dạng khác nhau. **Nếu bạn dùng tài liệu này để đứng lớp thì hãy theo sách: một mục, một buổi.**

---

## 7. Minh bạch tài chính — Enron nhìn từ phía nhân viên

Cả khoá này nhắc Enron ở [bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) *(ROA cao giả tạo)* và
[bài 9](bai_09_ty_le_hieu_suat_va_dupont.md) *(DuPont định vị đúng cột nhưng gọi sai tên)*. Chương 31 nhìn nó
từ một phía khác hẳn — **phía người làm thuê**:

> *"Các nhân viên của Enron tưởng rằng mình đang có trong tay điều tốt đẹp: **một công ty tăng trưởng, cổ
> phiếu lên giá nhanh, kế hoạch lương 401(k) hậu hĩnh, nhiều cơ hội thăng tiến**. Nhưng rồi mọi thứ **đột
> ngột đổ sụp**. Chỉ trong nháy mắt, gần như tất cả các nhân viên phải **vật vờ ra đường xin việc**."*
> — ch. 31 · PDF tr. 221

⭐ Và rút ra kết luận **thực dụng, không đạo đức**:

> *"vì những **lý do rất thực tế**, họ nên hiểu đôi điều về hoạt động tài chính của **công ty mà mình đang
> làm việc**. **Giống như các nhà đầu tư, họ cần biết công ty đang làm ăn như thế nào.**"*
> — ch. 31 · PDF tr. 221

⚠️ **Sách cũng tự đặt giới hạn cho mình, và giới hạn đó đúng:** *"chắc chắn là những doanh nghiệp **được
giao dịch công khai không thể** trưng cho các nhân viên xem những báo cáo tài chính hợp nhất **ngoài một lần
mỗi quý**, khi thông tin được bố cáo cho công chúng."* — đó là **luật công bố thông tin**, không phải sự
giấu giếm.

Nhưng: *"họ **có thể cố gắng giải thích** những báo cáo này **khi chúng được phát đi**. Trong thời gian đó,
họ có thể đảm bảo các nhân viên **thấy được các con số hoạt động** của phòng ban hoặc cơ sở mà mình làm
việc."*

⭐ **Câu kết của cả cuốn sách**, và nó là một ẩn dụ đáng giữ:

> *"**Thông tin tài chính là hệ thần kinh** của bất kỳ một doanh nghiệp nào… **Từ quá lâu, ở mỗi doanh
> nghiệp chỉ có một nhóm là những người duy nhất hiểu dữ liệu tài chính nói gì.** Chúng tôi cho rằng cần có
> thêm nhiều người hiểu dữ liệu tài chính, **bắt đầu từ những nhà quản lý, rồi cuối cùng mở rộng ra toàn bộ
> lực lượng lao động**."* — ch. 31 · PDF tr. 222

---

## 8. 📚 Hộp công cụ — Sarbanes-Oxley, và cái giá quy ra tỷ lệ

Đạo luật của Quốc hội Mỹ, **tháng 7/2002**, đáp lại chính loạt gian lận mà cả cuốn sách này kể: Enron,
WorldCom, Tyco, Sunbeam. Sách gọi nó là *"điều luật có **tác động lớn nhất** lên vấn đề quản lý doanh
nghiệp, tiết lộ thông tin tài chính và kế toán công **kể từ sau luật chứng khoán ban đầu** của Mỹ trong thập
niên 1930"*.

| điều khoản | liên hệ trong khoá này |
| --- | --- |
| lập **Ban kiểm soát kế toán** công ty niêm yết | — |
| cấm công ty kiểm toán bán **dịch vụ phi kiểm toán** | [bài 1](bai_01_nghe_thuat_tai_chinh.md): xung đột lợi ích |
| bắt lập thủ tục để nhân viên **báo gian lận** | ch. 31: minh bạch |
| **cấm sa thải / hạ bậc** người tố giác | ch. 31: minh bạch |
| CEO và CFO phải **ký chứng nhận** báo cáo | [bài 1](bai_01_nghe_thuat_tai_chinh.md): ai chịu trách nhiệm |
| cấm công ty **cho nhà điều hành vay** tiền | [bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md): Enron / Fastow |
| buộc **hoàn trả thưởng** nếu phải báo cáo lại | [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md): ghi nhận doanh thu |
| bắt thêm **"báo cáo kiểm soát nội bộ"** hằng năm | [bài 1](bai_01_nghe_thuat_tai_chinh.md): nghệ thuật tài chính |

📚 Sách kèm một con số đáng nhớ về **lý do** điều khoản cấm cho vay ra đời: một nghiên cứu của
**Corporate Library Research Group** phát hiện các doanh nghiệp đã cho nhà điều hành vay **trên 4,5 tỷ
đô-la** trong năm 2001, *"với mức lãi suất bằng 0 hoặc rất thấp"*.

### ⚠️ Sách đưa cái giá, rồi để nguyên

> *"việc triển khai hoạt động này **rất đắt đỏ**. Chi phí **trung bình** cho các doanh nghiệp là **5 triệu
> đô-la**; đối với những doanh nghiệp lớn như **General Electric**, con số có thể lên tới **30 triệu
> đô-la**."* — hộp công cụ · PDF tr. 223

**Đổi 5 triệu đô-la ra tỷ lệ** *(các mức lợi nhuận dưới đây là của bài học, để đo độ dốc)*:

| lợi nhuận thuần của doanh nghiệp | 5 triệu = bao nhiêu % |
| ---: | ---: |
| 25 triệu đô-la | **20,00%** |
| 100 triệu đô-la | 5,00% |
| **248 triệu đô-la** *(công ty mẫu)* | **2,02%** |
| 1.000 triệu đô-la | 0,50% |
| 5.000 triệu đô-la | 0,10% |

⭐ Với công ty mẫu: **2,0% lợi nhuận thuần mỗi năm**. Với một doanh nghiệp lợi nhuận 25 triệu — vẫn là doanh
nghiệp niêm yết — là **20%**.

**Chi phí tuân thủ gần như cố định, nên nó LUỸ THOÁI: doanh nghiệp càng nhỏ thì càng đau.** Sách đưa cả hai
con số 5 triệu và 30 triệu mà không nói điều này *(chốt bằng `assert`)*.

💼 Đó là một mẫu hình dùng lại được ở **mọi quy định**: chi phí tuân thủ ít khi tỷ lệ với quy mô. Muốn biết
một quy định mới ảnh hưởng ai nhiều nhất, hãy **chia chi phí tuân thủ cho lợi nhuận** chứ đừng nhìn con số
tuyệt đối. Đó đúng là [bài 8 mục 1](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md#1-so-với-cái-gì-kia):
***"So với cái gì kia?"***

---

## 9. Sổ tổng kết — mọi chỗ sách in sai

[Bài 0](bai_00_bat_dau_tu_dau.md) mở khoá bằng một bài tập: **đo lỗi của chính cuốn sách**. Đây là vòng khép
lại.

| lớp lỗi | số chỗ | nặng hay không |
| --- | ---: | --- |
| **số** | **10** | sai kết quả, nhưng **đo được** bằng phép tính |
| **dấu** | **2** | đảo dấu — đổi nghĩa cả bảng |
| **khái niệm** | **8** | **nặng nhất**: dạy người đọc gọi tên sai |
| **biên tập** | **8** | không làm sai phép tính nào |
| **TỔNG** | **28** | |

*(Danh sách đầy đủ từng chỗ nằm trong [README](../README.md) và trong tệp code của bài này.)*

### Nhưng con số đáng giá hơn là VỊ TRÍ

| vị trí | số lỗi | % số lỗi | ghi chú |
| --- | ---: | ---: | --- |
| **phụ lục** | 5 | 17,9% | **chỉ 4/227 trang sách** |
| **ô công thức** | 6 | 21,4% | vài chục ô trong cả cuốn |
| bảng số | 2 | 7,1% | hai bảng ở ch. 15 |
| chữ chạy | 14 | 50,0% | phần còn lại — **hầu hết cuốn sách** |
| tiêu đề | 1 | 3,6% | trang tiêu đề các phần |

⭐ **Phụ lục là chỗ đặc nhất, và cách biệt rất xa:**

| | |
| --- | ---: |
| phụ lục | 5 lỗi / 4 trang = **1,25 lỗi mỗi trang** |
| cả cuốn | 28 lỗi / 227 trang = **0,12 lỗi mỗi trang** |
| **→ đặc gấp** | **10 LẦN** |

*(chốt bằng `assert`)*

💼 Và đó là một **quy tắc đọc** dùng được cho mọi tài liệu tài chính, không riêng cuốn này: **lỗi tập trung ở
chỗ có nhiều con số và ít chữ.** Phụ lục, ô công thức, bảng biểu — đó là những chỗ **không ai đọc lại thành
câu**, nên **không ai nghe thấy nó sai**. Phần chữ chạy thì ngược lại: nó được đọc to lên trong đầu người
biên tập.

⭐ **Và nghịch lý khép lại cả khoá học:** cuốn sách có luận điểm trung tâm là *"đừng tin các con số — chúng
là sản phẩm của ước tính và giả định"*. **Nó tự chứng minh luận điểm đó 28 lần.**

Bài 0 gọi đây là *"bài tập số 1"*, và nó vẫn là bài tập tốt nhất của cả môn: **đọc một tài liệu tài chính là
cộng lại từng cột và kiểm từng phép tính.**

---

## 10. Kiểm toàn khoá — dựng lại mọi khẳng định

Mục này **không dạy gì mới**. Nó là một **bài kiểm hồi quy**: dựng lại từng con số đầu mục mà cả khoá đã
khẳng định, từ **cùng một** bộ dữ liệu gốc. Nếu một dòng nào đó đổi, mục này đổ.

| bài | khẳng định | giá trị | |
| :---: | --- | ---: | :---: |
| 0 | bảng cân đối **cân** ở cả hai năm | 5.193 / 5.354 | ✓ |
| 2 | lợi nhuận thuần cuối cùng | 248 | ✓ |
| 3 | ba tầng lợi nhuận gộp → EBIT → thuần | 1.933 / 652 / 248 | ✓ |
| 4 | tổng tài sản 2005 *(sách in 5.133)* | **5.193** | ✓ |
| 5 | lợi nhuận giữ lại cuộn chiếu | 1.191+248−166 | ✓ |
| 6 | tiền từ HĐKD so với lợi nhuận thuần | 2,01 lần | ✓ |
| 7 | ba mục cộng lại = thay đổi tiền mặt | 11 | ✓ |
| 8 | ROE và hệ số thanh toán lãi vay | 10,1% / 3,41 | ✓ |
| 9 | DuPont đóng: biên × vòng quay = ROA | 4,78% | ✓ |
| 10 | PV / NPV ví dụ chủ đạo ch. 25 | 3.350 / 350 | ✓ |
| 11 | chu kỳ tiền mặt *(sách in 73)* | **74,1 ngày** | ✓ |
| 11 | công thức đóng cho độ lệch công thức tắt | 105,9 | ✓ |
| 🇻🇳 | bảng cân đối Vinamilk **cân** | 56.993.245 | ✓ |
| 🇻🇳 | DuPont đóng ở cả Vinamilk | 15,24% | ✓ |
| chú thích | EPS và cổ tức khớp chú thích phụ lục | 3,35 / 166 | ✓ |
| | **TẤT CẢ** | **15/15** | ✓ |

⭐ **15/15 khẳng định đầu mục của cả khoá vẫn đúng, từ MỘT bộ dữ liệu gốc** *(chốt bằng `assert` — nếu một
cái hỏng thì tệp không chạy được)*.

Đó là thứ mà ch. 31 gọi là *"hệ thần kinh"*: **mọi con số nói với mọi con số khác, và nếu một chỗ hỏng thì
chỗ khác kêu.**

Và cũng là lý do [`thuc_hanh/cong_ty_mau.py`](../thuc_hanh/cong_ty_mau.py) **tự kiểm bằng `assert` ngay khi
import**: nếu gõ y nguyên theo sách thì **bảng cân đối không cân**, và cả khoá học sẽ sụp theo.

---

## 11. 🎓 Đi tiếp từ đây

**Khoá này dạy gì, và không dạy gì.**

| có trong khoá | **không** có trong khoá |
| --- | --- |
| đọc ba báo cáo tài chính | **lập** báo cáo — bút toán, sổ cái, khoá sổ |
| hệ tỷ lệ đầy đủ + phân rã DuPont | định giá doanh nghiệp, mô hình DCF nhiều kỳ |
| ROI: hoàn vốn, NPV, IRR, độ nhạy | quyền chọn thực, phân tích rủi ro Monte Carlo |
| vốn lưu động và chu kỳ tiền mặt | quản trị kho, dự báo cầu |
| đối chiếu IFRS ↔ VAS ở mức khái niệm | **VAS chi tiết** — Thông tư 200, chuẩn mực từng khoản mục |

**Ba việc còn mở**, ghi lại để ai tiếp tục thì biết bắt đầu từ đâu:

- 🚧 **Bản VAS của Vinamilk.** Cả khoá dùng bản **IFRS**; bản VAS cho tổng tài sản khác hẳn (~55,0 nghìn tỷ
  so với 56.993). Đối chiếu tay đôi hai khung kế toán trên **cùng một doanh nghiệp, cùng một năm** sẽ là
  minh hoạ mạnh nhất cho luận điểm *"nghệ thuật tài chính"* của ch. 1–3. Chưa làm vì chưa lấy được bản VAS
  **từ nguồn gốc** — website Vinamilk trả 403 với `curl`. **Không gõ số từ báo chí:** hai bài báo đã cho hai
  con số khác nhau.
- 🚧 **Capex riêng của Vinamilk.** Bộ dữ liệu chỉ có **tổng** lưu chuyển tiền từ đầu tư, không tách chi mua
  tài sản cố định — nên **không tính được dòng tiền tự do**
  ([bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) mục 11).
- 🚧 **WACC của Vinamilk.** Đo được **chi phí nợ** (3,06%/năm, gần đúng) nhưng **không** đo được **chi phí
  vốn chủ sở hữu** — cần beta và lãi suất phi rủi ro Việt Nam, hai con số không nằm trong báo cáo tài chính
  ([bài 10](bai_10_tinh_ty_le_hoan_von_dau_tu.md) mục 11).

**Ba việc làm được ngay tuần này** — lấy thẳng từ ch. 29–30:

1. **Hỏi phòng tài chính ba câu của [mục 1](#1-vì-sao-đọc-được-báo-cáo-tài-chính-lại-đổi-cách-làm-việc).**
   Không cần chuẩn bị gì thêm.
2. **Chọn hai, ba con số** đo đơn vị bạn, và bắt đầu **chia sẻ chúng trong họp tuần** — kèm *"chúng đến từ
   đâu, tại sao chúng quan trọng, và mọi người tác động đến chúng ra sao"* ([mục 5](#5-ba-phương-pháp-xoá-mù-tài-chính-và-bản-đồ-sang-khoá-này)).
3. **Lấy báo cáo tài chính công ty bạn và cộng lại từng cột.** Đó là bài tập của
   [bài 0](bai_00_bat_dau_tu_dau.md), và [mục 9](#9-sổ-tổng-kết--mọi-chỗ-sách-in-sai) vừa cho thấy nó bắt
   được **28 chỗ** trong một cuốn sách đã qua biên tập và xuất bản.

---

## 12. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py`](../thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py) rồi
chạy lại. Không có lời giải.

1. **Ba câu hỏi của bạn.** Ở mục 1, thay ba câu hỏi của sách bằng ba câu hỏi **cho chính công ty bạn**. Mỗi
   câu ứng với bài nào trong khoá?

2. **Hai, ba con số của đơn vị bạn.** Ở mục 3, thay bốn dòng chỉ số bằng chỉ số **thật** mà đơn vị bạn bị
   đo. Với mỗi cái, viết một quyết định mà người ở tuyến đầu tự ra được nếu biết nó đang bị siết.

3. **SOX ở doanh nghiệp Việt Nam.** Ở mục 8, đổi 5 triệu đô-la thành một mức chi phí tuân thủ mà bạn cho là
   hợp lý ở Việt Nam, và dùng lợi nhuận thật của một công ty niêm yết bạn biết. Tỷ lệ ra bao nhiêu?

4. **Điểm hoà của chi phí tuân thủ.** Vẫn mục 8, tìm mức lợi nhuận thuần làm chi phí 5 triệu chiếm đúng
   **1%**. Doanh nghiệp dưới ngưỡng đó nên niêm yết không?

5. **Đổi cách phân loại lỗi.** Ở mục 9, gộp *"biên tập"* vào *"khái niệm"*. Bức tranh đổi thế nào? Cách phân
   loại nào **trung thực hơn**, và vì sao?

6. **Mật độ theo chương.** Vẫn mục 9, đếm lỗi theo **chương** thay vì theo vị trí. Chương nào đặc nhất? Nó
   có phải chương nhiều số nhất không?

7. **Thêm một khẳng định.** Ở mục 10, thêm một dòng kiểm cho một con số mà bạn thấy quan trọng nhưng chưa có
   trong bảng. Nó có qua không?

8. **Phá một con số.** Vẫn mục 10, sửa **một** số trong [`cong_ty_mau.py`](../thuc_hanh/cong_ty_mau.py) —
   ví dụ tồn kho 2005 — rồi chạy lại **toàn bộ** `thuc_hanh/*.py`. **Bao nhiêu tệp đổ?** Đó là phép đo trực
   tiếp cho ẩn dụ *"hệ thần kinh"* của ch. 31. *(Nhớ hoàn tác sau khi thử.)*

---

## 13. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Xoá mù tài chính | financial literacy | dạy người ngoài phòng tài chính đọc được báo cáo |
| Trí tuệ tài chính | financial intelligence | hiểu **cả** con số **lẫn** giả định nằm sau nó |
| Minh bạch tài chính | financial transparency | *"mục tiêu tối thượng"* — mọi người thấy các con số |
| Chỉ số hiệu quả hoạt động chính | key performance indicator (KPI) | ⚠️ sách in *"key perfomance index"* |
| Bảng điểm | scorecard | *"rõ ràng, trực diện và nằm ngay trước mắt"* |
| Sơ đồ dòng tiền | money map | công cụ trực quan: mỗi đồng doanh thu đi đâu |
| Đạo luật Sarbanes-Oxley | Sarbanes-Oxley Act (SOX) | luật Mỹ 7/2002 sau Enron / WorldCom |
| Báo cáo kiểm soát nội bộ | internal control report | mục bắt buộc thêm vào báo cáo thường niên |
| Ban kiểm soát kế toán công ty niêm yết | PCAOB | cơ quan SOX lập ra |
| 💼 Chi phí tuân thủ luỹ thoái | regressive compliance cost | chi phí cố định ⇒ **doanh nghiệp nhỏ chịu nặng hơn** |

---

## 14. Câu hỏi tự kiểm tra

1. Sách so sánh việc kinh doanh với trò chơi nào? Ý của phép so sánh đó là gì? (mục 1)
2. Kể **ba** thứ bạn có được khi nắm luật chơi. (mục 1)
3. Kể **ba câu hỏi** sách bảo mang đi hỏi phòng tài chính, và mỗi câu ứng với bài nào. (mục 1)
4. Sách dự đoán phòng tài chính phản ứng thế nào? Phần thưởng thật nằm ở vế nào? (mục 1)
5. Kể câu chuyện nhân viên bán hàng. Công ty đã đổi cơ sở trả thưởng từ gì sang gì? (mục 2)
6. Cái đắt nhất trong câu chuyện đó là gì? Nó nằm ở dòng nào trên báo cáo tài chính? (mục 2)
7. Liều thuốc giải mà sách kê cho "chính trị công sở" là gì? (mục 2)
8. Lập luận từ *Warfighting* là gì? Nó về **đạo đức** hay về **tốc độ**? (mục 3)
9. Cho một chỉ số bị siết, nêu một quyết định mà tuyến đầu tự ra được. (mục 3)
10. Trung tâm Effective Organizations đo **hai** thước đo nào? Kết quả tương quan với những gì? (mục 4)
11. Vì sao phải đọc kết quả đó là **tương quan** chứ không phải **nhân quả**? (mục 4)
12. Chuỗi nhân quả mà sách **thực sự** đề xuất là gì? (mục 4)
13. Kế toán viên của Setpoint giải thích thế nào về việc công ty trụ được? (mục 4)
14. Vì sao minh bạch còn là một **cơ chế kiểm soát**? (mục 4)
15. Vì sao xoá mù tài chính **không thể** là việc làm một lần? (mục 5)
16. Ba buổi của Joe ở Setpoint dạy gì? Chúng phủ mấy bài của khoá này? (mục 5)
17. Sách gợi ý nâng cấp gì cho buổi họp tuần với "các con số"? (mục 5)
18. Cảnh báo của sách về **đồ thị nhỏ** là gì? (mục 5)
19. Hai sơ đồ dòng tiền của công ty nọ khác nhau ở đâu? Nó ứng với trục so sánh nào của bài 8? (mục 5)
20. Kể **năm** quy tắc học của người trưởng thành. (mục 6)
21. Chỗ nào khoá này **đi ngược** quy tắc của sách, và vì sao? (mục 6)
22. Nhân viên Enron nghĩ họ đang có gì? Kết cục ra sao? (mục 7)
23. Kết luận của ch. 31 là **đạo đức** hay **thực dụng**? Trích câu. (mục 7)
24. Vì sao công ty niêm yết **không thể** cho nhân viên xem báo cáo hợp nhất thường xuyên hơn một quý một
    lần? (mục 7)
25. Ẩn dụ khép lại cả cuốn sách là gì? (mục 7)
26. Sarbanes-Oxley ra đời năm nào, vì sao? Kể **bốn** điều khoản. (mục 8)
27. Nghiên cứu Corporate Library Research Group phát hiện gì? Nó giải thích điều khoản nào? (mục 8)
28. Chi phí tuân thủ 5 triệu chiếm bao nhiêu % lợi nhuận công ty mẫu? Với công ty 25 triệu thì sao? (mục 8)
29. Vì sao chi phí tuân thủ là **luỹ thoái**? Cách đọc đúng một quy định mới là gì? (mục 8)
30. Cả cuốn sách có bao nhiêu chỗ in sai? Phân thành mấy lớp? (mục 9)
31. Lớp lỗi nào **nặng nhất**, và vì sao? (mục 9)
32. Phụ lục chiếm bao nhiêu % số trang nhưng bao nhiêu % số lỗi? Đặc gấp mấy lần? (mục 9)
33. Phát biểu **quy tắc đọc** rút ra từ phân bố lỗi. Vì sao chữ chạy ít sai hơn? (mục 9)
34. Nghịch lý khép lại cả khoá học là gì? (mục 9)
35. Mục 10 kiểm bao nhiêu khẳng định? Chuyện gì xảy ra nếu một cái hỏng? (mục 10)
36. Vì sao `cong_ty_mau.py` phải tự kiểm bằng `assert` ngay khi import? (mục 10)
37. Kể **ba** thứ khoá này **không** dạy. (mục 11)
38. Kể **ba** việc còn mở, và vì sao mỗi việc chưa làm được. (mục 11)
39. Kể **ba** việc làm được ngay tuần này. (mục 11)
40. Nếu chỉ được giữ **một** điều từ cả khoá học, bạn giữ điều gì? *(không có đáp án đúng)*

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 12 — TỔ CHỨC CÓ TRÍ TUỆ TÀI CHÍNH   ·   BÀI ĐÓNG CẢ KHOÁ            ║
║           (ch. 29–31 + hộp công cụ, PDF tr. 210–223)                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⭐ "Bạn sẽ KHÔNG BAO GIỜ chơi bóng rổ mà không tìm hiểu luật chơi;      ║
║      VẬY THÌ TẠI SAO CÔNG VIỆC KINH DOANH LẠI KHÁC?"                     ║
║     Ba câu hỏi mang đi hỏi phòng tài chính:                              ║
║       "công nhận doanh thu THẾ NÀO?"      → bài 2                        ║
║       "vì sao CHỌN khung khấu hao ĐÓ?"    → bài 3, 4                     ║
║       "vì sao DII TĂNG?"                  → bài 9, 11                    ║
║     Phần thưởng thật: giả định bị hỏi đến thì GIẢ ĐỊNH SẼ ĐỔI.           ║
║                                                                          ║
║  NHÂN VIÊN BÁN HÀNG: hoa hồng đổi từ "khi BÁN" sang "khi THU ĐƯỢC        ║
║     TIỀN" — tức từ con số KẾ TOÁN sang con số TIỀN MẶT.                  ║
║     Cái đắt nhất KHÔNG phải kế hoạch mới, mà là MỘT NĂM KHÔNG AI         ║
║     GIẢI THÍCH. Chi phí đó không nằm ở dòng nào trên báo cáo.            ║
║                                                                          ║
║  WARFIGHTING — lập luận mạnh nhất, và nó về TỐC ĐỘ không phải đạo đức:   ║
║     chỉ huy nói rõ MỤC TIÊU CHUNG, cấp dưới TỰ RA QUYẾT ĐỊNH.            ║
║     Người biết chỉ số nào đang bị siết thì không cần họp.                ║
║                                                                          ║
║  ⭐ BẰNG CHỨNG (Effective Organizations): chia sẻ thông tin + đào tạo    ║
║     "kỹ năng hiểu kinh doanh" TỶ LỆ THUẬN với năng suất, chất lượng,     ║
║     khả năng sinh lời, sự hài lòng…                                      ║
║     ⚠️ TƯƠNG QUAN, KHÔNG PHẢI NHÂN QUẢ. Sách không nói quá — người đọc   ║
║        dễ đọc quá. Chuỗi sách thực sự đề xuất:                           ║
║        hiểu số → tin tưởng ↑ → biến động nhân sự ↓ → cam kết ↑           ║
║     "khó XÀO NẤU sổ sách khi nó MỞ CHO TẤT CẢ" — minh bạch là KIỂM SOÁT. ║
║                                                                          ║
║  BA BUỔI CỦA JOE Ở SETPOINT phủ đúng SÁU bài đầu của khoá này:           ║
║     ① KQKD → bài 2–3  ② LCTT + dự án → bài 6, 7, 10  ③ BCĐKT → bài 4–5   ║
║     ⚠️ Sách: mỗi buổi 30–50 phút, MỘT khái niệm. Khoá này dài hơn nhiều  ║
║        — vì đây là TÀI LIỆU TRA CỨU, không phải giáo án. Đứng lớp thì    ║
║        theo sách: MỘT MỤC, MỘT BUỔI.                                     ║
║                                                                          ║
║  ⭐ SARBANES-OXLEY: chi phí tuân thủ 5 TRIỆU $ quy ra tỷ lệ              ║
║        lợi nhuận 25 triệu  → 20,00%       công ty mẫu 248 → 2,02%        ║
║        lợi nhuận 5.000 triệu → 0,10%                                     ║
║     ⇒ CHI PHÍ TUÂN THỦ LUỸ THOÁI. Sách đưa 5 và 30 triệu mà không nói.   ║
║     Đọc mọi quy định mới bằng cách CHIA CHO LỢI NHUẬN — "so với cái gì?" ║
║                                                                          ║
║  ⭐ SỔ TỔNG KẾT — 28 CHỖ SÁCH IN SAI                                     ║
║        số 10  ·  dấu 2  ·  KHÁI NIỆM 8 (nặng nhất)  ·  biên tập 8        ║
║     VỊ TRÍ mới là điều đáng giá:                                         ║
║        phụ lục   5 lỗi / 4 trang   = 1,25 lỗi/trang                      ║
║        cả cuốn  28 lỗi / 227 trang = 0,12 lỗi/trang   → ĐẶC GẤP 10 LẦN   ║
║     ⇒ QUY TẮC ĐỌC: lỗi tập trung ở chỗ NHIỀU SỐ, ÍT CHỮ — phụ lục, ô     ║
║       công thức, bảng biểu. Không ai đọc lại thành câu nên không ai      ║
║       nghe thấy nó sai.                                                  ║
║     ⭐ NGHỊCH LÝ: cuốn sách nói "ĐỪNG TIN CÁC CON SỐ" — và tự chứng      ║
║        minh luận điểm đó 28 LẦN.                                         ║
║                                                                          ║
║  ⭐ KIỂM TOÀN KHOÁ: 15/15 khẳng định đầu mục của 12 bài vẫn đúng,        ║
║     dựng lại từ MỘT bộ dữ liệu gốc. Đó là "HỆ THẦN KINH" của ch. 31:     ║
║     mọi con số nói với mọi con số khác — một chỗ hỏng thì chỗ khác kêu.  ║
║                                                                          ║
║  🎓 "THÔNG TIN TÀI CHÍNH LÀ HỆ THẦN KINH của bất kỳ doanh nghiệp nào…    ║
║      TỪ QUÁ LÂU, ở mỗi doanh nghiệp CHỈ CÓ MỘT NHÓM là những người       ║
║      duy nhất hiểu dữ liệu tài chính nói gì."                — ch. 31    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần VIII — Xây dựng bộ phận (và tổ chức) có trí tuệ tài chính**, trang tiêu đề PDF tr. 209.
    ⚠️ Bản dịch in **"PHẦN VII"**.
    - Ch. 29 *Xoá mù tài chính và hiệu quả hoạt động của doanh nghiệp*, PDF tr. 210–215
      — ⭐ *"bóng rổ hay cờ thỏ cáo"*, *"phần nào phản ánh hiện thực"*, **ba câu hỏi cho phòng tài chính**
      và *"cơn choáng váng"* (tr. 210); **NHỮNG DOANH NGHIỆP TỐT HƠN** và ⭐ **câu chuyện nhân viên bán
      hàng** (tr. 211); chính trị công sở và *"ánh sáng mặt trời, sự minh bạch và truyền thông mở"*,
      ⭐ ***Warfighting*** (tr. 212); *"nói rõ mục tiêu chung"*, *"không thể tham vấn cấp cao hơn"* và
      **ĐƯA TRÍ TUỆ TÀI CHÍNH XUỐNG HÀNG NGŨ QUÂN LÍNH** (tr. 213); **KPI**, ⭐ **nghiên cứu Effective
      Organizations**, Denison / Drucker / Pfeffer (tr. 214); 💼 **kế toán viên của Setpoint** và
      ⭐ *"khó xào nấu sổ sách khi nó mở cho tất cả"* (tr. 215)
    - Ch. 30 *Các chiến lược xoá mù tài chính*, PDF tr. 216–220
      — *"không thể chỉ tổ chức một lần rồi thôi"*, **CÔNG CỤ VÀ KỸ THUẬT**, ⭐ **ba buổi 30–50 phút của
      Joe ở Setpoint** (tr. 216); **họp tuần với "các con số"**, *"đặt cược uy tín"*, **bảng điểm**
      (tr. 217); **Sơ đồ dòng tiền** (Hình 30-1), cảnh báo về *"đồ thị nhỏ"*, 💼 **hai sơ đồ mục tiêu / thật**
      (tr. 218); ⭐ **năm quy tắc học của người trưởng thành** (tr. 219); *"đừng cố biến họ thành kế toán
      viên"* và 📚 **câu chuyện "đối tác kinh doanh"** (tr. 220)
    - Ch. 31 *Minh bạch tài chính: mục tiêu tối thượng*, PDF tr. 221–222
      — ⭐ **Enron nhìn từ phía nhân viên**, *"401(k)"*, *"vật vờ ra đường xin việc"*, và giới hạn *"một lần
      mỗi quý"* (tr. 221); ⭐ **câu kết: *"thông tin tài chính là hệ thần kinh"*** (tr. 222)
    - **Hộp công cụ** *Hiểu đạo luật Sarbanes-Oxley*, PDF tr. 222–223
      — bối cảnh 7/2002 và *"thập niên 1930"* (tr. 222); **các điều khoản**, 📚 **nghiên cứu Corporate
      Library Research Group — 4,5 tỷ đô-la cho nhà điều hành vay năm 2001**, và ⚠️ **chi phí tuân thủ
      5 triệu / 30 triệu đô-la** (tr. 223)
  - Phụ lục, PDF tr. 224–227 — công ty mẫu, dùng ở [mục 8](#8--hộp-công-cụ--sarbanes-oxley-và-cái-giá-quy-ra-tỷ-lệ)
    và [mục 10](#10-kiểm-toàn-khoá--dựng-lại-mọi-khẳng-định)
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py`](../thuc_hanh/bai-12-to-chuc-co-tri-tue-tai-chinh.py):
  - chi phí tuân thủ 5 triệu đô-la đè lên doanh nghiệp lợi nhuận 25 triệu **nặng hơn tám lần** so với công
    ty mẫu — chốt bằng `assert`;
  - mật độ lỗi ở **phụ lục** **cao hơn tám lần** mật độ trung bình của cả cuốn *(thực tế: 11 lần)* — chốt
    bằng `assert`;
  - **cả 15 khẳng định đầu mục** của 12 bài đều dựng lại được từ một bộ dữ liệu gốc — chốt bằng `assert`
    *(tệp không chạy được nếu một cái hỏng)*.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** bốn tình huống *"chỉ số bị siết → quyết định"* ở mục
  3; bản đồ ba buổi của Joe sang các bài của khoá ở mục 5; bảng đối chiếu năm quy tắc học với cách khoá này
  được dựng ở mục 6; dải lợi nhuận 25–5.000 triệu ở mục 8; **toàn bộ cách phân loại và đếm lỗi** ở mục 9
  *(sách không tự kiểm)*; toàn bộ mục 10 và 11. Mọi con số **của sách** đều được trích kèm mốc
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
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| **12** | **Tổ chức có trí tuệ tài chính** ← *bạn đang ở đây* | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
