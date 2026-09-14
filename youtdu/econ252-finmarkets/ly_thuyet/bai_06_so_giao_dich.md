# Sở giao dịch, môi giới, dealer và giao dịch tần suất cao

> [!info] Về bài này
> Bài học dựng từ **buổi 21** khoá **Yale ECON 252 *Financial Markets*** (Xuân 2011), giảng viên
> **Robert J. Shiller** — YouTube `kAl8DezwLAE`, 7 chương, ~72 phút.
> Mục có mốc `21 MM:SS` là **lấy từ video**, đã đối chiếu ngược với phụ đề gốc bằng script.
> Mục có 📚 là **kiến thức bài này bổ sung**, không có trong video.
> Mục có 🇻🇳 là **số liệu Việt Nam**, không có trong video, mọi con số đều trích nguồn.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).
>
> **Nên đọc trước:** [Bài 5 — Ngân hàng đầu tư](bai_05_ngan_hang_dau_tu.md) (chênh lệch mua-bán,
> vòng xoáy ký quỹ), [Bài 12 — Tài chính hành vi](bai_12_tai_chinh_hanh_vi.md) (thao túng giá).

Đây là buổi giảng **vi cấu trúc thị trường** duy nhất của cả khoá — buổi duy nhất Shiller nói về việc
một lệnh mua thật sự đi qua những đâu. Ông chiếu lên màn hình một sổ lệnh NASDAQ Level II rồi giải
thích bằng lời.

Bài này dựng lại **chính sổ lệnh đó** và cho các loại lệnh chạy qua nó. Có những thứ chỉ nhìn bằng mắt
thì không thấy được — trong đó có **một chỗ lời giảng nói quá**, và nó là chỗ nguy hiểm nhất cho người
mới.

---

## Mục lục

1. [Trao đổi là trung tâm của kinh tế học](#1-trao-đổi-là-trung-tâm-của-kinh-tế-học)
2. [Môi giới và người tạo lập — ranh giới nền tảng](#2-môi-giới-và-người-tạo-lập--ranh-giới-nền-tảng)
3. [Lịch sử sở giao dịch, từ đền Castor tới cây bàng](#3-lịch-sử-sở-giao-dịch-từ-đền-castor-tới-cây-bàng)
4. [Ba loại lệnh](#4-ba-loại-lệnh)
5. [⚠️ Lệnh dừng lỗ — chỗ lời giảng nói quá](#5-lệnh-dừng-lỗ--chỗ-lời-giảng-nói-quá)
6. [Sổ lệnh Level II — thứ Shiller chiếu lên màn hình](#6-sổ-lệnh-level-ii--thứ-shiller-chiếu-lên-màn-hình)
7. [📚 Lệnh thị trường ăn vào sổ lệnh](#7-lệnh-thị-trường-ăn-vào-sổ-lệnh)
8. [Giao dịch điện tử, ECN và HFT](#8-giao-dịch-điện-tử-ecn-và-hft)
9. [1987, uỷ ban Brady và cầu dao ngắt mạch](#9-1987-uỷ-ban-brady-và-cầu-dao-ngắt-mạch)
10. [Trả tiền cho luồng lệnh và Hệ thống Thị trường Quốc gia](#10-trả-tiền-cho-luồng-lệnh-và-hệ-thống-thị-trường-quốc-gia)
11. [Ngày 6/5/2010](#11-ngày-652010)
12. [Nghề tạo lập: lựa chọn ngược và bài toán phá sản](#12-nghề-tạo-lập-lựa-chọn-ngược-và-bài-toán-phá-sản)
13. [⚠️ Đối chiếu 2026](#13-đối-chiếu-2026)
14. [🇻🇳 Góc Việt Nam](#14-góc-việt-nam)
15. [Chương trình](#15-chương-trình)
16. [Từ điển thuật ngữ](#16-từ-điển-thuật-ngữ)
17. [Câu hỏi tự kiểm tra](#17-câu-hỏi-tự-kiểm-tra)

---

## 1. Trao đổi là trung tâm của kinh tế học

Shiller mở đầu bằng tên buổi giảng: **sở giao dịch và trung tâm thanh toán bù trừ** (`21 00:02`). Giữ
chữ thứ hai lại — [§14](#14-góc-việt-nam) sẽ quay lại nó, và đó là chỗ Việt Nam còn thiếu.

Ông dẫn thầy cũ của mình, **Kenneth Boulding**, người ông từng học ở Đại học Michigan. Trong bài diễn
văn nhậm chức chủ tịch Hội Kinh tế Mỹ năm 1969, Boulding đặt lại câu hỏi *kinh tế học là gì*. Định
nghĩa quen thuộc — **phân bổ nguồn lực khan hiếm** — Boulding thấy không ổn, vì chính trị học cũng
phân bổ nguồn lực khan hiếm, và ngay cả gia đình cũng vậy. Ông đề nghị: kinh tế học là **môn học về sự
trao đổi**. Giá và lượng, hai thứ kinh tế học nhấn mạnh nhất, chính là hai tham số của một cuộc trao
đổi.

Rồi Shiller dẫn **Karl Polanyi**, ***The Great Transformation*** (1944). "Chuyển hoá vĩ đại" theo
Polanyi là gì? Là **phát minh ra sự trao đổi**. Ông cho rằng trong các xã hội sơ khai gần như không
có **trao đổi sòng phẳng** — loại giao dịch chỉ gồm một mức giá và một số lượng, không kèm quan hệ nào
khác. Trước đó chỉ có **trao đổi quà tặng**: bạn củng cố một mối quan hệ bằng cách tặng, rồi người kia
đáp lễ về sau. Không có giá.

📌 Đáng chú ý là Shiller **không để lập luận này đứng yên**. Ông nói ngay rằng một số nhà nhân học nghi
ngờ mốc 10.000 năm, và dẫn bằng chứng: các loại vật liệu như đá lửa để làm công cụ, hay thổ hoàng để
vẽ lên người, được tìm thấy **cách xa nơi khai thác hàng nghìn dặm** ngay từ thời đồ đá cũ — phân tích
hoá học truy được nguồn gốc. Vậy phải có trao đổi.

Rồi một sinh viên chen vào: *"Hay là họ chỉ giết người ta thôi?"* Shiller cười và công nhận: **có thể
lắm, vậy thì chẳng ai biết cả.**

Đoạn đối đáp đó ngắn nhưng nó dạy một điều: **bằng chứng "hàng hoá xuất hiện xa nơi khai thác" không
phân biệt được trao đổi với cướp bóc.** Cả hai đều di chuyển hàng hoá. Muốn phân biệt thì cần bằng
chứng khác — và đó chính là loại lỗ hổng suy luận mà một khoá học nên dạy người ta nhìn ra.

---

## 2. Môi giới và người tạo lập — ranh giới nền tảng

Shiller nói ông có sẵn định nghĩa gần như một khẩu hiệu (`21 06:22`):

|                       | **Môi giới** (broker) | **Người tạo lập / dealer**             |
| --------------------- | --------------------- | -------------------------------------- |
| Giao dịch **cho ai**  | cho **người khác**    | cho **chính mình**                     |
| Tư cách pháp lý       | **đại lý** (agent)    | **bên chính** (principal) (`21 07:00`) |
| Kiếm tiền bằng        | **hoa hồng**          | **chênh lệch giá** (markup)            |
| Có nắm giữ hàng không | **không**             | **có**                                 |
| Rủi ro giá            | của khách             | **của chính mình**                     |

Hai ví dụ đời thường ông dùng rất đắt:

- **Bán nhà** → bạn thuê **môi giới** bất động sản. Người này **không mua nhà của bạn**; họ nhận
  khoảng 6% giá trị nếu tìm được người mua.
- **Mua tủ ngăn kéo cũ** → bạn tới **cửa hàng đồ cổ**. Người bán **đã sở hữu** món đồ, và kiếm lời
  bằng cách bán lại **cao hơn giá họ mua vào** (`21 08:40`).

Rồi ông đặt một câu hỏi hay mà **ông không trả lời được** — và ông nói thẳng là không: **vì sao đồ cổ
bán qua dealer còn bất động sản bán qua môi giới?** Ông kể đã cùng một đồng nghiệp đi tìm "dealer bất
động sản" khắp nơi và gần như không thấy ở đâu; sinh viên tìm được vài trường hợp ở Đức, thế thôi.

Hai giả thuyết ông đưa ra:

1. **Thuế.** Dealer phải nộp thuế thu nhập trên lợi nhuận thương vụ, ở mức cao hơn thuế lãi vốn. Điều
   đó đẩy người ta ra khỏi nghề.
2. **Thông tin.** Định giá một căn nhà quá chủ quan và thị trường biến động nhanh, nên ôm nhà để bán
   lại quá rủi ro (`21 10:50`).

📌 Giả thuyết thứ hai mới là giả thuyết đúng hướng, và [§12](#12-nghề-tạo-lập-lựa-chọn-ngược-và-bài-toán-phá-sản)
sẽ cho thấy vì sao: nghề tạo lập chỉ sống được khi bạn **giao dịch đủ nhiều lần** để luật số lớn hoạt
động. Một dealer đồ cổ mua bán hàng trăm món; một "dealer bất động sản" mỗi năm chỉ vài căn. Với vài
căn thì không có phân phối nào để dựa vào — chỉ có vài canh bạc lớn.

Và câu trả lời cho thị trường chứng khoán là **cả hai** (`21 12:07`):

- **Sở Giao dịch New York (NYSE)** là **thị trường môi giới** — chính xác hơn là **đấu giá hai chiều
  liên tục**. Bạn trả **hoa hồng**.
- **NASDAQ** là **thị trường tạo lập**. Bạn trả **chênh lệch giá**.

---

## 3. Lịch sử sở giao dịch, từ đền Castor tới cây bàng

Shiller kể lịch sử theo lối liệt kê nhanh, và điều thú vị là **mọi sở giao dịch lớn đều bắt đầu ngoài
trời**.

**La Mã cổ đại.** *"Sở giao dịch chứng khoán đầu tiên mà tôi nghĩ là ai cũng biết tới"* (`21 12:47`).
Người giao dịch gặp nhau ngoài trời **tại Quảng trường La Mã, ở đền Castor** (`21 13:18`) — *"đó là
nơi bạn tới để mua và bán cổ phần"* (`21 13:32`). Cổ phần trong tiếng Latin gọi là ***partes***
(`21 13:35`), công ty gọi là ***publicani*** (`21 13:40`).

Đặc điểm kỳ lạ Shiller nhấn (`21 13:47`): **khách hàng của họ là nhà nước.** Họ làm dịch vụ cho chính
quyền — cung cấp ngựa cho quân đội, hoặc **nuôi đàn ngỗng trên đồi Capitol** (`21 13:58`). Ngỗng được
coi là thiêng ở La Mã cổ *"vì chúng từng báo động một cuộc xâm lăng bằng cách kêu quang quác"*
(`21 14:07`) — nên *"có hẳn một publicanus phụ trách việc cho ngỗng ăn"* (`21 14:14`). Người ta có
bàn về giá cổ phần, và *"biết rằng giá lên xuống, ngay cả hồi đó, nhưng **không có dữ liệu nào** về
giá cổ phần của họ"* (`21 14:26`).

> [!warning]
> Shiller nói rõ ông dựa vào nghiên cứu của **Ulrike Malmendier** (`21 12:59`), người đã nghiên cứu
> các sở giao dịch La Mã cổ *"nhiều nhất có thể nghiên cứu được"* — và rằng ***"không có nhiều bằng
> chứng về nó"*** (`21 13:16`). Đó là cách trích dẫn đúng — nên khi bạn gặp câu "La Mã đã có sàn chứng
> khoán" ở nơi khác, hãy nhớ chính người kể cũng đã gắn kèm cảnh báo.

Rồi *"một khoảng trống dài cho sở giao dịch sau khi Đế chế La Mã sụp đổ, và các publicani biến mất"*
(`21 14:32`):

|                Năm | Nơi        | Sự kiện                                                                                                                       | Mốc        |
| -----------------: | ---------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- |
|           **1602** | Amsterdam  | Công ty Đông Ấn Hà Lan bắt đầu giao dịch — *"sự tái sinh của sở giao dịch"*                                                   | `21 14:58` |
|           **1698** | London     | Ai đó bắt đầu **dán giá cổ phiếu lên tường quán cà phê Jonathan's**; *"Sở Giao dịch London mọc ra từ quán cà phê Jonathan's"* | `21 15:38` |
|           **1792** | New York   | Người giao dịch Mỹ gặp nhau ngoài trời **dưới một cây buttonwood** và ký thoả thuận lập NYSE                                  | `21 16:14` |
| thập niên **1850** | Bombay     | Người giao dịch tụ dưới **một cây đa** nổi tiếng — *"cây đa oai vệ hơn cây buttonwood"*                                       | `21 16:55` |
|           **1875** | Bombay     | Sở Giao dịch Bombay chính thức thành lập                                                                                      | `21 17:10` |
|           **1890** | São Paulo  |                                                                                                                               | `21 19:58` |
|           **1894** | Mexico     | nước này tới nay vẫn chỉ có **một** sở giao dịch                                                                              | `21 20:05` |
|           **1990** | Trung Quốc | Thượng Hải và Thâm Quyến — *"vì chính quyền cộng sản, Trung Quốc không có sở giao dịch cho tới 1990"*                         | `21 19:11` |
|           **1992** | Ấn Độ      | **Sở Giao dịch Quốc gia (NSE)** — *"toàn điện tử, nên nó là phiên bản hiện đại"*                                              | `21 18:48` |

Shiller nhấn một điểm (`21 20:11`): ta có **hai loại sở giao dịch** — *"loại cũ, ít nhất 100 tuổi, và
loại mới chạy điện tử"*. Và loại mới **đuổi rất nhanh**: NSE ra đời năm 1992 *"đang bắt kịp Sở Giao
dịch Bombay rất nhanh"* (`21 19:00`) — một sàn 117 tuổi.

Ông cũng mô tả sàn NYSE vẫn hoạt động theo kiểu cũ (`21 17:51`–`21 18:20`): có một **sàn giao dịch vật
lý**, môi giới *"thật sự đến tận nơi bằng thân xác và đứng đó"*, mỗi cổ phiếu có một **trạm** riêng, và
nếu khách muốn mua IBM thì *"bạn đi tới đám đông IBM… và bạn làm việc đó **bằng miệng**"*. Ông so sánh
thẳng: *"y như ở quán cà phê Jonathan's"* (`21 17:55`).

**NASDAQ** ra đời thập niên 1970 từ một vấn đề cụ thể (`21 21:05`). NYSE khi đó có **điều kiện niêm
yết** rất chặt (`21 21:26`). Hệ quả là công ty không đạt chuẩn bị đẩy ra **thị trường phi tập trung
(OTC)** (`21 22:08`), nơi môi giới *"gọi điện cho nhau, hoặc thật ra là gặp nhau ngoài đường"*
(`21 22:30`), và giá được in trên **các tờ giấy màu hồng** (`21 22:52`). Một tổ chức của chính các nhà
kinh doanh OTC (`21 22:59`) bèn dựng hệ thống máy tính đầu tiên — *"đó là hệ thống NASDAQ"*
(`21 23:28`).

📌 Chi tiết đáng nhớ: **NASDAQ sinh ra từ những công ty bị NYSE từ chối.** Và bốn mươi năm sau,
[§13](#13-đối-chiếu-2026) cho thấy chính NASDAQ đã đi hỏi mua NYSE.

> [!warning]
> Một chỗ cần đính chính nhỏ. Shiller nói (`21 24:05`): *"phát minh **đầu tiên** của Thomas Edison
> thật ra là một máy in giá chứng khoán"*, và đoán *"khoảng thập niên 1870"* (`21 24:10`). Bằng sáng chế
> đầu tiên của Edison — **cấp năm 1869** — là một **máy đếm phiếu bầu bằng điện**, thứ không ai mua. Máy
> in giá chứng khoán cải tiến của ông đến ngay sau đó và là **thành công thương mại đầu tiên**, chứ không
> phải phát minh đầu tiên.

Chi tiết nhỏ, nhưng nó đổi ý nghĩa câu chuyện: bài học thật là **phát minh đầu tiên của Edison đã thất
bại** — và ông chuyển sang thứ thị trường thật sự cần. Phần còn lại Shiller nói đúng và nói hay
(`21 24:14`): máy in giá *"chỉ là một bản ghi những gì vừa giao dịch. Nó **không phải** một hệ thống
giúp bạn giao dịch"* — thuần tuý lịch sử, không phải công cụ. Đó đúng là ranh giới mà [§6](#6-sổ-lệnh-level-ii--thứ-shiller-chiếu-lên-màn-hình)
và [§8](#8-giao-dịch-điện-tử-ecn-và-hft) sẽ vượt qua: từ **báo cáo** giá sang **hình thành** giá.

---

## 4. Ba loại lệnh

Phần này ngắn nhưng là phần thực dụng nhất cả buổi.

**Lệnh thị trường.** Bạn chỉ nói **số lượng**, không nói giá. Môi giới sẽ cố lấy giá tốt nhất, nhưng
bạn **không biết trước giá**. Shiller diễn tả phản ứng của môi giới khi khách phàn nàn: *nếu không hài
lòng thì lẽ ra anh phải nói trước.*

**Lệnh giới hạn.** Bạn nói **cả số lượng lẫn giá**. Lệnh mua sẽ chỉ khớp ở mức giá bạn đặt hoặc thấp
hơn; lệnh bán ở mức đó hoặc cao hơn. Có thể **không khớp**, hoặc **khớp một phần**.

**Lệnh dừng.** Cũng nói cả số lượng và giá, nhưng **chiều ngược lại** (`21 27:52`):

|              | Lệnh **giới hạn** bán | Lệnh **dừng** bán |
| ------------ | --------------------- | ----------------- |
| Khớp khi giá | **≥** mức bạn đặt     | **≤** mức bạn đặt |
| Mục đích     | bán ở giá tốt         | **cắt lỗ**        |

Còn có **lệnh dừng mua**, dùng khi bạn đang **bán khống** và muốn chặn khoản lỗ vô hạn nếu giá tăng.

Và Shiller nhắc lời khuyên phổ biến của giới tư vấn (`21 29:08`): ***đừng bao giờ đặt lệnh thị
trường.*** Luôn có một mức giá mà bạn sẽ không hài lòng, vậy thì cứ nói ra. Một số sở giao dịch **thậm
chí không cho phép** lệnh thị trường.

---

## 5. Lệnh dừng lỗ — chỗ lời giảng nói quá

Đây là chỗ quan trọng nhất cần đính chính trong cả buổi, vì nó là loại lệnh mà người mới dùng nhiều
nhất và hiểu sai nhiều nhất.

Shiller giải thích (`21 28:13`–`28:17`): giá đang 100, bạn đặt lệnh dừng lỗ ở 80, **"thế là ít nhất
tôi biết tôi không thể mất quá 20% khoản đầu tư"**.

**Câu đó không đúng.** Và lý do nằm ngay trong định nghĩa của chính loại lệnh này:

> [!note]
> Lệnh dừng lỗ khi bị kích hoạt sẽ **trở thành lệnh thị trường**. Nó bảo đảm **BÁN**, không bảo đảm
> **GIÁ**. Mức 80 là mức **kích hoạt**, không phải mức bán. Mức bán là **bất cứ giá nào còn trên sổ
> lệnh tại thời điểm đó**.

[Mục 3 của chương trình](#15-chương-trình) cho thấy khoảng cách giữa hai thứ đó:

| Tình huống             | Giá khớp thực |    Mất thật |
| ---------------------- | ------------: | ----------: |
| thị trường bình thường |         80,00 |     20,00 % |
| mở cửa gap giá         |         72,00 |     28,00 % |
| tin xấu đột ngột       |         61,00 |     39,00 % |
| **ngày 6/5/2010**      |      **0,01** | **99,99 %** |

Hàng cuối **không phải giả thuyết**. Đó chính là ngày [§11](#11-ngày-652010) mô tả, và Shiller kể
chính ông rằng hôm đó có cổ phiếu 30 đô giao dịch ở 30 xu rồi bật lại.

> [!note]
> **Nghịch lý của lệnh dừng lỗ:** nó được thiết kế để bảo vệ bạn khỏi cú sập. Nhưng đúng trong cú sập
> là lúc sổ lệnh mỏng nhất, nên đó cũng là lúc nó thực hiện tệ nhất. **Nó hoạt động tốt nhất khi bạn
> cần nó ít nhất.**

> [!note] Cách xử lý đúng
> là dùng **lệnh dừng-giới hạn** (*stop-limit*): khi giá chạm mức kích hoạt, lệnh
> trở thành **lệnh giới hạn** chứ không phải lệnh thị trường. Đánh đổi thì rõ ràng và không tránh được:

|                      | Dừng lỗ (stop-market) | Dừng-giới hạn (stop-limit) |
| -------------------- | --------------------- | -------------------------- |
| Bảo đảm **bán được** | ✅                     | ❌                          |
| Bảo đảm **giá**      | ❌                     | ✅                          |
| Rủi ro của bạn       | bán ở giá thảm hoạ    | **không bán được gì cả**   |

Không có loại lệnh nào bảo đảm cả hai. Đó là lý do câu *"tôi không thể mất quá 20%"* là một câu không
loại lệnh nào thực hiện được.

---

## 6. Sổ lệnh Level II — thứ Shiller chiếu lên màn hình

Shiller chiếu lên màn hình một **sổ lệnh giới hạn NASDAQ Level II** (`21 29:29`) — ảnh chụp đứng yên
của thứ mà trên máy thật sẽ nhấp nháy liên tục.

Sáu cột: **khối lượng, giá, nơi đặt lệnh** cho mỗi bên. **MPID** là mã định danh nơi lệnh được đặt.
Máy tính đã **sắp xếp sẵn**: bên mua giảm dần từ trên xuống, bên bán tăng dần.

Rồi ông chỉ ra điều quan trọng nhất (`21 34:37`): giá bán tốt nhất **cao hơn** giá mua tốt nhất, nên
**không có giao dịch nào xảy ra**. Nếu vẽ chúng thành đường cung và đường cầu, **hai đường không cắt
nhau** — trong khi lẽ ra chúng phải cắt nhau ở đâu đó.

Ông giải thích ngay vì sao điều đó **không hề lạ**: nếu chúng cắt nhau, lệnh đã khớp và **biến mất
khỏi màn hình** ngay lập tức.

> [!note]
> 📌 Đây là một ý ngắn mà sâu: **sổ lệnh không phải ảnh chụp cung cầu của thị trường.** Nó là ảnh chụp
> phần cung cầu mà thị trường **chưa tiêu hoá được**. Mọi thứ khớp được đã khớp rồi.

Và ông so sánh hai gói dịch vụ (`21 34:59`): **Level I chỉ cho bạn hàng đầu tiên** — tức chênh lệch
mua-bán trong cùng. **Level II cho bạn cả sổ.** Với Level II bạn biết được, chẳng hạn, giá sẽ khó rơi
nhanh xuống dưới một mức nào đó vì ở đó **có một người mua lớn đang đợi**.

[Mục 1 của chương trình](#15-chương-trình) dựng lại sổ lệnh đó và tính **độ sâu tích luỹ** — thứ Level
I không cho thấy:

| Mức giá | KL mua tích luỹ | Mức giá | KL bán tích luỹ |
| ------: | --------------: | ------: | --------------: |
|   25,23 |             100 |   25,24 |           2.400 |
|   25,22 |           9.530 |   25,24 |      **10.600** |
|   25,21 |          12.330 |   25,25 |          12.100 |
|   25,20 |          26.530 |   25,26 |          18.800 |
|   25,19 |          32.130 |   25,27 |          30.800 |
|   25,18 |      **63.130** |   25,28 |      **57.300** |

> [!warning]
> Chú ý hàng thứ hai bên bán. **Hai lệnh đầu tiên đều ở 25,24**, từ hai nơi khác nhau — chính Shiller
> cũng chỉ ra điều này (`21 33:21`): hai khách hàng khác nhau, cùng một mức giá, vẫn là hai lệnh riêng.
> Nên **độ sâu thật ở đỉnh sổ lệnh là 10.600 cổ phiếu, không phải 2.400.**

Đó là kiểu chi tiết chỉ hiện ra khi bạn cộng các con số lại — và là lý do bảng này đáng dựng.

---

## 7. Lệnh thị trường ăn vào sổ lệnh

Shiller nhắc rằng nếu môi giới muốn 10.000 cổ phiếu thì *"chúng sẽ ở nhiều mức giá khác nhau"*. Ông
dừng ở đó. [Mục 2 của chương trình](#15-chương-trình) tính ra bao nhiêu.

| Khối lượng đặt mua | Giá bình quân thực | Trượt giá | Chi phí trượt |
| -----------------: | -----------------: | --------: | ------------: |
|                100 |            25,2400 |   0,000 % |      0,00 USD |
|             10.000 |            25,2400 |   0,000 % |      0,00 USD |
|             12.100 |            25,2412 |   0,000 % | **15,00 USD** |
|             25.000 |            25,2534 |   0,050 % |    335,00 USD |
|             57.300 |            25,2674 |   0,110 % |  1.569,00 USD |

Ba điều rút ra:

**Một.** Mọi lệnh từ **10.600 cổ phiếu trở xuống** đều được đúng giá niêm yết, **không trượt một xu**.
Sổ lệnh có một "vùng phẳng", và biết nó rộng bao nhiêu là thông tin có giá trị thật.

**Hai.** Hàng 12.100 đáng nhìn kỹ: cột tỷ lệ hiện **0,000 %** nhưng cột chi phí hiện **15 USD**. Trượt
giá thật là **nửa điểm cơ bản** — quá nhỏ để hiện ra ở ba chữ số thập phân, nhưng tiền thì có thật.
Đây là lý do bảng có cả hai cột: tỷ lệ để so sánh, tiền để biết mình mất gì.

**Ba.** Ăn hết **cả sáu mức** chào bán trên màn hình chỉ cần **57.300 cổ phiếu**. Sổ lệnh mỏng hơn rất
nhiều so với cảm giác — và đó là lúc thị trường đang **bình thường**.

📌 Nối vào §5: nếu 57.300 cổ phiếu đã quét sạch sổ lệnh trong ngày thường, thì trong một cú sập — khi
người tạo lập rút lệnh và người mua biến mất — chuyện giá rơi xuống 1 xu **không còn là điều khó
hiểu**. Nó là số học.

---

## 8. Giao dịch điện tử, ECN và HFT

Trên hệ thống tự động hoàn toàn, lệnh khớp **tức thì** — *"con số thậm chí không hiện trên màn hình đủ
lâu để bạn nhìn thấy nó"* (`21 36:31`).

**Giao dịch tần suất cao (HFT)** là *"giao dịch do máy tính thực hiện"* (`21 36:41`, `21 36:56`).
Shiller giải thích bằng một tương phản rất rõ (`21 37:01`–`21 37:28`): khi phải giao dịch qua môi giới
sàn ở NYSE, mọi thứ *"phải diễn ra theo **nhịp con người**"* — bạn gọi điện cho môi giới, môi giới gọi
cho người đại diện ở sàn, người đó **đi bộ** tới đám đông rồi bàn bạc. Và ông mô tả cuộc bàn bạc đó rất
đắt (`21 37:23`):

> [!quote]
> *"Nó giống một ván **poker**. Bạn không muốn lật bài, nhưng bạn dò xem người ta thế nào, rồi sau một
> hồi trao đổi thì chốt được một giao dịch."*

Khi mọi thứ nằm trong máy tính thì *"nó chạy **ngay lập tức**"* (`21 37:32`). Từ đó có **giao dịch
thuật toán / giao dịch bằng chương trình** (`21 37:57`), thứ có từ *"thực tế là từ thập niên 1970"*
(`21 38:07`) và *"chắc chắn tới thập niên 1980 đã thành một hiện tượng lớn"* (`21 38:15`).

Ông mô tả các **chiến lược mili giây** (`21 38:29`): bạn có thể phát một lệnh mua hoặc bán *"tồn tại
một phần nghìn giây"* rồi rút lại (`21 38:37`, `21 38:41`). Và ông nêu một cách dùng khiến người ta
phải suy nghĩ (`21 38:51`–`21 39:11`) — dùng nó để **lọc xem ai đang giao dịch với mình**:

> [!quote]
> *"Nếu bạn chỉ muốn giao dịch với **máy tính**, nếu bạn nghĩ con người quá tinh khôn so với mình…
> thì bạn viết một chiến lược mili giây, và thế là bạn **phân loại được ai giao dịch với bạn**."*

Hệ quả (`21 39:16`): HFT **thiên vị các sở giao dịch điện tử**, vì người ta *"muốn giao dịch trên
những sở hoàn toàn điện tử để chơi được hết những trò này"* (`21 39:30`) — nên **các sàn giao dịch vật
lý đang chết dần trên phần lớn thế giới** (`21 39:36`).

> [!warning]
> Và Shiller nói thẳng một điều dễ bỏ qua (`21 39:48`): **chính NYSE đã chậm chân** trong việc thích
> nghi với những công nghệ này. Đó là bối cảnh của cả phần còn lại.

Lịch sử của làn sóng này, theo Shiller, bắt đầu từ **ECN — mạng truyền thông điện tử** (`21 40:10`),
được **Uỷ ban Chứng khoán Mỹ** cho phép trong thập niên 1990 như **giải pháp thay thế cho sở giao
dịch** (`21 40:15`), *"ít nhất là như một **thí nghiệm**"* (`21 40:38`). Và cố tình **không gọi là sở
giao dịch** (`21 40:40`):

> [!quote]
> *"Nên họ không gọi mấy thứ này là sở giao dịch, họ gọi chúng là **ECN**."*

Hai cái quan trọng: **Archipelago** (`21 40:46`) và **Island** (`21 40:53`). Chúng *"thật ra chỉ là các
trang web nơi bạn có thể giao dịch, và chúng **mở cho công chúng**"* (`21 40:56`).

Và chúng có **một nền văn hoá khác** — văn hoá web (`21 41:02`):

> [!quote] 21 41:05
> *"Chúng tôi sẽ **không thu tiền của bạn để xem sổ lệnh**, chúng tôi cứ đưa nó ra cho tất cả mọi
> người. Web không thu tiền cho rất nhiều thứ."* (`21 41:05`)

Điều đó làm chúng thành nơi giao dịch phổ biến cho công chúng (`21 41:15`), và Shiller nói chúng
*"lớn lên theo cách máy tính cá nhân đã lớn lên"* (`21 41:20`).

Phản ứng ban đầu của NYSE với Archipelago (`21 41:23`):

> [!quote]
> *"À, đây chỉ là một đám sinh viên nghịch ngợm, kiểu một trò chơi máy tính thôi."*

Họ **không coi là nghiêm túc** (`21 41:32`) — cho tới khi *"Archipelago lớn quá nhanh"* (`21 41:37`),
và **NYSE phải mua lại nó năm 2005** (`21 42:14`), lúc **ARCX đã thở sát gáy NYSE về khối lượng giao
dịch** (`21 42:21`). Shiller nhấn quy mô của cú đổi (`21 42:35`): NYSE từng là *"một sở giao dịch danh
giá duy nhất, kéo dài **hơn 150 năm mà không có thay đổi thực chất nào**"* — rồi giao dịch điện tử ập
vào và *"mọi thứ bị đảo lộn"*.

Rồi NYSE sáp nhập với **Euronext** năm **2006** (`21 43:02`), và tại thời điểm giảng bài đang trong một
quá trình sáp nhập nữa với **Deutsche Börse** (`21 43:24`) — *"đó là năm 2011. **Chưa xong.**"*
(`21 43:33`). Trong khi đó **NASDAQ** đang chào mua NYSE, và **Intercontinental Exchange (ICE)** cũng
vậy (`21 43:37`). Bản ghi Open Yale Courses chèn một ghi chú ngay tại đây: *"Mô tả các sự kiện này là
tính tới ngày 13/4/2011."*

Ông tóm lại bằng một hình ảnh (`21 43:48`): **"những kẻ tí hon đang mua lại những gã khổng lồ già
nua."** Và dẫn lời **Laura Cha** từ một buổi trước (`21 43:55`): ta từng nghĩ sở giao dịch giống như
**công trình công ích** — *"mỗi nước có sở giao dịch của riêng mình, nó là niềm tự hào quốc gia"*
(`21 43:58`) — nhưng điều đó **không còn đúng nữa**.

📌 Laura Cha là khách mời của [bài 10](bai_10_quy_dinh_tu_quan.md). Chi tiết bà nêu ở đó — mọi tầng quy
định đều đang **sửa vấn đề của ngày hôm qua** — và chi tiết bà nêu ở đây là cùng một quan sát: định chế
tài chính được thiết kế cho một thế giới đã đi mất.

[§13](#13-đối-chiếu-2026) cho biết câu chuyện đó kết thúc ra sao.

---

## 9. 1987, uỷ ban Brady và cầu dao ngắt mạch

Ngày **19/10/1987**, chỉ số S&P 500 rơi **hơn 20 % trong một ngày** — cú rơi một ngày lớn nhất lịch sử
thị trường Mỹ. Tổng thống Reagan ra lệnh điều tra, giao cho **Nicholas Brady** (`21 45:31`).

**Uỷ ban Brady** kết luận **giao dịch bằng chương trình đóng vai trò lớn** trong cú rơi (`21 45:48`).
Cụ thể là một loại chương trình gọi là **"bảo hiểm danh mục"** — mà Shiller nói thẳng: *nó chẳng phải
bảo hiểm gì cả*. Nó là một chiến lược **bán tự động**, giống lệnh dừng lỗ nhưng tinh vi hơn và chạy
liên tục. Và nó tạo ra **một sự bất ổn mà không ai lường trước**.

Khuyến nghị nổi bật của uỷ ban (`21 46:37`–`46:47`): các sở giao dịch nên áp đặt **lệnh dừng giao
dịch** để ngăn cả thị trường sụp. Từ đó ra đời **cầu dao ngắt mạch** (`21 47:07`) — cơ chế tự động
dừng thị trường khi giá đang rơi.

📌 Nối thẳng vào §5: **bảo hiểm danh mục năm 1987 chính là lệnh dừng lỗ, phóng to lên quy mô toàn thị
trường.** Cùng một cơ chế — bán tự động khi giá xuống — và cùng một hậu quả: nó bán **đúng lúc thanh
khoản đã cạn**, làm giá rơi thêm, kích hoạt đợt bán tiếp theo. Ba trong bốn mục đầu của bài này nói về
đúng vòng lặp đó, ở ba quy mô khác nhau.

---

## 10. Trả tiền cho luồng lệnh và Hệ thống Thị trường Quốc gia

Vấn đề Shiller nêu (`21 47:46`): có **nhiều sở giao dịch**, và môi giới **được toàn quyền chọn** đưa
lệnh của bạn tới sở nào. Nên môi giới có thể chọn một nơi **không cho bạn giá tốt nhất**. Ông nói
thẳng (`21 48:17`): *môi giới, trên thực tế, có thể móc túi bạn.*

Rồi ông đặt tên cho cơ chế cụ thể (`21 48:23`): **trả tiền cho luồng lệnh** (*payment for order
flow*). Một người tạo lập sẵn sàng **trả phí cho môi giới** để lệnh của khách hàng bán lẻ được chuyển
tới mình thay vì tới NYSE. Điều đó **có thể không phục vụ lợi ích của khách**, vì khách rốt cuộc có
thể trả giá cao hơn.

Shiller giữ thái độ cân bằng: đây là **vấn đề khó**, vì rất khó giám sát mọi việc người ta làm, và
**có thể có lý do chính đáng** cho việc trả tiền mua luồng lệnh.

Phản ứng chính sách: năm **1975**, Quốc hội Mỹ lập **Hệ thống Thị trường Quốc gia (NMS)** cùng **Hệ
thống Giao dịch Liên thị trường (ITS)**. Nguyên tắc: môi giới **có nghĩa vụ lấy giá tốt nhất** cho
khách — *giá mua tốt nhất, giá chào bán tốt nhất* (`21 49:58`). Kèm theo là **hệ thống báo giá hợp
nhất**, cho phép môi giới nhìn giá ở mọi sở và định tuyến lệnh tới nơi có giá tốt nhất.

Nhưng Shiller chỉ ra ngay lỗ hổng, bằng chính sổ lệnh đang chiếu: nếu khách muốn **10.000 cổ phiếu**
thì **không thể khớp hết ở một giá**. Vậy nghĩa vụ "giá tốt nhất" áp dụng cho phần nào? Uỷ ban Chứng
khoán làm rõ vào khoảng 2006 rằng nghĩa vụ đó chỉ áp cho **mức giá tốt nhất ở đỉnh sổ**. Còn phần
còn lại thì *"chúng tôi không đi sâu vào được"*.

> [!note]
> Nên đó **không phải sự bảo vệ đầy đủ** cho khách hàng. Nghĩa vụ vẫn tồn tại, nhưng hệ thống quá phức
> tạp — quá nhiều máy tính, quá nhiều sở, quá nhiều quy tắc.

[§13.3](#133-trả-tiền-cho-luồng-lệnh--từ-vấn-đề-khó-thành-mô-hình-kinh-doanh) cho thấy vấn đề này về
sau đi tới đâu — và câu trả lời sẽ làm bạn ngạc nhiên.

---

## 11. Ngày 6/5/2010

Shiller giao **báo cáo chung của Uỷ ban Chứng khoán (SEC) và Uỷ ban Giao dịch Hàng hoá Tương lai
(CFTC)** về ngày này làm tài liệu đọc thêm (`21 53:48`), rồi kể lại (`21 52:51`–`21 53:18`):

Khoảng **2 giờ 30 chiều**, thị trường Mỹ **đã giảm 4 %**. Rồi *"trong vòng vài phút, nó rơi thêm
**6 %**"* (`21 53:02`), và sau đó *"nó **bật lại rất nhanh**"* (`21 53:07`). Một số cổ phiếu riêng lẻ
*"rơi xuống gần như bằng không"* — *"bạn có thể mua một cổ phiếu **30 đô** với giá **30 xu**, đại loại
thế"* (`21 53:09`). Rồi chúng hồi phục (`21 53:18`).

Ông so ngay với 1987 (`21 53:30`): *"Nó **không giống 1987**, khi thị trường xuống rồi ở lại dưới đó."*

Và đây là điểm Shiller nhấn (`21 53:35`):

> [!quote] 21 53:39
> *"Nếu bạn nhìn **giá đóng cửa** thì **gần như không có gì xảy ra**. Đó là một trục trặc rất ngắn, thứ
> có lẽ đã làm một số người mất **những khoản tiền khổng lồ** — vì nếu bạn đang giao dịch đúng khoảnh
> khắc đó, bạn gặp rắc rối."* (`21 53:39`)

📌 Câu đó đáng đọc hai lần. **Một cú sập không để lại dấu vết nào trên dữ liệu mà hầu hết mọi người
dùng.** Ai nghiên cứu thị trường bằng chuỗi giá đóng cửa — tức gần như toàn bộ tài chính thực nghiệm
trước 2010 — sẽ **không nhìn thấy ngày 6/5/2010 tồn tại**.

Diễn biến, theo chính báo cáo đó (`21 54:14`–`21 55:23`):

```
Trước 14:30   thị trường đã căng · chỉ số VIX vọt lên · có tin xấu · giảm 4 %
      ↓
Người giao dịch là NGƯỜI THẬT bắt đầu rút lui cho an toàn
      ↓
Nhưng MÁY TÍNH vẫn giao dịch
      ↓
Máy bắt đầu mua bán qua lại nhau tính bằng mili giây
      ↓
Khối lượng giao dịch vọt lên mức thiên văn -> làm người ta sợ thêm
      ↓
Các sở tạm dừng · người tạo lập tuyên bố rút khỏi thị trường
      ↓
Phần còn lại chủ yếu là máy giao dịch với máy -> THỊ TRƯỜNG CẠN THANH KHOẢN
```

Shiller thừa nhận giới hạn hiểu biết, và thừa nhận rất thẳng (`21 54:47`):

> [!quote]
> *"Tôi **không biết** các chương trình đó được lập trình để làm gì… **có lẽ chẳng ai biết toàn
> cảnh**."*

> [!warning]
> Báo cáo có khuyến nghị cách sửa, nhưng Shiller nêu rõ nó **không** khuyến nghị chấm dứt HFT
> (`21 55:26`) — dù *"rất nhiều người sẽ khuyến nghị làm thế"* (`21 55:36`).

Rồi ông đưa ra **đánh giá của mình**, và đây là chỗ thời gian đã phán xử. Ông cho rằng cơn giận của
công chúng nổ ra một phần vì ngày 6/5/2010 rơi đúng vào giai đoạn khủng hoảng tài chính nên *"người ta
tưởng tượng hai thứ đó liên quan với nhau"*, trong khi theo ông **chúng khá độc lập** (`21 55:39`,
`21 55:51`). Đánh giá của ông (`21 55:53`): hiện tượng ấy là do *"một dạng **bất thường**, hoặc do
**chưa quen** với giao dịch tần suất cao"* — và:

> [!quote] 21 56:05
> *"Nó là **một trục trặc, không phải một khiếm khuyết lớn** — nhưng nó dẫn tới rất nhiều phẫn nộ về
> giao dịch tần suất cao."* (`21 56:05`)

Ông dẫn người ở **Sàn Giao dịch Hàng hoá Chicago (CME)**, những người cho rằng nỗi lo của công chúng
về HFT là **đặt nhầm chỗ** (`21 56:15`). Lý lẽ họ đưa (`21 56:33`): nghề này *"về cơ bản vẫn giống hệt
100 năm trước, chỉ là bây giờ chúng tôi có **máy tính xách tay**"*. Và Shiller nối thêm phép so sánh
của chính mình (`21 56:43`): nó *"giống như khi bạn viết một bài luận"* — về bản chất vẫn là việc mà
người ta đã làm *"bằng bút lông và một tờ giấy 200 năm trước"*.

Và ông kết (`21 57:11`):

> [!quote] 21 57:14, 21 57:23
> ***"Chưa có ngày 6/5/2010 nào nữa kể từ đó. Đó chỉ là một sự bất thường, vì người ta chưa quen với
> loại sự kiện ấy… Tôi nghĩ rồi sẽ ổn thôi."*** (`21 57:14`, `21 57:23`)

Đó là câu sẽ được kiểm ở [§13.1](#131-chưa-có-ngày-652010-nào-nữa--câu-này-hỏng-sau-16-tháng).

### Một hệ quả ông nói đúng: địa lý quay trở lại

Phần này Shiller đoán rất chuẩn, và ông mở bằng đúng chữ (`21 57:28`): *"một thứ mà nó **đang làm** là
**thay đổi địa lý**."*

Thế kỷ 18, môi giới **phải sống ở London, Paris hay New York** để ở gần nơi giao dịch, *"vì họ không có
cách nào gọi điện thoại"* (`21 57:32`). Điện thoại ra đời và giải phóng họ (`21 57:44`): *"tôi không
phải sống ở New York nữa. Tôi sống đâu cũng được."*

**HFT đảo ngược điều đó** (`21 57:52`). Giao dịch nhanh tới mức (`21 58:04`):

> [!quote]
> *"nếu bạn định dựng một hoạt động giao dịch tần suất cao ở **St. Louis** và vận hành bằng đường dây
> tới New York, thì **thời gian điện chạy từ St. Louis tới New York là quá lâu**, và bạn sẽ **chậm
> chân** trong giao dịch."*

Nên bạn muốn ở *"**gần máy chủ của sở giao dịch nhất có thể về mặt vật lý**"* (`21 58:19`).

Và Shiller đóng lập luận bằng một đối lập rất gọn (`21 58:28`–`21 58:49`): các **sở giao dịch khu vực**
từng có ở mọi thành phố lớn của Mỹ, và chúng tồn tại vì **lý do xã hội** — *"người Chicago muốn nói
chuyện với một môi giới người Chicago; họ muốn tới được tận văn phòng ông ta và gặp mặt"*. Giờ xuất hiện
**một lý do điện tử** thay thế. Lý do cuối cùng thì không ai cãi được (`21 58:49`):

> [!quote] 21 58:55
> *"Vì vật lý lý thuyết cơ bản, bạn **không thể di chuyển bất cứ thứ gì nhanh hơn ánh sáng**. Chuyện
> này sẽ còn ở lại với chúng ta, giờ khi đã có giao dịch tính bằng **micro giây**."* (`21 58:55`)

📌 Nghe kỹ thì đây là một đảo chiều sâu hơn vẻ ngoài. Suốt hai trăm năm, công nghệ liên tục **xoá bỏ**
vai trò của khoảng cách. Đây là lần đầu tiên công nghệ **dựng khoảng cách trở lại** — và lần này nó
không dựng bằng tập quán xã hội có thể thay đổi, mà bằng **tốc độ ánh sáng**, thứ không thương lượng
được.

Lý do ông đưa ra là lý do vật lý thuần tuý: **không gì di chuyển nhanh hơn ánh sáng.** Các sở giao
dịch khu vực ngày xưa tồn tại vì **lý do xã hội** — người Chicago muốn gặp môi giới người Chicago. Giờ
xuất hiện một **lý do điện tử** thay thế.

---

## 12. Nghề tạo lập: lựa chọn ngược và bài toán phá sản

Chương cuối là chương hay nhất, và Shiller mở đầu bằng cách gọi tên nó: **những nỗi bực dọc của nghề
tạo lập** (`21 63:56`) — đặt song song với những nỗi bực dọc của nghề ngân hàng đầu tư ở
[bài 5](bai_05_ngan_hang_dau_tu.md).

**Rủi ro cốt lõi** (`21 61:35`): bạn đặt lệnh lên sổ và để đó, nên bạn **có thể bị móc túi bởi người
có thông tin tốt hơn**.

Ông giải thích bằng hình ảnh người buôn đồ cổ (`21 61:49`), và hình ảnh này chính xác đến mức đáng
giữ nguyên: thứ người buôn đồ cổ **ghét nhất** là dân buôn chuyên nghiệp vào cửa hàng mình. Người đó
sẽ lục hết mọi thứ để tìm món **bị định giá sai** — chẳng hạn một cái tủ thế kỷ 18 của một thợ nổi
tiếng — rồi mua đúng theo giá bạn đang niêm yết. Bạn **bị moi mất món ngon và còn lại đồ tầm thường**.

Rồi ông đóng lập luận theo hướng mà nhiều người không nghĩ tới (`21 62:54`): bạn **không thể** chống
lại bằng cách thông minh hơn. Không thể là người hiểu biết nhất — có quá nhiều loại đồ cổ và quá nhiều
thông tin nội bộ. Nên chỉ còn **một cách duy nhất** (`21 63:42`):

> [!note]
> **Đặt chênh lệch mua-bán đủ rộng để bạn bị moi mà vẫn có lãi.**

Với cổ phiếu cũng vậy. Bạn niêm yết giá lên màn hình thì bạn là **con vịt ngồi im** (`21 63:14`): sẽ
có tin tốt hoặc tin xấu, và **ai đó sẽ nghe được trước bạn**; khi lệnh của bạn bị khớp thì đó là lúc
bất lợi cho bạn.

> [!note] Chênh lệch mua-bán phải rộng bao nhiêu
>
> Shiller nói "đủ rộng" bằng lời. [Mục 4 của chương trình](#15-chương-trình) tính ra con số. Cổ phiếu
> đang giá 25,00; sắp có tin đưa giá về 26,00 hoặc 24,00; một tỷ lệ người giao dịch **biết trước tin
> đó**, và người tạo lập **không phân biệt được ai là ai**:
>
> | Tỷ lệ người biết trước | Chênh lệch hoà vốn | Trên giá cổ phiếu |
> | ---------------------: | -----------------: | ----------------: |
> |             **0,00 %** |           **0 xu** |       **0,000 %** |
> |                 1,00 % |               2 xu |           0,080 % |
> |                 5,00 % |              11 xu |           0,440 % |
> |                10,00 % |              22 xu |           0,880 % |
> |                30,00 % |              86 xu |           3,440 % |
>
> Hàng đầu tiên là chìa khoá: nếu **không ai** biết trước tin, chênh lệch hoà vốn **bằng 0**.
>
> > Chênh lệch mua-bán **không phải phí dịch vụ**, cũng **không phải lợi nhuận độc quyền**. Nó là **giá
> > của việc không biết ai đang đứng bên kia.**
>
> Điều này giải thích một hiện tượng mà lời giảng không nhắc: vì sao **cổ phiếu ít người theo dõi có
> chênh lệch rộng hơn cổ phiếu lớn**. Không phải vì nó rủi ro hơn về mặt kinh doanh, mà vì **tỷ lệ người
> biết trước trong số người giao dịch nó cao hơn**.

### Bài toán phá sản của người tạo lập

Shiller đóng buổi giảng bằng toán (`21 64:43`) — ông nói ông biết không nên kết thúc một bài giảng
bằng toán, nhưng vẫn làm.

Vấn đề (`21 64:15`, `21 64:33`): bạn có thể làm nghề tạo lập **20 năm**, thấy tài sản mình lớn dần,
nhưng chỉ cần **vài nước đi sai** là bị xoá sổ. *Hai mươi năm làm việc, và bạn phá sản.*

Ông gọi đây là **bài toán phá sản của con bạc**, và cũng là **bài toán phá sản của người tạo lập**
(`21 64:47`). Với vốn ban đầu $S$ và xác suất thắng mỗi ván là $p$:

$$
P(\text{phá sản cuối cùng}) =
\begin{cases}
\left(\dfrac{1-p}{p}\right)^{S} & p > 1/2 \\[2mm]
1 & p \le 1/2
\end{cases}
$$

[Mục 5 của chương trình](#15-chương-trình) tính bảng đầy đủ:

|         $p$ |     $S{=}1$ |     $S{=}5$ |    $S{=}20$ |    $S{=}50$ |   $S{=}100$ |
| ----------: | ----------: | ----------: | ----------: | ----------: | ----------: |
| **50,00 %** | **1,00000** | **1,00000** | **1,00000** | **1,00000** | **1,00000** |
|     51,00 % |     0,96078 |     0,81871 |     0,44928 |     0,13530 |     0,01831 |
|     55,00 % |     0,81818 |     0,36665 |     0,01807 |     0,00004 |     0,00000 |
|     60,00 % |     0,66667 |     0,13169 |     0,00030 |     0,00000 |     0,00000 |

Hai điều đọc ra:

**Một — hàng đầu tiên.** Ở $p = 50\%$, phá sản là **chắc chắn**, dù vốn bao nhiêu. Một người tạo lập
chỉ hoà vốn trên từng lệnh thì **chắc chắn chết**. Đó chính là lý do chênh lệch mua-bán ở bảng trên
phải lớn hơn 0 thật sự — hai mục này là **một lập luận duy nhất**, không phải hai chủ đề rời.

**Hai — Shiller nhấn mạnh** (`21 68:00`): xác suất đó **không bao giờ bằng không**. Và ông gọi đó là
**sự trớ trêu của nghề tạo lập** (`21 68:02`): *bạn ngủ không ngon, vì bạn không bao giờ biết chắc nó
sẽ không sụp đổ* (`21 68:11`).

Rồi ông thêm ràng buộc thứ hai làm mọi thứ chặt hơn (`21 68:18`–`68:25`): bạn **không thể** đặt chênh
lệch tuỳ ý cao, vì như thế sẽ **mất hết khách vào tay người khác**. Người tạo lập bị ép giữa hai phía:

```
đặt HẸP   ->  p về gần 1/2  ->  phá sản gần như chắc chắn
đặt RỘNG  ->  không ai giao dịch với bạn  ->  không có việc để làm
```

📌 Và Shiller kết bằng một nhận xét về con người, nối lại với [bài 12](bai_12_tai_chinh_hanh_vi.md):
bạn phải là **kiểu người chơi trò chơi, người không bị bận tâm bởi khả năng phá sản cuối cùng**, mới
làm được nghề này.

---

## 13. Đối chiếu 2026

### 13.1 "Chưa có ngày 6/5/2010 nào nữa" — câu này hỏng sau 16 tháng

Shiller nói câu đó ngày 13/4/2011, và nó là dự đoán rõ ràng nhất của cả buổi giảng.

| Ngày          | Sự kiện                                                                                                                                                                                                                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1/8/2012**  | **Knight Capital** — một trong những người tạo lập lớn nhất Mỹ. Lỗi triển khai phần mềm kích hoạt đoạn mã cũ đã nằm im nhiều năm. Trong **45 phút**, hệ thống gửi hơn **4 triệu lệnh** trong khi chỉ cần khớp **212 lệnh** của khách, giao dịch hơn **397 triệu cổ phiếu**. Thiệt hại **440–460 triệu USD** — gần như xoá sổ công ty |
| 23/4/2013     | Tài khoản Twitter của hãng tin AP bị chiếm quyền → thị trường sụt trong chốc lát                                                                                                                                                                                                                                                     |
| 15/1/2015     | Franc Thuỵ Sĩ sập chớp nhoáng khi Ngân hàng Trung ương bỏ neo tỷ giá                                                                                                                                                                                                                                                                 |
| **24/8/2015** | Dow rơi khoảng **1.100 điểm trong 5 phút đầu phiên**. Nhiều quỹ ETF **tách rời khỏi giá trị tài sản cơ sở**. Các biện pháp bảo vệ dựng sau 2010 **tỏ ra không đủ**                                                                                                                                                                   |
| 7/10/2016     | Bảng Anh sập chớp nhoáng                                                                                                                                                                                                                                                                                                             |
| **5/2/2018**  | *"Volmageddon"* — S&P 500 giảm 4,10 %, VIX vọt lên 37, quỹ **XIV bị chấm dứt hoạt động** sau cú giảm 97 %                                                                                                                                                                                                                            |
| 2/1/2019      | Yên Nhật sập chớp nhoáng                                                                                                                                                                                                                                                                                                             |
| 2/5/2022      | Thị trường châu Âu sập chớp nhoáng                                                                                                                                                                                                                                                                                                   |

**Mười sáu tháng** sau khi Shiller nói *"rồi sẽ ổn thôi"*, Knight Capital mất gần nửa tỷ đô trong 45
phút vì đúng loại nguyên nhân ông vừa gạt đi.

> [!warning]
> Nhưng phải công bằng với ông ở hai điểm. **Thứ nhất**, lập luận của ông không phải "sẽ không có sự
> cố nào nữa" mà là "đây là trục trặc, không phải khiếm khuyết cấu trúc, và ta sẽ học được" — và điều đó
> **đúng một phần**: [§13.2](#132-cầu-dao-mà-shiller-mô-tả-đã-bị-thay-thế-hoàn-toàn) cho thấy hệ thống
> đã học thật. **Thứ hai**, ông nói câu đó **có kèm điều kiện**: *"chúng ta phải cẩn thận một chút, mọi
> thứ có thể xảy ra với tốc độ ánh sáng."*

Lỗi nằm ở chỗ ông rút ra kết luận **"chỉ là một sự bất thường"** từ một mẫu quan sát **11 tháng**. Đó
là đúng loại sai lầm mà chính ông dạy ở [bài 12](bai_12_tai_chinh_hanh_vi.md): khoảng tin cậy quá hẹp,
rút kết luận từ quá ít dữ liệu.

### 13.2 Cầu dao mà Shiller mô tả đã bị thay thế hoàn toàn

Hệ cầu dao ông mô tả **không còn tồn tại**. Sau ngày 6/5/2010, Uỷ ban Chứng khoán phê duyệt hai đề
xuất vào **31/5/2012**, chạy thử từ **4/2/2013** và triển khai đầy đủ từ **8/4/2013**.

**Thay đổi thứ nhất — ngưỡng dừng toàn thị trường được hạ xuống:**

|  Cấp | Bản Shiller mô tả | Bản hiện hành |
| ---: | ----------------: | ------------: |
|    1 |              10 % |       **7 %** |
|    2 |              20 % |      **13 %** |
|    3 |              30 % |      **20 %** |

**Thay đổi thứ hai quan trọng hơn nhiều** — cơ chế **Limit Up-Limit Down (LULD)** thay thế cầu dao
từng cổ phiếu:

|               | Bản cũ (2010–2013)                  | **LULD** (từ 2013)                          |
| ------------- | ----------------------------------- | ------------------------------------------- |
| Kích hoạt khi | giá đổi > 10 % trong 5 phút trước   | giá chạm biên độ **và ở đó 15 giây**        |
| Biên độ       | —                                   | **5 %** (cổ phiếu lớn) · **10 %** (còn lại) |
| Hành động     | **DỪNG** giao dịch 5 phút           | **CẤM khớp** ngoài biên độ                  |
| Lệnh sai giá  | dừng thị trường **sau khi** đã khớp | **bị chặn trước khi** khớp                  |

> [!note]
> Khác biệt cơ bản: bản cũ **chữa cháy**, LULD **chống cháy**.

Bản cũ có một vấn đề thực tế mà chính cơ quan quản lý ghi nhận: nó bị kích hoạt bởi **chính các lệnh
sai giá**, gây ra một mớ hỗn độn hành chính vì hàng loạt cổ phiếu bị dừng và nhiều giao dịch sai phải
huỷ. LULD **không cho lệnh sai khớp ngay từ đầu**, nên không có gì phải huỷ.

📌 Và điều này nối thẳng vào §5: LULD chặn ở mức **95** trong khi cầu dao cũ chỉ dừng ở **90** — **sớm
hơn 5 đô mỗi cổ phiếu**. Đó chính là khoản mà người đặt lệnh dừng lỗ trước đây phải trả, và nay không
còn phải trả nữa. Một lệnh dừng lỗ ngày nay **an toàn hơn nhiều** so với năm 2010 — không phải nhờ bản
thân loại lệnh đó tốt lên, mà nhờ **hạ tầng xung quanh nó**.

### 13.3 Trả tiền cho luồng lệnh — từ "vấn đề khó" thành mô hình kinh doanh

Shiller nêu PFOF năm 2011 như một vấn đề khó rồi đi tiếp. Mười lăm năm sau, ba khu vực pháp lý lớn đã
đi ba hướng khác nhau:

|            | **Liên minh châu Âu**                               | **Anh**                 | **Mỹ**                         |
| ---------- | --------------------------------------------------- | ----------------------- | ------------------------------ |
| Trạng thái | **CẤM HOÀN TOÀN**                                   | **cấm từ 2012**         | **vẫn hợp pháp**               |
| Cơ sở      | Điều 39a MiFIR                                      | FCA FG12/13, COBS 11.2A | Quy tắc 606/607, FINRA 5310    |
| Mốc        | hiệu lực 28/3/2024; Đức được miễn tới **30/6/2026** |                         | dựa trên **công bố thông tin** |

Từ **30/6/2026**, khi ngoại lệ chuyển tiếp của Đức hết hạn, PFOF **bị cấm trên toàn Liên minh châu
Âu**. Mọi công ty môi giới chịu quản lý của EU nay phải sống bằng chênh lệch giá, hoa hồng, phí thuê
bao hoặc sở giao dịch của chính mình.

Mỹ đi hướng ngược lại: Uỷ ban Chứng khoán **tuyên bố sẽ không cấm hẳn**, mà theo đuổi công bố thông
tin. Tháng 12/2022 các uỷ viên bỏ phiếu 3–2 đề xuất một bộ quy tắc mới, gồm cơ chế **đấu giá theo từng
lệnh**.

Và đây là chi tiết Shiller không thể lường: **PFOF đã trở thành nền tảng của giao dịch "miễn phí hoa
hồng"**. Tháng 12/2020, Uỷ ban Chứng khoán phạt **Robinhood 65 triệu USD** vì không công bố việc nhận
tiền từ luồng lệnh và không tuân thủ nghĩa vụ thực hiện lệnh tốt nhất.

[Mục 7 của chương trình](#15-chương-trình) tính xem ai thật sự trả tiền. Với 100 lệnh/năm, chênh lệch
mua-bán 1 xu, người bảo lãnh trả lại 30 % chênh lệch:

| Khối lượng mỗi lệnh | Hoa hồng/năm | Chi phí ẩn/năm | Cái nào rẻ hơn |
| ------------------: | -----------: | -------------: | -------------- |
|                  50 |       500,00 |          10,00 | PFOF           |
|                 500 |       500,00 |         100,00 | PFOF           |
|               2.000 |       500,00 |         400,00 | PFOF           |
|           **5.000** |       500,00 |   **1.000,00** | **hoa hồng**   |

**Điểm hoà vốn: khoảng 2.500 cổ phiếu mỗi lệnh.** Dưới mức đó, "miễn phí hoa hồng" rẻ thật. Trên mức
đó, nó đắt hơn cả mô hình tính phí — **và người trả không bao giờ nhìn thấy hoá đơn**.

📌 Nên câu trả lời cho *"ai được lợi từ PFOF"* không phải "nhà môi giới" hay "nhà đầu tư" mà là: **nhà
đầu tư lệnh nhỏ được lợi, nhà đầu tư lệnh lớn trả tiền.** Đó là một khoản trợ cấp chéo, và nó vô hình
theo thiết kế.

### 13.4 Ai gây ra ngày 6/5/2010 — câu trả lời phức tạp hơn ông tưởng

Shiller nói *"có lẽ chẳng ai biết toàn cảnh"*. Bốn năm sau có một cái tên.

Ngày **21/4/2015**, Bộ Tư pháp Mỹ truy tố **Navinder Singh Sarao** — biệt danh *"Chú chó vùng
Hounslow"* — với **22 tội danh**, giao dịch từ nhà bố mẹ ở tây London. Cáo buộc: **giả lệnh**
(*spoofing*) — đặt hàng nghìn lệnh hợp đồng tương lai E-mini S&P 500 với ý định huỷ trước khi khớp.

Ông nhận tội năm 2016, và ngày **28/1/2020** bị tuyên **thời gian đã tạm giam cộng một năm quản thúc
tại gia** — kèm 25,7 triệu USD dàn xếp với Uỷ ban Giao dịch Hàng hoá Tương lai.

Nhưng **mức độ đóng góp của ông ta vào cú sập thì đang tranh cãi thật sự**:

- Báo cáo năm 2014 của Uỷ ban Giao dịch Hàng hoá Tương lai kết luận Sarao **không gây ra** cú sập,
  nhưng **có góp phần**.
- Một nghiên cứu của **Aldrich và Laughlin (UC Santa Cruz)** cùng một đồng nghiệp ở Stanford xem xét
  các giao dịch trước ngày 6/5/2010 và kết luận **rất khó có khả năng** lệnh giả của ông ta gây ra cú
  sập; nó **có thể đã xảy ra ngay cả khi không có Sarao**. Họ chỉ sang **điểm yếu của hạ tầng báo cáo
  giao dịch**.
- Tại phiên dẫn độ, giáo sư **Lawrence Harris** (USC) làm chứng rằng nguyên nhân chính là **một lệnh
  bán khổng lồ từ một quỹ tương hỗ** cộng với thanh khoản suy giảm liên quan tới khủng hoảng nợ Hy
  Lạp.

📌 Bài học: **giả lệnh là hành vi có thật và đã bị kết án. Nhưng "tìm được thủ phạm" không đồng nghĩa
với "giải thích được sự kiện".** Câu nói thận trọng của Shiller — *có lẽ chẳng ai biết toàn cảnh* —
mười lăm năm sau vẫn còn đúng, chỉ là bây giờ ta biết rõ hơn **mình đang không biết cái gì**.

### 13.5 Cuộc đua sáp nhập kết thúc thế nào

Shiller kể câu chuyện đang dở dang. Nó kết thúc thế này:

| Mốc            | Sự kiện                                                                            |
| -------------- | ---------------------------------------------------------------------------------- |
| **1/2/2012**   | Uỷ ban châu Âu **CHẶN** thương vụ Deutsche Börse–NYSE Euronext trị giá 10,2 tỷ USD |
|                | Lý do: hai bên sẽ kiểm soát **hơn 90 %** giao dịch phái sinh châu Âu trên toàn cầu |
| 2011           | NASDAQ và ICE **rút** lời chào mua chung sau khi Bộ Tư pháp Mỹ nói sẽ chặn         |
| 12/2012        | ICE **quay lại một mình**                                                          |
| **13/11/2013** | **ICE hoàn tất mua NYSE Euronext**, khoảng **11 tỷ USD**                           |

Kết quả: **Sở Giao dịch New York, thành lập dưới gốc cây năm 1792, nay thuộc sở hữu của một công ty
giao dịch năng lượng thành lập năm 2000.**

📌 Shiller nói *"NYSE có thể sắp thành một công ty Đức"*. Ông **sai về người mua** nhưng **đúng về bản
chất**: sở giao dịch không còn là công trình công ích quốc gia. Và điều đáng chú ý — ông đã **nêu đúng
tên người thắng cuộc** (ICE) trong danh sách các bên chào mua, chỉ là qua một con đường khác và muộn
hơn hai năm.

### 13.6 Bảng tổng kết

| Nội dung buổi giảng                                 | Trạng thái 2026                                        |
| --------------------------------------------------- | ------------------------------------------------------ |
| Ranh giới môi giới / người tạo lập                  | ✅ **sống, và là phần bền nhất**                        |
| Chênh lệch mua-bán = giá của lựa chọn ngược         | ✅ sống                                                 |
| Bài toán phá sản của người tạo lập                  | ✅ sống — toán học không hết hạn                        |
| Sổ lệnh không phải ảnh chụp cung cầu                | ✅ sống                                                 |
| HFT kéo địa lý trở lại, giới hạn là tốc độ ánh sáng | ✅ **đúng, và ngày càng đúng hơn**                      |
| Sàn giao dịch vật lý đang chết dần                  | ✅ đúng                                                 |
| "Không thể mất quá 20 % nhờ lệnh dừng lỗ"           | ❌ **sai — §5**                                         |
| Cầu dao 10/20/30 % và cầu dao từng cổ phiếu         | ❌ đã thay bằng 7/13/20 % và LULD                       |
| "Chưa có ngày 6/5/2010 nào nữa, rồi sẽ ổn"          | ❌ **hỏng sau 16 tháng**                                |
| PFOF là "vấn đề khó"                                | ⚠️ thành mô hình kinh doanh chính ở Mỹ, **bị cấm ở EU** |
| NYSE "có thể thành công ty Đức"                     | ❌ thành công ty Mỹ (ICE), 2013                         |
| Phát minh đầu tiên của Edison là máy in giá         | ❌ là máy đếm phiếu bầu                                 |

Quy luật quen thuộc từ [bài 4](bai_04_chinh_sach_tien_te.md), [bài 5](bai_05_ngan_hang_dau_tu.md) và
[bài 9](bai_09_bat_dong_san.md) lặp lại: **cơ chế sống, tham số chết.** Nhưng bài này thêm một loại
thứ ba — **các dự đoán về công nghệ thì hỏng nhanh nhất**, và hỏng theo hướng lạc quan.

---

## 14. Góc Việt Nam

### 14.1 Sổ lệnh không có ai đứng sau

Shiller dành cả buổi để phân biệt hai vai trò. Thị trường cổ phiếu Việt Nam gần như **chỉ có vế thứ
nhất**.

HOSE vận hành **thuần khớp lệnh** (*order-driven*): giá do cung cầu trên sổ lệnh quyết định, khớp theo
thứ tự ưu tiên **giá — rồi thời gian**. Không có ai **bắt buộc phải yết giá hai chiều**.

Phiên giao dịch:

| Phiên                      | Giờ         |
| -------------------------- | ----------- |
| Khớp lệnh định kỳ mở cửa   | 09:00–09:15 |
| Khớp lệnh liên tục I       | 09:15–11:30 |
| Khớp lệnh liên tục II      | 13:00–14:30 |
| Khớp lệnh định kỳ đóng cửa | 14:30–14:45 |

Biên độ dao động **±7 %** so với giá tham chiếu, lô tối thiểu 100 cổ phiếu.

> [!warning] Một chỗ dễ nói sai, cần nói cho đúng.
> Không phải Việt Nam "chưa có" khái niệm tạo lập thị
> trường. Khung pháp lý về **thành viên tạo lập thị trường đã có** — Thông tư 120/2020/TT-BTC. Nhưng
> trên thực tế nó **chủ yếu áp dụng cho chứng chỉ quỹ ETF và chứng quyền có bảo đảm**, chưa triển khai
> rộng cho cổ phiếu niêm yết thông thường.

Hệ quả thực tế: **thanh khoản hoàn toàn phụ thuộc vào việc có nhà đầu tư khác tình cờ muốn giao dịch
ngược chiều hay không** — và đúng lúc thị trường căng thẳng thì họ biến mất.

Nhưng mô hình thuần khớp lệnh **cũng có lý do tồn tại**, và §12 cho thấy lý do đó: người tạo lập sống
bằng **chênh lệch mua-bán**, tức bằng tiền của người khác. Họ cũng có **đặc quyền về thông tin thị
trường**, và đó là một nguồn xung đột lợi ích thật. Bỏ họ đi thì bỏ luôn khoản chênh lệch đó.

> [!quote]
> Đây là một **đánh đổi**, không phải một thiếu sót. Câu hỏi đúng không phải "Việt Nam có nên có nhà
> tạo lập không" mà là "**thanh khoản trong khủng hoảng đáng giá bao nhiêu, so với khoản chênh lệch
> phải trả mỗi ngày**".

### 14.2 Nhưng còn một thứ thiếu, và thứ này thì không phải đánh đổi

Nhớ lại tên buổi giảng (`21 00:02`): **sở giao dịch VÀ TRUNG TÂM THANH TOÁN BÙ TRỪ**.

Việt Nam có **cơ chế đối tác bù trừ trung tâm (CCP)** cho thị trường **phái sinh** từ năm **2017**.
Thị trường **cơ sở thì chưa có**.

Theo Ngân hàng Thế giới, **80 % hệ thống thanh toán trên toàn cầu đã áp dụng CCP**.

Vì sao nó quan trọng: **không có CCP thì mỗi bên giao dịch chịu rủi ro bên kia không thanh toán.** Có
CCP thì trung tâm đứng ra làm đối tác của **cả hai** bên — bạn không cần biết ai đứng bên kia, vì bạn
không giao dịch với họ nữa, bạn giao dịch với trung tâm. Đó chính là lý do Shiller ghép hai chữ vào
cùng một tiêu đề.

**Lộ trình đã công bố:**

| Mốc                                      | Nội dung                                                    |
| ---------------------------------------- | ----------------------------------------------------------- |
| **Luật 56/2024/QH15**                    | cho phép VSDC thành lập công ty con                         |
| **Nghị định 245/2025/NĐ-CP** (11/9/2025) | cơ sở pháp lý cho cơ chế CCP                                |
| Quý III/2025                             | bắt đầu hoàn thiện khung, chuẩn bị lập công ty con của VSDC |
| 2026                                     | cấp giấy chứng nhận thành viên bù trừ, đào tạo, chạy thử    |
| **Quý I/2027**                           | mục tiêu **vận hành CCP cho thị trường cơ sở**              |

### 14.3 Hệ thống KRX và việc nâng hạng

Hai sự kiện lớn khép lại phần này, và chúng nối thẳng vào §8 — nơi Shiller kể chuyện các sở giao dịch
cũ bị công nghệ điện tử làm đảo lộn.

**Hệ thống KRX vận hành từ 5/5/2025**, xây cùng Sở Giao dịch Chứng khoán Hàn Quốc, thay hạ tầng cũ. Nó
mở đường cho những thứ Việt Nam chưa có: **CCP**, thanh toán **giao chứng khoán đồng thời với tiền
(DvP)**, giao dịch trong ngày (T+0), bán khống.

📌 Đọc danh sách đó cạnh bài giảng thì thấy: **những thứ Shiller coi là mặc định năm 2011 — bán khống
có lệnh dừng mua (§4), giao dịch trong ngày, người tạo lập — thì Việt Nam vẫn đang xây.** Đây không
phải chuyện tụt hậu; đây là chuyện **thứ tự xây dựng hạ tầng**, và Việt Nam đang xây phần móng sau khi
đã có nhà.

**Nâng hạng FTSE Russell.** Ngày **7/10/2025**, FTSE Russell công bố Việt Nam sẽ được tái phân hạng từ
**Thị trường Cận biên** lên **Thị trường Mới nổi Thứ cấp**, sau gần bảy năm cải cách kể từ khi vào
danh sách theo dõi năm 2018. Tháng 4/2026, FTSE **xác nhận** sau kỳ đánh giá giữa kỳ. Hiệu lực từ
**thứ Hai 21/9/2026**, đưa vào chỉ số theo bốn giai đoạn với hệ số 10 %, 30 %, 65 % rồi hoàn tất.

Hai cải cách được FTSE ghi nhận cụ thể:

- **Gỡ yêu cầu ký quỹ trước giao dịch** cho nhà đầu tư tổ chức nước ngoài (mô hình *non-prefunding*)
- **Thông tư 08/2026/TT-BTC** thiết lập khuôn khổ tiếp cận qua công ty chứng khoán toàn cầu

Quy mô hiện tại: vốn hoá khoảng **410 tỷ USD**, giá trị giao dịch bình quân trên HOSE khoảng **1,2 tỷ
USD/phiên** tính tới giữa tháng 5/2026 — thanh khoản dẫn đầu Đông Nam Á theo trung bình 10 phiên gần
nhất.

FTSE cũng nêu rõ những việc còn phải làm: cải thiện quy trình đăng ký tài khoản cho nhà đầu tư nước
ngoài, tăng khả năng tiếp cận thông tin tiếng Anh của doanh nghiệp niêm yết, và **bảo đảm hệ thống KRX
vận hành thông suốt**.

### 14.4 Ba việc dùng được ngay

> [!example]
> Từ bài này, ba thứ một nhà đầu tư Việt Nam kiểm tra được:

1. **Đừng dùng lệnh thị trường cho cổ phiếu thanh khoản thấp.** §7 cho thấy sổ lệnh mỏng hơn cảm giác
   rất nhiều. Với cổ phiếu ít giao dịch, hãy xem độ sâu sổ lệnh **trước khi** đặt lệnh, và dùng lệnh
   giới hạn.
2. **Hiểu đúng lệnh dừng lỗ.** §5: nó bảo đảm bán, không bảo đảm giá. Việt Nam có biên độ ±7 % nên rủi
   ro ít cực đoan hơn Mỹ năm 2010, nhưng nguyên tắc không đổi.
3. **Chênh lệch mua-bán rộng là tín hiệu, không phải phiền toái.** §12: nó đo **tỷ lệ người biết trước
   tin** trong số người đang giao dịch mã đó. Chênh lệch rộng bất thường ở một cổ phiếu là lời cảnh
   báo rằng có người biết thứ bạn không biết.

---

## 15. Chương trình

📂 **[thuc_hanh/bai-06-so-giao-dich.py](../thuc_hanh/bai-06-so-giao-dich.py)** — 588 dòng, 8 mục.

> [!note]
> ⚙️ **Chạy:** cần **Python 3.10+**. Không cần cài gói nào, không gọi mạng, không đọc file ngoài.
> ```bash
> python3 bai-06-so-giao-dich.py
> ```

Chương trình dựng lại **chính sổ lệnh Shiller chiếu lên màn hình** rồi cho các loại lệnh chạy qua nó.

Trong quá trình viết, `assert` bắt được **hai lỗi của tác giả bài này**. Lần đầu: bài này khẳng định lệnh
10.000 cổ phiếu phải bị trượt giá — sai, vì hai mức chào bán đầu tiên **cùng ở giá 25,24** từ hai sàn
khác nhau, nên độ sâu ở đỉnh là 10.600 chứ không phải 2.400. Lần thứ hai: khẳng định trượt giá ở
12.100 cổ phiếu phải lớn hơn 0 — đúng về tiền (15 USD) nhưng **sai khi làm tròn về điểm cơ bản**, nên
phép khẳng định phải chuyển sang đo bằng tiền.

Cả hai lần, thứ sai là **phép khẳng định**, không phải mô hình — và cả hai đều dẫn tới một chi tiết
đáng viết vào bài.

Kết quả chạy thật:

```
BAI 6 - SO GIAO DICH, MOI GIOI, DEALER VA GIAO DICH TAN SUAT CAO
Yale ECON 252 buoi 21 - Robert J. Shiller

==============================================================================
MUC 1. SO LENH GIOI HAN: vi sao hai duong cung cau KHONG cat nhau
==============================================================================
   MUA (bid)                        BAN (ask)
   KL       Gia      Noi            KL       Gia      Noi
------------------------------------------------------------------------------
      100    25.23   ARCX         2,400    25.24   NSDQ
    9,430    25.22   NSDQ         8,200    25.24   CINN
    2,800    25.21   BATS         1,500    25.25   ARCX
   14,200    25.20   EDGX         6,700    25.26   BATS
    5,600    25.19   ARCX        12,000    25.27   EDGX
   31,000    25.18   NSDQ        26,500    25.28   NSDQ

  Gia mua tot nhat 25.23 · gia ban tot nhat 25.24
  CHENH LECH MUA-BAN = 1 xu = 0.030 % gia

  Shiller `21 34:37`: hai duong nay KHONG CAT NHAU, va do khong phai
  chuyen la. Neu chung cat nhau thi lenh da khop va bien mat khoi man
  hinh ngay lap tuc. Cai ta nhin thay tren so lenh la phan CHUA khop.

  Do la mot dieu ngan gon ma sau: so lenh khong phai anh chup cung cau
  cua thi truong. No la anh chup phan cung cau ma thi truong CHUA
  tieu hoa duoc.

  DO SAU TICH LUY (thu ma Level I khong cho ban thay):

   Muc gia    KL mua tich luy      Muc gia    KL ban tich luy
------------------------------------------------------------------------------
    25.23              100       25.24            2,400
    25.22            9,530       25.24           10,600
    25.21           12,330       25.25           12,100
    25.20           26,530       25.26           18,800
    25.19           32,130       25.27           30,800
    25.18           63,130       25.28           57,300

  Shiller `21 34:59`: Level I chi cho ban HANG DAU TIEN. Level II cho
  ca so. Nhin bang tren se hieu vi sao ong noi 'gia se kho roi nhanh
  xuong duoi 25.22' - vi o do co mot nguoi mua lon dang doi.

==============================================================================
MUC 2. LENH THI TRUONG AN VAO SO LENH: cai gia cua su voi vang
==============================================================================
  Gia ban tot nhat tren man hinh: 25.24
  Do sau tai muc gia do: 10,600 co phieu.

  ⚠ De y: HAI lenh dau tien deu o 25.24, tu hai noi khac nhau
  (NSDQ va CINN). Shiller cung chi ra dieu nay o `21 33:21`: hai
  khach hang khac nhau, cung mot gia, van la hai lenh rieng. Nen do
  sau that o dinh so lenh la 10,600 chu khong phai 2,400.

   Khoi luong dat mua   Gia binh quan thuc   Truot gia   Chi phi truot
------------------------------------------------------------------------------
                100             25.2400     0.000 %         0.00 USD
             10,000             25.2400     0.000 %         0.00 USD
             12,100             25.2412     0.000 %        15.00 USD
             25,000             25.2534     0.050 %       335.00 USD
             57,300             25.2674     0.110 %     1,569.00 USD

  Moi lenh tu 10,600 co phieu tro xuong deu duoc dung gia
  niem yet - khong truot mot xu nao. Vuot qua nguong do thi bat dau
  phai tra them, va lenh 57,300 co phieu tra cao hon 0.11 %.

  De y hang 12.100: cot ty le hien 0,000 % nhung cot chi phi hien 15.00 USD.
  Truot gia that la nua diem co ban - qua nho de hien ra o ba chu so
  thap phan, nhung tien thi co that. Do la ly do bang nay co ca hai
  cot: ty le de so sanh, tien de biet minh mat gi.

  Day la ly do Shiller `21 29:08` nhac loi khuyen cua gioi tu van:
  'dung bao gio dat lenh thi truong'. Lenh thi truong khong noi gia,
  nen no chap nhan MOI muc gia con lai tren so.

  Va de y con so cuoi: an het ca sau muc ban tren man hinh chi can
  57,300 co phieu. So lenh mong hon rat nhieu so voi cam giac -
  va do la luc thi truong dang BINH THUONG. Muc 3 xem luc khong.

==============================================================================
MUC 3. LENH DUNG LO: vi sao no phan boi dung luc can nhat
==============================================================================
  Shiller `21 28:17`: gia dang 100, dat lenh dung lo o 80,
  'the la it nhat toi biet toi khong the mat qua 20 % khoan dau tu'.

  ⚠ CAU DO KHONG DUNG, va ly do nam ngay trong dinh nghia cua lenh:
  lenh dung lo khi bi kich hoat se tro thanh LENH THI TRUONG. No bao
  dam BAN, khong bao dam GIA. Muc 80 la muc KICH HOAT, khong phai muc
  ban. Muc ban la bat cu gia nao con tren so lenh luc do.

   Tinh huong                       Gia khop thuc   Mat that
------------------------------------------------------------------------------
   thi truong binh thuong                80.00     20.00 %
   mo cua gap gia                        72.00     28.00 %
   tin xau dot ngot                      61.00     39.00 %
   ngay 6/5/2010 - flash crash            0.01     99.99 %

  Hang cuoi khong phai gia thuyet. Ngay 6/5/2010, mot so co phieu
  giao dich xuong toi 1 xu roi bat lai trong vai phut. Ai dat lenh
  dung lo deu bi ban tai day, roi nhin gia hoi phuc ma khong con hang.

  Nghich ly cua lenh dung lo: no duoc thiet ke de bao ve ban khoi cu
  sap. Nhung dung trong cu sap la luc so lenh mong nhat, nen do cung
  la luc no thuc hien te nhat. No hoat dong tot nhat khi ban can no
  it nhat.

==============================================================================
MUC 4. CHENH LECH MUA-BAN: bai toan lua chon nguoc
==============================================================================
  Co phieu dang gia 25.00. Sap co tin: gia ve 26.00 hoac 24.00.
  Mot so nguoi giao dich BIET TRUOC tin do. So con lai thi khong.
  Nguoi tao lap khong phan biet duoc ai la ai.

   Ty le nguoi biet truoc   Chenh lech hoa von   Tren gia co phieu
------------------------------------------------------------------------------
                 0.00 %               0 xu            0.000 %
                 1.00 %               2 xu            0.080 %
                 5.00 %              11 xu            0.440 %
                10.00 %              22 xu            0.880 %
                20.00 %              50 xu            2.000 %
                30.00 %              86 xu            3.440 %

  Hang dau tien la chia khoa: neu KHONG AI biet truoc tin, chenh lech
  hoa von bang 0. Chenh lech mua-ban KHONG phai phi dich vu, cung
  khong phai loi nhuan doc quyen. No la GIA CUA VIEC KHONG BIET AI
  DANG DUNG BEN KIA.

  Shiller dung dung hinh anh nguoi buon do co `21 61:49`: ho ghet nhat
  la dan buon chuyen nghiep vao cua hang minh, vi nhung nguoi do se
  loc het mon dinh gia sai. Va ong ket dung: khong the khon hon tat ca
  moi nguoi duoc, nen chi con mot cach la DAT GIA DU RONG.

  Day cung la ly do co phieu it nguoi theo doi co chenh lech rong hon
  co phieu lon: khong phai vi no rui ro hon, ma vi ty le nguoi biet
  truoc trong so nguoi giao dich no CAO HON.

==============================================================================
MUC 5. PHA SAN CUA NGUOI TAO LAP: cong thuc Shiller viet len bang
==============================================================================
  P(pha san) = ((1-p)/p)^S   neu p > 1/2
  P(pha san) = 1             neu p <= 1/2
  voi p = xac suat thang moi lenh, S = so von ban dau (don vi cuoc)

   p        S=1        S=5        S=20       S=50       S=100
------------------------------------------------------------------------------
   50.00 %    1.00000    1.00000    1.00000    1.00000    1.00000
   51.00 %    0.96078    0.81871    0.44928    0.13530    0.01831
   55.00 %    0.81818    0.36665    0.01807    0.00004    0.00000
   60.00 %    0.66667    0.13169    0.00030    0.00000    0.00000
   70.00 %    0.42857    0.01446    0.00000    0.00000    0.00000

  HAI DIEU DOC RA TU BANG NAY:

   · Hang dau: p = 50 % thi pha san la CHAC CHAN, du von bao nhieu.
     Mot nguoi tao lap chi hoa von tren tung lenh thi CHAC CHAN chet.
     Do la ly do chenh lech mua-ban o muc 4 phai lon hon 0 that su.

   · Nhung cot cuoi: p = 60 %, von 100 don vi -> pha san 2.46e-18
     Rat nho, NHUNG KHONG BANG KHONG. Va vi nguoi tao lap dat cuoc
     lien tuc suot doi, 'cuoi cung' la mot khoang thoi gian dai.

  Shiller `21 68:11`: 'Day la su tro treu cua nghe tao lap. Ban ngu
  khong ngon, vi ban khong bao gio biet chac no se khong sup do.'

  Va co mot rang buoc thu hai lam moi thu chat hon: KHONG THE dat
  chenh lech tuy y cao, vi se mat het khach vao tay nguoi khac. Nguoi
  tao lap bi ep giua hai phia - dat hep thi p ve gan 1/2 va chac chet,
  dat rong thi khong co viec de lam.

==============================================================================
MUC 6. CAU DAO NGAT MACH: ban 1987 va ban sau 2013
==============================================================================
  Ngay 19/10/1987 chi so S&P 500 roi hon 20 % TRONG MOT NGAY.
  Uy ban Brady ket luan giao dich bang chuong trinh gop phan lon,
  va khuyen nghi lap cau dao ngat mach.

   Nguong dung thi truong toan phan
------------------------------------------------------------------------------
   Ban Shiller mo ta (2011)     Ban hien hanh (tu 8/4/2013)
   10 %                         7 %
   20 %                         13 %
   30 %                         20 %

  Nguong da duoc HA XUONG o ca ba cap. Nhung thay doi lon hon nam o
  cap tung co phieu, va do la thu Shiller khong the biet.

   Co che                     Ban cu (2010-2013)      Ban LULD (tu 2013)
------------------------------------------------------------------------------
   Kich hoat khi              roi/tang 10 % trong     gia cham bien do
                              5 phut truoc            va o do 15 giay
   Bien do co phieu lon       -                       5 %
   Bien do co phieu khac      -                       10 %
   Hanh dong                  DUNG giao dich 5 phut   CAM khop ngoai bien do
   Lenh sai gia                                        bi CHAN truoc khi khop

  Khac biet co ban: ban cu DUNG thi truong SAU khi lenh sai da khop.
  Ban LULD KHONG CHO lenh khop ngoai bien do ngay tu dau.
  Mot ben chua chay, mot ben chong chay.

   Gia co phieu roi dan tu 100. Ban nao chan duoc o dau?
------------------------------------------------------------------------------
   Gia tham chieu 5 phut truoc       100.00
   Bien duoi LULD (5 %)               95.00   -> khong cho khop duoi muc nay
   Nguong cau dao cu (10 %)           90.00   -> chi dung SAU khi da roi toi day

  LULD chan som hon 5.00 USD tren moi co phieu.
  Do dung la khoan ma nha dau tu dat lenh dung lo o muc 3 khong con
  phai tra nua - vi lenh cua ho khong the khop duoi bien LULD.

==============================================================================
MUC 7. TRA TIEN CHO LUONG LENH: ai tra cho 'mien phi hoa hong'
==============================================================================
  Nha dau tu ca nhan: 100 lenh/nam, 500 co phieu/lenh, gia 50 USD
  Chenh lech mua-ban 1 xu. Nguoi bao lanh tra lai 30 % chenh lech.

   Mo hinh                     Chi phi hien   Chi phi an   Tong/nam
------------------------------------------------------------------------------
   Hoa hong truyen thong          500.00         0.00     500.00 USD
   'Mien phi hoa hong' (PFOF)       0.00       100.00     100.00 USD

  Voi ho so giao dich NAY, PFOF re hon 400.00 USD/nam.

  Nhung con so tren phu thuoc manh vao QUY MO LENH. Chi phi an ty le
  voi so co phieu; hoa hong thi co dinh moi lenh:

   KL moi lenh   Hoa hong/nam   Chi phi an/nam   Cai nao re hon
------------------------------------------------------------------------------
            50       500.00          10.00   PFOF
           200       500.00          40.00   PFOF
           500       500.00         100.00   PFOF
         2,000       500.00         400.00   PFOF
         5,000       500.00       1,000.00   hoa hong

  DIEM HOA VON: khoang 2,500 co phieu moi lenh.
  Duoi muc do, 'mien phi hoa hong' re that. Tren muc do, no dat hon
  ca mo hinh tinh phi - va nguoi tra khong bao gio nhin thay hoa don.

  Do la dieu Shiller canh bao o `21 48:17`: nguoi moi gioi 'trong thuc
  te co the moc tui ban'. Ong khong the biet rang muoi nam sau, co che
  do se tro thanh nen tang cua toan bo nganh moi gioi ban le My.

==============================================================================
MUC 8. VIET NAM: so lenh khong co ai dung sau
==============================================================================
  Shiller danh ca buoi de phan biet hai vai tro (`21 06:22`):
     NGUOI MOI GIOI  - giao dich HO nguoi khac, an hoa hong
     NGUOI TAO LAP   - giao dich CHO CHINH MINH, an chenh lech

  Thi truong co phieu Viet Nam gan nhu chi co ve thu nhat.
  HOSE van hanh thuan khop lenh: gia do cung cau tren so lenh quyet
  dinh, khong co ai bat buoc phai yet gia hai chieu.

  Khung phap ly ve thanh vien tao lap thi truong DA CO - Thong tu
  120/2020/TT-BTC. Nhung tren thuc te no chu yeu ap dung cho chung chi
  quy ETF va chung quyen co bao dam, chua trien khai rong cho co phieu
  niem yet thong thuong.

  MO PHONG: mot nha dau tu can ban gap 60,000 co phieu.

   Cau truc thi truong        Do sau moi buoc   Gia truot
------------------------------------------------------------------------------
   Co nguoi tao lap yet gia          20,000      0.12 %
   Chi co lenh nha dau tu             5,000      0.48 %

  Cung mot lenh ban, gia truot gap 4.0 lan.

  ⚠ Day la mo hinh MINH HOA - hai con so do sau la do tac gia dat ra
  de thay huong, khong lay tu so lieu HOSE. Thu dang tin la CO CHE:
  khong co ai bat buoc yet gia hai chieu thi thanh khoan hoan toan
  phu thuoc vao viec co nha dau tu khac tinh co muon giao dich nguoc
  chieu hay khong - va dung luc thi truong cang thang thi ho bien mat.

  Doi lai, mo hinh thuan khop lenh cung co ly do ton tai. Nguoi tao
  lap co dac quyen ve thong tin, va do la mot nguon xung dot loi ich.
  Muc 4 cho thay ho SONG BANG chenh lech - tuc bang tien cua nguoi
  khac. Bo ho di thi bo luon khoan do. Day la mot DANH DOI, khong
  phai mot thieu sot.

  CON MOT THU NUA THIEU, VA THU NAY THI KHONG PHAI DANH DOI.
  Tieu de buoi giang cua Shiller la 'so giao dich VA TRUNG TAM THANH
  TOAN BU TRU' (`21 00:02`). Viet Nam co co che doi tac bu tru trung
  tam (CCP) cho thi truong PHAI SINH tu 2017, nhung thi truong co so
  thi CHUA CO.

   Theo Ngan hang The gioi: 80 % he thong thanh toan toan cau da
   ap dung CCP. Viet Nam dat muc tieu van hanh CCP cho co so vao
   quy 1/2027, tren co so Luat 56/2024/QH15 va Nghi dinh 245/2025.

  Vi sao CCP quan trong: khong co no thi moi ben giao dich chiu rui ro
  ben kia khong thanh toan. Co CCP thi trung tam dung ra lam doi tac
  cua CA HAI ben. Do chinh la ly do Shiller ghep 'so giao dich' va
  'trung tam thanh toan bu tru' vao cung mot tieu de.

==============================================================================
Tat ca assert deu qua. Chay lai cho ket qua giong het.
==============================================================================
```

> [!example] Tự thử
>
> 1. **Mục 1** — thêm một lệnh mua 50.000 cổ phiếu ở giá 25,23 vào `BEN_MUA`. Chênh lệch mua-bán có đổi
>    không? Độ sâu có đổi không? Điều đó nói gì về việc **chênh lệch giá là thước đo không đầy đủ**?
> 2. **Mục 2** — xoá lệnh 8.200 ở 25,24 khỏi `BEN_BAN`. Lệnh 10.000 cổ phiếu giờ trượt bao nhiêu?
> 3. **Mục 3** — nếu biên độ ±7 % của Việt Nam được áp vào bảng này, hàng nào biến mất?
> 4. **Mục 4** — tìm tỷ lệ người biết trước khiến chênh lệch hoà vốn vượt 1 % giá cổ phiếu. Con số đó có
>    thực tế không, và loại cổ phiếu nào rơi vào vùng đó?
> 5. **Mục 5** — với `p = 52 %`, cần bao nhiêu vốn để xác suất phá sản xuống dưới 1 %? So với `p = 60 %`.
> 6. **Mục 5** — vì sao tăng $p$ hiệu quả hơn tăng $S$? Trả lời bằng dạng của công thức.
> 7. **Mục 7** — đổi `CAI_THIEN_GIA_BP` thành `5_000` (người bảo lãnh trả lại **toàn bộ** nửa chênh
>    lệch). Chi phí ẩn về đâu, và mô hình PFOF còn lãi không?
> 8. **Mục 8** — đổi `DO_SAU_KHONG_TAO_LAP` thành `15_000`. Khoảng cách giữa hai cấu trúc thị trường thu
>    hẹp bao nhiêu? Điều đó nói gì về vai trò của **số lượng nhà đầu tư** so với **người tạo lập**?

---

## 16. Từ điển thuật ngữ

| Tiếng Việt                      | Tiếng Anh                 | Nghĩa                                                                  |
| ------------------------------- | ------------------------- | ---------------------------------------------------------------------- |
| Môi giới                        | broker                    | giao dịch **hộ** người khác, ăn **hoa hồng**, là **đại lý**            |
| Người tạo lập / dealer          | dealer                    | giao dịch **cho mình**, ăn **chênh lệch**, là **bên chính**            |
| Thị trường khớp lệnh            | order-driven market       | giá do sổ lệnh quyết định — HOSE, NYSE                                 |
| Thị trường khớp giá             | quote-driven market       | giao dịch với người tạo lập — NASDAQ                                   |
| Đấu giá hai chiều liên tục      | continuous double auction | cơ chế của NYSE                                                        |
| Thị trường phi tập trung        | OTC                       | giao dịch ngoài sở giao dịch                                           |
| Điều kiện niêm yết              | listing requirements      | chuẩn để được giao dịch trên sở — thứ đẻ ra NASDAQ                     |
| Lệnh thị trường                 | market order              | chỉ nói **số lượng** — chấp nhận mọi giá                               |
| Lệnh giới hạn                   | limit order               | nói cả **số lượng và giá**                                             |
| Lệnh dừng lỗ                    | stop-loss order           | kích hoạt khi giá **giảm** tới mức đặt, rồi thành **lệnh thị trường**  |
| Lệnh dừng-giới hạn              | stop-limit order          | kích hoạt rồi thành **lệnh giới hạn** — bảo đảm giá, không bảo đảm bán |
| Sổ lệnh giới hạn                | limit order book          | tập hợp các lệnh **chưa khớp**                                         |
| Độ sâu sổ lệnh                  | market depth              | khối lượng có sẵn ở mỗi mức giá                                        |
| Chênh lệch mua-bán              | bid-ask spread            | **giá của việc không biết ai đứng bên kia**                            |
| Trượt giá                       | slippage                  | chênh giữa giá niêm yết và giá khớp bình quân                          |
| Lựa chọn ngược                  | adverse selection         | bị "moi" bởi người có thông tin tốt hơn                                |
| Phá sản của con bạc             | gambler's ruin            | $((1-p)/p)^S$ nếu $p > 1/2$; bằng 1 nếu $p \le 1/2$                    |
| Giao dịch tần suất cao          | HFT                       | giao dịch bằng máy tính ở thang mili giây                              |
| Mạng truyền thông điện tử       | ECN                       | tiền thân sở giao dịch điện tử — Archipelago, Island                   |
| Cầu dao ngắt mạch               | circuit breaker           | dừng thị trường khi giá rơi mạnh — nay là 7/13/20 %                    |
| Biên độ trên-dưới               | Limit Up-Limit Down       | **cấm khớp** ngoài biên độ, thay cầu dao từng cổ phiếu                 |
| Bảo hiểm danh mục               | portfolio insurance       | chiến lược bán tự động — thủ phạm chính năm 1987                       |
| Trả tiền cho luồng lệnh         | payment for order flow    | trả phí để nhận lệnh bán lẻ — **cấm ở EU từ 30/6/2026**                |
| Hệ thống Thị trường Quốc gia    | National Market System    | Mỹ 1975 — nghĩa vụ lấy **giá tốt nhất**                                |
| Giả lệnh                        | spoofing                  | đặt lệnh rồi huỷ để đánh lừa — tội của Sarao                           |
| Đối tác bù trừ trung tâm        | CCP                       | đứng làm đối tác của **cả hai** bên — Việt Nam nhắm quý I/2027         |
| Giao chứng khoán đồng thời tiền | DvP                       | thanh toán song trùng                                                  |

---

## 17. Câu hỏi tự kiểm tra

1. Phân biệt **môi giới** và **người tạo lập** theo bốn tiêu chí. Vì sao ranh giới này quyết định toàn
   bộ cấu trúc phí của một thị trường?
2. Vì sao gần như không tồn tại "dealer bất động sản"? Shiller đưa hai giả thuyết — giả thuyết nào
   khớp với bài toán phá sản ở §12, và vì sao?
3. Sổ lệnh **không phải** ảnh chụp cung cầu của thị trường. Vậy nó là ảnh chụp của cái gì?
4. Câu *"tôi không thể mất quá 20 % nhờ lệnh dừng lỗ"* sai ở đâu? Trả lời bằng định nghĩa của loại
   lệnh, không bằng ví dụ.
5. Không loại lệnh nào bảo đảm **cả** việc bán được **và** giá bán. Vì sao? Nêu đánh đổi giữa lệnh
   dừng lỗ và lệnh dừng-giới hạn.
6. Trong sổ lệnh ở §6, độ sâu ở đỉnh là 10.600 chứ không phải 2.400. Chi tiết đó thay đổi điều gì với
   người sắp đặt một lệnh 10.000 cổ phiếu?
7. Ăn hết cả sáu mức chào bán chỉ cần 57.300 cổ phiếu — khi thị trường **bình thường**. Dùng con số
   đó để giải thích vì sao ngày 6/5/2010 có cổ phiếu rơi xuống 1 xu.
8. **Bảo hiểm danh mục** năm 1987 và **lệnh dừng lỗ** cá nhân có cùng cấu trúc. Nêu cấu trúc đó bằng
   một câu, và giải thích vì sao nó tự khuếch đại.
9. Chênh lệch mua-bán hoà vốn bằng **0** khi không ai biết trước tin. Vì sao đó là kết quả quan trọng
   nhất của mục 4 chương trình?
10. Vì sao cổ phiếu ít người theo dõi có chênh lệch rộng hơn? Trả lời **không** dùng chữ "rủi ro".
11. Ở $p = 50\%$, phá sản là chắc chắn **dù vốn bao nhiêu**. Vì sao kết quả này khiến §12 và mục 4 trở
    thành **một lập luận duy nhất** chứ không phải hai chủ đề?
12. Người tạo lập bị ép giữa hai phía. Nêu cả hai, và nói vì sao **không có** mức chênh lệch nào an
    toàn tuyệt đối.
13. Shiller nói *"chưa có ngày 6/5/2010 nào nữa"* dựa trên **11 tháng** quan sát. Lỗi phương pháp ở
    đây là gì, và nó trùng với thiên lệch nào ở [bài 12](bai_12_tai_chinh_hanh_vi.md)?
14. LULD khác cầu dao cũ ở điểm căn bản nào? Vì sao khác biệt đó làm lệnh dừng lỗ **an toàn hơn** mà
    không cần sửa gì ở bản thân loại lệnh?
15. PFOF rẻ hơn với lệnh nhỏ, đắt hơn với lệnh lớn. Ai đang trợ cấp cho ai, và vì sao khoản trợ cấp đó
    vô hình?
16. Sarao bị kết án vì giả lệnh, nhưng các nghiên cứu cho rằng ông ta **không gây ra** cú sập. Vì sao
    "tìm được thủ phạm" và "giải thích được sự kiện" là hai việc khác nhau?
17. Việt Nam **có** khung pháp lý về tạo lập thị trường nhưng chưa vận hành cho cổ phiếu thường. Nêu
    hai mặt của đánh đổi này.
18. Vì sao thiếu **CCP** khác về bản chất với thiếu **người tạo lập** — một bên là đánh đổi, một bên
    thì không?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  SỞ GIAO DỊCH, MÔI GIỚI, DEALER VÀ HFT                                       ║
║  Yale ECON 252, buổi 21 (Shiller, 13/4/2011)                                 ║
║  Buổi vi cấu trúc thị trường DUY NHẤT của cả khoá.                           ║
║  Tên buổi: "sở giao dịch VÀ TRUNG TÂM THANH TOÁN BÙ TRỪ"                     ║
║  — giữ chữ thứ hai lại: Việt Nam còn thiếu nó.                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  RANH GIỚI NỀN TẢNG                                                          ║
║    MÔI GIỚI : giao dịch HỘ người khác · đại lý · ăn HOA HỒNG                 ║
║               · không nắm hàng, không chịu rủi ro giá                        ║
║    DEALER   : giao dịch CHO MÌNH · bên chính · ăn CHÊNH LỆCH                 ║
║               · NẮM hàng, chịu rủi ro giá                                    ║
║    Bán nhà -> môi giới. Đồ cổ -> dealer. Vì sao?                             ║
║    Shiller KHÔNG trả lời được, và ông nói thẳng là không.                    ║
║    NYSE = thị trường môi giới (đấu giá hai chiều liên tục).                  ║
║    NASDAQ = thị trường dealer.                                               ║
║                                                                              ║
║  LỊCH SỬ: MỌI SỞ GIAO DỊCH LỚN ĐỀU BẮT ĐẦU NGOÀI TRỜI                        ║
║    La Mã: đền Castor · partes/publicani · nuôi ngỗng thiêng                  ║
║       (Shiller tự cảnh báo: rất ít bằng chứng)                               ║
║    1602 Amsterdam · 1698 quán cà phê Jonathan's -> LSE                       ║
║    1792 cây buttonwood -> NYSE                                               ║
║    1850s cây đa Bombay -> BSE 1875 · 1990 Thượng Hải + Thâm Quyến            ║
║    1992 NSE toàn điện tử                                                     ║
║    NASDAQ (1970s) SINH RA TỪ NHỮNG CÔNG TY BỊ NYSE TỪ CHỐI (OTC).            ║
║    40 năm sau, chính NASDAQ đi hỏi mua NYSE.                                 ║
║                                                                              ║
║  BA LOẠI LỆNH                                                                ║
║    thị trường: chỉ nói SỐ LƯỢNG · giới hạn: nói cả SỐ LƯỢNG VÀ GIÁ           ║
║    dừng: cũng cả hai, nhưng chiều NGƯỢC lại                                  ║
║    "Đừng bao giờ đặt lệnh thị trường" — vài sở còn KHÔNG CHO PHÉP.           ║
║                                                                              ║
║  ⚠️ CHỖ LỜI GIẢNG NÓI QUÁ — quan trọng nhất cả bài                           ║
║    Shiller: giá 100, dừng lỗ ở 80, "ít nhất tôi biết tôi không thể mất       ║
║    quá 20 %". CÂU ĐÓ SAI.                                                    ║
║    LỆNH DỪNG LỖ KHI KÍCH HOẠT THÀNH LỆNH THỊ TRƯỜNG.                         ║
║    Bảo đảm BÁN, không bảo đảm GIÁ.                                           ║
║       bình thường 80,00 (-20 %) · gap 72,00 (-28 %) · tin xấu 61,00 (-39 %)  ║
║       NGÀY 6/5/2010: 0,01 (-99,99 %)   <- không phải giả thuyết              ║
║    NGHỊCH LÝ: thiết kế để bảo vệ khỏi cú sập, nhưng trong cú sập thì         ║
║    sổ lệnh mỏng nhất — nó chạy tốt nhất khi bạn cần nó ít nhất.              ║
║       NÓ HOẠT ĐỘNG TỐT NHẤT KHI BẠN CẦN NÓ ÍT NHẤT.                          ║
║    Cách đúng: dừng-GIỚI HẠN. Đánh đổi không tránh được:                      ║
║       dừng lỗ      -> bảo đảm bán ✅, giá ❌ (rủi ro: bán ở giá thảm hoạ)      ║
║       dừng-giới hạn -> giá ✅, bán ❌ (rủi ro: KHÔNG BÁN ĐƯỢC GÌ)              ║
║                                                                              ║
║  SỔ LỆNH LEVEL II                                                            ║
║    Hai đường cung cầu KHÔNG CẮT NHAU — vì nếu cắt thì đã khớp và biến mất.   ║
║    -> SỔ LỆNH KHÔNG PHẢI ẢNH CHỤP CUNG CẦU. Là ảnh chụp phần thị             ║
║       trường CHƯA TIÊU HOÁ ĐƯỢC. Khớp được thì đã khớp rồi.                  ║
║    Level I chỉ cho hàng đầu. Level II cho cả sổ.                             ║
║    ⚠️ HAI lệnh đầu cùng ở 25,24 từ hai sàn                                   ║
║       -> ĐỘ SÂU ĐỈNH LÀ 10.600, KHÔNG PHẢI 2.400.                            ║
║                                                                              ║
║  📚 LỆNH THỊ TRƯỜNG ĂN VÀO SỔ (Shiller dừng ở "sẽ ở nhiều mức giá khác nhau") ║
║       100 cp -> 0 trượt · 10.000 -> 0 trượt                                  ║
║       12.100 -> 0,000 % NHƯNG mất 15 USD thật                                ║
║       25.000 -> 0,050 %      57.300 -> 0,110 %, 1.569 USD                    ║
║    Ăn hết CẢ SÁU mức chào bán chỉ cần 57.300 cp — lúc BÌNH THƯỜNG.           ║
║    -> Rơi xuống 1 xu ngày 6/5/2010 không khó hiểu. Là số học.                ║
║                                                                              ║
║  HFT VÀ ECN                                                                  ║
║    Chiến lược MILI GIÂY: phát lệnh tồn tại 1/1000 giây rồi rút               ║
║    — để LỌC xem ai đang giao dịch với mình.                                  ║
║    ECN (Archipelago, Island): SEC cho phép thập niên 1990,                   ║
║    cố tình KHÔNG gọi chúng là sở giao dịch.                                  ║
║       Văn hoá web: KHÔNG THU TIỀN để xem sổ lệnh.                            ║
║       NYSE ban đầu coi thường ("đám sinh viên nghịch máy tính")              ║
║       -> rồi phải MUA LẠI năm 2005.                                          ║
║    ĐỊA LÝ QUAY TRỞ LẠI: điện thoại từng giải phóng môi giới khỏi New York.   ║
║       HFT kéo họ về, vì KHÔNG GÌ NHANH HƠN ÁNH SÁNG. -> Shiller đoán đúng.   ║
║                                                                              ║
║  1987 VÀ CẦU DAO                                                             ║
║    19/10/1987: S&P 500 rơi HƠN 20 % TRONG MỘT NGÀY. Uỷ ban Brady.            ║
║    Thủ phạm: "BẢO HIỂM DANH MỤC" — Shiller: nó chẳng phải bảo hiểm gì        ║
║    cả, nó là BÁN TỰ ĐỘNG.                                                    ║
║    -> ĐÓ CHÍNH LÀ LỆNH DỪNG LỖ PHÓNG TO LÊN QUY MÔ TOÀN THỊ TRƯỜNG.          ║
║       Cùng một vòng lặp, ở ba quy mô.                                        ║
║                                                                              ║
║  📚 NGHỀ TẠO LẬP — chương hay nhất                                            ║
║    Rủi ro: BỊ MOI bởi người có thông tin tốt hơn. Hình ảnh người buôn đồ cổ: ║
║       dân buôn chuyên nghiệp vào lục tìm món ĐỊNH GIÁ SAI                    ║
║       -> bạn mất món ngon, còn lại đồ tầm thường.                            ║
║    KHÔNG THỂ chống bằng cách thông minh hơn — quá nhiều thứ phải biết.       ║
║    Chỉ còn MỘT cách: ĐẶT CHÊNH LỆCH ĐỦ RỘNG ĐỂ BỊ MOI MÀ VẪN LÃI.            ║
║    Niêm yết giá lên màn hình = CON VỊT NGỒI IM.                              ║
║                                                                              ║
║    CHÊNH LỆCH HOÀ VỐN (Shiller nói "đủ rộng", chương trình tính ra số):      ║
║       0 % người biết trước ->  0 xu      5 %  -> 11 xu                       ║
║       1 %                  ->  2 xu     30 %  -> 86 xu (3,44 % giá)          ║
║    -> CHÊNH LỆCH KHÔNG PHẢI PHÍ DỊCH VỤ, KHÔNG PHẢI LỢI NHUẬN ĐỘC QUYỀN.     ║
║       NÓ LÀ GIÁ CỦA VIỆC KHÔNG BIẾT AI ĐANG ĐỨNG BÊN KIA.                    ║
║       Vì thế cổ phiếu ít người theo dõi có chênh lệch rộng hơn               ║
║       — không phải vì rủi ro hơn,                                            ║
║       mà vì TỶ LỆ NGƯỜI BIẾT TRƯỚC CAO HƠN.                                  ║
║                                                                              ║
║    PHÁ SẢN CỦA NGƯỜI TẠO LẬP:  P = ((1-p)/p)^S nếu p>1/2 ; = 1 nếu p<=1/2    ║
║       p=50 %: PHÁ SẢN CHẮC CHẮN, DÙ VỐN BAO NHIÊU                            ║
║               <- nên chênh lệch phải lớn hơn 0 thật sự                       ║
║       p=60 %, S=100: 2,46e-18 — rất nhỏ NHƯNG KHÔNG BẰNG KHÔNG,              ║
║               và "cuối cùng" thì rất dài                                     ║
║    BỊ ÉP GIỮA HAI PHÍA: hẹp -> p về 1/2, chắc chết                           ║
║                         rộng -> không có việc làm                            ║
║    Shiller: "Bạn ngủ không ngon, vì không bao giờ biết chắc nó sẽ            ║
║    không sụp đổ."                                                            ║
║                                                                              ║
║  ⚠️ ĐỐI CHIẾU 2026                                                           ║
║    "Chưa có ngày 6/5/2010 nào nữa, rồi sẽ ổn thôi" -> HỎNG SAU 16 THÁNG      ║
║       1/8/2012 KNIGHT CAPITAL: 45 phút, hơn 4 TRIỆU lệnh                     ║
║       (cần khớp 212), 397 triệu cp,                                          ║
║          mất 440-460 TRIỆU USD — gần như xoá sổ công ty                      ║
║       24/8/2015 Dow rơi ~1.100 điểm trong 5 PHÚT đầu phiên;                  ║
║       ETF tách khỏi giá trị cơ sở;                                           ║
║          các biện pháp dựng sau 2010 TỎ RA KHÔNG ĐỦ                          ║
║       5/2/2018 Volmageddon: XIV bị chấm dứt sau cú giảm 97 %                 ║
║       Lỗi phương pháp: rút kết luận "chỉ là bất thường" từ mẫu 11 THÁNG.     ║
║       Đúng thiên lệch ông dạy ở bài 12 — khoảng tin cậy quá hẹp.             ║
║                                                                              ║
║    CẦU DAO ĐÃ BỊ THAY HOÀN TOÀN (SEC duyệt 31/5/2012, đầy đủ 8/4/2013)       ║
║       Ngưỡng toàn thị trường: 10/20/30 % -> 7/13/20 %                        ║
║       LULD thay cầu dao từng cổ phiếu: biên độ 5 % (cp lớn) /                ║
║       10 % (còn lại), giữ 15 giây                                            ║
║       KHÁC BIỆT CĂN BẢN: bản cũ CHỮA CHÁY (dừng SAU khi lệnh sai đã khớp)    ║
║                  LULD CHỐNG CHÁY (CẤM khớp ngoài biên độ từ đầu)             ║
║       -> LULD chặn ở 95, cầu dao cũ chỉ dừng ở 90: SỚM HƠN 5 USD/cp.         ║
║          Lệnh dừng lỗ nay AN TOÀN HƠN — không nhờ loại lệnh tốt lên,         ║
║          mà nhờ HẠ TẦNG QUANH NÓ.                                            ║
║                                                                              ║
║    PFOF: từ "vấn đề khó" -> MÔ HÌNH KINH DOANH CHÍNH                         ║
║       EU: CẤM HOÀN TOÀN từ 30/6/2026 (Điều 39a MiFIR;                        ║
║           Đức được miễn tới đúng ngày đó)                                    ║
║       Anh: cấm từ 2012.   Mỹ: VẪN HỢP PHÁP, dựa trên công bố thông tin.      ║
║       Robinhood bị SEC phạt 65 TRIỆU USD (12/2020).                          ║
║       ĐIỂM HOÀ VỐN ~2.500 cp/lệnh: dưới -> "miễn phí" rẻ thật;               ║
║       trên -> ĐẮT HƠN cả việc trả hoa hồng                                   ║
║       -> NĐT LỆNH NHỎ ĐƯỢC LỢI, LỆNH LỚN TRẢ TIỀN.                           ║
║          Trợ cấp chéo, VÔ HÌNH THEO THIẾT KẾ.                                ║
║                                                                              ║
║    AI GÂY RA 6/5/2010: Navinder Sarao, truy tố 21/4/2015, 22 tội danh,       ║
║       nhận tội năm 2016,                                                     ║
║       tuyên án 28/1/2020 (thời gian tạm giam + 1 năm quản thúc tại gia).     ║
║       NHƯNG: CFTC 2014 nói ông ta KHÔNG GÂY RA, chỉ góp phần.                ║
║       Aldrich & Laughlin (UCSC): rất khó có khả năng;                        ║
║       CÓ THỂ ĐÃ XẢY RA NGAY CẢ KHI KHÔNG CÓ ÔNG TA.                          ║
║       -> TÌM ĐƯỢC THỦ PHẠM ≠ GIẢI THÍCH ĐƯỢC SỰ KIỆN.                        ║
║                                                                              ║
║    CUỘC ĐUA SÁP NHẬP: EC CHẶN Deutsche Börse-NYSE ngày 1/2/2012              ║
║       (vụ này sẽ nắm hơn 90 % phái sinh EU).                                 ║
║       ICE hoàn tất mua NYSE Euronext 13/11/2013, ~11 tỷ USD.                 ║
║       -> NYSE, lập dưới gốc cây năm 1792, nay thuộc một công ty giao         ║
║          dịch NĂNG LƯỢNG lập năm 2000.                                       ║
║       Shiller sai về người mua ("có thể thành công ty Đức")                  ║
║       nhưng ĐÃ NÊU ĐÚNG TÊN ICE.                                             ║
║                                                                              ║
║    Phát minh ĐẦU TIÊN của Edison là MÁY ĐẾM PHIẾU BẦU (1869), không ai mua.  ║
║       Máy in giá chứng khoán là THÀNH CÔNG THƯƠNG MẠI đầu tiên.              ║
║       -> Phát minh ĐẦU TIÊN của ông đã THẤT BẠI.                             ║
║                                                                              ║
║    QUY LUẬT: cơ chế sống, tham số chết — VÀ THÊM LOẠI THỨ BA:                ║
║       DỰ ĐOÁN VỀ CÔNG NGHỆ HỎNG NHANH NHẤT, VÀ HỎNG THEO HƯỚNG LẠC QUAN.     ║
║                                                                              ║
║  🇻🇳 VIỆT NAM                                                                 ║
║    HOSE THUẦN KHỚP LỆNH: giá do sổ lệnh quyết định,                          ║
║    KHÔNG AI bắt buộc yết giá hai chiều.                                      ║
║       09:00-09:15 định kỳ mở · 09:15-11:30 liên tục I                        ║
║       13:00-14:30 liên tục II                                                ║
║       14:30-14:45 định kỳ đóng · biên độ ±7 % · lô tối thiểu 100             ║
║    ⚠️ NÓI CHO ĐÚNG: khung pháp lý tạo lập thị trường ĐÃ CÓ                   ║
║       (Thông tư 120/2020/TT-BTC),                                            ║
║       nhưng chủ yếu áp cho ETF và chứng quyền, CHƯA rộng cho cp thường.      ║
║       -> Thanh khoản phụ thuộc HOÀN TOÀN vào việc có ai tình cờ muốn         ║
║          giao dịch ngược chiều.                                              ║
║       Nhưng ĐÂY LÀ ĐÁNH ĐỔI, KHÔNG PHẢI THIẾU SÓT: dealer sống bằng          ║
║       chênh lệch = tiền của người khác,                                      ║
║       và họ có đặc quyền thông tin. Câu hỏi đúng:                            ║
║       THANH KHOẢN TRONG KHỦNG HOẢNG ĐÁNG GIÁ BAO NHIÊU?                      ║
║                                                                              ║
║    NHƯNG CÒN MỘT THỨ THIẾU, VÀ THỨ NÀY KHÔNG PHẢI ĐÁNH ĐỔI:                  ║
║    CCP — Việt Nam có cho PHÁI SINH từ 2017, thị trường CƠ SỞ thì CHƯA.       ║
║       Ngân hàng Thế giới: 80 % hệ thống thanh toán toàn cầu đã áp dụng CCP.  ║
║       Không có CCP -> mỗi bên chịu rủi ro bên kia không thanh toán.          ║
║       Có CCP -> trung tâm làm đối tác CỦA CẢ HAI.                            ║
║       Bạn không cần biết ai đứng bên kia.                                    ║
║       Luật 56/2024/QH15 · NĐ 245/2025 (11/9/2025) · MỤC TIÊU QUÝ I/2027      ║
║                                                                              ║
║    KRX vận hành 5/5/2025 — mở đường cho CCP, DvP, T+0, bán khống.            ║
║    FTSE RUSSELL: công bố 7/10/2025, xác nhận 4/2026,                         ║
║    HIỆU LỰC THỨ HAI 21/9/2026.                                               ║
║       Cận biên -> MỚI NỔI THỨ CẤP.                                           ║
║       Vào chỉ số 4 giai đoạn: 10 % · 30 % · 65 % · hoàn tất.                 ║
║       Ghi nhận: gỡ ký quỹ trước giao dịch (non-prefunding)                   ║
║       · Thông tư 08/2026/TT-BTC                                              ║
║       Vốn hoá ~410 tỷ USD · HOSE ~1,2 tỷ USD/phiên (giữa 5/2026),            ║
║       thanh khoản dẫn đầu Đông Nam Á                                         ║
║                                                                              ║
║    BA VIỆC DÙNG ĐƯỢC NGAY:                                                   ║
║       (1) đừng dùng lệnh thị trường cho cp thanh khoản thấp                  ║
║           — xem độ sâu sổ lệnh TRƯỚC                                         ║
║       (2) lệnh dừng lỗ bảo đảm BÁN, không bảo đảm GIÁ                        ║
║       (3) chênh lệch rộng bất thường = CÓ NGƯỜI BIẾT THỨ BẠN KHÔNG BIẾT      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

**Nguồn gốc**

1. Shiller, Robert J. *Financial Markets* (ECON 252), buổi 21 — *Exchanges, Brokers, Dealers,
   Clearinghouses*, Yale University, 13/4/2011. YouTube `kAl8DezwLAE`.
2. Bản ghi Open Yale Courses buổi 21 —
   <https://oyc.yale.edu/economics/econ-252-11/lecture-21>
3. Polanyi, Karl. *The Great Transformation*, 1944 — nguồn của §1.
4. Boulding, Kenneth E. — diễn văn nhậm chức chủ tịch Hội Kinh tế Mỹ, 1969.
5. SEC & CFTC. *Findings Regarding the Market Events of May 6, 2010* — tài liệu Shiller giao đọc thêm.

**Cho các sự kiện sau 2011**

6. SEC — *SEC Charges Knight Capital With Violations of Market Access Rule*, 2013 —
   <https://www.sec.gov/newsroom/press-releases/2013-222>
7. Knight Capital Group — Form 8-K, 2012, công bố thiệt hại —
   <https://www.sec.gov/Archives/edgar/data/0001060749/000119312512332176/d391111dex991.htm>
8. Harvard Law School Forum on Corporate Governance — *"Limit Up-Limit Down" Plan and Circuit
   Breakers Approved*, 13/6/2012 —
   <https://corpgov.law.harvard.edu/2012/06/13/limit-up-limit-down-plan-and-circuit-breakers-approved/>
9. Nasdaq — *Limit Up-Limit Down FAQ*, biên độ 5 %/10 %, quy tắc 15 giây —
   <https://nasdaqtrader.com/content/MarketRegulation/LULD_FAQ.pdf>
10. Investor.gov (SEC) — *Stock Market Circuit Breakers*, ngưỡng 7/13/20 % —
    <https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-market-circuit-breakers>
11. Wikipedia — *2010 flash crash*, tổng hợp diễn biến và các mốc pháp lý —
    <https://en.wikipedia.org/wiki/2010_flash_crash>

**Cho vụ Sarao**

12. CNBC — *'Flash crash' trader Navinder Singh Sarao sentenced to home detention*, 29/1/2020 —
    <https://www.cnbc.com/2020/01/29/flash-crash-trader-navinder-singh-sarao-sentenced-to-home-detention.html>
13. Georgetown Law Technology Review — *U.S. v. Sarao: The Flash Crash and a New Effort to Prosecute
    Market Manipulation* —
    <https://georgetownlawtechreview.org/u-s-v-sarao-the-flash-crash-and-a-new-effort-to-prosecute-market-manipulation-and-deceptive-trading-practices/GLTR-04-2017/>
14. UC Santa Cruz — *New paper examines the details behind stock market 'flash crash'* (Aldrich &
    Laughlin) — <https://news.ucsc.edu/2016/03/flash-crash/>

**Cho cuộc đua sáp nhập**

15. CNN Money — *NYSE Euronext and Deutsche Boerse merger blocked*, 1/2/2012 —
    <https://money.cnn.com/2012/02/01/markets/nyse_euronext_deutsche_boerse/index.htm>
16. Intercontinental Exchange — *IntercontinentalExchange Completes Acquisition of NYSE Euronext*,
    13/11/2013 —
    <https://ir.theice.com/press/news-details/2013/IntercontinentalExchange-Completes-Acquisition-of-NYSE-Euronext/default.aspx>

**Cho trả tiền cho luồng lệnh**

17. Norton Rose Fulbright — *MiFIR and MiFID II review*, Điều 39a về lệnh cấm PFOF —
    <https://www.nortonrosefulbright.com/en/knowledge/publications/494a828d/mifir-and-mifid-ii-review-a-further-ten-key-things-that-eu-financial-institutions-should-know>
18. National Law Review — *The EU Adopts a Directive Amending MiFID II and MiFIR on Data
    Transparency, the Consolidated Tape and Payment for Order Flow* —
    <https://natlawreview.com/article/eu-adopts-directive-amending-mifid-ii-and-mifir-data-transparency-consolidated-tape>
19. Congressional Research Service — *Payment for Order Flow (PFOF) and Broker-Dealer Regulation* —
    <https://www.congress.gov/crs-product/IF12594>
20. Congressional Research Service — *Payment for Order Flow: The SEC Proposes Reforms* —
    <https://www.congress.gov/crs-product/IF12332>
21. InnReg — *Payment for Order Flow and FINRA Rule 5310*, gồm mức phạt Robinhood —
    <https://www.innreg.com/blog/payment-for-order-flow-and-finra-rule-5310>

**Cho góc Việt Nam**

22. FPTS — *Quy định giao dịch của HOSE*: các phiên khớp lệnh, biên độ ±7 %, lô tối thiểu —
    <https://fpts.com.vn/ho-tro-khach-hang/giao-dich-chung-khoan/huong-dan-giao-dich-co-phieu/quy-dinh-giao-dich/quy-dinh-giao-dich-cua-hose/>
23. Vietnambiz — *Hệ thống giao dịch khớp giá (quote-driven) và khớp lệnh (order-driven) là gì?* —
    <https://vietnambiz.vn/he-thong-giao-dich-khop-gia-price-driven-system-va-khop-lenh-order-driven-system-la-gi-20190820210224793.htm>
24. **Thông tư 120/2020/TT-BTC** — quy định về giao dịch của thành viên tạo lập thị trường.
25. Báo Chính phủ — *Chính thức công bố Kế hoạch triển khai Cơ chế đối tác bù trừ trung tâm (CCP)*,
    18/7/2025 —
    <https://baochinhphu.vn/chinh-thuc-cong-bo-ke-hoach-trien-khai-co-che-doi-tac-bu-tru-trung-tam-102250718093953823.htm>
26. VnEconomy — *Cơ chế đối tác bù trừ trung tâm (CCP) dự kiến vận hành trong quý 1/2027* —
    <https://vneconomy.vn/co-che-doi-tac-bu-tru-trung-tam-ccp-du-kien-van-hanh-trong-quy-12027.htm>
27. Thời báo Tài chính Việt Nam — *Khung pháp lý mới "mở cánh cửa" cho cơ chế bù trừ trung tâm*: Luật
    56/2024/QH15, Nghị định 245/2025/NĐ-CP, số liệu 80 % của Ngân hàng Thế giới —
    <https://thoibaotaichinhvietnam.vn/khung-phap-ly-moi-mo-canh-cua-cho-co-che-bu-tru-trung-tam-185257-185257.html>
28. LSEG / FTSE Russell — *FTSE Russell country classification September 2025*, công bố 7/10/2025 —
    <https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025>
29. CNBC — *FTSE Russell confirms Vietnam's emerging market status*, 8/4/2026 —
    <https://www.cnbc.com/2026/04/08/ftse-russell-confirms-vietnams-emerging-market-status.html>
30. Báo Chính phủ — *FTSE Russell xác nhận lộ trình nâng hạng thị trường chứng khoán Việt Nam* —
    <https://baochinhphu.vn/chinh-thuc-xac-nhan-lo-trinh-nang-hang-thi-truong-chung-khoan-102260407214555354.htm>
31. TheLEADER — *Hệ thống KRX và kỳ vọng nâng hạng chứng khoán Việt Nam* —
    <https://theleader.vn/he-thong-krx-va-ky-vong-nang-hang-chung-khoan-d45206.html>
32. Vietnam Briefing — *Vietnam Reclassified to Emerging Market Status by FTSE Russell* —
    <https://www.vietnam-briefing.com/news/vietnam-reclassified-to-emerging-market-status-by-ftse-russell.html/>

---

**Bản đồ khoá học**

Yale ECON 252 — *Thị trường Tài chính*, Robert J. Shiller · [chỉ mục môn học](../README.md)

1. [Tài chính là hạ tầng xã hội](bai_01_ha_tang_xa_hoi.md) — phát minh, trách nhiệm hữu hạn, gắn chỉ số lạm phát
2. [Bảo hiểm](bai_02_bao_hiem.md) — gộp rủi ro, và ba chỗ nó gãy
3. [Ngân hàng](bai_03_ngan_hang.md) — thanh khoản, lựa chọn ngược, bank run, Basel
4. [Chính sách tiền tệ](bai_04_chinh_sach_tien_te.md) — ngân hàng trung ương, công cụ, giới hạn
5. [Ngân hàng đầu tư](bai_05_ngan_hang_dau_tu.md) — shadow banking, repo, đòn bẩy
6. **Sở giao dịch, môi giới, dealer, HFT** — sổ lệnh, tạo lập, thanh toán bù trừ ← *bạn đang ở đây*
7. [Nhà quản lý quỹ và nghĩa vụ tín thác](bai_07_quan_ly_quy.md) — quy tắc người thận trọng, hưu trí, Mô hình Yale
8. [Cổ phiếu nhìn từ góc định chế](bai_08_co_phieu_dinh_che.md) — cổ tức, pha loãng, bảng cân đối, giá trên sổ sách
9. [Bất động sản](bai_09_bat_dong_san.md) — từ quyền tài sản tới MBS
10. [Quy định, tự quản, hành vi sai trái](bai_10_quy_dinh_tu_quan.md) — năm tầng, năm cửa thoát, con lắc của Laura Cha
11. [Tài chính công và phi lợi nhuận](bai_11_tai_chinh_cong.md) — phi lợi nhuận, ngân sách vốn, Bismarck và công nghệ thông tin
12. [Tài chính hành vi](bai_12_tai_chinh_hanh_vi.md) — Shiller phản biện Lo
13. [Mục đích, đạo đức, dân chủ hoá tài chính](bai_13_muc_dich_dao_duc.md) — bài giảng kết — bất bình đẳng là thất bại quản trị rủi ro

📐 Nửa **định giá** nằm ở kho bên cạnh: [MIT 15.401 — Lý thuyết Tài chính I](../../mit-15401-finance/README.md)
🐍 Chương trình Python tính mọi con số: [thuc_hanh/README.md](../thuc_hanh/README.md)
