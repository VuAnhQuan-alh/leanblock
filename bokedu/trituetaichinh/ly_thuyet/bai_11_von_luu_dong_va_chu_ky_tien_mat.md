# Bài 11 — Vốn lưu động và chu kỳ tiền mặt

> [!info] Về bài này
> Bài học dựng từ **Phần VII — Ứng dụng trí tuệ tài chính vào thực tế quản lý vốn lưu động**: chương 26
> *Phép ảo thuật quản lý bảng cân đối kế toán* (PDF tr. 193–196), chương 27 *Các đòn bẩy trên bảng cân đối
> kế toán* (PDF tr. 197–202), chương 28 *Tập trung chuyển đổi tiền mặt* (PDF tr. 203–207), và hộp công cụ
> (PDF tr. 207–208).
>
> ⭐ **Vòng 1, dùng được ngay.** [Bài 9](bai_09_ty_le_hieu_suat_va_dupont.md) đo **ba tỷ lệ ngày riêng lẻ**.
> Phần này cộng cả ba thành **một con số** — chu kỳ chuyển đổi tiền mặt — rồi đổi nó ra **tiền**.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).
>
> **Cần đọc trước:** [Bài 4](bai_04_bang_can_doi_ke_toan.md) *(phải thu là tài sản, phải trả là nợ — mục
> 2 dưới đây phụ thuộc vào việc bạn nắm chắc điều này)* · [Bài 9](bai_09_ty_le_hieu_suat_va_dupont.md)
> *(DSO, DII, DPO và cái bẫy mẫu số)*.
> ⚙️ **Code:** [`thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py`](../thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py)
> — kiểm lại từng con số của ch. 26–28 *(có **năm** chỗ sách in sai)*, và tìm ra **công thức đóng** cho độ
> lệch của công thức tắt mà sách dùng.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vốn lưu động — "phép ảo thuật" và ba tài khoản bạn chạm được](#1-vốn-lưu-động--phép-ảo-thuật-và-ba-tài-khoản-bạn-chạm-được)
- [2. Định nghĩa vốn lưu động — sách in ba câu, hai câu đảo ngược](#2-định-nghĩa-vốn-lưu-động--sách-in-ba-câu-hai-câu-đảo-ngược)
- [3. Chu kỳ sản xuất — vốn lưu động đổi dạng, số lượng không đổi](#3-chu-kỳ-sản-xuất--vốn-lưu-động-đổi-dạng-số-lượng-không-đổi)
- [4. Ba đòn bẩy — và chúng không bằng nhau](#4-ba-đòn-bẩy--và-chúng-không-bằng-nhau)
- [5. "2/10 net 30" — giá thật của chiết khấu thanh toán sớm](#5-210-net-30--giá-thật-của-chiết-khấu-thanh-toán-sớm)
- [6. Quản lý tồn kho — ai chạm vào nó, và Tyco](#6-quản-lý-tồn-kho--ai-chạm-vào-nó-và-tyco)
- [7. DPO — nơi tài chính gặp triết lý, quy ra tiền](#7-dpo--nơi-tài-chính-gặp-triết-lý-quy-ra-tiền)
- [8. Chu kỳ chuyển đổi tiền mặt — và ba con số "vốn lưu động" khác nhau](#8-chu-kỳ-chuyển-đổi-tiền-mặt--và-ba-con-số-vốn-lưu-động-khác-nhau)
- [9. Công thức tắt của sách lệch ở đâu — và lệch đúng bao nhiêu](#9-công-thức-tắt-của-sách-lệch-ở-đâu--và-lệch-đúng-bao-nhiêu)
- [10. Hộp công cụ — kỳ thu tiền, thứ DSO giấu đi](#10-hộp-công-cụ--kỳ-thu-tiền-thứ-dso-giấu-đi)
- [11. Vinamilk — chỉ báo của sách báo động, và công thức tắt lệch ngược chiều](#11-vinamilk--chỉ-báo-của-sách-báo-động-và-công-thức-tắt-lệch-ngược-chiều)
- [12. Tự thử](#12-tự-thử)
- [13. Từ điển thuật ngữ](#13-từ-điển-thuật-ngữ)
- [14. Câu hỏi tự kiểm tra](#14-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vốn lưu động — "phép ảo thuật" và ba tài khoản bạn chạm được

Sách mở phần này bằng một lời hứa rất to, và nó đúng nghĩa đen:

> [!quote]
> *"Quản lý bảng cân đối kế toán một cách khôn ngoan cũng giống như thực hiện **một phép ảo thuật tài
> chính**. Nó cho phép doanh nghiệp **cải thiện hiệu quả hoạt động, mà không cần thúc đẩy doanh thu hay cắt
> giảm chi phí**."* — ch. 26 · PDF tr. 193

Đó là **cùng một luận điểm** mà [bài 9 mục 7](bai_09_ty_le_hieu_suat_va_dupont.md#7-ba-đòn-bẩy-của-sách-đo-bằng-số)
đã đo bằng số: hai đòn bẩy "không đau đớn" gộp **782 triệu** mà không bán thêm một món hàng nào. Phần này
**đặt tên** cho nó.

⭐ Và sách khoanh vùng **rất hẹp**: trong cả bảng cân đối, người ngoài tài chính chỉ chạm được vào **ba tài
khoản**.

> [!quote]
> *"Ba tài khoản vốn lưu động mà các nhà quản lý **không làm về tài chính** thật sự tác động đến là **khoản
> phải thu, hàng tồn kho**, và ở **mức độ hạn hẹp hơn** là các khoản phải trả."* — ch. 26 · PDF tr. 195

| tài khoản | giá trị | ai chạm được |
| --- | ---: | --- |
| Khoản phải thu | 1.312 | bán hàng, CSKH, tín dụng, giao nhận |
| Hàng tồn kho | 1.270 | bán hàng, kỹ sư, sản xuất, kho vận |
| Khoản phải trả | 1.022 | gần như chỉ phòng tài chính |
| **→ VỐN LƯU ĐỘNG VẬN HÀNH** | **1.560** | *phải thu + tồn kho − phải trả* |

⭐ **1.560 triệu — bằng 6,29 lần lợi nhuận thuần cả năm.** Đó là số tiền doanh nghiệp phải **bỏ ra trước**
và chờ thu về, mỗi năm, **chỉ để vận hành**. Sách gọi đây là *"đấu trường chính để phát triển và áp dụng trí
tuệ tài chính"* — vì nó là phần bảng cân đối mà người ngoài phòng tài chính **thật sự điều khiển được**.

---

## 2. Định nghĩa vốn lưu động — sách in ba câu, hai câu đảo ngược

Trang 193–194 đưa **ba phát biểu** về cùng một khái niệm, cách nhau chưa tới một trang. Đọc liên tiếp
thì chúng **mâu thuẫn nhau**.

**① Định nghĩa bằng lời:**

> [!quote]
> *"Vốn lưu động là hạng mục nguồn lực, bao gồm tiền mặt, hàng tồn kho, và các khoản phải thu **trừ đi bất
> kỳ thứ gì mà doanh nghiệp SỞ HỮU trong ngắn hạn**."* — ch. 26 · PDF tr. 193

> [!warning] Sở hữu?
> Trừ đi thứ mình *sở hữu* thì ra số âm. Phải là **NỢ** — những gì doanh nghiệp **nợ** trong
> ngắn hạn. **Một chữ, đảo ngược cả định nghĩa.**

**② Công thức, ngay dòng sau:**

> [!quote]
> *"Vốn lưu động = tài sản ngắn hạn – nợ ngắn hạn"*

✓ **Đúng.** Và chính câu này chứng minh câu ① sai.

**③ Diễn giải công thức, ngay đoạn sau nữa:**

> [!quote]
> *"tài sản ngắn hạn bao gồm các khoản mục như tiền mặt, **các khoản phải trả** và hàng tồn kho. Nợ ngắn
> hạn bao gồm **các khoản phải thu** và các nghĩa vụ ngắn hạn khác."* — ch. 26 · PDF tr. 194

> [!warning] Đảo ngược hoàn toàn.
> Phải thu là **tài sản** (khách nợ mình), phải trả là **nợ** (mình nợ nhà cung
> cấp). [Bài 4](bai_04_bang_can_doi_ke_toan.md) đã dùng cả một mục cho việc này.

**Kiểm bằng chính số liệu.** Đọc câu ③ theo đúng chữ *(một cách đọc minh hoạ — bỏ qua "các nghĩa vụ ngắn
hạn khác")*:

| cách tính | kết quả |
| --- | ---: |
| ② đúng — TSNH − NNH | **1.576** |
| ③ theo chữ: *(tiền + phải TRẢ + tồn kho) − phải THU* | **1.063** |
| **chênh** | **513** |

⭐ Lệch **513 triệu — 33% vốn lưu động thật**. Không phải lỗi làm tròn. Đây là **lỗi khái niệm**: nó đẩy
người đọc gọi **tên sai** cho hai dòng lớn nhất của bảng cân đối ngắn hạn — cùng một lớp với bảy chỗ ở
Phần V ([bài 9 mục 10](bai_09_ty_le_hieu_suat_va_dupont.md#10-chỗ-sách-in-sai-trong-chương-23))
*(chốt bằng `assert`)*.

⭐ **Ba câu, ba trạng thái:** ① sai **một chữ** · ② **đúng** · ③ sai **hai dòng**. Câu đúng nằm **ở giữa**
hai câu sai — nên người đọc cẩn thận vẫn tìm được đường ra. Đó là lý do cuốn sách này vẫn dùng được: nó
**tự mâu thuẫn** chứ không sai **nhất quán**.

---

## 3. Chu kỳ sản xuất — vốn lưu động đổi dạng, số lượng không đổi

```
   tiền mặt  →  tồn kho NVL thô  →  sản phẩm đang xử lý  →  thành phẩm
         ↑                                                      ↓
         └──────────  khoản phải thu  ←──────  bán hàng  ───────┘
```

> [!quote]
> *"Xuyên suốt chu kỳ này, vốn lưu động **liên tục thay đổi dạng thức. Nhưng số lượng vẫn giữ nguyên** cho
> đến khi hệ thống có thêm tiền mặt — từ, chẳng hạn như, vay nợ hoặc đầu tư vốn chủ sở hữu."*
> — ch. 26 · PDF tr. 194

⭐ Câu *"số lượng vẫn giữ nguyên"* là thứ dễ bỏ qua nhất và quan trọng nhất. Nó có nghĩa là: **bạn không thể
tạo ra vốn lưu động bằng cách chạy vòng nhanh hơn.** Chạy nhanh hơn làm giảm **số vốn lưu động cần thiết** —
đó là chuyện khác hẳn, và là toàn bộ nội dung [mục 8](#8-chu-kỳ-chuyển-đổi-tiền-mặt--và-ba-con-số-vốn-lưu-động-khác-nhau).

> [!note] Chu kỳ dịch vụ đơn giản hơn nhưng cùng hình dạng.
> Sách lấy chính công ty của tác giả — Viện Business
> Literacy: *"Chu kỳ hoạt động là toàn bộ thời gian từ khâu phát triển tài liệu đào tạo ban đầu, đến hoàn tất
> các khoá đào tạo, và cuối cùng là thu hoá đơn."* Kết luận: *"cách tốt nhất để làm ra tiền trong ngành dịch
> vụ là **cung cấp dịch vụ nhanh chóng, và sau đó thu công nợ nhanh hết sức có thể**."*

⭐ Và sách hạ thêm một câu rào mà cả Phần I đến V **không** hạ được:

> [!quote]
> *"Trước khi bắt đầu, chúng ta rất nên đặt lại câu hỏi **có bao nhiêu "nghệ thuật"** tham gia vào những
> phép tính này. Trong trường hợp này, câu trả lời hay nhất có lẽ là **"một chút"**. Tiền mặt là **một số
> cứng**, nó không dễ điều khiển. Các khoản phải thu và khoản phải trả cũng **tương đối cứng**. Hàng tồn kho
> thì **mềm dẻo hơn**."* — ch. 26 · PDF tr. 196

Đó là **lần duy nhất** trong cả cuốn sách các tác giả nói *"chỗ này ít nghệ thuật thôi"*. Và nó đúng: ba
dòng này là thứ **gần tiền mặt nhất** trên bảng cân đối. Càng gần tiền mặt thì càng ít chỗ cho ước tính —
đúng mạch lập luận của [bài 6](bai_06_loi_nhuan_khac_tien_mat.md).

---

## 4. Ba đòn bẩy — và chúng không bằng nhau

Sách đưa đúng **ba con số** *"một ngày đáng giá bao nhiêu"*, ở ba chỗ khác nhau. Cả ba đều đúng:

| sách viết | kiểm lại | |
| --- | ---: | :---: |
| tr. 199 — *"một ngày doanh thu… **hơn 24 triệu** đô-la"* | 24,14 triệu | ✓ |
| tr. 202 — *"rút một ngày DII… **gần 19 triệu** đô-la"* | 18,77 triệu | ✓ |
| tr. 203 — *"tăng DPO một ngày… **khoảng 19 triệu** đô-la"* | 18,77 triệu | ✓ |

**Nhưng** sách xếp ba đòn bẩy cạnh nhau như thể chúng tương đương: *"giảm DSO, giảm tồn kho và tăng DPO"*
(tr. 207). **Chúng không tương đương.**

| đòn bẩy | một ngày đáng giá | so với DSO |
| --- | ---: | ---: |
| **DSO** — thu tiền về sớm 1 ngày | **24,14 triệu** | **1,00 lần** |
| DII — tồn kho bớt 1 ngày | 18,77 triệu | 0,78 lần |
| DPO — trả chậm thêm 1 ngày | 18,77 triệu | 0,78 lần |

⭐ **Một ngày DSO đáng giá bằng 1,29 ngày tồn kho hoặc phải trả.** Lý do thuần cơ học, đã gặp ở
[bài 9 mục 4](bai_09_ty_le_hieu_suat_va_dupont.md#4-dso-dpo--và-một-quy-ước-không-nhất-quán-ngay-trong-một-chương):
phải thu định giá theo **giá bán**, tồn kho và phải trả định giá theo **giá vốn**. Tỷ lệ chính là:

$$\frac{\text{doanh thu}}{\text{COGS}} = \frac{8.689}{6.756} = \frac{1}{1 - \text{biên lợi nhuận gộp}}
= \frac{1}{1 - 22{,}2\%} = \mathbf{1{,}29}$$

*(chốt bằng `assert`)*

> [!example] Hệ quả dùng được ngay:
> nếu phải chọn **một** chiến dịch và ba đòn bẩy khó ngang nhau, thì **đòn DSO
> trước**. Và **biên lợi nhuận gộp càng cao thì khoảng cách càng giãn ra** — ở một doanh nghiệp biên gộp 50%,
> một ngày DSO bằng **hai** ngày tồn kho.

---

## 5. "2/10 net 30" — giá thật của chiết khấu thanh toán sớm

> [!quote]
> *"Chẳng hạn, **'2/10 net 30'** có nghĩa là khách hàng sẽ được **chiết khấu 2%** nếu thanh toán hoá đơn
> trong vòng **10 ngày** và sẽ không được hưởng chiết khấu nếu họ đợi đúng **30 ngày**… Đôi khi khoản chiết
> khấu 1–2% có thể giúp một doanh nghiệp **đang chống đỡ với khó khăn** thu được các khoản phải thu và do
> đó giảm được DSO — nhưng tất nhiên, làm vậy tức là **doanh nghiệp đang ăn vào lợi nhuận của mình**."*
> — ch. 27 · PDF tr. 198–199

**Sách dừng ở "ăn vào lợi nhuận". Ăn bao nhiêu?** Đổi ra lãi suất năm:

| điều khoản | chiết khấu | sớm (ngày) | lãi/kỳ | **lãi năm đơn** | lãi năm kép |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1/10 net 30 | 1% | 20 | 1,01% | **18,2%** | 19,8% |
| **2/10 net 30** | 2% | 20 | 2,04% | **36,7%** | 43,9% |
| 2/20 net 30 | 2% | 10 | 2,04% | **73,5%** | 106,9% |

⭐ **"2/10 net 30" = cho khách vay tiền với lãi suất 36,7%/năm** *(tính đơn)*. Khoản 2% ấy **không phải một
khoản giảm giá — nó là một khoản vay**, và là khoản vay **đắt nhất** trong bảng cân đối.

> [!warning]
> So với **lãi suất vay thật** của chính công ty mẫu — 191/1.714 = **11,1%/năm**
> ([bài 8 mục 7](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md#7-hai-tỷ-lệ-đòn-bẩy-và-giá-của-việc-làm-đẹp-chúng)):
> chiết khấu 2/10 **đắt gấp 3,3 lần** đi vay ngân hàng *(chốt bằng `assert`)*.

Muốn rút ngắn DSO 20 ngày thì **vay rồi trả lãi rẻ hơn nhiều**. Chiết khấu chỉ đáng đồng tiền khi **ngân
hàng không cho vay** — tức là đúng lúc doanh nghiệp *"đang chống đỡ với khó khăn"*, y như sách mô tả.

> [!example]
> Đọc theo kiểu khác: 2% doanh thu trên biên lợi nhuận gộp 22,2% là **9,0% lợi nhuận gộp** biến mất. Đó mới
> là nghĩa đen của *"ăn vào lợi nhuận của mình"*.

---

## 6. Quản lý tồn kho — ai chạm vào nó, và Tyco

Sách làm một việc không chương nào khác làm: **liệt kê từng bộ phận** và chỉ ra họ đẩy tồn kho lên bằng cách
nào.

| bộ phận | hành vi hợp lý của họ | hậu quả lên tồn kho |
| --- | --- | --- |
| Bán hàng | hứa đáp ứng mọi yêu cầu riêng *("Có nó như cách của bạn")* | mọi tuỳ chọn = thêm tồn kho |
| Kỹ sư | cải tiến phiên bản 2.54 → 2.55 | *"sự phát triển ồ ạt của các phiên bản"* |
| Sản xuất | giảm **chi phí đơn vị** | chạy máy khi cầu xuống = tồn kho |
| Nhà xưởng | sơ đồ quy hoạch, thời gian đổi máy | luồng chạy kém = đệm tồn kho |

⭐ Câu nặng nhất của chương 27 nhắm vào bộ phận sản xuất:

> [!quote]
> *"Khi hoạt động kinh doanh lắng xuống, họ **vẫn tiếp tục sản xuất hàng loạt** để duy trì hiệu quả nhà
> máy… Họ được **đào luyện** làm vậy, được **yêu cầu** làm vậy, và được **trả lương (cộng thêm thưởng)** để
> đạt được như vậy… **Đến chỗ làm và đọc một cuốn sách xem chừng còn hữu ích hơn** là tạo ra một sản phẩm
> chưa sẵn sàng để bán."* — ch. 27 · PDF tr. 201–202

Đó là **cùng một cơ chế** mà [bài 9 mục 5](bai_09_ty_le_hieu_suat_va_dupont.md#5-tốc-độ-thay-thế-ppe--tỷ-lệ-có-tiền-thưởng-gắn-vào)
đã chỉ ra ở tốc độ thay thế PPE: **một tỷ lệ có tiền thưởng gắn vào thì nó sẽ được tối ưu**, kể cả khi làm
hỏng thứ khác.

### Tyco — chỗ sách ước lượng thấp hơn thực tế

> [!quote]
> *"ngày tồn kho bắt đầu theo vòng xoắn ốc vượt ra khỏi tầm kiểm soát, khiến thời gian ở **một số khu vực**
> tăng **hơn 10 ngày**. Với một công ty đa quốc gia có doanh thu **hơn 30 tỷ đô-la**, quy mô tăng như vậy
> có thể **vắt kiệt hàng triệu đô-la** tiền mặt!"* — ch. 28 · PDF tr. 207

Đo thử, **giả định tỷ lệ giá vốn bằng công ty mẫu (77,8%)** — *giả định của bài học, sách không cho số*:

> [!note]
> COGS ≈ 23,3 tỷ → một ngày = **64,8 triệu** đô-la
> 10 ngày tồn kho = **648 triệu** đô-la

⭐ **648 triệu — gần hai phần ba tỷ đô-la, không phải "hàng triệu".** Sách dùng đúng đơn vị nhưng nhỏ hơn
thực tế **hai bậc độ lớn**.

> [!warning] Công bằng với sách:
> sách viết *"ở **một số khu vực**"*, không phải toàn tập đoàn. Nếu chỉ **10%**
> doanh thu bị ảnh hưởng thì con số về **65 triệu** — đúng là *"hàng chục triệu"*. Con số 648 là **cận trên**,
> nếu nó lan ra cả tập đoàn.

---

## 7. DPO — nơi tài chính gặp triết lý, quy ra tiền

> [!quote]
> *"Khoản phải trả là **một con số rất khó dàn xếp ổn thoả**. Đó là nơi mà **tài chính gặp gỡ triết lý**."*
> — ch. 28 · PDF tr. 203

### Và ngay câu tiếp theo sách in sai

> [!quote]
> sách in: *"Chỉ cân nhắc tài chính không thôi sẽ khuyến khích nhà quản lý đẩy **kỳ thu tiền bình quân
> (DSO)** lên mức cao nhất có thể, từ đó bảo tồn được tiền mặt của doanh nghiệp."*

> [!warning]
> Phải là **DPO**. Đẩy DSO lên cao là **giữ tiền ở chỗ khách hàng** — ngược hẳn. Và **chính câu ngay sau
> đó** dùng đúng DPO: *"việc tăng DPO lên một ngày giúp tăng số dư tiền mặt… khoảng 19 triệu đô-la"*.

### Câu chuyện Setpoint, và giá của một nguyên tắc

Hai kỹ sư sáng lập Setpoint từng làm ở một nơi trả chậm **hơn 100 ngày**:

> [!quote]
> *"khi họ gửi bản thiết kế đi chế tạo, **không ai làm chi tiết cho họ**… Và các kỹ sư **phải trở thành
> những kẻ đàm phán** chỉ để dự án của mình có thể chạy! Khi bắt đầu mở công ty riêng, **họ thề** sẽ không
> bao giờ đẩy các kỹ sư của mình vào tình thế tương tự."* — ch. 28 · PDF tr. 203

Setpoint **không bao giờ** để hoá đơn vượt quá **30 ngày**. Sách thừa nhận cái giá — **bằng lời**: *"triết
lý này đặt các chướng ngại vật lên dòng lưu chuyển tiền"*. Quy ra tiền trên công ty mẫu:

| | |
| --- | ---: |
| DPO hiện tại | 54,5 ngày |
| DPO kiểu Setpoint | 30,0 ngày |
| → phải trả sớm hơn | 24,5 ngày |
| **→ tiền mặt phải bỏ ra** | **459 triệu** |

⭐ **459 triệu — bằng 1,85 lần lợi nhuận thuần cả năm** *(chốt bằng `assert`)*. Đó là **giá của một nguyên
tắc, tính bằng tiền mặt**. Sách kể câu chuyện này như một điều đáng khen — và nó **đáng khen** — nhưng nó
**không miễn phí**, và cuốn sách không đặt con số lên bàn.

> [!note] Sách cũng nêu ba lý do khác để không kéo DPO quá dài:
> nhà cung cấp phiền lòng và **báo giá cao hơn**;
> **điểm số Dun & Bradstreet** xây một phần trên lịch sử thanh toán; và *"một tổ chức luôn thanh toán chậm có
> thể thấy mình sẽ **gặp khó khăn khi vay nợ** về sau"*.

⭐ Và sách đưa một **chỉ báo ra quyết định** dùng được ngay:

> [!quote]
> *"nếu bạn để ý thấy DPO của công ty mình **đang tăng** — và cụ thể nếu nó **đang cao hơn DSO**, có thể
> bạn cần đặt cho các chuyên gia tài chính của công ty **một vài câu hỏi**."* — ch. 28 · PDF tr. 204

Công ty mẫu: DPO 54,5 so với DSO 54,4 — chênh **0,1 ngày**. Có, nhưng không đáng kể.
[Mục 11](#11-vinamilk--chỉ-báo-của-sách-báo-động-và-công-thức-tắt-lệch-ngược-chiều) đem chính chỉ báo này
áp lên Vinamilk, và nó **báo động**.

---

## 8. Chu kỳ chuyển đổi tiền mặt — và ba con số "vốn lưu động" khác nhau

[Bài 9](bai_09_ty_le_hieu_suat_va_dupont.md) đo ba tỷ lệ ngày riêng lẻ. Chương 28 cộng chúng lại thành
**một**:

```
   mua NVL ──── trả tiền NVL ──────────── bán thành phẩm ──── thu tiền về
     │              │                          │                  │
     ├── kỳ thanh toán phải trả ──┤            │                  │
     ├──────────── kỳ tồn kho ────────────────┤                  │
                    ├────── CHU KỲ CHUYỂN ĐỔI TIỀN MẶT ──────────┤
                                               ├── kỳ thu công nợ ┤
```

$$\text{Chu kỳ chuyển đổi tiền mặt} = \text{DSO} + \text{DII} - \text{DPO}
= 54{,}4 + 74{,}2 - 54{,}5 = \mathbf{74{,}1}\ \text{ngày}$$

> [!warning] Sách in *"54 ngày + 74 ngày – 55 ngày = 73 ngày"
> * *(tr. 206)*. Ba số hạng đều bị làm tròn về số
> nguyên, và số 55 lấy từ **DPO** chứ không phải DSO. Dùng số của chính ch. 23: **74,1 ngày** *(chốt bằng `assert`)*.

> [!warning] Và một chỗ nữa ngay dưới công thức:
> *"hãy lấy thời gian thu tiền bình quân, cộng thời gian lưu kho,
> **trừ đi thời gian có thể thu tiền**"*. Vế cuối là **DPO** — thời gian được phép **TRẢ** tiền, không phải
> thu tiền. Lại một lần DSO/DPO bị lẫn.

Rồi sách đổi chu kỳ ra **tiền**: *"lấy tỷ lệ doanh thu theo ngày **nhân với** số ngày chuyển đổi tiền mặt"*.

| cách tính | kết quả *(triệu)* |
| --- | ---: |
| **sách in:** 73 × 24.136.000 | **1.762** |
| sửa số ngày: 74,1 × 24,136 triệu | **1.788** |
| **bảng cân đối:** TSNH − NNH | **1.576** |
| **vận hành:** phải thu + tồn kho − phải trả | **1.560** |

⭐ **Ba con số, đều được gọi là "vốn lưu động", cách nhau tới 15%:**

- **1.576** và **1.560** — hai cách đọc **bảng cân đối**, lệch **1,0%**. *(Chúng gần nhau vì tiền 83 + trả
  trước 85 gần bằng hạn mức tín dụng 100 + nợ đến hạn 52 — một **sự trùng hợp**, không phải quy luật.)*
- **1.788** — **công thức tắt của sách**, cao hơn **228 triệu**.

[Mục 9](#9-công-thức-tắt-của-sách-lệch-ở-đâu--và-lệch-đúng-bao-nhiêu) chỉ ra chênh lệch ấy đến từ đâu, và
nó có **một công thức đóng**.

---

## 9. Công thức tắt của sách lệch ở đâu — và lệch đúng bao nhiêu

Công thức của sách nhân **cả ba** số ngày với **doanh thu/ngày**. Nhưng ba số ngày ấy **không** được tính
trên cùng một mẫu số — đây là điều
[bài 9 mục 4](bai_09_ty_le_hieu_suat_va_dupont.md#4-dso-dpo--và-một-quy-ước-không-nhất-quán-ngay-trong-một-chương)
đã chỉ ra:

| số hạng | tính trên | số ngày | định giá **đúng** | là dòng nào trên BCĐKT |
| --- | ---: | ---: | ---: | --- |
| DSO | doanh thu/ngày | 54,4 | **1.312** | khoản phải thu |
| DII | **COGS**/ngày | 74,2 | **1.392** | tồn kho bình quân |
| DPO | **COGS**/ngày | 54,5 | **1.022** | khoản phải trả |

| | |
| --- | ---: |
| định giá **đúng** từng số hạng | 1.682,0 |
| công thức tắt của sách | 1.787,9 |
| **→ LỆCH** | **105,9** |

⭐ **Và độ lệch có một công thức đóng:**

$$\text{lệch} = (\text{DII} - \text{DPO}) \times \left(\frac{\text{doanh thu}}{\text{ngày}} - \frac{\text{COGS}}{\text{ngày}}\right)$$

$$= (74{,}17 - 54{,}46) \times (24{,}136 - 18{,}767) = 19{,}72 \times 5{,}369 = \mathbf{105{,}9}$$

Khớp đến từng chữ số *(chốt bằng `assert`)*.

⭐ **Đọc công thức đó thì ra hai điều kiện để công thức tắt đúng tuyệt đối:**

1. **DII = DPO** — tồn kho nằm trong kho đúng bằng thời gian mình nợ nhà cung cấp;
2. **biên lợi nhuận gộp = 0** — doanh thu/ngày bằng COGS/ngày.

Ngoài hai trường hợp đó, công thức tắt **luôn lệch**. Và **dấu** của độ lệch là dấu của $(\text{DII} -
\text{DPO})$: tồn kho lâu hơn nợ thì **đội lên**, ngắn hơn thì **đội xuống**.

> [!warning]
> Ở đây: DII 74,2 > DPO 54,5 → lệch **dương 106 triệu**, tức **6,3% đội lên**. Không lớn, và con số
> *"khoảng 1,8 tỷ"* của sách vẫn đúng về **độ lớn**. Nhưng **dấu lệch đổi chiều theo doanh nghiệp** —
> [mục 11](#11-vinamilk--chỉ-báo-của-sách-báo-động-và-công-thức-tắt-lệch-ngược-chiều) cho một trường hợp lệch
> **âm** và lệch **rất lớn**.

> [!example] Cách dùng cho đúng:
> công thức *chu kỳ × doanh thu/ngày* là **một công cụ ước lượng nhanh** để trả lời
> *"có bao nhiêu tiền đang bị giam trong vòng quay"*. Muốn con số **đúng** thì đọc thẳng từ bảng cân đối:
> **phải thu + tồn kho − phải trả**.

---

## 10. Hộp công cụ — kỳ thu tiền, thứ DSO giấu đi

> [!quote]
> *"**DSO không phải là thước đo duy nhất** cần dõi theo… theo định nghĩa, DSO là **con số bình quân**."*
> — hộp công cụ · PDF tr. 207

Sách dùng một ví dụ hai công ty. Dựng lại bằng số:

| | CÔNG TY A | CÔNG TY B |
| --- | ---: | ---: |
| tổng khoản phải thu | 2.000.000 | 2.000.000 |
| phần **quá 90 ngày** | **1.000.000** | **250.000** |
| **% quá 90 ngày** | **50,0%** | **12,5%** |
| phần còn lại thu trong | 10 ngày | 44,3 ngày |
| **DSO** | **50 ngày** | **50 ngày** |

⭐ **Cùng một DSO 50 ngày.** Nhưng công ty A có **50%** công nợ quá 90 ngày, công ty B chỉ **12,5%**
*(chốt bằng `assert`)*.

> [!quote]
> *"Con số này **có vẻ không tệ**, nhưng thực tế là công ty bạn có thể **đang gặp rắc rối lớn**, bởi vì
> **một nửa khách hàng** dường như không thanh toán đúng hẹn."* — hộp công cụ · PDF tr. 207–208

⭐ Đó là lý do phải đọc **bảng phân tuổi** chứ không chỉ đọc DSO: *"tổng khoản phải thu **dưới 30 ngày**,
tổng khoản phải thu **từ 30 đến 60 ngày**, v.v…"*. **Một tỷ lệ là một con số. Một bảng phân tuổi là một
phân bố.** [Bài 9 mục 4](bai_09_ty_le_hieu_suat_va_dupont.md#4-dso-dpo--và-một-quy-ước-không-nhất-quán-ngay-trong-một-chương)
đã nêu đúng cảnh báo này từ phía ch. 23; đây là chỗ sách đưa ra **công cụ để vá**.

> [!example] Con số đáng theo dõi hằng tháng, và nó không có trong sách: tỷ lệ phải thu quá 90 ngày.
> Nó bắt được
> cái mà DSO làm nhoè đi, và là thứ **đầu tiên** một ngân hàng hỏi khi thẩm định khoản vay vốn lưu động.

---

## 11. Vinamilk — chỉ báo của sách báo động, và công thức tắt lệch ngược chiều

| | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| --- | ---: | ---: |
| Kỳ thu tiền (DSO) | 54,4 ngày | 43,7 ngày |
| Ngày tồn kho (DII) | 74,2 ngày | 56,4 ngày |
| Kỳ thanh toán (DPO) | 54,5 ngày | **78,2 ngày** |
| **Chu kỳ chuyển đổi tiền mặt** | **74,1 ngày** | **21,8 ngày** |

⭐ **74,1 ngày so với 21,8 ngày — ngắn hơn 52 ngày.** Vinamilk chỉ giam tiền trong vòng quay bằng **29%** so
với công ty mẫu — chưa tới một phần ba.

### Chỉ báo của sách báo động ở Vinamilk

> [!quote]
> *"nếu bạn để ý thấy DPO của công ty mình đang tăng — và cụ thể **nếu nó đang cao hơn DSO**, có thể bạn cần
> đặt… một vài câu hỏi."*

| | DPO | DSO | chênh |
| --- | ---: | ---: | ---: |
| Công ty mẫu | 54,5 | 54,4 | 0,1 ngày |
| **Vinamilk** | **78,2** | **43,7** | **34,5 NGÀY** |

> [!warning] Nhưng đọc cho đúng.
> Sách viết chỉ báo này cho một doanh nghiệp **đang gặp khó** — DPO tăng là triệu
> chứng thiếu tiền. Ở Vinamilk thì ngược lại:

- hệ số thanh toán lãi vay **30 lần** ([bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md)) — không hề
  thiếu tiền;
- **45% tài sản là tiền và tiền gửi** ([bài 9](bai_09_ty_le_hieu_suat_va_dupont.md)).

DPO 78 ngày ở đây **không phải triệu chứng túi nghèo — nó là sức mạnh đàm phán** với nhà cung cấp. Sách cũng
nói đúng điều đó ở mặt kia: *"thực tế thì doanh nghiệp có **bao nhiêu đòn bẩy** với nhà cung cấp?"* **Chỉ
báo của sách đúng — nó bảo bạn đặt câu hỏi, không bảo bạn kết luận.**

### Và công thức tắt của mục 9 lệch **ngược chiều** ở Vinamilk

| | Công ty mẫu *(triệu USD)* | Vinamilk *(triệu VND)* |
| --- | ---: | ---: |
| **DII − DPO** | **+19,7 ngày** | **−21,9 ngày** |
| công thức tắt *(chu kỳ × DT/ngày)* | 1.788 | 3.187.634 |
| định giá đúng từng số hạng | 1.682 | 4.108.723 |
| **→ LỆCH** | **+106** | **−921.089** |
| **→ LỆCH (%)** | **+6,3%** | **−22,4%** |

⭐ Công ty mẫu: DII > DPO → công thức tắt **đội lên 6,3%**.
Vinamilk: DII < DPO → công thức tắt **đội xuống 22%** *(chốt bằng `assert` cả hai chiều)*.

**Cùng một công thức, hai chiều lệch ngược nhau.** Và độ lệch của Vinamilk lớn hơn nhiều vì **biên lợi nhuận
gộp của nó cao hơn** (28,8% so với 22,2%), làm thừa số $(\text{DT/ngày} - \text{COGS/ngày})$ giãn ra.

📌 **Ba lưu ý khi tính chu kỳ chuyển đổi tiền mặt trên báo cáo Việt Nam:**

- **DSO của Vinamilk tính từ *"phải thu khách hàng VÀ phải thu khác"*** vì bản IFRS gộp chung một dòng — nên
  nó **hơi cao** so với DSO thuần thương mại.
- **VAS / Thông tư 200 tách *"phải thu ngắn hạn của khách hàng"* riêng** — dùng dòng đó thì con số thấp hơn,
  và so với đối thủ mới đúng.
- **DPO nên tính trên *"phải trả người bán"*** chứ không phải tổng phải trả. Ở đây mẫu số gộp cả phải trả
  khác, nên **DPO 78 ngày là cận trên**.

---

## 12. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py`](../thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py)
rồi chạy lại. Không có lời giải.

1. **Vốn lưu động âm.** Ở mục 1, tìm mức phải trả làm vốn lưu động vận hành bằng **0**. Doanh nghiệp nào
   trong đời thực chạy được như thế, và vì sao? *(gợi ý: khách trả trước, nhà cung cấp trả sau)*

2. **Đọc câu ③ đầy đủ.** Ở mục 2, thêm cả *"các nghĩa vụ ngắn hạn khác"* vào vế nợ khi đọc câu ③ theo chữ.
   Con số lệch bao nhiêu? Kết luận có đổi không?

3. **Biên gộp và tỷ giá đòn bẩy.** Ở mục 4, vẽ quan hệ giữa **biên lợi nhuận gộp** và **tỷ số một ngày DSO /
   một ngày tồn kho**. Ở biên gộp bao nhiêu thì tỷ số đạt **2,0**? Ngành nào có biên gộp như thế?

4. **Ngưỡng chiết khấu.** Ở mục 5, tìm mức chiết khấu làm *"x/10 net 30"* có lãi suất năm **bằng đúng**
   11,1% — lãi suất vay của công ty mẫu. Con số đó có thực tế không?

5. **Net 60.** Vẫn mục 5, đổi điều khoản thành *"2/10 net 60"* (sớm 50 ngày). Lãi suất năm còn bao nhiêu?
   Vì sao **kéo dài kỳ hạn chuẩn** lại làm chiết khấu **rẻ đi**?

6. **Tyco ở biên gộp khác.** Ở mục 6, đổi tỷ lệ giá vốn từ 77,8% xuống **60%**. Con số 10 ngày tồn kho đổi
   bao nhiêu? Giả định nào bạn thấy hợp lý hơn cho một tập đoàn công nghiệp?

7. **Giá của Setpoint ở DPO khác.** Ở mục 7, tính giá của chính sách 30 ngày nếu DPO hiện tại là **90 ngày**
   thay vì 54,5. Ở mức nào thì nguyên tắc trở nên **không kham nổi**?

8. **Chu kỳ bằng 0.** Ở mục 8, tìm mức DPO làm chu kỳ chuyển đổi tiền mặt bằng **0**. Nó có khả thi không,
   và điều đó nói gì về mô hình kinh doanh cần có?

9. **Khi công thức tắt đúng.** Ở mục 9, đặt DII = DPO rồi chạy lại. Độ lệch bằng bao nhiêu? Dựng thêm một
   trường hợp biên gộp = 0 và kiểm điều kiện thứ hai.

10. **Dấu lệch.** Vẫn mục 9, tìm mức DII làm độ lệch **đổi dấu**. Nó bằng đúng cái gì? Vì sao?

11. **Bảng phân tuổi.** Ở mục 10, dựng một công ty thứ ba có DSO **50 ngày** nhưng **0%** công nợ quá 90
    ngày. Phần còn lại phải thu trong bao nhiêu ngày? Điều đó có hợp lý không?

12. **Vinamilk theo VAS.** Ở mục 11, giả sử "phải thu khách hàng" chỉ bằng **60%** con số IFRS đang dùng.
    DSO, chu kỳ tiền mặt và độ lệch công thức tắt đổi thế nào? Chiều lệch có đảo không?

---

## 13. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Vốn lưu động | working capital | tài sản ngắn hạn − nợ ngắn hạn |
| 💼 Vốn lưu động vận hành | operating working capital | phải thu + tồn kho − phải trả — **không có trong sách** |
| Quản lý bảng cân đối kế toán | balance sheet management | *"một phép ảo thuật tài chính"* — cải thiện mà không đổi doanh thu/chi phí |
| Chu kỳ chuyển đổi tiền mặt | cash conversion cycle | DSO + DII − DPO. Tiền bị giam bao nhiêu ngày |
| Chu kỳ sản xuất / hoạt động | operating cycle | tiền → NVL → sản phẩm → phải thu → tiền |
| Kỳ thu tiền bình quân | days sales outstanding (DSO) | phải thu / **doanh thu** mỗi ngày |
| Ngày tồn kho | days in inventory (DII) | tồn kho / **COGS** mỗi ngày |
| Kỳ thanh toán bình quân | days payable outstanding (DPO) | phải trả / **COGS** mỗi ngày |
| 2/10 net 30 | 2/10 net 30 | chiết khấu 2% nếu trả trong 10 ngày — **36,7%/năm** |
| Bảng phân tuổi công nợ | AR aging report | phân bố phải thu theo số ngày — thứ DSO **giấu đi** |
| Sản xuất tinh gọn | lean manufacturing | *"những từ rất kêu"* mà sách chỉ nhắc tên |
| Tồn kho đúng thời điểm | just-in-time (JIT) | *nt.* |
| Số lượng đơn hàng hợp lý | economic order quantity (EOQ) | *nt.* |
| Điểm số Dun & Bradstreet | D&B rating | xếp hạng dựa một phần trên **lịch sử thanh toán** |
| 💼 Tỷ lệ phải thu quá 90 ngày | AR > 90 days | thước đo bổ sung cho DSO — **không có trong sách** |

---

## 14. Câu hỏi tự kiểm tra

1. Sách gọi quản lý bảng cân đối là gì? Vì sao đó là "ảo thuật"? (mục 1)
2. **Ba** tài khoản nào người ngoài phòng tài chính thật sự chạm được? (mục 1)
3. Vốn lưu động vận hành của công ty mẫu bằng mấy lần lợi nhuận thuần cả năm? (mục 1)
4. Chỉ ra **hai** chỗ sai trong ba phát biểu về vốn lưu động ở tr. 194. (mục 2)
5. Đọc câu ③ theo đúng chữ thì lệch bao nhiêu phần trăm so với con số đúng? (mục 2)
6. Vì sao *"cuốn sách này vẫn dùng được"* dù có lỗi khái niệm? (mục 2)
7. Vẽ chu kỳ sản xuất. Vốn lưu động đổi những dạng nào? (mục 3)
8. Câu *"số lượng vẫn giữ nguyên"* nghĩa là gì? Chạy vòng nhanh hơn thì **được gì**? (mục 3)
9. Vì sao ba dòng vốn lưu động ít "nghệ thuật tài chính" hơn phần còn lại? Dòng nào **mềm dẻo nhất**?
   (mục 3)
10. Kiểm ba con số *"một ngày đáng giá bao nhiêu"* của sách. (mục 4)
11. Một ngày DSO bằng mấy ngày tồn kho? Viết công thức theo **biên lợi nhuận gộp**. (mục 4)
12. Nếu chỉ chọn được một đòn bẩy, chọn cái nào và vì sao? (mục 4)
13. *"2/10 net 30"* nghĩa là gì? Quy ra **lãi suất năm** là bao nhiêu? (mục 5)
14. So với lãi vay ngân hàng 11,1%, chiết khấu 2/10 đắt gấp mấy lần? (mục 5)
15. Khi nào chiết khấu thanh toán sớm **đáng** dùng? (mục 5)
16. Kể **bốn** bộ phận đẩy tồn kho lên, và hành vi hợp lý của mỗi bên. (mục 6)
17. Vì sao quản đốc nhà máy vẫn chạy máy khi cầu xuống? Sách nói gì về việc **trả thưởng**? (mục 6)
18. Tyco: 10 ngày tồn kho trên doanh thu 30 tỷ là bao nhiêu tiền? Vì sao con số đó là **cận trên**? (mục 6)
19. Chỗ nào ở tr. 203 sách viết DSO trong khi phải là DPO? Câu nào ngay sau đó chứng minh? (mục 7)
20. Kể câu chuyện Setpoint. Nguyên tắc 30 ngày đến từ đâu? (mục 7)
21. Nguyên tắc đó **giá bao nhiêu** trên công ty mẫu? Bằng mấy lần lợi nhuận năm? (mục 7)
22. Kể **ba** lý do khác để không kéo DPO quá dài. (mục 7)
23. Chỉ báo nào sách bảo bạn để ý ở DPO? (mục 7)
24. Viết công thức chu kỳ chuyển đổi tiền mặt và tính cho công ty mẫu. (mục 8)
25. Sách in **73 ngày**. Sai ở đâu, và đúng là bao nhiêu? (mục 8)
26. *"Trừ đi thời gian có thể thu tiền"* — sai chỗ nào? (mục 8)
27. Kể **ba** con số cùng được gọi là "vốn lưu động" và giải thích vì sao chúng khác nhau. (mục 8)
28. Vì sao 1.576 và 1.560 gần nhau chỉ là **trùng hợp**? (mục 8)
29. Viết công thức đóng cho độ lệch của công thức tắt. (mục 9)
30. **Hai** điều kiện nào làm công thức tắt đúng tuyệt đối? (mục 9)
31. Dấu của độ lệch phụ thuộc vào cái gì? (mục 9)
32. Khi nào nên dùng công thức tắt, và khi nào phải đọc thẳng bảng cân đối? (mục 9)
33. Hai công ty cùng DSO 50 ngày khác nhau thế nào? (mục 10)
34. Vì sao *"một tỷ lệ là một con số, một bảng phân tuổi là một phân bố"*? (mục 10)
35. Con số nào nên theo dõi hằng tháng bên cạnh DSO? Ai hỏi nó đầu tiên? (mục 10)
36. Chu kỳ tiền mặt của Vinamilk so với công ty mẫu? Chênh bao nhiêu ngày? (mục 11)
37. Chỉ báo DPO > DSO báo động ở Vinamilk. Vì sao **không** nên kết luận là Vinamilk gặp khó? (mục 11)
38. Vì sao công thức tắt lệch **ngược chiều** ở Vinamilk? (mục 11)
39. Vì sao độ lệch của Vinamilk **lớn hơn** của công ty mẫu? (mục 11)
40. Kể ba lưu ý khi tính chu kỳ tiền mặt trên báo cáo Việt Nam. (mục 11)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 11 — VỐN LƯU ĐỘNG VÀ CHU KỲ TIỀN MẶT                                ║
║           (ch. 26–28 + hộp công cụ, PDF tr. 193–208)                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⭐ "PHÉP ẢO THUẬT": cải thiện hiệu quả MÀ KHÔNG cần đổi doanh thu       ║
║     hay chi phí. Người ngoài tài chính chạm được ĐÚNG BA tài khoản:      ║
║        phải thu 1.312 + tồn kho 1.270 − phải trả 1.022 = 1.560           ║
║        = 6,29 LẦN lợi nhuận thuần cả năm, bỏ ra trước và chờ thu về.     ║
║                                                                          ║
║  ⚠️ TRANG 194 IN BA CÂU, HAI CÂU SAI:                                    ║
║     ① "trừ đi thứ doanh nghiệp SỞ HỮU" → phải là NỢ (sai MỘT CHỮ)        ║
║     ② "TSNH − NNH"  ✓ ĐÚNG                                               ║
║     ③ "TSNH gồm... PHẢI TRẢ; NNH gồm PHẢI THU" → ĐẢO NGƯỢC HOÀN TOÀN     ║
║     Đọc theo ③: 1.063 thay vì 1.576 — lệch 33%.                          ║
║     Câu đúng nằm GIỮA hai câu sai: sách TỰ MÂU THUẪN, không sai đều.     ║
║                                                                          ║
║  ⭐ BA ĐÒN BẨY KHÔNG BẰNG NHAU                                           ║
║     1 ngày DSO = 24,14 triệu  ·  1 ngày DII/DPO = 18,77 triệu            ║
║     → 1 ngày DSO = 1,29 NGÀY tồn kho = 1/(1 − biên gộp)                  ║
║     Biên gộp càng cao, khoảng cách càng giãn. Chọn một thì chọn DSO.     ║
║                                                                          ║
║  ⭐ "2/10 NET 30" = CHO KHÁCH VAY VỚI LÃI 36,7%/NĂM                      ║
║     so với lãi vay thật của công ty 11,1% → ĐẮT GẤP 3,3 LẦN.             ║
║     2% doanh thu = 9,0% LỢI NHUẬN GỘP biến mất.                          ║
║     Chỉ đáng dùng khi ngân hàng KHÔNG cho vay.                           ║
║                                                                          ║
║  TỒN KHO: bán hàng / kỹ sư / sản xuất / nhà xưởng đều đẩy nó lên.        ║
║     "được trả lương (CỘNG THÊM THƯỞNG)" để giữ chi phí đơn vị thấp →     ║
║     chạy máy khi cầu xuống. Cùng cơ chế PPE của bài 9 mục 5.             ║
║     ⚠️ Tyco: 10 ngày trên doanh thu 30 tỷ ≈ 648 TRIỆU $, không phải      ║
║        "hàng triệu" — nhỏ hơn hai bậc độ lớn (cận trên, xem mục 6).      ║
║                                                                          ║
║  ⭐ DPO — TÀI CHÍNH GẶP TRIẾT LÝ                                         ║
║     ⚠️ tr.203 in "đẩy DSO lên cao nhất" → phải là DPO                    ║
║     Setpoint không bao giờ để hoá đơn quá 30 ngày (vì hai sáng lập       ║
║     từng làm ở nơi trả chậm 100+ ngày). GIÁ: 459 TRIỆU = 1,85 LẦN        ║
║     lợi nhuận năm. Sách kể như điều đáng khen — và nó đáng khen —        ║
║     nhưng KHÔNG MIỄN PHÍ, và sách không đặt con số lên bàn.              ║
║                                                                          ║
║  ⭐ CHU KỲ TIỀN MẶT = DSO + DII − DPO = 54,4 + 74,2 − 54,5 = 74,1        ║
║     ⚠️ sách in "54 + 74 − 55 = 73"  ·  ⚠️ "trừ thời gian CÓ THỂ THU TIỀN"║
║        → là DPO, thời gian được phép TRẢ tiền.                           ║
║     BA CON SỐ CÙNG TÊN "VỐN LƯU ĐỘNG":                                   ║
║        1.762 (sách) · 1.788 (sửa) · 1.576 (BCĐKT) · 1.560 (vận hành)     ║
║                                                                          ║
║  ⭐ ĐỘ LỆCH CỦA CÔNG THỨC TẮT CÓ CÔNG THỨC ĐÓNG:                         ║
║        lệch = (DII − DPO) × (doanh thu/ngày − COGS/ngày)                 ║
║              = 19,72 × 5,369 = 105,9   ← khớp từng chữ số                ║
║     ⇒ đúng tuyệt đối CHỈ KHI: ① DII = DPO  hoặc  ② biên gộp = 0          ║
║     Dấu lệch = dấu của (DII − DPO).                                      ║
║                                                                          ║
║  📚 DSO GIẤU PHÂN BỐ: hai công ty cùng DSO 50 ngày —                     ║
║     A có 50% nợ quá 90 ngày, B chỉ 12,5%. Đọc BẢNG PHÂN TUỔI.            ║
║                                                                          ║
║  🇻🇳 VINAMILK chu kỳ 21,8 ngày vs 74,1 — chỉ bằng 29%.                    ║
║     DPO 78,2 > DSO 43,7 → chỉ báo của sách BÁO ĐỘNG, nhưng đọc cho       ║
║     đúng: coverage 30 lần, 45% tài sản là tiền → SỨC MẠNH ĐÀM PHÁN,      ║
║     không phải túi nghèo. Chỉ báo bảo ĐẶT CÂU HỎI, không bảo kết luận.   ║
║     ⭐ DII < DPO → công thức tắt ĐỘI XUỐNG 22%, ngược chiều công ty mẫu  ║
║        (+6,3%). Cùng một công thức, hai chiều lệch ngược nhau.           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần VII — Ứng dụng trí tuệ tài chính vào thực tế quản lý vốn lưu động**, trang tiêu đề PDF tr. 192.
    ⚠️ Bản dịch in **"PHẦN VI"**, trùng số với phần ROI (tr. 170).
    - Ch. 26 *Phép ảo thuật quản lý bảng cân đối kế toán*, PDF tr. 193–196
      — ⭐ *"một phép ảo thuật tài chính"* và ⚠️ **định nghĩa ① sai chữ "sở hữu"** (tr. 193); ⚠️ **công thức ②
      đúng và diễn giải ③ đảo ngược phải thu/phải trả**, **chu kỳ sản xuất**, ví dụ Viện Business Literacy,
      *"số lượng vẫn giữ nguyên"*, Hình 26-1 (tr. 194); ⭐ **ba tài khoản** người ngoài tài chính chạm được
      (tr. 195); ⭐ *"có bao nhiêu nghệ thuật… một chút"* (tr. 196)
    - Ch. 27 *Các đòn bẩy trên bảng cân đối kế toán*, PDF tr. 197–202
      — DSO và vốn lưu động, **quản lý DSO** (tr. 197); ai tác động lên khoản phải thu và ⭐ **"2/10 net 30"**
      (tr. 198); ⭐ **giảm DSO một ngày = hơn 24 triệu**, **khách hàng lý tưởng "Bob"**, *"ăn vào lợi nhuận"*
      (tr. 199); **quản lý tồn kho**, *"khoản tiền đông cứng"*, lean/JIT/EOQ (tr. 200); **ai đẩy tồn kho lên**
      — bán hàng, kỹ sư, sản xuất, và ⭐ *"được trả lương (cộng thêm thưởng)"* (tr. 201); ⭐ *"đọc một cuốn
      sách còn hữu ích hơn"* và **rút một ngày DII = gần 19 triệu** (tr. 202)
    - Ch. 28 *Tập trung chuyển đổi tiền mặt*, PDF tr. 203–207
      — *"tài chính gặp gỡ triết lý"*, ⚠️ **DSO in nhầm thay DPO**, **Dun & Bradstreet** và ⭐ **câu chuyện
      Setpoint 30 ngày** (tr. 203); ⭐ **chỉ báo DPO > DSO** và Hình 28-1 (tr. 204); **chu kỳ chuyển đổi tiền
      mặt** — công thức, ⚠️ *"73 ngày"* và ⚠️ *"trừ thời gian có thể thu tiền"* (tr. 206); ⚠️ **Tyco — 10
      ngày trên doanh thu 30 tỷ** và ba cách rút ngắn chu kỳ (tr. 207)
    - **Hộp công cụ** *Kỳ thu tiền*, PDF tr. 207–208 — 📚 *"DSO là con số bình quân"* (tr. 207); **hai công
      ty cùng DSO 50 ngày** và **bảng phân tuổi công nợ** (tr. 208)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mọi mục
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 11](#11-vinamilk--chỉ-báo-của-sách-báo-động-và-công-thức-tắt-lệch-ngược-chiều).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py`](../thuc_hanh/bai-11-von-luu-dong-va-chu-ky-tien-mat.py):
  - đọc định nghĩa vốn lưu động theo câu ③ cho **1.063** thay vì **1.576** — chốt bằng `assert`;
  - ba con số *"một ngày đáng giá"* của sách (24,1 / 18,8 / 18,8 triệu) đều khớp — chốt bằng `assert`;
  - tỷ số một ngày DSO / một ngày tồn kho **bằng đúng** $1/(1 - \text{biên lợi nhuận gộp})$ — chốt bằng
    `assert`, và kiểm thêm ở biên gộp 50% thì tỷ số bằng đúng **2,0**;
  - lãi suất ngầm của *"2/10 net 30"* **lớn hơn ba lần** lãi vay thật của công ty mẫu — chốt bằng `assert`;
  - giá của chính sách DPO 30 ngày kiểu Setpoint **lớn hơn** lợi nhuận thuần cả năm — chốt bằng `assert`;
  - chu kỳ chuyển đổi tiền mặt bằng **74,1 ngày**, không phải **73** như sách in — chốt bằng `assert`;
  - **độ lệch của công thức tắt bằng đúng** $(\text{DII} - \text{DPO}) \times (\text{DT/ngày} -
    \text{COGS/ngày})$ — chốt bằng `assert` ở **cả hai** doanh nghiệp;
  - độ lệch **dương** ở công ty mẫu và **âm** ở Vinamilk — chốt bằng `assert`;
  - hai công ty trong ví dụ hộp công cụ có **cùng DSO 50 ngày** — chốt bằng `assert`;
  - DPO của Vinamilk **lớn hơn** DSO — chỉ báo của sách báo động — chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** khái niệm **vốn lưu động vận hành** ở mục 1; cách
  đọc câu ③ theo chữ ở mục 2; toàn bộ so sánh ba đòn bẩy ở mục 4; mọi phép quy chiết khấu ra lãi suất năm ở
  mục 5; tỷ lệ giá vốn 77,8% dùng cho Tyco ở mục 6; mức DPO mục tiêu 30 ngày ở mục 7; ba cách đọc "vốn lưu
  động" ở mục 8; **công thức đóng cho độ lệch** ở mục 9; cách dựng công ty B ở mục 10. Mọi con số **của
  sách** đều được trích kèm mốc `ch. N · PDF tr. M`.

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
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| **11** | **Vốn lưu động và chu kỳ tiền mặt** ← *bạn đang ở đây* | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
