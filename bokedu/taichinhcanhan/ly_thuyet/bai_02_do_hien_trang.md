# Bài 2 — Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối

> Bài học gộp **ba chỗ của hai tập**: C1 tr. 10–12 (Unit 2 Lesson 3), C1 tr. 18 (Unit 3 Lesson 2),
> và C2 tr. 15–17 (Unit 2 Lesson 1). Sách dạy cùng một khái niệm ở cả ba chỗ dưới ba cái tên khác
> nhau — lý do gộp ở [bài 0 mục 4](bai_00_bat_dau_tu_dau.md#4-vì-sao-khoá-học-không-đi-theo-thứ-tự-sách).
>
> **Cần đọc trước:** [Bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md) — đây là **bước 1** trong bốn bước.
>
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[2026]** là mục đối chiếu với hiện tại.
>
> **Code:** [`thuc_hanh/bai-02-do-hien-trang.py`](../thuc_hanh/bai-02-do-hien-trang.py)
> — dựng lại ba ví dụ Net worth của C2 tr. 16, tách hai nguyên nhân làm tài sản ròng thay đổi, và
> tính chiếc ô tô của ví dụ 2 mất bao lâu mới thoát khỏi số âm.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Hai con số, hai câu hỏi](#1-hai-con-số-hai-câu-hỏi)
- [2. Dòng tiền — bước 1 của sách](#2-dòng-tiền--bước-1-của-sách)
- [3. Tài sản ròng — bước 2, và bảng cân đối cá nhân](#3-tài-sản-ròng--bước-2-và-bảng-cân-đối-cá-nhân)
- [4. [bổ sung] Dòng chảy và tồn kho — cái tên mà sách không đặt](#4-bổ-sung-dòng-chảy-và-tồn-kho--cái-tên-mà-sách-không-đặt)
- [5. [bổ sung] Tài sản ròng đổi vì hai lý do, sách chỉ đặt tên một](#5-bổ-sung-tài-sản-ròng-đổi-vì-hai-lý-do-sách-chỉ-đặt-tên-một)
- [6. Vì sao tài sản ròng quan trọng hơn lương](#6-vì-sao-tài-sản-ròng-quan-trọng-hơn-lương)
- [7. [bổ sung] Bốn ô — đọc hai con số cùng lúc](#7-bổ-sung-bốn-ô--đọc-hai-con-số-cùng-lúc)
- [8. [bổ sung] Tài sản ròng cũng là một ý kiến](#8-bổ-sung-tài-sản-ròng-cũng-là-một-ý-kiến)
- [9. Tự thử](#9-tự-thử)
- [10. Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
- [11. Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Hai con số, hai câu hỏi

Bài 1 nói bước đầu tiên của kế hoạch là *"Xác định dòng tiền và giá trị tài sản"*. Sách mở bước đó
bằng một câu rất gọn:

> *"Hành động đầu tiên để cải thiện tình hình tài chính đó là biết bạn đang ở đâu."* — C1 tr. 11

"Ở đâu" được đo bằng **đúng hai con số**, và chúng trả lời hai câu hỏi khác hẳn nhau:

| | Dòng tiền | Tài sản ròng |
| --- | --- | --- |
| Công thức | Tổng thu nhập − Tổng chi phí | Tổng tài sản − Tổng nợ |
| Trả lời | tháng này tôi **dôi ra** hay hụt đi? | tính đến hôm nay tôi **có** bao nhiêu? |
| Đo trong | một **khoảng** thời gian | một **thời điểm** |
| Sách gọi là | *"phản ánh khả năng thanh toán"* | *"sự giàu có"* |
| Ở đâu | C1 tr. 11 | C1 tr. 12 · C2 tr. 15–16 |

Cả hai đều là phép trừ hai số. Cái khó không nằm ở phép tính — nó nằm ở chỗ **hai con số này đo hai
thứ khác loại nhau**, và sách dạy cả hai mà không bao giờ nói ra điều đó. Mục 4 lấp chỗ trống ấy.

---

## 2. Dòng tiền — bước 1 của sách

Sách bảo lấy giấy bút ra, và liệt kê thu nhập theo **ba nguồn**:

```
   THU NHẬP                             CHI PHÍ
   ────────                             ───────
   thường xuyên                         thường xuyên
     lương, thưởng, phụ cấp               ăn, nhà ở, điện/nước/internet
   từ kinh doanh                        kinh doanh
     sản phẩm/dịch vụ tự làm
   từ đầu tư                            đầu tư
     cổ tức, lợi tức trái phiếu,
     tiền thuê nhà…

              Dòng tiền = Tổng thu nhập − Tổng chi phí
                                                            C1 tr. 11
```

Ba khả năng, và sách xếp hạng chúng:

> *"Dòng tiền yếu khi âm hoặc tình trạng qua các tháng lúc âm, lúc dương không ổn định. Dòng tiền
> mạnh khi lớn hơn 0. Điều này rất quan trọng, vì khi và chỉ khi dòng tiền dương bạn mới nên nghĩ
> đến việc đầu tư dài hạn."* — C1 tr. 12

Chú ý sách xếp **"lúc âm lúc dương không ổn định"** vào cùng nhóm với âm. Dòng tiền dương nhưng
chập chờn không đủ để mở cổng sang bước 4. Đó là một chuẩn chặt hơn nhiều so với "tháng này tôi có
dư", và nó giải thích vì sao bài 3 yêu cầu ghi chép **3–6 tháng** chứ không phải một tháng.

### Hai chỗ sách phân loại rất tốt

**Một.** Trading không phải đầu tư:

> *"Nếu bạn giao dịch cổ phiếu theo cách mua đi bán lại, lợi nhuận thu được bạn nên để vào mục
> [kinh doanh]. Bởi công việc trading được tính là một hoạt động kinh doanh."* — C1 tr. 11

Đây là một phân loại sắc và ít sách phổ thông nào chịu nói. Mua đi bán lại là **đổi thời gian và
công sức lấy tiền** — nó nằm ở bài toán *kiếm tiền*, không phải *đầu tư*. Hệ quả thực tế: nếu bạn
ngừng ngồi trước bảng điện, dòng thu nhập đó dừng. Đó là định nghĩa của thu nhập chủ động.

**Hai.** Sách đặt một ngưỡng cụ thể cho chữ "đầu tư":

> *"Đầu tư nên hiểu là hoạt động trung và dài hạn, có thời hạn từ 3 năm trở lên."* — C1 tr. 11

Con số 3 năm không thiêng liêng, nhưng việc **có một ngưỡng** thì quan trọng: nó ngăn người ta gọi
mọi hành vi mua bán là "đầu tư".

### [đính chính] Một chỗ mơ hồ trong danh sách thu nhập

Trong nhóm *thu nhập từ đầu tư*, sách liệt kê: *"lợi nhuận đầu tư cổ phiếu, lợi tức trái phiếu,
tiền thuê nhà, **thanh lý BĐS**…"* (C1 tr. 11).

Ba khoản đầu là **lợi tức** — tiền sinh ra từ tài sản mà tài sản vẫn còn đó. Khoản thứ tư khác
loại: bán một mảnh đất là **đổi tài sản này lấy tài sản khác**, không phải sinh ra tiền mới.

Quy tắc để không nhầm: **chỉ phần lãi mới là thu nhập, phần gốc thì không.** Bán mảnh đất mua 1,4
tỷ được 1,6 tỷ thì thu nhập là **200 triệu**, không phải 1,6 tỷ.

Sai chỗ này thì hỏng đúng thứ bài này đang đo. Ghi cả 1,6 tỷ vào thu nhập, dòng tiền tháng đó vọt
lên rực rỡ — trong khi **tài sản ròng không đổi một đồng nào** ngoài phần lãi. Bạn tưởng mình vừa
có một tháng xuất sắc, thật ra chỉ vừa đổi hình dạng tài sản. Bài 8 dùng đúng mảnh đất 1,4 tỷ này
để làm bài toán tỷ suất sinh lợi.

---

## 3. Tài sản ròng — bước 2, và bảng cân đối cá nhân

Bước 2 cũng chỉ là một phép trừ:

> *"hãy lấy tổng tài sản trừ đi tổng nợ. Con số bạn có lúc này là Tài sản ròng… **Tài sản ròng =
> Tổng tài sản − Tổng nợ**"* — C1 tr. 12

Sách chia tài sản làm ba nhóm — **tiêu dùng** (nhà ở, ô tô), **kinh doanh** (vốn góp), **đầu tư**
(số dư ngân hàng, BĐS) — và mỗi nhóm có khoản vay tương ứng: vay tiêu dùng, vay kinh doanh, vay đầu
tư. Cách chia đôi này (ba loại tài sản ↔ ba loại nợ) chính là **bảng cân đối tài chính cá nhân**,
mà sách giới thiệu riêng ở Unit 3:

> *"Đây là phiên bản đơn giản hơn của báo cáo tài chính doanh nghiệp. Cả hai đều là những công cụ
> có thể cho thấy sức khỏe tài chính của đối tượng. Bảng cân đối tài chính cá nhân là bản phác thảo
> tình hình tài chính của cá nhân **tại một thời điểm nhất định**."* — C1 tr. 18

Ai đã học [Trí tuệ tài chính](../../trituetaichinh/README.md) sẽ nhận ra ngay: đây đúng là bảng cân
đối kế toán, bỏ đi phần vốn chủ sở hữu. Ở doanh nghiệp, *tài sản = nợ + vốn chủ sở hữu*; ở cá nhân,
"vốn chủ sở hữu" chính là **tài sản ròng** của bạn.
[Bài 4 của môn đó](../../trituetaichinh/ly_thuyet/bai_04_bang_can_doi_ke_toan.md) làm kỹ chỗ này.

Sách chốt bằng một quy tắc hai vế, và vế thứ hai sẽ quay lại ở mục 7:

> *"Bạn cần luôn bảo đảm Dòng tiền thuần và Tài sản thuần luôn là con số dương."* — C1 tr. 17

### Ba cái tên cho hai khái niệm

Đây là chỗ dễ tưởng mình đang học ba thứ:

| Sách viết | Ở đâu | Thật ra là |
| --- | --- | --- |
| **Tài sản ròng** | C1 tr. 12 | tổng tài sản − tổng nợ |
| **Tài sản thuần** | C1 tr. 17 | y hệt |
| **Net worth** *(Giá trị tài sản ròng)* | C2 tr. 15 | y hệt, đúng ba trang ví dụ mới |
| **Dòng tiền** | C1 tr. 11 | thu − chi |
| **Dòng tiền thuần** | C1 tr. 17 | y hệt |

Khoá học dùng **tài sản ròng** và **dòng tiền**, và chỉ nhắc *net worth* khi trích C2.

Một chi tiết nhỏ nữa: C1 tr. 18 nói bảng cân đối *"mô tả thông tin về **tỷ lệ** dòng tiền thuần,
**tỷ lệ** tài sản ròng"*. Cả hai đều là **số tiền**, không phải tỷ lệ. Chữ *tỷ lệ* ở đây thừa.

### [đính chính] Định nghĩa nợ của sách quá hẹp

> *"Nợ (Liabilities) là các khoản vay để tạo ra tài sản."* — C1 tr. 17

Không phải khoản nợ nào cũng tạo ra tài sản. Vay để trả viện phí, quẹt thẻ tín dụng cho một bữa
ăn, mượn tiền đóng tiền nhà — đó là nợ thật, phải trả thật, mà chẳng tạo ra tài sản nào.

Định nghĩa dùng được là: **nợ là mọi nghĩa vụ phải trả, bất kể nó đã dùng vào việc gì.**

Chỗ này không phải bắt bẻ chữ nghĩa, vì nó **đổi con số**. Ai đọc theo đúng chữ của sách sẽ chỉ
liệt kê các khoản vay có tài sản đối ứng, bỏ sót phần nợ tiêu dùng — và tài sản ròng tính ra
**cao hơn sự thật**. Đúng cái sai lầm mà C2 tr. 16 mô tả ở mục 6.

Phần tài sản và tiêu sản đầy đủ nằm ở **bài 4**; ở đây chỉ cần đủ để phép trừ không hụt vế.

---

## 4. [bổ sung] Dòng chảy và tồn kho — cái tên mà sách không đặt

Sách dạy hai con số ở hai bước liền nhau và không lần nào nói chúng **khác loại**. Đây là cái tên
của sự khác nhau đó, và nó là khái niệm quan trọng nhất của cả bài:

```
   DÒNG CHẢY (flow)                      TỒN KHO (stock)
   ────────────────                      ───────────────
   đo trong MỘT KHOẢNG thời gian         đo tại MỘT THỜI ĐIỂM
   "tháng 9 tôi dôi ra 3 triệu"          "ngày 30/9 tôi có 250 triệu"
   không có ý nghĩa nếu thiếu            không có ý nghĩa nếu thiếu
     khoảng thời gian                      ngày cụ thể
   → dòng tiền                           → tài sản ròng

        vòi nước chảy vào bể                 lượng nước trong bể
```

Ẩn dụ cái bể là đủ để nhớ cả bài: **dòng tiền là vòi, tài sản ròng là mực nước.** Vòi mở to suốt
tháng mà bể vẫn cạn thì có lỗ rò ở đâu đó — mục 5 chỉ ra lỗ rò ấy.

Ba hệ quả dùng được ngay:

1. **Nói dòng tiền mà không nói khoảng thời gian là vô nghĩa.** "Dòng tiền của tôi là 3 triệu" —
   một tháng? một năm?
2. **Nói tài sản ròng mà không nói ngày cũng vô nghĩa**, và ví dụ 3 ở mục 5 cho thấy vì sao: con
   số ấy đổi qua đêm mà bạn không làm gì cả.
3. **Không được cộng hai loại vào nhau.** Đây là lỗi mà chính sách mắc ở C2 tr. 28, khi khuyên
   *"tỷ lệ tiết kiệm cần lớn hơn hoặc bằng số tuổi"* — trộn một dòng chảy (tỷ lệ tiết kiệm) với
   các quy tắc vốn đo tồn kho. **Bài 7** quay lại chỗ đó, và nó sai được chính vì bài 2 của sách
   chưa bao giờ dựng lên sự phân biệt này.

---

## 5. [bổ sung] Tài sản ròng đổi vì hai lý do, sách chỉ đặt tên một

Nối hai con số của mục 1 lại với nhau:

$$
\underbrace{\Delta\,\text{tài sản ròng}}_{\text{giữa hai ảnh chụp}}
\;=\;
\underbrace{\text{dòng tiền}}_{\text{tiền thật vào ra}}
\;+\;
\underbrace{\Delta\,\text{định giá}}_{\text{giá thị trường của thứ đang nắm đổi}}
$$

Sách **đưa ra ví dụ về vế thứ hai nhưng không đặt tên cho nó**. Đây là ví dụ thứ ba của C2 tr. 16:

> *"Bạn dồn tất cả tài sản vào đầu tư chứng khoán. Hôm nay giá trị cổ phiếu là 1 tỷ đồng, vì vậy
> Net worth của bạn là 1 tỷ đồng. Nhưng ngày mai, giá cổ phiếu đi xuống còn 800 triệu thì Net worth
> của bạn cũng sẽ chỉ còn 800 triệu."* — C2 tr. 16

Tách ra:

```
   dòng tiền                     0 đồng     không kiếm thêm, không tiêu thêm
   thay đổi định giá  −200.000.000 đồng     giá cổ phiếu tụt
   ────────────────────────────────────
   tài sản ròng đổi   −200.000.000 đồng
```

**Hai trăm triệu bốc hơi với dòng tiền bằng không.** Ví dụ 1 và ví dụ 2 của sách là ảnh chụp tĩnh;
ví dụ 3 là một *thay đổi*, và nó thuộc loại mà cày cuốc cả tháng không đụng tới được.

Đó cũng là lỗ rò của cái bể ở mục 4: **tháng nào cũng dôi ra mà tài sản ròng vẫn đi xuống** là
chuyện hoàn toàn bình thường, nếu thứ bạn đang nắm mất giá nhanh hơn tốc độ bạn tích luỹ.

### Chiếc ô tô của ví dụ 2, tính đến cùng

Ví dụ 2 của sách dừng ở chỗ tài sản ròng **âm 90 triệu**. Câu hỏi tự nhiên mà sách không hỏi:
*bao lâu thì thoát?*

Nếu bỏ qua mất giá thì đó là phép chia lớp ba: $90 \div 3 = 30$ tháng với dòng tiền 3 triệu/tháng.
Nhưng chiếc xe **mất giá**, và nó kéo ngược lại đúng theo vế thứ hai của công thức trên. Cho xe mất
10%/năm:

| Dòng tiền/tháng | Xe không mất giá | Xe mất giá 10%/năm | Chậm hơn |
| ---: | ---: | ---: | ---: |
| 1 triệu | 90 tháng | **272 tháng** | +182 |
| 2 triệu | 45 tháng | 106 tháng | +61 |
| 3 triệu | 30 tháng | **56 tháng** | +26 |
| 5 triệu | 18 tháng | 27 tháng | +9 |
| 8 triệu | 12 tháng | 15 tháng | +3 |

Tháng đầu tiên chiếc xe mất **1.748.322 đồng**. Dòng tiền thấp hơn con số đó thì tài sản ròng còn
**tụt xuống trước khi bò lên**:

```
   dòng tiền 1 triệu/tháng, xe mất giá 10%/năm

   sau   0 tháng   tài sản ròng    −90.000.000
   sau  12 tháng   tài sản ròng    −98.000.000     ← è cổ trả nợ một năm, âm SÂU HƠN
   sau  24 tháng   tài sản ròng   −104.000.001
   sau  60 tháng   tài sản ròng   −111.902.000     ← đáy nằm ở đâu đó quanh đây
   sau 272 tháng   tài sản ròng        +359.468     ← thoát, sau hơn 22 năm
```

Người này làm mọi thứ đúng — dòng tiền dương, đều đặn, kỷ luật — và suốt năm năm đầu vẫn thấy con
số xấu đi. Không phải vì họ sai, mà vì **hai lực đang đánh nhau** và họ chỉ nhìn thấy một.

Đó là lý do phải đo **cả hai** con số. Nhìn mỗi dòng tiền thì thấy mình đang tiến; nhìn mỗi tài sản
ròng thì tưởng mình vô dụng. Chỉ khi đặt cạnh nhau mới đọc được chuyện gì đang xảy ra.

Toàn bộ bảng trên do [`bai-02-do-hien-trang.py`](../thuc_hanh/bai-02-do-hien-trang.py) tính.
Con số 10%/năm là **giả định của khoá học**, không phải của sách — đổi nó trong code là mọi số đổi theo.

---

## 6. Vì sao tài sản ròng quan trọng hơn lương

C2 mở đầu Unit 2 bằng một câu rất Việt Nam:

> *"Nhiều người Việt có thói quen hỏi 'Lương tháng bao tiền?' để đoán xem đối phương 'đắt giá' bao
> nhiêu. Nhưng thực sự, câu hỏi đúng hơn phải là 'Net worth thế nào?'"* — C2 tr. 15

Sách đưa **ba lý do**:

**Một — lương đo cái kiếm được, tài sản ròng đo cái giữ được.**

> *"Có những người nhìn bề ngoài rất 'hoành tráng': nhà lầu, xe hơi, đi du lịch, mua sắm quanh
> năm... Tuy nhiên, những tài sản và trải nghiệm mà họ có được đó lại đều từ tiền vay mượn, trả
> góp, tín dụng mà ra. Net worth của họ ở mức rất thấp, hoặc thậm chí âm."* — C2 tr. 16

Đó chính là ví dụ 2 — chiếc ô tô 200 triệu với khoản nợ 300 triệu. Người ngoài nhìn thấy **chiếc
xe**; bảng cân đối nhìn thấy **âm 90 triệu**.

**Hai — lạm phát lối sống.**

> *"tập trung vào Net worth thay vì lương tháng sẽ giúp kiểm soát được nguy cơ lạm phát lối sống
> (lifestyle creep/lifestyle inflation)… khi 'vung tiền quá trán', Net worth của bạn thậm chí có
> thể xuống thấp hơn so với lúc bạn còn nhận mức lương cũ."* — C2 tr. 17

Đây là hiện tượng quan trọng nhất mà bài này chạm tới, và **bài 10** sẽ đặt nó vào khung tài chính
hành vi cùng với ba thiên kiến khác mà sách nhắc rời rạc.

**Ba — có con số thì mới đặt được cột mốc.** Sách gợi ý hai loại: *"trả nợ để đưa Net worth ra khỏi
con số âm"* và *"có được 1 tỷ đồng Net worth ở tuổi 35"* (C2 tr. 17). Bài 14 biến chúng thành mục
tiêu SMART.

### Bốn quy tắc quản lý của sách

| Quy tắc | C2 tr. 17 |
| --- | --- |
| Kiểm tra **ít nhất 1 lần/tháng** | đủ dày để thấy xu hướng |
| Vạch cột mốc cụ thể | biến con số thành mục tiêu |
| **Đừng** kiểm tra hàng ngày, đừng lo khi nó giảm | tài sản ròng có phần định giá — nó dao động mà bạn không làm gì cả (mục 5) |
| **Đừng** so sánh với người khác khi chưa biết tình hình của họ | người có chiếc xe kia có thể đang âm 90 triệu |

Bốn quy tắc này nhất quán với nhau, và quy tắc thứ ba chính là hệ quả trực tiếp của phép tách ở
mục 5 — dù sách không nối hai chỗ lại.

---

## 7. [bổ sung] Bốn ô — đọc hai con số cùng lúc

Sách đặt **hai** điều kiện dương, ở hai chỗ cách nhau:

- C1 tr. 12 — *"khi và chỉ khi dòng tiền dương bạn mới nên nghĩ đến việc đầu tư dài hạn"*
- C1 tr. 17 — *"luôn bảo đảm Dòng tiền thuần và Tài sản thuần luôn là con số dương"*

Hai điều kiện, bốn tổ hợp. Sách không bao giờ vẽ bảng này ra:

```
                          TÀI SẢN RÒNG ÂM              TÀI SẢN RÒNG DƯƠNG
                      ┌────────────────────────┬────────────────────────┐
                      │                        │                        │
   DÒNG TIỀN DƯƠNG    │     ĐANG ĐÀO LÊN       │     ĐANG TÍCH LUỸ      │
                      │  hướng đúng, chưa tới  │  cả hai cổng đã qua;   │
                      │  nơi; trả nợ trước     │  câu hỏi kế tiếp là    │
                      │  khi đầu tư            │  đầu tư vào đâu        │
                      ├────────────────────────┼────────────────────────┤
                      │                        │                        │
   DÒNG TIỀN ÂM       │      KHỦNG HOẢNG       │   ĐANG ĂN VÀO VỐN      │
                      │  không bước nào của    │  có đệm, nhưng đệm     │
                      │  kế hoạch bắt đầu      │  đang mỏng đi; sửa     │
                      │  được ở đây            │  dòng tiền trước       │
                      └────────────────────────┴────────────────────────┘
```

Hai ô bên trái và ô dưới bên phải **đều chưa được phép sang bước 4**, nhưng vì ba lý do khác nhau
và cần ba hành động khác nhau. Đó là lý do một con số không đủ.

Ví dụ 2 của sách, nếu người đó có dòng tiền +3 triệu/tháng, nằm ở ô **ĐANG ĐÀO LÊN** — và mục 5 vừa
cho thấy họ sẽ đào 56 tháng.

Ô nguy hiểm nhất **không phải** ô khủng hoảng — ô đó ai cũng biết là mình đang gặp chuyện. Nguy
nhất là **ĐANG ĂN VÀO VỐN**: con số lớn vẫn còn đó, cảm giác vẫn ổn, và mỗi tháng nó nhỏ đi một ít.
Người trong ô này thường phát hiện muộn vì họ nhìn tài sản ròng chứ không nhìn dòng tiền.

---

## 8. [bổ sung] Tài sản ròng cũng là một ý kiến

Sách nói tính tài sản ròng bằng *"tiền quy ra từ **giá thị trường** của các tài sản như: nhà cửa,
đất đai, xe cộ..."* (C2 tr. 16). Nghe như một con số khách quan. Nó không hẳn vậy.

**Hai vế của phép trừ có độ chắc chắn rất khác nhau:**

| | Biết chính xác đến đâu |
| --- | --- |
| **Nợ** | đến từng đồng. Sao kê ngân hàng ghi rõ dư nợ |
| **Tài sản** | tiền mặt và số dư ngân hàng thì chính xác. Còn nhà, đất, xe, vốn góp — đều là **ước lượng** |

Và sai số không đối xứng: người ta hiếm khi định giá thấp căn nhà của mình. Nên **tài sản ròng tự
tính có xu hướng cao hơn sự thật**, và cao hơn đúng ở vế mà bạn ít kiểm chứng được nhất.

Ba quy tắc để con số dùng được:

1. **Chặt tay với tài sản, chính xác với nợ.** Định giá thấp còn hơn định giá cao — sai theo hướng
   an toàn.
2. **Định giá bằng cái người khác thật sự trả**, không phải giá bạn muốn. Với xe cũ là giá rao bán
   thực tế của xe cùng đời; với đất là giao dịch gần nhất trong khu, không phải giá chào.
3. **Ghi lại giả định định giá cùng với con số.** Tháng sau so lại, bạn cần biết tài sản ròng tăng
   vì bạn tích luỹ được hay vì bạn vừa lạc quan hơn tháng trước.

Người đã học [Trí tuệ tài chính](../../trituetaichinh/README.md) sẽ thấy quen: luận điểm trung tâm
của cuốn đó là **lợi nhuận là một ý kiến, tiền mặt mới là sự thật**. Ở quy mô cá nhân, mệnh đề
tương ứng là: **tài sản ròng là một ý kiến, dòng tiền mới là sự thật.** Bạn có thể tự thuyết phục
mình rằng căn nhà đáng giá hơn 200 triệu; bạn không thể tự thuyết phục mình rằng tài khoản còn
tiền.

---

## 9. Tự thử

1. **Đo chính mình.** Lấy giấy bút đúng như C1 tr. 11 yêu cầu. Tính hai con số cho tháng gần nhất.
   Bạn nằm ở ô nào trong bốn ô của mục 7?

2. **Tách hai nguyên nhân.** Nếu tháng trước bạn đã tính tài sản ròng, lấy hiệu số của tháng này.
   Bao nhiêu phần đến từ **dòng tiền**, bao nhiêu phần từ **thay đổi định giá**? Nếu chưa có số
   tháng trước — đó chính là lý do quy tắc "kiểm tra ít nhất 1 lần/tháng" tồn tại.

3. **Đổi tốc độ mất giá.** Trong `bai-02-do-hien-trang.py`, đổi `0.10` ở bảng cuối thành `0.15`.
   Với dòng tiền 3 triệu/tháng, số tháng thoát âm thay đổi thế nào? Mức dòng tiền nào trở thành
   ngưỡng "tụt trước khi bò lên"?

4. **Bán xe thì sao?** Vẫn ví dụ 2 của sách. Nếu bán chiếc xe 200 triệu và trả bớt nợ ngay hôm nay,
   tài sản ròng **đổi bao nhiêu**? Và sau đó bao lâu thì thoát âm với dòng tiền 3 triệu/tháng? So
   với 56 tháng ở mục 5.

5. **Thêm một tài sản mất giá vào code.** `BangCanDoi` hiện chỉ giữ con số tĩnh. Thêm một chiếc
   điện thoại 20 triệu mất giá 30%/năm vào ví dụ 2 và chạy lại. Nó đẩy ngày thoát âm ra xa bao nhiêu?

6. **Tìm chỗ sách trộn hai loại.** Mục 4 nói dòng chảy không được cộng với tồn kho. Đọc lướt hai
   tập, tìm **một chỗ nữa** ngoài C2 tr. 28 nơi sách đặt một dòng chảy cạnh một tồn kho như thể
   chúng cùng loại.

---

## 10. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Dòng tiền | cash flow | thu − chi, đo trong **một khoảng** thời gian — C1 tr. 11 |
| Tài sản ròng · tài sản thuần | net worth | tổng tài sản − tổng nợ, tại **một thời điểm** — C1 tr. 12 · C2 tr. 15 |
| Bảng cân đối tài chính cá nhân | personal balance sheet | ảnh chụp tài sản và nợ; *"phiên bản đơn giản hơn của báo cáo tài chính doanh nghiệp"* — C1 tr. 18 |
| Tài sản tiêu dùng | — | nhà ở, ô tô — thứ tạo chi phí để duy trì; bài 4 |
| Tài sản đầu tư | — | thứ mang tiền về; bài 4 |
| Nợ | liabilities | mọi nghĩa vụ phải trả — **rộng hơn** định nghĩa ở C1 tr. 17 |
| Lạm phát lối sống | lifestyle creep · lifestyle inflation | chi tiêu phình theo lương — C2 tr. 17; bài 10 |
| **[bổ sung]** Dòng chảy | flow | đại lượng chỉ có nghĩa khi kèm một **khoảng** thời gian |
| **[bổ sung]** Tồn kho | stock | đại lượng chỉ có nghĩa khi kèm một **thời điểm** |
| **[bổ sung]** Thay đổi định giá | valuation change | phần tài sản ròng đổi mà **không** qua dòng tiền |
| **[bổ sung]** Mất giá | depreciation | tài sản tụt giá theo thời gian; kéo ngược tài sản ròng |

---

## 11. Câu hỏi tự kiểm tra

1. Hai con số đo "bạn đang ở đâu" là gì? Mỗi con số trả lời câu hỏi nào? (mục 1)
2. Sách xếp *"lúc âm lúc dương không ổn định"* vào nhóm nào? Điều đó ảnh hưởng gì tới bài 3? (mục 2)
3. Vì sao sách xếp lợi nhuận **trading** vào thu nhập kinh doanh chứ không phải thu nhập đầu tư? (mục 2)
4. Bán mảnh đất mua 1,4 tỷ được 1,6 tỷ. Ghi vào thu nhập **bao nhiêu**, và vì sao không phải 1,6 tỷ? (mục 2)
5. Bảng cân đối cá nhân khác bảng cân đối kế toán doanh nghiệp ở chỗ nào? "Vốn chủ sở hữu" của bạn
   là con số nào? (mục 3)
6. Sách dùng **mấy** cái tên cho khái niệm tài sản ròng? Kể ra. (mục 3)
7. Định nghĩa nợ của C1 tr. 17 hẹp ở chỗ nào, và ai đọc theo đúng chữ đó sẽ tính ra tài sản ròng
   **cao hơn hay thấp hơn** sự thật? (mục 3)
8. Dòng chảy khác tồn kho ở chỗ nào? Cho một câu **vô nghĩa** vì thiếu khoảng thời gian, và một
   câu vô nghĩa vì thiếu thời điểm. (mục 4)
9. Viết công thức nối $\Delta$ tài sản ròng với dòng tiền. Vế thứ hai là gì? (mục 5)
10. Trong ví dụ 3 của C2 tr. 16, dòng tiền là bao nhiêu và tài sản ròng đổi bao nhiêu? Điều đó
    chứng minh gì? (mục 5)
11. Người trong ví dụ 2 trả nợ đều 1 triệu/tháng. Sau 12 tháng tài sản ròng của họ **tốt hơn hay
    xấu hơn** lúc bắt đầu? Vì sao? (mục 5)
12. Kể ba lý do sách đưa ra để nói tài sản ròng quan trọng hơn lương. (mục 6)
13. Vì sao sách khuyên **đừng** kiểm tra tài sản ròng hàng ngày? Nối câu trả lời với mục 5. (mục 6)
14. Kể bốn ô. Ô nào nguy hiểm nhất và **vì sao không phải** ô khủng hoảng? (mục 7)
15. Vế nào của phép trừ tài sản ròng bạn biết chính xác, vế nào là ước lượng? Sai số lệch về
    hướng nào? (mục 8)
16. Phát biểu *"lợi nhuận là một ý kiến, tiền mặt mới là sự thật"* có phiên bản cá nhân là gì? (mục 8)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 2 — ĐO HIỆN TRẠNG          C1 tr.10-12, 18  ·  C2 tr.15-17          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  HAI CON SỐ, HAI CÂU HỎI                                                 ║
║     Dòng tiền   = thu − chi        một KHOẢNG   "tháng này dôi ra?"      ║
║     Tài sản ròng = tài sản − nợ    một THỜI ĐIỂM "hôm nay tôi có?"       ║
║                                                                          ║
║  DÒNG CHẢY vs TỒN KHO   vòi nước  vs  mực nước trong bể                  ║
║     sách dạy cả hai mà KHÔNG BAO GIỜ đặt tên cho sự khác nhau            ║
║     => lỗi "tỷ lệ tiết kiệm >= số tuổi" ở C2 tr.28 sinh ra từ đây (bài 7)║
║                                                                          ║
║  TÀI SẢN RÒNG ĐỔI VÌ HAI LÝ DO                                          ║
║     Δ tài sản ròng = dòng tiền + thay đổi ĐỊNH GIÁ                       ║
║     ví dụ 3 của sách: dòng tiền = 0, mất 200 TRIỆU  (C2 tr.16)          ║
║     => cày cuốc cả tháng không đụng tới vế thứ hai                       ║
║                                                                          ║
║  CHIẾC Ô TÔ CỦA VÍ DỤ 2   tài sản ròng −90tr, xe 200tr, nợ 300tr        ║
║     bỏ qua mất giá, 3tr/tháng  ->  30 tháng   (90/3, phép chia lớp ba)   ║
║     xe mất giá 10%/năm         ->  56 tháng                              ║
║     dòng tiền 1tr/tháng: sau 12 tháng tài sản ròng −98tr — ÂM SÂU HƠN    ║
║     đáy quanh tháng 60 ở −111,9tr; thoát ở tháng 272                     ║
║     => làm mọi thứ đúng mà con số vẫn xấu đi: HAI LỰC ĐANG ĐÁNH NHAU     ║
║                                                                          ║
║  BỐN Ô                    tài sản ròng ÂM      tài sản ròng DƯƠNG        ║
║     dòng tiền DƯƠNG       đang đào lên         đang tích luỹ             ║
║     dòng tiền ÂM          khủng hoảng          ĐANG ĂN VÀO VỐN  <- nguy  ║
║                                                    nhất, vì trông vẫn ổn ║
║                                                                          ║
║  ĐỊNH NGHĨA NỢ CỦA SÁCH QUÁ HẸP   "các khoản vay để TẠO RA TÀI SẢN"      ║
║     (C1 tr.17) — bỏ sót nợ tiêu dùng => tài sản ròng CAO HƠN sự thật     ║
║                                                                          ║
║  TÀI SẢN RÒNG CŨNG LÀ MỘT Ý KIẾN                                        ║
║     nợ: biết đến từng đồng.  tài sản: ƯỚC LƯỢNG, và ta hay lạc quan      ║
║     => chặt tay với tài sản, chính xác với nợ, ghi lại giả định          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1***, Waka.vn.
  - **Unit 2 Lesson 3 *Xác định tình trạng tài chính của bạn* (tr. 10–12)** — nguồn chính: ba nguồn
    thu nhập và ba nhóm chi phí, công thức dòng tiền, trading là kinh doanh, ngưỡng 3 năm cho chữ
    "đầu tư" (tr. 11); ba mức dòng tiền, *"khi và chỉ khi dòng tiền dương…"*, ba nhóm tài sản và ba
    loại vay, công thức tài sản ròng (tr. 12)
  - Unit 3 Lesson 1 (tr. 17) — định nghĩa nợ; *"Dòng tiền thuần và Tài sản thuần luôn là con số dương"*
  - **Unit 3 Lesson 2 *Bảng cân đối tài chính cá nhân tối ưu* (tr. 18)** — *"phiên bản đơn giản hơn
    của báo cáo tài chính doanh nghiệp"*, *"tại một thời điểm nhất định"*
- ***Tài chính cá nhân 101 — Class 2***, Waka.vn.
  - Unit 2 mở đầu (tr. 14–15) — quy trình *"Pay yourself first"*; bài 7 làm phần này
  - **Unit 2 Lesson 1 *"Net worth" là gì* (tr. 15–17)** — nguồn chính: câu hỏi *"Lương tháng bao
    tiền?"* (tr. 15); công thức và **ba ví dụ** 8 triệu / âm 90 triệu / 800 triệu (tr. 16); ba lý do
    net worth quan trọng hơn lương, lạm phát lối sống, bốn quy tắc quản lý (tr. 16–17)
  - Unit 2 Lesson 5 (tr. 28) — *"lớn hơn hoặc bằng số tuổi"*, chỗ trộn dòng chảy với tồn kho; bài 7
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-02-do-hien-trang.py`](../thuc_hanh/bai-02-do-hien-trang.py).
  Ba ví dụ Net worth dựng lại và `assert` đúng con số sách in (8 triệu, âm 90 triệu, 800 triệu).
  Mọi số ở mục 5 do tệp này tính.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Cặp khái niệm **dòng chảy / tồn kho** ở [mục 4](#4-bổ-sung-dòng-chảy-và-tồn-kho--cái-tên-mà-sách-không-đặt)
    **không có trong sách**. Sách dạy cả hai đại lượng nhưng không phân loại chúng.
  - Công thức tách $\Delta$ tài sản ròng ở [mục 5](#5-bổ-sung-tài-sản-ròng-đổi-vì-hai-lý-do-sách-chỉ-đặt-tên-một)
    là của khoá học. Ví dụ số (1 tỷ → 800 triệu) thì là của sách.
  - **Toàn bộ phần chiếc ô tô mất giá** là của khoá học. Sách dừng ở con số âm 90 triệu và không
    hỏi tiếp. Tốc độ mất giá 10%/năm là **giả định**, không phải số liệu.
  - Bảng **bốn ô** ở [mục 7](#7-bổ-sung-bốn-ô--đọc-hai-con-số-cùng-lúc) do khoá học dựng từ hai câu
    của sách (C1 tr. 12 và tr. 17). Tên bốn ô và lời khuyên kèm theo là của khoá học.
  - Toàn bộ [mục 8](#8-bổ-sung-tài-sản-ròng-cũng-là-một-ý-kiến) **không có trong sách**.
- **Liên hệ chéo:**
  - Bảng cân đối kế toán ở tầm doanh nghiệp, và vì sao nó cân:
    [Trí tuệ tài chính bài 4](../../trituetaichinh/ly_thuyet/bai_04_bang_can_doi_ke_toan.md) và
    [bài 5](../../trituetaichinh/ly_thuyet/bai_05_vi_sao_bang_can_doi_lai_can.md).
  - *"Lợi nhuận là một ý kiến, tiền mặt mới là sự thật"* — bản gốc của mục 8:
    [Trí tuệ tài chính bài 6](../../trituetaichinh/ly_thuyet/bai_06_loi_nhuan_khac_tien_mat.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| **2** | **Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối** ← *bạn đang ở đây* | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
| 5 | [Kiếm tiền: vì sao được trả, Kim tứ đồ, vốn con người](bai_05_kiem_tien.md) | C2 tr. 4–13 | 1 |
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
