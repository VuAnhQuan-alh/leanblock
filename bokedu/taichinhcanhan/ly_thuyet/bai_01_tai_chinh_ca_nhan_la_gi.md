# Bài 1 — Tài chính cá nhân là gì

> [!info] Về bài này
> Bài học dựa trên **Unit 1 của Class 1** — C1 tr. 4–6. Ba trang, khoảng 700 chữ: unit ngắn nhất
> của cả hai tập, và là unit duy nhất nói về **toàn cảnh**.
> **Cần đọc trước:** [Bài 0](bai_00_bat_dau_tu_dau.md) — quy ước trích dẫn và bản đồ khoá học.
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
> **Code:** [`thuc_hanh/bai-01-bao-lau-thi-den.py`](../thuc_hanh/bai-01-bao-lau-thi-den.py)
> — lấy công thức của chính cuốn sách trả lời câu hỏi mà sách né: *bao lâu thì đến?* Mục 5.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).

---

## Mục lục

<!-- MUC-LUC -->
- [1. Định nghĩa của sách, và một chỗ không kiểm chứng được](#1-định-nghĩa-của-sách-và-một-chỗ-không-kiểm-chứng-được)
- [2. Ba bài toán](#2-ba-bài-toán)
- [3. Bốn bước của một kế hoạch hoàn chỉnh](#3-bốn-bước-của-một-kế-hoạch-hoàn-chỉnh)
- [4. Ba bài toán và bốn bước không khớp nhau](#4-ba-bài-toán-và-bốn-bước-không-khớp-nhau)
- [5. [bổ sung] Bao lâu thì đến — tính bằng chính công thức của sách](#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách)
- [6. Thứ tự có ràng buộc — vì sao không nhảy thẳng vào bước cuối](#6-thứ-tự-có-ràng-buộc--vì-sao-không-nhảy-thẳng-vào-bước-cuối)
- [7. [bổ sung] "Kỹ năng có thể học được" đúng đến đâu](#7-bổ-sung-kỹ-năng-có-thể-học-được-đúng-đến-đâu)
- [8. Tự thử](#8-tự-thử)
- [9. Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
- [10. Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Định nghĩa của sách, và một chỗ không kiểm chứng được

Sách mở đầu bằng một định nghĩa mượn:

> [!quote]
> *"Định nghĩa của Wikipedia: 'Tài chính cá nhân là việc quản lý tài chính mà mỗi cá nhân hoặc một
> gia đình thực hiện để lập ngân sách, tiết kiệm và chi tiêu các nguồn tiền mặt theo thời gian, có
> tính đến các rủi ro tài chính và các sự kiện trong tương lai'."* — C1 tr. 4

Định nghĩa này gọn và đủ. Bốn động từ — **lập ngân sách, tiết kiệm, chi tiêu, tính đến rủi ro** —
là bốn việc mà mười ba bài còn lại sẽ làm kỹ.

**Một lưu ý về phương pháp, không phải về nội dung.** Trích Wikipedia mà không ghi phiên bản ngày
nào thì **không kiểm chứng được**. Wikipedia là trang ai cũng sửa được; câu hôm nay khác câu năm
ngoái. Đây không phải lỗi làm sai kiến thức — định nghĩa vẫn đúng — nhưng nó là loại trích dẫn mà
[bài 0](bai_00_bat_dau_tu_dau.md#2-quy-ước-trích-dẫn--vì-sao-không-có-số-trang-giấy) đã dựng cả một
quy ước để tránh. Khi bạn gặp một con số hay một câu định nghĩa trong bất kỳ tài liệu tài chính
nào, câu hỏi đầu tiên luôn là: **tra ngược về đâu?**

Sách tự diễn giải lại, và bản diễn giải này mới là thứ đáng nhớ:

> [!quote]
> *"Tài chính cá nhân là những gì xoay quanh chủ đề tiền bạc của một cá nhân cụ thể."* — C1 tr. 4

Ba chữ **"một cá nhân cụ thể"** đặt ra nguyên tắc chi phối cả khoá học: **không có lời khuyên tài
chính nào đúng cho tất cả mọi người.** Sách nhắc lại nguyên tắc này ít nhất ba lần nữa — ở
C1 tr. 17 khi nói mọi quyết định phải dựa trên bảng cân đối của riêng bạn, và ở C1 tr. 31 khi nói
*"Không có lời khuyên nào đúng cho tất cả các trường hợp."*

---

## 2. Ba bài toán

Cả hai tập sách đứng trên đúng ba chân:

```
   ┌──────────────────────────────────────────────────────────────────┐
   │  KIẾM TIỀN   "Qua công việc, sự nghiệp, hoạt động kinh doanh…    │
   │              Làm thế nào để mang về nhiều tiền nhất, thông qua   │
   │              việc trao đổi với những GIÁ TRỊ chúng ta đang có."  │
   ├──────────────────────────────────────────────────────────────────┤
   │  GIỮ TIỀN    "quản lý, tiết kiệm, bảo vệ tiền"                   │
   ├──────────────────────────────────────────────────────────────────┤
   │  ĐẦU TƯ      "tìm cách để tiền bạc tự thân làm việc, tự động     │
   │              mang thêm tiền về ngay cả khi ta đang ngủ"          │
   └──────────────────────────────────────────────────────────────────┘
                                                            C1 tr. 4–5
```

Ba bài toán này **không ngang hàng nhau**, và sách nói rõ bài toán nào quan trọng nhất ngay khi
giới thiệu nó:

> [!quote]
> *"Vì hầu hết đều đồng ý rằng số tiền bạn kiếm được không quan trọng bằng số tiền bạn giữ được.
> Và khi tìm kiếm cụm từ 'tài chính cá nhân' trên Google thì đứng trước nó luôn có từ khoá 'quản lý'."*
> — C1 tr. 5

Đó là lý do khoá học dành **năm bài** (3, 7, 8, 9, và một phần bài 2) cho bài toán giữ tiền, và
**hai bài** cho đầu tư.

Chú ý một chữ trong ô đầu tiên: **giá trị**. Sách không nói kiếm tiền là bán thời gian; nó nói kiếm
tiền là *"trao đổi với những giá trị chúng ta đang có"*. Chữ đó chuẩn bị cho toàn bộ **bài 5**,
nơi C2 tr. 5 đưa ra công thức
$\text{Thu nhập} = \text{Giá trị} \times \text{Thời gian} \times \text{Quy mô}$ và chỉ ra rằng
lương theo giờ chỉ là *cách đo tiện lợi*, không phải cái được trả tiền.

Và sách đóng khung ba bài toán bằng một mệnh đề hoặc–hoặc:

> [!quote]
> *"Hoặc bạn sẽ phải lần lượt tìm đáp án cho 3 bài toán này. Hoặc bạn sẽ giống số đông ngoài kia,
> chịu áp lực về tiền bạc hàng ngày."* — C1 tr. 5

---

## 3. Bốn bước của một kế hoạch hoàn chỉnh

> [!quote]
> *"Một kế hoạch tài chính cá nhân hoàn chỉnh bao gồm 4 bước sau:"* — C1 tr. 5

| Bước | Sách viết | Làm ở bài |
| ---: | --- | --- |
| 1 | Xác định dòng tiền và giá trị tài sản | 2, 3, 4 |
| 2 | Xác định hồ sơ rủi ro | 12 |
| 3 | Xác định mục tiêu và lập kế hoạch | 14 |
| 4 | Đầu tư theo danh mục đề xuất | 13 |

Bốn bước này là **xương sống của Class 1**: Unit 2 làm bước 1 phần dòng tiền, Unit 3 làm bước 1
phần tài sản, Unit 4 làm bước 2, Unit 5 làm bước 3 và 4. Đọc xong bài 1 là biết Class 1 đi đâu.

Bước 4 trong sách gắn liền với một ứng dụng thương mại — phần đó khoá học **đã cắt**, lý do ở
[bài 0 mục 5](bai_00_bat_dau_tu_dau.md#5-hai-mảng-bổ-sung-và-phần-đã-cắt). Chữ *"danh mục đề xuất"*
được giữ nguyên vì nó là khái niệm thật (phân bổ tài sản theo hồ sơ rủi ro), chỉ có **người đề
xuất** là thay đổi: bài 12 dạy bạn tự dựng.

---

## 4. Ba bài toán và bốn bước không khớp nhau

Đây là chỗ đáng dừng lại nhất của cả unit, và sách không nói ra.

Đặt ba bài toán cạnh bốn bước, rồi hỏi: **bước nào giải bài toán kiếm tiền?**

```
   BA BÀI TOÁN                    BỐN BƯỚC CỦA KẾ HOẠCH
   ───────────                    ─────────────────────
   Kiếm tiền   ──────────────▶    (không có bước nào)
                             ┌──  1. dòng tiền và tài sản
   Giữ tiền    ──────────────┤
                             └──  3. mục tiêu và kế hoạch   (một phần)
                             ┌──  2. hồ sơ rủi ro
   Đầu tư      ──────────────┤    3. mục tiêu và kế hoạch   (một phần)
                             └──  4. đầu tư theo danh mục
```

**Bài toán thứ nhất không có bước nào cả.** Kế hoạch bốn bước bắt đầu từ chỗ *"bạn đang kiếm được
bao nhiêu"* và coi con số đó là dữ kiện cho trước.

Điều này không phải suy diễn. Nó được chính cấu trúc hai tập sách xác nhận: **toàn bộ chủ đề kiếm
tiền nằm ở Unit 1 của Class 2** — tức là ở cuốn thứ hai, *bên ngoài* kế hoạch bốn bước. Và Class 1
kết thúc bằng câu:

> [!quote]
> *"Sang đến Class 2, chúng ta sẽ cùng nhau giải 3 bài toán cụ thể: kiếm tiền, giữ tiền, tạo tiền."*
> — C1 tr. 40

Nói cách khác: Class 1 là **kế hoạch bốn bước**, Class 2 là **ba bài toán**. Hai khung khác nhau,
chồng lên nhau một phần, và sách không bao giờ ghép chúng lại.

**Hệ quả thực tế cho bạn.** Một kế hoạch tài chính chỉ tối ưu phía chi tiêu và đầu tư sẽ đụng trần
rất nhanh. [Mục 5](#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách) cho thấy trần
đó nằm ở đâu bằng con số. Chính sách cũng thừa nhận điều này về sau, ở C2 tr. 27:

> [!quote]
> *"bạn không thể giảm chi tiêu được mãi. Chúng ta không muốn giàu có bằng cách sống tằn tiện…
> điều quan trọng hơn cần làm là tìm cách tăng thu nhập."*

Đó là câu đúng, nhưng nó nằm ở **trang 27 của tập thứ hai** — cách chỗ này rất xa. Khoá học kéo nó
lên sớm: bài 5 (kiếm tiền) và bài 6 (thuế) đặt **trước** bài 7 (phân bổ thu nhập), chứ không phải sau.

---

## 5. [bổ sung] Bao lâu thì đến — tính bằng chính công thức của sách

Sách hứa hai lần, ở hai tập, hai con số:

| Sách viết | Ở đâu |
| --- | --- |
| *"đó là một lộ trình dài hạn, có thể **5 năm, 10 năm**, hoặc hơn thế nữa"* | C1 tr. 5 |
| *"sau vài năm (**tối đa là 20 năm**), chúng ta có một kế hoạch đúng đắn đạt đến sự tự do tài chính"* | C2 tr. 15 |

Năm năm và hai mươi năm cách nhau **bốn lần**. Câu hỏi tự nhiên: cái nào đúng?

Sách không trả lời. Nhưng sách đưa đủ nguyên liệu để **tự trả lời**, và ta không cần thêm giả định
nào từ bên ngoài:

- công thức số tiền cần thiết, C1 tr. 31: $\text{số tiền cần} = \dfrac{\text{chi tiêu một năm}}{\text{lợi suất} - \text{lạm phát}}$
- giả định của chính sách trong ví dụ đi kèm: lợi suất **12%**/năm, lạm phát **4%**/năm
- ba công thức phân bổ thu nhập ở C2 tr. 18–25

### Số năm không phụ thuộc vào lương

Gọi $s$ là tỷ lệ thu nhập để dành mỗi năm và $g$ là lợi suất **thực** (lợi suất trừ lạm phát).
Chuẩn hoá thu nhập về 1, xuất phát từ con số 0:

$$
\text{đích} = \frac{1-s}{g}
\qquad\qquad
\text{tích luỹ sau } n \text{ năm} = s \cdot \frac{(1+g)^n - 1}{g}
$$

Cho hai vế bằng nhau, $g$ triệt tiêu, và **thu nhập cũng biến mất**:

$$
s\left[(1+g)^n - 1\right] = 1-s
\quad\Longrightarrow\quad
(1+g)^n = \frac{1}{s}
\quad\Longrightarrow\quad
\boxed{\;n = \frac{-\ln s}{\ln(1+g)}\;}
$$

Lương 10 triệu hay 100 triệu **không đổi được số năm**. Chỉ hai thứ đổi được: **tỷ lệ** để dành, và
lợi suất thực. Đây là kết quả đáng nhớ nhất của bài này, và nó là hệ quả trực tiếp của công thức
C1 tr. 31 — người thu nhập cao có đích đến cao hơn đúng bằng tỷ lệ họ tiêu nhiều hơn.

Với giả định của sách ($g = 12\% - 4\% = 8\%$):

```
  tỷ lệ tiết kiệm      số năm
  ─────────────────────────────
        10%             29,9   ███████████████
        20%             20,9   ██████████
        30%             15,6   ████████
        40%             11,9   ██████
        50%              9,0   █████
        70%              4,6   ██
```

### Hai lời hứa đòi hỏi gì

Đảo ngược công thức:

| Lời hứa | Đòi tiết kiệm |
| --- | ---: |
| C1 tr. 5 — *"5 năm"* | **68%** thu nhập |
| C1 tr. 5 — *"10 năm"* | **46%** thu nhập |
| C2 tr. 15 — *"tối đa là 20 năm"* | **21%** thu nhập |

### Và chính sách khuyên để dành bao nhiêu?

| Công thức của sách | Để dành | Ra số năm | Nguồn |
| --- | ---: | ---: | --- |
| 6 jars — chỉ FFA | 10% | **29,9** | C2 tr. 18 |
| 6 jars — FFA + LTSS | 20% | **20,9** | C2 tr. 18, 21 |
| 50/30/20 — vế *Savings* | 20% | **20,9** | C2 tr. 23 |
| 70/30 — đầu tư vốn + tiết kiệm | 20% | **20,9** | C2 tr. 25 |

Ba hệ phân bổ của ba tác giả khác nhau, và cả ba **hội tụ về đúng 20%**. Đó không phải trùng hợp —
bài 7 sẽ cho thấy vì sao.

**Kết luận, và nó gọn:**

- Con số **20 năm** của C2 tr. 15 **khớp** với chính tỷ lệ mà sách khuyên. Sách tự nhất quán ở đây.
- Con số **5 năm** của C1 tr. 5 đòi để dành **68%** thu nhập — gấp hơn ba lần con số sách tự đề
  xuất. Nó không sai, nhưng nó mô tả một người sống rất khác người mà sách đang viết cho.
- Đọc chặt hệ 6 jars (chỉ FFA mới thật sự là tiền đầu tư, C2 tr. 18) thì con số là **30 năm**.

Khoảng thật nằm giữa **21 và 30 năm**. Không phải 5.

### Và con số đó nhạy đến mức nào

Giữ nguyên tiết kiệm 20%, chỉ đổi giả định lợi suất:

```
  lợi suất kỳ vọng   lợi suất thực   số năm
  ──────────────────────────────────────────
        12%                8%          20,9
        10%                6%          27,6
         8%                4%          41,0
         6%                2%          81,3
```

Hạ lợi suất kỳ vọng từ 12% xuống 8% thì thời gian **đúng gấp đôi**. Giả định 12%/năm duy trì bền
vững suốt hai mươi năm là một giả định **mạnh** — mạnh hơn nhiều so với cách sách trình bày nó,
tức là một con số đưa ra không kèm biện luận. Bài 12 và bài 14 quay lại chỗ này.

Toàn bộ bảng trên do [`thuc_hanh/bai-01-bao-lau-thi-den.py`](../thuc_hanh/bai-01-bao-lau-thi-den.py)
tính ra. Tệp đó cũng **kiểm công thức đóng bằng mô phỏng từng năm** — hai cách phải cho cùng kết quả.

---

## 6. Thứ tự có ràng buộc — vì sao không nhảy thẳng vào bước cuối

Bốn bước ở mục 3 **không phải danh sách để chọn**. Chúng có ràng buộc thứ tự, và sách phát biểu
ràng buộc mạnh nhất ở Unit 2:

> [!quote]
> *"Điều này rất quan trọng, vì khi và chỉ khi dòng tiền dương bạn mới nên nghĩ đến việc đầu tư dài
> hạn."* — C1 tr. 12

*"Khi và chỉ khi"* là ngôn ngữ của logic, không phải lời khuyên mềm. Nó nói: chưa qua bước 1 thì
bước 4 không được phép bắt đầu.

Sách quay lại đúng nguyên tắc này ba lần nữa, mỗi lần ở một tầng khác:

| Ràng buộc | Ở đâu |
| --- | --- |
| Dòng tiền phải dương trước khi đầu tư dài hạn | C1 tr. 12 |
| Tháp tài sản xây **từ đáy lên**; người nghiệp dư lại lao thẳng vào đỉnh | C1 tr. 20–21 |
| Đang có nợ thì quỹ *Savings* dùng để trả nợ trước, *"thường chúng ta sẽ không đầu tư"* | C2 tr. 24 |
| Phải xác định mức chấp nhận rủi ro **rồi mới** chọn kênh đầu tư, không phải ngược lại | C1 tr. 32 |

Bốn câu này, ở bốn chỗ cách xa nhau, đều nói một điều: **thứ tự bị vi phạm là dạng sai lầm phổ biến
nhất trong tài chính cá nhân.** Không phải chọn sai cổ phiếu — mà là chọn cổ phiếu khi đáng lẽ phải
đang trả nợ.

Bài 4 và bài 12 làm kỹ chỗ này.

---

## 7. [bổ sung] "Kỹ năng có thể học được" đúng đến đâu

Sách đưa ra một khẳng định lạc quan và đặt nó ở vị trí trang trọng:

> [!quote]
> *"Tự do tài chính - hay cái cảnh giới mà bạn vĩnh viễn thoát khỏi ảnh hưởng của tiền bạc - là một
> kỹ năng có thể học được."* — C1 tr. 5

Phép tính ở mục 5 **ủng hộ** khẳng định này mạnh hơn cả cách sách lập luận. Số năm không phụ thuộc
lương — nghĩa là kết quả thật sự do **hành vi** quyết định chứ không do xuất phát điểm. Đó đúng là
định nghĩa của một kỹ năng.

Nhưng cùng phép tính đó cũng chỉ ra **giới hạn**, và giới hạn nằm sẵn trong chính cuốn sách. C2
tr. 19 đặt một ngưỡng cảnh báo:

> [!quote]
> *"Cảnh báo 'red flag' xuất hiện nếu NEC > 80% tổng thu nhập, lúc này bạn cần ngay lập tức tăng
> thu, hoặc mạnh tay cắt giảm chi phí."*

Ghép hai chỗ lại: nếu **chi phí thiết yếu** đã ăn hết 80% thu nhập thì phần để dành tối đa còn 20%,
và đó là trong trường hợp không tiêu một đồng nào cho bất cứ thứ gì khác — không giáo dục, không
hưởng thụ, không cho đi. Dưới ngưỡng thu nhập ấy, công thức $n = -\ln s / \ln(1+g)$ vẫn đúng nhưng
**$s$ không nằm trong tay bạn nữa**, nó do giá thuê nhà và giá thực phẩm quyết định.

Nên phát biểu đầy đủ hơn là: **tự do tài chính là một kỹ năng có thể học được, với điều kiện thu
nhập vượt một ngưỡng nhất định.** Dưới ngưỡng đó, bài toán phải giải là bài toán số một — kiếm
tiền — đúng bài toán mà kế hoạch bốn bước không có bước nào ([mục 4](#4-ba-bài-toán-và-bốn-bước-không-khớp-nhau)).

Đây không phải phản bác sách. Sách nói đúng, chỉ nói thiếu điều kiện. Và điều kiện ấy giải thích
luôn câu hỏi mà sách tự đặt ra ngay sau đó — *"Tại sao vẫn còn rất nhiều người chưa 'tốt nghiệp'
lớp kỹ năng này?"* (C1 tr. 5). Sách trả lời bằng *"nhiều người đã bỏ cuộc"*. Một phần câu trả lời
là vậy. Phần còn lại là số học.

---

## 8. Tự thử

1. **Tỷ lệ của riêng bạn.** Lấy thu nhập và chi tiêu tháng gần nhất. Tính
   $s = 1 - \text{chi tiêu}/\text{thu nhập}$. Tra bảng ở mục 5: bao nhiêu năm? Con số đó gần
   *"5 năm"* của C1 tr. 5 hay gần *"20 năm"* của C2 tr. 15 hơn?

2. **Rút ngắn năm năm.** Vẫn tỷ lệ đó, bạn cần nâng $s$ lên bao nhiêu để giảm được **5 năm**?
   Dùng $s_{\text{mới}} = s \cdot (1+g)^{-5}$ với $g = 8\%$. Mức tăng đó có khả thi không?

3. **Đổi giả định trong code.** Trong `bai-01-bao-lau-thi-den.py`, sửa `G = 0.12 - 0.04` thành
   `G = 0.09 - 0.04`. Chạy lại. **Assert nào gãy trước**, và điều đó nói gì về việc các con số
   trong bài phụ thuộc chặt vào giả định 12% đến mức nào? Nhớ sửa lại.

4. **Xuất phát không từ số 0.** Mô hình ở mục 5 giả định bắt đầu với 0 đồng. Sửa hàm `mo_phong`
   để nhận thêm tham số tài sản ban đầu. Có sẵn một khoản bằng **5 năm chi tiêu** thì rút ngắn
   được bao nhiêu năm?

5. **Bước nào cho bài toán nào.** Không nhìn lại mục 4: tự viết ba bài toán ra một cột, bốn bước
   ra cột kia, rồi nối. Bạn có nối được bài toán số một vào bước nào không?

6. **Tìm câu thứ năm.** Mục 6 dẫn bốn chỗ sách phát biểu ràng buộc thứ tự. Đọc lướt hai tập, tìm
   **một chỗ nữa** — và một chỗ mà sách có vẻ **vi phạm** chính ràng buộc đó.

---

## 9. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Tài chính cá nhân | personal finance | quản lý tiền của **một cá nhân cụ thể** — C1 tr. 4 |
| Ba bài toán | — | kiếm tiền, giữ tiền, đầu tư tiền — C1 tr. 4–5 |
| Tự do tài chính | financial freedom / independence | *"cảnh giới mà bạn vĩnh viễn thoát khỏi ảnh hưởng của tiền bạc"* — C1 tr. 5 |
| Dòng tiền | cash flow | thu trừ chi, đo trong **một khoảng** thời gian — bài 2 |
| Hồ sơ rủi ro | risk profile | mức rủi ro một người chịu được — bước 2, bài 12 |
| Danh mục đầu tư | portfolio | tập hợp tài sản đang nắm và tỷ trọng từng loại — bước 4, bài 13 |
| Thu nhập thụ động | passive income | *"tiền bạc tự thân làm việc… ngay cả khi ta đang ngủ"* — C1 tr. 5 |
| **[bổ sung]** Lợi suất thực | real return | lợi suất danh nghĩa trừ lạm phát — mẫu số của mọi phép tính ở mục 5 |
| **[bổ sung]** Tỷ lệ tiết kiệm | savings rate | phần thu nhập để dành; sách định nghĩa muộn, ở C2 tr. 26 |

---

## 10. Câu hỏi tự kiểm tra

1. Sách trích định nghĩa tài chính cá nhân từ đâu? Vì sao trích dẫn đó **không kiểm chứng được**? (mục 1)
2. Ba chữ nào trong bản diễn giải của sách đặt ra nguyên tắc chi phối cả khoá học? (mục 1)
3. Kể ba bài toán. Sách nói bài toán nào quan trọng nhất, và dùng lập luận gì? (mục 2)
4. Sách nói kiếm tiền là trao đổi cái gì lấy tiền? Vì sao chữ đó quan trọng? (mục 2)
5. Kể bốn bước của một kế hoạch hoàn chỉnh. Bước nào bị khoá học cắt một phần, và vì sao? (mục 3)
6. **Bài toán nào trong ba bài toán không có bước nào của kế hoạch bốn bước?** Cấu trúc hai tập
   sách xác nhận điều đó ra sao? (mục 4)
7. Trong công thức $n = -\ln s / \ln(1+g)$, vì sao **thu nhập** không xuất hiện? Điều đó có nghĩa gì? (mục 5)
8. Sách hứa bao lâu ở C1 tr. 5, và bao lâu ở C2 tr. 15? Con số nào khớp với tỷ lệ tiết kiệm mà
   sách tự khuyên? (mục 5)
9. Muốn xong trong 5 năm thì phải để dành bao nhiêu phần trăm thu nhập? (mục 5)
10. Ba công thức phân bổ của sách để dành bao nhiêu phần trăm? Cả ba cho ra bao nhiêu năm? (mục 5)
11. Giữ nguyên tiết kiệm 20%, hạ lợi suất kỳ vọng từ 12% xuống 8% thì số năm thay đổi thế nào? (mục 5)
12. Câu nào của sách phát biểu ràng buộc thứ tự bằng ngôn ngữ logic? Ràng buộc đó nói gì? (mục 6)
13. Kể hai chỗ khác nơi sách nhắc lại cùng ràng buộc thứ tự đó. (mục 6)
14. Ngưỡng *"red flag"* của C2 tr. 19 là gì, và nó đặt trần nào lên tỷ lệ tiết kiệm? (mục 7)
15. Phát biểu *"tự do tài chính là kỹ năng có thể học được"* cần thêm điều kiện gì để đầy đủ? (mục 7)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 1 — TÀI CHÍNH CÁ NHÂN LÀ GÌ                     C1 tr. 4-6          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ĐỊNH NGHĨA   "những gì xoay quanh chủ đề tiền bạc của MỘT CÁ NHÂN       ║
║               CỤ THỂ"  => không lời khuyên nào đúng cho tất cả           ║
║                                                                          ║
║  BA BÀI TOÁN     kiếm tiền  ·  GIỮ TIỀN  ·  đầu tư tiền                  ║
║                  "tiền kiếm được không quan trọng bằng tiền giữ được"    ║
║                                                                          ║
║  BỐN BƯỚC     1 dòng tiền + tài sản      -> bài 2, 3, 4                  ║
║               2 hồ sơ rủi ro             -> bài 12                       ║
║               3 mục tiêu + kế hoạch      -> bài 14                       ║
║               4 đầu tư theo danh mục     -> bài 13                       ║
║                                                                          ║
║  BA BÀI TOÁN VÀ BỐN BƯỚC KHÔNG KHỚP                                     ║
║     bài toán KIẾM TIỀN không có bước nào — nó nằm ở Class 2 Unit 1,     ║
║     tức là NGOÀI kế hoạch bốn bước                                       ║
║                                                                          ║
║  THỨ TỰ CÓ RÀNG BUỘC   C1 tr.12: "KHI VÀ CHỈ KHI dòng tiền dương bạn    ║
║     mới nên nghĩ đến việc đầu tư dài hạn"  — ngôn ngữ logic, không       ║
║     phải lời khuyên mềm. Sai phổ biến nhất KHÔNG phải chọn sai cổ        ║
║     phiếu, mà là chọn cổ phiếu khi đáng lẽ đang phải trả nợ              ║
║                                                                          ║
║  BAO LÂU THÌ ĐẾN?      n = -ln(s) / ln(1+g)                              ║
║     THU NHẬP BIẾN MẤT khỏi công thức. Chỉ TỶ LỆ tiết kiệm mới đổi được  ║
║                                                                          ║
║     sách hứa  "5 năm"  (C1 tr.5)   ->  đòi để dành 68% thu nhập          ║
║     sách hứa  "20 năm" (C2 tr.15)  ->  đòi để dành 21%                   ║
║     sách KHUYÊN để dành 20%        ->  ra 20,9 năm   (cả 3 công thức)    ║
║     đọc chặt 6 jars, chỉ FFA 10%   ->  ra 29,9 năm                       ║
║     => khoảng thật: 21-30 NĂM, không phải 5                              ║
║                                                                          ║
║     nhạy với lợi suất: 12% -> 8% thì thời gian ĐÚNG GẤP ĐÔI (21 -> 41)   ║
║                                                                          ║
║  GIỚI HẠN   C2 tr.19 red flag: NEC > 80% thu nhập => s tối đa còn 20%,   ║
║     và đó là khi không tiêu gì khác. Dưới ngưỡng thu nhập ấy, s không    ║
║     còn nằm trong tay bạn => phải giải bài toán số một trước             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1***, Waka.vn. Tệp trong kho:
  `tai_lieu/Tài Chính Cá Nhân 101 - Class 1_ Lập Kế Hoạch Tài Chính Cá Nhân - Waka.pdf`.
  - **Unit 1 *Tài chính cá nhân là gì?* (tr. 4–6)** — nguồn chính của bài này: định nghĩa
    Wikipedia và bản diễn giải (tr. 4), ba bài toán (tr. 4–5), *"kỹ năng có thể học được"* và
    *"5 năm, 10 năm"* (tr. 5), bốn bước (tr. 5–6)
  - Unit 2 Lesson 3 (tr. 12) — *"khi và chỉ khi dòng tiền dương…"*
  - Unit 3 Lesson 1 (tr. 17) — mọi quyết định dựa trên bảng cân đối của riêng mình
  - Unit 3 Lesson 3 (tr. 20–21) — người nghiệp dư lao vào đỉnh; tháp xây *"dần từ đế lên"*
  - Unit 4 Lesson 2 (tr. 31) — công thức số tiền cần cho tự do tài chính với ví dụ 12% / 4%;
    và *"Không có lời khuyên nào đúng cho tất cả các trường hợp"*
  - Unit 4 Lesson 3 (tr. 32) — xác định mức chấp nhận rủi ro trước, chọn kênh sau
  - *Lời kết* (tr. 40) — *"Sang đến Class 2… giải 3 bài toán cụ thể"*
- ***Tài chính cá nhân 101 — Class 2***, Waka.vn. Tệp trong kho:
  `tai_lieu/Tài Chính Cá Nhân 101 - Class 2_ Nâng Cao Năng Lực Tài Chính Cá Nhân - Waka.pdf`.
  - Unit 1 Lesson 1 (tr. 5) — công thức thu nhập = giá trị × thời gian × quy mô
  - Unit 2 mở đầu (tr. 15) — *"sau vài năm (tối đa là 20 năm)"*
  - Unit 2 Lesson 2 (tr. 18, 21) — FFA 10%, LTSS 10%
  - Unit 2 Lesson 2 (tr. 19) — ngưỡng *"red flag"* NEC > 80%
  - Unit 2 Lesson 3 (tr. 23–24) — 50/30/20; trả nợ trước khi đầu tư
  - Unit 2 Lesson 4 (tr. 25) — 70/30
  - Unit 2 Lesson 5 (tr. 27) — *"không thể giảm chi tiêu được mãi"*
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-01-bao-lau-thi-den.py`](../thuc_hanh/bai-01-bao-lau-thi-den.py).
  Mọi con số ở mục 5 do tệp này tính, không gõ tay. Công thức đóng được kiểm chéo bằng mô phỏng
  tích luỹ từng năm.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Toàn bộ [mục 5](#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách) **không có
    trong sách**. Sách đưa công thức số tiền cần (C1 tr. 31) và các tỷ lệ phân bổ (C2 tr. 18–25)
    nhưng **chưa bao giờ ghép chúng lại** để ra số năm. Phép ghép, công thức
    $n = -\ln s/\ln(1+g)$, và mọi bảng số là của khoá học.
  - Nhận xét ở [mục 4](#4-ba-bài-toán-và-bốn-bước-không-khớp-nhau) rằng bài toán *kiếm tiền* không
    có bước nào là **quan sát của khoá học**; sách không nói điều này ra. Bằng chứng dẫn kèm
    (cấu trúc Class 2 và lời kết C1 tr. 40) thì là của sách.
  - Điều kiện bổ sung cho phát biểu *"kỹ năng có thể học được"* ở
    [mục 7](#7-bổ-sung-kỹ-năng-có-thể-học-được-đúng-đến-đâu) là lập luận của khoá học, dựng từ hai
    câu của sách (C1 tr. 5 và C2 tr. 19) đặt cạnh nhau.
- **Liên hệ chéo:**
  - Giá trị hiện tại, chuỗi tiền tệ và lãi kép — nền toán của mục 5:
    [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).
  - Lạm phát và lợi suất thực:
    [EG14 — Kinh tế vĩ mô](../../../houedu/eg14-kinhtevimo-macro/README.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| **1** | **Tài chính cá nhân là gì** ← *bạn đang ở đây* | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| 5 | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md) | C2 tr. 4–13 | 1 |
| 6 | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách | 1 |
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | [**[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai](bai_10_tai_chinh_hanh_vi.md) | ngoài sách | 2 |
| 11 | [Nhận diện lừa đảo: Ponzi và CFD](bai_11_nhan_dien_lua_dao.md) | C2 tr. 47–57 | 1 |
| 12 | [Rủi ro, khẩu vị rủi ro, phân bổ tài sản](bai_12_rui_ro_khau_vi_phan_bo.md) | C1 tr. 25–33 | 1 |
| 13 | [Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF](bai_13_kenh_dau_tu.md) | C2 tr. 58–67 | 2 |
| 14 | [Mục tiêu SMART và ráp lại thành kế hoạch](bai_14_muc_tieu_smart.md) | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
