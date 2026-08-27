# Bài 2 — Cung và cầu

> Bài học dựng từ **Chương 4 — Các lực lượng cung và cầu trên thị trường** (tr. 77–102)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🎯 **Vòng 1** — bài bắt buộc. Đây là mô hình mà **mọi chương còn lại đều dùng lại**.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp phụ.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 1 — Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md),
> đặc biệt mục 15 về **dịch chuyển đường ↔ di chuyển dọc đường**.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Thị trường là gì](#1-thị-trường-là-gì)
- [2. Cạnh tranh là gì](#2-cạnh-tranh-là-gì)
- [3. Cầu — lượng cầu, quy luật cầu, biểu cầu, đường cầu](#3-cầu--lượng-cầu-quy-luật-cầu-biểu-cầu-đường-cầu)
- [4. Cầu thị trường là tổng của cầu cá nhân — cộng theo chiều NGANG](#4-cầu-thị-trường-là-tổng-của-cầu-cá-nhân--cộng-theo-chiều-ngang)
- [5. Năm yếu tố làm dịch chuyển đường cầu](#5-năm-yếu-tố-làm-dịch-chuyển-đường-cầu)
- [6. ⚠️ Dịch chuyển ĐƯỜNG hay di chuyển DỌC theo đường — chỗ sai nhiều nhất](#6--dịch-chuyển-đường-hay-di-chuyển-dọc-theo-đường--chỗ-sai-nhiều-nhất)
- [7. Nghiên cứu tình huống — hai cách giảm cầu thuốc lá](#7-nghiên-cứu-tình-huống--hai-cách-giảm-cầu-thuốc-lá)
- [8. Cung — lượng cung, quy luật cung, biểu cung, đường cung](#8-cung--lượng-cung-quy-luật-cung-biểu-cung-đường-cung)
- [9. Bốn yếu tố làm dịch chuyển đường cung](#9-bốn-yếu-tố-làm-dịch-chuyển-đường-cung)
- [10. Cân bằng — nơi hai đường gặp nhau](#10-cân-bằng--nơi-hai-đường-gặp-nhau)
- [11. Thặng dư và thiếu hụt — cơ chế đưa thị trường về cân bằng](#11-thặng-dư-và-thiếu-hụt--cơ-chế-đưa-thị-trường-về-cân-bằng)
- [12. Ba bước phân tích sự thay đổi của trạng thái cân bằng](#12-ba-bước-phân-tích-sự-thay-đổi-của-trạng-thái-cân-bằng)
- [13. Bảng 4 — chín ô, và vì sao hai ô ghi "không rõ"](#13-bảng-4--chín-ô-và-vì-sao-hai-ô-ghi-không-rõ)
- [14. 📚 Giá cả phân bổ nguồn lực — và tranh cãi về "giá cắt cổ"](#14--giá-cả-phân-bổ-nguồn-lực--và-tranh-cãi-về-giá-cắt-cổ)
- [15. Code minh hoạ](#15-code-minh-hoạ)
- [16. Tự thử](#16-tự-thử)
- [17. Từ điển thuật ngữ](#17-từ-điển-thuật-ngữ)
- [18. Câu hỏi tự kiểm tra](#18-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Thị trường là gì

Sách mở chương bằng bốn hiện tượng tưởng chẳng liên quan (tr. 77):

- Một đợt không khí lạnh đổ vào Florida → **giá nước cam** ở khắp Hoa Kỳ tăng.
- Thời tiết ấm lên vào mùa hè ở New England → **giá thuê phòng khách sạn** vùng Caribbean giảm mạnh.
- Chiến tranh bùng nổ ở Trung Đông → **giá xăng** ở Hoa Kỳ tăng và **giá xe Cadillac cũ** giảm.

Điểm chung: *"Tất cả chúng đều cho thấy sự vận hành của cung và cầu."*

> **Thị trường** (*market*): một nhóm những người mua và người bán của một hàng hoá hay dịch vụ cụ thể. (tr. 77)

Điều quan trọng trong định nghĩa này là nó **rất rộng**. Sách nêu hai đầu của quang phổ (tr. 78):

| Kiểu thị trường                         | Ví dụ của sách                 | Đặc điểm                                                                                       |
| --------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------- |
| Tổ chức **chặt chẽ**                    | thị trường nhiều loại nông sản | người mua và người bán gặp nhau ở **một thời gian và địa điểm cụ thể**, có **người xướng giá** |
| Tổ chức **kém chặt chẽ** (phổ biến hơn) | thị trường kem ở một thị trấn  | không ai xướng giá; mỗi người bán **tự niêm yết giá**, mỗi người mua tự quyết định mua ở đâu   |

Và câu kết luận đáng nhớ về thị trường kem: *"Ngay cả khi không được tổ chức, nhóm người mua và bán kem cũng hình thành một thị trường."*

⚠️ **Thị trường không cần có một cái chợ.** Nó là một **quan hệ**, không phải một địa điểm. Điều này quan trọng khi bạn đi làm: "thị trường của chúng ta" không phải cái sàn thương mại điện tử bạn đang bán, mà là tập hợp mọi người mua và mọi người bán loại sản phẩm đó.

### 💼 Góc QTKD — định nghĩa thị trường sai là sai từ gốc

Câu hỏi *"thị trường của ta là gì"* quyết định mọi con số sau đó — thị phần, đối thủ, quy mô tăng trưởng.

| Cách định nghĩa                                  | Thị phần của một quán cà phê | Kết luận rút ra              |
| ------------------------------------------------ | ---------------------------- | ---------------------------- |
| "thị trường cà phê pha máy trong bán kính 500 m" | 40%                          | *"ta đang thống lĩnh"*       |
| "thị trường đồ uống mang đi trong quận"          | 3%                           | *"ta là người chơi nhỏ"*     |
| "thị trường mọi thứ khách có thể uống buổi sáng" | 0,2%                         | *"ta gần như không tồn tại"* |

Không có định nghĩa nào **đúng tuyệt đối**. Cái đúng là cái bao gồm **những thứ khách hàng thật sự cân nhắc thay cho sản phẩm của bạn** — tức là những **hàng hoá thay thế**, khái niệm sẽ gặp ở mục 5.

---

## 2. Cạnh tranh là gì

> **Thị trường cạnh tranh** (*competitive market*): một thị trường có nhiều người bán và người mua, mỗi người không có khả năng ảnh hưởng đến giá thị trường. — chú thích tr. 78

Sách giải thích qua thị trường kem: mỗi người bán kem *"có khả năng kiểm soát giá kem rất hạn chế"* vì người khác cũng bán loại tương tự — bán cao hơn thì mất khách, bán thấp hơn thì không có lý do gì (tr. 78).

**Cạnh tranh hoàn hảo** đòi hỏi **hai** đặc trưng (tr. 78):

```
CẠNH TRANH HOÀN HẢO
 ├── (1) các sản phẩm được bán phải GIỐNG NHAU HOÀN TOÀN
 └── (2) số người mua và người bán QUÁ LỚN, không cá nhân nào tác động được giá
        ⟹ mọi người đều là NGƯỜI CHẤP NHẬN GIÁ (price taker)
```

Ở mức giá thị trường, **người mua mua bao nhiêu cũng được, người bán bán bao nhiêu cũng được** (tr. 78).

Ba loại thị trường mà sách phân biệt:

| Loại                                                                 | Ví dụ của sách                                          | tr. |
| -------------------------------------------------------------------- | ------------------------------------------------------- | --- |
| **Cạnh tranh hoàn hảo**                                              | lúa mì — hàng ngàn nông dân, hàng triệu người tiêu dùng | 79  |
| **Độc quyền** — duy nhất một người bán, **người này quyết định giá** | công ty truyền hình cáp ở thị trấn của bạn              | 79  |
| Nằm **giữa hai thái cực**                                            | phần lớn thị trường thực tế                             | 79  |

Và sách nói thẳng vì sao vẫn giả định cạnh tranh hoàn hảo trong chương này: nó là *"một sự giản lược hữu ích và vì vậy là một điểm mấu chốt để bắt đầu"* — vì các thành viên **chấp nhận mức giá được cho trước**, đây là loại thị trường **dễ phân tích nhất** (tr. 79). Đúng tinh thần "vai trò của giả định" ở bài 1.

📌 Ba loại thị trường nằm giữa hai thái cực sẽ là **bài 6** (cạnh tranh), **bài 7** (độc quyền), **bài 8** (cạnh tranh độc quyền), **bài 9** (độc quyền nhóm).

---

## 3. Cầu — lượng cầu, quy luật cầu, biểu cầu, đường cầu

> **Lượng cầu** (*quantity demanded*): lượng hàng mà người mua sẵn lòng và có khả năng mua. — chú thích tr. 79

⚠️ **Hai chữ trong định nghĩa hay bị bỏ qua: "và có khả năng".** Muốn mua mà không có tiền thì **không** tính vào lượng cầu. Cầu trong kinh tế học là **mong muốn có khả năng chi trả**, không phải mong muốn suông.

> **Quy luật cầu** (*law of demand*): với các yếu tố khác không đổi, lượng cầu của một hàng hoá **giảm khi giá của nó tăng lên**. — chú thích tr. 79

Sách minh hoạ bằng chính bạn: nếu kem tăng lên 20 đô la một que, bạn sẽ mua ít hơn — *"có lẽ bạn sẽ mua sữa chua đông lạnh"*. Nếu giảm còn 0,2 đô la một que, bạn mua nhiều hơn (tr. 79).

### Biểu cầu của Catherine — Hình 1, tr. 80

> **Biểu cầu** (*demand schedule*): một bảng thể hiện mối quan hệ giữa giá bán và lượng cầu của một hàng hoá. — chú thích tr. 80
> **Đường cầu** (*demand curve*): đồ thị biểu diễn mối quan hệ giữa mức giá và lượng cầu của một hàng hoá. — chú thích tr. 80

| Giá kem | Lượng cầu của Catherine |
| ------: | ----------------------: |
|   $0,00 |                  12 cây |
|   $0,50 |                      10 |
|   $1,00 |                       8 |
|   $1,50 |                       6 |
|   $2,00 |                       4 |
|   $2,50 |                       2 |
|   $3,00 |                   **0** |

Hai điều rút ra:

1. Nếu kem **miễn phí**, Catherine vẫn chỉ mua **12 que mỗi tháng** — không phải vô hạn. Đây là biểu hiện của **lợi ích biên giảm dần** (bài 1, mục 4).
2. Ở mức **3 đô la**, Catherine **không mua nữa**. Đó là **giá sẵn lòng trả cao nhất** của cô — khái niệm sẽ thành nền của **thặng dư tiêu dùng** ở bài 4.

⚠️ **Quy ước trục — nhớ kỹ vì nó ngược với thói quen toán học.** Sách ghi rõ (tr. 80):

> *"Theo quy ước, giá bán nằm trên **trục tung** và lượng cầu nằm trên **trục hoành**."*

Trong toán, biến độc lập thường nằm trục hoành. Ở đây **giá** (thứ ta coi là nguyên nhân) lại nằm **trục tung**. Đây là quy ước lịch sử của kinh tế học, và bạn phải theo, vì mọi đồ thị trong sách, trong slide giảng và trong đề thi đều vẽ như vậy.

---

## 4. Cầu thị trường là tổng của cầu cá nhân — cộng theo chiều NGANG

Hình 2, tr. 81 — Catherine và Nicholas là hai người mua duy nhất trên thị trường:

| Giá mỗi que | Catherine |   +   | Nicholas |   =   | **Thị trường** |
| ----------: | --------: | :---: | -------: | :---: | -------------: |
|       $0,00 |        12 |   +   |        7 |   =   |     **19** que |
|       $0,50 |        10 |   +   |        6 |   =   |         **16** |
|       $1,00 |         8 |   +   |        5 |   =   |         **13** |
|       $1,50 |         6 |   +   |        4 |   =   |         **10** |
|   **$2,00** |     **4** |   +   |    **3** |   =   |          **7** |
|       $2,50 |         2 |   +   |        2 |   =   |          **4** |
|       $3,00 |         0 |   +   |        1 |   =   |          **1** |

⚠️ **Cộng theo chiều NGANG, không phải chiều dọc.** Sách nhấn mạnh riêng điểm này (tr. 81):

> *"Lưu ý rằng chúng ta cộng các đường cầu cá nhân **theo chiều ngang** để có được đường cầu thị trường. Tức là, để tìm tổng lượng cầu tại mỗi mức giá, chúng ta cộng các lượng cầu cá nhân trên trục hoành."*

Nói cách khác: **giữ nguyên giá, cộng lượng**. Cộng giá lại với nhau là vô nghĩa — không ai trả $0,00 + $0,00 = $0,00 cho hai que kem của hai người khác nhau.

### 💼 Góc QTKD — đây chính là cách bạn dựng dự báo doanh số

Cộng ngang là thao tác bạn làm thật khi lập kế hoạch bán hàng, chỉ là gọi tên khác:

```
   phân khúc A: ở giá 45k mua 1.200 ly/tháng
   phân khúc B: ở giá 45k mua   800 ly/tháng   ← GIỮ NGUYÊN GIÁ
   phân khúc C: ở giá 45k mua   500 ly/tháng
   ────────────────────────────────────────
   tổng cầu    ở giá 45k       2.500 ly/tháng   ← CỘNG LƯỢNG
```

Và hệ quả thực tế: **hai phân khúc có độ nhạy giá khác nhau thì đường cầu tổng sẽ gãy khúc**, không còn là đường thẳng. Đó là lý do một lần giảm giá có thể làm doanh số nhảy vọt bất ngờ — bạn vừa chạm ngưỡng chấp nhận của cả một phân khúc.

---

## 5. Năm yếu tố làm dịch chuyển đường cầu

Đường cầu thị trường **giữ mọi yếu tố khác không đổi**. Khi một trong các yếu tố đó đổi, **cả đường dịch chuyển** (Hình 3, tr. 82):

- dịch **sang phải** = **cầu tăng** (ở mọi mức giá đều muốn mua nhiều hơn)
- dịch **sang trái** = **cầu giảm**

**Bảng 1, tr. 83** liệt kê các biến ảnh hưởng đến người mua:

| Biến số                | Thay đổi biến này dẫn đến        |
| ---------------------- | -------------------------------- |
| **Giá của hàng hoá**   | **di chuyển dọc theo** đường cầu |
| Thu nhập               | **dịch chuyển** đường cầu        |
| Giá hàng hoá liên quan | **dịch chuyển** đường cầu        |
| Thị hiếu               | **dịch chuyển** đường cầu        |
| Kỳ vọng                | **dịch chuyển** đường cầu        |
| Số lượng người mua     | **dịch chuyển** đường cầu        |

### ① Thu nhập — hàng hoá thông thường và hàng hoá thứ cấp

> **Hàng hoá thông thường** (*normal good*): với các yếu tố khác không đổi, thu nhập tăng dẫn đến cầu tăng. — chú thích tr. 82
> **Hàng hoá thứ cấp** (*inferior good*): với các yếu tố khác không đổi, thu nhập tăng làm **giảm** cầu. — chú thích tr. 82

Ví dụ của sách cho hàng thứ cấp: **xe buýt**. *"Khi thu nhập của bạn giảm, bạn ít có khả năng mua xe hơi hoặc đi taxi và khả năng bạn phải đi xe buýt sẽ lớn hơn"* (tr. 82).

⚠️ **"Thứ cấp" không có nghĩa là "chất lượng kém".** Nó chỉ mô tả **chiều phản ứng với thu nhập**. Một món có thể là hàng thông thường với người này và thứ cấp với người kia.

### ② Giá của hàng hoá liên quan — thay thế và bổ sung

> **Hàng hoá thay thế** (*substitutes*): hai hàng hoá mà khi giá của hàng hoá này tăng sẽ làm **tăng** cầu của hàng hoá kia. — chú thích tr. 82
> **Hàng hoá bổ sung** (*complements*): hai hàng hoá mà khi giá hàng hoá này tăng thì cầu của hàng hoá kia **giảm**. — chú thích tr. 83

| Quan hệ      | Ví dụ của sách                                                                           | tr. |
| ------------ | ---------------------------------------------------------------------------------------- | --- |
| **Thay thế** | kem ↔ sữa chua; xúc xích ↔ bánh mì kẹp thịt; áo len ↔ áo nỉ; vé xem phim rạp ↔ đĩa DVD   | 82  |
| **Bổ sung**  | kem ↔ chocolate dạng lỏng; xăng ↔ ô tô; máy tính ↔ phần mềm; bơ đậu phộng ↔ sữa ong chúa | 83  |

Cách nhớ dứt điểm: **thay thế = dùng thay cho nhau; bổ sung = dùng cùng nhau.**

### ③ Thị hiếu

Sách thẳng thắn về giới hạn của kinh tế học ở đây (tr. 83): *"Các nhà kinh tế học thường không cố gắng giải thích thị hiếu của con người bởi thị hiếu được hình thành dựa trên các yếu tố lịch sử và tâm lý **nằm ngoài lĩnh vực kinh tế**. Tuy nhiên, điều mà các nhà kinh tế học thường làm là xem xét điều gì sẽ xảy ra khi thị hiếu thay đổi."*

### ④ Kỳ vọng

Kỳ vọng về **tương lai** ảnh hưởng cầu **hiện tại** (tr. 83): mong kiếm được nhiều hơn tháng tới → tiết kiệm ít hơn, chi nhiều hơn ngay bây giờ. Mong giá kem sẽ giảm vào ngày mai → mua ít kem hơn hôm nay.

### ⑤ Số lượng người mua

Nếu Peter tham gia cùng Catherine và Nicholas, lượng cầu thị trường cao hơn ở **mọi** mức giá (tr. 83).

### 💼 Góc QTKD — bảng chẩn đoán khi doanh số tụt

Khi doanh số giảm, câu hỏi đầu tiên phải là: **giá của ta có đổi không?** Vì hai nguyên nhân đó cần hai cách xử lý hoàn toàn khác nhau.

| Doanh số giảm vì                 | Bản chất                               | Việc phải làm                                       |
| -------------------------------- | -------------------------------------- | --------------------------------------------------- |
| ta vừa tăng giá                  | **di chuyển dọc** đường cầu            | tính lại: doanh thu tăng hay giảm? (bài 3)          |
| đối thủ giảm giá                 | dịch trái — giá **hàng thay thế** giảm | so sánh giá trị, không nhất thiết chạy đua giảm giá |
| kinh tế khó khăn, khách thắt chi | dịch trái — **thu nhập** giảm          | nếu hàng thông thường: ra dòng phổ thông            |
| xu hướng tiêu dùng đổi           | dịch trái — **thị hiếu**               | đổi sản phẩm, không phải đổi giá                    |
| khách chờ đợt sale cuối tháng    | dịch trái — **kỳ vọng**                | ⚠️ chính chính sách khuyến mãi của bạn tạo ra nó     |
| cửa hàng mới mở gần đó hút khách | **số người mua** ở khu vực bạn giảm    | mở rộng vùng phục vụ                                |

Dòng **kỳ vọng** đáng suy nghĩ nhất: khuyến mãi định kỳ **dạy khách hàng chờ**. Kỳ vọng giá sẽ giảm làm cầu hiện tại dịch trái — bạn tự tay bóp doanh số của chính những tuần không giảm giá.

---

## 6. ⚠️ Dịch chuyển ĐƯỜNG hay di chuyển DỌC theo đường — chỗ sai nhiều nhất

Sách nhắc lại quy tắc từ phụ lục chương 2 (tr. 83–84), và nhắc **hai lần** (một lần cho cầu tr. 83, một lần cho cung tr. 89) — dấu hiệu cho thấy đây là chỗ sinh viên hay sai:

> Một đường biểu diễn thay đổi khi có sự thay đổi của một trong những biến liên quan mà sự thay đổi này **không được đo ở hai trục**. Do **giá nằm trên trục tung**, một sự thay đổi của giá sẽ cho thấy một sự **di chuyển dọc theo** đường cầu. Ngược lại, thu nhập, giá cả hàng hoá liên quan, thị hiếu, kỳ vọng và số lượng người mua **không được đo lường trên hai trục**, do đó một sự thay đổi trong những biến này sẽ làm **đường cầu dịch chuyển**. (tr. 83–84)

Quy tắc rút gọn để dùng khi làm bài:

```
   Biến vừa thay đổi có nằm trên một trong hai TRỤC không?
      ├── CÓ  (giá, hoặc lượng)  →  DI CHUYỂN DỌC theo đường
      └── KHÔNG (mọi thứ khác)   →  CẢ ĐƯỜNG DỊCH CHUYỂN
```

Và **cặp thuật ngữ đi kèm** mà sách chốt lại ở tr. 93 — đề thi rất hay hỏi đúng chỗ này:

| Hiện tượng                        | Gọi là                           |
| --------------------------------- | -------------------------------- |
| **cả đường cầu** dịch chuyển      | "sự thay đổi của **cầu**"        |
| **di chuyển dọc** theo đường cầu  | "sự thay đổi của **lượng cầu**"  |
| **cả đường cung** dịch chuyển     | "sự thay đổi của **cung**"       |
| **di chuyển dọc** theo đường cung | "sự thay đổi của **lượng cung**" |

Nói gọn: **"cầu" là vị trí của cả đường; "lượng cầu" là một điểm trên đường đó.**

---

## 7. Nghiên cứu tình huống — hai cách giảm cầu thuốc lá

Đây là ví dụ hay nhất chương để phân biệt hai loại thay đổi, vì **hai chính sách khác nhau cho ra hai loại dịch chuyển khác nhau** (tr. 84).

**Cách 1 — làm dịch chuyển cả đường cầu** (Hình 4a): thông báo công cộng, cảnh báo sức khoẻ bắt buộc trên bao bì, cấm quảng cáo thuốc lá trên tivi. Những chính sách này cắt giảm lượng cầu **tại bất cứ mức giá nào** → đường cầu dịch **sang trái**, từ $D_1$ đến $D_2$.

> Ở mức giá **2 đô la một gói**, lượng cầu giảm từ **20 xuống còn 10 điếu mỗi ngày** (điểm A → điểm B).

**Cách 2 — làm di chuyển dọc theo đường cầu** (Hình 4b): đánh thuế sản xuất thuốc lá. Các công ty **chuyển hầu hết khoản thuế này sang người tiêu dùng** bằng cách bán giá cao hơn. Đường cầu **không đổi**; ta chỉ trượt tới một điểm khác trên nó.

> Giá tăng từ **2 đô la lên 4 đô la**, lượng cầu giảm từ **20 xuống còn 12 điếu mỗi ngày** (điểm A → điểm C).

### Con số cần nhớ (tr. 84–85)

> Giá tăng **10 phần trăm** làm giảm **4 phần trăm** lượng cầu.
> Với **thanh thiếu niên**: mỗi 10 phần trăm tăng giá làm giảm **12 phần trăm** số trẻ vị thành niên hút thuốc.

Thanh thiếu niên **nhạy cảm với giá gấp ba lần** người trưởng thành. Đây chính là **độ co giãn**, chủ đề của bài 3.

### Thuốc lá và cần sa — bổ sung, không phải thay thế

Một tranh luận mà sách thuật lại và kết bằng **dữ liệu**, không bằng suy luận (tr. 85):

| Lập luận                                              | Dự đoán                                           | Kết quả thực nghiệm                                             |
| ----------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------- |
| Thuốc lá và cần sa là **hàng thay thế**               | giá thuốc lá cao → dùng **nhiều** cần sa hơn      | ❌                                                               |
| Thuốc lá là **"cửa ngõ ma tuý"**, hai thứ **bổ sung** | giá thuốc lá **thấp** → dùng **nhiều** cần sa hơn | ✅ *"Các dữ liệu nghiên cứu cũng phù hợp với quan điểm thứ hai"* |

Kết luận nguyên văn của sách: *"Nói cách khác, thuốc lá và cần sa là những hàng hoá **bổ sung** chứ không phải là những hàng hoá thay thế nhau."*

📌 Đây là một **phát biểu thực chứng** được kiểm bằng dữ liệu (bài 1, mục 13). Chú ý sách **không** kết luận nên hay không nên đánh thuế — đó sẽ là phát biểu chuẩn tắc.

---

## 8. Cung — lượng cung, quy luật cung, biểu cung, đường cung

Mọi thứ đối xứng với phần cầu, chỉ đổi chiều.

> **Lượng cung** (*quantity supplied*): lượng hàng mà người bán có thể và sẵn lòng bán. — chú thích tr. 85
> **Quy luật cung** (*law of supply*): với các yếu tố khác không đổi, lượng cung của một hàng hoá **tăng khi giá của nó tăng lên**. — chú thích tr. 85

Cơ chế mà sách mô tả (tr. 85): giá kem cao → bán kem có lợi nhuận → người bán *"làm việc nhiều giờ, mua nhiều máy làm kem và thuê nhiều lao động"*. Giá thấp → ít lợi nhuận → sản xuất ít; ở mức giá đủ thấp, **một số người bán đóng cửa và lượng cung của họ giảm xuống bằng không**.

### Biểu cung của Ben — Hình 5, tr. 86

| Giá kem | Lượng cung của Ben |
| ------: | -----------------: |
|   $0,00 |                  0 |
|   $0,50 |                  0 |
|   $1,00 |                  1 |
|   $1,50 |                  2 |
|   $2,00 |                  3 |
|   $2,50 |                  4 |
|   $3,00 |                  5 |

⚠️ **Chú ý hai dòng đầu bằng 0.** Ở mức giá dưới 1 đô la, *"Ben sẽ không cung cấp kem nữa"* (tr. 85). Đường cung **không** bắt đầu từ gốc toạ độ — có một **ngưỡng giá tối thiểu** để người bán chịu bán. Ngưỡng này sẽ có tên chính thức ở bài 6: **quyết định đóng cửa**.

### Cung thị trường — Hình 6, tr. 87

Cộng **theo chiều ngang**, giống hệt bên cầu:

|   Giá kem |   Ben |   +   | Jerry |   =   | **Thị trường** |
| --------: | ----: | :---: | ----: | :---: | -------------: |
|     $0,00 |     0 |   +   |     0 |   =   |          **0** |
|     $0,50 |     0 |   +   |     0 |   =   |          **0** |
|     $1,00 |     1 |   +   |     0 |   =   |          **1** |
|     $1,50 |     2 |   +   |     2 |   =   |          **4** |
| **$2,00** | **3** |   +   | **4** |   =   |          **7** |
|     $2,50 |     4 |   +   |     6 |   =   |         **10** |
|     $3,00 |     5 |   +   |     8 |   =   |         **13** |

---

## 9. Bốn yếu tố làm dịch chuyển đường cung

**Bảng 2, tr. 88:**

| Biến số              | Thay đổi biến này sẽ làm          |
| -------------------- | --------------------------------- |
| **Giá của hàng hoá** | **di chuyển dọc** theo đường cung |
| Giá các đầu vào      | **dịch chuyển** đường cung        |
| Công nghệ            | **dịch chuyển** đường cung        |
| Kỳ vọng              | **dịch chuyển** đường cung        |
| Số lượng người bán   | **dịch chuyển** đường cung        |

**① Giá đầu vào** (tr. 88). Đầu vào của kem: *"kem, đường, hương liệu, máy kem, nhà xưởng sản xuất kem và lao động"*. Giá đầu vào tăng → lợi nhuận giảm → cung ít đi; nếu tăng đáng kể, *"doanh nghiệp có thể đóng cửa và không bán kem nữa"*. Quan hệ: **cung nghịch biến với giá đầu vào**.

**② Công nghệ** (tr. 88). *"Việc phát minh ra máy làm kem hiện đại hơn giúp giảm số lượng lao động cần thiết"* → giảm chi phí → **tăng cung**.

**③ Kỳ vọng** (tr. 88). Kỳ vọng giá sẽ tăng trong tương lai → *"cất một số sản phẩm hiện hành vào kho lưu trữ và cung cấp cho thị trường hiện tại ít kem hơn"*.

**④ Số lượng người bán** (tr. 88). Ben hay Jerry nghỉ kinh doanh → cung thị trường giảm.

⚠️ **Đính chính — sách in lỗi sắp chữ, tr. 88.**

Đoạn **"Tóm lại"** của phần Cung kết thúc bằng một câu bị **ghép nhầm và lặp**:

> *"Bảng 2 liệt kê các yếu tố ảnh hưởng đến việc nhà sản xuất chọn mức cung bao nhiêu **doanh nghiệp có thể đóng cửa và không bán kem nữa. Vì vậy, cung của một hàng hoá có quan hệ nghịch biến với giá các yếu tố đầu vào của nó**"*

Phần in đậm là **mảnh văn bản của đoạn "Giá đầu vào" phía trên bị lặp lại**, không thuộc câu này. Câu đúng phải dừng ở:

> *"Bảng 2 liệt kê các yếu tố ảnh hưởng đến việc nhà sản xuất chọn mức cung bao nhiêu."*

Đã đối chiếu bản quét 300 dpi. Không đổi nội dung kiến thức, nhưng đọc tới đó mà thấy rối thì **không phải do bạn**.

### 💼 Góc QTKD — bốn yếu tố này chính là bốn đòn bẩy chi phí của bạn

| Yếu tố       | Đòn bẩy trong doanh nghiệp                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| Giá đầu vào  | đàm phán nhà cung cấp, hợp đồng dài hạn, đa dạng nguồn cung                                            |
| Công nghệ    | tự động hoá — **dịch cả đường cung sang phải**, tức là ở **mọi** mức giá đều bán được nhiều hơn có lãi |
| Kỳ vọng      | chính sách tồn kho: giữ hàng chờ giá lên là một quyết định **cung**, không phải quyết định kho vận     |
| Số người bán | đối thủ mới gia nhập → đường cung ngành dịch phải → **giá thị trường giảm** (bài 6)                    |

Dòng **công nghệ** là dòng đáng đầu tư nhất: giảm giá bán chỉ **trượt dọc** đường cung, còn giảm chi phí **dịch cả đường** — nó cải thiện vị thế của bạn ở mọi mức giá cùng lúc.

---

## 10. Cân bằng — nơi hai đường gặp nhau

> **Điểm cân bằng** (*equilibrium*): tình huống mà ở đó giá thị trường làm cho lượng cung bằng lượng cầu. — chú thích tr. 89
> **Giá cân bằng** (*equilibrium price*): mức giá làm cân bằng lượng cung và lượng cầu. — chú thích tr. 89
> **Lượng cân bằng** (*equilibrium quantity*): lượng cung và lượng cầu tại mức giá cân bằng. — chú thích tr. 89

Với hai biểu số ở mục 4 và mục 8, giao điểm nằm ở **giá 2 đô la, lượng 7 que kem** (Hình 8, tr. 90).

Định nghĩa bằng lời của sách, đáng thuộc (tr. 89):

> *"Tại mức giá cân bằng, lượng hàng mà người mua sẵn lòng và có thể mua **chính xác bằng** lượng hàng mà người bán sẵn lòng và có thể bán."*

Và vì sao gọi là **giá thị trường**: *"ở mức giá này, tất cả mọi người trên thị trường đều hài lòng: Người mua được tất cả hàng hoá họ muốn mua, và người bán cũng bán hết hàng họ muốn bán"* (tr. 89).

⚠️ **"Hài lòng" ở đây là nghĩa kỹ thuật, không phải nghĩa cảm xúc.** Không ai *thích* mức giá đó; chỉ là ở mức đó, **không ai còn động cơ thay đổi hành vi**. Người mua vẫn muốn rẻ hơn, người bán vẫn muốn đắt hơn.

---

## 11. Thặng dư và thiếu hụt — cơ chế đưa thị trường về cân bằng

> **Thặng dư** (*surplus*): tình huống theo đó lượng cung lớn hơn lượng cầu. — chú thích tr. 90
> **Thiếu hụt** (*shortage*): tình huống mà trong đó lượng cầu cao hơn lượng cung. — chú thích tr. 90

**Hình 9(a) — giá quá cao ($2,50):**

```
   lượng cung 10  >  lượng cầu 4        →  THẶNG DƯ 6 que  (thừa cung)
   "người bán kem nhận thấy trong tủ lạnh của họ đầy kem"        (tr. 90)
   →  họ CẮT GIẢM GIÁ BÁN
   →  giá giảm ⟹ lượng cầu TĂNG và lượng cung GIẢM
   →  DI CHUYỂN DỌC theo cả hai đường, KHÔNG đường nào dịch chuyển
```

**Hình 9(b) — giá quá thấp ($1,50):**

```
   lượng cầu 10  >  lượng cung 4        →  THIẾU HỤT 6 que  (dư cầu)
   "người mua phải xếp hàng dài"                                 (tr. 90)
   →  người bán TĂNG GIÁ mà không bị mất doanh thu
   →  giá tăng ⟹ lượng cầu GIẢM và lượng cung TĂNG
```

Sách nhấn mạnh **hai lần** rằng đây là **di chuyển dọc, không phải dịch chuyển** (tr. 90) — quay lại đúng mục 6.

> **Quy luật cung và cầu** (*law of supply and demand*): giá của một hàng hoá sẽ điều chỉnh sao cho lượng cầu và lượng cung bằng nhau. — chú thích tr. 91

Và một nhận xét thực tế mà sách thêm vào (tr. 90): *"Việc thị trường đạt đến trạng thái cân bằng nhanh hay chậm tuỳ thuộc vào việc giá thay đổi nhanh hay chậm."*

### 💼 Góc QTKD — thặng dư và thiếu hụt trong kho của bạn

Hai tình trạng này có tên khác trong doanh nghiệp, và chúng là **tín hiệu định giá**, không phải chỉ là chuyện vận hành:

| Hiện tượng                                               | Kinh tế học gọi | Tín hiệu thật                             |
| -------------------------------------------------------- | --------------- | ----------------------------------------- |
| hàng tồn chất kho, phải xả lỗ cuối mùa                   | **thặng dư**    | giá đang **cao hơn** mức thị trường chịu  |
| hết hàng liên tục, khách phải đặt trước, chợ đen bán lại | **thiếu hụt**   | giá đang **thấp hơn** mức thị trường chịu |

⚠️ Vé xem ca nhạc "cháy trong 3 phút" rồi bán lại gấp 5 lần ngoài chợ đen **không phải** thành công marketing — đó là bằng chứng bạn **định giá thấp**, và toàn bộ phần chênh lệch đó rơi vào túi người bán lại chứ không phải bạn.

---

## 12. Ba bước phân tích sự thay đổi của trạng thái cân bằng

**Bảng 3, tr. 92** — quy trình dùng cho **mọi** bài tập cung cầu từ giờ tới hết môn:

```
   ① Xác định sự kiện làm dịch chuyển đường CUNG, đường CẦU, hay CẢ HAI
   ② Xác định các đường dịch chuyển sang TRÁI hay PHẢI
   ③ Dùng đồ thị cung cầu để so sánh cân bằng CŨ và cân bằng MỚI
```

### Ví dụ 1 — cầu dịch chuyển: mùa hè nóng bất thường (tr. 92)

| Bước | Lập luận                                                                                                                                           |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| ①    | Thời tiết nóng tác động vào **cầu** (thay đổi **sở thích**). **Cung không đổi** — *"thời tiết không ảnh hưởng trực tiếp đến doanh nghiệp bán kem"* |
| ②    | Muốn dùng nhiều kem hơn → cầu dịch **sang phải**, $D_1 \to D_2$                                                                                    |
| ③    | Ở giá cũ 2 đô la xuất hiện **thiếu hụt** → giá bị đẩy lên. Cân bằng mới: **giá 2 → 2,5 đô la**, **lượng 7 → 10 que**                               |

### Ví dụ 2 — cung dịch chuyển: bão phá vụ mía, giá đường tăng (tr. 93)

| Bước | Lập luận                                                                                                                                            |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| ①    | Giá đường là **giá đầu vào** → tác động **đường cung**. **Cầu không đổi** — *"chi phí đầu vào cao không trực tiếp ảnh hưởng đến sở thích dùng kem"* |
| ②    | Chi phí cao hơn → bán ít hơn ở mọi mức giá → cung dịch **sang trái**, $S_1 \to S_2$                                                                 |
| ③    | Ở giá cũ 2 đô la xuất hiện **thiếu hụt** → giá tăng. Cân bằng mới: **giá 2 → 2,5 đô la**, **lượng 7 → 4 que**                                       |

⚠️ **So sánh hai ví dụ này cạnh nhau — đây là ý quan trọng nhất mục 12.** Cả hai đều làm **giá tăng lên 2,5 đô la**. Nhưng lượng thì **ngược nhau**: nóng làm lượng **tăng lên 10**, bão làm lượng **giảm xuống 4**.

Nghĩa là: **nhìn giá tăng thôi thì không biết chuyện gì đã xảy ra.** Phải nhìn **lượng** mới phân biệt được cú sốc cầu với cú sốc cung. Đây là một trong những công cụ chẩn đoán hữu ích nhất mà chương này cho bạn.

### Ví dụ 3 — cả hai cùng dịch chuyển: nắng nóng và bão (tr. 94)

Cầu dịch **phải**, cung dịch **trái**. Cả hai đều đẩy **giá lên** → giá chắc chắn tăng. Nhưng lượng thì:

| Hình 12 | Tình huống                                 | Lượng cân bằng |
| ------- | ------------------------------------------ | -------------- |
| (a)     | cầu tăng **đáng kể**, cung giảm **một ít** | **tăng**       |
| (b)     | cung giảm **đáng kể**, cầu tăng **một ít** | **giảm**       |

Kết luận nguyên văn: *"những sự kiện này chắc chắn làm giá kem tăng lên, nhưng tác động của số lượng kem bán ra là **không rõ ràng**"* (tr. 94).

---

## 13. Bảng 4 — chín ô, và vì sao hai ô ghi "không rõ"

**Bảng 4, tr. 95:**

|                   | **Cung không đổi**         | **Cung tăng**                | **Cung giảm**                |
| ----------------- | -------------------------- | ---------------------------- | ---------------------------- |
| **Cầu không đổi** | P không đổi<br>Q không đổi | P **giảm**<br>Q **tăng**     | P **tăng**<br>Q **giảm**     |
| **Cầu tăng**      | P **tăng**<br>Q **tăng**   | P **không rõ**<br>Q **tăng** | P **tăng**<br>Q **không rõ** |
| **Cầu giảm**      | P **giảm**<br>Q **giảm**   | P **giảm**<br>Q **không rõ** | P **không rõ**<br>Q **giảm** |

📚 **Đừng học thuộc bảng này.** Nó có quy luật, và quy luật ấy chỉ có một dòng:

> Khi hai đường dịch chuyển, đại lượng nào **được cả hai cú dịch chuyển đẩy về cùng một hướng** thì **kết luận chắc chắn**; đại lượng nào **bị đẩy về hai hướng ngược nhau** thì **không rõ**, vì kết quả phụ thuộc **biên độ** của hai cú dịch chuyển.

Kiểm chứng bằng ô "cầu tăng + cung tăng":

```
   cầu tăng  →  P đẩy LÊN,   Q đẩy TĂNG
   cung tăng →  P đẩy XUỐNG, Q đẩy TĂNG
   ───────────────────────────────────────
   Q: cả hai cùng đẩy TĂNG      →  Q TĂNG  (chắc chắn)
   P: một đẩy lên, một đẩy xuống →  KHÔNG RÕ
```

Mục 15 để máy tự sinh lại toàn bộ Bảng 4 từ hai phương trình đường thẳng — bạn sẽ thấy hai ô "không rõ" **xuất hiện tự động**, không phải do ai quy ước.

---

## 14. 📚 Giá cả phân bổ nguồn lực — và tranh cãi về "giá cắt cổ"

Phần kết chương (tr. 95–97) trả lời câu hỏi lớn của bài 1: **bàn tay vô hình vận hành bằng cách nào?**

Ví dụ **đất ven biển** (tr. 95–97): diện tích có hạn, không phải ai cũng được hưởng. Ai sẽ được?

> *"Câu trả lời là bất cứ ai sẵn sàng và có khả năng chi trả. Giá đất bên bờ biển được điều chỉnh cho đến khi lượng cầu về đất đúng bằng lượng cung."*

Ví dụ **ai làm nông** (tr. 97): trong một xã hội tự do *"không có cơ quan lập kế hoạch của chính phủ để quyết định điều này"*. Việc phân bổ dựa trên quyết định của hàng triệu người lao động, và nó chạy được vì các quyết định ấy **phụ thuộc vào giá cả** — giá thực phẩm và tiền lương nông trại tự điều chỉnh để bảo đảm đủ người làm nông.

Ẩn dụ khép lại chương (tr. 97):

> *"Nếu một bàn tay vô hình dẫn dắt nền kinh tế thị trường, như tuyên bố nổi tiếng của Adam Smith, thì **hệ thống giá cả là chiếc đũa** mà bàn tay vô hình sử dụng để điều khiển các dàn nhạc kinh tế."*

### Theo dòng thời sự — "Điều gì sai với giá cắt cổ" (tr. 96)

Bài báo của **Jeff Jacoby**, bối cảnh: **năm 2010**, đường ống nước chính ở Great Boston vỡ, nhiều thị trấn không có nước máy sạch → cầu nước đóng chai tăng vọt.

| Bên                               | Hành động                                                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Tổng chưởng lý **Martha Coakley** | cảnh báo doanh nghiệp không được "chặt chém"; phái thanh tra kiểm tra theo từng điểm; lập đường dây nóng nhận tố giác "những kẻ bán giá cắt cổ" |
| Thống đốc **Deval Patrick**       | ra lệnh "giám sát chặt chẽ giá nước đóng chai"                                                                                                  |
| Tác giả bài báo                   | **phản đối** kiểm soát giá                                                                                                                      |

Phép thử giả định mà tác giả dựng lên — đáng đọc kỹ vì nó là toàn bộ chương 4 gói trong một đoạn:

|             | Người bán A                                                                          | Người bán B                                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| Phản ứng    | giữ giá **69 xu** một chai                                                           | tăng hơn **4 lần**, lên **2,99 đô la**                                                                                      |
| Điều xảy ra | *"Trong vòng vài giờ toàn bộ hàng đã được bán sạch"*, khách tới sau **về tay không** | bán chậm hơn, **nhiều lời phàn nàn**                                                                                        |
| Nhưng       |                                                                                      | *"ngay cả khách hàng đến trễ cũng có thể mua được lượng nước họ cần, và gần như không ai mua nhiều hơn mức họ thực sự cần"* |

Hai chức năng của việc giá tăng, theo lập luận của bài báo:

1. **Phân phối** — giữ các nguồn lực khan hiếm không biến mất trong vài giờ đầu (**hạn chế tích trữ**).
2. **Thu hút nguồn cung mới** — *"làm gia tăng trong các nguồn cung bất thường vào ngày mai"*. Bài báo dẫn thực tế: các nhà cung cấp **làm thêm giờ**, nhà máy nước giải khát Polar ở Worcester *"đã vét sạch nhà máy ở thành phố này trong đêm qua và phải chuyển thêm nước từ cơ sở của mình ở New York"*.

Và câu chốt: kiểm soát giá cũng là một lựa chọn — *"giả sử bạn không phản đối những điều hiển nhiên như tham nhũng, xếp hàng dài, và thị trường chợ đen"*.

⚠️ **Cân bằng lại — đây là một bài xã luận, không phải kết luận của sách.** Sách đặt nó trong hộp "Theo dòng thời sự" và mở đầu bằng câu *"ý kiến sau đây tán thành với phản ứng tự nhiên của thị trường"* — tức là **một quan điểm**, có phần **chuẩn tắc**. Lập luận về hiệu quả là vững; nhưng câu hỏi *"có công bằng không khi người nghèo không mua nổi nước sau thảm hoạ"* thuộc về **bình đẳng**, và bài báo không trả lời nó. Đúng cặp đánh đổi hiệu quả ↔ bình đẳng ở bài 1. Chính sách giá trần sẽ được phân tích đầy đủ ở **bài 13** (chương 6, tr. 127).

### 💼 Góc QTKD — bài học định giá lúc khủng hoảng

Ba điều rút ra được, không cần đồng ý với bài báo:

1. **Hết hàng trong vài giờ là dấu hiệu định giá thấp**, không phải dấu hiệu thành công.
2. Nếu vì lý do thương hiệu bạn **không** muốn tăng giá lúc khan hiếm, hãy dùng **công cụ phi giá** để thay thế chức năng phân phối: giới hạn số lượng mỗi khách, ưu tiên khách thành viên, đặt trước. Nếu không, hàng sẽ về tay người mua gom bán lại.
3. **Rủi ro danh tiếng là có thật và có thể lớn hơn phần lãi thêm.** Kinh tế học nói cái gì *hiệu quả*; nó không nói khách hàng sẽ nghĩ gì về bạn năm sau.
---

## 15. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-02-cung-va-cau.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-02-cung-va-cau.py](../thuc_hanh/bai-02-cung-va-cau.py).

Điểm mấu chốt của đoạn code này: **hai biểu số của sách khớp đúng hai đường thẳng.**

$$Q_d = 19 - 3k \qquad Q_s = 3k - 5 \qquad \text{với } k = \frac{P}{0{,}50}$$

Dùng $k$ = **số nửa đô la** thay cho $P$ khiến mọi phép tính thành số nguyên (đúng quy tắc *tiền
không dùng số thực*). Nhờ có công thức, ta giải cân bằng **chính xác bằng phân số** thay vì đọc mò
trên đồ thị — và quan trọng hơn: **sinh lại được toàn bộ Bảng 4** thay vì học thuộc nó.

```python
"""Bai 2 — Cac luc luong cung va cau tren thi truong (Mankiw, chuong 4).
Chay: python3 bai-02-cung-va-cau.py   (Python 3.10+, khong can cai goi nao)

Gia tinh bang SO NUA DO LA (k) de moi phep tinh deu la so nguyen:
    P = k / 2 do la.  k = 4  <=>  P = 2,00 do la.
Cac ham cung/cau duoi day khop DUNG tung o cua Hinh 2 va Hinh 6 trong sach.
"""

from fractions import Fraction

# ══ 1. BIEU CAU CUA CATHERINE — Hinh 1, tr. 80 ══════════════════════════════
cau_catherine = {0: 12, 1: 10, 2: 8, 3: 6, 4: 4, 5: 2, 6: 0}   # khoa la k
cau_nicholas  = {0: 7,  1: 6,  2: 5, 3: 4, 4: 3, 5: 2, 6: 1}   # Hinh 2, tr. 81
cung_ben      = {0: 0,  1: 0,  2: 1, 3: 2, 4: 3, 5: 4, 6: 5}   # Hinh 5, tr. 86
cung_jerry    = {0: 0,  1: 0,  2: 0, 3: 2, 4: 4, 5: 6, 6: 8}   # Hinh 6, tr. 87

def do_la(k):
    return f"${float(k) / 2:.2f}"

print("1. BIEU CAU CA NHAN VA BIEU CAU THI TRUONG — Hinh 1 va Hinh 2 (tr. 80–81)")
print("   gia      Catherine  +  Nicholas  =  thi truong")
cau_tt = {}
for k in sorted(cau_catherine):
    cau_tt[k] = cau_catherine[k] + cau_nicholas[k]
    print(f"   {do_la(k):>6}   {cau_catherine[k]:>7}     {cau_nicholas[k]:>7}      {cau_tt[k]:>7}")
print("   ⚠ Cong theo CHIEU NGANG: cong LUONG tai cung mot muc GIA, khong cong gia.")
print()

print("2. BIEU CUNG CA NHAN VA BIEU CUNG THI TRUONG — Hinh 5 va Hinh 6 (tr. 86–87)")
print("   gia         Ben     +    Jerry   =  thi truong")
cung_tt = {}
for k in sorted(cung_ben):
    cung_tt[k] = cung_ben[k] + cung_jerry[k]
    print(f"   {do_la(k):>6}   {cung_ben[k]:>7}     {cung_jerry[k]:>7}      {cung_tt[k]:>7}")
print()

# ══ 2. HAI BIEU TREN LA HAI DUONG THANG — kiem lai ══════════════════════════
# Cau thi truong:  Qd = 19 - 3k      Cung thi truong: Qs = 3k - 5 (chan duoi o 0)
def Qd(k, dich_cau=0):    return 19 - 3 * k + dich_cau
def Qs(k, dich_cung=0):   return max(0, 3 * k - 5 + dich_cung)

print("3. HAI BIEU SO CUA SACH CHINH LA HAI DUONG THANG")
khop_cau  = all(Qd(k) == cau_tt[k] for k in cau_tt)
khop_cung = all(Qs(k) == cung_tt[k] for k in cung_tt)
print(f"   Qd = 19 - 3k  khop tung o cua Hinh 2:  {khop_cau}")
print(f"   Qs = 3k - 5   khop tung o cua Hinh 6:  {khop_cung}   (k = so nua do la)")
print("   => tu day tinh duoc can bang CHINH XAC bang phan so, khong phai doc do thi.")
print()

# ══ 3. CAN BANG — Hinh 8, tr. 90 ════════════════════════════════════════════
def can_bang(dich_cau=0, dich_cung=0):
    """Giai 19 - 3k + dc = 3k - 5 + ds  ->  k = (24 + dc - ds) / 6."""
    k = Fraction(24 + dich_cau - dich_cung, 6)
    return k, Fraction(19) - 3 * k + dich_cau

k0, q0 = can_bang()
print("4. CAN BANG THI TRUONG — Hinh 8, tr. 90")
print(f"   19 - 3k = 3k - 5  ->  6k = 24  ->  k = {k0}  ->  P = {do_la(float(k0))}, Q = {q0} que kem")
print(f"   (sach: gia can bang 2 do la, luong can bang 7 que — tr. 89)")
print()

print("5. THUA CUNG VA DU CAU — Hinh 9, tr. 91")
for k, nhan in [(5, "CAO hon can bang"), (3, "THAP hon can bang")]:
    d, s = Qd(k), Qs(k)
    if s > d:
        print(f"   P = {do_la(k)} ({nhan}): cung {s} > cau {d}  ->  THANG DU {s - d} que  ->  nguoi ban HA GIA")
    else:
        print(f"   P = {do_la(k)} ({nhan}): cau {d} > cung {s}  ->  THIEU HUT {d - s} que  ->  nguoi ban TANG GIA")
print("   (sach: o 2,5 do la thang du 10 - 4; o 1,5 do la thieu hut 10 - 4 — tr. 90)")
print()

# ══ 4. VE HAI DUONG TREN CUNG MOT DO THI ════════════════════════════════════
def ve(cac_duong, tieu_de, k_max=7, q_max=20, cao=15, rong=42):
    """cac_duong: danh sach (ham_theo_k, ky_tu, nhan)."""
    luoi = [[" "] * rong for _ in range(cao)]
    for ham, ky, _ in cac_duong:
        for i in range(rong * 4):
            k = k_max * i / (rong * 4 - 1)
            q = ham(k)
            if not (0 <= q <= q_max):
                continue
            c = round(q / q_max * (rong - 1))
            r = cao - 1 - round(k / k_max * (cao - 1))
            if luoi[r][c] == " ":
                luoi[r][c] = ky
    print(f"      {tieu_de}")
    print("      gia")
    for i, hang in enumerate(luoi):
        k = k_max - i * k_max / (cao - 1)
        nhan = f"{k / 2:>5.2f}" if abs(k - round(k)) < 1e-9 and round(k) % 2 == 0 else "     "
        print(f"      {nhan} │{''.join(hang)}".rstrip())
    print("            └" + "─" * rong)
    print("             0" + " " * (rong - 6) + f"{q_max:>4}  luong")
    for _, ky, nhan in cac_duong:
        print(f"      {ky} = {nhan}")

print("6. DO THI CUNG — CAU")
ve([(lambda k: Qd(k), "d", "cau  Qd = 19 - 3k"),
    (lambda k: Qs(k), "s", "cung Qs = 3k - 5")], "can bang tai P = $2.00, Q = 7")
print()

# ══ 5. BA BUOC PHAN TICH — Bang 3, tr. 92 ══════════════════════════════════
print("7. BA BUOC PHAN TICH SU THAY DOI CAN BANG — Bang 3, tr. 92")
tinh_huong = [
    ("Mua he nong bat thuong (tr. 92)",          +6,  0, "cau dich PHAI, cung khong doi"),
    ("Bao pha mia, gia duong tang (tr. 93)",      0, -6, "cung dich TRAI, cau khong doi"),
    ("Ca hai cung xay ra (tr. 94)",              +6, -6, "cau PHAI va cung TRAI"),
]
for ten, dc, ds, mo_ta in tinh_huong:
    k1, q1 = can_bang(dc, ds)
    print(f"   {ten}")
    print(f"      buoc 1-2: {mo_ta}")
    print(f"      buoc 3  : P {do_la(float(k0))} -> {do_la(float(k1))}   |   Q {q0} -> {q1}")
print("   (sach: nong -> 2 do la len 2,5 va 7 len 10 que — tr. 92)")
print("   (sach: bao  -> 2 do la len 2,5 va 7 xuong 4 que — tr. 94)")
print("   ⚠ Truong hop 3: gia tang MANH hon, con luong quay ve dung 7 — hai dich chuyen")
print("      trai dau nhau vua khit. Do chinh la o 'Q khong ro' cua Bang 4.")
print()

# ══ 6. SINH LAI BANG 4 THAY VI HOC THUOC — tr. 95 ═══════════════════════════
print("8. BANG 4 (tr. 95) — SINH LAI BANG MAY, KHONG HOC THUOC")

def huong(cu, moi):
    return "tang" if moi > cu else ("giam" if moi < cu else "khong doi")

def o_bang(dau_cau, dau_cung):
    """Thu NHIEU bien do dich chuyen. Neu ket qua khong thong nhat -> 'khong ro'."""
    P, Q = set(), set()
    for bien_do_cau in (2, 6, 10):
        for bien_do_cung in (2, 6, 10):
            dc = dau_cau * bien_do_cau
            ds = dau_cung * bien_do_cung
            k1, q1 = can_bang(dc, ds)
            P.add(huong(k0, k1)); Q.add(huong(q0, q1))
            if dau_cau == 0 and dau_cung == 0:
                break
        if dau_cau == 0 and dau_cung == 0:
            break
    return ("khong ro" if len(P) > 1 else P.pop()), ("khong ro" if len(Q) > 1 else Q.pop())

nhan_cung = {0: "Cung khong doi", 1: "Cung tang", -1: "Cung giam"}
nhan_cau  = {0: "Cau khong doi",  1: "Cau tang",  -1: "Cau giam"}
print((f"   {'':<16}" + "".join(f"{nhan_cung[s]:<18}" for s in (0, 1, -1))).rstrip())
for dcau in (0, 1, -1):
    dong_p, dong_q = f"   {nhan_cau[dcau]:<16}", f"   {'':<16}"
    for dcung in (0, 1, -1):
        p, q = o_bang(dcau, dcung)
        dong_p += f"P {p:<16}"
        dong_q += f"Q {q:<16}"
    print(dong_p.rstrip()); print(dong_q.rstrip()); print()
print("   ⚠ Hai o 'khong ro' KHONG phai vi ta thieu thong tin ve quy luat,")
print("      ma vi ket qua that su PHU THUOC BIEN DO dich chuyen. Kiem chung:")
for dc, ds, ghi in [(10, 2, "cau tang MANH, cung tang nhe"), (2, 10, "cau tang nhe, cung tang MANH")]:
    k1, q1 = can_bang(dc, ds)
    print(f"      {ghi:<32} P {huong(k0, k1):<9} Q {huong(q0, q1)}")
print()

# ══ 7. 💼 GOC QTKD — bang gia va doanh thu ══════════════════════════════════
print("9. 💼 GOC QTKD — QUAN CA PHE: GIA NAO CHO DOANH THU CAO NHAT?")
# Duong cau uoc luong tu du lieu ban hang: moi tang 5 nghin dong thi mat 30 ly/ngay
GIA_GOC, LUONG_GOC, DOC = 35, 300, 6      # nghin dong, ly/ngay, ly mat moi nghin dong tang
def luong_ban(gia):
    return max(0, LUONG_GOC - DOC * (gia - GIA_GOC))

print("   duong cau uoc luong: cu tang 1 nghin dong thi ban hut 6 ly/ngay")
print("     gia    luong ban   doanh thu/ngay   thay doi doanh thu")
truoc = None
for gia in range(25, 76, 5):
    q = luong_ban(gia)
    dt = gia * q
    chenh = "" if truoc is None else f"{dt - truoc:+8,}"
    print(f"   {gia:>4}k   {q:>7} ly   {dt:>10,}k   {chenh:>10}")
    truoc = dt
dinh = [g for g in range(25, 76) if g * luong_ban(g) == max(x * luong_ban(x) for x in range(25, 76))]
print(f"   => doanh thu cao nhat tai gia {dinh[0]}k va {dinh[-1]}k: "
      f"{dinh[0] * luong_ban(dinh[0]):,}k/ngay  (dinh ly thuyet 42,5k)")
print("   ⚠ Day moi la DOANH THU. Muon toi da LOI NHUAN phai tru chi phi — bai 5, 6.")
print("   ⚠ Vi sao doanh thu tang roi lai giam? Vi DO CO GIAN doi dau o dung diem giua.")
print("      Do la toan bo noi dung bai 3 (chuong 5, tr. 103).")
```

**Kết quả chạy thật:**

```
1. BIEU CAU CA NHAN VA BIEU CAU THI TRUONG — Hinh 1 va Hinh 2 (tr. 80–81)
   gia      Catherine  +  Nicholas  =  thi truong
    $0.00        12           7           19
    $0.50        10           6           16
    $1.00         8           5           13
    $1.50         6           4           10
    $2.00         4           3            7
    $2.50         2           2            4
    $3.00         0           1            1
   ⚠ Cong theo CHIEU NGANG: cong LUONG tai cung mot muc GIA, khong cong gia.

2. BIEU CUNG CA NHAN VA BIEU CUNG THI TRUONG — Hinh 5 va Hinh 6 (tr. 86–87)
   gia         Ben     +    Jerry   =  thi truong
    $0.00         0           0            0
    $0.50         0           0            0
    $1.00         1           0            1
    $1.50         2           2            4
    $2.00         3           4            7
    $2.50         4           6           10
    $3.00         5           8           13

3. HAI BIEU SO CUA SACH CHINH LA HAI DUONG THANG
   Qd = 19 - 3k  khop tung o cua Hinh 2:  True
   Qs = 3k - 5   khop tung o cua Hinh 6:  True   (k = so nua do la)
   => tu day tinh duoc can bang CHINH XAC bang phan so, khong phai doc do thi.

4. CAN BANG THI TRUONG — Hinh 8, tr. 90
   19 - 3k = 3k - 5  ->  6k = 24  ->  k = 4  ->  P = $2.00, Q = 7 que kem
   (sach: gia can bang 2 do la, luong can bang 7 que — tr. 89)

5. THUA CUNG VA DU CAU — Hinh 9, tr. 91
   P = $2.50 (CAO hon can bang): cung 10 > cau 4  ->  THANG DU 6 que  ->  nguoi ban HA GIA
   P = $1.50 (THAP hon can bang): cau 10 > cung 4  ->  THIEU HUT 6 que  ->  nguoi ban TANG GIA
   (sach: o 2,5 do la thang du 10 - 4; o 1,5 do la thieu hut 10 - 4 — tr. 90)

6. DO THI CUNG — CAU
      can bang tai P = $2.00, Q = 7
      gia
            │                                ss
            │d                           ssss
       3.00 │ ddd                     ssss
            │    ddd               ssss
            │       dddd        ssss
            │          dddd  ssss
       2.00 │             dddd
            │          ssss  dddd
            │       ssss        dddd
            │    ssss              dddd
       1.00 │ sss                     dddd
            │s                           dddd
            │s                              dddd
            │s                                  ddd
       0.00 │s                                     dd
            └──────────────────────────────────────────
             0                                      20  luong
      d = cau  Qd = 19 - 3k
      s = cung Qs = 3k - 5

7. BA BUOC PHAN TICH SU THAY DOI CAN BANG — Bang 3, tr. 92
   Mua he nong bat thuong (tr. 92)
      buoc 1-2: cau dich PHAI, cung khong doi
      buoc 3  : P $2.00 -> $2.50   |   Q 7 -> 10
   Bao pha mia, gia duong tang (tr. 93)
      buoc 1-2: cung dich TRAI, cau khong doi
      buoc 3  : P $2.00 -> $2.50   |   Q 7 -> 4
   Ca hai cung xay ra (tr. 94)
      buoc 1-2: cau PHAI va cung TRAI
      buoc 3  : P $2.00 -> $3.00   |   Q 7 -> 7
   (sach: nong -> 2 do la len 2,5 va 7 len 10 que — tr. 92)
   (sach: bao  -> 2 do la len 2,5 va 7 xuong 4 que — tr. 94)
   ⚠ Truong hop 3: gia tang MANH hon, con luong quay ve dung 7 — hai dich chuyen
      trai dau nhau vua khit. Do chinh la o 'Q khong ro' cua Bang 4.

8. BANG 4 (tr. 95) — SINH LAI BANG MAY, KHONG HOC THUOC
                   Cung khong doi    Cung tang         Cung giam
   Cau khong doi   P khong doi       P giam            P tang
                   Q khong doi       Q tang            Q giam

   Cau tang        P tang            P khong ro        P tang
                   Q tang            Q tang            Q khong ro

   Cau giam        P giam            P giam            P khong ro
                   Q giam            Q khong ro        Q giam

   ⚠ Hai o 'khong ro' KHONG phai vi ta thieu thong tin ve quy luat,
      ma vi ket qua that su PHU THUOC BIEN DO dich chuyen. Kiem chung:
      cau tang MANH, cung tang nhe     P tang      Q tang
      cau tang nhe, cung tang MANH     P giam      Q tang

9. 💼 GOC QTKD — QUAN CA PHE: GIA NAO CHO DOANH THU CAO NHAT?
   duong cau uoc luong: cu tang 1 nghin dong thi ban hut 6 ly/ngay
     gia    luong ban   doanh thu/ngay   thay doi doanh thu
     25k       360 ly        9,000k             
     30k       330 ly        9,900k         +900
     35k       300 ly       10,500k         +600
     40k       270 ly       10,800k         +300
     45k       240 ly       10,800k           +0
     50k       210 ly       10,500k         -300
     55k       180 ly        9,900k         -600
     60k       150 ly        9,000k         -900
     65k       120 ly        7,800k       -1,200
     70k        90 ly        6,300k       -1,500
     75k        60 ly        4,500k       -1,800
   => doanh thu cao nhat tai gia 42k va 43k: 10,836k/ngay  (dinh ly thuyet 42,5k)
   ⚠ Day moi la DOANH THU. Muon toi da LOI NHUAN phai tru chi phi — bai 5, 6.
   ⚠ Vi sao doanh thu tang roi lai giam? Vi DO CO GIAN doi dau o dung diem giua.
      Do la toan bo noi dung bai 3 (chuong 5, tr. 103).
```

### Đọc kết quả

**① Cộng ngang (mục 1–2).** Hai bảng đầu tái tạo Hình 2 và Hình 6. Chú ý cột thị trường: cầu
19 → 1, cung 0 → 13. Chúng cắt nhau đúng ở dòng $2,00 với **7 = 7**.

**② Hai biểu số là hai đường thẳng (mục 3).** Cả hai dòng in `True`. Đây không phải trùng hợp —
Mankiw chọn số để đường cung và đường cầu **đều tuyến tính và cắt nhau tại điểm tròn**. Biết vậy thì
bạn giải được bằng đại số thay vì đếm ô.

**③ Cân bằng (mục 4).** $19 - 3k = 3k - 5 \Rightarrow k = 4 \Rightarrow P = \$2{,}00,\ Q = 7$ —
khớp tr. 89.

**④ Thặng dư và thiếu hụt (mục 5).** Ở \$2,50: cung 10 > cầu 4, thặng dư **6**. Ở \$1,50: cầu 10 >
cung 4, thiếu hụt **6**. Đối xứng, vì hai đường có cùng độ dốc 3.

**⑤ Ba bước (mục 7).** Cú sốc cầu $+6$ và cú sốc cung $-6$ tái tạo **đúng** con số của sách: nóng →
(\$2,50; 10), bão → (\$2,50; 4). Trường hợp thứ ba là phần đáng chú ý nhất: cả hai cùng xảy ra →
giá lên **\$3,00** nhưng lượng **quay về đúng 7**. Hai cú dịch chuyển triệt tiêu nhau vừa khít trên
trục lượng — đó chính là ô "Q không rõ" của Bảng 4, nhìn thấy bằng con số cụ thể.

**⑥ Bảng 4 tự sinh (mục 8).** Hàm `o_bang()` thử **chín biên độ khác nhau** cho mỗi ô. Nếu chín lần
đều ra cùng một hướng → ghi hướng đó; nếu không thống nhất → ghi `khong ro`. Kết quả trùng khớp
từng ô với Bảng 4 tr. 95 — nhưng lần này bạn **thấy vì sao**, không phải nhớ suông. Hai dòng kiểm
chứng cuối cho thấy cùng một ô "cầu tăng + cung tăng" cho **P tăng** hay **P giảm** tuỳ biên độ.

**⑦ Góc QTKD (mục 9).** Bảng doanh thu tăng dần rồi **giảm dần**, đỉnh ở khoảng 42–43 nghìn. Cột
"thay đổi doanh thu" giảm đều $+900 \to +600 \to +300 \to 0 \to -300$: **doanh thu biên** giảm
tuyến tính và **đổi dấu** đúng ở đỉnh. Vì sao có đỉnh, và làm sao biết nó ở đâu mà không cần dò cả
bảng — đó là **bài 3**.

---

## 16. Tự thử

Sửa tham số rồi chạy lại. Không có lời giải kèm theo.

1. Trong hàm `Qs`, đổi `3 * k - 5` thành `6 * k - 5` (đường cung **dốc hơn** — người bán phản ứng
   mạnh hơn với giá). Cân bằng mới ở đâu? Khi cầu tăng $+6$, giá tăng **nhiều hơn hay ít hơn** so
   với trước? Rút ra: độ dốc đường cung quyết định điều gì?
2. Đổi `Qd` thành `19 - 12 * k` (đường cầu **rất dốc**, khách gần như không đổi hành vi theo giá).
   Bây giờ một cú sốc cung $-6$ đẩy giá lên bao nhiêu? Liên hệ với giá xăng và giá thuốc chữa bệnh.
3. Trong `tinh_huong`, thêm dòng `("Doi thu moi gia nhap", 0, +6, "cung dich PHAI")`. Giá và lượng
   đi về đâu? Đây là kết cục mà **bài 6** sẽ chứng minh là tất yếu trong thị trường cạnh tranh.
4. Trong `o_bang`, đổi `for bien_do_cau in (2, 6, 10)` thành `(6,)` và `bien_do_cung` thành `(6,)`
   — tức chỉ thử **một** biên độ. Bảng 4 còn ô `khong ro` nào không? Điều đó nói gì về việc *"thử một
   trường hợp rồi kết luận"*?
5. Trong mục 9, đổi `DOC = 6` thành `DOC = 2` (khách **ít nhạy giá** hơn nhiều). Giá tối đa hoá doanh
   thu dịch về đâu? Doanh thu đỉnh là bao nhiêu? Loại quán nào trong thực tế có `DOC` nhỏ?

---

## 17. Từ điển thuật ngữ

Cột tiếng Anh lấy từ mục **Khái niệm then chốt** của sách (tr. 98–99).

| Tiếng Việt            | Tiếng Anh                | Ghi chú                                                      |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| Thị trường            | Market                   | tr. 77 — một **quan hệ**, không phải một địa điểm            |
| Thị trường cạnh tranh | Competitive market       | tr. 78 — nhiều người mua và bán, không ai ảnh hưởng được giá |
| Người chấp nhận giá   | Price taker              | tr. 78                                                       |
| Lượng cầu             | Quantity demanded        | tr. 79 — sẵn lòng **và có khả năng** mua                     |
| Quy luật cầu          | Law of demand            | tr. 79                                                       |
| Biểu cầu              | Demand schedule          | tr. 80 — cái **bảng**                                        |
| Đường cầu             | Demand curve             | tr. 80 — cái **đồ thị**                                      |
| Hàng hoá thông thường | Normal good              | tr. 82 — thu nhập tăng ⟹ cầu tăng                            |
| Hàng hoá thứ cấp      | Inferior good            | tr. 82 — thu nhập tăng ⟹ cầu **giảm**                        |
| Hàng hoá thay thế     | Substitutes              | tr. 82 — dùng **thay cho** nhau                              |
| Hàng hoá bổ sung      | Complements              | tr. 83 — dùng **cùng** nhau                                  |
| Lượng cung            | Quantity supplied        | tr. 85                                                       |
| Quy luật cung         | Law of supply            | tr. 85                                                       |
| Biểu cung             | Supply schedule          | tr. 86                                                       |
| Đường cung            | Supply curve             | tr. 86                                                       |
| Trạng thái cân bằng   | Equilibrium              | tr. 89                                                       |
| Giá cân bằng          | Equilibrium price        | tr. 89                                                       |
| Lượng cân bằng        | Equilibrium quantity     | tr. 89                                                       |
| Thặng dư              | Surplus                  | tr. 90 — cung > cầu, giá **quá cao**                         |
| Thiếu hụt             | Shortage                 | tr. 90 — cầu > cung, giá **quá thấp**                        |
| Quy luật cung và cầu  | Law of supply and demand | tr. 91                                                       |

⚠️ **Đính chính — tr. 98.** Trong bảng *Khái niệm then chốt*, dòng "Lượng cầu" được dịch sang tiếng
Anh là **"quantitive demanded"**. Đúng phải là **"quantity demanded"** — so với chính chú thích ở
tr. 79 của sách và với dòng "Lượng cung = quantity supplied" ở tr. 99. Lỗi đánh máy; nếu bạn tra
Google cụm sai đó sẽ không ra gì.

---

## 18. Câu hỏi tự kiểm tra

1. Định nghĩa "lượng cầu" có hai vế: *sẵn lòng mua* và *có khả năng mua*. Nêu một tình huống có vế
   đầu mà thiếu vế sau. Nó có được tính vào đường cầu không?
2. Vì sao đường cầu thị trường được dựng bằng cách cộng **theo chiều ngang** chứ không phải chiều
   dọc? Cộng dọc thì con số thu được có ý nghĩa gì không?
3. Giá cà phê tăng. Điều gì xảy ra với **cầu** trà, và với **lượng cầu** cà phê? Hai câu trả lời này
   dùng hai từ khác nhau — vì sao?
4. Xe buýt là hàng hoá thứ cấp. Nếu thu nhập bình quân trong thành phố tăng mạnh, đường cầu xe buýt
   dịch chuyển về hướng nào? Điều đó có nghĩa xe buýt là dịch vụ kém không?
5. Chính phủ bắt in cảnh báo sức khoẻ trên bao thuốc lá, **và** đồng thời tăng thuế thuốc lá. Vẽ
   (hoặc mô tả) chuyện gì xảy ra trên đồ thị. Cái nào làm dịch chuyển đường, cái nào làm di chuyển dọc?
6. Ở mức giá 2,50 đô la thị trường kem có thặng dư 6 que. Mô tả **chuỗi phản ứng** đưa thị trường về
   cân bằng. Trong chuỗi đó có đường nào dịch chuyển không?
7. Một mùa hè, giá kem tăng và lượng kem bán ra **cũng tăng**. Chuyện gì đã xảy ra: cú sốc cầu hay
   cú sốc cung? Vì sao chỉ nhìn giá thì không kết luận được?
8. Trong Bảng 4, ô "cầu giảm + cung tăng" ghi *P giảm, Q không rõ*. Giải thích **không dùng bảng**,
   chỉ bằng lập luận về hướng đẩy của hai cú dịch chuyển.
9. Sau bão, một cửa hàng giữ nguyên giá nước và bán sạch trong hai giờ; cửa hàng bên cạnh tăng giá
   gấp bốn và còn hàng tới chiều. Xét trên **hiệu quả phân bổ**, cửa hàng nào phục vụ khách tốt hơn?
   Xét trên **bình đẳng** thì sao? Vì sao hai câu trả lời có thể khác nhau?
10. Vé một buổi diễn bán hết trong ba phút và ngay sau đó xuất hiện trên chợ thứ cấp với giá gấp năm.
    Ai đang nhận phần chênh lệch đó? Nhà tổ chức có thể làm gì nếu **không** muốn tăng giá vé?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 2 — CUNG VÀ CẦU                            (Ch. 4, tr. 77–102)      ║
╠══════════════════════════════════════════════════════════════════════════╣
║  THỊ TRƯỜNG  nhóm người mua + người bán một hàng hoá — là QUAN HỆ,       ║
║              không phải địa điểm                                         ║
║  CẠNH TRANH HOÀN HẢO  ① sản phẩm giống hệt  ② quá nhiều người            ║
║              ⟹ ai cũng là NGƯỜI CHẤP NHẬN GIÁ                            ║
║                                                                          ║
║  ── CẦU ────────────────────────────────────────────────────────────     ║
║  QUY LUẬT CẦU   giá ↑ ⟹ lượng cầu ↓        đường cầu DỐC XUỐNG           ║
║      ⚠ lượng cầu = sẵn lòng VÀ CÓ KHẢ NĂNG mua                           ║
║  CẦU THỊ TRƯỜNG = cộng cầu cá nhân theo CHIỀU NGANG                      ║
║      (giữ nguyên GIÁ, cộng LƯỢNG)                                        ║
║  NĂM YẾU TỐ LÀM DỊCH CHUYỂN:                                             ║
║      thu nhập      thông thường ↑ | thứ cấp ↓                            ║
║      giá hàng liên quan  thay thế = dùng THAY | bổ sung = dùng CÙNG      ║
║      thị hiếu · kỳ vọng · số người mua                                   ║
║                                                                          ║
║  ── CUNG ───────────────────────────────────────────────────────────     ║
║  QUY LUẬT CUNG  giá ↑ ⟹ lượng cung ↑       đường cung DỐC LÊN            ║
║  BỐN YẾU TỐ: giá đầu vào · công nghệ · kỳ vọng · số người bán            ║
║      💼 giảm giá bán = TRƯỢT DỌC | giảm chi phí = DỊCH CẢ ĐƯỜNG          ║
║                                                                          ║
║  ⚠⚠ DỊCH CHUYỂN hay DI CHUYỂN DỌC — hỏi: biến đó có trên TRỤC không?     ║
║      trên trục (giá)  → DI CHUYỂN DỌC  → "thay đổi LƯỢNG cầu/cung"       ║
║      ngoài trục        → DỊCH CẢ ĐƯỜNG → "thay đổi CẦU/CUNG"             ║
║                                                                          ║
║  ── CÂN BẰNG ───────────────────────────────────────────────────────     ║
║  giao điểm hai đường:  kem $2,00 và 7 que          (Hình 8, tr. 90)      ║
║      P quá CAO → THẶNG DƯ (cung>cầu) → người bán HẠ giá                  ║
║      P quá THẤP → THIẾU HỤT (cầu>cung) → người bán TĂNG giá              ║
║      ⚠ cả hai đều là DI CHUYỂN DỌC, không đường nào dịch chuyển          ║
║                                                                          ║
║  ── BA BƯỚC PHÂN TÍCH ──────────────────────────────────────────────     ║
║  ① đường nào dịch  ② trái hay phải  ③ so cân bằng cũ với mới             ║
║      nóng (cầu→phải):  $2,00→$2,50   Q 7→10                              ║
║      bão  (cung→trái): $2,00→$2,50   Q 7→ 4                              ║
║      ⭐ GIÁ GIỐNG NHAU, LƯỢNG NGƯỢC NHAU                                  ║
║         ⟹ nhìn giá KHÔNG đủ, phải nhìn LƯỢNG mới biết cú sốc nào         ║
║                                                                          ║
║  BẢNG 4 — đừng học thuộc, chỉ một dòng:                                  ║
║      hai cú dịch đẩy CÙNG hướng  → kết luận CHẮC CHẮN                    ║
║      hai cú dịch đẩy NGƯỢC hướng → KHÔNG RÕ, tuỳ BIÊN ĐỘ                 ║
║                                                                          ║
║  📚 GIÁ CẢ = chiếc đũa mà bàn tay vô hình dùng để phân bổ nguồn lực      ║
║      "giá cắt cổ" sau thảm hoạ: hạn chế tích trữ + kéo nguồn cung tới    ║
║      ⚠ đó là lập luận HIỆU QUẢ; câu hỏi BÌNH ĐẲNG vẫn để ngỏ             ║
║                                                                          ║
║  💼 QTKD  hàng tồn chất kho = định giá CAO | cháy hàng = định giá THẤP   ║
║          vé bán hết trong 3 phút rồi chợ đen gấp 5 → bạn ĐỊNH GIÁ THẤP   ║
║          khuyến mãi định kỳ DẠY KHÁCH CHỜ → cầu hiện tại dịch trái       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **N. Gregory Mankiw, *Kinh tế học vi mô*** — bản dịch của Khoa Kinh tế, Trường ĐH Kinh tế TP.HCM,
  Cengage Learning Asia. Tệp trong kho: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  — **trang sách N = trang PDF N + 33**.
  - **Chương 4 — Các lực lượng cung và cầu trên thị trường**, tr. 77–102
    - Hình 1 *Biểu cầu và đường cầu của Catherine*, tr. 80
    - Hình 2 *Cầu thị trường là tổng của cầu các cá nhân*, tr. 81
    - Hình 3 *Dịch chuyển đường cầu*, tr. 82
    - Bảng 1 *Các biến số ảnh hưởng đến người mua*, tr. 83
    - Nghiên cứu tình huống *Hai cách giảm cầu thuốc lá* + Hình 4, tr. 84–85
    - Hình 5 *Biểu cung và đường cung của Ben*, tr. 86
    - Hình 6 *Lượng cung thị trường là tổng các lượng cung cá nhân*, tr. 87
    - Hình 7 *Dịch chuyển đường cung* + Bảng 2 *Các biến ảnh hưởng đến người bán*, tr. 87–88
    - Hình 8 *Cân bằng cung và cầu*, tr. 90
    - Hình 9 *Thị trường không cân bằng*, tr. 91
    - Bảng 3 *Ba bước phân tích sự thay đổi trong trạng thái cân bằng*, tr. 92
    - Hình 10, 11, 12 *Tác động của các dịch chuyển*, tr. 92–94
    - Bảng 4 *Điều gì xảy ra với giá và lượng khi cung hay cầu dịch chuyển*, tr. 95
    - Theo dòng thời sự *Giá tăng sau thảm hoạ* — Jeff Jacoby, "Điều gì sai với giá cắt cổ", tr. 96
- **Đính chính đã ghi trong bài:**
  - tr. 88 — đoạn "Tóm lại" của phần Cung bị **lặp và ghép nhầm** một mảnh văn bản từ đoạn "Giá đầu vào".
  - tr. 98 — *Khái niệm then chốt* in "quantitive demanded", đúng là **"quantity demanded"**.
  - Cả hai đã đối chiếu bản quét 300 dpi.
- **Liên hệ chéo:**
  - [Bài 1 — Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md), mục 15 — dịch chuyển đường ↔ di chuyển dọc.
  - Ước lượng đường cầu từ dữ liệu bán hàng thật: [Bài 14 — Tương quan và hồi quy](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md) của môn *Xác suất Thống kê*.

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md) | ch. 1–2 | 🎯 |
| **2** | **Cung và cầu** ← *bạn đang ở đây* | ch. 4 | 🎯 |
| 3 | [Độ co giãn và định giá](bai_03_do_co_gian_va_dinh_gia.md) | ch. 5 | 🎯⭐ |
| 4 | [Thặng dư và chi phí của thuế](bai_04_thang_du_va_chi_phi_cua_thue.md) | ch. 7–8 | 🔸 |
| 5 | [Chi phí sản xuất](bai_05_chi_phi_san_xuat.md) | ch. 13 | 🎯 |
| 6 | [Doanh nghiệp trên thị trường cạnh tranh](bai_06_thi_truong_canh_tranh.md) | ch. 14 | 🎯 |
| 7 | [Độc quyền và phân biệt giá](bai_07_doc_quyen_va_phan_biet_gia.md) | ch. 15 | 🎯 |
| 8 | [Cạnh tranh độc quyền và thương hiệu](bai_08_canh_tranh_doc_quyen.md) | ch. 16 | 🎯 |
| 9 | [Độc quyền nhóm và lý thuyết trò chơi](bai_09_doc_quyen_nhom_va_ly_thuyet_tro_choi.md) | ch. 17 | 🎯 |
| 10 | Lựa chọn của người tiêu dùng *(chưa viết)* | ch. 21 | 🎯 |
| 11 | Thông tin bất cân xứng và hành vi *(chưa viết)* | ch. 22 | 🎯 |
| 12 | Lao động, tiền lương, bất bình đẳng *(chưa viết)* | ch. 18–20 | 🔸 |
| 13 | Chính phủ can thiệp thị trường *(chưa viết)* | ch. 6, 12 | 🔸 |
| 14 | Thương mại, ngoại tác, hàng hoá công *(chưa viết)* | ch. 3, 9–11 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương quan trọng nhất với QTKD

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
