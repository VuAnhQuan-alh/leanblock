# Bài 8 — Chiến lược kiểm thử: kim tự tháp để "QA không tìm thấy gì"

> [!info] Về bài này
> Dựng từ **Chương 8 — Testing Strategies** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 113–119`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Cần đọc trước: [Bài 5 — TDD](bai_05_tdd.md), [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md).

## Mục lục

1. [Mở đầu: ngày "săn bug" ở Rational, 1989](#1-mở-đầu-ngày-săn-bug-ở-rational-1989)
2. ["QA không được tìm thấy gì" — và QA là một phần của đội](#2-qa-không-được-tìm-thấy-gì--và-qa-là-một-phần-của-đội)
3. [Ca chính — Kim tự tháp tự động hoá kiểm thử](#3-ca-chính--kim-tự-tháp-tự-động-hoá-kiểm-thử)
4. [Kiểm thử khám phá thủ công: nơi con người vẫn cần](#4-kiểm-thử-khám-phá-thủ-công-nơi-con-người-vẫn-cần)
5. [Đối chiếu 2026](#5-đối-chiếu-2026)
6. [Áp dụng vào việc của bạn](#6-áp-dụng-vào-việc-của-bạn)
7. [Từ điển thuật ngữ](#7-từ-điển-thuật-ngữ)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mở đầu: ngày "săn bug" ở Rational, 1989

Năm 1989, Uncle Bob làm ở Rational trên bản phát hành đầu tiên của **Rose**. Cứ chừng một tháng, QA manager lại hô lên một ngày **"Bug Hunt"** (săn bug): *tất tần tật* mọi người trong đội — từ lập trình viên, quản lý, thư ký, cho tới quản trị viên cơ sở dữ liệu — ngồi xuống với Rose và ra sức làm cho nó hỏng. Có cả giải thưởng: ai moi được một con bug làm sập máy thì được một **bữa tối cho hai người**; ai bắt được nhiều bug nhất thì có khi ẵm luôn một **kỳ nghỉ cuối tuần ở Monterey**.

Cái ngày săn bug ấy chính là hạt mầm của chương này: viết được vài unit test hay vài acceptance test là tốt, nhưng **vẫn chưa đủ**. Cái mà mỗi đội chuyên nghiệp cần là một **chiến lược kiểm thử** hoàn chỉnh — một hệ thống gồm nhiều tầng.

## 2. "QA không được tìm thấy gì" — và QA là một phần của đội

Uncle Bob nhắc lại cái nguyên tắc từ [Bài 1](bai_01_tinh_chuyen_nghiep.md):

> [!quote] The Clean Coder — Ch.8 (tr. 114)
> "it should be the goal of the development group that QA find nothing wrong."
>
> *mục tiêu của nhóm phát triển phải là làm sao cho **QA không tìm ra một lỗi nào**.*

Tất nhiên cái mục tiêu ấy hiếm khi đạt trọn — một đám người thông minh cứ nhất quyết bới lỗi thì kiểu gì cũng bới ra vài cái. Nhưng cái đáng nói ở đây là *thái độ*:

> [!quote] The Clean Coder — Ch.8 (tr. 114)
> "every time QA finds something the development team should react in horror."
>
> *mỗi lần QA moi ra một lỗi, nhóm phát triển nên **giật mình kinh hãi** — tự hỏi vì sao nó lọt qua được, rồi tìm cách chặn nó tái diễn.*

Nói vậy *không* phải để biến QA thành kẻ thù. Ngược lại, QA là một phần của đội, với hai vai:

- **QA như người đặc tả (Specifiers).** Cùng bên nghiệp vụ viết ra các *acceptance test tự động* — thứ về sau thành tài liệu yêu cầu thật của cả hệ (xem [Bài 7](bai_07_acceptance_testing.md)). Nghiệp vụ lo đường "hạnh phúc"; QA lo ca góc, ca biên, đường "bất hạnh".
- **QA như người mô tả đặc tính (Characterizers).** Dùng **kiểm thử khám phá** (exploratory testing) để mô tả lại *hành vi thật* của hệ khi đang chạy — không phải để diễn giải yêu cầu, mà để chỉ ra hệ *thực sự* làm những gì.

## 3. Ca chính — Kim tự tháp tự động hoá kiểm thử

**Chuyện gì đã xảy ra.** Uncle Bob mượn **Kim tự tháp tự động hoá kiểm thử** (Test Automation Pyramid) của Mike Cohn để xếp các loại test mà một tổ chức chuyên nghiệp cần — từ nhiều-và-nhanh ở đáy cho tới ít-và-chậm ở đỉnh:

```
              ▲   Khám phá thủ công (con người)     ~5%
             ╱ ╲  ─────────────────────────────────────
            ╱   ╲  System tests (gui)               ~10%
           ╱     ╲ ─────────────────────────────────────
          ╱       ╲ Integration tests (api)         ~20%
         ╱         ╲───────────────────────────────────
        ╱           ╲ Component tests (api)          ~50%
       ╱             ╲─────────────────────────────────
      ╱               ╲ Unit tests (xUnit)          ~100%
     ╱_________________╲───────────────────────────────
   nhiều · nhanh · lập trình viên → ít · chậm · kiến trúc sư/người
```

**Điều rút ra.** Mỗi tầng có tác giả riêng, mục đích riêng và độ phủ riêng:

- **Unit tests (đáy, ~100% dòng thực).** Lập trình viên viết *cho lập trình viên*, bằng chính ngôn ngữ của hệ, để đặc tả ở mức thấp nhất; viết *trước* code (TDD), chạy trong CI. Độ phủ nên ở khoảng chín-mươi-mấy phần trăm, mà phải là *phủ thật* — chứ không phải mấy cái test rỗng chỉ chạy qua code chứ chẳng kiểm hành vi gì.
- **Component tests (~50%).** Chính là acceptance test, nhưng bọc quanh *từng thành phần* (nơi gói các luật nghiệp vụ): bơm dữ liệu vào, hứng kết quả ra, kiểm xem có khớp không; còn các thành phần khác thì tách ra bằng *mock/test-double*. QA + nghiệp vụ viết (dev phụ một tay), bằng FitNesse/JBehave/Cucumber. Chủ yếu là đường hạnh phúc cộng vài ca góc hiển nhiên.
- **Integration tests (~20%).** Chỉ có nghĩa với hệ lớn, nhiều thành phần: ráp từng nhóm thành phần lại rồi kiểm xem *chúng giao tiếp với nhau ăn ý tới đâu*:

> [!quote] The Clean Coder — Ch.8 (tr. 117)
> "Integration tests are choreography tests. They do not test business rules."
>
> *Integration test là **test vũ đạo** — kiểm xem các thành phần "nhảy" ăn khớp với nhau ra sao, chứ **không** kiểm luật nghiệp vụ.*

Kiến trúc sư hoặc lead viết; thường *không* nằm trong CI vì chạy lâu, nên đem chạy định kỳ (mỗi đêm, mỗi tuần). Test hiệu năng và thông lượng cũng nằm ở tầng này.
- **System tests (~10%).** Chạy trên *toàn bộ* hệ đã tích hợp — "integration test tối thượng". Không kiểm hành vi nghiệp vụ, mà kiểm xem **hệ có được ráp đúng cách** và các phần có phối hợp đúng kế hoạch không. Kiến trúc sư/technical lead viết.

## 4. Kiểm thử khám phá thủ công: nơi con người vẫn cần

Đỉnh kim tự tháp (~5%) là chỗ **con người đặt tay lên bàn phím, dán mắt vào màn hình** — không tự động, không kịch bản:

> [!quote] The Clean Coder — Ch.8 (tr. 118)
> "The intent of these tests is to explore the system for unexpected behaviors while confirming expected behaviors."
>
> *Mục đích của loại test này là **lục lọi khắp hệ để tìm những hành vi bất ngờ**, đồng thời xác nhận lại những hành vi vốn được mong đợi.*

Đây chính là mấy cái "ngày săn bug" ở đầu bài: càng đông người xúm vào "nện" hệ thì càng tốt. Và mục tiêu ở tầng này khác hẳn các tầng dưới:

> [!quote] The Clean Coder — Ch.8 (tr. 119)
> "The goal is not coverage. […] the goal is to ensure that the system behaves well under human operation and to creatively find as many 'peculiarities' as possible."
>
> *Mục tiêu **không** phải độ phủ. […] mục tiêu là bảo đảm hệ vận hành ngon lành dưới tay người thật, và **moi ra càng nhiều "điều kỳ quặc" càng tốt**, một cách sáng tạo.*

Chốt chương: TDD thì mạnh, acceptance test thì quý — nhưng đó cũng chỉ là *một phần*. Muốn giữ được lời "QA không tìm thấy gì", đội phải cùng QA dựng nên **cả một phả hệ** unit → component → integration → system → khám phá, rồi cho chạy càng thường xuyên càng tốt.

## 5. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — kim tự tháp: lõi bền, tỉ lệ linh hoạt
> **Còn sống:** cái ý cốt lõi — *nhiều test cấp thấp chạy nhanh làm nền, ít test cấp cao chạy chậm ở đỉnh* — tới năm 2026 vẫn là kim chỉ nam, dạy trong mọi khoá kiểm thử. Nó chống lại đúng cái phản-mẫu "**ly kem ốc quế**" (kim tự tháp lộn ngược: quá nhiều E2E chậm, quá ít unit).
> **Đã tinh chỉnh:** mấy cái *tỉ lệ* 100/50/20/10/5 chỉ là ước lệ, mà nay đã có những biến thể cạnh tranh — **Testing Trophy** của Kent C. Dodds thì dồn trọng lượng hơn cho *integration test* ("write tests. not too many. mostly integration"); còn với kiến trúc microservice, "**testing honeycomb**" lại đề nghị *nhiều integration, ít unit*. Bài học cho 2026: cứ giữ *hình dạng kim tự tháp* làm mặc định, nhưng chọn cách phân bố tuỳ theo *kiến trúc* của mình.
>
> [!warning] Đối chiếu 2026 — mô hình "QA" đã dịch chuyển
> Chương này ngầm cho rằng có một **nhóm QA riêng** chuyên viết acceptance test và tổ chức "bug hunt". Nhưng năm 2026 nhiều đội đã *dịch trái* xa hơn nữa: **"whole-team quality"** — cả đội cùng sở hữu chất lượng; vai QA chuyển thành **SDET** (kỹ sư kiểm thử biết code) hoặc *coach chất lượng*; không ít đội bỏ hẳn khâu QA thủ công riêng. Khẩu hiệu "QA should find nothing" thì vẫn đúng về *tinh thần*, chỉ có cách tổ chức là đã khác. Riêng kiểm thử khám phá thì *vẫn* được coi trọng như một nghề thủ công (session-based test management), mà 2026 lại có thêm **AI hỗ trợ sinh test và khám phá**.
> **Công cụ:** FitNesse/JBehave/Watir là đồ 2011; 2026 dùng Cucumber (vẫn còn), Playwright, Cypress, Testcontainers. Cái lệ "integration test không nằm trong CI vì chạy lâu" nay cũng nới ra: CI chạy song song cộng với môi trường phù du (ephemeral env) cho phép nhét thêm khối thứ vào pipeline.

## 6. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Vẽ kim tự tháp của dự án bạn.** Đếm thô số test ở mỗi tầng (unit / component / integration / system / E2E). Hình dạng thật là một cái kim tự tháp, hay là một "ly kem ốc quế"? Nếu ngược, thì tầng nào cần bồi thêm?
> 2. **Chọn cách phân bố theo kiến trúc.** Nếu bạn làm microservice, thử nghiêng về integration test (honeycomb); nếu là monolith, giữ kim tự tháp cổ điển. Viết một câu lý do cho lựa chọn đó.
> 3. **Tổ chức một "bug hunt" nhỏ.** Rủ vài người ngoài đội "nện" vào tính năng mới trong 30 phút — mục tiêu *không* phải phủ, mà là moi cho ra những "điều kỳ quặc".

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **Nhiều lớp kiểm, chứ đừng chỉ một.** Trong nghề bạn, việc kiểm chất lượng có bị dồn hết vào *một* lớp cuối (kiểu như chỉ có E2E) không? Có thể tách ra thành nhiều tầng nhanh-chậm khác nhau như thế nào?
> 2. **"Giật mình khi bị bắt lỗi".** Lần gần nhất người kiểm (biên tập, khách, sếp) moi ra lỗi của bạn — bạn phản ứng ra sao, và đã *tìm cách chặn nó tái diễn* chưa?

## 7. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Test Automation Pyramid** | Sắp xếp các loại test: nhiều-nhanh ở đáy (unit) → ít-chậm ở đỉnh (khám phá) (tr. 115). |
| **QA as specifiers / characterizers** | QA vừa *viết acceptance test đặc tả*, vừa *khám phá mô tả hành vi thật* của hệ (tr. 114). |
| **Component test** | Acceptance test bọc một thành phần (luật nghiệp vụ), tách phần còn lại bằng mock (tr. 116). |
| **Integration test ("choreography")** | Kiểm các thành phần *giao tiếp* với nhau, không kiểm luật nghiệp vụ (tr. 117). |
| **Exploratory testing** | Con người khám phá tìm hành vi bất ngờ, không kịch bản; mục tiêu không phải độ phủ (tr. 118–119). |
| **Ice-cream cone / Testing Trophy** | (Khung 2026) phản-mẫu kim tự tháp ngược; và biến thể dồn trọng lượng cho integration test. |

## 8. Câu hỏi tự kiểm tra

1. "Ngày săn bug" ở Rational minh hoạ tầng nào của kim tự tháp? *(tr. 113, 118)*
2. Hai vai của QA trong đội là gì? *(tr. 114)*
3. Kể tên năm tầng của kim tự tháp và độ phủ ước lệ mỗi tầng. *(tr. 115)*
4. Integration test kiểm cái gì, và vì sao gọi là "test vũ đạo"? *(tr. 117)*
5. Vì sao mục tiêu của kiểm thử khám phá *không* phải độ phủ? *(tr. 119)*
6. 2026 tinh chỉnh kim tự tháp ra sao — nêu một biến thể và lý do?

## Tóm tắt một trang

```
BÀI 8 — CHIẾN LƯỢC KIỂM THỬ: KIM TỰ THÁP ĐỂ "QA KHÔNG TÌM THẤY GÌ"
────────────────────────────────────────────────────────
MỞ ĐẦU  Rational 1989: ngày "Bug Hunt" — cả đội (kể cả thư ký)
        cố làm Rose hỏng; giải bữa tối/kỳ nghỉ.

NGUYÊN TẮC  Mục tiêu: "QA find nothing wrong" (tr. 114). QA tìm
        ra lỗi → "react in horror". QA là ĐỒNG ĐỘI: specifier
        (viết acceptance test) + characterizer (khám phá).

KIM TỰ THÁP (nhiều-nhanh → ít-chậm)
  Unit ~100% (dev, trong CI) · Component ~50% (acceptance, mock)
  Integration ~20% ("choreography", không CI) · System ~10%
  Khám phá thủ công ~5% (con người, không kịch bản).

KHÁM PHÁ  "explore for unexpected behaviors" (tr. 118). "Goal is
        not coverage" — tìm "điều kỳ quặc" (tr. 119).

2026  Hình kim tự tháp = GIỮ (chống "ly kem ốc quế"). Tỉ lệ linh
      hoạt: Testing Trophy / honeycomb theo kiến trúc. QA dịch
      trái → whole-team quality/SDET. Công cụ: Cucumber/Playwright.
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.8 **Testing Strategies** (`tr. 113–119`): ca "Bug Hunt" ở Rational 1989 (tr. 113–114); "QA Should Find Nothing" (tr. 114); "QA Is Part of the Team" — specifiers & characterizers (tr. 114–115); "The Test Automation Pyramid" (Mike Cohn) (tr. 115); unit / component / integration / system tests (tr. 116–118); "Manual Exploratory Tests" (tr. 118–119); Conclusion (tr. 119). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Bối cảnh 2026 (ngoài sách): Testing Trophy (Kent C. Dodds), testing honeycomb, whole-team quality / SDET, Playwright/Cypress/Testcontainers.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 ← bạn đang ở đây] · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
