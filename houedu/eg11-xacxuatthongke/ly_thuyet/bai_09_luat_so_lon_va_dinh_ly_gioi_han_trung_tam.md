# Bài 9 — Hàm của biến ngẫu nhiên, luật số lớn và định lý giới hạn trung tâm

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương III §3–§4**, tr. 96–112.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính một lỗi in** của giáo trình: thí dụ 4.1b (tr. 107).
> 📌 **Cần đọc trước:** [Bài 6](bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md) · [Bài 7](bai_07_cac_phan_phoi_thong_dung.md) · [Bài 8](bai_08_bien_ngau_nhien_hai_chieu_va_tuong_quan.md)

Đây là bài **khép lại phần xác suất** và **mở ra phần thống kê**. Giáo trình nói rõ (tr. 103):

> "Các định lý giới hạn và luật số lớn **rất có ý nghĩa trong thực tiễn**. Nó tạo ra **cơ sở cho các
> ứng dụng của thống kê toán học** sau này."

Từ bài 10 trở đi, ta sẽ lấy dữ liệu mẫu để suy đoán về tổng thể. **Vì sao được phép làm thế?**
Câu trả lời nằm ở đây, trong hai định lý:

- **Luật số lớn** — trung bình mẫu tiến về kỳ vọng thật. *Vì thế đo được.*
- **Định lý giới hạn trung tâm** — trung bình mẫu có phân phối **chuẩn**, bất kể dữ liệu gốc
  phân phối thế nào. *Vì thế tính được sai số.*

Không có hai định lý này thì cả phần thống kê là vô căn cứ.

## Mục lục

1. [Hàm của một biến ngẫu nhiên](#1-hàm-của-một-biến-ngẫu-nhiên)
2. [Hàm của hai biến ngẫu nhiên](#2-hàm-của-hai-biến-ngẫu-nhiên)
3. [Số đặc trưng của hàm các biến ngẫu nhiên](#3-số-đặc-trưng-của-hàm-các-biến-ngẫu-nhiên)
4. [Bốn kiểu hội tụ](#4-bốn-kiểu-hội-tụ)
5. [Bất đẳng thức Chebyshev](#5-bất-đẳng-thức-chebyshev)
6. [Luật số lớn](#6-luật-số-lớn)
7. [Định lý giới hạn trung tâm](#7-định-lý-giới-hạn-trung-tâm)
8. [📚 Vì sao hai định lý này là nền của cả phần thống kê](#8--vì-sao-hai-định-lý-này-là-nền-của-cả-phần-thống-kê)
9. [Code minh hoạ](#9-code-minh-hoạ)
10. [Tự thử](#10-tự-thử)
11. [Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
12. [Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Hàm của một biến ngẫu nhiên

**Bài toán:** biết luật phân phối của $X$, tìm luật phân phối của $Z = g(X)$.

### Trường hợp rời rạc — dễ

**Thí dụ 3.1 (tr. 96).**

> $X$ có phân phối: $-2, -1, 0, 1, 2$ với xác suất $0{,}1;\ 0{,}2;\ 0{,}3;\ 0{,}2;\ 0{,}2$.
> Xác định luật phân phối của $Z = X^2$ và tìm $EZ$.

*Giải.* Ghép các giá trị $x$ cho cùng một $z$:

$$
\begin{aligned}
P(Z = 0) &= P(X = 0) = 0{,}3 \\
P(Z = 1) &= P(X = -1) + P(X = 1) = 0{,}2 + 0{,}2 = 0{,}4 \\
P(Z = 4) &= P(X = -2) + P(X = 2) = 0{,}1 + 0{,}2 = 0{,}3
\end{aligned}
$$

| $z$    | 0   | 1   | 4   |
| ------ | --- | --- | --- |
| $p(z)$ | 0,3 | 0,4 | 0,3 |

$$EZ = 0 \cdot 0{,}3 + 1 \cdot 0{,}4 + 4 \cdot 0{,}3 = \mathbf{1{,}6}$$

**Quy tắc:** hàm không đơn ánh thì **cộng** các xác suất của những $x$ cho cùng $z$.
(Đã gặp ở bài 5 thí dụ 2.4a.)

Giáo trình nhắc lại lối tắt (tr. 97): không cần lập bảng của $Z$, tính thẳng bằng tính chất (v)
của kỳ vọng (bài 6 mục 2):

$$EZ = E[g(X)] = \sum_i g(x_i)\,p_i = (-2)^2 \cdot 0{,}1 + (-1)^2 \cdot 0{,}2 + 0^2 \cdot 0{,}3 + 1^2 \cdot 0{,}2 + 2^2 \cdot 0{,}2 = 1{,}6$$

Cùng kết quả, **ít việc hơn**.

### Trường hợp liên tục — công thức đổi biến

Giáo trình cảnh báo (tr. 97): *"Khi $X$ là biến ngẫu nhiên liên tục, vấn đề sẽ phức tạp hơn."*

Giả sử $X$ có mật độ $f(x)$, và $Z = g(X)$ với $g$ **đơn điệu**, tồn tại hàm ngược duy nhất
$x = \psi(z) = g^{-1}(z)$. Khi đó mật độ của $Z$:

$$\varphi(z) = f\big[\psi(z)\big]\cdot\big|\psi'(z)\big| \tag{3.1}$$

**Vì sao có $|\psi'(z)|$?** Vì phép đổi biến làm co giãn trục số; thừa số đó là **hệ số co giãn**,
giữ cho tổng xác suất vẫn bằng 1. Dấu trị tuyệt đối để mật độ luôn không âm.

**Thí dụ 3.3 (tr. 98) — kết quả quan trọng nhất mục này.**

> $X \sim N(m; \sigma^2)$. Tìm luật phân phối của $Y = aX + b$ với $a, b \in \mathbb{R}$.

*Giải.* $\psi(y) = \dfrac{y-b}{a}$, $\psi'(y) = \dfrac1a$. Thay vào (3.1) và rút gọn, giáo trình
được đúng dạng mật độ chuẩn với hai tham số:

$$EY = am + b, \qquad VY = a^2\sigma^2$$

> "Như vậy một **hàm tuyến tính của biến ngẫu nhiên chuẩn vẫn bảo toàn tính phân phối chuẩn**." (tr. 98)

⭐ Đây chính là điều làm phép **quy chuẩn** ở bài 7 mục 6 hợp lệ: $Z = \dfrac{X-a}{\sigma}$
là một hàm tuyến tính, nên $Z$ vẫn chuẩn. Không có tính chất này thì cả bảng tra hàm Laplace
vô dụng.

💼 Hệ quả kinh doanh: nếu doanh thu chuẩn thì **lợi nhuận = doanh thu × biên − chi phí cố định**
cũng chuẩn (vì là hàm tuyến tính). Nhưng nếu bạn nhân hai biến ngẫu nhiên với nhau
(doanh thu = số đơn × giá trị đơn) thì **không** còn chuẩn — phép nhân không tuyến tính.

---

## 2. Hàm của hai biến ngẫu nhiên

Giáo trình thu hẹp phạm vi ngay (tr. 98–99): *"Nếu $g$ là một hàm tuỳ ý thì bài toán... sẽ **rất
phức tạp**. Ta sẽ xét một trường hợp đơn giản khi $g(X,Y) = X + Y$."*

### Rời rạc

$$P(Z = z_k) = \sum_i P(X = x_i;\ Y = z_k - x_i)$$

Nếu $X$, $Y$ **độc lập**:

$$P(Z = z_k) = \sum_i p_1(x_i)\,p_2(z_k - x_i) \tag{3.2}$$

**Thí dụ 3.3 (tr. 99).** *(Giáo trình đánh trùng số hiệu với thí dụ ở mục 1 — chú ý khi tra.)*

> Cho luật phân phối đồng thời của $(X, Y)$, xác định luật phân phối của $X + Y$.

| $X \backslash Y$ |    2 |    3 |    4 |
| ---------------- | ---: | ---: | ---: |
| **1**            |    0 | 0,15 | 0,05 |
| **2**            | 0,20 | 0,10 |    0 |
| **3**            | 0,25 | 0,05 | 0,20 |

*Giải.* Tập giá trị của $Z$ là $\{3,4,5,6,7\}$. Gom theo **đường chéo** của bảng:

$$
\begin{aligned}
P(Z=3) &= P(1,2) = 0 \\
P(Z=4) &= P(1,3) + P(2,2) = 0{,}15 + 0{,}20 = 0{,}35 \\
P(Z=5) &= P(1,4) + P(2,3) + P(3,2) = 0{,}05 + 0{,}10 + 0{,}25 = 0{,}40 \\
P(Z=6) &= P(2,4) + P(3,3) = 0 + 0{,}05 = 0{,}05 \\
P(Z=7) &= P(3,4) = 0{,}20
\end{aligned}
$$

⚠️ Chú ý bài này **không** cần giả thiết độc lập — đề cho sẵn bảng đồng thời. Chỉ khi phải suy ra
bảng đồng thời từ hai bảng biên mới cần độc lập.

### Thí dụ 3.4 (tr. 100) — tổng hai Poisson

> $X \sim P(\lambda)$, $Y \sim P(\mu)$ độc lập. Tìm luật phân phối của $Z = X + Y$.

*Giải.* Theo (3.2), nhân và chia vế phải với $z!$, giáo trình biến đổi được:

$$P(Z = z) = \frac{e^{-(\lambda+\mu)}(\lambda+\mu)^z}{z!}$$

> "Hệ thức cuối cho thấy $Z = X + Y$ cũng tuân theo luật Poisson với tham số $\lambda + \mu$."

Đây chính là **tính cộng được** đã nêu ở bài 7 mục 3, giờ được chứng minh.

### Liên tục — tích chập

$$\varphi(z) = \int_{-\infty}^{+\infty} f(x, z-x)\,dx \tag{3.3a}$$

Nếu $X$, $Y$ độc lập:

$$\varphi(z) = \int_{-\infty}^{+\infty} f_1(x)\,f_2(z-x)\,dx = f_1 * f_2 \tag{3.4}$$

Phép toán này gọi là **tích chập** (convolution), ký hiệu $f_1 * f_2$.

### Thí dụ 3.5 (tr. 101) — hai biến đều cộng lại thành tam giác

> $X$, $Y$ độc lập cùng $\sim \mathcal{U}([0;1])$. Tìm mật độ của $Z = X + Y$.

*Giải.* Chia theo khoảng, giáo trình được:

$$\varphi(z) = \begin{cases}
0, & z < 0 \\
z, & 0 \le z \le 1 \\
2 - z, & 1 < z \le 2 \\
0, & z > 2
\end{cases}$$

```
   φ(z)
    1 ┤        ╱╲
      │      ╱    ╲
      │    ╱        ╲
    0 ┼──╱────────────╲──► z
      0      1        2
```

Biến $Z$ này gọi là **phân phối tam giác** hay **phân phối Simpson** (Simpson).

⭐ **Đây là bằng chứng đầu tiên của định lý giới hạn trung tâm.** Cộng **hai** biến phẳng lì đã ra
hình tam giác — đã có đỉnh, đã đối xứng. Cộng ba biến sẽ ra đường cong trơn hơn nữa; cộng nhiều
biến thì tiến về hình chuông. Mục 7 sẽ phát biểu chính xác.

💼 Ứng dụng: **phân phối tam giác được dùng rộng rãi trong quản trị dự án** (thay cho đều, như đã
nhắc ở bài 7 mục 1) vì nó cho phép nêu ba con số: tối thiểu, khả năng cao nhất, tối đa.

---

## 3. Số đặc trưng của hàm các biến ngẫu nhiên

Giáo trình nêu vấn đề thực tế (tr. 102):

> "Việc xác định luật phân phối của $Z$ khá phức tạp. Trong thực tế nhiều khi ta **chỉ cần quan tâm
> đến các số đặc trưng** của $Z$ là đủ."

Công thức tổng quát:

$$EZ = E[g(X,Y)] = \sum_i\sum_j g(x_i, y_j)\,p(x_i, y_j) \tag{3.6a}$$

$$EZ = \iint_{\mathbb{R}^2} g(x,y)\,f(x,y)\,dx\,dy \tag{3.6b}$$

Từ (3.6) chứng minh được chặt chẽ các tính chất đã dùng ở bài 6:

$$E(X+Y) = EX + EY, \qquad X,Y \text{ độc lập} \Rightarrow E(XY) = EX \cdot EY$$

$$X, Y \text{ độc lập} \Rightarrow V(X+Y) = VX + VY$$

📚 **Bổ sung — điều kiện có thể nới lỏng.** Bài 6 mục 4 có ghi lời hứa của giáo trình:
*"điều kiện độc lập là khá chặt, sau này ở chương III ta thấy có thể giảm nhẹ"*. Đây là câu trả lời:

$$\boxed{V(X + Y) = VX + VY + 2\mu_{XY}}$$

Nên chỉ cần $\mu_{XY} = 0$ (**không tương quan**) là đủ, không cần độc lập hoàn toàn.
Vì độc lập ⟹ không tương quan (bài 8 mục 5), điều kiện mới **yếu hơn thật sự**.

💼 Công thức này là **công thức rủi ro danh mục đầu tư**. Ghép hai tài sản:

- $\mu_{12} > 0$ (cùng lên cùng xuống) → rủi ro tổng **lớn hơn** tổng rủi ro riêng lẻ;
- $\mu_{12} = 0$ → cộng đơn thuần;
- $\mu_{12} < 0$ (ngược chiều) → rủi ro tổng **nhỏ hơn** — đây chính là lợi ích của **đa dạng hoá**.

---

## 4. Bốn kiểu hội tụ

Trước khi phát biểu các định lý giới hạn, phải nói rõ "hội tụ" nghĩa là gì. Với biến ngẫu nhiên,
có **bốn nghĩa khác nhau** (tr. 103–105).

### 1. Hội tụ hầu chắc chắn (mạnh) — $X_n \xrightarrow{h.c.c} X$

$$P\left(\lim_{n\to\infty} X_n = X\right) = 1$$

*"Hội tụ hầu chắc chắn trùng với hội tụ thường đối với sự kiện có xác suất 1."*

### 2. Hội tụ theo xác suất — $X_n \xrightarrow{xs} X$

$$\forall \varepsilon > 0: \quad P\big(|X_n - X| > \varepsilon\big) \xrightarrow[n\to\infty]{} 0 \tag{4.2}$$

Nghĩa: xác suất để $X_n$ lệch khỏi $X$ quá $\varepsilon$ tiến về 0.

### 3. Hội tụ theo luật — $X_n \xrightarrow{L} X$

Dãy hàm phân phối $F_n(x)$ hội tụ đến $F(x)$ tại mọi điểm liên tục của $F$.

Giáo trình nhận xét (tr. 104): *"Đây là kiểu hội tụ **yếu nhất**, tuy nhiên lại **hay dùng nhất**."*
Bài 7 đã dùng nó khi viết $\dfrac{X - np}{\sqrt{npq}} \xrightarrow{L} N(0;1)$ (4.3).

### 4. Hội tụ trung bình cấp $k$ — $X_n \xrightarrow{tbk} X$

$$E|X_n - X|^k \xrightarrow[n\to\infty]{} 0$$

Hay dùng với $k = 2$ (hội tụ trung bình bình phương).

### Thứ tự mạnh yếu

```
   HẦU CHẮC CHẮN  ─┐
                   ├──►  THEO XÁC SUẤT  ──►  THEO LUẬT
   TRUNG BÌNH CẤP k┘         (4.2)              (yếu nhất, hay dùng nhất)
        (k=2)

   Mũi tên = "kéo theo".  Chiều ngược lại nói chung SAI.
```

⚠️ Vì sao phải phân biệt? Vì **luật số lớn** dùng hội tụ theo **xác suất**, còn **định lý giới hạn
trung tâm** dùng hội tụ theo **luật** — hai loại kết luận khác nhau về bản chất. Giáo trình lưu ý
điều này ở tr. 107.

📚 **Nói bằng lời cho dễ nhớ:**

| Kiểu          | Nói gì                                                       |
| ------------- | ------------------------------------------------------------ |
| Theo xác suất | *"$X_n$ tiến gần **một con số**"*                            |
| Theo luật     | *"**hình dạng phân phối** của $X_n$ tiến gần một hình dạng"* |

Luật số lớn nói trung bình mẫu tiến về **con số** $a$. CLT nói **hình dạng** phân phối của nó tiến
về hình chuông. Hai câu khác hẳn nhau, và cả hai đều cần thiết.

---

## 5. Bất đẳng thức Chebyshev

**Định lý 1 (tr. 107).** Nếu $X$ có $EX = a$ và $VX = \sigma^2$ **hữu hạn** thì

$$P\big(|X - a| \ge \varepsilon\big) \le \frac{\sigma^2}{\varepsilon^2} \tag{4.7}$$

Dạng tương đương:

$$P\big(|X - a| < \varepsilon\big) \ge 1 - \frac{\sigma^2}{\varepsilon^2} \tag{4.8}$$

**Chứng minh** (giáo trình làm cho trường hợp liên tục, tr. 107) — rất ngắn và đáng đọc:

$$P(|X-a| \ge \varepsilon) = \int_{|x-a|\ge\varepsilon} f(x)dx$$

Trong miền lấy tích phân, $\dfrac{(x-a)^2}{\varepsilon^2} \ge 1$, nên có thể nhân vào mà tích phân
không giảm:

$$\le \int_{|x-a|\ge\varepsilon} \frac{(x-a)^2}{\varepsilon^2}f(x)dx
\le \frac{1}{\varepsilon^2}\int_{-\infty}^{+\infty}(x-a)^2 f(x)dx = \frac{\sigma^2}{\varepsilon^2} \qquad \blacksquare$$

### ⭐ Vì sao bất đẳng thức "yếu" này lại quan trọng

Giáo trình nói (tr. 108): *"Mặc dù (4.7) – (4.8) được chứng minh khá đơn giản, song chúng có
**ý nghĩa rất to lớn** để dùng làm cơ sở cho các ứng dụng của thống kê."*

**Vì nó không cần biết dạng phân phối.** Đúng cho *mọi* biến ngẫu nhiên có phương sai hữu hạn.

Cái giá phải trả: chặn rất lỏng. Giáo trình chỉ ra ngay:

| $\varepsilon$ |    Chặn Chebyshev | Giá trị thật nếu $X$ chuẩn |
| ------------- | -----------------: | -------------------------: |
| $1\sigma$     | $\le 1$ (vô nghĩa) |                     0,3173 |
| $2\sigma$     |       $\le 0{,}25$ |                     0,0455 |
| $3\sigma$     |     $\le 0{,}1111$ |                     0,0027 |
| $4\sigma$     |     $\le 0{,}0625$ |                   0,000063 |

Giáo trình nhận xét (tr. 108): với $\varepsilon = 3\sigma$ ta có $P(|X-a| < 3\sigma) \ge 1 - \frac19 \approx 0{,}9$
— *"ít nhất bằng 0,9"*, trong khi với phân phối chuẩn con số thật là **0,9973**.

⚠️ Nếu chọn $\varepsilon < \sigma$ thì bất đẳng thức trở nên **tầm thường** (chặn > 1, không nói gì).

**Cách nghĩ đúng về Chebyshev:**

> Nó là **bảo đảm tối thiểu** khi bạn không biết gì về phân phối. Biết thêm (ví dụ: phân phối chuẩn)
> thì có kết quả tốt hơn nhiều. Không biết gì thì đây là tất cả những gì bạn có.

💼 Trong quản trị rủi ro, Chebyshev cho **giới hạn xấu nhất tuyệt đối**: dù lợi suất phân phối
kiểu gì, xác suất lệch quá $3\sigma$ không bao giờ vượt 11%. Câu này đúng kể cả với phân phối
đuôi nặng — nơi giả định chuẩn thất bại thảm hại (bài 6 mục 6).

---

## 6. Luật số lớn

### Luật số lớn Chebyshev

**Định lý 2 (tr. 108).** Nếu dãy $X_1, X_2, \dots$ **độc lập**, có kỳ vọng hữu hạn và
**phương sai bị chặn đều** ($VX_i \le C$ với mọi $i$), thì với mọi $\varepsilon > 0$:

$$\lim_{n\to\infty} P\left(\left|\frac1n\sum_{i=1}^n X_i - \frac1n\sum_{i=1}^n EX_i\right| < \varepsilon\right) = 1 \tag{4.9}$$

**Chứng minh** (tr. 108) chỉ ba dòng — áp Chebyshev cho $\overline{X}$:

Đặt $\overline{X} = \frac1n\sum X_i$. Khi đó $E\overline{X} = \frac1n\sum EX_i$ và
$V\overline{X} = \frac{1}{n^2}\sum VX_i \le \frac{C}{n}$ (dùng luật căn bậc hai ở bài 6 mục 4).
Áp (4.8):

$$P\big(|\overline{X} - E\overline{X}| < \varepsilon\big) \ge 1 - \frac{V\overline{X}}{\varepsilon^2} \ge 1 - \frac{C}{n\varepsilon^2} \xrightarrow[n\to\infty]{} 1 \qquad \blacksquare$$

**Ý nghĩa (tr. 109):** *"khi $n$ đủ lớn thì **trung bình cộng của các biến ngẫu nhiên** sẽ có giá trị
**lệch rất ít so với trung bình cộng của các kỳ vọng**."*

**Hệ quả quan trọng** — khi các $X_i$ có **cùng kỳ vọng** $a$:

$$\overline{X} \xrightarrow{xs} a$$

> "Sự kiện này cho phép ta **ước lượng kỳ vọng bằng trung bình cộng các kết quả đo đạc độc lập**." (tr. 109)

⭐ **Đây là lý do tồn tại của toàn bộ ngành thống kê.** Ta không biết $a$; ta đo $n$ lần rồi lấy
trung bình; luật số lớn bảo đảm con số đó tiến về $a$.

### Luật số lớn Bernoulli

**Định lý 3 (tr. 109).** Dãy $n$ phép thử Bernoulli độc lập với $p = P(A)$, $m$ là số lần xuất hiện $A$:

$$\lim_{n\to\infty} P\left(\left|\frac{m}{n} - p\right| < \varepsilon\right) = 1 \tag{4.11}$$

tức $\dfrac{m}{n} \xrightarrow{xs} p$.

Chứng minh: là trường hợp riêng của định lý 2 với $X_i \sim B(p)$, $EX_i = p$, $VX_i = p(1-p) \le 1$.

⭐ Giáo trình kết luận (tr. 109):

> "đó chính là **cơ sở cho định nghĩa thống kê của xác suất** đã đưa ra ở chương I."

**Vòng tròn khép lại.** Ở bài 2 mục 5, ta *chấp nhận* rằng tần suất ổn định quanh một hằng số và
lấy nó làm xác suất. Bây giờ điều đó được **chứng minh** — nó là một định lý, không phải một giả định.

Và giáo trình khép §4 bằng một câu tổng kết đẹp (tr. 110):

> "Như vậy tổng của một số khá lớn các biến ngẫu nhiên **tương đối tuỳ ý** lại trở nên tuân theo
> **một số quy luật xác định**."

### 💼 Góc QTKD — luật số lớn ai được lợi

| Ai                       | Lặp bao nhiêu lần               | Luật số lớn có hiệu lực?       |
| ------------------------ | ------------------------------- | ------------------------------ |
| Công ty bảo hiểm         | hàng triệu hợp đồng             | ✅ lợi nhuận gần như chắc chắn |
| Sòng bạc / xổ số         | hàng triệu ván                  | ✅ (bài 6 thí dụ 3.4)          |
| Sàn thương mại điện tử   | hàng triệu đơn                  | ✅ tỷ lệ hoàn hàng rất ổn định |
| Quỹ đầu tư chỉ số        | hàng nghìn cổ phiếu × nhiều năm | ✅ một phần                    |
| **Người mua vé số**      | vài chục lần                    | ❌                             |
| **Startup gọi vốn**      | 1 lần                           | ❌                             |
| **Bạn chọn nghề nghiệp** | 1 lần                           | ❌                             |

⚠️ **Bài học quản trị quan trọng nhất:** luật số lớn chỉ giúp **bên lặp lại nhiều lần**.
Với quyết định **làm một lần**, kỳ vọng gần như vô dụng — phải nhìn tình huống xấu nhất và
khả năng chịu đựng.

Đó cũng là lý do bảo hiểm tồn tại được: công ty bảo hiểm ở phía "lặp nhiều lần", khách hàng
ở phía "một lần". Hai bên đều có lợi dù kỳ vọng của khách hàng là âm.

---

## 7. Định lý giới hạn trung tâm

### de Moivre – Laplace

Từ (4.3), giáo trình suy ra hai định lý đã dùng ở chương I và II (tr. 105):

$$P_n(k) \approx \frac{1}{\sqrt{npq}}\varphi\!\left(\frac{k-np}{\sqrt{npq}}\right) \tag{4.4}$$

$$P_n(k_1;k_2) \approx \phi(x_2) - \phi(x_1), \quad x_i = \frac{k_i - np}{\sqrt{npq}} \tag{4.5}$$

Điều kiện: *"khá tốt khi $np > 5$ hoặc $nq > 5$. Nếu $p$ càng gần 0,5 đồ thị của phân phối nhị thức
càng rất gần chuẩn."*

### ⭐ Định lý giới hạn trung tâm (Lindeberg – Lévy, 1922)

**Định lý (tr. 106).** Giả sử $\{X_n\}$ là dãy biến ngẫu nhiên **độc lập, cùng phân phối**,
với $EX_n = m$ và $VX_n = \sigma^2$ với mọi $n$. Khi đó

$$\frac{\overline{X} - m}{\sigma/\sqrt{n}} \ \xrightarrow{\ L\ } \ N(0;1)
\qquad\text{hay tương đương}\qquad
\sum_{i=1}^n X_i \ \xrightarrow{\ L\ } \ N(nm;\ n\sigma^2) \tag{4.6}$$

**Ý nghĩa, theo lời giáo trình (tr. 106):**

> "Khi có **nhiều nhân tố ngẫu nhiên tác động** (sao cho **không có nhân tố nào vượt trội lấn át**
> các nhân tố khác) thì kết quả của chúng có dạng **phân phối tiệm cận chuẩn**."

**Ba điều làm định lý này phi thường:**

1. **Không cần biết phân phối gốc.** Dữ liệu gốc có thể lệch, rời rạc, kỳ quái — trung bình vẫn chuẩn.
2. **Hội tụ khá nhanh.** Trong thực hành $n \ge 30$ thường là đủ (thấy ở mục 9).
3. **Nó giải thích vì sao phân phối chuẩn ở khắp nơi** — bất cứ đại lượng nào là tổng của nhiều
   ảnh hưởng nhỏ độc lập đều tiệm cận chuẩn (đã nhắc ở bài 7 mục 5).

⚠️ **Ba điều kiện dễ bị vi phạm trong thực tế:**

- **Độc lập** — dữ liệu chuỗi thời gian (doanh thu tháng liên tiếp) thường tự tương quan.
- **Cùng phân phối** — gộp dữ liệu từ nhiều nguồn khác nhau.
- **"Không nhân tố nào lấn át"** — nếu một khách hàng chiếm 60% doanh thu thì tổng doanh thu
  **không** tiệm cận chuẩn, dù có nghìn khách hàng khác.

Điều kiện thứ ba là chỗ hay bị bỏ quên nhất, và cũng là chỗ dữ liệu kinh doanh hay vi phạm nhất
(quy luật 80/20).

### Thí dụ 4.1 (tr. 106) — ⚠️ có lỗi in

> Một quả đậu có trọng lượng trung bình 15 g, độ lệch chuẩn 3 g. Túi 100 quả đạt **loại A** nếu
> trọng lượng ít nhất 1,5 kg.
> a) Lấy ngẫu nhiên một túi, xác suất túi đó đạt loại A?
> b) Chọn ngẫu nhiên 40 túi, xác suất số túi loại A **không vượt quá 15**?

*Giải.* **a)** $S_{100} = X_1 + \cdots + X_{100}$. Theo CLT (4.6):

$$ES_{100} = 100 \times 15 = 1500 \text{ g} = 1{,}5 \text{ kg}, \qquad VS_{100} = 100 \times 3^2 = 900 \text{ g}^2$$

$$S_{100} \approx N(1500;\ 30^2)$$

Vì 1,5 kg **đúng bằng kỳ vọng** và phân phối chuẩn đối xứng:

$$P(S_{100} \ge 1500) = \mathbf{0{,}5}$$

**b)** $p = 0{,}5$ là xác suất một túi đạt loại A, nên số túi loại A $X \sim B(40; 0{,}5)$.
$np = 20 > 5$, áp (4.5) với $\sqrt{npq} = \sqrt{10} \approx 3{,}1623$:

$$
P(X \le 15) \approx \phi\!\left(\frac{15-20}{\sqrt{10}}\right) - \phi\!\left(\frac{0-20}{\sqrt{10}}\right)
= \phi(6{,}32) - \phi(1{,}58) = 0{,}5 - 0{,}443 = \mathbf{0{,}057}
$$

⚠️ **Đính chính.** Sách in kết quả cuối là **0,017**. Nhưng $0{,}5 - 0{,}443 = \mathbf{0{,}057}$ —
lỗi ở **phép trừ cuối cùng**. Đã đối chiếu bản quét gốc trang 107: dòng in nguyên văn là
`≈ φ(6,32) − φ(1,58) = 0,5 − 0,443 = 0,017`. Mọi bước trước đó đều đúng.

Kiểm bằng máy: giá trị nhị thức đúng $P(X \le 15) = \mathbf{0{,}0769}$.

| Cách tính                                           |    Kết quả |
| --------------------------------------------------- | ---------: |
| Nhị thức đúng                                       | **0,0769** |
| Xấp xỉ chuẩn, không hiệu chỉnh                      |     0,0569 |
| Xấp xỉ chuẩn, **có hiệu chỉnh** $+0{,}5$ (mốc 15,5) | **0,0774** |
| ~~Sách in~~                                         |  ~~0,017~~ |

Hiệu chỉnh liên tục (bài 3 mục 8, bài 7 mục 7) đưa sai số từ 0,020 xuống **0,0005**.

### 💼 Góc QTKD — CLT là thứ khiến khảo sát 1.000 người hoạt động

Giá trị đơn hàng của một shop **rất lệch phải**: 80% đơn 200k, 15% đơn 1 triệu, 5% đơn 10 triệu.

$$EX = 810\text{k}, \qquad \sigma = 2\,127\text{k}, \qquad \frac{\sigma}{EX} = 2{,}63$$

Một biến cực kỳ phân tán và **không hề chuẩn**. Nhưng theo CLT, **giá trị đơn trung bình** của $n$ đơn:

| Số đơn $n$ | $\sigma$ của trung bình |
| ---------: | ----------------------: |
|          1 |                  2.127k |
|         30 |                    388k |
|        300 |                    123k |
|      3.000 |                     39k |

Với 3.000 đơn/tháng, giá trị đơn trung bình dao động chỉ $\pm 39$k quanh 810k — **dự báo được**,
dù từng đơn thì hoàn toàn không.

⭐ **Đây là lý do bài 11 (khoảng tin cậy) và bài 12 (kiểm định) dùng được cho mọi loại dữ liệu
kinh doanh**, kể cả dữ liệu lệch nặng. Ta không cần dữ liệu gốc chuẩn — chỉ cần **trung bình mẫu**
chuẩn, và CLT bảo đảm điều đó.

---

## 8. 📚 Vì sao hai định lý này là nền của cả phần thống kê

Giáo trình khẳng định điều này ở tr. 103 nhưng không giải thích cụ thể. Đây là phần bổ sung.

**Bài toán trung tâm của thống kê:** không biết $a$ (kỳ vọng thật của tổng thể), chỉ có $n$ quan sát.
Làm sao nói được gì về $a$?

```
   BƯỚC 1 — Đo được không?
       Luật số lớn:  X̄ ──xs──► a
       ⟹ CÓ. Trung bình mẫu tiến về kỳ vọng thật.
       ⟹ Bài 11: dùng X̄ làm ƯỚC LƯỢNG ĐIỂM cho a.

   BƯỚC 2 — Sai bao nhiêu?
       Luật căn bậc hai (bài 6):  σ(X̄) = σ/√n
       ⟹ Biết ĐỘ LỚN sai số, nhưng chưa biết PHÂN PHỐI của nó.

   BƯỚC 3 — Sai theo phân phối nào?
       CLT:  (X̄ − a)/(σ/√n) ──L──► N(0;1)
       ⟹ Sai số phân phối CHUẨN. Tra bảng được.
       ⟹ Bài 11: KHOẢNG TIN CẬY  X̄ ± z·σ/√n
       ⟹ Bài 12: KIỂM ĐỊNH GIẢ THUYẾT

   BƯỚC 4 — Nếu không biết cả σ?
       Thay σ bằng s (độ lệch chuẩn mẫu) → phân phối STUDENT t(n−1)
       ⟹ Bài 11 và 12, trường hợp σ chưa biết.
```

**Bảng đối chiếu ba định lý:**

|             | Chebyshev         | Luật số lớn                  | Giới hạn trung tâm                    |
| ----------- | ------------------ | ---------------------------- | ------------------------------------- |
| Nói về      | một biến           | trung bình mẫu               | trung bình mẫu                        |
| Kết luận    | chặn xác suất lệch | tiến về **một số**           | tiến về **một phân phối**             |
| Kiểu hội tụ | —                  | theo xác suất                | theo luật                             |
| Cần gì      | $\sigma^2$ hữu hạn | độc lập, $\sigma^2$ chặn đều | độc lập, **cùng phân phối**           |
| Cho ra      | chặn lỏng          | *"đo được"*                  | *"tính được sai số"*                  |
| Dùng ở      | quản trị rủi ro    | ước lượng điểm (bài 11)      | khoảng tin cậy, kiểm định (bài 11–14) |

**Ba câu tóm tắt cả bài:**

1. **Chebyshev:** dù phân phối thế nào, không lệch quá xa được.
2. **Luật số lớn:** đo nhiều lần rồi lấy trung bình thì ra đúng.
3. **CLT:** sai số của trung bình đó phân phối chuẩn, nên đo được luôn cả độ tin cậy.

---

## 9. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-09-luat-so-lon.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**. Chạy khoảng 7 giây (có mô phỏng).
> Mọi mô phỏng dùng **seed cố định** nên chạy lại ra kết quả y hệt.

```python
"""Bài 9 — Hàm của biến ngẫu nhiên, luật số lớn và định lý giới hạn trung tâm."""

import math
import random
from fractions import Fraction as F
from statistics import NormalDist

Z = NormalDist()
laplace = lambda x: Z.cdf(x) - 0.5      # ham Laplace, tich phan TU 0


def E(dist, g=lambda v: v):
    return sum(g(v) * p for v, p in dist.items())


def transform(dist, g):
    """Luat phan phoi cua g(X) — gop cac gia tri trung nhau."""
    out = {}
    for x, p in dist.items():
        out[g(x)] = out.get(g(x), 0) + p
    return dict(sorted(out.items()))


# ─────────────────────────────────────────────────────────────
# 1. HÀM CỦA MỘT BIẾN — Thí dụ 3.1 (tr. 96), Z = X^2
# ─────────────────────────────────────────────────────────────
X = {-2: F(1, 10), -1: F(2, 10), 0: F(3, 10), 1: F(2, 10), 2: F(2, 10)}
assert sum(X.values()) == 1
Zsq = transform(X, lambda x: x * x)
print("THI DU 3.1 — Z = X^2")
print("  Bang cua Z:", {k: float(v) for k, v in Zsq.items()},
      "  (sach: 0,3 / 0,4 / 0,3)")
print("  EZ tu bang cua Z    =", E(Zsq), "=", float(E(Zsq)), "  (sach: 1,6)")
print("  EZ tu bang cua X    =", E(X, lambda x: x * x),
      "  <- KHONG can lap bang cua Z (tinh chat (v) bai 6)")
assert E(Zsq) == E(X, lambda x: x * x)

# ─────────────────────────────────────────────────────────────
# 2. TỔNG HAI BIẾN RỜI RẠC — Thí dụ 3.3 (tr. 99)
# ─────────────────────────────────────────────────────────────
J = {(1, 2): F(0), (1, 3): F(15, 100), (1, 4): F(5, 100),
     (2, 2): F(20, 100), (2, 3): F(10, 100), (2, 4): F(0),
     (3, 2): F(25, 100), (3, 3): F(5, 100), (3, 4): F(20, 100)}
assert sum(J.values()) == 1
Zsum = {}
for (x, y), p in J.items():
    Zsum[x + y] = Zsum.get(x + y, 0) + p
print()
print("THI DU 3.3 — luat phan phoi cua Z = X + Y")
for z, p in sorted(Zsum.items()):
    print(f"  P(Z={z}) = {float(p):.2f}")
print("  Tong =", sum(Zsum.values()), "  (sach: 0 / 0,35 / 0,40 / 0,05 / 0,20)")

# ─────────────────────────────────────────────────────────────
# 3. TỔNG HAI POISSON VẪN LÀ POISSON — Thí dụ 3.4 (tr. 100)
# ─────────────────────────────────────────────────────────────
def poisson(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)


print()
LAM, MU = 2.0, 3.0
print(f"THI DU 3.4 — X ~ P({LAM}), Y ~ P({MU}) doc lap  ->  X+Y ~ P({LAM + MU})?")
print(f"{'z':>4}{'tich chap':>14}{'P(lam+mu) truc tiep':>24}")
for z in range(6):
    conv = sum(poisson(k, LAM) * poisson(z - k, MU) for k in range(z + 1))
    direct = poisson(z, LAM + MU)
    assert math.isclose(conv, direct)
    print(f"{z:>4}{conv:>14.6f}{direct:>24.6f}")
print("  Khop hoan toan -> tinh CONG DUOC cua Poisson")

# ─────────────────────────────────────────────────────────────
# 4. TỔNG HAI BIẾN ĐỀU = PHÂN PHỐI TAM GIÁC — Thí dụ 3.5 (tr. 101)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 3.5 — X, Y doc lap ~ U([0;1])  ->  Z = X+Y co phan phoi TAM GIAC")
phi = lambda z: z if 0 <= z <= 1 else (2 - z if 1 < z <= 2 else 0.0)
rng = random.Random(2026)
NSIM = 400_000
hist = {}
for _ in range(NSIM):
    z = rng.random() + rng.random()
    hist[round(z, 1)] = hist.get(round(z, 1), 0) + 1
print(f"{'z':>6}{'mat do ly thuyet':>20}{'mo phong (seed 2026)':>24}")
for z10 in range(0, 21, 4):
    z = z10 / 10
    emp = hist.get(round(z, 1), 0) / NSIM / 0.1
    print(f"{z:>6.1f}{phi(z):>20.4f}{emp:>24.4f}")
print("  Do thi hinh TAM GIAC: dinh tai z = 1, day tu 0 den 2")

# ─────────────────────────────────────────────────────────────
# 5. BẤT ĐẲNG THỨC CHEBYSHEV (4.7) vs giá trị thật
# ─────────────────────────────────────────────────────────────
print()
print("BAT DANG THUC CHEBYSHEV:  P(|X - a| >= eps) <= sigma^2 / eps^2")
print(f"{'eps':>8}{'chan Chebyshev':>18}{'that (neu X chuan)':>22}{'chenh':>10}")
for k in [1, 2, 3, 4]:
    bound = min(1.0, 1 / k**2)
    real = 2 * (1 - Z.cdf(k))
    print(f"{str(k) + ' sigma':>8}{bound:>18.4f}{real:>22.6f}{bound - real:>10.4f}")
print("  ⚠ Chan rat LONG (eps = 1 sigma cho chan = 1, vo nghia)")
print("  ⭐ Nhung dung cho MOI phan phoi, khong can biet dang phan phoi")

# ─────────────────────────────────────────────────────────────
# 6. LUẬT SỐ LỚN BERNOULLI (4.11) — tần suất hội tụ về p
# ─────────────────────────────────────────────────────────────
print()
print("LUAT SO LON BERNOULLI — tan suat m/n hoi tu ve p = 0,3")
P_TRUE = 0.3
rng = random.Random(7)
hit = 0
print(f"{'n':>9}{'m/n':>10}{'|m/n - p|':>12}{'chan Chebyshev':>18}")
for n in range(1, 200_001):
    hit += rng.random() < P_TRUE
    if n in (100, 1_000, 10_000, 100_000, 200_000):
        f_ = hit / n
        # P(|m/n - p| >= 0,01) <= p(1-p)/(n * 0,01^2)
        bound = min(1.0, P_TRUE * (1 - P_TRUE) / (n * 0.01**2))
        print(f"{n:>9}{f_:>10.4f}{abs(f_ - P_TRUE):>12.4f}{bound:>18.4f}")
print("  => Day chinh la co so cho DINH NGHIA THONG KE cua xac suat (bai 2)")

# ─────────────────────────────────────────────────────────────
# 7. ĐỊNH LÝ GIỚI HẠN TRUNG TÂM — Thí dụ 4.1 (tr. 106), túi đậu
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.1 — 100 qua dau, moi qua EX = 15g, sigma = 3g")
n_dau, m_dau, s_dau = 100, 15, 3
ES = n_dau * m_dau
VS = n_dau * s_dau**2
print(f"  E(S100) = {ES} g = {ES / 1000} kg   V(S100) = {VS} g^2"
      f"   sigma = {math.sqrt(VS)} g")
print(f"  a) P(S100 >= 1500 g) = {1 - Z.cdf(0):.1f}   (doi xung qua ky vong)")
n_tui, p_tui = 40, 0.5
np_, sd_ = n_tui * p_tui, math.sqrt(n_tui * p_tui * (1 - p_tui))
b = laplace((15 - np_) / sd_) - laplace((0 - np_) / sd_)
print(f"  b) X ~ B(40; 0,5), np = {np_}, can(npq) = {sd_:.4f}")
print(f"     P(X <= 15) = phi({(15 - np_) / sd_:.2f}) - phi({(0 - np_) / sd_:.2f})"
      f" = {b:.4f}   (sach: 0,017)")
exact_b = sum(math.comb(n_tui, k) * 0.5**n_tui for k in range(16))
print(f"     Nhi thuc dung P(X <= 15) = {exact_b:.4f}"
      f"   -> xap xi lech {abs(b - exact_b):.4f}")

# ─────────────────────────────────────────────────────────────
# 8. 💼 GÓC QTKD — CLT hoạt động kể cả khi biến gốc RẤT không chuẩn
# ─────────────────────────────────────────────────────────────
print()
print("💼 GOC QTKD — gia tri don hang RAT lech phai, nhung TONG thang van chuan")
# Bien goc: 80% don 200k, 15% don 1tr, 5% don 10tr  (rat lech phai)
order = {200: F(80, 100), 1_000: F(15, 100), 10_000: F(5, 100)}   # nghin dong
mu = float(E(order))
var = float(E(order, lambda v: v * v)) - mu**2
print(f"  Bien goc: EX = {mu:.0f}k, sigma = {math.sqrt(var):.0f}k"
      f"  -> sigma/EX = {math.sqrt(var) / mu:.2f} (rat phan tan)")
vals = list(order.keys())
weights = [float(p) for p in order.values()]
rng = random.Random(2026)
print(f"{'so don n':>10}{'trung binh mo phong':>22}{'sigma mo phong':>18}"
      f"{'sigma/can(n) ly thuyet':>26}")
for n in [1, 30, 300, 3000]:
    sums = []
    for _ in range(4000):
        s = sum(rng.choices(vals, weights)[0] for _ in range(n))
        sums.append(s / n)
    m_ = sum(sums) / len(sums)
    v_ = sum((s - m_) ** 2 for s in sums) / (len(sums) - 1)
    print(f"{n:>10}{m_:>22.1f}{math.sqrt(v_):>18.1f}"
          f"{math.sqrt(var / n):>26.1f}")
print("  => sigma cua trung binh giam dung theo 1/can(n) (luat can bac hai, bai 6)")
print("  => Do la ly do khoang tin cay o bai 11 dung duoc cho MOI loai du lieu")
```

Kết quả chạy thật:

```
THI DU 3.1 — Z = X^2
  Bang cua Z: {0: 0.3, 1: 0.4, 4: 0.3}   (sach: 0,3 / 0,4 / 0,3)
  EZ tu bang cua Z    = 8/5 = 1.6   (sach: 1,6)
  EZ tu bang cua X    = 8/5   <- KHONG can lap bang cua Z (tinh chat (v) bai 6)

THI DU 3.3 — luat phan phoi cua Z = X + Y
  P(Z=3) = 0.00
  P(Z=4) = 0.35
  P(Z=5) = 0.40
  P(Z=6) = 0.05
  P(Z=7) = 0.20
  Tong = 1   (sach: 0 / 0,35 / 0,40 / 0,05 / 0,20)

THI DU 3.4 — X ~ P(2.0), Y ~ P(3.0) doc lap  ->  X+Y ~ P(5.0)?
   z     tich chap     P(lam+mu) truc tiep
   0      0.006738                0.006738
   1      0.033690                0.033690
   2      0.084224                0.084224
   3      0.140374                0.140374
   4      0.175467                0.175467
   5      0.175467                0.175467
  Khop hoan toan -> tinh CONG DUOC cua Poisson

THI DU 3.5 — X, Y doc lap ~ U([0;1])  ->  Z = X+Y co phan phoi TAM GIAC
     z    mat do ly thuyet    mo phong (seed 2026)
   0.0              0.0000                  0.0133
   0.4              0.4000                  0.4011
   0.8              0.8000                  0.7996
   1.2              0.8000                  0.8046
   1.6              0.4000                  0.3947
   2.0              0.0000                  0.0117
  Do thi hinh TAM GIAC: dinh tai z = 1, day tu 0 den 2

BAT DANG THUC CHEBYSHEV:  P(|X - a| >= eps) <= sigma^2 / eps^2
     eps    chan Chebyshev    that (neu X chuan)     chenh
 1 sigma            1.0000              0.317311    0.6827
 2 sigma            0.2500              0.045500    0.2045
 3 sigma            0.1111              0.002700    0.1084
 4 sigma            0.0625              0.000063    0.0624
  ⚠ Chan rat LONG (eps = 1 sigma cho chan = 1, vo nghia)
  ⭐ Nhung dung cho MOI phan phoi, khong can biet dang phan phoi

LUAT SO LON BERNOULLI — tan suat m/n hoi tu ve p = 0,3
        n       m/n   |m/n - p|    chan Chebyshev
      100    0.3300      0.0300            1.0000
     1000    0.3360      0.0360            1.0000
    10000    0.3020      0.0020            0.2100
   100000    0.3016      0.0016            0.0210
   200000    0.3010      0.0010            0.0105
  => Day chinh la co so cho DINH NGHIA THONG KE cua xac suat (bai 2)

THI DU 4.1 — 100 qua dau, moi qua EX = 15g, sigma = 3g
  E(S100) = 1500 g = 1.5 kg   V(S100) = 900 g^2   sigma = 30.0 g
  a) P(S100 >= 1500 g) = 0.5   (doi xung qua ky vong)
  b) X ~ B(40; 0,5), np = 20.0, can(npq) = 3.1623
     P(X <= 15) = phi(-1.58) - phi(-6.32) = 0.0569   (sach: 0,017)
     Nhi thuc dung P(X <= 15) = 0.0769   -> xap xi lech 0.0200

💼 GOC QTKD — gia tri don hang RAT lech phai, nhung TONG thang van chuan
  Bien goc: EX = 810k, sigma = 2127k  -> sigma/EX = 2.63 (rat phan tan)
  so don n   trung binh mo phong    sigma mo phong    sigma/can(n) ly thuyet
         1                 792.0            2103.3                    2127.4
        30                 804.3             380.6                     388.4
       300                 806.3             123.9                     122.8
      3000                 808.9              38.2                      38.8
  => sigma cua trung binh giam dung theo 1/can(n) (luat can bac hai, bai 6)
  => Do la ly do khoang tin cay o bai 11 dung duoc cho MOI loai du lieu
```

Năm điểm đáng để ý:

1. **Thí dụ 3.5**: cột mô phỏng khớp cột lý thuyết tới 2–3 chữ số ở giữa (`0.4011` vs `0.4000`).
   Hai đầu lệch (`0.0133` vs `0`) là do làm tròn `round(z, 1)` gom cả nửa ô ngoài biên — không phải
   lỗi lý thuyết.
2. **Bảng Chebyshev**: cột "chênh" cho thấy chặn lỏng đến mức nào. Ở $1\sigma$ chặn nói *"≤ 100%"* —
   tức không nói gì cả.
3. **Luật số lớn**: `|m/n − p|` giảm từ 0,030 xuống 0,001 khi $n$ tăng từ 100 lên 200.000.
   Nhưng **không đơn điệu** — ở $n = 1000$ còn tệ hơn $n = 100$. Đúng như bài 2 mục 8 đã cảnh báo:
   hội tụ **theo xác suất**, không phải hội tụ từng bước.
4. **Thí dụ 4.1b**: máy tính ra `0.0569`, sách in `0,017`. Bằng chứng cho đính chính ở mục 7.
   Và giá trị đúng `0.0769` cho thấy xấp xỉ không hiệu chỉnh lệch 0,02 — nên dùng hiệu chỉnh.
5. **Góc QTKD**: cột "sigma mô phỏng" và "sigma/√n lý thuyết" gần như trùng khít
   (`380.6` vs `388.4`, `38.2` vs `38.8`) — **CLT hoạt động đúng dù biến gốc chỉ có 3 giá trị
   và lệch phải kinh khủng**. Đây là điều đáng kinh ngạc nhất của định lý này.

---

## 10. Tự thử

1. Ở thí dụ 3.1, đổi hàm thành $Z = |X|$ rồi $Z = X^3$. Hàm nào cần gộp xác suất, hàm nào không?
   Vì sao?
2. Ở thí dụ 3.4, thêm biến thứ ba $W \sim P(1{,}5)$ và kiểm $X + Y + W \sim P(6{,}5)$.
   Tính cộng được có mở rộng cho ba biến không?
3. Sửa mục 4 để cộng **ba** biến đều $\mathcal{U}([0;1])$ thay vì hai. Đồ thị còn là tam giác không?
   In histogram 20 ô và quan sát — nó giống hình gì?
4. Trong bảng Chebyshev, thay `Z.cdf(k)` bằng phân phối **mũ** $\mathcal{E}(1)$ (kỳ vọng 1, $\sigma$ = 1).
   Chặn Chebyshev còn đúng không? Chênh lệch so với phân phối chuẩn thế nào?
5. Ở mục 6, đổi `P_TRUE` thành 0,01 (sự kiện hiếm). Cần $n$ bằng bao nhiêu để $|m/n - p| < 0{,}001$?
   So với trường hợp $p = 0{,}3$ — hội tụ nhanh hơn hay chậm hơn?
6. Sửa thí dụ 4.1b để **có hiệu chỉnh liên tục**: đổi `(15 - np_)` thành `(15.5 - np_)`.
   Kết quả có gần `0.0769` hơn không? Lệch bao nhiêu?
7. Ở Góc QTKD, đổi phân phối gốc thành cực đoan hơn: 99% đơn 100k, 1% đơn 100 triệu.
   Với $n = 30$, trung bình mẫu đã "chuẩn" chưa? Cần $n$ khoảng bao nhiêu?
   (Đây chính là điều kiện *"không nhân tố nào lấn át"* ở mục 7.)

---

## 11. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)     | Tiếng Anh                         | Ghi chú                       |
| --------------------------- | --------------------------------- | ----------------------------- |
| Tích chập                   | Convolution                       | $f_1 * f_2$, luật của $X+Y$   |
| Phân phối tam giác, Simpson | Triangular / Simpson distribution | tổng hai biến đều             |
| Hội tụ hầu chắc chắn        | Almost sure convergence           | mạnh nhất                     |
| Hội tụ theo xác suất        | Convergence in probability        | dùng cho luật số lớn          |
| Hội tụ theo luật            | Convergence in distribution       | dùng cho CLT; yếu nhất        |
| Hội tụ trung bình cấp $k$   | Convergence in $k$-th mean        | $k=2$: trung bình bình phương |
| Bất đẳng thức Chebyshev    | Chebyshev's inequality            | (4.7)                         |
| Luật số lớn                 | Law of large numbers (LLN)        | (4.9), (4.11)                 |
| Luật số lớn Bernoulli       | Bernoulli's LLN                   | tần suất → xác suất           |
| Định lý giới hạn trung tâm  | Central limit theorem (CLT)       | (4.6)                         |
| Lindeberg – Lévy          | Lindeberg–Lévy                    | tác giả CLT dạng cổ điển      |
| de Moivre – Laplace         | de Moivre–Laplace                 | CLT cho nhị thức              |
| Phương sai bị chặn đều      | Uniformly bounded variance        | $VX_i \le C$                  |
| Đa dạng hoá                 | Diversification                   | 💼 mục 3                      |

---

## 12. Câu hỏi tự kiểm tra

1. Vì sao trong công thức đổi biến (3.1) phải có thừa số $|\psi'(z)|$? Điều gì xảy ra nếu bỏ nó?
2. Hàm tuyến tính của biến chuẩn vẫn chuẩn. Còn $X^2$ của biến chuẩn thì sao?
   (Gợi ý: bài 7 mục 8, định nghĩa $\chi^2$.)
3. Nêu điều kiện để $V(X+Y) = VX + VY$. Điều kiện này mạnh hơn hay yếu hơn "độc lập"?
4. Bất đẳng thức Chebyshev với $\varepsilon = 0{,}5\sigma$ cho chặn bằng bao nhiêu?
   Kết quả đó có ích không? Vì sao?
5. Phát biểu bằng lời sự khác nhau giữa luật số lớn và định lý giới hạn trung tâm.
   Vì sao cần **cả hai**, không thể chỉ một?
6. Doanh thu ngày của một chuỗi cửa hàng có $EX = 50$ triệu, $\sigma = 12$ triệu, phân phối
   **không chuẩn** (lệch phải). Doanh thu trung bình của 36 ngày:
   a) Kỳ vọng và $\sigma$? b) Có được coi là chuẩn không, vì sao?
   c) $P(\text{trung bình } > 54 \text{ triệu})$?
7. Vì sao công ty bảo hiểm có lãi ổn định trong khi từng hợp đồng là canh bạc?
   Nếu công ty chỉ bán 10 hợp đồng thì sao?
8. Một quỹ đầu tư nói: *"danh mục 50 cổ phiếu nên rủi ro giảm theo $1/\sqrt{50}$."*
   Nêu hai lý do câu này có thể sai. (Gợi ý: mục 3 và mục 7.)
9. Bài 3 (tr. 110): tiến hành 3 thí nghiệm với xác suất thành công mỗi lần 0,7.
   Tìm luật phân phối đồng thời của $(X, Y)$ với $X$ = số thành công, $Y$ = số thất bại.
   Hai biến này có độc lập không? $\rho_{XY}$ bằng bao nhiêu?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 9 — LUẬT SỐ LỚN & GIỚI HẠN TRUNG TÂM      (Ch. III §3–4, tr.96–112) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  HÀM CỦA BIẾN NGẪU NHIÊN                                                 ║
║      rời rạc  Z = g(X)  → GỘP xác suất các x cho cùng z                  ║
║      liên tục φ(z) = f[ψ(z)]·|ψ'(z)|      ψ = hàm ngược của g            ║
║      ⭐ Y = aX + b của biến CHUẨN vẫn CHUẨN  → cơ sở của phép quy chuẩn  ║
║      tổng 2 biến: TÍCH CHẬP  φ(z) = ∫ f₁(x)f₂(z−x)dx                     ║
║      Poisson cộng được: P(λ) + P(μ) = P(λ+μ)                             ║
║      U([0;1]) + U([0;1]) = TAM GIÁC  ← manh nha của CLT                  ║
║                                                                          ║
║  📚 V(X+Y) = VX + VY + 2μ_XY                                             ║
║      → chỉ cần KHÔNG TƯƠNG QUAN, không cần độc lập                       ║
║      → μ < 0 làm giảm rủi ro tổng = ĐA DẠNG HOÁ danh mục                 ║
║                                                                          ║
║  BỐN KIỂU HỘI TỤ                                                         ║
║      h.c.c ┐                                                             ║
║            ├─► theo XÁC SUẤT ─► theo LUẬT   (yếu nhất, hay dùng nhất)    ║
║      tb.k  ┘      ↑                 ↑                                    ║
║                 LUẬT SỐ LỚN        CLT                                   ║
║      "tiến về MỘT SỐ"      "tiến về MỘT PHÂN PHỐI"                       ║
║                                                                          ║
║  CHEBYSHEV   P(|X − a| ≥ ε) ≤ σ²/ε²                                      ║
║      ⭐ đúng cho MỌI phân phối, chỉ cần σ² hữu hạn                       ║
║      ⚠ nhưng RẤT LỎNG: ε = 3σ cho ≤ 0,111, thật (chuẩn) là 0,0027        ║
║      ε ≤ σ → chặn ≥ 1 → vô nghĩa                                         ║
║                                                                          ║
║  LUẬT SỐ LỚN (Chebyshev)   X̄ ──xs──► a                                   ║
║      cần: độc lập, phương sai bị chặn đều                                ║
║      ⟹ ĐO NHIỀU LẦN RỒI LẤY TRUNG BÌNH THÌ RA ĐÚNG                      ║
║                                                                          ║
║  LUẬT SỐ LỚN BERNOULLI      m/n ──xs──► p                                ║
║      ⭐ đây là CHỨNG MINH cho định nghĩa thống kê của xác suất (bài 2)   ║
║                                                                          ║
║  ⭐⭐ ĐỊNH LÝ GIỚI HẠN TRUNG TÂM (Lindeberg – Lévy)                      ║
║      Xᵢ độc lập, CÙNG PHÂN PHỐI, EXᵢ = m, VXᵢ = σ²                       ║
║                                                                          ║
║           X̄ − m                                                          ║
║          ─────────  ──L──►  N(0;1)         ΣXᵢ ──L──► N(nm; nσ²)         ║
║           σ/√n                                                           ║
║                                                                          ║
║      KHÔNG CẦN biết phân phối gốc.  n ≥ 30 thường là đủ.                 ║
║      ⚠ ba điều kiện dễ vi phạm:                                          ║
║        độc lập (chuỗi thời gian) | cùng phân phối | KHÔNG AI LẤN ÁT      ║
║                                                                          ║
║  📚 BỐN BƯỚC DẪN TỚI PHẦN THỐNG KÊ                                       ║
║      1. Luật số lớn  → X̄ đo được a          (ước lượng điểm, bài 11)     ║
║      2. Luật căn √n  → σ(X̄) = σ/√n          (độ lớn sai số, bài 6)       ║
║      3. CLT          → sai số phân phối CHUẨN (khoảng tin cậy, bài 11)   ║
║      4. σ chưa biết  → thay bằng s → Student t(n−1)      (bài 11, 12)    ║
║                                                                          ║
║  ⚠ ĐÍNH CHÍNH tr.107 thí dụ 4.1b: 0,5 − 0,443 = 0,057 (sách in 0,017)    ║
║                                                                          ║
║  💼 QTKD  luật số lớn CHỈ giúp bên LẶP NHIỀU LẦN                         ║
║          (bảo hiểm, sòng bạc, sàn TMĐT) — không giúp quyết định 1 lần    ║
║          CLT: giá trị đơn hàng lệch nặng nhưng TRUNG BÌNH vẫn chuẩn      ║
║          ⟹ khảo sát 1.000 người hoạt động được là nhờ CLT               ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương III §3–§4, tr. 96–112.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Đính chính thí dụ 4.1b (tr. 107): đã đối chiếu bản quét gốc. Sách in
  `≈ φ(6,32) − φ(1,58) = 0,5 − 0,443 = 0,017`; phép trừ đúng cho **0,057**.
  Giá trị nhị thức chính xác là 0,0769.
- Mục 8 (bốn bước dẫn tới phần thống kê) và công thức $V(X+Y) = VX+VY+2\mu_{XY}$ ở mục 3:
  kiến thức bổ sung. Giáo trình có hứa "sẽ giảm nhẹ điều kiện độc lập" ở tr. 53 nhưng không viết
  công thức đầy đủ.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 8 — Biến ngẫu nhiên hai chiều và hệ số tương quan](bai_08_bien_ngau_nhien_hai_chieu_va_tuong_quan.md) ·
Bài sau: Bài 10 — Mẫu và thống kê mô tả
