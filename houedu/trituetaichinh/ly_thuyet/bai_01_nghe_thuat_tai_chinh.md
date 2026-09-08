# Bài 1 — Nghệ thuật tài chính

> Bài học dựng từ **Phần I — Nghệ thuật tài chính (và tại sao nghệ thuật tài chính lại quan trọng)**:
> chương 1 *Không phải lúc nào cũng có thể tin tưởng các con số* (PDF tr. 9–15), chương 2 *Xác định
> các giả định, ước tính, và định kiến* (PDF tr. 16–22), chương 3 *Tại sao phải tăng cường trí tuệ
> tài chính?* (PDF tr. 23–31), và hộp công cụ *Nhận về những gì bạn mong muốn* (PDF tr. 32–34).
> 🎯 **Vòng 1.** Đây là bài đặt nền cho mười một bài còn lại. Nó không dạy một con số nào —
> nó dạy **thái độ** khi nhìn con số.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 0](bai_00_bat_dau_tu_dau.md) — ba báo cáo tài chính và công ty mẫu.
> ⚙️ **Code:** [`thuc_hanh/bai-01-nghe-thuat-tai-chinh.py`](../thuc_hanh/bai-01-nghe-thuat-tai-chinh.py)

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vấn đề mà cả cuốn sách xoay quanh](#1-vấn-đề-mà-cả-cuốn-sách-xoay-quanh)
- [2. Vì sao con số buộc phải "mềm"](#2-vì-sao-con-số-buộc-phải-mềm)
- [3. Bảy chỗ con số có thể nhảy — mà không ai phạm luật](#3-bảy-chỗ-con-số-có-thể-nhảy--mà-không-ai-phạm-luật)
- [4. Cứng hay mềm](#4-cứng-hay-mềm)
- [5. 📚 Ba con số của Phần I — kiểm lại](#5--ba-con-số-của-phần-i--kiểm-lại)
- [6. 💼 Góc quản trị — ai thật sự ra quyết định](#6--góc-quản-trị--ai-thật-sự-ra-quyết-định)
- [7. 📚 Hộp công cụ — nhận về những gì bạn mong muốn](#7--hộp-công-cụ--nhận-về-những-gì-bạn-mong-muốn)
- [8. 🇻🇳 Đối chiếu Việt Nam](#8--đối-chiếu-việt-nam)
- [9. Tự thử](#9-tự-thử)
- [10. Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
- [11. Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vấn đề mà cả cuốn sách xoay quanh

Sách mở đầu bằng các vụ gian lận, nhưng **gian lận không phải chủ đề của nó**. Chương 1 dẫn vài vụ
để bạn thấy vùng ngoài rìa — công ty phần mềm gửi *"những thùng các-tông rỗng ngay trước khi kết
quý"* (khách trả lại, nhưng lúc đó đã sang quý khác) — rồi lập tức chuyển hướng:

> *"…nhiều doanh nghiệp có những cách đánh bóng sổ sách **hoàn toàn hợp pháp**. Tuy vậy, những công
> cụ hợp pháp này không mạnh bằng những mánh khóe gian lận thẳng tay: chúng không thể làm cho một
> công ty phá sản trông như một công ty ăn nên làm ra… **Nhưng những gì chúng có thể làm được thật
> đáng kinh ngạc.**"* — ch. 1 · PDF tr. 9

⭐ Đó là câu luận đề của cả Phần I, và của cả khoá học này. **Chủ đề không phải kẻ gian, mà là vùng
xám hợp pháp** — nơi không ai phạm luật mà con số vẫn nhảy.

Sách đoán trước phản ứng của người đọc, và nói thẳng ra hộ:

> *"Mọi hoạt động khác trong công việc kinh doanh — như marketing, nghiên cứu và phát triển, quản lý
> nhân sự, xây dựng chiến lược — đều mang tính chủ quan thấy rõ… Vậy còn tài chính? Và cả kế toán
> nữa? **Chắc chắn các con số mà những bộ phận này tạo ra đều khách quan, trắng đen rõ ràng, miễn
> bàn cãi.**"* — ch. 1 · PDF tr. 9

Rồi bác bỏ nó bằng một câu mà đáng nhớ nguyên văn:

> *"**Tài chính — kế toán không phải là thực tế, mà là phản ánh thực tế**, và tính chính xác của sự
> phản ánh đó phụ thuộc vào năng lực của kế toán viên và chuyên gia tài chính trong việc đưa ra
> những giả định và ước tính hợp lý."* — ch. 1 · PDF tr. 10

---

## 2. Vì sao con số buộc phải "mềm"

Không phải vì kế toán viên lười hay bất lương. Sách đưa ra lý do có tính cấu trúc — họ **không thể
biết**:

> *"…ngay cả những người đang kiểm soát các con số cũng không thể biết hết mọi điều. Họ không thể
> biết chính xác mỗi ngày các thành viên trong doanh nghiệp làm gì, thế nên họ không biết chính xác
> phải phân bổ chi phí ra sao. Họ không thể biết chính xác một thiết bị sẽ hoạt động trong bao lâu,
> thế nên họ không biết phải ghi nhận mức khấu hao là bao nhiêu…"* — ch. 1 · PDF tr. 10

```
   Kế toán viên phải trả lời những câu hỏi KHÔNG CÓ CÂU TRẢ LỜI ĐÚNG:

      · Lương quản đốc nhà máy thuộc giá vốn hay chi phí hoạt động?
      · Chiếc máy này dùng được mấy năm?
      · Hợp đồng gói máy + bảo trì: bao nhiêu phần là máy?
      · Doanh nghiệp kia đáng giá bao nhiêu?

   ⟹  họ phải GIẢ ĐỊNH và ƯỚC TÍNH
   ⟹  kết quả là một ĐỊNH KIẾN — con số nghiêng về một hướng
```

⚠️ **Từ "định kiến" ở đây không phải lời buộc tội.** Sách dừng lại hẳn một đoạn để nói rõ, và đây là
chỗ người đọc hay hiểu sai nhất:

> *"Xin các bạn đừng hiểu lầm rằng chúng tôi sử dụng từ 'định kiến' để công kích sự liêm chính của
> bất kỳ ai. (Trong số những người bạn thân thiết của chúng tôi, có nhiều người cũng là kế toán và
> một trong hai chúng tôi, Joe, thực chất còn có chức danh CFO trên danh thiếp). Ở giác độ liên quan
> đến kết quả tài chính, **'định kiến' chỉ có nghĩa là các con số có thể nghiêng theo hướng này hoặc
> hướng kia**."* — ch. 1 · PDF tr. 10

Chương 2 biến điều đó thành **bốn câu hỏi**. Đây là công cụ dùng được ngay, và nó lặp lại suốt cả
khoá học:

```
   ①  Con số này chứa những GIẢ ĐỊNH gì?
   ②  Có ƯỚC TÍNH nào trong nó không?
   ③  Những giả định và ước tính đó dẫn đến ĐỊNH KIẾN gì?
   ④  Chúng có TÁC ĐỘNG như thế nào?
```

---

## 3. Bảy chỗ con số có thể nhảy — mà không ai phạm luật

Sách kể bảy trường hợp bằng lời, rải khắp ba chương, và **không đặt con số cho trường hợp nào**.
Dưới đây là cả bảy, đặt số lên **cùng một doanh nghiệp** — công ty mẫu ở phụ lục.

### ① Khi nào thì doanh thu là doanh thu

Chương 1 liệt kê bốn thời điểm có thể ghi nhận: **khi ký hợp đồng · khi bàn giao · khi gửi hoá đơn ·
khi được thanh toán**. Rồi bẫy người đọc: *"Nếu bạn cho rằng đó là 'khi sản phẩm hoặc dịch vụ được
bàn giao,' thì bạn đã lầm."*

Ví dụ của sách: máy photocopy giao tháng Mười, kèm hợp đồng bảo trì chạy 12 tháng sau đó, cả gói
12.000 đô-la. Ghi vào tháng Mười bao nhiêu?

| Cách chia gói | Tháng 10 | 12 tháng sau |
| --- | ---: | ---: |
| toàn bộ là tiền máy, bảo trì miễn phí | **12.000** | 0 |
| máy 75% / bảo trì 25% | 9.250 | 2.750 |
| máy 50% / bảo trì 50% | 6.500 | 5.500 |
| toàn bộ tính dần theo 12 tháng sử dụng | **1.000** | 11.000 |

⭐ Cùng một hợp đồng, cùng một khách hàng, cùng một số tiền — doanh thu tháng Mười chạy từ 1.000 đến
12.000, **gấp 12 lần**. Sách gọi việc chia gói đó là *"phán đoán chủ quan đáng kể"*.

### ② Xerox — vì sao phải ghi trước ngày càng nhiều

Xerox bán thiết bị theo hợp đồng thuê **bốn năm** gồm cả dịch vụ và bảo trì, rồi *"quyết định ghi
nhận trước **tỷ lệ phần trăm tiếp tục tăng** của doanh thu ước tính"*. Kết cục: bị phát hiện ghi sai
**6 tỷ đô-la**.

Mấy chữ *"tiếp tục tăng"* là chỗ đáng dừng lại. Vì sao không ghi trước một lần rồi thôi? Mô phỏng:
mỗi năm ký được 100 triệu hợp đồng 4 năm, số hợp đồng mới **không đổi**:

| Năm | Trải đều 4 năm | Ghi trước 100% | Chênh lệch |
| ---: | ---: | ---: | ---: |
| 1 | 25,0 | 100,0 | **+75,0** |
| 2 | 50,0 | 100,0 | +50,0 |
| 3 | 75,0 | 100,0 | +25,0 |
| 4 | 100,0 | 100,0 | **0,0** |
| 5 | 100,0 | 100,0 | 0,0 |

⭐ Đến năm 4 hai cách **bằng nhau**. Ghi trước chỉ "thắng" ở ba năm đầu, và chỉ khi lượng hợp đồng
mới còn tăng. Một khi nó chững lại, lợi thế bay hết — và doanh nghiệp phải ghi trước **mạnh hơn nữa**
để giữ đà. Đó chính là *"tỷ lệ phần trăm tiếp tục tăng"*. **Đây là một vòng xoáy, không phải một thủ
thuật dùng một lần** — và nó giải thích vì sao những vụ như Xerox luôn kết thúc bằng sụp đổ chứ
không phải bằng hạ cánh mềm.

### ③ WorldCom — chuyển chi phí hoạt động thành chi phí đầu tư

Đây là trường hợp đáng học nhất, vì cơ chế của nó cực kỳ đơn giản:

```
   chi phí HOẠT ĐỘNG   →  trừ NGAY vào lợi nhuận kỳ này
   chi phí ĐẦU TƯ      →  nằm ở bảng cân đối; chỉ phần KHẤU HAO vào báo cáo KQKD
```

Sách trích cáo trạng của Bộ Tư pháp: WorldCom đẩy lợi nhuận *"bằng đủ loại thủ đoạn kế toán, bao gồm
khai bớt chi phí và **xếp các chi phí hoạt động vào chi phí đầu tư cơ bản**"*.

Áp lên công ty mẫu — chuyển X triệu từ SG&A (1.061) sang tài sản, khấu hao đều trong 5 năm:

| | LN gộp | EBIT | LN thuần | Biên gộp |
| --- | ---: | ---: | ---: | ---: |
| nguyên trạng (báo cáo thật) | 1.933 | 652 | 248 | 22,2% |
| chuyển 50 triệu | 1.933 | 692 | 270 | 22,2% |
| **chuyển 100 triệu** | 1.933 | **732** | **291** | 22,2% |
| chuyển 200 triệu | 1.933 | 812 | 334 | 22,2% |

Chỉ một bút toán phân loại lại 100 triệu: EBIT **+12,3%**, lợi nhuận thuần **+17,4%**.

⚠️ **Nhưng tiền mặt thì không nhúc nhích một đồng nào.** Khoản 100 triệu vẫn rời khỏi tài khoản ngân
hàng y hệt như trước. Nó chỉ đổi **chỗ đứng** trên báo cáo lưu chuyển tiền tệ:

```
   tiền từ hoạt động kinh doanh    498  →  598    (+100, trông khoẻ hơn)
   tiền từ hoạt động đầu tư       −205  → −305    (−100)
   ───────────────────────────────────────────────────────
   thay đổi trong tiền mặt              KHÔNG ĐỔI
```

⭐ Đây chính là lý do Buffett nhìn tiền mặt ([bài 6](bai_06_loi_nhuan_khac_tien_mat.md)). Thủ thuật
này bôi trơn được hai báo cáo đầu, nhưng dòng cuối cùng thì không.

### ④ Hàng không — tự quyết mức khấu hao

Sách kể: các hãng hàng không *"nhận ra rằng máy bay của họ có tuổi đời hoạt động lâu hơn dự kiến"*,
nên kế toán đổi bảng khấu hao. *"Lợi nhuận ngành tăng đáng kể."*

Công ty mẫu có tài sản 2.230 và khấu hao 239, tức tuổi đời ngầm định khoảng **9,3 năm**. Kéo dài nó:

| Tuổi đời giả định | Khấu hao | EBIT | LN thuần |
| --- | ---: | ---: | ---: |
| 9,3 năm *(nguyên trạng)* | 239 | 652 | 248 |
| 12 năm | 186 | 705 | 277 |
| 15 năm | 149 | 742 | 297 |
| 20 năm | 112 | 780 | **317** |

⭐ Kéo tuổi đời từ 9,3 lên 20 năm làm lợi nhuận thuần **tăng 28%**. Không bán thêm một món hàng nào.
Không cắt một đồng chi phí nào. Chỉ là một phán đoán về việc máy bay bay được bao lâu.

⚠️ **Và phán đoán đó có thể đúng.** Sách không nói các hãng hàng không gian lận — máy bay **thật sự**
bền hơn dự kiến. Điểm của sách tinh tế hơn: một phán đoán hợp lý vẫn là một phán đoán, và nó kéo
theo hệ quả — *"nhà đầu tư quyết định mua nhiều cổ phiếu hơn, các vị giám đốc điều hành của các hãng
hàng không tính toán thấy khả năng có thể tăng lương hậu hĩnh hơn."*

### ⑤ Phân bổ lương — "định kiến nhân đôi"

Chương 2 hỏi: lương của bạn tháng Sáu nên tính vào **giá thành sản phẩm** hay **chi phí phát triển**?
Chuyển 100 triệu trên công ty mẫu:

| | LN gộp | EBIT | LN thuần | Biên gộp |
| --- | ---: | ---: | ---: | ---: |
| nguyên trạng | 1.933 | 652 | 248 | 22,2% |
| giá vốn → chi phí phát triển | 2.033 | **652** | **248** | 23,4% |
| chi phí phát triển → giá vốn | 1.833 | **652** | **248** | 21,1% |

⭐ **Cột EBIT và LN thuần không đổi một đồng nào.** Chỉ biên lợi nhuận gộp nhảy, từ 21,1% đến 23,4%.

Vậy thì sao? Sách trả lời bằng thuật ngữ **"định kiến nhân đôi"**:

```
   ①  chi phí phát triển CAO hơn
      → "hoạt động phát triển sản phẩm quá đắt đỏ, không nên mạo hiểm thêm"
      → CẮT R&D, hại tương lai doanh nghiệp

   ②  giá thành sản phẩm THẤP hơn
      → sản phẩm trông dễ sinh lời
      → ĐỊNH GIÁ QUÁ THẤP, và TUYỂN THÊM người để làm một thứ thật ra không lãi như vẻ
```

⚠️ Đây là chỗ nguy hiểm nhất của cả Phần I: **một bút toán không làm đổi lợi nhuận của công ty, nhưng
làm đổi hai quyết định lớn.** Nếu chỉ nhìn dòng cuối, bạn sẽ không thấy gì cả.

### ⑥ Ba phương pháp định giá, ba câu trả lời

Sách nêu ba phương pháp — **tỷ suất giá trên lợi nhuận**, **chiết giảm dòng tiền**, **định giá tài
sản** — nói *"mỗi phương pháp đều có một định kiến đưa đến những kết quả khác nhau"*, rồi dừng. Đặt
số vào, định giá chính công ty mẫu:

| Phương pháp | Giá trị |
| --- | ---: |
| Tài sản — vốn chủ sở hữu sổ sách | **2.457** ← thấp nhất |
| P/E, bội số 10 | 2.480 |
| DCF, chiết khấu 12% / tăng trưởng 3% | 3.256 |
| DCF, chiết khấu 10% / tăng trưởng 2% | 3.662 |
| P/E, bội số 15 | 3.720 |
| DCF, chiết khấu 8% / tăng trưởng 2% | 4.883 |
| P/E, bội số 20 | **4.960** ← cao nhất |

⭐ Cùng một doanh nghiệp, cùng một ngày, cùng một bộ báo cáo — **chênh nhau 2,0 lần**. Và **không con
số nào trong bảng là sai**.

⚠️ Người **bán** sẽ trích con số cao nhất. Người **mua** sẽ trích con số thấp nhất. Cả hai đều đang
dùng một phương pháp được thừa nhận. Sách chốt: *"phần lớn khía cạnh nghệ thuật ở đây nằm ở việc
**lựa chọn** phương pháp định giá."*

### ⑦ Joe và chiếc máy tính 5.000 đô-la

Chương 3 kể Joe *"thích kể với khán giả rằng anh là một chuyên gia tài chính kỳ cựu, và anh có thể
dễ dàng đưa ra một phân tích cho thấy rõ rằng công ty **nên** mua một chiếc máy tính có giá 5.000
đô-la"* — chỉ bằng cách giả định tiết kiệm một giờ mỗi ngày.

| Bộ giả định | Lợi ích/năm | ROI năm 1 |
| --- | ---: | ---: |
| Joe: tiết kiệm 1 giờ/ngày | 10.000 | **+200%** |
| Joe thận trọng hơn: 30 phút/ngày | 5.000 | +100% |
| cấp trên: +1 giờ nhưng **mất** 1 giờ lướt web | 0 | 0% |
| cấp trên bi quan: mất nhiều hơn được | −2.500 | **−50%** |

*(Sách không đặt con số cho lương. Bảng này dùng 40 đô-la/giờ và 250 ngày làm việc.)*

Phản biện của cấp trên là câu hay nhất chương 3: Joe có thể **mất** một giờ mỗi ngày *"vì giờ đây anh
có thể dễ dàng lướt web và tải nhạc về nghe."*

💼 Bài học không phải "đừng tin đề xuất của người khác". Mà là: **mọi đề xuất ROI đều có một giả định
chịu trách nhiệm cho phần lớn kết quả.** Việc của bạn là tìm ra nó.

---

## 4. Cứng hay mềm

Sách gói cả Phần I vào một câu, và đây là câu đáng thuộc:

> *"Có trí tuệ tài chính nghĩa là hiểu được khi nào các con số là **'cứng'** — có căn cứ chắc chắn và
> tương đối ít gây tranh cãi, và lúc nào chúng **'mềm'** — tức là, phụ thuộc nhiều vào các phán đoán
> chủ quan."* — ch. 1 · PDF tr. 12

Xếp lại bảy trường hợp trên theo độ cứng:

| Khoản mục | Độ cứng | Vì sao |
| --- | :---: | --- |
| Tiền trong tài khoản | **CỨNG** | ngân hàng xác nhận được |
| Vốn chủ sở hữu sổ sách | cứng | cộng trừ từ các dòng khác |
| Giá vốn hàng bán | mềm | ranh giới với chi phí hoạt động là phán đoán — ⑤ |
| Khấu hao | **MỀM** | phụ thuộc tuổi đời tài sản — ④ |
| Doanh thu kỳ này | **MỀM** | phụ thuộc thời điểm ghi nhận — ①② |
| Chi phí đầu tư hay hoạt động | **MỀM** | ranh giới là quy tắc nội bộ — ③ |
| Giá trị doanh nghiệp | **RẤT MỀM** | chênh 2 lần tuỳ phương pháp — ⑥ |

⭐ Chú ý: **không dòng nào trong bảng là gian lận.** Sách vạch ranh giới rất rõ:

> *"…**không cần phải 'xào nấu' sổ sách**, người ta luôn có thể tìm ra nhiều kẽ hở để làm cho các con
> số trông có vẻ thế này hoặc thế khác."* — ch. 1 · PDF tr. 11

---

## 5. 📚 Ba con số của Phần I — kiểm lại

| Sách nói | Kiểm |
| --- | --- |
| Giám đốc các doanh nghiệp Fortune 500 làm bài kiểm tra hiểu biết tài chính, **đúng trung bình 32%** | tức **sai 68%** — và đây là **giám đốc**, không phải nhân viên mới |
| Tyco mua **600 công ty trong 2 năm**, *"mỗi ngày làm việc mua ít nhất một công ty"* | 2 × 52 × 5 = 520 ngày làm việc; 600/520 = **1,15 công ty/ngày** ✓ sách nói đúng, và còn nói giảm |
| Lợi thế thương mại: mua công ty tài sản thuần 1 triệu với giá 3 triệu → ghi **2 triệu** | ✓ khớp |

📚 Con số thứ ba đáng nhớ hơn vẻ ngoài của nó. **Lợi thế thương mại là tài sản không cầm nắm được** —
không bán lại được lúc cấp thiết. Đó chính là lý do sách nêu: khi Tyco mua 600 công ty, lợi thế
thương mại trên bảng cân đối *"tăng cao đến mức khiến các ngân hàng bắt đầu lo ngại"*, và họ buộc
Tyco dừng mua lại. Chiến lược của công ty bị chặn bởi **một dòng trên bảng cân đối kế toán**.

---

## 6. 💼 Góc quản trị — ai thật sự ra quyết định

Chương 3 có một cảnh báo mà hầu như không sách tài chính nào nói thẳng như vậy:

> *"Nếu thiếu đi những kiến thức như vậy, điều gì sẽ xảy ra? Rất đơn giản: **người của bộ phận tài
> chính kế toán sẽ điều khiển các quyết định.** Chúng tôi sử dụng từ 'điều khiển' là vì khi các quyết
> định được đưa ra dựa trên các con số, và khi các con số lại dựa trên các giả định và ước tính của
> kế toán viên, thì các kế toán viên và nhân viên tài chính đã nắm quyền điều khiển có hiệu lực
> (**ngay cả khi họ chẳng cố ý điều khiển thứ gì**)."* — ch. 3 · PDF tr. 27

Mấy chữ trong ngoặc mới là điểm chính. Đây **không** phải thuyết âm mưu về phòng tài chính. Đó là hệ
quả cơ học: ai đặt giả định, người đó lái quyết định — dù không hề muốn.

### 💼 Câu hỏi "trong bao lâu và ở nhiệt độ nào?"

Ví dụ hay nhất trong Phần I, và là thứ mang đi họp được ngay. Ở Ford Motor, Joe và nhóm tài chính
trình bày kết quả cho một giám đốc marketing cấp cao. Ông này nhìn thẳng vào họ:

> *"Trước khi tôi mở những báo cáo tài chính này ra, tôi cần biết… **trong bao lâu và ở nhiệt độ
> nào?**"* — ch. 3 · PDF tr. 27

Joe hiểu ra và đáp: *"Vâng thưa sếp, chúng được xử lý trong hai tiếng đồng hồ ở 350 độ."* Vị giám đốc
nói: *"Tốt, giờ thì tôi đã biết các anh xử lý chúng bao lâu. Chúng ta bắt đầu nào."*

⭐ Cách đùa ấy làm được ba việc cùng lúc, và đó là lý do nó đáng học:

1. nói cho phòng tài chính biết ông **hiểu** có giả định trong đó — nên đừng giấu;
2. mở đường để hỏi *"con số này chắc chắn đến đâu?"* mà **không** thành ra buộc tội ai;
3. kết quả: nhóm tài chính *"yên tâm giải thích nguồn gốc của con số"*, và ông ra quyết định **có
   cảm giác yên tâm**.

Sau đó ông vẫn **dùng** các con số ấy. Mục tiêu chưa bao giờ là bác bỏ báo cáo — mà là biết mình đang
đứng trên nền gì.

### ❓ Bốn câu mang đi hỏi phòng tài chính

Bốn câu hỏi của chương 2, viết lại thành thứ hỏi được trong một cuộc họp thật:

1. **Con số này có giả định gì?** — *"Khấu hao dòng thiết bị này đang tính theo mấy năm, và lần gần
   nhất con số đó được xem lại là khi nào?"*
2. **Có ước tính nào không?** — *"Phần chi phí chung phân bổ vào sản phẩm của tôi tính theo cơ sở gì
   — theo doanh thu, theo đầu người, hay theo giờ máy?"*
3. **Định kiến đi về hướng nào?** — *"Nếu đổi cơ sở phân bổ đó, biên lợi nhuận gộp của tôi tăng hay
   giảm?"*
4. **Tác động là gì?** — *"Có quyết định nào — giá bán, tuyển dụng, ngân sách — đang dựa trên chính
   con số này không?"*

⚠️ Chương 3 liệt kê **bốn rào cản** sẽ gặp, và đoán trước cả cái khó chịu nhất: *"cấp trên không muốn
bạn đặt câu hỏi về các con số"*. Lời khuyên của sách là **cứ tiếp tục** — vì thường thì chính cấp
trên cũng đang lo lắng về kiến thức tài chính của mình.

Còn rào cản đầu tiên thì sách gạt đi rất gọn:

> *"Có thể một rào cản trong số đó là bạn ghét toán, sợ toán… Bạn có thể ngạc nhiên khi biết, **phần
> lớn các hoạt động tài chính chỉ liên quan đến phép cộng và phép trừ.** Khi dân tài chính thực sự
> hứng thú, họ mới thực hiện phép nhân và phép chia."* — ch. 3 · PDF tr. 29

---

## 7. 📚 Hộp công cụ — nhận về những gì bạn mong muốn

Hộp công cụ cuối Phần I (PDF tr. 32–34) đổi giọng hẳn: từ *"hiểu con số"* sang *"dùng con số cho
chính mình"*.

**Khi xin tăng lương**, sách gợi ý mang theo ba thứ: tăng trưởng doanh thu và cải thiện biên lợi
nhuận năm qua · những thách thức tài chính còn tồn đọng mà bạn có thể góp phần gỡ · và tình trạng
tiền mặt — *"dòng tiền tự do của công ty đủ để tăng lương cho những nhân viên mẫn cán."*

**Khi đi phỏng vấn**, hỏi ngược lại nhà tuyển dụng bốn câu:

```
   Công ty có sinh lợi không?
   Nguồn vốn của công ty có dương không?
   Hệ số thanh toán ngắn hạn có thể hỗ trợ quỹ lương không?
   Doanh thu đang tăng hay giảm?
```

⭐ Câu thứ ba là câu sắc nhất, và nó nối thẳng tới [bài 6](bai_06_loi_nhuan_khac_tien_mat.md): nó
không hỏi công ty **có lãi** không, mà hỏi công ty **có trả nổi lương** không. Hai câu hỏi khác nhau.

📚 Hộp này cũng giới thiệu **ba người giữ tiền**, và phân biệt của sách rất gọn:

| Chức danh | Nhìn ra ngoài hay vào trong | Việc chính |
| --- | --- | --- |
| **Giám đốc tài chính** (CFO) | cả hai | quản lý và chiến lược tài chính; kế toán trưởng và thủ quỹ báo cáo cho người này |
| **Thủ quỹ** (treasurer) | **ra ngoài** | quan hệ ngân hàng, quản lý dòng tiền, cơ cấu vốn, quan hệ đầu tư |
| **Kế toán trưởng** (controller) | **vào trong** | báo cáo tài chính chính xác, kiểm soát nội bộ, phân tích kinh doanh |

💼 Biết ai làm gì là biết **hỏi ai**. Câu hỏi về khấu hao và phân bổ chi phí → kế toán trưởng. Câu hỏi
về ngưỡng thu hồi vốn và tiền có sẵn để đầu tư → thủ quỹ.

---

## 8. 🇻🇳 Đối chiếu Việt Nam

Sách viết theo GAAP của Mỹ. Ranh giới hợp pháp ở Việt Nam do khung khác quy định — nhưng **khoảng
trống phán đoán thì không biến mất**, vì nó bắt nguồn từ chỗ *"kế toán viên không thể biết hết mọi
điều"*, chứ không phải từ chỗ luật lỏng.

Bằng chứng đo được, và nó nằm sẵn trong kho này: **Vinamilk công bố song song hai bộ báo cáo cho cùng
năm 2024** — một theo VAS, một theo IFRS. Tổng tài sản theo IFRS là **56.993 tỷ đồng**; con số VAS mà
báo chí trích thì khác. Cùng một công ty, cùng một ngày, hai con số.

⚠️ Đó **không phải lỗi của ai**, và cũng không phải hai bộ sổ. Đó đúng là điều chương 1 mô tả: *"tài
chính — kế toán không phải là thực tế, mà là phản ánh thực tế"* — và khi đổi khung phản ánh thì hình
ảnh đổi theo.

💼 Hệ quả thực dụng cho người đọc báo cáo ở Việt Nam:

- **Luôn hỏi báo cáo lập theo khung nào** trước khi so sánh hai doanh nghiệp. So một công ty báo cáo
  IFRS với một công ty báo cáo VAS là so hai thước đo khác nhau.
- **Đọc thuyết minh, không chỉ đọc bảng.** Chính sách khấu hao, chính sách ghi nhận doanh thu và cơ
  sở phân bổ chi phí đều nằm ở đó — và đó chính là ①④⑤ của mục 3.
- **Chú ý các con số "mềm" nhất trước.** Theo bảng ở mục 4: doanh thu kỳ này, khấu hao, ranh giới
  đầu tư/hoạt động, và giá trị doanh nghiệp.

📚 Sách có nhắc một thứ hoàn toàn của Mỹ mà Việt Nam không có tương đương trực tiếp: **Sarbanes-Oxley**
(2002), đạo luật ra đời để đáp lại chính những vụ Enron và WorldCom trong bài này. Nó ở hộp công cụ
cuối sách — bài 12.

---

## 9. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-01-nghe-thuat-tai-chinh.py`](../thuc_hanh/bai-01-nghe-thuat-tai-chinh.py) rồi chạy
lại. Không có lời giải.

1. **Ngưỡng WorldCom.** Ở ③, tìm số tiền X nhỏ nhất cần chuyển từ SG&A sang tài sản để lợi nhuận
   thuần vượt **300 triệu**. X đó bằng bao nhiêu phần trăm SG&A? Con số ấy có đủ nhỏ để lọt qua mắt
   một kiểm toán viên không?

2. **Khấu hao ngược chiều.** Ở ④, thử **rút ngắn** tuổi đời xuống 5 năm. Lợi nhuận thuần còn bao
   nhiêu? Doanh nghiệp nào lại **muốn** làm điều đó, và trong hoàn cảnh nào?

3. **Hai thủ thuật cộng dồn.** Áp đồng thời ③ (chuyển 100 triệu) và ④ (tuổi đời 20 năm). Lợi nhuận
   thuần thành bao nhiêu? So với 248 gốc là **mấy lần**? Tiền mặt đổi bao nhiêu?

4. **Biên gộp mục tiêu.** Ở ⑤, ban giám đốc muốn biên lợi nhuận gộp đạt **25%**. Cần chuyển bao nhiêu
   triệu từ giá vốn sang chi phí hoạt động? Lợi nhuận thuần đổi bao nhiêu?

5. **Khoảng định giá thu hẹp.** Ở ⑥, giả sử bạn thuyết phục được cả hai bên dùng **chỉ** phương pháp
   DCF. Khoảng giá còn chênh mấy lần? Biến nào giờ quyết định tất cả?

6. **Định giá theo tiền, không theo lợi nhuận.** Vẫn ở ⑥, thay dòng tiền tự do 293 bằng lợi nhuận
   thuần 248 trong công thức DCF. Giá đổi bao nhiêu? Vì sao dùng dòng tiền lại **khó bóp méo hơn**?

7. **Điểm hoà của Joe.** Ở ⑦, tìm số **phút** tiết kiệm mỗi ngày để ROI năm 1 đúng bằng 0%. Rồi đổi
   lương giờ từ 40 xuống 20 đô-la — con số phút đó đổi thế nào?

8. **Ghi trước khi doanh thu tăng.** Ở ②, cho lượng hợp đồng mới **tăng 20%/năm** thay vì đứng yên.
   Lợi thế của việc ghi trước có biến mất ở năm 4 nữa không? Điều này nói gì về việc vì sao Xerox
   không thể dừng lại?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Nghệ thuật tài chính | the art of finance | vùng phán đoán mà không quy tắc nào phủ hết |
| Định kiến | bias | con số **nghiêng** về một hướng — **không** hàm ý gian lận |
| Ghi nhận / công nhận doanh thu | revenue recognition | quyết định **khi nào** doanh thu vào sổ |
| Chi phí trả trước | accrual | trải một khoản thu/chi ra nhiều kỳ cho khớp nhau |
| Dự trù chi phí | allocation | phân bổ chi phí chung cho các bộ phận |
| Khấu hao | depreciation | trải chi phí tài sản theo **tuổi đời hữu dụng** |
| Chi phí hoạt động | operating expense | trừ **ngay** vào lợi nhuận kỳ này |
| Chi phí đầu tư cơ bản | capital expenditure | vào bảng cân đối; chỉ khấu hao mới vào báo cáo KQKD |
| Lợi thế thương mại | goodwill | giá mua − tài sản thuần; **không cầm nắm được** |
| Giá trị vốn hoá thị trường | market capitalization | giá cổ phiếu × số cổ phiếu lưu hành |
| Cứng / mềm | hard / soft | con số ít hay nhiều phụ thuộc phán đoán |
| GAAP | generally accepted accounting principles | khung kế toán Mỹ, ~4.000 trang |
| Thủ quỹ | treasurer | nhìn **ra ngoài**: ngân hàng, dòng tiền, cơ cấu vốn |
| Kế toán trưởng | controller | nhìn **vào trong**: báo cáo chính xác, kiểm soát nội bộ |
| 🇻🇳 VAS | Vietnamese Accounting Standards | chuẩn mực kế toán Việt Nam — **không có trong sách** |

---

## 11. Câu hỏi tự kiểm tra

1. Chủ đề của Phần I là gian lận hay là điều gì khác? Trích một câu của sách để chứng minh. (mục 1)
2. *"Tài chính — kế toán không phải là ___, mà là ___ ."* Điền và giải thích. (mục 1)
3. Vì sao con số buộc phải "mềm" — lỗi của kế toán viên, hay lý do có tính cấu trúc? (mục 2)
4. Từ **"định kiến"** trong sách có hàm ý buộc tội không? Sách nói rõ điều đó ở đâu và bằng cách nào? (mục 2)
5. Kể bốn câu hỏi của chương 2. (mục 2)
6. Kể bốn thời điểm có thể ghi nhận doanh thu. Chọn "khi bàn giao" thì đúng hay sai? (mục 3①)
7. Hợp đồng máy photocopy 12.000: doanh thu tháng Mười chạy từ bao nhiêu đến bao nhiêu, **vì sao**? (mục 3①)
8. Xerox ghi trước doanh thu. Vì sao phải ghi trước **ngày càng nhiều** chứ không phải một lần rồi thôi? (mục 3②)
9. Cơ chế của WorldCom là gì? Nêu bằng hai dòng. (mục 3③)
10. Chuyển 100 triệu từ SG&A sang tài sản làm lợi nhuận thuần tăng bao nhiêu phần trăm?
    **Tiền mặt** đổi bao nhiêu? (mục 3③)
11. Vì sao thủ thuật đó bôi trơn được hai báo cáo mà không bôi trơn được báo cáo thứ ba? (mục 3③)
12. Kéo tuổi đời tài sản từ 9,3 lên 20 năm làm lợi nhuận tăng bao nhiêu? Sách có nói hàng không gian lận không? (mục 3④)
13. Chuyển 100 triệu giữa giá vốn và chi phí phát triển: **cái gì đổi, cái gì không đổi**? (mục 3⑤)
14. Giải thích "định kiến nhân đôi". Vì sao nó nguy hiểm dù lợi nhuận không đổi? (mục 3⑤)
15. Ba phương pháp định giá cho khoảng chênh mấy lần trên cùng một công ty? Phương pháp nào cho
    giá cao nhất, thấp nhất? (mục 3⑥)
16. Người mua và người bán mỗi bên sẽ chọn phương pháp nào, và cả hai có ai sai không? (mục 3⑥)
17. ROI chiếc máy tính của Joe chạy từ đâu đến đâu? Giả định nào chịu trách nhiệm? (mục 3⑦)
18. Nêu ba khoản mục **cứng** nhất và ba khoản **mềm** nhất. (mục 4)
19. Có khoản nào trong bảng "cứng/mềm" là gian lận không? (mục 4)
20. Vì sao ngân hàng buộc Tyco dừng mua lại? Dòng nào trên bảng cân đối đã chặn chiến lược của họ? (mục 5)
21. *"Người của bộ phận tài chính kế toán sẽ điều khiển các quyết định"* — mấy chữ nào trong ngoặc
    làm câu này **không** phải thuyết âm mưu? (mục 6)
22. Câu *"trong bao lâu và ở nhiệt độ nào?"* làm được **ba** việc gì cùng lúc? (mục 6)
23. Sau khi đùa xong, vị giám đốc có bác bỏ báo cáo không? Điều đó nói gì về mục tiêu thật sự? (mục 6)
24. Kể bốn rào cản của chương 3. Sách khuyên gì với rào cản "cấp trên không muốn bạn hỏi"? (mục 6)
25. Bốn câu nên hỏi nhà tuyển dụng. Vì sao câu về **hệ số thanh toán ngắn hạn** là sắc nhất? (mục 7)
26. Phân biệt thủ quỹ và kế toán trưởng. Hỏi về chính sách khấu hao thì hỏi ai? (mục 7)
27. Vinamilk 2024 có hai con số tổng tài sản khác nhau. Đó là lỗi, là hai bộ sổ, hay là gì? (mục 8)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 1 — NGHỆ THUẬT TÀI CHÍNH  (ch. 1–3, PDF tr. 9–34)                   ║
╠══════════════════════════════════════════════════════════════════════════╣
║  CHỦ ĐỀ KHÔNG PHẢI GIAN LẬN — mà là VÙNG XÁM HỢP PHÁP                    ║
║  "Không cần phải xào nấu sổ sách, người ta luôn có thể tìm ra nhiều      ║
║   kẽ hở để làm cho các con số trông có vẻ thế này hoặc thế khác."        ║
║                                                                          ║
║  ⭐ "TÀI CHÍNH — KẾ TOÁN KHÔNG PHẢI LÀ THỰC TẾ, MÀ LÀ PHẢN ÁNH THỰC TẾ." ║
║                                                                          ║
║  VÌ SAO MỀM:  kế toán viên KHÔNG THỂ BIẾT hết  →  phải GIẢ ĐỊNH          ║
║                                                  →  sinh ĐỊNH KIẾN       ║
║  ("định kiến" = nghiêng về một hướng, KHÔNG hàm ý gian lận)              ║
║                                                                          ║
║  BỐN CÂU HỎI    ① giả định gì?  ② ước tính nào?                          ║
║                 ③ định kiến hướng nào?  ④ tác động gì?                   ║
║                                                                          ║
║  BẢY CHỖ CON SỐ NHẢY — cùng một công ty mẫu, không chỗ nào phạm luật     ║
║     ① ghi nhận doanh thu    doanh thu tháng 10:  1.000 → 12.000  (12×)   ║
║     ② Xerox ghi trước       lợi thế TAN HẾT ở năm 4 → phải ghi mạnh hơn  ║
║     ③ WorldCom capex        LN thuần 248 → 291 (+17%), TIỀN KHÔNG ĐỔI    ║
║     ④ khấu hao hàng không   tuổi đời 9,3 → 20 năm:  248 → 317  (+28%)    ║
║     ⑤ phân bổ lương         biên gộp 21,1% ↔ 23,4%, LN THUẦN KHÔNG ĐỔI   ║
║     ⑥ ba cách định giá      2.457 → 4.960 triệu  (chênh 2,0 lần)         ║
║     ⑦ máy tính của Joe      ROI +200% → −50%, cùng một chiếc máy         ║
║                                                                          ║
║  CỨNG → MỀM:  tiền · vốn chủ · giá vốn · khấu hao · doanh thu ·          ║
║               ranh giới capex · GIÁ TRỊ DOANH NGHIỆP                     ║
║                                                                          ║
║  💼 "Trong bao lâu và ở nhiệt độ nào?"  — cách hỏi mà không buộc tội ai  ║
║     rồi VẪN DÙNG con số. Mục tiêu là biết mình đứng trên nền gì.         ║
║                                                                          ║
║  ⚠️ Ai đặt giả định, người đó lái quyết định — kể cả khi không cố ý.     ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần I — Nghệ thuật tài chính (và tại sao nghệ thuật tài chính lại quan trọng)**, PDF tr. 9–34.
    - Ch. 1 *Không phải lúc nào cũng có thể tin tưởng các con số*, PDF tr. 9–15
      — thùng các-tông rỗng và Enron (tr. 9); *"những gì chúng có thể làm được thật đáng kinh ngạc"* (tr. 9);
      *"phản ánh thực tế"* (tr. 10); đoạn đính chính nghĩa của từ **định kiến** (tr. 10);
      bốn thời điểm ghi nhận doanh thu và ví dụ máy photocopy (tr. 10–11);
      **Xerox** và 6 tỷ đô-la (tr. 11); ranh giới chi phí đầu tư / chi phí hoạt động và **WorldCom** (tr. 11);
      *"cứng"* và *"mềm"* (tr. 12); các khung định nghĩa **báo cáo kết quả kinh doanh**,
      **chi phí hoạt động**, **chi phí đầu tư cơ bản**
    - Ch. 2 *Xác định các giả định, ước tính, và định kiến*, PDF tr. 16–22
      — bốn câu hỏi (tr. 16); **chi phí trả trước và dự trù chi phí**, ví dụ phân bổ lương và
      *"định kiến nhân đôi"* (tr. 17–19); **khấu hao** và ngành hàng không (tr. 19–20);
      **ba phương pháp định giá** và bong bóng dot-com (tr. 20–22)
    - Ch. 3 *Tại sao phải tăng cường trí tuệ tài chính?*, PDF tr. 23–31
      — giám đốc Fortune 500 đúng 32% (tr. 23); **WorldCom** (tr. 24); **Tyco** 600 công ty và
      **lợi thế thương mại** (tr. 25); Joe và chiếc máy tính 5.000 đô-la (tr. 26–27);
      *"trong bao lâu và ở nhiệt độ nào?"* tại Ford (tr. 27); *"sẽ điều khiển các quyết định"* (tr. 27);
      lợi ích cho tổ chức (tr. 28–29); **bốn rào cản** (tr. 29–31)
    - Hộp công cụ *Nhận về những gì bạn mong muốn*, PDF tr. 32–34
      — xin tăng lương, bốn câu hỏi khi phỏng vấn, và **ba chức danh** CFO / thủ quỹ / kế toán trưởng
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng cho toàn bộ mục 3
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 8](#8--đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-01-nghe-thuat-tai-chinh.py`](../thuc_hanh/bai-01-nghe-thuat-tai-chinh.py):
  - Thuế suất hiệu dụng **suy ngược từ chính báo cáo** của công ty mẫu ($213/461$), và hàm tính lại
    báo cáo được chốt bằng `assert`: không đổi giả định nào thì phải ra đúng 1.933 / 652 / 248.
  - ⑤ chốt bằng `assert` rằng EBIT và lợi nhuận thuần **không đổi** trong khi lợi nhuận gộp thì đổi.
  - Ba con số của mục 5 (32%, Tyco 600/520, lợi thế thương mại 3 − 1) đều tính lại.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - ⭐ **Sách không đặt con số cho bất kỳ trường hợp nào trong bảy trường hợp ở mục 3.** Sách kể bằng
    lời. Mọi con số ở mục 3 là do bài này tính, áp lên công ty mẫu ở phụ lục — trừ hai con số **của
    sách**: Xerox 6 tỷ đô-la và giá máy tính 5.000 đô-la.
  - Mức lương 40 đô-la/giờ và 250 ngày làm việc ở ⑦, các bội số P/E và cặp chiết khấu/tăng trưởng ở
    ⑥, kỳ khấu hao 5 năm ở ③ — đều **do bài này chọn**, sách không nêu.
  - Bảng "cứng / mềm" ở [mục 4](#4-cứng-hay-mềm) do bài này dựng; sách chỉ nêu cặp khái niệm bằng lời.
  - Bốn câu hỏi *"mang đi hỏi phòng tài chính"* ở [mục 6](#6--góc-quản-trị--ai-thật-sự-ra-quyết-định)
    là diễn giải của bài này từ bốn câu hỏi trừu tượng của chương 2.
  - [Mục 8 — Đối chiếu Việt Nam](#8--đối-chiếu-việt-nam) hoàn toàn nằm ngoài sách. Bài **không** dẫn
    con số tổng tài sản theo VAS của Vinamilk vì chưa lấy được bản VAS từ nguồn gốc.
- **Liên hệ chéo:**
  - [Bài 0 mục 5](bai_00_bat_dau_tu_dau.md#5--gaap-vas-và-ifrs--sách-viết-theo-khung-nào) — GAAP 4.000 trang mà vẫn để lại khoảng trống.
  - [Bài 6](bai_06_loi_nhuan_khac_tien_mat.md) — vì sao tiền mặt là con số ít "nghệ thuật" nhất.
  - [Bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) — nguyên tắc phù hợp và ghi nhận doanh thu, làm kỹ.
  - [Bài 3](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) — chi phí, nợ phải trả, và ranh giới
    "trên vạch / dưới vạch".
  - [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) — biên lợi nhuận gộp, thước đo mà ⑤ làm nhiễu.
  - Bài 10 — ngưỡng thu hồi vốn và cách chất vấn một đề xuất ROI như của Joe.

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| **1** | **Nghệ thuật tài chính** ← *bạn đang ở đây* | ch. 1–3 | 🎯 |
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
