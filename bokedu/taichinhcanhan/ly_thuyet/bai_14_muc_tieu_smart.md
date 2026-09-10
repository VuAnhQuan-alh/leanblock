# Bài 14 — Mục tiêu SMART và ráp lại thành kế hoạch

> Bài học dựa trên **C1 tr. 34–40** — Unit 5 (*Mục tiêu và lập kế hoạch*) Lesson 1–2 của *Tài chính
> cá nhân 101, Class 1*. Đây là **bài cuối** của khoá.
>
> **Cần đọc trước:** không phải một bài, mà **cả mười ba bài trước** — bài này ráp chúng lại. Đặc
> biệt [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md) (công thức tự do tài chính, khẩu vị) và
> [bài 13](bai_13_kenh_dau_tu.md) (danh mục bốn kênh).
>
> **[đã cắt]:** Lesson 2 của sách (*"5 bước lập kế hoạch tự do tài chính cùng TOPI"*, tr. 39–40) là
> hướng dẫn dùng app. Khoá học thay bằng **bảng tính tự dựng** — và điều bất ngờ là năm bước ấy
> **chính là cả khoá học này**. [Mục 4](#4-đã-cắt-5-bước-cùng-topi-chính-là-cả-khoá-học).
>
> **Ký hiệu:** **[bổ sung]** ngoài sách · **[đính chính]** chỗ sách sai · **[đã cắt]** phần thương
> mại thay bằng cách khác.
>
> **Code:** [`thuc_hanh/bai-14-ke-hoach.py`](../thuc_hanh/bai-14-ke-hoach.py)
> — dựng bảng kế hoạch tự do tài chính cho người ở bài 3 từ chính số của các bài trước, và tính số
> tiền đích theo lợi suất thực. Công thức một dòng kèm theo.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Bài cuối làm hai việc](#1-bài-cuối-làm-hai-việc)
- [2. SMART: nguồn gốc và năm chữ](#2-smart-nguồn-gốc-và-năm-chữ)
- [3. Áp SMART vào người ở bài 3](#3-áp-smart-vào-người-ở-bài-3)
- [4. [đã cắt] "5 bước cùng Topi" chính là cả khoá học](#4-đã-cắt-5-bước-cùng-topi-chính-là-cả-khoá-học)
- [5. Ráp một kế hoạch tự do tài chính, không cần app](#5-ráp-một-kế-hoạch-tự-do-tài-chính-không-cần-app)
- [6. Toàn khoá trong một trang](#6-toàn-khoá-trong-một-trang)
- [7. Tự thử](#7-tự-thử)
- [8. Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
- [9. Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Bài cuối làm hai việc

Mười ba bài trước cho từng mảnh: đo hiện trạng, kiếm, giữ, bảo vệ, nhận diện lừa đảo, đo khẩu vị,
chọn kênh. Bài cuối làm hai việc để những mảnh ấy thành một thứ dùng được:

1. **Đặt mục tiêu cho đúng** — bằng nguyên tắc **SMART** (Lesson 1, tr. 34–39). Một mục tiêu mơ hồ
   thì không bao giờ thành kế hoạch.
2. **Ráp mọi bài lại thành một bản kế hoạch** — Lesson 2 của sách làm việc này *"cùng Topi"*; khoá
   học làm bằng một bảng tính tự dựng, và chỉ ra rằng năm bước của app **không thêm gì mới** ngoài
   những bài bạn đã học.

Sách mở Unit 5 bằng một lời khuyên đáng làm trước khi đọc tiếp (tr. 34): *"viết ra toàn bộ các mục
tiêu về tài chính mà bạn muốn trong vòng từ 1 đến 10 năm tới"* — đừng hạn chế trí tưởng tượng, rồi
mới tinh chỉnh bằng SMART. Và một câu rất hay về động lực (tr. 34):

> *"Nếu 'Tại sao' đủ lớn thì 'Làm thế nào' trở nên đơn giản."*

---

## 2. SMART: nguồn gốc và năm chữ

Sách ghi nguồn đầy đủ, điều hiếm thấy (tr. 35): nguyên tắc **SMART** do **George T. Doran** nêu trong
*Management Review* tháng 11/1981, sau được **Robert S. Rubin** (ĐH Saint Louis) nghiên cứu tiếp, và
**Peter Drucker** cũng đề cập. Năm chữ, mỗi chữ là một phép thử cho mục tiêu:

| Chữ | Nghĩa | Ví dụ của sách | Phép thử |
| --- | --- | --- | --- |
| **S** — Specific | cụ thể | *"giàu có"* chưa đủ → *"giàu như Bill Gates với 114 tỷ USD"* | trả lời được 5W: What/Who/Where/When/Why? |
| **M** — Measurable | đo lường được | *"tích luỹ 100 triệu"*, *"để dành 10% thu nhập mỗi tháng"* | có **con số** chưa? |
| **A** — Attainable | khả thi | 114 tỷ USD khi 40 tuổi, lương 5tr/tháng → **không** khả thi | phù hợp xuất phát điểm và thời gian? |
| **R** — Relevant | phù hợp, có liên quan | 20 tuổi để dành 10%, nhắm tự do tài chính năm 35 tuổi | nó là **bước đệm** cho mục tiêu lớn hơn? |
| **T** — Time-bound | có thời hạn | đọc xong *Tài chính cá nhân 101*, mỗi ngày 1 bài, từ ngày… đến ngày… | có **deadline** chưa? |

Hai điểm sách nói rất hay, đáng giữ nguyên:

- **A — chia nhỏ để khả thi (tr. 37):** *"chia mục tiêu lớn thành các mục tiêu nhỏ hơn, sau đó chia
  mục tiêu nhỏ thành các công việc cần làm hàng ngày, hàng tuần… giống như đặt từng mảnh ghép, bức
  tranh lớn sẽ hoàn thành."* Đây chính là *"sửa hệ thống, không sửa người"* của
  [bài 10](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại):
  một việc nhỏ mỗi tuần dễ giữ hơn một quyết tâm lớn.
- **T — Định luật Parkinson (tr. 38):** *"công việc luôn mở rộng ra để lấp đầy khoảng thời gian sẵn
  có."* Không đặt deadline thì *"tâm trí bạn ngầm hiểu mục tiêu này cần 'cả đời'"*. Câu đùa của sách
  đáng nhớ: đặt thời hạn *"vô hạn"* thì *"nhiều khả năng bạn sẽ đạt được khi đã sang thế giới bên
  kia, người thân sẽ đốt rất nhiều tiền vàng gửi cho bạn."*

Chú ý ví dụ Bill Gates rất thông minh về mặt sư phạm: cùng một mục tiêu *"giàu như Bill Gates"* vừa
minh hoạ **S** (cụ thể tới 114 tỷ USD) lại vừa là ví dụ **A** (không khả thi với người lương 5tr).
Cùng một câu, hai chữ — cho thấy năm chữ không rời nhau mà lọc cùng một mục tiêu.

---

## 3. Áp SMART vào người ở bài 3

Lấy người đã theo suốt khoá (bài 3: thu nhập ròng 16tr/tháng, chi thiết yếu 10,37tr, để dành thực tế
2,48tr = 15,5%). Biến một câu mơ hồ thành một mục tiêu SMART, mỗi chữ dùng số của chính khoá học:

| Chữ | Mục tiêu mơ hồ → SMART |
| --- | --- |
| **S** | ~~"Tôi muốn tự do tài chính"~~ → *"Có đủ tài sản đầu tư để sống bằng lợi suất của nó, không phải đi làm để trả chi phí sống"* |
| **M** | Số đích = chi tiêu/năm ÷ lợi suất thực. Chi thiết yếu 124,4tr/năm ⟹ **1,56 tỷ** (lợi suất thực 8%) tới **3,46 tỷ** (~3,6%). *([Bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#6-bổ-sung-công-thức-tự-do-tài-chính-và-cái-giá-của-an-toàn) dùng số tròn 120tr của sách → 1,5–3,33 tỷ; đây dùng 124,4tr thực tế của người này.)* |
| **A** | Khả thi? Để dành 2,48tr/tháng thì phải **chia nhỏ**: trước hết quỹ khẩn cấp, rồi trả nợ lãi cao, rồi mới DCA vào danh mục |
| **R** | Là bước đệm cho an toàn gia đình và nghỉ hưu; mỗi tháng để dành đúng 15,5% là một mảnh ghép |
| **T** | Đặt mốc năm cụ thể — dùng *"bao lâu thì đến"* của [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách), rồi ghi ngày trên giấy |

### [bổ sung] Ví dụ R của sách dùng con số hơi lạc quan

Ví dụ **R** của sách (tr. 37) — *"20 tuổi… lợi nhuận 15%/năm… tự do tài chính năm 35 tuổi"* — có hai
chỗ cần đọc kỹ:

- **15%/năm là mức cao**, tương ứng một danh mục thiên về cổ phiếu, không phải *Cân bằng* (mà
  [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#5-bổ-sung-con-số-12-gánh-quá-nặng) chỉ ra kỳ vọng thật
  ~7,6%). Đặt mục tiêu trên 15% rồi thực tế chỉ đạt 8% thì đích lùi xa — nên **A** và **M** phải dùng
  con số kỳ vọng khớp với danh mục thật.
- *"10% thu nhập"* nên đọc là **10% thu nhập ròng**, vì các công thức đều chia trên ròng
  ([bài 6](bai_06_thue_thu_nhap_ca_nhan.md)). Sai mẫu số thì sai cả kế hoạch.

Không phải để bắt bẻ — mà để mục tiêu SMART thật sự *khả thi* (**A**) và *đo được đúng* (**M**), con
số đưa vào phải là con số thật, không phải con số đẹp.

---

## 4. [đã cắt] "5 bước cùng Topi" chính là cả khoá học

Lesson 2 của sách (tr. 39–40) là *"5 bước lập kế hoạch tự do tài chính **cùng TOPI**"* — hướng dẫn
nhập liệu vào app để nó vẽ mô phỏng và đề xuất danh mục. Khoá học cắt phần phụ thuộc app. Nhưng trước
khi cắt, hãy nhìn kỹ năm bước ấy — vì **mỗi bước đúng bằng một (vài) bài đã học**:

| Bước của sách (Topi) | Thật ra là | Đã học ở |
| --- | --- | --- |
| **1.** Xác định tình trạng tài chính (dòng tiền) | dòng tiền thu–chi | [bài 2](bai_02_do_hien_trang.md), [bài 3](bai_03_ghi_chep_chi_tieu.md) |
| **2.** Thông tin tài sản (bảng cân đối + tháp tài sản) | tài sản ròng, tháp tài sản | [bài 2](bai_02_do_hien_trang.md), [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md) |
| **3.** Xác định hồ sơ rủi ro | khẩu vị rủi ro | [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md) |
| **4.** Xác định mục tiêu và lập kế hoạch | mục tiêu SMART | **bài 14** (mục 2–3) |
| **5.** Mô phỏng và đề xuất danh mục | danh mục theo khẩu vị + số đích | [bài 13](bai_13_kenh_dau_tu.md), công thức [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md) |

> **Cái app làm không phải phép màu — nó chỉ nhập giúp năm thứ bạn đã tự tính được.** Và chính sách
> thừa nhận: bước 3 bảo *"xem lại 'Cách thiết lập hồ sơ rủi ro' trong các bài trước"*. Nghĩa là ngay
> tài liệu cũng biết nội dung nằm ở bài học, không nằm ở app.

Nên khoá học thay Lesson 2 bằng **một bảng tính tự dựng** — mục 5. Lý do vẫn là tuổi thọ (như
[bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#3-bốn-cách-đo-và-đã-cắt-vì-sao-bỏ-topi-thay-bằng-missouri)):
app đổi hay ngừng thì kế hoạch của bạn vẫn còn; một bảng tính thì bạn sở hữu mãi. Và bước 5 của
sách — *"Việc còn lại là tuân thủ một cách kỷ luật"* — thì đúng dù dùng công cụ nào.

---

## 5. Ráp một kế hoạch tự do tài chính, không cần app

Dựng lại năm bước bằng chính số của người ở bài 3, không cần cài gì:

```
   BƯỚC 1 — DÒNG TIỀN (bài 2, 3)
     thu ròng            16,00tr/tháng
     chi thiết yếu       10,37tr/tháng
     để dành thực tế      2,48tr/tháng  (15,5%)

   BƯỚC 2 — TÀI SẢN & THÁP (bài 2, 4)
     tài sản ròng: cộng tài sản trừ nợ (bài 2)
     tháp: lớp bảo vệ (quỹ khẩn cấp) còn TRỐNG -> ưu tiên số 1

   BƯỚC 3 — KHẨU VỊ (bài 12)
     làm bảng Missouri -> giả sử ra hồ sơ "Cân bằng"
     danh mục: 40% tiết kiệm · 25% trái phiếu · 5% vàng · 30% cổ phiếu (bài 13)

   BƯỚC 4 — MỤC TIÊU SMART (mục 3)
     "tự do tài chính": số đích = 124,4tr / lợi suất thực
                        = 1,56 tỷ (lạc quan 8%) ... 3,46 tỷ (thật ~3,6%)

   BƯỚC 5 — THỨ TỰ THỰC HIỆN, và KỶ LUẬT
```

Điều sách (và app) **không** xếp thứ tự, mà cả khoá đã dạy: **để dành 2,48tr/tháng đi đâu trước?**

| Ưu tiên | Việc | Vì sao | Bài |
| ---: | --- | --- | --- |
| 1 | **Quỹ khẩn cấp** 3–6 tháng chi | không có nó thì một cú sốc là phải vay 20% | [bài 9](bai_09_bao_ve.md) |
| 2 | **Trả hết nợ lãi cao** | trả nợ 20% = "sinh lời" 20% chắc chắn | [bài 8](bai_08_vay_va_tra_no.md) |
| 3 | **DCA vào danh mục** theo khẩu vị | giờ mới tới đầu tư, và mua đều, giữ dài | [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md), [bài 13](bai_13_kenh_dau_tu.md) |

Đó là toàn bộ kế hoạch: đo mình, vá lớp bảo vệ, dọn nợ đắt, rồi mới đầu tư đều đặn — và **giữ kỷ
luật** cho tới đích. Không app nào rút ngắn được ba bước đầu, và không app nào giữ kỷ luật thay bạn.

---

## 6. Toàn khoá trong một trang

Sách khép Class 1 bằng lời kết: đã xong *"Lập kế hoạch tài chính cá nhân"*, sang Class 2 giải ba bài
toán *"kiếm tiền, giữ tiền, tạo tiền"*. Khoá học này gộp cả hai tập theo đúng ba bài toán đó, và đây
là toàn bộ mười bốn bài nhìn từ trên xuống:

```
   ĐO MÌNH        bài 1 (là gì) · bài 2 (hiện trạng) · bài 3 (ghi chép) · bài 4 (tháp tài sản)

   KIẾM           bài 5 (vì sao được trả) · bài 6 (thuế -> tiền thật về tay)

   GIỮ            bài 7 (phân bổ) · bài 8 (nợ) · bài 9 (bảo vệ) ·
                  bài 10 (hành vi) · bài 11 (lừa đảo)

   ĐẦU TƯ         bài 12 (rủi ro & khẩu vị) · bài 13 (kênh)

   RÁP LẠI        bài 14 (mục tiêu SMART + kế hoạch)  <- bạn đang ở đây
```

Nhìn lại luận điểm trung tâm của cả khoá ([bài 0](bai_00_bat_dau_tu_dau.md)): *"số tiền bạn kiếm được
không quan trọng bằng số tiền bạn giữ được"* — bảy trong mười bốn bài nói về **giữ**, chỉ hai bài nói
về **đầu tư**. Kế hoạch tự do tài chính không bắt đầu từ việc chọn mã, nó bắt đầu từ việc **biết mình
đang ở đâu, giữ được bao nhiêu, và chịu được rủi ro tới đâu** — rồi mới tới chỗ để tiền.

Giấy bút của bạn đâu? Như sách nói ở tr. 39: **viết ra mục tiêu tài chính của bạn ngay thôi.**

---

## 7. Tự thử

Sửa [`thuc_hanh/bai-14-ke-hoach.py`](../thuc_hanh/bai-14-ke-hoach.py) rồi chạy lại.

1. **Một mục tiêu SMART của bạn.** Viết một mục tiêu tài chính thật, rồi chấm nó theo năm chữ. Chữ
   nào bạn còn để mơ hồ? Sửa cho đủ cả năm.

2. **Số đích của bạn.** Lấy chi tiêu/năm theo phong cách sống bạn muốn, chia cho lợi suất thực. Dùng
   lần lượt 8% và 3,6% (mục 3) — hai con số cách nhau bao nhiêu? Con số nào bạn nên lập kế hoạch theo?

3. **Bao lâu thì đến.** Với mức để dành hàng tháng của bạn và số đích ở câu 2, dùng công thức "bao
   lâu thì đến" của [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md). Đặt năm đó làm chữ **T** của mục tiêu.

4. **Thứ tự của bạn.** Bạn đã có quỹ khẩn cấp chưa? Còn nợ lãi cao không? Vẽ thứ tự ba ưu tiên ở mục
   5 cho hoàn cảnh của bạn — tháng này đồng để dành đầu tiên nên đi đâu?

5. **Bảng tính thay app.** Dựng một bảng năm bước (mục 5) cho chính bạn. Nó thiếu thông tin nào bạn
   chưa có? Mỗi ô thiếu ứng với một bài bạn cần quay lại làm bài tập.

---

## 8. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| SMART | SMART | Năm phép thử cho mục tiêu: Cụ thể, Đo được, Khả thi, Phù hợp, Có thời hạn — C1 tr. 35 |
| Specific | Specific | Cụ thể; trả lời được 5W — C1 tr. 35 |
| Measurable | Measurable | Đo lường được, có con số — C1 tr. 36 |
| Attainable | Attainable / Achievable | Khả thi; chia mục tiêu lớn thành việc hàng ngày/tuần — C1 tr. 36 |
| Relevant | Relevant / Realistic | Phù hợp; là bước đệm cho mục tiêu lớn hơn — C1 tr. 37 |
| Time-bound | Time-bound / Time-based | Có thời hạn; không có deadline thì thành "cả đời" — C1 tr. 38 |
| Định luật Parkinson | Parkinson's law | Công việc mở rộng để lấp đầy thời gian sẵn có — C1 tr. 38 |
| 5W | 5W | What, Who, Where, When, Why — bộ câu hỏi cụ thể hoá mục tiêu — C1 tr. 36 |
| Số tiền tự do tài chính | FI number | Chi tiêu/năm ÷ lợi suất thực; số tài sản đủ để sống bằng lợi suất — bài 1, 12 |

---

## 9. Câu hỏi tự kiểm tra

1. Bài cuối làm hai việc gì?
2. SMART là viết tắt của năm chữ nào? Ai nêu ra và năm nào?
3. Với mỗi chữ, viết một phép thử một câu.
4. Ví dụ "giàu như Bill Gates 114 tỷ USD" minh hoạ chữ nào? Vì sao nó cũng là ví dụ cho chữ A?
5. Định luật Parkinson là gì, và nó liên quan chữ T thế nào?
6. Biến "tôi muốn tự do tài chính" thành một mục tiêu SMART với số của người bài 3.
7. Vì sao ví dụ R của sách (15%/năm) hơi lạc quan? "10% thu nhập" nên đọc là gì?
8. Năm bước "cùng Topi" của sách ứng với những bài nào đã học?
9. App làm được gì mà bạn không tự làm được? (Gợi ý: gần như không.)
10. Để dành mỗi tháng nên đi đâu trước: quỹ khẩn cấp, trả nợ, hay đầu tư? Vì sao thứ tự đó?
11. Vì sao kế hoạch tự do tài chính không bắt đầu từ việc chọn mã cổ phiếu?
12. Bảy trong mười bốn bài nói về việc gì? Điều đó phản ánh luận điểm trung tâm nào của khoá?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 14 — MỤC TIÊU SMART VÀ RÁP LẠI THÀNH KẾ HOẠCH     C1 tr. 34-40      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  BÀI CUỐI: (1) đặt mục tiêu đúng bằng SMART  (2) ráp cả khoá thành 1 KH ║
║     "Nếu TẠI SAO đủ lớn thì LÀM THẾ NÀO trở nên đơn giản" (tr.34)       ║
║                                                                          ║
║  SMART (Doran 1981)                                                      ║
║     S cụ thể      -> 5W; "giàu như Bill Gates 114 tỷ USD"              ║
║     M đo được     -> có CON SỐ; "để dành 10% thu nhập"                 ║
║     A khả thi     -> chia lớn thành việc hàng ngày/tuần                ║
║     R phù hợp     -> là BƯỚC ĐỆM cho mục tiêu lớn hơn                  ║
║     T thời hạn    -> Parkinson: không deadline = "cả đời"              ║
║                                                                          ║
║  ÁP VÀO NGƯỜI BÀI 3 (ròng 16tr, chi 10,37tr, để dành 2,48tr)           ║
║     số đích = 124,4tr / lợi suất thực                                   ║
║        = 1,56 tỷ (lạc quan 8%) ... 3,46 tỷ (thật ~3,6%, bài 12)        ║
║     [bổ sung] ví dụ R của sách (15%/năm) hơi cao; "10%" = 10% RÒNG      ║
║                                                                          ║
║  [đã cắt] "5 BƯỚC CÙNG TOPI" = CHÍNH LÀ CẢ KHOÁ HỌC:                    ║
║     1 dòng tiền -> bài 2,3   2 tài sản/tháp -> bài 2,4                  ║
║     3 khẩu vị -> bài 12      4 mục tiêu -> bài 14                       ║
║     5 danh mục + số đích -> bài 13 + công thức bài 12                  ║
║     app chỉ NHẬP GIÚP thứ bạn đã tự tính -> thay bằng BẢNG TÍNH tự dựng ║
║                                                                          ║
║  THỨ TỰ ĐỒNG ĐỂ DÀNH (điều app không xếp):                              ║
║     1) QUỸ KHẨN CẤP (bài 9)  2) TRẢ NỢ LÃI CAO (bài 8)                 ║
║     3) DCA VÀO DANH MỤC (bài 12,13) -> rồi GIỮ KỶ LUẬT                 ║
║                                                                          ║
║  TOÀN KHOÁ: ĐO MÌNH (1-4) · KIẾM (5-6) · GIỮ (7-11) · ĐẦU TƯ (12-13)   ║
║     · RÁP LẠI (14)                                                      ║
║     7/14 bài nói về GIỮ -> "giữ được quan trọng hơn kiếm được"         ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1***, Waka.vn. **Unit 5 — *Mục tiêu và lập kế hoạch*, Lesson 1–2
  (tr. 34–40):** viết ra mục tiêu 1–10 năm và *"Nếu Tại sao đủ lớn…"* (tr. 34); nguồn gốc SMART —
  George T. Doran, *Management Review* 11/1981, Robert S. Rubin, Peter Drucker (tr. 35); năm chữ với
  ví dụ Bill Gates 114 tỷ USD, 5W, *"tích luỹ 100 triệu"*, ví dụ R *"20 tuổi… 15%/năm… tự do năm 35"*,
  Định luật Parkinson (tr. 35–39); *"5 bước lập kế hoạch tự do tài chính cùng TOPI"* và lời kết
  *"kiếm tiền, giữ tiền, tạo tiền"* (tr. 39–40, Lời kết) — đều chép từ đây.
- **[đã cắt] Topi → bảng tính tự dựng.** Khoá học thay Lesson 2 (hướng dẫn app Topi, tr. 39–40) bằng
  một bảng năm bước tự dựng từ chính các bài trước — lý do là tuổi thọ, giống
  [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#3-bốn-cách-đo-và-đã-cắt-vì-sao-bỏ-topi-thay-bằng-missouri).
  Chính sách cũng chỉ về *"các bài trước"* ở bước 3, xác nhận nội dung nằm ở bài học.
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-14-ke-hoach.py`](../thuc_hanh/bai-14-ke-hoach.py).
  Bảng kế hoạch và số đích do tệp này tính, chạy hai lần ra giống hệt nhau. Công thức một dòng để tự
  kiểm: số tiền tự do tài chính `= chi tiêu năm / (lợi suất − lạm phát)`.
- **Số liệu lấy nguyên từ bài trước:** thu nhập ròng 16tr, chi thiết yếu 10,37tr (124,4tr/năm), để
  dành thực tế 2,48tr (15,5%) — [bài 3](bai_03_ghi_chep_chi_tieu.md), [bài 7](bai_07_phan_bo_thu_nhap.md);
  số đích 1,56 tỷ và 3,46 tỷ tính bằng công thức và lợi suất thực của
  [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md); thứ tự ưu tiên từ [bài 8](bai_08_vay_va_tra_no.md),
  [bài 9](bai_09_bao_ve.md).
- **Liên hệ chéo (bài này ráp cả khoá):**
  - Đo hiện trạng, tài sản ròng: [bài 2](bai_02_do_hien_trang.md) · ghi chép: [bài 3](bai_03_ghi_chep_chi_tieu.md) ·
    tháp tài sản: [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md).
  - Thu nhập ròng và mẫu số của mọi công thức: [bài 6](bai_06_thue_thu_nhap_ca_nhan.md).
  - Thứ tự để dành — quỹ khẩn cấp trước, trả nợ, rồi đầu tư:
    [bài 8](bai_08_vay_va_tra_no.md), [bài 9](bai_09_bao_ve.md).
  - Chia nhỏ và kỷ luật là "sửa hệ thống":
    [bài 10 mục 8](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại).
  - Khẩu vị, công thức tự do tài chính, cái giá của an toàn:
    [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md).
  - Danh mục bốn kênh, DCA vào ETF chỉ số:
    [bài 13](bai_13_kenh_dau_tu.md).
  - "Bao lâu thì đến":
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).

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
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | [**[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai](bai_10_tai_chinh_hanh_vi.md) | ngoài sách | 2 |
| 11 | [Nhận diện lừa đảo: Ponzi và CFD](bai_11_nhan_dien_lua_dao.md) | C2 tr. 47–57 | 1 |
| 12 | [Rủi ro, khẩu vị rủi ro, phân bổ tài sản](bai_12_rui_ro_khau_vi_phan_bo.md) | C1 tr. 25–33 | 1 |
| 13 | [Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF](bai_13_kenh_dau_tu.md) | C2 tr. 58–67 | 2 |
| **14** | **Mục tiêu SMART và ráp lại thành kế hoạch** ← *bạn đang ở đây* | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
