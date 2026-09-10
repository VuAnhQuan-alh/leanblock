# Bài 10 — Tính tỷ lệ hoàn vốn đầu tư

> Bài học dựng từ **Phần VI — Hướng dẫn cách tính toán (và thật sự hiểu) tỷ lệ hoàn vốn đầu tư**:
> chương 24 *Những khối đá làm nên tỷ lệ hoàn vốn đầu tư* (PDF tr. 172–178), chương 25 *Tính tỷ lệ hoàn
> vốn đầu tư* (PDF tr. 179–189), và hộp công cụ Phần VI (PDF tr. 189–191).
> 🔸 **Vòng 2 — và bài này CỐ TÌNH MỎNG.** Giá trị hiện tại, chiết khấu, NPV và IRR đã được dạy kỹ hơn ở
> **[EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md)**. Bài này
> **không dạy lại cơ chế chiết khấu** — nó chỉ kiểm lại từng con số của sách, rồi làm bốn thứ EG14 **không
> có**: thời gian hoàn vốn, ngưỡng thu hồi vốn, chi phí sử dụng vốn, và phân tích độ nhạy.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:**
> [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md) *(bắt buộc —
> toàn bộ phép chiết khấu nằm ở đó)* · [Bài 7](bai_07_bao_cao_luu_chuyen_tien_te.md) *(mọi phép tính ở đây
> chạy trên **dòng tiền**, không phải lợi nhuận)* ·
> [Bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) *(lá chắn thuế của lãi vay)*.
> ⚙️ **Code:** [`thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py`](../thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py)
> — kiểm lại **từng con số** của ch. 24–25 (có hai chỗ sách in sai), và đo bằng số bốn thứ sách chỉ nói
> bằng lời.

---

## Mục lục

<!-- MUC-LUC -->

- [1. Vì sao bài này cố tình mỏng](#1-vì-sao-bài-này-cố-tình-mỏng)
- [2. Ba khối đá của chương 24](#2-ba-khối-đá-của-chương-24)
- [3. Chi phí sử dụng vốn — phép tính duy nhất chương 24 đưa ra](#3-chi-phí-sử-dụng-vốn--phép-tính-duy-nhất-chương-24-đưa-ra)
- [4. Thời gian hoàn vốn — phương pháp EG14 không có](#4-thời-gian-hoàn-vốn--phương-pháp-eg14-không-có)
- [5. Thời gian hoàn vốn chiết khấu — con số sách không đưa](#5-thời-gian-hoàn-vốn-chiết-khấu--con-số-sách-không-đưa)
- [6. NPV và IRR — kiểm lại từng con số, và hai chỗ in sai](#6-npv-và-irr--kiểm-lại-từng-con-số-và-hai-chỗ-in-sai)
- [7. Ngưỡng thu hồi vốn là một QUYẾT ĐỊNH, không phải một phép tính](#7-ngưỡng-thu-hồi-vốn-là-một-quyết-định-không-phải-một-phép-tính)
- [8. Phân tích độ nhạy — sách ra bài kiểm, ví dụ của chính sách suýt trượt](#8-phân-tích-độ-nhạy--sách-ra-bài-kiểm-ví-dụ-của-chính-sách-suýt-trượt)
- [9. Ba phương án A/B/C — và con số sách bỏ ngỏ](#9-ba-phương-án-abc--và-con-số-sách-bỏ-ngỏ)
- [10. 💼 Setpoint — bốn câu hỏi của người kỹ thuật, quy ra tiền](#10--setpoint--bốn-câu-hỏi-của-người-kỹ-thuật-quy-ra-tiền)
- [11. 🇻🇳 Cùng một dự án, hai doanh nghiệp, hai quyết định ngược nhau](#11--cùng-một-dự-án-hai-doanh-nghiệp-hai-quyết-định-ngược-nhau)
- [12. 📚 Hộp công cụ — hướng dẫn từng bước viết một đề án](#12--hộp-công-cụ--hướng-dẫn-từng-bước-viết-một-đề-án)
- [13. Tự thử](#13-tự-thử)
- [14. Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
- [15. Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Vì sao bài này cố tình mỏng

Chương 24 và 25 là **hai chương duy nhất** của cuốn sách trùng với một môn đã học. Giá trị tương lai, giá
trị hiện tại, chiết khấu, NPV, IRR —
[EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md) đã dạy kỹ hơn
hẳn, có cả lãi kép và quy tắc 70. Nên bài này **không dạy lại cơ chế ấy**.

| khái niệm | ch. | học ở đâu |
| --- | :---: | --- |
| Giá trị tiền tệ theo thời gian | 24 | [EG14 bài 5 mục 2](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md#2-giá-trị-hiện-tại--đo-giá-trị-của-tiền-tệ-theo-thời-gian) — **kỹ hơn** |
| Giá trị tương lai / hiện tại | 24 | [EG14 bài 5 mục 2](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md#2-giá-trị-hiện-tại--đo-giá-trị-của-tiền-tệ-theo-thời-gian) |
| Lãi kép, quy tắc 70 | — | [EG14 bài 5 mục 3](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md#3--ma-thuật-của-lãi-kép-và-quy-tắc-70--hộp-bạn-có-biết-tr-316) *(sách này **không có**)* |
| Rủi ro và tỷ suất sinh lợi | 24 | [EG14 bài 5 mục 7](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md#7-đánh-đổi-giữa-rủi-ro-và-sinh-lợi--hình-3-tr-321) |
| Chi phí cơ hội | 24 | [EG13 bài 1 mục 3](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó) — nguyên lý 2 |
| Chi phí chìm | — | [EG13 bài 1 mục 5](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#5--chi-phí-chìm--hệ-quả-quan-trọng-nhất-mà-sách-để-trong-bài-tập) *(sách này **không có**)* |
| **Thời gian hoàn vốn** | 25 | ⭐ **chỉ có ở đây** — [mục 4](#4-thời-gian-hoàn-vốn--phương-pháp-eg14-không-có)–[5](#5-thời-gian-hoàn-vốn-chiết-khấu--con-số-sách-không-đưa) |
| **Ngưỡng thu hồi vốn** | 24 | ⭐ **chỉ có ở đây** — [mục 7](#7-ngưỡng-thu-hồi-vốn-là-một-quyết-định-không-phải-một-phép-tính) |
| **Chi phí sử dụng vốn (WACC)** | 24 | ⭐ **chỉ có ở đây** — [mục 3](#3-chi-phí-sử-dụng-vốn--phép-tính-duy-nhất-chương-24-đưa-ra) |
| **Phân tích độ nhạy** | 25 | ⭐ **chỉ có ở đây** — [mục 8](#8-phân-tích-độ-nhạy--sách-ra-bài-kiểm-ví-dụ-của-chính-sách-suýt-trượt) |

⭐ Bốn dòng có ⭐ là ruột của bài này. Chúng **không phải kỹ thuật chiết khấu** — chúng là những thứ **bao
quanh** phép chiết khấu: **lấy số ở đâu, chọn ngưỡng nào, và tin con số kết quả đến mức nào.**

Và sách nói thẳng ngay đầu ch. 25 rằng đó mới là chỗ khó:

> *"Hãy nhớ rằng đây cũng là **một bài luyện nghệ thuật tài chính**. Nó quả thật rất tuyệt vời: các chuyên
> gia tài chính có thể và thật sự phân tích các đề án, rồi đưa ra những khuyến nghị **dựa trên các giả định
> và ước tính**… Họ thậm chí còn **thích thú với thách thức** khi tính toán **những con số không biết**, và
> **định lượng chúng theo cách thức giúp doanh nghiệp trông thành công hơn**."* — ch. 25 · PDF tr. 180

---

## 2. Ba khối đá của chương 24

Sách gọi tên ba khái niệm ở giữa chương, rồi thêm hai cái nữa ở cuối:

> ① giá trị tương lai · ② giá trị hiện tại · ③ tỷ suất sinh lợi yêu cầu
> ④ chi phí cơ hội · ⑤ chi phí sử dụng vốn

**Kiểm lại hai ví dụ số của chương.** Kế hoạch nghỉ hưu: 50.000 đô-la ở tuổi 35, đến 65 tuổi còn bao nhiêu?

| tỷ suất giả định | giá trị sau 30 năm | sách viết |
| ---: | ---: | ---: |
| 3% | **121.363** | *"hơn 121.000"* |
| 6% | **287.175** | *"hơn 287.000"* |

⭐ **Ba điểm phần trăm lãi suất làm số tiền gấp 2,37 lần sau 30 năm** *(chốt bằng `assert`)*. Sách đặt
chính ví dụ này để nói về nghệ thuật tài chính:

> *"Bạn giả định tỷ suất sinh lợi bình quân trong 30 năm tới là **3%, hay 6%**? **Chênh lệch giữa hai giả
> định sẽ rất lớn**… May mắn thì việc tính toán giá trị tương lai trong khoảng thời gian xa như thế là
> **một phỏng đoán kinh nghiệm** – một phép thực hành thể hiện tài năng nghệ thuật."* — ch. 24 · PDF tr. 174

Một ô trong bảng tính, **hơn gấp đôi** kết quả.

Giá trị hiện tại, chiều ngược lại: **106.000** đô-la sau một năm, chiết khấu 6% → **100.000** đô-la hôm nay.

⭐ **Tỷ suất sinh lợi yêu cầu = ngưỡng thu hồi vốn** *(hurdle rate)*. Sách neo nó bằng một cặp số rất dễ nhớ:

> *"Bạn **có thể không** đầu tư 100.000 đô-la ngày hôm nay để nhận được **102.000** đô-la sau một năm – lãi
> suất **2%**, nhưng **rất có thể** bạn sẽ đầu tư 100.000 đô-la ngày hôm nay để thu được **120.000** đô-la
> một năm sau đó – **20%**."* — ch. 24 · PDF tr. 176

📌 **Chi phí cơ hội** là khối đá thứ tư, và nó không phải của cuốn sách này:

> *"Trong ngôn ngữ thường ngày, cụm từ này chỉ **những gì bạn phải từ bỏ** khi theo đuổi một hoạt động nhất
> định. Nếu bạn dành toàn bộ số tiền có được cho một kỳ nghỉ xa hoa, chi phí cơ hội là **bạn không thể mua
> xe**."* — ch. 24 · PDF tr. 177

Đó là **nguyên lý 2** của Mankiw, đã học ở
[EG13 bài 1 mục 3](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó).
[Mục 11](#11--cùng-một-dự-án-hai-doanh-nghiệp-hai-quyết-định-ngược-nhau) đo nó bằng số liệu thật.

---

## 3. Chi phí sử dụng vốn — phép tính duy nhất chương 24 đưa ra

> *"Các chuyên gia tài chính tính toán chi phí sử dụng vốn của doanh nghiệp theo nhiều cách: (1) tính
> **chi phí vay nợ** (lãi suất), (2) ước tính **lợi nhuận mà cổ đông kỳ vọng** thu về, và (3) tính toán
> **con số trung bình có điều chỉnh** từ hai con số trên."* — ch. 24 · PDF tr. 178

| nguồn vốn | tỷ trọng | chi phí | góp vào WACC |
| --- | ---: | ---: | ---: |
| Vay nợ *(sau thuế)* | 25% | 4% | 1% |
| Vốn chủ sở hữu | 75% | 16% | 12% |
| **CHI PHÍ SỬ DỤNG VỐN** | **100%** | | **13%** |

⭐ Hai chi tiết trong ô này đáng dừng lại:

- **vốn chủ sở hữu đắt gấp bốn lần vay nợ** (16% so với 4%). Cổ đông đòi hỏi nhiều hơn chủ nợ vì họ **đứng
  sau** trong hàng đợi và **không có gì bảo đảm**.
- **lãi suất vay 4% đã là sau thuế** — sách ghi rõ *"(sau khi tính đến chi tiết có thể trừ lãi suất đó khỏi
  thuế)"*. Đó là cùng một **lá chắn thuế** mà [bài 8](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) mục 6
  đã nói khi giải thích vì sao nhiều doanh nghiệp sẵn lòng vay nhiều.

Và sách hạ một **luật**, không phải một gợi ý:

> *"Một vụ đầu tư có tỷ suất sinh lợi **thấp hơn** chi phí sử dụng vốn sẽ không đáp ứng được cả hai mục
> tiêu này, vì vậy **tỷ suất sinh lợi yêu cầu luôn phải cao hơn chi phí sử dụng vốn**."*
> — ch. 24 · PDF tr. 176

[Mục 7](#7-ngưỡng-thu-hồi-vốn-là-một-quyết-định-không-phải-một-phép-tính) đem luật này đối chiếu với chính
ví dụ của chương 25.

---

## 4. Thời gian hoàn vốn — phương pháp EG14 không có

**Ví dụ chủ đạo của ch. 25**, dùng suốt bài này: mua một máy tính chuyên dụng giá **3.000** đô-la, dùng được
**3 năm**, mỗi năm mang về **1.300** đô-la. Ngưỡng thu hồi vốn **8%**.

$$\text{Thời gian hoàn vốn} = \frac{3.000}{1.300\ \text{mỗi năm}} = \mathbf{2{,}31}\ \text{năm}$$

Bài kiểm thứ nhất của sách: *"Thời gian hoàn vốn **rõ ràng phải ngắn hơn tuổi đời của dự án**; nếu không,
chẳng có lý do gì để đầu tư cả."* — 2,31 < 3 → qua.

⚠️ Sách liệt kê **ba nhược điểm**, và cả ba đều đo được:

> ① *"không đánh giá được liệu dòng tiền **có vượt ra khỏi điểm hoà vốn** không"*
> ② *"không cho bạn biết **tổng lợi nhuận** có thể là bao nhiêu"*
> ③ *"**không tính đến giá trị tiền tệ theo thời gian**… đó chỉ là **so sánh táo với cam**"*
> — ch. 25 · PDF tr. 182

Đo nhược điểm ① và ② bằng một cặp dự án **có cùng thời gian hoàn vốn** *(cặp này là của bài học)*:

| dự án | dòng tiền 3 năm | hoàn vốn | NPV @8% |
| --- | ---: | ---: | ---: |
| Dự án X | 1.300 · 1.700 · **0** | **2,00 năm** | **−339** |
| Dự án Y | 1.300 · 1.700 · **4.000** | **2,00 năm** | **+2.837** |

⭐ Cùng một thời gian hoàn vốn **2,00 năm**, nhưng NPV lệch **3.175 đô-la — 106% vốn đầu tư**. Một dự án
đáng **loại**, một dự án đáng **nhận**, và thời gian hoàn vốn cho ra **cùng một con số**. Nó không nhìn thấy
năm thứ ba *(chốt bằng `assert`)*.

---

## 5. Thời gian hoàn vốn chiết khấu — con số sách không đưa

Nhược điểm ③ — *"so sánh táo với cam"* — thì sách chỉ nói bằng lời. **Nó sửa được:** chiết khấu từng dòng
tiền **trước** khi cộng dồn.

| năm | dòng tiền | hệ số $1/1{,}08^n$ | giá trị hiện tại | luỹ kế |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1.300 | 0,9259 | 1.203,70 | 1.203,70 |
| 2 | 1.300 | 0,8573 | 1.114,54 | 2.318,24 |
| 3 | 1.300 | 0,7938 | 1.031,98 | **3.350,23** |

| | |
| --- | ---: |
| thời gian hoàn vốn **đơn giản** | 2,31 năm |
| thời gian hoàn vốn **CHIẾT KHẤU** | **2,66 năm** |

⭐ **2,66 năm thay vì 2,31 — dài hơn 15%.** Và đây mới là chỗ quan trọng: tuổi đời dự án là **3 năm**, nên
**biên an toàn thật chỉ còn 0,34 năm**, chứ không phải 0,69 năm như con số thô gợi ý. **Bớt một nửa**
*(chốt bằng `assert`)*.

⚠️ Nhưng thời gian hoàn vốn chiết khấu **vẫn không sửa được** nhược điểm ① và ②: nó vẫn mù tịt với mọi thứ
xảy ra **sau** khi hoàn vốn. Chỉ NPV nhìn thấy cả chuỗi. Đó là lý do sách xếp nó là *"**quy tắc mang tính
kinh nghiệm dạng thô sơ**, chứ không phải một phân tích tài chính hùng hồn"*.

---

## 6. NPV và IRR — kiểm lại từng con số, và hai chỗ in sai

⚠️ **Cơ chế chiết khấu không dạy lại ở đây** — xem
[EG14 bài 5 mục 2](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md#2-giá-trị-hiện-tại--đo-giá-trị-của-tiền-tệ-theo-thời-gian).
Mục này **chỉ kiểm số**.

| | tính ra | sách in | |
| --- | ---: | ---: | :---: |
| PV @ 8% | 3.350,23 | 3.350 | ✓ |
| NPV = PV − vốn | 350,23 | 350 | ✓ |
| tổng dòng tiền thô | 3.900 | 3.900 | ✓ |
| **IRR** *(NPV = 0)* | **14,36%** | **14,36%** | ✓ |

### ⚠️ Hai chỗ sách in sai, cả hai ở cùng một đoạn giải thích IRR (tr. 186)

| ngưỡng | sách in | tính đúng | lệch |
| ---: | ---: | ---: | ---: |
| 10% | **212** | **233** | +21 |
| 20% | **−218** | **−262** | −44 |

⭐ Nhưng **kết luận** của sách thì không hỏng: *"điểm uốn mà tại đó NPV bằng 0 sẽ nằm đâu đó **trong khoảng
từ 10–20%**."* Với cả hai bộ số, kết luận đó vẫn đúng, và **IRR 14,36% mà sách in cuối cùng là đúng**. Chỉ
hai con số trung gian sai.

💼 **Và đây là một bẫy mà cả hai bộ số đều dính:** nội suy tuyến tính giữa hai NPV **không** cho ra IRR, vì
NPV là hàm **cong** của $r$, không phải đường thẳng.

| cách | kết quả |
| --- | ---: |
| nội suy theo số **sách in** | 14,93% |
| nội suy theo số **tính đúng** | 14,71% |
| **IRR thật** | **14,36%** |

Cả hai đều **vọt quá**. Khoảng cách càng rộng thì nội suy càng lệch *(chốt bằng `assert`)*.

---

## 7. Ngưỡng thu hồi vốn là một QUYẾT ĐỊNH, không phải một phép tính

> *"Các quyết định về ngưỡng thu hồi vốn **hiếm khi là vấn đề thực hiện công thức**. Giám đốc tài chính hay
> thủ quỹ của doanh nghiệp sẽ đánh giá **mức độ rủi ro** của một vụ đầu tư, **nguồn vốn** có thể cấp cho nó,
> và **tình hình tổng thể** của doanh nghiệp… Sau đó, ông ta **phán đoán – hay giả định** – về ngưỡng thu
> hồi vốn hợp lý."* — ch. 24 · PDF tr. 177

Sách cho hai quy tắc ngón tay cái: doanh nghiệp **tăng trưởng cao** dùng ngưỡng **cao**; doanh nghiệp
**tăng trưởng thấp, ổn định** dùng ngưỡng **thấp**.

Đo xem cái "phán đoán" ấy đắt giá bao nhiêu — **cùng một dự án**, đổi ngưỡng:

| ngưỡng | PV | NPV | kết luận | ghi chú |
| ---: | ---: | ---: | :---: | --- |
| 4,00% | 3.608 | 608 | NHẬN | *"thu được 4% ở những nơi khác"* |
| **8,00%** | 3.350 | **350** | NHẬN | ngưỡng của ví dụ ch. 25 |
| 9,00% | 3.291 | 291 | NHẬN | ngưỡng của ví dụ A/B/C, [mục 9](#9-ba-phương-án-abc--và-con-số-sách-bỏ-ngỏ) |
| **13,00%** | 3.069 | **69** | NHẬN | ⚠️ WACC 13% của chính ch. 24 |
| 14,36% | 3.000 | 0 | HOÀ | **IRR — điểm lật** |
| 20,00% | 2.738 | **−262** | LOẠI | *"thủ quỹ đặt ngưỡng 20%"* |

⭐ Cùng một chiếc máy, cùng một dòng tiền. Ngưỡng **8%** thì *"nên mua"*; ngưỡng **20%** thì *"đừng mua"*.
**Không có phép tính nào trong ch. 25 quyết định điều đó** — nó được quyết ở ch. 24, bởi **một người**, bằng
**phán đoán**.

### ⚠️ Một phép đối chiếu đáng chạy

Chương 24 tính **WACC = 13%**, rồi hạ luật *"tỷ suất sinh lợi yêu cầu **luôn phải cao hơn** chi phí sử dụng
vốn"*. Chương 25 đặt ngưỡng **8%**.

- ở ngưỡng **8%**: NPV = **350** — dự án vượt thoải mái *(11,7% vốn)*
- ở ngưỡng **13%**: NPV = **69** — vẫn dương, nhưng chỉ còn **2,3% vốn**

**Đây không phải lỗi của sách:** hai chương dùng **hai doanh nghiệp giả định khác nhau**. Nhưng nó là một
bài kiểm tra bạn nên tự chạy: ngưỡng 8% **hàm ý** một doanh nghiệp có WACC **dưới 8%** — một doanh nghiệp
khác hẳn cái ở ch. 24 *(chốt bằng `assert`)*.

---

## 8. Phân tích độ nhạy — sách ra bài kiểm, ví dụ của chính sách suýt trượt

Sách ra bài kiểm ở **hai chỗ**, và lần nào cũng cùng một con số:

> *"Thường thì việc tiến hành **một phân tích độ nhạy** là hợp lý – tức là **kiểm tra các phép tính sử dụng
> dòng tiền tương lai bằng 80–90% phỏng đoán ban đầu**, và xem liệu phương án đầu tư đó **có còn hợp lý** hay
> không."* — ch. 25 · PDF tr. 188

> *"Tiến hành phân tích độ nhạy, và nếu có thể hãy **chứng minh ước tính đó vẫn hợp lý ngay cả nếu dòng tiền
> không trở thành hiện thực** ở cấp độ mà bạn hi vọng."* — hộp công cụ · PDF tr. 191

**Chạy chính bài kiểm ấy lên chính ví dụ của sách:**

| dòng tiền | mỗi năm | PV @8% | NPV | kết luận |
| --- | ---: | ---: | ---: | :---: |
| 100,0% phỏng đoán | 1.300 | 3.350 | **350** | NHẬN |
| 95,0% | 1.235 | 3.183 | 183 | NHẬN |
| **90,0%** | 1.170 | 3.015 | **15** | NHẬN |
| **89,55%** | 1.164 | 3.000 | **0** | **HOÀ VỐN** |
| 85,0% | 1.105 | 2.848 | −152 | LOẠI |
| **80,0%** | 1.040 | 2.680 | **−320** | **LOẠI** |

⭐ **Điểm hoà vốn chính xác: 89,55% của dòng tiền dự báo.** Sách bảo kiểm ở khoảng **80–90%** (tr. 188). Ví dụ **chủ
đạo của chính sách**:

- ở **90%** → NPV = **15** — sống sót, nhưng chỉ **vừa đủ**;
- ở **80%** → NPV = **−320** — **trượt**.

**Tức là dự án này trượt ở đáy dưới của chính khoảng mà sách bảo phải kiểm** *(chốt bằng `assert`)*.

⚠️ Con số **350 đô-la** nghe rất vững, cho đến khi đổi ra tỷ lệ: **11,7% của vốn đầu tư**. Ước tính dòng
tiền lệch **10,5%** là nó biến mất. **Đọc NPV trần thì không thấy điều đó; đọc NPV chia vốn đầu tư thì thấy
ngay.**

💼 **Nên đọc NPV kèm hai con số nữa**, và cả hai đều tính miễn phí:

| | |
| --- | ---: |
| NPV / vốn ban đầu *(biên an toàn)* | **11,7%** |
| IRR − ngưỡng *(khoảng hở về tỷ suất)* | **6,36 điểm phần trăm** |

Cả hai đều nói cùng một câu: **dự án này không còn nhiều chỗ để sai.**

---

## 9. Ba phương án A/B/C — và con số sách bỏ ngỏ

Cùng **3.000** đô-la, ba phương án, ngưỡng **9%**, *"cả ba đều có mức độ rủi ro ngang nhau"*:

| PA | dòng tiền | hoàn vốn | NPV @9% | IRR |
| :---: | --- | ---: | ---: | ---: |
| A | 1.000 · 1.000 · 1.000 | 3 năm | **−469** | 0,0% |
| B | **3.600** · 0 · 0 | **1 năm** | 303 | **20,0%** |
| C | 0 · 0 · **4.600** | 3 năm | **552** | 15,3% |

⭐ **Cả chín con số đều khớp sách** *(chốt bằng `assert`)*. Đây là đoạn tính toán sách làm **chính xác
nhất**.

**Ba phương pháp, ba người thắng khác nhau:** hoàn vốn → **B** · IRR → **B** · NPV → **C**.

> *"Nếu chỉ áp dụng phương pháp tính IRR, chúng ta sẽ chọn phương án B. Nhưng phép tính NPV lại nghiêng về
> phương án C, **và đó sẽ là quyết định đúng đắn**… Mặc dù B cho tỷ suất sinh lợi cao hơn C, nhưng ta
> **chỉ thu được lợi nhuận trong một năm**."* — ch. 25 · PDF tr. 188

Sách tự kiểm — **bằng lời, không đưa con số**: *"nếu chúng ta lấy số tiền 3.600 đô-la mà phương án đầu tư B
mang về… và tái đầu tư với tỷ lệ sinh lợi 9%, đến cuối năm thứ ba chúng ta vẫn **thu được về ít hơn** so
với lợi nhuận từ phương án đầu tư C."* Tính ra: $3.600 \times 1{,}09^2 = \mathbf{4.277} < 4.600$.
**Sách đúng.**

### Nhưng sách dừng ở đó

Câu hỏi còn lại là: **tái đầu tư ở bao nhiêu thì B thắng?** Giải $3.600 \times (1+r)^2 = 4.600$:

$$r = \sqrt{\tfrac{4.600}{3.600}} - 1 = \mathbf{13{,}04\%}$$

**Trên 13,04% thì B thắng; dưới thì C thắng.** Sách chỉ thử **một** điểm (9%), và 9% thấp hơn 13,04% — nên
kết luận của sách **đúng, nhưng chỉ đúng trong phạm vi giả định đó**. Doanh nghiệp nào thật sự tái đầu tư
được ở 13% thì **đảo ngược kết luận** *(chốt bằng `assert`)*.

⚠️ Đó chính là **giả định âm thầm của NPV**, mà sách nói thẳng một nửa:

> *"Phương pháp NPV **không thể tính được** các phương án đầu tư giả định trong tương lai. Nó chỉ **định
> được là công ty có thể tiếp tục có tỷ suất sinh lợi là 9%**."* — ch. 25 · PDF tr. 188

Tức là NPV giả định mọi đồng tiền thu về đều được tái đầu tư **ở đúng ngưỡng**, không hơn.

⚠️ **Sách in sai một chỗ ở đây:** *"ở phương án C, giá trị tiền tệ tính theo thời giá hiện tại cao hơn
**phương án C**."* Vế sau phải là **phương án B**. Lỗi biên tập.

---

## 10. 💼 Setpoint — bốn câu hỏi của người kỹ thuật, quy ra tiền

Sách đóng ch. 25 bằng **một câu chuyện**, không bằng một công thức. Một giám đốc đề nghị Setpoint đầu tư
**80.000 đô-la** làm thiết bị tự sản xuất linh kiện. Trước khi Joe kịp lên tiếng, **một chuyên gia kỹ thuật
ở xưởng lắp ráp** hỏi bốn câu:

| câu hỏi | ứng với bước nào |
| --- | --- |
| *"Ông đã tính **lợi nhuận hàng tháng** mà chúng ta có thể thu về từ thiết bị này chưa? 80.000 đô-la là khoản lớn đấy!"* | bước 2 — dự kiến dòng tiền |
| *"Ông có thấy rằng chúng ta đang ở **kỳ xuân**, và hoạt động kinh doanh thường ảm đạm, còn **tiền mặt thì không dư dả** trong suốt mùa hè không?"* | bước 1 — **thời điểm** của dòng tiền ra |
| *"Ông đã tính **chi phí lao động** để vận hành thiết bị đó chưa? … có thể ông sẽ phải **tuyển thêm người vận hành** đấy."* | bước 1 — **tổng** chi phí, không chỉ giá mua |
| *"Còn **cách chi tiêu nào hay hơn** để phát triển hoạt động kinh doanh không?"* | ⭐ **chi phí cơ hội** |

> *"Sau màn chất vấn này, **vị giám đốc từ bỏ đề xuất**. Chuyên gia kỹ thuật kia **có thể không phải là
> chuyên gia về các phép tính giá trị hiện tại thuần**, nhưng hẳn là **ông hiểu tất cả những khái niệm đó**."*
> — ch. 25 · PDF tr. 189

**Quy câu hỏi thứ nhất ra số** *(tuổi đời 5 năm và ngưỡng 9% là giả định của bài học — sách không cho)*:

> hệ số niên kim 5 năm @ 9% = **3,8897**
> → thiết bị phải mang về **20.567 đô-la mỗi năm**, tức **1.714 đô-la mỗi tháng**, **chỉ để hoà vốn**

⭐ Và đó là lý do **câu hỏi số 3 giết chết đề xuất**. Nếu phải tuyển một người vận hành:

| lương người vận hành | thiết bị phải mang về | gấp |
| ---: | ---: | ---: |
| 2.000 $/tháng | **3.714 $/tháng** | 2,17 lần |
| 3.000 $/tháng | **4.714 $/tháng** | 2,75 lần |

Một dòng **chi phí vận hành** bị bỏ quên ở bước 1 làm **bội số** yêu cầu ở bước 2. **Người kỹ thuật không
tính NPV. Ông ấy chỉ không để sót đồng nào** *(chốt bằng `assert`)*.

---

## 11. 🇻🇳 Cùng một dự án, hai doanh nghiệp, hai quyết định ngược nhau

Chi phí cơ hội của ch. 24 nghe rất trừu tượng cho đến khi đặt hai doanh nghiệp thật cạnh nhau. Chiếc máy
tính của ch. 25 có **IRR 14,36%**. Đem nó đi chào hàng:

| | Công ty mẫu (Mỹ, 2005) | Vinamilk (VN, 2024) |
| --- | ---: | ---: |
| ROA hiện tại | **4,78%** | **15,24%** |
| ROE hiện tại | 10,09% | 23,37% |
| IRR của dự án | 14,36% | 14,36% |
| **quyết định** | **NHẬN** — kéo trung bình **lên** | **LOẠI** — kéo trung bình **xuống** |

⭐ **Cùng một dự án, cùng một dòng tiền, cùng một IRR — hai quyết định ngược nhau.** Không phải vì dự án
đổi. Vì **cái mà mỗi bên phải từ bỏ** thì khác nhau. Đó đúng là định nghĩa chi phí cơ hội mà ch. 24 đưa ra,
và là nguyên lý 2 của
[EG13](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md#3-nguyên-lý-2--chi-phí-của-một-thứ-là-cái-mà-bạn-từ-bỏ-để-có-được-nó)
*(chốt bằng `assert`)*.

⚠️ Và nó là một pha **sát nút**, không phải một khoảng cách an toàn: 14,36% so với 15,24% — chỉ **0,88 điểm
phần trăm**. Đổi một giả định nhỏ trong dự báo dòng tiền là kết luận lật. Đó đúng là
[mục 8](#8-phân-tích-độ-nhạy--sách-ra-bài-kiểm-ví-dụ-của-chính-sách-suýt-trượt): dự án này không còn chỗ
để sai.

### ⚠️ Ba giới hạn của phép so sánh này — phải nói rõ, không được làm ngơ

1. **ROA là tỷ suất KẾ TOÁN** *(lợi nhuận / tài sản)*, **IRR là tỷ suất TIỀN MẶT**. Chúng **không cùng đơn
   vị**. Đây là một **sàn dưới thô**, không phải ngưỡng đúng chuẩn.
2. **Ngưỡng đúng chuẩn của sách là WACC**, mà WACC đòi hỏi **chi phí vốn chủ sở hữu** — một con số **không
   có trong bất kỳ báo cáo tài chính nào**. Nó phải ước tính, và đó là một **giả định**, không phải một dữ
   kiện.
3. Doanh nghiệp ROA cao **không thể từ chối mọi dự án dưới ROA** — làm vậy thì không bao giờ mở rộng được.
   Sàn thật nằm **giữa WACC và ROA**.

Cái **đo được** từ báo cáo Vinamilk là về **nợ**, không phải về vốn chủ:

$$\text{chi phí lãi vay } 319.138 \;/\; \text{nợ vay } 10.442.325 = \mathbf{3{,}06\%/\text{năm}}$$

*(con số **gần đúng**: mẫu số gộp vay ngắn hạn và nợ dài hạn, tử số lấy từ báo cáo lưu chuyển tiền tệ)*. Đủ
để thấy một điều: **3,1% rất rẻ so với chi phí vốn chủ** — dùng mô hình 25/75 của ch. 24 thì vế vốn chủ áp
đảo.

> 🚧 **Việc còn mở:** **không tính được WACC của Vinamilk** vì không có chi phí vốn chủ sở hữu từ nguồn gốc.
> Ước nó cần hệ số beta và lãi suất phi rủi ro Việt Nam — hai con số không nằm trong báo cáo tài chính.
> **Đây là một lỗ hổng dữ liệu, không phải một kết luận.** Không gõ số từ báo chí.

---

## 12. 📚 Hộp công cụ — hướng dẫn từng bước viết một đề án

> *"Bạn đang nói chuyện với cấp trên về việc mua một thiết bị mới… Và cấp trên đột ngột kết thúc cuộc trò
> chuyện: **'Nghe được đấy. Về viết cho tôi một bản đề xuất có tính đến tỷ lệ hoàn vốn đầu tư, và nộp cho
> tôi chậm nhất là thứ Hai.'**"* — hộp công cụ · PDF tr. 189

Sách cho sáu bước. Rút gọn, kèm chỗ dễ hỏng nhất ở mỗi bước:

| bước | sách nói | chỗ dễ hỏng |
| :---: | --- | --- |
| 1 | Hiểu **ROI ở đây nghĩa là gì**: *"chỉ là một cách nói khác đi của câu: 'Hãy chuẩn bị một bản phân tích khoản mục chi phí đầu tư cơ bản này'"* | tưởng sếp hỏi một tỷ lệ, thật ra sếp hỏi cả một phân tích |
| 2 | **Thu thập mọi dữ liệu về chi phí**: giá mua, phí vận chuyển, phí lắp đặt, thời gian ngừng việc, thời gian khắc phục lỗi. *"Nếu phải đưa ra ước tính ở đâu, **hãy ghi chú lại**"* | chỉ lấy giá mua — [mục 10](#10--setpoint--bốn-câu-hỏi-của-người-kỹ-thuật-quy-ra-tiền) đo hậu quả |
| 3 | **Xác định lợi ích**: tiết kiệm từ tốc độ sản xuất, giảm chỉnh sửa, số nhân công, doanh thu tăng vì khách hài lòng | *"phần đòi hỏi sự khéo léo là biến tất cả thành **ước tính dòng tiền**"* |
| 4 | **Tìm ngưỡng thu hồi vốn của công ty** cho dạng đầu tư này, rồi tính NPV | [mục 7](#7-ngưỡng-thu-hồi-vốn-là-một-quyết-định-không-phải-một-phép-tính) — đây là bước quyết định kết quả |
| 5 | Tính **thời gian hoàn vốn và IRR** để phòng câu hỏi | ba phương pháp có thể cho ba câu trả lời khác nhau — [mục 9](#9-ba-phương-án-abc--và-con-số-sách-bỏ-ngỏ) |
| 6 | **Viết ngắn gọn**: mô tả, chi phí và lợi ích, **rủi ro**, mức phù hợp với chiến lược, rồi khuyến nghị | bỏ mục rủi ro |

Và sách đóng phần VI bằng một lời cảnh báo về **động cơ của chính người viết đề án**:

> *"Các nhà quản lý đôi khi **rất nhiệt tình** với ý tưởng viết đề xuất cho các dự án đầu tư cơ bản. Có lẽ
> đó là bản tính của con người: tất cả chúng ta đều thích những điều mới mẻ, và thường thì việc **đánh bóng
> các con số** để khoản đầu tư trông như thể hứa hẹn **khá dễ dàng**."* — hộp công cụ · PDF tr. 191

💼 Cách đọc nó cho đúng: **người viết đề án và người phê duyệt có động cơ khác nhau**, và người viết là
người chọn giả định. Đó là lý do sách bắt **ghi chú lại chỗ nào là ước tính** *(bước 2)* và **chạy phân tích
độ nhạy** *(bước 6)* — hai việc duy nhất khiến giả định trở nên **kiểm được từ bên ngoài**.

---

## 13. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py`](../thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py) rồi
chạy lại. Không có lời giải.

1. **Nghỉ hưu ở 9%.** Ở mục 2, thêm dòng 9% vào bảng giá trị tương lai. Chênh lệch 3% → 6% và 6% → 9% có
   bằng nhau không? Vì sao?

2. **WACC của doanh nghiệp vay nhiều.** Ở mục 3, đổi cơ cấu thành 75% nợ / 25% vốn chủ. WACC mới là bao
   nhiêu? Dự án của ch. 25 có vượt ngưỡng đó không? So với kết quả bài 8 mục 5 về đòn bẩy.

3. **Cặp dự án của riêng bạn.** Ở mục 4, dựng một cặp dự án có **cùng NPV** nhưng **thời gian hoàn vốn khác
   nhau**. Phương pháp nào phân biệt được chúng?

4. **Hoàn vốn chiết khấu ở ngưỡng cao.** Ở mục 5, đổi ngưỡng lên 14%. Thời gian hoàn vốn chiết khấu là bao
   nhiêu? Nó nói gì về quan hệ giữa hoàn vốn chiết khấu và IRR?

5. **Nội suy trên khoảng hẹp.** Ở mục 6, nội suy tuyến tính giữa NPV ở **14%** và **15%**. Kết quả gần IRR
   thật đến đâu? Sai số giảm bao nhiêu lần so với khoảng 10–20%?

6. **Ngưỡng làm dự án chết.** Ở mục 7, tìm ngưỡng làm NPV bằng **−500**. Nó cách IRR bao xa? Vẽ quan hệ NPV
   theo ngưỡng — nó có phải đường thẳng không?

7. **Độ nhạy hai chiều.** Ở mục 8, giảm dòng tiền **và** tăng vốn đầu tư cùng lúc, mỗi cái 5%. NPV còn bao
   nhiêu? Vì sao hai sai số nhỏ lại nguy hiểm hơn tổng của chúng?

8. **Dự án chịu được 80%.** Vẫn mục 8, dòng tiền mỗi năm phải là bao nhiêu để dự án **vẫn qua** ở mức 80%
   phỏng đoán? IRR khi đó là bao nhiêu?

9. **Phương án D.** Ở mục 9, thêm một phương án trả về 1.800 đô-la ở cuối năm 2 và 1.800 ở cuối năm 3.
   Hoàn vốn, NPV, IRR là bao nhiêu? Nó xếp thứ mấy theo từng phương pháp?

10. **Điểm hoà B–C ở dòng tiền khác.** Vẫn mục 9, đổi phương án B thành 3.400 đô-la. Tỷ suất tái đầu tư hoà
    B với C dịch đến đâu? Nó **tăng hay giảm**, và vì sao?

11. **Thiết bị Setpoint tuổi đời 10 năm.** Ở mục 10, đổi tuổi đời từ 5 lên 10 năm. Yêu cầu mỗi tháng giảm
    bao nhiêu phần trăm? Nếu bạn là người phê duyệt, bạn tin con số tuổi đời nào hơn?

12. **Sàn của Vinamilk.** Ở mục 11, giả sử chi phí vốn chủ sở hữu của Vinamilk là 12% và cơ cấu vốn theo
    đúng bảng cân đối 2024. WACC ra bao nhiêu? Dự án 14,36% giờ **được nhận hay bị loại**? Kết quả nhạy
    thế nào với con số 12% mà bạn vừa **bịa ra**?

---

## 14. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Chi phí đầu tư cơ bản | capital expenditure | *"những dự án lớn, đòi hỏi phải đầu tư lượng tiền mặt đáng kể"* |
| Ngân sách vốn | capital budgeting | quá trình quyết định rót vốn vào đâu |
| Tỷ lệ hoàn vốn đầu tư | return on investment (ROI) | ở ch. 25 nghĩa là **cả một bản phân tích**, không phải một tỷ lệ |
| Giá trị tương lai | future value | một khoản tiền hôm nay sẽ thành bao nhiêu — [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md) |
| Giá trị hiện tại | present value | chiều ngược lại — [EG14 bài 5](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md) |
| Giá trị hiện tại thuần | net present value (NPV) | PV − vốn ban đầu. **> 0 thì nhận** |
| Tỷ suất sinh lợi nội bộ | internal rate of return (IRR) | *"ngưỡng thu hồi vốn làm cho NPV bằng 0"* |
| **Thời gian hoàn vốn** | payback period | vốn / dòng tiền mỗi năm. **Không** tính giá trị thời gian |
| 💼 **Thời gian hoàn vốn chiết khấu** | discounted payback | chiết khấu trước rồi mới cộng dồn — **không có trong sách** |
| **Ngưỡng thu hồi vốn** | hurdle rate / required rate of return | *"phán đoán – hay giả định"*, không phải phép tính |
| **Chi phí sử dụng vốn** | cost of capital (WACC) | trung bình có trọng số của chi phí nợ và chi phí vốn chủ |
| Chi phí cơ hội | opportunity cost | *"những gì bạn phải từ bỏ"* — nguyên lý 2 của EG13 |
| **Phân tích độ nhạy** | sensitivity analysis | chạy lại ở **80–90%** phỏng đoán và xem còn hợp lý không |
| 💼 Biên an toàn | margin of safety | NPV / vốn ban đầu — **không có trong sách** |

---

## 15. Câu hỏi tự kiểm tra

1. Vì sao bài này mỏng? Bốn thứ nào **chỉ** có ở đây? (mục 1)
2. Sách nói gì về việc chuyên gia tài chính *"định lượng những con số không biết"*? (mục 1)
3. Kể **năm** khối đá của chương 24. (mục 2)
4. 50.000 đô-la sau 30 năm ở 3% và ở 6% là bao nhiêu? Chênh mấy lần? (mục 2)
5. Sách dùng ví dụ nghỉ hưu để nói về điều gì? (mục 2)
6. Cặp số 102.000 / 120.000 minh hoạ khái niệm nào? (mục 2)
7. Viết công thức WACC của ví dụ ch. 24 và giải ra 13%. (mục 3)
8. Vì sao vốn chủ sở hữu **đắt gấp bốn lần** vay nợ trong ví dụ đó? (mục 3)
9. Lãi suất 4% trong ví dụ WACC là trước hay sau thuế? Vì sao điều đó quan trọng? (mục 3)
10. Phát biểu **luật** mà ch. 24 hạ về quan hệ giữa ngưỡng và WACC. (mục 3)
11. Tính thời gian hoàn vốn của ví dụ chủ đạo. Bài kiểm thứ nhất của sách là gì? (mục 4)
12. Kể **ba nhược điểm** của phương pháp thời gian hoàn vốn. (mục 4)
13. Dựng một cặp dự án cùng thời gian hoàn vốn nhưng NPV lệch hẳn. (mục 4)
14. Thời gian hoàn vốn **chiết khấu** của ví dụ là bao nhiêu? Dài hơn bao nhiêu phần trăm? (mục 5)
15. Vì sao biên an toàn thật *"bớt một nửa"*? (mục 5)
16. Hoàn vốn chiết khấu sửa được nhược điểm nào, và **không** sửa được nhược điểm nào? (mục 5)
17. PV, NPV và IRR của ví dụ chủ đạo là bao nhiêu? (mục 6)
18. Hai chỗ nào sách in sai trong đoạn giải thích IRR? Kết luận của sách có hỏng không? (mục 6)
19. Vì sao **không** nội suy tuyến tính được giữa hai NPV để tìm IRR? (mục 6)
20. Vì sao ngưỡng thu hồi vốn là **quyết định** chứ không phải phép tính? (mục 7)
21. Doanh nghiệp tăng trưởng cao dùng ngưỡng cao hay thấp? Vì sao? (mục 7)
22. Cùng chiếc máy đó, ở ngưỡng 4% / 13% / 20% thì NPV bao nhiêu và quyết định là gì? (mục 7)
23. Ngưỡng 8% của ch. 25 **hàm ý** gì về WACC của doanh nghiệp đó? Vì sao đây **không** phải lỗi? (mục 7)
24. Sách bảo chạy phân tích độ nhạy ở mức nào? (mục 8)
25. Điểm hoà vốn của ví dụ chủ đạo nằm ở bao nhiêu phần trăm dòng tiền dự báo? (mục 8)
26. Ví dụ của sách **qua hay trượt** bài kiểm độ nhạy của chính sách? (mục 8)
27. Hai con số nào nên đọc kèm NPV, và mỗi cái nói gì? (mục 8)
28. Ba phương pháp cho ba người thắng nào trong ví dụ A/B/C? (mục 9)
29. Vì sao NPV chọn C dù IRR của B cao hơn? (mục 9)
30. Tái đầu tư ở **bao nhiêu** thì B thắng C? Sách có đưa con số này không? (mục 9)
31. Giả định âm thầm của NPV về tái đầu tư là gì? (mục 9)
32. Kể **bốn câu hỏi** của người kỹ thuật ở Setpoint, và mỗi câu ứng với bước nào. (mục 10)
33. Thiết bị 80.000 đô-la phải mang về bao nhiêu **mỗi tháng** chỉ để hoà vốn? (mục 10)
34. Vì sao câu hỏi về **chi phí lao động** giết chết đề xuất? (mục 10)
35. Cùng một dự án IRR 14,36%, vì sao công ty mẫu nhận còn Vinamilk loại? (mục 11)
36. Kể **ba giới hạn** của phép so sánh IRR với ROA. (mục 11)
37. Vì sao **không** tính được WACC của Vinamilk từ báo cáo tài chính? (mục 11)
38. Kể sáu bước viết đề án của hộp công cụ. (mục 12)
39. Sách cảnh báo gì về **động cơ của chính người viết đề án**? (mục 12)
40. Hai việc nào khiến giả định trở nên **kiểm được từ bên ngoài**? (mục 12)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 10 — TÍNH TỶ LỆ HOÀN VỐN ĐẦU TƯ                                     ║
║           (ch. 24–25 + hộp công cụ Phần VI, PDF tr. 172–191)             ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⚠️ BÀI NÀY CỐ TÌNH MỎNG. NPV / IRR / chiết khấu → EG14 bài 5.           ║
║     Chỉ có ở đây: THỜI GIAN HOÀN VỐN · NGƯỠNG THU HỒI VỐN ·              ║
║                   CHI PHÍ SỬ DỤNG VỐN · PHÂN TÍCH ĐỘ NHẠY                ║
║     Bốn thứ này KHÔNG phải kỹ thuật chiết khấu — chúng bao quanh nó:     ║
║     lấy số ở đâu, chọn ngưỡng nào, tin kết quả đến mức nào.              ║
║                                                                          ║
║  BA (thật ra NĂM) KHỐI ĐÁ CỦA CH. 24                                     ║
║     giá trị tương lai · giá trị hiện tại · tỷ suất sinh lợi yêu cầu      ║
║     + chi phí cơ hội (= nguyên lý 2 EG13) + chi phí sử dụng vốn          ║
║     50.000 sau 30 năm:  @3% → 121.363   @6% → 287.175   GẤP 2,37 LẦN     ║
║     WACC = 25%×4% + 75%×16% = 13%.  Vốn chủ ĐẮT GẤP BỐN LẦN vay nợ.      ║
║     LUẬT: "tỷ suất yêu cầu LUÔN phải cao hơn chi phí sử dụng vốn"        ║
║                                                                          ║
║  VÍ DỤ CHỦ ĐẠO: máy 3.000 $, 3 năm, 1.300 $/năm, ngưỡng 8%               ║
║     hoàn vốn 2,31 năm · PV 3.350 · NPV 350 · IRR 14,36%  (khớp sách)     ║
║                                                                          ║
║  ⭐ HOÀN VỐN CHIẾT KHẤU — CON SỐ SÁCH KHÔNG ĐƯA                          ║
║     2,66 năm thay vì 2,31 (dài hơn 15%).                                 ║
║     Biên an toàn thật 0,34 năm, KHÔNG PHẢI 0,69. Bớt một nửa.            ║
║     Nhưng vẫn mù tịt với mọi thứ SAU khi hoàn vốn.                       ║
║     X = [1300,1700,0] và Y = [1300,1700,4000]: CÙNG hoàn vốn 2,00 năm,   ║
║     NPV −339 vs +2.837. Một cái LOẠI, một cái NHẬN.                      ║
║                                                                          ║
║  ⚠️ HAI CHỖ SÁCH IN SAI (tr. 186): NPV @10% = 212 → 233                  ║
║                                     NPV @20% = −218 → −262               ║
║     Kết luận "IRR nằm trong 10–20%" và con số 14,36% thì ĐÚNG.           ║
║     💼 Nội suy tuyến tính KHÔNG cho ra IRR: 14,93% / 14,71% vs 14,36%    ║
║                                                                          ║
║  ⭐ NGƯỠNG LÀ MỘT QUYẾT ĐỊNH, KHÔNG PHẢI PHÉP TÍNH                       ║
║     cùng chiếc máy:  @4% NPV 608  ·  @8% 350  ·  @13% 69  ·  @20% −262   ║
║     "nên mua" hay "đừng mua" được quyết ở CH. 24, bởi MỘT NGƯỜI.         ║
║     ⚠️ ch.24 tính WACC 13%, ch.25 dùng ngưỡng 8% → hai DN khác nhau.     ║
║                                                                          ║
║  ⭐ SÁCH RA BÀI KIỂM ĐỘ NHẠY 80–90%, VÍ DỤ CỦA CHÍNH SÁCH SUÝT TRƯỢT     ║
║     điểm hoà vốn = 89,55% dòng tiền dự báo                               ║
║        @90% → NPV +15  (vừa đủ)      @80% → NPV −320  (TRƯỢT)            ║
║     NPV 350 nghe vững, đổi ra tỷ lệ chỉ là 11,7% VỐN. Lệch 10,5% là hết. ║
║     💼 đọc kèm: NPV/vốn = 11,7%  ·  IRR − ngưỡng = 6,36 điểm             ║
║                                                                          ║
║  ⭐ A/B/C — CẢ CHÍN CON SỐ CỦA SÁCH ĐỀU KHỚP                             ║
║     hoàn vốn → B  ·  IRR → B (20%)  ·  NPV → C (552)   NPV thắng         ║
║     sách kiểm tái đầu tư @9%: 3.600×1,09² = 4.277 < 4.600 ✓              ║
║     ⭐ SÁCH DỪNG Ở ĐÓ. Điểm hoà: √(4600/3600) − 1 = 13,04%               ║
║        Trên 13,04% thì B THẮNG. Kết luận của sách đúng — trong giả định. ║
║                                                                          ║
║  💼 SETPOINT: máy 80.000 $, 5 năm, 9% → phải về 1.714 $/THÁNG để hoà vốn ║
║     thêm 1 người vận hành 3.000 $/tháng → phải về 4.714 $, GẤP 2,75 LẦN  ║
║     Người kỹ thuật không tính NPV. Ông chỉ không để sót đồng nào.        ║
║                                                                          ║
║  🇻🇳 CÙNG DỰ ÁN IRR 14,36%, HAI QUYẾT ĐỊNH NGƯỢC NHAU                     ║
║     công ty mẫu ROA 4,78% → NHẬN   ·   Vinamilk ROA 15,24% → LOẠI        ║
║     sát nút: chỉ 0,88 ĐIỂM. Đó chính là chi phí cơ hội, bằng số.         ║
║     ⚠️ ROA là tỷ suất KẾ TOÁN, IRR là tỷ suất TIỀN MẶT — sàn THÔ.        ║
║     🚧 không tính được WACC Vinamilk: thiếu chi phí vốn chủ sở hữu.      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần VI — Hướng dẫn cách tính toán (và thật sự hiểu) tỷ lệ hoàn vốn đầu tư**, trang tiêu đề PDF
    tr. 170–171
    - Ch. 24 *Những khối đá làm nên tỷ lệ hoàn vốn đầu tư*, PDF tr. 172–178
      — giá trị tiền tệ theo thời gian (tr. 172–173); **giá trị tương lai** và ⭐ ví dụ nghỉ hưu 3% / 6%
      (tr. 174); **giá trị hiện tại** — ví dụ 106.000 → 100.000 (tr. 175); ⭐ **tỷ suất sinh lợi yêu cầu**,
      cặp 102.000 / 120.000 và ⭐ **luật** *"tỷ suất yêu cầu luôn phải cao hơn chi phí sử dụng vốn"*
      (tr. 175–176); ⭐ **chi phí cơ hội** và *"ngưỡng thu hồi vốn hiếm khi là vấn đề thực hiện công thức"*
      (tr. 177); ⭐ **chi phí sử dụng vốn** — WACC 13% (tr. 178)
    - Ch. 25 *Tính tỷ lệ hoàn vốn đầu tư*, PDF tr. 179–189
      — thuật ngữ *chi phí đầu tư cơ bản* (tr. 179); ⭐ *"một bài luyện nghệ thuật tài chính"* (tr. 180);
      **ba bước** phân tích (tr. 180–181); ví dụ chủ đạo máy tính 3.000 đô-la (tr. 181); ⭐ **thời gian
      hoàn vốn** 2,31 năm và **ba nhược điểm** (tr. 182); *"quy tắc mang tính kinh nghiệm dạng thô sơ"*
      (tr. 183); **NPV** — phương trình khấu trừ, PV 3.350, NPV 350 (tr. 184); quan hệ lãi suất ↔ NPV
      (tr. 185); **IRR** — ⚠️ NPV in sai ở 10% và 20%, IRR 14,36%, vấn đề quy mô (tr. 186); ⭐ **so sánh
      ba phương pháp** — ba phương án A/B/C và NPV (tr. 187); IRR 0/20/15,3%, ⚠️ *"cao hơn phương án C"*,
      giả định tái đầu tư, và ⭐ **phân tích độ nhạy 80–90%** (tr. 188); 💼 **Setpoint và bốn câu hỏi của
      người kỹ thuật** (tr. 189)
    - **Hộp công cụ Phần VI** *Hướng dẫn từng bước để phân tích các khoản mục chi phí đầu tư cơ bản*,
      PDF tr. 189–191 — mở đầu *"chậm nhất là thứ Hai"* (tr. 189); sáu bước viết đề án (tr. 190); ⭐ cảnh
      báo về *"đánh bóng các con số"* và lời dặn chạy phân tích độ nhạy (tr. 191)
- **Đại học Yale / Mankiw** — hai môn đã học trong kho, dùng thay cho phần sách trùng lặp:
  - [EG14 bài 5 — *Các công cụ cơ bản của tài chính*](../../../houedu/eg14-kinhtevimo-macro/ly_thuyet/bai_05_cong_cu_co_ban_cua_tai_chinh.md)
    — giá trị hiện tại, chiết khấu, lãi kép, rủi ro và sinh lợi
  - [EG13 bài 1 — *Mười nguyên lý và tư duy kinh tế*](../../../houedu/eg13-kinhtevimo-micro/ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)
    — chi phí cơ hội *(nguyên lý 2)* và chi phí chìm
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 11](#11--cùng-một-dự-án-hai-doanh-nghiệp-hai-quyết-định-ngược-nhau).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py`](../thuc_hanh/bai-10-tinh-ty-le-hoan-von-dau-tu.py):
  - giá trị tương lai 50.000 đô-la sau 30 năm ở 3% và 6% ra **121.363** và **287.175** — chốt bằng `assert`;
  - 106.000 / 1,06 = **100.000** đúng đến từng đồng — chốt bằng `assert`;
  - WACC = **13%** — chốt bằng `assert`;
  - thời gian hoàn vốn = **2,31 năm** — chốt bằng `assert`;
  - cặp X/Y có **cùng** thời gian hoàn vốn nhưng một NPV âm và một NPV dương, lệch **hơn cả vốn đầu tư** —
    chốt bằng `assert`;
  - hoàn vốn chiết khấu **dài hơn** hoàn vốn thô, và biên an toàn còn lại **chưa tới một nửa** — chốt bằng
    `assert`;
  - PV **3.350**, NPV **350**, IRR **14,36%** — cả ba khớp sách, chốt bằng `assert`;
  - NPV ở 10% và 20% ra **233** và **−262**, **không** phải 212 và −218 như sách in — chốt bằng `assert`;
  - nội suy tuyến tính **luôn vọt quá** IRR thật, với cả hai bộ số — chốt bằng `assert`;
  - ở ngưỡng WACC 13%, NPV vẫn dương nhưng **nhỏ hơn hẳn** ở ngưỡng 8% — chốt bằng `assert`;
  - điểm hoà vốn độ nhạy nằm **trong khoảng 80–90%** mà sách bảo phải kiểm — chốt bằng `assert`;
  - **cả chín** con số A/B/C của sách *(3 hoàn vốn, 3 NPV, 3 IRR)* đều khớp — chốt bằng `assert`;
  - tái đầu tư 3.600 ở 9% trong 2 năm **nhỏ hơn** 4.600, và điểm hoà nằm **giữa 9% và IRR của B** — chốt
    bằng `assert`;
  - dòng tiền niên kim cần thiết cho thiết bị Setpoint làm NPV **bằng đúng 0** — chốt bằng `assert`;
  - IRR của dự án nằm **giữa** ROA của công ty mẫu và ROA của Vinamilk — chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** cặp dự án X/Y ở mục 4; toàn bộ mục 5 *(thời gian hoàn
  vốn chiết khấu — sách chỉ nêu nhược điểm bằng lời)*; phép nội suy tuyến tính ở mục 6; dải ngưỡng
  4–20% ở mục 7; điểm hoà vốn 89,55% và hai chỉ số *biên an toàn* / *khoảng hở tỷ suất* ở mục 8; tỷ suất
  tái đầu tư hoà B–C 13,04% ở mục 9; tuổi đời 5 năm, ngưỡng 9% và mức lương người vận hành ở mục 10; phép
  so IRR với ROA ở mục 11. Mọi con số **của sách** đều được trích kèm mốc `ch. N · PDF tr. M`.

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
| **10** | **Tính tỷ lệ hoàn vốn đầu tư** ← *bạn đang ở đây* | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
