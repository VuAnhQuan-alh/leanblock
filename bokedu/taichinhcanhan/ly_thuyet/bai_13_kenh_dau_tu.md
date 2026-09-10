# Bài 13 — Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF

> Bài học dựa trên **C2 tr. 58–67** — Unit 5 (*Đầu tư*) Lesson 1–4 của *Tài chính cá nhân 101,
> Class 2*.
>
> **Cần đọc trước:** [Bài 12](bai_12_rui_ro_khau_vi_phan_bo.md) — khẩu vị rủi ro đứng trước chọn kênh;
> bài này lấp nội dung cho bốn dòng trong danh mục *Cân bằng* ở đó. Và
> [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md) — tháp tài sản chia lớp an toàn / tăng trưởng /
> mạo hiểm là chính các kênh này xếp theo rủi ro.
>
> **Đây là bài vòng 2** — đọc hiểu, nắm ý là đủ. Sách viết phần đầu tư **mỏng và có chỗ sai**
> ([bài 0](bai_00_bat_dau_tu_dau.md) đã báo trước); bài này giữ nguyên độ mỏng đó, chỉ bắt lỗi và bổ
> khung, **không** phình thành một khoá đầu tư nửa vời.
>
> **[đã cắt]:** phần *"hình thức mua vàng Doji online"* (tr. 61) đặt sản phẩm thương mại vào vị trí
> phương pháp. Khoá học nêu **hình thức** giao dịch, không nêu nhà cung cấp — [mục 3](#3-vàng--và-đính-chính-sách-tự-mâu-thuẫn-về-vàng).
>
> **Ký hiệu:** **[bổ sung]** ngoài sách · **[đính chính]** chỗ sách sai · **[đã cắt]** phần thương
> mại thay bằng cách khác · **[2026]** đối chiếu hiện tại.
>
> **Về [2026]:** mục 5 dẫn văn bản và số liệu khủng hoảng trái phiếu, tra ngày **10/09/2026**.
>
> **Code:** [`thuc_hanh/bai-13-kenh-dau-tu.py`](../thuc_hanh/bai-13-kenh-dau-tu.py)
> — kiểm hai con số sách để trống: *"2tr/tháng vào VN30 → hàng tỷ"* thật ra ra bao nhiêu, và giá trái
> phiếu **hội tụ về mệnh giá** khi tới hạn (ngược với sách). Công thức một dòng kèm theo.

---

## Mục lục

<!-- MUC-LUC -->
- [1. Bốn kênh, một nguyên tắc: khớp kênh với khẩu vị](#1-bốn-kênh-một-nguyên-tắc-khớp-kênh-với-khẩu-vị)
- [2. Trước khi đầu tư cần bao nhiêu, và [bổ sung] con số "hàng tỷ" đáng ngờ](#2-trước-khi-đầu-tư-cần-bao-nhiêu-và-bổ-sung-con-số-hàng-tỷ-đáng-ngờ)
- [3. Vàng — và [đính chính] sách tự mâu thuẫn về vàng](#3-vàng--và-đính-chính-sách-tự-mâu-thuẫn-về-vàng)
- [4. Trái phiếu — và [đính chính] "gần đáo hạn giá càng giảm" là ngược](#4-trái-phiếu--và-đính-chính-gần-đáo-hạn-giá-càng-giảm-là-ngược)
- [5. [2026] Khủng hoảng trái phiếu doanh nghiệp 2022](#5-2026-khủng-hoảng-trái-phiếu-doanh-nghiệp-2022)
- [6. Chứng chỉ quỹ và ETF — và [đính chính] "niêm yết hay không"](#6-chứng-chỉ-quỹ-và-etf--và-đính-chính-niêm-yết-hay-không)
- [7. Ráp bốn kênh vào danh mục Cân bằng, và cầu sang bài 14](#7-ráp-bốn-kênh-vào-danh-mục-cân-bằng-và-cầu-sang-bài-14)
- [8. Tự thử](#8-tự-thử)
- [9. Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
- [10. Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)
<!-- /MUC-LUC -->

---

## 1. Bốn kênh, một nguyên tắc: khớp kênh với khẩu vị

[Bài 12](bai_12_rui_ro_khau_vi_phan_bo.md) đã chốt nguyên tắc: **đo khẩu vị trước, chọn kênh sau.**
Bài này là bước "chọn kênh" — nhưng đừng đọc nó như một danh sách mã để mua. Đọc nó như phần **lấp
nội dung** cho danh mục mẫu *Cân bằng* mà bài 12 chỉ mới đưa tỷ trọng:

| Dòng trong danh mục *Cân bằng* (bài 12) | Tỷ trọng | Bài này nói ở |
| --- | ---: | --- |
| Tiền gửi tiết kiệm | 40% | (đã học ở [bài 9](bai_09_bao_ve.md)) |
| Trái phiếu | 25% | [mục 4](#4-trái-phiếu--và-đính-chính-gần-đáo-hạn-giá-càng-giảm-là-ngược) |
| Vàng | 5% | [mục 3](#3-vàng--và-đính-chính-sách-tự-mâu-thuẫn-về-vàng) |
| Cổ phiếu (trực tiếp hoặc qua quỹ/ETF) | 30% | [mục 2](#2-trước-khi-đầu-tư-cần-bao-nhiêu-và-bổ-sung-con-số-hàng-tỷ-đáng-ngờ), [mục 6](#6-chứng-chỉ-quỹ-và-etf--và-đính-chính-niêm-yết-hay-không) |

Mỗi lớp có một chu kỳ rủi ro riêng — *"mùa nào thức nấy"* ([bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#7-tại-sao-phân-bổ-tài-sản--rủi-ro-biến-động-dca-và-câu-hay-nhất)) — nên phân bổ nhiều lớp mới cho lợi
nhuận đều. Bài này đi qua từng lớp, chỉ ra chỗ sách nói đúng, chỗ sách tự cãi mình, và một chỗ sách
viết ngược hẳn.

---

## 2. Trước khi đầu tư cần bao nhiêu, và [bổ sung] con số "hàng tỷ" đáng ngờ

Lesson 1 mở bằng một điểm rất đúng (tr. 58): *"Miễn là bạn có tiền, dù nhiều hay ít, việc đầu tư luôn
có hành trình phù hợp dành cho bạn."* Sách nối thẳng về **tỷ lệ tiết kiệm** đã học ở
[bài 7](bai_07_phan_bo_thu_nhap.md) (*"Tỷ lệ tiết kiệm = Tiết kiệm / Thu nhập ròng"*), và khuyên có
thể **bắt đầu từ 500 nghìn – 1 triệu/tháng**, miễn là **đều và dài hạn**. Đúng và dùng được.

Sách cũng phân tầng kênh theo dòng tiền tháng (tr. 59):

| Dòng tiền/tháng | Sách gợi ý |
| --- | --- |
| dưới 10tr | cổ phiếu tăng trưởng niêm yết chính thống, vàng, tiền điện tử **hàng đầu vốn hoá** (*"tuyệt đối tránh coin rác"*) |
| 10 – dưới 50tr | gửi tiết kiệm, trái phiếu, góp vốn mua nhà cho thuê |
| trên 50tr | bất động sản đất nền |

Câu *"tuyệt đối tránh coin rác"* khớp thẳng với [bài 11](bai_11_nhan_dien_lua_dao.md) — coin rác là
nơi Ponzi và bơm–xả trú ngụ.

### [bổ sung] Con số "hàng tỷ" gánh survivorship

Ngay tr. 58 sách đưa một con số hấp dẫn:

> *"nếu đầu tư định kỳ 2 triệu đồng/tháng vào **chỉ một vài doanh nghiệp lớn thuộc nhóm VN30** trong
> 10 năm liên tiếp, bạn đã có số tiền **hàng tỷ đồng** ở hiện tại."*

Tính lại thì con số này quá lạc quan. Góp 2tr/tháng trong 10 năm là bỏ vào **240 triệu**. Để ra
"hàng tỷ", suất sinh lời phải rất cao:

| Lợi suất giả định | 2tr/tháng × 10 năm thành |
| ---: | ---: |
| 8%/năm | 0,36 tỷ |
| 12%/năm | 0,44 tỷ |
| 20%/năm | 0,68 tỷ |
| 27%/năm | ~1,0 tỷ |
| 35%/năm | ~1,5 tỷ |

Ngay ở mức 12%/năm — mức chính sách dùng cho cả danh mục ở [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#5-bổ-sung-con-số-12-gánh-quá-nặng) —
kết quả chỉ **0,44 tỷ**, không phải "hàng tỷ". Muốn ra 1,5 tỷ phải giữ **35%/năm suốt mười năm**.

Chữ khoá là *"chỉ một vài doanh nghiệp lớn"*: nhìn lại quá khứ thì luôn có vài mã VN30 tăng gấp
mười, nhưng đó là **chọn người thắng sau khi trận đấu đã xong** — đúng **thiên kiến sống sót** của
[bài 10 mục 3](bai_10_tai_chinh_hanh_vi.md#3-thiên-kiến-sống-sót--cái-tên-duy-nhất-sách-gọi-đúng-ở-trang-10).
Ai đứng ở thời điểm mua thì không biết mã nào sẽ là mã thắng. Đây cũng là lý do các mục sau nghiêng
về **quỹ và ETF** (mua cả rổ) hơn là đặt cược vào *"một vài doanh nghiệp"*.

---

## 3. Vàng — và [đính chính] sách tự mâu thuẫn về vàng

Sách nói về vàng ở hai chỗ, và hai chỗ đá nhau.

**Chỗ tỉnh táo (tr. 59–60):**

> *"Tăng trưởng giá vàng trong dài hạn khoảng **1,8%/năm** trong 100 năm qua (tính theo USD)."*
>
> *"chỉ nên đầu tư 1 phần tiền vào vàng như một khoản phòng ngừa rủi ro, còn xét về lợi suất đầu tư
> thì **không đặt niềm tin vào vàng như 1 khoản đầu tư có lợi suất cao**."*

Đây là lời khuyên tốt: vàng là **bảo hiểm**, không phải máy sinh lời. Đúng vai của 5% vàng trong danh
mục *Cân bằng*.

**Chỗ tự cãi lại (tr. 61), trong phần ưu điểm của Lesson 2:**

> *"Giá trị lưu trữ trường tồn theo thời gian: vàng nắm giữ **càng lâu càng có giá**, vì theo thời
> gian giá vàng sẽ ngày càng tăng."*

Hai câu không thể cùng đúng. Nếu vàng chỉ tăng ~1,8%/năm (tr. 59) thì nó **không** *"càng lâu càng có
giá"* theo nghĩa sinh lời — 1,8% là mức rất thấp, thua xa gửi tiết kiệm.

### [đính chính] Và 1,8% ấy nhiều khả năng là lợi suất **thực**

Con số *"khoảng 1,8%/năm trong 100 năm"* gần với **lợi suất thực** (đã trừ lạm phát) mà các nghiên
cứu dài hạn về vàng đưa ra, **không phải** lợi suất danh nghĩa. Sách không nói rõ là loại nào — mà
đây là khác biệt lớn: 1,8% **thực** nghĩa là vàng gần như chỉ **giữ được sức mua** qua rất dài hạn,
đúng vai bảo hiểm. Chốt lại cho gọn:

> **Vàng để giữ sức mua khi bất ổn, không để sinh lời.** Nó *"không mang lại thu nhập thụ động"*
> (chính sách thừa nhận, tr. 61) — không cho thuê, không trả lãi, không cổ tức. Giữ một phần nhỏ là
> đủ.

### [đã cắt] Mua vàng thế nào

Sách dành gần một trang (tr. 61) hướng dẫn mua vàng qua **DOJI eGold**, cần tài khoản **TPBank** hoặc
mua qua **Topi**. Khoá học cắt phần gắn nhà cung cấp cụ thể, chỉ nêu **hình thức**: có thể mua vàng
vật chất (giữ hộ hoặc tự cất), hoặc vàng "số" liên kết vàng vật chất qua một tổ chức được cấp phép.
Nguyên tắc chọn nơi mua: **được cấp phép, tách bạch tài sản khách, cho rút vàng vật chất** — không
phụ thuộc một thương hiệu nào, vì thương hiệu đổi chính sách thì bài học vẫn phải dùng được.

---

## 4. Trái phiếu — và [đính chính] "gần đáo hạn giá càng giảm" là ngược

Lesson 3 định nghĩa đúng (tr. 63): trái phiếu là cho tổ chức phát hành **vay**, phát hành bởi *"chính
phủ, chính quyền và doanh nghiệp"*. Và sách xếp hạng rủi ro đúng:

> *"trái phiếu kho bạc là giải pháp khá an toàn khi khủng hoảng kinh tế xảy ra. **Rủi ro nhất vẫn là
> trái phiếu doanh nghiệp**."*

Ghi nhớ câu sau — nó chính là cửa vào [mục 5](#5-2026-khủng-hoảng-trái-phiếu-doanh-nghiệp-2022).

### [đính chính] 1 — "Rủi ro thấp" mà "lãi cao hơn tiết kiệm" thì mâu thuẫn

Phần ưu điểm (tr. 62) liệt kê cùng lúc *"Rủi ro thấp"* và *"Lãi suất lớn hơn việc gửi tiết kiệm ngân
hàng"*. Nếu vừa an toàn hơn vừa lãi cao hơn gửi tiết kiệm thì không ai gửi tiết kiệm nữa. Sự thật là
**lãi cao hơn chính là phần bù cho rủi ro cao hơn** — đúng *"high risk high EXPECTED return"* của
[bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#7-tại-sao-phân-bổ-tài-sản--rủi-ro-biến-động-dca-và-câu-hay-nhất).
Và chính sách thừa nhận điều đó ngay ở phần nhược điểm: *"Nếu tổ chức phát hành không có khả năng
thanh toán, trái chủ sẽ bị mất cả vốn lẫn lãi."* — tức **không** hề "rủi ro thấp" một cách vô điều
kiện. "Rủi ro thấp" chỉ đúng với trái phiếu **kho bạc/chính phủ**, không đúng với trái phiếu doanh
nghiệp.

### [đính chính] 2 — Giá trái phiếu **hội tụ về mệnh giá**, không "càng giảm"

Sách liệt kê một nhược điểm sai (tr. 63):

> *"Càng gần ngày đáo hạn thì giá trị của trái phiếu càng giảm."*

Ngược. Đến ngày đáo hạn, trái chủ nhận lại đúng **mệnh giá**, nên giá thị trường của trái phiếu
**hội tụ về mệnh giá** khi tới hạn — gọi là *pull to par*. Trái phiếu đang giao dịch **dưới** mệnh
giá thì giá **tăng** dần lên về mệnh giá. Ví dụ một trái phiếu chiết khấu, mệnh giá 100tr, lợi suất
8%/năm:

| Còn bao lâu tới hạn | Giá thị trường |
| ---: | ---: |
| 3 năm | 79,38tr |
| 2 năm | 85,73tr |
| 1 năm | 92,59tr |
| **đáo hạn** | **100,00tr** |

Giá **tăng** khi lại gần đáo hạn, không giảm. (Trái phiếu đang giao dịch **trên** mệnh giá thì giá
giảm dần về mệnh giá — nên chiều đi phụ thuộc mua trên hay dưới mệnh giá, chứ không phải "luôn giảm".)
Điều thật sự làm giá trái phiếu **giảm giữa chừng** là **lãi suất thị trường tăng**, không phải việc
đến gần đáo hạn — và đó là một cơ chế khác hẳn.

---

## 5. [2026] Khủng hoảng trái phiếu doanh nghiệp 2022

Sách được viết trước một biến động lớn của thị trường trái phiếu doanh nghiệp Việt Nam, nên gọi trái
phiếu là *"rủi ro thấp"* mà không nhắc sự kiện nào. Với người đọc 2026, đây là bối cảnh không thể bỏ
qua — và nó cho thấy vì sao câu *"rủi ro nhất vẫn là trái phiếu doanh nghiệp"* (tr. 63) mới là câu
đúng.

**Bùng nổ rồi vỡ.** Giai đoạn 2018–2021 trái phiếu doanh nghiệp phát hành **riêng lẻ** tăng rất nóng
(riêng 2021 hơn **742.000 tỷ đồng**), phần lớn là doanh nghiệp bất động sản, dưới khung
**Nghị định 153/2020** rất lỏng — không bắt buộc xếp hạng tín nhiệm, không bắt công khai đầy đủ.

**Cú sốc niềm tin.** Năm 2022 các sai phạm lớn bị phanh phui: **Tân Hoàng Minh** (4/2022, Uỷ ban
Chứng khoán huỷ 9 đợt phát hành ~**10.030 tỷ đồng**), rồi **Vạn Thịnh Phát**. Lãnh đạo bị bắt vì gian
lận phát hành. Quý 4/2022 phát hành mới **giảm ~98,8%** so với cùng kỳ — thị trường gần như đóng
băng, người muốn bán cũng không có người mua.

**Hai nghị định phải nhớ:**

| Văn bản | Ngày | Làm gì |
| --- | --- | --- |
| **Nghị định 65/2022/NĐ-CP** | cuối 9/2022 | **siết**: nâng chuẩn *nhà đầu tư chứng khoán chuyên nghiệp*, buộc minh bạch mục đích dùng vốn, hồ sơ, điều kiện chào bán |
| **Nghị định 08/2023/NĐ-CP** | 5/3/2023 | **tháo gỡ**: lùi 1 năm quy định NĐT chuyên nghiệp và xếp hạng tín nhiệm bắt buộc; cho **gia hạn kỳ hạn** và thoả thuận điều chỉnh điều khoản trái phiếu |

**Con số nói nhiều nhất:** theo FiinGroup, tính đến 30/6/2023 có tới **38,5% trái phiếu bất động sản
trong tình trạng chậm trả nợ**. Đó là "rủi ro thấp" theo cách sách gọi.

Ba điều rút ra cho người học:

- **"Trái phiếu" không phải một loại.** Trái phiếu **chính phủ/kho bạc** an toàn; trái phiếu **doanh
  nghiệp riêng lẻ** có thể mất cả vốn lẫn lãi — đúng như phần nhược điểm của chính sách.
- **Nhà đầu tư chuyên nghiệp là một hàng rào pháp lý, không phải một danh hiệu.** Từ 2022 việc mua
  trái phiếu riêng lẻ bị siết đúng vì nhà đầu tư cá nhân không đủ thông tin để định giá rủi ro.
- **Trái phiếu 25% trong danh mục *Cân bằng*** (bài 12) nên hiểu là trái phiếu chính phủ hoặc quỹ
  trái phiếu đa dạng, không phải một lô trái phiếu doanh nghiệp riêng lẻ lãi cao.

---

## 6. Chứng chỉ quỹ và ETF — và [đính chính] "niêm yết hay không"

Lesson 4 là phần hay và thực dụng nhất của Unit 5: **đầu tư thụ động** qua chứng chỉ quỹ và ETF —
giao tiền cho tổ chức chuyên nghiệp thay vì tự chọn mã.

**Chứng chỉ quỹ** (tr. 65) có hai dạng, và sách phân biệt gần đúng:

| | Quỹ mở | Quỹ đóng |
| --- | --- | --- |
| Phát hành | liên tục | **một lần duy nhất** |
| Rút vốn | quỹ **mua lại** theo yêu cầu (theo NAV) | quỹ **không** mua lại |
| Mua bán lại | qua chính quỹ | trên **sàn chứng khoán** |

Quỹ mở còn ba loại (tr. 66): quỹ mở **cổ phiếu**, **cân bằng** (cả cổ phiếu và trái phiếu), **trái
phiếu**. Chú ý: **quỹ mở cân bằng** gần như đúng bằng cả danh mục *Cân bằng* của
[bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#4-sáu-hồ-sơ-và-danh-mục-mẫu) gói trong **một** sản phẩm.

### [đính chính] "Chứng chỉ quỹ không được niêm yết" — cùng trang tự cãi

tr. 67 viết, cách nhau vài dòng, hai câu ngược nhau:

> *"[Quỹ đóng]… các chứng chỉ quỹ sẽ được **niêm yết** trên thị trường chứng khoán."*
>
> *"Chứng chỉ quỹ **không được niêm yết** trên sàn chứng khoán."*

Rồi ngay dưới, phần ETF lại viết: *"Các quỹ ETF tại Việt Nam được xem như một loại cổ phiếu, được
**niêm yết** và giao dịch trên sàn."* Vậy câu *"không được niêm yết"* bị chính sách phản bác **hai
lần** trong cùng một trang. Bản đúng, gỡ mâu thuẫn:

| Loại | Có niêm yết trên sàn không |
| --- | --- |
| Chứng chỉ **quỹ mở** | **Không** — mua bán qua quỹ theo NAV |
| Chứng chỉ **quỹ đóng** | **Có** — giao dịch trên sàn thứ cấp |
| **ETF** | **Có** — giao dịch trên sàn như cổ phiếu, theo giá thời gian thực |

Câu *"không được niêm yết"* chỉ đúng với **quỹ mở**, nhưng sách viết như một phát biểu chung cho mọi
chứng chỉ quỹ — đó là chỗ sai.

### [bổ sung] "Thụ động" theo nghĩa nào

Sách gộp cả chứng chỉ quỹ lẫn ETF vào *"đầu tư thụ động"*. Cần tách một chữ: **thụ động với bạn**
(bạn giao tiền, không tự chọn mã) **khác** *đầu tư chỉ số thụ động* (bám theo một chỉ số, phí rất
thấp):

- **ETF / quỹ chỉ số**: bám theo một chỉ số (VN30, VN100…), *"sở hữu hàng nghìn cổ phiếu"*, **phí
  thấp**, lợi nhuận *"tương đương với chỉ số… mà nó mô phỏng"* (tr. 67). Đây là đầu tư thụ động thật.
- **Quỹ mở chủ động (cổ phiếu)**: có đội ngũ **chủ động chọn mã** để cố thắng thị trường — bạn thụ
  động, nhưng chiến lược thì chủ động, và **phí quản lý cao hơn**. Phí ăn vào lợi nhuận dài hạn, nên
  đây là con số cần hỏi trước khi mua.

Lời khuyên của sách thì đúng và đáng giữ (tr. 67): mua chứng chỉ quỹ để **đầu tư trung–dài hạn cho
lãi kép**, *"không nên lướt sóng"* vì lướt sóng tốn phí mua đi bán lại. Đó cũng là DCA của
[bài 12](bai_12_rui_ro_khau_vi_phan_bo.md#7-tại-sao-phân-bổ-tài-sản--rủi-ro-biến-động-dca-và-câu-hay-nhất):
với người không chuyên, **mua đều một quỹ chỉ số rồi giữ** là chiến lược khó sai nhất.

---

## 7. Ráp bốn kênh vào danh mục Cân bằng, và cầu sang bài 14

Ghép cả bài lại, danh mục *Cân bằng* của bài 12 giờ có nội dung thật cho từng dòng:

| Lớp | Tỷ trọng | Vai | Cách vào đơn giản nhất cho người không chuyên |
| --- | ---: | --- | --- |
| Tiền gửi tiết kiệm | 40% | an toàn, thanh khoản | gửi ngân hàng; cũng là nơi để quỹ khẩn cấp (bài 9) |
| Trái phiếu | 25% | thu nhập ổn định | **quỹ trái phiếu** hoặc trái phiếu chính phủ, tránh riêng lẻ doanh nghiệp (mục 5) |
| Vàng | 5% | bảo hiểm bất ổn | một phần nhỏ, giữ sức mua, không kỳ vọng lãi cao (mục 3) |
| Cổ phiếu | 30% | tăng trưởng dài hạn | **ETF/quỹ chỉ số** thay vì "một vài mã" (mục 2, 6) |

Nguyên tắc xuyên suốt vẫn là của [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md): **danh mục phải khớp
khẩu vị của bạn**, không phải sao chép bảng này. Người ưa an toàn dịch tỷ trọng về tiết kiệm và trái
phiếu; người chịu được rủi ro và còn dài thời gian thì nâng cổ phiếu — nhưng **kỳ vọng phải khớp
danh mục** (đừng gắn 12% cho một danh mục 40% tiền gửi, như mục 5 bài 12 đã bắt).

Còn một việc cuối để cả khoá thành dùng được: biến "danh mục" và "khẩu vị" thành một **kế hoạch có
mục tiêu, có thời hạn**. Đó là [**bài 14**](bai_14_muc_tieu_smart.md) — mục tiêu SMART và ráp mọi bài
lại thành một bản kế hoạch tự do tài chính.

---

## 8. Tự thử

Bài vòng 2, không bắt buộc code. Nhưng bốn câu này đáng ngồi tính —
[`thuc_hanh/bai-13-kenh-dau-tu.py`](../thuc_hanh/bai-13-kenh-dau-tu.py) kiểm hai câu đầu.

1. **"Hàng tỷ" cần lợi suất bao nhiêu.** Với 2tr/tháng trong 10 năm, tìm mức lợi suất/năm để đạt
   đúng 1 tỷ; rồi 2 tỷ. Con số đó có thực tế không? Nó nói gì về chữ *"một vài doanh nghiệp"*?

2. **Pull to par.** In giá một trái phiếu chiết khấu (mệnh giá 100, lợi suất 8%) khi còn 5, 4, 3, 2,
   1, 0 năm. Giá đi lên hay đi xuống khi tới gần đáo hạn? Sách viết đúng hay ngược?

3. **Vàng giữ sức mua tới đâu.** 1,8%/năm: sau 30 năm, 1 triệu thành bao nhiêu? Nếu 1,8% là lợi suất
   **thực**, thì so với lạm phát 4% nó bảo vệ sức mua ở mức nào?

4. **Danh mục của bạn.** Đặt tỷ trọng bốn lớp theo khẩu vị của bạn (từ bài 12), gán lợi suất thành
   phần hợp lý, tính kỳ vọng cả danh mục. So với một danh mục toàn ETF chỉ số — cái nào hợp bạn hơn,
   và vì sao?

---

## 9. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa |
| --- | --- | --- |
| Vàng (kênh đầu tư) | Gold | Bảo hiểm bất ổn/lạm phát; ~1,8%/năm dài hạn (có lẽ là **thực**), không sinh thu nhập thụ động — C2 tr. 59–61 |
| Trái phiếu | Bond | Cho tổ chức phát hành vay; kho bạc an toàn, doanh nghiệp rủi ro nhất — C2 tr. 63 |
| Mệnh giá | Face value / par | Số tiền trái chủ nhận lại khi đáo hạn; giá thị trường **hội tụ** về đây |
| Pull to par | Pull to par | Giá trái phiếu tiến dần về mệnh giá khi tới hạn (dưới giá thì tăng lên) |
| Chứng chỉ quỹ | Fund certificate | Bằng chứng góp vốn vào quỹ đại chúng; quỹ **mở** và quỹ **đóng** — C2 tr. 65 |
| Quỹ mở | Open-end fund | Phát hành liên tục, quỹ mua lại theo NAV, **không** niêm yết — C2 tr. 66 |
| Quỹ đóng | Closed-end fund | Phát hành một lần, **có** niêm yết trên sàn — C2 tr. 67 |
| ETF | Exchange Traded Fund | Quỹ hoán đổi danh mục, bám chỉ số, niêm yết như cổ phiếu, phí thấp — C2 tr. 67 |
| Đầu tư thụ động (chỉ số) | Passive / index investing | Bám theo chỉ số thay vì chọn mã; phí thấp — khác "quỹ chủ động" |
| Nhà đầu tư chứng khoán chuyên nghiệp | Professional investor | Tư cách pháp lý bị siết từ Nghị định 65/2022 để mua trái phiếu riêng lẻ |

---

## 10. Câu hỏi tự kiểm tra

1. Vì sao bài này nên đọc như "lấp nội dung cho danh mục *Cân bằng*", không phải danh sách mã để mua?
2. Sách phân tầng kênh theo dòng tiền tháng thế nào (dưới 10tr / 10–50tr / trên 50tr)?
3. 2tr/tháng vào VN30 trong 10 năm, ở lợi suất 12%/năm, ra bao nhiêu? Vì sao "hàng tỷ" là lạc quan?
4. *"Một vài doanh nghiệp lớn"* dính thiên kiến nào của bài 10?
5. Nêu hai câu về vàng của sách mâu thuẫn nhau. Câu nào đúng?
6. Con số 1,8%/năm của vàng nhiều khả năng là lợi suất gì? Vai đúng của vàng trong danh mục là gì?
7. Vì sao *"rủi ro thấp"* và *"lãi cao hơn tiết kiệm"* không thể cùng đúng với trái phiếu doanh nghiệp?
8. Sách viết *"càng gần đáo hạn giá trái phiếu càng giảm"*. Đúng hay sai? Giải thích *pull to par*.
9. Cái gì mới thật sự làm giá trái phiếu giảm giữa chừng?
10. Kể diễn biến khủng hoảng trái phiếu 2022. Nghị định 65/2022 và 08/2023 mỗi cái làm gì?
11. Phân biệt niêm yết của quỹ mở, quỹ đóng, ETF. Câu nào của sách sai?
12. *"Thụ động với bạn"* khác *"đầu tư chỉ số thụ động"* ra sao? Cái nào phí thấp hơn?
13. Vì sao với người không chuyên, mua đều một ETF chỉ số rồi giữ là chiến lược khó sai?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 13 — KÊNH ĐẦU TƯ: VÀNG, TRÁI PHIẾU, CHỨNG CHỈ QUỸ, ETF  C2 tr.58-67 ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  NGUYÊN TẮC: đo khẩu vị TRƯỚC (bài 12), chọn kênh SAU                   ║
║     bài này = lấp nội dung 4 dòng danh mục Cân bằng:                    ║
║     tiết kiệm 40% · trái phiếu 25% · vàng 5% · cổ phiếu 30%             ║
║                                                                          ║
║  CHUẨN BỊ VỐN  bắt đầu từ 500k-1tr/tháng, miễn ĐỀU và DÀI HẠN           ║
║     [bổ sung] "2tr/tháng vào VN30 -> HÀNG TỶ" (tr.58) là lạc quan:      ║
║        góp vào 240tr; 12%/năm -> 0,44 tỷ; cần ~35%/năm mới ra 1,5 tỷ    ║
║        "một vài doanh nghiệp" = THIÊN KIẾN SỐNG SÓT (bài 10)            ║
║                                                                          ║
║  VÀNG  [đính chính] sách TỰ MÂU THUẪN:                                  ║
║     tr.59 "1,8%/năm, đừng tin vàng là lợi suất cao" (ĐÚNG) vs           ║
║     tr.61 "càng lâu càng có giá, ngày càng tăng" (SAI)                  ║
║     1,8% có lẽ là lợi suất THỰC -> vàng chỉ GIỮ SỨC MUA, là bảo hiểm    ║
║     [đã cắt] mua qua Doji/eGold/TPBank/Topi -> nêu HÌNH THỨC, không hãng ║
║                                                                          ║
║  TRÁI PHIẾU  kho bạc an toàn · DOANH NGHIỆP rủi ro nhất (tr.63)         ║
║     [đính chính] "rủi ro thấp" + "lãi cao hơn tiết kiệm" = mâu thuẫn    ║
║        lãi cao = phần bù rủi ro (high risk high EXPECTED return)        ║
║     [đính chính] "gần đáo hạn giá càng GIẢM" = NGƯỢC                    ║
║        giá HỘI TỤ về mệnh giá (pull to par): 79->86->93->100tr          ║
║        cái làm giá giảm giữa chừng là LÃI SUẤT thị trường tăng          ║
║                                                                          ║
║  [2026] KHỦNG HOẢNG TPDN 2022 — điều sách không biết                    ║
║     Tân Hoàng Minh (huỷ ~10.030 tỷ), Vạn Thịnh Phát; Q4/22 phát hành   ║
║        giảm ~98,8%; FiinGroup 30/6/23: 38,5% TP bất động sản CHẬM TRẢ  ║
║     NĐ 65/2022 SIẾT (chuẩn NĐT chuyên nghiệp) · NĐ 08/2023 THÁO GỠ     ║
║                                                                          ║
║  CHỨNG CHỈ QUỸ & ETF  đầu tư thụ động, giao cho tổ chức                 ║
║     quỹ mở (mua lại theo NAV, KHÔNG niêm yết) · quỹ đóng (CÓ niêm yết)  ║
║     [đính chính] "chứng chỉ quỹ không niêm yết" bị tự cãi 2 lần/trang   ║
║        đúng: quỹ mở KHÔNG · quỹ đóng CÓ · ETF CÓ                        ║
║     [bổ sung] "thụ động với bạn" ≠ "đầu tư chỉ số": ETF phí THẤP,       ║
║        quỹ chủ động phí CAO -> người không chuyên: mua ETF chỉ số, GIỮ  ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- ***Tài chính cá nhân 101 — Class 2***, Waka.vn. **Unit 5 — *Đầu tư*, Lesson 1–4 (tr. 58–67):**
  chuẩn bị vốn theo tỷ lệ tiết kiệm và phân tầng dòng tiền, câu *"2tr/tháng vào VN30… hàng tỷ"*
  (tr. 58–59); vàng 1,8%/năm và *"không đặt niềm tin vào vàng như khoản lợi suất cao"* (tr. 59–60),
  ưu/nhược điểm vàng và *"càng lâu càng có giá"* (tr. 61), hình thức Doji eGold (tr. 61); trái phiếu
  kho bạc/doanh nghiệp, *"rủi ro thấp"*, *"lãi lớn hơn gửi tiết kiệm"*, *"càng gần đáo hạn giá càng
  giảm"* (tr. 62–64); chứng chỉ quỹ mở/đóng, ba loại quỹ mở, mâu thuẫn *"niêm yết / không niêm yết"*,
  ETF (tr. 65–67) — đều chép từ đây.
- **[2026] Khủng hoảng trái phiếu doanh nghiệp**, tra ngày **10/09/2026**: bùng nổ phát hành riêng lẻ
  2018–2021 dưới Nghị định 153/2020; Tân Hoàng Minh (Uỷ ban Chứng khoán huỷ 9 đợt ~10.030 tỷ, 4/2022),
  Vạn Thịnh Phát; Q4/2022 phát hành giảm ~98,8%; **Nghị định 65/2022/NĐ-CP** (siết chuẩn nhà đầu tư
  chuyên nghiệp), **Nghị định 08/2023/NĐ-CP** ngày 5/3/2023 (lùi thời hạn, cho gia hạn kỳ hạn);
  FiinGroup: 38,5% trái phiếu bất động sản chậm trả tính đến 30/6/2023.
  - [Thị trường trái phiếu doanh nghiệp thực tiễn 2022 và triển vọng 2023 — Tạp chí Ngân hàng](https://tapchinganhang.gov.vn/thi-truong-trai-phieu-doanh-nghiep-thuc-tien-nam-2022-va-trien-vong-nam-2023-10213.html)
  - [Phát triển thị trường trái phiếu doanh nghiệp sau khủng hoảng — Tạp chí Công Thương](https://ojs.tapchicongthuong.vn/vi/ojs-post/phat-trien-thi-truong-trai-phieu-doanh-nghiep-hieu-qua--an-toan--ben-vung-sau-khung-hoang-120987.htm)
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-13-kenh-dau-tu.py`](../thuc_hanh/bai-13-kenh-dau-tu.py).
  Hai bảng số do tệp này tính, chạy hai lần ra giống hệt nhau. Công thức một dòng để tự kiểm: giá trị
  tương lai khoản góp đều `= P × ((1+i)^n − 1) / i`; giá trái phiếu chiết khấu `= mệnh giá / (1+lợi
  suất)^số năm còn lại`.
- **Con số giả định, không phải của sách:** các mức lợi suất trong bảng VN30 ở mục 2; mệnh giá 100tr
  và lợi suất 8% ở ví dụ pull to par; lợi suất thành phần từng lớp ở mục 7. Con số 1,8%/năm và
  742.000 tỷ, 10.030 tỷ, 98,8%, 38,5% là của sách và của các nguồn [2026] đã dẫn.
- **Liên hệ chéo:**
  - Danh mục *Cân bằng*, khẩu vị đứng trước chọn kênh, "mùa nào thức nấy", DCA:
    [bài 12](bai_12_rui_ro_khau_vi_phan_bo.md).
  - Thiên kiến sống sót (*"một vài doanh nghiệp"*):
    [bài 10 mục 3](bai_10_tai_chinh_hanh_vi.md#3-thiên-kiến-sống-sót--cái-tên-duy-nhất-sách-gọi-đúng-ở-trang-10).
  - Coin rác, kênh rủi ro nhất:
    [bài 11](bai_11_nhan_dien_lua_dao.md).
  - Tháp tài sản (lớp an toàn/tăng trưởng/mạo hiểm):
    [bài 4](bai_04_tai_san_tieu_san_thap_tai_san.md).
  - Ráp mọi thứ thành kế hoạch có mục tiêu, thời hạn: **bài 14**.

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
| 12 | [Rủi ro, khẩu vị rủi ro, phân bổ tài sản](bai_12_rui_ro_khau_vi_phan_bo.md) | C1 tr. 25–33 | 1 |
| **13** | **Kênh đầu tư: vàng, trái phiếu, chứng chỉ quỹ, ETF** ← *bạn đang ở đây* | C2 tr. 58–67 | 2 |
| 14 | Mục tiêu SMART và ráp lại thành kế hoạch | C1 tr. 34–40 | 1 |

Vòng 1 — học kỹ, làm hết bài tập · Vòng 2 — đọc hiểu, nắm ý là đủ.

Chỉ mục môn học: [README.md](../README.md)
<!-- /BAN-DO -->
