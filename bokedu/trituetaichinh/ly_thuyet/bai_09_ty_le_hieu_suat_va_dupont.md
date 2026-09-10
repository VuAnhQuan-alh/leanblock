# Bài 9 — Tỷ lệ hiệu suất và phân rã DuPont

> Bài học dựng từ **chương 23 — *Các tỷ lệ thể hiện hiệu suất hoạt động*** (PDF tr. 162–168) và
> **Hộp công cụ Phần V** (PDF tr. 168–170), nơi cuốn sách giấu **phân rã DuPont** dưới một tiêu đề khiêm
> tốn là *"Mối quan hệ tỷ lệ"*.
> 🎯 **Vòng 1.** Bài này đóng Phần V. Bài 8 đọc tỷ lệ trên **báo cáo kết quả kinh doanh**; chương 23 quay
> sang **bảng cân đối kế toán** — và coi nó là thứ **điều khiển được**.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 4](bai_04_bang_can_doi_ke_toan.md) ·
> [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) · [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md)
> — mọi tỷ lệ ở đây lấy mẫu số từ bảng cân đối, và [mục 8](#8-dupont-đứng-trước-enron) trả nốt lời hứa
> của bài 8.
> ⚙️ **Code:** [`thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py`](../thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py)
> — sách đưa **công thức và một phép tính mẫu** cho từng tỷ lệ rồi dừng. File này đo **giá của việc chọn
> định nghĩa**, **quy ra tiền** khoảng cách Target/Wal-Mart, và **đo bằng số** ba đòn bẩy mà hộp công cụ
> chỉ liệt kê bằng lời.

---

## Mục lục

<!-- MUC-LUC -->

- [1. "Quản lý bảng cân đối kế toán" — chương 23 nói về cái gì](#1-quản-lý-bảng-cân-đối-kế-toán--chương-23-nói-về-cái-gì)
- [2. Ngày tồn kho — và cái giá của việc chọn định nghĩa](#2-ngày-tồn-kho--và-cái-giá-của-việc-chọn-định-nghĩa)
- [3. Mười một ngày giữa Target và Wal-Mart, quy ra tiền](#3-mười-một-ngày-giữa-target-và-wal-mart-quy-ra-tiền)
- [4. DSO, DPO — và một quy ước không nhất quán ngay trong một chương](#4-dso-dpo--và-một-quy-ước-không-nhất-quán-ngay-trong-một-chương)
- [5. Tốc độ thay thế PPE — tỷ lệ có tiền thưởng gắn vào](#5-tốc-độ-thay-thế-ppe--tỷ-lệ-có-tiền-thưởng-gắn-vào)
- [6. Phân rã DuPont](#6-phân-rã-dupont)
- [7. Ba đòn bẩy của sách, đo bằng số](#7-ba-đòn-bẩy-của-sách-đo-bằng-số)
- [8. DuPont đứng trước Enron](#8-dupont-đứng-trước-enron)
- [9. 📚 Hộp công cụ Phần V — tỷ lệ riêng và phần trăm doanh thu](#9--hộp-công-cụ-phần-v--tỷ-lệ-riêng-và-phần-trăm-doanh-thu)
- [10. ⚠️ Chỗ sách in sai trong chương 23](#10--chỗ-sách-in-sai-trong-chương-23)
- [11. 🇻🇳 Đối chiếu Việt Nam — hai đường đến ROA](#11--đối-chiếu-việt-nam--hai-đường-đến-roa)
- [12. Tự thử](#12-tự-thử)
- [13. Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
- [14. Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. "Quản lý bảng cân đối kế toán" — chương 23 nói về cái gì

Bảy bài đầu **dựng** ba báo cáo. Bài 8 **đọc tỷ lệ** trên báo cáo kết quả kinh doanh. Chương 23 làm một
việc khác hẳn: nó coi bảng cân đối kế toán là thứ **có thể điều khiển được**.

> *"Cách nói **'quản lý bảng cân đối kế toán'** có thể mang ý nghĩa rất riêng, đặc biệt là khi hầu hết các
> nhà quản lý thường **chỉ tập trung vào báo cáo kết quả kinh doanh**. Nhưng hãy nghĩ thế này: bảng cân
> đối kế toán liệt kê tài sản và những khoản nợ phải trả, và những tài sản và khoản nợ phải trả này **luôn
> biến động**. Nếu bạn có thể **giảm tồn kho** hay **đẩy nhanh quá trình thu công nợ**, bạn sẽ tạo ra được
> **tác động trực tiếp và tức thời** lên tình trạng tiền mặt của doanh nghiệp."* — ch. 23 · PDF tr. 162

Và một câu nằm ngay đầu chương, dễ bỏ qua nhưng là bản lề của cả bài:

> *"Nếu bạn coi hàng tồn kho như **một khoản tiền đông cứng**, thì khi đó bạn càng đưa nó ra khỏi cửa và
> thu tiền thực về nhanh bao nhiêu, **bạn càng giàu hơn** bấy nhiêu."* — ch. 23 · PDF tr. 162

Sáu tỷ lệ của chương này đều trả lời cùng một câu hỏi: **mỗi đồng tài sản để trên bảng cân đối đang làm ra
bao nhiêu doanh thu, và nằm ở đó bao lâu?**

| tỷ lệ | giá trị | đọc bảng cân đối ở dòng nào |
| --- | ---: | --- |
| Ngày tồn kho (DII) | **74,2 ngày** | tồn kho |
| Tốc độ luân chuyển tồn kho | **4,85 lần** | tồn kho |
| Kỳ thu tiền (DSO) | **54,4 ngày** | khoản phải thu |
| Kỳ thanh toán (DPO) | **54,5 ngày** | khoản phải trả |
| Tốc độ thay thế PPE | **3,90 lần** | đất đai, nhà xưởng, thiết bị |
| Vòng quay tổng tài sản | **1,67 lần** | **toàn bộ** cột tài sản |

⚠️ Bốn tỷ lệ đầu là **con số ngày**, hai tỷ lệ sau là **số lần**. Chúng đo cùng một thứ từ hai phía, và
**bài 11** *(ch. 26–28, chưa viết)* sẽ cộng ba con số ngày đầu lại thành **một**.

---

## 2. Ngày tồn kho — và cái giá của việc chọn định nghĩa

Sách định nghĩa tử số là **tồn kho trung bình** — đầu kỳ cộng cuối kỳ chia đôi — rồi hạ một câu trong
ngoặc và đi tiếp: *"(Một số doanh nghiệp **chỉ sử dụng tồn kho cuối kỳ**)."*

Câu trong ngoặc đó đáng giá bao nhiêu?

| định nghĩa tử số | tử số | DII | tốc độ luân chuyển |
| --- | ---: | ---: | ---: |
| tồn kho **trung bình** | 1.392 | **74,2 ngày** | 4,85 lần |
| tồn kho **cuối kỳ** | 1.270 | **67,7 ngày** | 5,32 lần |

⭐ Chênh **6,5 ngày — 8,8%** — mà doanh nghiệp **không đổi một li nào**. Tồn kho năm nay **giảm** (1.514 →
1.270), nên bản cuối kỳ đẹp hơn. Nếu tồn kho **tăng** thì ngược lại.

⚠️ Đó là điều phải hỏi **trước khi** so với đối thủ: **hai bên có dùng cùng một định nghĩa không?** Chương
23 không đặt câu hỏi đó. Đối thủ chọn bản cuối kỳ trong một năm tồn kho giảm thì họ "thắng" bạn **8,8%**
mà không làm gì cả.

📚 **Tốc độ luân chuyển không phải một tỷ lệ độc lập.** Sách viết nó là $360 / \text{DII}$. Nhưng nó bằng
đúng COGS chia tồn kho — cùng một phép tính, lật ngược *(chốt bằng `assert`)*:

$$\frac{360}{74{,}2} = 4{,}8534 \qquad\qquad \frac{6.756}{1.392} = 4{,}8534$$

### ⚠️ Quy ước 360 ngày

> *"Các chuyên gia tài chính thường tính số ngày trong năm là **360 ngày, chỉ bởi đây là số tròn**."*
> — ch. 23 · PDF tr. 163

Đổi sang 365 thì **mọi** tỷ lệ ngày đều nở ra đúng $365/360 = 1{,}0139$ lần:

| | 360 ngày | 365 ngày | chênh |
| --- | ---: | ---: | ---: |
| DII | 74,2 | 75,2 | +1,0 |
| DSO | 54,4 | 55,1 | +0,8 |
| DPO | 54,5 | 55,2 | +0,8 |

Chênh nhỏ, nhưng nó **là thật**: so một công ty dùng 360 với một công ty dùng 365 là tự tạo ra **1,4%**
khác biệt mà không ai làm gì sai cả.

---

## 3. Mười một ngày giữa Target và Wal-Mart, quy ra tiền

Sách đưa hai con số rồi để nguyên:

> *"Năm 2002, chuỗi cửa hàng **Target Stores** có tốc độ luân chuyển hàng tồn kho là **6,5**, đây là một
> con số **đáng nể** đối với một nhà bán lẻ lớn. Nhưng đó vẫn chưa là gì so với tốc độ luân chuyển tồn kho
> **8,1 của Wal-Mart**. Trong ngành bán lẻ, chênh lệch trong tốc độ luân chuyển tồn kho **có thể nói lên
> sự thành công hay thất bại** của doanh nghiệp."* — ch. 23 · PDF tr. 163

**Bước một: đổi sang ngày**, vì "hơn 1,6 vòng một năm" không nói lên gì.

| | tốc độ luân chuyển | = số ngày tồn kho |
| --- | ---: | ---: |
| Target | 6,50 lần | 55,4 ngày |
| Wal-Mart | 8,10 lần | 44,4 ngày |
| **khoảng cách** | +1,60 vòng | **10,9 NGÀY** |

⭐ **10,9 ngày.** Đó là toàn bộ "sự thành công hay thất bại" mà sách nói tới.

**Bước hai: quy ra tiền.** Sách không có bảng cân đối của Target hay Wal-Mart, nên đo trên **công ty mẫu** —
nếu nó chạy được tốc độ của Wal-Mart thì tồn kho phải là bao nhiêu, và bao nhiêu tiền được **giải phóng**?

| | triệu $ | |
| --- | ---: | --- |
| tồn kho hiện tại (cuối kỳ) | 1.270 | → luân chuyển 5,32 lần |
| tồn kho nếu chạy tốc độ Wal-Mart | 834 | → luân chuyển 8,10 lần |
| **→ TIỀN ĐƯỢC GIẢI PHÓNG** | **436** | |

⭐ **436 triệu** — bằng **1,76 lần** lợi nhuận thuần cả năm (248). Một năm quản lý tồn kho tốt bằng gần
**hai năm** làm ra lợi nhuận *(chốt bằng `assert`)*. Đó là lý do sách gọi tồn kho là *"khoản tiền đông
cứng"*.

⚠️ Nhưng nếu lấy **tồn kho trung bình** làm mốc thì con số khác hẳn: **558** thay vì 436 — chênh **122
triệu**, chỉ vì [mục 2](#2-ngày-tồn-kho--và-cái-giá-của-việc-chọn-định-nghĩa). Câu trả lời phải **kèm định
nghĩa**. Con số trần không dùng được một mình.

---

## 4. DSO, DPO — và một quy ước không nhất quán ngay trong một chương

Hai tỷ lệ đối xứng nhau: bao lâu thì **khách** trả mình, bao lâu thì **mình** trả nhà cung cấp. Sách gọi
DPO là *"một dạng đối ngược với DSO"*.

| tỷ lệ | tử số | mẫu số | kết quả |
| --- | ---: | --- | ---: |
| DSO (kỳ thu tiền) | 1.312 | **doanh thu**/ngày | 54,4 ngày |
| DPO (kỳ thanh toán) | 1.022 | **COGS**/ngày | 54,5 ngày |

> *"Các nhà cung cấp của doanh nghiệp đợi một thời gian dài mới thanh toán, khoảng thời gian này **gần như
> tương đương** với thời gian mà doanh nghiệp chờ thu công nợ từ khách hàng."* — ch. 23 · PDF tr. 165

54,5 − 54,4 = 0,1 ngày. Đúng là gần như tương đương.

### ⚠️ Nhưng hai mẫu số khác nhau

DSO chia **doanh thu**, DPO chia **COGS**. Đó **không** phải lỗi — bán hàng ghi theo giá bán, mua hàng ghi
theo giá vốn — nhưng nó có nghĩa là *"54,4 gần bằng 54,5"* **không phải** là "hoà". Đổi cả hai về **tiền**
thì thấy ngay:

| | triệu $ |
| --- | ---: |
| Khoản phải thu — khách đang nợ mình | 1.312 |
| Khoản phải trả — mình đang nợ nhà cung cấp | 1.022 |
| **→ doanh nghiệp đang ỨNG RA** | **290** |

⭐ **290 triệu — bằng 1,17 lần lợi nhuận cả năm.** Hai con số **ngày** gần bằng nhau, nhưng bằng **tiền**
thì doanh nghiệp đang **tài trợ** cho chuỗi cung ứng của nó. Lý do thuần cơ học: cùng một số ngày, nhưng
một bên nhân mẫu số **8.689** còn bên kia nhân mẫu số **6.756**. **Bài 11** *(chưa viết)* sẽ gọi khoản
này đúng tên của nó: **vốn lưu động** *(chốt bằng `assert`)*.

### ⚠️ Và chương 23 không nhất quán với chính nó

| tỷ lệ | dùng số đầu kỳ? | sách in |
| --- | --- | --- |
| DII | **CÓ — trung bình** | (1.270+1.514)/2 |
| DSO | không — cuối kỳ | số cuối kỳ |
| DPO | không — cuối kỳ | số cuối kỳ |
| Tốc độ thay thế PPE | không — cuối kỳ | số cuối kỳ |
| Vòng quay tổng tài sản | không — cuối kỳ | số cuối kỳ |

⭐ **Đúng một** tỷ lệ trong năm dùng số trung bình. Bốn cái kia dùng số cuối kỳ. Cả năm mẫu số đều là con
số **cả năm**, nên về nguyên tắc cả năm đều nên dùng trung bình.

Đo thử trên PPE: cuối kỳ **3,90 lần**, trung bình **3,87 lần** — chênh **0,8%**. Nhỏ ở đây vì PPE năm nay
gần như đứng yên. **Không nhỏ** ở một doanh nghiệp vừa mua xong một nhà máy vào tháng 12.

💼 Sách cảnh báo đúng chỗ về DSO: *"theo định nghĩa nó là **một con số bình quân được điều chỉnh**… Rất có
thể có **một số hoá đơn với giá trị cao bất thường**, bị thanh toán chậm đang **làm méo xẹo** chỉ số DSO."*
Cách kiểm: **đừng nhìn DSO, nhìn bảng phân tuổi công nợ.** Một tỷ lệ là một con số; một bảng phân tuổi là
một **phân bố**.

⚠️ **DPO cao không miễn phí:** *"DPO càng cao, tình trạng tiền mặt của doanh nghiệp càng tốt, **nhưng nhà
cung cấp thì hết sức phiền lòng**. Một doanh nghiệp có tiếng là thanh toán chậm có thể thấy các nhà cung
cấp hàng đầu **không nhiệt tình giành nhau** để có được mối làm ăn với mình. **Giá họ đưa ra có thể cao
hơn**, các điều khoản của họ **có thể ngặt nghèo hơn**."* Tức là: kéo dài DPO là một khoản **vay**, trả lãi
bằng **giá mua cao hơn**.

---

## 5. Tốc độ thay thế PPE — tỷ lệ có tiền thưởng gắn vào

$$\text{Tốc độ thay thế PPE} = \frac{\text{doanh thu}}{\text{PPE}} = \frac{8.689}{2.230} = 3{,}90 \text{ lần}$$

Sách dặn ngay một câu rào, rồi lật nó lại:

> *"Bản thân con số **3,9 đô-la doanh thu cho mỗi đô-la PPE không nói lên gì nhiều**. Nhưng nó có thể mang
> nhiều ý nghĩa **khi so sánh** với hiệu quả hoạt động trước đây, và với hiệu quả hoạt động của các đối thủ
> cạnh tranh."* — ch. 23 · PDF tr. 166

> *"Nhưng vui lòng lưu ý đến **điều kiện nho nhỏ, thầm lặng này**, 'các yếu tố khác không đổi'. Thực tế,
> đây là **một tỷ lệ mà tại đó nghệ thuật tài chính có thể tác động mạnh** đến các con số. Chẳng hạn, nếu
> doanh nghiệp **thuê** phần lớn thiết bị, thay vì sở hữu chúng, tài sản đi thuê này **có thể không xuất
> hiện** trên bảng cân đối kế toán. Tổng tài sản được thể hiện ra của doanh nghiệp sẽ **thấp hơn nhiều**,
> và tốc độ thay thế PPE cũng **cao hơn tương ứng**."* — ch. 23 · PDF tr. 166–167

Đo độ lớn. Thuê đi một phần PPE, **không đổi một đồng doanh thu**:

| thuê đi | % PPE | PPE còn lại | tốc độ thay thế | so với gốc |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0% | 2.230 | 3,90 lần | 1,00 lần |
| 558 | 25% | 1.672 | 5,20 lần | 1,33 lần |
| **1.115** | **50%** | 1.115 | **7,79 lần** | **2,00 lần** |
| 1.672 | 75% | 558 | 15,59 lần | 4,00 lần |

⭐ Thuê đi đúng **một nửa** thiết bị thì tỷ lệ **gấp đôi** *(chốt bằng `assert`)*. Và sách hạ câu kết nặng
nhất của cả chương:

> *"**Một số doanh nghiệp trả thưởng theo tỷ lệ này**, điều này khiến các nhà quản lý **có động cơ thuê,
> hơn là mua** thiết bị. Việc thuê như vậy có thể mang ý nghĩa chiến lược với doanh nghiệp, **hoặc không**.
> **Điểm vô lý ở đây là việc ra quyết định dựa trên cơ sở thanh toán thưởng.**"* — ch. 23 · PDF tr. 167

📌 [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 7 đã đo **giá** của thủ thuật này: đưa 770 ra
khỏi bảng bằng hợp đồng thuê làm doanh nghiệp **đắt thêm 22 triệu mỗi năm** ở phí thuê 14%. Chỗ này thêm
một vế: **có người được thưởng vì khoản chi thêm đó.** Và IFRS 16 / ASC 842 (2019) đã bịt lỗ hổng — nhưng
chỉ bịt về **kế toán**, không bịt về **động cơ**.

---

## 6. Phân rã DuPont

Điều này **không nằm trong chương 23**. Nó nằm trong **hộp công cụ cuối Phần V**, dưới một tiêu đề khiêm
tốn là *"Mối quan hệ tỷ lệ"*, và sách còn rào trước:

> *"Chúng tôi sẽ **không đi sâu vào chi tiết** ở đây, bởi cuốn sách này không nhắm tới các chuyên gia tài
> chính. **Nhưng** giữa các tỷ lệ này có **một mối quan hệ rất đáng được nói rõ**."* — ch. 23 · PDF tr. 169–170

$$\underbrace{\frac{\text{thu nhập thuần}}{\text{doanh thu}}}_{\text{biên lợi nhuận thuần}} \times
\underbrace{\frac{\text{doanh thu}}{\text{tài sản}}}_{\text{vòng quay tài sản}} =
\frac{\text{thu nhập thuần}}{\text{tài sản}} = \text{ROA}$$

$$2{,}854\% \times 1{,}6732 = 4{,}776\% \qquad\left(\text{ROA} = \frac{248}{5.193} = 4{,}776\%\right)$$

Doanh thu triệt tiêu. Đó là một **đồng nhất thức**, không phải một ước lượng — đúng với mọi doanh nghiệp,
mọi năm, không điều kiện *(chốt bằng `assert`)*.

⭐ Nhưng đồng nhất thức đó làm một việc thật: nó **chia câu hỏi** *"ROA của chúng ta có tốt không?"* thành
**hai câu hỏi trả lời được**:

- số hạng thứ nhất — **biên lợi nhuận thuần** — là câu hỏi của **báo cáo kết quả kinh doanh**: mỗi đồng
  doanh thu giữ lại được bao nhiêu?
- số hạng thứ hai — **vòng quay tài sản** — là câu hỏi của **bảng cân đối kế toán**: mỗi đồng tài sản làm
  ra được bao nhiêu doanh thu?

Sách đọc đúng ra hai đường:

> *"Có **hai cách để bật nhảy qua vòng**, với 'vòng' ở đây là ROA cao. **Một là** tăng tỷ lệ lợi nhuận
> thuần, thông qua các hình thức hoặc là **tăng giá**, hoặc là **cung cấp hàng hoá hoặc dịch vụ hiệu quả
> hơn**. Cách này **có thể sẽ khó thực hiện** nếu thị trường doanh nghiệp đang hoạt động có mức độ cạnh
> tranh cao. **Cách thứ hai** là tăng tốc độ luân chuyển tài sản."* — ch. 23 · PDF tr. 170

Đo hai đường ấy. Mục tiêu: đưa ROA từ **4,78%** lên **6%**, mỗi đường **đi một mình**:

| đường | phải đổi | mức đổi | % phải đổi |
| --- | --- | ---: | ---: |
| ① tăng biên lợi nhuận | lợi nhuận 248 → **312** | +64 | **+25,6%** |
| ② tăng vòng quay | tài sản 5.193 → **4.133** | −1.060 | **−20,4%** |

⭐ Cùng một đích đến, **hai cái giá rất khác nhau về bản chất**:

- đường ① đòi doanh nghiệp **kiếm thêm 64 triệu lợi nhuận** — tăng giá hoặc hạ chi phí, trong một thị
  trường đã cạnh tranh. Sách gọi thẳng là *"khó thực hiện"*.
- đường ② đòi doanh nghiệp **để xuống 1.060 triệu tài sản** — mà **không cần bán thêm một món hàng nào**.

[Mục 7](#7-ba-đòn-bẩy-của-sách-đo-bằng-số) đo xem đường ② có đủ chi tiết để đi không.

---

## 7. Ba đòn bẩy của sách, đo bằng số

Sách liệt kê đúng ba hành động cho đường ②, rồi dừng:

> *"Cách này mở ra một loạt những hành động khả thi: **giảm tồn kho trung bình**, **giảm kỳ thu tiền bình
> quân**, và **giảm mua đất đai, nhà xưởng và thiết bị**."* — ch. 23 · PDF tr. 170

Đo từng cái. Cần để xuống **1.060 triệu**:

| đòn bẩy | từ | xuống | gộp được |
| --- | ---: | ---: | ---: |
| ① tồn kho → tốc độ Wal-Mart 8,1 | 1.270 | 834 | **436** |
| ② DSO 54,4 → 40 ngày *(sách gợi ý)* | 1.312 | 965 | **347** |
| **hai đòn bẩy đầu tiên** | | | **782** |
| còn thiếu → phải chạm vào **PPE** | | | 277 |

⭐ Hai đòn bẩy "không đau đớn" gộp **782 triệu — 74% quãng đường**. **277 triệu** còn lại phải lấy từ PPE
(**12,4%** thiết bị) — và **đó** là đòn bẩy có hậu quả thật: ít thiết bị hơn thì ít năng lực hơn.

### ⚠️ Nhưng dừng lại — tiền vẫn nằm trên bảng

Giảm tồn kho và thu tiền về **không làm tổng tài sản giảm**. Tồn kho giảm 436 → **tiền tăng 436**. Phải thu
giảm 347 → **tiền tăng 347**. Cả hai đều là **tài sản ngắn hạn**.

| | trước | sau |
| --- | ---: | ---: |
| Tiền | 83,00 | **865,48** |
| Khoản phải thu | 1.312,00 | 965,44 |
| Tồn kho | 1.270,00 | 834,07 |
| **TỔNG TÀI SẢN** | **5.193,00** | **5.193,00** |
| Vòng quay tổng tài sản | 1,67 | **1,67** |
| ROA | 4,78% | **4,78%** |

⭐ **Đó là cái bẫy.** Ba dòng trên đổi rất nhiều, hai dòng dưới **không đổi một li**. Vòng quay tổng tài
sản chỉ tăng khi **tiền ấy ra khỏi bảng cân đối** *(tổng tài sản ngắn hạn không đổi — chốt bằng `assert`)*.

Nhưng một số tỷ lệ **khác** thì đổi ngay lập tức — đó là lý do vẫn nên làm:

| | trước | sau |
| --- | ---: | ---: |
| DII *(ngày, cuối kỳ)* | 67,7 | **44,4** |
| DSO *(ngày)* | 54,4 | **40,0** |
| Hệ số thanh toán ngắn hạn | 2,34 | 2,34 |
| Hệ số thanh toán nhanh | 1,26 | **1,63** |

⭐ Hệ số thanh toán **nhanh** nhảy từ 1,26 lên **1,63** — vì tồn kho bị trừ ra còn tiền thì không. Hệ số
**ngắn hạn** đứng yên. [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 8 nói hai hệ số này *"khác
nhau ở đúng một dòng"*; đây là lúc dòng ấy lên tiếng.

### Vậy đưa tiền đi đâu — và đây là chỗ đóng lại bài 8

[Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 7 đã hỏi đúng câu này từ phía ngược lại: để hạ
nợ/vốn chủ từ 1,11 xuống 0,80 cần đưa **770 triệu** ra khỏi bảng, và cách bài 8 xét đến là **đi thuê tài
sản**, đắt thêm **22 triệu mỗi năm** ở phí thuê 14%.

**Chương 23 đưa ra 782 triệu mà không tốn một đồng nào** *(chốt bằng `assert`)*.

Làm thật đi: dùng 782 triệu tiền đó **trả bớt nợ** *(so sánh tĩnh, một bước)*. Lãi suất vay hiện tại
191/1.714 = **11,1%/năm** → tiết kiệm **87 triệu** lãi, sau thuế *(thuế suất 46,2%)* còn **47 triệu**.

| | trước | sau |
| --- | ---: | ---: |
| Lợi nhuận thuần | 248 | **295** |
| Tổng tài sản | 5.193 | **4.411** |
| ① Biên lợi nhuận thuần | 2,854% | **3,394%** |
| ② Vòng quay tổng tài sản | 1,6732 | **1,9701** |
| **① × ② = ROA** | **4,78%** | **6,69%** |
| Nợ / vốn chủ sở hữu | 1,11 | **0,80** |

⭐ ROA đi từ 4,78% lên **6,69%** — **vượt** mục tiêu 6% của [mục 6](#6-phân-rã-dupont) — và **cả hai số
hạng DuPont cùng tăng**. Không bán thêm một món hàng nào *(chốt bằng `assert`)*.

⚠️ **Ba điều bài học này *không* khẳng định:**

- rằng tốc độ Wal-Mart là khả thi với mọi ngành — **nó không**;
- rằng cắt DSO xuống 40 không làm mất khách — sách đã liệt kê bốn nguyên nhân DSO cao, trong đó có *"nhân
  viên bán hàng quá dễ dãi khi đàm phán các điều khoản"*;
- rằng trả nợ là cách dùng tiền tốt nhất — đây chỉ là **một** cách, chọn vì nó **đo được** bằng chính số
  liệu có sẵn.

---

## 8. DuPont đứng trước Enron

[Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 4 dựng lại Enron: đẩy tài sản ra khỏi bảng cân
đối, giữ nguyên lợi nhuận, thì ROA gấp đôi — và cảnh báo rằng **vòng quay tài sản cũng tăng theo**. Giờ có
đủ hai số hạng để xem DuPont nói gì.

| | thật | sau bút toán |
| --- | ---: | ---: |
| Doanh thu | 8.689 | 8.689 |
| Lợi nhuận thuần | 248 | 248 |
| Tổng tài sản | 5.193 | **2.596** |
| ① Biên lợi nhuận thuần | 2,854% | **2,854%** |
| ② Vòng quay tài sản | 1,6732 | **3,3471** |
| **① × ② = ROA** | 4,78% | **9,55%** |

⭐ **DuPont nói một câu hoàn toàn đúng:** số hạng ① không nhúc nhích, nên **toàn bộ** mức tăng ROA đến từ
số hạng ②. Phân rã đã làm đúng việc của nó — nó **định vị** được chỗ thay đổi, thứ mà ROA trần không làm
được.

⚠️ **Chỗ sai nằm ở cái tên.** Số hạng ② được gọi là *"hiệu suất sử dụng tài sản"*, và ở đây tài sản **không**
được dùng hiệu quả hơn — nó chỉ **đi chỗ khác**. Người đọc dừng lại ở đây sẽ kết luận *"hiệu suất tuyệt
vời"*. Đó là **dừng sớm một bước**.

⭐ **Câu hỏi tiếp theo mà DuPont buộc bạn phải hỏi:** tài sản thật sự **co lại**, hay chỉ **di chuyển**? Và
**không một tỷ lệ nào trong Phần V trả lời được nó.** Chỉ có:

- **báo cáo lưu chuyển tiền tệ** — bán tài sản thì tiền phải vào mục **đầu tư**
  ([bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md));
- **thuyết minh** — các bên liên quan, cam kết ngoài bảng.

Đó là **ranh giới của cả Phần V**, và sách đặt nó ngay ở câu kết chương 23:

> *"Các tỷ lệ đưa bạn tới **tầng bậc tiếp theo**; chúng mở ra cho bạn cách thức hiểu **ý nghĩa hàm ẩn giữa
> (hoặc có thể là bên dưới) các dòng**, nhờ đó bạn có thể thấy những gì đang thật sự diễn ra."*
> — ch. 23 · PDF tr. 168

💼 **Kiểm tra nhanh dùng được ngay:** nếu vòng quay tài sản của một doanh nghiệp tăng mạnh, hãy hỏi **tài
sản nào giảm**. Nếu câu trả lời là *"chúng tôi đã chuyển sang mô hình nhẹ tài sản"* thì hỏi tiếp: chuyển
**sang đâu**, và **ai đang sở hữu** chúng.

---

## 9. 📚 Hộp công cụ Phần V — tỷ lệ riêng và phần trăm doanh thu

Hộp công cụ cho hai thứ mà chương 23 không cho.

### ① Tỷ lệ tự chế

> *"Các doanh nghiệp thường muốn **tạo ra những tỷ lệ trọng yếu của riêng mình**, tuỳ theo hoàn cảnh và
> tình hình cạnh tranh của bản thân."* — ch. 23 · PDF tr. 168

Ví dụ thật: công ty **Setpoint** của Joe — nhỏ, làm theo dự án — theo hai tỷ lệ. Một là tỷ lệ tự chế:
**lợi nhuận gộp chia chi phí hoạt động**, *"đảm bảo rằng chi phí hoạt động không chệch ra khỏi lợi nhuận
gộp mà công ty đang tạo ra"*. Hai là hệ số thanh toán ngắn hạn.

Trên công ty mẫu: $1.933 / 1.300 = \mathbf{1{,}49}$ lần. Ý nghĩa trực tiếp: **nếu tỷ lệ này về 1 thì EBIT
về 0.** Kiểm: 1.933 − 1.300 = 633, và EBIT = 652 — chênh đúng bằng thu nhập khác 19 *(chốt bằng `assert`)*.

### ② Phần trăm doanh thu

> *"Bạn sẽ thường nhìn thấy một dạng tỷ lệ được **lồng ghép ngay trong** báo cáo kết quả kinh doanh: mỗi
> khoản mục sẽ được thể hiện không chỉ dưới dạng đồng, mà còn dưới dạng **phần trăm doanh thu**."*
> — ch. 23 · PDF tr. 169

Sách ra bài tập: *"lấy **ba báo cáo kết quả kinh doanh gần đây**, và tính toán phần trăm doanh thu cho từng
khoản mục lớn."* Kho chỉ có một bộ số liệu cho công ty mẫu, nên làm biến thể: **hai doanh nghiệp**.

| khoản mục | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) | chênh |
| --- | ---: | ---: | ---: |
| Doanh thu | 100,0% | 100,0% | 0,0 |
| Giá vốn hàng bán | **77,8%** | **71,2%** | **−6,6** |
| Lợi nhuận gộp | 22,2% | 28,8% | +6,6 |
| Chi phí bán hàng + quản lý | 15,0% | 10,5% | −4,5 |
| **EBIT** | **7,5%** | **18,4%** | **+10,9** |
| Lợi nhuận thuần | 2,9% | 16,5% | +13,7 |

⭐ Đọc dòng **giá vốn**: 77,8% so với 71,2%. Chênh **6,6 điểm phần trăm** — và đó gần như là **toàn bộ**
chênh lệch biên lợi nhuận gộp. Dòng chi phí bán hàng + quản lý thì Vinamilk cũng thấp hơn **4,5 điểm**. Hai
dòng cộng lại giải thích vì sao EBIT cách nhau **10,9 điểm phần trăm**.

⭐ Đó chính là thứ sách hứa: *"các phép tính phần trăm doanh thu mang lại cho nhà quản lý **nhiều thông tin
hơn những số liệu thô**."* Số thô thì một bên tính bằng triệu đô-la, một bên bằng triệu đồng — **không so
được**. Đổi ra phần trăm thì hai báo cáo cách nhau 19 năm và một đại dương **dùng chung một thước đo**.

---

## 10. ⚠️ Chỗ sách in sai trong chương 23

Chương 23 có **sáu ô công thức**. Hai trong số đó sai số, và cả hai đều ở chỗ dễ kiểm.

| # | chỗ | sách in | đúng ra |
| ---: | --- | --- | --- |
| ① | tr. 163 | DII, mẫu số **6.765** | COGS là **6.756** — xem dưới |
| ② | tr. 164 | DSO = **54,5** | **54,4**. 54,5 là DPO ở ô ngay dưới (tr. 165) |
| ③ | tr. 165 | *"**PDO** càng cao, tình trạng tiền mặt càng tốt"* | viết tắt là **DPO**. Đảo hai chữ cái |
| ④ | tr. 162 | *"bảng cân đối kế **toán toán** liệt kê tài sản"* | thừa một chữ *"toán"* |
| ⑤ | tr. 162, 165 | trỏ tới *"**Phần VII**"* cho phần vốn lưu động | bản dịch in phần đó là **"PHẦN VI"** — xem dưới |

**① Mẫu số DII.** Kiểm cả hai khả năng:

| dùng mẫu số | DII | làm tròn |
| ---: | ---: | ---: |
| 6.765 *(sách in)* | 74,08 | 74,1 |
| **6.756** *(COGS thật)* | 74,17 | **74,2** ← đúng con số sách in |

Kết quả **74,2 chỉ khớp khi dùng 6.756**. Tức là chỉ **con số in ra** sai, còn **phép tính phía sau thì
đúng**. Rớt một chữ số *(chốt bằng `assert`)*.

**② DSO.** $1.312 / (8.689/360) = 54{,}358 \to \mathbf{54{,}4}$. Còn 54,5 là **DPO** — ở ô công thức ngay
dưới. Khả năng cao là chép nhầm xuống. Và câu văn ngay sau ô công thức viết *"khoảng 54 ngày"*, khớp với
54,4 hơn *(chốt bằng `assert`)*.

**⑤ Lỗi đánh số phần, lộ ra ngay bên trong một chương.** Hai câu trỏ ngược trong chương 23:

> *"(Chúng tôi sẽ nói thêm về vấn đề quản lý bảng cân đối kế toán trong **Phần VII**)."* — tr. 162
> *"Chúng ta sẽ quay trở lại với DSO trong **Phần VII**, trong nội dung về quản lý vốn lưu động."* — tr. 165

Nhưng bản dịch in phần đó là **"PHẦN VI"** (tr. 192) — **và cũng in "Phần VI"** cho phần ROI (tr. 170).
**Hai phần cùng mang số VI.** Bản gốc có **8 phần**; hai câu trỏ ngược ở trên dùng số của **bản gốc**, còn
trang tiêu đề thì dùng số **bị đánh nhầm**. Đây là chỗ lỗi đánh số phần **lộ ra** ngay bên trong một chương
— thứ mà [README](../README.md) mới chỉ ghi nhận ở mục lục.

### Cộng cả Phần V lại

| lớp lỗi | ch. 19–21 *(bài 8)* | ch. 23 *(bài này)* | tổng |
| --- | ---: | ---: | ---: |
| lỗi **nhãn** / tham chiếu | 4 | 3 | **7** |
| lỗi **số** | 1 | 2 | **3** |

*(chưa kể biên lợi nhuận thuần 2,8% ở tr. 151, nằm ở ranh giới làm tròn)*

Tỷ lệ hai lớp lỗi này tự nó là một dữ kiện: **phần chữ ít sai hơn phần ô công thức**, và cái sai hay gặp
nhất **không phải con số — là cái tên đặt cho con số**.

---

## 11. 🇻🇳 Đối chiếu Việt Nam — hai đường đến ROA

Năm tỷ lệ hiệu suất của chương 23, hai doanh nghiệp:

| | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| --- | ---: | ---: |
| Ngày tồn kho (DII) | 74,2 ngày | **56,4 ngày** |
| Kỳ thu tiền (DSO) | 54,4 ngày | **43,7 ngày** |
| Kỳ thanh toán (DPO) | 54,5 ngày | **78,2 ngày** |
| Vòng quay tổng tài sản | **1,67 lần** | **0,92 lần** |
| Tốc độ thay thế PPE | **3,90 lần** | **4,44 lần** |

⚠️ Đọc **hai dòng cuối cùng nhau** thì thấy một điều nghịch lý:

- tốc độ thay thế **PPE**: 3,90 → 4,44 — **Vinamilk cao hơn**;
- vòng quay **tổng tài sản**: 1,67 → 0,92 — **Vinamilk thấp hơn hẳn**.

Tài sản **cố định** của Vinamilk làm việc **nặng hơn**, mà **tổng** tài sản lại quay **chậm hơn gần một
nửa**. Vậy cái gì đang nằm giữa?

| khoản mục | triệu VND | % tổng tài sản |
| --- | ---: | ---: |
| Tiền và tương đương tiền | 2.225.944 | 3,9% |
| Đầu tư tài chính ngắn hạn | 23.260.089 | **40,8%** |
| **→ CỘNG** | **25.486.033** | **44,7%** |

⭐ **45% tổng tài sản của Vinamilk là tiền và tiền gửi**, không phải tài sản vận hành. Bỏ hai dòng đó ra
khỏi mẫu số ở **cả hai** công ty rồi tính lại:

| | Công ty mẫu | Vinamilk |
| --- | ---: | ---: |
| vòng quay **TỔNG** tài sản | 1,67 lần | 0,92 lần |
| vòng quay tài sản **VẬN HÀNH** | **1,70 lần** | **1,67 lần** |

⭐ **1,70 so với 1,67 — chênh 1,9%.** Sau khi bỏ đống tiền ra, **hai doanh nghiệp quay tài sản vận hành
gần như bằng nhau**. Toàn bộ ấn tượng *"Vinamilk kém hiệu suất"* đến từ **một dòng trên bảng cân đối**,
không từ hoạt động *(chốt bằng `assert`)*.

⚠️ Điều này **không** có nghĩa đống tiền đó là lãng phí —
[bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 8 đã chỉ ra công ty mẫu chỉ trụ được **3,8 ngày**
bằng tiền mặt. Hai doanh nghiệp đang ở hai thái cực, và cả hai đều **trả giá** cho vị trí của mình. Ý ở đây
chỉ là: **vòng quay tổng tài sản gộp cả hai thứ vào một con số**, nên phải tách ra trước khi kết luận.

### Phân rã DuPont cho cả hai

| | Công ty mẫu | Vinamilk | tỷ số |
| --- | ---: | ---: | ---: |
| ① biên lợi nhuận thuần | 2,85% | 16,52% | **5,79 lần** |
| ② vòng quay tổng tài sản | 1,67 lần | 0,92 lần | **0,55 lần** |
| **① × ② = ROA** | **4,78%** | **15,24%** | **3,19 lần** |

⭐ Đọc cột cuối: $5{,}79 \times 0{,}55 = 3{,}19$ = đúng tỷ số ROA *(chốt bằng `assert`)*.

Vinamilk hơn công ty mẫu **3,19 lần** về ROA — nhưng **không phải vì làm mọi thứ tốt hơn**. Nó hơn **5,79
lần** ở biên lợi nhuận, và **thua 45%** ở vòng quay. **Toàn bộ lợi thế nằm ở một số hạng, và số hạng kia
kéo ngược lại.**

💼 Đó là cách dùng DuPont trong đời thật: **không phải để tính ROA** — tính thẳng còn nhanh hơn — mà để trả
lời *"chúng ta hơn/kém họ ở chỗ nào"*. Một con số ROA nói **ai thắng**. Hai số hạng nói **vì sao**, và đó
mới là thứ **hành động được**.

📚 **Ba lưu ý khi tính các tỷ lệ này trên báo cáo Việt Nam:**

- **"Đầu tư tài chính ngắn hạn" là dòng phải nhìn kỹ nhất.** Ở Vinamilk nó là tiền gửi có kỳ hạn, nhưng ở
  doanh nghiệp khác nó có thể là cổ phiếu, trái phiếu, hoặc cho vay bên liên quan. Vòng quay tổng tài sản
  gộp tất cả vào một chỗ.
- **DSO tính từ "phải thu khách hàng VÀ phải thu khác"** vì báo cáo IFRS của Vinamilk gộp chung một dòng —
  nên nó **hơi cao** so với DSO thuần thương mại. Trên báo cáo VAS theo Thông tư 200 thì hai dòng tách
  riêng và con số sẽ thấp hơn.
- **DPO 78,2 ngày của Vinamilk lớn hơn DSO 43,7 ngày.** Ngược hẳn công ty mẫu. Nghĩa là **nhà cung cấp đang
  tài trợ vốn lưu động cho Vinamilk**, chứ không phải ngược lại — chủ đề của **bài 11** *(chưa viết)*.

---

## 12. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py`](../thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py) rồi
chạy lại. Không có lời giải.

1. **Năm tồn kho tăng.** Ở mục 2, đổi tồn kho 2004 thành **1.000** (tức năm nay tồn kho *tăng*). Bản cuối
   kỳ giờ đẹp hơn hay xấu hơn bản trung bình? Điều này nói gì về việc chọn định nghĩa **có lợi cho mình**?

2. **Ngưỡng 365 ngày.** Ở mục 2, DII phải lớn đến mức nào thì chênh lệch 360/365 vượt **5 ngày**? Ngành nào
   có DII lớn như thế?

3. **Target thay vì Wal-Mart.** Ở mục 3, đặt mục tiêu là tốc độ của **Target (6,5)** thay vì Wal-Mart. Tiền
   giải phóng còn bao nhiêu phần trăm? Khoảng cách 10,9 ngày ấy đáng giá bao nhiêu **mỗi ngày**?

4. **DPO quy về cùng mẫu số.** Ở mục 4, tính DPO bằng cách chia **doanh thu**/ngày thay vì COGS/ngày. Con
   số ra bao nhiêu? Vì sao cách này **sai** về mặt kế toán nhưng lại **đúng** khi so với DSO?

5. **PPE trung bình.** Vẫn mục 4, giả sử doanh nghiệp mua thêm **800 triệu** PPE vào tháng 12. Tốc độ thay
   thế PPE tính theo số cuối kỳ và theo trung bình chênh nhau bao nhiêu phần trăm? Con số nào **trung
   thực** hơn?

6. **Thưởng theo tỷ lệ nào.** Ở mục 5, giả sử bạn là CEO và phải chọn **một** tỷ lệ để trả thưởng cho giám
   đốc nhà máy. Chọn tốc độ thay thế PPE hay vòng quay tổng tài sản? Mỗi lựa chọn **khuyến khích** hành vi
   gì, và **mở ra** lỗ hổng gì?

7. **Mục tiêu ROA 8%.** Ở mục 6, đổi mục tiêu từ 6% lên **8%**. Đường ① đòi bao nhiêu phần trăm lợi nhuận
   tăng thêm? Đường ② còn khả thi không?

8. **Ba đòn bẩy không đủ.** Ở mục 7, nếu doanh nghiệp **không được động vào PPE**, DSO phải xuống bao nhiêu
   ngày để một mình nó bù được phần thiếu? Con số đó có thực tế không?

9. **Tiền dùng để trả cổ tức.** Vẫn mục 7, thay vì trả nợ, dùng 782 triệu để **trả cổ tức**. ROA mới là bao
   nhiêu? Vì sao nó **khác** kết quả trả nợ, dù cả hai đều đưa tiền ra khỏi bảng?

10. **Enron ở mức nhẹ hơn.** Ở mục 8, đẩy **10%** tài sản ra ngoài thay vì 50%. Vòng quay tăng bao nhiêu?
    Ở mức nào thì một người ngoài **không thể** phân biệt được với hiệu suất thật?

11. **DuPont ba số hạng.** Nhân thêm $\frac{\text{tài sản}}{\text{vốn chủ}}$ vào phân rã ở mục 11 thì được
    **ROE**. Tính cho cả hai doanh nghiệp. Số hạng thứ ba nói lên điều gì mà bài 8 mục 5 đã đo?

12. **Vinamilk không có đống tiền.** Ở mục 11, giả sử Vinamilk trả toàn bộ 25.486 tỷ tiền và đầu tư ngắn
    hạn cho cổ đông. ROA và ROE mới là bao nhiêu? Doanh nghiệp **an toàn hơn hay rủi ro hơn**?

---

## 13. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Tỷ lệ hiệu suất hoạt động | efficiency ratio | nhóm tỷ lệ đọc **bảng cân đối**, không đọc báo cáo KQKD |
| Quản lý bảng cân đối kế toán | balance sheet management | coi tài sản/nợ là thứ **điều khiển được**, không phải kết quả |
| Ngày tồn kho | days in inventory (DII) | tồn kho / COGS mỗi ngày — hàng nằm trong hệ thống bao lâu |
| Tốc độ luân chuyển tồn kho | inventory turn | $360/\text{DII}$ = COGS / tồn kho. Cao hơn thì tốt hơn |
| Kỳ thu tiền bình quân | days sales outstanding (DSO) | phải thu / **doanh thu** mỗi ngày |
| Kỳ thanh toán bình quân | days payable outstanding (DPO) | phải trả / **COGS** mỗi ngày. Cao = vay của nhà cung cấp |
| Tốc độ thay thế PPE | PPE turnover | doanh thu / PPE — **tỷ lệ dễ bị thuê tài sản bóp méo nhất** |
| Vòng quay tổng tài sản | total asset turnover | doanh thu / tổng tài sản — số hạng ② của DuPont |
| Phân rã DuPont | DuPont analysis | ROA = biên lợi nhuận × vòng quay tài sản. **Đồng nhất thức** |
| Phần trăm doanh thu | common-size / percent of sales | mọi dòng chia cho doanh thu — cho phép so hai doanh nghiệp |
| Bảng phân tuổi công nợ | AR aging report | phân bố phải thu theo số ngày quá hạn — thứ DSO **giấu đi** |
| 💼 Tài sản vận hành | operating assets | tổng tài sản **trừ** tiền và đầu tư tài chính — **không có trong sách** |

---

## 14. Câu hỏi tự kiểm tra

1. *"Quản lý bảng cân đối kế toán"* nghĩa là gì? Vì sao hầu hết nhà quản lý không làm? (mục 1)
2. Sách ví hàng tồn kho với hình ảnh nào? (mục 1)
3. Kể sáu tỷ lệ của chương 23 và mỗi cái đọc dòng nào trên bảng cân đối. (mục 1)
4. Hai định nghĩa tử số của DII cho chênh lệch bao nhiêu ngày, bao nhiêu phần trăm? (mục 2)
5. Trong năm nào thì bản **cuối kỳ** đẹp hơn bản trung bình, và ngược lại? (mục 2)
6. Chứng minh tốc độ luân chuyển tồn kho = COGS / tồn kho. (mục 2)
7. Vì sao dân tài chính dùng 360 ngày? Đổi sang 365 thì mọi tỷ lệ ngày thay đổi thế nào? (mục 2)
8. Target và Wal-Mart cách nhau bao nhiêu **vòng**, bao nhiêu **ngày**? (mục 3)
9. Nếu công ty mẫu chạy được tốc độ Wal-Mart, bao nhiêu tiền được giải phóng? Bằng mấy lần lợi nhuận năm?
   (mục 3)
10. Vì sao con số ở câu 9 **phải kèm định nghĩa** mới dùng được? (mục 3)
11. DSO và DPO khác nhau ở **mẫu số** thế nào? Vì sao khác biệt đó **không** phải lỗi? (mục 4)
12. *"54,4 gần bằng 54,5"* — vì sao đó **không** phải là "hoà"? Đổi ra tiền thì bao nhiêu? (mục 4)
13. Trong năm tỷ lệ của chương 23, **mấy** cái dùng số trung bình? Vì sao đó là điểm không nhất quán?
    (mục 4)
14. Sách cảnh báo gì về DSO như một *"con số bình quân được điều chỉnh"*? Cách kiểm là gì? (mục 4)
15. DPO cao có miễn phí không? Doanh nghiệp trả giá bằng gì? (mục 4)
16. Thuê đi một nửa PPE thì tốc độ thay thế PPE đổi bao nhiêu? Doanh thu đổi bao nhiêu? (mục 5)
17. Sách nói *"điểm vô lý"* nằm ở đâu trong chuyện thưởng theo tỷ lệ? (mục 5)
18. Viết phân rã DuPont. Vì sao nó là **đồng nhất thức** chứ không phải ước lượng? (mục 6)
19. Hai số hạng của DuPont ứng với **báo cáo nào**? (mục 6)
20. Sách nêu **hai cách** để tăng ROA. Cách nào sách gọi là *"khó thực hiện"*, và vì sao? (mục 6)
21. Để ROA đi từ 4,78% lên 6%, mỗi đường **một mình** đòi thay đổi bao nhiêu phần trăm? (mục 6)
22. Kể **ba đòn bẩy** sách liệt kê cho đường ②. Hai cái đầu gộp được bao nhiêu phần trăm quãng đường?
    (mục 7)
23. Vì sao giảm tồn kho **không** làm tăng vòng quay tổng tài sản? (mục 7)
24. Tỷ lệ nào **đổi ngay** khi giảm tồn kho, tỷ lệ nào **đứng yên**? Vì sao? (mục 7)
25. Bài 8 cần bao nhiêu để hạ nợ/vốn chủ xuống 0,80, và trả giá thế nào? Chương 23 làm được không? (mục 7)
26. Sau khi dùng tiền trả bớt nợ, **cả hai** số hạng DuPont thay đổi ra sao? (mục 7)
27. Kể ba điều bài học **không** khẳng định ở mục 7.
28. Sau bút toán Enron, số hạng nào của DuPont đổi, số hạng nào không? (mục 8)
29. Vì sao nói DuPont *"nói một câu hoàn toàn đúng"* nhưng người đọc vẫn kết luận sai? (mục 8)
30. Báo cáo nào trả lời được câu *"tài sản co lại hay di chuyển?"* (mục 8)
31. Setpoint tự chế tỷ lệ nào? Nếu nó về 1 thì điều gì xảy ra? (mục 9)
32. Vì sao **phần trăm doanh thu** cho phép so công ty mẫu với Vinamilk mà số thô thì không? (mục 9)
33. Chênh lệch EBIT 10,9 điểm phần trăm giữa hai doanh nghiệp đến từ hai dòng nào? (mục 9)
34. Kể năm chỗ sách in sai trong chương 23. Mấy chỗ là lỗi **số**? (mục 10)
35. DII mẫu số 6.765 hay 6.756? Chứng minh bằng kết quả 74,2. (mục 10)
36. Lỗi đánh số phần lộ ra thế nào ngay bên trong chương 23? (mục 10)
37. Cộng cả Phần V: bao nhiêu lỗi **nhãn**, bao nhiêu lỗi **số**? Tỷ lệ đó nói lên điều gì? (mục 10)
38. Nghịch lý gì khi đọc tốc độ thay thế PPE và vòng quay tổng tài sản của Vinamilk cùng nhau? (mục 11)
39. Bỏ tiền và đầu tư ngắn hạn ra khỏi mẫu số thì hai doanh nghiệp quay tài sản vận hành thế nào? (mục 11)
40. Tách chênh lệch ROA 3,19 lần thành hai thừa số. Số hạng nào **kéo ngược lại**? (mục 11)
41. Vì sao DuPont hữu ích **không phải** để tính ROA? (mục 11)
42. DPO của Vinamilk lớn hơn DSO — điều đó nghĩa là gì về vốn lưu động? (mục 11)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 9 — TỶ LỆ HIỆU SUẤT VÀ PHÂN RÃ DUPONT                               ║
║           (ch. 23 + hộp công cụ Phần V, PDF tr. 162–170)                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⭐ "QUẢN LÝ BẢNG CÂN ĐỐI KẾ TOÁN"                                       ║
║     bảy bài đầu DỰNG báo cáo; bài 8 ĐỌC TỶ LỆ trên báo cáo KQKD;         ║
║     chương 23 coi BẢNG CÂN ĐỐI là thứ ĐIỀU KHIỂN ĐƯỢC.                   ║
║     "tồn kho = MỘT KHOẢN TIỀN ĐÔNG CỨNG"                                 ║
║     DII 74,2 · turn 4,85 · DSO 54,4 · DPO 54,5 · PPE 3,90 · TS 1,67      ║
║                                                                          ║
║  ĐỊNH NGHĨA CŨNG LÀ MỘT ĐÒN BẨY                                          ║
║     tồn kho trung bình → DII 74,2 ngày                                   ║
║     tồn kho cuối kỳ    → DII 67,7 ngày   CHÊNH 8,8%, DN KHÔNG ĐỔI GÌ     ║
║     360 vs 365 ngày: mọi tỷ lệ ngày nở ra 1,4%                           ║
║                                                                          ║
║  ⭐ 11 NGÀY GIỮA TARGET (6,5) VÀ WAL-MART (8,1)                          ║
║     55,4 ngày vs 44,4 ngày. Trên công ty mẫu, chạy tốc độ Wal-Mart       ║
║     GIẢI PHÓNG 436 TRIỆU = 1,76 LẦN lợi nhuận cả năm.                    ║
║                                                                          ║
║  DSO ≈ DPO KHÔNG PHẢI LÀ "HOÀ"                                           ║
║     54,4 vs 54,5 ngày — nhưng mẫu số khác nhau (8.689 vs 6.756).         ║
║     Bằng TIỀN: 1.312 − 1.022 = 290 doanh nghiệp đang ỨNG RA.             ║
║     ⚠️ chỉ MỘT trong năm tỷ lệ dùng số trung bình. Bốn cái kia cuối kỳ.  ║
║                                                                          ║
║  ⭐ PHÂN RÃ DUPONT — thứ duy nhất NỐI các tỷ lệ lại                      ║
║        biên LN thuần  ×  vòng quay tài sản  =  ROA                       ║
║          2,854%       ×      1,6732         =  4,776%                    ║
║     ① câu hỏi của BÁO CÁO KQKD   ② câu hỏi của BẢNG CÂN ĐỐI              ║
║     ROA 4,78 → 6%:  ① lợi nhuận +25,6%   ② tài sản −20,4%                ║
║                                                                          ║
║  ⭐ BA ĐÒN BẨY, VÀ CÁI BẪY                                               ║
║     tồn kho 436 + DSO 347 = 782 (74% quãng đường), còn 277 phải cắt PPE  ║
║     ⚠️ NHƯNG tồn kho giảm → TIỀN TĂNG → TỔNG TÀI SẢN KHÔNG ĐỔI.          ║
║        vòng quay 1,67 ĐỨNG YÊN. Chỉ tăng khi tiền RA KHỎI BẢNG.          ║
║        (quick ratio 1,26 → 1,63 thì đổi ngay — bài 8 mục 8)              ║
║     Dùng 782 trả nợ:  ROA 4,78% → 6,69%, nợ/vốn chủ 1,11 → 0,80          ║
║     Bài 8 phải ĐI THUÊ, đắt thêm 22/năm. Chương 23: MIỄN PHÍ.            ║
║                                                                          ║
║  ⭐ DUPONT ĐỨNG TRƯỚC ENRON — trả lời bài 8                              ║
║     ① 2,854% KHÔNG ĐỔI   ② 1,6732 → 3,3471   ROA 4,78% → 9,55%           ║
║     DuPont nói ĐÚNG: toàn bộ mức tăng đến từ vế TÀI SẢN.                 ║
║     ⚠️ Sai ở CÁI TÊN: vế đó gọi là "hiệu suất", mà tài sản chỉ           ║
║        ĐI CHỖ KHÁC. Câu hỏi tiếp: CO LẠI hay DI CHUYỂN?                  ║
║        Không tỷ lệ nào trả lời — chỉ có LCTT và THUYẾT MINH.             ║
║                                                                          ║
║  ⚠️ NĂM CHỖ SÁCH IN SAI (ch. 23):                                        ║
║     tr.163 DII mẫu số 6.765 → 6.756  ·  tr.164 DSO 54,5 → 54,4           ║
║     tr.165 "PDO" → DPO  ·  tr.162 "kế toán toán"                         ║
║     tr.162+165 trỏ "Phần VII" mà bản dịch in "PHẦN VI" (tr.192)          ║
║     CẢ PHẦN V: 7 lỗi NHÃN, 3 lỗi SỐ.                                     ║
║                                                                          ║
║  🇻🇳 VÒNG QUAY 1,67 vs 0,92 — nhưng PPE 3,90 vs 4,44 (VNM CAO HƠN)        ║
║     45% tài sản Vinamilk là TIỀN + ĐẦU TƯ NGẮN HẠN.                      ║
║     Bỏ ra khỏi mẫu số: 1,70 vs 1,67 — GẦN NHƯ BẰNG NHAU.                 ║
║     DuPont: 5,79 lần (biên) × 0,55 lần (vòng quay) = 3,19 lần (ROA)      ║
║     → toàn bộ lợi thế ở MỘT số hạng, số hạng kia KÉO NGƯỢC LẠI.          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần V — Tỷ lệ: tìm hiểu ý nghĩa thật sự của các con số**
    - Ch. 23 *Các tỷ lệ thể hiện hiệu suất hoạt động*, PDF tr. 162–168
      — ⭐ *"quản lý bảng cân đối kế toán"* và *"khoản tiền đông cứng"* (tr. 162); **DII** và **tốc độ luân
      chuyển tồn kho**, ⚠️ mẫu số in 6.765, quy ước 360 ngày, ⭐ **Target 6,5 vs Wal-Mart 8,1** (tr. 163);
      **DSO**, ⚠️ in 54,5, bốn nguyên nhân DSO cao, **Sunbeam** (tr. 164); *"con số bình quân được điều
      chỉnh"*, **DPO** và ⚠️ *"PDO"* (tr. 165); DPO làm nhà cung cấp phiền lòng, **tốc độ thay thế PPE**
      (tr. 166); ⭐ *"các yếu tố khác không đổi"* và **thuê tài sản** (tr. 166–167); ⭐ **thưởng theo tỷ
      lệ** và **vòng quay tổng tài sản** (tr. 167); câu kết *"tầng bậc tiếp theo"* (tr. 168)
    - **Hộp công cụ Phần V**, PDF tr. 168–170
      — *"Tỷ lệ nào quan trọng nhất với công ty bạn?"* và **Setpoint** (tr. 168); *"Sức mạnh của con số
      phần trăm doanh thu"* (tr. 169); ⭐ *"Mối quan hệ tỷ lệ"* (tr. 169) — **phân rã DuPont** và **hai cách bật nhảy
      qua vòng** (tr. 170)
  - Ch. 22 *Các hệ số thanh toán*, PDF tr. 159–161 — hai hệ số thanh toán, nhắc ở
    [mục 7](#7-ba-đòn-bẩy-của-sách-đo-bằng-số)
  - **PHẦN VI *Ứng dụng trí tuệ tài chính vào thực tế quản lý vốn lưu động***, trang tiêu đề PDF tr. 192 —
    dùng để đối chiếu lỗi tham chiếu ⑤ ở [mục 10](#10--chỗ-sách-in-sai-trong-chương-23)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mọi mục
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 9](#9--hộp-công-cụ-phần-v--tỷ-lệ-riêng-và-phần-trăm-doanh-thu) và
  [mục 11](#11--đối-chiếu-việt-nam--hai-đường-đến-roa).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py`](../thuc_hanh/bai-09-ty-le-hieu-suat-va-dupont.py):
  - tốc độ luân chuyển tồn kho tính bằng $360/\text{DII}$ **bằng đúng** COGS/tồn kho — chốt bằng `assert`;
  - đổi 360 → 365 làm **mọi** tỷ lệ ngày nở ra **đúng** hệ số $365/360$ — chốt bằng `assert`;
  - chạy tốc độ Wal-Mart giải phóng lượng tiền **lớn hơn** lợi nhuận thuần cả năm — chốt bằng `assert`;
  - thuê đi **đúng một nửa** PPE làm tốc độ thay thế PPE **gấp đúng hai lần** — chốt bằng `assert`;
  - đồng nhất thức DuPont đúng ở **cả bốn** kịch bản (công ty mẫu, sau tái cấu trúc, sau bút toán Enron,
    Vinamilk) — chốt bằng `assert`;
  - giảm tồn kho + thu tiền **không đổi** tổng tài sản ngắn hạn — chốt bằng `assert`;
  - lượng tiền hai đòn bẩy giải phóng **lớn hơn** 770 triệu mà bài 8 cần để hạ nợ/vốn chủ xuống 0,80 —
    chốt bằng `assert`;
  - sau khi trả nợ, ROA **vượt** mục tiêu 6% và **cả hai** số hạng DuPont cùng tăng — chốt bằng `assert`;
  - DII = 74,2 **chỉ** khớp với mẫu số 6.756, **không** khớp với 6.765 như sách in — chốt bằng `assert`;
  - vòng quay **tài sản vận hành** của hai doanh nghiệp chênh **dưới 5%** — chốt bằng `assert`;
  - tỷ số biên × tỷ số vòng quay = **đúng** tỷ số ROA, với tỷ số vòng quay **nhỏ hơn 1** — chốt bằng
    `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** mục tiêu ROA 6% ở mục 6; mục tiêu DSO 40 ngày và
  toàn bộ kịch bản trả nợ ở mục 7 *(sách chỉ liệt kê ba đòn bẩy bằng lời)*; mức đẩy tài sản 2.597 ở mục 8
  *(kế thừa từ bài 8)*; khái niệm **tài sản vận hành** và cách bỏ tiền + đầu tư ngắn hạn ra khỏi mẫu số ở
  mục 11. Mọi con số **của sách** đều được trích kèm mốc `ch. N · PDF tr. M`.

---

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| 3 | [Chi phí và các tầng lợi nhuận](bai_03_chi_phi_va_cac_tang_loi_nhuan.md) | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| **9** | **Tỷ lệ hiệu suất và phân rã DuPont** ← *bạn đang ở đây* | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
