# Bài 0 — Nhập môn: cuốn sách là danh mục lỗi của chính tác giả

> [!info] Về bài này
> Dựng từ **Pre-Requisite Introduction** của *The Clean Coder* (Robert C. Martin — "Uncle Bob", `tai_lieu/`, `tr. 1–6`).
> Trích nguồn theo `Ch. N` (chương) và `tr. X` (số trang **in trong sách**; muốn tra tệp PDF thì cộng 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn ngay dưới — vì nguồn là tiếng Anh, sách không có sẵn câu dịch trong ngoặc kép.
> Đây là khoá **học qua hồ sơ ca** (case-study): mỗi bài mổ một chương, mỗi ca đi theo mạch *chuyện xảy ra → điều rút ra → đối chiếu 2026 → áp dụng cho bạn*.

## Mục lục

1. [Mở đầu: cậu bé 17 tuổi và cỗ máy đục lỗ](#1-mở-đầu-cậu-bé-17-tuổi-và-cỗ-máy-đục-lỗ)
2. ["Chuyên nghiệp" là từ xa lạ nhất với tôi](#2-chuyên-nghiệp-là-từ-xa-lạ-nhất-với-tôi)
3. [Ca 1 — Cú nghỉ việc trong cơn giận](#3-ca-1--cú-nghỉ-việc-trong-cơn-giận)
4. [Ca 2 — Danh mục tội lỗi: bản đồ những thất bại](#4-ca-2--danh-mục-tội-lỗi-bản-đồ-những-thất-bại)
5. [Mở rộng: thế giới lập trình năm 1969](#5-mở-rộng-thế-giới-lập-trình-năm-1969)
6. [Áp dụng vào việc của bạn](#6-áp-dụng-vào-việc-của-bạn)
7. [Từ điển thuật ngữ](#7-từ-điển-thuật-ngữ)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mở đầu: cậu bé 17 tuổi và cỗ máy đục lỗ

Năm **1969**, Robert Martin 17 tuổi. Cha cậu "ép" một doanh nghiệp địa phương tên ASC nhận cậu vào làm lập trình viên bán thời gian. Việc đầu tiên chẳng lấy gì làm oách: xếp hàng đống bản cập nhật vào các cuốn sổ tay máy IBM. Chính ở đó, lần đầu cậu bắt gặp dòng chữ *"This page intentionally left blank"* (trang này cố ý để trống).

Ít hôm sau, cấp trên giao cậu viết một chương trình Easycoder đơn giản: đọc các bản ghi từ băng từ, thay ID cũ bằng ID mới (bắt đầu từ 1, mỗi bản ghi tăng 1), rồi ghi ra băng mới. Cậu viết chương trình bằng **bút chì #2** lên "coding form", đưa xuống phòng đục thẻ, hôm sau nhận về một xấp thẻ đục lỗ. Cậu đem lên phòng máy tính — nơi khoá kín sau cánh cửa, có sàn nâng và điều hoà — rồi người vận hành lạnh lùng cầm lấy xấp thẻ, bỏ vào rổ chờ tới lượt.

Hôm sau, kết quả trả về: **compile lỗi**. Cấp trên liếc qua, càu nhàu, ngồi ngay vào máy đục lỗ sửa vài thẻ "nhanh như chớp", đem lên phòng máy, và chương trình chạy được. Rồi chuyện xảy ra thế này:

> [!quote] The Clean Coder — Introduction (tr. 4)
> "The next day my supervisor thanked me for my help, and terminated my employment. Apparently ASC didn't feel they had the time to nurture a 17-year-old."
>
> *Hôm sau, sếp cảm ơn tôi đã giúp một tay rồi cho tôi nghỉ việc luôn. Chắc ASC thấy chẳng hơi đâu mà kèm một thằng nhóc 17 tuổi.*

Đó là màn mở đầu cho một sự nghiệp mà chính tác giả gọi là chuỗi dài những cú vấp. Uncle Bob không mở sách bằng một chiến thắng; ông mở bằng một lần bị cho nghỉ. Và đó là chủ ý: cả cuốn sách dựng trên **những thất bại có thật của ông**, mỗi thất bại là một bài học về *tính chuyên nghiệp*.

## 2. "Chuyên nghiệp" là từ xa lạ nhất với tôi

Uncle Bob tự giới thiệu: ông đã lập trình **42 năm** và "thấy đủ cả" — từng bị đuổi việc lẫn được tung hô, từng làm lính quèn rồi cũng từng làm CEO. Ông viết cuốn này để trả lời một câu hỏi: **thế nào là một lập trình viên chuyên nghiệp?**

> [!quote] The Clean Coder — Introduction (tr. 2)
> "In the pages of this book I will try to define what it means to be a professional programmer. I will describe the attitudes, disciplines, and actions that I consider to be essentially professional."
>
> *Trong cuốn sách này, tôi sẽ thử định nghĩa thế nào là một lập trình viên chuyên nghiệp, bằng cách mô tả những **thái độ, kỷ luật và hành động** mà tôi cho là cốt lõi của sự chuyên nghiệp.*

Ba chữ **thái độ – kỷ luật – hành động** là bộ khung của cả cuốn sách lẫn khoá này. Chuyên nghiệp không nằm ở cấp bậc hay bằng cấp, mà nằm ở cách bạn *cư xử* với công việc.

Nhưng làm sao ông biết những thái độ ấy là gì? Vì ông đã học chúng theo cách khó nhất:

> [!quote] The Clean Coder — Introduction (tr. 2)
> "when I got my first job as a programmer, professional was the last word you'd have used to describe me."
>
> *Hồi mới vào nghề lập trình, "chuyên nghiệp" là từ cuối cùng người ta nghĩ tới khi nói về tôi.*

Cũng vì vậy mà Uncle Bob không lên giọng dạy đời. Ông kể lại chính những lần mình cư xử **thiếu chuyên nghiệp** rồi mới rút ra nguyên tắc. Đọc cuốn này cho đúng, do đó, không phải là nghe lời thầy giảng, mà là mổ từng ca để tự rút lấy bài học cho mình.

## 3. Ca 1 — Cú nghỉ việc trong cơn giận

**Chuyện gì đã xảy ra.** Khoảng năm 1971, sau đó 12 tháng, Martin (khi ấy 19 tuổi) cùng hai người bạn Richard và Tim và ba lập trình viên nữa viết một **hệ kế toán thời gian thực** cho công đoàn xe tải, chạy trên máy mini Varian 620i. Họ viết *từng dòng một*: hệ điều hành, trình điều khiển ngắt, driver vào/ra, hệ tập tin cho đĩa, trình liên kết, rồi cả code ứng dụng.

> [!quote] The Clean Coder — Introduction (tr. 5)
> "We wrote all this in 8 months working 70 and 80 hours a week to meet a hellish deadline. My salary was \$7,200 per year."
>
> *Cả đống ấy bọn tôi viết xong trong 8 tháng, cày 70–80 giờ mỗi tuần để kịp một deadline như địa ngục. Lương tôi khi đó 7.200 đô một năm.*

Họ giao hệ thống thành công. Phần thưởng công ty trao lại: **tăng lương 2%**. Thấy mình bị bạc đãi, cả nhóm nghỉ việc — nhưng cách Martin nghỉ mới là chuyện đáng nói:

> [!quote] The Clean Coder — Introduction (tr. 5)
> "We quit suddenly, and with malice. […] I and a buddy stormed into the boss' office and quit together rather loudly. This was emotionally very satisfying—for a day."
>
> *Bọn tôi nghỉ đột ngột, và đầy hằn học. […] Tôi với một cậu bạn xông thẳng vào phòng sếp, nghỉ việc cùng lúc, lại còn khá ầm ĩ. Xả được cơn tức thì đã thật — nhưng chỉ đã đúng một ngày.*

Hậu quả ập tới ngay hôm sau: 19 tuổi, thất nghiệp, không mảnh bằng. Đi phỏng vấn vài nơi đều trượt. Ông xin vào tiệm sửa máy cắt cỏ của anh rể, làm được bốn tháng thì bị cho nghỉ vì quá tệ, rồi trượt luôn vào trầm cảm — thức tới 3 giờ sáng ăn pizza xem phim quái vật đen trắng, ngủ vùi tới 1 giờ chiều, ghi danh học calculus ở trường cộng đồng rồi cũng trượt nốt.

**Điều rút ra.** Mẹ ông kéo ông lại và dạy cho một bài mà ông trích nguyên văn:

> [!quote] The Clean Coder — Introduction (tr. 6)
> "you never quit without having a new job, and you always quit calmly, coolly, and alone."
>
> *đừng bao giờ nghỉ việc khi chưa có chỗ mới, và lúc nghỉ thì phải **bình tĩnh, điềm đạm, và một mình**.*

Ông gọi cho sếp cũ, "ăn một miếng bánh khiêm nhường" (*humble pie*), và được nhận lại — với mức lương **6.800 đô/năm**, tức **thấp hơn** cả lúc trước. Ông vui vẻ nhận. Mười tám tháng sau ông rời công ty trong êm đẹp, tay cầm sẵn một lời mời việc tốt hơn.

> [!warning] Đối chiếu 2026
> Bài học cốt lõi — **nghỉ việc cho ra dáng chuyên nghiệp: có chỗ mới rồi hãy nghỉ, giữ điềm tĩnh, đừng lôi kéo đồng nghiệp nghỉ theo** — tới năm 2026 vẫn đúng y nguyên, mà còn đúng hơn, vì giới công nghệ **vốn nhỏ và dễ tra**: một lần "burn bridge" ầm ĩ có thể đuổi theo bạn qua LinkedIn, qua reference check, qua mạng lưới cựu đồng nghiệp.
> Nhưng vài chi tiết thì đã cũ và **đừng bắt chước**. Con số **70–80 giờ/tuần** ngày xưa kể ra như một tấm huy chương, nay lại là dấu hiệu của quản lý dự án hỏng và con đường dẫn thẳng tới *burnout* — chính Uncle Bob ở [Bài 11 (Áp lực)](bai_11_ap_luc.md) và trong chương Viết code cũng quay ra cảnh báo lối "cày kiệt sức" này. Còn chuyện "chịu lương thấp hơn để được nhận lại" chỉ là lối thoát cho hoàn cảnh 1971 của ông, không phải lời khuyên chung: năm 2026, đòn bẩy của bạn nằm ở kỹ năng chứng minh được và ở thị trường lao động, chứ không phải ở việc tự hạ giá mình.

> [!question] Áp dụng vào việc của bạn
> **Nếu bạn là lập trình viên.** Nhớ lại lần gần nhất bạn muốn "dứt áo ra đi" — bỏ việc, rời một dự án, rút khỏi một team. Bạn đã (hay sẽ) làm điều đó một cách *bình tĩnh, có chỗ mới hoặc có kế hoạch, và một mình* — hay làm theo cơn nóng? Thử viết ra kịch bản "nghỉ cho đúng" cho tình huống đó.
> **Suy rộng ra mọi nghề.** Chuyện "đừng đốt cầu khi đang giận" đúng cho mọi quan hệ nghề nghiệp: rời một khách hàng, một đối tác, một cộng đồng. Lần tới, khi bạn thấy rõ *mình đúng còn họ sai*, hãy tự hỏi: một năm nữa nhìn lại, cách mình rời đi hôm nay sẽ ra sao?

## 4. Ca 2 — Danh mục tội lỗi: bản đồ những thất bại

**Chuyện gì đã xảy ra.** Bạn có thể tưởng sau miếng bánh khiêm nhường ấy thì Martin đã "đắc đạo". Ông bác bỏ ngay: đó mới chỉ là bài học *đầu tiên*. Rồi ông liệt kê thẳng thừng những sai lầm của mấy năm về sau:

> [!quote] The Clean Coder — Introduction (tr. 6)
> "I would be fired from one job for carelessly missing critical dates, and nearly fired from still another for inadvertently leaking confidential information to a customer. I would take the lead on a doomed project and ride it into the ground without calling for the help I knew I needed. I would aggressively defend my technical decisions even though they flew in the face of the customers' needs. I would hire one wholly unqualified person, saddling my employer with a huge liability… And worst of all, I would get two other people fired because of my inability to lead."
>
> *Tôi sẽ bị đuổi ở một chỗ vì cẩu thả để trễ mấy mốc quan trọng; suýt bị đuổi ở chỗ khác vì vô ý làm lộ thông tin mật cho khách. Tôi sẽ nhận dẫn dắt một dự án vô vọng rồi lái nó đâm thẳng xuống đất, mà chẳng chịu gọi người giúp dù biết thừa là mình cần. Tôi sẽ khăng khăng bảo vệ quyết định kỹ thuật của mình dù nó đi ngược nhu cầu khách hàng. Tôi sẽ tuyển một người hoàn toàn không đủ sức, chất lên vai công ty một gánh nợ lớn… Và tệ nhất, tôi sẽ khiến hai người khác mất việc chỉ vì mình không biết lãnh đạo.*

**Điều rút ra.** Đây không chỉ là một lời thú tội — nó chính là **mục lục của cả cuốn sách**. Mỗi cái "tội" trong danh sách ứng với một chương bạn sắp học:

| Sai lầm Uncle Bob tự nhận (tr. 6) | Học cách tránh ở |
| --- | --- |
| Cẩu thả để trễ mốc quan trọng | [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md), [Bài 10 — Ước lượng](bai_10_uoc_luong.md) |
| Lái một dự án vô vọng xuống đất, không gọi trợ giúp | [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md), [Bài 4 — Viết code](bai_04_viet_code.md) |
| Khăng khăng bảo vệ quyết định kỹ thuật, ngược nhu cầu khách | [Bài 2 — Nói Không](bai_02_noi_khong.md), [Bài 12 — Cộng tác](bai_12_cong_tac.md) |
| Tuyển nhầm người không đủ năng lực | [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md), [Bài 14 — Dẫn dắt, học nghề](bai_14_dan_dat_hoc_nghe.md) |
| Không biết lãnh đạo, khiến người khác mất việc | [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md) |

Và đây là câu chốt định hình cả cách đọc cuốn sách:

> [!quote] The Clean Coder — Introduction (tr. 6)
> "So think of this book as a catalog of my own errors, a blotter of my own crimes, and a set of guidelines for you to avoid walking in my early shoes."
>
> *Vậy hãy xem cuốn sách này như một **bản danh mục lỗi của chính tôi**, một tờ khai tội của tôi, và một bộ chỉ dẫn để bạn khỏi phải giẫm lại con đường lầm lỗi thuở đầu của tôi.*

> [!warning] Đối chiếu 2026
> Cách học **"qua thất bại của người đi trước"** là điểm mạnh sống lâu nhất của cuốn sách: nó biến đạo lý trừu tượng thành những ca cụ thể. Cái cần chỉnh cho năm 2026 là **nguồn ca**. Bối cảnh của Uncle Bob là công ty phần mềm Mỹ những năm 1970–2000, đội nhỏ, tự viết cả hệ điều hành. Ngày nay, nhiều cơ chế đã gánh đỡ cho bạn phần lớn rủi ro ông từng chịu: *code review* chặn lỗi trước khi merge, *CI/CD* chặn một bản release hỏng, còn *mentorship* và tài liệu công khai thì thay cho lối "học bằng cách bị đuổi". Vì thế, ở khoá này mỗi ca đều có mục **Đối chiếu 2026** để tách phần *nguyên tắc còn sống* ra khỏi phần *bối cảnh đã chết*.

> [!question] Áp dụng vào việc của bạn
> **Nếu bạn là lập trình viên.** Tự viết "danh mục lỗi" của riêng bạn: 3 lần bạn cư xử thiếu chuyên nghiệp trong công việc (giấu một con bug, hứa một cái mốc rồi không giữ được, đẩy code chưa test sang cho người khác…). Giữ lại tờ giấy đó — cuối khoá bạn sẽ đối chiếu xem chương nào chạm đúng vào từng lỗi.
> **Suy rộng ra mọi nghề.** Bài tập trên hợp với bất kỳ nghề tri thức nào: viết lách, thiết kế, tư vấn, nghiên cứu. Với nghề của bạn, "chuyên nghiệp" nghĩa là gì — và lần gần nhất bạn *không* được như vậy là khi nào?

## 5. Mở rộng: thế giới lập trình năm 1969

Nhiều chi tiết trong câu chuyện mở đầu sẽ khó hình dung với người học năm 2026. Ít bối cảnh để đọc cho đúng:

> [!note] Mở rộng — lập trình bằng thẻ đục lỗ
> - **Coding form** — tờ giấy kẻ 25 dòng × 80 cột. Mỗi dòng là một *thẻ* (card); bạn viết code lên đó bằng **bút chì #2**, sáu cột cuối ghi số thứ tự (thường nhảy 10 để sau còn chèn thẻ vào giữa).
> - **Keypuncher** — nhân viên (thường là phụ nữ, cả một phòng vài chục người) gõ coding form thành **thẻ đục lỗ**: ký tự được *đục thủng thành lỗ* trên bìa cứng chứ không in ra giấy.
> - **Một lần chạy mất trọn một ngày.** Bạn nộp xấp thẻ, người vận hành chạy *khi nào rảnh*, hôm sau bạn mới nhận lại kết quả in kèm. Chỉ một lỗi compile là mất đứt một ngày. So với năm 2026: bạn gõ, lưu, và thấy lỗi ngay trong **mili-giây**.
> - **"Responsible engineer"** — thời đó, một người thường gánh trọn cả một hệ thống. Đội của Martin tự viết cả hệ điều hành lẫn trình liên kết — chuyện gần như không tưởng ngày nay, khi bạn đứng trên vai hàng nghìn thư viện có sẵn.
>
> Nắm được bối cảnh này thì mới đọc đúng các war story về sau: khi Uncle Bob nói chuyện "ship băng từ cho khách" hay "chạy nightly routine mất mấy tiếng" ([Bài 1](bai_01_tinh_chuyen_nghiep.md)), ông đang ở một thế giới mà **vòng phản hồi tính bằng ngày chứ không phải bằng giây** — nên cái giá của một sơ suất cẩu thả cao hơn bây giờ nhiều.

## 6. Áp dụng vào việc của bạn

Gộp lại phần hành động của cả bài — ba việc này làm nền cho toàn khoá:

> [!question] Ba việc trước khi sang Bài 1
> 1. **Định nghĩa "chuyên nghiệp" của riêng bạn.** Viết 3–5 câu: với nghề của bạn, một người *chuyên nghiệp* cư xử khác một người *nghiệp dư* ở chỗ nào? Cuối khoá đọc lại rồi sửa.
> 2. **Lập danh mục lỗi cá nhân** (mục 4) — 3 lần bạn thiếu chuyên nghiệp. Đây là "war story" của chính bạn.
> 3. **Chọn một góc để áp dụng.** Bạn sẽ đọc khoá này qua lăng kính *lập trình viên*, hay của *một nghề tri thức khác*? Mỗi bài đều có hai tầng câu hỏi — chọn tầng hợp với mình, nhưng thi thoảng thử tầng kia để thấy nguyên tắc ở dạng trần trụi nhất.

## 7. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Professionalism** (tính chuyên nghiệp) | Bộ *thái độ – kỷ luật – hành động* khiến bạn chịu trách nhiệm với công việc; chủ đề trung tâm cả sách (tr. 2). |
| **War story** | Câu chuyện thực chiến có thật của tác giả, dùng làm ca để rút bài học. Cả sách dựng trên war story. |
| **Humble pie** ("ăn bánh khiêm nhường") | Hạ cái tôi xuống để nhận lỗi hoặc chịu thiệt nhằm gỡ một sai lầm — điều Martin làm khi xin lại việc (tr. 6). |
| **Responsible engineer** | Người gánh trọn trách nhiệm một hệ thống — vai Martin từng giữ ở Teradyne ([Bài 1](bai_01_tinh_chuyen_nghiep.md)). |
| **Đối chiếu 2026** | Mục cố định của khoá: tách *nguyên tắc còn đúng* khỏi *bối cảnh, lời khuyên đã lỗi thời* trong lời Uncle Bob. |

## 8. Câu hỏi tự kiểm tra

1. Uncle Bob mở cuốn sách bằng một chiến thắng hay một thất bại? Vì sao ông chọn cách đó?
2. Ba trụ của "sự chuyên nghiệp" theo ông là gì? *(gợi ý: tr. 2)*
3. Mẹ ông dạy ba điều gì về cách nghỉ việc? Điều nào bạn thấy khó làm nhất?
4. Vì sao "danh mục tội lỗi" ở tr. 6 lại chính là mục lục cuốn sách?
5. Nêu một chi tiết trong câu chuyện 1969 mà cơ chế 2026 (CI, code review, mentorship) đã làm cho lỗi thời — và giải thích vì sao.

## Tóm tắt một trang

```
BÀI 0 — NHẬP MÔN: SÁCH = DANH MỤC LỖI CỦA CHÍNH TÁC GIẢ
─────────────────────────────────────────────────────────
LUẬN ĐỀ   Chuyên nghiệp = thái độ + kỷ luật + hành động (tr. 2).
          Không nằm ở bằng cấp hay chức danh — mà ở cách bạn
          cư xử với công việc.

CÁCH DẠY  Uncle Bob không giảng đạo. Ông kể chính những lần
          mình THIẾU chuyên nghiệp rồi mới rút nguyên tắc:
          "a catalog of my own errors" (tr. 6).

CA 1  Nghỉ việc trong cơn giận (19 tuổi) → thất nghiệp, trầm cảm.
      Bài học của mẹ: chưa có chỗ mới thì đừng nghỉ; nghỉ thì
      bình tĩnh, điềm đạm, MỘT MÌNH (tr. 6).

CA 2  "Danh mục tội lỗi" (tr. 6) = mục lục cuốn sách:
      trễ mốc→B9,10 · dự án vô vọng→B1,4 · cãi khách→B2,12 ·
      tuyển nhầm→B13,14 · không biết lãnh đạo→B14.

2026  Nguyên tắc (nhận lỗi của mình, nghỉ việc tử tế) còn sống.
      Bối cảnh (70–80h/tuần như huy chương, tự viết cả OS,
      học-bằng-cách-bị-đuổi) đã chết — nay có CI, review,
      mentorship gánh đỡ phần lớn rủi ro đó.

CÁCH HỌC KHOÁ NÀY   Mỗi ca: chuyện xảy ra → điều rút ra →
      ĐỐI CHIẾU 2026 → áp dụng cho bạn (2 tầng: dev / nghề khác).
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder: A Code of Conduct for Professional Programmers* (Pearson, 2011) — **Pre-Requisite Introduction** (`tr. 1–6`): tự giới thiệu 42 năm nghề và mục tiêu định nghĩa sự chuyên nghiệp (tr. 1–2); công việc đầu tiên ở ASC năm 1969 và bị cho nghỉ (tr. 2–4); hệ kế toán cho công đoàn, 70–80 giờ/tuần, cú nghỉ việc trong cơn giận và bài học của mẹ (tr. 5–6); "danh mục lỗi của chính tôi" (tr. 6). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 ← bạn đang ở đây] · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
