# Bài 6 — Lợi nhuận ≠ tiền mặt

> Bài học dựng từ **Phần IV — Tiền mặt là nhất**, chương 14 *Tiền mặt là một phép kiểm tra thực tế*
> (PDF tr. 109–112) và chương 15 *Lợi nhuận ≠ tiền mặt (Và ta cần cả hai)* (PDF tr. 113–120).
> 🎯⭐ **Vòng 1, và là bài đắt giá nhất cả cuốn.** Đây là chỗ cuốn sách trả lời câu hỏi mà nó đặt ra
> từ trang đầu. Nếu chỉ đọc được một bài trong khoá này, đọc bài này.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang số liệu Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 0](bai_00_bat_dau_tu_dau.md) — ba báo cáo tài chính và công ty mẫu.
> Mục 3 dùng lại **nguyên tắc phù hợp** của [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md).
> ⚙️ **Code:** [`thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py`](../thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py)

---

## Mục lục

<!-- MUC-LUC -->

- [1. Câu mở đầu của Phần IV](#1-câu-mở-đầu-của-phần-iv)
- [2. Warren Buffett và ba quy tắc](#2-warren-buffett-và-ba-quy-tắc)
- [3. Ba lý do lợi nhuận không bằng tiền mặt](#3-ba-lý-do-lợi-nhuận-không-bằng-tiền-mặt)
- [4. Sweet Dreams — có lãi mà hết sạch tiền](#4-sweet-dreams--có-lãi-mà-hết-sạch-tiền)
- [5. Fine Cigar — lỗ mà tiền mặt tăng đều](#5-fine-cigar--lỗ-mà-tiền-mặt-tăng-đều)
- [6. ⚠️ Hai bảng của chương 15 bị đảo dấu cho nhau](#6--hai-bảng-của-chương-15-bị-đảo-dấu-cho-nhau)
- [7. Cái giá của tăng trưởng — phép tính sách không làm](#7-cái-giá-của-tăng-trưởng--phép-tính-sách-không-làm)
- [8. 💼 Góc quản trị — hai bệnh, hai bác sĩ](#8--góc-quản-trị--hai-bệnh-hai-bác-sĩ)
- [9. 🇻🇳 Đối chiếu Việt Nam — Vinamilk 2024](#9--đối-chiếu-việt-nam--vinamilk-2024)
- [10. Tự thử](#10-tự-thử)
- [11. Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
- [12. Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Câu mở đầu của Phần IV

Sách mở phần này bằng một câu trích từ tạp chí *Fortune* số tháng Năm 2002, thời điểm hàng loạt
doanh nghiệp Mỹ đang phá sản sau khi bong bóng dot-com nổ:

> *"Các doanh nghiệp phải thắng phanh gấp vì đủ mọi lý do, song có một điều cuối cùng sẽ giết chết
> họ: **hết tiền mặt**."* — Ram Charan và Jerry Useem, dẫn ở ch. 14 · PDF tr. 109

Chú ý cấu trúc câu. Nó không nói *"doanh nghiệp chết vì hết tiền"*. Nó nói doanh nghiệp gặp khó vì
đủ thứ lý do — cạnh tranh, sản phẩm hỏng, quản lý kém — nhưng **cơ chế chết** thì chỉ có một.

Ba báo cáo tài chính, vậy thì cái nào cho biết doanh nghiệp sắp chết? Sách trả lời thẳng ở cuối
chương 14:

> *"…chính tiền mặt là huyết mạch của doanh nghiệp, và dòng tiền là thước đo trọng yếu cho sức khỏe
> tài chính. Chúng ta cần con người để hoạt động kinh doanh… Chúng ta cần địa điểm kinh doanh, điện
> thoại, điện, máy tính, các đồ dùng văn phòng, v.v… **Và chúng ta không thể dùng lợi nhuận để trả
> cho tất cả những thứ đó bởi lợi nhuận không phải là tiền thật. Tiền mặt thì có.**"*
> — ch. 14 · PDF tr. 112

---

## 2. Warren Buffett và ba quy tắc

Sách dùng Buffett làm nhân chứng, không phải làm thần tượng. Lập luận là: nếu nhà đầu tư giỏi nhất
lịch sử chỉ nhìn một con số, thì con số đó đáng để ta nhìn theo.

Ba quy tắc mà sách rút ra (ch. 14 · PDF tr. 109):

```
   ①  đánh giá doanh nghiệp theo triển vọng DÀI HẠN, không phải ngắn hạn
   ②  chỉ mua những doanh nghiệp mình HIỂU RÕ   (nhờ vậy tránh được làn sóng dot-com)
   ③  khi đọc báo cáo tài chính, chú trọng hơn cả vào THU NHẬP CHỦ SỞ HỮU — một
      thước đo DÒNG TIỀN, không phải lợi nhuận
```

> **Thu nhập chủ sở hữu** (*owner earnings*, còn gọi là **dòng tiền tự do** — *free cash flow*):
> thước đo khả năng tạo ra tiền mặt của doanh nghiệp trong một khoảng thời gian, **sau khi đã trừ
> các khoản chi đầu tư cần thiết để duy trì sức khoẻ doanh nghiệp**. — ch. 14 · PDF tr. 109

Mấy chữ cuối là điểm mấu chốt, và sách nói rõ vì sao thước đo này hơn hai thước đo quen thuộc:
*"Lợi nhuận và thậm chí cả các thước đo dòng lưu chuyển tiền từ hoạt động kinh doanh không làm được
điều này."* Cách tính cụ thể nằm ở hộp công cụ cuối Phần IV — [bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md).

Còn lý do sâu xa thì sách đặt ở PDF tr. 110, và nó nối thẳng về bài 1:

> *"…ông biết nó là con số **ít chịu tác động của nghệ thuật tài chính nhất**."*

⭐ **Một phép tính sách không làm.** Sách ghi cổ phiếu hạng A của Berkshire Hathaway đạt tăng trưởng
**17,9%/năm** từ tháng 1/1994 đến tháng 1/2004, rồi dừng ở đó. Gộp lãi mười năm, con số ấy là
**5,19 lần** vốn ban đầu. Để so sánh: 10%/năm cho 2,59 lần, 20%/năm cho 6,19 lần. Chênh 2,1 điểm
phần trăm mỗi năm giữa 17,9% và 20% thành **một lần vốn** sau mười năm.

---

## 3. Ba lý do lợi nhuận không bằng tiền mặt

Đây là ruột của chương 15 (PDF tr. 113). Sách nêu ba lý do — và cả ba đều bắt nguồn từ **nguyên tắc
phù hợp** đã học ở [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md).

|       | Lý do                                                                      | Hệ quả                                            |
| :---: | -------------------------------------------------------------------------- | ------------------------------------------------- |
|   ①   | **Doanh thu ghi nhận lúc giao hàng**, không phải lúc thu tiền              | lợi nhuận phản ánh **lời hứa trả tiền** của khách |
|   ②   | **Chi phí khớp với doanh thu**, không phải với lúc chi tiền                | khoản chi trên báo cáo ≠ tiền ra khỏi cửa         |
|   ③   | **Chi phí đầu tư cơ bản không làm giảm lợi nhuận** — chỉ khấu hao mới giảm | tiền ra rất lớn mà lợi nhuận không hề biết        |

Lý do ③ khó thấy nhất, nên hãy đo nó trên công ty mẫu ở phụ lục, năm 2005:

```
   tiền THỰC CHI mua tài sản (capex)        205 triệu   ← rời khỏi tài khoản ngân hàng
   khấu hao TRỪ vào lợi nhuận               239 triệu   ← không ai trả đồng nào
   ───────────────────────────────────────────────────
   Báo cáo kết quả kinh doanh KHÔNG hề biết 205 triệu đô đã đi mất.
   Chỉ báo cáo lưu chuyển tiền tệ thấy được.
```

⚠️ Đừng vội kết luận *"khấu hao 239 lớn hơn capex 205 nên ổn"*. Hai con số này **không** cùng loại:
239 là con số kế toán tính theo tuổi đời tài sản mua từ nhiều năm trước; 205 là tiền thật của riêng
năm 2005. Chúng chỉ tình cờ gần nhau. [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) sẽ tách bạch chỗ này.

---

## 4. Sweet Dreams — có lãi mà hết sạch tiền

Tiệm bánh mới mở. Bán chịu cho cửa hàng tạp hoá: **khách trả sau 60 ngày**. Nhà cung cấp cho tiệm
nợ **30 ngày**. Giá vốn 60% doanh thu, chi phí hoạt động 10.000/tháng, vốn ban đầu 10.000 đô-la.

```
                            tháng 1     tháng 2     tháng 3
   Doanh thu                 20.000      30.000      45.000
   Giá vốn hàng bán          12.000      18.000      27.000
   Chi phí hoạt động         10.000      10.000      10.000
   ────────────────────────────────────────────────────────
   LỢI NHUẬN THUẦN           −2.000      +2.000      +8.000    ← ĐI LÊN
   SỐ DƯ TIỀN MẶT                 0     −22.000     −30.000    ← ĐI XUỐNG
```

Hai hàng cuối **đi ngược chiều nhau**. Đó là toàn bộ Phần IV của sách, gói trong sáu con số.

Cơ chế thì tầm thường đến mức khó chịu: tháng 1 tiệm giao bánh và ghi 20.000 doanh thu, nhưng phải
đợi đến **tháng 3** mới thấy tiền. Trong khi đó nhà cung cấp đòi tiền ngay từ **tháng 2**. Tiệm trả
trước, thu sau, và khoảng cách đó là 30 ngày.

> *"Chuyện gì đang xảy ra ở đây vậy? Câu trả lời là Sweet Dreams **đang phình ra**."*
> — ch. 15 · PDF tr. 116

Và câu kết luận, đáng nhớ nguyên văn:

> *"Dù ví dụ về Sweet Dreams là hư cấu và đã được giản lược hết mức, song **đây chính xác là những gì
> sẽ đẩy các doanh nghiệp có tiềm năng lợi nhuận đi đến chỗ phá sản**. Và đây cũng là một trong những
> lý do giải thích cho việc tại sao nhiều doanh nghiệp nhỏ bại trận ngay từ năm đầu hoạt động. Lý do
> đơn giản là vì họ cạn tiền mặt."* — ch. 15 · PDF tr. 116

---

## 5. Fine Cigar — lỗ mà tiền mặt tăng đều

Bây giờ lật ngược lại. Cửa hàng xì gà bán lẻ: **thu tiền ngay**. Đàm phán được **60 ngày** với nhà
cung cấp. Giá vốn 70% doanh thu, chi phí 30.000/tháng (thuê mặt bằng đắt), vốn ban đầu 10.000.

```
                            tháng 1     tháng 2     tháng 3
   Doanh thu                 50.000      75.000      95.000
   Giá vốn hàng bán          35.000      52.500      66.500
   Chi phí hoạt động         30.000      30.000      30.000
   ────────────────────────────────────────────────────────
   LỢI NHUẬN THUẦN          −15.000      −7.500      −1.500    ← LỖ cả ba tháng
   SỐ DƯ TIỀN MẶT            30.000      75.000     105.000    ← TĂNG VÙN VỤT
```

Sách gọi cơ chế này là **"phao nổi"**: cầm tiền của khách trước khi phải trả nhà cung cấp. Amazon và
Dell sống bằng nó — và sách nhắc đích danh cả hai. Doanh nghiệp càng lớn nhanh, phao càng phình to.

⚠️ Nhưng sách cảnh báo ngay ở câu sau, và đây là chỗ nhiều người đọc lướt:

> *"…về lâu dài, **tiền mặt không phải là tấm khiên bảo vệ khỏi nguy cơ không lợi nhuận**."*
> — ch. 15 · PDF tr. 118

Nguy hiểm thật sự của Fine Cigar không phải là hết tiền — mà là **chủ cửa hàng nhìn số dư ngân hàng
tăng đều rồi tưởng mình đang làm ăn tốt**, và tăng chi phí. Lỗ trên sổ sách cuối cùng vẫn sẽ ăn hết
phao.

---

## 6. ⚠️ Hai bảng của chương 15 bị đảo dấu cho nhau

Đây là lỗi in nặng nhất trong cả cuốn sách, và nó rơi đúng vào hai bảng vừa xem.

| Bảng             | Bản dịch in                 | Đúng phải là                 |
| ---------------- | --------------------------- | ---------------------------- |
| **Sweet Dreams** | (2.000) (2.000) **(8.000)** | (2.000) **2.000 8.000**      |
| **Fine Cigar**   | 15.000 7.500 1.500          | **(15.000) (7.500) (1.500)** |

Hai bảng bị **hoán dấu cho nhau**: bảng đáng lẽ dương thì in âm, bảng đáng lẽ âm thì in dương.

Cách tự kiểm mà không cần máy tính — **đọc đoạn văn bao quanh bảng**:

- Ngay **trên** bảng Sweet Dreams, sách viết *"chỉ liếc qua các con số này, bạn có thể thấy cô sẽ
  nhanh chóng có lợi nhuận"*. Vậy mà bảng in lỗ cả ba tháng.
- Ngay **dưới** bảng Fine Cigar, sách viết *"mặc dù đang trong tình trạng tháng nào cũng lỗ"*. Vậy
  mà bảng in lãi cả ba tháng.

⭐ **Bằng chứng chốt hạ nằm trong chính cuốn sách.** Lời giới thiệu của Alphabooks ở đầu sách kể lại
đúng ví dụ Sweet Dreams, quy ra tiền Việt, với dấu **đúng**:

> *"…bạn rút ra được rằng bạn **lỗ 2 triệu** trong tháng đầu tiên, **lãi 2 triệu** trong tháng thứ
> hai, và **lãi 8 triệu** trong tháng thứ ba."* — Lời giới thiệu · PDF tr. 3

Cùng một cuốn sách, hai chỗ, hai kết quả trái ngược. Chỗ sai là bảng ở chương 15.

⚠️ **Vì sao lỗi này nặng hơn nó có vẻ.** Hai bảng ấy tồn tại **chỉ để** chứng minh một luận điểm: lợi
nhuận và tiền mặt đi ngược chiều nhau. In sai dấu làm cả hai bảng cùng nói "lỗ thì hết tiền, lãi thì
có tiền" — tức là đúng cái điều mà chương này muốn bác bỏ. Người đọc cẩn thận sẽ thấy chương 15
**tự mâu thuẫn** và không hiểu tại sao.

---

## 7. Cái giá của tăng trưởng — phép tính sách không làm

Sách dừng Sweet Dreams ở tháng 3 và chỉ nói *"chỉ cần doanh thu còn tăng thì tiệm sẽ không bao giờ
bắt kịp"*. Câu đó đúng, nhưng nó giấu một chuyện: **tiệm đã thiếu vốn ngay từ đầu**. Với 10.000
đô-la, tiệm âm tiền ở tháng 2 dù tăng trưởng bao nhiêu đi nữa — vì hai tháng đầu không thu được đồng
nào mà vẫn phải trả.

Nên câu hỏi đúng không phải *"sống hay chết"*, mà là **"cần bao nhiêu vốn để sống qua 24 tháng?"**

```
   tốc độ tăng   lợi nhuận tháng 24   VỐN TỐI THIỂU CẦN CÓ
        0%                   −2.000                 76.000
        2%                   +2.615                 48.081
        5%                  +14.572                 41.749
       10%                  +61.634                 40.485   ← rẻ nhất
       15%                 +189.132                 41.041
       20%                 +519.979                 41.939
       30%               +3.330.312                 44.777
       50%              +89.771.932                 55.750
```

⭐ **Đường cong hình chữ U.** Tốn ít vốn nhất ở khoảng **10,2%/tháng**, khi đó cần **40.467 đô-la**.
Cả hai đầu đều đắt hơn, nhưng vì **hai căn bệnh hoàn toàn khác nhau**:

```
   TĂNG QUÁ CHẬM  →  doanh thu không bao giờ phủ nổi 10.000 chi phí cố định.
                     Với biên lợi nhuận gộp 40%, tiệm chỉ có lãi khi doanh thu
                     vượt 25.000/tháng. Ở 0%/tháng nó đứng yên ở 20.000 —
                     LỖ MÃI MÃI, vốn cần là vô hạn.

   TĂNG QUÁ NHANH →  có lãi, nhưng khoảng trống tiền mặt phình theo doanh thu.
                     Mỗi đồng doanh thu mới phải NẰM CHỜ 60 ngày mới thành tiền.
```

⚠️ Đọc kỹ cột cuối. Nó nói rằng **một tiệm bánh có lãi, không nợ xấu, không bị cạnh tranh, vẫn cần
nhiều vốn hơn khi nó bán được nhiều hàng hơn.** Ở 50%/tháng, lợi nhuận tháng 24 là **89,8 triệu**
đô-la mà tiệm vẫn cần 55.750 đô-la vốn đệm. Lợi nhuận không trả được hoá đơn nào cả.

### Điều khoản thanh toán đáng giá bao nhiêu

Giữ tăng trưởng 20%/tháng, chỉ đổi điều khoản. Mỗi ô là **vốn tối thiểu cần có**, càng nhỏ càng tốt:

```
                 DPO 0    DPO 30    DPO 45    DPO 60    DPO 75    DPO 90
   DSO   0      2.400         0         0         0         0         0
   DSO  30     31.939    12.400    10.000    10.000    10.000    10.000
   DSO  45     53.243    26.248    17.400    15.000    15.000    15.000
   DSO  60     81.522    41.939    31.248    22.400    20.000    20.000   ← Sweet Dreams
   DSO  75    141.931    63.243    46.939    36.248    27.400    25.000
   DSO  90    449.299    91.522    68.243    51.939    41.248    32.400
```

Từ điểm xuất phát của sách (DSO 60 / DPO 30, cần 41.939):

- kéo **DSO 60 → 30** (thu nhanh hơn 30 ngày) → giảm **29.539** đô-la vốn
- kéo **DPO 30 → 60** (trả chậm hơn 30 ngày) → giảm **19.539** đô-la vốn

⭐ **Cùng là 30 ngày, nhưng thu nhanh cứu được nhiều hơn trả chậm — gấp 1,51 lần.** Lý do: 30 ngày
DSO gắn vào **doanh thu**, còn 30 ngày DPO chỉ gắn vào **giá vốn**. Giá vốn bằng 60% doanh thu, nên
đòn bẩy cũng chỉ bằng chừng ấy.

Giả thuyết đó dự đoán tỷ số phải bằng đúng $1/\text{tỷ lệ giá vốn}$. Kiểm lại:

| Tỷ lệ giá vốn | 1 / tỷ lệ | đo ở tăng 0% | đo ở tăng 20% |
| ------------: | --------: | -----------: | ------------: |
|           40% |      2,50 |        2,250 |         2,250 |
|           50% |      2,00 |    **2,000** |         1,806 |
|           60% |      1,67 |    **1,667** |         1,512 |
|           70% |      1,43 |    **1,429** |         1,290 |
|           80% |      1,25 |    **1,250** |         1,113 |

Ở **tăng trưởng 0%, tỷ số đúng bằng $1/\text{tỷ lệ giá vốn}$** — giả thuyết chính xác. Khi doanh thu
tăng thì tỷ số tụt xuống, vì 30 ngày doanh thu của tháng sau lớn hơn 30 ngày giá vốn của tháng
trước, nên lợi thế của DSO bị bóp bớt.

⚠️ Riêng dòng 40% thì hai cột bằng nhau — nhưng vì **lý do khác hẳn**. Với biên lợi nhuận gộp 60%,
tiệm có lãi ngay ở tăng trưởng 0%, nên thứ trói buộc không còn là lỗ luỹ kế mà chỉ là khoảng trống
ban đầu — mà khoảng trống ấy không phụ thuộc tốc độ tăng. Một con số trùng nhau vì hai lý do khác
nhau, và đó là kiểu bẫy mà bài 1 gọi tên.

---

## 8. 💼 Góc quản trị — hai bệnh, hai bác sĩ

Chương 15 kết bằng một lời khuyên rất thực dụng, và nó là thứ đáng mang đi họp:

> *"Nếu một doanh nghiệp **có lợi nhuận nhưng lại không có tiền mặt**, thì doanh nghiệp đó cần
> **chuyên gia tài chính** – một ai đó có khả năng tăng thêm nguồn tài chính bổ sung. Nếu một doanh
> nghiệp **có tiền mặt nhưng không có lợi nhuận**, doanh nghiệp đó cần **chuyên môn hoạt động**,
> nghĩa là ai đó có khả năng kiểm soát chi phí hoặc tạo thêm doanh thu mà không làm tăng chi phí."*
> — ch. 15 · PDF tr. 119

```
                        CÓ TIỀN MẶT              KHÔNG CÓ TIỀN MẶT
                   ┌─────────────────────┬─────────────────────────┐
       CÓ LÃI      │   khoẻ mạnh         │   Sweet Dreams          │
                   │   (giữ nguyên)      │   → cần CHUYÊN GIA      │
                   │                     │      TÀI CHÍNH          │
                   ├─────────────────────┼─────────────────────────┤
     KHÔNG LÃI     │   Fine Cigar        │   sắp chết              │
                   │   → cần CHUYÊN MÔN  │   → cần cả hai, gấp     │
                   │      HOẠT ĐỘNG      │                         │
                   └─────────────────────┴─────────────────────────┘
```

⭐ Điểm mạnh của khung này: nó biến báo cáo tài chính thành **quyết định tuyển dụng**. Ô nào thì gọi
ai. Sách viết: *"các báo cáo tài chính không chỉ cho bạn biết điều gì đang diễn ra trong doanh
nghiệp, chúng còn có thể cho bạn biết bạn cần loại chuyên môn nào."*

### Đơn thuốc nào mạnh nhất

Giữ Sweet Dreams ở tăng trưởng 50%/tháng, thử từng đơn thuốc, đo bằng vốn tối thiểu cần có:

| Đơn thuốc                             | Vốn cần |  Tiết kiệm |
| ------------------------------------- | ------: | ---------: |
| nguyên trạng của sách                 |  55.750 |          — |
| thu 30 ngày **và** trả 60 ngày        |  10.000 | **45.750** |
| khách trả trong 30 ngày thay vì 60    |  12.000 |     43.750 |
| đàm phán nhà cung cấp lên 60 ngày     |  22.000 |     33.750 |
| cắt chi phí hoạt động 10.000 → 6.000  |  32.500 |     23.250 |
| nâng giá: giá vốn 60% → 50% doanh thu |  37.500 |     18.250 |
| **hạ tăng trưởng 50% → 15%/tháng**    |  41.041 |     14.709 |

⚠️ Hai điều đáng chú ý. Thứ nhất: **không đơn thuốc nào làm tiệm hết cần vốn** — chúng chỉ thu nhỏ
khoảng trống lại. Đó là bản chất của vốn lưu động, và là lý do sách dành cả Phần VII cho nó
(bài 11).

Thứ hai, dòng cuối: **hạ tăng trưởng cũng là một đơn thuốc**, và nó không hề yếu. Đây là kết luận mà
không giám đốc bán hàng nào muốn nghe — nhưng nếu công ty không huy động được vốn, thì bán chậm lại
là lựa chọn thật, không phải thất bại.

### 💼 Quyết định về thời điểm — Setpoint

Sách kể một ứng dụng nhỏ mà rất cụ thể. Setpoint (công ty của Joe) có **quý I lãi cao nhất** vì đơn
hàng tự động hoá về nhiều, nhưng **tiền mặt eo hẹp** vì phải trả cấu kiện và nhà thầu. Sang quý II
thì ngược lại: lợi nhuận giảm, nhưng tiền về vì thu được công nợ quý trước.

Kết luận của họ: **mua thiết bị đầu tư vào quý II, không phải quý I** — dù quý II lợi nhuận thấp hơn.

⭐ Đây là ví dụ sạch nhất trong cả cuốn về chuyện *"biết hai báo cáo khác nhau thì ra quyết định khác
đi"*. Nhìn báo cáo kết quả kinh doanh, quý I là lúc mạnh nhất. Nhìn dòng tiền, quý I là lúc yếu nhất.

---

## 9. 🇻🇳 Đối chiếu Việt Nam — Vinamilk 2024

Sách chỉ đưa hai ví dụ hư cấu ba tháng. Đây là cùng phép so sánh ấy trên một doanh nghiệp thật, số
liệu từ báo cáo tài chính hợp nhất **đã kiểm toán**:

|                                       | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| ------------------------------------- | ---------------------: | ------------------: |
| Lợi nhuận thuần                       |          248 triệu USD | 8.686.245 triệu VND |
| Tiền từ hoạt động kinh doanh          |          498 triệu USD | 9.770.587 triệu VND |
| **Tỷ lệ chuyển lợi nhuận thành tiền** |               **2,01** |            **1,12** |

Cả hai đều **lớn hơn 1** — tiền về nhiều hơn lợi nhuận ghi sổ. Đó là dấu hiệu lành mạnh, và lý do
chính ở cả hai trường hợp là **khấu hao**: một khoản trừ vào lợi nhuận mà không ai trả đồng nào
(Vinamilk: 2.163.203 triệu VND).

⚠️ **Nhưng đừng vội khen con số 2,01 của công ty mẫu.** Tách ra thì thấy nó đến từ hai nguồn rất khác
nhau:

```
   lợi nhuận thuần                            248
   + khấu hao                                 239   ← lặp lại được mọi năm
   + hàng tồn kho GIẢM                        244   ← MỘT LẦN. Không lặp lại được.
   − phải thu tăng, phải trả giảm, khác      −233
   ─────────────────────────────────────────────
   tiền từ hoạt động kinh doanh               498
```

Gần một nửa con số 498 đến từ việc **bán bớt hàng tồn kho** — một cái kho chỉ vơi được một lần. Sang
năm mà không có khoản đó thì tỷ lệ tụt về khoảng 1,0.

⭐ Đây chính là *"nghệ thuật tài chính"* áp vào báo cáo được cho là ít nghệ thuật nhất. Con số tiền
mặt thì thật, nhưng **lý do đằng sau nó thì phải đọc mới biết**. [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) sẽ dạy cách đọc
đúng chỗ này.

---

## 10. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py`](../thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py)
rồi chạy lại. Không có lời giải.

1. **Sweet Dreams tháng thứ tư.** Thêm tháng 4 với doanh thu 60.000. Lợi nhuận bao nhiêu, số dư tiền
   bao nhiêu? Khoảng cách giữa hai con số đang **giãn ra hay thu hẹp**?

2. **Điểm hoà vốn tiền mặt.** Ở mục 4, tìm tháng đầu tiên mà số dư tiền của Sweet Dreams **thôi giảm**
   (tăng trưởng 10%/tháng, vốn đủ). Nó cách tháng có lãi đầu tiên bao xa? Vì sao lại có độ trễ đó?

3. **Fine Cigar cắt chi phí.** Chi phí 30.000/tháng đang giết cửa hàng. Tìm mức chi phí **cao nhất**
   mà cửa hàng vẫn có lãi ngay từ tháng 1. Gợi ý: giải bằng biên lợi nhuận gộp 30%.

4. **Fine Cigar chạy 24 tháng.** Giữ nguyên mọi thứ, chạy 24 tháng ở tăng trưởng 10%/tháng. Tiền mặt
   có bao giờ quay đầu không? Nếu có thì tháng mấy — và điều đó khớp với cảnh báo *"tấm khiên"* của
   sách ở mục 5 thế nào?

5. **Đảo vai hai cửa hàng.** Cho Sweet Dreams điều khoản của Fine Cigar (thu ngay, trả 60 ngày).
   Vốn tối thiểu còn bao nhiêu? Rồi làm ngược lại. **Điều khoản thanh toán đáng giá bao nhiêu phần
   trăm so với cả mô hình kinh doanh?**

6. **Đường cong chữ U dịch chuyển.** Ở mục 4, đổi `dso` từ 60 xuống 30 rồi tìm lại điểm tối ưu. Nó
   dịch sang trái hay phải? Giải thích bằng lời trước khi chạy, rồi kiểm.

7. **Biên lợi nhuận cứu được đến đâu.** Với `tl = 0.30` (biên gộp 70%), Sweet Dreams có còn cần vốn
   ở tăng trưởng 50% không? Tìm mức `tl` mà tại đó vốn cần bằng 0.

8. **Kiểm chứng cột "tăng 0%".** Bảng ở mục 7 khẳng định tỷ số đúng bằng $1/\text{tỷ lệ giá vốn}$ khi
   tăng trưởng bằng 0. Chứng minh bằng giấy bút — không cần code — rằng điều đó **phải** đúng.

---

## 11. Từ điển thuật ngữ

| Tiếng Việt                          | Tiếng Anh                   | Nghĩa ngắn                                                           |
| ----------------------------------- | --------------------------- | -------------------------------------------------------------------- |
| Thu nhập chủ sở hữu                 | owner earnings              | thước đo dòng tiền Buffett dùng; **sau** khi trừ chi đầu tư duy trì  |
| Dòng tiền tự do                     | free cash flow              | tên phổ thông của cùng khái niệm                                     |
| Phao nổi                            | float                       | cầm tiền khách **trước** khi phải trả nhà cung cấp                   |
| Chi phí đầu tư cơ bản               | capital expenditure (capex) | tiền mua tài sản; **không** trừ vào lợi nhuận                        |
| Khấu hao                            | depreciation                | khoản trừ vào lợi nhuận mà **không ai trả tiền**                     |
| Kế toán dồn tích                    | accrual accounting          | ghi nhận lúc phát sinh, không phải lúc tiền đổi tay                  |
| 💼 Kỳ thu tiền (DSO)                 | days sales outstanding      | số ngày khách trả tiền sau khi mua — bài 9 và 11                     |
| 💼 Kỳ thanh toán (DPO)               | days payable outstanding    | số ngày ta trả nhà cung cấp — bài 9 và 11                            |
| 💼 Chết vì tăng trưởng               | overtrading · growing broke | có lãi mà cạn tiền vì bán quá nhanh — **cụm từ không có trong sách** |
| 💼 Tỷ lệ chuyển lợi nhuận thành tiền | cash conversion             | tiền từ HĐKD ÷ lợi nhuận thuần — **không có trong sách**             |

---

## 12. Câu hỏi tự kiểm tra

1. Câu trích của Charan và Useem nói doanh nghiệp gặp khó vì nhiều lý do, nhưng **chết** vì mấy lý do? (mục 1)
2. Vì sao không thể dùng lợi nhuận để trả lương? Trả lời bằng một câu của sách. (mục 1)
3. Kể ba quy tắc của Buffett mà sách rút ra. Quy tắc thứ ba dùng thước đo nào? (mục 2)
4. **Thu nhập chủ sở hữu** khác dòng tiền từ hoạt động kinh doanh ở chỗ nào? (mục 2)
5. Vì sao Buffett chuộng tiền mặt hơn lợi nhuận? Trả lời bằng cụm *"nghệ thuật tài chính"*. (mục 2)
6. 17,9%/năm trong 10 năm là bao nhiêu lần vốn? So với 20%/năm thì chênh bao nhiêu? (mục 2)
7. Kể ba lý do lợi nhuận không bằng tiền mặt. Lý do nào **khó thấy nhất** và vì sao? (mục 3)
8. Công ty mẫu chi 205 triệu mua tài sản. Báo cáo kết quả kinh doanh ghi nhận bao nhiêu trong số đó? (mục 3)
9. Vì sao **không** được kết luận "khấu hao 239 > capex 205 nên ổn"? (mục 3)
10. Sweet Dreams lãi tăng đều mà tiền âm dần. Cơ chế chính xác là gì? (mục 4)
11. Fine Cigar lỗ cả ba tháng mà tiền tăng đều. Sách gọi cơ chế đó là gì? Ai sống bằng nó? (mục 5)
12. Nguy hiểm thật sự của Fine Cigar là gì — hết tiền, hay điều gì khác? (mục 5)
13. Hai bảng ở chương 15 sai thế nào? Nêu **hai** cách tự phát hiện mà không cần máy tính. (mục 6)
14. Vì sao lỗi đảo dấu này nặng hơn một lỗi in thông thường? (mục 6)
15. Với 10.000 đô-la vốn, Sweet Dreams âm tiền ở tháng 2 **dù tăng trưởng bao nhiêu**. Vì sao? (mục 7)
16. Đường cong vốn cần có hình chữ U. Đầu trái chết vì bệnh gì, đầu phải chết vì bệnh gì? (mục 7)
17. Ở 50%/tháng, lợi nhuận tháng 24 là 89,8 triệu đô mà vẫn cần 55.750 vốn đệm. Giải thích. (mục 7)
18. Cùng 30 ngày, vì sao rút DSO cứu được nhiều hơn nới DPO? Tỷ số đó bằng bao nhiêu và **vì sao**? (mục 7)
19. Ở tỷ lệ giá vốn 40%, hai cột trong bảng bằng nhau — nhưng vì lý do khác. Lý do đó là gì? (mục 7)
20. Doanh nghiệp **có lãi mà thiếu tiền** thì cần loại chuyên môn nào? Còn **có tiền mà không lãi**? (mục 8)
21. Vì sao Setpoint mua thiết bị vào quý II chứ không phải quý I, dù quý I lãi cao hơn? (mục 8)
22. Trong bảy đơn thuốc ở mục 8, cái nào mạnh nhất? Có cái nào làm tiệm **hết** cần vốn không? (mục 8)
23. Tỷ lệ chuyển lợi nhuận thành tiền của Vinamilk là 1,12, của công ty mẫu là 2,01.
    Vì sao con số cao hơn lại **không** đáng tin hơn? (mục 9)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 6 ⭐ — LỢI NHUẬN ≠ TIỀN MẶT  (ch. 14–15, PDF tr. 109–120)           ║
╠══════════════════════════════════════════════════════════════════════════╣
║  "Lợi nhuận không phải là tiền thật. Tiền mặt thì có."   — ch.14         ║
║                                                                          ║
║  BA LÝ DO CHÚNG KHÁC NHAU                                                ║
║     ① doanh thu ghi nhận lúc GIAO HÀNG, không phải lúc thu tiền          ║
║     ② chi phí khớp với DOANH THU, không phải với lúc chi tiền            ║
║     ③ capex KHÔNG giảm lợi nhuận — chỉ khấu hao mới giảm  (205 vs 239)   ║
║                                                                          ║
║  HAI VÍ DỤ ĐI NGƯỢC CHIỀU NHAU                                           ║
║     Sweet Dreams   lãi  −2.000 → +2.000 → +8.000    ĐI LÊN               ║
║      (thu 60/trả 30) tiền     0 → −22.000 → −30.000  ĐI XUỐNG            ║
║     Fine Cigar     lãi −15.000 → −7.500 → −1.500    LỖ                   ║
║      (thu 0/trả 60)  tiền 30.000 → 75.000 → 105.000  TĂNG  ← "phao nổi"  ║
║                                                                          ║
║  ⚠️ CH.15 IN ĐẢO DẤU CẢ HAI BẢNG CHO NHAU                                ║
║     tự kiểm: đọc đoạn văn trên/dưới bảng — chúng nói ngược lại bảng      ║
║     chốt hạ: lời giới thiệu Alphabooks (PDF tr.3) kể lại với dấu ĐÚNG    ║
║                                                                          ║
║  ⭐ CÁI GIÁ CỦA TĂNG TRƯỞNG — vốn tối thiểu, hình chữ U                  ║
║      0%/tháng → 76.000    (lỗ mãi mãi: doanh thu < 25.000 hoà vốn)       ║
║     10%/tháng → 40.485    ← rẻ nhất                                      ║
║     50%/tháng → 55.750    (lãi 89,8 triệu mà vẫn cần vốn đệm)            ║
║                                                                          ║
║     rút DSO 30 ngày cứu 29.539  ·  nới DPO 30 ngày cứu 19.539            ║
║     tỷ số = 1 / tỷ lệ giá vốn   (đúng chính xác khi tăng trưởng = 0)     ║
║                                                                          ║
║  💼 HAI BỆNH, HAI BÁC SĨ                                                 ║
║     có lãi + thiếu tiền  →  CHUYÊN GIA TÀI CHÍNH  (huy động vốn)         ║
║     có tiền + không lãi  →  CHUYÊN MÔN HOẠT ĐỘNG  (cắt phí, tăng thu)    ║
║                                                                          ║
║  🇻🇳 tiền từ HĐKD ÷ lợi nhuận:  công ty mẫu 2,01  ·  Vinamilk 1,12        ║
║     nhưng 2,01 có ~một nửa đến từ BÁN BỚT TỒN KHO — chỉ được một lần     ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần IV — Tiền mặt là nhất**, PDF tr. 108–140.
    - Ch. 14 *Tiền mặt là một phép kiểm tra thực tế*, PDF tr. 109–112
      — trích Ram Charan và Jerry Useem, *Fortune*, tháng 5/2002 (tr. 109);
      Buffett và ba quy tắc, tăng trưởng 17,9% từ 1/1994 đến 1/2004 (tr. 109);
      định nghĩa **thu nhập chủ sở hữu** (tr. 109);
      *"ít chịu tác động của nghệ thuật tài chính nhất"* (tr. 110);
      chuyện Joe và cuộc gọi của ngân hàng (tr. 111–112)
    - Ch. 15 *Lợi nhuận ≠ tiền mặt (Và ta cần cả hai)*, PDF tr. 113–120
      — ba lý do (tr. 113); **Sweet Dreams Bakery** (tr. 114–116);
      *"đây chính xác là những gì sẽ đẩy các doanh nghiệp có tiềm năng lợi nhuận đi đến chỗ phá sản"* (tr. 116);
      **Fine Cigar** (tr. 117–118); *"tấm khiên bảo vệ"* (tr. 118);
      hai loại chuyên môn (tr. 119); **Setpoint** và quyết định về thời điểm (tr. 120);
      *"các doanh nghiệp cần cả lợi nhuận và tiền mặt"* (tr. 120)
  - Lời giới thiệu của Alphabooks, PDF tr. 3 — ví dụ Sweet Dreams quy ra VND, **dấu đúng**
  - Ch. 4 *Lợi nhuận chỉ là dự toán*, PDF tr. 38 — **nguyên tắc phù hợp**
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 3 và mục 9
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán cho năm
  kết thúc 31/12/2024, lập theo IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 9](#9--đối-chiếu-việt-nam--vinamilk-2024).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py`](../thuc_hanh/bai-06-loi-nhuan-khac-tien-mat.py):
  - cả hai ví dụ Sweet Dreams và Fine Cigar được tái dựng bằng mô hình **theo ngày** và chốt bằng
    `assert` — lợi nhuận −2.000/+2.000/+8.000 và tiền 0/−22.000/−30.000; lợi nhuận −15.000/−7.500/−1.500
    và tiền 30.000/75.000/105.000. Cả sáu con số tiền mặt **khớp đúng bản in của sách**; chỉ các con
    số **lợi nhuận** là lệch, và lệch đúng ở dấu.
  - capex 205 = khấu hao 239 + thay đổi PPE (−34), chốt bằng `assert`.
  - quan hệ *"tỷ số = 1 / tỷ lệ giá vốn ở tăng trưởng 0"* được kiểm ở **bốn** mức tỷ lệ giá vốn.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - ⭐ Toàn bộ [mục 7](#7-cái-giá-của-tăng-trưởng--phép-tính-sách-không-làm) — chạy 24 tháng, đường cong
    chữ U, bản đồ DSO × DPO — **sách không làm**. Sách dừng ở tháng 3 và chỉ kết luận bằng lời.
  - Mô hình mô phỏng **theo ngày** là do bài này dựng. Sách chỉ tính tay theo tháng với điều khoản
    30/60 ngày. Mô hình tái dựng đúng cả hai ví dụ, nhưng **mọi con số ngoài ba tháng đầu là ngoại suy**,
    không phải số liệu của sách.
  - Bảng "đơn thuốc" ở [mục 8](#8--góc-quản-trị--hai-bệnh-hai-bác-sĩ) do bài này dựng; sách chỉ nêu
    khung "hai loại chuyên môn" bằng lời, không đặt con số.
  - Cụm **"chết vì tăng trưởng"** và **"tỷ lệ chuyển lợi nhuận thành tiền"** không có trong sách.
  - [Mục 9 — Đối chiếu Việt Nam](#9--đối-chiếu-việt-nam--vinamilk-2024) hoàn toàn nằm ngoài sách.
- **Liên hệ chéo:**
  - [Bài 0 mục 3](bai_00_bat_dau_tu_dau.md#3-ba-báo-cáo-tài-chính-trong-một-trang) — ba báo cáo khoá vào nhau thế nào.
  - [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) — đọc báo cáo lưu chuyển tiền tệ, và tính **thu nhập chủ sở hữu**.
  - Bài 11 — DSO, DPO và chu kỳ chuyển đổi tiền mặt, làm nghiêm túc.
  - Giá trị hiện tại và lãi kép (dùng ở mục 2):
    [EG14 bài 5](../../eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).

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
| **6** | **Lợi nhuận ≠ tiền mặt** ← *bạn đang ở đây* | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
