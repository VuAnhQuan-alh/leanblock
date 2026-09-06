# Bài 8 — Biến ngẫu nhiên hai chiều và hệ số tương quan

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương III §1–§2**, tr. 79–96.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> 📌 **Cần đọc trước:** [Bài 5](bai_05_bien_ngau_nhien_va_luat_phan_phoi.md) · [Bài 6](bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md) · [Bài 7](bai_07_cac_phan_phoi_thong_dung.md)

Giáo trình mở Chương III bằng lý do (tr. 79):

> "Trong thực tế nhiều khi phải xét **đồng thời nhiều biến khác nhau có quan hệ tương hỗ**...
> Việc nghiên cứu **riêng rẽ** từng khía cạnh có thể cho ta các thông tin **không đầy đủ**."

Đây là chương quan trọng nhất cho ngành QTKD trong toàn bộ phần xác suất. Vì mọi câu hỏi kinh doanh
đáng giá đều là câu hỏi về **quan hệ giữa hai biến**: chi quảng cáo và doanh số, giá và lượng bán,
mức lương và tỷ lệ nghỉ việc, số lần mua và giá trị đơn hàng.

Bài này cho bạn hai thứ:

- **Bộ ba phân phối** — đồng thời, biên, có điều kiện. Ba góc nhìn vào cùng một bảng số.
- **Thước đo quan hệ** — hiệp phương sai và hệ số tương quan $\rho$, cùng với **những gì $\rho$
  không đo được** (đây mới là phần đáng tiền).

## Mục lục

1. [Biến ngẫu nhiên hai chiều và hàm phân phối đồng thời](#1-biến-ngẫu-nhiên-hai-chiều-và-hàm-phân-phối-đồng-thời)
2. [Bảng phân phối và phân phối biên](#2-bảng-phân-phối-và-phân-phối-biên)
3. [Phân phối có điều kiện](#3-phân-phối-có-điều-kiện)
4. [Trường hợp liên tục](#4-trường-hợp-liên-tục)
5. [Hiệp phương sai](#5-hiệp-phương-sai)
6. [Hệ số tương quan](#6-hệ-số-tương-quan)
7. [Kỳ vọng có điều kiện và hàm hồi quy](#7-kỳ-vọng-có-điều-kiện-và-hàm-hồi-quy)
8. [Phân phối chuẩn hai chiều](#8-phân-phối-chuẩn-hai-chiều)
9. [📚 Bốn điều hệ số tương quan không nói cho bạn](#9--bốn-điều-hệ-số-tương-quan-không-nói-cho-bạn)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Biến ngẫu nhiên hai chiều và hàm phân phối đồng thời

**Véctơ ngẫu nhiên** (hay biến ngẫu nhiên nhiều chiều) là bộ nhiều biến ngẫu nhiên xét đồng thời.
Giáo trình cho ví dụ (tr. 79): khi nghiên cứu một chi tiết máy, ta quan tâm cùng lúc tới trọng lượng,
kích thước, chất lượng, chất liệu.

Để đơn giản chỉ xét **hai chiều** $(X, Y)$; *"hầu hết các kết quả có thể mở rộng khá dễ dàng cho
biến $n$ chiều"*.

**Định nghĩa 1 (tr. 79).** Hàm phân phối xác suất của $(X, Y)$:

$$F(x, y) = P(X < x;\ Y < y), \qquad x, y \in \mathbb{R} \tag{1.1}$$

Còn gọi là **hàm phân phối đồng thời**. (Vẫn dấu $<$ ngặt như bài 5 — nhớ khác biệt quy ước.)

**Bốn tính chất (tr. 80):**

$$
\begin{aligned}
&\text{(i)} && 0 \le F(x,y) \le 1 \\
&\text{(ii)} && F \text{ không giảm theo từng đối số} \\
&\text{(iii)} && F(-\infty, y) = F(x, -\infty) = 0, \quad F(+\infty, +\infty) = 1 \\
&\text{(iv)} && P(x_1 \le X < x_2;\ y_1 \le Y < y_2) = F(x_2,y_2) - F(x_1,y_2) - F(x_2,y_1) + F(x_1,y_1)
\end{aligned}
$$

Tính chất (iv) là xác suất để điểm ngẫu nhiên $(X,Y)$ rơi vào **miền chữ nhật**:

```
   y                                   Xác suất rơi vào ô gạch =
   │                                     F(x₂,y₂)  ← cả góc lớn
 y₂├────────┬───────┐                  − F(x₁,y₂)  ← trừ dải trái
   │        │▒▒▒▒▒▒▒│                  − F(x₂,y₁)  ← trừ dải dưới
 y₁├────────┼───────┤                  + F(x₁,y₁)  ← cộng lại vì đã trừ 2 lần
   │        │       │
   └────────┴───────┴──► x              (chính là bao hàm–loại trừ, bài 3)
           x₁      x₂
```

### Phân phối biên

Cho một biến chạy tới $+\infty$ thì biến kia "hiện ra":

$$
F(x; +\infty) = P(X < x) = F_1(x), \qquad
F(+\infty; y) = P(Y < y) = F_2(y)
$$

$F_1$, $F_2$ gọi là các **phân phối biên** (marginal) — *"đó cũng chính là các phân phối (một chiều)
thông thường của $X$ và $Y$"* (tr. 80).

### Độc lập

**Định nghĩa 2 (tr. 81).** $X$ và $Y$ **độc lập** nếu

$$F(x, y) = F_1(x)\,F_2(y) \tag{1.2}$$

Đây chính là định nghĩa độc lập ở bài 3 ($P(AB) = P(A)P(B)$), áp cho hai sự kiện $\{X<x\}$ và $\{Y<y\}$.

⚠️ **Câu quan trọng nhất của mục này** (tr. 81):

> "Nếu $X$ và $Y$ độc lập... từ các phân phối biên có thể xác định được phân phối của $(X,Y)$.
> Tuy nhiên chúng **không đủ để xác định phân phối đồng thời nếu $X$ và $Y$ không độc lập**."

**Phân phối đồng thời chứa nhiều thông tin hơn hai phân phối biên cộng lại.** Biết riêng phân phối
doanh thu và riêng phân phối chi phí thì **không** suy ra được phân phối lợi nhuận — trừ khi chúng
độc lập, mà chúng thì không.

Chiều ngược lại luôn được: từ đồng thời → luôn tính ra biên. Mất thông tin, không lấy lại được.

---

## 2. Bảng phân phối và phân phối biên

**Định nghĩa 3 (tr. 81).** Bảng phân phối xác suất của $(X, Y)$ rời rạc:

| $X \backslash Y$ | $y_1$      | $y_2$      | $\cdots$ | $y_m$      | $p_1(x)$   |
| ---------------- | ---------- | ---------- | -------- | ---------- | ---------- |
| $x_1$            | $p_{11}$   | $p_{12}$   | $\cdots$ | $p_{1m}$   | $p_1(x_1)$ |
| $x_2$            | $p_{21}$   | $p_{22}$   | $\cdots$ | $p_{2m}$   | $p_1(x_2)$ |
| $\vdots$         |            |            |          |            |            |
| $x_n$            | $p_{n1}$   | $p_{n2}$   | $\cdots$ | $p_{nm}$   | $p_1(x_n)$ |
| **$p_2(y)$**     | $p_2(y_1)$ | $p_2(y_2)$ | $\cdots$ | $p_2(y_m)$ | **1**      |

trong đó $p_{ij} = P(X = x_i;\ Y = y_j)$ là **xác suất đồng thời**.

**Hai tính chất** (tr. 82) — y hệt trường hợp một chiều:

$$\text{(i) } p_{ij} \ge 0 \ \forall i,j \qquad \text{(ii) } \sum_i\sum_j p_{ij} = 1$$

**Phân phối biên = tổng hàng và tổng cột** (1.4):

$$P(X = x_i) = p_1(x_i) = \sum_j p_{ij}, \qquad P(Y = y_j) = p_2(y_j) = \sum_i p_{ij}$$

**Tên gọi "biên" (marginal) đến từ đâu?** Vì hai phân phối này nằm ở **lề** (margin) của bảng —
cột cuối và hàng cuối. Đúng nghĩa đen.

**Hàm phân phối** (1.3): $F(x,y) = \displaystyle\sum_{x_i < x}\sum_{y_j < y} p_{ij}$

**Độc lập** (1.5): $p_{ij} = p_1(x_i)\,p_2(y_j)$ với **mọi** cặp $(i,j)$.
Chỉ cần **một** ô sai là đã phụ thuộc.

### Thí dụ 1.1 (tr. 82)

> Cho bảng phân phối đồng thời. Tìm luật phân phối của $X$ và $Y$, rồi tính $F(2, 3)$.

| $X \backslash Y$ |        1 |        2 |        3 | **$p_1(x)$** |
| ---------------- | -------: | -------: | -------: | -----------: |
| **1**            |     0,10 |     0,25 |     0,10 |     **0,45** |
| **2**            |     0,15 |     0,05 |     0,35 |     **0,55** |
| **$p_2(y)$**     | **0,25** | **0,30** | **0,45** |     **1,00** |

*Giải.* Lấy tổng hàng và tổng cột được ngay hai phân phối biên (in đậm).

$$F(2,3) = \sum_{x_i < 2}\sum_{y_j < 3} p_{ij} = p_{11} + p_{12} = 0{,}10 + 0{,}25 = \mathbf{0{,}35}$$

⚠️ Chú ý: $x_i < 2$ nên chỉ lấy $x_i = 1$; $y_j < 3$ nên chỉ lấy $y_j = 1, 2$. **Dấu ngặt.**
Nếu dùng quy ước $\le$ (Excel) sẽ ra $1{,}00$ — sai hoàn toàn.

**Kiểm độc lập:** $p_{11} = 0{,}10$ nhưng $p_1(1)\,p_2(1) = 0{,}45 \times 0{,}25 = 0{,}1125$.
Khác nhau → (1.5) bị phá → **$X$ và $Y$ không độc lập**.

### 💼 Góc QTKD — bảng chéo chính là phân phối đồng thời

Mọi **bảng chéo** (cross-tab, pivot table) bạn dựng trong Excel đều là một bảng phân phối đồng thời,
chỉ khác là ghi **số lượng** thay vì **tỷ lệ**. Chia cho tổng là ra ngay.

Ví dụ 1.000 khách hàng, chéo theo *số lần mua/năm* ($X$) và *mức chi mỗi đơn* ($Y$, triệu đồng):

| $X \backslash Y$ |     1 tr |     2 tr |     3 tr | **$p_1(x)$** |
| ---------------- | -------: | -------: | -------: | -----------: |
| **1 lần**        |     0,18 |     0,12 |     0,05 |     **0,35** |
| **2 lần**        |     0,12 |     0,16 |     0,12 |     **0,40** |
| **3 lần**        |     0,04 |     0,09 |     0,12 |     **0,25** |
| **$p_2(y)$**     | **0,34** | **0,37** | **0,29** |     **1,00** |

- Hàng lề $p_1$: *"35% khách chỉ mua 1 lần/năm"* — báo cáo tần suất mua.
- Cột lề $p_2$: *"34% đơn hàng ở mức 1 triệu"* — báo cáo giá trị đơn.
- Ô trong bảng: *"18% khách vừa mua ít vừa chi ít"* — **đây mới là phân khúc thật**.

Hai báo cáo lề riêng rẽ **không** cho bạn biết ô 18% đó. Đúng như câu ở mục 1: biên không suy ra
được đồng thời.

---

## 3. Phân phối có điều kiện

Cố định $Y = y_j$ rồi hỏi phân phối của $X$ thay đổi thế nào. Dùng công thức xác suất có điều kiện
ở bài 3:

$$P(X = x_i \mid Y = y_j) = \frac{p_{ij}}{p_2(y_j)} \tag{1.6}$$

Nghĩa hình học: **lấy một cột của bảng rồi chuẩn hoá để tổng bằng 1**.

```
   Bảng gốc                 Lấy cột Y=1             Chuẩn hoá
   ┌────┬────┬────┐         ┌────┐                  ┌──────┐
   │0,10│0,25│0,10│         │0,10│                  │ 0,40 │  ← 0,10/0,25
   ├────┼────┼────┤   ──►   ├────┤       ──►        ├──────┤
   │0,15│0,05│0,35│         │0,15│                  │ 0,60 │  ← 0,15/0,25
   └────┴────┴────┘         └────┘                  └──────┘
                          tổng = 0,25              tổng = 1,00
```

### Thí dụ 1.2 (tr. 83)

> Tìm phân phối có điều kiện của $X$ biết $Y = 1$, ở bài toán thí dụ 1.1.

$$P(X=1 \mid Y=1) = \frac{0{,}10}{0{,}25} = 0{,}40, \qquad P(X=2 \mid Y=1) = \frac{0{,}15}{0{,}25} = 0{,}60$$

| $x$             | 1    | 2    |
| --------------- | ---- | ---- |
| $p(x \mid Y=1)$ | 0,40 | 0,60 |

**So sánh với phân phối biên** $p_1 = (0{,}45;\ 0{,}55)$: biết $Y = 1$ đã làm xác suất $X=1$
tụt từ 0,45 xuống 0,40. **Thông tin về $Y$ có giá trị** — đúng vì hai biến không độc lập.

Nếu chúng độc lập, hai bảng sẽ **giống hệt nhau** — đó là một cách kiểm độc lập khác.

**Điều kiện tổng quát hơn** (1.7, tr. 84): điều kiện có thể là một **khoảng** chứ không chỉ một điểm:

$$P(X = x_i \mid y_1 < Y < y_2) = \frac{P(X = x_i;\ y_1 < Y < y_2)}{P(y_1 < Y < y_2)}$$

### 💼 Góc QTKD — đây là "phân khúc khách hàng", viết bằng công thức

| Ngôn ngữ xác suất                        | Ngôn ngữ kinh doanh                                 |
| ---------------------------------------- | --------------------------------------------------- |
| Phân phối biên $p_2(y)$                  | báo cáo tổng thể: "trung bình mỗi đơn 1,95 triệu"   |
| Phân phối có điều kiện $p(y \mid X = 3)$ | phân khúc: "khách mua 3 lần/năm chi bao nhiêu?"     |
| $E(Y \mid X = x)$                        | giá trị trung bình của từng phân khúc               |
| $X$, $Y$ độc lập                         | **phân khúc vô nghĩa** — chia thế nào cũng như nhau |

**Toàn bộ nghề phân tích khách hàng nằm ở dòng cuối.** Nếu $X$ và $Y$ độc lập thì chia khách theo
$X$ chẳng cho thêm thông tin gì về $Y$ — việc phân khúc là lãng phí. Chỉ khi chúng **phụ thuộc**
thì phân khúc mới có giá trị, và mức phụ thuộc càng mạnh thì phân khúc càng đáng tiền.

Vì thế trước khi xây dựng chiến lược phân khúc, hãy **kiểm (1.5) trên dữ liệu thật** —
hoặc dùng kiểm định độc lập $\chi^2$ ở bài 13.

---

## 4. Trường hợp liên tục

**Định nghĩa 4 (tr. 84).** Nếu

$$F(x, y) = \int_{-\infty}^{x}\int_{-\infty}^{y} f(u,v)\,du\,dv \tag{1.8a}$$

với $f(x,y) \ge 0$, thì $f(x,y)$ là **hàm mật độ đồng thời**. Về hình học nó là một **mặt cong**
trong không gian, gọi là **mặt phân phối xác suất**. Nếu $f$ liên tục theo cả hai biến:

$$f(x,y) = \frac{\partial^2 F}{\partial x \, \partial y}$$

**Ba tính chất (tr. 85)** — song song với trường hợp một chiều, chỉ đổi $\int$ thành $\iint$:

$$
\text{(i) } f \ge 0 \qquad
\text{(ii) } \iint_{\mathbb{R}^2} f\,dx\,dy = 1 \qquad
\text{(iii) } P[(X,Y) \in D] = \iint_D f(x,y)\,dx\,dy
$$

**Mật độ biên (1.9)** — thay "tổng hàng/cột" bằng "tích phân theo biến kia":

$$f_1(x) = \int_{-\infty}^{+\infty} f(x,y)\,dy, \qquad f_2(y) = \int_{-\infty}^{+\infty} f(x,y)\,dx$$

**Độc lập (1.10):** $f(x,y) = f_1(x)\,f_2(y)$.

**Mật độ có điều kiện (1.11):**

$$\varphi(x \mid y) = \frac{f(x,y)}{f_2(y)}, \qquad \psi(y \mid x) = \frac{f(x,y)}{f_1(x)}$$

### Thí dụ 1.3 (tr. 84) — phân phối đều hai chiều

> $f(x,y) = 1$ với $0 \le x, y \le 1$. Tính $F(x,y)$.

$$F(x,y) = \begin{cases}
0 & x < 0 \text{ hoặc } y < 0 \\
xy & 0 \le x \le 1,\ 0 \le y \le 1 \\
x & 0 \le x \le 1,\ y > 1 \\
y & x > 1,\ 0 \le y \le 1 \\
1 & x > 1,\ y > 1
\end{cases}$$

Giáo trình nhận xét (tr. 85): *"Dạng hàm phân phối thường khá phức tạp, nên người ta **hay dùng
hàm mật độ**."* — năm nhánh cho một bài toán đơn giản nhất có thể.

Tính xác suất trên hình chữ nhật:

$$P(0{,}2 < X < 0{,}7;\ 0{,}25 < Y < 0{,}45) = (0{,}7-0{,}2)(0{,}45-0{,}25) = \mathbf{0{,}1}$$

Về hình học đó là **thể tích** hộp chữ nhật có đáy trên nằm trong mặt $f(x,y) = 1$.
Với biến hai chiều, xác suất là **thể tích** (một chiều thì là diện tích).

### Thí dụ 1.5 (tr. 87)

> $f(x,y) = x + y$ với $0 \le x, y \le 1$. Xác định các hàm mật độ có điều kiện.

*Giải.* Trước hết tìm mật độ biên theo (1.9):

$$f_1(x) = \int_0^1 (x+y)\,dy = x + \frac12, \qquad f_2(y) = y + \frac12 \quad (0 \le x, y \le 1)$$

Rồi theo (1.11):

$$\varphi(x \mid y) = \frac{x+y}{y + 0{,}5}, \qquad \psi(y \mid x) = \frac{x+y}{x + 0{,}5}$$

⚠️ Giáo trình lưu ý (tr. 87): $\varphi(x \mid y)$ là **hàm của $x$**, còn $y$ đóng vai trò **tham số**.
Đổi $y$ thì được một hàm mật độ khác. Đây là chỗ hay lẫn.

Từ (1.11) suy ra $f(x,y) = f_2(y)\varphi(x \mid y) = f_1(x)\psi(y \mid x)$ — và nếu
$\varphi(x \mid y) = f_1(x)$ thì ta có lại điều kiện độc lập (1.10). Rõ ràng ở đây không phải,
nên $X$, $Y$ phụ thuộc.

---

## 5. Hiệp phương sai

Giáo trình xây dựng bằng cách đặt $g(X,Y) = (X - EX)(Y - EY)$ vào công thức kỳ vọng tổng quát (2.1).

**Định nghĩa (tr. 90).** **Hiệp phương sai** của $X$ và $Y$, ký hiệu $\mu_{XY}$:

$$\mu_{XY} = E\big[(X - EX)(Y - EY)\big] = E(XY) - EX \cdot EY \tag{2.2}$$

$$
\mu_{XY} = \sum_i\sum_j x_i y_j\, p(x_i, y_j) - EX \cdot EY \tag{2.2a}
$$

$$
\mu_{XY} = \iint xy\, f(x,y)\,dx\,dy - EX \cdot EY \tag{2.2b}
$$

**Cách nhớ:** hoàn toàn song song với công thức phương sai $VX = E(X^2) - (EX)^2$ ở bài 6.
Thật vậy, giáo trình chỉ ra: *"phương sai là **trường hợp riêng** của hiệp phương sai khi $X = Y$"*:

$$\mu_{XX} = E(X \cdot X) - EX \cdot EX = E(X^2) - (EX)^2 = VX$$

**Ý nghĩa dấu (tr. 90):**

$$
\begin{aligned}
\mu_{XY} > 0 &\ \Rightarrow \ X, Y \text{ đồng biến} && \text{(cùng tăng, cùng giảm)} \\
\mu_{XY} < 0 &\ \Rightarrow \ X, Y \text{ nghịch biến} && \text{(cái này tăng, cái kia giảm)}
\end{aligned}
$$

Hiểu tại sao: nếu $X$ lớn hơn trung bình thường đi kèm $Y$ lớn hơn trung bình, thì tích
$(X-EX)(Y-EY)$ **dương**; trung bình của các tích dương là dương.

### ⚠️ Độc lập ⟹ không tương quan, chiều ngược lại SAI

Giáo trình nêu rõ (tr. 90): $X$, $Y$ độc lập $\Rightarrow E(XY) = EX \cdot EY \Rightarrow \mu_{XY} = 0$.
*"Nhưng điều ngược lại **không chắc đúng**."*

**Định nghĩa 1 (tr. 90).** Nếu $\mu_{XY} = 0$, ta nói $X$ và $Y$ **không tương quan**.

$$\boxed{\text{độc lập} \ \Longrightarrow \ \text{không tương quan}, \qquad \text{chiều ngược lại: SAI}}$$

Giáo trình nói gọn: *"khái niệm độc lập là **mạnh hơn** không tương quan."*

Đây là **cùng một mẫu logic** với "độc lập tổng thể ⟹ độc lập từng đôi" ở bài 3 mục 2.
Trong xác suất, các khái niệm "không liên quan" xếp theo nhiều mức mạnh yếu khác nhau.

### Thí dụ 2.2 (tr. 92) — phản ví dụ kinh điển

> $(X, Y)$ có mật độ $f(x,y) = \dfrac{1}{2\pi}$ trên miền $4x^2 + y^2 < 4$ (hình elip).
> Chứng tỏ $X$, $Y$ phụ thuộc và tính $\mu_{XY}$.

*Giải.* Mật độ biên theo (1.9):

$$f_1(x) = \frac{2}{\pi}\sqrt{1-x^2} \ \ (|x| < 1), \qquad f_2(y) = \frac{\sqrt{4-y^2}}{2\pi} \ \ (|y| < 2)$$

Rõ ràng $f(x,y) \ne f_1(x)f_2(y)$ → **$X$, $Y$ phụ thuộc**.

Nhưng $f_1$, $f_2$ là các **hàm chẵn** nên $EX = EY = 0$, và

$$\mu_{XY} = \iint xy \cdot \frac{1}{2\pi}\,dx\,dy = \frac{1}{2\pi}\int_{-1}^{1} x\,dx \int_{-2\sqrt{1-x^2}}^{2\sqrt{1-x^2}} y\,dy = 0$$

(tích phân trong lấy theo **hàm lẻ có cận đối xứng**). Giáo trình kết luận:

> "Rõ ràng $X$ và $Y$ **không tương quan, nhưng vẫn phụ thuộc nhau**."

**Vì sao?** Vì quan hệ giữa chúng là quan hệ **hình dạng**, không phải quan hệ **tuyến tính**:
biết $X = 0{,}9$ thì $Y$ chỉ có thể nằm trong khoảng rất hẹp quanh 0. Rất phụ thuộc!
Nhưng hiệp phương sai chỉ đo được **xu hướng đi lên hay đi xuống**, và ở đây không có xu hướng nào.

### Ma trận hiệp phương sai

Với biến 2 chiều (tr. 91):

$$\Gamma = \begin{pmatrix} VX & \mu_{XY} \\ \mu_{YX} & VY \end{pmatrix}$$

Đường chéo chính là các phương sai; ma trận **đối xứng** vì $\mu_{XY} = \mu_{YX}$.

💼 Ma trận hiệp phương sai là công cụ trung tâm của **lý thuyết danh mục đầu tư** (Markowitz):
rủi ro của một danh mục không phải tổng rủi ro từng tài sản, mà phụ thuộc vào các $\mu_{ij}$.
Ghép hai tài sản có $\mu_{12} < 0$ làm giảm rủi ro tổng — đó là toàn bộ ý tưởng "đa dạng hoá".

---

## 6. Hệ số tương quan

Giáo trình nêu **hai hạn chế** của hiệp phương sai (tr. 91):

1. *"khó xác định được **miền biến thiên**, nó thay đổi từ cặp biến này sang cặp biến khác"* —
   không biết $\mu = 0{,}09$ là mạnh hay yếu.
2. *"về mặt vật lý nó có **đơn vị đo bằng bình phương** đơn vị đo của $X$ và $Y$"* —
   giống hệt vấn đề của phương sai ở bài 6 mục 4.

Giải pháp: **chuẩn hoá bằng cách chia cho hai độ lệch chuẩn**.

**Định nghĩa (tr. 91).** **Hệ số tương quan**:

$$\rho_{XY} = \frac{\mu_{XY}}{\sigma_X \, \sigma_Y} \tag{2.3}$$

Kết quả là **một số không đơn vị**, và:

$$\boxed{|\rho_{XY}| \le 1}$$

**Ba mốc cần nhớ (tr. 91):**

| $\rho_{XY}$        | Nghĩa                                                                      |
| ------------------ | -------------------------------------------------------------------------- |
| $= \pm 1$          | **tương quan tuyến tính hoàn hảo** — tồn tại $a$, $b$ sao cho $Y = aX + b$ |
| $= 0$              | **không tương quan**                                                       |
| $0 < \|\rho\| < 1$ | tương quan, mức độ đo bằng $\|\rho\|$                                      |

Giáo trình tóm tắt quan hệ (tr. 91):

> "Hai biến **tương quan thì phụ thuộc** (không độc lập), nhưng **không tương quan thì chưa chắc độc lập**."

```
   ┌──────────────────── PHỤ THUỘC ────────────────────┐
   │                                                   │
   │   ┌──────── TƯƠNG QUAN (ρ ≠ 0) ────────┐          │
   │   │                                    │          │
   │   │   ┌── TUYẾN TÍNH HOÀN HẢO ──┐      │          │
   │   │   │        ρ = ±1           │      │          │
   │   │   └─────────────────────────┘      │          │
   │   └────────────────────────────────────┘          │
   │                                                   │
   │   phần còn lại: ρ = 0 nhưng VẪN phụ thuộc         │
   │   (thí dụ 2.2 — hình elip)                        │
   └───────────────────────────────────────────────────┘

           ĐỘC LẬP  =  hoàn toàn bên ngoài vòng lớn
```

### Thí dụ 2.1 (tr. 91)

> Tính $\mu_{XY}$ và $\rho_{XY}$ cho bảng ở thí dụ 1.1.

Từ hai phân phối biên:

$$EX = 1{,}55, \quad VX = 0{,}2475, \qquad EY = 2{,}20, \quad VY = 0{,}66$$

$$
\begin{aligned}
E(XY) &= 1{\cdot}1{\cdot}0{,}10 + 1{\cdot}2{\cdot}0{,}25 + 1{\cdot}3{\cdot}0{,}10 \\
&\quad + 2{\cdot}1{\cdot}0{,}15 + 2{\cdot}2{\cdot}0{,}05 + 2{\cdot}3{\cdot}0{,}35 = 3{,}50
\end{aligned}
$$

$$\mu_{XY} = 3{,}50 - 1{,}55 \times 2{,}20 = \mathbf{0{,}09}$$

$$\rho_{XY} = \frac{0{,}09}{\sqrt{0{,}2475 \times 0{,}66}} = \frac{0{,}09}{0{,}4042} \approx \mathbf{0{,}22}$$

**Cách đọc kết quả:** $\rho = 0{,}22$ là tương quan dương **yếu**. So sánh: nếu chỉ nhìn
$\mu_{XY} = 0{,}09$, bạn không thể nói nó mạnh hay yếu. $\rho$ cho câu trả lời ngay.

### 💼 Góc QTKD — thang đọc $\rho$ trong thực tế

Không có ngưỡng tuyệt đối, nhưng đây là quy ước thường dùng:

| $\|\rho\|$ | Mức        | Ví dụ điển hình                      |
| ---------- | ---------- | ------------------------------------ |
| 0,0 – 0,2  | rất yếu    | tuổi khách hàng vs mức chi tiêu      |
| 0,2 – 0,4  | yếu        | số lần mua vs giá trị mỗi đơn        |
| 0,4 – 0,6  | trung bình | chi quảng cáo vs lượt truy cập       |
| 0,6 – 0,8  | mạnh       | doanh số tháng này vs tháng trước    |
| 0,8 – 1,0  | rất mạnh   | doanh thu vs số lượng bán (cùng giá) |

⚠️ **Cảnh báo về $\rho$ rất cao trong dữ liệu kinh doanh.** Nếu bạn thấy $\rho > 0{,}95$ giữa hai
chỉ số, nhiều khả năng chúng **đo cùng một thứ** (doanh thu và số đơn khi giá cố định), hoặc một
cái được **tính từ** cái kia. Đó không phải phát hiện, đó là trùng lặp — và trong hồi quy bội
(bài 14) nó gây ra vấn đề **đa cộng tuyến**.

---

## 7. Kỳ vọng có điều kiện và hàm hồi quy

**Định nghĩa (tr. 93).** Kỳ vọng có điều kiện của $X$ khi $Y = y^*$:

$$
E(X \mid y^*) = \sum_i x_i\,P(X = x_i \mid Y = y^*) \quad \text{(rời rạc)}
$$

$$
E(X \mid y^*) = \int_{-\infty}^{+\infty} x\,\varphi(x \mid y^*)\,dx \quad \text{(liên tục)}
$$

### ⭐ Cầu nối sang Chương VI

Giáo trình nói rõ ý nghĩa (tr. 93):

> "Kỳ vọng có điều kiện $E(Y \mid X)$ là một **hàm phụ thuộc $x$**, và trong thống kê người ta gọi là
> **hàm hồi quy** của $Y$ đối với $X$. Đồ thị của hàm đó... có tên gọi là **đường hồi quy**."

**Hồi quy — cả một chương VI của giáo trình — chính là bài toán ước lượng $E(Y \mid X = x)$ từ
dữ liệu.** Bài 14 sẽ làm việc đó. Nhớ định nghĩa này thì hồi quy không còn là công thức trên trời.

💼 Nói bằng ngôn ngữ QTKD: *"nếu tôi chi $x$ triệu quảng cáo, doanh số trung bình sẽ là bao nhiêu?"*
Câu trả lời chính là $E(Y \mid X = x)$ — hàm hồi quy.

**Bốn tính chất (tr. 93):**

$$
\begin{aligned}
&\text{(i)} && E[g(X)\,Y \mid X] = g(X)\,E(Y \mid X) && \text{(biết } X \text{ rồi thì } g(X) \text{ là hằng số)} \\
&\text{(ii)} && E(X_1 + X_2 \mid X) = E(X_1 \mid X) + E(X_2 \mid X) \\
&\text{(iii)} && X, Y \text{ độc lập} \Rightarrow E(Y \mid X) = EY && \text{(biết } X \text{ chẳng thêm gì)} \\
&\text{(iv)} && E\big[E(Y \mid X)\big] = EY && \textbf{luật kỳ vọng lặp}
\end{aligned}
$$

⭐ **Tính chất (iv) đáng nhớ nhất.** Nó nói: *lấy trung bình của các trung bình từng phân khúc,
có trọng số là cỡ phân khúc, thì được trung bình toàn bộ.*

💼 Đây là **công cụ kiểm tra báo cáo phân khúc**: nếu trung bình các phân khúc (có trọng số) không
khớp với trung bình tổng thể, ai đó đã tính sai hoặc bỏ sót một phân khúc. Cũng chính là công thức
xác suất đầy đủ (bài 4) viết dưới dạng kỳ vọng.

### Thí dụ 2.3 (tr. 93)

> Cho bảng phân phối. Tính $E(X \mid Y = 1)$ và $E(Y \mid X = 4)$.

| $X \backslash Y$ |    1 |    2 |    3 |
| ---------------- | ---: | ---: | ---: |
| **2**            | 0,15 | 0,08 | 0,27 |
| **4**            | 0,10 | 0,20 | 0,20 |

*Giải.* $p_2(1) = 0{,}25$, nên:

$$P(X=2 \mid Y=1) = \frac{0{,}15}{0{,}25} = 0{,}6, \qquad P(X=4 \mid Y=1) = \frac{0{,}10}{0{,}25} = 0{,}4$$

$$E(X \mid Y = 1) = 2 \cdot 0{,}6 + 4 \cdot 0{,}4 = \mathbf{2{,}8}$$

Tương tự, $p_1(4) = 0{,}50$:

$$P(Y=1 \mid X=4) = 0{,}2, \quad P(Y=2 \mid X=4) = 0{,}4, \quad P(Y=3 \mid X=4) = 0{,}4$$

$$E(Y \mid X = 4) = 1 \cdot 0{,}2 + 2 \cdot 0{,}4 + 3 \cdot 0{,}4 = \mathbf{2{,}2}$$

---

## 8. Phân phối chuẩn hai chiều

Ký hiệu gọn (tr. 94): $a_X = EX$, $a_Y = EY$, $\sigma_X^2 = VX$, $\sigma_Y^2 = VY$,
$\rho = \rho_{XY}$, $\mu = \mu_{XY}$.

**Định nghĩa 2 (tr. 94).** $(X,Y) \sim N(a_X, a_Y, \sigma_X^2, \sigma_Y^2, \rho)$ nếu

$$f(x,y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}\exp\left\{-\frac{1}{2(1-\rho^2)}
\left[\frac{(x-a_X)^2}{\sigma_X^2} + \frac{(y-a_Y)^2}{\sigma_Y^2}
- 2\rho\frac{(x-a_X)(y-a_Y)}{\sigma_X\sigma_Y}\right]\right\} \tag{2.4}$$

### ⭐ Ngoại lệ quan trọng nhất của bài

Giáo trình chỉ ra (tr. 95):

> "Có thể chỉ ra dễ dàng nếu $X$, $Y$ **không tương quan** ($\rho = 0$) thì **giả thiết chuẩn cho phép
> kết luận chúng là độc lập**."

$$\boxed{\text{Với phân phối CHUẨN hai chiều: } \ \rho = 0 \iff \text{độc lập}}$$

Đây là **ngoại lệ duy nhất** của cảnh báo ở mục 5. Với phân phối chuẩn, hai khái niệm trùng nhau.
Với mọi phân phối khác, chúng khác nhau (thí dụ 2.2).

⚠️ Đây cũng là **cái bẫy lớn nhất khi phân tích dữ liệu kinh doanh**: nhiều người học được rằng
"$\rho = 0$ thì độc lập" mà quên mất vế "*nếu dữ liệu chuẩn*". Mà dữ liệu kinh doanh
(doanh thu, thời gian chờ, số đếm) thì hầu như **không chuẩn** — bài 7 mục 5 đã nói.

### Dạng ma trận

Với ma trận hiệp phương sai $\Gamma$ và véctơ $\mathbf{x} = \binom{x}{y}$:

$$f(\mathbf{x}) = \frac{1}{2\pi\sqrt{\det\Gamma}}\exp\left[-\frac12(\mathbf{x} - E\mathbf{x})^{T}\Gamma^{-1}(\mathbf{x} - E\mathbf{x})\right]$$

Dạng này mở rộng thẳng lên $n$ chiều (chỉ đổi hằng số phía trước) — đó là lý do phân phối chuẩn
nhiều chiều thống trị trong thống kê và học máy.

### Thí dụ 2.4 (tr. 95) — công thức nền của hồi quy tuyến tính

> Tính các kỳ vọng và phương sai có điều kiện của phân phối chuẩn hai chiều.

*Giải.* Giáo trình biến đổi $\varphi(x \mid y) = f(x,y)/f_2(y)$ và nhận ra kết quả **vẫn là một
phân phối chuẩn**:

$$X \mid Y = y \ \sim \ N\left(a_X + \rho\frac{\sigma_X}{\sigma_Y}(y - a_Y);\ \sigma_X^2(1-\rho^2)\right)$$

$$\boxed{E(X \mid Y = y) = a_X + \rho\frac{\sigma_X}{\sigma_Y}(y - a_Y)}$$

$$V(X \mid Y = y) = \sigma_X^2(1 - \rho^2)$$

Do tính đối xứng, tương tự cho $Y$:

$$E(Y \mid X = x) = a_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - a_X), \qquad V(Y \mid X = x) = \sigma_Y^2(1-\rho^2)$$

**Ba điều rút ra — cả ba đều quan trọng:**

**1. Hàm hồi quy là đường THẲNG.** $E(Y \mid X = x)$ tuyến tính theo $x$, với hệ số góc
$\rho\dfrac{\sigma_Y}{\sigma_X}$. **Đây chính là công thức hệ số hồi quy** mà bài 14 sẽ ước lượng
từ dữ liệu. Với phân phối chuẩn, hồi quy tuyến tính không phải một *giả định tiện lợi* — nó là
**kết quả toán học chính xác**.

**2. Biết $X$ làm giảm bất định về $Y$ đúng một hệ số $(1-\rho^2)$.** Phương sai tụt từ $\sigma_Y^2$
xuống $\sigma_Y^2(1-\rho^2)$.

$$\text{Tỷ lệ bất định được giải thích} = 1 - (1-\rho^2) = \rho^2$$

⭐ **$\rho^2$ chính là hệ số xác định $R^2$** ở bài 14 — và ý nghĩa của nó đã hiện ra ngay tại đây.

**3. Phương sai có điều kiện KHÔNG phụ thuộc vào $x$.** Dù $X$ nhận giá trị nào, độ tán xạ của $Y$
quanh đường hồi quy vẫn như nhau. Tính chất này gọi là **phương sai thuần nhất**
(homoscedasticity) và là một giả thiết bắt buộc của hồi quy tuyến tính.

### 💼 Góc QTKD — đọc ba con số trên

Chi quảng cáo $X$ và doanh số $Y$, giả sử chuẩn hai chiều với
$a_X = 100$ tr, $\sigma_X = 20$; $a_Y = 500$ tr, $\sigma_Y = 80$; $\rho = 0{,}6$.

**Chi 130 triệu thì doanh số dự kiến bao nhiêu?**

$$E(Y \mid X = 130) = 500 + 0{,}6 \cdot \frac{80}{20}(130 - 100) = 500 + 2{,}4 \cdot 30 = \mathbf{572 \text{ tr}}$$

**Dự báo đó chắc chắn đến mức nào?**

$$\sigma(Y \mid X) = 80\sqrt{1 - 0{,}36} = 80 \cdot 0{,}8 = 64 \text{ tr}$$

Áp quy tắc $2\sigma$ (bài 7): khoảng $572 \pm 128$, tức **444 – 700 triệu** với xác suất 95%.

**Đây mới là cách trình bày dự báo cho ban giám đốc.** Nói "chi 130 sẽ ra 572" là nói dối bằng
sự chính xác giả tạo. Phải nói kèm khoảng.

Và chú ý: $\rho^2 = 0{,}36$ — quảng cáo chỉ giải thích **36%** biến động doanh số. 64% còn lại
đến từ mùa vụ, đối thủ, kinh tế vĩ mô, chất lượng sản phẩm. Một $\rho = 0{,}6$ nghe "khá mạnh"
nhưng thực ra để lại rất nhiều điều chưa giải thích được.

---

## 9. 📚 Bốn điều hệ số tương quan không nói cho bạn

Giáo trình định nghĩa $\rho$ và dừng ở đó. Nhưng $\rho$ là con số bị lạm dụng nhiều nhất trong
báo cáo kinh doanh. Bốn cảnh báo dưới đây là phần bổ sung.

### ⚠️ 1. $\rho$ chỉ đo quan hệ TUYẾN TÍNH

Đã thấy ở thí dụ 2.2: quan hệ hình elip cho $\rho = 0$ dù cực kỳ phụ thuộc. Tổng quát hơn,
mọi quan hệ **hình chữ U** đều cho $\rho \approx 0$.

💼 Ví dụ thật: **giá bán và lợi nhuận**. Giá quá thấp → lỗ. Giá quá cao → không ai mua, cũng lỗ.
Có một mức giá tối ưu ở giữa. Quan hệ này là parabol úp ngược → $\rho \approx 0$.
Kết luận "giá không ảnh hưởng lợi nhuận" sẽ là **sai hoàn toàn**.

**Cách tránh: luôn vẽ biểu đồ phân tán trước khi tính $\rho$.**

### ⚠️ 2. Tương quan không phải nhân quả

$\rho$ cao giữa $X$ và $Y$ có thể do bốn nguyên nhân khác nhau:

```
   ①  X → Y        X gây ra Y                (điều bạn hy vọng)
   ②  Y → X        chiều ngược lại
   ③  Z → X, Z → Y biến ẩn Z gây ra cả hai   (confounding)
   ④  ngẫu nhiên   trùng hợp, nhất là khi thử nhiều cặp
```

💼 Ví dụ ③ rất hay gặp: *"chi quảng cáo và doanh số tương quan $\rho = 0{,}8$"* — nhưng cả hai
đều tăng vào mùa cao điểm ($Z$ = mùa vụ). Cắt quảng cáo có thể chẳng ảnh hưởng gì.

**Cách tránh: chỉ kết luận nhân quả từ thí nghiệm có đối chứng** (A/B test), không từ dữ liệu quan sát.

### ⚠️ 3. $\rho$ cực kỳ nhạy với giá trị thái quá

Một điểm dữ liệu bất thường có thể kéo $\rho$ từ 0 lên 0,9 hoặc ngược lại. Giống hệt vấn đề của
trung bình ở bài 6 mục 5.

💼 Một khách hàng doanh nghiệp mua đơn 5 tỷ trong tập dữ liệu toàn đơn vài triệu sẽ chi phối
toàn bộ hệ số tương quan.

**Cách tránh: vẽ biểu đồ, kiểm giá trị thái quá, thử tính lại $\rho$ khi bỏ chúng ra.**

### ⚠️ 4. Nghịch lý Simpson (Simpson's paradox)

Tương quan tính trên toàn bộ dữ liệu có thể **ngược dấu** với tương quan tính trong từng nhóm con.

💼 Ví dụ: trên toàn công ty, *thời gian đào tạo* và *hiệu suất* có $\rho < 0$ (đào tạo nhiều thì
hiệu suất thấp?!). Nhưng trong từng phòng ban thì $\rho > 0$. Nguyên nhân: phòng ban khó nhất được
đào tạo nhiều nhất, nhưng vẫn có hiệu suất thấp nhất. Gộp lại thì dấu đảo ngược.

**Cách tránh: luôn kiểm tương quan trong từng phân khúc, không chỉ trên tổng thể.**
Đây chính là lý do phân phối **có điều kiện** ở mục 3 quan trọng đến thế.

### Tóm lại

| $\rho$ nói gì                             | $\rho$ KHÔNG nói gì                   |
| ----------------------------------------- | ------------------------------------- |
| có xu hướng tuyến tính hay không          | có quan hệ phi tuyến hay không        |
| chiều của xu hướng (dấu)                  | ai gây ra ai                          |
| độ mạnh của xu hướng tuyến tính           | có ổn định qua các phân khúc không    |
| $\rho^2$ = tỷ lệ bất định giải thích được | có bị giá trị thái quá chi phối không |

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-08-hai-chieu.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**. Chạy khoảng 1 giây.

Bảy hàm ở đầu file là **toàn bộ Chương III phần rời rạc**. Chú ý cách chúng gọi lẫn nhau:
`rho` gọi `cov`, `cov` gọi `marginal_x/y`, tất cả gọi `E`. Cấu trúc đó phản ánh đúng cấu trúc
lý thuyết.

```python
"""Bài 8 — Biến ngẫu nhiên hai chiều và hệ số tương quan."""

import math
from fractions import Fraction as F

# ─────────────────────────────────────────────────────────────
# Bộ công cụ cho biến HAI CHIỀU RỜI RẠC — dùng cho cả bài.
# Phân phối đồng thời cho dưới dạng dict {(x, y): p}.
# ─────────────────────────────────────────────────────────────
def marginal_x(joint):
    """Phan phoi bien cua X — cong thuc (1.4a): tong theo HANG."""
    out = {}
    for (x, y), p in joint.items():
        out[x] = out.get(x, 0) + p
    return dict(sorted(out.items()))


def marginal_y(joint):
    """Phan phoi bien cua Y — cong thuc (1.4b): tong theo COT."""
    out = {}
    for (x, y), p in joint.items():
        out[y] = out.get(y, 0) + p
    return dict(sorted(out.items()))


def conditional_x_given_y(joint, y0):
    """Phan phoi co dieu kien cua X biet Y = y0 — cong thuc (1.6)."""
    py = marginal_y(joint)[y0]
    return {x: p / py for (x, y), p in sorted(joint.items()) if y == y0}


def E(dist, g=lambda v: v):
    return sum(g(v) * p for v, p in dist.items())


def V(dist):
    return E(dist, lambda v: v * v) - E(dist) ** 2


def cov(joint):
    """Hiep phuong sai — cong thuc (2.2a): E(XY) - EX.EY."""
    exy = sum(x * y * p for (x, y), p in joint.items())
    return exy - E(marginal_x(joint)) * E(marginal_y(joint))


def rho(joint):
    """He so tuong quan — cong thuc (2.3)."""
    return cov(joint) / math.sqrt(
        float(V(marginal_x(joint))) * float(V(marginal_y(joint))))


def is_independent(joint):
    """Kiem dieu kien (1.5): p_ij = p1(xi) * p2(yj) voi MOI cap."""
    px, py = marginal_x(joint), marginal_y(joint)
    return all(joint.get((x, y), 0) == px[x] * py[y] for x in px for y in py)


def show(joint, title):
    px, py = marginal_x(joint), marginal_y(joint)
    print(title)
    print("      " + "".join(f"{y:>9}" for y in py) + f"{'p1(x)':>10}")
    for x in px:
        row = "".join(f"{float(joint.get((x, y), 0)):>9.2f}" for y in py)
        print(f"  x={x} " + row + f"{float(px[x]):>10.2f}")
    print("p2(y) " + "".join(f"{float(py[y]):>9.2f}" for y in py)
          + f"{float(sum(py.values())):>10.2f}")


# ─────────────────────────────────────────────────────────────
# 1. Thí dụ 1.1 (tr. 82) — bảng phân phối đồng thời
# ─────────────────────────────────────────────────────────────
J1 = {(1, 1): F(10, 100), (1, 2): F(25, 100), (1, 3): F(10, 100),
      (2, 1): F(15, 100), (2, 2): F(5, 100), (2, 3): F(35, 100)}
assert sum(J1.values()) == 1
show(J1, "THI DU 1.1 — phan phoi dong thoi va hai phan phoi BIEN")

# F(2,3) — chu y giao trinh dung dau < NGAT (bai 5 muc 5)
f23 = sum(p for (x, y), p in J1.items() if x < 2 and y < 3)
print("  F(2,3) = tong p_ij voi xi<2, yj<3 = p11 + p12 =", f23,
      "=", float(f23), "  (sach: 0,35)")

# Doc lap khong? — dieu kien (1.5)
px, py = marginal_x(J1), marginal_y(J1)
print(f"  p11 = {float(J1[(1, 1)]):.4f}  vs  p1(1).p2(1) ="
      f" {float(px[1] * py[1]):.4f}  ->  doc lap:", is_independent(J1))

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 1.2 (tr. 83) — phân phối có điều kiện
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 1.2 — phan phoi cua X biet Y = 1")
cond = conditional_x_given_y(J1, 1)
for x, p in cond.items():
    print(f"  P(X={x} | Y=1) = ({J1[(x, 1)]}) / ({py[1]}) = {float(p):.2f}")
print("  Tong =", sum(cond.values()))
print(f"  So sanh: P(X=1) = {float(px[1]):.2f} vs P(X=1|Y=1) ="
      f" {float(cond[1]):.2f}  ->  thong tin ve Y DA lam doi phan phoi cua X")

# ─────────────────────────────────────────────────────────────
# 3. Thí dụ 2.1 (tr. 91) — hiệp phương sai và hệ số tương quan
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.1 — hiep phuong sai va he so tuong quan cua bang tren")
print(f"  EX = {float(E(px)):.4f}   VX = {float(V(px)):.4f}   (sach: 1,55 / 0,2475)")
print(f"  EY = {float(E(py)):.4f}   VY = {float(V(py)):.4f}   (sach: 2,20 / 0,66)")
exy = sum(x * y * p for (x, y), p in J1.items())
print(f"  E(XY) = {float(exy):.4f}   (sach: 3,50)")
print(f"  muy_XY = E(XY) - EX.EY = {float(cov(J1)):.4f}   (sach: 0,09)")
print(f"  rho_XY = muy/(sigmaX.sigmaY) = {rho(J1):.4f}   (sach: 0,22)")

# ─────────────────────────────────────────────────────────────
# 4. Thí dụ 2.3 (tr. 93) — kỳ vọng có điều kiện
# ─────────────────────────────────────────────────────────────
print()
J2 = {(2, 1): F(15, 100), (2, 2): F(8, 100), (2, 3): F(27, 100),
      (4, 1): F(10, 100), (4, 2): F(20, 100), (4, 3): F(20, 100)}
assert sum(J2.values()) == 1
print("THI DU 2.3 — ky vong co dieu kien")
cx = conditional_x_given_y(J2, 1)
print("  P(X|Y=1):", {k: float(v) for k, v in cx.items()},
      "-> E(X|Y=1) =", E(cx), "=", float(E(cx)), "  (sach: 2,8)")
# E(Y | X = 4): doi vai tro hai bien
J2T = {(y, x): p for (x, y), p in J2.items()}
cy = conditional_x_given_y(J2T, 4)
print("  P(Y|X=4):", {k: float(v) for k, v in cy.items()},
      "-> E(Y|X=4) =", E(cy), "=", float(E(cy)), "  (sach: 2,2)")

# Tinh chat (iv) tr. 93:  E[E(Y|X)] = EY
inner = {x: E(conditional_x_given_y(J2T, x)) for x in marginal_x(J2)}
outer = sum(marginal_x(J2)[x] * inner[x] for x in inner)
print(f"  Kiem tinh chat (iv) E[E(Y|X)] = EY:"
      f" {outer} = {E(marginal_y(J2))}  ->", outer == E(marginal_y(J2)))

# ─────────────────────────────────────────────────────────────
# 5. ⚠ KHÔNG TƯƠNG QUAN NHƯNG VẪN PHỤ THUỘC — Thí dụ 2.2 (tr. 92)
#    (X,Y) deu tren hinh ellipse 4x^2 + y^2 < 4, f = 1/(2pi)
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.2 — (X,Y) deu tren ellipse 4x^2 + y^2 < 4,  f = 1/(2pi)")


def integrate2d(g, n=1200):
    """Tich phan g(x,y).f(x,y) tren mien ellipse, bang luoi deu."""
    hx, hy = 2 / n, 4 / n
    tot = 0.0
    for i in range(n):
        x = -1 + (i + 0.5) * hx
        for j in range(n):
            y = -2 + (j + 0.5) * hy
            if 4 * x * x + y * y < 4:
                tot += g(x, y) * hx * hy / (2 * math.pi)
    return tot


print(f"  Kiem tinh chat (ii) tong = 1 : {integrate2d(lambda x, y: 1.0):.4f}")
ex_ = integrate2d(lambda x, y: x)
ey_ = integrate2d(lambda x, y: y)
exy_ = integrate2d(lambda x, y: x * y)
print(f"  EX = {ex_:.4f}   EY = {ey_:.4f}   (doi xung -> deu bang 0)")
print(f"  muy_XY = E(XY) - EX.EY = {exy_ - ex_ * ey_:.4f}"
      "   ->  KHONG TUONG QUAN")
# Nhung co doc lap khong? f1(x) = (2/pi)can(1-x^2); f2(y) = can(4-y^2)/(2pi)
x0, y0 = 0.5, 1.0
f_joint = 1 / (2 * math.pi)
f1 = (2 / math.pi) * math.sqrt(1 - x0**2)
f2 = math.sqrt(4 - y0**2) / (2 * math.pi)
print(f"  Tai (x,y) = ({x0}, {y0}):")
print(f"    f(x,y)      = {f_joint:.6f}")
print(f"    f1(x).f2(y) = {f1 * f2:.6f}")
print(f"    Bang nhau? {math.isclose(f_joint, f1 * f2)}  ->  PHU THUOC")
print("  => KHONG TUONG QUAN nhung VAN PHU THUOC. Doc lap MANH hon.")

# ─────────────────────────────────────────────────────────────
# 6. 💼 GÓC QTKD — bảng chéo kênh quảng cáo x mức chi tiêu
# ─────────────────────────────────────────────────────────────
print()
print("💼 GOC QTKD — 1000 khach: so lan mua/nam (X) vs muc chi moi don (Y, trieu)")
J3 = {(1, 1): F(180, 1000), (1, 2): F(120, 1000), (1, 3): F(50, 1000),
      (2, 1): F(120, 1000), (2, 2): F(160, 1000), (2, 3): F(120, 1000),
      (3, 1): F(40, 1000), (3, 2): F(90, 1000), (3, 3): F(120, 1000)}
assert sum(J3.values()) == 1
show(J3, "  Bang cheo (cross-tab) = phan phoi dong thoi:")
print(f"  rho = {rho(J3):.4f}  ->  mua nhieu lan thi cung chi nhieu moi don")
print(f"  E(Y) toan bo         = {float(E(marginal_y(J3))):.4f} trieu")
J3T = {(y, x): p for (x, y), p in J3.items()}
for x in [1, 2, 3]:
    print(f"  E(Y | X={x} lan mua) = {float(E(conditional_x_given_y(J3T, x))):.4f}"
          " trieu")
print("  => Phan khuc theo X cho ba con so KHAC HAN trung binh chung.")
print("     Do la toan bo gia tri cua PHAN PHOI CO DIEU KIEN trong kinh doanh.")
```

Kết quả chạy thật:

```
THI DU 1.1 — phan phoi dong thoi va hai phan phoi BIEN
              1        2        3     p1(x)
  x=1      0.10     0.25     0.10      0.45
  x=2      0.15     0.05     0.35      0.55
p2(y)      0.25     0.30     0.45      1.00
  F(2,3) = tong p_ij voi xi<2, yj<3 = p11 + p12 = 7/20 = 0.35   (sach: 0,35)
  p11 = 0.1000  vs  p1(1).p2(1) = 0.1125  ->  doc lap: False

THI DU 1.2 — phan phoi cua X biet Y = 1
  P(X=1 | Y=1) = (1/10) / (1/4) = 0.40
  P(X=2 | Y=1) = (3/20) / (1/4) = 0.60
  Tong = 1
  So sanh: P(X=1) = 0.45 vs P(X=1|Y=1) = 0.40  ->  thong tin ve Y DA lam doi phan phoi cua X

THI DU 2.1 — hiep phuong sai va he so tuong quan cua bang tren
  EX = 1.5500   VX = 0.2475   (sach: 1,55 / 0,2475)
  EY = 2.2000   VY = 0.6600   (sach: 2,20 / 0,66)
  E(XY) = 3.5000   (sach: 3,50)
  muy_XY = E(XY) - EX.EY = 0.0900   (sach: 0,09)
  rho_XY = muy/(sigmaX.sigmaY) = 0.2227   (sach: 0,22)

THI DU 2.3 — ky vong co dieu kien
  P(X|Y=1): {2: 0.6, 4: 0.4} -> E(X|Y=1) = 14/5 = 2.8   (sach: 2,8)
  P(Y|X=4): {1: 0.2, 2: 0.4, 3: 0.4} -> E(Y|X=4) = 11/5 = 2.2   (sach: 2,2)
  Kiem tinh chat (iv) E[E(Y|X)] = EY: 111/50 = 111/50  -> True

THI DU 2.2 — (X,Y) deu tren ellipse 4x^2 + y^2 < 4,  f = 1/(2pi)
  Kiem tinh chat (ii) tong = 1 : 1.0000
  EX = 0.0000   EY = 0.0000   (doi xung -> deu bang 0)
  muy_XY = E(XY) - EX.EY = 0.0000   ->  KHONG TUONG QUAN
  Tai (x,y) = (0.5, 1.0):
    f(x,y)      = 0.159155
    f1(x).f2(y) = 0.151982
    Bang nhau? False  ->  PHU THUOC
  => KHONG TUONG QUAN nhung VAN PHU THUOC. Doc lap MANH hon.

💼 GOC QTKD — 1000 khach: so lan mua/nam (X) vs muc chi moi don (Y, trieu)
  Bang cheo (cross-tab) = phan phoi dong thoi:
              1        2        3     p1(x)
  x=1      0.18     0.12     0.05      0.35
  x=2      0.12     0.16     0.12      0.40
  x=3      0.04     0.09     0.12      0.25
p2(y)      0.34     0.37     0.29      1.00
  rho = 0.3369  ->  mua nhieu lan thi cung chi nhieu moi don
  E(Y) toan bo         = 1.9500 trieu
  E(Y | X=1 lan mua) = 1.6286 trieu
  E(Y | X=2 lan mua) = 2.0000 trieu
  E(Y | X=3 lan mua) = 2.3200 trieu
  => Phan khuc theo X cho ba con so KHAC HAN trung binh chung.
     Do la toan bo gia tri cua PHAN PHOI CO DIEU KIEN trong kinh doanh.
```

Bốn điểm đáng để ý:

1. **`doc lap: False`** — hàm `is_independent` kiểm cả 6 ô, chỉ cần một ô sai là trả về `False`.
   Đúng như (1.5) đòi hỏi "với mọi cặp".
2. **Thí dụ 2.2 chạy bằng tích phân số**: `muy_XY = 0.0000` nhưng `Bang nhau? False`.
   Hai dòng này cạnh nhau chính là **toàn bộ nội dung mục 5** — không tương quan mà vẫn phụ thuộc.
3. **Kiểm tính chất (iv)**: `111/50 = 111/50 -> True`. Dùng `Fraction` nên so sánh bằng `==` an toàn;
   với số thực phải dùng `math.isclose` (như dòng kiểm độc lập ở thí dụ 2.2).
4. **Góc QTKD**: trung bình chung 1,95 triệu, nhưng ba phân khúc cho 1,63 / 2,00 / 2,32.
   Chênh nhau 42% giữa phân khúc thấp nhất và cao nhất. **Con số trung bình chung không mô tả đúng
   nhóm khách hàng nào cả.**

---

## 11. Tự thử

1. Sửa bảng `J1` để hai biến **độc lập**: đặt $p_{ij} = p_1(x_i)p_2(y_j)$ với chính hai phân phối
   biên hiện có. Chạy lại — `is_independent` có trả về `True` không? $\rho$ bằng bao nhiêu?
2. Trong bảng độc lập vừa tạo, so `conditional_x_given_y(J, 1)` với `marginal_x(J)`.
   Chúng có giống nhau không? Giải thích bằng tính chất (iii) ở mục 7.
3. Tạo một bảng có $\rho = -1$ (tương quan âm hoàn hảo): chỉ 3 ô khác 0, nằm trên một đường thẳng
   đi xuống. Kiểm $|\rho| = 1$.
4. Kiểm **nghịch lý Simpson** bằng số: dựng hai bảng con, mỗi bảng có $\rho > 0$, nhưng khi gộp lại
   (cộng hai bảng rồi chia đôi) thì $\rho < 0$. Gợi ý: hai nhóm có $EX$, $EY$ rất khác nhau.
5. Ở Góc QTKD, tính thêm `V(conditional...)` cho từng phân khúc. Phân khúc nào có độ phân tán lớn
   nhất? Con số đó nói gì về việc dự báo doanh thu cho phân khúc đó?
6. Viết hàm tính $E(Y \mid X = x)$ cho phân phối chuẩn hai chiều theo công thức ở mục 8,
   rồi kiểm với ví dụ quảng cáo (ra 572 triệu không?). Thêm hàm tính khoảng $\pm 2\sigma$.
7. Trong thí dụ 2.2, đổi miền từ elip sang **hình vuông** $|x| < 1$, $|y| < 2$ với $f = 1/8$.
   Giờ $X$, $Y$ có độc lập không? So sánh với trường hợp elip và giải thích sự khác biệt.

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)                       | Tiếng Anh                           | Ghi chú                       |
| --------------------------------------------- | ----------------------------------- | ----------------------------- |
| Véctơ ngẫu nhiên, biến ngẫu nhiên nhiều chiều | Random vector                       |                               |
| Hàm phân phối đồng thời                       | Joint distribution function         | $F(x,y)$                      |
| Hàm mật độ đồng thời                          | Joint density function              | $f(x,y)$                      |
| Mặt phân phối xác suất                        | Probability surface                 | đồ thị của $f(x,y)$           |
| Phân phối biên                                | Marginal distribution               | tổng hàng / tổng cột          |
| Phân phối có điều kiện                        | Conditional distribution            | chuẩn hoá một hàng/cột        |
| Hiệp phương sai                               | Covariance                          | $\mu_{XY}$, $\text{Cov}(X,Y)$ |
| Ma trận hiệp phương sai                       | Covariance matrix                   | $\Gamma$                      |
| Hệ số tương quan                              | Correlation coefficient             | $\rho_{XY}$                   |
| Không tương quan                              | Uncorrelated                        | $\rho = 0$                    |
| Kỳ vọng có điều kiện                          | Conditional expectation             | $E(Y \mid X)$                 |
| Hàm hồi quy                                   | Regression function                 | $E(Y \mid X = x)$             |
| Đường hồi quy                                 | Regression curve/line               | đồ thị hàm hồi quy            |
| Luật kỳ vọng lặp                              | Law of iterated expectation         | $E[E(Y\mid X)] = EY$          |
| Phân phối chuẩn hai chiều                     | Bivariate normal distribution       | (2.4)                         |
| Phương sai thuần nhất                         | Homoscedasticity                    | 📚 mục 8                       |
| Nghịch lý Simpson                             | Simpson's paradox                   | 📚 mục 9                       |
| Biến ẩn, biến gây nhiễu                       | Confounding variable                | 📚 mục 9                       |
| Bảng chéo                                     | Cross-tabulation, contingency table | 💼 mục 2                       |

---

## 13. Câu hỏi tự kiểm tra

1. Vì sao hai phân phối biên **không đủ** để xác định phân phối đồng thời? Cho hai bảng khác nhau
   có cùng phân phối biên.
2. Nếu $X$, $Y$ độc lập thì bảng phân phối có điều kiện của $X$ biết $Y = y$ trông thế nào so với
   phân phối biên của $X$? Chứng minh.
3. Nêu quan hệ đúng giữa ba khái niệm: **độc lập**, **không tương quan**, **$\rho = 0$**.
   Trường hợp nào chúng trùng nhau?
4. $\rho_{XY} = 0{,}85$ giữa "số nhân viên bán hàng" và "doanh thu chi nhánh".
   Nêu bốn cách giải thích khác nhau cho con số này (gợi ý: mục 9 ý 2).
5. Cho $\rho = 0{,}5$. Biết $X$ giúp giảm bao nhiêu phần trăm bất định về $Y$?
   Còn $\rho = 0{,}9$? Nhận xét về quan hệ giữa $\rho$ và $\rho^2$.
6. Bài 4 (tr. 110): bảng phân phối đồng thời của số lỗi vẽ màu $X$ và số lỗi đúc $Y$.
   a) Hai biến có độc lập không? b) $P(X + Y > 4)$? c) Biết có 2 lỗi vẽ màu, xác suất không có
   lỗi đúc là bao nhiêu?
7. Vì sao trong hồi quy tuyến tính người ta luôn cần giả thiết "phương sai thuần nhất"?
   Nó đến từ đâu trong thí dụ 2.4?
8. Một báo cáo nói: *"tương quan giữa thời gian đào tạo và hiệu suất là $-0{,}3$, vậy nên cắt
   ngân sách đào tạo."* Nêu ít nhất ba lý do kết luận này có thể sai.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 8 — BIẾN NGẪU NHIÊN HAI CHIỀU              (Ch. III §1–2, tr.79–96) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BỘ BA PHÂN PHỐI — ba góc nhìn vào MỘT bảng số                           ║
║  ┌──────────────┬──────────────────────┬──────────────────────────┐      ║
║  │ ĐỒNG THỜI    │ p(xᵢ, yⱼ)            │ ô trong bảng             │      ║
║  │ BIÊN         │ p₁(x) = Σⱼ pᵢⱼ       │ tổng HÀNG / tổng CỘT     │      ║
║  │ CÓ ĐIỀU KIỆN │ p(x|y) = pᵢⱼ / p₂(y) │ 1 cột, chuẩn hoá về 1    │      ║
║  └──────────────┴──────────────────────┴──────────────────────────┘      ║
║      ⚠ ĐỒNG THỜI → BIÊN: luôn được                                       ║
║        BIÊN → ĐỒNG THỜI: CHỈ khi độc lập                                 ║
║                                                                          ║
║  ĐỘC LẬP   F(x,y) = F₁(x)F₂(y)   ⟺  pᵢⱼ = p₁(xᵢ)p₂(yⱼ)  MỌI cặp         ║
║            liên tục:  f(x,y) = f₁(x)f₂(y)                                ║
║                                                                          ║
║  ── ĐO QUAN HỆ ────────────────────────────────────────────────────      ║
║  HIỆP PHƯƠNG SAI   μ_XY = E(XY) − EX·EY                                  ║
║      μ > 0 đồng biến | μ < 0 nghịch biến | μ = 0 không tương quan        ║
║      VX là trường hợp riêng khi X = Y                                    ║
║      nhược: không biết miền biến thiên, sai đơn vị đo                    ║
║                                                                          ║
║  HỆ SỐ TƯƠNG QUAN   ρ_XY = μ_XY / (σ_X · σ_Y)      |ρ| ≤ 1               ║
║      ρ = ±1 → Y = aX + b (tuyến tính hoàn hảo)                           ║
║      ρ = 0  → không tương quan                                           ║
║                                                                          ║
║  ⚠⚠ QUAN HỆ BA KHÁI NIỆM                                                 ║
║      ĐỘC LẬP  ⟹  KHÔNG TƯƠNG QUAN                                       ║
║      chiều ngược lại SAI  (thí dụ 2.2: elip, ρ=0 mà vẫn phụ thuộc)       ║
║      NGOẠI LỆ DUY NHẤT: phân phối CHUẨN hai chiều thì ρ=0 ⟺ độc lập     ║
║                                                                          ║
║  ── KỲ VỌNG CÓ ĐIỀU KIỆN ──────────────────────────────────────────      ║
║     E(Y|X = x)  = HÀM HỒI QUY  ← cả chương VI dựng trên đây              ║
║  ⭐ E[E(Y|X)] = EY   luật kỳ vọng lặp                                    ║
║      (kiểm báo cáo phân khúc: trung bình có trọng số = trung bình chung) ║
║                                                                          ║
║  CHUẨN HAI CHIỀU — ba kết quả nền của hồi quy                            ║
║      E(Y|X=x) = a_Y + ρ(σ_Y/σ_X)(x − a_X)   ← ĐƯỜNG THẲNG                ║
║      V(Y|X=x) = σ_Y²(1 − ρ²)                ← không phụ thuộc x          ║
║      ⭐ ρ² = TỶ LỆ BẤT ĐỊNH GIẢI THÍCH ĐƯỢC = R² ở bài 14                ║
║                                                                          ║
║  📚 BỐN ĐIỀU ρ KHÔNG NÓI                                                 ║
║      1. quan hệ PHI TUYẾN (chữ U → ρ ≈ 0 dù rất phụ thuộc)               ║
║      2. NHÂN QUẢ (X→Y? Y→X? Z→cả hai? trùng hợp?)                        ║
║      3. bị GIÁ TRỊ THÁI QUÁ chi phối                                     ║
║      4. NGHỊCH LÝ SIMPSON (từng nhóm ρ>0, gộp lại ρ<0)                   ║
║      ⟹ LUÔN VẼ BIỂU ĐỒ PHÂN TÁN TRƯỚC KHI TÍNH ρ                        ║
║                                                                          ║
║  💼 QTKD  bảng chéo Excel = phân phối đồng thời                          ║
║          phân khúc khách hàng = phân phối CÓ ĐIỀU KIỆN                   ║
║          X,Y độc lập ⟹ phân khúc theo X là VÔ NGHĨA                     ║
║          dự báo phải kèm khoảng: E(Y|X) ± 2σ_Y√(1−ρ²)                    ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương III §1–§2, tr. 79–96.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Mục 9 (bốn cảnh báo về $\rho$), thang đọc $\rho$ ở mục 6, và cách diễn giải $\rho^2$ ở mục 8:
  kiến thức bổ sung, không có trong giáo trình.
- Nghịch lý Simpson: bổ sung; giáo trình không nhắc tới.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 7 — Các phân phối thông dụng](bai_07_cac_phan_phoi_thong_dung.md) ·
Bài sau: Bài 9 — Hàm của biến ngẫu nhiên, luật số lớn và định lý giới hạn trung tâm
