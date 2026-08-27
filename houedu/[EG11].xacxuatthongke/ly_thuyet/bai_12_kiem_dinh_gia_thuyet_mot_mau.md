# Bài 12 — Kiểm định giả thuyết, các bài toán một mẫu

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương V §1–§2**, tr. 158–170.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính một lỗi làm ĐẢO NGƯỢC kết luận** của thí dụ 2.3 (tr. 166).
> 📌 **Cần đọc trước:** [Bài 10](bai_10_mau_va_thong_ke_mo_ta.md) · [Bài 11](bai_11_uoc_luong_diem_va_khoang_tin_cay.md)

Bài 11 trả lời câu *"giá trị thật khoảng bao nhiêu?"*. Bài này trả lời câu **quyết định**:
*"lời tuyên bố kia có đúng không?"*

Giáo trình mở đầu (tr. 158):

> "Trong nhiều lĩnh vực đời sống kinh tế – xã hội chúng ta hay nêu ra các **nhận xét** khác nhau về
> các đối tượng quan tâm... Vấn đề xác định **đúng sai** của một giả thuyết sẽ được gọi là **kiểm định**."

💼 Đây là công cụ thống kê **được dùng nhiều nhất trong kinh doanh**: A/B test, kiểm tra chất lượng,
đánh giá chiến dịch, nghiệm thu nhà cung cấp — tất cả đều là kiểm định giả thuyết.

## Mục lục

1. [Giả thuyết gốc và đối thuyết](#1-giả-thuyết-gốc-và-đối-thuyết)
2. [Nguyên lý xác suất nhỏ và miền tới hạn](#2-nguyên-lý-xác-suất-nhỏ-và-miền-tới-hạn)
3. [Hai loại sai lầm](#3-hai-loại-sai-lầm)
4. [Ba dạng miền tới hạn](#4-ba-dạng-miền-tới-hạn)
5. [Bài toán 1 và 2: kiểm định về kỳ vọng](#5-bài-toán-1-và-2-kiểm-định-về-kỳ-vọng)
6. [Bài toán 3: kiểm định về tỷ lệ](#6-bài-toán-3-kiểm-định-về-tỷ-lệ)
7. [Bài toán 4: kiểm định về phương sai](#7-bài-toán-4-kiểm-định-về-phương-sai)
8. [📚 Giá trị p](#8--giá-trị-p)
9. [📚 Bảy điều kiểm định không nói cho bạn](#9--bảy-điều-kiểm-định-không-nói-cho-bạn)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Giả thuyết gốc và đối thuyết

**Giả thuyết thống kê** là một nhận xét về yếu tố chưa biết của tổng thể (tr. 158):
dạng phân phối, giá trị tham số...

| Loại                | Định nghĩa                                      | Ví dụ                |
| ------------------- | ----------------------------------------------- | -------------------- |
| **Giả thuyết đơn**  | $\theta$ bằng **một** giá trị cụ thể $\theta_0$ | $a = 50$             |
| **Giả thuyết phức** | mọi trường hợp khác                             | $a > 50$, $a \ne 50$ |

Giáo trình lưu ý: *"Việc kiểm định một giả thuyết đơn thường **dễ dàng hơn**."*

**Hai giả thuyết luôn đi cặp (tr. 158):**

| Ký hiệu | Tên                             | Đặc điểm                     |
| ------- | ------------------------------- | ---------------------------- |
| $H_0$   | **giả thuyết gốc**              | thường là giả thuyết **đơn** |
| $H_1$   | **giả thuyết đối** (đối thuyết) | đơn hoặc phức                |

> "Ta thừa nhận khi đã chọn cặp $H_0$, $H_1$ thì việc **chấp nhận $H_0$ chính là bác bỏ $H_1$** và
> ngược lại."

**Ví dụ của giáo trình** (nghiên cứu thu nhập cư dân một thành phố, tr. 158–159):

- $H_0$: thu nhập tuân theo luật chuẩn / $H_1$: không tuân theo.
- $H_0$: thu nhập trung bình năm là 50 triệu, với nhiều đối thuyết:
  $\ne 50$, $> 50$, hoặc $< 50$ triệu.

### 💼 Góc QTKD — chọn $H_0$ thế nào

⭐ **Quy tắc vàng: $H_0$ là điều bạn muốn BÁC BỎ, $H_1$ là điều bạn muốn CHỨNG MINH.**

Vì kiểm định chỉ có thể **bác bỏ** $H_0$ một cách mạnh mẽ; nó **không bao giờ chứng minh được** $H_0$
đúng (mục 9 sẽ giải thích).

| Bạn muốn chứng minh                   | $H_0$                            | $H_1$                            |
| ------------------------------------- | -------------------------------- | -------------------------------- |
| Trang mới chuyển đổi tốt hơn trang cũ | $p_{\text{mới}} = p_{\text{cũ}}$ | $p_{\text{mới}} > p_{\text{cũ}}$ |
| Quy trình mới giảm tỷ lệ lỗi          | $p = p_0$                        | $p < p_0$                        |
| Nhà cung cấp KHÔNG đạt cam kết        | $p = 2\%$ (cam kết)              | $p > 2\%$                        |
| Doanh thu vượt chỉ tiêu               | $a = 50$                         | $a > 50$                         |

⚠️ Chú ý dòng thứ ba: $H_0$ là **lời cam kết của nhà cung cấp**. Nếu dữ liệu không đủ mạnh để bác bỏ,
bạn phải **chấp nhận hàng** — gánh nặng chứng minh nằm ở phía bạn. Điều này giống hệt nguyên tắc
"suy đoán vô tội" trong pháp luật: $H_0$ = vô tội.

---

## 2. Nguyên lý xác suất nhỏ và miền tới hạn

**Nguyên tắc chung (tr. 159):**

> "Dựa trên **nguyên lý xác suất nhỏ**: một sự kiện có xác suất xuất hiện khá bé thì có thể coi rằng
> **nó không xảy ra** khi thực hiện một phép thử có liên quan đến sự kiện đó."

Nói cách khác: nếu $H_0$ đúng mà dữ liệu quan sát được lại **cực kỳ khó xảy ra**, thì có lẽ $H_0$ sai.

### Tiêu chuẩn kiểm định

Chọn một thống kê (1.1):

$$K = K(x_1, x_2, \dots, x_n)$$

⭐ **Điều kiện then chốt (tr. 159):** *"Nếu giả thuyết $H_0$ **đúng** thì luật phân phối của $K$ phải
**hoàn toàn xác định**."*

So với bài 11 mục 4: cùng một yêu cầu, cùng một bộ bốn thống kê. **Kiểm định và khoảng tin cậy là
hai mặt của một đồng xu** — mục 5 sẽ nói rõ.

### Quy tắc kiểm định

Chia miền xác định của $K$ thành hai phần:

| Miền                           | Ký hiệu               | Nghĩa                                 |
| ------------------------------ | --------------------- | ------------------------------------- |
| **Miền tới hạn** (miền bác bỏ) | $B_\alpha$            | $K$ rơi vào đây → **bác bỏ $H_0$**    |
| Miền chấp nhận                 | $\overline{B_\alpha}$ | $K$ rơi vào đây → **chấp nhận $H_0$** |

```
        phân phối của K KHI H₀ ĐÚNG
                    ╱▔▔╲
                  ╱      ╲
        ▒▒▒▒▒▒  ╱          ╲  ▒▒▒▒▒▒
      ──┴────┴─────────────────┴────┴──►  K
        │ Bα │  miền chấp nhận │ Bα │
        │    │                 │    │
    diện tích hai phần gạch cộng lại = α

    K rơi vào vùng gạch = "chuyện quá khó xảy ra nếu H₀ đúng"  →  bác bỏ H₀
```

---

## 3. Hai loại sai lầm

Giáo trình định nghĩa (tr. 160):

|                    | Định nghĩa                           | Xác suất | Công thức                                                              |
| ------------------ | ------------------------------------ | -------- | ---------------------------------------------------------------------- |
| **Sai lầm loại 1** | **bác bỏ** một giả thuyết **đúng**   | $\alpha$ | $\alpha = P(K_{tn} \in B_\alpha \mid H_0 \text{ đúng})$ (1.2)          |
| **Sai lầm loại 2** | **chấp nhận** một giả thuyết **sai** | $\beta$  | $\beta = P(K_{tn} \in \overline{B_\alpha} \mid H_0 \text{ sai})$ (1.3) |

$1 - \beta$ gọi là **lực lượng** của tiêu chuẩn $K$ — *"xác suất bác bỏ giả thuyết sai"*.

**Bảng bốn ô** — dạng dễ nhớ nhất:

|                     | $H_0$ **thật sự đúng**           | $H_0$ **thật sự sai**           |
| ------------------- | -------------------------------- | ------------------------------- |
| **Chấp nhận $H_0$** | ✅ đúng                          | ❌ **sai lầm loại 2** ($\beta$) |
| **Bác bỏ $H_0$**    | ❌ **sai lầm loại 1** ($\alpha$) | ✅ đúng (lực lượng $1-\beta$)   |

### ⭐ Đánh đổi không tránh được

Giáo trình nói thẳng (tr. 160):

> "Trong thực tế ta **không thể đồng thời làm giảm cả hai** xác suất đó, bởi vì cứ $\alpha$ giảm thì
> $\beta$ tăng và ngược lại."

**Vì sao chọn $\alpha$ mà không chọn $\beta$?** Giáo trình giải thích: *"do sai lầm loại 1 **dễ kiểm
soát** và (1.2) **dễ tính hơn**"*. Tính $\alpha$ chỉ cần biết phân phối của $K$ khi $H_0$ đúng —
mà đó là điều kiện đã đặt ra. Còn tính $\beta$ cần biết $H_1$ **cụ thể** là gì (giá trị thật bằng bao nhiêu),
mà thường ta không biết.

$\alpha$ gọi là **mức ý nghĩa**. Các giá trị thường dùng: **0,1; 0,05; 0,01; 0,001**.

### Thí dụ 1.2 (tr. 161)

> $X \sim N(\theta; 25)$, $n = 9$. $H_0: \theta = 3$ với $H_1: \theta = 4$. Ngưỡng $A_0 = 5{,}5$.
> Tìm $\alpha$ và $\beta$.

*Giải.* $\sigma/\sqrt{n} = 5/3$.

$$\alpha = P(\overline{X} > 5{,}5 \mid H_0) = P\!\left(Z > \frac{5{,}5-3}{5/3}\right)
= P(Z > 1{,}5) = 0{,}5 - 0{,}4332 = \mathbf{0{,}0668}$$

$$\beta = P(\overline{X} < 5{,}5 \mid H_1) = P\!\left(Z < \frac{5{,}5-4}{5/3}\right)
= P(Z < 0{,}9) = 0{,}5 + 0{,}3159 = \mathbf{0{,}8159}$$

Giáo trình nhận xét gọn: *"$\beta$... **khá lớn**"*. Lực lượng chỉ $1 - 0{,}8159 = 0{,}18$ —
kiểm định này gần như không có khả năng phát hiện ra $H_0$ sai.

**Đổi ngưỡng để thấy sự đánh đổi** (tính ở mục 10):

| Ngưỡng $A_0$ |   $\alpha$ |    $\beta$ | Lực lượng |
| -----------: | ---------: | ---------: | --------: |
|          3,5 |     0,3821 |     0,3821 |     0,618 |
|          4,5 |     0,1841 |     0,6179 |     0,382 |
|      **5,5** | **0,0668** | **0,8159** | **0,184** |
|          6,0 |     0,0359 |     0,8849 |     0,115 |

Cột $\alpha$ giảm thì cột $\beta$ tăng — **luôn luôn**, không có ngoại lệ.

**Cách duy nhất giảm cả hai: TĂNG CỠ MẪU.** Đây là kết luận thực tiễn quan trọng nhất của mục này,
và giáo trình không nêu rõ.

### 💼 Góc QTKD — hai loại sai lầm tốn tiền khác nhau

| Bối cảnh           | Sai lầm loại 1 (báo động giả)    | Sai lầm loại 2 (bỏ lọt)       |
| ------------------ | -------------------------------- | ----------------------------- |
| Nghiệm thu lô hàng | trả lại lô hàng **tốt**          | nhận lô hàng **lỗi**          |
| A/B test           | triển khai tính năng **vô dụng** | bỏ qua tính năng **tốt**      |
| Kiểm tra gian lận  | chặn giao dịch **hợp lệ**        | để lọt giao dịch **gian lận** |
| Tuyển dụng         | loại ứng viên **giỏi**           | tuyển người **không phù hợp** |

⭐ **Chọn $\alpha$ theo cái giá của sai lầm loại 1**, không theo thói quen:

- Sai lầm loại 1 rất đắt (thu hồi sản phẩm, huỷ hợp đồng) → $\alpha$ nhỏ: 0,01 hoặc 0,001.
- Sai lầm loại 2 đắt hơn (bỏ lỡ cơ hội lớn) → $\alpha$ rộng tay: 0,10.

⚠️ Con số 0,05 chỉ là **thói quen lịch sử** (do Fisher đề xuất năm 1925), **không** phải quy luật tự
nhiên. Rất nhiều quyết định kinh doanh tồi bắt nguồn từ việc dùng 0,05 một cách máy móc.

---

## 4. Ba dạng miền tới hạn

Chọn dạng miền tới hạn theo **dạng của $H_1$** (tr. 162–163):

| $H_1$                 | Dạng              | Miền tới hạn $B_\alpha$                                  | Hình      |
| --------------------- | ----------------- | -------------------------------------------------------- | --------- |
| $\theta \ne \theta_0$ | **hai phía**      | $(-\infty; K_{\alpha/2}) \cup (K_{1-\alpha/2}; +\infty)$ | hai đuôi  |
| $\theta < \theta_0$   | **một phía trái** | $(-\infty; K_\alpha)$                                    | đuôi trái |
| $\theta > \theta_0$   | **một phía phải** | $(K_{1-\alpha}; +\infty)$                                | đuôi phải |

```
   HAI PHÍA (H₁: θ ≠ θ₀)        TRÁI (H₁: θ < θ₀)      PHẢI (H₁: θ > θ₀)
        ╱▔▔╲                        ╱▔▔╲                    ╱▔▔╲
   ▒▒ ╱      ╲ ▒▒               ▒▒▒╱     ╲                ╱     ╲▒▒▒
   ──┴────────┴──               ──┴───────────           ───────────┴──
   α/2        α/2                  α                              α
```

⚠️ **Chỗ sai nhiều nhất:** cùng mức $\alpha$, kiểm định **một phía** dùng phân vị $z_{1-\alpha}$
(nhỏ hơn), kiểm định **hai phía** dùng $z_{1-\alpha/2}$ (lớn hơn).

Với $\alpha = 0{,}05$: một phía dùng **1,645**, hai phía dùng **1,960**.

⭐ **Kiểm định một phía DỄ bác bỏ $H_0$ hơn.** Đó là lý do phải chọn $H_1$ **trước khi nhìn dữ liệu** —
nếu nhìn dữ liệu rồi mới chọn chiều, bạn đã gian lận (mục 9).

**Cách chọn từ đề bài:**

| Đề nói                                            | $H_1$            |
| ------------------------------------------------- | ---------------- |
| "có đúng bằng... không", "kiểm tra lại thông báo" | $\ne$ (hai phía) |
| "có lớn hơn... không", "có vượt... không"         | $>$ (phải)       |
| "có nhỏ hơn... không", "nghi ngờ nói quá lên"     | $<$ (trái)       |

---

## 5. Bài toán 1 và 2: kiểm định về kỳ vọng

$H_0: a = a_0$ với mức ý nghĩa $\alpha$.

### Bài toán 1 — phương sai $\sigma_0^2$ ĐÃ BIẾT

**Tiêu chuẩn (2.1):**

$$K = \frac{\overline{X} - a_0}{\sigma_0}\sqrt{n} \ \sim N(0;1) \text{ khi } H_0 \text{ đúng}$$

**Miền tới hạn:**

| $H_1$       | Điều kiện bác bỏ          | Phân vị                         |
| ----------- | ------------------------- | ------------------------------- |
| $a \ne a_0$ | $\vert K_{tn}\vert > z_b$ | $z_b = z_{1-\alpha/2}$ (2.2)    |
| $a < a_0$   | $K_{tn} < z_b$            | $z_b = z_\alpha$ **(âm)** (2.3) |
| $a > a_0$   | $K_{tn} > z_b$            | $z_b = z_{1-\alpha}$ (2.4)      |

### ⭐ Kiểm định và khoảng tin cậy là một

Giáo trình nêu một nhận xét cực kỳ quan trọng (tr. 164):

> "Để ý rằng **miền chấp nhận $H_0$** (tính đối với thống kê $K$) chính là **khoảng tin cậy** với độ
> tin cậy $1-\alpha$ cho kỳ vọng."

$$\boxed{\text{Bác bỏ } H_0: a = a_0 \text{ ở mức } \alpha
\iff a_0 \text{ NẰM NGOÀI khoảng tin cậy } 1-\alpha}$$

💼 **Hệ quả rất tiện:** nếu đã tính khoảng tin cậy ở bài 11, bạn **không cần tính lại gì** để kiểm định.
Chỉ cần nhìn xem giá trị giả thuyết có nằm trong khoảng không.

Ví dụ: doanh thu 60 ngày cho khoảng 95% là $(50{,}95;\ 59{,}53)$. Vậy:
- $H_0: a = 50$ → 50 nằm **ngoài** → **bác bỏ**.
- $H_0: a = 55$ → 55 nằm **trong** → chưa có cơ sở bác bỏ.

### Thí dụ 2.1 (tr. 164)

> Hãng bảo hiểm thông báo tiền chi trả trung bình là 8.500 đô. Kiểm 25 hồ sơ thấy trung bình 8.900 đô.
> Biết $\sigma = 2600$. Kiểm định với $\alpha = 0{,}05$.

$H_0: a = 8500$, $H_1: a \ne 8500$ (hai phía — *"kiểm tra lại thông báo"*).

$$K_{tn} = \frac{8900 - 8500}{2600}\sqrt{25} = \frac{400}{2600} \times 5 = \mathbf{0{,}77}$$

$z_b = 1{,}96$. Vì $|0{,}77| < 1{,}96$ → **không có cơ sở bác bỏ** thông báo của hãng.

### Thí dụ 2.2 (tr. 165)

> Chủ cửa hàng cho rằng dung tích trung bình thùng là 55 lít ($\sigma = 6$). **Không thể đóng thùng
> lớn hơn** do kích thước tôn đã cố định. Kiểm 36 thùng thấy trung bình 49 lít. $\alpha = 0{,}001$.

$H_0: a = 55$, $H_1: a < 55$ — **một phía trái**, vì đề nói không thể lớn hơn.

$$K_{tn} = \frac{49 - 55}{6}\sqrt{36} = -1 \times 6 = \mathbf{-6}$$

$z_b = z_{0{,}001} = -3{,}09$. Vì $-6 < -3{,}09$ → **bác bỏ**: ý kiến của ông chủ **không đúng**.

⚠️ Giáo trình lưu ý (tr. 165): thống kê (2.1) *"sẽ có phân phối xấp xỉ chuẩn, **ngay cả trong trường
hợp chưa biết phân phối của biến gốc**"* khi $n$ lớn — nhờ CLT (bài 9).

### Bài toán 2 — phương sai CHƯA BIẾT

**Tiêu chuẩn (2.5):**

$$K = \frac{\overline{X} - a_0}{s}\sqrt{n} \ \sim t(n-1) \text{ khi } H_0 \text{ đúng}$$

Giáo trình chỉ ra: cách làm *"rất giống với bài toán 1"*, chỉ thay $\sigma_0 \to s$ và
bảng Laplace → bảng Student (2.6)–(2.8).

Và lưu ý (tr. 166): khi $n > 30$ thì tra bảng Laplace được, thậm chí *"có thể bỏ qua cả giả thiết
chuẩn của biến gốc $X$"* — nhưng kết quả chỉ là **gần đúng**.

### Thí dụ 2.3 (tr. 166) — ⚠️ SÁCH TÍNH SAI, ĐẢO NGƯỢC KẾT LUẬN

> Nhà nhân chủng học cho rằng chiều cao trung bình một bộ tộc là 160 cm. Chọn 16 người thấy chiều cao
> trung bình 164,25 cm với $s = 6{,}25$ cm. **Có thể cho rằng bộ tộc đó cao hơn 160 cm không?**
> ($\alpha = 0{,}05$)

$H_0: a = 160$, $H_1: a > 160$ — một phía phải.

$$K_{tn} = \frac{\overline{X} - a_0}{s}\sqrt{n} = \frac{164{,}25 - 160}{6{,}25}\sqrt{16}
= \frac{4{,}25}{6{,}25} \times 4 = 0{,}68 \times 4 = \mathbf{2{,}72}$$

$t_{15;\,0{,}95} = 1{,}753$. Vì $2{,}72 > 1{,}753$:

$$\boxed{\text{BÁC BỎ } H_0 \ \Longrightarrow \ \text{bộ tộc đó THẬT SỰ cao hơn 160 cm}}$$

### ⚠️ Đính chính — lỗi nghiêm trọng nhất của cả giáo trình

Bản quét gốc trang 166 in nguyên văn:

$$K_{tn} = \frac{\overline{X} - a_0}{s}\sqrt{n} = \frac{164{,}25 - 160}{6{,}25}\sqrt{16} \approx 1{,}36$$

> "Do $1{,}36 < 1{,}753$, ta **không có cơ sở để bác bỏ** $H_0$, có nghĩa là ý kiến của nhà nhân
> chủng học là có thể tin được."

**Sai ở đâu:** $\dfrac{4{,}25}{6{,}25} = 0{,}68$, nhân với $\sqrt{16} = \mathbf{4}$ được $\mathbf{2{,}72}$.
Sách nhân với **2** — tức là dùng $\sqrt{16} = 2$ (căn bậc bốn thay vì căn bậc hai).

**Hậu quả:** $2{,}72 > 1{,}753$ nên phải **BÁC BỎ** $H_0$. Kết luận đúng **ngược hoàn toàn** với sách.

⭐ **Đây là lỗi khác về bản chất so với sáu lỗi in đã gặp ở các bài trước** — chúng chỉ sai con số,
lỗi này **sai câu trả lời của bài toán**.

**Bài học tự bảo vệ:** khi làm bài, hãy ước lượng nhanh trong đầu trước khi tin máy tính hay sách:
$\overline{X}$ lệch $4{,}25$ cm so với $a_0$, mà $s/\sqrt{n} = 6{,}25/4 = 1{,}56$ — tức lệch tới
gần **3 lần sai số chuẩn**. Với $\alpha = 0{,}05$ thì gần như chắc chắn phải bác bỏ.

---

## 6. Bài toán 3: kiểm định về tỷ lệ

$H_0: p = p_0$, với $X \sim B(p)$.

**Điều kiện (tr. 167):** $n$ lớn và $p$ không quá gần 0 hoặc 1, cụ thể $np > 5$ hoặc $n(1-p) > 5$.

**Tiêu chuẩn (2.9):**

$$K = \frac{f - p_0}{\sqrt{p_0(1-p_0)}}\sqrt{n} \ \approx N(0;1)$$

⚠️ **Chú ý mẫu số dùng $p_0$**, không dùng $f$. Khác với **khoảng tin cậy** ở bài 11 mục 7 (dùng $f$).
Lý do: khi kiểm định, ta **giả sử $H_0$ đúng**, nên phương sai phải tính theo $p_0$.
Đây là chỗ khác biệt tinh tế giữa hai bài toán.

Miền tới hạn giống hoàn toàn bài toán 1 (thay $z$ tương ứng).

### Thí dụ 2.4 (tr. 167)

> Toà báo thông báo 25% học sinh THPT là độc giả thường xuyên. Mẫu 200 học sinh có 45 em đọc thường
> xuyên. Kiểm định với $\alpha = 0{,}05$.

$H_0: p = 0{,}25$, $H_1: p \ne 0{,}25$. $f = 45/200 = 0{,}225$:

$$K_{tn} = \frac{0{,}225 - 0{,}25}{\sqrt{0{,}25 \times 0{,}75}}\sqrt{200} = \mathbf{-0{,}82}$$

$|-0{,}82| < 1{,}96$ → **không có cơ sở bác bỏ** thông báo của toà báo.

### Thí dụ 2.5 (tr. 167)

> Hiệu làm đầu cho rằng 90% khách hài lòng. **Nghi ngờ chủ hiệu nói quá lên**, điều tra 150 khách
> thấy 132 người hài lòng. $\alpha = 0{,}05$.

*"Nghi ngờ nói quá lên"* → $H_1: p < 0{,}9$ — một phía trái. $f = 132/150 = 0{,}88$:

$$K_{tn} = \frac{0{,}88 - 0{,}9}{\sqrt{0{,}9 \times 0{,}1}}\sqrt{150} = \mathbf{-0{,}82}$$

$z_b = -1{,}645$. Vì $-0{,}82 > -1{,}645$ → **không có cơ sở bác bỏ** ý kiến của hiệu làm đầu.

⚠️ **Ghi chú nhỏ về số:** giáo trình in $-0{,}806$ (thí dụ 2.4) và $-0{,}833$ (thí dụ 2.5).
Tính chính xác, **cả hai đều bằng $-0{,}8165$** (trùng hợp thú vị). Chênh lệch do sách làm tròn ở
bước trung gian; **kết luận không đổi**.

### 💼 Góc QTKD — đây chính là A/B test một mẫu

Tỷ lệ chuyển đổi hiện tại là 3% ($p_0$). Sau khi đổi giao diện, trong 1.000 lượt truy cập có 38 đơn.
Đổi giao diện có hiệu quả không?

$$f = 0{,}038, \qquad K = \frac{0{,}038 - 0{,}03}{\sqrt{0{,}03 \times 0{,}97}}\sqrt{1000} = 1{,}48$$

$1{,}48 < 1{,}645$ → **chưa đủ bằng chứng**. Cần thêm dữ liệu.

⭐ **Cỡ mẫu bao nhiêu là đủ?** Đây là câu hỏi phải trả lời **trước khi** chạy test, bằng công thức
cỡ mẫu ở bài 11 mục 5. Chạy test rồi mới hỏi thì đã muộn.

⚠️ Và **đừng dừng test khi vừa thấy kết quả đẹp** — đó là lỗi "peeking", làm $\alpha$ thật cao hơn
nhiều so với 0,05 (mục 9).

---

## 7. Bài toán 4: kiểm định về phương sai

$H_0: VX = \sigma_0^2$, với giả thiết $X$ chuẩn.

**Tiêu chuẩn (2.10):**

$$K = \frac{(n-1)s^2}{\sigma_0^2} \ \sim \chi^2(n-1) \text{ khi } H_0 \text{ đúng}$$

⚠️ Giáo trình lưu ý (tr. 168): nếu **biết** $a_0 = EX$ và thay $(n-1)s^2$ bằng $\sum(x_i - a_0)^2$
thì thống kê tuân theo $\chi^2(n)$ — **đủ $n$ bậc tự do** (giống bài 11 mục 8).

**Miền tới hạn:**

| $H_1$                     | Bác bỏ khi                                                             | Công thức |
| ------------------------- | ---------------------------------------------------------------------- | --------- |
| $\sigma^2 \ne \sigma_0^2$ | $K < \chi^2_{n-1;\,\alpha/2}$ **hoặc** $K > \chi^2_{n-1;\,1-\alpha/2}$ | (2.11)    |
| $\sigma^2 < \sigma_0^2$   | $K < \chi^2_{n-1;\,\alpha}$                                            | (2.12a)   |
| $\sigma^2 > \sigma_0^2$   | $K > \chi^2_{n-1;\,1-\alpha}$                                          | (2.12b)   |

### Thí dụ 2.6 (tr. 169)

> Chủ hãng cho biết độ lệch chuẩn của sai số đo là 5 mm. Kiểm 19 thiết bị thấy $s^2 = 33$ mm².
> $\alpha = 0{,}05$.

$H_0: \sigma^2 = 25$:

$$K_{tn} = \frac{18 \times 33}{25} = \mathbf{23{,}76}$$

**a) $H_1: \sigma^2 \ne 25$** — hai phía: $\chi^2_{18;\,0{,}025} = 8{,}23$, $\chi^2_{18;\,0{,}975} = 31{,}53$.
Vì $8{,}23 < 23{,}76 < 31{,}53$ → **chấp nhận**.

**b) $H_1: \sigma^2 > 25$** — một phía: $\chi^2_{18;\,0{,}95} = 28{,}87$.
Vì $23{,}76 < 28{,}87$ → **chấp nhận**.

Cả hai trường hợp ý kiến của chủ hãng đều được chấp nhận.

### Thí dụ 2.7 (tr. 169) — mẹo khi $n$ lớn

> Thử độ chịu lực 35 chốt khoá thấy $s = 3{,}5$ pao. Người sản xuất bảo đảm $\sigma = 3$ pao.

$n = 35 > 30$ nên dùng sự kiện $s \approx N\!\left(\sigma;\ \dfrac{\sigma^2}{2n}\right)$ (bài 10 mục 7),
đưa về kiểm định chuẩn (2.4):

$$K_{tn} = \frac{s - \sigma_0}{\sigma_0/\sqrt{2n}} = \frac{3{,}5 - 3}{3/\sqrt{70}} = \mathbf{1{,}39}$$

$z_b = 1{,}645$. Vì $1{,}39 < 1{,}645$ → **không có cơ sở bác bỏ** bảo đảm của nhà sản xuất.

💼 Kiểm định phương sai là công cụ của **kiểm soát chất lượng**: không chỉ sản phẩm phải đúng kích
thước trung bình, mà **độ dao động** cũng phải trong giới hạn. Máy chạy đúng trung bình nhưng dao
động lớn thì vẫn cho nhiều phế phẩm — đó là ý tưởng của biểu đồ kiểm soát (control chart) trong
quản trị sản xuất.

---

## 8. 📚 Giá trị p

Giáo trình dạy theo lối **miền tới hạn** — so $K_{tn}$ với phân vị. Nhưng mọi phần mềm thống kê
hiện đại (Excel, SPSS, R, Python) đều báo **giá trị p**. Đây là phần bổ sung, cần để đọc được
kết quả máy.

**Định nghĩa.**

> **Giá trị p** là xác suất quan sát được kết quả **cực đoan như đã thấy hoặc hơn nữa**,
> **NẾU $H_0$ đúng**.

$$
\begin{aligned}
\text{hai phía:} \quad & p = 2\,P(Z > |K_{tn}|) \\
\text{phải:} \quad & p = P(Z > K_{tn}) \\
\text{trái:} \quad & p = P(Z < K_{tn})
\end{aligned}
$$

**Quy tắc quyết định — thay hoàn toàn cho miền tới hạn:**

$$\boxed{p < \alpha \ \Longrightarrow \ \text{BÁC BỎ } H_0}$$

Hai cách **hoàn toàn tương đương**. Nhưng giá trị p **cho biết nhiều hơn**: nó nói mức độ mâu thuẫn
với $H_0$, thay vì chỉ có/không.

| Thí dụ | $K_{tn}$ | Giá trị p | So với $\alpha$ | Kết luận   |
| ------ | -------: | --------: | --------------- | ---------- |
| 2.1    |    0,769 |    0,4418 | $p > 0{,}05$    | giữ $H_0$  |
| 2.2    |   −6,000 |    0,0000 | $p < 0{,}001$   | **bác bỏ** |
| 2.4    |   −0,817 |    0,4142 | $p > 0{,}05$    | giữ $H_0$  |
| 2.5    |   −0,817 |    0,2071 | $p > 0{,}05$    | giữ $H_0$  |

**Cách đọc giá trị p:**

| $p$          | Mức mâu thuẫn với $H_0$ |
| ------------ | ----------------------- |
| $> 0{,}10$   | không có bằng chứng nào |
| 0,05 – 0,10  | bằng chứng yếu          |
| 0,01 – 0,05  | bằng chứng vừa          |
| 0,001 – 0,01 | bằng chứng mạnh         |
| $< 0{,}001$  | bằng chứng rất mạnh     |

### ⚠️ Ba hiểu lầm về giá trị p

| Phát biểu                                                                        | Đúng/Sai   |
| -------------------------------------------------------------------------------- | ---------- |
| "$p = 0{,}03$ nghĩa là xác suất $H_0$ đúng là 3%"                                | ❌ **SAI** |
| "$p = 0{,}03$ nghĩa là xác suất kết luận sai là 3%"                              | ❌ **SAI** |
| "$p = 0{,}03$: nếu $H_0$ đúng thì chỉ 3% khả năng thấy dữ liệu cực đoan thế này" | ✅ đúng    |

$p$ là $P(\text{dữ liệu} \mid H_0)$, **không phải** $P(H_0 \mid \text{dữ liệu})$.
Đây chính là chỗ nhầm $P(H|A)$ với $P(A|H)$ đã cảnh báo ở **bài 4 mục 10**.

Muốn có $P(H_0 \mid \text{dữ liệu})$ thì cần công thức Bayes và một tiên nghiệm — tức là thống kê
Bayes, không phải trường phái này.

### 💼 Trong Excel

| Kiểm định             | Hàm                                         |
| --------------------- | ------------------------------------------- |
| $z$-test một mẫu      | `Z.TEST(mảng; a₀; σ)` → trả thẳng giá trị p |
| $t$-test              | `T.TEST(mảng1; mảng2; đuôi; loại)`          |
| Phân vị $t$           | `T.INV(p; df)`, `T.INV.2T(α; df)`           |
| Phân vị $\chi^2$      | `CHISQ.INV(p; df)`                          |
| Giá trị p từ $\chi^2$ | `CHISQ.DIST.RT(K; df)`                      |

⚠️ Tham số **đuôi** trong `T.TEST`: `1` = một phía, `2` = hai phía. Nhầm là sai gấp đôi giá trị p.

---

## 9. 📚 Bảy điều kiểm định không nói cho bạn

Giáo trình trình bày kỹ thuật mà không cảnh báo về cách diễn giải. Phần này là bổ sung —
và là phần **quan trọng nhất của bài** khi đi làm.

### 1. "Không bác bỏ $H_0$" ≠ "$H_0$ đúng"

Chú ý cách giáo trình luôn viết: *"**không có cơ sở để** bác bỏ"*, chứ không viết *"$H_0$ đúng"*.
Đây không phải chuyện chữ nghĩa.

**Lý do:** không bác bỏ có thể vì $H_0$ đúng, **hoặc** vì cỡ mẫu quá nhỏ để phát hiện sai khác
(sai lầm loại 2). Thí dụ 1.2 cho thấy $\beta = 0{,}82$ — kiểm định đó gần như *không thể* bác bỏ,
dù $H_0$ có sai thật.

> **Vắng bằng chứng không phải bằng chứng vắng.**

💼 Đừng bao giờ báo cáo *"đã chứng minh hai phương án không khác nhau"*. Phải nói:
*"với cỡ mẫu $n$, chưa phát hiện được khác biệt lớn hơn $X$."*

### 2. "Có ý nghĩa thống kê" ≠ "quan trọng trong thực tế"

$K_{tn}$ tỷ lệ với $\sqrt{n}$. **Với $n$ đủ lớn, mọi khác biệt dù nhỏ xíu đều "có ý nghĩa thống kê".**

💼 Ví dụ: A/B test trên 10 triệu lượt cho thấy tỷ lệ chuyển đổi tăng từ 3,00% lên 3,02%,
$p < 0{,}001$. Có ý nghĩa thống kê rực rỡ — nhưng **chênh 0,02 điểm phần trăm** có bù nổi chi phí
triển khai không?

⭐ **Luôn báo cáo cả ba:** giá trị p, **độ lớn của khác biệt**, và **khoảng tin cậy** cho khác biệt đó.
Giá trị p đơn độc là báo cáo thiếu.

### 3. Ngược lại: $n$ nhỏ thì khác biệt lớn cũng không có ý nghĩa

Thí dụ 2.3 (sau đính chính) suýt rơi vào tình huống này: chênh 4,25 cm là rất lớn về mặt thực tế,
nhưng với $n = 16$ thì suýt không đủ để kết luận.

### 4. Chọn $H_1$ SAU khi nhìn dữ liệu là gian lận

Kiểm định một phía dễ bác bỏ hơn hai phía. Nếu bạn nhìn dữ liệu thấy $\overline{X} > a_0$ rồi mới
quyết định dùng $H_1: a > a_0$, thì $\alpha$ thật của bạn là **0,10** chứ không phải 0,05.

**Quy tắc: viết $H_0$, $H_1$ và $\alpha$ ra giấy TRƯỚC khi mở dữ liệu.**

### 5. Thử nhiều lần thì kiểu gì cũng "tìm ra" điều gì đó

Nếu thử 20 giả thuyết độc lập ở mức $\alpha = 0{,}05$, xác suất có **ít nhất một** kết quả "có ý nghĩa"
do may rủi là (dùng bài 3 mục 5):

$$1 - (1 - 0{,}05)^{20} = 1 - 0{,}95^{20} = \mathbf{64\%}$$

Gọi là **vấn đề so sánh bội** (multiple comparisons) hay **p-hacking**.

💼 Rất hay gặp: chạy A/B test, không thấy hiệu quả trên toàn bộ, bèn cắt theo 15 phân khúc
(nam/nữ, các độ tuổi, các thành phố...) cho tới khi tìm được một phân khúc có $p < 0{,}05$.
Kết quả đó gần như chắc chắn là ngẫu nhiên.

**Cách chữa:** chia $\alpha$ cho số phép thử (**hiệu chỉnh Bonferroni**): thử 20 lần thì dùng
$\alpha = 0{,}05/20 = 0{,}0025$. Hoặc: quyết định phân khúc nào sẽ xét **trước khi** chạy test.

### 6. "Nhìn lén" (peeking) làm hỏng $\alpha$

Chạy A/B test và kiểm tra kết quả mỗi ngày, dừng ngay khi thấy $p < 0{,}05$ — đây là dạng khác của
vấn đề 5. Với đủ thời gian, $p$ sẽ chạm dưới 0,05 vào một lúc nào đó **dù không có khác biệt thật**.

**Cách chữa:** cố định cỡ mẫu và thời gian test trước, chỉ xem kết quả khi đủ.

### 7. Mọi công thức đều giả định mẫu NGẪU NHIÊN

Giống hệt cảnh báo ở bài 11 mục 9. Kiểm định đo sai số **lấy mẫu**, không cứu được sai số **chọn mẫu**.
Khảo sát sai đối tượng thì $p = 0{,}0001$ cũng vô nghĩa.

### Danh sách kiểm trước khi báo cáo kết quả

```
   ☐ Đã viết H₀, H₁, α TRƯỚC khi nhìn dữ liệu?
   ☐ Mẫu có thật sự ngẫu nhiên và đại diện?
   ☐ Đã kiểm điều kiện áp dụng (n > 30, np > 5, giả thiết chuẩn...)?
   ☐ Đã báo cáo ĐỘ LỚN khác biệt, không chỉ giá trị p?
   ☐ Đã kèm KHOẢNG TIN CẬY cho độ lớn đó?
   ☐ Có thử nhiều giả thuyết không? Đã hiệu chỉnh chưa?
   ☐ Nếu không bác bỏ được: đã nói rõ cỡ mẫu có đủ lực lượng không?
```

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.
> Chạy từ thư mục gốc khoá học: `cd houedu/xacxuatthongke && python3 bai-12-kiem-dinh.py`.

Code dùng lại module bảng tra ở [thuc_hanh/bang_tra.py](../thuc_hanh/bang_tra.py) — chính là các hàm
đã viết ở bài 11, giờ tách ra thành thư viện dùng chung cho bài 12, 13, 14.
Chạy riêng file đó để đối chiếu cả bốn bảng của phụ lục:

```bash
python3 thuc_hanh/bang_tra.py
```

```python
"""Bài 12 — Kiểm định giả thuyết, các bài toán một mẫu."""

import csv
import math
import pathlib
import sys

sys.path.append("thuc_hanh")
from bang_tra import Z, chi2_quantile, laplace, t_quantile, z_quantile

DATA = pathlib.Path("thuc_hanh/du_lieu")


def ket_luan(K, mien, ten="H0"):
    """In ket luan chuan: K co roi vao mien toi han khong."""
    return f"BAC BO {ten}" if mien else f"CHUA CO CO SO BAC BO {ten}"


# ─────────────────────────────────────────────────────────────
# 1. HAI LOẠI SAI LẦM — Thí dụ 1.2 (tr. 161)
#    X ~ N(theta; 25), n = 9. H0: theta = 3  vs  H1: theta = 4
#    Nguong A0 = 5,5
# ─────────────────────────────────────────────────────────────
print("THI DU 1.2 — hai loai sai lam, nguong A0 = 5,5")
sd_xbar = 5 / math.sqrt(9)          # sigma = 5, n = 9  ->  sigma/can(n) = 5/3
alpha = 1 - Z.cdf((5.5 - 3) / sd_xbar)
beta = Z.cdf((5.5 - 4) / sd_xbar)
print(f"  sigma/can(n) = 5/3 = {sd_xbar:.4f}")
print(f"  alpha = P(X > 5,5 | theta=3) = P(Z > {(5.5 - 3) / sd_xbar:.1f})"
      f" = {alpha:.4f}   (sach: 0,0668)")
print(f"  beta  = P(X < 5,5 | theta=4) = P(Z < {(5.5 - 4) / sd_xbar:.1f})"
      f" = {beta:.4f}   (sach: 0,8159)")
print(f"  Luc luong 1 - beta = {1 - beta:.4f}  ->  RAT YEU")
print("  ⚠ alpha be nhung beta rat lon — hai loai sai lam DANH DOI nhau")

# Doi ngưỡng de thay su danh doi
print()
print("  Doi nguong A0, xem alpha va beta doi nguoc chieu nhau:")
print(f"{'A0':>7}{'alpha':>10}{'beta':>10}{'luc luong':>12}")
for a0 in [3.5, 4.0, 4.5, 5.0, 5.5, 6.0]:
    al = 1 - Z.cdf((a0 - 3) / sd_xbar)
    be = Z.cdf((a0 - 4) / sd_xbar)
    print(f"{a0:>7.1f}{al:>10.4f}{be:>10.4f}{1 - be:>12.4f}")

# ─────────────────────────────────────────────────────────────
# 2. BÀI TOÁN 1 — kỳ vọng, ĐÃ BIẾT sigma
#    Thí dụ 2.1 (tr. 164) va 2.2 (tr. 165)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.1 — bao hiem chi tra TB 8500 do; mau 25 ho so cho 8900")
xbar, a0, sig, n, al = 8900, 8500, 2600, 25, 0.05
K = (xbar - a0) / sig * math.sqrt(n)
zb = z_quantile(1 - al / 2)
print(f"  H0: a = {a0}   H1: a != {a0}  (hai phia)")
print(f"  K = ({xbar}-{a0})/{sig} * can({n}) = {K:.4f}   (sach: 0,77)")
print(f"  z(1-a/2) = {zb:.4f}   |K| = {abs(K):.2f}"
      f"  ->  {ket_luan(K, abs(K) > zb)}")

print()
print("THI DU 2.2 — thung 55 lit (sigma=6); kiem 36 thung thay TB 49 lit")
xbar, a0, sig, n, al = 49, 55, 6, 36, 0.001
K = (xbar - a0) / sig * math.sqrt(n)
zb = z_quantile(al)                 # mot phia trai
print(f"  H0: a = {a0}   H1: a < {a0}  (mot phia TRAI)")
print(f"  K = ({xbar}-{a0})/{sig} * can({n}) = {K:.4f}   (sach: -6)")
print(f"  z(a) = {zb:.4f}   (sach: -3,09)  ->  {ket_luan(K, K < zb)}")

# ─────────────────────────────────────────────────────────────
# 3. BÀI TOÁN 2 — kỳ vọng, CHƯA BIẾT sigma  ->  Student
#    Thí dụ 2.3 (tr. 166) — ⚠ SACH TINH SAI, DAO NGUOC KET LUAN
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.3 — bo toc cao TB 160cm? mau 16 nguoi: X=164,25, s=6,25")
xbar, a0, s, n, al = 164.25, 160, 6.25, 16, 0.05
K = (xbar - a0) / s * math.sqrt(n)
tb = t_quantile(1 - al, n - 1)
print(f"  H0: a = {a0}   H1: a > {a0}  (mot phia PHAI)")
print(f"  K = ({xbar}-{a0})/{s} * can({n}) = {xbar - a0}/{s} * {math.sqrt(n):.0f}"
      f" = {K:.4f}")
print(f"  ⚠ SACH TINH RA 1,36 — dung can(16) = 2 thay vi 4. Dung la {K:.2f}.")
print(f"  t({n - 1}; {1 - al}) = {tb:.4f}   (sach: 1,753)")
print(f"  {K:.2f} > {tb:.3f}  ->  {ket_luan(K, K > tb)}")
print("  ⚠ SACH KET LUAN 'khong co co so bac bo' — NGUOC LAI voi ket qua dung.")
print("     Ket luan dung: bo toc do THAT SU cao hon 160 cm (muc y nghia 5%).")

# ─────────────────────────────────────────────────────────────
# 4. BÀI TOÁN 3 — kiểm định TỶ LỆ
#    Thí dụ 2.4 (tr. 167) va 2.5 (tr. 167)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.4 — toa bao noi 25% hoc sinh doc thuong xuyen; 45/200")
n, m, p0, al = 200, 45, 0.25, 0.05
f = m / n
K = (f - p0) / math.sqrt(p0 * (1 - p0)) * math.sqrt(n)
zb = z_quantile(1 - al / 2)
print(f"  f = {m}/{n} = {f}   H0: p = {p0}   H1: p != {p0}")
print(f"  K = ({f}-{p0})/can({p0}*{1 - p0}) * can({n}) = {K:.4f}"
      f"   (sach: -0,806)")
print(f"  |K| = {abs(K):.4f} vs z = {zb:.4f}  ->  {ket_luan(K, abs(K) > zb)}")

print()
print("THI DU 2.5 — hieu lam dau noi 90% hai long; 132/150 noi hai long")
n, m, p0, al = 150, 132, 0.9, 0.05
f = m / n
K = (f - p0) / math.sqrt(p0 * (1 - p0)) * math.sqrt(n)
zb = z_quantile(al)
print(f"  f = {m}/{n} = {f:.4f}   H0: p = {p0}   H1: p < {p0}  (mot phia TRAI)")
print(f"  K = {K:.4f}   (sach: -0,833)")
print(f"  z(a) = {zb:.4f}   (sach: -1,645)  ->  {ket_luan(K, K < zb)}")
print("  (Hai thi du tren tinh chinh xac deu cho K = -0,8165; sach lam tron"
      " o buoc trung gian.)")

# ─────────────────────────────────────────────────────────────
# 5. BÀI TOÁN 4 — kiểm định PHƯƠNG SAI
#    Thí dụ 2.6 (tr. 169) va 2.7 (tr. 169)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.6 — thiet bi do co sigma = 5mm? mau 19 cai cho s^2 = 33")
n, s2, sig2_0, al = 19, 33, 25, 0.05
K = (n - 1) * s2 / sig2_0
print(f"  H0: sigma^2 = {sig2_0}   K = ({n}-1)*{s2}/{sig2_0} = {K:.2f}"
      f"   (sach: 23,76)")
lo_, hi_ = chi2_quantile(al / 2, n - 1), chi2_quantile(1 - al / 2, n - 1)
print(f"  a) H1: sigma^2 != {sig2_0}: mien chap nhan ({lo_:.2f}; {hi_:.2f})"
      f"   (sach: 8,2 va 31,5)")
print(f"     {K:.2f} nam trong khoang  ->  {ket_luan(K, not lo_ < K < hi_)}")
one_ = chi2_quantile(1 - al, n - 1)
print(f"  b) H1: sigma^2 > {sig2_0}: nguong {one_:.2f}   (sach: 28,9)")
print(f"     {K:.2f} < {one_:.2f}  ->  {ket_luan(K, K > one_)}")

print()
print("THI DU 2.7 — chot khoa sigma = 3 pao? n=35 cho s = 3,5")
n, s, sig0, al = 35, 3.5, 3, 0.05
K = (s - sig0) / (sig0 / math.sqrt(2 * n))
zb = z_quantile(1 - al)
print(f"  n = {n} > 30  ->  dung xap xi s ~ N(sigma; sigma^2/(2n))")
print(f"  K = ({s}-{sig0})/({sig0}/can(2*{n})) = {K:.4f}   (sach: 1,39)")
print(f"  z(1-a) = {zb:.4f}  ->  {ket_luan(K, K > zb)}")

# ─────────────────────────────────────────────────────────────
# 6. 📚 GIÁ TRỊ p — cách hiện đại thay cho miền tới hạn
# ─────────────────────────────────────────────────────────────
print()
print("📚 GIA TRI p — giao trinh khong day, nhung moi phan mem deu bao con so nay")
print(f"{'thi du':>10}{'K':>9}{'gia tri p':>12}{'so voi a=0,05':>16}{'ket luan':>12}")
for lbl, K, kind, al in [("2.1", 0.7692, "hai phia", 0.05),
                         ("2.2", -6.0, "trai", 0.001),
                         ("2.4", -0.8165, "hai phia", 0.05),
                         ("2.5", -0.8165, "trai", 0.05)]:
    if kind == "hai phia":
        pval = 2 * (1 - Z.cdf(abs(K)))
    else:
        pval = Z.cdf(K)
    print(f"{lbl:>10}{K:>9.4f}{pval:>12.4f}"
          f"{('p < a' if pval < al else 'p > a'):>16}"
          f"{('bac bo' if pval < al else 'giu H0'):>12}")
print("  QUY TAC:  p < alpha  ->  BAC BO H0.   p la 'xac suat thay du lieu")
print("  cuc doan nhu vay (hoac hon) NEU H0 dung'.")

# ─────────────────────────────────────────────────────────────
# 7. 💼 GÓC QTKD — doanh thu 60 ngày có đạt chỉ tiêu 50 triệu?
# ─────────────────────────────────────────────────────────────
print()
with open(DATA / "doanh_thu_ngay.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
rev = [float(r["doanh_thu_trieu"]) for r in rows]
n = len(rev)
xbar = sum(rev) / n
s = math.sqrt(sum((x - xbar) ** 2 for x in rev) / (n - 1))
print(f"💼 GOC QTKD — chi tieu doanh thu TB 50 trieu/ngay. Du lieu {n} ngay:")
print(f"  X = {xbar:.2f}   s = {s:.2f}")
a0 = 50
K = (xbar - a0) / s * math.sqrt(n)
tb = t_quantile(0.95, n - 1)
pval = 1 - Z.cdf(K)
print(f"  H0: a = {a0}   H1: a > {a0}  (mot phia PHAI, a = 0,05)")
print(f"  K = {K:.4f}   t({n - 1}; 0,95) = {tb:.4f}   gia tri p = {pval:.5f}")
print(f"  ->  {ket_luan(K, K > tb)}: doanh thu TB THAT SU vuot 50 trieu")

# Nhung neu chi tieu la 55 thi sao?
for a0 in [52, 54, 55, 56]:
    K = (xbar - a0) / s * math.sqrt(n)
    pval = 1 - Z.cdf(K)
    print(f"  Chi tieu {a0}: K = {K:>6.3f}  p = {pval:>7.4f}"
          f"  ->  {'bac bo H0' if K > tb else 'chua du bang chung'}")
print("  ⚠ Cung mot bo du lieu, ket luan doi hoan toan theo NGUONG so sanh.")
print("     Chon nguong TRUOC khi nhin du lieu, khong phai sau.")
```

Kết quả chạy thật:

```
THI DU 1.2 — hai loai sai lam, nguong A0 = 5,5
  sigma/can(n) = 5/3 = 1.6667
  alpha = P(X > 5,5 | theta=3) = P(Z > 1.5) = 0.0668   (sach: 0,0668)
  beta  = P(X < 5,5 | theta=4) = P(Z < 0.9) = 0.8159   (sach: 0,8159)
  Luc luong 1 - beta = 0.1841  ->  RAT YEU
  ⚠ alpha be nhung beta rat lon — hai loai sai lam DANH DOI nhau

  Doi nguong A0, xem alpha va beta doi nguoc chieu nhau:
     A0     alpha      beta   luc luong
    3.5    0.3821    0.3821      0.6179
    4.0    0.2743    0.5000      0.5000
    4.5    0.1841    0.6179      0.3821
    5.0    0.1151    0.7257      0.2743
    5.5    0.0668    0.8159      0.1841
    6.0    0.0359    0.8849      0.1151

THI DU 2.1 — bao hiem chi tra TB 8500 do; mau 25 ho so cho 8900
  H0: a = 8500   H1: a != 8500  (hai phia)
  K = (8900-8500)/2600 * can(25) = 0.7692   (sach: 0,77)
  z(1-a/2) = 1.9600   |K| = 0.77  ->  CHUA CO CO SO BAC BO H0

THI DU 2.2 — thung 55 lit (sigma=6); kiem 36 thung thay TB 49 lit
  H0: a = 55   H1: a < 55  (mot phia TRAI)
  K = (49-55)/6 * can(36) = -6.0000   (sach: -6)
  z(a) = -3.0902   (sach: -3,09)  ->  BAC BO H0

THI DU 2.3 — bo toc cao TB 160cm? mau 16 nguoi: X=164,25, s=6,25
  H0: a = 160   H1: a > 160  (mot phia PHAI)
  K = (164.25-160)/6.25 * can(16) = 4.25/6.25 * 4 = 2.7200
  ⚠ SACH TINH RA 1,36 — dung can(16) = 2 thay vi 4. Dung la 2.72.
  t(15; 0.95) = 1.7531   (sach: 1,753)
  2.72 > 1.753  ->  BAC BO H0
  ⚠ SACH KET LUAN 'khong co co so bac bo' — NGUOC LAI voi ket qua dung.
     Ket luan dung: bo toc do THAT SU cao hon 160 cm (muc y nghia 5%).

THI DU 2.4 — toa bao noi 25% hoc sinh doc thuong xuyen; 45/200
  f = 45/200 = 0.225   H0: p = 0.25   H1: p != 0.25
  K = (0.225-0.25)/can(0.25*0.75) * can(200) = -0.8165   (sach: -0,806)
  |K| = 0.8165 vs z = 1.9600  ->  CHUA CO CO SO BAC BO H0

THI DU 2.5 — hieu lam dau noi 90% hai long; 132/150 noi hai long
  f = 132/150 = 0.8800   H0: p = 0.9   H1: p < 0.9  (mot phia TRAI)
  K = -0.8165   (sach: -0,833)
  z(a) = -1.6449   (sach: -1,645)  ->  CHUA CO CO SO BAC BO H0
  (Hai thi du tren tinh chinh xac deu cho K = -0,8165; sach lam tron o buoc trung gian.)

THI DU 2.6 — thiet bi do co sigma = 5mm? mau 19 cai cho s^2 = 33
  H0: sigma^2 = 25   K = (19-1)*33/25 = 23.76   (sach: 23,76)
  a) H1: sigma^2 != 25: mien chap nhan (8.23; 31.53)   (sach: 8,2 va 31,5)
     23.76 nam trong khoang  ->  CHUA CO CO SO BAC BO H0
  b) H1: sigma^2 > 25: nguong 28.87   (sach: 28,9)
     23.76 < 28.87  ->  CHUA CO CO SO BAC BO H0

THI DU 2.7 — chot khoa sigma = 3 pao? n=35 cho s = 3,5
  n = 35 > 30  ->  dung xap xi s ~ N(sigma; sigma^2/(2n))
  K = (3.5-3)/(3/can(2*35)) = 1.3944   (sach: 1,39)
  z(1-a) = 1.6449  ->  CHUA CO CO SO BAC BO H0

📚 GIA TRI p — giao trinh khong day, nhung moi phan mem deu bao con so nay
    thi du        K   gia tri p   so voi a=0,05    ket luan
       2.1   0.7692      0.4418           p > a      giu H0
       2.2  -6.0000      0.0000           p < a      bac bo
       2.4  -0.8165      0.4142           p > a      giu H0
       2.5  -0.8165      0.2071           p > a      giu H0
  QUY TAC:  p < alpha  ->  BAC BO H0.   p la 'xac suat thay du lieu
  cuc doan nhu vay (hoac hon) NEU H0 dung'.

💼 GOC QTKD — chi tieu doanh thu TB 50 trieu/ngay. Du lieu 60 ngay:
  X = 55.24   s = 16.61
  H0: a = 50   H1: a > 50  (mot phia PHAI, a = 0,05)
  K = 2.4447   t(59; 0,95) = 1.6711   gia tri p = 0.00725
  ->  BAC BO H0: doanh thu TB THAT SU vuot 50 trieu
  Chi tieu 52: K =  1.512  p =  0.0653  ->  chua du bang chung
  Chi tieu 54: K =  0.579  p =  0.2813  ->  chua du bang chung
  Chi tieu 55: K =  0.113  p =  0.4551  ->  chua du bang chung
  Chi tieu 56: K = -0.354  p =  0.6382  ->  chua du bang chung
  ⚠ Cung mot bo du lieu, ket luan doi hoan toan theo NGUONG so sanh.
     Chon nguong TRUOC khi nhin du lieu, khong phai sau.
```

Năm điểm đáng để ý:

1. **Bảng $\alpha$–$\beta$**: hai cột chạy **ngược chiều nhau** hoàn hảo. Ở $A_0 = 4{,}0$ thì
   $\beta = 0{,}5$ — kiểm định lúc đó chỉ ngang việc tung đồng xu.
2. **Thí dụ 2.3**: `K = 4.25/6.25 * 4 = 2.7200` — dòng code in ra cả phép tính trung gian
   để thấy $\sqrt{16} = 4$. Kết luận `BAC BO H0`, ngược với sách.
3. **Thí dụ 2.4 và 2.5 cùng cho `-0.8165`** — trùng hợp, và cả hai đều lệch nhẹ so với số in trong
   sách (−0,806 và −0,833) do làm tròn trung gian. Kết luận không đổi.
4. **Bảng giá trị p**: thí dụ 2.2 cho $p = 0{,}0000$ — bằng chứng áp đảo, khác hẳn thí dụ 2.1
   với $p = 0{,}44$. Một con số nói được nhiều hơn "bác bỏ / không bác bỏ".
5. **Phần cuối**: cùng bộ dữ liệu, chỉ tiêu 50 thì bác bỏ ($p = 0{,}007$), chỉ tiêu 52 thì không
   ($p = 0{,}065$). **Ngưỡng quyết định tất cả** — nên phải chọn ngưỡng trước.

---

## 11. Tự thử

1. Ở thí dụ 1.2, đổi $n$ từ 9 lên 36 (giữ ngưỡng ở chỗ cho $\alpha = 0{,}0668$).
   $\beta$ giảm còn bao nhiêu? Đây là **cách duy nhất** giảm cả hai loại sai lầm.
2. Ở thí dụ 2.1, đổi $\alpha$ từ 0,05 xuống 0,01 rồi lên 0,10. Kết luận có đổi không?
   Với $\alpha$ bằng bao nhiêu thì bắt đầu bác bỏ được? (So với giá trị p = 0,44.)
3. Ở thí dụ 2.3, tìm cỡ mẫu $n$ nhỏ nhất để vẫn bác bỏ được $H_0$ (giữ $\overline{X}$ và $s$).
   Rồi thử ngược: giữ $n = 16$, tìm $\overline{X}$ nhỏ nhất để bác bỏ được.
4. Viết hàm tính **lực lượng** $1-\beta$ cho bài toán 1, với $H_1$ cụ thể. Vẽ bảng lực lượng theo
   $n = 10, 30, 100, 300$ khi khác biệt thật là $0{,}3\sigma$.
5. Kiểm chứng liên hệ **kiểm định ↔ khoảng tin cậy**: với dữ liệu doanh thu, tính khoảng tin cậy
   95% hai phía, rồi kiểm định $H_0: a = a_0$ với $a_0$ chạy từ 48 đến 62. Ngưỡng bác bỏ có trùng
   đúng hai đầu khoảng tin cậy không?
6. Mô phỏng **p-hacking**: sinh 20 bộ dữ liệu ngẫu nhiên từ **cùng một** phân phối (tức $H_0$ đúng
   hoàn toàn), kiểm định từng bộ ở $\alpha = 0{,}05$. Có bao nhiêu bộ "có ý nghĩa"?
   Lặp 1.000 lần, tỷ lệ có **ít nhất một** kết quả sai bằng bao nhiêu? So với $1 - 0{,}95^{20} = 64\%$.
7. Mô phỏng **peeking**: sinh dữ liệu từng ngày với $H_0$ đúng, kiểm định lại mỗi ngày trong 30 ngày,
   dừng ngay khi $p < 0{,}05$. Tỷ lệ "bác bỏ nhầm" là bao nhiêu? Có bằng 5% không?

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)       | Tiếng Anh                         | Ghi chú                       |
| ----------------------------- | --------------------------------- | ----------------------------- |
| Kiểm định giả thuyết          | Hypothesis testing                |                               |
| Giả thuyết gốc                | Null hypothesis                   | $H_0$                         |
| Giả thuyết đối, đối thuyết    | Alternative hypothesis            | $H_1$                         |
| Giả thuyết đơn / phức         | Simple / Composite hypothesis     |                               |
| Tiêu chuẩn kiểm định          | Test statistic                    | $K$                           |
| Miền tới hạn, miền bác bỏ     | Critical region, Rejection region | $B_\alpha$                    |
| Mức ý nghĩa                   | Significance level                | $\alpha$                      |
| Sai lầm loại 1                | Type I error                      | bác bỏ $H_0$ đúng             |
| Sai lầm loại 2                | Type II error                     | chấp nhận $H_0$ sai           |
| Lực lượng                     | Power                             | $1-\beta$                     |
| Nguyên lý xác suất nhỏ        | Principle of rare events          |                               |
| Kiểm định hai phía / một phía | Two-tailed / One-tailed test      |                               |
| Giá trị p                     | p-value                           | 📚 mục 8                      |
| Có ý nghĩa thống kê           | Statistically significant         | ⚠️ ≠ quan trọng thực tế       |
| So sánh bội                   | Multiple comparisons              | 📚 mục 9                      |
| Hiệu chỉnh Bonferroni         | Bonferroni correction             | $\alpha/k$                    |
| Nhìn lén                      | Peeking, optional stopping        | 📚 mục 9                      |
| Bổ đề Neyman – Pearson      | Neyman–Pearson lemma              | tr. 160, tiêu chuẩn mạnh nhất |

---

## 13. Câu hỏi tự kiểm tra

1. Vì sao người ta cố định $\alpha$ mà không cố định $\beta$? Nêu hai lý do của giáo trình.
2. Vì sao không thể giảm đồng thời $\alpha$ và $\beta$? Có cách nào giảm cả hai không?
3. Cùng $\alpha = 0{,}05$: phân vị của kiểm định một phía và hai phía khác nhau thế nào?
   Kiểm định nào dễ bác bỏ $H_0$ hơn, và vì sao điều đó nguy hiểm?
4. Giải thích liên hệ giữa **miền chấp nhận $H_0$** và **khoảng tin cậy**. Cho một ví dụ dùng
   khoảng tin cậy để kiểm định mà không cần tính lại.
5. Vì sao kiểm định tỷ lệ dùng $p_0$ ở mẫu số, còn khoảng tin cậy cho tỷ lệ dùng $f$?
6. Một nhà cung cấp cam kết tỷ lệ lỗi không quá 2%. Kiểm 500 sản phẩm thấy 14 lỗi.
   a) Đặt $H_0$, $H_1$. b) Tính $K_{tn}$ và giá trị p. c) Kết luận ở $\alpha = 0{,}05$.
7. Một A/B test cho $p = 0{,}048$ với 2 triệu lượt truy cập, tỷ lệ chuyển đổi tăng từ 2,50% lên 2,52%.
   Có nên triển khai không? Nêu ít nhất ba yếu tố cần xét ngoài giá trị p.
8. Phát biểu nào sau đây đúng về $p = 0{,}02$?
   a) Xác suất $H_0$ đúng là 2%. b) Xác suất kết luận sai là 2%.
   c) Nếu $H_0$ đúng thì chỉ 2% khả năng thấy dữ liệu cực đoan thế này.
9. Một nhóm chạy 30 kiểm định độc lập và tìm được 2 kết quả có $p < 0{,}05$. Số kết quả "có ý nghĩa"
   kỳ vọng do may rủi là bao nhiêu? Kết luận của họ đáng tin không?
10. Bài toán thí dụ 2.3 sau khi đính chính: nếu nhà nhân chủng học đặt $H_1: a \ne 160$ (hai phía)
    thay vì $a > 160$, kết luận có đổi không? Tính lại.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 12 — KIỂM ĐỊNH GIẢ THUYẾT, MỘT MẪU         (Ch. V §1–2, tr.158–170) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  H₀ giả thuyết GỐC (thường ĐƠN)   H₁ ĐỐI THUYẾT                          ║
║  ⭐ QUY TẮC VÀNG: H₀ = điều muốn BÁC BỎ, H₁ = điều muốn CHỨNG MINH       ║
║      (kiểm định chỉ bác bỏ được, KHÔNG BAO GIỜ chứng minh H₀ đúng)       ║
║                                                                          ║
║  NGUYÊN LÝ XÁC SUẤT NHỎ: nếu H₀ đúng mà dữ liệu quá khó xảy ra           ║
║                          → có lẽ H₀ sai                                  ║
║                                                                          ║
║  HAI LOẠI SAI LẦM                                                        ║
║  ┌──────────────┬─────────────────────┬────────────────────────┐         ║
║  │              │   H₀ THẬT SỰ ĐÚNG   │    H₀ THẬT SỰ SAI      │         ║
║  ├──────────────┼─────────────────────┼────────────────────────┤         ║
║  │ chấp nhận H₀ │         ✓           │  SAI LẦM LOẠI 2  (β)   │         ║
║  │ bác bỏ H₀    │ SAI LẦM LOẠI 1 (α)  │  ✓  lực lượng 1−β      │         ║
║  └──────────────┴─────────────────────┴────────────────────────┘         ║
║      α ↓ thì β ↑ — LUÔN LUÔN. Giảm cả hai: chỉ có TĂNG CỠ MẪU.           ║
║      cố định α vì DỄ TÍNH (chỉ cần phân phối của K khi H₀ đúng)          ║
║                                                                          ║
║  BA DẠNG MIỀN TỚI HẠN  (chọn theo H₁)                                    ║
║      H₁: θ ≠ θ₀  → HAI PHÍA,  bác bỏ khi |K| > z_{1−α/2}   (1,96)        ║
║      H₁: θ < θ₀  → TRÁI,      bác bỏ khi K < z_α           (−1,645)      ║
║      H₁: θ > θ₀  → PHẢI,      bác bỏ khi K > z_{1−α}       (1,645)       ║
║      ⚠ một phía DỄ bác bỏ hơn → phải chọn H₁ TRƯỚC khi xem dữ liệu       ║
║                                                                          ║
║  BỐN BÀI TOÁN MỘT MẪU — TIÊU CHUẨN K                                     ║
║  ┌───┬───────────────┬──────────────────────────┬──────────────┐         ║
║  │ 1 │ a, BIẾT σ     │ K = (X̄−a₀)/σ₀ · √n       │ N(0;1)       │         ║
║  │ 2 │ a, CHƯA BIẾT σ│ K = (X̄−a₀)/s  · √n       │ t(n−1)       │         ║
║  │ 3 │ tỷ lệ p       │ K = (f−p₀)/√(p₀(1−p₀))·√n│ ≈ N(0;1)     │         ║
║  │ 4 │ phương sai σ² │ K = (n−1)s²/σ₀²          │ χ²(n−1)      │         ║
║  └───┴───────────────┴──────────────────────────┴──────────────┘         ║
║      ⚠ bài toán 3: mẫu số dùng p₀ (KHÔNG dùng f như khoảng tin cậy)      ║
║      ⚠ n > 30: bài toán 4 có thể dùng s ≈ N(σ; σ²/2n) → về chuẩn         ║
║                                                                          ║
║  ⭐⭐ KIỂM ĐỊNH ⟺ KHOẢNG TIN CẬY                                        ║
║      miền CHẤP NHẬN H₀  =  khoảng tin cậy 1−α                            ║
║      bác bỏ H₀: a = a₀  ⟺  a₀ NẰM NGOÀI khoảng tin cậy                  ║
║                                                                          ║
║  📚 GIÁ TRỊ p = P(dữ liệu cực đoan như đã thấy | H₀ ĐÚNG)                ║
║      QUY TẮC:  p < α  →  BÁC BỎ H₀                                       ║
║      ⚠ p ≠ P(H₀ đúng)! Đây là chỗ nhầm P(H|A) với P(A|H) ở bài 4         ║
║                                                                          ║
║  📚 BẢY CẢNH BÁO                                                         ║
║      1. "không bác bỏ" ≠ "H₀ đúng"  (vắng bằng chứng ≠ bằng chứng vắng)  ║
║      2. có ý nghĩa THỐNG KÊ ≠ quan trọng THỰC TẾ (K tỷ lệ với √n)        ║
║      3. n nhỏ → khác biệt lớn cũng không phát hiện được                  ║
║      4. chọn H₁ SAU khi xem dữ liệu = gian lận (α thật gấp đôi)          ║
║      5. thử 20 giả thuyết → 64% khả năng có 1 kết quả giả (p-hacking)    ║
║         chữa: Bonferroni α/k                                             ║
║      6. "nhìn lén" và dừng khi p < 0,05 → α thật cao hơn nhiều           ║
║      7. mẫu thiên lệch thì p = 0,0001 cũng vô nghĩa                      ║
║                                                                          ║
║  ⚠⚠ ĐÍNH CHÍNH tr.166 thí dụ 2.3 — LỖI ĐẢO NGƯỢC KẾT LUẬN                ║
║      K = (164,25−160)/6,25 · √16 = 0,68 × 4 = 2,72  (sách in 1,36)       ║
║      2,72 > 1,753  →  BÁC BỎ H₀: bộ tộc THẬT SỰ cao hơn 160 cm           ║
║      (sách kết luận ngược lại)                                           ║
║                                                                          ║
║  💼 QTKD  A/B test, nghiệm thu lô hàng, đánh giá chiến dịch = mục này    ║
║          chọn α theo GIÁ của sai lầm loại 1, không theo thói quen 0,05   ║
║          luôn báo cáo: p + ĐỘ LỚN khác biệt + KHOẢNG TIN CẬY             ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương V §1–§2, tr. 158–170.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- **Đính chính thí dụ 2.3 (tr. 166):** sách in $K_{tn} \approx 1{,}36$; giá trị đúng là **2,72**
  (sách nhân với 2 thay vì $\sqrt{16} = 4$). Hệ quả: phải **bác bỏ** $H_0$, ngược với kết luận
  in trong sách. Đã đối chiếu bản quét gốc.
- Thí dụ 2.4 và 2.5 (tr. 167): sách in $-0{,}806$ và $-0{,}833$; tính chính xác cả hai đều bằng
  $-0{,}8165$. Chênh lệch do làm tròn trung gian, kết luận không đổi.
- Mục 8 (giá trị p) và mục 9 (bảy cảnh báo): kiến thức bổ sung, không có trong giáo trình.
- Bảng phân vị dùng module [thuc_hanh/bang_tra.py](../thuc_hanh/bang_tra.py), đã đối chiếu khớp
  với bảng 2–5 của phụ lục.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 11 — Ước lượng điểm và khoảng tin cậy](bai_11_uoc_luong_diem_va_khoang_tin_cay.md) ·
Bài sau: Bài 13 — Kiểm định nhiều mẫu và phân tích phương sai
