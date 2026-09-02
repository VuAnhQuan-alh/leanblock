# Bài 9 — Độc quyền nhóm và lý thuyết trò chơi

> Bài học dựng từ **Chương 17 — Độc quyền nhóm** (tr. 391–420)
> của *N. Gregory Mankiw — **Kinh tế học vi mô***, bản dịch của Khoa Kinh tế, **ĐH Kinh tế TP.HCM** (Cengage Learning Asia).
> 🎯 **Vòng 1.** Ba bài trước, doanh nghiệp nhìn đường cầu rồi tự quyết một mình.
> Bài này là bài đầu tiên trong đó **đối thủ nhìn lại bạn**: quyết định của bạn thay đổi
> lợi nhuận của họ, và họ biết điều đó. Đây cũng là chương duy nhất của sách dạy
> **lý thuyết trò chơi** — bộ công cụ dùng được xa ngoài phạm vi kinh tế học.
> 💼 **Góc QTKD** — ví dụ thêm cho ngành quản trị kinh doanh, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc chỉ nêu kết quả mà không chứng minh.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 6](bai_06_thi_truong_canh_tranh.md) và [Bài 7](bai_07_doc_quyen_va_phan_biet_gia.md)
> — bài này đặt độc quyền nhóm **vào giữa** hai bài đó và đo xem nó nằm ở đâu.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Độc quyền nhóm là gì và vì sao nó khó hơn hai chương trước](#1-độc-quyền-nhóm-là-gì-và-vì-sao-nó-khó-hơn-hai-chương-trước)
- [2. Thị trường nhị quyền của Jack và Jill](#2-thị-trường-nhị-quyền-của-jack-và-jill)
- [3. Ba kết cục của cùng một thị trường](#3-ba-kết-cục-của-cùng-một-thị-trường)
- [4. Cân bằng Nash và vì sao cartel không giữ được](#4-cân-bằng-nash-và-vì-sao-cartel-không-giữ-được)
- [5. Số người bán tăng — hiệu ứng lượng đấu hiệu ứng giá](#5-số-người-bán-tăng--hiệu-ứng-lượng-đấu-hiệu-ứng-giá)
- [6. 📚 Nghiệm Cournot — chứng minh công thức tổng quát](#6--nghiệm-cournot--chứng-minh-công-thức-tổng-quát)
- [7. Tình thế tiến thoái lưỡng nan của người tù và chiến lược thống soái](#7-tình-thế-tiến-thoái-lưỡng-nan-của-người-tù-và-chiến-lược-thống-soái)
- [8. Bốn hoàn cảnh, một cấu trúc](#8-bốn-hoàn-cảnh-một-cấu-trúc)
- [9. Nghiên cứu tình huống — OPEC](#9-nghiên-cứu-tình-huống--opec)
- [10. Tiến thoái lưỡng nan có phải lúc nào cũng xấu không](#10-tiến-thoái-lưỡng-nan-có-phải-lúc-nào-cũng-xấu-không)
- [11. Trò chơi lặp — vì sao đôi khi người ta vẫn hợp tác](#11-trò-chơi-lặp--vì-sao-đôi-khi-người-ta-vẫn-hợp-tác)
- [12. 📚 Hệ số chiết khấu — hợp tác bền khi nào](#12--hệ-số-chiết-khấu--hợp-tác-bền-khi-nào)
- [13. Giải đấu Axelrod và ăn miếng trả miếng](#13-giải-đấu-axelrod-và-ăn-miếng-trả-miếng)
- [14. Một lần lỡ tay — chỗ sách chỉ nói bằng lời](#14-một-lần-lỡ-tay--chỗ-sách-chỉ-nói-bằng-lời)
- [15. Chính sách chống độc quyền](#15-chính-sách-chống-độc-quyền)
- [16. Ba hành vi gây tranh cãi](#16-ba-hành-vi-gây-tranh-cãi)
- [17. 💼 Cuộc chiến giảm giá — kiểm tra chứ không giả định](#17--cuộc-chiến-giảm-giá--kiểm-tra-chứ-không-giả-định)
- [18. Code minh hoạ](#18-code-minh-hoạ)
- [19. Tự thử](#19-tự-thử)
- [20. Từ điển thuật ngữ](#20-từ-điển-thuật-ngữ)
- [21. Câu hỏi tự kiểm tra](#21-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Độc quyền nhóm là gì và vì sao nó khó hơn hai chương trước

Sách mở chương bằng quả bóng tennis (tr. 391):

> *"Nếu bạn tới một cửa hàng bóng tennis, những quả bóng mà bạn mua rất có thể sẽ thuộc một trong
> những nhãn hiệu sau: Wilson, Penn, Dunlop hoặc là Spalding. Bốn công ty này sản xuất gần như
> toàn bộ số lượng bóng tennis trên thị trường Hoa Kỳ."*

Định nghĩa in ở chân trang 391:

> **Độc quyền nhóm** *(oligopoly)*: một cấu trúc thị trường mà trong đó chỉ có một số ít người bán,
> bán các sản phẩm tương tự hoặc gần như tương tự nhau.

Điểm mấu chốt nằm ở câu tiếp theo, và nó là **lý do chương này cần một bộ công cụ mới**:

> *"hành động của bất cứ người bán nào trên thị trường này cũng có thể có tác động lớn lên lợi nhuận
> của tất cả những người bán hàng còn lại."*

So sánh với ba bài trước để thấy chỗ đứt gãy:

| Cấu trúc                                                       | Doanh nghiệp phải nghĩ về ai?                     | Công cụ đủ dùng            |
| -------------------------------------------------------------- | ------------------------------------------------- | -------------------------- |
| Cạnh tranh hoàn hảo ([bài 6](bai_06_thi_truong_canh_tranh.md)) | không ai cả — giá là dữ kiện                      | `P = MC`                   |
| Độc quyền ([bài 7](bai_07_doc_quyen_va_phan_biet_gia.md))      | chỉ khách hàng                                    | `MR = MC`                  |
| Cạnh tranh độc quyền ([bài 8](bai_08_canh_tranh_doc_quyen.md)) | khách hàng, còn đối thủ thì quá đông để đếm       | `MR = MC` + tự do gia nhập |
| **Độc quyền nhóm**                                             | **từng đối thủ một, và họ cũng đang nghĩ về bạn** | **lý thuyết trò chơi**     |

Sách nói thẳng ra rằng chính vì thế mà nó phải giới thiệu một ngành học khác (tr. 391):

> **Lý thuyết trò chơi** *(game theory)*: là nghiên cứu về việc con người sẽ hành xử như thế nào
> trong các tình huống chiến lược.
>
> *"Chiến lược ở đây có nghĩa là một tình huống trong đó một người khi lựa chọn các phương án hành
> động khác nhau, phải cân nhắc xem những người khác sẽ phản ứng như thế nào trước hành động mà anh
> ta chọn."*

Và đặc điểm chính của toàn chương, gói trong một câu ở tr. 391:

> *"một đặc điểm chính của thị trường độc quyền nhóm là **sự đối nghịch giữa việc hợp tác và lợi ích
> cá nhân**."*

Cả chương chỉ là câu đó, được đo bằng số.

---

## 2. Thị trường nhị quyền của Jack và Jill

Để giữ mọi thứ đếm được, sách hạ độc quyền nhóm xuống trường hợp nhỏ nhất — **hai người bán**, gọi là
**thị trường nhị quyền** *(duopoly)*, và cho họ một công việc không tốn gì cả (tr. 392):

> *"Giả sử trong một thị trấn chỉ có hai cư dân là Jack và Jill sở hữu các giếng nước sạch có thể
> dùng cho sinh hoạt… hãy giả sử rằng Jack và Jill có thể bơm bao nhiêu nước tùy thích mà không tốn
> một đồng chi phí nào. Điều đó có nghĩa là **chi phí biên của nước bằng 0**."*

Chi phí biên bằng 0 là một mẹo sư phạm rất gọn: nó làm **tổng doanh thu chính là tổng lợi nhuận**,
nên mọi phép tính về sau chỉ còn một phép nhân.

**Bảng 1, tr. 392** — biểu cầu nước sinh hoạt:

```
 Sản lượng     Giá   Tổng doanh thu (và tổng lợi nhuận)
   0 gallon   $120                $0
        10     110             1.100
        20     100             2.000
        30      90             2.700
        40      80             3.200
        50      70             3.500
        60      60             3.600   <- đỉnh
        70      50             3.500
        80      40             3.200
        90      30             2.700
       100      20             2.000
       110      10             1.100
       120       0                 0
```

Sách chỉ in bảng. Nhưng nhìn hai cột đầu là thấy ngay công thức nằm sau lưng nó:

$$P = 120 - Q$$

Có công thức rồi thì không cần đọc bảng nữa — tính được **mọi** mức sản lượng, kể cả những mức sách
không in. Code ở [mục 18](#18-code-minh-hoạ) dựng lại cả 13 dòng và kiểm **13/13 khớp**.

⚠️ Đừng nhầm cột "tổng doanh thu" này với **doanh thu biên** ở [bài 7](bai_07_doc_quyen_va_phan_biet_gia.md).
Ở đây là *tổng*. Doanh thu biên là *chênh lệch giữa hai dòng liên tiếp*, và nó **âm** từ dòng 70 gallon
trở đi — đó chính là lý do đỉnh nằm ở 60.

---

## 3. Ba kết cục của cùng một thị trường

Cùng một biểu cầu, cùng một chi phí, ba cách tổ chức ngành, ba kết quả khác hẳn nhau (tr. 393–395):

| Kết cục                       |  Sản lượng |     Giá |   LN ngành |    Mỗi bên |
| ----------------------------- | ---------: | ------: | ---------: | ---------: |
| Cạnh tranh hoàn hảo           |    120 gal |      $0 |         $0 |          — |
| Độc quyền, hoặc **cartel**    |     60 gal |     $60 |     $3.600 |     $1.800 |
| **Nhị quyền — cân bằng Nash** | **80 gal** | **$40** | **$3.200** | **$1.600** |

**Cạnh tranh hoàn hảo** (tr. 393): giá bằng chi phí biên, mà chi phí biên bằng 0, nên **giá bằng 0**
và bán hết 120 gallon. Sách gọi đó là *"mức sản lượng hiệu quả"*.

**Cartel** (tr. 393): định nghĩa ở chân trang là

> **Sự cấu kết** *(collusion)*: thỏa thuận giữa các doanh nghiệp trong một thị trường về sản lượng và
> giá bán.
> **Cartel**: một nhóm các doanh nghiệp hoạt động vì mục tiêu chung.

> *"Khi một cartel được hình thành, thì thực chất thị trường chỉ được cung ứng bởi một doanh nghiệp
> độc quyền, và chúng ta có thể áp dụng những phân tích như trong Chương 15."*

Nghĩa là **cartel không phải một mô hình mới** — nó chỉ là [bài 7](bai_07_doc_quyen_va_phan_biet_gia.md)
mặc áo hai người.

**Nhị quyền** rơi vào **đúng giữa**. Đó là kết luận in nghiêng của sách ở tr. 395:

> *"khi mỗi doanh nghiệp trong thị trường độc quyền nhóm chọn mức sản lượng để tối đa hóa lợi nhuận,
> họ sẽ sản xuất ở một mức **lớn hơn** mức sản lượng của doanh nghiệp độc quyền, nhưng **thấp hơn**
> mức sản lượng của doanh nghiệp cạnh tranh. Giá của doanh nghiệp độc quyền nhóm **thấp hơn** giá độc
> quyền, nhưng **cao hơn** giá cạnh tranh (bằng chi phí biên)."*

Kiểm lại bằng con số: 60 < **80** < 120, và $0 < **$40** < $60. Đúng cả hai vế.

---

## 4. Cân bằng Nash và vì sao cartel không giữ được

Sách dẫn ra kết quả 40–40 bằng cách để Jack tự lẩm bẩm (tr. 394). Bốn con số trong hai đoạn lẩm bẩm đó
được code kiểm lại toàn bộ:

| Jack bơm | Jill bơm | Tổng |  Giá | LN Jack | Sách viết                                               |
| -------: | -------: | ---: | ---: | ------: | ------------------------------------------------------- |
|       30 |       30 |   60 |  $60 |  $1.800 | *"lợi nhuận của tôi sẽ là 1.800 đô la"*                 |
|       40 |       30 |   70 |  $50 |  $2.000 | *"lợi nhuận của tôi sẽ là 2.000 đô la"*                 |
|       40 |       40 |   80 |  $40 |  $1.600 | *"mỗi doanh nghiệp nhị quyền thu được lợi nhuận 1.600"* |
|       50 |       40 |   90 |  $30 |  $1.500 | *"lợi nhuận của tôi chỉ là 1.500 đô la"*                |

Hai dòng đầu **đẩy** Jack từ 30 lên 40. Dòng cuối **giữ chân** anh ta lại ở đó. Chỗ mà không ai còn
muốn nhúc nhích chính là định nghĩa (tr. 394):

> **Cân bằng Nash** *(Nash equilibrium)*: một tình huống mà ở đó các tác nhân kinh tế khi tương tác
> với những tác nhân khác, mỗi bên sẽ lựa chọn chiến lược tốt nhất **sau khi biết đối phương đã chọn
> những chiến lược của họ**.

Tên là của **John Nash**, và sách nhắc luôn rằng cuộc đời ông là nội dung phim *A Beautiful Mind*.

### 📚 Chứng minh thay vì tin

Sách dẫn tới (40, 40) bằng lời kể. Code làm ngược lại: **quét toàn bộ 13 × 13 tổ hợp** và hỏi ở mỗi
điểm rằng có ai muốn đổi ý không. Kết quả thật sự thú vị hơn câu chuyện:

- Có **4 điểm suy biến** ở góc (110–120, 110–120). Ở đó tổng sản lượng đã vượt 120 nên **giá bằng 0**,
  và ai bơm bao nhiêu cũng lãi 0 — mọi lựa chọn đều "tối ưu" một cách vô nghĩa. Loại chúng bằng điều
  kiện lợi nhuận > 0.
- Sau khi loại, vẫn còn **ba** điểm chứ không phải một: (30, 50), **(40, 40)**, (50, 30).

⚠️ Ba điểm này **không phải lỗi của sách** — chúng là hệ quả của việc sách đi từng bước 10 gallon.
Khi đối phương bơm 30 thì bơm 40 (được 40 × $50) và bơm 50 (được 50 × $40) **lãi y hệt nhau, $2.000**.
Thắt lưới nhỏ lại thì cụm co lại ngay:

| Bước lưới | Cân bằng Nash tìm được           |
| --------: | -------------------------------- |
|    10 gal | (30, 50), **(40, 40)**, (50, 30) |
|     5 gal | (35, 45), **(40, 40)**, (45, 35) |
|     2 gal | (38, 42), **(40, 40)**, (42, 38) |
|     1 gal | (39, 41), **(40, 40)**, (41, 39) |

Cụm luôn là $(40-h,\ 40+h)$, $(40, 40)$, $(40+h,\ 40-h)$ với $h$ đúng bằng bước lưới. Lưới càng mịn,
cụm càng siết về **(40, 40)** — cân bằng Nash thật sự của trò chơi liên tục.

Bài học phương pháp: **khi một cân bằng "biến mất" hoặc "nhân lên", hãy nghi ngờ độ mịn của lưới
trước khi nghi ngờ mô hình.**

### Vì sao cartel thua

Cartel cho mỗi bên $1.800, cân bằng Nash chỉ cho $1.600. Cả hai đều muốn cartel hơn. Nhưng cartel
**không phải cân bằng** — ở điểm (30, 30), Jack nhìn sang thấy bơm 40 được $2.000. Sách còn thêm hai
lý do thực tế nữa (tr. 394):

> *"Mâu thuẫn về việc phân chia lợi nhuận giữa các thành viên trong thị trường này khiến cho việc đạt
> được các thỏa thuận trở nên khó khăn hơn. Ngoài ra, **các bộ luật chống độc quyền cũng nghiêm cấm
> các thỏa thuận công khai** giữa các doanh nghiệp độc quyền nhóm."*

---

## 5. Số người bán tăng — hiệu ứng lượng đấu hiệu ứng giá

Sách đặt câu hỏi: nếu John và Joan cũng tìm ra giếng nước và nhảy vào (tr. 395)? Để trả lời, tr. 396
tách quyết định "có nên bơm thêm một gallon không" thành **hai lực ngược chiều**:

> - **Hiệu ứng lượng:** Bởi vì giá bán cao hơn chi phí biên, việc bán thêm một gallon nước ở mức giá
>   hiện hành sẽ làm **tăng** lợi nhuận.
> - **Hiệu ứng giá:** Việc tăng sản lượng sẽ làm tăng tổng lượng nước bán được, điều này sẽ làm **giảm**
>   giá bán và giảm lợi nhuận thu được trên những gallon nước khác.

Đây chính xác là **hai hiệu ứng của nhà độc quyền** ở [bài 7](bai_07_doc_quyen_va_phan_biet_gia.md),
chỉ khác một chỗ, và chỗ khác đó là toàn bộ chương:

> *"Số lượng người bán càng lớn thì mỗi người bán lại càng ít quan tâm tới tác động của họ lên giá thị
> trường… Khi thị trường độc quyền nhóm trở nên rất lớn, **hiệu ứng giá sẽ biến mất**."*

Và khi hiệu ứng giá biến mất thì chỉ còn hiệu ứng lượng — tức là **đúng logic của doanh nghiệp cạnh
tranh** ở bài 6. Sách chốt lại bằng câu in nghiêng ở tr. 396:

> *"khi số lượng người bán trên thị trường độc quyền nhóm càng nhiều, thị trường này sẽ càng giống một
> thị trường cạnh tranh. Giá sẽ tiến đến chi phí biên và sản lượng sẽ tiến đến mức sản lượng đạt hiệu
> quả xã hội."*

Đo bằng số (code mục 4):

| Số người bán | Mỗi bên bơm |          Tổng |             Giá | LN ngành |
| -----------: | ----------: | ------------: | --------------: | -------: |
|            1 |      60 gal |        60 gal |             $60 |   $3.600 |
|            2 |      40 gal |        80 gal |             $40 |   $3.200 |
|            3 |      30 gal |        90 gal |             $30 |   $2.700 |
|            4 |      24 gal |        96 gal |             $24 |   $2.304 |
|            5 |      20 gal |       100 gal |             $20 |   $2.000 |
|           10 |  120/11 gal |   1200/11 gal | $120/11 ≈ $10,9 |   $1.190 |
|          100 | 120/101 gal | 12000/101 gal |         ≈ $1,19 |     $141 |

Hình dạng của cột "Giá" quan trọng hơn từng con số: **người bán thứ hai làm giá sập một nửa; người
bán thứ 30 gần như không đổi gì nữa.**

> 💼 **Đọc bảng này theo kiểu quản trị.** Nếu bạn đang là người duy nhất trong một ngách, đối thủ
> *đầu tiên* mới là đối thủ đắt giá nhất — không phải đối thủ thứ mười. Ngược lại, nếu ngành đã có
> mười người chơi, việc thêm một người nữa gần như không đổi gì; muốn cải thiện biên lợi nhuận thì
> phải đi hướng khác — **khác biệt hoá** ([bài 8](bai_08_canh_tranh_doc_quyen.md)) chứ không phải
> đếm đối thủ.

Sách còn dùng cùng bảng này để giải thích **thương mại quốc tế** (tr. 396–397): nếu Nhật chỉ có Toyota
và Honda, Đức chỉ có Volkswagen và BMW, Mỹ chỉ có Ford và General, thì đóng cửa biên giới cho mỗi nước
một thị trường **hai** người bán; mở cửa cho cả thế giới một thị trường **sáu** người bán.

> *"Như vậy, ngoài lý thuyết về lợi thế cạnh tranh đã được thảo luận ở Chương 3, lý thuyết về thị
> trường độc quyền nhóm cho chúng ta một giải thích khác cho việc tại sao tất cả các quốc gia đều có
> lợi từ việc tự do hóa thương mại."*

---

## 6. 📚 Nghiệm Cournot — chứng minh công thức tổng quát

Sách không đưa công thức, chỉ mô tả cơ chế. Nhưng với đường cầu tuyến tính thì rút ra được, và nó
gọn tới mức đáng nhớ.

Gọi $n$ là số doanh nghiệp giống nhau, mỗi bên bơm $q$, tổng $Q = nq$, giá $P = a - Q$, chi phí biên
bằng 0. Lợi nhuận của **một** doanh nghiệp:

$$\pi = q \cdot (a - Q_{\text{người khác}} - q)$$

Đạo hàm theo $q$ rồi cho bằng 0:

$$a - Q_{\text{người khác}} - 2q = 0$$

Vì các doanh nghiệp giống nhau nên $Q_{\text{người khác}} = (n-1)q$, thay vào:

$$a - (n-1)q - 2q = 0 \quad\Longrightarrow\quad q^\* = \frac{a}{n+1}$$

Suy ra ba công thức của cả mục 5:

$$q^\* = \frac{a}{n+1}, \qquad Q = \frac{n}{n+1}\,a, \qquad P = \frac{a}{n+1}$$

Với $a = 120$: $n=1$ cho 60 gallon và $60 — **đúng kết cục độc quyền ở Bảng 1**. $n=2$ cho 40 gallon
mỗi bên và $40 — **đúng cân bằng Nash tìm được ở mục 4**. Một công thức, hai kiểm chứng.

Ba điều đọc thẳng ra từ công thức:

1. **Giá luôn dương với mọi $n$ hữu hạn.** Cạnh tranh hoàn hảo là *giới hạn*, không bao giờ đạt tới.
2. **Tổng sản lượng $\frac{n}{n+1}a$ tăng dần nhưng chậm lại.** Từ 1 lên 2 người bán, sản lượng tăng
   1/3. Từ 10 lên 11, tăng chưa tới 1%.
3. **Lợi nhuận ngành $= \frac{n}{(n+1)^2}a^2$ giảm đơn điệu.** Mỗi người mới vào không chỉ chia nhỏ
   miếng bánh — họ **làm miếng bánh nhỏ đi**.

Mô hình này mang tên **Antoine Augustin Cournot**, người viết ra nó năm **1838** — trước Nash 112 năm.
Nash chỉ đặt tên cho thứ Cournot đã tính.

---

## 7. Tình thế tiến thoái lưỡng nan của người tù và chiến lược thống soái

Đến đây sách rẽ sang một câu chuyện tưởng như không liên quan (tr. 397):

> **Tình huống tiến thoái lưỡng nan của người tù** *(prisoners' dilemma)*: một trò chơi giữa hai người
> tù qua đó cho thấy tại sao sự hợp tác lại trở nên khó khăn ngay cả khi nó có lợi cho cả hai.

Bonnie và Clyde bị bắt. Cảnh sát đủ chứng cứ cho tội mang súng trái phép — **1 năm** cho mỗi người.
Cảnh sát nghi họ cướp ngân hàng nhưng không có bằng chứng, nên tách hai phòng và chào mỗi người cùng
một lời (tr. 398):

> *"Bây giờ, chúng tôi có thể bắt giam anh một năm. Nhưng nếu anh thừa nhận đã thực hiện vụ cướp ngân
> hàng và tố cáo đồng phạm của anh, anh sẽ được miễn tội và thả tự do, còn đồng phạm của anh sẽ phải
> ở tù 20 năm. Nhưng nếu cả hai anh đều thừa nhận đã cướp ngân hàng… mỗi người bọn anh sẽ phải nhận
> án phạt 8 năm tù ngay lập tức."*

**Hình 1, tr. 398** — số trong ô là **số năm tù, càng ít càng tốt**:

```
                          QUYẾT ĐỊNH CỦA BONNIE
                     thú tội            giữ im lặng
                 ┌──────────────────┬──────────────────┐
        thú tội  │ Bonnie:  8 năm   │ Bonnie: 20 năm   │
 QUYẾT           │ Clyde :  8 năm   │ Clyde :  0 năm   │
 ĐỊNH            ├──────────────────┼──────────────────┤
 CỦA    giữ      │ Bonnie:  0 năm   │ Bonnie:  1 năm   │
 CLYDE  im lặng  │ Clyde : 20 năm   │ Clyde :  1 năm   │
                 └──────────────────┴──────────────────┘
```

Lập luận của Bonnie, chép nguyên (tr. 398):

> *"Tôi không biết Clyde sẽ làm gì. Nếu anh ta giữ im lặng, cách tốt nhất là tôi sẽ thú tội để được
> thả tự do hơn là phải ngồi tù 1 năm. Nếu anh ta thú tội, chiến lược tốt nhất của tôi vẫn là thú tội
> để ngồi tù tám năm thay vì phải ngồi tù 20 năm. Do đó, **mặc cho Clyde sẽ làm gì**, tôi sẽ có lợi
> hơn nếu như tôi thú tội."*

Cấu trúc "mặc cho đối phương làm gì" có tên riêng (tr. 398):

> **Chiến lược thống soái** *(dominant strategy)*: là chiến lược tốt nhất cho một người chơi, **bất kể**
> người chơi kia lựa chọn chiến lược nào.

⚠️ **Đừng nhầm chiến lược thống soái với cân bằng Nash.** Chiến lược thống soái là thuộc tính của
**một** người chơi; cân bằng Nash là thuộc tính của **một cặp lựa chọn**. Khi cả hai bên đều có chiến
lược thống soái thì cặp đó tất nhiên là cân bằng Nash — nhưng chiều ngược lại **không đúng**. Cân bằng
Nash (40, 40) ở mục 4 *không* đến từ chiến lược thống soái: bơm 40 chỉ tốt nhất **khi** đối phương bơm
40, chứ không phải khi họ bơm 0.

Kết cục: cả hai thú tội, **8 năm mỗi người** — trong khi cùng im lặng chỉ **1 năm**. Đây là điểm cay
đắng của trò chơi: **cả hai đều chơi tối ưu và cả hai đều thua**.

Và sách chặn trước câu hỏi hiển nhiên nhất (tr. 399):

> *"Nhưng liệu rằng hai tên tội phạm này có thực là sẽ giữ im lặng, đơn giản chỉ bởi vì chúng đã thỏa
> thuận với nhau như vậy? Một khi chúng bị tra xét một cách riêng biệt, **logic về lợi ích cá nhân sẽ
> thắng** và làm cho chúng thú tội."*

Nói cách khác: **một thỏa thuận không tự thi hành thì không phải là một thỏa thuận.**

---

## 8. Bốn hoàn cảnh, một cấu trúc

Đây là chỗ chương này chuyển từ một câu chuyện thành một **công cụ**. Cùng một bộ máy — tìm chiến lược
thống soái, tìm cân bằng Nash, so với kết cục tốt nhất cho cả hai — chạy qua bốn hoàn cảnh không liên
quan gì tới nhau:

| #   | Trò chơi                        | Nguồn              | Cân bằng Nash                  | Tốt nhất cho cả hai          |
| --- | ------------------------------- | ------------------ | ------------------------------ | ---------------------------- |
| a   | Bonnie và Clyde                 | Hình 1, tr. 398    | cùng thú tội — 8 năm           | cùng im lặng — 1 năm         |
| b   | Jack và Jill bơm nước           | Hình 2, tr. 399    | cùng 40 gal — $1.600           | cùng 30 gal — $1.800         |
| c   | Chạy đua vũ trang Mỹ–Liên Xô    | Hình 3, tr. 401    | cùng trang bị — cùng nguy hiểm | cùng giải trừ — cùng an toàn |
| d   | Exxon và Texaco khoan chung mỏ  | Hình 4, tr. 402    | cùng 2 giếng — $4 tr           | cùng 1 giếng — $5 tr         |
| e   | Chiến tranh thuế quan Mỹ–Mexico | bài tập 4, tr. 414 | cùng thuế cao — $20 tỷ         | cùng thuế thấp — $25 tỷ      |

Trong cả năm, cân bằng Nash **không phải** kết cục tốt nhất. Đó là định nghĩa của tiến thoái lưỡng nan.

⚠️ **Hình 3 (chạy đua vũ trang) không có số trong sách** — các ô chỉ ghi *"bị nguy hiểm"*, *"được an
toàn và mạnh"*. Vì thế code chỉ giải bốn trò chơi có số. Nếu bạn thấy ở đâu đó một bảng số cho Hình 3,
đó là số ai đó tự thêm vào, không phải của Mankiw.

### 📚 Ba ví dụ đáng dừng lại

**Chạy đua vũ trang** (tr. 401–402). Với mỗi nước, trang bị thêm vũ khí là chiến lược thống soái: nếu
đối phương trang bị, mình phải theo để không mất thế; nếu đối phương giải trừ, mình trang bị để mạnh
hơn. Kết quả là cả hai cùng nguy hiểm. Sách rút ra một câu rất sắc (tr. 402):

> *"Cũng giống như các cartel gặp phải các vấn đề trong việc thực hiện các mức sản lượng, Hoa Kỳ và
> Liên Xô đều **sợ rằng đối thủ sẽ không thực hiện các cam kết**."*

Hiệp định kiểm soát vũ khí và thỏa thuận cartel gặp **đúng một** vấn đề: không ai cưỡng chế được.

**Nguồn tài nguyên chung** (tr. 402). Exxon và Texaco ngồi trên một mỏ dầu chung trị giá $12 triệu.
Mỗi giếng tốn $1 triệu, và **số dầu lấy được tỷ lệ với số giếng của mình trên tổng số giếng**:

|                    | Exxon 2 giếng            | Exxon 1 giếng            |
| ------------------ | ------------------------ | ------------------------ |
| **Texaco 2 giếng** | Exxon $4tr / Texaco $4tr | Exxon $3tr / Texaco $6tr |
| **Texaco 1 giếng** | Exxon $6tr / Texaco $3tr | Exxon $5tr / Texaco $5tr |

Kiểm ô góc trên phải: Exxon 1 giếng trên tổng 3 giếng → được 1/3 × $12tr = $4tr, trừ $1tr chi phí =
**$3tr**. Texaco 2/3 × $12tr = $8tr, trừ $2tr = **$6tr**. Khớp.

Cái mất ở đây **không phải** là chuyển từ túi này sang túi kia — giếng thứ hai là **lãng phí thuần**:
nó không moi thêm được giọt dầu nào, chỉ tốn thêm $1 triệu tiền khoan.

**Chiến tranh thuế quan** (bài tập 4, tr. 414). Thuế cao là chiến lược thống soái cho cả hai; kết cục
$20 tỷ mỗi bên thay vì $25 tỷ. Và đó chính là **lý do tồn tại của các hiệp định thương mại**: NAFTA,
WTO, CPTPP không tạo ra lợi ích mới, chúng chỉ **biến kết cục hợp tác thành thứ có thể cưỡng chế được**.
Sách hỏi thẳng ở câu (c) của bài tập.

---

## 9. Nghiên cứu tình huống — OPEC

Sách chuyển thẳng từ Jack–Jill sang thật (tr. 400):

> *"nhưng nếu chúng ta chuyển từ nước sinh hoạt sang dầu thô, từ Jack và Jill sang **Iran và Iraq**,
> thì câu chuyện này gần đúng với thực tế."*

Dòng thời gian, theo tr. 400–401:

| Năm                 | Sự kiện                                                                     | Giá dầu       |
| ------------------- | --------------------------------------------------------------------------- | ------------- |
| 1960                | OPEC thành lập: Iran, Iraq, Kuwait, Ả Rập Saudi, Venezuela                  |               |
| 1970                | thêm 8 nước: Qatar, Indonesia, Libya, UAE, Algeria, Nigeria, Ecuador, Gabon |               |
| 1972                |                                                                             | $3/thùng      |
| 1974                |                                                                             | $11/thùng     |
| 1981                | đỉnh cao của sự hợp tác                                                     | $35/thùng     |
| giữa thập niên 1980 | *"các nước thành viên bắt đầu tranh cãi về các mức sản lượng"*              |               |
| 1986                |                                                                             | **$13/thùng** |

Sách nói 13 nước này *"nắm giữ khoảng ¾ trữ lượng dầu mỏ thế giới"* và rằng giai đoạn **1973–1985** là
*"khoảng thời gian thành công nhất của OPEC trong việc duy trì sự hợp tác và mức giá cao"*.

Hai điểm đáng ghi:

**Thứ nhất**, OPEC không sụp vì bị ai đánh bại — nó sụp vì **chính các thành viên gian lận**. Đó đúng
là bài toán của Jack ở tr. 394, phóng to lên quy mô quốc gia.

**Thứ hai**, đây là ví dụ hiếm hoi trong sách nơi **sự thiếu hợp tác là tin tốt** (tr. 401):

> *"Trong lúc sự thiếu hợp tác giữa các nước OPEC làm giảm lợi nhuận của các nước sản xuất dầu xuống
> dưới mức mà đáng lẽ ra họ sẽ nhận được, thì **nó đã mang lại lợi ích cho người tiêu dùng toàn thế
> giới**."*

⚠️ **Sách viết năm nào?** Câu cuối của nghiên cứu tình huống nhắc *"giá dầu đã tăng đáng kể trong năm
2007 và 2008"* và quy nguyên nhân cho *"sự tăng lên trong nhu cầu của thị trường dầu thế giới"* từ
Trung Quốc, **không phải** do OPEC hạn chế nguồn cung. Vậy bản gốc là **ấn bản khoảng 2009–2011**.
Đối chiếu với 2026: OPEC đã mở rộng thành **OPEC+** (có Nga từ 2016), Ecuador rút 2020, Qatar rút 2019,
Angola rút 2024 — và Mỹ, nhờ dầu đá phiến, trở thành **nước sản xuất dầu lớn nhất thế giới** từ 2018,
điều làm quyền lực định giá của cartel yếu đi hẳn so với thời điểm sách viết. Cơ chế trong sách vẫn
đúng; danh sách thành viên và cán cân quyền lực thì đã đổi.

---

## 10. Tiến thoái lưỡng nan có phải lúc nào cũng xấu không

Câu hỏi này ít khi được hỏi, và sách trả lời rất rõ ở tr. 403: **còn tùy bạn đứng ở đâu.**

| Trò chơi          | Thiếu hợp tác là… | Vì sao                                                 |
| ----------------- | ----------------- | ------------------------------------------------------ |
| Chạy đua vũ trang | **xấu**           | cả hai nước cùng nguy hiểm                             |
| Giếng dầu chung   | **xấu**           | giếng thứ hai là lãng phí thuần                        |
| Bonnie và Clyde   | **tốt**           | *"nó cho phép cảnh sát kết án họ đầy đủ tội hơn"*      |
| Độc quyền nhóm    | **tốt**           | sản lượng gần mức tối ưu hơn, giá gần chi phí biên hơn |

Rồi sách nối thẳng về **bàn tay vô hình** của [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md), và
đây có lẽ là câu hay nhất chương (tr. 403):

> *"bàn tay vô hình chỉ giúp thị trường phân bổ các nguồn lực một cách có hiệu quả khi thị trường đó
> là thị trường cạnh tranh, và **thị trường chỉ mang tính cạnh tranh khi các doanh nghiệp trong đó
> không thể hợp tác với nhau**."*

Đọc chậm câu này. Nó nói rằng cạnh tranh **không phải trạng thái tự nhiên** của thị trường — nó là
thứ tồn tại được **chỉ vì** việc cấu kết quá khó. Toàn bộ luật chống độc quyền ở mục 14 sinh ra từ ý đó.

---

## 11. Trò chơi lặp — vì sao đôi khi người ta vẫn hợp tác

Sách thừa nhận rằng bức tranh trên quá u ám so với thực tế (tr. 403):

> *"Không phải tất cả các tù nhân khi bị xét hỏi đều quyết định sẽ tố giác đồng phạm của họ. Các cartel
> thỉnh thoảng cũng thành công trong việc duy trì các thỏa thuận cấu kết… bởi vì họ chơi trò chơi này
> **không chỉ một mà là nhiều lần**."*

Cơ chế, dùng lại Jack và Jill (tr. 404):

> *"họ đồng ý rằng một khi một trong số bọn họ thất hứa và cùng sản xuất 40 gallon, cả hai sẽ cùng sản
> xuất 40 gallon từ đó về sau. Hình phạt này rất dễ thực hiện bởi vì nếu một bên sản xuất ở mức sản
> lượng cao, bên kia cũng có lý do để làm điều tương tự."*

Và câu quyết định (tr. 404):

> *"Mỗi người đều biết rằng rời bỏ thỏa thuận sẽ làm tăng lợi nhuận của họ từ 1.800 đô la lên 2.000 đô
> la. **Nhưng mối lợi này chỉ kéo dài được một tuần.** Sau đó, lợi nhuận sẽ giảm xuống mức 1.600 đô la
> và giữ nguyên mức này."*

Toàn bộ chiến lược này gói lại thành một cái tên: **trừng phạt vĩnh viễn** (*grim trigger*) — hợp tác
cho tới khi bị phản bội một lần, rồi bội ước mãi mãi.

---

## 12. 📚 Hệ số chiết khấu — hợp tác bền khi nào

Sách dừng ở câu *"khi những người chơi thực sự quan tâm tới lợi nhuận trong tương lai"*. Nhưng câu đó
**đo được**, và ngưỡng ra rất đẹp.

Gọi $d$ là **hệ số chiết khấu** mỗi tuần: một đô la tuần sau đáng giá $d$ đô la hôm nay.

$$\text{giữ hợp tác mãi mãi} = 1800 + 1800d + 1800d^2 + \dots = \frac{1800}{1-d}$$

$$\text{bội ước một lần rồi bị phạt mãi} = 2000 + \frac{1600\,d}{1-d}$$

Hợp tác bền khi vế trên không nhỏ hơn vế dưới:

$$\frac{1800}{1-d} \ \ge\ 2000 + \frac{1600\,d}{1-d} \quad\Longrightarrow\quad 400\,d \ \ge\ 200 \quad\Longrightarrow\quad \boxed{d \ \ge\ \tfrac{1}{2}}$$

Dạng tổng quát, đáng thuộc:

$$d \ \ge\ \frac{\text{món lợi từ bội ước}}{\text{món lợi từ bội ước} + \text{thiệt hại mỗi kỳ sau đó}} = \frac{2000-1800}{2000-1600} = \frac{1}{2}$$

Code mục 6 quét $d$ từ 1/10 tới 99/100 và cho thấy hai cột **cắt nhau đúng tại $d = 1/2$**.

**Đọc $d$ như thế nào trong đời thật:**

| $d$ gần 1                                 | $d$ gần 0                          |
| ----------------------------------------- | ---------------------------------- |
| quan hệ lâu dài, còn gặp nhau nhiều lần   | "chỉ còn lần này"                  |
| hợp đồng khung nhiều năm                  | đơn hàng lẻ, mua đứt bán đoạn      |
| nhà cung cấp trong nước, gặp mặt hàng quý | nhà cung cấp gặp một lần ở hội chợ |
| nhân viên đang xây sự nghiệp ở công ty    | nhân viên đã nộp đơn nghỉ          |

> 💼 Suy ra một câu dùng được ngay: **hợp tác sụp đổ khi tương lai ngắn lại.** Nhân viên sắp nghỉ,
> đối tác sắp phá sản, giám đốc sắp hết nhiệm kỳ, hợp đồng sắp hết hạn không tái ký — đó không phải
> vấn đề đạo đức, đó là $d$ tụt xuống dưới ngưỡng. Cách chữa cũng đọc thẳng ra từ công thức: **kéo dài
> tương lai** (gia hạn hợp đồng trước khi đàm phán chuyện khác), hoặc **giảm món lợi từ bội ước**
> (đặt cọc, bảo lãnh, thanh toán theo tiến độ).

---

## 13. Giải đấu Axelrod và ăn miếng trả miếng

Sách kể lại thí nghiệm của nhà chính trị học **Robert Axelrod** (tr. 404):

> *"Mọi người tham gia bằng cách gửi các chương trình máy tính được thiết kế để chơi trò chơi về tình
> huống tiến thoái lưỡng nan lặp đi lặp lại của người tù… 'Người chiến thắng' là chương trình nhận
> được tổng số năm ở tù ít nhất."*

Người thắng là chiến lược đơn giản nhất trong cuộc thi (tr. 404–405):

> **Ăn miếng trả miếng** *(tit for tat)*: *"một người chơi nên bắt đầu bằng việc hợp tác và sau đó làm
> theo bất cứ điều gì mà người chơi kia đã làm ở lần gần nhất."*
>
> *"Axelrod đã ngạc nhiên khi biết rằng, chiến lược đơn giản này hiệu quả hơn bất cứ chiến lược phức
> tạp nào khác mà mọi người đã sử dụng."*

Sách còn ghi rằng nó *"thực chất là chiến lược 'gieo nhân nào, gặp quả đó' trong kinh thánh"*.

Code mục 7 dựng một **giải đấu thu nhỏ**: năm chiến lược, mỗi cặp đánh 10 tuần bằng trò chơi Jack–Jill
(điểm = tổng lợi nhuận, càng cao càng tốt), đánh vòng tròn kể cả với bản sao của chính mình.

| #   | Chiến lược                  |        (1) |    (2) |    (3) |    (4) |    (5) |   **TỔNG** |
| --- | --------------------------- | ---------: | -----: | -----: | -----: | -----: | ---------: |
| 1   | Luôn hợp tác                |     18.000 | 15.000 | 18.000 | 18.000 | 18.000 |     87.000 |
| 2   | Luôn bội ước                | **20.000** | 16.000 | 16.400 | 16.400 | 16.800 |     85.600 |
| 3   | **Ăn miếng trả miếng**      |     18.000 | 15.900 | 18.000 | 18.000 | 18.000 | **87.900** |
| 4   | Trừng phạt vĩnh viễn        |     18.000 | 15.900 | 18.000 | 18.000 | 18.000 | **87.900** |
| 5   | Ăn miếng trả miếng độ lượng |     18.000 | 15.800 | 18.000 | 18.000 | 18.000 |     87.800 |

⚠️ **Đây không phải bản sao giải đấu của Axelrod** — ông có hàng chục chương trình dự thi, đây chỉ có
năm. Bảng này minh hoạ cơ chế chứ không tái lập kết quả lịch sử.

Ba điều bảng này nói thật, kể cả điều bất tiện:

**Một — ăn miếng trả miếng không thắng nổi ai.** Gặp "luôn bội ước" nó được 15.900 còn đối thủ được
16.400: nó **thua** trận đó. Gặp mọi chiến lược khác nó hoà. Vậy mà nó dẫn đầu bảng tổng. Đó chính là
nhận xét của Axelrod: **không cần thắng ai, chỉ cần không bao giờ bị vắt kiệt.**

**Hai — "trừng phạt vĩnh viễn" đồng hạng nhất, ngang hệt.** Trong một thế giới không có sai sót, hai
chiến lược này **không phân biệt được**. Mục tiếp theo mới tách chúng ra.

**Ba — "độ lượng" có giá của nó.** Nó xếp sau đúng $100, và toàn bộ khoảng cách đó đến từ trận gặp
"luôn bội ước" (15.800 so với 15.900): kẻ bội ước được ăn không **hai** tuần đầu thay vì một.

---

## 14. Một lần lỡ tay — chỗ sách chỉ nói bằng lời

Sách có một nhận xét ngắn ở tr. 404 mà rất dễ đọc lướt qua:

> *"chiến lược đã được mô tả trước kia cho cartel cung cấp nước sinh hoạt của Jack và Jill – là sẽ bội
> ước mãi mãi ngay khi người chơi kia bội ước – **không có tính vị tha cho lắm**. Trong một trò chơi
> được lặp đi lặp lại nhiều lần, chiến lược cho phép người chơi quay lại kết cục hợp tác sau một giai
> đoạn không hợp tác có lẽ được ưa thích hơn."*

Đặt con số vào nhận xét đó. Giả sử ở **tuần 5**, Jack lỡ tay bơm 40 gallon — không cố ý, chỉ là nhầm:

| Cả hai cùng dùng chiến lược |   Jack |   Jill |       Tổng | Mất so với hoàn hảo |
| --------------------------- | -----: | -----: | ---------: | ------------------: |
| Ăn miếng trả miếng          | 17.700 | 17.700 |     35.400 |                 600 |
| **Trừng phạt vĩnh viễn**    | 17.100 | 17.100 | **34.200** |           **1.800** |
| Ăn miếng trả miếng độ lượng | 18.200 | 17.700 | **35.900** |             **100** |
| *(không ai lỡ tay)*         | 18.000 | 18.000 |     36.000 |                   0 |

**Trừng phạt vĩnh viễn mất nhiều gấp ba lần ăn miếng trả miếng.** Một cái nhầm ở tuần 5 kéo cả hai
xuống đáy trong toàn bộ năm tuần còn lại.

**Ăn miếng trả miếng đỡ hơn nhưng vẫn không thoát ra được.** Nó rơi vào **vòng trả đũa so le**: tuần
này tôi phạt anh, tuần sau anh phạt tôi, và cứ thế tới hết. Không ai quay về hợp tác được.

**Chỉ "độ lượng" gần như không mất gì** — bỏ qua lần lỡ đầu tiên, và mọi thứ trở lại bình thường ngay
tuần sau.

Để ý một chi tiết trung thực: ở dòng "độ lượng", **Jack (người lỡ tay) được 18.200, nhiều hơn cả khi
không ai lỡ tay**. Độ lượng có thể bị lợi dụng — đó đúng là cái giá $100 ở mục 13. Đánh đổi: mất 100
vì bị bắt nạt, đổi lấy 500 vì phục hồi được sau sai sót.

> 💼 **Bài học quản trị, viết thẳng:** điều khoản phạt trong hợp đồng nên có **cửa quay lại**. Câu
> "vi phạm một lần là chấm dứt hợp tác vĩnh viễn" nghe cứng rắn và tưởng là an toàn, nhưng nó biến
> **một sai sót hành chính** thành **một cuộc chiến không lối thoát**. Ba dòng đầu của bảng trên là
> ba điều khoản phạt khác nhau, và chi phí của chúng chênh nhau 18 lần.

---

## 15. Chính sách chống độc quyền

Sách bắt đầu bằng cách nối về **Nguyên lý số 7** của [bài 1](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)
— *chính phủ thỉnh thoảng có thể cải thiện được những kết quả trên thị trường* — rồi rút ra mục tiêu
(tr. 405):

> *"các nhà hoạch định chính sách nên **khuyến khích các doanh nghiệp trong thị trường độc quyền nhóm
> cạnh tranh hơn là hợp tác** với nhau."*

**Hai bộ luật nền:**

| Luật        | Năm  | Nội dung, theo tr. 405–406                                                                                                       |
| ----------- | ---- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Sherman** | 1890 | biến thỏa thuận cấu kết từ *"dạng hợp đồng khó cưỡng chế thi hành"* thành **âm mưu phạm pháp**; phạt tới $50.000 hoặc một năm tù |
| **Clayton** | 1914 | cho **tư nhân** kiện, và nhận **bồi thường gấp ba lần** mức thiệt hại                                                            |

Điểm tinh tế của Clayton: bồi thường gấp ba là để **thuê tư nhân đi thực thi luật giúp nhà nước**.
Bộ Tư pháp không đủ người để soi mọi ngành; nạn nhân thì có động cơ tự đi tìm.

### Nghiên cứu tình huống — một cuộc điện thoại bất hợp pháp

Sách mở bằng Adam Smith, *Của Cải Của Các Quốc Gia* (tr. 406):

> *"Mọi người trong cùng một hoạt động thương mại hiếm khi gặp nhau, nhưng những cuộc đối thoại của họ
> thường kết thúc bằng một âm mưu chống lại công chúng hoặc là một mưu đồ nào đó để tăng giá."*

Rồi đưa bằng chứng đương đại: cuộc gọi giữa **Robert Crandall** (chủ tịch American Airlines) và
**Howard Putnam** (chủ tịch Braniff Airways), đăng trên *New York Times* ngày **24/2/1983** (tr. 406–407):

> **CRANDALL:** *Tôi nghĩ rằng thật là ngu xuẩn… khi cứ đấu đá nhau trong khi cả hai chẳng kiếm được
> một xu chết tiệt nào.*
> **PUTNAM:** *Anh có gợi ý gì?*
> **CRANDALL:** *Có, tôi có một gợi ý này cho anh. Hãy tăng giá vé của anh lên 20%. Tôi sẽ tăng giá vé
> của tôi vào sáng mai.*
> **PUTNAM:** *Robert, nhưng mà chúng ta….*
> **CRANDALL:** *Anh kiếm thêm được tiền và tôi cũng vậy.*
> **PUTNAM:** *Chúng ta không thể bàn bạc về việc định giá đâu*
> **CRANDALL:** *Ôi, Howard. Chúng ta có thể nói về bất cứ cái quái gì mà chúng ta muốn.*

Putnam ghi âm và nộp cho Bộ Tư pháp. Crandall bị khởi tố; hai năm sau dàn xếp, chấp nhận hạn chế cả
việc liên lạc với quan chức các hãng hàng không khác.

⚠️ **Ranh giới pháp lý ở đây rất hẹp và rất quan trọng với người làm kinh doanh.** Crandall **không**
tăng giá — ông ta chỉ **đề nghị**. Tự mình quyết định giữ giá cao là hoàn toàn hợp pháp. **Gọi điện
cho đối thủ để cùng thoả thuận giữ giá cao là phạm pháp.** Cùng một kết cục thị trường, hai địa vị
pháp lý khác hẳn nhau — vì cái bị cấm là **thoả thuận**, không phải mức giá.

---

## 16. Ba hành vi gây tranh cãi

Phần cuối chương là phần khó nhất, và sách nói rõ vì sao (tr. 407): không phải hành vi nào **trông
giống** giảm cạnh tranh cũng **thật sự** giảm cạnh tranh.

### 16.1 Cố định giá bán lẻ

Superduper bán đầu DVD cho cửa hàng với giá **$300**, và **buộc** họ bán lại không dưới **$350**
(tr. 407).

Thoạt nhìn: đây là cartel các nhà bán lẻ, do nhà sản xuất áp đặt. Toà từng xử là vi phạm.

Nhưng sách đưa **hai lập luận phản bác** (tr. 407–408):

**Thứ nhất — Superduper không có động cơ làm điều đó.** Nếu họ có quyền lực thị trường, họ đã dùng
**giá bán buôn** rồi. Và:

> *"bởi vì một cartel các nhà bán lẻ bán được ít hàng hơn một nhóm các nhà bán lẻ cạnh tranh nhau,
> **Superduper sẽ bị thiệt hại** khi các nhà bán lẻ của họ là một cartel."*

**Thứ hai — nó giải quyết vấn đề kẻ thụ hưởng miễn phí.** Không có sàn giá thì khách vào cửa hàng lớn
để xem hàng và hỏi nhân viên, rồi ra cửa hàng giảm giá để mua:

> *"dịch vụ tốt là một hàng hóa công của các nhà bán lẻ sản phẩm của Superduper… các nhà bán lẻ giảm
> giá sẽ tận dụng dịch vụ cung cấp thông tin từ các nhà bán lẻ khác, và dẫn đến có ít dịch vụ hơn mong
> muốn."*

> 📚 Ngày nay hiện tượng này có tên riêng: **showrooming** — xem hàng ở cửa hàng, quét mã, mua trên
> mạng. Vấn đề Mankiw mô tả năm 2009 giờ là bài toán sống còn của mọi chuỗi bán lẻ có mặt bằng.

Sách chốt bằng nguyên tắc in nghiêng, và nó áp cho cả ba hành vi trong mục này (tr. 408):

> *"các hoạt động kinh doanh tuy có vẻ làm giảm đi tính cạnh tranh nhưng **thực tế có thể có những mục
> đích chính đáng**."*

### 16.2 Bán phá giá

Coyote Air độc quyền vài tuyến bay. Roadrunner Express nhảy vào, lấy **20%** thị phần, để lại **80%**
cho Coyote. Coyote giảm giá vé. Có phải để giết đối thủ rồi tăng giá lại?

Sách nghi ngờ, và lý do là **số học** (tr. 408):

> *"nếu Coyote bắt đầu bán vé với giá rẻ tới mức họ bị thua lỗ, họ sẽ phải chuẩn bị cho việc có thêm
> nhiều chuyến bay vì giá rẻ sẽ thu hút thêm khách hàng. Trong khi đó, Roadrunner có thể đáp trả hành
> vi phá giá của Coyote bằng cách **cắt giảm số chuyến bay**. Kết quả là, **Coyote sẽ phải chịu hơn
> 80% tổn thất**."*

Đó là một lập luận rất đẹp: **kẻ có thị phần lớn hơn thì lỗ nhiều hơn trong cuộc chiến giá.** Muốn giết
đối thủ nhỏ, bạn phải chảy máu theo tỷ lệ thị phần của mình — tức là nhiều hơn nó.

Sách đóng bằng một câu đùa: *"Cũng giống như trong bộ phim hoạt hình Roadrunner-Coyote, kẻ săn mồi
phải chịu nhiều tổn thất hơn con mồi."*

### 16.3 Bán kèm sản phẩm

Hãng phim Makemoney có hai phim, *Ironman* (bom tấn) và *Hamlet* (nghệ thuật), và bán chúng thành một
gói (tr. 408–409). Toà tối cao cấm, lập luận rằng hãng dùng cầu cao của *Ironman* để ép rạp mua *Hamlet*.

**Sách bác bỏ lập luận đó bằng số** (tr. 409): nếu rạp sẵn lòng trả $20.000 cho *Ironman* và **$0** cho
*Hamlet*, thì rạp sẽ mua cả gói với giá **$20.000** — đúng bằng giá của mình *Ironman*.

> *"Ép buộc rạp chiếu phim mua một bộ phim không có giá trị thương mại như là một phần của hợp đồng
> **không làm tăng mức độ sẵn lòng chi trả** của họ."*

**Nhưng sách lại tìm ra một lý do khác, và lý do đó thì đúng** (tr. 409): bán kèm là một dạng
**phân biệt giá** ([bài 7](bai_07_doc_quyen_va_phan_biet_gia.md)). Hai rạp, sở thích **ngược nhau**:

|                 | *Ironman* | *Hamlet* |    Tổng |
| --------------- | --------: | -------: | ------: |
| City Theater    |   $15.000 |   $5.000 | $20.000 |
| Country Theater |    $5.000 |  $15.000 | $20.000 |

| Cách bán        | Giá                                    |   Doanh thu |
| --------------- | -------------------------------------- | ----------: |
| Riêng từng phim | mỗi phim $15.000, mỗi rạp mua một phim | **$30.000** |
| Theo gói        | cả gói $20.000, cả hai rạp mua         | **$40.000** |

Bán kèm hơn **$10.000, tức là +33%**. Code mục 9 quét mọi mức giá có thể trong cả hai trường hợp và
xác nhận cả hai kết luận.

**Điều kiện để bán kèm sinh lời, viết thành một câu kiểm tra được:** khách hàng phải **xếp hạng các sản
phẩm theo thứ tự ngược nhau**. Nếu ai cũng thích cùng một món thì gói vô dụng — đó chính là trường hợp
đầu, và cũng là lý do lập luận của toà không đứng vững.

> 💼 Ba câu hỏi trước khi đóng gói sản phẩm, đọc thẳng từ hai bảng trên:
> **(1)** Các nhóm khách có xếp hạng ngược nhau không, hay ai cũng chỉ muốn một món?
> **(2)** Tổng mức sẵn lòng chi trả của các nhóm có **gần nhau** không? (Ở đây cả hai đều đúng $20.000
> — đó là lý do một mức giá gói phục vụ được cả hai.)
> **(3)** Món "kèm" có chi phí biên gần bằng 0 không? Phần mềm, nội dung số, dịch vụ hậu mãi thì có;
> hàng vật lý thì không.

### Nghiên cứu tình huống — vụ kiện Microsoft

Vụ kiện năm **1998**, đúng về hành vi bán kèm: có nên cho Microsoft tích hợp trình duyệt Internet vào
Windows hay không (tr. 409–411).

| Bên                                     | Lập luận                                                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chính phủ Hoa Kỳ (Franklin Fisher, MIT) | dùng quyền lực trên thị trường **hệ điều hành** để bành sang thị trường **trình duyệt**, chặn công ty phần mềm khác                                     |
| Microsoft (Richard Schmalensee, MIT)    | *"việc đưa các đặc điểm mới vào các sản phẩm cũ là một bản chất của phát triển công nghệ"* — xe hơi gắn máy CD và điều hoà, máy chụp hình gắn đèn flash |

Về quy mô quyền lực: chính phủ chỉ ra **hơn 80% máy tính cá nhân** chạy Windows; Microsoft đáp rằng giá
Windows *"khoảng 50 đô la, chỉ bằng 3% giá của một chiếc máy tính thông thường"*.

Diễn biến, theo tr. 410–411:

| Thời điểm | Sự việc                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------- |
| 11/1999   | thẩm phán Penfield Jackson kết luận Microsoft lạm dụng sức mạnh độc quyền                             |
| 6/2000    | Jackson yêu cầu **tách làm hai công ty** — một bán hệ điều hành, một bán phần mềm ứng dụng            |
| 2001      | phiên kháng cáo **lật ngược** quyết định chia tách, chuyển vụ kiện sang thẩm phán khác                |
| 9/2001    | Bộ Tư pháp thông báo không tìm cách chia tách nữa                                                     |
| 11/2002   | kết thúc: Microsoft chấp nhận một số hạn chế; chính phủ chấp nhận trình duyệt là một phần của Windows |

⚠️ Đối chiếu 2026: sách kết thúc bằng việc Microsoft *"vẫn phải vật lộn với… các vụ kiện từ Liên minh
châu Âu"*. Từ đó tới nay, trọng tâm chống độc quyền công nghệ đã chuyển hẳn sang **Google, Apple,
Amazon, Meta**, và EU đã ban hành **Đạo luật Thị trường Kỹ thuật số (DMA)** năm **2022** — đạo luật cấm
trước một số hành vi bán kèm thay vì kiện từng vụ như thời Microsoft. Cơ chế kinh tế trong sách không đổi;
công cụ pháp lý thì đã đổi từ **kiện sau** sang **cấm trước**.

Kết luận của sách về toàn bộ mục này (tr. 411):

> *"các nhà hoạch định chính sách cần phải **cẩn thận khi họ sử dụng quyền lực lớn lao của các bộ luật
> chống độc quyền** để đặt ra các hạn chế lên hành vi của doanh nghiệp."*

---

## 17. 💼 Cuộc chiến giảm giá — kiểm tra chứ không giả định

Mọi trò chơi ở mục 8 đều được **cho sẵn** bảng lợi ích. Câu hỏi công bằng là: cấu trúc tiến thoái lưỡng
nan có thật sự **xuất hiện** từ số liệu kinh doanh, hay chỉ là một giả định đẹp mà người ta áp vào?

Kiểm tra bằng một mô hình dựng từ đầu, không mượn ô nào của sách. Hai chuỗi bán lẻ A và B, đơn vị
**nghìn đồng**:

- Tổng cầu: $Q = 2000 - 10 \times \bar{P}$ (với $\bar P$ là giá bình quân hai bên) — hạ giá làm thị
  trường nở ra
- Thị phần của A: $\dfrac{1}{2} + \dfrac{1}{50}\,(P_B - P_A)$ — ai rẻ hơn thì bán được nhiều hơn
- Chi phí biên: **60** nghìn đồng/đơn vị
- Hai lựa chọn: giữ giá **100**, hoặc giảm 10% xuống **90**

Cho chạy, không giả định gì thêm:

| Giá A | Giá B | Q bán ra | A bán | B bán |   LN của A |   LN của B |
| ----: | ----: | -------: | ----: | ----: | ---------: | ---------: |
|    90 |    90 |    1.100 |   550 |   550 |     16.500 |     16.500 |
|    90 |   100 |    1.050 |   735 |   315 | **22.050** |     12.600 |
|   100 |    90 |    1.050 |   315 |   735 |     12.600 | **22.050** |
|   100 |   100 |    1.000 |   500 |   500 | **20.000** | **20.000** |

Đưa đúng bốn ô đó vào **cùng bộ giải** đã dùng cho Bonnie–Clyde và Exxon–Texaco ở mục 8:

- Chiến lược thống soái của A: **giảm giá**. Của B: **giảm giá**.
- Cân bằng Nash: **cả hai cùng giảm** → 16.500 mỗi bên.
- Tốt nhất cho cả hai: **cả hai cùng giữ giá** → 20.000 mỗi bên.

**Cấu trúc tự hiện ra.** Không ai cài nó vào. Cả hai mất **3.500 nghìn đồng mỗi bên** so với việc không
ai giảm — và **không bên nào giành được thêm một phần trăm thị phần nào**, vì đối thủ đã giảm theo.

### Ba cách thoát, đọc thẳng từ các mục trên

| #   | Cách                                                                                                                             | Từ mục nào                                                                         | Điểm yếu                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------- |
| 1   | **Kéo dài tương lai**: hợp đồng khung nhiều năm thay vì đơn hàng lẻ, để $d$ tiến về 1                                            | [mục 12](#12--hệ-số-chiết-khấu--hợp-tác-bền-khi-nào)                               | cần đối thủ cũng nghĩ dài hạn           |
| 2   | **Bỏ qua một lần lỡ**: đừng tuyên bố "giảm giá một lần là chiến tranh vĩnh viễn"                                                 | [mục 14](#14-một-lần-lỡ-tay--chỗ-sách-chỉ-nói-bằng-lời)                            | có thể bị lợi dụng, giá $100 ở mục 13   |
| 3   | **Làm cầu bớt co giãn**: khách không so sánh được hai bên nữa thì hệ số nhạy thị phần tụt xuống, và **cám dỗ giảm giá biến mất** | [bài 3](bai_03_do_co_gian_va_dinh_gia.md), [bài 8](bai_08_canh_tranh_doc_quyen.md) | tốn thời gian, tốn tiền xây thương hiệu |

Cách (1) và (2) là **quản trị quan hệ bán hàng**. Cách (3) là **khác biệt hoá sản phẩm**. Cái thứ ba
bền hơn hẳn hai cái đầu vì một lý do rất đơn giản: **nó không cần đối thủ đồng ý điều gì.**

⚠️ **Và một ranh giới không được bước qua.** Cách (1) và (2) ở trên nói về việc *bạn tự quyết định*
chiến lược giá dài hạn của mình — hợp pháp. Nếu chúng biến thành **gọi điện cho đối thủ để cùng thống
nhất không giảm giá**, đó là hành vi Crandall bị khởi tố ở mục 15. Ranh giới nằm ở chữ **thoả thuận**,
không nằm ở mức giá.

---

## 18. Code minh hoạ

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-09-doc-quyen-nhom.py`.
> **Không cần cài gói nào.** File có sẵn tại [thuc_hanh/bai-09-doc-quyen-nhom.py](../thuc_hanh/bai-09-doc-quyen-nhom.py).

Toàn bộ tiền dùng **số nguyên**, mọi tỷ lệ dùng `Fraction` — không có số thực nào trong file, nên
chạy bao nhiêu lần cũng ra đúng một kết quả.

```python
"""Bai 9 - Doc quyen nhom va ly thuyet tro choi (Mankiw, chuong 17, tr. 391-420).

Chay: python3 bai-09-doc-quyen-nhom.py
Khong can cai goi nao ngoai thu vien chuan.
"""

from fractions import Fraction as F

DONG = "-" * 74


def tieu_de(so, ten):
    print()
    print("=" * 74)
    print(f"MUC {so}. {ten}")
    print("=" * 74)


def tien(x):
    """So nguyen co dau cham ngan cach nghin, kieu Viet Nam."""
    return f"{int(x):,}".replace(",", ".")


# ---------------------------------------------------------------------------
# MUC 1. Bang 1 tr. 392 - bieu cau nuoc sinh hoat cua thi tran
# ---------------------------------------------------------------------------
# Sach chi in bang so. Cong thuc dung sau lung no la mot duong cau tuyen tinh:
#     P = 120 - Q      (Q tinh bang gallon, P tinh bang do la)
# Chi phi bien bang 0 -> tong doanh thu CHINH LA tong loi nhuan.

GIA_TRAN = 120          # gia khi Q = 0
BUOC = 10               # sach di tung buoc 10 gallon


def gia(q):
    """Gia thi truong khi tong san luong la q gallon."""
    return max(GIA_TRAN - q, 0)


def loi_nhuan_nganh(q):
    """MC = 0 nen loi nhuan toan nganh = doanh thu = q * P(q)."""
    return q * gia(q)


# So lieu in trong Bang 1, tr. 392 (san luong, gia, tong doanh thu)
BANG_1_SACH = [
    (0, 120, 0), (10, 110, 1100), (20, 100, 2000), (30, 90, 2700),
    (40, 80, 3200), (50, 70, 3500), (60, 60, 3600), (70, 50, 3500),
    (80, 40, 3200), (90, 30, 2700), (100, 20, 2000), (110, 10, 1100),
    (120, 0, 0),
]

tieu_de(1, "Bang 1 tr. 392 - bieu cau nuoc sinh hoat")

print("Mo hinh dung lai:  P = 120 - Q,  chi phi bien = 0")
print()
print(f"{'San luong':>10} {'Gia':>8} {'Doanh thu':>12} {'Sach in':>10} {'Khop':>6}")
print(DONG)
khop_1 = 0
for q, p_sach, r_sach in BANG_1_SACH:
    p, r = gia(q), loi_nhuan_nganh(q)
    ok = (p == p_sach) and (r == r_sach)
    khop_1 += ok
    print(f"{q:>7} gal {'$' + str(p):>8} {tien(r):>12} {tien(r_sach):>10} {str(ok):>6}")
print(DONG)
print(f"Khop {khop_1}/{len(BANG_1_SACH)} dong.")


# ---------------------------------------------------------------------------
# MUC 2. Ba ket cuc: canh tranh, doc quyen, nhi quyen
# ---------------------------------------------------------------------------
tieu_de(2, "Ba ket cuc cua cung mot thi truong")

# (a) Canh tranh hoan hao: gia bang chi phi bien = 0 -> ban het 120 gallon.
q_ct = GIA_TRAN
# (b) Doc quyen / cartel: chon q toi da hoa loi nhuan nganh.
q_dq = max(range(0, GIA_TRAN + 1, BUOC), key=loi_nhuan_nganh)
# (c) Nhi quyen Nash: moi ben 40 gallon (chung minh o muc 3).
q_nq = 80

print(f"{'Ket cuc':<28} {'San luong':>10} {'Gia':>7} {'LN nganh':>10} {'Moi ben':>9}")
print(DONG)
for ten, q, n in [("Canh tranh hoan hao", q_ct, 0),
                  ("Doc quyen (hoac cartel)", q_dq, 2),
                  ("Nhi quyen - can bang Nash", q_nq, 2)]:
    ln = loi_nhuan_nganh(q)
    moi_ben = tien(ln // n) if n else "-"
    print(f"{ten:<28} {str(q) + ' gal':>10} {'$' + str(gia(q)):>7} {tien(ln):>10} {moi_ben:>9}")
print(DONG)
print("Nhi quyen nam GIUA hai thai cuc: san luong 80 > 60 nhung < 120;")
print("gia $40 < $60 nhung > $0. Dung nhu ket luan in nghieng tr. 395.")


# ---------------------------------------------------------------------------
# MUC 3. Vet can toan bo ma tran loi ich de tim can bang Nash
# ---------------------------------------------------------------------------
tieu_de(3, "Tim can bang Nash bang vet can - khong doan, chi thu het")

LUA_CHON = list(range(0, GIA_TRAN + 1, BUOC))


def loi_nhuan_rieng(q_toi, q_kia):
    """Loi nhuan cua mot nha san xuat khi hai ben bom q_toi va q_kia."""
    return q_toi * gia(q_toi + q_kia)


def phan_ung_tot_nhat(q_kia, luoi):
    """Tap san luong toi uu cua toi khi biet doi phuong bom q_kia."""
    tot = max(loi_nhuan_rieng(q, q_kia) for q in luoi)
    return [q for q in luoi if loi_nhuan_rieng(q, q_kia) == tot]


def tim_nash(luoi):
    """Tra ve (can bang that, can bang suy bien) tren mot luoi san luong."""
    pu = {q: phan_ung_tot_nhat(q, luoi) for q in luoi}
    tat_ca = [(a, b) for a in luoi for b in luoi if a in pu[b] and b in pu[a]]
    that = [(a, b) for a, b in tat_ca if loi_nhuan_rieng(a, b) > 0]
    return that, [x for x in tat_ca if x not in that]


print("Bang phan ung tot nhat (Jack chon gi khi biet Jill chon gi), luoi 10 gallon:")
print()
print(f"{'Jill bom':>10}   {'Jack nen bom':<44} {'LN Jack':>10}")
print(DONG)
for b in LUA_CHON:
    pu = phan_ung_tot_nhat(b, LUA_CHON)
    nhan = ", ".join(str(x) for x in pu) + " gal"
    if len(nhan) > 44:
        nhan = "moi muc deu nhu nhau (gia da bang 0)"
    print(f"{str(b) + ' gal':>10}   {nhan:<44} {tien(loi_nhuan_rieng(pu[0], b)):>10}")
print(DONG)

nash_that, nash_suy_bien = tim_nash(LUA_CHON)
print(f"Can bang Nash tim duoc  : {nash_that}")
print(f"Va them {len(nash_suy_bien)} diem SUY BIEN quanh (110-120, 110-120): o do tong san")
print("luong da vuot 120 nen gia bang 0 va ai bom bao nhieu cung lai 0 - moi lua")
print("chon deu 'toi uu' mot cach vo nghia. Loai chung bang dieu kien loi nhuan > 0.")
print()
print("Nhung ngay ca sau khi loai, van con BA diem chu khong phai mot. Vi sao?")
print("Vi tren luoi 10 gallon cua sach, khi doi phuong bom 30 thi bom 40 va bom 50")
print(f"lai y het nhau ({tien(loi_nhuan_rieng(40, 30))} do la ca hai) - mot the hoa do lam tron.")
print("That mo luoi ra thi cum nay co lai:")
print()
print(f"{'Buoc luoi':>11} {'So diem can bang':>18}   Can bang Nash that su")
print(DONG)
for buoc in (10, 5, 2, 1):
    that, _ = tim_nash(list(range(0, GIA_TRAN + 1, buoc)))
    print(f"{str(buoc) + ' gal':>11} {len(that):>18}   {that}")
print(DONG)
print("Cum luon la {(40-h, 40+h), (40, 40), (40+h, 40-h)} voi h dung bang buoc luoi.")
print("Luoi cang min, cum cang co ve (40, 40) - can bang Nash that su cua tro choi.")
print("Sach chi noi ket qua (40, 40) o tr. 394-395; day la cho chung minh no.")
print()

# Lat lai doan van tr. 394: Jack tinh nham 30 hay 40 gallon?
print("Doi chieu tung con so trong hai doan lap luan cua Jack, tr. 394:")
print()
print(f"  {'Jack':>5} {'Jill':>5} {'Tong':>6} {'Gia':>6} {'LN Jack':>9}   Sach viet gi")
print("  " + DONG[:66])
for q_jack, q_jill, ghi in [(30, 30, "1.800 - giu thoa thuan"),
                            (40, 30, "2.000 - boi uoc, co loi hon"),
                            (40, 40, "1.600 - ca hai cung boi uoc"),
                            (50, 40, "1.500 - bom them nua thi TE hon")]:
    print(f"  {q_jack:>5} {q_jill:>5} {q_jack + q_jill:>6}"
          f" {'$' + str(gia(q_jack + q_jill)):>6}"
          f" {tien(loi_nhuan_rieng(q_jack, q_jill)):>9}   {ghi}")
print("  " + DONG[:66])
print("  Bon con so sach in ra deu khop. Hai dong dau day Jack len 40 gallon;")
print("  dong cuoi giu chan anh ta lai o do. Do la dinh nghia cua can bang Nash.")


# ---------------------------------------------------------------------------
# MUC 4. So nguoi ban tang thi gia tien ve chi phi bien
# ---------------------------------------------------------------------------
tieu_de(4, "Them nguoi ban - gia truot ve chi phi bien")

# Voi n nha san xuat doi xung, MC = 0 va P = 120 - Q, moi ben bom
#     q* = 120 / (n + 1),   tong Q = 120n / (n + 1),   P = 120 / (n + 1).
# Day la nghiem Cournot. Chung minh: dao ham loi nhuan cua mot ben theo q
# bang 0 khi 120 - Q - q = 0; doi xung nen Q = n*q -> q = 120/(n+1).


def cournot(n):
    q_moi_ben = F(GIA_TRAN, n + 1)
    tong = q_moi_ben * n
    return q_moi_ben, tong, F(GIA_TRAN) - tong


print(f"{'So nguoi ban':>13} {'Moi ben bom':>14} {'Tong san luong':>17} {'Gia':>9} {'LN nganh':>10}")
print(DONG)
for n in [1, 2, 3, 4, 5, 10, 20, 50, 100]:
    q_i, tong, p = cournot(n)
    print(f"{n:>13} {str(q_i):>10} gal {str(tong):>13} gal"
          f" {'$' + str(p):>9} {tien(tong * p):>10}")
print(DONG)
print("n = 1 -> 60 gal, $60: dung ket cuc doc quyen o Bang 1.")
print("n = 2 -> 80 gal, $40: dung can bang Nash tim duoc o muc 3.")
print("n -> vo cung: gia -> $0 = chi phi bien, san luong -> 120 = muc hieu qua.")
print()

# Do thi ASCII: gia theo so nguoi ban
CAO, RONG = 13, 56
print("Gia can bang khi so nguoi ban tang (truc doc: $, truc ngang: n)")
print()
luoi = [[" "] * RONG for _ in range(CAO)]
for cot in range(RONG):
    n = 1 + cot * F(29, RONG - 1)          # n chay tu 1 toi 30
    p = F(GIA_TRAN) / (n + 1)
    hang = CAO - 1 - round(p * (CAO - 1) / 60)
    if 0 <= hang < CAO:
        luoi[hang][cot] = "*"
for hang in range(CAO):
    nhan = f"{round(60 - hang * 60 / (CAO - 1)):>3}"
    print(f"  ${nhan} |" + "".join(luoi[hang]))
print("       +" + "-" * RONG)
print("        1" + " " * (RONG // 2 - 3) + "15" + " " * (RONG // 2 - 4) + "30  nguoi ban")
print()
print("Duong tut rat nhanh o dau roi phang dan: hai nguoi ban dau lam gia sap")
print("mot nua, con them nguoi ban thu 30 gan nhu khong doi gi nua.")


# ---------------------------------------------------------------------------
# MUC 5. Bo giai tro choi 2x2 - dung chung cho ca bon hinh cua chuong
# ---------------------------------------------------------------------------
tieu_de(5, "Bo giai tro choi 2x2 - bon hinh cua chuong, cung mot bo may")


def giai_tro_choi(ten, nguon, ten_a, ten_b, hanh_dong, bang, cang_cao_cang_tot=True,
                  don_vi="", dinh_dang=str):
    """Tim chien luoc thong soai, can bang Nash va ket cuc tot nhat cho ca hai.

    bang[(a, b)] = (loi ich cua A, loi ich cua B) voi a, b thuoc hanh_dong.
    """
    def hon(x, y):
        return x > y if cang_cao_cang_tot else x < y

    print(f"{ten}   ({nguon})")
    print(DONG)
    # In ma tran. Cot dau rong 20, moi o rong 22.
    print((" " * 20 + "".join(f"| {ten_b}: {h}".ljust(22) for h in hanh_dong)).rstrip())
    for a in hanh_dong:
        o = [f"| {dinh_dang(bang[(a, b)][0])}{don_vi}"
             f" / {dinh_dang(bang[(a, b)][1])}{don_vi}".ljust(22) for b in hanh_dong]
        print((f"{ten_a}: {a}".ljust(20) + "".join(o)).rstrip())
    print()

    # Chien luoc thong soai: tot nhat BAT KE doi phuong lam gi
    thong_soai = {}
    for ai, (nguoi, lay) in enumerate([(ten_a, lambda a, b: bang[(a, b)][0]),
                                       (ten_b, lambda b, a: bang[(a, b)][1])]):
        ts = [x for x in hanh_dong
              if all(not hon(lay(y, k), lay(x, k)) for k in hanh_dong for y in hanh_dong)]
        thong_soai[nguoi] = ts
        nhan = ts[0] if len(ts) == 1 else "khong co"
        print(f"  Chien luoc thong soai cua {nguoi:<10}: {nhan}")

    # Can bang Nash
    diem = []
    for a in hanh_dong:
        for b in hanh_dong:
            a_on = not any(hon(bang[(x, b)][0], bang[(a, b)][0]) for x in hanh_dong)
            b_on = not any(hon(bang[(a, y)][1], bang[(a, b)][1]) for y in hanh_dong)
            if a_on and b_on:
                diem.append((a, b))
    print(f"  Can bang Nash                : {diem}")

    # Ket cuc tot nhat cho ca hai (tong loi ich)
    cong = max(bang, key=lambda k: (sum(bang[k]) if cang_cao_cang_tot else -sum(bang[k])))
    print(f"  Tot nhat cho ca hai cong lai : {cong} -> {bang[cong]}")
    la_lung_nan = diem == [cong]
    print(f"  Nash co phai ket cuc tot nhat khong? {'CO' if la_lung_nan else 'KHONG'}"
          f" -> {'khong phai' if la_lung_nan else 'DUNG la'} tien thoai luong nan")
    print()
    return diem, cong


# (a) Bonnie va Clyde - Hinh 1, tr. 398. Loi ich = so nam tu, CANG IT CANG TOT.
giai_tro_choi(
    "(a) Tinh the tien thoai luong nan cua nguoi tu", "Hinh 1, tr. 398",
    "Clyde", "Bonnie", ["thu toi", "im lang"],
    {("thu toi", "thu toi"): (8, 8), ("thu toi", "im lang"): (0, 20),
     ("im lang", "thu toi"): (20, 0), ("im lang", "im lang"): (1, 1)},
    cang_cao_cang_tot=False, don_vi=" nam")

# (b) Jack va Jill - Hinh 2, tr. 399. Loi ich = loi nhuan, CANG NHIEU CANG TOT.
giai_tro_choi(
    "(b) Tro choi doc quyen nhom cua Jack va Jill", "Hinh 2, tr. 399",
    "Jill", "Jack", ["40 gal", "30 gal"],
    {("40 gal", "40 gal"): (1600, 1600), ("40 gal", "30 gal"): (2000, 1500),
     ("30 gal", "40 gal"): (1500, 2000), ("30 gal", "30 gal"): (1800, 1800)},
    don_vi="$")

# (c) Exxon va Texaco - Hinh 4, tr. 402. Loi ich = trieu do la.
giai_tro_choi(
    "(c) Tro choi ve nguon tai nguyen chung", "Hinh 4, tr. 402",
    "Texaco", "Exxon", ["2 gieng", "1 gieng"],
    {("2 gieng", "2 gieng"): (4, 4), ("2 gieng", "1 gieng"): (6, 3),
     ("1 gieng", "2 gieng"): (3, 6), ("1 gieng", "1 gieng"): (5, 5)},
    don_vi=" tr")

# (d) Chien tranh thue quan - bai tap 4, tr. 414. Loi ich = ty do la.
giai_tro_choi(
    "(d) Chien tranh thue quan Hoa Ky - Mexico", "bai tap 4, tr. 414",
    "Mexico", "Hoa Ky", ["thue cao", "thue thap"],
    {("thue cao", "thue cao"): (20, 20), ("thue cao", "thue thap"): (30, 10),
     ("thue thap", "thue cao"): (10, 30), ("thue thap", "thue thap"): (25, 25)},
    don_vi=" ty")

print("Bon hoan canh khac nhau hoan toan - tu nha tu, gieng dau, thi truong nuoc")
print("toi hiep dinh thuong mai - deu ra CUNG MOT cau truc. Do la suc manh cua")
print("ly thuyet tro choi: no khong quan tam noi dung, chi quan tam hinh dang.")


# ---------------------------------------------------------------------------
# MUC 6. Tro choi lap - nguong chiet khau de hop tac ben vung
# ---------------------------------------------------------------------------
tieu_de(6, "Choi bao nhieu lan thi hop tac moi ben - nguong chiet khau")

HOP_TAC, BOI_UOC = 1800, 1600      # loi nhuan moi tuan neu ca hai cung mot phia
CAM_DO = 2000                      # loi nhuan tuan boi uoc dau tien
BI_LUA = 1500                      # loi nhuan tuan bi doi phuong boi uoc truoc

print("Sach viet o tr. 404: 'moi loi nay chi keo dai duoc mot tuan. Sau do,")
print("loi nhuan se giam xuong muc 1.600 do la va giu nguyen muc nay.'")
print("Bien cau do thanh mot bat dang thuc. Goi d la he so chiet khau moi tuan:")
print()
print("  giu hop tac mai mai :  1800 / (1 - d)")
print("  boi uoc mot lan roi bi trung phat mai mai :  2000 + d * 1600 / (1 - d)")
print()

# 1800/(1-d) >= 2000 + d*1600/(1-d)
#   <=> 1800 >= 2000*(1-d) + 1600*d  <=>  400*d >= 200  <=>  d >= 1/2
nguong = F(CAM_DO - HOP_TAC, CAM_DO - BOI_UOC)
print(f"Giai ra: d >= ({CAM_DO} - {HOP_TAC}) / ({CAM_DO} - {BOI_UOC}) = {nguong}"
      f" = {float(nguong):.4f}")
print()
print(f"{'He so chiet khau d':>19} {'Gia tri neu hop tac':>21} {'Gia tri neu boi uoc':>21} {'Hop tac ben?':>13}")
print(DONG)
for d in [F(1, 10), F(3, 10), F(1, 2), F(7, 10), F(9, 10), F(99, 100)]:
    v_hop_tac = F(HOP_TAC) / (1 - d)
    v_boi_uoc = CAM_DO + d * F(BOI_UOC) / (1 - d)
    print(f"{str(d):>19} {tien(round(v_hop_tac)):>21} {tien(round(v_boi_uoc)):>21}"
          f" {str(v_hop_tac >= v_boi_uoc):>13}")
print(DONG)
print(f"Nguong roi dung vao d = {nguong}: chinh la diem hai cot bang nhau.")
print()
print("Doc d nhu the nao: d gan 1 nghia la 'tuan sau van quan trong nhu tuan nay'")
print("- quan he lau dai, hai ben con gap nhau nhieu lan nua. d gan 0 nghia la")
print("'chi con lan nay' - hop dong sap het, doi tac sap pha san, sep sap nghi viec.")
print("Suy ra mot cau rat thuc te: HOP TAC SUP DO KHI TUONG LAI NGAN LAI.")


# ---------------------------------------------------------------------------
# MUC 7. Giai dau Axelrod thu nho
# ---------------------------------------------------------------------------
tieu_de(7, "Giai dau Axelrod thu nho - nam chien luoc, danh vong tron")

SO_TUAN = 10
BANG_LN = {("H", "H"): (HOP_TAC, HOP_TAC), ("H", "B"): (BI_LUA, CAM_DO),
           ("B", "H"): (CAM_DO, BI_LUA), ("B", "B"): (BOI_UOC, BOI_UOC)}
# "H" = hop tac (bom 30 gallon), "B" = boi uoc (bom 40 gallon)


def luon_hop_tac(lich_su_toi, lich_su_kia):
    return "H"


def luon_boi_uoc(lich_su_toi, lich_su_kia):
    return "B"


def an_mieng_tra_mieng(lich_su_toi, lich_su_kia):
    """Bat dau tu te, sau do lam y het nhung gi doi phuong vua lam."""
    return lich_su_kia[-1] if lich_su_kia else "H"


def trung_phat_vinh_vien(lich_su_toi, lich_su_kia):
    """Hop tac cho toi khi bi boi uoc mot lan, roi boi uoc mai mai."""
    return "B" if "B" in lich_su_kia else "H"


def an_mieng_do_luong(lich_su_toi, lich_su_kia):
    """Chi tra dua khi bi boi uoc HAI lan lien tiep - bo qua mot lan lo."""
    return "B" if lich_su_kia[-2:] == ["B", "B"] else "H"


CHIEN_LUOC = [
    ("Luon hop tac", luon_hop_tac),
    ("Luon boi uoc", luon_boi_uoc),
    ("An mieng tra mieng", an_mieng_tra_mieng),
    ("Trung phat vinh vien", trung_phat_vinh_vien),
    ("An mieng do luong", an_mieng_do_luong),
]


def dau(cl_a, cl_b, so_tuan=SO_TUAN, sai_sot_a=None):
    """Cho hai chien luoc danh nhau. sai_sot_a: tuan ma A lo tay boi uoc."""
    su_a, su_b, diem_a, diem_b = [], [], 0, 0
    for tuan in range(1, so_tuan + 1):
        a = cl_a(su_a, su_b)
        b = cl_b(su_b, su_a)
        if tuan == sai_sot_a:
            a = "B"                      # tay run, khong phai co y
        la, lb = BANG_LN[(a, b)]
        diem_a += la
        diem_b += lb
        su_a.append(a)
        su_b.append(b)
    return diem_a, diem_b


print(f"Moi cap danh {SO_TUAN} tuan, danh vong tron ke ca voi ban sao cua chinh minh.")
print("Diem = tong loi nhuan, cang cao cang tot.")
print()
print("Cot duoc danh so theo dung thu tu cua hang.")
print()
print(f"{'':<24}" + "".join(f"{'(' + str(i) + ')':>8}" for i in range(1, 6))
      + f"{'TONG':>9}")
print(DONG)
bang_diem = []
for i, (ten_a, cl_a) in enumerate(CHIEN_LUOC, 1):
    hang, tong = [], 0
    for ten_b, cl_b in CHIEN_LUOC:
        d, _ = dau(cl_a, cl_b)
        hang.append(d)
        tong += d
    bang_diem.append((ten_a, tong))
    print(f"{'(' + str(i) + ') ' + ten_a:<24}"
          + "".join(f"{tien(x):>8}" for x in hang) + f"{tien(tong):>9}")
print(DONG)
for hang, (ten, tong) in enumerate(sorted(bang_diem, key=lambda x: -x[1]), 1):
    print(f"  {hang}. {ten:<24} {tien(tong)}")
print()
print("Luu y: day KHONG phai ban sao giai dau cua Axelrod (ong co hang chuc")
print("chuong trinh du thi, con day chi co nam). No chi cho thay co che.")
print()
d_amtm, d_lbu = dau(an_mieng_tra_mieng, luon_boi_uoc)
print(f"Doc ky mot cap: an mieng tra mieng gap luon boi uoc -> {tien(d_amtm)}"
      f" so voi {tien(d_lbu)}.")
print("An mieng tra mieng THUA tran nay, va no khong THANG duoc doi thu nao ca -")
print("gap ai no cung chi hoa hoac thua. Nhung no khong bao gio bi vat kiet, nen")
print("tong diem van dan dau. Do dung la nhan xet cua Axelrod.")
print()
print("Luu y hai dieu ma bang tren noi that:")
print("  - An mieng tra mieng va trung phat vinh vien DONG HANG NHAT, khong hon")
print("    kem gi nhau. Trong mot the gioi khong co sai sot thi chung y het nhau.")
print("    Muc 8 se tach doi hai chien luoc nay ra.")
print("  - An mieng DO LUONG xep sau dung 100 do la, va toan bo khoang cach do")
print(f"    den tu tran gap luon boi uoc ({tien(dau(an_mieng_do_luong, luon_boi_uoc)[0])}"
      f" so voi {tien(d_amtm)}): ke boi uoc")
print("    duoc an khong hai tuan dau thay vi mot. Do luong co gia cua no.")


# ---------------------------------------------------------------------------
# MUC 8. Mot lan lo tay va cai gia cua trung phat vinh vien
# ---------------------------------------------------------------------------
tieu_de(8, "Mot lan lo tay - vi sao trung phat vinh vien la chien luoc te")

print("Sach nhan xet o tr. 404 rang chien luoc 'boi uoc mai mai ngay khi nguoi kia")
print("boi uoc' thi 'khong co tinh vi tha cho lam'. Dat con so vao nhan xet do:")
print("gia su o TUAN 5 Jack lo tay bom 40 gallon - khong co y, chi la nham.")
print()
TRON_VEN = HOP_TAC * SO_TUAN * 2
print(f"{'Ca hai cung dung chien luoc':<28} {'Jack':>10} {'Jill':>10} {'Tong':>10} {'Mat':>10}")
print(DONG)
for ten, cl in [("An mieng tra mieng", an_mieng_tra_mieng),
                ("Trung phat vinh vien", trung_phat_vinh_vien),
                ("An mieng do luong", an_mieng_do_luong)]:
    a, b = dau(cl, cl, sai_sot_a=5)
    print(f"{ten:<28} {tien(a):>10} {tien(b):>10} {tien(a + b):>10}"
          f" {tien(TRON_VEN - a - b):>10}")
print(f"{'(khong ai lo tay)':<28} {tien(TRON_VEN // 2):>10} {tien(TRON_VEN // 2):>10}"
      f" {tien(TRON_VEN):>10} {0:>10}")
print(DONG)
print("Trung phat vinh vien mat nhieu nhat: mot cai nham ngay tuan 5 keo ca hai")
print("xuong day trong nam tuan con lai. An mieng tra mieng do hon nhung roi vao")
print("vong tra dua so le - toi phat anh, anh phat toi, khong ai ve duoc.")
print("An mieng DO LUONG bo qua lan lo dau tien va gan nhu khong mat gi.")
print()
print("Bai hoc quan tri: dieu khoan phat trong hop dong nen co CUA QUAY LAI.")
print("Phat vinh vien nghe cung ran, nhung no bien mot sai sot thanh mot cuoc")
print("chien khong loi thoat.")


# ---------------------------------------------------------------------------
# MUC 9. Ban kem san pham - tr. 409
# ---------------------------------------------------------------------------
tieu_de(9, "Ban kem san pham - khi nao no lam ra tien, khi nao khong")


def doanh_thu_rieng(khach, gia_1, gia_2):
    """Ban rieng tung phim: khach mua phim nao co gia khong vuot muc san long tra."""
    t = 0
    for wtp_1, wtp_2 in khach:
        t += gia_1 if wtp_1 >= gia_1 else 0
        t += gia_2 if wtp_2 >= gia_2 else 0
    return t


def doanh_thu_goi(khach, gia_goi):
    """Ban ca goi: khach mua neu tong muc san long tra >= gia goi."""
    return sum(gia_goi for w1, w2 in khach if w1 + w2 >= gia_goi)


def toi_uu(khach, moc):
    """Quet moi to hop gia trong tap moc, tra ve phuong an tot nhat moi kieu."""
    rieng = max(((doanh_thu_rieng(khach, g1, g2), g1, g2) for g1 in moc for g2 in moc))
    goi = max(((doanh_thu_goi(khach, g), g) for g in moc))
    return rieng, goi


for nhan, khach, ghi_chu in [
    ("Truong hop sach bac bo (tr. 409, doan 3)",
     [(20000, 0), (20000, 0)],
     "ca hai rap deu tra 20.000 cho Ironman va 0 cho Hamlet"),
    ("Truong hop sach ung ho (tr. 409, doan 5)",
     [(15000, 5000), (5000, 15000)],
     "City thich Ironman, Country thich Hamlet - so thich NGUOC nhau"),
]:
    moc = sorted({w for k in khach for w in k} | {sum(k) for k in khach} | {0})
    (dt_rieng, g1, g2), (dt_goi, g_goi) = toi_uu(khach, moc)
    print(nhan)
    print(f"  {ghi_chu}")
    ban_1 = sum(1 for w1, _ in khach if w1 >= g1)
    ban_2 = sum(1 for _, w2 in khach if w2 >= g2)
    ban_goi = sum(1 for w1, w2 in khach if w1 + w2 >= g_goi)
    print(f"  Ban rieng tot nhat : {'Ironman $' + tien(g1) + ' (' + str(ban_1) + ' rap mua)':<32}"
          f" -> doanh thu {tien(dt_rieng):>7}")
    print(f"  {'':<19}  {'Hamlet  $' + tien(g2) + ' (' + str(ban_2) + ' rap mua)'}")
    print(f"  Ban theo goi       : {'ca goi  $' + tien(g_goi) + ' (' + str(ban_goi) + ' rap mua)':<32}"
          f" -> doanh thu {tien(dt_goi):>7}")
    chenh = dt_goi - dt_rieng
    if chenh > 0:
        print(f"  -> Goi hon {tien(chenh)} (+{chenh * 100 // dt_rieng}%)")
    else:
        print(f"  -> Goi KHONG hon gi ({tien(chenh)})")
    print()

print("Ket luan cua sach, dat thanh mot cau kiem tra duoc:")
print("ban kem chi lam ra tien khi cac khach hang XEP HANG cac san pham")
print("theo thu tu NGUOC nhau. Neu ai cung thich cung mot mon, goi vo dung.")


# ---------------------------------------------------------------------------
# MUC 10. Cartel kim cuong - bai tap 2, tr. 413
# ---------------------------------------------------------------------------
tieu_de(10, "Cartel kim cuong Nga - Nam Phi (bai tap 2, tr. 413)")

MC_KIM_CUONG = 1000
CAU_KIM_CUONG = [(8000, 5000), (7000, 6000), (6000, 7000), (5000, 8000),
                 (4000, 9000), (3000, 10000), (2000, 11000), (1000, 12000)]

print(f"{'Gia':>8} {'San luong':>11} {'Doanh thu':>14} {'Chi phi':>14} {'Loi nhuan':>14}")
print(DONG)
tot_nhat = None
for p, q in CAU_KIM_CUONG:
    ln = q * (p - MC_KIM_CUONG)
    print(f"{'$' + tien(p):>8} {tien(q):>11} {tien(p * q):>14}"
          f" {tien(q * MC_KIM_CUONG):>14} {tien(ln):>14}")
    if tot_nhat is None or ln > tot_nhat[2]:
        tot_nhat = (p, q, ln)
print(DONG)
p_cartel, q_cartel, ln_cartel = tot_nhat
print(f"(a) Nhieu nha cung cap : gia = MC = ${tien(MC_KIM_CUONG)},"
      f" {tien(12000)} vien, loi nhuan 0")
print(f"(b) Mot nha cung cap   : gia ${tien(p_cartel)},"
      f" {tien(q_cartel)} vien, loi nhuan {tien(ln_cartel)}")
print(f"(c) Cartel chia doi    : moi nuoc {tien(q_cartel // 2)} vien,"
      f" moi ben lai {tien(ln_cartel // 2)}")
print()

# Nam Phi gian lan: bom them 1.000 vien, Nga giu nguyen 3.000
q_gian = q_cartel // 2 + 1000
q_tong_gian = q_gian + q_cartel // 2
p_gian = dict((q, p) for p, q in CAU_KIM_CUONG)[q_tong_gian]
ln_nam_phi = q_gian * (p_gian - MC_KIM_CUONG)
ln_nga = (q_cartel // 2) * (p_gian - MC_KIM_CUONG)
print(f"    Nam Phi tang len {tien(q_gian)} vien, Nga van giu {tien(q_cartel // 2)}:")
print(f"      tong {tien(q_tong_gian)} vien -> gia tut xuong ${tien(p_gian)}")
print(f"      Nam Phi : {tien(ln_nam_phi)}  ({'+' if ln_nam_phi > ln_cartel // 2 else ''}"
      f"{tien(ln_nam_phi - ln_cartel // 2)} so voi giu cam ket)")
print(f"      Nga     : {tien(ln_nga)}  ({tien(ln_nga - ln_cartel // 2)})")
print(f"      Ca hai  : {tien(ln_nam_phi + ln_nga)}  ({tien(ln_nam_phi + ln_nga - ln_cartel)})")
print()
print("(d) Do la toan bo cau tra loi cho cau hoi 'tai sao cartel hay do vo':")
print(f"    ke gian lan duoc them {tien(ln_nam_phi - ln_cartel // 2)},")
print(f"    con nganh mat {tien(ln_cartel - ln_nam_phi - ln_nga)}. Loi ich rieng va")
print("    loi ich chung keo ve hai huong nguoc nhau - dung cau truc muc 5.")


# ---------------------------------------------------------------------------
# MUC 11. [QTKD] Cuoc chien giam gia co dung la tien thoai luong nan khong
# ---------------------------------------------------------------------------
tieu_de(11, "[QTKD] Cuoc chien giam gia - kiem tra chu khong gia dinh")

# Hai chuoi ban le doi dau. Don vi tien: nghin dong.
GIA_THUONG = 100                   # gia niem yet
GIA_HA = 90                        # gia sau khi giam 10%
CHI_PHI = 60                       # chi phi bien mot don vi
HE_SO_CAU = 10                     # thi truong no ra bao nhieu khi gia binh quan giam 1
CAU_GOC = 2000                     # Q = CAU_GOC - HE_SO_CAU * gia binh quan
NHAY_THI_PHAN = F(1, 50)           # chenh 1 nghin dong -> thi phan doi bao nhieu


def ket_cuc(gia_a, gia_b):
    """Tra ve (loi nhuan A, loi nhuan B) khi hai ben dat hai muc gia."""
    binh_quan = F(gia_a + gia_b, 2)
    tong_cau = CAU_GOC - HE_SO_CAU * binh_quan
    thi_phan_a = F(1, 2) + NHAY_THI_PHAN * (gia_b - gia_a)
    q_a = tong_cau * thi_phan_a
    q_b = tong_cau - q_a
    return q_a * (gia_a - CHI_PHI), q_b * (gia_b - CHI_PHI)


print("Mo hinh (khong co trong sach - dung de kiem tra xem cau truc muc 5 co that")
print("su xuat hien tu con so kinh doanh, hay chi la mot gia dinh dep):")
print(f"  Tong cau     Q = {CAU_GOC} - {HE_SO_CAU} x (gia binh quan hai ben)")
print(f"  Thi phan cua A = 1/2 + 1/{int(1 / NHAY_THI_PHAN)} x (gia cua B - gia cua A)")
print(f"  Chi phi bien   = {CHI_PHI} nghin dong / don vi")
print()
print(f"{'Gia cua A':>10} {'Gia cua B':>10} {'Q ban ra':>10} {'A ban':>8} {'B ban':>8}"
      f" {'LN cua A':>11} {'LN cua B':>11}")
print(DONG)
bang_gia = {}
for ga in (GIA_HA, GIA_THUONG):
    for gb in (GIA_HA, GIA_THUONG):
        la, lb = ket_cuc(ga, gb)
        bang_gia[(ga, gb)] = (int(la), int(lb))
        bq = F(ga + gb, 2)
        tong = CAU_GOC - HE_SO_CAU * bq
        qa = tong * (F(1, 2) + NHAY_THI_PHAN * (gb - ga))
        print(f"{ga:>10} {gb:>10} {str(tong):>10} {str(qa):>8} {str(tong - qa):>8}"
              f" {tien(la):>11} {tien(lb):>11}")
print(DONG)
print()

giai_tro_choi(
    "Cuoc chien giam gia, dung so vua tinh o tren", "mo hinh QTKD",
    "B", "A", [f"gia {GIA_HA}", f"gia {GIA_THUONG}"],
    {(f"gia {a}", f"gia {b}"): bang_gia[(a, b)]
     for a in (GIA_HA, GIA_THUONG) for b in (GIA_HA, GIA_THUONG)},
    don_vi="k", dinh_dang=tien)

thiet_hai = bang_gia[(GIA_THUONG, GIA_THUONG)][0] - bang_gia[(GIA_HA, GIA_HA)][0]
print(f"Ca hai cung giam gia thi moi ben mat {tien(thiet_hai)} nghin dong so voi")
print("khong ai giam - va van khong ai gianh duoc them thi phan nao, vi doi thu")
print("da giam theo. Nhung 'giam gia' van la chien luoc thong soai.")
print()
print("Ba cach thoat, doc thang tu cac muc tren:")
print(f"  1. Keo dai tuong lai (muc 6): quan he cang lau, d cang gan 1,")
print(f"     hop tac cang de giu. Hop dong nhieu nam thay vi tung don hang.")
print("  2. Bo qua mot lan lo (muc 8): dung tuyen bo 'giam mot lan la chien tranh")
print("     vinh vien' - mot dot khuyen mai le se keo ca nganh xuong day.")
print("  3. Lam cau bot co gian (bai 3, bai 8): neu khach khong so sanh duoc hai")
print("     ben nua thi he so nhay thi phan tut xuong, va cam do giam gia bien mat.")
print()
print("Chu y: (1) va (2) la quan tri quan he ban hang. (3) la khac biet hoa san")
print("pham. Cai thu ba KHONG can doi thu dong y dieu gi - do la ly do no ben hon.")
print()
print("Va mot ranh gioi phap ly khong duoc buoc qua (tr. 406-407): tu minh chon")
print("khong giam gia la hop phap; GOI DIEN cho doi thu de cung thoa thuan khong")
print("giam gia la pham phap. Crandall cua American Airlines bi khoi to chi vi mot")
print("cuoc dien thoai nhu vay nam 1983.")
```

**Kết quả chạy thật:**

```

==========================================================================
MUC 1. Bang 1 tr. 392 - bieu cau nuoc sinh hoat
==========================================================================
Mo hinh dung lai:  P = 120 - Q,  chi phi bien = 0

 San luong      Gia    Doanh thu    Sach in   Khop
--------------------------------------------------------------------------
      0 gal     $120            0          0   True
     10 gal     $110        1.100      1.100   True
     20 gal     $100        2.000      2.000   True
     30 gal      $90        2.700      2.700   True
     40 gal      $80        3.200      3.200   True
     50 gal      $70        3.500      3.500   True
     60 gal      $60        3.600      3.600   True
     70 gal      $50        3.500      3.500   True
     80 gal      $40        3.200      3.200   True
     90 gal      $30        2.700      2.700   True
    100 gal      $20        2.000      2.000   True
    110 gal      $10        1.100      1.100   True
    120 gal       $0            0          0   True
--------------------------------------------------------------------------
Khop 13/13 dong.

==========================================================================
MUC 2. Ba ket cuc cua cung mot thi truong
==========================================================================
Ket cuc                       San luong     Gia   LN nganh   Moi ben
--------------------------------------------------------------------------
Canh tranh hoan hao             120 gal      $0          0         -
Doc quyen (hoac cartel)          60 gal     $60      3.600     1.800
Nhi quyen - can bang Nash        80 gal     $40      3.200     1.600
--------------------------------------------------------------------------
Nhi quyen nam GIUA hai thai cuc: san luong 80 > 60 nhung < 120;
gia $40 < $60 nhung > $0. Dung nhu ket luan in nghieng tr. 395.

==========================================================================
MUC 3. Tim can bang Nash bang vet can - khong doan, chi thu het
==========================================================================
Bang phan ung tot nhat (Jack chon gi khi biet Jill chon gi), luoi 10 gallon:

  Jill bom   Jack nen bom                                    LN Jack
--------------------------------------------------------------------------
     0 gal   60 gal                                            3.600
    10 gal   50, 60 gal                                        3.000
    20 gal   50 gal                                            2.500
    30 gal   40, 50 gal                                        2.000
    40 gal   40 gal                                            1.600
    50 gal   30, 40 gal                                        1.200
    60 gal   30 gal                                              900
    70 gal   20, 30 gal                                          600
    80 gal   20 gal                                              400
    90 gal   10, 20 gal                                          200
   100 gal   10 gal                                              100
   110 gal   moi muc deu nhu nhau (gia da bang 0)                  0
   120 gal   moi muc deu nhu nhau (gia da bang 0)                  0
--------------------------------------------------------------------------
Can bang Nash tim duoc  : [(30, 50), (40, 40), (50, 30)]
Va them 4 diem SUY BIEN quanh (110-120, 110-120): o do tong san
luong da vuot 120 nen gia bang 0 va ai bom bao nhieu cung lai 0 - moi lua
chon deu 'toi uu' mot cach vo nghia. Loai chung bang dieu kien loi nhuan > 0.

Nhung ngay ca sau khi loai, van con BA diem chu khong phai mot. Vi sao?
Vi tren luoi 10 gallon cua sach, khi doi phuong bom 30 thi bom 40 va bom 50
lai y het nhau (2.000 do la ca hai) - mot the hoa do lam tron.
That mo luoi ra thi cum nay co lai:

  Buoc luoi   So diem can bang   Can bang Nash that su
--------------------------------------------------------------------------
     10 gal                  3   [(30, 50), (40, 40), (50, 30)]
      5 gal                  3   [(35, 45), (40, 40), (45, 35)]
      2 gal                  3   [(38, 42), (40, 40), (42, 38)]
      1 gal                  3   [(39, 41), (40, 40), (41, 39)]
--------------------------------------------------------------------------
Cum luon la {(40-h, 40+h), (40, 40), (40+h, 40-h)} voi h dung bang buoc luoi.
Luoi cang min, cum cang co ve (40, 40) - can bang Nash that su cua tro choi.
Sach chi noi ket qua (40, 40) o tr. 394-395; day la cho chung minh no.

Doi chieu tung con so trong hai doan lap luan cua Jack, tr. 394:

   Jack  Jill   Tong    Gia   LN Jack   Sach viet gi
  ------------------------------------------------------------------
     30    30     60    $60     1.800   1.800 - giu thoa thuan
     40    30     70    $50     2.000   2.000 - boi uoc, co loi hon
     40    40     80    $40     1.600   1.600 - ca hai cung boi uoc
     50    40     90    $30     1.500   1.500 - bom them nua thi TE hon
  ------------------------------------------------------------------
  Bon con so sach in ra deu khop. Hai dong dau day Jack len 40 gallon;
  dong cuoi giu chan anh ta lai o do. Do la dinh nghia cua can bang Nash.

==========================================================================
MUC 4. Them nguoi ban - gia truot ve chi phi bien
==========================================================================
 So nguoi ban    Moi ben bom    Tong san luong       Gia   LN nganh
--------------------------------------------------------------------------
            1         60 gal            60 gal       $60      3.600
            2         40 gal            80 gal       $40      3.200
            3         30 gal            90 gal       $30      2.700
            4         24 gal            96 gal       $24      2.304
            5         20 gal           100 gal       $20      2.000
           10     120/11 gal       1200/11 gal   $120/11      1.190
           20       40/7 gal         800/7 gal     $40/7        653
           50      40/17 gal       2000/17 gal    $40/17        276
          100    120/101 gal     12000/101 gal  $120/101        141
--------------------------------------------------------------------------
n = 1 -> 60 gal, $60: dung ket cuc doc quyen o Bang 1.
n = 2 -> 80 gal, $40: dung can bang Nash tim duoc o muc 3.
n -> vo cung: gia -> $0 = chi phi bien, san luong -> 120 = muc hieu qua.

Gia can bang khi so nguoi ban tang (truc doc: $, truc ngang: n)

  $ 60 |*                                                       
  $ 55 |                                                        
  $ 50 |                                                        
  $ 45 | *                                                      
  $ 40 |  *                                                     
  $ 35 |   *                                                    
  $ 30 |    *                                                   
  $ 25 |     **                                                 
  $ 20 |       ***                                              
  $ 15 |          *****                                         
  $ 10 |               ************                             
  $  5 |                           *****************************
  $  0 |                                                        
       +--------------------------------------------------------
        1                         15                        30  nguoi ban

Duong tut rat nhanh o dau roi phang dan: hai nguoi ban dau lam gia sap
mot nua, con them nguoi ban thu 30 gan nhu khong doi gi nua.

==========================================================================
MUC 5. Bo giai tro choi 2x2 - bon hinh cua chuong, cung mot bo may
==========================================================================
(a) Tinh the tien thoai luong nan cua nguoi tu   (Hinh 1, tr. 398)
--------------------------------------------------------------------------
                    | Bonnie: thu toi     | Bonnie: im lang
Clyde: thu toi      | 8 nam / 8 nam       | 0 nam / 20 nam
Clyde: im lang      | 20 nam / 0 nam      | 1 nam / 1 nam

  Chien luoc thong soai cua Clyde     : thu toi
  Chien luoc thong soai cua Bonnie    : thu toi
  Can bang Nash                : [('thu toi', 'thu toi')]
  Tot nhat cho ca hai cong lai : ('im lang', 'im lang') -> (1, 1)
  Nash co phai ket cuc tot nhat khong? KHONG -> DUNG la tien thoai luong nan

(b) Tro choi doc quyen nhom cua Jack va Jill   (Hinh 2, tr. 399)
--------------------------------------------------------------------------
                    | Jack: 40 gal        | Jack: 30 gal
Jill: 40 gal        | 1600$ / 1600$       | 2000$ / 1500$
Jill: 30 gal        | 1500$ / 2000$       | 1800$ / 1800$

  Chien luoc thong soai cua Jill      : 40 gal
  Chien luoc thong soai cua Jack      : 40 gal
  Can bang Nash                : [('40 gal', '40 gal')]
  Tot nhat cho ca hai cong lai : ('30 gal', '30 gal') -> (1800, 1800)
  Nash co phai ket cuc tot nhat khong? KHONG -> DUNG la tien thoai luong nan

(c) Tro choi ve nguon tai nguyen chung   (Hinh 4, tr. 402)
--------------------------------------------------------------------------
                    | Exxon: 2 gieng      | Exxon: 1 gieng
Texaco: 2 gieng     | 4 tr / 4 tr         | 6 tr / 3 tr
Texaco: 1 gieng     | 3 tr / 6 tr         | 5 tr / 5 tr

  Chien luoc thong soai cua Texaco    : 2 gieng
  Chien luoc thong soai cua Exxon     : 2 gieng
  Can bang Nash                : [('2 gieng', '2 gieng')]
  Tot nhat cho ca hai cong lai : ('1 gieng', '1 gieng') -> (5, 5)
  Nash co phai ket cuc tot nhat khong? KHONG -> DUNG la tien thoai luong nan

(d) Chien tranh thue quan Hoa Ky - Mexico   (bai tap 4, tr. 414)
--------------------------------------------------------------------------
                    | Hoa Ky: thue cao    | Hoa Ky: thue thap
Mexico: thue cao    | 20 ty / 20 ty       | 30 ty / 10 ty
Mexico: thue thap   | 10 ty / 30 ty       | 25 ty / 25 ty

  Chien luoc thong soai cua Mexico    : thue cao
  Chien luoc thong soai cua Hoa Ky    : thue cao
  Can bang Nash                : [('thue cao', 'thue cao')]
  Tot nhat cho ca hai cong lai : ('thue thap', 'thue thap') -> (25, 25)
  Nash co phai ket cuc tot nhat khong? KHONG -> DUNG la tien thoai luong nan

Bon hoan canh khac nhau hoan toan - tu nha tu, gieng dau, thi truong nuoc
toi hiep dinh thuong mai - deu ra CUNG MOT cau truc. Do la suc manh cua
ly thuyet tro choi: no khong quan tam noi dung, chi quan tam hinh dang.

==========================================================================
MUC 6. Choi bao nhieu lan thi hop tac moi ben - nguong chiet khau
==========================================================================
Sach viet o tr. 404: 'moi loi nay chi keo dai duoc mot tuan. Sau do,
loi nhuan se giam xuong muc 1.600 do la va giu nguyen muc nay.'
Bien cau do thanh mot bat dang thuc. Goi d la he so chiet khau moi tuan:

  giu hop tac mai mai :  1800 / (1 - d)
  boi uoc mot lan roi bi trung phat mai mai :  2000 + d * 1600 / (1 - d)

Giai ra: d >= (2000 - 1800) / (2000 - 1600) = 1/2 = 0.5000

 He so chiet khau d   Gia tri neu hop tac   Gia tri neu boi uoc  Hop tac ben?
--------------------------------------------------------------------------
               1/10                 2.000                 2.178         False
               3/10                 2.571                 2.686         False
                1/2                 3.600                 3.600          True
               7/10                 6.000                 5.733          True
               9/10                18.000                16.400          True
             99/100               180.000               160.400          True
--------------------------------------------------------------------------
Nguong roi dung vao d = 1/2: chinh la diem hai cot bang nhau.

Doc d nhu the nao: d gan 1 nghia la 'tuan sau van quan trong nhu tuan nay'
- quan he lau dai, hai ben con gap nhau nhieu lan nua. d gan 0 nghia la
'chi con lan nay' - hop dong sap het, doi tac sap pha san, sep sap nghi viec.
Suy ra mot cau rat thuc te: HOP TAC SUP DO KHI TUONG LAI NGAN LAI.

==========================================================================
MUC 7. Giai dau Axelrod thu nho - nam chien luoc, danh vong tron
==========================================================================
Moi cap danh 10 tuan, danh vong tron ke ca voi ban sao cua chinh minh.
Diem = tong loi nhuan, cang cao cang tot.

Cot duoc danh so theo dung thu tu cua hang.

                             (1)     (2)     (3)     (4)     (5)     TONG
--------------------------------------------------------------------------
(1) Luon hop tac          18.000  15.000  18.000  18.000  18.000   87.000
(2) Luon boi uoc          20.000  16.000  16.400  16.400  16.800   85.600
(3) An mieng tra mieng    18.000  15.900  18.000  18.000  18.000   87.900
(4) Trung phat vinh vien  18.000  15.900  18.000  18.000  18.000   87.900
(5) An mieng do luong     18.000  15.800  18.000  18.000  18.000   87.800
--------------------------------------------------------------------------
  1. An mieng tra mieng       87.900
  2. Trung phat vinh vien     87.900
  3. An mieng do luong        87.800
  4. Luon hop tac             87.000
  5. Luon boi uoc             85.600

Luu y: day KHONG phai ban sao giai dau cua Axelrod (ong co hang chuc
chuong trinh du thi, con day chi co nam). No chi cho thay co che.

Doc ky mot cap: an mieng tra mieng gap luon boi uoc -> 15.900 so voi 16.400.
An mieng tra mieng THUA tran nay, va no khong THANG duoc doi thu nao ca -
gap ai no cung chi hoa hoac thua. Nhung no khong bao gio bi vat kiet, nen
tong diem van dan dau. Do dung la nhan xet cua Axelrod.

Luu y hai dieu ma bang tren noi that:
  - An mieng tra mieng va trung phat vinh vien DONG HANG NHAT, khong hon
    kem gi nhau. Trong mot the gioi khong co sai sot thi chung y het nhau.
    Muc 8 se tach doi hai chien luoc nay ra.
  - An mieng DO LUONG xep sau dung 100 do la, va toan bo khoang cach do
    den tu tran gap luon boi uoc (15.800 so voi 15.900): ke boi uoc
    duoc an khong hai tuan dau thay vi mot. Do luong co gia cua no.

==========================================================================
MUC 8. Mot lan lo tay - vi sao trung phat vinh vien la chien luoc te
==========================================================================
Sach nhan xet o tr. 404 rang chien luoc 'boi uoc mai mai ngay khi nguoi kia
boi uoc' thi 'khong co tinh vi tha cho lam'. Dat con so vao nhan xet do:
gia su o TUAN 5 Jack lo tay bom 40 gallon - khong co y, chi la nham.

Ca hai cung dung chien luoc        Jack       Jill       Tong        Mat
--------------------------------------------------------------------------
An mieng tra mieng               17.700     17.700     35.400        600
Trung phat vinh vien             17.100     17.100     34.200      1.800
An mieng do luong                18.200     17.700     35.900        100
(khong ai lo tay)                18.000     18.000     36.000          0
--------------------------------------------------------------------------
Trung phat vinh vien mat nhieu nhat: mot cai nham ngay tuan 5 keo ca hai
xuong day trong nam tuan con lai. An mieng tra mieng do hon nhung roi vao
vong tra dua so le - toi phat anh, anh phat toi, khong ai ve duoc.
An mieng DO LUONG bo qua lan lo dau tien va gan nhu khong mat gi.

Bai hoc quan tri: dieu khoan phat trong hop dong nen co CUA QUAY LAI.
Phat vinh vien nghe cung ran, nhung no bien mot sai sot thanh mot cuoc
chien khong loi thoat.

==========================================================================
MUC 9. Ban kem san pham - khi nao no lam ra tien, khi nao khong
==========================================================================
Truong hop sach bac bo (tr. 409, doan 3)
  ca hai rap deu tra 20.000 cho Ironman va 0 cho Hamlet
  Ban rieng tot nhat : Ironman $20.000 (2 rap mua)      -> doanh thu  40.000
                       Hamlet  $20.000 (0 rap mua)
  Ban theo goi       : ca goi  $20.000 (2 rap mua)      -> doanh thu  40.000
  -> Goi KHONG hon gi (0)

Truong hop sach ung ho (tr. 409, doan 5)
  City thich Ironman, Country thich Hamlet - so thich NGUOC nhau
  Ban rieng tot nhat : Ironman $15.000 (1 rap mua)      -> doanh thu  30.000
                       Hamlet  $15.000 (1 rap mua)
  Ban theo goi       : ca goi  $20.000 (2 rap mua)      -> doanh thu  40.000
  -> Goi hon 10.000 (+33%)

Ket luan cua sach, dat thanh mot cau kiem tra duoc:
ban kem chi lam ra tien khi cac khach hang XEP HANG cac san pham
theo thu tu NGUOC nhau. Neu ai cung thich cung mot mon, goi vo dung.

==========================================================================
MUC 10. Cartel kim cuong Nga - Nam Phi (bai tap 2, tr. 413)
==========================================================================
     Gia   San luong      Doanh thu        Chi phi      Loi nhuan
--------------------------------------------------------------------------
  $8.000       5.000     40.000.000      5.000.000     35.000.000
  $7.000       6.000     42.000.000      6.000.000     36.000.000
  $6.000       7.000     42.000.000      7.000.000     35.000.000
  $5.000       8.000     40.000.000      8.000.000     32.000.000
  $4.000       9.000     36.000.000      9.000.000     27.000.000
  $3.000      10.000     30.000.000     10.000.000     20.000.000
  $2.000      11.000     22.000.000     11.000.000     11.000.000
  $1.000      12.000     12.000.000     12.000.000              0
--------------------------------------------------------------------------
(a) Nhieu nha cung cap : gia = MC = $1.000, 12.000 vien, loi nhuan 0
(b) Mot nha cung cap   : gia $7.000, 6.000 vien, loi nhuan 36.000.000
(c) Cartel chia doi    : moi nuoc 3.000 vien, moi ben lai 18.000.000

    Nam Phi tang len 4.000 vien, Nga van giu 3.000:
      tong 7.000 vien -> gia tut xuong $6.000
      Nam Phi : 20.000.000  (+2.000.000 so voi giu cam ket)
      Nga     : 15.000.000  (-3.000.000)
      Ca hai  : 35.000.000  (-1.000.000)

(d) Do la toan bo cau tra loi cho cau hoi 'tai sao cartel hay do vo':
    ke gian lan duoc them 2.000.000,
    con nganh mat 1.000.000. Loi ich rieng va
    loi ich chung keo ve hai huong nguoc nhau - dung cau truc muc 5.

==========================================================================
MUC 11. [QTKD] Cuoc chien giam gia - kiem tra chu khong gia dinh
==========================================================================
Mo hinh (khong co trong sach - dung de kiem tra xem cau truc muc 5 co that
su xuat hien tu con so kinh doanh, hay chi la mot gia dinh dep):
  Tong cau     Q = 2000 - 10 x (gia binh quan hai ben)
  Thi phan cua A = 1/2 + 1/50 x (gia cua B - gia cua A)
  Chi phi bien   = 60 nghin dong / don vi

 Gia cua A  Gia cua B   Q ban ra    A ban    B ban    LN cua A    LN cua B
--------------------------------------------------------------------------
        90         90       1100      550      550      16.500      16.500
        90        100       1050      735      315      22.050      12.600
       100         90       1050      315      735      12.600      22.050
       100        100       1000      500      500      20.000      20.000
--------------------------------------------------------------------------

Cuoc chien giam gia, dung so vua tinh o tren   (mo hinh QTKD)
--------------------------------------------------------------------------
                    | A: gia 90           | A: gia 100
B: gia 90           | 16.500k / 16.500k   | 22.050k / 12.600k
B: gia 100          | 12.600k / 22.050k   | 20.000k / 20.000k

  Chien luoc thong soai cua B         : gia 90
  Chien luoc thong soai cua A         : gia 90
  Can bang Nash                : [('gia 90', 'gia 90')]
  Tot nhat cho ca hai cong lai : ('gia 100', 'gia 100') -> (20000, 20000)
  Nash co phai ket cuc tot nhat khong? KHONG -> DUNG la tien thoai luong nan

Ca hai cung giam gia thi moi ben mat 3.500 nghin dong so voi
khong ai giam - va van khong ai gianh duoc them thi phan nao, vi doi thu
da giam theo. Nhung 'giam gia' van la chien luoc thong soai.

Ba cach thoat, doc thang tu cac muc tren:
  1. Keo dai tuong lai (muc 6): quan he cang lau, d cang gan 1,
     hop tac cang de giu. Hop dong nhieu nam thay vi tung don hang.
  2. Bo qua mot lan lo (muc 8): dung tuyen bo 'giam mot lan la chien tranh
     vinh vien' - mot dot khuyen mai le se keo ca nganh xuong day.
  3. Lam cau bot co gian (bai 3, bai 8): neu khach khong so sanh duoc hai
     ben nua thi he so nhay thi phan tut xuong, va cam do giam gia bien mat.

Chu y: (1) va (2) la quan tri quan he ban hang. (3) la khac biet hoa san
pham. Cai thu ba KHONG can doi thu dong y dieu gi - do la ly do no ben hon.

Va mot ranh gioi phap ly khong duoc buoc qua (tr. 406-407): tu minh chon
khong giam gia la hop phap; GOI DIEN cho doi thu de cung thoa thuan khong
giam gia la pham phap. Crandall cua American Airlines bi khoi to chi vi mot
cuoc dien thoai nhu vay nam 1983.
```

---

## 19. Tự thử

Mở [thuc_hanh/bai-09-doc-quyen-nhom.py](../thuc_hanh/bai-09-doc-quyen-nhom.py), sửa rồi chạy lại.
Không có lời giải kèm — chỗ học nằm ở việc đoán trước rồi xem mình đoán sai ở đâu.

1. **Đổi chi phí biên từ 0 sang một số dương.** Sửa `gia(q)` thành `max(GIA_TRAN - q, 0)` giữ nguyên
   nhưng thêm chi phí `MC = 20` vào `loi_nhuan_rieng`. Cân bằng Nash dịch về đâu? Nó có còn nằm đúng
   giữa độc quyền và cạnh tranh không? *(Gợi ý: công thức Cournot ở mục 6 vẫn dùng được, chỉ cần thay
   $a$ bằng $a - MC$.)*

2. **Đổi ô ăn không của trò chơi nhị quyền.** Trong `BANG_LN`, đổi `CAM_DO` từ 2000 xuống **1850**.
   Ngưỡng $d$ ở mục 12 thành bao nhiêu? Hợp tác dễ hơn hay khó hơn? Giờ thử đổi `BOI_UOC` từ 1600
   xuống **1000** và giải thích vì sao ngưỡng lại đi theo hướng đó.

3. **Thêm một chiến lược vào giải đấu.** Viết `luon_boi_uoc_tu_tuan_8` — hợp tác bảy tuần đầu rồi bội
   ước ba tuần cuối. Nó xếp hạng mấy? Bây giờ tăng `SO_TUAN` lên 50 và chạy lại — thứ hạng của nó đổi
   thế nào, và vì sao?

4. **Đổi tuần lỡ tay ở mục 8.** Đặt `sai_sot_a=1` (lỡ ngay tuần đầu) rồi `sai_sot_a=10` (lỡ tuần cuối).
   Chiến lược nào nhạy cảm nhất với **thời điểm** xảy ra sai sót?

5. **Phá vỡ điều kiện bán kèm.** Ở mục 9, đổi rạp Country thành `(15000, 5000)` — tức là cả hai rạp
   giờ thích cùng một phim. Gói còn hơn bán riêng không? Rồi đổi thành `(10000, 10000)` và giải thích
   kết quả.

6. **Cartel kim cương ba nước.** Ở mục 10, cho thêm Botswana vào cartel, chia đều 6.000 viên thành ba
   phần 2.000. Nếu **hai** nước cùng gian lận thêm 1.000 viên mỗi nước thì sao? So sánh với trường hợp
   một nước gian lận — cartel càng đông thì càng dễ hay càng khó giữ?

7. **💼 Chỉnh mô hình chiến giá.** Ở mục 11, đổi `NHAY_THI_PHAN` từ `1/50` xuống `1/500` — tức là khách
   gần như không chuyển sang bên rẻ hơn. Cấu trúc tiến thoái lưỡng nan có còn không? Tìm giá trị
   `NHAY_THI_PHAN` mà tại đó "giảm giá" **thôi** không còn là chiến lược thống soái. Con số đó nói gì
   về giá trị của thương hiệu?

---

## 20. Từ điển thuật ngữ

| Tiếng Việt                                 | Tiếng Anh                  | Nghĩa                                                                                                 |
| ------------------------------------------ | -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Độc quyền nhóm                             | *oligopoly*                | thị trường chỉ có một số ít người bán, sản phẩm tương tự hoặc gần như tương tự nhau                   |
| Thị trường nhị quyền                       | *duopoly*                  | độc quyền nhóm với đúng hai người bán — dạng đơn giản nhất                                            |
| Lý thuyết trò chơi                         | *game theory*              | nghiên cứu việc con người hành xử thế nào trong các tình huống chiến lược                             |
| Sự cấu kết                                 | *collusion*                | thỏa thuận giữa các doanh nghiệp về sản lượng và giá bán                                              |
| Cartel                                     | *cartel*                   | nhóm doanh nghiệp hoạt động vì mục tiêu chung — thực chất là một nhà độc quyền nhiều đầu              |
| Cân bằng Nash                              | *Nash equilibrium*         | mỗi bên chọn chiến lược tốt nhất **sau khi biết** đối phương đã chọn gì; không ai muốn đổi ý một mình |
| Chiến lược thống soái                      | *dominant strategy*        | tốt nhất **bất kể** đối phương chọn gì                                                                |
| Tình thế tiến thoái lưỡng nan của người tù | *prisoners' dilemma*       | trò chơi mà cân bằng Nash **không** là kết cục tốt nhất cho các bên                                   |
| Hiệu ứng lượng                             | *output effect*            | bán thêm một đơn vị thì lãi thêm, vì giá cao hơn chi phí biên                                         |
| Hiệu ứng giá                               | *price effect*             | bán thêm làm giá tụt, kéo lợi nhuận trên **mọi** đơn vị còn lại xuống                                 |
| Ăn miếng trả miếng                         | *tit for tat*              | bắt đầu tử tế, rồi lặp lại đúng nước đi vừa rồi của đối phương                                        |
| Trừng phạt vĩnh viễn                       | *grim trigger*             | hợp tác cho tới khi bị phản bội một lần, rồi bội ước mãi mãi                                          |
| Hệ số chiết khấu                           | *discount factor*          | một đồng ở kỳ sau đáng bao nhiêu đồng hôm nay — đo "tương lai còn dài bao nhiêu"                      |
| Nghiệm Cournot                             | *Cournot equilibrium*      | cân bằng Nash khi các doanh nghiệp cạnh tranh bằng **sản lượng**                                      |
| Cố định giá bán lẻ                         | *resale price maintenance* | nhà sản xuất buộc nhà bán lẻ không bán dưới một mức giá                                               |
| Bán phá giá                                | *predatory pricing*        | hạ giá dưới chi phí nhằm loại đối thủ rồi tăng giá lại                                                |
| Bán kèm sản phẩm                           | *tying / bundling*         | bán hai sản phẩm chung một gói với một mức giá                                                        |
| Luật chống độc quyền                       | *antitrust law*            | Sherman (1890) và Clayton (1914) ở Hoa Kỳ                                                             |

---

## 21. Câu hỏi tự kiểm tra

Trả lời rồi mới quay lại đối chiếu. Số trong ngoặc là mục chứa câu trả lời.

1. Vì sao ba bài trước không cần lý thuyết trò chơi mà bài này thì cần? *(mục 1)*
2. Cùng biểu cầu ở Bảng 1, ba cách tổ chức ngành cho ba mức sản lượng nào? Sắp xếp chúng. *(mục 3)*
3. Phát biểu định nghĩa cân bằng Nash. Vì sao (30, 30) — kết cục cartel — **không** phải cân bằng Nash?
   *(mục 4)*
4. Chiến lược thống soái khác cân bằng Nash ở chỗ nào? Cho một ví dụ có cân bằng Nash nhưng **không**
   có chiến lược thống soái. *(mục 7)*
5. Hai lực nào giằng nhau khi một doanh nghiệp độc quyền nhóm cân nhắc bơm thêm một gallon? Lực nào
   yếu đi khi số người bán tăng, và vì sao? *(mục 5)*
6. Với $n$ doanh nghiệp, cầu $P = a - Q$, chi phí biên bằng 0 — viết công thức sản lượng và giá cân
   bằng. Kiểm nó với $n = 1$ và $n = 2$. *(mục 6)*
7. Nêu bốn hoàn cảnh khác nhau trong chương có **cùng** cấu trúc tiến thoái lưỡng nan. Ở mỗi hoàn cảnh,
   "hợp tác" nghĩa là gì? *(mục 8)*
8. OPEC thành công nhất giai đoạn nào, và điều gì làm nó đổ vỡ? Sự đổ vỡ đó là tin tốt hay tin xấu —
   với ai? *(mục 9)*
9. Nêu hai trường hợp trong chương mà **thiếu hợp tác lại là điều tốt** cho xã hội, và giải thích vì sao.
   *(mục 10)*
10. Trò chơi lặp đi lặp lại thay đổi kết cục thế nào? Viết bất đẳng thức xác định ngưỡng hợp tác bền
    và giải nó cho trò chơi Jack–Jill. *(mục 12)*
11. Ăn miếng trả miếng thắng giải đấu của Axelrod dù **không thắng nổi đối thủ nào**. Nghịch lý này
    giải thích ra sao? *(mục 13)*
12. Vì sao "trừng phạt vĩnh viễn" là một điều khoản phạt tệ, dù nghe cứng rắn? Nêu con số. *(mục 14)*
13. Crandall làm gì mà bị khởi tố? Nếu ông ta chỉ **tự** tăng giá vé 20% mà không gọi ai thì sao?
    *(mục 15)*
14. Nêu điều kiện để bán kèm sản phẩm sinh lời. Vì sao lập luận của toà tối cao trong vụ Makemoney
    không đứng vững? *(mục 16)*
15. Vì sao "kẻ săn mồi phải chịu nhiều tổn thất hơn con mồi" trong một cuộc chiến giá? *(mục 16)*
16. 💼 Trong ba cách thoát khỏi cuộc chiến giảm giá, cách nào bền nhất và vì sao? Cách nào có nguy cơ
    dẫn tới vi phạm luật chống độc quyền? *(mục 17)*

---

## Tóm tắt một trang

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  BÀI 9 — ĐỘC QUYỀN NHÓM VÀ LÝ THUYẾT TRÒ CHƠI     (Mankiw ch.17, 391-420) ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ĐỘC QUYỀN NHÓM = ít người bán, và HÀNH ĐỘNG CỦA MỖI NGƯỜI ẢNH HƯỞNG      ║
║  LỢI NHUẬN CỦA NGƯỜI KHÁC. Đây là lý do cần một bộ công cụ mới.           ║
║                                                                           ║
║  ── BA KẾT CỤC, CÙNG MỘT BIỂU CẦU (P = 120 - Q, MC = 0) ────────────      ║
║                                                                           ║
║     Cạnh tranh hoàn hảo      120 gal    $0      lợi nhuận ngành  $0       ║
║     Cartel / độc quyền        60 gal   $60                    $3.600      ║
║     Nhị quyền (Nash)          80 gal   $40                    $3.200      ║
║                                                                           ║
║     Độc quyền nhóm luôn nằm GIỮA: sản lượng cao hơn độc quyền nhưng       ║
║     thấp hơn cạnh tranh; giá thấp hơn độc quyền nhưng cao hơn MC.         ║
║                                                                           ║
║  ── HAI ĐỊNH NGHĨA KHÔNG ĐƯỢC LẪN ─────────────────────────────────       ║
║                                                                           ║
║     CHIẾN LƯỢC THỐNG SOÁI  thuộc tính của MỘT người chơi                  ║
║                            "tốt nhất bất kể đối phương làm gì"            ║
║     CÂN BẰNG NASH          thuộc tính của MỘT CẶP lựa chọn                ║
║                            "không ai muốn đổi ý một mình"                 ║
║     Thống soái hai bên  =>  Nash.   Nash  =/=>  thống soái.               ║
║                                                                           ║
║  ── CÔNG THỨC COURNOT (sách không đưa, suy ra được) ───────────────       ║
║                                                                           ║
║     n doanh nghiệp,  P = a - Q,  MC = 0:                                  ║
║        mỗi bên bơm  a/(n+1)      giá  a/(n+1)      tổng  n.a/(n+1)        ║
║     n = 1 -> độc quyền.   n -> vô cùng -> cạnh tranh hoàn hảo.            ║
║     Giá tụt RẤT NHANH ở đầu rồi phẳng dần: đối thủ ĐẦU TIÊN đắt nhất.     ║
║                                                                           ║
║  ── TIẾN THOÁI LƯỠNG NAN: BỐN HOÀN CẢNH, MỘT CẤU TRÚC ─────────────       ║
║                                                                           ║
║     Bonnie & Clyde     cùng thú tội 8 năm   <  cùng im lặng 1 năm         ║
║     Jack & Jill        cùng 40 gal $1.600   <  cùng 30 gal $1.800         ║
║     Exxon & Texaco     cùng 2 giếng $4tr    <  cùng 1 giếng $5tr          ║
║     Mỹ & Mexico        cùng thuế cao $20tỷ  <  cùng thuế thấp $25tỷ       ║
║                                                                           ║
║     Cân bằng Nash KHÔNG PHẢI kết cục tốt nhất. Đó là định nghĩa.          ║
║                                                                           ║
║  ── THIẾU HỢP TÁC TỐT HAY XẤU? CÒN TÙY BẠN ĐỨNG Ở ĐÂU ─────────────       ║
║                                                                           ║
║     XẤU: chạy đua vũ trang, giếng dầu chung (lãng phí thuần)              ║
║     TỐT: Bonnie & Clyde (cảnh sát thắng), độc quyền nhóm (khách thắng)    ║
║                                                                           ║
║     "Bàn tay vô hình chỉ giúp thị trường phân bổ nguồn lực hiệu quả       ║
║      khi thị trường cạnh tranh, và thị trường chỉ mang tính cạnh tranh    ║
║      khi các doanh nghiệp KHÔNG THỂ hợp tác với nhau."   (tr. 403)        ║
║                                                                           ║
║  ── TRÒ CHƠI LẶP: HỢP TÁC BỀN KHI NÀO ─────────────────────────────       ║
║                                                                           ║
║               món lợi từ bội ước                2000 - 1800        1      ║
║     d  >=  ───────────────────────────────  =  ─────────────  =  ───      ║
║            món lợi + thiệt hại mỗi kỳ sau       2000 - 1600        2      ║
║                                                                           ║
║     d gần 1 = quan hệ còn dài.  d gần 0 = "chỉ còn lần này".              ║
║     => HỢP TÁC SỤP ĐỔ KHI TƯƠNG LAI NGẮN LẠI.                             ║
║                                                                           ║
║  ── MỘT LẦN LỠ TAY (tuần 5), TỔNG LỢI NHUẬN 10 TUẦN ───────────────       ║
║                                                                           ║
║     Ăn miếng trả miếng          35.400    mất   600                       ║
║     Trừng phạt vĩnh viễn        34.200    mất 1.800  <- tệ gấp 3          ║
║     Ăn miếng trả miếng độ lượng 35.900    mất   100  <- có CỬA QUAY LẠI   ║
║                                                                           ║
║  ── LUẬT CHỐNG ĐỘC QUYỀN ──────────────────────────────────────────       ║
║                                                                           ║
║     Sherman 1890   cấu kết = âm mưu phạm pháp, không chỉ hợp đồng vô hiệu ║
║     Clayton 1914   tư nhân được kiện, bồi thường GẤP BA                   ║
║                                                                           ║
║     RANH GIỚI: tự mình giữ giá cao = HỢP PHÁP.                            ║
║                Gọi điện rủ đối thủ cùng giữ giá cao = PHẠM PHÁP.          ║
║                (Crandall, American Airlines, 1983)                        ║
║                                                                           ║
║     Nhưng cẩn thận: cố định giá bán lẻ, bán kèm, giảm giá mạnh có thể     ║
║     có MỤC ĐÍCH CHÍNH ĐÁNG. Bán kèm sinh lời khi khách XẾP HẠNG NGƯỢC     ║
║     nhau ($30.000 -> $40.000); vô dụng khi ai cũng thích cùng một món.    ║
║                                                                           ║
║  ── 💼 GÓC QTKD ───────────────────────────────────────────────────       ║
║                                                                           ║
║     Cuộc chiến giảm giá TỰ SINH RA cấu trúc lưỡng nan từ số liệu thật:    ║
║     cả hai cùng giảm -> mỗi bên mất 3.500, THỊ PHẦN KHÔNG ĐỔI.            ║
║                                                                           ║
║     Ba cách thoát:  (1) kéo dài tương lai — hợp đồng khung nhiều năm      ║
║                     (2) bỏ qua một lần lỡ — đừng phạt vĩnh viễn           ║
║                     (3) làm cầu bớt co giãn — khác biệt hoá  <- BỀN NHẤT  ║
║                                                                           ║
║     (3) bền nhất vì nó KHÔNG CẦN ĐỐI THỦ ĐỒNG Ý ĐIỀU GÌ.                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Sách gốc:** N. Gregory Mankiw, *Kinh tế học vi mô* (*Principles of Microeconomics*), bản dịch của
  Khoa Kinh tế, **ĐH Kinh tế TP.HCM**, Cengage Learning Asia.
  File: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`
  *(số trang sách = số trang PDF − 33)*
- **Chương 17 — Độc quyền nhóm**, tr. 391–420 (PDF 424–453). Các mục được dùng:
  - *Thị trường chỉ có vài người bán* — ví dụ bóng tennis, tr. 391
  - *Ví dụ về thị trường nhị quyền* và **Bảng 1** *Biểu cầu nước sinh hoạt*, tr. 392
  - *Cạnh tranh, độc quyền và cartel*, tr. 393
  - *Trạng thái cân bằng của thị trường độc quyền nhóm* — lập luận của Jack, cân bằng Nash, tr. 394–395
  - *Quy mô của thị trường độc quyền nhóm tác động tới kết cục thị trường như thế nào* —
    hiệu ứng lượng và hiệu ứng giá, thương mại quốc tế, tr. 395–397
  - *Tình huống tiến thoái lưỡng nan của người tù* và **Hình 1**, tr. 397–398
  - *Doanh nghiệp độc quyền nhóm — Một dạng tình huống tiến thoái lưỡng nan của người tù* và
    **Hình 2**, tr. 399–400
  - Nghiên cứu tình huống *OPEC và thị trường dầu thô thế giới*, tr. 400–401
  - *Các ví dụ khác* — chạy đua vũ trang (**Hình 3**), nguồn tài nguyên chung (**Hình 4**), tr. 401–402
  - *Tình huống tiến thoái lưỡng nan của người tù và phúc lợi xã hội*, tr. 403
  - *Tại sao mọi người vẫn thỉnh thoảng hợp tác với nhau*, tr. 403–404
  - Nghiên cứu tình huống *Giải đấu về tình huống tiến thoái lưỡng nan của người tù* — Robert Axelrod
    và chiến lược ăn miếng trả miếng, tr. 404–405
  - *Hạn chế của những bộ luật thương mại và luật chống độc quyền* — Sherman 1890, Clayton 1914,
    tr. 405–406
  - Nghiên cứu tình huống *Một cuộc điện thoại bất hợp pháp* — Crandall và Putnam, *New York Times*
    24/2/1983, tr. 406–407
  - *Những điểm gây tranh cãi của chính sách chống độc quyền* — cố định giá bán lẻ, bán phá giá,
    bán kèm sản phẩm, tr. 407–409
  - Nghiên cứu tình huống *Vụ kiện tập đoàn Microsoft*, tr. 409–411
  - **Bài tập 2** (cartel kim cương Nga – Nam Phi), tr. 413 và **bài tập 4** (chiến tranh thuế quan
    Hoa Kỳ – Mexico), tr. 414
- **Ngoài sách:**
  - Nghiệm Cournot ở [mục 6](#6--nghiệm-cournot--chứng-minh-công-thức-tổng-quát) — Antoine Augustin
    Cournot, *Recherches sur les principes mathématiques de la théorie des richesses*, 1838.
  - Ngưỡng hệ số chiết khấu ở [mục 12](#12--hệ-số-chiết-khấu--hợp-tác-bền-khi-nào) — kết quả chuẩn
    của lý thuyết trò chơi lặp; sách chỉ mô tả bằng lời.
  - Chiến lược *ăn miếng trả miếng độ lượng* (**tit for two tats**) ở [mục 13](#13-giải-đấu-axelrod-và-ăn-miếng-trả-miếng)
    và [mục 14](#14-một-lần-lỡ-tay--chỗ-sách-chỉ-nói-bằng-lời) — cũng từ giải đấu Axelrod, sách không nhắc.
  - Đối chiếu 2026 ở [mục 9](#9-nghiên-cứu-tình-huống--opec) và [mục 16](#16-ba-hành-vi-gây-tranh-cãi)
    (OPEC+, dầu đá phiến Hoa Kỳ, Đạo luật Thị trường Kỹ thuật số của EU 2022).
  - Mô hình cuộc chiến giảm giá ở [mục 17](#17--cuộc-chiến-giảm-giá--kiểm-tra-chứ-không-giả-định) —
    dựng riêng cho bài này, không có trong sách.
- **Liên hệ chéo:**
  - [Bài 6](bai_06_thi_truong_canh_tranh.md) và [Bài 7](bai_07_doc_quyen_va_phan_biet_gia.md) — hai
    thái cực mà độc quyền nhóm nằm giữa.
  - [Bài 7](bai_07_doc_quyen_va_phan_biet_gia.md) — phân biệt giá, thứ giải thích vì sao bán kèm sinh lời.
  - [Bài 8](bai_08_canh_tranh_doc_quyen.md) — khác biệt hoá, cách thoát bền nhất khỏi chiến tranh giá.
  - [Bài 3](bai_03_do_co_gian_va_dinh_gia.md) — độ co giãn, thứ quyết định cuộc chiến giá đau tới đâu.
  - **Bài 10** (chương 21) — bỏ phía doanh nghiệp, quay sang **người tiêu dùng** quyết định thế nào.

<!-- BAN-DO -->

**Bản đồ khoá học**

|     # | Bài                                                                                  | Chương sách | Ưu tiên |
| ----: | ------------------------------------------------------------------------------------ | ----------- | :-----: |
|     1 | [Mười nguyên lý và tư duy kinh tế](bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)       | ch. 1–2     |    🎯    |
|     2 | [Cung và cầu](bai_02_cung_va_cau.md)                                                 | ch. 4       |    🎯    |
|     3 | [Độ co giãn và định giá](bai_03_do_co_gian_va_dinh_gia.md)                           | ch. 5       |   🎯⭐    |
|     4 | [Thặng dư và chi phí của thuế](bai_04_thang_du_va_chi_phi_cua_thue.md)               | ch. 7–8     |    🔸    |
|     5 | [Chi phí sản xuất](bai_05_chi_phi_san_xuat.md)                                       | ch. 13      |    🎯    |
|     6 | [Doanh nghiệp trên thị trường cạnh tranh](bai_06_thi_truong_canh_tranh.md)           | ch. 14      |    🎯    |
|     7 | [Độc quyền và phân biệt giá](bai_07_doc_quyen_va_phan_biet_gia.md)                   | ch. 15      |    🎯    |
|     8 | [Cạnh tranh độc quyền và thương hiệu](bai_08_canh_tranh_doc_quyen.md)                | ch. 16      |    🎯    |
| **9** | **Độc quyền nhóm và lý thuyết trò chơi** ← *bạn đang ở đây*                          | ch. 17      |    🎯    |
|    10 | [Lựa chọn của người tiêu dùng](bai_10_lua_chon_cua_nguoi_tieu_dung.md)               | ch. 21      |    🎯    |
|    11 | [Thông tin bất cân xứng và hành vi](bai_11_thong_tin_bat_can_xung.md)                | ch. 22      |    🎯    |
|    12 | [Lao động, tiền lương, bất bình đẳng](bai_12_thi_truong_lao_dong.md)                 | ch. 18–20   |    🔸    |
|    13 | [Chính phủ can thiệp thị trường](bai_13_chinh_phu_can_thiep_thi_truong.md)           | ch. 6, 12   |    🔸    |
|    14 | [Thương mại, ngoại tác, hàng hoá công](bai_14_thuong_mai_ngoai_tac_hang_hoa_cong.md) | ch. 3, 9–11 |    🔸    |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương quan trọng nhất với QTKD

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
