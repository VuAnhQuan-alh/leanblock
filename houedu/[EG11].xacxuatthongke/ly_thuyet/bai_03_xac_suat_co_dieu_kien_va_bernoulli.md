# Bài 3 — Xác suất có điều kiện và công thức Bernoulli

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương I §3**, tr. 18–29.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính hai lỗi in** của giáo trình: thí dụ 3.11 (tr. 27) và thí dụ 3.12 (tr. 27).
> 📌 **Cần đọc trước:** [Bài 1](bai_01_su_kien_ngau_nhien_va_giai_tich_ket_hop.md) · [Bài 2](bai_02_ba_dinh_nghia_cua_xac_suat.md)

Đây là bài dài nhất và **quan trọng nhất** của Chương I. Nó cho bạn bốn công cụ:

- **Xác suất có điều kiện** — cập nhật niềm tin khi có thông tin mới.
- **Độc lập** — biết khi nào được phép nhân xác suất, và khi nào không.
- **Công thức cộng và nhân** — hai cỗ máy tính xác suất của sự kiện phức tạp.
- **Lược đồ Bernoulli** — bộ công thức cho "lặp $n$ lần cùng một việc", có mặt ở mọi bài toán
  chất lượng, telesales, quảng cáo.

## Mục lục

1. [Xác suất có điều kiện](#1-xác-suất-có-điều-kiện)
2. [Độc lập từng đôi và độc lập trong tổng thể](#2-độc-lập-từng-đôi-và-độc-lập-trong-tổng-thể)
3. [Công thức nhân xác suất](#3-công-thức-nhân-xác-suất)
4. [Công thức cộng xác suất](#4-công-thức-cộng-xác-suất)
5. [Năm thí dụ mẫu của giáo trình](#5-năm-thí-dụ-mẫu-của-giáo-trình)
6. [Lược đồ và công thức Bernoulli](#6-lược-đồ-và-công-thức-bernoulli)
7. [Ba cách xấp xỉ khi n lớn](#7-ba-cách-xấp-xỉ-khi-n-lớn)
8. [📚 Hiệu chỉnh liên tục](#8--hiệu-chỉnh-liên-tục)
9. [Code minh hoạ](#9-code-minh-hoạ)
10. [Tự thử](#10-tự-thử)
11. [Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
12. [Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Xác suất có điều kiện

Giáo trình mở đầu bằng một nhận xét đáng suy nghĩ (tr. 18):

> "Thực ra **mọi** xác suất $P(A)$ đều là có điều kiện, vì sự kiện $A$ xảy ra khi thực hiện một bộ
> điều kiện xác định."

Nghĩa là: $P(A)$ luôn ngầm hiểu là "xác suất của $A$ *trong bộ điều kiện đang xét*". Khi có thêm
điều kiện mới — thể hiện bằng việc **đã biết $B$ xảy ra** — ta cần ký hiệu riêng: $P(A \mid B)$.

**Định nghĩa 1 (tr. 19).** Giả sử $P(B) > 0$. Xác suất có điều kiện của $A$, biết rằng đã có $B$:

$$P(A \mid B) = \frac{P(AB)}{P(B)} \tag{3.1}$$

### Hằng số $k$ đến từ đâu

Giáo trình dẫn dắt công thức này rất hay, đáng đọc kỹ (tr. 18–19). Trực giác: khi biết $B$ đã xảy ra,
"khả năng" xuất hiện $A$ nên **tỷ lệ với** $P(AB)$ — vì chỉ phần của $A$ nằm trong $B$ mới còn ý nghĩa.
Vậy đặt

$$P(A \mid B) = k \cdot P(AB), \quad k > 0$$

Xác định $k$ bằng cách chọn $A = B$: hiển nhiên $P(B \mid B) = 1$, mà $P(BB) = P(B)$, nên
$k \cdot P(B) = 1$, tức $k = 1/P(B)$. Thay vào ta được (3.1). ∎

**Cách hiểu bằng hình ảnh — hiệu quả hơn nhớ công thức:**

> Biết $B$ đã xảy ra nghĩa là **thu hẹp không gian mẫu** từ $\Omega$ xuống còn $B$.
> Rồi đếm lại trong không gian mới đó.

```
   Trước khi biết B:              Sau khi biết B:
   ┌──────── Ω ────────┐          ┌── B ──┐       ← Ω mới là B
   │  ┌───┐            │          │ ┌───┐ │
   │  │ A │ ┌── B ──┐  │    ──►   │ │ AB│ │       ← chỉ phần AB còn sống
   │  │  ┌┼─┼─ AB   │  │          │ └───┘ │
   │  └──┴┘ └───────┘  │          └───────┘
   └───────────────────┘
      P(A) = A / Ω                  P(A|B) = AB / B
```

Giáo trình lưu ý hai điều (tr. 19):

- Nói chung $P(A) \ne P(A \mid B)$ — biết thêm thông tin thì xác suất **thay đổi**.
- $P(A \mid B)$ có **mọi tính chất của một xác suất bình thường** (5 tính chất ở bài 2 mục 2 đều đúng).

**Hai trường hợp cực đoan**, dễ suy ra từ hình vẽ:

$$AB = V \Rightarrow P(A \mid B) = 0, \qquad B \Rightarrow A \ \text{ thì } \ P(A \mid B) = 1$$

### Thí dụ 3.1 (tr. 19)

> Gieo 2 con xúc sắc. Tính xác suất tổng số chấm bằng 6, **biết rằng** tổng đó là số chẵn.

*Giải.* Ở bài 2 ta đã có $P(A) = 5/36$ với $A$ = "tổng bằng 6". Gọi $B$ = "tổng chẵn".
Điều kiện đã thay đổi: tổng chẵn chỉ tương ứng với **18** kết cục trong 36.

$$P(A \mid B) = \frac{5}{18}$$

Đối chiếu với công thức (3.1): $P(AB) = P(A) = 5/36$ (vì tổng bằng 6 thì đương nhiên chẵn,
tức $A \Rightarrow B$ nên $AB = A$), $P(B) = 1/2$. Vậy $P(A \mid B) = \dfrac{5/36}{1/2} = \dfrac{5}{18}$. ✓

Chú ý: biết thêm "tổng chẵn" đã làm xác suất **tăng** từ $0{,}139$ lên $0{,}278$ — gấp đôi.
Thông tin có giá trị.

### Thí dụ 3.2 (tr. 19)

> Rút lần lượt 2 con bài từ bộ 52 con. Tìm xác suất con thứ hai là át, **biết rằng** con thứ nhất
> đã là át.

*Giải.* Gọi $A_i$ = "con thứ $i$ là át". Đã rút mất một con át, còn lại 51 con với 3 con át:

$$P(A_2 \mid A_1) = \frac{3}{51} = \frac{1}{17}$$

⚠️ **So sánh thí dụ này với thí dụ 2.3c của bài 2** — hai bài rất giống nhau nhưng đáp số khác hẳn:

|                             | Thí dụ 2.3c                             | Thí dụ 3.2                                           |
| --------------------------- | --------------------------------------- | ---------------------------------------------------- |
| Câu hỏi                     | viên thứ hai đỏ                         | con thứ hai là át, **biết** con đầu là át            |
| Có quan sát viên đầu không? | **không**                               | **có**                                               |
| Đáp số                      | $6/10 = 0{,}6$ (bằng xác suất viên đầu) | $3/51 \approx 0{,}059$ (khác $4/52 \approx 0{,}077$) |

**Bài học:** vị trí trong dãy rút *không* làm đổi xác suất; **quan sát** mới làm đổi.
Nếu bịt mắt rút thì viên nào cũng như nhau. Mở mắt nhìn viên đầu thì viên thứ hai đổi.

### 💼 Góc QTKD

Đây là công thức **nền tảng của mọi phân tích phễu bán hàng (sales funnel)**.

Website tháng vừa rồi: 10.000 lượt truy cập, 800 lượt thêm hàng vào giỏ, 240 đơn thanh toán thành công.

$$
\begin{aligned}
P(\text{thêm giỏ}) &= \frac{800}{10\,000} = 8\% \\
P(\text{thanh toán}) &= \frac{240}{10\,000} = 2{,}4\% \\
P(\text{thanh toán} \mid \text{thêm giỏ}) &= \frac{240}{800} = 30\%
\end{aligned}
$$

Con số thứ ba là con số **hành động được**. Nó nói: trong 100 người đã bỏ hàng vào giỏ, 70 người
bỏ đi. Đó là chỗ mất tiền lớn nhất, và cũng là chỗ dễ sửa nhất (phí ship bất ngờ, bắt đăng ký
tài khoản, form thanh toán rườm rà).

Hai con số đầu chỉ nói "shop kém"; con số thứ ba chỉ đúng **khâu nào** kém. Đó là toàn bộ giá trị
của xác suất có điều kiện trong kinh doanh: **thu hẹp không gian mẫu để nhìn rõ vấn đề**.

---

## 2. Độc lập từng đôi và độc lập trong tổng thể

**Định nghĩa 2 (tr. 19).** $A$ và $B$ **độc lập (thống kê)** nếu

$$P(A \mid B) = P(A) \quad \text{hoặc} \quad P(B \mid A) = P(B) \tag{3.2}$$

Nghĩa: việc xuất hiện sự kiện này **không làm thay đổi** xác suất của sự kiện kia.

Thay (3.1) vào (3.2) được dạng đối xứng, dễ dùng hơn nhiều:

$$P(AB) = P(A) \cdot P(B) \tag{3.3}$$

⚠️ Giáo trình cảnh báo rất thật (tr. 19–20): "việc kiểm tra tính chất (3.2) trong thực tiễn
**rất khó khăn** và trong nhiều trường hợp là **không thể**. Vì vậy dựa vào thực tế và trực giác
mà ta thừa nhận các sự kiện độc lập trong các bài tập sau này."

Nói cách khác: trong bài tập, **độc lập là một giả thiết bạn được cho, không phải thứ bạn chứng minh.**
Đề bài phải nói "các linh kiện làm việc độc lập", "kết quả mỗi lần sinh là độc lập". Không nói thì
đừng tự ý nhân.

**Định nghĩa 3 (tr. 20).** Bộ sự kiện $A_1, A_2, \dots, A_n$ **độc lập trong tổng thể** nếu

$$P(A_{i_1} A_{i_2} \cdots A_{i_k}) = P(A_{i_1}) P(A_{i_2}) \cdots P(A_{i_k}) \tag{3.4}$$

với **mọi** dãy $(i_1, \dots, i_k)$ gồm các số nguyên khác nhau lấy từ $\{1, 2, \dots, n\}$.

Chú ý chữ "mọi": phải kiểm tất cả các nhóm 2 phần tử, 3 phần tử, ..., $n$ phần tử.

### Thí dụ 3.3 (tr. 20) — phản ví dụ của Bernstein

> Gieo hai lần một đồng tiền, 4 kết cục đồng khả năng ($S$ = sấp, $N$ = ngửa):
> $\Omega = \{SS, SN, NS, NN\}$. Đặt $A = SS + SN$, $B = SS + NS$, $C = SS + NN$.

*Giải.* Cả ba đều có $P = 1/2$. Kiểm từng đôi:

$$P(AB) = P(AC) = P(BC) = \frac{1}{4} = \frac{1}{2} \cdot \frac{1}{2} \ \checkmark$$

Vậy chúng **độc lập từng đôi**. Nhưng:

$$P(ABC) = P(SS) = \frac{1}{4} \neq P(A)P(B)P(C) = \frac{1}{8}$$

Vậy chúng **không độc lập trong tổng thể**.

Giáo trình kết luận (tr. 20): *"Khái niệm độc lập trong tổng thể kéo theo độc lập từng đôi ...,
nhưng ngược lại nói chung không đúng."*

$$\text{độc lập tổng thể} \Longrightarrow \text{độc lập từng đôi}, \qquad \text{chiều ngược lại: SAI}$$

**Vì sao ví dụ này lại chạy được?** Vì $A$ = "lần 1 sấp", $B$ = "lần 2 sấp", $C$ = "hai lần giống nhau".
Biết $A$ không nói gì về $B$; biết $A$ không nói gì về $C$. Nhưng biết **cả $A$ và $B$** thì đã biết
chắc $C$ — thông tin nằm ở *tổ hợp*, không nằm ở từng cặp.

### 💼 Góc QTKD

Ba rủi ro của một chuỗi bán lẻ:

- $A$ = "giá nhập nguyên liệu tăng"
- $B$ = "chi phí vận chuyển tăng"
- $C$ = "biên lợi nhuận tụt xuống dưới ngưỡng"

Từng cặp có thể trông độc lập trên số liệu quá khứ. Nhưng $A$ và $B$ **cùng xảy ra** thì $C$ gần
như chắc chắn. Nếu mô hình rủi ro của bạn chỉ kiểm tra tương quan từng đôi, nó sẽ báo "ba rủi ro
độc lập" và đánh giá thấp nghiêm trọng khả năng khủng hoảng.

**Đây chính là cơ chế đã gây ra khủng hoảng tài chính 2008:** các mô hình định giá chứng khoán
đảm bảo bằng nợ giả định các khoản vay thế chấp độc lập với nhau. Từng cặp thì gần đúng; nhưng khi
toàn thị trường nhà đất đi xuống thì tất cả cùng vỡ nợ một lúc. Độc lập từng đôi không cứu được ai.

---

## 3. Công thức nhân xác suất

Suy trực tiếp từ (3.1), chỉ là chuyển vế:

$$P(AB) = P(A)\,P(B \mid A) = P(B)\,P(A \mid B) \tag{3.5}$$

Ba hệ quả (tr. 21):

**(i) Nếu $A$, $B$ độc lập:** $P(AB) = P(A)P(B)$ — chính là (3.3).

**(ii) Mở rộng cho tích $n$ sự kiện** — công thức *dây chuyền*:

$$P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1}) \tag{3.6}$$

**(iii) Nếu $A_1, \dots, A_n$ độc lập trong tổng thể:**

$$P\left(\prod_{i=1}^{n} A_i\right) = \prod_{i=1}^{n} P(A_i)$$

Công thức (3.6) đọc như một câu chuyện kể theo thời gian: *xác suất để cả dây chuyền xảy ra
= xác suất bước 1 × xác suất bước 2 khi đã có bước 1 × xác suất bước 3 khi đã có hai bước đầu × ...*

### 💼 Góc QTKD

Công thức (3.6) **chính là mô hình phễu bán hàng**, không cần đổi một chữ:

$$
\begin{aligned}
P(\text{ra đơn}) &= P(\text{truy cập}) \times P(\text{xem sản phẩm} \mid \text{truy cập}) \\
&\quad \times P(\text{thêm giỏ} \mid \text{xem}) \times P(\text{thanh toán} \mid \text{thêm giỏ})
\end{aligned}
$$

Với số liệu $1{,}0 \times 0{,}45 \times 0{,}18 \times 0{,}30 = 0{,}0243$, tức 2,43%.

Vì các thừa số đều nhỏ hơn 1, **thêm một bước vào phễu luôn làm giảm tỷ lệ chuyển đổi**.
Đó là lý do định lượng cho nguyên tắc thiết kế "one-click checkout": mỗi bước bạn bắt khách làm thêm
là một thừa số $< 1$ nữa nhân vào.

Và nó cũng cho biết **nên tối ưu khâu nào**: cải thiện khâu $0{,}18$ lên $0{,}22$ (tăng 22% tương đối)
làm tổng tăng lên 2,97%; trong khi cải thiện khâu $0{,}45$ lên $0{,}49$ (cũng tăng 9% tương đối)
chỉ đưa tổng lên 2,65%. **Khâu yếu nhất không phải lúc nào cũng là khâu đáng sửa nhất — hãy nhân thử.**

---

## 4. Công thức cộng xác suất

$$P(A + B) = P(A) + P(B) - P(AB) \tag{3.7}$$

**Vì sao phải trừ $P(AB)$?** Vì khi cộng $P(A)$ với $P(B)$, phần giao $AB$ bị **đếm hai lần**.
Trừ đi một lần cho đúng.

```
      ┌───────A───────┐
      │        ┌──────┼────B──────┐
      │        │  AB  │           │      P(A) đếm cả AB
      │        │      │           │      P(B) đếm cả AB
      └────────┼──────┘           │      cộng vào → AB đếm 2 lần
               └──────────────────┘      → phải trừ 1 lần
```

Ba hệ quả (tr. 21):

**(i) Nếu $A$, $B$ xung khắc:** $AB = V$ nên $P(AB) = 0$, còn lại $P(A+B) = P(A) + P(B)$.

**(ii) Mở rộng cho tổng $n$ sự kiện** — công thức *bao hàm – loại trừ*:

$$P\left(\sum_{i=1}^n A_i\right) = \sum_i P(A_i) - \sum_{i<j} P(A_iA_j) + \sum_{i<j<k} P(A_iA_jA_k) - \cdots + (-1)^{n-1} P(A_1A_2\cdots A_n) \tag{3.8}$$

Cộng đơn, trừ đôi, cộng ba, trừ bốn... dấu đan xen.

**(iii) Nếu $A_1, \dots, A_n$ xung khắc từng đôi:** mọi số hạng giao đều bằng 0, chỉ còn tổng đơn.

⚠️ **Lỗi sai phổ biến nhất trong bài thi:** dùng $P(A+B) = P(A) + P(B)$ khi $A$, $B$ **không** xung khắc.
Dấu hiệu nhận biết: nếu cộng ra kết quả **lớn hơn 1** thì chắc chắn bạn đã quên trừ giao.

### 💼 Góc QTKD

Chiến dịch chạy song song 2 kênh. Facebook tiếp cận 60% khách mục tiêu, Google 55%,
và 30% khách nhìn thấy quảng cáo trên **cả hai** kênh.

$$P(\text{tiếp cận được}) = 0{,}60 + 0{,}55 - 0{,}30 = 0{,}85$$

**85%, không phải 115%.** Con số 115% là thứ mà báo cáo marketing hay đưa ra khi cộng "reach"
của từng kênh — gọi là *reach trùng lặp*. Công thức (3.7) chính là cách khử trùng lặp.

Ngược lại, nếu biết reach thật là 85% mà từng kênh báo 60% và 55%, bạn **suy ngược ra** được
mức trùng lặp: $0{,}60 + 0{,}55 - 0{,}85 = 0{,}30$. Trùng lặp 30% nghĩa là gần một nửa ngân sách
Facebook đang chi cho người đã thấy quảng cáo Google — cơ sở để cắt ngân sách.

---

## 5. Năm thí dụ mẫu của giáo trình

### Thí dụ 3.4 (tr. 21) — độc lập hay không, đổi cả đáp số

> Hai cọc bài lấy từ bộ tú lơ khơ: cọc I gồm 4 con át, cọc II gồm 4 con ka.
> Rút ngẫu nhiên từ mỗi cọc một con. Tính xác suất: a) cả 2 con là cơ; b) có ít nhất 1 con cơ.
> Cũng câu hỏi đó nhưng **trộn hai cọc lại** rồi rút hú hoạ 2 con.

*Giải.* Gọi $A$ = "con thứ nhất là cơ", $B$ = "con thứ hai là cơ". Cả hai trường hợp đều có
$P(A) = P(B) = 1/4$ (cọc riêng: 1 con cơ trong 4; cọc trộn: 2 con cơ trong 8).

**Hai cọc riêng — $A$, $B$ độc lập:**

$$
\text{a) } P(AB) = \frac{1}{4}\cdot\frac{1}{4} = \frac{1}{16}, \qquad
\text{b) } P(A+B) = \frac{1}{4}+\frac{1}{4}-\frac{1}{16} = \frac{7}{16}
$$

**Trộn cọc — $A$, $B$ KHÔNG còn độc lập** (rút mất con cơ thì cọc còn ít con cơ hơn):

$$
\text{a) } P(AB) = P(A)P(B \mid A) = \frac{1}{4}\cdot\frac{1}{7} = \frac{1}{28}, \qquad
\text{b) } P(A+B) = \frac{1}{4}+\frac{1}{4}-\frac{1}{28} = \frac{13}{28}
$$

**Đây là thí dụ đắt giá nhất của mục này**: cùng đề bài, cùng $P(A)$, cùng $P(B)$, nhưng đáp số
khác nhau vì cấu trúc phụ thuộc khác nhau. Trong QTKD: lấy mẫu **có hoàn lại** (độc lập) khác
lấy mẫu **không hoàn lại** (phụ thuộc). Với lô hàng lớn thì chênh lệch nhỏ; với lô nhỏ thì lớn.

### Thí dụ 3.5 (tr. 22) — ba xạ thủ

> Ba xạ thủ mỗi người bắn một viên, xác suất trúng lần lượt 0,7; 0,8; 0,9.
> a) có **đúng hai** người bắn trúng; b) có **ít nhất một** người bắn trượt.

*Giải.* $A_i$ = "xạ thủ $i$ bắn trúng".

**a)** $A = A_1A_2\overline{A_3} + A_1\overline{A_2}A_3 + \overline{A_1}A_2A_3$ — ba số hạng
**xung khắc** (không thể vừa "trúng 1,2 trượt 3" vừa "trúng 1,3 trượt 2"), và trong mỗi số hạng
các $A_i$ **độc lập**. Vậy:

$$
\begin{aligned}
P(A) &= 0{,}7 \cdot 0{,}8 \cdot 0{,}1 + 0{,}7 \cdot 0{,}2 \cdot 0{,}9 + 0{,}3 \cdot 0{,}8 \cdot 0{,}9 \\
&= 0{,}056 + 0{,}126 + 0{,}216 = \mathbf{0{,}398}
\end{aligned}
$$

**b)** Giáo trình chỉ rõ: tính $P(\overline{B})$ **dễ dàng hơn nhiều** so với tính trực tiếp.
$\overline{B}$ = "không ai bắn trượt" = "cả ba đều trúng".

$$P(B) = 1 - 0{,}7 \cdot 0{,}8 \cdot 0{,}9 = 1 - 0{,}504 = \mathbf{0{,}496}$$

**Đây là khuôn mẫu giải bài chuẩn**, nhớ kỹ hai dòng:
- "có đúng $k$ cái" → liệt kê các tổ hợp, dùng **xung khắc + độc lập**.
- "có ít nhất một" → **lấy 1 trừ đi** trường hợp đối lập.

### Thí dụ 3.6 (tr. 23) — mạch 4 linh kiện

> Mạch gồm 4 linh kiện, xác suất **hỏng** lần lượt 0,2; 0,1; 0,05; 0,02. Tìm xác suất mạng hoạt
> động tốt, giả thiết các linh kiện làm việc độc lập và dây luôn tốt.

*Giải.* $A_i$ = "linh kiện $i$ làm việc tốt", nên $P(A_i) = 0{,}8; 0{,}9; 0{,}95; 0{,}98$.
Từ sơ đồ (hình 1.3):

$$A = A_1(A_2 + A_3)A_4$$

$A_1$, $A_4$ và $(A_2 + A_3)$ độc lập với nhau, nên:

$$P(A) = P(A_1) \cdot P(A_2 + A_3) \cdot P(A_4) \tag{3.9}$$

⚠️ **Chỗ dễ sai:** $A_2$ và $A_3$ **không xung khắc** (cả hai cùng tốt là chuyện bình thường!),
nên phải dùng (3.7):

$$P(A_2 + A_3) = 0{,}9 + 0{,}95 - 0{,}9 \cdot 0{,}95 = 0{,}995$$

Nếu cộng bừa sẽ ra $1{,}85 > 1$ — vô nghĩa ngay lập tức. Thay vào (3.9):

$$P(A) = 0{,}8 \cdot 0{,}995 \cdot 0{,}98 = \mathbf{0{,}78008}$$

💼 Đọc theo ngôn ngữ quản trị: linh kiện 2 và 3 mắc **song song** (dự phòng cho nhau) nên độ tin cậy
tổ hợp là 0,995 — cao hơn cả hai. Linh kiện 1 và 4 mắc **nối tiếp** (điểm chết đơn) nên độ tin cậy
tổ hợp *thấp hơn* từng cái. Cả hệ chỉ đạt 78% vì linh kiện 1 yếu (80%).

**Muốn cải thiện hệ thống, hãy nhân thử:** thêm dự phòng cho linh kiện 1 (biến 0,8 thành
$0{,}8 + 0{,}8 - 0{,}64 = 0{,}96$) đẩy cả hệ lên $0{,}96 \cdot 0{,}995 \cdot 0{,}98 = 0{,}936$.
Đầu tư đúng chỗ tăng 16 điểm phần trăm.

### Thí dụ 3.7 (tr. 24) — gia đình 6 con

> Một gia đình có 6 con. Tìm xác suất để số con trai **nhiều hơn** số con gái.

*Giải.* Giáo trình dùng một mẹo đối xứng rất đẹp thay vì cộng ba trường hợp.
Gọi $A$ = "trai > gái", $B$ = "gái > trai", $C$ = "bằng nhau". Ta có $A + B + C = U$ nên

$$P(A) + P(B) + P(C) = 1$$

Do **tính đối xứng** của việc sinh trai/gái (đều xác suất 0,5), $P(A) = P(B)$, suy ra:

$$P(A) = \frac{1 - P(C)}{2}$$

Còn $P(C)$ = xác suất có đúng 3 trai 3 gái. Một trường hợp cụ thể có xác suất $(1/2)^6 = 1/64$,
và có $C_6^3 = 20$ khả năng, nên $P(C) = 20/64 = 5/16$. Vậy:

$$P(A) = \frac{1 - 5/16}{2} = \frac{11}{32} \approx 0{,}344$$

**Bài học:** tìm đối xứng trước khi tính. Ở đây mẹo này thay 3 phép tính bằng 1.

### Thí dụ 3.8 (tr. 25) — bài toán bỏ thư, và số $e$

> Viết $n$ lá thư cho $n$ người khác nhau, bỏ ngẫu nhiên vào $n$ phong bì đã ghi sẵn địa chỉ.
> Tìm xác suất có **ít nhất một** lá thư đúng phong bì.

*Giải.* $A_i$ = "thư thứ $i$ đúng phong bì". Các $A_i$ **không xung khắc**, nên phải dùng (3.8).
Giáo trình tính từng lớp:

$$P(A_i) = \frac{(n-1)!}{n!}, \quad P(A_iA_j) = \frac{(n-2)!}{n!}, \quad P(A_iA_jA_k) = \frac{(n-3)!}{n!}, \ \dots$$

Nhân với số lượng nhóm mỗi lớp ($C_n^1$, $C_n^2$, $C_n^3$, ...) rồi thay vào (3.8), các giai thừa
triệt tiêu gọn gàng:

$$P(A) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n-1}\frac{1}{n!}$$

Và khi $n$ khá lớn:

$$P(A) \approx 1 - \frac{1}{e} \approx 0{,}632$$

**Kết quả gây bất ngờ nhất chương I:** dù có 5 lá thư hay 5 triệu lá thư, xác suất có ít nhất một
lá về đúng địa chỉ luôn xấp xỉ **63,2%** — không giảm về 0 như trực giác mách bảo.

💼 Trong QTKD kết quả này có tên là **bài toán ghép cặp ngẫu nhiên**: bốc thăm tặng quà nội bộ
(mỗi người rút tên một đồng nghiệp), xếp ngẫu nhiên nhân viên vào ca. Xác suất "có ít nhất một
người rút trúng tên chính mình" luôn khoảng 63% — nên nếu tổ chức Secret Santa mà không có cơ chế
loại trừ, gần như chắc chắn phải bốc lại.

### Thí dụ 3.9 (tr. 26) — gieo $n$ lần

> Tìm xác suất xuất hiện **ít nhất 1 lần** hai mặt 6 chấm khi gieo $n$ lần 2 con xúc sắc.

*Giải.* Một lần gieo: $P(\text{hai mặt 6}) = 1/36$. Dùng đối lập:

$$P(\overline{A}) = \left(1 - \frac{1}{36}\right)^n = \left(\frac{35}{36}\right)^n
\ \Rightarrow \ P(A) = 1 - \left(\frac{35}{36}\right)^n$$

**Khuôn mẫu "ít nhất 1 lần trong $n$ lần thử độc lập"** — dùng cực nhiều:

$$\boxed{P(\text{ít nhất 1 lần trong } n \text{ lần}) = 1 - (1-p)^n}$$

---

## 6. Lược đồ và công thức Bernoulli

**Lược đồ Bernoulli (tr. 26)** — ba điều kiện phải kiểm đủ:

1. Dãy $n$ phép thử **độc lập**, **giống nhau**.
2. Mỗi phép thử chỉ có **hai kết cục**: xảy ra $A$ hoặc không.
3. $P(A) = p$ **không phụ thuộc số thứ tự** của phép thử; $P(\overline{A}) = 1 - p = q$.

**Công thức Bernoulli.** Xác suất để trong $n$ phép thử, $A$ xuất hiện **đúng $k$ lần**:

$$P_n(k) = C_n^k \, p^k q^{n-k}, \qquad k = 0, 1, \dots, n \tag{3.10}$$

Cách nhớ, đọc từ phải sang trái:
- $p^k q^{n-k}$ — xác suất của **một** kịch bản cụ thể ($k$ lần thành công, $n-k$ lần thất bại);
- $C_n^k$ — **số kịch bản** như vậy (chọn $k$ vị trí thành công trong $n$ vị trí).

Xác suất để $A$ xuất hiện **từ $k_1$ đến $k_2$ lần**:

$$P_n(k_1, k_2) = \sum_{k=k_1}^{k_2} C_n^k p^k q^{n-k} \tag{3.11}$$

Giáo trình nhấn mạnh: dùng (3.10) **đơn giản hơn nhiều** so với các công thức (3.5)–(3.8), vì vậy
"nó có ý nghĩa thực tiễn rất lớn".

### Thí dụ 3.10 (tr. 26) — và một cái bẫy đọc đề

> Một thiết bị có 10 chi tiết, độ tin cậy mỗi chi tiết là 0,9. Tìm xác suất **đúng 2** chi tiết
> làm việc tốt.

*Giải.* $n = 10$, $p = 0{,}9$, $k = 2$:

$$P_{10}(2) = C_{10}^2 (0{,}9)^2 (0{,}1)^8 = 45 \cdot 0{,}81 \cdot 10^{-8} = 3645 \times 10^{-10}$$

Tức $0{,}0000003645$ — **cực kỳ nhỏ**. Hợp lý: mỗi chi tiết tốt tới 90%, mà đòi chỉ 2 trong 10 cái tốt
thì phải 8 cái cùng hỏng — gần như không xảy ra.

⚠️ Nhiều bạn đọc lướt thành "đúng 2 chi tiết **hỏng**" và tính $C_{10}^2(0{,}1)^2(0{,}9)^8 = 0{,}194$.
Lệch nhau **hơn 500.000 lần**. Đọc kỹ: $p$ trong công thức phải là xác suất của **đúng cái sự kiện
mà bạn đang đếm số lần**.

### Thí dụ 3.11 (tr. 27) — ⚠️ có lỗi in

> Một bác sỹ có xác suất chữa khỏi bệnh là 0,8. Có người nói cứ 10 người đến chữa thì **chắc chắn**
> 8 người khỏi; điều đó đúng không?

*Giải.* Câu khẳng định **sai**. Đây là lược đồ Bernoulli với $n = 10$, $p = 0{,}8$, $k = 8$:

$$P_{10}(8) = C_{10}^8 (0{,}8)^8 (0{,}2)^2 = 45 \cdot 0{,}16777216 \cdot 0{,}04 = \mathbf{0{,}3020}$$

⚠️ **Đính chính.** Sách in kết quả là **0,3108**. Đã đối chiếu bản quét gốc trang 27: công thức viết
đúng, chỉ **kết quả số bị sai**. Giá trị đúng là **0,3020**. Khi làm bài, dùng 0,3020.

Điều này không phá hỏng bài học — ngược lại, **con số nhỏ hơn còn củng cố bài học**: chỉ khoảng
**30%** khả năng có đúng 8 người khỏi. Xác suất 0,8 nói về **xu hướng dài hạn**, không phải lời hứa
cho từng nhóm 10 người.

💼 Đây là **hiểu lầm phổ biến nhất về xác suất trong kinh doanh**: "tỷ lệ chốt đơn 20%, gọi 10 cuộc
là được 2 đơn". Sai. Với $n = 10$, $p = 0{,}2$: $P_{10}(2) = C_{10}^2(0{,}2)^2(0{,}8)^8 = 0{,}302$.
Cũng chỉ 30%. Còn xác suất **không được đơn nào** là $(0{,}8)^{10} = 0{,}107$ — hơn 1 trên 10 nhân
viên telesales sẽ có một ngày trắng tay dù làm đúng quy trình. Biết điều này giúp bạn không sa thải
oan người giỏi vì một ngày xui.

### Thí dụ 3.12 (tr. 27) — ⚠️ có lỗi in

> Tỷ lệ phế phẩm của một lô hàng là 1%. Cỡ mẫu cần chọn ra là bao nhiêu (**có hoàn lại**) sao cho
> trong mẫu có ít nhất 1 phế phẩm với xác suất lớn hơn 0,95?

*Giải.* Chọn có hoàn lại → lược đồ Bernoulli với $p = 0{,}01$. Dùng khuôn mẫu "ít nhất 1 lần":

$$1 - 0{,}99^n > 0{,}95 \iff 0{,}05 > 0{,}99^n \iff n > \frac{\log 0{,}05}{\log 0{,}99}$$

$$\frac{\log 0{,}05}{\log 0{,}99} = 298{,}0729\ldots \ \Rightarrow \ n_{\min} = \mathbf{299}$$

⚠️ **Đính chính.** Sách in $\approx \mathbf{296}$. Đã đối chiếu bản quét gốc trang 27: công thức đúng,
kết quả số sai. Giá trị đúng là 298,07, nên cỡ mẫu tối thiểu là **299**. Kiểm lại:

$$1 - 0{,}99^{298} = 0{,}949963 \ (\text{chưa đạt}), \qquad 1 - 0{,}99^{299} = 0{,}950464 \ (\text{đạt})$$

💼 **Đây là bài toán cỡ mẫu QC kinh điển**, và kết quả rất phản trực giác: để **95% chắc chắn** phát
hiện được lỗi khi tỷ lệ lỗi chỉ 1%, bạn phải kiểm **gần 300 sản phẩm**. Kiểm 100 sản phẩm chỉ cho
$1 - 0{,}99^{100} = 63{,}4\%$ — nghĩa là hơn 1/3 khả năng lô hàng lỗi lọt qua.

Quy tắc ngón tay cái rút ra từ công thức: **muốn 95% chắc chắn bắt được lỗi tỷ lệ $p$, cần cỡ mẫu
khoảng $3/p$.** Lỗi 1% → 300 mẫu; lỗi 0,1% → 3.000 mẫu. Chi phí kiểm tra tăng tuyến tính khi
yêu cầu chất lượng khắt khe hơn — đó là lý do kinh tế khiến "zero defect" đắt đến vậy.

---

## 7. Ba cách xấp xỉ khi n lớn

Giáo trình nhận xét (tr. 28): khi $n$ và $k$ khá lớn, tính theo (3.10) và (3.11) **rất cồng kềnh**.
Thời chưa có máy tính, $C_{100}^{75}$ là con số 26 chữ số — không tính tay được. Nên có ba xấp xỉ:

### (i) Xấp xỉ Poisson — khi $n$ **rất lớn**, $p$ **rất nhỏ**

$$P_n(k) \approx \frac{e^{-\lambda}\lambda^k}{k!}, \qquad \lambda = np \tag{3.12}$$

**Thí dụ 3.13 (tr. 28).** Xác suất sản xuất ra phế phẩm của một máy là 0,005. Tìm xác suất trong
800 sản phẩm có **đúng 3** phế phẩm.

$$\lambda = np = 800 \cdot 0{,}005 = 4, \qquad P_{800}(3) \approx \frac{e^{-4} \cdot 4^3}{3!} = \mathbf{0{,}1954}$$

Giá trị Bernoulli đúng là $0{,}195611$ — sai lệch chỉ $0{,}00024$. Xấp xỉ rất tốt.

### (ii) Xấp xỉ chuẩn địa phương (de Moivre – Laplace) — khi $n$ lớn, $p$ không quá bé/lớn

$$P_n(k) \approx \frac{1}{\sqrt{npq}}\,\varphi\!\left(\frac{k - np}{\sqrt{npq}}\right) \tag{3.13}$$

trong đó $\varphi(x) = \dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$ là **hàm Gauss** (tra bảng 1, tr. 230).

### (iii) Xấp xỉ chuẩn tích phân — cho khoảng $[k_1, k_2]$

$$P_n(k_1, k_2) \approx \phi(x_2) - \phi(x_1), \qquad x_j = \frac{k_j - np}{\sqrt{npq}} \tag{3.14}$$

trong đó $\phi(x) = \dfrac{1}{\sqrt{2\pi}}\displaystyle\int_0^x e^{-t^2/2}\,dt$ là **hàm Laplace**
(tra bảng 2, tr. 232).

⚠️ **Bẫy ký hiệu.** $\varphi$ (Gauss) là **hàm mật độ**; $\phi$ (Laplace) là **tích phân từ 0**,
nên $\phi$ là hàm **lẻ** và $\phi(+\infty) = 0{,}5$ chứ không phải 1. Sách tiếng Anh thường dùng
$\Phi(x)$ = tích phân từ $-\infty$, tức $\Phi(x) = 0{,}5 + \phi(x)$. Nhầm hai cái này là sai 0,5.

**Thí dụ 3.14 (tr. 29).** Xác suất ném trúng rổ của một cầu thủ là 0,8. Trong 100 lần ném:
a) trúng 75 lần; b) trúng không ít hơn 75 lần.

$$np = 80, \qquad \sqrt{npq} = \sqrt{100 \cdot 0{,}8 \cdot 0{,}2} = 4$$

**a)** $x = \dfrac{75 - 80}{4} = -1{,}25$:

$$P_{100}(75) \approx \frac{\varphi(-1{,}25)}{4} = \frac{0{,}1826}{4} = \mathbf{0{,}04565}$$

**b)** $x_1 = -1{,}25$, $x_2 = \dfrac{100-80}{4} = 5$:

$$P_{100}(75; 100) \approx \phi(5) - \phi(-1{,}25) = 0{,}5 + 0{,}3944 = \mathbf{0{,}8943}$$

### Xấp xỉ tốt đến đâu — số liệu thật

|                                | Bernoulli đúng |     Xấp xỉ |   Sai lệch |
| ------------------------------ | -------------: | ---------: | ---------: |
| Thí dụ 3.13, Poisson          |       0,195611 |   0,195367 |    0,00024 |
| Thí dụ 3.14a, chuẩn địa phương |        0,04388 |    0,04566 |     0,0018 |
| Thí dụ 3.14b, chuẩn tích phân  |     **0,9125** | **0,8943** | **0,0182** |

⚠️ Dòng cuối lệch tới **1,8 điểm phần trăm** — đáng kể. Vì sao? Mục 8 giải thích và sửa.

### Chọn xấp xỉ nào

```
n lớn?
  ├─ KHÔNG  →  dùng thẳng công thức Bernoulli (3.10)/(3.11), máy tính lo được
  └─ CÓ
      ├─ p rất nhỏ (np ≤ 10, thường p < 0,1)  →  POISSON (3.12), λ = np
      └─ p vừa phải (npq > 20, hoặc np và nq đều > 5)
            ├─ hỏi ĐÚNG k lần        →  chuẩn địa phương (3.13), hàm Gauss φ
            └─ hỏi TỪ k₁ ĐẾN k₂ lần  →  chuẩn tích phân (3.14), hàm Laplace ϕ
```

💼 **Vì sao dân QTKD vẫn cần biết?** Vì máy tính tính được (3.10) trong tích tắc, nên xấp xỉ không
còn giá trị *tính toán*. Nhưng nó vẫn có giá trị *khái niệm*:

- **Poisson** cho biết: sự kiện hiếm gặp trong lượng lớn phép thử tuân theo một quy luật riêng —
  số khiếu nại/ngày, số lỗi máy/tháng, số khách vào cửa hàng/giờ. Bài 7 sẽ dạy kỹ.
- **Xấp xỉ chuẩn** là hình bóng đầu tiên của **định lý giới hạn trung tâm** (bài 9) — nền tảng của
  toàn bộ phần thống kê, khoảng tin cậy và kiểm định giả thuyết.

---

## 8. 📚 Hiệu chỉnh liên tục

Giáo trình đưa ra công thức (3.14) mà không nhắc tới một chi tiết làm sai lệch kết quả đáng kể.

**Vấn đề.** Phân phối nhị thức là **rời rạc** (chỉ nhận $k = 0, 1, 2, \dots$), còn phân phối chuẩn
là **liên tục**. Khi xấp xỉ cái rời rạc bằng cái liên tục, mỗi giá trị nguyên $k$ thực ra chiếm
một "thanh" rộng 1 đơn vị, từ $k - 0{,}5$ đến $k + 0{,}5$.

```
        thanh của k=75            Nếu lấy mốc tại đúng 75, ta
   ┌────────┴────────┐           mất một nửa thanh (phần gạch)
   │▒▒▒▒▒▒▒▒│████████│
   └────────┴────────┘
  74,5      75      75,5
            ↑
      mốc sách dùng      mốc ĐÚNG phải là 74,5
```

**Hiệu chỉnh liên tục (continuity correction):** lùi mốc ra nửa đơn vị.

$$P(X \ge k) \approx 1 - \Phi\!\left(\frac{k - 0{,}5 - np}{\sqrt{npq}}\right)$$

**Kiểm bằng thí dụ 3.14b:**

| Cách tính                   |      $x_1$ |    Kết quả | Sai lệch so với đúng |
| --------------------------- | ---------: | ---------: | -------------------: |
| Bernoulli đúng              |          — | **0,9125** |                    — |
| Theo sách, mốc 75           | $-1{,}250$ |     0,8943 |           $0{,}0182$ |
| **Có hiệu chỉnh, mốc 74,5** | $-1{,}375$ | **0,9154** |           $0{,}0029$ |

Hiệu chỉnh làm sai số **giảm 6 lần**.

**Khi nào cần?** Khi $n$ nhỏ hoặc $\sqrt{npq}$ nhỏ (dưới 10), sai số 0,5 đơn vị là đáng kể.
Khi $n$ rất lớn thì 0,5 trở nên không đáng gì.

⚠️ **Khi đi thi**, làm theo giáo trình (không hiệu chỉnh) để khớp đáp án. **Khi đi làm**, nhớ có
việc này — và tốt nhất là tính thẳng bằng công thức Bernoulli, khỏi xấp xỉ.

💼 Điều này quan trọng trong **kiểm định A/B**: khi so sánh 2 tỷ lệ chuyển đổi trên mẫu vài trăm
người, bỏ hiệu chỉnh liên tục có thể biến một kết quả "không có ý nghĩa thống kê" thành "có ý nghĩa"
một cách giả tạo. Bài 12 và 13 sẽ quay lại.

---

## 9. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-03-dieu-kien.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**. `statistics.NormalDist` có sẵn cho hàm Laplace.

```python
"""Bài 3 — Xác suất có điều kiện và công thức Bernoulli."""

import math
from fractions import Fraction
from itertools import product
from statistics import NormalDist

# ─────────────────────────────────────────────────────────────
# 1. XÁC SUẤT CÓ ĐIỀU KIỆN — Thí dụ 3.1 (tr. 19)
#    P(tổng = 6 | tổng chẵn)
# ─────────────────────────────────────────────────────────────
omega = list(product(range(1, 7), repeat=2))


def P(ev, given=None):
    """Xac suat co dien; neu co `given` thi tra ve xac suat co dieu kien."""
    space = [w for w in omega if given(w)] if given else omega
    return Fraction(sum(1 for w in space if ev(w)), len(space))


sum6 = lambda w: sum(w) == 6
even = lambda w: sum(w) % 2 == 0

print("P(tong = 6)            =", P(sum6))
print("P(tong chan)           =", P(even))
print("P(tong = 6 VA chan)    =", P(lambda w: sum6(w) and even(w)))
print("P(tong = 6 | tong chan) =", P(sum6, given=even),
      "= P(AB)/P(B) =", P(lambda w: sum6(w) and even(w)) / P(even))
assert P(sum6, given=even) == Fraction(5, 18)

# ─────────────────────────────────────────────────────────────
# 2. ĐỘC LẬP TỪNG ĐÔI ≠ ĐỘC LẬP TỔNG THỂ — Thí dụ 3.3 (tr. 20)
#    Gieo 2 đồng tiền. A = SS+SN, B = SS+NS, C = SS+NN
# ─────────────────────────────────────────────────────────────
coins = ["SS", "SN", "NS", "NN"]
A, B, C = {"SS", "SN"}, {"SS", "NS"}, {"SS", "NN"}


def Q(*sets):
    """Xac suat cua giao cac su kien tren khong gian 4 ket cuc."""
    hit = set(coins)
    for s in sets:
        hit &= s
    return Fraction(len(hit), len(coins))


print()
print("P(A) =", Q(A), " P(B) =", Q(B), " P(C) =", Q(C))
print("P(AB) =", Q(A, B), "vs P(A)P(B) =", Q(A) * Q(B), "->doc lap tung doi:",
      Q(A, B) == Q(A) * Q(B))
print("P(AC) =", Q(A, C), "vs P(A)P(C) =", Q(A) * Q(C), "->", Q(A, C) == Q(A) * Q(C))
print("P(BC) =", Q(B, C), "vs P(B)P(C) =", Q(B) * Q(C), "->", Q(B, C) == Q(B) * Q(C))
print("P(ABC)=", Q(A, B, C), "vs P(A)P(B)P(C) =", Q(A) * Q(B) * Q(C),
      "->doc lap tong the:", Q(A, B, C) == Q(A) * Q(B) * Q(C))

# ─────────────────────────────────────────────────────────────
# 3. CÔNG THỨC CỘNG VÀ NHÂN — Thí dụ 3.5 (tr. 22), ba xạ thủ
# ─────────────────────────────────────────────────────────────
hit = [0.7, 0.8, 0.9]
print()
# a) dung 2 nguoi ban trung: liet ke ca 8 to hop trung/truot
exactly2 = sum(
    math.prod(hit[i] if s[i] else 1 - hit[i] for i in range(3))
    for s in product([0, 1], repeat=3) if sum(s) == 2
)
print(f"a) P(dung 2 nguoi ban trung) = {exactly2:.4f}   (sach: 0,398)")
# b) it nhat 1 nguoi ban truot = 1 - ca ba deu trung
at_least_one_miss = 1 - math.prod(hit)
print(f"b) P(it nhat 1 nguoi truot)  = {at_least_one_miss:.4f}   (sach: 0,496)")

# ─────────────────────────────────────────────────────────────
# 4. Thí dụ 3.6 (tr. 23) — mạch 4 linh kiện, A = A1(A2 + A3)A4
# ─────────────────────────────────────────────────────────────
fail = [0.2, 0.1, 0.05, 0.02]
g = [1 - f for f in fail]                     # xac suat lam viec tot
p_parallel = g[1] + g[2] - g[1] * g[2]        # A2 + A3, KHONG xung khac
p_net = g[0] * p_parallel * g[3]
print()
print("Linh kien tot:", g)
print(f"P(A2 + A3) = {g[1]} + {g[2]} - {g[1]}*{g[2]} = {p_parallel}")
print(f"P(mang tot) = {g[0]} * {p_parallel} * {g[3]} = {p_net:.5f}   (sach: 0,78008)")

# Neu bo qua tinh khong xung khac ma cong bua:
print(f"Neu cong bua P(A2)+P(A3) = {g[1] + g[2]} > 1  ->  vo nghia")

# ─────────────────────────────────────────────────────────────
# 5. Thí dụ 3.7 (tr. 24) — gia đình 6 con, số trai > số gái
# ─────────────────────────────────────────────────────────────
print()
pc = Fraction(math.comb(6, 3), 2**6)          # P(3 trai 3 gai)
pa = (1 - pc) / 2                             # doi xung trai/gai
print("P(3 trai 3 gai) =", pc, "| P(so trai > so gai) =", pa,
      "=", round(float(pa), 4))
# kiem lai bang liet ke 64 ket cuc
brute = Fraction(sum(1 for s in product([0, 1], repeat=6) if sum(s) > 3), 2**6)
assert brute == pa
print("Liet ke 64 ket cuc cho ket qua y het:", brute)

# ─────────────────────────────────────────────────────────────
# 6. CÔNG THỨC BERNOULLI (3.10) — Thí dụ 3.10, 3.11 (tr. 26–27)
# ─────────────────────────────────────────────────────────────
def bernoulli(n, k, p):
    return math.comb(n, k) * p**k * (1 - p) ** (n - k)


print()
print(f"Thi du 3.10: P_10(2), n=10 p=0,9 -> {bernoulli(10, 2, 0.9):.6e}"
      "   (sach: 3645.10^-10)")
print(f"Thi du 3.11: P_10(8), n=10 p=0,8 -> {bernoulli(10, 8, 0.8):.4f}"
      "   (sach: 0,3108)")

# Thí dụ 3.12 (tr. 27) — cỡ mẫu để bắt được ít nhất 1 phế phẩm
need = math.log(0.05) / math.log(0.99)
print()
print(f"Thi du 3.12: log0,05/log0,99 = {need:.4f}  ->  n toi thieu = {math.ceil(need)}")
print(f"   Kiem: 1 - 0,99^298 = {1 - 0.99**298:.6f} (chua du)"
      f" | 1 - 0,99^299 = {1 - 0.99**299:.6f} (dat)")
assert 1 - 0.99**298 < 0.95 < 1 - 0.99**299

# ─────────────────────────────────────────────────────────────
# 7. BA CÁCH XẤP XỈ (3.12) – (3.14), so với giá trị đúng
# ─────────────────────────────────────────────────────────────
def poisson(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)


def gauss(x):                       # ham Gauss, bang 1
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def laplace(x):                     # ham Laplace, bang 2 (le, lap(inf) = 0,5)
    return NormalDist().cdf(x) - 0.5


print()
# Thí dụ 3.13 (tr. 28): n=800, p=0,005, k=3 -> xap xi Poisson
n, p, k = 800, 0.005, 3
print(f"Thi du 3.13  n={n} p={p} k={k}, np={n * p}")
print(f"   Bernoulli dung : {bernoulli(n, k, p):.6f}")
print(f"   Xap xi Poisson: {poisson(k, n * p):.6f}   (sach: 0,1954)")

# Thí dụ 3.14 (tr. 29): n=100, p=0,8
n, p = 100, 0.8
sigma = math.sqrt(n * p * (1 - p))
print()
print(f"Thi du 3.14  n={n} p={p}, np={n * p}, can(npq)={sigma}")
x = (75 - n * p) / sigma
print(f"   a) P_100(75) dung        : {bernoulli(n, 75, p):.5f}")
print(f"      xap xi de Moivre dia phuong: {gauss(x) / sigma:.5f}   (sach: 0,04565)")
exact_tail = sum(bernoulli(n, j, p) for j in range(75, 101))
x1, x2 = (75 - n * p) / sigma, (100 - n * p) / sigma
print(f"   b) P_100(75;100) dung    : {exact_tail:.4f}")
print(f"      xap xi de Moivre tich phan : {laplace(x2) - laplace(x1):.4f}   (sach: 0,8943)")
```

Kết quả chạy thật:

```
P(tong = 6)            = 5/36
P(tong chan)           = 1/2
P(tong = 6 VA chan)    = 5/36
P(tong = 6 | tong chan) = 5/18 = P(AB)/P(B) = 5/18

P(A) = 1/2  P(B) = 1/2  P(C) = 1/2
P(AB) = 1/4 vs P(A)P(B) = 1/4 ->doc lap tung doi: True
P(AC) = 1/4 vs P(A)P(C) = 1/4 -> True
P(BC) = 1/4 vs P(B)P(C) = 1/4 -> True
P(ABC)= 1/4 vs P(A)P(B)P(C) = 1/8 ->doc lap tong the: False

a) P(dung 2 nguoi ban trung) = 0.3980   (sach: 0,398)
b) P(it nhat 1 nguoi truot)  = 0.4960   (sach: 0,496)

Linh kien tot: [0.8, 0.9, 0.95, 0.98]
P(A2 + A3) = 0.9 + 0.95 - 0.9*0.95 = 0.9950000000000001
P(mang tot) = 0.8 * 0.9950000000000001 * 0.98 = 0.78008   (sach: 0,78008)
Neu cong bua P(A2)+P(A3) = 1.85 > 1  ->  vo nghia

P(3 trai 3 gai) = 5/16 | P(so trai > so gai) = 11/32 = 0.3438
Liet ke 64 ket cuc cho ket qua y het: 11/32

Thi du 3.10: P_10(2), n=10 p=0,9 -> 3.645000e-07   (sach: 3645.10^-10)
Thi du 3.11: P_10(8), n=10 p=0,8 -> 0.3020   (sach: 0,3108)

Thi du 3.12: log0,05/log0,99 = 298.0729  ->  n toi thieu = 299
   Kiem: 1 - 0,99^298 = 0.949963 (chua du) | 1 - 0,99^299 = 0.950464 (dat)

Thi du 3.13  n=800 p=0.005 k=3, np=4.0
   Bernoulli dung : 0.195611
   Xap xi Poisson: 0.195367   (sach: 0,1954)

Thi du 3.14  n=100 p=0.8, np=80.0, can(npq)=3.9999999999999996
   a) P_100(75) dung        : 0.04388
      xap xi de Moivre dia phuong: 0.04566   (sach: 0,04565)
   b) P_100(75;100) dung    : 0.9125
      xap xi de Moivre tich phan : 0.8943   (sach: 0,8943)
```

Bốn điểm đáng để ý:

1. **`P(ABC) = 1/4 vs 1/8 → False`** — đây là toàn bộ nội dung của thí dụ 3.3, gói trong một dòng.
2. **`Thi du 3.11 -> 0.3020` (sách: 0,3108)** — máy tính ra con số khác sách. Bằng chứng cho đính chính.
3. **`n toi thieu = 299`** (sách: 296), kèm hai dòng kiểm lại `0.949963` / `0.950464` chứng minh 299
   mới là số nhỏ nhất đạt yêu cầu.
4. **`can(npq) = 3.9999999999999996`** thay vì đúng 4 — sai số dấu phẩy động của máy tính.
   Không ảnh hưởng gì ở đây, nhưng nhớ: **đừng bao giờ so sánh hai số thực bằng `==`**.
   Với tiền bạc, phải dùng số nguyên (đồng, xu) — bài 10 sẽ nhắc lại.

---

## 10. Tự thử

1. Ở mục 1, đổi điều kiện từ "tổng chẵn" thành "cả hai con đều ra số lẻ".
   $P(\text{tổng} = 6 \mid \text{cả hai lẻ})$ bằng bao nhiêu? Vì sao lại lớn hơn hẳn $5/18$?
2. Ở mục 3 (ba xạ thủ), đổi câu hỏi thành "có **đúng một** người bắn trúng" và "có **ít nhất hai**
   người bắn trúng". Tổng của cả bốn xác suất (0, 1, 2, 3 người trúng) có bằng 1 không?
3. Ở mục 4, thử thêm dự phòng cho linh kiện 1: thay `g[0]` bằng `g[0] + g[0] - g[0]*g[0]`.
   Độ tin cậy cả hệ lên bao nhiêu? Còn nếu thay vào đó thêm dự phòng cho linh kiện 4?
   Đầu tư vào đâu lợi hơn?
4. Viết hàm tính bài toán bỏ thư (thí dụ 3.8): `1 - 1/2! + 1/3! - ... ± 1/n!` cho $n = 3, 5, 10, 20$.
   Từ $n$ bằng bao nhiêu thì kết quả đã sát $1 - 1/e = 0{,}632121$ tới 4 chữ số?
5. Thêm **hiệu chỉnh liên tục** vào thí dụ 3.14b: đổi `x1 = (75 - n*p)/sigma` thành
   `x1 = (74.5 - n*p)/sigma`. Kết quả có gần `0.9125` hơn không? Lệch bao nhiêu?
6. So xấp xỉ Poisson với Bernoulli đúng khi $p$ tăng dần: $n = 100$ và $p = 0{,}01; 0{,}05; 0{,}1; 0{,}3$,
   cùng hỏi $k = np$. Xấp xỉ bắt đầu tệ từ $p$ bằng bao nhiêu?

---

## 11. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)     | Tiếng Anh                        | Ghi chú                             |
| --------------------------- | -------------------------------- | ----------------------------------- |
| Xác suất có điều kiện       | Conditional probability          | $P(A \mid B)$                       |
| Độc lập (thống kê)          | (Statistically) independent      | $P(AB) = P(A)P(B)$                  |
| Độc lập từng đôi            | Pairwise independent             | yếu hơn                             |
| Độc lập trong tổng thể      | Mutually independent             | mạnh hơn, đúng cho mọi nhóm con     |
| Công thức nhân              | Multiplication rule / Chain rule | (3.5), (3.6)                        |
| Công thức cộng              | Addition rule                    | (3.7)                               |
| Bao hàm – loại trừ          | Inclusion–exclusion              | (3.8)                               |
| Lược đồ Bernoulli           | Bernoulli scheme / trials        | $n$ lần độc lập, 2 kết cục          |
| Công thức Bernoulli         | Binomial probability formula     | (3.10)                              |
| Xấp xỉ Poisson             | Poisson approximation            | $n$ lớn, $p$ nhỏ                    |
| Hàm Gauss $\varphi$        | Standard normal density          | bảng 1, tr. 230                     |
| Hàm Laplace $\phi$        | Laplace function                 | bảng 2, tr. 232; tích phân **từ 0** |
| Định lý de Moivre – Laplace | de Moivre–Laplace theorem        | (3.13), (3.14)                      |
| Hiệu chỉnh liên tục         | Continuity correction            | 📚 mục 8, không có trong giáo trình  |

---

## 12. Câu hỏi tự kiểm tra

1. Cho $P(A) = 0{,}6$, $P(B) = 0{,}5$, $P(AB) = 0{,}3$. $A$ và $B$ có độc lập không? Có xung khắc không?
   Tính $P(A \mid B)$, $P(B \mid A)$, $P(A + B)$.
2. Có thể vừa **xung khắc** vừa **độc lập** không? (Giả sử $P(A) > 0$ và $P(B) > 0$.)
   Chứng minh câu trả lời.
3. Vì sao đề thí dụ 3.6 phải ghi rõ "các linh kiện làm việc **độc lập** với nhau"?
   Nếu bỏ giả thiết đó, còn tính được không?
4. Một dây chuyền 5 công đoạn, mỗi công đoạn đạt 98%. Xác suất sản phẩm qua được cả 5 công đoạn?
   Nếu muốn cả dây chuyền đạt 95%, mỗi công đoạn phải đạt tối thiểu bao nhiêu?
5. Telesales gọi 20 cuộc, tỷ lệ chốt mỗi cuộc là 15%.
   a) Xác suất chốt được đúng 3 đơn?
   b) Xác suất không chốt được đơn nào?
   c) Xác suất chốt được ít nhất 1 đơn?
6. Tỷ lệ lỗi của nhà cung cấp là 2%. Bạn muốn 99% chắc chắn phát hiện được lỗi. Cỡ mẫu tối thiểu?
   (Dùng khuôn mẫu thí dụ 3.12.)
7. Vì sao "tỷ lệ chốt 20%, gọi 10 cuộc được 2 đơn" là phát biểu sai? Tính xác suất được **đúng** 2 đơn,
   và xác suất được **từ 1 đến 3** đơn.
8. Bài 29 (tr. 38): tỷ lệ hút thuốc ở một vùng là 35%; tỷ lệ viêm họng trong số người hút thuốc là 60%,
   trong số không hút là 30%. Khám ngẫu nhiên một người thấy bị viêm họng; xác suất đó là người hút
   thuốc? (Bài này cần công thức Bayes — xem trước bài 4.)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 3 — XÁC SUẤT CÓ ĐIỀU KIỆN & BERNOULLI        (Ch. I §3, tr. 18–29)  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  XÁC SUẤT CÓ ĐIỀU KIỆN      P(A|B) = P(AB) / P(B)        (P(B) > 0)      ║
║      = thu hẹp không gian mẫu từ Ω xuống còn B, rồi đếm lại              ║
║                                                                          ║
║  ĐỘC LẬP     P(A|B) = P(A)   ⟺   P(AB) = P(A)·P(B)                      ║
║      ⚠ độc lập TỔNG THỂ ⟹ độc lập TỪNG ĐÔI,  chiều ngược lại SAI        ║
║      ⚠ trong bài tập, độc lập là GIẢ THIẾT ĐƯỢC CHO, không tự suy ra    ║
║                                                                          ║
║  NHÂN     P(AB) = P(A)·P(B|A) = P(B)·P(A|B)                              ║
║           P(A₁...Aₙ) = P(A₁)·P(A₂|A₁)·P(A₃|A₁A₂)···   ← phễu bán hàng   ║
║           độc lập  →  P(∏Aᵢ) = ∏P(Aᵢ)                                    ║
║                                                                          ║
║  CỘNG     P(A+B) = P(A) + P(B) − P(AB)      ← trừ vì AB đếm 2 lần       ║
║           xung khắc  →  P(A+B) = P(A) + P(B)                             ║
║           n sự kiện  →  bao hàm–loại trừ, dấu đan xen  + − + −          ║
║                                                                          ║
║  BA KHUÔN MẪU GIẢI BÀI                                                   ║
║      "ít nhất một"        →  1 − P(không cái nào)                        ║
║      "ít nhất 1 trong n"  →  1 − (1−p)ⁿ                                  ║
║      "đúng k cái"         →  liệt kê tổ hợp, xung khắc + độc lập         ║
║                                                                          ║
║  LƯỢC ĐỒ BERNOULLI    n phép thử độc lập, giống nhau, 2 kết cục, p cố định║
║      Pₙ(k) = C(n,k) · pᵏ · q^(n−k)                                       ║
║               ↑ số kịch bản   ↑ xác suất một kịch bản                    ║
║      Pₙ(k₁,k₂) = Σ từ k₁ đến k₂                                          ║
║                                                                          ║
║  BA XẤP XỈ KHI n LỚN                                                     ║
║      p rất nhỏ        → POISSON   e^(−λ)·λᵏ/k!,   λ = np                 ║
║      p vừa, đúng k    → chuẩn địa phương  φ((k−np)/√npq) / √npq          ║
║      p vừa, khoảng    → chuẩn tích phân   ϕ(x₂) − ϕ(x₁)                  ║
║      ⚠ φ = Gauss (mật độ) ≠ ϕ = Laplace (tích phân TỪ 0, ϕ(∞)=0,5)      ║
║      📚 hiệu chỉnh liên tục: lùi mốc 0,5 → sai số giảm ~6 lần            ║
║                                                                          ║
║  ⚠ ĐÍNH CHÍNH  tr.27  P₁₀(8) = 0,3020 (sách in 0,3108)                  ║
║                tr.27  cỡ mẫu n ≥ 299   (sách in 296)                     ║
║                                                                          ║
║  💼 QTKD  phễu bán hàng = công thức nhân dây chuyền                       ║
║          reach 2 kênh = P(A)+P(B)−P(AB), KHÔNG phải cộng thẳng          ║
║          cỡ mẫu QC ≈ 3/p  để 95% bắt được lỗi tỷ lệ p                   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương I §3, tr. 18–29.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Đính chính thí dụ 3.11 (tr. 27) và thí dụ 3.12 (tr. 27): đã đối chiếu bản quét gốc.
  Công thức trong sách đúng, kết quả số sai.
- Hiệu chỉnh liên tục (mục 8): kiến thức bổ sung, không có trong giáo trình.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 2 — Ba định nghĩa của xác suất](bai_02_ba_dinh_nghia_cua_xac_suat.md) ·
Bài sau: Bài 4 — Xác suất đầy đủ và công thức Bayes
