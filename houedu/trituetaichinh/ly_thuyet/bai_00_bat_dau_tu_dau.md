# Bài 0 — Bắt đầu từ đâu

> Bài cầu nối, khoảng 40 phút. Không bám một chương nào của sách — nó chốt **quy ước trích dẫn**,
> dựng **bộ số liệu dùng chung cho cả khoá**, và giao **bài tập số 1**.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** không có. Đây là bài đầu tiên.
> Nếu đã học [Kinh tế vĩ mô EG14](../../eg14-kinhtevimo-macro/README.md) thì mục 5 sẽ quen tay.
> ⚙️ **Code:** [`thuc_hanh/bai-00-bat-dau-tu-dau.py`](../thuc_hanh/bai-00-bat-dau-tu-dau.py)
> — **máy dò lỗi** của mục 6: cộng lại từng cột phụ lục, tính lại từng tỷ lệ, rồi đối chiếu với con số
> sách in. Chưa tới 200 dòng, chỉ dùng thư viện chuẩn.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Cuốn sách này dạy gì, và cố tình không dạy gì](#1-cuốn-sách-này-dạy-gì-và-cố-tình-không-dạy-gì)
- [2. Quy ước trích dẫn — vì sao không có số trang giấy](#2-quy-ước-trích-dẫn--vì-sao-không-có-số-trang-giấy)
- [3. Ba báo cáo tài chính trong một trang](#3-ba-báo-cáo-tài-chính-trong-một-trang)
- [4. Công ty mẫu — một bộ số liệu cho cả khoá](#4-công-ty-mẫu--một-bộ-số-liệu-cho-cả-khoá)
- [5. 📚 GAAP, VAS và IFRS — sách viết theo khung nào](#5--gaap-vas-và-ifrs--sách-viết-theo-khung-nào)
- [6. ⚠️ Hai mươi tám chỗ sách in sai, và vì sao đó là bài tập số 1](#6--hai-mươi-tám-chỗ-sách-in-sai-và-vì-sao-đó-là-bài-tập-số-1)
- [7. Tự thử](#7-tự-thử)
- [8. 🇻🇳 Đối chiếu Việt Nam — Vinamilk 2024](#8--đối-chiếu-việt-nam--vinamilk-2024)
- [9. Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
- [10. Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Cuốn sách này dạy gì, và cố tình không dạy gì

Sách nói thẳng ở ngay chương 4:

> *"Ngay từ đầu chúng tôi đã nói rằng sẽ không dạy bạn về kế toán, vậy nên chúng tôi sẽ không
> làm thế. Tuy nhiên, có một khái niệm kế toán sẽ được chúng tôi giải thích trong chương này…"*
> — ch. 4 · PDF tr. 36

Khái niệm duy nhất đó là **nguyên tắc phù hợp** ([bài 2](bai_02_loi_nhuan_chi_la_du_toan.md)). Ngoài nó ra, cả cuốn sách không dạy
định khoản, không dạy sổ cái, không dạy bút toán. Mục tiêu khác hẳn: **đọc được ba báo cáo tài
chính, và biết chỗ nào đáng ngờ.**

Lời nói đầu đặt ra bốn nhóm kỹ năng. Đây là bản đồ để biết bài nào phủ nhóm nào:

```
   ① Thông hiểu kiến thức cơ bản     ba báo cáo tài chính            →  bài 2–7
   ② Thông hiểu THỦ THUẬT            ước tính, giả định, định kiến   →  bài 1, rải khắp
   ③ Thông hiểu phép phân tích       tỷ lệ, ROI                      →  bài 8–11
   ④ Thông hiểu bức tranh toàn cảnh  bối cảnh ngành, tổ chức         →  bài 12
```

⚠️ **Đừng nhầm nhóm ① là ruột sách.** Nhóm ② mới là. Một câu của chương 4 tóm gọn cả cuốn:

> *"Lợi nhuận luôn là dự toán — và bạn không thể chi tiêu một thứ được dự toán."*
> — ch. 4 · PDF tr. 40

Hay nói ngắn hơn: **lợi nhuận là một ý kiến, tiền mặt mới là sự thật.**

---

## 2. Quy ước trích dẫn — vì sao không có số trang giấy

[EG13](../../eg13-kinhtevimo-micro/README.md) và [EG14](../../eg14-kinhtevimo-macro/README.md)
trích được `tr. 315` vì giáo trình Mankiw là **bản quét** của sách in, giữ nguyên số trang.

Cuốn này thì không. Tệp PDF trong `tai_lieu/` là **ebook do calibre dàn lại**: 227 trang PDF,
trong khi bản in dày 350 trang. **Không có số trang giấy nào để mà trích.**

Nên quy ước của môn này là:

```
   ch. 23 · PDF tr. 162
   └──┬──┘   └────┬────┘
      │           └── số trang trong tệp PDF ở tai_lieu/ — tra được ngay
      └── số chương — mốc bền, đúng với mọi ấn bản, mọi bản dịch
```

Chương luôn đứng trước, vì nếu ai đó cầm bản in giấy hay bản tiếng Anh thì số chương vẫn dùng
được, còn số trang PDF thì không.

---

## 3. Ba báo cáo tài chính trong một trang

Toàn bộ phần II đến phần IV của sách là ba tài liệu. Trước khi đi vào từng cái, đây là chỗ chúng
khác nhau — bảng này đáng dán lên tường:

|                        | Báo cáo kết quả kinh doanh     | Bảng cân đối kế toán         | Báo cáo lưu chuyển tiền tệ  |
| ---------------------- | ------------------------------ | ---------------------------- | --------------------------- |
| Trả lời câu hỏi        | có lãi không?                  | đang sở hữu gì, nợ ai?       | tiền thật vào ra bao nhiêu? |
| Thời gian              | một **khoảng** (tháng/quý/năm) | một **thời điểm** (một ngày) | một **khoảng**              |
| Ẩn dụ của sách         | phiếu báo điểm                 | ảnh chụp                     | sao kê ngân hàng            |
| Bao nhiêu "nghệ thuật" | **rất nhiều**                  | nhiều                        | **ít nhất**                 |
| Bài                    | 2–3                            | 4–5                          | 6–7                         |

Cột cuối là điều đáng nhớ nhất. Sách viết:

> *"Đúng như những gì mà Warren Buffet nhận thấy, ở báo cáo này không có nhiều chỗ để chơi trò
> tiểu xảo với các con số, như trong các loại báo cáo khác. Tuy nhiên, cần nói rõ rằng 'không có
> nhiều chỗ' không có nghĩa là 'không có chỗ'."* — ch. 16 · PDF tr. 124

Và ba báo cáo **không độc lập**. Chúng khoá chặt vào nhau — [bài 5](bai_05_vi_sao_bang_can_doi_lai_can.md)
và [bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) sẽ dựng lại từng mối
nối. Ở đây chỉ cần nhớ hình dạng:

```
   BÁO CÁO KQKD          BẢNG CÂN ĐỐI KẾ TOÁN         BÁO CÁO LƯU CHUYỂN TIỀN TỆ
   ────────────          ────────────────────         ──────────────────────────
   Doanh thu                Tài sản                      Lợi nhuận thuần  ◄──┐
     − Giá vốn                 = Nợ phải trả               + Khấu hao        │
   = Lợi nhuận gộp             + Vốn chủ sở hữu            ± thay đổi các    │
     − Chi phí                         ▲                     dòng vốn lưu    │
   = Lợi nhuận thuần ──────────────────┘                      động   ◄───────┼── từ chênh lệch
                        cộng vào "lợi nhuận giữ lại"    = Tiền từ HĐKD       │   HAI bảng cân đối
                                                                             │
                                                        Tiền cuối kỳ ────────┘
                                                        quay lại dòng "Tiền" của bảng cân đối
```

---

## 4. Công ty mẫu — một bộ số liệu cho cả khoá

Sách có **đúng một** bộ báo cáo tài chính, nằm ở phụ lục (PDF tr. 223–227), và mọi chương từ 15
đến 28 đều tính toán trên nó. Nên cả khoá học này cũng dùng đúng một bộ.

`thuc_hanh/cong_ty_mau.py` là **hạ tầng dùng chung, không sửa**. Bài 2 đến bài 11 đều mở đầu bằng:

```python
from cong_ty_mau import KQKD, BCDKT, LCTT, tong_tai_san, von_chu_so_huu
```

Chạy thẳng nó để xem ba báo cáo:

```bash
cd thuc_hanh && python3 cong_ty_mau.py
```

⚠️ File này **tự kiểm bằng `assert` ngay khi import** — bảng cân đối phải cân ở cả hai năm, mười
một dòng của báo cáo lưu chuyển tiền tệ phải tái lập được từ chênh lệch hai bảng cân đối, lợi
nhuận giữ lại phải cuộn chiếu đúng. Lý do rất thực tế: **nếu gõ y nguyên theo sách thì bảng cân
đối không cân.** Xem mục 6.

---

## 5. 📚 GAAP, VAS và IFRS — sách viết theo khung nào

Sách là sách Mỹ, viết theo **GAAP** (*generally accepted accounting principles*). Sách tự định
nghĩa nó, và con số nó đưa ra đáng nhớ:

> *"Bộ tiêu chuẩn GAAP — các quy tắc kế toán được thừa nhận phổ quát dùng để kiểm soát cách ghi
> sổ sách của các kế toán viên ở Mỹ — **dày đến 4.000 trang** và có rất nhiều quy tắc chi tiết.
> Bạn có thể tưởng rằng GAAP sẽ quy định: 'giám đốc sản xuất không được tính' hoặc 'quản đốc thì
> tính'. Không may mắn như vậy, GAAP chỉ cung cấp cho ta các định hướng."* — ch. 7 · PDF tr. 57

⭐ Đây là chỗ mấu chốt của cả cuốn sách, và nó **không phụ thuộc vào khung kế toán nào**: bốn nghìn
trang quy tắc mà vẫn không nói được lương quản đốc nhà máy có nằm trong giá vốn hàng bán hay không.
Sách chốt bằng hai chữ — *"hợp lý và nhất quán"*:

> *"Chừng nào logic của doanh nghiệp vẫn còn hợp lý và chừng nào logic đó vẫn còn được áp dụng
> nhất quán, thì chừng đó doanh nghiệp muốn làm gì cũng được."* — ch. 7 · PDF tr. 57

**Ở Việt Nam khung khác, nhưng khoảng trống thì giống hệt.** Doanh nghiệp Việt Nam lập báo cáo
theo **VAS** — chế độ kế toán doanh nghiệp hiện hành. Một số công ty niêm yết lớn công bố **song
song** cả bản **IFRS**. Tên gọi dòng khác nhau, cách phân loại khác nhau, nhưng chỗ mà kế toán
viên phải **phán đoán** thì y hệt: khi nào ghi nhận doanh thu, khấu hao mấy năm, chi phí nào
"trên vạch", dự phòng bao nhiêu.

🇻🇳 Và điều này đo được bằng số thật — xem mục 8.

---

## 6. ⚠️ Hai mươi tám chỗ sách in sai, và vì sao đó là bài tập số 1

Đây là một cuốn sách có luận điểm trung tâm là **"đừng tin các con số"**. Bản dịch của nó in sai
**28 chỗ**. Đó không phải phiền toái — đó là cơ hội sư phạm tốt nhất mà cả khoá học có.

**Bài tập số 1 của môn này: đừng tin con số của chính cuốn sách.**

Đừng đọc bảng đính chính đầy đủ ở [README](../README.md) vội. Hãy tự làm ba việc sau trước, chỉ
cần giấy bút:

1. Mở phụ lục (PDF tr. 224). **Cộng tay cột tài sản năm 2005.** So với dòng "Tổng tài sản".
2. Mở chương 20 (PDF tr. 150), chỗ tính ROA. **Nhìn kỹ mẫu số.** Nó ghi nhãn là gì, và in số bao nhiêu?
3. Mở chương 15 (PDF tr. 114). Bảng của Sweet Dreams nói tiệm **lỗ cả ba tháng**. Nhưng đoạn văn
   ngay phía trên bảng nói gì? **Hai cái đó có khớp nhau không?**

Xong ba việc đó rồi hãy chạy **máy dò lỗi** để đối chiếu:

```bash
cd thuc_hanh && python3 bai-00-bat-dau-tu-dau.py
```

Nó cộng lại từng cột, tính lại từng tỷ lệ, và đối chiếu với con số sách in — chưa tới 200 dòng,
chỉ dùng thư viện chuẩn của Python. Kết quả: **bắt được 14 trong 28 chỗ** — đúng một nửa. Mười bốn chỗ
còn lại là lỗi chữ nghĩa, máy không thấy được, phải đọc bằng mắt.

⭐ Chỗ đáng chú ý nhất nằm ở chương 25: **IRR 14,36% thì đúng**, nhưng hai mốc NPV mà sách dùng để
dẫn tới nó (212 và −218; đúng ra là 233 và −262) thì sai. Kết quả cuối đúng mà đường đi tới nó
sai — đúng kiểu lỗi chỉ tính lại mới phát hiện được, đọc thì không.

### Bốn loại lỗi, và loại nào nguy hiểm nhất

| Loại              | Ví dụ                                                                                    | Mức nguy hiểm                             |
| ----------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Lỗi biên tập**  | *"Sunteam"* thay vì Sunbeam; *"PDO"* thay vì DPO                                         | thấp — đọc là biết                        |
| **Lỗi số**        | tổng tài sản in 5.133 thay vì 5.193                                                      | trung bình — tính lại là ra               |
| **Lỗi dấu**       | ch. 15 in hai bảng đảo dấu cho nhau: lãi thành lỗ                                        | cao — đổi nghĩa cả bảng                   |
| **Lỗi khái niệm** | ch. 26 xếp **khoản phải trả** vào tài sản ngắn hạn và **khoản phải thu** vào nợ ngắn hạn | ⚠️⚠️ **cao** — đọc xuôi tai, và **dạy sai** |

Loại **khái niệm** mới đáng sợ. Nó không làm sai một phép tính nào cả; nó cài một khái niệm ngược vào
đầu người đọc. [Bài 4](bai_04_bang_can_doi_ke_toan.md) và bài 11 sẽ quay lại đúng chỗ này, còn
[bài 12 mục 9](bai_12_to_chuc_co_tri_tue_tai_chinh.md#9-sổ-tổng-kết--mọi-chỗ-sách-in-sai) đếm đủ cả bốn loại.

---

## 7. Tự thử

1. **Tổng tài sản 2004.** Sách in 5.354 cho năm 2004. Cộng tay cột đó. Sách in **đúng** hay **sai**?
   Nếu đúng, tại sao chỉ cột 2005 sai? Điều đó gợi ý lỗi phát sinh ở khâu nào?

2. **Đảo ngược máy dò.** Trong `cong_ty_mau.py`, sửa `"tien": 83` thành `"tien": 84`. Chạy lại.
   **Bao nhiêu** `assert` gãy, và cái nào gãy trước? Nhớ sửa lại.

3. **Vòng quay tổng tài sản.** Máy dò chứng minh 5.193 mới đúng, bằng cách dùng ngược
   con số 1,67 của chương 23. Tìm **một tỷ lệ khác** trong sách cũng dùng tổng tài sản làm mẫu số,
   và kiểm xem nó ủng hộ 5.193 hay 5.133.

4. **Sweet Dreams sang tháng thứ tư.** Trong hàm `mo_phong`, thêm tháng 4 với doanh thu 60.000.
   Lợi nhuận tháng 4 bao nhiêu? Số dư tiền mặt bao nhiêu? **Khoảng cách giữa hai con số đó đang
   giãn ra hay thu hẹp lại?**

5. **Đổi điều khoản thanh toán.** Vẫn Sweet Dreams, đổi `tre_thu` từ 2 xuống 1 (khách trả trong
   30 ngày thay vì 60). Tiệm còn cạn tiền không? Đây là bài toán bài 11 sẽ làm nghiêm túc.

6. **Fine Cigar cắt chi phí.** Chi phí hoạt động 30.000/tháng đang giết cửa hàng. Tìm mức chi phí
   **cao nhất** mà cửa hàng vẫn có lãi ngay từ tháng 1. Gợi ý: giải theo biên lợi nhuận gộp 30%.

---

## 8. 🇻🇳 Đối chiếu Việt Nam — Vinamilk 2024

`thuc_hanh/doi_chieu_viet_nam.py` dựng báo cáo tài chính hợp nhất **đã kiểm toán** của **Công ty
Cổ phần Sữa Việt Nam (HOSE: VNM)** năm 2024, lập theo **IFRS**, in trong Báo cáo thường niên
Vinamilk 2024, tr. 180–185. Toàn bộ số liệu tự cân bằng `assert` như công ty mẫu.

```bash
cd thuc_hanh && python3 doi_chieu_viet_nam.py
```

Cùng **14 công thức**, hai doanh nghiệp cách nhau 19 năm và nửa vòng trái đất. Ba chỗ đáng dừng lại:

| Tỷ lệ                      | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| -------------------------- | ---------------------: | ------------------: |
| Hệ số thanh toán lãi vay   |               3,41 lần |       **30,28 lần** |
| Chu kỳ chuyển đổi tiền mặt |              74,1 ngày |       **21,8 ngày** |
| Biên lợi nhuận gộp         |                  22,2% |               28,8% |
| Vòng quay tổng tài sản     |           **1,67 lần** |            0,92 lần |
| ⟹ ROA                      |                   4,8% |           **15,2%** |

Hai dòng cuối là bài học lớn nhất: Vinamilk có **biên lợi nhuận cao hơn** nhưng **vòng quay tài
sản thấp hơn hẳn**. Hai con đường rất khác nhau dẫn tới hai mức ROA rất khác nhau. Đó chính là
**phân rã DuPont** — bài 9.

> ⚠️ **Đây là bản IFRS, không phải bản VAS.** Vinamilk công bố song song hai bộ báo cáo, và **hai
> bộ cho hai con số tổng tài sản khác nhau** cho cùng một công ty, cùng một ngày.
>
> Chênh lệch đó **không phải lỗi của ai cả.** Đó là hai khung kế toán áp lên cùng một doanh nghiệp
> — chính xác là *"nghệ thuật tài chính"* mà chương 1–3 nói tới, lần này bằng số liệu Việt Nam
> chứ không phải ví dụ Mỹ năm 2005.

---

## 9. Từ điển thuật ngữ

| Tiếng Việt                  | Tiếng Anh                                   | Nghĩa ngắn                                                               |
| --------------------------- | ------------------------------------------- | ------------------------------------------------------------------------ |
| Trí tuệ tài chính           | financial intelligence                      | bốn nhóm kỹ năng ở mục 1 — **không phải** năng khiếu bẩm sinh            |
| Nghệ thuật tài chính        | the art of finance                          | chỗ mà kế toán phải **phán đoán**, vì không quy tắc nào phủ hết          |
| Báo cáo kết quả kinh doanh  | income statement                            | có lãi không, trong **một khoảng** thời gian                             |
| Bảng cân đối kế toán        | balance sheet                               | sở hữu gì và nợ ai, tại **một thời điểm**                                |
| Báo cáo lưu chuyển tiền tệ  | cash flow statement                         | tiền thật vào ra — ít "nghệ thuật" nhất                                  |
| Nguyên tắc phù hợp          | matching principle                          | khớp chi phí với **doanh thu mà nó tạo ra**, không phải với lúc chi tiền |
| GAAP                        | generally accepted accounting principles    | bộ quy tắc kế toán Mỹ, ~4.000 trang, vẫn để lại khoảng trống phán đoán   |
| 🇻🇳 VAS                       | Vietnamese Accounting Standards             | chuẩn mực kế toán Việt Nam — **không có trong sách**                     |
| 🇻🇳 IFRS                      | International Financial Reporting Standards | chuẩn mực quốc tế; một số công ty niêm yết VN công bố song song          |
| 📚 Kế toán dựa trên tiền mặt | cash basis accounting                       | ghi nhận khi tiền đổi tay; chỉ doanh nghiệp rất nhỏ dùng                 |

---

## 10. Câu hỏi tự kiểm tra

1. Cuốn sách này **cố tình không dạy** cái gì? Nó phá lệ đúng **một** khái niệm kế toán — khái niệm nào? (mục 1)
2. Kể bốn nhóm kỹ năng của lời nói đầu. Nhóm nào là ruột của sách, và vì sao **không phải** nhóm ①? (mục 1)
3. Vì sao môn này trích `ch. 23 · PDF tr. 162` chứ không trích `tr. 162` như EG13 và EG14? (mục 2)
4. Ba báo cáo tài chính: cái nào đo **một khoảng thời gian**, cái nào đo **một thời điểm**? (mục 3)
5. Báo cáo nào ít "nghệ thuật tài chính" nhất? Sách có nói nó **hoàn toàn** không thể tác động được không? (mục 3)
6. Lợi nhuận thuần từ báo cáo kết quả kinh doanh chảy vào **dòng nào** của bảng cân đối kế toán? (mục 3)
7. Vì sao `cong_ty_mau.py` phải tự kiểm bằng `assert` thay vì chỉ chứa số liệu? (mục 4)
8. GAAP dày bao nhiêu trang, mà vẫn không trả lời được câu hỏi nào của chương 7? (mục 5)
9. Hai chữ mà sách dùng để chốt vấn đề đó là gì? (mục 5)
10. Kể bốn loại lỗi in trong bản dịch. Loại nào nguy hiểm nhất và **vì sao**? (mục 6)
11. Tổng tài sản 2005: sách in bao nhiêu, đúng là bao nhiêu? Dùng **con số nào của chính sách** để chứng minh? (mục 6–7)
12. Trong công thức ROA của chương 20, nhãn mẫu số ghi gì và số in ra là gì? Kết quả 4,8% đúng hay sai? (mục 6)
13. Sweet Dreams (ch. 15) **có lãi** mà hết sạch tiền; Fine Cigar **lỗ** mà tiền mặt tăng đều. Giải thích cả hai. (mục 6)
14. Bằng chứng nào **trong chính cuốn sách** chứng minh bảng Sweet Dreams ở chương 15 in sai dấu? (mục 6)
15. Ở chương 25, IRR 14,36% đúng nhưng hai mốc NPV dẫn tới nó thì sai. Loại lỗi này nguy hiểm ở chỗ nào? (mục 6)
16. Vinamilk có biên lợi nhuận gộp **cao hơn** công ty mẫu nhưng vòng quay tổng tài sản **thấp hơn**.
    Vậy mà ROA lại cao hơn gấp ba. Bằng cách nào? (mục 8)
17. Vì sao bản IFRS và bản VAS của cùng một công ty, cùng một ngày, cho hai con số tổng tài sản khác nhau —
    và vì sao đó **không** phải lỗi? (mục 8)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 0 — BẮT ĐẦU TỪ ĐÂU                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  SÁCH DẠY GÌ:  đọc ba báo cáo tài chính + biết chỗ nào đáng ngờ          ║
║  SÁCH KHÔNG DẠY:  kế toán. Phá lệ đúng 1 khái niệm — nguyên tắc phù hợp  ║
║                                                                          ║
║  BỐN NHÓM KỸ NĂNG        ① cơ bản  ② THỦ THUẬT  ③ phân tích  ④ toàn cảnh ║
║                                     ↑ ruột của sách                      ║
║                                                                          ║
║  ⭐ LỢI NHUẬN LÀ MỘT Ý KIẾN.  TIỀN MẶT MỚI LÀ SỰ THẬT.                   ║
║                                                                          ║
║  TRÍCH DẪN:  ch. N · PDF tr. M   — PDF là ebook, KHÔNG có số trang giấy  ║
║                                                                          ║
║  BA BÁO CÁO                                                              ║
║     KQKD          khoảng thời gian   phiếu báo điểm    nhiều "nghệ thuật"║
║     Cân đối       một thời điểm      ảnh chụp                            ║
║     Lưu chuyển    khoảng thời gian   sao kê            ÍT "nghệ thuật"   ║
║     → ba cái KHOÁ CHẶT vào nhau: bài 5 và bài 7 dựng lại từng mối nối    ║
║                                                                          ║
║  HẠ TẦNG    thuc_hanh/cong_ty_mau.py        phụ lục sách — dùng chung    ║
║             thuc_hanh/doi_chieu_viet_nam.py Vinamilk 2024 IFRS           ║
║             cả hai TỰ KIỂM bằng assert khi import                        ║
║                                                                          ║
║  BÀI TẬP SỐ 1:  ĐỪNG TIN CON SỐ CỦA CHÍNH CUỐN SÁCH                      ║
║     bản dịch in sai 28 chỗ — máy dò ở thuc_hanh/ bắt được 14             ║
║     · tổng tài sản  5.133  →  5.193   (ch. 23 tự tố cáo bằng vòng quay)  ║
║     · ROA mẫu số    8.689  →  5.193   (dán nhầm dòng doanh thu)          ║
║     · ch. 15 hai bảng ĐẢO DẤU cho nhau                                   ║
║     · ⚠️ nguy nhất: ch. 26 xếp phải TRẢ vào tài sản, phải THU vào nợ     ║
║                                                                          ║
║  🇻🇳 VIỆT NAM   thanh toán lãi vay  3,41  →  30,28 lần                    ║
║               chu kỳ tiền mặt     74,1  →  21,8 ngày                     ║
║               ROA  4,8% → 15,2%, nhưng vòng quay 1,67 → 0,92 (DuPont)    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf` — **227 trang PDF, không mang số
  trang của bản in 350 trang**.
  - Lời giới thiệu của Alphabooks (PDF tr. 3) — ví dụ Sweet Dreams quy ra VND, **dấu đúng**
  - Lời nói đầu *Thế nào là trí tuệ tài chính?* (PDF tr. 5–8) — bốn nhóm kỹ năng
  - Ch. 4 *Lợi nhuận chỉ là dự toán* (PDF tr. 36–40) — nguyên tắc phù hợp
  - Ch. 7 *Chi phí và nợ phải trả* (PDF tr. 54–65) — GAAP 4.000 trang, "hợp lý và nhất quán"
  - Ch. 15 *Lợi nhuận ≠ tiền mặt* (PDF tr. 113–120) — Sweet Dreams và Fine Cigar
  - Ch. 16 *Ngôn ngữ của báo cáo lưu chuyển tiền tệ* (PDF tr. 121–124) — nhận xét của Buffett
  - Ch. 20 *Các tỷ lệ lợi nhuận* (PDF tr. 148–154) — ROA
  - Ch. 23 *Các tỷ lệ thể hiện hiệu suất hoạt động* (PDF tr. 162–167) — DII, DSO, DPO, vòng quay
  - Ch. 25 *Tính tỷ lệ hoàn vốn đầu tư* (PDF tr. 179–188) — payback, NPV, IRR
  - Ch. 28 *Tập trung chuyển đổi tiền mặt* (PDF tr. 203–206) — chu kỳ chuyển đổi tiền mặt
  - Phụ lục (PDF tr. 223–227) — ba báo cáo tài chính của công ty mẫu
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán cho năm
  kết thúc 31/12/2024, lập theo IFRS. Trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026.
- **Đã kiểm chứng bằng code** — xem [`thuc_hanh/bai-00-bat-dau-tu-dau.py`](../thuc_hanh/bai-00-bat-dau-tu-dau.py):
  máy dò tìm được **14** chỗ in sai; bảng đính chính đầy đủ **20** chỗ ở [README](../README.md).
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Toàn bộ [mục 8 — Đối chiếu Việt Nam](#8--đối-chiếu-việt-nam--vinamilk-2024) **nằm ngoài sách**.
  - Bảng so sánh ba báo cáo ở [mục 3](#3-ba-báo-cáo-tài-chính-trong-một-trang) do bài này dựng;
    sách trình bày ba báo cáo rời ở ba phần khác nhau, không đặt cạnh nhau.
  - Thuật ngữ **VAS** và **IFRS** ở [mục 5](#5--gaap-vas-và-ifrs--sách-viết-theo-khung-nào)
    **không có trong sách** — sách chỉ nói về GAAP của Mỹ.
  - ⚠️ Bài này **không dẫn con số tổng tài sản theo VAS của Vinamilk**, vì chưa lấy được bản VAS
    từ nguồn gốc. Hai bài báo đã cho hai con số khác nhau — đúng kiểu sai lầm mà chương 1 cảnh báo.
- **Liên hệ chéo:**
  - Giá trị hiện tại, chiết khấu, NPV và IRR:
    [EG14 bài 5](../../eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).
  - Chi phí cơ hội:
    [EG13 bài 1](../../eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md).

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| **0** | **Bắt đầu từ đâu** ← *bạn đang ở đây* | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
