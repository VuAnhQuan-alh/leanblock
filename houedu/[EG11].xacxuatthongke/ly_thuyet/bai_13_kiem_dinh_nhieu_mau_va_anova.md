# Bài 13 — Kiểm định nhiều mẫu, phân tích phương sai và kiểm định phi tham số

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương V §3–§4**, tr. 170–193.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này nêu **hai chỗ số liệu không nhất quán** trong thí dụ 3.3 và 3.4.
> 📌 **Cần đọc trước:** [Bài 8](bai_08_bien_ngau_nhien_hai_chieu_va_tuong_quan.md) · [Bài 11](bai_11_uoc_luong_diem_va_khoang_tin_cay.md) · [Bài 12](bai_12_kiem_dinh_gia_thuyet_mot_mau.md)

Bài 12 so sánh **một mẫu với một con số cho trước**. Bài này so sánh **các mẫu với nhau** —
tình huống thực tế hơn nhiều.

💼 Vì trong kinh doanh, câu hỏi hầu như luôn là **so sánh**: phương án A hay B? chi nhánh nào tốt hơn?
nhà cung cấp nào ổn định hơn? Bốn bài toán của §3 và hai bài toán của §4 phủ gần hết các so sánh
bạn sẽ cần.

## Mục lục

1. [So sánh hai kỳ vọng](#1-so-sánh-hai-kỳ-vọng)
2. [So sánh hai tỷ lệ](#2-so-sánh-hai-tỷ-lệ)
3. [So sánh hai phương sai](#3-so-sánh-hai-phương-sai)
4. [Phân tích phương sai một nhân tố](#4-phân-tích-phương-sai-một-nhân-tố)
5. [Kiểm định phù hợp](#5-kiểm-định-phù-hợp)
6. [Kiểm định độc lập](#6-kiểm-định-độc-lập)
7. [📚 Quy trình chọn kiểm định](#7--quy-trình-chọn-kiểm-định)
8. [📚 Sau ANOVA thì làm gì](#8--sau-anova-thì-làm-gì)
9. [Code minh hoạ](#9-code-minh-hoạ)
10. [Tự thử](#10-tự-thử)
11. [Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
12. [Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. So sánh hai kỳ vọng

**Bài toán 1 (tr. 170).** Hai tổng thể $X \sim N(a_1; \sigma_1^2)$ và $Y \sim N(a_2; \sigma_2^2)$.
Kiểm định $H_0: a_1 = a_2$.

Giáo trình nêu ý tưởng gọn (tr. 170): *"đưa về kiểm định $a_1 - a_2 = 0 = E(X - Y)$"* —
tức là quy về bài toán một mẫu của bài 12.

### Trường hợp 1: biết $\sigma_1$, $\sigma_2$

**Tiêu chuẩn (3.1):**

$$K = \frac{(\overline{X} - \overline{Y}) - (a_1 - a_2)}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}} \ \sim N(0;1)$$

Khi $H_0$ đúng thì $a_1 - a_2 = 0$, tử số còn $\overline{X} - \overline{Y}$.

Miền tới hạn (3.2)–(3.4) giống hệt bài toán 1 của bài 12.

📚 **Mẫu số đến từ đâu?** Từ bài 9 mục 3: $V(X - Y) = VX + VY$ khi độc lập.
Chia cho cỡ mẫu tương ứng (bài 10 mục 5) được $\sigma_1^2/n_1 + \sigma_2^2/n_2$.

⚠️ Chú ý **cộng**, không phải trừ — dù đang tính hiệu. Trừ hai biến ngẫu nhiên độc lập làm
phương sai **tăng**, không giảm.

### Trường hợp 2: chưa biết $\sigma$, mẫu lớn ($n_1, n_2 > 30$)

Dùng (3.1) nhưng thay $\sigma_i^2$ bằng $s_i^2$. Kết quả gần đúng.

### Trường hợp 3: chưa biết $\sigma$, mẫu nhỏ

**Tiêu chuẩn (3.5)** — dùng **phương sai gộp** (pooled):

$$K = \frac{(\overline{X} - \overline{Y}) - (a_1 - a_2)}
{\sqrt{\dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}
\ \sim t(n_1 + n_2 - 2)$$

⚠️ **Điều kiện bắt buộc** mà giáo trình nêu rõ (tr. 171): *"nếu thêm giả thiết hai biến gốc có
**phương sai giống nhau**"*.

**Đây là điều kiện hay bị bỏ quên nhất của cả chương.** Nếu $\sigma_1^2 \ne \sigma_2^2$ thì (3.5)
**sai** — phải kiểm bằng bài toán 3 ở mục 3 trước, hoặc dùng cách khác (mục 7).

Phần trong căn giữa là **phương sai gộp** — trung bình có trọng số của hai phương sai mẫu, trọng số
là bậc tự do:

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

Bậc tự do $n_1 + n_2 - 2$: mất **hai** bậc vì ước lượng **hai** trung bình.

### Thí dụ 3.1 (tr. 171)

> Trọng lượng sơ sinh của trẻ có mẹ **không hút thuốc** ($n_1 = 15$, $\overline{X}_1 = 3{,}5933$,
> $s_1 = 0{,}3707$) và **hút thuốc** ($n_2 = 14$, $\overline{X}_2 = 3{,}2029$, $s_2 = 0{,}4927$).
> Giả sử chuẩn cùng phương sai. $\alpha = 0{,}05$: trẻ nhóm mẹ hút thuốc có nhẹ cân hơn không?

$H_0: a_1 = a_2$, $H_1: a_1 > a_2$ (một phía phải):

$$K_{tn} = \frac{3{,}5933 - 3{,}2029}
{\sqrt{\dfrac{14 \times 0{,}3707^2 + 13 \times 0{,}4927^2}{27}\left(\dfrac1{15}+\dfrac1{14}\right)}}
= \mathbf{2{,}42}$$

$t_{27;\,0{,}95} = 1{,}703$. Vì $2{,}42 > 1{,}703$ → **bác bỏ**: trẻ ở nhóm mẹ không hút thuốc
**nặng hơn** đáng kể.

### Thí dụ 3.2 (tr. 172)

> Năng suất lúa mỳ hai vùng: $n_1 = 9$, $\overline{X}_1 = 24{,}6$, $s_1^2 = 0{,}24$;
> $n_2 = 16$, $\overline{X}_2 = 25{,}8$, $s_2^2 = 0{,}16$. $\alpha = 0{,}05$, có sai khác đáng kể không?

$H_1: a_1 \ne a_2$ (hai phía). $t_{23;\,0{,}975} = 2{,}069$:

$$K_{tn} = \frac{24{,}6 - 25{,}8}{\sqrt{\dfrac{8 \times 0{,}24 + 15 \times 0{,}16}{23}\left(\dfrac19+\dfrac1{16}\right)}}
= \mathbf{-6{,}65}$$

$|-6{,}65| > 2{,}069$ → **bác bỏ**: năng suất hai vùng **khác nhau**.

(Sách in $-6{,}67$; tính chính xác được $-6{,}6453$. Chênh do làm tròn, kết luận không đổi.)

### ⭐ Ba chú ý của giáo trình (tr. 172)

1. Nếu $n_1$, $n_2$ **khá lớn**, có thể **bỏ giả thiết chuẩn** (nhờ CLT, bài 9).
2. Hai đối thuyết $a_1 > a_2$ và $a_1 < a_2$ **đổi cho nhau** bằng cách đổi thứ tự hai mẫu.
3. **Trường hợp mẫu cặp** $(x_i, y_i)$: nên lập hiệu $z_i = x_i - y_i$ rồi đưa về kiểm định
   $H_0: EZ = 0$ — tức bài toán một mẫu ở bài 12.

⭐ **Chú ý thứ ba rất quan trọng và hay bị bỏ sót.**

💼 Ví dụ mẫu cặp: đo doanh số của **cùng 20 cửa hàng** trước và sau khi đổi cách trưng bày.
Hai mẫu **không độc lập** (cùng cửa hàng!), nên (3.5) **sai**. Phải lấy hiệu từng cửa hàng rồi
kiểm định một mẫu.

**Cách phân biệt:**

|          | Mẫu độc lập                               | Mẫu cặp                                  |
| -------- | ----------------------------------------- | ---------------------------------------- |
| Đặc điểm | hai nhóm **khác nhau**                    | **cùng** đối tượng, đo hai lần           |
| Ví dụ    | nhóm A dùng giao diện cũ, nhóm B dùng mới | cùng khách hàng, trước và sau khuyến mại |
| Cỡ mẫu   | $n_1$ có thể $\ne n_2$                    | bắt buộc $n_1 = n_2$                     |
| Dùng     | (3.5), $t(n_1+n_2-2)$                     | lấy hiệu → bài 12, $t(n-1)$              |

⭐ Mẫu cặp **mạnh hơn nhiều** vì loại bỏ được biến thiên giữa các đối tượng. Thiết kế được thì nên
thiết kế thành mẫu cặp.

---

## 2. So sánh hai tỷ lệ

**Bài toán 2 (tr. 172).** $X \sim B(p_1)$, $Y \sim B(p_2)$. Kiểm định $H_0: p_1 = p_2$.

**Tiêu chuẩn (3.9):**

$$K = \frac{f_1 - f_2}{\sqrt{f(1-f)\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}} \ \approx N(0;1)$$

trong đó $f = \dfrac{m_1 + m_2}{n_1 + n_2}$ là **tần suất gộp**.

⚠️ **Vì sao gộp?** Vì $H_0$ nói $p_1 = p_2$ — khi giả sử $H_0$ đúng thì chỉ có **một** tỷ lệ chung,
ước lượng tốt nhất là gộp cả hai mẫu. Đây là cùng logic với việc bài 12 mục 6 dùng $p_0$ ở mẫu số.

### Thí dụ 3.3 (tr. 173)

> Lô 1: 500 sản phẩm có 50 phế phẩm. Lô 2: 400 sản phẩm có 60 phế phẩm. $\alpha = 0{,}05$.

$f_1 = 0{,}1$, $f_2 = 0{,}15$, $f = \dfrac{110}{900} = 0{,}1222$:

$$K_{tn} = \frac{0{,}1 - 0{,}15}{\sqrt{0{,}1222 \times 0{,}8778 \left(\dfrac1{500}+\dfrac1{400}\right)}}
= \mathbf{-2{,}276}$$

**a) $H_1: p_1 \ne p_2$:** $|-2{,}276| > 1{,}96$ → **bác bỏ**, hai lô khác nhau.

**b) $H_1: p_1 < p_2$:** $-2{,}276 < -1{,}645$ → **bác bỏ**, lô 1 có tỷ lệ phế phẩm **thấp hơn**
đáng kể.

Giáo trình nhấn mạnh một điều tinh tế (tr. 174): kiểm định hai phía chỉ cho biết **khác nhau**;
*"để kết luận lô thứ nhất có chất lượng tốt hơn thì **chưa đủ**"* — phải chạy thêm kiểm định
một phía.

### ⚠️ Ghi chú về số liệu

Giáo trình còn nêu cách tính **không gộp phương sai** và in kết quả $\approx -2{,}56$.
Tính chính xác:

$$K = \frac{0{,}1 - 0{,}15}{\sqrt{\dfrac{0{,}1 \times 0{,}9}{500} + \dfrac{0{,}15 \times 0{,}85}{400}}}
= \mathbf{-2{,}239}$$

Không phải $-2{,}56$. Kết luận không đổi (vẫn bác bỏ), nhưng con số in trong sách không tái tạo được.

Ngoài ra sách in $z_b = 1{,}654$ ở dòng dưới rồi lại dùng $1{,}645$ — lỗi đảo chữ số.

### 💼 Góc QTKD — đây chính là A/B test hai nhóm

|               | Nhóm A (cũ) | Nhóm B (mới) |
| ------------- | ----------: | -----------: |
| Lượt hiển thị |       5.000 |        5.000 |
| Số đơn        |         150 |          185 |
| Tỷ lệ         |       3,00% |        3,70% |

$$f = \frac{335}{10\,000} = 0{,}0335, \qquad
K = \frac{0{,}037 - 0{,}030}{\sqrt{0{,}0335 \times 0{,}9665 \times \dfrac{2}{5000}}} = 1{,}95$$

$1{,}95 < 1{,}96$ → **suýt** đủ, nhưng chưa. Giá trị p = 0,051.

⚠️ **Đây là tình huống nguy hiểm nhất của A/B test.** Cám dỗ rất lớn là chạy thêm vài ngày cho
$p$ xuống dưới 0,05 — đó chính là lỗi "nhìn lén" ở bài 12 mục 9.

**Cách làm đúng:** cố định cỡ mẫu trước, và nếu kết quả sát ngưỡng thì báo cáo trung thực
*"chênh lệch ước tính +0,7 điểm phần trăm, khoảng tin cậy 95% là (−0,002; +1,4), chưa kết luận được"* —
kèm cả khoảng tin cậy chứ không chỉ có/không.

---

## 3. So sánh hai phương sai

**Bài toán 3 (tr. 174).** $H_0: \sigma_1^2 = \sigma_2^2$.

**Tiêu chuẩn (3.12):**

$$K = \frac{s_1^2}{s_2^2} \ \sim F(n_1 - 1;\ n_2 - 1) \text{ khi } H_0 \text{ đúng}$$

Đây chính là công thức (2.16) đã học ở bài 10 mục 7.

**Miền tới hạn:**

| $H_1$                       | Bác bỏ khi                                                               | Công thức |
| --------------------------- | ------------------------------------------------------------------------ | --------- |
| $\sigma_1^2 \ne \sigma_2^2$ | $K < F_{n_1-1,n_2-1;\,\alpha/2}$ hoặc $K > F_{n_1-1,n_2-1;\,1-\alpha/2}$ | (3.13)    |
| $\sigma_1^2 > \sigma_2^2$   | $K > F_{n_1-1,n_2-1;\,1-\alpha}$                                         | (3.14)    |

💡 **Mẹo thực hành:** luôn đặt **phương sai lớn hơn ở tử số**. Khi đó $K > 1$ và chỉ cần tra
phân vị bên phải, không cần bảng cho phân vị nhỏ.

### Thí dụ 3.4 (tr. 175) — và quy trình hai bước

> Tốc độ đầu đạn của hai công ty: $n_1 = 10$, $\overline{X}_1 = 1210$, $s_1^2 = 2500$;
> $n_2 = 10$, $\overline{X}_2 = 1175$, $s_2^2 = 3600$. $\alpha = 0{,}05$, chất lượng hai mẫu đạn
> có giống nhau không?

⭐ **Giáo trình dạy đúng quy trình hai bước ở đây** (tr. 175):

> "Muốn đưa về mô hình so sánh kỳ vọng, ta **phải có giả thiết là $X_1$ và $X_2$ cùng phương sai**.
> Giả thiết đó **có thể được thừa nhận dựa vào bài toán 3**."

**Bước 1 — kiểm phương sai:**

$$K = \frac{s_2^2}{s_1^2} = \frac{3600}{2500} = \mathbf{1{,}44}$$

$F_{9,9;\,0{,}95} = 3{,}18$. Vì $1{,}44 < 3{,}18$ → **chấp nhận** cùng phương sai. ✓

**Bước 2 — giờ mới được dùng (3.5):**

$$K = \frac{1210 - 1175}{\sqrt{\dfrac{9 \times 2500 + 9 \times 3600}{18}\left(\dfrac1{10}+\dfrac1{10}\right)}} = \mathbf{1{,}42}$$

$t_{18;\,0{,}975} = 2{,}101$. Vì $|1{,}42| < 2{,}101$ → **chấp nhận** $H_0: a_1 = a_2$.

### ⚠️ Ghi chú số liệu không nhất quán

Đề bài ghi $s_1^2 = 2500$, nhưng phần giải viết $\dfrac{3600}{2550} = 1{,}41$ — dùng **2550**.
Với $2500$ thì $K = 1{,}44$; với $2550$ thì $K = 1{,}4118$. Kết luận không đổi trong cả hai trường hợp.

### 💼 Góc QTKD — so phương sai quan trọng không kém so trung bình

| Nhà cung cấp | Thời gian giao trung bình | Độ lệch chuẩn |
| ------------ | ------------------------: | ------------: |
| A            |                  5,0 ngày |      0,5 ngày |
| B            |                  5,0 ngày |      3,0 ngày |

**Cùng trung bình, nhưng B tệ hơn rất nhiều.** Với A, hầu như mọi đơn về trong 4–6 ngày.
Với B, có đơn về sau 2 ngày, có đơn sau 11 ngày — không lập kế hoạch tồn kho được.

⭐ **Trong quản trị vận hành, độ ổn định thường quan trọng hơn giá trị trung bình.**
Đó là toàn bộ triết lý của Six Sigma (bài 7 mục 5) và của sản xuất tinh gọn.

⚠️ Nhưng nhớ bài 11 mục 8: ước lượng phương sai **kém chính xác hơn nhiều** so với ước lượng kỳ vọng —
cần cỡ mẫu lớn hơn hẳn để kết luận chắc chắn về độ biến động.

---

## 4. Phân tích phương sai một nhân tố

**Bài toán 4 (tr. 176).** $k$ tổng thể $X_j \sim N(a_j; \sigma^2)$. Kiểm định

$$H_0: a_1 = a_2 = \dots = a_k \quad \text{với} \quad H_1: \exists\, j_1, j_2 \text{ sao cho } a_{j_1} \ne a_{j_2}$$

### Vì sao không so từng cặp?

Giáo trình nói thẳng (tr. 176): *"việc tách bài toán 4 thành nhiều bài toán 1 cho **sai số rất lớn**
và khối lượng tính toán rất đồ sộ khi $k$ lớn."*

📚 Đây chính là **vấn đề so sánh bội** ở bài 12 mục 9. Với $k = 5$ nhóm, có $C_5^2 = 10$ cặp;
chạy 10 kiểm định ở $\alpha = 0{,}05$ thì xác suất có ít nhất một kết quả sai là
$1 - 0{,}95^{10} = \mathbf{40\%}$.

**ANOVA giải quyết bằng cách kiểm tất cả cùng lúc, giữ $\alpha$ đúng 0,05.**

### ⭐ Ý tưởng: tách tổng bình phương

Giáo trình mô tả rất hay (tr. 176): *"các mẫu theo giả thiết đều có phân phối chuẩn **cùng phương sai**,
và do nhiều mẫu nên ta có **nhiều cách ước lượng phương sai đó**."*

Ký hiệu: $x_{ij}$ = quan sát thứ $i$ của nhóm $j$; $n_j$ = cỡ nhóm $j$; $n = \sum n_j$;
$\overline{X}_j$ = trung bình nhóm; $\overline{X}$ = trung bình chung.

**Đẳng thức tách (3.16)** — trái tim của ANOVA:

$$\underbrace{\sum_{j}\sum_{i}(x_{ij} - \overline{X})^2}_{\text{TOÀN BỘ}}
= \underbrace{\sum_{j}(\overline{X}_j - \overline{X})^2 n_j}_{\text{GIỮA các nhóm}}
+ \underbrace{\sum_{j}\sum_{i}(x_{ij} - \overline{X}_j)^2}_{\text{TRONG nhóm}}$$

> "Tổng thứ nhất bên phải đặc trưng cho sự **khác nhau giữa các nhóm**, còn tổng thứ hai —
> **giữa các số liệu trong nội bộ các nhóm**."

```
      biến thiên TOÀN BỘ  =  biến thiên GIỮA nhóm  +  biến thiên TRONG nhóm
           (tín hiệu + nhiễu)        (tín hiệu)              (nhiễu)

      Nếu H₀ đúng (các nhóm như nhau) → phần GIỮA chỉ là nhiễu → tỷ số ≈ 1
      Nếu H₀ sai  (các nhóm khác nhau) → phần GIỮA lớn        → tỷ số >> 1
```

**Bậc tự do cũng tách theo:** $\ (n-1) = (k-1) + (n-k)$

**Hai ước lượng phương sai (3.17):**

$$s_1^2 = \frac{\text{tổng bình phương GIỮA nhóm}}{k-1}, \qquad
s_2^2 = \frac{\text{tổng bình phương TRONG nhóm}}{n-k}$$

**Tiêu chuẩn (3.18):**

$$K = \frac{s_1^2}{s_2^2} \ \sim F(k-1;\ n-k) \text{ khi } H_0 \text{ đúng}$$

Miền tới hạn: $K > F_{k-1,\,n-k;\,1-\alpha}$ — **luôn một phía phải**.

⚠️ **Vì sao chỉ một phía?** Vì nếu các nhóm khác nhau thì $s_1^2$ chỉ có thể **lớn hơn** $s_2^2$,
không bao giờ nhỏ hơn một cách có ý nghĩa.

### Thí dụ 3.5 (tr. 178)

> Nồng độ haemoglobin ở 3 nhóm bệnh nhân mắc 3 dạng bệnh A, B, C. $\alpha = 0{,}05$.

Dữ liệu thô (41 quan sát) lưu ở [haemoglobin.csv](../thuc_hanh/du_lieu/haemoglobin.csv).

| Nhóm     |  $n_j$ |      Tổng | $\overline{X}_j$ |  $s_j$ |
| -------- | -----: | --------: | ---------------: | -----: |
| A        |     16 |     139,4 |           8,7125 | 0,8445 |
| B        |     10 |     106,3 |          10,6300 | 1,2841 |
| C        |     15 |     184,5 |          12,3000 | 0,9419 |
| **Tổng** | **41** | **430,2** |          10,4927 |        |

⚠️ Sách in $\overline{X}_1 = 8{,}7425$ trong bảng kết quả nhưng dùng **8,7125** trong phép tính.
Tính từ dữ liệu thô: $139{,}4/16 = \mathbf{8{,}7125}$ — con số dùng trong phép tính là đúng,
bảng in nhầm.

**Bảng ANOVA:**

| Nguồn         | Tổng bình phương | Bậc tự do | Trung bình bình phương |       $F$ |
| ------------- | ---------------: | --------: | ---------------------: | --------: |
| Giữa các nhóm |            99,89 |         2 |                  49,94 | **50,00** |
| Trong nhóm    |            37,96 |        38 |                 0,9989 |           |
| **Tổng**      |       **137,85** |    **40** |                        |           |

$F_{2,38;\,0{,}95} = 3{,}24$. Vì $50{,}00 \gg 3{,}24$ → **bác bỏ**: nồng độ haemoglobin của ba nhóm
bệnh **khác nhau đáng kể**.

(Sách in $K = 50{,}5$ vì dùng $s_2^2 = 0{,}99$ đã làm tròn; tính chính xác $s_2^2 = 0{,}9989$ cho
$K = 50{,}00$.)

### 💼 Góc QTKD

ANOVA trả lời các câu hỏi nhiều nhóm:

| Câu hỏi                                          | Nhân tố        | Nhóm |
| ------------------------------------------------ | -------------- | ---- |
| Bốn chi nhánh có doanh số như nhau không?        | chi nhánh      | 4    |
| Ba cách trưng bày có hiệu quả khác nhau không?   | cách trưng bày | 3    |
| Năm nhà cung cấp có chất lượng như nhau không?   | nhà cung cấp   | 5    |
| Doanh thu có khác nhau giữa các ngày trong tuần? | thứ trong tuần | 7    |

⚠️ **Ba điều kiện của ANOVA — kiểm trước khi dùng:**

1. **Các nhóm độc lập** với nhau.
2. **Trong mỗi nhóm, dữ liệu chuẩn** (hoặc $n_j$ đủ lớn nhờ CLT).
3. **Các nhóm cùng phương sai** (đồng nhất phương sai).

Điều kiện 3 hay bị vi phạm nhất. Kiểm bằng bài toán 3 (mục 3) từng cặp, hoặc bằng kiểm định Levene
(ngoài chương trình).

---

## 5. Kiểm định phù hợp

Sang §4, giáo trình chuyển từ kiểm định **tham số** sang kiểm định **phi tham số** — không giả định
dạng phân phối, mà **kiểm chính dạng phân phối đó**.

**Bài toán (tr. 179–180).** $H_0$: *"$X$ có hàm phân phối $F(x)$"* với $H_1$ đối lập.
Tiêu chuẩn dùng ở đây gọi là **tiêu chuẩn phù hợp**.

**Tiêu chuẩn Pearson (4.1):**

$$K = \sum_{i=1}^{k}\frac{(n_i - np_i)^2}{np_i} \ \xrightarrow{\ L\ } \chi^2(k - r - 1)$$

trong đó:
- $n_i$ = **tần số quan sát** ở lớp $i$;
- $np_i$ = **tần số lý thuyết** nếu $H_0$ đúng;
- $r$ = **số tham số phải ước lượng** từ dữ liệu.

**Cách nhớ:**

$$K = \sum \frac{(\text{quan sát} - \text{kỳ vọng})^2}{\text{kỳ vọng}}$$

> "Rõ ràng $K$ càng bé thì phân phối xác suất của $X$ càng gần $F(x)$." (tr. 180)

Miền tới hạn (4.2): $K > \chi^2_{k-r-1;\,1-\alpha}$ — **luôn một phía phải**.

### ⚠️ Ba điều kiện áp dụng

1. **$n_i$ không quá bé** — giáo trình yêu cầu $n_i \ge 5$, *"có thể chấp nhận ngoại lệ cho khoảng
   đầu và cuối"*. Nếu có lớp quá nhỏ, phải **gộp** với lớp bên cạnh.
2. **Trừ bậc tự do cho mỗi tham số ước lượng.** Nếu $F(x)$ chứa tham số chưa biết, *"ta phải thay thế
   chúng bằng các **ước lượng hợp lý nhất**"* (bài 11 mục 3), và mỗi tham số ước lượng làm **giảm
   một bậc tự do**.
3. **Với biến liên tục**, khi tính $p_i = F(x_i) - F(x_{i-1})$ thì lấy $x_0 = -\infty$ và
   $x_k = +\infty$ để tổng $p_i$ bằng đúng 1.

**Bảng bậc tự do:**

| Kiểm định                         |  $r$ | Bậc tự do |
| --------------------------------- | ---: | --------- |
| Phân phối đều (biết hết)          |    0 | $k - 1$   |
| Poisson (ước lượng $\lambda$)    |    1 | $k - 2$   |
| Chuẩn (ước lượng $a$ và $\sigma$) |    2 | $k - 3$   |

### Thí dụ 4.1 (tr. 181)

> Quan sát một thiết bị có 10 trạng thái, 75 lần:

| Trạng thái   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Số lần $n_i$ | 5   | 8   | 3   | 11  | 4   | 5   | 4   | 14  | 13  | 8   |

> $\alpha = 0{,}05$: vai trò các trạng thái có như nhau không?

$H_0$: $X$ có phân phối **đều rời rạc**, $p_i = 0{,}1$. Tần số lý thuyết $np_i = 7{,}5$ cho mọi lớp.

$$K_{tn} = \sum_{i=1}^{10}\frac{(n_i - 7{,}5)^2}{7{,}5} = \frac{142{,}5}{7{,}5} = \mathbf{19{,}0}$$

$r = 0$ (không ước lượng gì), bậc tự do $= 10 - 0 - 1 = 9$. $\chi^2_{9;\,0{,}95} = 16{,}92$.

Vì $19{,}0 > 16{,}92$ → **bác bỏ**: các trạng thái **không đều nhau**.

💼 Ứng dụng: kiểm tra xem máy quay số trúng thưởng có công bằng không, kiểm tra dữ liệu có bị làm giả
không (định luật Benford), kiểm tra khách hàng có phân bố đều giữa các khung giờ không.

---

## 6. Kiểm định độc lập

**Bài toán (tr. 184).** Kiểm định **tính độc lập của hai đặc tính**.

Lập **bảng liên hợp** $r \times s$ với $n_{ij}$ = số lần quan sát có đồng thời thuộc tính $i$ của $X$
và thuộc tính $j$ của $Y$.

Từ bài 8 mục 1, độc lập nghĩa là $p(i,j) = p_X(i)\,p_Y(j)$. Ước lượng bằng tần suất:

$$\hat{p}_X(i) = \frac{n_i}{n}, \qquad \hat{p}_Y(j) = \frac{m_j}{n}$$

trong đó $n_i$ = tổng hàng $i$, $m_j$ = tổng cột $j$.

**Tiêu chuẩn (4.4):**

$$K = n\left(\sum_{i=1}^{r}\sum_{j=1}^{s}\frac{n_{ij}^2}{n_i\, m_j} - 1\right)
\ \sim \chi^2\big((r-1)(s-1)\big)$$

Dạng tương đương, dễ hiểu hơn — cùng khuôn với (4.1):

$$K = \sum_{i}\sum_{j}\frac{(n_{ij} - e_{ij})^2}{e_{ij}}, \qquad
\boxed{e_{ij} = \frac{n_i \times m_j}{n}}$$

⭐ **Công thức tần số kỳ vọng $e_{ij}$ rất đáng nhớ**: *tổng hàng nhân tổng cột chia tổng chung*.
Đó chính là "nếu độc lập thì ô này phải có bao nhiêu".

**Bậc tự do $(r-1)(s-1)$** — vì biết $r-1$ tổng hàng và $s-1$ tổng cột là suy ra được phần còn lại.

### Thí dụ 4.4 (tr. 185)

> Khảo sát màu mắt và màu tóc của 6.800 người Pháp:

| Mắt \ Tóc |     Vàng |      Nâu |      Đen |    Hung | **Tổng** |
| --------- | -------: | -------: | -------: | ------: | -------: |
| Xanh      |     1768 |      807 |      189 |      47 | **2811** |
| Ghi       |      946 |     1387 |      746 |      53 | **3132** |
| Nâu       |      115 |      438 |      288 |      16 |  **857** |
| **Tổng**  | **2829** | **2632** | **1223** | **116** | **6800** |

$H_0$: màu mắt và màu tóc **độc lập**. Bậc tự do $= (3-1)(4-1) = 6$, $\chi^2_{6;\,0{,}95} = 12{,}59$.

$$K_{tn} = \mathbf{1073{,}5} \ \ggg \ 12{,}59$$

→ **bác bỏ** áp đảo: màu mắt và màu tóc **không độc lập**.

(Sách in 1075; tính lại từ bảng được 1073,5. Chênh do làm tròn trung gian, kết luận không đổi.)

### 💼 Góc QTKD — kiểm định $\chi^2$ độc lập là công cụ dùng nhiều nhất

Đây chính là **kiểm chứng bảng chéo** của bài 8 mục 2 — giờ có công cụ để nói *"khác biệt này có
thật hay chỉ là ngẫu nhiên"*.

| Bảng chéo                         | Câu hỏi                                |
| --------------------------------- | -------------------------------------- |
| Kênh quảng cáo × có mua/không mua | kênh nào hiệu quả hơn, hay như nhau?   |
| Khu vực × loại sản phẩm ưa thích  | có nên làm chiến lược riêng theo vùng? |
| Phân khúc khách × mức hài lòng    | có phân khúc nào đang bị bỏ rơi?       |
| Ca làm việc × tỷ lệ lỗi           | ca đêm có tệ hơn thật không?           |

⭐ **Nếu bác bỏ $H_0$ độc lập thì việc phân khúc là CÓ giá trị** (bài 8 mục 3 đã nói: độc lập ⟹
phân khúc vô nghĩa). Đây là bài kiểm tra định lượng cho quyết định "có nên phân khúc không".

⚠️ **Ba cảnh báo:**

1. **Điều kiện $e_{ij} \ge 5$** cho hầu hết các ô. Bảng có nhiều ô nhỏ thì phải gộp nhóm.
2. **$n$ lớn thì $K$ luôn lớn.** Với 6.800 quan sát, khác biệt nhỏ xíu cũng cho $K$ khổng lồ.
   Đây lại là vấn đề "có ý nghĩa thống kê ≠ quan trọng thực tế" (bài 12 mục 9).
   Nên báo cáo thêm **độ mạnh liên hệ** (ví dụ hệ số Cramér's V), không chỉ giá trị p.
3. **$\chi^2$ chỉ nói CÓ liên hệ**, không nói liên hệ theo chiều nào. Phải nhìn bảng để diễn giải —
   ví dụ ở đây: mắt xanh đi với tóc vàng, mắt nâu đi với tóc đen.

---

## 7. 📚 Quy trình chọn kiểm định

Giáo trình trình bày sáu bài toán rời rạc. Cây quyết định này là phần bổ sung.

```
   Bạn đang so sánh cái gì?
   │
   ├── MỘT nhóm với MỘT SỐ cho trước ────────────────────► BÀI 12
   │
   ├── HAI nhóm
   │    │
   │    ├── Đo TRUNG BÌNH
   │    │    ├── cùng đối tượng đo 2 lần?  → MẪU CẶP: lấy hiệu → bài 12
   │    │    └── hai nhóm khác nhau (độc lập):
   │    │         ├── n₁,n₂ > 30    → (3.1) với s₁,s₂ riêng, tra bảng chuẩn
   │    │         └── n nhỏ:
   │    │              ├── KIỂM PHƯƠNG SAI TRƯỚC bằng (3.12)!
   │    │              ├── cùng phương sai  → (3.5), t(n₁+n₂−2)
   │    │              └── khác phương sai  → dùng (3.1) với s riêng
   │    │                                     (Welch, ngoài chương trình)
   │    │
   │    ├── Đo TỶ LỆ         → (3.9) với f gộp, tra bảng chuẩn
   │    └── Đo PHƯƠNG SAI    → (3.12), tra bảng Fisher F(n₁−1; n₂−1)
   │
   ├── BA nhóm trở lên, đo TRUNG BÌNH ──► ANOVA (3.18), F(k−1; n−k)
   │    ⚠ KHÔNG so từng cặp — sai số cộng dồn (bài 12 mục 9)
   │
   └── Kiểm chính DẠNG PHÂN PHỐI hoặc QUAN HỆ
        ├── "dữ liệu có theo phân phối F không?" → PHÙ HỢP (4.1), χ²(k−r−1)
        └── "hai đặc tính có độc lập không?"     → ĐỘC LẬP (4.4), χ²((r−1)(s−1))
```

### Bảng tra nhanh — sáu bài toán của bài này

| #   | So sánh                               | Tiêu chuẩn | Phân phối | Bậc tự do         |
| --- | ------------------------------------- | ---------- | --------- | ----------------- |
| 1   | hai kỳ vọng, biết $\sigma$            | (3.1)      | $N(0;1)$  | —                 |
| 1'  | hai kỳ vọng, $n$ nhỏ, cùng $\sigma^2$ | (3.5)      | $t$       | $n_1+n_2-2$       |
| 2   | hai tỷ lệ                             | (3.9)      | $N(0;1)$  | —                 |
| 3   | hai phương sai                        | (3.12)     | $F$       | $(n_1-1;\ n_2-1)$ |
| 4   | $k$ kỳ vọng (ANOVA)                   | (3.18)     | $F$       | $(k-1;\ n-k)$     |
| 5   | dạng phân phối                        | (4.1)      | $\chi^2$  | $k-r-1$           |
| 6   | tính độc lập                          | (4.4)      | $\chi^2$  | $(r-1)(s-1)$      |

⭐ **Ba kiểm định cuối đều dùng $\chi^2$ hoặc $F$ và đều là kiểm định MỘT PHÍA PHẢI.**
Dễ nhớ: chúng đo *"lệch bao nhiêu so với mô hình"*, mà lệch thì chỉ có thể theo một chiều.

---

## 8. 📚 Sau ANOVA thì làm gì

Giáo trình dừng ở chỗ ANOVA bác bỏ $H_0$. Nhưng kết luận *"ba nhóm khác nhau"* chưa đủ để ra quyết định —
**nhóm nào khác nhóm nào?**

Đây gọi là **so sánh hậu nghiệm** (post-hoc). Ngoài chương trình nhưng cần biết:

**Cách 1 — Bonferroni (đơn giản nhất, học được ngay).**
Chạy tất cả $C_k^2$ cặp bằng bài toán 1, nhưng dùng mức ý nghĩa $\alpha/C_k^2$ thay vì $\alpha$.

Với $k = 3$: có 3 cặp, dùng $\alpha = 0{,}05/3 = 0{,}0167$.

⚠️ Cách này **thận trọng quá mức** khi $k$ lớn — dễ bỏ lọt khác biệt thật.

**Cách 2 — Tukey HSD** (dùng phân phối khoảng có studentised, ngoài chương trình): chuẩn mực trong
thực hành, ít thận trọng quá mức hơn.

### 💼 Và trước cả ANOVA: quan trọng hơn là VẼ ĐỒ THỊ

Trước khi chạy bất kỳ kiểm định nào, hãy vẽ:

- **Biểu đồ hộp (boxplot)** cho từng nhóm — thấy ngay trung vị, độ phân tán, giá trị thái quá.
- **Biểu đồ phân tán** nếu có hai biến liên tục (bài 8 mục 9).

Rất nhiều lần đồ thị cho câu trả lời trước khi kiểm định cho, và nó phát hiện được những thứ
kiểm định bỏ sót: nhóm có hai đỉnh, giá trị nhập sai, xu hướng theo thời gian.

### Danh sách kiểm cho một báo cáo so sánh

```
   ☐ Đã vẽ đồ thị từng nhóm trước khi tính?
   ☐ Mẫu độc lập hay mẫu cặp?           (nhầm là sai công thức)
   ☐ Đã kiểm ĐỒNG NHẤT PHƯƠNG SAI chưa? (điều kiện của (3.5) và ANOVA)
   ☐ Cỡ mẫu đủ để phát hiện khác biệt đáng quan tâm?  (lực lượng, bài 12)
   ☐ Có so nhiều cặp không? Đã hiệu chỉnh Bonferroni chưa?
   ☐ Đã báo cáo ĐỘ LỚN khác biệt + KHOẢNG TIN CẬY, không chỉ giá trị p?
   ☐ Nếu ANOVA bác bỏ: đã làm so sánh hậu nghiệm để biết nhóm nào khác?
```

---

## 9. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.
> Chạy từ thư mục gốc khoá học: `cd houedu/xacxuatthongke && python3 bai-13-nhieu-mau.py`.
> Dùng module [thuc_hanh/bang_tra.py](../thuc_hanh/bang_tra.py) (bảng $t$, $\chi^2$, $F$).

Hai tệp dữ liệu mới:

| Tệp                                                     | Nội dung                       | Nguồn               |
| ------------------------------------------------------- | ------------------------------ | ------------------- |
| [haemoglobin.csv](../thuc_hanh/du_lieu/haemoglobin.csv) | 41 quan sát, 3 nhóm bệnh       | thí dụ 3.5, tr. 178 |
| [mat_toc.csv](../thuc_hanh/du_lieu/mat_toc.csv)         | bảng liên hợp 3×4, 6.800 người | thí dụ 4.4, tr. 185 |

Cả hai là **số liệu nguyên văn của giáo trình**.

```python
"""Bài 13 — Kiểm định nhiều mẫu, phân tích phương sai và kiểm định phi tham số."""

import csv
import math
import pathlib
import sys

sys.path.append("thuc_hanh")
from bang_tra import Z, chi2_quantile, f_quantile, t_quantile, z_quantile

DATA = pathlib.Path("thuc_hanh/du_lieu")
kl = lambda bac_bo: "BAC BO H0" if bac_bo else "CHUA CO CO SO BAC BO H0"

# ─────────────────────────────────────────────────────────────
# 1. SO SÁNH HAI KỲ VỌNG — Thí dụ 3.1 (tr. 171) va 3.2 (tr. 172)
#    Cong thuc (3.5): phuong sai gop (pooled)
# ─────────────────────────────────────────────────────────────
def t_two_sample(n1, m1, v1, n2, m2, v2):
    """Tieu chuan (3.5) — hai mau doc lap, GIA THIET cung phuong sai.
    v1, v2 la PHUONG SAI mau hieu chinh (s^2)."""
    sp2 = ((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2)
    return (m1 - m2) / math.sqrt(sp2 * (1 / n1 + 1 / n2)), n1 + n2 - 2


print("THI DU 3.1 — trong luong so sinh: me KHONG hut thuoc vs me HUT")
n1, m1, s1 = 15, 3.5933, 0.3707
n2, m2, s2 = 14, 3.2029, 0.4927
K, df = t_two_sample(n1, m1, s1**2, n2, m2, s2**2)
tb = t_quantile(0.95, df)
print(f"  n1={n1} X1={m1} s1={s1} | n2={n2} X2={m2} s2={s2}")
print(f"  H0: a1 = a2   H1: a1 > a2  (mot phia PHAI)")
print(f"  K = {K:.4f}   (sach: 2,42)   t({df}; 0,95) = {tb:.4f}   (sach: 1,703)")
print(f"  -> {kl(K > tb)}: tre nhom me KHONG hut thuoc NANG HON")

print()
print("THI DU 3.2 — nang suat lua my o hai vung")
n1, m1, v1 = 9, 24.6, 0.24
n2, m2, v2 = 16, 25.8, 0.16
K, df = t_two_sample(n1, m1, v1, n2, m2, v2)
tb = t_quantile(0.975, df)
print(f"  n1={n1} X1={m1} s1^2={v1} | n2={n2} X2={m2} s2^2={v2}")
print(f"  H0: a1 = a2   H1: a1 != a2  (hai phia)")
print(f"  K = {K:.4f}   (sach: -6,67)   t({df}; 0,975) = {tb:.4f}   (sach: 2,069)")
print(f"  -> {kl(abs(K) > tb)}: nang suat hai vung KHAC NHAU")

# ─────────────────────────────────────────────────────────────
# 2. SO SÁNH HAI TỶ LỆ — Thí dụ 3.3 (tr. 173)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 3.3 — hai lo hang: 50/500 va 60/400 phe pham")
n1, m1_, n2, m2_ = 500, 50, 400, 60
f1, f2 = m1_ / n1, m2_ / n2
f = (m1_ + m2_) / (n1 + n2)
K = (f1 - f2) / math.sqrt(f * (1 - f) * (1 / n1 + 1 / n2))
print(f"  f1 = {f1}   f2 = {f2}   f gop = {m1_ + m2_}/{n1 + n2} = {f:.5f}"
      f"   (sach lam tron: 0,12)")
print(f"  K = {K:.4f}   (sach: -2,276)")
print(f"  a) H1: p1 != p2, z = {z_quantile(0.975):.4f}"
      f"  ->  {kl(abs(K) > z_quantile(0.975))}")
print(f"  b) H1: p1 < p2,  z = {z_quantile(0.05):.4f}"
      f"  ->  {kl(K < z_quantile(0.05))}")
print("     => Ty le phe pham lo 1 THAP HON dang ke so voi lo 2")
# Cach khong gop phuong sai (sach goi la 'tinh xap xi')
K2 = (f1 - f2) / math.sqrt(f1 * (1 - f1) / n1 + f2 * (1 - f2) / n2)
print(f"  Cach KHONG gop phuong sai: K = {K2:.4f}   (sach in: -2,56)")
print(f"  ⚠ Tinh lai duoc {K2:.4f}, khong phai -2,56. Ket luan khong doi.")

# ─────────────────────────────────────────────────────────────
# 3. SO SÁNH HAI PHƯƠNG SAI — Thí dụ 3.4 (tr. 175)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 3.4 — toc do dau dan cua hai cong ty")
n1, m1, v1 = 10, 1210, 2500
n2, m2, v2 = 10, 1175, 3600
K = max(v1, v2) / min(v1, v2)
fb = f_quantile(0.95, n2 - 1, n1 - 1)
print(f"  Buoc 1 — kiem dinh CUNG PHUONG SAI truoc:")
print(f"    H0: sigma1^2 = sigma2^2   K = {v2}/{v1} = {K:.4f}")
print(f"    ⚠ Sach tinh 3600/2550 = 1,41 — de bai ghi s1^2 = 2500,"
      " khong phai 2550.")
print(f"    F({n2 - 1}; {n1 - 1}; 0,95) = {fb:.4f}   (sach: 3,18)"
      f"  ->  {kl(K > fb)}")
print(f"  Buoc 2 — gio moi duoc dung (3.5) de so hai ky vong:")
K2, df = t_two_sample(n1, m1, v1, n2, m2, v2)
tb = t_quantile(0.975, df)
print(f"    K = {K2:.4f}   (sach: 1,42, dung 2550)")
print(f"    t({df}; 0,975) = {tb:.4f}   (sach: 2,101)  ->  {kl(abs(K2) > tb)}")

# ─────────────────────────────────────────────────────────────
# 4. PHÂN TÍCH PHƯƠNG SAI MỘT NHÂN TỐ — Thí dụ 3.5 (tr. 178)
# ─────────────────────────────────────────────────────────────
print()
with open(DATA / "haemoglobin.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
groups = {}
for r in rows:
    groups.setdefault(r["nhom"], []).append(float(r["nong_do"]))

print("THI DU 3.5 — nong do haemoglobin o 3 nhom benh nhan (ANOVA)")
n = sum(len(v) for v in groups.values())
k = len(groups)
grand = sum(sum(v) for v in groups.values()) / n
print(f"{'nhom':>6}{'nj':>5}{'tong':>9}{'Xj':>10}{'sj':>9}")
for g, v in groups.items():
    nj = len(v)
    mj = sum(v) / nj
    sj = math.sqrt(sum((x - mj) ** 2 for x in v) / (nj - 1))
    print(f"{g:>6}{nj:>5}{sum(v):>9.1f}{mj:>10.4f}{sj:>9.4f}")
print(f"  n = {n}   k = {k}   X chung = {grand:.4f}"
      f"   (sach: 8,7125 / 10,63 / 12,30 va s = 0,8445 / 1,2841 / 0,9419)")

# Tach tong binh phuong: S^2 = S1^2 (giua nhom) + S2^2 (trong nhom)
ss_total = sum((x - grand) ** 2 for v in groups.values() for x in v)
ss_between = sum(len(v) * (sum(v) / len(v) - grand) ** 2 for v in groups.values())
ss_within = ss_total - ss_between
print()
print(f"  Tong binh phuong TOAN BO   S^2  = {ss_total:.2f}   (sach: 137,85)")
print(f"  Tong binh phuong GIUA nhom      = {ss_between:.2f}"
      f"   (bac tu do k-1 = {k - 1})")
print(f"  Tong binh phuong TRONG nhom     = {ss_within:.2f}"
      f"   (bac tu do n-k = {n - k})")
print(f"  Kiem tach: {ss_between:.2f} + {ss_within:.2f} = {ss_between + ss_within:.2f}"
      f"  ->  khop: {math.isclose(ss_between + ss_within, ss_total)}")

s1_2 = ss_between / (k - 1)
s2_2 = ss_within / (n - k)
K = s1_2 / s2_2
fb = f_quantile(0.95, k - 1, n - k)
print()
print(f"  s1^2 (giua)  = {ss_between:.2f}/{k - 1} = {s1_2:.2f}   (sach: 49,94)")
print(f"  s2^2 (trong) = {ss_within:.2f}/{n - k} = {s2_2:.4f}   (sach: 0,99)")
print(f"  K = s1^2/s2^2 = {K:.2f}   (sach: 50,5)")
print(f"  F({k - 1}; {n - k}; 0,95) = {fb:.4f}   (sach: 3,24)  ->  {kl(K > fb)}")
print("  => Nong do haemoglobin cua 3 nhom benh KHAC NHAU dang ke")

# Bang ANOVA chuan — dang moi phan mem deu in ra
print()
print("  BANG ANOVA (dang chuan):")
print(f"  {'Nguon':<14}{'Tong b.phuong':>15}{'Bac tu do':>11}{'Trung binh b.p':>16}"
      f"{'F':>9}")
print(f"  {'Giua cac nhom':<14}{ss_between:>15.2f}{k - 1:>11}{s1_2:>16.2f}{K:>9.2f}")
print(f"  {'Trong nhom':<14}{ss_within:>15.2f}{n - k:>11}{s2_2:>16.4f}")
print(f"  {'TONG':<14}{ss_total:>15.2f}{n - 1:>11}")

# ─────────────────────────────────────────────────────────────
# 5. KIỂM ĐỊNH PHÙ HỢP (chi bình phương Pearson) — Thí dụ 4.1 (tr. 181)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.1 — 10 trang thai thiet bi, 75 lan quan sat; deu khong?")
obs = [5, 8, 3, 11, 4, 5, 4, 14, 13, 8]
n = sum(obs)
exp = [n / len(obs)] * len(obs)
K = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
df = len(obs) - 1                    # khong uoc luong tham so nao -> r = 0
cb = chi2_quantile(0.95, df)
print(f"  n = {n}   moi trang thai ky vong npi = {exp[0]}")
print(f"{'trang thai':>12}{'quan sat':>10}{'ky vong':>10}{'(O-E)^2/E':>12}")
for i, (o, e) in enumerate(zip(obs, exp), 1):
    print(f"{i:>12}{o:>10}{e:>10.1f}{(o - e) ** 2 / e:>12.4f}")
print(f"  K = {K:.4f}   (sach: 19,0)")
print(f"  chi2({df}; 0,95) = {cb:.4f}   (sach: 16,92)  ->  {kl(K > cb)}")
print("  => Cac trang thai KHONG deu nhau")

# ─────────────────────────────────────────────────────────────
# 6. KIỂM ĐỊNH ĐỘC LẬP — Thí dụ 4.4 (tr. 185), mau mat x mau toc
# ─────────────────────────────────────────────────────────────
print()
with open(DATA / "mat_toc.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
cols = [c for c in rows[0] if c != "mat"]
table = [[int(r[c]) for c in cols] for r in rows]
r_, s_ = len(table), len(cols)
row_tot = [sum(row) for row in table]
col_tot = [sum(table[i][j] for i in range(r_)) for j in range(s_)]
N = sum(row_tot)

print("THI DU 4.4 — mau mat x mau toc cua 6800 nguoi Phap")
print(f"  {'':>8}" + "".join(f"{c[4:]:>9}" for c in cols) + f"{'tong':>9}")
for i, row in enumerate(table):
    print(f"  {rows[i]['mat']:>8}" + "".join(f"{v:>9}" for v in row)
          + f"{row_tot[i]:>9}")
print(f"  {'tong':>8}" + "".join(f"{v:>9}" for v in col_tot) + f"{N:>9}")

K = 0.0
for i in range(r_):
    for j in range(s_):
        e = row_tot[i] * col_tot[j] / N
        K += (table[i][j] - e) ** 2 / e
df = (r_ - 1) * (s_ - 1)
cb = chi2_quantile(0.95, df)
print(f"  K = {K:.1f}   (sach: 1075)")
print(f"  Bac tu do = ({r_}-1)({s_}-1) = {df}"
      f"   chi2({df}; 0,95) = {cb:.4f}   (sach: 12,59)")
print(f"  -> {kl(K > cb)}: mau mat va mau toc KHONG doc lap")

# ─────────────────────────────────────────────────────────────
# 7. 💼 GÓC QTKD — ANOVA tren du lieu doanh thu, tach theo loai ngay
# ─────────────────────────────────────────────────────────────
print()
with open(DATA / "doanh_thu_ngay.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
g1 = [float(r["doanh_thu_trieu"]) for r in rows if r["loai_ngay"] == "trong tuan"]
g2 = [float(r["doanh_thu_trieu"]) for r in rows if r["loai_ngay"] == "T7/CN"]
print("💼 GOC QTKD — doanh thu ngay trong tuan vs cuoi tuan")
for lbl, g in [("trong tuan", g1), ("T7/CN     ", g2)]:
    m_ = sum(g) / len(g)
    v_ = sum((x - m_) ** 2 for x in g) / (len(g) - 1)
    print(f"  {lbl}  n={len(g):>3}  X={m_:>6.2f}  s={math.sqrt(v_):>5.2f}")

# Buoc 1: hai phuong sai co bang nhau khong?
v1 = sum((x - sum(g1) / len(g1)) ** 2 for x in g1) / (len(g1) - 1)
v2 = sum((x - sum(g2) / len(g2)) ** 2 for x in g2) / (len(g2) - 1)
Kf = max(v1, v2) / min(v1, v2)
fb = f_quantile(0.975, len(g2) - 1, len(g1) - 1)
print(f"  Buoc 1 — H0: sigma1^2 = sigma2^2. F = {Kf:.3f}"
      f"   F({len(g2) - 1};{len(g1) - 1};0,975) = {fb:.3f}  ->  {kl(Kf > fb)}")
print("     => PHUONG SAI KHAC NHAU -> KHONG duoc dung cong thuc (3.5) gop!")

# Buoc 2: dung xap xi mau lon (3.1) voi s1, s2 rieng — khong gop
Kz = (sum(g2) / len(g2) - sum(g1) / len(g1)) / math.sqrt(v2 / len(g2) + v1 / len(g1))
print(f"  Buoc 2 — dung (3.1) voi s1, s2 RIENG (khong gop):")
print(f"     K = {Kz:.4f}   z(0,975) = {z_quantile(0.975):.4f}"
      f"  ->  {kl(abs(Kz) > z_quantile(0.975))}")
print(f"     gia tri p = {2 * (1 - Z.cdf(abs(Kz))):.5f}")
print("  => Cuoi tuan doanh thu CAO HON dang ke, va cung BIEN DONG MANH HON.")
print("     Hai ket luan doi hoi hai quyet dinh quan tri khac nhau:")
print("     tang nhan su cuoi tuan, va du tru ton kho rong hon cho cuoi tuan.")
```

Kết quả chạy thật:

```
THI DU 3.1 — trong luong so sinh: me KHONG hut thuoc vs me HUT
  n1=15 X1=3.5933 s1=0.3707 | n2=14 X2=3.2029 s2=0.4927
  H0: a1 = a2   H1: a1 > a2  (mot phia PHAI)
  K = 2.4221   (sach: 2,42)   t(27; 0,95) = 1.7033   (sach: 1,703)
  -> BAC BO H0: tre nhom me KHONG hut thuoc NANG HON

THI DU 3.2 — nang suat lua my o hai vung
  n1=9 X1=24.6 s1^2=0.24 | n2=16 X2=25.8 s2^2=0.16
  H0: a1 = a2   H1: a1 != a2  (hai phia)
  K = -6.6453   (sach: -6,67)   t(23; 0,975) = 2.0687   (sach: 2,069)
  -> BAC BO H0: nang suat hai vung KHAC NHAU

THI DU 3.3 — hai lo hang: 50/500 va 60/400 phe pham
  f1 = 0.1   f2 = 0.15   f gop = 110/900 = 0.12222   (sach lam tron: 0,12)
  K = -2.2756   (sach: -2,276)
  a) H1: p1 != p2, z = 1.9600  ->  BAC BO H0
  b) H1: p1 < p2,  z = -1.6449  ->  BAC BO H0
     => Ty le phe pham lo 1 THAP HON dang ke so voi lo 2
  Cach KHONG gop phuong sai: K = -2.2389   (sach in: -2,56)
  ⚠ Tinh lai duoc -2.2389, khong phai -2,56. Ket luan khong doi.

THI DU 3.4 — toc do dau dan cua hai cong ty
  Buoc 1 — kiem dinh CUNG PHUONG SAI truoc:
    H0: sigma1^2 = sigma2^2   K = 3600/2500 = 1.4400
    ⚠ Sach tinh 3600/2550 = 1,41 — de bai ghi s1^2 = 2500, khong phai 2550.
    F(9; 9; 0,95) = 3.1789   (sach: 3,18)  ->  CHUA CO CO SO BAC BO H0
  Buoc 2 — gio moi duoc dung (3.5) de so hai ky vong:
    K = 1.4171   (sach: 1,42, dung 2550)
    t(18; 0,975) = 2.1009   (sach: 2,101)  ->  CHUA CO CO SO BAC BO H0

THI DU 3.5 — nong do haemoglobin o 3 nhom benh nhan (ANOVA)
  nhom   nj     tong        Xj       sj
     A   16    139.4    8.7125   0.8445
     B   10    106.3   10.6300   1.2841
     C   15    184.5   12.3000   0.9419
  n = 41   k = 3   X chung = 10.4927   (sach: 8,7125 / 10,63 / 12,30 va s = 0,8445 / 1,2841 / 0,9419)

  Tong binh phuong TOAN BO   S^2  = 137.85   (sach: 137,85)
  Tong binh phuong GIUA nhom      = 99.89   (bac tu do k-1 = 2)
  Tong binh phuong TRONG nhom     = 37.96   (bac tu do n-k = 38)
  Kiem tach: 99.89 + 37.96 = 137.85  ->  khop: True

  s1^2 (giua)  = 99.89/2 = 49.94   (sach: 49,94)
  s2^2 (trong) = 37.96/38 = 0.9989   (sach: 0,99)
  K = s1^2/s2^2 = 50.00   (sach: 50,5)
  F(2; 38; 0,95) = 3.2448   (sach: 3,24)  ->  BAC BO H0
  => Nong do haemoglobin cua 3 nhom benh KHAC NHAU dang ke

  BANG ANOVA (dang chuan):
  Nguon           Tong b.phuong  Bac tu do  Trung binh b.p        F
  Giua cac nhom           99.89          2           49.94    50.00
  Trong nhom              37.96         38          0.9989
  TONG                   137.85         40

THI DU 4.1 — 10 trang thai thiet bi, 75 lan quan sat; deu khong?
  n = 75   moi trang thai ky vong npi = 7.5
  trang thai  quan sat   ky vong   (O-E)^2/E
           1         5       7.5      0.8333
           2         8       7.5      0.0333
           3         3       7.5      2.7000
           4        11       7.5      1.6333
           5         4       7.5      1.6333
           6         5       7.5      0.8333
           7         4       7.5      1.6333
           8        14       7.5      5.6333
           9        13       7.5      4.0333
          10         8       7.5      0.0333
  K = 19.0000   (sach: 19,0)
  chi2(9; 0,95) = 16.9190   (sach: 16,92)  ->  BAC BO H0
  => Cac trang thai KHONG deu nhau

THI DU 4.4 — mau mat x mau toc cua 6800 nguoi Phap
               vang      nau      den     hung     tong
      Xanh     1768      807      189       47     2811
       Ghi      946     1387      746       53     3132
       Nau      115      438      288       16      857
      tong     2829     2632     1223      116     6800
  K = 1073.5   (sach: 1075)
  Bac tu do = (3-1)(4-1) = 6   chi2(6; 0,95) = 12.5916   (sach: 12,59)
  -> BAC BO H0: mau mat va mau toc KHONG doc lap

💼 GOC QTKD — doanh thu ngay trong tuan vs cuoi tuan
  trong tuan  n= 44  X= 50.05  s= 9.33
  T7/CN       n= 16  X= 69.53  s=23.21
  Buoc 1 — H0: sigma1^2 = sigma2^2. F = 6.190   F(15;43;0,975) = 2.156  ->  BAC BO H0
     => PHUONG SAI KHAC NHAU -> KHONG duoc dung cong thuc (3.5) gop!
  Buoc 2 — dung (3.1) voi s1, s2 RIENG (khong gop):
     K = 3.2622   z(0,975) = 1.9600  ->  BAC BO H0
     gia tri p = 0.00111
  => Cuoi tuan doanh thu CAO HON dang ke, va cung BIEN DONG MANH HON.
     Hai ket luan doi hoi hai quyet dinh quan tri khac nhau:
     tang nhan su cuoi tuan, va du tru ton kho rong hon cho cuoi tuan.
```

Sáu điểm đáng để ý:

1. **Dòng `Kiem tach: 99.89 + 37.96 = 137.85 -> khop: True`** — đẳng thức (3.16) được kiểm bằng số.
   Đây là cách tốt nhất để tin rằng mình hiểu đúng ANOVA: hai phần **phải** cộng lại đúng bằng tổng.
2. **Bảng ANOVA cuối** đúng dạng mọi phần mềm in ra. Nhìn quen dạng này thì đọc được kết quả
   của Excel, SPSS, R mà không cần học lại.
3. **Thí dụ 3.5**: cột $\overline{X}_j$ tính từ dữ liệu thô cho `8.7125`, xác nhận con số dùng trong
   phép tính của sách (bảng in nhầm 8,7425).
4. **Thí dụ 4.1**: cột `(O-E)^2/E` cho thấy trạng thái 8 đóng góp 5,63 trong tổng 19,0 —
   gần một phần ba. Nhìn cột này biết ngay **chỗ nào lệch nhiều nhất**, thứ mà con số $K$ tổng không cho.
5. **Thí dụ 4.4**: $K = 1073{,}5$ so với ngưỡng $12{,}59$ — vượt **85 lần**. Với $n = 6800$,
   liên hệ mạnh đến mức không cần kiểm định cũng thấy.
6. **Góc QTKD** minh hoạ đúng quy trình hai bước: bước 1 phát hiện **phương sai khác nhau**
   ($F = 6{,}19 > 2{,}16$), nên **không được** dùng công thức gộp (3.5), phải chuyển sang (3.1)
   với $s_1$, $s_2$ riêng. Đây là chi tiết mà rất nhiều báo cáo bỏ qua.

---

## 10. Tự thử

1. Ở thí dụ 3.1, đổi đối thuyết sang hai phía ($H_1: a_1 \ne a_2$). Kết luận có đổi không?
   Ngưỡng đổi từ 1,703 thành bao nhiêu?
2. Ở thí dụ 3.3, tính **khoảng tin cậy 95% cho hiệu $p_1 - p_2$** (dùng công thức bài 11
   với $\sqrt{f_1(1-f_1)/n_1 + f_2(1-f_2)/n_2}$). Khoảng đó có chứa 0 không?
   So với kết luận kiểm định.
3. Trong ANOVA thí dụ 3.5, bỏ nhóm B đi và chạy lại với 2 nhóm. So $F$ thu được với $K^2$ của
   kiểm định $t$ hai mẫu trên cùng dữ liệu. Có bằng nhau không? (Gợi ý: bài 7 mục 8, $t^2 \sim F(1,m)$.)
4. Làm **so sánh hậu nghiệm Bonferroni** cho thí dụ 3.5: chạy 3 kiểm định $t$ cho 3 cặp
   (A–B, A–C, B–C) ở mức $\alpha = 0{,}05/3$. Cặp nào khác nhau có ý nghĩa?
5. Ở thí dụ 4.1, gộp 10 trạng thái thành 5 cặp (1+2, 3+4, ...). $K$ và bậc tự do đổi thế nào?
   Kết luận có đổi không? Việc gộp làm mất thông tin gì?
6. Viết thêm phần in **bảng tần số kỳ vọng** $e_{ij}$ cho thí dụ 4.4, và cột đóng góp
   $(n_{ij}-e_{ij})^2/e_{ij}$ của từng ô. Ô nào đóng góp nhiều nhất vào $K = 1073{,}5$?
7. Với dữ liệu doanh thu, chạy **ANOVA theo thứ trong tuần** (7 nhóm) thay vì chỉ 2 nhóm.
   Cần thêm cột thứ vào CSV. $F$ bằng bao nhiêu? Kết luận?

---

## 11. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)          | Tiếng Anh                    | Ghi chú                   |
| -------------------------------- | ---------------------------- | ------------------------- |
| So sánh hai kỳ vọng              | Two-sample t-test            | (3.5)                     |
| Phương sai gộp                   | Pooled variance              | $s_p^2$                   |
| Mẫu cặp                          | Paired samples               | lấy hiệu → một mẫu        |
| Mẫu độc lập                      | Independent samples          |                           |
| So sánh hai tỷ lệ                | Two-proportion z-test        | (3.9)                     |
| Tần suất gộp                     | Pooled proportion            | $f = (m_1+m_2)/(n_1+n_2)$ |
| So sánh hai phương sai           | F-test for variances         | (3.12)                    |
| Phân tích phương sai             | Analysis of variance (ANOVA) | (3.18)                    |
| Phân tích phương sai một nhân tố | One-way ANOVA                |                           |
| Tổng bình phương giữa nhóm       | Between-group sum of squares | tín hiệu                  |
| Tổng bình phương trong nhóm      | Within-group sum of squares  | nhiễu                     |
| Đồng nhất phương sai             | Homogeneity of variance      | điều kiện của ANOVA       |
| Kiểm định phi tham số            | Non-parametric test          | §4                        |
| Tiêu chuẩn phù hợp               | Goodness-of-fit test         | (4.1)                     |
| Tiêu chuẩn Pearson              | Pearson's chi-squared test   |                           |
| Bảng liên hợp                    | Contingency table            | bảng chéo                 |
| Kiểm định độc lập                | Test of independence         | (4.4)                     |
| Tần số kỳ vọng                   | Expected frequency           | $e_{ij} = n_i m_j / n$    |
| So sánh hậu nghiệm               | Post-hoc comparison          | 📚 mục 8                  |
| Hiệu chỉnh Bonferroni            | Bonferroni correction        | $\alpha/k$                |
| Kiểm định Welch                  | Welch's t-test               | khi phương sai khác nhau  |

---

## 12. Câu hỏi tự kiểm tra

1. Vì sao mẫu số của (3.1) là $\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}$ — **cộng** chứ không trừ,
   dù đang tính hiệu hai trung bình?
2. Điều kiện bắt buộc của công thức (3.5) là gì? Làm sao kiểm điều kiện đó?
   Nếu vi phạm thì phải làm gì?
3. Phân biệt **mẫu độc lập** và **mẫu cặp**. Cho hai ví dụ kinh doanh cho mỗi loại.
   Vì sao mẫu cặp mạnh hơn?
4. Vì sao kiểm định hai tỷ lệ dùng **tần suất gộp** $f$ ở mẫu số, trong khi khoảng tin cậy cho
   hiệu hai tỷ lệ dùng $f_1$, $f_2$ riêng?
5. Vì sao không nên so sánh $k = 5$ nhóm bằng cách chạy 10 kiểm định $t$ từng cặp?
   Tính xác suất có ít nhất một kết luận sai.
6. Viết đẳng thức tách tổng bình phương của ANOVA và giải thích ý nghĩa từng thành phần.
   Vì sao ANOVA luôn là kiểm định một phía phải?
7. Ba điều kiện của ANOVA là gì? Điều kiện nào hay bị vi phạm nhất?
8. Trong kiểm định phù hợp, vì sao phải trừ $r$ bậc tự do? Nếu kiểm định "dữ liệu có phân phối chuẩn"
   với 8 lớp thì bậc tự do bằng bao nhiêu?
9. Công thức tần số kỳ vọng $e_{ij}$ trong kiểm định độc lập là gì? Giải thích vì sao nó chính là
   "nếu độc lập thì ô này phải có bao nhiêu".
10. Hai chi nhánh: A có 200 khách, 24 khiếu nại; B có 150 khách, 12 khiếu nại.
    a) Đặt $H_0$, $H_1$. b) Tính $K_{tn}$. c) Kết luận ở $\alpha = 0{,}05$.
    d) Tính khoảng tin cậy 95% cho hiệu hai tỷ lệ.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 13 — NHIỀU MẪU, ANOVA, PHI THAM SỐ         (Ch. V §3–4, tr.170–193) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ① HAI KỲ VỌNG                                                          ║
║      biết σ / n lớn:  K = (X̄−Ȳ)/√(σ₁²/n₁ + σ₂²/n₂)      ~ N(0;1)         ║
║                        ⚠ CỘNG hai phương sai, không trừ                  ║
║      n nhỏ, CÙNG σ²:  K = (X̄−Ȳ)/√(s_p²(1/n₁+1/n₂))     ~ t(n₁+n₂−2)      ║
║                        s_p² = ((n₁−1)s₁²+(n₂−1)s₂²)/(n₁+n₂−2)            ║
║      ⚠⚠ PHẢI KIỂM CÙNG PHƯƠNG SAI TRƯỚC bằng ③                          ║
║      ⭐ MẪU CẶP (cùng đối tượng, đo 2 lần): lấy HIỆU → về bài 12         ║
║                                                                          ║
║  ② HAI TỶ LỆ    K = (f₁−f₂)/√(f(1−f)(1/n₁+1/n₂))       ~ N(0;1)         ║
║      f = (m₁+m₂)/(n₁+n₂) — TẦN SUẤT GỘP (vì H₀ nói p₁ = p₂)              ║
║      = A/B TEST hai nhóm                                                 ║
║                                                                          ║
║  ③ HAI PHƯƠNG SAI   K = s₁²/s₂²   ~ F(n₁−1; n₂−1)                       ║
║      💡 mẹo: đặt phương sai LỚN ở tử → K > 1, chỉ tra một bên            ║
║      💼 độ ỔN ĐỊNH thường quan trọng hơn giá trị TRUNG BÌNH              ║
║                                                                          ║
║  ④ k KỲ VỌNG — ANOVA MỘT NHÂN TỐ                                        ║
║      ⚠ KHÔNG so từng cặp: k=5 → 10 cặp → 40% khả năng kết luận sai       ║
║                                                                          ║
║      ⭐ TÁCH TỔNG BÌNH PHƯƠNG                                            ║
║          TOÀN BỘ     =    GIỮA nhóm    +   TRONG nhóm                    ║
║         ΣΣ(xᵢⱼ−X̄)²   =    Σnⱼ(X̄ⱼ−X̄)²   +  ΣΣ(xᵢⱼ−X̄ⱼ)²                    ║
║        (tín hiệu+nhiễu)   (tín hiệu)        (nhiễu)                      ║
║          n−1        =      k−1         +      n−k     (bậc tự do)        ║
║                                                                          ║
║      K = s₁²/s₂² = [SS_giữa/(k−1)] / [SS_trong/(n−k)]  ~ F(k−1; n−k)     ║
║      LUÔN một phía PHẢI                                                  ║
║      ⚠ 3 điều kiện: độc lập | chuẩn | ĐỒNG NHẤT PHƯƠNG SAI               ║
║                                                                          ║
║  ── PHI THAM SỐ: cả hai dùng χ², cả hai MỘT PHÍA PHẢI ───────────        ║
║                                                                          ║
║  ⑤ PHÙ HỢP   K = Σ (quan sát − kỳ vọng)²/kỳ vọng   ~ χ²(k−r−1)          ║
║      r = SỐ THAM SỐ phải ước lượng   (đều: r=0 | Poisson: 1 | chuẩn: 2)  ║
║      ⚠ mỗi lớp cần nᵢ ≥ 5, không đủ thì GỘP lớp                          ║
║                                                                          ║
║  ⑥ ĐỘC LẬP   K = Σᵢ Σⱼ (nᵢⱼ − eᵢⱼ)²/eᵢⱼ    ~ χ²((r−1)(s−1))             ║
║      ⭐ eᵢⱼ = (tổng hàng i × tổng cột j) / n                             ║
║      = kiểm chứng BẢNG CHÉO của bài 8                                    ║
║      ⭐ bác bỏ độc lập ⟹ PHÂN KHÚC CÓ GIÁ TRỊ                           ║
║                                                                          ║
║  📚 SAU ANOVA: so sánh HẬU NGHIỆM để biết nhóm nào khác nhóm nào         ║
║      Bonferroni: chạy mọi cặp ở mức α/C(k,2)                             ║
║                                                                          ║
║  ⚠ GHI CHÚ SỐ LIỆU                                                       ║
║      tr.174 thí dụ 3.3: cách không gộp cho −2,24 (sách in −2,56)         ║
║      tr.175 thí dụ 3.4: đề ghi s₁²=2500, phần giải dùng 2550             ║
║      tr.178 thí dụ 3.5: bảng in X̄₁=8,7425, phép tính dùng 8,7125 (đúng)  ║
║                                                                          ║
║  💼 QTKD  ⚠ VẼ ĐỒ THỊ TRƯỚC KHI KIỂM ĐỊNH                                ║
║          A/B test = ②  |  so nhà cung cấp = ③  |  so chi nhánh = ④     ║
║          bảng chéo có ý nghĩa không = ⑥                                 ║
║          báo cáo: p + ĐỘ LỚN + KHOẢNG TIN CẬY, không chỉ có/không        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương V §3–§4, tr. 170–193.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Ghi chú số liệu: thí dụ 3.3 (tr. 174) — cách không gộp phương sai tính lại được $-2{,}239$,
  sách in $-2{,}56$; thí dụ 3.4 (tr. 175) — đề bài ghi $s_1^2 = 2500$ nhưng phần giải dùng 2550;
  thí dụ 3.5 (tr. 178) — bảng in $\overline{X}_1 = 8{,}7425$ nhưng phép tính dùng 8,7125
  (giá trị 8,7125 đúng, tính lại từ dữ liệu thô). Kết luận của cả ba thí dụ **không thay đổi**.
- Dữ liệu: `haemoglobin.csv` (thí dụ 3.5) và `mat_toc.csv` (thí dụ 4.4) là số liệu nguyên văn
  của giáo trình.
- Mục 7 (cây quyết định) và mục 8 (so sánh hậu nghiệm): kiến thức bổ sung.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 12 — Kiểm định giả thuyết, một mẫu](bai_12_kiem_dinh_gia_thuyet_mot_mau.md) ·
Bài sau: Bài 14 — Tương quan và phân tích hồi quy
