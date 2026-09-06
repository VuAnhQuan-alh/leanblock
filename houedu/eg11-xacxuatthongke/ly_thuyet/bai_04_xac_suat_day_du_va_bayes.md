# Bài 4 — Xác suất đầy đủ và công thức Bayes

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương I §4**, tr. 29–38.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> 📌 **Cần đọc trước:** [Bài 3 — Xác suất có điều kiện](bai_03_xac_suat_co_dieu_kien_va_bernoulli.md)

Bài này khép lại Chương I bằng hai công thức đi liền nhau, chạy theo **hai chiều ngược nhau**:

- **Xác suất đầy đủ** — biết nguyên nhân, tính ra kết quả. *"Ba máy có tỷ lệ lỗi riêng, cả phân
  xưởng lỗi bao nhiêu?"*
- **Bayes** — thấy kết quả, truy ngược nguyên nhân. *"Bắt được một phế phẩm, nhiều khả năng do
  máy nào?"*

Công thức Bayes (1763) là công thức có ảnh hưởng lớn nhất trong toàn bộ giáo trình này. Nó là
nền của lọc thư rác, chẩn đoán y khoa, chấm điểm tín dụng, và mọi hệ thống học máy hiện đại.

## Mục lục

1. [Nhóm đầy đủ](#1-nhóm-đầy-đủ)
2. [Công thức xác suất đầy đủ](#2-công-thức-xác-suất-đầy-đủ)
3. [Công thức Bayes](#3-công-thức-bayes)
4. [Tiên nghiệm và hậu nghiệm](#4-tiên-nghiệm-và-hậu-nghiệm)
5. [Bốn thí dụ mẫu của giáo trình](#5-bốn-thí-dụ-mẫu-của-giáo-trình)
6. [📚 Nghịch lý tỷ lệ nền](#6--nghịch-lý-tỷ-lệ-nền)
7. [📚 Quy trình bốn bước giải bài Bayes](#7--quy-trình-bốn-bước-giải-bài-bayes)
8. [Code minh hoạ](#8-code-minh-hoạ)
9. [Tự thử](#9-tự-thử)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Nhóm đầy đủ

Cả hai công thức của bài này **bắt buộc** phải có nhóm đầy đủ. Không có nó thì không dùng được.

**Định nghĩa (tr. 29).** Nhóm sự kiện $A_1, A_2, \dots, A_n$ ($n \ge 2$) của một phép thử được gọi là
một **nhóm đầy đủ** nếu:

$$
\begin{aligned}
&\text{(i)} && A_i A_j = V \quad \forall i \ne j && \text{(xung khắc từng đôi)} \\
&\text{(ii)} && A_1 + A_2 + \cdots + A_n = U && \text{(phủ hết mọi khả năng)}
\end{aligned}
$$

Đọc bằng lời: trong phép thử **chỉ có thể xuất hiện một** sự kiện trong số $n$ sự kiện đó,
và **phải có một** sự kiện xuất hiện. Không chồng lấn, không bỏ sót.

Hai điều kiện này chính là định nghĩa của một **phân hoạch** (partition) trong lý thuyết tập hợp.

```
   ┌──────────────── Ω ──────────────┐
   │        │        │       │       │
   │   A₁   │   A₂   │   A₃  │   A₄  │    ← không chồng lấn (xung khắc)
   │        │        │       │       │    ← lấp kín Ω     (tổng = U)
   └────────┴────────┴───────┴───────┘
```

**Thí dụ 4.1 (tr. 29).** Gieo một con xúc sắc. $A_i$ = "xuất hiện mặt $i$ chấm".

- $\{A_i, i = \overline{1,6}\}$ là một nhóm đầy đủ (6 phần tử).
- Đặt $A = A_6$, khi đó $\overline{A} = A_1 + \cdots + A_5$, và $\{A, \overline{A}\}$
  **cũng là** một nhóm đầy đủ (2 phần tử).

Giáo trình nêu bốn nhận xét (tr. 30):

1. Tập tất cả các sự kiện sơ cấp luôn tạo nên một nhóm đầy đủ.
2. Tổng quát hơn: mọi **phân hoạch** của $\Omega$ đều là một nhóm đầy đủ.
3. $\{A, \overline{A}\}$ với $A$ tuỳ ý là **nhóm đầy đủ bé nhất** (chỉ 2 phần tử).
4. $\{U, V\}$ cũng là nhóm đầy đủ, gọi là **nhóm đầy đủ tầm thường** (vô dụng trong tính toán).

⚠️ **Đây là chỗ hỏng nhiều nhất khi làm bài.** Trước khi viết công thức, hãy kiểm hai điều kiện:

- Các trường hợp có thể **cùng xảy ra** không? Nếu có → chưa xung khắc, chia lại.
- Có tình huống nào **không rơi vào trường hợp nào** không? Nếu có → chưa đầy đủ, thiếu nhánh.

Cách kiểm nhanh nhất: **cộng các xác suất lại, phải đúng bằng 1.**

### 💼 Góc QTKD

| Cách chia khách hàng                                       | Có phải nhóm đầy đủ?                             |
| ---------------------------------------------------------- | ------------------------------------------------ |
| {khách mới, khách cũ}                                      | ✅ xung khắc, phủ hết                            |
| {miền Bắc, miền Trung, miền Nam}                           | ✅ nếu chỉ bán trong nước                        |
| {đến từ Facebook, đến từ Google, đến từ email}             | ❌ **thiếu** kênh trực tiếp, giới thiệu          |
| {khách mua ≥ 2 lần, khách chi ≥ 5 triệu}                   | ❌ **chồng lấn** — một người có thể thuộc cả hai |
| {máy I, máy II, máy III} nếu 3 máy sản xuất 100% sản lượng | ✅                                               |

Cách chia thứ ba là **lỗi thực tế cực kỳ phổ biến** trong báo cáo marketing: cộng tỷ lệ chuyển đổi
theo kênh mà quên nhóm "direct/organic", ra tổng không bằng 100% rồi tự hỏi tiền đi đâu.

Cách chia thứ tư sai vì chồng lấn — một khách hàng VIP mua 5 lần và chi 20 triệu sẽ bị **đếm hai lần**.

---

## 2. Công thức xác suất đầy đủ

**Bài toán (tr. 30).** Có nhóm đầy đủ $A_1, \dots, A_n$ và một sự kiện $H$ nào đó.
Biết các $P(A_i)$ và $P(H \mid A_i)$, tính $P(H)$.

**Dẫn dắt.** Vì $A_1 + \cdots + A_n = U$ nên

$$H = HU = H(A_1 + A_2 + \cdots + A_n) = HA_1 + HA_2 + \cdots + HA_n$$

Các số hạng $HA_i$ **xung khắc từng đôi** (vì $A_i$ xung khắc), nên cộng thẳng được:

$$P(H) = \sum_{i=1}^{n} P(HA_i)$$

Áp dụng công thức nhân (3.5) cho từng số hạng, $P(HA_i) = P(A_i)P(H \mid A_i)$:

$$\boxed{P(H) = \sum_{i=1}^{n} P(A_i)\, P(H \mid A_i)} \tag{4.1}$$

Đây là **công thức xác suất đầy đủ** (hay xác suất toàn phần).

**Cách hiểu — đây là một trung bình có trọng số:**

> $P(H)$ = trung bình của các $P(H \mid A_i)$, với trọng số là $P(A_i)$.

Ví dụ: nếu ba máy có tỷ lệ lỗi 1%, 0,5%, 0,2% thì tỷ lệ lỗi cả phân xưởng phải nằm **giữa 0,2% và 1%**,
nghiêng về máy nào sản xuất nhiều hơn. Con số nằm ngoài khoảng đó là chắc chắn sai — một cách
kiểm tra đáp án rất nhanh.

**Cây xác suất** — cách vẽ ra để không nhầm:

```
                            ┌── P(H|A₁) ──► H     ┐
              ┌── P(A₁) ────┤                     │
              │             └── 1−P(H|A₁) ──► H̄   │
              │                                   │
   Bắt đầu ───┼── P(A₂) ────┬── P(H|A₂) ──► H     ├──►  P(H) = tổng
              │             └── ...               │      các đường
              │                                   │      dẫn tới H
              └── P(A₃) ────┬── P(H|A₃) ──► H     ┘
                            └── ...

   Luật: đi DỌC một nhánh thì NHÂN.  Cộng các nhánh CÙNG dẫn tới H thì CỘNG.
```

---

## 3. Công thức Bayes

Giờ chạy ngược: đã biết $H$ xảy ra, tính $P(A_i \mid H)$.

Từ công thức nhân (3.5), viết $P(A_iH)$ theo hai chiều:

$$P(A_iH) = P(A_i)P(H \mid A_i) = P(H)P(A_i \mid H)$$

Chia hai vế cho $P(H)$:

$$P(A_i \mid H) = \frac{P(A_i)P(H \mid A_i)}{P(H)} \tag{4.2}$$

Thay $P(H)$ bằng công thức xác suất đầy đủ (4.1):

$$\boxed{P(A_i \mid H) = \frac{P(A_i)\,P(H \mid A_i)}{\displaystyle\sum_{j=1}^{n} P(A_j)\,P(H \mid A_j)}} \tag{4.3}$$

Đây là **công thức Bayes**.

**Đọc công thức:**

$$P(A_i \mid H) = \frac{\text{đường đi qua } A_i \text{ tới } H}{\text{tổng mọi đường tới } H}$$

Tử số là *một* nhánh của cây; mẫu số là *tổng tất cả* các nhánh dẫn tới $H$. Nói cách khác:
trong tất cả những lần $H$ xảy ra, có bao nhiêu phần là do $A_i$ gây ra.

Giáo trình nhấn mạnh ba điều (tr. 31–32):

1. **Bắt buộc phải có nhóm đầy đủ** để dùng (4.1) hoặc (4.3).
2. **Sự kiện $A_i$ cần tính xác suất phải là thành viên của nhóm đầy đủ.** Điều này *gợi ý cách
   chọn nhóm*: hãy chọn nhóm đầy đủ sao cho thứ bạn muốn hỏi nằm trong đó.
3. Nếu không có (hoặc rất khó xác định) nhóm đầy đủ, dùng (4.2) — nhưng khi đó việc tính $P(H)$
   sẽ khó hơn nhiều.

---

## 4. Tiên nghiệm và hậu nghiệm

Giáo trình đặt tên cho hai loại xác suất trong công thức (tr. 32):

|       | Ký hiệu         | Tên                                    | Nghĩa                           |
| ----- | --------------- | -------------------------------------- | ------------------------------- |
| Trước | $P(A_i)$        | **xác suất tiên nghiệm** (a priori)    | biết trước khi có thông tin mới |
| Sau   | $P(A_i \mid H)$ | **xác suất hậu nghiệm** (a posteriori) | sau khi đã quan sát thấy $H$    |

> "Công thức Bayes cho phép **đánh giá lại** xác suất xảy ra các $A_i$ sau khi đã có thêm thông tin
> về $H$." (tr. 32)

Câu này là toàn bộ tinh thần của Bayes, và cũng là lý do nó thống trị khoa học dữ liệu hiện đại:

$$\text{niềm tin cũ} \ \xrightarrow{\ \text{bằng chứng mới}\ } \ \text{niềm tin mới}$$

**Ba điều luôn đúng, dùng để kiểm tra kết quả:**

1. Tổng các hậu nghiệm luôn bằng 1: $\sum_i P(A_i \mid H) = 1$.
2. Nếu $P(H \mid A_i)$ **lớn hơn trung bình** thì hậu nghiệm của $A_i$ **tăng** so với tiên nghiệm.
3. Bằng chứng càng "đặc trưng" cho một nguyên nhân, hậu nghiệm càng dịch chuyển mạnh.

### 💼 Góc QTKD

Đây là bộ máy phía sau mọi hệ thống **chấm điểm** trong doanh nghiệp.

**Lead scoring** — chấm điểm khách hàng tiềm năng:

- Tiên nghiệm: 5% khách tải tài liệu sẽ trở thành khách hàng thật.
- Bằng chứng $H$: khách này mở email 4 lần và xem trang bảng giá.
- Biết rằng 60% khách *thật sự mua* có hành vi đó, còn trong nhóm không mua chỉ 8% có hành vi đó.

$$P(\text{sẽ mua} \mid H) = \frac{0{,}05 \cdot 0{,}60}{0{,}05 \cdot 0{,}60 + 0{,}95 \cdot 0{,}08} = \frac{0{,}030}{0{,}106} \approx 28{,}3\%$$

Từ 5% lên 28,3% — gấp gần 6 lần. Đây là con số để đội sale quyết định gọi ai trước.

**Lọc thư rác** cũng đúng công thức đó, chỉ đổi tên: $A_i$ = {rác, không rác},
$H$ = "email chứa từ *miễn phí*". Thuật toán Naive Bayes chỉ là (4.3) áp dụng cho hàng nghìn từ
cùng lúc, với giả thiết (biết là sai nhưng vẫn dùng) rằng các từ độc lập với nhau.

---

## 5. Bốn thí dụ mẫu của giáo trình

### Thí dụ 4.2 (tr. 30) — ba máy, và ý nghĩa thật của $P(H)$

> Một phân xưởng có 3 máy sản xuất cùng loại sản phẩm với tỷ lệ phế phẩm tương ứng 1%; 0,5% và 0,2%.
> Máy I sản xuất 35%, máy II 45%, máy III 20% sản lượng. Chọn hú hoạ một sản phẩm, tìm xác suất
> đó là phế phẩm.

*Giải.* $M_i$ = "sản phẩm do máy $i$ sản xuất". $\{M_i\}$ là nhóm đầy đủ vì
$0{,}35 + 0{,}45 + 0{,}20 = 1$. ✓ Gọi $H$ = "rút được phế phẩm":

$$P(H) = 0{,}35 \cdot 1\% + 0{,}45 \cdot 0{,}5\% + 0{,}20 \cdot 0{,}2\% = \mathbf{0{,}615\%}$$

Giáo trình bổ sung một câu quan trọng: **"Ý nghĩa của xác suất này là tỷ lệ phế phẩm của phân xưởng."**

Nghĩa là công thức xác suất đầy đủ không chỉ trả lời một câu đố — nó **tổng hợp chỉ số của cả hệ
thống từ chỉ số của từng bộ phận**. Kiểm nhanh: $0{,}615\%$ nằm giữa $0{,}2\%$ và $1\%$. ✓

### Thí dụ 4.2 chạy ngược — bài toán truy nguyên

Giáo trình dừng ở đó, nhưng câu hỏi tự nhiên tiếp theo là: **bắt được một phế phẩm, nhiều khả năng
do máy nào?** Áp (4.3):

| Máy | Tiên nghiệm $P(M_i)$ | Hậu nghiệm $P(M_i \mid H)$ |             |
| --- | -------------------: | -------------------------: | ----------- |
| I   |                 0,35 |                 **0,5691** | ↑ tăng mạnh |
| II  |                 0,45 |                     0,3659 | ↓ giảm      |
| III |                 0,20 |                     0,0650 | ↓ giảm mạnh |

**Máy II sản xuất nhiều nhất (45%) nhưng máy I mới là thủ phạm khả dĩ nhất (57%).** Vì máy I bẩn
gấp đôi máy II. Bằng chứng "đây là phế phẩm" đã đảo ngược thứ hạng.

💼 Đây chính là **truy nguyên nguồn lỗi** trong quản trị chất lượng. Khi có khiếu nại từ khách,
đừng điều tra dây chuyền lớn nhất — hãy điều tra dây chuyền có **tích $P(A_i) \times P(H \mid A_i)$**
lớn nhất.

### Thí dụ 4.3 (tr. 31) — chọn nhóm đầy đủ cho khéo

> Hai hộp áo: hộp I có 10 áo trong đó 1 phế phẩm, hộp II có 8 áo trong đó 2 phế phẩm.
> Lấy hú hoạ 1 áo từ hộp I bỏ sang hộp II, sau đó từ hộp II chọn hú hoạ 2 áo.
> Tìm xác suất cả 2 áo đó đều là phế phẩm.

*Giải.* Cái khó: **không biết chiếc áo chuyển sang là tốt hay phế**, mà điều đó đổi hẳn thành phần
hộp II. Giáo trình xử lý bằng cách lập nhóm đầy đủ **đúng ngay chỗ thiếu thông tin**:

$$A = \text{"áo chuyển là phế phẩm"}, \quad \overline{A} = \text{"áo chuyển là áo tốt"}$$

$$P(A) = \frac{1}{10}, \qquad P(\overline{A}) = \frac{9}{10}$$

Sau khi chuyển, hộp II có **9 áo**. Gọi $H$ = "2 áo cuối chọn ra đều là phế phẩm":

$$
P(H \mid A) = \frac{C_3^2}{C_9^2} = \frac{3}{36} = \frac{1}{12}, \qquad
P(H \mid \overline{A}) = \frac{C_2^2}{C_9^2} = \frac{1}{36}
$$

Áp (4.1):

$$P(H) = \frac{1}{10}\cdot\frac{1}{12} + \frac{9}{10}\cdot\frac{1}{36} = \frac{1}{120} + \frac{1}{40} = \mathbf{\frac{1}{30}}$$

**Bài học lớn nhất của thí dụ này:** khi bài toán có một mắt xích **không biết**, hãy dựng nhóm đầy đủ
ngay tại mắt xích đó rồi tính từng nhánh. Đây là kỹ thuật dùng lại ở mọi bài toán nhiều giai đoạn.

💼 Cùng cấu trúc: một lô hàng nhập về **không rõ từ nhà cung cấp nào** (70% khả năng nhà A tỷ lệ lỗi
2%, 30% khả năng nhà B tỷ lệ lỗi 6%). Kiểm 3 sản phẩm, xác suất phát hiện lỗi là bao nhiêu?
Lập nhóm {A, B}, tính từng nhánh, cộng lại — y hệt.

### Thí dụ 4.4 (tr. 32) — mạch nối tiếp

> Mạch điện gồm 2 bộ phận mắc nối tiếp, xác suất làm việc tốt là 0,95 và 0,98. Thấy mạch ngừng
> làm việc; tìm xác suất **chỉ bộ phận thứ hai** hỏng.

*Giải.* Nối tiếp → chỉ cần một bộ phận hỏng là mạch chết. Có 4 khả năng, và chúng tạo nhóm đầy đủ:

|       | Trạng thái     |                        $P(B_i)$ | $P(H \mid B_i)$ |
| ----- | -------------- | ------------------------------: | --------------: |
| $B_0$ | cả hai tốt     | $0{,}95 \cdot 0{,}98 = 0{,}931$ |           **0** |
| $B_1$ | I tốt, II hỏng | $0{,}95 \cdot 0{,}02 = 0{,}019$ |               1 |
| $B_2$ | II tốt, I hỏng | $0{,}05 \cdot 0{,}98 = 0{,}049$ |               1 |
| $B_3$ | cả hai hỏng    | $0{,}05 \cdot 0{,}02 = 0{,}001$ |               1 |

Kiểm: $0{,}931 + 0{,}019 + 0{,}049 + 0{,}001 = 1$. ✓ Với $H$ = "mạch không làm việc":

$$P(H) = 0 + 0{,}019 + 0{,}049 + 0{,}001 = 0{,}069$$

$$P(B_1 \mid H) = \frac{0{,}019}{0{,}069} = \mathbf{\frac{19}{69}} \approx 0{,}275$$

Chú ý cột $P(H \mid B_i)$ chỉ gồm 0 và 1 — trạng thái quyết định hoàn toàn kết quả. Trường hợp này
rất hay gặp và làm công thức trở nên đơn giản: **Bayes thu về "tỷ lệ giữa các trạng thái gây ra $H$"**.

Giáo trình còn chỉ ra có thể dùng (4.2) mà không cần nhóm đầy đủ, viết
$H = A_1\overline{A_2} + \overline{A_1}A_2 + \overline{A_1}\,\overline{A_2}$ rồi tính $P(H) = 0{,}069$ —
nhưng "mọi khó khăn rơi vào việc tính trực tiếp $P(H)$" (tr. 33).

### Thí dụ 4.5 (tr. 33) — bài khó nhất chương I

> Tại một phòng khám chuyên khoa, tỷ lệ người đến khám **có bệnh là 83%**. Theo thống kê, nếu
> **chẩn đoán có bệnh thì đúng tới 90%**, còn nếu **chẩn đoán không bệnh thì chỉ đúng 80%**.
> a) Tính xác suất chẩn đoán đúng. b) Biết có một trường hợp chẩn đoán đúng; tìm xác suất người
> được chẩn đoán đúng có bệnh.

*Giải.* Đặt tên cẩn thận — đây là chỗ cả bài phụ thuộc vào:

| Ký hiệu              | Nghĩa                                               |
| -------------------- | --------------------------------------------------- |
| $A$ / $\overline{A}$ | người **có** bệnh / **không** có bệnh               |
| $B$ / $\overline{B}$ | bác sĩ **chẩn đoán** có bệnh / chẩn đoán không bệnh |
| $H$ / $\overline{H}$ | chẩn đoán **đúng** / chẩn đoán sai                  |

⚠️ **Chỗ bẫy:** thử dùng nhóm $\{A, \overline{A}\}$:

$$P(H) = P(A)P(H \mid A) + P(\overline{A})P(H \mid \overline{A})$$

Nhưng $P(H \mid A)$ = "khi người *có* bệnh thì chẩn đoán đúng" — **chưa biết**! Đề cho
$P(H \mid B) = 0{,}9$, tức là "khi *chẩn đoán* có bệnh thì đúng". Giáo trình cảnh báo thẳng:
*"chú ý phân biệt với xác suất chẩn đoán có bệnh thì đúng là $P(H \mid B)$"* (tr. 34).

Vậy phải chuyển sang nhóm $\{B, \overline{B}\}$:

$$P(H) = P(B)P(H \mid B) + P(\overline{B})P(H \mid \overline{B}) \tag{4.4}$$

Nhưng $P(B)$ cũng chưa biết! Giáo trình khai thác một công thức nữa (nhóm $\{B, \overline{B}\}$
áp cho $A$):

$$P(A) = P(B)P(A \mid B) + P(\overline{B})P(A \mid \overline{B}) \tag{4.5}$$

Bây giờ dịch dữ kiện thành các số hạng của (4.5):

- "Chẩn đoán có bệnh thì đúng 90%" nghĩa là *chẩn đoán có bệnh, và người đó thật sự có bệnh*:
  $P(A \mid B) = P(H \mid B) = 0{,}9$.
- "Chẩn đoán không bệnh thì đúng 80%" nghĩa là $P(\overline{A} \mid \overline{B}) = P(H \mid \overline{B}) = 0{,}8$,
  suy ra $P(A \mid \overline{B}) = 1 - 0{,}8 = 0{,}2$.

Đặt $P(B) = x$, thay vào (4.5) với $P(A) = 0{,}83$:

$$0{,}83 = 0{,}9x + 0{,}2(1-x) \iff 0{,}83 = 0{,}7x + 0{,}2 \iff x = 0{,}9$$

**a)** Thay vào (4.4):

$$P(H) = 0{,}9 \cdot 0{,}9 + 0{,}1 \cdot 0{,}8 = 0{,}81 + 0{,}08 = \mathbf{0{,}89}$$

**b)** Cần $P(A \mid H)$. Dùng (4.2), và nhận ra $P(H \mid A)P(A) = P(HA) = P(B)P(A \mid B)$
(vì "chẩn đoán đúng **và** có bệnh" chính là "chẩn đoán có bệnh **và** có bệnh"):

$$P(A \mid H) = \frac{P(B)P(A \mid B)}{P(H)} = \frac{0{,}9 \cdot 0{,}9}{0{,}89} = \frac{81}{89} \approx \mathbf{0{,}9101}$$

**Vì sao thí dụ này khó?** Vì phải **đổi nhóm đầy đủ giữa chừng**, và phải phân biệt bốn xác suất
có điều kiện nghe rất giống nhau:

$$P(H \mid A) \ne P(H \mid B) \ne P(A \mid H) \ne P(A \mid B)$$

Bài học: **luôn viết bảng ký hiệu ra giấy trước khi tính.** Mất 30 giây, cứu cả bài.

---

## 6. 📚 Nghịch lý tỷ lệ nền

Giáo trình chạm vào chủ đề này qua thí dụ 4.5 và bài tập 33 (tr. 38) nhưng không đặt tên và không
nhấn mạnh. Đây là **hệ quả quan trọng nhất của công thức Bayes trong thực tế**.

**Bài toán.** Một xét nghiệm có độ nhạy 99% (người bệnh thì 99% ra dương tính) và độ đặc hiệu 99%
(người khoẻ thì 99% ra âm tính). Bạn xét nghiệm và **ra dương tính**. Xác suất bạn thật sự bị bệnh
là bao nhiêu?

Câu trả lời trực giác là "99%". Câu trả lời đúng là: **phụ thuộc hoàn toàn vào tỷ lệ mắc bệnh
trong dân số**.

|       Tỷ lệ mắc bệnh | $P(\text{bệnh} \mid \text{dương tính})$ |
| -------------------: | --------------------------------------: |
|               0,001% |                               **0,10%** |
|                0,01% |                                   0,98% |
|                 0,1% |                                   9,02% |
|                   1% |                              **50,00%** |
|                  10% |                                  91,67% |
| 83% (như thí dụ 4.5) |                                  99,79% |

Với bệnh hiếm (tỷ lệ 0,1%), xét nghiệm 99% chính xác mà dương tính thì **chỉ 9% khả năng thật sự
bệnh** — 91% là báo động giả.

**Vì sao?** Vì trong 1 triệu người: 1.000 người bệnh (990 dương tính đúng) và 999.000 người khoẻ
(9.990 dương tính **sai**). Số báo động giả gấp 10 lần số ca thật, đơn giản vì nhóm khoẻ đông hơn
quá nhiều.

$$P(\text{bệnh} \mid +) = \frac{990}{990 + 9\,990} = 9{,}02\%$$

**Tỷ lệ nền (base rate) chi phối kết quả mạnh hơn cả độ chính xác của xét nghiệm.** Bỏ qua nó gọi là
**nguỵ biện tỷ lệ nền** (base rate fallacy).

### 💼 Góc QTKD — nơi sai lầm này đốt tiền thật

**Phát hiện gian lận thẻ tín dụng.** Tỷ lệ giao dịch gian lận thật sự khoảng 0,1%. Một mô hình
"chính xác 99%" sẽ chặn nhầm 10 giao dịch hợp lệ cho mỗi 1 giao dịch gian lận bắt được. Khách hàng
bị khoá thẻ oan sẽ bỏ ngân hàng. Đó là lý do các hệ thống thật phải đánh đổi: chấp nhận bỏ lọt
một phần gian lận để giảm báo động giả.

**Tuyển dụng.** Một bài test "dự đoán nhân viên xuất sắc với độ chính xác 90%". Nếu chỉ 5% ứng viên
thật sự xuất sắc, thì trong số người pass test chỉ có $\frac{0{,}05 \cdot 0{,}9}{0{,}05 \cdot 0{,}9 + 0{,}95 \cdot 0{,}1} = 32\%$
là xuất sắc thật. Hai phần ba số người bạn tuyển vì "pass bài test" là dương tính giả.

**Cảnh báo churn.** Hệ thống cảnh báo "khách sắp rời bỏ" chạy trên tập khách hàng mà chỉ 3% thật sự
rời bỏ mỗi tháng — hầu hết cảnh báo sẽ là giả, và đội chăm sóc khách hàng sẽ nhanh chóng học cách
phớt lờ chúng.

**Quy tắc thực hành:** trước khi mua bất kỳ công cụ nào quảng cáo "độ chính xác X%", hãy hỏi
**tỷ lệ nền là bao nhiêu**, rồi tự tính hậu nghiệm bằng (4.3). Nếu người bán không trả lời được
câu hỏi đó, họ chưa hiểu sản phẩm của chính mình.

---

## 7. 📚 Quy trình bốn bước giải bài Bayes

Tổng hợp từ bốn thí dụ trên, để làm bài không lạc:

**Bước 1 — Đặt tên và viết bảng ký hiệu.**
Phân biệt rõ *nguyên nhân* ($A_i$) và *bằng chứng quan sát được* ($H$). Nếu đề có hai chiều dễ nhầm
(có bệnh / chẩn đoán có bệnh), viết cả hai ra giấy.

**Bước 2 — Dựng nhóm đầy đủ, và kiểm.**
Nhóm phải **chứa thứ đề hỏi**. Cộng $\sum P(A_i)$, phải bằng đúng 1. Không bằng 1 → dừng, chia lại.

**Bước 3 — Điền hai cột số.**
Cột tiên nghiệm $P(A_i)$ và cột khả năng $P(H \mid A_i)$. Chú ý cột thứ hai **không cần cộng bằng 1**
— đây là chỗ nhầm phổ biến.

**Bước 4 — Chọn công thức theo chiều câu hỏi.**

| Đề hỏi                                     | Dùng                  |
| ------------------------------------------ | --------------------- |
| "tỷ lệ chung của cả hệ thống là bao nhiêu" | (4.1) xác suất đầy đủ |
| "xác suất xảy ra $H$"                      | (4.1)                 |
| "**biết** đã có $H$, xác suất do $A_i$"    | (4.3) Bayes          |
| "thấy kết quả, truy ngược nguyên nhân"     | (4.3)                 |

**Từ khoá nhận diện:** đề có chữ **"biết rằng"**, **"đã thấy"**, **"phát hiện"** đứng trước một kết
quả rồi mới hỏi về nguyên nhân → chắc chắn là Bayes.

**Kiểm tra cuối:** tổng các hậu nghiệm $\sum_i P(A_i \mid H)$ phải bằng 1.

---

## 8. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-04-bayet.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.

Toàn bộ bài này gói vào **hai hàm 5 dòng**. Chú ý dòng `assert` trong `total_probability` —
nó chính là bước kiểm "nhóm có đầy đủ không" ở mục 7, để máy bắt lỗi hộ bạn.

```python
"""Bài 4 — Công thức xác suất đầy đủ và công thức Bayes."""

from fractions import Fraction
from math import comb

# ─────────────────────────────────────────────────────────────
# Hai hàm dùng chung cho cả bài. Nhóm đầy đủ đưa vào dưới dạng
# danh sách (tên, P(Ai), P(H|Ai)).
# ─────────────────────────────────────────────────────────────
def total_probability(group):
    """Cong thuc (4.1): P(H) = sum P(Ai) * P(H|Ai)."""
    assert sum(prior for _, prior, _ in group) == 1, "nhom chua day du!"
    return sum(prior * lik for _, prior, lik in group)


def bayes(group):
    """Cong thuc (4.3): tra ve dict {ten: P(Ai|H)}."""
    ph = total_probability(group)
    return {name: prior * lik / ph for name, prior, lik in group}


# ─────────────────────────────────────────────────────────────
# 1. Thí dụ 4.2 (tr. 30) — ba máy, tìm tỷ lệ phế phẩm phân xưởng
# ─────────────────────────────────────────────────────────────
machines = [
    ("May I  ", Fraction(35, 100), Fraction(1, 100)),
    ("May II ", Fraction(45, 100), Fraction(5, 1000)),
    ("May III", Fraction(20, 100), Fraction(2, 1000)),
]
ph = total_probability(machines)
print("THI DU 4.2 — ty le phe pham cua phan xuong")
print(f"{'Nhom day du':<10}{'P(Mi)':>10}{'P(H|Mi)':>12}{'tich':>14}")
for name, prior, lik in machines:
    print(f"{name:<10}{float(prior):>10.2f}{float(lik):>12.4f}{float(prior * lik):>14.6f}")
print(f"{'P(H) =':<10}{'':>10}{'':>12}{float(ph):>14.6f}"
      f"  = {float(ph) * 100:.3f}%   (sach: 0,615%)")

# Bayes ngược: bắt được 1 phế phẩm, khả năng do máy nào?
print()
print("Bayes nguoc — bat duoc 1 phe pham, do may nao?")
post = bayes(machines)
for name, prior, _ in machines:
    print(f"  {name}  tien nghiem {float(prior):.2f}"
          f"  ->  hau nghiem {float(post[name]):.4f}"
          f"   ({'tang' if post[name] > prior else 'giam'})")
assert abs(sum(post.values()) - 1) < 1e-12

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 4.3 (tr. 31) — chuyển 1 áo từ hộp I sang hộp II
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.3 — hop I (10 ao, 1 phe), hop II (8 ao, 2 phe)")
shirts = [
    ("ao chuyen la PHE ", Fraction(1, 10), Fraction(comb(3, 2), comb(9, 2))),
    ("ao chuyen la TOT ", Fraction(9, 10), Fraction(comb(2, 2), comb(9, 2))),
]
for name, prior, lik in shirts:
    print(f"  {name}  P = {prior}   P(H|.) = {lik}")
print("  P(ca 2 ao cuoi deu phe) =", total_probability(shirts), "  (sach: 1/30)")
assert total_probability(shirts) == Fraction(1, 30)

# ─────────────────────────────────────────────────────────────
# 3. Thí dụ 4.4 (tr. 32) — mạch 2 bộ phận nối tiếp, 0,95 và 0,98
#    Mạch ngừng làm việc; xác suất CHỈ bộ phận thứ hai hỏng?
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.4 — mach 2 bo phan noi tiep (0,95 va 0,98), mach da chet")
g1, g2 = Fraction(95, 100), Fraction(98, 100)
states = [
    ("B0 ca hai tot   ", g1 * g2, Fraction(0)),        # mach van chay -> P(H|B0)=0
    ("B1 I tot, II hong", g1 * (1 - g2), Fraction(1)),
    ("B2 II tot, I hong", (1 - g1) * g2, Fraction(1)),
    ("B3 ca hai hong  ", (1 - g1) * (1 - g2), Fraction(1)),
]
for name, prior, lik in states:
    print(f"  {name}  P = {float(prior):.4f}   P(H|.) = {lik}")
ph4 = total_probability(states)
print("  P(mach chet) =", ph4, "=", float(ph4))
post4 = bayes(states)
print("  P(chi bo phan II hong | mach chet) =", post4["B1 I tot, II hong"],
      "  (sach: 19/69)")
assert post4["B1 I tot, II hong"] == Fraction(19, 69)

# ─────────────────────────────────────────────────────────────
# 4. Thí dụ 4.5 (tr. 33) — phòng khám chuyên khoa
#    83% người đến khám CÓ bệnh. Chẩn đoán "có bệnh" đúng 90%,
#    chẩn đoán "không bệnh" đúng 80%. Tìm P(chan doan dung).
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 4.5 — phong kham, P(co benh) = 0,83")
# Chua biet P(B) = P(chan doan co benh). Giai phuong trinh (4.5):
#   P(A) = P(B)P(A|B) + P(B ngang)P(A|B ngang)
#   0,83 = 0,9x + 0,2(1 - x)
x = (Fraction(83, 100) - Fraction(2, 10)) / (Fraction(9, 10) - Fraction(2, 10))
print("  Giai 0,83 = 0,9x + 0,2(1-x)  ->  P(chan doan co benh) = x =", x)
assert x == Fraction(9, 10)

diagnosis = [
    ("chan doan CO benh   ", x, Fraction(9, 10)),
    ("chan doan KHONG benh", 1 - x, Fraction(8, 10)),
]
ph5 = total_probability(diagnosis)
print("  a) P(chan doan dung) =", ph5, "=", float(ph5), "  (sach: 0,89)")
post5 = bayes(diagnosis)
print("  b) P(nguoi do CO benh | chan doan dung) =",
      post5["chan doan CO benh   "], "=", round(float(post5["chan doan CO benh   "]), 4),
      "  (sach: 0,91)")

# ─────────────────────────────────────────────────────────────
# 5. 📚 NGHỊCH LÝ TỶ LỆ NỀN — cùng một xét nghiệm, đổi tỷ lệ mắc
#    Độ nhạy 99%, độ đặc hiệu 99%. Dương tính thì thật sự bệnh bao nhiêu %?
# ─────────────────────────────────────────────────────────────
print()
print("📚 NGHICH LY TY LE NEN — xet nghiem do nhay 99%, do dac hieu 99%")
print(f"{'ty le mac benh':>16}{'P(benh | duong tinh)':>24}")
for rate in [Fraction(1, 100000), Fraction(1, 10000), Fraction(1, 1000),
             Fraction(1, 100), Fraction(1, 10), Fraction(83, 100)]:
    grp = [("benh   ", rate, Fraction(99, 100)),
           ("khong  ", 1 - rate, Fraction(1, 100))]
    p = bayes(grp)["benh   "]
    print(f"{float(rate) * 100:>15.3f}%{float(p) * 100:>23.2f}%")
```

Kết quả chạy thật:

```
THI DU 4.2 — ty le phe pham cua phan xuong
Nhom day du     P(Mi)     P(H|Mi)          tich
May I           0.35      0.0100      0.003500
May II          0.45      0.0050      0.002250
May III         0.20      0.0020      0.000400
P(H) =                                0.006150  = 0.615%   (sach: 0,615%)

Bayes nguoc — bat duoc 1 phe pham, do may nao?
  May I    tien nghiem 0.35  ->  hau nghiem 0.5691   (tang)
  May II   tien nghiem 0.45  ->  hau nghiem 0.3659   (giam)
  May III  tien nghiem 0.20  ->  hau nghiem 0.0650   (giam)

THI DU 4.3 — hop I (10 ao, 1 phe), hop II (8 ao, 2 phe)
  ao chuyen la PHE   P = 1/10   P(H|.) = 1/12
  ao chuyen la TOT   P = 9/10   P(H|.) = 1/36
  P(ca 2 ao cuoi deu phe) = 1/30   (sach: 1/30)

THI DU 4.4 — mach 2 bo phan noi tiep (0,95 va 0,98), mach da chet
  B0 ca hai tot     P = 0.9310   P(H|.) = 0
  B1 I tot, II hong  P = 0.0190   P(H|.) = 1
  B2 II tot, I hong  P = 0.0490   P(H|.) = 1
  B3 ca hai hong    P = 0.0010   P(H|.) = 1
  P(mach chet) = 69/1000 = 0.069
  P(chi bo phan II hong | mach chet) = 19/69   (sach: 19/69)

THI DU 4.5 — phong kham, P(co benh) = 0,83
  Giai 0,83 = 0,9x + 0,2(1-x)  ->  P(chan doan co benh) = x = 9/10
  a) P(chan doan dung) = 89/100 = 0.89   (sach: 0,89)
  b) P(nguoi do CO benh | chan doan dung) = 81/89 = 0.9101   (sach: 0,91)

📚 NGHICH LY TY LE NEN — xet nghiem do nhay 99%, do dac hieu 99%
  ty le mac benh    P(benh | duong tinh)
          0.001%                   0.10%
          0.010%                   0.98%
          0.100%                   9.02%
          1.000%                  50.00%
         10.000%                  91.67%
         83.000%                  99.79%
```

Ba điểm đáng để ý:

1. **Toàn bộ 4 thí dụ của giáo trình dùng chung đúng hai hàm.** Cấu trúc toán học giống hệt nhau,
   chỉ đổi ba con số đầu vào. Nhận ra được điều này thì không còn sợ dạng bài Bayes nữa.
2. **`Fraction` cho ra `1/30`, `19/69`, `81/89`** — đúng dạng đáp án của giáo trình, không phải
   số thập phân làm tròn.
3. **Bảng tỷ lệ nền ở cuối**: cùng một xét nghiệm 99%, hậu nghiệm chạy từ **0,1%** đến **99,79%**
   chỉ vì đổi tỷ lệ nền. Đó là toàn bộ nội dung mục 6 gói trong 6 dòng.

---

## 9. Tự thử

1. Ở thí dụ 4.2, đổi sản lượng thành máy I 10%, máy II 70%, máy III 20% (giữ nguyên tỷ lệ lỗi).
   Tỷ lệ phế phẩm phân xưởng đổi thế nào? Thủ phạm khả dĩ nhất còn là máy I không?
2. Vẫn thí dụ 4.2, đổi `Fraction(20, 100)` thành `Fraction(25, 100)` (tổng thành 1,05).
   Chương trình báo lỗi gì? Đọc thông điệp của `assert` — đó là bước 2 trong quy trình mục 7.
3. Ở thí dụ 4.3, đổi thành "chuyển **2 áo** từ hộp I sang hộp II". Nhóm đầy đủ giờ có mấy nhánh?
   Viết lại `shirts` cho đúng rồi tính.
4. Trong bảng tỷ lệ nền, đổi độ nhạy/độ đặc hiệu từ 99% lên **99,9%**. Với tỷ lệ mắc 0,1%,
   hậu nghiệm lên bao nhiêu? Cải thiện xét nghiệm có bù được tỷ lệ nền thấp không?
5. Áp bài toán lead scoring ở mục 4 vào code: tiên nghiệm 5%, $P(H \mid \text{mua}) = 0{,}60$,
   $P(H \mid \text{không mua}) = 0{,}08$. Có ra 28,3% không?
6. Bài 29 (tr. 38): tỷ lệ hút thuốc 35%; viêm họng trong nhóm hút thuốc 60%, nhóm không hút 30%.
   Người bị viêm họng thì xác suất hút thuốc? Người **không** viêm họng thì bao nhiêu?
   (Chỉ cần đổi ba con số trong `machines`.)

---

## 10. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)      | Tiếng Anh                             | Ghi chú                           |
| ---------------------------- | ------------------------------------- | --------------------------------- |
| Nhóm đầy đủ, hệ thống đầy đủ | Partition / Complete system of events | xung khắc từng đôi + tổng $= U$   |
| Nhóm đầy đủ tầm thường       | Trivial partition                     | $\{U, V\}$                        |
| Công thức xác suất đầy đủ    | Law of total probability              | (4.1)                             |
| Xác suất toàn phần           | Total probability                     | tên gọi khác của (4.1)            |
| Công thức Bayes             | Bayes' theorem / Bayes' rule          | (4.3)                             |
| Xác suất tiên nghiệm         | Prior probability                     | $P(A_i)$, biết trước              |
| Xác suất hậu nghiệm          | Posterior probability                 | $P(A_i \mid H)$, sau khi thấy $H$ |
| Khả năng (của bằng chứng)    | Likelihood                            | $P(H \mid A_i)$                   |
| Tỷ lệ nền                    | Base rate                             | 📚 mục 6                          |
| Nguỵ biện tỷ lệ nền          | Base rate fallacy                     | 📚 mục 6                          |
| Độ nhạy                      | Sensitivity, true positive rate       | $P(+ \mid \text{bệnh})$           |
| Độ đặc hiệu                  | Specificity, true negative rate       | $P(- \mid \text{khoẻ})$           |
| Dương tính giả               | False positive                        | $P(+ \mid \text{khoẻ})$           |

⚠️ **Ba xác suất dễ nhầm nhất**, luôn viết ra giấy trước khi tính:

$$P(H \mid A) \quad \ne \quad P(A \mid H) \quad \ne \quad P(A H)$$

- $P(H \mid A)$ — biết nguyên nhân, hỏi kết quả (**likelihood**, đề thường cho).
- $P(A \mid H)$ — biết kết quả, hỏi nguyên nhân (**hậu nghiệm**, đề thường hỏi).
- $P(AH)$ — cả hai cùng xảy ra (**xác suất đồng thời**, là tử số của Bayes).

---

## 11. Câu hỏi tự kiểm tra

1. Vì sao công thức (4.1) và (4.3) **bắt buộc** phải có nhóm đầy đủ? Điều gì hỏng nếu nhóm bị
   chồng lấn? Điều gì hỏng nếu nhóm bị thiếu nhánh?
2. Cột $P(A_i)$ phải cộng bằng 1. Cột $P(H \mid A_i)$ có phải cộng bằng 1 không? Giải thích.
3. Trong thí dụ 4.2, vì sao máy II sản xuất nhiều nhất mà hậu nghiệm lại thấp hơn máy I?
   Điều gì phải thay đổi để máy II thành thủ phạm khả dĩ nhất?
4. Hai kho hàng: kho A chứa 60% tồn kho với tỷ lệ hư hỏng 3%, kho B chứa 40% với tỷ lệ 8%.
   a) Tỷ lệ hư hỏng toàn công ty?
   b) Nhận được một khiếu nại hàng hỏng, khả năng hàng từ kho nào cao hơn?
5. Ngân hàng duyệt vay: 20% hồ sơ là rủi ro cao. Mô hình chấm điểm gắn cờ đỏ cho 85% hồ sơ rủi ro
   cao và 10% hồ sơ rủi ro thấp. Một hồ sơ bị gắn cờ đỏ — xác suất nó thật sự rủi ro cao?
   Con số này có đủ để từ chối cho vay không?
6. Vì sao trong thí dụ 4.5 **không dùng được** nhóm $\{A, \overline{A}\}$? Phân biệt $P(H \mid A)$
   và $P(H \mid B)$ bằng lời.
7. Một công cụ marketing quảng cáo "dự đoán khách sắp huỷ dịch vụ với độ chính xác 95%".
   Tỷ lệ huỷ thực tế là 2%/tháng. Trong 10.000 khách, mỗi tháng công cụ gắn cờ bao nhiêu người,
   và bao nhiêu trong số đó thật sự sắp huỷ? Có nên mua công cụ này không?
8. Bài 33 (tr. 38): tỷ lệ mắc bệnh A là 15%. Nếu không bị bệnh thì phản ứng dương tính chỉ 10%.
   Biết rằng khi phản ứng dương tính thì xác suất bị bệnh là 60%.
   a) Tính xác suất phản ứng dương tính của nhóm có bệnh.
   b) Tính xác suất chẩn đoán đúng.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 4 — XÁC SUẤT ĐẦY ĐỦ VÀ CÔNG THỨC BAYES      (Ch. I §4, tr. 29–38)   ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  NHÓM ĐẦY ĐỦ  A₁, A₂, ..., Aₙ                                            ║
║      (i)  AᵢAⱼ = V  ∀ i ≠ j        xung khắc từng đôi, không chồng lấn   ║
║      (ii) A₁ + A₂ + ... + Aₙ = U   phủ hết, không bỏ sót                 ║
║      KIỂM NHANH:  Σ P(Aᵢ) phải bằng đúng 1                               ║
║      ⚠ KHÔNG có nhóm đầy đủ thì KHÔNG dùng được cả hai công thức         ║
║                                                                          ║
║  ── CHIỀU XUÔI: biết nguyên nhân → tính kết quả ────────────────────     ║
║                                                                          ║
║  XÁC SUẤT ĐẦY ĐỦ      P(H) = Σ P(Aᵢ) · P(H|Aᵢ)                 (4.1)     ║
║      = trung bình có trọng số của các P(H|Aᵢ)                            ║
║      → P(H) luôn nằm GIỮA min và max của các P(H|Aᵢ)                     ║
║                                                                          ║
║  ── CHIỀU NGƯỢC: thấy kết quả → truy nguyên nhân ───────────────────     ║
║                                                                          ║
║  BAYES      P(Aᵢ|H) =    P(Aᵢ) · P(H|Aᵢ)                       (4.3)     ║
║                        ─────────────────────                             ║
║                        Σⱼ P(Aⱼ) · P(H|Aⱼ)                                ║
║                                                                          ║
║      tử  = MỘT đường qua Aᵢ tới H                                        ║
║      mẫu = TỔNG MỌI đường tới H                                          ║
║      KIỂM: Σ P(Aᵢ|H) = 1                                                 ║
║                                                                          ║
║  BA TÊN GỌI                                                              ║
║      P(Aᵢ)     tiên nghiệm  prior       biết trước                       ║
║      P(H|Aᵢ)   khả năng     likelihood  đề thường CHO                    ║
║      P(Aᵢ|H)   hậu nghiệm   posterior   đề thường HỎI                    ║
║      ⚠ P(H|A) ≠ P(A|H) ≠ P(AH)  — viết bảng ký hiệu trước khi tính       ║
║                                                                          ║
║  QUY TRÌNH 4 BƯỚC                                                        ║
║      1. đặt tên, phân biệt nguyên nhân Aᵢ vs bằng chứng H                ║
║      2. dựng nhóm đầy đủ CHỨA thứ đề hỏi, kiểm Σ P(Aᵢ) = 1               ║
║      3. điền 2 cột: tiên nghiệm + khả năng                               ║
║      4. đề hỏi "tỷ lệ chung" → (4.1) | "biết đã có H" → (4.3)            ║
║      TỪ KHOÁ NHẬN DIỆN BAYES:  "biết rằng", "đã thấy", "phát hiện"       ║
║                                                                          ║
║  📚 NGHỊCH LÝ TỶ LỆ NỀN                                                  ║
║      xét nghiệm 99% + bệnh hiếm 0,1%  →  dương tính chỉ 9% là thật       ║
║      TỶ LỆ NỀN chi phối mạnh hơn ĐỘ CHÍNH XÁC                            ║
║                                                                          ║
║  💼 QTKD  lead scoring, lọc thư rác, chấm điểm tín dụng = (4.3)          ║
║          truy nguyên lỗi: xét tích P(Aᵢ)·P(H|Aᵢ), không xét sản lượng    ║
║          mua công cụ "chính xác X%" → HỎI TỶ LỆ NỀN trước                ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương I §4, tr. 29–38.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Nghịch lý tỷ lệ nền (mục 6) và quy trình 4 bước (mục 7): kiến thức bổ sung, không có trong giáo trình.
  Giáo trình chạm tới qua thí dụ 4.5 và bài tập 33 (tr. 38) nhưng không đặt tên.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 3 — Xác suất có điều kiện và công thức Bernoulli](bai_03_xac_suat_co_dieu_kien_va_bernoulli.md) ·
Bài sau: Bài 5 — Biến ngẫu nhiên và luật phân phối
