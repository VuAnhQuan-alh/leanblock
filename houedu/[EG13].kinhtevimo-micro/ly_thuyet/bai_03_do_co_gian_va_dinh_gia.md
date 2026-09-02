# Bài 3 — Độ co giãn và định giá

> Bài học dựng từ **Chương 5 — Độ co giãn và ứng dụng** (tr. 103–126)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🎯⭐ **Vòng 1, chương quan trọng nhất cả cuốn với người làm quản trị.** Đây là chương biến
> cung–cầu từ một câu chuyện định tính thành một **con số dùng được để định giá**.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp phụ.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 2 — Cung và cầu](bai_02_cung_va_cau.md).
> Mục 15 dùng lại hồi quy ở [bài 14 môn Xác suất Thống kê](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md).

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vì sao cần độ co giãn — chương 4 mới chỉ nói được một nửa](#1-vì-sao-cần-độ-co-giãn--chương-4-mới-chỉ-nói-được-một-nửa)
- [2. Bốn yếu tố quyết định độ co giãn của cầu theo giá](#2-bốn-yếu-tố-quyết-định-độ-co-giãn-của-cầu-theo-giá)
- [3. Công thức — và quy ước bỏ dấu âm](#3-công-thức--và-quy-ước-bỏ-dấu-âm)
- [4. ⚠️ Phương pháp trung điểm — và vì sao bắt buộc phải dùng](#4--phương-pháp-trung-điểm--và-vì-sao-bắt-buộc-phải-dùng)
- [5. Năm dạng đường cầu](#5-năm-dạng-đường-cầu)
- [6. 📚 Độ co giãn trên thực tế — những con số đã đo được](#6--độ-co-giãn-trên-thực-tế--những-con-số-đã-đo-được)
- [7. Tổng doanh thu và độ co giãn — ba quy tắc phải thuộc](#7-tổng-doanh-thu-và-độ-co-giãn--ba-quy-tắc-phải-thuộc)
- [8. Độ co giãn thay đổi dọc theo một đường cầu thẳng](#8-độ-co-giãn-thay-đổi-dọc-theo-một-đường-cầu-thẳng)
- [9. Hai độ co giãn khác của cầu](#9-hai-độ-co-giãn-khác-của-cầu)
- [10. Độ co giãn của cung](#10-độ-co-giãn-của-cung)
- [11. Năm dạng đường cung — và độ co giãn thay đổi dọc theo nó](#11-năm-dạng-đường-cung--và-độ-co-giãn-thay-đổi-dọc-theo-nó)
- [12. Ứng dụng 1 — tin tốt cho nông nghiệp lại là tin xấu cho nông dân](#12-ứng-dụng-1--tin-tốt-cho-nông-nghiệp-lại-là-tin-xấu-cho-nông-dân)
- [13. Ứng dụng 2 — vì sao OPEC không giữ được giá dầu ở mức cao](#13-ứng-dụng-2--vì-sao-opec-không-giữ-được-giá-dầu-ở-mức-cao)
- [14. Ứng dụng 3 — cấm ma tuý làm tăng hay giảm tội phạm?](#14-ứng-dụng-3--cấm-ma-tuý-làm-tăng-hay-giảm-tội-phạm)
- [15. 💼 Đo độ co giãn từ dữ liệu bán hàng thật](#15--đo-độ-co-giãn-từ-dữ-liệu-bán-hàng-thật)
- [16. Code minh hoạ](#16-code-minh-hoạ)
- [17. Tự thử](#17-tự-thử)
- [18. Từ điển thuật ngữ](#18-từ-điển-thuật-ngữ)
- [19. Câu hỏi tự kiểm tra](#19-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vì sao cần độ co giãn — chương 4 mới chỉ nói được một nửa

Chương 4 cho ta các phát biểu dạng *"giá tăng thì lượng cầu giảm"*. Sách chỉ ra ngay giới hạn của
chúng (tr. 104):

> *"…chúng ta đã thảo luận về **xu hướng** lượng cầu thay đổi chứ không phải là **mức độ** của sự thay đổi."*

Với một nhà quản trị, "xu hướng" là thứ ai cũng biết mà không giúp được gì. Câu hỏi thật sự là:
**giảm giá 10% thì bán thêm được bao nhiêu, và tổng thu về nhiều hơn hay ít hơn?** Đó là câu hỏi mà
chương này trả lời.

> **Độ co giãn** (*elasticity*): số đo mức độ phản ứng của lượng cầu hoặc lượng cung đối với các yếu
> tố tác động đến nó. — chú thích tr. 104

Sách mở đầu chương bằng một tình huống rất hay (tr. 103–104): bạn là nông dân trồng lúa mì, và một
giống lai mới làm năng suất tăng **20%**. Tin tốt hay tin xấu? Mục 12 sẽ cho câu trả lời — và nó
**ngược** với trực giác.

---

## 2. Bốn yếu tố quyết định độ co giãn của cầu theo giá

> **Độ co giãn cầu theo giá** (*price elasticity of demand*): số đo cho biết lượng cầu của một hàng
> hoá thay đổi như thế nào ứng với sự thay đổi về giá của hàng hoá đó, được tính bằng phần trăm thay
> đổi trong lượng cầu chia cho phần trăm thay đổi về giá. — chú thích tr. 104

Sách nói thẳng là **không có quy tắc chung** để xác định độ co giãn, vì đường cầu phản ánh *"nhiều
yếu tố kinh tế, xã hội và tâm lý"* (tr. 104). Nhưng dựa trên kinh nghiệm thì có **bốn** quy tắc hữu ích:

### ① Sự sẵn có của hàng hoá thay thế gần gũi

Càng **nhiều thứ thay thế được** thì cầu càng **co giãn**, vì người tiêu dùng dễ chuyển sang thứ khác.

| Hàng hoá | Độ co giãn        | Vì sao                                      |
| -------- | ----------------- | ------------------------------------------- |
| Bơ       | **co giãn**       | bơ thực vật thay thế được dễ dàng           |
| Trứng    | **không co giãn** | *"không có các sản phẩm thay thế tương tự"* |

### ② Hàng thiết yếu và hàng xa xỉ

| Loại      | Ví dụ của sách | Độ co giãn                                               |
| --------- | -------------- | -------------------------------------------------------- |
| Thiết yếu | đi khám bệnh   | **không co giãn** — giá tăng thì đi ít hơn *"một chút"*  |
| Xa xỉ     | thuyền buồm    | **co giãn** — giá tăng thì lượng cầu *"giảm đi đáng kể"* |

⚠️ **Thiết yếu hay xa xỉ không phải tính chất của món hàng.** Sách nhấn mạnh điều này (tr. 104):
nó *"không phụ thuộc vào các tính chất nội tại của nó mà phụ thuộc vào **sở thích của người mua**"*.
Với người đam mê thuyền buồm và ít lo về sức khoẻ, **thuyền buồm là thiết yếu** còn **đi khám bệnh
là xa xỉ**.

### ③ Định nghĩa thị trường

Càng **định nghĩa hẹp** thì càng **co giãn**, vì càng dễ tìm thứ thay thế. Bậc thang của sách (tr. 105):

```
   thực phẩm      định nghĩa RẤT RỘNG   →  KHÔNG co giãn (không có gì thay thế thực phẩm)
      └─ kem      hẹp hơn               →  co giãn (đổi sang món tráng miệng khác)
           └─ kem vani  rất hẹp         →  co giãn RẤT LỚN (các vị kem khác gần như
                                            thay thế hoàn hảo)
```

💼 Đây chính là lý do câu hỏi *"thị trường của ta là gì"* ở [bài 2 mục 1](bai_02_cung_va_cau.md#1-thị-trường-là-gì)
lại quan trọng đến thế. **Định nghĩa thị trường hẹp bao nhiêu thì quyền định giá của bạn nhỏ bấy nhiêu.**

### ④ Thời gian

Cầu **co giãn hơn trong dài hạn**. Ví dụ xăng của sách (tr. 105):

| Thời gian     | Phản ứng                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------- |
| Vài tháng đầu | lượng cầu xăng *"giảm xuống rất ít"*                                                                                 |
| Vài năm       | mua xe tiết kiệm nhiên liệu, chuyển sang giao thông công cộng, dọn đến gần chỗ làm → *"lượng cầu xăng giảm đáng kể"* |

⚠️ **Hệ quả trực tiếp cho việc tăng giá:** doanh số **tháng đầu** sau khi tăng giá **không** cho bạn
biết sự thật. Khách chưa kịp tìm thứ thay thế. Phải đo sau vài quý.

---

## 3. Công thức — và quy ước bỏ dấu âm

$$\text{Độ co giãn cầu theo giá} = \frac{\text{Phần trăm thay đổi lượng cầu}}{\text{Phần trăm thay đổi giá}}$$

Ví dụ của sách (tr. 105): giá kem tăng **10%**, lượng bạn mua giảm **20%**:

$$\text{Độ co giãn} = \frac{20\%}{10\%} = 2$$

Nghĩa là *"sự thay đổi của lượng cầu lớn gấp đôi sự thay đổi của giá"*.

⚠️ **Quy ước dấu.** Vì lượng cầu **nghịch biến** với giá nên con số thật ra là **âm** ($-20/+10 = -2$).
Sách nêu quy ước rõ ràng (tr. 105):

> *"Trong cuốn sách này, chúng ta thống nhất sẽ **bỏ đi dấu trừ** và thể hiện tất cả các độ co giãn
> của cầu theo giá bằng các **số dương**. (Toán học gọi đây là **giá trị tuyệt đối**.)"*

Với quy ước này: **độ co giãn càng lớn nghĩa là phản ứng càng mạnh.**

---

## 4. ⚠️ Phương pháp trung điểm — và vì sao bắt buộc phải dùng

Đây là chỗ **mọi người tính sai đầu tiên**, và sách dành nguyên một mục cho nó (tr. 105–106).

Xét hai điểm trên đường cầu:

|            |     Giá | Lượng |
| ---------- | ------: | ----: |
| **Điểm A** | 4 đô la |   120 |
| **Điểm B** | 6 đô la |    80 |

Tính theo cách thông thường (chia cho **giá trị ban đầu**):

| Hướng | %Δ giá | %Δ lượng |       Độ co giãn |
| ----- | -----: | -------: | ---------------: |
| A → B |   +50% |     −33% | 33/50 = **0,66** |
| B → A |   −33% |     +50% |  50/33 = **1,5** |

**Cùng hai điểm, hai kết quả khác nhau gấp hơn hai lần.** Nguyên nhân: *"tỷ lệ phần trăm thay đổi
được tính từ các cơ sở khác nhau"* (tr. 106).

**Phương pháp trung điểm** sửa chỗ này: chia sự thay đổi cho **điểm giữa** (trung bình) của hai mức,
thay vì cho mức ban đầu.

|           |         Giá |   Lượng |
| --------- | ----------: | ------: |
| Điểm giữa | **5 đô la** | **100** |

Bây giờ đi từ A sang B: giá tăng $2/5 = 40\%$, lượng giảm $40/100 = 40\%$ → độ co giãn = **1**.
Đi ngược lại: giá giảm 40%, lượng tăng 40% → vẫn **1**. **Hai chiều cho cùng một số.**

Công thức đầy đủ (tr. 106):

$$\text{Độ co giãn của cầu theo giá} = \frac{(Q_2 - Q_1) \big/ \left[(Q_2 + Q_1)/2\right]}{(P_2 - P_1) \big/ \left[(P_2 + P_1)/2\right]}$$

📌 Nhưng chú ý câu sách viết ngay sau đó (tr. 106), rất đáng nhớ khi ôn thi:

> *"Tuy nhiên trong cuốn sách này, chúng ta hiếm khi thực hiện những tính toán như vậy. Đối với hầu
> hết các mục đích của chúng ta, độ co giãn **thể hiện điều gì** — phản ứng của lượng cầu trước sự
> thay đổi giá cả — có vai trò **quan trọng hơn cách tính**."*

Mục 16 chạy cả hai cách cạnh nhau để bạn thấy sự bất đối xứng biến mất.

---

## 5. Năm dạng đường cầu

Phân loại (tr. 106–107):

| Tên                         | Độ co giãn   | Nghĩa                                                  |
| --------------------------- | ------------ | ------------------------------------------------------ |
| **Hoàn toàn không co giãn** | $= 0$        | đường **thẳng đứng**; giá thế nào lượng cũng không đổi |
| **Không co giãn**           | $< 1$        | lượng thay đổi **ít hơn** giá                          |
| **Co giãn đơn vị**          | $= 1$        | lượng thay đổi **đúng bằng** giá                       |
| **Co giãn**                 | $> 1$        | lượng thay đổi **nhiều hơn** giá                       |
| **Hoàn toàn co giãn**       | $\to \infty$ | đường **nằm ngang**                                    |

Quy tắc liên hệ với hình dạng (tr. 107):

> *"Đường cầu càng **ít dốc**, độ co giãn càng **lớn**. Đường cầu càng **dốc**, thì độ co giãn càng **nhỏ**."*

**Hình 1, tr. 107** minh hoạ cả năm, tất cả đều dùng cùng một cú tăng giá từ **4 lên 5 đô la** (tăng
**22%** theo phương pháp trung điểm):

| Hình | Trường hợp              | Lượng                                                                                             | %Δ lượng |
| ---- | ----------------------- | ------------------------------------------------------------------------------------------------- | -------: |
| (a)  | hoàn toàn không co giãn | 100 → 100                                                                                         |       0% |
| (b)  | không co giãn           | 100 → 90                                                                                          |     −11% |
| (c)  | co giãn đơn vị          | 100 → 80                                                                                          |     −22% |
| (d)  | co giãn                 | 100 → 50                                                                                          |     −67% |
| (e)  | hoàn toàn co giãn       | ở giá **trên** 4 đô la lượng cầu bằng 0; ở đúng 4 đô la, người tiêu dùng mua **bất cứ lượng nào** |        — |

💡 **Mẹo nhớ của chính sách (tr. 108)**, hữu ích thật:

> *"Các đường cầu **không co giãn** (**I**nelastic), chẳng hạn như trong Hình 1(a), trông giống chữ
> cái **I** [thẳng đứng]. Đây không phải là điều quan trọng, nhưng nó có thể giúp bạn trong kỳ thi tới."*

---

## 6. 📚 Độ co giãn trên thực tế — những con số đã đo được

Hộp **"Bạn có biết", tr. 108** cho các ước lượng thực nghiệm:

| Mặt hàng                    | Độ co giãn của cầu theo giá |
| --------------------------- | --------------------------: |
| Trứng                       |                     **0,1** |
| Chăm sóc y tế               |                     **0,2** |
| Gạo                         |                     **0,5** |
| Nhà ở                       |                     **0,7** |
| Thịt bò                     |                     **1,6** |
| Bữa ăn tại nhà hàng         |                     **2,3** |
| Nước giải khát Mountain Dew |                     **4,4** |

Bảng này minh hoạ cả bốn quy tắc ở mục 2 cùng lúc: **thiết yếu** (trứng, y tế, gạo) nằm dưới 1;
**xa xỉ / dễ thay thế** (nhà hàng, thịt bò) nằm trên 1; và **định nghĩa hẹp** đẩy con số lên cao nhất —
"nước giải khát" nói chung sẽ không co giãn bằng **một nhãn hiệu cụ thể** là Mountain Dew.

⚠️ **Sách tự cảnh báo về chính bảng này** (tr. 108), và đây là đoạn đáng đọc kỹ:

1. Các kỹ thuật thống kê để ước tính *"cần tới một số giả định, và những giả định này có thể **không
   đúng trong thực tế**"*.
2. *"Độ co giãn của cầu theo giá **không nhất thiết phải giống nhau ở tất cả các điểm** trên một
   đường cầu"* — chính là nội dung mục 8.
3. Vì vậy: *"bạn cũng đừng quá ngạc nhiên nếu các nghiên cứu khác nhau **báo cáo khác nhau** về độ co
   giãn của cầu theo giá của cùng một hàng hoá."*

💼 Nói cách khác: **đừng lấy một con số độ co giãn từ sách vở rồi áp vào doanh nghiệp của bạn.**
Phải đo trên chính dữ liệu của mình — mục 15.

---

## 7. Tổng doanh thu và độ co giãn — ba quy tắc phải thuộc

> **Tổng doanh thu** (*total revenue*): lượng tiền người mua chi trả cho người bán một hàng hoá,
> được tính bằng cách nhân giá của hàng hoá với sản lượng bán ra. — chú thích tr. 108

$$TR = P \times Q$$

Trên đồ thị, đó là **diện tích hình chữ nhật** dưới đường cầu: chiều cao $P$, chiều rộng $Q$
(Hình 2, tr. 109 — với $P = 4$ và $Q = 100$ thì $TR = 400$ đô la).

Khi giá tăng, **hai lực đối nghịch nhau** tác động lên doanh thu:

```
   giá TĂNG
     ├── mỗi đơn vị bán được thu NHIỀU tiền hơn      →  doanh thu TĂNG  (diện tích A)
     └── nhưng bán được ÍT đơn vị hơn                →  doanh thu GIẢM  (diện tích B)

   Bên nào thắng?  ⟹  ĐỘ CO GIÃN quyết định.
```

**Hình 3, tr. 109** so hai trường hợp, cùng cú tăng giá từ 4 lên 5 đô la:

|                       | Lượng        | Tổng doanh thu      | Kết quả                    |
| --------------------- | ------------ | ------------------- | -------------------------- |
| Cầu **không co giãn** | 100 → **90** | 400 → **450** đô la | doanh thu **tăng** — A > B |
| Cầu **co giãn**       | 100 → **70** | 400 → **350** đô la | doanh thu **giảm** — A < B |

### ⭐ Ba quy tắc (tr. 110) — thuộc lòng ba dòng này

> - Khi cầu **không co giãn** (độ co giãn thấp hơn 1), giá và tổng doanh thu di chuyển **theo cùng một hướng**.
> - Khi cầu **co giãn** (độ co giãn cao hơn 1), giá và tổng doanh thu di chuyển **theo hướng ngược nhau**.
> - Nếu cầu là **co giãn đơn vị** (bằng 1), tổng doanh thu **không đổi** khi giá thay đổi.

💼 **Đây là ba dòng sinh lời nhất trong cả cuốn sách.** Dịch sang ngôn ngữ kinh doanh:

| Nếu cầu của bạn         | thì **tăng** giá làm doanh thu | và **giảm** giá làm doanh thu |
| ----------------------- | ------------------------------ | ----------------------------- |
| không co giãn ($e < 1$) | **tăng**                       | **giảm** ← giảm giá là tự sát |
| co giãn ($e > 1$)       | **giảm**                       | **tăng**                      |

Nghĩa là **câu hỏi "nên tăng hay giảm giá" có một câu trả lời bằng số**, và con số đó là $e$.
Không phải chuyện cảm tính hay chuyện "chiến lược".

⚠️ **Nhưng doanh thu không phải lợi nhuận.** Tối đa hoá doanh thu và tối đa hoá lợi nhuận là **hai
điểm khác nhau** — vì bán thêm hàng thì tốn thêm chi phí. Điểm tối đa hoá lợi nhuận luôn nằm ở
**giá cao hơn** điểm tối đa hoá doanh thu. Đó là **bài 5–6** (chi phí sản xuất, MR = MC).

---

## 8. Độ co giãn thay đổi dọc theo một đường cầu thẳng

Đây là ý tinh tế nhất chương, và cũng là ý bị hiểu sai nhiều nhất.

> **Độ dốc không đổi ≠ độ co giãn không đổi.**

Sách giải thích vì sao (tr. 111):

> *"Điều này xảy ra vì **độ dốc là tỷ lệ thay đổi tuyệt đối** giữa hai biến, trong khi đó **độ co giãn
> là tỷ lệ phần trăm thay đổi** (hay tỷ lệ thay đổi tương đối) giữa hai biến."*

**Hình 4, tr. 110** — đường cầu $Q = 14 - 2P$ (mỗi 1 đô la giảm giá làm lượng cầu tăng 2 đơn vị):

|  Giá | Lượng | Tổng doanh thu | %Δ giá | %Δ lượng | Độ co giãn | Mô tả              |
| ---: | ----: | -------------: | -----: | -------: | ---------: | ------------------ |
|   $7 |     0 |             $0 |     15 |      200 |   **13,0** | co giãn            |
|   $6 |     2 |             12 |     18 |       67 |    **3,7** | co giãn            |
|   $5 |     4 |             20 |     22 |       40 |    **1,8** | co giãn            |
|   $4 |     6 |         **24** |     29 |       29 |    **1,0** | **co giãn đơn vị** |
|   $3 |     8 |         **24** |     40 |       22 |    **0,6** | không co giãn      |
|   $2 |    10 |             20 |     67 |       18 |    **0,3** | không co giãn      |
|   $1 |    12 |             12 |    200 |       15 |    **0,1** | không co giãn      |
|   $0 |    14 |             $0 |        |          |            |                    |

Quy tắc rút ra (tr. 111):

> Tại các điểm có **mức giá thấp và lượng cao**, đường cầu **không co giãn**.
> Tại các điểm có **mức giá cao và lượng thấp**, đường cầu **co giãn**.

Và cột **tổng doanh thu** minh hoạ đúng ba quy tắc ở mục 7 (sách nêu rõ ở tr. 111):

- Giá **1 đô la** (không co giãn) → tăng lên 2 đô la thì doanh thu **tăng** (12 → 20). ✅ cùng hướng
- Giá **5 đô la** (co giãn) → tăng lên 6 đô la thì doanh thu **giảm** (20 → 12). ✅ ngược hướng
- Giữa **3 và 4 đô la** (co giãn đơn vị) → doanh thu ở hai mức giá này **bằng nhau** (24 = 24). ✅

💼 **Ý nghĩa quản trị của mục này rất lớn:** *"độ co giãn của cửa hàng tôi bằng 1,8"* là một câu
**chưa đầy đủ**. Phải hỏi: **ở vùng giá nào?** Con số đo được ở vùng giá 35–50 nghìn **không dùng
được** cho câu hỏi "có nên bán 120 nghìn không". Mục 15 sẽ nhắc lại đúng cảnh báo này.

---

## 9. Hai độ co giãn khác của cầu

### Độ co giãn của cầu theo thu nhập

> **Độ co giãn cầu theo thu nhập** (*income elasticity of demand*): số đo cho biết lượng cầu của một
> hàng hoá thay đổi như thế nào ứng với sự thay đổi trong thu nhập của người tiêu dùng. — chú thích tr. 111

$$\text{Độ co giãn theo thu nhập} = \frac{\text{Phần trăm thay đổi lượng cầu}}{\text{Phần trăm thay đổi thu nhập}}$$

⚠️ **Ở đây dấu KHÔNG bị bỏ** — dấu chính là thông tin:

| Dấu       | Loại hàng                 | Ví dụ của sách  |
| --------- | ------------------------- | --------------- |
| **Dương** | hàng hoá **thông thường** | hầu hết mọi thứ |
| **Âm**    | hàng hoá **thứ cấp**      | đi xe buýt      |

Và ngay trong hàng thông thường, mức độ cũng rất khác nhau (tr. 111–112):

| Nhóm                             | Độ co giãn theo thu nhập | Lý do sách nêu                                                                       |
| -------------------------------- | ------------------------ | ------------------------------------------------------------------------------------ |
| Thiết yếu — thực phẩm, quần áo   | **nhỏ**                  | *"người tiêu dùng phải mua chúng ngay cả khi thu nhập của họ thấp"*                  |
| Xa xỉ — trứng cá muối, kim cương | **cao**                  | *"nếu thu nhập của họ quá thấp, họ vẫn có thể sống mà không cần những hàng hoá này"* |

### Độ co giãn của cầu theo giá chéo

> **Độ co giãn của cầu theo giá chéo** (*cross-price elasticity of demand*): số đo cho biết lượng cầu
> của một hàng hoá thay đổi như thế nào ứng với sự thay đổi về giá của một hàng hoá khác. — chú thích tr. 112

$$\text{Độ co giãn theo giá chéo} = \frac{\text{\% thay đổi lượng cầu hàng hoá 1}}{\text{\% thay đổi giá hàng hoá 2}}$$

Dấu lại là thông tin, và lần này nó **định nghĩa quan hệ giữa hai sản phẩm**:

| Dấu       | Quan hệ      | Ví dụ của sách                                                              |
| --------- | ------------ | --------------------------------------------------------------------------- |
| **Dương** | **thay thế** | bánh mì kẹp xúc xích ↔ hamburger — giá xúc xích tăng thì cầu hamburger tăng |
| **Âm**    | **bổ sung**  | máy tính ↔ phần mềm — giá máy tính tăng thì cầu phần mềm giảm               |

### 💼 Góc QTKD — hai con số này trả lời hai câu hỏi rất cụ thể

| Câu hỏi kinh doanh                                      | Đo bằng                                                         |
| ------------------------------------------------------- | --------------------------------------------------------------- |
| Kinh tế suy thoái thì ngành ta bị ảnh hưởng nặng không? | **độ co giãn theo thu nhập** — càng cao càng theo chu kỳ        |
| Nên bán thêm dòng phổ thông hay dòng cao cấp?           | độ co giãn theo thu nhập của từng dòng                          |
| **Ai thật sự là đối thủ của ta?**                       | **độ co giãn theo giá chéo** — dương và lớn = đối thủ trực tiếp |
| Nên bán kèm (bundle) hai sản phẩm nào?                  | giá chéo **âm** = hàng bổ sung, bán kèm hợp lý                  |

⭐ Dòng thứ ba là dòng hay nhất. **Ai là đối thủ của bạn không phải là chuyện cảm nhận — nó là một
con số đo được.** Nếu đối thủ giảm giá 10% mà doanh số bạn không nhúc nhích, họ **không** cạnh tranh
với bạn, dù cùng bán một loại hàng.

---

## 10. Độ co giãn của cung

Đối xứng hoàn toàn với phần cầu.

> **Độ co giãn của cung theo giá** (*price elasticity of supply*): số đo cho biết lượng cung của một
> hàng hoá thay đổi như thế nào ứng với sự thay đổi về giá của hàng hoá đó. — chú thích tr. 112

$$\text{Độ co giãn của cung theo giá} = \frac{\text{Phần trăm thay đổi lượng cung}}{\text{Phần trăm thay đổi giá}}$$

Yếu tố quyết định: **sự linh hoạt của người bán trong việc thay đổi lượng hàng mình sản xuất** (tr. 113).

|                         | Ví dụ của sách                                                | Độ co giãn        |
| ----------------------- | ------------------------------------------------------------- | ----------------- |
| Không thể sản xuất thêm | nhà ở bãi biển — *"gần như không thể sản xuất thêm đất được"* | **không co giãn** |
| Sản xuất được thêm      | sách, xe hơi, truyền hình                                     | **co giãn**       |

### ⭐ Nhưng yếu tố lớn nhất vẫn là THỜI GIAN

Sách nói rõ đây là *"yếu tố quyết định độ co giãn của cung theo giá"* trong hầu hết thị trường (tr. 113):

|                          | Ngắn hạn                                 | Dài hạn                                           |
| ------------------------ | ---------------------------------------- | ------------------------------------------------- |
| Doanh nghiệp làm được gì | *"không dễ thay đổi quy mô các nhà máy"* | **xây nhà máy mới** hoặc **đóng cửa nhà máy cũ**  |
| Ngành làm được gì        | —                                        | công ty mới **gia nhập**, công ty cũ **rời khỏi** |
| Kết quả                  | lượng cung **không nhạy** với giá        | lượng cung **thay đổi đáng kể**                   |

### Ví dụ tính toán (tr. 113)

Giá một gallon sữa tăng từ **2,85** lên **3,15** đô la; người chăn nuôi tăng sản xuất từ **9.000** lên
**11.000** lít mỗi tháng.

$$\%\Delta P = \frac{3{,}15 - 2{,}85}{3{,}00} \times 100 = 10\% \qquad
\%\Delta Q = \frac{11.000 - 9.000}{10.000} \times 100 = 20\%$$

$$\text{Độ co giãn của cung} = \frac{20\%}{10\%} = \mathbf{2{,}0}$$

---

## 11. Năm dạng đường cung — và độ co giãn thay đổi dọc theo nó

**Hình 5, tr. 114** — cùng cấu trúc với Hình 1, cùng cú tăng giá 4 → 5 đô la (**22%**):

| Hình | Trường hợp                         | Lượng                                                                                        | %Δ lượng |
| ---- | ---------------------------------- | -------------------------------------------------------------------------------------------- | -------: |
| (a)  | hoàn toàn không co giãn ($e = 0$)  | 100 → 100                                                                                    |       0% |
| (b)  | không co giãn ($e < 1$)            | 100 → 110                                                                                    |     +10% |
| (c)  | co giãn đơn vị ($e = 1$)           | 100 → 125                                                                                    |     +22% |
| (d)  | co giãn ($e > 1$)                  | 100 → 200                                                                                    |     +67% |
| (e)  | hoàn toàn co giãn ($e \to \infty$) | ở đúng 4 đô la nhà sản xuất cung ở **bất cứ mức sản lượng nào**; dưới 4 đô la lượng cung = 0 |        — |

### 📚 Vì sao độ co giãn của cung thường GIẢM khi sản lượng tăng

**Hình 6, tr. 115** cho một trường hợp *"điển hình cho một ngành, trong đó các công ty có nhà máy với
công suất sản xuất hạn chế"* — và đây là phần rất sát thực tế sản xuất:

```
   SẢN LƯỢNG THẤP  (còn nhà máy, thiết bị nhàn rỗi)
      → chỉ cần giá nhích lên là doanh nghiệp có lãi và dùng ngay năng lực dư
      → cung RẤT CO GIÃN
             │
             ▼
   SẢN LƯỢNG CAO  (công suất đã dùng tối đa)
      → muốn tăng nữa phải XÂY NHÀ MÁY MỚI
      → giá phải tăng ĐÁNG KỂ mới bù nổi chi phí đó
      → cung KÉM CO GIÃN
```

Con số minh hoạ trong hình:

| Vùng           | Giá       | Lượng     | %Δ giá | %Δ lượng | Độ co giãn              |
| -------------- | --------- | --------- | -----: | -------: | ----------------------- |
| Sản lượng thấp | $3 → $4   | 100 → 200 |    29% |      67% | **> 1** — co giãn       |
| Sản lượng cao  | $12 → $15 | 500 → 525 |    22% |       5% | **< 1** — không co giãn |

💼 Đây là hình vẽ mô tả **chính xác** cái mà bên vận hành gọi là *"đụng trần công suất"*. Trước khi
đụng trần, tăng sản lượng gần như miễn phí; sau khi đụng trần, mỗi đơn vị thêm đều rất đắt. Sẽ gặp
lại đầy đủ ở **bài 5** dưới tên **chi phí biên tăng dần**.
---

## 12. Ứng dụng 1 — tin tốt cho nông nghiệp lại là tin xấu cho nông dân

Quay lại tình huống mở chương (tr. 116): Đại học Kansas công bố một **giống lai mới làm tăng năng
suất 20% trên mỗi acre**. Bạn là nông dân. Bạn khá hơn hay tệ hơn?

Dùng ba bước của [bài 2](bai_02_cung_va_cau.md#12-ba-bước-phân-tích-sự-thay-đổi-của-trạng-thái-cân-bằng):

| Bước | Lập luận                                                                                                                                                                                     |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ①    | Giống lai tác động vào **đường cung**. Cầu **không đổi** — *"nhu cầu về lúa mì của người tiêu dùng ở bất cứ mức giá nào được cho là không bị ảnh hưởng bởi sự ra đời của một giống lai mới"* |
| ②    | Sản xuất được nhiều hơn trên mỗi acre → cung dịch **sang phải**, $S_1 \to S_2$                                                                                                               |
| ③    | **Hình 7, tr. 116**: lượng bán tăng từ **100 lên 110**, giá giảm từ **3 xuống 2 đô la**                                                                                                      |

Bây giờ tính tổng doanh thu của nông dân:

$$\text{trước: } 3 \times 100 = \mathbf{300} \text{ đô la} \qquad\to\qquad \text{sau: } 2 \times 110 = \mathbf{220} \text{ đô la}$$

**Nông dân mất 80 đô la.** Vì sao? Vì cầu về lương thực **không co giãn**:

> *"Trong thực tế, cầu về các loại thực phẩm thiết yếu như lúa mì thường không co giãn bởi vì các mặt
> hàng này tương đối rẻ tiền và ít hàng hoá thay thế gần gũi."* (tr. 117)

Giá giảm **đáng kể** trong khi lượng chỉ tăng **nhẹ** → $P \times Q$ giảm. Đúng quy tắc số 1 ở mục 7.

### ⭐ Nghịch lý sâu hơn: vì sao nông dân vẫn dùng giống mới?

Sách đặt đúng câu hỏi (tr. 117): nếu giống mới làm họ nghèo đi, sao họ lại dùng nó? Câu trả lời nằm
ở **cấu trúc thị trường cạnh tranh**:

> *"Vì mỗi người nông dân chỉ là một phần nhỏ của thị trường lúa mì, họ **chấp nhận giá lúa mì do thị
> trường quyết định**. Đối với bất cứ mức giá nào của lúa mì, sẽ tốt hơn cho họ khi sử dụng giống lai
> mới để sản xuất và bán nhiều lúa mì hơn. Tuy nhiên, khi **tất cả** nông dân làm điều này, cung lúa
> mì tăng, giá giảm, và tất cả đều thiệt."*

📌 Đây là một **tình thế tiến thoái lưỡng nan**: lựa chọn tốt nhất cho *từng* người lại dẫn tới kết
cục xấu cho *tất cả*. Nó sẽ có tên chính thức và được phân tích đầy đủ ở **bài 9** (chương 17, lý
thuyết trò chơi).

### Con số lịch sử (tr. 117)

|              | Số người làm trang trại ở Hoa Kỳ | Tỷ lệ lực lượng lao động |
| ------------ | -------------------------------: | -----------------------: |
| **Năm 1950** |                         10 triệu |                  **17%** |
| **Ngày nay** |                     dưới 3 triệu |                   **2%** |

Và câu quan trọng: *"mặc dù có sự sụt giảm 70 phần trăm số nông dân, sản lượng các loại cây trồng và
vật nuôi mà các trang trại ở Hoa Kỳ hiện nay **cao gấp đôi** sản lượng mà họ đã sản xuất trong năm 1950."*

### Nghịch lý chính sách nông nghiệp (tr. 117–118)

Một số chương trình trợ giúp nông dân bằng cách **khuyên họ không nên trồng hết diện tích đất**. Nghe
vô lý, nhưng đúng logic ở trên:

> *"Với cầu cho các sản phẩm của họ không co giãn, nông dân, với tư cách là **một nhóm**, sẽ thu được
> tổng doanh thu lớn hơn nếu họ cung cấp **ít hơn** cho thị trường. Không một nông dân riêng lẻ nào bỏ
> hoang đất của họ… Nhưng nếu **tất cả** các nông dân cùng làm như vậy với nhau, mỗi người trong số họ
> có thể thu được nhiều hơn."*

⚠️ **Và câu cảnh tỉnh mà sách đặt ngay sau đó** (tr. 118) — đừng bỏ qua:

> *"…điều quan trọng là hãy nhớ rằng những gì tốt cho nông dân **không nhất thiết phải tốt cho toàn bộ
> xã hội**. Cải tiến công nghệ nông nghiệp có thể có hại cho nông dân bởi vì nó làm giảm vai trò của
> người nông dân, nhưng nó chắc chắn là tốt cho người tiêu dùng, những người được mua thực phẩm với
> giá rẻ hơn."*

### 💼 Góc QTKD — nghịch lý này lặp lại y hệt trong nhiều ngành

Cấu trúc *"cải tiến công nghệ → cung tăng → giá giảm → ngành nghèo đi"* xuất hiện ở mọi ngành có
**cầu không co giãn** và **nhiều người bán nhỏ**:

| Ngành               | Cải tiến                             | Kết cục cho người bán              |
| ------------------- | ------------------------------------ | ---------------------------------- |
| Vận tải hành khách  | ứng dụng gọi xe hạ chi phí điều phối | cước giảm, thu nhập tài xế/km giảm |
| Nhiếp ảnh, thiết kế | công cụ giúp làm nhanh gấp nhiều lần | đơn giá mỗi sản phẩm giảm mạnh     |
| Nuôi trồng thuỷ sản | giống và thức ăn tốt hơn             | được mùa mất giá                   |

Bài học rút ra: **năng suất cao hơn chỉ làm bạn giàu hơn nếu bạn giữ được giá.** Muốn giữ giá thì phải
làm cho cầu **bớt co giãn** — khác biệt hoá, thương hiệu, chuyển sang phân khúc ít thay thế. Đó là
toàn bộ nội dung **bài 8**.

---

## 13. Ứng dụng 2 — vì sao OPEC không giữ được giá dầu ở mức cao

**Bối cảnh lịch sử mà sách ghi lại** (tr. 118):

| Giai đoạn   | Diễn biến giá dầu (đã điều chỉnh theo lạm phát)                                |
| ----------- | ------------------------------------------------------------------------------ |
| 1973 → 1974 | tăng **hơn 50%**                                                               |
| 1979 → 1981 | tăng **gần gấp đôi**                                                           |
| 1982 → 1985 | **giảm khoảng 10% mỗi năm**                                                    |
| **1986**    | hợp tác giữa các thành viên OPEC **hoàn toàn bị phá vỡ**, giá dầu **giảm 45%** |
| 1990        | trở lại mức của **năm 1970**, và nằm ở mức thấp gần suốt thập niên 1990        |

Vì sao thành công trong ngắn hạn mà thất bại trong dài hạn? Toàn bộ nằm ở **độ co giãn thay đổi theo
thời gian** (Hình 8, tr. 119):

```
   NGẮN HẠN — cả cung và cầu đều ÍT CO GIÃN (hai đường đều RẤT DỐC)
      cung không co giãn: dự trữ và khả năng khai thác không đổi nhanh được
      cầu không co giãn : thói quen mua sắm không đổi ngay lập tức
      ⟹ OPEC cắt cung một chút → GIÁ TĂNG RẤT MẠNH → thu nhập TĂNG   ✅

   DÀI HẠN — cả hai đều CO GIÃN HƠN (hai đường THOẢI hơn)
      cung : nhà sản xuất NGOÀI OPEC tăng thăm dò, khai thác, lọc dầu
      cầu  : người tiêu dùng thay xe cũ tốn xăng bằng xe tiết kiệm hơn
      ⟹ CÙNG một mức cắt cung → GIÁ CHỈ TĂNG NHẸ → lợi ích ÍT ĐI      ❌
```

Kết luận nguyên văn (tr. 119):

> *"Cartel này nhận ra rằng **tăng giá trong ngắn hạn dễ dàng hơn trong dài hạn**."*

📌 Sách còn thêm một chú thích cẩn thận (tr. 118): những dao động giá dầu **trong thập kỷ đầu thế kỷ
21** có nguyên nhân chính là **thay đổi trong nhu cầu thế giới** (kinh tế Trung Quốc phát triển nhanh,
rồi suy thoái 2008–2009), **chứ không phải** do OPEC hạn chế cung.

### 💼 Góc QTKD — "chúng ta cứ tăng giá đi, khách quen rồi"

Đây chính là cái bẫy OPEC, và doanh nghiệp mắc phải rất thường xuyên:

1. **Quý đầu sau khi tăng giá**: doanh số gần như không đổi. Kết luận vội: *"cầu không co giãn, tăng
   tiếp!"*
2. **Sau 2–4 quý**: khách đã tìm được nhà cung cấp khác, đã đổi quy trình, đã đàm phán hợp đồng mới.
   Doanh số **rơi**, và **rất khó lấy lại** — vì họ đã tốn công chuyển đổi rồi, không quay lại nữa.

⚠️ **Đo tác động của một lần tăng giá bằng số liệu một tháng là sai về mặt phương pháp**, không phải
chỉ là thiếu kiên nhẫn. Độ co giãn ngắn hạn và dài hạn là **hai con số khác nhau**, và cái quyết định
số phận doanh nghiệp là cái thứ hai.

---

## 14. Ứng dụng 3 — cấm ma tuý làm tăng hay giảm tội phạm?

Ứng dụng này hay ở chỗ nó cho thấy độ co giãn có thể **đảo ngược kết luận của một chính sách**.

Bối cảnh (tr. 119–121): người nghiện thường phạm tội (trộm cắp) để có tiền mua ma tuý. So sánh **hai
chính sách** cùng nhằm giảm sử dụng ma tuý (**Hình 9, tr. 121**):

|                                        | (a) **Ngăn cấm** — tăng cường tuần tra, bắt giữ | (b) **Giáo dục** về tác hại   |
| -------------------------------------- | ----------------------------------------------- | ----------------------------- |
| Tác động vào                           | **đường cung** → dịch **trái**                  | **đường cầu** → dịch **trái** |
| Giá ma tuý                             | **TĂNG**                                        | **GIẢM**                      |
| Lượng sử dụng                          | giảm                                            | giảm                          |
| **Tổng số tiền người nghiện phải chi** | **TĂNG** (vì cầu không co giãn)                 | **GIẢM**                      |
| Tội phạm liên quan                     | **TĂNG**                                        | **GIẢM**                      |

Nguyên văn phần (a) trong chú thích Hình 9:

> *"Nếu cầu ma tuý không co giãn, tổng số tiền mà người sử dụng ma tuý phải trả **tăng lên**, ngay cả
> khi lượng ma tuý sử dụng giảm xuống."*

Và phần (b):

> *"Bởi vì cả giá và lượng giảm, số tiền mà người sử dụng ma tuý phải trả **sẽ giảm xuống**… trái ngược
> với ngăn chặn ma tuý, giáo dục về tác hại của ma tuý có thể giảm sử dụng ma tuý **và** tội phạm liên
> quan tới ma tuý."*

⚠️ **Sách trình bày cả phản biện** (tr. 121) — đây là chỗ đáng học về cách lập luận:

> *"Cầu về ma tuý có thể không co giãn **trong ngắn hạn** bởi vì giá cao chỉ làm giảm mức sử dụng ma
> tuý của người nghiện không đáng kể. Nhưng cầu có thể **co giãn hơn trong dài hạn** vì giá cao sẽ hạn
> chế việc thử ma tuý trong giới trẻ… Trong trường hợp này, ngăn chặn ma tuý sẽ làm **tăng** tội phạm
> liên quan đến ma tuý **trong ngắn hạn**, nhưng lại có thể **giảm** nó **trong dài hạn**."*

📌 **Điều đáng rút ra không phải là chính sách nào đúng.** Đó là: **kết luận phụ thuộc vào một con số
đo được** — độ co giãn ngắn hạn và dài hạn của cầu ma tuý — chứ không phụ thuộc vào quan điểm chính
trị của người tranh luận. Đây là một **câu hỏi thực chứng** nằm bên trong một tranh cãi **chuẩn tắc**
([bài 1, mục 13](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#13-phát-biểu-thực-chứng-và-phát-biểu-chuẩn-tắc)).

Mục 16 chạy cả hai kịch bản bằng số để bạn thấy tổng chi tiêu đi **hai hướng ngược nhau**.

---

## 15. 💼 Đo độ co giãn từ dữ liệu bán hàng thật

Sách dừng ở *"độ co giãn là gì"* và tự nhận *"chúng ta hiếm khi thực hiện những tính toán như vậy"*
(tr. 106). Nhưng với người làm quản trị, **con số cụ thể mới là thứ dùng được**. Mục này là phần
khoá học thêm vào.

### Cách 1 — hai điểm, phương pháp trung điểm

Dùng khi bạn có **đúng hai** quan sát (trước và sau một lần đổi giá). Đơn giản, nhưng **mong manh**:
chỉ cần một tháng bất thường là con số lệch hẳn.

### Cách 2 — hồi quy log–log, dùng toàn bộ dữ liệu

Đây là chỗ **môn Xác suất Thống kê gặp môn Kinh tế vi mô**. Giả sử đường cầu có dạng luỹ thừa:

$$Q = A \cdot P^{\,b}$$

Lấy logarit hai vế:

$$\ln Q = \ln A + b \ln P$$

Đây là một **đường thẳng** theo $\ln P$. Và điều kỳ diệu:

> ⭐ **Hệ số góc $b$ của hồi quy $\ln Q$ theo $\ln P$ CHÍNH LÀ độ co giãn** (mang dấu âm).

Chứng minh một dòng: $\dfrac{d\ln Q}{d\ln P} = \dfrac{dQ/Q}{dP/P} = \dfrac{\%\Delta Q}{\%\Delta P}$ —
đúng định nghĩa độ co giãn ở mục 3.

Nghĩa là bạn **đã có sẵn công cụ** rồi: đó chính là công thức hệ số góc ở
[bài 14 môn Xác suất Thống kê](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md):

$$b = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
\qquad \text{với } x = \ln P,\ y = \ln Q$$

Mục 16 chạy đúng phép này trên 12 tháng dữ liệu bán hàng của một quán cà phê.

### ⚠️ Ba cạm bẫy — và đây mới là phần quan trọng nhất

Con số hồi quy trông rất thuyết phục. Ba lý do khiến nó có thể **sai hoàn toàn**:

**① Bỏ sót biến.** Tháng bạn giảm giá cũng là tháng bạn chạy quảng cáo? Vậy hệ số bạn đo được là tác
động của **giá cộng quảng cáo**, không phải của riêng giá. Đúng cái bẫy hộp quẹt – ung thư ở
[bài 1, mục 15](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#15--đọc-đồ-thị-độ-dốc-bỏ-sót-biến-nhân-quả-ngược).

**② Nhân quả ngược.** Bạn giảm giá **vì** thấy bán chậm — chứ không phải bán chạy **vì** giảm giá. Khi
đó dấu của hệ số bị bóp méo hoặc thậm chí đảo chiều.

**③ Ngoại suy.** Dữ liệu chỉ phủ vùng giá 35–50 nghìn. Dùng con số đó để trả lời *"bán 120 nghìn thì
sao"* là **ngoại suy** — và mục 8 đã cho thấy độ co giãn **thay đổi dọc theo đường cầu**, nên nó gần
như chắc chắn sai.

> **Cách chắc chắn nhất vẫn là A/B test có đối chứng**: chia ngẫu nhiên khách hàng (hoặc cửa hàng, hoặc
> tuần) thành hai nhóm giá, rồi so sánh. Đó là
> [bài 12–13 môn Xác suất Thống kê](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_13_kiem_dinh_nhieu_mau_va_anova.md).
> Chỉ thí nghiệm mới cho phép kết luận nhân quả; dữ liệu quan sát thì không.

### 💼 Làm sao để cầu BỚT co giãn — bảng hành động

Nếu đo ra $e > 1$, tăng giá sẽ mất doanh thu. Nhưng độ co giãn **không phải hằng số của tự nhiên** —
nó do bốn yếu tố ở mục 2 quyết định, và bạn tác động được vào cả bốn:

| Yếu tố                | Đòn bẩy làm cầu **bớt** co giãn                                               | Học kỹ ở |
| --------------------- | ----------------------------------------------------------------------------- | -------- |
| Hàng thay thế         | khác biệt hoá sản phẩm, xây thương hiệu, tạo chi phí chuyển đổi               | bài 8    |
| Thiết yếu ↔ xa xỉ     | định vị sản phẩm thành *"thứ không thể thiếu"* của một công việc cụ thể       | bài 8    |
| Định nghĩa thị trường | chuyển từ "một loại hàng" sang "giải pháp trọn gói"                           | bài 8    |
| Thời gian             | hợp đồng dài hạn, gói thuê bao — **khoá khách trước khi họ kịp tìm thay thế** | bài 7    |

⭐ Nói ngắn: **giảm giá là cách cạnh tranh của người có $e$ lớn.** Việc của quản trị là làm cho $e$
nhỏ đi, chứ không phải chạy đua trong một thị trường $e$ lớn.
---

## 16. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-03-do-co-gian.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-03-do-co-gian.py](../thuc_hanh/bai-03-do-co-gian.py).

Chín phép tính. Điểm đáng chú ý nhất: **mục 4 tái tạo lại nguyên vẹn Bảng của Hình 4 (tr. 110)** từ
một dòng công thức $Q = 14 - 2P$ — cả bảy giá trị độ co giãn 13,0 · 3,7 · 1,8 · 1,0 · 0,6 · 0,3 · 0,1
đều khớp bản in. Và **mục 9 đo độ co giãn bằng hồi quy log–log**, nối thẳng sang môn Xác suất Thống kê.

```python
"""Bai 3 — Do co gian va ung dung (Mankiw, chuong 5).
Chay: python3 bai-03-do-co-gian.py   (Python 3.10+, khong can cai goi nao)

Tien dung SO NGUYEN (xu / do la) o moi cho co the. Ket qua tat dinh.
"""

import math
from statistics import fmean

# ══ 1. VI SAO CAN PHUONG PHAP TRUNG DIEM — tr. 106 ══════════════════════════
# Diem A: gia 4 do la, luong 120.   Diem B: gia 6 do la, luong 80.
A = (4, 120)
B = (6, 80)

def pt_thuong(cu, moi):
    """Phan tram thay doi kieu thong thuong: chia cho GIA TRI BAN DAU."""
    return (moi - cu) / cu * 100

def pt_trung_diem(cu, moi):
    """Phan tram thay doi kieu TRUNG DIEM: chia cho TRUNG BINH hai gia tri."""
    return (moi - cu) / ((cu + moi) / 2) * 100

print("1. VI SAO CAN PHUONG PHAP TRUNG DIEM — tr. 106")
print(f"   Diem A: gia ${A[0]}, luong {A[1]}      Diem B: gia ${B[0]}, luong {B[1]}")
print()
print("   CACH THONG THUONG (chia cho gia tri ban dau):")
for ten, (p1, q1), (p2, q2) in [("A -> B", A, B), ("B -> A", B, A)]:
    dp, dq = pt_thuong(p1, p2), pt_thuong(q1, q2)
    print(f"      {ten}: gia {dp:+6.1f}%   luong {dq:+6.1f}%   do co gian = {abs(dq / dp):.2f}")
print("      ⚠ HAI CHIEU RA HAI KET QUA KHAC NHAU — day la van de.")
print("        (sach: 0,66 va 1,5 — tr. 106)")
print()
print("   PHUONG PHAP TRUNG DIEM (chia cho trung binh):")
for ten, (p1, q1), (p2, q2) in [("A -> B", A, B), ("B -> A", B, A)]:
    dp, dq = pt_trung_diem(p1, p2), pt_trung_diem(q1, q2)
    print(f"      {ten}: gia {dp:+6.1f}%   luong {dq:+6.1f}%   do co gian = {abs(dq / dp):.2f}")
print("      ✓ HAI CHIEU RA CUNG MOT SO. Do la ly do dung trung diem.")
print()

def co_gian(p1, q1, p2, q2):
    """Do co gian cua cau theo gia, phuong phap trung diem, lay tri tuyet doi."""
    return abs(pt_trung_diem(q1, q2) / pt_trung_diem(p1, p2))

# ══ 2. NAM DANG DUONG CAU — Hinh 1, tr. 107 ═════════════════════════════════
print("2. NAM DANG DUONG CAU — Hinh 1, tr. 107   (gia $4 -> $5 o ca nam truong hop)")
print("   truong hop                        luong        %luong    do co gian")
nam_dang = [
    ("(a) hoan toan KHONG co gian", 100, 100),
    ("(b) khong co gian",           100,  90),
    ("(c) co gian DON VI",          100,  80),
    ("(d) co gian",                 100,  50),
]
for ten, q1, q2 in nam_dang:
    dq = pt_trung_diem(q1, q2)
    e = co_gian(4, q1, 5, q2)
    print(f"   {ten:<32} {q1} -> {q2:>3}   {dq:>6.0f}%   {e:>8.2f}")
print(f"   {'(e) hoan toan CO GIAN':<32} {'100 -> bat ky':>10}   {'':>6}   {'vo cung':>8}")
print("   (sach: gia tang 22%; luong giam 0%, 11%, 22%, 67% — tr. 107)")
print("   💡 Meo nho cua sach (tr. 108): duong cau KHONG co gian (Inelastic)")
print("      dung thang nhu chu I.")
print()

# ══ 3. DO CO GIAN TREN THUC TE — hop 'Ban co biet', tr. 108 ════════════════
print("3. DO CO GIAN CUA CAU THEO GIA — SO LIEU THUC TE (tr. 108)")
thuc_te = [("Trung", 0.1), ("Cham soc y te", 0.2), ("Gao", 0.5), ("Nha o", 0.7),
           ("Thit bo", 1.6), ("Bua an tai nha hang", 2.3), ("Nuoc giai khat Mountain Dew", 4.4)]
for ten, e in thuc_te:
    loai = "khong co gian" if e < 1 else "co gian"
    thanh = "█" * round(e * 6)
    print(f"   {ten:<30} {e:>4.1f}  {loai:<14} {thanh}")
print("   ⟹ cang DINH NGHIA HEP thi cang CO GIAN: 'nuoc giai khat' < 'Mountain Dew'")
print("   ⟹ cang THIET YEU thi cang KHONG co gian: trung, y te, gao")
print()

# ══ 4. TAI TAO BANG HINH 4 — duong cau tuyen tinh, tr. 110 ══════════════════
# Doc tu do thi Hinh 4: gia $7 -> luong 0,  moi 1 do la giam gia thi luong +2
#   =>  Q = 14 - 2P
def Q(P):
    return 14 - 2 * P

print("4. DO CO GIAN DOC THEO MOT DUONG CAU TUYEN TINH — Hinh 4, tr. 110")
print("   duong cau Q = 14 - 2P  (do doc KHONG DOI, nhung do co gian THI DOI)")
print()
print("   gia  luong   doanh thu   %gia   %luong   do co gian   mo ta")
gia = list(range(7, -1, -1))
for i, P in enumerate(gia):
    q, tr = Q(P), P * Q(P)
    if i + 1 < len(gia):
        P2 = gia[i + 1]
        dp = abs(pt_trung_diem(P, P2))
        dq = abs(pt_trung_diem(q, Q(P2)))
        e = dq / dp
        mo_ta = "co gian" if e > 1.02 else ("co gian don vi" if e > 0.98 else "khong co gian")
        print(f"   ${P}   {q:>4}   {tr:>8}   {dp:>5.0f}   {dq:>6.0f}   {e:>10.1f}   {mo_ta}")
    else:
        print(f"   ${P}   {q:>4}   {tr:>8}")
print("   (sach in: 13,0 · 3,7 · 1,8 · 1,0 · 0,6 · 0,3 · 0,1 — khop tung dong)")
print()
print("   ⭐ BA QUY TAC (tr. 110):")
print("      cau KHONG co gian (e < 1): gia va doanh thu DI CUNG HUONG")
print("      cau CO GIAN      (e > 1): gia va doanh thu DI NGUOC HUONG")
print("      cau co gian DON VI (e = 1): doanh thu KHONG DOI")
print()

# ══ 5. VE DUONG DOANH THU THEO GIA ══════════════════════════════════════════
print("5. DOANH THU THEO GIA — DINH NAM DUNG CHO CO GIAN = 1")
CAO, RONG = 13, 44
tr_max = 25
luoi = [[" "] * RONG for _ in range(CAO)]
for i in range(RONG):
    P = 7 * i / (RONG - 1)
    tr = P * (14 - 2 * P)
    r = CAO - 1 - round(tr / tr_max * (CAO - 1))
    luoi[r][i] = "●"
    for rr in range(r + 1, CAO):
        if luoi[rr][i] == " ":
            luoi[rr][i] = "·"
print("      doanh thu")
for i, hang in enumerate(luoi):
    v = tr_max - round(i * tr_max / (CAO - 1))
    nhan = f"{v:>4}" if i % 3 == 0 else "    "
    print(f"      {nhan} │{''.join(hang)}".rstrip())
print("           └" + "─" * RONG)
print("            $0" + " " * (RONG - 6) + "  $7  gia")
cot_dinh = round(3.5 / 7 * (RONG - 1))
print(" " * 12 + "|" + "-" * (cot_dinh - 1) + "^" + "-" * (RONG - cot_dinh - 2) + "|")
print(" " * 12 + "  KHONG co gian".ljust(cot_dinh) + "  CO GIAN")
print(" " * 12 + "  gia thap, luong cao".ljust(cot_dinh) + "  gia cao, luong thap")
print("      ⭐ TANG gia o nua TRAI  -> doanh thu TANG")
print("        TANG gia o nua PHAI  -> doanh thu GIAM")
print(f"      dinh o P = $3,50 (e = 1), doanh thu {3.5 * (14 - 2 * 3.5):.1f}")
print()

# ══ 6. DO CO GIAN CUA CUNG — vi du sua, tr. 113 ═════════════════════════════
# Tien tinh bang XU de khong dung so thuc
print("6. DO CO GIAN CUA CUNG THEO GIA — vi du sua, tr. 113")
gia_cu, gia_moi = 285, 315          # xu / gallon
sl_cu, sl_moi = 9000, 11000         # lit / thang
dp = pt_trung_diem(gia_cu, gia_moi)
dq = pt_trung_diem(sl_cu, sl_moi)
print(f"   gia ${gia_cu / 100:.2f} -> ${gia_moi / 100:.2f}   =>  {dp:.0f}% (trung diem la ${(gia_cu + gia_moi) / 200:.2f})")
print(f"   luong {sl_cu:,} -> {sl_moi:,} lit  =>  {dq:.0f}% (trung diem la {(sl_cu + sl_moi) // 2:,})")
print(f"   do co gian cua cung = {dq:.0f}% / {dp:.0f}% = {dq / dp:.1f}   (sach: 2,0)")
print("   ⭐ Yeu to quyet dinh lon nhat: THOI GIAN. Cung DAI HAN co gian hon NGAN HAN.")
print()

# ══ 7. UNG DUNG 1 — TIN TOT CHO NONG NGHIEP, TIN XAU CHO NONG DAN (tr. 116) ═
print("7. UNG DUNG 1 — GIONG LUA MOI LAM NONG DAN NGHEO DI  (Hinh 7, tr. 116)")
truoc = (3, 100)      # gia 3 do la, luong 100
sau   = (2, 110)      # cung dich phai: gia 2 do la, luong 110
for ten, (p, q) in [("truoc khi co giong moi", truoc), ("sau khi co giong moi ", sau)]:
    print(f"   {ten}: P = ${p}, Q = {q}  ->  tong doanh thu = ${p * q}")
e_cau = co_gian(truoc[0], truoc[1], sau[0], sau[1])
print(f"   do co gian cua cau = {e_cau:.2f}  ->  KHONG CO GIAN (< 1)")
print(f"   doanh thu ${truoc[0] * truoc[1]} -> ${sau[0] * sau[1]}, GIAM ${truoc[0] * truoc[1] - sau[0] * sau[1]}")
print("   ⚠ Nghich ly: nang suat TANG 20% ma thu nhap nong dan GIAM.")
print("      Vi cau luong thuc KHONG CO GIAN: gia giam manh, luong chi tang nhe.")
print("   ⚠ Nhung tung nong dan RIENG LE van phai dung giong moi — ho la nguoi")
print("      CHAP NHAN GIA, bo giong moi thi chi thiet mot minh. Ca nganh cung lam")
print("      thi tat ca cung thiet. (Day la tinh the se co ten o bai 9: TIEN THOAI LUONG NAN.)")
print()
print("   So lieu lich su Hoa Ky (tr. 117):")
print(f"      {'nam 1950':<12} 10 trieu nong dan = 17% luc luong lao dong")
print(f"      {'ngay nay':<12} duoi 3 trieu      =  2% luc luong lao dong")
print("      -> so nong dan giam 70%, san luong lai CAO GAP DOI nam 1950")
print()

# ══ 8. UNG DUNG 3 — CAM MA TUY vs GIAO DUC (Hinh 9, tr. 121) ════════════════
# Sach chi ve do thi, khong cho so. Day la so ta tu dat de thay co che.
print("8. UNG DUNG 3 — CAM MA TUY vs GIAO DUC  (Hinh 9, tr. 121)")
print("   (sach chi ve do thi; so duoi day do ta tu dat de thay co che)")
print("   cau RAT DOC (khong co gian):  Qd = 150 - P/2      cung:  Qs = 2P - 60")
def can_bang(dich_cau=0, dich_cung=0):
    # 150 - P/2 + dc = 2P - 60 + ds  ->  5P/2 = 210 + dc - ds
    P = (210 + dich_cau - dich_cung) * 2 // 5
    return P, 150 - P // 2 + dich_cau

P0, Q0 = can_bang()
chi0 = P0 * Q0
e0 = 0.5 * P0 / Q0
print(f"   ban dau                   : P = {P0:>3}, Q = {Q0:>3}  ->  tong chi = {chi0:>5}")
print(f"      do co gian cua cau tai diem nay = 0,5 x {P0}/{Q0} = {e0:.2f}  ->  KHONG CO GIAN")
for ten, dc, ds, ghi in [
        ("(a) CAM      -> cung giam", 0, -30, "gia TANG manh, luong giam it"),
        ("(b) GIAO DUC -> cau giam", -30, 0, "gia GIAM,      luong giam")]:
    P, q = can_bang(dc, ds)
    chi = P * q
    print(f"   {ten:<26}: P = {P:>3}, Q = {q:>3}  ->  tong chi = {chi:>5}   ({ghi})")
    print(f"      tong tien nguoi nghien phai bo ra: {chi0} -> {chi}  "
          f"({'TANG' if chi > chi0 else 'GIAM'} {abs(chi - chi0)})")
print("   ⟹ Ca hai deu GIAM luong ma tuy tieu thu. Nhung TONG SO TIEN CHI thi NGUOC NHAU.")
print("      Neu toi pham (trom cap de co tien mua) ty le voi tong so tien chi, thi")
print("      CAM lam toi pham TANG, con GIAO DUC lam toi pham GIAM.")
print("   ⚠ Sach ghi phan bien: trong DAI HAN cau ma tuy co gian hon (gia cao han che")
print("      gioi tre thu), nen cam co the giam toi pham ve lau dai. Ket luan phu thuoc")
print("      DO CO GIAN — mot con so, khong phai mot quan diem chinh tri.")
print()

# ══ 9. 💼 GOC QTKD — DO LAI DO CO GIAN TU DU LIEU BAN HANG THAT ═════════════
print("9. 💼 GOC QTKD — UOC LUONG DO CO GIAN BANG HOI QUY log-log")
print("   Sach dung o 'do co gian la gi'. Day la cach DO no tu du lieu ban hang.")
print()
# 12 thang thay doi gia, ghi lai luong ban. Gia: nghin dong. Luong: ly/thang.
du_lieu = [(35, 9100), (35, 9000), (38, 8300), (38, 8500), (40, 7900), (40, 8100),
           (42, 7500), (45, 6900), (45, 7100), (48, 6300), (50, 6100), (50, 5900)]
print("   gia (nghin)  luong ban/thang")
for g, l in du_lieu:
    print(f"   {g:>8}     {l:>10,}")

# Hoi quy ln(Q) theo ln(P): he so goc = -do co gian  (bai 14 mon Xac suat Thong ke)
xs = [math.log(g) for g, _ in du_lieu]
ys = [math.log(l) for _, l in du_lieu]
mx, my = fmean(xs), fmean(ys)
Sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
Sxx = sum((x - mx) ** 2 for x in xs)
Syy = sum((y - my) ** 2 for y in ys)
he_so_goc = Sxy / Sxx
r = Sxy / math.sqrt(Sxx * Syy)
print()
print(f"   hoi quy ln(Q) = a + b.ln(P)   ->  b = {he_so_goc:.4f}")
print(f"   ⭐ DO CO GIAN = |b| = {abs(he_so_goc):.2f}   (R^2 = {r * r:.4f})")
print(f"   {abs(he_so_goc):.2f} > 1  =>  cau CO GIAN  =>  TANG gia lam doanh thu GIAM")
print()
print("   Kiem lai bang phuong phap trung diem tren hai diem dau va cuoi:")
e_hai_diem = co_gian(du_lieu[0][0], du_lieu[0][1], du_lieu[-1][0], du_lieu[-1][1])
print(f"      ({du_lieu[0][0]}k, {du_lieu[0][1]:,}) -> ({du_lieu[-1][0]}k, {du_lieu[-1][1]:,})"
      f"  ->  do co gian = {e_hai_diem:.2f}")
print(f"      hai cach cho ket qua gan nhau: {abs(he_so_goc):.2f} va {e_hai_diem:.2f}")
print("      ⭐ Hoi quy dung CA 12 diem nen ben hon; trung diem chi dung 2 diem.")
print()
print("   QUYET DINH GIA — doanh thu du bao theo mo hinh Q = exp(a) . P^b:")
a = my - he_so_goc * mx
for gia_thu in (35, 40, 45, 50, 55):
    q_du_bao = math.exp(a) * gia_thu ** he_so_goc
    print(f"      gia {gia_thu}k  ->  luong {q_du_bao:>7,.0f} ly  ->  doanh thu {gia_thu * q_du_bao:>10,.0f} nghin")
print("   => do co gian > 1 nen doanh thu GIAM deu khi tang gia. Muon tang gia ma khong")
print("      mat doanh thu thi phai LAM CAU BOT CO GIAN truoc: khac biet hoa san pham,")
print("      giam so hang thay the gan gui (bai 8, chuong 16).")
print()
print("   ⚠ BA CANH BAO khi uoc luong do co gian tu du lieu quan sat:")
print("      1. BO SOT BIEN — thang giam gia cung la thang chay quang cao?  (bai 1 muc 15)")
print("      2. NHAN QUA NGUOC — ta giam gia VI thay ban cham, chu khong nguoc lai?")
print("      3. Du lieu chi phu vung gia 35-50k. Ngoai vung do la NGOAI SUY, khong tin duoc.")
print("      Cach chac chan nhat van la A/B TEST co doi chung — bai 12-13 mon Xac suat Thong ke.")
```

**Kết quả chạy thật:**

```
1. VI SAO CAN PHUONG PHAP TRUNG DIEM — tr. 106
   Diem A: gia $4, luong 120      Diem B: gia $6, luong 80

   CACH THONG THUONG (chia cho gia tri ban dau):
      A -> B: gia  +50.0%   luong  -33.3%   do co gian = 0.67
      B -> A: gia  -33.3%   luong  +50.0%   do co gian = 1.50
      ⚠ HAI CHIEU RA HAI KET QUA KHAC NHAU — day la van de.
        (sach: 0,66 va 1,5 — tr. 106)

   PHUONG PHAP TRUNG DIEM (chia cho trung binh):
      A -> B: gia  +40.0%   luong  -40.0%   do co gian = 1.00
      B -> A: gia  -40.0%   luong  +40.0%   do co gian = 1.00
      ✓ HAI CHIEU RA CUNG MOT SO. Do la ly do dung trung diem.

2. NAM DANG DUONG CAU — Hinh 1, tr. 107   (gia $4 -> $5 o ca nam truong hop)
   truong hop                        luong        %luong    do co gian
   (a) hoan toan KHONG co gian      100 -> 100        0%       0.00
   (b) khong co gian                100 ->  90      -11%       0.47
   (c) co gian DON VI               100 ->  80      -22%       1.00
   (d) co gian                      100 ->  50      -67%       3.00
   (e) hoan toan CO GIAN            100 -> bat ky             vo cung
   (sach: gia tang 22%; luong giam 0%, 11%, 22%, 67% — tr. 107)
   💡 Meo nho cua sach (tr. 108): duong cau KHONG co gian (Inelastic)
      dung thang nhu chu I.

3. DO CO GIAN CUA CAU THEO GIA — SO LIEU THUC TE (tr. 108)
   Trung                           0.1  khong co gian  █
   Cham soc y te                   0.2  khong co gian  █
   Gao                             0.5  khong co gian  ███
   Nha o                           0.7  khong co gian  ████
   Thit bo                         1.6  co gian        ██████████
   Bua an tai nha hang             2.3  co gian        ██████████████
   Nuoc giai khat Mountain Dew     4.4  co gian        ██████████████████████████
   ⟹ cang DINH NGHIA HEP thi cang CO GIAN: 'nuoc giai khat' < 'Mountain Dew'
   ⟹ cang THIET YEU thi cang KHONG co gian: trung, y te, gao

4. DO CO GIAN DOC THEO MOT DUONG CAU TUYEN TINH — Hinh 4, tr. 110
   duong cau Q = 14 - 2P  (do doc KHONG DOI, nhung do co gian THI DOI)

   gia  luong   doanh thu   %gia   %luong   do co gian   mo ta
   $7      0          0      15      200         13.0   co gian
   $6      2         12      18       67          3.7   co gian
   $5      4         20      22       40          1.8   co gian
   $4      6         24      29       29          1.0   co gian don vi
   $3      8         24      40       22          0.6   khong co gian
   $2     10         20      67       18          0.3   khong co gian
   $1     12         12     200       15          0.1   khong co gian
   $0     14          0
   (sach in: 13,0 · 3,7 · 1,8 · 1,0 · 0,6 · 0,3 · 0,1 — khop tung dong)

   ⭐ BA QUY TAC (tr. 110):
      cau KHONG co gian (e < 1): gia va doanh thu DI CUNG HUONG
      cau CO GIAN      (e > 1): gia va doanh thu DI NGUOC HUONG
      cau co gian DON VI (e = 1): doanh thu KHONG DOI

5. DOANH THU THEO GIA — DINH NAM DUNG CHO CO GIAN = 1
      doanh thu
        25 │                   ●●●●●●
           │               ●●●●······●●●●
           │             ●●··············●●
        19 │           ●●··················●●
           │         ●●······················●●
           │        ●··························●
        13 │      ●●····························●●
           │     ●································●
           │    ●··································●
         6 │   ●····································●
           │  ●······································●
           │ ●········································●
         0 │●··········································●
           └────────────────────────────────────────────
            $0                                        $7  gia
            |---------------------^--------------------|
              KHONG co gian         CO GIAN
              gia thap, luong cao   gia cao, luong thap
      ⭐ TANG gia o nua TRAI  -> doanh thu TANG
        TANG gia o nua PHAI  -> doanh thu GIAM
      dinh o P = $3,50 (e = 1), doanh thu 24.5

6. DO CO GIAN CUA CUNG THEO GIA — vi du sua, tr. 113
   gia $2.85 -> $3.15   =>  10% (trung diem la $3.00)
   luong 9,000 -> 11,000 lit  =>  20% (trung diem la 10,000)
   do co gian cua cung = 20% / 10% = 2.0   (sach: 2,0)
   ⭐ Yeu to quyet dinh lon nhat: THOI GIAN. Cung DAI HAN co gian hon NGAN HAN.

7. UNG DUNG 1 — GIONG LUA MOI LAM NONG DAN NGHEO DI  (Hinh 7, tr. 116)
   truoc khi co giong moi: P = $3, Q = 100  ->  tong doanh thu = $300
   sau khi co giong moi : P = $2, Q = 110  ->  tong doanh thu = $220
   do co gian cua cau = 0.24  ->  KHONG CO GIAN (< 1)
   doanh thu $300 -> $220, GIAM $80
   ⚠ Nghich ly: nang suat TANG 20% ma thu nhap nong dan GIAM.
      Vi cau luong thuc KHONG CO GIAN: gia giam manh, luong chi tang nhe.
   ⚠ Nhung tung nong dan RIENG LE van phai dung giong moi — ho la nguoi
      CHAP NHAN GIA, bo giong moi thi chi thiet mot minh. Ca nganh cung lam
      thi tat ca cung thiet. (Day la tinh the se co ten o bai 9: TIEN THOAI LUONG NAN.)

   So lieu lich su Hoa Ky (tr. 117):
      nam 1950     10 trieu nong dan = 17% luc luong lao dong
      ngay nay     duoi 3 trieu      =  2% luc luong lao dong
      -> so nong dan giam 70%, san luong lai CAO GAP DOI nam 1950

8. UNG DUNG 3 — CAM MA TUY vs GIAO DUC  (Hinh 9, tr. 121)
   (sach chi ve do thi; so duoi day do ta tu dat de thay co che)
   cau RAT DOC (khong co gian):  Qd = 150 - P/2      cung:  Qs = 2P - 60
   ban dau                   : P =  84, Q = 108  ->  tong chi =  9072
      do co gian cua cau tai diem nay = 0,5 x 84/108 = 0.39  ->  KHONG CO GIAN
   (a) CAM      -> cung giam : P =  96, Q = 102  ->  tong chi =  9792   (gia TANG manh, luong giam it)
      tong tien nguoi nghien phai bo ra: 9072 -> 9792  (TANG 720)
   (b) GIAO DUC -> cau giam  : P =  72, Q =  84  ->  tong chi =  6048   (gia GIAM,      luong giam)
      tong tien nguoi nghien phai bo ra: 9072 -> 6048  (GIAM 3024)
   ⟹ Ca hai deu GIAM luong ma tuy tieu thu. Nhung TONG SO TIEN CHI thi NGUOC NHAU.
      Neu toi pham (trom cap de co tien mua) ty le voi tong so tien chi, thi
      CAM lam toi pham TANG, con GIAO DUC lam toi pham GIAM.
   ⚠ Sach ghi phan bien: trong DAI HAN cau ma tuy co gian hon (gia cao han che
      gioi tre thu), nen cam co the giam toi pham ve lau dai. Ket luan phu thuoc
      DO CO GIAN — mot con so, khong phai mot quan diem chinh tri.

9. 💼 GOC QTKD — UOC LUONG DO CO GIAN BANG HOI QUY log-log
   Sach dung o 'do co gian la gi'. Day la cach DO no tu du lieu ban hang.

   gia (nghin)  luong ban/thang
         35          9,100
         35          9,000
         38          8,300
         38          8,500
         40          7,900
         40          8,100
         42          7,500
         45          6,900
         45          7,100
         48          6,300
         50          6,100
         50          5,900

   hoi quy ln(Q) = a + b.ln(P)   ->  b = -1.1615
   ⭐ DO CO GIAN = |b| = 1.16   (R^2 = 0.9842)
   1.16 > 1  =>  cau CO GIAN  =>  TANG gia lam doanh thu GIAM

   Kiem lai bang phuong phap trung diem tren hai diem dau va cuoi:
      (35k, 9,100) -> (50k, 5,900)  ->  do co gian = 1.21
      hai cach cho ket qua gan nhau: 1.16 va 1.21
      ⭐ Hoi quy dung CA 12 diem nen ben hon; trung diem chi dung 2 diem.

   QUYET DINH GIA — doanh thu du bao theo mo hinh Q = exp(a) . P^b:
      gia 35k  ->  luong   9,210 ly  ->  doanh thu    322,340 nghin
      gia 40k  ->  luong   7,887 ly  ->  doanh thu    315,462 nghin
      gia 45k  ->  luong   6,878 ly  ->  doanh thu    309,518 nghin
      gia 50k  ->  luong   6,086 ly  ->  doanh thu    304,296 nghin
      gia 55k  ->  luong   5,448 ly  ->  doanh thu    299,648 nghin
   => do co gian > 1 nen doanh thu GIAM deu khi tang gia. Muon tang gia ma khong
      mat doanh thu thi phai LAM CAU BOT CO GIAN truoc: khac biet hoa san pham,
      giam so hang thay the gan gui (bai 8, chuong 16).

   ⚠ BA CANH BAO khi uoc luong do co gian tu du lieu quan sat:
      1. BO SOT BIEN — thang giam gia cung la thang chay quang cao?  (bai 1 muc 15)
      2. NHAN QUA NGUOC — ta giam gia VI thay ban cham, chu khong nguoc lai?
      3. Du lieu chi phu vung gia 35-50k. Ngoai vung do la NGOAI SUY, khong tin duoc.
      Cach chac chan nhat van la A/B TEST co doi chung — bai 12-13 mon Xac suat Thong ke.
```

### Đọc kết quả

**① Vì sao cần trung điểm (mục 1).** Cách thường: **0,67** và **1,50** — cùng hai điểm, hai đáp án.
Trung điểm: **1,00** và **1,00**. Bất đối xứng biến mất. (Sách in 0,66; chênh do làm tròn 33,3% → 33%.)

**② Năm dạng đường cầu (mục 2).** Cùng cú tăng giá 22%, lượng phản ứng 0% → 11% → 22% → 67%, cho
$e$ = 0 → 0,47 → 1,00 → 3,00. Chỉ có **một** con số đổi ở đầu vào (lượng cầu mới), mà kết luận kinh
doanh đảo ngược hoàn toàn.

**③ Số liệu thực tế (mục 3).** Biểu đồ thanh cho thấy khoảng cách thật giữa trứng (0,1) và Mountain
Dew (4,4) — **gấp 44 lần**. Cùng một cú tăng giá 10% sẽ làm mất 1% khách của một bên và 44% của bên kia.

**④ Bảng Hình 4 (mục 4).** Bảy dòng độ co giãn khớp **từng con số** với bản in tr. 110. Chú ý cột
doanh thu: `0 → 12 → 20 → 24 → 24 → 20 → 12 → 0`. Nó **tăng rồi giảm**, và **đỉnh phẳng ở hai dòng
$4 và $3** — đúng chỗ $e$ đi qua 1.

**⑤ Đường doanh thu (mục 5).** Cùng thông tin, vẽ ra thành hình. Nửa **trái** (giá thấp) là vùng
**không co giãn** → tăng giá thì doanh thu tăng. Nửa **phải** là vùng **co giãn** → tăng giá thì
doanh thu giảm. Đỉnh ở $\$3{,}50$, đúng nơi $e = 1$.

**⑥ Độ co giãn của cung (mục 6).** 20% / 10% = **2,0**, khớp tr. 113.

**⑦ Nông dân (mục 7).** $3 \times 100 = 300 \to 2 \times 110 = 220$. Độ co giãn của cầu đo được
là **0,24** — rất không co giãn, nên giá rơi mạnh hơn nhiều so với mức lượng tăng. Nông dân **mất 80
đô la** vì năng suất tăng.

**⑧ Ma tuý (mục 8).** Đây là mục đáng chạy nhất. Cùng một mục tiêu *"giảm sử dụng ma tuý"*, hai chính
sách cho **hai hướng ngược nhau** ở tổng chi tiêu:

| Chính sách                  |      Giá | Lượng |    Tổng chi |
| --------------------------- | -------: | ----: | ----------: |
| ban đầu                     |       84 |   108 |       9.072 |
| **(a) cấm** — cung giảm     | **96** ↑ | 102 ↓ | **9.792** ↑ |
| **(b) giáo dục** — cầu giảm | **72** ↓ |  84 ↓ | **6.048** ↓ |

Độ co giãn của cầu tại điểm cân bằng là **0,39** — chính vì nó nhỏ hơn 1 mà cấm đoán đẩy tổng chi
**lên**. Nếu cầu co giãn, kết luận sẽ ngược lại.

**⑨ Hồi quy log–log (mục 9).** Trên 12 tháng dữ liệu: $b = -1{,}1615$ → **độ co giãn = 1,16**, với
$R^2 = 0{,}98$. Phương pháp trung điểm trên hai điểm đầu–cuối cho **1,21** — gần nhưng không bằng,
vì nó chỉ dùng 2 trong 12 điểm. Bảng dự báo cuối cho thấy doanh thu **giảm đều** khi tăng giá, đúng
như $e > 1$ báo trước.

---

## 17. Tự thử

Sửa tham số rồi chạy lại. Không có lời giải kèm theo.

1. Trong mục 1, đổi điểm B thành `(6, 40)` (lượng rơi mạnh hơn nhiều). Hai cách tính lệch nhau bao
   nhiêu? Độ lệch giữa hai phương pháp lớn lên hay nhỏ đi khi hai điểm **cách xa nhau** hơn?
2. Trong mục 4, đổi đường cầu thành `14 - 4 * P` (dốc hơn — nhớ sửa cả `Q(P)` lẫn phạm vi giá). Doanh
   thu đạt đỉnh ở mức giá nào? Có phải luôn ở **giữa** khoảng giá không?
3. Trong mục 7, đổi `sau = (2, 110)` thành `sau = (2, 160)` (cầu co giãn hơn nhiều). Bây giờ giống
   lúa mới làm nông dân **giàu lên hay nghèo đi**? Ngưỡng nào của độ co giãn làm kết luận đảo chiều?
4. Trong mục 8, đổi đường cầu thành `Qd = 200 - 2P` (co giãn hơn) — sửa cả hàm `can_bang`. Chính sách
   **cấm** bây giờ làm tổng chi tiêu tăng hay giảm? Bạn vừa tìm ra điều kiện để lập luận của sách đúng.
5. Trong mục 9, thêm vào `du_lieu` một điểm bất thường `(30, 3000)` (một tháng giảm giá mạnh mà bán
   được ít — ví dụ vì đóng cửa sửa chữa). Độ co giãn ước lượng đổi bao nhiêu? $R^2$ đổi thế nào?
   Vì sao một điểm duy nhất lại làm được vậy, và điều đó nói gì về việc **làm sạch dữ liệu trước khi
   hồi quy**?

---

## 18. Từ điển thuật ngữ

Cột tiếng Anh lấy từ mục **Khái niệm then chốt** của sách (tr. 122–123).

| Tiếng Việt                       | Tiếng Anh                        | Ghi chú                                                   |
| -------------------------------- | -------------------------------- | --------------------------------------------------------- |
| Độ co giãn                       | Elasticity                       | tr. 104 — đo **mức độ**, không chỉ xu hướng               |
| Độ co giãn của cầu theo giá      | Price elasticity of demand       | tr. 104                                                   |
| Phương pháp trung điểm           | Midpoint method                  | tr. 106 — chia cho **trung bình**, không phải giá trị đầu |
| Hoàn toàn không co giãn          | Perfectly inelastic              | $e = 0$, đường thẳng đứng                                 |
| Không co giãn                    | Inelastic                        | $e < 1$ — mẹo nhớ: giống chữ **I**                        |
| Co giãn đơn vị                   | Unit elastic                     | $e = 1$                                                   |
| Co giãn                          | Elastic                          | $e > 1$                                                   |
| Hoàn toàn co giãn                | Perfectly elastic                | $e \to \infty$, đường nằm ngang                           |
| Tổng doanh thu                   | Total revenue                    | tr. 108 — $P \times Q$                                    |
| Độ co giãn của cầu theo thu nhập | Income elasticity of demand      | tr. 111 — dấu **âm** = hàng thứ cấp                       |
| Độ co giãn của cầu theo giá chéo | Cross-price elasticity of demand | tr. 112 — dấu **dương** = hàng thay thế                   |
| Độ co giãn của cung theo giá     | Price elasticity of supply       | tr. 112                                                   |

⚠️ **Đính chính — Hình 3, tr. 109.** Hình có hai khung con, nhưng **cả hai đều được đánh nhãn "(a)"**:
"(a) Trường hợp cầu không co giãn" và "(a) Trường hợp cầu co giãn". Khung bên phải phải là **"(b)"** —
chính phần chú thích của hình và đoạn văn ở tr. 110 đều gọi nó là *"Hình 3(b)"*. Đã đối chiếu bản
quét 300 dpi. Lỗi sắp chữ, không đổi nội dung.

---

## 19. Câu hỏi tự kiểm tra

1. Vì sao phương pháp thông thường cho hai kết quả khác nhau khi đi từ A sang B và từ B về A? Phương
   pháp trung điểm sửa chỗ nào?
2. Sắp xếp theo thứ tự độ co giãn **tăng dần** và giải thích: *nước giải khát nói chung* — *Pepsi* —
   *đồ uống*. Quy tắc nào ở mục 2 đang được dùng?
3. Cầu về insulin với người bệnh tiểu đường co giãn hay không co giãn? Nếu nhà sản xuất tăng giá 20%,
   doanh thu của họ tăng hay giảm?
4. Một quán ăn giảm giá 15% và doanh thu **tăng**. Độ co giãn của cầu lớn hơn hay nhỏ hơn 1? Nếu giảm
   tiếp 15% nữa, doanh thu có chắc chắn tiếp tục tăng không? (Xem lại mục 8 trước khi trả lời.)
5. Trên đường cầu thẳng ở Hình 4, vì sao độ dốc không đổi mà độ co giãn lại đổi? Vùng nào của đường
   cầu là vùng co giãn?
6. Độ co giãn của cầu theo thu nhập của một hàng hoá bằng **−0,4**. Đó là hàng gì? Doanh số của nó sẽ
   thế nào khi nền kinh tế suy thoái?
7. Độ co giãn theo giá chéo giữa sản phẩm của bạn và sản phẩm X bằng **+2,1**; với sản phẩm Y bằng
   **−0,8**. X và Y là gì đối với bạn? Với mỗi cái, bạn nên làm gì khác đi?
8. Vì sao cung co giãn hơn trong dài hạn? Nêu **hai** cơ chế khác nhau mà sách đưa ra.
9. Giống lúa mì mới làm tăng năng suất 20% nhưng làm nông dân nghèo đi. Điều kiện nào về độ co giãn
   khiến chuyện đó xảy ra? Nếu từng nông dân biết trước điều này, họ có nên từ chối dùng giống mới không?
10. Chính sách cấm ma tuý làm tổng chi tiêu cho ma tuý **tăng**. Hãy chỉ ra chính xác **giả định về độ
    co giãn** nào đang chống đỡ kết luận đó, và nêu điều kiện khiến kết luận đảo chiều.

---

## Tóm tắt một trang

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  BÀI 3 — ĐỘ CO GIÃN VÀ ĐỊNH GIÁ                 (Ch. 5, tr. 103–126)      ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  Ch.4 nói XU HƯỚNG (giá lên, lượng xuống)                                 ║
║  Ch.5 nói MỨC ĐỘ    ⟹ một CON SỐ dùng được để định giá                   ║
║                                                                           ║
║  ── CÔNG THỨC ──────────────────────────────────────────────────────      ║
║      e = %Δ lượng cầu / %Δ giá        (bỏ dấu trừ, lấy trị tuyệt đối)     ║
║  ⚠ PHƯƠNG PHÁP TRUNG ĐIỂM: chia cho TRUNG BÌNH hai mức, không phải        ║
║      mức ban đầu — nếu không, A→B và B→A cho hai đáp án khác nhau         ║
║      (0,66 vs 1,5 → cùng bằng 1,0)                                        ║
║                                                                           ║
║  ── BỐN YẾU TỐ QUYẾT ĐỊNH e CỦA CẦU ────────────────────────────────      ║
║      ① nhiều hàng THAY THẾ  → co giãn hơn                                ║
║      ② XA XỈ co giãn, THIẾT YẾU không — nhưng tuỳ NGƯỜI MUA, không       ║
║         phải tính chất món hàng                                           ║
║      ③ thị trường định nghĩa càng HẸP → càng co giãn                     ║
║         thực phẩm 〈 kem 〈 kem vani                                      ║
║      ④ DÀI HẠN co giãn hơn NGẮN HẠN                                      ║
║                                                                           ║
║  ── NĂM DẠNG ───────────────────────────────────────────────────────      ║
║      e=0 thẳng đứng | e<1 dốc | e=1 | e>1 thoải | e=∞ nằm ngang           ║
║      💡 Inelastic trông như chữ I                                         ║
║      thực tế: trứng 0,1 · y tế 0,2 · gạo 0,5 · thịt bò 1,6 ·              ║
║               nhà hàng 2,3 · Mountain Dew 4,4                             ║
║                                                                           ║
║  ⭐⭐ BA QUY TẮC DOANH THU — thuộc lòng                                    ║
║      e < 1 (không co giãn): giá và doanh thu CÙNG hướng                   ║
║      e > 1 (co giãn)      : giá và doanh thu NGƯỢC hướng                  ║
║      e = 1                 : doanh thu KHÔNG ĐỔI                          ║
║      ⚠ doanh thu ≠ lợi nhuận. Đỉnh lợi nhuận ở giá CAO HƠN (bài 5-6)      ║
║                                                                           ║
║  ⚠ ĐỘ DỐC KHÔNG ĐỔI ≠ ĐỘ CO GIÃN KHÔNG ĐỔI                                ║
║      trên một đường cầu THẲNG: giá cao lượng thấp → CO GIÃN               ║
║                                giá thấp lượng cao → KHÔNG co giãn         ║
║      ⟹ "e của ta bằng 1,8" là câu THIẾU: phải hỏi Ở VÙNG GIÁ NÀO         ║
║                                                                           ║
║  ── HAI ĐỘ CO GIÃN KHÁC ────────────────────────────────────────────      ║
║      THU NHẬP  dấu ÂM = hàng thứ cấp | dương lớn = xa xỉ, theo chu kỳ     ║
║      GIÁ CHÉO  dấu DƯƠNG = thay thế (ĐỐI THỦ) | âm = bổ sung (bán kèm)    ║
║      ⭐ "ai là đối thủ của ta" là một CON SỐ ĐO ĐƯỢC                      ║
║                                                                           ║
║  ── CUNG ───────────────────────────────────────────────────────────      ║
║      yếu tố lớn nhất là THỜI GIAN: dài hạn xây/đóng nhà máy, ra/vào ngành ║
║      e của cung GIẢM khi đụng TRẦN CÔNG SUẤT (Hình 6)                     ║
║                                                                           ║
║  ── BA ỨNG DỤNG ────────────────────────────────────────────────────      ║
║  ① NÔNG DÂN  giống mới → cung↑ → giá rơi mạnh, lượng tăng nhẹ            ║
║      300 → 220 đô la. Năng suất TĂNG mà thu nhập GIẢM                     ║
║      từng người vẫn phải dùng → tiến thoái lưỡng nan (bài 9)              ║
║      1950: 10 tr nông dân = 17% LLLĐ | nay: <3 tr = 2%, sản lượng GẤP ĐÔI ║
║  ② OPEC  ngắn hạn hai đường DỐC → cắt cung, giá vọt → thắng              ║
║      dài hạn hai đường THOẢI → cùng mức cắt, giá nhích → thua             ║
║      💼 đo tác động tăng giá bằng số liệu 1 tháng là SAI PHƯƠNG PHÁP      ║
║  ③ MA TUÝ  cấm → cung↓ → giá↑ → cầu không co giãn → TỔNG CHI TĂNG        ║
║             giáo dục → cầu↓ → giá↓ → TỔNG CHI GIẢM                        ║
║      ⟹ kết luận chính sách xoay quanh MỘT CON SỐ, không phải quan điểm   ║
║                                                                           ║
║  💼 ĐO e TỪ DỮ LIỆU THẬT                                                  ║
║      hồi quy ln(Q) theo ln(P)  ⟹  hệ số góc CHÍNH LÀ −e                  ║
║      (đúng công thức Sxy/Sxx ở bài 14 môn Xác suất Thống kê)              ║
║      ⚠ bỏ sót biến · nhân quả ngược · ngoại suy ngoài vùng dữ liệu        ║
║      ⟹ chắc chắn nhất vẫn là A/B TEST có đối chứng                       ║
║      ⭐ giảm giá là cách cạnh tranh của người có e LỚN.                   ║
║         Việc của quản trị là làm cho e NHỎ ĐI (bài 7, 8)                  ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **N. Gregory Mankiw, *Kinh tế học vi mô*** — bản dịch của Khoa Kinh tế, Trường ĐH Kinh tế TP.HCM,
  Cengage Learning Asia. Tệp trong kho: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  — **trang sách N = trang PDF N + 33**.
  - **Chương 5 — Độ co giãn và ứng dụng**, tr. 103–126
    - *Độ co giãn của cầu theo giá và các nhân tố tác động*, tr. 104–105
    - *Phương pháp trung điểm*, tr. 105–106
    - Hình 1 *Độ co giãn của cầu theo giá — năm trường hợp*, tr. 107
    - Bạn có biết *Độ co giãn trên thực tế*, tr. 108
    - Hình 2 *Tổng doanh thu*, tr. 109
    - Hình 3 *Tác động của sự thay đổi của giá lên tổng doanh thu*, tr. 109
    - Hình 4 *Độ co giãn trên đường cầu tuyến tính*, tr. 110
    - *Các độ co giãn khác của cầu* (thu nhập, giá chéo), tr. 111–112
    - *Độ co giãn của cung*, tr. 112–113
    - Hình 5 *Độ co giãn của cung theo giá — năm trường hợp*, tr. 114
    - Hình 6 *Độ co giãn của cung có thể thay đổi như thế nào*, tr. 115
    - Hình 7 *Tăng cung trên thị trường lúa mì*, tr. 116
    - Hình 8 *Giảm cung trên thị trường dầu mỏ thế giới*, tr. 119
    - Hình 9 *Các chính sách làm giảm sử dụng ma tuý bất hợp pháp*, tr. 121
- **Đính chính đã ghi trong bài:** Hình 3, tr. 109 — hai khung con **cùng đánh nhãn "(a)"**; khung bên
  phải phải là **"(b)"** (chính đoạn văn tr. 110 gọi nó là *Hình 3(b)*). Đối chiếu bản quét 300 dpi.
- **Liên hệ chéo:**
  - [Bài 2 — Cung và cầu](bai_02_cung_va_cau.md) — mô hình mà chương này đo lường.
  - [Bài 1 — mục 15](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#15--đọc-đồ-thị-độ-dốc-bỏ-sót-biến-nhân-quả-ngược) — bỏ sót biến, nhân quả ngược.
  - [Bài 14 môn Xác suất Thống kê](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md) — công thức hồi quy dùng ở mục 15.
  - [Bài 13 môn Xác suất Thống kê](../../%5BEG11%5D.xacxuatthongke/ly_thuyet/bai_13_kiem_dinh_nhieu_mau_va_anova.md) — A/B test có đối chứng.

<!-- BAN-DO -->

**Bản đồ khoá học**

|     # | Bài                                                                                    | Chương sách | Ưu tiên |
| ----: | -------------------------------------------------------------------------------------- | ----------- | :-----: |
|     1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)         | ch. 1–2     |    🎯    |
|     2 | [Cung và cầu](bai_02_cung_va_cau.md)                                                   | ch. 4       |    🎯    |
| **3** | **Độ co giãn và định giá** ← *bạn đang ở đây*                                          | ch. 5       |   🎯⭐    |
|     4 | [Thặng dư và chi phí của thuế](bai_04_thang_du_va_chi_phi_cua_thue.md)                 | ch. 7–8     |    🔸    |
|     5 | [Chi phí sản xuất](bai_05_chi_phi_san_xuat.md)                                         | ch. 13      |    🎯    |
|     6 | [Doanh nghiệp trên thị trường cạnh tranh](bai_06_thi_truong_canh_tranh.md)             | ch. 14      |    🎯    |
|     7 | [Độc quyền và phân biệt giá](bai_07_doc_quyen_va_phan_biet_gia.md)                     | ch. 15      |    🎯    |
|     8 | [Cạnh tranh độc quyền và thương hiệu](bai_08_canh_tranh_doc_quyen.md)                  | ch. 16      |    🎯    |
|     9 | [Độc quyền nhóm và lý thuyết trò chơi](bai_09_doc_quyen_nhom_va_ly_thuyet_tro_choi.md) | ch. 17      |    🎯    |
|    10 | [Lựa chọn của người tiêu dùng](bai_10_lua_chon_cua_nguoi_tieu_dung.md)                 | ch. 21      |    🎯    |
|    11 | [Thông tin bất cân xứng và hành vi](bai_11_thong_tin_bat_can_xung.md)                  | ch. 22      |    🎯    |
|    12 | [Lao động, tiền lương, bất bình đẳng](bai_12_thi_truong_lao_dong.md)                   | ch. 18–20   |    🔸    |
|    13 | Chính phủ can thiệp thị trường *(chưa viết)*                                           | ch. 6, 12   |    🔸    |
|    14 | Thương mại, ngoại tác, hàng hoá công *(chưa viết)*                                     | ch. 3, 9–11 |    🔸    |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương quan trọng nhất với QTKD

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
