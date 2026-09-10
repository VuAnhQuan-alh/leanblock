# Bài 8 — Vay, lãi suất thật, trả nợ

> Bài học dựa trên **C2 tr. 29–38** — Unit 3 của *Tài chính cá nhân 101, Class 2*.
>
> **Cần đọc trước:** [Bài 7](bai_07_phan_bo_thu_nhap.md) — bài 7 kết thúc với **13 triệu phải vay
> ở tháng Tết** và sáu chiếc lọ không có lọ nào để trả. Bài này trả lời chỗ đó.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Về phần pháp lý:** mục 3 dẫn văn bản luật, tra ngày **09/09/2026**. Luật đổi thì con số đổi —
> kiểm lại ngày tra trước khi tin.
>
> **Code:** [`thuc_hanh/bai-08-vay-va-tra-no.py`](../thuc_hanh/bai-08-vay-va-tra-no.py)
> — mọi lãi suất trong bài đều tính lại từ **dòng tiền** bằng cách giải IRR, không tin con số ai
> nói, kể cả con số của sách.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Unit này khác hẳn phần còn lại của sách](#1-unit-này-khác-hẳn-phần-còn-lại-của-sách)
- [2. Đòn bẩy: sách cho hai điểm, công thức cho cả đường](#2-đòn-bẩy-sách-cho-hai-điểm-công-thức-cho-cả-đường)
- [3. Trần 20%/năm ở tr. 31 không phải lời khuyên — đó là luật](#3-trần-20năm-ở-tr-31-không-phải-lời-khuyên--đó-là-luật)
- [4. Bài toán mảnh đất: cùng một khoản lãi, khi thì lãi khi thì lỗ](#4-bài-toán-mảnh-đất-cùng-một-khoản-lãi-khi-thì-lãi-khi-thì-lỗ)
- [5. Bốn phương án của chị B — phần hay nhất của Unit](#5-bốn-phương-án-của-chị-b--phần-hay-nhất-của-unit)
- [6. [đính chính] Phương án 4: sách nói 11 tháng](#6-đính-chính-phương-án-4-sách-nói-11-tháng)
- [7. [bổ sung] Cái tên sách không gọi: lãi trên dư nợ gốc](#7-bổ-sung-cái-tên-sách-không-gọi-lãi-trên-dư-nợ-gốc)
- [8. Snowball và Avalanche](#8-snowball-và-avalanche)
- [9. [bổ sung] Khoản 13 triệu của bài 7: trả nợ hay bỏ vào FFA?](#9-bổ-sung-khoản-13-triệu-của-bài-7-trả-nợ-hay-bỏ-vào-ffa)
- [10. Bốn câu hỏi cần hỏi trước khi ký](#10-bốn-câu-hỏi-cần-hỏi-trước-khi-ký)
- [11. Tự thử](#11-tự-thử)
- [12. Từ điển thuật ngữ](#12-từ-điển-thuật-ngữ)
- [13. Câu hỏi tự kiểm tra](#13-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Unit này khác hẳn phần còn lại của sách

Bảy bài trước, sách nói bằng nguyên tắc. Unit 3 nói bằng số học, và đó là Unit tốt nhất của cả hai
tập: nó có bốn phép tính kiểm được, và **ba trong bốn phép ấy đúng**.

Nó cũng là Unit có một lỗi rất dễ bắt — một lỗi bạn phát hiện được **trước khi tính lãi đồng
nào** — và một khoảng trống lớn: cấu trúc vay phổ biến nhất Việt Nam được sách tính ra đúng con số
nhưng không bao giờ gọi tên.

Sách chia nợ theo **mục đích vay**, không theo hình thức (tr. 29):

| Dạng | Sách nói gì | Trang |
| --- | --- | --- |
| **Vay để đầu tư** (đòn bẩy) | nên vay khi lợi nhuận kỳ vọng cao hơn lãi vay | tr. 29–30 |
| **Vay tiêu dùng** | *"tạm ứng dòng tiền tương lai"*, không sinh lợi, cần hạn chế | tr. 30–31 |
| **Vay khẩn cấp** | người có quỹ dự phòng thường không rơi vào | tr. 31 |

Cách chia này tốt. Nó đặt câu hỏi đúng — **tiền vay về sẽ làm gì** — thay vì hỏi vay ở đâu.

Và sách nói thẳng một câu đáng nhớ về thẻ tín dụng (tr. 30–31): dùng thẻ **chính là vay tiêu dùng**,
dù có 45–60 ngày không lãi. Rủi ro sách nêu — dễ mất kiểm soát vì không phải đưa tiền mặt, bị trừ
tiền tự động khi gia hạn dịch vụ đã quên huỷ — đều là những thứ cụ thể, không phải lời khuyên chung
chung.

---

## 2. Đòn bẩy: sách cho hai điểm, công thức cho cả đường

Ví dụ ở tr. 29–30: vốn 100 triệu, phương pháp đầu tư kỳ vọng 15%/năm, vay thêm 100 triệu với lãi
10%/năm.

| | Không vay | Có vay |
| --- | ---: | ---: |
| Vốn đầu tư | 100tr | 200tr |
| Lãi gộp ở 15% | 15tr | 30tr |
| Trừ lãi vay | — | −10tr |
| **Lãi ròng** | **15tr** | **20tr** |
| **Trên vốn của bạn** | **15%** | **20%** |

Sách rồi lật ngược: nếu năm đó thị trường chỉ được 8%, người vay còn `200 × 8% − 10 = 6tr`, người
không vay được `100 × 8% = 8tr`. **Vay lại tệ hơn.**

Cả bốn con số đều đúng — code dựng lại từng cái. Nhưng sách chỉ cho **hai điểm rời rạc**, 15% và
8%. Viết ra công thức thì thấy cả đường:

```
lợi nhuận trên vốn = r + (r − lãi vay) × (nợ / vốn)
```

Đọc thẳng ra ba điều sách không nói: **hoà vốn đúng tại `r` = lãi vay**; trên mức đó đòn bẩy nhân
lãi lên; dưới mức đó nó nhân lỗ lên **theo đúng cùng một hệ số**. Đòn bẩy đối xứng — nó không phải
công cụ tăng lợi nhuận, nó là công cụ tăng **độ lớn**, cả hai chiều.

### [bổ sung] Phía dưới, chỗ sách nói nhẹ nhất

tr. 30 chỉ viết: *"Thậm chí nếu lợi nhuận năm đó âm, lãi vay sẽ làm hao hụt tiền gốc."* Đúng, nhưng
quá nhẹ. Đo bằng số, một năm thị trường −30%:

| Nợ / vốn | Lợi nhuận trên vốn | Mất bao nhiêu phần vốn |
| ---: | ---: | ---: |
| 0,0x (không vay) | −30% | 30% |
| 0,5x | −50% | 50% |
| **1,0x** (đúng ví dụ của sách) | **−70%** | **70%** |
| 2,0x | −110% | **hết vốn, còn nợ thêm** |
| 3,0x | −150% | hết vốn, còn nợ thêm |

Vay ngang vốn — đúng tỷ lệ trong ví dụ của sách — thì **một năm −30% lấy đi 70% vốn của bạn**. Cùng
năm đó người không vay mất 30% và vẫn còn đủ sức chờ hồi phục.

Từ 2,0x trở lên, một năm −30% không chỉ xoá sạch vốn mà còn để lại nợ. Đây là điều kiện phải nói
thành lời: **đòn bẩy không giết bạn bằng việc lỗ, nó giết bằng việc buộc bạn dừng cuộc chơi trước
khi thị trường hồi.** Câu *"nếu vay tiền, hãy chắc chắn bạn cảm thấy thoải mái"* của tr. 30 là lời
khuyên đúng, nhưng bảng trên mới là thứ giúp bạn biết mình có thoải mái thật không.

---

## 3. Trần 20%/năm ở tr. 31 không phải lời khuyên — đó là luật

tr. 31 đưa hai lưu ý khi phải "vay nóng":

> - *"Không vay lãi suất quá cao trên 20%/năm."*
> - *"Không vay ngắn hạn để giải quyết việc dài hạn."*

Lưu ý thứ hai là kinh nghiệm tốt. Lưu ý thứ nhất được viết như một lời khuyên thận trọng, nhưng
con số 20% không phải sách tự nghĩ ra: **đó là mức trần trong Bộ luật Dân sự 2015, Điều 468.**

Sách bỏ mất thông tin có giá trị nhất về con số ấy:

**Điều 468 khoản 1** — lãi suất do các bên thoả thuận, nhưng *không được vượt quá 20%/năm của khoản
tiền vay, trừ trường hợp luật khác có liên quan quy định khác*. Và câu quan trọng nhất: **phần lãi
suất vượt quá giới hạn thì không có hiệu lực.** Không phải "không nên vay" — mà là phần vượt **không
đòi được**. 20%/năm tương đương khoảng **1,67%/tháng**.

**Điều 468 khoản 2** — nếu các bên có thoả thuận trả lãi nhưng không xác định rõ mức, và có tranh
chấp, thì lãi suất được xác định bằng **10%/năm** (một nửa mức trần). Đây là điều đáng biết khi cho
bạn bè vay mà không ghi rõ.

**Ngoại lệ quan trọng — ngân hàng và công ty tài chính không chịu mức trần này.** Mệnh đề *"trừ
trường hợp luật khác có liên quan quy định khác"* dẫn chiếu sang **Luật Các tổ chức tín dụng** và
**Luật Ngân hàng Nhà nước**: lãi suất giữa tổ chức tín dụng với khách hàng theo cơ chế **tự thoả
thuận**, không có trần. Đây là quan điểm của cơ quan quản lý (Vụ Pháp chế – Ngân hàng Nhà nước) áp
dụng từ 01/01/2017, và **vẫn còn tranh luận trong giới nghiên cứu** vì Luật Các TCTD chỉ nói các bên
thoả thuận *"theo quy định của pháp luật"*.

Hệ quả thực tế: thẻ tín dụng 30%/năm hay công ty tài chính 40%/năm **không rơi vào Điều 468**. Mức
trần 20% chủ yếu bảo vệ bạn ở các khoản **vay dân sự ngoài hệ thống tổ chức tín dụng** — đúng loại
"vay nóng" mà tr. 31 đang nói tới.

**Còn ngưỡng hình sự thì cao hơn nhiều.** Tội cho vay lãi nặng (Bộ luật Hình sự 2015, sửa đổi 2017,
Điều 201; hướng dẫn tại Nghị quyết 01/2021/NQ-HĐTP) đòi lãi suất **gấp 5 lần** mức trần dân sự, tức
**từ 100%/năm trở lên** (khoảng 8,33%/tháng), **và** kèm điều kiện thu lợi bất chính từ 30 triệu
đồng. Nên khoảng giữa — từ trên 20% tới dưới 100%/năm — là vùng phần lãi vượt **vô hiệu về dân sự
nhưng chưa phải tội phạm**. Biết ranh giới đó có ích hơn nhiều so với việc chỉ nhớ "đừng vay lãi
cao".

---

## 4. Bài toán mảnh đất: cùng một khoản lãi, khi thì lãi khi thì lỗ

tr. 31–32. Anh A mua đất 1,4 tỷ, bán 1,6 tỷ, lãi 200 triệu, và kết luận tỷ suất sinh lợi 14,29%.

Sách trả lời đúng: con số ấy **thiếu dữ kiện thời gian**. Mua 2019 bán 2021 thì tỷ suất chỉ **7%**.
Kiểm lại: `(1,6/1,4)^(1/2) − 1 = 6,90%`, làm tròn thành 7% — sách khớp.

Đẩy thêm một bước nữa, thêm cột lạm phát 4%/năm:

| Giữ bao lâu | Lợi suất mỗi năm | Trừ lạm phát 4% | 1 triệu thành |
| ---: | ---: | ---: | ---: |
| 1 năm | 14,29% | +10,29% | 1,10tr |
| **2 năm** | **6,90%** | +2,90% | 1,06tr |
| 3 năm | 4,55% | +0,55% | 1,02tr |
| 5 năm | 2,71% | **−1,29%** | **0,94tr** |
| 10 năm | 1,34% | −2,66% | **0,76tr** |

Bài học của sách — *"tỷ suất lợi nhuận phải đi kèm với mốc thời gian cụ thể"* — đúng và quan trọng.
Chỗ sách dừng lại: **giữ 5 năm thì lợi suất thực đã âm.** Đúng một khoản "lãi 200 triệu" ấy, tuỳ
thời gian mà là lãi thật hay là lỗ đã ngụy trang. Giữ 10 năm thì sức mua còn **76%**.

Đây cũng là chỗ nối với [bài 2](bai_02_do_hien_trang.md): tài sản ròng tăng 200 triệu, nhưng phần
lớn mức tăng ấy chỉ là lạm phát chứ không phải giá trị.

---

## 5. Bốn phương án của chị B — phần hay nhất của Unit

tr. 32–35. Chị B vay anh C **100 triệu**, kỳ hạn 1 năm. Anh C nói lãi **8%/năm**, tổng phải trả
108 triệu, đề xuất trả **9 triệu mỗi tháng** trong 12 tháng.

Câu hỏi của sách: chị B có thật sự đang trả 8% không?

Cách kiểm duy nhất đáng tin là **bỏ qua mọi con số được nói ra, chỉ nhìn dòng tiền**, rồi giải IRR:

| Phương án | Lãi/tháng | Lãi/năm | Tổng trả | Sách ghi |
| --- | ---: | ---: | ---: | ---: |
| PA1 trả một lần cuối kỳ | 0,6434% | 8,00% | 108,00tr | 8% |
| **PA2 trả đều 12 tháng** (đề xuất của anh C) | 1,2043% | **15,45%** | 108,00tr | 15,39% |
| PA3 trả luôn tháng đầu | 1,4313% | 18,59% | 108,00tr | 18,58% |

**Kết luận của sách đứng vững, và đây là điều quan trọng nhất của cả bài:** cùng trả 108 triệu,
nhưng trả rải đều trong năm thì chi phí thật **gần gấp đôi** con số 8% được nói. Lý do đơn giản —
chị B không được giữ 100 triệu suốt một năm; từ tháng thứ hai trở đi cô đã trả bớt gốc mà lãi vẫn
tính như chưa trả.

Và PA3 cho thấy chỉ cần **dời một kỳ trả** lên sớm hơn — anh C bảo *"nhân tiện đây"* trả luôn tháng
này — là 15,45% thành 18,59%. Cùng số tiền, cùng số kỳ, chỉ khác thời điểm.

### Một chi tiết nhỏ về cách làm tròn

Sách ra 15,39% còn tính chính xác ra 15,45%. Không ai sai: sách **làm tròn lãi tháng xuống 1,2%
trước rồi mới luỹ thừa 12**, còn con số chính xác là 1,2043%/tháng.

| | Làm tròn rồi luỹ thừa (cách sách) | Chính xác |
| --- | ---: | ---: |
| PA2 | 1,2% → 15,39% | 1,2043% → 15,45% |
| PA3 | 1,43% → 18,58% | 1,4313% → 18,59% |

Chênh lệch 0,06 điểm ở đây không đổi kết luận gì. Nhưng quy tắc thì đáng nhớ, vì nó sẽ đổi kết luận
ở các khoản vay dài: **luỹ thừa 12 khuếch đại sai số làm tròn, nên làm tròn ở bước cuối, đừng làm
tròn ở bước giữa.**

---

## 6. [đính chính] Phương án 4: sách nói 11 tháng

tr. 34 chuyển sang tính xem **8%/năm thật** thì trả bao lâu:

> *"Lãi suất tháng = 8/12 = 0,67%. Sau 11 tháng chị B sẽ trả hết nợ như trong hình dưới
> đây:"*

Chỗ này sai, và bắt được **trước khi tính lãi đồng nào**:

```
11 tháng × 9 triệu = 99 triệu  <  100 triệu tiền GỐC
```

Trả 11 kỳ thì không thể hết nợ **kể cả khi lãi suất bằng 0**. Đây là loại lỗi đáng học nhất: không
cần công cụ gì, chỉ cần một phép nhân và một câu hỏi: tổng đã trả có vượt nổi tiền gốc chưa.

Trả dần thật trên dư nợ giảm dần, lãi 0,6667%/tháng đúng như sách quy đổi:

```
    kỳ      lãi     trả gốc     thực trả       dư nợ
  ──────────────────────────────────────────────────────
      1    0.67tr     8.33tr      9.00tr     91.67tr
      2    0.61tr     8.39tr      9.00tr     83.28tr
      3    0.56tr     8.44tr      9.00tr     74.83tr
      4    0.50tr     8.50tr      9.00tr     66.33tr
      5    0.44tr     8.56tr      9.00tr     57.77tr
      6    0.39tr     8.61tr      9.00tr     49.16tr
      7    0.33tr     8.67tr      9.00tr     40.49tr
      8    0.27tr     8.73tr      9.00tr     31.76tr
      9    0.21tr     8.79tr      9.00tr     22.97tr
     10    0.15tr     8.85tr      9.00tr     14.12tr
     11    0.09tr     8.91tr      9.00tr      5.22tr
     12    0.03tr     5.22tr      5.25tr      0.00tr
```

**12 kỳ, không phải 11.** Sau kỳ 11 vẫn còn nợ 5,22tr; kỳ 12 trả nốt 5,25tr.

### Và đây mới là điều PA4 thật sự chứng minh

Sách dừng ở chỗ đếm số tháng, nên bỏ lỡ kết quả quan trọng hơn nhiều. Đọc cột "lãi":

- **PA4** — 8%/năm thật trên dư nợ giảm dần: chị B trả tổng **104,25tr**, tiền lãi **4,25tr**.
- **PA2** — đề xuất của anh C: chị B trả tổng **108,00tr**, tiền lãi **8,00tr**.

**Chênh lệch 3,75 triệu chính là phần anh C thu thừa.** Sách tính được lãi suất của PA2 nhưng chưa
bao giờ quy nó về đồng — mà đồng mới là thứ chị B đưa ra khỏi ví.

Chú ý cả điều này: ở PA4, "8%/năm" chỉ tốn **4,25tr** chứ không phải 8tr. Vì bạn chỉ nợ đủ 100 triệu
trong tháng đầu; trung bình cả năm bạn chỉ nợ khoảng một nửa số đó. **Lãi 8% trên một khoản trả
góp không bao giờ bằng 8% số tiền vay ban đầu** — trừ khi hợp đồng cố tình viết như vậy, và đó chính
là mục sau.

### [đính chính] Sách quy đổi hai chiều bằng hai cách khác nhau

| Chiều | Sách dùng | Ở trang |
| --- | --- | --- |
| tháng → năm | luỹ thừa: `(1 + r)^12 − 1` | tr. 33, 34 |
| năm → tháng | chia 12: `8%/12 = 0,6667%` | tr. 34 |

Hai phép này **không phải nghịch đảo của nhau**. Chia 12 rồi luỹ thừa lại thì ra **8,30%**, không
quay về 8%. Nhất quán với chiều trên thì lãi tháng phải là `1,08^(1/12) − 1 = 0,6434%`.

Với PA4, dùng con số nhất quán thì tổng lãi là **4,10tr** thay vì 4,25tr. Chênh lệch nhỏ ở kỳ hạn
một năm, nhưng không nhỏ với khoản vay 20 năm. Quy tắc: **chọn một quy ước rồi dùng suốt.** Sách đổi
quy ước giữa hai trang liền nhau.

---

## 7. [bổ sung] Cái tên sách không gọi: lãi trên dư nợ gốc

Đây là khoảng trống lớn nhất của Unit 3.

PA2 **không phải một sự nhầm lẫn của anh C**. Nó là một cấu trúc vay có tên riêng, in trên hợp đồng,
và là cấu trúc phổ biến nhất trong cho vay tiêu dùng Việt Nam:

| Cách tính | Lãi tính trên cái gì |
| --- | --- |
| **lãi trên dư nợ gốc** (lãi phẳng, *flat rate*) | **số vay ban đầu**, suốt kỳ hạn, dù bạn đã trả gần hết |
| **lãi trên dư nợ giảm dần** | phần bạn **còn nợ thật** ở từng kỳ |

PA2 chính là cách thứ nhất: lãi tính trên 100 triệu suốt 12 tháng, dù đến tháng 11 chị B chỉ còn nợ
chưa tới 10 triệu. PA4 là cách thứ hai.

Sách tính ra 15,45% cho PA2 mà **không gọi tên cấu trúc ấy**. Người học vì thế nắm được phép tính
nhưng không nhận ra nó khi gặp lại trên một hợp đồng trả góp — chỗ mà kiến thức này thật sự cần
dùng.

Quy đổi tổng quát, vay trả đều trong 12 tháng:

| Lãi phẳng ghi trên hợp đồng | Lãi thật/tháng | Lãi thật/năm | Gấp mấy lần |
| ---: | ---: | ---: | ---: |
| 6%/năm | 0,91% | 11,46% | 1,91x |
| **8%/năm** (chính là PA2) | 1,20% | **15,45%** | 1,93x |
| 10%/năm | 1,50% | 19,53% | 1,95x |
| 12%/năm | 1,79% | 23,70% | 1,97x |
| 15%/năm | 2,22% | 30,12% | 2,01x |
| 20%/năm | 2,92% | 41,30% | 2,06x |

**Quy luật cần thuộc: trả đều trong 12 tháng thì lãi thật xấp xỉ gấp đôi con số phẳng ghi trên hợp
đồng.** Nhân đôi trong đầu là đủ để so sánh hai chào mời.

### Và một cái bẫy đo lường, ngay cạnh mức 20% của mục 3

| Hợp đồng ghi | Trả thật | So với 20% |
| ---: | ---: | --- |
| 8,0%/năm phẳng | 15,45%/năm | dưới |
| 10,0%/năm phẳng | 19,53%/năm | dưới |
| **10,5%/năm phẳng** | **20,56%/năm** | **trên** |
| 12,0%/năm phẳng | 23,70%/năm | trên |

Một hợp đồng ghi 10,5%/năm — nghe rất lành, thấp hơn hẳn lãi thẻ tín dụng — đã đưa chi phí thật của
bạn vượt mức 20%.

**Cần nói rõ đây là chuyện đo lường, không phải kết luận pháp lý.** Hai con số đo hai thứ khác nhau:
Điều 468 viết về *lãi suất theo thoả thuận của khoản tiền vay*, còn cột bên phải là *chi phí thực tế
theo dòng tiền*. Việc một hợp đồng lãi phẳng có vi phạm Điều 468 hay không là câu hỏi pháp lý mà bài
này không trả lời. Bài này chỉ nói một điều: **đừng đem con số trên hợp đồng đi so thẳng với 20%.**

---

## 8. Snowball và Avalanche

tr. 35–37. Hai cách sắp thứ tự trả nợ:

- **Snowball** (Dave Ramsey, *The Total Money Makeover*) — trả **khoản nhỏ nhất trước**, không quan
  tâm lãi suất. Mỗi khi dứt một khoản thì dồn số tiền đó sang khoản nhỏ tiếp theo (bốn bước ở
  tr. 36).
- **Avalanche** — trả **khoản lãi cao nhất trước**.

Sách trình bày cả hai công bằng và nêu đúng đánh đổi (tr. 37): Snowball *"không tính lãi suất nên
khi thời gian trả các khoản nợ lớn bị kéo dài, bạn sẽ mất nhiều tiền lãi hơn"*, đổi lại nó **tạo
động lực** vì bạn thấy các khoản nợ biến mất nhanh. Và một lưu ý thực tế tốt: trong lúc thực hiện,
**tuyệt đối hạn chế vay thêm**.

### [đính chính] Lý do thứ nhất của tr. 35 không đúng

tr. 35 đưa ba lý do chọn Snowball. Lý do đầu tiên:

> *"Thông thường, số lượng nợ nhỏ chiếm phần lớn tổng lượng nợ của bạn"*

Lấy ngay bốn khoản mà **chính sách liệt kê ở tr. 36** — thẻ tín dụng, trả góp laptop, trả góp điện
thoại, vay mua nhà — với dư nợ giả định hợp lý:

| Khoản nợ | Dư nợ | Lãi/năm | Tối thiểu/tháng | % tổng nợ |
| --- | ---: | ---: | ---: | ---: |
| trả góp điện thoại | 8,00tr | 12% | 0,70tr | 0,9% |
| nợ thẻ tín dụng | 20,00tr | 30% | 0,60tr | 2,3% |
| trả góp laptop | 25,00tr | 18% | 1,20tr | 2,9% |
| **vay mua nhà** | **800,00tr** | 9% | 7,00tr | **93,8%** |

Ba khoản nhỏ cộng lại **53tr = 6,2%** tổng nợ. Riêng khoản mua nhà chiếm **93,8%**.

Nhiều khoản nợ nhỏ về **số lượng**, nhưng nhỏ luôn cả về **tiền**. Đây lại là kiểu lẫn giữa *đếm* và
*đo* mà [bài 2](bai_02_do_hien_trang.md) đã cảnh báo. Hai lý do còn lại của tr. 35 — giữ uy tín bản
thân, và các khoản nhỏ vừa sức trả — thì đứng vững.

*(Dư nợ và lãi suất ở bảng trên là **giả định của bài này**; sách không cho con số nào. Đổi số thì
kết luận có thể đổi — đó là bài tập ở [mục 11](#11-tự-thử).)*

### Sách bảo không có câu trả lời. Có một nửa câu trả lời, và nó là một con số

> tr. 37: *"Vậy đâu là phương án tối ưu? Tôi không có câu trả lời dành cho bạn. Điều này phụ thuộc
> vào việc tâm lý và tính cách cá nhân bạn phù hợp với kiểu nào hơn."*

Câu này đúng một nửa. Cái nào **hợp** với bạn thì đúng là chuyện cá nhân. Nhưng cái nào **rẻ hơn**
thì không phải chuyện cá nhân: Avalanche không bao giờ tốn lãi nhiều hơn, vì mỗi đồng dư luôn được
dí vào chỗ sinh lãi nhanh nhất. Câu hỏi thật là **động lực đáng giá bao nhiêu**, và đó là số tính
được trước khi chọn.

Bộ nợ trên cố tình cho hai chiến lược đối đầu — khoản **nhỏ nhất** (điện thoại, 8tr) lại là khoản
lãi **thấp nhất** (12%):

**Kịch bản A — ba khoản tiêu dùng**, ngân sách 5tr/tháng (sách tự tách nợ mua nhà ra ở tr. 24):

| Chiến lược | Số tháng | Tổng lãi | Khoản đầu tiên hết |
| --- | ---: | ---: | --- |
| Snowball | 12 | 6,40tr | **tháng 3** (điện thoại) |
| Avalanche | 12 | **5,82tr** | tháng 8 (thẻ tín dụng) |

**Giá của động lực: 0,59tr — 10,1% tổng lãi.** Đổi lại, bạn thấy khoản nợ đầu tiên biến mất ở tháng
3 thay vì tháng 8. Đó là một đánh đổi thật, và bây giờ nó có giá niêm yết.

### [bổ sung] Thêm khoản mua nhà vào, hai đơn vị đo nói ngược nhau

**Kịch bản B — cả bốn khoản**, ngân sách 12tr/tháng:

| Kịch bản | Giá của động lực | Tính theo % tổng lãi |
| --- | ---: | ---: |
| A — ba khoản tiêu dùng | 0,59tr | **10,12%** |
| B — thêm nợ mua nhà | **1,16tr** | **0,31%** |

Hai cột nói ngược nhau, và cả hai đều đúng.

Theo **phần trăm**, thêm khoản mua nhà vào thì việc chọn chiến lược trông như không đáng bàn —
0,31%. Theo **đồng**, nó lại đáng gấp đôi: 0,59tr thành 1,16tr. Lý do: dứt điểm nợ tiêu dùng sớm hơn
thì ngân sách được giải phóng sớm hơn, và phần dư ấy chạy suốt gần 100 tháng còn lại của khoản vay
nhà.

Thứ đánh lừa là **mẫu số**. Khoản mua nhà chiếm 93,8% tổng nợ nên mọi tỷ lệ tính trên tổng đều bị nó
nuốt. Và cả hai chiến lược đều xếp nó **cuối cùng** — lớn nhất theo Snowball, lãi thấp nhất theo
Avalanche — nên việc chọn chiến lược thật ra chỉ điều khiển 6,2% số nợ.

**Đọc bằng đồng, đừng đọc bằng phần trăm của một tổng bị một khoản mục thống trị.**

### Về đường link Excel ở tr. 37

Sách kết Unit bằng một bảng tính chia sẻ qua liên kết rút gọn `bit.ly` kèm mã QR (tr. 37–38). Liên
kết rút gọn của bên thứ ba có tuổi thọ không đoán trước được, và bài này không kiểm chứng nội dung
bảng tính đó. Toàn bộ phép tính tương đương nằm trong
[`bai-08-vay-va-tra-no.py`](../thuc_hanh/bai-08-vay-va-tra-no.py) — sửa danh sách `NO` là ra kế
hoạch của bạn.

---

## 9. [bổ sung] Khoản 13 triệu của bài 7: trả nợ hay bỏ vào FFA?

[Bài 7](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật) kết thúc với một câu
hỏi bỏ ngỏ: tháng Tết phải vay 13 triệu, mà sáu chiếc lọ không có lọ trả nợ. Tiền dôi ra tháng sau
nên nạp lại FFA hay dập khoản vay?

Nguyên tắc gọn và đáng thuộc:

> **Trả một đồng nợ lãi `i` là một khoản đầu tư có lợi suất đúng bằng `i` — chắc chắn, không rủi ro,
> không phải nộp thuế.** Còn lọ FFA kỳ vọng 8% thực: *kỳ vọng*, và có rủi ro mất.

| Lãi vay/năm | Tiền lãi một năm trên 13tr | So với FFA 8% |
| ---: | ---: | --- |
| 8% | 1,04tr | hoà |
| 10% | 1,30tr | **trả nợ trước** |
| 15% | 1,95tr | **trả nợ trước** |
| 20% | 2,60tr | **trả nợ trước** |
| 30% | 3,90tr | **trả nợ trước** |

Ngưỡng nằm đúng ở lợi suất kỳ vọng của khoản đầu tư. Trên ngưỡng, trả nợ **thắng chắc** một khoản
đầu tư chỉ thắng **trên kỳ vọng** — và khoản vay nóng gần như luôn nằm trên ngưỡng. Nên thứ tự đúng
cho tình huống bài 7 là: **dập khoản vay trước, rồi mới nạp lại FFA.**

Sách có nói ý này, nhưng ở chỗ khác và không nối lại: tr. 24 viết *"nếu bạn đang mắc nợ, quỹ Savings
sẽ được trích ra để trả nợ trước"*, và cũng chính tr. 24 nêu ngoại lệ hợp lý — *"trừ nợ vay ngân
hàng trả góp mua nhà"*, vì lãi vay mua nhà thường **dưới** ngưỡng. Cái sách thiếu là **nói ngưỡng ấy
nằm ở đâu**, và nó nằm ở lợi suất kỳ vọng của chính khoản đầu tư bạn định làm.

---

## 10. Bốn câu hỏi cần hỏi trước khi ký

Gom cả bài thành một danh sách dùng được:

1. **Lãi tính trên dư nợ gốc hay dư nợ giảm dần?** Nếu là dư nợ gốc, nhân đôi con số ấy trước khi
   so sánh (mục 7).
2. **Tổng cộng tôi đưa ra bao nhiêu đồng?** Cộng hết các kỳ trả, trừ đi số vay. Con số này không nói
   dối được, không phụ thuộc quy ước tính lãi nào (mục 6).
3. **Kỳ trả đầu tiên vào lúc nào?** Trả ngay hôm nhận tiền hay tháng sau — chỉ khác biệt đó đã đưa
   15,45% lên 18,59% (mục 5).
4. **Có phí gì ngoài lãi không?** Phí thẩm định, phí bảo hiểm khoản vay, phí trả nợ trước hạn. Cả
   sách lẫn bài này đều chưa tính các khoản ấy, và chúng đẩy chi phí thật lên cao hơn nữa.

Và một câu cho phía cho vay: nếu bạn là anh C, **PA4 mới là 8%**. Đề xuất "9 triệu × 12 tháng" thu
gần gấp đôi con số bạn đang nói với bạn mình.

---

## 11. Tự thử

Sửa [`thuc_hanh/bai-08-vay-va-tra-no.py`](../thuc_hanh/bai-08-vay-va-tra-no.py) rồi chạy lại.

1. **Đòn bẩy tới ngưỡng nào thì đứt?** Trong `roe`, tìm mức `r` khiến người vay 2,0x mất trắng vốn.
   So với người không vay, thị trường phải xuống bao nhiêu thì họ mới mất trắng?

2. **Chị B trả bao nhiêu mỗi tháng thì hết đúng 12 kỳ?** Đổi `TRA_THANG` và tìm số tiền nhỏ nhất
   (làm tròn tới 100 nghìn) để `lich_tra_no` kết thúc ở kỳ 12. Kết quả cho biết đề xuất 9 triệu của
   anh C dư hay thiếu bao nhiêu.

3. **Quy luật gấp đôi đúng tới kỳ hạn nào?** `lai_that_tu_lai_phang` có tham số `so_thang`. Thử 6,
   12, 24, 36 tháng với cùng lãi phẳng 10%/năm. Tỷ số "gấp mấy lần" đi lên hay đi xuống? Giải thích
   vì sao.

4. **Lật ngược kết luận Snowball.** Trong `NO`, đổi lãi suất khoản điện thoại từ 12% lên 30% (bằng
   thẻ tín dụng). Hai chiến lược còn khác nhau không? Điều đó nói gì về *khi nào* mới cần tranh luận
   Snowball với Avalanche?

5. **Ngân sách quyết định bao nhiêu?** Chạy kịch bản A với ngân sách 3tr, 5tr, 8tr, 12tr. "Giá của
   động lực" đi theo hướng nào khi bạn có nhiều tiền hơn để dồn? Vì sao?

6. **Nợ của chính bạn.** Thay `NO` bằng các khoản nợ thật của bạn, đặt `NGAN_SACH` bằng số tiền bạn
   thật sự dành ra được mỗi tháng. Biết giá của động lực rồi mới chọn chiến lược.

---

## 12. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Đòn bẩy tài chính | Financial leverage | Dùng tiền vay để tăng quy mô đầu tư. Nhân cả lãi lẫn lỗ theo cùng một hệ số |
| Lãi trên dư nợ gốc, lãi phẳng | Flat interest rate | Lãi tính trên số vay ban đầu suốt kỳ hạn. Chi phí thật xấp xỉ gấp đôi con số ghi |
| Lãi trên dư nợ giảm dần | Reducing balance | Lãi tính trên phần còn nợ thật ở từng kỳ |
| Tỷ suất hoàn vốn nội bộ | IRR — Internal Rate of Return | Lãi suất làm giá trị hiện tại của dòng tiền bằng 0. Cách duy nhất đáng tin để so hai khoản vay khác cấu trúc |
| Lãi suất hiệu dụng năm | EAR — Effective Annual Rate | `(1 + lãi tháng)^12 − 1`. Sách dùng cách này ở tr. 33 |
| Bảng trả nợ dần | Amortization schedule | Bảng tách từng kỳ thành phần lãi và phần gốc |
| Quả cầu tuyết | Snowball | Trả khoản nợ nhỏ nhất trước |
| Tuyết lở | Avalanche | Trả khoản nợ lãi cao nhất trước |
| Nợ tốt / nợ xấu | Good debt / bad debt | Sách chia theo mục đích vay, không theo hình thức (tr. 29) |

---

## 13. Câu hỏi tự kiểm tra

1. Sách chia nợ thành ba dạng theo tiêu chí gì? Kể tên ba dạng.
2. Vốn 100tr, vay thêm 100tr với lãi 10%/năm. Viết công thức lợi nhuận trên vốn theo `r`.
3. Ở tỷ lệ nợ/vốn bằng bao nhiêu thì một năm thị trường −30% xoá sạch vốn của bạn?
4. Con số 20%/năm ở tr. 31 đến từ văn bản nào? Hậu quả pháp lý của phần lãi vượt quá là gì?
5. Vì sao thẻ tín dụng 30%/năm không rơi vào mức trần đó?
6. Anh A mua đất 1,4 tỷ bán 1,6 tỷ. Vì sao con số 14,29% chưa trả lời được câu hỏi nào?
7. Giữ mảnh đất ấy 5 năm thì lợi suất **thực** là bao nhiêu?
8. PA2 trả 9tr × 12 tháng cho khoản vay 100tr, lãi được nói là 8%. Lãi thật là bao nhiêu, và vì sao
   nó cao hơn?
9. Chỉ dời **một kỳ trả** lên sớm hơn thì 15,45% thành bao nhiêu?
10. Vì sao "sau 11 tháng chị B trả hết nợ" sai, và bạn chứng minh được điều đó bằng một phép tính
    nào?
11. Ở PA4, "8%/năm" tốn bao nhiêu tiền lãi? Vì sao không phải 8 triệu?
12. Hai cách quy đổi lãi tháng ↔ lãi năm mà sách dùng là gì? Chúng có nghịch đảo nhau không?
13. Một hợp đồng ghi "lãi 12%/năm trên dư nợ gốc, trả góp 12 tháng". Chi phí thật khoảng bao nhiêu?
14. Lý do đầu tiên tr. 35 đưa ra cho Snowball là gì, và vì sao nó sai?
15. Avalanche có bao giờ tốn lãi nhiều hơn Snowball không? Vậy "đâu là phương án tối ưu" là câu hỏi
    thuộc loại nào?
16. Vì sao thêm khoản vay mua nhà vào danh sách lại khiến chênh lệch hai chiến lược **tăng** tính
    theo đồng nhưng **giảm** tính theo phần trăm?
17. Có 13 triệu nợ lãi 15%/năm và một lọ FFA kỳ vọng 8% thực. Tiền dôi ra đi đâu trước? Ngưỡng nằm
    ở đâu?
18. Bốn câu cần hỏi trước khi ký hợp đồng vay?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 8 — VAY, LÃI SUẤT THẬT, TRẢ NỢ                    C2 tr. 29-38      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ĐÒN BẨY   lợi nhuận/vốn = r + (r - lãi vay) × nợ/vốn                   ║
║     hoà vốn tại r = lãi vay · ĐỐI XỨNG: nhân lãi bao nhiêu, nhân lỗ bấy ║
║     nợ/vốn 1,0x + thị trường -30%  ->  mất 70% vốn                      ║
║     nợ/vốn 2,0x + thị trường -30%  ->  hết vốn, CÒN NỢ THÊM             ║
║                                                                          ║
║  TRẦN 20%/NĂM ở tr. 31 KHÔNG phải lời khuyên — BLDS 2015 Đ.468          ║
║     phần lãi vượt quá KHÔNG CÓ HIỆU LỰC (không đòi được), ~1,67%/tháng  ║
║     không rõ mức lãi + có tranh chấp -> 10%/năm (Đ.468 khoản 2)         ║
║     NGOẠI LỆ: ngân hàng, công ty tài chính tự thoả thuận, KHÔNG trần    ║
║     hình sự (BLHS Đ.201): gấp 5 lần = từ 100%/năm, kèm thu lợi >= 30tr  ║
║                                                                          ║
║  MẢNH ĐẤT 1,4 -> 1,6 tỷ: 14,29% vô nghĩa nếu chưa nói giữ bao lâu       ║
║     2 năm 6,90% · 5 năm 2,71% -> TRỪ LẠM PHÁT 4% THÌ ÂM                 ║
║                                                                          ║
║  BỐN PHƯƠNG ÁN CỦA CHỊ B — vay 100tr, "8%/năm", trả 9tr/tháng           ║
║     PA1 trả cuối kỳ        8,00%   tổng 108,00tr                        ║
║     PA2 trả đều 12 tháng  15,45%   tổng 108,00tr   <- GẦN GẤP ĐÔI       ║
║     PA3 trả luôn tháng đầu 18,59%  tổng 108,00tr                        ║
║     PA4 8% THẬT, dư nợ giảm dần    tổng 104,25tr, lãi chỉ 4,25tr        ║
║     -> 3,75tr là phần anh C thu thừa. Sách tính ra %, không quy ra đồng ║
║                                                                          ║
║  [đính chính] tr. 34 "sau 11 tháng trả hết" — SAI                       ║
║     11 × 9tr = 99tr < 100tr GỐC. Sai kể cả khi lãi bằng 0. Thật: 12 kỳ  ║
║  [đính chính] tháng->năm luỹ thừa, năm->tháng chia 12. Không nghịch đảo ║
║     8%/12 rồi luỹ thừa lại = 8,30%, không quay về 8%                    ║
║                                                                          ║
║  [bổ sung] LÃI TRÊN DƯ NỢ GỐC (lãi phẳng) — tên sách không gọi          ║
║     PA2 chính là cấu trúc này, phổ biến nhất trong vay tiêu dùng VN     ║
║     QUY LUẬT: trả đều 12 tháng -> lãi thật XẤP XỈ GẤP ĐÔI số ghi trên HĐ║
║     HĐ ghi 10,5% phẳng -> trả thật 20,56%. Đừng so số trên HĐ với 20%   ║
║                                                                          ║
║  SNOWBALL (nhỏ nhất trước) vs AVALANCHE (lãi cao nhất trước)            ║
║     [đính chính] tr. 35 "nợ nhỏ chiếm phần lớn tổng nợ" — sai:          ║
║        chính ví dụ tr. 36: ba khoản nhỏ 6,2%, riêng nhà 93,8%           ║
║     kịch bản A (3 khoản tiêu dùng): Snowball tốn thêm 0,59tr = 10,1%    ║
║        đổi lại khoản đầu tiên hết ở tháng 3 thay vì tháng 8             ║
║     Avalanche KHÔNG BAO GIỜ tốn lãi hơn -> "cái nào rẻ" không phải      ║
║        chuyện cá nhân; chỉ "cái nào hợp" mới là                         ║
║     thêm nợ nhà: theo % còn 0,31% nhưng theo ĐỒNG tăng lên 1,16tr       ║
║        -> đọc bằng đồng, đừng đọc bằng % của tổng bị một khoản nuốt     ║
║                                                                          ║
║  [bổ sung] TRẢ NỢ HAY ĐẦU TƯ — ngưỡng = lợi suất kỳ vọng                ║
║     trả nợ lãi i = đầu tư lợi suất i, CHẮC CHẮN, miễn thuế              ║
║     13tr của bài 7: vay nóng luôn trên ngưỡng -> dập nợ trước, rồi FFA  ║
║                                                                          ║
║  BỐN CÂU TRƯỚC KHI KÝ                                                   ║
║     1. gốc hay dư nợ giảm dần?   2. tổng cộng đưa ra bao nhiêu đồng?    ║
║     3. kỳ trả đầu vào lúc nào?   4. còn phí gì ngoài lãi?               ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn.
  Unit 3, Lesson 1–3, **tr. 29–38**. Ba dạng vay, ví dụ đòn bẩy, hai bài toán lãi suất với bốn
  phương án, Snowball và Avalanche đều chép từ đây.
- Sách dẫn **Dave Ramsey, *The Total Money Makeover*** cho phương pháp Snowball (tr. 35). Bài này
  **không kiểm chứng nội dung cuốn gốc** — chỉ kiểm phần số học trong chính C2.
- **Văn bản pháp luật** (mục 3), tra ngày **09/09/2026**:
  - **Bộ luật Dân sự 2015, Điều 468** — lãi suất thoả thuận không vượt quá 20%/năm của khoản tiền
    vay, *trừ trường hợp luật khác có liên quan quy định khác*; phần vượt quá **không có hiệu lực**.
    Khoản 2: không xác định rõ lãi suất và có tranh chấp thì áp dụng 10%/năm.
  - **Luật Các tổ chức tín dụng 2024** (số 32/2024/QH15, hiệu lực 01/7/2024; sửa đổi bởi Luật
    43/2024/QH15 và Luật 96/2025/QH15) và **Luật Ngân hàng Nhà nước 2010** — lãi suất giữa tổ chức
    tín dụng với khách hàng theo cơ chế tự thoả thuận. Đây là quan điểm của Vụ Pháp chế – Ngân hàng
    Nhà nước áp dụng từ 01/01/2017, **vẫn còn tranh luận trong giới nghiên cứu**.
  - **Bộ luật Hình sự 2015** (sửa đổi, bổ sung 2017), **Điều 201** — tội cho vay lãi nặng trong giao
    dịch dân sự, và **Nghị quyết 01/2021/NQ-HĐTP** của Hội đồng Thẩm phán TAND tối cao hướng dẫn:
    lãi suất gấp 05 lần trở lên mức cao nhất tại khoản 1 Điều 468, kèm điều kiện thu lợi bất chính
    từ 30 triệu đồng.

  Các trang tra cứu đã dùng:
  [Cần hiểu đúng về trần lãi suất cho vay 20%/năm — Bảo hiểm tiền gửi Việt Nam](https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam) ·
  [Lãi suất theo Điều 468 BLDS 2015, đối tượng chịu sự điều chỉnh — Bộ Tư pháp](https://moj.gov.vn/qt/tintuc/Pages/nghien-cuu-trao-doi.aspx?ItemID=2083) ·
  [Những quy định mới về lãi suất theo BLDS — VKSND Tối cao](https://vksndtc.gov.vn/UserControls/Publishing/News/BinhLuan/pFormPrint.aspx?UrlListProcess=22D48E3E00E317DB107E3706F225B1CE22F006B7C704FC8B6894F6ABCA85660A&ItemID=2426&webP=portal) ·
  [Luật Các tổ chức tín dụng 2024, toàn văn — Cổng thông tin văn bản Chính phủ](https://vanban.chinhphu.vn/?pageid=27160&docid=211190) ·
  [Tội cho vay lãi nặng trong giao dịch dân sự (Điều 201 BLHS) — Thư viện Pháp luật](https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/tu-van-phap-luat/42507/toi-cho-vay-nang-lai-trong-giao-dich-dan-su-theo-bo-luat-hinh-su)
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-08-vay-va-tra-no.py`](../thuc_hanh/bai-08-vay-va-tra-no.py).
  Mọi lãi suất trong bài tính lại từ dòng tiền bằng bộ giải IRR chia đôi tự viết, không dùng gói
  ngoài; bộ giải tự kiểm bằng một ca biết trước đáp số. Tệp cũng dựng lại đúng bốn con số đòn bẩy
  của tr. 29–30 và ba lãi suất của tr. 32–34 trước khi tổng quát hoá, và tự kiểm rằng Avalanche
  không bao giờ tốn lãi nhiều hơn Snowball.
- **Con số giả định, không phải của sách:** dư nợ và lãi suất bốn khoản ở mục 8; lạm phát 4%/năm ở
  mục 4; lợi suất thực kỳ vọng 8% ở mục 9 (lấy từ giả định C1 tr. 31 đã dùng ở bài 1).
- **Liên hệ chéo:**
  - Khoản vay 13 triệu mà bài này nhận lại:
    [bài 7 mục 8](bai_07_phan_bo_thu_nhap.md#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật).
  - Lọ FFA và tỷ lệ giữ lại 20%:
    [bài 7 mục 6](bai_07_phan_bo_thu_nhap.md#6-bổ-sung-đặt-ba-công-thức-cạnh-nhau-một-đáp-số-duy-nhất).
  - Lãi kép và số năm tới tự do tài chính:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Nợ nằm ở đâu trên bảng cân đối cá nhân:
    [bài 2 mục 3](bai_02_do_hien_trang.md#3-tài-sản-ròng--bước-2-và-bảng-cân-đối-cá-nhân).
  - Định nghĩa nợ của sách quá hẹp:
    [bài 4 mục 2](bai_04_tai_san_tieu_san_thap_tai_san.md#2-đính-chính-định-nghĩa-nợ-quá-hẹp).
  - Đòn bẩy ở tầm doanh nghiệp:
    [Trí tuệ tài chính bài 8](../../trituetaichinh/ly_thuyet/bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md).
  - Lạm phát, quỹ khẩn cấp — thứ lẽ ra đã chặn khoản vay tháng Tết: **bài 9**.

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
| 6 | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách | 1 |
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| **8** | **Vay, lãi suất thật, trả nợ** ← *bạn đang ở đây* | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | **[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai | ngoài sách | 2 |
| 11 | Nhận diện lừa đảo: Ponzi và CFD | C2 tr. 47–57 | 1 |
| 12 | Rủi ro, khẩu vị rủi ro, phân bổ tài sản | C1 tr. 25–33 | 1 |
| 13 | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
