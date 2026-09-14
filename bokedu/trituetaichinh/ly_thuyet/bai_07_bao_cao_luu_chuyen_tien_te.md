# Bài 7 — Báo cáo lưu chuyển tiền tệ

> [!info] Về bài này
> Bài học dựng từ **Phần IV — Tiền mặt là nhất**: chương 16 *Ngôn ngữ của báo cáo lưu chuyển tiền tệ*
> (PDF tr. 121–124), chương 17 *Tiền mặt kết nối với mọi thứ khác ra sao* (PDF tr. 125–135), chương 18
> *Tại sao tiền mặt lại quan trọng* (PDF tr. 136–141).
>
> ⭐ **Vòng 1, chương dùng được ngay.** [Bài 6](bai_06_loi_nhuan_khac_tien_mat.md) đã chỉ ra lợi nhuận
> khác tiền mặt. Bài này dựng **báo cáo đo cái khác biệt đó** — và cho thấy nó **suy ra được** từ hai
> báo cáo kia.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).
>
> **Cần đọc trước:** [Bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md) ·
> [Bài 6](bai_06_loi_nhuan_khac_tien_mat.md) — đẳng thức ở mục 4 của bài 5 chính là bản thu nhỏ của
> thuật toán ở mục 1 bài này.
> ⚙️ **Code:** [`thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py`](../thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py)
> — mục 1 **viết chương 17 thành một hàm chạy được**: `dung_lctt()` nhận vào hai bảng cân đối, con số
> khấu hao và con số cổ tức, rồi **sinh ra cả báo cáo lưu chuyển tiền tệ**. Nó không hề "biết" báo cáo
> gốc — mà cả 13 dòng đều khớp.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vì sao báo cáo này khó đọc — ba lý do, và lý do thứ ba là lý do thật](#1-vì-sao-báo-cáo-này-khó-đọc--ba-lý-do-và-lý-do-thứ-ba-là-lý-do-thật)
- [2. Ba hạng mục, và câu hỏi gắn với từng hạng mục](#2-ba-hạng-mục-và-câu-hỏi-gắn-với-từng-hạng-mục)
- [3. Công ty khởi nghiệp — thuật toán nhỏ nhất kiểm được bằng tay](#3-công-ty-khởi-nghiệp--thuật-toán-nhỏ-nhất-kiểm-được-bằng-tay)
- [4. Thuật toán của chương 17](#4-thuật-toán-của-chương-17)
- [5. Quy tắc dấu — chỗ gây nhầm nhất của cả báo cáo](#5-quy-tắc-dấu--chỗ-gây-nhầm-nhất-của-cả-báo-cáo)
- [6. Ba hạng mục nói gì về công ty mẫu](#6-ba-hạng-mục-nói-gì-về-công-ty-mẫu)
- [7. Bốn chỗ sách in sai trong chính chương 17](#7-bốn-chỗ-sách-in-sai-trong-chính-chương-17)
- [8. Dòng lưu chuyển tiền tự do](#8-dòng-lưu-chuyển-tiền-tự-do)
- [9. "Không nhiều chỗ" không phải "không có chỗ"](#9-không-nhiều-chỗ-không-phải-không-có-chỗ)
- [10. Bốn đòn bẩy của nhà quản lý](#10-bốn-đòn-bẩy-của-nhà-quản-lý)
- [11. Đối chiếu Việt Nam](#11-đối-chiếu-việt-nam)
- [12. Tự thử](#12-tự-thử)
- [13. Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
- [14. Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vì sao báo cáo này khó đọc — ba lý do, và lý do thứ ba là lý do thật

Chương 16 mở bằng một kỳ vọng rồi bác nó ngay:

> [!quote]
> *"Chúng ta thường tưởng rằng báo cáo lưu chuyển tiền tệ sẽ **dễ đọc**. Vì tiền mặt là khoản tiền có
> thực, nên **không có những giả định và ước tính lồng trong các con số**… Tuy vậy, thực tế là chúng ta
> sẽ thấy rằng gần như tất cả những nhà quản lý không có kiến thức tài chính sẽ phải mất một thời gian
> mới hiểu được nó."* — ch. 16 · PDF tr. 121

| # | lý do | mục xử lý |
| ---: | --- | --- |
| 1 | *"báo cáo này luôn được chia thành nhiều hạng mục, và **nhãn tên** trong các hạng mục có thể khó hiểu"* | [mục 2](#2-ba-hạng-mục-và-câu-hỏi-gắn-với-từng-hạng-mục) |
| 2 | *"những **con số âm dương** không phải lúc nào cũng rõ ràng"* | [mục 5](#5-quy-tắc-dấu--chỗ-gây-nhầm-nhất-của-cả-báo-cáo) |
| 3 | *"ta rất khó thấy được **mối quan hệ** giữa báo cáo lưu chuyển tiền tệ và hai báo cáo tài chính kia"* | [mục 4](#4-thuật-toán-của-chương-17) |

Về lý do 2, sách nêu đúng cái bẫy khiến ai cũng khựng lại:

> [!quote]
> *"Trong một mục điển hình có thể xuất hiện dòng **'(tăng)/giảm khoản phải thu'** sau một con số âm
> hoặc con số dương. **Như vậy, đó là tăng hay giảm?**"* — ch. 16 · PDF tr. 121

Và sách chọn giải quyết lý do 3 trước, vì hai lý do kia dễ hơn nhiều một khi bạn thấy được mối nối.

---

## 2. Ba hạng mục, và câu hỏi gắn với từng hạng mục

| hạng mục | gồm những gì | câu hỏi sách gắn vào |
| --- | --- | --- |
| **Hoạt động kinh doanh** (HĐKD) | tiền khách trả, tiền trả lương, trả nhà cung cấp, trả chủ nhà — *"tất cả các nguồn tiền mặt khác để cánh cửa doanh nghiệp luôn mở"* | *"xét trên nhiều phương diện là **con số quan trọng nhất** cho biết tình trạng của doanh nghiệp"* |
| **Hoạt động đầu tư** | đầu tư **do doanh nghiệp**, không phải do chủ doanh nghiệp. Lớn nhất là mua/bán tài sản | *"cho biết doanh nghiệp **dành ra bao nhiêu để đầu tư cho tương lai**"* |
| **Hoạt động tài chính** | vay và trả nợ; giao dịch với cổ đông — góp vốn, mua lại cổ phiếu, trả cổ tức | *"cho biết doanh nghiệp **phụ thuộc như thế nào vào nguồn tài chính bên ngoài**"* |

> [!note]
> Sách còn đùa một câu về nhãn tên: *"nhiều kế toán viên không thể nói 'hoạt động,' họ phải nói 'hoạt
> động kinh doanh'"* (PDF tr. 121). Nhãn khác nhau, nội dung như nhau.

Ba câu hỏi trên là công cụ đọc, và [mục 6](#6-ba-hạng-mục-nói-gì-về-công-ty-mẫu) sẽ chạy cả ba trên
số thật. Trước đó, hai điều đáng nhớ về từng hạng mục:

**① HĐKD khoẻ có nghĩa gì.** *"Một doanh nghiệp có dòng lưu chuyển tiền từ hoạt động kinh doanh luôn
khoẻ mạnh rất có thể có tiềm năng sinh lợi nhuận, và nó cũng có thể làm tốt việc **biến lợi nhuận thành
tiền mặt**. Ngoài ra… doanh nghiệp có thể rót thêm vốn để tăng trưởng hơn nữa, **mà không cần phải vay
mượn hay bán cổ phiếu**."* — ch. 16 · PDF tr. 122

**② Đầu tư thấp không phải lúc nào cũng là tiết kiệm.** *"Nếu con số thấp… có thể doanh nghiệp không hề
đầu tư; ban quản lý có thể đang coi hoạt động kinh doanh là **'con bò sữa'**, nên tiếp tục vắt kiệt
nguồn tiền mặt mà nó tạo ra, thay vì đầu tư để nó có thể phát triển."* — ch. 16 · PDF tr. 122–123

> [!warning]
> Nhưng sách cũng tự rào: *"cách tính cao hay thấp sẽ còn phụ thuộc vào loại hình kinh doanh. Chẳng
> hạn, các doanh nghiệp dịch vụ thường ít đầu tư vào tài sản hơn khối doanh nghiệp sản xuất."*

---

## 3. Công ty khởi nghiệp — thuật toán nhỏ nhất kiểm được bằng tay

Trước khi làm doanh nghiệp thật, sách chạy thử một ví dụ tí hon. Cái hay của nó: **kết quả kiểm lại
được bằng một đường hoàn toàn khác.**

Doanh thu 100 · COGS 50 · chi phí khác 15 · khấu hao 10 → **lợi nhuận thuần 25**. Toàn bộ doanh thu nằm
trong phải thu; toàn bộ COGS nằm trong phải trả.

> [!quote]
> **Nguyên tắc chính:** *"nếu **tài sản tăng, thì tiền mặt giảm** – vì vậy chúng ta sẽ trừ phần tăng
> thêm này khỏi thu nhập thuần. Với bên nợ thì ngược lại. **Nếu nợ tăng thì tiền mặt cũng tăng** – vì
> vậy chúng ta thêm phần tăng thêm vào thu nhập thuần."* — ch. 17 · PDF tr. 128

| | |
| --- | ---: |
| Bắt đầu với lợi nhuận thuần | 25 |
| Trừ mức tăng trong phải thu | (100) |
| Cộng mức tăng trong phải trả | 50 |
| Cộng thêm khấu hao | 10 |
| **= Chênh lệch tiền mặt thuần** | **(15)** |

⭐ Sách kiểm bằng đường khác: *"Bạn có thể thấy phép toán trên là đúng vì **khoản chi tiêu tiền mặt duy
nhất** trong kỳ của công ty là 15 đô-la chi phí hoạt động."* Hai đường độc lập, cùng ra −15. Chốt bằng
`assert`.

> [!warning]
> Và sách cảnh báo ngay đừng quen tay: *"trong hoạt động kinh doanh **thực tế**, bạn **không thể** xác
> nhận kết quả chỉ đơn giản bằng theo dõi thông thường."* Ví dụ này kiểm được vì nó chỉ có **một** dòng
> tiền duy nhất.

> [!note]
> Vì sao bắt đầu từ lợi nhuận thuần chứ không từ đâu khác? *"Nếu mọi giao dịch đều được thực hiện bằng
> tiền mặt, và nếu không có khoản chi tiêu phi tiền mặt nào như khấu hao, **lợi nhuận thuần và dòng lưu
> chuyển tiền từ hoạt động kinh doanh sẽ là một**."* (PDF tr. 126). Cả báo cáo này chỉ là danh sách những
> chỗ hai con số ấy **tách nhau ra**.

---

## 4. Thuật toán của chương 17

Chương 17 hứa một điều nghe khó tin:

> [!quote]
> *"Bạn có thể **tính toán số liệu cho báo cáo lưu chuyển tiền tệ chỉ bằng cách nhìn vào báo cáo kết quả
> kinh doanh và bảng cân đối kế toán**."* — ch. 17 · PDF tr. 125

Và giải thích vì sao điều đó **phải** đúng:

> [!quote]
> *"Tất cả những quy tắc, giả định và ước tính này đều phải cung cấp cho chúng ta thông tin hữu dụng về
> **thế giới thực**. Và vì trong tài chính, **thế giới thực được đại diện bởi tiền mặt**, nên bảng cân
> đối kế toán và báo cáo kết quả kinh doanh **phải có một mối quan hệ logic** nào đó với báo cáo lưu
> chuyển tiền tệ."* — ch. 17 · PDF tr. 125

Đó là một **thuật toán**, nên bài này viết nó ra thành hàm. `dung_lctt()` nhận vào **hai bảng cân đối,
con số khấu hao và con số cổ tức** — và không gì khác:

| | DỰNG LẠI | SÁCH IN | khớp? |
| --- | ---: | ---: | :---: |
| **HOẠT ĐỘNG KINH DOANH** | | | |
| Lợi nhuận thuần | 248 | 248 | ✓ |
| Khấu hao | 239 | 239 | ✓ |
| Khoản phải thu | (108) | (108) | ✓ |
| Hàng tồn kho | 244 | 244 | ✓ |
| Tài sản ngắn hạn khác | (18) | (18) | ✓ |
| Khoản phải trả | (107) | (107) | ✓ |
| **→ Tổng HĐKD** | **498** | **498** | |
| **HOẠT ĐỘNG ĐẦU TƯ** | | | |
| Đất đai, nhà xưởng và thiết bị | (205) | (205) | ✓ |
| Tài sản dài hạn khác | 20 | 20 | ✓ |
| **→ Tổng đầu tư** | **(185)** | **(185)** | |
| **HOẠT ĐỘNG TÀI CHÍNH** | | | |
| Hạn mức tín dụng | (50) | (50) | ✓ |
| Khoản phải trả của nợ dài hạn | 1 | 1 | ✓ |
| Nợ dài hạn | (121) | (121) | ✓ |
| Nợ dài hạn khác | 34 | 34 | ✓ |
| Cổ tức thanh toán | (166) | (166) | ✓ |
| **→ Tổng tài chính** | **(302)** | **(302)** | |
| **THAY ĐỔI TRONG TIỀN** | **11** | **11** | |
| Tiền đầu kỳ *(bảng cân đối 2004)* | 72 | | |
| **Tiền cuối kỳ** | **83** | **83** | ✓ |

⭐ **13 dòng, không một dòng nào lệch.** Sách nói đúng: *"Quả là một bài tập phức tạp! Nhưng bạn có thể
thấy tất cả những **liên kết này đẹp đẽ và tinh vi** đến độ nào."*

> [!note] Lưu ý 1 của sách — vì sao dòng PPE cần điều chỉnh.
> PPE trên sổ sách **giảm 34** (2.264 → 2.230).
> Nhưng đó không phải doanh nghiệp bán bớt tài sản: nó đã **chi ra 205 tiền thật**, chỉ là khấu hao 239 ăn
> mất nhiều hơn thế.

> [!note]
> **capex = khấu hao + thay đổi PPE = 239 + (−34) = 205**

Sách minh hoạ bằng đội xe tải 100.000, khấu hao 10.000/năm → cuối năm dòng PPE là 90.000. *"Khấu hao là
một khoản chi tiêu phi tiền mặt, và vì chúng ta đang cố tìm đến một con số tiền mặt, nên chúng ta phải
**'bỏ qua' khoản này bằng cách cộng nó trở lại**."* (PDF tr. 133)

> [!note] Lưu ý 2 — cổ tức.
> 2,24 đô-la/cổ phiếu × 74 triệu cổ phiếu ≈ **166 triệu**. Và 248 − 166 = **82** —
> đúng bằng mức tăng vốn chủ sở hữu ở [bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md) mục 3. Sách rút ra
> một hệ quả gọn: *"Nếu doanh nghiệp **không trả cổ tức hay bán cổ phiếu**, thì khi đó dòng lưu chuyển
> tiền cho hoạt động tài chính **sẽ là 0**."*

---

## 5. Quy tắc dấu — chỗ gây nhầm nhất của cả báo cáo

Toàn bộ câu trả lời cho câu hỏi *"đó là tăng hay giảm?"* nằm trong hai dòng quy tắc của mục 3. Kiểm trên
từng dòng thật của công ty mẫu:

| dòng trên bảng cân đối | 2004 | 2005 | đổi | tiền | quy tắc |
| --- | ---: | ---: | ---: | ---: | --- |
| Khoản phải thu | 1.204 | 1.312 | +108 | **−108** | TS tăng → tiền giảm |
| Hàng tồn kho | 1.514 | 1.270 | −244 | **+244** | TS giảm → tiền tăng |
| Tài sản ngắn hạn khác | 67 | 85 | +18 | **−18** | TS tăng → tiền giảm |
| Khoản phải trả | 1.129 | 1.022 | −107 | **−107** | nợ giảm → tiền giảm |

⭐ **Dấu của dòng trên báo cáo luôn NGƯỢC dấu thay đổi của tài sản, và CÙNG dấu thay đổi của nợ.** Chốt
bằng `assert` trên từng dòng.

> [!example] Mẹo đọc nhanh
> khi gặp dòng *"(tăng)/giảm"* mà không biết dấu nào ứng với gì: dòng đó nằm ở hạng
> mục HĐKD, nên nó là một **điều chỉnh tiền mặt**. Số **dương luôn nghĩa là tiền tăng**. Còn bản thân
> khoản mục trên bảng cân đối tăng hay giảm thì suy ngược ra — tài sản thì ngược dấu, nợ thì cùng dấu.

📌 Sách dẫn đúng chuỗi giao dịch làm nền cho quy tắc này (PDF tr. 125–126): bán chịu 100 → phải thu +100
**và** doanh thu +100; khách trả → phải thu −100, tiền +100. Mua 100 tồn kho → phải trả +100 và tồn kho
+100; trả hoá đơn → phải trả −100, tiền −100. *"**Hầu hết các giao dịch cuối cùng đều sẽ tìm đường thể
hiện trên cả ba báo cáo.**"*

---

## 6. Ba hạng mục nói gì về công ty mẫu

### ① HĐKD

| | |
| --- | ---: |
| tiền từ HĐKD | 498 |
| lợi nhuận thuần | 248 |
| **tỷ lệ chuyển đổi** | **2,01 lần** |

> [!quote]
> *"Dòng lưu chuyển tiền từ hoạt động kinh doanh **cao hơn nhiều** so với thu nhập thuần. Hàng tồn kho
> giảm, vì vậy có thể giả định rằng doanh nghiệp **đang thắt chặt hoạt động**."* — ch. 18 · PDF tr. 136

> [!warning]
> Đúng, nhưng cần đọc kỹ hơn một bước: **riêng khoản tồn kho giảm 244 đã đóng góp 49% tiền từ HĐKD** —
> và đó là **nguồn chỉ dùng được một lần**. Năm sau không thể giảm thêm 244 nữa. Tỷ lệ 2,01 lần này **không
> bền**.

### ② Đầu tư

| | |
| --- | ---: |
| capex | 205 |
| khấu hao | 239 |
| **capex / khấu hao** | **0,86 lần** |

> [!quote]
> *"**Khấu hao vượt xa đầu tư mới**, điều này làm chúng ta phải băn khoăn không rõ ban quản lý có tin
> rằng doanh nghiệp có tương lai hay không."* — ch. 18 · PDF tr. 136

> [!warning] Chữ "vượt xa" hơi quá tay.
> Khấu hao 239 so với capex 205 — vượt **34**, tức **17%**. Với nhịp
> này, nền tài sản PPE 2.230 phải mất **66 năm** mới mòn hết. Hướng thì sách nói đúng, nhưng độ lớn thì là
> "vượt **nhẹ**", không phải "vượt xa".

### ③ Tài chính

| | |
| --- | ---: |
| Hạn mức tín dụng | (50) |
| Khoản phải trả của nợ dài hạn | 1 |
| Nợ dài hạn | (121) |
| Nợ dài hạn khác | 34 |
| **→ trả bớt nợ ròng** | **(136)** |
| Cổ tức | **(166)** |
| **→ Tổng** | **(302)** |

⭐ Cả ba đều âm → doanh nghiệp **không gọi vốn từ bên ngoài một đồng nào**. Nó dùng tiền từ hoạt động để
trả bớt 136 nợ **và** chia 166 cổ tức. Đó chính là câu trả lời cho câu hỏi của
[bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md) mục 7 — *"huy động vốn hay tự làm ra tiền?"* — nhìn từ
báo cáo thứ ba.

Sách đọc thêm một tầng: cổ tức hậu hĩnh trong khi đầu tư mỏng *"có thể cho thấy rằng doanh nghiệp **coi
trọng tiềm năng tạo ra tiền mặt hơn là tương lai của mình**"* (PDF tr. 136). Rồi tự rào ngay: *"tất cả
những điều trên đều là **giả thuyết**; để biết sự thật, bạn phải nắm được thêm thông tin về doanh
nghiệp."*

---

## 7. Bốn chỗ sách in sai trong chính chương 17

Chương 17 in lại cả ba báo cáo để bạn đối chiếu. Vì thuật toán ở mục 4 chạy được, ta chỉ ra được **chính
xác** chỗ nào hỏng:

| chỗ | khoản mục | sách in | đúng ra | vì sao |
| --- | --- | ---: | ---: | --- |
| tr. 130 | Tổng tài sản 2005 | 5.133 | **5.193** | cộng cột ra 5.193; chính dòng dưới (nợ + vốn chủ) ở tr. 131 in **đúng** 5.193 |
| **tr. 132** | **dòng 8: *"khoản phải trả giảm…"*** | **10** | **107** | 1.129 − 1.022 = 107; và chính báo cáo ở tr. 134 in (107). **Rớt một chữ số** |
| tr. 135 | Tổng tiền từ đầu tư | 185 | **−185** | phải âm; nếu không 498 − 185 − 302 không ra 11 |
| tr. 135 | Tổng tiền từ tài chính | 302 | **−302** | cùng lý do |

⭐ **Chỗ thứ hai chỉ lộ ra ở bài này** — không cách nào thấy nó bằng cách đọc, mà phải dựng lại được báo
cáo ở mục 4 rồi đối chiếu từng dòng. Bảng *"bước thực hiện"* ở tr. 132 có **12 dòng** *(sách không đánh
số, đây là thứ tự xuất hiện)*; **dòng thứ 8 ghi một con số, còn báo cáo ở tr. 134 ghi con số khác** — cùng
một chương, cách nhau hai trang. Nó đã được đưa vào sổ tổng kết ở
[bài 12 mục 9](bai_12_to_chuc_co_tri_tue_tai_chinh.md#9-sổ-tổng-kết--mọi-chỗ-sách-in-sai).

> [!example] Bài học đọc báo cáo:
> khi hai chỗ trong **cùng một tài liệu** nói hai con số khác nhau, đừng đoán
> cái nào đúng. **Cộng cột lại.** Ở đây chỉ có một cách làm 498 − 185 − 302 = 11 khớp với thay đổi tiền
> mặt trên bảng cân đối, và đó là con số đúng.

---

## 8. Dòng lưu chuyển tiền tự do

> [!quote]
> *"**EBITDA không còn** là 'thước đo yêu thích để theo dõi' của Phố Wall nữa. Thước đo hiện đang thu
> hút được sự quan tâm là **dòng lưu chuyển tiền tự do**. Một số doanh nghiệp đã theo dõi nó từ nhiều
> năm. **Berkshire Hathaway** của Warren Buffett là ví dụ đình đám nhất, dù Buffett gọi thước đo này là
> **thu nhập chủ sở hữu**."* — ch. 18 · PDF tr. 139

Công thức thì một dòng: *"lấy lưu chuyển tiền thuần từ hoạt động kinh doanh **trừ đi** con số được đầu
tư vào thiết bị thuộc hạng mục đầu tư cơ bản. **Tất cả chỉ có vậy.**"*

| | triệu $ |
| --- | ---: |
| Tiền từ hoạt động kinh doanh | 498 |
| − Đầu tư cơ bản (capex) | (205) |
| **= DÒNG LƯU CHUYỂN TIỀN TỰ DO** | **293** |
| − Cổ tức đã trả | (166) |
| **= Còn lại để trả nợ hoặc tích luỹ** | **127** |

⭐ Đọc ba con số này cạnh nhau:

- **FCF 293 lớn hơn lợi nhuận thuần 248** (1,18 lần) — doanh nghiệp thu về nhiều tiền hơn con số lợi
  nhuận nó báo cáo.
- **Cổ tức 166 ăn hết 57% FCF** — cao, nhưng vẫn trong khả năng.
- Còn **127** để trả nợ. Mà thực tế nó đã trả **136** — nhiều hơn phần còn lại; phần chênh lấy từ tồn
  kho giảm. **Đó là lý do khoản tồn kho giảm 244 lại quan trọng đến thế.**

> [!note]
> Sách kể thước đo này bắt được gì mà các thước đo khác không bắt được:

> [!quote]
> *"Đáng lẽ nó đã có thể giúp chúng ta trong suốt thời kỳ bùng nổ điên cuồng các công ty **dot-com**,
> khi mà nhiều doanh nghiệp mới thành lập có dòng lưu chuyển tiền từ HĐKD **âm** và dòng lưu chuyển tiền
> từ đầu tư **khổng lồ**. Dòng lưu chuyển tiền tự do của các doanh nghiệp này khi đó **âm nặng**, và nhu
> cầu tiền mặt của họ được đáp ứng chỉ vì các nhà đầu tư **ném tiền vào đống lửa đang bùng cháy**. Gần
> như là người duy nhất đơn độc dựa vào dòng lưu chuyển tiền tự do khi đó, Buffett **chưa bao giờ đầu tư
> vào những doanh nghiệp như vậy. Thật bất ngờ!**"* — ch. 18 · PDF tr. 140

Ba thứ mà FCF khoẻ và đang tăng nói lên: doanh nghiệp **có nhiều phương án** (trả nợ, mua đối thủ, chia
cổ tức); bạn và đồng nghiệp **tập trung được vào công việc** thay vì lo bảng lương và huy động vốn; và
Phố Wall **nhìn cổ phiếu ưu ái hơn**.

---

## 9. "Không nhiều chỗ" không phải "không có chỗ"

Sách khen báo cáo này sạch hơn hai báo cáo kia — rồi rào lại ngay:

> [!quote]
> *"Ở báo cáo này **không có nhiều chỗ** để chơi trò tiểu xảo với các con số… Tuy nhiên, cần nói rõ rằng
> **'không có nhiều chỗ' không có nghĩa là 'không có chỗ'**. Ví dụ, nếu một doanh nghiệp muốn cố thể
> hiện dòng lưu chuyển tiền tệ vững mạnh trong một quý cụ thể, doanh nghiệp đó có thể **trì hoãn thanh
> toán cho nhà cung cấp**, hoặc trì hoãn thanh toán tiền thưởng cho nhân viên đến quý sau."*
> — ch. 16 · PDF tr. 124

**Sách không đo độ lớn.** Đo thử. Giá vốn 6.756/năm → **18,77 triệu mỗi ngày**. Kỳ thanh toán hiện tại
(DPO) = 54,5 ngày.

| trì hoãn thêm | phải trả tăng | tiền từ HĐKD | so với hiện tại |
| --- | ---: | ---: | ---: |
| 0 ngày | 0 | 498 | +0% |
| **10 ngày** | **188** | **686** | **+38%** |
| 20 ngày | 375 | 873 | +75% |
| 30 ngày | 563 | 1.061 | +113% |

⭐ Trì hoãn trả nhà cung cấp đúng **mười ngày** làm tiền từ HĐKD tăng **38%**, bằng **76%** lợi nhuận
thuần cả năm. Chỉ cần **13,2 ngày** là đẩy được một con số bằng **đúng cả năm lợi nhuận** vào dòng tiền
từ HĐKD. **Không một con số nào bị bịa. Không một bút toán nào sai.**

Nhưng nó không miễn phí:

| năm | phải trả cuối năm | ảnh hưởng lên tiền từ HĐKD |
| --- | ---: | ---: |
| năm 1 | 1.210 | **+188** |
| năm 2 | 1.022 | **−188** |
| **TỔNG HAI NĂM** | | **0** |

⭐ Hai năm cộng lại bằng **0** — đúng mẫu hình **nhồi hàng vào kênh** ở
[bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) mục 9, chỉ là đổi sang báo cáo khác. Và sách chốt cùng một
ý: *"trừ khi doanh nghiệp trì hoãn **hết lần này đến lần khác**, và cuối cùng **nhà cung cấp ngừng cung
cấp** hàng hoá và dịch vụ, nếu không, tác động này **chỉ có ý nghĩa trong ngắn hạn**."*

---

## 10. Bốn đòn bẩy của nhà quản lý

Lý do thứ hai sách đưa ra cho việc học báo cáo này:

> [!quote]
> *"**Bạn có tác động đến tiền mặt.** Như chúng tôi đã nói trước đó, hầu hết các nhà quản lý đều tập
> trung vào lợi nhuận, trong khi lẽ ra họ nên tập trung vào **cả lợi nhuận và tiền mặt**."*
> — ch. 18 · PDF tr. 137

Sách liệt kê bốn dòng, mỗi dòng kèm một loạt câu hỏi — nhưng **không dòng nào có số**:

| dòng | sách hỏi gì |
| --- | --- |
| **Khoản phải thu** | *"bạn có bán hàng cho những khách hàng thanh toán hoá đơn đúng hẹn không?"* · *"Các hoá đơn có chính xác không? Phòng thư tín có gửi hoá đơn đúng thời gian quy định không?"* — vì *"những khách hàng bất mãn nổi tiếng là **thanh toán lâu la** – họ muốn đợi cho đến khi mọi tranh chấp được giải quyết."* |
| **Hàng tồn kho** | *"Nếu bạn làm trong bộ phận thiết kế, bạn có luôn yêu cầu sản phẩm đặc biệt không?"* · giữ kho đầy thì *"**tiền mặt chỉ nằm im trên giá**"*. Giải pháp: nguyên tắc sản xuất **tinh gọn** do **Toyota** khởi xướng |
| **Chi phí hoạt động** | *"Bạn có tính toán đến **thời gian lưu chuyển tiền** khi ra quyết định mua hàng không?"* — nhưng rào ngay: *"chúng tôi không nói việc trì hoãn chi tiêu lúc nào cũng khôn ngoan"* |
| **Bán chịu** | *"Bạn có dễ bán chịu… hay bạn từ chối khi lẽ ra nên làm thế?"* — cả hai đều sai, *"đây là lý do tại sao phòng tín dụng luôn phải cân đối thận trọng"* |

Đo giá **một ngày** trên từng dòng:

| dòng | hiện tại | một ngày đáng | đơn giá tính theo |
| --- | ---: | ---: | ---: |
| Khoản phải thu (DSO) | 54,4 ngày | **24,14 triệu** | doanh thu / 360 |
| Tồn kho (ngày tồn cuối kỳ) | 67,7 ngày | **18,77 triệu** | giá vốn / 360 |
| Khoản phải trả (DPO) | 54,5 ngày | **18,77 triệu** | giá vốn / 360 |

*(Bài 9 sẽ định nghĩa DII theo **tồn kho bình quân** hai năm — ra 74,2 ngày. Ở đây dùng tồn kho **cuối
kỳ** vì đó mới là số dư thực sự có thể rút xuống.)*

Một kịch bản **rất** khiêm tốn — thu tiền nhanh hơn 5 ngày và giữ kho mỏng hơn 10 ngày:

| | triệu $ |
| --- | ---: |
| rút DSO 5 ngày | 121 |
| rút tồn kho 10 ngày | 188 |
| **= tiền mặt giải phóng được** | **308** |

⭐ **308 triệu — nhiều hơn cả năm lợi nhuận thuần (248)**, và bằng 62% tiền từ HĐKD cả năm. Không cần
bán thêm một đơn hàng nào, không cần cắt một nhân sự nào.

> [!warning] Và đây không phải mục 9.
> Mục 9 là trì hoãn trả tiền — nó **đảo ngược** ở kỳ sau. Mục này là rút
> ngắn chu kỳ thật; tiền giải phóng ra thì **ở lại**. Sự khác biệt nằm ở chỗ bạn có đổi được **hành vi**
> hay chỉ đổi được **thời điểm ghi sổ**.

> [!example]
> Sách kể cả câu nói mẫu để mở chuyện với phòng tài chính: *"Chẳng hạn nếu tôi thấy DSO của chúng ta
> trong vài tháng gần đây đang đi chệch hướng – **tôi có thể giúp gì** để xoay chuyển tình thế?"* Và nói
> thẳng phần thưởng: nhà quản lý hiểu dòng tiền *"thường được giao nhiều trọng trách hơn, và thường có
> khuynh hướng **thăng tiến nhanh hơn** những người chỉ thuần tuý tập trung vào báo cáo kết quả kinh
> doanh."* (PDF tr. 138–139)

Câu đóng Phần IV:

> [!quote]
> *"Dòng lưu chuyển tiền tệ là chỉ báo chính cho sức khoẻ tài chính, cùng với khả năng sinh lời và vốn
> chủ sở hữu. Nó là **liên kết cuối cùng trong tam giác**, và bạn cần **cả ba** để đánh giá sức khoẻ tài
> chính của doanh nghiệp."* — ch. 18 · PDF tr. 139

---

## 11. Đối chiếu Việt Nam

**① Hai phương pháp lập, và Việt Nam dùng cả hai.** Thuật toán ở mục 4 — bắt đầu từ lợi nhuận thuần rồi
điều chỉnh — gọi là **phương pháp gián tiếp**. Còn **phương pháp trực tiếp** liệt kê thẳng tiền thu từ
khách và tiền trả cho nhà cung cấp. Mẫu B03-DN của Việt Nam có **cả hai biểu mẫu**; doanh nghiệp chọn
một, và đa số chọn gián tiếp — đúng cái mà chương 17 dạy.

> [!example]
> Nếu công ty bạn lập theo **trực tiếp**, mục 4 vẫn dùng được: nó là cách **kiểm chéo** con số mà phòng
> kế toán đưa ra.

**② Tỷ lệ chuyển lợi nhuận thành tiền — thước đo mà chương 18 đặt lên hàng đầu:**

| | tiền từ HĐKD | lợi nhuận thuần | tỷ lệ |
| --- | ---: | ---: | ---: |
| Công ty mẫu (Mỹ, 2005) | 498 | 248 | **2,01 lần** |
| Vinamilk (VN, 2024) | 9.770.587 | 8.686.245 | **1,12 lần** |

⭐ Cả hai đều **trên 1,0** — cả hai đều biến được lợi nhuận thành tiền thật. Nhưng con số cao hơn **không
có nghĩa là khoẻ hơn**: 49% tiền từ HĐKD của công ty mẫu đến từ **giảm tồn kho**, một nguồn chỉ dùng
được một lần. Tỷ lệ 1,12 của Vinamilk **bền hơn** tỷ lệ 2,01 của công ty mẫu, dù trông kém hơn.

> [!warning] Chưa tính được dòng lưu chuyển tiền tự do cho Vinamilk trong kho này.
> Bộ số liệu đang có chỉ ghi
> **tổng** tiền từ hoạt động đầu tư (−3.739.093), chưa tách riêng capex khỏi tiền gửi và đầu tư tài chính.
> Muốn tính phải lấy thêm thuyết minh từ báo cáo gốc. Đây là một **lỗ hổng dữ liệu**, không phải một kết
> luận.

**③ Chỗ "tiểu xảo" của mục 9 có một dấu vết cụ thể trong báo cáo Việt Nam.** Trì hoãn trả nhà cung cấp
làm **DPO** nhảy vọt ở kỳ cuối năm. Vì báo cáo năm chỉ chụp một ngày 31/12, cách kiểm là so **DPO cuối
năm** với DPO các quý trong năm — nếu quý 4 vọt lên rồi quý 1 năm sau tụt về, đó là dấu hiệu. Bài 11 sẽ
dựng công cụ đo DPO.

---

## 12. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py`](../thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py)
rồi chạy lại. Không có lời giải.

1. **Phá thuật toán.** Ở mục 4, đổi dấu một dòng trong `dung_lctt()` — ví dụ cho tài sản tăng thì
   **cộng** thay vì trừ. Chuyện gì xảy ra? Dòng nào báo lệch, và tổng lệch bao nhiêu?

2. **Một năm không chia cổ tức.** Vẫn mục 4, đặt cổ tức bằng 0. Tiền cuối kỳ giờ là bao nhiêu? Câu nói
   của sách — *"nếu không trả cổ tức hay bán cổ phiếu thì dòng tài chính sẽ là 0"* — có đúng ở đây không?
   Vì sao?

3. **Công ty khởi nghiệp thu tiền ngay.** Ở mục 3, cho toàn bộ doanh thu thu bằng tiền thay vì ghi vào
   phải thu. Chênh lệch tiền mặt thuần giờ là bao nhiêu? Kiểm lại bằng đường thứ hai.

4. **Khấu hao gấp đôi.** Ở mục 3, đổi khấu hao từ 10 lên 20 (lợi nhuận thuần xuống 15). Tiền mặt có đổi
   không? Vì sao? Điều này nói gì về quan hệ giữa khấu hao và tiền?

5. **Tồn kho tăng thay vì giảm.** Ở mục 6, nếu tồn kho **tăng** 244 thay vì giảm, tiền từ HĐKD là bao
   nhiêu? Tỷ lệ chuyển đổi còn trên 1,0 không? Kết luận của sách về doanh nghiệp này có đổi không?

6. **Capex bằng khấu hao.** Vẫn mục 6, cho capex = 239 (đúng bằng khấu hao). FCF giờ là bao nhiêu? Nó
   còn đủ trả cổ tức 166 không?

7. **Cổ tức ăn hết FCF.** Ở mục 8, tìm mức cổ tức làm phần "còn lại để trả nợ" **bằng 0**. Nó là bao
   nhiêu đô-la trên mỗi cổ phiếu? So với 2,24 hiện tại.

8. **Trì hoãn ở doanh nghiệp biên dày.** Ở mục 9, thử với doanh nghiệp có giá vốn chỉ 30% doanh thu.
   Trì hoãn 10 ngày giờ đáng bao nhiêu phần trăm tiền từ HĐKD? Doanh nghiệp nào **dễ** dùng thủ thuật
   này hơn — biên dày hay biên mỏng?

9. **Kịch bản tham vọng.** Ở mục 10, thử rút DSO **15 ngày** và tồn kho **30 ngày**. Tiền giải phóng
   bằng bao nhiêu lần lợi nhuận thuần? Ở mức nào thì bạn bắt đầu ngờ rằng con số không thực tế?

10. **Đòn bẩy nào rẻ nhất.** Vẫn mục 10: một ngày DSO đáng 24,14 triệu, một ngày tồn kho đáng 18,77
    triệu. Nhưng cái nào **dễ rút** hơn trong thực tế? Vì sao con số lớn hơn chưa chắc là đòn bẩy tốt hơn?

---

## 13. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Báo cáo lưu chuyển tiền tệ | cash flow statement | báo cáo thứ ba — đo **tiền thật vào ra** |
| Dòng tiền vào / dòng tiền ra | cash inflow / outflow | tiền chảy vào / ra khỏi doanh nghiệp |
| Lưu chuyển tiền từ HĐKD | cash flow from operations (CFO) | *"con số quan trọng nhất cho biết tình trạng"* |
| Lưu chuyển tiền từ đầu tư | cash flow from investing | mua/bán tài sản — đầu tư **của doanh nghiệp** |
| Lưu chuyển tiền từ tài chính | cash flow from financing | vay/trả nợ, và giao dịch với cổ đông |
| Phương pháp gián tiếp | indirect method | bắt đầu từ lợi nhuận thuần rồi điều chỉnh — thuật toán ch. 17 |
| 💼 Phương pháp trực tiếp | direct method | liệt kê thẳng tiền thu, tiền chi — **không có trong sách** |
| Cân đối | reconcile | khớp dòng tiền trên sổ với tiền thật trong ngân hàng |
| Chi tiêu phi tiền mặt | noncash expense | trừ vào lợi nhuận nhưng không chi tiền — phải **cộng lại** |
| Đầu tư cơ bản / capex | capital expenditure | tiền chi mua tài sản dài hạn |
| Dòng lưu chuyển tiền tự do | free cash flow (FCF) | **CFO − capex** |
| Thu nhập chủ sở hữu | owner earnings | tên Buffett đặt cho cùng thước đo đó |
| Con bò sữa | cash cow | vắt kiệt tiền mà không tái đầu tư |
| Rót vốn | funding | lấy tiền để khởi nghiệp hoặc mở rộng — vay nợ hoặc gọi vốn |
| Mua lại cổ phiếu | share buyback | giảm số cổ phiếu lưu hành → mỗi cổ đông sở hữu phần lớn hơn |
| Sản xuất tinh gọn | lean manufacturing | giữ tồn kho tối thiểu — nguyên tắc do **Toyota** khởi xướng |
| 💼 Tỷ lệ chuyển lợi nhuận thành tiền | cash conversion | CFO / lợi nhuận thuần — **cụm từ không có trong sách** |

---

## 14. Câu hỏi tự kiểm tra

1. Kể ba lý do sách đưa ra cho việc báo cáo lưu chuyển tiền tệ khó đọc. (mục 1)
2. Sách nêu ví dụ nào cho lý do "dấu không rõ ràng"? (mục 1)
3. Ba hạng mục của báo cáo là gì? Mỗi hạng mục gồm những gì? (mục 2)
4. Hạng mục nào sách gọi là *"con số quan trọng nhất cho biết tình trạng của doanh nghiệp"*? (mục 2)
5. Dòng đầu tư **thấp** có thể là dấu hiệu gì? Sách tự rào lại thế nào? (mục 2)
6. "Hoạt động đầu tư" ở đây là đầu tư **của ai**? (mục 2)
7. Công ty khởi nghiệp: viết bốn dòng của phép tính và kết quả. (mục 3)
8. Kiểm kết quả đó bằng đường thứ hai — đường nào? (mục 3)
9. Vì sao thuật toán **bắt đầu từ lợi nhuận thuần**? (mục 3)
10. Phát biểu **nguyên tắc chính** về tài sản và nợ. (mục 3)
11. Sách hứa điều gì ở đầu chương 17? Vì sao điều đó **phải** đúng? (mục 4)
12. Hàm `dung_lctt()` cần đầu vào gì? Nó **không** cần gì? (mục 4)
13. PPE trên sổ sách giảm 34, nhưng dòng đầu tư ghi (205). Giải thích. Viết công thức. (mục 4)
14. Cổ tức 166 tính từ đâu? 248 − 166 = 82 là con số gì? (mục 4)
15. *"Nếu doanh nghiệp không trả cổ tức hay bán cổ phiếu thì dòng tài chính sẽ ___."* Điền. (mục 4)
16. Phải thu tăng 108 thì dòng trên báo cáo ghi bao nhiêu? Phải trả giảm 107 thì sao? (mục 5)
17. Phát biểu quy tắc dấu bằng một câu. (mục 5)
18. Gặp dòng *"(tăng)/giảm"* với một số dương — nghĩa là tiền tăng hay giảm? (mục 5)
19. Tỷ lệ chuyển lợi nhuận thành tiền của công ty mẫu là bao nhiêu? Vì sao nó **không bền**? (mục 6)
20. Sách viết *"khấu hao vượt xa đầu tư mới"*. Con số thật là bao nhiêu? Nhận xét đó có quá tay không? (mục 6)
21. Cả ba hạng mục tài chính đều âm — điều đó nghĩa là gì? (mục 6)
22. Kể bốn chỗ sách in sai trong chương 17. Chỗ nào là **mới** so với bài 0? (mục 7)
23. Vì sao ta biết chắc 5.193 đúng chứ không phải 5.133? (mục 7)
24. Khi hai chỗ trong cùng một tài liệu nói hai con số khác nhau, làm gì? (mục 7)
25. Viết công thức **dòng lưu chuyển tiền tự do**. Buffett gọi nó là gì? (mục 8)
26. FCF của công ty mẫu là bao nhiêu? Cổ tức ăn hết bao nhiêu phần trăm? (mục 8)
27. FCF bắt được gì ở các công ty dot-com mà EBITDA không bắt được? (mục 8)
28. Kể ba thứ mà FCF khoẻ và đang tăng nói lên. (mục 8)
29. Trì hoãn trả nhà cung cấp 10 ngày làm tiền từ HĐKD tăng bao nhiêu phần trăm? (mục 9)
30. Cần trì hoãn bao nhiêu ngày để đẩy được một con số bằng cả năm lợi nhuận? (mục 9)
31. Hai năm cộng lại bằng bao nhiêu? Thủ thuật này giống thủ thuật nào ở bài 2? (mục 9)
32. Sách nói giới hạn của thủ thuật này ở đâu? (mục 9)
33. Kể bốn dòng mà nhà quản lý tác động được, và một câu hỏi sách gắn với mỗi dòng. (mục 10)
34. Một ngày DSO của công ty mẫu đáng bao nhiêu? Một ngày tồn kho? (mục 10)
35. Rút DSO 5 ngày và tồn kho 10 ngày giải phóng bao nhiêu tiền? So với lợi nhuận thuần cả năm. (mục 10)
36. Vì sao mục 10 **khác về bản chất** so với mục 9? (mục 10)
37. Sách nói gì về triển vọng nghề nghiệp của nhà quản lý hiểu dòng tiền? (mục 10)
38. *"Nó là liên kết cuối cùng trong ___."* Điền, và kể đủ ba đỉnh. (mục 10)
39. Hai phương pháp lập báo cáo lưu chuyển tiền tệ là gì? Chương 17 dạy phương pháp nào? (mục 11)
40. Tỷ lệ 1,12 của Vinamilk **bền hơn** tỷ lệ 2,01 của công ty mẫu. Vì sao? (mục 11)
41. Vì sao chưa tính được FCF của Vinamilk trong kho này? (mục 11)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 7 — BÁO CÁO LƯU CHUYỂN TIỀN TỆ  (ch. 16–18, PDF tr. 121–141)        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  BA HẠNG MỤC, BA CÂU HỎI:                                                ║
║    ① HĐKD    → "con số QUAN TRỌNG NHẤT cho biết tình trạng"              ║
║    ② đầu tư  → "dành ra bao nhiêu để ĐẦU TƯ CHO TƯƠNG LAI"               ║
║                thấp = coi doanh nghiệp là CON BÒ SỮA                     ║
║    ③ tài chính → "PHỤ THUỘC thế nào vào nguồn bên ngoài"                 ║
║                                                                          ║
║  ⭐ THUẬT TOÁN CỦA CHƯƠNG 17 — dựng cả báo cáo CHỈ từ hai báo cáo kia    ║
║       tài sản TĂNG → tiền GIẢM  ·  nợ TĂNG → tiền TĂNG                   ║
║       khấu hao là chi phí PHI TIỀN MẶT → CỘNG LẠI                        ║
║     13 dòng, KHÔNG MỘT DÒNG NÀO LỆCH so với báo cáo sách in.             ║
║     "vì trong tài chính, THẾ GIỚI THỰC ĐƯỢC ĐẠI DIỆN BỞI TIỀN MẶT"       ║
║                                                                          ║
║     bẫy PPE:  capex = khấu hao + thay đổi PPE = 239 + (−34) = 205        ║
║     PPE giảm 34 KHÔNG phải bán tài sản — đã chi 205 tiền thật.           ║
║                                                                          ║
║  ⭐ QUY TẮC DẤU — trả lời "đó là tăng hay giảm?"                         ║
║     dấu trên báo cáo NGƯỢC dấu thay đổi TÀI SẢN, CÙNG dấu thay đổi NỢ    ║
║     mẹo: số DƯƠNG luôn nghĩa là TIỀN TĂNG. Suy ngược ra phần còn lại.    ║
║                                                                          ║
║  ⚠️ BỐN CHỖ SÁCH IN SAI TRONG CHÍNH CHƯƠNG 17:                           ║
║     tr.130 tổng tài sản 5.133 → 5.193                                    ║
║     tr.132 bước 8 "phải trả giảm 10" → 107   ← CHỖ NÀY LÀ MỚI            ║
║     tr.135 hai dòng tổng in thiếu dấu âm                                 ║
║     → tìm ra được vì thuật toán dựng lại báo cáo rồi đối chiếu.          ║
║                                                                          ║
║  BA HẠNG MỤC NÓI GÌ VỀ CÔNG TY MẪU:                                      ║
║     ① CFO 498 / lợi nhuận 248 = 2,01 lần — NHƯNG 49% đến từ              ║
║        GIẢM TỒN KHO, nguồn CHỈ DÙNG ĐƯỢC MỘT LẦN. Không bền.             ║
║     ② capex 205 / khấu hao 239 = 0,86.  Sách nói "vượt XA" —             ║
║        thật ra vượt 17%, PPE mất 66 NĂM mới mòn hết. "Vượt NHẸ".         ║
║     ③ cả ba âm → không gọi vốn ngoài một đồng nào.                       ║
║                                                                          ║
║  ⭐ DÒNG LƯU CHUYỂN TIỀN TỰ DO = CFO − capex   (Buffett: "thu nhập       ║
║     chủ sở hữu"). EBITDA KHÔNG CÒN là thước đo của Phố Wall.             ║
║       498 − 205 = 293   →  − cổ tức 166  →  còn 127                      ║
║       FCF 293 > lợi nhuận 248. Cổ tức ăn 57% FCF.                        ║
║     dot-com: CFO ÂM + đầu tư KHỔNG LỒ → FCF âm nặng, sống nhờ            ║
║     "nhà đầu tư NÉM TIỀN VÀO ĐỐNG LỬA ĐANG BÙNG CHÁY".                   ║
║                                                                          ║
║  ⭐ "KHÔNG NHIỀU CHỖ" KHÔNG PHẢI "KHÔNG CÓ CHỖ"                          ║
║     trì hoãn trả nhà cung cấp 10 ngày → CFO +188 = +38%                  ║
║     13,2 ngày = đẩy được CẢ NĂM LỢI NHUẬN vào dòng tiền                  ║
║     nhưng hai năm cộng lại = 0. Giống NHỒI HÀNG VÀO KÊNH (bài 2).        ║
║                                                                          ║
║  ⭐ BỐN ĐÒN BẨY — và giá MỘT NGÀY của từng cái:                          ║
║       DSO 54,4 ngày   → 1 ngày = 24,14 triệu                             ║
║       tồn kho 67,7 ngày → 1 ngày = 18,77 triệu                           ║
║     rút DSO 5 ngày + tồn kho 10 ngày = GIẢI PHÓNG 308 TRIỆU              ║
║     — NHIỀU HƠN cả năm lợi nhuận (248), không bán thêm đơn hàng nào.     ║
║     KHÁC mục 9: rút chu kỳ thật thì tiền Ở LẠI; trì hoãn thì ĐẢO NGƯỢC.  ║
║                                                                          ║
║  🇻🇳 tỷ lệ chuyển đổi: công ty mẫu 2,01 · Vinamilk 1,12                   ║
║     Con số THẤP HƠN lại BỀN HƠN — vì 2,01 vay từ tồn kho một lần.        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần IV — Tiền mặt là nhất**, PDF tr. 108–141.
    - Ch. 16 *Ngôn ngữ của báo cáo lưu chuyển tiền tệ*, PDF tr. 121–124
      — **ba lý do khó đọc** và ví dụ *"(tăng)/giảm khoản phải thu"* (tr. 121); **ba hạng mục** —
      HĐKD (tr. 121–122), đầu tư và tài chính (tr. 122); ý nghĩa từng hạng mục, **"con bò sữa"**
      (tr. 122–123); hộp **"Rót vốn cho doanh nghiệp"** và **"Mua lại cổ phiếu"** (tr. 123);
      ⭐ *"không có nhiều chỗ… không có nghĩa là không có chỗ"* và **trì hoãn trả nhà cung cấp**
      (tr. 124)
    - Ch. 17 *Tiền mặt kết nối với mọi thứ khác ra sao*, PDF tr. 125–135
      — ⭐ lời hứa *"tính toán số liệu… chỉ bằng cách nhìn vào"* và lý do *"thế giới thực được đại diện
      bởi tiền mặt"* (tr. 125); **chuỗi giao dịch** bán chịu 100 / mua tồn kho 100 (tr. 125–126);
      **cân đối lợi nhuận và tiền mặt**, ví dụ A/R 100 → 125 (tr. 126–127); hộp **"Cân đối"** (tr. 127);
      ⭐ **công ty khởi nghiệp** và **nguyên tắc chính** tài sản/nợ (tr. 128–129); **doanh nghiệp thực
      tế** — hai báo cáo in lại (tr. 129–132), **12 bước** (tr. 132–133), **Lưu ý 1** đội xe tải
      100.000 và **Lưu ý 2** cổ tức 166 (tr. 133); *"đẹp đẽ và tinh vi"* (tr. 134); **báo cáo lưu
      chuyển tiền tệ đầy đủ** (tr. 134–135)
    - Ch. 18 *Tại sao tiền mặt lại quan trọng*, PDF tr. 136–141
      — đọc báo cáo công ty mẫu, *"khấu hao vượt xa đầu tư mới"* (tr. 136); **ba lý do** nên hiểu dòng
      tiền (tr. 136–139); ⭐ **bốn đòn bẩy** — phải thu, tồn kho, chi phí hoạt động, bán chịu, và
      **Toyota** (tr. 137–138); **DSO** và thăng tiến (tr. 138–139); *"liên kết cuối cùng trong tam
      giác"* (tr. 139); hộp công cụ ⭐ **dòng lưu chuyển tiền tự do**, **Berkshire Hathaway / thu nhập
      chủ sở hữu**, **dot-com** (tr. 139–140)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 4, 5, 6, 7, 8, 9, 10
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 11](#11-đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py`](../thuc_hanh/bai-07-bao-cao-luu-chuyen-tien-te.py):
  - ⭐ **`dung_lctt()` sinh lại cả 13 dòng của báo cáo chỉ từ hai bảng cân đối + khấu hao + cổ tức**, và
    cả ba hạng mục khớp **từng dòng** với bản sách in — chốt bằng `assert` trên cả ba dict;
  - công ty khởi nghiệp: thuật toán cho **−15**, đúng bằng khoản chi tiền mặt duy nhất — chốt bằng `assert`;
  - **quy tắc dấu** đúng trên **từng dòng** tài sản và nợ — chốt bằng `assert`;
  - capex = khấu hao + Δ PPE = **205** — chốt bằng `assert`;
  - 498 − 185 − 302 = 11 = Δ tiền trên bảng cân đối — chốt bằng `assert`;
  - *"khấu hao vượt xa đầu tư"*: tỷ lệ thật **dưới 1,2 lần** — chốt bằng `assert`;
  - FCF = **293** và lớn hơn cổ tức — chốt bằng `assert`;
  - trì hoãn trả nợ: hai năm cộng lại **bằng 0**, và **13,2 ngày** thì bằng cả năm lợi nhuận — chốt bằng
    `assert`;
  - rút DSO 5 ngày + tồn kho 10 ngày giải phóng **nhiều hơn** cả năm lợi nhuận — chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** toàn bộ kịch bản trì hoãn 5/10/20/30 ngày ở mục
  9; kịch bản rút DSO 5 ngày và tồn kho 10 ngày ở mục 10; cách quy "một ngày" theo doanh thu/360 và giá
  vốn/360. Mọi con số **của sách** đều được trích kèm mốc `ch. N · PDF tr. M`.

---

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| **7** | **Báo cáo lưu chuyển tiền tệ** ← *bạn đang ở đây* | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
