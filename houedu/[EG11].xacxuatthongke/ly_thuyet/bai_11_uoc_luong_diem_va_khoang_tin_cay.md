# Bài 11 — Ước lượng điểm và khoảng tin cậy

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương IV §3–§4**, tr. 133–157.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính hai lỗi in**: thí dụ 4.2 (tr. 143) và thí dụ 4.3 (tr. 144).
> 📌 **Cần đọc trước:** [Bài 7](bai_07_cac_phan_phoi_thong_dung.md) · [Bài 9](bai_09_luat_so_lon_va_dinh_ly_gioi_han_trung_tam.md) · [Bài 10](bai_10_mau_va_thong_ke_mo_ta.md)

Bài 10 cho bạn **một con số**: $\overline{X} = 55{,}24$ triệu. Giáo trình nêu ngay vấn đề của nó (tr. 140):

> "Ước lượng điểm có một nhược điểm cơ bản là **không thể biết được độ chính xác** cũng như xác suất
> để ước lượng đó chính xác."

Bài này biến một con số thành **một khoảng kèm mức tin cậy**:

$$55{,}24 \ \longrightarrow \ (50{,}95;\ 59{,}53) \text{ với độ tin cậy } 95\%$$

Đó là bước biến thống kê từ mô tả thành **công cụ ra quyết định**.

## Mục lục

1. [Bài toán ước lượng tham số](#1-bài-toán-ước-lượng-tham-số)
2. [Ba tính chất của ước lượng điểm](#2-ba-tính-chất-của-ước-lượng-điểm)
3. [Ba phương pháp ước lượng](#3-ba-phương-pháp-ước-lượng)
4. [Ước lượng khoảng: nguyên lý chung](#4-ước-lượng-khoảng-nguyên-lý-chung)
5. [Bài toán 1: kỳ vọng khi đã biết sigma](#5-bài-toán-1-kỳ-vọng-khi-đã-biết-sigma)
6. [Bài toán 2: kỳ vọng khi chưa biết sigma](#6-bài-toán-2-kỳ-vọng-khi-chưa-biết-sigma)
7. [Bài toán 3: khoảng tin cậy cho tỷ lệ](#7-bài-toán-3-khoảng-tin-cậy-cho-tỷ-lệ)
8. [Bài toán 4: khoảng tin cậy cho phương sai](#8-bài-toán-4-khoảng-tin-cậy-cho-phương-sai)
9. [📚 95% nghĩa là gì và không nghĩa là gì](#9--95-nghĩa-là-gì-và-không-nghĩa-là-gì)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Bài toán ước lượng tham số

**Phát biểu tổng quát (tr. 133).** Cho biến ngẫu nhiên gốc $X$ có luật phân phối **đã biết dạng**
nhưng **chưa biết tham số** $\theta$. Xác định giá trị của $\theta$ dựa trên mẫu quan sát
$x_1, x_2, \dots, x_n$.

Giá trị tìm được, ký hiệu $\hat\theta$, gọi là **ước lượng** của $\theta$. Vì nó là **một số**,
gọi là **ước lượng điểm**.

⚠️ Chú ý $\hat\theta = \hat\theta(x_1, \dots, x_n)$ là **một hàm của mẫu**, tức là một **thống kê**
(bài 10 mục 4) — nên bản thân nó cũng là biến ngẫu nhiên.

Giáo trình nêu vấn đề đánh giá (tr. 133): *"để đánh giá một ước lượng là tốt hay không, ta phải
so sánh nó với giá trị $\theta$ thật, **nhưng $\theta$ chưa biết**."*

Giải pháp: đặt ra **tiêu chuẩn** cho $\hat\theta$ (mục 2), thay vì so trực tiếp.

**Hàm tổn thất.** Giáo trình dùng dạng bình phương (tr. 133): $L(g, \theta) = (g - \theta)^2$,
và mục tiêu là cực tiểu **hàm rủi ro** $R(g,\theta) = E[L(g,\theta)]$.

📚 Vì sao dùng bình phương? Giáo trình giải thích bằng khai triển Taylor (3.1): với giả thiết lồi,
liên tục và khả vi hai lần, mọi hàm tổn thất đều **xấp xỉ được bằng dạng bình phương** ở lân cận
$\theta$. Đây là cùng một lý do đã gặp ở bài 6 mục 3 (vì sao phương sai bình phương độ lệch).

---

## 2. Ba tính chất của ước lượng điểm

### 1. Không chệch (unbiased)

**Định nghĩa 1 (tr. 134).** $\hat\theta$ là **ước lượng không chệch** của $\theta$ nếu

$$E\hat\theta = \theta$$

Tức là $E(\hat\theta - \theta) = 0$: *"trung bình độ lệch của ước lượng so với giá trị thật bằng 0."*

Giáo trình đặt tên cho hai loại sai số (tr. 134):

|                           | Trung bình độ lệch | Tên                   |
| ------------------------- | ------------------ | --------------------- |
| Ước lượng **không chệch** | $= 0$              | **sai số ngẫu nhiên** |
| Ước lượng **chệch**       | $\ne 0$            | **sai số hệ thống**   |

⭐ **Bốn kết quả cần nhớ (tr. 135):**

$$
\begin{aligned}
&\overline{X} && \text{ước lượng không chệch của } && EX = a \\
&s^2 \ (\text{chia } n-1) && \text{ước lượng không chệch của } && VX = \sigma^2 \\
&f = m/n && \text{ước lượng không chệch của } && p \\
&\hat{S}^2 \ (\text{chia } n) && \textbf{ước lượng CHỆCH của } && \sigma^2
\end{aligned}
$$

Dòng cuối chính là lý do bài 10 mục 6 phải chia $n-1$.

⚠️ Giáo trình còn nêu một trường hợp tinh tế: nếu **biết trước** $a$, thì
$\frac1n\sum(x_i - a)^2$ **là** ước lượng không chệch của $\sigma^2$ — chia $n$, không phải $n-1$.
Chỉ khi phải ước lượng $a$ bằng $\overline{X}$ mới mất một bậc tự do.

💼 **Sai số hệ thống là thứ đáng sợ trong kinh doanh.** Sai số ngẫu nhiên tự triệt tiêu khi lấy
nhiều mẫu; sai số hệ thống thì **không bao giờ** — càng nhiều dữ liệu càng tự tin vào một con số sai.
Cân bị lệch 100 g thì cân một triệu lần vẫn lệch 100 g.

### 2. Vững (consistent)

**Định nghĩa 2 (tr. 135).** $\hat\theta$ là **ước lượng vững** nếu

$$\hat\theta(X_1, \dots, X_n) \xrightarrow{xs} \theta \quad (n \to \infty)$$

**Điều kiện đủ tiện dùng** (tr. 135): nếu $\lim E\hat\theta = \theta$ (tiệm cận không chệch)
và $\lim V\hat\theta = 0$ thì $\hat\theta$ vững.

$\overline{X}$, $s^2$, $\hat{S}^2$ và $f$ đều là ước lượng **vững**.

⭐ Chú ý $\hat{S}^2$ **chệch nhưng vẫn vững** — độ chệch $\frac{n-1}{n}\sigma^2 \to \sigma^2$.
Hai tính chất độc lập với nhau.

### 3. Hiệu quả (efficient)

**Định nghĩa 3 (tr. 135).** $\hat\theta$ là **ước lượng hiệu quả** nếu nó **không chệch** và có
**phương sai bé nhất** trong lớp các ước lượng không chệch.

**Giới hạn Cramér – Rao (3.2), tr. 135:**

$$V\hat\theta \ge \frac{1}{n\,E\!\left[\left(\dfrac{\partial \ln f(x,\theta)}{\partial \theta}\right)^{\!2}\right]}$$

Mọi ước lượng không chệch đều có phương sai **không nhỏ hơn** vế phải. Nghịch đảo của mẫu số gọi là
**lượng thông tin Fisher** của mẫu.

**Thí dụ 3.1 (tr. 136).** Nếu $X \sim N(a; \sigma^2)$ thì $\overline{X}$ là ước lượng **hiệu quả**
của $a$ — nó đạt đúng giới hạn Cramér – Rao $\sigma^2/n$.

Tương tự, tần suất mẫu $f$ là ước lượng hiệu quả của $p$ khi $X$ có phân phối Bernoulli.

### 📚 Ba tính chất, ba câu hỏi khác nhau

```
   KHÔNG CHỆCH  "Có nhắm đúng tâm không?"        → E θ̂ = θ
   VỮNG         "Càng nhiều dữ liệu càng đúng?"  → θ̂ → θ khi n → ∞
   HIỆU QUẢ     "Có phải cách chụm nhất không?"  → V θ̂ nhỏ nhất
```

```
   không chệch + hiệu quả      không chệch, kém hiệu quả    CHỆCH
        ●●●                          ●    ●                  ●●●
       ●●⊕●●         vs            ●  ⊕     ●        vs     ●●●   ⊕
        ●●●                        ●     ●   ●              ●●●
                                                        (chụm nhưng lệch tâm)
   ⊕ = giá trị thật θ   ● = các ước lượng từ những mẫu khác nhau
```

⚠️ Chụm mà lệch tâm (hình phải) là tình huống **nguy hiểm nhất**: bạn rất tự tin vào một con số sai.

---

## 3. Ba phương pháp ước lượng

### 1. Dùng các đặc trưng mẫu

Cách đơn giản nhất: dùng thẳng $\overline{X}$, $s^2$, $s$ như ở bài 10.

### 2. Phương pháp mômen

**Ý tưởng (tr. 137):** các mômen **mẫu** hội tụ hầu chắc chắn về các mômen **lý thuyết**. Vậy hãy
đặt chúng bằng nhau rồi giải hệ.

$$m_j(\theta) = m_j(e, n), \qquad j = 1, \dots, k$$

**Thí dụ 3.2 (tr. 137).** $X \sim \gamma(r, \lambda)$. Từ bài 7: $EX = r/\lambda$, $VX = r/\lambda^2$.
Đặt bằng $\overline{X}$ và $\hat{S}^2$:

$$\frac{r}{\lambda} = \overline{X}, \qquad \frac{r}{\lambda^2} = \hat{S}^2
\ \Longrightarrow \ \hat{r} = \frac{(\overline{X})^2}{\hat{S}^2}, \quad \hat\lambda = \frac{\overline{X}}{\hat{S}^2}$$

**Ưu:** dễ, luôn giải được. **Nhược:** thường kém hiệu quả hơn phương pháp thứ ba.

### 3. Phương pháp hợp lý nhất (maximum likelihood)

**Nguyên lý (tr. 137):** tìm $\theta$ sao cho **xác suất thu được chính các quan sát đó là lớn nhất**.

**Hàm hợp lý** (3.3):

$$L(x, \theta) = \prod_{i=1}^{n} f(x_i, \theta)$$

$\hat\theta$ là **ước lượng hợp lý nhất** nếu $L(x, \hat\theta) \ge L(x, \theta)$ với mọi $\theta$ (3.4).

Trong thực hành, giải **phương trình hợp lý nhất** (3.5) — lấy log trước cho biến tích thành tổng:

$$\frac{\partial \ln L(x, \theta)}{\partial \theta} = 0, \qquad
\text{kiểm điều kiện đủ } \frac{\partial^2 \ln L}{\partial\theta^2}\bigg|_{\theta = \hat\theta} < 0$$

⚠️ Giáo trình cảnh báo thẳng (tr. 138): hàm hợp lý *"không là hàm lồi và tất nhiên thường phi tuyến.
**Không có lý do nào để đảm bảo** cho $\hat\theta$... là duy nhất, hoặc là không chệch."*

Nhưng: *"nếu phương trình (3.5) có **nghiệm duy nhất** thì khi đó **không cần** kiểm tra điều kiện đủ."*

**Thí dụ 3.3 (tr. 138).** $X \sim P(\lambda)$ (Poisson). Giải phương trình hợp lý nhất được:

$$\hat\lambda = \overline{X}$$

**Thí dụ 3.4 (tr. 139).** $X \sim N(a; \sigma^2)$. Giải hệ hai phương trình được:

$$\hat{a} = \overline{X}, \qquad \hat\sigma^2 = \frac1n\sum(x_i - \overline{X})^2 = \hat{S}^2$$

⚠️ **Chú ý điều thú vị ở đây:** ước lượng hợp lý nhất của $\sigma^2$ chia cho $n$ — tức là
**$\hat{S}^2$, ước lượng CHỆCH!** Phương pháp hợp lý nhất không bảo đảm không chệch.

Đây là một đánh đổi thật: hợp lý nhất tối ưu theo tiêu chí "xác suất quan sát lớn nhất", không phải
tiêu chí "không chệch". Trong thực hành người ta vẫn dùng $s^2$ (chia $n-1$).

💼 Phương pháp hợp lý nhất là nền của **hầu hết mọi mô hình thống kê hiện đại**: hồi quy logistic,
mô hình sinh tồn, mô hình hỗn hợp. Khi phần mềm báo "log-likelihood", đó chính là $\ln L$ ở đây.

---

## 4. Ước lượng khoảng: nguyên lý chung

Giáo trình mô tả rất rõ ưu điểm (tr. 140):

> "Một khoảng ước lượng **vẫn có thể sai**, giống như mọi ước lượng khác, nhưng khác với ước lượng
> điểm, **xác suất sai lầm có thể biết** và trong chừng mực nào đó có thể **hy vọng kiểm soát được**."

Và lưu ý: *"ước lượng khoảng sẽ được xây dựng **xung quanh ước lượng điểm**"* — hai cái bổ sung nhau,
không thay thế nhau.

### Định nghĩa

Đặt $1 - \alpha = \gamma$ là **độ tin cậy**. Tìm $\theta_1$, $\theta_2$ sao cho

$$P(\theta_1 < \theta < \theta_2) = 1 - \alpha \tag{4.1}$$

Khoảng $(\theta_1, \theta_2)$ là **khoảng tin cậy** với độ tin cậy $1-\alpha$; $\theta_2 - \theta_1$
là **độ dài** của khoảng.

### ⭐ Quy trình chung — bốn bước, dùng cho cả bốn bài toán

Giáo trình nêu quy tắc (tr. 140–141):

```
   B1. Tìm một THỐNG KÊ G = G(x₁,...,xₙ, θ)
       sao cho PHÂN PHỐI của G xác định hoàn toàn — KHÔNG còn chứa θ.
       (thống kê G vẫn phụ thuộc θ, nhưng phân phối của nó thì không)

   B2. Với 1−α cho trước, chọn α₁ + α₂ = α, tìm hai phân vị g_α₁, g_{1−α₂}:
           P(G < g_α₁) = α₁        P(G > g_{1−α₂}) = α₂

   B3. Khi đó   P(g_α₁ < G < g_{1−α₂}) = 1 − α₁ − α₂ = 1 − α

   B4. Biến đổi TƯƠNG ĐƯƠNG bất đẳng thức ở B3 về dạng  θ₁ < θ < θ₂
```

**Bước 1 là bước tinh tế nhất.** Bốn thống kê $G$ cho bốn bài toán chính là bốn công thức (2.13)–(2.16)
đã học ở bài 10 mục 7:

| Bài toán                       | Thống kê $G$                                     | Phân phối        |
| ------------------------------ | ------------------------------------------------ | ---------------- |
| 1. Kỳ vọng, biết $\sigma$      | $Z = \dfrac{\overline{X} - a}{\sigma_0}\sqrt{n}$ | $N(0;1)$         |
| 2. Kỳ vọng, chưa biết $\sigma$ | $T = \dfrac{\overline{X} - a}{s}\sqrt{n}$        | $t(n-1)$         |
| 3. Tỷ lệ                       | $Z = \dfrac{f - p}{\sqrt{p(1-p)}}\sqrt{n}$       | $\approx N(0;1)$ |
| 4. Phương sai                  | $\chi^2 = \dfrac{(n-1)s^2}{\sigma^2}$            | $\chi^2(n-1)$    |

**Ba kiểu khoảng**, tuỳ cách chia $\alpha$ thành $\alpha_1 + \alpha_2$:

| Kiểu         | $\alpha_1$ | $\alpha_2$ | Dùng khi                                           |
| ------------ | ---------- | ---------- | -------------------------------------------------- |
| **Đối xứng** | $\alpha/2$ | $\alpha/2$ | muốn khoảng **ngắn nhất** (mặc định)               |
| **Phải**     | 0          | $\alpha$   | chỉ quan tâm **cận dưới** ("ít nhất bao nhiêu")    |
| **Trái**     | $\alpha$   | 0          | chỉ quan tâm **cận trên** ("nhiều nhất bao nhiêu") |

Giáo trình nhận xét (tr. 143): *"Với cùng độ tin cậy $1-\alpha$, rõ ràng khoảng tin cậy **càng ngắn
càng tốt**. Theo nghĩa đó **khoảng (4.7) đối xứng là tốt nhất**."*

Trong thực tế thường chọn $1-\alpha =$ **0,95; 0,99 hoặc 0,999**.

---

## 5. Bài toán 1: kỳ vọng khi đã biết sigma

**Giả thiết:** $X \sim N(a; \sigma^2)$, $\sigma = \sigma_0$ **đã biết**, tìm khoảng cho $a$.

**Thống kê (4.4):** $\ Z = \dfrac{\overline{X} - a}{\sigma_0}\sqrt{n} \sim N(0;1)$

### Khoảng đối xứng (4.7) — công thức quan trọng nhất

$$\boxed{\left(\overline{X} - \frac{\sigma_0}{\sqrt{n}}z_{1-\alpha/2};\ \
\overline{X} + \frac{\sigma_0}{\sqrt{n}}z_{1-\alpha/2}\right)}$$

Đại lượng

$$\varepsilon = \frac{\sigma_0}{\sqrt{n}}\,z_{1-\alpha/2} \tag{4.10}$$

gọi là **độ chính xác của ước lượng** — *"nó phản ánh độ lệch của trung bình mẫu so với kỳ vọng
lý thuyết với độ tin cậy $1-\alpha$."*

**Khoảng phải (4.8):** $\left(\overline{X} - \dfrac{\sigma_0}{\sqrt n}z_{1-\alpha};\ +\infty\right)$

**Khoảng trái (4.9):** $\left(-\infty;\ \overline{X} + \dfrac{\sigma_0}{\sqrt n}z_{1-\alpha}\right)$

⚠️ **Bẫy tra bảng.** Giáo trình lưu ý (tr. 143): với bảng **hàm Laplace** (bảng 2, tr. 232 —
tích phân **từ 0**, xem bài 7 mục 6):

$$\text{khoảng đối xứng: } \phi(z_b) = \frac{1-\alpha}{2}, \qquad
\text{khoảng một phía: } \phi(z_b) = \frac{1}{2} - \alpha$$

Ba giá trị dùng nhiều nhất — **nên thuộc**:

| $1-\alpha$ | $z_{1-\alpha/2}$ (hai phía) | $z_{1-\alpha}$ (một phía) |
| ---------- | --------------------------: | ------------------------: |
| 90%        |                       1,645 |                     1,282 |
| **95%**    |                   **1,960** |                 **1,645** |
| 99%        |                       2,576 |                     2,326 |

### ⭐ Công thức (4.10) — ba biến, biết hai suy ra một

$$\varepsilon = \frac{\sigma_0}{\sqrt{n}}\,z_{1-\alpha/2}$$

Ba đại lượng: **độ chính xác** $\varepsilon$, **cỡ mẫu** $n$, **độ tin cậy** $1-\alpha$.
Giáo trình nói: *"Nếu biết 2 trong số 3 tham số ta hoàn toàn xác định được biến thứ ba."*

Hai nhận xét (tr. 144):

- $n$ tăng, độ tin cậy giữ nguyên → $\varepsilon$ **giảm** (chính xác hơn).
- Độ tin cậy tăng, $n$ giữ nguyên → $z$ tăng → $\varepsilon$ **tăng** (kém chính xác hơn).

💼 **Đây là tam giác đánh đổi của mọi nghiên cứu thị trường**: chính xác – tin cậy – chi phí.
Muốn tăng hai cái đầu thì phải trả cái thứ ba.

### Thí dụ 4.1 (tr. 143)

> Ước lượng thời gian trung bình sản xuất 1 ram giấy. Thời gian tuân theo luật chuẩn với
> $\sigma = 0{,}3$ phút. Mẫu 36 ram cho $\overline{X} = 1{,}2$ phút. Khoảng tin cậy 95%?

$$\varepsilon = \frac{0{,}3}{\sqrt{36}} \times 1{,}96 = 0{,}05 \times 1{,}96 = 0{,}098$$

$$(1{,}2 - 0{,}098;\ 1{,}2 + 0{,}098) = \mathbf{(1{,}102;\ 1{,}298)}$$

### Thí dụ 4.2 (tr. 143) — ⚠️ có lỗi in

> Muốn độ chính xác **tăng gấp đôi** nhưng độ tin cậy không đổi (0,95) thì cần cỡ mẫu bao nhiêu?

*Giải.* Độ chính xác gấp đôi nghĩa là $\varepsilon$ **giảm một nửa**: $\varepsilon = 0{,}049$.
Từ (4.10):

$$n \ge \frac{\sigma_0^2}{\varepsilon^2}z_{0{,}975}^2 = \frac{(0{,}3)^2}{(0{,}049)^2}(1{,}96)^2
= \left(\frac{0{,}3 \times 1{,}96}{0{,}049}\right)^2 = 12^2 = \mathbf{144}$$

⚠️ **Đính chính.** Sách in $\approx \mathbf{142}$. Đã đối chiếu bản quét gốc trang 143: công thức
viết đúng, kết quả số sai. Giá trị đúng là **144**.

⭐ Và con số 144 **đẹp hơn nhiều** so với 142, vì $144 = 4 \times 36$ — đúng **luật căn bậc hai**
của bài 6 mục 4: muốn chính xác gấp đôi thì phải tăng cỡ mẫu **gấp bốn**.

Con số 142 làm mất đi bài học đó.

### 💼 Góc QTKD — công thức cỡ mẫu

Đảo (4.10) được công thức lập kế hoạch khảo sát:

$$\boxed{n \ge \left(\frac{\sigma \cdot z_{1-\alpha/2}}{\varepsilon}\right)^{\!2}}$$

Ví dụ: doanh thu ngày có $\sigma \approx 16{,}6$ triệu. Muốn ước lượng doanh thu trung bình với
sai số $\pm 2$ triệu, độ tin cậy 95%:

$$n \ge \left(\frac{16{,}6 \times 1{,}96}{2}\right)^2 = 265 \text{ ngày}$$

Con số này nên tính **trước khi** thu thập dữ liệu, không phải sau. Thu 60 ngày rồi mới biết cần 265
là đã muộn.

⚠️ Vòng luẩn quẩn: công thức cần $\sigma$, mà $\sigma$ chỉ biết sau khi có dữ liệu. Cách thoát:
làm **khảo sát thử** (pilot) cỡ 30 để ước lượng $\sigma$, rồi mới tính $n$ cho khảo sát chính.

---

## 6. Bài toán 2: kỳ vọng khi chưa biết sigma

Đây là **trường hợp thực tế nhất** — trong kinh doanh gần như không bao giờ biết trước $\sigma$.

**Cách làm (tr. 144):** ước lượng $\sigma$ bằng $s$, rồi dùng thống kê

$$T = \frac{\overline{X} - a}{s}\sqrt{n} \sim t(n-1) \tag{4.11}$$

Giáo trình chỉ ra: so (4.13) với (4.6) *"ta thấy **chỉ khác nhau ở hai chỗ**: thay $\sigma_0$ bằng $s$
và thay giá trị bảng Laplace bằng bảng Student."*

### Khoảng đối xứng (4.13)

$$\boxed{\left(\overline{X} - \frac{s}{\sqrt{n}}\,t_{n-1;\,1-\alpha/2};\ \
\overline{X} + \frac{s}{\sqrt{n}}\,t_{n-1;\,1-\alpha/2}\right)}$$

Khoảng phải và trái tương tự, với $t_{n-1;\,1-\alpha}$.

⚠️ **Ba chỗ dễ sai:**

1. **Bậc tự do là $n-1$**, không phải $n$.
2. **Dùng $s$** (chia $n-1$), không phải $\hat{S}$ (chia $n$).
3. **$t > z$ luôn luôn** — khoảng Student **rộng hơn** khoảng chuẩn. Đó là cái giá của việc
   không biết $\sigma$.

|  $n$ | $t_{n-1;\,0{,}975}$ | so với $z = 1{,}96$ |
| ---: | ------------------: | ------------------- |
|    5 |               2,776 | rộng hơn 42%        |
|   10 |               2,262 | rộng hơn 15%        |
|   30 |               2,045 | rộng hơn 4,3%       |
|   61 |               2,000 | rộng hơn 2,0%       |
|  121 |               1,980 | rộng hơn 1,0%       |

Giáo trình cho mốc thực hành (tr. 146): **$n > 30$ thì $T$ tiệm cận $N(0;1)$**, làm như bài toán 1
với $\sigma_0$ thay bằng $s$.

### Thí dụ 4.3 (tr. 144) — ⚠️ có lỗi in

> Lò bánh ước lượng trọng lượng trung bình bột dùng hằng ngày. 14 ngày cho $\overline{X} = 17{,}3$ kg,
> $s = 4{,}5$ kg. Khoảng tin cậy 99%?

*Giải.* $t_{13;\,0{,}995} = 3{,}012$:

$$\varepsilon = \frac{4{,}5}{\sqrt{14}} \times 3{,}012 = 1{,}2027 \times 3{,}012 = 3{,}6228$$

$$(17{,}3 - 3{,}62;\ 17{,}3 + 3{,}62) = \mathbf{(13{,}68;\ 20{,}92)}$$

⚠️ **Đính chính — sách sai hai chỗ cùng lúc.** Bản quét gốc trang 144 in:

$$\left(\overline{X} - \frac{4{,}5}{14}\cdot 3{,}012,\ \overline{X} + \frac{4{,}5}{14}\cdot 3{,}012\right) = (136{,}77;\ 209{,}23)$$

1. **Thiếu dấu căn:** mẫu số phải là $\sqrt{14} = 3{,}742$, không phải $14$.
2. **Sai dấu phẩy:** kết quả in lớn gấp **10 lần**. Với $\overline{X} = 17{,}3$ thì khoảng tin cậy
   **bắt buộc phải nằm quanh 17,3** — con số 136,77 vô lý ngay từ cái nhìn đầu tiên.

Kết quả đúng: **(13,68; 20,92)**.

⭐ **Bài học kiểm tra bài làm:** khoảng tin cậy cho kỳ vọng **luôn đối xứng quanh $\overline{X}$**.
Nếu $\overline{X}$ không nằm chính giữa khoảng bạn tính ra, đã sai ở đâu đó.

### Thí dụ 4.4 (tr. 145) — mẫu rất nhỏ

> Nhiệt độ cao nhất ở 5 vùng tỉnh Lâm Đồng ngày 25/9: **25, 27, 29, 32, 33** °C.
> Khoảng tin cậy 95% cho nhiệt độ cao nhất trung bình?

*Giải.*

$$\overline{X} = \frac{146}{5} = 29{,}2, \qquad \sum(x_i - \overline{X})^2 = 44{,}8,
\qquad s = \sqrt{\frac{44{,}8}{4}} = 3{,}35$$

$t_{4;\,0{,}975} = 2{,}776$:

$$\left(29{,}2 - \frac{3{,}35}{\sqrt5}\cdot 2{,}776;\ 29{,}2 + \frac{3{,}35}{\sqrt5}\cdot 2{,}776\right)
= \mathbf{(25{,}04;\ 33{,}36)}$$

Khoảng rộng **8,3 độ** với chỉ 5 quan sát — minh hoạ rõ cái giá của mẫu nhỏ.

### ⚠️ Câu cảnh báo quan trọng nhất của cả bài

Ngay sau thí dụ 4.4, giáo trình viết (tr. 146):

> "Để ý đây là khoảng tin cậy 95% tính trên bộ số liệu cụ thể của thí dụ, nó **hoàn toàn không có
> nghĩa là xác suất để trung bình thật rơi vào khoảng tin cậy trên là 0,95**. Bởi vậy không nên quên
> rằng độ tin cậy 95% của một khoảng nào đó được hiểu **theo nghĩa thống kê** (tức là nếu cứ làm
> thí nghiệm 100 lần với các khoảng tin cậy 95% thì có khoảng **95 lần giá trị trung bình thật
> nằm trong khoảng đó**)."

Mục 9 sẽ mổ xẻ câu này.

---

## 7. Bài toán 3: khoảng tin cậy cho tỷ lệ

**Bối cảnh (tr. 146):** dấu hiệu $X \sim B(p)$ (Bernoulli). Tần suất mẫu $f = m/n$ là ước lượng điểm
của $p$. Vì $nf \sim B(n,p)$ nên $Ef = p$, $Vf = \dfrac{p(1-p)}{n}$.

**Thống kê (4.14):**

$$Z = \frac{f - p}{\sqrt{p(1-p)}}\sqrt{n} \ \xrightarrow{\ L\ } N(0;1) \quad (n \text{ khá lớn})$$

Giáo trình cho **hai cách** giải.

### Cách 1 — chính xác, giải phương trình bậc hai (4.15)

Giữ nguyên $p$ ở mẫu số, bình phương hai vế bất đẳng thức rồi giải:

$$p_{1,2} = \frac{nf + \frac12 z_b^2 \pm z_b\sqrt{nf(1-f) + \frac14 z_b^2}}{n + z_b^2}$$

Giáo trình thừa nhận: *"việc tính toán theo (4.15) sẽ **khá khó khăn**."*
(Ngày nay công thức này có tên là **khoảng Wilson**, và là khoảng được khuyến nghị dùng.)

### Cách 2 — xấp xỉ, thay $p$ bằng $f$ ở mẫu số

Khi $n$ khá lớn, thay $Vf = p(1-p)/n$ bằng ước lượng điểm $f(1-f)/n$. Khi đó quy trình bài toán 1
áp dụng được ngay, với $\overline{X} \to f$ và $\sigma_0 \to \sqrt{f(1-f)}$:

**Khoảng đối xứng (4.16):**

$$\boxed{\left(f - \sqrt{\frac{f(1-f)}{n}}\,z_{1-\alpha/2};\ \
f + \sqrt{\frac{f(1-f)}{n}}\,z_{1-\alpha/2}\right)}$$

**Khoảng phải (4.17a)** và **trái (4.17b)** với $z_{1-\alpha}$.

Độ chính xác: $\ \varepsilon = \sqrt{\dfrac{f(1-f)}{n}}\,z_{1-\alpha/2}$

### Thí dụ 4.5 (tr. 148)

> Kiểm 600 sản phẩm thấy 24 phế phẩm. Độ tin cậy 95%, ước lượng tỷ lệ phế phẩm **tối đa**.

*"Tối đa"* → dùng **khoảng trái** (4.17b), $z_b = z_{0{,}95} = 1{,}645$:

$$f = \frac{24}{600} = 0{,}04, \qquad
0{,}04 + \sqrt{\frac{0{,}04 \times 0{,}96}{600}} \times 1{,}645 = \mathbf{0{,}05316}$$

Tỷ lệ phế phẩm tối đa **5,32%**. (Sách in 5,312% do tra bảng $z = 1{,}64$; dùng $1{,}6449$ chính xác
được 5,316%.)

💼 **Đọc đề để chọn kiểu khoảng:**

| Đề hỏi                                     | Kiểu khoảng             |
| ------------------------------------------ | ----------------------- |
| "tối đa bao nhiêu", "không quá bao nhiêu"  | **trái** (chỉ cận trên) |
| "tối thiểu bao nhiêu", "ít nhất bao nhiêu" | **phải** (chỉ cận dưới) |
| "trong khoảng nào", "ước lượng"            | **đối xứng**            |

### Thí dụ 4.6 (tr. 149)

> Phỏng vấn 400 người ở khu vực 300.000 người, 240 người ủng hộ dự luật A. Độ tin cậy 0,95,
> ước lượng **số người** ủng hộ trong khu vực.

$$f = \frac{240}{400} = 0{,}6, \qquad \varepsilon = \sqrt{\frac{0{,}6 \times 0{,}4}{400}} \times 1{,}96 = 0{,}048$$

$$0{,}552 < p < 0{,}648$$

Nhân với dân số:

$$(300\,000 \times 0{,}552;\ 300\,000 \times 0{,}648) = \mathbf{(165\,600;\ 194\,400)}$$

So với công thức chính xác (4.15): $(0{,}5513;\ 0{,}6468)$ — chênh chưa tới 0,1 điểm phần trăm.
Với $n = 400$ và $f$ gần 0,5, hai cách gần như trùng nhau.

⚠️ Nhưng khi $f$ **gần 0 hoặc gần 1**, hai cách chênh nhiều. Ví dụ $f = 0{,}02$, $n = 50$:
công thức (4.16) cho cận dưới **âm** — vô nghĩa với một tỷ lệ. Khi đó **bắt buộc dùng (4.15)**.

**Quy tắc kiểm tra nhanh:** cần $nf > 5$ **và** $n(1-f) > 5$ thì xấp xỉ chuẩn mới dùng được
(đúng điều kiện xấp xỉ nhị thức ở bài 7 mục 7).

### 💼 Góc QTKD — vì sao thăm dò dư luận luôn ghi "±3%"

Với $f$ gần 0,5 (trường hợp xấu nhất, $f(1-f)$ đạt max) và độ tin cậy 95%:

$$\varepsilon \approx \frac{0{,}98}{\sqrt{n}}$$

|       $n$ | $\varepsilon$ |
| --------: | ------------: |
|       100 |         ±9,8% |
|       400 |         ±4,9% |
| **1.000** |     **±3,1%** |
|     1.500 |         ±2,5% |
|     4.000 |         ±1,5% |

⭐ **Đây là lý do con số 1.000 xuất hiện ở mọi cuộc thăm dò**: đó là điểm mà sai số xuống ~3%,
đủ dùng, và tăng thêm thì chi phí tăng nhanh hơn nhiều so với lợi ích (luật căn bậc hai).

⚠️ Và chú ý: sai số này **không phụ thuộc dân số** (miễn là $N \gg n$). Khảo sát 1.000 người cho
sai số ±3% dù dân số là 300.000 hay 100 triệu. Điều này rất phản trực giác nhưng đúng — xem lại
thừa số hiệu chỉnh ở bài 10 mục 5.

---

## 8. Bài toán 4: khoảng tin cậy cho phương sai

**Giả thiết:** $X \sim N(a; \sigma^2)$, tìm khoảng cho $\sigma^2$.

Dựa trên hai sự kiện (4.18), (4.19):

$$\frac{(n-1)s^2}{\sigma^2} = \frac{\sum(x_i - \overline{X})^2}{\sigma^2} \sim \chi^2(n-1)
\qquad \text{(chưa biết } a)$$

$$\frac{\sum(x_i - a)^2}{\sigma^2} \sim \chi^2(n) \qquad \text{(biết } a)$$

### Khoảng đối xứng

**Khi BIẾT $a = a_0$** (4.21) — dùng $\chi^2(n)$:

$$\left(\frac{\sum(x_i - a_0)^2}{\chi^2_{n;\,1-\alpha/2}};\ \
\frac{\sum(x_i - a_0)^2}{\chi^2_{n;\,\alpha/2}}\right)$$

**Khi CHƯA BIẾT $a$** (4.22) — dùng $\chi^2(n-1)$ và $\overline{X}$:

$$\boxed{\left(\frac{(n-1)s^2}{\chi^2_{n-1;\,1-\alpha/2}};\ \
\frac{(n-1)s^2}{\chi^2_{n-1;\,\alpha/2}}\right)}$$

⚠️ **Hai điều khác hẳn ba bài toán trước:**

1. **Khoảng KHÔNG đối xứng** quanh $s^2$ — vì phân phối $\chi^2$ lệch phải.
2. **Phân vị lớn ở MẪU SỐ của cận DƯỚI.** Chia cho số lớn được số nhỏ. Đây là chỗ nhầm nhiều nhất —
   nhiều người viết ngược và ra khoảng âm hoặc lộn đầu.

### Thí dụ 4.7 (tr. 152)

> Khối lượng sản phẩm tuân theo luật chuẩn. Mẫu 25 đơn vị:

| Khối lượng  | 29,3 | 29,7 | 30,0 | 30,5 | 30,7 |
| ----------- | ---: | ---: | ---: | ---: | ---: |
| Số sản phẩm |    4 |    5 |    8 |    5 |    3 |

> Độ tin cậy 95%, tìm khoảng cho phương sai: a) biết $a = 30$; b) không biết $a$.

*Giải.* $\overline{X} = \dfrac{750{,}3}{25} = 30{,}012$

**a) Biết $a = 30$** — dùng $\chi^2(25)$:

$$\sum(x_i - 30)^2 n_i = 5{,}13, \qquad \chi^2_{25;\,0{,}975} = 40{,}65, \quad \chi^2_{25;\,0{,}025} = 13{,}12$$

$$\left(\frac{5{,}13}{40{,}65};\ \frac{5{,}13}{13{,}12}\right) = \mathbf{(0{,}1262;\ 0{,}3910)}$$

**b) Chưa biết $a$** — dùng $\chi^2(24)$:

$$24s^2 = \sum(x_i - 30{,}012)^2 n_i = 5{,}1264,
\qquad \chi^2_{24;\,0{,}975} = 39{,}36, \quad \chi^2_{24;\,0{,}025} = 12{,}40$$

$$\left(\frac{5{,}1264}{39{,}36};\ \frac{5{,}1264}{12{,}40}\right) = \mathbf{(0{,}1302;\ 0{,}4134)}$$

Lấy căn được khoảng cho **độ lệch chuẩn**: $(0{,}361;\ 0{,}643)$.

⚠️ **Nhận xét quan trọng:** khoảng cho $\sigma^2$ rộng gấp hơn **3 lần** (0,13 đến 0,41).
Ước lượng phương sai **kém chính xác hơn nhiều** so với ước lượng kỳ vọng ở cùng cỡ mẫu — cần
nhiều dữ liệu hơn hẳn để nói được điều gì chắc chắn về độ biến động.

💼 Đây là lý do các phát biểu kiểu *"quy trình mới giảm được độ biến động"* rất khó chứng minh
trong thực tế: cần cỡ mẫu lớn hơn nhiều so với chứng minh *"quy trình mới tăng được năng suất
trung bình"*.

---

## 9. 📚 95% nghĩa là gì và không nghĩa là gì

Giáo trình nêu đúng vấn đề ở tr. 146 nhưng chỉ trong một đoạn. Đây là phần khai triển —
và là **hiểu lầm phổ biến nhất về thống kê**.

### ❌ Cách hiểu SAI

> *"Xác suất để kỳ vọng thật nằm trong khoảng (25,04; 33,36) là 95%."*

**Sai ở đâu?** Vì $a$ là **một hằng số** — cố định, không ngẫu nhiên (bài 10 mục 9: chữ Hy Lạp =
tham số tổng thể, cố định nhưng chưa biết). Nó **hoặc nằm trong khoảng đó, hoặc không**.
Xác suất là 0 hoặc 1, ta chỉ không biết là cái nào.

Khoảng $(25{,}04;\ 33{,}36)$ cũng đã cố định — nó được tính từ dữ liệu cụ thể rồi.
**Hai vật cố định không có xác suất nào giữa chúng.**

### ✅ Cách hiểu ĐÚNG

> *"Nếu lặp lại quy trình này nhiều lần — mỗi lần lấy một mẫu mới và tính khoảng tin cậy 95% —
> thì khoảng **95% số khoảng** sẽ chứa giá trị thật."*

Đúng như giáo trình viết: *"nếu cứ làm thí nghiệm 100 lần với các khoảng tin cậy 95% thì có
khoảng 95 lần giá trị trung bình thật nằm trong khoảng đó."*

**95% là tính chất của QUY TRÌNH, không phải của MỘT khoảng cụ thể.**

```
   Giá trị thật a (cố định)
             │
   mẫu 1  ├──┼───┤          ✓ chứa a
   mẫu 2     ├──┼──┤        ✓
   mẫu 3  ├─┼────┤          ✓
   mẫu 4              ├───┤ ✗ KHÔNG chứa a   ← khoảng 5% số lần
   mẫu 5   ├───┼──┤         ✓
   ...
             │
        khoảng DI CHUYỂN, a ĐỨNG YÊN
```

Mô phỏng ở mục 10 kiểm điều này bằng số: lấy 1.000 mẫu, đếm được **946/1000 = 94,6%** khoảng
chứa giá trị thật — sát 95%.

### 💼 Hệ quả thực tế

| Phát biểu                                                             | Đúng/Sai                                    |
| --------------------------------------------------------------------- | ------------------------------------------- |
| "95% khả năng doanh thu trung bình nằm trong (50,95; 59,53)"          | ❌ sai (về mặt chặt chẽ)                    |
| "Quy trình này cho khoảng chứa giá trị thật trong 95% trường hợp"     | ✅ đúng                                     |
| "Chúng tôi tin cậy 95% rằng doanh thu trung bình nằm trong khoảng đó" | ⚠️ thông dụng, chấp nhận được trong báo cáo |

⚠️ **Trong thi cử thì phải phát biểu đúng.** Trong báo cáo kinh doanh, cách nói thứ ba được chấp
nhận rộng rãi — nhưng nên nhớ nó là cách nói tắt.

📚 Nếu bạn thật sự muốn nói *"xác suất để $a$ nằm trong khoảng này là 95%"* thì cần **thống kê
Bayes** (dựa trên công thức bài 4), nơi tham số **được coi là** biến ngẫu nhiên. Khoảng tương ứng
gọi là **khoảng tin (credible interval)**, khác với **khoảng tin cậy (confidence interval)** ở đây.
Giáo trình chỉ dạy trường phái tần suất.

### Ba điều khác cần nhớ

1. **Độ tin cậy cao hơn ⟹ khoảng rộng hơn.** Không có bữa ăn miễn phí. Muốn chắc chắn hơn thì
   phải nói mơ hồ hơn. Khoảng tin cậy 100% luôn là $(-\infty; +\infty)$ — đúng tuyệt đối và vô dụng
   hoàn toàn.

2. **Khoảng tin cậy KHÔNG nói về từng quan sát.** Khoảng $(50{,}95;\ 59{,}53)$ là cho **doanh thu
   trung bình**, không phải cho doanh thu của một ngày cụ thể. Ngày mai vẫn có thể 30 hoặc 130 triệu.
   (Khoảng cho một quan sát mới gọi là **khoảng dự báo**, rộng hơn nhiều — bài 14.)

3. **Mọi công thức trong bài đều giả định mẫu NGẪU NHIÊN.** Không có phép màu nào cứu được một
   mẫu thiên lệch. Khảo sát sai đối tượng thì khoảng tin cậy 99,9% cũng vô nghĩa —
   nó chỉ đo sai số **lấy mẫu**, không đo sai số **chọn mẫu**.

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.
> Chạy từ thư mục gốc khoá học: `cd houedu/xacxuatthongke && python3 bai-11-khoang-tin-cay.py`.
> Chạy khoảng 0,5 giây.

**Điểm đặc biệt của code này: nó tự dựng lại bảng 3 và bảng 4 của phụ lục giáo trình.**

Phân vị Student và chi bình phương thường phải tra bảng hoặc cài `scipy`. Ở đây ta tự viết bằng
`math.lgamma` (có sẵn trong thư viện chuẩn), theo đúng định nghĩa:

```
   hàm mật độ  ──tích phân số (Simpson)──►  hàm phân phối F(x)
                                                     │
                              ◄──chia đôi (bisection)┘
                          phân vị = nghiệm của F(x) = p
```

Bảy dòng đầu của kết quả đối chiếu với phụ lục — khớp tới **4 chữ số**. Nghĩa là bạn không còn cần
bảng tra số nữa, và quan trọng hơn: bạn thấy **bảng tra số thực chất là gì**.

```python
"""Bài 11 — Ước lượng điểm và khoảng tin cậy."""

import csv
import math
import pathlib
import random
from functools import lru_cache
from statistics import NormalDist

DATA = pathlib.Path("thuc_hanh/du_lieu")
Z = NormalDist()

# ─────────────────────────────────────────────────────────────
# BẢNG TRA SỐ TỰ VIẾT — thay bang 2, 3, 4 cua phu luc.
# Chi dung math.lgamma cua thu vien chuan, KHONG can scipy.
# Y tuong: mat do -> tich phan so ra CDF -> chia doi de tim phan vi.
# ─────────────────────────────────────────────────────────────
def _cdf_from_pdf(pdf, x, lo, steps=20_000):
    """Tich phan so (Simpson) tu `lo` den `x`."""
    if x <= lo:
        return 0.0
    h = (x - lo) / steps
    s = pdf(lo) + pdf(x)
    for i in range(1, steps):
        s += pdf(lo + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def t_pdf(x, n):
    c = math.lgamma((n + 1) / 2) - math.lgamma(n / 2) - 0.5 * math.log(n * math.pi)
    return math.exp(c) * (1 + x * x / n) ** (-(n + 1) / 2)


def chi2_pdf(x, n):
    if x <= 0:
        return 0.0
    c = (n / 2 - 1) * math.log(x) - x / 2 - (n / 2) * math.log(2) - math.lgamma(n / 2)
    return math.exp(c)


def _invert(cdf, p, lo, hi):
    """Tim x sao cho cdf(x) = p, bang phuong phap chia doi."""
    for _ in range(60):
        mid = (lo + hi) / 2
        if cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


@lru_cache(maxsize=None)
def t_quantile(p, n):
    """Phan vi muc p cua Student t(n) — thay bang 3 (tr. 233)."""
    if p < 0.5:
        return -t_quantile(1 - p, n)
    cdf = lambda x: 0.5 + _cdf_from_pdf(lambda u: t_pdf(u, n), x, 0.0, 2000)
    return _invert(cdf, p, 0.0, 60.0)


@lru_cache(maxsize=None)
def chi2_quantile(p, n):
    """Phan vi muc p cua chi bình phương chi2(n) — thay bang 4 (tr. 234)."""
    cdf = lambda x: _cdf_from_pdf(lambda u: chi2_pdf(u, n), x, 1e-12, 3000)
    return _invert(cdf, p, 1e-9, 20 * n + 200)


# Doi chieu voi bang so cua giao trinh de chung minh ham tren dung
print("KIEM BANG TRA SO TU VIET (doi chieu voi phu luc giao trinh)")
for p, n, sach in [(0.975, 4, 2.776), (0.995, 13, 3.012), (0.975, 9, 2.262)]:
    print(f"  t({n}) phan vi {p}  = {t_quantile(p, n):.4f}   (bang 3: {sach})")
for p, n, sach in [(0.975, 25, 40.65), (0.025, 25, 13.12),
                   (0.975, 24, 39.36), (0.025, 24, 12.40)]:
    print(f"  chi2({n}) phan vi {p} = {chi2_quantile(p, n):>7.4f}   (bang 4: {sach})")

# ─────────────────────────────────────────────────────────────
# 1. BÀI TOÁN 1 — khoảng tin cậy cho kỳ vọng, ĐÃ BIẾT sigma
#    Thí dụ 4.1 (tr. 143): n=36, X=1,2 phut/ram, sigma=0,3
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.1 — thoi gian san xuat 1 ram giay, sigma DA BIET")
xbar, sig, n, alpha = 1.2, 0.3, 36, 0.05
z = Z.inv_cdf(1 - alpha / 2)
eps = sig / math.sqrt(n) * z
print(f"  n={n}  X={xbar}  sigma={sig}  1-alpha={1 - alpha}")
print(f"  z(1-a/2) = {z:.4f}   (sach tra bang: 1,96)")
print(f"  Do chinh xac eps = sigma/can(n) * z = {eps:.4f}")
print(f"  Khoang doi xung: ({xbar - eps:.3f}; {xbar + eps:.3f})"
      f"   (sach: 1,102; 1,298)")
print(f"  Khoang PHAI: ({xbar - sig / math.sqrt(n) * Z.inv_cdf(1 - alpha):.3f}; +vc)")
print(f"  Khoang TRAI: (-vc; {xbar + sig / math.sqrt(n) * Z.inv_cdf(1 - alpha):.3f})")

# Thí dụ 4.2 (tr. 143) — muốn độ chính xác GẤP ĐÔI thì cần n bao nhiêu?
print()
print("THI DU 4.2 — muon do chinh xac GAP DOI, giu do tin cay 95%")
eps2 = eps / 2
n_need = (sig * z / eps2) ** 2
print(f"  eps moi = {eps2:.4f}")
print(f"  n >= (sigma.z/eps)^2 = ({sig}*{z:.2f}/{eps2:.3f})^2 = {n_need:.2f}"
      f"  ->  n = {math.ceil(n_need)}   (sach: 142 - xem dinh chinh)")
print(f"  Kiem bang luat can bac hai: gap doi chinh xac -> 4 lan co mau ="
      f" {4 * n}")

# ─────────────────────────────────────────────────────────────
# 2. BÀI TOÁN 2 — kỳ vọng, CHƯA BIẾT sigma  ->  dùng Student
#    Thí dụ 4.3 (tr. 144) va 4.4 (tr. 145)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.3 — lo banh, n=14, X=17,3 kg, s=4,5 kg, do tin cay 99%")
xbar, s, n, alpha = 17.3, 4.5, 14, 0.01
tq = t_quantile(1 - alpha / 2, n - 1)
eps = s / math.sqrt(n) * tq
print(f"  t({n - 1}; {1 - alpha / 2}) = {tq:.4f}   (sach: 3,012)")
print(f"  eps = s/can(n) * t = {s}/{math.sqrt(n):.4f} * {tq:.3f} = {eps:.4f}")
print(f"  Khoang tin cay 99%: ({xbar - eps:.2f}; {xbar + eps:.2f})")
print(f"  ⚠ Sach in (136,77; 209,23) — sai dau phay VA thieu dau can. Xem dinh chinh.")

print()
print("THI DU 4.4 — nhiet do 5 vung Lam Dong: 25, 27, 29, 32, 33")
temps = [25, 27, 29, 32, 33]
n = len(temps)
xbar = sum(temps) / n
ss = sum((x - xbar) ** 2 for x in temps)
s = math.sqrt(ss / (n - 1))
print(f"  X = {xbar}   tong binh phuong do lech = {ss}   s = {s:.4f}"
      f"   (sach: 29,2 / 44,8 / 3,35)")
tq = t_quantile(0.975, n - 1)
eps = s / math.sqrt(n) * tq
print(f"  t(4; 0,975) = {tq:.4f}   (sach: 2,776)")
print(f"  Khoang 95%: ({xbar - eps:.2f}; {xbar + eps:.2f})   (sach: 25,04; 33,36)")

# ─────────────────────────────────────────────────────────────
# 3. ⚠ Ý NGHĨA THẬT của "độ tin cậy 95%" — mô phỏng 1000 lần
# ─────────────────────────────────────────────────────────────
print()
print("⚠ '95%' NGHIA LA GI — lay 1000 mau n=10 tu N(50; 8^2), dem so lan trung")
rng = random.Random(2026)
MU, SD, NS, REPS = 50.0, 8.0, 10, 1000
hit = 0
for _ in range(REPS):
    smp = [rng.gauss(MU, SD) for _ in range(NS)]
    m_ = sum(smp) / NS
    s_ = math.sqrt(sum((x - m_) ** 2 for x in smp) / (NS - 1))
    e_ = s_ / math.sqrt(NS) * t_quantile(0.975, NS - 1)
    hit += m_ - e_ <= MU <= m_ + e_
print(f"  So khoang CHUA gia tri that {MU}: {hit}/{REPS} = {hit / REPS:.1%}")
print("  => '95%' la tinh chat cua QUY TRINH, khong phai cua MOT khoang cu the")

# ─────────────────────────────────────────────────────────────
# 4. BÀI TOÁN 3 — khoảng tin cậy cho TỶ LỆ
#    Thí dụ 4.5 (tr. 148) va 4.6 (tr. 149)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.5 — 600 san pham co 24 phe pham, uoc luong ty le TOI DA (95%)")
n, m = 600, 24
f = m / n
zb = Z.inv_cdf(0.95)
hi_ = f + math.sqrt(f * (1 - f) / n) * zb
print(f"  f = {m}/{n} = {f}   z(0,95) = {zb:.4f}   (sach: 1,64)")
print(f"  Khoang TRAI: (-vc; {hi_:.5f})  ->  ty le phe pham toi da"
      f" {hi_ * 100:.3f}%   (sach: 5,312%)")

print()
print("THI DU 4.6 — phong van 400 nguoi, 240 ung ho; khu vuc 300.000 nguoi")
n, m, POP = 400, 240, 300_000
f = m / n
z = Z.inv_cdf(0.975)
eps = math.sqrt(f * (1 - f) / n) * z
print(f"  f = {f}   z(0,975) = {z:.4f}   eps = {eps:.4f}")
print(f"  Khoang cho p: ({f - eps:.4f}; {f + eps:.4f})   (sach: 0,5522; 0,6478)")
print(f"  Quy ra so nguoi: ({round(POP * (f - eps)):,}; {round(POP * (f + eps)):,})"
      f"   (sach: 165660; 194340)")
# Cach chinh xac hon — cong thuc (4.15), giai phuong trinh bac 2
z2 = z * z
den = n + z2
p1 = (n * f + z2 / 2 - z * math.sqrt(n * f * (1 - f) + z2 / 4)) / den
p2 = (n * f + z2 / 2 + z * math.sqrt(n * f * (1 - f) + z2 / 4)) / den
print(f"  Theo (4.15) chinh xac hon: ({p1:.4f}; {p2:.4f})"
      f"   (sach: 0,5513; 0,6468)")

# ─────────────────────────────────────────────────────────────
# 5. BÀI TOÁN 4 — khoảng tin cậy cho PHƯƠNG SAI
#    Thí dụ 4.7 (tr. 152)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.7 — khoi luong 25 san pham, do tin cay 95%")
vals = [29.3, 29.7, 30.0, 30.5, 30.7]
cnt = [4, 5, 8, 5, 3]
n = sum(cnt)
xbar = sum(v * c for v, c in zip(vals, cnt)) / n
print(f"  X = {xbar:.4f}   (sach: 30,012)")
ss_known = sum(c * (v - 30) ** 2 for v, c in zip(vals, cnt))
ss_unknown = sum(c * (v - xbar) ** 2 for v, c in zip(vals, cnt))
print(f"  a) BIET a = 30: tong (xi-30)^2.ni = {ss_known:.4f}   (sach: 5,13)")
lo_ = ss_known / chi2_quantile(0.975, n)
hi_ = ss_known / chi2_quantile(0.025, n)
print(f"     chi2(25) = {chi2_quantile(0.975, 25):.2f} va"
      f" {chi2_quantile(0.025, 25):.2f}   (sach: 40,65 va 13,12)")
print(f"     Khoang cho sigma^2: ({lo_:.4f}; {hi_:.4f})   (sach: 0,1262; 0,3910)")
print(f"  b) CHUA BIET a: 24s^2 = {ss_unknown:.4f}   (sach: 5,1264)")
lo_ = ss_unknown / chi2_quantile(0.975, n - 1)
hi_ = ss_unknown / chi2_quantile(0.025, n - 1)
print(f"     chi2(24) = {chi2_quantile(0.975, 24):.2f} va"
      f" {chi2_quantile(0.025, 24):.2f}   (sach: 39,36 va 12,40)")
print(f"     Khoang cho sigma^2: ({lo_:.4f}; {hi_:.4f})   (sach: 0,1302; 0,4134)")
print(f"     -> khoang cho sigma: ({math.sqrt(lo_):.4f}; {math.sqrt(hi_):.4f})")

# ─────────────────────────────────────────────────────────────
# 6. 💼 GÓC QTKD — doanh thu 60 ngày từ file CSV
# ─────────────────────────────────────────────────────────────
print()
with open(DATA / "doanh_thu_ngay.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
rev = [float(r["doanh_thu_trieu"]) for r in rows]
n = len(rev)
xbar = sum(rev) / n
s = math.sqrt(sum((x - xbar) ** 2 for x in rev) / (n - 1))
print(f"💼 GOC QTKD — doanh thu {n} ngay: X = {xbar:.2f}, s = {s:.2f} trieu")
print(f"{'do tin cay':>12}{'t/z':>9}{'eps':>9}{'khoang tin cay':>26}"
      f"{'do dai':>9}")
for conf in [0.80, 0.90, 0.95, 0.99]:
    tq = t_quantile(1 - (1 - conf) / 2, n - 1)
    e_ = s / math.sqrt(n) * tq
    print(f"{conf:>12.0%}{tq:>9.3f}{e_:>9.3f}"
          f"{f'({xbar - e_:.2f}; {xbar + e_:.2f})':>26}{2 * e_:>9.3f}")
print("  => Do tin cay cang cao thi khoang cang RONG. Khong co bua an mien phi.")

# Co mau can thiet de sai so +-2 trieu, do tin cay 95%
target = 2.0
n_need = (s * Z.inv_cdf(0.975) / target) ** 2
print(f"  Muon sai so +-{target} trieu voi 95%: can n >= {math.ceil(n_need)} ngay"
      f"  (hien co {n})")

# Khoang tin cay cho TY LE ngay 'tot' (doanh thu > 60 trieu)
good = sum(1 for x in rev if x > 60)
f = good / n
z = Z.inv_cdf(0.975)
e_ = math.sqrt(f * (1 - f) / n) * z
print(f"  Ty le ngay doanh thu > 60 trieu: f = {good}/{n} = {f:.4f}")
print(f"  Khoang 95% cho p: ({f - e_:.4f}; {f + e_:.4f})"
      f"  -> rat rong vi n chi {n}")
```

Kết quả chạy thật:

```
KIEM BANG TRA SO TU VIET (doi chieu voi phu luc giao trinh)
  t(4) phan vi 0.975  = 2.7764   (bang 3: 2.776)
  t(13) phan vi 0.995  = 3.0123   (bang 3: 3.012)
  t(9) phan vi 0.975  = 2.2622   (bang 3: 2.262)
  chi2(25) phan vi 0.975 = 40.6465   (bang 4: 40.65)
  chi2(25) phan vi 0.025 = 13.1197   (bang 4: 13.12)
  chi2(24) phan vi 0.975 = 39.3641   (bang 4: 39.36)
  chi2(24) phan vi 0.025 = 12.4012   (bang 4: 12.4)

THI DU 4.1 — thoi gian san xuat 1 ram giay, sigma DA BIET
  n=36  X=1.2  sigma=0.3  1-alpha=0.95
  z(1-a/2) = 1.9600   (sach tra bang: 1,96)
  Do chinh xac eps = sigma/can(n) * z = 0.0980
  Khoang doi xung: (1.102; 1.298)   (sach: 1,102; 1,298)
  Khoang PHAI: (1.118; +vc)
  Khoang TRAI: (-vc; 1.282)

THI DU 4.2 — muon do chinh xac GAP DOI, giu do tin cay 95%
  eps moi = 0.0490
  n >= (sigma.z/eps)^2 = (0.3*1.96/0.049)^2 = 144.00  ->  n = 144   (sach: 142 - xem dinh chinh)
  Kiem bang luat can bac hai: gap doi chinh xac -> 4 lan co mau = 144

THI DU 4.3 — lo banh, n=14, X=17,3 kg, s=4,5 kg, do tin cay 99%
  t(13; 0.995) = 3.0123   (sach: 3,012)
  eps = s/can(n) * t = 4.5/3.7417 * 3.012 = 3.6228
  Khoang tin cay 99%: (13.68; 20.92)
  ⚠ Sach in (136,77; 209,23) — sai dau phay VA thieu dau can. Xem dinh chinh.

THI DU 4.4 — nhiet do 5 vung Lam Dong: 25, 27, 29, 32, 33
  X = 29.2   tong binh phuong do lech = 44.8   s = 3.3466   (sach: 29,2 / 44,8 / 3,35)
  t(4; 0,975) = 2.7764   (sach: 2,776)
  Khoang 95%: (25.04; 33.36)   (sach: 25,04; 33,36)

⚠ '95%' NGHIA LA GI — lay 1000 mau n=10 tu N(50; 8^2), dem so lan trung
  So khoang CHUA gia tri that 50.0: 946/1000 = 94.6%
  => '95%' la tinh chat cua QUY TRINH, khong phai cua MOT khoang cu the

THI DU 4.5 — 600 san pham co 24 phe pham, uoc luong ty le TOI DA (95%)
  f = 24/600 = 0.04   z(0,95) = 1.6449   (sach: 1,64)
  Khoang TRAI: (-vc; 0.05316)  ->  ty le phe pham toi da 5.316%   (sach: 5,312%)

THI DU 4.6 — phong van 400 nguoi, 240 ung ho; khu vuc 300.000 nguoi
  f = 0.6   z(0,975) = 1.9600   eps = 0.0480
  Khoang cho p: (0.5520; 0.6480)   (sach: 0,5522; 0,6478)
  Quy ra so nguoi: (165,597; 194,403)   (sach: 165660; 194340)
  Theo (4.15) chinh xac hon: (0.5513; 0.6468)   (sach: 0,5513; 0,6468)

THI DU 4.7 — khoi luong 25 san pham, do tin cay 95%
  X = 30.0120   (sach: 30,012)
  a) BIET a = 30: tong (xi-30)^2.ni = 5.1300   (sach: 5,13)
     chi2(25) = 40.65 va 13.12   (sach: 40,65 va 13,12)
     Khoang cho sigma^2: (0.1262; 0.3910)   (sach: 0,1262; 0,3910)
  b) CHUA BIET a: 24s^2 = 5.1264   (sach: 5,1264)
     chi2(24) = 39.36 va 12.40   (sach: 39,36 va 12,40)
     Khoang cho sigma^2: (0.1302; 0.4134)   (sach: 0,1302; 0,4134)
     -> khoang cho sigma: (0.3609; 0.6429)

💼 GOC QTKD — doanh thu 60 ngay: X = 55.24, s = 16.61 trieu
  do tin cay      t/z      eps            khoang tin cay   do dai
         80%    1.296    2.779            (52.46; 58.02)    5.558
         90%    1.671    3.583            (51.66; 58.82)    7.166
         95%    2.001    4.290            (50.95; 59.53)    8.581
         99%    2.662    5.707            (49.53; 60.95)   11.414
  => Do tin cay cang cao thi khoang cang RONG. Khong co bua an mien phi.
  Muon sai so +-2.0 trieu voi 95%: can n >= 265 ngay  (hien co 60)
  Ty le ngay doanh thu > 60 trieu: f = 14/60 = 0.2333
  Khoang 95% cho p: (0.1263; 0.3404)  -> rat rong vi n chi 60
```

Sáu điểm đáng để ý:

1. **Bảy dòng đầu**: bảng tra tự viết khớp phụ lục giáo trình tới 4 chữ số. Toàn bộ bảng 3 và
   bảng 4 (tr. 233–234) gói trong 40 dòng code, không cần gói ngoài nào.
2. **Thí dụ 4.2**: `144.00 -> n = 144` so với sách in 142. Và dòng dưới cho thấy $144 = 4 \times 36$
   — luật căn bậc hai hiện ra rõ ràng.
3. **Thí dụ 4.3**: `(13.68; 20.92)` — nằm quanh $\overline{X} = 17{,}3$ như phải thế, khác hẳn
   `(136,77; 209,23)` của sách.
4. **Mô phỏng 95%**: `946/1000 = 94.6%`. Đây là bằng chứng bằng số cho câu cảnh báo của giáo trình
   ở tr. 146.
5. **Bảng bốn mức độ tin cậy**: độ dài khoảng tăng từ 5,56 (80%) lên 11,41 (99%) — **gấp đôi**.
   Cột `do dai` cho thấy trực tiếp cái giá của sự chắc chắn.
6. **`can n >= 265 ngay (hien co 60)`** — một câu trả lời thẳng thắn mà rất ít báo cáo kinh doanh
   dám đưa ra: *"dữ liệu hiện có chưa đủ để nói điều bạn muốn nói."*

---

## 11. Tự thử

1. Ở thí dụ 4.1, đổi độ tin cậy sang 99% rồi 99,9%. Khoảng rộng thêm bao nhiêu phần trăm?
   Với 99,9% thì $z$ bằng bao nhiêu?
2. Ở thí dụ 4.4 (5 vùng Lâm Đồng), thêm hai quan sát nữa: 28 và 30. Khoảng tin cậy hẹp lại
   bao nhiêu? Có phải nhờ $n$ tăng, hay còn vì $s$ giảm?
3. So sánh khoảng Student với khoảng chuẩn ở cùng dữ liệu: thay `t_quantile(0.975, n-1)` bằng
   `Z.inv_cdf(0.975)` trong phần Góc QTKD. Với $n = 60$ chênh bao nhiêu? Còn nếu chỉ lấy 5 ngày đầu?
4. Trong mô phỏng ở mục 3, đổi `NS` từ 10 lên 100. Tỷ lệ trúng có gần 95% hơn không?
   Rồi thử `t_quantile` → `Z.inv_cdf` với `NS = 5` — tỷ lệ trúng tụt xuống bao nhiêu?
   (Đây là lý do phải dùng Student khi $n$ nhỏ.)
5. Ở thí dụ 4.6, thử với $f$ rất nhỏ: $n = 50$, $m = 1$. So công thức (4.16) và (4.15).
   Cận dưới của (4.16) có âm không? Kiểm điều kiện $nf > 5$.
6. Viết hàm tính **cỡ mẫu cần thiết cho khoảng tỷ lệ**: cho trước $\varepsilon$ và độ tin cậy,
   trả về $n$ (dùng $f = 0{,}5$ cho trường hợp xấu nhất). Dựng lại bảng ±3% ở mục 7.
7. Với dữ liệu doanh thu, tính khoảng tin cậy 95% **riêng cho ngày trong tuần** và
   **riêng cho cuối tuần**. Hai khoảng có chồng lấn không? Điều đó gợi ý gì? (Bài 13 sẽ trả lời
   chặt chẽ bằng kiểm định.)

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)          | Tiếng Anh                              | Ghi chú                              |
| -------------------------------- | -------------------------------------- | ------------------------------------ |
| Ước lượng điểm                   | Point estimate                         | một con số $\hat\theta$              |
| Ước lượng khoảng, khoảng tin cậy | Interval estimate, Confidence interval |                                      |
| Độ tin cậy                       | Confidence level                       | $1-\alpha$                           |
| Mức ý nghĩa                      | Significance level                     | $\alpha$                             |
| Độ chính xác của ước lượng       | Margin of error                        | $\varepsilon$                        |
| Ước lượng không chệch            | Unbiased estimator                     | $E\hat\theta = \theta$               |
| Ước lượng chệch                  | Biased estimator                       |                                      |
| Sai số hệ thống / ngẫu nhiên     | Systematic / Random error              |                                      |
| Ước lượng vững                   | Consistent estimator                   | $\hat\theta \xrightarrow{xs} \theta$ |
| Ước lượng hiệu quả               | Efficient estimator                    | phương sai bé nhất                   |
| Giới hạn Cramér – Rao            | Cramér–Rao bound                       | (3.2)                                |
| Lượng thông tin Fisher           | Fisher information                     |                                      |
| Hàm tổn thất / rủi ro            | Loss / Risk function                   |                                      |
| Phương pháp mômen                | Method of moments                      |                                      |
| Phương pháp hợp lý nhất          | Maximum likelihood (MLE)               |                                      |
| Hàm hợp lý                       | Likelihood function                    | $L(x,\theta)$                        |
| Khoảng đối xứng / phải / trái    | Two-sided / lower / upper bound        |                                      |
| Khoảng dự báo                    | Prediction interval                    | 📚 mục 9, khác khoảng tin cậy        |
| Khoảng tin (Bayes)              | Credible interval                      | 📚 mục 9                             |

⚠️ **Ba khoảng khác nhau, đừng nhầm:**

| Khoảng                     | Nói về                          | Độ rộng         |
| -------------------------- | ------------------------------- | --------------- |
| **Tin cậy** (confidence)   | tham số $a$ của tổng thể        | hẹp nhất        |
| **Dự báo** (prediction)    | **một quan sát mới**            | rộng hơn nhiều  |
| **Tin** (credible, Bayes) | tham số, coi là biến ngẫu nhiên | tuỳ tiên nghiệm |

---

## 13. Câu hỏi tự kiểm tra

1. Phân biệt **không chệch**, **vững**, **hiệu quả**. Cho ví dụ một ước lượng chệch nhưng vững.
2. Vì sao ước lượng hợp lý nhất của $\sigma^2$ (thí dụ 3.4) lại là ước lượng **chệch**?
   Điều đó có làm phương pháp hợp lý nhất trở nên vô dụng không?
3. Ba đại lượng trong công thức (4.10) là gì? Nếu muốn giảm $\varepsilon$ một nửa mà giữ nguyên
   $1-\alpha$ thì $n$ phải đổi thế nào?
4. Khi nào dùng phân phối Student thay cho chuẩn? Với $n = 50$ thì chênh lệch có đáng kể không?
5. Một mẫu 25 sản phẩm cho $\overline{X} = 100$ g, $s = 5$ g. Tìm khoảng tin cậy 95% cho khối lượng
   trung bình. Nếu đề nói "biết $\sigma = 5$ g" thì khoảng đổi thế nào?
6. Khảo sát 1.000 người, 380 người thích sản phẩm A.
   a) Khoảng tin cậy 95% cho tỷ lệ thích A?
   b) Kiểm điều kiện $nf > 5$ và $n(1-f) > 5$.
   c) Muốn sai số ±2% thì cần bao nhiêu người?
7. Vì sao khoảng tin cậy cho phương sai **không đối xứng**? Vì sao phân vị lớn nằm ở mẫu số của
   cận dưới?
8. Giải thích vì sao câu *"xác suất để kỳ vọng thật nằm trong khoảng (10; 20) là 95%"* là sai.
   Phát biểu lại cho đúng.
9. Một báo cáo viết: *"khảo sát 500 khách hàng, mức hài lòng trung bình 8,2/10 với khoảng tin cậy
   95% là (8,0; 8,4). Vậy 95% khách hàng có mức hài lòng từ 8,0 đến 8,4."* Sai ở đâu?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 11 — ƯỚC LƯỢNG ĐIỂM VÀ KHOẢNG TIN CẬY     (Ch. IV §3–4, tr.133–157) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BA TÍNH CHẤT CỦA ƯỚC LƯỢNG ĐIỂM                                         ║
║      KHÔNG CHỆCH  E θ̂ = θ          "nhắm đúng tâm"                       ║
║      VỮNG         θ̂ →xs θ           "nhiều dữ liệu thì đúng"             ║
║      HIỆU QUẢ     V θ̂ bé nhất       "chụm nhất" (giới hạn Cramér–Rao)    ║
║      ⚠ chệch mà chụm = nguy hiểm nhất (rất tự tin vào số sai)            ║
║                                                                          ║
║      X̄ ✓không chệch ✓vững ✓hiệu quả   |   s² (chia n−1) ✓không chệch     ║
║      f  ✓không chệch ✓vững ✓hiệu quả   |   Ŝ² (chia n)   ✗CHỆCH ✓vững    ║
║                                                                          ║
║  BA PHƯƠNG PHÁP  đặc trưng mẫu | mômen | HỢP LÝ NHẤT (MLE)               ║
║      MLE: cực đại L(x,θ) = ∏f(xᵢ,θ)  → giải ∂lnL/∂θ = 0                  ║
║      ⚠ MLE của σ² ra Ŝ² (chia n) — CHỆCH!                                ║
║                                                                          ║
║  ⭐ QUY TRÌNH 4 BƯỚC CHO MỌI KHOẢNG TIN CẬY                              ║
║      1. tìm thống kê G có PHÂN PHỐI không chứa θ                         ║
║      2. chọn α₁ + α₂ = α, tra hai phân vị                                ║
║      3. P(g_α₁ < G < g_{1−α₂}) = 1 − α                                   ║
║      4. biến đổi tương đương về  θ₁ < θ < θ₂                             ║
║                                                                          ║
║  BỐN BÀI TOÁN — BỐN CÔNG THỨC                                            ║
║  ┌───┬──────────────┬────────────────────┬──────────────────────────┐    ║
║  │ 1 │ a, BIẾT σ    │ Z ~ N(0;1)         │ X̄ ± (σ/√n)·z_{1−α/2}     │    ║
║  │ 2 │ a, CHƯA BIẾT │ T ~ t(n−1)         │ X̄ ± (s/√n)·t_{n−1;1−α/2} │    ║
║  │ 3 │ tỷ lệ p      │ Z ≈ N(0;1)         │ f ± √(f(1−f)/n)·z        │    ║
║  │ 4 │ phương sai σ²│ χ² ~ χ²(n−1)       │ (n−1)s²/χ²  ← xem dưới   │    ║
║  └───┴──────────────┴────────────────────┴──────────────────────────┘    ║
║                                                                          ║
║      Bài toán 4:  ( (n−1)s²/χ²_{n−1;1−α/2} ;  (n−1)s²/χ²_{n−1;α/2} )     ║
║      ⚠ KHÔNG đối xứng | phân vị LỚN ở mẫu số cận DƯỚI                    ║
║                                                                          ║
║  BA KIỂU KHOẢNG                                                          ║
║      ĐỐI XỨNG α₁=α₂=α/2  → NGẮN NHẤT, mặc định                           ║
║      PHẢI     α₁=0       → "ít nhất bao nhiêu"                           ║
║      TRÁI     α₂=0       → "tối đa bao nhiêu"                            ║
║                                                                          ║
║  z HAY DÙNG   90%: 1,645 | 95%: 1,960 | 99%: 2,576   (hai phía)          ║
║               90%: 1,282 | 95%: 1,645 | 99%: 2,326   (một phía)          ║
║                                                                          ║
║  ⭐ CÔNG THỨC CỠ MẪU     ε = (σ/√n)·z    ⟹    n ≥ (σz/ε)²               ║
║      biết 2 trong 3 (ε, n, 1−α) → suy ra cái thứ 3                       ║
║      gấp đôi chính xác ⟹ gấp BỐN cỡ mẫu (luật căn bậc hai)              ║
║      thăm dò dư luận: n = 1.000 → ε ≈ ±3%, KHÔNG phụ thuộc dân số        ║
║                                                                          ║
║  ⚠⚠ "95%" NGHĨA LÀ GÌ                                                    ║
║      SAI : "xác suất a nằm trong (25,04; 33,36) là 95%"                  ║
║            (a cố định, khoảng cũng cố định → không có xác suất)          ║
║      ĐÚNG: "lặp quy trình nhiều lần thì 95% số khoảng chứa a"            ║
║      → 95% là tính chất của QUY TRÌNH, không phải của MỘT khoảng         ║
║      → mô phỏng 1000 lần cho 94,6%                                       ║
║                                                                          ║
║  ⚠ ĐÍNH CHÍNH  tr.143 thí dụ 4.2: n = 144 (sách in 142)                  ║
║                tr.144 thí dụ 4.3: (13,68; 20,92) — sách in               ║
║                        (136,77; 209,23), thiếu √ và sai dấu phẩy         ║
║      MẸO KIỂM: khoảng cho kỳ vọng LUÔN đối xứng quanh X̄                  ║
║                                                                          ║
║  💼 QTKD  tính cỡ mẫu TRƯỚC khi thu dữ liệu, không phải sau              ║
║          "tối đa/tối thiểu" trong đề → khoảng MỘT PHÍA                   ║
║          khoảng tin cậy chỉ đo sai số LẤY MẪU, không cứu mẫu thiên lệch  ║
║          ước lượng PHƯƠNG SAI kém chính xác hơn ước lượng KỲ VỌNG        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương IV §3–§4, tr. 133–157.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Đính chính thí dụ 4.2 (tr. 143): sách in `≈142`, giá trị đúng là **144**. Đã đối chiếu bản quét gốc.
- Đính chính thí dụ 4.3 (tr. 144): sách in $\frac{4,5}{14}$ (thiếu dấu căn) và kết quả
  `(136,77; 209,23)` (sai dấu phẩy 10 lần). Kết quả đúng: **(13,68; 20,92)**.
- Mục 9 (ý nghĩa của độ tin cậy) khai triển từ đoạn cảnh báo của giáo trình ở tr. 146.
  Phân biệt khoảng tin cậy / dự báo / khoảng tin Bayes là bổ sung.
- Bảng phân vị Student và chi bình phương trong code được tính lại từ định nghĩa, đối chiếu khớp
  với bảng 3 (tr. 233) và bảng 4 (tr. 234) của phụ lục.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 10 — Mẫu và thống kê mô tả](bai_10_mau_va_thong_ke_mo_ta.md) ·
Bài sau: Bài 12 — Kiểm định giả thuyết, một mẫu
