# Bài 7 — Kiểm thử chấp nhận: biến yêu cầu mơ hồ thành đặc tả chạy được

> [!info] Về bài này
> Dựng từ **Chương 7 — Acceptance Testing** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 95–111`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới. Hội thoại Sam–Paula–Tom kể lại bằng lời.
> Cần đọc trước: [Bài 4 — Viết code](bai_04_viet_code.md) (định nghĩa "Done"), [Bài 5 — TDD](bai_05_tdd.md).

## Mục lục

1. [Mở đầu: nhà điêu khắc và cái đục (ED-402, 1979)](#1-mở-đầu-nhà-điêu-khắc-và-cái-đục-ed-402-1979)
2. [Bẫy "chính xác quá sớm" và nguyên lý bất định của yêu cầu](#2-bẫy-chính-xác-quá-sớm-và-nguyên-lý-bất-định-của-yêu-cầu)
3. [Ca 1 — Thư mục "backup": cùng một từ, hai thế giới](#3-ca-1--thư-mục-backup-cùng-một-từ-hai-thế-giới)
4. [Acceptance test: định nghĩa "Done" mà mọi bên cùng ký](#4-acceptance-test-định-nghĩa-done-mà-mọi-bên-cùng-ký)
5. [Ca 2 — Bản kế hoạch test một triệu đô](#5-ca-2--bản-kế-hoạch-test-một-triệu-đô)
6. [Ai viết, khi nào, và nghệ thuật đàm phán test](#6-ai-viết-khi-nào-và-nghệ-thuật-đàm-phán-test)
7. [Test là tài liệu trước, là test sau; GUI; và "dừng máy in"](#7-test-là-tài-liệu-trước-là-test-sau-gui-và-dừng-máy-in)
8. [Đối chiếu 2026](#8-đối-chiếu-2026)
9. [Áp dụng vào việc của bạn](#9-áp-dụng-vào-việc-của-bạn)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
12. [Tóm tắt một trang](#tóm-tắt-một-trang)
13. [Nguồn](#nguồn)

---

## 1. Mở đầu: nhà điêu khắc và cái đục (ED-402, 1979)

Năm 1979 ở Teradyne, Tom — quản lý lắp đặt và dịch vụ hiện trường — nhờ Uncle Bob **dạy** cho cách dùng trình soạn thảo ED-402 để tự viết lấy một hệ ghi phiếu sự cố đơn giản. Tom không phải dân lập trình, nhưng ứng dụng trông có vẻ đơn giản, nên cả hai đều tưởng dạy vài buổi là xong. Ngờ đâu, lúc Bob chỉ cách gõ ký hiệu lệnh soạn thảo vào một tệp script (chẳng hạn `^B` để đưa con trỏ về đầu dòng), anh nhìn vào mắt Tom thì thấy... trống rỗng. Tom không ngốc — anh chỉ vừa nhận ra cái chuyện "dùng một trình soạn thảo để điều khiển một trình soạn thảo" nó rối rắm hơn nhiều so với tưởng tượng, và anh chẳng buồn bỏ công ra học.

Thế là, từng chút một, Bob thấy mình **tự tay viết luôn cái ứng dụng** trong khi Tom ngồi nhìn. Cả một ngày trời trôi qua như vậy: Tom tả một tính năng, Bob cài trong năm phút, hai người thử, rồi Tom lại đổi ý — "chưa ra cái *cảm giác* tôi muốn, thử kiểu khác xem". Hết giờ này sang giờ khác.

> [!quote] The Clean Coder — Ch.7 (tr. 96)
> "It became very clear to me that he was the sculptor, and I was the tool he was wielding."
>
> *Tôi thấy rõ mồn một: anh ta mới là **nhà điêu khắc**, còn tôi chỉ là **cái đục** trong tay anh ta.*

Cuối ngày, Tom có đúng cái ứng dụng mình muốn — nhưng vẫn mù tịt chuyện tự làm cái kế tiếp. Còn Bob thì học được một bài học nặng ký về cách khách hàng *thật sự* mò ra điều họ cần:

> [!quote] The Clean Coder — Ch.7 (tr. 96)
> "their vision of the features does not often survive actual contact with the computer."
>
> *cái hình dung của họ về tính năng thường **không sống sót** nổi qua lần chạm mặt thật với máy tính.*

Cả chương này là câu trả lời cho đúng vấn đề đó: làm sao truyền đạt yêu cầu cho khỏi hỏng.

## 2. Bẫy "chính xác quá sớm" và nguyên lý bất định của yêu cầu

Cả hai phía đều dễ sa vào **premature precision** (chính xác quá sớm): bên nghiệp vụ muốn biết *chính xác* mình sắp nhận được gì trước khi duyệt dự án; còn lập trình viên thì muốn biết *chính xác* phải giao gì trước khi ước lượng. Cả hai đòi một độ chính xác không thể có được — bởi mọi thứ trên giấy khác hẳn khi chạy trong hệ thật:

> [!quote] The Clean Coder — Ch.7 (tr. 97)
> "the more precise you make your requirements, the less relevant they become as the system is implemented."
>
> *bạn viết yêu cầu càng tỉ mỉ bao nhiêu, thì tới lúc cài đặt hệ, chúng lại càng **ít ăn nhập** bấy nhiêu.*

Đây là một kiểu **hiệu ứng người quan sát**: cứ mỗi lần bạn demo một tính năng là bên nghiệp vụ lại có thêm thông tin, mà thông tin mới thì lại đổi cái cách họ nhìn cả hệ thống. Lời giải là **hoãn sự chính xác** tới sát lúc phát triển (*late precision*). Nhưng hoãn quá tay thì lại đẻ ra **mơ hồ muộn** (late ambiguity), mà Tom DeMarco tóm gọn bằng một câu Uncle Bob rất tâm đắc:

> [!quote] The Clean Coder — Ch.7 (tr. 98)
> "An ambiguity in a requirements document represents an argument amongst the stakeholders."
>
> *Một chỗ mơ hồ trong tài liệu yêu cầu thực chất là **một cuộc cãi vã chưa ngã ngũ giữa các bên**.*

## 3. Ca 1 — Thư mục "backup": cùng một từ, hai thế giới

**Chuyện gì đã xảy ra.** Uncle Bob dựng một hội thoại kinh điển. Sam (bên nghiệp vụ) bảo Paula (lập trình viên): "mấy tệp log cần được sao lưu." Qua vài câu hỏi, họ chốt: cứ nửa đêm mỗi ngày là ghi log vào một thư mục tên `backup`, tệp đặt tên `log.backup`. Nghe rõ ràng đâu ra đấy. Nhưng ở một phòng khác, Sam lại nói với khách hàng Carl: "log sẽ được lưu lại" — và Carl nhấn mạnh: "**tuyệt đối không được để mất log nào**, chúng tôi cần lục lại log của **nhiều tháng, nhiều năm** sau mỗi lần có sự cố."

Chỗ mơ hồ giờ mới lòi ra: khách muốn giữ **mọi** log **mãi mãi**; còn Paula thì tưởng chỉ cần lưu **log của đêm hôm qua**. Đến lúc khách đi tìm log mấy tháng trước, họ chỉ thấy đúng log một đêm.

**Điều rút ra.** Cả Paula lẫn Sam đều "làm rớt quả bóng". Dọn sạch *mọi* chỗ mơ hồ khỏi yêu cầu là trách nhiệm của cả lập trình viên lẫn các bên — và Uncle Bob bảo ông chỉ biết có **một cách** để làm việc đó: acceptance test.

## 4. Acceptance test: định nghĩa "Done" mà mọi bên cùng ký

Uncle Bob định nghĩa **acceptance test** hẹp mà rõ: đó là *test do bên nghiệp vụ và lập trình viên cùng nhau viết ra, để xác định khi nào thì một yêu cầu coi như **xong***. Mà "xong" lại là một trong những từ mơ hồ nhất nghề:

> [!quote] The Clean Coder — Ch.7 (tr. 100)
> "Done means done. Done means all code written, all tests pass, QA and the stakeholders have accepted. Done."
>
> *Xong là xong. Xong nghĩa là **code đã viết hết, test pass hết, QA và các bên đã chấp nhận**. Xong.*

Làm sao đạt được mức "xong" đó mà vẫn tiến nhanh qua từng vòng lặp? Dựng một bộ **test tự động** mà hễ pass là thoả hết mọi tiêu chí trên. Uncle Bob diễn lại đúng cái hội thoại backup — nhưng lần này có thêm **Tom (tester)**: Tom truy "backup là cái tên chung chung quá, thư mục này *rốt cuộc* chứa gì?", rồi lần ra đó là các log cũ đã ngừng hoạt động → đổi tên thành `old_inactive_logs`, rồi viết test theo khuôn **given / when / then** (viết bằng FitNesse): *cho lệnh khởi động, cho thư mục chưa tồn tại → khi lệnh chạy → thì thư mục phải tồn tại và phải rỗng*. Đến lúc Sam kêu "viết ngần ấy test có cần không?", Paula liền phản đòn: "Sam, trong hai phát biểu này, cái nào *không* đủ quan trọng để mà đặc tả?" Còn Tom chốt: viết test này *chẳng* tốn hơn viết một bản kế hoạch test thủ công — mà đem chạy tay lại nhiều lần thì còn tốn hơn gấp bội.

## 5. Ca 2 — Bản kế hoạch test một triệu đô

**Chuyện gì đã xảy ra.** Acceptance test thì **phải luôn tự động**, vì một lẽ đơn giản: *chi phí*. Uncle Bob kể về một tấm ảnh (Hình 7-1): đôi bàn tay của một QA manager ở một công ty Internet lớn, đang cầm cái bản **mục lục** cho kế hoạch test thủ công của mình. Ông ta có cả một đạo quân tester thuê ngoài, cứ **6 tuần một lần** lại chạy hết cái kế hoạch đó, mỗi lần ngốn hơn **một triệu đô**. Ông vừa họp về, sếp bảo cắt ngân sách đi 50%. Câu ông hỏi Uncle Bob là:

> [!quote] The Clean Coder — Ch.7 (tr. 104)
> "Which half of these tests should I not run?"
>
> *Trong cả đống test này, tôi **nên thôi không chạy nửa nào**?*

**Điều rút ra.** Gọi đây là thảm hoạ vẫn còn là nói nhẹ: chi phí chạy test thủ công lớn tới mức họ đành hy sinh nó, và **chấp nhận là không biết một nửa sản phẩm có chạy hay không**. Chi phí *tự động hoá* acceptance test thì nhỏ tới mức ngồi viết script cho người-chạy-tay là chuyện vô nghĩa về kinh tế. Đây cũng là chỗ mà câu "viết test = làm thêm việc" hoá ra hiểu sai: viết acceptance test *chính là* việc **đặc tả hệ thống** — cách duy nhất để lập trình viên biết "xong" nghĩa là gì, và để các bên chắc rằng thứ mình bỏ tiền ra đúng là thứ mình cần.

## 6. Ai viết, khi nào, và nghệ thuật đàm phán test

- **Ai viết.** Lý tưởng là bên nghiệp vụ và QA viết, lập trình viên rà lại cho nhất quán. Thực tế thì thường uỷ cho BA/QA/lập trình viên. Nếu buộc lập trình viên phải viết, thì **người viết test không nên là người cài chính tính năng đó**. BA thường viết đường "hạnh phúc" (happy path — nơi có giá trị nghiệp vụ); QA lo đường "bất hạnh" (ca biên, ngoại lệ, ca góc), bởi việc của QA là ngồi nghĩ xem cái gì có thể hỏng.
- **Khi nào.** Theo tinh thần "late precision": viết sát lúc cài, chừng vài ngày trước. Vài test đầu tiên có sẵn ngay ngày đầu iteration, tới nửa chặng thì phải xong hết; nếu cứ trễ cái mốc đó hoài thì phải bổ sung thêm BA/QA.
- **Vai trò lập trình viên.** Cài đặt bắt đầu khi acceptance test đã sẵn: chạy test lên thấy nó đỏ, nối test vào hệ, rồi làm cho nó pass.
- **Đàm phán test, chứ đừng thụ động-gây hấn.** Người viết test cũng là người, cũng sai. Khi cái test viết ra vô lý, rối rắm thừa thãi, hay đơn giản là sai, thì việc của bạn là **đàm phán** để có một cái test tốt hơn:

> [!quote] The Clean Coder — Ch.7 (tr. 107)
> "What you should never do is take the passive-aggressive option and say to yourself, 'Well, that's what the test says, so that's what I'm going to do.'"
>
> *Cái bạn **tuyệt đối đừng** làm là chọn lối thụ động-gây hấn rồi tự nhủ: "Ừ thì test nó ghi vậy, thôi tôi cứ làm y vậy."*

Uncle Bob minh hoạ bằng ca test "thao tác post phải xong trong 2 giây": Paula chỉ ra rằng chỉ có thể bảo đảm điều đó *theo nghĩa thống kê* (99,5% số lần), rồi cùng Tom mài lại câu test thành một dạng thống kê đọc được — thay vì âm thầm đi cài một thứ mà mình biết thừa là bất khả.

## 7. Test là tài liệu trước, là test sau; GUI; và "dừng máy in"

- **Acceptance test ≠ unit test.** Unit test do lập trình viên viết *cho lập trình viên* (tài liệu thiết kế cấp thấp); còn acceptance test do bên nghiệp vụ viết *cho bên nghiệp vụ* (tài liệu yêu cầu). Hai cái không thừa nhau, bởi chúng đi qua những đường thực thi khác nhau (unit thì đào thẳng vào ruột; acceptance thì gọi ở mức API/UI). Mà lý do sâu xa hơn là:

> [!quote] The Clean Coder — Ch.7 (tr. 108)
> "Unit tests and acceptance tests are documents first, and tests second."
>
> *Unit test và acceptance test trước hết là **tài liệu, sau mới là test**. Chuyện chúng tự động kiểm chứng thì cực kỳ hữu ích, nhưng **đặc tả** mới là mục đích thật sự.*

- **GUI.** Rất khó đặc tả trước, vì thẩm mỹ thì chủ quan mà lại hay đổi. Mẹo là: **coi GUI như một API** (theo Single Responsibility Principle), test *xuyên qua cái API ngay dưới GUI* thay vì bấm nút theo vị trí; chọn nút theo *ID* (`ok_button`) chứ đừng theo kiểu "nút ở cột 3 hàng 4". Và giữ số test-qua-GUI ở mức tối thiểu, vì GUI dễ vỡ.
- **CI và "Stop the Presses".** Cho chạy mọi unit test + acceptance test nhiều lần mỗi ngày trong hệ CI, để hệ quản lý mã nguồn tự kích hoạt. Build đỏ là tình trạng khẩn cấp:

> [!quote] The Clean Coder — Ch.7 (tr. 110)
> "A broken build in the CI system should be viewed as an emergency, a 'stop the presses' event."
>
> *Một bản build hỏng trong hệ CI phải được coi là **tình trạng khẩn cấp**, một sự kiện kiểu "**dừng máy in ngay lập tức**".*

Ông kể một đội "bận quá" nên chẳng sửa test đỏ, bèn gỡ luôn chúng ra khỏi build, rồi quên gắn lại — mãi tới khi khách hàng nổi đoá gọi tới báo lỗi mới hay.

## 8. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — chương già đi rất đẹp
> Đây là một trong những chương **đúng nhất theo năm tháng**. "Đặc tả bằng acceptance test tự động, viết theo given/when/then, mà cả bên nghiệp vụ cũng đọc được" thì chính là **BDD** (Behavior-Driven Development) và cú pháp **Gherkin** rất phổ biến năm 2026. "Test là tài liệu sống" (documents first, tests second) đã thành khẩu quyết chung. "Definition of Done" là thuật ngữ chuẩn trong Scrum. "Stop the Presses" thì đúng là văn hoá *stop-the-line* của CI năm 2026 — build đỏ chặn mọi merge. Còn ca "kế hoạch test 1 triệu đô" thì trong kỷ nguyên ship liên tục lại càng đắt giá hơn.
> **Công cụ đã đổi:** FitNesse, cuke4duke, robot framework là đồ của 2011; 2026 dùng Cucumber (vẫn sống), Playwright, Cypress, Selenium (còn dùng nhưng đã có lớp kế thừa). Lời khuyên "coi GUI như API, test dưới GUI" thì vẫn đúng về nguyên tắc, nhưng mấy công cụ E2E hiện đại (Playwright) đã làm test-qua-GUI **bớt giòn** hơn hồi 2011 — nên tỉ lệ test-qua-GUI có thể nhỉnh hơn mức ông khuyến nghị.
> **Một sắc thái cần cân:** đội nào lạm dụng acceptance/E2E test thì dễ rơi vào phản-mẫu "**ly kem ốc quế**" (nhiều E2E chậm, ít unit nhanh). 2026 cân lại bằng *kim tự tháp test* / *testing trophy*: nhiều unit test nhanh làm nền, acceptance test chỉ nằm ở lớp mỏng hơn. Còn cái câu "acceptance test là tài liệu yêu cầu **hoàn hảo**" thì hơi quá lời: test đặc tả được *hành vi*, nhưng không ghi lại được *lý do* (why) đằng sau — nên vẫn cần thêm tài liệu để chống lưng cho các quyết định.

## 9. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Săn một chỗ "mơ hồ muộn".** Trong backlog hiện tại, tìm một yêu cầu mà bạn và người viết ra nó *có thể* đang hiểu khác nhau (kiểu như "backup"). Viết một acceptance test given/when/then buộc cả hai phải chốt cho rõ nghĩa.
> 2. **Đổi "xong" thành test.** Chọn một task sắp làm; trước khi code, viết ra bộ acceptance test định nghĩa thế nào là "xong". Bạn có moi ra được câu hỏi nào chưa ai trả lời không?
> 3. **Tập đàm phán test.** Lần tới gặp một cái test vô lý, đừng cứ thế cài theo kiểu thụ động-gây hấn — hãy mở một cuộc trao đổi với người viết, y như Paula với Tom.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **"Định nghĩa Done" cho một lần bàn giao.** Trong nghề bạn, lần bàn giao gần nhất có bị hiểu "xong" theo hai nghĩa khác nhau không? Viết ra một tiêu chí nghiệm thu *kiểm chứng được* mà cả bạn lẫn bên nhận cùng ký vào.
> 2. **Cái giá của "test thủ công".** Có quy trình lặp đi lặp lại nào trong công việc bạn đang ngốn tiền y như "kế hoạch test 1 triệu đô" không? Phần nào có thể tự động hoá hay chuẩn hoá để khỏi phải đến nước "bỏ nửa nào"?

## 10. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Acceptance test** | Test do nghiệp vụ + lập trình viên cùng viết để định nghĩa khi nào một yêu cầu là *xong* (tr. 100). |
| **Premature precision** | Đòi chính xác quá sớm; vô ích vì yêu cầu đổi khi hệ chạy thật (tr. 97). |
| **Uncertainty principle (yêu cầu)** | Mỗi lần demo lại đổi cách nghiệp vụ nhìn hệ thống → chính xác sớm mất giá trị (tr. 97). |
| **Late precision / late ambiguity** | Hoãn chính xác tới sát lúc cài (tốt) nhưng coi chừng mơ hồ muộn (tr. 98). |
| **given / when / then** | Khuôn viết acceptance test đọc được bởi cả nghiệp vụ; nền của BDD/Gherkin 2026 (tr. 102). |
| **Documents first, tests second** | Test tồn tại trước hết như *đặc tả*; việc tự kiểm chứng là phần thưởng thêm (tr. 108). |
| **Stop the Presses** | Build CI đỏ = khẩn cấp, cả đội dừng lại sửa (tr. 110). |

## 11. Câu hỏi tự kiểm tra

1. Bài học Uncle Bob rút ra từ ca ED-402/Tom là gì? *(tr. 96)*
2. "Nguyên lý bất định của yêu cầu" nói gì về việc đặc tả quá chi tiết quá sớm? *(tr. 97)*
3. Trong ca "backup", chỗ mơ hồ nằm ở đâu, và acceptance test given/when/then gỡ nó thế nào? *(tr. 99–102)*
4. Câu hỏi "nên bỏ chạy nửa nào?" phơi bày điều gì về test thủ công? *(tr. 104)*
5. Vì sao acceptance test và unit test *không* thừa nhau dù đôi khi test cùng thứ? *(tr. 108)*
6. Chương này già đi thế nào so với 2026 — nêu một phần còn nguyên giá trị và một phản-mẫu cần tránh.

## Tóm tắt một trang

```
BÀI 7 — KIỂM THỬ CHẤP NHẬN: YÊU CẦU MƠ HỒ → ĐẶC TẢ CHẠY ĐƯỢC
────────────────────────────────────────────────────────
MỞ ĐẦU  1979, ED-402: Tom tả, Bob cài, Tom đổi ý cả ngày —
        "he was the sculptor, and I was the tool" (tr. 96).
        Hình dung của khách KHÔNG sống sót khi gặp máy tính.

BẪY  Premature precision: chi tiết càng sớm càng vô nghĩa (tr.97).
     Mơ hồ = "một cuộc tranh cãi chưa ngã ngũ" — DeMarco (tr. 98).

CA 1  "backup": Paula tưởng lưu 1 đêm, khách muốn giữ MÃI MÃI.
      → viết lại thành old_inactive_logs, given/when/then (tr.102).

DONE  "Done means done… all tests pass, QA & stakeholders
      accepted" (tr. 100). Acceptance test tự động = định nghĩa Done.

CA 2  Kế hoạch test thủ công: 1 triệu đô mỗi 6 tuần → "nên bỏ
      chạy nửa nào?" (tr. 104). ⇒ PHẢI tự động.

AI/KHI  BA viết happy path, QA viết unhappy path. Viết sát lúc cài.
        Đàm phán test, KHÔNG thụ động-gây hấn (tr. 107).

TÀI LIỆU  "documents first, tests second" (tr. 108). GUI: test
        dưới-GUI như API. CI đỏ = "stop the presses" (tr. 110).

2026  BDD/Gherkin, Definition of Done, stop-the-line = GIỮ (đúng
      hơn theo thời gian). Tránh phản-mẫu "ly kem ốc quế"; cân
      bằng kim tự tháp test. Công cụ: Cucumber/Playwright/Cypress.
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.7 **Acceptance Testing** (`tr. 95–111`): "Communicating Requirements" — ca ED-402/Tom (tr. 95–96); "Premature Precision", uncertainty principle, estimation anxiety, late ambiguity, DeMarco (tr. 97–99); ca "backup" (tr. 99); "Acceptance Tests" & định nghĩa Done, ca backup viết lại given/when/then (tr. 100–102); "Automation" — ca kế hoạch test 1 triệu đô (tr. 103–104); "Extra Work", "Who Writes… and When" (tr. 105); "The Developer's Role", "Test Negotiation and Passive Aggression" (tr. 106–107); "Acceptance Tests and Unit Tests" (tr. 108); "GUIs" (tr. 109–110); "Continuous Integration" / "Stop the Presses" (tr. 110); Conclusion (tr. 111). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Bối cảnh 2026 (ngoài sách): BDD/Gherkin, Cucumber/Playwright/Cypress, kim tự tháp test / testing trophy, phản-mẫu "ice-cream cone".
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 ← bạn đang ở đây] · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
