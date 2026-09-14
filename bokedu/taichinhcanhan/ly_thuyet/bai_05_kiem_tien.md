# Bài 5 — Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người

> [!info] Về bài này
> Bài học dựa trên **toàn bộ Unit 1 của Class 2** — C2 tr. 4–13. Mười trang, ba lesson: đây là
> unit dài nhất mà khoá học gộp vào một bài.
> **Cần đọc trước:** [Bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md) — bài 4 tính ra lớp vô hình
> chiếm **94%** tháp tài sản rồi hỏi *"đang làm gì để lớp đáy dày lên?"*. Bài này là câu trả lời.
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
> **Code:** [`thuc_hanh/bai-05-kiem-tien.py`](../thuc_hanh/bai-05-kiem-tien.py)
> — ba phép tính mà Unit 1 gợi ra nhưng không làm: bóc ví dụ gia sư ở tr. 6, dựng lại biểu đồ hai
> nguồn vốn ở tr. 11, và kiểm câu *"không mô hình nào lợi thế hơn"* ở tr. 13.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).

---

## Mục lục

<!-- MUC-LUC -->
- [1. Vì sao chúng ta được trả tiền — sách đặt hai câu trả lời](#1-vì-sao-chúng-ta-được-trả-tiền--sách-đặt-hai-câu-trả-lời)
- [2. [đính chính] Hai góc nhìn ấy phủ định nhau, và sách không nói](#2-đính-chính-hai-góc-nhìn-ấy-phủ-định-nhau-và-sách-không-nói)
- [3. Công thức Thu nhập = Giá trị × Thời gian × Quy mô](#3-công-thức-thu-nhập--giá-trị--thời-gian--quy-mô)
- [4. Kim tứ đồ và bốn quy tắc](#4-kim-tứ-đồ-và-bốn-quy-tắc)
- [5. [bổ sung] Quy tắc 3 và quy tắc 4 kéo về hai hướng](#5-bổ-sung-quy-tắc-3-và-quy-tắc-4-kéo-về-hai-hướng)
- [6. Vốn con người và vốn tài chính](#6-vốn-con-người-và-vốn-tài-chính)
- [7. [bổ sung] Cả kế hoạch tài chính là một phép chuyển đổi](#7-bổ-sung-cả-kế-hoạch-tài-chính-là-một-phép-chuyển-đổi)
- [8. Bốn mô hình thu nhập](#8-bốn-mô-hình-thu-nhập)
- [9. [đính chính] "Không có mô hình nào lợi thế hơn" — lãi kép nói khác](#9-đính-chính-không-có-mô-hình-nào-lợi-thế-hơn--lãi-kép-nói-khác)
- [10. Tự thử](#10-tự-thử)
- [11. Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
- [12. Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Vì sao chúng ta được trả tiền — sách đặt hai câu trả lời

Class 2 mở đầu bằng một quan sát xã hội, nói thẳng không rào đón:

> [!quote]
> *"Càng kiếm nhiều tiền người ta càng được những người lạ ngưỡng mộ… Sự tôn trọng thường được ban
> phát theo thu nhập. Hệ quả là, nếu bạn không có khả năng tài chính đủ tốt, bạn sẽ khó lòng khiến
> xã hội coi trọng cá tính và quan điểm của bạn."* — C2 tr. 4

Đây là câu **mô tả** một chuẩn mực, không phải câu tán thành nó. Nó cùng họ với đoạn *"nhìn lên
những người hơn mình"* ở [bài 3](bai_03_ghi_chep_chi_tieu.md#2-phản-biện-của-chính-sách-và-câu-trả-lời);
**bài 10** gom cả cụm lại.

Rồi sách đặt câu hỏi thật của lesson — *"chính xác thì ta được trả tiền cho điều gì?"* — và đưa ra
**hai câu trả lời**, đánh số rõ ràng.

### Góc nhìn một: chủ nghĩa tư bản — bạn được trả cho **giá trị**

> [!quote]
> *"Mức lương một người được xác định nhờ mức độ đóng góp của họ cho xã hội."* — C2 tr. 5

Sách dẫn Jim Rohn để tách **thời gian** khỏi **giá trị**:

> [!quote]
> *"Một cách sai lầm, 'người đàn ông' sẽ nói: 'Tôi kiếm được 20 đôla mỗi giờ'. Điều đó không đúng!
> Nếu điều đó đúng, anh ta chỉ việc ở nhà để nhận tiền được gửi đến. Không, anh ta được trả 20 đô la
> cho **giá trị được đưa vào** một giờ đồng hồ mà anh ta làm việc. Trả lương theo giờ chỉ đơn giản
> là một cách thức tiện lợi để đo lường giá trị đã được tính toán trước."* — C2 tr. 5

Lập luận *"nếu đúng thì anh ta chỉ việc ở nhà để nhận tiền"* là một phép thử sắc: nếu tiền trả cho
thời gian thì thời gian nào cũng được trả. Nó không phải vậy.

Kết luận của góc nhìn này là một mệnh lệnh: **hãy trở nên giá trị hơn.**

> [!quote]
> *"Nếu bạn cung cấp nhiều giá trị hơn, bạn nhận lại nhiều hơn. Từ khoá là 'phát triển bản thân'."*
> — C2 tr. 6

### Góc nhìn hai: kinh tế học — bạn được trả cho **sự hiếm**

> [!quote]
> *"Lương được xác định **không phải nhờ giá trị đóng góp**, mà nhờ số người có khả năng và sẵn sàng
> làm công việc đó, trong khi những người khác không muốn hoặc không thể thực hiện."* — C2 tr. 6

> [!quote]
> *"Nếu nhiều người có thể làm tác vụ này, mức độ cạnh tranh cao, **dù công việc phức tạp đến đâu**,
> tin buồn là số tiền bạn có thể nhận sẽ không nhiều."* — C2 tr. 6

Và câu chốt:

> [!quote]
> *"Ở góc nhìn này, không có chỗ nào phán xét giá trị của công việc. Lương chỉ đơn giản là độ chênh
> lệch giữa cầu và cung."* — C2 tr. 6

---

## 2. [đính chính] Hai góc nhìn ấy phủ định nhau, và sách không nói

Đọc lại hai câu chủ đề, đặt cạnh nhau:

```
   góc nhìn 1 (tr. 5)   "Mức lương được xác định NHỜ mức độ đóng góp"
   góc nhìn 2 (tr. 6)   "Lương được xác định KHÔNG PHẢI nhờ giá trị đóng góp"
```

Câu thứ hai **phủ định thẳng** câu thứ nhất — bằng đúng chữ *"không phải"*. Đây không phải hai khía
cạnh bổ sung cho nhau; đây là hai mệnh đề mâu thuẫn. Và sách kết thúc lesson bằng:

> [!quote]
> *"Hy vọng qua nội dung này, bạn đã hiểu vì sao chúng ta được trả tiền."* — C2 tr. 6

Không có phần hoà giải. Người đọc được đưa hai câu trả lời loại trừ nhau rồi chúc hiểu.

### Chỗ này quan trọng vì hai góc nhìn cho hai lời khuyên khác nhau

| | Góc nhìn 1 | Góc nhìn 2 |
| --- | --- | --- |
| Lương do gì quyết định | giá trị bạn tạo ra | có bao nhiêu người làm được việc đó |
| Muốn tăng lương thì | **giỏi hơn** | **hiếm hơn** |
| Nếu bạn rất giỏi nhưng nghề đông người | vẫn nên được trả cao | sẽ **không** được trả cao |
| Sách gọi là | *"phát triển bản thân"* | *"chênh lệch giữa cầu và cung"* |

Hai lời khuyên đó **không phải một**. Giỏi hơn trong một nghề đông người thì lương không nhúc
nhích — chính sách thừa nhận điều này ở tr. 6: *"dù công việc phức tạp đến đâu"*.

### Cách hoà giải, và sách có sẵn nó ở lesson sau

Hai mệnh đề đúng ở hai chỗ khác nhau:

> [!note]
> **Giá trị quyết định TRẦN** — lương của bạn không thể vượt quá giá trị bạn tạo ra, nếu không
> người thuê bạn lỗ.
>
> **Sự hiếm quyết định BẠN ĐƯỢC BAO NHIÊU PHẦN của cái trần đó** — nếu ngoài kia có mười người làm
> được y hệt, bạn nhận phần sát đáy; nếu chỉ có bạn, bạn nhận phần sát trần.

Điều dễ chịu: **chính cuốn sách chốt vấn đề này ở quy tắc 3 của lesson sau**, chỉ là nó không nhắc
lại lesson 1 lúc chốt:

> [!quote]
> *"dù bạn ở nhóm nào, bí quyết thành công/giàu có là bạn cần trở thành **số ít chuyên gia** trong
> lĩnh vực của mình."* — C2 tr. 10

*"Số ít"* là góc nhìn 2. *"Chuyên gia"* là góc nhìn 1. **Câu này là bản hoà giải, và nó nằm cách
chỗ mâu thuẫn đúng bốn trang** — chỉ có điều sách không nói ra rằng nó đang hoà giải cái gì.

---

## 3. Công thức Thu nhập = Giá trị × Thời gian × Quy mô

> [!quote]
> *"Nếu chị B muốn được trả nhiều tiền hơn, công thức là: **Thu nhập = Giá trị × Thời gian ×
> Quy mô**"* — C2 tr. 5

Công thức này **là của sách**, không phải của Jim Rohn — Jim Rohn chỉ nói về "giá trị đưa vào một
giờ", không đưa công thức nào. Nó gọn và có ích, và có một tính chất đáng để ý: **phép nhân**. Một
thừa số bằng 0 thì cả tích bằng 0.

| Thừa số | Sách nói | Trần |
| --- | --- | --- |
| **Thời gian** | *"Làm nhiều giờ hơn"* | *"hữu hạn, maximum 24h/ngày/người"* |
| **Quy mô** | *"Mang giá trị đến nhiều người hơn"* | không nêu trần |
| **Giá trị** | *"Nhân tố quan trọng nhất theo góc nhìn của chủ nghĩa tư bản"* | không nêu trần |

Sách chỉ đặt trần cho **thời gian**. Đó là chỗ dẫn tới quy tắc 4 của lesson sau — *"đòn bẩy thời
gian"* (mục 5).

### [bổ sung] Ví dụ gia sư của sách chứng minh nhiều hơn nó định chứng minh

> [!quote]
> *"Ví dụ bạn dạy gia sư 1 kèm 1, học phí 100 ngàn/buổi. Một giáo viên dạy trung tâm, lớp 15 học
> sinh, 20 ngàn/học sinh/buổi. Giáo viên dạy quy mô lớn hơn thu về 300 ngàn, gấp 3 lần bạn **khi
> thời gian và giá trị tương đương nhau**."* — C2 tr. 6

Bóc con số của chính sách ra:

```
   1 kèm 1      1 học sinh × 100k  =  100k / buổi
   trung tâm   15 học sinh ×  20k  =  300k / buổi

   quy mô           × 15
   giá mỗi học sinh ×  0,2      (tức CHIA 5)
   ─────────────────────────
   thu nhập         ×  3        <- con số "gấp 3" của sách
```

Câu *"giá trị tương đương nhau"* không đứng vững trước chính con số của sách: giá mỗi học sinh
**tụt từ 100k xuống 20k**. Quy mô nhân 15, giá trị mỗi người chia 5, còn lại đúng 3.

Điều này **không làm hỏng công thức — nó làm công thức sâu hơn.** Ba thừa số không độc lập với
nhau. Mở rộng quy mô hầu như luôn phải trả bằng giá trị trên mỗi người: lớp 15 em thì không ai được
kèm riêng.

Và nếu giá tụt nhanh hơn nữa thì quy mô lớn **không cứu được**:

| Số học sinh | Giá mỗi em | Thu nhập/buổi | So với 1 kèm 1 |
| ---: | ---: | ---: | --- |
| 1 | 100k | 100k | × 1,0 |
| 5 | 40k | 200k | × 2,0 |
| 15 | 20k | 300k | × 3,0 |
| 30 | 8k | 240k | × 2,4 |
| 50 | 2k | 100k | × 1,0 — **hoà** |
| 80 | 1k | 80k | × 0,8 — **thua** |

Người dạy 50 học sinh một lúc có thể kiếm **đúng bằng** người kèm một em. Câu hỏi đúng không phải
*"làm sao mở rộng quy mô"* mà là **quy mô tăng có nhanh hơn giá trị giảm không**.

---

## 4. Kim tứ đồ và bốn quy tắc

> [!quote]
> *"Cashflow quadrant (Kim tứ đồ) là một khái niệm được Robert Kiyosaki đưa ra trong bộ sách Rich
> Dad. Mô hình này thể hiện 4 cách khác nhau để tạo ra tiền bạc, tương ứng là 4 nhóm người."*
> — C2 tr. 7

```
                 │
        E        │        B
   Employee      │   Business Owner
   "họ có một    │   "làm chủ một hệ thống
    công việc"   │    và người khác làm việc cho họ"
   ──────────────┼──────────────────────────────
        S        │        I
   Self-employed │      Investor
   "tự làm chủ   │   "tiền làm việc cho họ"
    một công việc"│
                 │
   ◄─ bán THỜI GIAN ─►│◄─ dùng thời gian và tiền của NGƯỜI/THỨ khác ─►
                                                              C2 tr. 7
```

Bốn quy tắc sách rút ra:

| | Quy tắc | Trang |
| ---: | --- | --- |
| **1** | Phần lớn mọi người thuộc nhóm E — kèm ba lời khuyên: *làm đúng việc*, *làm hiệu quả*, *làm tận lực* | tr. 7–9 |
| **2** | Mỗi người đều có thể kiếm tiền ở **cả bốn** nhóm | tr. 9–10 |
| **3** | Bạn có thể **giàu hoặc nghèo ở cả bốn** nhóm | tr. 10 |
| **4** | Nên học cách kiếm tiền ở **phía bên phải** — vì *đòn bẩy thời gian* | tr. 10–11 |

### Quy tắc 1 — thang bốn bậc cho người làm công

Phần *"làm hiệu quả"* là một thang bốn bậc, viết rất gọn:

> [!quote]
> - *"**Làm cầm chừng** để giữ công việc. Họ không thích đi làm, mơ mộng một ngày nào đó sẽ 'nhảy
>   việc', yêu ngày lĩnh lương và ghét thứ hai đầu tuần."*
> - *"**Làm đúng với số tiền được trả.** Những người này sợ 'lỗ' công sức bỏ ra, nếu công ty trả 10
>   đồng thì họ làm đúng 10 đồng."*
> - *"**Làm việc một cách chuyên nghiệp** và có trách nhiệm."*
> - *"**Làm việc với tinh thần làm chủ**: trăn trở, nhiệt huyết với công ty, san sẻ gánh nặng với
>   sếp. Đây là cái đích bạn nên hướng đến."* — C2 tr. 8

Bậc thứ hai đáng dừng lại, vì nó là bẫy đúng theo lập luận của mục 2: *"công ty trả 10 đồng thì làm
đúng 10 đồng"* nghe rất công bằng, nhưng nó khoá bạn ở mức giá trị hiện tại. Không có cách nào
chứng minh bạn đáng 15 đồng nếu bạn chưa bao giờ làm quá 10.

Sách cũng rất sòng phẳng ở phần *"làm tận lực"*:

> [!quote]
> *"Điều này không sai. Tận lực không phải điều kiện bắt buộc. Có những người đang tận lực. Có người
> không. Lựa chọn là ở bạn!"* — C2 tr. 9

Và nó **hứa một lý do rồi giữ lời**: tr. 9 viết *"(Có một lý do chính đáng cho việc tại sao chúng ta
nên tận lực làm việc, tôi sẽ nói trong bài học tiếp theo)"*, rồi tr. 13 quay lại trả nợ. Lý do đó
là mục 6 và 7 của bài này.

### Quy tắc 2 — ví dụ anh Quyết

Ví dụ ở tr. 10 rất tốt vì nó cụ thể: một bác sĩ nội khoa **(E)**, mở phòng khám tối và cuối tuần
**(S)**, cùng bạn mở chuỗi quầy thuốc tự vận hành **(B)**, mua cổ phiếu bệnh viện nơi mình làm
**(I)**. Bốn nhóm, một người.

Nó cũng cho lằn ranh B/S sắc nhất của cả lesson:

> [!quote]
> *"Trong khi nhóm B làm chủ hệ thống kinh doanh thì nhóm S là một phần mắt xích của hệ thống. Những
> người nhóm B có thể **rời bỏ công việc kinh doanh từ 1 năm** mà khi quay lại, hệ thống vẫn vận
> hành hiệu quả và phát triển mà không cần sự có mặt của họ. Còn nhóm S thì không."* — C2 tr. 9

Đây là một **phép thử** chứ không phải một định nghĩa: nghỉ một năm, quay lại, còn gì không? Chủ
tiệm phở tự đứng bếp là **S**, dù có thuê mười nhân viên.

### Quy tắc 3 — chỗ sách phản biện chính Kiyosaki

Đây là đoạn sắc nhất của cả Unit, và đáng chú ý vì sách đang trình bày mô hình của Kiyosaki rồi
quay ra bác cách đọc phổ biến nhất của nó:

> [!quote]
> *"Nhiều người cho rằng phải ở nhóm B hoặc nhóm I mới trở nên giàu có… Suy nghĩ vậy là sai lầm do
> ảnh hưởng bởi **thiên kiến sống sót**. Truyền thông cho chúng ta thấy rất nhiều gương doanh nhân -
> nhà đầu tư thành công nhưng đằng sau đó là vô số trường hợp thất bại không hề được nhắc đến."*
> — C2 tr. 10

> [!quote]
> *"Thực tế, ở phía bên phải Kim tứ đồ, **xác suất khởi nghiệp thất bại rất cao, và hầu hết nhà đầu
> tư thua lỗ**."* — C2 tr. 10

Đây là lần duy nhất trong hai tập sách mà một thiên kiến nhận thức được **gọi đúng tên**.
**Bài 10** lấy đoạn này làm điểm tựa.

---

## 5. [bổ sung] Quy tắc 3 và quy tắc 4 kéo về hai hướng

Đọc liền hai quy tắc:

```
   QUY TẮC 3 (tr. 10)   phía bên phải: "xác suất khởi nghiệp thất bại rất cao,
                        và hầu hết nhà đầu tư thua lỗ"
                        => ô nào không quyết định kết quả; CHUYÊN MÔN mới quyết định

   QUY TẮC 4 (tr. 10)   "Bạn NÊN học cách kiếm tiền ở phía bên phải"
                        => ô nào có quyết định
```

Một trang, hai quy tắc, hai hướng. Sách không nhắc tới sự căng đó.

Chúng **hoà giải được**, nhưng phải nói ra điều mà sách để ngầm: **hai quy tắc nói về hai đại lượng
khác nhau.**

| | Quy tắc 3 nói về | Quy tắc 4 nói về |
| --- | --- | --- |
| Đại lượng | **xác suất** thành công | **trần** của thu nhập |
| Kết luận | bên phải, xác suất **thấp hơn** | bên phải, trần **cao hơn** |
| Vì | khởi nghiệp hay thất bại | *"đòn bẩy thời gian"* |

Lập luận của quy tắc 4 nằm ở tr. 10–11, và nó quay về đúng công thức ở mục 3:

> [!quote]
> *"Với nhóm E và S, càng kiếm được nhiều tiền càng phải bỏ ra nhiều thời gian của bản thân cho công
> việc… Trong khi nhóm B sử dụng thời gian và giá trị của **người khác**, còn nhóm I dùng **tiền** để
> sinh ra tiền. Thời gian là nguồn lực hữu hạn."* — C2 tr. 11

Nói bằng công thức của mục 3: bên trái, thừa số **Thời gian** bị chặn ở 24 giờ và chính bạn phải
cung cấp nó. Bên phải, thừa số ấy do người khác hoặc do tiền cung cấp, nên trần bị gỡ bỏ.

**Vậy phát biểu đầy đủ là:** bên phải có trần cao hơn *và* xác suất thấp hơn. Đó là một đánh đổi,
không phải một nâng cấp — và nó khớp với quy tắc 3: cái quyết định bạn ở phía nào của xác suất ấy
là **có phải "số ít chuyên gia" hay không**, chứ không phải bạn đứng ở ô nào.

Đây cũng chính là bản hoà giải cho mâu thuẫn ở mục 2, chỉ nói ở tầng khác.

---

## 6. Vốn con người và vốn tài chính

> [!quote]
> *"Về cơ bản, tổng thu nhập của một người đến từ hai nguồn: **Vốn con người** (Human capital) và
> **Vốn tài chính** (Financial capital)."* — C2 tr. 11

| | Sách định nghĩa | Ở bài trước gọi là |
| --- | --- | --- |
| **Vốn con người** | *"tổng hòa của trình độ chuyên môn (kiến thức, kỹ năng) cùng với những mối quan hệ chất lượng"* | **lớp tài sản vô hình** — [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md#4-năm-lớp-từ-đáy-lên-đỉnh) |
| **Vốn tài chính** | *"tổng giá trị tài sản của bạn, trừ đi các khoản nợ"* | **tài sản ròng** — [bài 2](bai_02_do_hien_trang.md#1-hai-con-số-hai-câu-hỏi) |

Hai khái niệm này không mới trong khoá học — đây là lần thứ ba chúng xuất hiện dưới tên thứ ba. Cái
**mới** ở lesson này là mối quan hệ theo thời gian giữa chúng:

> [!quote]
> *"Trong đời người, hai nguồn vốn này có mối tương quan như trong biểu đồ:"* — C2 tr. 11

Rồi sách in một biểu đồ, và mô tả nó ở tr. 13:

> [!quote]
> *"vốn con người sẽ **giảm** theo thời gian, do tuổi trẻ là giai đoạn tốt nhất cho sự học hỏi và
> phát triển, nhưng càng lớn tuổi thì 'vốn' sẽ giảm đi liền với sức khỏe bản thân. **Đây chính là lý
> do cho việc tại sao bạn nên làm tận lực** như bài trước tôi đã nói."* — C2 tr. 13

Đó là lời hứa ở tr. 9 được trả: **tận lực khi trẻ, vì thứ bạn đang bán sẽ mất giá.**

---

## 7. [bổ sung] Cả kế hoạch tài chính là một phép chuyển đổi

Biểu đồ ở tr. 11 là hình ảnh, không kèm số. Dựng lại nó từ **một dòng thu nhập duy nhất** — người
đi làm từ 22 đến 60 tuổi, 20 triệu/tháng, tiết kiệm 20%, lợi suất thực 8%:

- **vốn con người tại tuổi $t$** = giá trị hiện tại của thu nhập **còn lại** — đúng phép định giá ở
  [bài 4 mục 6](bai_04_tai_san_tieu_san_thap_tai_san.md#6-đính-chính-định-giá-lớp-vô-hình-đo-cái-gì),
  nhưng có điểm dừng, đúng như C2 tr. 13 đòi hỏi
- **vốn tài chính tại tuổi $t$** = tiền đã tiết kiệm, cộng lãi

```
   tuổi   vốn con người   vốn tài chính     tổng      ▓ con người  ░ tài chính
  ──────────────────────────────────────────────────────────────────────────────
    22         2,80 tỷ            0 đ     2,80 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    26         2,74 tỷ         216 tr     2,96 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
    30         2,66 tỷ         510 tr     3,17 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
    34         2,56 tỷ         910 tr     3,47 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░
    38         2,45 tỷ        1,46 tỷ     3,90 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░
    42         2,25 tỷ        2,20 tỷ     4,45 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░
    46         1,98 tỷ        3,20 tỷ     5,18 tỷ   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░
    50         1,61 tỷ        4,58 tỷ     6,19 tỷ   ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    54         1,11 tỷ        6,44 tỷ     7,55 tỷ   ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    58          428 tr        8,98 tỷ     9,41 tỷ   ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    60               0       10,58 tỷ    10,58 tỷ   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

**Hai đường cắt nhau ở tuổi 43.** Trước đó bạn chủ yếu là một người có khả năng kiếm tiền; sau đó
bạn chủ yếu là một người có tiền.

Lúc 22 tuổi vốn con người chiếm **100%** — chưa tiết kiệm được đồng nào. Tỷ trọng đó tụt xuống dưới
**94%** (con số [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md#5-bổ-sung-làm-bài-tập-của-tr-24-và-kiểm-nguyên-tắc-của-tr-21)
tính cho tháp tài sản) ở tuổi **27**. Lúc 60 tuổi nó bằng **không**: không còn năm đi làm nào để
chiết khấu.

### Điều đó đổi cách hiểu về tiết kiệm

> [!note]
> **Cả kế hoạch tài chính cá nhân là một phép chuyển đổi: biến vốn con người thành vốn tài chính
> trước khi nó tiêu tan.**

Vốn con người **không thể giữ lại**. Nó hết hạn, và sách nói đúng cơ chế ở tr. 13 — sức khoẻ, tuổi
tác. Bạn không chọn được việc nó có mất đi hay không. Bạn chỉ chọn được **có đổi nó lấy thứ khác
không**.

Cùng dòng thu nhập ấy, tiết kiệm **0%**:

```
   vốn con người lúc 60 tuổi:        0 đồng   (hết hạn)
   vốn tài chính lúc 60 tuổi:        0 đồng   (không chuyển đổi gì)
   ─────────────────────────────────────────
   tổng:                             0 đồng
```

Người đó đã kiếm **9,12 tỷ** cả đời và kết thúc với hai số không. Không phải vì họ kiếm ít.

Nên tiết kiệm ở đây **không phải một đức tính**. Nó là **cơ chế chuyển đổi duy nhất bạn có**, và
**bài 7** sẽ nói về
tốc độ chuyển đổi đó.

Đây cũng là câu trả lời cho câu hỏi mà [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md#5-bổ-sung-làm-bài-tập-của-tr-24-và-kiểm-nguyên-tắc-của-tr-21)
để lại — *"đang làm gì để lớp đáy dày lên?"*. Hoá ra câu hỏi ấy có **hai** vế: làm lớp đáy dày lên
(mục 3: giá trị, quy mô), **và** rút nó ra kịp trước khi nó mỏng đi.

---

## 8. Bốn mô hình thu nhập

> [!quote]
> *"Từ vốn con người, chúng ta có thể chia ra 4 dạng mô hình thu nhập sau."* — C2 tr. 12

| Mô hình | Sách mô tả | Ví dụ của sách |
| --- | --- | --- |
| **Đi ngang** | *"không có sự tăng lên hoặc giảm xuống quá nhiều"* | công chức nhà nước |
| **Linh hoạt** | *"thay đổi theo khối lượng và/hoặc hiệu quả công việc"* | nghề bán hàng hưởng lương theo doanh số |
| **Giảm dần** | *"thu nhập rất cao ở những năm đầu sự nghiệp, nhưng giảm dần theo thời gian"* | nghệ sĩ, cầu thủ, vận động viên |
| **Tăng dần** | *"tăng dần theo thời gian bởi giá trị họ cung cấp… ngày càng lớn"* | tư vấn, cố vấn |

Lời khuyên đi kèm rất đúng và rất cụ thể:

> [!quote]
> *"nếu bạn thuộc nhóm **thu nhập giảm dần**, những năm đầu sự nghiệp bạn cần phát huy tối đa khả
> năng của bản thân, mang tiền về nhiều nhất có thể. Còn nếu bạn thuộc nhóm **thu nhập tăng dần**,
> những năm đầu không nên kỳ vọng việc kiếm được nhiều ngay, mà nên tích lũy kinh nghiệm."*
> — C2 tr. 13

---

## 9. [đính chính] "Không có mô hình nào lợi thế hơn" — lãi kép nói khác

Ngay trước lời khuyên vừa trích, sách viết một câu rộng hơn mức nó chịu được:

> [!quote]
> *"**Không có mô hình nào mang lại lợi thế hơn các mô hình khác**, bạn cần nắm được đâu là giai đoạn
> vàng để tập trung phát triển sự nghiệp."* — C2 tr. 13

Kiểm bằng cách cho cả bốn mô hình **cùng tổng thu nhập cả đời** (9,12 tỷ, từ 22 đến 60 tuổi) và
**cùng tỷ lệ tiết kiệm** (20%), lợi suất thực 8%:

| Mô hình | Thấp nhất | Cao nhất | Dạng | **Vốn tài chính lúc 60** |
| --- | ---: | ---: | --- | ---: |
| Đi ngang | 240 tr | 240 tr | phẳng | 10,58 tỷ |
| Linh hoạt | 96 tr | 384 tr | so le | 10,82 tỷ |
| **Tăng dần** | 96 tr | 384 tr | dốc lên | **7,78 tỷ** |
| **Giảm dần** | 96 tr | 384 tr | dốc xuống | **13,37 tỷ** |

Cùng số tiền kiếm được cả đời, cùng kỷ luật tiết kiệm, mà **"giảm dần" về hưu với nhiều hơn "tăng
dần" 1,72 lần** — chênh **5,59 tỷ**.

Lý do chỉ có một: **lãi kép thưởng cho tiền đến sớm.** Đồng tiết kiệm năm 23 tuổi có 37 năm để sinh
sôi; đồng tiết kiệm năm 59 tuổi có một năm.

*(Con số của "linh hoạt" nhỉnh hơn "đi ngang" một chút chỉ vì mô hình dựng ở đây bắt đầu bằng một
năm cao. Đảo lại thì nó thấp hơn. Đừng đọc gì thêm từ chỗ đó.)*

### Vậy câu của sách sai chỗ nào

Nó **quá rộng**, chứ không sai hoàn toàn. Tách ra hai nghĩa:

> [!note]
> **Đúng:** không mô hình nào **đáng mong muốn** hơn. Bạn thường không chọn được nghề mình hợp, và
> cầu thủ không nên ước mình là cố vấn.
>
> **Sai:** ở khâu **tích luỹ** thì bốn mô hình **không ngang nhau**. Với cùng tỷ lệ tiết kiệm, người
> thu nhập giảm dần về đích trước rất xa.

Và cái đáng nói: **chính sách nói đúng điều này ở câu ngay sau** — khuyên nhóm giảm dần *"mang tiền
về nhiều nhất có thể"* trong những năm đầu. Lời khuyên ấy chỉ có nghĩa nếu thời điểm tiền đến **có**
quan trọng. Câu tổng quát và lời khuyên cụ thể không khớp nhau; lời khuyên đúng.

### Người thu nhập tăng dần phải làm gì

Không phải đổi nghề. Phải **tiết kiệm tỷ lệ cao hơn** để bù cho việc tiền đến muộn:

> [!quote]
> Để đuổi kịp người "giảm dần", người "tăng dần" phải nâng tỷ lệ tiết kiệm từ **20% lên 35%**.

Đó là con số dùng được ngay: nếu thu nhập của bạn đang trên đường đi lên, đừng đợi tới lúc lương
cao mới bắt đầu tiết kiệm — chính đường đi lên ấy đã lấy mất phần lãi kép của bạn rồi.

Ngược lại, người "giảm dần" — nghệ sĩ, vận động viên — có một cửa sổ hẹp và không mở lại. Đây là
chỗ [bài 3](bai_03_ghi_chep_chi_tieu.md#7-bổ-sung-câu-hỏi-số-2-của-kakeibo-đã-là-trả-cho-mình-trước--từ-năm-1904)
và bài 7 quan trọng nhất với họ.

---

## 10. Tự thử

1. **Bạn được trả cho cái gì?** Với công việc hiện tại, viết ra **hai** câu trả lời: một theo góc
   nhìn 1, một theo góc nhìn 2. Nếu ngày mai có thêm 100 người làm được đúng việc bạn đang làm,
   lương bạn đổi thế nào? Câu trả lời đó nghiêng về góc nhìn nào?

2. **Ba thừa số của bạn.** Trong $\text{Giá trị} \times \text{Thời gian} \times \text{Quy mô}$, thừa
   số nào bạn đang có nhiều dư địa nhất? Tăng nó lên sẽ **phải trả** bằng thừa số nào?

3. **Phép thử nghỉ một năm.** Áp phép thử của C2 tr. 9 vào công việc của bạn: nghỉ hẳn một năm rồi
   quay lại, thu nhập từ nguồn đó còn bao nhiêu phần trăm? Bạn đang ở ô nào?

4. **Mô hình thu nhập của bạn.** Bạn thuộc mô hình nào trong bốn? Nếu là *tăng dần*, hãy dùng code
   tính xem bạn cần tiết kiệm bao nhiêu phần trăm để bằng người *giảm dần*.

5. **Đổi tuổi nghỉ hưu trong code.** Trong `bai-05-kiem-tien.py`, đổi `TUOI_HUU = 60` thành `65`.
   Tuổi giao nhau của hai đường vốn dịch đi bao nhiêu? Và vốn tài chính lúc nghỉ hưu tăng bao nhiêu?

6. **Đổi lợi suất.** Vẫn trong code, đổi `G = 0.08` thành `0.04`. Khoảng cách giữa "giảm dần" và
   "tăng dần" **rộng ra hay hẹp lại**? Giải thích tại sao trước khi chạy.

7. **Cãi lại mục 7.** Mục 7 nói vốn con người "không thể giữ lại". Tìm **một trường hợp** mà nó
   không hoàn toàn đúng — và nói rõ cơ chế nào khiến nó khác.

---

## 11. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Vốn con người | human capital | chuyên môn cộng mạng lưới; **giảm** theo tuổi — C2 tr. 11, 13 |
| Vốn tài chính | financial capital | tổng tài sản trừ nợ; chính là **tài sản ròng** của bài 2 |
| Kim tứ đồ | cashflow quadrant | bốn cách tạo ra tiền: E · S · B · I — C2 tr. 7 |
| Nhóm E | employee | *"họ có một công việc"* |
| Nhóm S | self-employed | *"tự làm chủ một công việc"*; là **mắt xích** của hệ thống |
| Nhóm B | business owner | làm chủ **hệ thống**; nghỉ một năm hệ thống vẫn chạy |
| Nhóm I | investor | *"tiền làm việc cho họ"* |
| Đòn bẩy thời gian | time leverage | dùng thời gian của người khác hoặc của tiền — C2 tr. 10–11 |
| Thiên kiến sống sót | survivorship bias | chỉ thấy người thành công; C2 tr. 10 — lần **duy nhất** sách gọi tên một thiên kiến |
| Bốn mô hình thu nhập | — | đi ngang · linh hoạt · giảm dần · tăng dần — C2 tr. 12–13 |
| **[bổ sung]** Trần và phần được chia | — | giá trị quyết định trần, sự hiếm quyết định bạn nhận bao nhiêu phần của trần đó |
| **[bổ sung]** Phép chuyển đổi vốn | — | biến vốn con người thành vốn tài chính trước khi nó hết hạn |

---

## 12. Câu hỏi tự kiểm tra

1. Sách đưa **mấy** câu trả lời cho câu hỏi "vì sao ta được trả tiền"? Kể ra. (mục 1)
2. Lập luận *"nếu đúng thì anh ta chỉ việc ở nhà để nhận tiền"* chứng minh điều gì? (mục 1)
3. Hai góc nhìn ấy mâu thuẫn ở chỗ nào? Chép ra **cụm từ** trong câu thứ hai phủ định câu thứ nhất. (mục 2)
4. Hai góc nhìn cho hai lời khuyên khác nhau thế nào? Người rất giỏi trong một nghề đông người
   thì góc nhìn nào đúng? (mục 2)
5. Cách hoà giải hai góc nhìn là gì? Câu nào **trong chính cuốn sách** thực hiện phép hoà giải
   đó, ở trang nào? (mục 2)
6. Viết công thức thu nhập của C2 tr. 5. Thừa số nào sách đặt trần, và trần đó là gì? (mục 3)
7. Trong ví dụ gia sư, quy mô nhân mấy lần và giá mỗi học sinh chia mấy lần? Câu *"giá trị tương
   đương nhau"* của sách có đứng vững không? (mục 3)
8. Ở mức nào thì mở rộng quy mô **hoà** với dạy 1 kèm 1? Câu hỏi đúng cần đặt là gì? (mục 3)
9. Kể bốn nhóm của Kim tứ đồ và bốn quy tắc. (mục 4)
10. Phép thử phân biệt nhóm B với nhóm S là gì? Chủ tiệm phở tự đứng bếp thuộc nhóm nào? (mục 4)
11. Quy tắc 3 nói gì về xác suất ở phía bên phải? Sách gọi tên thiên kiến nào? (mục 4)
12. Quy tắc 3 và quy tắc 4 kéo về hai hướng ra sao? Chúng nói về **hai đại lượng** nào khác nhau? (mục 5)
13. Lập luận *"đòn bẩy thời gian"* quay về thừa số nào của công thức ở mục 3? (mục 5)
14. Vốn con người ở bài này chính là khái niệm nào của bài 4? Vốn tài chính là khái niệm nào của bài 2? (mục 6)
15. Hai đường vốn cắt nhau ở tuổi nào? Lúc 60 tuổi vốn con người bằng bao nhiêu, và **vì sao**? (mục 7)
16. Người kiếm 9,12 tỷ cả đời mà tiết kiệm 0% thì lúc 60 tuổi có bao nhiêu? Điều đó nói gì về vai
    trò của tiết kiệm? (mục 7)
17. Bốn mô hình có cùng tổng thu nhập và cùng tỷ lệ tiết kiệm. Mô hình nào về đích nhiều nhất,
    ít nhất, chênh mấy lần? (mục 9)
18. Câu *"không có mô hình nào lợi thế hơn"* đúng ở nghĩa nào và sai ở nghĩa nào? (mục 9)
19. Người thu nhập tăng dần phải nâng tỷ lệ tiết kiệm lên bao nhiêu để đuổi kịp? (mục 9)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 5 — KIẾM TIỀN                                      C2 tr. 4-13     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  SÁCH ĐƯA HAI CÂU TRẢ LỜI CHO "VÌ SAO TA ĐƯỢC TRẢ TIỀN" — VÀ CHÚNG      ║
║  PHỦ ĐỊNH NHAU                                                          ║
║     tr.5  "lương được xác định NHỜ mức độ đóng góp"      -> GIÁ TRỊ     ║
║     tr.6  "KHÔNG PHẢI nhờ giá trị đóng góp, mà nhờ số                   ║
║            người có khả năng làm công việc đó"           -> SỰ HIẾM     ║
║     lời khuyên khác nhau: "giỏi hơn"  vs  "hiếm hơn"                     ║
║     HOÀ GIẢI: giá trị quyết định TRẦN · sự hiếm quyết định PHẦN của trần ║
║     và sách TỰ hoà giải ở tr.10: "trở thành SỐ ÍT CHUYÊN GIA"           ║
║                                                                          ║
║  Thu nhập = GIÁ TRỊ × THỜI GIAN × QUY MÔ    (tr.5, công thức của sách)  ║
║     chỉ THỜI GIAN có trần: 24h/ngày                                     ║
║     ví dụ gia sư tr.6: quy mô ×15, giá mỗi em ÷5, thu nhập ×3           ║
║        => sách viết "giá trị tương đương nhau" — con số nói khác        ║
║        50 em × 2k = HOÀ với 1 kèm 1 · 80 em × 1k = THUA                 ║
║        ba thừa số KHÔNG độc lập; tăng cái này trả bằng cái kia          ║
║                                                                          ║
║  KIM TỨ ĐỒ   E làm công · S tự làm chủ · B chủ hệ thống · I nhà đầu tư  ║
║     phép thử B/S: nghỉ 1 NĂM rồi quay lại, hệ thống còn chạy không?     ║
║     QT3 bên phải "xác suất thất bại rất cao"  <- THIÊN KIẾN SỐNG SÓT    ║
║     QT4 "nên học kiếm tiền ở bên phải"        <- đòn bẩy thời gian      ║
║        => hai quy tắc, hai hướng. Hoà giải: QT3 nói XÁC SUẤT,           ║
║           QT4 nói TRẦN. Bên phải trần cao hơn VÀ xác suất thấp hơn      ║
║                                                                          ║
║  HAI NGUỒN VỐN   vốn con người = lớp vô hình (bài 4) = 94% tháp         ║
║                  vốn tài chính = tài sản ròng (bài 2)                   ║
║     dựng lại biểu đồ tr.11 từ MỘT dòng thu nhập:                        ║
║        22 tuổi  2,80 tỷ / 0        -> vốn con người 100%                ║
║        43 tuổi  HAI ĐƯỜNG CẮT NHAU                                      ║
║        60 tuổi  0 / 10,58 tỷ       -> vốn con người bằng KHÔNG          ║
║                                                                          ║
║     => CẢ KẾ HOẠCH TÀI CHÍNH LÀ MỘT PHÉP CHUYỂN ĐỔI: biến vốn con       ║
║        người thành vốn tài chính TRƯỚC KHI NÓ HẾT HẠN                   ║
║        tiết kiệm 0%: kiếm 9,12 tỷ cả đời, 60 tuổi còn HAI SỐ KHÔNG      ║
║        tiết kiệm không phải đức tính — là cơ chế chuyển đổi DUY NHẤT    ║
║                                                                          ║
║  BỐN MÔ HÌNH THU NHẬP   đi ngang · linh hoạt · giảm dần · tăng dần      ║
║     sách: "Không có mô hình nào mang lại lợi thế hơn"  (tr.13)          ║
║     cùng tổng 9,12 tỷ, cùng tiết kiệm 20%, vốn TC lúc 60:               ║
║        giảm dần  13,37 tỷ   <- nhiều nhất                               ║
║        đi ngang  10,58 tỷ                                               ║
║        tăng dần   7,78 tỷ   <- ít nhất,  chênh 1,72 LẦN = 5,59 tỷ      ║
║     lãi kép thưởng cho tiền đến SỚM                                     ║
║     câu của sách ĐÚNG về "đáng mong muốn", SAI về "tích luỹ"           ║
║     người tăng dần phải nâng tiết kiệm 20% -> 35% mới đuổi kịp          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2***, Waka.vn.
  - **Unit 1 Lesson 1 *Tại sao chúng ta được trả tiền?* (tr. 4–6)** — *"Sự tôn trọng thường được ban
    phát theo thu nhập"* (tr. 4); góc nhìn chủ nghĩa tư bản, trích Jim Rohn từ *7 chiến lược thịnh
    vượng và hạnh phúc*, công thức Thu nhập = Giá trị × Thời gian × Quy mô, trần 24h của thừa số
    thời gian (tr. 5); ví dụ gia sư, *"phát triển bản thân"*, góc nhìn kinh tế học và câu *"không
    phải nhờ giá trị đóng góp"*, *"Lương chỉ đơn giản là độ chênh lệch giữa cầu và cung"* (tr. 6)
  - **Unit 1 Lesson 2 *Cashflow Quadrant* (tr. 6–11)** — bốn nhóm E/S/B/I và quy tắc 1 (tr. 7); thang
    bốn bậc *"làm hiệu quả"*, Ikigai (tr. 8); *"làm tận lực"* và lời hứa giải thích sau, quy tắc 2,
    phép thử **nghỉ một năm** phân biệt B với S (tr. 9); ví dụ anh Quyết, **quy tắc 3 và thiên kiến
    sống sót**, quy tắc 4 (tr. 10); *"đòn bẩy thời gian"* (tr. 11)
  - **Unit 1 Lesson 3 *Vốn và mô hình thu nhập* (tr. 11–13)** — hai nguồn vốn và biểu đồ tương quan
    (tr. 11); bốn mô hình thu nhập (tr. 12); *"vốn con người sẽ giảm theo thời gian"*, lời khuyên
    riêng cho nhóm giảm dần và nhóm tăng dần, câu *"Không có mô hình nào mang lại lợi thế hơn"*
    (tr. 13)
- ***Tài chính cá nhân 101 — Class 1***, Waka.vn.
  - Unit 3 Lesson 3 (tr. 22–23) — phép định giá lớp vô hình, dùng lại ở mục 7
  - Unit 4 Lesson 2 (tr. 31) — giả định lợi suất 12% và lạm phát 4%, tức lợi suất thực 8%
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-05-kiem-tien.py`](../thuc_hanh/bai-05-kiem-tien.py).
  Mọi bảng số ở mục 3, 7 và 9 do tệp này tính.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Nhận xét rằng **hai góc nhìn phủ định nhau** ([mục 2](#2-đính-chính-hai-góc-nhìn-ấy-phủ-định-nhau-và-sách-không-nói))
    và cách hoà giải "trần / phần được chia" là của khoá học. Sách in cả hai và không bình luận.
    Việc câu ở tr. 10 hoà giải được chúng cũng là quan sát của khoá học.
  - Phép bóc ví dụ gia sư thành ba thừa số, và bảng mở rộng quy mô tới điểm hoà/thua ở
    [mục 3](#3-công-thức-thu-nhập--giá-trị--thời-gian--quy-mô) **không có trong sách**. Bốn dòng
    cuối của bảng (30, 50, 80 học sinh) là **giả định của khoá học**, không phải số liệu.
  - Nhận xét về căng thẳng giữa **quy tắc 3 và quy tắc 4** ([mục 5](#5-bổ-sung-quy-tắc-3-và-quy-tắc-4-kéo-về-hai-hướng))
    là của khoá học.
  - **Toàn bộ bảng hai nguồn vốn ở [mục 7](#7-bổ-sung-cả-kế-hoạch-tài-chính-là-một-phép-chuyển-đổi)
    là do khoá học dựng.** Sách in một biểu đồ không kèm số. Thu nhập 20 triệu/tháng, tuổi 22–60,
    tiết kiệm 20%, lợi suất thực 8% đều là **giả định** để minh hoạ cơ chế.
  - Bảng bốn mô hình ở [mục 9](#9-đính-chính-không-có-mô-hình-nào-lợi-thế-hơn--lãi-kép-nói-khác) là
    của khoá học. Sách chỉ mô tả bốn dạng bằng lời, không cho con số nào.
- **Liên hệ chéo:**
  - Lớp tài sản vô hình và phép định giá nó:
    [bài 4 mục 6](bai_04_tai_san_tieu_san_thap_tai_san.md#6-đính-chính-định-giá-lớp-vô-hình-đo-cái-gì).
  - Tài sản ròng: [bài 2](bai_02_do_hien_trang.md).
  - Số năm tới tự do tài chính, cùng giả định lợi suất:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Lãi kép và giá trị theo thời gian:
    [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| **5** | **Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người** ← *bạn đang ở đây* | C2 tr. 4–13 | 1 |
| 6 | [**[bổ sung]** Thuế thu nhập cá nhân — tiền thật về tay](bai_06_thue_thu_nhap_ca_nhan.md) | ngoài sách | 1 |
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | [**[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai](bai_10_tai_chinh_hanh_vi.md) | ngoài sách | 2 |
| 11 | [Nhận diện lừa đảo: Ponzi và CFD](bai_11_nhan_dien_lua_dao.md) | C2 tr. 47–57 | 1 |
| 12 | [Rủi ro, khẩu vị rủi ro, phân bổ tài sản](bai_12_rui_ro_khau_vi_phan_bo.md) | C1 tr. 25–33 | 1 |
| 13 | [Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF](bai_13_kenh_dau_tu.md) | C2 tr. 58–67 | 2 |
| 14 | [Mục tiêu SMART và ráp lại thành kế hoạch](bai_14_muc_tieu_smart.md) | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
