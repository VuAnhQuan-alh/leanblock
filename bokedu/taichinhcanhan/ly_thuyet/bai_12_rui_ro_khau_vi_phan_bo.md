# Bài 12 — Rủi ro, khẩu vị rủi ro, phân bổ tài sản

> [!info] Về bài này
> Bài học dựa trên **C1 tr. 25–33** — Unit 4 (*Hồ sơ rủi ro*) Lesson 1–3 của *Tài chính cá nhân 101,
> Class 1*. Có dùng thêm đoạn *"Hai. Khẩu vị rủi ro"* ở **C2 tr. 54** (bài blog) như minh hoạ sống.
> **Cần đọc trước:** [Bài 11](bai_11_nhan_dien_lua_dao.md) — sách gọi CFD và coin là *"những kênh
> rủi ro nhất"* (C1 tr. 32); bài này cho cái thước để đo *"rủi ro"* ấy là bao nhiêu so với sức chịu
> của bạn. Và [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md) — tháp tài sản chia lớp an toàn /
> tăng trưởng / mạo hiểm chính là phân bổ tài sản nhìn từ một góc khác.
> **[đã cắt]:** Lesson 2 của sách (C1 tr. 28–31) là **hướng dẫn dùng app Topi**. Khoá học cắt phần
> phụ thuộc nhà cung cấp và thay bằng **bảng câu hỏi Đại học Missouri** — chính sách đã dẫn nó ở
> tr. 26 là *"cách 2… (uy tín)"*. Lý do ở [mục 3](#3-bốn-cách-đo-và-đã-cắt-vì-sao-bỏ-topi-thay-bằng-missouri).
> **Ký hiệu:** **[bổ sung]** là kiến thức ngoài sách · **[đính chính]** là chỗ sách sai ·
> **[đã cắt]** là phần thương mại thay bằng cách khác · **[2026]** là mục đối chiếu hiện tại.
> **Code:** [`thuc_hanh/bai-12-rui-ro-khau-vi.py`](../thuc_hanh/bai-12-rui-ro-khau-vi.py)
> — kiểm hai con số sách để trống: kỳ vọng thật của danh mục "Cân bằng", và số tiền tự do tài chính
> đổi thế nào khi lợi suất kỳ vọng đổi. Công thức một dòng kèm theo để tự tính tay.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).

---

## Mục lục

<!-- MUC-LUC -->
- [1. Một hồ sơ rủi ro trả lời ba câu](#1-một-hồ-sơ-rủi-ro-trả-lời-ba-câu)
- [2. Khẩu vị rủi ro, và [bổ sung] hai thứ sách để lẫn](#2-khẩu-vị-rủi-ro-và-bổ-sung-hai-thứ-sách-để-lẫn)
- [3. Bốn cách đo, và [đã cắt] vì sao bỏ Topi thay bằng Missouri](#3-bốn-cách-đo-và-đã-cắt-vì-sao-bỏ-topi-thay-bằng-missouri)
- [4. Sáu hồ sơ và danh mục mẫu](#4-sáu-hồ-sơ-và-danh-mục-mẫu)
- [5. [bổ sung] Con số 12% gánh quá nặng](#5-bổ-sung-con-số-12-gánh-quá-nặng)
- [6. [bổ sung] Công thức tự do tài chính, và cái giá của an toàn](#6-bổ-sung-công-thức-tự-do-tài-chính-và-cái-giá-của-an-toàn)
- [7. Tại sao phân bổ tài sản — rủi ro, biến động, DCA, và câu hay nhất](#7-tại-sao-phân-bổ-tài-sản--rủi-ro-biến-động-dca-và-câu-hay-nhất)
- [8. Ráp lại và cầu sang bài 13](#8-ráp-lại-và-cầu-sang-bài-13)
- [9. Tự thử](#9-tự-thử)
- [10. Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
- [11. Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Một hồ sơ rủi ro trả lời ba câu

Unit 4 tên là *"Hồ sơ rủi ro"* và đi qua ba việc, mà đọc rời thì tưởng là ba bài. Thật ra chúng là
**ba câu hỏi nối tiếp**, câu sau dựa trên câu trước:

```
   1. BẠN chịu được bao nhiêu rủi ro?      -> khẩu vị rủi ro   (Lesson 1)
   2. Vậy nên chia tiền vào đâu?           -> phân bổ tài sản   (Lesson 2, 3)
   3. Thế thì bao lâu mới đủ / đủ là bao nhiêu?  -> công thức tự do tài chính (tr. 31)
```

Thứ tự này quan trọng: **khẩu vị rủi ro đứng trước, kênh đầu tư đứng sau.** Sách nói thẳng điều đó ở
tr. 32 — *"Hướng tiếp cận đúng phải là xác định mức độ chấp nhận rủi ro của mỗi cá nhân. Từ đó mới
lựa chọn các kênh đầu tư phù hợp."* Ai chọn mã cổ phiếu trước rồi mới hỏi mình chịu được bao nhiêu là
làm ngược. Đó cũng là lý do bài này đứng trước **bài 13** (các kênh đầu tư):
biết sức chịu rồi mới bàn tới chỗ để tiền.

---

## 2. Khẩu vị rủi ro, và [bổ sung] hai thứ sách để lẫn

Định nghĩa của sách gọn và đúng (C1 tr. 25):

> [!quote]
> *"Khẩu vị rủi ro… là mức độ rủi ro mà nhà đầu tư (cá nhân hoặc tổ chức) sẵn sàng chấp nhận để theo
> đuổi các mục tiêu của mình."*

Điểm quan trọng nhất, và sách nhấn đúng ở tr. 31: **khẩu vị rủi ro mỗi người một khác** —
*"Không có lời khuyên nào đúng cho tất cả các trường hợp."* Minh hoạ sống nằm ngay trong bài blog ở
C2 tr. 54, nơi tác giả tự khai khẩu vị của mình rồi so với người khác:

| Người | Khẩu vị (lời của họ, C2 tr. 54) |
| --- | --- |
| Tác giả (*"tôi là rùa"*) | đầu tư giá trị cổ phiếu, *"hài lòng nếu mức lợi nhuận 20%~25%/năm"*; *"từ 5%/tháng trở lên được coi là rủi ro"* |
| *"nhiều người"* | *"10%/tháng vẫn 'khả thi' lắm"* |

Cùng một thị trường, hai người ở hai đầu — và cả hai đều có thể là lựa chọn hợp lý *cho chính họ*.
Đó là toàn bộ ý nghĩa của việc đo khẩu vị: không phải để tìm con số đúng, mà để tìm **con số của
bạn**.

### [bổ sung] Sách để lẫn hai phép đo khác loại

Lesson 1 mở đầu bằng một **ma trận 5×5** (tr. 25): chấm *"Khả năng xảy ra"* (1–5) nhân *"Hậu quả"*
(1–5), ra điểm 1–25. Ngay sau đó là câu *"Làm thế nào để xác định khẩu vị rủi ro?"* với bốn bộ câu
hỏi. Nhưng **hai thứ này đo hai đại lượng khác nhau**, và để cạnh nhau dưới một tiêu đề thì dễ tưởng
là một:

| | Ma trận 5×5 (tr. 25) | Bốn bộ câu hỏi (tr. 26–29) |
| --- | --- | --- |
| Đo cái gì | **một khoản đầu tư nguy tới đâu** | **bạn chịu được bao nhiêu** |
| Kết quả | điểm rủi ro của *khoản đó* (1–25) | hồ sơ rủi ro của *bạn* |
| Câu hỏi nó trả lời | *"cái này rủi ro thế nào?"* | *"tôi hợp với mức rủi ro nào?"* |

Cả hai đều dùng được, nhưng **đừng lẫn**: ma trận nói cái đầu tư đáng sợ tới đâu; bộ câu hỏi nói bạn
gan tới đâu. Chọn kênh đúng cần **cả hai** — một khoản điểm 20/25 mà khẩu vị bạn thấp thì tránh, dù
người khác vẫn mua.

---

## 3. Bốn cách đo, và [đã cắt] vì sao bỏ Topi thay bằng Missouri

Sách đưa **bốn cách** xác định khẩu vị rủi ro (tr. 26–29), và tự dán nhãn cho từng cách:

| Cách | Là gì | Nhãn của sách |
| --- | --- | --- |
| 1 | sơ đồ hỏi Có/Không nhanh | — |
| 2 | **Bảng câu hỏi Đại học Missouri** (`pfp.missouri.edu`) | **"(uy tín)"** |
| 3 | trắc nghiệm TheFreeFinancialadvisor | **"(uy tín)"** |
| 4 | tạo hồ sơ + nhận khuyến nghị phân bổ **trên app Topi** | **"(tối ưu)"** |

Chú ý cái nhãn: hai công cụ **miễn phí, có nguồn học thuật** thì sách gọi là *"uy tín"*, còn **app
thương mại** thì được phong *"tối ưu"* — rồi toàn bộ Lesson 2 (tr. 28–31) là hướng dẫn từng bước
đăng nhập, khảo sát, đọc kết quả **trên Topi**. Đây đúng là kiểu *đặt sản phẩm thương mại vào vị trí
phương pháp* mà [bài 0](bai_00_bat_dau_tu_dau.md) đã nêu là lý do khoá học cắt.

### [đã cắt] Lý do không phải đạo đức, mà là tuổi thọ

Một bài học phải còn dùng được khi app đổi chính sách hoặc ngừng chạy. Link `app.topi.vn/wakavn` in
ở tr. 28 cần kiểm lại trước khi tin; còn một bảng câu hỏi học thuật thì không phụ thuộc nhà cung cấp
nào. Nên khoá học **thay Cách 4 bằng Cách 2** — chính cái sách đã gọi là *"uy tín"*:

> [!note]
> **Bảng câu hỏi Đại học Missouri** — *Investment Risk Tolerance Assessment*, dựng trên thang **Grable
> & Lytton (1999)**, **13 câu**, miễn phí, không cần cài app:
> `https://pfp.missouri.edu/research/investment-risk-tolerance-assessment/`

Làm mất chừng 5 phút, ra một điểm số xếp bạn vào một mức chịu rủi ro. Sách khuyên làm lại **định kỳ
6 tháng/lần** (tr. 28) — giữ nguyên lời khuyên đó, chỉ đổi công cụ. Phần *"khuyến nghị phân bổ tài
sản"* mà Topi đưa ra thì khoá học không mượn: nó tự dựng ở **bài 13** (các
kênh) và **bài 14** (ráp thành kế hoạch), từ chính các bài trước.

---

## 4. Sáu hồ sơ và danh mục mẫu

Kết quả khảo sát xếp bạn vào **một trong sáu hồ sơ rủi ro** (HSRR), sách liệt kê ở tr. 29 theo thứ
tự từ ngại rủi ro nhất tới ưa rủi ro nhất:

```
   Rất an toàn -> Thận trọng -> Thận trọng vừa phải -> Cân bằng -> Tăng trưởng -> Tăng trưởng mạnh
        (lợi nhuận kỳ vọng tăng dần, và rủi ro cũng tăng dần theo)
```

Mỗi hồ sơ ứng với một **danh mục mẫu**. Sách chỉ in ví dụ một hồ sơ — *Cân bằng* (tr. 30), qua ảnh
chụp app:

| Lớp tài sản | Tỷ trọng |
| --- | ---: |
| Tiền gửi tiết kiệm | 40% |
| Trái phiếu | 25% |
| Vàng | 5% |
| Cổ phiếu | 30% |
| **Lợi nhuận kỳ vọng (app ghi)** | **12%/năm** |

Đây là danh mục cụ thể duy nhất trong cả chủ đề, nên đáng soi kỹ — và soi kỹ thì con số **12%** có
vấn đề. Mục sau nói riêng.

---

## 5. [bổ sung] Con số 12% gánh quá nặng

Danh mục *Cân bằng* có **40% tiền gửi tiết kiệm** — lớp gần như không sinh lời thực (xem
[bài 9 mục 5](bai_09_bao_ve.md#5-bổ-sung-lạm-phát-nối-thẳng-với-bài-8-lãi-suất-thật)). Một danh mục
mà gần một nửa nằm ở tiết kiệm thì **không thể kỳ vọng 12%/năm**. Thử ráp lại bằng lợi suất hợp lý
cho từng lớp:

| Lớp | Tỷ trọng | Kỳ vọng thành phần (giả định) | Góp vào |
| --- | ---: | ---: | ---: |
| Tiền gửi tiết kiệm | 40% | 5% | 2,00% |
| Trái phiếu | 25% | 7% | 1,75% |
| Vàng | 5% | 5% | 0,25% |
| Cổ phiếu | 30% | 12% | 3,60% |
| **Cả danh mục** | 100% | | **≈ 7,6%** |

*(Lợi suất thành phần là **giả định của bài này**, không phải của sách — nhưng dù rộng tay tới đâu,
40% tiết kiệm cũng kéo trung bình xuống xa 12%.)*

**Kỳ vọng thật của danh mục này chừng 7–8%, không phải 12%.** Con số 12% có lẽ là mức của một hồ sơ
*Tăng trưởng mạnh* (gần như toàn cổ phiếu) bị gán nhầm cho hồ sơ *Cân bằng*. Vì sao chuyện này không
nhỏ: chính con số ấy đi thẳng vào công thức tự do tài chính ở mục sau, và một điểm phần trăm ở mẫu số
đổi số tiền cần có tới **hàng tỷ**. Đây đúng tinh thần *"chú ý chữ KỲ VỌNG"* mà chính sách dạy ở
tr. 32 ([mục 7](#7-tại-sao-phân-bổ-tài-sản--rủi-ro-biến-động-dca-và-câu-hay-nhất)) — kỳ vọng phải
khớp với danh mục, không phải một con số đẹp gắn lên cho vui.

---

## 6. [bổ sung] Công thức tự do tài chính, và cái giá của an toàn

Ý thứ ba của sách ở tr. 31 là một công thức đáng nhớ:

```
   Số tiền cần cho tự do tài chính = Chi tiêu theo phong cách sống mong muốn
                                     ────────────────────────────────────────
                                        Lợi suất HSRR  −  Lạm phát
```

Ví dụ của sách: chi 120tr/năm, lợi suất HSRR 12%, lạm phát 4% ⟹ **120 / (12% − 4%) = 1,5 tỷ**. Đây
là cùng một công thức tự do tài chính đã gặp ở
[bài 1](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách):
sống bằng **lợi suất thực** của khối tài sản mà không đụng vào gốc.

Chỗ sách không nói: **mẫu số là lợi suất thực (đã trừ lạm phát), nên hồ sơ càng an toàn thì số tiền
cần càng phình — rất nhanh.** Giữ nguyên chi 120tr/năm và lạm phát 4%, đổi lợi suất theo hồ sơ:

| Hồ sơ (lợi suất kỳ vọng) | Mẫu số thực | Số tiền cần có |
| --- | ---: | ---: |
| Tăng trưởng mạnh (12%) | 8% | **1,5 tỷ** |
| Cân bằng — **thật ~7,6%** (mục 5) | 3,6% | **3,33 tỷ** |
| Thận trọng (8%) | 4% | 3,0 tỷ |
| Thận trọng vừa phải (6%) | 2% | 6,0 tỷ |
| Rất an toàn (5%) | 1% | **12,0 tỷ** |
| toàn tiết kiệm ≈ lạm phát (4%) | 0% | **bất khả** |

Hai điều rút ra, cả hai đều là hệ quả trực tiếp của công thức:

1. **An toàn có giá của nó.** Chọn hồ sơ ngại rủi ro không phải là miễn phí — nó **nhân số vốn bạn
   cần lên nhiều lần**. Người muốn tự do tài chính bằng danh mục 5%/năm cần gấp **tám lần** người
   chấp nhận 12%. Đây là mặt kia của *"high risk high expected return"*: ít rủi ro thì cũng ít kỳ
   vọng, và ít kỳ vọng thì đích lùi ra rất xa.
2. **Dùng đúng con số 12% của mục 5 mới ra 1,5 tỷ; dùng con số thật ~7,6% thì phải 3,33 tỷ.** Con số
   kỳ vọng thổi phồng khiến tự do tài chính trông gần gấp đôi so với thực. Sai ở mẫu số thì sai cả
   kế hoạch — đúng lý do mục 5 phải bắt lỗi con số 12%.

*(Con số cho các hồ sơ khác 12% là **[bổ sung]** để minh hoạ độ nhạy của công thức; sách chỉ đưa ví
dụ 12% ⟹ 1,5 tỷ.)*

---

## 7. Tại sao phân bổ tài sản — rủi ro, biến động, DCA, và câu hay nhất

Lesson 3 (tr. 31–33) trả lời *"tại sao nên phân bổ tài sản"*, bắt đầu từ định nghĩa rủi ro (tr. 31):

> [!quote]
> *"Rủi ro (Risk) là khả năng có điều gì đó xấu xảy ra hoặc khi mọi thứ không diễn ra như kỳ vọng…
> mất một phần hoặc toàn bộ vốn."*

**Hai loại rủi ro** (tr. 32):

| Loại | Sách mô tả | Phân bổ tài sản có đỡ được không |
| --- | --- | --- |
| **Rủi ro hệ thống** (*systematic*) | ảnh hưởng **toàn bộ** thị trường, *"chắc chắn sẽ xảy ra… chỉ có thể chuẩn bị vài biện pháp giảm bớt thiệt hại"* | **không tránh được** — chỉ giảm nhẹ |
| **Rủi ro cụ thể / phi hệ thống** (*unsystematic*) | ở *"khoản đầu tư riêng lẻ, cá biệt"* | **có** — đa dạng hoá làm loãng nó đi |

Đây là lý do cốt lõi của đa dạng hoá: nó không cứu bạn khỏi một cú sập cả thị trường, nhưng nó xoá
được cái rủi ro của việc **bỏ hết trứng vào một mã**. Sách chốt đúng bản chất (tr. 33):
*"Bản chất của việc phân bổ tài sản chính là đa dạng hóa."*

### Câu hay nhất của cả bài

Ngay giữa Lesson 3, sách viết một câu mà cả hai tập hiếm khi sắc như vậy (tr. 32):

> [!quote]
> *"Rủi ro cao chỉ tương ứng lợi tức **kỳ vọng** cao (High risk high EXPECTED return). Hãy chú ý chữ
> KỲ VỌNG. Không có chuyện rủi ro cao tương ứng với lợi nhuận lớn."*

Câu này đáng in đậm vì nó phá tan lời quảng cáo phổ biến nhất: *"rủi ro cao, lợi nhuận cao"*. Không.
Rủi ro cao chỉ **có thể** cho lợi nhuận cao — và cũng chính nó cho khả năng mất trắng. Đây là bản
bác bỏ trực tiếp câu *"một vốn bốn mươi lời"* của [bài 11](bai_11_nhan_dien_lua_dao.md#7-bổ-sung-đòn-bẩy-giết-bằng-cách-nào)
(C2 tr. 54: *"bốn mươi lời cũng có nếu bạn chấp nhận mất trắng… trong 99% trường hợp"*). Sách gọi
CFD và coin là *"những kênh rủi ro nhất"* (tr. 32) đúng theo nghĩa này: kỳ vọng có thể cao, nhưng
phương sai lớn tới mức phần lớn người chơi về không.

### Biến động và DCA

Sách nêu **biến động thị trường** (*market volatility*, tr. 32) — giá lên xuống — và một cách giảm
tác động của nó: **nắm giữ đủ lâu** để bình quân hoá, cùng phương pháp **DCA** (*Dollar Cost
Averaging* — bình quân giá, tr. 32–33): chia tiền mua **làm nhiều lần** thay vì một cục.

Sách mô tả đúng nhưng không cho thấy DCA "làm mịn" bằng cách nào. Một ví dụ nhỏ: góp cố định **2tr
mỗi tháng** vào một tài sản có giá dao động:

| Tháng | Giá (nghìn/đơn vị) | 2tr mua được |
| ---: | ---: | ---: |
| 1 | 20 | 100 đơn vị |
| 2 | 10 | 200 đơn vị |
| 3 | 20 | 100 đơn vị |
| **Tổng** | | **400 đơn vị, chi 6tr** |

Giá vốn bình quân = 6.000 / 400 = **15 nghìn/đơn vị**, trong khi trung bình cộng của giá là
(20+10+20)/3 = **16,67 nghìn**. Góp đều tự động **mua nhiều hơn lúc rẻ, ít hơn lúc đắt**, nên giá vốn
luôn thấp hơn trung bình giá. Đó là toàn bộ "phép màu" của DCA — không phải đoán đáy, chỉ là để cơ
chế tự làm việc. Nó cũng chính là *"sửa hệ thống, không sửa người"* của
[bài 10 mục 8](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại):
lệnh mua tự động mỗi tháng gỡ luôn cám dỗ canh thời điểm.

### Các lớp tài sản

Cuối cùng, **các lớp tài sản** (*asset classes*, tr. 33): *"tiền, trái phiếu, cổ phiếu, vàng, BĐS,
tài sản số"*, mỗi lớp biến động theo chu kỳ riêng — *"mùa nào thức nấy"*. Chính sáu lớp này là bốn
dòng trong danh mục *Cân bằng* ở mục 4, và là nội dung **bài 13** mổ xẻ từng
kênh: vàng, trái phiếu, chứng chỉ quỹ, ETF.

---

## 8. Ráp lại và cầu sang bài 13

Cả Unit 4 khép thành một chuỗi ba bước dùng được ngay:

```
   1. Đo khẩu vị      -> bảng Missouri, 13 câu, 6 tháng/lần   (thay cho Topi)
   2. Chọn danh mục   -> theo hồ sơ; đa dạng hoá để xoá rủi ro phi hệ thống
   3. Tính đích        -> chi tiêu / (lợi suất thực), với lợi suất KHỚP danh mục
```

Và hai điều bài này thêm vào so với sách:

- **Đừng lẫn "khoản đó nguy tới đâu" với "bạn chịu được bao nhiêu"** (mục 2). Chọn kênh cần cả hai.
- **Kỳ vọng phải khớp danh mục** (mục 5, 6). Con số 12% cho một danh mục 40% tiền gửi là quá cao, và
  nó bóp méo cả kế hoạch tự do tài chính. Sách tự dạy *"chú ý chữ KỲ VỌNG"* — bài này áp đúng lời đó
  vào chính con số của sách.

Bài tiếp — **bài 13** — đi vào từng lớp tài sản (vàng, trái phiếu, chứng chỉ
quỹ, ETF) để mỗi dòng trong danh mục mẫu ở mục 4 có nội dung thật, thay vì chỉ một tỷ trọng.

---

## 9. Tự thử

Sửa [`thuc_hanh/bai-12-rui-ro-khau-vi.py`](../thuc_hanh/bai-12-rui-ro-khau-vi.py) rồi chạy lại.

1. **Làm bảng Missouri thật.** Vào `pfp.missouri.edu`, làm 13 câu, ghi lại điểm và hồ sơ của bạn.
   Nó rơi vào cái nào trong sáu hồ sơ ở mục 4? Ba tháng sau làm lại — có đổi không?

2. **Kỳ vọng thật của danh mục bạn.** Sửa `DANH_MUC` thành tỷ trọng của chính bạn (hoặc của một hồ
   sơ khác *Cân bằng*), đặt lợi suất thành phần bạn thấy hợp lý. Kỳ vọng cả danh mục ra bao nhiêu?
   Có gần con số app/sách đưa không?

3. **Cái giá của an toàn.** In bảng "số tiền tự do tài chính" cho lợi suất kỳ vọng từ 5% tới 12%,
   bước 1 điểm, với chi tiêu của bạn. Từ mức nào trở xuống thì con số bắt đầu phình chóng mặt? Ở mức
   nào thì thành bất khả?

4. **DCA có luôn thắng không?** Đổi dãy giá ở ví dụ mục 7 thành một dãy **chỉ tăng đều** (10, 20, 30).
   Giá vốn DCA so với trung bình giá lúc này thế nào? DCA "làm mịn" biến động, nhưng nó có giúp gì khi
   thị trường chỉ đi một chiều không?

5. **Hai phép đo, một quyết định.** Lấy một khoản đầu tư thật (một mã cổ phiếu, một loại coin). Chấm
   nó trên ma trận 5×5 (khả năng × hậu quả). Rồi đặt cạnh hồ sơ Missouri của bạn ở câu 1. Điểm khoản
   đó và khẩu vị của bạn có khớp không? Nếu lệch, bạn nên làm gì?

---

## 10. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Khẩu vị rủi ro | Risk appetite | Mức rủi ro **bạn sẵn sàng chấp nhận** để theo đuổi mục tiêu — C1 tr. 25 |
| Hồ sơ rủi ro | Risk profile | Kết quả xếp loại khẩu vị của bạn; sách chia 6 mức — C1 tr. 29 |
| Ma trận rủi ro | Risk matrix | Chấm *khả năng × hậu quả* để đo **một khoản** nguy tới đâu (khác khẩu vị) — C1 tr. 25 |
| Rủi ro hệ thống | Systematic risk | Ảnh hưởng cả thị trường; đa dạng hoá **không** tránh được — C1 tr. 32 |
| Rủi ro phi hệ thống | Unsystematic risk | Của một khoản riêng lẻ; đa dạng hoá **loãng** được — C1 tr. 32 |
| Lợi tức kỳ vọng | Expected return | Kỳ vọng, không phải chắc chắn; *"high risk high EXPECTED return"* — C1 tr. 32 |
| Biến động thị trường | Market volatility | Mức giá lên xuống của một khoản đầu tư — C1 tr. 32 |
| Bình quân giá | Dollar Cost Averaging (DCA) | Chia tiền mua nhiều lần; giá vốn thấp hơn trung bình giá — C1 tr. 32–33 |
| Phân bổ tài sản | Asset allocation | Chia tiền theo mục tiêu, thời gian, khẩu vị; bản chất là đa dạng hoá — C1 tr. 33 |
| Lớp tài sản | Asset class | Nhóm tài sản có chu kỳ rủi ro riêng: tiền, trái phiếu, cổ phiếu, vàng, BĐS, tài sản số — C1 tr. 33 |
| Đa dạng hoá | Diversification | Không bỏ hết trứng một giỏ; công cụ chính chống rủi ro phi hệ thống |

---

## 11. Câu hỏi tự kiểm tra

1. Một hồ sơ rủi ro trả lời ba câu hỏi nào, theo thứ tự nào? Vì sao khẩu vị đứng trước chọn kênh?
2. Khẩu vị rủi ro là gì? Vì sao *"không có lời khuyên nào đúng cho tất cả"*?
3. Ma trận 5×5 và bộ câu hỏi khẩu vị đo hai đại lượng khác nhau thế nào? Chọn kênh cần cái nào?
4. Sách đưa bốn cách đo khẩu vị. Khoá học dùng cách nào và bỏ cách nào? Vì sao?
5. Kể sáu hồ sơ rủi ro theo thứ tự rủi ro tăng dần.
6. Danh mục *Cân bằng* của sách gồm những gì, tỷ trọng bao nhiêu? App ghi lợi nhuận kỳ vọng bao nhiêu?
7. Vì sao con số 12% cho danh mục *Cân bằng* là quá cao? Kỳ vọng thật ước chừng bao nhiêu?
8. Viết công thức số tiền cần cho tự do tài chính. Mẫu số là gì?
9. Cùng chi 120tr/năm, lạm phát 4%: lợi suất 12% cần bao nhiêu tiền? 6% cần bao nhiêu? 4% thì sao?
10. "Cái giá của an toàn" nghĩa là gì trong công thức này?
11. Phân biệt rủi ro hệ thống và phi hệ thống. Đa dạng hoá đỡ được loại nào?
12. Giải thích câu *"high risk high EXPECTED return"*. Vì sao chữ *kỳ vọng* quan trọng?
13. DCA là gì? Vì sao giá vốn DCA thấp hơn trung bình cộng của giá? Cho ví dụ.
14. Sáu lớp tài sản sách nêu là gì? *"Mùa nào thức nấy"* nghĩa là gì?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 12 — RỦI RO, KHẨU VỊ RỦI RO, PHÂN BỔ TÀI SẢN     C1 tr. 25-33       ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  HỒ SƠ RỦI RO = 3 CÂU nối tiếp:                                         ║
║     1) BẠN chịu bao nhiêu?  2) chia tiền vào đâu?  3) đủ là bao nhiêu?  ║
║     KHẨU VỊ ĐỨNG TRƯỚC chọn kênh (tr.32) -> nên bài 12 trước bài 13     ║
║                                                                          ║
║  KHẨU VỊ RỦI RO  mức rủi ro BẠN sẵn sàng chấp nhận (tr.25)              ║
║     "không có lời khuyên đúng cho tất cả" — mỗi người một khác          ║
║     tác giả (C2 tr.54): "tôi là rùa", 20-25%/năm; người khác 10%/tháng ║
║     [bổ sung] sách để LẪN 2 phép đo:                                    ║
║        ma trận 5×5 = KHOẢN ĐÓ nguy tới đâu · câu hỏi = BẠN chịu bao nhiêu║
║                                                                          ║
║  4 CÁCH ĐO -> [đã cắt] Cách 4 (Topi "tối ưu") là quảng cáo             ║
║     khoá dùng Cách 2: BẢNG MISSOURI (sách gọi "uy tín"), 13 câu, free  ║
║        pfp.missouri.edu · làm lại 6 tháng/lần                          ║
║     lý do cắt: tuổi thọ — app đổi/ngừng thì bài vẫn dùng được          ║
║                                                                          ║
║  6 HỒ SƠ: Rất an toàn -> ... -> Tăng trưởng mạnh                        ║
║     danh mục "Cân bằng" (tr.30): tiết kiệm 40% · trái phiếu 25% ·      ║
║        vàng 5% · cổ phiếu 30% · app ghi kỳ vọng 12%                    ║
║     [bổ sung] 12% QUÁ CAO: 40% tiền gửi -> kỳ vọng thật ~7,6%          ║
║        (giả định thành phần: TK 5, TP 7, vàng 5, CP 12)               ║
║                                                                          ║
║  CÔNG THỨC TỰ DO TÀI CHÍNH (tr.31):                                     ║
║     = chi tiêu / (lợi suất HSRR − lạm phát)                            ║
║     120 / (12%−4%) = 1,5 tỷ   [nhưng dùng 7,6% thật -> 3,33 tỷ]        ║
║     [bổ sung] CÁI GIÁ CỦA AN TOÀN — mẫu số là lợi suất THỰC:           ║
║        12%->1,5 tỷ · 8%->3 tỷ · 6%->6 tỷ · 5%->12 tỷ · 4%->BẤT KHẢ    ║
║                                                                          ║
║  TẠI SAO PHÂN BỔ = ĐA DẠNG HOÁ (tr.33)                                  ║
║     rủi ro HỆ THỐNG (cả thị trường, không tránh) vs                    ║
║     PHI HỆ THỐNG (khoản riêng lẻ, đa dạng hoá LOÃNG được)             ║
║     >>> CÂU HAY NHẤT: "high risk high EXPECTED return" (tr.32)         ║
║         chú ý chữ KỲ VỌNG — bác thẳng "một vốn bốn mươi lời" (bài 11)  ║
║     DCA: góp đều -> mua nhiều lúc rẻ; giá vốn 15 < TB giá 16,67        ║
║     lớp tài sản: tiền/trái phiếu/cổ phiếu/vàng/BĐS/số — "mùa nào thức nấy"║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 1: Lập kế hoạch tài chính cá nhân***, Waka.vn. **Unit 4 — *Hồ sơ
  rủi ro*, Lesson 1–3 (tr. 25–33):** định nghĩa khẩu vị rủi ro và ma trận 5×5 (tr. 25); bốn cách xác
  định khẩu vị với nhãn *"uy tín"* / *"tối ưu"* (tr. 26–29); sáu hồ sơ HSRR và danh mục *Cân bằng*
  40/25/5/30 kỳ vọng 12% (tr. 29–30); ba ý tổng kết và công thức tự do tài chính (tr. 31); rủi ro hệ
  thống / phi hệ thống, *"high risk high EXPECTED return"*, biến động, DCA, các lớp tài sản (tr. 31–33)
  — đều chép từ đây.
- ***Tài chính cá nhân 101 — Class 2***, **bài blog tr. 54** (*"Hai. Khẩu vị rủi ro"*): khẩu vị của
  tác giả *"20~25%/năm"*, *"từ 5%/tháng trở lên được coi là rủi ro"*, *"một vốn bốn mươi lời… mất
  trắng… trong 99% trường hợp"*, ẩn dụ *"tôi là rùa"* — dùng làm minh hoạ ở mục 2 và 7.
- **[đã cắt] Topi → Missouri.** Khoá học thay Lesson 2 (hướng dẫn app Topi, tr. 28–31) bằng **Bảng
  câu hỏi Đại học Missouri** — *Investment Risk Tolerance Assessment*, dựng trên thang **Grable &
  Lytton (1999)**, 13 câu, miễn phí:
  [pfp.missouri.edu/research/investment-risk-tolerance-assessment](https://pfp.missouri.edu/research/investment-risk-tolerance-assessment/).
  Chính sách đã dẫn công cụ này ở tr. 26 là *"cách 2… (uy tín)"*. Bài này **không đọc bản gốc Grable
  & Lytton** — nêu tên thang để cho biết bảng câu hỏi có nguồn học thuật, không phải để trích.
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-12-rui-ro-khau-vi.py`](../thuc_hanh/bai-12-rui-ro-khau-vi.py).
  Ba bảng số do tệp này tính, chạy hai lần ra giống hệt nhau. Công thức một dòng để tự kiểm: kỳ vọng
  danh mục `= Σ (tỷ trọng × lợi suất thành phần)`; số tiền tự do tài chính `= chi tiêu / (lợi suất −
  lạm phát)`; giá vốn DCA `= tổng tiền / tổng đơn vị`.
- **Con số giả định, không phải của sách:** lợi suất thành phần từng lớp ở mục 5 (tiết kiệm 5%, trái
  phiếu 7%, vàng 5%, cổ phiếu 12%); các mức lợi suất kỳ vọng ngoài 12% ở bảng mục 6; dãy giá và mức
  góp 2tr ở ví dụ DCA. Lạm phát 4%/năm theo giả định C1 tr. 31 đã dùng từ bài 1.
- **Liên hệ chéo:**
  - Công thức tự do tài chính lần đầu:
    [bài 1 mục 5](bai_01_tai_chinh_ca_nhan_la_gi.md#5-bổ-sung-bao-lâu-thì-đến--tính-bằng-chính-công-thức-của-sách).
  - Tháp tài sản (lớp an toàn / tăng trưởng / mạo hiểm) — phân bổ nhìn từ góc khác:
    [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md).
  - Tiền gửi ở mức lạm phát = không sinh lời thực (vì sao 40% tiết kiệm kéo kỳ vọng xuống):
    [bài 9 mục 5](bai_09_bao_ve.md#5-bổ-sung-lạm-phát-nối-thẳng-với-bài-8-lãi-suất-thật).
  - *"Một vốn bốn mươi lời"*, CFD/coin là kênh rủi ro nhất:
    [bài 11 mục 7](bai_11_nhan_dien_lua_dao.md#7-bổ-sung-đòn-bẩy-giết-bằng-cách-nào).
  - Tự động hoá thắng ý chí (nền của DCA):
    [bài 10 mục 8](bai_10_tai_chinh_hanh_vi.md#8-bổ-sung-vì-sao-biết-mà-vẫn-sai--và-cách-duy-nhất-chống-lại).
  - Từng lớp tài sản (vàng, trái phiếu, chứng chỉ quỹ, ETF): **bài 13**.

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
| 7 | [Phân bổ thu nhập: 6 jars, 50/30/20, 70/30, tỷ lệ tiết kiệm](bai_07_phan_bo_thu_nhap.md) | C2 tr. 18–28 | 1 |
| 8 | [Vay, lãi suất thật, trả nợ](bai_08_vay_va_tra_no.md) | C2 tr. 29–38 | 1 |
| 9 | [Bảo vệ: lạm phát, quỹ khẩn cấp, bảo hiểm](bai_09_bao_ve.md) | C2 tr. 39–47 | 1 |
| 10 | [**[bổ sung]** Tài chính hành vi — vì sao biết mà vẫn sai](bai_10_tai_chinh_hanh_vi.md) | ngoài sách | 2 |
| 11 | [Nhận diện lừa đảo: Ponzi và CFD](bai_11_nhan_dien_lua_dao.md) | C2 tr. 47–57 | 1 |
| **12** | **Rủi ro, khẩu vị rủi ro, phân bổ tài sản** ← *bạn đang ở đây* | C1 tr. 25–33 | 1 |
| 13 | Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
