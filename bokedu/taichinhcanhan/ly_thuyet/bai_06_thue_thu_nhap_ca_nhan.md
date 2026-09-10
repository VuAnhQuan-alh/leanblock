# Bài 6 — [bổ sung] Thuế thu nhập cá nhân: tiền thật về tay

> **Bài này không có trong sách.** Toàn bộ nội dung là **[bổ sung]** — hai tập *Tài chính cá nhân
> 101* dùng chữ *"thu nhập"* xuyên suốt mà chưa lần nào phân biệt **gộp** với **ròng**, trong khi cả
> ba công thức phân bổ ở C2 tr. 18–25 đều chia trên thu nhập ròng.
>
> **Cần đọc trước:** [Bài 5](bai_05_kiem_tien.md) — bài 5 nói về việc **kiếm** được bao nhiêu. Bài
> này nói về việc **giữ lại** được bao nhiêu trong số đó, trước khi bài 7 chia nó ra.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Mọi con số pháp lý trong bài đều tra từ văn bản, ngày 09/09/2026.** Nguồn ghi ở
> [mục 8](#8-nguồn-pháp-lý-và-hạn-dùng-của-bài-này) và trong chính code. Luật thuế đổi thường
> xuyên — **kiểm lại ngày tra trước khi tin con số**.
>
> **Code:** [`thuc_hanh/bai-06-thue-tncn.py`](../thuc_hanh/bai-06-thue-tncn.py)
> — mọi hằng số pháp lý gom trong một khối đầu tệp, kèm số hiệu văn bản. Luật đổi thì sửa đúng
> khối đó.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Vì sao bài này phải đứng trước bài 7](#1-vì-sao-bài-này-phải-đứng-trước-bài-7)
- [2. Ba bước từ lương gộp tới tiền về tay](#2-ba-bước-từ-lương-gộp-tới-tiền-về-tay)
- [3. Bảo hiểm bắt buộc, và cái bẫy hai trần](#3-bảo-hiểm-bắt-buộc-và-cái-bẫy-hai-trần)
- [4. Biểu thuế luỹ tiến từng phần — và chữ "từng phần" mới là chỗ quan trọng](#4-biểu-thuế-luỹ-tiến-từng-phần--và-chữ-từng-phần-mới-là-chỗ-quan-trọng)
- [5. Người phụ thuộc: đáng giá bao nhiêu, và vì sao không cố định](#5-người-phụ-thuộc-đáng-giá-bao-nhiêu-và-vì-sao-không-cố-định)
- [6. [bổ sung] Điều này đổi gì cho các bài trước](#6-bổ-sung-điều-này-đổi-gì-cho-các-bài-trước)
- [7. Ba chỗ bài này cố tình không đi sâu](#7-ba-chỗ-bài-này-cố-tình-không-đi-sâu)
- [8. Nguồn pháp lý, và hạn dùng của bài này](#8-nguồn-pháp-lý-và-hạn-dùng-của-bài-này)
- [9. Tự thử](#9-tự-thử)
- [10. Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
- [11. Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Vì sao bài này phải đứng trước bài 7

Sáu chiếc lọ của C2 tr. 18–22 chia thu nhập thành 10% FFA, 55% NEC, 10% EDU, 10% PLAY, 5% GIVE,
10% LTSS. Cộng lại đúng 100%.

Câu hỏi mà sách không đặt: **100% của cái gì?**

Với người làm công ăn lương, con số ghi trên hợp đồng và con số vào tài khoản là hai số khác nhau.
Ở mức lương 30 triệu, chúng cách nhau **3,79 triệu mỗi tháng**:

```
   lương gộp ghi trên hợp đồng               30,00tr
     − bảo hiểm bắt buộc (10,5%)             − 3,15tr
     − thuế thu nhập cá nhân                 − 0,64tr
   ────────────────────────────────────────────────
   = TIỀN VÀO TÀI KHOẢN                       26,21tr
```

Chia sáu chiếc lọ trên **gộp** thì tổng sáu lọ là 30 triệu, trong khi tài khoản chỉ có 26,21 triệu.
**Thiếu 3,79 triệu ngay từ ngày đầu tháng**, và cái lọ chịu trận là lọ lớn nhất:

| Lọ | Chia trên **gộp** | Chia trên **ròng** | Hụt |
| --- | ---: | ---: | ---: |
| FFA 10% | 3,00tr | 2,62tr | 0,38tr |
| **NEC 55%** | **16,50tr** | **14,42tr** | **2,08tr** |
| EDU 10% | 3,00tr | 2,62tr | 0,38tr |
| PLAY 10% | 3,00tr | 2,62tr | 0,38tr |
| GIVE 5% | 1,50tr | 1,31tr | 0,19tr |
| LTSS 10% | 3,00tr | 2,62tr | 0,38tr |

Riêng lọ NEC hụt **2,08 triệu/tháng**, tức **24,98 triệu/năm**. Người áp dụng 6 jars trên lương gộp
sẽ thấy chi phí thiết yếu tháng nào cũng "vỡ" mà không hiểu vì sao — trong khi lỗi không nằm ở chi
tiêu, nó nằm ở mẫu số.

Và khoảng cách ấy **rộng ra theo thu nhập**:

| Lương gộp | Về tay | Mất |
| ---: | ---: | ---: |
| 20tr | 17,78tr | 11,1% |
| 30tr | 26,21tr | 12,6% |
| 50tr | 42,33tr | 15,3% |

Nên quy tắc của cả khoá học, và nó dùng cho mọi công thức phân bổ ở bài 7:

> **Mọi tỷ lệ phần trăm đều chia trên số tiền THẬT SỰ VÀO TÀI KHOẢN, không phải con số trên hợp
> đồng lao động.**

---

## 2. Ba bước từ lương gộp tới tiền về tay

```
   LƯƠNG GỘP
      │
      ├─── (1) BẢO HIỂM BẮT BUỘC              10,5% phần người lao động
      │         8% hưu trí · 1,5% BHYT · 1% BHTN
      │         hai TRẦN khác nhau — mục 3
      │
      ├─── (2) GIẢM TRỪ GIA CẢNH              15,5tr bản thân
      │         + 6,2tr mỗi người phụ thuộc
      │         => còn lại là THU NHẬP TÍNH THUẾ
      │
      ├─── (3) THUẾ LUỸ TIẾN TỪNG PHẦN        5 bậc, 5% → 35%
      │
      ▼
   TIỀN VỀ TAY
```

Ba bước này **theo đúng thứ tự đó**, và thứ tự quan trọng: bảo hiểm được trừ **trước** khi tính
thuế, nên tiền đóng bảo hiểm không bị đánh thuế.

### Bảng đầy đủ

| Lương gộp | Bảo hiểm | Giảm trừ | Thu nhập tính thuế | Thuế | **Về tay** | Giữ được |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10,00tr | 1,05tr | 15,50tr | 0 | **0** | 8,95tr | 89,5% |
| 15,00tr | 1,57tr | 15,50tr | 0 | **0** | 13,43tr | 89,5% |
| 17,00tr | 1,78tr | 15,50tr | 0 | **0** | 15,21tr | 89,5% |
| 20,00tr | 2,10tr | 15,50tr | 2,40tr | 0,12tr | 17,78tr | 88,9% |
| 25,00tr | 2,62tr | 15,50tr | 6,88tr | 0,34tr | 22,03tr | 88,1% |
| 30,00tr | 3,15tr | 15,50tr | 11,35tr | 0,64tr | 26,21tr | 87,4% |
| 40,00tr | 4,20tr | 15,50tr | 20,30tr | 1,53tr | 34,27tr | 85,7% |
| 50,00tr | 5,25tr | 15,50tr | 29,25tr | 2,42tr | 42,33tr | 84,7% |
| 60,00tr | 5,41tr | 15,50tr | 39,09tr | 4,32tr | 50,27tr | 83,8% |
| 80,00tr | 5,61tr | 15,50tr | 58,89tr | 8,28tr | 66,11tr | 82,6% |
| 100,00tr | 5,81tr | 15,50tr | 78,69tr | 14,11tr | 80,09tr | 80,1% |
| 150,00tr | 5,87tr | 15,50tr | 128,63tr | 30,52tr | 113,61tr | 75,7% |

Để ý cột **bảo hiểm**: nó tăng đều tới mức 50tr rồi gần như đứng lại — đó là trần ở mục 3.

### Ngưỡng bắt đầu nộp thuế

Dưới trần bảo hiểm, thu nhập tính thuế $= G - 0{,}105G - \text{giảm trừ} = 0{,}895G - \text{giảm trừ}$,
nên ngưỡng là $\text{giảm trừ} \div 0{,}895$:

| Số người phụ thuộc | Tổng giảm trừ | **Lương gộp dưới mức này thì không nộp một đồng thuế nào** |
| :---: | ---: | ---: |
| 0 | 15,50tr | **17,32tr** |
| 1 | 21,70tr | **24,25tr** |
| 2 | 27,90tr | **31,17tr** |
| 3 | 34,10tr | **38,10tr** |

---

## 3. Bảo hiểm bắt buộc, và cái bẫy hai trần

Phần người lao động đóng là **10,5%**, chia làm ba quỹ:

| Quỹ | Tỷ lệ | Trần tính đóng |
| --- | ---: | --- |
| Hưu trí (BHXH) | 8% | 20 × mức tham chiếu = **50,6tr** |
| Y tế (BHYT) | 1,5% | 20 × mức tham chiếu = **50,6tr** |
| Thất nghiệp (BHTN) | 1% | 20 × **lương tối thiểu vùng** = **106,2tr** (vùng I) |

**Hai mẫu số khác nhau.** Đây là chỗ dễ nhầm nhất của cả bài, và nó có hệ quả thấy được ngay trong
bảng ở mục 2: từ mức 50tr trở lên, cột bảo hiểm gần như không tăng nữa — 9,5% đã chạm trần, chỉ còn
1% BHTN bò tiếp tới 106,2tr.

```
   lương 50tr   ->  bảo hiểm 5,25tr   (10,5% × 50,0tr, chưa chạm trần nào)
   lương 60tr   ->  bảo hiểm 5,41tr   (9,5% × 50,6tr  +  1% × 60,0tr)
   lương 150tr  ->  bảo hiểm 5,87tr   (9,5% × 50,6tr  +  1% × 106,2tr — cả hai trần)
```

Lương gấp ba mà tiền bảo hiểm chỉ tăng 12%. Điều đó cũng có nghĩa: **phần vượt trần không đóng bảo
hiểm nhưng vẫn chịu thuế đầy đủ.**

Hệ quả thực tế cho kế hoạch hưu trí: lương hưu sau này tính trên phần đã đóng, mà phần đã đóng bị
chặn ở 50,6tr. Người lương 150tr **không** có lương hưu gấp ba người lương 50tr. Chênh lệch đó phải
tự bù bằng lọ FFA của bài 7 — đây là một lý do rất cụ thể để lọ ấy tồn tại.

---

## 4. Biểu thuế luỹ tiến từng phần — và chữ "từng phần" mới là chỗ quan trọng

Từ **kỳ tính thuế 2026**, biểu thuế rút từ 7 bậc xuống **5 bậc**:

| Bậc | Thu nhập **tính thuế**/tháng | Thuế suất |
| :---: | --- | ---: |
| 1 | đến 10tr | **5%** |
| 2 | trên 10tr đến 30tr | **10%** |
| 3 | trên 30tr đến 60tr | **20%** |
| 4 | trên 60tr đến 100tr | **30%** |
| 5 | trên 100tr | **35%** |

### Hiểu lầm phổ biến nhất về thuế

> *"Lương tôi nhảy lên bậc trên, thế là đóng thuế nhiều hơn cả phần tăng."*

**Không bao giờ xảy ra.** Chữ **"từng phần"** trong *"luỹ tiến từng phần"* nghĩa là mỗi bậc chỉ đánh
vào **phần thu nhập nằm trong bậc đó**, không phải toàn bộ.

Ví dụ với lương gộp 30tr, thu nhập tính thuế **11,35tr**:

```
   10,00tr đầu tiên   × 5%   =  500.000        <- bậc 1
    1,35tr tiếp theo  × 10%  =  135.000        <- bậc 2, CHỈ phần vượt 10tr
   ─────────────────────────────────────
   tổng thuế                  =  635.000
```

Không phải $11{,}35 \times 10\% = 1{,}135$ triệu. Phần 10 triệu đầu vẫn hưởng thuế suất 5% dù bạn
kiếm bao nhiêu đi nữa.

Bảng ở mục 2 chứng minh điều đó: cột *"giữ được"* giảm **đều và liên tục** từ 89,5% xuống 75,7%,
không có bậc thang, không có chỗ nào tụt đột ngột. **Tăng lương luôn làm tăng tiền về tay.**

### [2026] Luật mới bớt được bao nhiêu

Luật cũ có 7 bậc, giảm trừ 11tr + 4,4tr. Luật mới có 5 bậc, giảm trừ 15,5tr + 6,2tr. So sánh trực
tiếp trên cùng một mức lương:

| Lương gộp | Thuế theo luật **cũ** | Thuế theo luật **mới** | Bớt được | Mỗi năm |
| ---: | ---: | ---: | ---: | ---: |
| 15tr | 0,12tr | **0** | 0,12tr | 1,46tr |
| 20tr | 0,44tr | 0,12tr | 0,32tr | 3,84tr |
| 30tr | 1,63tr | 0,64tr | 0,99tr | **11,91tr** |
| 50tr | 5,19tr | 2,42tr | 2,76tr | 33,15tr |
| 80tr | 13,17tr | 8,28tr | 4,89tr | 58,67tr |
| 150tr | 36,75tr | 30,52tr | 6,22tr | 74,70tr |

Không mức nào phải nộp nhiều hơn trước. Nhóm lương phổ thông hưởng lợi nhiều nhất **theo tỷ lệ** —
vừa được nâng giảm trừ, vừa được giãn bậc 1 từ 5tr lên 10tr, vừa được hạ hai bậc giữa
(15% → 10% và 25% → 20%).

Người lương 30 triệu bớt được gần **12 triệu một năm**. Con số đó lớn hơn cả lọ FFA của họ trong ba
tháng — đáng để không bỏ qua khi lập kế hoạch năm nay.

---

## 5. Người phụ thuộc: đáng giá bao nhiêu, và vì sao không cố định

| Lương gộp | 0 phụ thuộc | 1 phụ thuộc | 2 phụ thuộc | Thêm 1 người |
| ---: | ---: | ---: | ---: | ---: |
| 20tr | 17,78tr | 17,90tr | 17,90tr | **+0,12tr** |
| 30tr | 26,21tr | 26,59tr | 26,85tr | +0,38tr |
| 50tr | 42,33tr | 42,95tr | 43,56tr | +0,62tr |
| 80tr | 66,11tr | 67,35tr | 68,59tr | **+1,24tr** |

Cùng một người phụ thuộc, cùng mức giảm trừ 6,2 triệu — mà giá trị chênh nhau **hơn mười lần** giữa
người lương 20tr và người lương 80tr. Lý do:

> Giá trị của một người phụ thuộc = **phần thu nhập tính thuế được cắt bỏ** × **thuế suất biên**

| Lương gộp | Thu nhập tính thuế | Phần cắt được | Thuế suất biên | Lợi |
| ---: | ---: | ---: | :---: | ---: |
| 20tr | 2,40tr | **2,40tr** (chạm đáy) | 5% | 0,12tr |
| 50tr | 29,25tr | 6,20tr | 10% | 0,62tr |
| 80tr | 58,89tr | 6,20tr | 20% | 1,24tr |

Ba trường hợp, ba cơ chế khác nhau:

- **Lương 20tr** — thu nhập tính thuế chỉ 2,4tr, **nhỏ hơn cả mức giảm trừ 6,2tr**. Khai một người
  phụ thuộc là thuế về 0, và khai **người thứ hai không đem lại thêm một đồng nào**. Giảm trừ không
  hoàn lại tiền; nó chỉ xoá phần thuế bạn đang phải nộp.
- **Lương 50tr** — phần cắt nằm gọn trong bậc 10%.
- **Lương 80tr** — phần cắt nằm trong bậc 20%, nên đáng gấp đôi.

Giảm trừ luôn cắt vào phần thu nhập ở **bậc cao nhất** bạn đang chịu. Đó cũng là lý do một khoản
giảm trừ bất kỳ luôn có giá trị lớn hơn với người thu nhập cao.

---

## 6. [bổ sung] Điều này đổi gì cho các bài trước

Bài này không chỉ sửa mẫu số cho bài 7. Nó chạm vào ba con số đã dùng ở các bài trước.

**Bài 1 — số năm tới tự do tài chính.** Công thức
$n = -\ln s / \ln(1+g)$ ở [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách)
dùng $s$ là tỷ lệ tiết kiệm. Nếu bạn tính $s$ trên lương gộp, bạn đang lạc quan hơn thực tế: người
"tiết kiệm 20% lương gộp 30tr" thật ra đang để dành 6tr trên **26,21tr** về tay, tức **22,9%** thu
nhập thật — nhưng chi tiêu của họ cũng đo trên tiền thật. Cả tử số lẫn mẫu số phải cùng một loại.

**Bài 2 — dòng tiền.** Danh sách thu nhập ở C1 tr. 11 ghi *"lương, thưởng, phụ cấp"*. Con số điền
vào phải là **tiền vào tài khoản**, không phải con số trên hợp đồng. Sổ ghi chép của
[bài 3](bai_03_ghi_chep_chi_tieu.md) tự nhiên đã đúng — nó ghi tiền thật — nên nếu hai con số của
bạn lệch nhau, gần như chắc chắn là bảng lương đang dùng số gộp.

**Bài 5 — vốn con người.** Phép định giá của C1 tr. 22–23 chia **thu nhập năm** cho lãi suất. Dùng
thu nhập gộp thì "tài sản vô hình" của bạn phồng lên khoảng 12–15% so với dùng thu nhập ròng. Không
sai hẳn — tuỳ bạn muốn định giá *cái bạn tạo ra* hay *cái bạn nhận được* — nhưng phải nói rõ đang
dùng cái nào, và giữ nguyên nó khi so hai năm.

---

## 7. Ba chỗ bài này cố tình không đi sâu

Đây là bài **[bổ sung]**, và phạm vi của nó chỉ là: đủ để bài 7 có mẫu số đúng. Ba mảng liên quan
nằm ngoài phạm vi, ghi ra để bạn biết chúng tồn tại:

| Mảng | Vì sao không làm ở đây |
| --- | --- |
| **Quyết toán thuế** cuối năm, hoàn thuế, tự quyết toán hay uỷ quyền | Là thủ tục, không phải cơ chế. Nhưng đáng nhớ một điều: nếu thu nhập của bạn dao động trong năm, phần bị tạm khấu trừ có thể **nhiều hơn** số phải nộp — và bạn phải tự đi đòi lại. |
| **Thu nhập ngoài lương** — cho thuê nhà, cổ tức, chuyển nhượng chứng khoán, hộ kinh doanh | Mỗi loại một cách tính riêng, không dùng biểu luỹ tiến ở mục 4. Bài 13 chạm tới khi nói về từng kênh đầu tư. |
| **Lương hưu và chế độ BHXH** | Bài này chỉ tính phần *đóng*. Phần *hưởng* là một chủ đề riêng, và [bài 0](bai_00_bat_dau_tu_dau.md#5-hai-mảng-bổ-sung-và-phần-đã-cắt) đã ghi rõ khoá học không mở nó. |

---

## 8. Nguồn pháp lý, và hạn dùng của bài này

Mọi con số ở trên tra ngày **09/09/2026**. Chúng nằm gọn trong một khối ở đầu tệp code, kèm số hiệu
văn bản, để khi luật đổi thì chỉ phải sửa một chỗ.

| Con số | Văn bản | Hiệu lực |
| --- | --- | --- |
| Giảm trừ **15,5tr** bản thân, **6,2tr** mỗi người phụ thuộc | **Nghị quyết 110/2025/UBTVQH15** | từ **kỳ tính thuế 2026** |
| Biểu thuế **5 bậc** (5/10/20/30/35%) | **Luật Thuế TNCN số 109/2025/QH15**, Điều 9 — Quốc hội thông qua 10/12/2025 | luật có hiệu lực **01/7/2026**; riêng phần tiền lương áp dụng **từ kỳ tính thuế 2026** |
| Người lao động đóng **10,5%** (8% + 1,5% + 1%) | Luật BHXH 2024 (Đ.33–34), Luật Việc làm 2025 (Đ.33), NĐ 188/2025/NĐ-CP | 2026 |
| Trần BHXH/BHYT = **20 × mức tham chiếu** | Luật BHXH 2024, điểm đ khoản 1 Điều 31 | — |
| Mức tham chiếu **2,53tr** (⟹ trần **50,6tr**) | NĐ 161/2026/NĐ-CP | **từ 01/7/2026**; trước đó là 2,34tr ⟹ trần 46,8tr |
| Trần BHTN = **20 × lương tối thiểu vùng** | Luật Việc làm 2025 | từ 01/01/2026 |
| Lương tối thiểu vùng I **5,31tr** (⟹ trần BHTN **106,2tr**) | **NĐ 293/2025/NĐ-CP** ngày 10/11/2025 | từ 01/01/2026 |

Ba mức vùng còn lại theo NĐ 293/2025: vùng II **4,73tr**, vùng III **4,14tr**, vùng IV **3,70tr**.

> **Một chỗ tinh tế của riêng năm 2026.** Mức tham chiếu đổi **giữa năm**: 2,34tr tới 30/6, rồi
> 2,53tr từ 01/7. Nên trần bảo hiểm nửa đầu năm là **46,8tr**, nửa sau là **50,6tr**. Bài này và
> code dùng mốc **sau** — đúng cho thời điểm đọc, nhưng nếu bạn quyết toán cả năm 2026 thì hai nửa
> năm phải tính riêng.

> **Hạn dùng.** Luật thuế và mức lương cơ sở đổi gần như hằng năm. Trước khi dùng con số nào
> trong bài cho quyết định thật, hãy tra lại văn bản gốc — đúng tinh thần *"tra ngược về đâu?"* mà
> [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#1-định-nghĩa-của-sách-và-một-chỗ-không-kiểm-chứng-được)
> đã đặt ra khi bàn về cách sách trích Wikipedia.

---

## 9. Tự thử

1. **Tính tiền về tay của bạn.** Lấy lương gộp trên hợp đồng, số người phụ thuộc đang khai. Chạy
   `bai-06-thue-tncn.py` sau khi thêm mức lương của bạn vào bảng ở mục 1. Con số ra có khớp với
   tiền thật vào tài khoản không? Nếu lệch, phần lệch có thể là phụ cấp không tính thuế, thưởng,
   hay công đoàn phí.

2. **Sáu chiếc lọ, đúng mẫu số.** Chia sáu chiếc lọ trên tiền về tay của bạn. So với cách bạn đang
   làm. Lọ NEC chênh bao nhiêu một năm?

3. **Ngưỡng của bạn.** Bạn cách ngưỡng nộp thuế ở mục 2 bao xa? Nếu khai thêm một người phụ thuộc
   hợp lệ, thuế của bạn giảm bao nhiêu — và con số đó bằng bao nhiêu phần trăm của 6,2 triệu?

4. **Kiểm hiểu lầm về bậc thuế.** Trong code, tính tiền về tay ở lương gộp **59,9tr** và **60,1tr**
   (hai bên ranh giới bậc 3 và bậc 4 của thu nhập tính thuế thì ở mức lương nào?). Tiền về tay có
   **tụt** khi vượt ranh giới không? Vì sao?

5. **Đổi vùng.** Trong code, đổi `LUONG_TOI_THIEU_VUNG_I` sang mức vùng IV (3,70tr). Trần BHTN đổi
   thế nào? Ở mức lương nào thì thay đổi ấy bắt đầu ảnh hưởng tới tiền về tay?

6. **Nửa đầu năm 2026.** Đổi `MUC_THAM_CHIEU` từ `2_530_000` xuống `2_340_000`. Ở mức lương 80tr,
   tiền về tay nửa đầu năm khác nửa sau bao nhiêu? Ai được lợi khi trần bảo hiểm **tăng**?

7. **Nối với bài 5.** Người "thu nhập tăng dần" ở
   [bài 5](bai_05_kiem_tien.md#9-đính-chính-không-có-mô-hình-nào-lợi-thế-hơn--lãi-kép-nói-khác)
   cần tiết kiệm 35% để đuổi kịp. Nếu con số 35% ấy tính trên **gộp**, thì tính trên **ròng** nó
   phải là bao nhiêu?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Lương gộp | gross salary | con số trên hợp đồng, trước bảo hiểm và thuế |
| Tiền về tay · lương ròng | net salary · take-home pay | tiền thật vào tài khoản — **mẫu số của mọi tỷ lệ ở bài 7** |
| Bảo hiểm bắt buộc | mandatory social insurance | 10,5% phần người lao động: 8% hưu trí + 1,5% y tế + 1% thất nghiệp |
| Giảm trừ gia cảnh | personal & dependant allowance | 15,5tr bản thân + 6,2tr mỗi người phụ thuộc |
| Thu nhập tính thuế | taxable income | lương gộp − bảo hiểm − giảm trừ; **không phải** lương gộp |
| Luỹ tiến **từng phần** | progressive, **marginal** brackets | mỗi bậc chỉ đánh vào **phần** thu nhập nằm trong bậc đó |
| Thuế suất biên | marginal tax rate | thuế suất của bậc cao nhất bạn đang chạm tới |
| Thuế suất hiệu dụng | effective tax rate | tổng thuế ÷ thu nhập; **luôn thấp hơn** thuế suất biên |
| Mức tham chiếu | reference level | mẫu số của trần BHXH/BHYT; bằng lương cơ sở khi chưa bãi bỏ |
| Trần đóng | contribution ceiling | mức lương tối đa dùng để tính đóng; **hai trần khác nhau** cho hai nhóm quỹ |

---

## 11. Câu hỏi tự kiểm tra

1. Sáu chiếc lọ chia trên gộp hay trên ròng? Ở lương 30tr, tổng sáu lọ chia trên gộp **thiếu** bao
   nhiêu so với tiền thật có? (mục 1)
2. Lọ nào chịu trận nặng nhất khi chia sai mẫu số, và hụt bao nhiêu một năm ở mức 30tr? (mục 1)
3. Kể ba bước từ lương gộp tới tiền về tay, **theo đúng thứ tự**. Vì sao thứ tự quan trọng? (mục 2)
4. Người không có người phụ thuộc bắt đầu nộp thuế từ mức lương gộp nào? Có hai người phụ thuộc
   thì sao? (mục 2)
5. Ba quỹ bảo hiểm có **mấy** trần khác nhau? Mẫu số của mỗi trần là gì? (mục 3)
6. Vì sao người lương 150tr đóng bảo hiểm gần bằng người lương 60tr? Điều đó có nghĩa gì với
   lương hưu của họ? (mục 3)
7. Kể năm bậc của biểu thuế mới kèm thuế suất. (mục 4)
8. *"Tăng lương lên bậc trên thì đóng thuế nhiều hơn cả phần tăng"* — đúng hay sai, và **vì sao**?
   Chữ nào trong *"luỹ tiến từng phần"* trả lời câu này? (mục 4)
9. Lương gộp 30tr, thu nhập tính thuế 11,35tr. Tính thuế bằng tay, ghi rõ từng bậc. (mục 4)
10. Luật mới so với luật cũ: người lương 30tr bớt được bao nhiêu một năm? Ba thay đổi nào tạo ra
    khoản đó? (mục 4)
11. Vì sao một người phụ thuộc đáng 0,12tr với người lương 20tr nhưng đáng 1,24tr với người lương
    80tr? (mục 5)
12. Người lương 20tr khai **người phụ thuộc thứ hai** thì được thêm bao nhiêu? Vì sao? (mục 5)
13. Nếu bạn tính tỷ lệ tiết kiệm trên lương gộp thay vì trên tiền về tay, bạn đang lạc quan hay
    bi quan hơn thực tế? (mục 6)
14. Năm 2026 có một chỗ tinh tế về trần bảo hiểm. Đó là gì, và nó ảnh hưởng tới việc quyết toán
    cả năm ra sao? (mục 8)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 6 — THUẾ THU NHẬP CÁ NHÂN            [bổ sung] — KHÔNG có trong sách║
║                                            số liệu tra ngày 09/09/2026   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  VÌ SAO BÀI NÀY ĐỨNG TRƯỚC BÀI 7                                        ║
║     6 jars chia 100% — nhưng 100% CỦA CÁI GÌ?                           ║
║     lương gộp 30tr  −3,15tr bảo hiểm  −0,64tr thuế  =  26,21tr về tay   ║
║     chia trên GỘP thì tổng sáu lọ 30tr mà tài khoản chỉ có 26,21tr       ║
║     riêng lọ NEC hụt 2,08tr/tháng = 24,98tr/NĂM                          ║
║     => MỌI TỶ LỆ CHIA TRÊN TIỀN THẬT VÀO TÀI KHOẢN                      ║
║                                                                          ║
║  BA BƯỚC   gộp → −bảo hiểm 10,5% → −giảm trừ → thuế luỹ tiến → về tay   ║
║     bảo hiểm trừ TRƯỚC thuế, nên tiền đóng bảo hiểm không bị đánh thuế  ║
║                                                                          ║
║  GIẢM TRỪ GIA CẢNH   15,5tr bản thân · 6,2tr mỗi người phụ thuộc        ║
║     ngưỡng chưa phải nộp thuế:  0 phụ thuộc 17,32tr · 1 người 24,25tr   ║
║                                 2 người 31,17tr · 3 người 38,10tr       ║
║                                                                          ║
║  BẢO HIỂM: HAI TRẦN KHÁC NHAU  <- chỗ dễ nhầm nhất                      ║
║     BHXH 8% + BHYT 1,5%  ->  trần 20 × MỨC THAM CHIẾU     =  50,6tr     ║
║     BHTN 1%              ->  trần 20 × LƯƠNG TT VÙNG      = 106,2tr     ║
║     lương 50tr → BH 5,25tr ;  lương 150tr → BH chỉ 5,87tr               ║
║     phần vượt trần KHÔNG đóng bảo hiểm nhưng VẪN chịu thuế đủ           ║
║                                                                          ║
║  BIỂU THUẾ 5 BẬC (từ kỳ tính thuế 2026, Luật 109/2025/QH15)             ║
║     ≤10tr 5% · 10-30tr 10% · 30-60tr 20% · 60-100tr 30% · >100tr 35%    ║
║     (áp trên THU NHẬP TÍNH THUẾ, không phải lương gộp)                  ║
║                                                                          ║
║  "TỪNG PHẦN" LÀ CHỖ QUAN TRỌNG                                          ║
║     lương 30tr, TNTT 11,35tr:  10tr × 5% + 1,35tr × 10% = 635.000       ║
║     KHÔNG phải 11,35tr × 10%                                            ║
║     => TĂNG LƯƠNG LUÔN LÀM TĂNG TIỀN VỀ TAY. Không có bậc thang.        ║
║     cột "giữ được" giảm mượt: 89,5% (10tr) → 75,7% (150tr)              ║
║                                                                          ║
║  LUẬT MỚI 2026 BỚT ĐƯỢC   lương 30tr: 11,91tr/năm · 50tr: 33,15tr/năm   ║
║     ba thay đổi: giảm trừ 11→15,5tr · bậc 1 nới 5→10tr · 15%→10%,25%→20%║
║                                                                          ║
║  NGƯỜI PHỤ THUỘC KHÔNG CÓ GIÁ CỐ ĐỊNH                                   ║
║     giá trị = phần TNTT cắt được × THUẾ SUẤT BIÊN                       ║
║     lương 20tr: TNTT 2,4tr < 6,2tr → chạm đáy, người THỨ HAI = 0 đồng   ║
║     lương 50tr: bậc 10% → 0,62tr/tháng                                  ║
║     lương 80tr: bậc 20% → 1,24tr/tháng, GẤP ĐÔI                         ║
║                                                                          ║
║  RIÊNG 2026: mức tham chiếu đổi GIỮA NĂM 2,34 -> 2,53tr (từ 01/7)       ║
║     trần bảo hiểm nửa đầu 46,8tr, nửa sau 50,6tr — quyết toán tách đôi  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

**Bài này không dựa trên *Tài chính cá nhân 101*.** Sách không có nội dung về thuế. Mọi con số pháp
lý tra từ các văn bản dưới đây, ngày **09/09/2026**:

- **Luật Thuế thu nhập cá nhân số 109/2025/QH15** — Quốc hội khoá XV thông qua ngày 10/12/2025.
  Điều 9: biểu thuế luỹ tiến từng phần 5 bậc. Hiệu lực 01/7/2026; riêng quy định về thu nhập từ
  tiền lương, tiền công của cá nhân cư trú áp dụng **từ kỳ tính thuế năm 2026**.
- **Nghị quyết 110/2025/UBTVQH15** — mức giảm trừ gia cảnh 15,5 triệu đồng/tháng cho bản thân người
  nộp thuế và 6,2 triệu đồng/tháng cho mỗi người phụ thuộc, từ kỳ tính thuế năm 2026.
- **Luật Bảo hiểm xã hội 2024**, Điều 31 (điểm đ khoản 1), Điều 33–34 — tỷ lệ đóng và trần bằng
  20 lần mức tham chiếu.
- **Luật Việc làm 2025**, Điều 33 — trần đóng bảo hiểm thất nghiệp bằng 20 lần mức lương tối thiểu
  vùng, áp dụng từ 01/01/2026.
- **Nghị định 188/2025/NĐ-CP** và **Nghị định 158/2025/NĐ-CP** — mức đóng chi tiết.
- **Nghị định 293/2025/NĐ-CP** ngày 10/11/2025 — mức lương tối thiểu vùng từ 01/01/2026:
  vùng I 5.310.000đ, vùng II 4.730.000đ, vùng III 4.140.000đ, vùng IV 3.700.000đ.
- **Nghị định 161/2026/NĐ-CP** — mức lương cơ sở 2.530.000đ từ 01/7/2026, kéo theo mức tham chiếu.
- **Luật Thuế thu nhập cá nhân 2007**, Điều 22 và **Nghị quyết 954/2020/UBTVQH14** — biểu 7 bậc và
  mức giảm trừ 11 triệu / 4,4 triệu, giữ lại **chỉ để đối chiếu** ở mục 4.

Các trang tra cứu đã dùng để xác định số hiệu văn bản và con số:
[Biểu thuế 5 bậc từ kỳ tính thuế 2026 — LuatVietnam](https://luatvietnam.vn/tin-van-ban-moi/ap-dung-bieu-thue-luy-tien-5-bac-tu-ky-tinh-thue-2026-186-106263-article.html) ·
[Biểu thuế 7 bậc xuống 5 bậc — MeInvoice](https://www.meinvoice.vn/tin-tuc/37299/bieu-thue-thue-tncn-tu-7-bac-xuong-5-bac/) ·
[Mức giảm trừ gia cảnh mới 2026 — Thư viện Pháp luật](https://thuvienphapluat.vn/phap-luat-doanh-nghiep/bai-viet/muc-giam-tru-gia-canh-moi-2026-va-cach-tinh-18704.html) ·
[Tỷ lệ đóng BHXH, BHYT, BHTN năm 2026 — Thư viện Pháp luật](https://thuvienphapluat.vn/phap-luat/ty-le-dong-bhxh-bat-buoc-bhyt-bhtn-nam-2026-cu-the-ra-sao-muc-dong-bhxh-toi-da-nam-2026-la-bao-nhie-951895-249767.html) ·
[Mức tham chiếu và trần đóng 2026 — LuatVietnam](https://luatvietnam.vn/bao-hiem/tu-2026-muc-dong-bhxh-bhyt-bhtn-cua-nld-va-nsdld-duoc-tinh-nhu-the-nao-563-106906-article.html) ·
[Lương tối thiểu vùng từ 01/01/2026 — Cổng Xây dựng chính sách, Chính phủ](https://xaydungchinhsach.chinhphu.vn/tu-1-1-2026-muc-luong-toi-thieu-duoc-tang-bao-nhieu-119251111091442629.htm)

- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-06-thue-tncn.py`](../thuc_hanh/bai-06-thue-tncn.py).
  Mọi bảng trong bài do tệp này tính. Tệp tự kiểm một trường hợp bằng tay từng bậc (lương gộp 30tr),
  và kiểm ngưỡng nộp thuế bằng cách thử hai bên ranh giới.
- **Liên hệ chéo:**
  - Ba công thức phân bổ thu nhập cần mẫu số của bài này: **bài 7**.
  - Tỷ lệ tiết kiệm và số năm tới tự do tài chính:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Dòng tiền và việc điền số nào vào bảng thu nhập:
    [bài 2 mục 2](bai_02_do_hien_trang.md#2-dòng-tiền--bước-1-của-sách).
  - Định giá vốn con người bằng thu nhập năm:
    [bài 5 mục 7](bai_05_kiem_tien.md#7-bổ-sung-cả-kế-hoạch-tài-chính-là-một-phép-chuyển-đổi).
  - Thuế ở tầm doanh nghiệp và chỗ nó nằm trên báo cáo kết quả kinh doanh:
    [Trí tuệ tài chính bài 3](../../trituetaichinh/ly_thuyet/bai_03_chi_phi_va_cac_tang_loi_nhuan.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| 5 | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md) | C2 tr. 4–13 | 1 |
| **6** | ****[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay** ← *bạn đang ở đây* | ngoài sách | 1 |
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | **[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai | ngoài sách | 2 |
| 11 | Nhận diện lừa đảo: Ponzi và CFD | C2 tr. 47–57 | 1 |
| 12 | Rủi ro, khẩu vị rủi ro, phân bổ tài sản | C1 tr. 25–33 | 1 |
| 13 | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
