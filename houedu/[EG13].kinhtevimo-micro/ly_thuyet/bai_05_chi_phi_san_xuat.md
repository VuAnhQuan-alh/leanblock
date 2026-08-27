# Bài 5 — Chi phí sản xuất

> Bài học dựng từ **Chương 13 — Chi phí sản xuất** (tr. 283–307)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🎯 **Vòng 1.** Đây là bài mở đầu **Phần V — Hành vi doanh nghiệp**, và là **bộ công cụ** mà bài 6, 7,
> 8, 9 đều dùng lại. Không nắm chương này thì không đọc được bốn bài sau.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp phụ.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 1, mục 3–4](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó)
> (chi phí cơ hội và tư duy biên). Bài này là phiên bản đầy đủ của hai nguyên lý đó.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Lời cảnh báo thật thà của chính tác giả](#1-lời-cảnh-báo-thật-thà-của-chính-tác-giả)
- [2. Chi phí sổ sách và chi phí ẩn](#2-chi-phí-sổ-sách-và-chi-phí-ẩn)
- [3. Chi phí vốn — khoản chi phí ẩn lớn nhất](#3-chi-phí-vốn--khoản-chi-phí-ẩn-lớn-nhất)
- [4. Lợi nhuận kinh tế và lợi nhuận kế toán](#4-lợi-nhuận-kinh-tế-và-lợi-nhuận-kế-toán)
- [5. Hàm sản xuất và sản lượng biên giảm dần](#5-hàm-sản-xuất-và-sản-lượng-biên-giảm-dần)
- [6. Bốn thước đo chi phí — và bảng phải thuộc](#6-bốn-thước-đo-chi-phí--và-bảng-phải-thuộc)
- [7. Ba đặc điểm của mọi đường chi phí](#7-ba-đặc-điểm-của-mọi-đường-chi-phí)
- [8. Ngắn hạn và dài hạn — ranh giới cố định/biến đổi là ranh giới THỜI GIAN](#8-ngắn-hạn-và-dài-hạn--ranh-giới-cố-địnhbiến-đổi-là-ranh-giới-thời-gian)
- [9. Lợi thế và bất lợi thế kinh tế theo quy mô](#9-lợi-thế-và-bất-lợi-thế-kinh-tế-theo-quy-mô)
- [10. 💼 Ba con số, ba câu hỏi — và cái bẫy định giá theo chi phí](#10--ba-con-số-ba-câu-hỏi--và-cái-bẫy-định-giá-theo-chi-phí)
- [11. Bảng 3 — tóm tắt toàn bộ từ vựng chi phí](#11-bảng-3--tóm-tắt-toàn-bộ-từ-vựng-chi-phí)
- [12. Code minh hoạ](#12-code-minh-hoạ)
- [13. Tự thử](#13-tự-thử)
- [14. Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
- [15. Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Lời cảnh báo thật thà của chính tác giả

Sách mở chương bằng một câu hiếm thấy trong giáo trình (tr. 284):

> *"Một lưu ý nho nhỏ: chủ đề này hơi khô khan và mang tính kỹ thuật. Thành thật mà nói, bạn có thể
> cảm thấy chán. Nhưng tài liệu này cung cấp **một nền tảng quan trọng** cho những chủ đề hấp dẫn tiếp
> theo sau đó."*

Đúng như vậy. Chương này không có kết luận gây ngạc nhiên nào. Nhưng nó là **bộ từ vựng** — ATC, AVC,
MC, quy mô hiệu quả — mà mọi quyết định sản xuất và định giá ở bài 6 đến bài 9 đều phát biểu bằng.

Toàn chương xoay quanh một mục tiêu duy nhất mà sách giả định cho doanh nghiệp (tr. 284):

> *"các nhà kinh tế giả định rằng mục tiêu của các doanh nghiệp là **tối đa hoá lợi nhuận**, và họ thấy
> rằng giả định này thường đúng trong hầu hết mọi trường hợp."*

$$\text{Lợi nhuận} = \text{Tổng doanh thu} - \text{Tổng chi phí}$$

Ba định nghĩa nền (chú thích tr. 284):

> **Tổng doanh thu** (*total revenue*): khoản thu của doanh nghiệp khi bán sản phẩm đầu ra.
> **Tổng chi phí** (*total cost*): giá trị thị trường của những đầu vào mà doanh nghiệp sử dụng để sản xuất.
> **Lợi nhuận** (*profit*): tổng doanh thu trừ đi tổng chi phí.

Nhân vật xuyên suốt: **Caroline**, chủ Nhà máy Bánh quy bơ. Cô mua bột, đường, hạt chocolate, máy trộn,
lò nướng và thuê công nhân. Nếu sản xuất **10.000 bánh** bán giá **2 đô la**, tổng doanh thu là
**20.000 đô la** (tr. 285). Doanh thu dễ tính. **Chi phí thì không.**

---

## 2. Chi phí sổ sách và chi phí ẩn

Sách gọi thẳng về nguyên lý 2 ở [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó):
*"Chi phí của một thứ gì đó là tất cả những gì chúng ta từ bỏ để có được nó"* (tr. 285). Khi nhà kinh
tế nói **chi phí sản xuất**, họ **đã tính luôn chi phí cơ hội**.

> **Chi phí sổ sách** (*explicit costs*): những chi phí cho yếu tố đầu vào đòi hỏi doanh nghiệp phải
> bỏ tiền ra chi trả. — chú thích tr. 285
> **Chi phí ẩn** (*implicit costs*): những chi phí đầu vào không đòi hỏi doanh nghiệp phải chi tiền ra
> để trả. — chú thích tr. 285

| Loại | Ví dụ của sách | Có dòng tiền đi ra? |
| --- | --- | --- |
| **Sổ sách** | 1.000 đô la mua bột; tiền công trả công nhân | ✅ có |
| **Ẩn** | Caroline giỏi máy tính, có thể kiếm **100 đô la mỗi giờ** làm lập trình viên — mỗi giờ làm bánh là **100 đô la thu nhập từ bỏ** | ❌ không |

Và sách rút ra sự khác biệt nghề nghiệp rất rõ (tr. 285):

| | Nhà kinh tế | Nhân viên kế toán |
| --- | --- | --- |
| Nghiên cứu / làm gì | doanh nghiệp **sản xuất và định giá** thế nào | quản lý **dòng tiền** ra vào |
| Tính chi phí nào | **cả** sổ sách **và** ẩn | **chỉ** sổ sách |

Ví dụ mà sách dùng để cho thấy chi phí ẩn **thật sự ảnh hưởng quyết định** (tr. 286): nếu tiền công
lập trình viên của Caroline tăng từ **100 lên 500 đô la một giờ**, cô có thể quyết định *"chi phí vận
hành việc kinh doanh bánh quy bơ là quá lớn"* và **đóng cửa nhà máy** để đi lập trình toàn thời gian.

⚠️ Chú ý: **không có dòng tiền nào thay đổi** trong sổ sách của tiệm bánh, nhưng quyết định thì đảo
ngược. Đó là bằng chứng chi phí ẩn là chi phí **thật**.

---

## 3. Chi phí vốn — khoản chi phí ẩn lớn nhất

Sách dành một mục riêng cho vốn vì nó là *"một khoản chi phí ẩn quan trọng của hầu hết các doanh
nghiệp"* (tr. 286).

**Tình huống A — toàn bộ vốn tự có.** Caroline dùng **300.000 đô la** tiền tiết kiệm mua nhà máy. Nếu
gửi ngân hàng lãi **5%**, cô sẽ có **15.000 đô la tiền lãi mỗi năm**. Khoản 15.000 bị từ bỏ đó là
**chi phí ẩn**.

**Tình huống B — vay một phần.** Caroline chỉ có **100.000**, vay ngân hàng **200.000** lãi **5%**:

| | Cách tính | Kết quả |
| --- | --- | ---: |
| **Kế toán** | chỉ lãi vay trả ngân hàng (có dòng tiền ra) | **10.000** |
| **Nhà kinh tế** | lãi vay 10.000 (**sổ sách**) + lãi tiết kiệm từ bỏ 5.000 (**ẩn**) | **15.000** |

⭐ **Điểm đáng nhớ nhất mục này:** chi phí cơ hội của vốn **vẫn là 15.000 đô la** trong cả hai tình
huống. Nó **không đổi theo cơ cấu vốn**. Vay hay không vay chỉ đổi chỗ khoản tiền nằm trong sổ kế
toán, không đổi chi phí thật của việc dùng 300.000 đô la vào tiệm bánh thay vì việc khác.

---

## 4. Lợi nhuận kinh tế và lợi nhuận kế toán

> **Lợi nhuận kinh tế** (*economic profit*): tổng doanh thu trừ đi tổng chi phí, bao gồm **cả** chi phí
> sổ sách **và** chi phí ẩn. — chú thích tr. 286
> **Lợi nhuận kế toán** (*accounting profit*): tổng doanh thu trừ đi **chỉ** chi phí sổ sách. — chú thích tr. 287

**Hình 1, tr. 287** trình bày hai cột song song:

```
        ĐỐI VỚI NHÀ KINH TẾ              ĐỐI VỚI NHÂN VIÊN KẾ TOÁN
   ┌──────────────────────────┐      ┌──────────────────────────┐
   │   LỢI NHUẬN KINH TẾ      │      │                          │
   ├──────────────────────────┤      │   LỢI NHUẬN KẾ TOÁN      │
   │   chi phí ẨN             │      │                          │
   ├──────────────────────────┤      ├──────────────────────────┤
   │                          │      │                          │
   │   chi phí SỔ SÁCH        │      │   chi phí SỔ SÁCH        │
   │                          │      │                          │
   └──────────────────────────┘      └──────────────────────────┘
        cùng một DOANH THU                cùng một DOANH THU
```

⭐ **Hệ quả bắt buộc phải nhớ:**

> **Lợi nhuận kế toán LUÔN LỚN HƠN lợi nhuận kinh tế** (trừ khi chi phí ẩn bằng 0).

Và ý nghĩa của lợi nhuận kinh tế, theo sách (tr. 287):

| Lợi nhuận kinh tế | Nghĩa là | Chủ doanh nghiệp sẽ |
| --- | --- | --- |
| **dương** | doanh thu bù được **mọi** chi phí cơ hội, còn dư | **tiếp tục** kinh doanh |
| **âm** (lỗ kinh tế) | *"chủ sở hữu doanh nghiệp sẽ thu không đủ để bù đắp chi phí sản xuất"* | *"chắc chắn sẽ **đóng cửa** kinh doanh và rời khỏi ngành"* |

📌 Câu cuối cùng ấy — *"rời khỏi ngành"* — là hạt giống của toàn bộ **bài 6** (chương 14): trong thị
trường cạnh tranh, doanh nghiệp gia nhập khi lợi nhuận kinh tế dương và rời đi khi âm, cho tới khi
**lợi nhuận kinh tế bằng 0**.

⚠️ **"Lợi nhuận kinh tế bằng 0" KHÔNG có nghĩa là "làm không công".** Nó nghĩa là doanh thu vừa đủ bù
mọi chi phí cơ hội — tức chủ doanh nghiệp đang kiếm **đúng bằng** phương án tốt nhất kế tiếp của mình.
Đây là chỗ nhầm phổ biến nhất trong cả môn học.

### 💼 Góc QTKD — ba khoản chi phí ẩn mà báo cáo của bạn không ghi

Mục 12 tính đầy đủ một bảng lãi–lỗ hai cách. Ba khoản thường bị bỏ sót nhất:

| Khoản ẩn | Cách ước lượng |
| --- | --- |
| **Vốn chủ sở hữu** | vốn × lợi suất phương án an toàn (gửi ngân hàng, trái phiếu) |
| **Mặt bằng tự có** | giá thuê thị trường của chính mặt bằng đó |
| **Công sức người sáng lập** | mức lương bạn nhận được nếu đi làm thuê cùng vị trí |

⭐ **Bài kiểm tra nhanh:** nếu bạn cộng ba khoản trên vào và lợi nhuận thành **âm**, doanh nghiệp của
bạn đang **phá huỷ giá trị** — dù báo cáo tài chính vẫn màu xanh. Bạn đang bù lỗ bằng chính tài sản và
thời gian của mình.

---

## 5. Hàm sản xuất và sản lượng biên giảm dần

Từ đây sách chuyển sang **cơ chế**: chi phí đến từ đâu.

⚠️ **Giả định quan trọng của cả phần này** (tr. 288): *"quy mô nhà máy của Caroline là **cố định** và
Caroline có thể thay đổi sản lượng… bằng cách duy nhất là thay đổi số lượng công nhân"*. Sách nói rõ
đây là **ngắn hạn**; dài hạn sẽ bàn ở mục 10.

> **Hàm sản xuất** (*production function*): mối quan hệ giữa sản lượng đầu vào được sử dụng để tạo ra
> hàng hoá và sản lượng đầu ra của hàng hoá đó. — chú thích tr. 288
> **Sản lượng biên** (*marginal product*): gia tăng trong sản lượng do tăng một đơn vị đầu vào. — chú thích tr. 289
> **Sản lượng biên giảm dần** (*diminishing marginal product*): đặc tính thể hiện mức sản lượng biên
> giảm khi số lượng đầu vào tăng. — chú thích tr. 290

**Bảng 1, tr. 288** — nhà máy 30 đô la/giờ, mỗi công nhân 10 đô la/giờ:

| Số công nhân | Sản lượng | Sản lượng biên | CP nhà máy | CP nhân công | **Tổng chi phí** |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | | $30 | $0 | **$30** |
| | | **50** | | | |
| 1 | 50 | | 30 | 10 | **40** |
| | | **40** | | | |
| 2 | 90 | | 30 | 20 | **50** |
| | | **30** | | | |
| 3 | 120 | | 30 | 30 | **60** |
| | | **20** | | | |
| 4 | 140 | | 30 | 40 | **70** |
| | | **10** | | | |
| 5 | 150 | | 30 | 50 | **80** |
| | | **5** | | | |
| 6 | 155 | | 30 | 60 | **90** |

Sản lượng biên đi **50 → 40 → 30 → 20 → 10 → 5**. Lý do sách đưa ra rất cụ thể (tr. 290):

> *"khi chỉ có một vài công nhân được thuê, họ dễ dàng sử dụng các thiết bị trong nhà bếp của Caroline.
> Khi số lượng công nhân tăng lên, những công nhân mới vào sẽ phải chia sẻ thiết bị và làm việc trong
> môi trường chật chội hơn. Thậm chí là **nhà bếp trở nên quá chật chội đến nỗi mọi người bắt đầu vướng
> tay vướng chân nhau**."*

### ⭐ Hai mặt của một đồng xu

**Hình 2, tr. 289** đặt cạnh nhau hàm sản xuất (a) và đường tổng chi phí (b). Sách nói rõ chúng là
*"hai mặt của một đồng xu"* (tr. 290):

```
   SẢN LƯỢNG BIÊN GIẢM DẦN
        │
        ├──► hàm sản xuất ngày càng BẰNG PHẲNG
        │     (thêm công nhân, sản lượng tăng ít dần)
        │
        └──► đường tổng chi phí ngày càng DỐC
              (thêm sản lượng, chi phí tăng nhiều dần)
```

Lập luận nối hai điều: *"khi nhà bếp chật chội, sản xuất thêm một cái bánh quy bơ đòi hỏi thêm nhiều
lao động và do đó rất là tốn kém"* (tr. 290).

---

## 6. Bốn thước đo chi phí — và bảng phải thuộc

Nhân vật mới: **Conrad**, hàng xóm của Caroline, chủ tiệm cà phê. **Bảng 2, tr. 292** là bảng quan
trọng nhất chương.

Bốn định nghĩa (chú thích tr. 292–293):

> **Chi phí cố định** (*fixed costs*): chi phí không đổi theo sản lượng.
> **Chi phí biến đổi** (*variable costs*): chi phí thay đổi theo sản lượng.
> **Tổng chi phí bình quân** (*average total cost*): tổng chi phí chia cho sản lượng.
> **Chi phí biên** (*marginal cost*): phần tăng thêm trong tổng chi phí khi sản xuất thêm một đơn vị sản phẩm.

$$ATC = \frac{TC}{Q} \qquad\qquad MC = \frac{\Delta TC}{\Delta Q}$$

Cùng với hai thước đo phụ: $AFC = FC/Q$ và $AVC = VC/Q$, và $ATC = AFC + AVC$.

**Bảng 2 — Tiệm Café của Conrad (tr. 292):**

| Q (ly/giờ) | Tổng CP | CP cố định | CP biến đổi | AFC | AVC | **ATC** | *Chi phí biên* |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | $3,00 | $3,00 | $0,00 | — | — | — | |
| | | | | | | | *$0,30* |
| 1 | 3,30 | 3,00 | 0,30 | $3,00 | $0,30 | **$3,30** | |
| | | | | | | | *0,50* |
| 2 | 3,80 | 3,00 | 0,80 | 1,50 | 0,40 | **1,90** | |
| | | | | | | | *0,70* |
| 3 | 4,50 | 3,00 | 1,50 | 1,00 | 0,50 | **1,50** | |
| | | | | | | | *0,90* |
| 4 | 5,40 | 3,00 | 2,40 | 0,75 | 0,60 | **1,35** | |
| | | | | | | | *1,10* |
| **5** | 6,50 | 3,00 | 3,50 | 0,60 | 0,70 | **1,30** ⭐ | |
| | | | | | | | *1,30* |
| **6** | 7,80 | 3,00 | 4,80 | 0,50 | 0,80 | **1,30** ⭐ | |
| | | | | | | | *1,50* |
| 7 | 9,30 | 3,00 | 6,30 | 0,43 | 0,90 | **1,33** | |
| | | | | | | | *1,70* |
| 8 | 11,00 | 3,00 | 8,00 | 0,38 | 1,00 | **1,38** | |
| | | | | | | | *1,90* |
| 9 | 12,90 | 3,00 | 9,90 | 0,33 | 1,10 | **1,43** | |
| | | | | | | | *2,10* |
| 10 | 15,00 | 3,00 | 12,00 | 0,30 | 1,20 | **1,50** | |

📚 **Một quan sát không có trong sách nhưng rất hữu ích:** bảng này không phải số ngẫu nhiên. Chi phí
biên tăng **đều đúng 0,20 đô la** mỗi ly, tức $MC(q) = 0{,}10 + 0{,}20q$. Từ đó suy ra công thức đóng
cho toàn bảng:

$$VC(Q) = 0{,}10 \cdot Q \cdot (Q+2) \qquad TC(Q) = 3 + 0{,}10 \cdot Q \cdot (Q+2)$$

Mục 12 dùng đúng công thức này để **sinh lại toàn bộ Bảng 2** và đối chiếu từng ô với bản in — khớp
10/10 dòng.

⚠️ **Chú ý vị trí của chi phí biên trong bảng.** Sách viết rõ (tr. 293): *"chi phí biên xuất hiện nằm
ở lưng chừng giữa hai cột và nó thể hiện sự thay đổi trong tổng chi phí khi sản lượng đầu ra tăng từ
mức độ này sang mức độ khác"*. Nó **không thuộc về một sản lượng**, mà thuộc về **bước đi giữa hai
sản lượng**.

---

## 7. Ba đặc điểm của mọi đường chi phí

**Hình 4, tr. 294** vẽ bốn đường ATC, AFC, AVC, MC. Sách rút ra **ba đặc điểm chung của mọi doanh
nghiệp** (tr. 297):

> - Sớm muộn gì thì **chi phí biên cũng sẽ tăng** khi sản lượng đầu ra tăng.
> - **Đường tổng chi phí bình quân có dạng hình chữ U.**
> - **Đường chi phí biên cắt đường tổng chi phí bình quân tại điểm thấp nhất** của đường tổng chi phí bình quân.

### ① Chi phí biên tăng dần

Phản ánh trực tiếp **sản lượng biên giảm dần**. Cơ chế của sách (tr. 294–295): ở sản lượng thấp, Conrad
*"có ít công nhân, và nhiều thiết bị không được sử dụng hết công suất"* → thuê thêm rẻ. Ở sản lượng
cao, *"nhân viên mới phải làm trong điều kiện chật chội và có thể phải xếp hàng chờ đến lượt sử dụng
trang thiết bị"* → chi phí biên cao.

### ② Đường ATC hình chữ U

Vì $ATC = AFC + AVC$, và hai thành phần đi **ngược chiều nhau**:

```
   AFC = FC/Q   GIẢM liên tục         (chi phí cố định chia cho ngày càng nhiều đơn vị)
   AVC = VC/Q   TĂNG dần               (do sản lượng biên giảm dần)
   ──────────────────────────────────────────────────────────────
   ATC          giảm trước, tăng sau  ⟹  hình chữ U
```

> **Quy mô hiệu quả** (*efficient scale*): mức sản lượng mà tại đó tổng chi phí bình quân thấp nhất.
> — chú thích tr. 295

Với Conrad, quy mô hiệu quả là **5 hay 6 ly cà phê mỗi giờ**, ATC = **1,30 đô la**.

### ③ MC cắt ATC tại đáy chữ U — và vì sao

Đây là quan hệ đẹp nhất chương, và sách phát biểu nó bằng hai câu in nghiêng (tr. 295–296):

> *"**Bất cứ khi nào mà chi phí biên nhỏ hơn tổng chi phí bình quân, thì tổng chi phí bình quân đang
> giảm dần. Bất cứ khi nào mà chi phí biên lớn hơn tổng chi phí bình quân, tổng chi phí bình quân đang
> tăng dần.**"*

💡 **Phép ẩn dụ của sách rất hay** (tr. 296):

> Tổng chi phí bình quân giống như **điểm trung bình tích luỹ**. Chi phí biên giống như **điểm của môn
> học kế tiếp** mà bạn sẽ nhận được. Nếu điểm môn kế tiếp **thấp hơn** điểm trung bình, điểm trung bình
> sẽ bị **kéo xuống**. Nếu **cao hơn**, điểm trung bình được **nâng lên**.

Và hệ quả logic:

> ⭐ *"đường chi phí biên sẽ đi qua **điểm thấp nhất** của đường tổng chi phí bình quân"*

Vì trước giao điểm MC < ATC nên ATC giảm; sau giao điểm MC > ATC nên ATC tăng. Chỗ chuyển từ giảm sang
tăng **chính là** chỗ hai đường gặp nhau.

📌 Sách nói trước tầm quan trọng của điểm này: *"điểm có tổng chi phí bình quân thấp nhất sẽ đóng vai
trò **then chốt** trong việc phân tích hoạt động của các doanh nghiệp cạnh tranh trên thị trường"*
(tr. 296) — đó là **bài 6**.

Mục 12 kiểm quy tắc này bằng số cho **cả 9 bước** của bảng Conrad: mọi bước đều đúng, và MC(6) = ATC(6)
= 1,30 đô la đúng tại quy mô hiệu quả.

### 📚 Đường chi phí "điển hình" thực tế phức tạp hơn

Sách thừa nhận ví dụ Conrad là **đơn giản hoá** (tr. 296). Trong nhiều doanh nghiệp, *"nhân viên thứ
hai hay thứ ba có thể mang lại mức sản lượng biên lớn hơn người đầu tiên, bởi vì làm việc nhóm có thể
phân chia công việc và nhiệm vụ một cách hiệu quả hơn là một cá nhân"*.

Nên **Hình 5 (tr. 297)** vẽ đường chi phí điển hình hơn: MC **giảm một đoạn** rồi mới tăng, AVC cũng
vậy. Nhưng **ba đặc điểm ở trên vẫn đúng**.
---

## 8. Ngắn hạn và dài hạn — ranh giới cố định/biến đổi là ranh giới THỜI GIAN

Đây là ý mà sinh viên hay bỏ qua, nhưng nó quyết định cách đọc mọi con số chi phí:

> **Ranh giới phân chia tổng chi phí thành chi phí cố định và chi phí biến đổi phụ thuộc vào độ dài
> thời gian.** (tr. 297)

Ví dụ **Ford Motor** của sách (tr. 297–298):

| Khoảng thời gian | Ford làm được gì | Nhà máy là chi phí |
| --- | --- | --- |
| **Vài tháng** (ngắn hạn) | *"không thể điều chỉnh số lượng hay quy mô nhà máy"* — chỉ thuê thêm nhân công | **cố định** |
| **Vài năm** (dài hạn) | *"mở rộng quy mô nhà máy, xây dựng thêm nhà máy mới hay đóng cửa những nhà máy cũ"* | **biến đổi** |

**Hình 6, tr. 298** vẽ ba đường ATC ngắn hạn (nhà máy nhỏ, trung bình, lớn) cùng một đường **ATC dài
hạn**. Hai tính chất:

```
   ① ATC DÀI HẠN có dạng chữ U PHẲNG HƠN NHIỀU so với ngắn hạn
   ② MỌI đường ngắn hạn đều NẰM TRÊN hoặc CHẠM đường dài hạn
```

Lý do sách nêu rất gọn (tr. 298): *"doanh nghiệp trong dài hạn có **tính linh hoạt cao hơn** trong
ngắn hạn… trong dài hạn, ứng với từng giai đoạn, doanh nghiệp sẽ **chọn** đường ngắn hạn nào mà họ
muốn sử dụng. Nhưng trong ngắn hạn, họ sẽ **phải sử dụng** đường chi phí ngắn hạn mà họ đã chọn
trước đó."*

### Câu chuyện Ford — con số cụ thể

| | Sản lượng | ATC |
| --- | ---: | ---: |
| Hiện tại (nhà máy trung bình) | 1.000 xe/ngày | **10.000 đô la** |
| **Ngắn hạn** — chỉ thuê thêm công nhân ở nhà máy cũ | 1.200 xe/ngày | **12.000 đô la** |
| **Dài hạn** — mở rộng cả nhà máy lẫn nhân công | 1.200 xe/ngày | **10.000 đô la** |

⚠️ **Đính chính — tr. 298.** Sách viết:

> *"Khi Ford muốn gia tăng sản lượng từ 1.000 lên **2.000** chiếc xe hơi mỗi ngày…"*

Con số **2.000** là **sai**, đúng phải là **1.200**:

- **Hình 6 ngay trên đoạn văn đó** đánh dấu trục hoành tại **1.000** và **1.200**, không có 2.000.
- Đường gạch ngang ATC = **12.000 đô la** trong hình cắt đường ATC ngắn hạn của nhà máy trung bình
  **đúng tại 1.200**.
- Bản gốc tiếng Anh: *"from 1,000 to 1,200 cars per day"*.

Đã đối chiếu bản quét 300 dpi cả phần chữ lẫn phần hình. Không đổi lập luận, nhưng nếu bạn vẽ lại đồ
thị theo con số 2.000 thì sẽ không khớp hình của chính sách.

Sách cũng nói **mất bao lâu để "chuyển sang dài hạn"** thì không có câu trả lời chung (tr. 298–299):
*"Có thể mất một năm hoặc lâu hơn để một doanh nghiệp lớn, như là công ty sản xuất xe hơi, xây dựng
nhà máy rộng lớn hơn. Ngược lại, một người quản lý quán cà phê có thể mua một máy chế biến cà phê khác
**trong vòng một vài ngày**."*

💼 **Đây là câu hỏi thực tế bạn phải tự trả lời cho doanh nghiệp mình:** *"chi phí nào của ta là cố
định trong 3 tháng? trong 1 năm? trong 3 năm?"* — ba câu trả lời khác nhau, và chúng dẫn tới ba quyết
định khác nhau khi cầu sụt.

---

## 9. Lợi thế và bất lợi thế kinh tế theo quy mô

Ba định nghĩa (chú thích tr. 299):

> **Lợi thế kinh tế theo quy mô** (*economies of scale*): tổng chi phí bình quân trong dài hạn **giảm**
> khi sản lượng tăng.
> **Bất lợi thế kinh tế theo quy mô** (*diseconomies of scale*): tổng chi phí bình quân trong dài hạn
> **tăng** khi sản lượng tăng.
> **Lợi thế không đổi theo quy mô** (*constant returns to scale*): tổng chi phí bình quân trong dài hạn
> **không đổi** khi sản lượng thay đổi.

Và **nguyên nhân** — đây mới là phần đáng nhớ:

| Hiện tượng | Nguyên nhân theo sách (tr. 299) |
| --- | --- |
| **Lợi thế** theo quy mô | **chuyên môn hoá** — *"mức sản lượng cao hơn cho phép sự chuyên môn hoá trong những người công nhân lao động, cho phép mỗi công nhân làm việc tốt hơn với mỗi nhiệm vụ cụ thể được giao"* |
| **Bất lợi thế** theo quy mô | **vấn đề phối hợp** — *"Càng sản xuất thêm nhiều xe hơi, đội ngũ quản lý càng bị kéo giãn hơn, và các nhà quản lý sẽ khó mà kìm giữ được chi phí ở mức thấp"* |

Đó cũng là lý do đường dài hạn có **dạng chữ U**: ở sản lượng thấp, chuyên môn hoá thắng; ở sản lượng
cao, vấn đề phối hợp thắng.

### 📚 Nhà máy sản xuất đinh ghim của Adam Smith (tr. 300)

Hộp *"Bạn có biết"* dẫn lại đoạn nổi tiếng trong *Bàn về bản chất và nguồn gốc của sự giàu có của các
quốc gia* — cùng cuốn sách 1776 đã gặp ở [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#7-nguyên-lý-5-6-7--con-người-tương-tác-với-nhau):

> *"Một người rút dây, một người kéo thẳng nó ra, người thứ ba cắt, người thứ tư bám lỗ, người thứ năm
> đập vào đầu sợi dây để tạo thành đầu kim, để làm được đầu ghim cần có hai hay ba thao tác; làm ra nó
> là một công đoạn kỳ diệu, đánh bóng nó lại là một công đoạn khác, thậm chí việc đóng hộp cũng là một
> công đoạn riêng."*

Con số Smith đưa ra: nhờ chuyên môn hoá, mỗi công nhân tạo ra **hàng ngàn chiếc mỗi ngày**; nếu làm
độc lập, *"họ chắc chắn không thể nào làm nổi **20 chiếc** mỗi ngày, thậm chí còn không được chiếc
nào"*.

Ngạn ngữ Việt mà bản dịch mở đầu hộp này bằng: **"Nhất nghệ tinh, nhất thân vinh."**

💼 Ví dụ hiện đại mà sách nêu: xây nhà. *"hầu hết mọi người sẽ tìm nhà thầu xây dựng: người đó sẽ đi
thuê thợ mộc, thợ ống nước, thợ điện, thợ sơn"* — chuyên môn hoá vẫn là lý do chính khiến xã hội hiện
đại thịnh vượng.

---

## 10. 💼 Ba con số, ba câu hỏi — và cái bẫy định giá theo chi phí

Chương này cho bạn **ba con số**, và chúng trả lời **ba câu hỏi khác nhau**. Nhầm lẫn giữa chúng là
sai lầm định giá phổ biến nhất trong thực tế.

| Con số | Trả lời câu hỏi | Học ở |
| --- | --- | --- |
| **Chi phí biên (MC)** | *"Giá sàn tuyệt đối của tôi là bao nhiêu?"* — dưới mức này thì không bao giờ bán | [bài 1, mục 4](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#4-nguyên-lý-3--con-người-duy-lý-suy-nghĩ-tại-điểm-cận-biên) |
| **ATC tại sản lượng kế hoạch** | *"Bán giá nào thì hoà vốn ở sản lượng đó?"* | mục 6 |
| **Quy mô hiệu quả** | *"Nếu chọn được, tôi nên nhắm sản lượng nào?"* | mục 7 |

⚠️ **Không con nào trong ba con số trên trả lời câu hỏi "nên bán giá bao nhiêu".** Câu đó cần thêm
**đường cầu** ([bài 3](bai_03_do_co_gian_va_dinh_gia.md)) và quy tắc **MR = MC** (bài 6, bài 7).

### Cái bẫy cost-plus pricing

Cách định giá phổ biến nhất trong doanh nghiệp: *"lấy chi phí bình quân cộng thêm 20% lợi nhuận"*.
Nghe hợp lý. Nhưng nó **vòng tròn**:

```
   ATC phụ thuộc SẢN LƯỢNG   (vì ATC = FC/Q + AVC)
        │
   SẢN LƯỢNG phụ thuộc GIÁ   (đường cầu, bài 3)
        │
   GIÁ được đặt từ ATC       ← quay lại đầu
```

Và vòng này **chạy sai hướng khi cầu yếu**: bán ít → ATC cao → cost-plus đòi tăng giá → bán ít hơn nữa
→ ATC cao hơn nữa. Mục 12 in ra ba mức giá cost-plus khác nhau cho **cùng một doanh nghiệp**, chỉ khác
giả định sản lượng — từ 42k đến 66k.

### Điểm hoà vốn và độ nguy hiểm của chi phí cố định

$$\text{Điểm hoà vốn} = \frac{\text{Chi phí cố định}}{\text{Giá bán} - \text{Biến phí}}$$

Mẫu số $(P - AVC)$ chính là **phần đóng góp** mỗi đơn vị. Mục 12 cho thấy: giữ nguyên giá và biến phí,
**chi phí cố định gấp đôi thì điểm hoà vốn gấp đôi**.

⭐ **Hệ quả quản trị:** mô hình kinh doanh nặng chi phí cố định (nhà máy riêng, cửa hàng lớn, đội xe
riêng, đội ngũ biên chế đông) có **đòn bẩy hoạt động cao** — lãi rất nhanh khi vượt hoà vốn, nhưng
**lỗ rất nhanh khi cầu sụt**, vì chi phí không co lại theo.

📌 Đây chính là **nguyên lý 10** ở [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#8-nguyên-lý-8-9-10--nền-kinh-tế-vận-hành-như-thế-nào)
(chu kỳ kinh tế) nhìn từ bên trong bảng cân đối của một doanh nghiệp.

---

## 11. Bảng 3 — tóm tắt toàn bộ từ vựng chi phí

| Thuật ngữ | Định nghĩa | Công thức |
| --- | --- | --- |
| Chi phí sổ sách | chi phí đòi hỏi chi tiền ra | — |
| Chi phí ẩn | chi phí **không** đòi hỏi chi tiền ra | — |
| Chi phí cố định (FC) | không đổi theo sản lượng | — |
| Chi phí biến đổi (VC) | thay đổi theo sản lượng | — |
| Tổng chi phí (TC) | giá trị thị trường mọi đầu vào | $TC = FC + VC$ |
| Chi phí cố định bình quân (AFC) | chi phí cố định trên mỗi đơn vị | $AFC = FC/Q$ |
| Chi phí biến đổi bình quân (AVC) | chi phí biến đổi trên mỗi đơn vị | $AVC = VC/Q$ |
| Tổng chi phí bình quân (ATC) | tổng chi phí trên mỗi đơn vị | $ATC = TC/Q = AFC + AVC$ |
| **Chi phí biên (MC)** | chi phí tăng thêm khi làm thêm một đơn vị | $MC = \Delta TC / \Delta Q$ |

---

## 12. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-05-chi-phi-san-xuat.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-05-chi-phi-san-xuat.py](../thuc_hanh/bai-05-chi-phi-san-xuat.py).

Tám mục. Đáng chú ý nhất:

- **Mục 3** sinh lại **toàn bộ Bảng 2 của sách** từ một công thức duy nhất $VC(Q) = 0{,}1 \cdot Q(Q+2)$,
  rồi tự đối chiếu cột ATC với bản in — **khớp 10/10 dòng**.
- **Mục 4** không chỉ nói mà **kiểm** quy tắc "MC < ATC thì ATC giảm" cho từng bước một, đánh dấu ✓
  từng dòng.
- **Mục 6–7** dựng đường ATC dài hạn **đúng theo hình của sách**: phẳng ở 10.000 đô la trong khoảng
  600–1.400 xe, dốc lên ở hai đầu.

Tiền tính bằng **xu** (chương 13) và **nghìn đồng** (góc QTKD) để mọi phép tính là số nguyên.

```python
"""Bai 5 — Chi phi san xuat (Mankiw, chuong 13).
Chay: python3 bai-05-chi-phi-san-xuat.py   (Python 3.10+, khong can cai goi nao)

Tien tinh bang XU (chuong 13) va NGHIN DONG (goc QTKD) de moi phep tinh
deu la so nguyen. Ket qua tat dinh.
"""

def usd(xu):
    return f"${xu / 100:.2f}"

# ══ 1. LOI NHUAN KE TOAN vs LOI NHUAN KINH TE — tr. 285-287 ═════════════════
print("1. LOI NHUAN KE TOAN vs LOI NHUAN KINH TE  (Nha may Banh quy bo Caroline, tr. 285-287)")
doanh_thu = 20_000          # 10.000 banh x $2
chi_phi_so_sach = 12_000    # bot, duong, chocolate, luong cong nhan... (so gia dinh)
luong_lap_trinh = 100       # $/gio ma Caroline tu bo  (tr. 285)
gio_lam_moi_nam = 40
thu_nhap_tu_bo = luong_lap_trinh * gio_lam_moi_nam
von_tu_co = 300_000
lai_suat = 5                # phan tram
lai_tu_bo = von_tu_co * lai_suat // 100

def dong(nhan, so):
    print(f"   {nhan:<46}{so:>+10,}")

dong(f"doanh thu ({10_000:,} banh x $2)", doanh_thu)
dong("chi phi SO SACH (co dong tien di ra)", -chi_phi_so_sach)
print("   " + "─" * 56)
dong("LOI NHUAN KE TOAN", doanh_thu - chi_phi_so_sach)
print()
print("   chi phi AN — khong co dong tien nao di ra:")
dong(f"   thu nhap lap trinh tu bo (${luong_lap_trinh}/gio x {gio_lam_moi_nam} gio)", -thu_nhap_tu_bo)
dong(f"   lai tiet kiem tu bo (${von_tu_co:,} x {lai_suat}%)", -lai_tu_bo)
print("   " + "─" * 56)
ln_kinh_te = doanh_thu - chi_phi_so_sach - thu_nhap_tu_bo - lai_tu_bo
dong("LOI NHUAN KINH TE", ln_kinh_te)
print()
print("   ⚠ LOI NHUAN KE TOAN LUON LON HON LOI NHUAN KINH TE.")
print("     Ke toan bo qua chi phi AN vi khong co dong tien nao di ra.")
print(f"     O day: ke toan bao LAI {doanh_thu - chi_phi_so_sach:,}, kinh te bao "
      f"{'LAI' if ln_kinh_te > 0 else 'LO'} {abs(ln_kinh_te):,}.")
print()

# Bien the: vay ngan hang mot phan  (tr. 286)
print("   BIEN THE (tr. 286): Caroline chi co $100.000, vay ngan hang $200.000 lai 5%")
tu_co, vay = 100_000, 200_000
lai_vay = vay * lai_suat // 100
lai_tiet_kiem_tu_bo = tu_co * lai_suat // 100
print(f"      ke toan tinh : lai vay tra ngan hang            = ${lai_vay:,}")
print(f"      kinh te tinh : lai vay ${lai_vay:,} (so sach) + lai tiet kiem tu bo "
      f"${lai_tiet_kiem_tu_bo:,} (an) = ${lai_vay + lai_tiet_kiem_tu_bo:,}")
print(f"      ⭐ Chi phi co hoi cua VON van la ${lai_vay + lai_tiet_kiem_tu_bo:,} — "
      f"KHONG doi du co cau von thay doi.")
print()

# ══ 2. HAM SAN XUAT VA SAN LUONG BIEN — Bang 1, tr. 288 ═════════════════════
CHI_PHI_NHA_MAY = 30        # $/gio
CHI_PHI_MOI_CONG_NHAN = 10  # $/gio
san_luong = [0, 50, 90, 120, 140, 150, 155]     # theo so cong nhan 0..6

print("2. HAM SAN XUAT VA TONG CHI PHI — Bang 1, tr. 288")
print("   cong nhan   san luong   SL bien   chi phi nha may   chi phi nhan cong   TONG CHI PHI")
for n, q in enumerate(san_luong):
    nc = CHI_PHI_MOI_CONG_NHAN * n
    tc = CHI_PHI_NHA_MAY + nc
    bien = "" if n == 0 else f"{san_luong[n] - san_luong[n - 1]:>7}"
    print(f"   {n:>9}   {q:>9}   {bien:>7}   {CHI_PHI_NHA_MAY:>15}   {nc:>17}   {tc:>12}")
print("   ⭐ SAN LUONG BIEN GIAM DAN: 50 -> 40 -> 30 -> 20 -> 10 -> 5")
print("      Vi sao: 'nha bep tro nen chat choi', cong nhan moi phai chia se thiet bi (tr. 290)")
print("   ⟹ HAI MAT CUA MOT DONG XU:")
print("      ham san xuat cang BANG PHANG  <=>  duong tong chi phi cang DOC")
print()

# ══ 3. BANG 2 — TIEM CAFE CUA CONRAD, tr. 292 ═══════════════════════════════
# Doc nguoc tu bang cua sach: chi phi bien tang deu 0,20 do la moi ly
#   MC(q) = 0,10 + 0,20q   =>  chi phi bien doi VC(Q) = 0,10 x Q x (Q + 2)
FC = 300                                   # xu — chi phi co dinh
def VC(Q):  return 10 * Q * (Q + 2)        # xu
def TC(Q):  return FC + VC(Q)
def MC(Q):  return TC(Q) - TC(Q - 1)       # = 10 x (2Q + 1) xu

print("3. CAC DO LUONG CHI PHI — Tiem Cafe cua Conrad  (Bang 2, tr. 292)")
print("     Q    tong CP   CP co dinh   CP bien doi     AFC     AVC     ATC   |  CP bien")
sach_atc = {1: 330, 2: 190, 3: 150, 4: 135, 5: 130, 6: 130, 7: 133, 8: 138, 9: 143, 10: 150}
lech = 0
for Q in range(0, 11):
    if Q == 0:
        print(f"   {Q:>3}   {usd(TC(0)):>8}   {usd(FC):>10}   {usd(VC(0)):>11}"
              f"   {'—':>5}   {'—':>5}   {'—':>5}   |")
        continue
    afc, avc, atc = FC // Q, VC(Q) // Q, TC(Q) // Q
    # lam tron nhu sach: chia lay tron xuong voi AFC, con AVC/ATC chia chan
    afc = round(FC / Q); avc = round(VC(Q) / Q); atc = round(TC(Q) / Q)
    if atc != sach_atc[Q]:
        lech += 1
    print(f"   {Q:>3}   {usd(TC(Q)):>8}   {usd(FC):>10}   {usd(VC(Q)):>11}"
          f"   {usd(afc):>5}   {usd(avc):>5}   {usd(atc):>5}   |  {usd(MC(Q)):>6}")
print(f"   Doi chieu cot ATC voi ban in tr. 292: {10 - lech}/10 dong khop, {lech} dong lech")
print("   ⭐ Cong thuc:  ATC = TC / Q        MC = ΔTC / ΔQ")
print("      AFC = FC/Q GIAM lien tuc (chia deu cho ngay cang nhieu don vi)")
print("      AVC = VC/Q TANG dan (san luong bien giam dan)")
print("      ⟹ ATC = AFC + AVC co dang chu U")
print()

# ══ 4. QUY MO HIEU QUA VA QUAN HE MC — ATC ══════════════════════════════════
print("4. QUY MO HIEU QUA VA QUAN HE GIUA MC VOI ATC  (tr. 295-296)")
atc_theo_q = {Q: TC(Q) / Q for Q in range(1, 11)}
thap_nhat = min(atc_theo_q.values())
quy_mo = [Q for Q, v in atc_theo_q.items() if abs(v - thap_nhat) < 1e-9]
print(f"   ATC thap nhat = {usd(thap_nhat)} tai Q = {quy_mo}  ->  QUY MO HIEU QUA")
print("   (sach tr. 295: 'quy mo hieu qua la 5 hay 6 ly ca phe moi gio')")
print()
print("   Kiem quy tac: MC < ATC thi ATC GIAM; MC > ATC thi ATC TANG")
print("     Q   MC       ATC(Q-1)   so sanh   ATC(Q)    ATC dang")
for Q in range(2, 11):
    mc, atc_truoc, atc_nay = MC(Q), TC(Q - 1) / (Q - 1), TC(Q) / Q
    ss = "<" if mc < atc_truoc else (">" if mc > atc_truoc else "=")
    huong = "GIAM" if atc_nay < atc_truoc else ("TANG" if atc_nay > atc_truoc else "khong doi")
    hop_le = (ss == "<" and huong == "GIAM") or (ss == ">" and huong == "TANG") or ss == "="
    print(f"   {Q:>3}   {usd(mc):>6}   {usd(atc_truoc):>8}      {ss}      "
          f"{usd(atc_nay):>6}    {huong}   {'✓' if hop_le else '✗'}")
print("   ⭐ HE QUA: duong MC cat duong ATC DUNG TAI DIEM THAP NHAT cua ATC.")
print(f"      Kiem: MC(6) = {usd(MC(6))} va ATC(6) = {usd(TC(6) / 6)}  ->  bang nhau: "
      f"{MC(6) == TC(6) // 6}")
print("   💡 Vi du cua sach: ATC giong DIEM TRUNG BINH TICH LUY, MC giong DIEM MON HOC")
print("      TIEP THEO. Diem mon moi thap hon trung binh thi keo trung binh xuong.")
print()

# ══ 5. VE BON DUONG CHI PHI — Hinh 4, tr. 294 ═══════════════════════════════
print("5. BON DUONG CHI PHI CUA CONRAD  (Hinh 4, tr. 294)")
CAO, RONG = 18, 46
tran = 360          # xu
luoi = [[" "] * RONG for _ in range(CAO)]
def ve_duong(ham, ky):
    """Noi cac diem Q = 1..10 bang noi suy tuyen tinh de duong lien mach."""
    for i in range(RONG):
        Q = 1 + 9 * i / (RONG - 1)
        lo, hi = int(Q), min(int(Q) + 1, 10)
        t = Q - lo
        v = ham(lo) * (1 - t) + ham(hi) * t
        if not (0 <= v <= tran):
            continue
        r = CAO - 1 - round(v / tran * (CAO - 1))
        if luoi[r][i] == " ":
            luoi[r][i] = ky
for ham, ky in [(lambda q: FC / q, "f"), (lambda q: VC(q) / q, "v"),
                (lambda q: TC(q) / q, "A"), (lambda q: MC(q), "M")]:
    ve_duong(ham, ky)
print("      chi phi")
for i, hang in enumerate(luoi):
    v = tran - round(i * tran / (CAO - 1))
    nhan = f"{usd(v):>6}" if i % 3 == 0 else "      "
    print(f"      {nhan} │{''.join(hang)}".rstrip())
print("             └" + "─" * RONG)
print("              1" + " " * (RONG - 4) + "10  so ly ca phe")
print("      A = ATC (tong CP binh quan)   v = AVC (CP bien doi bq)")
print("      f = AFC (CP co dinh bq)       M = MC  (chi phi bien)")
print("      ⭐ M cat A tai day chu U cua A. f giam mai, khong bao gio cham 0.")
print()

# ══ 6. NGAN HAN vs DAI HAN — Hinh 6, tr. 298 ════════════════════════════════
# Duong ATC DAI HAN dung theo hinh cua sach: PHANG o $10.000 trong khoang
# 600-1.400 xe (loi the theo quy mo KHONG DOI), doc len o hai dau.
def atc_dai_han(Q):
    if Q < 600:
        return 10_000 + (600 - Q) ** 2 // 20
    if Q > 1400:
        return 10_000 + (Q - 1400) ** 2 // 20
    return 10_000

# ATC NGAN HAN cua mot nha may cong suat K: cham duong dai han tai Q = K,
# nam TREN no o moi noi khac (nha may cang sai co thi cang dat).
def atc_ngan_han(Q, K):
    return atc_dai_han(K) + (Q - K) ** 2 // 20

print("6. NGAN HAN vs DAI HAN — vi du Ford  (Hinh 6, tr. 298)")
print("   ba nha may: quy mo NHO (600 xe), TRUNG BINH (1.000), LON (1.400)")
print("     san luong   nha may nho   trung binh   nha may lon   ATC DAI HAN")
for Q in (600, 800, 1000, 1200, 1400):
    o = "   ".join(f"{atc_ngan_han(Q, K):>10,}" for K in (600, 1000, 1400))
    print(f"   {Q:>9,}   {o}   {atc_dai_han(Q):>10,}")
print("   (ba nha may tren chi la BA VI DU. Trong dai han doanh nghiep chon duoc")
print("    BAT KY quy mo nao, nen duong dai han la duong bao duoi cua VO SO duong ngan han.)")
print()
print("   ⭐ Cau chuyen cua sach (tr. 298):")
print(f"      Ford dang o 1.000 xe/ngay, ATC = ${atc_ngan_han(1000, 1000):,}")
print(f"      Muon len 1.200 xe. NGAN HAN chi thue them cong nhan o nha may cu:")
print(f"         ATC = ${atc_ngan_han(1200, 1000):,}  (tang ${atc_ngan_han(1200, 1000) - 10_000:,})")
print(f"      DAI HAN xay duoc nha may dung co cho 1.200 xe:")
print(f"         ATC = ${10_000:,}  (ve lai muc cu)")
print("   ⟹ MOI DUONG NGAN HAN DEU NAM TREN hoac CHAM duong dai han.")
print("      Dai han LINH HOAT HON, nen khong bao gio dat hon ngan han.")
print()
print("   ⚠ ĐINH CHINH tr. 298: sach viet 'gia tang san luong tu 1.000 len 2.000 chiec'.")
print("      Dung phai la 1.200 — chinh Hinh 6 tren cung trang danh dau 1.000 va 1.200,")
print("      va diem ATC = $12.000 nam dung tai 1.200. Ban goc tieng Anh: '1,200 cars'.")
print()

# ══ 7. LOI THE KINH TE THEO QUY MO — tr. 299 ════════════════════════════════
print("7. LOI THE / BAT LOI THE KINH TE THEO QUY MO  (tr. 299)")
print("      san luong   ATC dai han   so voi muc truoc")
truoc = None
for Q in range(200, 2001, 200):
    dh = atc_dai_han(Q)
    if truoc is None:
        nx = ""
    elif dh < truoc:
        nx = "GIAM -> loi the kinh te theo quy mo"
    elif dh > truoc:
        nx = "TANG -> bat loi the kinh te theo quy mo"
    else:
        nx = "khong doi -> loi the khong doi theo quy mo"
    print(f"   {Q:>11,}   {dh:>11,}   {nx}".rstrip())
    truoc = dh
print("   ⭐ NGUYEN NHAN (tr. 299):")
print("      loi the theo quy mo  <-  CHUYEN MON HOA  (Adam Smith, nha may dinh ghim)")
print("      bat loi the theo quy mo  <-  VAN DE PHOI HOP  ('doi ngu quan ly bi keo gian')")
print()

# ══ 8. 💼 GOC QTKD — DIEM HOA VON VA CAI BAY 'CHI PHI BINH QUAN' ════════════
print("8. 💼 GOC QTKD — TIEM BANH MI: DIEM HOA VON VA CAI BAY CHI PHI BINH QUAN")
CP_CO_DINH = 60_000        # nghin dong / thang: thue mat bang, luong quan ly, khau hao
BIEN_PHI = 25              # nghin dong / o banh
GIA_BAN = 45               # nghin dong / o banh
dong_gop = GIA_BAN - BIEN_PHI
hoa_von = CP_CO_DINH // dong_gop

print(f"   chi phi co dinh {CP_CO_DINH:,}k/thang · bien phi {BIEN_PHI}k/o · gia ban {GIA_BAN}k/o")
print(f"   dong gop moi o = {GIA_BAN} - {BIEN_PHI} = {dong_gop}k")
print(f"   ⭐ DIEM HOA VON = {CP_CO_DINH:,} / {dong_gop} = {hoa_von:,} o/thang")
print()
print("     san luong   tong chi phi   ATC (k/o)   doanh thu   loi nhuan")
for Q in (1000, 2000, hoa_von, 4000, 6000, 8000):
    tc = CP_CO_DINH + BIEN_PHI * Q
    atc = tc / Q
    dt = GIA_BAN * Q
    dau = "  <-- HOA VON" if Q == hoa_von else ""
    print(f"   {Q:>11,}   {tc:>12,}   {atc:>9.1f}   {dt:>9,}   {dt - tc:>+9,}{dau}")
print()
print("   ⚠ CAI BAY 'DINH GIA THEO CHI PHI BINH QUAN' (cost-plus):")
print("      Ban muon lai 20% tren chi phi binh quan. Nhung ATC bao nhieu?")
for Q in (2000, 3000, 6000):
    atc = (CP_CO_DINH + BIEN_PHI * Q) / Q
    print(f"         o {Q:,} o/thang: ATC = {atc:.1f}k  ->  gia = {atc * 1.2:.1f}k")
print("      ⟹ Gia phu thuoc SAN LUONG, ma san luong lai phu thuoc GIA. LAP LUAN VONG TRON.")
print("      Ban cang dat gia cao thi ban cang it, ATC cang cao, lai doi tang gia tiep...")
print("      Do la 'vong xoay tu huy' cua cost-plus pricing.")
print()
print("   ⭐ BA CON SO, BA CAU HOI KHAC NHAU:")
print(f"      BIEN PHI {BIEN_PHI}k        -> gia SAN tuyet doi. Duoi muc nay khong bao gio ban.")
print(f"                            (bai 1 muc 4: quyet dinh nhan don hang le)")
print(f"      ATC tai san luong ke hoach -> muc gia de HOA VON o san luong do")
print(f"      QUY MO HIEU QUA            -> san luong nen nham toi neu chon duoc")
print("      ⚠ Khong con nao trong ba con so tren tra loi 'nen ban gia bao nhieu'.")
print("        Cau tra loi do can them DUONG CAU (bai 3) va quy tac MR = MC (bai 6, 7).")
print()
print("   💼 CHI PHI CO DINH CANG LON THI DIEM HOA VON CANG XA:")
for cp in (30_000, 60_000, 120_000):
    print(f"      chi phi co dinh {cp:>7,}k  ->  hoa von {cp // dong_gop:>6,} o/thang")
print("      ⟹ Mo hinh nhieu chi phi co dinh (nha may, cua hang lon, doi xe rieng)")
print("        RAT NGUY HIEM khi cau sut — dung nguyen ly 10 o bai 1.")
```

**Kết quả chạy thật:**

```
1. LOI NHUAN KE TOAN vs LOI NHUAN KINH TE  (Nha may Banh quy bo Caroline, tr. 285-287)
   doanh thu (10,000 banh x $2)                     +20,000
   chi phi SO SACH (co dong tien di ra)             -12,000
   ────────────────────────────────────────────────────────
   LOI NHUAN KE TOAN                                 +8,000

   chi phi AN — khong co dong tien nao di ra:
      thu nhap lap trinh tu bo ($100/gio x 40 gio)    -4,000
      lai tiet kiem tu bo ($300,000 x 5%)           -15,000
   ────────────────────────────────────────────────────────
   LOI NHUAN KINH TE                                -11,000

   ⚠ LOI NHUAN KE TOAN LUON LON HON LOI NHUAN KINH TE.
     Ke toan bo qua chi phi AN vi khong co dong tien nao di ra.
     O day: ke toan bao LAI 8,000, kinh te bao LO 11,000.

   BIEN THE (tr. 286): Caroline chi co $100.000, vay ngan hang $200.000 lai 5%
      ke toan tinh : lai vay tra ngan hang            = $10,000
      kinh te tinh : lai vay $10,000 (so sach) + lai tiet kiem tu bo $5,000 (an) = $15,000
      ⭐ Chi phi co hoi cua VON van la $15,000 — KHONG doi du co cau von thay doi.

2. HAM SAN XUAT VA TONG CHI PHI — Bang 1, tr. 288
   cong nhan   san luong   SL bien   chi phi nha may   chi phi nhan cong   TONG CHI PHI
           0           0                          30                   0             30
           1          50        50                30                  10             40
           2          90        40                30                  20             50
           3         120        30                30                  30             60
           4         140        20                30                  40             70
           5         150        10                30                  50             80
           6         155         5                30                  60             90
   ⭐ SAN LUONG BIEN GIAM DAN: 50 -> 40 -> 30 -> 20 -> 10 -> 5
      Vi sao: 'nha bep tro nen chat choi', cong nhan moi phai chia se thiet bi (tr. 290)
   ⟹ HAI MAT CUA MOT DONG XU:
      ham san xuat cang BANG PHANG  <=>  duong tong chi phi cang DOC

3. CAC DO LUONG CHI PHI — Tiem Cafe cua Conrad  (Bang 2, tr. 292)
     Q    tong CP   CP co dinh   CP bien doi     AFC     AVC     ATC   |  CP bien
     0      $3.00        $3.00         $0.00       —       —       —   |
     1      $3.30        $3.00         $0.30   $3.00   $0.30   $3.30   |   $0.30
     2      $3.80        $3.00         $0.80   $1.50   $0.40   $1.90   |   $0.50
     3      $4.50        $3.00         $1.50   $1.00   $0.50   $1.50   |   $0.70
     4      $5.40        $3.00         $2.40   $0.75   $0.60   $1.35   |   $0.90
     5      $6.50        $3.00         $3.50   $0.60   $0.70   $1.30   |   $1.10
     6      $7.80        $3.00         $4.80   $0.50   $0.80   $1.30   |   $1.30
     7      $9.30        $3.00         $6.30   $0.43   $0.90   $1.33   |   $1.50
     8     $11.00        $3.00         $8.00   $0.38   $1.00   $1.38   |   $1.70
     9     $12.90        $3.00         $9.90   $0.33   $1.10   $1.43   |   $1.90
    10     $15.00        $3.00        $12.00   $0.30   $1.20   $1.50   |   $2.10
   Doi chieu cot ATC voi ban in tr. 292: 10/10 dong khop, 0 dong lech
   ⭐ Cong thuc:  ATC = TC / Q        MC = ΔTC / ΔQ
      AFC = FC/Q GIAM lien tuc (chia deu cho ngay cang nhieu don vi)
      AVC = VC/Q TANG dan (san luong bien giam dan)
      ⟹ ATC = AFC + AVC co dang chu U

4. QUY MO HIEU QUA VA QUAN HE GIUA MC VOI ATC  (tr. 295-296)
   ATC thap nhat = $1.30 tai Q = [5, 6]  ->  QUY MO HIEU QUA
   (sach tr. 295: 'quy mo hieu qua la 5 hay 6 ly ca phe moi gio')

   Kiem quy tac: MC < ATC thi ATC GIAM; MC > ATC thi ATC TANG
     Q   MC       ATC(Q-1)   so sanh   ATC(Q)    ATC dang
     2    $0.50      $3.30      <       $1.90    GIAM   ✓
     3    $0.70      $1.90      <       $1.50    GIAM   ✓
     4    $0.90      $1.50      <       $1.35    GIAM   ✓
     5    $1.10      $1.35      <       $1.30    GIAM   ✓
     6    $1.30      $1.30      =       $1.30    khong doi   ✓
     7    $1.50      $1.30      >       $1.33    TANG   ✓
     8    $1.70      $1.33      >       $1.38    TANG   ✓
     9    $1.90      $1.38      >       $1.43    TANG   ✓
    10    $2.10      $1.43      >       $1.50    TANG   ✓
   ⭐ HE QUA: duong MC cat duong ATC DUNG TAI DIEM THAP NHAT cua ATC.
      Kiem: MC(6) = $1.30 va ATC(6) = $1.30  ->  bang nhau: True
   💡 Vi du cua sach: ATC giong DIEM TRUNG BINH TICH LUY, MC giong DIEM MON HOC
      TIEP THEO. Diem mon moi thap hon trung binh thi keo trung binh xuong.

5. BON DUONG CHI PHI CUA CONRAD  (Hinh 4, tr. 294)
      chi phi
       $3.60 │
             │A
             │
       $2.96 │fA
             │ fA
             │   A
       $2.33 │  f
             │   fA                                      MMM
             │     AA                               MMMMM
       $1.69 │    f  AA                        MMMMM
             │     ff  AAAAAA            MMMMMM   AAAAAAAAAA
             │       ff      AAAAAAAAAAAAAAAAAAAAA        vv
       $1.06 │         ff      MMMMM           vvvvvvvvvvv
             │           fffffM      vvvvvvvvvv
             │      MMMMMMvvvvffffffff
       $0.42 │ vvvvvvvvvvv            fffffffffffffffffff
             │v                                          fff
             │
             └──────────────────────────────────────────────
              1                                          10  so ly ca phe
      A = ATC (tong CP binh quan)   v = AVC (CP bien doi bq)
      f = AFC (CP co dinh bq)       M = MC  (chi phi bien)
      ⭐ M cat A tai day chu U cua A. f giam mai, khong bao gio cham 0.

6. NGAN HAN vs DAI HAN — vi du Ford  (Hinh 6, tr. 298)
   ba nha may: quy mo NHO (600 xe), TRUNG BINH (1.000), LON (1.400)
     san luong   nha may nho   trung binh   nha may lon   ATC DAI HAN
         600       10,000       18,000       42,000       10,000
         800       12,000       12,000       28,000       10,000
       1,000       18,000       10,000       18,000       10,000
       1,200       28,000       12,000       12,000       10,000
       1,400       42,000       18,000       10,000       10,000
   (ba nha may tren chi la BA VI DU. Trong dai han doanh nghiep chon duoc
    BAT KY quy mo nao, nen duong dai han la duong bao duoi cua VO SO duong ngan han.)

   ⭐ Cau chuyen cua sach (tr. 298):
      Ford dang o 1.000 xe/ngay, ATC = $10,000
      Muon len 1.200 xe. NGAN HAN chi thue them cong nhan o nha may cu:
         ATC = $12,000  (tang $2,000)
      DAI HAN xay duoc nha may dung co cho 1.200 xe:
         ATC = $10,000  (ve lai muc cu)
   ⟹ MOI DUONG NGAN HAN DEU NAM TREN hoac CHAM duong dai han.
      Dai han LINH HOAT HON, nen khong bao gio dat hon ngan han.

   ⚠ ĐINH CHINH tr. 298: sach viet 'gia tang san luong tu 1.000 len 2.000 chiec'.
      Dung phai la 1.200 — chinh Hinh 6 tren cung trang danh dau 1.000 va 1.200,
      va diem ATC = $12.000 nam dung tai 1.200. Ban goc tieng Anh: '1,200 cars'.

7. LOI THE / BAT LOI THE KINH TE THEO QUY MO  (tr. 299)
      san luong   ATC dai han   so voi muc truoc
           200        18,000
           400        12,000   GIAM -> loi the kinh te theo quy mo
           600        10,000   GIAM -> loi the kinh te theo quy mo
           800        10,000   khong doi -> loi the khong doi theo quy mo
         1,000        10,000   khong doi -> loi the khong doi theo quy mo
         1,200        10,000   khong doi -> loi the khong doi theo quy mo
         1,400        10,000   khong doi -> loi the khong doi theo quy mo
         1,600        12,000   TANG -> bat loi the kinh te theo quy mo
         1,800        18,000   TANG -> bat loi the kinh te theo quy mo
         2,000        28,000   TANG -> bat loi the kinh te theo quy mo
   ⭐ NGUYEN NHAN (tr. 299):
      loi the theo quy mo  <-  CHUYEN MON HOA  (Adam Smith, nha may dinh ghim)
      bat loi the theo quy mo  <-  VAN DE PHOI HOP  ('doi ngu quan ly bi keo gian')

8. 💼 GOC QTKD — TIEM BANH MI: DIEM HOA VON VA CAI BAY CHI PHI BINH QUAN
   chi phi co dinh 60,000k/thang · bien phi 25k/o · gia ban 45k/o
   dong gop moi o = 45 - 25 = 20k
   ⭐ DIEM HOA VON = 60,000 / 20 = 3,000 o/thang

     san luong   tong chi phi   ATC (k/o)   doanh thu   loi nhuan
         1,000         85,000        85.0      45,000     -40,000
         2,000        110,000        55.0      90,000     -20,000
         3,000        135,000        45.0     135,000          +0  <-- HOA VON
         4,000        160,000        40.0     180,000     +20,000
         6,000        210,000        35.0     270,000     +60,000
         8,000        260,000        32.5     360,000    +100,000

   ⚠ CAI BAY 'DINH GIA THEO CHI PHI BINH QUAN' (cost-plus):
      Ban muon lai 20% tren chi phi binh quan. Nhung ATC bao nhieu?
         o 2,000 o/thang: ATC = 55.0k  ->  gia = 66.0k
         o 3,000 o/thang: ATC = 45.0k  ->  gia = 54.0k
         o 6,000 o/thang: ATC = 35.0k  ->  gia = 42.0k
      ⟹ Gia phu thuoc SAN LUONG, ma san luong lai phu thuoc GIA. LAP LUAN VONG TRON.
      Ban cang dat gia cao thi ban cang it, ATC cang cao, lai doi tang gia tiep...
      Do la 'vong xoay tu huy' cua cost-plus pricing.

   ⭐ BA CON SO, BA CAU HOI KHAC NHAU:
      BIEN PHI 25k        -> gia SAN tuyet doi. Duoi muc nay khong bao gio ban.
                            (bai 1 muc 4: quyet dinh nhan don hang le)
      ATC tai san luong ke hoach -> muc gia de HOA VON o san luong do
      QUY MO HIEU QUA            -> san luong nen nham toi neu chon duoc
      ⚠ Khong con nao trong ba con so tren tra loi 'nen ban gia bao nhieu'.
        Cau tra loi do can them DUONG CAU (bai 3) va quy tac MR = MC (bai 6, 7).

   💼 CHI PHI CO DINH CANG LON THI DIEM HOA VON CANG XA:
      chi phi co dinh  30,000k  ->  hoa von  1,500 o/thang
      chi phi co dinh  60,000k  ->  hoa von  3,000 o/thang
      chi phi co dinh 120,000k  ->  hoa von  6,000 o/thang
      ⟹ Mo hinh nhieu chi phi co dinh (nha may, cua hang lon, doi xe rieng)
        RAT NGUY HIEM khi cau sut — dung nguyen ly 10 o bai 1.
```

### Đọc kết quả

**① Kế toán và kinh tế (mục 1).** Cùng một doanh nghiệp: kế toán báo **lãi 8.000**, nhà kinh tế báo
**lỗ 11.000**. Chênh lệch 19.000 là hai khoản ẩn — thu nhập lập trình từ bỏ và lãi tiết kiệm từ bỏ.
Biến thể vay ngân hàng cho thấy chi phí cơ hội của vốn **vẫn là 15.000** dù cơ cấu vốn đổi.

**② Sản lượng biên (mục 2).** 50 → 40 → 30 → 20 → 10 → 5. Mỗi công nhân thêm đóng góp ít hơn người
trước. Cột tổng chi phí tăng đều 10 đô la mỗi bước **nhưng sản lượng tăng ít dần** — đó chính là lý do
đường tổng chi phí dốc lên.

**③ Bảng Conrad (mục 3).** Dòng cuối in `10/10 dong khop, 0 dong lech`. Bảng của sách được sinh lại
hoàn toàn từ công thức, không gõ tay số nào.

**④ Quy tắc MC–ATC (mục 4).** Chín dòng, chín dấu ✓. Chú ý dòng $Q = 6$: MC = ATC(5) = **1,30** và
ATC(6) cũng **1,30** — đó là **giao điểm**, và nó rơi đúng vào **quy mô hiệu quả**.

**⑤ Bốn đường (mục 5).** `f` (AFC) rơi từ trên xuống nhưng **không bao giờ chạm 0**. `v` (AVC) đi lên
đều. `A` (ATC) là tổng hai đường ấy — chữ U. `M` (MC) là đường dốc nhất, cắt `A` ở đáy.

**⑥ Ngắn hạn / dài hạn (mục 6).** Đọc theo hàng: ở mỗi mức sản lượng, **cột ATC dài hạn luôn ≤ mọi cột
ngắn hạn**. Ở $Q = 800$ cả ba nhà máy đều cho 12.000 nhưng dài hạn cho 10.000 — vì trong dài hạn xây
được nhà máy **đúng cỡ 800**.

**⑦ Kinh tế theo quy mô (mục 7).** Ba giai đoạn hiện rõ: **giảm** (200 → 600), **không đổi**
(600 → 1.400), **tăng** (1.600 → 2.000) — đúng ba nhãn trong Hình 6.

**⑧ Góc QTKD (mục 8).** Điểm hoà vốn 3.000 ổ/tháng. Bảng cost-plus cho **ba mức giá khác nhau**
(66k / 54k / 42k) cho **cùng một tiệm bánh** — chỉ khác giả định sản lượng. Và bảng cuối: chi phí cố
định 30k → 60k → 120k đẩy điểm hoà vốn 1.500 → 3.000 → 6.000 ổ.

---

## 13. Tự thử

Sửa tham số rồi chạy lại. Không có lời giải kèm theo.

1. Trong mục 1, đổi `luong_lap_trinh = 100` thành `500` (đúng tình huống sách nêu ở tr. 286). Lợi
   nhuận kinh tế bằng bao nhiêu? Caroline nên tiếp tục làm bánh không? Lợi nhuận **kế toán** có đổi không?
2. Trong mục 3, đổi `FC = 300` thành `FC = 600` (tiền thuê mặt bằng tăng gấp đôi). Quy mô hiệu quả dịch
   sang trái hay phải? Chi phí biên có đổi không? Vì sao?
3. Trong mục 3, đổi `VC(Q)` thành `20 * Q * (Q + 2)` (mọi chi phí biến đổi gấp đôi). ATC thấp nhất là
   bao nhiêu và ở sản lượng nào? So với câu 2 — **chi phí cố định** và **chi phí biến đổi** dịch quy mô
   hiệu quả theo hai hướng ngược nhau, đúng không?
4. Trong mục 6, thêm nhà máy `K = 800` vào danh sách `(600, 1000, 1400)`. Nó có làm cột "ATC dài hạn"
   thay đổi không? Giải thích bằng ý *"đường dài hạn là đường bao dưới"*.
5. Trong mục 8, đổi `GIA_BAN = 45` thành `35`. Điểm hoà vốn mới là bao nhiêu? Tăng bao nhiêu phần trăm
   trong khi giá chỉ giảm 22%? Bạn vừa tìm ra vì sao **giảm giá nguy hiểm với mô hình nhiều chi phí cố định**.

---

## 14. Từ điển thuật ngữ

Cột tiếng Anh lấy từ mục **Khái niệm then chốt** của sách (tr. 302).

| Tiếng Việt | Tiếng Anh | Ghi chú |
| --- | --- | --- |
| Tổng doanh thu | Total revenue | tr. 284 |
| Tổng chi phí | Total cost | tr. 284 |
| Lợi nhuận | Profit | tr. 284 — doanh thu trừ chi phí |
| Chi phí sổ sách | Explicit costs | tr. 285 — **có** dòng tiền ra |
| Chi phí ẩn | Implicit costs | tr. 285 — **không** có dòng tiền ra |
| Lợi nhuận kinh tế | Economic profit | tr. 286 — trừ **cả** chi phí ẩn |
| Lợi nhuận kế toán | Accounting profit | tr. 287 — **luôn lớn hơn** lợi nhuận kinh tế |
| Hàm sản xuất | Production function | tr. 288 |
| Sản lượng biên | Marginal product | tr. 289 |
| Sản lượng biên giảm dần | Diminishing marginal product | tr. 290 — nguồn gốc của mọi hình dạng đường chi phí |
| Chi phí cố định | Fixed costs | tr. 292 |
| Chi phí biến đổi | Variable costs | tr. 292 |
| Tổng chi phí bình quân | Average total cost | tr. 293 — $TC/Q$ |
| Chi phí cố định bình quân | Average fixed cost | tr. 293 — giảm mãi |
| Chi phí biến đổi bình quân | Average variable cost | tr. 293 |
| Chi phí biên | Marginal cost | tr. 293 — $\Delta TC/\Delta Q$ |
| Quy mô hiệu quả | Efficient scale | tr. 295 — đáy chữ U |
| Lợi thế kinh tế theo quy mô | Economies of scale | tr. 299 — do **chuyên môn hoá** |
| Bất lợi thế kinh tế theo quy mô | Diseconomies of scale | tr. 299 — do **vấn đề phối hợp** |
| Lợi thế không đổi theo quy mô | Constant returns to scale | tr. 299 |

---

## 15. Câu hỏi tự kiểm tra

1. Ông McDonald dạy đàn banjo giá 20 đô la mỗi giờ. Một ngày nọ ông bỏ ra **10 giờ** trồng cây với hạt
   giống trị giá **100 đô la**. Chi phí cơ hội của ông là bao nhiêu? Kế toán ghi nhận bao nhiêu? Nếu vụ
   mùa thu được **200 đô la**, ông có lợi nhuận kế toán không? Lợi nhuận kinh tế thì sao?
   *(Kiểm tra nhanh của sách, tr. 287)*
2. Vì sao lợi nhuận kế toán **luôn** lớn hơn lợi nhuận kinh tế? Trong trường hợp nào hai con số bằng nhau?
3. "Lợi nhuận kinh tế bằng 0" có nghĩa là doanh nghiệp đang làm không công không? Giải thích.
4. Caroline mua nhà máy bằng 300.000 đô la tiền túi. Bạn của cô mua nhà máy y hệt bằng tiền vay 100%.
   Chi phí cơ hội của vốn của hai người có khác nhau không? Kế toán ghi nhận có khác nhau không?
5. Vì sao hàm sản xuất càng bằng phẳng thì đường tổng chi phí càng dốc? Nêu cơ chế, không chỉ nêu kết luận.
6. Tổng chi phí sản xuất 4 xe của Honda là 225.000 đô la, sản xuất 5 xe là 250.000 đô la. Tính ATC của
   5 xe và MC của chiếc thứ 5. *(Kiểm tra nhanh của sách, tr. 297)*
7. Vì sao đường ATC có dạng chữ U? Chỉ ra **hai lực** đối nghịch tạo nên hình dạng đó.
8. Chứng minh (bằng lời) rằng đường MC **phải** cắt đường ATC tại điểm thấp nhất của ATC.
9. Boeing sản xuất 9 chiếc phản lực mỗi tháng với tổng chi phí dài hạn 9 triệu đô la; sản xuất 10 chiếc
   thì 9,5 triệu. Boeing có lợi thế hay bất lợi thế theo quy mô? *(Kiểm tra nhanh của sách, tr. 300)*
10. Một tiệm bánh có chi phí cố định 60 triệu/tháng, biến phí 25 nghìn/ổ, bán 45 nghìn/ổ. Chủ tiệm muốn
    "lãi 20% trên chi phí bình quân". Chỉ ra vì sao quy tắc này **không xác định được một mức giá duy nhất**.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 5 — CHI PHÍ SẢN XUẤT                       (Ch. 13, tr. 283–307)    ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Mục tiêu doanh nghiệp: TỐI ĐA HOÁ LỢI NHUẬN = doanh thu − chi phí       ║
║                                                                          ║
║  ── CHI PHÍ LÀ CHI PHÍ CƠ HỘI ──────────────────────────────────────     ║
║      SỔ SÁCH  có dòng tiền ra    | ẨN  không có dòng tiền ra             ║
║      LỢI NHUẬN KẾ TOÁN = DT − chi phí SỔ SÁCH                            ║
║      LỢI NHUẬN KINH TẾ = DT − chi phí SỔ SÁCH − chi phí ẨN               ║
║      ⭐ kế toán LUÔN lớn hơn kinh tế                                      ║
║      ⚠ "lợi nhuận kinh tế = 0" KHÔNG phải làm không công — mà là         ║
║        kiếm ĐÚNG BẰNG phương án tốt nhất kế tiếp                         ║
║      ⭐ chi phí cơ hội của VỐN không đổi theo cơ cấu vốn                  ║
║        ($300k tự có hay vay 200k: vẫn là $15.000)                        ║
║                                                                          ║
║  ── NGUỒN GỐC CỦA MỌI ĐƯỜNG CHI PHÍ ────────────────────────────────     ║
║      SẢN LƯỢNG BIÊN GIẢM DẦN  50→40→30→20→10→5                           ║
║        (nhà bếp chật, công nhân chia nhau thiết bị)                      ║
║      ⟹ hàm sản xuất BẰNG PHẲNG dần ⟺ tổng chi phí DỐC dần                ║
║                                                                          ║
║  ── BỐN THƯỚC ĐO ───────────────────────────────────────────────────     ║
║      TC = FC + VC                                                        ║
║      AFC = FC/Q   giảm mãi, không bao giờ chạm 0                         ║
║      AVC = VC/Q   tăng dần                                               ║
║      ATC = TC/Q = AFC + AVC   ⟹  hình chữ U                              ║
║      MC  = ΔTC/ΔQ   nằm GIỮA hai dòng, thuộc về BƯỚC ĐI                  ║
║                                                                          ║
║  ⭐⭐ BA ĐẶC ĐIỂM CỦA MỌI ĐƯỜNG CHI PHÍ                                    ║
║      ① MC sớm muộn cũng TĂNG                                             ║
║      ② ATC hình chữ U — đáy gọi là QUY MÔ HIỆU QUẢ                       ║
║      ③ MC cắt ATC ĐÚNG TẠI ĐÁY chữ U                                     ║
║      MC < ATC ⟹ ATC đang GIẢM  |  MC > ATC ⟹ ATC đang TĂNG               ║
║      💡 ATC = điểm trung bình tích luỹ; MC = điểm môn học kế tiếp        ║
║                                                                          ║
║  ── NGẮN HẠN vs DÀI HẠN ────────────────────────────────────────────     ║
║      ranh giới cố định/biến đổi là ranh giới THỜI GIAN                   ║
║      MỌI đường ngắn hạn NẰM TRÊN hoặc CHẠM đường dài hạn                 ║
║      Ford: 1.000→1.200 xe, ngắn hạn ATC $10.000→$12.000                  ║
║            dài hạn xây nhà máy đúng cỡ → về lại $10.000                  ║
║      ⚠ ĐÍNH CHÍNH tr. 298: sách in "2.000", đúng là "1.200"              ║
║                                                                          ║
║  ── KINH TẾ THEO QUY MÔ ────────────────────────────────────────────     ║
║      LỢI THẾ (ATC dài hạn giảm)  ← CHUYÊN MÔN HOÁ (Adam Smith, đinh ghim)║
║      BẤT LỢI (ATC dài hạn tăng)  ← VẤN ĐỀ PHỐI HỢP                       ║
║      KHÔNG ĐỔI ở khoảng giữa                                             ║
║                                                                          ║
║  💼 QTKD  BA CON SỐ, BA CÂU HỎI KHÁC NHAU                                ║
║      MC   → giá SÀN tuyệt đối, dưới mức này không bao giờ bán            ║
║      ATC  → giá HOÀ VỐN tại một sản lượng cụ thể                         ║
║      quy mô hiệu quả → sản lượng nên nhắm tới                            ║
║      ⚠ KHÔNG con nào trả lời "nên bán giá bao nhiêu"                     ║
║        cần thêm ĐƯỜNG CẦU (bài 3) và MR = MC (bài 6, 7)                  ║
║      ⚠ COST-PLUS LÀ LẬP LUẬN VÒNG TRÒN: ATC phụ thuộc sản lượng,         ║
║        sản lượng phụ thuộc giá, giá lại đặt từ ATC                       ║
║        cầu yếu → bán ít → ATC cao → tăng giá → bán ít hơn nữa            ║
║      ĐIỂM HOÀ VỐN = chi phí cố định / (giá − biến phí)                   ║
║        chi phí cố định gấp đôi ⟹ điểm hoà vốn gấp đôi                    ║
║        ⟹ mô hình nặng chi phí cố định rất nguy hiểm khi cầu sụt          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **N. Gregory Mankiw, *Kinh tế học vi mô*** — bản dịch của Khoa Kinh tế, Trường ĐH Kinh tế TP.HCM,
  Cengage Learning Asia. Tệp trong kho: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  — **trang sách N = trang PDF N + 33**.
  - **Chương 13 — Chi phí sản xuất**, tr. 283–307
    - *Tổng doanh thu, tổng chi phí và lợi nhuận*, tr. 284
    - *Chi phí tính bằng chi phí cơ hội*, tr. 285
    - *Chi phí sử dụng vốn được xem như là một loại chi phí cơ hội*, tr. 286
    - Hình 1 *Thị trường nhôm* — lợi nhuận kinh tế và lợi nhuận kế toán, tr. 287
    - Bảng 1 *Hàm sản xuất và Tổng chi phí — Nhà máy Bánh quy bơ của Caroline*, tr. 288
    - Hình 2 *Hàm sản xuất và Đường tổng chi phí của Caroline*, tr. 289
    - Hình 3 *Đường Tổng chi phí của Conrad*, tr. 291
    - Bảng 2 *Các đo lường khác nhau về chi phí: Tiệm cà phê của Conrad*, tr. 292
    - Hình 4 *Đường Chi phí bình quân và Chi phí biên của Conrad*, tr. 294
    - Hình 5 *Đường chi phí của một doanh nghiệp thông thường*, tr. 297
    - Hình 6 *Tổng chi phí bình quân trong ngắn hạn và dài hạn*, tr. 298
    - *Lợi thế và bất lợi thế kinh tế theo quy mô*, tr. 299
    - Bạn có biết *Bài học từ nhà máy sản xuất đinh ghim* (Adam Smith), tr. 300
    - Bảng 3 *Các dạng chi phí khác nhau*, tr. 301
- **Đính chính đã ghi trong bài:** tr. 298 — sách viết Ford tăng sản lượng *"từ 1.000 lên **2.000**
  chiếc"*, đúng phải là **1.200**; chính Hình 6 trên cùng trang đánh dấu 1.000 và 1.200, và điểm
  ATC = 12.000 đô la nằm đúng tại 1.200. Đối chiếu bản quét 300 dpi cả chữ lẫn hình.
- **Liên hệ chéo:**
  - [Bài 1, mục 3–4](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó) — chi phí cơ hội, tư duy biên, chi phí chìm.
  - [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) — đường cầu, thứ còn thiếu để trả lời "bán giá bao nhiêu".
  - [Bài 4, mục 6](bai_04_thang_du_va_chi_phi_cua_thue.md#6-thặng-dư-sản-xuất--đối-xứng-hoàn-toàn) — chi phí của người bán trong thặng dư sản xuất.
  - **Bài 6** (chương 14) dùng trực tiếp ATC, AVC, MC để trả lời: sản xuất bao nhiêu, khi nào đóng cửa.

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md) | ch. 1–2 | 🎯 |
| 2 | [Cung và cầu](bai_02_cung_va_cau.md) | ch. 4 | 🎯 |
| 3 | [Độ co giãn và định giá](bai_03_do_co_gian_va_dinh_gia.md) | ch. 5 | 🎯⭐ |
| 4 | [Thặng dư và chi phí của thuế](bai_04_thang_du_va_chi_phi_cua_thue.md) | ch. 7–8 | 🔸 |
| **5** | **Chi phí sản xuất** ← *bạn đang ở đây* | ch. 13 | 🎯 |
| 6 | Doanh nghiệp trên thị trường cạnh tranh *(chưa viết)* | ch. 14 | 🎯 |
| 7 | Độc quyền và phân biệt giá *(chưa viết)* | ch. 15 | 🎯 |
| 8 | Cạnh tranh độc quyền và thương hiệu *(chưa viết)* | ch. 16 | 🎯 |
| 9 | Độc quyền nhóm và lý thuyết trò chơi *(chưa viết)* | ch. 17 | 🎯 |
| 10 | Lựa chọn của người tiêu dùng *(chưa viết)* | ch. 21 | 🎯 |
| 11 | Thông tin bất cân xứng và hành vi *(chưa viết)* | ch. 22 | 🎯 |
| 12 | Lao động, tiền lương, bất bình đẳng *(chưa viết)* | ch. 18–20 | 🔸 |
| 13 | Chính phủ can thiệp thị trường *(chưa viết)* | ch. 6, 12 | 🔸 |
| 14 | Thương mại, ngoại tác, hàng hoá công *(chưa viết)* | ch. 3, 9–11 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương quan trọng nhất với QTKD

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
