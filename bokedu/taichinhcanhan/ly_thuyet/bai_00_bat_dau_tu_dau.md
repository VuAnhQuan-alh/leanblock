# Bài 0 — Bắt đầu từ đâu

> Bài cầu nối, khoảng 40 phút. Không bám unit nào của sách — nó chốt **quy ước trích dẫn**, giải
> thích **vì sao khoá học xếp lại thứ tự**, và giao **bài tập số 1**.
>
> **Cần đọc trước:** không có. Đây là bài đầu tiên.
> Nếu đã học [Trí tuệ tài chính](../../trituetaichinh/README.md) thì mục 6 sẽ quen tay — cùng một
> kiểu bài tập, khác chỗ là lần này số ít hơn nhiều và tự kiểm được bằng đầu ngón tay.
>
> **Ký hiệu:** môn này **không dùng biểu tượng**. **[bổ sung]** là kiến thức ngoài sách ·
> **[đính chính]** là chỗ sách sai · **[2026]** là mục đối chiếu với hiện tại ·
> **[đã cắt]** là phần quảng bá sản phẩm đã bỏ.
>
> **Code:** [`thuc_hanh/bai-00-kiem-lai-sach.py`](../thuc_hanh/bai-00-kiem-lai-sach.py)
> — máy dò lỗi của mục 6. Tính lại từng con số sách đưa ra rồi đối chiếu. Dưới 200 dòng, chỉ dùng
> thư viện chuẩn.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Hai cuốn sách này dạy gì, và cố tình không dạy gì](#1-hai-cuốn-sách-này-dạy-gì-và-cố-tình-không-dạy-gì)
- [2. Quy ước trích dẫn — vì sao không có số trang giấy](#2-quy-ước-trích-dẫn--vì-sao-không-có-số-trang-giấy)
- [3. Ba bài toán, và bản đồ mười lăm bài](#3-ba-bài-toán-và-bản-đồ-mười-lăm-bài)
- [4. Vì sao khoá học không đi theo thứ tự sách](#4-vì-sao-khoá-học-không-đi-theo-thứ-tự-sách)
- [5. Hai mảng bổ sung, và phần đã cắt](#5-hai-mảng-bổ-sung-và-phần-đã-cắt)
- [6. Đính chính — sách sai ở đâu, và bài tập số 1](#6-đính-chính--sách-sai-ở-đâu-và-bài-tập-số-1)
- [7. Sách viết năm nào, và cái gì đã cũ](#7-sách-viết-năm-nào-và-cái-gì-đã-cũ)
- [8. Tự thử](#8-tự-thử)
- [9. Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
- [10. Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Hai cuốn sách này dạy gì, và cố tình không dạy gì

Sách tự đặt phạm vi ngay Unit 1 của tập 1. Tiền có **ba bài toán**, và chỉ ba:

> *"Nói về tiền, chúng ta có 3 bài toán cần giải quyết: **Kiếm tiền**… **Giữ tiền**… **Đầu tư tiền**."*
> — C1 tr. 4

Bài toán thứ hai mới là chỗ sách dồn sức:

> *"Vì hầu hết đều đồng ý rằng số tiền bạn kiếm được không quan trọng bằng số tiền bạn giữ được.
> Và khi tìm kiếm cụm từ 'tài chính cá nhân' trên Google thì đứng trước nó luôn có từ khoá 'quản lý'."*
> — C1 tr. 4–5

Đếm thử trên chính hai cuốn sách: phần **giữ tiền** — ghi chép, phân bổ thu nhập, vay và trả nợ,
lạm phát, quỹ khẩn cấp, bảo hiểm, lừa đảo — chiếm khoảng **hai phần ba** tổng số chữ. Phần **đầu tư**
gói gọn trong 10 trang cuối C2. Đó là tỷ trọng có chủ ý, và khoá học giữ nguyên nó.

**Sách cố tình không dạy:** cách chọn cổ phiếu, cách phân tích doanh nghiệp, cách đọc báo cáo tài
chính. Sách nói thẳng ở phần CFD rằng nó chỉ đưa *"những kiến thức cần thiết. Không quá màu mè,
không quá đa dạng. Đây là bước đệm"* (C2 tr. 55).

Ai cần phần doanh nghiệp thì sang [Trí tuệ tài chính](../../trituetaichinh/README.md) — cùng thư
mục `bokedu/`, dạy đúng thứ cuốn này bỏ qua.

---

## 2. Quy ước trích dẫn — vì sao không có số trang giấy

[EG13](../../../houedu/eg13-kinhtevimo-micro/README.md) và
[EG14](../../../houedu/eg14-kinhtevimo-macro/README.md) trích được `tr. 315` vì giáo trình Mankiw là
**bản quét** của sách in, giữ nguyên số trang giấy.

Hai tệp của môn này thì không. Metadata nói rõ chúng do **calibre 8.5.0** dàn lại — nghĩa là số
trang phụ thuộc cỡ chữ lúc chuyển đổi, **không phải số trang của bản in nào cả**.

Nên quy ước của môn này là:

```
   C2  tr. 34
   └┬┘  └──┬──┘
    │      └── số trang trong tệp PDF ở tai_lieu/ — mở ra tra được ngay
    └── tập nào: C1 = Class 1, C2 = Class 2
```

Hai tập là **hai tệp riêng**, và chúng đánh số trang độc lập. Trích `tr. 34` mà quên ghi tập thì
người đọc mở nhầm tệp sẽ ra một bài hoàn toàn khác — C1 tr. 34 là nguyên tắc SMART, C2 tr. 34 là
bảng trả góp. Vì vậy **ký hiệu tập luôn đứng trước, không bao giờ được lược**.

Mọi mốc trang trong khoá học đã được tra bằng máy chứ không gõ tay: trích từng trang một rồi tìm
chuỗi. Cách này bắt được đúng loại lỗi mà bài học về tiền không được phép mắc.

---

## 3. Ba bài toán, và bản đồ mười lăm bài

```
                        ┌─────────────── KIẾM TIỀN ───────────────┐
                        │  5  vì sao ta được trả tiền, Kim tứ đồ  │
                        │  6  [bổ sung] thuế — tiền thật về tay   │
                        └────────────────────┬────────────────────┘
                                             │
   ┌────────── ĐO ──────────┐                ▼
   │  2  dòng tiền, tài sản │   ┌─────────── GIỮ TIỀN ───────────┐
   │     ròng, bảng cân đối │   │  3  ghi chép chi tiêu          │
   │  4  tháp tài sản       │──▶│  7  phân bổ thu nhập           │
   └────────────────────────┘   │  8  vay, lãi suất thật, trả nợ │
                                │  9  lạm phát, quỹ khẩn cấp,    │
                                │     bảo hiểm                   │
                                └────────────────┬───────────────┘
                                                 │
                    ┌───── PHÒNG THỦ ─────┐      ▼
                    │ 10 [bổ sung] tài    │  ┌────── ĐẦU TƯ ──────┐
                    │    chính hành vi    │─▶│ 12 rủi ro, phân bổ │
                    │ 11 Ponzi và CFD     │  │ 13 các kênh        │
                    └─────────────────────┘  └─────────┬──────────┘
                                                       │
                                          ┌────────────▼────────────┐
                                          │ 14  SMART và ráp lại    │
                                          │     thành một kế hoạch  │
                                          └─────────────────────────┘
```

Bài 1 đứng riêng ở đầu: nó là bài duy nhất nói về **toàn cảnh** — ba bài toán và bốn bước của một
kế hoạch hoàn chỉnh (C1 tr. 5–6). Đọc xong bài 1 là biết mười ba bài sau nằm ở đâu.

Bảng đầy đủ kèm số trang nguồn nằm ở [README](../README.md#lộ-trình-15-bài).

---

## 4. Vì sao khoá học không đi theo thứ tự sách

Cách hiển nhiên nhất là đi C1 rồi C2, mỗi unit một bài, ra 10 bài. Cách đó **hỏng**, vì hai tập
**trùng nhau** chứ không nối tiếp nhau.

| Chủ đề | Sách dạy ở | Và dạy lại ở |
| --- | --- | --- |
| Tài sản ròng | C1 tr. 12 — *"Tài sản ròng = Tổng tài sản − Tổng nợ"* | C2 tr. 16 — *"Net worth = … − Số tiền đang nợ"*, kèm ba ví dụ mới |
| Bảng cân đối cá nhân | C1 tr. 18 | C2 tr. 16, dưới tên khác |
| Khẩu vị rủi ro | C1 tr. 25–27, có thang chấm điểm | C2 tr. 54 — mục *"Hai. Khẩu vị rủi ro"* trong bài blog |
| Lãi kép và thời gian | C2 tr. 19 — *"Bắt đầu sớm… tốt hơn rất nhiều so với tỷ suất sinh lời khủng"* | C2 tr. 66, lại một lần nữa |

Đi theo sách thì người học gặp tài sản ròng ở bài 2, tưởng đã xong, rồi gặp lại nguyên vẹn ở bài 7
dưới tên tiếng Anh. Ba lần lặp cho một khái niệm cộng trừ hai số.

**Khoá học gộp mỗi chủ đề về đúng một chỗ**, lấy ví dụ hay nhất từ cả hai tập. Cụ thể: bài 2 gộp
C1 tr. 10–12 với C2 tr. 15–17, giữ ba ví dụ Net worth của C2 (nhất là ví dụ chiếc ô tô cho ra
**Net worth âm 90 triệu**) vì chúng cụ thể hơn hẳn phần C1.

Hai chỗ khoá học đảo thứ tự, và lý do:

**Bài 6 (thuế) đứng trước bài 7 (phân bổ thu nhập).** Cả ba công thức của sách đều chia trên "thu
nhập", mà sách chưa lần nào nói là gộp hay ròng. Với người làm công ăn lương thì hai con số đó cách
nhau một quãng đáng kể — bảo hiểm bắt buộc trừ trước, rồi thuế. Chia 55% NEC trên lương gộp thì cái
lọ đầu tiên đã hụt trước khi bắt đầu.

**Bài 10 (tài chính hành vi) đứng trước bài 11 (Ponzi).** Sách để phần hay nhất ở cuối, trong một
bài blog phụ lục: tác giả tự nhận mình từng nghĩ nạn nhân Ponzi là *"ngu ngốc"*, rồi nhận ra
*"Người có tiền thường không ngu ngốc"* (C2 tr. 52). Nhận xét đó đúng nhưng dừng ở mô tả. Có khung
thiên kiến trước thì bài 11 giải thích được, chứ không chỉ kể lại.

---

## 5. Hai mảng bổ sung, và phần đã cắt

### Bổ sung: thuế và tài chính hành vi

Hai bài **không có trong sách**, đánh dấu **[bổ sung]** ở tiêu đề để ranh giới không nhoè:

- **Bài 6 — thuế thu nhập cá nhân.** Lý do ở mục 4.
- **Bài 10 — tài chính hành vi.** Sách chạm vào chủ đề này **bốn lần, ở bốn chỗ rời nhau**, và
  không lần nào gọi tên nó:

  | Sách viết | Ở đâu | Tên thật của hiện tượng |
  | --- | --- | --- |
  | *"sai lầm do ảnh hưởng bởi thiên kiến sống sót"* | C2 tr. 10, quy tắc 3 Kim tứ đồ | thiên kiến sống sót |
  | *"nguy cơ lạm phát lối sống (lifestyle creep)"* | C2 tr. 17 | lạm phát lối sống |
  | *"Một. Sự tham lam"* | C2 tr. 52 | — |
  | ẩn dụ Lọ Lem của Buffett, *"nhảy múa trong một căn phòng với những chiếc đồng hồ không có kim"* | C2 tr. 53 | thiên kiến lạc quan, ảo tưởng kiểm soát |

  Riêng chỗ **thiên kiến sống sót** đáng chú ý: sách dùng nó để **phản biện chính Robert Kiyosaki**
  — tác giả của Kim tứ đồ mà sách đang trình bày. Đó là đoạn sắc sảo nhất trong cả hai tập, và
  bài 5 sẽ tôn nó lên chứ không lướt qua.

### Đã cắt: nội dung thương mại

Sách đặt sản phẩm thương mại vào **vị trí phương pháp**, không phải phụ lục. Ba chỗ:

| Chỗ | Sách bảo làm gì | Khoá học thay bằng |
| --- | --- | --- |
| C1 tr. 28–29 | tải app Topi, làm 13 câu để có hồ sơ rủi ro | **bảng câu hỏi Đại học Missouri** — chính sách đã dẫn ở C1 tr. 26 là *"cách 2… (uy tín)"* |
| C1 tr. 38–39 | *"5 bước lập kế hoạch tự do tài chính **cùng TOPI**"* | bảng tính tự dựng ở bài 14 |
| C2 tr. 61 | mua vàng qua DOJI eGold / app TPBank / Topi | nêu hình thức, không nêu nhà cung cấp |

Lý do không phải đạo đức mà là **tuổi thọ**. Một bài học dạy "mở app X, bấm mục Y" sẽ chết ngay khi
X đổi giao diện. Bài học dạy *"đây là các câu hỏi cần trả lời để biết mình chịu được bao nhiêu rủi
ro"* thì không.

Chỗ đáng chú ý: sách tự đưa ra **bốn cách** xác định khẩu vị rủi ro (C1 tr. 26–28), trong đó cách 2
là bảng câu hỏi Đại học Missouri và cách 3 là một bộ trắc nghiệm khác, cả hai đều được sách gán
nhãn *"(uy tín)"*. Rồi cách 4 — Topi — được gán nhãn *"(tối ưu)"* và là cách duy nhất được dành hẳn
một lesson để hướng dẫn từng bước. Khoá học dùng **cách 2**, đúng thứ sách gọi là uy tín.

---

## 6. Đính chính — sách sai ở đâu, và bài tập số 1

Đây là hai cuốn sách dạy bạn đừng tin lời hứa lợi nhuận. Bài tập đầu tiên của môn này là:
**đừng tin con số của chính cuốn sách.**

Đừng đọc bảng đính chính ở [README](../README.md#đính-chính-sách) vội. Làm ba việc sau trước, chỉ
cần giấy bút — **không cần máy tính bỏ túi**:

### Bài tập số 1

**Việc 1.** Mở **C2 tr. 34**, phương án 4. Chị B vay **100 triệu**, trả **9 triệu mỗi tháng**, lãi
thật 8%/năm tính trên dư nợ. Sách kết luận: *"Sau 11 tháng chị B sẽ trả hết nợ."*

Nhân nhẩm: $11 \times 9 = ?$ So với 100. **Chưa cần tính một đồng lãi nào.**

**Việc 2.** Mở **C2 tr. 24**. Sách nói 30% *Wants* của quy tắc 50/30/20 *"tương ứng"* với
PLAY + EDU + GIVE của hệ 6 jars. Lật lại **C2 tr. 18–22** lấy ba con số đó ra. Cộng lại. Bằng 30?

**Việc 3.** Mở **C2 tr. 65**. Đọc đoạn nói về **quỹ đóng**, rồi đọc tiếp xuống vài dòng đến câu bắt
đầu bằng *"Chứng chỉ quỹ không được…"*. Hai câu đó **cùng một trang**. Chúng có cùng nói một điều không?

Xong ba việc rồi mới chạy máy dò để đối chiếu:

```bash
cd thuc_hanh && python3 bai-00-kiem-lai-sach.py
```

### Kết quả: hai chỗ sai, ba chỗ đúng

**Chỗ sai thứ nhất — C2 tr. 34, phương án 4.** Sách nói 11 tháng. Đúng là **12 tháng**.
$11 \times 9 = 99$ triệu, còn chưa đủ trả gốc 100 triệu, chứ chưa nói tới lãi. Máy dò dựng lại bảng
trả góp từng tháng và cho ra: tháng 12 phải trả nốt **5.250.615 đồng**. Không cách hiểu nào cứu
được con số 11 — thử trả đầu kỳ cũng 12 tháng, thử lãi phẳng 8% thì $108 \div 9 = 12$ kỳ chẵn.

**Chỗ sai thứ hai — C2 tr. 24, ánh xạ hai hệ phân bổ.** Sách nói hai hệ *"tương ứng"* nhau. Thật ra:

| Vế của 50/30/20 | Sách nói | Cộng từ 6 jars | |
| --- | ---: | ---: | --- |
| Needs | 50% | NEC = 55% | lệch $+5$ |
| Wants | 30% | PLAY + EDU + GIVE = **25%** | lệch $-5$ |
| Savings | 20% | FFA + LTSS = 20% | khớp |

Chỉ **một trong ba vế** khớp thật. Điều này không làm hỏng cả hai phương pháp — bài 7 sẽ cho thấy
5 điểm phần trăm ấy chính là chỗ hai tác giả bất đồng, chứ không phải lỗi tính toán.

**Ba chỗ đúng.** Phần lãi suất trả góp ở C2 tr. 32–33 là đoạn **chắc nhất** của cả hai tập, và
máy dò xác nhận từng con số:

| Phương án | Sách in | Tính đủ số lẻ |
| --- | ---: | ---: |
| 1 — giữ gốc cả năm | 8%/năm | 8,00% |
| 2 — trả 9tr/tháng từ tháng sau | 1,2%/tháng ⟹ **15,39%**/năm | 1,2043% ⟹ 15,45% |
| 3 — trả luôn 9tr ngay tháng này | 1,43%/tháng ⟹ **18,58%**/năm | 1,4313% ⟹ 18,59% |

Sách làm tròn ở bước trung gian, không sai. Và bài học của nó thì rất đắt: cùng một khoản vay,
cùng lời hứa *"lãi 8% thôi, bạn bè mà"*, lãi thật **gần gấp đôi** ở phương án 2 và **gấp 2,3 lần**
ở phương án 3 — chỉ vì thời điểm trả tiền khác nhau. Bài 8 làm kỹ chỗ này.

### Bốn loại lỗi, và loại nào đáng sợ

| Loại | Ví dụ | Mức nguy hiểm |
| --- | --- | --- |
| **Biên tập** | C2 tr. 32–33 gọi người đi vay là *"chị C"* bốn lần, trong khi C là người cho vay | thấp — đọc là biết |
| **Số** | phương án 4: 11 tháng thay vì 12 | trung bình — nhân nhẩm là ra |
| **Mâu thuẫn nội tại** | C2 tr. 65 nói quỹ đóng được niêm yết rồi nói chứng chỉ quỹ không được niêm yết | cao — người đọc không biết tin câu nào |
| **Khái niệm** | C2 tr. 63: *"Càng gần ngày đáo hạn thì giá trị của trái phiếu càng giảm"* | **cao nhất** — đọc xuôi tai, và **dạy sai** |

Loại **khái niệm** mới đáng sợ. Nó không làm sai phép tính nào; nó cài một hiểu biết ngược vào đầu
người đọc và ở lại đó. Câu về trái phiếu là ví dụ chuẩn: giá trái phiếu **hội tụ về mệnh giá** khi
đến hạn, nên trái phiếu đang giao dịch dưới mệnh giá thì càng gần đáo hạn giá càng **tăng**. Ai tin
câu của sách sẽ bán sớm đúng lúc không nên bán. Bài 13 quay lại đúng chỗ này.

Bảng đầy đủ cả năm lỗi khái niệm nằm ở [README](../README.md#lỗi-khái-niệm--nguy-hiểm-nhất-vì-dạy-sai).

---

## 7. Sách viết năm nào, và cái gì đã cũ

Sách **không ghi năm xuất bản** ở đâu cả. Nhưng nội dung tự khai:

| Manh mối | Ở đâu | Suy ra |
| --- | --- | --- |
| *"Lãi suất ngân hàng tại thời điểm này là 9%/năm"* | C1 tr. 23 | mức huy động cao — giai đoạn cuối 2022 đầu 2023 |
| mua *"mã cổ phiếu TNH của bệnh viện nơi anh làm việc"* | C2 tr. 10 | TNH lên sàn HOSE tháng 1/2021, nên sau mốc đó |
| *"Từ năm 2020, DOJI đã ra mắt hình thức eGold"* | C2 tr. 61 | sau 2020 |
| *"giàu có như Bill Gates với khối tài sản 114 tỷ USD"* | C1 tr. 35 | quanh 2020–2021 |

Cộng lại: **sách viết khoảng 2022–2023**. Ngày tạo tệp PDF (10/2025) chỉ là ngày calibre chuyển
đổi, không phải ngày viết.

Điều đó có nghĩa gì với người học năm 2026? Bốn mảng, và mảng đầu tiên **ảnh hưởng thẳng tới hai
phép tính chính của sách**:

| Mảng | Sách viết | Bài nào xử lý |
| --- | --- | --- |
| Lãi suất huy động 9%/năm | dùng làm mẫu số cho cả phép định giá tài sản vô hình lẫn công thức tự do tài chính | bài 4 và bài 14 |
| Trái phiếu doanh nghiệp *"Rủi ro thấp"* | không nhắc sự kiện 2022 nào | bài 13 |
| Bảo hiểm nhân thọ | khuyến khích, không cảnh báo kênh phân phối | bài 9 |
| Trần lãi vay 20%/năm | đúng con số, không dẫn luật | bài 8 |

Mảng lãi suất đáng nói riêng. Sách định giá "tài sản vô hình" của một người bằng cách chia thu nhập
năm cho lãi suất ngân hàng: 120 triệu ÷ 9% ≈ **1,3 tỷ** (C1 tr. 23). Phép chia đó có hai vấn đề,
và cả hai đều nằm sẵn trong chính cuốn sách:

**Một, mẫu số đã đổi.** Lãi suất thấp hơn thì thương số lớn hơn — cùng một người, cùng thu nhập, giá
trị nhảy lên đáng kể chỉ vì ngân hàng hạ lãi. Con số nói về **thị trường tiền tệ** nhiều hơn nói về
người được định giá.

**Hai, công thức giả định thu nhập chảy về vĩnh viễn.** Chia cho lãi suất là phép vốn hoá một dòng
tiền **không bao giờ dừng**. Nhưng C2 tr. 13 nói ngược lại:

> *"vốn con người sẽ giảm theo thời gian, do tuổi trẻ là giai đoạn tốt nhất cho sự học hỏi và phát
> triển, nhưng càng lớn tuổi thì 'vốn' sẽ giảm đi liền với sức khỏe bản thân."* — C2 tr. 13

Hai chỗ không thể cùng đúng. Máy dò tính thử với số năm đi làm còn lại hữu hạn:

```
   còn 10 năm  ->    770.118.924 đồng   (58% con số của sách)
   còn 20 năm  ->  1.095.425.480 đồng   (82%)
   còn 30 năm  ->  1.232.838.485 đồng   (92%)
   còn 40 năm  ->  1.290.883.223 đồng   (97%)
```

Người 45 tuổi còn 20 năm đi làm thì "tài sản vô hình" của họ là **1,1 tỷ**, không phải 1,3 tỷ.
Khoảng cách giữa hai cách tính chính là điều mà C2 tr. 13 muốn nói. Bài 4 làm kỹ chỗ này.

Công thức tự do tài chính ở C1 tr. 31 cũng nhạy y hệt. Sách lấy chi tiêu 120 triệu/năm, lợi suất
kỳ vọng 12%, lạm phát 4%, ra **1,5 tỷ**. Đổi mỗi giả định lợi suất:

```
   lợi suất 12%  ->  cần  1.500.000.000  (con số của sách)
   lợi suất 10%  ->  cần  2.000.000.000
   lợi suất  8%  ->  cần  3.000.000.000   gấp đôi
   lợi suất  6%  ->  cần  6.000.000.000   gấp bốn
```

Một giả định, chênh nhau bốn lần. Đây không phải lỗi của sách — công thức đúng. Nhưng nó cho thấy
**con số 1,5 tỷ không phải một sự thật, nó là một hệ quả của giả định**, và giả định 12%/năm bền
vững suốt vài chục năm là giả định mạnh. Bài 14 đối chiếu nó với các cách ước lượng thận trọng hơn.

---

## 8. Tự thử

1. **Kiểm phương án 4 bằng đầu ngón tay.** Không mở máy dò, không dùng máy tính. Chị B trả 9
   triệu/tháng cho khoản vay 100 triệu. Bỏ qua lãi hoàn toàn. **Ít nhất** bao nhiêu tháng mới trả
   hết? Vậy con số 11 của sách sai kể cả trong trường hợp thuận lợi nhất — trường hợp nào?

2. **Đổi số tiền trả hàng tháng.** Trong `bai-00-kiem-lai-sach.py`, sửa `TRA_HANG_THANG` từ 9 lên
   10 triệu. Chạy lại. Phương án 4 hết nợ sau bao nhiêu tháng? Tổng tiền lãi trả ra thay đổi thế nào?
   Nhớ sửa lại.

3. **Đảo ngược máy dò.** Vẫn trong tệp đó, sửa `SAU_LO["NEC"]` từ 55 xuống 50. Chạy lại. **Bao
   nhiêu** `assert` gãy, và cái nào gãy trước? Điều đó nói gì về việc 6 jars có cộng ra 100% không?

4. **Tìm mốc thời gian thứ năm.** Mục 7 dùng bốn manh mối để định vị năm viết sách. Đọc lướt cả hai
   tập, tìm **một manh mối nữa** — một con số, một sự kiện, một sản phẩm — và xem nó ủng hộ hay
   phản bác mốc 2022–2023.

5. **Perpetuity với lãi suất hôm nay.** Lấy lãi suất huy động kỳ hạn 12 tháng của một ngân hàng bất
   kỳ hôm nay. Áp vào công thức C1 tr. 23 với thu nhập 120 triệu/năm. Ra bao nhiêu? Bạn có thấy con
   số đó mô tả **bạn**, hay mô tả **ngân hàng**?

6. **Tự do tài chính, giả định của riêng bạn.** Công thức C1 tr. 31 cần ba đầu vào: chi tiêu năm,
   lợi suất kỳ vọng, lạm phát. Điền số của chính bạn, nhưng làm **hai lần**: một lần lạc quan, một
   lần thận trọng. Khoảng cách giữa hai kết quả là bao nhiêu năm làm việc?

---

## 9. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Tài chính cá nhân | personal finance | ba bài toán: kiếm, giữ, đầu tư — C1 tr. 4 |
| Dòng tiền | cash flow | tổng thu nhập − tổng chi phí, đo trong **một khoảng** thời gian |
| Tài sản ròng | net worth | tổng tài sản − tổng nợ, đo tại **một thời điểm** |
| Tài sản | assets | thứ tạo ra lợi ích trong tương lai; sách chia đầu tư / tiêu dùng — C1 tr. 16 |
| Tiêu sản | liability (theo cách gọi của Kiyosaki) | thứ lấy tiền ra khỏi túi; sách gọi khái niệm này là *"sơ sài"* — C1 tr. 16 |
| Tháp tài sản | asset pyramid | mô hình phân tầng tài sản theo rủi ro — C1 tr. 19 |
| Hồ sơ rủi ro | risk profile | mức rủi ro một người chịu được — C1 tr. 25 |
| Tỷ lệ tiết kiệm | savings rate | $1 -$ chi tiêu / thu nhập — C2 tr. 26 |
| Vốn con người | human capital | chuyên môn cộng quan hệ; **giảm** theo tuổi — C2 tr. 11–13 |
| Vốn tài chính | financial capital | tổng tài sản trừ nợ — C2 tr. 11 |
| Đòn bẩy tài chính | financial leverage | vay để đầu tư — C2 tr. 29 |
| Quỹ khẩn cấp | emergency fund | tiền cho việc **không lường trước** — C2 tr. 43 |
| Quỹ chi tiêu | sinking fund | tiền cho việc **đã lên kế hoạch** — C2 tr. 45 |
| Lạm phát lối sống | lifestyle creep | chi tiêu phình theo lương — C2 tr. 17 |
| **[bổ sung]** Thu nhập gộp / ròng | gross / net income | trước và sau bảo hiểm bắt buộc và thuế — **không có trong sách**, bài 6 |
| **[bổ sung]** Tỷ suất rút an toàn | safe withdrawal rate | rút bao nhiêu mỗi năm mà không cạn vốn — **không có trong sách**, bài 14 |

---

## 10. Câu hỏi tự kiểm tra

1. Ba bài toán của tiền là gì? Sách dồn sức vào bài toán nào, và câu nào chứng minh điều đó? (mục 1)
2. Hai cuốn sách này **cố tình không dạy** gì? Trong kho có môn nào dạy phần đó? (mục 1)
3. Vì sao ký hiệu tập (`C1`/`C2`) **không bao giờ được lược** khi trích dẫn? (mục 2)
4. Kể **ba** chủ đề mà hai tập sách dạy trùng nhau. Khoá học xử lý sự trùng lặp đó bằng cách nào? (mục 4)
5. Vì sao bài thuế phải đứng **trước** bài phân bổ thu nhập? Sai mẫu số thì hỏng cái gì? (mục 4)
6. Sách chạm vào tài chính hành vi ở **bốn chỗ**. Kể ít nhất hai, và nói vì sao chúng cần một bài riêng. (mục 5)
7. Sách gán nhãn *"uy tín"* cho cách nào, *"tối ưu"* cho cách nào, khi xác định khẩu vị rủi ro?
   Khoá học chọn cách nào và vì sao? (mục 5)
8. Không dùng máy tính: chứng minh phương án 4 ở C2 tr. 34 sai. Cần đúng **một** phép nhân. (mục 6)
9. Trong ba vế của 50/30/20, vế nào thật sự khớp với 6 jars? Hai vế còn lại lệch bao nhiêu điểm phần trăm? (mục 6)
10. Bốn loại lỗi in trong sách — loại nào nguy hiểm nhất và **vì sao**? Cho ví dụ. (mục 6)
11. Giá trái phiếu khi càng gần ngày đáo hạn thì thế nào? Sách nói gì, và ai tin sách sẽ hành động sai ra sao? (mục 6)
12. Kể **ba** manh mối định vị năm viết sách. (mục 7)
13. Phép tính "tài sản vô hình = thu nhập năm ÷ lãi suất" giả định điều gì về tương lai? Câu nào
    trong chính cuốn sách mâu thuẫn với giả định đó? (mục 7)
14. Với cùng chi tiêu 120 triệu/năm và lạm phát 4%, số tiền cần cho tự do tài chính ở lợi suất 12%
    và ở lợi suất 6% chênh nhau **mấy lần**? (mục 7)
15. Vì sao con số 1,5 tỷ ở C1 tr. 31 **không phải một sự thật**? (mục 7)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 0 — BẮT ĐẦU TỪ ĐÂU                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  BA BÀI TOÁN     kiếm tiền  ·  GIỮ TIỀN  ·  đầu tư tiền                  ║
║                              ↑ 2/3 số chữ của cả hai tập                 ║
║  SÁCH KHÔNG DẠY  chọn cổ phiếu, đọc báo cáo tài chính                    ║
║                  → sang bokedu/trituetaichinh                            ║
║                                                                          ║
║  TRÍCH DẪN   C2 tr. 34   — PDF do calibre dàn, KHÔNG có số trang giấy    ║
║              ký hiệu tập LUÔN đứng trước: C1 tr.34 = SMART               ║
║                                           C2 tr.34 = bảng trả góp        ║
║                                                                          ║
║  KHÔNG ĐI THEO THỨ TỰ SÁCH — hai tập TRÙNG nhau, không nối tiếp         ║
║     tài sản ròng dạy 2 lần · bảng cân đối 2 lần · khẩu vị rủi ro 2 lần   ║
║     bài 6 (thuế) trước bài 7  — 3 công thức đều chia trên thu nhập RÒNG  ║
║     bài 10 (hành vi) trước bài 11 — có khung mới giải thích được Ponzi   ║
║                                                                          ║
║  BÀI TẬP SỐ 1:  ĐỪNG TIN CON SỐ CỦA CHÍNH CUỐN SÁCH                      ║
║     C2 tr.34  "11 tháng"  ->  12 tháng.  11 x 9tr = 99tr < gốc 100tr     ║
║     C2 tr.24  Wants 30%   ->  PLAY+EDU+GIVE = 25%. Chỉ Savings khớp      ║
║     C2 tr.65  quỹ đóng "được niêm yết" / CCQ "không được niêm yết"       ║
║               — cùng một trang                                           ║
║     nguy nhất: C2 tr.63 "gần đáo hạn giá trái phiếu càng giảm" — NGƯỢC   ║
║                                                                          ║
║  ĐÚNG VÀ RẤT ĐẮT   C2 tr.32-33 lãi suất trả góp, kiểm từng số:          ║
║     hứa 8%/năm  ->  thật 15,39%  (trả góp)  ->  18,58%  (trả ngay kỳ 1)  ║
║                                                                          ║
║  SÁCH VIẾT ~2022-2023   lãi huy động 9% · TNH lên sàn 1/2021 · eGold 2020║
║     lãi suất đổi  =>  "tài sản vô hình 1,3 tỷ" và "tự do tài chính       ║
║     1,5 tỷ" đều đổi theo. Lợi suất 12% -> 6% thì cần GẤP BỐN LẦN         ║
║                                                                          ║
║  ĐÃ CẮT   Topi (2 chỗ) · DOJI eGold — thay bằng cách không phụ thuộc app ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1: Lập kế hoạch tài chính cá nhân***, Waka.vn.
  Tệp trong kho: `tai_lieu/Tài Chính Cá Nhân 101 - Class 1_ Lập Kế Hoạch Tài Chính Cá Nhân - Waka.pdf`
  — **40 trang PDF**, dàn bằng calibre 8.5.0, **không mang số trang bản in**.
  - Unit 1 *Tài chính cá nhân là gì?* (tr. 4–6) — ba bài toán, bốn bước
  - Unit 2 Lesson 3 *Xác định tình trạng tài chính* (tr. 10–12) — dòng tiền, tài sản ròng
  - Unit 3 Lesson 1 *Khái niệm tài sản* (tr. 16–17) — tài sản, tiêu sản, nợ
  - Unit 3 Lesson 3 *Kim tự tháp tài sản* (tr. 19–24) — năm lớp; định giá tài sản vô hình ở tr. 23
  - Unit 4 Lesson 1 *Khẩu vị rủi ro* (tr. 25–27) — bốn cách xác định
  - Unit 4 Lesson 2 (tr. 28–29) — hướng dẫn Topi, **đã cắt**
  - Unit 4 Lesson 2 phần tổng kết (tr. 31) — công thức số tiền cần cho tự do tài chính
  - Unit 5 Lesson 1 *Đặt mục tiêu tài chính* (tr. 34–37) — SMART; Bill Gates 114 tỷ USD ở tr. 35
  - Unit 5 Lesson 2 (tr. 38–39) — 5 bước cùng TOPI, **đã cắt**
- ***Tài chính cá nhân 101 — Class 2: Nâng cao năng lực tài chính cá nhân***, Waka.vn.
  Tệp trong kho: `tai_lieu/Tài Chính Cá Nhân 101 - Class 2_ Nâng Cao Năng Lực Tài Chính Cá Nhân - Waka.pdf`
  — **68 trang PDF**, cùng nguồn dàn trang.
  - Unit 1 Lesson 2 *Cashflow Quadrant* (tr. 6–10) — bốn quy tắc; thiên kiến sống sót ở tr. 10
  - Unit 1 Lesson 3 *Vốn và mô hình thu nhập* (tr. 11–13) — vốn con người giảm theo tuổi, tr. 13
  - Unit 2 Lesson 1 *"Net worth"* (tr. 15–17) — ba ví dụ; lạm phát lối sống ở tr. 17
  - Unit 2 Lesson 2 *Hệ thống "6 jars"* (tr. 18–22) — sáu tỷ lệ
  - Unit 2 Lesson 3 *Quy tắc 50/30/20* (tr. 23–24) — ánh xạ sang 6 jars ở tr. 24
  - Unit 2 Lesson 5 *Tỷ lệ tiết kiệm* (tr. 26–28) — quy tắc theo số tuổi ở tr. 28
  - Unit 3 Lesson 1 *Các hình thức vay tiền* (tr. 29–31) — đòn bẩy; trần 20%/năm ở tr. 31
  - Unit 3 Lesson 2 *Lãi suất* (tr. 31–34) — bốn phương án; phương án 4 sai ở tr. 34
  - Unit 4 Lesson 1 *Lạm phát* (tr. 39–42) — ba mức độ, ngưỡng 1000% ở tr. 40
  - Unit 4 Lesson 4 *Mô hình Ponzi* (tr. 47–53) — gọi Ponzi là đa cấp kim tự tháp ở tr. 48;
    bài blog và ẩn dụ Lọ Lem ở tr. 52–53
  - Unit 5 Lesson 2 *Đầu tư vào vàng* (tr. 60–61) — 1,8%/năm ở tr. 59; eGold ở tr. 61
  - Unit 5 Lesson 3 *Đầu tư trái phiếu* (tr. 62–63) — ưu nhược điểm; câu về đáo hạn ở tr. 63
  - Unit 5 Lesson 4 *Chứng chỉ quỹ và ETF* (tr. 63–67) — mâu thuẫn niêm yết ở tr. 65
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-00-kiem-lai-sach.py`](../thuc_hanh/bai-00-kiem-lai-sach.py).
  Mọi con số trong mục 6 và mục 7 đều do tệp này tính ra, không gõ tay.
- **Chỗ đã ghi rõ để không nhoè ranh giới:**
  - Sơ đồ mười lăm bài ở [mục 3](#3-ba-bài-toán-và-bản-đồ-mười-lăm-bài) do khoá học dựng; sách
    không có bản đồ nào như vậy.
  - Toàn bộ [mục 4](#4-vì-sao-khoá-học-không-đi-theo-thứ-tự-sách) là quyết định biên tập của khoá
    học, **không phải nội dung sách**.
  - Phép tính chuỗi hữu hạn ở [mục 7](#7-sách-viết-năm-nào-và-cái-gì-đã-cũ) **không có trong sách** —
    sách chỉ đưa phép chia vĩnh viễn. Bảng độ nhạy theo lợi suất cũng vậy.
  - Ngưỡng siêu lạm phát 50%/tháng và khái niệm *pull to par* **không có trong sách**.
- **Liên hệ chéo:**
  - Lạm phát ở tầm nền kinh tế: [EG14 — Kinh tế vĩ mô](../../../houedu/eg14-kinhtevimo-macro/README.md).
  - Giá trị hiện tại và chiết khấu:
    [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md).
  - Tài sản và nợ ở tầm doanh nghiệp:
    [Trí tuệ tài chính bài 4](../../trituetaichinh/ly_thuyet/bai_04_bang_can_doi_ke_toan.md).
  - IRR — cùng công cụ dùng ở mục 6:
    [Trí tuệ tài chính bài 10](../../trituetaichinh/ly_thuyet/bai_10_tinh_ty_le_hoan_von_dau_tu.md).

<!-- BAN-DO -->
**Bản đồ khoá học**

| # | Bài | Nguồn | Vòng |
| ---: | --- | --- | :---: |
| **0** | **Bắt đầu từ đâu** ← *bạn đang ở đây* | — | 2 |
| 1 | [Tài chính cá nhân là gì](bai_01_tai_chinh_ca_nhan_la_gi.md) | C1 tr. 4–6 | 1 |
| 2 | [Đo hiện trạng: dòng tiền, tài sản ròng, bảng cân đối](bai_02_do_hien_trang.md) | C1 tr. 10–12, 18 · C2 tr. 15–17 | 1 |
| 3 | [Ghi chép chi tiêu và phương pháp Kakeibo](bai_03_ghi_chep_chi_tieu.md) | C1 tr. 7–10 | 1 |
| 4 | [Tài sản, tiêu sản, tháp tài sản](bai_04_tai_san_tieu_san_thap_tai_san.md) | C1 tr. 16–24 | 1 |
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
