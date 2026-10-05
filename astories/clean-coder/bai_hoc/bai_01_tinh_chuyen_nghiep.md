# Bài 1 — Tính chuyên nghiệp: tấm huy chương có hai mặt

> [!info] Về bài này
> Dựng từ **Chương 1 — Professionalism** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 7–22`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Cần đọc trước: [Bài 0 — Nhập môn](bai_00_nhap_mon.md).
> Mỗi ca đi theo mạch *chuyện xảy ra → điều rút ra → `[!warning] Đối chiếu 2026` → `[!question] Áp dụng*.

## Mục lục

1. [Mở đầu: đêm mất trắng dữ liệu ở Teradyne](#1-mở-đầu-đêm-mất-trắng-dữ-liệu-ở-teradyne)
2. [Chuyên nghiệp = danh dự cộng trách nhiệm](#2-chuyên-nghiệp--danh-dự-cộng-trách-nhiệm)
3. [Ca 1 — Bài học từ đêm Teradyne: trách nhiệm là gì](#3-ca-1--bài-học-từ-đêm-teradyne-trách-nhiệm-là-gì)
4. [Ca 2 — "QA không được tìm thấy gì" và đòi hỏi 100%](#4-ca-2--qa-không-được-tìm-thấy-gì-và-đòi-hỏi-100)
5. [Không gây hại cho cấu trúc: quy tắc Nam Hướng Đạo](#5-không-gây-hại-cho-cấu-trúc-quy-tắc-nam-hướng-đạo)
6. [Ca 3 — Đạo đức nghề: "sự nghiệp là của bạn" và công thức 60 giờ](#6-ca-3--đạo-đức-nghề-sự-nghiệp-là-của-bạn-và-công-thức-60-giờ)
7. [Biết nghề mình và học không ngừng](#7-biết-nghề-mình-và-học-không-ngừng)
8. [Khiêm nhường: lập trình là hành vi kiêu ngạo tột cùng](#8-khiêm-nhường-lập-trình-là-hành-vi-kiêu-ngạo-tột-cùng)
9. [Áp dụng vào việc của bạn](#9-áp-dụng-vào-việc-của-bạn)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
12. [Tóm tắt một trang](#tóm-tắt-một-trang)
13. [Nguồn](#nguồn)

---

## 1. Mở đầu: đêm mất trắng dữ liệu ở Teradyne

Năm **1979**, Uncle Bob là "responsible engineer" — người gánh trọn trách nhiệm — cho phần mềm điều khiển một hệ đo chất lượng đường dây điện thoại ở Teradyne. Một máy mini trung tâm nối qua đường 300-baud tới hàng chục máy vệ tinh; tất cả viết bằng assembler. Khách hàng là các quản lý dịch vụ của những công ty điện thoại lớn, mỗi người trông coi hơn 100.000 đường dây. Đêm nào hệ thống cũng chạy một "nightly routine": trung tâm ra lệnh cho từng vệ tinh test mọi đường dây, sáng ra gom về danh sách đường lỗi để thợ đi sửa **trước khi** khách kịp than phiền.

Một bận, Uncle Bob ship bản mới — ship theo đúng nghĩa đen: ghi phần mềm ra băng từ rồi gửi băng cho khách. Bản này sửa vài lỗi nhỏ, thêm một tính năng khách đang chờ, và đã hứa giao đúng ngày. Anh chạy nước rút cho kịp. Chỉ có điều bài test cho nightly routine chạy mất **mấy tiếng**, nên anh bỏ qua, tự nhủ mấy bản sửa lỗi có đụng gì tới code của routine đâu mà lo.

Hai hôm sau, Tom — quản lý dịch vụ hiện trường — gọi tới: hàng loạt khách báo nightly routine không chạy xong, sáng ra chẳng có báo cáo nào. Mất một đêm dữ liệu nghĩa là thợ sửa bị dồn việc, khách bắt đầu kêu, còn Tom thì bị các quản lý dịch vụ "nướng" trên lửa. Uncle Bob nạp phần mềm mới vào hệ lab, chạy routine — mấy tiếng sau nó **abort**, đúng như anh lo. Anh đành bảo khách quay về bản cũ (đòn kép: vừa mất một đêm dữ liệu, vừa mất luôn tính năng mới đã hứa), rồi mất **cả mấy ngày**, sửa hụt vài lần mới ra được lỗi.

> [!quote] The Clean Coder — Ch.1 (tr. 9)
> "in order to ship the software on time, I had neglected to test the routine."
>
> *chỉ vì muốn ship phần mềm kịp hạn mà tôi đã bỏ khâu test cái routine.*

Xong xuôi rồi, ngồi ngẫm lại, anh thấy nguyên nhân thật ra chẳng nằm ở kỹ thuật:

> [!quote] The Clean Coder — Ch.1 (tr. 10)
> "It was about me saving face. I had not been concerned about the customer, nor about my employer. I had only been concerned about my own reputation."
>
> *Chung quy là tôi giữ thể diện. Tôi đâu có bận tâm tới khách hàng, cũng chẳng nghĩ tới công ty. Tôi chỉ lo cho danh tiếng của riêng mình.*

Cả chương 1 khởi nguồn từ chính đêm đó.

## 2. Chuyên nghiệp = danh dự cộng trách nhiệm

Uncle Bob mở chương bằng hình ảnh ai cũng thầm *muốn*: được gọi là "chuyên nghiệp", được ngẩng cao đầu, được nể trọng, được các bà mẹ chỉ vào mà bảo con "hãy noi gương chú kia". Rồi ông lật cho ta xem mặt sau tấm huy chương:

> [!quote] The Clean Coder — Ch.1 (tr. 8)
> "Certainly it is a badge of honor and pride, but it is also a marker of responsibility and accountability. […] You can't take pride and honor in something that you can't be held accountable for."
>
> *Đúng, nó là tấm huy hiệu của danh dự và tự hào, nhưng cũng là dấu của trách nhiệm và sự chịu trách nhiệm. […] Bạn không thể tự hào về một thứ mà mình không dám đứng ra chịu.*

Ông minh hoạ bằng một ví dụ rất đắt: một con bug lọt lưới, làm công ty thiệt **10.000 đô**. Dân nghiệp dư nhún vai "chuyện thường ấy mà" rồi quay sang viết module kế. Còn người chuyên nghiệp thì:

> [!quote] The Clean Coder — Ch.1 (tr. 8)
> "The professional would write the company a check for \$10,000! […] professionalism is all about taking responsibility."
>
> *Người chuyên nghiệp sẽ viết cho công ty một tấm séc 10.000 đô! […] chuyên nghiệp, rốt cuộc, chỉ là chuyện dám nhận lấy trách nhiệm.*

Cái cảm giác "đây là tiền túi của mình" ấy, theo Uncle Bob, chính là thứ người chuyên nghiệp mang trong người **suốt cả ngày làm việc**. Và đó là ranh giới sâu xa nhất phân tách dân nghiệp dư với người chuyên nghiệp.

## 3. Ca 1 — Bài học từ đêm Teradyne: trách nhiệm là gì

**Điều rút ra.** Từ đêm mất dữ liệu ấy, Uncle Bob rút ra nguyên tắc đầu tiên, mượn từ lời thề Hippocrates của ngành y: **"First, do no harm"** — trước hết, đừng gây hại. Với lập trình viên, gây hại nghĩa là đẻ ra bug:

> [!quote] The Clean Coder — Ch.1 (tr. 11)
> "We harm the function of our software when we create bugs. Therefore, in order to be professional, we must not create bugs."
>
> *Cứ tạo ra bug là ta làm hại chức năng của phần mềm. Vậy nên, muốn chuyên nghiệp thì **không được tạo ra bug**.*

Ông biết thừa cái phản bác sẽ tới: phần mềm phức tạp thế, viết sao cho hết lỗi được? Ông không chối, nhưng đáp lại bằng phép so với bác sĩ: cơ thể người cũng phức tạp đến mức không ai hiểu thấu, vậy mà thầy thuốc vẫn thề "do no harm" đấy thôi. Kết luận không phải là "phải hoàn hảo", mà là **phải chịu trách nhiệm cho cái bất toàn của mình**:

> [!quote] The Clean Coder — Ch.1 (tr. 11)
> "you must be responsible for your imperfections. […] your error rate should rapidly decrease towards the asymptote of zero."
>
> *bạn phải chịu trách nhiệm cho những khiếm khuyết của mình. […] tỉ lệ lỗi của bạn phải giảm thật nhanh, tiệm cận về zero.*

Việc đầu tiên phải luyện, theo ông, là **biết xin lỗi** — nhưng xin lỗi thôi thì chưa đủ; cái chính là đừng vấp mãi cùng một lỗi.

## 4. Ca 2 — "QA không được tìm thấy gì" và đòi hỏi 100%

**Chuyện gì đã xảy ra.** Từ nguyên tắc "do no harm", Uncle Bob đẩy tới một đòi hỏi rất gắt: giao code cho QA thì bạn phải **kỳ vọng QA chẳng tìm ra lỗi nào**.

> [!quote] The Clean Coder — Ch.1 (tr. 12)
> "when you release your software you should expect QA to find no problems. It is unprofessional in the extreme to purposely send code that you know to be faulty to QA."
>
> *khi phát hành phần mềm, bạn nên kỳ vọng QA **không tìm thấy vấn đề gì**. Cố tình đẩy cho QA đoạn code mà mình biết là lỗi thì thiếu chuyên nghiệp tới cùng cực.*

Làm sao để chắc code chạy đúng? Thì test — mà phải là test tự động, để chạy được bất cứ lúc nào. Rồi ông chốt một con số vào loại gây tranh cãi nhất cả cuốn sách:

> [!quote] The Clean Coder — Ch.1 (tr. 13)
> "Am I suggesting 100% test coverage? No, I'm not suggesting it. I'm demanding it. Every single line of code that you write should be tested. Period."
>
> *Tôi có đang gợi ý phủ 100% test không? Không, tôi không gợi ý. Tôi **đòi hỏi** điều đó. Mọi dòng code bạn viết ra đều phải được test. Chấm hết.*

Ông lấy chính dự án mã nguồn mở của mình ra làm bằng — FitNesse: 60k dòng, hơn 2000 unit test, công cụ Emma báo phủ khoảng 90% — để chứng minh "QA tự động" là chuyện làm được: cả bộ test chạy hết trong tầm 3 phút, pass là ship.

> [!warning] Đối chiếu 2026
> **Phần còn sống:** cái tinh thần "tự động hoá khâu kiểm tra để biết chắc code chạy trước khi giao" nay đã thành dòng chính, mang một cái tên khác: *CI/CD*. Mỗi lần push là test tự động chạy, đỏ thì chặn merge. Thứ Uncle Bob mô tả như một kỷ luật cá nhân, giờ đã là *hạ tầng* ép người ta làm. Còn cái nguyên tắc "đừng đẩy code mình biết là lỗi cho người khác" thì vẫn nguyên là chuẩn mực.
> **Phần đã lỗi thời / gây tranh cãi:** cái đòi hỏi tuyệt đối **"100% coverage, mọi dòng, chấm hết"** thì phần lớn cộng đồng ngày nay bác bỏ, coi đó là một *mục tiêu sai*. Lý do: coverage chỉ đo *dòng nào được chạy*, chứ không đo *code có đúng hay không* — phủ 100% vẫn có thể bỏ sót vô số ca biên. Con số ấy còn dễ bị "gian" (viết test rỗng cho đủ phần trăm), mà mấy dòng cuối cùng để chạm mốc 100% thì tốn kém một cách vô lý. 2026 người ta chuộng *test có ý nghĩa* cộng với những kỹ thuật mạnh hơn: **mutation testing** (đo xem test có thật sự bắt được lỗi không), **property-based testing**, và phân tầng theo mức rủi ro. Mấy công cụ ông dẫn (FitNesse, Emma) thì cũng cũ cả rồi. Giữ lấy tinh thần "biết chắc code chạy"; **bỏ** con số 100% như một mệnh lệnh.

## 5. Không gây hại cho cấu trúc: quy tắc Nam Hướng Đạo

"Do no harm" còn một mặt thứ hai: đừng hại **cấu trúc** của code. Lập luận của Uncle Bob: cả ngành phần mềm đứng trên một giả định nền, rằng "phần mềm thì *dễ sửa*"; hễ bạn dựng nên cấu trúc cứng nhắc là bạn phá luôn cái mô hình kinh tế đó. Mà cách duy nhất để chứng minh phần mềm dễ sửa là **cứ sửa nó luôn tay** — ông đặt hẳn tên cho thói quen này:

> [!quote] The Clean Coder — Ch.1 (tr. 15)
> "I call it 'the Boy Scout rule': Always check in a module cleaner than when you checked it out."
>
> *Tôi gọi đó là "quy tắc Nam Hướng Đạo": **luôn check-in một module sạch hơn lúc bạn check-out.***

Vì sao đa số ngại đụng vào code đang chạy? Vì sợ làm hỏng. Vì sao sợ làm hỏng? Vì **không có test**. Rốt cuộc mọi thứ lại quay về test: có sẵn một bộ test tự động phủ gần hết và chạy nhanh, thì bạn chẳng còn sợ sửa code nữa.

> [!warning] Đối chiếu 2026
> Đây là phần **già đi đẹp nhất** cả chương. "Boy Scout rule" và lối *refactoring liên tục dựa trên lưới an toàn là test* nay đã thành văn hoá phổ biến, nhúng thẳng vào quy trình *code review* và *pull request*. Chỉ cần chỉnh một chút về sắc thái: cụm "merciless refactoring" hay "đổi tên class theo hứng" phải đi kèm kỷ luật commit nhỏ, có review, và — trong đội đông — biết cân cả chi phí review của người khác. Còn nguyên tắc thì vẫn vẹn nguyên.

## 6. Ca 3 — Đạo đức nghề: "sự nghiệp là của bạn" và công thức 60 giờ

**Chuyện gì đã xảy ra.** Uncle Bob nêu một nguyên tắc mạnh về trách nhiệm với chính mình:

> [!quote] The Clean Coder — Ch.1 (tr. 16)
> "Your career is your responsibility. It is not your employer's responsibility to make sure you are marketable."
>
> *Sự nghiệp của bạn là trách nhiệm của **bạn**. Giữ cho bạn còn giá trị trên thị trường không phải việc của công ty.*

Rồi ông tung ra cái công thức thời gian vừa nổi tiếng vừa tai tiếng:

> [!quote] The Clean Coder — Ch.1 (tr. 16)
> "You should plan on working 60 hours per week. The first 40 are for your employer. The remaining 20 are for you."
>
> *Bạn nên tính làm 60 giờ mỗi tuần. 40 giờ đầu cho công ty. 20 giờ còn lại là cho chính bạn* (để đọc, để luyện, để học).

Ông ngồi "làm toán" cho ta yên tâm: một tuần có 168 giờ, trừ 40 cho công ty, 20 cho sự nghiệp, 56 cho giấc ngủ, thì vẫn còn tới 52 giờ cho mọi thứ khác. Ông cả quyết rằng 20 giờ ấy **không** phải công thức dẫn tới burnout, mà là cách để *tránh* burnout — "Those 20 hours should be fun!". Còn ai không chịu cam kết kiểu đó, theo ông, thì "đừng nên tự nhận mình chuyên nghiệp".

> [!warning] Đối chiếu 2026
> Đây là đoạn **gây tranh cãi nhất** cả cuốn sách, và phần lớn đã bị 2026 bác bỏ.
> **Cái còn đúng — cái lõi:** "sự nghiệp là trách nhiệm của bạn; đừng phó thác việc học cho công ty; hãy chủ động trau dồi." Điều này vẫn vững, mà giữa thị trường công nghệ đổi nhanh năm 2026 còn vững hơn.
> **Cái đã sai / lỗi thời — cái vỏ:** cái công thức cứng **"60 giờ/tuần, không thì không phải dân chuyên nghiệp"** ngày nay bị coi là *chuẩn hoá việc làm quá sức*, và **mù trước đặc quyền**. Nó ngầm cho rằng người đọc là nam, trẻ, độc thân, khoẻ mạnh, không con nhỏ, không phải chăm ai — bỏ quên cha mẹ đơn thân, người có bệnh nền, người còn gánh gia đình. Các nghiên cứu về năng suất và sức khoẻ sau 2011 khá thống nhất: **giờ làm cứ kéo dài thì năng suất tụt** và rủi ro burnout tăng, ngược hẳn điều ông khẳng định. 2026 người ta tách bạch rõ: *cam kết học cả đời* (giữ) là một chuyện, còn *đo sự chuyên nghiệp bằng số giờ cày ngoài lương* (bỏ) lại là chuyện khác. Bạn hoàn toàn có thể là một lập trình viên xuất sắc, ham học, mà **không** cần cày thêm 20 giờ mỗi tuần ngoài giờ.

## 7. Biết nghề mình và học không ngừng

Uncle Bob quay ra "khảo bài" người đọc: bạn có biết Nassi-Schneiderman chart là gì, có phân biệt được máy trạng thái Mealy với Moore, có viết nổi quicksort mà không cần tra không? Ông đòi người chuyên nghiệp phải nắm một "khối" tri thức tích 50 năm của ngành và liên tục nới rộng nó ra, kèm lời cảnh báo mượn của Santayana:

> [!quote] The Clean Coder — Ch.1 (tr. 18)
> "Those who cannot remember the past are condemned to repeat it."
>
> *Ai không nhớ nổi quá khứ thì bị kết án phải lặp lại nó.*

Ông cũng vạch ra một cặp khái niệm quan trọng, sẽ còn trở lại ở [Bài 6](bai_06_luyen_tap.md):

> [!quote] The Clean Coder — Ch.1 (tr. 19)
> "Doing your daily job is performance, not practice."
>
> *Làm công việc hằng ngày là **biểu diễn**, chứ không phải **luyện tập**.*

> [!note] Mở rộng — danh sách "phải biết" của Uncle Bob và 2026
> Ông liệt kê những thứ tối thiểu phải thông: **Design patterns** (24 mẫu trong sách GOF), **SOLID** cùng các nguyên lý về component, **Methods** (XP, Scrum, Lean, Kanban, Waterfall), **Disciplines** (TDD, OO, CI, Pair Programming), **Artifacts** (UML, DFD, biểu đồ trạng thái…). Đối chiếu 2026: một nửa danh sách vẫn là nền tảng (SOLID, Scrum/Kanban, CI, TDD); vài mục đã lùi về ngách (Nassi-Schneiderman, Petri Net, Structure Chart). Đổi lại, danh sách **thiếu** hẳn những thứ năm 2011 chưa nổi mà nay là căn bản: điện toán đám mây, hệ phân tán, an ninh (security by design), quan sát vận hành (observability), và lập trình có **AI hỗ trợ**. Bài học thì vẫn thế — *phải biết lịch sử và nền tảng của nghề* — chỉ có "khối tri thức" là đã dịch chuyển.

Rồi ông nhắc lại phép so với ngành y để chốt phần "học không ngừng": "Would you visit a doctor who did not keep current with medical journals?" (tr. 19) — bạn có đi khám một ông bác sĩ chẳng buồn cập nhật tạp chí y khoa không? Vậy cớ gì công ty phải thuê một lập trình viên chẳng chịu cập nhật?

## 8. Khiêm nhường: lập trình là hành vi kiêu ngạo tột cùng

Chương khép lại bằng một nghịch lý đẹp. Lập trình, theo Uncle Bob, là *dựng trật tự lên từ hỗn mang*, là ra lệnh chi li cho một cỗ máy vốn có thể gây hại khôn lường — nên tự nó đã là "một hành vi kiêu ngạo tột cùng":

> [!quote] The Clean Coder — Ch.1 (tr. 22)
> "programming is an act of supreme arrogance. Professionals know they are arrogant and are not falsely humble."
>
> *lập trình là một hành vi kiêu ngạo tột cùng. Người chuyên nghiệp **biết** mình kiêu ngạo, và không giả bộ khiêm tốn.*

Người chuyên nghiệp tự tin, dám nhận những rủi ro có tính toán — nhưng cũng thừa biết sẽ có lúc mình tính sai, thất bại, soi gương rồi thấy "một gã ngốc kiêu ngạo đang cười lại". Cho nên khi thành trò cười, họ là người **bật cười trước tiên**; và họ chẳng bao giờ hạ nhục ai vì một cái lỗi, bởi biết đâu người ngã kế tiếp chính là mình. Lời khuyên cuối cùng, mượn của nhân vật Howard trong bộ phim mở đầu chương, gọn lỏn: *Laugh.* — Cứ cười thôi.

## 9. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Soi lại "đêm Teradyne" của bạn.** Lần gần nhất bạn bỏ một bước kiểm chỉ vì "chắc không sao / cho kịp deadline" là khi nào? Kết cục ra sao? Nếu hồi đó có CI chặn merge khi test đỏ, liệu nó đã chặn được không?
> 2. **Đặt lại mục tiêu test cho đúng thời 2026.** Thay câu hỏi "code mình phủ được bao nhiêu phần trăm?" bằng câu "những **đường đi và ca biên nào** mới thật sự có rủi ro, và mình đã có test *có ý nghĩa* cho chúng chưa?".
> 3. **Thử quy tắc Nam Hướng Đạo một tuần.** Mỗi lần đụng vào một file, để nó sạch hơn một chút (đổi cái tên khó hiểu, tách một hàm quá dài). Cuối tuần nhìn lại diff.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **Mặt sau tấm huy chương.** Với nghề của bạn (viết, thiết kế, tư vấn, dạy học…), "chịu trách nhiệm" cụ thể là gì? Cái "tấm séc 10.000 đô" tương đương trong nghề bạn trông ra sao?
> 2. **Tách lõi khỏi vỏ trong lời khuyên "60 giờ".** Bạn *làm chủ* con đường nghề của mình tới đâu — và có đang nhầm "chuyên nghiệp" với "hi sinh sức khoẻ, gia đình" không? Viết ra một định nghĩa "học liên tục" hợp với hoàn cảnh thật của bạn.

## 10. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Accountability** (sự chịu trách nhiệm) | Sẵn sàng gánh hậu quả việc mình làm — mặt sau của "danh dự" nghề (tr. 8). |
| **First, do no harm** | Nguyên tắc mượn từ y khoa: đừng hại *chức năng* (bug) lẫn *cấu trúc* (code cứng nhắc) của phần mềm (tr. 11–14). |
| **QA should find nothing** | Kỳ vọng QA không tìm ra lỗi — vì bạn đã tự kiểm trước; 2026 hiện thực hoá bằng CI (tr. 12). |
| **Boy Scout rule** (quy tắc Nam Hướng Đạo) | Luôn để lại module sạch hơn lúc nhận; refactoring liên tục dựa trên lưới test (tr. 15). |
| **Performance vs practice** | *Biểu diễn* (việc hằng ngày) khác *luyện tập* (rèn kỹ năng ngoài công việc) — nền của [Bài 6](bai_06_luyen_tap.md) (tr. 19). |
| **Coverage / mutation testing** | Coverage = % dòng được test chạy (không đo tính đúng); mutation testing = đo test có thật sự bắt lỗi — thước đo 2026 thay cho "100%". |

## 11. Câu hỏi tự kiểm tra

1. Theo Uncle Bob, hai mặt của "tính chuyên nghiệp" là gì? *(tr. 8)*
2. Nguyên nhân *thật* khiến anh bỏ test nightly routine là gì — kỹ thuật hay điều khác? *(tr. 10)*
3. "First, do no harm" áp vào *chức năng* và *cấu trúc* khác nhau ra sao? *(tr. 11, 14)*
4. Vì sao đòi hỏi "100% coverage, chấm hết" bị 2026 xem là mục tiêu sai? Thay bằng gì?
5. Trong lời khuyên "60 giờ/tuần", đâu là *lõi* còn đúng và đâu là *vỏ* đã lỗi thời?
6. "Doing your daily job is performance, not practice" nghĩa là gì với việc rèn nghề của bạn?

## Tóm tắt một trang

```
BÀI 1 — TÍNH CHUYÊN NGHIỆP: HUY CHƯƠNG HAI MẶT
────────────────────────────────────────────────────────
LÕI     Chuyên nghiệp = danh dự + TRÁCH NHIỆM (tr. 8).
        Bug làm mất 10k$ → nghiệp dư nhún vai; chuyên nghiệp
        "viết séc 10k$". Cảm giác-tiền-của-mình = bản chất nghề.

CA 1  Teradyne 1979: bỏ test routine cho kịp ship → mất trắng
      một đêm dữ liệu ở hàng chục khách. Nguyên nhân thật:
      "saving face" (tr. 10). → First, do no harm (tr. 11).

CA 2  "QA should find nothing" + đòi 100% coverage "chấm hết"
      (tr. 13).
      2026: tinh thần tự-động-kiểm = CI/CD (GIỮ). Con số 100%
      như mệnh lệnh = mục tiêu sai (BỎ) → test có ý nghĩa,
      mutation/property testing.

CẤU TRÚC  Boy Scout rule: để module sạch hơn lúc nhận (tr. 15).
      Sợ đổi code = thiếu test. 2026: đã thành văn hoá review.

CA 3  "Sự nghiệp là của bạn" (GIỮ) + công thức 60h/tuần
      "không thì không chuyên nghiệp" (tr. 16) → 2026 BÁC BỎ:
      chuẩn-hoá-làm-quá-sức, mù trước đặc quyền, ngược nghiên
      cứu về burnout.

KHIÊM NHƯỜNG  Lập trình = kiêu ngạo tột cùng; nên khi ngã,
      hãy cười trước tiên (tr. 22).
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.1 **Professionalism** (`tr. 7–22`): "Be Careful What You Ask For" — huy hiệu danh dự + trách nhiệm, con bug 10.000 đô (tr. 8); "Taking Responsibility" — ca Teradyne 1979 (tr. 8–10); "First, Do No Harm" — không gây hại cho chức năng & cấu trúc, "QA should find nothing", đòi 100% coverage, FitNesse (tr. 11–14); Boy Scout rule (tr. 15–16); "Work Ethic" — sự nghiệp là của bạn, công thức 60 giờ (tr. 16–17); "Know Your Field" / "Continuous Learning" / "Practice" (tr. 17–20); "Humility" (tr. 22). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 ← bạn đang ở đây] · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
