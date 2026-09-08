# Thị trường Tài chính — Yale ECON 252

Bộ bài học tiếng Việt dựng **từ chính phụ đề gốc của video**, không viết theo trí nhớ.

**Nguồn:** khoá **Yale ECON 252 *Financial Markets*, Xuân 2011** — giảng viên **Prof. Robert J.
Shiller**, Nobel Kinh tế 2013. **23 buổi giảng, mỗi buổi ~63–78 phút, tổng ~27 giờ 51 phút.**
Kênh **YaleCourses** trên YouTube · Open Yale Courses, giấy phép **CC BY-NC-SA**.

- Playlist: <https://www.youtube.com/playlist?list=PL8FB14A2200B87185>
- Trang khoá học OYC: <https://oyc.yale.edu/economics/econ-252>
- Giáo trình Shiller giao (`01 15:14`–`15:47`): **Fabozzi, Modigliani & Jones, *Foundations of
  Financial Markets and Institutions*** — Shiller nói thẳng Modigliani là **thầy hướng dẫn luận án
  của ông ở MIT**, mất năm 2003. Đọc thêm: **Shiller, *Finance and the Good Society***.

> ⚠️ **Khoá này ghi Xuân 2011** — hai năm rưỡi sau khi Lehman sụp, khi Dodd-Frank vừa ký mà chưa thi
> hành và Basel III còn là bản thảo. Mỗi bài đều có mục ⚠️ **đối chiếu 2026** cho những chỗ thời
> gian đã bác bỏ.

---

## Khoá này KHÔNG phải khoá định giá

Đây là điểm phải nắm trước khi đọc dòng nào. Shiller mở đầu buổi 1 (`01 00:47`):

> *"Nó nói về xã hội chúng ta. Bạn có thể tưởng đây là khoá về giao dịch, vì tên có chữ 'thị
> trường', nhưng nó rộng hơn thế. Tài chính, theo tôi, đúng như mô tả khoá học nói, là **một trụ
> cột của xã hội văn minh**."* (`01 00:59`–`01:03`)

Rồi ông định nghĩa (`01 01:13`): tài chính là việc **phân bổ nguồn lực qua không gian và thời
gian**, tạo động lực cho người ta làm việc có ích, và **bảo đảm người ta được đối xử công bằng**.

Cái vế thứ ba mới là chỗ khoá này khác. Nó là khoá về **định chế** — ai đứng ở đâu trong hệ thống,
cơ quan nào giám sát ai, và vì sao hệ thống sập. Không phải khoá về *"cái này đáng bao nhiêu"*.

📐 **Nửa còn lại nằm ở kho bên cạnh:** [MIT 15.401 *Finance Theory I*](../mit-15401-finance/README.md)
của Andrew Lo là khoá **định giá** — chiết khấu, trái phiếu, quyền chọn, danh mục, CAPM, WACC. Hai
khoá gần như không đè lên nhau; đọc cạnh nhau thì thành một bộ đủ. Toàn bộ phân tích độ phủ, đối
chiếu từng buổi, ở [tai_lieu/gom-nhom.md](tai_lieu/gom-nhom.md).

---

## Cách đọc

| Ký hiệu | Nghĩa |
| --- | --- |
| `13 41:06` | **buổi 13, phút 41:06** — mọi mốc đều đã đối chiếu ngược với phụ đề gốc bằng script |
| `12 ch5` | buổi 12 chỉ trích được ở **cấp chương** — xem cảnh báo dưới |
| 📚 **Mở rộng** | kiến thức video lướt qua, hoặc phần bài học này bổ sung — **không có trong video** |
| 🇻🇳 **Góc Việt Nam** | số liệu và ví dụ trong nước — **không có trong video** |
| ⚠️ | chỗ dễ hiểu sai, chỗ video nói sai, hoặc chỗ thực tế sau 2011 đã bác lại |
| 💡 **Tự thử** | bài tập sửa tham số rồi quan sát, **không kèm lời giải** |

Công thức viết bằng LaTeX. Mở bằng **Obsidian** (hoặc VS Code + Markdown Preview Enhanced).

Code thực hành viết bằng **Python 3.10+ thuần**, không thư viện ngoài — **giống hệt quy ước của
[MIT 15.401](../mit-15401-finance/README.md)**, để hai kho dùng chung được hạ tầng vẽ hình và bộ
kiểm output. Chạy bằng `python3 <tên-file>.py`. Kết quả **tất định**.

---

## Sáu thứ hỏng trong nguồn — đã kiểm, đừng vấp lại

### 1. Tiêu đề buổi 8 nói sai nội dung của chính nó

YouTube đặt tên buổi 8 là *"Theory of Debt, Its Proper Role, **Leverage Cycles**"*. Trong toàn bộ
transcript buổi 8, từ `leverage` xuất hiện **0 lần**. Buổi 8 thật ra dạy lý thuyết quyết định lãi
suất, giá trị hiện tại, lãi suất kỳ hạn, lịch sử cho vay nặng lãi, và Cục Bảo vệ Tài chính Người
tiêu dùng.

**Chu kỳ đòn bẩy không nằm trong khoá này.** Nó là của Geanakoplos, Yale ECON 251, và đã viết rồi ở
[bài 20 của MIT 15.401](../mit-15401-finance/ly_thuyet/bai_20_chu_ky_don_bay.md).

⛔ Đặt tên bài tiếng Việt theo **chương**, không theo tiêu đề YouTube.

### 2. Buổi 12 không có phụ đề người viết

Bản `.en.vtt` của buổi 12 là máy nghe — timing từng từ, mở đầu ra `"Today we Rules, real Rules in"`.
22 buổi còn lại đều là phụ đề người viết, sạch. Buổi 12 dùng transcript Open Yale Courses cho câu
chữ và **chỉ trích mốc ở cấp chương** (8 mốc). Cổng kiểm mốc phải chừa buổi 12 ra.

✅ Mốc chương OYC dùng thẳng được. Đo trên **47 chương** thuộc 7 buổi: mốc OYC và mốc phụ đề YouTube
lệch nhau **trung vị 0 giây, biên độ ±4 giây**. Nên buổi 12 vẫn trích được 8 mốc chính xác, chỉ là
thô hơn — không có mốc giữa chương.

### 3. Hơn nửa buổi 19 không phải bài giảng

Shiller giảng ngân hàng đầu tư từ `00:00` đến `33:04`. Ba mươi tám phút còn lại là **Jon Fougner**,
cựu sinh viên chính lớp này, kể chuyện từ Wall Street sang Facebook. Nội dung ngân hàng đầu tư thật
chỉ **~33 phút**.

### 4. Mốc vượt 60 phút trên trang OYC ghi dạng `hh:mm:ss`

`[01:07:42]`, không phải `[07:42]`. Cắt nhầm phần giờ thì **17 mốc** trong khoá sai. Đã sửa khi sinh
mục lục chương.

### 5. Cổng kiểm mốc phải có dung sai ±5 giây

Cổng kiểm của [MIT 15.401](../mit-15401-finance/README.md) đối chiếu mốc **chính xác tuyệt đối** —
hợp lý ở đó, vì mọi mốc đều lấy từ chính phụ đề. Ở kho này thì không dùng được: mốc lấy từ chương
OYC lệch phụ đề YouTube 1–4 giây, nên khớp tuyệt đối sẽ báo sai hàng loạt mốc **đúng**.

Ví dụ thật: chương 6 của buổi 13 bắt đầu ở `41:07` theo OYC, nhưng dòng phụ đề gần nhất nằm ở
`41:06`. Cả hai đều đúng.

**Luật:** script kiểm mốc phải tìm dòng phụ đề trong **cửa sổ ±5 giây** và in ra dòng khớp để đọc
bằng mắt, chứ không tra khoá chính xác.

### 6. Bài gộp nhiều buổi phải kiểm mốc RIÊNG từng buổi

Bài 2 lấy từ buổi 5 và buổi 14. Nếu gộp phụ đề hai buổi vào một bảng rồi dò, script sẽ báo "đúng"
cho một mốc thực ra thuộc **buổi kia**. Ví dụ thật, cùng mốc `34:52`:

| Buổi | Câu ở `34:52` |
| --- | --- |
| 5 | *"But, of course, Goldman Sachs was not being bailed out."* |
| 14 | *"sold as a CDO --"* |

**Luật:** tách phụ đề theo buổi, dò mốc `05 mm:ss` chỉ trong buổi 5 và `14 mm:ss` chỉ trong buổi 14.
Script kiểm của bài 2 còn báo thêm *"mốc này thuộc buổi kia!"* khi bắt được trường hợp đó.

---

## Lộ trình 13 bài

23 buổi được gom thành 13 bài **theo ranh giới chủ đề**. Lưới từ khoá trên transcript thật cho thấy
khoá này rất mô-đun: bảo hiểm nhắc 244 lần và gần như chỉ ở buổi 5; sở giao dịch 248 lần và chỉ ở
buổi 21. Nên gom chủ yếu là **ghép buổi khách mời vào đúng bài chủ đề**.

`⭐` = **MIT 15.401 hoàn toàn không có**. Mười trên mười ba bài là như vậy.

### Phần A — Khung

| # | Bài | Buổi | Trạng thái |
| ---: | --- | --- | --- |
| 1 | ⭐ [**Tài chính là hạ tầng xã hội**](ly_thuyet/bai_01_ha_tang_xa_hoi.md) — phát minh, trách nhiệm hữu hạn, gắn chỉ số lạm phát | 1 + 3 | ✅ |

### Phần B — Định chế gánh rủi ro

| # | Bài | Buổi | Trạng thái |
| ---: | --- | --- | --- |
| 2 | ⭐ [**Bảo hiểm** — gộp rủi ro, và ba chỗ nó gãy](ly_thuyet/bai_02_bao_hiem.md) | 5 + **14 (Hank Greenberg, cựu CEO AIG)** | ✅ |
| 3 | ⭐ [**Ngân hàng** — thanh khoản, lựa chọn ngược, bank run, Basel](ly_thuyet/bai_03_ngan_hang.md) | 13 | ✅ |
| 4 | ⭐ [**Chính sách tiền tệ và ngân hàng trung ương**](ly_thuyet/bai_04_chinh_sach_tien_te.md) | 18 | ✅ |
| 5 | ⭐ [**Ngân hàng đầu tư, shadow banking và repo**](ly_thuyet/bai_05_ngan_hang_dau_tu.md) | 19 (ch1–4) | ✅ |

### Phần C — Nơi giao dịch xảy ra

| # | Bài | Buổi | Trạng thái |
| ---: | --- | --- | --- |
| 6 | ⭐ [**Sở giao dịch, môi giới, dealer, HFT**](ly_thuyet/bai_06_so_giao_dich.md) | 21 | ✅ |
| 7 | ⭐ [**Nhà quản lý quỹ và nghĩa vụ tín thác**](ly_thuyet/bai_07_quan_ly_quy.md) | 20 + **6 (David Swensen, CIO Yale)** | ✅ |
| 8 | ⭐ [**Cổ phiếu nhìn từ góc định chế**](ly_thuyet/bai_08_co_phieu_dinh_che.md) | 9 | ✅ |

### Phần D — Tài sản và luật chơi

| # | Bài | Buổi | Trạng thái |
| ---: | --- | --- | --- |
| 9 | ⭐ [**Bất động sản** — từ quyền tài sản tới MBS](ly_thuyet/bai_09_bat_dong_san.md) | 10 | ✅ |
| 10 | ⭐ [**Quy định, tự quản, và hành vi sai trái**](ly_thuyet/bai_10_quy_dinh_tu_quan.md) — năm tầng, năm cửa thoát, con lắc của Laura Cha | 12 + **16 (Laura Cha, cựu phó CT UBCK Trung Quốc)** | ✅ |
| 11 | ⭐ [**Tài chính công và phi lợi nhuận**](ly_thuyet/bai_11_tai_chinh_cong.md) — ngân sách vốn, Bismarck, công nghệ thông tin | 22 | ✅ |

### Phần E — Con người

| # | Bài | Buổi | Trạng thái |
| ---: | --- | --- | --- |
| 12 | [**Tài chính hành vi** — Shiller phản biện Lo](ly_thuyet/bai_12_tai_chinh_hanh_vi.md) | 11 | ✅ |
| 13 | ⭐ [**Mục đích, đạo đức, dân chủ hoá tài chính**](ly_thuyet/bai_13_muc_dich_dao_duc.md) — bài giảng kết | 23 + 19 (ch5–8) | ✅ |

> 🥊 **Bài 12 cố ý mâu thuẫn với kho bên cạnh.**
> [Bài 13 của MIT 15.401](../mit-15401-finance/ly_thuyet/bai_13_thi_truong_hieu_qua.md) đã dạy hành
> vi, nhưng qua lăng kính **adaptive markets của Andrew Lo**. Shiller đi hướng khác hẳn: lý thuyết
> triển vọng, lý thuyết hối tiếc, quá tự tin, bất hoà nhận thức, neo, lan truyền xã hội. Hai người
> mâu thuẫn thật, và đó là thứ đáng giá nhất khi đọc hai khoá cạnh nhau — nên bài này **đứng riêng**
> chứ không vá vào.

> 🎯 **Bài 13 là chỗ Shiller đặt luận điểm riêng của ông.** *"Dân chủ hoá tài chính là cố đưa nó
> vượt ra khỏi tầng lớp tinh hoa […] **Bất bình đẳng phần lớn đến từ việc không quản trị được rủi
> ro.**"* (`23 50:47`–`51:13`). Đây là câu nối thẳng khoá học vào ngành quản trị kinh doanh.

---

## Sáu miếng vá sang MIT 15.401

Sáu buổi còn lại trùng chủ đề với 15.401, và **Lo dạy phần toán kỹ hơn nhiều lần**. Nên chỉ lấy phần
lịch sử, giai thoại và phản biện, vá vào bài MIT tương ứng dưới dạng `###`.

| Buổi | Phần đáng lấy | Vá vào |
| --- | --- | --- |
| 2 | thất bại của giả định độc lập; đuôi béo, phân phối Cauchy | [bai_09 rủi ro và lợi suất](../mit-15401-finance/ly_thuyet/bai_09_rui_ro_va_loi_suat.md) |
| 4 | Công ty Đông Ấn Hà Lan, sàn Amsterdam; câu đố phần bù vốn cổ phần | [bai_10 lý thuyết danh mục](../mit-15401-finance/ly_thuyet/bai_10_ly_thuyet_danh_muc.md) |
| 7 | thao túng tỷ số Sharpe; phân tích kỹ thuật và mẫu vai-đầu-vai | [bai_13 thị trường hiệu quả](../mit-15401-finance/ly_thuyet/bai_13_thi_truong_hieu_qua.md) |
| 8 | lịch sử cho vay nặng lãi; Elizabeth Warren và CFPB | [bai_04 trái phiếu và đường cong](../mit-15401-finance/ly_thuyet/bai_04_trai_phieu_va_duong_cong.md) |
| 15 | chợ gạo Dojima; contango và backwardation; lịch sử thị trường dầu | [bai_07 kỳ hạn và tương lai](../mit-15401-finance/ly_thuyet/bai_07_ky_han_va_tuong_lai.md) |
| 17 | chỉ số VIX; quyền chọn cho thị trường nhà ở | [bai_08 quyền chọn](../mit-15401-finance/ly_thuyet/bai_08_quyen_chon.md) |

⚠️ Dùng `###`, **không** thêm `##` mới — sẽ lệch mục lục và mọi tham chiếu `[phần N]` trong bài MIT.

---

## Nên học môn này thế nào

**1. Có đề thi. Dùng nó.** Open Yale Courses công bố cả ba đề của chính khoá này:
[Midterm 1](https://oyc.yale.edu/economics/econ-252-11/exam-1) ·
[Midterm 2](https://oyc.yale.edu/economics/econ-252-11/exam-2) ·
[Final](https://oyc.yale.edu/economics/econ-252-11/exam-3). Học thụ động 28 giờ rồi tự thấy "hiểu
rồi" là ảo giác; làm đề thì lộ ngay chỗ hổng.

**2. Đọc transcript trước, xem video sau.** Mỗi buổi có transcript đầy đủ trên trang OYC. Shiller
nói lan man và hay rẽ ngang; biết trước cấu trúc thì xem đỡ mệt và tua được.

**3. Mỗi bài hỏi đúng một câu: *cơ chế này sập kiểu gì?*** Khoá này không dạy công thức, nó dạy
định chế. Định chế nào cũng có chỗ gãy, và Shiller luôn chỉ ra chỗ đó — bảo hiểm gãy khi rủi ro hết
độc lập, ngân hàng gãy khi niềm tin mất, sở giao dịch gãy khi tốc độ vượt giám sát. Nắm chỗ gãy thì
nhớ được cả bài.

**4. Ba buổi khách mời xem sau bài lý thuyết tương ứng**, không xem theo số thứ tự. Nghe Greenberg
nói về rủi ro *sau khi* đã học chương AIG của buổi 5 thì khác hẳn nghe trước.

**5. Ôn thì đọc "Tóm tắt một trang" của từng bài**, không đọc lại cả bài.

---

## Vì sao khoá này hợp với quản trị kinh doanh

15.401 hợp với người làm **đầu tư**. ECON 252 hợp với người làm **quản trị**, vì nó chính là những
học phần mà chương trình QTKD dạy rời rạc rồi không ai nối lại: bảo hiểm, ngân hàng thương mại, thị
trường chứng khoán, quản trị rủi ro, tài chính công. Shiller nối chúng bằng đúng một sợi — **mọi
định chế tài chính đều là một cách gộp và chuyển rủi ro, và mỗi cách đều có điều kiện để hỏng.**

Mục 🇻🇳 **Góc Việt Nam** trong mỗi bài là chỗ nối vào thực tế trong nước. Quy tắc: **mọi số liệu Việt
Nam phải có nguồn độc lập trích rõ**, không viết theo cảm nhận.

---

## Bố cục kho

```
econ252-finmarkets/
  README.md               ← bạn đang ở đây
  ly_thuyet/              13 bài học
  thuc_hanh/              chương trình Python — nơi mọi con số được TÍNH RA
  hinh/                   biểu đồ SVG sinh từ dữ liệu ở thuc_hanh/
  tai_lieu/
    gom-nhom.md           phân tích độ phủ và quyết định gom nhóm
```

**Code chỉ nằm ở một chỗ.** Bài lý thuyết không chép lại mã nguồn — nó liên kết tới file trong
`thuc_hanh/` và dán **output chạy thật**.

Lấy lại toàn bộ phụ đề và transcript:

```bash
mkdir -p /tmp/dl/econ252 && cd /tmp/dl/econ252
uvx yt-dlp --skip-download --write-subs --write-auto-subs \
  --sub-langs "en.*" --sub-format vtt -o "%(playlist_index)02d_%(id)s" \
  --sleep-requests 1 "https://www.youtube.com/playlist?list=PL8FB14A2200B87185"
```

Đã kiểm: 23 phụ đề, **236.705 từ**, phủ 99–100 % thời lượng mỗi video. Transcript OYC **216.131
từ**. Hai nguồn lệch dưới 5 % ở mọi bài.

---

## Ghi chú về độ tin cậy

1. **Mọi mốc đều được đối chiếu ngược với phụ đề gốc bằng script** — trừ buổi 12, chỉ có mốc cấp
   chương, và chỗ nào dùng buổi 12 đều ghi rõ.
2. **Bài gộp nhiều buổi thì kiểm mốc riêng từng buổi.** Gộp phụ đề vào một bảng sẽ báo "đúng" cho
   mốc thực ra thuộc buổi khác.
3. **Video nói sai thì đính chính, không chép lại**, kèm mốc thời gian.
4. **Dữ kiện ngoài video phải có nguồn độc lập**, liệt kê ở mục Nguồn cuối mỗi bài.
5. **Output code trong bài là output chạy thật**, không gõ tay.

---

**Bản đồ khoá học**

- [MIT 15.401 — Lý thuyết Tài chính I](../mit-15401-finance/README.md) — nửa **định giá**: chiết
  khấu, trái phiếu, cổ phiếu, phái sinh, danh mục, CAPM, tài chính doanh nghiệp
- **Yale ECON 252 — Thị trường Tài chính** ← *bạn đang ở đây* — nửa **định chế**: bảo hiểm, ngân
  hàng, quy định, sở giao dịch, bất động sản, tài chính công
