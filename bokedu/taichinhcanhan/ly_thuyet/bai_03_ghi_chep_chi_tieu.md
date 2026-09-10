# Bài 3 — Ghi chép chi tiêu và phương pháp Kakeibo

> Bài học dựa trên **Unit 2 Lesson 1–2 của Class 1** — C1 tr. 7–10.
>
> **Cần đọc trước:** [Bài 2](bai_02_do_hien_trang.md) — bài này cung cấp **dữ liệu** cho hai công
> thức mà bài 2 dựng ra. Không có sổ ghi chép thì dòng tiền chỉ là con số đoán.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Code:** [`thuc_hanh/bai-03-ghi-chep-bao-lau.py`](../thuc_hanh/bai-03-ghi-chep-bao-lau.py)
> — trả lời bằng số cho chỉ dẫn *"3-6 tháng"* mà sách đưa ra không kèm lý do. Mục 6.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Công việc đầu tiên](#1-công-việc-đầu-tiên)
- [2. Phản biện của chính sách, và câu trả lời](#2-phản-biện-của-chính-sách-và-câu-trả-lời)
- [3. Kakeibo — bốn câu hỏi](#3-kakeibo--bốn-câu-hỏi)
- [4. [đính chính] Sách tự mâu thuẫn: app hay giấy bút?](#4-đính-chính-sách-tự-mâu-thuẫn-app-hay-giấy-bút)
- [5. [đính chính] Hai khẳng định không nguồn](#5-đính-chính-hai-khẳng-định-không-nguồn)
- [6. [bổ sung] Vì sao 3–6 tháng, và vì sao 3–6 tháng vẫn chưa đủ](#6-bổ-sung-vì-sao-36-tháng-và-vì-sao-36-tháng-vẫn-chưa-đủ)
- [7. [bổ sung] Câu hỏi số 2 của Kakeibo đã là "trả cho mình trước" — từ năm 1904](#7-bổ-sung-câu-hỏi-số-2-của-kakeibo-đã-là-trả-cho-mình-trước--từ-năm-1904)
- [8. Bốn mẹo cải thiện, và tên thật của chúng](#8-bốn-mẹo-cải-thiện-và-tên-thật-của-chúng)
- [9. Tự thử](#9-tự-thử)
- [10. Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
- [11. Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Công việc đầu tiên

Sách đặt tên cho Lesson 1 là *"Công việc đầu tiên"*, và câu mở đầu nói rõ vì sao:

> *"Lập kế hoạch tài chính bắt đầu bằng việc ghi chép lại những khoản thu chi. Điều này khiến bạn
> hướng sự chú tâm vào tiền bạc."* — C1 tr. 7

Chú ý sách **không** nói ghi chép giúp bạn tiêu ít đi. Nó nói ghi chép khiến bạn **chú tâm**. Đó là
một khẳng định khiêm tốn hơn và đúng hơn, và mục 5 sẽ cho thấy nó là phần chắc chắn nhất trong cả
hai lesson.

Vị trí của bài này trong mạch khoá học rất rõ:

```
   bài 3  ─────────────▶  bài 2  ─────────────▶  bài 7
   ghi chép                dòng tiền              phân bổ thu nhập
   (dữ liệu thô)           tài sản ròng           (quyết định)
                           (đo lường)

   Không có bài 3 thì bài 2 chỉ là hai công thức không có số để điền.
```

Sách nói thẳng cái giá phải trả và cái nhận lại:

> *"Bạn đổi chút ít sự thoải mái hôm nay lấy sự dư dả ngày mai. Quản lý tiền không đồng nghĩa với
> việc bạn phải 'thắt lưng buộc bụng', chỉ yêu cầu tính kỷ luật và sự kiên nhẫn."* — C1 tr. 8

Và nó đặt một chỉ tiêu cụ thể — con số duy nhất trong Lesson 1, mà mục 6 sẽ đem ra kiểm:

> *"Ghi chép một cách kỷ luật và kiên trì trong vòng **3-6 tháng**, bạn sẽ nhận ra hiện trạng bức
> tranh tài chính của bản thân cũng như gia đình."* — C1 tr. 7

---

## 2. Phản biện của chính sách, và câu trả lời

Chỗ đáng khen nhất của Lesson 1 là sách **tự viết ra lời phản đối** thay vì lờ nó đi:

> *"Bạn có thể nói 'Dù sao đây cũng là tiền của tôi, do tôi làm ra, tôi muốn được thoải mái trong
> việc sử dụng tiền. Đến cuối tháng còn bao nhiêu sẽ để dành cho tiết kiệm. Tại sao phải ghi chép một
> cách phiền phức thế làm gì?'"* — C1 tr. 7

Và câu trả lời không hề lên lớp:

> *"Suy nghĩ đó đúng. Bạn làm gì với tiền của bạn là việc cá nhân. Bạn không thể sai được, dĩ nhiên.
> Chỉ là, có một cách tốt hơn."* — C1 tr. 7

Lý lẽ mà sách đưa ra sau đó là **thực nghiệm**, không phải đạo đức: cách "cuối tháng còn bao nhiêu
thì để dành" cho ra kết quả tệ.

> *"Kể cả chắt bóp mấy, việc tiết kiệm của bạn cũng sẽ chập chờn tháng có tháng không, tháng nhiều
> tháng ít."* — C1 tr. 7–8

Chữ **"chập chờn"** đáng nhớ, vì [bài 2](bai_02_do_hien_trang.md#2-dòng-tiền--bước-1-của-sách) đã
gặp nó: C1 tr. 12 xếp *"lúc âm, lúc dương không ổn định"* vào **cùng nhóm với dòng tiền âm**. Hai
chỗ nói cùng một điều — dao động tự nó là một vấn đề, không chỉ mức trung bình. Mục 7 đo cái chập
chờn ấy bằng số.

Đoạn tiếp theo mô tả một cơ chế tâm lý mà sách không gọi tên:

> *"Sau đó, bạn sẽ nhìn lên những người xung quanh. Không phải 'nhìn sang' những người giống mình mà
> 'nhìn lên' những người hơn mình… Bạn thoáng ghen tỵ với thành công của họ."* — C1 tr. 8

Đó là **so sánh xã hội hướng lên**, và nó nối thẳng với hai chỗ khác: quy tắc *"không so sánh Net
worth với người khác khi chưa hiểu rõ tình hình của họ"* ở [bài 2](bai_02_do_hien_trang.md#6-vì-sao-tài-sản-ròng-quan-trọng-hơn-lương),
và người có chiếc ô tô mà tài sản ròng âm 90 triệu. **Bài 10** gom chúng lại.

---

## 3. Kakeibo — bốn câu hỏi

> *"Kakeibo (家計簿 – kah keh boh) có nghĩa là 'Sổ ghi chép chi tiêu tài chính'. Phương pháp này có
> nguồn gốc từ nước Nhật, do nữ nhà báo Hani Motoko sáng tạo vào năm 1904, giúp phụ nữ Nhật biết
> cách kiểm soát hiện trạng tài chính của gia đình."* — C1 tr. 8

Phần lịch sử này sách viết **chính xác**, và đáng để ý: đây là công cụ tài chính cá nhân ra đời
trước cả khi có thẻ tín dụng, và nó vẫn còn dùng được.

Kakeibo là **bốn câu hỏi**, hỏi theo đúng thứ tự đó:

```
   1. Bạn có bao nhiêu tiền?              lương, lãi tiết kiệm, việc bán thời gian…
      ─────────────────────────

   2. Bạn muốn tiết kiệm bao nhiêu?       "cất riêng khoản này TRƯỚC"
      ─────────────────────────           ↑ mục 7 nói về đúng chữ "trước" này

   3. Bạn sẽ tiêu bao nhiêu tiền?         ghi hàng ngày, chia làm bốn nhóm
      ─────────────────────────

   4. Bạn sẽ làm gì để cải thiện?         cuối tháng ngồi lại, xem lại toàn bộ
      ─────────────────────────
                                                                    C1 tr. 9
```

Bốn nhóm chi tiêu của câu hỏi 3, kèm đúng ví dụ sách đưa (C1 tr. 9):

| Nhóm | Ví dụ của sách |
| --- | --- |
| **Thiết yếu** | ăn uống, phương tiện đi lại, hoá đơn điện/nước/internet |
| **Sở thích** | ăn ngoài, mua sắm |
| **Bồi dưỡng tâm hồn và thư giãn** | mua sách, khoá học trực tuyến, đi xem phim, thể thao |
| **Khoản chi tiêu bất thường** | cưới hỏi, đầy tháng con, sửa chữa xe máy |

### Bốn nhóm này khác với sáu chiếc lọ ở chỗ nào

Người đọc tiếp Class 2 sẽ gặp ba hệ phân bổ thu nhập nữa. Chúng **không cùng loại** với bốn nhóm ở
trên, và lẫn hai thứ này là hỏng cả hai:

|  | Bốn nhóm Kakeibo | Sáu chiếc lọ, 50/30/20, 70/30 |
| --- | --- | --- |
| Làm khi nào | **sau khi** tiêu, để ghi lại | **trước khi** tiêu, để quyết định |
| Trả lời | tiền đã đi đâu? | tiền được phép đi đâu? |
| Bài | 3 | 7 |

Đặt cạnh nhau thì thấy chỗ khớp và chỗ hụt:

```
   Kakeibo (ghi lại)                6 jars (quyết trước)
   ─────────────────                ────────────────────
   Thiết yếu            ←→          NEC    55%
   Sở thích             ←→          PLAY   10%
   Bồi dưỡng tâm hồn    ←→          EDU    10%
   Chi bất thường       ←→          (không có lọ nào)
                                    GIVE    5%   ← Kakeibo không có nhóm này
                                    FFA    10%   ┐ nằm ở CÂU HỎI 2 của Kakeibo,
                                    LTSS   10%   ┘ không nằm trong bốn nhóm chi
```

Hai chỗ lệch đều có nghĩa. **FFA và LTSS** không nằm trong bốn nhóm vì Kakeibo đã cất chúng đi từ
câu hỏi 2 — tiết kiệm không phải một hạng mục chi tiêu. Còn **nhóm "chi bất thường"** thì không có
lọ nào tương ứng, và mục 6 cho thấy đó là nhóm nguy hiểm nhất.

---

## 4. [đính chính] Sách tự mâu thuẫn: app hay giấy bút?

Hai trang liền nhau, hai lời khuyên ngược nhau.

**Trang 7** — Lesson 1:

> *"Hoặc bạn **nên dùng các app** quản lý tiền trên điện thoại như Money Lover, Fast Budget…"*
> — C1 tr. 7

**Trang 8** — Lesson 2, mở đầu phần Kakeibo:

> *"Phương pháp này chỉ cần một quyển sổ và một cây bút để ghi chép lại mọi khoản thu chi (**không
> sử dụng các app** quản lý tài chính hiện đại)."* — C1 tr. 8

Một trang bảo nên dùng app, trang sau bảo không dùng app. Sách không hề nhắc tới sự đối lập này.

### Cách gỡ, và nó nằm ngay trong chính cuốn sách

Sách tự cung cấp tiêu chí quyết định, ở cuối Lesson 2:

> *"lợi ích lớn nhất của Kakeibo là yêu cầu bạn phải **chú tâm** vào những khoản thu chi hàng tháng
> của mình."* — C1 tr. 10

Nếu thứ cần đạt là **chú tâm**, thì hai công cụ mạnh ở hai việc khác nhau:

| | Sổ và bút | App |
| --- | --- | --- |
| **Đầy đủ** | dễ quên, dễ bỏ sót khoản lẻ | tự đồng bộ ngân hàng, gần như không sót |
| **Chú tâm** | mỗi khoản là một lần dừng lại | tự động ⟹ **có thể chẳng chú tâm gì cả** |
| Công sức mỗi ngày | vài phút | gần bằng không |
| Bỏ cuộc sau vài tuần | hay xảy ra | ít hơn |

App tự động hoá đúng cái phần mà Kakeibo cố tình giữ lại. Sao kê đầy đủ tới từng đồng mà không ai
mở ra đọc thì không đem lại chú tâm nào.

Cách dùng được, và mục 6 sẽ củng cố nó: **app cho ba nhóm đều đặn** (đầy đủ, tốn ít công), **sổ tay
cho những khoản bạn còn đang cân nhắc** (chú tâm, ít khoản nhưng đáng dừng lại). Còn nếu phải chọn
một: chọn cái bạn sẽ thật sự làm được đủ sáu tháng. Công cụ tốt nhất là công cụ không bị bỏ giữa chừng.

---

## 5. [đính chính] Hai khẳng định không nguồn

Lesson 2 đưa ra hai khẳng định mạnh, cạnh nhau, không kèm nguồn nào.

### "Tiết kiệm được 35% tổng thu nhập"

> *"Theo thống kê, bạn có thể tiết kiệm được **35%** tổng thu nhập của gia đình hoặc thu nhập cá
> nhân khi áp dụng Kakeibo."* — C1 tr. 8

Ba chữ *"theo thống kê"* là toàn bộ phần dẫn nguồn. Không có nghiên cứu, không có cỡ mẫu, không có
năm.

Có một cách kiểm mà không cần đi tìm nguồn: **đặt con số đó cạnh chính lời khuyên của cuốn sách.**

| Tỷ lệ tiết kiệm | Nguồn trong sách | Số năm tới tự do tài chính |
| ---: | --- | ---: |
| **35%** | C1 tr. 8 — *"áp dụng Kakeibo"* | **13,6** |
| 20% | C2 tr. 18–25 — cả **ba** công thức phân bổ | 20,9 |
| 10% | C2 tr. 18 — chỉ riêng lọ FFA | 29,9 |

*(số năm tính bằng công thức của [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách))*

Con số 35% **cao hơn mọi tỷ lệ mà chính cuốn sách khuyên** ở Class 2, và cao hơn tới mức rút lộ
trình từ 21 năm xuống 14 năm. Nếu một quyển sổ và một cây bút làm được điều đó thì Class 2 đã không
cần ba chương về phân bổ thu nhập.

Cách đọc đúng con số này: coi nó là **quảng cáo cho phương pháp**, không phải một phát hiện. Phần
đáng tin của Kakeibo là cơ chế chú tâm ở tr. 10, không phải con số 35% ở tr. 8.

### "Khoa học đã chứng minh"

> *"Khoa học đã chứng minh rằng việc ghi chép bằng tay sẽ tốt hơn việc sử dụng các thiết bị công
> nghệ."* — C1 tr. 9

Cũng không có nguồn. Và có một khoảng cách mà câu này bước qua rất nhanh: các nghiên cứu thường
được viện dẫn cho ý "viết tay hơn gõ máy" là về **ghi chép bài giảng và ghi nhớ khái niệm** — tức
là học, không phải theo dõi chi tiêu. Hai việc khác nhau; kết luận của việc này không tự động thành
kết luận của việc kia.

Điều đáng nói: **sách không cần câu đó.** Lập luận ở tr. 10 (viết tay buộc bạn dừng lại ở từng
khoản) tự nó đã đủ, và nó là lập luận về **cơ chế** chứ không phải viện dẫn quyền uy. Câu *"khoa học
đã chứng minh"* chỉ làm chỗ mạnh nhất của lesson trở nên dễ bác bỏ hơn.

Cả hai chỗ này giống hệt lỗi phương pháp ở [bài 1 mục 1](bai_01_tai_chinh_ca_nhan_la_gi.md#1-định-nghĩa-của-sách-và-một-chỗ-không-kiểm-chứng-được)
— trích Wikipedia không ghi phiên bản. Câu hỏi vẫn là câu hỏi ấy: **tra ngược về đâu?**

---

## 6. [bổ sung] Vì sao 3–6 tháng, và vì sao 3–6 tháng vẫn chưa đủ

Sách ra chỉ dẫn *"3-6 tháng"* (C1 tr. 7) mà không giải thích. Đây là câu trả lời bằng số.

Lấy một năm chi tiêu, chia theo **đúng bốn nhóm của Kakeibo**. Không có ngẫu nhiên — mười hai tháng
là một bảng cố định trong code, thu nhập 16 triệu/tháng:

```
  tháng  thiết yếu  sở thích  bồi dưỡng  bất thường     TỔNG   dôi ra
  ─────────────────────────────────────────────────────────────────────
     1      10,0tr     3,5tr      0,5tr      15,0tr    29,0tr  −13,0tr   Tết
     2       8,0tr     2,0tr      1,0tr       0,0tr    11,0tr    5,0tr
     3       8,2tr     1,8tr      0,8tr       0,0tr    10,8tr    5,2tr
     4       8,0tr     2,2tr      1,2tr       0,0tr    11,4tr    4,6tr
     5       8,1tr     2,0tr      0,5tr       3,0tr    13,6tr    2,4tr   cưới bạn
     6       8,5tr     2,5tr      1,0tr       0,0tr    12,0tr    4,0tr
     7       8,3tr     1,9tr      0,6tr       0,0tr    10,8tr    5,2tr
     8       8,0tr     2,1tr      0,9tr       4,0tr    15,0tr    1,0tr   sửa xe máy
     9       8,2tr     2,0tr      1,5tr       0,0tr    11,7tr    4,3tr
    10       8,4tr     2,3tr      0,7tr       0,0tr    11,4tr    4,6tr
    11       8,1tr     2,0tr      1,0tr       2,0tr    13,1tr    2,9tr   đầy tháng con bạn
    12       8,6tr     3,0tr      0,8tr       0,0tr    12,4tr    3,6tr

  Chi tiêu trung bình THẬT: 13,5tr/tháng
  Nhóm "bất thường": 14,8% tổng chi cả năm, nhưng chỉ xuất hiện ở 4/12 tháng
```

Người học không chọn được tháng bắt đầu ghi — họ bắt đầu khi đọc xong cuốn sách. Nên với mỗi độ dài
ghi chép, xét **cả mười hai điểm xuất phát** và lấy trường hợp xấu nhất:

| Ghi bao lâu | Ước lượng thấp nhất | Cao nhất | Khoảng sai | Rộng |
| ---: | ---: | ---: | :---: | ---: |
| **1 tháng** | 10,8tr | 29,0tr | −20,1% … **+114,5%** | 134,6% |
| 2 tháng | 10,9tr | 20,7tr | −19,4% … +53,1% | 72,5% |
| **3 tháng** | 11,1tr | 18,2tr | −18,1% … +34,4% | 52,5% |
| **6 tháng** | 11,6tr | 15,4tr | −14,2% … +14,2% | 28,4% |
| 9 tháng | 12,0tr | 14,3tr | −11,5% … +6,0% | 17,5% |
| 12 tháng | 13,5tr | 13,5tr | 0% | 0% |

Ghi **một tháng** thì tuỳ bạn xui hay may: rơi vào tháng 7 thì tưởng mình tiêu 10,8 triệu, rơi vào
tháng Tết thì tưởng mình tiêu 29 triệu. Sai số **hơn gấp đôi** theo chiều lên.

Còn đây là chỗ phải nói thật, và nó không tâng bốc cuốn sách: **sáu tháng đưa sai số xuống 14%,
không xuống 0.**

```
   muốn chắc chắn sai dưới    thì phải ghi
   ───────────────────────    ────────────
            30%                  4 tháng
            20%                  5 tháng
            15%                  5 tháng
            10%                 12 tháng
             5%                 12 tháng
```

Vậy *"3-6 tháng"* đưa bạn tới khoảng **±14–18%** — đủ để thấy **hình dạng** bức tranh, chưa đủ để
có con số dùng cho một kế hoạch chặt.

### Thủ phạm là nhóm thứ tư

Bỏ nhóm *"chi bất thường"* ra và tính lại trên ba nhóm đều đặn:

| Ghi bao lâu | Ba nhóm đều đặn | Cả bốn nhóm | Nhóm thứ tư nới rộng |
| ---: | ---: | ---: | ---: |
| 1 tháng | 29,5% | 134,6% | **gấp 4,6 lần** |
| 3 tháng | 13,6% | 52,5% | gấp 3,9 lần |
| 6 tháng | **7,2%** | **28,4%** | gấp 3,9 lần |

Ba nhóm đầu ổn định tới mức **sáu tháng đã đưa sai số xuống 4%** — quá đủ dùng. Thêm nhóm thứ tư
vào, vẫn sáu tháng đó, sai số vọt lên **14%**.

Nên chỉ dẫn "3-6 tháng" của sách không phải để đo tiền ăn hay tiền điện. Nó là để **bắt được vài
lần chi bất thường**. Và ngay cả thế cũng không đủ, vì Tết mỗi năm chỉ đến một lần — sáu tháng ghi
chép có thể không chứa cái tháng tốn nhất của cả năm.

### Cách vá, suy thẳng từ mấy con số trên

> **Ba nhóm đầu:** lấy trung bình từ sổ ghi chép 3–6 tháng. Ổn định, ngắn thế là đủ.
>
> **Nhóm thứ tư:** **đừng** lấy trung bình từ sổ. Hãy ngồi liệt kê theo **năm** — Tết, cưới hỏi,
> giỗ chạp, đầy tháng, bảo dưỡng xe, khám sức khoẻ, học phí — rồi chia cho 12.

Đây là hai phép đo khác nhau cho hai loại chi khác nhau, và nó giải thích luôn vì sao Kakeibo phải
tách nhóm thứ tư ra thay vì gộp vào ba nhóm kia. Hani Motoko không có công cụ thống kê nào; bà chỉ
quan sát thấy loại chi ấy hành xử khác.

Cũng chú ý: nhóm thứ tư là nhóm **không có lọ nào tương ứng** ở hệ 6 jars (mục 3). Bài 7 và bài 9
xử lý khoảng trống đó bằng hai công cụ khác nhau — quỹ chi tiêu và quỹ khẩn cấp.

---

## 7. [bổ sung] Câu hỏi số 2 của Kakeibo đã là "trả cho mình trước" — từ năm 1904

Đọc lại câu hỏi 2, chú ý chữ cuối:

> *"**2. Bạn muốn tiết kiệm bao nhiêu tiền?** Ghi chép lại số tiền muốn tiết kiệm vào trang tiếp
> theo và **cất riêng khoản này trước**. Cố gắng chi tiêu làm sao để không phải sử dụng đến khoản
> tiết kiệm."* — C1 tr. 9

Bây giờ mở Class 2, trang 15, nơi sách giới thiệu một nguyên tắc như thể lần đầu:

> *"thay vì trả cho người khác, chúng ta ưu tiên thanh toán cho bản thân trước tiên… hãy ưu tiên
> trả cho bản thân theo quy tắc **'Pay yourself first'**. Quy trình mới sẽ là: Kiếm tiền − Pay your
> self first − Chi tiêu − Bảo vệ − Đầu tư."* — C2 tr. 15

**Hai chỗ nói cùng một điều.** Kakeibo hỏi "tiết kiệm bao nhiêu" (câu 2) **trước khi** hỏi "tiêu bao
nhiêu" (câu 3) — thứ tự đó *là* pay-yourself-first. Sách đã dạy nguyên tắc ấy ở Class 1 mà không
đặt tên, rồi đặt tên cho nó ở Class 2 như một ý mới.

Đây là ví dụ rõ nhất cho lý do khoá học **gộp lại theo chủ đề** thay vì đi theo thứ tự sách
([bài 0 mục 4](bai_00_bat_dau_tu_dau.md#4-vì-sao-khoá-học-không-đi-theo-thứ-tự-sách)).

### Thứ tự ấy đổi được gì — đo trên đúng một năm ở mục 6

**Cách A — để dành phần còn lại** (cách sách mô tả ở C2 tr. 14: *"Cuối tháng phần lớn khả năng là
không có dư tiền"*):

```
   gom được trong 11 tháng dương      42,8tr
   tháng Tết ăn ngược lại            −13,0tr
   ────────────────────────────────────────
   còn lại RÒNG cả năm                29,8tr

   tháng để ra nhiều nhất  5,2tr  ·  ít nhất  −13,0tr
   số tháng trắng tay: 1  (tháng Tết)
```

**Cách B — cất riêng 10% ngay khi nhận lương** (Kakeibo câu 2):

```
   cất 1,6tr/tháng  =>  19,2tr/năm, đều tăm tắp
   số tháng phải cắt chi tiêu mới đủ cất: 2
      tháng  1: thiếu 14,6tr
      tháng  8: thiếu  0,6tr
```

Đọc kỹ hai khối này thì thấy điều bất ngờ: **cách A để ra được nhiều tiền hơn** — 29,8 triệu so với
19,2 triệu. Nếu chỉ nhìn tổng cuối năm, cách A thắng.

Nhưng số dư lên xuống từ **+5,2 triệu** xuống **−13 triệu** thì rất khó biết mình đang tích luỹ hay
đang giậm chân — đúng cái *"chập chờn"* mà C1 tr. 8 tả. Còn cách B cho một con số đều tăm tắp, đổi
lại **buộc phải cắt chi tiêu ở hai tháng**.

Và chính việc buộc phải cắt đó mới là thứ có giá trị. Cách A không bao giờ đặt ra câu hỏi *"cắt cái
gì"*; nó chỉ ghi nhận kết quả. Cách B ép câu hỏi ấy xuất hiện đúng hai lần trong năm, vào đúng
tháng cần hỏi. **Bài 7** làm kỹ phần này.

---

## 8. Bốn mẹo cải thiện, và tên thật của chúng

Câu hỏi 4 của Kakeibo là *"Bạn sẽ làm gì để cải thiện?"*, và sách kèm bốn mẹo:

| Sách viết (C1 tr. 10) | Đây thật ra là gì |
| --- | --- |
| *"Đừng vội quyết định mua sắm ngay mà hãy suy nghĩ, cân nhắc về món đồ đó trong vòng **72 giờ**"* | **quãng nguội** — tách quyết định ra khỏi lúc đang bị kích thích |
| *"Đừng bị thu hút bởi những 'dịp đại hạ giá', 'săn sale'. Bạn sẽ mua rất nhiều thứ không cần thiết chỉ vì chúng quá rẻ"* | **neo giá** — giá gạch bỏ làm cái neo, khiến bạn so với nó thay vì so với nhu cầu |
| *"Thường xuyên nhìn vào số dư trong ví hoặc tài khoản ngân hàng"* | **làm cho nổi bật** — cái không nhìn thấy thì không tính vào quyết định |
| *"Dùng tiền mặt để dễ kiểm soát chi tiêu hơn"* | **nỗi đau khi trả** — đếm tiền ra khỏi ví đau hơn quẹt thẻ |

Bốn mẹo này **khác loại** với mọi thứ khác trong bài. Ba mục trước là đo lường; bốn mẹo này là
**can thiệp vào hành vi**. Sách đưa chúng vào như "vài mẹo nhỏ" mà không nhận ra chúng thuộc một
họ công cụ riêng.

Cả bốn đều xoay quanh cùng một ý: **quyết định chi tiêu không được đưa ra bởi một người tính toán
tỉnh táo.** Nó được đưa ra bởi một người đang đứng trong cửa hàng, đang mệt, đang thấy chữ "giảm
50%". Bốn mẹo trên không dạy bạn tính giỏi hơn — chúng thay đổi **hoàn cảnh** lúc bạn quyết định.

**Bài 10** gom bốn mẹo này với ba mảnh khác mà sách rải ở Class 2 (thiên kiến sống sót ở C2 tr. 10,
lạm phát lối sống ở C2 tr. 17, *"Sự tham lam"* ở C2 tr. 52) thành một khung hoàn chỉnh.

### [2026] Mẹo thứ tư đã cũ đi

*"Dùng tiền mặt để dễ kiểm soát chi tiêu hơn"* viết vào khoảng 2022–2023. Ở Việt Nam năm 2026, quét
mã và chuyển khoản đã thành mặc định ở phần lớn hàng quán, và nhiều chỗ không nhận tiền mặt nữa.

Cơ chế phía sau mẹo này thì **không cũ** — trả bằng cách nào cũng được, miễn hành động trả phải có
một chút ma sát và phải để lại dấu vết bạn nhìn thấy. Cách thay tương đương: đặt hạn mức tuần cho
một ví riêng, hoặc tắt lưu thẻ trên các ứng dụng mua sắm để mỗi lần mua phải nhập lại. Ba mẹo đầu
thì không phụ thuộc phương tiện thanh toán nào cả.

---

## 9. Tự thử

1. **Chọn công cụ.** Đọc lại bảng ở mục 4. Bạn định dùng sổ, app, hay cả hai? Viết ra **một câu**
   lý do — và một tháng sau đọc lại xem lý do đó có còn đúng không.

2. **Đo nhóm thứ tư của chính bạn.** Đừng ghi chép gì cả, chỉ ngồi liệt kê mọi khoản **bất thường**
   trong 12 tháng qua: Tết, cưới hỏi, giỗ, đầy tháng, sửa xe, khám bệnh, học phí. Cộng lại chia 12.
   Con số đó chiếm bao nhiêu phần trăm chi tiêu tháng của bạn? So với **14,8%** ở mục 6.

3. **Đổi bảng chi tiêu trong code.** Trong `bai-03-ghi-chep-bao-lau.py`, thay `NAM` bằng số của
   chính bạn (ước lượng cũng được). Sai số khi ghi 3 tháng và 6 tháng thay đổi thế nào? Nhóm thứ
   tư của bạn nới rộng sai số gấp mấy lần?

4. **Bỏ tháng Tết đi.** Vẫn trong code, đổi khoản bất thường tháng 1 từ `15_000` xuống `0`. Bảng
   "muốn chắc chắn sai dưới ngưỡng" đổi thế nào? Điều đó nói gì về việc **thời điểm bắt đầu ghi
   chép** quan trọng đến đâu?

5. **Cách A hay cách B?** Mục 7 cho thấy cách A để ra nhiều tiền hơn cách B trong đúng năm này.
   Viết ra **hai lý do** vẫn nên chọn cách B, và **một hoàn cảnh** mà cách A thật sự tốt hơn.

6. **Kiểm con số 35%.** Nếu Kakeibo thật sự nâng tỷ lệ tiết kiệm lên 35%, thì với bảng chi tiêu ở
   mục 6 (thu nhập 16 triệu/tháng), mỗi tháng phải để ra bao nhiêu? Con số đó có nằm trong khoảng
   *"dôi ra"* của cột cuối không? Còn thiếu bao nhiêu, và cắt từ nhóm nào?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh / gốc | Nghĩa ngắn |
| --- | --- | --- |
| Kakeibo | 家計簿 | *"sổ ghi chép chi tiêu tài chính"*; Hani Motoko, 1904 — C1 tr. 8 |
| Bốn nhóm chi tiêu | — | thiết yếu · sở thích · bồi dưỡng tâm hồn · **bất thường** — C1 tr. 9 |
| Chi bất thường | irregular expense | cưới hỏi, sửa xe, Tết — chiếm phần lớn sai số của mọi ước lượng ngắn hạn |
| Trả cho mình trước | pay yourself first | cất tiết kiệm **trước** khi tiêu; Kakeibo câu 2, C1 tr. 9 · C2 tr. 15 |
| Chập chờn | — | dao động tháng có tháng không; C1 tr. 8, và C1 tr. 12 xếp nó ngang dòng tiền âm |
| **[bổ sung]** Quãng nguội | cooling-off period | quy tắc 72 giờ — tách quyết định khỏi lúc bị kích thích |
| **[bổ sung]** Neo giá | anchoring | giá gạch bỏ làm điểm so sánh; *"săn sale"* |
| **[bổ sung]** Làm cho nổi bật | salience | nhìn số dư thường xuyên |
| **[bổ sung]** Nỗi đau khi trả | pain of paying | tiền mặt đau hơn quẹt thẻ |
| **[bổ sung]** So sánh xã hội hướng lên | upward social comparison | *"nhìn lên những người hơn mình"* — C1 tr. 8 |

---

## 11. Câu hỏi tự kiểm tra

1. Sách nói ghi chép đem lại **cái gì**? Nó có nói ghi chép làm bạn tiêu ít đi không? (mục 1)
2. Vì sao bài 3 phải đứng trước bài 2 về mặt dữ liệu, dù bài 2 đứng trước về mặt số thứ tự? (mục 1)
3. Lời phản đối mà sách tự viết ra là gì, và sách trả lời bằng lập luận đạo đức hay thực nghiệm? (mục 2)
4. Chữ *"chập chờn"* ở C1 tr. 8 nối với câu nào ở C1 tr. 12? Hai chỗ đó nói cùng điều gì? (mục 2)
5. Kể bốn câu hỏi của Kakeibo **theo đúng thứ tự**. Vì sao thứ tự quan trọng? (mục 3, 7)
6. Kể bốn nhóm chi tiêu. Nhóm nào **không có** lọ tương ứng trong hệ 6 jars? (mục 3)
7. Bốn nhóm Kakeibo khác sáu chiếc lọ ở chỗ nào — làm trước hay làm sau khi tiêu? (mục 3)
8. Sách khuyên dùng app ở trang nào và khuyên **không** dùng app ở trang nào? (mục 4)
9. Tiêu chí nào trong chính cuốn sách giúp gỡ mâu thuẫn đó? App mạnh ở việc gì, yếu ở việc gì? (mục 4)
10. Con số 35% được dẫn nguồn bằng mấy chữ? Nó **cao hơn hay thấp hơn** mọi tỷ lệ mà chính sách
    khuyên ở Class 2? (mục 5)
11. Ghi chép **một tháng** thì ước lượng chi tiêu có thể sai tối đa bao nhiêu phần trăm? (mục 6)
12. Ghi **sáu tháng** thì còn sai bao nhiêu? Vậy chỉ dẫn "3-6 tháng" đủ để làm gì và **không** đủ
    để làm gì? (mục 6)
13. Nhóm thứ tư nới rộng biên độ sai gấp mấy lần? Cách vá là gì? (mục 6)
14. Kakeibo câu 2 (1904) và *"Pay yourself first"* (C2 tr. 15) khác nhau ở chỗ nào? (mục 7)
15. Trong năm ở mục 6, cách A để ra được **nhiều hay ít** tiền hơn cách B? Vậy vì sao vẫn nên
    chọn cách B? (mục 7)
16. Kể bốn mẹo của câu hỏi 4 và tên cơ chế của từng mẹo. Chúng khác loại với phần còn lại của
    bài ở chỗ nào? (mục 8)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 3 — GHI CHÉP CHI TIÊU VÀ KAKEIBO                    C1 tr. 7-10     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  GHI CHÉP LÀ ĐỂ CHÚ TÂM, không phải để tiêu ít đi        (C1 tr.7, 10)  ║
║     bài 3 (dữ liệu)  ->  bài 2 (đo)  ->  bài 7 (quyết định)             ║
║                                                                          ║
║  KAKEIBO   家計簿 · Hani Motoko · 1904 · bốn câu hỏi                     ║
║     1 có bao nhiêu → 2 TIẾT KIỆM bao nhiêu → 3 tiêu bao nhiêu → 4 cải   ║
║     bốn nhóm chi: thiết yếu · sở thích · bồi dưỡng · BẤT THƯỜNG          ║
║     nhóm bất thường KHÔNG có lọ tương ứng ở 6 jars                       ║
║                                                                          ║
║  SÁCH TỰ MÂU THUẪN   tr.7 "nên dùng các app"                            ║
║                      tr.8 "không sử dụng các app"                        ║
║     gỡ bằng tiêu chí của chính sách (tr.10): thứ cần đạt là CHÚ TÂM      ║
║     app mạnh về ĐẦY ĐỦ, yếu về chú tâm — vì nó tự động                  ║
║                                                                          ║
║  HAI KHẲNG ĐỊNH KHÔNG NGUỒN                                             ║
║     "tiết kiệm 35% khi áp dụng Kakeibo"  (tr.8, "theo thống kê")        ║
║        35% CAO HƠN mọi tỷ lệ sách tự khuyên ở Class 2 (20%)             ║
║        nếu đúng: 14 năm thay vì 21 năm                                   ║
║     "khoa học đã chứng minh viết tay tốt hơn"  (tr.9)                   ║
║        nghiên cứu hay được dẫn là về GHI BÀI GIẢNG, không phải chi tiêu  ║
║                                                                          ║
║  VÌ SAO 3-6 THÁNG   ghi 1 tháng: sai −20% … +114%   (biên độ 135%)      ║
║                     ghi 3 tháng: −18% … +34%                             ║
║                     ghi 6 tháng: −14% … +14%   <- KHÔNG phải 0           ║
║     muốn sai dưới 10% thì phải ghi đủ 12 tháng                           ║
║     => 3-6 tháng đủ thấy HÌNH DẠNG, chưa đủ có con số chặt               ║
║                                                                          ║
║  THỦ PHẠM LÀ NHÓM THỨ TƯ   14,8% tổng chi, chỉ hiện ở 4/12 tháng        ║
║     ba nhóm đều đặn, ghi 6 tháng: sai  4%                                ║
║     thêm nhóm bất thường:          sai 14%   — gấp ~4 lần ở mọi độ dài  ║
║     VÁ: ba nhóm đầu lấy trung bình từ sổ 3-6 tháng                       ║
║         nhóm thứ tư ĐỪNG lấy trung bình — liệt kê theo NĂM, chia 12      ║
║                                                                          ║
║  CÂU 2 CỦA KAKEIBO ĐÃ LÀ "PAY YOURSELF FIRST" — TỪ 1904                 ║
║     C2 tr.15 đặt tên cho nó như một ý mới ở tập hai                      ║
║     cách A (để dành phần còn lại) ra 29,8tr — NHIỀU HƠN cách B 19,2tr   ║
║     nhưng A dao động +5,2tr … −13,0tr, 1 tháng trắng tay                 ║
║     B đều tăm tắp, ép câu hỏi "cắt cái gì" xuất hiện đúng 2 lần/năm      ║
║                                                                          ║
║  BỐN MẸO = BỐN CAN THIỆP HÀNH VI   72 giờ · săn sale · nhìn số dư ·     ║
║     tiền mặt  ->  quãng nguội · neo giá · nổi bật · nỗi đau khi trả     ║
║     không dạy bạn tính giỏi hơn — đổi HOÀN CẢNH lúc bạn quyết định       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1***, Waka.vn.
  - **Unit 2 Lesson 1 *Công việc đầu tiên* (tr. 7–8)** — nguồn chính: ghi chép để *"hướng sự chú tâm
    vào tiền bạc"*, gợi ý app Money Lover / Fast Budget, chỉ dẫn *"3-6 tháng"*, lời phản đối tự viết
    ra và câu trả lời *"Chỉ là, có một cách tốt hơn"* (tr. 7); *"chập chờn tháng có tháng không"*,
    *"nhìn lên những người hơn mình"*, *"đổi chút ít sự thoải mái hôm nay lấy sự dư dả ngày mai"*,
    *"không đồng nghĩa với việc bạn phải 'thắt lưng buộc bụng'"* (tr. 8)
  - **Unit 2 Lesson 2 *Phương pháp Kakeibo* (tr. 8–10)** — nguồn chính: 家計簿, Hani Motoko 1904,
    con số 35% *"theo thống kê"*, *"chỉ cần một quyển sổ và một cây bút… không sử dụng các app"*
    (tr. 8); *"Khoa học đã chứng minh…"*, bốn câu hỏi, bốn nhóm chi tiêu (tr. 9); bốn mẹo cải thiện
    và *"lợi ích lớn nhất của Kakeibo là yêu cầu bạn phải chú tâm"* (tr. 10)
  - Unit 2 Lesson 3 (tr. 12) — *"lúc âm, lúc dương không ổn định"*; bài 2
- ***Tài chính cá nhân 101 — Class 2***, Waka.vn.
  - Unit 2 mở đầu (tr. 14–15) — *"Cuối tháng phần lớn khả năng là không có dư tiền"*; quy tắc
    *"Pay yourself first"* và quy trình năm bước
  - Unit 2 Lesson 2 (tr. 18–22) và Lesson 3–4 (tr. 23–25) — sáu chiếc lọ và hai hệ còn lại; bài 7
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-03-ghi-chep-bao-lau.py`](../thuc_hanh/bai-03-ghi-chep-bao-lau.py).
  Mọi bảng số ở mục 6 và mục 7 do tệp này tính. Không dùng ngẫu nhiên: mười hai tháng chi tiêu là
  một bảng cố định gõ thẳng trong code, chạy hai lần ra giống hệt nhau.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - **Bảng mười hai tháng chi tiêu ở [mục 6](#6-bổ-sung-vì-sao-36-tháng-và-vì-sao-36-tháng-vẫn-chưa-đủ)
    là số liệu do khoá học dựng**, không phải của sách và không phải khảo sát. Nó chỉ dùng để cho
    thấy **cơ chế**; con số cụ thể sẽ khác với từng người.
  - Toàn bộ phân tích sai số theo độ dài ghi chép, bảng "nhóm thứ tư nới rộng gấp mấy lần", và
    cách vá (liệt kê nhóm bất thường theo năm) **không có trong sách**. Sách chỉ đưa chỉ dẫn
    *"3-6 tháng"* mà không giải thích.
  - So sánh cách A và cách B ở [mục 7](#7-bổ-sung-câu-hỏi-số-2-của-kakeibo-đã-là-trả-cho-mình-trước--từ-năm-1904)
    là của khoá học. Việc **Kakeibo câu 2 chính là pay-yourself-first** cũng là quan sát của khoá
    học; sách không nối hai chỗ này.
  - Tên bốn cơ chế hành vi ở [mục 8](#8-bốn-mẹo-cải-thiện-và-tên-thật-của-chúng) **không có trong
    sách** — sách chỉ gọi chúng là *"vài mẹo nhỏ"*.
  - Nhận xét về câu *"khoa học đã chứng minh"* ở [mục 5](#5-đính-chính-hai-khẳng-định-không-nguồn)
    **không bác bỏ** ý viết tay có ích. Nó chỉ nêu rằng sách không dẫn nguồn, và các nghiên cứu
    thường được viện dẫn cho ý này là về ghi chép bài giảng chứ không phải theo dõi chi tiêu.
- **Liên hệ chéo:**
  - Công thức số năm dùng ở [mục 5](#5-đính-chính-hai-khẳng-định-không-nguồn):
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Dòng tiền chập chờn bị xếp ngang dòng tiền âm:
    [bài 2 mục 2](bai_02_do_hien_trang.md#2-dòng-tiền--bước-1-của-sách).
  - Lãi kép và giá trị theo thời gian:
    [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| **3** | **Ghi chép chi tiêu và phương pháp Kakeibo** ← *bạn đang ở đây* | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| 5 | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md) | C2 tr. 4–13 | 1 |
| 6 | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách | 1 |
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
