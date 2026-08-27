# Bài 2 — Ba định nghĩa của xác suất

> Bài học dựa trên **Giáo trình Xác suất Thống kê** (Tống Đình Quỳ, NXB Bách Khoa – Hà Nội), **Chương I §2**, tr. 11–18.
> 💼 **Góc QTKD** là ví dụ thêm cho ngành Quản trị Kinh doanh, không có trong giáo trình.
> 📚 **Mở rộng** là kiến thức nền giáo trình lướt qua.
> ⚠️ Bài này **đính chính một lỗi in** của giáo trình ở mục 5 (bảng gieo đồng tiền, tr. 15).
> 📌 **Cần đọc trước:** [Bài 1 — Sự kiện ngẫu nhiên và giải tích kết hợp](bai_01_su_kien_ngau_nhien_va_giai_tich_ket_hop.md)

Bài 1 dạy **mô tả** cái gì có thể xảy ra. Bài này gắn **con số** vào đó.

Điều bất ngờ: xác suất không có *một* định nghĩa. Giáo trình đưa ra **ba** — cổ điển, thống kê,
tiên đề (cộng thêm biến thể hình học) — vì mỗi cái chỉ dùng được trong một hoàn cảnh.
Biết dùng cái nào khi nào chính là nội dung của bài.

## Mục lục

1. [Định nghĩa cổ điển](#1-định-nghĩa-cổ-điển)
2. [Năm tính chất của xác suất](#2-năm-tính-chất-của-xác-suất)
3. [Ba thí dụ mẫu của giáo trình](#3-ba-thí-dụ-mẫu-của-giáo-trình)
4. [Định nghĩa hình học](#4-định-nghĩa-hình-học)
5. [Định nghĩa thống kê](#5-định-nghĩa-thống-kê)
6. [Định nghĩa tiên đề của Kolmogorov](#6-định-nghĩa-tiên-đề-của-kolmogorov)
7. [📚 Ba định nghĩa: chọn cái nào khi nào](#7--ba-định-nghĩa-chọn-cái-nào-khi-nào)
8. [Code minh hoạ](#8-code-minh-hoạ)
9. [Tự thử](#9-tự-thử)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)

- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

---

## 1. Định nghĩa cổ điển

Giáo trình mở đầu bằng một điều kiện tiên quyết mà nhiều người đọc lướt qua (tr. 11):

> "Trong mục này ta làm việc với các phép thử có kết cục **đồng khả năng**."

**Đồng khả năng** (equally likely) là khái niệm chủ đạo, và cũng "khó có thể định nghĩa một cách
hình thức" — lại một khái niệm nguyên thuỷ nữa. Ta chỉ nhận biết nó bằng tính đối xứng vật lý:
xúc sắc đồng chất, bi giống nhau về kích cỡ, đồng tiền cân đối.

**Thí dụ 2.1 (tr. 11).** Hộp có $n$ viên bi giống nhau về kích cỡ, chỉ khác màu: $m$ bi trắng và
$n-m$ bi đỏ. Rút hú hoạ 1 viên. Vì $n$ viên như nhau nên mỗi viên có cùng khả năng được rút.
Gọi $A$ = "rút được bi trắng" thì trong $n$ kết cục đồng khả năng có $m$ kết cục thuận lợi cho $A$.
Trực giác bảo ta lấy tỷ số $m/n$.

**Định nghĩa cổ điển (tr. 11).** Cho một phép thử với $n$ kết cục **đồng khả năng**, trong đó có
$m$ kết cục **thuận lợi** cho $A$:

$$P(A) = \frac{m}{n} = \frac{\text{số kết cục thuận lợi cho } A}{\text{tổng số kết cục có thể}} \tag{2.1}$$

Giáo trình đánh giá thẳng ưu và nhược (tr. 12):

| Ưu điểm                                   | Nhược điểm                                |
| ----------------------------------------- | ----------------------------------------- |
| tương đối đơn giản và trực quan           | phạm vi áp dụng **rất hạn chế**           |
| tính được chính xác, không cần thí nghiệm | chỉ dùng cho phép thử **hữu hạn** kết cục |
|                                           | và các kết cục phải **đồng khả năng**     |

Chính vì nhược điểm này mà phải có thêm hai định nghĩa nữa ở các mục sau.

⚠️ **Bẫy chết người số 1 của cả môn học.** Công thức $m/n$ chỉ đúng khi $n$ kết cục **đồng khả năng**.
Chọn sai $\Omega$ là sai toàn bộ. Mục 3 và mục 8 sẽ cho bạn thấy một trường hợp cụ thể lệch tới 35%.

Trong tính toán, ta dùng lại bốn công thức đếm của bài 1: $A_n^k$, $\overline{A}_n^k$, $P_n$, $C_n^k$.
Đó là lý do bài 1 phải học trước.

### 💼 Góc QTKD

Công ty tổ chức bốc thăm trúng thưởng: thùng có 500 phiếu, trong đó 20 phiếu trúng.
Khách hàng bốc 1 phiếu.

$$P(\text{trúng}) = \frac{20}{500} = 0{,}04 = 4\%$$

Điều kiện đồng khả năng ở đây có thật không? **Chỉ khi** các phiếu giống hệt nhau về kích thước,
chất liệu, và thùng được xóc kỹ. Nếu phiếu trúng in trên giấy dày hơn, hoặc bỏ vào sau nên nằm
trên mặt, thì $20/500$ **sai**. Đây không phải chuyện lý thuyết — đó là lý do các chương trình
khuyến mại hợp pháp phải có biên bản niêm phong và giám sát.

---

## 2. Năm tính chất của xác suất

Từ (2.1) suy ra được ngay năm tính chất, và giáo trình lưu ý chúng **đúng cho cả các định nghĩa
khác** (tr. 13) — nghĩa là bạn dùng được vô điều kiện suốt cả môn học:

$$
\begin{aligned}
&\text{(i)} && 0 \le P(A) \le 1 \\
&\text{(ii)} && P(U) = 1, \quad P(V) = 0 \\
&\text{(iii)} && A, B \text{ xung khắc} \Rightarrow P(A + B) = P(A) + P(B) \\
&\text{(iv)} && P(\overline{A}) = 1 - P(A) \\
&\text{(v)} && A \Rightarrow B \ \text{ thì } \ P(A) \le P(B)
\end{aligned}
$$

Trong năm cái, **(iv) là công cụ làm bài quan trọng nhất**. Nhớ lại bài 1 mục 4: mọi câu hỏi dạng
"có ít nhất một..." đều nên lật ngược thành "không có cái nào" rồi lấy $1$ trừ đi.

$$P(\text{ít nhất một}) = 1 - P(\text{không cái nào})$$

Tính chất (v) cũng đáng để ý: nếu $A$ kéo theo $B$ thì $A$ "khó xảy ra hơn". Nghe hiển nhiên,
nhưng nó là công cụ kiểm tra đáp án: nếu bạn tính ra $P(\text{có đúng 3 phế phẩm})$ lớn hơn
$P(\text{có ít nhất 1 phế phẩm})$ thì chắc chắn sai ở đâu đó.

⚠️ Tính chất (iii) **bắt buộc phải có điều kiện xung khắc**. Không xung khắc thì phải dùng công
thức cộng đầy đủ $P(A+B) = P(A) + P(B) - P(AB)$ ở bài 3. Cộng bừa hai xác suất là lỗi phổ biến nhất
trong bài thi.

---

## 3. Ba thí dụ mẫu của giáo trình

### Thí dụ 2.2 (tr. 12) — và cái bẫy đồng khả năng

> Gieo đồng thời 2 con xúc sắc **giống nhau**. Tính xác suất để tổng số chấm bằng 6.

*Giải.* Phép thử có $6 \times 6 = 36$ kết cục đồng khả năng. Gọi $A$ = "tổng số chấm bằng 6",
có 5 kết cục thuận lợi: $\{1,5\}, \{2,4\}, \{3,3\}, \{4,2\}, \{5,1\}$ (số thứ nhất chỉ con xúc sắc 1).

$$P(A) = \frac{5}{36} \approx 0{,}1389$$

⚠️ **Đây là chỗ dễ sai nhất trong toàn bài.** Đề nói hai con xúc sắc *giống nhau*, nên nhiều bạn
tưởng $\{1,5\}$ và $\{5,1\}$ là một, và lấy $\Omega$ = 11 giá trị tổng có thể ($2, 3, \dots, 12$),
rồi kết luận $P(A) = 1/11 \approx 0{,}0909$.

Sai. Vì **11 giá trị tổng đó không đồng khả năng** — tổng 7 dễ ra hơn tổng 2 rất nhiều
(6 cách so với 1 cách). Chỉ 36 cặp mới đồng khả năng. Sai số ở đây là $0{,}048$, tức lệch 35%.

**Quy tắc rút ra:** khi phân vân, hãy chọn $\Omega$ **mịn nhất** — mịn tới mức mọi kết cục thật sự
như nhau. Gộp kết cục lại cho gọn hầu như luôn phá vỡ tính đồng khả năng.

### Thí dụ 2.3 (tr. 12–13) — một bài, ba cách hỏi

> Hộp có 4 bi trắng và 6 bi đỏ cùng kích cỡ. Rút hú hoạ 2 bi. Tính xác suất để trong đó có:
> a) hai viên trắng; b) ít nhất 1 viên đỏ; c) viên **thứ hai** đỏ.

**a) Hai viên trắng.** Giáo trình giải bằng cả hai cách để cho thấy chúng tương đương:

*Cách có thứ tự (chỉnh hợp):* tổng số cách $A_{10}^2 = 10 \cdot 9 = 90$; thuận lợi $A_4^2 = 4 \cdot 3 = 12$.

$$P(A) = \frac{12}{90} = \frac{2}{15}$$

*Cách không thứ tự (tổ hợp):* tổng số cách $C_{10}^2 = 45$; thuận lợi $C_4^2 = 6$.

$$P(A) = \frac{6}{45} = \frac{2}{15}$$

Cùng đáp số. **Bài học:** đếm có thứ tự hay không thứ tự đều được, **miễn là tử số và mẫu số dùng
cùng một kiểu đếm**. Trộn hai kiểu (tử tổ hợp, mẫu chỉnh hợp) là sai.

**b) Ít nhất 1 viên đỏ.** Đây là lúc dùng tính chất (iv). Sự kiện đối lập $\overline{B}$ = "cả 2 bi
đều trắng" chính là câu a), đã có $P(\overline{B}) = 2/15$.

$$P(B) = 1 - \frac{2}{15} = \frac{13}{15}$$

Nếu tính trực tiếp, bạn phải cộng hai trường hợp (1 đỏ 1 trắng, và 2 đỏ) — dài gấp ba.

**c) Viên thứ hai đỏ.** Từ "thứ hai" buộc phải đếm **có thứ tự**. Số cách thuận lợi:
$6 \cdot 5 = 30$ (viên đầu đỏ) $+ \ 4 \cdot 6 = 24$ (viên đầu trắng) $= 54$.

$$P(C) = \frac{54}{90} = \frac{3}{5}$$

Giáo trình còn nêu một lối lý luận đẹp hơn nhiều:

> "Do viên bi đầu **không biết màu sắc** nên thông tin về tỷ lệ màu không thay đổi với viên bi
> thứ hai. Vậy $C$ sẽ có cùng xác suất với việc rút hú hoạ ra 1 bi đỏ từ hộp 10 viên ban đầu."

$$P(C) = \frac{6}{10} = \frac{3}{5}$$

**Đây là một ý tưởng rất sâu, đáng ghi nhớ:** rút bi mà *không nhìn* thì viên thứ hai có cùng
xác suất với viên thứ nhất. Vị trí trong dãy rút không mang thông tin gì, chừng nào bạn chưa
quan sát các viên trước. (Nếu đề nói "biết viên đầu là trắng" thì hoàn toàn khác — đó là
**xác suất có điều kiện**, bài 3.)

### 💼 Góc QTKD

Lô hàng nhập về 10 thùng, trong đó 4 thùng đạt chuẩn xuất khẩu và 6 thùng chỉ đạt chuẩn nội địa.
Bộ phận QC lấy ngẫu nhiên 2 thùng đi kiểm.

| Câu hỏi kinh doanh                                         | Tương ứng thí dụ 2.3 | Kết quả                  |
| ---------------------------------------------------------- | -------------------- | ------------------------ |
| Xác suất cả 2 thùng kiểm đều là hàng xuất khẩu?            | a)                   | $2/15 \approx 13{,}3\%$  |
| Xác suất mẫu kiểm dính ít nhất 1 thùng nội địa?            | b)                   | $13/15 \approx 86{,}7\%$ |
| Nếu kiểm lần lượt, thùng kiểm **thứ hai** là hàng nội địa? | c)                   | $3/5 = 60\%$             |

Câu (b) chính là câu QC quan tâm nhất: **lấy 2 thùng thôi mà tới 86,7% khả năng phát hiện được
hàng không đạt chuẩn xuất khẩu**. Đó là lập luận cơ bản của lấy mẫu kiểm tra chất lượng — không
cần kiểm 100% lô hàng vẫn có độ tin cậy cao. Bài 7 (phân phối siêu bội, nhị thức) sẽ mở rộng
lập luận này thành một quy trình lấy mẫu hoàn chỉnh.

---

## 4. Định nghĩa hình học

Định nghĩa cổ điển chết ngay khi số kết cục là vô hạn. Giáo trình khắc phục bằng cách thay
**phép đếm** bằng **phép đo** (tr. 13).

Giả sử tập vô hạn các kết cục đồng khả năng biểu thị được bằng một miền hình học $G$ (đoạn thẳng,
mặt cong, khối không gian...), còn tập kết cục thuận lợi cho $A$ là miền con $S \subset G$. Khi đó:

$$P(A) = \frac{\text{độ đo } S}{\text{độ đo } G} \tag{2.2}$$

Tuỳ $S$ và $G$ mà "độ đo" là **độ dài**, **diện tích** hoặc **thể tích**.

"Rơi đồng khả năng vào $G$" nghĩa là: điểm gieo có thể rơi vào bất kỳ điểm nào của $G$, và xác suất
rơi vào một miền con **tỷ lệ với độ đo** của miền ấy, *không phụ thuộc vị trí và hình dạng* của miền
(tr. 14).

**Thí dụ 2.4 (tr. 14).** Đường dây điện thoại ngầm nối một tổng đài với một trạm dài 1 km.
Tính xác suất để dây đứt tại nơi cách tổng đài không quá 100 m.

*Giải.* Dây đồng chất → khả năng đứt tại mọi điểm là như nhau → $G$ là đoạn thẳng 1000 m,
$S$ là đoạn 100 m đầu.

$$P(A) = \frac{100}{1000} = 0{,}1$$

### ⚠️ Xác suất 0 không có nghĩa là không thể

Giáo trình nêu một hệ quả rất quan trọng của định nghĩa này (tr. 14):

> "Theo cách định nghĩa này thì sự kiện có xác suất bằng 0 **vẫn có thể xảy ra** (chẳng hạn mũi
> tên bắn trúng một điểm cho trước)."

Vì một điểm có độ dài bằng 0, nên $P(\text{đứt đúng tại mét thứ 300}) = 0/1000 = 0$. Nhưng dây
vẫn phải đứt ở *một* điểm nào đó! Xác suất 0 ở đây nghĩa là "hầu như không xảy ra", chứ không phải
"bất khả" ($V$).

Đảo lại: $P(A) = 1$ cũng không đồng nghĩa với "tất yếu" ($U$).

Đây là đặc trưng của **biến ngẫu nhiên liên tục**, sẽ gặp lại ở bài 5. Ghi nhớ ngay, vì nó phá vỡ
trực giác: với biến liên tục, hỏi "xác suất doanh thu đúng bằng 15.000.000 đồng" luôn cho đáp án 0.
Câu hỏi có nghĩa phải là "xác suất doanh thu **nằm trong khoảng** 14–16 triệu".

### 💼 Góc QTKD

Xe giao hàng đến kho vào một thời điểm ngẫu nhiên trong khung 8h–17h (9 tiếng). Nhân viên nhận
hàng nghỉ trưa 12h–13h.

$$P(\text{xe đến lúc không có người nhận}) = \frac{1 \text{ giờ}}{9 \text{ giờ}} \approx 0{,}111$$

Trên 11% chuyến hàng sẽ phải chờ. Nếu mỗi lần chờ tốn 30 phút tài xế, với 200 chuyến/tháng thì
mất $200 \times 0{,}111 \times 0{,}5 \approx 11$ giờ công mỗi tháng — đủ để biện minh cho việc bố trí
nhân viên trực luân phiên giờ trưa. **Xác suất hình học biến một câu hỏi mơ hồ thành một con số
để ra quyết định.**

---

## 5. Định nghĩa thống kê

Điều kiện đồng khả năng không phải lúc nào cũng có. Giáo trình nêu hai ví dụ đắt giá (tr. 14):
xác suất một đứa trẻ sắp sinh là con trai; xác suất ngày mai trời mưa vào lúc chính ngọ.
Không có đối xứng nào ở đây để mà đếm.

**Tần suất.** Tiến hành $n_1$ phép thử cùng loại, nếu $A$ xuất hiện trong $m_1$ phép thử thì
$m_1/n_1$ gọi là **tần suất** xuất hiện $A$. Làm tương tự với loạt thứ hai, thứ ba... được
$m_2/n_2$, $m_3/n_3$, ...

**Quan sát then chốt (tr. 15):** tần suất có **tính ổn định** — thay đổi rất ít giữa các loạt và
dao động quanh một hằng số xác định, và sự khác biệt càng nhỏ khi số phép thử càng lớn. Hơn nữa,
với các phép thử ở mục 1, hằng số đó **trùng với xác suất cổ điển**.

**Định nghĩa thống kê.** Lấy ngay tần suất khi số phép thử đủ lớn làm xác suất của sự kiện.
Phát biểu chặt chẽ hơn:

$$P(A) = \lim_{n \to \infty} \frac{m}{n}$$

Giáo trình thẳng thắn thừa nhận (tr. 15): xác suất ở đây là **một giá trị gần đúng** và
"nhiều người cho rằng đó không phải là một định nghĩa thật sự". Nhưng nó được thừa nhận rộng rãi
vì trong khoa học thực nghiệm, sai số của cách này thường **bé hơn nhiều so với sai số đo của
thí nghiệm**.

### Số liệu thật của giáo trình (tr. 15)

Tần suất xuất hiện mặt sấp khi gieo một đồng tiền nhiều lần:

| Người thí nghiệm | Số lần gieo | Số lần sấp | Tần suất (sách in) | Tần suất (tính lại) |
| ---------------- | ----------: | ---------: | -----------------: | ------------------: |
| Buffon       |        4040 |       2048 |      ~~0,5080~~ ⚠️ |          **0,5069** |
| Pearson         |       12000 |       6019 |             0,5016 |            0,5016 ✓ |
| Pearson         |       24000 |      12012 |             0,5005 |            0,5005 ✓ |

⚠️ **Đính chính.** Sách in tần suất của Buffon là **0,5080**, nhưng $2048 / 4040 = 0{,}50693\ldots$
tức **0,5069**. Đã đối chiếu bản quét gốc trang 15 — đúng là chữ in trên giấy, không phải lỗi quét.
Hai dòng của Pearson thì khớp hoàn toàn. Con số lịch sử của Buffon cũng là 0,5069. Khi làm bài,
dùng 0,5069.

Con số này không phá hỏng bài học — ngược lại, nó **củng cố** bài học: tần suất tiến dần về 0,5 khi
$n$ tăng ($0{,}5069 \to 0{,}5016 \to 0{,}5005$), đúng như định nghĩa thống kê nói.

Giáo trình còn nêu một ví dụ khác: xác suất phân rã của một nguyên tử Ra$^{226}$ sau 100 năm là
**0,04184** (chính xác tới 5 chữ số sau dấu phẩy) — đạt được vì số nguyên tử tham gia thí nghiệm
cỡ $10^{18}$–$10^{24}$.

**Cầu nối giữa hai định nghĩa.** Vì sao tần suất lại hội tụ về đúng xác suất cổ điển? Giáo trình
hẹn trả lời ở **luật số lớn Bernoulli** (bài 9). Đó không phải trùng hợp mà là một định lý.

⚠️ **Điều kiện bắt buộc** mà giáo trình nhấn mạnh (tr. 16): các phép thử phải **lặp lại như nhau**.
Trên thực tế điều này không dễ bảo đảm, nên "tần suất có thể phụ thuộc vào thời gian".

### 💼 Góc QTKD

Đây là định nghĩa mà bạn sẽ dùng **nhiều nhất** trong nghề, dù có thể không gọi tên nó.

| Chỉ số kinh doanh                        | Chính là tần suất của...         |
| ---------------------------------------- | -------------------------------- |
| Tỷ lệ chuyển đổi (conversion rate) 2,3%  | số đơn hàng / số lượt truy cập   |
| Tỷ lệ khách rời bỏ (churn rate) 5%/tháng | số khách huỷ / tổng khách đầu kỳ |
| Tỷ lệ mở email (open rate) 21%           | số email được mở / số email gửi  |
| Tỷ lệ hàng lỗi 0,3%                      | số sản phẩm lỗi / tổng sản phẩm  |

Không ai đếm "kết cục đồng khả năng" để ra 2,3% cả — người ta **đo tần suất trên dữ liệu quá khứ**
rồi dùng nó làm xác suất cho tương lai.

Và cũng vì thế mà điều kiện "lặp lại như nhau" là **cảnh báo nghiêm túc cho dân marketing**:
conversion rate đo trong tháng 12 (mùa mua sắm) không dùng được cho tháng 2. Bộ điều kiện đã đổi
thì tần suất cũ hết giá trị. Đây là sai lầm phổ biến khi lập kế hoạch doanh số.

Câu hỏi thực tế: **bao nhiêu lượt truy cập thì mới tin được con số 2,3%?** Giáo trình chưa trả lời
ở đây; đó là nội dung của **khoảng tin cậy** (bài 11).

---

## 6. Định nghĩa tiên đề của Kolmogorov

Hai định nghĩa trên đều có lỗ hổng (tr. 16):

- **Cổ điển** không dùng được khi không xây được hệ đầy đủ các sự kiện đồng khả năng.
- **Thống kê** chỉ là giá trị xấp xỉ, đòi hỏi số quan sát rất lớn, và tần suất tìm được phải lớn
  hơn nhiều sai số đo lẫn sai số tính toán.

Nên cần một nền móng tổng quát. Kolmogorov (Kolmogorov, 1933) giải quyết bằng cách **không định
nghĩa xác suất là gì cả** — chỉ liệt kê các tính chất nó phải thoả mãn.

### Bước 1: xây hệ thống sự kiện $\mathcal{A}$

Quay lại không gian $\Omega$. Xác định một hệ thống $\mathcal{A}$ gồm các **tập con** của $\Omega$;
phần tử của $\mathcal{A}$ gọi là các sự kiện ngẫu nhiên. Yêu cầu (tr. 17):

$$
\begin{aligned}
&\text{(i)} && \Omega \in \mathcal{A} \\
&\text{(ii)} && A, B \in \mathcal{A} \Rightarrow \overline{A},\ \overline{B},\ A+B,\ AB \in \mathcal{A}
\end{aligned}
$$

Hệ thống thoả mãn hai điều kiện trên gọi là **đại số Boole** (Boolean algebra; giáo trình phiên âm *đại số Bun*). Ý nghĩa: *làm phép
toán trên sự kiện thì vẫn ra sự kiện* — hệ thống đóng kín.

Yêu cầu thêm điều kiện thứ ba cho dãy **vô hạn**:

$$\text{(iii)} \quad A_1, A_2, \dots, A_n, \dots \in \mathcal{A} \Rightarrow \sum_{n=1}^{\infty} A_n \in \mathcal{A} \ \text{ và } \ \prod_{n=1}^{\infty} A_n \in \mathcal{A}$$

thì được **trường Borel** (Borel field), hay **$\sigma$-đại số**.

### Bước 2: ba tiên đề

**Định nghĩa (tr. 17).** Xác suất trên $(\Omega, \mathcal{A})$ là một hàm số xác định trên
$\mathcal{A}$, nhận giá trị trong $[0; 1]$, thoả mãn 3 tiên đề:

$$
\begin{aligned}
&(T_1) && P(\Omega) = 1 \\
&(T_2) && P(A + B) = P(A) + P(B) \quad (A, B \text{ xung khắc}) \\
&(T_3) && \text{Nếu } A_i \supset A_j \ \forall i < j \ \text{ và } \ A_1 A_2 \dots A_n \dots = V \text{ thì } P(A_n) \to 0
\end{aligned}
$$

Có thể thay $(T_2)$ và $(T_3)$ bằng một **tiên đề cộng mở rộng** duy nhất (tr. 18):

$$(T_4) \quad \{A_n\} \text{ xung khắc từng đôi}, \ A = \sum_{n=1}^{\infty} A_n \Rightarrow P(A) = \sum_{n=1}^{\infty} P(A_n)$$

Từ hệ tiên đề này chứng minh được toàn bộ 5 tính chất ở mục 2.

### Bước 3: không gian xác suất

Bộ ba $\{\Omega, \mathcal{A}, P\}$ gọi là **không gian xác suất**. Nhìn từ lý thuyết tập hợp, định
nghĩa tiên đề chính là việc đưa vào $\Omega$ một **độ đo không âm, trực chuẩn, cộng tính** (tr. 18).

### ⚠️ Hai điều giáo trình lưu ý

1. **Hệ tiên đề chưa đầy đủ:** "ứng với một tập $\Omega$ có thể chọn xác suất theo nhiều cách khác
   nhau" (tr. 17). Tiên đề chỉ nói $P$ phải *thoả mãn gì*, không nói $P$ *bằng bao nhiêu*.
   Con số cụ thể vẫn phải lấy từ định nghĩa cổ điển (đếm) hoặc thống kê (đo).
2. **Phải có đủ ba thành phần:** không chỉ $\Omega$, mà cả $\mathcal{A}$ và hàm $P$.

### 💼 Góc QTKD

Nghe rất trừu tượng, nhưng tiên đề chính là **quy tắc kiểm tra tính nhất quán của số liệu**.
Một báo cáo thị phần:

| Hãng     | A   | B   | C   | Khác |
| -------- | --- | --- | --- | ---- |
| Thị phần | 42% | 31% | 20% | 9%   |

Tổng $= 102\%$. Vi phạm $(T_1)$: $P(\Omega) = 1$. Báo cáo này sai, không cần biết số liệu lấy ở đâu.

Ví dụ tinh vi hơn — một khảo sát khách hàng công bố:

- 60% khách hàng dùng sản phẩm trên điện thoại
- 55% dùng trên máy tính
- 30% dùng cả hai

Kiểm bằng công thức cộng (bài 3): $P(\text{ĐT} + \text{MT}) = 0{,}60 + 0{,}55 - 0{,}30 = 0{,}85$.
Vậy 15% khách không dùng thiết bị nào — mâu thuẫn, vì họ phải dùng *một trong hai* mới là khách hàng.
Số "30% dùng cả hai" chắc chắn bị báo cáo thiếu.

**Tiên đề Kolmogorov cho bạn quyền bác bỏ một báo cáo mà không cần điều tra lại dữ liệu gốc.**

---

## 7. 📚 Ba định nghĩa: chọn cái nào khi nào

Giáo trình trình bày ba định nghĩa nối tiếp nhau nhưng không tổng kết. Bảng dưới là phần bổ sung.

|                       | **Cổ điển**                      | **Hình học**                | **Thống kê**                       | **Tiên đề**        |
| --------------------- | -------------------------------- | --------------------------- | ---------------------------------- | ------------------ |
| Công thức             | $m/n$                            | $\text{đo}(S)/\text{đo}(G)$ | $\lim m/n$                         | (không có)         |
| Cần gì                | $\Omega$ hữu hạn, đồng khả năng  | $\Omega$ là miền hình học   | dữ liệu quá khứ, phép thử lặp được | $\sigma$-đại số    |
| Tính trước hay đo sau | **trước** (không cần thí nghiệm) | **trước**                   | **sau** (phải có dữ liệu)          | —                  |
| Chính xác?            | tuyệt đối                        | tuyệt đối                   | gần đúng, tốt dần theo $n$         | —                  |
| Vai trò               | công cụ làm bài tập              | mở rộng sang vô hạn         | công cụ đi làm                     | nền móng lý thuyết |
| Điểm chết             | không có đối xứng thì bó tay     | phải xác định được độ đo    | điều kiện lặp lại như nhau         | không cho ra số    |

**Cách chọn trong 10 giây:**

```
Bài toán cho bạn cái gì?
   │
   ├─ Cho cấu trúc (bao nhiêu bi, bao nhiêu sản phẩm, xúc sắc)
   │        và các kết cục đối xứng nhau?          →  CỔ ĐIỂN, đếm m/n
   │
   ├─ Cho một khoảng / miền liên tục
   │        (thời gian, chiều dài, diện tích)?     →  HÌNH HỌC, đo tỷ lệ
   │
   ├─ Cho bảng số liệu quá khứ,
   │        không có đối xứng nào?                 →  THỐNG KÊ, lấy tần suất
   │
   └─ Hỏi "công thức này có hợp lệ không",
            "số liệu này có nhất quán không"?      →  TIÊN ĐỀ, kiểm tính chất
```

**Điểm giao nhau quan trọng:** ba định nghĩa đầu **không mâu thuẫn**. Với đồng tiền cân đối, cổ điển
cho $1/2$ và thống kê cũng tiến về $1/2$. Luật số lớn (bài 9) chứng minh điều này *phải* xảy ra.
Tiên đề bao trùm cả ba như trường hợp riêng.

---

## 8. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+** (macOS/Linux có sẵn). Lưu file rồi gõ `python3 bai-02-dinh-nghia.py`.
> Chỉ dùng thư viện chuẩn — **không cần cài gói nào**.

Code làm bốn việc: liệt kê thật $\Omega$ của thí dụ 2.2 để thấy cái bẫy 11-vs-36; giải thí dụ 2.3
bằng cả hai kiểu đếm; đối chiếu bảng gieo đồng tiền của giáo trình; và mô phỏng tần suất hội tụ.
Dùng `Fraction` để ra **phân số đúng**, không phải số thập phân làm tròn.

```python
"""Bài 2 — Ba định nghĩa của xác suất."""

import random
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb

# ─────────────────────────────────────────────────────────────
# 1. ĐỊNH NGHĨA CỔ ĐIỂN — Thí dụ 2.2 (tr. 12)
#    Gieo 2 xúc sắc, tính P(tổng = 6).
#    Bẫy: phải lấy Omega = 36 cặp, KHÔNG phải 11 giá trị tổng.
# ─────────────────────────────────────────────────────────────
omega = list(product(range(1, 7), repeat=2))   # 36 ket cuc dong kha nang
favourable = [w for w in omega if sum(w) == 6]
p_correct = Fraction(len(favourable), len(omega))
print("Omega co", len(omega), "ket cuc dong kha nang")
print("Thuan loi cho 'tong = 6':", favourable)
print("P(tong = 6) =", p_correct, "=", round(float(p_correct), 4))

# Cách SAI: coi 11 giá trị tổng (2..12) là đồng khả năng
p_wrong = Fraction(1, 11)
print("Neu coi 11 gia tri tong la dong kha nang -> P =", p_wrong,
      "(SAI, lech", round(float(p_wrong) - float(p_correct), 4), ")")

# ─────────────────────────────────────────────────────────────
# 2. Thí dụ 2.3 (tr. 12) — hộp 4 bi trắng + 6 bi đỏ, rút 2 bi
#    a) hai viên trắng   b) ít nhất 1 đỏ   c) viên thứ hai đỏ
# ─────────────────────────────────────────────────────────────
WHITE, RED = 4, 6
balls = ["T"] * WHITE + ["D"] * RED           # T = trang, D = do

# a) đếm KHÔNG thứ tự (tổ hợp) và CÓ thứ tự (chỉnh hợp) -> cùng đáp số
unordered = list(combinations(range(10), 2))
ordered = list(permutations(range(10), 2))
a_unordered = Fraction(sum(1 for c in unordered if all(balls[i] == "T" for i in c)),
                       len(unordered))
a_ordered = Fraction(sum(1 for c in ordered if all(balls[i] == "T" for i in c)),
                     len(ordered))
print()
print("a) P(2 trang) to hop  =", a_unordered, "| chinh hop =", a_ordered,
      "| bang nhau:", a_unordered == a_ordered)
print("   Kiem lai bang cong thuc: C(4,2)/C(10,2) =",
      Fraction(comb(4, 2), comb(10, 2)))

# b) dùng đối lập: P(it nhat 1 do) = 1 - P(ca 2 trang)
b = 1 - a_unordered
print("b) P(it nhat 1 do) = 1 -", a_unordered, "=", b)

# c) viên THỨ HAI đỏ -> bắt buộc đếm có thứ tự
c = Fraction(sum(1 for x, y in ordered if balls[y] == "D"), len(ordered))
print("c) P(vien thu hai do) =", c, "= P(rut 1 bi do tu 10 bi) =", Fraction(6, 10))

# ─────────────────────────────────────────────────────────────
# 3. ĐỊNH NGHĨA HÌNH HỌC — Thí dụ 2.4 (tr. 14)
#    Dây 1000 m, đứt cách tổng đài không quá 100 m.
# ─────────────────────────────────────────────────────────────
print()
print("P(dut trong 100m dau) = 100/1000 =", Fraction(100, 1000))

# ─────────────────────────────────────────────────────────────
# 4. ĐỊNH NGHĨA THỐNG KÊ — tần suất ổn định dần
#    Số liệu THẬT của giáo trình (tr. 15) + mô phỏng để thấy quy luật.
# ─────────────────────────────────────────────────────────────
print()
print("So lieu that trong giao trinh (tr. 15), gieo dong tien:")
print(f"{'Nguoi thi nghiem':<18}{'So lan gieo':>12}{'So lan sap':>12}{'Tan suat':>10}")
for who, tosses, heads in [("Buffon", 4040, 2048),
                           ("Pearson", 12000, 6019),
                           ("Pearson", 24000, 12012)]:
    print(f"{who:<18}{tosses:>12}{heads:>12}{heads / tosses:>10.4f}")

print()
print("Mo phong (seed co dinh 2026 -> chay lai ra y het):")
rng = random.Random(2026)
heads = 0
print(f"{'n':>8}{'so lan sap':>12}{'tan suat':>10}{'|lech so voi 0,5|':>20}")
for n in range(1, 100_001):
    heads += rng.random() < 0.5
    if n in (10, 100, 1_000, 10_000, 100_000):
        f = heads / n
        print(f"{n:>8}{heads:>12}{f:>10.4f}{abs(f - 0.5):>20.4f}")

# ─────────────────────────────────────────────────────────────
# 5. ĐỊNH NGHĨA TIÊN ĐỀ — kiểm 3 tiên đề Kolmogorov trên Omega ở mục 1
# ─────────────────────────────────────────────────────────────
def P(event):
    """Xac suat co dien tren Omega 36 ket cuc."""
    return Fraction(sum(1 for w in omega if event(w)), len(omega))

print()
even_sum = lambda w: sum(w) % 2 == 0
sum_is_6 = lambda w: sum(w) == 6
sum_is_7 = lambda w: sum(w) == 7

assert P(lambda w: True) == 1                       # (T1) P(Omega) = 1
assert P(lambda w: sum_is_6(w) or sum_is_7(w)) == P(sum_is_6) + P(sum_is_7)  # (T2)
assert P(lambda w: False) == 0                      # he qua: P(V) = 0
assert P(lambda w: not even_sum(w)) == 1 - P(even_sum)      # P(A ngang) = 1 - P(A)
print("(T1) P(Omega) = 1                       : OK")
print("(T2) P(A+B) = P(A)+P(B) khi A,B xung khac: OK")
print("     P(V) = 0  va  P(A ngang) = 1 - P(A) : OK")
print("P(tong chan) =", P(even_sum), "| P(tong le) =", P(lambda w: not even_sum(w)))
```

Kết quả chạy thật:

```
Omega co 36 ket cuc dong kha nang
Thuan loi cho 'tong = 6': [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
P(tong = 6) = 5/36 = 0.1389
Neu coi 11 gia tri tong la dong kha nang -> P = 1/11 (SAI, lech -0.048 )

a) P(2 trang) to hop  = 2/15 | chinh hop = 2/15 | bang nhau: True
   Kiem lai bang cong thuc: C(4,2)/C(10,2) = 2/15
b) P(it nhat 1 do) = 1 - 2/15 = 13/15
c) P(vien thu hai do) = 3/5 = P(rut 1 bi do tu 10 bi) = 3/5

P(dut trong 100m dau) = 100/1000 = 1/10

So lieu that trong giao trinh (tr. 15), gieo dong tien:
Nguoi thi nghiem   So lan gieo  So lan sap  Tan suat
Buffon                    4040        2048    0.5069
Pearson                  12000        6019    0.5016
Pearson                  24000       12012    0.5005

Mo phong (seed co dinh 2026 -> chay lai ra y het):
       n  so lan sap  tan suat   |lech so voi 0,5|
      10           3    0.3000              0.2000
     100          43    0.4300              0.0700
    1000         495    0.4950              0.0050
   10000        5122    0.5122              0.0122
  100000       50200    0.5020              0.0020

(T1) P(Omega) = 1                       : OK
(T2) P(A+B) = P(A)+P(B) khi A,B xung khac: OK
     P(V) = 0  va  P(A ngang) = 1 - P(A) : OK
P(tong chan) = 1/2 | P(tong le) = 1/2
```

Ba điều đáng để ý trong kết quả:

1. **Dòng `0.5069`** là con số máy tính ra từ chính $2048/4040$ của giáo trình — khác với `0,5080`
   sách in. Đây là bằng chứng cho phần đính chính ở mục 5.
2. **Cột `|lệch so với 0,5|`** không giảm đều: ở $n = 10\,000$ lệch $0{,}0122$, lớn hơn ở
   $n = 1\,000$ ($0{,}0050$). Tần suất hội tụ **theo nghĩa xác suất**, không phải hội tụ đơn điệu.
   Nói cách khác: chạy nhiều thí nghiệm hơn *thường* chính xác hơn, chứ không *chắc chắn* chính xác
   hơn ở từng bước. Bài 9 sẽ phát biểu chính xác điều này.
3. `Fraction` cho ra **`5/36`, `2/15`, `13/15`** — đúng dạng đáp án thi. Trong Excel không có kiểu
   phân số đúng; muốn ra phân số phải tự rút gọn.

---

## 9. Tự thử

1. Đổi câu hỏi ở mục 1 từ `sum(w) == 6` thành `sum(w) == 7`. Đáp số bao nhiêu? Tổng nào có xác suất
   lớn nhất, và vì sao?
2. In ra bảng đầy đủ $P(\text{tổng} = k)$ với $k = 2, 3, \dots, 12$. Cộng cả 11 xác suất lại có bằng 1
   không? Đó là tiên đề nào?
3. Đổi hộp bi ở mục 2 thành 5 trắng, 5 đỏ, rút 3 bi. Câu b) "ít nhất 1 đỏ" ra bao nhiêu?
   Dùng đối lập có nhanh hơn tính trực tiếp không?
4. Đổi `random.Random(2026)` thành `random.Random(7)`. Các con số ở mục 4 đổi hết, nhưng cột cuối
   ở $n = 100\,000$ có còn nhỏ không? Chạy thử 3 seed khác nhau và ghi lại.
5. Sửa mô phỏng để đồng tiền **không cân đối**: đổi `rng.random() < 0.5` thành `< 0.3`. Tần suất
   hội tụ về đâu? Định nghĩa cổ điển có tính được con số đó không?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt (giáo trình)        | Tiếng Anh                     | Ghi chú                                             |
| ------------------------------ | ----------------------------- | --------------------------------------------------- |
| Đồng khả năng                  | Equally likely                | điều kiện bắt buộc của định nghĩa cổ điển           |
| Kết cục thuận lợi              | Favourable outcome            | tử số của $m/n$                                     |
| Định nghĩa cổ điển             | Classical definition          | Laplace                                             |
| Định nghĩa hình học            | Geometric probability         | thay đếm bằng đo                                    |
| Độ đo                          | Measure                       | độ dài / diện tích / thể tích                       |
| Tần suất                       | Relative frequency            | $m/n$ trên dữ liệu thật                             |
| Định nghĩa thống kê            | Frequentist definition        | trường phái tần suất                                |
| Tính ổn định của tần suất      | Stability of frequency        | nền tảng thực nghiệm của xác suất                   |
| Đại số Boole                   | Boolean algebra               | đóng kín với $+$, $\cdot$, $\overline{\phantom{A}}$ |
| Trường Borel, $\sigma$-đại số | Borel field, $\sigma$-algebra | thêm điều kiện vô hạn                               |
| Không gian xác suất            | Probability space             | bộ ba $\{\Omega, \mathcal{A}, P\}$                  |
| Trực chuẩn                     | Normalized                    | $P(\Omega) = 1$                                     |
| Cộng tính                      | Additive                      | $P(A+B) = P(A)+P(B)$ khi xung khắc                  |

**Phiên âm trong sách.** Giáo trình 1997 viết tên riêng theo lối phiên âm; khoá học này dùng
**tên gốc**. Bài này gặp: *Kôn-mô-gô-rôp* = **Kolmogorov** · *Bô-ren* = **Borel** ·
*Bun* = **Boole** · *Buýt-phông* = **Buffon** · *Piếc-xơn* = **Pearson** ·
*Béc-nu-li* = **Bernoulli**.

---

## 11. Câu hỏi tự kiểm tra

1. Vì sao không thể dùng định nghĩa cổ điển để tính xác suất "ngày mai trời mưa"?
   Nêu đủ **hai** lý do khác nhau.
2. Gieo 3 đồng tiền. Có bạn nói $\Omega = \{0, 1, 2, 3\}$ mặt sấp, nên $P(2 \text{ sấp}) = 1/4$.
   Sai ở đâu? Đáp án đúng là bao nhiêu?
3. Chứng minh tính chất (v): nếu $A \Rightarrow B$ thì $P(A) \le P(B)$, dùng định nghĩa cổ điển.
4. Một sự kiện có $P(A) = 0$. Nó có phải sự kiện bất khả $V$ không? Cho một ví dụ minh hoạ.
5. Xe buýt chạy đều 15 phút một chuyến. Bạn ra bến vào lúc ngẫu nhiên.
   Xác suất phải chờ quá 10 phút là bao nhiêu? Dùng định nghĩa nào?
6. Một shop online có 4.000 lượt truy cập và 92 đơn hàng trong tháng.
   a) Xác suất một khách vào shop sẽ đặt hàng là bao nhiêu? Dùng định nghĩa nào?
   b) Con số đó có phải giá trị chính xác không? Nếu tháng sau có 4.000 lượt, có chắc được 92 đơn?
7. Kiểm tra tính nhất quán: khảo sát nói 70% khách hài lòng về giá, 65% hài lòng về chất lượng,
   và 20% hài lòng về cả hai. Có gì bất thường không? (Gợi ý: dùng công thức cộng ở bài 3.)
8. Bài 12 (tr. 36): một cậu bé có 10 bi, 6 đỏ và 4 xanh, làm mất 1 viên. Rút hú hoạ 1 bi trong số
   còn lại, tìm xác suất đó là bi đỏ. (Gợi ý: nghĩ theo lối lý luận ở thí dụ 2.3c.)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 2 — BA ĐỊNH NGHĨA CỦA XÁC SUẤT               (Ch. I §2, tr. 11–18)  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ① CỔ ĐIỂN         P(A) = m / n                                          ║
║      m = số kết cục THUẬN LỢI,  n = tổng số kết cục                      ║
║      ĐIỀU KIỆN BẮT BUỘC: n kết cục phải ĐỒNG KHẢ NĂNG                    ║
║      ⚠ chọn Ω mịn nhất. 2 xúc sắc → 36 cặp, KHÔNG phải 11 tổng           ║
║                                                                          ║
║  ② HÌNH HỌC        P(A) = đo(S) / đo(G)                                  ║
║      độ đo = độ dài / diện tích / thể tích                               ║
║      ⚠ P(A) = 0  KHÔNG  có nghĩa là bất khả (điểm có độ dài 0)          ║
║                                                                          ║
║  ③ THỐNG KÊ        P(A) = lim (m/n)  khi n → ∞                           ║
║      lấy TẦN SUẤT trên dữ liệu quá khứ làm xác suất                      ║
║      ⚠ phép thử phải LẶP LẠI NHƯ NHAU                                    ║
║      → đây là định nghĩa dân kinh doanh dùng hằng ngày                   ║
║                                                                          ║
║  ④ TIÊN ĐỀ (Kolmogorov)     không gian xác suất {Ω, 𝒜, P}               ║
║      (T1) P(Ω) = 1                                                       ║
║      (T2) P(A+B) = P(A) + P(B)     khi A, B xung khắc                    ║
║      (T3) A₁ ⊃ A₂ ⊃ ... , ∏Aₙ = V  ⟹  P(Aₙ) → 0                         ║
║      ⚠ tiên đề KHÔNG cho ra con số, chỉ ràng buộc tính nhất quán        ║
║                                                                          ║
║  NĂM TÍNH CHẤT (đúng cho MỌI định nghĩa)                                 ║
║      (i)   0 ≤ P(A) ≤ 1                                                  ║
║      (ii)  P(U) = 1,  P(V) = 0                                           ║
║      (iii) A,B xung khắc → P(A+B) = P(A) + P(B)                          ║
║      (iv)  P(Ā) = 1 − P(A)          ← công cụ dùng nhiều nhất           ║
║      (v)   A ⇒ B  thì  P(A) ≤ P(B)  ← dùng để kiểm tra đáp án           ║
║                                                                          ║
║  CHỌN ĐỊNH NGHĨA NÀO?                                                    ║
║      có đối xứng, đếm được  → cổ điển                                    ║
║      miền liên tục          → hình học                                   ║
║      có bảng số liệu        → thống kê                                   ║
║      hỏi "có hợp lệ không"  → tiên đề                                    ║
║                                                                          ║
║  ⚠ ĐÍNH CHÍNH tr. 15: Buffon 2048/4040 = 0,5069 (sách in 0,5080)        ║
║                                                                          ║
║  💼 QTKD: conversion rate, churn rate, tỷ lệ lỗi = TẦN SUẤT              ║
║           tổng thị phần ≠ 100%  →  vi phạm (T1), bác bỏ báo cáo         ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội, Chương I §2, tr. 11–18.
  File: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](../tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)
- Bảng gieo đồng tiền: tr. 15 — đã đối chiếu bản quét gốc, sách in `0,5080` cho Buffon,
  giá trị đúng là `0,5069`.

---

**Điều hướng:** [🏠 Mục lục khoá học](../README.md) ·
Bài trước: [Bài 1 — Sự kiện ngẫu nhiên và giải tích kết hợp](bai_01_su_kien_ngau_nhien_va_giai_tich_ket_hop.md) ·
Bài sau: Bài 3 — Xác suất có điều kiện và công thức Bernoulli
