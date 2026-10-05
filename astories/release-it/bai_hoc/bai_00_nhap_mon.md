# Bài 0 — Nhập môn: "feature complete" chưa phải "production ready"

> [!info] Về bài này
> Dựng từ **Preface** và **Ch.1 — Introduction** của *Release It!* (Michael T. Nygard, 2007, `tai_lieu/`, `tr. 10–19`).
> Trích theo `Ch. N` và `tr. X` (**số trang in = số trang PDF**). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Đây là bài mở của khoá **5 bài**: Bài 0 Nhập môn (Preface + Ch.1) · Bài 1 Ổn định (Ch.2–6) · Bài 2 Công suất (Ch.7–10) · Bài 3 Thiết kế tổng quát (Ch.11–15) · Bài 4 Vận hành (Ch.16–18). Người đọc được hình dung là **dev kiêm vận hành**, nên mục Áp dụng có hai tầng: lúc thiết kế và viết code, và lúc trực on-call, viết postmortem.

## Mục lục

1. [Mở đầu: "Xong rồi." Thật không?](#1-mở-đầu-xong-rồi-thật-không)
2. [Ba ngộ nhận phải bỏ trước khi đọc](#2-ba-ngộ-nhận-phải-bỏ-trước-khi-đọc)
3. [Nửa còn thiếu của thiết kế: những điều hệ thống không được làm](#3-nửa-còn-thiếu-của-thiết-kế-những-điều-hệ-thống-không-được-làm)
4. [Qua được QA chưa có nghĩa là sống được ở production](#4-qua-được-qa-chưa-có-nghĩa-là-sống-được-ở-production)
5. [Quyết định sớm nhất lại là quyết định mù nhất](#5-quyết-định-sớm-nhất-lại-là-quyết-định-mù-nhất)
6. [Một triệu đô chỗ này, một triệu đô chỗ kia](#6-một-triệu-đô-chỗ-này-một-triệu-đô-chỗ-kia)
7. [Kiến trúc sư tháp ngà và kiến trúc sư thực dụng](#7-kiến-trúc-sư-tháp-ngà-và-kiến-trúc-sư-thực-dụng)
8. [Bốn phần của sách và lộ trình khoá học](#8-bốn-phần-của-sách-và-lộ-trình-khoá-học)
9. [Đối chiếu 2026](#9-đối-chiếu-2026)
10. [Áp dụng vào việc của bạn](#10-áp-dụng-vào-việc-của-bạn)
11. [Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
12. [Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
13. [Tóm tắt một trang](#tóm-tắt-một-trang)
14. [Nguồn](#nguồn)

---

## 1. Mở đầu: "Xong rồi." Thật không?

Nygard mở sách bằng một cảnh quen thuộc. Bạn cày dự án hơn một năm. Mọi tính năng có vẻ đã xong, phần lớn còn có unit test. Bạn thở phào: xong rồi. Rồi ông hỏi:

> [!quote] Release It! — Preface (tr. 10)
> "Does “feature complete” mean “production ready”? Is your system really ready to be deployed?"
>
> *"Đủ tính năng" có đồng nghĩa với "sẵn sàng chạy thật" không? Hệ thống của bạn đã thật sự sẵn sàng để triển khai chưa?*

Đội vận hành có chạy được nó mà không cần bạn không? Bạn đã thấy chùng xuống khi nghĩ tới những cuộc gọi khẩn lúc nửa đêm chưa? (tr. 10)

Theo Nygard, quá thường xuyên, các đội dự án nhắm tới việc **qua được bài kiểm của QA**, chứ không nhắm tới **cuộc sống ở Production** (ông viết hoa chữ P). Mà kiểm thử giỏi tới đâu cũng không đủ:

> [!quote] Release It! — Preface (tr. 10)
> "But testing—even agile, pragmatic, automated testing—is not enough to prove that software is ready for the real world."
>
> *Nhưng kiểm thử, kể cả kiểu agile, thực dụng, tự động hoá, cũng không đủ để chứng minh phần mềm đã sẵn sàng cho thế giới thật.*

Thế giới thật có người dùng "điên rồ", lưu lượng trải khắp địa cầu, những đám viết virus từ những nước bạn chưa nghe tên (tr. 10). Tên bài này lấy từ chính khoảng cách đó: **"feature complete" là đích của dự án, còn "production ready" là điểm xuất phát của hệ thống.**

## 2. Ba ngộ nhận phải bỏ trước khi đọc

Trước khi vào việc, Nygard dọn đường bằng ba ngộ nhận (tr. 10–11). Chúng là cặp kính để đọc cả cuốn sách.

**Một: làm kỹ thì sẽ không có chuyện xấu.** Dù kế hoạch khéo tới đâu, chuyện xấu vẫn xảy ra. Ngăn được thì tốt, nhưng tin rằng mình đã lường trước và loại hết mọi sự cố thì, theo ông, "có khi là chí mạng". Việc đúng là ngăn những gì ngăn được, và thiết kế sao cho **cả hệ thống hồi phục được** sau những cú chấn thương không ai lường trước (tr. 10). Đây là mầm của Bài 1.

**Hai: Release 1.0 là vạch đích.**

> [!quote] Release It! — Preface (tr. 11)
> "Second, realize that “Release 1.0” is not the end of the development project but the beginning of the system’s life on its own."
>
> *Thứ hai, hãy hiểu rằng "Release 1.0" không phải là lúc dự án phát triển kết thúc, mà là lúc hệ thống bắt đầu cuộc đời tự lập của nó.*

Ông ví như đứa con trưởng thành rời nhà lần đầu: bạn không muốn nó dọn về ở lại, kéo theo vợ hoặc chồng, bốn đứa con, hai con chó và một con vẹt (tr. 11). Thiết kế không tính tới production thì đời bạn sau ngày release sẽ đầy "kịch tính", và không phải thứ kịch tính dễ chịu.

**Ba: công nghệ hay là đủ.**

> [!quote] Release It! — Preface (tr. 11)
> "In the world of business—which is the world that pays us—it all comes down to money."
>
> *Trong thế giới kinh doanh, cũng là thế giới trả lương cho chúng ta, mọi thứ rốt cuộc quy về tiền.*

Làm thêm việc thì tốn tiền, nhưng downtime cũng tốn tiền; code kém hiệu quả đẩy chi phí đầu tư và vận hành lên. Muốn hiểu một hệ thống đang chạy, hãy **lần theo đồng tiền** (tr. 11).

Sách viết cho ai? Cho người làm phần mềm "cấp doanh nghiệp", mà Nygard định nghĩa rất đời: phần mềm ngừng chạy thì công ty mất tiền; nếu có ai phải nghỉ về nhà cả ngày vì phần mềm của bạn dừng, sách này dành cho bạn (tr. 11).

## 3. Nửa còn thiếu của thiết kế: những điều hệ thống không được làm

Chương 1 mở bằng một lời phê bình thẳng:

> [!quote] Release It! — Ch.1 (tr. 14)
> "Software design as taught today is terribly incomplete. It talks only about what systems should do. It doesn’t address the converse—things systems should not do. They should not crash, hang, lose data, violate privacy, lose money, destroy your company, or kill your customers."
>
> *Thiết kế phần mềm như cách người ta dạy hiện nay thiếu sót trầm trọng. Nó chỉ nói về những gì hệ thống nên làm, mà không đụng tới chiều ngược lại: những điều hệ thống không được làm. Không được sập, không được treo, không được mất dữ liệu, không được xâm phạm quyền riêng tư, không được làm mất tiền, không được phá huỷ công ty bạn, không được giết khách hàng của bạn.*

Để hình dung, Nygard kể chuyện ngành ô tô đầu thập niên 90. Những chiếc xe thiết kế trong phòng thí nghiệm mát lạnh bóng loáng trên bản vẽ CAD và trước quạt gió khổng lồ; những người thiết kế trong không gian êm ả ấy làm ra những thiết kế "thanh lịch, tinh xảo, khéo léo, mong manh, chẳng làm ai hài lòng và rốt cuộc chết yểu" (tr. 14). Chiếc xe bạn *muốn* mua là chiếc được thiết kế bởi một người biết rằng lần thay dầu nào cũng trễ 3.000 dặm, rằng lốp phải bám đường ở một phần mười sáu inch gai cuối cùng y như lúc mới, và rằng sẽ có lúc bạn đạp phanh gấp khi một tay cầm bánh Egg McMuffin, tay kia cầm điện thoại (tr. 14).

Phần mềm cũng phải được làm cho cái thế giới lấm lem ấy. Nygard hứa sẽ chuẩn bị cho "những đạo quân người dùng phi lý" làm những điều điên rồ, không đoán trước được. Phần mềm bị tấn công từ khoảnh khắc được phát hành, và phải đứng vững trước cơn lũ truy cập khi một trang lớn trỏ link tới (tr. 14).

## 4. Qua được QA chưa có nghĩa là sống được ở production

Hãy nhớ lại những bài kiểm mà phần mềm của bạn được làm ra để vượt qua, kiểu "họ và tên khách là bắt buộc, chữ lót thì tuỳ chọn". Theo Nygard, phần lớn phần mềm được thiết kế cho phòng lab hay cho tester (tr. 15):

> [!quote] Release It! — Ch.1 (tr. 15)
> "It aims to survive the artificial realm of QA, not the real world of production."
>
> *Nó nhắm tới việc sống sót trong cõi nhân tạo của QA, chứ không phải thế giới thật của production.*

Qua QA cho biết rất ít về ba đến mười năm tới. Phần mềm của bạn có thể là chiếc Toyota Camry chạy liên tục hàng nghìn giờ, cũng có thể là chiếc Chevy Vega (theo Nygard, xe gãy phần đầu ngay trên đường thử của hãng) hay chiếc Ford Pinto dễ phát nổ nếu bị tông đúng kiểu (tr. 15).

Rồi ông mượn một bài học của ngành sản xuất: **"design for manufacturability"**, thiết kế sao cho sản phẩm làm ra được rẻ và tốt. Trước đó, bản vẽ ném qua tường xuống xưởng có cả những con vít không với tới. Ngành phần mềm, ông bảo, đang y như vậy: ta tụt hậu trong dự án mới vì cứ phải nghe điện thoại hỗ trợ cho dự án "nửa sống nửa chín" vừa đẩy ra cửa. Thứ tương đương mà ngành cần, ông gọi là **"design for production"**: thiết kế từng hệ thống, *và cả hệ sinh thái các hệ thống phụ thuộc nhau*, để vận hành rẻ và chất lượng cao (tr. 15).

## 5. Quyết định sớm nhất lại là quyết định mù nhất

Hãy nghĩ tới những quyết định đầu tiên của dự án: ranh giới hệ thống ở đâu, chia thành những hệ con nào. Theo Nygard, chúng có ảnh hưởng lớn nhất và khó đảo ngược nhất, vì chúng đông cứng lại thành cơ cấu đội, ngân sách, cấu trúc quản lý, thậm chí mã chấm công:

> [!quote] Release It! — Ch.1 (tr. 15)
> "Team assignments are the first draft of the architecture."
>
> *Cách chia đội chính là bản nháp đầu tiên của kiến trúc.*

Trớ trêu là chúng cũng là những quyết định **thiếu thông tin nhất**, đưa ra lúc đội mù mờ nhất về hình dạng cuối cùng của phần mềm (tr. 16). Tên mục ("Use the Force") lấy từ đây: kể cả ở dự án "agile", quyết định vẫn nên đưa ra với tầm nhìn xa, và người thiết kế dường như phải "dùng Thần lực" để nhìn thấy tương lai mà chọn thiết kế bền nhất (tr. 16). Các phương án thường tốn công xây dựng ngang nhau nhưng **chi phí vòng đời khác nhau một trời một vực** (tr. 16). Nygard hứa sẽ chỉ ra hệ quả về sau của hàng chục phương án thiết kế, với ví dụ lấy từ hệ thống thật ông từng làm, và "phần lớn từng làm tôi mất ngủ" (tr. 16).

Ông tự nhận ủng hộ agile mạnh mẽ, và lý do nằm trong một chú thích đáng chép lại:

> [!quote] Release It! — Ch.1 (tr. 16)
> "Since production is the only place to learn how the software will respond to real-world stimuli, I advocate any approach that begins the learning process as soon as possible."
>
> *Vì production là nơi duy nhất để biết phần mềm phản ứng ra sao trước tác động của thế giới thật, tôi ủng hộ mọi cách làm giúp quá trình học ấy bắt đầu càng sớm càng tốt.*

## 6. Một triệu đô chỗ này, một triệu đô chỗ kia

Theo Nygard, "khủng hoảng phần mềm" đã kéo dài hơn ba mươi năm: **gold owner** (người trả tiền) vẫn chê phần mềm đắt, **goal donor** (người có nhu cầu mà phần mềm phải đáp ứng) vẫn chê làm chậm, và hai người này "hiếm khi là một" (tr. 16).

Thời client/server, người dùng một hệ thống tính bằng chục, bằng trăm. Giờ người tài trợ thản nhiên đòi "25.000 người dùng đồng thời" hay "4 triệu lượt khách mỗi ngày". "Năm số chín" (99,999%) từng là đặc quyền của mainframe, nay trang thương mại bình thường cũng bị đòi chạy suốt ngày đêm quanh năm (tr. 17). Quy mô lớn hơn thì cách hỏng nhiều hơn và sức chịu lỗi thấp hơn.

Rồi ông nói chuyện tiền thật. Hệ thống làm cho QA thường ngốn chi phí vận hành, downtime và bảo trì tới mức không bao giờ hoà vốn. Với nhiều khách của Nygard, **downtime tốn trực tiếp hơn 100.000 đô mỗi giờ** (tr. 17). Từ đó ông tính: chênh lệch giữa uptime 98% và 99,99% là **hơn 17 triệu đô một năm**; và chi **5.000 đô** cho hệ thống build và release tự động để tránh downtime khi release thì công ty tránh được **200.000 đô**, với giả định mỗi lần release tốn 10.000 đô (gồm công lao động và chi phí downtime có kế hoạch), bốn lần một năm, trong năm năm. Ông cho rằng phần lớn giám đốc tài chính sẽ không ngại duyệt một khoản chi lãi 4.000% (tr. 18). Nguyên tắc rút ra được in thành khung bên lề:

> [!quote] Release It! — Ch.1 (tr. 18)
> "Don’t avoid one-time development expenses at the cost of recurring operational expenses."
>
> *Đừng né một khoản chi phát triển chỉ tốn một lần để rồi gánh một khoản chi vận hành lặp đi lặp lại.*

Đội dự án bị đo bằng ngân sách và hạn giao nên dễ đẩy chi phí sang vận hành; nhưng hệ thống sống ở giai đoạn vận hành lâu hơn phát triển rất nhiều (tr. 18). Nygard chốt: **quyết định thiết kế và kiến trúc cũng là quyết định tài chính**, và sự kết hợp góc nhìn kỹ thuật với góc nhìn tài chính là một trong những chủ đề quan trọng nhất lặp lại suốt cuốn sách (tr. 18).

> [!note] Mở rộng — tự tính lại con số của Nygard
> Phần tính này của khoá, không có trong sách. Một năm có 8.760 giờ.
> - **98%** uptime = được phép ngừng 175,2 giờ/năm (hơn 7 ngày). **99,99%** = 0,876 giờ, khoảng 52,6 phút.
> - Chênh khoảng 174,3 giờ × 100.000 đô = **khoảng 17,4 triệu đô**, khớp với "hơn 17 triệu".
> - "4.000%" là tỉ lệ 200.000 / 5.000 = 40 lần. Tính ROI chặt (lợi ích ròng chia chi phí) thì là 3.900%. Kết luận không đổi.
>
> Bài học không nằm ở con số chính xác mà ở thói quen: **mỗi số chín thêm vào có giá, mỗi giờ ngừng cũng có giá, và hai cái giá ấy phải đặt lên cùng một bàn cân.**

## 7. Kiến trúc sư tháp ngà và kiến trúc sư thực dụng

Bạn từng nghiến răng phải code một thứ theo "chuẩn công ty", trong khi dùng công nghệ khác thì dễ hơn mười lần chưa? Nygard bảo khi đó bạn là nạn nhân của **kiến trúc sư tháp ngà**: người vươn tới trừu tượng, xa phần cứng và mạng, ban sắc lệnh xuống đám coder kiểu "Dùng EJB container-managed persistence!" hay "Mọi giao diện phải dựng bằng JSF!" (tr. 18–19).

> [!quote] Release It! — Ch.1 (tr. 19)
> "I guarantee that an architect who doesn’t bother to listen to the coders on the team doesn’t bother listening to the users either."
>
> *Tôi dám chắc: một kiến trúc sư không buồn nghe coder trong đội thì cũng chẳng buồn nghe người dùng.*

Kiểu thứ hai, **kiến trúc sư thực dụng**, ngồi cạnh coder, có khi chính là coder, không ngại mở nắp hay vứt bỏ một lớp trừu tượng không hợp. Người tháp ngà mơ một trạng thái cuối "hoàn hảo như pha lê"; người thực dụng nghĩ về **động lực của thay đổi**: triển khai sao cho khỏi khởi động lại cả thế giới, cần thu số liệu gì, phần nào cần cải thiện nhất. Mỗi phần trong hệ thống của họ chỉ *đủ tốt cho sức ép hiện tại*, và họ biết phần nào cần thay khi sức ép đổi khác (tr. 19).

## 8. Bốn phần của sách và lộ trình khoá học

Preface cho biết sách chia bốn phần, mỗi phần mở bằng một nghiên cứu tình huống (tr. 12). Bài 1–4 của khoá ứng với bốn phần này. *Ghi chú của khoá:* thực tế Part III (tr. 218) không có case; xem [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md).

| Phần của sách (tr. 12–13) | Nygard nói gì |
| --- | --- |
| 1 — Ổn định (Ch.2–6) | Giữ hệ thống sống. Hệ phân tán dù hứa tin cậy nhờ dư thừa vẫn thường chỉ đạt "hai số tám" chứ không phải "năm số chín". |
| 2 — Công suất (Ch.7–10) | Đo, hiểu và tối ưu công suất qua mẫu và phản mẫu. |
| 3 — Thiết kế tổng quát (Ch.11–15) | Thiết kế cho trung tâm dữ liệu: multihoming, mạng nhiều lớp, mạng lưu trữ. *(Part III thực tế không có mục riêng về mạng lưu trữ.)* |
| 4 — Vận hành (Ch.16–18) | Nhiều hệ thống như con mèo của Schrödinger, nhốt trong hộp, không cách gì quan sát. Minh bạch (Ch.17) và Thích nghi (Ch.18). |

Thứ tự có lý do: **ổn định là điều kiện tiên quyết**. Hệ thống ngày nào cũng sập thì chẳng ai quan tâm tương lai xa, và lối nghĩ vá víu ngắn hạn sẽ thống trị (tr. 12). Các nghiên cứu tình huống là sự cố thật Nygard tận mắt thấy, đã đổi tên nhưng giữ nguyên ngành, trình tự sự kiện, kiểu hỏng, đường lan lỗi, kết cục và chi phí (tr. 13). Bài 1, 2 và 4 sẽ kể từng ca như một hồ sơ sự cố; Bài 3 thì không, vì sách không có case.

## 9. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống.** Luận điểm "feature complete chưa phải production ready" nay đã thành quy trình. Sách *Site Reliability Engineering* của Google mô tả **Production Readiness Review (PRR)**: quy trình xác định nhu cầu tin cậy của dịch vụ theo đặc thù của nó, là điều kiện tiên quyết để đội SRE nhận vận hành dịch vụ; PRR rà kiến trúc và phụ thuộc, giám sát, ứng cứu khẩn cấp, kế hoạch công suất, quản lý thay đổi (Ch.32). Nỗi lo rằng làm nhanh thì phải hy sinh ổn định cũng bị nghiên cứu DORA bác bỏ: DORA viết rằng nghiên cứu của họ "nhiều lần chứng minh tốc độ và ổn định không phải là đánh đổi", và đội giỏi thì giỏi đều ở cả năm chỉ số giao phần mềm.
>
> **Phần cần chỉnh.**
> - *Con số tiền.* Mức 100.000 đô/giờ năm 2007 nay là thấp. Khảo sát ITIC 2024 (hơn 1.000 công ty, 11/2023 đến giữa 3/2024): với **hơn 90%** doanh nghiệp vừa và lớn, một giờ downtime tốn **trên 300.000 đô**; **41%** nói 1 đến hơn 5 triệu đô. Báo cáo "The Hidden Costs of Downtime 2026" của Oxford Economics (22/7/2026) đặt con số tổng cho nhóm Global 2000 ở mức **600 tỉ đô**. "Lần theo đồng tiền" càng đúng, chỉ có đơn vị phải nhân lên.
> - *Cái đích "năm số chín".* Nygard kể áp lực chạy 24/7 như xu thế phải theo. Google SRE nói "100% có lẽ không bao giờ là mục tiêu tin cậy đúng", vì không đạt được và thường vượt mức người dùng cần; mỗi bước tăng tin cậy có thể tốn gấp 100 lần bước trước (Ch.3 "Embracing Risk").
> - *Ranh giới dev và ops.* Preface hình dung đội vận hành chạy hệ thống "mà không có bạn". Theo nhà xuất bản, bản 2 (1/2018) thêm "DevOps, microservices và kiến trúc cloud-native" cùng **chaos engineering**. Khoá dựng trên bản 1, nên mỗi bài sẽ chỉ ra chỗ đã bị thời gian vượt qua.
>
> **Phần đã lỗi thời.** Tên ví dụ (Slashdot, Fark, Digg, EJB, JSF, trung tâm dữ liệu tự vận hành) là của năm 2007: giữ lấy mẫu hình, thay tên bằng thứ của thời mình.

## 10. Áp dụng vào việc của bạn

> [!question] Khi thiết kế và viết code
> 1. **Viết nửa còn thiếu của đặc tả.** Với tính năng bạn đang làm, bên cạnh "hệ thống phải làm gì", viết thêm "hệ thống **không được** làm gì" theo bảy động từ ở tr. 14: sập, treo, mất dữ liệu, lộ riêng tư, mất tiền, phá công ty, giết khách.
> 2. **Soi bản nháp kiến trúc trong sơ đồ tổ chức.** Đặt sơ đồ chia đội cạnh sơ đồ dịch vụ. Chỗ nào một thay đổi nhỏ phải đi qua ba đội? Đó là "bản nháp đầu tiên của kiến trúc" (tr. 15) đang cản bạn.
> 3. **Đặt một quyết định lên bàn cân tiền.** Lấy một thứ bạn vừa cắt để kịp hạn (tự động hoá release, timeout, giám sát). Ước chi phí một lần đã tiết kiệm và chi phí vận hành lặp lại nó sẽ sinh ra trong một năm. Bên nào lớn hơn?

> [!question] Khi vận hành, trực on-call, viết postmortem
> 1. **Tính giá một giờ ngừng của hệ thống bạn.** Hỏi người làm sản phẩm hoặc tài chính: một giờ ngừng thì mất bao nhiêu? Làm lại phép tính ở mục 6 với con số của bạn.
> 2. **Thêm dòng "chi phí" vào mẫu postmortem.** Ghi thêm: sự cố tốn khoảng bao nhiêu, và quyết định thiết kế nào lúc phát triển đã khiến nó xảy ra hoặc kéo dài.
> 3. **Tự làm một bản PRR mini.** Trước lần release lớn tới, trả lời thành văn: số liệu nào cho biết hệ thống đang khoẻ? Rollback mất bao lâu? Phụ thuộc nào hỏng thì kéo mình sập theo? Câu nào chưa trả lời được là khoảng cách giữa "feature complete" và "production ready" của bạn.

## 11. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Feature complete** | Đã làm đủ tính năng theo đặc tả. Đích của *dự án*, chưa nói gì về đời sống ở production (tr. 10). |
| **Production ready** | Sẵn sàng sống ở môi trường thật: người dùng, tải và sự cố thật, vận hành lâu dài (tr. 10). |
| **Design for production** | Thiết kế tính tới chi phí và chất lượng vận hành, tương tự "design for manufacturability" (tr. 15). |
| **Uptime / availability** | Tỉ lệ thời gian hệ thống chạy được. "Năm số chín" = 99,999%; "hai số tám" = 88% (tr. 12, 17). |
| **Gold owner / goal donor** | Người trả tiền cho phần mềm / người có nhu cầu phần mềm phải đáp ứng; "hiếm khi là một người" (tr. 16). |
| **Kiến trúc sư tháp ngà** | Xa rời code và phần cứng, ban tiêu chuẩn từ trên xuống, nhắm trạng thái cuối hoàn hảo (tr. 18–19). |
| **Kiến trúc sư thực dụng** | Sát code, quan tâm tài nguyên, triển khai, số liệu, luôn nghĩ về động lực thay đổi (tr. 19). |
| **PRR** (Production Readiness Review) | Quy trình rà độ sẵn sàng vận hành trong mô hình SRE của Google; không có trong sách, xem mục 9. |

## 12. Câu hỏi tự kiểm tra

1. Vì sao Nygard nói kiểm thử, kể cả tự động, "không đủ"? Kể hai thứ QA không mô phỏng được. *(tr. 10)*
2. Ba ngộ nhận Nygard muốn người đọc bỏ đi là gì? *(tr. 10–11)*
3. "Nửa còn thiếu" của thiết kế phần mềm là gì? Nêu đủ bảy điều hệ thống không được làm. *(tr. 14)*
4. "Design for manufacturability" là gì, và nó gợi cho Nygard khái niệm nào? *(tr. 15)*
5. Vì sao quyết định kiến trúc sớm nhất vừa quan trọng nhất vừa nguy hiểm nhất? *(tr. 15–16)*
6. Tự tính lại vì sao 98% so với 99,99% uptime chênh "hơn 17 triệu đô" một năm. Giả định nào năm 2026 phải chỉnh? *(tr. 17–18)*

## Tóm tắt một trang

```
BÀI 0 — NHẬP MÔN: "FEATURE COMPLETE" CHƯA PHẢI "PRODUCTION READY"
────────────────────────────────────────────────────────────────
MỞ ĐẦU   Xong mọi tính năng, có unit test, thở phào.
         "Does feature complete mean production ready?" (tr. 10)
         Kiểm thử, dù tự động, không đủ chứng minh.

3 NGỘ NHẬN (tr. 10–11)
         1. Làm kỹ thì không có sự cố → sự cố VẪN tới; phải hồi phục được.
         2. Release 1.0 là vạch đích  → là lúc hệ thống bắt đầu tự sống.
         3. Công nghệ hay là đủ        → mọi thứ quy về TIỀN.

NỬA THIẾU (tr. 14)  Chỉ dạy hệ thống NÊN làm gì. Quên KHÔNG ĐƯỢC:
         sập · treo · mất dữ liệu · lộ riêng tư · mất tiền ·
         phá công ty · giết khách.

ĐÚNG ĐÍCH (tr. 15)  Qua QA ≠ sống ở production. DESIGN FOR PRODUCTION.
         "Team assignments are the first draft of the architecture."

TIỀN (tr. 17–18)  Downtime > $100.000/giờ (2007).
         98% → 99,99% = hơn $17 triệu/năm. $5.000 → tránh $200.000.
         Thiết kế và kiến trúc cũng là quyết định tài chính.

KIẾN TRÚC SƯ (tr. 18–19)  Tháp ngà: sắc lệnh, trạng thái cuối hoàn hảo.
         Thực dụng: sát code, số liệu, ĐỘNG LỰC THAY ĐỔI.

2026     Còn sống: PRR (Google SRE); tốc độ và ổn định không đánh đổi (DORA).
         Cần chỉnh: downtime >$300.000/giờ (ITIC 2024); 100% không phải đích.
```

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software* (Pragmatic Bookshelf, 2007), `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`:
  - **Preface** (`tr. 10–13`): "feature complete" và production ready, kiểm thử không đủ, ngộ nhận thứ nhất (tr. 10); Release 1.0, tiền, ai nên đọc (tr. 11); bốn phần của sách, "hai số tám" (tr. 12); các nghiên cứu tình huống có thật (tr. 13).
  - **Ch.1 Introduction** (`tr. 14–19`): nửa còn thiếu, ô tô (tr. 14); 1.1–1.2 (tr. 15–16); 1.3–1.4, gold owner/goal donor (tr. 16–17); 1.5 tiền (tr. 17–18); 1.6 kiến trúc sư (tr. 18–19).
  - Quy ước trích: `tr. X` = số trang in = số trang PDF.
- Nguồn web dùng ở Đối chiếu 2026 (truy cập 9/2026):
  - Pragmatic Bookshelf, *Release It! Second Edition*: https://pragprog.com/titles/mnee2/release-it-second-edition/
  - Google, *Site Reliability Engineering*, Ch.32 "The Evolving SRE Engagement Model": https://sre.google/sre-book/evolving-sre-engagement-model/
  - Google, *Site Reliability Engineering*, Ch.3 "Embracing Risk": https://sre.google/sre-book/embracing-risk/
  - DORA, "DORA's software delivery performance metrics": https://dora.dev/guides/dora-metrics/
  - ITIC, "ITIC 2024 Hourly Cost of Downtime Report Part 1": https://itic-corp.com/itic-2024-hourly-cost-of-downtime-report/
  - Oxford Economics, "The Hidden Costs of Downtime 2026": https://www.oxfordeconomics.com/resource/the-hidden-costs-of-downtime-2026/

---

**Bản đồ khoá học:** [Bài 0 ← bạn đang ở đây] · [Bài 1 — Ổn định](bai_01_on_dinh.md) · [Bài 2 — Công suất](bai_02_cong_suat.md) · [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md) · [Bài 4 — Vận hành](bai_04_van_hanh.md)

Xem thêm [README khoá học](../README.md).
