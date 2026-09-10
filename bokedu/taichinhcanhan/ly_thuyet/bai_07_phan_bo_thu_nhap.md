# Bài 7 — Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm

> Bài học dựa trên **C2 tr. 18–28** — Unit 2, Lesson 2 đến Lesson 5 của *Tài chính cá nhân 101,
> Class 2*.
>
> **Cần đọc trước:** [Bài 6](bai_06_thue_thu_nhap_ca_nhan.md) — mọi tỷ lệ phần trăm trong bài này
> chia trên **tiền thật về tài khoản**, không phải con số trên hợp đồng lao động. Chia nhầm mẫu số
> thì cả hệ thống lệch ngay tháng đầu.
>
> **Nên đọc trước:** [Bài 3](bai_03_ghi_chep_chi_tieu.md) — bài này chạy thử các công thức trên
> đúng bảng chi tiêu 12 tháng của bài 3. Không có bảng đó thì không kiểm được công thức nào cả.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Code:** [`thuc_hanh/bai-07-phan-bo-thu-nhap.py`](../thuc_hanh/bai-07-phan-bo-thu-nhap.py)
> — mọi bảng số trong bài do tệp này tính. Ba công thức khai báo thành dữ liệu ở đầu tệp, muốn
> đổi tỷ lệ thì sửa đúng chỗ đó.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Ba bộ công cụ, và câu hỏi sách không đặt](#1-ba-bộ-công-cụ-và-câu-hỏi-sách-không-đặt)
- [2. Sáu chiếc lọ](#2-sáu-chiếc-lọ)
- [3. Quy tắc 50/30/20](#3-quy-tắc-503020)
- [4. [đính chính] Ánh xạ sang 50/30/20 hụt 5 điểm](#4-đính-chính-ánh-xạ-sang-503020-hụt-5-điểm)
- [5. Quy luật 70/30](#5-quy-luật-7030)
- [6. [bổ sung] Đặt ba công thức cạnh nhau: một đáp số duy nhất](#6-bổ-sung-đặt-ba-công-thức-cạnh-nhau-một-đáp-số-duy-nhất)
- [7. [bổ sung] Sàn chi thiết yếu — mỗi công thức có một ngưỡng thu nhập](#7-bổ-sung-sàn-chi-thiết-yếu--mỗi-công-thức-có-một-ngưỡng-thu-nhập)
- [8. [bổ sung] Chạy thử mười hai tháng có thật](#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật)
- [9. Tỷ lệ tiết kiệm](#9-tỷ-lệ-tiết-kiệm)
- [10. [đính chính] Mẹo tỷ lệ tiết kiệm lớn hơn số tuổi](#10-đính-chính-mẹo-tỷ-lệ-tiết-kiệm-lớn-hơn-số-tuổi)
- [11. [bổ sung] Chọn công thức nào — và khi nào không công thức nào chạy](#11-bổ-sung-chọn-công-thức-nào--và-khi-nào-không-công-thức-nào-chạy)
- [12. Tự thử](#12-tự-thử)
- [13. Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
- [14. Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Ba bộ công cụ, và câu hỏi sách không đặt

C2 tr. 18–25 đưa ba cách chia thu nhập, mỗi cách một lesson riêng, rồi kết ở tr. 25:

> *"Đến đây thì bạn cũng đã có trong tay 3 bộ công cụ. Chọn lấy 1 và thực hiện."*

Chọn theo tiêu chí gì thì sách không nói. Ba công thức được trình bày nối tiếp nhau, không có một
bảng nào đặt chúng cạnh nhau. Tác giả có nêu ý kiến cá nhân — 50/30/20 *"là công thức đơn giản cho
người mới bắt đầu"* (tr. 24), còn 70/30 là *"phương pháp tôi ưa thích nhất"* (tr. 25) — nhưng đó là
sở thích, không phải tiêu chí.

Bài này làm ba việc sách không làm:

1. **Gom ba công thức về cùng một đơn vị** để so được. Kết quả bất ngờ ở [mục 6](#6-bổ-sung-đặt-ba-công-thức-cạnh-nhau-một-đáp-số-duy-nhất).
2. **Hỏi công thức nào chạy được với thu nhập nào.** Câu trả lời đảo ngược lời khuyên của sách —
   [mục 7](#7-bổ-sung-sàn-chi-thiết-yếu--mỗi-công-thức-có-một-ngưỡng-thu-nhập).
3. **Chạy thử trên 12 tháng chi tiêu có thật** thay vì mô tả suông — [mục 8](#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật).

Trước hết, chép lại ba công thức cho đúng.

---

## 2. Sáu chiếc lọ

T. Harv Eker, sách *Secrets of the Millionaire Mind*. Quy tắc vận hành, C2 tr. 18:

> *"Khi bạn nhận được bất kỳ một khoản tiền nào, có thể là lương, tiền lãi đầu tư chứng khoán, bán
> đồ ... Việc đầu tiên là chia số tiền nhận được thành 6 phần"*

Chú ý chữ **bất kỳ khoản tiền nào** — không chỉ lương. Bán một món đồ cũ, nhận tiền lãi, được
thưởng: chia hết.

| Lọ | Tỷ lệ | Dùng cho | Trang |
| --- | ---: | --- | --- |
| **FFA** — Tự do tài chính | 10% | đầu tư, góp vốn, mua cổ phiếu — tiền làm việc thay bạn | tr. 18 |
| **NEC** — Chi tiêu thiết yếu | 55% | nhà, ăn, hoá đơn, **và cả phong bì mừng cưới, sửa xe, hỏng laptop** | tr. 19 |
| **EDU** — Giáo dục | 10% | sách, khoá học, mời người giỏi đi cà phê | tr. 19–20 |
| **PLAY** — Hưởng thụ | 10% | tiêu thoải mái theo sở thích, được phép "vung tay quá trán" trong hạn mức | tr. 20 |
| **GIVE** — Cho đi | 5% | cho người **xứng đáng**, không phải người **cần** | tr. 20–21 |
| **LTSS** — Tiết kiệm dài hạn | 10% | điện thoại, xe, nhà — khoản lớn tích luỹ dần | tr. 21 |

Bốn điểm trong phần này đáng nhớ hơn bản thân các con số:

**FFA là lọ ưu tiên số một.** tr. 18: *"nếu hệ thống "6 jars" chỉ còn "1 jar" thì FFA là khoản đó"*.
Sách nối nó với *The Richest Man in Babylon*: dành 10% để đầu tư, sống bằng 90% còn lại.

**NEC nuốt cả các khoản bất thường.** Đây là chi tiết dễ lướt qua nhất và cũng là chi tiết làm hệ
thống vỡ ở [mục 8](#8-bổ-sung-chạy-thử-mười-hai-tháng-có-thật). tr. 19 xếp thẳng *"Tiền phong bì
mừng cưới bạn bè người thân cũng ở đây"*, rồi hỏng laptop, bảo dưỡng xe cũng ở đây. Tức là toàn bộ
**nhóm thứ tư của Kakeibo** — nhóm "chi tiêu bất thường" mà [bài 3](bai_03_ghi_chep_chi_tieu.md)
chứng minh là thủ phạm gây sai số lớn nhất — đổ hết vào một chiếc lọ được cấp cố định 55%.

**Sách tự đặt một cái cờ đỏ kiểm được.** tr. 19: *"Cảnh báo "red flag" xuất hiện nếu NEC > 80% tổng
thu nhập, lúc này bạn cần ngay lập tức tăng thu, hoặc mạnh tay cắt giảm chi phí."* Giữ lấy con số
80% này, mục 8 sẽ đem nó ra thử.

**LTSS là lọ duy nhất "ở lại".** tr. 21 nói rất rõ, và đây là câu quan trọng nhất của cả Unit:

> *"Nếu bạn để ý, cả 5 "chiếc lọ" ở trên đều là chi tiêu. Ngay cả FFA, dù đầu tư với kỳ vọng tiền
> sinh ra tiền, bạn vẫn chịu rủi ro mất tiền, có thể là một phần tiền nhưng có khi là mất trắng.
> Chỉ có LTSS là ở lại, là dành dụm."*

Sách cũng tự phân loại EDU là **chi phí**, không phải đầu tư (tr. 19–20) — *"EDU vẫn là chi phí"*,
một thứ *"chi phí tốt"*, nhưng vẫn là chi phí. Hai phân loại này là của tác giả, không phải của bài
học này, và mục 6 sẽ dùng chính chúng.

### Ba tình huống thực tế — C2 tr. 22–23

Phần này là phần hữu ích nhất của Unit, vì nó biến quy tắc thành thao tác.

**Bạn bè hỏi vay tiền.** Phản xạ là lấy từ NEC (vay nóng) hoặc LTSS (vay dài). Sách bảo cả hai đều
sai, phải lấy từ **GIVE**: *"Bạn cần lấy số tiền ở GIVE."* Lý do là để định giá trước rủi ro không
đòi được — nếu được trả thì tốt, không trả thì quan hệ vẫn còn. Và nếu GIVE không đủ thì nói thẳng
là chỉ giúp được chừng đó. Đây là một quy tắc tốt: nó chuyển một quyết định cảm tính thành một
quyết định ngân sách.

**Khoản tiền quá nhỏ.** Bán bộ quần áo lời 120.000₫, chia sáu lọ ra 12 nghìn PLAY, 6 nghìn GIVE.
Sách bảo đừng chi li: làm tròn, hoặc gộp về hai lọ. *"Số phần trăm chỉ mang tính tương đối. Thói
quen mới là quan trọng."*

**Tháng bội chi — NEC cháy sạch.** Sách quy định một **thứ tự phá lọ** cụ thể:

```
PLAY  ->  LTSS  ->  EDU  ->  GIVE  ->  FFA
```

Lý lẽ từng bước: PLAY trước vì tháng đó thôi không chơi; LTSS tiếp *"vì đó là khoản tiết kiệm"*;
rồi EDU; GIVE để sau vì nó khiến bạn thấy giàu có; FFA cuối cùng vì đó là *"số tiền mua sự tự do
của bạn"*.

**Thứ tự này mâu thuẫn với chính tr. 21.** Nếu LTSS là chiếc lọ *duy nhất* ở lại, thì đem nó ra hy
sinh ở vị trí **thứ hai**, trước cả hai khoản chi thuần tuý là EDU và GIVE, là hạ đúng thứ mà cả hệ
thống tồn tại để bảo vệ. Mục 8 đo hậu quả bằng số: sau 12 tháng, lọ được bảo vệ cuối cùng (FFA) còn
**17,60tr**, còn lọ "ở lại" (LTSS) chỉ còn **8,60tr** — chưa bằng một nửa.

---

## 3. Quy tắc 50/30/20

Elizabeth Warren và Amelia Warren Tyagi, sách *All Your Worth: The Ultimate Lifetime Money Plan*.
C2 tr. 23–24. Ba khoản thay vì sáu:

| Khoản | Tỷ lệ | Là gì |
| --- | ---: | --- |
| **Needs** | 50% | thiết yếu hàng tháng: sinh hoạt phí và hoá đơn |
| **Wants** | 30% | mong muốn |
| **Savings** | 20% | tiết kiệm |

Sách cho sẵn một **lối thoát khi 50% không đủ** (tr. 23): giảm mỗi khoản còn lại 5 điểm, thành
**60/25/15**. Đây là chi tiết tốt và mục 7 sẽ cho thấy nó quan trọng hơn vẻ ngoài — nó là công cụ
duy nhất trong cả ba công thức cho phép người có thu nhập thấp nới phần thiết yếu. Hệ thống 6 jars
**không có** lối thoát tương đương: nó chỉ cho phép phá lọ khi đã cháy, chứ không cho sửa tỷ lệ.

Sách cũng nêu hai chỗ yếu của chính công thức này, và cả hai đều đúng:

- **Wants không có thứ tự ưu tiên bên trong** (tr. 24). Mong muốn nào đến trước tiêu trước, cho tới
  khi hết ngân sách. Ai đó hỏi vay 3 triệu là tháng đó hết cả sách lẫn ăn chơi. Trong 6 jars, ba
  nhu cầu ấy nằm ở ba lọ riêng nên không giẫm lên nhau — đó là lý do chính đáng để chọn 6 jars.
- **Savings không nói tách đầu tư với tiết kiệm thế nào** (tr. 24). Lãi ngân hàng đang cao, chứng
  khoán đang giảm, thì 20% ấy đi đâu? Sách để ngỏ. Trong 6 jars, câu này đã được trả lời sẵn:
  FFA 10% đầu tư, LTSS 10% để dành.

---

## 4. [đính chính] Ánh xạ sang 50/30/20 hụt 5 điểm

C2 tr. 23–24 nối 50/30/20 với 6 jars bằng ba câu, và cả ba đều là câu cộng số. Cộng thử:

| Khoản | Sách bảo cộng từ | Cộng ra | Sách nói thêm | Thành | Sách ghi | Lệch |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Needs | NEC | 55% | *"thấp hơn 5%"* | 50% | 50% | 0 |
| **Wants** | PLAY + EDU + GIVE | **25%** | — | **25%** | **30%** | **−5 điểm** |
| Savings | FFA + LTSS | 20% | — | 20% | 20% | 0 |

Câu của sách về Wants (tr. 24) không kèm điều chỉnh nào:

> *"Tương ứng với "6 jars", đó là các khoản cộng gộp của PLAY+EDU+GIVE."*

PLAY 10 + EDU 10 + GIVE 5 = **25**, không phải 30.

Tổng ba khoản vẫn ra 100% — nên lỗi này không lộ ra khi đọc lướt. Nó không lộ vì đúng **5 điểm bị
lấy khỏi NEC ở dòng trên đã lặng lẽ chạy sang Wants** mà sách không nói.

**Vì sao chuyện này không phải bắt bẻ.** Đọc ba câu ánh xạ ấy, người ta hiểu 50/30/20 chỉ là 6 jars
gộp lại, nên hai công thức tương đương và chuyển qua lại tuỳ thích được. Thật ra 50/30/20 **dời 5
điểm từ thiết yếu
sang tuỳ ý**. Với người chi thiết yếu sát nút, 5 điểm đó là 5 điểm quyết định — mục 7 quy nó ra
tiền: với cùng một mức chi thiết yếu, 50/30/20 đòi lương gộp **23,47tr** trong khi 6 jars đòi
**21,26tr**.

---

## 5. Quy luật 70/30

Jim Rohn, sách *7 chiến lược thịnh vượng và hạnh phúc*. C2 tr. 24–25. Ý chính: **học cách sống với
70% thu nhập của mình.**

| Khoản | Tỷ lệ | Là gì |
| --- | ---: | --- |
| Chi tiêu | 70% | *"những thứ cần thiết và xa xỉ"* — gộp cả cần lẫn muốn |
| Từ thiện | 10% | trả lại cho cộng đồng |
| Đầu tư vốn | 10% | *"dùng tiền để sinh ra tiền"* — tương đương FFA |
| Tiết kiệm | 10% | phòng những mùa đông tài chính |

Hai chỗ đáng chú ý.

**Sách tự đối chiếu với 50/30/20** ở tr. 25: *"70% rơi vào mục Wants và Needs"*. Mà Needs + Wants
trong 50/30/20 là 50 + 30 = **80%**. Nên 70/30 chặt hơn 10 điểm ở phần tiêu dùng thuần tuý. Đây là
lần duy nhất sách so trực tiếp hai công thức, và nó đúng.

**Từ thiện được nâng gấp đôi và được phép tuỳ chỉnh.** tr. 25: *"Nếu như T. Harv Eker cố định GIVE
ở mốc 5% thì Jim Rohn cho rằng bạn có thể tùy chỉnh con số dựa trên kế hoạch cá nhân."* Ghi nhớ
điều này, vì mục 6 sẽ cho thấy 10% từ thiện chính là chỗ cái tên "70/30" gây hiểu nhầm.

---

## 6. [bổ sung] Đặt ba công thức cạnh nhau: một đáp số duy nhất

Ba công thức có 6, 3 và 4 khoản mục, tên khác nhau hoàn toàn. Muốn so thì phải quy về cùng một câu
hỏi. Câu hỏi ấy là:

> **Sau khi chia xong, đồng tiền này còn thuộc về bạn không?**

Phân loại theo đúng câu đó, và dùng chính phân loại của sách:

- **chi** — tiền ra khỏi tài sản ròng. EDU vào đây vì tr. 19 nói thẳng đừng gọi nó là đầu tư, nó là
  chi phí. GIVE vào đây theo định nghĩa. Từ thiện của 70/30 cũng vậy.
- **đầu tư** — tiền ở lại nhưng chịu rủi ro mất. FFA, và "đầu tư vốn". tr. 21 tự xếp như vậy.
- **để dành** — tiền ở lại. LTSS, Savings, và "tiết kiệm" 10%.

| Hệ thống | Chi ra | Đầu tư | Để dành | **Tiền ở lại** |
| --- | ---: | ---: | ---: | ---: |
| 6 jars | 80% | 10% | 10% | **20%** |
| 50/30/20 | 80% | 0% | 20% | **20%** |
| 70/30 | 80% | 10% | 10% | **20%** |

**Ba cái tên khác nhau, ba cách chia khác nhau, một đáp số: giữ lại 20%.**

Cái tên **"70/30" gây hiểu nhầm nhiều nhất**: nghe như để lại 30%, nhưng 10 điểm trong đó là từ
thiện — tiền cho đi, tức là tiền chi. Tỷ lệ chi/giữ thật của 70/30 cũng là **80/20**, y hệt hai
công thức kia.

Đọc theo nghĩa chặt của tr. 21 — chỉ LTSS mới thật sự "ở lại" — thì con số còn thấp hơn: 6 jars và
70/30 chỉ chắc chắn giữ **10%**.

### Điều này nghĩa là gì

[Bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách)
đã rút ra: số năm tới tự do tài chính **không phụ thuộc thu nhập**, chỉ phụ thuộc tỷ lệ tiết kiệm
và lợi suất thực, theo `n = -ln(s)/ln(1+g)`. Ghép hai kết quả lại:

| Tỷ lệ tiết kiệm | Số năm (lợi suất thực 8%) | Ứng với |
| ---: | ---: | --- |
| 20,0% | 20,9 năm | cả ba công thức, đọc thường |
| 15,5% | 24,2 năm | thực tế 12 tháng ở mục 8 |
| 10,0% | 29,9 năm | đọc chặt theo tr. 21, chỉ LTSS |

Nên câu *"Chọn lấy 1 và thực hiện"* của tr. 25 nhẹ nhàng hơn vẻ ngoài rất nhiều: **chọn cái nào
cũng đưa bạn tới cùng một chỗ, trong cùng một khoảng thời gian.** Ba công thức khác nhau ở chỗ
**dễ theo tới đâu**, không khác nhau ở chỗ tới đâu.

Và điều đó dẫn thẳng tới câu hỏi thật sự cần hỏi khi chọn: **công thức nào chạy được với thu nhập
của tôi?**

---

## 7. [bổ sung] Sàn chi thiết yếu — mỗi công thức có một ngưỡng thu nhập

Cả ba công thức chia bằng **phần trăm**. Điều đó ngầm giả định chi tiêu thiết yếu **co giãn theo
thu nhập**: lương gấp đôi thì tiền ăn tiền nhà cũng gấp đôi.

Giả định ấy sai ở đầu dưới. Tiền nhà, tiền ăn, tiền điện có một cái **sàn tính bằng đồng**. Dưới
sàn đó thì kỷ luật không cứu được gì — công thức đơn giản là không chạy.

Gọi sàn ấy là `S`. Ngưỡng thu nhập ròng tối thiểu để công thức chạy được:

```
thu nhập ròng tối thiểu = S / (tỷ lệ dành cho thiết yếu)
```

Hai mốc sàn dùng làm ví dụ, cả hai đều có nguồn chứ không phải bịa:

- **Sàn A = 10,37tr/tháng** — chi thiết yếu thật của 12 tháng ở
  [bài 3](bai_03_ghi_chep_chi_tieu.md): nhóm "thiết yếu" cộng nhóm "bất thường", vì tr. 19 xếp
  phong bì mừng cưới và bảo dưỡng xe vào NEC.
- **Sàn B = 15,50tr/tháng** — mức giảm trừ gia cảnh cho bản thân năm 2026
  ([bài 6](bai_06_thue_thu_nhap_ca_nhan.md)), tức con số nhà nước coi là phần thu nhập không đánh
  thuế được.

Cột "gộp" quy ngược ra lương trên hợp đồng bằng đúng hàm thuế của bài 6:

| Công thức | Phần thiết yếu | Sàn A: cần ròng | → lương gộp | Sàn B: cần ròng | → lương gộp |
| --- | ---: | ---: | ---: | ---: | ---: |
| 70/30 | 70% (gộp cần + muốn) | 14,81tr | **16,55tr** | 22,14tr | 25,13tr |
| 60/25/15 | 60% | 17,28tr | 19,41tr | 25,83tr | 29,53tr |
| 6 jars | 55% (NEC) | 18,85tr | 21,26tr | 28,18tr | 32,44tr |
| 50/30/20 | 50% (Needs) | 20,73tr | **23,47tr** | 31,00tr | 35,94tr |

**Thứ tự này đảo ngược lời khuyên của sách.**

50/30/20 được giới thiệu là *"công thức đơn giản cho người mới bắt đầu"* (tr. 24). Nó đơn giản thật
— ba khoản dễ nhớ hơn sáu. Nhưng nó **đòi thu nhập cao nhất trong cả bốn cách**, vì nó bóp phần
thiết yếu xuống thấp nhất (50%). Với sàn A, khoảng cách là **23,47tr so với 16,55tr lương gộp** —
gần 7 triệu một tháng.

70/30 đòi ít nhất, và lý do có tính cấu trúc: **nó không tách "cần" khỏi "muốn"**. Gộp cả hai vào
70% nghĩa là tháng nào chi thiết yếu vọt lên thì phần xa xỉ tự động co lại, không cần luật gì thêm.
Càng ít ngăn thì càng ít chỗ vỡ. Đây là một lý do khách quan để chọn 70/30, tốt hơn hẳn lý do
*"phương pháp tôi ưa thích nhất"* mà sách đưa ở tr. 25.

Còn **60/25/15** đáng chú ý ở chỗ: nó là công cụ duy nhất trong sách cho phép nới phần thiết yếu
mà không phá vỡ hệ thống, và nó bị chôn trong một câu phụ ở tr. 23. Với người có sàn chi cao, đó
là dòng quan trọng nhất của cả Unit 2.

---

## 8. [bổ sung] Chạy thử mười hai tháng có thật

Mô tả một hệ thống thì dễ. Cho nó chạy trên số liệu có thật thì khác.

Lấy nguyên bảng chi tiêu 12 tháng của [bài 3](bai_03_ghi_chep_chi_tieu.md), ánh xạ bốn nhóm Kakeibo
vào các lọ **theo đúng chỉ dẫn của sách**:

| Nhóm Kakeibo (C1 tr. 9) | Vào lọ nào | Vì sao |
| --- | --- | --- |
| thiết yếu | NEC | hiển nhiên |
| **bất thường** | **NEC** | tr. 19: phong bì mừng cưới, bảo dưỡng xe, hỏng laptop |
| sở thích | PLAY | |
| bồi dưỡng tâm hồn | EDU | |

Thu nhập **về tay** 16,00tr/tháng. Khi lọ nào âm thì bù theo đúng thứ tự phá lọ của tr. 22–23.

```
  tháng   NEC chi   vượt cấp   phá lọ   phải vay      FFA     LTSS     GIVE   ghi chú
  ────────────────────────────────────────────────────────────────────────────────────
     1    25.00tr   +16.20tr    5.10tr    13.00tr   0.00tr   0.00tr   0.00tr   Tết: biếu tết, về quê
     2     8.00tr    -0.80tr    0.40tr     0.00tr   1.60tr   1.20tr   0.80tr
     3     8.20tr    -0.60tr    0.20tr     0.00tr   3.20tr   2.60tr   1.60tr
     4     8.00tr    -0.80tr    0.60tr     0.00tr   4.80tr   3.60tr   2.40tr
     5    11.10tr    +2.30tr    0.50tr     0.00tr   6.40tr   4.70tr   3.20tr   cưới bạn
     6     8.50tr    -0.30tr    0.90tr     0.00tr   8.00tr   5.40tr   4.00tr
     7     8.30tr    -0.50tr    0.30tr     0.00tr   9.60tr   6.70tr   4.80tr
     8    12.00tr    +3.20tr    2.90tr     0.00tr  11.20tr   5.40tr   5.60tr   sửa xe máy
     9     8.20tr    -0.60tr    0.40tr     0.00tr  12.80tr   6.60tr   6.40tr
    10     8.40tr    -0.40tr    0.70tr     0.00tr  14.40tr   7.50tr   7.20tr
    11    10.10tr    +1.30tr    0.70tr     0.00tr  16.00tr   8.40tr   8.00tr   đầy tháng con bạn
    12     8.60tr    -0.20tr    1.40tr     0.00tr  17.60tr   8.60tr   8.80tr
```

### Tháng 1 phá vỡ hệ thống ngay lập tức

NEC được cấp 8,80tr, phải chi **25,00tr**. Phá sạch cả năm lọ còn lại được 5,10tr, **vẫn thiếu
13,00tr**. Sách không có quy tắc nào cho tình huống này — tr. 23 chỉ viết *"Hy vọng bạn không rơi
vào hoàn cảnh tệ nhất."*

Mười một tháng còn lại không phải vay thêm đồng nào. Nhưng khoản vay tháng 1 cũng không có quy tắc
nào bảo lấy đâu ra mà trả — trong sáu chiếc lọ không có lọ trả nợ. Đó là lỗ hổng mà
**bài 8** phải vá.

Chú ý: tháng 1 không phải tháng tiêu hoang. Đó là tháng Tết, một sự kiện **biết trước cả năm**.

### Cuối năm còn lại bao nhiêu

```
Cả năm: thu 192,00tr · chi 162,20tr · dôi ra 29,80tr
Còn trong sáu lọ 42,80tr · đã phải vay 13,00tr  ->  TÍCH LUỸ RÒNG 29,80tr

Tỷ lệ giữ lại DANH NGHĨA của 6 jars:  20,0%
Tỷ lệ giữ lại THỰC TẾ sau 12 tháng:   15,5%
```

Hụt 4,5 điểm. Câu hỏi đáng giá là **hụt ở đâu** — tách ra từng lọ:

| Lọ | Ngân sách | Chi thật cả năm | Bình quân/tháng | Lệch |
| --- | ---: | ---: | ---: | ---: |
| NEC | 55% | 124,40tr | 10,37tr | **+9,8 điểm** |
| PLAY | 10% | 27,30tr | 2,27tr | +4,2 điểm |
| EDU | 10% | 10,50tr | 0,88tr | −4,5 điểm |
| GIVE | 5% | 0,00tr | 0,00tr | −5,0 điểm |

Bốn cột lệch cộng lại: +9,8 + 4,2 − 4,5 − 5,0 = **+4,5 điểm**, đúng bằng phần giữ lại bị hụt. Không
có đồng nào bốc hơi. (GIVE âm 5 điểm là vì bảng bài 3 không có mục cho đi — tiền giữ lại chứ chưa
chi ra. Nếu thật sự cho đi thì tỷ lệ giữ lại còn 10,5%.)

**PLAY vượt 4,2 điểm nhưng EDU hụt 4,5 điểm — hai cái gần như triệt tiêu nhau.** Toàn bộ phần còn
lại là **NEC: cần 64,8% thu nhập chứ không phải 55%**.

Kết luận không dễ chịu nhưng quan trọng: **người này không tiêu hoang.** Họ chi cho giáo dục dưới
ngân sách, chi hưởng thụ vượt một chút, và họ vẫn không sống nổi trong 55%. Vấn đề không nằm ở kỷ
luật, mà ở chỗ tỷ lệ 55% không đúng với họ.

### Cờ đỏ của sách không bắt được ca này

tr. 19 đặt ngưỡng cảnh báo **NEC > 80%**. Người này ở **64,8%** — dưới ngưỡng, không có cờ nào bật
lên. Nhưng họ vẫn phải vay 13 triệu trong tháng đầu tiên và về đích chậm hơn 3,3 năm so với con số
danh nghĩa.

Cờ đỏ 80% bắt được **khủng hoảng**. Nó không bắt được **lệch cấu hình** — trường hợp phổ biến hơn
nhiều.

### Và thứ tự phá lọ ăn đúng chiếc lọ quan trọng nhất

Cuối năm: **FFA 17,60tr, LTSS 8,60tr.** FFA được sách đặt cuối hàng hy sinh nên gần như không bị
sứt mẻ; LTSS đứng thứ hai nên bị ăn liên tục — trong khi chính tr. 21 nói LTSS là chiếc lọ **duy
nhất "ở lại"**.

Sửa thế nào thì đơn giản: **đổi thứ tự phá lọ thành PLAY → EDU → GIVE → LTSS → FFA**, tức là tiêu
hết các lọ chi tiêu trước khi động vào hai lọ tích luỹ. Bài tập 3 ở [mục 12](#12-tự-thử) để bạn tự
đo xem đổi thứ tự thì cuối năm khác bao nhiêu.

---

## 9. Tỷ lệ tiết kiệm

C2 tr. 26. Định nghĩa và một biến đổi đại số ngắn mà sách làm rất tốt:

```
tỷ lệ tiết kiệm = tiết kiệm / thu nhập
                = (thu nhập - chi tiêu) / thu nhập
                = 1 - chi tiêu / thu nhập
```

Lý do biến đổi này đáng giá, theo đúng lời sách:

> *"chúng ta không thể kiểm soát số tiền tiết kiệm, nhưng có thể kiểm soát được chi tiêu và thu
> nhập để từ đó tác động vào kết quả."*

Đúng, và đây là điểm nối với cả khoá: tiết kiệm là **kết quả**, không phải hành động. Bạn không
"tiết kiệm" — bạn giảm chi (bài 3) hoặc tăng thu (bài 5), rồi tiết kiệm hiện ra.

Sách cũng nêu đúng giới hạn của vế giảm chi (tr. 27): *"Chúng ta không muốn giàu có bằng cách sống
tằn tiện."* Cắt chi có đáy — chi thiết yếu là sàn cứng, đúng như mục 7 đã đo. Tăng thu thì không có
trần. Đó là lý do bài 5 đứng trước bài này.

Còn mục tiêu ở tr. 27 — *"Hãy tìm cách để mỗi năm tăng gia tốc đầu tư thêm 1%"* — là một lời khuyên
tốt và khiêm tốn. Một điểm phần trăm mỗi năm thì gần như không cảm thấy, mà sau mười năm là mười
điểm.

---

## 10. [đính chính] Mẹo tỷ lệ tiết kiệm lớn hơn số tuổi

C2 tr. 28 kết cả Unit bằng một mẹo:

> *"Một mẹo đơn giản là con số này cần lớn hơn hoặc bằng số tuổi của bạn. Nếu năm nay bạn 25, tỷ lệ
> tiết kiệm hàng tháng nên từ 25% trở lên."*

Có ba vấn đề, xếp theo mức độ nặng dần.

**Một — bộ công cụ của chính sách không thoả nổi mẹo của chính sách.** Mục 6 vừa cho thấy cả ba
công thức đều cho đúng 20%. Mẹo đòi:

| Tuổi | Mẹo đòi | Ba công thức cho | Đạt? |
| ---: | ---: | ---: | --- |
| 20 | 20% | 20% | có |
| 25 | 25% | 20% | **không** |
| 30 | 30% | 20% | **không** |
| 40 | 40% | 20% | **không** |
| 55 | 55% | 20% | **không** |

Tám trang trước, sách dạy ba công thức và bảo chọn lấy một. Ở trang 28, sách ra một mẹo mà **không
công thức nào trong ba công thức ấy thoả được**, trừ khi người đọc từ 20 tuổi trở xuống. Sách không
nối hai chỗ này lại.

**Hai — sai thứ nguyên.** Tỷ lệ tiết kiệm là một **dòng** (phần trăm thu nhập mỗi tháng). Tuổi là
một **mức**. Buộc một dòng phải tăng theo một mức là đòi tiết kiệm mạnh nhất **đúng lúc quãng đường
còn lại ngắn nhất** — ngược hoàn toàn với logic tích luỹ. Đây chính là kiểu lẫn dòng chảy với tồn
kho mà [bài 2 mục 4](bai_02_do_hien_trang.md#4-bổ-sung-dòng-chảy-và-tồn-kho--cái-tên-mà-sách-không-đặt)
đã đặt tên.

Mẹo cũng không có điểm dừng: cứ theo chữ, người 60 tuổi phải để ra 60% thu nhập — đúng lúc lẽ ra
được tiêu số đã tích luỹ.

**Ba — nó vẫn "chạy" được, và đó mới là chỗ dễ nhầm.** Chạy thử một người 25 tuổi, thu nhập thực
không đổi, lợi suất thực 8%:

| Chiến lược | Xong ở tuổi | Năm cuối phải để ra |
| --- | ---: | ---: |
| giữ cố định 20% (điều ba công thức thật sự cho) | 46 | 20% |
| làm theo mẹo, tỷ lệ = số tuổi mỗi năm | **40** | **39%** |

Mẹo **rút ngắn được 6 năm thật**. Nhưng nó rút ngắn bằng cách bắt người ta sống với 61% thu nhập ở
năm cuối, chứ không phải bằng một cơ chế nào khác. Nó là một cách nói "hãy tiết kiệm nhiều hơn"
được gói trong một con số dễ nhớ.

**Dùng nó thế nào.** Như một cái đích để nhắm, không phải một quy tắc để tuân. Nếu 25 tuổi mà đang
ở 20% thì bạn không sai — bạn đang đúng bằng chính công thức sách dạy. Muốn lên 25% thì phải rời
khỏi cả ba công thức, xem [mục 11](#11-bổ-sung-chọn-công-thức-nào--và-khi-nào-không-công-thức-nào-chạy).

Một chi tiết nhỏ mà sách bỏ lỡ: **tr. 27 chính là đạo hàm của tr. 28.** Ai bắt đầu ở tỷ lệ đúng
bằng tuổi rồi mỗi năm cộng thêm 1 điểm (lời khuyên tr. 27) thì bám đúng đường "tỷ lệ = tuổi" mãi
mãi. Hai trang cách nhau đúng một trang phát biểu cùng một quy tắc, và sách không nối lại.

---

## 11. [bổ sung] Chọn công thức nào — và khi nào không công thức nào chạy

Sách bảo *"Chọn lấy 1 và thực hiện"* mà không cho tiêu chí. Đây là tiêu chí, dựng từ mục 7 và
mục 8, làm theo đúng thứ tự:

**Bước 1 — Đo, đừng đoán.** Ghi chép 12 tháng (bài 3), lấy tổng nhóm "thiết yếu" cộng nhóm "bất
thường", chia 12. Đó là sàn `S` của bạn. Ba đến sáu tháng như sách khuyên vẫn còn sai tới ±34%
([bài 3 mục 6](bai_03_ghi_chep_chi_tieu.md#6-bổ-sung-vì-sao-36-tháng-và-vì-sao-36-tháng-vẫn-chưa-đủ)),
và với bài này thì sai số đó rơi thẳng vào lọ NEC.

**Bước 2 — Lấy thu nhập RÒNG.** Tiền thật vào tài khoản, không phải con số hợp đồng
([bài 6 mục 2](bai_06_thue_thu_nhap_ca_nhan.md#2-ba-bước-từ-lương-gộp-tới-tiền-về-tay)).

**Bước 3 — Tính tỷ lệ thiết yếu thật của bạn:** `S / thu nhập ròng`.

**Bước 4 — Chọn công thức có phần thiết yếu rộng hơn con số vừa tính:**

| Tỷ lệ thiết yếu thật | Công thức chạy được | Ghi chú |
| ---: | --- | --- |
| dưới 50% | cả bốn | chọn theo sở thích; 6 jars chi tiết nhất |
| 50–55% | 6 jars · 60/25/15 · 70/30 | 50/30/20 sẽ vỡ |
| 55–60% | 60/25/15 · 70/30 | |
| 60–70% | **chỉ 70/30** | ví dụ ở mục 8 (64,8%) rơi vào đây |
| trên 70% | **không công thức nào** | xem dưới |

**Khi không công thức nào chạy.** Đây không phải thất bại của bạn, và cũng không phải chỗ để cố
gắng hơn. Phần trăm không giải được bài toán khi tử số là một con số cứng. Ba lối ra, xếp theo thứ
tự nên thử:

1. **Tăng thu** — [bài 5](bai_05_kiem_tien.md). Lối ra duy nhất không có trần.
2. **Xử lý nợ trước** — bài 8. Nếu sàn `S` phình lên vì tiền trả nợ thì cắt chi phí sinh hoạt là
   cắt nhầm chỗ.
3. **Hạ sàn bằng thay đổi cấu trúc, không phải bằng ý chí.** Đổi chỗ ở, đổi phương tiện. Cắt cà phê
   không hạ được sàn; đổi nhà thì có.

**Và một điều cả ba công thức đều không làm được:** đặt tỷ lệ tiết kiệm **trước**. Cả ba đều chia
từ phía chi tiêu xuống, nên phần giữ lại luôn ra đúng 20% dù hoàn cảnh bạn thế nào. Muốn 30% thì
không có công thức nào trong sách cho bạn con số đó — bạn phải tự chốt 30% trước, rồi cho phần chi
tiêu nhận phần còn lại. Đó là cách làm ngược lại với cả ba, và là cách duy nhất khiến tỷ lệ tiết
kiệm trở thành **quyết định** thay vì **kết quả**.

---

## 12. Tự thử

Sửa [`thuc_hanh/bai-07-phan-bo-thu-nhap.py`](../thuc_hanh/bai-07-phan-bo-thu-nhap.py) rồi chạy lại.
Không có lời giải kèm theo — mục đích là quan sát con số đổi thế nào.

1. **Đổi thu nhập.** `THU_NHAP_RONG` đang là 16tr. Hạ xuống 13tr rồi 11tr. Ở mức nào thì tháng 1
   không còn là tháng duy nhất phải vay? Ở mức nào thì tỷ lệ giữ lại thực tế xuống 0?

2. **Bỏ tháng Tết.** Đặt chi tiêu tháng 1 bằng trung bình các tháng còn lại. Tỷ lệ giữ lại thực tế
   lên bao nhiêu? So với 20% danh nghĩa còn cách bao xa? (Câu này tách phần "sự kiện lớn" khỏi phần
   "tỷ lệ sai".)

3. **Đổi thứ tự phá lọ.** `THU_TU_PHA` đang theo đúng sách: `PLAY, LTSS, EDU, GIVE, FFA`. Đổi thành
   `PLAY, EDU, GIVE, LTSS, FFA` — tức bảo vệ hai lọ tích luỹ tới cuối. Tổng tích luỹ ròng có đổi
   không? Còn phân bố giữa FFA và LTSS thì sao? Kết quả nói gì về việc thứ tự phá lọ thật sự ảnh
   hưởng tới cái gì?

4. **Chạy 70/30 trên cùng bảng chi tiêu ấy.** Viết thêm một vòng lặp cho ba khoản của Jim Rohn, gộp
   thiết yếu và sở thích vào cùng 70%. Còn phải vay bao nhiêu? So với 6 jars thì hơn kém thế nào,
   và điều đó có khớp với dự đoán ở mục 7 không?

5. **Sàn của chính bạn.** Thay `NAM_BAI_3` bằng 12 tháng chi tiêu thật của bạn. Tỷ lệ thiết yếu
   thật của bạn là bao nhiêu, và bảng ở mục 11 xếp bạn vào dòng nào?

---

## 13. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Sáu chiếc lọ | 6 jars | Chia mọi khoản tiền nhận được thành sáu phần cố định: FFA, NEC, EDU, PLAY, GIVE, LTSS |
| Tự do tài chính | FFA — Financial Freedom Account | Lọ đầu tư, 10%. Sách coi là lọ ưu tiên số một |
| Chi tiêu thiết yếu | NEC — Necessities | Lọ sinh hoạt, 55%. Gồm cả các khoản bất thường |
| Tiết kiệm dài hạn | LTSS — Long Term Savings for Spending | Lọ 10%. Sách nói đây là lọ duy nhất "ở lại" |
| Nhu cầu / Mong muốn | Needs / Wants | Hai khoản chi trong 50/30/20 |
| Tỷ lệ tiết kiệm | Savings rate | `1 − chi tiêu/thu nhập`. Là kết quả, không phải hành động |
| Thu nhập ròng | Net income / take-home pay | Tiền thật vào tài khoản. Mẫu số đúng của mọi công thức trong bài |
| Sàn chi thiết yếu | — | Mức chi thiết yếu tối thiểu tính bằng đồng, không co giãn theo thu nhập. Tên do bài này đặt |
| Điểm phần trăm | Percentage point | Đơn vị của hiệu hai tỷ lệ. 64,8% và 55% cách nhau 9,8 **điểm**, không phải 9,8% |

---

## 14. Câu hỏi tự kiểm tra

1. Sáu chiếc lọ và tỷ lệ của từng lọ? Tổng có bằng 100% không?
2. Tiền phong bì mừng cưới lấy từ lọ nào? Tiền sửa xe? Tiền cho bạn vay?
3. Vì sao câu trả lời cho ba câu trên không giống nhau, dù cả ba đều là tiền đi ra?
4. Thứ tự phá lọ khi NEC cháy là gì? Chỗ nào trong thứ tự ấy mâu thuẫn với tr. 21?
5. Sách bảo Wants trong 50/30/20 tương ứng PLAY+EDU+GIVE của 6 jars. Cộng ba lọ ấy ra bao nhiêu?
6. Tỷ lệ tiền **ở lại** của 6 jars, 50/30/20 và 70/30 lần lượt là bao nhiêu?
7. Vì sao cái tên "70/30" gây hiểu nhầm?
8. Sàn chi thiết yếu là gì, và vì sao nó làm hỏng giả định của mọi công thức phần trăm?
9. Trong bốn công thức ở mục 7, cái nào đòi thu nhập cao nhất? Điều đó có khớp với lời khuyên của
   sách không?
10. Ở ví dụ 12 tháng, tỷ lệ giữ lại thực tế là 15,5% chứ không phải 20%. Lọ nào chịu trách nhiệm
    chính, và vì sao nói "người này không tiêu hoang"?
11. Cờ đỏ NEC > 80% của tr. 19 có bắt được ca ấy không? Vì sao?
12. Viết công thức tỷ lệ tiết kiệm ở dạng `1 − …`. Vì sao dạng ấy hữu ích hơn?
13. Mẹo "tỷ lệ tiết kiệm ≥ số tuổi" có ba vấn đề. Kể ra và nói vấn đề nào nặng nhất.
14. Một người 25 tuổi theo đúng 6 jars thì tỷ lệ tiết kiệm là bao nhiêu? Có thoả mẹo tr. 28 không?
15. Muốn tiết kiệm 30% thì công thức nào trong sách cho bạn con số đó?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 7 — PHÂN BỔ THU NHẬP                              C2 tr. 18-28      ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  MẪU SỐ ĐÚNG: thu nhập RÒNG, không phải lương gộp        (bài 6)         ║
║                                                                          ║
║  BA CÔNG THỨC                                                            ║
║     6 jars     FFA 10 · NEC 55 · EDU 10 · PLAY 10 · GIVE 5 · LTSS 10    ║
║     50/30/20   Needs 50 · Wants 30 · Savings 20                          ║
║     70/30      chi 70 · từ thiện 10 · đầu tư 10 · tiết kiệm 10          ║
║                                                                          ║
║  GOM THEO CHỨC NĂNG -> BA CÔNG THỨC CÙNG MỘT ĐÁP SỐ                     ║
║     chi ra 80%  ·  tiền ở lại 20%  — cả ba, không trừ cái nào           ║
║     '70/30' gây hiểu nhầm: 10% từ thiện là CHI, nên nó cũng là 80/20    ║
║     ghép bài 1: 20% -> 20,9 năm tới tự do tài chính (lợi suất thực 8%)  ║
║                                                                          ║
║  [đính chính] tr. 24: Wants = PLAY+EDU+GIVE = 25%, KHÔNG phải 30%       ║
║     5 điểm lấy khỏi NEC đã lặng lẽ chạy sang Wants                      ║
║                                                                          ║
║  [bổ sung] SÀN CHI THIẾT YẾU — phần trăm giả định chi co giãn, sai      ║
║     thu nhập ròng tối thiểu = sàn / tỷ lệ dành cho thiết yếu            ║
║     với sàn 10,37tr:  70/30 cần gộp 16,55tr  <  50/30/20 cần 23,47tr    ║
║     THỨ TỰ ĐẢO lời khuyên sách: 50/30/20 'cho người mới' đòi CAO NHẤT   ║
║                                                                          ║
║  CHẠY THỬ 12 THÁNG THẬT CỦA BÀI 3, thu nhập ròng 16tr                   ║
║     tháng 1 (Tết): NEC cần 25tr, được cấp 8,8tr, phá sạch 6 lọ vẫn      ║
║        thiếu 13tr -> phải vay. Sách không có lọ trả nợ.                 ║
║     giữ lại DANH NGHĨA 20,0%  ->  THỰC TẾ 15,5%                         ║
║     tách 4,5 điểm hụt: NEC +9,8 · PLAY +4,2 · EDU -4,5 · GIVE -5,0     ║
║        EDU DƯỚI ngân sách. Không phải tiêu hoang — NEC cần 64,8%.       ║
║     cờ đỏ 'NEC > 80%' của tr. 19 KHÔNG bắt được ca này                  ║
║     thứ tự phá lọ hạ LTSS thứ hai -> cuối năm FFA 17,6tr, LTSS 8,6tr    ║
║        trong khi tr. 21 nói LTSS là lọ DUY NHẤT ở lại                   ║
║                                                                          ║
║  TỶ LỆ TIẾT KIỆM = 1 - chi tiêu/thu nhập          (tr. 26, sách đúng)   ║
║     là KẾT QUẢ, không phải hành động: giảm chi (bài 3) hoặc tăng thu    ║
║                                                                          ║
║  [đính chính] tr. 28 'tỷ lệ tiết kiệm >= số tuổi' — ba vấn đề           ║
║     1. ba công thức của chính sách chỉ cho 20% -> thoả tới tuổi 20      ║
║     2. sai thứ nguyên: dòng so với mức; đòi mạnh nhất khi còn ít thời gian ║
║     3. có rút ngắn 6 năm thật, nhưng bằng cách sống với 61% ở năm cuối  ║
║     tr. 27 ('mỗi năm thêm 1%') chính là đạo hàm của tr. 28              ║
║                                                                          ║
║  CHỌN CÔNG THỨC: đo sàn -> chia cho thu nhập ròng -> tra bảng mục 11    ║
║     trên 70% thì không công thức nào chạy: tăng thu, xử nợ, đổi cấu trúc ║
║     cả ba đều chia từ phía CHI xuống -> giữ lại luôn ra đúng 20%        ║
║     muốn 30% thì phải chốt 30% TRƯỚC, ngược với cả ba                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn.
  Unit 2, Lesson 2–5, **tr. 18–28**. Toàn bộ tỷ lệ, thứ tự phá lọ, ba tình huống thực tế, ngưỡng
  cờ đỏ 80%, công thức tỷ lệ tiết kiệm và mẹo "lớn hơn hoặc bằng số tuổi" đều chép từ đây.
- Sách dẫn lại ba nguồn gốc: T. Harv Eker, *Secrets of the Millionaire Mind* (6 jars, tr. 18);
  Elizabeth Warren & Amelia Warren Tyagi, *All Your Worth: The Ultimate Lifetime Money Plan*
  (50/30/20, tr. 23); Jim Rohn, *7 chiến lược thịnh vượng và hạnh phúc* (70/30, tr. 25). Sách cũng
  nhắc *The Richest Man in Babylon* cho quy tắc 10% (tr. 18). **Bài này không kiểm chứng nội dung
  ba cuốn gốc** — chỉ kiểm phần số học trong chính C2.
- **Đã kiểm chứng bằng code** —
  [`thuc_hanh/bai-07-phan-bo-thu-nhap.py`](../thuc_hanh/bai-07-phan-bo-thu-nhap.py). Mọi bảng số
  trong bài do tệp này tính, chạy hai lần ra giống hệt nhau. Tệp tự kiểm: ba công thức cộng đủ
  100%; phần "tiền ở lại" của cả ba bằng đúng 20%; bốn cột lệch ở mục 8 cộng đúng bằng phần giữ lại
  bị hụt; và hàm thuế khớp con số đã kiểm tay ở bài 6 (lương gộp 30tr về tay 26.215.000đ).
- **Dữ liệu chi tiêu 12 tháng** lấy nguyên từ
  [`thuc_hanh/bai-03-ghi-chep-bao-lau.py`](../thuc_hanh/bai-03-ghi-chep-bao-lau.py), không sửa một
  con số nào.
- **Liên hệ chéo:**
  - Mẫu số đúng của mọi tỷ lệ trong bài:
    [bài 6 mục 2](bai_06_thue_thu_nhap_ca_nhan.md#2-ba-bước-từ-lương-gộp-tới-tiền-về-tay).
  - Tỷ lệ tiết kiệm ra bao nhiêu năm:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Vì sao phải ghi chép 12 tháng mới đo được sàn:
    [bài 3 mục 6](bai_03_ghi_chep_chi_tieu.md#6-bổ-sung-vì-sao-36-tháng-và-vì-sao-36-tháng-vẫn-chưa-đủ).
  - Lẫn dòng chảy với tồn kho — cùng loại lỗi với mẹo tr. 28:
    [bài 2 mục 4](bai_02_do_hien_trang.md#4-bổ-sung-dòng-chảy-và-tồn-kho--cái-tên-mà-sách-không-đặt).
  - Tăng thu, lối ra duy nhất không có trần:
    [bài 5](bai_05_kiem_tien.md).
  - Khoản vay 13 triệu ở tháng 1 và việc sáu chiếc lọ không có lọ trả nợ: **bài 8**.

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
| **7** | **Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm** ← *bạn đang ở đây* | C2 tr. 18–28 | 1 |
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
