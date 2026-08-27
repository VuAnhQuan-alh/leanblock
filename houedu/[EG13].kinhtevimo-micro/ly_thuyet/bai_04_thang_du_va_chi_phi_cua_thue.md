# Bài 4 — Thặng dư, giá sẵn lòng trả và chi phí của thuế

> Bài học dựng từ **Chương 7 — Người tiêu dùng, nhà sản xuất và hiệu quả của thị trường** (tr. 153–173)
> và **Chương 8 — Ứng dụng: Chi phí của thuế** (tr. 174–189)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🔸 **Vòng 2** — không phải chương "định giá" như bài 3, nhưng nó cho bạn **thước đo giá trị**
> mà mọi lập luận về hiệu quả từ đây tới hết môn đều dùng. Riêng khái niệm **giá sẵn lòng trả**
> là nền trực tiếp của **phân biệt giá** ở bài 7.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp phụ.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 2 — Cung và cầu](bai_02_cung_va_cau.md) và
> [Bài 3 — Độ co giãn](bai_03_do_co_gian_va_dinh_gia.md) (mục 10 của bài này dùng lại độ co giãn).

---

## Mục lục

<!-- MUC-LUC -->

- [1. Kinh tế học phúc lợi — câu hỏi mà hai chương này trả lời](#1-kinh-tế-học-phúc-lợi--câu-hỏi-mà-hai-chương-này-trả-lời)
- [2. Giá sẵn lòng trả — khái niệm nền](#2-giá-sẵn-lòng-trả--khái-niệm-nền)
- [3. Thặng dư tiêu dùng](#3-thặng-dư-tiêu-dùng)
- [4. Đường cầu chính là bảng giá sẵn lòng trả](#4-đường-cầu-chính-là-bảng-giá-sẵn-lòng-trả)
- [5. 📚 Thặng dư tiêu dùng đo lường điều gì — và khi nào nó KHÔNG đo được](#5--thặng-dư-tiêu-dùng-đo-lường-điều-gì--và-khi-nào-nó-không-đo-được)
- [6. Thặng dư sản xuất — đối xứng hoàn toàn](#6-thặng-dư-sản-xuất--đối-xứng-hoàn-toàn)
- [7. Tổng thặng dư — thước đo phúc lợi](#7-tổng-thặng-dư--thước-đo-phúc-lợi)
- [8. Ba kết luận về thị trường tự do](#8-ba-kết-luận-về-thị-trường-tự-do)
- [9. ⚠️ Nhưng kết luận trên đứng trên HAI giả định](#9--nhưng-kết-luận-trên-đứng-trên-hai-giả-định)
- [10. Thuế làm gì với thị trường — bảng phúc lợi](#10-thuế-làm-gì-với-thị-trường--bảng-phúc-lợi)
- [11. Vì sao tổn thất vô ích xuất hiện — ví dụ Joe và Jane](#11-vì-sao-tổn-thất-vô-ích-xuất-hiện--ví-dụ-joe-và-jane)
- [12. Cái gì quyết định độ lớn của tổn thất vô ích — độ co giãn](#12-cái-gì-quyết-định-độ-lớn-của-tổn-thất-vô-ích--độ-co-giãn)
- [13. Thuế tăng thì chuyện gì xảy ra — và đường cong Laffer](#13-thuế-tăng-thì-chuyện-gì-xảy-ra--và-đường-cong-laffer)
- [14. 💼 Thặng dư tiêu dùng và tổn thất vô ích trong doanh nghiệp](#14--thặng-dư-tiêu-dùng-và-tổn-thất-vô-ích-trong-doanh-nghiệp)
- [15. Code minh hoạ](#15-code-minh-hoạ)
- [16. Tự thử](#16-tự-thử)
- [17. Từ điển thuật ngữ](#17-từ-điển-thuật-ngữ)
- [18. Câu hỏi tự kiểm tra](#18-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Kinh tế học phúc lợi — câu hỏi mà hai chương này trả lời

Chương 4 cho ta **mô hình**, chương 5 cho ta **thước đo phản ứng**. Nhưng cả hai đều chỉ mô tả *thị
trường vận hành thế nào*, chưa trả lời được câu hỏi **thị trường vận hành có tốt không**.

> **Kinh tế học phúc lợi** (*welfare economics*): nghiên cứu việc phân bổ nguồn lực tác động đến
> phúc lợi kinh tế như thế nào. — chương 7

Câu hỏi trung tâm mà sách đặt ra (tr. 163):

> *"Phân bổ nguồn lực được quyết định bởi thị trường tự do có đáng mong muốn không?"*

Để trả lời được, ta cần **một con số đo phúc lợi**. Chương 7 xây dựng con số đó bằng hai mảnh:
**thặng dư tiêu dùng** (lợi ích người mua) và **thặng dư sản xuất** (lợi ích người bán). Chương 8 dùng
ngay bộ công cụ ấy để đo **chi phí thật của một sắc thuế**.

---

## 2. Giá sẵn lòng trả — khái niệm nền

Sách bắt đầu bằng một câu chuyện rất cụ thể (tr. 154): bạn có một bản thu âm nguyên bản của **tập đĩa
đầu tay Elvis Presley** và muốn bán. Bạn mở một cuộc đấu giá. Bốn người hâm mộ tham gia:

> **Giá sẵn lòng trả** (*willingness to pay*): số tiền tối đa mà người mua sẵn lòng trả để mua một
> hàng hoá. — chú thích tr. 154

**Bảng 1, tr. 154:**

| Người mua | Giá sẵn lòng trả |
| --- | ---: |
| **John** | **$100** |
| Paul | 80 |
| George | 70 |
| Ringo | 50 |

Ý nghĩa của con số này, theo cách sách diễn đạt: *"nó được đo lường bằng giá trị người mua định giá
cho hàng hoá"*. Và tại đúng mức giá bằng mức sẵn lòng trả, người mua **bàng quan**:

> *"Nếu giá chính xác bằng đúng giá trị anh ta định giá tập đĩa, việc giữ lại tiền hay mua tập đĩa
> đối với anh ta là như nhau."* (tr. 154)

**Kết quả đấu giá:** giá tăng dần, dừng ở **80 đô la** (hoặc cao hơn chút ít) — vì Paul, George,
Ringo không trả cao hơn 80. **John thắng.**

Nhận xét mà sách nêu và đáng ghi nhớ: *"tập đĩa đã thuộc về người mua định giá trị tập đĩa ở mức cao
nhất"* (tr. 154). Đây là hạt giống của kết luận về hiệu quả ở mục 8.

---

## 3. Thặng dư tiêu dùng

> **Thặng dư tiêu dùng** (*consumer surplus*): mức sẵn lòng trả của người tiêu dùng cho một hàng hoá
> trừ cho số tiền mà người đó thực tế phải trả cho hàng hoá đó. — chú thích tr. 155

$$\text{Thặng dư tiêu dùng} = \text{giá sẵn lòng trả} - \text{giá thực trả}$$

John sẵn lòng trả 100, chỉ phải trả 80 → **thặng dư 20 đô la**. Paul, George, Ringo **không** nhận
được thặng dư nào vì họ *"đã ngừng lại lúc chưa mua được tập đĩa và chưa phải thanh toán gì"* (tr. 155).

### Trường hợp hai tập đĩa — chỗ ý tưởng thật sự hiện ra

Giả sử bạn có **hai** tập đĩa giống hệt, cùng bán một giá, mỗi người chỉ mua một. Đấu giá dừng ở
**70 đô la** (George và Ringo bỏ cuộc).

| Người thắng | Sẵn lòng trả | Trả | Thặng dư |
| --- | ---: | ---: | ---: |
| John | 100 | 70 | **$30** |
| Paul | 80 | 70 | **$10** |
| | | **Tổng** | **$40** |

⭐ **Điều đáng chú ý:** thặng dư của John **tăng từ 20 lên 30**, dù anh vẫn mua đúng một tập đĩa.
Nguyên nhân là **giá giảm**. Sách nói rõ: *"Thặng dư tiêu dùng của John lúc này cao hơn so với ví dụ
trước vì anh ta nhận được một tập đĩa giống hệt như vậy nhưng trả ít tiền hơn"* (tr. 155).

---

## 4. Đường cầu chính là bảng giá sẵn lòng trả

Từ Bảng 1, ta dựng được **biểu cầu** (Hình 1, tr. 156):

| Giá | Người mua | Lượng cầu |
| --- | --- | ---: |
| Nhiều hơn $100 | không ai | 0 |
| $80 đến $100 | John | 1 |
| $70 đến $80 | John, Paul | 2 |
| $50 đến $70 | John, Paul, George | 3 |
| $50 hoặc ít hơn | John, Paul, George, Ringo | 4 |

⭐ **Ý quan trọng nhất mục này** (tr. 156):

> *"Tại một mức sản lượng bất kỳ, mức giá tương ứng trên đường cầu thể hiện mức giá sẵn lòng trả của
> người mua sau cùng hay **người mua cận biên**, đây là người đầu tiên rời khỏi thị trường khi mức
> giá gia tăng."*

Ví dụ của sách: ở lượng 4, chiều cao đường cầu là **50 đô la** — mức Ringo sẵn lòng trả. Ở lượng 3,
chiều cao là **70 đô la** — mức George sẵn lòng trả.

### Và từ đó: thặng dư tiêu dùng là một DIỆN TÍCH

> **Phần diện tích dưới đường cầu và trên mức giá đo lường thặng dư tiêu dùng trên một thị trường.** (tr. 156)

Kiểm lại bằng Hình 2 (tr. 157):

| | Giá | Diện tích trên giá, dưới đường cầu | Khớp với tính tay ở mục 3? |
| --- | ---: | ---: | --- |
| Hình 2(a) | $80 | $20 | ✅ |
| Hình 2(b) | $70 | $30 + $10 = $40 | ✅ |

Với thị trường thật có **nhiều người mua**, các bậc thang nhỏ đến mức *"thật sự tạo nên một đường liên
tục"* (tr. 157) — nên đường cầu trơn, và thặng dư là một **tam giác**.

### Giá thấp hơn làm thặng dư tăng ra sao — hai phần khác nhau

**Hình 3, tr. 158.** Khi giá giảm từ $P_1$ xuống $P_2$, phần thặng dư tăng thêm (diện tích BCFD) gồm
**hai mảnh có bản chất khác nhau**:

```
   ① Hình chữ nhật BCED  —  KHÁCH CŨ, vẫn mua Q₁ như trước, nhưng nay TRẢ ÍT HƠN
   ② Tam giác CEF        —  KHÁCH MỚI, trước không mua nổi, nay gia nhập thị trường
                            làm lượng cầu tăng từ Q₁ lên Q₂
```

💼 Phân biệt hai mảnh này rất có ích khi đánh giá một đợt giảm giá: **mảnh ① là tiền bạn mất từ khách
sẵn sàng trả giá cũ**, mảnh ② là **doanh số mới thật sự**. Một chương trình khuyến mãi chỉ đáng làm
khi mảnh ② đủ lớn để bù mảnh ①.

---

## 5. 📚 Thặng dư tiêu dùng đo lường điều gì — và khi nào nó KHÔNG đo được

Sách dành hẳn một mục để tự vấn (tr. 158–159), và đây là phần trung thực nhất chương.

Thặng dư tiêu dùng là **thước đo tốt cho phúc lợi** *"nếu nhà hoạch định chính sách quan tâm đến quyền
lợi của người mua"*, vì nó đo lợi ích **theo nhận thức chủ quan của chính người mua**.

⚠️ **Nhưng có ngoại lệ**, và sách nêu thẳng ví dụ:

> *"Chẳng hạn như người nghiện ma tuý sẽ sẵn lòng trả giá cao để mua heroin. Tuy nhiên, chúng ta sẽ
> không nói rằng những người nghiện sẽ có nhiều lợi ích hơn khi mua được ma tuý với giá thấp… **thặng
> dư tiêu dùng không còn là thước đo tốt cho phúc lợi** của nền kinh tế vì những người nghiện không
> tìm kiếm những lợi ích tốt nhất cho bản thân mình."* (tr. 158)

Nói cách khác, toàn bộ công cụ này **đứng trên giả định người mua là duy lý**. Sách phát biểu rõ:
*"các nhà kinh tế học hay giả định người mua là duy lý khi đưa ra quyết định"* (tr. 158).

📌 Giả định đó sẽ bị **đặt lại nghiêm túc** ở **bài 11** (chương 22 — kinh tế học hành vi).

---

## 6. Thặng dư sản xuất — đối xứng hoàn toàn

Sách dựng lại đúng cấu trúc ở phía người bán (tr. 159): bạn muốn sơn nhà, mời **bốn** nhà cung cấp đấu
thầu.

> **Chi phí** (*cost*): giá trị của những thứ mà người bán phải bỏ ra để sản xuất một hàng hoá. — chú thích tr. 159

⚠️ **"Chi phí" ở đây là chi phí CƠ HỘI**, không phải chi tiền. Sách nói rõ: nó bao gồm cả tiền sơn,
cọ… *"cũng như giá trị của thời gian mà người sơn nhà phải bỏ ra trong thời gian đó"* — đúng nguyên lý 2
ở [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó).

**Bảng 2, tr. 159:**

| Người bán | Chi phí |
| --- | ---: |
| Mary | $900 |
| Frida | 800 |
| Georgia | 600 |
| **Grandma** | **$500** |

> **Thặng dư sản xuất** (*producer surplus*): số tiền nhà sản xuất được trả cho việc cung cấp một hàng
> hoá trừ cho tổng chi phí sản xuất ra hàng hoá đó. — chú thích tr. 160

| Số nhà cần sơn | Giá dừng ở | Người thắng | Thặng dư sản xuất |
| ---: | ---: | --- | ---: |
| **1** | $600 | Grandma | $600 − $500 = **$100** |
| **2** | $800 | Grandma, Georgia | ($800−500) + ($800−600) = **$500** |

Và đối xứng với phần cầu:

> **Phần diện tích dưới mức giá và trên đường cung đo lường thặng dư sản xuất trên một thị trường.**

Cũng như bên cầu, **chiều cao đường cung tại lượng Q là chi phí của người bán cận biên** (tr. 161):
ở lượng 4, chiều cao là 900 (Mary); ở lượng 3, là 800 (Frida).

### 💼 Góc QTKD — hai bảng này là hai bảng bạn thật sự phải lập

Hai khái niệm nghe hàn lâm, nhưng chúng là hai bảng tính rất cụ thể trong công việc:

| Kinh tế học gọi | Trong doanh nghiệp gọi là | Bạn dùng nó để |
| --- | --- | --- |
| **Giá sẵn lòng trả** | *willingness to pay*, "giá trần cảm nhận" | đặt giá niêm yết, thiết kế gói sản phẩm |
| **Chi phí (cơ hội)** | giá sàn thật, chi phí biên | biết mức thấp nhất còn nhận đơn ([bài 1, mục 4](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#4-nguyên-lý-3--con-người-duy-lý-suy-nghĩ-tại-điểm-cận-biên)) |
| **Thặng dư tiêu dùng** | phần giá trị **bạn để lại trên bàn** | ước lượng dư địa tăng giá / phân biệt giá |
| **Thặng dư sản xuất** | phần đóng góp (contribution margin) | biết đơn hàng nào thật sự sinh lời |

⭐ Dòng thứ ba là dòng đắt nhất. **Thặng dư tiêu dùng là tiền mà khách hàng đáng lẽ đã trả cho bạn
nhưng không phải trả** — vì bạn niêm yết một giá duy nhất. Mục 12 tính con số đó bằng một ví dụ cụ thể.

---

## 7. Tổng thặng dư — thước đo phúc lợi

Sách đưa vào một nhân vật giả tưởng để đặt câu hỏi cho gọn (tr. 163): **nhà hoạch định xã hội tốt bụng**
— *"một nhà độc tài hiểu biết mọi thứ, quyền lực toàn năng và có mục đích tốt"*, muốn tối đa hoá phúc
lợi kinh tế của mọi người.

Anh ta đo phúc lợi bằng **tổng thặng dư**:

$$
\begin{aligned}
\text{Thặng dư tiêu dùng} &= \text{Giá trị người tiêu dùng nhận được} - \text{Khoản phí người tiêu dùng phải trả} \\
\text{Thặng dư sản xuất} &= \text{Khoản tiền người sản xuất nhận được} - \text{Chi phí người sản xuất phải chịu}
\end{aligned}
$$

Cộng lại, hai khoản ở giữa **triệt tiêu nhau** (tiền người mua trả **đúng bằng** tiền người bán nhận):

$$\boxed{\text{Tổng thặng dư} = \text{Giá trị người tiêu dùng nhận được} - \text{Chi phí người sản xuất phải chịu}}$$

⭐ Công thức cuối này rất đáng nhớ, vì nó cho thấy **tiền chuyển từ túi này sang túi kia không tạo ra
và cũng không phá huỷ phúc lợi**. Chỉ có **giá trị tạo ra** và **chi phí bỏ ra** mới đáng kể.

> **Hiệu quả** (*efficiency*): thuộc tính của sự phân bổ nguồn lực, theo đó các thành viên xã hội đạt
> được tổng thặng dư cao nhất có thể từ những nguồn lực khan hiếm. — chú thích tr. 164
> **Bình đẳng** (*equality*): tình trạng phân phối sự thịnh vượng kinh tế một cách bằng nhau giữa các
> thành viên trong xã hội. — chú thích tr. 164

Sách nêu **hai kiểu không hiệu quả** (tr. 164), cùng một logic:

| Không hiệu quả khi | Sửa bằng cách |
| --- | --- |
| hàng hoá **không** được sản xuất bởi nhà cung cấp có **chi phí thấp nhất** | chuyển sản xuất sang nhà chi phí thấp → giảm tổng chi phí |
| hàng hoá **không** được tiêu thụ bởi người **định giá cao nhất** | chuyển hàng sang người định giá cao → tăng tổng giá trị |

Và nhắc lại ẩn dụ chiếc bánh từ [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#2-nguyên-lý-1--con-người-đối-mặt-với-sự-đánh-đổi):
hiệu quả hỏi *"chiếc bánh có to hết mức không"*, bình đẳng hỏi *"chiếc bánh được cắt ra như thế nào"*.
Chương này **chỉ tập trung vào hiệu quả** — sách ghi rõ điều đó.

---

## 8. Ba kết luận về thị trường tự do

**Hình 7 (tr. 165)** cho thấy khi thị trường cân bằng, tổng thặng dư là **toàn bộ diện tích giữa đường
cung và đường cầu, tính đến sản lượng cân bằng**.

Sách rút ra **ba hàm ý** (tr. 165–166):

> **1.** Thị trường tự do phân phối cung hàng hoá đến những người mua đánh giá hàng hoá **cao nhất**,
> nghĩa là có mức sẵn lòng trả cao nhất.
> **2.** Thị trường tự do phân phối cầu hàng hoá đến những người bán có thể sản xuất mặt hàng đó ở
> mức **chi phí thấp nhất**.
> **3.** Thị trường tự do tạo ra mức sản lượng hàng hoá **tối đa hoá tổng thặng dư** sản xuất và tiêu dùng.

Hai hàm ý đầu là về **phân phối cho ai**; hàm ý thứ ba là về **sản xuất bao nhiêu**, và **Hình 8
(tr. 166)** giải thích nó:

```
   Q < Q*  →  giá trị hàng hoá với người mua cận biên  >  chi phí của người bán cận biên
              ⟹ sản xuất thêm làm TĂNG tổng phúc lợi

   Q > Q*  →  giá trị với người mua cận biên  <  chi phí của người bán cận biên
              ⟹ sản xuất thêm làm GIẢM tổng phúc lợi

   ⟹ Điểm dừng tối ưu là chỗ HAI ĐƯỜNG GIAO NHAU — đúng cân bằng thị trường.
```

Mục 12 **chứng minh điều này bằng số**: quét mọi mức sản lượng và tính tổng thặng dư ở từng mức. Đỉnh
rơi đúng vào sản lượng cân bằng.

Kết luận về vai trò chính sách (tr. 166): *"nhà hoạch định xã hội cân bằng sẽ để thị trường tự vận hành
để đạt được hiệu quả"* — chính là **nguyên lý 6** ở bài 1, nay đã được **chứng minh** chứ không còn là
một ẩn dụ.

---

## 9. ⚠️ Nhưng kết luận trên đứng trên HAI giả định

Đây là mục quan trọng nhất của chương 7, và cũng là mục dễ bị bỏ qua nhất (tr. 169).

**Giả định 1 — thị trường cạnh tranh hoàn hảo.** Trong thực tế, *"một người mua hay người bán (hoặc
một nhóm nhỏ trong số họ) có thể kiểm soát giá thị trường"*. Đó là **quyền lực thị trường**, và nó
*"có thể làm cho thị trường không hiệu quả vì nó giữ mức giá và sản lượng cách xa mức cân bằng của
cung và cầu"*.

**Giả định 2 — kết quả thị trường chỉ tác động đến người mua và người bán trong thị trường đó.** Trong
thực tế, quyết định của họ *"đôi khi thỉnh thoảng tác động đến những người không tham gia vào thị
trường đó"*. Ví dụ của sách: **ô nhiễm** — hoá chất nông nghiệp tác động cả đến *"những người hít phải
không khí hay uống phải nguồn nước bị ô nhiễm"*. Đó là **ngoại tác**.

> Quyền lực thị trường và ngoại tác là những ví dụ về một hiện tượng chung gọi là **thất bại thị trường**
> — từ đó một vài thị trường không được điều tiết sẽ không thể phân bổ nguồn lực hiệu quả. (tr. 169)

📌 Hai thất bại này chính là **lộ trình của cả phần còn lại của môn học**:

| Thất bại | Học ở | Chương sách |
| --- | --- | --- |
| **Quyền lực thị trường** | bài 7 (độc quyền), bài 8, bài 9 | 15, 16, 17 |
| **Ngoại tác** | bài 14 | 10 |

⚠️ Nhưng sách cũng cân bằng lại ngay: *"Dù có những khả năng tồn tại thất bại thị trường nhưng **bàn
tay vô hình của thị trường vẫn cực kỳ quan trọng**. Ở nhiều thị trường, những giả định chúng ta đưa ra
ở chương này có thể được thoả mãn"* (tr. 169).
---

## 10. Thuế làm gì với thị trường — bảng phúc lợi

Từ đây là **chương 8**. Câu hỏi: nếu thị trường tự do đã hiệu quả, thì một sắc thuế **tốn của xã hội
bao nhiêu**?

Nhắc lại kết quả từ chương 6 (sẽ học kỹ ở **bài 13**): thuế tạo ra **khoảng cách** giữa mức giá người
mua **trả** và mức giá người bán **nhận**, và làm sản lượng giao dịch **giảm**. Điều quan trọng mà
sách nhấn mạnh:

> *"Tác động của thuế là **như nhau** khi thuế đánh lên người mua hoặc người bán."* (tr. 175)

Ai nộp thuế về mặt pháp lý **không quan trọng**; cái quyết định phần gánh chịu là **độ co giãn**.

### Ký hiệu (Hình 1–2, tr. 175–176)

| | |
| --- | --- |
| $P_B$ | giá người mua **phải trả** |
| $P_S$ | giá người bán **nhận được** |
| $T = P_B - P_S$ | độ lớn của thuế |
| $Q$ | sản lượng bán ra **khi có thuế** |
| **Doanh thu thuế** | $T \times Q$ — hình chữ nhật giữa hai đường |

⚠️ Sách lưu ý một điểm dễ hiểu nhầm về doanh thu thuế (tr. 176): phần lợi ích này *"thật sự không chỉ
dành cho chính phủ mà còn cho **những người được hưởng các lợi ích được chi trả bởi doanh thu thuế**"*
— đường sá, cảnh sát, giáo dục. Nên nó **được tính vào** tổng phúc lợi, không bị coi là mất đi.

### Bảng phúc lợi — Hình 3, tr. 177

Sáu vùng diện tích A → F:

| | **Không có thuế** | **Có thuế** | **Thay đổi** |
| --- | --- | --- | --- |
| Thặng dư tiêu dùng | $A+B+C$ | $A$ | $-(B+C)$ |
| Thặng dư sản xuất | $D+E+F$ | $F$ | $-(D+E)$ |
| Doanh thu thuế | không | $B+D$ | $+(B+D)$ |
| **Tổng thặng dư** | $A+B+C+D+E+F$ | $A+B+D+F$ | $\mathbf{-(C+E)}$ |

> **Tổn thất vô ích** (*deadweight loss*): phần giảm sút trong tổng thặng dư gây ra bởi những biến dạng
> thị trường, chẳng hạn như thuế. — chú thích tr. 178

⭐ **Đọc bảng này cho đúng.** Người mua mất $B + C$; chính phủ chỉ thu được $B$ từ họ. Người bán mất
$D + E$; chính phủ chỉ thu được $D$. Phần $C + E$ **không đến tay ai cả** — nó **biến mất**.

$$\text{Tổn thất vô ích} = \tfrac{1}{2} \times T \times (\text{sụt giảm sản lượng})$$

---

## 11. Vì sao tổn thất vô ích xuất hiện — ví dụ Joe và Jane

Đây là ví dụ hay nhất của chương 8, vì nó cho thấy tổn thất vô ích **không phải là tiền bị lấy đi**
mà là **giao dịch không xảy ra** (tr. 178).

**Khi chưa có thuế:**

| | |
| --- | --- |
| Joe quét dọn nhà cho Jane, giá | $100/tuần |
| Chi phí cơ hội thời gian của Joe | $80 |
| Giá trị một ngôi nhà sạch với Jane | $120 |
| **Joe lợi** | $100 − $80 = **$20** |
| **Jane lợi** | $120 − $100 = **$20** |
| **Tổng thặng dư** | **$40** |

**Bây giờ đánh thuế $50 lên dịch vụ vệ sinh.** Sách chỉ ra **không tồn tại mức giá nào** làm cả hai
cùng chấp nhận:

```
   Jane trả tối đa $120  →  Joe chỉ còn $120 − $50 = $70  <  chi phí cơ hội $80  →  Joe TỪ CHỐI
   Joe cần ít nhất $80   →  Jane phải trả $80 + $50 = $130  >  giá trị $120     →  Jane TỪ CHỐI
```

Kết quả: **thoả thuận bị huỷ.** Joe không có thu nhập, Jane sống trong ngôi nhà bụi bẩn hơn, và —
điểm mấu chốt — **chính phủ không thu được đồng nào** từ họ.

> *"Khoản tiền 40 đô la đơn thuần là khoản tổn thất vô ích: Đó là khoản thiệt hại mà người mua và người
> bán phải chịu trên một thị trường mà không được bù đắp bằng chính mức tăng trong doanh thu của chính
> phủ."* (tr. 178–179)

Và nguồn gốc, in nghiêng trong sách:

> ⭐ *"**Thuế gây ra tổn thất vô ích vì chúng làm người bán và người mua không nhận thấy được những lợi
> ích từ thương mại.**"* (tr. 179)

📌 Liên hệ về **nguyên lý 4** ở bài 1: thuế làm **biến dạng động cơ**. Người mua tiêu ít đi, người bán
sản xuất ít đi — và chính sự thay đổi hành vi ấy mới là nguồn gốc của tổn thất, chứ không phải khoản
tiền nộp.

⚠️ **Đính chính — tr. 178: một nhân vật, ba cái tên.**

Trong đúng một trang, người thuê Joe được gọi lần lượt là:

| Vị trí | Sách in |
| --- | --- |
| Câu mở đầu ví dụ | *"Joe quét dọn nhà cho **Jeal**"* |
| Câu tiếp theo | *"giá trị một ngôi nhà sạch đẹp đối với **Jean**"* |
| Các câu sau | *"**Jane** sẵn lòng trả…"*, *"**Jane** và Joe huỷ bỏ thoả thuận"* |
| Đoạn kết | *"Thuế gây tổn thất cho Joe và **Jean** là 40 đô la"* |

Bản gốc tiếng Anh dùng **Jane** xuyên suốt. **"Jeal"** là lỗi đánh máy, **"Jean"** là lỗi chuyển tự.
Đã đối chiếu bản quét 300 dpi. Không đổi nội dung, nhưng đọc lần đầu rất dễ tưởng là **hai người khác
nhau** và mất mạch. Khoá học này dùng thống nhất **Jane**.

---

## 12. Cái gì quyết định độ lớn của tổn thất vô ích — độ co giãn

Câu trả lời rất gọn (tr. 179): **độ co giãn của cung và cầu**.

**Hình 5, tr. 180** — bốn khung, mỗi khung cùng một mức thuế:

| Khung | Đường thay đổi | Tổn thất vô ích |
| --- | --- | --- |
| (a) | cung **ít co giãn** | **nhỏ** |
| (b) | cung **co giãn** | **lớn** |
| (c) | cầu **ít co giãn** | **nhỏ** |
| (d) | cầu **co giãn** | **lớn** |

Kết luận in nghiêng trong sách:

> ⭐ *"**Độ co giãn của cung và cầu càng lớn thì phần tổn thất vô ích do thuế gây ra cũng càng lớn.**"* (tr. 181)

**Cơ chế** (tr. 180–181): thuế gây tổn thất *"vì thuế làm cho người mua và người bán **thay đổi hành
vi**"*. Độ co giãn chính là **thước đo mức độ thay đổi hành vi**. Co giãn cao = phản ứng mạnh = thị
trường co lại nhiều = tổn thất lớn.

💡 **Hệ quả thực tiễn rất rõ:** muốn thu thuế mà ít gây méo mó, hãy đánh vào thứ có cầu và cung **không
co giãn** — điều này giải thích vì sao thuế thuốc lá, rượu, xăng phổ biến đến vậy ở mọi quốc gia.

### 📚 Nghiên cứu tình huống — tranh luận về tổn thất vô ích (tr. 181–182)

Sách chỉ ra rằng tranh cãi *"quy mô của chính phủ nên ở mức nào"* thực chất xoay quanh **một con số**:

> *"khi tổn thất vô ích do thuế càng lớn, thì chi phí của bất kỳ chương trình nào của chính phủ cũng
> càng lớn."*

Ví dụ được dùng: **thuế đánh lên lao động** ở Hoa Kỳ — thuế Bảo hiểm Xã hội, thuế Dịch vụ Y tế, thuế
thu nhập liên bang và của bang cộng lại cho **mức thuế suất biên khoảng 40%** trên thu nhập lao động.

| Nhóm | Tin rằng | Suy ra |
| --- | --- | --- |
| Cho rằng thuế lao động **ít bóp méo** | cung lao động **rất ít co giãn** — *"hầu hết mọi người sẽ làm việc toàn thời gian bất kể là ở mức lương nào"* | đường cung lao động gần **thẳng đứng** → tổn thất vô ích **nhỏ** |
| Cho rằng thuế lao động **bóp méo nhiều** | cung lao động **co giãn nhiều** hơn | tổn thất vô ích **lớn** |

📌 Lại đúng cấu trúc đã gặp ở [bài 3, mục 14](bai_03_do_co_gian_va_dinh_gia.md#14-ứng-dụng-3--cấm-ma-tuý-làm-tăng-hay-giảm-tội-phạm):
một tranh cãi **chuẩn tắc** ("chính phủ nên to hay nhỏ") mà điểm bất đồng thật sự lại là một **câu hỏi
thực chứng** ("độ co giãn của cung lao động bằng bao nhiêu").

---

## 13. Thuế tăng thì chuyện gì xảy ra — và đường cong Laffer

**Hình 6, tr. 183** theo dõi hai đại lượng khi mức thuế tăng dần:

### ① Tổn thất vô ích tăng theo BÌNH PHƯƠNG

Lý do rất hình học và rất đáng nhớ (tr. 183):

> *"phần tổn thất vô ích bằng diện tích của một tam giác, và diện tích của một tam giác thì tuỳ thuộc
> vào chiều cao và cạnh đáy của nó. Chẳng hạn, nếu chúng ta tăng thuế lên gấp đôi thì cạnh đáy và chiều
> cao của hình tam giác này cũng tăng gấp đôi, do đó phần tổn thất vô ích **tăng lên 4 lần**. Nếu chúng
> ta tăng thuế lên gấp ba, cạnh đáy và chiều cao cũng tăng gấp ba, vì vậy phần tổn thất vô ích **tăng
> lên 9 lần**."*

$$\text{Tổn thất vô ích} \propto T^2$$

### ② Doanh thu thuế tăng RỒI GIẢM — đường cong Laffer

| Mức thuế | Doanh thu | Vì |
| --- | --- | --- |
| (a) thấp | thấp | $T$ nhỏ |
| (b) vừa | **tăng lên** | $T$ tăng nhanh hơn $Q$ giảm |
| (c) cao | **giảm xuống** | *"mức thuế cao hơn này làm giảm đáng kể quy mô của thị trường"* |
| rất cao | về 0 | *"người ta sẽ cùng nhau ngừng mua và bán hàng hoá"* |

Đồ thị hình chuông ấy là **đường cong Laffer** (Hình 6e). Mục 14 vẽ lại nó bằng ký tự.

### 📚 Đường cong Laffer và kinh tế học trọng cung (tr. 184–185)

Câu chuyện mà sách kể, đáng đọc vì nó là ví dụ mẫu về việc **một ý tưởng đúng về lý thuyết bị dùng sai
trong thực tế**:

- **Năm 1974**, nhà kinh tế **Arthur Laffer** ngồi với các nhà báo và chính trị gia tại một nhà hàng ở
  Washington, vẽ đồ thị này lên một chiếc **khăn ăn**. Ông cho rằng Hoa Kỳ đang ở **nửa đi xuống** của
  đường cong → **giảm thuế suất sẽ làm tăng doanh thu thuế**.
- Ý tưởng được **Ronald Reagan** tán thành và trở thành chủ đề tranh cử **1980**; quan điểm này được
  gọi là **kinh tế học trọng cung**.
- Giai thoại mà **David Stockman** (Giám đốc Ngân khố nhiệm kỳ đầu của Reagan) kể lại: thời Thế chiến
  II, thuế suất thu nhập luỹ tiến lên đến **90%**; Reagan nói *"Bạn có thể đóng bốn bộ phim và rồi bạn
  sẽ thuộc vào nhóm đóng thuế cao nhất. Do đó, chúng ta sẽ ngừng làm việc sau khi đóng xong bốn bộ phim
  và về quê."*

⚠️ **Nhưng đánh giá của giới kinh tế thì khác**, và sách ghi rất rõ:

> *"**Hầu hết các nhà kinh tế học đều hoài nghi đề xuất của Laffer.** Ý tưởng cắt giảm thuế suất có thể
> làm tăng doanh thu thuế là chính xác trên góc độ lý thuyết kinh tế học, tuy nhiên trong thực tế điều
> này có xảy ra hay không vẫn còn khá mơ hồ. **Có rất ít bằng chứng ủng hộ quan điểm của Laffer** cho
> rằng thuế suất của Hoa Kỳ thực tế đang ở mức cao đến như vậy."* (tr. 184)

Sách nêu **hai điều kiện** mà lập luận Laffer có sức thuyết phục hơn:

1. Khi cắt giảm áp dụng cho **những người đang chịu mức thuế suất cao nhất**.
2. Ở **những quốc gia có thuế suất cao hơn Hoa Kỳ** — ví dụ **Thuỵ Điển đầu thập niên 1980**, người lao
   động thông thường chịu thuế suất biên **khoảng 80%**. *"Các nghiên cứu đề xuất rằng Thuỵ Điển thật
   sự đã có thể tăng thêm nhiều doanh thu thuế nếu nước này hạ thấp các mức thuế suất."*

Và câu kết luận mà **không ai tranh cãi** (tr. 185):

> *"Khoản doanh thu mà chính phủ đạt được hay mất đi do những thay đổi về thuế **không thể được tính
> toán chỉ dựa vào mức thuế suất**. Điều này còn phụ thuộc vào tác động của thuế lên **hành vi của con
> người** như thế nào."*

⭐ **Điều đáng rút ra:** đường cong Laffer **tồn tại** — đó là toán học. Nhưng *"đang ở nửa nào của
đường cong"* là một **câu hỏi thực nghiệm**, và trả lời nó cần dữ liệu chứ không phải một chiếc khăn ăn.

---

## 14. 💼 Thặng dư tiêu dùng và tổn thất vô ích trong doanh nghiệp

Hai khái niệm của chương này nghe rất "chính sách công", nhưng chúng mô tả chính xác hai thứ xảy ra
hằng ngày trong một doanh nghiệp.

### ① Thặng dư tiêu dùng = tiền bạn để lại trên bàn

Nếu bạn bán **một giá duy nhất**, mọi khách hàng có giá sẵn lòng trả **cao hơn** giá niêm yết đều đang
giữ lại phần chênh lệch. Đó là **thặng dư tiêu dùng của họ** — và cũng là **doanh thu bạn không thu được**.

Mục 15 tính con số này cho một ví dụ ba phân khúc. Kết quả: chuyển từ một giá sang **phân biệt giá**
làm doanh thu tăng **79%**, đến từ hai nguồn:

```
   ① thu lại phần thặng dư của khách SẴN SÀNG trả cao hơn
   ② bán được cho nhóm trước đây KHÔNG MUA NỔI ở mức giá chung
```

⚠️ Nguồn ② đáng chú ý: nó **không lấy của ai cả** — nhóm đó trước đây không mua, nay mua. Về mặt phúc
lợi, đây là **giảm tổn thất vô ích**, không phải chuyển giao. Đó là lý do phân biệt giá có thể vừa tăng
lợi nhuận vừa tăng tổng thặng dư — chi tiết ở **bài 7** (chương 15, tr. 351).

Nhưng phân biệt giá đòi **hai điều kiện** mà mô hình không nói:
- **ngăn được bán lại** giữa các nhóm;
- chịu được **rủi ro cảm nhận bất công**. Kinh tế học nói cái gì *hiệu quả*, nó không nói khách hàng sẽ
  nghĩ gì về bạn.

### ② Tổn thất vô ích không chỉ do thuế — mọi "khoản phí" đều tạo ra nó

Cơ chế của thuế là: **tạo chênh lệch giữa cái người mua trả và cái người bán nhận** → một số giao dịch
đáng lẽ có lợi **không xảy ra**. Bất cứ thứ gì tạo ra chênh lệch đó đều gây tổn thất vô ích:

| Trong doanh nghiệp | Chênh lệch nó tạo ra | Giao dịch bị mất |
| --- | --- | --- |
| Phí nội bộ tính chéo giữa các phòng ban | phòng dùng trả X, phòng cung cấp nhận X − phí | phòng ban tự đi thuê ngoài dù nội bộ rẻ hơn |
| Quy trình duyệt chi rườm rà | chi phí thời gian không ai nhận được | khoản chi đáng lẽ có lợi bị bỏ qua |
| Hoa hồng quá cao cho kênh trung gian | khách trả nhiều, hãng nhận ít | đơn hàng biên không thành |
| Chính sách chiết khấu cứng nhắc | không khớp được giá sẵn lòng trả | phân khúc nhạy giá bị mất trắng |

⭐ **Câu hỏi đúng khi rà soát một khoản phí nội bộ** không phải *"phí bao nhiêu"* mà là:
**"có bao nhiêu giao dịch đáng lẽ có lợi đã không xảy ra vì khoản phí này?"** — đúng câu hỏi mà tam
giác $C + E$ đo lường.

Và kèm theo hai hệ quả trực tiếp từ chương 8:

- **Phí tăng gấp đôi → thiệt hại gấp bốn.** Đừng tuyến tính hoá.
- **Bộ phận nào "co giãn" nhất chịu thiệt nhiều nhất** — tức bộ phận có nhiều lựa chọn thay thế nhất
  (thuê ngoài được, tự làm được). Họ sẽ phản ứng mạnh nhất với khoản phí.
---

## 15. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-04-thang-du-va-thue.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-04-thang-du-va-thue.py](../thuc_hanh/bai-04-thang-du-va-thue.py).

Mười một mục. Hai mục đáng chạy nhất:

- **Mục 5** không *minh hoạ* Hình 8 mà **chứng minh** nó: quét mọi mức sản lượng, tính tổng thặng dư
  ở từng mức, và đỉnh rơi đúng vào sản lượng cân bằng.
- **Mục 8** cho thấy tổn thất vô ích tăng theo **bình phương** mức thuế, còn doanh thu thuế thì
  **tăng rồi giảm** — đường cong Laffer hiện ra từ chính bảng số, không cần vẽ tay.

Thị trường dùng xuyên suốt: $Q_d = 120 - 2P$ và $Q_s = 2P - 40$, cân bằng tại $P = 40$, $Q = 40$.
Chọn số để **mọi kết quả đều là số nguyên**.

```python
"""Bai 4 — Thang du tieu dung, thang du san xuat va chi phi cua thue
(Mankiw, chuong 7 va chuong 8).
Chay: python3 bai-04-thang-du-va-thue.py   (Python 3.10+, khong can cai goi nao)

Moi so tien deu la SO NGUYEN (do la). Ket qua tat dinh.
"""

# ══ 1. THANG DU TIEU DUNG TU MOT CUOC DAU GIA — Bang 1, tr. 154 ═════════════
nguoi_mua = [("John", 100), ("Paul", 80), ("George", 70), ("Ringo", 50)]

print("1. THANG DU TIEU DUNG — dau gia tap dia Elvis  (Bang 1, tr. 154)")
print("   nguoi mua   gia san long tra")
for ten, v in nguoi_mua:
    print(f"   {ten:<10}   ${v}")
print()

def dau_gia(gia_tri, so_hang):
    """Dau gia tang dan: gia dung lai ngay tren muc san long tra cua nguoi
    dau tien BI LOAI. Tra ve (gia ban, danh sach nguoi thang)."""
    xep = sorted(gia_tri, key=lambda x: -x[1])
    gia = xep[so_hang][1] if so_hang < len(xep) else 0
    return gia, xep[:so_hang]

for so_hang in (1, 2):
    gia, thang = dau_gia(nguoi_mua, so_hang)
    print(f"   BAN {so_hang} TAP DIA  ->  gia dung o ${gia}")
    tong = 0
    for ten, v in thang:
        tong += v - gia
        print(f"      {ten:<8} tra ${gia}, dinh gia ${v}  ->  thang du = ${v - gia}")
    print(f"      TONG THANG DU TIEU DUNG = ${tong}")
print("   (sach: 1 tap dia -> $20; 2 tap dia -> $40 — tr. 155)")
print("   ⚠ John duoc LOI HON khi ban 2 tap dia ($30 thay vi $20): cung mon hang do,")
print("     nhung gia thap hon. Gia GIAM lam thang du cua nguoi mua CU tang len.")
print()

# ══ 2. BIEU CAU DUNG TU GIA SAN LONG TRA — Hinh 1, tr. 156 ══════════════════
print("2. BIEU CAU DUNG TU GIA SAN LONG TRA — Hinh 1, tr. 156")
print("   khoang gia          nguoi mua                     luong cau")
moc = [(101, None, "Nhieu hon $100", "khong ai"),
       (100, 80,  "$80 den $100",   "John"),
       (80,  70,  "$70 den $80",    "John, Paul"),
       (70,  50,  "$50 den $70",    "John, Paul, George"),
       (50,  0,   "$50 hoac it hon", "John, Paul, George, Ringo")]
for tren, _duoi, nhan, ai in moc:
    n = sum(1 for _, v in nguoi_mua if v >= tren) if tren > 100 else \
        sum(1 for _, v in nguoi_mua if v >= tren)
    print(f"   {nhan:<18}  {ai:<28}  {n}")
print("   ⭐ CHIEU CAO cua duong cau tai luong Q = gia san long tra cua NGUOI MUA")
print("      CAN BIEN (nguoi dau tien roi thi truong khi gia tang).")
print()

# ══ 3. THANG DU SAN XUAT TU MOT CUOC DAU THAU — Bang 2, tr. 159 ═════════════
nguoi_ban = [("Mary", 900), ("Frida", 800), ("Georgia", 600), ("Grandma", 500)]

print("3. THANG DU SAN XUAT — dau thau son nha  (Bang 2, tr. 159)")
print("   nguoi ban    chi phi")
for ten, c in nguoi_ban:
    print(f"   {ten:<10}   ${c}")
print()

def dau_thau(chi_phi, so_viec):
    """Dau thau giam dan: gia dung lai ngay duoi chi phi cua nguoi dau tien BI LOAI."""
    xep = sorted(chi_phi, key=lambda x: x[1])
    gia = xep[so_viec][1] if so_viec < len(xep) else 0
    return gia, xep[:so_viec]

for so_viec in (1, 2):
    gia, thang = dau_thau(nguoi_ban, so_viec)
    print(f"   SON {so_viec} NGOI NHA  ->  gia dung o ${gia}")
    tong = 0
    for ten, c in thang:
        tong += gia - c
        print(f"      {ten:<8} nhan ${gia}, chi phi ${c}  ->  thang du = ${gia - c}")
    print(f"      TONG THANG DU SAN XUAT = ${tong}")
print("   (sach: 1 nha -> $100; 2 nha -> $500 — tr. 160)")
print("   ⚠ Doi xung hoan toan voi phan cau: gia CAO hon lam thang du nguoi ban CU tang.")
print()

# ══ 4. THI TRUONG LIEN TUC — cong thuc va can bang ══════════════════════════
# Cau:  Qd = 120 - 2P   <=>  gia san long tra cho don vi thu q la  Pd(q) = 60 - q/2
# Cung: Qs = 2P -  40   <=>  chi phi san xuat don vi thu q la      Ps(q) = 20 + q/2
def Pd(q):  return 60 - q / 2
def Ps(q):  return 20 + q / 2

P0, Q0 = 40, 40                       # 120 - 2P = 2P - 40  ->  P = 40, Q = 40
CS0 = (60 - P0) * Q0 // 2
PS0 = (P0 - 20) * Q0 // 2

print("4. THI TRUONG LIEN TUC — THANG DU KHI CAN BANG  (Hinh 7, tr. 165)")
print("   cau  Qd = 120 - 2P     cung  Qs = 2P - 40")
print(f"   can bang: P = ${P0}, Q = {Q0}")
print(f"   thang du TIEU DUNG = 1/2 x {Q0} x (60 - {P0}) = ${CS0}")
print(f"   thang du SAN XUAT  = 1/2 x {Q0} x ({P0} - 20) = ${PS0}")
print(f"   TONG THANG DU = ${CS0 + PS0}")
print()

# ══ 5. CHUNG MINH BANG SO: CAN BANG TOI DA HOA TONG THANG DU (Hinh 8, tr.166) ═
def tong_thang_du(Q):
    """Tong gia tri nguoi mua nhan duoc tru tong chi phi nguoi ban chiu,
    khi thi truong giao dich dung Q don vi:  tich phan (Pd - Ps) tu 0 den Q."""
    return 40 * Q - Q * Q // 2

print("5. VI SAO CAN BANG LA HIEU QUA — quet moi muc san luong (Hinh 8, tr. 166)")
print("      Q     gia tri nguoi mua   chi phi nguoi ban   TONG THANG DU")
for Q in range(0, 70, 10):
    gt = 60 * Q - Q * Q // 4          # dien tich duoi duong cau tu 0 den Q
    cp = 20 * Q + Q * Q // 4          # dien tich duoi duong cung tu 0 den Q
    dau = "  <-- CAN BANG, LON NHAT" if Q == Q0 else ""
    print(f"   {Q:>4}   {gt:>15,}   {cp:>17,}   {gt - cp:>13,}{dau}")
print(f"   ⭐ Dinh dung tai Q = {Q0} — chinh la san luong can bang cua thi truong.")
print("      Q < 40: don vi tiep theo co GIA TRI voi nguoi mua LON HON chi phi")
print("              nguoi ban  ->  san xuat them lam TANG tong thang du")
print("      Q > 40: nguoc lai  ->  san xuat them lam GIAM tong thang du")
print("   ⟹ 'nha hoach dinh xa hoi tot bung' khong lam hon duoc thi truong tu do.")
print()

# ══ 6. THUE — tai tao bang Hinh 3, tr. 177 ══════════════════════════════════
def thi_truong_co_thue(T):
    """Thue T tren moi don vi. Tra ve (gia nguoi mua tra, gia nguoi ban nhan,
    luong, CS, PS, doanh thu thue, tong thang du, ton that vo ich)."""
    Pb = 40 + T // 2 if T % 2 == 0 else None      # giu so nguyen: chi dung T chan
    Ps_ = 40 - T // 2
    Q = 40 - T
    cs = (60 - Pb) * Q // 2
    ps = (Ps_ - 20) * Q // 2
    dt = T * Q
    return Pb, Ps_, Q, cs, ps, dt, cs + ps + dt, (CS0 + PS0) - (cs + ps + dt)

T = 10
Pb, Psell, Q, cs, ps, dt, tong, dwl = thi_truong_co_thue(T)
print(f"6. THUE ${T} MOT DON VI — bang phuc loi  (Hinh 3, tr. 177)")
print(f"   gia nguoi mua PHAI TRA  P_B = ${Pb}   (truoc: ${P0})")
print(f"   gia nguoi ban NHAN DUOC P_S = ${Psell}   (truoc: ${P0})")
print(f"   luong giao dich Q = {Q}          (truoc: {Q0})")
print()
print("                        khong co thue    co thue     thay doi")
for ten, cu, moi in [("Thang du tieu dung", CS0, cs),
                     ("Thang du san xuat ", PS0, ps),
                     ("Doanh thu thue    ", 0,   dt),
                     ("TONG THANG DU     ", CS0 + PS0, tong)]:
    print(f"   {ten}   {cu:>10,}   {moi:>10,}   {moi - cu:>+9,}")
print(f"   ⟹ TON THAT VO ICH = ${dwl}  (dien tich C + E cua Hinh 3)")
print(f"      Kiem: 1/2 x thue x sut giam san luong = 1/2 x {T} x {Q0 - Q} = {T * (Q0 - Q) // 2}")
print("   ⚠ Nguoi mua mat nhieu hon phan chinh phu thu duoc tu ho; nguoi ban cung vay.")
print("     Phan chenh lech do KHONG di dau ca — no bien mat. Do la ton that vo ich.")
print()

# ══ 7. VI DU JOE VA JANE — tr. 178 ══════════════════════════════════════════
gia_thue_lao_cong = 100
chi_phi_co_hoi_joe = 80
gia_tri_voi_jane = 120
thue = 50
print("7. VI DU JOE VA JANE — vi sao ton that vo ich XUAT HIEN  (tr. 178)")
print(f"   Joe quet don nha cho Jane gia ${gia_thue_lao_cong}/tuan")
print(f"      chi phi co hoi thoi gian cua Joe = ${chi_phi_co_hoi_joe}")
print(f"      gia tri mot ngoi nha sach voi Jane = ${gia_tri_voi_jane}")
print(f"      -> Joe loi ${gia_thue_lao_cong - chi_phi_co_hoi_joe}, "
      f"Jane loi ${gia_tri_voi_jane - gia_thue_lao_cong}, "
      f"TONG THANG DU = ${gia_tri_voi_jane - chi_phi_co_hoi_joe}")
print()
print(f"   Bay gio danh thue ${thue} len dich vu ve sinh:")
print(f"      Jane tra toi da ${gia_tri_voi_jane}  ->  Joe chi con "
      f"${gia_tri_voi_jane - thue} < chi phi co hoi ${chi_phi_co_hoi_joe}  ->  Joe TU CHOI")
print(f"      Joe can it nhat ${chi_phi_co_hoi_joe}  ->  Jane phai tra "
      f"${chi_phi_co_hoi_joe + thue} > gia tri ${gia_tri_voi_jane}  ->  Jane TU CHOI")
print(f"      => KHONG CO MUC GIA NAO ca hai cung chap nhan. Giao dich BIEN MAT.")
print(f"      Chinh phu thu duoc: $0.  Xa hoi mat: "
      f"${gia_tri_voi_jane - chi_phi_co_hoi_joe}  <- toan bo la TON THAT VO ICH")
print("   ⭐ Thue gay ton that vo ich vi no lam nguoi mua va nguoi ban KHONG NHAN THAY")
print("      duoc nhung LOI ICH TU THUONG MAI von co that.")
print()

# ══ 8. TON THAT VO ICH TANG THEO BINH PHUONG — Hinh 6, tr. 183 ══════════════
print("8. THUE TANG THI DIEU GI XAY RA?  (Hinh 6, tr. 183)")
print("      thue   luong   ton that vo ich   doanh thu thue")
for T in range(0, 42, 4):
    *_, Qt, _cs, _ps, dtt, _tong, dwlt = thi_truong_co_thue(T)
    print(f"   {T:>7}   {Qt:>5}   {dwlt:>15,}   {dtt:>14,}")
print()
print("   ⭐ THUE GAP DOI -> TON THAT VO ICH GAP BON (dien tich tam giac):")
for T in (4, 8, 16):
    *_, dwlt = thi_truong_co_thue(T)
    print(f"      thue ${T:>2}  ->  ton that vo ich ${dwlt}")
print("      4 -> 8 -> 16 la gap doi; 16 -> 64 -> 256 la gap BON moi lan.")
print("   (sach tr. 183: 'tang thue len gap doi thi ton that vo ich tang len 4 lan;")
print("    gap ba thi ton that vo ich tang len 9 lan')")
print()

# ══ 9. DUONG CONG LAFFER ════════════════════════════════════════════════════
print("9. DUONG CONG LAFFER — doanh thu thue theo muc thue  (Hinh 6e, tr. 183)")
CAO, RONG = 13, 42
dt_max = 400
luoi = [[" "] * RONG for _ in range(CAO)]
for i in range(RONG):
    t = 40 * i / (RONG - 1)
    dtt = t * (40 - t)
    r = CAO - 1 - round(dtt / dt_max * (CAO - 1))
    luoi[r][i] = "●"
    for rr in range(r + 1, CAO):
        if luoi[rr][i] == " ":
            luoi[rr][i] = "·"
print("      doanh thu thue")
for i, hang in enumerate(luoi):
    v = dt_max - round(i * dt_max / (CAO - 1))
    nhan = f"{v:>4}" if i % 3 == 0 else "    "
    print(f"      {nhan} │{''.join(hang)}".rstrip())
print("           └" + "─" * RONG)
print("            $0" + " " * (RONG - 6) + " $40  muc thue")
cot = round(20 / 40 * (RONG - 1))
print(" " * 12 + " " * cot + "^ dinh o thue = $20, doanh thu $400")
print("   ⭐ Tang thue tu $0 -> $20: doanh thu TANG.  Tu $20 -> $40: doanh thu GIAM.")
print("      O thue $40, luong giao dich = 0 nen doanh thu = $0 du thue suat cao nhat.")
print("   ⚠ Sach ghi ro (tr. 184): 'Hau het cac nha kinh te hoc deu hoai nghi de xuat")
print("      cua Laffer... Co rat it bang chung ung ho quan diem cho rang thue suat cua")
print("      Hoa Ky thuc te dang o muc cao den nhu vay.' Duong cong TON TAI khong co")
print("      nghia la nen kinh te dang o NUA BEN PHAI cua no.")
print()

# ══ 10. DO CO GIAN QUYET DINH TON THAT VO ICH — Hinh 5, tr. 180 ════════════
print("10. DO CO GIAN QUYET DINH TON THAT VO ICH  (Hinh 5, tr. 180)")
# Ca bon truong hop deu di qua diem can bang (P=40, Q=40) va deu chiu thue $10.
# He so PHAN UNG cang LON  =>  duong cang THOAI  =>  cang CO GIAN.
#     Qd = 40 + hs_cau  x (40 - P)      Qs = 40 - hs_cung x (40 - P)
T10 = 10
print(f"    Ca bon deu di qua can bang (P=$40, Q=40) va cung chiu thue ${T10}.")
print("    He so phan ung cang LON = duong cang THOAI = cang CO GIAN.")
print("    truong hop                    he so cau   he so cung   luong giam   ton that")
for ten, hs_cau, hs_cung in [
        ("(a) cung KHONG co gian",  2,  1),
        ("(b) cung CO GIAN",        2,  8),
        ("(c) cau  KHONG co gian",  1,  2),
        ("(d) cau  CO GIAN",        8,  2)]:
    Pb = (40 * (hs_cau + hs_cung) + hs_cung * T10) / (hs_cau + hs_cung)
    Qt = 40 + hs_cau * (40 - Pb)
    giam = 40 - Qt
    ton_that = T10 * giam / 2
    print(f"    {ten:<28} {hs_cau:>9}   {hs_cung:>10}   {giam:>10.1f}   {ton_that:>8.1f}")
print("    ⭐ Duong nao CANG CO GIAN thi ton that vo ich CANG LON: (a)->(b) va (c)->(d)")
print("       deu lam ton that nhay tu 33,3 len 80,0.")
print("       Vi co gian = nguoi ta DOI HANH VI nhieu; ma chinh su doi hanh vi do")
print("       moi la nguon goc cua ton that.")
print()

# ══ 11. 💼 GOC QTKD ═════════════════════════════════════════════════════════
print("11. 💼 GOC QTKD — THANG DU TIEU DUNG LA 'TIEN BAN DE LAI TREN BAN'")
khach = [("khach doanh nghiep", 500, 40), ("khach le", 300, 120), ("sinh vien", 150, 200)]
GIA_DONG = 300
print(f"    Ba nhom khach, gia san long tra khac nhau. Neu ban MOT GIA ${GIA_DONG}:")
print("    nhom                 san long tra   so khach   mua?   doanh thu   thang du KHACH")
tong_dt = tong_td = 0
for ten, wtp, n in khach:
    mua = wtp >= GIA_DONG
    dt = GIA_DONG * n if mua else 0
    td = (wtp - GIA_DONG) * n if mua else 0
    tong_dt += dt; tong_td += td
    print(f"    {ten:<20} {wtp:>10}   {n:>8}   {'CO' if mua else 'KHONG':<6} {dt:>10,}   {td:>14,}")
print(f"    {'TONG':<20} {'':>10}   {'':>8}   {'':<6} {tong_dt:>10,}   {tong_td:>14,}")
print()
print("    Neu PHAN BIET GIA — ban dung gia san long tra cua tung nhom:")
tong_dt2 = 0
for ten, wtp, n in khach:
    tong_dt2 += wtp * n
    print(f"    {ten:<20} ban gia ${wtp:<5} x {n:>3} khach = {wtp * n:>7,}")
print(f"    {'TONG':<20} {tong_dt2:>34,}")
print(f"    => doanh thu {tong_dt:,} -> {tong_dt2:,}  (+{tong_dt2 - tong_dt:,})")
print(f"       Toan bo thang du cua KHACH ({tong_td:,}) chuyen thanh doanh thu,")
print(f"       CONG THEM {tong_dt2 - tong_dt - tong_td:,} tu nhom sinh vien truoc day khong mua noi.")
print("    ⭐ Day chinh la PHAN BIET GIA — bai 7 (chuong 15, tr. 351).")
print("    ⚠ Nhung: doi hoi phai NGAN duoc ban lai giua cac nhom, va co rui ro")
print("      ve cam nhan cong bang. Kinh te hoc noi cai gi HIEU QUA, khong noi")
print("      khach hang se nghi gi ve ban.")
print()
print("    💼 TON THAT VO ICH BEN TRONG DOANH NGHIEP")
print("       Moi 'khoan phi' noi bo deu tao ra chenh lech giua nguoi mua va nguoi ban,")
print("       va do do tao ton that vo ich — dung co che nhu thue:")
print("       - phi noi bo tinh cheo giua cac phong ban  -> phong ban ngung dung dich vu")
print("         noi bo du no van re hon thue ngoai")
print("       - quy trinh duyet chi ruom ra              -> nhan vien bo qua khoan chi")
print("         dang le co loi")
print("       - hoa hong qua cao cho kenh trung gian     -> giao dich dang le xay ra thi khong")
print("       ⟹ cau hoi dung khong phai 'phi bao nhieu' ma 'co bao nhieu giao dich")
print("          DANG LE CO LOI da khong xay ra vi khoan phi nay'.")
```

**Kết quả chạy thật:**

```
1. THANG DU TIEU DUNG — dau gia tap dia Elvis  (Bang 1, tr. 154)
   nguoi mua   gia san long tra
   John         $100
   Paul         $80
   George       $70
   Ringo        $50

   BAN 1 TAP DIA  ->  gia dung o $80
      John     tra $80, dinh gia $100  ->  thang du = $20
      TONG THANG DU TIEU DUNG = $20
   BAN 2 TAP DIA  ->  gia dung o $70
      John     tra $70, dinh gia $100  ->  thang du = $30
      Paul     tra $70, dinh gia $80  ->  thang du = $10
      TONG THANG DU TIEU DUNG = $40
   (sach: 1 tap dia -> $20; 2 tap dia -> $40 — tr. 155)
   ⚠ John duoc LOI HON khi ban 2 tap dia ($30 thay vi $20): cung mon hang do,
     nhung gia thap hon. Gia GIAM lam thang du cua nguoi mua CU tang len.

2. BIEU CAU DUNG TU GIA SAN LONG TRA — Hinh 1, tr. 156
   khoang gia          nguoi mua                     luong cau
   Nhieu hon $100      khong ai                      0
   $80 den $100        John                          1
   $70 den $80         John, Paul                    2
   $50 den $70         John, Paul, George            3
   $50 hoac it hon     John, Paul, George, Ringo     4
   ⭐ CHIEU CAO cua duong cau tai luong Q = gia san long tra cua NGUOI MUA
      CAN BIEN (nguoi dau tien roi thi truong khi gia tang).

3. THANG DU SAN XUAT — dau thau son nha  (Bang 2, tr. 159)
   nguoi ban    chi phi
   Mary         $900
   Frida        $800
   Georgia      $600
   Grandma      $500

   SON 1 NGOI NHA  ->  gia dung o $600
      Grandma  nhan $600, chi phi $500  ->  thang du = $100
      TONG THANG DU SAN XUAT = $100
   SON 2 NGOI NHA  ->  gia dung o $800
      Grandma  nhan $800, chi phi $500  ->  thang du = $300
      Georgia  nhan $800, chi phi $600  ->  thang du = $200
      TONG THANG DU SAN XUAT = $500
   (sach: 1 nha -> $100; 2 nha -> $500 — tr. 160)
   ⚠ Doi xung hoan toan voi phan cau: gia CAO hon lam thang du nguoi ban CU tang.

4. THI TRUONG LIEN TUC — THANG DU KHI CAN BANG  (Hinh 7, tr. 165)
   cau  Qd = 120 - 2P     cung  Qs = 2P - 40
   can bang: P = $40, Q = 40
   thang du TIEU DUNG = 1/2 x 40 x (60 - 40) = $400
   thang du SAN XUAT  = 1/2 x 40 x (40 - 20) = $400
   TONG THANG DU = $800

5. VI SAO CAN BANG LA HIEU QUA — quet moi muc san luong (Hinh 8, tr. 166)
      Q     gia tri nguoi mua   chi phi nguoi ban   TONG THANG DU
      0                 0                   0               0
     10               575                 225             350
     20             1,100                 500             600
     30             1,575                 825             750
     40             2,000               1,200             800  <-- CAN BANG, LON NHAT
     50             2,375               1,625             750
     60             2,700               2,100             600
   ⭐ Dinh dung tai Q = 40 — chinh la san luong can bang cua thi truong.
      Q < 40: don vi tiep theo co GIA TRI voi nguoi mua LON HON chi phi
              nguoi ban  ->  san xuat them lam TANG tong thang du
      Q > 40: nguoc lai  ->  san xuat them lam GIAM tong thang du
   ⟹ 'nha hoach dinh xa hoi tot bung' khong lam hon duoc thi truong tu do.

6. THUE $10 MOT DON VI — bang phuc loi  (Hinh 3, tr. 177)
   gia nguoi mua PHAI TRA  P_B = $45   (truoc: $40)
   gia nguoi ban NHAN DUOC P_S = $35   (truoc: $40)
   luong giao dich Q = 30          (truoc: 40)

                        khong co thue    co thue     thay doi
   Thang du tieu dung          400          225        -175
   Thang du san xuat           400          225        -175
   Doanh thu thue                0          300        +300
   TONG THANG DU               800          750         -50
   ⟹ TON THAT VO ICH = $50  (dien tich C + E cua Hinh 3)
      Kiem: 1/2 x thue x sut giam san luong = 1/2 x 10 x 10 = 50
   ⚠ Nguoi mua mat nhieu hon phan chinh phu thu duoc tu ho; nguoi ban cung vay.
     Phan chenh lech do KHONG di dau ca — no bien mat. Do la ton that vo ich.

7. VI DU JOE VA JANE — vi sao ton that vo ich XUAT HIEN  (tr. 178)
   Joe quet don nha cho Jane gia $100/tuan
      chi phi co hoi thoi gian cua Joe = $80
      gia tri mot ngoi nha sach voi Jane = $120
      -> Joe loi $20, Jane loi $20, TONG THANG DU = $40

   Bay gio danh thue $50 len dich vu ve sinh:
      Jane tra toi da $120  ->  Joe chi con $70 < chi phi co hoi $80  ->  Joe TU CHOI
      Joe can it nhat $80  ->  Jane phai tra $130 > gia tri $120  ->  Jane TU CHOI
      => KHONG CO MUC GIA NAO ca hai cung chap nhan. Giao dich BIEN MAT.
      Chinh phu thu duoc: $0.  Xa hoi mat: $40  <- toan bo la TON THAT VO ICH
   ⭐ Thue gay ton that vo ich vi no lam nguoi mua va nguoi ban KHONG NHAN THAY
      duoc nhung LOI ICH TU THUONG MAI von co that.

8. THUE TANG THI DIEU GI XAY RA?  (Hinh 6, tr. 183)
      thue   luong   ton that vo ich   doanh thu thue
         0      40                 0                0
         4      36                 8              144
         8      32                32              256
        12      28                72              336
        16      24               128              384
        20      20               200              400
        24      16               288              384
        28      12               392              336
        32       8               512              256
        36       4               648              144
        40       0               800                0

   ⭐ THUE GAP DOI -> TON THAT VO ICH GAP BON (dien tich tam giac):
      thue $ 4  ->  ton that vo ich $8
      thue $ 8  ->  ton that vo ich $32
      thue $16  ->  ton that vo ich $128
      4 -> 8 -> 16 la gap doi; 16 -> 64 -> 256 la gap BON moi lan.
   (sach tr. 183: 'tang thue len gap doi thi ton that vo ich tang len 4 lan;
    gap ba thi ton that vo ich tang len 9 lan')

9. DUONG CONG LAFFER — doanh thu thue theo muc thue  (Hinh 6e, tr. 183)
      doanh thu thue
       400 │                 ●●●●●●●●
           │              ●●●········●●●
           │            ●●··············●●
       300 │          ●●··················●●
           │        ●●······················●●
           │       ●··························●
       200 │      ●····························●
           │     ●······························●
           │    ●································●
       100 │   ●··································●
           │  ●····································●
           │ ●······································●
         0 │●········································●
           └──────────────────────────────────────────
            $0                                     $40  muc thue
                                ^ dinh o thue = $20, doanh thu $400
   ⭐ Tang thue tu $0 -> $20: doanh thu TANG.  Tu $20 -> $40: doanh thu GIAM.
      O thue $40, luong giao dich = 0 nen doanh thu = $0 du thue suat cao nhat.
   ⚠ Sach ghi ro (tr. 184): 'Hau het cac nha kinh te hoc deu hoai nghi de xuat
      cua Laffer... Co rat it bang chung ung ho quan diem cho rang thue suat cua
      Hoa Ky thuc te dang o muc cao den nhu vay.' Duong cong TON TAI khong co
      nghia la nen kinh te dang o NUA BEN PHAI cua no.

10. DO CO GIAN QUYET DINH TON THAT VO ICH  (Hinh 5, tr. 180)
    Ca bon deu di qua can bang (P=$40, Q=40) va cung chiu thue $10.
    He so phan ung cang LON = duong cang THOAI = cang CO GIAN.
    truong hop                    he so cau   he so cung   luong giam   ton that
    (a) cung KHONG co gian               2            1          6.7       33.3
    (b) cung CO GIAN                     2            8         16.0       80.0
    (c) cau  KHONG co gian               1            2          6.7       33.3
    (d) cau  CO GIAN                     8            2         16.0       80.0
    ⭐ Duong nao CANG CO GIAN thi ton that vo ich CANG LON: (a)->(b) va (c)->(d)
       deu lam ton that nhay tu 33,3 len 80,0.
       Vi co gian = nguoi ta DOI HANH VI nhieu; ma chinh su doi hanh vi do
       moi la nguon goc cua ton that.

11. 💼 GOC QTKD — THANG DU TIEU DUNG LA 'TIEN BAN DE LAI TREN BAN'
    Ba nhom khach, gia san long tra khac nhau. Neu ban MOT GIA $300:
    nhom                 san long tra   so khach   mua?   doanh thu   thang du KHACH
    khach doanh nghiep          500         40   CO         12,000            8,000
    khach le                    300        120   CO         36,000                0
    sinh vien                   150        200   KHONG           0                0
    TONG                                                    48,000            8,000

    Neu PHAN BIET GIA — ban dung gia san long tra cua tung nhom:
    khach doanh nghiep   ban gia $500   x  40 khach =  20,000
    khach le             ban gia $300   x 120 khach =  36,000
    sinh vien            ban gia $150   x 200 khach =  30,000
    TONG                                             86,000
    => doanh thu 48,000 -> 86,000  (+38,000)
       Toan bo thang du cua KHACH (8,000) chuyen thanh doanh thu,
       CONG THEM 30,000 tu nhom sinh vien truoc day khong mua noi.
    ⭐ Day chinh la PHAN BIET GIA — bai 7 (chuong 15, tr. 351).
    ⚠ Nhung: doi hoi phai NGAN duoc ban lai giua cac nhom, va co rui ro
      ve cam nhan cong bang. Kinh te hoc noi cai gi HIEU QUA, khong noi
      khach hang se nghi gi ve ban.

    💼 TON THAT VO ICH BEN TRONG DOANH NGHIEP
       Moi 'khoan phi' noi bo deu tao ra chenh lech giua nguoi mua va nguoi ban,
       va do do tao ton that vo ich — dung co che nhu thue:
       - phi noi bo tinh cheo giua cac phong ban  -> phong ban ngung dung dich vu
         noi bo du no van re hon thue ngoai
       - quy trinh duyet chi ruom ra              -> nhan vien bo qua khoan chi
         dang le co loi
       - hoa hong qua cao cho kenh trung gian     -> giao dich dang le xay ra thi khong
       ⟹ cau hoi dung khong phai 'phi bao nhieu' ma 'co bao nhieu giao dich
          DANG LE CO LOI da khong xay ra vi khoan phi nay'.
```

### Đọc kết quả

**① Đấu giá (mục 1).** Bán 1 tập đĩa → thặng dư **$20**; bán 2 → **$40**. Khớp tr. 155. Chú ý dòng
cảnh báo: thặng dư của John nhảy từ 20 lên **30** dù anh vẫn mua đúng một tập — vì **giá giảm**.

**② Đấu thầu (mục 3).** Đối xứng: **$100** rồi **$500**, khớp tr. 160.

**③ Cân bằng là hiệu quả (mục 5).** Bảng quét $Q = 0 \to 60$:

| $Q$ | 0 | 10 | 20 | 30 | **40** | 50 | 60 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tổng thặng dư | 0 | 350 | 600 | 750 | **800** | 750 | 600 |

Đỉnh đúng tại $Q = 40$ — sản lượng cân bằng. Đây là hàm ý thứ ba ở mục 8, được kiểm bằng số.

**④ Bảng phúc lợi khi có thuế (mục 6).** Thuế \$10: giá người mua trả lên **\$45**, giá người bán
nhận xuống **\$35**, lượng từ 40 còn **30**.

| | Không thuế | Có thuế | Thay đổi |
| --- | ---: | ---: | ---: |
| Thặng dư tiêu dùng | 400 | 225 | **−175** |
| Thặng dư sản xuất | 400 | 225 | **−175** |
| Doanh thu thuế | 0 | 300 | **+300** |
| **Tổng** | **800** | **750** | **−50** |

Người mua và người bán mất tổng cộng **350**; chính phủ chỉ thu **300**. Chênh **50** là tổn thất vô
ích, và nó khớp đúng $\frac{1}{2} \times 10 \times 10$.

**⑤ Joe và Jane (mục 7).** Thuế \$50 làm **cả \$40 thặng dư biến mất**, và chính phủ thu **\$0**.
Đây là trường hợp cực đoan cho thấy tổn thất vô ích không phải "tiền bị lấy" mà là **giao dịch không
xảy ra**.

**⑥ Bình phương (mục 8).** Thuế 4 → 8 → 16 cho tổn thất **8 → 32 → 128**: mỗi lần thuế gấp đôi thì
tổn thất **gấp bốn**, đúng như tr. 183. Cột doanh thu thuế thì đi lên tới đỉnh **400 ở thuế \$20**
rồi đi xuống.

**⑦ Laffer (mục 9).** Chính cột doanh thu ở trên, vẽ thành hình. Ở thuế \$40 sản lượng bằng 0 nên
doanh thu bằng 0 dù thuế suất cao nhất.

**⑧ Độ co giãn (mục 10).** Cả bốn trường hợp đi qua cùng một điểm cân bằng và chịu cùng mức thuế
\$10. Kết quả: co giãn thấp → tổn thất **33,3**; co giãn cao → **80,0**. Gấp **2,4 lần**, chỉ vì độ
dốc đường khác nhau.

**⑨ Góc QTKD (mục 11).** Một giá \$300 cho doanh thu **48.000** và để lại **8.000** thặng dư trong
tay khách. Phân biệt giá ba mức cho **86.000** — tăng **79%**. Trong đó **8.000** là phần lấy lại từ
khách cũ, còn **30.000** đến từ nhóm sinh viên **trước đây không mua nổi** — phần này không lấy của
ai, nó là **tổn thất vô ích được xoá bỏ**.

---

## 16. Tự thử

Sửa tham số rồi chạy lại. Không có lời giải kèm theo.

1. Trong mục 1, thêm một người mua `("Yoko", 90)` vào `nguoi_mua`. Khi bán **2** tập đĩa, ai thắng và
   tổng thặng dư tiêu dùng bằng bao nhiêu? Vì sao thặng dư **giảm** so với trước dù có thêm người mua?
2. Trong mục 6, đổi `T = 10` thành `T = 30`. Doanh thu thuế tăng hay giảm so với `T = 10`? Còn tổn
   thất vô ích? Bạn đang đứng ở nửa nào của đường cong Laffer?
3. Trong mục 7, đổi `thue = 50` thành `thue = 30`. Giao dịch Joe–Jane còn xảy ra không? Với mức thuế
   nào thì nó **vừa đúng** biến mất? So con số đó với tổng thặng dư \$40.
4. Trong mục 10, thêm dòng `("(e) ca hai deu CO GIAN", 8, 8)`. Tổn thất vô ích bằng bao nhiêu? So với
   (b) và (d) — hai đường cùng co giãn thì tổn thất cộng lại hay nhân lên?
5. Trong mục 11, đổi `GIA_DONG = 300` thành `GIA_DONG = 150`. Doanh thu một giá bằng bao nhiêu? Có
   cao hơn 48.000 không? Và bây giờ phân biệt giá còn hơn được bao nhiêu phần trăm? Rút ra: **dư địa
   của phân biệt giá phụ thuộc vào cái gì**?

---

## 17. Từ điển thuật ngữ

Cột tiếng Anh lấy từ mục **Khái niệm then chốt** của chương 7 (tr. 170) và chương 8 (tr. 186).

| Tiếng Việt | Tiếng Anh | Ghi chú |
| --- | --- | --- |
| Kinh tế học phúc lợi | Welfare economics | ch. 7 — phân bổ nguồn lực tác động phúc lợi thế nào |
| Giá sẵn lòng trả | Willingness to pay | tr. 154 — nền của phân biệt giá (bài 7) |
| Thặng dư tiêu dùng | Consumer surplus | tr. 155 — diện tích **dưới đường cầu, trên giá** |
| Người mua cận biên | Marginal buyer | tr. 156 — người đầu tiên rời thị trường khi giá tăng |
| Chi phí | Cost | tr. 159 — là chi phí **cơ hội** |
| Thặng dư sản xuất | Producer surplus | tr. 160 — diện tích **dưới giá, trên đường cung** |
| Người bán cận biên | Marginal seller | tr. 161 |
| Tổng thặng dư | Total surplus | tr. 164 — giá trị người mua nhận − chi phí người bán chịu |
| Hiệu quả | Efficiency | tr. 164 — **quy mô** chiếc bánh |
| Bình đẳng | Equality | tr. 164 — **cách chia** chiếc bánh |
| Thất bại thị trường | Market failure | tr. 169 — quyền lực thị trường, ngoại tác |
| Tổn thất vô ích | Deadweight loss | tr. 178 — diện tích $C + E$ |
| Đường cong Laffer | Laffer curve | tr. 183 — doanh thu thuế tăng rồi giảm |
| Kinh tế học trọng cung | Supply-side economics | tr. 184 |

---

## 18. Câu hỏi tự kiểm tra

1. Một người sẵn lòng trả 200 nghìn cho một bữa ăn nhưng chỉ phải trả 150 nghìn. Thặng dư tiêu dùng
   của người đó là bao nhiêu? Nếu nhà hàng tăng giá lên 210 nghìn, thặng dư còn bao nhiêu?
2. Vì sao chiều cao của đường cầu tại lượng $Q$ lại chính là giá sẵn lòng trả của **người mua cận biên**,
   chứ không phải của người mua trung bình?
3. Khi giá giảm, phần thặng dư tiêu dùng tăng thêm gồm hai mảnh. Nêu tên và ý nghĩa kinh doanh của
   từng mảnh. Mảnh nào là "doanh số mới thật sự"?
4. Sách nói thặng dư tiêu dùng **không** là thước đo tốt cho phúc lợi trong trường hợp nào? Giả định
   nào đang bị vi phạm?
5. Viết công thức tổng thặng dư sau khi rút gọn. Vì sao khoản tiền người mua trả lại **biến mất** khỏi
   công thức? Điều đó nói gì về việc "chuyển tiền từ túi này sang túi kia"?
6. Nêu **ba** hàm ý về thị trường tự do ở tr. 165–166. Hàm ý nào nói về *phân phối cho ai*, hàm ý nào
   nói về *sản xuất bao nhiêu*?
7. Kết luận "thị trường tự do là hiệu quả" đứng trên hai giả định. Nêu cả hai, và cho một ví dụ thực tế
   vi phạm từng giả định.
8. Thuế 10 nghìn/đơn vị làm người mua mất 175, người bán mất 175, chính phủ thu 300. Tổn thất vô ích
   bằng bao nhiêu? Khoản đó đi đâu?
9. Chính phủ tăng thuế xăng lên **gấp ba**. Tổn thất vô ích tăng khoảng bao nhiêu lần? Doanh thu thuế
   có chắc chắn tăng gấp ba không? Giải thích bằng đường cong Laffer.
10. Hai thị trường có cùng mức thuế. Thị trường A có cầu và cung rất co giãn; thị trường B thì không.
    Thị trường nào chịu tổn thất vô ích lớn hơn? Nếu bạn là người thiết kế chính sách thuế và chỉ quan
    tâm tới hiệu quả, bạn đánh thuế thị trường nào?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 4 — THẶNG DƯ VÀ CHI PHÍ CỦA THUẾ      (Ch. 7–8, tr. 153–189)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Ch.4 mô hình · Ch.5 đo phản ứng · Ch.7-8 đo PHÚC LỢI                    ║
║                                                                          ║
║  ── THẶNG DƯ TIÊU DÙNG ─────────────────────────────────────────────     ║
║      = giá SẴN LÒNG TRẢ − giá THỰC TRẢ                                   ║
║      = diện tích DƯỚI đường cầu, TRÊN mức giá                            ║
║      chiều cao đường cầu tại Q = giá sẵn lòng trả của NGƯỜI MUA CẬN BIÊN ║
║      giá giảm ⟹ tăng 2 mảnh: ① khách CŨ trả ít hơn ② khách MỚI vào       ║
║      ⚠ chỉ là thước đo tốt NẾU người mua duy lý (ma tuý = phản ví dụ)    ║
║                                                                          ║
║  ── THẶNG DƯ SẢN XUẤT ──────────────────────────────────────────────     ║
║      = tiền NHẬN ĐƯỢC − CHI PHÍ (là chi phí CƠ HỘI)                      ║
║      = diện tích DƯỚI mức giá, TRÊN đường cung                           ║
║                                                                          ║
║  ⭐ TỔNG THẶNG DƯ = giá trị người mua nhận − chi phí người bán chịu       ║
║      (tiền trả và tiền nhận TRIỆT TIÊU nhau ⟹ chuyển tiền KHÔNG tạo      ║
║       ra cũng không phá huỷ phúc lợi)                                    ║
║                                                                          ║
║  ── BA HÀM Ý VỀ THỊ TRƯỜNG TỰ DO ───────────────────────────────────     ║
║      ① hàng đến người ĐỊNH GIÁ CAO NHẤT                                  ║
║      ② sản xuất bởi người CHI PHÍ THẤP NHẤT                              ║
║      ③ sản lượng TỐI ĐA HOÁ tổng thặng dư                                ║
║      Q < Q*: giá trị > chi phí ⟹ nên làm thêm                            ║
║      Q > Q*: giá trị < chi phí ⟹ nên làm ít lại                          ║
║  ⚠⚠ ĐỨNG TRÊN HAI GIẢ ĐỊNH                                               ║
║      ① cạnh tranh hoàn hảo — vi phạm ⟹ QUYỀN LỰC THỊ TRƯỜNG (bài 7-9)    ║
║      ② không tác động người ngoài — vi phạm ⟹ NGOẠI TÁC (bài 14)         ║
║      hai thứ này = THẤT BẠI THỊ TRƯỜNG                                   ║
║                                                                          ║
║  ── THUẾ ───────────────────────────────────────────────────────────     ║
║      tạo khoảng cách P_B − P_S = T, làm sản lượng GIẢM                   ║
║      đánh lên người mua hay người bán đều NHƯ NHAU                       ║
║      doanh thu thuế = T × Q  (hình chữ nhật)                             ║
║      người mua mất B+C, người bán mất D+E, chính phủ thu B+D             ║
║      ⟹ TỔN THẤT VÔ ÍCH = C + E = ½ × T × (sụt giảm sản lượng)            ║
║                                                                          ║
║  ⭐ JOE & JANE  thuế $50 xoá sạch $40 thặng dư, chính phủ thu $0          ║
║      ⟹ tổn thất vô ích KHÔNG phải tiền bị lấy, mà là GIAO DỊCH KHÔNG     ║
║        XẢY RA. Thuế làm hai bên không nhận thấy LỢI ÍCH TỪ THƯƠNG MẠI    ║
║                                                                          ║
║  ⭐ ĐỘ CO GIÃN CÀNG LỚN ⟹ TỔN THẤT VÔ ÍCH CÀNG LỚN                        ║
║      vì co giãn = đổi hành vi nhiều, mà đổi hành vi mới là nguồn tổn thất║
║      ⟹ thuế thuốc lá, rượu, xăng phổ biến vì cầu KHÔNG co giãn           ║
║                                                                          ║
║  ⭐ THUẾ GẤP ĐÔI ⟹ TỔN THẤT GẤP BỐN  (diện tích tam giác, ∝ T²)           ║
║      doanh thu thuế TĂNG rồi GIẢM = ĐƯỜNG CONG LAFFER                    ║
║      ⚠ đường cong TỒN TẠI ≠ đang ở nửa bên phải của nó                   ║
║        "hầu hết nhà kinh tế hoài nghi đề xuất của Laffer" (tr. 184)      ║
║                                                                          ║
║  💼 QTKD  thặng dư tiêu dùng = TIỀN BẠN ĐỂ LẠI TRÊN BÀN                  ║
║          một giá 48.000 → phân biệt giá 86.000 (+79%)                    ║
║          trong đó phần từ nhóm TRƯỚC KHÔNG MUA NỔI = xoá tổn thất vô ích ║
║          mọi KHOẢN PHÍ nội bộ đều gây tổn thất vô ích như thuế:          ║
║          hỏi "bao nhiêu giao dịch ĐÁNG LẼ CÓ LỢI đã không xảy ra?"       ║
║          phí gấp đôi ⟹ thiệt hại gấp bốn                                 ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **N. Gregory Mankiw, *Kinh tế học vi mô*** — bản dịch của Khoa Kinh tế, Trường ĐH Kinh tế TP.HCM,
  Cengage Learning Asia. Tệp trong kho: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  — **trang sách N = trang PDF N + 33**.
  - **Chương 7 — Người tiêu dùng, nhà sản xuất và hiệu quả của thị trường**, tr. 153–173
    - Bảng 1 *Mức sẵn lòng trả của bốn người mua tiềm năng*, tr. 154
    - Hình 1 *Biểu cầu và đường cầu*, tr. 156
    - Hình 2 *Đo lường thặng dư tiêu dùng bằng đường cầu*, tr. 157
    - Hình 3 *Tác động của giá lên thặng dư tiêu dùng*, tr. 158
    - Bảng 2 *Chi phí sản xuất của bốn nhà cung ứng tiềm năng*, tr. 159
    - Hình 4 *Đường cung và biểu cung*, tr. 160
    - Hình 5 *Đo lường thặng dư sản xuất bằng đường cung*, tr. 161
    - Hình 7 *Thặng dư sản xuất và tiêu dùng khi thị trường cân bằng*, tr. 165
    - Hình 8 *Tính hiệu quả của sản lượng cân bằng*, tr. 166
    - *Kết luận: hiệu quả thị trường và thất bại thị trường*, tr. 169
  - **Chương 8 — Ứng dụng: Chi phí của thuế**, tr. 174–189
    - Hình 1 *Tác động của thuế*, tr. 175
    - Hình 2 *Doanh thu thuế*, tr. 176
    - Hình 3 *Tác động của thuế lên phúc lợi*, tr. 177
    - Ví dụ Joe và Jane, tr. 178
    - Hình 4 *Tổn thất vô ích*, tr. 179
    - Hình 5 *Độ co giãn và tác động của thuế*, tr. 180
    - Nghiên cứu tình huống *Tranh luận về tổn thất vô ích*, tr. 181–182
    - Hình 6 *Tổn thất vô ích và doanh thu thuế thay đổi thế nào với các mức thuế*, tr. 183
    - Nghiên cứu tình huống *Đường cong Laffer và kinh tế học trọng cung*, tr. 184–185
- **Đính chính đã ghi trong bài:** tr. 178 — cùng một nhân vật được gọi là **Jeal**, **Jean** và **Jane**
  trong một trang; bản gốc dùng **Jane**. Đối chiếu bản quét 300 dpi.
- **Liên hệ chéo:**
  - [Bài 1, mục 3](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó) — chi phí là chi phí cơ hội.
  - [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) — độ co giãn, thứ quyết định độ lớn tổn thất vô ích.
  - Phân biệt giá: **bài 7** (chương 15). Ngoại tác: **bài 14** (chương 10). Kiểm soát giá và thuế: **bài 13** (chương 6).

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md) | ch. 1–2 | 🎯 |
| 2 | [Cung và cầu](bai_02_cung_va_cau.md) | ch. 4 | 🎯 |
| 3 | [Độ co giãn và định giá](bai_03_do_co_gian_va_dinh_gia.md) | ch. 5 | 🎯⭐ |
| **4** | **Thặng dư và chi phí của thuế** ← *bạn đang ở đây* | ch. 7–8 | 🔸 |
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
