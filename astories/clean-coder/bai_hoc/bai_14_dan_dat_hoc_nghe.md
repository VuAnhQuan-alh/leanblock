# Bài 14 — Dẫn dắt, học nghề & nghề thủ công: bắt bằng nêu gương, không bằng tranh luận

> [!info] Về bài này
> Dựng từ **Chương 14 — Mentoring, Apprenticeship, and Craftsmanship** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 173–185`) — chương **kết** của cả cuốn sách.
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Cần đọc trước: [Bài 12 — Cộng tác](bai_12_cong_tac.md), [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md). Khép lại vòng tròn với [Bài 0 — Nhập môn](bai_00_nhap_mon.md).

## Mục lục

1. [Mở đầu: chiếc Digi-Comp I và ba chữ "And it worked!"](#1-mở-đầu-chiếc-digi-comp-i-và-ba-chữ-and-it-worked)
2. [Nỗi thất vọng với bằng cấp, và sự dẫn dắt không quy ước](#2-nỗi-thất-vọng-với-bằng-cấp-và-sự-dẫn-dắt-không-quy-ước)
3. [Ca 1 — Mô hình học nghề của ngành y, và sự điên rồ của ngành phần mềm](#3-ca-1--mô-hình-học-nghề-của-ngành-y-và-sự-điên-rồ-của-ngành-phần-mềm)
4. [Học nghề phần mềm: bậc thầy, thợ lành nghề, người học việc](#4-học-nghề-phần-mềm-bậc-thầy-thợ-lành-nghề-người-học-việc)
5. [Ca 2 — Nghề thủ công là một "meme" lây lan bằng nêu gương](#5-ca-2--nghề-thủ-công-là-một-meme-lây-lan-bằng-nêu-gương)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào việc của bạn](#7-áp-dụng-vào-việc-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn — và lời kết khoá](#nguồn--và-lời-kết-khoá)

---

## 1. Mở đầu: chiếc Digi-Comp I và ba chữ "And it worked!"

Năm 1964, sinh nhật 12 tuổi, mẹ tặng Uncle Bob một cỗ máy tính nhựa nhỏ tên **Digi-Comp I** — ba cái flip-flop nhựa với sáu cổng and, đủ để dựng một máy trạng thái hữu hạn 3-bit. Bạn "lập trình" nó bằng cách cắm mấy đoạn ống hút vào các chốt. Cuốn sách kèm theo chỉ bảo cắm ống vào *chỗ nào*, chứ chẳng nói *vì sao* — làm cậu bé phát bực. Cậu ngồi nhìn cỗ máy hàng giờ, hiểu được cách nó chạy ở mức thấp nhất, nhưng nghĩ mãi vẫn không sao bắt nó làm được điều mình muốn. Trang cuối cuốn sách mách nước: gửi một đô, họ sẽ gửi lại cuốn *hướng dẫn lập trình*.

Cậu gửi ngay một đô, rồi chờ với cái sốt ruột của một đứa 12 tuổi. Cuốn sách vừa tới là cậu ngấu nghiến: một chuyên luận ngắn gọn về **đại số Boole** — phân tích thừa số, luật kết hợp/phân phối, định lý DeMorgan — chỉ ra cách diễn một bài toán thành chuỗi phương trình Boole rồi rút gọn cho vừa 6 cổng and. Cậu nghĩ ra chương trình đầu đời, tới giờ còn nhớ cả tên: *Mr. Patternson's Computerized Gate*. Viết phương trình, rút gọn, ánh xạ vào ống và chốt:

> [!quote] The Clean Coder — Ch.14 (tr. 175)
> "And it worked! […] I was hooked. My life would never be the same."
>
> *Và nó **chạy**! […] Tôi dính câu luôn. Đời tôi từ đó chẳng bao giờ còn như cũ.*

Uncle Bob nhấn mạnh: cậu **không tự mình nghĩ ra hết** — cậu *được dẫn dắt*. Những con người tử tế và tài giỏi (mà cậu chẳng bao giờ biết tên) đã bỏ công viết một chuyên luận đại số Boole *đủ dễ cho một đứa 12 tuổi*, nối cái lý thuyết toán học với cỗ máy nhựa và **trao cho cậu quyền năng** bắt máy làm theo ý mình. Đó chính là *mentoring*. Và câu chuyện này khép lại vòng tròn với [Bài 0](bai_00_nhap_mon.md): cả một sự nghiệp lớn lên từ đúng cái khoảnh khắc "nó chạy!" ấy.

## 2. Nỗi thất vọng với bằng cấp, và sự dẫn dắt không quy ước

Uncle Bob mở chương bằng một nỗi thất vọng cứ lặp đi lặp lại với sinh viên khoa học máy tính — không phải vì họ kém, mà vì "họ chưa được dạy lập trình *thật sự* là gì". Đỉnh điểm: anh phỏng vấn một nữ sinh đang làm thạc sĩ CS, xin thực tập hè; đến lúc anh rủ ngồi viết code cùng, cô đáp:

> [!quote] The Clean Coder — Ch.14 (tr. 174)
> "I don't really write code."
>
> *Em không thật sự viết code đâu ạ.*

Cô chưa học lấy một môn lập trình nào trong cả chương trình thạc sĩ. Còn những sinh viên *giỏi*, Uncle Bob nhận ra, thì gần như đều có một điểm chung: **họ tự học lập trình từ trước khi vào đại học, và cứ tiếp tục tự học bất chấp cả đại học**.

Rồi anh kể mấy kiểu dẫn dắt *không quy ước* của đời mình: học từ tác giả cuốn sách Digi-Comp; học bằng cách *đứng nhìn* mấy kỹ thuật viên vận hành máy ECP-18 ở trường trung học (nghe họ lẩm bẩm "store in 204", "load 213" mà đoán ra mã lệnh bát phân — dù chẳng ai buồn nói với cậu một câu); người hàng xóm cho hẳn một hộp 30 cái rơ-le điện thoại; và **Jim Carlin**, một lập trình viên BAL đã *cứu anh khỏi cú đuổi việc đầu tiên* bằng cách giúp gỡ một chương trình Cobol vượt tầm anh, dạy anh đọc core dump và định dạng code cho tử tế — "cú đẩy đầu tiên đưa tôi về phía **nghề thủ công**" (tr. 179). Nhưng đầu thập niên 70 có quá ít lập trình viên kỳ cựu; đi đâu anh cũng gần như là người *senior*, chẳng có lấy một hình mẫu nào dạy cho *hành xử chuyên nghiệp* nghĩa là gì. Nhắc lại cái ca bị đuổi năm 1976 ([Bài 12](bai_12_cong_tac.md)), anh chốt: "**phải có một cách tốt hơn chứ**… giá mà hồi đó tôi có một người thầy thật sự. A sensei. A master. A mentor."

## 3. Ca 1 — Mô hình học nghề của ngành y, và sự điên rồ của ngành phần mềm

**Chuyện gì đã xảy ra.** Uncle Bob đem so với ngành y: chẳng bệnh viện nào lại thuê một sinh viên y mới ra trường rồi ném thẳng vào phòng mổ tim ngay ngày đầu. Ngành y có cả một kỷ luật kèm cặp dày đặc: **internship** (1 năm thực hành có giám sát), **residency** (3–5 năm), **fellowship** (1–3 năm), rồi mới được thi lấy chứng chỉ. Còn ngành phần mềm thì sao?

> [!quote] The Clean Coder — Ch.14 (tr. 181)
> "when the stakes are high, we do not send graduates into a room, throw meat in occasionally, and expect good things to come out. So why do we do this in software?"
>
> *khi rủi ro cao, ta **không** nhốt sinh viên mới ra trường vào một căn phòng, thỉnh thoảng ném thịt sống vào, rồi mong điều tốt đẹp chui ra. Vậy cớ sao ta lại làm đúng như thế trong phần mềm?*

Cái chuyện thuê mấy đứa trẻ vừa tốt nghiệp, gom lại thành "đội", rồi giao cho chúng xây những hệ thống trọng yếu nhất — Uncle Bob gọi thẳng ra:

> [!quote] The Clean Coder — Ch.14 (tr. 181)
> "It's insane!"
>
> *Thật điên rồ!*

**Điều rút ra.** Thợ sơn, thợ ống nước, thợ điện — chẳng ai làm kiểu đó. Mà phần mềm thì điều khiển cả động cơ, phanh xe, tài khoản ngân hàng, tin nhắn — "nền văn minh của chúng ta chạy trên phần mềm". Vậy thì một *khoảng thời gian đào tạo và thực hành có giám sát cho hợp lý* là điều hoàn toàn chính đáng.

## 4. Học nghề phần mềm: bậc thầy, thợ lành nghề, người học việc

Uncle Bob phác ra một mô hình học nghề (làm ngược từ trên xuống):

- **Bậc thầy (Masters).** Đã từng dẫn dắt hơn một dự án lớn, thường là 10+ năm, thạo nhiều hệ/ngôn ngữ/nền tảng; biết lãnh đạo nhiều đội, là nhà thiết kế/kiến trúc sư giỏi, code "vòng quanh" mọi người. Từng được mời làm quản lý nhưng *hoặc từ chối, hoặc nhận rồi chạy về, hoặc gộp nó luôn vào vai kỹ thuật* — và giữ cái vai kỹ thuật ấy bằng cách đọc, học, luyện, làm, và **dạy**. ("Cứ nghĩ tới Scotty ấy.")
- **Thợ lành nghề (Journeymen).** Được đào tạo, có năng lực, đầy năng lượng; đang học cách làm việc trong đội và dần thành trưởng nhóm; trung bình chừng 5 năm. Được bậc thầy (hoặc thợ lành nghề kỳ cựu hơn) giám sát; càng dày kinh nghiệm thì càng nhiều tự chủ, rồi dần chuyển sang *peer review*.
- **Người học việc / thực tập (Apprentices).** Sinh viên mới ra trường bắt đầu từ đây, **chưa có chút tự chủ nào**, được thợ lành nghề kèm cặp thật sát. Ban đầu chỉ *phụ việc* thôi, và đây chính là lúc **ghép cặp mạnh mẽ nhất**, lúc học kỷ luật và dựng nền giá trị — thợ lành nghề dạy cho TDD, refactoring, ước lượng, giao bài đọc và bài tập. Học việc nên kéo dài chừng một năm, rồi được tiến cử lên cho bậc thầy xét.

**Điều rút ra.** Thực tế hôm nay *không* khác cái mô hình này bao nhiêu — sinh viên thì được team-lead trẻ giám sát, team-lead lại được project-lead giám sát… Có điều, **sự giám sát ấy lại chẳng mang tính kỹ thuật**:

> [!quote] The Clean Coder — Ch.14 (tr. 183)
> "In most companies there is no technical supervision at all."
>
> *Ở phần lớn công ty, **chẳng hề có** giám sát kỹ thuật nào cả.*

Cái đang thiếu chính là ý niệm rằng **giá trị nghề nghiệp và năng lực kỹ thuật phải được *dạy, nuôi dưỡng, vun trồng*** — và rằng dạy người đi sau là trách nhiệm của người đi trước.

## 5. Ca 2 — Nghề thủ công là một "meme" lây lan bằng nêu gương

**Chuyện gì đã xảy ra.** Cuối cùng thì Uncle Bob mới định nghĩa *craftsmanship* (nghề thủ công). Một *craftsman* (người thợ lành nghề) là người làm nhanh mà không hối hả, đưa ra ước lượng hợp lý và giữ đúng cam kết, biết lúc nào cần nói Không nhưng vẫn cố hết sức để nói Có:

> [!quote] The Clean Coder — Ch.14 (tr. 184)
> "A craftsman is a professional."
>
> *Một người thợ lành nghề **chính là** một người chuyên nghiệp.*

Cả cuốn sách (và cả khoá học này) hội tụ về đúng câu đó. Nghề thủ công là một **meme** — một gói giá trị, kỷ luật, kỹ thuật, thái độ — được trao tay từ người này sang người khác:

> [!quote] The Clean Coder — Ch.14 (tr. 184)
> "Craftsmanship is a contagion, a kind of mental virus. You catch it by observing others and allowing the meme to take hold."
>
> *Nghề thủ công là một thứ **lây lan, một loại virus tinh thần**. Bạn "nhiễm" nó bằng cách **đứng nhìn người khác** rồi để cái meme ấy bén rễ trong mình.*

**Điều rút ra.** Và đây mới là một tự-nhận thức đầy mỉa mai, đáng để suy ngẫm — nhất là với một *khoá học case-study*:

> [!quote] The Clean Coder — Ch.14 (tr. 184)
> "You can't convince people to be craftsmen. […] Arguments are ineffective. Data is inconsequential. Case studies mean nothing."
>
> *Bạn **không thể thuyết phục** người ta thành thợ lành nghề. Lý lẽ thì vô hiệu. Dữ liệu thì vô nghĩa. **Case study cũng chẳng là gì**.*

Vậy thì làm sao lan được cái meme đó? Vì meme chỉ lây khi *quan sát được* — nên bạn phải **làm cho nó quan sát được**: bản thân bạn *trở thành* một craftsman trước đã, để cái nghề thủ công của mình lộ ra, rồi để meme tự lo phần còn lại. Nói cách khác: *nêu gương, đừng tranh luận*.

> [!note] Mở rộng — một nghịch lý dành cho khoá này
> Uncle Bob bảo "case study cũng chẳng là gì" — mà cả cuốn sách của ông (lẫn cái khoá bạn đang đọc) *lại chính là* một chuỗi case study! Mâu thuẫn chăng? Không hẳn. Ý ông là bạn không thể *cãi* để một người thành chuyên nghiệp bằng lý lẽ khô khan. Nhưng câu chuyện đêm Teradyne, đoạn code 3 giờ sáng, người đàn ông trong gương — chúng đâu có "chứng minh" bằng dữ liệu; chúng để bạn **đứng nhìn** một người thợ *sống* qua chính những sai lầm mà rút ra. Cái đó gần với "làm cho meme quan sát được" hơn là với "tranh luận". Một khoá case-study mà *đọc cho đúng cách* thì không phải để bạn *bị thuyết phục*, mà để bạn *nhiễm* — bằng cách đứng sau lưng Uncle Bob mà nhìn.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — tầm nhìn đã thành một phong trào có tên
> Chương này không chỉ là một lời kêu gọi — nó *đã* thành phong trào thật. Năm 2009, bản **Manifesto for Software Craftsmanship** ra đời (Uncle Bob là một trong những người ký), làm nảy ra cả các cộng đồng craftsmanship lẫn những **chương trình học việc** thực thụ (như mấy công ty kiểu 8th Light, Apprenticeship.io, hay nhiều bootcamp có kèm cặp). Còn cái vai "Master giữ vai kỹ thuật, từ chối leo lên làm quản lý" thì chính là **nhánh sự nghiệp IC (individual contributor)** của năm 2026: *Staff / Principal / Distinguished Engineer* — một con đường thăng tiến kỹ thuật chạy song song với quản lý, đúng như điều Uncle Bob hằng mong.
>
> [!warning] Đối chiếu 2026 — cái đúng, cái cần cân
> **Còn đúng:** "trường lớp dạy được lý thuyết, chứ không dạy nổi nghề thủ công", giá trị của mentoring, và chuyện "giám sát thì phải mang tính *kỹ thuật*" — tất cả đều còn vững; mentoring vẫn là một trong những đòn bẩy phát triển mạnh nhất năm 2026. "Nêu gương, đừng tranh luận" thì khớp với hiểu biết về việc thay đổi văn hoá qua *modeling*.
> **Cần cân:** cái khung *master/journeyman/apprentice* mang màu phường hội khá lãng mạn; 2026 dùng *junior/mid/senior/staff/principal* — ánh xạ được, nhưng bớt cái chất "guild" đi. Và bản thân phong trào craftsmanship *cũng bị phản biện*: có người cho rằng nó dễ trượt sang **tinh hoa/gatekeeping**, hoặc quá mải chăm chút *cái đẹp của code* mà nhẹ mất *giá trị giao cho người dùng*. Cứ giữ lấy tinh thần kèm cặp và nêu gương; nhưng phải cảnh giác với cái chủ nghĩa tinh hoa.
>
> [!warning] Đối chiếu 2026 — góc mới: học nghề trong kỷ nguyên AI
> Cái nỗi lo "sinh viên ra trường mà không viết được code" nay mang một hình dạng mới trong năm 2026: với **code có AI hỗ trợ**, người mới rất dễ *sinh* ra một đống code mà chưa *hiểu* nó. Chuyện này khiến mô hình học việc — *ghép cặp, được người đi trước review về kỹ thuật, học cái phán đoán chứ không chỉ cú pháp* — càng quan trọng hơn chứ chẳng kém đi. Bởi cái mà AI *không* dạy được lại chính là thứ chương này bàn tới: giá trị nghề, phản xạ, và khi nào thì phải nói Không.

## 7. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Kể lại "khoảnh khắc nó chạy" của bạn.** Chương trình đầu tiên chạy được của bạn là gì, và ai đã *dẫn dắt* bạn tới đó (một cuốn sách, một con người, một cộng đồng)? Bạn có đang trả lại món nợ đó cho ai chưa?
> 2. **Kiểm "giám sát kỹ thuật".** Trong đội bạn, code của người mới có được người đi trước *review về mặt kỹ thuật* không, hay chỉ có "quản lý" phi kỹ thuật thôi? Nếu thiếu, hãy đề xuất một nhịp mentoring/pair.
> 3. **Làm cho meme quan sát được.** Chọn một kỷ luật bạn tin (TDD, refactoring, biết nói Không đúng lúc) và tuần này *thực hành nó công khai* ngay bên cạnh một người mới hơn — nêu gương, thay vì đứng giảng giải.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **Người thầy không quy ước của bạn.** Ai đã "cho bạn đứng nhìn qua vai" trong nghề của bạn — kể cả những người *chẳng hề cố* dạy bạn điều gì? Bạn đã học được gì chỉ bằng cách *quan sát*?
> 2. **Nêu gương vs tranh luận.** Có một giá trị nghề nào đó mà bạn từng ra sức *cãi* để người khác tin theo, nhưng thất bại. Nếu thay bằng cách *sống nó ra cho họ thấy*, kết quả liệu có khác không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Mentoring không quy ước** | Học bằng cách quan sát người khác (kể cả người phớt lờ bạn) và đọc tài liệu hay, không chỉ qua thầy chính thức (tr. 179). |
| **Apprenticeship (học nghề)** | Mô hình y khoa áp cho phần mềm: internship → residency → fellowship; rủi ro cao thì phải kèm cặp (tr. 180–181). |
| **Master / Journeyman / Apprentice** | Ba bậc: bậc thầy (10+ năm, giữ vai kỹ thuật) / thợ lành nghề (~5 năm) / người học việc (không tự chủ, pair mạnh) (tr. 182). |
| **Giám sát kỹ thuật** | Điều đang thiếu: người đi trước *review và dạy về kỹ thuật*, không chỉ quản lý hành chính (tr. 183). |
| **Craftsmanship là một meme** | Gói giá trị/kỷ luật/thái độ, lây bằng *quan sát và nêu gương*, không bằng lý lẽ (tr. 184). |
| **"Make the meme observable"** | Cách lan nghề thủ công: trở thành craftsman trước, để nó lộ ra (tr. 184). |

## 9. Câu hỏi tự kiểm tra

1. Ai đã "dẫn dắt" cậu bé Uncle Bob tới khoảnh khắc "And it worked!" với Digi-Comp I? *(tr. 175)*
2. Điểm chung của những sinh viên CS *giỏi* mà Uncle Bob gặp là gì? *(tr. 174)*
3. Ngành y kèm cặp bác sĩ mới qua những giai đoạn nào, và câu hỏi "so why do we do this in software?" ngụ ý gì? *(tr. 180–181)*
4. Phân biệt Master, Journeyman, Apprentice. Điều gì đang *thiếu* trong giám sát hôm nay? *(tr. 182–183)*
5. Vì sao "case studies mean nothing" để *thuyết phục*, mà nghề thủ công lại lan bằng *nêu gương*? Nghịch lý này áp thế nào cho chính khoá học của bạn? *(tr. 184)*
6. Tầm nhìn craftsmanship đã thành hiện thực ra sao năm 2026, và bị phản biện điều gì?

## Tóm tắt một trang

```
BÀI 14 — DẪN DẮT, HỌC NGHỀ & NGHỀ THỦ CÔNG (chương kết)
────────────────────────────────────────────────────────
MỞ ĐẦU  1964, Digi-Comp I: gửi 1$ mua sách đại số Boole → "And
        it worked!" (tr. 175). Anh KHÔNG tự nghĩ ra — anh được
        DẪN DẮT (khép vòng với Bài 0).

BẰNG CẤP  "I don't really write code" (tr. 174). Grad giỏi = tự
        học trước & bất chấp đại học. Học không quy ước: quan sát
        (ECP-18), Jim Carlin cứu khỏi bị đuổi.

CA 1 — HỌC NGHỀ  Ngành y: internship→residency→fellowship. Phần
        mềm ném grad xây hệ trọng yếu = "It's insane!" (tr. 181).

BẬC  Master (10+ năm, giữ vai kỹ thuật) / Journeyman (~5 năm) /
        Apprentice (không tự chủ, pair mạnh). Thiếu: "no technical
        supervision at all" (tr. 183).

CA 2 — NGHỀ THỦ CÔNG  "A craftsman is a professional" (tr. 184).
        Craftsmanship = meme, "a mental virus" (tr. 184). "Case
        studies mean nothing" để THUYẾT PHỤC → lan bằng NÊU GƯƠNG,
        "make the meme observable".

2026  Manifesto for Software Craftsmanship (2009) + chương trình
      học việc thật; "Master" = nhánh IC Staff/Principal. Cảnh
      giác gatekeeping. AI khiến mentoring càng cần.
```

## Nguồn — và lời kết khoá

- **Robert C. Martin**, *The Clean Coder*, Ch.14 **Mentoring, Apprenticeship, and Craftsmanship** (`tr. 173–185`): "Degrees of Failure" — "I don't really write code" (tr. 174); "Mentoring" — Digi-Comp I, ECP-18, mentoring không quy ước, Jim Carlin, "Hard Knocks" (tr. 174–179); "Apprenticeship" — mô hình y khoa, "It's insane!", Masters/Journeymen/Apprentices, "The Reality" (tr. 180–183); "Craftsmanship" — meme, "Convincing People" (tr. 184); Conclusion (tr. 185). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Bối cảnh 2026 (ngoài sách): Manifesto for Software Craftsmanship (2009), chương trình học việc (8th Light…), nhánh sự nghiệp IC (Staff/Principal Engineer), phản biện gatekeeping, mentoring trong kỷ nguyên AI.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

> [!success] Hết khoá — 15 bài, một vòng tròn khép kín
> Bạn khởi hành ở [Bài 0](bai_00_nhap_mon.md) với "danh mục lỗi của chính tôi", rồi kết lại ở đây bằng khoảnh khắc "And it worked!" — vẫn cùng một con người, học nghề qua vấp ngã và qua đủ loại người thầy, cả quy ước lẫn không quy ước. Đúng tinh thần chương cuối: đừng để khoá này *thuyết phục* bạn; hãy để nó cho bạn **đứng sau lưng Uncle Bob mà quan sát** một người thợ sống trọn bốn thập niên sai lầm rồi rút ra bài học. Rồi tự mình *trở thành* người thợ ấy — và làm cho nghề thủ công của mình *quan sát được* trước mắt người đi sau.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 ← bạn đang ở đây]

Xem thêm [README khoá học](../README.md).
