# Bài 11 — Nhận diện lừa đảo: Ponzi và CFD

> [!info] Về bài này
> Bài học dựa trên **C2 tr. 47–57** — Unit 4, **Lesson 4 (Mô hình Ponzi, tr. 47–53)** và **Lesson 5
> (CFD là gì?, tr. 55–57)** của *Tài chính cá nhân 101, Class 2*.
> **Cần đọc trước:** [Bài 10](bai_10_tai_chinh_hanh_vi.md) — bài này là chỗ khung thiên kiến ở bài 10
> được đem ra dùng. Ponzi không đánh vào sự thiếu hiểu biết, nó đánh vào lòng tham và ảo tưởng kiểm
> soát; bài 10 đã gọi tên sẵn từng cú đánh.
> **Một chỗ để dành cho bài sau:** đoạn *"Hai. Khẩu vị rủi ro"* trong bài blog (**C2 tr. 54**) —
> mức 5%/tháng, 10%/tháng, *"một vốn bốn mươi lời"* — thuộc về **bài 12** (rủi ro và khẩu vị rủi ro),
> nên bài này chỉ chạm qua.
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
> **Về phần pháp lý:** mục 8 dẫn quan điểm cơ quan quản lý, tra ngày **10/09/2026**. Chính sách đổi
> thì kiểm lại ngày tra trước khi tin.
> **Code:** [`thuc_hanh/bai-11-nhan-dien-lua-dao.py`](../thuc_hanh/bai-11-nhan-dien-lua-dao.py)
> — hai phép tính sách bỏ trống (Ponzi gấp đôi bao nhiêu vòng thì hết người, đòn bẩy đi ngược bao
> nhiêu thì cháy tài khoản) do tệp này tính, kèm công thức một dòng để tự kiểm.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).

---

## Mục lục

<!-- MUC-LUC -->

- [1. Hai loại nguy hiểm khác loại nhau](#1-hai-loại-nguy-hiểm-khác-loại-nhau)
- [2. Ponzi: sách định nghĩa và mô tả cơ chế](#2-ponzi-sách-định-nghĩa-và-mô-tả-cơ-chế)
- [3. [đính chính] Ponzi không phải "đa cấp kim tự tháp"](#3-đính-chính-ponzi-không-phải-đa-cấp-kim-tự-tháp)
- [4. [bổ sung] Vì sao Ponzi chắc chắn sụp — phép nhân sách không làm](#4-bổ-sung-vì-sao-ponzi-chắc-chắn-sụp--phép-nhân-sách-không-làm)
- [5. Đặc điểm nhận diện, và phép thử một dòng](#5-đặc-điểm-nhận-diện-và-phép-thử-một-dòng)
- [6. CFD: sách nói gì, và một chỗ gọi sai tên](#6-cfd-sách-nói-gì-và-một-chỗ-gọi-sai-tên)
- [7. [bổ sung] Đòn bẩy giết bằng cách nào](#7-bổ-sung-đòn-bẩy-giết-bằng-cách-nào)
- [8. [2026] Forex và CFD ở Việt Nam: chưa được cấp phép](#8-2026-forex-và-cfd-ở-việt-nam-chưa-được-cấp-phép)
- [9. Ráp lại: hai loại nguy hiểm, hai cách phòng](#9-ráp-lại-hai-loại-nguy-hiểm-hai-cách-phòng)
- [10. Tự thử](#10-tự-thử)
- [11. Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
- [12. Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
  <!-- /MUC-LUC -->

---

## 1. Hai loại nguy hiểm khác loại nhau

Sách xếp Ponzi và CFD cạnh nhau trong hai lesson liền kề, và người đọc dễ gộp chúng thành một mối
"những thứ nguy hiểm nên tránh". Nhưng chúng **nguy hiểm theo hai cách khác hẳn nhau**, và gộp lại
thì mất luôn cách phòng đúng cho từng cái:


|                   | Ponzi                                           | CFD / Forex                                                         |
| ----------------- | ----------------------------------------------- | ------------------------------------------------------------------- |
| Bản chất          | **lừa đảo** — không có hoạt động thật           | **công cụ tài chính có thật**, rủi ro rất cao                       |
| Có sòng bạc không | **không có sòng nào cả** — tiền chỉ luân chuyển | có sòng thật, giá thật, đối thủ thật                                |
| Bạn thua vì       | bị lấy cắp, sớm muộn gì cũng mất                | thị trường đi ngược, đòn bẩy nhân cái thua lên                      |
| Kết cục xấu nhất  | mất toàn bộ khi hệ thống sụp                    | cháy tài khoản chỉ sau một biến động nhỏ                            |
| Sách nói          | *"hình thức lừa đảo"* (tr. 48)                  | *"mặc dù không phải lừa đảo, tuy nhiên độ rủi ro rất cao"* (tr. 57) |
| Cách phòng        | **nhận diện và tránh hoàn toàn**                | hiểu đòn bẩy trước khi nghĩ tới tham gia                            |


Nói gọn: **Ponzi là nơi không có sòng bạc mà bạn vẫn thua; CFD là sòng bạc thật, nơi đòn bẩy khiến
bạn thua nhanh hơn tưởng.** Một cái phải tránh; một cái phải hiểu. Bài này tách bạch hai việc đó.

---

## 2. Ponzi: sách định nghĩa và mô tả cơ chế

Lesson 4 mở bằng một câu đặt đúng trọng tâm (tr. 47):

> [!quote]
> *"Nhận biết sớm những dấu hiệu của mô hình lừa đảo Ponzi là cách thiết thực để bạn bảo vệ túi tiền
> của bản thân và gia đình."*

Và ở tr. 48, sách nối thẳng lừa đảo với thứ mà [bài 10](bai_10_tai_chinh_hanh_vi.md) vừa dựng khung:

> [!quote]
> *"Hầu hết cơ hội lại là 'bánh vẽ'. Và hầu hết các loại bánh vẽ chính là Ponzi."*

Định nghĩa của sách gọn và **đúng phần cốt lõi** (tr. 48):

> [!quote]
> *"Ponzi (hay mô hình đa cấp kim tự tháp) là hình thức lừa đảo, mời gọi mua sản phẩm hoặc đầu tư,
> cam kết trả lãi cao, đồng thời đưa ra nhiều tấm gương đã nhận lợi tức cao trước đó. Thực tế không
> hề có hoạt động kinh doanh - đầu tư nào diễn ra, hoạt động chỉ dựa trên việc lấy tiền của người đến
> sau trả cho người đến trước."*

Câu cuối là toàn bộ Ponzi trong một dòng: **không có hoạt động kinh doanh nào cả.** Tiền người sau
chảy vào túi người trước, và một phần vào túi kẻ chủ mưu. Ngoặc đơn *"(hay mô hình đa cấp kim tự
tháp)"* là chỗ sai — [mục 3](#3-đính-chính-ponzi-không-phải-đa-cấp-kim-tự-tháp) nói riêng.

Sách gắn ngay lừa đảo với lòng tham (tr. 48): *"Họ bị mờ mắt trước lợi nhuận nên quên mất những rủi
ro có thể gặp phải."* — đúng chỗ [bài 10 mục 5](bai_10_tai_chinh_hanh_vi.md#5-sự-tham-lam--khi-quá-tốt-để-là-thật-vẫn-thắng-ở-trang-52) gọi là **chạy theo lợi nhuận**.

### Ba thành phần của mô hình (tr. 50)

Sách chia người trong mô hình làm ba vai, và đây là phần mô tả rất tốt:


| Vai                            | Sách mô tả                                                                                                                     | Làm gì                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| **Schemer**                    | *"kẻ chủ mưu lập nên hệ thống, xây dựng hình ảnh cá nhân là những doanh nhân thành đạt, kỹ năng hùng biện và thuyết phục tốt"* | dựng và điều hành, thu tiền |
| **Investor**                   | *"đội 'gà' được chăn dắt bởi Schemer… hưởng lợi từ lãi suất cao ngất ngưởng… **mà không cần phải làm gì**"*                    | góp vốn, thụ động           |
| **Ponzi Introducing Investor** | *"không bỏ vốn vào mô hình mà kiếm tiền bằng cách **giới thiệu nhiều người gia nhập**"*                                        | tuyển người, ăn hoa hồng    |


Chú ý hai vai đầu là Ponzi thuần; vai thứ ba mới là chỗ sách trộn lẫn một mô hình khác vào — giữ ba
vai này trong đầu, mục 3 sẽ dùng lại chính bảng này để tách hai thứ ra.

### Phương thức hoạt động (tr. 51–52)

Sách mô tả vòng đời Ponzi chính xác. Điểm nhấn của chính sách:

- **Từ khoá là "hứa hẹn".** Nhà đầu tư góp vốn trước, được *"hứa hẹn"* trả cả vốn lẫn lãi. Chưa
có gì được trả, mới chỉ có lời hứa.
- **Lấy của người sau trả người trước.** Sách viết cụ thể: *"trích tiền từ hai người đến sau để trả
cho người đầu tiên"* — con số "hai người" ấy là chìa khoá của [mục 4](#4-bổ-sung-vì-sao-ponzi-chắc-chắn-sụp--phép-nhân-sách-không-làm).
- **Trả bằng báo cáo, không bằng tiền.** Khi lãi hứa càng cao, nhà đầu tư càng để tiền lại tái đầu
tư: *"schemer không thực sự trả tiền mà chỉ gửi báo cáo số tiền kiếm được."* Đây là mấu chốt vì
sao Ponzi kéo dài được — phần lớn "lợi nhuận" chưa bao giờ rời hệ thống.
- **Càng khó rút càng gần sụp.** Schemer dựng "kế hoạch mới" hưởng lãi cao hơn nhưng khoá không cho
rút một thời gian.
- **Và cái kết**: *"Nếu hệ thống không duy trì được nữa, Schemer sẽ biến mất cùng số tiền thu được
từ các nhà đầu tư."*

Sách chốt bằng câu đáng mang theo (tr. 52):

> [!quote]
> *"họ sẽ lấy tiền của bạn bằng cách bán cho mỗi người một giấc mơ không có thật. Tôi luôn tâm niệm
> câu 'Too good to be true'. Bạn cũng nên như vậy."*

---

## 3. [đính chính] Ponzi không phải "đa cấp kim tự tháp"

Sách gọi Ponzi là *"mô hình đa cấp kim tự tháp"* ở tr. 48, rồi gọi Charles Ponzi là *"'tổ nghề' của
mô hình kim tự tháp đa cấp"* ở tr. 49. **Đây là hai mô hình khác nhau**, và gộp làm một thì mất luôn
dấu hiệu nhận diện quan trọng nhất của mỗi loại.


|                       | **Ponzi**                                               | **Kim tự tháp / đa cấp (pyramid, MLM)**         |
| --------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| Ai trả tiền cho ai    | **một** kẻ trung tâm lấy tiền người sau trả người trước | trả **hoa hồng theo tầng** cho việc tuyển người |
| Người tham gia làm gì | **thụ động** — góp tiền rồi chờ lãi                     | **chủ động đi tuyển** người mới bên dưới mình   |
| Nguồn "lợi nhuận"     | tiền của nhà đầu tư mới                                 | hoa hồng từ mạng lưới mình tuyển được           |
| Cấu trúc              | một trung tâm, các nạn nhân ngang hàng                  | hình tháp nhiều tầng, mỗi tầng ăn của tầng dưới |


Điều thú vị: **chính bảng ba thành phần của sách (mục 2) đã tự tách hai mô hình ra mà sách không nhận
ra.** Vai *Schemer* + *Investor thụ động "không cần làm gì"* là **Ponzi đúng nghĩa**. Vai *Ponzi
Introducing Investor* — *"kiếm tiền bằng cách giới thiệu nhiều người gia nhập"* — cùng với dấu hiệu
*"hoa hồng giới thiệu nhiều lớp"* ở tr. 51, lại là **đặc trưng của kim tự tháp**, không phải Ponzi.
Sách mô tả một mô hình **lai** rồi dán cho nó một cái tên.

Và về lịch sử: Charles Ponzi (1882–1949, sách ghi đúng năm sinh) chạy một Ponzi **thuần** — hứa lãi
từ chênh lệch tem phiếu bưu chính quốc tế, lấy tiền người sau trả người trước, **không** có mạng lưới
tuyển tầng. Gọi ông là *"tổ nghề của mô hình kim tự tháp đa cấp"* là gán cho ông đúng cái mô hình mà
ông không dựng.

Vì sao phân biệt này đáng tiền, không phải bắt bẻ chữ:

- **Dấu hiệu nhận ra khác nhau.** Nghi Ponzi thì hỏi *"lợi nhuận đến từ hoạt động kinh doanh nào có
thật?"*. Nghi kim tự tháp thì hỏi *"tôi kiếm tiền từ **bán sản phẩm** hay từ **tuyển người**?"*.
Gộp hai câu này thì bỏ sót một nửa số bẫy.
- Con số 15 triệu USD và *"6 ngân hàng phá sản"* ở tr. 49 thì bài này **không kiểm chứng được từ
sách**; nêu lại nguyên văn và đánh dấu là số của sách, chưa đối chiếu nguồn độc lập.

---

## 4. [bổ sung] Vì sao Ponzi chắc chắn sụp — phép nhân sách không làm

Sách nói Ponzi *"lấy tiền người sau trả người trước"* và rồi *"sẽ biến mất"*, nhưng không nói **vì
sao sụp là chắc chắn**, không phải xui rủi. Câu trả lời nằm ngay trong con số của chính sách: *"trích
tiền từ **hai** người đến sau để trả cho người đầu tiên"* (tr. 51).

Nếu mỗi người được trả cần hai người mới nuôi, thì **số người phải gấp đôi sau mỗi vòng**. Mà nhân
đôi liên tục thì rất nhanh vượt quá số người có trên đời:

```
   số người vòng n = 2 mũ (n − 1)          (mỗi vòng gấp đôi vòng trước)
```


| Sau bao nhiêu vòng gấp đôi | Số người cần có thêm | Vượt qua                    |
| --------------------------: | --------------------: | --------------------------- |
| 17                         | ~131 nghìn           | một thị trấn                |
| 20                         | ~1 triệu             | một thành phố lớn           |
| **27**                     | **~134 triệu**       | **toàn bộ dân số Việt Nam** |
| **33**                     | **~8,6 tỷ**          | **toàn bộ dân số thế giới** |


Chỉ **27 vòng** là mô hình đã cần nhiều người hơn cả nước Việt Nam; **33 vòng** là hết sạch loài
người. Không có Ponzi nào tìm được nguồn người vô hạn, nên câu hỏi chưa bao giờ là *"có sụp không"*
mà là *"sụp vào vòng thứ mấy"* — và ai còn ở trong hệ thống lúc đó thì mất trắng.

Đây đúng là **phép nhân một dòng** mà [bài 10 mục 5](bai_10_tai_chinh_hanh_vi.md#5-sự-tham-lam--khi-quá-tốt-để-là-thật-vẫn-thắng-ở-trang-52)
dạy để bật Hệ thống 2: ở đó ta nhân **lãi** ra cả năm (*"20%/tháng"* thành 791%/năm — bất khả); ở
đây ta nhân **số người** qua từng vòng, và cũng ra một con số bất khả. Cùng một công cụ, hai chỗ dùng.

---

## 5. Đặc điểm nhận diện, và phép thử một dòng

Sách liệt kê dấu hiệu Ponzi ở tr. 50–51, và danh sách này chép được, gần như đủ:


| Dấu hiệu sách nêu                                                    | Hỏi lại một câu                               |
| -------------------------------------------------------------------- | --------------------------------------------- |
| *"Kêu gọi đầu tư làm giàu một cách nhanh chóng nhưng thiếu cơ sở"*   | tiền lời đến từ hoạt động thật nào?           |
| *"Thông tin đưa ra mơ hồ và thường phóng đại"*                       | có giải thích được bằng số cụ thể không?      |
| *"Hứa hẹn lãi suất cao ngất ngưởng hoặc 'không làm gì vẫn có tiền'"* | nhân ra cả năm là bao nhiêu?                  |
| *"Cam kết chắc chắn không rủi ro, đưa ra tỷ lệ hoàn vốn cố định"*    | đầu tư thật nào mà không rủi ro?              |
| *"Khó rút vốn"* — cho rút ít lúc đầu để tạo niềm tin                 | thử rút toàn bộ xem có được không?            |
| *"Hoạt động chui, không khai báo với cơ quan có thẩm quyền"*         | có được cấp phép không, tra ở đâu?            |
| *"Sản phẩm đầu tư hời hợt, hoa hồng giới thiệu nhiều lớp"*           | tôi kiếm tiền từ sản phẩm hay từ tuyển người? |


Hai câu hỏi mạnh nhất cả bảng, đáng tách ra:

1. **Nhân lãi ra cả năm.** Đây là phép thử của bài 10. Bất kỳ mức lãi nào nghe hấp dẫn, nhân lên bằng
 lãi kép rồi hỏi cả nền kinh tế có làm nổi không. *"Too good to be true"* (tr. 52) chính là câu này
 nói bằng tiếng Anh.
2. **Lợi nhuận đến từ đâu.** Ponzi không có hoạt động kinh doanh thật (tr. 48). Nếu không ai chỉ được
 ra tiền lời sinh ra từ việc bán cái gì, làm ra cái gì — mà chỉ nói *"mô hình"*, *"hệ thống"*,
 *"cơ hội"* — thì gần như chắc chắn nguồn duy nhất là tiền người vào sau.

Và tại sao chỉ biết dấu hiệu vẫn chưa đủ: [bài 10](bai_10_tai_chinh_hanh_vi.md) đã cảnh báo — người
dính Ponzi thường **ngửi ra mùi Ponzi** nhưng vẫn vào, vì tin mình là kẻ đến sớm (thiên kiến lạc
quan) và sẽ rút kịp (ảo tưởng kiểm soát). Nên phòng Ponzi không phải "nhận ra dấu hiệu" — mà là
**một quy tắc cứng dựng sẵn**: không bỏ tiền vào thứ không chỉ ra được nguồn lợi nhuận thật, bất kể
lời chào hấp dẫn tới đâu. Đúng tinh thần *"sửa hệ thống, không sửa người"* của
[bài 10 mục 8](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại).

---

## 6. CFD: sách nói gì, và một chỗ gọi sai tên

Lesson 5 chuyển sang một thứ **khác loại hẳn** với Ponzi. Sách thành thật về phạm vi (tr. 55):

> [!quote]
> *"tôi chắc chắn với bạn, sẽ chỉ đưa ra những kiến thức cần thiết. Không quá màu mè, không quá đa
> dạng. Đây là bước đệm…"*

Sách vào đề bằng Forex (tr. 55–56):

> [!quote]
> *"Bạn nghĩ những người tham gia Forex có trao đổi ngoại tệ không? Không! Thực chất họ đang giao
> dịch CFD - Kiếm lợi nhuận từ sự chênh lệch tỷ giá."*

Rồi định nghĩa (tr. 56):

> [!quote]
> *"CFD - Contracts for Difference - Hợp đồng chênh lệch là một loại thỏa thuận giữa bên mua và bên
> bán, được thực hiện nhờ vào khoảng chênh lệch giá của chứng khoán hoặc loại tài sản nào đó tại thời
> điểm mở và đóng lệnh."*

Nói gọn: bạn **không mua tài sản**, bạn cá cược vào **chênh lệch giá của nó** giữa lúc mở và lúc đóng
lệnh. Sách nêu hai đặc điểm đúng (tr. 56): *"CFD là một loại hàng hóa phái sinh"* và *"Có thể sử dụng
các đòn bẩy khi giao dịch"* — cái thứ hai là chỗ nguy hiểm, để riêng cho [mục 7](#7-bổ-sung-đòn-bẩy-giết-bằng-cách-nào).

### [đính chính] "Contract for Difference", không phải "different"

Trong bài blog ở tr. 54, sách viết tắt CFD thành *"contract for different"*, rồi hai trang sau ở
tr. 56 lại viết đúng *"Contracts for Difference"*. Bản đúng là **Contract for Difference** — *hợp
đồng chênh lệch*. *"Different"* (tính từ: khác biệt) khác nghĩa hẳn *"Difference"* (danh từ: khoản
chênh lệch), và chính khoản chênh lệch giá mới là thứ hợp đồng này nói tới. Lỗi nhỏ, nhưng vì nó nằm
ngay trong cái tên nên đáng sửa — giống lỗi *"chị B / chị C"* mà [bài 8](bai_08_vay_va_tra_no.md)
đã bắt.

---

## 7. [bổ sung] Đòn bẩy giết bằng cách nào

Sách nói CFD *"có thể sử dụng các đòn bẩy"* và mô tả đúng cơ chế (tr. 56):

> [!quote]
> *"trader chỉ cần một tỷ lệ vốn nhỏ so với tổng giá trị thực của giao dịch để đặt lệnh, phần còn lại
> vay từ nhà môi giới. Giao dịch đòn bẩy hay còn được gọi là giao dịch ký quỹ."*

Nhưng sách dừng ở mô tả, không cho con số cho thấy *"độ rủi ro rất cao"* (tr. 57) cao tới đâu. Mà đây
là chỗ một phép tính một dòng đổi hẳn cách nhìn. Đòn bẩy nghĩa là bạn điều khiển một vị thế lớn gấp
nhiều lần vốn thật của mình, nên **giá chỉ cần đi ngược một chút là vốn thật bay sạch**:

```
   mức giá đi ngược làm cháy tài khoản = 1 / đòn bẩy
```


| Đòn bẩy | Vốn thật bỏ ra | Giá đi ngược bao nhiêu là **mất trắng** |
| ------- | --------------: | ---------------------------------------: |
| 1:10    | 10%            | **10%**                                 |
| 1:20    | 5%             | **5%**                                  |
| 1:50    | 2%             | **2%**                                  |
| 1:100   | 1%             | **1%**                                  |
| 1:500   | 0,2%           | **0,2%**                                |


Ở mức đòn bẩy 1:100 mà các sàn thường mời, **thị trường đi ngược đúng 1% là bạn mất toàn bộ vốn** —
và tỷ giá hay giá cổ phiếu nhúc nhích 1% trong một ngày là chuyện thường. Đây là lý do câu *"độ rủi
ro rất cao"* của sách còn nhẹ: với đòn bẩy cao, rủi ro không phải "lỗ nhiều" mà là **cháy sạch, rất
nhanh**.

Ba mối nối ra ngoài bài:

- **Đòn bẩy là vay.** Sách gọi đúng: *"phần còn lại vay từ nhà môi giới"*. Nên toàn bộ cảnh báo về nợ
ở [bài 8](bai_08_vay_va_tra_no.md) áp vào đây — chỉ khác là khoản vay này có thể quét sạch vốn
trong vài phút.
- **Bất đối xứng lỗ–lãi.** [Bài 10 mục 7](bai_10_tai_chinh_hanh_vi.md#7-bổ-sung-bản-đồ-thiên-kiến-mỗi-cái-đã-xuất-hiện-ở-đâu):
lỗ 50% cần lãi 100% mới về vốn; còn cháy tài khoản là lỗ 100%, cần lãi **vô hạn** — tức không về
được nữa, ván đó kết thúc.
- **Khẩu vị rủi ro.** Chính tác giả ở tr. 54 tự nhận *"một vốn bốn mươi lời… cũng có nếu bạn chấp
nhận mất trắng toàn bộ số tiền trong 99% trường hợp"* — đó là khẩu vị rủi ro, và là chủ đề của
**bài 12**.

---

## 8. [2026] Forex và CFD ở Việt Nam: chưa được cấp phép

Sách chốt Lesson 5 bằng một cảnh báo pháp lý (tr. 57):

> [!quote]
> *"Giao dịch CFD mặc dù không phải lừa đảo, tuy nhiên độ rủi ro rất cao và giao dịch Forex hiện tại
> chưa được sự cho phép tại thị trường Việt Nam. Các bạn cần cân nhắc kỹ trước khi tham gia loại hình
> này."*

Đối chiếu 2026, cảnh báo này **vẫn đúng, và còn nên nói mạnh hơn**:

- **Ngân hàng Nhà nước chưa cấp phép cho bất kỳ sàn Forex nào tại Việt Nam.** Hoạt động sàn Forex
không thuộc phạm vi hoạt động ngoại hối được phép. Theo Pháp lệnh Ngoại hối, **chỉ tổ chức tín dụng
có giấy phép** mới được kinh doanh, cung ứng dịch vụ ngoại hối.
- **Chuyển tiền ra nước ngoài để chơi Forex bị coi là bất hợp pháp** — vì bản thân hoạt động này
không được phép, nên việc thanh toán, chuyển tiền cho nó cũng không hợp pháp.
- **Không được pháp luật Việt Nam bảo vệ.** Cá nhân nạp tiền vào sàn quốc tế, khi xảy ra tranh chấp
hoặc bị chiếm đoạt, gần như không có cửa đòi lại: *"người dân nộp tiền thật, nhận lại tiền ảo hoặc
các sản phẩm không có thực."*
- **Và đây là chỗ hai lesson gặp nhau:** rất nhiều "sàn Forex/CFD" ở Việt Nam thực chất là **Ponzi
núp bóng** — cơ quan quản lý gọi thẳng là *"ma trận huy động vốn 4.0 trên danh nghĩa sàn Forex"*.
Nghĩa là cái nguy hiểm loại 1 (lừa đảo) thường **đội lốt** cái nguy hiểm loại 2 (công cụ rủi ro
cao). Người phân biệt được hai loại ở [mục 1](#1-hai-loại-nguy-hiểm-khác-loại-nhau) sẽ hỏi đúng câu:
*đây là CFD thật với đòn bẩy, hay chỉ là Ponzi mượn chữ "Forex"?*

Khung tài sản số mới (Luật Công nghiệp công nghệ số, Quốc hội thông qua 6/2025) lần đầu định nghĩa
tài sản số, nhưng **chưa** có quy định chi tiết cho phái sinh kiểu CFD hay futures. Nên tình trạng
"chưa được cấp phép" của sách vẫn là bức tranh đúng tính đến ngày tra.

---

## 9. Ráp lại: hai loại nguy hiểm, hai cách phòng

Cả Unit 4 khép lại ở đây, và nó nối vòng về đúng khung ba lớp bảo vệ của
[bài 9 mục 1](bai_09_bao_ve.md#1-ba-lớp-bảo-vệ--khung-mà-sách-không-dựng): có một khoản tiền sắp mất
đi, ai chịu. Với lừa đảo, câu trả lời là **bạn chịu hết, và không đòi lại được** — nên lớp phòng duy
nhất là **đừng để tiền vào**.


|                 | Ponzi (loại 1)                                  | CFD / Forex (loại 2)                               |
| --------------- | ----------------------------------------------- | -------------------------------------------------- |
| Phải làm gì     | **tránh hoàn toàn**                             | hiểu đòn bẩy; biết là chưa cấp phép ở VN           |
| Câu hỏi chốt    | lợi nhuận đến từ hoạt động thật nào?            | giá đi ngược bao nhiêu % là tôi cháy?              |
| Phép thử        | nhân lãi ra cả năm (bài 10)                     | 1 / đòn bẩy (mục 7)                                |
| Vì sao vẫn dính | tham lam, lạc quan, ảo tưởng kiểm soát (bài 10) | đánh giá quá cao khả năng "canh" của mình (bài 12) |


Và điều quan trọng nhất, đúng như [bài 10](bai_10_tai_chinh_hanh_vi.md) đã đặt nền: nạn nhân lừa đảo
**không phải người ngu** — sách tự nhận *"người có tiền thường không ngu ngốc"* (tr. 52). Lừa đảo
đánh vào phản xạ mà ai cũng có. Nên câu trả lời không bao giờ là *"tại họ dại"*, mà là dựng sẵn quy
tắc cứng từ lúc đầu óc còn tỉnh — để lúc gặp lời chào hấp dẫn thì không phải quyết định nữa.

Bài tiếp theo — **bài 12** — quay về phía đầu tư hợp pháp: rủi ro
là gì, khẩu vị rủi ro của bạn đo bằng cách nào, và phân bổ tài sản ra sao cho khớp với nó.

---

## 10. Tự thử

Sửa [`thuc_hanh/bai-11-nhan-dien-lua-dao.py`](../thuc_hanh/bai-11-nhan-dien-lua-dao.py) rồi chạy lại.

1. **Ponzi hết người sau bao nhiêu vòng?** Sách nói "hai người sau nuôi một người trước". Nếu là
 **ba** người thì sao — số vòng để vượt dân số Việt Nam tăng hay giảm? In bảng cho tỷ lệ 2, 3, 5.
2. **Nhân lãi ra cả năm.** Viết hàm nhận lãi theo tháng, trả lãi cả năm. Thử với các lời chào có
 thật ngoài đời bạn từng nghe. Cái nào vượt 791%/năm của ví dụ "20%/tháng"?
3. **Đòn bẩy nào là cháy.** In bảng `1 / đòn bẩy` cho 1:5 tới 1:1000. Ở mức nào thì một biến động giá
 0,5% trong ngày (rất thường) đủ để mất trắng?
4. **Ponzi hay kim tự tháp?** Lấy ba mô tả lừa đảo bất kỳ (tự bịa hoặc từ tin tức) và phân loại từng
 cái bằng đúng hai câu hỏi ở mục 3: lợi nhuận từ đâu, và tôi kiếm tiền từ sản phẩm hay từ tuyển
 người?
5. **Bẫy đội lốt.** Một "sàn Forex" hứa lãi 15%/tháng, cam kết không rủi ro, cho rút thử 1 triệu lúc
 đầu, kiếm thêm hoa hồng nếu rủ bạn bè. Nó là CFD thật hay Ponzi mượn chữ "Forex"? Chỉ ra từng dấu
 hiệu.

---

## 11. Từ điển thuật ngữ


| Tiếng Việt            | Tiếng Anh                 | Nghĩa                                                                                          |
| --------------------- | ------------------------- | ---------------------------------------------------------------------------------------------- |
| Mô hình Ponzi         | Ponzi scheme              | Lừa đảo lấy tiền người sau trả người trước; **không** có hoạt động kinh doanh thật — C2 tr. 48 |
| Kim tự tháp / đa cấp  | Pyramid scheme / MLM      | Trả hoa hồng **theo tầng** cho việc tuyển người; khác Ponzi                                    |
| Schemer               | —                         | Kẻ chủ mưu dựng và điều hành Ponzi — C2 tr. 50                                                 |
| "Too good to be true" | —                         | Tốt tới mức khó tin thì đừng tin; phép thử của tác giả — C2 tr. 52                             |
| CFD                   | Contract for Difference   | Hợp đồng chênh lệch; cá cược vào chênh lệch giá, không sở hữu tài sản — C2 tr. 56              |
| Forex                 | Foreign Exchange          | Thị trường ngoại hối; giao dịch bán lẻ ở VN thực chất là CFD tỷ giá — C2 tr. 55                |
| Hàng hoá phái sinh    | Derivative                | Sản phẩm có giá dựa trên giá của một tài sản cơ sở — C2 tr. 56                                 |
| Đòn bẩy               | Leverage                  | Điều khiển vị thế lớn bằng vốn nhỏ, phần còn lại vay môi giới — C2 tr. 56                      |
| Giao dịch ký quỹ      | Margin trading            | Tên khác của giao dịch đòn bẩy — C2 tr. 56                                                     |
| Cháy tài khoản        | Margin call / liquidation | Vốn ký quỹ mất hết, vị thế bị đóng; xảy ra khi giá ngược `1/đòn bẩy`                           |


---

## 12. Câu hỏi tự kiểm tra

1. Ponzi và CFD nguy hiểm theo hai cách khác nhau thế nào? Cái nào phải tránh hẳn, cái nào phải hiểu?
2. Định nghĩa Ponzi của sách. Câu nào là cốt lõi của cả mô hình?
3. Ba thành phần của mô hình Ponzi theo sách là gì, mỗi vai làm gì?
4. Vì sao gọi Ponzi là "đa cấp kim tự tháp" là sai? Phân biệt hai mô hình.
5. Dùng chính ba thành phần của sách, chỉ ra vai nào là Ponzi thuần, vai nào là kim tự tháp.
6. Charles Ponzi chạy mô hình loại nào? Vì sao gọi ông là "tổ nghề kim tự tháp đa cấp" là gán sai?
7. Nếu mỗi người được trả cần hai người mới nuôi, sau bao nhiêu vòng thì vượt dân số Việt Nam? Thế
 giới? Viết công thức.
8. Vì sao sụp là chắc chắn chứ không phải xui rủi?
9. Hai câu hỏi mạnh nhất để nhận diện Ponzi là gì?
10. Vì sao chỉ biết dấu hiệu vẫn không đủ để không dính? (nối với bài 10)
11. CFD là gì? Khi giao dịch CFD bạn có sở hữu tài sản không?
12. Sách viết sai tên CFD ở chỗ nào? Bản đúng là gì và nghĩa khác ra sao?
13. Viết công thức mức giá đi ngược làm cháy tài khoản. Ở đòn bẩy 1:100 là bao nhiêu phần trăm?
14. Vì sao "cháy tài khoản" tệ hơn "lỗ 50%" xét theo bất đối xứng lỗ–lãi của bài 10?
15. Tính đến 2026, Forex/CFD có được cấp phép ở Việt Nam không? Chuyển tiền ra nước ngoài để chơi thì sao?
16. Vì sao nhiều "sàn Forex" ở VN thực chất là Ponzi? Câu hỏi nào tách được hai thứ?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 11 — NHẬN DIỆN LỪA ĐẢO: PONZI VÀ CFD             C2 tr. 47-57       ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  HAI LOẠI NGUY HIỂM KHÁC LOẠI:                                           ║
║     PONZI = LỪA ĐẢO, không có sòng bạc nào -> TRÁNH HẲN                  ║
║     CFD   = công cụ THẬT, đòn bẩy giết -> phải HIỂU trước                ║
║     sách: Ponzi "hình thức lừa đảo" · CFD "không phải lừa đảo,           ║
║           tuy nhiên độ rủi ro rất cao"                                   ║
║                                                                          ║
║  PONZI (tr.48)  lấy tiền người sau trả người trước, KHÔNG hoạt động thật ║
║     3 vai: Schemer (chủ mưu) · Investor ("gà", thụ động) ·               ║
║        Ponzi Introducing Investor (ăn hoa hồng tuyển người)              ║
║     từ khoá "HỨA HẸN" · trả bằng BÁO CÁO không bằng tiền ·               ║
║        hết người mới thì "Schemer biến mất cùng số tiền"                 ║
║     chốt: "Too good to be true" (tr.52)                                  ║
║                                                                          ║
║  [đính chính] PONZI ≠ ĐA CẤP KIM TỰ THÁP (tr.48, 49)                     ║
║     Ponzi: 1 kẻ trung tâm, nạn nhân THỤ ĐỘNG                             ║
║     kim tự tháp: hoa hồng THEO TẦNG, người tham gia đi TUYỂN người       ║
║     chính 3 vai: vai 1+2 = Ponzi, vai 3 = kim tự tháp.                   ║
║     Charles Ponzi chạy Ponzi THUẦN, không phải MLM                       ║
║                                                                          ║
║  [bổ sung] VÌ SAO CHẮC CHẮN SỤP — phép nhân sách không làm               ║
║     "2 người sau nuôi 1 người trước" -> mỗi vòng GẤP ĐÔI                 ║
║     số người vòng n = 2^(n-1)                                            ║
║        27 vòng > dân số VN · 33 vòng > dân số thế giới                   ║
║     câu hỏi không phải "có sụp không" mà "sụp vòng thứ mấy"              ║
║                                                                          ║
║  NHẬN DIỆN: 2 câu mạnh nhất                                              ║
║     (1) nhân lãi ra cả năm — cả nền KT làm nổi không? (bài 10)           ║
║     (2) lợi nhuận đến từ HOẠT ĐỘNG THẬT nào?                             ║
║     biết dấu hiệu vẫn dính -> dựng QUY TẮC CỨNG, "sửa hệ thống"          ║
║                                                                          ║
║  CFD (tr.56)  cá cược CHÊNH LỆCH GIÁ, KHÔNG sở hữu tài sản; phái sinh    ║
║     [đính chính] "Contract for DIFFERENCE", không phải "different"       ║
║     [bổ sung] ĐÒN BẨY GIẾT: giá ngược 1/đòn bẩy là MẤT TRẮNG             ║
║        1:100 -> chỉ 1% là cháy tài khoản (đòn bẩy = VAY, bài 8)          ║
║        cháy = lỗ 100% = cần lãi VÔ HẠN để về (bài 10)                    ║
║                                                                          ║
║  [2026] FOREX/CFD Ở VN: NHNN CHƯA cấp phép sàn Forex nào                 ║
║     chuyển tiền ra nước ngoài để chơi = bất hợp pháp; không được bảo vệ  ║
║     nhiều "sàn Forex" thực chất là PONZI núp bóng ("ma trận HĐV 4.0")    ║
║                                                                          ║
║  NẠN NHÂN KHÔNG NGU — lừa đảo đánh vào phản xạ ai cũng có (bài 10)       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn.
  - **Unit 4, Lesson 4 — *Mô hình Ponzi* (tr. 47–53):** định nghĩa Ponzi và câu *"không hề có hoạt
  động kinh doanh - đầu tư nào diễn ra"* (tr. 48); Charles Ponzi sinh 1882, *"15 triệu USD"*,
  *"6 ngân hàng phá sản"*, *"tổ nghề của mô hình kim tự tháp đa cấp"* (tr. 49); ba thành phần
  Schemer / Investor / Ponzi Introducing Investor (tr. 50); bảy dấu hiệu nhận diện (tr. 50–51);
  phương thức hoạt động và *"trích tiền từ hai người đến sau"* (tr. 51–52); *"Too good to be true"*
  (tr. 52) — đều chép từ đây.
  - **Unit 4, Lesson 5 — *CFD là gì?* (tr. 55–57):** *"bước đệm"* (tr. 55); Forex thực chất là giao
  dịch CFD (tr. 55–56); định nghĩa *"Contracts for Difference - Hợp đồng chênh lệch"* và hai đặc
  điểm phái sinh + đòn bẩy (tr. 56); cơ chế ký quỹ (tr. 56); cảnh báo *"không phải lừa đảo, tuy
  nhiên độ rủi ro rất cao… Forex hiện tại chưa được sự cho phép"* (tr. 57).
  - **[đính chính] tên CFD:** blog ở tr. 54 viết *"contract for different"*; bản đúng *"Contract for
  Difference"* xác nhận ngay tại tr. 56 của chính sách.
- **[2026] pháp lý Forex/CFD ở Việt Nam**, tra ngày **10/09/2026**: Ngân hàng Nhà nước chưa cấp phép
sàn Forex nào; theo Pháp lệnh Ngoại hối chỉ tổ chức tín dụng có phép mới được kinh doanh ngoại hối;
chuyển tiền ra nước ngoài cho giao dịch Forex là bất hợp pháp; nhiều sàn là *"ma trận huy động vốn
4.0"* núp bóng.
  - [*"Ma trận" Forex/CFD (kỳ cuối): Cảnh báo tiếp tay cho các hoạt động phi pháp — VnEconomy](https://vneconomy.vn/ma-tran-forex-cfd-ky-cuoi-canh-bao-tiep-tay-cho-cac-hoat-dong-phi-phap.htm)
  - [Cảnh báo nóng từ Ngân hàng Nhà nước, cách truy quét sàn giao dịch ngoại hối bất hợp pháp — Dân Việt/etime](https://etime.danviet.vn/canh-bao-nong-tu-ngan-hang-nha-nuoc-tiet-lo-cach-truy-quet-san-forex-bat-hop-phap-d1370699.html)
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-11-nhan-dien-lua-dao.py`](../thuc_hanh/bai-11-nhan-dien-lua-dao.py).
Hai bảng số của bài do tệp này tính, chạy hai lần ra giống hệt nhau. Công thức một dòng để tự kiểm:
số người vòng n `= 2^(n-1)` (mục 4), mức giá cháy tài khoản `= 1 / đòn bẩy` (mục 7). Các con số dân
số (VN ~100 triệu, thế giới ~8 tỷ) là mốc tròn để so, không phải số liệu chính xác.
- **Con số của sách chưa đối chiếu nguồn độc lập:** *"15 triệu USD"* và *"6 ngân hàng phá sản"* ở
tr. 49 nêu nguyên văn, đánh dấu là số của sách.
- **Liên hệ chéo:**
  - Khung thiên kiến giải thích vì sao người có tiền vẫn dính, phép thử "nhân lãi ra cả năm", bất đối
  xứng lỗ–lãi: [bài 10](bai_10_tai_chinh_hanh_vi.md), đặc biệt
  [mục 5](bai_10_tai_chinh_hanh_vi.md#5-sự-tham-lam--khi-quá-tốt-để-là-thật-vẫn-thắng-ở-trang-52),
  [mục 8](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại).
  - Đòn bẩy là một khoản vay:
  [bài 8](bai_08_vay_va_tra_no.md).
  - Khung "ai chịu khoản tiền sắp mất":
  [bài 9 mục 1](bai_09_bao_ve.md#1-ba-lớp-bảo-vệ--khung-mà-sách-không-dựng).
  - Khẩu vị rủi ro (tr. 54, *"một vốn bốn mươi lời"*, 5%/tháng): **bài 12**.

<!-- BAN-DO -->

**Bản đồ khoá học**


| #      | Bài                                                                                       | Nguồn                           | Vòng |
| ------: | ----------------------------------------------------------------------------------------- | ------------------------------- | :----: |
| 0      | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md)                                                | —                               | 2    |
| 1      | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md)                              | C1 tr. 4–6                      | 1    |
| 2      | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md)           | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1    |
| 3      | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md)                   | C1 tr. 7–10                     | 1    |
| 4      | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md)                | C1 tr. 16–24                    | 1    |
| 5      | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md)               | C2 tr. 4–13                     | 1    |
| 6      | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách                      | 1    |
| 7      | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md)  | C2 tr. 18–28                    | 1    |
| 8      | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md)                                     | C2 tr. 29–38                    | 1    |
| 9      | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md)                              | C2 tr. 39–47                    | 1    |
| 10     | [**[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai](bai_10_tai_chinh_hanh_vi.md)   | ngoài sách                      | 2    |
| **11** | **Nhận diện lừa đảo: Ponzi và CFD** ← *bạn đang ở đây*                                    | C2 tr. 47–57                    | 1    |
| 12     | Rủi ro, khẩu vị rủi ro, phân bổ tài sản                                                   | C1 tr. 25–33                    | 1    |
| 13     | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF                                         | C2 tr. 58–67                    | 2    |
| 14     | Mục tiêu SMART và ráp lại thành kế hoạch                                                  | C1 tr. 34–40                    | 1    |


Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->

