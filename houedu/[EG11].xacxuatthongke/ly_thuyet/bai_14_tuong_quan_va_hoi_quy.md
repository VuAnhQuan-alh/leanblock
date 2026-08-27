# Bài 14 — Tương quan và phân tích hồi quy

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương VI**, tr. 194–229.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này nêu **ba chỗ số liệu không khớp** trong thí dụ 1.1, 1.3 và 2.3.
> 📌 **Cần đọc trước:** [Bài 8](bai_08_bien_ngau_nhien_hai_chieu_va_tuong_quan.md) · [Bài 11](bai_11_uoc_luong_diem_va_khoang_tin_cay.md) · [Bài 12](bai_12_kiem_dinh_gia_thuyet_mot_mau.md) · [Bài 13](bai_13_kiem_dinh_nhieu_mau_va_anova.md)

**Bài cuối của khoá học**, và cũng là bài dùng nhiều nhất trong công việc.

Bài 8 mục 7 đã hẹn: *"hồi quy chính là bài toán ước lượng $E(Y \mid X = x)$ từ dữ liệu"*.
Giờ ta làm việc đó. Giáo trình mở đầu Chương VI (tr. 194):

> "Nội dung chính của chương này là **xác định sự phụ thuộc giữa các biến ngẫu nhiên**...
> Trong trường hợp chúng không độc lập, cần xác định **mức độ phụ thuộc** và **quan hệ hàm** giữa
> các biến."

Hai vế đó là hai nửa của bài:

| Phần              | Câu hỏi                                              | Công cụ                |
| ----------------- | ---------------------------------------------------- | ---------------------- |
| **§1 Tương quan** | *"hai biến có liên hệ không, mạnh yếu thế nào?"*     | hệ số $r$              |
| **§2 Hồi quy**    | *"liên hệ đó là hàm gì, dùng để dự báo được không?"* | đường thẳng $y = ax+b$ |

## Mục lục

1. [Hệ số tương quan mẫu](#1-hệ-số-tương-quan-mẫu)
2. [Kiểm định tính độc lập](#2-kiểm-định-tính-độc-lập)
3. [Kiểm định giả thuyết về hệ số tương quan](#3-kiểm-định-giả-thuyết-về-hệ-số-tương-quan)
4. [Mô hình hồi quy tuyến tính](#4-mô-hình-hồi-quy-tuyến-tính)
5. [Ước lượng hệ số bằng bình phương cực tiểu](#5-ước-lượng-hệ-số-bằng-bình-phương-cực-tiểu)
6. [Khoảng tin cậy và kiểm định hệ số](#6-khoảng-tin-cậy-và-kiểm-định-hệ-số)
7. [Hệ số xác định](#7-hệ-số-xác-định)
8. [Hồi quy phi tuyến và hồi quy bội](#8-hồi-quy-phi-tuyến-và-hồi-quy-bội)
9. [📚 Bảy sai lầm khi dùng hồi quy](#9--bảy-sai-lầm-khi-dùng-hồi-quy)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Hệ số tương quan mẫu

Chương III (bài 8) đã định nghĩa hệ số tương quan **lý thuyết**:

$$\rho_{XY} = \frac{\mu_{XY}}{\sigma_X \sigma_Y} \tag{1.1}$$

với ba tính chất giáo trình nhắc lại (tr. 195):

$$
\begin{aligned}
&\text{(i)} && |\rho_{XY}| \le 1 \\
&\text{(ii)} && |\rho_{XY}| = 1 \iff Y = aX + b \text{ (tuyến tính hoàn hảo)} \\
&\text{(iii)} && X, Y \text{ độc lập} \Rightarrow \rho_{XY} = 0 \text{ (chiều ngược lại nói chung SAI)}
\end{aligned}
$$

Và nhắc lại **ngoại lệ chuẩn**: *"Nếu có thêm giả thiết chuẩn của $X$ và $Y$ thì $\rho_{XY} = 0$
tương đương với khẳng định $X$ và $Y$ độc lập."*

### Ước lượng bằng $r$

Trong thực hành không tính được $\rho$, phải ước lượng bằng **hệ số tương quan mẫu**:

$$r = \frac{\displaystyle\sum_i (x_i - \overline{X})(y_i - \overline{Y})}
{(n-1)\,s_x\,s_y}
= \frac{\displaystyle\sum_i x_i y_i - n\overline{X}\,\overline{Y}}{(n-1)\,s_x\,s_y} \tag{1.2}$$

Giáo trình cho **quy tắc thực hành** (tr. 196):

> "$r$ rất khó bằng $\pm 1$ (hoặc 0). Vì vậy trong thực hành nếu $|r| > 0{,}8$ ta đã có thể coi là
> **có mối quan hệ dạng tuyến tính** (xấp xỉ tuyến tính) giữa hai biến đang xét."

**Hệ số xác định mẫu** (tr. 197): $\ \beta = r^2$, với $0 \le r^2 \le 1$.

### Thí dụ 1.1 (tr. 197)

> Tính các đặc trưng mẫu của 15 cặp $(x_i, y_i)$.

Dữ liệu lưu ở [cap_so_lieu_15.csv](../thuc_hanh/du_lieu/cap_so_lieu_15.csv).

⭐ **Mẹo tính tay của giáo trình:** *"Để tránh phải tính toán với các số quá lớn, các giá trị của $y$
được trừ đi 42,2."* Vì phép tịnh tiến không đổi phương sai (bài 6 mục 4):

$$s_{y'} = s_y, \qquad r_{xy'} = r_{xy}$$

| Đại lượng       |        Giá trị |           Sách |
| --------------- | -------------: | -------------: |
| $\overline{X}$  |           5,83 |         5,83 ✓ |
| $\overline{Y}$  |           79,9 |         79,9 ✓ |
| $s_x^2$ / $s_x$ |   13,69 / 3,70 |   13,7 / 3,7 ✓ |
| $s_y^2$ / $s_y$ | 255,60 / 15,99 | 255,6 / 16,0 ✓ |
| **$r$**         |    **−0,5422** |      −0,5417 ✓ |
| $r^2$           |         0,2939 |       0,2934 ✓ |

⚠️ **Ghi chú số liệu:** hàng "Tổng" của bảng in $\sum x_i y_i' = 2489{,}81$, nhưng dòng tính toán
ngay bên dưới dùng **2849,81**. Cộng lại từ cột thứ sáu của chính bảng đó được **2849,81** —
con số dùng trong phép tính là đúng, hàng Tổng in đảo hai chữ số.

(Nếu dùng 2489,81 thì $r = -0{,}924$, khác hẳn kết quả 0,5417 mà sách công bố.)

### 💼 Góc QTKD — thang đọc $r$

Đã cho ở bài 8 mục 6. Nhắc lại điểm quan trọng nhất: **$r$ chỉ đo quan hệ TUYẾN TÍNH.**
Quan hệ hình chữ U (giá bán vs lợi nhuận) cho $r \approx 0$ dù rất chặt chẽ.

⭐ **Luôn vẽ biểu đồ phân tán trước khi tính $r$.**

---

## 2. Kiểm định tính độc lập

$r$ tính từ mẫu nên **luôn khác 0** kể cả khi $\rho = 0$. Cần kiểm định.

**Bài toán.** $H_0: \rho_{XY} = 0$ với $H_1: \rho_{XY} \ne 0$ (giả thiết $X$, $Y$ chuẩn).

**Tiêu chuẩn (1.3):**

$$K = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}} \ \sim t(n-2) \text{ khi } H_0 \text{ đúng}$$

Miền tới hạn (1.4): $|K_{tn}| > t_{n-2;\,1-\alpha/2}$.

Giáo trình nêu ý nghĩa (tr. 201): *"Nếu giả thuyết về tính độc lập của $X$ và $Y$ chấp nhận được,
**ít có lý do để xem xét đồng thời hai biến đó**."*

💼 Nói cách khác: **kiểm định này quyết định có nên làm hồi quy hay không.** Nếu không bác bỏ được
$H_0$, đừng vẽ đường hồi quy — nó vô nghĩa.

### Thí dụ 1.3 (tr. 201)

> $n = 8$ cặp số liệu. $\alpha = 0{,}05$: kiểm định tính độc lập.

$\sum(x_i-\overline{X})^2 = 48{,}125$, $\sum(y_i-\overline{Y})^2 = 0{,}6780$,
$\sum(x_i-\overline{X})(y_i-\overline{Y}) = -0{,}2795$

$$r = \frac{-0{,}2795}{\sqrt{48{,}125 \times 0{,}678}} = \mathbf{-0{,}0489}$$

$$K_{tn} = \frac{-0{,}0489\sqrt{6}}{\sqrt{1-0{,}0489^2}} = \mathbf{-0{,}12}$$

$t_{6;\,0{,}975} = 2{,}447$. Vì $|-0{,}12| < 2{,}447$ → **chấp nhận** $H_0$: coi như độc lập.

⚠️ **Ghi chú:** sách in số hạng giữa là $-0{,}2975$; tính lại từ dữ liệu được $-0{,}2795$
(đảo hai chữ số). Nhưng $r = -0{,}0489$ mà sách công bố lại khớp với **−0,2795** — nên kết quả
cuối cùng đúng.

### ⭐ Thí dụ 1.4 (tr. 202) — bài học đáng giá nhất chương VI

> Kiểm định tính độc lập cho bộ số liệu thí dụ 1.1 ($n = 15$, $r = -0{,}5417$), $\alpha = 0{,}01$.

$$K_{tn} = \frac{-0{,}5417\sqrt{13}}{\sqrt{1-0{,}5417^2}} = \mathbf{-2{,}32}$$

| $\alpha$ | $t_{13;\,1-\alpha/2}$ | So sánh           | Kết luận                              |
| -------- | --------------------: | ----------------- | ------------------------------------- |
| **0,01** |                  3,01 | $2{,}32 < 3{,}01$ | **chấp nhận** $H_0$ (coi như độc lập) |
| **0,05** |                  2,16 | $2{,}32 > 2{,}16$ | **bác bỏ** $H_0$ (có tương quan)      |

Giáo trình bình luận thẳng thắn (tr. 202):

> "Ở đây ta thấy $r = -0{,}5417$ khác khá xa 0 mà ta vẫn chưa thể khẳng định là giữa $X$ và $Y$
> có quan hệ nào đó. Nguyên nhân cũng có thể là **kích thước mẫu quá bé** chăng?...
> Như vậy có thể thấy rằng ước lượng hệ số tương quan **phụ thuộc tới mức độ nào vào kích thước mẫu**
> và những kết luận không dựa trên những tiêu chuẩn thống kê chính xác và hợp lý sẽ dẫn tới
> **những sai lầm nguy hiểm**."

⭐ **Hai bài học:**

1. **$r$ lớn chưa chắc có ý nghĩa.** $r = -0{,}54$ nghe "khá mạnh" nhưng với $n = 15$ vẫn có thể là
   ngẫu nhiên.
2. **Kết luận phụ thuộc vào $\alpha$ bạn chọn.** Đây chính là lý do bài 12 mục 9 nhấn mạnh:
   **chọn $\alpha$ trước khi nhìn dữ liệu**.

💼 Ngưỡng $|r|$ cần thiết để có ý nghĩa ở $\alpha = 0{,}05$ giảm nhanh theo $n$:

|  $n$ |     $ | r | $ tối thiểu |
| ---: | ----: |
|   10 | 0,632 |
|   20 | 0,444 |
|   30 | 0,361 |
|  100 | 0,197 |
| 1000 | 0,062 |

⚠️ Dòng cuối là cảnh báo: với $n = 1000$, $r = 0{,}07$ đã "có ý nghĩa thống kê" — nhưng
$r^2 = 0{,}005$, tức mô hình giải thích được **0,5%**. Có ý nghĩa thống kê ≠ hữu ích.

---

## 3. Kiểm định giả thuyết về hệ số tương quan

**Bài toán tổng quát hơn:** $H_0: \rho = \rho_0$ (không nhất thiết bằng 0).

Vấn đề: phân phối của $r$ **lệch mạnh** khi $\rho$ xa 0, nên không dùng $t$ được.
Giải pháp của Fisher — **phép biến đổi $Z$** (1.5):

$$Z = \frac12\ln\frac{1+r}{1-r}$$

Khi $n \to \infty$, $Z$ tiệm cận chuẩn với:

$$EZ \approx \frac12\ln\frac{1+\rho_0}{1-\rho_0} + \frac{\rho_0}{2(n-1)}, \qquad
VZ = \frac{1}{n-3}$$

**Tiêu chuẩn:** $\ K = \dfrac{Z - EZ}{\sqrt{VZ}} \sim N(0;1)$, miền tới hạn đối xứng (1.6).

Giáo trình cho mốc: *"Trong thực hành với $n > 50$ đã có thể chấp nhận kết quả trên."*

### Thí dụ 1.5 (tr. 203)

> 150 cặp số liệu thuỷ văn cho $r = 0{,}5273$. $\alpha = 0{,}05$: có thể cho rằng $\rho = 0{,}5$ không?

$$Z = \frac12\ln\frac{1{,}5273}{0{,}4727} = 0{,}5864, \qquad
EZ = \frac12\ln 3 + \frac{0{,}5}{298} = 0{,}5510, \qquad \sqrt{VZ} = \frac{1}{\sqrt{147}} = 0{,}0825$$

$$K_{tn} = \frac{0{,}5864 - 0{,}5510}{0{,}0825} = \mathbf{0{,}43}$$

$|0{,}43| < 1{,}96$ → **chấp nhận** $\rho = 0{,}5$.

**So sánh hai hệ số tương quan (tr. 204):** cũng dùng biến đổi $Z$:

$$K = \frac{Z_1 - Z_2}{\sqrt{VZ_1 + VZ_2}} \sim N(0;1)$$

💼 Dùng để trả lời: *"quan hệ giữa chi quảng cáo và doanh số ở miền Bắc có chặt hơn ở miền Nam không?"*

---

## 4. Mô hình hồi quy tuyến tính

Sang §2. **Mô hình (2.4):**

$$Y_i = aX_i + b + \varepsilon_i, \qquad i = \overline{1,n}$$

**Ba giả thiết (2.3a–c):**

$$
\begin{aligned}
&\text{(a)} && E\varepsilon_i = 0 && \text{sai số không thiên lệch} \\
&\text{(b)} && V\varepsilon_i = \sigma^2 \ \forall i, \quad E(\varepsilon_i\varepsilon_j) = 0 \ (i \ne j)
&& \text{cùng phương sai, không tương quan} \\
&\text{(c)} && \varepsilon_i \sim N(0; \sigma^2) && \text{chuẩn (chỉ cần khi suy luận)}
\end{aligned}
$$

⭐ **Giả thiết (b) chính là "phương sai thuần nhất"** đã gặp ở bài 8 mục 8 — và ở đó ta đã thấy nó
**tự động đúng** nếu $(X,Y)$ có phân phối chuẩn hai chiều. Không phải giả định tuỳ tiện.

Cũng ở bài 8 mục 8, hàm hồi quy lý thuyết của chuẩn hai chiều là

$$E(Y \mid X = x) = a_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - a_X)$$

— **một đường thẳng**. Mô hình (2.4) chính là dạng mẫu của công thức đó.

---

## 5. Ước lượng hệ số bằng bình phương cực tiểu

**Nguyên lý:** chọn $\hat{a}$, $\hat{b}$ cực tiểu tổng bình phương sai số:

$$\sum_{i=1}^{n}\left(y_i - \hat{a}x_i - \hat{b}\right)^2 \to \min$$

Lấy đạo hàm riêng theo $\hat a$, $\hat b$ rồi cho bằng 0, được **(2.6)**:

$$\boxed{\hat{a} = \frac{\sum(x_i - \overline{X})(y_i - \overline{Y})}{\sum(x_i - \overline{X})^2} = \frac{S_{xy}}{S_{xx}},
\qquad \hat{b} = \overline{Y} - \hat{a}\,\overline{X}}$$

⭐ **Hai nhận xét đáng nhớ:**

1. $\hat{a} = r\dfrac{s_y}{s_x}$ — hệ số góc là **hệ số tương quan đã đổi thang đo**.
   Giống hệt công thức lý thuyết ở bài 8 mục 8.
2. $\hat b = \overline{Y} - \hat a \overline{X}$ nghĩa là **đường hồi quy luôn đi qua điểm
   $(\overline{X}, \overline{Y})$** — một cách kiểm tra bài làm rất nhanh.

**Ước lượng phương sai sai số (2.9)** — giáo trình cảnh báo rõ (tr. 208): ước lượng **không chệch**
**không phải** là chia $n$ mà là:

$$s^2 = \frac{1}{n-2}\sum_{i=1}^{n}\hat{\varepsilon}_i^2 = \frac{1}{n-2}\sum(y_i - \hat{a}x_i - \hat{b})^2$$

⚠️ **Chia $n-2$**, mất **hai** bậc tự do vì ước lượng **hai** tham số $a$ và $b$.
(So bài 10 mục 6: chia $n-1$ vì ước lượng một tham số.)

**Công thức tính nhanh (2.11):**

$$\sum \hat{\varepsilon}_i^2 = S_{yy} - \hat{a}\,S_{xy}$$

📚 Giáo trình cũng nêu (tr. 208): với giả thiết chuẩn (2.3c), **ước lượng hợp lý nhất trùng với
bình phương cực tiểu** — hai nguyên lý khác nhau cho cùng kết quả. (Nhưng ước lượng hợp lý nhất
của $\sigma^2$ lại chia $n$, tức **chệch** — đúng như bài 11 mục 3 đã cảnh báo.)

**Tính chất của ước lượng (tr. 210–211):** $\hat a$, $\hat b$ là ước lượng **không chệch** và
**hiệu quả** của $a$, $b$, với

$$V\hat{a} = \frac{\sigma^2}{S_{xx}}, \qquad V\hat{b} = \sigma^2\frac{\sum x_i^2}{n\,S_{xx}} \tag{2.12}$$

⭐ Chú ý $V\hat{a}$ tỷ lệ nghịch với $S_{xx}$ — **$x$ trải rộng thì ước lượng hệ số góc chính xác hơn**.
Đây là nguyên lý thiết kế thí nghiệm: muốn đo tác động của quảng cáo cho chuẩn, hãy **thử nhiều mức
chi khác nhau**, đừng chi đều đều.

### Thí dụ 2.1 (tr. 209)

> Trọng lượng cơ thể ($X$, kg) và lượng huyết tương ($Y$, lít) của 8 người đàn ông.
> Xây dựng đường hồi quy tuyến tính mẫu.

Dữ liệu: [huyet_tuong.csv](../thuc_hanh/du_lieu/huyet_tuong.csv).

$$S_{xy} = 8{,}96, \quad S_{xx} = 205{,}38, \quad S_{yy} = 0{,}6780, \quad r = 0{,}76$$

$$\hat{a} = \frac{8{,}96}{205{,}38} = \mathbf{0{,}0436}, \qquad
\hat{b} = 3{,}0025 - 0{,}0436 \times 66{,}875 = \mathbf{0{,}0857}$$

$$\boxed{y = 0{,}0436x + 0{,}0857}$$

$$s^2 = \frac{1}{6}(0{,}6780 - 0{,}0436 \times 8{,}96) = \mathbf{0{,}0479}, \qquad s = 0{,}219$$

**Đọc kết quả:** mỗi kg trọng lượng cơ thể tương ứng thêm **0,0436 lít** huyết tương.

⚠️ Hệ số chặn $\hat b = 0{,}0857$ nghĩa là "người nặng 0 kg có 0,086 lít huyết tương" — **vô nghĩa**.
Đó là chuyện bình thường: hệ số chặn thường **không diễn giải được** vì $x = 0$ nằm ngoài vùng
dữ liệu (mục 9 ý 4).

---

## 6. Khoảng tin cậy và kiểm định hệ số

Với giả thiết chuẩn (2.3c), giáo trình cho phân phối của các ước lượng (2.15)–(2.16):

$$\hat{a} \sim N(a; \sigma_a^2), \qquad \hat{b} \sim N(b; \sigma_b^2), \qquad
\frac{(n-2)s^2}{\sigma^2} \sim \chi^2(n-2)$$

Kết hợp lại được thống kê Student — **hoàn toàn giống bài 11**:

$$\frac{\hat{a} - a}{s/\sqrt{S_{xx}}} \sim t(n-2)$$

**Khoảng tin cậy (2.18a–c):**

$$\hat{a} \pm t_{n-2;\,1-\alpha/2}\cdot\frac{s}{\sqrt{S_{xx}}}$$

$$\hat{b} \pm t_{n-2;\,1-\alpha/2}\cdot s\sqrt{\frac{\sum x_i^2}{n\,S_{xx}}}$$

$$\left(\frac{(n-2)s^2}{\chi^2_{n-2;\,1-\alpha/2}};\ \frac{(n-2)s^2}{\chi^2_{n-2;\,\alpha/2}}\right)$$

### Thí dụ 2.3 (tr. 214) — khoảng tin cậy 95%

$t_{6;\,0{,}975} = 2{,}447$, $\chi^2_{6;\,0{,}975} = 14{,}449$, $\chi^2_{6;\,0{,}025} = 1{,}237$:

| Tham số    | Khoảng           | Sách                |
| ---------- | ---------------- | ------------------- |
| $a$        | (0,0063; 0,0810) | (0,0062; 0,0810) ✓  |
| $b$        | (−2,420; 2,591)  | (−2,8049; 2,9763) ⚠️|
| $\sigma^2$ | (0,0199; 0,2322) | (0,0199; 0,2325) ✓  |

⚠️ **Ghi chú:** khoảng cho $b$ tính lại được (−2,420; 2,591), hẹp hơn con số in trong sách.
Sách cũng in $\sum x_i^2 = 35893{,}5$ trong công thức trong khi thí dụ 2.1 cho **35983,5** —
đảo hai chữ số. Nhưng dù dùng số nào thì kết quả vẫn không ra được (−2,8049; 2,9763).
**Kết luận không đổi:** cả hai khoảng đều **chứa 0**, nên hệ số chặn không khác 0 có ý nghĩa.

### Thí dụ 2.4 (tr. 216) — kiểm định quan trọng nhất

> $\alpha = 0{,}05$, kiểm định $H_0: a = 0$ với $H_1: a \ne 0$.

**Tiêu chuẩn (2.19):**

$$K = \frac{\hat{a} - a_0}{s/\sqrt{S_{xx}}} = \frac{0{,}043615}{0{,}015268} = \mathbf{2{,}857}$$

$t_{6;\,0{,}975} = 2{,}447$. Vì $2{,}857 > 2{,}447$ → **bác bỏ** $H_0$.

⭐ Giáo trình giải thích ý nghĩa (tr. 216):

> "Giả thuyết $H_0: a = 0$ có **ý nghĩa rất quan trọng** vì nó cho phép **chấp nhận hay bác bỏ
> sự có mặt của biến $X$ trong mô hình** đang xét."

Nếu $a = 0$ thì $Y = b + \varepsilon$ — biến $X$ **không đóng vai trò gì**. Đây là kiểm định
đầu tiên phải làm với mọi mô hình hồi quy.

**Ba cách kiểm tương đương** — giáo trình nêu, đáng nhớ:

| Cách                   | Điều kiện bác bỏ               | Kết quả                  |
| ---------------------- | ------------------------------ | ------------------------ |
| Thống kê $t$           | $\|K\| > t_{n-2;\,1-\alpha/2}$ | $2{,}857 > 2{,}447$ ✓    |
| Khoảng tin cậy cho $a$ | khoảng **không chứa 0**        | $(0{,}0063; 0{,}0810)$ ✓ |
| Thống kê $F$           | $K^2 > F_{1,n-2;\,1-\alpha}$   | $8{,}16 > 5{,}99$ ✓      |

Cách thứ ba dùng quan hệ $t(m)^2 \sim F(1,m)$ (bài 7 mục 8). Giáo trình cho công thức:

$$K^2 = \frac{r^2(n-2)}{1-r^2}$$

⭐ Ba cách **luôn cho cùng kết luận** — đây là cách kiểm tra bài làm rất tốt.

---

## 7. Hệ số xác định

Giáo trình dùng lại **đúng ý tưởng tách tổng bình phương của ANOVA** (bài 13 mục 4), công thức (2.13):

$$\underbrace{\sum(y_i - \overline{Y})^2}_{\text{TOÀN BỘ } S_{yy}}
= \underbrace{\sum(\hat{y}_i - \overline{Y})^2}_{\text{do HỒI QUY giải thích}}
+ \underbrace{\sum(y_i - \hat{y}_i)^2}_{\text{DƯ, không giải thích được}}$$

**Định nghĩa (2.20):**

$$\boxed{r^2 = \frac{\sum(\hat{y}_i - \overline{Y})^2}{\sum(y_i - \overline{Y})^2}
= 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \overline{Y})^2}}$$

Giáo trình nêu ý nghĩa (tr. 217):

> "$r^2$ cho thấy **tỷ lệ tổng bình phương sai số tiên nghiệm được giải thích bởi mô hình tuyến tính**
> (bởi biến $X$)... $1 - r^2$ cho ta **phần không được giải thích** bởi mô hình tuyến tính."

Và trường hợp hoàn hảo: *"nếu $r^2 = 1$ thì $\sum(y_i - \hat{y}_i)^2 = 0$ hay trong mọi trường hợp
$y_i = \hat{y}_i$ (mô hình chính xác)."*

⭐ **Vòng tròn khép lại.** Bài 8 mục 8 đã dẫn ra từ phân phối chuẩn hai chiều:
$V(Y \mid X) = \sigma_Y^2(1-\rho^2)$, tức $\rho^2$ = tỷ lệ bất định giải thích được.
Giờ ta thấy đúng đại lượng đó xuất hiện lại từ dữ liệu mẫu.

**Với thí dụ 2.1:** $r^2 = 0{,}576$ — trọng lượng cơ thể giải thích **57,6%** biến động của lượng
huyết tương; 42,4% còn lại do các yếu tố khác (chiều cao, tuổi, thể trạng, sai số đo).

### 💼 Góc QTKD — đọc $R^2$ cho đúng

| $R^2$     | Trong khoa học tự nhiên | Trong kinh doanh / xã hội                               |
| --------- | ----------------------- | ------------------------------------------------------- |
| > 0,9     | bình thường             | **đáng nghi** — nhiều khả năng hai biến đo cùng một thứ |
| 0,5 – 0,9 | tốt                     | rất tốt                                                 |
| 0,2 – 0,5 | yếu                     | **bình thường, vẫn dùng được**                          |
| < 0,2     | vô dụng                 | yếu nhưng có thể vẫn có ích nếu $a$ có ý nghĩa          |

⚠️ **$R^2$ thấp không có nghĩa mô hình vô dụng.** Nếu $R^2 = 0{,}3$ nhưng hệ số $a$ có ý nghĩa
thống kê và độ lớn đáng kể, mô hình vẫn cho biết **hướng và độ lớn tác động** — đủ để ra quyết định.

⚠️ Ngược lại **$R^2$ cao không có nghĩa mô hình đúng.** Ba lý do ở mục 9.

---

## 8. Hồi quy phi tuyến và hồi quy bội

Giáo trình khép chương bằng hai mở rộng (§2.5 và §3).

### Hồi quy phi tuyến

Nếu quan hệ không thẳng, dùng hàm khác — ví dụ **đa thức bậc hai**:

$$y = c_0 + c_1 x + c_2 x^2$$

⭐ **Mẹo then chốt:** đặt $x_1 = x$, $x_2 = x^2$ thì bài toán trở thành **hồi quy bội tuyến tính**
theo $(x_1, x_2)$. Phương pháp bình phương cực tiểu áp dụng y nguyên.

Tương tự với các dạng khác — **tuyến tính hoá** bằng đổi biến:

| Dạng gốc                | Đổi biến                   | Thành               |
| ----------------------- | -------------------------- | ------------------- |
| $y = c\,e^{ax}$         | $y' = \ln y$               | $y' = \ln c + ax$   |
| $y = c\,x^a$            | $x' = \ln x$, $y' = \ln y$ | $y' = \ln c + a x'$ |
| $y = \dfrac{1}{a + bx}$ | $y' = 1/y$                 | $y' = a + bx$       |

💼 Dạng thứ hai (log–log) rất hay dùng trong kinh tế: hệ số $a$ chính là **độ co giãn** —
"chi quảng cáo tăng 1% thì doanh số tăng $a$%".

### Hồi quy bội (§3, tr. 221)

$$Y = b + a_1 X_1 + a_2 X_2 + \dots + a_k X_k + \varepsilon$$

Giải bằng bình phương cực tiểu dưới dạng ma trận. Giáo trình cũng giới thiệu
**tương quan bội** và **tương quan riêng** (tr. 224).

⚠️ **Vấn đề mới xuất hiện khi có nhiều biến: đa cộng tuyến.**
Nếu hai biến giải thích tương quan mạnh với nhau (bài 8 mục 6 đã cảnh báo về $r > 0{,}95$),
các hệ số trở nên **rất không ổn định** — đổi vài quan sát là hệ số nhảy, thậm chí đổi dấu.

💼 Rất hay gặp: đưa cả "chi quảng cáo Facebook", "chi quảng cáo Google" và "tổng chi quảng cáo"
vào cùng một mô hình. Ba biến này phụ thuộc tuyến tính hoàn toàn → mô hình vô nghĩa.

📚 **Hệ số xác định hiệu chỉnh.** Thêm biến vào **luôn** làm $R^2$ tăng, kể cả biến vô dụng.
Vì thế phải dùng:

$$R^2_{\text{hiệu chỉnh}} = 1 - (1-R^2)\frac{n-1}{n-k-1}$$

Nó **phạt** việc thêm biến. So sánh hai mô hình khác số biến thì phải so $R^2$ hiệu chỉnh,
không so $R^2$ thô. (Giáo trình không nêu công thức này.)

---

## 9. 📚 Bảy sai lầm khi dùng hồi quy

Giáo trình dạy kỹ thuật; phần này bổ sung phần diễn giải — nơi hầu hết sai lầm thực tế xảy ra.

### 1. Coi tương quan là nhân quả

Đã cảnh báo ở bài 8 mục 9. Hồi quy làm sai lầm này **nặng hơn**, vì công thức $y = ax + b$ trông
như một cơ chế nhân quả.

⚠️ **Hồi quy không chứng minh nhân quả, bất kể $R^2$ cao đến đâu.** Chỉ **thí nghiệm có đối chứng**
mới làm được.

💼 *"Mỗi triệu quảng cáo mang về 2,29 triệu doanh số"* — có thể đúng, hoặc có thể chỉ là:
công ty chi nhiều quảng cáo **vào những tháng đang bán tốt**. Chiều nhân quả ngược lại.

### 2. Ngoại suy ra ngoài vùng dữ liệu

Mô hình chỉ đáng tin **trong khoảng $x$ đã quan sát**.

💼 Dữ liệu chi quảng cáo từ 20 đến 100 triệu. Dùng mô hình để dự báo khi chi **500 triệu** là sai —
thực tế luôn có **hiệu suất giảm dần**, đường thẳng không kéo dài mãi.

Đây cũng là lý do hệ số chặn $b$ thường vô nghĩa: $x = 0$ nằm ngoài vùng dữ liệu.

### 3. Nhầm khoảng tin cậy với khoảng dự báo

Hai khoảng rất khác nhau (đã nhắc ở bài 11 mục 12):

$$
\begin{aligned}
\text{Khoảng cho } E(Y|x_0): \quad & \hat{y}_0 \pm t\cdot s\sqrt{\frac{1}{n} + \frac{(x_0-\overline{X})^2}{S_{xx}}} \\
\text{Khoảng DỰ BÁO cho } y_0: \quad & \hat{y}_0 \pm t\cdot s\sqrt{1 + \frac{1}{n} + \frac{(x_0-\overline{X})^2}{S_{xx}}}
\end{aligned}
$$

Khác nhau ở **số 1** dưới căn — và nó làm khoảng rộng gấp nhiều lần (mục 10 cho thấy gấp 3,4 lần).

💼 **Lập kế hoạch cho tháng tới phải dùng khoảng DỰ BÁO.** Dùng khoảng tin cậy là tự lừa mình.

### 4. Không vẽ đồ thị

Bốn bộ dữ liệu có thể có **cùng $\overline{X}$, $\overline{Y}$, $r$, $\hat a$, $\hat b$, $R^2$**
mà hình dạng hoàn toàn khác nhau (bộ dữ liệu Anscombe kinh điển):

```
   ①  quan hệ tuyến tính     ②  quan hệ CONG        ③  tuyến tính + 1 điểm lạ
      ·  ·                       ·  ·  ·               ·                   ·
    ·  ·  ·                    ·        ·            ·  ·  ·  ·  ·
   ·  ·                       ·          ·          ·

   Cùng r = 0,816 và cùng đường hồi quy. Chỉ có ① là dùng được.
```

⭐ **Luôn vẽ: (a) biểu đồ phân tán $y$ theo $x$, (b) biểu đồ phần dư $\hat\varepsilon$ theo $\hat y$.**
Biểu đồ phần dư phải trông như **mây ngẫu nhiên**; nếu thấy hình cong hoặc hình phễu thì
giả thiết (2.3a) hoặc (2.3b) bị vi phạm.

### 5. Bỏ qua biến ẩn

Thêm một biến quan trọng vào mô hình có thể làm hệ số **đổi dấu**. Đây là nghịch lý Simpson
(bài 8 mục 9) trong hồi quy.

💼 *"Giá cao thì bán được nhiều hơn"* — nghe vô lý, nhưng xảy ra khi bỏ qua biến **chất lượng**:
sản phẩm tốt vừa đắt vừa bán chạy.

### 6. $R^2$ cao vì lý do sai

Ba nguyên nhân thường gặp:

- **Hai biến đo cùng một thứ** (doanh thu và số đơn khi giá cố định).
- **Xu hướng thời gian chung** — hai chuỗi cùng tăng theo năm sẽ có $r$ cao dù không liên quan
  (gọi là *hồi quy giả*).
- **Quá khớp** (overfitting): thêm nhiều biến vào mẫu nhỏ.

### 7. Vi phạm giả thiết mà không kiểm

| Giả thiết                              | Vi phạm điển hình       | Dấu hiệu trên biểu đồ phần dư |
| -------------------------------------- | ----------------------- | ----------------------------- |
| $E\varepsilon = 0$, quan hệ tuyến tính | quan hệ thật là cong    | phần dư có hình **cong**      |
| Cùng phương sai                        | sai số tăng theo $x$    | hình **phễu** loe ra          |
| Không tương quan                       | dữ liệu chuỗi thời gian | phần dư có **chu kỳ**         |
| Chuẩn                                  | có giá trị thái quá     | vài điểm rất xa               |

### Danh sách kiểm cho một báo cáo hồi quy

```
   ☐ Đã vẽ biểu đồ phân tán? Quan hệ có thật sự thẳng?
   ☐ Đã kiểm định H₀: a = 0? (nếu không bác bỏ được thì mô hình vô dụng)
   ☐ Đã báo cáo KHOẢNG TIN CẬY cho a, không chỉ giá trị điểm?
   ☐ R² là bao nhiêu? Đã nói rõ phần KHÔNG giải thích được?
   ☐ Dự báo có nằm trong vùng dữ liệu đã quan sát?
   ☐ Dùng khoảng DỰ BÁO (không phải khoảng tin cậy) khi dự báo một quan sát?
   ☐ Đã vẽ biểu đồ PHẦN DƯ để kiểm giả thiết?
   ☐ Có tuyên bố nhân quả nào không? Có thí nghiệm đối chứng để đỡ không?
```

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.
> Chạy từ thư mục gốc khoá học: `cd houedu/xacxuatthongke && python3 bai-14-hoi-quy.py`.
> Dùng module [thuc_hanh/bang_tra.py](../thuc_hanh/bang_tra.py).

Ba tệp dữ liệu:

| Tệp                                                                   | Nội dung                            | Nguồn               |
| --------------------------------------------------------------------- | ----------------------------------- | ------------------- |
| [cap_so_lieu_15.csv](../thuc_hanh/du_lieu/cap_so_lieu_15.csv)         | 15 cặp $(x,y)$                      | thí dụ 1.1, tr. 197 |
| [huyet_tuong.csv](../thuc_hanh/du_lieu/huyet_tuong.csv)               | trọng lượng vs huyết tương, 8 người | thí dụ 2.1, tr. 209 |
| [quang_cao_doanh_so.csv](../thuc_hanh/du_lieu/quang_cao_doanh_so.csv) | chi quảng cáo vs doanh số, 24 tháng | 💼 mô phỏng         |

Hàm `hoi_quy` ở đầu file trả về **một dict chứa mọi thứ** cần cho cả chương VI —
đúng những gì `LINEST` của Excel và `Data Analysis ▸ Regression` in ra.

```python
"""Bài 14 — Tương quan và phân tích hồi quy."""

import csv
import math
import pathlib
import sys

sys.path.append("thuc_hanh")
from bang_tra import Z, chi2_quantile, f_quantile, t_quantile, z_quantile

DATA = pathlib.Path("thuc_hanh/du_lieu")
kl = lambda bac_bo: "BAC BO H0" if bac_bo else "CHUA CO CO SO BAC BO H0"


def doc(name, cx, cy):
    with open(DATA / name, newline="") as fh:
        rows = list(csv.DictReader(fh))
    return [float(r[cx]) for r in rows], [float(r[cy]) for r in rows]


# ─────────────────────────────────────────────────────────────
# Bộ công cụ hồi quy đơn — toan bo chuong VI phan mot bien
# ─────────────────────────────────────────────────────────────
def hoi_quy(x, y):
    """Tra ve dict day du: he so, sai so, r, R^2, khoang tin cay..."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    Sxx = sum((v - mx) ** 2 for v in x)
    Syy = sum((v - my) ** 2 for v in y)
    Sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    r = Sxy / math.sqrt(Sxx * Syy)
    a = Sxy / Sxx                       # he so goc  (2.6)
    b = my - a * mx                     # he so chan
    ss_res = Syy - a * Sxy              # tong binh phuong sai so  (2.11)
    s2 = ss_res / (n - 2)               # uoc luong KHONG CHECH  (2.9)
    s = math.sqrt(s2)
    return dict(n=n, mx=mx, my=my, Sxx=Sxx, Syy=Syy, Sxy=Sxy, r=r, R2=r * r,
                a=a, b=b, s2=s2, s=s, ss_res=ss_res,
                se_a=s / math.sqrt(Sxx),
                se_b=s * math.sqrt(sum(v * v for v in x) / (n * Sxx)))


# ─────────────────────────────────────────────────────────────
# 1. HỆ SỐ TƯƠNG QUAN MẪU — Thí dụ 1.1 (tr. 197)
# ─────────────────────────────────────────────────────────────
x, y = doc("cap_so_lieu_15.csv", "x", "y")
m = hoi_quy(x, y)
print("THI DU 1.1 — 15 cap so lieu, tinh cac dac trung mau")
print(f"  n = {m['n']}   Sx = {sum(x)}   Sy = {sum(y)}")
print(f"  X = {m['mx']:.2f}   Y = {m['my']:.1f}   (sach: 5,83 va 79,9)")
print(f"  sx^2 = {m['Sxx'] / (m['n'] - 1):.4f}  sx = {math.sqrt(m['Sxx'] / (m['n'] - 1)):.4f}"
      f"   (sach: 13,7 va 3,7)")
print(f"  sy^2 = {m['Syy'] / (m['n'] - 1):.4f}  sy = {math.sqrt(m['Syy'] / (m['n'] - 1)):.4f}"
      f"   (sach: 255,6 va 16,0)")
print(f"  Tong xy' = {sum(a * (b - 42.2) for a, b in zip(x, y)):.2f}"
      "   (sach: dong tinh ghi 2849,81; hang Tong cua bang in 2489,81)")
print(f"  r = {m['r']:.4f}   (sach: -0,5417)")
print(f"  He so xac dinh R^2 = r^2 = {m['R2']:.4f}   (sach: 0,2934)")

# ─────────────────────────────────────────────────────────────
# 2. KIỂM ĐỊNH ĐỘC LẬP QUA r — Thí dụ 1.3 (tr. 201) va 1.4 (tr. 202)
#    Tieu chuan (1.3): K = r.can(n-2)/can(1-r^2) ~ t(n-2)
# ─────────────────────────────────────────────────────────────
def kiem_dinh_r(r, n):
    return r * math.sqrt(n - 2) / math.sqrt(1 - r * r)


print()
xs = [12.0, 16.5, 15.2, 11.7, 18.3, 10.9, 14.4, 16.0]
ys = [2.75, 3.37, 2.86, 2.62, 2.76, 3.49, 3.12, 3.05]
m3 = hoi_quy(xs, ys)
print("THI DU 1.3 — kiem dinh doc lap, n = 8")
print(f"  Sxx = {m3['Sxx']:.4f}   (sach: 48,125)")
print(f"  Syy = {m3['Syy']:.4f}   (sach: 0,6780)")
print(f"  Sxy = {m3['Sxy']:.4f}   (sach in: -0,2975 — tinh lai duoc"
      f" {m3['Sxy']:.4f})")
K = kiem_dinh_r(m3["r"], m3["n"])
tb = t_quantile(0.975, m3["n"] - 2)
print(f"  r = {m3['r']:.4f}   (sach: -0,0489)")
print(f"  K = {K:.4f}   (sach: -0,1199)   t(6; 0,975) = {tb:.4f}   (sach: 2,447)")
print(f"  -> {kl(abs(K) > tb)}: X va Y coi nhu DOC LAP")

print()
print("THI DU 1.4 — kiem dinh doc lap cho bo so lieu thi du 1.1 (n = 15)")
K = kiem_dinh_r(m["r"], m["n"])
print(f"  r = {m['r']:.4f}   K = {K:.4f}   (sach: -2,32)")
for al, sach in [(0.01, 3.01), (0.05, 2.16)]:
    tb = t_quantile(1 - al / 2, m["n"] - 2)
    print(f"  alpha = {al}: t(13; {1 - al / 2}) = {tb:.4f}   (sach: {sach})"
          f"  ->  {kl(abs(K) > tb)}")
print("  ⚠ CUNG mot bo du lieu, alpha = 0,01 thi CHAP NHAN, alpha = 0,05 thi BAC BO.")
print("     Giao trinh binh luan: 'nhung ket luan khong dua tren nhung tieu chuan")
print("     thong ke chinh xac va hop ly se dan toi nhung sai lam nguy hiem'.")

# ─────────────────────────────────────────────────────────────
# 3. KIỂM ĐỊNH rho = rho0 (phép biến đổi Fisher) — Thí dụ 1.5 (tr. 203)
# ─────────────────────────────────────────────────────────────
print()
n_, r_, rho0 = 150, 0.5273, 0.5
Ztn = 0.5 * math.log((1 + r_) / (1 - r_))
EZ = 0.5 * math.log((1 + rho0) / (1 - rho0)) + rho0 / (2 * (n_ - 1))
sdZ = 1 / math.sqrt(n_ - 3)
K = (Ztn - EZ) / sdZ
print("THI DU 1.5 — n=150, r=0,5273; co the cho rang rho that = 0,5 khong?")
print(f"  Z    = 0,5.ln((1+r)/(1-r))     = {Ztn:.4f}   (sach: 0,5862)")
print(f"  EZ   = 0,5.ln((1+p0)/(1-p0)) + p0/(2(n-1)) = {EZ:.4f}   (sach: 0,5510)")
print(f"  canVZ = 1/can(n-3)             = {sdZ:.4f}   (sach: 0,082)")
print(f"  K = {K:.4f}   (sach: 0,43)   z(0,975) = {z_quantile(0.975):.4f}")
print(f"  -> {kl(abs(K) > z_quantile(0.975))}: chap nhan rho = 0,5")

# ─────────────────────────────────────────────────────────────
# 4. HỒI QUY TUYẾN TÍNH — Thí dụ 2.1 (tr. 209)
# ─────────────────────────────────────────────────────────────
print()
xw, yw = doc("huyet_tuong.csv", "trong_luong_kg", "huyet_tuong_lit")
h = hoi_quy(xw, yw)
print("THI DU 2.1 — luong huyet tuong theo trong luong co the, n = 8")
print(f"  Sx = {sum(xw)}  Sy = {sum(yw):.2f}  X = {h['mx']:.3f}  Y = {h['my']:.4f}")
print(f"  Sxy = {h['Sxy']:.4f}   (sach: 8,96)")
print(f"  Sxx = {h['Sxx']:.4f}   (sach: 205,38)")
print(f"  Syy = {h['Syy']:.4f}   (sach: 0,6780)")
print(f"  r = {h['r']:.4f}   (sach: 0,76)     R^2 = {h['R2']:.4f}")
print(f"  a = Sxy/Sxx        = {h['a']:.6f}   (sach: 0,043615)")
print(f"  b = Y - a.X        = {h['b']:.4f}   (sach: 0,0857)")
print(f"  ==> DUONG HOI QUY MAU:  y = {h['a']:.4f}x + {h['b']:.4f}")
print(f"  s^2 = (Syy - a.Sxy)/(n-2) = {h['s2']:.6f}   (sach: 0,047929)")
print(f"  s   = {h['s']:.4f}   (sach: 0,2189)")

# ─────────────────────────────────────────────────────────────
# 5. KHOẢNG TIN CẬY VÀ KIỂM ĐỊNH HỆ SỐ — Thí dụ 2.3, 2.4 (tr. 214–216)
# ─────────────────────────────────────────────────────────────
print()
n = h["n"]
tb = t_quantile(0.975, n - 2)
print(f"THI DU 2.3 — khoang tin cay 95%   t(6; 0,975) = {tb:.4f}   (sach: 2,447)")
ea = tb * h["se_a"]
print(f"  a: {h['a']:.4f} +- {ea:.4f} = ({h['a'] - ea:.4f}; {h['a'] + ea:.4f})"
      f"   (sach: 0,0062; 0,0810)")
eb = tb * h["se_b"]
print(f"  b: {h['b']:.4f} +- {eb:.4f} = ({h['b'] - eb:.4f}; {h['b'] + eb:.4f})")
print(f"     ⚠ Sach in (-2,8049; 2,9763) — rong hon ket qua tinh lai."
      " Ca hai deu CHUA 0.")
lo_ = h["ss_res"] / chi2_quantile(0.975, n - 2)
hi_ = h["ss_res"] / chi2_quantile(0.025, n - 2)
print(f"  sigma^2: ({lo_:.4f}; {hi_:.4f})   (sach: 0,0199; 0,2325)")
print(f"     chi2(6) = {chi2_quantile(0.975, 6):.3f} va"
      f" {chi2_quantile(0.025, 6):.3f}   (sach: 14,449 va 1,237)")

print()
K = h["a"] / h["se_a"]
print(f"THI DU 2.4 — kiem dinh H0: a = 0  (bien X co trong mo hinh khong?)")
print(f"  K = a/se(a) = {h['a']:.6f}/{h['se_a']:.6f} = {K:.4f}   (sach: 2,8542)")
print(f"  t(6; 0,975) = {tb:.4f}  ->  {kl(abs(K) > tb)}")
print("  => Trong luong co the CO anh huong den luong huyet tuong")
fq = f_quantile(0.95, 1, n - 2)
print(f"  Kiem qua phan phoi F (bai 7 muc 8: t(m)^2 ~ F(1,m)):")
print(f"    K^2 = {K * K:.4f}   F(1; {n - 2}; 0,95) = {fq:.4f}"
      f"   t(6;0,975)^2 = {tb * tb:.4f}  ->  khop: {math.isclose(fq, tb * tb)}")
print(f"  Khoang tin cay cho a KHONG chua 0  ->  cung ket luan (bai 12 muc 5)")

# ─────────────────────────────────────────────────────────────
# 6. HỆ SỐ XÁC ĐỊNH — tách tổng bình phương (2.13), (2.20)
# ─────────────────────────────────────────────────────────────
print()
yhat = [h["a"] * v + h["b"] for v in xw]
ss_reg = sum((p - h["my"]) ** 2 for p in yhat)
ss_res = sum((o - p) ** 2 for o, p in zip(yw, yhat))
print("HE SO XAC DINH — tach tong binh phuong (giong ANOVA o bai 13)")
print(f"  Tong binh phuong TOAN BO Syy      = {h['Syy']:.6f}")
print(f"  Do HOI QUY giai thich duoc        = {ss_reg:.6f}")
print(f"  DU (sai so, khong giai thich duoc)= {ss_res:.6f}")
print(f"  Kiem: {ss_reg:.6f} + {ss_res:.6f} = {ss_reg + ss_res:.6f}"
      f"  ->  khop: {math.isclose(ss_reg + ss_res, h['Syy'])}")
print(f"  R^2 = {ss_reg:.6f}/{h['Syy']:.6f} = {ss_reg / h['Syy']:.4f}"
      f"  = r^2 = {h['R2']:.4f}")
print(f"  => Mo hinh giai thich {h['R2'] * 100:.1f}% bien dong cua Y;"
      f" con lai {(1 - h['R2']) * 100:.1f}% chua giai thich duoc")

# ─────────────────────────────────────────────────────────────
# 7. 💼 GÓC QTKD — chi quảng cáo vs doanh số, 24 tháng
# ─────────────────────────────────────────────────────────────
print()
xa, ya = doc("quang_cao_doanh_so.csv", "chi_quang_cao_trieu", "doanh_so_trieu")
q = hoi_quy(xa, ya)
n = q["n"]
tb = t_quantile(0.975, n - 2)
print(f"💼 GOC QTKD — chi quang cao vs doanh so, {n} thang (trieu dong)")
print(f"  X = {q['mx']:.2f}   Y = {q['my']:.2f}   r = {q['r']:.4f}"
      f"   R^2 = {q['R2']:.4f}")
print(f"  DUONG HOI QUY:  doanh_so = {q['a']:.3f} x chi_quang_cao + {q['b']:.2f}")
print(f"  s = {q['s']:.2f} trieu  (do lech chuan quanh duong hoi quy)")
ea = tb * q["se_a"]
K = q["a"] / q["se_a"]
print(f"  Kiem H0: a = 0.  K = {K:.3f} vs t({n - 2}; 0,975) = {tb:.3f}"
      f"  ->  {kl(abs(K) > tb)}")
print(f"  Khoang tin cay 95% cho a: ({q['a'] - ea:.3f}; {q['a'] + ea:.3f})")
print(f"  => Chi them 1 trieu quang cao lam doanh so tang khoang"
      f" {q['a']:.2f} trieu,")
print(f"     nhung KHOANG TIN CAY tu {q['a'] - ea:.2f} den {q['a'] + ea:.2f}"
      " — do bat dinh con lon.")

# Du bao va HAI loai khoang
x0 = 80.0
y0 = q["a"] * x0 + q["b"]
se_mean = q["s"] * math.sqrt(1 / n + (x0 - q["mx"]) ** 2 / q["Sxx"])
se_pred = q["s"] * math.sqrt(1 + 1 / n + (x0 - q["mx"]) ** 2 / q["Sxx"])
print()
print(f"  DU BAO khi chi {x0} trieu quang cao:  y = {y0:.2f} trieu")
print(f"    Khoang cho TRUNG BINH  ({y0 - tb * se_mean:.1f};"
      f" {y0 + tb * se_mean:.1f})  <- 'thang trung binh'")
print(f"    Khoang DU BAO 1 thang  ({y0 - tb * se_pred:.1f};"
      f" {y0 + tb * se_pred:.1f})  <- 'thang toi cu the'")
print(f"    ⚠ Khoang du bao RONG GAP {se_pred / se_mean:.1f} LAN. Bao cao ke hoach")
print("       phai dung khoang thu hai, khong phai khoang thu nhat.")
print(f"  ⚠ R^2 = {q['R2']:.2f}: quang cao chi giai thich"
      f" {q['R2'] * 100:.0f}% bien dong doanh so.")
print("     Tuong quan KHONG phai nhan qua (bai 8 muc 9) — muon ket luan nhan qua")
print("     phai lam thi nghiem co doi chung, khong phai nhin du lieu quan sat.")
```

Kết quả chạy thật:

```
THI DU 1.1 — 15 cap so lieu, tinh cac dac trung mau
  n = 15   Sx = 87.5   Sy = 1198.5
  X = 5.83   Y = 79.9   (sach: 5,83 va 79,9)
  sx^2 = 13.6867  sx = 3.6995   (sach: 13,7 va 3,7)
  sy^2 = 255.5971  sy = 15.9874   (sach: 255,6 va 16,0)
  Tong xy' = 2849.81   (sach: dong tinh ghi 2849,81; hang Tong cua bang in 2489,81)
  r = -0.5422   (sach: -0,5417)
  He so xac dinh R^2 = r^2 = 0.2939   (sach: 0,2934)

THI DU 1.3 — kiem dinh doc lap, n = 8
  Sxx = 48.1150   (sach: 48,125)
  Syy = 0.6780   (sach: 0,6780)
  Sxy = -0.2795   (sach in: -0,2975 — tinh lai duoc -0.2795)
  r = -0.0489   (sach: -0,0489)
  K = -0.1200   (sach: -0,1199)   t(6; 0,975) = 2.4469   (sach: 2,447)
  -> CHUA CO CO SO BAC BO H0: X va Y coi nhu DOC LAP

THI DU 1.4 — kiem dinh doc lap cho bo so lieu thi du 1.1 (n = 15)
  r = -0.5422   K = -2.3264   (sach: -2,32)
  alpha = 0.01: t(13; 0.995) = 3.0123   (sach: 3.01)  ->  CHUA CO CO SO BAC BO H0
  alpha = 0.05: t(13; 0.975) = 2.1604   (sach: 2.16)  ->  BAC BO H0
  ⚠ CUNG mot bo du lieu, alpha = 0,01 thi CHAP NHAN, alpha = 0,05 thi BAC BO.
     Giao trinh binh luan: 'nhung ket luan khong dua tren nhung tieu chuan
     thong ke chinh xac va hop ly se dan toi nhung sai lam nguy hiem'.

THI DU 1.5 — n=150, r=0,5273; co the cho rang rho that = 0,5 khong?
  Z    = 0,5.ln((1+r)/(1-r))     = 0.5864   (sach: 0,5862)
  EZ   = 0,5.ln((1+p0)/(1-p0)) + p0/(2(n-1)) = 0.5510   (sach: 0,5510)
  canVZ = 1/can(n-3)             = 0.0825   (sach: 0,082)
  K = 0.4294   (sach: 0,43)   z(0,975) = 1.9600
  -> CHUA CO CO SO BAC BO H0: chap nhan rho = 0,5

THI DU 2.1 — luong huyet tuong theo trong luong co the, n = 8
  Sx = 535.0  Sy = 24.02  X = 66.875  Y = 3.0025
  Sxy = 8.9575   (sach: 8,96)
  Sxx = 205.3750   (sach: 205,38)
  Syy = 0.6780   (sach: 0,6780)
  r = 0.7591   (sach: 0,76)     R^2 = 0.5763
  a = Sxy/Sxx        = 0.043615   (sach: 0,043615)
  b = Y - a.X        = 0.0857   (sach: 0,0857)
  ==> DUONG HOI QUY MAU:  y = 0.0436x + 0.0857
  s^2 = (Syy - a.Sxy)/(n-2) = 0.047878   (sach: 0,047929)
  s   = 0.2188   (sach: 0,2189)

THI DU 2.3 — khoang tin cay 95%   t(6; 0,975) = 2.4469   (sach: 2,447)
  a: 0.0436 +- 0.0374 = (0.0063; 0.0810)   (sach: 0,0062; 0,0810)
  b: 0.0857 +- 2.5056 = (-2.4199; 2.5914)
     ⚠ Sach in (-2,8049; 2,9763) — rong hon ket qua tinh lai. Ca hai deu CHUA 0.
  sigma^2: (0.0199; 0.2322)   (sach: 0,0199; 0,2325)
     chi2(6) = 14.449 va 1.237   (sach: 14,449 va 1,237)

THI DU 2.4 — kiem dinh H0: a = 0  (bien X co trong mo hinh khong?)
  K = a/se(a) = 0.043615/0.015268 = 2.8566   (sach: 2,8542)
  t(6; 0,975) = 2.4469  ->  BAC BO H0
  => Trong luong co the CO anh huong den luong huyet tuong
  Kiem qua phan phoi F (bai 7 muc 8: t(m)^2 ~ F(1,m)):
    K^2 = 8.1601   F(1; 6; 0,95) = 5.9874   t(6;0,975)^2 = 5.9874  ->  khop: True
  Khoang tin cay cho a KHONG chua 0  ->  cung ket luan (bai 12 muc 5)

HE SO XAC DINH — tach tong binh phuong (giong ANOVA o bai 13)
  Tong binh phuong TOAN BO Syy      = 0.677950
  Do HOI QUY giai thich duoc        = 0.390684
  DU (sai so, khong giai thich duoc)= 0.287266
  Kiem: 0.390684 + 0.287266 = 0.677950  ->  khop: True
  R^2 = 0.390684/0.677950 = 0.5763  = r^2 = 0.5763
  => Mo hinh giai thich 57.6% bien dong cua Y; con lai 42.4% chua giai thich duoc

💼 GOC QTKD — chi quang cao vs doanh so, 24 thang (trieu dong)
  X = 59.82   Y = 324.71   r = 0.6340   R^2 = 0.4019
  DUONG HOI QUY:  doanh_so = 2.285 x chi_quang_cao + 188.01
  s = 51.63 trieu  (do lech chuan quanh duong hoi quy)
  Kiem H0: a = 0.  K = 3.845 vs t(22; 0,975) = 2.074  ->  BAC BO H0
  Khoang tin cay 95% cho a: (1.053; 3.518)
  => Chi them 1 trieu quang cao lam doanh so tang khoang 2.29 trieu,
     nhung KHOANG TIN CAY tu 1.05 den 3.52 — do bat dinh con lon.

  DU BAO khi chi 80.0 trieu quang cao:  y = 370.81 trieu
    Khoang cho TRUNG BINH  (337.7; 403.9)  <- 'thang trung binh'
    Khoang DU BAO 1 thang  (258.7; 482.9)  <- 'thang toi cu the'
    ⚠ Khoang du bao RONG GAP 3.4 LAN. Bao cao ke hoach
       phai dung khoang thu hai, khong phai khoang thu nhat.
  ⚠ R^2 = 0.40: quang cao chi giai thich 40% bien dong doanh so.
     Tuong quan KHONG phai nhan qua (bai 8 muc 9) — muon ket luan nhan qua
     phai lam thi nghiem co doi chung, khong phai nhin du lieu quan sat.
```

Bảy điểm đáng để ý:

1. **Hàm `hoi_quy` 15 dòng** làm được toàn bộ §2 của chương VI. Chú ý nó trả về cả `se_a`, `se_b` —
   sai số chuẩn của hệ số, thứ mà mọi phần mềm thống kê đều in ra bên cạnh hệ số.
2. **Thí dụ 1.4**: hai dòng liên tiếp cho hai kết luận **ngược nhau** chỉ vì đổi $\alpha$.
   Đây là minh hoạ sống động nhất cho lời cảnh báo của giáo trình ở tr. 202.
3. **Dòng `Kiem: 0.390684 + 0.287266 = 0.677950 -> khop: True`** — đẳng thức tách tổng bình phương
   (2.13) được kiểm bằng số. Cùng ý tưởng với ANOVA ở bài 13.
4. **`R^2 = 0.5763 = r^2 = 0.5763`** — hai cách tính hoàn toàn khác nhau (một từ tổng bình phương,
   một từ bình phương hệ số tương quan) cho cùng con số. Đó là nội dung của công thức (2.20).
5. **Ba cách kiểm $H_0: a = 0$ đều cho cùng kết luận**: $t = 2{,}857 > 2{,}447$;
   khoảng $(0{,}0063; 0{,}0810)$ không chứa 0; $K^2 = 8{,}16 > F = 5{,}99$.
6. **Góc QTKD, hai khoảng dự báo**: `(337.7; 403.9)` cho *trung bình* so với `(258.7; 482.9)` cho
   *một tháng cụ thể* — **rộng gấp 3,4 lần**. Báo cáo nhầm khoảng là sai lầm tốn tiền nhất trong
   toàn bài.
7. **`R^2 = 0.40`** với hệ số $a$ có ý nghĩa thống kê — đúng tình huống ở mục 7: mô hình *yếu về
   giải thích* nhưng vẫn *dùng được để ra quyết định*, miễn là báo cáo trung thực phần chưa
   giải thích được.

---

## 11. Tự thử

1. Ở thí dụ 2.1, thêm một người: 90 kg, 4,2 lít. $\hat a$, $\hat b$, $r$, $R^2$ đổi thế nào?
   Điểm này có phải giá trị thái quá không?
2. Đảo vai trò hai biến: hồi quy $x$ theo $y$ thay vì $y$ theo $x$. Hệ số góc mới có bằng
   $1/\hat a$ không? Vì sao không? (Gợi ý: $\hat a = r\,s_y/s_x$.)
3. Kiểm chứng đường hồi quy **luôn đi qua $(\overline{X}, \overline{Y})$**: tính
   $\hat a \overline{X} + \hat b$ và so với $\overline{Y}$.
4. Viết hàm in **biểu đồ phần dư** bằng ký tự: trục ngang $\hat y$, trục dọc $\hat\varepsilon$.
   Với dữ liệu quảng cáo, phần dư có trông ngẫu nhiên không?
5. Với dữ liệu quảng cáo, thử **hồi quy log–log**: đặt $x' = \ln x$, $y' = \ln y$ rồi hồi quy.
   Hệ số góc mới là **độ co giãn**. $R^2$ có tốt hơn không?
6. Tính hai khoảng (tin cậy và dự báo) tại $x_0 = \overline{X}$ và tại $x_0$ ở rìa dữ liệu.
   Khoảng nào rộng hơn? Vì sao công thức có số hạng $(x_0 - \overline{X})^2$?
7. Tạo một bộ dữ liệu **quan hệ hình chữ U** (ví dụ $y = -(x-5)^2 + 30 + $ nhiễu, $x$ từ 0 đến 10).
   Tính $r$ — có gần 0 không? Rồi thêm biến $x^2$ và hồi quy bội. $R^2$ đổi thế nào?
   (Đây là mục 8 và mục 9 ý 4 gộp lại.)

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)   | Tiếng Anh                      | Ghi chú                              |
| ------------------------- | ------------------------------ | ------------------------------------ |
| Phân tích tương quan      | Correlation analysis           | §1                                   |
| Hệ số tương quan mẫu      | Sample correlation coefficient | $r$                                  |
| Hệ số xác định (mẫu)      | Coefficient of determination   | $r^2$, $R^2$                         |
| Phép biến đổi Fisher      | Fisher's z-transformation      | (1.5)                                |
| Phân tích hồi quy         | Regression analysis            | §2                                   |
| Hồi quy tuyến tính        | Linear regression              | $y = ax+b$                           |
| Đường hồi quy mẫu         | Sample regression line         |                                      |
| Bình phương cực tiểu      | Least squares                  | (2.6)                                |
| Hệ số góc / hệ số chặn    | Slope / Intercept              | $a$ / $b$                            |
| Phần dư, sai số ước lượng | Residual                       | $\hat\varepsilon_i = y_i - \hat y_i$ |
| Sai số chuẩn của hệ số    | Standard error                 | $s/\sqrt{S_{xx}}$                    |
| Tổng bình phương dư       | Residual sum of squares        |                                      |
| Phương sai thuần nhất     | Homoscedasticity               | giả thiết (2.3b)                     |
| Khoảng dự báo             | Prediction interval            | 📚 mục 9 ý 3                         |
| Hồi quy phi tuyến         | Non-linear regression          | §2.5                                 |
| Tuyến tính hoá            | Linearization                  | đổi biến                             |
| Hồi quy bội               | Multiple regression            | §3                                   |
| Tương quan bội / riêng    | Multiple / Partial correlation | tr. 224                              |
| Đa cộng tuyến             | Multicollinearity              | 📚 mục 8                             |
| Hệ số xác định hiệu chỉnh | Adjusted $R^2$                 | 📚 mục 8                             |
| Hồi quy giả               | Spurious regression            | 📚 mục 9 ý 6                         |
| Quá khớp                  | Overfitting                    | 📚 mục 9 ý 6                         |
| Độ co giãn                | Elasticity                     | hệ số của log–log                    |

### 💼 Trong Excel

| Việc                             | Hàm / công cụ                         |
| -------------------------------- | ------------------------------------- |
| $r$                              | `CORREL(mảng_x; mảng_y)`              |
| $\hat a$                         | `SLOPE(mảng_y; mảng_x)`               |
| $\hat b$                         | `INTERCEPT(mảng_y; mảng_x)`           |
| $R^2$                            | `RSQ(mảng_y; mảng_x)`                 |
| Dự báo                           | `FORECAST.LINEAR(x₀; mảng_y; mảng_x)` |
| Toàn bộ (kèm sai số chuẩn)       | `LINEST(...)` — công thức mảng        |
| Báo cáo đầy đủ + biểu đồ phần dư | **Data ▸ Data Analysis ▸ Regression** |

⭐ Công cụ cuối cùng in ra bảng ANOVA cho hồi quy, hệ số kèm giá trị p và khoảng tin cậy —
đúng mọi thứ bài này dạy. Nếu chỉ nhớ một thứ từ bảng này, hãy nhớ nó.

---

## 13. Câu hỏi tự kiểm tra

1. Giải thích vì sao $\hat a = r\,\dfrac{s_y}{s_x}$. Từ đó suy ra: nếu $r = 0$ thì đường hồi quy
   trông thế nào?
2. Vì sao ước lượng $\sigma^2$ trong hồi quy chia cho $n-2$, trong khi phương sai mẫu ở bài 10
   chia cho $n-1$?
3. Với $n = 20$ và $r = 0{,}40$, kiểm định $H_0: \rho = 0$ ở $\alpha = 0{,}05$. Kết luận?
   Còn nếu $n = 100$ với cùng $r$?
4. Nêu ba cách tương đương để kiểm định $H_0: a = 0$. Vì sao chúng luôn cho cùng kết luận?
5. Một mô hình có $R^2 = 0{,}85$. Nêu **ba** lý do khiến con số đó có thể gây hiểu nhầm.
6. Phân biệt **khoảng tin cậy cho $E(Y|x_0)$** và **khoảng dự báo cho $y_0$**.
   Khoảng nào rộng hơn và rộng hơn bao nhiêu? Khi lập kế hoạch kinh doanh thì dùng khoảng nào?
7. Hồi quy doanh số theo chi quảng cáo cho $\hat a = 3{,}2$ với khoảng tin cậy 95% là (0,4; 6,0).
   a) Hệ số có ý nghĩa thống kê không?
   b) Có thể kết luận "chi thêm 1 triệu thu về 3,2 triệu" không?
   c) Với khoảng rộng như vậy, bạn khuyến nghị gì?
8. Vì sao đưa cả "chi Facebook", "chi Google" và "tổng chi quảng cáo" vào một mô hình hồi quy bội
   là sai? Hiện tượng đó gọi là gì?
9. Cho $x$ từ 1 đến 10 và $y = 3x + 5$ **chính xác** (không nhiễu). $r$, $R^2$, $s^2$ bằng bao nhiêu?
   Khoảng tin cậy cho $a$ rộng bao nhiêu?
10. Một báo cáo viết: *"$R^2 = 0{,}92$ giữa số nhân viên bán hàng và doanh thu, vậy tuyển thêm
    nhân viên sẽ tăng doanh thu."* Nêu ít nhất ba vấn đề của kết luận này.

---

## Tóm tắt một trang

```
╔════════════════════════════════════════════════════════════════════════════╗
║  BÀI 14 — TƯƠNG QUAN VÀ PHÂN TÍCH HỒI QUY             (Ch. VI, tr.194–229) ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ── §1 TƯƠNG QUAN: "có liên hệ không, mạnh yếu thế nào" ────────           ║
║                                                                            ║
║  r = Sxy / ((n−1)·sx·sy)          |r| ≤ 1     R² = r²                      ║
║      thực hành: |r| > 0,8 → coi như xấp xỉ tuyến tính                      ║
║      ⚠ r chỉ đo quan hệ TUYẾN TÍNH — luôn VẼ ĐỒ THỊ trước                  ║
║                                                                            ║
║  KIỂM ĐỊNH ĐỘC LẬP   H₀: ρ = 0                                             ║
║      K = r√(n−2) / √(1−r²)   ~ t(n−2)                                      ║
║      ⭐ quyết định CÓ NÊN LÀM HỒI QUY HAY KHÔNG                            ║
║      ⚠ r lớn chưa chắc có ý nghĩa: n=15, r=−0,54                           ║
║          α=0,01 → CHẤP NHẬN | α=0,05 → BÁC BỎ   (thí dụ 1.4!)              ║
║      |r| tối thiểu để có ý nghĩa: n=10→0,63 | n=100→0,20 | n=1000→0,06     ║
║                                                                            ║
║  KIỂM ĐỊNH ρ = ρ₀    biến đổi Fisher  Z = ½·ln((1+r)/(1−r))                ║
║      EZ ≈ ½·ln((1+ρ₀)/(1−ρ₀)) + ρ₀/(2(n−1)),   VZ = 1/(n−3)                ║
║                                                                            ║
║  ── §2 HỒI QUY: "liên hệ đó là hàm gì" ─────────────────────────           ║
║                                                                            ║
║  MÔ HÌNH   Yᵢ = aXᵢ + b + εᵢ                                               ║
║      (a) Eε = 0   (b) Vε = σ² ∀i, không tương quan   (c) ε chuẩn           ║
║   ⭐ (b) = PHƯƠNG SAI THUẦN NHẤT, tự động đúng nếu (X,Y) chuẩn 2 chiều     ║
║                                                                            ║
║  ⭐ BÌNH PHƯƠNG CỰC TIỂU                                                   ║
║       â = Sxy/Sxx = r·(sy/sx)          b̂ = Ȳ − â·X̄                         ║
║       ⭐ đường hồi quy LUÔN đi qua (X̄, Ȳ)   ← cách kiểm bài                ║
║       s² = (Syy − â·Sxy)/(n−2)   ← chia n−2, mất 2 bậc tự do               ║
║       V(â) = σ²/Sxx  →  x TRẢI RỘNG thì â chính xác hơn                    ║
║                                                                            ║
║  KHOẢNG TIN CẬY   â ± t(n−2; 1−α/2) · s/√Sxx                               ║
║                   σ²: ((n−2)s²/χ²_{1−α/2} ; (n−2)s²/χ²_{α/2})              ║
║                                                                            ║
║  ⭐⭐ KIỂM ĐỊNH H₀: a = 0  — "biến X có vai trò gì không?"                 ║
║      BA CÁCH TƯƠNG ĐƯƠNG, luôn cùng kết luận:                              ║
║        ① |K| = |â/se(â)| > t(n−2; 1−α/2)                                  ║
║        ② khoảng tin cậy cho a KHÔNG chứa 0                                ║
║        ③ K² > F(1; n−2; 1−α)        [t(m)² ~ F(1,m), bài 7 mục 8]         ║
║                                                                            ║
║  HỆ SỐ XÁC ĐỊNH — tách tổng bình phương như ANOVA (bài 13)                 ║
║      Σ(yᵢ−Ȳ)²  =  Σ(ŷᵢ−Ȳ)²   +   Σ(yᵢ−ŷᵢ)²                                 ║
║      TOÀN BỘ   = HỒI QUY g.thích + DƯ (không g.thích)                      ║
║      R² = phần giải thích / toàn bộ  = r²                                  ║
║      ⭐ khớp với V(Y|X) = σ²_Y(1−ρ²) ở bài 8 mục 8                         ║
║      💼 kinh doanh: R² = 0,2–0,5 là BÌNH THƯỜNG; R² > 0,9 thì ĐÁNG NGHI    ║
║                                                                            ║
║  MỞ RỘNG  phi tuyến → TUYẾN TÍNH HOÁ bằng đổi biến (log–log = độ co giãn)  ║
║           hồi quy bội → ⚠ ĐA CỘNG TUYẾN, dùng R² HIỆU CHỈNH                ║
║                                                                            ║
║  📚 BẢY SAI LẦM                                                            ║
║      1. coi TƯƠNG QUAN là NHÂN QUẢ  (hồi quy KHÔNG chứng minh nhân quả)    ║
║      2. NGOẠI SUY ra ngoài vùng dữ liệu (b̂ thường vô nghĩa vì x=0 ngoài)   ║
║      3. nhầm KHOẢNG TIN CẬY với KHOẢNG DỰ BÁO (khác nhau ở số 1 dưới căn)  ║
║      4. không VẼ ĐỒ THỊ (Anscombe: cùng r, hình khác hẳn)                  ║
║      5. bỏ qua BIẾN ẨN (hệ số có thể ĐỔI DẤU)                              ║
║      6. R² cao vì lý do sai (đo cùng thứ / xu hướng thời gian / quá khớp)  ║
║      7. không kiểm GIẢ THIẾT → vẽ BIỂU ĐỒ PHẦN DƯ:                         ║
║            hình cong = quan hệ phi tuyến | hình phễu = phương sai đổi      ║
║                                                                            ║
║  ⚠ GHI CHÚ SỐ LIỆU                                                         ║
║      tr.197 thí dụ 1.1: hàng Tổng in 2489,81; đúng là 2849,81              ║
║      tr.201 thí dụ 1.3: Sxy in −0,2975; tính lại −0,2795 (r vẫn đúng)      ║
║      tr.215 thí dụ 2.3: khoảng cho b tính lại (−2,42; 2,59)                ║
║                          và Σx² in 35893,5 (thí dụ 2.1 cho 35983,5)        ║
║                                                                            ║
║  💼 QTKD  Excel: Data ▸ Data Analysis ▸ Regression (có cả biểu đồ phần dư) ║
║          lập kế hoạch → dùng KHOẢNG DỰ BÁO, không phải khoảng tin cậy      ║
║          báo cáo: â + KHOẢNG TIN CẬY + R² + phần CHƯA giải thích được      ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương VI, tr. 194–229.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Ghi chú số liệu: thí dụ 1.1 (tr. 197) — hàng Tổng của bảng in $\sum x_i y_i' = 2489{,}81$ trong khi
  dòng tính toán dùng 2849,81 (giá trị đúng, cộng lại từ chính cột của bảng);
  thí dụ 1.3 (tr. 201) — $\sum(x_i-\overline{X})(y_i-\overline{Y})$ in $-0{,}2975$, tính lại được
  $-0{,}2795$ (con số $r = -0{,}0489$ mà sách công bố khớp với giá trị tính lại);
  thí dụ 2.3 (tr. 215) — khoảng tin cậy cho $b$ tính lại được $(-2{,}42;\ 2{,}59)$, và công thức
  in $\sum x_i^2 = 35893{,}5$ trong khi thí dụ 2.1 cho 35983,5.
  **Kết luận của cả ba thí dụ không thay đổi.**
- Dữ liệu: `cap_so_lieu_15.csv` (thí dụ 1.1) và `huyet_tuong.csv` (thí dụ 2.1) là số liệu nguyên văn
  của giáo trình. `quang_cao_doanh_so.csv` là **dữ liệu mô phỏng** cho phần 💼.
- Mục 9 (bảy sai lầm), công thức khoảng dự báo, $R^2$ hiệu chỉnh, bảng đối chiếu Excel:
  kiến thức bổ sung, không có trong giáo trình.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 13 — Kiểm định nhiều mẫu và phân tích phương sai](bai_13_kiem_dinh_nhieu_mau_va_anova.md) ·
Bài sau: — **hết khoá học** 🎓
