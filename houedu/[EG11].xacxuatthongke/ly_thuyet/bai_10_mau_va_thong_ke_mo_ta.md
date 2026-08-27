# Bài 10 — Mẫu và thống kê mô tả

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương IV §1–§2**, tr. 113–133.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính ba lỗi số học** trong thí dụ 2.4 (tr. 132).
> 📌 **Cần đọc trước:** [Bài 6](bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md) · [Bài 9](bai_09_luat_so_lon_va_dinh_ly_gioi_han_trung_tam.md)
> 📊 **Dữ liệu:** bài này bắt đầu dùng file `.csv` trong [thuc_hanh/du_lieu/](../thuc_hanh/du_lieu/doanh_thu_ngay.csv)

**Đây là bản lề của cả khoá học.** Chín bài trước đi theo chiều **xuôi**: biết luật phân phối,
tính ra xác suất. Từ bài này đi theo chiều **ngược**: có dữ liệu, suy ra luật phân phối.

Giáo trình mở Chương IV bằng định nghĩa (tr. 113):

> "Thống kê... là một **khoa học về phân tích dữ liệu** (bao gồm cả thu nhập và xử lý) nhằm thu nhận
> thông tin chân thực về đối tượng nghiên cứu với **một độ tin cậy nhất định** và rút ra những kết
> luận hợp lý."

Và nêu **hai điều kiện** để bài toán thống kê xuất hiện:

1. có **nhiều tình huống** cần phải lựa chọn;
2. có **thông tin** về các tình huống thông qua dữ liệu thống kê.

💼 Đúng mô tả công việc của một nhà quản trị: nhiều phương án, có số liệu, phải chọn.

## Mục lục

1. [Mẫu và tập nền](#1-mẫu-và-tập-nền)
2. [Bốn cách chọn mẫu](#2-bốn-cách-chọn-mẫu)
3. [Tần số, tần suất và bảng phân phối thực nghiệm](#3-tần-số-tần-suất-và-bảng-phân-phối-thực-nghiệm)
4. [Mẫu ngẫu nhiên và thống kê](#4-mẫu-ngẫu-nhiên-và-thống-kê)
5. [Trung bình mẫu](#5-trung-bình-mẫu)
6. [Phương sai mẫu và câu chuyện chia n trừ 1](#6-phương-sai-mẫu-và-câu-chuyện-chia-n-trừ-1)
7. [Luật phân phối của các đặc trưng mẫu](#7-luật-phân-phối-của-các-đặc-trưng-mẫu)
8. [Tính toán với mẫu có tần số và mẫu lớp](#8-tính-toán-với-mẫu-có-tần-số-và-mẫu-lớp)
9. [📚 Chữ ký hiệu nào là mẫu, chữ nào là tổng thể](#9--chữ-ký-hiệu-nào-là-mẫu-chữ-nào-là-tổng-thể)
10. [Code minh hoạ](#10-code-minh-hoạ)
11. [Tự thử](#11-tự-thử)
12. [Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
13. [Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Mẫu và tập nền

**Hai khái niệm gốc (tr. 114):**

|                            | Định nghĩa                    | Ký hiệu     |
| -------------------------- | ----------------------------- | ----------- |
| **Tập đám đông** (tập nền) | toàn bộ đối tượng ta quan tâm | $N$ phần tử |
| **Mẫu**                    | dãy số liệu lấy ra từ tập nền | $n$ phần tử |

> "Mẫu sẽ mang **thông tin nào đó** về tập nền, mặc dù các thông tin đó **có thể khác nhau ở những
> mẫu khác nhau**."

Câu này chứa cả hy vọng lẫn vấn đề của thống kê: mẫu *có* thông tin, nhưng mỗi mẫu cho một câu trả lời
hơi khác. Bài 11 sẽ định lượng "hơi khác" đó.

### Vì sao không nghiên cứu cả tập nền?

Giáo trình nêu ba lý do (tr. 114):

1. **Quá lớn** → đòi hỏi quá nhiều chi phí vật chất và thời gian.
2. **Trình độ tổ chức hạn chế** → không nắm bắt và kiểm soát được quá trình khi quy mô lớn.
3. **Không thể làm được** nếu tập nền biến động nhanh, các phần tử thay đổi thường xuyên.

Kết luận (tr. 114): *"việc nghiên cứu trên tập nền, trừ các tập đủ bé, **thường không thể thực hiện
được**."*

💼 Lý do thứ ba là lý do thực tế nhất trong kinh doanh: **tập khách hàng thay đổi mỗi ngày**.
Điều tra xong toàn bộ khách hàng thì danh sách đã khác rồi. Với dữ liệu chuỗi thời gian
(doanh thu tương lai), tập nền thậm chí **chưa tồn tại** — không thể khảo sát toàn bộ.

### Kỳ vọng vào mẫu

> "Nếu mẫu được chọn **ngẫu nhiên** và với **số lượng đủ**, chúng ta hy vọng rằng việc xử lý chúng sẽ
> cho ta kết quả **vừa nhanh vừa đỡ tốn kém** mà vẫn đạt được **độ chính xác và tin cậy cần thiết**."

Hai điều kiện in đậm là hai trụ cột — và cả hai đều đã được chứng minh ở bài 9:

- **"ngẫu nhiên"** → điều kiện độc lập, cùng phân phối của luật số lớn và CLT.
- **"số lượng đủ"** → $n$ lớn để $\sigma/\sqrt{n}$ đủ nhỏ.

---

## 2. Bốn cách chọn mẫu

Giáo trình mở đầu thẳng thắn (tr. 115): *"có nhiều phương pháp khác nhau để chọn mẫu, nhưng **khó có
thể nói rằng phương pháp nào là tốt nhất**."*

### a) Chọn mẫu ngẫu nhiên đơn giản

**Tính chất:** mọi mẫu **cùng kích cỡ** có **cùng xác suất** được chọn, và mọi phần tử của tập nền
**đồng khả năng** lọt vào mẫu.

Cách làm: bốc thăm, hoặc dùng bảng số ngẫu nhiên. Có hai phương thức: **không hoàn lại** và
**có hoàn lại**.

⚠️ Giáo trình lưu ý (tr. 115): *"Nếu số lượng phần tử của mẫu **khá bé so với tập nền** thì kết quả
lấy mẫu theo hai phương thức sai lệch không đáng kể."* — chính là điều kiện $N > 10n$ ở bài 7 mục 4.

| Ưu                         | Nhược                                 |
| -------------------------- | ------------------------------------- |
| tính đại diện cao, tin cậy | **đòi hỏi phải biết toàn bộ tập nền** |
| khách quan                 | chi phí chọn mẫu khá lớn              |

### b) Chọn mẫu phân nhóm

Chia tập nền thành các nhóm **tương đối thuần nhất**, rồi từ mỗi nhóm trích một mẫu ngẫu nhiên.

Dùng khi *"trong nội bộ tập nền có những sai khác lớn"*.

| Ưu                                            | Nhược                                 |
| --------------------------------------------- | ------------------------------------- |
| đơn giản khi các nhóm đã bé và thuần nhất     | **tính chủ quan khi phân chia nhóm**  |
| mỗi nhóm có trọng số riêng theo độ quan trọng | đòi hỏi hiểu biết về cấu trúc tập nền |

### c) Chọn mẫu chùm

Chọn ngẫu nhiên một số **tập con** (chùm), rồi nghiên cứu **toàn bộ** phần tử của các chùm đó.

Ví dụ của giáo trình (tr. 116): nghiên cứu nhu cầu tiêu thụ một mặt hàng — chia thành phố thành các
khu dân cư, chọn ra một số khu, rồi nghiên cứu tất cả gia đình sống trong các khu được chọn.

| Ưu                                                              | Nhược                                          |
| --------------------------------------------------------------- | ---------------------------------------------- |
| tiết kiệm kinh phí và thời gian (không phải di chuyển khắp nơi) | **sai số có thể lớn hơn** hai phương pháp trên |

⚠️ Điều kiện: mỗi chùm phải **vẫn có độ phân tán cao như tập nền** và **đồng đều nhau về quy mô**.

### d) Chọn mẫu có suy luận

Dựa trên ý kiến các chuyên gia. Giáo trình phê bình rõ (tr. 116):

> "Khi không có sự tham gia của các công cụ thống kê vào việc chọn mẫu, **tính khách quan rất khó
> được bảo đảm**, từ đó kéo theo các kết luận **mang nặng tính chủ quan**."

Nhưng không phủ nhận hoàn toàn: *"điều đó không có nghĩa là không nên dùng các phương pháp chuyên gia."*

### 💼 Góc QTKD — chọn cách nào

| Tình huống                                                  | Cách phù hợp             |
| ----------------------------------------------------------- | ------------------------ |
| Có danh sách đầy đủ khách hàng (CRM)                        | ngẫu nhiên đơn giản      |
| Khách chia rõ theo miền/kênh/quy mô, các nhóm rất khác nhau | **phân nhóm**            |
| Khảo sát cửa hàng trên toàn quốc, chi phí đi lại lớn        | **chùm**                 |
| Thử nghiệm ý tưởng sản phẩm mới, chưa có dữ liệu            | có suy luận (chuyên gia) |

⚠️ **Sai lầm chọn mẫu phổ biến nhất trong kinh doanh — thiên lệch sống sót:**
khảo sát *khách hàng hiện tại* để hỏi vì sao khách rời bỏ. Người đã rời bỏ **không nằm trong mẫu**.
Kết quả sẽ luôn đẹp một cách giả tạo.

Tương tự: khảo sát trên website chỉ bắt được người **vẫn còn vào website**; hộp góp ý chỉ bắt được
người **chịu khó viết**. Cả hai đều vi phạm điều kiện "mọi phần tử đồng khả năng lọt vào mẫu".

---

## 3. Tần số, tần suất và bảng phân phối thực nghiệm

**Ba dạng trình bày mẫu (tr. 116):**

| Dạng              | Mô tả                                                         |
| ----------------- | ------------------------------------------------------------- |
| **Mẫu đơn**       | $n$ giá trị $x_1, x_2, \dots, x_n$, liệt kê thẳng             |
| **Mẫu có tần số** | $x_i$ xuất hiện $n_i$ lần, $\sum n_i = n$                     |
| **Mẫu lớp**       | số liệu chia thành nhiều lớp là các **khoảng không cắt nhau** |

**Tần số** $n_i$ = số lần xuất hiện $x_i$ hoặc lớp thứ $i$.
**Tần suất** $f_i = \dfrac{n_i}{n}$, và hiển nhiên $\sum f_i = 1$.

Giáo trình nhận xét (tr. 119): bảng tần suất *"rất giống với bảng phân phối xác suất của một biến ngẫu
nhiên rời rạc"* — chỉ khác một chữ: bảng xác suất là **lý thuyết**, bảng tần suất là **thực nghiệm**.

### Chia bao nhiêu lớp?

Giáo trình cho quy tắc thực hành (tr. 117): *"Thông thường người ta hay chia các số liệu vào từ
**5 đến 15 lớp**."*

> "Nếu số lớp nhiều hơn, có thể làm tốt hơn các phân tích, nhưng **việc cải thiện đó không nhiều**;
> ngược lại nếu số lớp ít quá, **có khả năng sẽ bị mất mát nhiều thông tin**."

### Thí dụ 1.1 (tr. 117) — chiều cao 300 học sinh

| Chiều cao (cm) | Số lượng |
| -------------- | -------: |
| 117,5 – 122,5  |        9 |
| 122,5 – 127,5  |       33 |
| 127,5 – 132,5  |       74 |
| 132,5 – 137,5  |   **93** |
| 137,5 – 142,5  |       64 |
| 142,5 – 147,5  |       21 |
| 147,5 – 152,5  |        6 |

7 lớp, mỗi lớp rộng 5 cm, tổng 300 số liệu. Dữ liệu này đã được lưu thành
[chieu_cao_hoc_sinh.csv](../thuc_hanh/du_lieu/chieu_cao_hoc_sinh.csv) để dùng cho code ở mục 10.

### Hai cách vẽ (tr. 117–118)

**a) Biểu đồ** (histogram) — các hình chữ nhật cạnh nhau, đáy bằng độ dài lớp, chiều cao bằng tần số.
*"Diện tích các hình chữ nhật tỷ lệ với tần số của các lớp tương ứng."*

**b) Đa giác tần số** — đường gấp khúc nối các điểm $(x_i, n_i)$.

Giáo trình nêu một quan sát rất sâu (tr. 119):

> "Khi hiệu giữa hai hoành độ liên tiếp khá bé, đường gấp khúc sẽ càng ngày càng trơn và
> **dần tiến tới dạng hàm mật độ xác suất**."

⭐ Đây là **cầu nối trực quan giữa thực nghiệm và lý thuyết**: histogram là hình bóng thô của $f(x)$.
Chia càng nhiều lớp, mẫu càng lớn, hình bóng càng rõ.

### Hàm phân phối thực nghiệm

Đặt $F_n(x)$ = tần suất tích luỹ:

$$F_n(x) = \sum_{x_i < x} f_i$$

Giáo trình gọi là **hàm phân phối thực nghiệm** (hay hàm phân phối mẫu), và nêu kết quả then chốt
(tr. 119):

> "Chú ý rằng theo **luật số lớn (định lý Bernoulli)**: $F_n(x) \xrightarrow{xs} F(x) = P(X < x)$...
> Như vậy hàm phân phối mẫu có thể dùng để **xấp xỉ luật phân phối của tập nền**."

⭐ **Đây là câu quan trọng nhất của §1.** Nó nói: histogram của bạn *hội tụ về* mật độ thật; bảng
tần suất *hội tụ về* bảng xác suất thật. Bài 9 đã chứng minh; giờ ta dùng.

### 💼 Góc QTKD

| Khái niệm thống kê        | Trong công việc                            |
| ------------------------- | ------------------------------------------ |
| Bảng tần số               | pivot table đếm số lượng                   |
| Biểu đồ (histogram)       | biểu đồ cột phân bố giá trị đơn hàng       |
| Tần suất tích luỹ         | *"80% đơn hàng dưới 2 triệu"*              |
| Hàm phân phối thực nghiệm | đường cong phân bố khách hàng theo mức chi |

⚠️ **Số lớp thay đổi kết luận.** Cùng một bộ dữ liệu doanh thu, chia 5 lớp có thể cho thấy phân phối
"một đỉnh"; chia 20 lớp có thể lộ ra **hai đỉnh** (khách lẻ và khách sỉ). Đây là lý do luôn phải
thử vài cách chia trước khi kết luận về hình dạng phân phối.

---

## 4. Mẫu ngẫu nhiên và thống kê

Đến §2, giáo trình chuyển từ mô tả sang lý thuyết. Giả thiết nền (tr. 121):

> "Các phần tử của một tập đám đông nào đó đều được **cảm sinh bởi một biến ngẫu nhiên gốc** $X$."

**Định nghĩa 1 (tr. 121).** **Mẫu ngẫu nhiên** kích thước $n$ là tập các biến $X_1, X_2, \dots, X_n$
thoả mãn:

$$
\begin{aligned}
&\text{(i)} && \text{độc lập thống kê} \\
&\text{(ii)} && \text{có cùng phân phối xác suất với } X
\end{aligned}
$$

Gọi tắt là **độc lập và đồng phân phối** (i.i.d.).

⭐ **Đây chính xác là điều kiện của định lý giới hạn trung tâm** (bài 9 mục 7). Không phải trùng hợp:
định nghĩa mẫu ngẫu nhiên được thiết kế để CLT áp dụng được.

⚠️ **Phân biệt hai thứ:**

|                      | Ký hiệu                        | Là gì                                  |
| -------------------- | ------------------------------ | -------------------------------------- |
| **Mẫu ngẫu nhiên**   | $X_1, \dots, X_n$ (chữ HOA)    | các **biến ngẫu nhiên**, chưa quan sát |
| **Thể hiện của mẫu** | $x_1, \dots, x_n$ (chữ thường) | các **con số** đã đo được              |

Đây là quy ước từ bài 5 mục 1, giờ mới thấy hết tầm quan trọng: *"khái niệm mẫu mà ta đưa vào tiết
trước có thể hiểu như là **một thể hiện của một mẫu ngẫu nhiên**"* (tr. 121).

**Giả thiết độc lập cho phép viết phân phối đồng thời rất gọn** (2.1):

$$p_n(x_1, \dots, x_n) = \prod_{i=1}^{n} p(x_i), \qquad f_n(x_1, \dots, x_n) = \prod_{i=1}^{n} f(x_i)$$

### Thống kê

**Định nghĩa 2 (tr. 122).** Một hàm $g(X_1, X_2, \dots, X_n)$ phụ thuộc vào tập giá trị của mẫu ngẫu
nhiên được gọi là một **thống kê**.

⚠️ Điều kiện quan trọng: thống kê **không phụ thuộc vào các tham số chưa biết**.
Nếu công thức chứa $\sigma$ mà bạn không biết $\sigma$, đó **không phải** thống kê — vì không tính được.

**Thí dụ 2.1 (tr. 122)** — ba thống kê:

$$
\text{a) } \overline{X} = \frac1n\sum X_i \qquad
\text{b) } \frac1n\sum (X_i - \overline{X})^2 \qquad
\text{c) } (X_{(1)}, \dots, X_{(n)}) \text{ — thống kê hạng}
$$

trong đó $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$ là dãy đã sắp xếp.

📚 Vì thống kê là **hàm của các biến ngẫu nhiên**, bản thân nó **cũng là một biến ngẫu nhiên** —
có phân phối riêng, kỳ vọng riêng, phương sai riêng. Đó là ý tưởng khó nhất của phần thống kê,
và cũng là ý tưởng làm mọi thứ hoạt động.

💼 Nói bằng lời: *"nếu tôi lấy một mẫu 100 khách hàng khác, trung bình mẫu sẽ ra một số khác."*
Tập hợp mọi giá trị có thể có đó chính là **phân phối của thống kê** — bài 11 gọi nó là
**phân phối chọn mẫu** (sampling distribution).

---

## 5. Trung bình mẫu

**Định nghĩa (tr. 123).**

$$\overline{X} = \frac1n\sum_{i=1}^{n} x_i \tag{2.4}$$

hoặc với mẫu có tần số:

$$\overline{X} = \frac1n\sum_{i=1}^{k} x_i n_i \tag{2.5}$$

*"Về mặt bản chất (2.4) và (2.5) là một"* — chỉ khác cách viết.

### Hai số đặc trưng của $\overline{X}$

Nếu biến gốc có $EX = a$, $VX = \sigma^2$ thì:

$$\boxed{E\overline{X} = a, \qquad V\overline{X} = \frac{\sigma^2}{n}} \tag{2.6}$$

**Chứng minh vế trái** (giáo trình làm, tr. 124): $E\overline{X} = \frac1n(EX_1 + \dots + EX_n)$;
các $X_i$ cùng phân phối với $X$ nên $EX_i = a$, suy ra $E\overline{X} = \frac1n(na) = a$. ∎

Vế phải chính là luật căn bậc hai đã chứng minh ở bài 6 mục 4.

**Ý nghĩa (tr. 124):** *"do phương sai $V\overline{X}$ bé hơn $n$ lần $VX$, nên các giá trị có thể có
của $\overline{X}$ sẽ **ổn định quanh kỳ vọng hơn** các giá trị của $X$."*

### ⚠️ Trường hợp tập nền nhỏ, lấy mẫu không hoàn lại

Phải nhân thêm **thừa số hiệu chỉnh tổng thể hữu hạn** (đã gặp ở bài 7 mục 4):

$$V\overline{X} = \frac{\sigma^2}{n}\cdot\frac{N-n}{N-1} \tag{2.7}$$

Hai trường hợp cực đoan giáo trình nêu (tr. 124):

- $n = N$ (lấy toàn bộ) → $V\overline{X} = 0$. Hợp lý: biết hết rồi thì không còn bất định.
- $N \to \infty$ → $\dfrac{N-n}{N-1} \to 1$ → về lại (2.6).

### Thí dụ 2.2 (tr. 125)

> Năm mảnh bìa đánh số 1 đến 5. Lấy mẫu **2 mảnh không hoàn lại**. Tìm phân phối của $\overline{X}$
> và các số đặc trưng.

*Giải.* $X \sim \mathcal{U}(5)$ với $EX = 3$, $VX = 2$. Có $C_5^2 = 10$ cặp, mỗi cặp xác suất $1/10$:

| $\overline{x}$    | 1,5 | 2   | 2,5 | 3   | 3,5 | 4   | 4,5 |
| ----------------- | --- | --- | --- | --- | --- | --- | --- |
| $p(\overline{x})$ | 0,1 | 0,1 | 0,2 | 0,2 | 0,2 | 0,1 | 0,1 |

$$E\overline{X} = \mathbf{3} \ (= EX \ \checkmark), \qquad V\overline{X} = \mathbf{0{,}75} < VX = 2$$

Kiểm bằng (2.7): $\dfrac{2}{2}\cdot\dfrac{5-2}{5-1} = 1 \times 0{,}75 = 0{,}75$ ✓

Nếu **có hoàn lại**, (2.6) cho $\sigma^2/n = 1$ — lớn hơn. Đúng như lý thuyết: lấy mẫu không hoàn lại
ít phân tán hơn.

⚠️ Giáo trình lưu ý (tr. 125): *"khi chọn mẫu **không hoàn lại**, $X_2$ đã **không cùng phân phối**
như $X$ nữa nên việc áp dụng (2.6) là **không được phép**."* — điều kiện (ii) của định nghĩa mẫu
ngẫu nhiên bị vi phạm.

### 💼 Góc QTKD

Bảng phân phối của $\overline{X}$ trong thí dụ 2.2 rất đáng suy nghĩ: tập nền chỉ có giá trị
$1, 2, 3, 4, 5$, nhưng trung bình mẫu nhận cả giá trị $1{,}5;\ 2{,}5;\ \dots$ và **tập trung mạnh
quanh 3**.

Đó là hình ảnh thu nhỏ của điều xảy ra khi khảo sát 1.000 khách hàng: từng câu trả lời rất khác nhau,
nhưng trung bình thì ổn định. **Đó là toàn bộ lý do khảo sát hoạt động.**

Và thừa số $\dfrac{N-n}{N-1}$ có ý nghĩa thực tế: nếu bạn khảo sát 200 trong tổng số 500 khách hàng
($n/N = 40\%$), sai số **nhỏ hơn** công thức chuẩn tính ra:
$\sqrt{(500-200)/(500-1)} = 0{,}775$ — giảm 22,5%. Nhiều phần mềm bỏ qua thừa số này và báo sai số
lớn hơn thực tế.

---

## 6. Phương sai mẫu và câu chuyện chia n trừ 1

Đây là chỗ gây bối rối nhất của cả phần thống kê. Giáo trình định nghĩa **hai** đại lượng.

**Phương sai mẫu (tr. 125–126):**

$$\hat{S}^2 = \frac1n\sum_{i=1}^{n}(x_i - \overline{X})^2 \tag{2.8}$$

$$\hat{S}^2 = \frac1n\sum_{i=1}^{k} n_i(x_i - \overline{X})^2 \tag{2.9}$$

### Vì sao nó SAI

Giáo trình tính $E\hat{S}^2$ và được (tr. 126):

$$E\hat{S}^2 = \frac{n-1}{n}\,\sigma^2 \ne \sigma^2 \tag{2.10}$$

Nghĩa là $\hat{S}^2$ **luôn nhỏ hơn** $\sigma^2$ trung bình — nó **chệch**.

**Trực giác vì sao:** ta đo độ tán xạ quanh $\overline{X}$ chứ không phải quanh $a$ (không biết $a$).
Mà $\overline{X}$ được tính **từ chính dữ liệu đó**, nên nó nằm "chính giữa" mẫu hơn $a$ —
tổng bình phương độ lệch quanh $\overline{X}$ luôn là **nhỏ nhất có thể**. Vì thế ta đánh giá thấp
độ tán xạ thật.

⭐ Bài 7 mục 8 đã cho câu trả lời sâu hơn: dùng $\overline{X}$ thay $a$ làm **mất một bậc tự do**,
nên $\dfrac{1}{\sigma^2}\sum(X_i - \overline{X})^2 \sim \chi^2(n-1)$ chứ không phải $\chi^2(n)$.

### Sửa: chia cho $n-1$

**Phương sai mẫu hiệu chỉnh (2.11), (2.12):**

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \overline{X})^2 = \frac{n}{n-1}\hat{S}^2$$

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{k} n_i(x_i - \overline{X})^2$$

Khi đó:

$$E s^2 = \frac{n}{n-1}\cdot\frac{n-1}{n}\sigma^2 = \sigma^2 \quad \checkmark$$

$$\boxed{\text{Dùng } s^2 \text{ (chia } n-1) \text{ khi ước lượng } \sigma^2 \text{ của tổng thể}}$$

### 📚 Khi nào dùng cái nào

|            | $\hat{S}^2$ (chia $n$)              | $s^2$ (chia $n-1$)                    |
| ---------- | ----------------------------------- | ------------------------------------- |
| Tên        | phương sai mẫu                      | phương sai mẫu **hiệu chỉnh**         |
| $E(\cdot)$ | $\frac{n-1}{n}\sigma^2$ — **chệch** | $\sigma^2$ — **không chệch**          |
| Dùng khi   | mô tả **chính mẫu** đó              | **ước lượng** $\sigma^2$ của tổng thể |
| Excel      | `VAR.P()`, `STDEV.P()`              | `VAR.S()`, `STDEV.S()`                |
| Python     | `statistics.pvariance`              | `statistics.variance`                 |

⚠️ Chữ **P** trong Excel = Population (tổng thể), **S** = Sample (mẫu). Nghe ngược trực giác:
`VAR.S` dùng cho *mẫu* nhưng chia $n-1$; `VAR.P` dùng khi dữ liệu **chính là** toàn bộ tổng thể.

**Quy tắc thực hành:** trong kinh doanh bạn gần như **luôn** làm việc với mẫu, nên
**mặc định dùng `VAR.S` / `STDEV.S`**.

**Khi nào khác biệt đáng kể?** Tỷ số $\dfrac{n}{n-1}$:

|  $n$ | $n/(n-1)$ | Chênh lệch         |
| ---: | --------: | ------------------ |
|    5 |     1,250 | 25% — **rất lớn**  |
|   10 |     1,111 | 11%                |
|   30 |     1,034 | 3,4%               |
|  100 |     1,010 | 1%                 |
| 1000 |     1,001 | 0,1% — bỏ qua được |

Với mẫu lớn thì không quan trọng; với mẫu nhỏ (dưới 30) thì **rất** quan trọng.

### Các đặc trưng mẫu khác (tr. 127)

$$\text{mômen mẫu cấp } k: \ m_k = \frac1n\sum x_i^k, \qquad
\text{mômen trung tâm mẫu cấp } k: \ \hat{S}_k = \frac1n\sum(x_i - \overline{X})^k$$

cùng với **trung vị mẫu**, **mốt mẫu**.

---

## 7. Luật phân phối của các đặc trưng mẫu

Đây là phần **quan trọng nhất về mặt lý thuyết** của bài — nó cho bốn công thức mà bài 11–14 dùng liên tục.

### Khi biến gốc CHUẨN: $X \sim N(a, \sigma^2)$

Giáo trình nêu (tr. 127) rằng khi đó $\overline{X}$ và $\hat{S}^2$ **độc lập với nhau**, và:

$$\text{a) } \ \overline{X} \sim N\!\left(a; \frac{\sigma^2}{n}\right)
\quad\text{hay}\quad \frac{\overline{X} - a}{\sigma/\sqrt{n}}\sqrt{n} \sim N(0;1) \tag{2.13}$$

$$\text{b) } \ \frac{n\hat{S}^2}{\sigma^2} = \frac{(n-1)s^2}{\sigma^2}
= \frac{1}{\sigma^2}\sum_{i=1}^n (X_i - \overline{X})^2 \sim \chi^2(n-1) \tag{2.14}$$

$$\text{c) } \ \frac{\overline{X} - a}{s}\sqrt{n} \sim t(n-1) \tag{2.15}$$

$$\text{d) } \ \frac{s_1^2}{s_2^2} \sim F(n_1 - 1;\ n_2 - 1) \quad (\text{giả thiết } \sigma_1^2 = \sigma_2^2) \tag{2.16}$$

⚠️ Giáo trình lưu ý cuối (tr. 127): nếu trong (2.14) **thay $\overline{X}$ bằng $a$** (tức là biết $a$)
thì được $\chi^2(n)$ — **đủ $n$ bậc tự do**. Mất một bậc chính là giá phải trả cho việc ước lượng $a$.

**Bốn công thức này dùng ở đâu:**

| Công thức | Phân phối         | Dùng cho                        | Bài    |
| --------- | ----------------- | ------------------------------- | ------ |
| (2.13)    | $N(0;1)$          | kỳ vọng, **biết** $\sigma$      | 11, 12 |
| (2.14)    | $\chi^2(n-1)$     | **phương sai**                  | 11, 13 |
| (2.15)    | $t(n-1)$          | kỳ vọng, **chưa biết** $\sigma$ | 11, 12 |
| (2.16)    | $F(n_1-1; n_2-1)$ | **so sánh hai phương sai**      | 13     |

### Khi biến gốc KHÔNG chuẩn — nhờ luật số lớn và CLT

Với $n \to \infty$ (tr. 128):

$$
\begin{aligned}
&\text{a)} && \overline{X} \xrightarrow{h.c.c} a, \quad s^2 \xrightarrow{h.c.c} \sigma^2 \\
&\text{b)} && \frac{\overline{X} - a}{\sigma/\sqrt{n}} \xrightarrow{L} N(0;1)
\end{aligned}
$$

⭐ **Câu quan trọng nhất của mục này** (tr. 128):

> "Các kết quả trên sẽ **rất có ích trong thực hành** vì **không cần đến giả thiết chuẩn** của biến
> ngẫu nhiên gốc và trong nhiều trường hợp ta đã có thể chấp nhận kết quả với $n$ **không quá lớn**.
> Chẳng hạn với $n > 30$, kết quả (b) đã có thể chấp nhận được."

💼 **Đây là giấy phép để dùng thống kê trên dữ liệu kinh doanh.** Doanh thu, giá trị đơn hàng,
thời gian chờ đều **không chuẩn** (bài 7 mục 5), nhưng với $n > 30$ ta vẫn dùng được (2.13) và (2.15).

**Định lý Glivenko – Cantelli** (tr. 128) — kết quả cuối cùng, mạnh nhất:

$$\sup_{x \in \mathbb{R}}\big|F_n(x) - F(x)\big| \xrightarrow{h.c.c} 0$$

Không chỉ tại từng điểm, mà **toàn bộ** hàm phân phối thực nghiệm hội tụ **đều** về hàm phân phối
thật. Đây là lý do người ta gọi nó là **"định lý cơ bản của thống kê"**.

---

## 8. Tính toán với mẫu có tần số và mẫu lớp

### Công thức tính nhanh

Giáo trình chỉ ra (tr. 128–129) rằng nên thay tổng bình phương độ lệch bằng:

$$\sum_{i=1}^{n}(x_i - \overline{X})^2 = \sum_{i=1}^{n} x_i^2 - n(\overline{X})^2$$

Đây là công thức (3.4) của bài 6 áp cho mẫu — chỉ cần **một lượt duyệt** dữ liệu thay vì hai.

**Trung vị thực nghiệm** = giá trị thứ $\dfrac{n+1}{2}$ của mẫu **đã sắp xếp**
($n$ lẻ: giá trị chính giữa; $n$ chẵn: trung bình cộng hai giá trị chính giữa).

### Cách tính rút gọn (đổi gốc, đổi thang)

Khi số liệu **cách đều** nhau khoảng $h$, giáo trình cho cách tính tay nhanh (tr. 129):

**B1.** Chọn một giá trị trung tâm tuỳ ý $x_0$.
**B2.** Đặt $d_i = \dfrac{x_i - x_0}{h}$ — biến đổi thành các số nguyên nhỏ.
**B3.** Tính $\sum d_i n_i$ và $\sum d_i^2 n_i$.
**B4.**

$$\overline{X} = x_0 + \frac{h}{n}\sum d_i n_i \tag{2.17}$$

$$s^2 = \frac{h^2}{n-1}\left[\sum d_i^2 n_i - \frac{(\sum d_i n_i)^2}{n}\right] \tag{2.18a}$$

$$\hat{S}^2 = \frac{h^2}{n}\left[\sum d_i^2 n_i - \frac{(\sum d_i n_i)^2}{n}\right] \tag{2.18b}$$

📚 **Vì sao được phép làm thế?** Vì $d_i$ là một **phép biến đổi tuyến tính** của $x_i$, và bài 6 mục 4
đã cho: $E(cX + b) = cEX + b$, $V(cX+b) = c^2 VX$. Chính vì thế mới nhân lại $h$ và $h^2$ ở cuối.

⚠️ Hạn chế giáo trình nêu: *"thường đòi hỏi số liệu cách đều"*. Thời có máy tính thì cách này
không còn cần thiết để **tính**, nhưng vẫn hữu ích để **kiểm tra bằng tay** khi nghi ngờ kết quả máy.

### Thí dụ 2.3 (tr. 130) — cân nặng 150 con vịt

| Cân nặng (kg) | 1,25 | 1,50 | 1,75 | 2,00 |   2,25 | 2,50 | 2,75 | 3,00 |
| ------------- | ---: | ---: | ---: | ---: | -----: | ---: | ---: | ---: |
| Số con        |    2 |    6 |   24 |   35 | **39** |   24 |   14 |    6 |

Chọn $x_0 = 2{,}25$, $h = 0{,}25$; tính được $\sum d_i n_i = -39$, $\sum d_i^2 n_i = 351$:

$$\overline{X} = 2{,}25 + \frac{0{,}25}{150}(-39) = \mathbf{2{,}185} \text{ kg}$$

$$\hat{S}^2 = \frac{0{,}25^2}{150}\left[351 - \frac{39^2}{150}\right] = \mathbf{0{,}142025}$$

Trung vị mẫu = **2,25**, cũng là mốt thực nghiệm.

Dữ liệu lưu ở [can_nang_vit.csv](../thuc_hanh/du_lieu/can_nang_vit.csv).

### Mẫu lớp — mốt và trung vị

Với mẫu lớp, $\overline{X}$ và $\hat{S}^2$ chỉ tính **gần đúng**: thay mỗi khoảng bằng **giá trị giữa
khoảng**, rồi đưa về mẫu có tần số.

Riêng mốt và trung vị có công thức nội suy riêng (tr. 131):

$$\text{Mod} = x_{mo} + \frac{d_1}{d_1 + d_2}\,h \tag{2.20}$$

- $x_{mo}$ — điểm đầu của **khoảng mốt** (khoảng có tần số lớn nhất)
- $d_1$ — hiệu tần số của khoảng mốt và khoảng **trước**
- $d_2$ — hiệu tần số của khoảng mốt và khoảng **sau**
- $h$ — độ dài khoảng

$$\text{Med} = x_{me} + \frac{\dfrac{n}{2} - n_{tl}}{n_{me}}\,h \tag{2.21}$$

- $x_{me}$ — điểm đầu của **khoảng trung vị**
- $n_{tl}$ — tần số **tích luỹ trước** khoảng trung vị
- $n_{me}$ — tần số **của** khoảng trung vị

### Thí dụ 2.4 (tr. 132) — ⚠️ có ba lỗi số học

> Tính các đặc trưng mẫu của thí dụ 1.1 (chiều cao 300 học sinh).

Bảng tính, chọn $x_0 = 135$, $h = 5$:

| Khoảng      |   TB |   $n_i$ | $d_i$ | $d_i n_i$ | $d_i^2 n_i$ | tích luỹ |
| ----------- | ---: | ------: | ----: | --------: | ----------: | -------: |
| 117,5–122,5 |  120 |       9 |    −3 |       −27 |          81 |        9 |
| 122,5–127,5 |  125 |      33 |    −2 |       −66 |         132 |       42 |
| 127,5–132,5 |  130 |      74 |    −1 |       −74 |          74 |      116 |
| 132,5–137,5 |  135 |  **93** |     0 |         0 |           0 |      209 |
| 137,5–142,5 |  140 |      64 |     1 |        64 |          64 |      273 |
| 142,5–147,5 |  145 |      21 |     2 |        42 |          84 |      294 |
| 147,5–152,5 |  150 |       6 |     3 |        18 |          54 |      300 |
| **Σ**       |      | **300** |       |   **−43** |     **489** |          |

$$\overline{X} = 135 + \frac{5}{300}(-43) = \mathbf{134{,}2833}$$

$$\hat{S}^2 = \frac{5^2}{300}\left[489 - \frac{43^2}{300}\right] = \mathbf{40{,}2364}$$

Khoảng mốt là 132,5–137,5 (tần số 93):

$$d_1 = 93 - 74 = \mathbf{19}, \qquad d_2 = 93 - 64 = \mathbf{29}$$

$$\text{Mod} = 132{,}5 + \frac{19}{19+29}\cdot 5 = \mathbf{134{,}4792}$$

$$\text{Med} = 132{,}5 + \frac{150 - 116}{93}\cdot 5 = \mathbf{134{,}3280}$$

### ⚠️ Đính chính ba lỗi

Đã đối chiếu bản quét gốc trang 132:

| Chỗ                   | Sách in        | Đúng phải là            | Ghi chú                                                                 |
| --------------------- | -------------- | ----------------------- | ----------------------------------------------------------------------- |
| Hàng Σ của cột tần số | 150            | **300**                 | tổng $9+33+74+93+64+21+6 = 300$; chính công thức bên dưới cũng dùng 300 |
| $\overline{X}$        | 134,2823       | **134,2833**            | $135 - 215/300 = 134{,}28\overline{3}$                                  |
| $d_1$                 | $93 - 74 = 9$  | $93 - 74 = \mathbf{19}$ | phép trừ sai                                                            |
| $d_2$                 | $93 - 64 = 19$ | $93 - 64 = \mathbf{29}$ | phép trừ sai                                                            |
| **Mod**               | **134,1072**   | **134,4792**            | hệ quả của hai lỗi trên                                                 |

$\hat{S}^2 = 40{,}2364$ và $\text{Med} = 134{,}3279$ của sách **đúng**.

**Kết quả sau đính chính đọc được nhiều hơn:**

$$\overline{X}\ (134{,}283) \ < \ \text{Med}\ (134{,}328) \ < \ \text{Mod}\ (134{,}479)$$

Đúng thứ tự của phân phối **lệch trái** (bài 6 mục 5) — có một đuôi kéo nhẹ về phía học sinh thấp.
Với con số Mod sai của sách (134,107), thứ tự sẽ là Mod < $\overline{X}$ < Med, không tương ứng với
dạng lệch nào cả.

---

## 9. 📚 Chữ ký hiệu nào là mẫu, chữ nào là tổng thể

Giáo trình dùng nhiều ký hiệu song song mà không có bảng tổng kết. Đây là phần bổ sung —
**bảng này nên dán lên tường**, vì nhầm lẫn ở đây là nguồn gốc của hầu hết lỗi sai từ bài 11 trở đi.

| Đại lượng            | **Tổng thể** (chưa biết) | **Mẫu** (tính được) | Quan hệ             |
| -------------------- | :----------------------: | :-----------------: | ------------------- |
| Cỡ                   |           $N$            |         $n$         | $n \ll N$           |
| Kỳ vọng / trung bình |     $a$ (hay $\mu$)      |   $\overline{X}$    | $E\overline{X} = a$ |
| Phương sai           |        $\sigma^2$        |        $s^2$        | $Es^2 = \sigma^2$   |
| Độ lệch chuẩn        |         $\sigma$         |         $s$         |                     |
| Tỷ lệ                |           $p$            |      $f = m/n$      | $Ef = p$            |
| Hàm phân phối        |          $F(x)$          |      $F_n(x)$       | $F_n \to F$         |
| Tương quan           |          $\rho$          |         $r$         | (bài 14)            |

**Quy ước chung — nhớ ba dòng này là đủ:**

```
   CHỮ HY LẠP   (a, σ, ρ, μ)  →  THAM SỐ TỔNG THỂ, cố định nhưng CHƯA BIẾT
   CHỮ LA-TINH  (X̄, s, r, f)  →  THỐNG KÊ MẪU, tính được nhưng NGẪU NHIÊN
   CHỮ HOA vs thường          →  X = biến ngẫu nhiên, x = giá trị đã quan sát
```

**Nghịch lý trung tâm của thống kê, gói trong một dòng:**

> Cái ta **muốn biết** thì cố định nhưng không biết. Cái ta **biết được** thì đo được nhưng ngẫu nhiên.

Toàn bộ bài 11 (khoảng tin cậy) và bài 12 (kiểm định) là các cách khác nhau để bắc cầu qua khoảng
trống đó.

### 💼 Đối chiếu với Excel

| Khái niệm                 | Excel                                   |
| ------------------------- | --------------------------------------- |
| $\overline{X}$            | `AVERAGE()`                             |
| $s$ (chia $n-1$)          | `STDEV.S()` ← **mặc định dùng cái này** |
| $\hat{S}$ (chia $n$)      | `STDEV.P()`                             |
| Trung vị                  | `MEDIAN()`                              |
| Mốt                       | `MODE.SNGL()`                           |
| Phân vị                   | `PERCENTILE.INC()`                      |
| Bảng tần số               | `FREQUENCY()` hoặc PivotTable           |
| $\overline{X} \pm$ sai số | `CONFIDENCE.NORM()` (bài 11)            |

---

## 10. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.
> Code đọc dữ liệu từ `thuc_hanh/du_lieu/`, nên phải chạy **từ thư mục gốc của khoá học**:
> ```bash
> cd houedu/xacxuatthongke
> python3 bai-10-mau.py
> ```

**Đây là bài đầu tiên dùng file CSV.** Ba tệp dữ liệu:

| Tệp                                                                   | Nội dung                       | Nguồn                       |
| --------------------------------------------------------------------- | ------------------------------ | --------------------------- |
| [chieu_cao_hoc_sinh.csv](../thuc_hanh/du_lieu/chieu_cao_hoc_sinh.csv) | 300 học sinh, mẫu lớp 7 khoảng | thí dụ 1.1, tr. 117         |
| [can_nang_vit.csv](../thuc_hanh/du_lieu/can_nang_vit.csv)             | 150 con vịt, mẫu có tần số     | thí dụ 2.3, tr. 130         |
| [doanh_thu_ngay.csv](../thuc_hanh/du_lieu/doanh_thu_ngay.csv)         | 60 ngày doanh thu, mẫu đơn     | 💼 dữ liệu mô phỏng cho QTKD |

⚠️ Tệp thứ ba là **dữ liệu mô phỏng**, sinh một lần bằng seed cố định rồi lưu lại — không phải số liệu
doanh nghiệp thật. Hai tệp đầu là số liệu **nguyên văn của giáo trình**.

```python
"""Bài 10 — Mẫu và thống kê mô tả.

Doc du lieu tu thu muc thuc_hanh/du_lieu/. Chay tu thu muc goc cua khoa hoc:
    python3 bai-10-mau.py
"""

import csv
import math
import pathlib
import random
from fractions import Fraction as F
from itertools import combinations

DATA = pathlib.Path("thuc_hanh/du_lieu")


def read_csv(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


# ─────────────────────────────────────────────────────────────
# Bộ công cụ thống kê mô tả — dùng cho cả bài, chỉ thư viện chuẩn
# ─────────────────────────────────────────────────────────────
def mean(xs, ns=None):
    """Trung binh mau (2.4) neu ns=None, hoac (2.5) neu co tan so."""
    if ns is None:
        return sum(xs) / len(xs)
    return sum(x * n for x, n in zip(xs, ns)) / sum(ns)


def var_biased(xs, ns=None):
    """Phuong sai mau (2.8)/(2.9) — chia cho n. CHECH."""
    m = mean(xs, ns)
    if ns is None:
        return sum((x - m) ** 2 for x in xs) / len(xs)
    return sum(n * (x - m) ** 2 for x, n in zip(xs, ns)) / sum(ns)


def var_corrected(xs, ns=None):
    """Phuong sai mau HIEU CHINH (2.11)/(2.12) — chia cho n-1. KHONG CHECH."""
    n = len(xs) if ns is None else sum(ns)
    return var_biased(xs, ns) * n / (n - 1)


def median(xs, ns=None):
    """Trung vi mau — gia tri thu (n+1)/2 cua day da sap xep."""
    data = sorted(xs) if ns is None else sorted(
        v for x, n in zip(xs, ns) for v in [x] * n)
    n = len(data)
    return data[n // 2] if n % 2 else (data[n // 2 - 1] + data[n // 2]) / 2


# ─────────────────────────────────────────────────────────────
# 1. MẪU LỚP — Thí dụ 1.1 và 1.2 (tr. 117, 119)
#    Chiều cao 300 học sinh, 7 lớp mỗi lớp rộng 5 cm.
# ─────────────────────────────────────────────────────────────
h_rows = read_csv("chieu_cao_hoc_sinh.csv")
lo = [float(r["can_duoi"]) for r in h_rows]
hi = [float(r["can_tren"]) for r in h_rows]
freq = [int(r["tan_so"]) for r in h_rows]
N = sum(freq)
mid = [(a + b) / 2 for a, b in zip(lo, hi)]      # gia tri giua lop

print("THI DU 1.1 / 1.2 — chieu cao 300 hoc sinh (mau LOP)")
print(f"{'Lop':>16}{'TB lop':>9}{'tan so':>8}{'tich luy':>10}"
      f"{'tan suat':>10}{'ts tich luy':>13}")
cum = 0
for a, b, m_, n_ in zip(lo, hi, mid, freq):
    cum += n_
    print(f"{f'{a}-{b}':>16}{m_:>9.1f}{n_:>8}{cum:>10}"
          f"{n_ / N:>10.3f}{cum / N:>13.3f}")
print(f"{'TONG':>16}{'':>9}{N:>8}")

# Bieu do tan so bang ky tu (thay cho hinh 1.1)
print()
print("Bieu do tan so (hinh 1.1):")
for a, b, n_ in zip(lo, hi, freq):
    print(f"  {a:>6.1f}-{b:<6.1f} {'#' * round(n_ / 2):<47} {n_}")

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 2.4 (tr. 132) — đặc trưng mẫu của mẫu lớp
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.4 — dac trung mau cua chieu cao")
xbar = mean(mid, freq)
print(f"  Trung binh mau X = {xbar:.4f}   (sach: 134,2823 - xem dinh chinh)")
print(f"  Kiem lai bang (2.17): 135 + (5/300)(-43) ="
      f" {135 + 5 / 300 * (-43):.4f}")
print(f"  Phuong sai mau     S^ = {var_biased(mid, freq):.4f}   (sach: 40,2364)")
print(f"  Phuong sai h.chinh s^ = {var_corrected(mid, freq):.4f}")
print(f"  Do lech chuan      s  = {math.sqrt(var_corrected(mid, freq)):.4f} cm")

# Mot va trung vi cua mau LOP — cong thuc (2.20), (2.21)
i_mod = freq.index(max(freq))
d1 = freq[i_mod] - freq[i_mod - 1]
d2 = freq[i_mod] - freq[i_mod + 1]
h = hi[0] - lo[0]
mod = lo[i_mod] + d1 / (d1 + d2) * h
print(f"  Mod = {lo[i_mod]} + {d1}/({d1}+{d2}) * {h} = {mod:.4f}   (sach: 134,1072)")

cum = 0
for i, n_ in enumerate(freq):
    if cum + n_ >= N / 2:
        med = lo[i] + (N / 2 - cum) / n_ * h
        print(f"  Med = {lo[i]} + ({N}/2 - {cum})/{n_} * {h} ="
              f" {med:.4f}   (sach: 134,3279)")
        break
    cum += n_
print(f"  ⚠ X = {xbar:.4f} < Med = {med:.4f} < Mod = {mod:.4f}"
      "  ->  phan phoi hoi LECH TRAI (bai 6 muc 5)")

# ─────────────────────────────────────────────────────────────
# 3. Thí dụ 2.3 (tr. 130) — cân nặng 150 con vịt
# ─────────────────────────────────────────────────────────────
print()
d_rows = read_csv("can_nang_vit.csv")
w = [float(r["can_nang_kg"]) for r in d_rows]
c = [int(r["so_con"]) for r in d_rows]
print("THI DU 2.3 — can nang 150 con vit")
print(f"  Trung binh mau  X  = {mean(w, c):.4f} kg   (sach: 2,185)")
print(f"  Phuong sai mau  S^ = {var_biased(w, c):.6f}   (sach: 0,142025)")
print(f"  Phuong sai h.ch s^ = {var_corrected(w, c):.6f}")
print(f"  Trung vi           = {median(w, c):.2f} kg   (sach: 2,25)")
print(f"  Mot                = {w[c.index(max(c))]:.2f} kg   (sach: 2,25)")

# ─────────────────────────────────────────────────────────────
# 4. VÌ SAO CHIA n-1 CHỨ KHÔNG PHẢI n — kiểm bằng mô phỏng
#    Cong thuc (2.10): E(S^) = (n-1)/n * sigma^2  -> CHECH
# ─────────────────────────────────────────────────────────────
print()
print("VI SAO CHIA n-1? — lay 20000 mau co n=5 tu tap nen da biet sigma^2")
pop = [1, 2, 3, 4, 5]                      # tap nen, sigma^2 = 2 (thi du 2.2)
sigma2 = sum((x - 3) ** 2 for x in pop) / len(pop)
print(f"  Tap nen {pop}: EX = 3, sigma^2 = {sigma2}")
rng = random.Random(2026)
n_s, reps = 5, 20_000
sum_b = sum_c = 0.0
for _ in range(reps):
    s = [rng.choice(pop) for _ in range(n_s)]
    sum_b += var_biased(s)
    sum_c += var_corrected(s)
print(f"  Trung binh cua S^ (chia n)   = {sum_b / reps:.4f}"
      f"   ly thuyet (n-1)/n * sigma^2 = {(n_s - 1) / n_s * sigma2:.4f}  -> CHECH")
print(f"  Trung binh cua s^ (chia n-1) = {sum_c / reps:.4f}"
      f"   ly thuyet sigma^2           = {sigma2:.4f}  -> KHONG CHECH")

# ─────────────────────────────────────────────────────────────
# 5. Thí dụ 2.2 (tr. 125) — lấy mẫu KHÔNG hoàn lại, thừa số hiệu chỉnh
# ─────────────────────────────────────────────────────────────
print()
print("THI DU 2.2 — 5 manh bia danh so 1..5, lay mau 2 KHONG hoan lai")
pairs = list(combinations(pop, 2))
means = {}
for p in pairs:
    m_ = F(sum(p), 2)
    means[m_] = means.get(m_, 0) + F(1, len(pairs))
print("  Phan phoi cua X ngang:",
      {float(k): float(v) for k, v in sorted(means.items())})
exb = sum(k * v for k, v in means.items())
vxb = sum(k * k * v for k, v in means.items()) - exb**2
print(f"  E(X ngang) = {exb} = {float(exb)}   (sach: 3)")
print(f"  V(X ngang) = {vxb} = {float(vxb)}   (sach: 0,75)")
Nn, nn = 5, 2
print(f"  Kiem (2.7): (sigma^2/n)*(N-n)/(N-1) ="
      f" ({sigma2}/{nn})*({Nn}-{nn})/({Nn}-1) ="
      f" {sigma2 / nn * (Nn - nn) / (Nn - 1)}")
print(f"  Neu CO hoan lai thi (2.6) cho sigma^2/n = {sigma2 / nn}"
      "  ->  lon hon, dung nhu ly thuyet")

# ─────────────────────────────────────────────────────────────
# 6. 💼 GÓC QTKD — doanh thu 60 ngày, mẫu ĐƠN từ file CSV
# ─────────────────────────────────────────────────────────────
print()
rev_rows = read_csv("doanh_thu_ngay.csv")
rev = [float(r["doanh_thu_trieu"]) for r in rev_rows]
print(f"💼 GOC QTKD — doanh thu {len(rev)} ngay (trieu dong)")
print(f"  Trung binh  = {mean(rev):.2f}")
print(f"  Trung vi    = {median(rev):.2f}")
print(f"  Do lech chuan s = {math.sqrt(var_corrected(rev)):.2f}")
print(f"  Nho nhat = {min(rev):.1f}   Lon nhat = {max(rev):.1f}")
srt = sorted(rev)
q = lambda a: srt[min(int(a * len(srt)), len(srt) - 1)]
print(f"  Phan vi 25% / 50% / 75% / 90% = {q(.25):.1f} / {q(.50):.1f}"
      f" / {q(.75):.1f} / {q(.90):.1f}")
print(f"  ⚠ Trung binh > trung vi  ->  LECH PHAI (vai ngay don si keo len)")

# Phan nhom theo loai ngay — phan phoi CO DIEU KIEN (bai 8)
print()
for kind in ["trong tuan", "T7/CN"]:
    g = [float(r["doanh_thu_trieu"]) for r in rev_rows if r["loai_ngay"] == kind]
    print(f"  {kind:<12} n={len(g):>3}  TB={mean(g):>6.2f}"
          f"  trung vi={median(g):>6.2f}  s={math.sqrt(var_corrected(g)):>5.2f}")
print("  => Tach nhom cho buc tranh ro hon nhieu so voi mot con so trung binh")
```

Kết quả chạy thật:

```
THI DU 1.1 / 1.2 — chieu cao 300 hoc sinh (mau LOP)
             Lop   TB lop  tan so  tich luy  tan suat  ts tich luy
     117.5-122.5    120.0       9         9     0.030        0.030
     122.5-127.5    125.0      33        42     0.110        0.140
     127.5-132.5    130.0      74       116     0.247        0.387
     132.5-137.5    135.0      93       209     0.310        0.697
     137.5-142.5    140.0      64       273     0.213        0.910
     142.5-147.5    145.0      21       294     0.070        0.980
     147.5-152.5    150.0       6       300     0.020        1.000
            TONG              300

Bieu do tan so (hinh 1.1):
   117.5-122.5  ####                                            9
   122.5-127.5  ################                                33
   127.5-132.5  #####################################           74
   132.5-137.5  ##############################################  93
   137.5-142.5  ################################                64
   142.5-147.5  ##########                                      21
   147.5-152.5  ###                                             6

THI DU 2.4 — dac trung mau cua chieu cao
  Trung binh mau X = 134.2833   (sach: 134,2823 - xem dinh chinh)
  Kiem lai bang (2.17): 135 + (5/300)(-43) = 134.2833
  Phuong sai mau     S^ = 40.2364   (sach: 40,2364)
  Phuong sai h.chinh s^ = 40.3710
  Do lech chuan      s  = 6.3538 cm
  Mod = 132.5 + 19/(19+29) * 5.0 = 134.4792   (sach: 134,1072)
  Med = 132.5 + (300/2 - 116)/93 * 5.0 = 134.3280   (sach: 134,3279)
  ⚠ X = 134.2833 < Med = 134.3280 < Mod = 134.4792  ->  phan phoi hoi LECH TRAI (bai 6 muc 5)

THI DU 2.3 — can nang 150 con vit
  Trung binh mau  X  = 2.1850 kg   (sach: 2,185)
  Phuong sai mau  S^ = 0.142025   (sach: 0,142025)
  Phuong sai h.ch s^ = 0.142978
  Trung vi           = 2.25 kg   (sach: 2,25)
  Mot                = 2.25 kg   (sach: 2,25)

VI SAO CHIA n-1? — lay 20000 mau co n=5 tu tap nen da biet sigma^2
  Tap nen [1, 2, 3, 4, 5]: EX = 3, sigma^2 = 2.0
  Trung binh cua S^ (chia n)   = 1.5912   ly thuyet (n-1)/n * sigma^2 = 1.6000  -> CHECH
  Trung binh cua s^ (chia n-1) = 1.9890   ly thuyet sigma^2           = 2.0000  -> KHONG CHECH

THI DU 2.2 — 5 manh bia danh so 1..5, lay mau 2 KHONG hoan lai
  Phan phoi cua X ngang: {1.5: 0.1, 2.0: 0.1, 2.5: 0.2, 3.0: 0.2, 3.5: 0.2, 4.0: 0.1, 4.5: 0.1}
  E(X ngang) = 3 = 3.0   (sach: 3)
  V(X ngang) = 3/4 = 0.75   (sach: 0,75)
  Kiem (2.7): (sigma^2/n)*(N-n)/(N-1) = (2.0/2)*(5-2)/(5-1) = 0.75
  Neu CO hoan lai thi (2.6) cho sigma^2/n = 1.0  ->  lon hon, dung nhu ly thuyet

💼 GOC QTKD — doanh thu 60 ngay (trieu dong)
  Trung binh  = 55.24
  Trung vi    = 52.05
  Do lech chuan s = 16.61
  Nho nhat = 28.0   Lon nhat = 132.8
  Phan vi 25% / 50% / 75% / 90% = 47.3 / 52.1 / 59.4 / 72.5
  ⚠ Trung binh > trung vi  ->  LECH PHAI (vai ngay don si keo len)

  trong tuan   n= 44  TB= 50.05  trung vi= 50.45  s= 9.33
  T7/CN        n= 16  TB= 69.53  trung vi= 61.60  s=23.21
  => Tach nhom cho buc tranh ro hon nhieu so voi mot con so trung binh
```

Năm điểm đáng để ý:

1. **`Mod = 132.5 + 19/(19+29) * 5.0 = 134.4792`** — máy in ra chính hai hiệu số $19$ và $29$,
   khác với $9$ và $19$ của sách. Bằng chứng cho đính chính ở mục 8.
2. **Mô phỏng chia $n$ vs $n-1$:** `1.5912` so với lý thuyết `1.6000`, và `1.9890` so với `2.0000`.
   Công thức (2.10) đúng tới hai chữ số sau dấu phẩy trên 20.000 mẫu. Đây là **bằng chứng thực nghiệm**
   cho việc phải chia $n-1$, thứ mà giáo trình chỉ chứng minh bằng đại số.
3. **Biểu đồ tần số bằng ký tự `#`** thay cho hình 1.1 của sách — nhìn thấy ngay hình chuông hơi
   lệch trái, khớp với kết luận $\overline{X} <$ Med $<$ Mod.
4. **Góc QTKD**: trung bình 55,24 nhưng trung vị 52,05 và cực đại 132,8. Một con số 55,24 giấu mất
   cả câu chuyện.
5. **Tách nhóm cuối:** trong tuần 50,05 ± 9,33; cuối tuần 69,53 ± 23,21. Không chỉ mức khác nhau
   mà **độ ổn định** cũng khác hẳn — cuối tuần phân tán gấp 2,5 lần. Đó là thông tin để bố trí
   nhân sự và tồn kho, mà con số trung bình chung không hề cho thấy.

---

## 11. Tự thử

1. Mở [chieu_cao_hoc_sinh.csv](../thuc_hanh/du_lieu/chieu_cao_hoc_sinh.csv), gộp 7 lớp thành **4 lớp**
   (rộng 10 cm mỗi lớp, lớp cuối 5 cm). Tính lại $\overline{X}$ và $\hat{S}^2$. Chênh bao nhiêu?
   Đây là **mất mát thông tin** do chia ít lớp mà giáo trình cảnh báo ở tr. 117.
2. Trong mô phỏng ở mục 4, đổi `n_s` từ 5 lên 10, 30, 100. Vẽ bảng chênh lệch giữa $E\hat{S}^2$ và
   $\sigma^2$. Từ $n$ bằng bao nhiêu thì chênh lệch dưới 2%?
3. Thay `pop = [1,2,3,4,5]` bằng một tổng thể lệch mạnh, ví dụ `[1,1,1,1,1,1,1,1,1,50]`.
   Công thức (2.10) còn đúng không? (Gợi ý: nó không cần giả thiết chuẩn.)
4. Ở thí dụ 2.2, đổi thành lấy mẫu **3 mảnh** không hoàn lại. $V\overline{X}$ bằng bao nhiêu?
   Kiểm bằng (2.7).
5. Viết hàm tính **hàm phân phối thực nghiệm** $F_n(x)$ cho dữ liệu doanh thu, rồi in giá trị tại
   $x = 40, 50, 60, 70, 80$. So với hàm phân phối chuẩn $N(\overline{X}; s^2)$ — sát nhau không?
   (Đây là ý tưởng của kiểm định phù hợp ở bài 13.)
6. Với dữ liệu doanh thu, tính $\overline{X}$ và $s$ **chỉ trên 10 ngày đầu**, rồi 20, 30, 60 ngày.
   Vẽ bảng. $\overline{X}$ có ổn định dần không? Còn $s$?
7. Thêm một ngày doanh thu **500 triệu** vào dữ liệu. Trung bình, trung vị, $s$ và phân vị 75%
   đổi bao nhiêu phần trăm? Đại lượng nào bền vững nhất?

---

## 12. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)             | Tiếng Anh                       | Ghi chú                            |
| ----------------------------------- | ------------------------------- | ---------------------------------- |
| Thống kê mô tả                      | Descriptive statistics          | §1                                 |
| Tập đám đông, tập nền               | Population                      | cỡ $N$                             |
| Mẫu                                 | Sample                          | cỡ $n$                             |
| Mẫu ngẫu nhiên                      | Random sample                   | độc lập, đồng phân phối (i.i.d.)   |
| Thể hiện của mẫu                    | Realization, observed sample    | $x_1, \dots, x_n$                  |
| Chọn mẫu ngẫu nhiên đơn giản        | Simple random sampling          |                                    |
| Chọn mẫu phân nhóm                  | Stratified sampling             |                                    |
| Chọn mẫu chùm                       | Cluster sampling                |                                    |
| Chọn mẫu có suy luận                | Judgmental / purposive sampling |                                    |
| Mẫu đơn / có tần số / lớp           | Raw / frequency / grouped data  |                                    |
| Tần số                              | Frequency                       | $n_i$                              |
| Tần suất                            | Relative frequency              | $f_i = n_i/n$                      |
| Biểu đồ                             | Histogram                       |                                    |
| Đa giác tần số                      | Frequency polygon               |                                    |
| Hàm phân phối thực nghiệm           | Empirical distribution function | $F_n(x)$                           |
| Thống kê                            | Statistic                       | hàm của mẫu, không chứa tham số ẩn |
| Thống kê hạng                       | Order statistic                 | dãy đã sắp xếp                     |
| Trung bình mẫu                      | Sample mean                     | $\overline{X}$                     |
| Phương sai mẫu                      | Sample variance (biased)        | $\hat{S}^2$, chia $n$              |
| Phương sai mẫu hiệu chỉnh           | Sample variance (unbiased)      | $s^2$, chia $n-1$                  |
| Thừa số hiệu chỉnh tổng thể hữu hạn | Finite population correction    | $\frac{N-n}{N-1}$                  |
| Định lý Glivenko – Cantelli      | Glivenko–Cantelli theorem       | "định lý cơ bản của thống kê"      |
| Thiên lệch sống sót                 | Survivorship bias               | 💼 mục 2                           |

---

## 13. Câu hỏi tự kiểm tra

1. Nêu ba lý do không nghiên cứu toàn bộ tập nền. Lý do nào áp dụng cho việc dự báo doanh thu
   quý sau?
2. Hai điều kiện của **mẫu ngẫu nhiên** là gì? Nêu một tình huống kinh doanh vi phạm điều kiện (i)
   và một tình huống vi phạm điều kiện (ii).
3. Vì sao $\hat{S}^2$ (chia $n$) là ước lượng **chệch** của $\sigma^2$? Giải thích bằng lời,
   không bằng công thức.
4. Với $n = 8$, $s^2 = 14$. Tính $\hat{S}^2$. Chênh lệch bao nhiêu phần trăm?
5. Một khảo sát 400 khách hàng từ tổng thể 2.000 khách. Thừa số hiệu chỉnh bằng bao nhiêu?
   Nó làm sai số tăng hay giảm, và bao nhiêu phần trăm?
6. Vì sao (2.14) có $n-1$ bậc tự do mà không phải $n$? Nếu **biết trước** $a$ thì sao?
7. Doanh thu ngày không tuân theo phân phối chuẩn. Vì sao vẫn dùng được công thức (2.13)?
   Cần điều kiện gì?
8. Một công ty khảo sát khách hàng bằng cách gửi email tới danh sách hiện tại và nhận 200 phản hồi
   trên 5.000 email gửi đi. Nêu **ba** vấn đề về tính đại diện của mẫu này.
9. Cho mẫu lớp có khoảng mốt là 20–30 với tần số 45, khoảng trước tần số 30, khoảng sau tần số 25.
   Tính Mod theo (2.20).

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 10 — MẪU VÀ THỐNG KÊ MÔ TẢ                (Ch. IV §1–2, tr.113–133) ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ⭐ BẢN LỀ CỦA KHOÁ HỌC                                                  ║
║      bài 1–9 : biết luật phân phối → tính xác suất   (chiều XUÔI)        ║
║      bài 10+ : có dữ liệu          → suy luật phân phối (chiều NGƯỢC)    ║
║                                                                          ║
║  TẬP NỀN (N, chưa biết)  ──lấy mẫu──►  MẪU (n, đo được)                  ║
║      không nghiên cứu cả tập nền vì: quá lớn / khó tổ chức / biến động   ║
║                                                                          ║
║  BỐN CÁCH CHỌN MẪU                                                       ║
║      ngẫu nhiên đơn giản  mọi phần tử đồng khả năng — cần biết cả tập    ║
║      phân nhóm            chia nhóm thuần nhất — chủ quan khi chia       ║
║      chùm                 chọn cả cụm — rẻ nhưng sai số lớn hơn          ║
║      có suy luận          chuyên gia — thiếu khách quan                  ║
║      ⚠ THIÊN LỆCH SỐNG SÓT: khảo sát khách còn lại về lý do khách bỏ đi  ║
║                                                                          ║
║  MẪU NGẪU NHIÊN  X₁,...,Xₙ                                               ║
║      (i) ĐỘC LẬP   (ii) CÙNG PHÂN PHỐI với X gốc      (= i.i.d.)         ║
║      ⭐ đúng bằng điều kiện của CLT ở bài 9                              ║
║      THỐNG KÊ = hàm g(X₁,...,Xₙ), KHÔNG chứa tham số chưa biết           ║
║      thống kê cũng là BIẾN NGẪU NHIÊN → có phân phối riêng               ║
║                                                                          ║
║  TRUNG BÌNH MẪU   X̄ = (1/n)Σxᵢ                                           ║
║      E X̄ = a        V X̄ = σ²/n                                           ║
║      không hoàn lại, N nhỏ:  V X̄ = (σ²/n)·(N−n)/(N−1)                    ║
║                                                                          ║
║  ⭐⭐ PHƯƠNG SAI MẪU — HAI CÔNG THỨC                                     ║
║  ┌────────────────┬──────────────┬─────────────┬───────────────┐         ║
║  │                │   chia n     │  chia n−1   │               │         ║
║  ├────────────────┼──────────────┼─────────────┼───────────────┤         ║
║  │ ký hiệu        │     Ŝ²       │     s²      │               │         ║
║  │ E(·)           │ (n−1)/n · σ² │     σ²      │               │         ║
║  │ tính chất      │   CHỆCH      │ KHÔNG CHỆCH │               │         ║
║  │ Excel          │  VAR.P       │   VAR.S     │ ← dùng cái này│         ║
║  └────────────────┴──────────────┴─────────────┴───────────────┘         ║
║      LÝ DO: dùng X̄ thay a làm MẤT MỘT BẬC TỰ DO                          ║
║      n=5 chênh 25% | n=30 chênh 3,4% | n=1000 chênh 0,1%                 ║
║                                                                          ║
║  ⭐ BỐN PHÂN PHỐI MẪU (biến gốc CHUẨN) — nền của bài 11–14               ║
║      (2.13)  (X̄−a)/(σ/√n)        ~ N(0;1)     kỳ vọng, BIẾT σ            ║
║      (2.14)  (n−1)s²/σ²          ~ χ²(n−1)    PHƯƠNG SAI                 ║
║      (2.15)  (X̄−a)√n/s          ~ t(n−1)     kỳ vọng, CHƯA BIẾT σ        ║
║      (2.16)  s₁²/s₂²             ~ F(n₁−1;n₂−1)  SO 2 PHƯƠNG SAI         ║
║                                                                          ║
║      ⭐ n > 30 thì KHÔNG CẦN giả thiết chuẩn (nhờ CLT)                   ║
║      Glivenko–Cantelli:  sup|Fₙ(x) − F(x)| → 0  "định lý cơ bản"         ║
║                                                                          ║
║  MẪU LỚP    Mod = x_mo + d₁/(d₁+d₂)·h                                    ║
║             Med = x_me + (n/2 − n_tl)/n_me · h                           ║
║                                                                          ║
║  📚 KÝ HIỆU — nhầm ở đây là sai từ bài 11 trở đi                         ║
║      HY LẠP  a, σ, ρ  → tham số TỔNG THỂ: cố định, CHƯA BIẾT             ║
║      LA-TINH X̄, s, r  → thống kê MẪU: đo được, NGẪU NHIÊN                ║
║                                                                          ║
║  ⚠ ĐÍNH CHÍNH tr.132 thí dụ 2.4:  Σ = 300 (không phải 150)               ║
║      X̄ = 134,2833 | d₁ = 19, d₂ = 29 | Mod = 134,4792                    ║
║                                                                          ║
║  💼 QTKD  luôn dùng STDEV.S / VAR.S                                      ║
║          tách nhóm trước khi kết luận: TB chung giấu cả câu chuyện       ║
║          số lớp của histogram có thể làm lộ hoặc giấu đỉnh thứ hai       ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương IV §1–§2, tr. 113–133.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Đính chính thí dụ 2.4 (tr. 132): đã đối chiếu bản quét gốc. Hàng Σ in `150` (đúng: 300);
  $\overline{X}$ in `134,2823` (đúng: 134,2833); $d_l$ in `93 − 74 = 9` và $d_s$ in `93 − 64 = 19`
  (đúng: 19 và 29), kéo theo Mod in `134,1072` (đúng: 134,4792).
- Dữ liệu: `chieu_cao_hoc_sinh.csv` (thí dụ 1.1) và `can_nang_vit.csv` (thí dụ 2.3) là số liệu
  nguyên văn của giáo trình. `doanh_thu_ngay.csv` là **dữ liệu mô phỏng** cho phần 💼.
- Mục 9 (bảng ký hiệu mẫu vs tổng thể) và bảng đối chiếu Excel: kiến thức bổ sung.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 9 — Luật số lớn và định lý giới hạn trung tâm](bai_09_luat_so_lon_va_dinh_ly_gioi_han_trung_tam.md) ·
Bài sau: Bài 11 — Ước lượng điểm và khoảng tin cậy
