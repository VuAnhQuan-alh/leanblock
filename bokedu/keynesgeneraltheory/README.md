# Lý thuyết tổng quát — đọc thẳng Keynes

Bộ bài học dựng **từ chính cuốn sách**, không viết theo trí nhớ. Đây là **nguồn gốc** —
đọc thẳng Keynes 1936, cuốn khai sinh ngành **kinh tế học vĩ mô**. Bổ trợ cho
[Của cải của các dân tộc (Adam Smith)](../adamsmitccccdt/README.md) — Keynes chính là người
**lật ngược** nhiều kết luận của Smith mà bạn đã học ở đó.

**Sách gốc:** John Maynard Keynes, ***The General Theory of Employment, Interest and Money***
(1936). Kho giữ **một bản** (không có bản dịch tiếng Việt trong kho):

| Tệp trong `tai_lieu/` | Là gì | Dùng để |
| --- | --- | --- |
| `The General Theory - Keynes (Gutenberg AU).txt` | Bản gốc tiếng Anh, đã làm sạch (Project Gutenberg Australia #0300071h, phạm vi công cộng tại Úc) | Văn chính — trích nguyên văn + kiểm mọi con số |
| `The General Theory - Keynes (Gutenberg AU).html` | Bản HTML gốc, giữ nguyên để đối chiếu | Kiểm chứng khi nghi ngờ bản text |

> [!warning] Ba điều đã kiểm về bản nguồn
> 1. **Chỉ có bản tiếng Anh** — kho không có bản dịch Việt của Keynes. Mọi câu dịch trong khoá
>    là **do người soạn dịch**, luôn kèm nguyên văn Anh trong `> [!quote]` để bạn tự đối chiếu.
> 2. Bản Gutenberg AU **chèn thêm một "GENERAL INTRODUCTION" do người biên tập viết năm 2003** —
>    *không phải* văn Keynes. Bản `.txt` trong kho **đã lược bỏ** phần đó; văn bắt đầu từ đúng
>    **Lời tựa** của chính Keynes.
> 3. Bản etext này **bỏ tiêu đề 6 Quyển** (chỉ ghi "BOOK I"…). Tên Quyển trong khoá lấy từ mục
>    lục gốc Macmillan (đối chiếu History of Economic Thought), không bịa.

---

## Cách đọc

| Quy ước | Nghĩa |
| --- | --- |
| `QIV, Ch 12` | trích **Quyển IV, Chương 12** — theo cấu trúc gốc của sách, ổn định qua mọi ấn bản |
| `> [!quote]` | câu kinh điển in **nguyên văn tiếng Anh** (Gutenberg), kèm bản dịch Việt |
| `> [!warning]` | chỗ dễ hiểu sai, chỗ Keynes viết khó/gây tranh cãi, hoặc chỗ hậu thế đọc lệch ý ông |
| `> [!info]` | ghi chú định hướng đầu mỗi bài |
| `> [!example]` **Góc đời sống** | ví dụ đời thường để hiểu khái niệm trừu tượng — **không có trong sách** |
| **Mở rộng** | kiến thức nền sách nói lướt, hoặc thuật ngữ (số nhân, IS–LM…) cần giải thích thêm |
| **Nối môn** | liên hệ [Adam Smith](../adamsmitccccdt/README.md), [Ba người khổng lồ](../bigthreeeconomic/README.md), [EG43 Kinh tế Chính trị](../../houedu/eg43-kinhtechinhtri/README.md) — **không có trong sách** |
| **Đối chiếu 2026** | sách viết năm 1936 — mục này soi lại bằng con mắt hôm nay |

Công thức viết bằng LaTeX. Mở bằng **Obsidian** (hoặc VS Code + Markdown Preview Enhanced).

---

## Vì sao học cuốn này

Năm 1936, giữa lòng **Đại khủng hoảng** (thất nghiệp Mỹ có lúc 25%), một nhà kinh tế Cambridge
xuất bản cuốn sách bác thẳng niềm tin cốt lõi của kinh tế học đương thời: rằng thị trường tự
do luôn tự đưa mình về **toàn dụng nhân công**. Keynes hỏi một câu đơn giản mà cả một trường
phái không trả lời nổi: *nếu thị trường tự chữa, vì sao hàng triệu người thất nghiệp năm này
qua năm khác?*

Cuốn sách khai sinh ngành **kinh tế học vĩ mô** và bộ khái niệm mà hôm nay ai học kinh tế cũng
gặp — **cầu hữu hiệu, số nhân chi tiêu, khuynh hướng tiêu dùng, hiệu suất biên của vốn, ưa
thích thanh khoản, bẫy thanh khoản**. Mọi gói kích cầu, mọi lần ngân hàng trung ương hạ lãi
suất trong khủng hoảng đều là con cháu của cuốn này.

Học cuốn này để **khép vòng** với [Adam Smith](../adamsmitccccdt/README.md): Smith dạy "bàn tay
vô hình" và "tiết kiệm là đức"; Keynes chỉ ra cả hai có thể **phản tác dụng** khi nền kinh tế
kẹt trong suy thoái. Đọc xong hai cuốn, bạn nắm được **hai cực** của tranh luận kinh tế suốt
250 năm.

---

## Bản đồ khoá học

Keynes chia tác phẩm thành **6 Quyển**. Khoá bám đúng bố cục đó — 6 Quyển → **8 bài + Bài 0**:

```
QUYỂN I    Dẫn nhập              (phê phán cổ điển, nguyên lý cầu hữu hiệu)      → bài 1
QUYỂN II   Định nghĩa & ý niệm   (đơn vị đo, kỳ vọng, tiết kiệm ≡ đầu tư)        → bài 2
QUYỂN III  Khuynh hướng tiêu dùng (số nhân chi tiêu, nghịch lý tiết kiệm)       → bài 3
QUYỂN IV   Động lực đầu tư        (hiệu suất vốn, lãi suất, ưa thích thanh khoản) → bài 4–6
QUYỂN V    Tiền công & giá cả     (vì sao giảm lương không chữa được thất nghiệp) → bài 7
QUYỂN VI   Ghi chú mở rộng        (chu kỳ, trọng thương, triết lý xã hội)         → bài 8
```

| # | Bài | Nội dung sách | Chương | Vòng |
| ---: | --- | --- | :---: | :---: |
| 0 | [Nhập môn — 1936, Đại khủng hoảng và cuộc cách mạng Keynes](ly_thuyet/bai_00_nhap_mon.md) | Bối cảnh + bản đồ 6 Quyển | — | 1 |
| 1 | [Cầu hữu hiệu — cú lật đổ "cung tự tạo cầu"](ly_thuyet/bai_01_cau_huu_hieu.md) | QI, Ch 1–3 | 1 · trọng tâm |
| 2 | [Bộ công cụ: đơn vị đo, kỳ vọng, tiết kiệm ≡ đầu tư](ly_thuyet/bai_02_dinh_nghia_cong_cu.md) | QII, Ch 4–7 | 2 |
| 3 | [Khuynh hướng tiêu dùng và Số nhân chi tiêu](ly_thuyet/bai_03_tieu_dung_so_nhan.md) | QIII, Ch 8–10 | 1 · trọng tâm |
| 4 | [Đầu tư — hiệu suất biên của vốn và "animal spirits"](ly_thuyet/bai_04_dau_tu_animal_spirits.md) | QIV, Ch 11–12 | 1 · trọng tâm |
| 5 | [Lãi suất và ưa thích thanh khoản — bẫy thanh khoản](ly_thuyet/bai_05_lai_suat_thanh_khoan.md) | QIV, Ch 13–15 | 1 · trọng tâm |
| 6 | [Bản chất vốn, tính chất riêng của tiền và mô hình việc làm](ly_thuyet/bai_06_von_tien_mo_hinh.md) | QIV, Ch 16–18 | 2 |
| 7 | [Tiền công, giá cả và lạm phát](ly_thuyet/bai_07_tien_cong_gia_ca.md) | QV, Ch 19–21 | 2 |
| 8 | [Chu kỳ, trọng thương và triết lý xã hội (+ nhìn lại cả khoá)](ly_thuyet/bai_08_chu_ky_triet_ly.md) | QVI, Ch 22–24 | 1 · trọng tâm |

Vòng 1 = học kỹ · Vòng 2 = đọc hiểu. Toàn khoá dựng từ **bản Anh** (kho không có bản dịch Việt).

> [!note] Tiến độ
> **Giáo án đã chốt (Bài 0–8).** Các bài sẽ dựng dần từ bản Anh Gutenberg, mỗi bài trích nguyên
> văn + dịch, kèm Góc đời sống cho từng khái niệm khó.

---

## Nối môn đang học

| Môn trong kho | Giao ở đâu | Học kết hợp thế nào |
| --- | --- | --- |
| [Của cải của các dân tộc (Adam Smith)](../adamsmitccccdt/ly_thuyet/bai_05_von.md) | Bài 3 (nghịch lý tiết kiệm) | Smith: "tiết kiệm là ân nhân xã hội" (Q2). Keynes: trong suy thoái, cả nước cùng tiết kiệm thì tổng cầu sụp — **nghịch lý tiết kiệm**. Đọc song song thấy đúng điểm hai người va nhau. |
| [Của cải của các dân tộc (Adam Smith)](../adamsmitccccdt/ly_thuyet/bai_07_trong_thuong_ban_tay_vo_hinh.md) | Bài 8 (Ch 23 trọng thương) | Smith đập tan chủ nghĩa trọng thương. Keynes ở Ch 23 **bênh vực một phần** giới trọng thương — họ trực giác đúng về tổng cầu và lãi suất. Một cú vặn lại bất ngờ. |
| [Ba người khổng lồ (Skousen)](../bigthreeeconomic/README.md) | Cả khoá | Skousen xếp Keynes là **người khổng lồ thứ ba** (sau Smith, Marx). Ở đây đọc nguyên tác thay vì tóm tắt. |
| [EG43 — Kinh tế Chính trị Mác–Lênin](../../houedu/eg43-kinhtechinhtri/README.md) | Bài 1, 8 | Cả Marx và Keynes đều bác "thị trường tự cân bằng" của phái cổ điển, nhưng kê hai toa thuốc trái ngược: Marx đòi thay hệ thống, Keynes đòi **cứu** hệ thống bằng nhà nước. |
