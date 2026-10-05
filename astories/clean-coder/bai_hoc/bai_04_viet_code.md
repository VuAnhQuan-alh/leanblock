# Bài 4 — Viết code: kỷ luật của tâm trí, không phải số giờ

> [!info] Về bài này
> Dựng từ **Chương 4 — Coding** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 57–76`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Cần đọc trước: [Bài 3 — Nói Có](bai_03_noi_co.md).
> ⚠️ Uncle Bob nói thẳng: chương này là *quy tắc cá nhân* về **hành vi, tâm trạng, thái độ** khi viết code — "you may violently disagree" (tr. 57). Vì thế mục [Đối chiếu 2026](#8-đối-chiếu-2026) ở đây dày hơn thường lệ.

## Mục lục

1. [Mở đầu: 3 giờ sáng và "gửi thư cho chính mình"](#1-mở-đầu-3-giờ-sáng-và-gửi-thư-cho-chính-mình)
2. [Chuẩn bị: viết code là tung hứng bốn mối lo cùng lúc](#2-chuẩn-bị-viết-code-là-tung-hứng-bốn-mối-lo-cùng-lúc)
3. [Ca 1 — "Vùng Phập Phù" (the Zone): hãy tránh nó](#3-ca-1--vùng-phập-phù-the-zone-hãy-tránh-nó)
4. [Ca 2 — Cuộc gỡ lỗi 1972: thời gian debug cũng là tiền](#4-ca-2--cuộc-gỡ-lỗi-1972-thời-gian-debug-cũng-là-tiền)
5. [Giữ nhịp: marathon chứ không phải chạy nước rút](#5-giữ-nhịp-marathon-chứ-không-phải-chạy-nước-rút)
6. [Trễ hạn, hy vọng, tăng ca và ba con số](#6-trễ-hạn-hy-vọng-tăng-ca-và-ba-con-số)
7. [Giao hàng giả và định nghĩa "Xong"](#7-giao-hàng-giả-và-định-nghĩa-xong)
8. [Đối chiếu 2026](#8-đối-chiếu-2026)
9. [Áp dụng vào việc của bạn](#9-áp-dụng-vào-việc-của-bạn)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
12. [Tóm tắt một trang](#tóm-tắt-một-trang)
13. [Nguồn](#nguồn)

---

## 1. Mở đầu: 3 giờ sáng và "gửi thư cho chính mình"

Năm **1988**, Uncle Bob làm ở một start-up viễn thông tên Clear Communications; cả nhóm cày trối chết để gây "vốn mồ hôi", ai nấy đều mơ đổi đời. Một đêm rất khuya — nói cho đúng là một sáng rất sớm — để gỡ một vấn đề định thời, anh cho code **tự gửi một thông điệp cho chính nó** qua hệ điều phối sự kiện (họ gọi là "gửi mail"). Đó là một giải pháp sai bét, nhưng vào lúc 3 giờ sáng thì nó trông đẹp mê hồn — sau 18 tiếng code liền tù tì (chưa kể mấy tuần 60–70 giờ), đầu anh chẳng còn nghĩ ra nổi cái gì khác.

> [!quote] The Clean Coder — Ch.4 (tr. 59)
> "I remember thinking that working at 3 am is what serious professionals do. How wrong I was!"
>
> *Tôi nhớ hồi đó mình cứ đinh ninh rằng cày tới 3 giờ sáng mới là điều dân chuyên nghiệp thứ thiệt làm. Tôi đã lầm to đến thế đấy!*

Cái đoạn code 3 giờ sáng ấy về sau quay lại cắn cả đội hết lần này tới lần khác: nó gài vào hệ một cấu trúc thiết kế lỗi mà ai cũng phải né, đẻ ra đủ kiểu lỗi định thời và cả những vòng lặp mail vô tận. Chẳng bao giờ có thời gian ngồi viết lại, nhưng lúc nào cũng có thời gian vá thêm một mụn cóc nữa quanh nó. Nhiều năm sau, nó thành câu đùa của cả đội: hễ thấy Bob mệt hay bực, họ lại kêu: *"Coi chừng! Bob sắp gửi mail cho chính mình đấy!"* Bài học rút ra:

> [!quote] The Clean Coder — Ch.4 (tr. 60)
> "Don't write code when you are tired. Dedication and professionalism are more about discipline than hours."
>
> *Đừng viết code khi đang mệt. Sự tận tuỵ và tính chuyên nghiệp nằm ở **kỷ luật**, chứ không phải ở **số giờ**.*

Cả chương này khởi nguồn từ một điều anh nhận ra hồi 18 tuổi, lúc tập gõ mù trên máy đục thẻ IBM 029: bí quyết của sự thành thạo không phải là tốc độ, mà là **sự tự tin và giác quan-lỗi** (error-sense) — cái khả năng cảm thấy mình vừa sai gần như tức khắc, để đóng vòng phản hồi thật nhanh.

> [!quote] The Clean Coder — Ch.4 (tr. 58)
> "the key to mastery is confidence and error-sense."
>
> *chìa khoá của sự tinh thông là **sự tự tin và giác quan-lỗi**.*

## 2. Chuẩn bị: viết code là tung hứng bốn mối lo cùng lúc

Vì sao code lại đòi tập trung ghê gớm đến vậy? Vì nó bắt bạn giữ thăng bằng **bốn mối lo** cùng một lúc (tr. 58–59):

1. **Code phải chạy** — bạn phải hiểu đúng vấn đề, cài đúng lời giải, mà vẫn nhất quán với ngôn ngữ, nền tảng, kiến trúc và cả những "mụn cóc" sẵn có của hệ.
2. **Code phải giải đúng vấn đề của khách** — mà yêu cầu khách nêu ra thường *không* thật sự giải được vấn đề của họ; bạn phải nhìn ra điều đó rồi đàm phán.
3. **Code phải khớp với hệ hiện có** — đừng làm nó cứng thêm, giòn thêm, mờ đục thêm; các phụ thuộc phải được quản cho gọn.
4. **Code phải đọc được với lập trình viên khác** — không phải cứ comment cho đẹp là xong, mà là phải *bộc lộ được ý định*; đây có lẽ là thứ khó thành thạo nhất.

Tung hứng cả bốn thứ đó một lúc là cực khó, khó về mặt sinh lý. Nên kết luận rất thực dụng:

> [!quote] The Clean Coder — Ch.4 (tr. 58)
> "If you are tired or distracted, do not code. You'll only wind up redoing what you did."
>
> *Mệt hay đang phân tâm thì **đừng code**. Chỉ tổ làm lại đúng cái mình vừa làm mà thôi.*

Ông còn bàn tới **"worry code"** (tr. 60): khi trong đầu có một tiến trình nền cứ gặm nhấm mãi (vừa cãi nhau với vợ, con ốm, khách đang khủng hoảng), thì bạn ngồi trước màn hình mà đờ ra. Cách của ông là **chia vùng thời gian**: dành hẳn một khối (chừng một tiếng) để xử đúng cái nỗi lo đó (gọi về nhà, nói chuyện với vợ) cho nó hạ ưu tiên xuống, chứ đừng cố nặn ra thứ code rồi lại vứt đi.

## 3. Ca 1 — "Vùng Phập Phù" (the Zone): hãy tránh nó

**Chuyện gì đã xảy ra.** Nhiều lập trình viên tôn thờ cái trạng thái "flow" hay "the Zone" — tầm nhìn thu vào một đường hầm, thấy mình siêu năng suất và bất khả chiến bại, thậm chí đo giá trị bản thân bằng số giờ ngồi được trong đó. Uncle Bob thì đưa ra một lời khuyên ngược dòng:

> [!quote] The Clean Coder — Ch.4 (tr. 62)
> "Avoid the Zone. This state of consciousness is not really hyper-productive and is certainly not infallible."
>
> *Hãy **tránh** the Zone. Trạng thái ý thức đó thật ra chẳng siêu năng suất gì, và chắc chắn không phải là không thể sai.*

Lập luận của ông: trong Zone thì bạn viết code nhanh hơn thật, thấy lâng lâng thật, nhưng lại **đánh mất cái nhìn tổng thể**, nên hay ra những quyết định mà về sau phải quay lại đảo ngược — "Code written in the Zone may come out faster, but you'll be going back to visit it more" (tr. 62). Cách ông làm: hễ thấy mình đang trượt vào Zone thì đứng dậy đi ra ngoài vài phút, hoặc tìm một **cặp lập trình** (pair) — vì hai người ngồi cặp thì gần như không thể vào Zone (Zone là trạng thái im re không nói năng, còn pairing thì buộc phải trao đổi liên tục).

Ông cũng thú thật vài quy tắc rất riêng: **nhạc** không giúp anh code (có lần anh phát hiện cả lời bài *The Wall* lọt vào trong comment của mình!); về **ngắt quãng** — cái phản ứng cộc cằn khi bị ai đó hỏi han thường là từ chính the Zone mà ra; còn khi **bí ý** (writer's block) — cách chữa gần như luôn hiệu nghiệm là kiếm một pair partner, bởi "creative output depends on creative input" (với anh thì đó là truyện khoa học viễn tưởng).

## 4. Ca 2 — Cuộc gỡ lỗi 1972: thời gian debug cũng là tiền

**Chuyện gì đã xảy ra.** Năm 1972, các terminal của hệ kế toán Teamster cứ đóng băng một hai lần mỗi ngày, mà chẳng cách nào ép nó tái hiện theo ý mình. Riêng khâu chẩn đoán đã ngốn **mấy tuần**: đội phỏng vấn người dùng qua điện thoại (terminal đặt ở trung tâm Chicago, đội thì cách đó 30 dặm), không có log, không có counter, không có debugger — chỉ có mấy cái đèn và công tắc gạt trên bảng điều khiển. Họ tự viết lấy một "real-time inspector" bằng assembler để soi bộ nhớ ngay khi hệ đang chạy, rồi lần ra: mỗi khi terminal treo là do **ba biến quản lý bộ đệm vòng (circular buffer) bị lệch nhau**.

Nguyên nhân nằm sâu hơn: các "interrupt head" chạy ở một "luồng" khác, nên biến dùng chung phải được che khỏi chuyện cập nhật đồng thời — tức phải **tắt ngắt** (disable interrupts) quanh đoạn code nào có đụng vào ba biến ấy. Uncle Bob (19 tuổi) lật từng trang của tập in dày cả tấc, đi tìm chỗ nào đụng vào biến mà lại **quên tắt ngắt**. Cuối cùng anh cũng ra: một chỗ giữa code cập nhật một biến trong khi ngắt vẫn đang bật — một khe hở chỉ dài chừng **2 micro-giây**, mà đủ để gây treo một hai lần mỗi ngày.

**Điều rút ra.** Lập trình viên hay quên mất rằng thời gian ngồi gỡ lỗi cũng đắt ngang thời gian ngồi viết code:

> [!quote] The Clean Coder — Ch.4 (tr. 69)
> "a software developer who creates many bugs is acting unprofessionally."
>
> *một lập trình viên đẻ ra lắm bug là đang hành xử **thiếu chuyên nghiệp**.*

Uncle Bob nói nhờ áp dụng TDD (chủ đề [Bài 5](bai_05_tdd.md)) mà anh đã giảm thời gian debug đi **cỡ 10 lần** so với mười năm trước. Dù bạn theo TDD hay một kỷ luật tương đương, thì bổn phận nghề nghiệp vẫn là kéo thời gian debug về càng gần zero càng tốt. So với năm 1972 khi công cụ chỉ có mỗi "đôi mắt", đây chính là chỗ 2026 đã đổi khác tận gốc (xem [Đối chiếu 2026](#8-đối-chiếu-2026)).

## 5. Giữ nhịp: marathon chứ không phải chạy nước rút

> [!quote] The Clean Coder — Ch.4 (tr. 69)
> "Software development is a marathon, not a sprint. You can't win the race by trying to run as fast as you can from the outset."
>
> *Làm phần mềm là chạy **marathon, không phải nước rút**. Không ai thắng cuộc đua bằng cách lao hết tốc lực ngay từ vạch xuất phát.*

Từ đó ra một loạt quy tắc giữ sức. **Biết lúc nào nên buông** — không giải được thì cứ về nhà, đừng ngồi nện cái não đã kiệt hết tiếng này qua tiếng khác. **Lái xe về** và **đứng dưới vòi sen** là hai chỗ Uncle Bob giải được vô số bài toán, bởi chính lúc *ngắt ra khỏi vấn đề* thì tiềm thức mới có khoảng để mò lời giải mà sự tập trung căng cứng đang bóp nghẹt.

## 6. Trễ hạn, hy vọng, tăng ca và ba con số

**Chuyện gì đã xảy ra.** Rồi sẽ có lúc bạn trễ hạn — chuyện đó xảy ra với cả những người giỏi nhất. Vấn đề là quản nó thế nào:

> [!quote] The Clean Coder — Ch.4 (tr. 71)
> "The trick to managing lateness is early detection and transparency."
>
> *Mẹo để quản chuyện trễ hạn là **phát hiện sớm và minh bạch**.*

Thay vì tới phút chót vẫn cứ hứa "sẽ kịp" rồi làm cả nhà vỡ mộng, hãy đo tiến độ đều đặn và đưa ra **ba con số dựa trên sự thật**: tốt nhất / bình thường / xấu nhất — cập nhật hằng ngày, và tuyệt đối:

> [!quote] The Clean Coder — Ch.4 (tr. 71)
> "Do not incorporate hope into your estimates! […] Hope is the project killer."
>
> *Đừng nhét **hy vọng** vào ước lượng! […] Hy vọng là **kẻ giết dự án**.*

Nếu triển lãm còn 10 ngày nữa mà ước lượng của bạn là 8/12/20, thì bạn **sẽ không kịp** — phải cho cả đội và các bên thấy rõ tình hình và chuẩn bị phương án dự phòng, đừng để ai còn ôm hy vọng hão. Còn khi sếp ép "cứ cố đi", thì **giữ lấy con số ước lượng của bạn** — bản gốc bao giờ cũng chuẩn hơn mấy con số bạn sửa vội dưới áp lực; muốn cải thiện lịch thì chỉ có cách *cắt bớt phạm vi*, chứ không phải chạy nhanh hơn ("There is no way to rush", tr. 72). Còn về **tăng ca**, ông đặt ba điều kiện cứng, mà điều thứ ba mới là điểm phá vỡ thoả thuận:

> [!quote] The Clean Coder — Ch.4 (tr. 72)
> "you should not agree to work overtime unless (1) you can personally afford it, (2) it is short term, two weeks or less, and (3) your boss has a fall-back plan in case the overtime effort fails."
>
> *đừng đồng ý tăng ca trừ khi (1) bản thân bạn kham nổi, (2) chỉ ngắn hạn, tối đa hai tuần, và (3) sếp có sẵn **phương án dự phòng** phòng khi tăng ca vẫn thất bại.*

Bởi "You are not likely to get 20% more work done by working 20% more hours" (tr. 72) — làm thêm 20% giờ đâu có nghĩa là ra thêm được 20% việc.

## 7. Giao hàng giả và định nghĩa "Xong"

> [!quote] The Clean Coder — Ch.4 (tr. 73)
> "Of all the unprofessional behaviors that a programmer can indulge in, perhaps the worst of all is saying you are done when you know you aren't."
>
> *Trong mọi thói thiếu chuyên nghiệp, có lẽ tệ nhất là **nói mình đã xong trong khi biết thừa là chưa**.*

Còn nguy hiểm hơn cả một lời nói dối trắng trợn, là khi ta **tự bịa ra một định nghĩa mới cho chữ "xong"** ("xong đủ dùng rồi", "phần còn lại để sau"). Cái thói này lây: một người co giãn định nghĩa, người khác thấy vậy cũng bắt chước rồi nới thêm. Uncle Bob kể có khách hàng từng định nghĩa "done" là "đã check-in" — code còn chẳng cần compile được! Cả đội mà sa vào bẫy này thì mọi báo cáo đều "đúng tiến độ", y như "một đám người mù đi picnic trên đường ray: chẳng ai thấy đoàn tàu công-việc-chưa-xong đang lao tới". Cách chống lại: dựng một **định nghĩa "Xong" độc lập** bằng *acceptance test tự động* (chủ đề [Bài 7](bai_07_acceptance_testing.md)), viết bằng thứ ngôn ngữ mà cả bên nghiệp vụ cũng đọc hiểu.

Chương khép lại bằng phần **Help**: lập trình khó tới mức vượt sức một người; từ chối giúp nhau là phạm vào đạo đức nghề, mà **biết mở miệng xin giúp** cũng là một bổn phận — "It is unprofessional to remain stuck when help is easily accessible" (tr. 74). Có một chi tiết đáng lưu để đối chiếu 2026: ông thừa nhận mình đang vẽ nên một **định kiến** ("lập trình viên là kẻ hướng nội, kiêu ngạo, tự mê"), rồi kết: chính vì cộng tác *không* phải bản năng của nhiều người trong nghề, nên ta **cần một kỷ luật để ép mình cộng tác**.

## 8. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — phần "the Zone"
> Đây là luận điểm **gây tranh cãi nhất** chương, và phần lớn 2026 **không đồng ý** với Uncle Bob. Lời khuyên "tránh the Zone" của ông dính liền với việc ông cổ vũ *pair programming*. Nhưng dòng nghiên cứu về năng suất tri thức sau 2011 (tiêu biểu là *Deep Work* của Cal Newport) lại **tôn vinh** trạng thái tập trung sâu như nguồn của công việc giá trị cao. Cách hoà giải là tách ra hai thứ mà ông gộp làm một: *flow lành mạnh* (tập trung sâu nhưng vẫn giữ được cái nhìn tổng thể) thì đáng quý; còn cái ông mô tả (tầm nhìn đường hầm khiến bỏ sót cả bức tranh thiết kế lớn) mới là **tunnel vision** đáng tránh. 2026 giữ lấy giá trị của tập trung sâu, mà vẫn giữ luôn ý ông: cứ *chủ động bước ra ngắm lại bức tranh lớn* theo chu kỳ. Pair/mob programming thì vẫn dùng, nhưng như *một lựa chọn*, chứ không phải một mệnh lệnh chống-Zone.
>
> [!warning] Đối chiếu 2026 — phần đã già đi đẹp
> Ngược lại, phần lớn chương này lại **đúng hơn theo năm tháng**: "đừng code khi mệt", "marathon chứ không phải nước rút", "hope is the project killer", ba mốc best/nominal/worst, và **ba điều kiện tăng ca** — tất cả đều khớp với hiểu biết 2026 về burnout và về *sustainable pace* (xem thêm [Bài 11](bai_11_ap_luc.md)). "Định nghĩa Xong bằng acceptance test tự động" thì chính là **Definition of Done** cộng với BDD ngày nay (Cucumber vẫn dùng; còn FitNesse/RobotFX đã lỗi thời). Cuộc gỡ lỗi 1972 làm nổi bật đúng cái ông nói: 2026 ta có debugger, log tập trung, tracing, static analysis, cả *time-travel debugging* — chỗ ông mất *mấy ngày* lật giấy, nay chỉ còn *vài phút*; nên chuẩn "kéo thời gian debug về gần zero" lại càng khả thi. Riêng con số "TDD giảm debug 10 lần" chỉ là giai thoại cá nhân của ông; 2026 xem TDD là *một* kỷ luật mạnh, chứ không phải con đường duy nhất — chuyện này sẽ bàn kỹ ở [Bài 5](bai_05_tdd.md).
>
> [!warning] Đối chiếu 2026 — cái định kiến
> Cái hình ảnh "lập trình viên = kẻ hướng nội kiêu ngạo, chọn nghề vì không ưa con người" (kèm cả cái chú thích đối lập "chinh phục quái vật" của nam với "nuôi dưỡng sáng tạo" của nữ) là một **định kiến vừa lỗi thời vừa hẹp hòi**. 2026 xem cộng tác, giao tiếp và sự đa dạng là *năng lực cốt lõi* của nghề, chứ không phải ngoại lệ dành cho một nhóm "vốn không ưa người". Cứ giữ lấy kết luận đúng của ông ("cần kỷ luật để cộng tác"), nhưng bỏ đi cái khung định kiến đã dẫn ông tới đó.

## 9. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Truy tìm "đoạn code 3 giờ sáng" của bạn.** Lục trong codebase một chỗ bạn viết lúc kiệt sức mà giờ ai cũng phải né. Nó đã ngốn bao nhiêu lần vá rồi? Tự đặt cho mình một luật: quá giờ nào thì *ngừng* code.
> 2. **Thí nghiệm với the Zone.** Trong một tuần, ghi lại: đoạn code nào bạn viết trong "tunnel vision" mà sau phải quay lại sửa? Đem so với đoạn viết lúc *tập trung sâu nhưng vẫn thi thoảng ngẩng lên nhìn bức tranh lớn*. Bạn nghiêng về phía nào trong cuộc tranh luận Uncle Bob vs *Deep Work*?
> 3. **Ba con số thay cho một lời hứa.** Việc kế tiếp, thay vì báo mỗi một ngày, hãy báo best/nominal/worst rồi cập nhật hằng ngày — và soi lại ba điều kiện tăng ca trước khi gật đầu làm thêm.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **"Hy vọng là kẻ giết dự án" trong nghề bạn.** Nhớ một lần bạn (hoặc sếp) nhét hy vọng vào một kế hoạch thay vì nhìn thẳng vào sự thật. Cái giá là gì? Nếu "phát hiện sớm + minh bạch" thì kết cục đã khác ra sao?
> 2. **Định nghĩa "Xong" của bạn.** Trong công việc của bạn (một báo cáo, một bản thiết kế, một bài giảng), chữ "xong" có bị co giãn tuỳ hứng không? Viết ra một định nghĩa "Xong" *độc lập, kiểm chứng được* cho một đầu việc sắp tới.

## 10. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Error-sense** (giác quan-lỗi) | Khả năng cảm thấy mình vừa sai gần như tức thì, đóng vòng phản hồi nhanh — nền của sự tinh thông (tr. 58). |
| **3 AM code / worry code** | Code viết lúc kiệt sức hoặc đầu óc bị nỗi lo nền chiếm — chất lượng rác, phải vứt (tr. 59–60). |
| **The Zone** (vùng phập phù) | Trạng thái tầm-nhìn-đường-hầm; Uncle Bob khuyên tránh, 2026 tách thành *flow lành mạnh* (giữ) vs *tunnel vision* (tránh) (tr. 62). |
| **Ba con số ước lượng** | best / nominal / worst dựa trên sự thật, cập nhật hằng ngày — không nhét hy vọng (tr. 71). |
| **Hope is the project killer** | Ôm hy vọng thay vì đối diện dữ liệu ước lượng = giết lịch và danh tiếng (tr. 71). |
| **Ba điều kiện tăng ca** | (1) kham được, (2) ≤ 2 tuần, (3) sếp có phương án dự phòng (tr. 72). |
| **False delivery** (giao hàng giả) | Nói "xong" khi biết chưa xong, thường bằng cách co giãn định nghĩa "Xong" (tr. 73). |

## 11. Câu hỏi tự kiểm tra

1. Bài học của "đoạn code 3 giờ sáng" là gì — và vì sao kỷ luật quan trọng hơn số giờ? *(tr. 59–60)*
2. Bốn mối lo cạnh tranh khi viết code là gì? *(tr. 58–59)*
3. Uncle Bob khuyên gì về "the Zone", và 2026 hoà giải lời khuyên đó thế nào?
4. Vì sao "thời gian debug cũng đắt như thời gian code"? Cuộc gỡ lỗi 1972 minh hoạ điều gì về công cụ? *(tr. 69)*
5. Ba con số nào thay cho một lời hứa khi báo tiến độ, và vì sao "hope is the project killer"? *(tr. 71)*
6. Ba điều kiện để đồng ý tăng ca là gì? Điều kiện nào là "deal breaker"? *(tr. 72)*

## Tóm tắt một trang

```
BÀI 4 — VIẾT CODE: KỶ LUẬT CỦA TÂM TRÍ, KHÔNG PHẢI SỐ GIỜ
────────────────────────────────────────────────────────
MỞ ĐẦU  1988, 3 giờ sáng: code "gửi mail cho chính mình" — giải
        pháp sai, ám cả đội nhiều năm. "How wrong I was!" (tr. 59).
        → kỷ luật > số giờ (tr. 60). Nền: confidence + error-sense.

CHUẨN BỊ  Code = tung hứng 4 mối lo: chạy · giải đúng vấn đề khách
        · khớp hệ · đọc được (tr. 58). Mệt/phân tâm → ĐỪNG code.

CA 1  The Zone: "Avoid the Zone" (tr. 62) — mất bức tranh lớn.
      2026: tách flow-lành-mạnh (GIỮ) vs tunnel-vision (TRÁNH).

CA 2  Gỡ lỗi 1972: ba biến buffer lệch, khe hở 2µs quên tắt ngắt,
      mất NHIỀU NGÀY lật giấy. "Nhiều bug = thiếu chuyên nghiệp"
      (tr. 69). 2026: debugger/tracing → vài phút.

GIỮ NHỊP  "Marathon, not a sprint" (tr. 69). Bí thì rời đi; vòi
        sen/lái xe giải được bài toán.

TRỄ HẠN  Phát hiện sớm + minh bạch (tr. 71). Ba con số 8/12/20.
        "Hope is the project killer" (tr. 71). Giữ ước lượng, giảm
        scope chứ đừng rush. Tăng ca: 3 điều kiện (tr. 72).

XONG  Tệ nhất: nói xong khi chưa (tr. 73). Chống bằng định nghĩa
      "Done" độc lập = acceptance test tự động.

2026  Đúng hơn theo thời gian: pace/hope/overtime/Define-Done.
      Tranh cãi: "avoid the Zone". Lỗi thời: định kiến "coder
      hướng nội kiêu ngạo".
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.4 **Coding** (`tr. 57–76`): gõ mù & error-sense (tr. 57–58); "Preparedness" — 4 mối lo, "worry code" (tr. 58–61); "3 AM Code" (tr. 59–60); "The Flow Zone", music, interruptions, writer's block (tr. 62–65); "Debugging" — ca 1972 Teamster, "Debugging Time" (tr. 66–69); "Pacing Yourself", walk away, shower (tr. 69–70); "Being Late", hope, rushing, overtime (tr. 71–72); "False Delivery" & "Define Done" (tr. 73); "Help" & mentoring (tr. 73–76). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 ← bạn đang ở đây] · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
