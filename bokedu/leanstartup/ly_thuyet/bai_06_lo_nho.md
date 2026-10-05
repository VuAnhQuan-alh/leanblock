# Bài 6 — Lô nhỏ & triển khai liên tục

> [!info] Về bài này
> Dựng từ **Ch. 9 "Loạt sản xuất"** của *Khởi nghiệp Tinh gọn* (Eric Ries, `tai_lieu/`, `PDF tr. 210–234`).
> Mở đầu **Phần III "Tăng tốc"**: các kỹ thuật để **chạy vòng BML nhanh hơn** — mà nhanh hơn nghĩa là đường băng dài hơn ([Bài 5](bai_05_pivot.md)).
> 📌 Nên đọc trước: [Bài 5 — Điều chỉnh hay kiên định (Pivot)](bai_05_pivot.md).

## Mục lục

1. [Mở đầu: cuộc đua gấp phong bì](#1-mở-đầu-cuộc-đua-gấp-phong-bì)
2. [Vì sao lô nhỏ nhanh hơn, dù phản trực giác](#2-vì-sao-lô-nhỏ-nhanh-hơn-dù-phản-trực-giác)
3. [Dây Andon: dừng dây chuyền để sửa lỗi ngay](#3-dây-andon-dừng-dây-chuyền-để-sửa-lỗi-ngay)
4. [Triển khai liên tục: IMVU giao hàng 50 lần mỗi ngày](#4-triển-khai-liên-tục-imvu-giao-hàng-50-lần-mỗi-ngày)
5. [Kéo, đừng đẩy](#5-kéo-đừng-đẩy)
6. [Lô nhỏ nối lại toàn khoá](#6-lô-nhỏ-nối-lại-toàn-khoá)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: cuộc đua gấp phong bì

Ries kể một thí nghiệm ai cũng thử được. Cần gửi một xấp thư: mỗi phong bì phải **gấp thư, cho vào bì, dán địa chỉ, dán tem, dán mép**. Hai cách:

- **Lô lớn**: gấp *tất cả* thư trước, rồi nhét *tất cả* vào bì, rồi dán *tất cả* tem… — làm xong từng công đoạn cho cả xấp.
- **Lô nhỏ (một-lần-một)**: làm trọn vẹn *một* phong bì từ đầu tới cuối, rồi mới sang cái tiếp theo.

Trực giác nói cách lô lớn nhanh hơn. Thực tế ngược lại:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 210)
> "Phương pháp **một lần một bao thư** là cách làm **nhanh hơn** cho dù nó có vẻ không hiệu quả. Cách này đã được khẳng định qua nhiều thí nghiệm."

Vì sao? Đó là câu hỏi mở ra toàn bộ bài — và toàn bộ Phần "Tăng tốc".

## 2. Vì sao lô nhỏ nhanh hơn, dù phản trực giác

Hai lý do, cùng áp dụng cho startup:

**Lý do 1 — trực giác quên mất chi phí "gom lô".**

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 211)
> "Vì sao xếp một lần một bao thư lại nhanh hơn…? Bởi vì trực giác của chúng ta đã **không tính đến thời gian phụ thêm để phân loại, xếp chồng và đi lòng vòng** [những chồng bán thành phẩm]."

**Lý do 2 — quan trọng hơn — lô nhỏ phát hiện lỗi *sớm*.**

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 211, 220)
> "Sẽ thế nào nếu các bao thư bị lỗi và không dán dính được? Ở **loạt lớn**, chúng ta sẽ phải lấy thư ra hết, thay [toàn bộ]… Với **loạt nhỏ, chúng ta hầu như phát hiện ra được ngay**. Ưu thế lớn nhất của làm việc theo từng loạt nhỏ là **những vấn đề về chất lượng được phát hiện từ rất sớm**."

Nếu cả xấp bì đều lỗi, cách lô lớn khiến bạn phát hiện khi đã gấp xong *tất cả* — hỏng cả mẻ. Cách lô nhỏ báo lỗi ngay ở phong bì đầu tiên. Với startup, "phong bì lỗi" = một giả định sai; **lô nhỏ = tung thay đổi nhỏ và học ngay**, thay vì dồn sáu tháng công sức rồi mới biết sai (đúng bẫy IMVU ở [Bài 1](bai_01_hoc_hoi_co_kiem_chung.md)).

## 3. Dây Andon: dừng dây chuyền để sửa lỗi ngay

Nguyên tắc "phát hiện lỗi sớm" của Toyota được thể chế hoá thành một sợi dây:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 213)
> "Hệ thống **'Andon cord' (kéo dây báo lỗi)** nổi tiếng của Toyota cho phép **bất kỳ công nhân nào** cũng có thể yêu cầu được hỗ trợ ngay khi họ phát hiện ra bất kỳ vấn đề gì… [và] **ngừng toàn bộ dây chuyền** sản xuất nếu lỗi ấy không được chữa ngay lập tức."

Nghe phản trực giác: dừng cả dây chuyền vì một lỗi nhỏ? Nhưng:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 213–214)
> "Lợi ích của việc **tìm thấy và khắc phục vấn đề nhanh hơn vượt xa chi phí** [dừng dây chuyền]… Đây chính là nguyên nhân cốt lõi của **chất lượng cao và chi phí thấp** nổi tiếng trong lịch sử của Toyota."

Bài học cho startup: đừng để lỗi (hay giả định sai) "chảy xuôi" tích tụ. Dừng lại, sửa tận gốc ngay — cơ chế "sửa tận gốc" chính là **5 Tại Sao** ở [Bài 8](bai_08_thich_nghi_cach_tan_dung_lang_phi.md).

## 4. Triển khai liên tục: IMVU giao hàng 50 lần mỗi ngày

Áp lô nhỏ vào phần mềm cho ra **triển khai liên tục** (continuous deployment) — tung thay đổi thành vô số mẩu tí hon thay vì bản "đại cập nhật":

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 220)
> "[IMVU giao hàng mỗi] ngày **50 lần**… bài học là bằng việc **giảm kích cỡ loạt sản xuất, chúng ta có thể di chuyển qua vòng phản hồi Xây dựng – Đo lường – Học hỏi** [nhanh hơn]."

Gốc kỹ thuật của lô nhỏ đến từ chính Toyota:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 212–213)
> "[Toyota dùng] khái niệm **SMED (Single-Minute Exchange of Die - chuyển đổi khuôn từng phút)** để thực hiện việc sản xuất với quy mô loạt nhỏ hơn."

SMED giảm *thời gian chuyển đổi* để làm lô nhỏ mà không bị phạt năng suất. Tương đương với phần mềm: đầu tư vào tự động hoá kiểm thử/triển khai để mỗi thay đổi nhỏ ra được ngay, rẻ. Kết quả: mỗi thay đổi là một vòng BML mini — học liên tục thay vì học theo mẻ lớn.

## 5. Kéo, đừng đẩy

Câu hỏi cuối: sản xuất bao nhiêu, khi nào? Lối cũ **đẩy** (push): dự báo nhu cầu rồi làm sẵn hàng loạt, trữ kho. Rủi ro:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 228)
> "Trữ nhiều hàng thì rất tốn kém… Sẽ ra sao nếu cái chống va đập đời 2011 bỗng nhiên bị lỗi? **Tất cả phụ tùng ở tất cả các kho bỗng chốc trở thành vô giá trị.**"

Lối tinh gọn **kéo** (pull): chỉ làm khi có nhu cầu thật kích hoạt:

> [!quote] Khởi nghiệp Tinh gọn — Ch. 9 (PDF tr. 228)
> "Sản xuất tinh gọn giải quyết vấn đề [cháy hàng] bằng một kỹ thuật gọi là **kéo (pull)**. Khi bạn đem xe đến một đại lý… một cái chống va đập cho Camry màu xanh đời 2011 được sử dụng. Điều này tạo ra 'một lỗ hổng' trong hàng tồn kho… **tự động phát ra** [tín hiệu bổ sung đúng một cái]."

Với startup, "kéo" nghĩa là: **để công việc được kéo bởi thí nghiệm cần chạy và học-có-kiểm-chứng cần thu**, không **đẩy** hàng loạt tính năng suy diễn vào sản phẩm với hy vọng có người cần. Mỗi tính năng nên được "kéo" bởi một phỏng đoán cần kiểm ([Bài 3](bai_03_phong_doan_niem_tin_va_mvp.md)), không phải "đẩy" vì "biết đâu hữu ích".

## 6. Lô nhỏ nối lại toàn khoá

Lô nhỏ không phải mẹo kỹ thuật lẻ — nó là **động cơ tăng tốc** của mọi thứ đã học:

- Vòng **BML** ([Bài 2](bai_02_vong_xay_dung_do_luong_hoc_hoi.md)) chạy nhanh hơn khi mỗi lần xây là một mẩu nhỏ.
- **MVP** ([Bài 3](bai_03_phong_doan_niem_tin_va_mvp.md)) chính là lô nhỏ đầu tiên: xây tối thiểu để học.
- **Đường băng** ([Bài 5](bai_05_pivot.md)) dài ra vì lô nhỏ → vòng ngắn → nhiều lần pivot hơn với cùng số tiền.

> [!warning] Lô nhỏ ≠ làm cẩu thả cho nhanh
> Rút nhỏ lô là để **học nhanh và bắt lỗi sớm**, không phải để bỏ qua chất lượng. Ngược lại: chính vì phát hiện lỗi sớm (dây Andon) mà lô nhỏ cho *chất lượng cao hơn* với chi phí thấp hơn. Tốc độ ở đây là tốc độ **học**, không phải tốc độ **ẩu**.

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. Nhìn cách bạn đang làm việc: bạn đang **gom lô lớn** (dồn nhiều thay đổi rồi mới tung một lần) hay **lô nhỏ** (tung từng mẩu, học ngay)? Kể một "mẻ lớn" bạn từng làm mà lỗi chỉ lộ ra ở cuối.
> 2. Chọn một việc lớn sắp tới, **chẻ nó thành lô nhỏ nhất có thể tung & học độc lập**. Mẩu đầu tiên là gì?
> 3. "Dây Andon" của bạn là gì — dấu hiệu nào khiến bạn **dừng lại sửa tận gốc ngay** thay vì để lỗi tích tụ?
> 4. Rà các tính năng trong kế hoạch: cái nào đang bị **đẩy** (làm vì "biết đâu cần") thay vì **kéo** (một phỏng đoán cụ thể đang cần nó)? Cân nhắc bỏ.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Tiếng Anh | Nghĩa trong khoá |
| --- | --- | --- |
| Lô nhỏ / loạt nhỏ | small batch | Làm & tung từng mẩu nhỏ trọn vẹn, thay vì gom lô lớn |
| Dòng chảy một-lần-một | single-piece flow | Hoàn thành trọn một đơn vị rồi mới sang đơn vị kế; nhanh & bắt lỗi sớm hơn |
| Dây Andon | andon cord | Cơ chế cho phép bất kỳ ai dừng dây chuyền để sửa lỗi ngay khi phát hiện |
| Triển khai liên tục | continuous deployment | Tung thay đổi thành vô số mẩu tí hon (IMVU: 50 lần/ngày) |
| SMED | Single-Minute Exchange of Die | Kỹ thuật Toyota giảm thời gian chuyển đổi để làm lô nhỏ không bị phạt năng suất |
| Kéo | pull | Chỉ làm khi có nhu cầu thật kích hoạt (đối lập với đẩy/push suy diễn) |
| Đẩy | push | Làm sẵn hàng loạt theo dự báo, trữ kho — rủi ro tồn kho vô giá trị |

## 9. Câu hỏi tự kiểm tra

1. Trong cuộc đua gấp phong bì, vì sao **lô nhỏ (một-lần-một)** thắng dù trông kém hiệu quả? Nêu **hai** lý do.
2. **Dây Andon** làm gì? Vì sao "dừng cả dây chuyền vì một lỗi" lại dẫn tới *chất lượng cao + chi phí thấp*?
3. "Giảm kích cỡ lô" liên hệ thế nào với tốc độ vòng **Xây dựng–Đo lường–Học hỏi**? IMVU minh hoạ bằng con số nào?
4. Phân biệt **kéo (pull)** và **đẩy (push)**. Với startup, "kéo" một tính năng nghĩa là gì?
5. Vì sao lô nhỏ giúp **kéo dài đường băng** ([Bài 5](bai_05_pivot.md))?
6. "Lô nhỏ để nhanh" có mâu thuẫn với "chất lượng" không? Giải thích.

---

## Tóm tắt một trang

```
BÀI 6 — LÔ NHỎ & TRIỂN KHAI LIÊN TỤC  (Ch.9 "Loạt sản xuất", tr.210–234)
                                        [mở đầu Phần III "Tăng tốc"]

  CUỘC ĐUA GẤP PHONG BÌ:
    lô lớn (gấp hết → nhét hết → dán hết)  vs  LÔ NHỎ (trọn 1 bì rồi sang cái kế)
    → LÔ NHỎ NHANH HƠN (dù trông kém hiệu quả)

  VÌ SAO?  (1) trực giác quên chi phí phân loại/xếp chồng/đi lòng vòng
           (2) LÔ NHỎ PHÁT HIỆN LỖI SỚM  (bì lỗi → biết ngay, không hỏng cả mẻ)
    startup: "bì lỗi" = giả định sai → tung nhỏ, học ngay (tránh bẫy 6 tháng IMVU)

  DÂY ANDON (Toyota): ai cũng được DỪNG DÂY CHUYỀN để sửa lỗi ngay
    lợi ích sửa-sớm >> chi phí dừng  →  chất lượng CAO + chi phí THẤP

  TRIỂN KHAI LIÊN TỤC: IMVU giao hàng 50 LẦN/NGÀY
    giảm kích cỡ lô = chạy vòng BML nhanh hơn
    gốc kỹ thuật = SMED (chuyển đổi khuôn từng phút) của Toyota

  KÉO, ĐỪNG ĐẨY:
    đẩy = làm sẵn hàng loạt theo dự báo → tồn kho có thể thành vô giá trị
    KÉO = chỉ làm khi nhu cầu thật kích hoạt (Camry: dùng 1 → bổ sung 1)
    startup: tính năng phải được KÉO bởi 1 phỏng đoán cần kiểm, không ĐẨY suy diễn

  LÔ NHỎ = ĐỘNG CƠ TĂNG TỐC: vòng BML ngắn hơn → đường băng DÀI hơn (Bài 5)
    ≠ làm ẩu: tốc độ HỌC, không phải tốc độ cẩu thả
```

## Nguồn

- **Eric Ries**, *Khởi nghiệp Tinh gọn* — **Ch. 9 "Loạt sản xuất"** (tr. 210–234): thí nghiệm gấp phong bì, một-lần-một nhanh hơn (tr. 210–211); phát hiện lỗi sớm & dây Andon của Toyota (tr. 211, 213); SMED (tr. 212–213); triển khai liên tục, IMVU 50 lần/ngày & giảm lô để tăng tốc vòng BML (tr. 220); kéo, đừng đẩy — ví dụ chống va đập Camry (tr. 228). `tai_lieu/Khoi-Nghiep-Tinh-Gon-Eric-Ries.pdf`

---

**Bản đồ khoá học:** [Bài 0 — Vì sao khởi nghiệp cần lối quản trị riêng](bai_00_vi_sao_khoi_nghiep_can_quan_tri.md) · [Bài 1 — Học hỏi có kiểm chứng](bai_01_hoc_hoi_co_kiem_chung.md) · [Bài 2 — Vòng Xây dựng–Đo lường–Học hỏi](bai_02_vong_xay_dung_do_luong_hoc_hoi.md) · [Bài 3 — Phỏng đoán niềm tin & MVP](bai_03_phong_doan_niem_tin_va_mvp.md) · [Bài 4 — Kế toán cách tân](bai_04_ke_toan_cach_tan.md) · [Bài 5 — Điều chỉnh hay kiên định (Pivot)](bai_05_pivot.md) · [Bài 6 ← bạn đang ở đây] · [Bài 7 — Ba động cơ tăng trưởng](bai_07_ba_dong_co_tang_truong.md) · [Bài 8 — Thích nghi, cách tân & đừng lãng phí](bai_08_thich_nghi_cach_tan_dung_lang_phi.md)

Xem thêm [README khoá học](../README.md).
