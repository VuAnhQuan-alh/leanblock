# Bài 7 — Các phân phối thông dụng

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương II §4**, tr. 56–78.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Mục 8 nêu **một chỗ thiếu nhất quán** trong thí dụ 4.5 của giáo trình (tr. 69).
> 📌 **Cần đọc trước:** [Bài 5](bai_05_bien_ngau_nhien_va_luat_phan_phoi.md) · [Bài 6](bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md)

Bài 5 và 6 dạy **cách mô tả** một biến ngẫu nhiên bất kỳ. Bài này đưa ra **danh mục các mẫu có sẵn**:
khoảng một chục phân phối bao phủ gần hết các tình huống thực tế.

Học bài này không phải học thuộc công thức, mà là học **nhận diện**: nhìn một bài toán và biết ngay
nó thuộc mẫu nào. Nhận diện đúng thì công thức tra bảng là xong.

Đây cũng là **bài dài nhất Chương II** và là bản lề: bốn phân phối cuối (chuẩn, $\chi^2$, Student,
Fisher) là toàn bộ công cụ của phần thống kê từ bài 11 trở đi.

## Mục lục

1. [Phân phối đều](#1-phân-phối-đều)
2. [Bernoulli và nhị thức](#2-bernoulli-và-nhị-thức)
3. [Phân phối Poisson](#3-phân-phối-poisson)
4. [Siêu bội, hình học, nhị thức âm](#4-siêu-bội-hình-học-nhị-thức-âm)
5. [Phân phối chuẩn](#5-phân-phối-chuẩn)
6. [Quy chuẩn và cách tra bảng](#6-quy-chuẩn-và-cách-tra-bảng)
7. [Xấp xỉ nhị thức bằng chuẩn](#7-xấp-xỉ-nhị-thức-bằng-chuẩn)
8. [Bốn phân phối của phần thống kê](#8-bốn-phân-phối-của-phần-thống-kê)
9. [📚 Cây quyết định chọn phân phối](#9--cây-quyết-định-chọn-phân-phối)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Phân phối đều

### Đều rời rạc

**Định nghĩa 1 (tr. 56).** $X \sim \mathcal{U}(n)$ nếu bảng phân phối là

| $x$    | 1         | 2         | $\cdots$ | $n$       |
| ------ | --------- | --------- | -------- | --------- |
| $p(x)$ | $\frac1n$ | $\frac1n$ | $\cdots$ | $\frac1n$ |

tức $p(i) = \dfrac1n$ với $i = \overline{1,n}$ (4.1). Mở rộng được cho tập hữu hạn bất kỳ
$\{x_1, \dots, x_n\}$.

$$EX = \frac{n+1}{2}, \qquad VX = \frac{n^2 - 1}{12}$$

### Đều liên tục

**Định nghĩa 2 (tr. 57).** $X \sim \mathcal{U}([a;b])$ nếu

$$f(x) = \begin{cases} \dfrac{1}{b-a}, & x \in [a; b] \\[6pt] 0, & x \notin [a; b] \end{cases} \tag{4.2}$$

$$EX = \frac{a+b}{2}, \qquad VX = \frac{(b-a)^2}{12}$$

⚠️ Chú ý $f(x) = \frac{1}{b-a}$ **có thể lớn hơn 1** — nếu $b - a < 1$. Đúng như cảnh báo ở bài 5
mục 6: mật độ không phải xác suất.

Giáo trình nhấn mạnh (tr. 57): *"Phân phối đều $\mathcal{U}([0;1])$ có vai trò **rất quan trọng**
trong mô phỏng các số ngẫu nhiên."* Đó chính là hàm `random.random()` bạn dùng ở bài 2 — mọi số
ngẫu nhiên khác đều sinh ra từ nó qua các phép biến đổi.

### 💼 Góc QTKD

Phân phối đều là **giả định mặc định khi bạn không biết gì** ngoài khoảng giá trị:

- Ước tính thời gian hoàn thành dự án: "từ 3 đến 5 tháng" mà không có thông tin gì thêm
  → $\mathcal{U}([3;5])$, kỳ vọng 4 tháng.
- Bốc thăm, quay số trúng thưởng, chọn mẫu ngẫu nhiên → đều rời rạc.
- Thời điểm khách đến trong khung giờ mở cửa (bài 2 mục 4) → đều liên tục.

⚠️ Nhưng đây là **giả định yếu nhất trong danh mục**. Trong quản trị dự án, người ta thường dùng
**phân phối tam giác** (thêm giá trị "khả năng cao nhất") hoặc **PERT** thay cho đều — vì thực tế
hiếm khi mọi giá trị đồng khả năng.

---

## 2. Bernoulli và nhị thức

### Phân phối Bernoulli

**Định nghĩa 3 (tr. 57).** $X \sim B(p)$ nếu

$$p(x) = p^x q^{1-x}, \qquad x = 0 \text{ và } 1 \tag{4.3}$$

| $x$    | 0   | 1   |
| ------ | --- | --- |
| $p(x)$ | $q$ | $p$ |

$$EX = 0 \cdot q + 1 \cdot p = p, \qquad VX = E(X^2) - (EX)^2 = p - p^2 = pq$$

*"Mọi phép thử chỉ có hai kết cục đều có thể mô hình hoá bằng phân phối này"* (tr. 58).

Giáo trình nhận xét thẳng: *"Trong thực tế phân phối Bernoulli **ít được sử dụng** (có thể do nó
quá đơn giản), tuy nhiên nó được dùng làm **cơ sở** để tìm luật phân phối của các biến ngẫu nhiên khác."*

Nó là **viên gạch**, không phải bức tường.

### Phân phối nhị thức

**Định nghĩa 4 (tr. 58).** $X \sim B(n, p)$ nếu

$$p(x) = P_n(x) = C_n^x p^x q^{n-x}, \qquad x = \overline{0, n} \tag{4.4}$$

Đây chính là công thức Bernoulli ở bài 3 (3.10), giờ được đặt tên chính thức.
Bernoulli là trường hợp riêng khi $n = 1$.

**Ba điều kiện bắt buộc (tr. 59)** — thiếu một là dùng sai:

1. Dãy các phép thử **giống nhau, độc lập**.
2. Trong mỗi phép thử chỉ có **2 kết cục** (có và không).
3. Hai tham số hằng xác định: **số phép thử $n$** và **xác suất $p$**.

**Kỳ vọng và phương sai** — giáo trình dẫn rất đẹp (tr. 59–60). Gọi $X_i$ = số lần xuất hiện $A$
trong phép thử thứ $i$; mỗi $X_i \sim B(p)$ với $EX_i = p$, $VX_i = pq$. Vì $X = X_1 + \cdots + X_n$
và các $X_i$ độc lập:

$$EX = \sum_{i=1}^n EX_i = np, \qquad VX = \sum_{i=1}^n VX_i = npq$$

**Đây là cách dùng tính chất của kỳ vọng/phương sai (bài 6) để né hoàn toàn việc tính tổng
$\sum x C_n^x p^x q^{n-x}$** — một tổng rất khó. Kỹ thuật "tách thành tổng các biến đơn giản"
này dùng lại nhiều lần về sau.

**Hai kết quả bổ sung (tr. 60):**

$$
\begin{aligned}
&\text{(i)} && X \sim B(n, p) \Rightarrow Y = n - X \sim B(n, 1-p) \\
&\text{(ii)} && X_1 \sim B(n_1, p),\ X_2 \sim B(n_2, p) \Rightarrow X_1 + X_2 \sim B(n_1+n_2, p)
\end{aligned}
$$

(ii) gọi là **tính cộng được**: gộp hai đợt kiểm tra cùng tỷ lệ lỗi thì vẫn là nhị thức.
Chú ý điều kiện **cùng $p$** — gộp hai nhà cung cấp có tỷ lệ lỗi khác nhau thì **không** ra nhị thức.

### Thí dụ 4.1 (tr. 59)

> $X \sim B(5; 0{,}25)$. Lập bảng phân phối, rồi tính: a) $P(X > 3)$; b) $P(X \ge 1)$; c) $P(X < 4)$.

| $x$    | 0      | 1          | 2      | 3      | 4      | 5      |
| ------ | ------ | ---------- | ------ | ------ | ------ | ------ |
| $p(x)$ | 0,2373 | **0,3955** | 0,2637 | 0,0879 | 0,0146 | 0,0010 |

- a) $P(X > 3) = p(4) + p(5) = \mathbf{0{,}0156}$
- b) $P(X \ge 1) = 1 - p(0) = \mathbf{0{,}7627}$
- c) $P(X < 4) = 1 - p(5) - p(4) = \mathbf{0{,}9990}$

Giáo trình chỉ ra $x = 1$ có xác suất lớn nhất, vậy **mốt của $X$ bằng 1**, và trong ứng dụng người ta
gọi là **"số lần xuất hiện chắc chắn nhất"**.

⚠️ Chú ý mốt $= 1$ trong khi $EX = np = 1{,}25$ — không trùng nhau, vì phân phối này lệch phải
($p < 0{,}5$). Đúng như bài 6 mục 5 dự đoán.

### 💼 Góc QTKD — phân phối được dùng nhiều thứ hai

| Bài toán                                        | $n$ | $p$              |
| ----------------------------------------------- | --- | ---------------- |
| Trong 100 khách vào shop, bao nhiêu người mua?  | 100 | tỷ lệ chuyển đổi |
| Trong 50 email gửi đi, bao nhiêu email được mở? | 50  | open rate        |
| Trong 200 sản phẩm, bao nhiêu cái lỗi?          | 200 | tỷ lệ lỗi        |
| Trong 30 khách hàng, bao nhiêu người gia hạn?   | 30  | tỷ lệ gia hạn    |

⚠️ **Điều kiện hay bị vi phạm nhất là "độc lập"**: nếu 100 khách vào shop trong cùng một chương trình
khuyến mại thì họ **không** độc lập — cùng chịu một cú hích chung. Khi đó phương sai thực tế
**lớn hơn** $npq$, và mọi ước lượng rủi ro dựa trên nhị thức đều lạc quan quá mức.

---

## 3. Phân phối Poisson

**Định nghĩa 5 (tr. 60).** $X \sim P(\lambda)$ nếu

$$p(x) = \frac{e^{-\lambda}\lambda^x}{x!}, \qquad x = 0, 1, 2, \dots \tag{4.5}$$

Chú ý $X$ nhận **vô hạn** giá trị — nhưng vẫn đếm được, nên vẫn rời rạc (bài 5 mục 2).

**Ứng dụng (tr. 60):** *"Phân phối Poisson có nhiều ứng dụng trong **lý thuyết phục vụ đám đông**,
**kiểm tra chất lượng sản phẩm**... Chẳng hạn số cuộc gọi điện thoại của một tổng đài trong 1 ngày,
số lượng khách hàng của một nhà băng trong 1 giờ..."*

**Quan hệ với nhị thức (tr. 60).** Khi $n \to +\infty$, $p \to 0$ sao cho $np \to \lambda$ = hằng số:

$$C_n^x p^x (1-p)^{n-x} \ \longrightarrow \ \frac{e^{-\lambda}\lambda^x}{x!}$$

Đây chính là xấp xỉ Poisson (3.12) ở bài 3, giờ được phát biểu như một **định lý giới hạn**.
Vì thế Poisson còn được gọi là **"luật của các sự kiện hiếm"**.

**Kỳ vọng và phương sai** — đặc điểm nổi bật nhất:

$$\boxed{EX = VX = \lambda}$$

⚠️ **Đây là dấu hiệu nhận biết Poisson trên dữ liệu thật.** Nếu bạn có dữ liệu đếm (số khiếu nại/ngày,
số lỗi/lô) và thấy **trung bình mẫu ≈ phương sai mẫu**, rất có thể nó là Poisson. Nếu phương sai
**lớn hơn hẳn** trung bình (gọi là *quá phân tán*, overdispersion), Poisson **không** phù hợp —
thường là do dữ liệu bị vón cục (khiếu nại đến theo đợt sau một sự cố).

**Mốt (tr. 61).** $\lambda - 1 \le \text{mốt} \le \lambda$:

- $\lambda$ **nguyên** → có **2 mốt** là $\lambda$ và $\lambda - 1$;
- $\lambda$ **không nguyên** → mốt là giá trị nguyên nằm giữa $\lambda - 1$ và $\lambda$.

### Thí dụ 4.2 (tr. 61)

> Vận chuyển 5000 chai rượu vào kho, xác suất vỡ mỗi chai là 0,0004. Tính xác suất có **không quá
> 1 chai** bị vỡ.

*Giải.* $n = 5000$ **rất lớn**, $p = 0{,}0004$ **quá bé** → dùng Poisson với $\lambda = np = 2$:

$$P(0 \le X \le 1) = \frac{e^{-2} \cdot 2^0}{0!} + \frac{e^{-2} \cdot 2^1}{1!} = \frac{3}{e^2} \approx \mathbf{0{,}406}$$

Giá trị nhị thức đúng là $0{,}40597$ — lệch $0{,}000054$. Xấp xỉ gần như hoàn hảo.

Vì $\lambda = 2$ nguyên nên có **hai mốt**: 1 và 2, mỗi cái xác suất $0{,}2707$.
Đó là số chai có khả năng vỡ nhiều nhất.

### 💼 Góc QTKD — phân phối của "chuyện hiếm nhưng vẫn xảy ra"

| Bài toán                              | $\lambda$                  |
| ------------------------------------- | -------------------------- |
| Số khách vào cửa hàng trong 1 giờ     | lượng khách trung bình/giờ |
| Số cuộc gọi vào tổng đài trong 5 phút | trung bình/5 phút          |
| Số khiếu nại trong 1 tháng            | trung bình/tháng           |
| Số lỗi trong 1 lô hàng lớn            | $n \times$ tỷ lệ lỗi       |
| Số tai nạn lao động trong 1 quý       | trung bình/quý             |

**Ứng dụng lớn nhất: bài toán xếp hàng và bố trí nhân sự.** Nếu trung bình 6 khách/giờ ($\lambda = 6$),
xác suất có hơn 10 khách trong một giờ nào đó là $1 - P(X \le 10) \approx 4{,}3\%$ — nghĩa là cứ
khoảng 23 giờ làm việc lại có một giờ quá tải nếu bạn chỉ bố trí nhân sự phục vụ 10 khách/giờ.

⚠️ **Quy tắc cộng của Poisson:** nếu $X_1 \sim P(\lambda_1)$, $X_2 \sim P(\lambda_2)$ độc lập thì
$X_1 + X_2 \sim P(\lambda_1 + \lambda_2)$. Nhờ vậy bạn **đổi được đơn vị thời gian tự do**:
trung bình 6 khách/giờ → 1 khách/10 phút → 48 khách/ngày 8 tiếng. Chỉ cần nhân $\lambda$.

---

## 4. Siêu bội, hình học, nhị thức âm

### Siêu bội — khi lấy mẫu KHÔNG hoàn lại

Giáo trình mở đầu bằng đúng chỗ nhị thức hỏng (tr. 61):

> "Một trong các giả thiết của phân phối nhị thức là **sự độc lập** của các phép thử... Một trường hợp
> cổ điển là việc **chọn mẫu không hoàn lại**, trong đó xác suất **không còn là hằng số** nữa."

Có $N$ sản phẩm trong đó $M$ phế phẩm; chọn **không hoàn lại** $n$ sản phẩm. Theo định nghĩa cổ điển
(bài 2), xác suất có đúng $x$ phế phẩm:

**Định nghĩa 6 (tr. 62).** $X \sim H(N, n, p)$ với $p = M/N$:

$$p(x) = \frac{C_M^x \, C_{N-M}^{n-x}}{C_N^n}, \qquad x = 0, 1, \dots, n \tag{4.6}$$

Đọc công thức: chọn $x$ phế phẩm từ $M$ cái phế × chọn $n-x$ chính phẩm từ $N-M$ cái tốt,
chia cho tổng số cách chọn $n$ từ $N$.

$$EX = np, \qquad VX = npq\,\frac{N-n}{N-1}$$

Chú ý: **kỳ vọng giống hệt nhị thức**, chỉ phương sai khác — nhân thêm thừa số
$\dfrac{N-n}{N-1} < 1$, gọi là **hệ số hiệu chỉnh tổng thể hữu hạn**. Lấy mẫu không hoàn lại
luôn **ít phân tán hơn** lấy có hoàn lại.

### ⚠️ Điều kiện xấp xỉ: $N > 10n$

**Thí dụ 4.3 (tr. 62).** Hộp 15 bóng có 5 bóng kém. Chọn ngẫu nhiên 10 bóng (không hoàn lại).

| $x$                 |       0 |       1 |       2 |           3 |       4 |       5 |
| ------------------- | ------: | ------: | ------: | ----------: | ------: | ------: |
| **Siêu bội** (đúng) | 0,00033 | 0,01665 | 0,14985 | **0,39960** | 0,34965 | 0,08392 |
| Nhị thức (xấp xỉ)   | 0,01734 | 0,08671 | 0,19509 |     0,26012 | 0,22761 | 0,13656 |
| Sai lệch            |   0,017 |   0,070 |   0,045 |   **0,139** |   0,122 |   0,053 |

Giáo trình kết luận (tr. 63): *"Trong trường hợp này ta **không thể** xấp xỉ các xác suất bằng phân
phối nhị thức được... Trong thực hành khi $N > 10n$ người ta mới chấp nhận xấp xỉ bằng phân phối
nhị thức."*

Ở đây $N = 15$ trong khi $10n = 100$ — vi phạm nặng. Sai lệch tới **0,139**.

💼 **Đây là quy tắc quan trọng nhất cho lấy mẫu QC:** kiểm 50 sản phẩm từ lô 1.000 ($N = 1000 > 500$) →
dùng nhị thức thoải mái. Kiểm 50 sản phẩm từ lô 100 → **bắt buộc dùng siêu bội**.

### Hình học — đếm số lần thất bại trước lần thành công đầu tiên

**Định nghĩa 7 (tr. 63).** $X \sim G(p)$ nếu

$$p(x) = p(1-p)^x, \qquad x = 0, 1, 2, \dots \tag{4.7}$$

$X$ là **số lần không xuất hiện trước lần xuất hiện đầu tiên** của $A$.

$$EX = \frac{q}{p}, \qquad VX = \frac{q}{p^2}$$

⚠️ **Chú ý quy ước.** Giáo trình đếm **số lần thất bại** ($x$ bắt đầu từ 0). Nhiều sách khác đếm
**số lần thử** ($x$ bắt đầu từ 1), khi đó $EX = 1/p$. Chênh nhau đúng 1. Khi làm bài, đọc kỹ đề
hỏi "số lần thất bại" hay "số lần thử".

### Nhị thức âm

**Định nghĩa 8 (tr. 64).** $X \sim NB(r, p)$ — số lần **không** xuất hiện trước lần xuất hiện **thứ $r$**:

$$p(x) = C_{x+r-1}^{x}\, p^r (1-p)^x, \qquad x = 0, 1, 2, \dots \tag{4.8}$$

$$EX = \frac{rq}{p}, \qquad VX = \frac{rq}{p^2}$$

Hình học là trường hợp riêng khi $r = 1$.

### Sơ đồ quan hệ giữa các phân phối rời rạc

Giáo trình vẽ sơ đồ này (tr. 64) nhưng bản quét mờ. Dựng lại:

```
                        PHÉP THỬ BERNOULLI  B(p)
                     (một lần thử, 2 kết cục)
                                │
              ┌─────────────────┼───────────────────┐
              │                 │                   │
    lặp n lần CỐ ĐỊNH,   lặp đến khi        lấy mẫu KHÔNG
    đếm số thành công    thành công r lần,   hoàn lại từ N
              │          đếm số thất bại            │
              ▼                 ▼                   ▼
        NHỊ THỨC B(n,p)   NHỊ THỨC ÂM NB(r,p)  SIÊU BỘI H(N,n,p)
              │                 │                   │
              │  n → ∞, p → 0   │  r = 1            │  N > 10n
              │  np = λ         ▼                   │  (xấp xỉ)
              ▼            HÌNH HỌC G(p)            │
        POISSON P(λ)                                │
              ▲                                     │
              └─────────────────────────────────────┘
                       (N rất lớn, p rất nhỏ)
```

**Đọc sơ đồ:** mọi phân phối rời rạc trong chương trình đều sinh ra từ **một** phép thử Bernoulli,
khác nhau ở **cách lặp** và **cái được đếm**.

### 💼 Góc QTKD

| Phân phối       | Câu hỏi kinh doanh                                        |
| --------------- | --------------------------------------------------------- |
| **Nhị thức**    | "Gọi 50 cuộc, chốt được mấy đơn?"                         |
| **Hình học**    | "Phải gọi bao nhiêu cuộc mới chốt được đơn đầu tiên?"     |
| **Nhị thức âm** | "Phải gọi bao nhiêu cuộc để đủ chỉ tiêu 5 đơn?"           |
| **Siêu bội**    | "Lô 100 sản phẩm có 8 lỗi, kiểm 20 cái bắt được mấy lỗi?" |
| **Poisson**    | "Giờ tới có bao nhiêu khách vào?"                         |

**Hình học trả lời câu hỏi chi phí thu hút khách hàng (CAC).** Tỷ lệ chốt $p = 0{,}1$ →
$EX = q/p = 9$ lần thất bại, tức trung bình **10 cuộc gọi mỗi đơn**. Nếu mỗi cuộc tốn 15 phút thì
CAC theo thời gian là 2,5 giờ/đơn. Đó là con số để so với biên lợi nhuận.

---

## 5. Phân phối chuẩn

Giáo trình mở đầu (tr. 65): *"Đây là phân phối liên tục **quan trọng và có ứng dụng rộng rãi nhất**,
còn có tên gọi là **phân phối Gauss**."*

**Định nghĩa 9 (tr. 65).** $X \sim N(a, \sigma^2)$ nếu

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-a)^2}{2\sigma^2}}, \qquad x \in \mathbb{R} \tag{4.9}$$

Hai tham số $a$ và $\sigma^2$ **chính là** $EX$ và $VX$; $\sigma$ là độ lệch chuẩn.

⚠️ **Ký hiệu.** Giáo trình dùng $a$ cho kỳ vọng; sách quốc tế dùng $\mu$. Cùng một thứ.
Cũng chú ý viết $N(a, \sigma^2)$ — tham số thứ hai là **phương sai**, không phải độ lệch chuẩn.
(Python `NormalDist(mu, sigma)` nhận **độ lệch chuẩn** — dễ nhầm.)

**Ba tính chất từ đồ thị hình chuông (tr. 65):**

- $f(x)$ **đối xứng** qua $EX = a$ → $\text{med}X = a$;
- $f(x)$ đạt max tại $x = a$ → **mốt** $X = a$;
- vậy **kỳ vọng = trung vị = mốt = $a$** — đúng như bài 6 mục 5 nói về phân phối đối xứng một mốt.

**Ảnh hưởng của $\sigma$ (tr. 66):** *"Nếu $\sigma$ càng lớn $f(x)$ phân tán nhiều hơn, đỉnh đồ thị
càng thấp và tù hơn, đường cong tiệm cận tới trục hoành chậm hơn"* — vì tổng diện tích luôn bằng 1,
bè ngang ra thì phải thấp xuống.

```
   f(x)
     │        ╱╲             σ nhỏ: cao, hẹp
     │       ╱  ╲
     │      │    │
     │    ╭─┘    └─╮         σ lớn: thấp, bè
     │  ╭─┘        └─╮
     │╭─┘            └─╮
     └─────────┬─────────► x
               a
        EX = med = mốt = a
```

### ⭐ Quy tắc 3 sigma (4.10)

$$
\begin{aligned}
P(|X - a| < \sigma) &= 68{,}26\% \\
P(|X - a| < 2\sigma) &= 95{,}44\% \\
P(|X - a| < 3\sigma) &= 99{,}74\%
\end{aligned}
\tag{4.10}
$$

Giáo trình gọi đây là **quy tắc $3\sigma$**, *"rất quen thuộc trong các tính toán kỹ thuật"*:
hầu như chắc chắn $X$ nhận giá trị trong lân cận $3\sigma$ của kỳ vọng.

**Ba con số này phải thuộc lòng.** Chúng cho phép ước lượng xác suất trong đầu mà không cần tra bảng.

### Thí dụ 4.4 (tr. 66)

> Độ dài chi tiết máy $X \sim N(20; 0{,}5^2)$ (cm). Tính xác suất độ dài:
> a) lớn hơn 20cm; b) bé hơn 19,5cm; c) lớn hơn 21,5cm.

*Giải.*

**a)** Phân phối đối xứng qua kỳ vọng nên $P(X > 20) = \mathbf{0{,}5}$.

**b)** $19{,}5 = 20 - 1\sigma$. Theo quy tắc $1\sigma$, $P(19{,}5 < X < 20{,}5) = 68{,}26\%$,
nên ngoài khoảng đó là $31{,}74\%$. Do đối xứng, chia đôi:

$$P(X < 19{,}5) = \frac{31{,}74\%}{2} = \mathbf{15{,}87\%}$$

**c)** $21{,}5 = 20 + 3\sigma$. Theo quy tắc $3\sigma$:

$$P(X > 21{,}5) = \frac{1 - 99{,}74\%}{2} = \mathbf{0{,}13\%}$$

Giáo trình bình luận: *"xác suất không đáng kể"*.

**Kỹ thuật cần nhớ:** khi mốc rơi đúng vào $\pm 1\sigma, \pm 2\sigma, \pm 3\sigma$, dùng quy tắc
$3\sigma$ + tính đối xứng là ra ngay, **không cần tra bảng**.

### 💼 Góc QTKD — vì sao chuẩn ở khắp nơi

Phân phối chuẩn xuất hiện tự nhiên khi một đại lượng là **tổng của nhiều yếu tố nhỏ độc lập** —
đó là nội dung **định lý giới hạn trung tâm** (bài 9).

| Đại lượng                   | Tổng của những gì                         |
| --------------------------- | ----------------------------------------- |
| Chiều cao người             | hàng nghìn gene + dinh dưỡng + môi trường |
| Sai số đo lường             | nhiều nguồn nhiễu nhỏ                     |
| Doanh thu ngày của siêu thị | hàng trăm giao dịch độc lập               |
| Điểm thi của một lớp đông   | nhiều yếu tố nhỏ về năng lực, may rủi     |

⚠️ **Nhưng đừng lạm dụng.** Những đại lượng **KHÔNG** chuẩn:

- **Thu nhập, giá trị đơn hàng, giá nhà** — lệch phải mạnh (bài 6 mục 5), thường là *log-chuẩn*.
- **Số đếm** (số đơn, số lỗi) — rời rạc, không âm, thường Poisson.
- **Lợi suất tài chính** — đuôi nặng, $\beta_2 > 3$ (bài 6 mục 6).

**Cách kiểm nhanh:** dữ liệu có âm được không? Nếu không (doanh thu, thời gian, số lượng) mà
$\sigma$ lại lớn so với trung bình, thì gần như chắc chắn **không** chuẩn.

**💼 Ứng dụng trực tiếp: kiểm soát chất lượng Six Sigma.** Tên gọi đến từ chính công thức (4.10):
đặt giới hạn dung sai ở $\pm 6\sigma$ thì tỷ lệ lỗi chỉ còn khoảng 3,4 phần triệu.
Ví dụ tính dung sai ở mục sau chính là mô hình thu nhỏ của việc này.

---

## 6. Quy chuẩn và cách tra bảng

Giáo trình nêu vấn đề (tr. 66): với thí dụ 4.4, *"khó tìm được xác suất để độ dài $X$ nằm trong một
khoảng **tuỳ ý**"* — vì tích phân của (4.9) không có nguyên hàm sơ cấp. Hai lối ra: dùng máy tính,
hoặc **tra bảng số**.

Nhưng không thể lập bảng cho **mọi** cặp $(a, \sigma)$. Giải pháp: **quy chuẩn**.

**Phép biến đổi quy chuẩn (4.14):**

$$Z = \frac{X - a}{\sigma}$$

Khi $X \sim N(a; \sigma^2)$ thì $Z \sim N(0; 1)$ — gọi là **phân phối chuẩn rút gọn**
(hay chuẩn chuẩn tắc), với hàm mật độ chính là **hàm Gauss**:

$$f(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$$

⚠️ Giáo trình lưu ý (tr. 68): *"$Z$ chỉ có phân phối chuẩn khi biến $X$ tương ứng tuân theo luật chuẩn,
tuy nhiên **$Z$ luôn có kỳ vọng 0 và phương sai 1**."* Quy chuẩn luôn làm được; nhưng chỉ ra chuẩn
khi $X$ vốn đã chuẩn.

**Hàm phân phối qua hàm Laplace (4.15):**

$$F(x) = 0{,}5 + \phi\!\left(\frac{x-a}{\sigma}\right), \qquad
\phi(x) = \frac{1}{\sqrt{2\pi}}\int_0^x e^{-t^2/2}\,dt \tag{4.11}$$

**Công thức tính xác suất trên một khoảng (4.16):**

$$P(\alpha < X < \beta) = \phi\!\left(\frac{\beta - a}{\sigma}\right) - \phi\!\left(\frac{\alpha - a}{\sigma}\right)$$

**Trường hợp đối xứng** — dùng rất nhiều trong bài toán dung sai:

$$P(|X - a| < \varepsilon) = 2\phi\!\left(\frac{\varepsilon}{\sigma}\right)$$

### Ví dụ dung sai (tr. 68)

> Vẫn chi tiết máy $N(20; 0{,}5^2)$, dung sai của máy là $\varepsilon = 1{,}25$. Tính tỷ lệ chính phẩm.

$$P(|X - 20| < 1{,}25) = 2\phi\!\left(\frac{1{,}25}{0{,}5}\right) = 2\phi(2{,}5) = 2 \cdot 0{,}4938 = \mathbf{0{,}9876}$$

> "Ở đây xác suất này có ý nghĩa là **tỷ lệ chính phẩm** của chiếc máy đã cho bằng 98,76%." (tr. 68)

💼 Đây là **bài toán trung tâm của quản trị chất lượng**: cho dung sai kỹ thuật, tính tỷ lệ đạt chuẩn.
Đảo lại cũng dùng được: muốn tỷ lệ chính phẩm 99,9%, cần $2\phi(\varepsilon/\sigma) = 0{,}999$
→ $\varepsilon/\sigma = 3{,}29$ → hoặc nới dung sai, hoặc **giảm $\sigma$** bằng cách cải tiến máy.

### ⚠️ Bẫy ký hiệu — ba hàm dễ nhầm

| Ký hiệu      | Tên                 | Định nghĩa                                           | Giá trị tại $+\infty$ | Bảng                |
| ------------ | ------------------- | ---------------------------------------------------- | --------------------- | ------------------- |
| $\varphi(x)$ | hàm **Gauss**      | $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$                    | 0                     | bảng 1, tr. 230     |
| $\phi(x)$    | hàm **Laplace**   | $\frac{1}{\sqrt{2\pi}}\int_0^x e^{-t^2/2}dt$         | **0,5**               | bảng 2, tr. 232     |
| $\Phi(x)$    | CDF chuẩn (quốc tế) | $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}dt$ | **1**                 | Excel `NORM.S.DIST` |

$$\Phi(x) = 0{,}5 + \phi(x)$$

**Hàm Laplace là hàm lẻ**: $\phi(-x) = -\phi(x)$. Hàm $\Phi$ thì không.

Trong Python: `NormalDist().cdf(x)` cho $\Phi(x)$, nên $\phi(x) =$ `NormalDist().cdf(x) - 0.5`.

**Tổng của các biến chuẩn (4.17).** Tổng $n$ biến chuẩn độc lập vẫn là biến chuẩn. Nếu
$X_i \sim N(a; \sigma^2)$ độc lập, $i = \overline{1,n}$:

$$\overline{X} \sim N\!\left(a; \frac{\sigma^2}{n}\right)
\qquad\Longleftrightarrow\qquad
\frac{\overline{X} - a}{\sigma/\sqrt{n}} \sim N(0; 1) \tag{4.17}$$

⭐ **Công thức (4.17b) là công thức quan trọng nhất của cả phần thống kê.** Bài 11 (khoảng tin cậy)
và bài 12 (kiểm định giả thuyết) đều dựng trên nó. Chú ý mẫu số $\sigma/\sqrt{n}$ — chính là
luật căn bậc hai ở bài 6 mục 4.

---

## 7. Xấp xỉ nhị thức bằng chuẩn

**Điều kiện (tr. 69):** $p$ không quá gần 0 hoặc 1, và $n$ khá lớn. Cụ thể:

$$np > 5 \text{ khi } p < 0{,}5, \qquad n(1-p) > 5 \text{ khi } p > 0{,}5$$

Khi đó $B(n, p) \approx N(np; npq)$ và:

$$P(\alpha < X < \beta) \approx \phi\!\left(\frac{\beta - np}{\sqrt{npq}}\right) - \phi\!\left(\frac{\alpha - np}{\sqrt{npq}}\right) \tag{4.18}$$

Giáo trình gọi đây là **luật nhị thức hội tụ theo luật đến luật chuẩn chuẩn tắc**:

$$\frac{X - np}{\sqrt{npq}} \ \xrightarrow{\ L\ } \ N(0; 1)$$

Tương tự với Poisson (tr. 70): $\dfrac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{\ L\ } N(0;1)$ khi $\lambda \to \infty$.

### Thí dụ 4.5 (tr. 69) — và hiệu chỉnh liên tục

> $X \sim B(20; 0{,}4)$, tính $P(4 < X < 13)$.

$np = 8$, $npq = 4{,}8$, $\sqrt{npq} = 2{,}1909$.

**Không hiệu chỉnh**, theo (4.18):

$$\phi\!\left(\frac{13-8}{\sqrt{4{,}8}}\right) + \phi\!\left(\frac{8-4}{\sqrt{4{,}8}}\right)
= \phi(2{,}28) + \phi(1{,}83) = 0{,}4884 + 0{,}4664 = \mathbf{0{,}9548}$$

Giáo trình nhận xét (tr. 69): *"do $n = 20$ vẫn chưa thật lớn, trong thực hành người ta **hiệu chỉnh**
(4.18) như sau"*:

$$P(\alpha < X < \beta) \approx \phi\!\left(\frac{\beta + 0{,}5 - np}{\sqrt{npq}}\right) - \phi\!\left(\frac{\alpha - 0{,}5 - np}{\sqrt{npq}}\right)$$

> "Việc cộng thêm vào $+0{,}5$ và $-0{,}5$ chính là **yếu tố hiệu chỉnh khi xấp xỉ một biến rời rạc
> bằng biến liên tục**." (tr. 70)

$$P(4 < X < 13) \approx \phi(2{,}51) + \phi(1{,}60) = \mathbf{0{,}9743}$$

Đây chính là **hiệu chỉnh liên tục** đã giới thiệu ở bài 3 mục 8 — giáo trình có dùng ở đây,
chỉ không dùng ở chương I.

### ⚠️ Một chỗ thiếu nhất quán trong giáo trình

Giáo trình ghi: *"kết quả thật của xác suất này là **0,978**"*. Nhưng tính bằng máy:

| Cách hiểu                                         | Giá trị nhị thức đúng |
| ------------------------------------------------- | --------------------: |
| $P(4 < X < 13)$ — dấu **ngặt** (đúng như đề viết) |            **0,9280** |
| $P(4 \le X \le 13)$ — dấu **không ngặt**          |  **0,9776** ≈ 0,978 ✓ |

Con số "0,978" của sách ứng với **$P(4 \le X \le 13)$**, không phải $P(4 < X < 13)$ như đề bài viết.
Và công thức hiệu chỉnh dùng mốc $13{,}5$ / $3{,}5$ cũng xấp xỉ cho **$P(4 \le X \le 13)$**.

**Không phải lỗi tính toán, mà là lỗi ký hiệu**: dấu ngoặc trong đề nên là $\le$. Khi làm bài,
điều quan trọng là **thống nhất**: nếu hiệu chỉnh bằng $\alpha - 0{,}5$ thì bạn đang tính
$P(X \ge \alpha)$, không phải $P(X > \alpha)$.

**Bảng đối chiếu bốn con số** (tính bằng máy, xem mục 10):

|                                         |    Giá trị |
| --------------------------------------- | ---------: |
| Xấp xỉ chuẩn, không hiệu chỉnh          |     0,9548 |
| Xấp xỉ chuẩn, có hiệu chỉnh $\pm 0{,}5$ |     0,9740 |
| Nhị thức đúng $P(4 \le X \le 13)$       | **0,9776** |
| Nhị thức đúng $P(4 < X < 13)$           |     0,9280 |

Hiệu chỉnh kéo sai số từ 0,023 xuống 0,004 — **giảm gần 6 lần**, đúng như bài 3 mục 8 nói.
(Sách ghi 0,9743 vì tra bảng làm tròn; tính chính xác được 0,9740.)

---

## 8. Bốn phân phối của phần thống kê

Giáo trình mở mục 4.6 (tr. 70): *"nhiều phân phối liên tục được **cảm sinh trực tiếp bởi phân phối
chuẩn**"*. Bốn phân phối dưới đây **chưa dùng ngay ở Chương II**, nhưng là công cụ của bài 11–14.
Đọc lướt bây giờ, quay lại khi cần.

### chi bình phương $\chi^2(n)$

**Định nghĩa 10 (tr. 71).** Cho $n$ biến độc lập $X_i \sim N(0;1)$. Khi đó

$$U = \sum_{i=1}^{n} X_i^2 \sim \chi^2(n) \tag{4.20}$$

$n$ gọi là **bậc tự do**. Giáo trình khen cách định nghĩa này: nó *"cho ta cách nhận biết đơn giản"*
so với việc viết hàm mật độ (4.19) rắc rối.

$$EU = n, \qquad VU = 2n$$

**Tính chất:**
- $X \sim \chi^2(n)$, $Y \sim \chi^2(m)$ độc lập $\Rightarrow X + Y \sim \chi^2(n+m)$ (cộng bậc tự do);
- $\dfrac{U - n}{\sqrt{2n}} \xrightarrow{\ L\ } N(0;1)$ khi $n \to \infty$.

⭐ **Hệ quả quan trọng nhất (4.21), tr. 71** — nền của khoảng tin cậy cho phương sai (bài 11):
nếu $X_i \sim N(a; \sigma^2)$ độc lập và $\overline{X} = \frac1n(X_1 + \cdots + X_n)$ thì

$$\frac{1}{\sigma^2}\sum_{i=1}^{n}\left(X_i - \overline{X}\right)^2 \sim \chi^2(n-1)$$

Giáo trình giải thích chỗ **mất một bậc tự do**: *"do ta thay thế $a$ bằng $\overline{X}$, vì vậy
bậc tự do của phân phối đã bớt đi 1."*

⚠️ **Đây là lý do sâu xa của việc chia cho $n-1$ thay vì $n$** khi tính phương sai mẫu — bài 10
sẽ quay lại. Ước lượng $a$ từ chính dữ liệu đã "tiêu" mất một bậc tự do.

### Student $t(n)$

**Định nghĩa 11 (tr. 72).** Cho $X \sim N(0;1)$ và $Y \sim \chi^2(n)$ **độc lập**:

$$T = \frac{X}{\sqrt{Y/n}} \sim t(n) \tag{4.22}$$

$$ET = 0 \ (n > 1), \qquad VT = \frac{n}{n-2} \ (n > 2)$$

**Tính chất then chốt:** $t(n) \xrightarrow[n \to \infty]{} N(0;1)$.

Giáo trình cho mốc thực hành (tr. 72): *"khi $n > 30$, đồ thị của đường cong mật độ phân phối $t(n)$
đã **rất gần** với $N(0;1)$."*

Đồ thị $t(n)$ giống chuẩn nhưng **thấp hơn ở giữa và đuôi dày hơn** — phản ánh sự bất định thêm do
phải ước lượng $\sigma$ từ mẫu.

⚠️ Trường hợp $n = 1$ cho **phân phối Cauchy** — giáo trình lưu ý đây là *"phân phối **không có mômen
nào**"*, tức không có kỳ vọng, không có phương sai. Một quái vật toán học hữu ích để nhớ rằng
"mọi phân phối đều có trung bình" là sai.

Bảng phân vị $t(n)$: bảng 3, tr. 233.

### Fisher – Snedecor $F(n, m)$

**Định nghĩa 12 (tr. 72).** $X \sim \chi^2(n)$, $Y \sim \chi^2(m)$ độc lập:

$$U = \frac{X/n}{Y/m} \sim F(n, m) \tag{4.23}$$

$$EU = \frac{m}{m-2} \ (m > 2), \qquad VU = \frac{2m^2(n+m-2)}{n(m-2)^2(m-4)} \ (m > 4)$$

**Hai tính chất tiện dụng (tr. 73):**
- $U \sim F(n,m) \Rightarrow \dfrac1U \sim F(m,n)$ (đảo bậc tự do);
- nếu $T \sim t(m)$ thì $T^2 \sim F(1, m)$.

Bảng phân vị: bảng 5, tr. 235.

### Gamma $\gamma(r, \lambda)$

**Định nghĩa 13 (tr. 73).**

$$f(x) = \frac{\lambda^r}{\Gamma(r)}x^{r-1}e^{-\lambda x}, \qquad r > 0,\ \lambda > 0,\ x > 0 \tag{4.24}$$

$$EX = \frac{r}{\lambda}, \qquad VX = \frac{r}{\lambda^2}$$

Tính chất: $X \sim \gamma(p,\lambda)$, $Y \sim \gamma(q,\lambda)$ độc lập $\Rightarrow X+Y \sim \gamma(p+q,\lambda)$.

⚠️ **Khi $r = 1$ ta được phân phối mũ $\mathcal{E}(\lambda)$** (thí dụ 2.8, bài 5) —
*"có nhiều ứng dụng trong lý thuyết độ tin cậy"*.

### Quan hệ giữa bốn phân phối

```
                    N(0;1)  ← quy chuẩn từ N(a, σ²)
                       │
        ┌──────────────┼──────────────┐
        │ bình phương  │              │  chia cho √(χ²/n)
        │ và cộng n cái│              ▼
        ▼              │           t(n)  ─── bình phương ──► F(1, m)
     χ²(n)             │              │
        │              │              │  n → ∞
        │ tỷ số        │              ▼
        │ hai cái      │           N(0;1)
        ▼              │
     F(n, m)           │
                       │  n → ∞ (chuẩn hoá)
                       ▼
                    N(0;1)
```

**Dùng khi nào** (xem trước cho bài 11–14):

| Phân phối   | Dùng để                                                  | Bài    |
| ----------- | -------------------------------------------------------- | ------ |
| $N(0;1)$    | suy luận về kỳ vọng khi **đã biết** $\sigma$             | 11, 12 |
| $t(n)$      | suy luận về kỳ vọng khi **chưa biết** $\sigma$           | 11, 12 |
| $\chi^2(n)$ | suy luận về **phương sai**; kiểm định phù hợp và độc lập | 11, 13 |
| $F(n,m)$    | so sánh **hai phương sai**; phân tích phương sai ANOVA   | 13     |

---

## 9. 📚 Cây quyết định chọn phân phối

Giáo trình trình bày mười mấy phân phối mà không có bảng tra cứu tổng hợp. Đây là phần bổ sung.

```
   Biến đếm được (RỜI RẠC) hay đo được (LIÊN TỤC)?
   │
   ├─── RỜI RẠC ───────────────────────────────────────────────
   │    │
   │    ├─ Mọi giá trị đồng khả năng?          → ĐỀU RỜI RẠC U(n)
   │    │
   │    ├─ Lặp n lần CỐ ĐỊNH, đếm số thành công?
   │    │     ├─ lấy mẫu CÓ hoàn lại / N > 10n → NHỊ THỨC B(n,p)
   │    │     └─ lấy mẫu KHÔNG hoàn lại, N nhỏ → SIÊU BỘI H(N,n,p)
   │    │
   │    ├─ Đếm sự kiện hiếm trong 1 đơn vị thời gian/không gian?
   │    │                                       → POISSON P(λ)
   │    │     dấu hiệu: trung bình ≈ phương sai
   │    │
   │    └─ Lặp tới khi thành công, đếm số lần?
   │          ├─ tới lần thành công ĐẦU TIÊN    → HÌNH HỌC G(p)
   │          └─ tới lần thành công THỨ r       → NHỊ THỨC ÂM NB(r,p)
   │
   └─── LIÊN TỤC ──────────────────────────────────────────────
        │
        ├─ Chỉ biết khoảng, không biết gì hơn?  → ĐỀU U([a;b])
        │
        ├─ Thời gian CHỜ, giả thiết "không nhớ"? → MŨ E(λ)
        │     ⚠ có hao mòn thì dùng WEIBULL
        │
        ├─ Tổng của NHIỀU yếu tố nhỏ độc lập?   → CHUẨN N(a, σ²)
        │     ⚠ dữ liệu không âm và lệch phải  → LOG-CHUẨN
        │
        └─ Dùng cho suy luận thống kê?
              ├─ về kỳ vọng, biết σ             → N(0;1)
              ├─ về kỳ vọng, chưa biết σ        → t(n)
              ├─ về phương sai / phù hợp        → χ²(n)
              └─ so 2 phương sai / ANOVA        → F(n,m)
```

### Bảng tra nhanh — kỳ vọng và phương sai

| Phân phối       | Ký hiệu                | $EX$                 | $VX$                                 |
| --------------- | ---------------------- | -------------------- | ------------------------------------ |
| Đều rời rạc     | $\mathcal{U}(n)$       | $\dfrac{n+1}{2}$     | $\dfrac{n^2-1}{12}$                  |
| Đều liên tục    | $\mathcal{U}([a;b])$   | $\dfrac{a+b}{2}$     | $\dfrac{(b-a)^2}{12}$                |
| Bernoulli       | $B(p)$                 | $p$                  | $pq$                                 |
| **Nhị thức**    | $B(n,p)$               | $np$                 | $npq$                                |
| **Poisson**    | $P(\lambda)$           | $\lambda$            | $\lambda$                            |
| Siêu bội        | $H(N,n,p)$             | $np$                 | $npq\dfrac{N-n}{N-1}$                |
| Hình học        | $G(p)$                 | $\dfrac{q}{p}$       | $\dfrac{q}{p^2}$                     |
| Nhị thức âm     | $NB(r,p)$              | $\dfrac{rq}{p}$      | $\dfrac{rq}{p^2}$                    |
| **Chuẩn**       | $N(a,\sigma^2)$        | $a$                  | $\sigma^2$                           |
| Mũ              | $\mathcal{E}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$               |
| Gamma          | $\gamma(r,\lambda)$    | $\dfrac{r}{\lambda}$ | $\dfrac{r}{\lambda^2}$               |
| chi bình phương | $\chi^2(n)$            | $n$                  | $2n$                                 |
| Student        | $t(n)$                 | $0$                  | $\dfrac{n}{n-2}$                     |
| Fisher          | $F(n,m)$               | $\dfrac{m}{m-2}$     | $\dfrac{2m^2(n+m-2)}{n(m-2)^2(m-4)}$ |

**Ba dòng in đậm là ba phân phối bạn sẽ dùng 90% thời gian.**

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-07-phan-phoi.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**. `statistics.NormalDist` lo phần phân phối chuẩn.

Code dựng lại năm thí dụ của giáo trình, và quan trọng nhất là **đo sai số của các phép xấp xỉ** —
thứ mà sách chỉ khẳng định bằng lời.

```python
"""Bài 7 — Các phân phối thông dụng."""

import math
from fractions import Fraction
from statistics import NormalDist

Z = NormalDist()                      # chuan chuan tac N(0;1)
laplace = lambda x: Z.cdf(x) - 0.5    # ham Laplace (bang 2): tich phan TU 0


def binom(n, k, p):
    return math.comb(n, k) * p**k * (1 - p) ** (n - k)


def poisson(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)


def hyper(N, M, n, k):
    """Sieu boi: N san pham, M phe pham, chon n, hoi dung k phe pham."""
    return Fraction(math.comb(M, k) * math.comb(N - M, n - k), math.comb(N, n))


# ─────────────────────────────────────────────────────────────
# 1. NHỊ THỨC — Thí dụ 4.1 (tr. 59), X ~ B(5; 0,25)
# ─────────────────────────────────────────────────────────────
n, p = 5, 0.25
print("THI DU 4.1 — X ~ B(5; 0,25)")
table = {k: binom(n, k, p) for k in range(n + 1)}
print(f"{'x':>4}" + "".join(f"{k:>10}" for k in table))
print(f"{'p(x)':>4}" + "".join(f"{v:>10.4f}" for v in table.values()))
print(f"  Tong = {sum(table.values()):.4f}")
print(f"  a) P(X > 3) = p(4)+p(5) = {table[4] + table[5]:.4f}   (sach: 0,0156)")
print(f"  b) P(X >= 1) = 1 - p(0) = {1 - table[0]:.4f}   (sach: 0,7627)")
print(f"  c) P(X < 4)  = 1 - p(5) = {1 - table[5]:.4f}   (sach: 0,9990)")
mode = max(table, key=table.get)
print(f"  Mot = {mode}  (so lan xuat hien 'chac chan nhat')")
print(f"  EX = np = {n * p}   VX = npq = {n * p * (1 - p)}"
      f"   sigma = {math.sqrt(n * p * (1 - p)):.4f}")

# ─────────────────────────────────────────────────────────────
# 2. POISSON — Thí dụ 4.2 (tr. 61), 5000 chai, p = 0,0004
# ─────────────────────────────────────────────────────────────
print()
N_CHAI, P_VO = 5000, 0.0004
lam = N_CHAI * P_VO
print(f"THI DU 4.2 — {N_CHAI} chai, p = {P_VO}  ->  lambda = np = {lam}")
approx = poisson(0, lam) + poisson(1, lam)
exact = binom(N_CHAI, 0, P_VO) + binom(N_CHAI, 1, P_VO)
print(f"  P(0 <= X <= 1) xap xi Poisson = 3/e^2 = {approx:.4f}   (sach: 0,406)")
print(f"  P(0 <= X <= 1) nhi thuc DUNG   =         {exact:.4f}")
print(f"  Sai lech = {abs(approx - exact):.6f}")
print(f"  EX = VX = lambda = {lam}")
print(f"  Mot: lambda-1 <= mot <= lambda  ->  mot = 1 va 2,"
      f" p(1) = p(2) = {poisson(1, lam):.4f}   (sach: 0,2707)")

# ─────────────────────────────────────────────────────────────
# 3. SIÊU BỘI — Thí dụ 4.3 (tr. 62), 15 bóng, 5 kém, chọn 10
# ─────────────────────────────────────────────────────────────
print()
N, M, n_pick = 15, 5, 10
print(f"THI DU 4.3 — {N} bong, {M} kem chat luong, chon {n_pick} (KHONG hoan lai)")
print(f"{'x':>4}{'sieu boi p(x)':>16}{'nhi thuc p(x)':>16}{'sai lech':>12}")
for k in range(0, 6):
    h = hyper(N, M, n_pick, k)
    b = binom(n_pick, k, 1 / 3)
    print(f"{k:>4}{float(h):>16.5f}{b:>16.5f}{abs(float(h) - b):>12.5f}")
tong = sum(hyper(N, M, n_pick, k) for k in range(6))
print(f"  Tong sieu boi = {tong}  (x >= 6 deu bang 0 vi chi co 5 bong kem)")
print("  ⚠ Sai lech qua lon -> KHONG duoc xap xi. Dieu kien: N > 10n")
print(f"     o day N={N}, 10n={10 * n_pick}  ->  {N} > {10 * n_pick}? "
      f"{N > 10 * n_pick}")
p_ = Fraction(M, N)
print(f"  EX = np = {n_pick * p_} | VX = npq(N-n)/(N-1) ="
      f" {n_pick * p_ * (1 - p_) * Fraction(N - n_pick, N - 1)}")

# ─────────────────────────────────────────────────────────────
# 4. CHUẨN — quy tắc 3 sigma (4.10) và Thí dụ 4.4 (tr. 66)
# ─────────────────────────────────────────────────────────────
print()
print("QUY TAC 3 SIGMA (4.10)")
for k, sach in [(1, "68,26%"), (2, "95,44%"), (3, "99,74%")]:
    pk = 2 * laplace(k)
    print(f"  P(|X - a| < {k} sigma) = {pk * 100:.2f}%   (sach: {sach})")

print()
print("THI DU 4.4 — chi tiet may, a = 20 cm, sigma = 0,5")
a, s = 20, 0.5
print(f"  a) P(X > 20)   = {1 - NormalDist(a, s).cdf(20):.4f}   (sach: 0,5)")
print(f"  b) P(X < 19,5) = {NormalDist(a, s).cdf(19.5) * 100:.2f}%   (sach: 15,87%)")
print(f"  c) P(X > 21,5) = {(1 - NormalDist(a, s).cdf(21.5)) * 100:.4f}%"
      "   (sach: 0,13%)")
# Vi du dung sai 1,25 (tr. 68)
eps = 1.25
print(f"  Dung sai {eps}: P(|X-20| < {eps}) = 2.phi({eps / s}) ="
      f" {2 * laplace(eps / s):.4f}   (sach: 0,9876)")
print(f"  -> ty le chinh pham = {2 * laplace(eps / s) * 100:.2f}%")

# ─────────────────────────────────────────────────────────────
# 5. XẤP XỈ CHUẨN CHO NHỊ THỨC — Thí dụ 4.5 (tr. 69)
#    X ~ B(20; 0,4), tính P(4 < X < 13)
# ─────────────────────────────────────────────────────────────
print()
n, p = 20, 0.4
np_, sd = n * p, math.sqrt(n * p * (1 - p))
print(f"THI DU 4.5 — X ~ B(20; 0,4), np = {np_}, npq = {n * p * (1 - p)},"
      f" can = {sd:.4f}")
no_corr = laplace((13 - np_) / sd) - laplace((4 - np_) / sd)
corr = laplace((13 + 0.5 - np_) / sd) - laplace((4 - 0.5 - np_) / sd)
print(f"  Khong hieu chinh (4.18)      : {no_corr:.4f}   (sach: 0,9548)")
print(f"  Co hieu chinh +-0,5          : {corr:.4f}   (sach: 0,9743)")
strict = sum(binom(n, k, p) for k in range(5, 13))     # 4 < X < 13, dau NGAT
closed = sum(binom(n, k, p) for k in range(4, 14))     # 4 <= X <= 13
print(f"  Nhi thuc DUNG P(4 < X < 13)  : {strict:.4f}")
print(f"  Nhi thuc DUNG P(4 <= X <= 13): {closed:.4f}   (sach ghi 'that': 0,978)")
print("  ⚠ Hieu chinh +-0,5 xap xi cho P(4 <= X <= 13), khong phai dau ngat")

# ─────────────────────────────────────────────────────────────
# 6. 💼 GÓC QTKD — chọn phân phối nào cho bài toán nào
# ─────────────────────────────────────────────────────────────
print()
print("💼 GOC QTKD — mot bai toan, ba phan phoi")
LO, LOI, MAU = 1000, 30, 50        # lo 1000 sp, 30 loi, kiem 50 sp
print(f"Lo {LO} san pham co {LOI} loi. Kiem {MAU} san pham.")
print("  P(khong tim thay loi nao):")
h0 = hyper(LO, LOI, MAU, 0)
b0 = binom(MAU, 0, LOI / LO)
p0 = poisson(0, MAU * LOI / LO)
print(f"    Sieu boi (dung, khong hoan lai) : {float(h0):.6f}")
print(f"    Nhi thuc (xap xi, co hoan lai)  : {b0:.6f}"
      f"   sai lech {abs(float(h0) - b0):.6f}")
print(f"    Poisson (xap xi, lambda = {MAU * LOI / LO})  : {p0:.6f}"
      f"   sai lech {abs(float(h0) - p0):.6f}")
print(f"  N = {LO} > 10n = {10 * MAU}  ->  duoc phep xap xi nhi thuc")
print(f"  => Kiem {MAU} sp ma khong thay loi thi van con"
      f" {float(h0) * 100:.1f}% kha nang lo co 3% loi")
```

Kết quả chạy thật:

```
THI DU 4.1 — X ~ B(5; 0,25)
   x         0         1         2         3         4         5
p(x)    0.2373    0.3955    0.2637    0.0879    0.0146    0.0010
  Tong = 1.0000
  a) P(X > 3) = p(4)+p(5) = 0.0156   (sach: 0,0156)
  b) P(X >= 1) = 1 - p(0) = 0.7627   (sach: 0,7627)
  c) P(X < 4)  = 1 - p(5) = 0.9990   (sach: 0,9990)
  Mot = 1  (so lan xuat hien 'chac chan nhat')
  EX = np = 1.25   VX = npq = 0.9375   sigma = 0.9682

THI DU 4.2 — 5000 chai, p = 0.0004  ->  lambda = np = 2.0
  P(0 <= X <= 1) xap xi Poisson = 3/e^2 = 0.4060   (sach: 0,406)
  P(0 <= X <= 1) nhi thuc DUNG   =         0.4060
  Sai lech = 0.000054
  EX = VX = lambda = 2.0
  Mot: lambda-1 <= mot <= lambda  ->  mot = 1 va 2, p(1) = p(2) = 0.2707   (sach: 0,2707)

THI DU 4.3 — 15 bong, 5 kem chat luong, chon 10 (KHONG hoan lai)
   x   sieu boi p(x)   nhi thuc p(x)    sai lech
   0         0.00033         0.01734     0.01701
   1         0.01665         0.08671     0.07006
   2         0.14985         0.19509     0.04524
   3         0.39960         0.26012     0.13948
   4         0.34965         0.22761     0.12204
   5         0.08392         0.13656     0.05265
  Tong sieu boi = 1  (x >= 6 deu bang 0 vi chi co 5 bong kem)
  ⚠ Sai lech qua lon -> KHONG duoc xap xi. Dieu kien: N > 10n
     o day N=15, 10n=100  ->  15 > 100? False
  EX = np = 10/3 | VX = npq(N-n)/(N-1) = 50/63

QUY TAC 3 SIGMA (4.10)
  P(|X - a| < 1 sigma) = 68.27%   (sach: 68,26%)
  P(|X - a| < 2 sigma) = 95.45%   (sach: 95,44%)
  P(|X - a| < 3 sigma) = 99.73%   (sach: 99,74%)

THI DU 4.4 — chi tiet may, a = 20 cm, sigma = 0,5
  a) P(X > 20)   = 0.5000   (sach: 0,5)
  b) P(X < 19,5) = 15.87%   (sach: 15,87%)
  c) P(X > 21,5) = 0.1350%   (sach: 0,13%)
  Dung sai 1.25: P(|X-20| < 1.25) = 2.phi(2.5) = 0.9876   (sach: 0,9876)
  -> ty le chinh pham = 98.76%

THI DU 4.5 — X ~ B(20; 0,4), np = 8.0, npq = 4.8, can = 2.1909
  Khong hieu chinh (4.18)      : 0.9548   (sach: 0,9548)
  Co hieu chinh +-0,5          : 0.9740   (sach: 0,9743)
  Nhi thuc DUNG P(4 < X < 13)  : 0.9280
  Nhi thuc DUNG P(4 <= X <= 13): 0.9776   (sach ghi 'that': 0,978)
  ⚠ Hieu chinh +-0,5 xap xi cho P(4 <= X <= 13), khong phai dau ngat

💼 GOC QTKD — mot bai toan, ba phan phoi
Lo 1000 san pham co 30 loi. Kiem 50 san pham.
  P(khong tim thay loi nao):
    Sieu boi (dung, khong hoan lai) : 0.209681
    Nhi thuc (xap xi, co hoan lai)  : 0.218065   sai lech 0.008384
    Poisson (xap xi, lambda = 1.5)  : 0.223130   sai lech 0.013449
  N = 1000 > 10n = 500  ->  duoc phep xap xi nhi thuc
  => Kiem 50 sp ma khong thay loi thi van con 21.0% kha nang lo co 3% loi
```

Bốn điểm đáng để ý:

1. **Quy tắc $3\sigma$ máy tính ra 68,27 / 95,45 / 99,73** — sách ghi 68,26 / 95,44 / 99,74.
   Chênh ở chữ số thứ tư, do sách tra bảng 4 chữ số. Không phải lỗi.
2. **Bảng siêu bội vs nhị thức**: cột sai lệch lên tới **0,139** ở $x = 3$. Đây là bằng chứng bằng số
   cho điều kiện $N > 10n$ mà sách chỉ nói bằng lời.
3. **Thí dụ 4.5**: bốn con số 0,9548 / 0,9740 / 0,9280 / 0,9776 cho thấy rõ chuyện đã nêu ở mục 7 —
   "0,978" của sách khớp với $P(4 \le X \le 13)$, không phải dấu ngặt.
4. **Góc QTKD**: kiểm 50/1000 sản phẩm mà không thấy lỗi nào thì **vẫn còn 21% khả năng lô hàng có
   3% lỗi**. Đây là con số nên đưa vào mọi cuộc thương lượng với nhà cung cấp — "chúng tôi kiểm
   không thấy lỗi" không đồng nghĩa "lô hàng sạch".

---

## 11. Tự thử

1. Ở thí dụ 4.1, đổi $p = 0{,}25$ thành $0{,}5$. Mốt bằng bao nhiêu? Bảng có đối xứng không?
   Còn $p = 0{,}75$?
2. Ở thí dụ 4.2, đổi $p$ từ 0,0004 lên 0,01 (giữ $n = 5000$, $\lambda = 50$). Sai lệch giữa Poisson
   và nhị thức đúng tăng hay giảm? Xấp xỉ còn dùng được không?
3. Ở thí dụ 4.3, đổi thành $N = 150$ bóng, 50 bóng kém, chọn 10. Điều kiện $N > 10n$ có thoả không?
   Sai lệch lớn nhất giờ là bao nhiêu?
4. Viết hàm tìm dung sai $\varepsilon$ cho trước tỷ lệ chính phẩm mong muốn (nghịch đảo của ví dụ
   tr. 68): cho 99,9%, tìm $\varepsilon$ khi $\sigma = 0{,}5$. Dùng `NormalDist().inv_cdf`.
5. Ở phần Góc QTKD, đổi cỡ mẫu từ 50 lên 100, 200, 300. Vẽ bảng $P(\text{không thấy lỗi nào})$
   theo cỡ mẫu. Cần kiểm bao nhiêu sản phẩm để con số đó xuống dưới 5%?
   So với quy tắc $3/p$ ở bài 3 mục 6.
6. Kiểm hai tính chất cộng: (a) $X_1 \sim B(10; 0{,}3)$, $X_2 \sim B(15; 0{,}3)$ độc lập, tổng có
   phải $B(25; 0{,}3)$ không? Dùng `convolve` ở bài 5. (b) Thử với $p$ **khác nhau** — còn đúng không?
7. Tính $EX$ và $VX$ của $X \sim G(0{,}1)$ (hình học). Kiểm bằng cách cộng trực tiếp
   $\sum x\,p(1-p)^x$ với $x$ từ 0 đến 500.

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)           | Tiếng Anh                          | Ký hiệu                |
| --------------------------------- | ---------------------------------- | ---------------------- |
| Phân phối đều                     | Uniform distribution               | $\mathcal{U}$          |
| Phân phối Bernoulli               | Bernoulli distribution             | $B(p)$                 |
| Phân phối nhị thức                | Binomial distribution              | $B(n,p)$               |
| Phân phối Poisson                | Poisson distribution               | $P(\lambda)$           |
| Phân phối siêu bội, siêu hình học | Hypergeometric distribution        | $H(N,n,p)$             |
| Phân phối hình học                | Geometric distribution             | $G(p)$                 |
| Phân phối nhị thức âm             | Negative binomial                  | $NB(r,p)$              |
| Phân phối chuẩn, Gauss           | Normal, Gaussian distribution      | $N(a,\sigma^2)$        |
| Chuẩn rút gọn, chuẩn chuẩn tắc    | Standard normal                    | $N(0;1)$               |
| Quy chuẩn                         | Standardization                    | $Z = (X-a)/\sigma$     |
| Quy tắc 3 sigma                   | Three-sigma rule / 68–95–99.7 rule | (4.10)                 |
| Số lần xuất hiện chắc chắn nhất   | Most probable number               | = mốt                  |
| Phân phối mũ                      | Exponential distribution           | $\mathcal{E}(\lambda)$ |
| Phân phối Gamma                  | Gamma distribution                 | $\gamma(r,\lambda)$    |
| Phân phối Weibull                 | Weibull distribution               |                        |
| Phân phối chi bình phương         | Chi-squared distribution           | $\chi^2(n)$            |
| Bậc tự do                         | Degrees of freedom                 | $n$                    |
| Phân phối Student                | Student's t-distribution           | $t(n)$                 |
| Phân phối Cauchy                   | Cauchy distribution                | $t(1)$                 |
| Phân phối Fisher – Snedecor      | Fisher–Snedecor F-distribution     | $F(n,m)$               |
| Hội tụ theo luật                  | Convergence in distribution        | $\xrightarrow{L}$      |
| Hiệu chỉnh liên tục               | Continuity correction              | $\pm 0{,}5$            |

---

## 13. Câu hỏi tự kiểm tra

1. Ba điều kiện của phân phối nhị thức là gì? Với mỗi điều kiện, cho một ví dụ kinh doanh **vi phạm** nó.
2. Vì sao $EX = VX$ là dấu hiệu nhận biết Poisson? Nếu dữ liệu thật có phương sai gấp 3 lần trung
   bình thì nói lên điều gì?
3. Khi nào được xấp xỉ siêu bội bằng nhị thức? Chứng minh bằng số với $N = 1000$, $n = 20$, $M = 100$.
4. Một lô hàng 200 sản phẩm có 10 lỗi. Kiểm 30 sản phẩm.
   a) Dùng phân phối nào? Kiểm điều kiện.
   b) Xác suất tìm được ít nhất 1 lỗi?
5. Doanh thu ngày $\sim N(50; 8^2)$ triệu. Không tra bảng, chỉ dùng quy tắc $3\sigma$:
   a) $P(42 < X < 58)$? b) $P(X > 66)$? c) Khoảng nào chứa 95% số ngày?
6. Thời gian giao hàng $\sim N(3; 0{,}5^2)$ ngày. Công ty cam kết "giao trong 4 ngày, chậm thì đền tiền".
   Tỷ lệ đơn phải đền là bao nhiêu? Muốn giảm xuống dưới 1%, phải cam kết mấy ngày?
7. Vì sao hệ quả (4.21) có $n-1$ bậc tự do chứ không phải $n$? Liên hệ với việc chia $n-1$ khi tính
   phương sai mẫu.
8. Bài 12 (tr. 78): ở một thửa ruộng trung bình 1 giờ tìm được 60 con sâu. Tìm xác suất trong vòng
   **1 phút** không tìm thấy con sâu nào. (Gợi ý: đổi $\lambda$ theo đơn vị thời gian.)
9. Bài 6 (tr. 77): vùng dân cư có tỷ lệ sốt rét 5%. Cần chọn ít nhất bao nhiêu người để với xác suất
   95% có ít nhất 1 người mắc? (So với thí dụ 3.12 ở bài 3.)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 7 — CÁC PHÂN PHỐI THÔNG DỤNG                (Ch. II §4, tr. 56–78)  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  RỜI RẠC — tất cả sinh ra từ PHÉP THỬ BERNOULLI B(p): EX=p, VX=pq        ║
║  ┌────────────────┬──────────────────────┬─────────┬──────────────┐      ║
║  │ Phân phối      │ Khi nào              │   EX    │      VX      │      ║
║  ├────────────────┼──────────────────────┼─────────┼──────────────┤      ║
║  │ ĐỀU U(n)       │ đồng khả năng        │ (n+1)/2 │  (n²−1)/12   │      ║
║  │ NHỊ THỨC B(n,p)│ n lần cố định        │   np    │     npq      │      ║
║  │ POISSON P(λ)  │ sự kiện HIẾM, n→∞p→0 │    λ    │      λ       │       ║
║  │ SIÊU BỘI       │ KHÔNG hoàn lại       │   np    │npq(N−n)/(N−1)│      ║
║  │ HÌNH HỌC G(p)  │ tới thành công ĐẦU   │   q/p   │    q/p²      │      ║
║  │ NHỊ THỨC ÂM    │ tới thành công thứ r │  rq/p   │   rq/p²      │      ║
║  └────────────────┴──────────────────────┴─────────┴──────────────┘      ║
║                                                                          ║
║  ⚠ SIÊU BỘI → NHỊ THỨC chỉ khi  N > 10n   (thí dụ 4.3: sai 0,139!)       ║
║  ⚠ POISSON: dấu hiệu nhận biết là  EX ≈ VX  trên dữ liệu thật            ║
║  ⚠ POISSON cộng được: λ₁ + λ₂ → đổi đơn vị thời gian tự do               ║
║                                                                          ║
║  LIÊN TỤC                                                                ║
║      ĐỀU U([a;b])   EX=(a+b)/2      VX=(b−a)²/12                         ║
║      MŨ E(λ)        EX=1/λ          VX=1/λ²    ← EX = σ                  ║
║      CHUẨN N(a,σ²)  EX=a            VX=σ²      ← EX = med = mốt = a      ║
║                                                                          ║
║  ⭐ QUY TẮC 3 SIGMA — THUỘC LÒNG                                         ║
║      P(|X−a| < 1σ) = 68,26%                                              ║
║      P(|X−a| < 2σ) = 95,44%                                              ║
║      P(|X−a| < 3σ) = 99,74%                                              ║
║                                                                          ║
║  QUY CHUẨN   Z = (X − a)/σ  ~ N(0;1)                                     ║
║      F(x) = 0,5 + ϕ((x−a)/σ)                                             ║
║      P(α<X<β) = ϕ((β−a)/σ) − ϕ((α−a)/σ)                                  ║
║      P(|X−a| < ε) = 2ϕ(ε/σ)          ← bài toán DUNG SAI                 ║
║                                                                          ║
║  ⚠ BA HÀM DỄ NHẦM                                                        ║
║      φ(x) Gauss    = mật độ,          φ(∞) = 0     bảng 1                ║
║      ϕ(x) Laplace = ∫ TỪ 0 đến x,    ϕ(∞) = 0,5   bảng 2   ← sách        ║
║      Φ(x) CDF       = ∫ TỪ −∞ đến x,   Φ(∞) = 1     Excel/Python         ║
║      Φ(x) = 0,5 + ϕ(x)                                                   ║
║                                                                          ║
║  ⭐⭐ CÔNG THỨC NỀN CỦA CẢ PHẦN THỐNG KÊ            (4.17b)              ║
║      Xᵢ ~ N(a, σ²) độc lập  ⟹  (X̄ − a)/(σ/√n) ~ N(0;1)                  ║
║                                                                          ║
║  XẤP XỈ NHỊ THỨC BẰNG CHUẨN  (np > 5 và nq > 5)                          ║
║      B(n,p) ≈ N(np, npq)                                                 ║
║      NHỚ HIỆU CHỈNH ±0,5 khi n chưa lớn → sai số giảm ~6 lần             ║
║                                                                          ║
║  BỐN PHÂN PHỐI CHO PHẦN THỐNG KÊ (bài 11–14)                             ║
║      χ²(n) = Σ Zᵢ²          EU = n,      VU = 2n     → phương sai        ║
║      t(n)  = Z/√(χ²/n)      ET = 0,      VT = n/(n−2) → kỳ vọng, σ ẩn    ║
║      F(n,m)= (χ²ₙ/n)/(χ²ₘ/m)                          → so 2 phương sai  ║
║      γ(r,λ)                 EX = r/λ,    VX = r/λ²   ; r=1 → mũ          ║
║      ⭐ (4.21): Σ(Xᵢ−X̄)²/σ² ~ χ²(n−1)  ← LÝ DO CHIA n−1                  ║
║                                                                          ║
║  💼 QTKD  nhị thức = chuyển đổi | Poisson = xếp hàng, sự cố              ║
║          hình học = CAC (bao nhiêu cuộc gọi/đơn)                         ║
║          siêu bội = QC lô nhỏ  | chuẩn = dung sai, Six Sigma             ║
║          ⚠ tiền/thời gian/số đếm hầu như KHÔNG chuẩn                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương II §4, tr. 56–78.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Thí dụ 4.5 (tr. 69): con số "kết quả thật 0,978" ứng với $P(4 \le X \le 13)$, không phải
  $P(4 < X < 13)$ như đề bài viết. Đã tính lại bằng máy ở mục 10.
- Sơ đồ quan hệ các phân phối (mục 4, 8) và cây quyết định (mục 9): dựng lại/bổ sung.
  Giáo trình có sơ đồ ở tr. 64 và tr. 76 nhưng bản quét không đọc được.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 6 — Kỳ vọng, phương sai và các số đặc trưng](bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md) ·
Bài sau: Bài 8 — Biến ngẫu nhiên hai chiều và hệ số tương quan
