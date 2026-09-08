# Ngân hàng — thanh khoản, bank run, Basel

> Bài học dựa trên buổi **13 "Banks"** của khoá **Yale ECON 252 *Financial Markets*** (Xuân 2011),
> giảng viên **Robert J. Shiller**, YouTube `1mDL1fKEVZM`, 73:19.
> Mốc dạng `13 33:03` = **buổi 13, phút 33:03**, đã đối chiếu ngược với phụ đề gốc bằng script.
> Phần **📚 Mở rộng** và **🇻🇳 Góc Việt Nam** không có trong video.
> ⚠️ **Video ghi Xuân 2011** — §10 đối chiếu với 2026, và §9 liệt kê bốn chỗ video nói sai.
> 📌 **Đọc cùng:** [MIT 15.401 bài 5 — chứng khoán hoá](../../mit-15401-finance/ly_thuyet/bai_05_duration_va_chung_khoan_hoa.md)
> giải thích cỗ máy tạo AAA mà §7 dưới đây nói tới hậu quả.

## Mục lục

1. [Ngân hàng là gì — hai chênh lệch, không phải một](#1-ngân-hàng-là-gì--hai-chênh-lệch-không-phải-một)
2. [Từ con cừu Sumer tới thợ kim hoàn London](#2-từ-con-cừu-sumer-tới-thợ-kim-hoàn-london)
3. [📚 Diamond–Dybvig — vì sao một ngân hàng lành mạnh vẫn sập](#3--diamonddybvig--vì-sao-một-ngân-hàng-lành-mạnh-vẫn-sập)
4. [Ba bài toán ngân hàng giải mà thị trường không giải được](#4-ba-bài-toán-ngân-hàng-giải-mà-thị-trường-không-giải-được)
5. [Bảo hiểm tiền gửi và bốn lần thử](#5-bảo-hiểm-tiền-gửi-và-bốn-lần-thử)
6. [Basel — tài sản có rủi ro và yêu cầu vốn](#6-basel--tài-sản-có-rủi-ro-và-yêu-cầu-vốn)
7. [Chỗ Basel đẩy sai hướng — 71 triệu so với 14 triệu](#7-chỗ-basel-đẩy-sai-hướng--71-triệu-so-với-14-triệu)
8. [Ba cuộc khủng hoảng và một mẫu hình](#8-ba-cuộc-khủng-hoảng-và-một-mẫu-hình)
9. [⚠️ Bốn chỗ video nói sai](#9--bốn-chỗ-video-nói-sai)
10. [⚠️ Đối chiếu 2026](#10--đối-chiếu-2026)
11. [🇻🇳 Góc Việt Nam — hạn mức bảo hiểm tiền gửi](#11--góc-việt-nam--hạn-mức-bảo-hiểm-tiền-gửi)
12. [Chương trình](#12-chương-trình)
13. [Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
14. [Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)

---

## 1. Ngân hàng là gì — hai chênh lệch, không phải một

Shiller mở buổi bằng việc rào ba lần cho chắc (`13 02:52`–`13 03:28`): bài này nói về **ngân hàng
thương mại** — nơi nhận tiền gửi rồi cho vay. Không phải ngân hàng đầu tư, vốn *"không nhận tiền
gửi"* và đặc trưng là **bảo lãnh phát hành chứng khoán**. Cũng không phải ngân hàng trung ương, vốn
là *"tổ chức của chính phủ quản lý cung tiền của một quốc gia"*.

Rào chắn này quan trọng hơn vẻ ngoài của nó. Ba loại định chế trên chịu ba chế độ quản lý khác nhau,
và §10 dưới đây sẽ cho thấy chính chỗ nhập nhằng giữa chúng là nơi khủng hoảng 2008 chui qua.

Chữ **bank** đến từ *cái bàn* hoặc *mặt quầy* nơi người làm nghề ngồi giao dịch, xuất hiện trong
tiếng Anh thế kỷ 15 (`13 03:56`). Còn nghề thì có trước cái tên rất lâu.

### Chênh lệch thứ nhất: lãi suất

Đặc trưng cốt lõi, theo Shiller (`13 04:25`): ngân hàng kiếm **thu nhập chênh lệch** — vay vào ở lãi
suất thấp, cho vay ra ở lãi suất cao, ăn phần chênh.

Đơn giản đến mức dễ tưởng là đã xong. Nhưng ngay sau đó Shiller tự bác: *"tôi không chắc cái đó đã
tóm gọn được"* (`13 04:57`).

### Một chức năng đã biến mất: phát hành tiền giấy

Trước khi sang chênh lệch thứ hai, Shiller rẽ ngang một đoạn đáng giá (`13 05:05`–`13 08:26`). Nếu
chặn một người trên phố **hai trăm năm trước** mà hỏi bản chất của ngân hàng là gì, câu trả lời đầu
tiên sẽ là: *nó in tiền*.

Ngày nay hầu như không còn. Ngân hàng tư nhân phát hành tiền giấy chỉ còn tập trung ở hai nơi
(`13 06:09`): **Anh** — tám ngân hàng vẫn in bảng — và **Hồng Kông** — ba ngân hàng, gồm HSBC,
Standard Chartered và Bank of China (Hong Kong).

Vì sao mất? Shiller trả lời gọn (`13 07:31`): vì *"những tờ giấy đó mất giá quá nhiều lần trong các
cuộc khủng hoảng tài chính"*, nên chính phủ ra luật cấm.

Ông kể một chuyện nhỏ minh hoạ (`13 06:46`): mang tờ bảng Scotland đi tàu sang Pháp, người soát vé
nhìn rồi hỏi *"cái gì đây?"* và từ chối nhận — dù nó là bảng Anh hợp pháp, giao dịch ngang giá với
tiền của Bank of England. Rồi ông chỉ vào tờ đô la trong túi sinh viên: nó ghi tên **một trong 12
Ngân hàng Dự trữ Liên bang**. Ở New Haven thì phần lớn là tiền của Fed Boston. *"Nếu đây là năm 1750
và bạn có tiền Boston trong túi — vì ta đang ở Connecticut — bạn sẽ gặp rắc rối"* (`13 08:14`). Phải
tìm người đổi tiền, vì chẳng ai biết hay tin ngân hàng Boston.

Rẽ ngang này không thừa: nó cho thấy **tính đồng nhất của tiền là một thành tựu**, không phải mặc
định. Cái ta coi là hiển nhiên hôm nay từng phải xây bằng luật.

### Chênh lệch thứ hai: kỳ hạn — và đây mới là chỗ gãy

Đến `13 08:52` Shiller nêu thứ khác hẳn: ngân hàng **tạo ra thanh khoản bằng cách vay ngắn cho vay
dài**. Ông nói rõ đây *"khác với thu nhập chênh lệch"* — chênh lệch kia là về **lãi suất**, cái này
là về **kỳ hạn**.

Người mua nhà muốn khoá tiền 30 năm. Người gửi tiết kiệm muốn rút bất cứ lúc nào. Ngân hàng đứng
giữa và hứa với **cả hai** (`13 09:19`–`13 10:03`):

|               | Người gửi                    | Người vay                |
| ------------- | ---------------------------- | ------------------------ |
| Nhận được     | tài khoản rút bất cứ lúc nào | khoản vay 30 năm         |
| Ngân hàng hứa | tiền của bạn luôn sẵn sàng   | tiền của bạn khoá 30 năm |

Cả hai lời hứa đều thật — **miễn là đừng ai đến đòi cùng lúc**. Shiller nói thẳng hệ quả
(`13 10:15`): *"nếu mọi người cùng đòi rút tiền một lúc, họ không làm được. Ngân hàng trong hoàn
cảnh bình thường tạo ra thanh khoản, nhưng nó tạo ra một hệ thống dễ tổn thương."*

Rồi câu kết luận lịch sử (`13 10:36`): ngành ngân hàng *"bị hành hạ bởi những cuộc khủng hoảng liên
tiếp suốt chiều dài lịch sử"*.

📚 **Chỗ cần tách bạch.** Chênh lệch lãi suất là nguồn thu **vô hại** — nếu ngân hàng chỉ làm việc
đó, nó là một quỹ đầu tư bình thường, lỗ thì cổ đông chịu. Chênh lệch kỳ hạn vừa là nguồn thu vừa là
**cơ chế sụp đổ**, và người chịu không chỉ có cổ đông. Toàn bộ phần còn lại của bài học này là hệ
quả của một câu duy nhất: hai chênh lệch đó không cùng loại. [Mục 1 của chương trình](#12-chương-trình)
tách chúng ra bằng số.

---

## 2. Từ con cừu Sumer tới thợ kim hoàn London

Shiller đi ngược tới gốc, và gốc không phải ngân hàng — mà là **lãi suất** (`13 11:03`).

### Chữ "lãi" đầu tiên có nghĩa là "con cừu non"

Từ *interest* xuất hiện lần đầu trong tiếng **Sumer**, thư tịch cổ nhất khoảng **2000 trước Công
nguyên**, viết là **`mas`** (`13 11:18`–`13 11:41`). Cùng một từ ấy còn có nghĩa **cừu non**.

Một sử gia kinh tế đặt câu hỏi vì sao, và giả thuyết của ông là: ý tưởng cho vay lấy lãi mọc ra từ ý
tưởng cũ hơn — **cho thuê đất** (`13 11:51`–`13 12:31`). Anh có mảnh đất không dùng, cho người khác
thuê, người ta nuôi cừu trên đó. Anh nói: tôi cần chút hoa lợi từ đất để bù cho việc cho anh dùng.
Người kia đáp: được, tôi trả anh bằng đám cừu non.

Shiller rút ra ý (`13 12:35`): *"Nếu tôi cho anh vay tiền, tôi đang trao cho anh nguồn lực sản xuất,
và nó sẽ sinh ra thứ gì đó. Ta gọi thứ đó là cừu non."*

📚 Nhìn kỹ thì đây không phải chuyện từ nguyên vui vẻ. Nó là **lập luận biện minh cho lãi suất**,
xuất hiện cùng lúc với chính khái niệm ấy, và nó vẫn là lập luận đang dùng hôm nay: vốn sinh ra sản
lượng, nên vốn có giá. Ba nghìn năm sau, người ta vẫn cãi nhau bằng đúng câu đó — §8 của
[buổi 8](../../mit-15401-finance/ly_thuyet/bai_04_trai_phieu_va_duong_cong.md) là lịch sử cho vay
nặng lãi, tức lịch sử của phe phản đối.

### Không cần tiền vẫn làm được ngân hàng

Shiller nói ông không biết Sumer có ngân hàng chưa, nhưng *"chắc là có"* — vì làm ngân hàng chỉ cần
**làm cả hai vế** (`13 13:03`). Và quan trọng: người ta không nhất thiết cho vay **tiền**. Họ cho
vay **lúa mạch hoặc lúa mì**, và tính lãi bằng lúa mì. *"Bạn không cần tiền để làm ngân hàng"*
(`13 13:23`).

Ghi chú khác: ghi chép lãi suất đầu tiên ở **Trung Quốc** là thời **nhà Tống**, năm **960–1279**
(`13 13:44`) — đúng lúc họ đang phát minh **tiền giấy**.

### Ngân hàng còn sống lâu nhất thế giới

Ngân hàng hiện đại xuất hiện ở **Ý thời Phục hưng**, và ngân hàng cổ nhất còn tồn tại là **Banca
Monte dei Paschi** ở **Siena**, lập năm **1472** (`13 14:37`–`13 15:28`). Tên nó nghĩa là *ngân hàng
của ngọn núi cừu* — Shiller đùa rằng chắc lại cùng cái phép ẩn dụ ấy.

Hai chi tiết ông nhấn (`13 15:44`–`13 16:22`), và cả hai đều sẽ quay lại ở §10:

1. Nó được lập ra như **một tổ chức từ thiện**, để **cho người nghèo vay**, bằng tiền của các nhà
   hảo tâm giàu có ở Ý.
2. Vào **thập niên 1600**, Công tước xứ Siena tuyên bố **bảo lãnh toàn bộ tiền gửi**. Tức là **bảo
   hiểm tiền gửi cũng được phát minh ở Ý**, ba trăm năm trước FDIC.

Shiller nói ông đã tới đó; tầng trệt gần sảnh có một bảo tàng nhỏ. Năm 2011 nó là **ngân hàng lớn
thứ ba nước Ý**.

### Thợ kim hoàn London: tiền giấy tự mọc ra

Phần lịch sử Anh, Shiller lấy từ **Clive Day, *History of Commerce* (1907)** — một giáo sư Yale đời
trước, sách đã hết bản quyền và đọc được trên Google Books (`13 16:41`–`13 16:57`).

Câu chuyện (`13 17:14`–`13 18:58`):

1. Thợ kim hoàn làm đồ vàng nên có **két sắt tốt**. Người ta gửi vàng nhờ giữ.
2. Thợ kim hoàn đưa lại **một tờ giấy** hứa trả số vàng ấy.
3. Đi chợ, khách trả bằng tờ giấy đó — nhưng phải **ký hậu** sang tên người bán.
4. Tờ giấy lưu thông với ngày càng nhiều chữ ký hậu. Cuối cùng thợ kim hoàn bảo: thôi khỏi ký hậu,
   ghi luôn **"trả cho người cầm phiếu"**.
5. Rồi họ để ý: vàng nằm im trong két, chẳng ai đến đòi nữa. **Vậy đem cho vay đi.**

Shiller thêm một quan sát sắc (`13 18:47`): họ **không phải trả lãi** cho tờ phiếu, vì người ta giữ
nó chỉ để được cất hộ. *"Chắc họ vẫn trả lãi, theo nghĩa là họ cung cấp dịch vụ giữ hộ."*

📚 Bước 5 chính là **dự trữ một phần**, và nó xuất hiện **không do ai thiết kế**. Không có luật nào
cho phép, không có nhà kinh tế nào đề xuất. Nó mọc ra vì có lãi và vì chưa ai kịp cấm. Mọi thứ ở §3
tới §7 — Diamond–Dybvig, FDIC, Basel — đều là ba trăm năm loài người chạy theo dọn dẹp cái quyết
định mà một thợ kim hoàn nào đó ở London đã tự tiện đưa ra.

### Bốn loại ngân hàng ở Mỹ

Shiller liệt kê (`13 20:04`–`13 23:36`), số liệu **2010**:

| Loại                        |    Tổng tài sản 2010 | Nguồn gốc                         | Cho vay chính    |
| --------------------------- | -------------------: | --------------------------------- | ---------------- |
| Ngân hàng thương mại        | **14,6 nghìn tỷ đô** | loại cổ điển                      | vay doanh nghiệp |
| — trong đó *do Mỹ cấp phép* |   *10,1 nghìn tỷ đô* |                                   |                  |
| Ngân hàng tiết kiệm         |      1,2 nghìn tỷ đô | phong trào **từ thiện** thế kỷ 19 | vay mua nhà      |
| Quỹ tín dụng                |      0,9 nghìn tỷ đô | phong trào xã hội, câu lạc bộ     | vay mua nhà      |

Hai điều đáng chú ý:

- **Gần một phần ba** ngân hàng thương mại hoạt động ở Mỹ là **ngân hàng nước ngoài** — HSBC, các
  ngân hàng Thuỵ Sĩ, Deutsche Bank (`13 21:00`, `13 21:29`).
- **Ngân hàng tiết kiệm và quỹ tín dụng đều sinh ra từ động cơ từ thiện.** Ngân hàng thương mại
  ngày xưa *"không nhận tiền gửi nhỏ, phải đủ mức tối thiểu, họ không giao dịch với người thường"*
  (`13 22:39`). Nên người ta lập loại ngân hàng khác cho người thu nhập thấp.

⚠️ Shiller nhắc kỹ (`13 23:36`): đây là **tài sản**, không phải vốn hoá thị trường. Vốn hoá thấp hơn
nhiều, vì đối ứng với đám tài sản đó là **nợ phải trả người gửi tiền**. Nhầm hai thứ này là nhầm
toàn bộ §6.

---

## 3. 📚 Diamond–Dybvig — vì sao một ngân hàng lành mạnh vẫn sập

Shiller giới thiệu mô hình rồi nói thẳng *"tôi sẽ không trình bày mô hình, chỉ kể cho các bạn về
nó"* (`13 24:52`). Mục này trình bày mô hình đó, vì nó là **trục của cả buổi giảng** và không nắm nó
thì §5 tới §7 chỉ còn là danh sách sự kiện.

⚠️ **Shiller đọc sai năm.** Ông nói mô hình đăng trên *Journal of Political Economy* năm **1988**
(`13 24:41`). Bài gốc là **1983**, JPE tập 91 số 3, trang 401–419. Xem [§9](#9--bốn-chỗ-video-nói-sai).

### Bối cảnh

100 người, mỗi người có 1 đơn vị ở kỳ 0. Một công nghệ sản xuất:

- rút ở **kỳ 1** (sớm): thu về đúng **1** — thanh lý giữa chừng thì không sinh lời gì;
- để tới **kỳ 2**: thành **2**.

Vấn đề: **25% số người sẽ cần tiêu ở kỳ 1**, nhưng ở kỳ 0 **chưa ai biết mình có nằm trong nhóm đó
không**. Đây là rủi ro cá nhân, không phải rủi ro của nền kinh tế.

**Không có ngân hàng:** ai hoá ra là người "gấp" buộc phải thanh lý sớm và chỉ nhận **1**. Người
kiên nhẫn nhận **2**.

**Có ngân hàng:** gom tiền lại, hứa trả người rút sớm **r₁ = 1,28** và người đợi tới kỳ 2 phần còn
lại:

|                 | Không ngân hàng | Có ngân hàng |  Thay đổi |
| --------------- | --------------: | -----------: | --------: |
| Người gấp       |           1,000 |    **1,280** | **+28 %** |
| Người kiên nhẫn |           2,000 |    **1,813** |    −9,3 % |

Người gấp được thêm 28%, người kiên nhẫn mất 9,3%. Nhưng ở **kỳ 0**, khi chưa ai biết mình thuộc
nhóm nào, **mọi người đều thích hợp đồng ngân hàng hơn** — vì nó bảo hiểm cho họ chống lại rủi ro
"hoá ra mình cần tiền sớm".

Đây đúng ý Shiller (`13 25:03`): thanh khoản là *"một thứ hàng hoá kinh tế mà bạn có được từ hư
không. Y hệt đa dạng hoá danh mục — ta không cần bỏ ra nguồn lực nào để có đa dạng hoá, chỉ cần quản
danh mục cho đúng."*

Không ai bỏ thêm gì vào. Tổng nguồn lực không đổi. **Phúc lợi tăng chỉ nhờ sắp xếp lại.**

### Cân bằng thứ hai

Nhưng hợp đồng đó có **hai** cân bằng, và đó là toàn bộ luận điểm của bài báo (`13 25:41`).

Nếu ai cũng tin hệ thống lành mạnh, chỉ 25 người gấp đến rút, mọi thứ chạy đẹp.

Nếu ai cũng tin sắp có tháo chạy, thì **rút ngay là hành động đúng** — kể cả với người kiên nhẫn.
Và khi cả 100 người cùng đến kỳ 1:

```
tong von thanh ly duoc     100,00 don vi
moi nguoi doi                1,28 don vi
so nguoi duoc tra DU            78
nguoi thu 79 nhan            0,16 don vi
so nguoi nhan SO KHONG          21
```

**Ngân hàng này không hề mất khả năng thanh toán.** Tài sản vẫn đủ 100 đơn vị. Nó chỉ không thể biến
100 đơn vị của kỳ 2 thành 128 đơn vị ở kỳ 1.

Chỗ đáng sợ nằm ở đây: **không ai làm gì sai cả**. Người thứ 90 xếp hàng không phải kẻ hoảng loạn phi
lý — anh ta tính đúng. Nếu 89 người trước đã rút thì phần anh ta bằng không. Xếp hàng sớm là **hành
vi hợp lý**. Và chính vì nó hợp lý nên nó xảy ra.

Shiller tóm (`13 25:52`): *"chỉ cần người ta đột ngột đổi kỳ vọng, và thế là mọi thứ sụp đổ."*

### Không có mức r₁ nào an toàn

Đánh đổi này không tránh được. Tăng r₁ = bảo hiểm hào phóng hơn, nhưng chịu được ít người rút hơn:

|       r₁ | Người kiên nhẫn nhận |                     Chịu được bao nhiêu người rút |
| -------: | -------------------: | ------------------------------------------------: |
|     1,00 |                2,000 | 100 — không bảo hiểm gì, nên **không thể có run** |
|     1,20 |                1,867 |                                                83 |
| **1,28** |            **1,813** |                                            **78** |
|     1,50 |                1,667 |                                                66 |

Chỉ có đúng một điểm miễn nhiễm bank run: **r₁ = 1,00**, tức không bảo hiểm gì cả, tức không có ngân
hàng. Mọi mức hữu ích đều mong manh.

Kết luận của Diamond–Dybvig — và Shiller nói rõ đây là **đóng góp chính** của bài báo (`13 26:04`) —
là **lý do kinh tế cho bảo hiểm tiền gửi**: cần một bên thứ ba đủ lớn đứng ra bảo lãnh, để cân bằng
xấu không bao giờ được kích hoạt.

⚠️ Shiller nêu luôn giới hạn (`13 26:31`): bank run có thể bị châm ngòi bởi **cú sốc ngẫu nhiên**
nằm ngoài mô hình. Khủng hoảng vừa rồi bắt đầu từ **bong bóng bất động sản** — *"không phải thứ được
biểu diễn trong Diamond và Dybvig"*. Mô hình giải thích **cơ chế** sụp đổ, không giải thích **ngòi
nổ**.

---

## 4. Ba bài toán ngân hàng giải mà thị trường không giải được

Thanh khoản mới là một. Shiller nêu thêm hai, và cả hai đều là bài toán **thông tin**.

### Lựa chọn ngược — vì sao không tự đi vay thẳng công chúng

Doanh nghiệp cần tiền xây nhà máy có lựa chọn khác: **phát hành trái phiếu hoặc thương phiếu**, vay
thẳng công chúng qua một ngân hàng đầu tư, không cần trung gian tín dụng (`13 27:51`).

Vấn đề (`13 28:24`): *"công chúng không dễ đánh giá được chất lượng của công ty."*

Cơ chế hỏng, theo lời Shiller (`13 28:48`–`13 29:25`): người **biết** sẽ mua hết hàng tốt. Người
không biết bắt đầu nghĩ — *"sao món này lại được chào cho tôi? Tôi có phải thằng ngốc đâu, tôi chỉ
là không biết."* Nhắm mắt mua bừa thì **chắc chắn nhận phần tệ nhất**, vì *"họ sẽ dúi giấy xấu cho
tôi."*

Ngân hàng giải bằng cách **ở trong cộng đồng** (`13 29:25`). Và Shiller mô tả rất cụ thể
(`13 30:00`–`13 30:38`): cán bộ tín dụng theo truyền thống là người **dính vào đời sống địa phương**
— tên trong danh sách tài trợ dàn nhạc, có mặt ở đủ loại sự kiện, chơi golf với giới doanh nhân,
**nghe đủ thứ chuyện**. Ai đó nói *"cái ông CEO ấy, tôi nghĩ ông ta nghiện rượu, coi chừng"* — và
hôm sau ông ta không được duyệt vay.

Shiller kết bằng một câu hơi ngại (`13 30:34`): *"tôi ngại phải nói thế, nhưng họ kiểu như bảo lãnh
cho nhân cách của người ta."* Rồi giải thích vì sao phải vậy (`13 30:44`): *"anh không thể chứng
minh hay đánh giá ai là người tốt. Anh không thể viết ra một cách khách quan rằng ai sẽ là một doanh
nhân có trách nhiệm."*

📚 Đây là luận điểm mạnh hơn vẻ ngoài. Nó nói rằng **có loại thông tin không thể chứng khoán hoá** —
không viết được vào hợp đồng, không nhét được vào mô hình chấm điểm. Ngân hàng tồn tại vì nó là nơi
chứa loại thông tin ấy. Và điều đó dự báo luôn chuyện gì xảy ra khi ta thay cán bộ tín dụng địa
phương bằng chấm điểm tự động rồi bán khoản vay đi — đúng cỗ máy mà
[MIT 15.401 bài 5](../../mit-15401-finance/ly_thuyet/bai_05_duration_va_chung_khoan_hoa.md) mổ xẻ.

### Rủi ro đạo đức — và chuyến đi trường đua

Bài toán thứ hai (`13 31:08`): người vay có thể cầm tiền rồi **đánh một ván lớn**.

Ví dụ của Shiller (`13 31:17`–`13 32:20`), giữ nguyên giọng: ta có công ty nhỏ đang làm ăn bết bát.
Ta vay **10 triệu đô**, mang hết ra **trường đua**, đặt vào **con ngựa ít khả năng thắng nhất**. Cơ
hội thắng 1 trên 10, nhưng thắng thì được **100 triệu**. Thua thì *"ừ thì phá sản thôi. Ta nói: xin
lỗi nhé."*

*"Công ty của anh dù sao cũng sắp chết, anh chẳng còn triển vọng gì."* Thắng thì trả hết nợ, ai cũng
vui. Thua thì chủ nợ chịu. Shiller gọi tên nó ở `13 32:20`: **trách nhiệm hữu hạn**.

Ngân hàng giải bằng **giám sát liên tục** (`13 32:22`): họ cho vay thương mại **thực chất dài hạn
nhưng trên giấy tờ là ngắn hạn**, cứ đến hạn lại gia hạn — và **cắt được bất cứ lúc nào** khi thấy
anh làm điều gì có mùi rủi ro đạo đức.

Shiller chốt (`13 32:42`): giám sát liên tục giải rủi ro đạo đức, y như thu thập thông tin giải lựa
chọn ngược.

📚 **Ba bài toán, một cấu trúc.** Thanh khoản, lựa chọn ngược, rủi ro đạo đức — cả ba đều là thứ
**hợp đồng viết ra giấy không xử lý được**, và ngân hàng xử lý được nhờ **quan hệ kéo dài theo thời
gian**. Đó là lý do ngân hàng không bị thay thế bởi thị trường trái phiếu, dù thị trường trái phiếu
rẻ hơn.

Và nó cũng báo trước §6: khi cơ quan quản lý đo rủi ro của ngân hàng bằng **một bảng trọng số cố
định**, họ đang đo đúng cái thứ mà ngân hàng tồn tại để nói rằng không đo được.

---

## 5. Bảo hiểm tiền gửi và bốn lần thử

Bảo hiểm tiền gửi có **lịch sử lẫn lộn** (`13 33:55`) — Shiller dùng đúng chữ *checkered*.

### Lần 1: FDIC, 1933 — thành công không ai giải thích nổi

Trước FDIC, nhiều bang và chính quyền địa phương Mỹ đã lập quỹ bảo hiểm tiền gửi, và **phần lớn đổ**
— tới mức *"người ta bảo đây là ý tưởng điên rồ"* (`13 33:55`).

Rồi năm **1933**, trong khuôn khổ **New Deal** của Roosevelt, **Federal Deposit Insurance
Corporation** ra đời (`13 34:14`). Shiller: *"và tới hôm nay nó chưa bao giờ đổ."*

Vì sao? Shiller thừa nhận **không rõ** (`13 34:39`): *"Khó mà biết chính xác."* Giả thuyết của ông
(`13 34:46`): nó tạo ra **một trạng thái tâm lý** — người ta thôi lo về chuyện ngân hàng sập, vì tin
mình được bảo hiểm. Rồi ông đùa: *"chắc họ tin Franklin Delano Roosevelt."*

Và ông nối thẳng về §3 (`13 35:08`): *"chừng nào người ta còn tin hệ thống ngân hàng lành mạnh, thì
nó lành mạnh."* Đó chính là chọn cân bằng tốt.

### Lần 2: FSLIC — quỹ bảo hiểm tự phá sản

Mỹ lập thêm **Federal Savings and Loan Insurance Corporation (FSLIC)** cho các hiệp hội tiết kiệm và
cho vay (`13 35:15`).

Cái này **đổ** (`13 35:26`).

Khủng hoảng S&L thập niên 1980. Điều xảy ra, theo Shiller (`13 36:08`–`13 36:27`): FSLIC có dự trữ
đủ cho một mức lỗ nhất định, **nhưng lỗ vượt qua sạch**. Rồi họ phá sản. **Chính công ty bảo hiểm
phá sản.**

Chính phủ Mỹ đứng ra trả. Tổng hoá đơn: **150 tỷ đô** (`13 36:27`). FSLIC không còn tồn tại; các
hiệp hội S&L nay do FDIC bảo hiểm.

### Câu quan trọng nhất trong cả buổi

Từ đó Shiller rút ra một điều mà phần còn lại của bài học này xoay quanh (`13 36:47`–`13 37:23`):

> *"Những định chế này không nhất thiết đại diện cho lớp bảo hiểm thật. Anh phải luôn nhìn xuyên qua
> định chế. FSLIC khuyến khích người ta tin vào sự an toàn của hệ thống ngân hàng, nhưng nó không
> phải lớp bảo đảm sau cùng."*
>
> *"**Lớp bảo đảm sau cùng thậm chí không được viết ra.** Nó là việc chính phủ Mỹ nhận ra rằng nếu
> để FSLIC đổ, và để toàn bộ người gửi tiền ở các S&L mất tiền, thì nó sẽ phá huỷ chính niềm tin đã
> giữ chúng ta khỏi bank run."* (`13 37:04`)

Rồi câu tổng quát (`13 37:28`): *"cái luôn xảy ra là chính phủ đứng sau những lời hứa này, kể cả khi
chúng chưa từng được nói ra rõ ràng."*

📚 Ghi nhớ câu này. §10 sẽ cho thấy nó dự báo chính xác chuyện xảy ra ở Mỹ **12 năm sau**, và §11 cho
thấy Việt Nam đã xử lý nó theo một cách khác.

### Lần 3: Northern Rock, Anh 2007 — có bảo hiểm mà vẫn bị rút

Tin đồn lan ra rằng Northern Rock ôm nhiều chứng khoán dưới chuẩn và sắp phá sản. Người ta đổ tới,
**xếp hàng dài ngoài cửa**. Phóng viên chụp ảnh đám đông, và người xem nghĩ *"y hệt 1933"*
(`13 37:58`–`13 38:25`).

Shiller đặt đúng câu hỏi (`13 39:07`): **Anh có bảo hiểm tiền gửi rồi, sao vẫn bị rút?**

Câu trả lời của ông đúng về cơ chế: **vì có những người gửi nhiều hơn mức được bảo hiểm toàn phần.**

⚠️ Nhưng hai con số ông đọc đều sai — xem [§9](#9--bốn-chỗ-video-nói-sai). Chế độ Anh trước
01/10/2007 thực tế là: **100% của 2.000 bảng đầu, rồi 90% của 33.000 bảng tiếp theo**, trần 35.000
bảng, chi trả tối đa **31.700 bảng**.

Áp công thức đúng thì cơ chế Shiller mô tả hiện ra rõ hơn cả cách ông kể:

|       Số dư |    Được trả | Mất trắng |     % mất | Có lý do xếp hàng? |
| ----------: | ----------: | --------: | --------: | ------------------ |
|     1.000 £ |     1.000 £ |       0 £ |     0,0 % | không              |
| **2.000 £** | **2.000 £** |   **0 £** | **0,0 %** | **không**          |
|     5.000 £ |     4.700 £ |     300 £ |     6,0 % | **CÓ**             |
|    35.000 £ |    31.700 £ |   3.300 £ |     9,4 % | **CÓ**             |
|   100.000 £ |    31.700 £ |  68.300 £ |    68,3 % | **CÓ**             |

Ngưỡng khởi phát là **2.000 bảng** — thấp đến mức gần như mọi người gửi tiền thật đều nằm trên nó.
Bảo hiểm **một phần** không dập được bank run; nó chỉ **dời điểm khởi phát lên cao hơn một chút**.

Kết cục: chính phủ Anh **bảo lãnh toàn bộ**, bỏ qua chính chế độ bảo hiểm của mình, và cuộc tháo chạy
dừng lại (`13 39:23`–`13 39:37`). ⚠️ Shiller gán việc này cho **Mervyn King**; người quyết định thật
là **Alistair Darling** — xem [§9](#9--bốn-chỗ-video-nói-sai).

Rồi Anh sửa luật, và sửa theo đúng hướng bài học chỉ ra — **bỏ hẳn đồng bảo hiểm**:

| Thời điểm        |     Trần | Đồng bảo hiểm        |
| ---------------- | -------: | -------------------- |
| trước 01/10/2007 | 35.000 £ | 90 % sau 2.000 £ đầu |
| từ 01/10/2007    | 35.000 £ | **100 %**            |
| từ 10/2008       | 50.000 £ | 100 %                |
| từ 12/2010       | 85.000 £ | 100 %                |

Shiller lưu ý thêm (`13 39:47`): Anh **chưa từng có ngân hàng đổ vì bank run kể từ 1866**, và
*"không thực sự nhờ chế độ bảo hiểm tiền gửi nào cả"* — mà nhờ **Bank of England** và những gì nó
làm để giữ niềm tin.

### Lần 4: IKB, Đức 2007 — cứu trước cả khi bị rút

Ngân hàng Đức **IKB Deutsche Industriebank** đầu tư nhiều vào chứng khoán dưới chuẩn và bắt đầu có
dấu hiệu lo ngại. Chính phủ Đức **không thèm đợi bank run xảy ra** — họ cứu luôn, tốn **1,5 tỷ euro**
(`13 40:09`–`13 40:47`).

Shiller kết (`13 40:58`): *"các chính phủ biết họ muốn duy trì niềm tin, nên họ làm. Họ làm điều phải
làm."*

📚 Bốn ca này xếp thành một thang, và thang ấy chỉ đi một chiều:

```
   FSLIC 1980s      quy bao hiem tu pha san  -> chinh phu tra 150 ty do
   Northern Rock    che do bao hiem khong du -> chinh phu bao lanh toan bo
   IKB 2007         chua kip co run          -> chinh phu cuu truoc
```

Mỗi lần, cái được viết ra đều không đủ, và cái không được viết ra mới là thứ thực sự đỡ.

---

## 6. Basel — tài sản có rủi ro và yêu cầu vốn

Shiller mở phần này bằng một nguyên lý áp cho **mọi** loại bảo hiểm (`13 41:06`–`13 41:59`):

> *"Nếu anh bảo hiểm cho ngân hàng thì anh phải quản lý họ, vì có vấn đề rủi ro đạo đức."*

Và ông chỉ ra rằng ngân hàng làm được **đúng cái trò trường đua** ở §4 (`13 41:27`): vay tiền rồi
chọn một canh bạc thật rủi ro — chỉ khác là không ra trường đua thật. *"Và nếu thua, tất cả rơi xuống
đầu công ty bảo hiểm tiền gửi."*

Câu tổng quát (`13 41:46`): **"Đây là bài học nền tảng của bảo hiểm: hễ anh bảo hiểm cho thứ gì, anh
phải quản lý cái thứ được bảo hiểm. Vì một khi anh nhấc rủi ro khỏi vai họ, anh tạo ra rủi ro đạo
đức cho họ."**

### Ba lần Basel

Uỷ ban Basel đóng ở **Basel, Thuỵ Sĩ**, và Shiller nhấn một điểm dễ bỏ qua (`13 42:49`): nó **không
có thẩm quyền pháp lý nào**. *"Tất cả những gì nó làm được là khuyến nghị."*

|               |                 Năm | Bối cảnh                               | Kết cục                                                                   |
| ------------- | ------------------: | -------------------------------------- | ------------------------------------------------------------------------- |
| **Basel I**   | sau khủng hoảng S&L | thống nhất quy định giữa các nước      | được áp dụng rộng rãi                                                     |
| **Basel II**  |                2004 | hệ thống phức tạp lên — phái sinh, SPV | ⚠️ *"ngay sau Basel II ta có khủng hoảng tài chính thế giới"* (`13 44:08`) |
| **Basel III** |                2010 | G-20 họp ở Seoul ủng hộ                | Shiller nói sẽ áp dụng đủ **tới 2019**                                    |

Lý do phải thống nhất quốc tế (`13 42:51`): nếu một nước siết quá chặt, *"nó sẽ đẩy hoạt động ra khỏi
nước đó sang nước khác."*

Shiller nói thẳng về Basel II (`13 44:17`): *"họ đã làm sai điều gì đó. Họ không thực sự sửa được hệ
thống."*

Và ông thừa nhận giáo trình lỗi thời ngay lúc đang giảng (`13 45:43`): sách Fabozzi bản quyền 2010
có Basel I và II nhưng **không có Basel III**, vì Basel III ra cuối 2010, không kịp vào sách.

### Tài sản có rủi ro

Ý tưởng cốt lõi (`13 46:21`): mọi hiệp ước Basel *"đều nói về chuyện ngân hàng phải có đủ tiền. Đủ
tiền cho những rủi ro họ nhận."*

Nhưng không phải mọi tài sản đều rủi ro như nhau. Basel I đặt **bốn trọng số**, và Shiller nhấn rằng
phần này *"về cơ bản giống nhau"* qua cả Basel I, II và III (`13 48:47`):

|  Trọng số | Tài sản                                                 | Lý lẽ khi đó                               |
| --------: | ------------------------------------------------------- | ------------------------------------------ |
|   **0 %** | trái phiếu chính phủ OECD, gồm trái phiếu chính phủ Mỹ  | *"không có rủi ro"*                        |
|  **20 %** | trái phiếu địa phương, **và Fannie Mae / Freddie Mac**  | khá an toàn                                |
|  **50 %** | vay mua nhà                                             | *"có thể có khủng hoảng bất động sản lớn"* |
| **100 %** | mọi thứ còn lại, **đáng chú ý là cho vay doanh nghiệp** | —                                          |

⚠️ Shiller giải thích sai chữ viết tắt OECD ở `13 48:40` — xem [§9](#9--bốn-chỗ-video-nói-sai).

Ông không giấu vấn đề của dòng 20% (`13 50:00`–`13 50:59`). Fannie và Freddie được xếp 20% *"vì
người ta nghĩ mấy ông này thực sự an toàn, và dù sao chính phủ Mỹ cũng đỡ lưng."* Rồi ông nói thêm
cái ai cũng biết mà không ai viết ra: *"Mặc dù chính phủ Mỹ nói là sẽ không đỡ lưng. Nhưng ta đều
biết họ sẽ đỡ — và thực tế họ đã đỡ khi hai công ty này sụp."*

Đúng cái "lớp bảo đảm không được viết ra" ở §5, lần này áp cho tổ chức chứ không phải người gửi tiền.

Nhưng trước khủng hoảng, Fannie và Freddie **ngày càng đầu tư vào vay dưới chuẩn** và phát hành
chứng khoán thế chấp dưới chuẩn *"thực sự rất rủi ro và cuối cùng thì tiêu tùng"* (`13 50:27`).
Shiller kết luận thẳng (`13 50:48`): *"Basel I không biết điều đó, mà Basel II và Basel III cũng thế,
họ vẫn chỉ cho trọng số 20%. Đó là một sai lầm lớn, và một phần khủng hoảng ngân hàng đến từ chỗ
đó."*

### Ví dụ trên bảng

Shiller dựng một ngân hàng có **400 triệu đô tài sản** (`13 51:34`):

```
   Khoan muc                    Gia tri   Trong so   Tinh vao RWA
   Trai phieu chinh phu My      100 tr        0 %           0 tr
   Trai phieu Fannie Mae        100 tr       20 %          20 tr
   Vay mua nha tu nam giu       100 tr       50 %          50 tr
   Cho vay doanh nghiep         100 tr      100 %         100 tr
   TONG                         400 tr                    170 tr
```

Tài sản sổ sách 400 triệu, **tài sản có rủi ro chỉ 170 triệu**.

### Yêu cầu vốn của Basel III

Shiller chỉ trình bày phần **vốn chủ sở hữu phổ thông** (`13 53:18`), và gọi cấu trúc này là *"một
kiến trúc thú vị và sáng tạo"*:

| Thành phần             |            Mức | Tính chất                                        |
| ---------------------- | -------------: | ------------------------------------------------ |
| Vốn phổ thông bắt buộc | **4,50 %** RWA | bắt buộc **mọi lúc**                             |
| Đệm bảo toàn vốn       |    **+2,50 %** | thiếu thì **không được chia cổ tức**             |
| **Mức thực tế**        |     **7,00 %** |                                                  |
| Đệm nghịch chu kỳ      |        +2,50 % | chỉ khi cơ quan quản lý trong nước quyết định áp |
| **Trần**               |     **9,50 %** |                                                  |

Chỗ tinh tế nằm ở đệm 2,5% (`13 54:29`): *"Anh nhất định phải có 4,5% là vốn phổ thông, nhưng nếu
anh không có thêm 2,5% nữa, anh không được trả cổ tức. Cái đó thì chẳng hay ho gì. Nên trên thực tế,
anh nên giữ 7%."*

📚 Đây là một thiết kế đáng học: quy định **không cấm**, nó chỉ làm cho việc vi phạm trở nên đắt đỏ
theo cách hội đồng quản trị quan tâm. Cổ đông đòi cổ tức, nên ban điều hành tự giữ đủ 7%. Cưỡng chế
bằng động cơ thay vì bằng lệnh cấm.

Đệm nghịch chu kỳ thì có logic riêng (`13 55:30`): *"Ta phải chặn bong bóng **trước khi** nó vỡ."*
Nếu đợi tới lúc khủng hoảng mới siết thì *"ngân hàng sẽ ngừng cho vay, và cái đó sẽ làm sập cả nền
kinh tế. Anh phải siết khi thời thế đang tốt."*

Áp vào ngân hàng ở trên: **170 triệu × 7% = 11,90 triệu đô** vốn phổ thông phải giữ (`13 56:33`).

Một sinh viên ngắt lời để hỏi cho rõ đó là 4,5% hay 7% (`13 56:59`), và Shiller xác nhận: **7% của
170 triệu**.

---

## 7. Chỗ Basel đẩy sai hướng — 71 triệu so với 14 triệu

Đây là đoạn hay nhất của buổi giảng, và Shiller dựng nó như một cảnh họp hội đồng quản trị.

Giả sử ngân hàng nhìn vào bảng cân đối và thấy mình có **12,9 triệu** vốn phổ thông, trong khi chỉ
cần 11,9 triệu. **Thừa 1 triệu** (`13 57:26`).

Ai đó trong hội đồng lên tiếng (`13 58:15`): *"khoan đã, thế nghĩa là ta có thừa 1 triệu đô. Nó nằm
đó không, ta còn chẳng dùng tới. Đem dùng đi."*

Dùng thế nào? **Vay thêm rồi mua thêm tài sản** — tăng cả tài sản lẫn nợ. Câu hỏi là: đi được bao xa
trước khi chạm trần vốn?

Và câu trả lời phụ thuộc **hoàn toàn** vào việc mua thứ gì:

| Loại tài sản              | Trọng số |      Mua thêm được | Bội số vốn |
| ------------------------- | -------: | -----------------: | ---------: |
| Trái phiếu chính phủ Mỹ   |      0 % | **không giới hạn** |     vô hạn |
| **Trái phiếu Fannie Mae** |     20 % |    **71,43 triệu** |    **71×** |
| Vay mua nhà tự nắm giữ    |     50 % |        28,57 triệu |        28× |
| **Cho vay doanh nghiệp**  |    100 % |    **14,29 triệu** |    **14×** |

Shiller đọc tròn là *"khoảng 70 triệu"* (`13 59:53`) và *"khoảng 14 triệu"* (`13 60:31`). Tỷ lệ đúng
**5 lần**.

Rồi ông diễn tiếp cảnh họp (`13 60:50`): *"nhưng ở cuộc họp hội đồng, ai đó có thể nói: này, 70 triệu
nghe sướng hơn 14 triệu đấy, tôi nghĩ ta nên mua trái phiếu Fannie, còn mấy ông chủ doanh nghiệp nhỏ
đến gõ cửa thì bảo họ là **thôi xui rồi, chúng tôi không có tiền cho các ông**."*

Shiller gọi tên vấn đề (`13 61:06`): quy định Basel *"đang đẩy ngân hàng về phía đầu tư vào các khoản
vay dưới chuẩn do Fannie Mae phát hành, thay vì cho doanh nghiệp vay."*

Rồi ông đặt câu hỏi mà cả đoạn hướng tới (`13 61:26`): *"nhưng anh phải hỏi, chẳng phải sự thịnh
vượng của một quốc gia là do doanh nghiệp quyết định sao?"*

Và định nghĩa lại vay dưới chuẩn cho rõ (`13 61:34`): *"vay dưới chuẩn là gì? Là khoản vay cho người
có tín dụng xấu, lịch sử việc làm xấu, để mua nhà. Vậy là ta đã tạo ra động cơ để ngân hàng cho những
người đó vay thay vì cho doanh nghiệp vay."*

📌 **Điểm quan trọng nhất của cả bài học nằm ở đây:** hội đồng quản trị chọn Fannie **không phải vì
tham lam**. Họ chọn vì **quy định nói Fannie an toàn gấp năm lần cho vay doanh nghiệp**. Đó là quyết
định lý trí dưới bộ luật đang có hiệu lực. Quy định không thất bại vì bị lách — nó thất bại vì được
**tuân thủ**.

Shiller đưa cả lời tự bào chữa của phía Basel (`13 62:08`): *"chúng tôi không thể làm đúng hoàn toàn.
Chúng tôi nghĩ Fannie và Freddie — và chúng tôi đúng, chúng đâu có sụp. Việc của Basel là ngăn bank
run, nên chúng tôi muốn ngân hàng vững. Có thể anh đúng, có thể nên khuyến khích doanh nghiệp, nhưng
**đó không phải phần việc của chúng tôi**."*

📚 Câu cuối là chỗ đáng suy nghĩ nhất. Cơ quan quản lý ngân hàng tối ưu **đúng mục tiêu được giao** —
ngân hàng không sụp. Nhưng mục tiêu ấy không bao gồm *"vốn có chảy vào nơi tạo ra năng suất không"*.
Không ai làm sai việc của mình, và kết quả tổng vẫn tệ. Cùng cấu trúc với §3: **thất bại hệ thống
không cần ai hành xử sai.**

---

## 8. Ba cuộc khủng hoảng và một mẫu hình

Shiller lướt nhanh ba ca (`13 62:46`–`13 68:58`), nói thẳng là hết giờ. Nhưng ba ca ấy có chung một
xương sống.

### Mexico 1994–1995

Dưới thời Tổng thống **Salinas** — Shiller ghi rõ là *"nhà kinh tế học được đào tạo ở Harvard, muốn
hiện đại hoá kinh tế Mexico"* — chính phủ **tư nhân hoá ngân hàng**, giao cho thị trường tự do, *"và
họ quên mất việc quản lý nó"* (`13 63:56`–`13 64:20`).

Hệ quả bằng số (`13 64:26`–`13 64:42`):

|      | Dư nợ cho vay / GDP |
| ---- | ------------------: |
| 1988 |            **10 %** |
| 1994 |            **40 %** |

Gấp bốn lần trong sáu năm. Salinas không chặn. Bùng nổ, rồi bong bóng. Shiller: *"lẽ ra phải có một
cơ quan quản lý nói: dừng lại"* (`13 64:58`).

Không khí hình thành ở Mexico (`13 65:14`): *"tôi không lo về khủng hoảng, vì chính phủ Mexico sẽ cứu
hết."* **Hoá ra họ không cứu nổi tất cả.** Hệ thống ngân hàng Mexico bị phá huỷ; phần lớn ngân hàng
Mexico rơi vào tay ngân hàng nước ngoài.

### Châu Á 1997

Ngân hàng quốc tế đã cho các nước châu Á vay rất nhiều. Rồi các khoản vay ấy **bị rút về** khi *"một
dạng bank run xảy ra"* (`13 67:12`) — nhà đầu tư quốc tế đồng loạt muốn rút tiền khỏi châu Á.

Bắt đầu ở **Thái Lan, Hàn Quốc, Indonesia**, rồi lan ra toàn thế giới: tới **Nga** thành Khủng hoảng
Nợ Nga, rồi xuống tận **Brazil** (`13 67:28`–`13 67:57`).

Shiller đặt câu hỏi tu từ (`13 67:57`): *"bạn thắc mắc, vì sao Brazil lại bị ảnh hưởng bởi một cuộc
khủng hoảng châu Á? Thì đấy, thế giới đã và đang liên kết với nhau."*

📚 Đây là **bank run ở cấp quốc gia**. Không ai xếp hàng ngoài cửa chi nhánh, nhưng cấu trúc giống
hệt §3: chủ nợ ngắn hạn đồng loạt đòi tiền từ những con nợ đã đem tiền đầu tư dài hạn. Diamond–Dybvig
không nói gì về biên giới, nên nó áp được cả ở đây.

### Argentina 2002

Ca này Shiller nói ngắn nhất, chỉ kịp nêu bản chất (`13 68:32`): chính phủ Argentina **đóng cửa hệ
thống ngân hàng**.

### Mẫu hình chung

Shiller tự rút ở Mexico (`13 66:21`), và nó áp cho cả ba: **"lại là một thất bại về quản lý."**

Chi tiết hơn (`13 66:24`): *"nếu anh để rủi ro đạo đức phát triển, nếu anh để người ta nghĩ rằng —
này, cứ cho vay hết đi, chắc ổn thôi, mà không ổn thì mình có bạn bè trên Mexico City, đâu vào đấy
cả."*

Và ông kết phần cuối bằng lời bênh vực nghề quản lý (`13 69:50`–`13 70:34`): *"có một thái độ ở nhiều
người là họ không thích cơ quan quản lý, hoặc không trân trọng họ. Nhưng thực ra người làm quản lý là
những người đang vận hành một hệ thống rất phức tạp, thứ thực sự quan trọng với sự thịnh vượng của
chúng ta."*

Rồi một quan sát thực nghiệm đáng nhớ (`13 70:09`): nếu nhìn vào nguyên nhân của các cú đứt gãy kinh
tế, **thất bại của hệ thống ngân hàng thường là thủ phạm**. Ghép nó với khủng hoảng dầu — *"hai thứ
đó cộng lại giải thích phần lớn các cuộc khủng hoảng kinh tế."*

### Điều Shiller nói ông chưa kịp nói

Cuối buổi ông nêu **ngân hàng ngầm** như lời hẹn (`13 70:34`–`13 71:24`): những công ty *"không chính
thức là ngân hàng, nhưng làm việc giống ngân hàng và không bị quản lý."*

Ví dụ ông đưa rất sắc: **Lehman Brothers** và **Bear Stearns** — hai vụ đổ lớn dẫn tới khủng hoảng —
*"không phải ngân hàng. Không phải ngân hàng thương mại. Chúng không nằm dưới Basel III. Chúng là
ngân hàng đầu tư, một con vật khác, và Basel III không quản chúng."*

Đây chính là chỗ rào chắn ở `13 02:52` trả về kết quả: hai định chế lớn nhất sụp trong khủng hoảng
2008 **nằm ngoài toàn bộ bộ máy** mà buổi giảng này vừa mô tả.

---

## 9. ⚠️ Bốn chỗ video nói sai

Bốn chỗ dưới đây đều đã đối chiếu với nguồn độc lập, liệt kê ở [Nguồn](#nguồn).

### 9.1 Diamond–Dybvig là 1983, không phải 1988

Shiller (`13 24:32`–`13 24:41`): *"the Diamond-Dybvig model in the Journal of Political Economy,
**1988**"*.

**Thật:** Diamond, D.W. & Dybvig, P.H. (**1983**), "Bank Runs, Deposit Insurance, and Liquidity",
*Journal of Political Economy* **91(3)**, 401–419.

Lệch 5 năm này không phải vặt. Bài báo ra **1983**, tức **ngay sau** làn sóng đổ vỡ ngân hàng đầu
thập niên 1980 và **trước** khủng hoảng S&L mà Shiller kể ở §5. Đặt đúng năm thì thấy lý thuyết ra
đời **trước** sự kiện nó giải thích, chứ không phải sau.

### 9.2 Hạn mức bảo hiểm tiền gửi Anh: 2.000 và 35.000, không phải 3.000 và 75.000

Shiller (`13 38:40`–`13 38:53`): *"insure fully all deposits up to GBP **3,000**. And then, it gave
90% insurance up to GBP **75,000**."*

**Thật:** chế độ Anh trước 01/10/2007 bảo hiểm **100% của 2.000 bảng đầu**, rồi **90% của 33.000
bảng tiếp theo** — trần **35.000 bảng**, chi trả tối đa **31.700 bảng**.

Con số 75.000 lệch hơn gấp đôi, và nó làm **yếu** đi chính lập luận của Shiller: ngưỡng khởi phát
thật là **2.000 bảng**, thấp hơn nhiều so với con số ông đọc, nên số người có lý do xếp hàng còn
đông hơn ông nói.

### 9.3 Người bảo lãnh Northern Rock là Alistair Darling, không phải Mervyn King

Shiller (`13 39:23`): *"So **Mervyn King**, who's head of the Bank of England, just decided, you
know what, we'll bail everybody out."*

**Thật:** người tuyên bố bảo lãnh toàn bộ tiền gửi của Northern Rock ngày **17/9/2007** là **Alistair
Darling**, Bộ trưởng Tài chính, thay mặt **Bộ Tài chính Anh** — không phải Thống đốc Ngân hàng Trung
ương.

Đây không phải bắt bẻ. Sự phân biệt **ngân hàng trung ương** và **bộ tài chính** chính là điều
Shiller tự rào ở `13 03:21`. Ngân hàng trung ương cho vay để cứu thanh khoản; chỉ **kho bạc** mới
cam kết được tiền thuế. Northern Rock cần đúng loại thứ hai, và đó là lý do phải là Darling.

### 9.4 OECD là "Economic", không phải "European"

Shiller (`13 48:40`): *"The OECD is the organization for **European** Cooperation and Development."*

**Thật:** **Organisation for Economic Co-operation and Development** — Tổ chức Hợp tác và Phát triển
**Kinh tế**. Ông có lẽ nhớ nhầm sang tổ chức tiền thân, **OEEC** (Organisation for European Economic
Co-operation), giải thể năm 1961.

Ngay sau đó ông tự mô tả OECD là *"các nước châu Âu tiên tiến, ổn định"* rồi phải nói thêm *"và trái
phiếu chính phủ Mỹ cũng nằm trong nhóm đó"* (`13 48:51`) — chính chỗ vá víu ấy lộ ra nhầm lẫn. OECD
năm 2011 đã có Mỹ, Nhật, Hàn Quốc, Úc, Mexico, Chile.

---

## 10. ⚠️ Đối chiếu 2026

### 10.1 "Chưa có bank run lớn nào kể từ 1933" — đã hết đúng vào tháng 3/2023

Shiller nói FDIC *"tới hôm nay chưa bao giờ đổ"* và *"chúng ta chưa có bank run lớn nào kể từ 1933"*
(`13 34:34`, `13 34:42`).

Câu đó đúng trong **90 năm**, rồi hỏng trong **một ngày**.

Ngày **9/3/2023**, người gửi tiền cố rút **42 tỷ đô khỏi Silicon Valley Bank trong một ngày**, và
**100 tỷ nữa xếp hàng chờ rút hôm sau**. Cuối ngày, số dư tiền mặt của ngân hàng **âm 958 triệu đô**.
Hôm sau nó bị đóng cửa; tài sản cuối 2022 là **209 tỷ đô**. Hai ngày sau, **Signature Bank** (110 tỷ)
đóng cửa. Ngày **1/5/2023**, **First Republic** (213 tỷ) đóng cửa — ngân hàng này có **gần 70% tiền
gửi không được bảo hiểm**.

Điều Diamond–Dybvig ở §3 mô tả bằng 100 người xếp hàng, năm 2023 xảy ra **qua điện thoại**. Không ai
phải đến chi nhánh. Tốc độ tháo chạy không còn bị giới hạn bởi tốc độ đi bộ.

### 10.2 Và §5 dự báo đúng chính xác chuyện xảy ra tiếp theo

Nhớ câu ở `13 37:04`: *"lớp bảo đảm sau cùng thậm chí không được viết ra."*

Hạn mức FDIC là **250.000 đô**. Ngày **12/3/2023**, cơ quan quản lý Mỹ viện **ngoại lệ rủi ro hệ
thống** (12 U.S.C. §1823(c)(4)(G)) và **bảo vệ toàn bộ người gửi tiền, kể cả phần vượt hạn mức**.
FDIC ước tính đã gánh **16,7 tỷ đô** lỗ mà lẽ ra người gửi tiền không được bảo hiểm phải chịu.

Đúng khuôn mẫu FSLIC năm 1989, đúng khuôn mẫu Northern Rock năm 2007. Ba lần, ba nước, bốn thập
niên — và lần nào chính phủ cũng trả nhiều hơn mức đã hứa bằng văn bản.

Ngoại lệ này **không** cứu cổ đông và trái chủ không bảo đảm; hội đồng quản trị và phần lớn lãnh đạo
cấp cao bị bãi nhiệm. Nó được viện tổng cộng **sáu lần**: năm lần trong khủng hoảng 2008–2009 và một
lần năm 2023.

### 10.3 Basel III: Shiller nói "áp dụng đủ tới 2019". Năm 2026 vẫn chưa xong

Shiller nói Basel III *"sẽ không được áp dụng đầy đủ cho tới 2019"* (`13 44:55`), và giải thích lý do
giãn tiến độ: thế giới đang trong khủng hoảng, áp một lúc thì căng quá.

Mười lăm năm sau mốc ấy:

| Nơi        | Tình trạng tháng 9/2026                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mỹ**     | **chưa xong.** Bản đề xuất 2023 không đạt đồng thuận; cơ quan quản lý **đề xuất lại ngày 19/3/2026**, hạn góp ý 18/6/2026. Bản 2023 ước tính tăng ~19% vốn cho ngân hàng nhóm I–II; bản đề xuất lại **giảm vốn ròng**. |
| **Anh**    | quy định cuối cùng công bố **20/1/2026**, áp dụng từ **1/1/2027** — lùi một năm để chờ Mỹ                                                                                                                              |
| **EU**     | CRR3 hiệu lực **1/1/2025**; sàn đầu ra vào dần, đạt 72,5% **năm 2030**                                                                                                                                                 |
| **Canada** | **hoãn vô thời hạn** phần tăng sàn vốn                                                                                                                                                                                 |

Shiller nói ở `13 71:42`: *"sẽ có Basel IV."* Ông đúng về tinh thần và sai về nhịp độ — mười lăm năm
sau, thế giới còn chưa đi hết Basel III.

⚠️ Và có một điều Shiller **không** thể lường: hệ quả của việc chậm trễ không đều nhau. Ngân hàng
châu Âu có thể phải giữ vốn cao hơn ngân hàng Mỹ cho cùng một mức rủi ro — đúng cái *"đẩy hoạt động
sang nước khác"* mà ông nêu ở `13 42:51` là lý do phải có Basel ngay từ đầu.

### 10.4 Diamond và Dybvig đoạt Nobel năm 2022

Shiller giới thiệu họ là *"đồng nghiệp của chúng tôi ở Yale, giờ đã chuyển đi"* và *"tôi biết cả
hai"* (`13 24:44`). Năm **2022**, **Douglas Diamond** và **Philip Dybvig** nhận **Nobel Kinh tế**
cùng **Ben Bernanke**, chủ yếu nhờ chính bài báo 1983 ấy — trao đúng **một năm trước** khi SVB chứng
minh lại mô hình bằng thực tế.

Shiller thì đã nhận Nobel năm **2013**, hai năm sau buổi giảng này.

### 10.5 Ngân hàng cổ nhất thế giới suýt chết, rồi thành lớn thứ ba nước Ý

Shiller kể về **Banca Monte dei Paschi di Siena** (lập 1472) với giọng trìu mến ở §2 — tổ chức từ
thiện cho người nghèo vay, ngân hàng lớn thứ ba nước Ý năm 2011, có bảo tàng nhỏ ở sảnh.

Chuyện sau đó:

- **2015:** danh mục nợ xấu lớn nhất nước Ý — **34,8%** tổng dư nợ.
- **2016:** ngân hàng **duy nhất trượt** bài kiểm tra sức chịu đựng kịch bản bất lợi của EBA.
- **2017:** **tái cấp vốn phòng ngừa** được Uỷ ban châu Âu duyệt, tổng **8,1 tỷ euro**. Toàn bộ
  **4,3 tỷ euro** nợ thứ cấp chuyển thành cổ phần; Bộ Kinh tế và Tài chính Ý nắm **52,2%**.
- **2023–2024:** nhà nước Ý bán dần, còn khoảng **4,9%**.
- **2025:** MPS **thâu tóm Mediobanca** trong thương vụ **16 tỷ euro**, nắm 86,3% cổ phần, và trở lại
  thành **ngân hàng lớn thứ ba nước Ý**.

📚 Chi tiết đáng chú ý nhất của vụ 2017, xét theo bài học này: **cổ đông và trái chủ thứ cấp chịu 4,3
tỷ euro lỗ, còn người gửi tiền và chủ nợ ưu tiên không mất gì.** Đó là nguyên tắc §6 được thi hành —
ai hưởng lợi khi ngân hàng đánh bạc thì người ấy chịu lỗ. Nhưng nhà nước vẫn phải bỏ 3,9 tỷ euro,
tức lớp bảo đảm sau cùng ở `13 37:04` lại xuất hiện, lần này ở Ý.

Ngân hàng do các nhà hảo tâm lập ra năm 1472 để cho người nghèo vay, năm 2017 phải nhờ người đóng
thuế cứu. Năm trăm bốn mươi lăm năm không miễn nhiễm được gì.

---

## 11. 🇻🇳 Góc Việt Nam — hạn mức bảo hiểm tiền gửi

Việt Nam có bảo hiểm tiền gửi, và cách nó được thiết kế cho thấy người soạn đã học đúng bài học của
Northern Rock.

### Hạn mức

| Văn bản                       |            Hạn mức | Hiệu lực       |
| ----------------------------- | -----------------: | -------------- |
| Quyết định 21/2017/QĐ-TTg     |      75 triệu đồng | 5/8/2017       |
| **Quyết định 32/2021/QĐ-TTg** | **125 triệu đồng** | **12/12/2021** |

Đây là số tiền tối đa Bảo hiểm tiền gửi Việt Nam trả cho **tất cả** khoản tiền gửi được bảo hiểm — cả
gốc lẫn lãi — của **một người** tại **một tổ chức**.

### Chỗ Việt Nam làm đúng

**Không có đồng bảo hiểm.** Trả **100% tới hạn mức**. So với chế độ Anh 2007 ở §5:

> ⚙️ **Cách đọc cột cuối.** Không thể bê thẳng 2.000 £ / 35.000 £ sang tiền Việt được — hai hạn mức
> khác nhau về độ lớn. Nên cột này **quy đổi cấu trúc theo tỷ lệ**: ngưỡng trả đầy đủ của Anh bằng
> $2.000/35.000 = 5{,}71\,\%$ hạn mức, áp lên hạn mức 125 triệu thì ra **7,143 triệu đồng**; phần vượt
> ngưỡng đó được **90 %**, và tổng vẫn chặn ở hạn mức. Giữ nguyên **hình dạng** của chế độ Anh, chỉ đổi
> **thang**.

|         Số dư | Việt Nam trả | Mất trắng | Nếu áp cấu trúc Anh 2007 *(đã quy đổi thang)* |
| ------------: | -----------: | --------: | --------------------------------------------: |
|      50 triệu |        50 tr |         0 |                                      45,71 tr |
|     100 triệu |       100 tr |         0 |                                      90,71 tr |
| **125 triệu** |   **125 tr** |     **0** |                                 **113,21 tr** |
|     500 triệu |       125 tr |    375 tr |                                     113,21 tr |

Kiểm thử một dòng: với số dư 50 triệu, $7{,}143 + 0{,}9 \times (50 - 7{,}143) = 7{,}143 + 38{,}571 =
\mathbf{45{,}714}$ triệu.

Cột cuối là điều **không** xảy ra ở Việt Nam. Dưới cấu trúc đồng bảo hiểm, **ngay cả người gửi đúng
bằng hạn mức cũng mất tiền** — nên ai cũng có lý do xếp hàng. Bỏ đồng bảo hiểm là bỏ đúng cái ngòi nổ
mà Northern Rock đã chứng minh là có thật.

### Chỗ cần đọc kỹ con số

Theo Bảo hiểm tiền gửi Việt Nam, hạn mức 125 triệu bảo vệ **toàn bộ tiền gửi của trên 92% người gửi
tiền**, nằm trong khoảng 90–95% mà **IADI** khuyến nghị.

⚠️ Nhưng con số ấy nói về **số người**, không phải **số tiền**. Phần lớn tiền trong hệ thống nằm ở
nhóm dưới 8% còn lại, và nhóm đó **không được bảo hiểm hết**.

Đó chính xác là nhóm xếp hàng trước — đúng như bảng ở §5 cho thấy với Northern Rock, và đúng như
First Republic năm 2023 với gần 70% tiền gửi không được bảo hiểm. **Tỷ lệ phủ tính theo đầu người
không đo được rủi ro bank run; tỷ lệ phủ tính theo số tiền mới đo được.**

### Và Việt Nam đã viết "cái không được viết ra" vào văn bản

Câu quan trọng nhất của buổi giảng, ở `13 37:04`: *lớp bảo đảm sau cùng thậm chí không được viết ra.*

**Luật Các tổ chức tín dụng 2024** bổ sung: ngoài hạn mức 125 triệu, **Ngân hàng Nhà nước có thể
trình Thủ tướng quyết định chi trả toàn bộ cho người gửi tiền** trong từng trường hợp cụ thể.

📚 Đây là một lựa chọn thiết kế thú vị, và nó **cắt cả hai chiều**:

- **Được:** khi khủng hoảng đến, không cần ứng biến kiểu Darling năm 2007 hay ngoại lệ rủi ro hệ
  thống kiểu Mỹ năm 2023. Đường đi đã có sẵn, và người gửi tiền **biết** là có.
- **Mất:** một bảo lãnh ai cũng biết là bảo lãnh **thật**, và đó chính là **rủi ro đạo đức** mà
  Shiller nêu ở `13 41:46` — *"hễ anh bảo hiểm cho thứ gì, anh phải quản lý cái thứ được bảo hiểm."*
  Bảo lãnh càng rõ ràng thì gánh nặng đặt lên khâu giám sát càng nặng.

Câu hỏi để mở, và nó không có đáp án trong video: **giữa việc để lớp bảo đảm mơ hồ (Mỹ, Anh) và viết
nó thành luật (Việt Nam), cách nào tạo ít rủi ro đạo đức hơn?**

---

## 12. Chương trình

> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-03-ngan-hang.py`. Không cần cài
> gói, không đọc file ngoài, không gọi mạng. Kết quả **tất định**.

Chương trình: [`../thuc_hanh/bai-03-ngan-hang.py`](../thuc_hanh/bai-03-ngan-hang.py) — 7 mục, mọi
khoản tiền là **số nguyên** ở đơn vị nhỏ nhất, mọi con số Shiller đọc trên lớp đều có một `assert`
đứng sau.

Kết quả chạy thật:

```
BAI 3 — NGAN HANG: THANH KHOAN, BANK RUN, BASEL
Yale ECON 252 (2011) buoi 13 — Robert J. Shiller

==============================================================================
1. Thu nhap chenh lech va lech ky han — hai thu khac nhau
==============================================================================
  Tien gui nhan vao       1,000 tr do   lai 1.00 %/nam   ky han: RUT BAT CU LUC NAO
  Du tru giu lai            100 tr do   = 10 % tien gui
  Cho vay ra                900 tr do   lai 5.00 %/nam   ky han: 30 NAM

  Thu tu cho vay             45 tr do
  Tra cho nguoi gui          10 tr do
  Thu nhap chenh lech        35 tr do

  Hai chenh lech, khong phai mot:
    chenh lech LAI SUAT   4.00 diem phan tram   -> nguon thu, vo hai
    chenh lech KY HAN     0 ngay vs 30 nam   -> nguon thu, VA la cho gay

  Ngan hang hua hai dieu mau thuan cung luc:
    voi nguoi gui:  tien cua ban luon san sang
    voi nguoi vay:  tien cua ban khoa 30 nam
  Ca hai loi hua deu that — mien la dung ai den doi cung luc.

==============================================================================
2. Diamond-Dybvig: cung mot ngan hang, hai ket cuc
==============================================================================
  100 nguoi gui, moi nguoi 1 don vi. De toi ky 2 thi 1 don vi thanh 2.
  25 nguoi la 'gap' (buoc tieu o ky 1), 75 nguoi kien nhan.

  KHONG co ngan hang — nguoi gap phai thanh ly som:
    nguoi gap       nhan  1.000
    nguoi kien nhan nhan  2.000

  CO ngan hang — hop dong tra nguoi rut som r1 = 1.28:
    nguoi gap       nhan  1.280   +28 % so voi tu lo
    nguoi kien nhan nhan  1.813   -9.3 % so voi tu lo

  Khong ai bo them nguon luc nao vao. Thanh khoan hien ra tu hu khong —
  dung nhu da dang hoa danh muc, chi can sap xep cho dung.

  NHUNG hop dong do co can bang thu hai. Neu ca 100 nguoi cung den ky 1:

    tong von thanh ly duoc   100.00 don vi
    moi nguoi doi              1.28 don vi
    so nguoi duoc tra DU         78   (nguoi thu 1 den 78)
    nguoi thu 79 nhan           0.16 don vi
    so nguoi nhan SO KHONG       21

  Ngan hang nay KHONG he mat kha nang thanh toan. Tai san van du 100 don vi.
  No chi khong the bien 100 don vi ky-2 thanh 128 don vi ky-1.
  Dung y Shiller `13 25:52`: chi can nguoi ta doi ky vong la moi thu sup.
  Ai xep hang sau nguoi thu 79 thi trang tay — nen XEP HANG SOM LA HOP LY.
  Do moi la cho dang so: khong ai lam gi sai ca.

==============================================================================
3. Bao hiem cang hao phong, ngan hang cang de vo
==============================================================================
  r1 la muc ngan hang hua tra nguoi rut som. Tang r1 = bao hiem tot hon
  cho nguoi gap, nhung chiu duoc it nguoi rut hon khi hoang loan.

     r1    nguoi kien nhan nhan    chiu duoc bao nhieu nguoi rut
  --------------------------------------------------------------------
    1.00                2.000                        100  khong bao hiem gi — khong the co run
    1.10                1.933                         90
    1.20                1.867                         83
    1.28                1.813                         78  <- hop dong trong muc 2
    1.40                1.733                         71
    1.50                1.667                         66

  Khong co muc r1 nao vua bao hiem tot vua mien nhiem bank run.
  Do la ly do phai co nguoi thu ba dung ra bao lanh — bao hiem tien gui.

==============================================================================
4. Tai san co rui ro — vi du Shiller viet tren bang
==============================================================================
  Mot ngan hang co 400 trieu do tai san. Trong so rui ro theo Basel:

     Khoan muc                    Gia tri   Trong so   Tinh vao RWA
  --------------------------------------------------------------------
     Trai phieu chinh phu My      100 tr        0 %           0 tr
     Trai phieu Fannie Mae        100 tr       20 %          20 tr
     Vay mua nha tu nam giu       100 tr       50 %          50 tr
     Cho vay doanh nghiep         100 tr      100 %         100 tr
  --------------------------------------------------------------------
     TONG                         400 tr                    170 tr

  Tai san so sach 400 trieu, nhung tai san co rui ro chi 170 trieu.
  Von phai giu = mot ty le cua RWA, khong phai cua tong tai san:

    4,50 %  von pho thong bat buoc           7.65 tr do
    +2,50 % dem bao toan von  -> 7,00 %     11.90 tr do  <- muc thuc te
    +2,50 % dem nghich chu ky -> 9,50 %     16.15 tr do  (khi co bong bong)

  11,90 trieu — dung con so Shiller doc o `13 56:33`.

  Dem 2,50 % khong bat buoc theo nghia den: thieu no thi ngan hang van
  hoat dong, chi la KHONG DUOC CHIA CO TUC. Nen thuc te ai cung giu du 7 %.

==============================================================================
5. Mot trieu do von thua mua duoc bao nhieu tai san
==============================================================================
  Ngan hang o muc 4 can 11.90 trieu von,
  nhung tren bang can doi dang co 12,90 trieu — thua 1 trieu.

  Vay them roi mua them tai san, duoc bao nhieu truoc khi cham tran?

     Loai tai san                Trong so    Mua them duoc    Boi so von
  --------------------------------------------------------------------
     Trai phieu chinh phu My           0 %   khong gioi han      vo han
     Trai phieu Fannie Mae            20 %         71.43 tr         71x
     Vay mua nha tu nam giu           50 %         28.57 tr         28x
     Cho vay doanh nghiep            100 %         14.29 tr         14x

  Shiller doc tron la 'khoang 70 trieu' (`13 59:53`) va 'khoang 14 trieu'
  (`13 60:31`). So dung: 71.43 trieu va 14.29 trieu — ty le dung 5 lan.

  Day la toan bo van de, goi trong mot dong:

     cung 1 trieu do von
       -> mua Fannie Mae:         71.43 trieu
       -> cho doanh nghiep vay:   14.29 trieu

  Mot hoi dong quan tri LY TRI se chon Fannie. Khong phai vi tham, ma vi
  quy dinh noi Fannie an toan gap 5 lan cho vay doanh nghiep.
  Fannie va Freddie sau do om day vay duoi chuan roi sup nam 2008.
  Trong so van la 20 %.

==============================================================================
6. Vi sao Northern Rock bi rut tien du DA CO bao hiem tien gui
==============================================================================
  Che do Anh truoc 01/10/2007: 100 % cua 2 000 bang dau,
  roi 90 % cua 33 000 bang tiep theo. Tren 35 000 bang thi khong duoc gi.

      So du      Duoc tra    Mat trang    % mat   Co ly do xep hang?
  --------------------------------------------------------------------
      1,000 £     1,000 £          0 £     0.0 %   khong
      2,000 £     2,000 £          0 £     0.0 %   khong
      5,000 £     4,700 £        300 £     6.0 %   CO
     10,000 £     9,200 £        800 £     8.0 %   CO
     35,000 £    31,700 £      3,300 £     9.4 %   CO
     50,000 £    31,700 £     18,300 £    36.6 %   CO
    100,000 £    31,700 £     68,300 £    68.3 %   CO

  Chi tra toi da 31 700 bang, cham tran ngay o 35 000 va khong tang nua.

  Shiller hoi dung cau (`13 39:07`): vi sao co bao hiem ma van bi rut tien?
  Bang tren cho thay nguong khoi phat la 2 000 bang. Tren muc ay, xep hang
  la hanh vi HOP LY, y het muc 2. Bao hiem MOT PHAN khong dap duoc run —
  no chi doi diem khoi phat len cao hon mot chut.

  Anh sua ngay sau do, va sua theo huong bo han dong bao hiem:

     truoc 01/10/2007   tran  35,000 £   dong bao hiem: 90 % sau 2 000 £ dau
     tu 01/10/2007      tran  35,000 £   dong bao hiem: 100 %
     tu 10/2008         tran  50,000 £   dong bao hiem: 100 %
     tu 12/2010         tran  85,000 £   dong bao hiem: 100 %

==============================================================================
7. GOC VIET NAM — han muc bao hiem tien gui
==============================================================================
  Quyet dinh 21/2017/QD-TTg     75 trieu dong
  Quyet dinh 32/2021/QD-TTg    125 trieu dong   (+66 %, hieu luc 12/12/2021)

  Viet Nam chon dung cau truc ma Anh phai tra gia moi hoc duoc:
  tra 100 % toi han muc, KHONG dong bao hiem.

       So du       Viet Nam tra   Mat trang   Neu ap cau truc Anh 2007
  --------------------------------------------------------------------
        50 trieu        50 tr          0 tr               45.71 tr
       100 trieu       100 tr          0 tr               90.71 tr
       125 trieu       125 tr          0 tr              113.21 tr
       200 trieu       125 tr         75 tr              113.21 tr
       500 trieu       125 tr        375 tr              113.21 tr
     1,000 trieu       125 tr        875 tr              113.21 tr

  Cot cuoi la dieu KHONG xay ra o Viet Nam. Duoi cau truc dong bao hiem,
  ngay ca nguoi gui DUNG BANG han muc cung mat tien — nen ai cung co ly do
  xep hang. Bo dong bao hiem la bo dung cai ngoi no do.

  Theo Bao hiem tien gui Viet Nam, han muc 125 trieu bao ve TOAN BO tien gui
  cua tren 92 % nguoi gui tien — trong khoang 90-95 % ma IADI khuyen nghi.

  Nhung doc ky thi con so do noi ve SO NGUOI, khong phai SO TIEN.
  Phan lon tien trong he thong nam o nhom duoi 8 % con lai, va nhom do
  khong duoc bao hiem het. Do chinh la nhom xep hang truoc.

  Luat Cac to chuc tin dung 2024 bo sung mot dieu dang chu y: ngoai han muc
  125 trieu, Ngan hang Nha nuoc co the trinh Thu tuong quyet dinh chi tra
  TOAN BO cho nguoi gui tien trong tung truong hop cu the.

  Do dung la dieu Shiller noi o `13 37:04`: bao dam that su nam ngoai van ban.
  Khac biet la Viet Nam da viet chinh cai 'ngoai van ban' ay vao van ban.

==============================================================================
Het. Moi assert da qua.
```

### 💡 Tự thử

1. **Đổi `TY_LE_GAP_PCT` từ 25 lên 40** ở mục 2. Người kiên nhẫn còn nhận bao nhiêu? Ở mức nào thì
   hợp đồng ngân hàng trở nên **tệ hơn** tự lo cho cả hai nhóm?
2. **Ở mục 3, tìm mức `r1` lớn nhất mà ngân hàng vẫn chịu được 85 người rút.** So với `r1 = 1,28`,
   người kiên nhẫn mất bao nhiêu để mua thêm 7 người đệm đó?
3. **Đổi trọng số Fannie Mae ở `TRONG_SO` từ 20% lên 50%** — bằng vay mua nhà. Mục 5 còn chênh lệch
   không? Nếu Basel I đã làm thế từ đầu, phần nào của §7 sẽ biến mất?
4. **Viết thêm hàm `chi_tra_my()` cho hạn mức FDIC 250.000 đô**, rồi áp cho một ngân hàng có 70% tiền
   gửi không được bảo hiểm như First Republic. Bao nhiêu phần trăm **số tiền** được phủ, so với bao
   nhiêu phần trăm **số người**?

---

## 13. Từ điển thuật ngữ

| Tiếng Việt               | Tiếng Anh                     | Nghĩa trong bài                                                 |
| ------------------------ | ----------------------------- | --------------------------------------------------------------- |
| Thu nhập chênh lệch      | *spread income*               | chênh giữa lãi cho vay và lãi tiền gửi                          |
| Lệch kỳ hạn              | *maturity mismatch*           | vay ngắn cho vay dài — nguồn thanh khoản và nguồn sụp đổ        |
| Dự trữ một phần          | *fractional reserve*          | chỉ giữ lại một phần tiền gửi dưới dạng tiền mặt                |
| Rút tiền hàng loạt       | *bank run*                    | người gửi đồng loạt đòi rút, kể cả khi ngân hàng vẫn đủ tài sản |
| Đa cân bằng              | *multiple equilibria*         | cùng một hệ thống, hai kết cục, quyết định bởi kỳ vọng          |
| Lựa chọn ngược           | *adverse selection*           | người không biết thông tin luôn nhận phần hàng tệ nhất          |
| Rủi ro đạo đức           | *moral hazard*                | được che rủi ro nên hành xử liều hơn                            |
| Trách nhiệm hữu hạn      | *limited liability*           | lỗ tối đa bằng phần vốn góp — nền của trò trường đua ở §4       |
| Bảo hiểm tiền gửi        | *deposit insurance*           | bên thứ ba bảo lãnh tiền gửi để chặn cân bằng xấu               |
| Đồng bảo hiểm            | *co-insurance*                | chỉ trả một phần trăm nhất định — chỗ Anh sai năm 2007          |
| Tài sản có rủi ro        | *risk-weighted assets (RWA)*  | tổng tài sản nhân trọng số rủi ro từng loại                     |
| Đệm bảo toàn vốn         | *capital conservation buffer* | 2,5% thêm; thiếu thì không được chia cổ tức                     |
| Đệm nghịch chu kỳ        | *countercyclical buffer*      | 2,5% thêm, áp khi có dấu hiệu bong bóng                         |
| Ngân hàng ngầm           | *shadow banking*              | làm việc như ngân hàng nhưng không chịu quản lý ngân hàng       |
| Ngoại lệ rủi ro hệ thống | *systemic risk exception*     | điều khoản Mỹ dùng năm 2023 để bảo vệ cả tiền gửi vượt hạn mức  |

---

## 14. Câu hỏi tự kiểm tra

1. Ngân hàng ở §3 có đủ tài sản trả hết mọi người gửi tiền. Vậy vì sao nó vẫn sập? Trả lời **không
   dùng** chữ "hoảng loạn".
2. Vì sao `r1 = 1,00` là mức duy nhất miễn nhiễm bank run, và vì sao không ai chọn nó?
3. Shiller nói cán bộ tín dụng *"bảo lãnh cho nhân cách của người ta"*. Loại thông tin nào ở đây
   không viết được vào hợp đồng? Điều gì xảy ra khi ta thay họ bằng mô hình chấm điểm rồi bán khoản
   vay đi?
4. Một ngân hàng có 200 triệu trái phiếu chính phủ Mỹ và 200 triệu cho vay doanh nghiệp. RWA bằng
   bao nhiêu? Vốn phổ thông phải giữ theo mức 7% là bao nhiêu? So với ngân hàng ở §6 — cùng tổng tài
   sản, vì sao khác?
5. Hội đồng quản trị ở §7 chọn Fannie Mae thay vì cho doanh nghiệp vay. Chỉ ra chỗ trong chuỗi lập
   luận của họ **sai** — nếu có.
6. Vì sao việc phân biệt Alistair Darling với Mervyn King (§9.3) không phải chuyện bắt bẻ chữ nghĩa?
7. Hạn mức bảo hiểm tiền gửi Việt Nam phủ trên 92% **người gửi tiền**. Vì sao con số đó không cho
   biết hệ thống chống bank run tốt đến đâu? Cần thêm số liệu gì?
8. Luật Các tổ chức tín dụng 2024 cho phép chi trả toàn bộ theo quyết định của Thủ tướng. Nêu một lý
   do điều này **giảm** rủi ro bank run và một lý do nó **tăng** rủi ro đạo đức.

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  NGÂN HÀNG — Yale ECON 252 buổi 13, Robert Shiller (Xuân 2011)               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  HAI CHÊNH LỆCH, chỉ một cái nguy hiểm                                       ║
║    lãi suất: vay 1 % cho vay 5 %         -> nguồn thu, vô hại                ║
║    KỲ HẠN:   vay 0 ngày cho vay 30 năm   -> nguồn thu, VÀ là chỗ gãy         ║
║                                                                              ║
║  BA BÀI TOÁN ngân hàng giải mà thị trường không giải được                    ║
║    thanh khoản      Diamond-Dybvig 1983 (Shiller đọc nhầm 1988)              ║
║    lựa chọn ngược   cán bộ tín dụng sống trong cộng đồng, nghe ngóng         ║
║    rủi ro đạo đức   giám sát liên tục, cho vay ngắn hạn liên tục gia hạn     ║
║    => cả ba là thứ HỢP ĐỒNG GIẤY KHÔNG XỬ LÝ ĐƯỢC, chỉ QUAN HỆ KÉO DÀI       ║
║       theo thời gian mới xử lý được.                                         ║
║                                                                              ║
║  DIAMOND-DYBVIG — 100 người, r₁ = 1,28                                       ║
║    cân bằng tốt: người gấp +28 %, người kiên nhẫn -9,3 %, ai cũng thích      ║
║    cân bằng xấu: 78 người được trả ĐỦ, người 79 được 0,16, 21 người = 0      ║
║    Ngân hàng KHÔNG hề mất khả năng thanh toán. Xếp hàng sớm là HỢP LÝ.       ║
║    r₁ = 1,00 là mức duy nhất miễn nhiễm run — tức là không có ngân hàng.     ║
║                                                                              ║
║  BẢO HIỂM TIỀN GỬI — bốn lần, một chiều duy nhất                             ║
║    FDIC 1933      chưa bao giờ đổ (đúng tới 3/2023)                          ║
║    FSLIC 1980s    QUỸ BẢO HIỂM tự phá sản -> chính phủ trả 150 tỷ đô         ║
║    Northern Rock  bảo hiểm MỘT PHẦN không đủ -> bảo lãnh toàn bộ             ║
║    IKB 2007       Đức cứu TRƯỚC khi có run -> 1,5 tỷ euro                    ║
║                                                                              ║
║    >> "LỚP BẢO ĐẢM SAU CÙNG THẬM CHÍ KHÔNG ĐƯỢC VIẾT RA" (13 37:04)          ║
║                                                                              ║
║  BASEL — vốn tính trên TÀI SẢN CÓ RỦI RO, không phải tổng tài sản            ║
║    0 %   trái phiếu chính phủ OECD                                           ║
║    20 %  trái phiếu địa phương VÀ Fannie/Freddie   <- sai lầm lớn            ║
║    50 %  vay mua nhà                                                         ║
║    100 % còn lại, kể cả CHO VAY DOANH NGHIỆP                                 ║
║    400 tr tài sản -> 170 tr RWA -> 7 % -> 11,90 tr vốn phải giữ              ║
║                                                                              ║
║  CHỖ BASEL ĐẨY SAI HƯỚNG — cùng 1 triệu đô vốn thừa:                         ║
║    mua Fannie Mae         71,43 triệu                                        ║
║    cho doanh nghiệp vay   14,29 triệu     -> chênh 5 LẦN                     ║
║    Hội đồng chọn Fannie vì LÝ TRÍ, không phải vì tham.                       ║
║    QUY ĐỊNH THẤT BẠI VÌ ĐƯỢC TUÂN THỦ, KHÔNG PHẢI VÌ BỊ LÁCH.                ║
║                                                                              ║
║  ĐỐI CHIẾU 2026                                                              ║
║    9/3/2023   SVB: 42 tỷ đô rút trong MỘT NGÀY, 100 tỷ xếp hàng hôm sau      ║
║               -> Diamond-Dybvig diễn ra QUA ĐIỆN THOẠI. Tốc độ tháo chạy     ║
║                  không còn bị giới hạn bởi tốc độ đi bộ.                     ║
║    12/3/2023  Mỹ viện ngoại lệ rủi ro hệ thống, bảo vệ CẢ phần vượt hạn      ║
║               mức -> đúng khuôn mẫu FSLIC 1989 và Northern Rock 2007         ║
║    9/2026     Basel III VẪN chưa xong ở Mỹ (đề xuất lại 19/3/2026);          ║
║               Anh 1/1/2027; EU sàn đầu ra tới 2030. Shiller đoán 2019.       ║
║    2022       Diamond và Dybvig nhận Nobel — đúng một năm trước SVB          ║
║    2017-2025  Monte dei Paschi (lập 1472) được nhà nước cứu 8,1 tỷ euro,     ║
║               rồi 2025 thâu tóm Mediobanca 16 tỷ euro                        ║
║                                                                              ║
║  🇻🇳 GÓC VIỆT NAM                                                             ║
║    125 triệu đồng/người/tổ chức (QĐ 32/2021, hiệu lực 12/12/2021)            ║
║    TRẢ 100 % tới hạn mức — KHÔNG đồng bảo hiểm  <- đúng bài học 2007         ║
║    Phủ hơn 92 % NGƯỜI GỬI... nhưng đó là số NGƯỜI, không phải số TIỀN        ║
║       -> tỷ lệ phủ theo đầu người KHÔNG đo được rủi ro bank run;             ║
║          tỷ lệ phủ theo SỐ TIỀN mới đo được.                                 ║
║    Luật TCTD 2024: NHNN có thể trình Thủ tướng trả TOÀN BỘ                   ║
║       -> Việt Nam VIẾT cái "ngoài văn bản" VÀO văn bản.                      ║
║          Được: khủng hoảng đến thì không phải ứng biến.                      ║
║          Mất: một bảo lãnh ai cũng biết là thật = rủi ro đạo đức thật.       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

**Video gốc**

- Yale ECON 252 *Financial Markets* (2011), buổi 13 "Banks" — YouTube `1mDL1fKEVZM`, 73:19.
  Phụ đề tiếng Anh do người viết; transcript đầy đủ tại
  [Open Yale Courses](https://oyc.yale.edu/economics/econ-252-11/lecture-13).
- Giáo trình Shiller giao: Fabozzi, Modigliani & Jones, *Foundations of Financial Markets and
  Institutions*.

**Nguồn cho các đính chính ở §9**

- Diamond, D.W. & Dybvig, P.H. (1983), "Bank Runs, Deposit Insurance, and Liquidity", *Journal of
  Political Economy* 91(3), 401–419 —
  [bản quét](https://www.bu.edu/econ/files/2012/01/DD83jpe.pdf) ·
  [EconPapers](https://econpapers.repec.org/RePEc:ucp:jpolec:v:91:y:1983:i:3:p:401-19)
- FSCS, mức bảo vệ trước và sau 2007 —
  [FSCS protection has more than doubled since the financial crisis](https://www.fscs.org.uk/news/protection/protection-doubled-since-crash/)
- Bối cảnh Northern Rock và tuyên bố bảo lãnh của Alistair Darling —
  [Yale Program on Financial Stability](https://newbagehot.yale.edu/docs/united-kingdom-financial-services-compensation-scheme)

**Nguồn cho §10 — đối chiếu 2026**

- Metrick, A. (2024), "The Failure of Silicon Valley Bank and the Panic of 2023", Yale Tobin Center —
  [PDF](https://tobin.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf)
- Congressional Research Service, "Bank Failures: The FDIC's Systemic Risk Exception" —
  [IF12378](https://www.congress.gov/crs-product/IF12378)
- FDIC, "Lessons Learned from the U.S. Regional Bank Failures of 2023" —
  [bài phát biểu 2024](https://www.fdic.gov/news/speeches/2024/lessons-learned-us-regional-bank-failures-2023)
- Nghị viện châu Âu, "The implementation of Basel III: progress, divergence" (2025) —
  [PDF](https://www.europarl.europa.eu/RegData/etudes/IDAN/2025/773694/ECTI_IDA(2025)773694_EN.pdf)
- Uỷ ban châu Âu, "State aid: Commission authorises precautionary recapitalisation of Monte dei
  Paschi di Siena" (2017) —
  [IP/17/1905](https://ec.europa.eu/commission/presscorner/detail/en/ip_17_1905)
- Nghị viện châu Âu, "The precautionary recapitalisation of Monte dei Paschi di Siena" —
  [briefing 2017](https://www.europarl.europa.eu/RegData/etudes/BRIE/2017/587392/IPOL_BRI(2017)587392_EN.pdf)

**Nguồn cho §11 — Góc Việt Nam**

- Quyết định 32/2021/QĐ-TTg về hạn mức trả tiền bảo hiểm —
  [Thư viện Pháp luật](https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Quyet-dinh-32-2021-QD-TTg-han-muc-tra-tien-bao-hiem-448826.aspx)
- Bảo hiểm tiền gửi Việt Nam, "Từ ngày 12/12/2021, hạn mức trả tiền bảo hiểm là 125 triệu đồng" —
  [div.gov.vn](https://www.div.gov.vn/tu-ngay-12-12-2021-han-muc-tra-tien-bao-hiem-la-125-trieu-dong)
- Báo Chính phủ, "Nâng hạn mức trả tiền bảo hiểm tiền gửi lên 125 triệu đồng" —
  [baochinhphu.vn](https://baochinhphu.vn/nang-han-muc-tra-tien-bao-hiem-tien-gui-len-125-trieu-dong-102302543.htm)

---

**Bản đồ khoá học**

Yale ECON 252 — *Thị trường Tài chính*, Robert J. Shiller · [chỉ mục môn học](../README.md)

1. [Tài chính là hạ tầng xã hội](bai_01_ha_tang_xa_hoi.md) — phát minh, trách nhiệm hữu hạn, gắn chỉ số lạm phát
2. [Bảo hiểm](bai_02_bao_hiem.md) — gộp rủi ro, và ba chỗ nó gãy
3. **Ngân hàng** — thanh khoản, lựa chọn ngược, bank run, Basel ← *bạn đang ở đây*
4. [Chính sách tiền tệ](bai_04_chinh_sach_tien_te.md) — ngân hàng trung ương, công cụ, giới hạn
5. [Ngân hàng đầu tư](bai_05_ngan_hang_dau_tu.md) — shadow banking, repo, đòn bẩy
6. [Sở giao dịch, môi giới, dealer, HFT](bai_06_so_giao_dich.md) — sổ lệnh, tạo lập, thanh toán bù trừ
7. [Nhà quản lý quỹ và nghĩa vụ tín thác](bai_07_quan_ly_quy.md) — quy tắc người thận trọng, hưu trí, Mô hình Yale
8. [Cổ phiếu nhìn từ góc định chế](bai_08_co_phieu_dinh_che.md) — cổ tức, pha loãng, bảng cân đối, giá trên sổ sách
9. [Bất động sản](bai_09_bat_dong_san.md) — từ quyền tài sản tới MBS
10. [Quy định, tự quản, hành vi sai trái](bai_10_quy_dinh_tu_quan.md) — năm tầng, năm cửa thoát, con lắc của Laura Cha
11. [Tài chính công và phi lợi nhuận](bai_11_tai_chinh_cong.md) — phi lợi nhuận, ngân sách vốn, Bismarck và công nghệ thông tin
12. [Tài chính hành vi](bai_12_tai_chinh_hanh_vi.md) — Shiller phản biện Lo
13. [Mục đích, đạo đức, dân chủ hoá tài chính](bai_13_muc_dich_dao_duc.md) — bài giảng kết — bất bình đẳng là thất bại quản trị rủi ro

📐 Nửa **định giá** nằm ở kho bên cạnh: [MIT 15.401 — Lý thuyết Tài chính I](../../mit-15401-finance/README.md)
🐍 Chương trình Python tính mọi con số: [thuc_hanh/README.md](../thuc_hanh/README.md)
