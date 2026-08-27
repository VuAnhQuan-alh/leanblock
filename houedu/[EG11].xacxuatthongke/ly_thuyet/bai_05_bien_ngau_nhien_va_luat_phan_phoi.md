# Bài 5 — Biến ngẫu nhiên và luật phân phối xác suất

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương II §1–§2**, tr. 39–48.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này nêu **một khác biệt quy ước** giữa giáo trình và Excel/Python (mục 5) — nhầm là sai đáp án.
> 📌 **Cần đọc trước:** [Bài 2](bai_02_ba_dinh_nghia_cua_xac_suat.md) · [Bài 3](bai_03_xac_suat_co_dieu_kien_va_bernoulli.md)

Chương I làm việc với **sự kiện** — thứ mô tả bằng lời. Giáo trình mở đầu Chương II bằng lý do
phải đổi cách làm (tr. 39):

> "Tính toán bằng số vốn đã quen thuộc và dễ sử dụng trong ứng dụng, nhất là có dùng tới máy tính.
> Khi nghiên cứu các sự kiện ngẫu nhiên, **rất bất tiện** khi mô tả và làm tính với các sự kiện."

Giải pháp: gắn **một con số** vào mỗi kết cục. Từ đó mọi công cụ của giải tích — tổng, tích phân,
đạo hàm — dùng được ngay. Đó là **biến ngẫu nhiên**.

## Mục lục

1. [Biến ngẫu nhiên là gì](#1-biến-ngẫu-nhiên-là-gì)
2. [Rời rạc và liên tục](#2-rời-rạc-và-liên-tục)
3. [Bảng phân phối và hàm xác suất](#3-bảng-phân-phối-và-hàm-xác-suất)
4. [Hàm của biến ngẫu nhiên](#4-hàm-của-biến-ngẫu-nhiên)
5. [Hàm phân phối xác suất](#5-hàm-phân-phối-xác-suất)
6. [Hàm mật độ xác suất](#6-hàm-mật-độ-xác-suất)
7. [📚 Ba cách mô tả một biến ngẫu nhiên](#7--ba-cách-mô-tả-một-biến-ngẫu-nhiên)
8. [Code minh hoạ](#8-code-minh-hoạ)
9. [Tự thử](#9-tự-thử)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Biến ngẫu nhiên là gì

**Định nghĩa không hình thức (tr. 39):** biến ngẫu nhiên là **một đại lượng phụ thuộc vào kết cục
của một phép thử ngẫu nhiên**.

**Thí dụ 1.1 (tr. 39).** Gieo một con xúc sắc. Biến ngẫu nhiên "số chấm xuất hiện" phụ thuộc vào
kết cục của phép thử, nhận các giá trị nguyên từ 1 đến 6.

**Thí dụ 1.2 (tr. 39).** Biến ngẫu nhiên "nhiệt độ" của một phản ứng hoá học trong một khoảng thời
gian nào đó. Nó nhận giá trị trong khoảng $[t; T]$ với $t$, $T$ là nhiệt độ thấp nhất và cao nhất.

**Định nghĩa hình thức (tr. 39):** biến ngẫu nhiên là một **hàm số có giá trị thực xác định trên
không gian các sự kiện sơ cấp** (sao cho nghịch ảnh của một khoảng số là một sự kiện).

$$X : \Omega \longrightarrow \mathbb{R}$$

Nói cách khác, biến ngẫu nhiên là **cái nhãn số** ta dán lên từng kết cục.

```
        Ω  (thế giới sự kiện)              ℝ  (thế giới số)
   ┌─────────────────────────┐
   │  ω₁ "mặt 1 chấm"  ──────┼───────────►  1
   │  ω₂ "mặt 2 chấm"  ──────┼───────────►  2
   │  ...                    │              ...
   │  ω₆ "mặt 6 chấm"  ──────┼───────────►  6
   └─────────────────────────┘
              X là mũi tên này
```

### ⚠️ Quy ước ký hiệu — nhớ kỹ, dùng suốt cả môn

Giáo trình quy định rõ (tr. 39–40):

| Ký hiệu       | Là gì                                               | Ví dụ                  |
| ------------- | --------------------------------------------------- | ---------------------- |
| $X, Y, \dots$ | **biến ngẫu nhiên** — chữ HOA, mang tính ngẫu nhiên | "số chấm sẽ xuất hiện" |
| $x, y, \dots$ | **giá trị** của biến — chữ thường, là số cụ thể     | 3                      |

> "$X$ mang tính ngẫu nhiên, còn $x$ là giá trị cụ thể quan sát được khi phép thử **đã tiến hành**
> (trong thống kê được gọi là **thể hiện** của $X$)."

Vì thế viết $P(X = 3)$ là đúng, viết $P(x = 3)$ là sai — $x$ đã là một số rồi, hỏi xác suất nó bằng 3
thì vô nghĩa. Sang phần thống kê (bài 10 trở đi), phân biệt này còn quan trọng hơn nữa.

### Chưa đủ — còn thiếu một nửa

Giáo trình cảnh báo ngay (tr. 40):

> "Việc xác định một biến ngẫu nhiên bằng **tập các giá trị** của nó rõ ràng là **chưa đủ**.
> Bước tiếp theo là phải xác định **xác suất** của từng giá trị hoặc từng tập các giá trị."

Biết "doanh thu ngày nằm trong khoảng 0 đến 50 triệu" thì chưa nói được gì. Phải biết thêm
xác suất rơi vào từng vùng — đó là **luật phân phối**, nội dung §2.

### 💼 Góc QTKD

Mọi chỉ số kinh doanh bạn theo dõi hằng ngày đều là biến ngẫu nhiên:

| Phép thử                  | Biến ngẫu nhiên $X$     | Tập giá trị            |
| ------------------------- | ----------------------- | ---------------------- |
| Một ngày kinh doanh       | số đơn hàng             | $\{0, 1, 2, \dots\}$   |
| Một chiến dịch quảng cáo  | số lượt click           | $\{0, 1, 2, \dots\}$   |
| Một khách hàng            | giá trị đơn hàng (đồng) | $[0, +\infty)$         |
| Một nhân viên trong tháng | doanh số đạt được       | $[0, +\infty)$         |
| Một lô hàng 100 sản phẩm  | số sản phẩm lỗi         | $\{0, 1, \dots, 100\}$ |

Cột giữa là "cái nhãn số" ta chọn dán lên phép thử. **Chọn nhãn khác thì bài toán khác.**
Cùng một ngày kinh doanh, có thể đặt $X$ = số đơn, hoặc $X$ = tổng doanh thu, hoặc $X$ = doanh thu
trung bình mỗi đơn — ba biến ngẫu nhiên khác nhau, ba luật phân phối khác nhau.

---

## 2. Rời rạc và liên tục

Đây là **phân đôi quan trọng nhất của cả Chương II** — mọi công thức về sau đều có hai phiên bản.

**Định nghĩa (tr. 40).**

|              | **Rời rạc** (discrete)               | **Liên tục** (continuous)                             |
| ------------ | ------------------------------------ | ----------------------------------------------------- |
| Tập giá trị  | hữu hạn **hoặc vô hạn đếm được**     | **lấp kín một khoảng** trên trục số                   |
| Miền giá trị | dãy số $x_1, x_2, \dots, x_n, \dots$ | đoạn $[a; b] \subset \mathbb{R}$ hoặc cả $\mathbb{R}$ |
| Số phần tử   | đếm được                             | vô hạn **không** đếm được                             |
| Mô tả bằng   | bảng phân phối, hàm xác suất $p(x)$  | hàm mật độ $f(x)$                                     |
| Tính bằng    | **tổng** $\sum$                      | **tích phân** $\int$                                  |

**Ví dụ của giáo trình (tr. 40):**

- **Rời rạc:** số điểm thi của một học sinh; số cuộc gọi điện thoại của một tổng đài trong một đơn vị
  thời gian; số tai nạn giao thông.
- **Liên tục:** huyết áp của một bệnh nhân; độ dài của chi tiết máy; tuổi thọ của một loại bóng đèn
  điện tử.

⚠️ **Chú ý "vô hạn đếm được" vẫn là rời rạc.** Số cuộc gọi trong một ngày về lý thuyết có thể là
$0, 1, 2, \dots$ không giới hạn — vô hạn, nhưng vẫn **đếm được**, nên vẫn rời rạc. Ranh giới không
nằm ở "hữu hạn hay vô hạn" mà ở **"đếm được hay lấp kín"**.

**Cách phân biệt trong 3 giây:** giữa hai giá trị kề nhau có giá trị nào khác không?

- Số đơn hàng: giữa 3 và 4 **không có gì** → rời rạc.
- Doanh thu: giữa 3.000.000 và 3.000.001 có 3.000.000,5 → liên tục.

### 💼 Góc QTKD — ranh giới thường bị mờ trong thực tế

**Tiền là rời rạc hay liên tục?** Về bản chất, doanh thu tính bằng đồng là **rời rạc** (không có
0,5 đồng). Nhưng vì bước nhảy (1 đồng) quá nhỏ so với độ lớn (triệu đồng), người ta **coi như liên tục**
để dùng được tích phân và phân phối chuẩn.

Ngược lại: **thời gian là liên tục**, nhưng nếu chỉ đo tới phút thì trong thực hành lại xử lý như
rời rạc.

**Quy tắc thực hành:** nếu số giá trị có thể có **lớn hơn vài chục**, hãy mô hình hoá bằng biến liên
tục — dễ tính hơn nhiều mà sai số không đáng kể. Nếu chỉ vài giá trị (số sao đánh giá 1–5, số sản
phẩm trong đơn hàng), giữ nguyên rời rạc.

⚠️ Nhưng **khi tính tiền thì luôn dùng số nguyên** trong code (đồng, xu), vì phép cộng số thực
tích luỹ sai số. Bài 10 sẽ nhắc lại chi tiết.

---

## 3. Bảng phân phối và hàm xác suất

Với biến **rời rạc**, mỗi giá trị được gắn với một xác suất: $p_i = P(X = x_i)$.

**Định nghĩa 1 (tr. 40).** Bảng phân phối xác suất của $X$:

| $X = x$ | $x_1$ | $x_2$ | $\cdots$ | $x_n$ |
| ------- | ----- | ----- | -------- | ----- |
| $p(x)$  | $p_1$ | $p_2$ | $\cdots$ | $p_n$ |

trong đó $\{x_1, x_2, \dots\}$ là tập giá trị của $X$ **đã sắp xếp theo thứ tự tăng**,
và $p_i = p(x_i) = P(X = x_i)$.

Hàm số $p(x) = P(X = x)$ gọi là **hàm xác suất** của $X$, có **hai tính chất cơ bản** (tr. 42):

$$
\begin{aligned}
&\text{(i)} && p(x) \ge 0 \quad \forall x \\
&\text{(ii)} && \sum_{\text{mọi } x} p(x) = 1
\end{aligned}
$$

Tính chất (ii) là **cách kiểm tra bài làm nhanh nhất**: lập xong bảng, cộng hàng dưới lại,
phải bằng đúng 1.

⚠️ Giáo trình lưu ý (tr. 41): $p(x) = 0$ với mọi $x$ **không nằm trong** tập giá trị của $X$.
Chẳng hạn với xúc sắc, $p(8) = 0$. Hàm xác suất xác định trên cả $\mathbb{R}$, chỉ khác 0 tại hữu hạn
(hoặc đếm được) điểm.

### Thí dụ 2.1 (tr. 41) — phân phối đều

Bảng phân phối của "số chấm xuất hiện khi gieo xúc sắc":

| $x$    | 1         | 2         | 3         | 4         | 5         | 6         |
| ------ | --------- | --------- | --------- | --------- | --------- | --------- |
| $p(x)$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ | $\frac16$ |

Các $p(x)$ đều bằng nhau → $X$ có **phân phối đều** trên tập $\{1, 2, \dots, 6\}$. Bài 7 sẽ đặt tên
chính thức cho nó.

### Thí dụ 2.2 (tr. 41) — bắn tới khi trúng

> Một xạ thủ chỉ có **3 viên đạn**. Anh ta bắn từng phát cho đến khi trúng mục tiêu thì dừng,
> biết xác suất trúng của mỗi lần bắn là 0,6. Lập bảng phân phối của **số đạn cần bắn**.

*Giải.* $X$ = số đạn cần bắn, nhận 3 giá trị 1, 2, 3.

$$
\begin{aligned}
p_1 &= P(X = 1) = P(\text{phát 1 trúng}) = 0{,}6 \\
p_2 &= P(X = 2) = P(\text{phát 1 trượt, phát 2 trúng}) = 0{,}4 \cdot 0{,}6 = 0{,}24 \\
p_3 &= P(X = 3) = 0{,}4^2 = 0{,}16
\end{aligned}
$$

| $x$    | 1   | 2    | 3    |
| ------ | --- | ---- | ---- |
| $p(x)$ | 0,6 | 0,24 | 0,16 |

⚠️ **Chỗ tinh tế nhất của thí dụ này** — giáo trình giải thích rõ: *"nếu viên thứ hai vẫn trượt,
thì **dù viên thứ ba kết quả thế nào**, $p_3$ vẫn bằng $P(X = 3) = 0{,}4^2 = 0{,}16$."*

Vì hết đạn thì buộc phải dừng, nên $X = 3$ xảy ra ngay khi hai phát đầu trượt — không cần biết
phát 3 trúng hay không. Nếu ghi $p_3 = 0{,}4^2 \cdot 0{,}6 = 0{,}096$ thì tổng chỉ được 0,936,
tính chất (ii) sập ngay.

### Thí dụ 2.3 (tr. 41) — bắn 3 phát, đếm số trúng

> Một xạ thủ **bắn 3 phát**, xác suất trúng mỗi phát là 0,6. Lập bảng phân phối của **số đạn trúng**.

*Giải.* Đây đúng là lược đồ Bernoulli ở bài 3 với $n = 3$, $p = 0{,}6$:
$p(k) = C_3^k (0{,}6)^k (0{,}4)^{3-k}$.

| $x$    | 0     | 1     | 2     | 3     |
| ------ | ----- | ----- | ----- | ----- |
| $p(x)$ | 0,064 | 0,288 | 0,432 | 0,216 |

**So sánh thí dụ 2.2 và 2.3** — cùng xạ thủ, cùng $p = 0{,}6$, nhưng hai biến ngẫu nhiên hoàn toàn
khác nhau:

|                | Thí dụ 2.2                 | Thí dụ 2.3             |
| -------------- | -------------------------- | ---------------------- |
| $X$ là gì      | số đạn **cần bắn**         | số đạn **trúng**       |
| Kịch bản       | bắn tới khi trúng thì dừng | bắn đủ 3 phát          |
| Tập giá trị    | $\{1, 2, 3\}$              | $\{0, 1, 2, 3\}$       |
| Luật phân phối | hình học (cụt)             | nhị thức $B(3; 0{,}6)$ |

**Bài học:** cùng một phép thử vật lý, đặt nhãn số khác nhau ra biến ngẫu nhiên khác nhau.
Đọc đề phải xác định **chính xác $X$ đếm cái gì**.

### 💼 Góc QTKD

Đúng hai kịch bản trên, dịch sang telesales:

|                  | "Gọi tới khi chốt được đơn thì dừng" | "Gọi đủ 20 cuộc trong ca" |
| ---------------- | ------------------------------------ | ------------------------- |
| $X$              | số cuộc gọi cần thực hiện            | số đơn chốt được          |
| Câu hỏi quản trị | *chi phí trung bình mỗi đơn*         | *sản lượng ca làm việc*   |
| Dùng để          | định giá chi phí thu hút khách (CAC) | lập kế hoạch doanh số     |

Cùng một đội telesales, hai chỉ số này trả lời hai câu hỏi quản trị khác nhau — và cần hai luật
phân phối khác nhau để tính.

---

## 4. Hàm của biến ngẫu nhiên

Giáo trình nêu một nhận xét quan trọng (tr. 42):

> "**Hàm của một hoặc nhiều biến ngẫu nhiên vẫn tiếp tục là một biến ngẫu nhiên.** Trong trường hợp
> biến rời rạc việc tìm luật phân phối của một biến hàm như vậy thường **dễ hơn** so với biến liên tục."

### Thí dụ 2.4 (tr. 42)

> Cho $X$: $-1, 0, 1$ với xác suất $0{,}3; 0{,}4; 0{,}3$ và $Y$: $1, 2$ với xác suất $0{,}3; 0{,}7$.
> Lập bảng phân phối của: a) $X^2$; b) $X + Y$.

**a) $Z = X^2$.** Chỉ có hai giá trị 0 và 1. Chú ý $Z = 1$ xảy ra khi $X = -1$ **hoặc** $X = 1$,
nên phải **gộp** hai xác suất:

| $z$    | 0   | 1                       |
| ------ | --- | ----------------------- |
| $p(z)$ | 0,4 | $0{,}3 + 0{,}3 = 0{,}6$ |

**Quy tắc:** khi hàm biến đổi làm hai giá trị khác nhau cho **cùng kết quả**, cộng xác suất lại.

**b) $Z = X + Y$.** Các giá trị: 0, 1, 2, 3. Giáo trình cho công thức tổng quát:

$$P(Z = z_k) = P(X + Y = z_k) = \sum_{x_i + y_j = z_k} P(X = x_i;\ Y = y_j)$$

Nếu $X$, $Y$ **độc lập** (sẽ nói kỹ ở chương III / bài 8) thì $P(X = x_i; Y = y_j) = P(X = x_i)P(Y = y_j)$:

| $z$    | 0    | 1    | 2    | 3    |
| ------ | ---- | ---- | ---- | ---- |
| $p(z)$ | 0,09 | 0,33 | 0,37 | 0,21 |

Ví dụ giáo trình kiểm lại (tr. 43):

$$P(Z = 2) = P(X=0; Y=2) + P(X=1; Y=1) = 0{,}4 \cdot 0{,}7 + 0{,}3 \cdot 0{,}3 = 0{,}37$$

**Phép toán này gọi là tích chập (convolution)** — cộng hai biến ngẫu nhiên độc lập.
Cách làm: xét mọi cặp $(x_i, y_j)$, nhân xác suất, rồi gom theo tổng.

💼 Trong QTKD, đây là cách **cộng doanh thu của hai chi nhánh**, **cộng số lỗi của hai dây chuyền**,
hay **gộp rủi ro của hai dự án**. Chú ý điều kiện độc lập: nếu hai chi nhánh cùng chịu ảnh hưởng của
một chiến dịch quảng cáo chung thì **không** được nhân xác suất như trên.

---

## 5. Hàm phân phối xác suất

Bảng phân phối có một hạn chế cơ bản (tr. 43): *"chưa đủ tổng quát để đặc trưng cho một biến ngẫu
nhiên tuỳ ý, nhất là trường hợp biến liên tục"*. Với biến liên tục, không thể liệt kê vô hạn không
đếm được giá trị vào một bảng.

**Định nghĩa 2 (tr. 43).**

$$F(x) = P(X < x), \qquad x \in \mathbb{R} \tag{2.1}$$

### ⚠️ KHÁC BIỆT QUY ƯỚC — đọc kỹ mục này

**Giáo trình dùng dấu $<$ NGẶT.** Sách tiếng Anh, Excel, Python, R, và hầu hết tài liệu quốc tế
dùng dấu $\le$:

$$\underbrace{F(x) = P(X < x)}_{\text{giáo trình này}} \qquad \text{vs} \qquad \underbrace{F(x) = P(X \le x)}_{\text{Excel, Python, sách Anh}}$$

Giáo trình nhất quán với quy ước của mình: ở tr. 44 nêu rõ *"$F(x)$ ít nhất phải là hàm **liên tục
trái**"*. Quy ước quốc tế cho hàm liên tục phải.

**Khi nào khác nhau?** Chỉ tại **đúng các điểm nhảy** của biến rời rạc. Với biến **liên tục**,
$P(X = a) = 0$ nên hai quy ước **cho kết quả giống hệt nhau** — đó là lý do khác biệt này ít gây hoạ.

**Khi nào gây hoạ?** Khi làm bài tập biến rời rạc và tra bảng số hoặc dùng Excel:

- Giáo trình: $F(3) = P(X < 3)$
- Excel `BINOM.DIST(3, n, p, TRUE)` $= P(X \le 3)$

Lệch nhau đúng bằng $p(3)$. **Khi đi thi, dùng quy ước giáo trình. Khi dùng máy, nhớ chuyển đổi.**

### Ý nghĩa và tính chất

$F(x)$ phản ánh **độ tập trung xác suất ở bên trái** của số thực $x$. Với biến rời rạc, (2.1) cho
một hàm còn gọi là **hàm phân phối tích luỹ** (xác suất tích luỹ).

Bốn tính chất (tr. 44):

$$
\begin{aligned}
&\text{(i)} && 0 \le F(x) \le 1 \\
&\text{(ii)} && F(x) \text{ không giảm: } x_1 < x_2 \Rightarrow F(x_1) \le F(x_2) \\
&\text{(iii)} && P(\alpha \le X < \beta) = F(\beta) - F(\alpha) \\
&\text{(iv)} && F(+\infty) = 1, \quad F(-\infty) = 0
\end{aligned}
\tag{2.2}
$$

**Tính chất (iii) là công cụ dùng nhiều nhất**: muốn xác suất rơi vào một khoảng, lấy hiệu hai giá trị
hàm phân phối. Giáo trình nhấn mạnh nó *"luôn đúng với mọi biến $X$ liên tục hay rời rạc"*.

**Hệ quả quan trọng (tr. 44):** nếu $X$ liên tục và $F(x)$ liên tục tại $a$ thì $P(X = a) = 0$.
Khi đó bốn dấu ngoặc đều như nhau:

$$P(\alpha < X < \beta) = P(\alpha \le X < \beta) = P(\alpha < X \le \beta) = P(\alpha \le X \le \beta)$$

Đây chính là điều đã gặp ở bài 2 mục 4 (xác suất hình học): với biến liên tục, một điểm có xác suất 0.

### Thí dụ 2.5 (tr. 43) — đồ thị bậc thang

Từ bảng phân phối của thí dụ 2.2, dùng (2.1): $F(x) = \sum_{x_i < x} p(x_i)$

$$
F(x) = \begin{cases}
0, & x \le 1 \\
0{,}6, & 1 < x \le 2 \\
0{,}84, & 2 < x \le 3 \\
1, & x > 3
\end{cases}
$$

```
  F(x)
   1 ┤                          ●━━━━━━━━━━━
     │                          ○
0,84 ┤              ●━━━━━━━━━━━┘
     │              ○
 0,6 ┤   ●━━━━━━━━━━┘
     │   ○
   0 ┼━━━┘
     └───┬──────────┬───────────┬───────────► x
         1          2           3

  ● = có lấy giá trị tại điểm đó   ○ = không lấy
```

Giáo trình nhận xét (tr. 43): *"$X$ có bao nhiêu giá trị thì $F(x)$ có bằng ấy **điểm gián đoạn
loại 1**"* — 3 giá trị, 3 bậc nhảy. Và **độ cao mỗi bậc chính là $p(x_i)$**. Đó là cách đọc ngược
bảng phân phối từ đồ thị.

### ⚠️ Một câu thẳng thắn đáng nhớ

> "Nếu ta biết được hàm phân phối xác suất có nghĩa là **xác định hoàn toàn** biến ngẫu nhiên.
> Tuy nhiên trong thực tế cũng phải thấy rằng việc **tìm được $F(x)$ là rất khó, nếu không nói là
> hầu như không thể làm được**." (tr. 44)

Đây là lý do tồn tại của **cả phần thống kê** (bài 10–14): vì không biết $F(x)$, ta phải **ước lượng**
nó từ dữ liệu mẫu. Và cũng là lý do của §3 (bài 6): thay vì mô tả toàn bộ $F(x)$, ta rút gọn về
vài con số đặc trưng (kỳ vọng, phương sai).

### Thí dụ 2.6 (tr. 45)

> Cho $F(x) = \begin{cases} 0, & x < 2 \\ a(x-2)^2, & 2 \le x \le 4 \\ 1, & x > 4 \end{cases}$
> Xác định $a$ và tính $P(2 < X < 3)$.

*Giải.* $X$ liên tục nên $F(x)$ liên tục. Tại $x = 4$ phải có $a(4-2)^2 = 1$, suy ra $4a = 1$:

$$a = \frac{1}{4}$$

Dùng (2.2): $P(2 < X < 3) = F(3) - F(2) = \frac14 (3-2)^2 - 0 = \mathbf{\frac14}$

**Kỹ thuật cần nhớ:** với biến liên tục, hằng số trong $F(x)$ luôn tìm được bằng **điều kiện liên tục
ở hai đầu mút** — hoặc tương đương, $F(-\infty) = 0$ và $F(+\infty) = 1$.

### 💼 Góc QTKD

Với dữ liệu kinh doanh rời rạc, $F(x)$ trả lời trực tiếp các câu hỏi hằng ngày. Ví dụ số đơn hàng
mỗi ngày của một shop:

| Số đơn $x$   | 0    | 1    | 2    | 3    | 4    | 5    |
| ------------ | ---- | ---- | ---- | ---- | ---- | ---- |
| $p(x)$       | 0,05 | 0,15 | 0,30 | 0,25 | 0,15 | 0,10 |
| $P(X \le x)$ | 0,05 | 0,20 | 0,50 | 0,75 | 0,90 | 1,00 |

- *"Xác suất hôm nay được ít nhất 3 đơn?"* $= 1 - P(X \le 2) = 1 - 0{,}50 = \mathbf{50\%}$
- *"Xác suất được từ 2 đến 4 đơn?"* $= P(X \le 4) - P(X \le 1) = 0{,}90 - 0{,}20 = \mathbf{70\%}$
- *"Ngày tệ nhất trong 10% số ngày là bao nhiêu đơn?"* → tìm $x$ nhỏ nhất với $P(X \le x) \ge 0{,}10$
  → **1 đơn**. Đây là **phân vị 10%**, khái niệm dùng để đặt ngưỡng cảnh báo.

Hàng $P(X \le x)$ chính là thứ dùng để **đặt mục tiêu và ngưỡng cảnh báo**: đặt KPI ở phân vị 75%
là mục tiêu thách thức nhưng đạt được 1/4 số ngày.

---

## 6. Hàm mật độ xác suất

Hàm $F(x)$ vẫn còn một hạn chế mà bảng phân phối không có (tr. 45): *"không cho biết rõ phân phối
xác suất ở **lân cận một điểm** nào đó trên trục số"*. Nhìn vào $F(x)$ bạn biết xác suất tích luỹ,
nhưng không thấy ngay chỗ nào "đông" chỗ nào "vắng".

Giải pháp: lấy **đạo hàm**.

**Định nghĩa 3 (tr. 45).** Hàm mật độ xác suất của biến ngẫu nhiên $X$ có $F(x)$ khả vi
(trừ ở một số hữu hạn điểm gián đoạn bị chặn):

$$f(x) = F'(x) \tag{2.3a}$$

Vì tích phân là phép toán ngược của đạo hàm:

$$F(x) = \int_{-\infty}^{x} f(t)\,dt \tag{2.3b}$$

Và (2.2) trở thành:

$$P(\alpha < X < \beta) = \int_{\alpha}^{\beta} f(x)\,dx \tag{2.4}$$

**Về mặt hình học**, (2.3b) và (2.4) cho **diện tích** phần mặt phẳng chắn bởi đường cong $y = f(x)$,
trục $Ox$ và các đường thẳng tương ứng.

```
   f(x)
     │      ╭──────╮
     │    ╱ │▒▒▒▒▒▒│ ╲
     │  ╱   │▒▒▒▒▒▒│   ╲            phần gạch = P(α < X < β)
     │╱     │▒▒▒▒▒▒│     ╲          = ∫ từ α đến β của f(x)dx
     └──────┴──────┴───────────► x
            α      β

   Tổng diện tích dưới toàn bộ đường cong = 1
```

**Hai tính chất cơ bản** (tr. 46) — song song hoàn hảo với hàm xác suất ở mục 3:

$$
\begin{aligned}
&\text{(i)} && f(x) \ge 0 \quad \forall x \\
&\text{(ii)} && \int_{-\infty}^{+\infty} f(x)\,dx = 1
\end{aligned}
$$

**Tên gọi "mật độ" từ đâu?** Giáo trình giải thích (tr. 46): ở nơi nào $f(x)$ lớn thì tại lân cận
điểm đó có **độ tập trung xác suất cao**. Giống mật độ dân số — không phải số người tại một điểm
(bằng 0!), mà là số người trên một đơn vị diện tích quanh điểm đó.

⚠️ **$f(x)$ KHÔNG phải xác suất.** Nó có thể **lớn hơn 1**. Chỉ có *diện tích dưới nó* mới là xác suất.
Ví dụ biến đều trên $[0; 0{,}1]$ có $f(x) = 10$ trên khoảng đó. Đây là chỗ nhầm rất phổ biến.

|                   | Rời rạc           | Liên tục          |
| ----------------- | ----------------- | ----------------- |
| Hàm               | $p(x) = P(X = x)$ | $f(x) = F'(x)$    |
| Có phải xác suất? | **có**            | **không**         |
| Giới hạn trên     | $\le 1$           | có thể $> 1$      |
| Tổng/tích phân    | $\sum p(x) = 1$   | $\int f(x)dx = 1$ |
| Xác suất một điểm | $p(x)$            | **luôn bằng 0**   |

### Thí dụ 2.7 (tr. 46)

> $f(x) = \begin{cases} a\cos x, & x \in [-\frac{\pi}{2}; \frac{\pi}{2}] \\ 0, & \text{ngoài ra} \end{cases}$
> a) Tìm $a$ và xác định $F(x)$. b) Tính $P\!\left(\frac{\pi}{4} < X < \pi\right)$.

*Giải.* **a)** Dùng tính chất (ii):

$$\int_{-\pi/2}^{\pi/2} a\cos x\,dx = a\left[\sin x\right]_{-\pi/2}^{\pi/2} = 2a = 1 \ \Rightarrow \ a = \frac12$$

Dùng (2.3b):

$$F(x) = \begin{cases}
0, & x < -\frac{\pi}{2} \\[4pt]
\dfrac12(\sin x + 1), & -\frac{\pi}{2} \le x \le \frac{\pi}{2} \\[4pt]
1, & x > \frac{\pi}{2}
\end{cases}$$

**b)** Theo (2.2):

$$P\!\left(\tfrac{\pi}{4} < X < \pi\right) = F(\pi) - F\!\left(\tfrac{\pi}{4}\right)
= 1 - \frac12\!\left(\frac{\sqrt2}{2} + 1\right) \approx \mathbf{0{,}1464}$$

**Quy trình chuẩn cho mọi bài "cho $f(x)$ có tham số"** — dùng lại rất nhiều:

1. Tìm tham số bằng $\int_{-\infty}^{+\infty} f(x)dx = 1$.
2. Tìm $F(x)$ bằng cách lấy tích phân từ $-\infty$ đến $x$, chia theo từng khoảng.
3. Tính xác suất bằng hiệu $F(\beta) - F(\alpha)$, hoặc tích phân trực tiếp (2.4).

### Thí dụ 2.8 (tr. 47) — phân phối mũ sinh ra từ đâu

> Xác suất phân rã của một nguyên tử chất phóng xạ trong khoảng thời gian $dt$ khá bé là $\lambda\,dt$
> (giả sử sự phân rã **không phụ thuộc vào quá khứ**). Xác định: a) xác suất phân rã trong khoảng
> thời gian $t$; b) hàm mật độ của thời điểm phân rã.

*Giải.* **a)** Xác suất **không** phân rã trong $dt$ là $1 - \lambda\,dt$. Chia $t$ thành $t/dt$
khoảng con; do độc lập, xác suất không phân rã trong cả $t$ là $(1 - \lambda\,dt)^{t/dt}$.
Lấy giới hạn khi $dt \to 0$:

$$\lim_{dt \to 0}(1 - \lambda\,dt)^{t/dt} = e^{-\lambda t}$$

Vậy xác suất phân rã trong khoảng $t$ là $1 - e^{-\lambda t}$.

**b)** $T$ = thời điểm phân rã. Xác suất phân rã trong $[t; t+dt]$ = (không phân rã trong $t$)
× (phân rã trong $dt$):

$$P(t < T < t + dt) = f(t)\,dt = e^{-\lambda t} \cdot \lambda\,dt$$

$$f(t) = \begin{cases} 0, & t < 0 \\ \lambda e^{-\lambda t}, & t \ge 0 \end{cases}$$

Đây là **phân phối mũ**, ký hiệu $T \sim \mathcal{E}(\lambda)$. Bài 7 sẽ quay lại.

**Điểm cốt lõi cần rút ra — tính "không nhớ" (memoryless):** giả thiết "phân rã không phụ thuộc
quá khứ" là **toàn bộ** nguyên nhân sinh ra dạng hàm mũ. Không có giả thiết ấy thì không ra $e^{-\lambda t}$.

💼 Trong QTKD, phân phối mũ mô tả **thời gian chờ giữa hai sự kiện độc lập**: thời gian giữa hai
khách vào cửa hàng, thời gian tới lần hỏng máy tiếp theo, thời gian tới cuộc gọi tiếp theo vào tổng đài.

⚠️ Nhưng phải kiểm giả thiết "không nhớ": máy móc **có** hao mòn (máy chạy 10 năm dễ hỏng hơn máy mới),
nên phân phối mũ **không** phù hợp cho tuổi thọ thiết bị cơ khí. Với chúng phải dùng
**phân phối Weibull** (Weibull) — sẽ gặp ở bài 6 thí dụ 3.8.

---

## 7. 📚 Ba cách mô tả một biến ngẫu nhiên

Giáo trình giới thiệu ba công cụ ở ba mục riêng mà không tổng kết. Bảng này là phần bổ sung.

|              | **Bảng phân phối / $p(x)$** | **Hàm phân phối $F(x)$**              | **Hàm mật độ $f(x)$**    |
| ------------ | --------------------------- | ------------------------------------- | ------------------------ |
| Dùng cho     | chỉ **rời rạc**             | **cả hai**                            | chỉ **liên tục**         |
| Trả lời      | $P(X = x)$                  | $P(X < x)$                            | độ đậm đặc quanh $x$     |
| Là xác suất? | ✅ có                       | ✅ có                                 | ❌ không                 |
| Chuẩn hoá    | $\sum p(x) = 1$             | $F(+\infty) = 1$                      | $\int f = 1$             |
| Đồ thị       | các cột rời                 | bậc thang (rời rạc) / trơn (liên tục) | đường cong               |
| Ưu điểm      | trực quan nhất              | **tổng quát nhất**                    | thấy hình dạng phân phối |

**Chuyển đổi qua lại:**

```
   RỜI RẠC                              LIÊN TỤC

     p(x)                                  f(x)
       │  cộng dồn                          │  tích phân
       │  Σ p(xᵢ), xᵢ < x                   │  ∫ f(t)dt từ −∞ đến x
       ▼                                    ▼
     F(x)  ◄── độ cao bậc nhảy            F(x)
              = p(xᵢ)                       │  đạo hàm
                                            ▼
                                          f(x) = F'(x)
```

**Chỉ có $F(x)$ dùng được cho cả hai** — đó là lý do giáo trình gọi nó là công cụ tổng quát nhất,
và cũng là lý do phần thống kê sau này làm việc chủ yếu với $F(x)$.

### 💼 Ba cách này trong công cụ thật

| Khái niệm      | Excel                        | Python (`statistics.NormalDist`)   |
| -------------- | ---------------------------- | ---------------------------------- |
| $p(x)$ rời rạc | `BINOM.DIST(x, n, p, FALSE)` | `math.comb(n,x)*p**x*(1-p)**(n-x)` |
| $F(x)$ rời rạc | `BINOM.DIST(x, n, p, TRUE)`  | cộng dồn                           |
| $f(x)$ chuẩn   | `NORM.DIST(x, μ, σ, FALSE)`  | `NormalDist(μ,σ).pdf(x)`           |
| $F(x)$ chuẩn   | `NORM.DIST(x, μ, σ, TRUE)`   | `NormalDist(μ,σ).cdf(x)`           |

Tham số cuối `TRUE/FALSE` trong Excel chính là **"tích luỹ hay không"** — tức chọn $F$ hay $p/f$.
Nhầm tham số này là lỗi Excel phổ biến nhất khi làm bài xác suất.

⚠️ Nhớ lại mục 5: Excel dùng $P(X \le x)$, giáo trình dùng $P(X < x)$.

---

## 8. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-05-bien-ngau-nhien.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.

Code dựng lại cả 6 thí dụ, và quan trọng nhất là **in hai cột $F(x)$ song song** để bạn thấy tận mắt
khác biệt quy ước ở mục 5.

```python
"""Bài 5 — Biến ngẫu nhiên và luật phân phối xác suất."""

import math
from fractions import Fraction
from itertools import product

# ─────────────────────────────────────────────────────────────
# 1. BẢNG PHÂN PHỐI — Thí dụ 2.2 (tr. 41)
#    Xạ thủ có 3 viên, bắn tới khi trúng thì dừng. p = 0,6.
#    X = số đạn cần bắn.
# ─────────────────────────────────────────────────────────────
p = Fraction(6, 10)
q = 1 - p
shots = {1: p, 2: q * p, 3: q * q}      # X=3: ban vien 3 du trung hay khong
print("THI DU 2.2 — so dan can ban (xa thu co 3 vien, p = 0,6)")
print(f"{'x':>4}{'p(x)':>12}{'thap phan':>12}")
for x, px in shots.items():
    print(f"{x:>4}{str(px):>12}{float(px):>12.4f}")
print("  Tong p(x) =", sum(shots.values()), "  (tinh chat (ii))")
assert sum(shots.values()) == 1

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 2.3 (tr. 41) — bắn 3 phát, X = số đạn TRÚNG
#    Đây là phân phối nhị thức B(3; 0,6)
# ─────────────────────────────────────────────────────────────
def binom(n, k, p):
    return math.comb(n, k) * p**k * (1 - p) ** (n - k)


print()
print("THI DU 2.3 — so dan TRUNG khi ban 3 phat, p = 0,6")
hits = {k: binom(3, k, Fraction(6, 10)) for k in range(4)}
print(f"{'x':>4}{'p(x)':>12}")
for x, px in hits.items():
    print(f"{x:>4}{float(px):>12.4f}")
print("  Tong =", sum(hits.values()))
assert sum(hits.values()) == 1

# ─────────────────────────────────────────────────────────────
# 3. Thí dụ 2.4 (tr. 42) — hàm của biến ngẫu nhiên
#    X: -1, 0, 1 voi 0,3 / 0,4 / 0,3 ; Y: 1, 2 voi 0,3 / 0,7
#    a) Z = X^2      b) Z = X + Y   (X, Y doc lap)
# ─────────────────────────────────────────────────────────────
X = {-1: Fraction(3, 10), 0: Fraction(4, 10), 1: Fraction(3, 10)}
Y = {1: Fraction(3, 10), 2: Fraction(7, 10)}


def transform(dist, func):
    """Luat phan phoi cua func(X) — gop cac gia tri trung nhau."""
    out = {}
    for x, px in dist.items():
        out[func(x)] = out.get(func(x), 0) + px
    return dict(sorted(out.items()))


def convolve(d1, d2, func):
    """Luat phan phoi cua func(X, Y) khi X, Y DOC LAP."""
    out = {}
    for x, px in d1.items():
        for y, py in d2.items():
            out[func(x, y)] = out.get(func(x, y), 0) + px * py
    return dict(sorted(out.items()))


print()
print("THI DU 2.4a — Z = X^2")
for z, pz in transform(X, lambda x: x * x).items():
    print(f"  z = {z}   p(z) = {float(pz)}")

print("THI DU 2.4b — Z = X + Y")
zsum = convolve(X, Y, lambda x, y: x + y)
for z, pz in zsum.items():
    print(f"  z = {z}   p(z) = {float(pz):.2f}")
print("  Kiem P(Z=2) = P(X=0)P(Y=2) + P(X=1)P(Y=1) ="
      f" {float(X[0] * Y[2] + X[1] * Y[1]):.2f}   (sach: 0,37)")
assert sum(zsum.values()) == 1

# ─────────────────────────────────────────────────────────────
# 4. HÀM PHÂN PHỐI — Thí dụ 2.5 (tr. 43)
#    ⚠ Giáo trình dùng F(x) = P(X < x)  (dấu < NGẶT)
#      Excel / Python / sách Anh dùng F(x) = P(X <= x)
# ─────────────────────────────────────────────────────────────
def F_giaotrinh(x, dist):
    return sum(px for xi, px in dist.items() if xi < x)     # dau <


def F_quocte(x, dist):
    return sum(px for xi, px in dist.items() if xi <= x)    # dau <=


print()
print("THI DU 2.5 — ham phan phoi cua bang o thi du 2.2")
print(f"{'x':>6}{'F(x)=P(X<x) giao trinh':>26}{'F(x)=P(X<=x) quoc te':>24}")
for x in [0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
    print(f"{x:>6}{float(F_giaotrinh(x, shots)):>26.2f}"
          f"{float(F_quocte(x, shots)):>24.2f}")
print("  ⚠ Hai cot chi khac nhau DUNG TAI cac diem nhay 1, 2, 3")

# ─────────────────────────────────────────────────────────────
# 5. Thí dụ 2.6 (tr. 45) — F(x) = a(x-2)^2 tren [2;4]
# ─────────────────────────────────────────────────────────────
print()
a = Fraction(1, (4 - 2) ** 2)          # lien tuc tai x=4: a(4-2)^2 = 1
print("THI DU 2.6 — F(x) = a(x-2)^2 tren [2;4]")
print("  Lien tuc tai x=4:  a(4-2)^2 = 1  ->  a =", a)
F26 = lambda x: 0 if x < 2 else (a * (x - 2) ** 2 if x <= 4 else 1)
print("  P(2 < X < 3) = F(3) - F(2) =", F26(3), "-", F26(2), "=", F26(3) - F26(2))
assert F26(3) - F26(2) == Fraction(1, 4)

# ─────────────────────────────────────────────────────────────
# 6. Thí dụ 2.7 (tr. 46) — f(x) = a cos x tren [-pi/2; pi/2]
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.7 — f(x) = a.cos(x) tren [-pi/2; pi/2]")
# tich phan cos tu -pi/2 den pi/2 = 2  ->  a = 1/2
print("  Tich phan cos tren [-pi/2;pi/2] = 2  ->  a = 1/2")
F27 = lambda x: 0.0 if x < -math.pi / 2 else (
    0.5 * (math.sin(x) + 1) if x <= math.pi / 2 else 1.0)
lo, hi = math.pi / 4, math.pi
print(f"  P(pi/4 < X < pi) = F(pi) - F(pi/4) = {F27(hi):.6f} - {F27(lo):.6f}"
      f" = {F27(hi) - F27(lo):.6f}")


def integrate(f, a_, b_, n=200_000):
    """Tich phan so bang quy tac hinh thang — de KIEM CHUNG ket qua giai tich."""
    h = (b_ - a_) / n
    return h * (f(a_) / 2 + f(b_) / 2 + sum(f(a_ + i * h) for i in range(1, n)))


f27 = lambda x: 0.5 * math.cos(x) if -math.pi / 2 <= x <= math.pi / 2 else 0.0
print(f"  Kiem bang tich phan so:            {integrate(f27, lo, hi):.6f}")
print(f"  Kiem tinh chat (ii) tong = 1:      "
      f"{integrate(f27, -math.pi / 2, math.pi / 2):.6f}")

# ─────────────────────────────────────────────────────────────
# 7. 💼 GÓC QTKD — số đơn hàng mỗi ngày của một shop nhỏ
#    Rời rạc: lập bảng, tính F(x), trả lời câu hỏi kinh doanh.
# ─────────────────────────────────────────────────────────────
print()
print("💼 GOC QTKD — so don hang moi ngay cua mot shop")
orders = {0: Fraction(5, 100), 1: Fraction(15, 100), 2: Fraction(30, 100),
          3: Fraction(25, 100), 4: Fraction(15, 100), 5: Fraction(10, 100)}
assert sum(orders.values()) == 1
print(f"{'so don x':>10}{'p(x)':>10}{'P(X<=x)':>12}")
cum = Fraction(0)
for x, px in orders.items():
    cum += px
    print(f"{x:>10}{float(px):>10.2f}{float(cum):>12.2f}")
print("  P(it nhat 3 don) = 1 - P(X<=2) =",
      1 - F_quocte(2, orders), "=", float(1 - F_quocte(2, orders)))
print("  P(2 <= X <= 4)   =", F_quocte(4, orders) - F_quocte(1, orders),
      "=", float(F_quocte(4, orders) - F_quocte(1, orders)))
```

Kết quả chạy thật:

```
THI DU 2.2 — so dan can ban (xa thu co 3 vien, p = 0,6)
   x        p(x)   thap phan
   1         3/5      0.6000
   2        6/25      0.2400
   3        4/25      0.1600
  Tong p(x) = 1   (tinh chat (ii))

THI DU 2.3 — so dan TRUNG khi ban 3 phat, p = 0,6
   x        p(x)
   0      0.0640
   1      0.2880
   2      0.4320
   3      0.2160
  Tong = 1

THI DU 2.4a — Z = X^2
  z = 0   p(z) = 0.4
  z = 1   p(z) = 0.6
THI DU 2.4b — Z = X + Y
  z = 0   p(z) = 0.09
  z = 1   p(z) = 0.33
  z = 2   p(z) = 0.37
  z = 3   p(z) = 0.21
  Kiem P(Z=2) = P(X=0)P(Y=2) + P(X=1)P(Y=1) = 0.37   (sach: 0,37)

THI DU 2.5 — ham phan phoi cua bang o thi du 2.2
     x    F(x)=P(X<x) giao trinh    F(x)=P(X<=x) quoc te
   0.5                      0.00                    0.00
     1                      0.00                    0.60
   1.5                      0.60                    0.60
     2                      0.60                    0.84
   2.5                      0.84                    0.84
     3                      0.84                    1.00
   3.5                      1.00                    1.00
  ⚠ Hai cot chi khac nhau DUNG TAI cac diem nhay 1, 2, 3

THI DU 2.6 — F(x) = a(x-2)^2 tren [2;4]
  Lien tuc tai x=4:  a(4-2)^2 = 1  ->  a = 1/4
  P(2 < X < 3) = F(3) - F(2) = 1/4 - 0 = 1/4

THI DU 2.7 — f(x) = a.cos(x) tren [-pi/2; pi/2]
  Tich phan cos tren [-pi/2;pi/2] = 2  ->  a = 1/2
  P(pi/4 < X < pi) = F(pi) - F(pi/4) = 1.000000 - 0.853553 = 0.146447
  Kiem bang tich phan so:            0.146447
  Kiem tinh chat (ii) tong = 1:      1.000000

💼 GOC QTKD — so don hang moi ngay cua mot shop
  so don x      p(x)     P(X<=x)
         0      0.05        0.05
         1      0.15        0.20
         2      0.30        0.50
         3      0.25        0.75
         4      0.15        0.90
         5      0.10        1.00
  P(it nhat 3 don) = 1 - P(X<=2) = 1/2 = 0.5
  P(2 <= X <= 4)   = 7/10 = 0.7
```

Ba điểm đáng để ý:

1. **Bảng hai cột $F(x)$** — tại $x = 1$: giáo trình cho `0.00`, Excel cho `0.60`. Tại $x = 1{,}5$
   cả hai cùng cho `0.60`. Khác biệt **chỉ** tại các điểm nhảy, đúng như mục 5 nói.
2. **Tích phân số cho `0.146447`** khớp với kết quả giải tích tới 6 chữ số. Đây là cách kiểm chứng
   một bài tích phân mà không cần tra bảng: nếu hai con số lệch nhau, bạn tính sai đâu đó.
3. **Hàm `convolve` chỉ 5 dòng** nhưng làm được đúng thứ thí dụ 2.4b yêu cầu. Chú ý dòng
   `out[func(x,y)] = out.get(...) + px*py` — chữ `+` ở đó chính là bước "gộp các giá trị trùng nhau".

---

## 9. Tự thử

1. Ở thí dụ 2.2, đổi thành xạ thủ có **5 viên đạn**. Bảng phân phối có mấy dòng? Viết lại `shots`
   cho đúng (chú ý dòng cuối!) rồi kiểm tổng có bằng 1 không.
2. Đổi `p = Fraction(6,10)` thành `Fraction(1,10)` (xạ thủ kém). Giá trị nào của $X$ giờ có xác suất
   lớn nhất? So với lúc $p = 0{,}6$.
3. Ở thí dụ 2.4, thêm phần c) $Z = XY$ và d) $Z = \max(X, Y)$. Dùng `convolve` với `lambda x,y: x*y`
   và `lambda x,y: max(x,y)`. Kiểm tổng.
4. Ở mục 4, thay `F_quocte` bằng `F_giaotrinh` trong phần Góc QTKD. Câu "P(ít nhất 3 đơn)"
   ra kết quả gì? Sai ở đâu, và vì sao?
5. Viết hàm tìm **phân vị** của bảng `orders`: cho trước $\alpha$, trả về $x$ nhỏ nhất sao cho
   $P(X \le x) \ge \alpha$. Tìm phân vị 10%, 50%, 90%.
6. Ở thí dụ 2.7, đổi hàm mật độ thành $f(x) = a x$ trên $[0; 3]$. Tìm $a$ bằng cách giải
   $\int_0^3 ax\,dx = 1$, rồi **kiểm lại bằng `integrate`**. Tính $P(1 < X < 2)$.

---

## 10. Từ điển thuật ngữ

| Tiếng Việt (giáo trình) | Tiếng Anh                              | Ghi chú                      |
| ----------------------- | -------------------------------------- | ---------------------------- |
| Biến ngẫu nhiên         | Random variable                        | ký hiệu chữ HOA $X$          |
| Thể hiện (của $X$)      | Realization / Observed value           | ký hiệu chữ thường $x$       |
| Rời rạc                 | Discrete                               | đếm được                     |
| Liên tục                | Continuous                             | lấp kín một khoảng           |
| Bảng phân phối xác suất | Probability distribution table         |                              |
| Hàm xác suất            | Probability mass function (PMF)        | $p(x) = P(X=x)$, chỉ rời rạc |
| Hàm phân phối xác suất  | Cumulative distribution function (CDF) | $F(x)$                       |
| Hàm phân phối tích luỹ  | Cumulative distribution                | tên khác của $F(x)$          |
| Hàm mật độ xác suất     | Probability density function (PDF)     | $f(x) = F'(x)$, chỉ liên tục |
| Điểm gián đoạn loại 1   | Jump discontinuity                     | bậc nhảy của $F(x)$          |
| Liên tục trái           | Left-continuous                        | do quy ước $F(x) = P(X < x)$ |
| Tích chập               | Convolution                            | luật phân phối của $X + Y$   |
| Phân phối mũ            | Exponential distribution               | $\mathcal{E}(\lambda)$       |
| Tính không nhớ          | Memoryless property                    | đặc trưng của phân phối mũ   |

---

## 11. Câu hỏi tự kiểm tra

1. Phân biệt $X$ và $x$. Viết $P(x = 3)$ sai ở chỗ nào?
2. "Số lượt truy cập website trong một ngày" là rời rạc hay liên tục? Tập giá trị có hữu hạn không?
3. Cho bảng phân phối với $p(1) = a$, $p(2) = 2a$, $p(3) = a$, $p(4) = 3a$, $p(5) = 2a$
   (bài 5, tr. 77). a) Tìm $a$. b) Tìm $k$ nhỏ nhất sao cho $P(X < k) > \frac12$.
4. Vì sao trong thí dụ 2.2, $p_3 = 0{,}4^2$ chứ không phải $0{,}4^2 \cdot 0{,}6$? Nếu xạ thủ có
   **vô hạn** đạn thì bảng phân phối thế nào?
5. Hàm mật độ $f(x)$ có thể lớn hơn 1 không? Cho một ví dụ cụ thể và giải thích vì sao không mâu thuẫn.
6. Cho $F(x) = a + b\arcsin\frac{x}{2}$ với $-2 \le x \le 2$ (bài 9, tr. 77). Tìm $a$, $b$
   bằng điều kiện $F(-2) = 0$ và $F(2) = 1$.
7. Một shop có bảng phân phối số đơn hàng như ở mục 5. Nếu mỗi đơn lãi 50.000 đồng và chi phí cố định
   mỗi ngày là 100.000 đồng, lập bảng phân phối của **lợi nhuận ngày**. Xác suất lỗ là bao nhiêu?
8. Vì sao phân phối mũ **không** phù hợp để mô tả tuổi thọ của một chiếc xe máy?
   Giả thiết nào của thí dụ 2.8 bị vi phạm?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 5 — BIẾN NGẪU NHIÊN VÀ LUẬT PHÂN PHỐI     (Ch. II §1–2, tr. 39–48)  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BIẾN NGẪU NHIÊN  X : Ω → ℝ    "dán nhãn số lên mỗi kết cục"            ║
║      X chữ HOA = biến (ngẫu nhiên)                                       ║
║      x chữ thường = giá trị quan sát được (thể hiện)                     ║
║      ⚠ P(X = 3) đúng   |   P(x = 3) SAI                                 ║
║                                                                          ║
║  HAI LOẠI                                                                ║
║      RỜI RẠC   đếm được (kể cả vô hạn)   → dùng Σ                       ║
║      LIÊN TỤC  lấp kín một khoảng        → dùng ∫                       ║
║      Phân biệt: giữa 2 giá trị kề nhau có giá trị nào khác không?       ║
║                                                                          ║
║  BA CÁCH MÔ TẢ                                                           ║
║  ┌──────────┬────────────┬──────────────┬─────────────────────┐          ║
║  │          │   p(x)     │     F(x)     │        f(x)         │          ║
║  ├──────────┼────────────┼──────────────┼─────────────────────┤          ║
║  │ dùng cho │  rời rạc   │   CẢ HAI     │      liên tục       │          ║
║  │ nghĩa    │  P(X=x)    │   P(X<x)     │  mật độ = F'(x)     │          ║
║  │ là XS?   │    CÓ      │     CÓ       │  KHÔNG (có thể >1)  │          ║
║  │ chuẩn hoá│  Σp = 1    │   F(∞)=1     │      ∫f = 1         │          ║
║  └──────────┴────────────┴──────────────┴─────────────────────┘          ║
║                                                                          ║
║      p(x) ──cộng dồn──► F(x) ◄──đạo hàm/tích phân──► f(x)              ║
║      độ cao bậc nhảy của F(x) = p(xᵢ)                                    ║
║                                                                          ║
║  ⚠⚠ KHÁC BIỆT QUY ƯỚC                                                   ║
║      GIÁO TRÌNH:  F(x) = P(X < x)   dấu < NGẶT, liên tục TRÁI           ║
║      EXCEL/PYTHON: F(x) = P(X ≤ x)  dấu ≤,      liên tục PHẢI           ║
║      → chỉ khác nhau tại các ĐIỂM NHẢY của biến rời rạc                 ║
║      → với biến LIÊN TỤC hai quy ước cho kết quả GIỐNG HỆT              ║
║                                                                          ║
║  TÍNH CHẤT F(x)                                                          ║
║      0 ≤ F ≤ 1 ;  F không giảm ;  F(−∞)=0, F(+∞)=1                      ║
║      P(α ≤ X < β) = F(β) − F(α)          ← dùng nhiều nhất              ║
║      X liên tục ⟹ P(X = a) = 0 ⟹ 4 kiểu ngoặc như nhau                  ║
║                                                                          ║
║  QUY TRÌNH BÀI "CHO f(x) CÓ THAM SỐ"                                     ║
║      1. ∫f = 1  →  tìm tham số                                           ║
║      2. F(x) = ∫ từ −∞ đến x, chia theo khoảng                          ║
║      3. P(α<X<β) = F(β) − F(α)                                           ║
║      (biến F(x) có tham số: dùng ĐIỀU KIỆN LIÊN TỤC ở hai mút)          ║
║                                                                          ║
║  PHÂN PHỐI MŨ  f(t) = λe^(−λt), t ≥ 0                                    ║
║      sinh ra từ giả thiết KHÔNG NHỚ (không phụ thuộc quá khứ)           ║
║      ⚠ không dùng cho thứ có HAO MÒN → dùng Weibull                     ║
║                                                                          ║
║  💼 QTKD  hàng P(X≤x) = công cụ đặt KPI và ngưỡng cảnh báo               ║
║          Excel: tham số TRUE/FALSE cuối = chọn F(x) hay p(x)/f(x)       ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương II §1–§2, tr. 39–48.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Khác biệt quy ước $F(x) = P(X < x)$ vs $P(X \le x)$ (mục 5): giáo trình dùng dấu $<$ tại (2.1)
  tr. 43 và khẳng định $F$ liên tục trái ở tr. 44. So sánh với quy ước quốc tế là phần bổ sung.
- Bảng đối chiếu ba cách mô tả (mục 7): kiến thức bổ sung.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 4 — Xác suất đầy đủ và công thức Bayes](bai_04_xac_suat_day_du_va_bayes.md) ·
Bài sau: Bài 6 — Kỳ vọng, phương sai và các số đặc trưng
