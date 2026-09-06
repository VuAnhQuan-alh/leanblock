# Bài 6 — Kỳ vọng, phương sai và các số đặc trưng

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương II §3**, tr. 48–56.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> 📌 **Cần đọc trước:** [Bài 5 — Biến ngẫu nhiên và luật phân phối](bai_05_bien_ngau_nhien_va_luat_phan_phoi.md)

Bài 5 kết thúc bằng một lời thú nhận của giáo trình: tìm được $F(x)$ là *"rất khó, nếu không nói là
hầu như không thể"*. Bài này đưa ra lối thoát — mở đầu §3 (tr. 48):

> "Dẫu biết rằng hàm phân phối xác suất cho ta thông tin **đầy đủ nhất** về biến ngẫu nhiên,
> nhưng trong thực tế ta **không thể xác định được nó**; từ đó dẫn đến việc tìm một vài đặc trưng
> quan trọng, thông thường là đặc trưng về **vị trí** và về **độ phân tán**."

Đó là toàn bộ tinh thần: **đánh đổi thông tin đầy đủ lấy vài con số dùng được**.

| Nhóm          | Câu hỏi trả lời        | Các số đặc trưng                        |
| ------------- | ---------------------- | --------------------------------------- |
| **Vị trí**    | "trung tâm ở đâu?"     | kỳ vọng $EX$, mốt, trung vị             |
| **Phân tán**  | "toả rộng bao nhiêu?"  | phương sai $VX$, độ lệch chuẩn $\sigma$ |
| **Hình dạng** | "méo và nhọn thế nào?" | hệ số bất đối xứng, hệ số nhọn          |

## Mục lục

1. [Kỳ vọng](#1-kỳ-vọng)
2. [Năm tính chất của kỳ vọng](#2-năm-tính-chất-của-kỳ-vọng)
3. [Phương sai](#3-phương-sai)
4. [Độ lệch chuẩn và tính chất của phương sai](#4-độ-lệch-chuẩn-và-tính-chất-của-phương-sai)
5. [Mốt, trung vị và phân vị](#5-mốt-trung-vị-và-phân-vị)
6. [Mômen và hình dạng phân phối](#6-mômen-và-hình-dạng-phân-phối)
7. [📚 Chọn số đặc trưng nào](#7--chọn-số-đặc-trưng-nào)
8. [Code minh hoạ](#8-code-minh-hoạ)
9. [Tự thử](#9-tự-thử)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Kỳ vọng

**Định nghĩa 1 (tr. 48–49).** Kỳ vọng của biến ngẫu nhiên $X$, ký hiệu $EX$:

$$
\text{rời rạc: } \ EX = \sum_{\forall i} x_i p_i \tag{3.1a}
$$

$$
\text{liên tục: } \ EX = \int_{-\infty}^{+\infty} x f(x)\,dx \tag{3.1b}
$$

Đây là **mẫu chung của mọi công thức từ đây tới hết môn học**: rời rạc thì $\sum$ với $p_i$,
liên tục thì $\int$ với $f(x)dx$. Nhớ một cái là nhớ cả hai.

**Ý nghĩa (tr. 49):** kỳ vọng là **tổng có trọng số** của tất cả giá trị của $X$, hay **trị trung bình**
của biến ngẫu nhiên. Giáo trình yêu cầu phân biệt nó với *trung bình cộng của các giá trị* — vì
kỳ vọng có trọng số, còn trung bình cộng thì không.

> "Trong thực tế, nếu quan sát các giá trị của $X$ nhiều lần và lấy trung bình cộng, thì khi số quan
> sát càng lớn số trung bình đó càng **gần tới kỳ vọng** $EX$." (tr. 49)

Đây chính là **luật số lớn**, sẽ được chứng minh ở bài 9. Nó là cầu nối giữa kỳ vọng (lý thuyết)
và trung bình mẫu (thực nghiệm) — nền của cả phần thống kê.

### Thí dụ 3.1 (tr. 49)

> $X$ = số chấm khi gieo xúc sắc. Theo (3.1a):

$$EX = \frac16(1 + 2 + 3 + 4 + 5 + 6) = 3{,}5$$

Giáo trình rút ra hai nhận xét:

1. Khi xác suất **phân phối đều**, kỳ vọng chính là trung bình cộng của các giá trị.
2. $EX = 3{,}5$ nghĩa là **gieo nhiều lần thì số chấm trung bình sẽ là 3,5**.

⚠️ **Kỳ vọng không nhất thiết là giá trị $X$ có thể nhận.** Xúc sắc không bao giờ ra 3,5 chấm.
Kỳ vọng là **trọng tâm** của phân phối, không phải một kết cục. Điều này gây hiểu nhầm rất nhiều
trong báo cáo kinh doanh: *"số con trung bình mỗi hộ là 2,3"* không có nghĩa là có hộ nào sinh
2,3 đứa con.

### Thí dụ 3.2 và 3.3 (tr. 49)

**3.2** — từ bảng phân phối thí dụ 2.3 (bắn 3 phát, $p = 0{,}6$):

$$EX = 0 \cdot 0{,}064 + 1 \cdot 0{,}288 + 2 \cdot 0{,}432 + 3 \cdot 0{,}216 = \mathbf{1{,}8}$$

Kiểm nhanh bằng công thức nhị thức (bài 7): $EX = np = 3 \cdot 0{,}6 = 1{,}8$. ✓

**3.3** — biến liên tục ở thí dụ 2.6. Trước hết tìm mật độ từ $F(x) = \frac14(x-2)^2$:

$$f(x) = F'(x) = \frac12(x-2), \quad x \in [2; 4]$$

Rồi dùng (3.1b):

$$EX = \int_2^4 x \cdot \frac12(x-2)\,dx = \frac12\int_2^4 (x^2 - 2x)\,dx
= \frac12\left[\frac{x^3}{3} - x^2\right]_2^4 = \frac12 \cdot \frac{20}{3} = \mathbf{\frac{10}{3}}$$

### Thí dụ 3.4 (tr. 50) — vì sao nhà cái luôn thắng

> Một người mua vé số lô tô 2 số giá **10.000 đồng**. Anh ta thắng **700.000 đồng** (gấp 70 lần)
> nếu số mua trùng 2 số cuối của giải độc đắc, không được gì nếu trượt. Tìm số tiền thắng trung bình.

*Giải.* $X$ = số tiền thắng, nhận giá trị 0 (xác suất 99%) và 700.000 (xác suất 1%):

$$EX = 0 \cdot 99\% + 700\,000 \cdot 1\% = \mathbf{7\,000 \text{ đồng}}$$

Giáo trình kết luận sắc bén (tr. 50):

> "Mặc dù $EX > 0$, nhưng chớ quên rằng anh ta đã bỏ ra 10.000 đồng để mua xổ số. Như vậy trong thực
> tế mỗi lần chơi anh ta **mất trung bình 3.000 đồng**."

**Đây là thí dụ quan trọng nhất của mục này.** Nó dạy hai điều:

1. **Phải so kỳ vọng với chi phí bỏ ra**, không nhìn kỳ vọng đơn độc. Đại lượng cần tính là
   **kỳ vọng lợi nhuận** $= EX - \text{chi phí} = 7\,000 - 10\,000 = -3\,000$.
2. Tỷ lệ hoàn trả cho người chơi là $7\,000/10\,000 = 70\%$. Nhà cái giữ lại 30% — và vì luật số lớn,
   với hàng triệu lượt chơi, 30% đó là **chắc chắn**, không phải may rủi.

### 💼 Góc QTKD

Thí dụ 3.4 chính là khuôn mẫu của **mọi quyết định đầu tư dưới bất định**. Ba dự án cùng vốn 1 tỷ:

| Dự án | Kịch bản   | Xác suất | Lợi nhuận | $E(\text{lợi nhuận})$ |
| ----- | ---------- | -------- | --------- | --------------------- |
| A     | thành công | 0,9      | +200 tr   | \multirow             |
|       | thất bại   | 0,1      | −500 tr   | **+130 tr**           |
| B     | thành công | 0,3      | +900 tr   |                       |
|       | thất bại   | 0,7      | −200 tr   | **+130 tr**           |
| C     | chắc chắn  | 1,0      | +130 tr   | **+130 tr**           |

Ba dự án **cùng kỳ vọng 130 triệu**. Chọn cái nào?

Kỳ vọng **không đủ để quyết định** — cần thêm thước đo rủi ro, tức là **phương sai** ở mục 3.
Đó chính là lý do §3 có hai phần chứ không phải một.

Và với những quyết định **chỉ làm một lần** (mua nhà, đổi nghề, đầu tư toàn bộ vốn), kỳ vọng còn
kém tin cậy hơn nữa: luật số lớn chỉ đúng khi bạn lặp lại nhiều lần. Nhà cái xổ số thắng chắc vì
họ chơi hàng triệu ván; người mua vé chỉ chơi vài ván.

---

## 2. Năm tính chất của kỳ vọng

Giáo trình liệt kê (tr. 50):

$$
\begin{aligned}
&\text{(i)} && E(c) = c && (c \text{ là hằng số}) \\
&\text{(ii)} && E(cX) = c\,EX \\
&\text{(iii)} && E(X + Y) = EX + EY && \textbf{luôn đúng, không cần độc lập} \\
&\text{(iv)} && E(XY) = EX \cdot EY && \textbf{chỉ khi } X, Y \textbf{ độc lập} \\
&\text{(v)} && Y = \varphi(X) \Rightarrow EY = \sum_i \varphi(x_i)p_i \ \text{ hoặc } \int \varphi(x)f(x)dx
\end{aligned}
$$

⚠️ **Chỗ nhớ nhầm nhiều nhất: (iii) và (iv) có điều kiện khác nhau.**

- **Cộng thì luôn được**: $E(X+Y) = EX + EY$ đúng kể cả khi $X$, $Y$ phụ thuộc chặt chẽ.
- **Nhân thì phải độc lập**: $E(XY) = EX \cdot EY$ chỉ đúng khi độc lập.

💼 Hệ quả thực tế: **doanh thu tổng của hai chi nhánh luôn bằng tổng hai kỳ vọng**, kể cả khi hai
chi nhánh cạnh tranh khách của nhau. Nhưng kỳ vọng của **tích** (ví dụ: doanh thu = số đơn × giá trị
trung bình mỗi đơn) thì **không** bằng tích hai kỳ vọng nếu hai yếu tố tương quan — mà chúng thường
tương quan (đơn nhiều thì thường vào mùa cao điểm, giá trị mỗi đơn cũng cao hơn).

**Tính chất (v) rất tiện** — đây là cái người ta gọi là *"luật của nhà thống kê vô thức"*.
Để tính $E[\varphi(X)]$ bạn **không cần** tìm luật phân phối của $\varphi(X)$; cứ nhân $\varphi(x)$
vào rồi cộng như thường.

### Thí dụ 3.5 (tr. 50)

> Gieo đồng thời 2 con xúc sắc. Tìm tổng số chấm trung bình.

*Giải.* $X_i$ = số chấm con thứ $i$. Từ thí dụ 3.1, $EX_1 = EX_2 = 3{,}5$. Dùng tính chất (iii):

$$E(X_1 + X_2) = 3{,}5 + 3{,}5 = \mathbf{7}$$

**Chú ý cái đẹp ở đây:** không cần lập bảng phân phối của tổng (11 giá trị, xác suất khác nhau).
Tính chất (iii) cho đáp số trong một dòng. Đó là lý do các số đặc trưng có giá trị thực tiễn.

---

## 3. Phương sai

**Định nghĩa 2 (tr. 51).**

$$VX = E\left[(X - EX)^2\right] \tag{3.2}$$

**Ý nghĩa (tr. 51):** $X - EX$ là **độ lệch** của biến so với trung bình của nó; phương sai là
**trung bình của bình phương độ lệch**. Vậy phương sai đặc trưng cho **độ phân tán** quanh trị
trung bình. *"Phương sai càng lớn thì độ bất định của biến tương ứng càng lớn."*

**Vì sao bình phương?** Vì nếu lấy trung bình của $(X - EX)$ thẳng thì luôn được **0** — các độ lệch
âm và dương triệt tiêu nhau. Bình phương làm mọi độ lệch thành dương, đồng thời **phạt nặng các độ
lệch lớn** (lệch gấp đôi bị phạt gấp bốn).

Hai công thức tính theo định nghĩa:

$$
VX = \sum_{\forall i}(x_i - EX)^2 p_i \tag{3.3a} \qquad
VX = \int_{-\infty}^{+\infty}(x - EX)^2 f(x)\,dx \tag{3.3b}
$$

Nhưng giáo trình chỉ ra ngay (tr. 51): *"việc tính theo (3.3) khá phức tạp"*. Biến đổi (3.2) bằng
tính chất của kỳ vọng cho ra dạng tương đương **dễ tính hơn nhiều**:

$$\boxed{VX = E(X^2) - (EX)^2} \tag{3.4}$$

$$
VX = \sum_i x_i^2 p_i - \left(\sum_i x_i p_i\right)^2 \tag{3.4a} \qquad
VX = \int x^2 f(x)dx - \left(\int x f(x)dx\right)^2 \tag{3.4b}
$$

**Chứng minh** (giáo trình không viết ra, nhưng nên biết):

$$
\begin{aligned}
VX &= E[(X - EX)^2] = E[X^2 - 2X\,EX + (EX)^2] \\
&= E(X^2) - 2\,EX \cdot EX + (EX)^2 && \text{(dùng (iii), (ii), (i))} \\
&= E(X^2) - (EX)^2 \qquad \blacksquare
\end{aligned}
$$

**Cách nhớ:** *"trung bình của bình phương trừ bình phương của trung bình"*.

⚠️ Thứ tự không được đổi: $E(X^2) \ne (EX)^2$, và luôn có $E(X^2) \ge (EX)^2$ (vì $VX \ge 0$).

### Thí dụ 3.6 (tr. 51)

> Tính $VX$ cho bảng phân phối thí dụ 2.3 (đã biết $EX = 1{,}8$).

Giáo trình nói thẳng: *"việc tính theo (3.3a) khá phức tạp. Ta sẽ dùng công thức (3.4a)"*:

$$
\begin{aligned}
E(X^2) &= 0^2 \cdot 0{,}064 + 1^2 \cdot 0{,}288 + 2^2 \cdot 0{,}432 + 3^2 \cdot 0{,}216 = 3{,}96 \\
VX &= 3{,}96 - 1{,}8^2 = 3{,}96 - 3{,}24 = \mathbf{0{,}72}
\end{aligned}
$$

Kiểm bằng công thức nhị thức (bài 7): $VX = npq = 3 \cdot 0{,}6 \cdot 0{,}4 = 0{,}72$. ✓

### Thí dụ 3.7 (tr. 52) — phân phối mũ

> $f(x) = \lambda e^{-\lambda x}$ với $x \ge 0$, $\lambda > 0$ (từ thí dụ 2.8). Tính $VX$.

$$EX = \int_0^{+\infty} x\lambda e^{-\lambda x}dx = \frac{1}{\lambda},
\qquad E(X^2) = \int_0^{+\infty} x^2\lambda e^{-\lambda x}dx = \frac{2}{\lambda^2}$$

$$VX = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \mathbf{\frac{1}{\lambda^2}}$$

**Đặc điểm đáng nhớ của phân phối mũ:** $EX = \sigma = 1/\lambda$ — **kỳ vọng bằng đúng độ lệch chuẩn**.
Nghĩa là thời gian chờ trung bình và độ dao động của nó bằng nhau; phân phối mũ **rất phân tán**.

💼 Thực tế: nếu thời gian chờ khách hàng trung bình 10 phút và tuân theo phân phối mũ, thì độ lệch
chuẩn cũng 10 phút — sẽ có những khoảng chờ 30 phút không có ai. Đó là lý do quán cà phê không thể
lên lịch nhân sự dựa trên trung bình.

---

## 4. Độ lệch chuẩn và tính chất của phương sai

Giáo trình nêu vấn đề (tr. 53): về mặt vật lý, $VX$ **không cùng thứ nguyên** (đơn vị đo) với $X$.
Nếu $X$ đo bằng triệu đồng thì $VX$ có đơn vị là "triệu đồng bình phương" — vô nghĩa.

**Định nghĩa 3 (tr. 53).** Độ lệch chuẩn:

$$\sigma(X) = \sqrt{VX} \tag{3.5}$$

> "Độ lệch chuẩn được dùng **thường xuyên hơn** phương sai do có **cùng đơn vị đo** với chính biến $X$."

Vì thế phương sai còn được ký hiệu $\sigma^2(X)$ hay $\sigma_X^2$.

**Ba tính chất (tr. 53):**

$$
\begin{aligned}
&\text{(i)} && V(c) = 0 \\
&\text{(ii)} && V(cX) = c^2\,VX, \qquad \sigma(cX) = |c|\,\sigma(X) \\
&\text{(iii)} && X, Y \text{ độc lập} \Rightarrow V(X+Y) = VX + VY
\end{aligned}
$$

⚠️ **So sánh với kỳ vọng — ba khác biệt phải nhớ:**

|               | Kỳ vọng           | Phương sai                          |
| ------------- | ----------------- | ----------------------------------- |
| Nhân hằng số  | $E(cX) = c\,EX$   | $V(cX) = \mathbf{c^2}\,VX$          |
| Cộng hằng số  | $E(X+c) = EX + c$ | $V(X+c) = \mathbf{VX}$ (không đổi!) |
| Cộng hai biến | luôn cộng được    | **chỉ khi độc lập**                 |

**Cộng hằng số không đổi phương sai** — hiển nhiên khi hiểu ý nghĩa: dịch cả phân phối sang phải
5 đơn vị thì độ toả rộng không đổi. Còn nhân đôi mọi giá trị thì độ toả rộng nhân đôi, nên phương sai
(là bình phương) nhân bốn.

Giáo trình lưu ý (tr. 53): *"điều kiện độc lập là khá chặt, sau này ở chương III ta thấy có thể
giảm nhẹ"* — bài 8 sẽ cho biết chỉ cần **không tương quan** là đủ.

### Hai hệ quả — hệ quả thứ hai là nền của cả thống kê

**Hệ quả 1:** $V(X + c) = VX$.

**Hệ quả 2 (tr. 53).** Phương sai của trung bình cộng $n$ biến ngẫu nhiên **độc lập cùng phân phối**
sẽ **bé hơn $n$ lần** phương sai của các biến thành phần. Nếu $VX_i = \sigma^2$ với mọi $i$:

$$V(\overline{X}) = V\!\left(\frac{X_1 + \cdots + X_n}{n}\right) = \frac{\sigma^2}{n},
\qquad \sigma(\overline{X}) = \frac{\sigma}{\sqrt{n}}$$

*Chứng minh:* dùng (ii) với $c = 1/n$ và (iii): $V(\overline{X}) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$. ∎

Giáo trình giải thích ứng dụng (tr. 53): *"Đây chính là lý do khi đo đạc các đại lượng vật lý người ta
thường **đo nhiều lần rồi lấy trung bình cộng** các kết quả."*

### ⚠️ Luật căn bậc hai — con số quan trọng nhất bài này

Chú ý: phương sai giảm theo $n$, nhưng **độ lệch chuẩn giảm theo $\sqrt{n}$**.

| Cỡ mẫu $n$ | $\sigma(\overline{X})$ so với $\sigma$ |
| ---------: | :------------------------------------- |
|          1 | $\sigma$                               |
|          4 | $\sigma/2$                             |
|         25 | $\sigma/5$                             |
|        100 | $\sigma/10$                            |
|        400 | $\sigma/20$                            |

> **Muốn giảm sai số 2 lần, phải tăng cỡ mẫu 4 lần. Muốn giảm 10 lần, phải tăng 100 lần.**

💼 Đây là **định luật kinh tế của mọi nghiên cứu thị trường**. Khảo sát 400 người chính xác gấp đôi
khảo sát 100 người — nhưng tốn gấp bốn tiền. Muốn chính xác gấp đôi nữa (1.600 người) thì tốn
gấp 16 lần so với ban đầu.

Vì thế các công ty nghiên cứu thị trường hầu như luôn dừng ở cỡ mẫu **1.000–1.200** — đó là điểm
mà chi phí bắt đầu tăng nhanh hơn nhiều so với độ chính xác thu được. Bài 11 sẽ tính chính xác
cỡ mẫu cần cho một sai số cho trước.

---

## 5. Mốt, trung vị và phân vị

Kỳ vọng không phải thước đo vị trí duy nhất. Giáo trình bổ sung hai cái nữa (tr. 54).

### Mốt

**Định nghĩa.** **Mốt** là giá trị của $X$ có **khả năng xuất hiện lớn nhất** trong một lân cận nào đó.

- Biến **rời rạc**: giá trị ứng với **xác suất lớn nhất**.
- Biến **liên tục**: giá trị làm **hàm mật độ đạt max**.

⚠️ Giáo trình lưu ý: *"mốt có thể chỉ là **cực đại địa phương** và một biến ngẫu nhiên có thể có
**một mốt hoặc nhiều mốt**."*

### Trung vị

**Định nghĩa.** **Trung vị** $\text{med}X$ chia phân phối thành hai phần có xác suất bằng nhau:

$$P(X < \text{med}X) = P(X > \text{med}X) = \frac12$$

Cách tìm: **giải phương trình $F(x) = \frac12$**.

> "Trong nhiều trường hợp ứng dụng, trung vị là đặc trưng vị trí **rất tốt, nhiều khi tốt hơn cả
> kỳ vọng**, nhất là khi trong số liệu có những **sai sót thái quá**." (tr. 54)

### Phân vị

Trung vị còn có tên là **phân vị 50%**. Tổng quát (tr. 55): **phân vị** là một điểm sao cho xác suất
để $X$ nhận giá trị bé hơn nó bằng số phần trăm cho trước.

$$x \text{ là phân vị } \alpha\% \iff F(x) = \frac{\alpha}{100}$$

Ví dụ giáo trình: *"2 là phân vị 72% của $X$ nếu $F(2) = 0{,}72$"*. Thường xét phân vị
**25%, 50% (trung vị), 75%, 95%**.

### Thí dụ 3.8 và 3.9 (tr. 54–55) — ba số, ba giá trị khác nhau

> Phân phối Weibull: $f(x) = \dfrac{x}{2}e^{-x^2/4}$ với $x > 0$. Tìm mốt và trung vị.

**Mốt** — giải $f'(x) = 0$. Giáo trình rút gọn về $1 - \dfrac{x^2}{2} = 0$; do $x > 0$:

$$\text{mốt} = \sqrt{2} \approx \mathbf{1{,}414}$$

**Trung vị** — giải $F(\text{med}X) = 0{,}5$, tức $1 - e^{-(\text{med}X)^2/4} = 0{,}5$:

$$\text{med}X = 2\sqrt{\ln 2} \approx \mathbf{1{,}665}$$

**Kỳ vọng** — tính thêm được $EX = \sqrt{\pi} \approx \mathbf{1{,}772}$.

Giáo trình tổng kết (tr. 55): *"Nói chung, ba số đặc trưng kỳ vọng, mốt và trung vị **không trùng
nhau**... Tuy nhiên trong trường hợp phân phối **đối xứng và chỉ có một mốt** thì cả ba đặc trưng
đó **trùng nhau**."*

$$\text{mốt } (1{,}414) \ < \ \text{med}X \ (1{,}665) \ < \ EX \ (1{,}772)$$

Thứ tự này cho biết phân phối **lệch phải** (đuôi kéo dài về bên phải):

```
   f(x)
     │      ╭╮
     │     ╱  ╲
     │    ╱    ╲___
     │   ╱         ‾‾‾───____          đuôi dài bên phải
     └──┴──┴──┴────────────────► x     kéo EX ra xa nhất
        │  │  │
      mốt med EX
```

**Quy tắc nhớ:** kỳ vọng bị đuôi kéo mạnh nhất, mốt không bị kéo, trung vị nằm giữa.

- lệch **phải**: mốt < med < $EX$
- đối xứng: mốt = med = $EX$
- lệch **trái**: $EX$ < med < mốt

### 💼 Góc QTKD — vì sao "lương trung bình" luôn gây tranh cãi

Lương tháng của 10 nhân viên (triệu đồng): 12, 13, 14, 14, 15, 15, 16, 18, 22, **121** (giám đốc).

| Thước đo   |  Giá trị |    Bỏ người lương 121 ra |
| ---------- | -------: | -----------------------: |
| Trung bình | **26,0** |          15,4 (đổi mạnh) |
| Trung vị   | **15,0** | 14,5 (gần như không đổi) |

**9 trên 10 nhân viên có lương thấp hơn "mức trung bình" 26 triệu.** Con số trung bình đúng về mặt
số học nhưng mô tả sai thực tế.

Đây là lý do:

- **Thống kê thu nhập quốc gia** luôn công bố **thu nhập trung vị**, không phải trung bình.
- **Giá nhà** báo cáo theo giá trung vị.
- **Thời gian phản hồi hệ thống** báo cáo theo phân vị 95% và 99%, không phải trung bình —
  vì trung bình che giấu 5% khách hàng có trải nghiệm tệ.

⚠️ **Quy tắc thực hành:** dữ liệu kinh doanh (thu nhập, giá trị đơn hàng, thời gian chờ, doanh thu
khách hàng) hầu như **luôn lệch phải** — có ít giá trị rất lớn kéo trung bình lên. **Mặc định dùng
trung vị**, chỉ dùng trung bình khi đã kiểm tra phân phối gần đối xứng.

Nhưng có một ngoại lệ quan trọng: **khi cộng dồn thì phải dùng kỳ vọng**. Tổng doanh thu tháng =
$30 \times$ doanh thu trung bình ngày (đúng, do tính chất (iii)); không phải $30 \times$ trung vị.
Trung vị không cộng được.

---

## 6. Mômen và hình dạng phân phối

Giáo trình khép §3 bằng khái niệm tổng quát hoá cả kỳ vọng lẫn phương sai (tr. 55).

**Định nghĩa 4.** **Mômen cấp $k$ đối với $a$** của biến ngẫu nhiên $X$:

$$\nu_k(a) = E\left[(X - a)^k\right] \tag{3.6}$$

Hai trường hợp riêng có tên gọi:

| $a$      | Ký hiệu                 | Tên                         | Quan hệ      |
| -------- | ----------------------- | --------------------------- | ------------ |
| $a = 0$  | $\nu_k = E(X^k)$        | **mômen gốc** cấp $k$       | $EX = \nu_1$ |
| $a = EX$ | $\mu_k = E[(X - EX)^k]$ | **mômen trung tâm** cấp $k$ | $VX = \mu_2$ |

Liên hệ giữa hai loại (tr. 56):

$$
\begin{aligned}
\mu_2 &= \nu_2 - \nu_1^2 = \sigma^2 \\
\mu_3 &= \nu_3 - 3\nu_2\nu_1 + 2\nu_1^3 \\
\mu_4 &= \nu_4 - 4\nu_3\nu_1 + 6\nu_2\nu_1^2 - 3\nu_1^4
\end{aligned}
$$

Dòng đầu chính là công thức (3.4) đã biết.

### Hai hệ số hình dạng (tr. 56)

**Hệ số bất đối xứng** (skewness):

$$\beta_1 = \frac{\mu_3}{\sigma^3}$$

- $\beta_1 = 0$ → đường cong mật độ **đối xứng**
- $\beta_1 > 0$ → **lệch phải** (đuôi dài bên phải)
- $\beta_1 < 0$ → **lệch trái**

**Hệ số nhọn** (kurtosis):

$$\beta_2 = \frac{\mu_4}{\sigma^4}$$

*"Nếu tỷ số này càng lớn đường cong có đỉnh càng nhọn hơn."* Giáo trình cho một mốc chuẩn rất hữu ích:

> **Đường cong mật độ của phân phối chuẩn có $\beta_2 = 3$.**

Con số 3 là **thước đo tham chiếu**: $\beta_2 > 3$ nghĩa là phân phối nhọn hơn chuẩn và **đuôi nặng
hơn** (nhiều giá trị cực đoan hơn); $\beta_2 < 3$ nghĩa là bẹt hơn.

### 💼 Góc QTKD — đuôi nặng là chuyện sống còn

Trong tài chính, $\beta_2 > 3$ (**đuôi nặng**, fat tails) là đặc điểm cố hữu của lợi suất tài sản:
các cú sốc lớn xảy ra **thường xuyên hơn nhiều** so với phân phối chuẩn dự đoán.

Nếu mô hình rủi ro của bạn giả định phân phối chuẩn ($\beta_2 = 3$) trong khi thực tế $\beta_2 = 8$,
bạn sẽ **đánh giá thấp nghiêm trọng** xác suất của một ngày sụp đổ. Đây là một trong những nguyên nhân
kỹ thuật của khủng hoảng tài chính 2008 — cùng với sai lầm về độc lập đã nêu ở bài 3 mục 2.

**Cách kiểm nhanh trên dữ liệu thật:** tính $\beta_1$ và $\beta_2$ trước khi áp dụng bất kỳ mô hình
nào giả định phân phối chuẩn. Excel có sẵn `SKEW()` và `KURT()`.

⚠️ Lưu ý: Excel `KURT()` trả về **kurtosis dư** $= \beta_2 - 3$, nên phân phối chuẩn cho `KURT() = 0`
chứ không phải 3. Lại một khác biệt quy ước nữa, giống như $F(x)$ ở bài 5.

---

## 7. 📚 Chọn số đặc trưng nào

Giáo trình trình bày sáu số đặc trưng ở ba mục riêng mà không so sánh. Bảng này là phần bổ sung.

| Số đặc trưng               | Đo cái gì     | Ưu                                          | Nhược                              |
| -------------------------- | ------------- | ------------------------------------------- | ---------------------------------- |
| **Kỳ vọng** $EX$           | trọng tâm     | cộng được, tính được, luật số lớn bảo chứng | **bị giá trị thái quá kéo méo**    |
| **Trung vị**               | điểm giữa     | bền vững với giá trị thái quá               | **không cộng được**                |
| **Mốt**                    | đỉnh cao nhất | là giá trị *thật sự* hay gặp                | có thể có nhiều mốt, không ổn định |
| **Phương sai** $VX$        | độ phân tán   | cộng được (khi độc lập), tính dễ            | **sai đơn vị đo**                  |
| **Độ lệch chuẩn** $\sigma$ | độ phân tán   | **cùng đơn vị với $X$**                     | không cộng được trực tiếp          |
| **$\beta_1$, $\beta_2$**   | hình dạng     | phát hiện lệch và đuôi nặng                 | cần cỡ mẫu lớn mới ổn định         |

**Quy trình mô tả một biến ngẫu nhiên trong 4 bước:**

```
   1. VỊ TRÍ ở đâu?
      dữ liệu đối xứng?  ──► CÓ  ──► dùng EX  (và EX ≈ med ≈ mốt)
                         └─► KHÔNG ──► dùng med X, báo cáo thêm EX

   2. PHÂN TÁN bao nhiêu?
      luôn báo cáo σ (cùng đơn vị), không báo cáo VX trần

   3. HÌNH DẠNG thế nào?
      β₁ ≠ 0  ──► lệch, cẩn thận khi dùng EX
      β₂ > 3  ──► đuôi nặng, mô hình chuẩn sẽ đánh giá thấp rủi ro

   4. SO VỚI CHI PHÍ
      quyết định đầu tư: nhìn E(lợi nhuận) = EX − chi phí, KHÔNG nhìn EX trần
      quyết định làm MỘT LẦN: kỳ vọng kém tin cậy, phải xét σ và tình huống xấu nhất
```

**Một cặp số luôn đi cùng nhau: $(EX, \sigma)$.** Báo cáo kỳ vọng mà không kèm độ lệch chuẩn
là báo cáo thiếu — đúng như ví dụ ba dự án ở mục 1 cho thấy.

---

## 8. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-06-ky-vong.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.

Ba hàm `E`, `V`, `V_dinhnghia` ở đầu file làm được **toàn bộ** phần rời rạc của bài. Chú ý hàm `E`
nhận thêm tham số `g` — đó chính là tính chất (v), và nhờ nó mà `V` chỉ cần một dòng.

```python
"""Bài 6 — Kỳ vọng, phương sai và các số đặc trưng."""

import math
from fractions import Fraction

# ─────────────────────────────────────────────────────────────
# Bộ công cụ cho biến RỜI RẠC — dùng lại cho cả bài
# ─────────────────────────────────────────────────────────────
def E(dist, g=lambda x: x):
    """Ky vong cua g(X):  E[g(X)] = sum g(x)*p(x)   — cong thuc (3.1a) va (v)."""
    return sum(g(x) * px for x, px in dist.items())


def V(dist):
    """Phuong sai theo (3.4a):  VX = E(X^2) - (EX)^2."""
    return E(dist, lambda x: x * x) - E(dist) ** 2


def V_dinhnghia(dist):
    """Phuong sai theo dinh nghia (3.3a):  VX = E[(X - EX)^2]."""
    m = E(dist)
    return E(dist, lambda x: (x - m) ** 2)


# ─────────────────────────────────────────────────────────────
# 1. KỲ VỌNG — Thí dụ 3.1 (tr. 49), xúc sắc
# ─────────────────────────────────────────────────────────────
dice = {k: Fraction(1, 6) for k in range(1, 7)}
print("THI DU 3.1 — xuc sac")
print("  EX =", E(dice), "=", float(E(dice)), "  (sach: 3,5)")
print("  ⚠ EX = 3,5 KHONG phai gia tri X co the nhan duoc")

# Thí dụ 3.5 (tr. 50) — tổng 2 xúc sắc, dùng tính chất (iii)
print("THI DU 3.5 — tong so cham 2 xuc sac: E(X1+X2) =",
      E(dice) + E(dice), "  (sach: 7)")

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 3.2 và 3.6 (tr. 49, 51) — bắn 3 phát, p = 0,6
# ─────────────────────────────────────────────────────────────
hits = {0: Fraction(64, 1000), 1: Fraction(288, 1000),
        2: Fraction(432, 1000), 3: Fraction(216, 1000)}
assert sum(hits.values()) == 1
print()
print("THI DU 3.2 / 3.6 — so dan trung khi ban 3 phat, p = 0,6")
print("  EX =", E(hits), "=", float(E(hits)), "  (sach: 1,8)")
print("  E(X^2) =", E(hits, lambda x: x * x), "=", float(E(hits, lambda x: x * x)))
print("  VX theo (3.4a) = E(X^2) - (EX)^2 =", V(hits), "=", float(V(hits)),
      "  (sach: 0,72)")
print("  VX theo dinh nghia (3.3a)        =", V_dinhnghia(hits),
      "  -> hai cach bang nhau:", V(hits) == V_dinhnghia(hits))
print(f"  Do lech chuan sigma = can(VX) = {math.sqrt(float(V(hits))):.4f}")
# Doi chieu cong thuc nhi thuc: EX = np, VX = npq
print("  Kiem cong thuc nhi thuc: np =", 3 * Fraction(6, 10),
      "| npq =", 3 * Fraction(6, 10) * Fraction(4, 10))

# ─────────────────────────────────────────────────────────────
# 3. Thí dụ 3.4 (tr. 50) — xổ số lô tô, vì sao nhà cái luôn thắng
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 3.4 — mua 10.000d ve lo to 2 so, trung thi duoc 700.000d")
lotto = {0: Fraction(99, 100), 700_000: Fraction(1, 100)}
ex = E(lotto)
print("  EX (tien thang trung binh) =", ex, "dong   (sach: 7000)")
print("  Nhung da bo ra 10.000d  ->  moi lan choi MAT trung binh",
      10_000 - ex, "dong")
print(f"  Ty le hoan tra cho nguoi choi = {float(ex) / 10_000 * 100:.0f}%")

# ─────────────────────────────────────────────────────────────
# 4. TÍNH CHẤT KỲ VỌNG VÀ PHƯƠNG SAI — kiểm bằng số
# ─────────────────────────────────────────────────────────────
print()
print("KIEM CAC TINH CHAT (tr. 50 va tr. 53)")
c = 5
shifted = {x + c: px for x, px in hits.items()}
scaled = {c * x: px for x, px in hits.items()}
print(f"  (ii) E(cX) = cEX      : {E(scaled)} = {c}*{E(hits)}  ->",
      E(scaled) == c * E(hits))
print(f"  (iii) E(X+c) = EX + c : {E(shifted)} = {E(hits)}+{c}  ->",
      E(shifted) == E(hits) + c)
print(f"  (ii') V(cX) = c^2 VX  : {V(scaled)} = {c}^2*{V(hits)}  ->",
      V(scaled) == c * c * V(hits))
print(f"  V(X+c) = VX           : {V(shifted)} = {V(hits)}  ->",
      V(shifted) == V(hits))
print("  ⚠ Cong hang so lam DOI ky vong nhung KHONG doi phuong sai")

# Hệ quả: phương sai của trung bình cộng n biến độc lập = sigma^2 / n
print()
print("HE QUA QUAN TRONG — V(trung binh cong n bien doc lap) = VX / n")
vx = V(hits)
print(f"{'n':>6}{'V(X ngang)':>16}{'sigma(X ngang)':>18}")
for n in [1, 4, 25, 100, 400]:
    v_mean = vx / n
    print(f"{n:>6}{float(v_mean):>16.5f}{math.sqrt(float(v_mean)):>18.5f}")
print("  Muon giam sai so 2 lan -> phai tang co mau 4 lan (luat can bac hai)")

# ─────────────────────────────────────────────────────────────
# 5. MỐT, TRUNG VỊ — Thí dụ 3.8, 3.9 (tr. 54–55), phân phối Weibull
#    f(x) = (x/2) e^(-x^2/4),  x > 0
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 3.8 / 3.9 — phan phoi Weibull f(x) = (x/2)e^(-x^2/4)")
mode = math.sqrt(2)                        # nghiem cua f'(x) = 0
median = 2 * math.sqrt(math.log(2))        # 1 - e^(-med^2/4) = 0,5
mean = math.sqrt(math.pi)                  # tinh bang tich phan


def integrate(f, a, b, n=400_000):
    h = (b - a) / n
    return h * (f(a) / 2 + f(b) / 2 + sum(f(a + i * h) for i in range(1, n)))


f_wb = lambda x: (x / 2) * math.exp(-x * x / 4) if x > 0 else 0.0
print(f"  mot     = can(2)      = {mode:.4f}   (sach: 1,414)")
print(f"  med X   = 2can(ln2)   = {median:.4f}   (sach: 1,665)")
print(f"  EX      = can(pi)     = {mean:.4f}   (sach: 1,772)")
print(f"  Kiem EX bang tich phan so         : {integrate(lambda x: x * f_wb(x), 0, 30):.4f}")
print(f"  Kiem tinh chat (ii) tong = 1      : {integrate(f_wb, 0, 30):.4f}")
print(f"  Kiem med: F(med) = {1 - math.exp(-median**2 / 4):.4f}  (phai bang 0,5)")
print("  ⚠ mot < med < EX  ->  phan phoi LECH PHAI (duoi keo ve ben phai)")

# ─────────────────────────────────────────────────────────────
# 6. 💼 GÓC QTKD — vì sao lương trung bình luôn cao hơn lương "điển hình"
# ─────────────────────────────────────────────────────────────
print()
print("💼 GOC QTKD — luong thang cua 10 nhan vien (trieu dong)")
salary = [12, 13, 14, 14, 15, 15, 16, 18, 22, 121]   # 1 nguoi la giam doc
n = len(salary)
mean_s = sum(salary) / n
srt = sorted(salary)
med_s = (srt[n // 2 - 1] + srt[n // 2]) / 2
print("  Du lieu:", salary)
print(f"  Trung binh (ky vong mau) = {mean_s:.1f} trieu")
print(f"  Trung vi                 = {med_s:.1f} trieu")
print(f"  -> 9/10 nhan vien co luong THAP HON muc trung binh {mean_s:.1f}")
print("  Bo nguoi luong 121 ra:")
cut = salary[:-1]
print(f"    trung binh -> {sum(cut) / len(cut):.1f}   (doi manh)")
srt2 = sorted(cut)
print(f"    trung vi   -> {(srt2[len(cut) // 2 - 1] + srt2[len(cut) // 2]) / 2:.1f}"
      "   (gan nhu khong doi)")
print("  => TRUNG VI ben vung voi gia tri thai qua, TRUNG BINH thi khong")
```

Kết quả chạy thật:

```
THI DU 3.1 — xuc sac
  EX = 7/2 = 3.5   (sach: 3,5)
  ⚠ EX = 3,5 KHONG phai gia tri X co the nhan duoc
THI DU 3.5 — tong so cham 2 xuc sac: E(X1+X2) = 7   (sach: 7)

THI DU 3.2 / 3.6 — so dan trung khi ban 3 phat, p = 0,6
  EX = 9/5 = 1.8   (sach: 1,8)
  E(X^2) = 99/25 = 3.96
  VX theo (3.4a) = E(X^2) - (EX)^2 = 18/25 = 0.72   (sach: 0,72)
  VX theo dinh nghia (3.3a)        = 18/25   -> hai cach bang nhau: True
  Do lech chuan sigma = can(VX) = 0.8485
  Kiem cong thuc nhi thuc: np = 9/5 | npq = 18/25

THI DU 3.4 — mua 10.000d ve lo to 2 so, trung thi duoc 700.000d
  EX (tien thang trung binh) = 7000 dong   (sach: 7000)
  Nhung da bo ra 10.000d  ->  moi lan choi MAT trung binh 3000 dong
  Ty le hoan tra cho nguoi choi = 70%

KIEM CAC TINH CHAT (tr. 50 va tr. 53)
  (ii) E(cX) = cEX      : 9 = 5*9/5  -> True
  (iii) E(X+c) = EX + c : 34/5 = 9/5+5  -> True
  (ii') V(cX) = c^2 VX  : 18 = 5^2*18/25  -> True
  V(X+c) = VX           : 18/25 = 18/25  -> True
  ⚠ Cong hang so lam DOI ky vong nhung KHONG doi phuong sai

HE QUA QUAN TRONG — V(trung binh cong n bien doc lap) = VX / n
     n      V(X ngang)    sigma(X ngang)
     1         0.72000           0.84853
     4         0.18000           0.42426
    25         0.02880           0.16971
   100         0.00720           0.08485
   400         0.00180           0.04243
  Muon giam sai so 2 lan -> phai tang co mau 4 lan (luat can bac hai)

THI DU 3.8 / 3.9 — phan phoi Weibull f(x) = (x/2)e^(-x^2/4)
  mot     = can(2)      = 1.4142   (sach: 1,414)
  med X   = 2can(ln2)   = 1.6651   (sach: 1,665)
  EX      = can(pi)     = 1.7725   (sach: 1,772)
  Kiem EX bang tich phan so         : 1.7725
  Kiem tinh chat (ii) tong = 1      : 1.0000
  Kiem med: F(med) = 0.5000  (phai bang 0,5)
  ⚠ mot < med < EX  ->  phan phoi LECH PHAI (duoi keo ve ben phai)

💼 GOC QTKD — luong thang cua 10 nhan vien (trieu dong)
  Du lieu: [12, 13, 14, 14, 15, 15, 16, 18, 22, 121]
  Trung binh (ky vong mau) = 26.0 trieu
  Trung vi                 = 15.0 trieu
  -> 9/10 nhan vien co luong THAP HON muc trung binh 26.0
  Bo nguoi luong 121 ra:
    trung binh -> 15.4   (doi manh)
    trung vi   -> 14.5   (gan nhu khong doi)
  => TRUNG VI ben vung voi gia tri thai qua, TRUNG BINH thi khong
```

Ba điểm đáng để ý:

1. **`V(hits) == V_dinhnghia(hits)` cho `True`** — công thức (3.4) và định nghĩa (3.3) cho cùng
   kết quả, đúng như chứng minh ở mục 3. Nhưng nhìn code sẽ thấy (3.4) ngắn hơn: không cần tính $EX$
   trước rồi mới trừ từng số hạng.
2. **Bảng $\sigma(\overline{X})$**: từ $n=1$ tới $n=400$ (gấp 400 lần), $\sigma$ chỉ giảm từ 0,849
   xuống 0,042 — **giảm đúng 20 lần** $= \sqrt{400}$. Đây là luật căn bậc hai, nhìn bằng số.
3. **Phần lương**: bỏ một người ra khỏi 10 người làm trung bình rơi từ 26,0 xuống 15,4
   (mất 40%), nhưng trung vị chỉ từ 15,0 xuống 14,5 (mất 3%). Đó là ý nghĩa của chữ **"bền vững"**.

---

## 9. Tự thử

1. Ở thí dụ 3.4, đổi giải thưởng từ 700.000 lên **1.000.000** đồng. Người chơi giờ lãi hay lỗ trung
   bình? Giải thưởng phải bằng bao nhiêu để trò chơi **công bằng** ($EX$ = giá vé)?
2. Thêm vào phần "kiểm các tính chất": kiểm $E(XY) = EX \cdot EY$ khi $X$, $Y$ độc lập, dùng hàm
   `convolve` ở bài 5. Rồi thử với $Y = X$ (phụ thuộc hoàn toàn) — đẳng thức còn đúng không?
3. Tính $\sigma$ cho ba dự án A, B, C ở Góc QTKD mục 1. Dự án nào rủi ro nhất? Nếu bạn chỉ được
   chọn **một lần duy nhất**, bạn chọn dự án nào, vì sao?
4. Ở phần Weibull, tính $\beta_1 = \mu_3/\sigma^3$ bằng tích phân số. Dấu của nó có khớp với kết luận
   "lệch phải" không?
5. Thêm một nhân viên lương **200 triệu** vào danh sách lương. Trung bình và trung vị đổi bao nhiêu
   phần trăm? Vẽ lại kết luận.
6. Viết hàm tính **phân vị $\alpha$** cho một danh sách số, rồi tính phân vị 25%, 50%, 75%, 95%
   của danh sách lương. Con số nào bạn sẽ đưa vào báo cáo cho ban giám đốc, và vì sao?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt (giáo trình) | Tiếng Anh              | Ghi chú                                            |
| ----------------------- | ---------------------- | -------------------------------------------------- |
| Kỳ vọng, trị trung bình | Expected value, Mean   | $EX$, $\mu$                                        |
| Phương sai              | Variance               | $VX$, $\sigma^2$                                   |
| Độ lệch chuẩn           | Standard deviation     | $\sigma = \sqrt{VX}$                               |
| Độ lệch                 | Deviation              | $X - EX$                                           |
| Thứ nguyên              | Dimension, Unit        | lý do dùng $\sigma$ thay $VX$                      |
| Độ phân tán, độ tán xạ  | Dispersion, Spread     |                                                    |
| Mốt                     | Mode                   | giá trị hay gặp nhất                               |
| Trung vị                | Median                 | phân vị 50%                                        |
| Phân vị                 | Quantile, Percentile   | $F(x) = \alpha$                                    |
| Mômen cấp $k$           | $k$-th moment          | $\nu_k(a) = E[(X-a)^k]$                            |
| Mômen gốc               | Raw moment             | $a = 0$                                            |
| Mômen trung tâm         | Central moment         | $a = EX$                                           |
| Hệ số bất đối xứng      | Skewness               | $\beta_1 = \mu_3/\sigma^3$                         |
| Hệ số nhọn              | Kurtosis               | $\beta_2 = \mu_4/\sigma^4$; chuẩn có $\beta_2 = 3$ |
| Đuôi nặng               | Fat tails, Heavy tails | $\beta_2 > 3$                                      |

⚠️ **Hai khác biệt quy ước cần nhớ khi dùng Excel:**
`KURT()` trả về $\beta_2 - 3$ (kurtosis dư), không phải $\beta_2$.
`VAR.S()` là phương sai **mẫu** (chia $n-1$), `VAR.P()` là phương sai **tổng thể** (chia $n$) —
bài 10 sẽ giải thích vì sao có hai loại.

---

## 11. Câu hỏi tự kiểm tra

1. Vì sao định nghĩa phương sai phải **bình phương** độ lệch? Nếu lấy $E(X - EX)$ thì được gì?
   Nếu lấy $E|X - EX|$ thì sao?
2. Chứng minh $VX = E(X^2) - (EX)^2$ từ định nghĩa (3.2).
3. $E(X+Y) = EX + EY$ có cần $X$, $Y$ độc lập không? Còn $V(X+Y) = VX + VY$?
   Cho ví dụ cụ thể mà đẳng thức thứ hai sai.
4. Vì sao $V(X + 100) = VX$ nhưng $E(X + 100) = EX + 100$? Giải thích bằng hình ảnh, không bằng
   công thức.
5. Doanh thu ngày của một cửa hàng có $EX = 20$ triệu, $\sigma = 4$ triệu. Doanh thu tháng (30 ngày,
   giả sử các ngày độc lập cùng phân phối) có kỳ vọng và độ lệch chuẩn bằng bao nhiêu?
   Vì sao $\sigma$ tháng **không** bằng $30 \times 4$?
6. Một khảo sát 100 người cho sai số ±4%. Muốn sai số ±1% thì cần bao nhiêu người?
   Chi phí tăng bao nhiêu lần?
7. Trong ba số kỳ vọng / trung vị / mốt, số nào phù hợp nhất để trả lời:
   a) "Một khách hàng điển hình chi bao nhiêu?"
   b) "Tổng doanh thu dự kiến năm tới?"
   c) "Mức giá nào bán chạy nhất?"
8. Bài 7 (tr. 77): xác suất bắn trúng đích của một khẩu súng là $p$, bắn liên tiếp tới khi trúng
   thì dừng. Tìm số đạn trung bình phải bắn. (Gợi ý: đây là phân phối hình học, sẽ gặp ở bài 7.)

---

## Tóm tắt một trang

```
╔═════════════════════════════════════════════════════════════════════════╗
║  BÀI 6 — KỲ VỌNG, PHƯƠNG SAI, SỐ ĐẶC TRƯNG       (Ch. II §3, tr. 48–56) ║
╠═════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  MẪU CHUNG CỦA MỌI CÔNG THỨC                                            ║
║      RỜI RẠC:  Σ ... pᵢ        LIÊN TỤC:  ∫ ... f(x)dx                  ║
║                                                                         ║
║  ── VỊ TRÍ ────────────────────────────────────────────────────────     ║
║  KỲ VỌNG    EX = Σ xᵢpᵢ  =  ∫ x f(x)dx        "trọng tâm"               ║
║      ⚠ EX không nhất thiết là giá trị X nhận được (xúc sắc: 3,5)        ║
║      ⚠ quyết định đầu tư: nhìn EX − CHI PHÍ, không nhìn EX trần         ║
║                                                                         ║
║  MỐT       giá trị p(x) hoặc f(x) LỚN NHẤT   (có thể nhiều mốt)         ║
║  TRUNG VỊ  giải F(x) = 1/2                    (= phân vị 50%)           ║
║  PHÂN VỊ α giải F(x) = α                                                ║
║                                                                         ║
║      lệch PHẢI:  mốt < med < EX        ← dữ liệu kinh doanh thường vậy  ║
║      đối xứng :  mốt = med = EX                                         ║
║      lệch TRÁI:  EX < med < mốt                                         ║
║                                                                         ║
║  ── PHÂN TÁN ──────────────────────────────────────────────────────     ║
║  PHƯƠNG SAI  VX = E[(X−EX)²]  =  E(X²) − (EX)²   ← dùng dạng thứ 2      ║
║              "trung bình của bình phương − bình phương của trung bình"  ║
║  ĐỘ LỆCH CHUẨN  σ = √VX      ← báo cáo cái này, CÙNG ĐƠN VỊ với X       ║
║                                                                         ║
║  ── TÍNH CHẤT: BA KHÁC BIỆT GIỮA E VÀ V ──────────────────────────      ║
║  ┌──────────────┬──────────────────┬───────────────────────────┐        ║
║  │              │   KỲ VỌNG        │      PHƯƠNG SAI           │        ║
║  ├──────────────┼──────────────────┼───────────────────────────┤        ║
║  │ nhân hằng số │  E(cX) = c·EX    │  V(cX) = c²·VX            │        ║
║  │ cộng hằng số │  E(X+c) = EX + c │  V(X+c) = VX   KHÔNG ĐỔI  │        ║
║  │ cộng 2 biến  │  LUÔN cộng được  │  CHỈ KHI ĐỘC LẬP          │        ║
║  │ nhân 2 biến  │  chỉ khi độc lập │  —                        │        ║
║  └──────────────┴──────────────────┴───────────────────────────┘        ║
║                                                                         ║
║  ⭐ HỆ QUẢ LỚN NHẤT — LUẬT CĂN BẬC HAI                                  ║
║      V(X̄) = σ²/n        σ(X̄) = σ/√n                                     ║
║      → giảm sai số 2 lần  ⟹  tăng cỡ mẫu 4 lần                          ║
║      → giảm sai số 10 lần ⟹  tăng cỡ mẫu 100 lần                        ║
║      (lý do khảo sát thị trường luôn dừng ở ~1.000 người)                ║
║                                                                          ║
║  ── HÌNH DẠNG ─────────────────────────────────────────────────────      ║
║  MÔMEN cấp k đối với a:  νₖ(a) = E[(X−a)ᵏ]                               ║
║      a = 0    → mômen GỐC      ν₁ = EX                                   ║
║      a = EX   → mômen TRUNG TÂM μ₂ = VX                                  ║
║  β₁ = μ₃/σ³  bất đối xứng   0 = đối xứng, >0 lệch phải                   ║
║  β₂ = μ₄/σ⁴  độ nhọn        CHUẨN có β₂ = 3;  >3 = ĐUÔI NẶNG             ║
║      ⚠ Excel KURT() trả về β₂ − 3, không phải β₂                         ║
║                                                                          ║
║  💼 QTKD  lương/giá nhà/thời gian chờ → dùng TRUNG VỊ (lệch phải)        ║
║          nhưng CỘNG DỒN thì phải dùng KỲ VỌNG (trung vị không cộng được) ║
║          luôn báo cáo cặp (EX, σ) — kỳ vọng đơn độc là báo cáo thiếu     ║
║          β₂ > 3 trong tài chính → mô hình chuẩn ĐÁNH GIÁ THẤP rủi ro     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương II §3, tr. 48–56.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Chứng minh công thức (3.4) (mục 3) và bảng chọn số đặc trưng (mục 7): kiến thức bổ sung.
- Khác biệt quy ước Excel `KURT()`: bổ sung.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 5 — Biến ngẫu nhiên và luật phân phối](bai_05_bien_ngau_nhien_va_luat_phan_phoi.md) ·
Bài sau: Bài 7 — Các phân phối thông dụng
