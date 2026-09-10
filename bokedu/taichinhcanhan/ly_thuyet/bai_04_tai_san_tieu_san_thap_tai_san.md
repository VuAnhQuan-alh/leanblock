# Bài 4 — Tài sản, tiêu sản, tháp tài sản

> Bài học dựa trên **Unit 3 của Class 1** — C1 tr. 16–24. Phần bảng cân đối ở tr. 18 đã làm ở
> [bài 2](bai_02_do_hien_trang.md#3-tài-sản-ròng--bước-2-và-bảng-cân-đối-cá-nhân); bài này lo hai
> lesson còn lại.
>
> **Cần đọc trước:** [Bài 2](bai_02_do_hien_trang.md) — bài này trả lời câu hỏi mà bài 2 để ngỏ:
> **cái gì được tính là tài sản**, và xếp chúng theo thứ tự nào.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Code:** [`thuc_hanh/bai-04-thap-tai-san.py`](../thuc_hanh/bai-04-thap-tai-san.py)
> — làm đúng bài tập mà C1 tr. 24 giao, và thêm phép kiểm cho nguyên tắc mà sách nêu ở tr. 21
> nhưng không cho công cụ.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Sách bác Kiyosaki, và bác đúng](#1-sách-bác-kiyosaki-và-bác-đúng)
- [2. [đính chính] Định nghĩa nợ quá hẹp](#2-đính-chính-định-nghĩa-nợ-quá-hẹp)
- [3. Sách đưa hai cái tháp và không bao giờ nối chúng lại](#3-sách-đưa-hai-cái-tháp-và-không-bao-giờ-nối-chúng-lại)
- [4. Năm lớp, từ đáy lên đỉnh](#4-năm-lớp-từ-đáy-lên-đỉnh)
- [5. [bổ sung] Làm bài tập của tr. 24, và kiểm nguyên tắc của tr. 21](#5-bổ-sung-làm-bài-tập-của-tr-24-và-kiểm-nguyên-tắc-của-tr-21)
- [6. [đính chính] Định giá lớp vô hình đo cái gì](#6-đính-chính-định-giá-lớp-vô-hình-đo-cái-gì)
- [7. Tự thử](#7-tự-thử)
- [8. Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
- [9. Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Sách bác Kiyosaki, và bác đúng

Unit 3 mở đầu bằng cách nhắc định nghĩa nổi tiếng nhất của thể loại này:

> *"Bắt đầu từ cuốn sách 'Rich dad poor dad', Robert Kiyosaki đưa ra khái niệm **tài sản** (asset)
> là những gì mang tiền vào túi bạn, còn **tiêu sản** (liability) là những gì lấy tiền trong túi bạn
> ra."* — C1 tr. 16

Rồi bác nó ngay:

> *"Định nghĩa như vậy dễ hiểu nhưng **sơ sài**, vì đã bỏ qua những loại tài sản vô hình, đồng thời
> dẫn đến một cuộc tranh luận không dứt cho câu hỏi 'Ngôi nhà là tài sản hay tiêu sản'."* — C1 tr. 16

Đây là chỗ sách làm tốt, và làm tốt vì hai lý do khác nhau.

**Một, nó chỉ đúng chỗ hỏng.** Định nghĩa của Kiyosaki là một phép phân đôi: hoặc mang tiền vào,
hoặc lấy tiền ra. Ngôi nhà bạn đang ở không rơi vào ô nào — nó **có giá trị**, bán được, nhưng
hằng tháng lại **ngốn tiền** sửa chữa, thuế, bảo trì. Ép nó vào một trong hai ô thì hoặc bạn nói
căn nhà là "tiêu sản" (nghe vô lý với người vừa mua nhà), hoặc nói nó là "tài sản" (và mất luôn ý
nghĩa của khái niệm).

**Hai, thay thế bằng cái tốt hơn.** Sách bỏ phép phân đôi và thay bằng một định nghĩa rộng cộng một
phép chia:

> *"**Tài sản (Assets) là những gì tạo ra lợi ích trong tương lai.** Tài sản chia làm 2 loại là Tài
> sản đầu tư và Tài sản tiêu dùng."* — C1 tr. 16

```
   TÀI SẢN = những gì tạo ra lợi ích trong tương lai
   │
   ├── TÀI SẢN ĐẦU TƯ      tạo ra TIỀN trong tương lai (future cash inflow)
   │   ├── hữu hình:  cổ phiếu, trái phiếu, BĐS, vàng, các loại tiền
   │   └── VÔ HÌNH:   Năng lực · Mạng lưới · Thương hiệu
   │
   └── TÀI SẢN TIÊU DÙNG   tạo ra CHI PHÍ trong tương lai để duy trì
       ví dụ: BĐS để ở, phương tiện đi lại
                                                          C1 tr. 16-17
```

Câu hỏi "ngôi nhà là gì" giờ có câu trả lời không cần cãi nhau: **nhà để ở là tài sản tiêu dùng.**
Nó vẫn là tài sản — nằm bên trái bảng cân đối, cộng vào tài sản ròng ở
[bài 2](bai_02_do_hien_trang.md#3-tài-sản-ròng--bước-2-và-bảng-cân-đối-cá-nhân) — nhưng thuộc loại
sinh chi phí chứ không sinh tiền. Nhà cho thuê thì là tài sản đầu tư. Cùng một căn nhà, hai cách
dùng, hai loại.

### Chữ "tiêu sản" biến mất sau đúng một trang

Đáng chú ý: từ **tiêu sản** xuất hiện **đúng một lần trong cả hai tập sách**, ở C1 tr. 16, trong
chính câu trích dẫn Kiyosaki để phản bác. Sau đó không bao giờ dùng lại.

Đó là lựa chọn nhất quán — sách đã thay khung khái niệm thì không dùng lại từ của khung cũ. Nhưng
nó cũng có nghĩa: nếu bạn đọc lướt và nhớ mỗi cặp "tài sản / tiêu sản", bạn đã nhớ đúng cái mà
sách vừa bảo là sơ sài. Cặp từ cần nhớ là **tài sản đầu tư / tài sản tiêu dùng**.

---

## 2. [đính chính] Định nghĩa nợ quá hẹp

[Bài 2](bai_02_do_hien_trang.md#3-tài-sản-ròng--bước-2-và-bảng-cân-đối-cá-nhân) đã nêu và hẹn làm
kỹ ở đây:

> *"**Nợ (Liabilities) là các khoản vay để tạo ra tài sản.**"* — C1 tr. 17

Vế "để tạo ra tài sản" là chỗ hẹp. Ba khoản nợ rất thật không lọt qua được:

| Khoản nợ | Tạo ra tài sản gì? |
| --- | --- |
| Vay trả viện phí | không tạo ra tài sản nào |
| Dư nợ thẻ tín dụng của một bữa ăn | bữa ăn đã tiêu hết |
| Mượn tiền đóng tiền nhà tháng này | tiền thuê không tạo ra tài sản |

Định nghĩa dùng được: **nợ là mọi nghĩa vụ phải trả, bất kể khoản vay đó đã dùng vào việc gì.**

Chỗ này đổi con số, không phải đổi chữ. Ai liệt kê nợ theo đúng chữ của sách sẽ bỏ sót phần nợ tiêu
dùng, và **tài sản ròng tính ra cao hơn sự thật** — đúng cái bẫy mà chính sách mô tả ở C2 tr. 16
với người *"nhìn bề ngoài rất 'hoành tráng'"* mà net worth âm.

Trớ trêu là ví dụ phản chứng nằm ngay trong sách: chiếc ô tô ở C2 tr. 16 mua trả góp, nay còn nợ
**300 triệu** trong khi xe chỉ đáng **200 triệu**. Khoản vay ấy có "tạo ra tài sản", nhưng tài sản
đó đã teo lại nhỏ hơn khoản nợ. Nghĩa vụ trả 300 triệu vẫn nguyên vẹn dù định nghĩa có phân loại
thế nào.

---

## 3. Sách đưa hai cái tháp và không bao giờ nối chúng lại

Đây là chỗ hỏng lớn nhất của Unit 3.

**Trang 20–21**, sách giới thiệu tháp tài sản và chia nó làm **bốn tầng**:

> *"Một mô hình tháp tài sản cơ bản có thể chia làm **4 tầng** bao gồm: **Tầng 1: Bảo vệ**…
> **Tầng 2: Lập kế hoạch**… **Tầng 3: Mục tiêu ưu tiên**… **Tầng 4: Tài sản cho thế hệ sau**."*
> — C1 tr. 20–21

**Trang 21**, ngay sau đó, mục *"Nguyên tắc xây dựng"* liệt kê một thứ tự khác hẳn — **năm lớp**,
tên khác:

> *"Một tháp tài sản được xem là bền vững khi bạn xây dần từ đế lên với phần bên dưới càng rộng
> càng tốt. Bắt đầu với **Lớp tài sản vô hình**, sau đó lên dần là **Lớp bảo vệ**, **Lớp tạo thu
> nhập**, **Lớp tăng trưởng**. Trên đỉnh tháp là **Lớp rủi ro** với phần trăm phân bổ ít nhất."*
> — C1 tr. 21

Đặt hai danh sách cạnh nhau:

```
   BỐN TẦNG (tr. 20-21)              NĂM LỚP (tr. 21-24)
   ────────────────────              ───────────────────
                                     Tài sản vô hình      ← không có ở bản 4 tầng
   Bảo vệ                    ←──→    Bảo vệ               ← tên duy nhất trùng nhau
   Lập kế hoạch                                           ← không có ở bản 5 lớp
   Mục tiêu ưu tiên                  Tạo thu nhập         ← không có ở bản 4 tầng
                                     Tăng trưởng          ← không có ở bản 4 tầng
   Tài sản cho thế hệ sau                                  ← không có ở bản 5 lớp
                                     Mạo hiểm             ← không có ở bản 4 tầng
```

**Đúng một tên trùng nhau**, trên tổng số bốn và năm. Đây không phải hai cách gọi của cùng một mô
hình — đây là **hai mô hình khác nhau**, đặt cách nhau một trang, và sách không một lần nói chúng
liên hệ ra sao.

Chúng cũng chia theo **hai tiêu chí khác nhau**, nên không thể ánh xạ:

| | Bốn tầng | Năm lớp |
| --- | --- | --- |
| Chia theo | **mục đích** của khoản tiền | **mức rủi ro** của tài sản |
| Tầng "Lập kế hoạch" | tiết kiệm cho mua nhà, mua xe, học hành | không có lớp nào tương ứng |
| Tầng "Thế hệ sau" | quỹ để lại, từ thiện | không có lớp nào tương ứng |
| Lớp "Vô hình" | không có tầng nào tương ứng | năng lực, mạng lưới, thương hiệu |

Và bản bốn tầng **xuất hiện đúng một lần rồi biến mất**. Toàn bộ phần còn lại của Unit 3 — mục
*"Nguyên tắc xây dựng"*, năm mục con mô tả từng lớp ở tr. 22–24, và cả bài tập cuối bài ở tr. 24
(*"Tính toán mỗi **lớp** tài sản…"*) — chỉ nói về bản năm lớp.

**Khoá học dùng bản năm lớp.** Nó là bản được mô tả chi tiết, được ra bài tập, và là bản có nguyên
tắc kiểm được ở mục 5. Bản bốn tầng không mất đi đâu cả: "Lập kế hoạch" chính là **quỹ chi tiêu**
mà **bài 9** sẽ phân biệt với quỹ khẩn cấp, còn "Thế hệ sau" tương ứng với lọ **GIVE** của bài 7.

### Lớp trên cùng cũng có hai tên

Nhỏ hơn nhưng cùng loại: tr. 19 và tr. 21 gọi lớp đỉnh là **"Lớp rủi ro"**, tr. 23–24 lại đặt tiêu
đề **"Lớp tài sản mạo hiểm"**. Khoá học dùng **mạo hiểm**, theo tiêu đề của phần mô tả.

---

## 4. Năm lớp, từ đáy lên đỉnh

```
                          ┌──────────────┐
                          │   MẠO HIỂM   │  tiền mã hoá, chứng khoán phái sinh
                          ├──────────────┤  "phần trăm phân bổ ít nhất"
                       ┌──┤ TĂNG TRƯỞNG  ├──┐  chứng khoán, BĐS, tiền cho vay
                       ├──┴──────────────┴──┤
                    ┌──┤    TẠO THU NHẬP    ├──┐  cho thuê nhà, lãi tiết kiệm,
                    ├──┴────────────────────┴──┤  cổ tức, lãi từ kinh doanh
                 ┌──┤         BẢO VỆ           ├──┐  tiền mặt, vàng, BĐS —
                 ├──┴──────────────────────────┴──┤  thứ đổi ra tiền được ngay
              ┌──┤      TÀI SẢN VÔ HÌNH           ├──┐  kiến thức, kỹ năng,
              └──┴────────────────────────────────┴──┘  kinh nghiệm, quan hệ
                                                              C1 tr. 21-24
```

| Lớp | Sách định nghĩa | Bài làm kỹ |
| --- | --- | --- |
| **Vô hình** | *"kiến thức, kỹ năng, kinh nghiệm, các mối quan hệ… nền tảng để tạo ra các loại tài sản khác"* | 5 |
| **Bảo vệ** | *"tài sản dự phòng trường hợp… bệnh tật, thất nghiệp… dễ dàng chuyển đổi thành tiền"* | 9 |
| **Tạo thu nhập** | *"trực tiếp tạo ra thu nhập: tiền thu từ cho thuê nhà, tiền lãi… cổ tức"* | 13 |
| **Tăng trưởng** | *"đầu tư với mục đích tăng trưởng, kiếm lợi nhuận… đi kèm rủi ro tài chính tương ứng"* | 12, 13 |
| **Mạo hiểm** | *"tiền mã hóa, chứng khoán phái sinh… rủi ro cao nhưng lợi nhuận kỳ vọng cũng rất lớn"* | 11, 12 |

Hai điều kiện lọc mà sách đặt ra cho việc xếp tài sản vào tháp:

**Một, chỉ tính thứ nắm giữ lâu dài.**

> *"Bạn sẽ chỉ đưa vào đây những tài sản nắm giữ lâu dài. Chúng ta sẽ không tính các cổ phiếu hay
> các loại tài sản mà bạn liên tục giao dịch, trading ngắn hạn."* — C1 tr. 21

Nhất quán với C1 tr. 11, nơi sách xếp lợi nhuận trading vào **thu nhập kinh doanh** chứ không phải
thu nhập đầu tư ([bài 2](bai_02_do_hien_trang.md#2-dòng-tiền--bước-1-của-sách)). Hai chỗ, cùng một
lằn ranh: tài sản là thứ *nắm giữ*, không phải thứ *xoay vòng*.

**Hai, xây từ đáy lên.**

> *"Một tháp tài sản được xem là bền vững khi bạn xây dần từ đế lên với **phần bên dưới càng rộng
> càng tốt**."* — C1 tr. 21

Câu này nghe như lời khuyên tinh thần, nhưng nó **kiểm được bằng máy** — mục 5.

### Một chỗ lẫn nhỏ ở tầng đáy

Bản bốn tầng mô tả tầng 1 là *"bao gồm các **chi phí** cơ bản cho cuộc sống (ăn uống, thuốc men,
chữa bệnh…)"* (C1 tr. 20). Một tầng của tháp **tài sản** không thể chứa chi phí — chi phí không
phải tài sản. Sách tự sửa ngay câu sau: *"Để xây dựng tầng này, bạn cần có một **tài khoản dự
phòng**"*. Cái nằm trong tháp là **quỹ**, không phải khoản chi mà quỹ đó chi trả.

Con số kèm theo thì đúng và nhất quán với C2: *"Số tiền tích lũy thấp nhất là từ **3-6 tháng** chi
tiêu tối thiểu"* (C1 tr. 21). **Bài 9** làm kỹ, kèm tiêu chí chọn giữa 3, 6 và 12 tháng.

---

## 5. [bổ sung] Làm bài tập của tr. 24, và kiểm nguyên tắc của tr. 21

Sách kết thúc Unit 3 bằng một bài tập:

> *"Tính toán mỗi lớp tài sản hiện tại chiếm bao nhiêu phần trăm trong cấu trúc tháp tài sản của
> bạn? Vẽ hình dáng tháp tài sản cá nhân."* — C1 tr. 24

Và ở tr. 21 sách đã cho tiêu chí chấm: *"phần bên dưới càng rộng càng tốt"*. Gộp hai câu lại thì ra
một phép kiểm rõ ràng — **mỗi lớp phải rộng hơn lớp ngay trên nó** — mà máy làm được.

### A. Người mà chính sách mô tả ở tr. 19–20

> *"Khi có một khoản tiền nhàn rỗi, họ đưa ngay vào Lớp rủi ro nhất như Cổ phiếu penny, Chứng khoán
> phái sinh, Forex, Crypto…"* — C1 tr. 19

Cho người đó 85 triệu: 5 triệu để dành, 80 triệu đổ vào crypto.

```
       mạo hiểm  94,1% ████████████████████████████████████████████████████████
    tăng trưởng   0,0% ·
   tạo thu nhập   0,0% ·
         bảo vệ   5,9% ████
        vô hình   0,0% ·
  ! lớp 'vô hình' HẸP HƠN lớp 'bảo vệ' nằm trên nó
  ! lớp 'tăng trưởng' HẸP HƠN lớp 'mạo hiểm' nằm trên nó
```

Không phải kim tự tháp. Đó là một cái đinh cắm ngược. **Hai chỗ gãy.**

### B. Cùng 85 triệu, xếp lại theo thứ tự sách khuyên

```
       mạo hiểm   5,9% ██████
    tăng trưởng  11,8% ███████████
   tạo thu nhập  23,5% ██████████████████████
         bảo vệ  58,8% ████████████████████████████████████████████████████████
        vô hình   0,0% ·
  ! lớp 'vô hình' HẸP HƠN lớp 'bảo vệ' nằm trên nó
```

Hai chỗ gãy xuống còn **một**. Và chỗ gãy còn lại **không phải lỗi xếp tiền** — lớp đáy đang rỗng
vì ta chưa đếm nó vào. Mà tr. 21 nói rõ tháp phải *"Bắt đầu với Lớp tài sản vô hình"*.

### C. Đếm cả lớp vô hình, đúng như sách bảo

Người này lương 10 triệu/tháng, nên theo phép ở tr. 22–23 (mục 6) lớp vô hình của họ đáng **1,33 tỷ**:

```
       mạo hiểm   0,4% █
    tăng trưởng   0,7% █
   tạo thu nhập   1,4% █
         bảo vệ   3,5% ██
        vô hình  94,0% ████████████████████████████████████████████████████████
  -> đúng hình tháp: mỗi lớp rộng hơn lớp trên nó
```

**Lớp vô hình chiếm 94% toàn bộ tháp. Bốn lớp hữu hình cộng lại chỉ 6%.**

### Hệ quả mà sách không rút ra

Với một người đi làm bình thường, tháp tài sản **đã sẵn đúng hình dạng** — không phải nhờ kỷ luật
đầu tư, mà chỉ vì lớp đáy là năng lực kiếm tiền và nó áp đảo mọi thứ khác. Bài tập ở tr. 24, nếu
làm đúng như sách bảo, gần như luôn cho ra hình tháp đẹp.

Nên câu hỏi có ích không phải *"tháp của tôi có cân không"*. Nó là hai câu khác:

> **(1)** Sáu phần trăm hữu hình kia có xếp đúng thứ tự không? — đó là chỗ tháp A và tháp B khác
> nhau, và là chỗ người ta thật sự phá sản.
>
> **(2)** Tôi đang làm gì để lớp đáy dày lên? — 94% tài sản nằm ở đó. **Bài 5** là bài về đúng câu
> hỏi này, và giờ thì rõ vì sao nó quan trọng đến thế.

Câu (2) cũng giải thích một chỗ của [bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#4-ba-bài-toán-và-bốn-bước-không-khớp-nhau):
kế hoạch bốn bước không có bước nào cho bài toán *kiếm tiền*, trong khi tháp tài sản của chính sách
nói phần lớn tài sản của bạn **nằm ở đó**.

---

## 6. [đính chính] Định giá lớp vô hình đo cái gì

Sách đưa ra cách định giá lớp đáy:

> *"Thu nhập hàng tháng của bạn là bao nhiêu? Ví dụ: giả sử anh A có mức lương 10 triệu đồng/tháng.
> Nhân con số đó với 12… là 120 triệu đồng. Lãi suất ngân hàng tại thời điểm này là 9%/năm. Bằng
> phép tính nhân chéo đơn giản, ta có con số **1,3 tỷ**."* — C1 tr. 22–23

Phép tính đúng: $120 \text{ triệu} \div 9\% = 1{,}33$ tỷ. Sách cũng rất sòng phẳng về giới hạn —
*"Dĩ nhiên đây chỉ là con số ước lượng"* (tr. 23). Nhưng có hai vấn đề mà sách không nêu, và cả hai
đều nằm sẵn trong chính hai cuốn sách.

### Vấn đề một: phép chia đó giả định thu nhập chảy về **mãi mãi**

Chia thu nhập cho lãi suất là phép vốn hoá một dòng tiền **không bao giờ dừng**. Nhưng C2 nói ngược:

> *"vốn con người sẽ giảm theo thời gian, do tuổi trẻ là giai đoạn tốt nhất cho sự học hỏi và phát
> triển, nhưng càng lớn tuổi thì 'vốn' sẽ giảm đi liền với sức khỏe bản thân."* — C2 tr. 13

Hai chỗ không thể cùng đúng. Cho chuỗi một điểm dừng:

| Số năm đi làm còn lại | Giá trị lớp vô hình | So với con số của sách |
| ---: | ---: | ---: |
| 10 năm | 770 triệu | 58% |
| 20 năm | 1,10 tỷ | 82% |
| 30 năm | 1,23 tỷ | 92% |
| 40 năm | 1,29 tỷ | 97% |

Người 45 tuổi còn 20 năm đi làm thì lớp vô hình của họ đáng **1,1 tỷ**, không phải 1,33 tỷ. Khoảng
cách ấy chính là điều C2 tr. 13 muốn nói.

### Vấn đề hai: con số bám vào lãi suất, không bám vào bạn

Đây là vấn đề nặng hơn. Giữ nguyên anh A — cùng năng lực, cùng mạng lưới, cùng lương — chỉ đổi lãi
suất ngân hàng:

| Lãi suất | Giá trị "năng lực" của anh A |
| ---: | ---: |
| 9% | 1,33 tỷ |
| 7% | 1,71 tỷ |
| 5% | 2,40 tỷ |
| **4%** | **3,00 tỷ** |

Lãi suất từ 9% xuống 4% thì "năng lực" của anh A **tăng gấp 2,3 lần**, trong khi anh A không học
thêm được gì, không quen thêm ai. Con số này nói về **thị trường tiền tệ** nhiều hơn nói về anh A.

Nó cũng có một hệ quả ngược đời: khi ngân hàng tăng lãi suất, "tài sản vô hình" của bạn **giảm**.

### [2026] Và mẫu số đã đổi

Sách viết khi lãi suất huy động 9%/năm, tức khoảng 2022–2023
([bài 0 mục 7](bai_00_bat_dau_tu_dau.md#7-sách-viết-năm-nào-và-cái-gì-đã-cũ)). Mức hiện tại thấp
hơn hẳn. Ai làm phép tính này hôm nay bằng lãi suất hôm nay sẽ ra một con số lớn hơn nhiều so với
1,3 tỷ — không phải vì họ giỏi hơn anh A.

### Vậy dùng con số đó thế nào

Đừng dùng nó như một **giá trị**. Dùng nó như một **thước đo tương đối**, và sách gợi đúng cách
dùng đó ở câu ngay sau:

> *"Nó trả về một kết quả mà nếu bạn không hài lòng về điều này, bạn sẽ có động lực để thay đổi
> định giá bản thân."* — C1 tr. 23

So con số của bạn hôm nay với con số của chính bạn năm ngoái, **giữ nguyên lãi suất** ở cả hai lần
tính. Chênh lệch khi đó phản ánh đúng thứ cần đo: thu nhập bạn tạo ra đã đổi bao nhiêu. Còn đem so
với người khác, hay so hai năm bằng hai mức lãi suất khác nhau, thì bạn đang đo lãi suất.

Đây cũng chính là mệnh đề của [bài 2 mục 8](bai_02_do_hien_trang.md#8-bổ-sung-tài-sản-ròng-cũng-là-một-ý-kiến)
lặp lại ở một tầng khác: **tài sản ròng là một ý kiến**, và lớp đáy của tháp là phần "ý kiến" nhất
trong toàn bộ bảng cân đối của bạn.

---

## 7. Tự thử

1. **Vẽ tháp của bạn.** Làm đúng bài tập C1 tr. 24. Liệt kê tài sản theo năm lớp, tính tỷ trọng.
   Có lớp nào hẹp hơn lớp trên nó không?

2. **Hai lần, có và không có lớp đáy.** Tính lại tháp của bạn **bỏ lớp vô hình ra**. Hình dáng đổi
   thế nào? Con số nào trong hai bản mô tả đúng hơn tình trạng của bạn — và để trả lời câu gì?

3. **Chạy code với số của bạn.** Trong `bai-04-thap-tai-san.py`, sửa ba tháp mẫu thành tháp của
   bạn. Máy báo bao nhiêu chỗ gãy?

4. **Ngôi nhà.** Bạn đang ở một căn nhà trị giá 2 tỷ, còn nợ ngân hàng 1,2 tỷ. Theo khung của sách
   (mục 1): đó là tài sản gì? Nó vào lớp nào của tháp? Và tài sản ròng đổi bao nhiêu nếu bạn cho
   thuê nó rồi đi ở trọ?

5. **Định giá bằng lãi suất hôm nay.** Tra lãi suất huy động 12 tháng của một ngân hàng bất kỳ. Áp
   vào phép tính ở mục 6 với thu nhập của bạn. So con số đó với con số tính bằng 9% của sách. Chênh
   bao nhiêu, và **cái gì** đã thay đổi giữa hai con số?

6. **Tìm chỗ ở của bốn tầng.** Mục 3 nói hai tầng của bản bốn tầng không có lớp tương ứng. Đọc lướt
   C2, tìm xem *"Lập kế hoạch"* và *"Tài sản cho thế hệ sau"* xuất hiện lại dưới tên nào, ở trang nào.

7. **Cãi lại mục 5.** Mục 5 kết luận tháp của người đi làm bình thường "đã sẵn đúng hình dạng". Tìm
   **một loại người** mà kết luận đó sai — và nói rõ vì sao.

---

## 8. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Tài sản | assets | *"những gì tạo ra lợi ích trong tương lai"* — C1 tr. 16 |
| Tài sản đầu tư | investment asset | tạo ra **tiền** trong tương lai (*future cash inflow*) |
| Tài sản tiêu dùng | consumption asset | tạo ra **chi phí** trong tương lai để duy trì; nhà để ở, xe |
| Tiêu sản | liability *(nghĩa của Kiyosaki)* | *"những gì lấy tiền trong túi bạn ra"*; xuất hiện **đúng một lần**, C1 tr. 16 |
| Nợ | liabilities | mọi nghĩa vụ phải trả — **rộng hơn** định nghĩa ở C1 tr. 17 |
| Tài sản vô hình | intangible asset | năng lực, mạng lưới, thương hiệu — C1 tr. 16, 22 |
| Tháp tài sản | asset pyramid | mô hình phân tầng theo rủi ro, xây từ đáy lên — C1 tr. 19–24 |
| Lớp bảo vệ | — | quỹ dự phòng 3–6 tháng chi tiêu; bài 9 |
| Lớp mạo hiểm · lớp rủi ro | — | đỉnh tháp, *"phần trăm phân bổ ít nhất"*; hai tên cho một lớp |
| **[bổ sung]** Vốn hoá vĩnh viễn | perpetuity | chia dòng tiền cho lãi suất; giả định dòng tiền không bao giờ dừng |
| **[bổ sung]** Quỹ chi tiêu | sinking fund | tầng *"Lập kế hoạch"* của bản bốn tầng; bài 9 |

---

## 9. Câu hỏi tự kiểm tra

1. Sách chê định nghĩa của Kiyosaki **sơ sài** vì hai lý do. Kể ra. (mục 1)
2. Theo khung của sách, ngôi nhà bạn đang ở là loại tài sản gì? Nếu đem cho thuê thì sao? (mục 1)
3. Từ *"tiêu sản"* xuất hiện **mấy lần** trong cả hai tập? Cặp từ nên nhớ thay cho nó là gì? (mục 1)
4. Định nghĩa nợ ở C1 tr. 17 bỏ sót loại nợ nào? Ai đọc theo đúng chữ đó tính tài sản ròng ra
   **cao hơn hay thấp hơn** sự thật? (mục 2)
5. Kể bốn tầng ở C1 tr. 20–21 và năm lớp ở C1 tr. 21. **Bao nhiêu tên trùng nhau?** (mục 3)
6. Hai mô hình đó chia theo hai tiêu chí nào? Vì sao không ánh xạ được vào nhau? (mục 3)
7. Bản nào được sách mô tả chi tiết và ra bài tập? Hai tầng của bản kia đi đâu trong khoá học? (mục 3)
8. Kể năm lớp **từ đáy lên đỉnh** kèm một ví dụ mỗi lớp. (mục 4)
9. Hai điều kiện lọc mà sách đặt cho việc xếp tài sản vào tháp là gì? Điều kiện thứ nhất nhất
   quán với chỗ nào ở C1 tr. 11? (mục 4)
10. Nguyên tắc *"phần bên dưới càng rộng càng tốt"* dịch thành phép kiểm nào? (mục 4, 5)
11. Tháp A ở mục 5 có **mấy** chỗ gãy? Xếp lại tiền thì còn mấy? Vì sao vẫn còn? (mục 5)
12. Khi đếm cả lớp vô hình, nó chiếm bao nhiêu phần trăm tháp? Hai câu hỏi có ích thay cho
    *"tháp của tôi có cân không"* là gì? (mục 5)
13. Phép $120 \text{ triệu} \div 9\%$ giả định điều gì về tương lai? Câu nào ở C2 tr. 13 mâu
    thuẫn với giả định đó? (mục 6)
14. Lãi suất từ 9% xuống 4% thì "năng lực" của anh A đổi bao nhiêu lần? Anh A đã làm gì để xứng
    với mức tăng đó? (mục 6)
15. Cách dùng đúng con số định giá lớp vô hình là gì, và phải giữ nguyên cái gì giữa hai lần
    tính? (mục 6)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 4 — TÀI SẢN, TIÊU SẢN, THÁP TÀI SẢN               C1 tr. 16-24     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  SÁCH BÁC KIYOSAKI, VÀ BÁC ĐÚNG                                         ║
║     Kiyosaki: tài sản = mang tiền vào / tiêu sản = lấy tiền ra           ║
║     => phân đôi này không xử được câu "ngôi nhà là gì"                   ║
║     SÁCH THAY BẰNG: tài sản = thứ tạo LỢI ÍCH trong tương lai, chia hai  ║
║        tài sản ĐẦU TƯ    -> tạo TIỀN     (gồm cả VÔ HÌNH)                ║
║        tài sản TIÊU DÙNG -> tạo CHI PHÍ  (nhà để ở, xe)                  ║
║     "tiêu sản" xuất hiện ĐÚNG 1 LẦN trong cả hai tập, rồi biến mất       ║
║                                                                          ║
║  NỢ ĐỊNH NGHĨA QUÁ HẸP   "các khoản vay để TẠO RA tài sản" (tr.17)       ║
║     bỏ sót nợ tiêu dùng => tài sản ròng tính ra CAO HƠN sự thật          ║
║                                                                          ║
║  SÁCH ĐƯA HAI CÁI THÁP VÀ KHÔNG NỐI CHÚNG                               ║
║     tr.20-21  BỐN TẦNG: bảo vệ · lập kế hoạch · mục tiêu ưu tiên ·      ║
║                         tài sản cho thế hệ sau        (chia theo MỤC ĐÍCH)║
║     tr.21-24  NĂM LỚP:  vô hình · bảo vệ · tạo thu nhập · tăng trưởng · ║
║                         mạo hiểm                      (chia theo RỦI RO) ║
║     => ĐÚNG MỘT TÊN TRÙNG ("bảo vệ") trên tổng 4 và 5                    ║
║     bản bốn tầng hiện 1 lần rồi biến mất; bài tập tr.24 hỏi về "lớp"     ║
║     đỉnh tháp cũng hai tên: "Lớp rủi ro" (tr.19,21) / "mạo hiểm"(tr.23)  ║
║                                                                          ║
║  BÀI TẬP tr.24 + NGUYÊN TẮC tr.21 = MỘT PHÉP KIỂM CHẠY ĐƯỢC            ║
║     "phần bên dưới càng rộng càng tốt" => mỗi lớp phải rộng hơn lớp trên ║
║     A. người của tr.19-20 (85tr, 80tr vào crypto):  2 chỗ gãy            ║
║     B. cùng 85tr xếp lại:                           1 chỗ gãy            ║
║     C. đếm cả lớp vô hình (1,33 tỷ):                0 — đúng hình tháp   ║
║        lớp vô hình = 94% tháp · bốn lớp hữu hình = 6%                    ║
║     => tháp người đi làm ĐÃ SẴN đúng hình. Hai câu hỏi thật:             ║
║        (1) 6% hữu hình có xếp đúng thứ tự không?                         ║
║        (2) đang làm gì để lớp đáy dày lên?  -> bài 5                     ║
║                                                                          ║
║  ĐỊNH GIÁ LỚP VÔ HÌNH ĐO CÁI GÌ?   120tr/năm ÷ 9% = 1,33 tỷ (tr.22-23)  ║
║     (a) giả định thu nhập chảy về MÃI MÃI — C2 tr.13 nói ngược lại       ║
║         còn 20 năm đi làm  ->  1,10 tỷ, chỉ 82%                          ║
║     (b) bám vào LÃI SUẤT, không bám vào bạn                              ║
║         9% -> 4%: "năng lực" anh A tăng GẤP 2,3 LẦN mà không học gì      ║
║         lãi suất TĂNG thì "tài sản vô hình" của bạn GIẢM                 ║
║     DÙNG ĐÚNG: so với chính mình năm ngoái, GIỮ NGUYÊN lãi suất cả 2 lần ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1***, Waka.vn.
  - **Unit 3 Lesson 1 *Khái niệm tài sản* (tr. 16–17)** — nguồn chính: định nghĩa của Kiyosaki và
    lời phản bác, định nghĩa thay thế, tài sản đầu tư / tài sản tiêu dùng, dạng hữu hình và vô hình
    (tr. 16); tài sản tiêu dùng, định nghĩa nợ, *"Không có lời khuyên nào phù hợp cho tất cả"*,
    *"Dòng tiền thuần và Tài sản thuần luôn là con số dương"* (tr. 17)
  - Unit 3 Lesson 2 (tr. 18) — bảng cân đối tài chính cá nhân; đã làm ở bài 2
  - **Unit 3 Lesson 3 *Kim tự tháp tài sản* (tr. 19–24)** — nguồn chính: người nghiệp dư dồn tiền
    vào *"Lớp rủi ro nhất"* (tr. 19–20); **bản bốn tầng** (tr. 20–21); *"Nguyên tắc xây dựng"* và
    **bản năm lớp**, *"xây dần từ đế lên"*, loại trừ trading ngắn hạn (tr. 21); lớp vô hình và phép
    định giá (tr. 22–23); lớp bảo vệ, tạo thu nhập, tăng trưởng (tr. 23); lớp mạo hiểm và **bài tập
    cuối bài** (tr. 24)
  - Unit 2 Lesson 3 (tr. 11) — trading là hoạt động kinh doanh; bài 2
- ***Tài chính cá nhân 101 — Class 2***, Waka.vn.
  - Unit 1 Lesson 3 (tr. 13) — *"'vốn' sẽ giảm đi liền với sức khỏe bản thân"*
  - Unit 2 Lesson 1 (tr. 16) — chiếc ô tô 200 triệu với khoản nợ 300 triệu
  - Unit 4 Lesson 2 (tr. 43–45) — quỹ khẩn cấp và quỹ chi tiêu; bài 9
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-04-thap-tai-san.py`](../thuc_hanh/bai-04-thap-tai-san.py).
  Ba tháp ở mục 5, mọi tỷ trọng, và cả hai bảng định giá ở mục 6 do tệp này tính. Việc *"đúng một
  tên trùng nhau"* giữa hai mô hình cũng do code đối chiếu hai danh sách chứ không đếm tay.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Quan sát rằng **hai mô hình tháp không ánh xạ được vào nhau** ([mục 3](#3-sách-đưa-hai-cái-tháp-và-không-bao-giờ-nối-chúng-lại))
    là của khoá học. Sách in cả hai và không bình luận gì.
  - **Ba tháp A / B / C ở [mục 5](#5-bổ-sung-làm-bài-tập-của-tr-24-và-kiểm-nguyên-tắc-của-tr-21)
    là số liệu do khoá học dựng.** Sách chỉ mô tả hành vi của người ở tr. 19–20 mà không cho con số.
    Phép kiểm "mỗi lớp phải rộng hơn lớp trên nó" là cách khoá học **hình thức hoá** câu *"phần bên
    dưới càng rộng càng tốt"* của tr. 21.
  - Kết luận rằng lớp vô hình áp đảo tháp (94%) và hai câu hỏi thay thế **không có trong sách**.
  - Hai bảng độ nhạy ở [mục 6](#6-đính-chính-định-giá-lớp-vô-hình-đo-cái-gì) (theo số năm còn lại,
    và theo lãi suất) là của khoá học. Sách chỉ đưa **một** con số, ở **một** mức lãi suất.
- **Liên hệ chéo:**
  - Bảng cân đối và tài sản ròng: [bài 2](bai_02_do_hien_trang.md).
  - Vì sao kế hoạch bốn bước bỏ trống bài toán kiếm tiền:
    [bài 1 mục 4](bai_01_tai_chinh_ca_nhan_la_gi.md#4-ba-bài-toán-và-bốn-bước-không-khớp-nhau).
  - Lãi suất 9% và những gì đã cũ:
    [bài 0 mục 7](bai_00_bat_dau_tu_dau.md#7-sách-viết-năm-nào-và-cái-gì-đã-cũ).
  - Tài sản vô hình ở tầm doanh nghiệp, và vì sao chúng khó lên bảng cân đối:
    [Trí tuệ tài chính bài 4](../../trituetaichinh/ly_thuyet/bai_04_bang_can_doi_ke_toan.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| **4** | **Tài sản, tiêu sản, tháp tài sản** ← *bạn đang ở đây* | C1 tr. 16–24 | 1 |
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
