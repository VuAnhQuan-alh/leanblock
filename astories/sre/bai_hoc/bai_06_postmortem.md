# Bài 6 — Postmortem culture: học từ sự cố, không đổ lỗi

> [!info] Về bài này
> Sự cố đã qua (Bài 5), hệ đã ổn — nhưng việc *quan trọng nhất* mới bắt đầu: **học để nó không tái diễn**. Công cụ là **postmortem**, và linh hồn là **blameless** (không đổ lỗi). Nghe "mềm mại" nhưng đây là một trong những ý tưởng *phản trực giác và mạnh nhất* của SRE: đổ lỗi cá nhân *làm giảm* độ tin cậy, còn văn hoá không-đổ-lỗi *tăng* nó.
> Nguồn: **SRE Book** — *Postmortem Culture: Learning from Failure*.
> **Trích:** `SRE: <chương>`. **Demo:** Node 22.
> Nên đọc trước: [Bài 5 (incident)](bai_05_incident-oncall.md).

## Mục lục

1. [Tình huống: cuộc họp "ai làm sập?"](#1-tình-huống-cuộc-họp-ai-làm-sập)
2. [Postmortem: để học, không để phạt](#2-postmortem-để-học-không-để-phạt)
3. [Blameless: hỏi "vì sao hệ cho phép", không "ai gây ra"](#3-blameless-hỏi-vì-sao-hệ-cho-phép-không-ai-gây-ra)
4. [Demo: chuỗi 5 whys](#4-demo-chuỗi-5-whys)
5. [Thẻ ôn (active recall)](#5-thẻ-ôn-active-recall)
6. [Câu hỏi tự kiểm tra](#6-câu-hỏi-tự-kiểm-tra)
7. [Tóm tắt một trang](#tóm-tắt-một-trang)
8. [Nguồn](#nguồn)

---

## 1. Tình huống: cuộc họp "ai làm sập?"

> [!example] Sáng hôm sau sự cố
> Sếp triệu tập họp: *"Ai deploy cái làm sập hệ tối qua?"*. Mọi ánh mắt đổ về `kỹ sư A`. A cúi mặt, bị khiển trách, nhắc nhở "cẩn thận hơn". Họp xong, ai cũng rút ra *một bài học*: **đừng để bị bắt**. Lần sau khi A (hoặc bất kỳ ai) gây ra một suýt-sự-cố, họ sẽ *im lặng*, *che giấu*, *không báo cáo* — vì báo cáo = bị phạt. Kết quả: công ty *mất* cơ hội học, và cùng loại lỗi đó sẽ *tái diễn* qua một người khác. Đổ lỗi tạo ra **văn hoá sợ hãi và che giấu** — kẻ thù số một của độ tin cậy.

SRE lật ngược hoàn toàn: sự cố không phải để *tìm thủ phạm*, mà để *tìm lỗ hổng hệ thống*. Công cụ là postmortem.

## 2. Postmortem: để học, không để phạt

> [!quote] SRE: postmortem-culture
> "A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve it, the root cause(s), and the follow-up actions to prevent the incident from recurring."
>
> *Một **postmortem** là một **bản ghi** về sự cố: tác động, các hành động để cầm máu/giải quyết, **nguyên nhân gốc**, và **các hành động tiếp theo để ngăn sự cố tái diễn**.*

Chú ý vế cuối — *ngăn tái diễn* — đó là mục đích. Và tư thế tinh thần phải đúng:

> [!quote] SRE: postmortem-culture
> "Writing a postmortem is not punishment—it is a learning opportunity for the entire company."
>
> *Viết postmortem **không phải hình phạt** — nó là **cơ hội học** cho toàn công ty.*

Nếu postmortem bị coi là "bản án", không ai muốn viết thật → mất học. Nếu nó là "bài học chung", người ta *chủ động* chia sẻ cả những suýt-sự-cố. Chìa khoá để đạt điều đó là một chữ: blameless.

## 3. Blameless: hỏi "vì sao hệ cho phép", không "ai gây ra"

> [!quote] SRE: postmortem-culture
> "A blamelessly written postmortem assumes that everyone involved in an incident had good intentions and did the right thing with the information they had."
>
> *Một postmortem **viết không-đổ-lỗi** giả định rằng **mọi người liên quan đều có thiện chí và đã làm điều đúng với thông tin họ có** lúc đó.*

Điều này *không* phải "tha lỗi" hay "ai cũng đúng". Nó là một *kỹ thuật tìm nguyên nhân*: nếu một người giỏi, có thiện chí vẫn gây ra sự cố, thì vấn đề *không nằm ở người* — mà ở **hệ thống đã cho phép** một hành động bình thường trở thành thảm hoạ. Hỏi *"vì sao hệ cho phép điều này xảy ra?"* dẫn tới fix *hệ thống* (ngăn tái diễn cho mọi người); hỏi *"ai làm?"* dừng ở người (không ngăn được gì).

> [!example] Ẩn dụ: điều tra tai nạn máy bay
> Ngành hàng không an toàn nhất thế giới *chính nhờ* văn hoá này. Khi có sự cố, điều tra viên **không** đổ lỗi phi công rồi đóng hồ sơ. Họ hỏi: *"vì sao hệ thống cho phép một sai sót của phi công thành thảm hoạ?"* → thêm cảnh báo tự động, checklist, thiết kế buồng lái chống nhầm lẫn. Mỗi tai nạn làm *cả ngành* an toàn hơn — vì phi công *dám báo cáo* suýt-va-chạm mà không sợ mất việc. Đổ lỗi cá nhân sẽ khiến họ im lặng, và máy bay sẽ *kém* an toàn.

Nghịch lý cốt lõi: **đổ lỗi → sợ → giấu → ít học → kém tin cậy; blameless → an toàn tâm lý → báo cáo thật → học nhiều → tin cậy hơn.** Demo mục 4 cho thấy cùng một sự cố, hai cách hỏi dẫn tới hai loại hành động khác hẳn.

## 4. Demo: chuỗi 5 whys

Kỹ thuật "5 whys": hỏi "vì sao" liên tục để đi từ *triệu chứng* tới *gốc hệ thống*. Đổ lỗi người dừng ở why #1; blameless đào tiếp tới fix ngăn tái diễn:

```typescript
// Postmortem BLAMELESS: hỏi "VÌ SAO HỆ cho phép điều này" thay vì "AI gây ra".
// Đổ lỗi người → dừng ở "người bất cẩn" → action vô dụng (phạt/đào tạo lại).
// Đào tới gốc HỆ THỐNG → action NGĂN TÁI DIỄN (thêm rào chắn).
const whys = [
  "Sự cố: 30% request lỗi 20 phút",
  "vì sao? → một deploy xoá nhầm biến môi trường DB_URL",
  "vì sao deploy xoá được? → script deploy không validate config trước khi áp",
  "vì sao không validate? → không có bước kiểm bắt buộc trong pipeline",
  "vì sao thiếu bước đó? → pipeline chưa ai thiết kế guardrail cho config",
];
console.log("CHUỖI 5 WHYS:");
whys.forEach((w, i) => console.log(`  ${i === 0 ? "" : "↓ "}${w}`));

console.log("\nĐỔ LỖI NGƯỜI (dừng sớm ở why #1):");
console.log("   root cause = 'kỹ sư A bất cẩn' → action: phạt/đào tạo lại A");
console.log("   → KHÔNG ngăn tái diễn: kỹ sư B ngày mai vẫn xoá nhầm được.");

console.log("\nBLAMELESS (đào tới gốc hệ thống):");
console.log("   root cause = 'pipeline không có guardrail validate config'");
console.log("   → action: thêm bước validate bắt buộc + canary (B7)");
console.log("   → NGĂN tái diễn: không AI xoá nhầm được nữa, kể cả người mới.");

console.log("\nCùng sự cố, hai cách viết postmortem → hai loại action. Blameless không");
console.log("phải 'tha lỗi' — nó là HỎI ĐÚNG CÂU để tìm fix NGĂN TÁI DIỄN, không fix người.");
```

Kết quả chạy thật *(tất định)*:

```
CHUỖI 5 WHYS:
  Sự cố: 30% request lỗi 20 phút
  ↓ vì sao? → một deploy xoá nhầm biến môi trường DB_URL
  ↓ vì sao deploy xoá được? → script deploy không validate config trước khi áp
  ↓ vì sao không validate? → không có bước kiểm bắt buộc trong pipeline
  ↓ vì sao thiếu bước đó? → pipeline chưa ai thiết kế guardrail cho config

ĐỔ LỖI NGƯỜI (dừng sớm ở why #1):
   root cause = 'kỹ sư A bất cẩn' → action: phạt/đào tạo lại A
   → KHÔNG ngăn tái diễn: kỹ sư B ngày mai vẫn xoá nhầm được.

BLAMELESS (đào tới gốc hệ thống):
   root cause = 'pipeline không có guardrail validate config'
   → action: thêm bước validate bắt buộc + canary (B7)
   → NGĂN tái diễn: không AI xoá nhầm được nữa, kể cả người mới.

Cùng sự cố, hai cách viết postmortem → hai loại action. Blameless không
phải 'tha lỗi' — nó là HỎI ĐÚNG CÂU để tìm fix NGĂN TÁI DIỄN, không fix người.
```

Cùng một sự cố, *điểm dừng* của câu hỏi quyết định *chất lượng* bài học. Dừng ở "kỹ sư A bất cẩn" → action là "phạt A / đào tạo lại A" — **không ngăn được gì**: kỹ sư B (hoặc chính A lúc mệt) ngày mai vẫn xoá nhầm, vì *hệ thống* vẫn cho phép. Đào tiếp ("vì sao hệ cho phép?") → "pipeline thiếu guardrail" → action là "thêm bước validate bắt buộc" — **ngăn tái diễn cho mọi người, mãi mãi**. Đây là lý do blameless không phải sự tử tế suông mà là *kỹ thuật tìm fix tốt hơn*: nó ép bạn đi qua người, tới hệ thống — nơi duy nhất có thể sửa để không lặp lại. (Guardrail đó chính là CI/CD + validate của aws-fund Bài 6/8.)

> [!note] Tự thử
> 1. Viết chuỗi 5 whys cho một sự cố bạn từng gặp. Bạn dừng ở "ai" hay đào tới "hệ thống nào cho phép"?
> 2. Vì sao "action = đào tạo lại người" gần như luôn là một action *yếu* trong postmortem? (gợi ý: con người sẽ lại mệt/quên; hệ thống thì không.)
> 3. Một postmortem tốt có "action items" đánh số, có người phụ trách, có hạn. Vì sao "sẽ cẩn thận hơn" không phải action item hợp lệ?

## 5. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — Vì sao văn hoá đổ lỗi *làm giảm* độ tin cậy?
> **Đáp:** đổ lỗi → sợ → **giấu/không báo cáo** suýt-sự-cố → mất cơ hội học → cùng lỗi tái diễn. Sợ hãi + che giấu là kẻ thù của reliability.

> [!question] Thẻ 6.2 — Postmortem là gì? Mục đích vế cuối?
> **Đáp:** bản ghi sự cố (tác động, cầm máu, nguyên nhân gốc, hành động tiếp). Mục đích = **ngăn tái diễn**, và là *cơ hội học*, không phải hình phạt.

> [!question] Thẻ 6.3 — "Blameless" giả định gì? Nó có phải "tha lỗi"?
> **Đáp:** giả định mọi người có **thiện chí + làm đúng với thông tin họ có** lúc đó. KHÔNG phải tha lỗi — là *kỹ thuật*: nếu người giỏi vẫn gây lỗi thì vấn đề ở **hệ thống**.

> [!question] Thẻ 6.4 — "Vì sao hệ cho phép?" vs "Ai gây ra?" dẫn tới action khác nhau ra sao?
> **Đáp:** "ai?" → dừng ở người → phạt/đào tạo (không ngăn tái diễn). "vì sao hệ cho phép?" → fix **hệ thống** (guardrail) → ngăn mọi người lặp lại.

> [!question] Thẻ 6.5 — Nghịch lý cốt lõi của blameless?
> **Đáp:** đổ lỗi → sợ → giấu → ít học → kém tin cậy. Blameless → an toàn tâm lý → báo cáo thật → học nhiều → **tin cậy hơn**.

## 6. Câu hỏi tự kiểm tra

1. Mô tả cuộc họp "ai làm sập?". Nó tạo văn hoá gì, hại reliability ra sao? *(mục 1)*
2. Postmortem là gì, mục đích chính? Vì sao "không phải hình phạt"? *(mục 2, SRE book)*
3. "Blameless" nghĩa là gì, KHÔNG nghĩa là gì? *(mục 3, SRE book)*
4. Chạy demo mục 4. Vì sao "đào tạo lại người" không ngăn tái diễn mà "thêm guardrail" thì có? *(mục 4)*
5. Phát biểu nghịch lý: đổ lỗi vs blameless ảnh hưởng độ tin cậy thế nào? *(mục 3)*

## Tóm tắt một trang

```
BÀI 6 — POSTMORTEM CULTURE (BLAMELESS)
─────────────────────────────────────────────────────────
ĐỔ LỖI = KẺ THÙ  họp "ai làm sập?" → sợ → giấu/không báo cáo → mất học → tái
   diễn. Văn hoá sợ hãi + che giấu hại reliability.

POSTMORTEM  bản ghi sự cố (tác động, cầm máu, nguyên nhân gốc, hành động ngăn
   TÁI DIỄN) (SRE book). KHÔNG phải hình phạt — là CƠ HỘI HỌC.

BLAMELESS  giả định mọi người có THIỆN CHÍ + làm đúng với thông tin lúc đó
   (SRE book). KHÔNG phải "tha lỗi" — là KỸ THUẬT: người giỏi vẫn lỗi ⇒ vấn đề
   ở HỆ THỐNG. (ẩn dụ: điều tra tai nạn máy bay.)

HỎI ĐÚNG CÂU  "ai gây ra?" → dừng ở người → phạt (vô dụng). "vì sao HỆ cho
   phép?" → fix hệ thống (guardrail) → NGĂN tái diễn cho mọi người.

DEMO  5 whys: "A bất cẩn" (dừng #1 → đào tạo lại A, không ngăn) vs "pipeline
   thiếu guardrail" (gốc → thêm validate bắt buộc, ngăn mãi mãi).

NGHỊCH LÝ  đổ lỗi→sợ→giấu→ít học→kém tin cậy. Blameless→báo cáo thật→học→TIN
   CẬY HƠN. (guardrail = CI/CD aws-fund B6/8.)
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Postmortem Culture: Learning from Failure**: định nghĩa postmortem, "not punishment", blameless giả định thiện chí. `tai_lieu/sre_postmortem-culture.txt`.
- Nối: [Bài 5 (incident)](bai_05_incident-oncall.md), [Bài 7 (ngăn cascading)](bai_07_overload-cascading.md); guardrail: [aws-fund Bài 6 (CI/CD)](../../aws-fund/bai_hoc/bai_06_cicd.md), [Bài 8 (IaC)](../../aws-fund/bai_hoc/bai_08_infrastructure-as-code.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · **[Bài 6 — Postmortem] ← bạn đang ở đây** · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
