# Bài 1 — Sự kiện ngẫu nhiên và giải tích kết hợp

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương I §1**, tr. 5–11.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> 📌 **Cần đọc trước:** không có — đây là bài đầu tiên.

Cả môn Xác suất Thống kê dựng trên hai thứ của bài này: **mô tả cho đúng cái gì có thể xảy ra**,
và **đếm cho đúng có bao nhiêu cách xảy ra**. Chưa làm chủ hai thứ đó thì mọi công thức
xác suất phía sau đều thành học vẹt.

## Mục lục

1. [Phép thử, kết cục và sự kiện](#1-phép-thử-kết-cục-và-sự-kiện)
2. [Không gian các sự kiện sơ cấp](#2-không-gian-các-sự-kiện-sơ-cấp)
3. [Bảy phép toán và quan hệ giữa các sự kiện](#3-bảy-phép-toán-và-quan-hệ-giữa-các-sự-kiện)
4. [📚 Luật De Morgan](#4--luật-de-morgan)
5. [Giải tích kết hợp: bốn công thức đếm](#5-giải-tích-kết-hợp-bốn-công-thức-đếm)
6. [Chọn công thức đếm nào](#6-chọn-công-thức-đếm-nào)
7. [Nhị thức Newton và hằng đẳng thức Pascal](#7-nhị-thức-newton-và-hằng-đẳng-thức-pascal)
8. [Code minh hoạ](#8-code-minh-hoạ)
9. [Tự thử](#9-tự-thử)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Phép thử, kết cục và sự kiện

Giáo trình mở đầu bằng một lời thú nhận thẳng thắn (tr. 5):

> "Khái niệm thường gặp trong lý thuyết xác suất là **sự kiện** (mà không thể định nghĩa chặt chẽ)."

Đây không phải sự lười biếng. Trong toán học, mọi hệ thống đều phải bắt đầu từ vài khái niệm
**nguyên thuỷ** không định nghĩa được (như "điểm" và "đường thẳng" trong hình học). Với xác suất,
khái niệm nguyên thuỷ đó là *sự kiện*. Ta chỉ mô tả, không định nghĩa.

Ba từ khoá phải phân biệt được:

| Từ           | Nghĩa                                                     | Thí dụ 1.1 (tr. 5)                                               |
| ------------ | --------------------------------------------------------- | ---------------------------------------------------------------- |
| **Phép thử** | thực hiện một bộ điều kiện xác định                       | gieo một con xúc sắc đồng chất trên mặt phẳng                    |
| **Kết cục**  | một kết quả có thể có của phép thử                        | xuất hiện mặt 1 chấm, mặt 2 chấm, ..., mặt 6 chấm — có 6 kết cục |
| **Sự kiện**  | một điều có thể xảy ra hoặc không, khi thực hiện phép thử | "mặt có số chấm chẵn", "mặt có số chấm là bội của 3"             |

Điểm dễ nhầm: **kết cục là trường hợp riêng của sự kiện**, chứ không phải hai loại khác nhau.
"Xuất hiện mặt 3 chấm" vừa là một kết cục, vừa là một sự kiện. Còn "số chấm chẵn" là sự kiện
nhưng không phải kết cục — nó gộp ba kết cục 2, 4, 6.

Sự kiện được đặt tên bằng chữ in hoa $A, B, C, \dots$ và chia làm ba loại:

$$
\begin{aligned}
&\textbf{Tất yếu } U && \text{chắc chắn xảy ra} && \text{nước đóng băng ở } 0^\circ C \\
&\textbf{Bất khả } V && \text{không thể xảy ra} && \text{xúc sắc ra mặt bảy chấm} \\
&\textbf{Ngẫu nhiên} && \text{có thể xảy ra hoặc không} && \text{xúc sắc ra mặt chẵn}
\end{aligned}
$$

Ký hiệu $U$ và $V$ sẽ dùng suốt chương I, nhớ kỹ. Theo một nghĩa nào đó, $U$ và $V$ chính là hai
**trường hợp cực đoan** của sự kiện ngẫu nhiên: xác suất bằng 1 và bằng 0.

### 💼 Góc QTKD

**Phép thử:** gửi 5 email chào hàng cho 5 khách hàng tiềm năng trong danh sách.

- **Kết cục:** có 0, 1, 2, 3, 4 hoặc 5 khách phản hồi — 6 kết cục.
- **Sự kiện tất yếu $U$:** "số khách phản hồi nằm trong khoảng 0 đến 5".
- **Sự kiện bất khả $V$:** "có 6 khách phản hồi".
- **Sự kiện ngẫu nhiên:** "có ít nhất 1 khách phản hồi" — thứ bạn thật sự quan tâm.

Chú ý cách phát biểu phép thử: *phải nói rõ làm gì và đo cái gì*. "Gửi email" chưa phải phép thử;
"gửi 5 email rồi đếm số phản hồi" mới là phép thử. Trong bài tập, nhiều bạn mất điểm ngay ở bước
này vì mô tả phép thử lỏng lẻo, dẫn đến đếm sai kết cục.

Một câu hỏi giáo trình đặt ra ở tr. 6 và trả lời rất đáng đọc: **do đâu có sự kiện ngẫu nhiên?**
Không phải vì thế giới vô luật, mà vì *ta thiếu tri thức, thông tin và phương tiện* (kinh phí,
thiết bị, thời gian) để nhận thức đầy đủ. Chỉ cần một thay đổi rất nhỏ của bộ điều kiện đã đổi
kết cục. Vì thế giáo trình kết luận thẳng: bài toán xác định bản chất xác suất của một sự kiện
bất kỳ trong một phép thử tuỳ ý là **không thể giải được**.

Với QTKD, đó là lời cảnh báo hữu ích: khách hàng không phải máy phát ngẫu nhiên; họ có lý do
để mua hay không mua. Ta dùng xác suất vì *không quan sát được* các lý do đó, chứ không phải
vì chúng không tồn tại.

---

## 2. Không gian các sự kiện sơ cấp

Mỗi kết cục của phép thử được gọi là một **sự kiện sơ cấp**, ký hiệu $\omega_i$.
Tập hợp tất cả sự kiện sơ cấp gọi là **không gian các sự kiện sơ cấp**:

$$\Omega = \{\omega_i,\ i \in I\}$$

trong đó $I$ là tập chỉ số, **có thể vô hạn** (đếm được hoặc không đếm được).

Ở thí dụ 1.1, nếu $A_i$ là sự kiện "xuất hiện mặt $i$ chấm" thì

$$\Omega = \{A_1, A_2, A_3, A_4, A_5, A_6\}$$

**Thí dụ 1.3 (tr. 8).** Chọn từ một lô hàng ra 5 sản phẩm, quan tâm số phế phẩm.

a) Xác định các sự kiện sơ cấp.
b) Biểu diễn: "có nhiều nhất 1 phế phẩm", "có không quá 4 phế phẩm", "có ít nhất 1 phế phẩm".

*Giải.* Đặt $A_i$ = "trong 5 sản phẩm có $i$ phế phẩm", $i = \overline{0,5}$. Vậy

$$\Omega = \{A_0, A_1, A_2, A_3, A_4, A_5\}$$

Ba sự kiện cần tìm:

$$
\begin{aligned}
A &= A_0 + A_1 && \text{(nhiều nhất 1 phế phẩm)} \\
B &= A_0 + A_1 + A_2 + A_3 + A_4 = \overline{A_5} && \text{(không quá 4 phế phẩm)} \\
C &= A_1 + A_2 + A_3 + A_4 + A_5 = \overline{A_0} && \text{(ít nhất 1 phế phẩm)}
\end{aligned}
$$

Hai dòng cuối là **mẹo cực kỳ hay dùng**: thay vì cộng 5 sự kiện, viết thành *đối lập của một
sự kiện*. Ở bài 2 khi tính xác suất, việc này giảm 5 phép tính xuống còn 1.

⚠️ **Cẩn thận với $\Omega$.** Cùng một phép thử vật lý, nếu đo đại lượng khác thì $\Omega$ khác hẳn.
Vẫn lấy 5 sản phẩm, nhưng nếu quan tâm *sản phẩm nào bị lỗi* (chứ không chỉ có bao nhiêu cái lỗi)
thì $\Omega$ có $2^5 = 32$ phần tử, không phải 6. Câu hỏi quyết định $\Omega$, không phải phép thử.

### 💼 Góc QTKD

Một cửa hàng theo dõi doanh thu ngày, phân loại theo mức: dưới 10 triệu, 10–20 triệu, trên 20 triệu.

$$\Omega = \{L, M, H\}$$

Sự kiện "hôm nay không phải ngày tệ" $= \overline{L} = M + H$.

Nhưng nếu bài toán là *doanh thu chính xác bao nhiêu đồng*, thì $\Omega = [0, +\infty)$ — vô hạn
không đếm được. Đây chính là ranh giới giữa **biến ngẫu nhiên rời rạc** và **liên tục** mà bài 5
sẽ xử lý. Ba mức $L, M, H$ là rời rạc; số tiền là liên tục.

---

## 3. Bảy phép toán và quan hệ giữa các sự kiện

Giáo trình liệt kê bảy mục (tr. 6–7). Cột "tương ứng tập hợp" là chìa khoá để nhớ:
**sự kiện chính là tập hợp**, phép toán trên sự kiện chính là phép toán trên tập hợp.

| #   | Tên             | Ký hiệu                        | Nghĩa                                  | Tương ứng tập hợp            |
| --- | --------------- | ------------------------------ | -------------------------------------- | ---------------------------- |
| i   | **Tổng**        | $A + B$                        | xuất hiện **ít nhất một** trong hai    | hợp $A \cup B$               |
| ii  | **Tích**        | $AB$                           | xuất hiện **đồng thời** cả hai         | giao $A \cap B$              |
| iii | **Đối lập**     | $\overline{A}$                 | **không** xuất hiện $A$                | phần bù $\Omega \setminus A$ |
| iv  | **Xung khắc**   | $AB = V$                       | không thể đồng thời xảy ra             | rời nhau                     |
| v   | **Kéo theo**    | $A \Rightarrow B$              | có $A$ thì có $B$                      | $A \subset B$                |
| vi  | **Tương đương** | $A = B$                        | có cái này thì có cái kia và ngược lại | bằng nhau                    |
| vii | **Hiệu**        | $A - B$ (hay $A \backslash B$) | có $A$ nhưng không có $B$              | $A \cap \overline{B}$        |

Ba đẳng thức về đối lập cần thuộc lòng (tr. 7):

$$\overline{\overline{A}} = A, \qquad A + \overline{A} = U, \qquad A\,\overline{A} = V, \qquad \overline{U} = V$$

Và các luật đại số, đọc thấy quen vì y hệt luật của tập hợp (tr. 8):

$$
\begin{aligned}
A + B &= B + A, & AB &= BA && \text{(giao hoán)} \\
A + (B + C) &= (A + B) + C, & A(BC) &= (AB)C && \text{(kết hợp)} \\
A(B + C) &= AB + AC & & && \text{(phân phối)} \\
A + U &= U, & A + V &= A, & A + A &= A \\
AU &= A, & AV &= V, & AA &= A
\end{aligned}
$$

⚠️ **Dấu $+$ ở đây không phải phép cộng số học.** $A + A = A$, chứ không phải $2A$. Ký hiệu $+$
chỉ là quy ước của trường phái xác suất Nga (giáo trình này theo trường phái đó); sách tiếng Anh
viết $A \cup B$. Nếu đọc song song hai loại sách, đừng bị rối.

**Thí dụ 1.4 (tr. 8).** Mạng điện gồm 3 bóng đèn. Mạng mất điện (sự kiện $A$) chỉ có thể do
cháy bóng ($A_i$ = bóng $i$ cháy). Biểu diễn $A$ theo $A_i$.

*Giải.* $A$ xuất hiện khi xảy ra một trong 3 trường hợp: (i) cả ba bóng cháy, (ii) cháy bóng 1 và 2,
(iii) cháy bóng 1 và 3. Từ đó

$$A = A_1 A_2 A_3 + A_1 A_2 \overline{A_3} + A_1 \overline{A_2} A_3$$

Dùng tính chất mạng nối tiếp – song song, ta có cách viết gọn hơn nhiều (tr. 9):

$$A = A_1 (A_2 + A_3)$$

Đọc câu này: mạng chết khi **bóng 1 cháy** *và* (**bóng 2 cháy** *hoặc* **bóng 3 cháy**). Nghĩa là
bóng 1 mắc nối tiếp, còn bóng 2 và 3 mắc song song với nhau.

Bài học rút ra: **cấu trúc vật lý của hệ thống dịch thẳng thành biểu thức đại số sự kiện.**
Nối tiếp → phép nhân (cần *tất cả* cùng hỏng thì mới đứt... hoặc cần *tất cả* cùng tốt thì mới chạy,
tuỳ bạn viết theo hỏng hay theo tốt). Song song → phép cộng.

### 💼 Góc QTKD

Một doanh nghiệp có chuỗi cung ứng: nguyên liệu chỉ mua từ nhà cung cấp $N_1$ (độc quyền),
còn khâu vận chuyển thì có hai đối tác $V_2$ và $V_3$ có thể thay nhau.

Gọi $A_i$ = "đối tác $i$ ngừng phục vụ". Sản xuất bị đình trệ khi:

$$A = A_1 + A_2 A_3$$

Đọc: đứt hàng khi **nhà cung cấp nguyên liệu chết**, *hoặc* **cả hai hãng vận chuyển cùng chết**.

So sánh với thí dụ 1.4 để thấy sự khác biệt: ở đó công thức là $A_1(A_2 + A_3)$, ở đây là
$A_1 + A_2 A_3$. Đảo dấu cộng và nhân vì ở đó $A_i$ nghĩa là "cháy" trong một mạng mà cháy
mới ngắt điện, còn ở đây $N_1$ độc quyền nên chỉ mình nó chết là đủ chết cả chuỗi.

**Đây là bài học quản trị rủi ro cơ bản:** thành phần mắc *nối tiếp* (một điểm chết) là điểm
yếu; thành phần mắc *song song* (có dự phòng) là điểm mạnh. Bài 3 sẽ cho bạn con số cụ thể:
hai nhà vận chuyển dự phòng, mỗi hãng có 10% khả năng chết, thì rủi ro đứt vận chuyển tụt
từ 10% xuống 1%.

---

## 4. 📚 Luật De Morgan

Giáo trình đẩy công thức này xuống phần bài tập (bài 2, tr. 35) mà không giải, nhưng nó xuất hiện
dày đặc ở chương sau nên cần nắm ngay:

$$\overline{A + B} = \overline{A} \cdot \overline{B}, \qquad \overline{AB} = \overline{A} + \overline{B}$$

Đọc bằng lời:

- **"Không có cái nào trong hai"** $=$ **"không có cái này *và* không có cái kia"**.
- **"Không phải cả hai cùng có"** $=$ **"thiếu cái này *hoặc* thiếu cái kia"**.

Chứng minh bằng lời cho vế thứ nhất: $\overline{A+B}$ xảy ra $\iff$ không xuất hiện ít nhất một
trong hai $\iff$ không xuất hiện $A$ và cũng không xuất hiện $B$ $\iff$ $\overline{A}\,\overline{B}$. ∎

Mở rộng cho $n$ sự kiện:

$$\overline{A_1 + A_2 + \dots + A_n} = \overline{A_1}\,\overline{A_2}\cdots\overline{A_n}$$

**Vì sao quan trọng?** Vì "ít nhất một" là dạng câu hỏi phổ biến nhất trong đề thi, và tính trực tiếp
thì rất mệt. De Morgan cho ta lối tắt: chuyển "ít nhất một" thành "không cái nào" rồi lấy phần bù.

Bạn đã gặp mẹo này ở thí dụ 1.3 mục 2: $C = \overline{A_0}$. Ở bài 3 nó sẽ thành công thức

$$P(\text{ít nhất một}) = 1 - P(\text{không cái nào})$$

và bạn sẽ dùng nó gần như mọi bài tập.

### 💼 Góc QTKD

Chiến dịch marketing chạy trên 3 kênh: Facebook ($A_1$), Google ($A_2$), TikTok ($A_3$).
$A_i$ = "kênh $i$ mang về ít nhất một đơn hàng".

"Chiến dịch thất bại hoàn toàn" $= \overline{A_1 + A_2 + A_3} = \overline{A_1}\,\overline{A_2}\,\overline{A_3}$
— cả ba kênh cùng không ra đơn nào.

Nên nếu bạn muốn biết xác suất chiến dịch *có* ra đơn, đừng cộng ba kênh (sẽ đếm trùng khách
mua qua nhiều kênh). Hãy tính xác suất cả ba cùng trượt rồi lấy $1$ trừ đi.

---

## 5. Giải tích kết hợp: bốn công thức đếm

Đây là phần "cày" của bài. Toàn bộ quy về **một mô hình duy nhất** (tr. 9):

> Chọn hú hoạ ra $k$ phần tử từ $n$ phần tử cho trước.

Hai câu hỏi tách ra bốn trường hợp:

|               | **Có phân biệt thứ tự**          | **Không phân biệt thứ tự**    |
| ------------- | -------------------------------- | ----------------------------- |
| **Không lặp** | Chỉnh hợp $A_n^k$                | Tổ hợp $C_n^k$                |
| **Có lặp**    | Chỉnh hợp lặp $\overline{A}_n^k$ | *(không có trong giáo trình)* |

Trường hợp thứ tư (không thứ tự, có lặp) tồn tại trong toán tổ hợp — gọi là *tổ hợp lặp*,
bằng $C_{n+k-1}^{k}$ — nhưng giáo trình không dạy và đề thi không hỏi. Bỏ qua.

### 5.1. Chỉnh hợp

**Chỉnh hợp chập $k$ từ $n$** là một nhóm **có thứ tự** gồm $k$ phần tử **khác nhau** lấy từ $n$
đã cho. Số các chỉnh hợp, với $k \le n$:

$$A_n^k = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!} \tag{1.1}$$

Cách nhớ: vế giữa là **tích của $k$ số nguyên liên tiếp đếm lùi từ $n$**. Chọn phần tử đầu có
$n$ cách, chọn phần tử thứ hai còn $n-1$ cách (vì đã lấy mất một), ..., đến phần tử thứ $k$ còn
$n-k+1$ cách. Nhân lại.

### 5.2. Chỉnh hợp lặp

**Chỉnh hợp lặp chập $k$ từ $n$** là nhóm **có thứ tự** gồm $k$ phần tử **có thể giống nhau**:

$$\overline{A}_n^k = n^k \tag{1.2}$$

Cách nhớ: mỗi vị trí trong $k$ vị trí đều được chọn tự do từ $n$ phần tử, độc lập với các vị trí
khác. $n \times n \times \cdots \times n$ ($k$ lần).

Chú ý ở đây **$k$ được phép lớn hơn $n$**, khác hẳn ba công thức kia.

### 5.3. Hoán vị

**Hoán vị của $n$** là nhóm gồm cả $n$ phần tử được sắp theo một thứ tự nào đó:

$$P_n = n! \tag{1.3}$$

Đây chỉ là trường hợp riêng của chỉnh hợp khi $k = n$: $A_n^n = \dfrac{n!}{0!} = n!$.

### 5.4. Tổ hợp

**Tổ hợp chập $k$ từ $n$** là nhóm **không phân biệt thứ tự** gồm $k$ phần tử **khác nhau**:

$$C_n^k = \frac{A_n^k}{k!} = \frac{n!}{k!\,(n-k)!} \tag{1.4}$$

Đây là công thức quan trọng nhất của bài, cũng là công thức xuất hiện nhiều nhất trong cả môn học.

**Vì sao chia cho $k!$?** Vì mỗi nhóm $k$ phần tử có thể xếp theo $k!$ thứ tự khác nhau, mà tổ hợp
coi tất cả $k!$ cách xếp đó là **cùng một nhóm**. Chỉnh hợp đếm chúng thành $k!$ nhóm riêng, nên
muốn ra tổ hợp phải chia bớt đi.

Viết lại quan hệ này cho dễ nhớ — nó là cây cầu nối hai công thức:

$$\boxed{A_n^k = C_n^k \cdot k!}$$

Đọc: *"Chọn rồi mới xếp."* Muốn có một nhóm có thứ tự, hãy chọn $k$ người ($C_n^k$ cách),
rồi xếp $k$ người đó vào $k$ vị trí ($k!$ cách).

### 5.5. Bốn thí dụ của giáo trình

**Thí dụ 1.5 (tr. 10).** Tập $\{a, b, c\}$, tạo nhóm 2 phần tử.

| Điều kiện               | Công thức                | Kết quả | Liệt kê                     |
| ----------------------- | ------------------------ | ------- | --------------------------- |
| có thứ tự, không lặp    | $A_3^2 = 3 \cdot 2$      | 6       | $ab, ba, ac, ca, bc, cb$    |
| có thứ tự, có lặp       | $\overline{A}_3^2 = 3^2$ | 9       | 6 nhóm trên $+\ aa, bb, cc$ |
| không thứ tự, không lặp | $C_3^2$                  | 3       | $ab, ac, bc$                |

**Thí dụ 1.6 (tr. 10).** Một lớp phải học 6 môn trong học kỳ, mỗi ngày học 3 môn. Có bao nhiêu
cách xếp thời khoá biểu trong 1 ngày?

*Giải.* Hai thời khoá biểu khác nhau nếu **có ít nhất một môn khác nhau, hoặc thứ tự môn khác nhau**
— tức là có phân biệt thứ tự, không lặp (một ngày không học một môn hai lần). Theo (1.1):

$$A_6^3 = 6 \cdot 5 \cdot 4 = 120 \text{ cách}$$

**Thí dụ 1.7 (tr. 10).** Có thể đánh số được bao nhiêu xe nếu chỉ dùng 3 con số từ 1 đến 5?

*Giải.* Biển số 3 chữ số, mỗi chữ số lấy từ 5 giá trị, **được phép lặp** (biển 111 hợp lệ), có thứ tự
(112 khác 121). Theo (1.2):

$$\overline{A}_5^3 = 5^3 = 125 \text{ xe}$$

**Thí dụ 1.8 (tr. 10).** Có bao nhiêu cách lập một hội đồng gồm 3 người chọn trong số 8 người?

*Giải.* Hội đồng không phân biệt thứ tự (3 người này lập hội đồng, ai đứng trước ai không quan
trọng). Theo (1.4):

$$C_8^3 = \frac{8!}{3!\,5!} = 56 \text{ cách}$$

### 💼 Góc QTKD

Cùng một phòng ban 8 nhân viên, ba câu hỏi khác nhau ra ba con số khác nhau:

| Câu hỏi                                                                 | Thứ tự? | Lặp?   | Công thức                | Kết quả |
| ----------------------------------------------------------------------- | ------- | ------ | ------------------------ | ------- |
| Lập tổ dự án 3 người, vai trò như nhau                                  | không   | không  | $C_8^3$                  | **56**  |
| Bổ nhiệm 3 vị trí: trưởng nhóm, phụ trách kỹ thuật, phụ trách tài chính | **có**  | không  | $A_8^3$                  | **336** |
| Xếp lịch trực 3 ca trong tuần, một người có thể trực nhiều ca           | **có**  | **có** | $\overline{A}_8^3 = 8^3$ | **512** |

Ba tình huống nghe rất giống nhau trong lời nói hàng ngày, nhưng đáp số chênh gần 10 lần.
**Đọc kỹ đề là kỹ năng quan trọng hơn nhớ công thức.**

Vẫn cùng phòng ban đó, thêm một bài toán mã hoá sản phẩm:

> Công ty cần mã SKU 3 ký tự, lấy từ 5 chữ cái `A B C D E`, cho phép trùng. Được bao nhiêu mã?

$$\overline{A}_5^3 = 5^3 = 125 \text{ mã}$$

Đúng bằng thí dụ 1.7 của giáo trình — cùng bài toán, đổi vỏ từ biển số xe sang mã SKU. Rất nhiều
bài toán kinh doanh chỉ là bài toán giáo trình đội lốt.

---

## 6. Chọn công thức đếm nào

Quy trình 3 câu hỏi, làm theo đúng thứ tự này thì không bao giờ chọn nhầm:

```
        Bài toán đếm số cách chọn k từ n
                      │
        ┌─────────────┴─────────────┐
   Câu 1: Có lấy hết n phần tử không?
        │ CÓ (k = n)                │ KHÔNG (k < n)
        ▼                           ▼
    Hoán vị P_n = n!        Câu 2: Đổi chỗ 2 phần tử
                            thì có ra kết quả khác không?
                                    │
                    ┌───────────────┴───────────────┐
                 CÓ (có thứ tự)              KHÔNG (không thứ tự)
                    │                               │
        Câu 3: Một phần tử được                     ▼
        chọn nhiều lần không?                  Tổ hợp C(n,k)
                    │
        ┌───────────┴───────────┐
      CÓ                      KHÔNG
        ▼                       ▼
  Chỉnh hợp lặp n^k     Chỉnh hợp A(n,k)
```

Mẹo phát hiện "có thứ tự" trong đề bài — tìm các từ khoá sau:

| Có thứ tự                            | Không thứ tự                          |
| ------------------------------------ | ------------------------------------- |
| xếp, sắp, bố trí, lịch, hàng, dãy    | chọn, lấy ra, nhóm, tổ, hội đồng, mẫu |
| chức vụ khác nhau, giải nhất nhì ba  | vai trò như nhau, cùng chức danh      |
| biển số, mã, mật khẩu, số điện thoại | tập con, tổ hợp món                   |

Mẹo phát hiện "có lặp": trong đề có chữ **"có hoàn lại"**, **"trả lại rồi lấy tiếp"**, hoặc bản chất
bài toán cho phép trùng (biển số, mã, ca trực).

---

## 7. Nhị thức Newton và hằng đẳng thức Pascal

Giáo trình khép §1 bằng hai kết quả (tr. 11) mà chương II sẽ dùng lại liên tục.

**Nhị thức Newton:**

$$(x + a)^n = C_n^0 x^n + C_n^1 x^{n-1} a + \dots + C_n^k x^{n-k} a^k + \dots + C_n^n a^n = \sum_{k=0}^{n} C_n^k x^{n-k} a^k$$

Đây chính là **lý do tổ hợp có tên "hệ số nhị thức"**. Và nó chính là bộ khung của
**phân phối nhị thức** ở bài 7 — thay $x = q$, $a = p$ với $p + q = 1$ thì vế trái bằng $1$,
còn vế phải là tổng tất cả các xác suất của lược đồ Bernoulli. Tổng bằng 1: đúng như phải thế.

**Hằng đẳng thức Pascal** (giáo trình gợi ý tự chứng minh, để ý $C_n^0 = C_n^n = 1$):

$$C_n^k = C_{n-1}^{k-1} + C_{n-1}^{k}$$

Chứng minh bằng lời, không cần tính: muốn chọn $k$ người từ $n$ người, hãy nhìn vào **một người
cụ thể** — gọi là anh X.

- Nếu **có** anh X trong nhóm: còn phải chọn $k-1$ người từ $n-1$ người còn lại → $C_{n-1}^{k-1}$ cách.
- Nếu **không có** anh X: phải chọn đủ $k$ người từ $n-1$ người còn lại → $C_{n-1}^{k}$ cách.

Hai trường hợp xung khắc và phủ hết mọi khả năng, nên cộng lại. ∎

Đây cũng là quy tắc dựng **tam giác Pascal**: mỗi số bằng tổng hai số trên nó.

```
n=0                 1
n=1               1   1
n=2             1   2   1
n=3           1   3   3   1
n=4         1   4   6   4   1
n=5       1   5  10  10   5   1
n=6     1   6  15  20  15   6   1
```

Hàng $n = 5$ đọc ra ngay: $C_5^0 = 1$, $C_5^1 = 5$, $C_5^2 = 10$, $C_5^3 = 10$, $C_5^4 = 5$, $C_5^5 = 1$.
Tổng một hàng luôn bằng $2^n$ (đặt $x = a = 1$ trong nhị thức Newton) — chính là số tập con của
một tập $n$ phần tử.

---

## 8. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-01-su-kien.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.

Code này không dạy thêm lý thuyết; nó **kiểm chứng** rằng bốn công thức đếm ở mục 5 khớp với
phép liệt kê thật, và tính luôn ba con số của Góc QTKD.

```python
"""Bài 1 — Sự kiện ngẫu nhiên và giải tích kết hợp."""

from itertools import combinations, permutations, product
from math import comb, factorial, perm

# ─────────────────────────────────────────────────────────────
# 1. Không gian sự kiện sơ cấp — Thí dụ 1.3 (giáo trình tr. 8)
#    Lấy 5 sản phẩm, quan tâm số phế phẩm.
# ─────────────────────────────────────────────────────────────
LOT_SIZE = 5
omega = [f"A{i}" for i in range(LOT_SIZE + 1)]  # A0..A5
print("Omega =", omega, "| so su kien so cap:", len(omega))

# A = "co nhieu nhat 1 phe pham", B = "co khong qua 4", C = "co it nhat 1"
A = {"A0", "A1"}
B = set(omega) - {"A5"}
C = set(omega) - {"A0"}
print("A =", sorted(A), "| B = doi lap cua A5:", B == set(omega) - {"A5"})
print("C = doi lap cua A0:", C == set(omega) - {"A0"})

# Luật De Morgan kiểm trên chính Omega này
U = set(omega)
assert U - (A | C) == (U - A) & (U - C)
assert U - (A & C) == (U - A) | (U - C)
print("De Morgan: OK")

# ─────────────────────────────────────────────────────────────
# 2. Bốn công thức đếm — đối chiếu công thức với phép liệt kê thật
#    Thí dụ 1.5, tập {a, b, c}, chọn 2 phần tử.
# ─────────────────────────────────────────────────────────────
items = ["a", "b", "c"]
k = 2

arrangements = list(permutations(items, k))        # chỉnh hợp A(3,2)
with_repeat = list(product(items, repeat=k))       # chỉnh hợp lặp 3^2
orderings = list(permutations(items))              # hoán vị P(3)
subsets = list(combinations(items, k))             # tổ hợp C(3,2)

print()
print(f"{'Khai niem':<22}{'Cong thuc':>12}{'Liet ke':>10}")
for name, formula, listed in [
    ("Chinh hop A(3,2)", perm(3, 2), len(arrangements)),
    ("Chinh hop lap 3^2", 3**2, len(with_repeat)),
    ("Hoan vi P(3)", factorial(3), len(orderings)),
    ("To hop C(3,2)", comb(3, 2), len(subsets)),
]:
    assert formula == listed, name
    print(f"{name:<22}{formula:>12}{listed:>10}")
print("To hop C(3,2) =", ["".join(s) for s in subsets])

# ─────────────────────────────────────────────────────────────
# 3. Góc QTKD — ba bài toán đếm có thật trong doanh nghiệp
# ─────────────────────────────────────────────────────────────
print()
# (a) Lập tổ dự án 3 người từ 8 nhân viên — không phân biệt vai trò
print("(a) To du an 3 nguoi tu 8 nhan vien   :", comb(8, 3), "cach")
# (b) Cùng 8 người nhưng 3 vai trò khác nhau: trưởng nhóm / kỹ thuật / tài chính
print("(b) Cung 8 nguoi, 3 vai tro khac nhau :", perm(8, 3), "cach")
# (c) Mã SKU 3 ký tự lấy từ 5 chữ cái, cho phép lặp
print("(c) Ma SKU 3 ky tu tu 5 chu cai       :", 5**3, "ma")
assert comb(8, 3) == 56 and perm(8, 3) == 336 and 5**3 == 125

# ─────────────────────────────────────────────────────────────
# 4. Vì sao "vai trò" làm số cách gấp 6 lần?
#    A(n,k) = C(n,k) * k!  — chọn xong rồi mới xếp vai
# ─────────────────────────────────────────────────────────────
assert perm(8, 3) == comb(8, 3) * factorial(3)
print()
print(f"A(8,3) = C(8,3) * 3! = {comb(8, 3)} * {factorial(3)} = {perm(8, 3)}")

# Hằng đẳng thức Pascal (tr. 11): C(n,k) = C(n-1,k-1) + C(n-1,k)
for n in range(1, 12):
    for j in range(1, n):
        assert comb(n, j) == comb(n - 1, j - 1) + comb(n - 1, j)
print("Hang dang thuc Pascal dung voi moi n <= 11: OK")
```

Kết quả chạy thật:

```
Omega = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'] | so su kien so cap: 6
A = ['A0', 'A1'] | B = doi lap cua A5: True
C = doi lap cua A0: True
De Morgan: OK

Khai niem                Cong thuc   Liet ke
Chinh hop A(3,2)                 6         6
Chinh hop lap 3^2                9         9
Hoan vi P(3)                     6         6
To hop C(3,2)                    3         3
To hop C(3,2) = ['ab', 'ac', 'bc']

(a) To du an 3 nguoi tu 8 nhan vien   : 56 cach
(b) Cung 8 nguoi, 3 vai tro khac nhau : 336 cach
(c) Ma SKU 3 ky tu tu 5 chu cai       : 125 ma

A(8,3) = C(8,3) * 3! = 56 * 6 = 336
Hang dang thuc Pascal dung voi moi n <= 11: OK
```

Điểm cần để ý: `math.comb`, `math.perm`, `math.factorial` là hàm **có sẵn trong Python từ 3.8**,
không cần cài gì. Trong Excel, ba hàm tương đương là `COMBIN(n,k)`, `PERMUT(n,k)`, `FACT(n)`.

---

## 9. Tự thử

Sửa code ở mục 8 rồi quan sát. Không có lời giải ở đây — chạy thử là biết.

1. Đổi `LOT_SIZE = 5` thành `20`. $|\Omega|$ ra bao nhiêu? Vì sao không phải $2^{20}$?
   (Gợi ý: đọc lại ô ⚠️ ở mục 2.)
2. Đổi `items` thành `["a", "b", "c", "d"]` và `k = 3`. Dự đoán 4 con số **trước khi chạy**,
   rồi chạy để kiểm tra. Tỷ số giữa chỉnh hợp và tổ hợp bằng bao nhiêu? Có đúng bằng $k!$ không?
3. Thêm dòng in ra `sum(comb(6, j) for j in range(7))`. Kết quả có bằng $2^6$ không?
   Giải thích bằng ý nghĩa "số tập con".
4. Viết thêm một khối kiểm chứng nhị thức Newton bằng số: với $n = 5$, $x = 2$, $a = 3$,
   so sánh `(2+3)**5` với `sum(comb(5,j) * 2**(5-j) * 3**j for j in range(6))`.

---

## 10. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)       | Tiếng Anh                     | Ghi chú                            |
| ----------------------------- | ----------------------------- | ---------------------------------- |
| Phép thử                      | Experiment / Trial            | bộ điều kiện xác định được lặp lại |
| Kết cục                       | Outcome                       | một kết quả có thể có              |
| Sự kiện                       | Event                         | tập hợp các kết cục                |
| Sự kiện sơ cấp                | Elementary event              | một kết cục đơn lẻ, $\omega_i$     |
| Không gian các sự kiện sơ cấp | Sample space                  | $\Omega$                           |
| Sự kiện tất yếu               | Certain event                 | $U$, chắc chắn xảy ra              |
| Sự kiện bất khả               | Impossible event              | $V$, không thể xảy ra              |
| Đối lập                       | Complement                    | $\overline{A}$                     |
| Xung khắc                     | Mutually exclusive / Disjoint | $AB = V$                           |
| Giải tích kết hợp             | Combinatorics                 | toán tổ hợp                        |
| Chỉnh hợp                     | Arrangement / $k$-permutation | $A_n^k$, có thứ tự                 |
| Chỉnh hợp lặp                 | Arrangement with repetition   | $\overline{A}_n^k = n^k$           |
| Hoán vị                       | Permutation                   | $P_n = n!$                         |
| Tổ hợp                        | Combination                   | $C_n^k$, không thứ tự              |
| Luật De Morgan             | De Morgan's laws              |                                    |
| Nhị thức Newton              | Binomial theorem              | Newton                             |
| Tam giác Pascal              | Pascal's triangle             |                                    |

⚠️ **Bẫy phiên âm — đọc kỹ mục này một lần rồi quên nó đi.**
Giáo trình in năm 1997 viết tên riêng theo lối **phiên âm tiếng Việt**. Khoá học này luôn
dùng **tên gốc**, vì đó là thứ bạn gõ vào Google, đọc trong sách tiếng Anh và thấy trong
tên hàm của mọi phần mềm thống kê. Bảng đối chiếu để bạn đọc được bản in:

| Sách in (phiên âm) | Khoá học dùng   | Sách in (phiên âm) | Khoá học dùng  |
| ------------------ | --------------- | ------------------ | -------------- |
| Béc-nu-li          | **Bernoulli**   | Stiu-đơn           | **Student**    |
| Bay-ét             | **Bayes**       | Phi-sơ             | **Fisher**     |
| Poa-xông           | **Poisson**     | Sne-đơ-co          | **Snedecor**   |
| Láp-la-xơ          | **Laplace**     | Piếc-xơn           | **Pearson**    |
| Gao-xơ             | **Gauss**       | Kôn-mô-gô-rôp      | **Kolmogorov** |
| Trê-bư-sép         | **Chebyshev**   | Moa-vrơ            | **de Moivre**  |
| Đơ Moóc-găng       | **De Morgan**   | Niu-tơn            | **Newton**     |
| Pa-xcan            | **Pascal**      | Buýt-phông         | **Buffon**     |
| Cô-si              | **Cauchy**      | Vây-bun            | **Weibull**    |
| Nây-man            | **Neyman**      | Cra-me             | **Cramér**     |
| Lin-đơ-bớc – Lê-vi | **Lindeberg – Lévy** | Gli-ven-cô – Can-te-li | **Glivenko – Cantelli** |

Riêng "phân phối **khi bình phương**" — "khi" là phiên âm của chữ Hy Lạp $\chi$ (*chi*).
Khoá học viết **$\chi^2$** hoặc **chi bình phương**, tiếng Anh là *chi-squared*.

---

## 11. Câu hỏi tự kiểm tra

1. Phép thử "gieo 2 con xúc sắc phân biệt và ghi lại cặp số chấm" có bao nhiêu sự kiện sơ cấp?
   Còn phép thử "gieo 2 con xúc sắc giống nhau và ghi lại tổng số chấm"?
2. Biểu diễn sự kiện "có đúng một trong hai sự kiện $A$, $B$ xảy ra" qua $A$, $B$ và các phép toán.
3. Cho $A \Rightarrow B$. Rút gọn $A + B$ và $AB$.
4. Một quán cà phê có 7 loại đồ uống. Khách gọi 3 ly.
   a) Nếu 3 ly phải khác loại và bạn cần biết ly nào đến trước để phục vụ đúng thứ tự?
   b) Nếu 3 ly phải khác loại, thứ tự không quan trọng?
   c) Nếu khách được gọi trùng loại và bạn ghi theo thứ tự gọi?
5. Vì sao $A_n^k = C_n^k \cdot k!$ mà không phải $C_n^k = A_n^k \cdot k!$? Giải thích bằng lời,
   đừng bằng công thức.
6. Doanh nghiệp có 3 máy chủ. Hệ thống chết khi **cả ba** máy cùng chết. Viết sự kiện "hệ thống
   chết" theo $A_i$ = "máy $i$ chết". Sau đó dùng De Morgan viết sự kiện "hệ thống còn sống".
7. Bài 3 (tr. 35): có bao nhiêu số tự nhiên mà mỗi số có 4 chữ số? (Cẩn thận: chữ số đầu không
   được là 0.)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 1 — SỰ KIỆN NGẪU NHIÊN VÀ GIẢI TÍCH KẾT HỢP    (Ch. I §1, tr. 5–11) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BA KHÁI NIỆM GỐC                                                        ║
║    Phép thử  → bộ điều kiện xác định, lặp lại được                       ║
║    Kết cục   → một kết quả có thể có  (= sự kiện sơ cấp ω)               ║
║    Sự kiện   → tập hợp các kết cục    (A, B, C ...)                      ║
║    Ω = tập tất cả kết cục.  U = tất yếu.  V = bất khả.                   ║
║                                                                          ║
║  BẢY PHÉP TOÁN — sự kiện chính là tập hợp                                ║
║    A + B  tổng   ít nhất một      ↔  A ∪ B                               ║
║    A B    tích   đồng thời cả hai ↔  A ∩ B                               ║
║    Ā      đối lập                 ↔  phần bù                             ║
║    AB = V xung khắc               ↔  rời nhau                            ║
║    A ⇒ B  kéo theo                ↔  A ⊂ B                               ║
║    A − B  hiệu   có A không B     ↔  A ∩ B̄                              ║
║                                                                          ║
║    Ā̄ = A      A + Ā = U      A·Ā = V      A + A = A      A·A = A         ║
║                                                                          ║
║  DE MORGAN        ‾A‾+‾B‾ = Ā·B̄        ‾A‾B‾ = Ā + B̄                    ║
║    → "ít nhất một"  luôn đổi thành  1 − P(không cái nào)                 ║
║                                                                          ║
║  BỐN CÔNG THỨC ĐẾM — chọn k từ n                                         ║
║  ┌──────────────┬──────────────────────┬─────────────────────┐           ║
║  │              │  CÓ phân biệt thứ tự │  KHÔNG phân biệt    │           ║
║  ├──────────────┼──────────────────────┼─────────────────────┤           ║
║  │ KHÔNG lặp    │  A(n,k) = n!/(n−k)!  │  C(n,k) = n!/k!(n−k)!│          ║
║  │ CÓ lặp       │  n^k                 │  (ngoài chương trình)│          ║
║  └──────────────┴──────────────────────┴─────────────────────┘           ║
║    k = n, có thứ tự  →  hoán vị  P(n) = n!                               ║
║    CẦU NỐI:  A(n,k) = C(n,k) · k!    "chọn xong rồi mới xếp"             ║
║                                                                          ║
║  QUY TRÌNH 3 CÂU HỎI                                                     ║
║    1. Lấy hết n phần tử?           → có: P(n) = n!                       ║
║    2. Đổi chỗ có ra kết quả khác?  → không: C(n,k)                       ║
║    3. Được chọn trùng?             → có: n^k   |  không: A(n,k)          ║
║                                                                          ║
║  PASCAL   C(n,k) = C(n−1,k−1) + C(n−1,k)      Σ C(n,k) = 2^n             ║
║  NEWTON   (x+a)^n = Σ C(n,k)·x^(n−k)·a^k      → nền của bài 7            ║
║                                                                          ║
║  💼 QTKD:  8 nhân viên chọn 3                                            ║
║       tổ dự án (vai trò như nhau)      C(8,3) =  56                      ║
║       bổ nhiệm 3 chức vụ khác nhau     A(8,3) = 336                      ║
║       xếp 3 ca trực, được trùng người      8³ = 512                      ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương I §1, tr. 5–11.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Luật De Morgan: bài tập 2, tr. 35 (giáo trình nêu, không giải — mục 4 của bài này giải).

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) · Bài trước: — · Bài sau: Bài 2 — Ba định nghĩa của xác suất
