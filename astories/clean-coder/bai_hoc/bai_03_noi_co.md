# Bài 3 — Nói Có: ngôn ngữ của sự cam kết

> [!info] Về bài này
> Dựng từ **Chương 3 — Saying Yes** của *The Clean Coder* (Robert C. Martin, có phần khách mời của **Roy Osherove**, `tai_lieu/`, `tr. 45–56`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới. Hội thoại Peter–Marge kể lại bằng lời.
> Cần đọc trước: [Bài 2 — Nói Không](bai_02_noi_khong.md) — "There is no trying" quay lại ở đây từ mặt kia.

## Mục lục

1. [Mở đầu: chờ trên cây sồi và câu "Tôi cam kết… chắc vậy"](#1-mở-đầu-chờ-trên-cây-sồi-và-câu-tôi-cam-kết-chắc-vậy)
2. [Say. Mean. Do. — ba tầng của một cam kết](#2-say-mean-do--ba-tầng-của-một-cam-kết)
3. [Ca 1 — Nhận diện sự thiếu cam kết qua ngôn từ](#3-ca-1--nhận-diện-sự-thiếu-cam-kết-qua-ngôn-từ)
4. ["Tôi sẽ… trước…" — câu thần chú của cam kết thật](#4-tôi-sẽ-trước--câu-thần-chú-của-cam-kết-thật)
5. [Ca 2 — Peter và Marge: mặt kia của chữ "cố"](#5-ca-2--peter-và-marge-mặt-kia-của-chữ-cố)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào việc của bạn](#7-áp-dụng-vào-việc-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: chờ trên cây sồi và câu "Tôi cam kết… chắc vậy"

Đầu thập niên 1980, ở Teradyne, Uncle Bob (cùng Ken Finder và Jerry Fitzpatrick) phát minh ra **"The Electronic Receptionist" (ER)** — cỗ máy trả lời điện thoại, dò tìm người theo nhiều số, tìm không ra thì ghi lời nhắn. Nói cách khác, đó chính là **voice mail**, và họ được cấp bằng sáng chế hẳn hoi. Có điều Teradyne loay hoay không biết bán ER kiểu gì; dự án cạn ngân sách, bị biến thành CDS (hệ điều phối thợ sửa điện thoại), rồi công ty **âm thầm buông luôn cái bằng sáng chế** (người giữ bằng bây giờ nộp đơn *sau* họ những ba tháng).

Vẫn tin ER có thể hái ra tiền, Uncle Bob **trèo hẳn lên cây sồi trước cửa toà nhà, ngồi rình chiếc Jaguar của CEO** rồi xin gặp vài phút. Anh cứ đinh ninh CEO sẽ bảo "Cậu nói đúng, tôi cho khởi động lại dự án ngay". Nào ngờ Russ (CEO) đẩy ngược gánh nặng về phía anh: *"OK Bob, cậu dựng cho tôi một cái kế hoạch. Chỉ tôi thấy tiền về từ đâu. Tôi mà tin thì tôi cho chạy lại ER."* Bob vốn là dân phần mềm, chẳng muốn ôm chuyện lời lỗ, nhưng cũng không muốn để lộ sự lưỡng lự — thế là anh cảm ơn rồi bước ra với một câu:

> [!quote] The Clean Coder — Ch.3 (tr. 47)
> "Thanks Russ. I'm committed . . . I guess."
>
> *Cảm ơn Russ. Tôi cam kết… chắc vậy.*

Chính cái đuôi "chắc vậy" thảm hại ấy mở ra cả chương. Uncle Bob mời hẳn **Roy Osherove** viết một phần để mổ xem nó thảm hại ở đâu.

## 2. Say. Mean. Do. — ba tầng của một cam kết

Roy Osherove tách một cam kết thật ra làm ba phần:

> [!quote] The Clean Coder — Ch.3 (tr. 47)
> "Say. Mean. Do. There are three parts to making a commitment. 1. You say you'll do it. 2. You mean it. 3. You actually do it."
>
> *Nói. Thật lòng. Làm. Một cam kết gồm ba phần: 1. Bạn **nói** sẽ làm. 2. Bạn **thật lòng** muốn làm. 3. Bạn **thực sự bắt tay vào làm**.*

Rất ít người đi trọn được cả ba tầng. Có kẻ nói mà chẳng thật lòng ("tôi cần giảm cân" — nghe là biết sẽ chẳng làm gì); có người thật lòng nhưng rốt cuộc chẳng bao giờ làm xong. Đáng nói là trực giác hay đánh lừa ta: ta *muốn tin* một lập trình viên bị dồn vào chân tường khi cậu ta bảo "việc hai tuần em làm gọn trong một tuần", dù lẽ ra không nên tin. Cách của Roy không phải là đặt cược vào ruột gan, mà là **soi cho kỹ ngôn ngữ**: đổi cách nói thì tự khắc lo được hai tầng đầu.

## 3. Ca 1 — Nhận diện sự thiếu cam kết qua ngôn từ

**Chuyện gì đã xảy ra.** Roy chỉ ra rằng sự thiếu cam kết bao giờ cũng để lại dấu vết trong lời nói. Không thấy "mấy chữ thần chú" đâu thì nhiều khả năng người nói hoặc không thật lòng, hoặc chẳng tin việc làm nổi. Có ba nhóm từ báo động:

- **Need / should** (cần / nên): "Chúng ta *cần* làm xong cái này." "*Ai đó nên* lo chuyện đó." → đùn cho một tập thể mơ hồ, chẳng ai đứng ra chịu.
- **Hope / wish** (hy vọng / ước): "Tôi *hy vọng* xong trước mai." "*Giá mà* tôi có thời gian." → đẩy kết quả ra ngoài tầm tay mình.
- **Let's** (mà không kèm "tôi…"): "*Hôm nào* gặp nhau nhé." "*Làm cho xong* cái này đi." → lời rủ rê chẳng có ai là chủ thể hành động.

**Điều rút ra.** Cái chung của mấy câu ấy là chúng đều **coi như mọi thứ nằm ngoài tay "tôi"**, cư xử như thể mình là nạn nhân của hoàn cảnh chứ không phải người cầm trịch. Roy lật lại bằng một sự thật giải phóng:

> [!quote] The Clean Coder — Ch.3 (tr. 49)
> "you, personally, ALWAYS have something that's under your control, so there is always something you can fully commit to doing."
>
> *bản thân bạn thì **LÚC NÀO** cũng nắm trong tay một cái gì đó, nên **luôn luôn** có một việc bạn có thể cam kết làm cho trọn.*

## 4. "Tôi sẽ… trước…" — câu thần chú của cam kết thật

Cam kết thật có một hình hài ngôn ngữ rất cụ thể:

> [!quote] The Clean Coder — Ch.3 (tr. 49)
> "The secret ingredient to recognizing real commitment is to look for sentences that sound like this: I will . . . by . . . (example: I will finish this by Tuesday.)"
>
> *Bí quyết để nhận ra một cam kết thật là tìm những câu nghe như: **Tôi sẽ… trước…** (ví dụ: Tôi sẽ làm xong việc này trước thứ Ba.)*

Vì sao câu ấy mạnh? Vì nó nói về hành động **của chính bạn** (không phải của ai khác), có **mốc kết thúc rõ ràng**, và chỉ cho ra một kết quả nhị phân:

> [!quote] The Clean Coder — Ch.3 (tr. 49)
> "only a binary result is possible—you either get it done, or you don't."
>
> *chỉ có đúng hai khả năng — hoặc bạn làm xong, hoặc không.*

Nghe mà phát sợ, bởi bạn **nhận trọn trách nhiệm trước ít nhất một người khác** — chứ không còn là mình đứng lẩm bẩm trước gương nữa. Roy lường trước ba lời chối và cách gỡ từng cái:

- *"Không được đâu, việc này còn phụ thuộc người X."* → Đúng là bạn chỉ cam kết được cái mình toàn quyền. Nhưng bạn vẫn có thể **cam kết những hành động cụ thể** kéo mình lại gần đích: ngồi một tiếng với người bên đội hạ tầng cho hiểu chỗ phụ thuộc, dựng một interface tách phần phụ thuộc ra, tự tạo một bản build chạy test tích hợp. *"If the end goal depends on someone else, you should commit to specific actions that bring you closer to the end goal"* (tr. 50).
- *"Không được đâu, tôi còn chưa chắc việc này làm nổi."* → Thì **chính cái việc "đi tìm hiểu xem có làm được không" đã có thể là một hành động để cam kết**. Thay vì hứa sửa cả 25 con bug, hãy cam kết: tái hiện đủ 25 bug, ngồi với QA xem repro từng cái, dồn hết thời gian tuần này vào sửa.
- *"Không được đâu, có khi tôi lại không kịp."* → Chuyện đời mà. Nhưng khi đó thì phải **đổi lại kỳ vọng càng sớm càng tốt**:

> [!quote] The Clean Coder — Ch.3 (tr. 51)
> "If you can't make your commitment, the most important thing is to raise a red flag as soon as possible to whoever you committed to."
>
> *Khi thấy không giữ nổi cam kết, điều quan trọng nhất là **giương cờ đỏ thật sớm** cho người mà bạn đã hứa.*

Giương cờ sớm cho các bên liên quan thì đội còn kịp dừng lại, tính lại, đổi ưu tiên — cam kết vẫn có thể về đích, hoặc được thay bằng một cam kết khác. Còn giấu nhẹm vấn đề đi thì chẳng khác nào **tước mất cơ hội để người khác giúp bạn**.

## 5. Ca 2 — Peter và Marge: mặt kia của chữ "cố"

**Chuyện gì đã xảy ra.** Ở [Bài 2](bai_02_noi_khong.md), chữ "try" mang nghĩa "cố thêm chút sức". Ở đây Uncle Bob soi cái nghĩa còn lại: "*ừ thì thử, được hay không tính sau*". Peter tự nhẩm phần sửa rating engine mất 5–6 ngày, còn tài liệu thì thêm vài giờ. Sếp Marge hỏi có xong trước thứ Sáu không. Peter đáp lấp lửng: "Em nghĩ là được" / "Em sẽ cố làm luôn phần tài liệu". Marge hỏi câu cần đáp có/không dứt khoát, mà Peter cứ trả lời nhoè nhoẹt.

Nói cho thật thì Peter nên bảo: "Có thể kịp, mà cũng có thể sang thứ Hai" — mô tả đúng cái mức bất định của mình. Đến khi Marge cần một câu **dứt khoát** có hay không cho thứ Sáu, Peter phải nói Không và cam kết đúng cái mốc mình chắc: "Sớm nhất mà em dám chắc là thứ Ba."

Marge ép tiếp, vì Willy — người viết tài liệu — cần bản thảo ngay sáng thứ Hai. Đôi bên đàm phán qua lại, Peter tính đến chuyện làm thêm cuối tuần. Nhưng có một lằn ranh Peter suýt vượt qua: anh nghĩ mình sẽ nhanh hơn nếu **bỏ viết test, bỏ refactor, bỏ luôn chạy regression**. Đúng chỗ này thì Uncle Bob chặn lại:

> [!quote] The Clean Coder — Ch.3 (tr. 55)
> "This is where the professional draws the line. […] breaking disciplines only slows us down."
>
> *Đây chính là chỗ người chuyên nghiệp **vạch ra một lằn ranh**. […] phá bỏ kỷ luật chỉ tổ làm ta **chậm hơn**.*

Có hai lẽ. Một, Peter **tưởng bở** — bỏ test, bỏ refactor, bỏ regression chẳng làm anh nhanh hơn đâu. Hai, người chuyên nghiệp thì **đã cam kết từ trước** với một loạt chuẩn mực (code phải có test, phải sạch, không được phá vỡ phần khác), và mọi cam kết về sau đều phải nằm dưới cái cam kết gốc đó. Rốt cuộc Peter chốt một đề nghị vừa thật thà vừa có kỷ luật: gọi về nhà xin phép làm thêm, xong trước sáng thứ Hai, sáng thứ Hai có mặt để phối hợp với Willy — rồi sau đó nghỉ tới thứ Tư, bởi:

> [!quote] The Clean Coder — Ch.3 (tr. 56)
> "Professionals know their limits. They know how much overtime they can effectively apply, and they know what the cost will be."
>
> *Người chuyên nghiệp **biết rõ giới hạn của mình**. Họ biết mình làm thêm được tới đâu thì còn ra kết quả, và biết cái giá phải trả là gì.*

**Điều rút ra.** Nói Có không có nghĩa là gật với mọi thứ:

> [!quote] The Clean Coder — Ch.3 (tr. 56)
> "Professionals are not required to say yes to everything that is asked of them. However, they should work hard to find creative ways to make 'yes' possible."
>
> *Người chuyên nghiệp **không buộc phải nói Có với mọi yêu cầu**. Nhưng họ phải cố hết sức tìm ra cách sáng tạo để làm cho chữ "Có" **khả thi**.*

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống — gần như trọn vẹn:** đây là một trong những chương **già đi đẹp nhất** cả cuốn sách. "Ngôn ngữ cam kết" (*I will… by…*) chính là tinh thần của một loạt thực hành năm 2026: **Definition of Done** trong Scrum, mục tiêu **SMART**, phần cam kết trong sprint planning, và cái cột "blocker" nêu sớm trong daily standup — bản hiện đại của câu "giương cờ đỏ thật sớm". Nguyên tắc "chỉ cam kết cái trong tầm mình; phụ thuộc người khác thì cam kết *hành động*" trùng khít với văn hoá *async, ownership rõ ràng* bây giờ.
> **Một sắc thái cần cân:** làn sóng ước lượng theo xác suất (dải thời gian, story point, thậm chí *#NoEstimates*) nổi lên sau 2011 có cảnh báo: ép mọi thứ về khuôn "Tôi sẽ xong **trước** ngày X" nhị phân dễ đẻ ra cam kết giả khi công việc thực sự bất định. Nhưng chính Uncle Bob đã cài sẵn lời giải qua Peter: chưa chắc thì cứ **nói thẳng cái dải bất định** ("có thể thứ Hai, cũng có thể thứ Ba") thay vì phịa ra một mốc cứng. Ghép lại: dùng ngôn ngữ cam kết cho *phần mình nắm chắc*, dùng ngôn ngữ xác suất cho *phần còn bất định* — đừng trộn hai thứ vào nhau.
> **Phần vẫn phải cảnh giác:** đoạn "vạch lằn ranh, không bỏ test để chạy nhanh" thì đúng hơn bao giờ hết trong thời CI/CD; còn chi tiết "làm thêm cuối tuần" nên đọc kèm [Bài 11 (Áp lực)](bai_11_ap_luc.md) — 2026 xem overtime là *ngoại lệ có tính toán và có cái giá của nó*, chứ không phải một công cụ để dùng thường trực.

## 7. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Soi lại ngôn ngữ standup của bạn.** Thử một ngày, đếm xem bạn (và đồng đội) dùng bao nhiêu lần các chữ *need / should / hope / wish / let's* khi nói về việc của mình. Mỗi lần như thế, viết lại thành câu "Tôi sẽ… trước…" — hoặc thành một cam kết *hành động* nếu việc còn phụ thuộc người khác.
> 2. **Tập "giương cờ đỏ sớm".** Lần tới, hễ ngờ một cam kết sắp trượt, hãy báo *ngay cái hôm nhận ra* thay vì để đến sát hạn. Rồi để ý: người khác có kịp giúp hay đổi ưu tiên không?
> 3. **Vạch lằn ranh của Peter.** Viết ra danh sách những kỷ luật bạn **nhất định không** đánh đổi để chạy cho nhanh (test, review, regression). Đó là "cam kết gốc" mà mọi cam kết về deadline đều phải nằm dưới.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **Câu "chắc vậy" của bạn.** Nhớ một lần bạn cũng gật đầu nửa vời hệt như Uncle Bob trước mặt CEO. Nếu nói lại bằng ngôn ngữ cam kết (hoặc từ chối cho thẳng), câu đó sẽ ra sao?
> 2. **Cam kết hành động khi đích còn phụ thuộc người khác.** Chọn một mục tiêu của bạn đang "kẹt vì người khác". Tách ra 2–3 *việc nằm trong tầm tay bạn* mà bạn có thể cam kết làm ngay tuần này.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Say · Mean · Do** | Ba tầng của cam kết thật: nói → thật lòng → làm (tr. 47). |
| **Từ báo động thiếu cam kết** | *need/should, hope/wish, let's* — đặt kết quả ngoài tầm tay mình (tr. 48). |
| **"I will… by…"** | Khuôn câu của cam kết thật: hành động của chính bạn + mốc rõ + kết quả nhị phân (tr. 49). |
| **Cam kết hành động** | Khi đích phụ thuộc người khác/bất định, cam kết các *bước trong tầm kiểm soát* thay vì cam kết cả đích (tr. 50). |
| **Raise a red flag** (giương cờ đỏ) | Báo sớm khi cam kết sắp trượt, để người khác kịp giúp/đổi ưu tiên (tr. 51). |
| **Draw the line** (vạch lằn ranh) | Không đánh đổi kỷ luật (test, refactor, regression) để chạy nhanh — vì phá kỷ luật chỉ làm chậm hơn (tr. 55). |

## 9. Câu hỏi tự kiểm tra

1. Câu "I'm committed… I guess" thiếu tầng nào trong ba tầng *Say·Mean·Do*? *(tr. 47)*
2. Ba nhóm từ báo động sự thiếu cam kết là gì? *(tr. 48)*
3. Khuôn câu của cam kết thật là gì, và vì sao nó tạo kết quả nhị phân? *(tr. 49)*
4. Khi đích phụ thuộc người khác hoặc bạn chưa chắc làm được, bạn cam kết cái gì thay thế? *(tr. 50–51)*
5. Peter suýt "phá kỷ luật" nào để chạy nhanh, và vì sao đó là sai lầm kép? *(tr. 55)*
6. Ngôn ngữ cam kết (*I will… by…*) và ngôn ngữ xác suất (dải bất định) nên dùng cho loại công việc nào — theo góc nhìn 2026?

## Tóm tắt một trang

```
BÀI 3 — NÓI CÓ: NGÔN NGỮ CỦA SỰ CAM KẾT
────────────────────────────────────────────────────────
MỞ ĐẦU  Bob trèo cây sồi chờ CEO xin khởi động lại ER (voice
        mail). CEO đẩy gánh nặng về. Bob: "I'm committed…
        I guess" (tr. 47) — cam kết thảm hại.

SAY·MEAN·DO  Cam kết thật = nói + thật lòng + làm (tr. 47).

CA 1  Từ báo động thiếu cam kết: need/should · hope/wish · let's
      (tr. 48). Chúng đẩy kết quả ra ngoài tầm tay "tôi". Sự thật
      giải phóng: bạn LUÔN có điều gì đó trong tầm kiểm soát.

CAM KẾT THẬT  "I will … by …" → kết quả nhị phân (tr. 49).
      Phụ thuộc người khác/chưa chắc → cam kết HÀNH ĐỘNG (tr. 50).
      Sắp trượt → giương cờ đỏ SỚM (tr. 51).

CA 2  Peter/Marge: "try" nghĩa "maybe" = nhoè. Nói thật dải bất
      định. Suýt bỏ test/refactor/regression để nhanh →
      "professional draws the line"; phá kỷ luật chỉ CHẬM hơn
      (tr. 55). "Professionals know their limits" (tr. 56).

CHỐT  Không buộc nói Có với mọi thứ, nhưng phải tìm cách sáng
      tạo làm chữ "Có" khả thi (tr. 56).

2026  Ngôn ngữ cam kết = Definition of Done / SMART / blocker
      nêu sớm (GIỮ). Bổ sung: dùng ngôn ngữ xác suất cho phần
      bất định, đừng ép mốc cứng giả tạo.
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.3 **Saying Yes** (`tr. 45–56`): ca voice mail / ER và câu "I'm committed… I guess" (tr. 45–47); phần khách mời **Roy Osherove**, "A Language of Commitment" — Say·Mean·Do, từ báo động, "I will… by…", cam kết hành động, giương cờ đỏ (tr. 47–52); "Learning How to Say Yes" và ca Peter–Marge, "the professional draws the line", "know their limits" (tr. 52–56). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 ← bạn đang ở đây] · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
