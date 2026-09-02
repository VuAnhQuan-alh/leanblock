# Bài 10 — Lý thuyết lựa chọn của người tiêu dùng

> Bài học dựng từ **Chương 21 — Lý thuyết về sự lựa chọn của người tiêu dùng** (tr. 495–524)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🎯 **Vòng 1.** Chín bài trước đều dùng đường cầu dốc xuống như một **dữ kiện cho sẵn**.
> Bài này mở nắp ra xem bên dưới có gì — và phát hiện rằng đường cầu không phải giả định,
> nó **rơi ra** từ một bài toán tối ưu hoá có ràng buộc.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nêu kết quả mà không chứng minh, hoặc vẽ mà không nói ra giả định.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ mô hình trong bài **không** khớp hình vẽ của sách.
> 📌 **Cần đọc trước:** [Bài 2](bai_02_cung_va_cau.md) và
> [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) — bài này chứng minh hai thứ mà hai bài đó
> chỉ nêu ra: **vì sao cầu dốc xuống** và **độ co giãn đến từ đâu**.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Câu hỏi mà chín bài trước đã lặng lẽ giả định câu trả lời](#1-câu-hỏi-mà-chín-bài-trước-đã-lặng-lẽ-giả-định-câu-trả-lời)
- [2. Đường ràng buộc ngân sách](#2-đường-ràng-buộc-ngân-sách)
- [3. Đường bàng quan và tỷ lệ thay thế biên](#3-đường-bàng-quan-và-tỷ-lệ-thay-thế-biên)
- [4. Bốn tính chất của đường bàng quan](#4-bốn-tính-chất-của-đường-bàng-quan)
- [5. Hai trường hợp đặc biệt](#5-hai-trường-hợp-đặc-biệt)
- [6. Điểm tối ưu — nơi hai đường tiếp tuyến nhau](#6-điểm-tối-ưu--nơi-hai-đường-tiếp-tuyến-nhau)
- [7. 📚 Độ thoả dụng — cách nói thứ hai cho cùng một điều](#7--độ-thoả-dụng--cách-nói-thứ-hai-cho-cùng-một-điều)
- [8. Thu nhập tăng — hàng hoá thông thường và hàng hoá thứ cấp](#8-thu-nhập-tăng--hàng-hoá-thông-thường-và-hàng-hoá-thứ-cấp)
- [9. Giá đổi — tách tác động thu nhập và tác động thay thế](#9-giá-đổi--tách-tác-động-thu-nhập-và-tác-động-thay-thế)
- [10. Dựng đường cầu từ các điểm tối ưu](#10-dựng-đường-cầu-từ-các-điểm-tối-ưu)
- [11. 📚 Độ cong của đường bàng quan quyết định mọi thứ còn lại](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại)
- [12. Có phải mọi đường cầu đều dốc xuống?](#12-có-phải-mọi-đường-cầu-đều-dốc-xuống)
- [13. Nghiên cứu tình huống — cuộc tìm kiếm hàng hoá Giffen](#13-nghiên-cứu-tình-huống--cuộc-tìm-kiếm-hàng-hoá-giffen)
- [14. Lương tăng thì làm việc nhiều hơn hay ít hơn?](#14-lương-tăng-thì-làm-việc-nhiều-hơn-hay-ít-hơn)
- [15. Nghiên cứu tình huống — người trúng số và phán đoán của Carnegie](#15-nghiên-cứu-tình-huống--người-trúng-số-và-phán-đoán-của-carnegie)
- [16. Lãi suất tăng thì tiết kiệm nhiều hơn hay ít hơn?](#16-lãi-suất-tăng-thì-tiết-kiệm-nhiều-hơn-hay-ít-hơn)
- [17. Con người có thực sự nghĩ theo hướng này không?](#17-con-người-có-thực-sự-nghĩ-theo-hướng-này-không)
- [18. 💼 Chia ngân sách marketing bằng đúng quy tắc của mục 6](#18--chia-ngân-sách-marketing-bằng-đúng-quy-tắc-của-mục-6)
- [19. Code minh hoạ](#19-code-minh-hoạ)
- [20. Tự thử](#20-tự-thử)
- [21. Từ điển thuật ngữ](#21-từ-điển-thuật-ngữ)
- [22. Câu hỏi tự kiểm tra](#22-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Câu hỏi mà chín bài trước đã lặng lẽ giả định câu trả lời

Sách mở chương bằng một câu rất khiêm tốn (tr. 495):

> *"Đến phần này của cuốn sách, chúng ta đã tổng kết những hành vi của người tiêu dùng với đường cầu…
> Bây giờ chúng ta sẽ phân tích sâu hơn vào những quyết định ẩn sau đường cầu."*

Và nói rõ chương này là **cặp đối xứng** của chương 14:

> *"Lý thuyết sự lựa chọn của người tiêu dùng được giới thiệu trong chương này cung cấp một sự hiểu
> biết toàn diện hơn về cầu, giống như lý thuyết về các công ty cạnh tranh ở Chương 14 cung cấp những
> hiểu biết hoàn chỉnh hơn về cung."*

|                            | Phía cung                                         | Phía cầu                          |
| -------------------------- | ------------------------------------------------- | --------------------------------- |
| Cái được cho sẵn ở bài đầu | đường cung dốc lên                                | đường cầu dốc xuống               |
| Bài mở nắp                 | [Bài 6](bai_06_thi_truong_canh_tranh.md) (ch. 14) | **Bài này** (ch. 21)              |
| Thứ tìm thấy bên dưới      | `P = MC`, và đường cung **chính là** đường MC     | ràng buộc ngân sách + sự ưa thích |

Sách hứa trả lời **ba câu hỏi** (tr. 496), và thoạt nghe chúng chẳng liên quan gì tới nhau:

> - *Có phải mọi đường cầu đều dốc xuống không?*
> - *Mức lương ảnh hưởng đến cung lao động như thế nào?*
> - *Lãi suất ảnh hưởng tiết kiệm của hộ gia đình như thế nào?*
>
> *"Ban đầu những câu hỏi này có vẻ không liên quan với nhau. Nhưng rồi chúng ta sẽ thấy, chúng ta có
> thể dùng lý thuyết về sự lựa chọn của người tiêu dùng để trả lời từng câu một."*

Ba câu trả lời nằm ở [mục 12](#12-có-phải-mọi-đường-cầu-đều-dốc-xuống), [mục 14](#14-lương-tăng-thì-làm-việc-nhiều-hơn-hay-ít-hơn)
và [mục 16](#16-lãi-suất-tăng-thì-tiết-kiệm-nhiều-hơn-hay-ít-hơn) của bài này. Và [mục 11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại)
sẽ cho thấy **cả ba đều là cùng một câu hỏi**, hỏi ba lần bằng ba bộ từ vựng khác nhau — điều mà
sách không nói ra.

---

## 2. Đường ràng buộc ngân sách

Sách giữ mọi thứ ở mức nhỏ nhất có thể: **hai** hàng hoá, pizza và Pepsi (tr. 496).

> *"Giả sử người tiêu dùng có mức thu nhập 1.000 đô la mỗi tháng và anh ta tiêu hết thu nhập của mình
> vào pizza và Pepsi. Giá của một chiếc pizza là 10 đô la và giá của một chai Pepsi là 2 đô la."*

Định nghĩa ở chân trang 497:

> **Ràng buộc về ngân sách** *(budget constraint)*: giới hạn về gói hàng hoá mà người tiêu dùng có thể
> chi trả.

**Hình 1, tr. 497** in 11 dòng. Nhưng nhìn hai cột đầu là thấy ngay nó chỉ là một **phương trình bậc nhất**:

$$10 \times \text{pizza} + 2 \times \text{Pepsi} = 1000$$

Code ở [mục 19](#19-code-minh-hoạ) dựng lại cả bảng và kiểm **11/11 dòng khớp**. Cột "Tổng" bằng đúng
$1.000 ở mọi dòng — đó chính là ý nghĩa của chữ *ràng buộc*.

### Độ dốc là giá tương đối

Sách tính độ dốc theo hai cách và thu về cùng một con số (tr. 497):

> *"Từ điểm A đến điểm B, khoảng thay đổi trên trục tung là 500 chai Pepsi, và sự thay đổi trên trục
> hoành là 100 chiếc pizza. Vì vậy, độ dốc là 5 chai Pepsi trên 1 chiếc pizza."*
>
> *"Ghi nhớ rằng độ dốc của đường ràng buộc ngân sách bằng mức **giá tương đối** của hai hàng hóa."*

$$\frac{500 \text{ chai}}{100 \text{ chiếc}} = 5 \qquad\text{và}\qquad \frac{\$10}{\$2} = 5$$

Đây là chỗ **chi phí cơ hội** của [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md) xuất hiện lại
dưới dạng hình học: chi phí cơ hội của một chiếc pizza **là** 5 chai Pepsi, và nó **là** độ dốc.

⚠️ Một điểm dễ trượt: đường ngân sách nói **bạn mua được gì**, không nói **bạn muốn gì**. Nó là nửa
bài toán. Nửa còn lại ở mục sau.

---

## 3. Đường bàng quan và tỷ lệ thay thế biên

Định nghĩa ở chân trang 498:

> **Đường bàng quan** *(indifference curve)*: đường biểu diễn những gói hàng hoá đem lại **cùng một
> mức độ thoả mãn**.

Và độ dốc của nó có tên riêng (tr. 498–499):

> **Tỷ lệ thay thế biên** *(marginal rate of substitution, MRS)*: tỷ lệ mà theo đó người tiêu dùng
> sẵn lòng đánh đổi một hàng hoá để lấy một hàng hoá khác.

⚠️ **Hai độ dốc, đừng lẫn.** Cả đường ngân sách lẫn đường bàng quan đều dốc xuống, và cả hai độ dốc
đều là "bao nhiêu Pepsi đổi một pizza". Nhưng chúng trả lời hai câu khác nhau:

| Đường               | Độ dốc là                                              | Ai quyết định    |
| ------------------- | ------------------------------------------------------ | ---------------- |
| Ràng buộc ngân sách | giá tương đối — **thị trường** cho đổi ở tỷ lệ nào     | thị trường       |
| Bàng quan           | tỷ lệ thay thế biên — **bạn** sẵn lòng đổi ở tỷ lệ nào | sở thích của bạn |

Sách viết rõ chỗ này ở tr. 503: *"Giá tương đối là tỷ lệ mà **thị trường** sẵn lòng trao đổi hàng hóa
này lấy hàng hóa khác trong khi tỷ lệ thay thế biên là tỷ lệ mà **người tiêu dùng** sẵn lòng trao đổi."*

### Một hàm cụ thể, vì sách không cho

Sách chỉ vẽ hình. Để tính được, bài này chọn hàm gọn nhất có đủ bốn tính chất mà sách liệt kê:

$$U = \text{pizza} \times \text{Pepsi}$$

Từ đó $MRS = \dfrac{\text{Pepsi}}{\text{pizza}}$. Đi dọc đường bàng quan $U = 12.500$:

| Pizza | Pepsi |     MRS | Đọc là                                             |
| ----: | ----: | ------: | -------------------------------------------------- |
|    10 | 1.250 | **125** | ít pizza → đòi rất nhiều Pepsi mới chịu bỏ 1 chiếc |
|    25 |   500 |      20 |                                                    |
|    50 |   250 |       5 | vùng giữa                                          |
|   100 |   125 |     5/4 |                                                    |
|   125 |   100 | **4/5** | nhiều pizza → bỏ 1 chiếc chỉ cần ít Pepsi          |

MRS **giảm đơn điệu** từ 125 xuống 0,8 khi đi sang phải. Sách giải thích bằng một câu rất đời thường
(tr. 500):

> *"con người thường sẵn lòng trao đổi hàng hóa mà họ có nhiều và ít sẵn lòng đánh đổi hàng hóa mà
> họ có ít hơn."*

**Hình 4, tr. 501** minh hoạ đúng điều này bằng hai điểm:

> *"Tại điểm A, vì người tiêu dùng có quá nhiều Pepsi và chỉ có một ít pizza, anh ta đang đói và không
> quá khát. Để khiến người tiêu dùng từ bỏ 1 chiếc pizza, anh ta phải được thêm đi **6 chai Pepsi**…
> Ở điểm B, anh ta sẵn lòng cho đi 1 chiếc pizza để có được **1 chai Pepsi**."*

---

## 4. Bốn tính chất của đường bàng quan

Sách liệt kê bốn (tr. 499–500). Kiểm từng cái bằng số, với $U = \text{pizza} \times \text{Pepsi}$:

| #   | Tính chất                                   | Kiểm                                                                                          |
| --- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 1   | *Đường bàng quan cao hơn được ưa thích hơn* | tại pizza = 50, đường $U$=25.000 cho **500** chai còn $U$=12.500 cho **250**. Nhiều hơn thật. |
| 2   | *Đường bàng quan có hướng dốc xuống*        | pizza 10 → 125 thì Pepsi 1.250 → 100. Một lên thì một xuống.                                  |
| 3   | *Đường bàng quan không cắt nhau*            | nếu tại một điểm vừa có $xy = 12.500$ vừa có $xy = 25.000$ thì $12.500 = 25.000$. Vô lý.      |
| 4   | *Đường bàng quan cong về gốc toạ độ*        | bảng MRS ở mục 3.                                                                             |

Tính chất 3 đáng dừng lại, vì lập luận của sách là một phép **phản chứng** rất sạch (tr. 500, Hình 3):

> *"vì điểm A nằm cùng đường bàng quan với điểm B, hai điểm này khiến người tiêu dùng thỏa mãn như
> nhau. Bên cạnh đó, vì điểm B nằm trên cùng đường bàng quan với điểm C, hai điểm này cũng làm người
> tiêu dùng thỏa mãn như nhau. Hai kết luận trên dẫn tới việc các điểm A và C làm người tiêu dùng thỏa
> mãn tương đương nhau **dù cho ở điểm C, lượng hàng hóa tiêu dùng là lớn hơn**. Điều này trái ngược
> với giả định của chúng ta."*

Nói gọn: **nếu bàng quan là bắc cầu, và nhiều hơn thì tốt hơn, thì hai đường không thể cắt.** Hai giả
định rất nhẹ, một kết luận rất chặt.

---

## 5. Hai trường hợp đặc biệt

Sách đưa hai thái cực (tr. 501–502) — và chúng quan trọng hơn vẻ ngoài, vì [mục 11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại)
sẽ cho thấy **mọi trường hợp thực tế nằm giữa hai cái này**, và vị trí đó quyết định gần như tất cả.

### (a) Thay thế hoàn hảo — đồng 5 cent và đồng 10 cent

> **Hàng hoá thay thế hoàn hảo** *(perfect substitutes)*: hai hàng hoá có những đường bàng quan **thẳng**.

Bạn chỉ quan tâm tổng số tiền, nên luôn sẵn lòng đổi 2 đồng 5 cent lấy 1 đồng 10 cent, **bất kể** đang
có bao nhiêu. MRS = 2 ở mọi điểm → đường bàng quan là đường thẳng.

### (b) Bổ sung hoàn hảo — giày trái và giày phải

> **Hàng hoá bổ sung hoàn hảo** *(perfect complements)*: hai hàng hoá có những đường bàng quan **vuông góc**.

| Trái | Phải | Số đôi |                       |
| ---: | ---: | -----: | --------------------- |
|    5 |    5 |      5 | vừa đủ                |
|    5 |    7 |      5 | thừa 2 chiếc, vô dụng |
|    7 |    5 |      5 | thừa 2 chiếc, vô dụng |

Ba gói này **bàng quan** với nhau. Sách viết: *"Có thêm một chiếc bên phải lúc này chả có ý nghĩa gì
nếu không có một chiếc bên trái đi kèm."*

Và sách thừa nhận thực tế nằm ở giữa (tr. 502):

> *"Thông thường, các đường bàng quan có dạng cong về gốc tọa độ, nhưng không cong đến nỗi tạo thành
> dạng vuông góc."*

---

## 6. Điểm tối ưu — nơi hai đường tiếp tuyến nhau

Ghép hai nửa lại. Người tiêu dùng muốn lên **đường bàng quan cao nhất** mà **vẫn nằm trên đường ngân
sách**. Chỗ đó là chỗ hai đường **chạm nhau mà không cắt nhau** (tr. 503).

Với $U = \text{pizza} \times \text{Pepsi}$, điểm tối ưu là **50 chiếc pizza và 250 chai Pepsi** — chi
đúng $500 cho mỗi loại.

Đó **chính là điểm C trên Hình 1** của sách, điểm mà tr. 496 mô tả là *"người tiêu dùng chi tiêu những
khoản bằng nhau (500 đô la) cho hai mặt hàng pizza và Pepsi"*.

Kiểm điều kiện tiếp tuyến:

$$\underbrace{MRS = \frac{250}{50} = 5}_{\text{độ dốc đường bàng quan}} \qquad=\qquad \underbrace{\frac{P_{\text{pizza}}}{P_{\text{Pepsi}}} = \frac{10}{2} = 5}_{\text{độ dốc đường ngân sách}}$$

Sách in kết luận này nghiêng ở tr. 503:

> *"người tiêu dùng sẽ quyết định tiêu dùng hai hàng hóa sao cho **tỷ lệ thay thế biên bằng với giá
> tương đối** của chúng."*

Và rút ra một hệ quả rất đẹp, nối thẳng về [bài 4](bai_04_thang_du_va_chi_phi_cua_thue.md) (tr. 503):

> *"Ở điểm tối ưu cho người tiêu dùng, sự đánh giá của người tiêu dùng với hai hàng hóa (đo bằng tỷ lệ
> thay thế biên) bằng với sự đánh giá của thị trường (đo bằng giá tương đối). Kết quả của sự tối ưu hóa
> này là **giá thị trường của những hàng hóa khác nhau phản ánh giá trị mà người tiêu dùng đánh giá chúng**."*

Hai điểm sách vẽ để đối chiếu ở Hình 6:

- Một điểm **thích hơn nhưng không với tới** — nằm trên đường ngân sách.
- Một điểm **đủ tiền nhưng thoả dụng thấp hơn** — nằm dưới đường ngân sách.

Điểm tối ưu là chỗ duy nhất không mắc lỗi nào trong hai lỗi đó.

---

## 7. 📚 Độ thoả dụng — cách nói thứ hai cho cùng một điều

Hộp *"Bạn có biết"* ở tr. 504 làm một việc rất đáng giá: dịch toàn bộ hình học ở trên sang một ngôn
ngữ khác, rồi chứng minh hai ngôn ngữ nói cùng một điều.

> **Độ thoả dụng biên** *(marginal utility)*: sự tăng lên trong mức thoả dụng mà người tiêu dùng nhận
> được từ một đơn vị tăng thêm của hàng hoá đó.

Chuỗi ba bước của sách:

$$MRS = \frac{P_X}{P_Y} \quad\Longrightarrow\quad \frac{MU_X}{MU_Y} = \frac{P_X}{P_Y} \quad\Longrightarrow\quad \boxed{\frac{MU_X}{P_X} = \frac{MU_Y}{P_Y}}$$

Với $U = xy$ thì $MU_{\text{pizza}} = \text{Pepsi}$ và $MU_{\text{Pepsi}} = \text{pizza}$. Tại điểm
tối ưu (50, 250):

$$\frac{MU_{\text{pizza}}}{P_{\text{pizza}}} = \frac{250}{10} = 25 \qquad \frac{MU_{\text{Pepsi}}}{P_{\text{Pepsi}}} = \frac{50}{2} = 25$$

Bằng nhau. Sách diễn giải (tr. 504):

> *"Tại điểm tối ưu, mức thỏa dụng biên của một đô la tiêu dùng trên hàng hóa X bằng với độ thỏa dụng
> biên của một đô la tiêu dùng trên hàng hóa Y. **Tại sao?** Nếu hai vế của đẳng thức này không bằng
> nhau, người tiêu dùng có thể tăng độ thỏa dụng bằng cách chi tiêu ít hơn cho hàng hóa mang lại độ
> thỏa dụng biên trên một đô la thấp hơn và chi tiêu nhiều hơn cho hàng hóa mang lại độ thỏa dụng biên
> trên một đô la cao hơn."*

Đọc câu đó chậm, vì nó là **thuật toán**, không phải mô tả: *chừng nào một đồng ở chỗ này còn đáng giá
hơn một đồng ở chỗ kia, hãy chuyển tiền sang — và dừng đúng lúc hai bên bằng nhau.*

[Mục 18](#18--chia-ngân-sách-marketing-bằng-đúng-quy-tắc-của-mục-6) dùng nguyên văn quy tắc này cho một
bài toán chia ngân sách thật.

Sách đóng hộp bằng một nhận xét về phương pháp mà đáng nhớ:

> *"Một nhà kinh tế có thể phát biểu rằng mục đích của tiêu dùng là để tối đa hóa độ thỏa dụng. Nhà
> kinh tế khác có thể nói rằng mục đích của người tiêu dùng là được ở trên đường bàng quan cao nhất có
> thể… **Về bản chất, hai cách nói đó là một.**"*

---

## 8. Thu nhập tăng — hàng hoá thông thường và hàng hoá thứ cấp

Thu nhập tăng đẩy đường ngân sách **song song ra ngoài** — giá không đổi nên độ dốc vẫn là 5 (Hình 7,
tr. 505):

| Thu nhập | Pizza | Pepsi |
| -------: | ----: | ----: |
|   $1.000 |    50 |   250 |
|   $1.200 |    60 |   300 |
|   $1.500 |    75 |   375 |
|   $2.000 |   100 |   500 |

Hai định nghĩa ở chân trang 505:

> **Hàng hoá thông thường** *(normal good)*: thu nhập tăng dẫn đến gia tăng lượng cầu.
> **Hàng hoá thứ cấp** *(inferior good)*: thu nhập tăng làm **giảm** lượng cầu.

Ví dụ sách đưa ở tr. 506: **các chuyến xe buýt**. *"Khi thu nhập tăng lên, những người tiêu dùng thường
sẽ mua xe hơi hoặc đi taxi và ít khi đi xe buýt."*

⚠️ **Chỗ mô hình trong bài không làm được.** Hàm $U = \text{pizza} \times \text{Pepsi}$ **không bao giờ**
tạo ra hàng hoá thứ cấp — nó luôn cho cả hai tăng theo thu nhập. Hình 8 của sách vẽ trường hợp ngược
lại, và để dựng được nó thì phải đổi sang một dạng sở thích khác. [Mục 12](#12-có-phải-mọi-đường-cầu-đều-dốc-xuống)
dùng đúng một dạng như vậy.

Đây không phải khiếm khuyết cần giấu — nó là thông tin: **hàng hoá thứ cấp đòi hỏi một cấu trúc sở
thích đặc biệt hơn hàng hoá thông thường.** Trường hợp chung là thông thường.

---

## 9. Giá đổi — tách tác động thu nhập và tác động thay thế

Giá Pepsi giảm từ $2 xuống $1 (tr. 506). Đường ngân sách **xoay** thay vì dịch song song: điểm mút
phía pizza không đổi (nếu tiêu hết vào pizza thì giá Pepsi không liên quan), còn điểm mút phía Pepsi
đi từ 500 lên 1.000 chai.

Sách cho người tiêu dùng nói hai câu, và cả hai đều có lý (tr. 507):

> - *"Tin tốt lành! Giờ thì Pepsi đã rẻ hơn, thu nhập của tôi có sức mua lớn hơn. Tôi thực sự đã giàu
>   hơn trước. Vì thế, tôi có thể mua nhiều pizza hơn và cả nhiều Pepsi hơn."* → **tác động thu nhập**
> - *"Giờ giá của Pepsi đã giảm, tôi sẽ có được nhiều chai Pepsi hơn cho mỗi chiếc pizza mà tôi không
>   tiêu dùng. Vì lúc này pizza đắt lên một cách tương đối, tôi nên mua ít pizza và nhiều Pepsi hơn."*
>   → **tác động thay thế**

Định nghĩa ở chân trang 507:

> **Tác động thu nhập** *(income effect)*: thay đổi trong tiêu dùng do thay đổi về giá làm người tiêu
> dùng dịch chuyển đến một đường bàng quan **cao hơn hoặc thấp hơn**.
> **Tác động thay thế** *(substitution effect)*: thay đổi trong tiêu dùng do thay đổi về giá làm người
> tiêu dùng dịch chuyển **dọc theo** đường bàng quan đến một điểm có tỷ lệ thay thế biên khác.

Code tách bằng ba bước:

| Bước                                |     Pizza |    Pepsi | Thu nhập |
| ----------------------------------- | --------: | -------: | -------: |
| **A.** Ban đầu                      |        50 |      250 |   $1.000 |
| **B.** Chỉ đổi giá, bù lại thu nhập |      37,5 |      375 |     $750 |
| **C.** Trả lại phần thu nhập đã bù  |        50 |      500 |   $1.000 |
| **A → B** tác động **thay thế**     | **−12,5** | **+125** |          |
| **B → C** tác động **thu nhập**     | **+12,5** | **+125** |          |
| **A → C** tổng                      |     **0** | **+250** |          |

⚠️ **Một khác biệt kỹ thuật cần nói rõ.** Sách tách bằng cách giữ nguyên **độ thoả mãn** (đi dọc đường
bàng quan cũ) — cách này mang tên **Hicks**. Code giữ nguyên **sức mua của giỏ hàng cũ** — cách này
mang tên **Slutsky**, và được chọn vì nó cho ra số hữu tỉ thay vì căn bậc hai. Hai cách cho kết quả
gần nhau và **luôn cùng dấu**, nên mọi kết luận định tính của sách vẫn đúng nguyên.

Đối chiếu với **Bảng 1, tr. 508** — sách kết luận bằng lời, đây là bảng số:

| Hàng hoá  | Thay thế | Thu nhập |     Tổng | Sách viết                                                                         |
| --------- | -------: | -------: | -------: | --------------------------------------------------------------------------------- |
| **Pepsi** |     +125 |     +125 | **+250** | *"xảy ra theo cùng chiều hướng, vì vậy người tiêu dùng sẽ mua nhiều Pepsi hơn"* ✓ |
| **Pizza** |    −12,5 |    +12,5 |    **0** | *"tổng tác động lên tiêu dùng pizza là **không rõ ràng**"* ✓                      |

Sách nói *"không rõ ràng"*, và ở đây hai tác động **triệt tiêu nhau hoàn toàn**. Đó không phải tình cờ,
và [mục 11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại) giải thích vì sao.

---

## 10. Dựng đường cầu từ các điểm tối ưu

Đây là chỗ trả nợ cho [bài 2](bai_02_cung_va_cau.md). Đường cầu **không phải một giả định** — nó là
**tập hợp các điểm tối ưu** khi cho giá chạy (Hình 11, tr. 509):

| Giá Pepsi | Pizza | Pepsi | Chi cho Pepsi |
| --------: | ----: | ----: | ------------: |
|        $5 |    50 |   100 |          $500 |
|        $4 |    50 |   125 |          $500 |
|     $2,50 |    50 |   200 |          $500 |
|        $2 |    50 |   250 |          $500 |
|     $1,25 |    50 |   400 |          $500 |
|        $1 |    50 |   500 |          $500 |

Ba điều bảng này nói ngay:

1. **Giá xuống thì lượng lên.** Đường cầu dốc xuống — không giả định gì cả, nó rơi ra từ bản thân việc
   tối ưu hoá. Đó là câu trả lời cho món nợ mở đầu bài.
2. **Lượng pizza không đổi** đúng 50 chiếc ở mọi mức giá Pepsi.
3. **Chi tiêu cho Pepsi không đổi** đúng $500 → độ co giãn bằng **1 chẵn**.

Sách viết rất đúng về vị trí của lý thuyết này (tr. 509–510):

> *"Không cần thiết phải có một khung phân tích chính xác chỉ để kết luận rằng con người phản ứng với
> những thay đổi trong giá cả."*

### ⚠️ Chỗ mô hình không khớp hình vẽ của sách

Hình 11 của sách ghi: giá $2 → $1 thì Pepsi đi từ **250 lên 750** chai. Mô hình trong bài cho **250 lên
500**. **Không khớp** — và chỗ lệch này là chỗ học được nhiều nhất trong cả bài.

Lý do rất cụ thể: hàm $U = xy$ luôn giữ chi tiêu cho mỗi mặt hàng ở đúng **một nửa** thu nhập, nên khi
giá giảm một nửa, lượng chỉ có thể **gấp đôi** — không thể gấp ba. Muốn ra 750, hai mặt hàng phải
**thay thế cho nhau dễ hơn**, tức là đường bàng quan phải **thẳng hơn**.

Nói cách khác: **hoạ sĩ vẽ Hình 11 đã ngầm chọn một giả định mà sách không nói ra ở đâu cả.** Mục sau
đo giả định đó.

---

## 11. 📚 Độ cong của đường bàng quan quyết định mọi thứ còn lại

Ở [mục 5](#5-hai-trường-hợp-đặc-biệt), sách đưa hai thái cực — thay thế hoàn hảo (thẳng) và bổ sung
hoàn hảo (vuông góc) — rồi bỏ đó. Nhưng giữa hai thái cực ấy có một **thang đo liên tục**, và nó có
tên: **độ co giãn thay thế**, ký hiệu $\sigma$.

| $\sigma$ | Đường bàng quan | Hai hàng hoá                      |
| -------: | --------------- | --------------------------------- |
|        0 | vuông góc       | bổ sung hoàn hảo — Hình 5(b)      |
|        1 | vừa phải        | $U = xy$, hàm dùng ở các mục trên |
|  2, 3, … | thẳng dần       | càng dễ thay thế                  |
| $\infty$ | thẳng           | thay thế hoàn hảo — Hình 5(a)     |

Hiệu chỉnh mỗi trường hợp sao cho **điểm xuất phát vẫn đúng là (50 pizza, 250 Pepsi)** — chỉ đổi độ
cong, không đổi gì khác — rồi cho giá Pepsi giảm từ $2 xuống $1:

| $\sigma$ | Pepsi khi giá $2 | Pepsi khi giá $1 |
| -------: | ---------------: | ---------------: |
|        0 |              250 |             333⅓ |
|        1 |              250 |              500 |
|        2 |              250 |             666⅔ |
|        3 |              250 |              800 |

Con số **750** của sách nằm giữa $\sigma = 2$ và $\sigma = 3$. Giải ngược:

$$\frac{1000}{1 + 2^{\,1-\sigma}} = 750 \;\Longrightarrow\; 2^{\,1-\sigma} = \frac13 \;\Longrightarrow\; \sigma = 1 + \log_2 3 \approx 2{,}585$$

**Hình 11 của sách được vẽ với giả định ngầm rằng pizza và Pepsi thay thế cho nhau dễ gấp khoảng 2,6
lần mức trung gian.** Giả định đó không xuất hiện trong bất kỳ câu chữ nào của chương — nó nằm trong
độ cong mà hoạ sĩ đã vẽ.

### Và đây là cây cầu về bài 3

Với hai hàng hoá thuộc họ này, độ co giãn của cầu theo giá tại điểm mà hàng hoá chiếm tỷ phần $s$ của
chi tiêu là:

$$|e| = \sigma\,(1-s) + s$$

Tại điểm xuất phát, Pepsi chiếm $s = \tfrac12$:

| $\sigma$ | $\|e\|$ |                    |
| -------: | ------: | ------------------ |
|        0 |     1/2 | không co giãn      |
|        1 |   **1** | **co giãn đơn vị** |
|        2 |     3/2 | co giãn            |
|        3 |       2 | co giãn            |

$\sigma = 1$ cho đúng $|e| = 1$ — và đó là lý do ở [mục 10](#10-dựng-đường-cầu-từ-các-điểm-tối-ưu) chi
tiêu cho Pepsi không đổi dù giá đổi. [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) gọi đó là *"cầu co giãn
đơn vị"* và đo nó từ dữ liệu; bài này cho thấy **nó đến từ đâu**: từ độ cong của đường bàng quan, chứ
không phải từ một con số trời ơi.

Và cũng từ đó giải thích luôn chỗ lệch ở [mục 9](#9-giá-đổi--tách-tác-động-thu-nhập-và-tác-động-thay-thế):
khi $\sigma = 1$, tác động thay thế và tác động thu nhập lên **pizza** triệt tiêu nhau chính xác. Đó là
**trường hợp đặc biệt**, không phải trường hợp chung — sách nói "không rõ ràng" là hoàn toàn chính xác.

> 📌 **Giữ lấy chữ $\sigma$ này.** Ba mục còn lại của chương — Giffen, cung lao động, tiết kiệm — đều là
> cùng một câu hỏi về $\sigma$, hỏi lại bằng ba bộ từ vựng khác nhau.

---

## 12. Có phải mọi đường cầu đều dốc xuống?

Câu hỏi thứ nhất trong ba câu hỏi mở chương. Câu trả lời của sách: **không, nhưng rất hiếm** (tr. 510).

> **Hàng hoá Giffen** *(Giffen good)*: một hàng hoá mà **giá tăng làm tăng lượng cầu**.

Sách đặt tên theo *"nhà kinh tế Robert Giffen, người đầu tiên chú ý đến khả năng này"*, và mô tả cơ
chế ở tr. 511:

> *"Khi giá khoai tây tăng lên, người tiêu dùng càng nghèo đi. Tác động thu nhập khiến người tiêu dùng
> muốn mua ít thịt và nhiều khoai tây hơn. Cùng lúc đó, vì khoai tây trở nên đắt hơn một cách tương đối
> so với thịt, tác động thay thế khiến người tiêu dùng muốn mua nhiều thịt và ít khoai tây hơn. Tuy
> nhiên trong trường hợp đặc biệt này, **tác động thu nhập mạnh tới nỗi nó vượt quá tác động thay thế**."*

### Dựng lại cơ chế bằng số

Cần một dạng sở thích khác hẳn các mục trên, và cơ chế thật nằm ở chỗ có **một ràng buộc thứ hai** bên
cạnh ràng buộc ngân sách: **ràng buộc dinh dưỡng**.

- Ngân sách 100 nghìn đồng/tuần, cần ít nhất **2.000 calo**
- Khoai tây và thịt đều cho 100 calo một đơn vị; thịt giá **8**, ngon hơn
- Hộ gia đình mua **nhiều thịt nhất có thể**, miễn là đủ calo

| Giá khoai |  Khoai | Thịt | Tiền khoai | Tiền thịt |  Calo |
| --------: | -----: | ---: | ---------: | --------: | ----: |
|         2 | **10** |   10 |         20 |        80 | 2.000 |
|         3 | **12** |    8 |         36 |        64 | 2.000 |
|         4 | **15** |    5 |         60 |        40 | 2.000 |
|         5 | **20** |    0 |        100 |         0 | 2.000 |

**Giá khoai tăng từ 2 lên 3 mà lượng khoai mua lại tăng từ 10 lên 12.** Đường cầu dốc **lên**.

Cơ chế đọc thẳng từ bảng: khoai lên giá → hộ nghèo đi → không còn đủ tiền mua thịt → phải lấy calo từ
nguồn rẻ nhất, **mà nguồn rẻ nhất vẫn là khoai**.

---

## 13. Nghiên cứu tình huống — cuộc tìm kiếm hàng hoá Giffen

Sách kể hai câu chuyện (tr. 511).

**Ireland thế kỷ 19.** *"Khoai tây là một phần quan trọng trong chế độ ăn của mọi người đến nỗi khi giá
của nó tăng, nó có tác động thu nhập rất lớn. Người ta phản ứng với sự giảm xuống trong mức sống đó
bằng cách giảm mua những hàng hóa đắt đỏ như thịt và mua nhiều hơn món thức ăn chính yếu này."*

**Hồ Nam, Trung Quốc.** Robert Jensen và Nolan Miller làm *"một thí nghiệm trong năm tháng"*: phát
phiếu giảm giá mua gạo cho các hộ được chọn ngẫu nhiên, rồi đo phản ứng.

> *"Họ tìm thấy những bằng chứng chắc chắn rằng **những hộ gia đình nghèo** thể hiện các hành vi Giffen…
> 'Với những gì chúng ta đã biết lúc này, đây là bằng chứng thực nghiệm đúng đắn nhất về hành vi Giffen.'"*

⚠️ Chú ý hai chữ **hộ nghèo**. Kiểm lại bằng mô hình, giữ nguyên mọi thứ và chỉ cho ngân sách chạy:

| Ngân sách | Khoai (giá 2) | Khoai (giá 3) | Kết luận           |
| --------: | ------------: | ------------: | ------------------ |
|       100 |            10 |            12 | **Giffen**         |
|       120 |          20/3 |             8 | **Giffen**         |
|       140 |          10/3 |             4 | **Giffen**         |
|       160 |             0 |             0 | không ăn khoai nữa |
|       180 |             0 |             0 | không ăn khoai nữa |

Ngưỡng nằm ở **160** — đúng số tiền mua toàn thịt. Từ đó trở lên, ràng buộc calo không còn siết nữa và
hành vi Giffen **biến mất**.

**Giffen là hiện tượng của cái nghèo, không phải của hàng hoá.** Cùng một củ khoai tây, cùng một mức
giá: nghèo thì Giffen, đủ ăn thì không. Đó chính là điều Jensen và Miller tìm thấy, và mô hình dựng lại
được nó mà không cần thêm giả định nào.

---

## 14. Lương tăng thì làm việc nhiều hơn hay ít hơn?

Câu hỏi thứ hai. Sách dùng lại **đúng bộ máy cũ**, chỉ đổi tên hai trục (tr. 512):

> *"Con người dành một lượng thời gian để giải trí và phần còn lại để lao động nhằm giúp họ đáp ứng
> các nhu cầu chi tiêu."*

Mẹo ở đây rất gọn và đáng học riêng: **thời gian nhàn rỗi cũng là một hàng hoá, và GIÁ của nó chính là
mức lương.** Bỏ một giờ nhàn rỗi thì được thêm đúng một mức lương để tiêu dùng.

Sally thức **100 giờ** một tuần, lương **$50/giờ** (tr. 512). Ba con số của sách:

|                      |  Tiêu dùng |
| -------------------- | ---------: |
| Nghỉ hết 100 giờ     |         $0 |
| Làm hết 100 giờ      |     $5.000 |
| Làm 40 giờ (nghỉ 60) | **$2.000** |

Cho lương tăng $50 → $60 (tr. 513), với ba độ cong khác nhau — vẫn là một núm $\sigma$ như mục 11:

| $\sigma$ | Nhàn rỗi và tiền là        | Nghỉ (giờ) | Làm (giờ) | Tiêu dùng |
| -------: | -------------------------- | ---------: | --------: | --------: |
|    **0** | bổ sung: nghỉ phải có tiền |  **64,29** |     35,71 | $2.142,86 |
|    **1** | trung gian                 |      60,00 |     40,00 | $2.400,00 |
|    **2** | thay thế: tiền bù được giờ |  **55,56** |     44,44 | $2.666,67 |

*(Cả ba đều xuất phát từ nghỉ 60 giờ, làm 40 giờ khi lương là $50.)*

Ba dòng, ba kết cục khác hẳn nhau:

- $\sigma = 0$ → nghỉ **nhiều** hơn → **đường cung lao động dốc xuống** (Hình 14b)
- $\sigma = 1$ → không đổi gì → đường cung **thẳng đứng**
- $\sigma = 2$ → nghỉ **ít** hơn → **đường cung dốc lên** (Hình 14a)

Sách kết luận ở tr. 514:

> *"lý thuyết kinh tế không cho thấy một sự phán đoán rõ ràng về việc liệu một sự tăng lên trong mức
> lương khiến cô làm việc nhiều hơn hay ít hơn."*

Bảng trên là câu đó, viết bằng số. Và nó nói rõ hơn sách một chút: **không phải lý thuyết yếu, mà là
kết quả thật sự phụ thuộc vào một tham số mà lý thuyết không biết trước.**

Đọc $\sigma = 0$ cho dễ: *"nghỉ mà không có tiền tiêu thì cũng chẳng nghỉ được"*. Đi chơi, du lịch, sở
thích — đều tốn tiền. Với người như vậy, lương tăng là cơ hội để **nghỉ nhiều hơn**, không phải làm
nhiều hơn.

---

## 15. Nghiên cứu tình huống — người trúng số và phán đoán của Carnegie

Sách đưa bằng chứng cho thấy trong dài hạn, tác động thu nhập **thắng** (tr. 514–515):

| Bằng chứng                 | Con số                                                                                                                                         |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Xu hướng lịch sử           | *"Một trăm năm trước, rất nhiều người làm việc sáu ngày mỗi tuần. Ngày nay, tuần làm việc năm ngày là chuyện phổ biến"* — lương tăng, giờ giảm |
| Trúng số **trên $50.000**  | gần **25%** nghỉ việc trong vòng 1 năm; 9% khác giảm số giờ                                                                                    |
| Trúng số **trên $1 triệu** | gần **40%** ngừng làm việc                                                                                                                     |
| Thừa kế **trên $150.000**  | khả năng nghỉ việc cao **gấp bốn lần** so với người thừa kế dưới $25.000 (*Quarterly Journal of Economics*, 1993)                              |

📚 **Vì sao dữ liệu người trúng số lại sắc bén đến vậy** — sách giải thích ở tr. 515, và đây là một mẩu
phương pháp luận rất đẹp:

> *"vì lương của những người trúng số vẫn không đổi nên **độ dốc của đường ràng buộc ngân sách của họ
> vẫn như cũ**. Vì thế, không có tác động thay thế nào. Bằng cách phân tích hành vi của những người
> trúng số, chúng ta có thể **tách biệt** tác động thu nhập lên cung lao động."*

Nói cách khác: trúng số là một **thí nghiệm tự nhiên** dịch chuyển đường ngân sách ra ngoài mà không
xoay nó. Đó chính là bước B → C của [mục 9](#9-giá-đổi--tách-tác-động-thu-nhập-và-tác-động-thay-thế),
xảy ra ngoài đời thật.

Và sách đóng bằng **Andrew Carnegie**, nhà công nghiệp thế kỷ 19:

> *"những phụ huynh để lại cho con cái mình những món thừa kế khổng lồ vô hình chung sẽ làm lu mờ tài
> năng, giảm ý chí của chúng, và xúi giục chúng sống một cuộc sống kém có ích và ít giá trị hơn cuộc
> sống vốn có."*
>
> *"Suốt cuộc đời mình cho đến lúc chết, Carnegie dành rất nhiều trong khối tài sản khổng lồ của mình
> cho từ thiện."*

Carnegie tin vào tác động thu nhập mạnh tới mức ông **cho hết tài sản đi** vì nó.

---

## 16. Lãi suất tăng thì tiết kiệm nhiều hơn hay ít hơn?

Câu hỏi thứ ba, và lại vẫn là bộ máy cũ với hai trục mới: **tiêu dùng lúc trẻ** và **tiêu dùng lúc già**
(tr. 515). Giá tương đối giữa chúng chính là **lãi suất**.

Sam kiếm **$100.000** lúc trẻ, không kiếm gì lúc già. Lãi suất **10%**. Ba con số của sách (tr. 516):

|                    |     Lúc trẻ |     Lúc già |
| ------------------ | ----------: | ----------: |
| Không tiết kiệm gì |    $100.000 |          $0 |
| Tiết kiệm tất cả   |          $0 |    $110.000 |
| **Điểm tối ưu**    | **$50.000** | **$55.000** |

Cho lãi suất tăng 10% → 20% (tr. 516), vẫn ba độ cong:

| $\sigma$ | Tiêu lúc trẻ |      Tiết kiệm | Tiêu lúc già |
| -------: | -----------: | -------------: | -----------: |
|    **0** |   $52.173,91 | **$47.826,09** |   $57.391,30 |
|    **1** |   $50.000,00 |     $50.000,00 |   $60.000,00 |
|    **2** |   $47.826,09 | **$52.173,91** |   $62.608,70 |

*(Cả ba đều xuất phát từ tiết kiệm $50.000 ở lãi suất 10%.)*

- $\sigma = 0$ → tiết kiệm **giảm** (Hình 16b)
- $\sigma = 1$ → không đổi
- $\sigma = 2$ → tiết kiệm **tăng** (Hình 16a)

**Cùng một cấu trúc với mục 14, cùng một núm $\sigma$.** Ba câu hỏi mở chương — tưởng chẳng liên quan
gì tới nhau — hoá ra là **một câu hỏi duy nhất** về độ cong của đường bàng quan.

### Vì sao chuyện này không chỉ là chuyện lý thuyết

Sách rút ra một hệ quả chính sách rất thật (tr. 517–518):

> *"Một số nhà kinh tế đã kêu gọi giảm thuế đánh vào tiền lãi và thu nhập trên vốn. Họ lập luận rằng
> một chính sách giảm thuế sẽ làm tăng mức lãi suất sau thuế mà những người tiết kiệm có thể có được và
> vì thế sẽ khuyến khích người ta tiết kiệm nhiều hơn. Những nhà kinh tế khác đã lập luận rằng vì sự bù
> trừ của tác động thu nhập và tác động thay thế, một chính sách như vậy **có thể không làm tăng tiết
> kiệm và thậm chí có thể làm giảm nó**."*

**Cả hai phe đều đúng về mặt lý thuyết.** Câu hỏi *"$\sigma$ bằng bao nhiêu"* là một câu hỏi **thực
nghiệm**, và sách thừa nhận thẳng ở tr. 518 rằng *"các nghiên cứu đã không mang tới một sự đồng thuận
về cách lãi suất tác động đến tiết kiệm"*.

---

## 17. Con người có thực sự nghĩ theo hướng này không?

Sách tự đặt câu hỏi hoài nghi hiển nhiên nhất, ngay trong phần kết luận (tr. 518):

> *"Cuối cùng thì bạn là một người tiêu dùng. Bạn quyết định sẽ mua gì mỗi khi bước vào một cửa hàng?
> Và bạn biết rằng bạn không làm việc đó bằng cách vẽ ra những đường giới hạn ngân sách và những đường
> bàng quan. Chẳng phải điều này đi ngược lại với lý thuyết sao?"*

Và trả lời rất thẳng:

> *"Câu trả lời là không. Lý thuyết người tiêu dùng không cố gắng thể hiện một sự tính toán theo nghĩa
> đen về cách mà con người ra quyết định. Nó là **một mô hình**… Cách tốt nhất để nhìn nhận lý thuyết
> người tiêu dùng là coi nó như **một phép ẩn dụ** cho cách mà người tiêu dùng ra quyết định."*
>
> *"Đến giờ những người tiêu dùng vẫn biết rằng lựa chọn của họ bị giới hạn bởi các nguồn lực tài chính.
> Với những giới hạn đó, họ làm điều tốt nhất có thể để có được mức thỏa mãn cao nhất."*

⚠️ Đây là một trong những đoạn trung thực nhất của cả cuốn sách, và cũng là chỗ dễ hiểu sai nhất. Mô
hình **không** khẳng định người ta vẽ đồ thị trong đầu. Nó khẳng định rằng **hành vi quan sát được trông
như thể** người ta làm vậy — và điều đó là đủ để dự đoán.

📌 Và đó cũng là bản lề nối sang **Bài 11** (chương 22): kinh tế học hành vi hỏi thẳng rằng phép ẩn dụ
này **hỏng ở đâu**, và hỏng theo những kiểu **có quy luật** nào.

---

## 18. 💼 Chia ngân sách marketing bằng đúng quy tắc của mục 6

Quy tắc *"cân bằng lợi ích biên trên một đồng"* ở [mục 7](#7--độ-thoả-dụng--cách-nói-thứ-hai-cho-cùng-một-điều)
không chỉ dùng cho pizza và Pepsi. Nó là quy tắc cho **mọi** bài toán chia một nguồn lực hữu hạn giữa
nhiều cách dùng — kể cả những cách dùng chẳng liên quan gì tới người tiêu dùng.

Bài toán: **100 triệu đồng ngân sách quảng cáo, chia cho hai kênh.** Mỗi kênh có lợi ích biên giảm dần —
10 triệu đầu bao giờ cũng hiệu quả hơn 10 triệu thứ tám:

| Khối 10 triệu thứ |    1 |    2 |    3 |    4 |    5 |    6 |    7 |    8 |    9 |   10 |
| ----------------- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tìm kiếm (lead)   |  380 |  340 |  300 |  260 |  220 |  180 |  140 |  100 |   60 |   20 |
| Mạng XH (lead)    |  225 |  200 |  175 |  150 |  125 |  100 |   75 |   50 |   25 |    0 |

Áp dụng quy tắc: mỗi khối tiếp theo đặt vào nơi có **lợi ích biên cao nhất**. Kết quả: **6 khối cho Tìm
kiếm, 4 khối cho Mạng XH**, thu về **2.430 lead**.

Kiểm điều kiện biên — phiên bản rời rạc của $MU_A/P_A = MU_B/P_B$:

|                                                  | Lead |
| ------------------------------------------------ | ---: |
| Lợi ích biên **thấp nhất** trong các khối đã đặt |  150 |
| Lợi ích biên **cao nhất** trong các khối bỏ lại  |  140 |

Đã đặt ≥ bỏ lại → **không thể cải thiện bằng cách đổi chỗ**. Đó là điều kiện tối ưu của tr. 504, chỉ
khác là tiền đi từng khối 10 triệu nên hai vế chỉ *gần* bằng chứ không bằng chằn chặn.

### Bài học thứ hai quan trọng hơn bài học thứ nhất

| Cách chia                   | Tổng lead | Mất so với tối ưu |
| --------------------------- | --------: | ----------------: |
| **Tối ưu** (6/4)            |     2.430 |                 — |
| Chia đôi 50/50 (5/5)        |     2.375 |     55 — **2,3%** |
| Dồn hết vào Tìm kiếm (10/0) |     2.000 |   430 — **17,7%** |
| Dồn hết vào Mạng XH (0/10)  |     1.125 | 1.305 — **53,7%** |

**Đỉnh của đường cong rất phẳng, còn hai đầu thì dốc đứng.** Chia 5/5 thay vì 6/4 chỉ mất 2,3% — gần
như không đáng kể. Nhưng dồn hết 100 triệu vào một kênh thì mất tới 54%.

> 💼 Suy ra một câu dùng được ngay: **đừng mất thời gian tính toán để đi từ 5/5 sang 6/4.** Hãy dùng
> thời gian đó để đảm bảo bạn **không** đang ở 10/0 hay 0/10. Sai lầm đắt tiền trong phân bổ nguồn lực
> gần như luôn là sai lầm **cực đoan** — và chúng thường đến từ những câu nghe rất quyết đoán như
> *"năm nay ta tất tay vào kênh này"*.

⚠️ Và một giới hạn của mô hình, nói rõ để khỏi dùng sai: bảng lợi ích biên ở trên được **cho sẵn**.
Ngoài đời bạn phải **đo** nó, và đo được nó mới là phần khó. Quy tắc chỉ nói *phải cân bằng cái gì*;
nó không nói *cái đó bằng bao nhiêu*. Đây đúng là vấn đề mà sách gặp với $\sigma$ ở mục 14 và 16 — lý
thuyết cho bạn dạng của câu trả lời, dữ liệu mới cho bạn con số.

---

## 19. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-10-lua-chon-nguoi-tieu-dung.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-10-lua-chon-nguoi-tieu-dung.py](../thuc_hanh/bai-10-lua-chon-nguoi-tieu-dung.py).

Mọi thứ dùng `Fraction` — không có số thực nào trong phần tính toán, nên chạy bao nhiêu lần cũng ra
đúng một kết quả. Chỗ duy nhất xuất hiện số thực là $\log_2 3$ ở mục 8, và nó được đánh dấu rõ.

⚠️ Code có **12 mục đánh số riêng của nó**, không trùng với 22 mục của bài học. Bảng đối chiếu:

| Mục trong code | Mục trong bài                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–3            | [2](#2-đường-ràng-buộc-ngân-sách), [3](#3-đường-bàng-quan-và-tỷ-lệ-thay-thế-biên) + [4](#4-bốn-tính-chất-của-đường-bàng-quan), [5](#5-hai-trường-hợp-đặc-biệt)              |
| 4              | [6](#6-điểm-tối-ưu--nơi-hai-đường-tiếp-tuyến-nhau) + [7](#7--độ-thoả-dụng--cách-nói-thứ-hai-cho-cùng-một-điều)                                                              |
| 5–7            | [8](#8-thu-nhập-tăng--hàng-hoá-thông-thường-và-hàng-hoá-thứ-cấp), [9](#9-giá-đổi--tách-tác-động-thu-nhập-và-tác-động-thay-thế), [10](#10-dựng-đường-cầu-từ-các-điểm-tối-ưu) |
| 8              | [11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại)                                                                                                           |
| 9              | [12](#12-có-phải-mọi-đường-cầu-đều-dốc-xuống) + [13](#13-nghiên-cứu-tình-huống--cuộc-tìm-kiếm-hàng-hoá-giffen)                                                              |
| 10–11          | [14](#14-lương-tăng-thì-làm-việc-nhiều-hơn-hay-ít-hơn), [16](#16-lãi-suất-tăng-thì-tiết-kiệm-nhiều-hơn-hay-ít-hơn)                                                          |
| 12             | [18](#18--chia-ngân-sách-marketing-bằng-đúng-quy-tắc-của-mục-6)                                                                                                             |

```python
"""Bai 10 - Ly thuyet lua chon cua nguoi tieu dung (Mankiw, chuong 21, tr. 495-524).

Chay: python3 bai-10-lua-chon-nguoi-tieu-dung.py
Khong can cai goi nao ngoai thu vien chuan.
"""

import math
from fractions import Fraction as F

DONG = "-" * 74


def tieu_de(so, ten):
    print()
    print("=" * 74)
    print(f"MUC {so}. {ten}")
    print("=" * 74)


def tien(x):
    """So NGUYEN co dau cham ngan cach nghin. Nem loi neu bi truyen so le."""
    x = F(x)
    assert x.denominator == 1, f"tien() chi nhan so nguyen, nhan duoc {x}"
    return f"{x.numerator:,}".replace(",", ".")


def thap_phan(x, le=2):
    """Lam tron ra so thap phan kieu Viet Nam: dau phay la phan le."""
    x = F(x)
    nguyen = x.numerator // x.denominator
    du = round((x - nguyen) * 10 ** le)
    if du == 10 ** le:
        nguyen, du = nguyen + 1, 0
    return f"{nguyen:,}".replace(",", ".") + "," + str(du).rjust(le, "0")


def dau(x):
    """Nhu so() nhung luon co dau + hoac - o dau."""
    x = F(x)
    return ("+" if x > 0 else "") + so(x)


def so(x):
    """In mot Fraction: nguyen thi khong co phan le, khong thi giu dang phan so."""
    x = F(x)
    return tien(x) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# ---------------------------------------------------------------------------
# MUC 1. Duong rang buoc ngan sach - Hinh 1, tr. 497
# ---------------------------------------------------------------------------
THU_NHAP = 1000       # do la moi thang
GIA_PIZZA = 10        # do la mot chiec
GIA_PEPSI = 2         # do la mot chai

tieu_de(1, "Duong rang buoc ngan sach - Hinh 1, tr. 497")

# Sach in 11 dong. Cong thuc dang sau no chi la mot phuong trinh bac nhat:
#     10 * pizza + 2 * pepsi = 1000
BANG_SACH = [(100, 0), (90, 50), (80, 100), (70, 150), (60, 200), (50, 250),
             (40, 300), (30, 350), (20, 400), (10, 450), (0, 500)]


def pepsi_theo_pizza(pizza, thu_nhap=THU_NHAP, gia_pepsi=GIA_PEPSI):
    """Con lai bao nhieu chai Pepsi sau khi da mua ngan ay pizza."""
    return F(thu_nhap - GIA_PIZZA * pizza, gia_pepsi)


print(f"Thu nhap {tien(THU_NHAP)} do la/thang;"
      f" pizza {GIA_PIZZA} do la/chiec; Pepsi {GIA_PEPSI} do la/chai.")
print(f"Rang buoc: {GIA_PIZZA} x pizza + {GIA_PEPSI} x pepsi = {tien(THU_NHAP)}")
print()
print(f"{'Pizza':>7} {'Pepsi':>7} {'Tien pizza':>12} {'Tien Pepsi':>12}"
      f" {'Tong':>10} {'Sach in':>9} {'Khop':>6}")
print(DONG)
khop = 0
for pizza, pepsi_sach in BANG_SACH:
    pepsi = pepsi_theo_pizza(pizza)
    tp, tq = GIA_PIZZA * pizza, GIA_PEPSI * pepsi
    ok = pepsi == pepsi_sach and tp + tq == THU_NHAP
    khop += ok
    print(f"{pizza:>7} {so(pepsi):>7} {tien(tp):>12} {tien(tq):>12}"
          f" {tien(tp + tq):>10} {pepsi_sach:>9} {str(ok):>6}")
print(DONG)
print(f"Khop {khop}/{len(BANG_SACH)} dong. Cot 'Tong' bang {tien(THU_NHAP)} o moi dong -")
print("do chinh la y nghia cua tu 'rang buoc'.")
print()

# Do doc = gia tuong doi
do_doc = F(GIA_PIZZA, GIA_PEPSI)
print(f"Do doc = 500 chai Pepsi / 100 chiec pizza = {so(do_doc)} chai tren 1 chiec.")
print(f"Va cung bang gia tuong doi: {GIA_PIZZA} / {GIA_PEPSI} = {so(do_doc)}.")
print("Hai cach tinh, mot con so. Do doc duong ngan sach CHINH LA gia tuong doi.")


# ---------------------------------------------------------------------------
# MUC 2. Duong bang quan va ty le thay the bien
# ---------------------------------------------------------------------------
tieu_de(2, "Duong bang quan - ty le thay the bien giam dan")

# Sach khong cho ham thoa dung. Chon ham don gian nhat co dung bon tinh chat
# ma sach liet ke o tr. 499-500:  U = pizza * pepsi.
#   MU_pizza = pepsi,  MU_pepsi = pizza,  MRS = MU_pizza / MU_pepsi = pepsi / pizza


def thoa_dung(pizza, pepsi):
    return F(pizza) * F(pepsi)


def mrs(pizza, pepsi):
    """So chai Pepsi phai bu them de bo bot mot chiec pizza ma van bang quan."""
    return F(pepsi, pizza)


U_TOI_UU = 50 * 250     # duong bang quan di qua diem toi uu o muc 3

print(f"Ham thoa dung dung o day: U = pizza x pepsi   (duong bang quan U = {tien(U_TOI_UU)})")
print("Sach khong cho ham nay - day la ham gon nhat co du bon tinh chat tr. 499-500.")
print()
print(f"{'Pizza':>7} {'Pepsi':>9} {'U':>10} {'MRS':>10}   Doc la")
print(DONG)
for pizza in (10, 25, 50, 100, 125):
    pepsi = F(U_TOI_UU, pizza)
    m = mrs(pizza, pepsi)
    ghi = ("it pizza -> doi nhieu Pepsi moi chiu bo 1 chiec"
           if m > 10 else
           "nhieu pizza -> bo 1 chiec chi can it Pepsi" if m < 2 else
           "vung giua")
    print(f"{pizza:>7} {so(pepsi):>9} {tien(thoa_dung(pizza, pepsi)):>10} {so(m):>10}   {ghi}")
print(DONG)
print("MRS giam don dieu tu 125 xuong 0,8 khi di sang phai. Do chinh la TINH CHAT 4")
print("(tr. 500): duong bang quan CONG VE GOC TOA DO. Sach giai thich bang mot cau")
print("rat doi thuong: 'con nguoi thuong san long trao doi hang hoa ma ho co nhieu'.")
print()
print("Bon tinh chat, kiem tung cai bang so:")
u_thap, u_cao = 12500, 25000
print(f"  1. Duong cao hon duoc ua thich hon: U={tien(u_cao)} > U={tien(u_thap)}."
      f" Tai pizza=50,")
print(f"     duong tren cho {so(F(u_cao, 50))} chai Pepsi thay vi {so(F(u_thap, 50))}. Nhieu hon that.")
print(f"  2. Doc xuong: pizza 10 -> 125 thi Pepsi {tien(F(U_TOI_UU, 10))} -> {tien(F(U_TOI_UU, 125))}."
      f" Mot len thi mot xuong.")
print("  3. Khong cat nhau: neu pizza x pepsi = 12.500 VA = 25.000 tai cung mot diem")
print("     thi 12.500 = 25.000. Vo ly. Hai duong khac muc thi khong the giao nhau.")
print("  4. Cong ve goc toa do: bang MRS o tren.")


# ---------------------------------------------------------------------------
# MUC 3. Hai truong hop dac biet - Hinh 5, tr. 502
# ---------------------------------------------------------------------------
tieu_de(3, "Hai truong hop dac biet - Hinh 5, tr. 502")

print("(a) THAY THE HOAN HAO - dong 5 cent va dong 10 cent (tr. 501)")
print("    Ban chi quan tam tong so tien, nen MRS la mot hang so.")
print()
print(f"    {'Dong 10c':>9} {'Dong 5c':>9} {'Tong (cent)':>13} {'MRS':>6}")
print("    " + DONG[:42])
for muoi in (0, 1, 2, 3):
    nam = (30 - 10 * muoi) // 5
    print(f"    {muoi:>9} {nam:>9} {10 * muoi + 5 * nam:>13} {2:>6}")
print("    " + DONG[:42])
print("    MRS = 2 o MOI diem -> duong bang quan la duong THANG.")
print()
print("(b) BO SUNG HOAN HAO - giay trai va giay phai (tr. 501)")
print("    Ban chi quan tam so DOI giay: so doi = min(trai, phai).")
print()
print(f"    {'Trai':>6} {'Phai':>6} {'So doi':>8}   Doc la")
print("    " + DONG[:52])
for trai, phai in [(5, 5), (5, 7), (7, 5), (7, 7)]:
    doi = min(trai, phai)
    ghi = "vua du" if trai == phai else f"thua {abs(trai - phai)} chiec, vo dung"
    print(f"    {trai:>6} {phai:>6} {doi:>8}   {ghi}")
print("    " + DONG[:52])
print("    (5,5) va (5,7) va (7,5) deu cho 5 doi -> BANG QUAN. Duong bang quan")
print("    la goc VUONG. Sach viet: 'Co them mot chiec ben phai luc nay cha co y")
print("    nghia gi neu khong co mot chiec ben trai di kem.'")
print()
print("Hai truong hop nay la HAI DAU MUT cua mot thang do. Muc 8 se dat ten")
print("cho thang do do va cho thay no quyet dinh gan nhu moi ket luan con lai.")


# ---------------------------------------------------------------------------
# MUC 4. Diem toi uu - Hinh 6, tr. 503 va hop "Ban co biet" tr. 504
# ---------------------------------------------------------------------------
tieu_de(4, "Diem toi uu - noi hai duong tiep tuyen nhau")


def toi_uu_cobb_douglas(thu_nhap, gia_x, gia_y, trong_so_x=F(1, 2)):
    """Voi U = x^a * y^(1-a): tieu dung dung a phan thu nhap cho x."""
    x = F(thu_nhap) * trong_so_x / gia_x
    y = F(thu_nhap) * (1 - trong_so_x) / gia_y
    return x, y


pizza_tu, pepsi_tu = toi_uu_cobb_douglas(THU_NHAP, GIA_PIZZA, GIA_PEPSI)
print(f"Diem toi uu: {so(pizza_tu)} chiec pizza va {so(pepsi_tu)} chai Pepsi.")
print(f"  Chi cho pizza: {tien(GIA_PIZZA * pizza_tu)} do la")
print(f"  Chi cho Pepsi: {tien(GIA_PEPSI * pepsi_tu)} do la")
print(f"  Cong          : {tien(GIA_PIZZA * pizza_tu + GIA_PEPSI * pepsi_tu)} do la"
      f"  (dung bang thu nhap)")
print()
print("Day chinh la DIEM C tren Hinh 1, tr. 496 - diem ma sach mo ta la")
print("'nguoi tieu dung chi tieu nhung khoan bang nhau (500 do la) cho hai mat hang'.")
print()

# Dieu kien tiep tuyen: MRS = gia tuong doi
m = mrs(pizza_tu, pepsi_tu)
print("Kiem dieu kien tiep tuyen ma sach nhan manh o tr. 503:")
print(f"  Do doc duong bang quan (MRS)      = {so(m)}")
print(f"  Do doc duong ngan sach (gia t.doi) = {so(do_doc)}")
print(f"  Bang nhau? {m == do_doc}")
print()

# Hop "Ban co biet" tr. 504: MU_x / P_x = MU_y / P_y
mu_pizza, mu_pepsi = pepsi_tu, pizza_tu     # vi U = pizza * pepsi
print("Hop 'Ban co biet' tr. 504 viet lai dieu kien do bang do thoa dung bien:")
print(f"  MU_pizza / P_pizza = {so(mu_pizza)} / {GIA_PIZZA} = {so(mu_pizza / GIA_PIZZA)}")
print(f"  MU_pepsi / P_pepsi = {so(mu_pepsi)} / {GIA_PEPSI} = {so(mu_pepsi / GIA_PEPSI)}")
print(f"  Bang nhau? {mu_pizza / GIA_PIZZA == mu_pepsi / GIA_PEPSI}")
print()
print("Doc cau nay cham: MOT DO LA CHI THEM VAO PIZZA MANG LAI DUNG BANG MOT DO LA")
print("CHI THEM VAO PEPSI. Neu khong bang, chuyen tien tu ben thap sang ben cao la")
print("loi ngay - nen chua the goi la toi uu. Muc 12 dung dung quy tac nay cho mot")
print("bai toan chia ngan sach marketing.")
print()

# Doi chieu voi hai diem A va B ma sach ve o Hinh 6
print("Sach ve them hai diem de doi chieu (tr. 503):")
for ten, pizza, pepsi, ghi in [
        ("A", 70, 400, "TREN duong ngan sach - khong voi toi"),
        ("B", 20, 300, "DUOI duong ngan sach - con thua tien")]:
    chi = GIA_PIZZA * pizza + GIA_PEPSI * pepsi
    print(f"  Diem {ten}: {pizza} pizza + {pepsi} Pepsi = {tien(chi)} do la"
          f" -> {ghi}")
    print(f"           U = {tien(thoa_dung(pizza, pepsi))}"
          f" (toi uu la {tien(thoa_dung(pizza_tu, pepsi_tu))})")
print("  A thi thich hon nhung KHONG DU TIEN. B thi du tien nhung THOA DUNG THAP HON.")


# ---------------------------------------------------------------------------
# MUC 5. Thu nhap tang - Hinh 7 va Hinh 8
# ---------------------------------------------------------------------------
tieu_de(5, "Thu nhap tang - hang hoa thong thuong va hang hoa thu cap")

print(f"{'Thu nhap':>10} {'Pizza':>8} {'Pepsi':>8}   Nhan xet")
print(DONG)
truoc = None
for m_thu in (1000, 1200, 1500, 2000):
    x, y = toi_uu_cobb_douglas(m_thu, GIA_PIZZA, GIA_PEPSI)
    ghi = "" if truoc is None else "ca hai cung tang -> deu la HANG HOA THONG THUONG"
    print(f"{tien(m_thu):>10} {so(x):>8} {so(y):>8}   {ghi}")
    truoc = (x, y)
print(DONG)
print("Duong ngan sach dich chuyen SONG SONG ra ngoai: gia khong doi nen do doc")
print(f"van la {so(do_doc)}. Do la Hinh 7, tr. 505.")
print()
print("Hinh 8 (tr. 506) ve truong hop nguoc lai: thu nhap tang ma mua IT Pepsi di.")
print("Ham U = pizza x pepsi khong bao gio tao ra ket cuc do - no luon cho ra hang")
print("hoa thong thuong. Muon co hang hoa THU CAP thi phai doi so thich, va muc 9")
print("se dung dung mot mo hinh nhu vay (mo hinh calo) de dung ra hang hoa Giffen.")
print()
print("Vi du hang hoa thu cap ma sach dua ra o tr. 506: cac chuyen XE BUYT.")
print("'Khi thu nhap tang len, nhung nguoi tieu dung thuong se mua xe hoi hoac di")
print("taxi va it khi di xe buyt.'")


# ---------------------------------------------------------------------------
# MUC 6. Gia doi - tach tac dong thu nhap va tac dong thay the
# ---------------------------------------------------------------------------
tieu_de(6, "Gia Pepsi giam - tach tac dong thu nhap va tac dong thay the")

GIA_PEPSI_MOI = 1

x0, y0 = pizza_tu, pepsi_tu
x2, y2 = toi_uu_cobb_douglas(THU_NHAP, GIA_PIZZA, GIA_PEPSI_MOI)

# Buoc trung gian: bu thu nhap sao cho gio hang CU van vua du mua o gia MOI.
# (Sach dung cach giu nguyen DO THOA MAN - Hicks. O day dung cach giu nguyen
#  SUC MUA CUA GIO CU - Slutsky - vi no cho so huu ti. Hai cach cung dau.)
thu_nhap_bu = GIA_PIZZA * x0 + GIA_PEPSI_MOI * y0
x1, y1 = toi_uu_cobb_douglas(thu_nhap_bu, GIA_PIZZA, GIA_PEPSI_MOI)

print(f"Gia Pepsi giam tu {GIA_PEPSI} xuong {GIA_PEPSI_MOI} do la (tr. 506).")
print(f"Gio hang cu ({so(x0)} pizza, {so(y0)} Pepsi) o gia moi chi con ton"
      f" {tien(thu_nhap_bu)} do la")
print(f"thay vi {tien(THU_NHAP)} -> nguoi tieu dung tu nhien giau len {tien(THU_NHAP - thu_nhap_bu)} do la.")
print()
print(f"{'Buoc':<34} {'Pizza':>9} {'Pepsi':>9} {'Thu nhap':>10}")
print(DONG)
print(f"{'A. Ban dau':<34} {so(x0):>9} {so(y0):>9} {tien(THU_NHAP):>10}")
print(f"{'B. Chi doi GIA, bu lai thu nhap':<34} {so(x1):>9} {so(y1):>9} {tien(thu_nhap_bu):>10}")
print(f"{'C. Tra lai phan thu nhap da bu':<34} {so(x2):>9} {so(y2):>9} {tien(THU_NHAP):>10}")
print(DONG)
print(f"{'  A -> B  TAC DONG THAY THE':<34} {so(x1 - x0):>9} {so(y1 - y0):>9}")
print(f"{'  B -> C  TAC DONG THU NHAP':<34} {so(x2 - x1):>9} {so(y2 - y1):>9}")
print(f"{'  A -> C  TONG':<34} {so(x2 - x0):>9} {so(y2 - y0):>9}")
print(DONG)
print()
print("Doi chieu voi Bang 1, tr. 508 - sach ket luan bang loi, day la bang so:")
print()
print(f"  PEPSI : thay the {dau(y1 - y0):>5}  va thu nhap {dau(y2 - y1):>5}"
      f"  -> CUNG CHIEU, tong {dau(y2 - y0):>5}")
print(f"          Sach: 'tac dong thu nhap va tac dong thay the xay ra theo cung")
print(f"          chieu huong, vi vay nguoi tieu dung se mua nhieu Pepsi hon.' Dung.")
print()
print(f"  PIZZA : thay the {dau(x1 - x0):>5}  va thu nhap {dau(x2 - x1):>5}"
      f"  -> NGUOC CHIEU, tong {dau(x2 - x0):>5}")
print(f"          Sach: 'tong tac dong len tieu dung pizza la KHONG RO RANG.' Dung -")
print(f"          va o day hai tac dong triet tieu nhau HOAN TOAN. Muc 8 giai thich")
print(f"          vi sao dieu do khong phai tinh co.")


# ---------------------------------------------------------------------------
# MUC 7. Dung duong cau tu cac diem toi uu - Hinh 11, tr. 509
# ---------------------------------------------------------------------------
tieu_de(7, "Dung duong cau tu cac diem toi uu - Hinh 11, tr. 509")

print("Duong cau khong phai mot gia dinh - no la TAP HOP CAC DIEM TOI UU khi cho")
print("gia chay. Cho gia Pepsi chay tu 5 do la xuong 1 do la, ghi lai luong toi uu:")
print()
print(f"{'Gia Pepsi':>10} {'Pizza':>8} {'Pepsi':>8} {'Chi cho Pepsi':>15}")
print(DONG)
for gp in (5, 4, F(5, 2), 2, F(5, 4), 1):
    x, y = toi_uu_cobb_douglas(THU_NHAP, GIA_PIZZA, gp)
    print(f"{so(gp):>10} {so(x):>8} {so(y):>8} {tien(gp * y):>15}")
print(DONG)
print("Ba dieu bang nay noi ngay:")
print("  - Gia xuong thi luong len -> DUONG CAU DOC XUONG. Khong gia dinh gi ca,")
print("    no roi ra tu ban than viec toi uu hoa.")
print("  - Luong pizza KHONG DOI dung 50 chiec o moi muc gia Pepsi.")
print("  - Chi tieu cho Pepsi KHONG DOI dung 500 do la -> do co gian bang 1 chan.")
print()

# So sanh voi con so cua sach
y_sach_truoc, y_sach_sau = 250, 750
x_ta, y_ta = toi_uu_cobb_douglas(THU_NHAP, GIA_PIZZA, 1)
print("So voi Hinh 11 cua sach:")
print(f"  Sach : gia 2 -> 1 do la thi Pepsi {y_sach_truoc} -> {y_sach_sau} chai")
print(f"  Ham U = pizza x pepsi : {so(pepsi_tu)} -> {so(y_ta)} chai")
print()
print("KHONG KHOP, va cho lech nay la cho hoc duoc nhieu nhat trong ca bai.")
print("Ham U = pizza x pepsi luon giu chi tieu cho moi mat hang o dung mot nua thu")
print("nhap, nen no KHONG THE cho ra gap ba. De ra 750 chai, hai mat hang phai THAY")
print("THE cho nhau de hon - tuc la duong bang quan phai THANG hon. Muc 8 do dieu do.")


# ---------------------------------------------------------------------------
# MUC 8. Do cong cua duong bang quan quyet dinh moi thu con lai
# ---------------------------------------------------------------------------
tieu_de(8, "Do cong cua duong bang quan - mot tham so, moi ket luan")

# Ho ham CES:  U = (A*x^r + B*y^r)^(1/r),  sigma = 1/(1-r) la do co gian thay the.
# Cau:  x = M*A*px^(-s) / (A*px^(1-s) + B*py^(1-s)).
# sigma = 0  -> bo sung hoan hao (goc vuong, Hinh 5b)
# sigma = 1  -> U = x*y  (ham dung o cac muc tren)
# sigma -> vo cung -> thay the hoan hao (duong thang, Hinh 5a)


def cau_ces(thu_nhap, gia_x, gia_y, sigma, A, B):
    """Luong cau hang x theo ho ham CES voi do co gian thay the sigma nguyen."""
    tren = F(thu_nhap) * A * F(gia_x) ** (-sigma)
    duoi = A * F(gia_x) ** (1 - sigma) + B * F(gia_y) ** (1 - sigma)
    return tren / duoi


def hieu_chinh(sigma):
    """Chon A, B sao cho diem toi uu ban dau van dung la (50 pizza, 250 Pepsi)."""
    A = 1
    B = F(GIA_PEPSI, GIA_PIZZA) ** (1 - sigma)
    return A, B


print("Ho ham CES cho phep xoay mot num duy nhat - do co gian thay the sigma -")
print("de di tu 'bo sung hoan hao' sang 'thay the hoan hao'. Hieu chinh moi truong")
print(f"hop sao cho diem xuat phat van dung la ({so(pizza_tu)} pizza, {so(pepsi_tu)} Pepsi).")
print()
print(f"{'sigma':>6}  {'Hai mat hang la':<24} {'Pepsi khi gia 2':>16} {'khi gia 1':>11}")
print(DONG)
for sigma, nhan in [(0, "bo sung hoan hao"), (1, "trung gian (U = x.y)"),
                    (2, "de thay the"), (3, "rat de thay the")]:
    A, B = hieu_chinh(sigma)
    y_truoc = cau_ces(THU_NHAP, GIA_PEPSI, GIA_PIZZA, sigma, A, B)
    y_sau = cau_ces(THU_NHAP, GIA_PEPSI_MOI, GIA_PIZZA, sigma, A, B)
    print(f"{sigma:>6}  {nhan:<24} {so(y_truoc):>16} {so(y_sau):>11}")
print(DONG)
print(f"Con so cua sach o Hinh 11 la {y_sach_sau} chai - nam giua sigma = 2 va sigma = 3.")

# Giai nguoc: sigma nao cho dung 750?
#   y(gia 1) = 1000 / (1 + 2^(1-sigma)) = 750  <=>  2^(1-sigma) = 1/3
sigma_sach = 1 + math.log2(3)
print(f"Giai nguoc phuong trinh 1000 / (1 + 2^(1-sigma)) = {y_sach_sau}:")
print(f"  2^(1-sigma) = 1/3  ->  sigma = 1 + log2(3) = {thap_phan(sigma_sach, 4)}")
print()
print("Nghia la: Hinh 11 cua sach duoc ve voi gia dinh ngam rang pizza va Pepsi")
print(f"THAY THE cho nhau de gap khoang {thap_phan(sigma_sach, 1)} lan muc trung gian. Sach khong noi")
print("dieu do o dau ca - no nam trong do cong ma hoa si da ve.")
print()

# Do co gian theo gia, suy ra tu sigma
print("Va day la cong thuc noi ca bai nay voi bai 3. Voi ho CES hai hang hoa, do co")
print("gian cua cau theo gia tai diem ma hang hoa chiem ty phan s cua chi tieu la:")
print()
print("        |e| = sigma * (1 - s) + s")
print()
print(f"O diem xuat phat, Pepsi chiem s = {so(F(GIA_PEPSI * pepsi_tu, THU_NHAP))}"
      f" chi tieu. Vay:")
print()
print(f"{'sigma':>6} {'|e| = sigma(1-s) + s':>22}   Doc la")
print(DONG)
s_phan = F(GIA_PEPSI * pepsi_tu, THU_NHAP)
for sigma in (0, 1, 2, 3):
    e = sigma * (1 - s_phan) + s_phan
    ghi = ("khong co gian" if e < 1 else "co gian don vi" if e == 1 else "co gian")
    print(f"{sigma:>6} {so(e):>22}   {ghi}")
print(DONG)
print("sigma = 1 cho dung |e| = 1 - va do la ly do o muc 7 chi tieu cho Pepsi khong")
print("doi du gia doi. Bai 3 goi do la 'cau co gian don vi'; bai nay cho thay no den")
print("tu dau: tu DO CONG cua duong bang quan, chu khong phai tu mot con so troi oi.")
print()
print("Va cung tu do giai thich luon cho lech o muc 6: khi sigma = 1 thi tac dong")
print("thay the va tac dong thu nhap len PIZZA triet tieu nhau chinh xac. Do la")
print("truong hop DAC BIET, khong phai truong hop chung.")


# ---------------------------------------------------------------------------
# MUC 9. Hang hoa Giffen - Hinh 12, tr. 510-511
# ---------------------------------------------------------------------------
tieu_de(9, "Hang hoa Giffen - khi duong cau doc LEN")

# Mo hinh calo. Sach ke chuyen khoai tay o Ireland the ky 19 va nghien cuu cua
# Jensen - Miller o Ho Nam. Ca hai deu co chung mot co che: mot rang buoc DINH
# DUONG nam ben canh rang buoc ngan sach.
NGAN_SACH = 100      # nghin dong moi tuan
CALO_CAN = 2000      # calo toi thieu moi tuan
CALO_MOI_DON_VI = 100
GIA_THIT = 8         # nghin dong mot don vi (100 calo)
DON_VI_CAN = CALO_CAN // CALO_MOI_DON_VI     # tong so don vi thuc an can co


def gio_hang(gia_khoai, ngan_sach=NGAN_SACH):
    """Mua nhieu THIT nhat co the, mien la du calo va khong vuot ngan sach.

    khoai + thit = DON_VI_CAN (du calo)
    gia_khoai * khoai + GIA_THIT * thit <= ngan_sach
    """
    if gia_khoai * DON_VI_CAN > ngan_sach:
        return None                      # khong du tien de du calo
    thit = F(ngan_sach - gia_khoai * DON_VI_CAN, GIA_THIT - gia_khoai)
    thit = min(thit, DON_VI_CAN)
    return DON_VI_CAN - thit, thit


print(f"Mo hinh (khong co trong sach, dung de dung lai co che tr. 510-511):")
print(f"  Ngan sach {NGAN_SACH} nghin dong/tuan, can it nhat {tien(CALO_CAN)} calo.")
print(f"  Khoai tay va thit deu cho {CALO_MOI_DON_VI} calo mot don vi;"
      f" thit gia {GIA_THIT}, ngon hon.")
print(f"  Ho gia dinh mua NHIEU THIT NHAT co the, mien la du calo.")
print()
print(f"{'Gia khoai':>10} {'Khoai':>8} {'Thit':>8} {'Tien khoai':>12} {'Tien thit':>11}"
      f" {'Calo':>7}")
print(DONG)
for gia in (2, 3, 4, 5):
    kq = gio_hang(gia)
    if kq is None:
        print(f"{gia:>10}   khong du tien de dat {tien(CALO_CAN)} calo - doi mat nan doi")
        continue
    khoai, thit = kq
    print(f"{gia:>10} {so(khoai):>8} {so(thit):>8} {so(gia * khoai):>12}"
          f" {so(GIA_THIT * thit):>11} {tien((khoai + thit) * CALO_MOI_DON_VI):>7}")
print(DONG)
print("GIA KHOAI TANG TU 2 LEN 3 MA LUONG KHOAI MUA LAI TANG TU 10 LEN 12.")
print("Duong cau doc LEN. Do la hang hoa Giffen, dinh nghia o tr. 511.")
print()
print("Co che, doc thang tu bang: khoai len gia -> ho ngheo di -> khong con du tien")
print("mua thit -> phai lay calo tu nguon re nhat, ma nguon re nhat VAN LA KHOAI.")
print("Sach viet: 'tac dong thu nhap manh toi noi no VUOT QUA tac dong thay the'.")
print()

# Kiem lai lap luan cua Jensen - Miller: chi ho NGHEO moi co hanh vi Giffen
print("Nghien cuu tinh huong tr. 511 - Jensen va Miller o Ho Nam, Trung Quoc - noi")
print("ro rang chi nhung HO NGHEO moi the hien hanh vi Giffen. Kiem lai:")
print()
print(f"{'Ngan sach':>10} {'Khoai (gia 2)':>14} {'Khoai (gia 3)':>14}   Ket luan")
print(DONG)
for ns in (100, 120, 140, 160, 180):
    a = gio_hang(2, ns)
    b = gio_hang(3, ns)
    ka = min(a[0], DON_VI_CAN) if a else None
    kb = min(b[0], DON_VI_CAN) if b else None
    if ka is None or kb is None:
        ket = "khong du calo"
    elif kb > ka:
        ket = "GIFFEN - gia len, mua nhieu hon"
    elif kb == ka == 0:
        ket = "khong an khoai nua"
    else:
        ket = "binh thuong - gia len, mua it di"
    print(f"{tien(ns):>10} {so(ka):>14} {so(kb):>14}   {ket}")
print(DONG)
print("Nguong nam o ngan sach 160: tu do tro len, ho du tien mua toan thit va rang")
print("buoc calo khong con siet nua - hanh vi Giffen bien mat. Dung nhu Jensen va")
print("Miller tim thay: Giffen la hien tuong cua CAI NGHEO, khong phai cua hang hoa.")


# ---------------------------------------------------------------------------
# MUC 10. Cung lao dong cua Sally - Hinh 13 va Hinh 14
# ---------------------------------------------------------------------------
tieu_de(10, "Cung lao dong - vi sao luong tang chua chac lam viec nhieu hon")

GIO_THUC = 100          # so gio Sally thuc moi tuan (tr. 512)
LUONG_CU, LUONG_MOI = 50, 60

# Thoi gian nhan roi cung la mot "hang hoa", va GIA cua no chinh la muc luong.
# Tong nguon luc = 100 gio x luong. Dung lai ho CES nhu muc 8.


def lua_chon_lao_dong(luong, sigma, A, B):
    """Tra ve (so gio nhan roi, muc tieu dung)."""
    tong = GIO_THUC * luong               # thu nhap neu lam viec toan bo
    nhan_roi = cau_ces(tong, luong, 1, sigma, B, A)
    nhan_roi = min(nhan_roi, GIO_THUC)
    return nhan_roi, F(tong) - luong * nhan_roi


# Hieu chinh sao cho o muc luong 50 do la, Sally nghi 60 gio va tieu 2.000 do la
# - dung ba con so ma sach in o tr. 512.
def hieu_chinh_lao_dong(sigma):
    """Chon A (tieu dung), B (nhan roi) de o luong 50 thi nhan roi dung 60 gio."""
    # nhan_roi = tong*B*w^-s / (A*1 + B*w^(1-s)) = 60  voi tong = 100w
    #   <=> 100*B*w^(1-s) = 60*A + 60*B*w^(1-s)  <=>  40*B*w^(1-s) = 60*A
    A = 2 * F(LUONG_CU) ** (1 - sigma)
    return A, F(3)


print(f"Sally thuc {GIO_THUC} gio mot tuan, luong {LUONG_CU} do la/gio (tr. 512).")
print("Thoi gian nhan roi cung la mot hang hoa - va GIA cua no chinh la muc luong:")
print("bo mot gio nhan roi thi duoc them dung mot muc luong de tieu dung.")
print()
A0, B0 = hieu_chinh_lao_dong(1)
nr, td = lua_chon_lao_dong(LUONG_CU, 1, A0, B0)
print(f"Kiem lai ba con so sach in o tr. 512:")
print(f"  Nghi het {GIO_THUC} gio  -> tieu dung {tien(0)} do la")
print(f"  Lam het {GIO_THUC} gio   -> tieu dung {tien(GIO_THUC * LUONG_CU)} do la")
print(f"  Lam {so(GIO_THUC - nr)} gio    -> nghi {so(nr)} gio,"
      f" tieu dung {tien(td)} do la")
print("  Sach viet: 'Neu co lam viec binh thuong o muc 40 gio mot tuan, co co 60 gio")
print("  de nghi ngoi va co muc chi tieu hang tuan la 2.000 do la.' Khop ca ba.")
print()
print(f"Bay gio cho luong tang {LUONG_CU} -> {LUONG_MOI} do la/gio (tr. 513), voi ba")
print("kieu so thich khac nhau - van la mot num sigma nhu muc 8:")
print()
print(f"{'sigma':>6}  {'Nhan roi va tien la':<26} {'Nghi (gio)':>11} {'Lam (gio)':>10} {'Tieu dung':>11}")
print(DONG)
for sigma, nhan in [(0, "bo sung: nghi phai co tien"),
                    (1, "trung gian"),
                    (2, "thay the: tien bu duoc gio")]:
    A, B = hieu_chinh_lao_dong(sigma)
    nr0, td0 = lua_chon_lao_dong(LUONG_CU, sigma, A, B)
    nr1, td1 = lua_chon_lao_dong(LUONG_MOI, sigma, A, B)
    print(f"{sigma:>6}  {nhan:<26} {thap_phan(nr1):>11} {thap_phan(GIO_THUC - nr1):>10}"
          f" {thap_phan(td1):>11}")
print(DONG)
print(f"(Ca ba deu xuat phat tu nghi {so(nr)} gio, lam {GIO_THUC - nr} gio khi luong la {LUONG_CU}.)")
print(f"(Nghiem la phan so: sigma=0 cho nghi dung {so(F(450, 7))} gio,"
      f" sigma=2 cho {so(F(500, 9))} gio.)")
print()
print("Ba dong, ba ket cuc khac han nhau:")
print("  sigma = 0 -> nghi NHIEU hon, lam IT hon  => DUONG CUNG LAO DONG DOC XUONG")
print("               (Hinh 14b, tr. 513)")
print("  sigma = 1 -> khong doi gi ca             => duong cung THANG DUNG")
print("  sigma = 2 -> nghi IT hon, lam NHIEU hon  => DUONG CUNG DOC LEN (Hinh 14a)")
print()
print("Sach ket luan o tr. 514: 'ly thuyet kinh te khong cho thay mot su phan doan")
print("ro rang ve viec lieu mot su tang len trong muc luong khien co lam viec nhieu")
print("hon hay it hon.' Bang tren la cau do, viet bang so: KHONG PHAI ly thuyet yeu,")
print("ma la KET QUA THAT SU PHU THUOC vao mot tham so ma ly thuyet khong biet truoc.")
print()
print("Doc sigma = 0 cho de: 'nghi ma khong co tien tieu thi cung chang nghi duoc'.")
print("Di choi, du lich, so thich - deu ton tien. Voi nguoi nhu vay, luong tang la")
print("co hoi de NGHI NHIEU HON chu khong phai lam nhieu hon.")
print()
print("Va do dung la thu ma nghien cuu tinh huong tr. 514-515 tim thay:")
print("  - Mot tram nam truoc lam sau ngay/tuan; nay nam ngay - luong tang, gio giam.")
print("  - Nguoi trung xo so tren 50.000 do la: gan 25% nghi viec trong vong 1 nam.")
print("  - Nguoi trung tren 1 trieu do la: gan 40% ngung lam viec.")
print("  - Thua ke tren 150.000 do la: kha nang nghi viec cao GAP BON lan so voi")
print("    nguoi thua ke duoi 25.000 do la (Quarterly Journal of Economics, 1993).")
print("Nguoi trung so la bang chung sach nhat vi luong cua ho KHONG DOI - khong co")
print("tac dong thay the nao ca, chi con lai tac dong thu nhap thuan tuy.")


# ---------------------------------------------------------------------------
# MUC 11. Tiet kiem cua Sam - Hinh 15 va Hinh 16
# ---------------------------------------------------------------------------
tieu_de(11, "Tiet kiem - vi sao lai suat tang chua chac tiet kiem nhieu hon")

THU_NHAP_TRE = 100000
LAI_CU, LAI_MOI = F(1, 10), F(2, 10)


def lua_chon_tiet_kiem(lai, sigma, A, B):
    """Tra ve (tieu dung luc tre, tieu dung luc gia)."""
    gia_tuong_lai = F(1) / (1 + lai)      # gia hom nay cua mot dong ngay mai
    tre = cau_ces(THU_NHAP_TRE, 1, gia_tuong_lai, sigma, A, B)
    tre = min(tre, F(THU_NHAP_TRE))
    return tre, (F(THU_NHAP_TRE) - tre) * (1 + lai)


def hieu_chinh_tiet_kiem(sigma):
    """Chon A, B de o lai suat 10% thi Sam tieu dung dung 50.000 luc tre."""
    # tre = M*A*1 / (A*1 + B*p^(1-s)) = M/2  <=>  A = B*p^(1-s)
    p = F(1) / (1 + LAI_CU)
    return p ** (1 - sigma), F(1)


A0, B0 = hieu_chinh_tiet_kiem(1)
tre0, gia0 = lua_chon_tiet_kiem(LAI_CU, 1, A0, B0)
print(f"Sam kiem {tien(THU_NHAP_TRE)} do la luc tre, khong kiem gi luc gia (tr. 515).")
print(f"Lai suat {so(LAI_CU * 100)}%: moi do la de danh luc tre thanh"
      f" {thap_phan(1 + LAI_CU)} do la luc gia.")
print()
print("Kiem lai ba con so sach in o tr. 516:")
print(f"  Khong tiet kiem gi -> tieu {tien(THU_NHAP_TRE)} luc tre, {tien(0)} luc gia")
print(f"  Tiet kiem tat ca   -> tieu {tien(0)} luc tre,"
      f" {tien(THU_NHAP_TRE * (1 + LAI_CU))} luc gia")
print(f"  Diem toi uu        -> tieu {tien(tre0)} luc tre, {tien(gia0)} luc gia")
print("  Sach viet: 'Sam tieu dung 50.000 do la luc tre va 55.000 do la khi ve gia.'")
print("  Khop ca ba.")
print()
print(f"Bay gio cho lai suat tang {so(LAI_CU * 100)}% -> {so(LAI_MOI * 100)}% (tr. 516):")
print()
print(f"{'sigma':>6}  {'Hai giai doan la':<26} {'Tieu luc tre':>13} {'Tiet kiem':>11} {'Tieu luc gia':>13}")
print(DONG)
for sigma, nhan in [(0, "bo sung"), (1, "trung gian"), (2, "de thay the")]:
    A, B = hieu_chinh_tiet_kiem(sigma)
    tre1, gia1 = lua_chon_tiet_kiem(LAI_MOI, sigma, A, B)
    print(f"{sigma:>6}  {nhan:<26} {thap_phan(tre1):>13}"
          f" {thap_phan(THU_NHAP_TRE - tre1):>11} {thap_phan(gia1):>13}")
print(DONG)
print(f"(Ca ba deu xuat phat tu tiet kiem {tien(THU_NHAP_TRE - tre0)} do la o lai suat"
      f" {so(LAI_CU * 100)}%.)")
print()
print("  sigma = 0 -> tiet kiem GIAM  => Hinh 16b, tr. 517")
print("  sigma = 1 -> tiet kiem KHONG DOI")
print("  sigma = 2 -> tiet kiem TANG  => Hinh 16a, tr. 517")
print()
print("Cung mot cau truc voi muc 10, cung mot num sigma. Va sach rut ra mot he qua")
print("chinh sach rat that o tr. 517-518:")
print()
print("  'Mot so nha kinh te da keu goi giam thue danh vao tien lai va thu nhap tren")
print("   von. Ho lap luan rang mot chinh sach giam thue se lam tang muc lai suat sau")
print("   thue... Nhung nha kinh te khac da lap luan rang vi su bu tru cua tac dong")
print("   thu nhap va tac dong thay the, mot chinh sach nhu vay CO THE KHONG LAM TANG")
print("   TIET KIEM va tham chi CO THE LAM GIAM no.'")
print()
print("Ca hai phe deu dung ve mat ly thuyet. Cau hoi 'sigma bang bao nhieu' la mot")
print("cau hoi THUC NGHIEM, va sach thua nhan o tr. 518 rang 'cac nghien cuu da khong")
print("mang toi mot su dong thuan'.")


# ---------------------------------------------------------------------------
# MUC 12. [QTKD] Chia ngan sach marketing bang dung quy tac cua muc 4
# ---------------------------------------------------------------------------
tieu_de(12, "[QTKD] Chia ngan sach marketing - dung quy tac MU/P cua muc 4")

# Don vi: moi "khoi" la 10 trieu dong. Ngan sach 100 trieu = 10 khoi.
SO_KHOI = 10
KENH = {
    "Tim kiem": [420 - 40 * k for k in range(1, 11)],
    "Mang XH":  [250 - 25 * k for k in range(1, 11)],
}

print("Bai toan: 100 trieu dong ngan sach quang cao, chia cho hai kenh. Moi kenh co")
print("LOI ICH BIEN GIAM DAN - 10 trieu dau bao gio cung hieu qua hon 10 trieu thu tam.")
print()
print(f"{'Khoi 10 trieu thu':<20}" + "".join(f"{k:>5}" for k in range(1, 11)))
print(DONG)
for ten, ds in KENH.items():
    print(f"{ten + ' (lead)':<20}" + "".join(f"{v:>5}" for v in ds))
print(DONG)
print()

# Quy tac cua muc 4, phien ban roi rac: luon tieu dong tiep theo vao cho co
# loi ich bien tren mot dong CAO NHAT. Vi hai kenh cung gia moi khoi, chi can
# so sanh loi ich bien.
ung_vien = [(v, ten, i) for ten, ds in KENH.items() for i, v in enumerate(ds)]
ung_vien.sort(key=lambda t: (-t[0], t[1], t[2]))
chon = ung_vien[:SO_KHOI]
phan_bo = {ten: sum(1 for _, t, _ in chon if t == ten) for ten in KENH}
tong_toi_uu = sum(v for v, _, _ in chon)

print("Ap dung quy tac: moi khoi tiep theo dat vao noi co loi ich bien cao nhat.")
print()
print(f"{'Khoi':>5} {'Dat vao':<12} {'Lead them':>10}   Vi sao")
print(DONG)
for n, (v, ten, i) in enumerate(chon, 1):
    kia = [k for k in KENH if k != ten][0]
    da_dung = sum(1 for _, t, _ in chon[:n - 1] if t == kia)
    doi_thu = KENH[kia][da_dung] if da_dung < len(KENH[kia]) else 0
    print(f"{n:>5} {ten:<12} {v:>10}   so voi {doi_thu} neu dat vao {kia}")
print(DONG)
for ten, n in phan_bo.items():
    print(f"  {ten:<12} {n} khoi = {n * 10} trieu, thu ve {tien(sum(KENH[ten][:n]))} lead")
print(f"  {'TONG':<12} {SO_KHOI} khoi = 100 trieu, thu ve {tien(tong_toi_uu)} lead")
print()

# Kiem dieu kien bien - phien ban roi rac cua MU_x/P_x = MU_y/P_y
bien_cuoi = min(v for v, _, _ in chon)
bien_bo = max(v for v, ten, i in ung_vien if (v, ten, i) not in chon)
print("Kiem dieu kien bien (muc 4, ban roi rac):")
print(f"  Loi ich bien THAP NHAT trong so cac khoi da dat : {bien_cuoi} lead")
print(f"  Loi ich bien CAO NHAT trong so cac khoi bo lai   : {bien_bo} lead")
print(f"  Da dat >= bo lai? {bien_cuoi >= bien_bo}  -> khong the cai thien bang cach doi cho.")
print("Do la MU_A/P_A = MU_B/P_B cua tr. 504, chi khac la tien di tung khoi 10 trieu")
print("nen hai ve chi 'gan bang' chu khong bang chan.")
print()

# Do thi ASCII: tong lead theo so khoi danh cho kenh Tim kiem
print("Tong lead theo cach chia (truc ngang: so khoi cho Tim kiem):")
print()
tong_theo = []
for a in range(SO_KHOI + 1):
    b = SO_KHOI - a
    tong_theo.append(sum(KENH["Tim kiem"][:a]) + sum(KENH["Mang XH"][:b]))
dinh, day = max(tong_theo), min(tong_theo)
CAO = 12
for hang in range(CAO, -1, -1):
    nguong = day + (dinh - day) * hang / CAO
    dong = "".join("  #  " if t >= nguong else "     " for t in tong_theo)
    print(f"  {round(nguong):>5} |{dong}")
print("        +" + "-" * (5 * (SO_KHOI + 1)))
print("         " + "".join(f"{a:>3}  " for a in range(SO_KHOI + 1)))
print()
print(f"{'Cach chia':<34} {'Tong lead':>10} {'Mat so voi toi uu':>19}")
print(DONG)
for nhan, a in [("Toi uu (quy tac bien)", phan_bo["Tim kiem"]),
                ("Chia doi 50/50", 5),
                ("Don het vao Tim kiem", 10),
                ("Don het vao Mang XH", 0)]:
    t = tong_theo[a]
    mat = tong_toi_uu - t
    pct = thap_phan(F(mat * 100, tong_toi_uu), 1) + "%" if mat else "-"
    print(f"{nhan + f'  ({a}/{SO_KHOI - a})':<34} {tien(t):>10}"
          f" {(tien(mat) + '  ' + pct) if mat else '-':>19}")
print(DONG)
print()
print("Hai bai hoc, va cai thu hai quan trong hon:")
print()
print("  1. Quy tac dung la 'CAN BANG LOI ICH BIEN TREN MOT DONG', khong phai 'chia")
print("     deu' va cung khong phai 'don het vao kenh manh nhat'.")
print()
print("  2. Dinh cua duong cong RAT PHANG con hai dau thi DOC DUNG. Chia 5/5 thay vi")
mat_5 = tong_toi_uu - tong_theo[5]
mat_cd = tong_toi_uu - min(tong_theo[0], tong_theo[10])
print(f"     {phan_bo['Tim kiem']}/{phan_bo['Mang XH']} chi mat {tien(mat_5)} lead"
      f" ({thap_phan(F(mat_5 * 100, tong_toi_uu), 1)}%) - gan nhu khong dang ke.")
print(f"     Nhung don het 100 trieu vao mot kenh thi mat toi {tien(mat_cd)} lead"
      f" ({thap_phan(F(mat_cd * 100, tong_toi_uu), 1)}%).")
print()
print("     Nghia la: dung mat thoi gian tinh toan de di tu 5/5 sang 6/4. Hay dung")
print("     thoi gian do de dam bao ban KHONG dang o 10/0 hay 0/10. Sai lam dat tien")
print("     trong phan bo nguon luc gan nhu luon la sai lam CUC DOAN.")
```

**Kết quả chạy thật:**

```

==========================================================================
MUC 1. Duong rang buoc ngan sach - Hinh 1, tr. 497
==========================================================================
Thu nhap 1.000 do la/thang; pizza 10 do la/chiec; Pepsi 2 do la/chai.
Rang buoc: 10 x pizza + 2 x pepsi = 1.000

  Pizza   Pepsi   Tien pizza   Tien Pepsi       Tong   Sach in   Khop
--------------------------------------------------------------------------
    100       0        1.000            0      1.000         0   True
     90      50          900          100      1.000        50   True
     80     100          800          200      1.000       100   True
     70     150          700          300      1.000       150   True
     60     200          600          400      1.000       200   True
     50     250          500          500      1.000       250   True
     40     300          400          600      1.000       300   True
     30     350          300          700      1.000       350   True
     20     400          200          800      1.000       400   True
     10     450          100          900      1.000       450   True
      0     500            0        1.000      1.000       500   True
--------------------------------------------------------------------------
Khop 11/11 dong. Cot 'Tong' bang 1.000 o moi dong -
do chinh la y nghia cua tu 'rang buoc'.

Do doc = 500 chai Pepsi / 100 chiec pizza = 5 chai tren 1 chiec.
Va cung bang gia tuong doi: 10 / 2 = 5.
Hai cach tinh, mot con so. Do doc duong ngan sach CHINH LA gia tuong doi.

==========================================================================
MUC 2. Duong bang quan - ty le thay the bien giam dan
==========================================================================
Ham thoa dung dung o day: U = pizza x pepsi   (duong bang quan U = 12.500)
Sach khong cho ham nay - day la ham gon nhat co du bon tinh chat tr. 499-500.

  Pizza     Pepsi          U        MRS   Doc la
--------------------------------------------------------------------------
     10     1.250     12.500        125   it pizza -> doi nhieu Pepsi moi chiu bo 1 chiec
     25       500     12.500         20   it pizza -> doi nhieu Pepsi moi chiu bo 1 chiec
     50       250     12.500          5   vung giua
    100       125     12.500        5/4   nhieu pizza -> bo 1 chiec chi can it Pepsi
    125       100     12.500        4/5   nhieu pizza -> bo 1 chiec chi can it Pepsi
--------------------------------------------------------------------------
MRS giam don dieu tu 125 xuong 0,8 khi di sang phai. Do chinh la TINH CHAT 4
(tr. 500): duong bang quan CONG VE GOC TOA DO. Sach giai thich bang mot cau
rat doi thuong: 'con nguoi thuong san long trao doi hang hoa ma ho co nhieu'.

Bon tinh chat, kiem tung cai bang so:
  1. Duong cao hon duoc ua thich hon: U=25.000 > U=12.500. Tai pizza=50,
     duong tren cho 500 chai Pepsi thay vi 250. Nhieu hon that.
  2. Doc xuong: pizza 10 -> 125 thi Pepsi 1.250 -> 100. Mot len thi mot xuong.
  3. Khong cat nhau: neu pizza x pepsi = 12.500 VA = 25.000 tai cung mot diem
     thi 12.500 = 25.000. Vo ly. Hai duong khac muc thi khong the giao nhau.
  4. Cong ve goc toa do: bang MRS o tren.

==========================================================================
MUC 3. Hai truong hop dac biet - Hinh 5, tr. 502
==========================================================================
(a) THAY THE HOAN HAO - dong 5 cent va dong 10 cent (tr. 501)
    Ban chi quan tam tong so tien, nen MRS la mot hang so.

     Dong 10c   Dong 5c   Tong (cent)    MRS
    ------------------------------------------
            0         6            30      2
            1         4            30      2
            2         2            30      2
            3         0            30      2
    ------------------------------------------
    MRS = 2 o MOI diem -> duong bang quan la duong THANG.

(b) BO SUNG HOAN HAO - giay trai va giay phai (tr. 501)
    Ban chi quan tam so DOI giay: so doi = min(trai, phai).

      Trai   Phai   So doi   Doc la
    ----------------------------------------------------
         5      5        5   vua du
         5      7        5   thua 2 chiec, vo dung
         7      5        5   thua 2 chiec, vo dung
         7      7        7   vua du
    ----------------------------------------------------
    (5,5) va (5,7) va (7,5) deu cho 5 doi -> BANG QUAN. Duong bang quan
    la goc VUONG. Sach viet: 'Co them mot chiec ben phai luc nay cha co y
    nghia gi neu khong co mot chiec ben trai di kem.'

Hai truong hop nay la HAI DAU MUT cua mot thang do. Muc 8 se dat ten
cho thang do do va cho thay no quyet dinh gan nhu moi ket luan con lai.

==========================================================================
MUC 4. Diem toi uu - noi hai duong tiep tuyen nhau
==========================================================================
Diem toi uu: 50 chiec pizza va 250 chai Pepsi.
  Chi cho pizza: 500 do la
  Chi cho Pepsi: 500 do la
  Cong          : 1.000 do la  (dung bang thu nhap)

Day chinh la DIEM C tren Hinh 1, tr. 496 - diem ma sach mo ta la
'nguoi tieu dung chi tieu nhung khoan bang nhau (500 do la) cho hai mat hang'.

Kiem dieu kien tiep tuyen ma sach nhan manh o tr. 503:
  Do doc duong bang quan (MRS)      = 5
  Do doc duong ngan sach (gia t.doi) = 5
  Bang nhau? True

Hop 'Ban co biet' tr. 504 viet lai dieu kien do bang do thoa dung bien:
  MU_pizza / P_pizza = 250 / 10 = 25
  MU_pepsi / P_pepsi = 50 / 2 = 25
  Bang nhau? True

Doc cau nay cham: MOT DO LA CHI THEM VAO PIZZA MANG LAI DUNG BANG MOT DO LA
CHI THEM VAO PEPSI. Neu khong bang, chuyen tien tu ben thap sang ben cao la
loi ngay - nen chua the goi la toi uu. Muc 12 dung dung quy tac nay cho mot
bai toan chia ngan sach marketing.

Sach ve them hai diem de doi chieu (tr. 503):
  Diem A: 70 pizza + 400 Pepsi = 1.500 do la -> TREN duong ngan sach - khong voi toi
           U = 28.000 (toi uu la 12.500)
  Diem B: 20 pizza + 300 Pepsi = 800 do la -> DUOI duong ngan sach - con thua tien
           U = 6.000 (toi uu la 12.500)
  A thi thich hon nhung KHONG DU TIEN. B thi du tien nhung THOA DUNG THAP HON.

==========================================================================
MUC 5. Thu nhap tang - hang hoa thong thuong va hang hoa thu cap
==========================================================================
  Thu nhap    Pizza    Pepsi   Nhan xet
--------------------------------------------------------------------------
     1.000       50      250   
     1.200       60      300   ca hai cung tang -> deu la HANG HOA THONG THUONG
     1.500       75      375   ca hai cung tang -> deu la HANG HOA THONG THUONG
     2.000      100      500   ca hai cung tang -> deu la HANG HOA THONG THUONG
--------------------------------------------------------------------------
Duong ngan sach dich chuyen SONG SONG ra ngoai: gia khong doi nen do doc
van la 5. Do la Hinh 7, tr. 505.

Hinh 8 (tr. 506) ve truong hop nguoc lai: thu nhap tang ma mua IT Pepsi di.
Ham U = pizza x pepsi khong bao gio tao ra ket cuc do - no luon cho ra hang
hoa thong thuong. Muon co hang hoa THU CAP thi phai doi so thich, va muc 9
se dung dung mot mo hinh nhu vay (mo hinh calo) de dung ra hang hoa Giffen.

Vi du hang hoa thu cap ma sach dua ra o tr. 506: cac chuyen XE BUYT.
'Khi thu nhap tang len, nhung nguoi tieu dung thuong se mua xe hoi hoac di
taxi va it khi di xe buyt.'

==========================================================================
MUC 6. Gia Pepsi giam - tach tac dong thu nhap va tac dong thay the
==========================================================================
Gia Pepsi giam tu 2 xuong 1 do la (tr. 506).
Gio hang cu (50 pizza, 250 Pepsi) o gia moi chi con ton 750 do la
thay vi 1.000 -> nguoi tieu dung tu nhien giau len 250 do la.

Buoc                                   Pizza     Pepsi   Thu nhap
--------------------------------------------------------------------------
A. Ban dau                                50       250      1.000
B. Chi doi GIA, bu lai thu nhap         75/2       375        750
C. Tra lai phan thu nhap da bu            50       500      1.000
--------------------------------------------------------------------------
  A -> B  TAC DONG THAY THE            -25/2       125
  B -> C  TAC DONG THU NHAP             25/2       125
  A -> C  TONG                             0       250
--------------------------------------------------------------------------

Doi chieu voi Bang 1, tr. 508 - sach ket luan bang loi, day la bang so:

  PEPSI : thay the  +125  va thu nhap  +125  -> CUNG CHIEU, tong  +250
          Sach: 'tac dong thu nhap va tac dong thay the xay ra theo cung
          chieu huong, vi vay nguoi tieu dung se mua nhieu Pepsi hon.' Dung.

  PIZZA : thay the -25/2  va thu nhap +25/2  -> NGUOC CHIEU, tong     0
          Sach: 'tong tac dong len tieu dung pizza la KHONG RO RANG.' Dung -
          va o day hai tac dong triet tieu nhau HOAN TOAN. Muc 8 giai thich
          vi sao dieu do khong phai tinh co.

==========================================================================
MUC 7. Dung duong cau tu cac diem toi uu - Hinh 11, tr. 509
==========================================================================
Duong cau khong phai mot gia dinh - no la TAP HOP CAC DIEM TOI UU khi cho
gia chay. Cho gia Pepsi chay tu 5 do la xuong 1 do la, ghi lai luong toi uu:

 Gia Pepsi    Pizza    Pepsi   Chi cho Pepsi
--------------------------------------------------------------------------
         5       50      100             500
         4       50      125             500
       5/2       50      200             500
         2       50      250             500
       5/4       50      400             500
         1       50      500             500
--------------------------------------------------------------------------
Ba dieu bang nay noi ngay:
  - Gia xuong thi luong len -> DUONG CAU DOC XUONG. Khong gia dinh gi ca,
    no roi ra tu ban than viec toi uu hoa.
  - Luong pizza KHONG DOI dung 50 chiec o moi muc gia Pepsi.
  - Chi tieu cho Pepsi KHONG DOI dung 500 do la -> do co gian bang 1 chan.

So voi Hinh 11 cua sach:
  Sach : gia 2 -> 1 do la thi Pepsi 250 -> 750 chai
  Ham U = pizza x pepsi : 250 -> 500 chai

KHONG KHOP, va cho lech nay la cho hoc duoc nhieu nhat trong ca bai.
Ham U = pizza x pepsi luon giu chi tieu cho moi mat hang o dung mot nua thu
nhap, nen no KHONG THE cho ra gap ba. De ra 750 chai, hai mat hang phai THAY
THE cho nhau de hon - tuc la duong bang quan phai THANG hon. Muc 8 do dieu do.

==========================================================================
MUC 8. Do cong cua duong bang quan - mot tham so, moi ket luan
==========================================================================
Ho ham CES cho phep xoay mot num duy nhat - do co gian thay the sigma -
de di tu 'bo sung hoan hao' sang 'thay the hoan hao'. Hieu chinh moi truong
hop sao cho diem xuat phat van dung la (50 pizza, 250 Pepsi).

 sigma  Hai mat hang la           Pepsi khi gia 2   khi gia 1
--------------------------------------------------------------------------
     0  bo sung hoan hao                      250      1000/3
     1  trung gian (U = x.y)                  250         500
     2  de thay the                           250      2000/3
     3  rat de thay the                       250         800
--------------------------------------------------------------------------
Con so cua sach o Hinh 11 la 750 chai - nam giua sigma = 2 va sigma = 3.
Giai nguoc phuong trinh 1000 / (1 + 2^(1-sigma)) = 750:
  2^(1-sigma) = 1/3  ->  sigma = 1 + log2(3) = 2,5850

Nghia la: Hinh 11 cua sach duoc ve voi gia dinh ngam rang pizza va Pepsi
THAY THE cho nhau de gap khoang 2,6 lan muc trung gian. Sach khong noi
dieu do o dau ca - no nam trong do cong ma hoa si da ve.

Va day la cong thuc noi ca bai nay voi bai 3. Voi ho CES hai hang hoa, do co
gian cua cau theo gia tai diem ma hang hoa chiem ty phan s cua chi tieu la:

        |e| = sigma * (1 - s) + s

O diem xuat phat, Pepsi chiem s = 1/2 chi tieu. Vay:

 sigma   |e| = sigma(1-s) + s   Doc la
--------------------------------------------------------------------------
     0                    1/2   khong co gian
     1                      1   co gian don vi
     2                    3/2   co gian
     3                      2   co gian
--------------------------------------------------------------------------
sigma = 1 cho dung |e| = 1 - va do la ly do o muc 7 chi tieu cho Pepsi khong
doi du gia doi. Bai 3 goi do la 'cau co gian don vi'; bai nay cho thay no den
tu dau: tu DO CONG cua duong bang quan, chu khong phai tu mot con so troi oi.

Va cung tu do giai thich luon cho lech o muc 6: khi sigma = 1 thi tac dong
thay the va tac dong thu nhap len PIZZA triet tieu nhau chinh xac. Do la
truong hop DAC BIET, khong phai truong hop chung.

==========================================================================
MUC 9. Hang hoa Giffen - khi duong cau doc LEN
==========================================================================
Mo hinh (khong co trong sach, dung de dung lai co che tr. 510-511):
  Ngan sach 100 nghin dong/tuan, can it nhat 2.000 calo.
  Khoai tay va thit deu cho 100 calo mot don vi; thit gia 8, ngon hon.
  Ho gia dinh mua NHIEU THIT NHAT co the, mien la du calo.

 Gia khoai    Khoai     Thit   Tien khoai   Tien thit    Calo
--------------------------------------------------------------------------
         2       10       10           20          80   2.000
         3       12        8           36          64   2.000
         4       15        5           60          40   2.000
         5       20        0          100           0   2.000
--------------------------------------------------------------------------
GIA KHOAI TANG TU 2 LEN 3 MA LUONG KHOAI MUA LAI TANG TU 10 LEN 12.
Duong cau doc LEN. Do la hang hoa Giffen, dinh nghia o tr. 511.

Co che, doc thang tu bang: khoai len gia -> ho ngheo di -> khong con du tien
mua thit -> phai lay calo tu nguon re nhat, ma nguon re nhat VAN LA KHOAI.
Sach viet: 'tac dong thu nhap manh toi noi no VUOT QUA tac dong thay the'.

Nghien cuu tinh huong tr. 511 - Jensen va Miller o Ho Nam, Trung Quoc - noi
ro rang chi nhung HO NGHEO moi the hien hanh vi Giffen. Kiem lai:

 Ngan sach  Khoai (gia 2)  Khoai (gia 3)   Ket luan
--------------------------------------------------------------------------
       100             10             12   GIFFEN - gia len, mua nhieu hon
       120           20/3              8   GIFFEN - gia len, mua nhieu hon
       140           10/3              4   GIFFEN - gia len, mua nhieu hon
       160              0              0   khong an khoai nua
       180              0              0   khong an khoai nua
--------------------------------------------------------------------------
Nguong nam o ngan sach 160: tu do tro len, ho du tien mua toan thit va rang
buoc calo khong con siet nua - hanh vi Giffen bien mat. Dung nhu Jensen va
Miller tim thay: Giffen la hien tuong cua CAI NGHEO, khong phai cua hang hoa.

==========================================================================
MUC 10. Cung lao dong - vi sao luong tang chua chac lam viec nhieu hon
==========================================================================
Sally thuc 100 gio mot tuan, luong 50 do la/gio (tr. 512).
Thoi gian nhan roi cung la mot hang hoa - va GIA cua no chinh la muc luong:
bo mot gio nhan roi thi duoc them dung mot muc luong de tieu dung.

Kiem lai ba con so sach in o tr. 512:
  Nghi het 100 gio  -> tieu dung 0 do la
  Lam het 100 gio   -> tieu dung 5.000 do la
  Lam 40 gio    -> nghi 60 gio, tieu dung 2.000 do la
  Sach viet: 'Neu co lam viec binh thuong o muc 40 gio mot tuan, co co 60 gio
  de nghi ngoi va co muc chi tieu hang tuan la 2.000 do la.' Khop ca ba.

Bay gio cho luong tang 50 -> 60 do la/gio (tr. 513), voi ba
kieu so thich khac nhau - van la mot num sigma nhu muc 8:

 sigma  Nhan roi va tien la         Nghi (gio)  Lam (gio)   Tieu dung
--------------------------------------------------------------------------
     0  bo sung: nghi phai co tien       64,29      35,71    2.142,86
     1  trung gian                       60,00      40,00    2.400,00
     2  thay the: tien bu duoc gio       55,56      44,44    2.666,67
--------------------------------------------------------------------------
(Ca ba deu xuat phat tu nghi 60 gio, lam 40 gio khi luong la 50.)
(Nghiem la phan so: sigma=0 cho nghi dung 450/7 gio, sigma=2 cho 500/9 gio.)

Ba dong, ba ket cuc khac han nhau:
  sigma = 0 -> nghi NHIEU hon, lam IT hon  => DUONG CUNG LAO DONG DOC XUONG
               (Hinh 14b, tr. 513)
  sigma = 1 -> khong doi gi ca             => duong cung THANG DUNG
  sigma = 2 -> nghi IT hon, lam NHIEU hon  => DUONG CUNG DOC LEN (Hinh 14a)

Sach ket luan o tr. 514: 'ly thuyet kinh te khong cho thay mot su phan doan
ro rang ve viec lieu mot su tang len trong muc luong khien co lam viec nhieu
hon hay it hon.' Bang tren la cau do, viet bang so: KHONG PHAI ly thuyet yeu,
ma la KET QUA THAT SU PHU THUOC vao mot tham so ma ly thuyet khong biet truoc.

Doc sigma = 0 cho de: 'nghi ma khong co tien tieu thi cung chang nghi duoc'.
Di choi, du lich, so thich - deu ton tien. Voi nguoi nhu vay, luong tang la
co hoi de NGHI NHIEU HON chu khong phai lam nhieu hon.

Va do dung la thu ma nghien cuu tinh huong tr. 514-515 tim thay:
  - Mot tram nam truoc lam sau ngay/tuan; nay nam ngay - luong tang, gio giam.
  - Nguoi trung xo so tren 50.000 do la: gan 25% nghi viec trong vong 1 nam.
  - Nguoi trung tren 1 trieu do la: gan 40% ngung lam viec.
  - Thua ke tren 150.000 do la: kha nang nghi viec cao GAP BON lan so voi
    nguoi thua ke duoi 25.000 do la (Quarterly Journal of Economics, 1993).
Nguoi trung so la bang chung sach nhat vi luong cua ho KHONG DOI - khong co
tac dong thay the nao ca, chi con lai tac dong thu nhap thuan tuy.

==========================================================================
MUC 11. Tiet kiem - vi sao lai suat tang chua chac tiet kiem nhieu hon
==========================================================================
Sam kiem 100.000 do la luc tre, khong kiem gi luc gia (tr. 515).
Lai suat 10%: moi do la de danh luc tre thanh 1,10 do la luc gia.

Kiem lai ba con so sach in o tr. 516:
  Khong tiet kiem gi -> tieu 100.000 luc tre, 0 luc gia
  Tiet kiem tat ca   -> tieu 0 luc tre, 110.000 luc gia
  Diem toi uu        -> tieu 50.000 luc tre, 55.000 luc gia
  Sach viet: 'Sam tieu dung 50.000 do la luc tre va 55.000 do la khi ve gia.'
  Khop ca ba.

Bay gio cho lai suat tang 10% -> 20% (tr. 516):

 sigma  Hai giai doan la            Tieu luc tre   Tiet kiem  Tieu luc gia
--------------------------------------------------------------------------
     0  bo sung                        52.173,91   47.826,09     57.391,30
     1  trung gian                     50.000,00   50.000,00     60.000,00
     2  de thay the                    47.826,09   52.173,91     62.608,70
--------------------------------------------------------------------------
(Ca ba deu xuat phat tu tiet kiem 50.000 do la o lai suat 10%.)

  sigma = 0 -> tiet kiem GIAM  => Hinh 16b, tr. 517
  sigma = 1 -> tiet kiem KHONG DOI
  sigma = 2 -> tiet kiem TANG  => Hinh 16a, tr. 517

Cung mot cau truc voi muc 10, cung mot num sigma. Va sach rut ra mot he qua
chinh sach rat that o tr. 517-518:

  'Mot so nha kinh te da keu goi giam thue danh vao tien lai va thu nhap tren
   von. Ho lap luan rang mot chinh sach giam thue se lam tang muc lai suat sau
   thue... Nhung nha kinh te khac da lap luan rang vi su bu tru cua tac dong
   thu nhap va tac dong thay the, mot chinh sach nhu vay CO THE KHONG LAM TANG
   TIET KIEM va tham chi CO THE LAM GIAM no.'

Ca hai phe deu dung ve mat ly thuyet. Cau hoi 'sigma bang bao nhieu' la mot
cau hoi THUC NGHIEM, va sach thua nhan o tr. 518 rang 'cac nghien cuu da khong
mang toi mot su dong thuan'.

==========================================================================
MUC 12. [QTKD] Chia ngan sach marketing - dung quy tac MU/P cua muc 4
==========================================================================
Bai toan: 100 trieu dong ngan sach quang cao, chia cho hai kenh. Moi kenh co
LOI ICH BIEN GIAM DAN - 10 trieu dau bao gio cung hieu qua hon 10 trieu thu tam.

Khoi 10 trieu thu       1    2    3    4    5    6    7    8    9   10
--------------------------------------------------------------------------
Tim kiem (lead)       380  340  300  260  220  180  140  100   60   20
Mang XH (lead)        225  200  175  150  125  100   75   50   25    0
--------------------------------------------------------------------------

Ap dung quy tac: moi khoi tiep theo dat vao noi co loi ich bien cao nhat.

 Khoi Dat vao       Lead them   Vi sao
--------------------------------------------------------------------------
    1 Tim kiem            380   so voi 225 neu dat vao Mang XH
    2 Tim kiem            340   so voi 225 neu dat vao Mang XH
    3 Tim kiem            300   so voi 225 neu dat vao Mang XH
    4 Tim kiem            260   so voi 225 neu dat vao Mang XH
    5 Mang XH             225   so voi 220 neu dat vao Tim kiem
    6 Tim kiem            220   so voi 200 neu dat vao Mang XH
    7 Mang XH             200   so voi 180 neu dat vao Tim kiem
    8 Tim kiem            180   so voi 175 neu dat vao Mang XH
    9 Mang XH             175   so voi 140 neu dat vao Tim kiem
   10 Mang XH             150   so voi 140 neu dat vao Tim kiem
--------------------------------------------------------------------------
  Tim kiem     6 khoi = 60 trieu, thu ve 1.680 lead
  Mang XH      4 khoi = 40 trieu, thu ve 750 lead
  TONG         10 khoi = 100 trieu, thu ve 2.430 lead

Kiem dieu kien bien (muc 4, ban roi rac):
  Loi ich bien THAP NHAT trong so cac khoi da dat : 150 lead
  Loi ich bien CAO NHAT trong so cac khoi bo lai   : 140 lead
  Da dat >= bo lai? True  -> khong the cai thien bang cach doi cho.
Do la MU_A/P_A = MU_B/P_B cua tr. 504, chi khac la tien di tung khoi 10 trieu
nen hai ve chi 'gan bang' chu khong bang chan.

Tong lead theo cach chia (truc ngang: so khoi cho Tim kiem):

   2430 |                                #                      
   2321 |                           #    #    #    #            
   2212 |                      #    #    #    #    #            
   2104 |                      #    #    #    #    #    #       
   1995 |                 #    #    #    #    #    #    #    #  
   1886 |                 #    #    #    #    #    #    #    #  
   1778 |            #    #    #    #    #    #    #    #    #  
   1669 |            #    #    #    #    #    #    #    #    #  
   1560 |            #    #    #    #    #    #    #    #    #  
   1451 |       #    #    #    #    #    #    #    #    #    #  
   1342 |       #    #    #    #    #    #    #    #    #    #  
   1234 |       #    #    #    #    #    #    #    #    #    #  
   1125 |  #    #    #    #    #    #    #    #    #    #    #  
        +-------------------------------------------------------
           0    1    2    3    4    5    6    7    8    9   10  

Cach chia                           Tong lead   Mat so voi toi uu
--------------------------------------------------------------------------
Toi uu (quy tac bien)  (6/4)            2.430                   -
Chia doi 50/50  (5/5)                   2.375            55  2,3%
Don het vao Tim kiem  (10/0)            2.000          430  17,7%
Don het vao Mang XH  (0/10)             1.125        1.305  53,7%
--------------------------------------------------------------------------

Hai bai hoc, va cai thu hai quan trong hon:

  1. Quy tac dung la 'CAN BANG LOI ICH BIEN TREN MOT DONG', khong phai 'chia
     deu' va cung khong phai 'don het vao kenh manh nhat'.

  2. Dinh cua duong cong RAT PHANG con hai dau thi DOC DUNG. Chia 5/5 thay vi
     6/4 chi mat 55 lead (2,3%) - gan nhu khong dang ke.
     Nhung don het 100 trieu vao mot kenh thi mat toi 1.305 lead (53,7%).

     Nghia la: dung mat thoi gian tinh toan de di tu 5/5 sang 6/4. Hay dung
     thoi gian do de dam bao ban KHONG dang o 10/0 hay 0/10. Sai lam dat tien
     trong phan bo nguon luc gan nhu luon la sai lam CUC DOAN.
```

---

## 20. Tự thử

Mở [thuc_hanh/bai-10-lua-chon-nguoi-tieu-dung.py](../thuc_hanh/bai-10-lua-chon-nguoi-tieu-dung.py),
sửa rồi chạy lại. Không có lời giải kèm — chỗ học nằm ở việc đoán trước rồi xem mình đoán sai ở đâu.

1. **Đổi giá và thu nhập cùng lúc.** Nhân cả `THU_NHAP`, `GIA_PIZZA` và `GIA_PEPSI` với 2. Điểm tối ưu
   có đổi không? Kết quả này nói gì về câu *"lạm phát làm người ta nghèo đi"*? *(Đây chính là bài tập 3
   của sách, tr. 521.)*

2. **Đổi trọng số của hàm thoả dụng.** Trong `toi_uu_cobb_douglas`, đổi `trong_so_x` từ `F(1, 2)` sang
   `F(3, 4)`. Người này thích gì hơn? Tỷ phần chi tiêu cho pizza bây giờ là bao nhiêu, và nó có phụ
   thuộc vào giá không?

3. **Tìm σ từ dữ liệu.** Ở mục 8 của code, thêm σ = 4 và σ = 5 vào bảng. Lượng Pepsi ở giá $1 tiến tới
   giới hạn nào khi σ → ∞? Giải thích giới hạn đó bằng Hình 5(a).

4. **Đẩy mô hình Giffen tới chỗ gãy.** Ở mục 9 của code, hạ `GIA_THIT` từ 8 xuống 4. Hành vi Giffen còn
   không? Rồi nâng `CALO_CAN` lên 2.400. Ngưỡng ngân sách mà Giffen biến mất dịch đi đâu?

5. **Cung lao động cong ngược.** Ở mục 10 của code, cho lương chạy 40, 50, 60, 80, 100 với σ = 0 và vẽ
   số giờ làm việc theo lương. Đường cung lao động này có dạng gì? Nó có bao giờ **cong ngược lại**
   không, hay luôn dốc xuống?

6. **Lãi suất âm.** Ở mục 11 của code, đặt `LAI_MOI = F(-5, 100)`. Sam làm gì? Kết quả này có ý nghĩa
   gì với các nền kinh tế từng có lãi suất danh nghĩa âm (Nhật Bản, khu vực đồng euro những năm 2010)?

7. **💼 Ba kênh thay vì hai.** Ở mục 12 của code, thêm kênh thứ ba với lợi ích biên `[300 - 30*k]`. Quy
   tắc phân bổ có phải sửa gì không? Bây giờ tính lại: dồn hết vào một kênh mất bao nhiêu phần trăm so
   với tối ưu — nhiều hơn hay ít hơn trường hợp hai kênh, và vì sao?

---

## 21. Từ điển thuật ngữ

| Tiếng Việt                 | Tiếng Anh                       | Nghĩa                                                                                                       |
| -------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Ràng buộc ngân sách        | *budget constraint*             | giới hạn về gói hàng hoá mà người tiêu dùng có thể chi trả; độ dốc của nó **là giá tương đối**              |
| Đường bàng quan            | *indifference curve*            | tập hợp các gói hàng hoá đem lại **cùng một mức thoả mãn**                                                  |
| Tỷ lệ thay thế biên (MRS)  | *marginal rate of substitution* | tỷ lệ mà **người tiêu dùng** sẵn lòng đánh đổi hàng hoá này lấy hàng hoá kia; **là độ dốc đường bàng quan** |
| Độ thoả dụng               | *utility*                       | thước đo trừu tượng của sự thoả mãn                                                                         |
| Độ thoả dụng biên          | *marginal utility*              | mức thoả dụng tăng thêm từ một đơn vị hàng hoá nữa; thường **giảm dần**                                     |
| Hàng hoá thay thế hoàn hảo | *perfect substitutes*           | đường bàng quan **thẳng** — MRS là hằng số                                                                  |
| Hàng hoá bổ sung hoàn hảo  | *perfect complements*           | đường bàng quan **vuông góc** — thừa một bên là vô dụng                                                     |
| Hàng hoá thông thường      | *normal good*                   | thu nhập tăng → mua nhiều hơn                                                                               |
| Hàng hoá thứ cấp           | *inferior good*                 | thu nhập tăng → mua **ít** hơn (ví dụ của sách: xe buýt)                                                    |
| Tác động thu nhập          | *income effect*                 | phần thay đổi do người tiêu dùng **giàu hơn hoặc nghèo đi** — nhảy sang đường bàng quan khác                |
| Tác động thay thế          | *substitution effect*           | phần thay đổi do **giá tương đối** đổi — trượt dọc **cùng một** đường bàng quan                             |
| Hàng hoá Giffen            | *Giffen good*                   | giá tăng làm **tăng** lượng cầu; xảy ra khi tác động thu nhập lấn át tác động thay thế                      |
| Độ co giãn thay thế        | *elasticity of substitution*    | ký hiệu σ — đo **độ cong** của đường bàng quan; 0 là vuông góc, ∞ là thẳng. **Không có trong sách**         |

---

## 22. Câu hỏi tự kiểm tra

Trả lời rồi mới quay lại đối chiếu. Số trong ngoặc là mục chứa câu trả lời.

1. Chương này là "cặp đối xứng" của chương nào, và vì sao? *(mục 1)*
2. Độ dốc đường ngân sách bằng gì? Chứng minh bằng hai cách khác nhau. *(mục 2)*
3. Cả đường ngân sách lẫn đường bàng quan đều dốc xuống. Hai độ dốc đó khác nhau ở chỗ nào? *(mục 3)*
4. Chứng minh rằng hai đường bàng quan không thể cắt nhau. Bạn cần đúng mấy giả định? *(mục 4)*
5. Vẽ đường bàng quan cho: (a) hai tờ 50.000đ và một tờ 100.000đ; (b) cà phê và đường. Cái nào thẳng
   hơn? *(mục 5)*
6. Phát biểu điều kiện tối ưu bằng **hai** cách: bằng độ dốc, và bằng độ thoả dụng biên. Chứng minh hai
   cách đó tương đương. *(mục 6, 7)*
7. Vì sao "một đồng chi thêm vào X phải đáng giá bằng một đồng chi thêm vào Y" lại là điều kiện tối ưu?
   Chuyện gì xảy ra nếu không bằng? *(mục 7)*
8. Thu nhập tăng làm đường ngân sách **dịch song song**; giá đổi làm nó **xoay**. Vì sao khác nhau?
   *(mục 8, 9)*
9. Giá Pepsi giảm. Tách tác động lên **Pepsi** và lên **pizza** thành hai thành phần. Vì sao kết luận
   cho Pepsi thì rõ ràng còn cho pizza thì không? *(mục 9)*
10. Đường cầu đến từ đâu? Nói cách khác: nếu bạn chỉ có ràng buộc ngân sách và đường bàng quan, làm sao
    dựng ra được đường cầu? *(mục 10)*
11. σ là gì, và nó liên hệ thế nào với hai trường hợp đặc biệt ở mục 5? *(mục 11)*
12. Chứng minh rằng với $\sigma = 1$, chi tiêu cho một mặt hàng không đổi dù giá đổi. Suy ra độ co giãn.
    *(mục 11)*
13. Hàng hoá Giffen cần những điều kiện gì? Vì sao Jensen và Miller chỉ tìm thấy nó ở **hộ nghèo**?
    *(mục 12, 13)*
14. Mẹo nào cho phép dùng cùng một bộ máy cho bài toán làm việc – nghỉ ngơi? Giá của thời gian nhàn rỗi
    là gì? *(mục 14)*
15. Vì sao dữ liệu **người trúng số** lại sắc bén hơn dữ liệu tăng lương thông thường khi đo tác động
    thu nhập? *(mục 15)*
16. Hai nhà kinh tế tranh cãi xem giảm thuế lãi vốn có làm tăng tiết kiệm không. Cả hai đều đúng về lý
    thuyết. Điều gì quyết định ai đúng trên thực tế? *(mục 16)*
17. Sách thừa nhận không ai vẽ đường bàng quan khi đi siêu thị. Vậy lý thuyết này khẳng định điều gì?
    *(mục 17)*
18. 💼 Bạn có 100 triệu chia cho hai kênh quảng cáo. Quy tắc chia là gì? Và trong hai sai lầm — "chia
    5/5 thay vì 6/4" và "dồn hết vào một kênh" — cái nào đắt hơn, đắt hơn bao nhiêu lần? *(mục 18)*

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 10 — LỰA CHỌN CỦA NGƯỜI TIÊU DÙNG      (Mankiw ch.21, tr. 495-524)  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  CHÍN BÀI TRƯỚC dùng đường cầu dốc xuống như một DỮ KIỆN CHO SẴN.        ║
║  Bài này mở nắp ra: đường cầu KHÔNG PHẢI giả định, nó RƠI RA từ một      ║
║  bài toán tối ưu hoá có ràng buộc. Đây là cặp đối xứng của bài 6.        ║
║                                                                          ║
║  ── HAI NỬA CỦA BÀI TOÁN ─────────────────────────────────────────       ║
║                                                                          ║
║     RÀNG BUỘC NGÂN SÁCH   bạn MUA ĐƯỢC gì   10.pizza + 2.pepsi = 1000    ║
║        độ dốc = GIÁ TƯƠNG ĐỐI = 10/2 = 5      (thị trường quyết định)    ║
║                                                                          ║
║     ĐƯỜNG BÀNG QUAN       bạn MUỐN gì       U = pizza x pepsi            ║
║        độ dốc = TỶ LỆ THAY THẾ BIÊN (MRS)     (sở thích quyết định)      ║
║                                                                          ║
║     Bốn tính chất: cao hơn thì thích hơn · dốc xuống · không cắt nhau    ║
║                    · cong về gốc toạ độ (MRS giảm dần)                   ║
║                                                                          ║
║  ── ĐIỂM TỐI ƯU: NƠI HAI ĐƯỜNG TIẾP TUYẾN NHAU ────────────────────      ║
║                                                                          ║
║                        MU_x       MU_y                                   ║
║      MRS = P_x/P_y  <=>  ────  =  ────    50 pizza + 250 Pepsi           ║
║                         P_x        P_y     (đúng điểm C của Hình 1)      ║
║                                                                          ║
║     Đọc là: MỘT ĐỒNG CHI THÊM VÀO X ĐÁNG GIÁ ĐÚNG BẰNG MỘT ĐỒNG          ║
║     CHI THÊM VÀO Y. Nếu chưa bằng thì chuyển tiền sang là lời ngay.      ║
║                                                                          ║
║  ── GIÁ ĐỔI: TÁCH LÀM HAI ───────────────────────────────────────        ║
║                                                                          ║
║     TÁC ĐỘNG THAY THẾ   trượt DỌC cùng một đường bàng quan               ║
║     TÁC ĐỘNG THU NHẬP   NHẢY sang đường bàng quan khác                   ║
║                                                                          ║
║     Pepsi rẻ đi:  Pepsi  +125 và +125  -> CÙNG CHIỀU, tăng chắc chắn     ║
║                   pizza  -12,5 và +12,5 -> NGƯỢC CHIỀU, KHÔNG RÕ RÀNG    ║
║                                                                          ║
║  ── 📚 MỘT THAM SỐ GIẢI THÍCH CẢ BA CÂU HỎI CỦA CHƯƠNG ────────────      ║
║                                                                          ║
║     σ = ĐỘ CO GIÃN THAY THẾ = độ CONG của đường bàng quan                ║
║        σ = 0  vuông góc (bổ sung hoàn hảo)                               ║
║        σ = 1  U = x.y  -> hai tác động TRIỆT TIÊU NHAU                   ║
║        σ = ∞  thẳng (thay thế hoàn hảo)                                  ║
║                                                                          ║
║     |e| = σ(1-s) + s   <- cây cầu về bài 3. σ=1 cho |e|=1 đúng chằn.     ║
║                                                                          ║
║     Ba câu hỏi mở chương HOÁ RA LÀ MỘT:                                  ║
║        lương tăng -> làm nhiều hay ít?   σ<1 ít  · σ>1 nhiều             ║
║        lãi suất tăng -> tiết kiệm?       σ<1 giảm · σ>1 tăng             ║
║        Sách nói "không rõ ràng" — đúng, vì σ là câu hỏi THỰC NGHIỆM.     ║
║                                                                          ║
║  ── HÀNG HOÁ GIFFEN: KHI ĐƯỜNG CẦU DỐC LÊN ────────────────────────      ║
║                                                                          ║
║     Cần MỘT RÀNG BUỘC THỨ HAI (dinh dưỡng) bên cạnh ngân sách.           ║
║     Khoai lên giá 2 -> 3 mà lượng mua tăng 10 -> 12 đơn vị.              ║
║     Vì: nghèo đi -> hết tiền mua thịt -> lấy calo từ nguồn rẻ nhất,      ║
║         mà nguồn rẻ nhất VẪN LÀ KHOAI.                                   ║
║                                                                          ║
║     Ngân sách >= 160 thì ràng buộc calo hết siết -> GIFFEN BIẾN MẤT.     ║
║     => Giffen là hiện tượng của CÁI NGHÈO, không phải của hàng hoá.      ║
║        (Jensen & Miller, Hồ Nam — chỉ hộ nghèo mới có hành vi này)       ║
║                                                                          ║
║  ── 💼 GÓC QTKD ───────────────────────────────────────────────────      ║
║                                                                          ║
║     Chia 100 triệu cho hai kênh quảng cáo = ĐÚNG bài toán MU/P.          ║
║     Quy tắc: cân bằng LỢI ÍCH BIÊN TRÊN MỘT ĐỒNG, không phải chia đều.   ║
║                                                                          ║
║        Tối ưu 6/4    2.430 lead                                          ║
║        Chia 5/5      2.375 lead   mất  2,3%  <- gần như không đáng kể    ║
║        Dồn 10/0      2.000 lead   mất 17,7%                              ║
║        Dồn 0/10      1.125 lead   mất 53,7%  <- đây mới là chỗ chết      ║
║                                                                          ║
║     ĐỈNH RẤT PHẲNG, HAI ĐẦU DỐC ĐỨNG. Đừng tốn công đi từ 5/5 sang       ║
║     6/4; hãy lo chuyện bạn không đang ở 10/0. Sai lầm đắt tiền trong     ║
║     phân bổ nguồn lực gần như luôn là sai lầm CỰC ĐOAN.                  ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Sách gốc:** N. Gregory Mankiw, *Kinh tế học vi mô* (*Principles of Microeconomics*), bản dịch của
  Khoa Kinh tế, **ĐH Kinh tế TP.HCM**, Cengage Learning Asia.
  File: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  *(số trang sách = số trang PDF − 33)*
- **Chương 21 — Lý thuyết về sự lựa chọn của người tiêu dùng**, tr. 495–524 (PDF 528–557). Các mục được dùng:
  - Ba câu hỏi mở chương, tr. 496
  - *Giới hạn ngân sách: khả năng mua hàng của người tiêu dùng* và **Hình 1**, tr. 496–497
  - *Sự ưa thích: những gì mà người tiêu dùng muốn* — đường bàng quan và **Hình 2**, tr. 498
  - *Bốn tính chất của đường bàng quan* và **Hình 3**, **Hình 4**, tr. 499–501
  - *Hai trường hợp đặc biệt của đường bàng quan* và **Hình 5**, tr. 501–502
  - *Tối ưu hoá: người tiêu dùng sẽ chọn gì?* và **Hình 6**, tr. 502–503
  - Bạn có biết *Độ thoả dụng: một cách khác để diễn tả sở thích và sự tối ưu hoá*, tr. 504
  - *Tác động của thay đổi trong thu nhập* và **Hình 7**, **Hình 8**, tr. 504–506
  - *Tác động của thay đổi giá lên hành vi người tiêu dùng* và **Hình 9**, tr. 506–507
  - *Tác động thu nhập và tác động thay thế*, **Bảng 1** và **Hình 10**, tr. 507–509
  - *Xây dựng đường cầu* và **Hình 11**, tr. 509–510
  - *Có phải mọi đường cầu đều dốc xuống?* và **Hình 12** (hàng hoá Giffen), tr. 510–511
  - Nghiên cứu tình huống *Cuộc tìm kiếm các hàng hoá Giffen* — Robert Jensen và Nolan Miller, Hồ Nam, tr. 511
  - *Các mức lương ảnh hưởng đến cung lao động như thế nào?* và **Hình 13**, **Hình 14**, tr. 512–514
  - Nghiên cứu tình huống *Tác động thu nhập với cung lao động: những xu hướng lịch sử, những người
    trúng số và phán đoán của Carnegie*, tr. 514–515 (*Quarterly Journal of Economics*, 1993)
  - *Lãi suất tác động lên tiết kiệm của hộ gia đình như thế nào?* và **Hình 15**, **Hình 16**, tr. 515–518
  - *Kết luận: con người có thực sự nghĩ theo hướng này không?*, tr. 518
  - **Bài tập 3** (mọi giá và lương cùng tăng 10%), tr. 521
- **Ngoài sách:**
  - Hàm $U = \text{pizza} \times \text{Pepsi}$ ở [mục 3](#3-đường-bàng-quan-và-tỷ-lệ-thay-thế-biên) —
    sách chỉ vẽ hình, không cho hàm nào. Đây là hàm gọn nhất có đủ bốn tính chất của tr. 499–500.
  - Họ hàm CES và tham số σ ở [mục 11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại) —
    không có trong sách. Công thức $|e| = \sigma(1-s) + s$ là kết quả chuẩn của lý thuyết tiêu dùng.
  - Cách tách **Slutsky** dùng ở [mục 9](#9-giá-đổi--tách-tác-động-thu-nhập-và-tác-động-thay-thế) —
    sách dùng cách **Hicks**; khác biệt được nêu rõ tại chỗ.
  - Mô hình ràng buộc calo dựng ra hàng hoá Giffen ở [mục 12](#12-có-phải-mọi-đường-cầu-đều-dốc-xuống) —
    dựng riêng cho bài này để tái tạo cơ chế mà sách chỉ mô tả bằng lời.
  - Bài toán chia ngân sách marketing ở [mục 18](#18--chia-ngân-sách-marketing-bằng-đúng-quy-tắc-của-mục-6)
    — dựng riêng cho bài này.
- **Liên hệ chéo:**
  - [Bài 2](bai_02_cung_va_cau.md) — nơi đường cầu được cho sẵn; bài này chứng minh nó.
  - [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) — độ co giãn; [mục 11](#11--độ-cong-của-đường-bàng-quan-quyết-định-mọi-thứ-còn-lại)
    cho thấy nó đến từ độ cong của đường bàng quan.
  - [Bài 4](bai_04_thang_du_va_chi_phi_cua_thue.md) — giá sẵn lòng trả; mục 6 giải thích vì sao giá thị
    trường phản ánh giá trị người tiêu dùng đánh giá.
  - [Bài 6](bai_06_thi_truong_canh_tranh.md) — cặp đối xứng phía cung.
  - **Bài 11** (chương 22) — thông tin bất cân xứng và kinh tế học hành vi: hỏi thẳng rằng "phép ẩn dụ"
    ở [mục 17](#17-con-người-có-thực-sự-nghĩ-theo-hướng-này-không) hỏng ở đâu và hỏng theo quy luật nào.

<!-- BAN-DO -->

**Bản đồ khoá học**

|      # | Bài                                                                                    | Chương sách | Ưu tiên |
| -----: | -------------------------------------------------------------------------------------- | ----------- | :-----: |
|      1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)         | ch. 1–2     |    🎯    |
|      2 | [Cung và cầu](bai_02_cung_va_cau.md)                                                   | ch. 4       |    🎯    |
|      3 | [Độ co giãn và định giá](bai_03_do_co_gian_va_dinh_gia.md)                             | ch. 5       |   🎯⭐    |
|      4 | [Thặng dư và chi phí của thuế](bai_04_thang_du_va_chi_phi_cua_thue.md)                 | ch. 7–8     |    🔸    |
|      5 | [Chi phí sản xuất](bai_05_chi_phi_san_xuat.md)                                         | ch. 13      |    🎯    |
|      6 | [Doanh nghiệp trên thị trường cạnh tranh](bai_06_thi_truong_canh_tranh.md)             | ch. 14      |    🎯    |
|      7 | [Độc quyền và phân biệt giá](bai_07_doc_quyen_va_phan_biet_gia.md)                     | ch. 15      |    🎯    |
|      8 | [Cạnh tranh độc quyền và thương hiệu](bai_08_canh_tranh_doc_quyen.md)                  | ch. 16      |    🎯    |
|      9 | [Độc quyền nhóm và lý thuyết trò chơi](bai_09_doc_quyen_nhom_va_ly_thuyet_tro_choi.md) | ch. 17      |    🎯    |
| **10** | **Lựa chọn của người tiêu dùng** ← *bạn đang ở đây*                                    | ch. 21      |    🎯    |
|     11 | [Thông tin bất cân xứng và hành vi](bai_11_thong_tin_bat_can_xung.md)                  | ch. 22      |    🎯    |
|     12 | [Lao động, tiền lương, bất bình đẳng](bai_12_thi_truong_lao_dong.md)                   | ch. 18–20   |    🔸    |
|     13 | Chính phủ can thiệp thị trường *(chưa viết)*                                           | ch. 6, 12   |    🔸    |
|     14 | Thương mại, ngoại tác, hàng hoá công *(chưa viết)*                                     | ch. 3, 9–11 |    🔸    |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương quan trọng nhất với QTKD

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
