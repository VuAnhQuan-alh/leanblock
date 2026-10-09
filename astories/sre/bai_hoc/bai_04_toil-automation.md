# Bài 4 — Toil và tự động hoá

> [!info] Về bài này
> SRE không phải "ops làm tay nhanh hơn" — mà là **kỹ sư dùng code để *xoá* việc tay**. Khái niệm trung tâm: **toil** (việc tay lặp lại, không giá trị lâu dài, phình tuyến tính theo quy mô). Bài này định nghĩa toil cho chặt, cho thấy vì sao nó *nguy hiểm* (nuốt dần 100% thời gian → không còn giờ cải thiện hệ), và luật "**tối thiểu 50% thời gian làm kỹ thuật**".
> Nguồn: **SRE Book** — *Eliminating Toil*.
> **Trích:** `SRE: <chương>`. **Demo:** Node 22.
> Nên đọc trước: [Bài 0 (SRE là gì)](bai_00_sre-la-gi-error-budget.md); công cụ: [aws-fund Bài 8 (IaC)](../../aws-fund/bai_hoc/bai_08_infrastructure-as-code.md).

## Mục lục

1. [Tình huống: cả ngày đi restart service](#1-tình-huống-cả-ngày-đi-restart-service)
2. [Toil là gì (không phải "việc tao ghét")](#2-toil-là-gì-không-phải-việc-tao-ghét)
3. [Vì sao toil nguy hiểm, và cap 50%](#3-vì-sao-toil-nguy-hiểm-và-cap-50)
4. [Demo: kinh tế tự động hoá toil](#4-demo-kinh-tế-tự-động-hoá-toil)
5. [Thẻ ôn (active recall)](#5-thẻ-ôn-active-recall)
6. [Câu hỏi tự kiểm tra](#6-câu-hỏi-tự-kiểm-tra)
7. [Tóm tắt một trang](#tóm-tắt-một-trang)
8. [Nguồn](#nguồn)

---

## 1. Tình huống: cả ngày đi restart service

> [!example] Một ngày của bạn
> 9h: một service treo, bạn SSH vào restart (10 phút). 10h30: service khác, restart lại. 11h: tạo tay một tài khoản cho khách mới (15 phút). 14h: dọn log đầy ổ. 15h: lại restart. Cuối ngày bạn *kiệt sức* mà nhìn lại — **không làm được gì mới**, chỉ chạy quanh dập lửa. Mai lại y hệt. Dịch vụ càng đông khách, số lần restart/tạo tài khoản càng nhiều. Bạn đang chạy trên một *vòng quay chuột hamster* ngày càng nhanh.

Những việc đó có tên: **toil**. Và chúng không chỉ mệt — chúng *nguy hiểm về mặt cấu trúc*, vì chúng phình theo quy mô trong khi thời gian của bạn thì không.

## 2. Toil là gì (không phải "việc tao ghét")

Toil có định nghĩa *chính xác*, không phải "việc chán":

> [!quote] SRE: eliminating-toil
> "Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows."
>
> ***Toil** là loại việc gắn với vận hành dịch vụ production, thường **thủ công, lặp lại, tự-động-hoá-được, chiến thuật (tactical), không có giá trị lâu dài, và *scale tuyến tính* khi dịch vụ lớn lên**.*

Sáu đặc điểm — chú ý hai cái cuối. *"Không giá trị lâu dài"*: xong một lần restart, hệ không *tốt lên*, chỉ trở về như cũ (khác với viết code sửa gốc — giá trị còn mãi). *"Scale tuyến tính"*: gấp đôi khách → gấp đôi số lần restart. Đây là phần chết người.

> [!example] Ẩn dụ: tát nước thuyền thủng
> Toil như **tát nước khỏi một con thuyền thủng**. Thuyền càng to, nước vào càng nhiều, bạn tát càng mệt — và tát mãi mãi. *Vá lỗ thủng* (tự động hoá / sửa gốc) tốn công một lần nhưng rồi bạn *hết phải tát*. Người làm việc hiệu quả không tát nhanh hơn — họ *vá lỗ*.

## 3. Vì sao toil nguy hiểm, và cap 50%

Nếu không chặn, toil có một thuộc tính ác:

> [!quote] SRE: eliminating-toil
> "We share this 50% goal because toil tends to expand if left unchecked and can quickly fill 100% of everyone's time."
>
> *Chúng tôi nêu mục tiêu 50% này vì **toil có xu hướng phình ra nếu không kiểm soát và nhanh chóng lấp đầy 100% thời gian của mọi người**.*

Vòng xoáy tử thần: toil phình → bạn bận tát nước → không còn giờ vá lỗ → toil phình tiếp → ... cho tới khi cả đội làm ops tay 100%, không ai cải thiện gì, và kiệt sức. SRE chặn vòng này bằng một luật cứng:

> [!quote] SRE: eliminating-toil
> "At least 50% of each SRE's time should be spent on engineering project work that will either reduce future toil or add service features."
>
> ***Tối thiểu 50%** thời gian mỗi SRE phải dành cho **việc kỹ thuật (engineering)** — hoặc *giảm toil tương lai*, hoặc *thêm tính năng*.*

Nửa còn lại được phép làm ops/toil, nhưng *trần 50%* đảm bảo luôn có thời gian *vá lỗ*. Nếu toil vượt 50%, đó là tín hiệu phải *dừng nhận việc tay* và đầu tư tự động hoá (hoặc trả bớt dịch vụ về cho dev). Đây là điều phân biệt SRE với "sysadmin truyền thống": SRE coi mỗi việc tay là *một bug cần sửa bằng code*, không phải *một nhiệm vụ cần làm nhanh hơn*. Demo mục 4 cho thấy phép tính "vá lỗ có đáng không".

## 4. Demo: kinh tế tự động hoá toil

Toil scale tuyến tính; automation là chi phí một lần. Tính điểm hoà vốn + lợi ích — và vì sao scale càng lớn, automation càng đáng:

```typescript
// TOIL = việc tay, lặp lại, tự-động-hoá-được, không giá trị lâu dài, và SCALE
// TUYẾN TÍNH theo dịch vụ. Tự động hoá = chi phí MỘT LẦN. Khi scale tăng, toil
// phình tuyến tính còn automation đứng yên → luôn đáng ở quy mô đủ lớn.
const MANUAL_MIN = 15;          // mỗi lần làm tay 15 phút
const RUNS_PER_WEEK = 20;       // chạy 20 lần/tuần
const AUTOMATION_HOURS = 40;    // dựng tự động tốn 40 giờ (một lần)

const manualHrsPerWeek = MANUAL_MIN * RUNS_PER_WEEK / 60;
const breakEvenWeeks = AUTOMATION_HOURS / manualHrsPerWeek;
const yearSavedHrs = manualHrsPerWeek * 52 - AUTOMATION_HOURS;

console.log(`Việc tay: ${MANUAL_MIN} phút × ${RUNS_PER_WEEK} lần/tuần = ${manualHrsPerWeek} giờ/tuần toil`);
console.log(`Tự động hoá: ${AUTOMATION_HOURS} giờ (một lần)\n`);
console.log(`  hoà vốn sau: ${breakEvenWeeks.toFixed(1)} tuần`);
console.log(`  tiết kiệm năm đầu: ${yearSavedHrs.toFixed(0)} giờ (≈ ${(yearSavedHrs/8).toFixed(0)} ngày công)`);

console.log(`\nKhi dịch vụ LỚN GẤP ĐÔI (toil scale tuyến tính → ${RUNS_PER_WEEK*2} lần/tuần):`);
const manual2 = MANUAL_MIN * RUNS_PER_WEEK*2 / 60;
console.log(`  toil = ${manual2} giờ/tuần, hoà vốn chỉ ${(AUTOMATION_HOURS/manual2).toFixed(1)} tuần — automation CÀNG đáng.`);
console.log(`\nToil nguy hiểm vì PHÌNH tuyến tính: không tự động hoá → nó nuốt dần 100% thời gian`);
console.log(`→ không còn giờ làm kỹ thuật → không giảm được toil → vòng xoáy. Vì sao cần cap 50%.`);
```

Kết quả chạy thật *(tất định)*:

```
Việc tay: 15 phút × 20 lần/tuần = 5 giờ/tuần toil
Tự động hoá: 40 giờ (một lần)

  hoà vốn sau: 8.0 tuần
  tiết kiệm năm đầu: 220 giờ (≈ 28 ngày công)

Khi dịch vụ LỚN GẤP ĐÔI (toil scale tuyến tính → 40 lần/tuần):
  toil = 10 giờ/tuần, hoà vốn chỉ 4.0 tuần — automation CÀNG đáng.

Toil nguy hiểm vì PHÌNH tuyến tính: không tự động hoá → nó nuốt dần 100% thời gian
→ không còn giờ làm kỹ thuật → không giảm được toil → vòng xoáy. Vì sao cần cap 50%.
```

Phép tính rõ ràng: bỏ 40 giờ tự động hoá, hoà vốn sau **8 tuần**, rồi *lãi* 220 giờ/năm (28 ngày công) mãi mãi. Và vì toil *scale tuyến tính* (dịch vụ gấp đôi → 40 lần/tuần), điểm hoà vốn rút còn **4 tuần** — càng lớn càng phải tự động. Đây là lý do "cứ làm tay cho nhanh" là bẫy: nó *rẻ hôm nay, đắt cấp số về sau*. Lưu ý mắt xích: tự động hoá này chính là **IaC + CI/CD** của [aws-fund Bài 8](../../aws-fund/bai_hoc/bai_08_infrastructure-as-code.md)/[Bài 6](../../aws-fund/bai_hoc/bai_06_cicd.md) — dựng/sửa hạ tầng bằng code thay vì click tay là xoá toil tận gốc.

> [!note] Tự thử
> 1. Đổi `AUTOMATION_HOURS` lên `200` (việc khó tự động): hoà vốn bao lâu? Có ngưỡng nào mà *không* nên tự động hoá (gợi ý: việc hiếm + khó tự động)?
> 2. Thêm "chi phí bảo trì automation" (vd 2 giờ/tháng): phép tính đổi ra sao? Vì sao automation cũng cần chăm?
> 3. Một việc chạy *1 lần/năm*: tự động hoá có đáng không? Khi nào viết tài liệu (runbook) tốt hơn viết code?

## 5. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — Toil là gì (định nghĩa chặt, không phải "việc chán")?
> **Đáp:** việc vận hành production **thủ công, lặp lại, tự-động-hoá-được, tactical, không giá trị lâu dài, scale tuyến tính** theo dịch vụ.

> [!question] Thẻ 4.2 — Hai đặc điểm chết người nhất của toil?
> **Đáp:** *không giá trị lâu dài* (làm xong hệ không tốt lên, chỉ về như cũ) + *scale tuyến tính* (gấp đôi khách → gấp đôi toil, trong khi thời gian bạn không tăng).

> [!question] Thẻ 4.3 — "Vòng xoáy tử thần" của toil? Luật chặn nó?
> **Đáp:** toil phình → bận tát nước → không còn giờ vá lỗ → phình tiếp → kiệt sức 100% ops. Chặn bằng **cap: tối thiểu 50% thời gian làm kỹ thuật**.

> [!question] Thẻ 4.4 — Vì sao automation gần như luôn đáng ở quy mô lớn?
> **Đáp:** toil scale *tuyến tính*, automation là chi phí *một lần* → điểm hoà vốn càng ngắn khi scale càng lớn; sau đó lãi mãi.

> [!question] Thẻ 4.5 — SRE khác sysadmin truyền thống ở tư duy nào?
> **Đáp:** SRE coi mỗi việc tay là **một bug cần sửa bằng code**, không phải nhiệm vụ cần làm *nhanh hơn*. "Vá lỗ" thay vì "tát nước nhanh".

## 6. Câu hỏi tự kiểm tra

1. Định nghĩa toil (6 đặc điểm). Vì sao "việc tao ghét" không phải định nghĩa? *(mục 2, SRE book)*
2. Ẩn dụ "tát nước thuyền thủng" nói gì về toil vs sửa gốc? *(mục 2)*
3. Vòng xoáy toil + luật 50%. Vì sao cần trần cứng? *(mục 3, SRE book)*
4. Chạy demo mục 4. Vì sao scale càng lớn automation càng đáng? Khi nào *không* nên tự động? *(mục 4, Tự thử)*
5. Tự động hoá toil nối về khái niệm AWS nào? *(mục 4)*

## Tóm tắt một trang

```
BÀI 4 — TOIL & AUTOMATION
─────────────────────────────────────────────────────────
TOIL (SRE book)  việc production THỦ CÔNG, LẶP LẠI, tự-động-hoá-được, tactical,
   KHÔNG giá trị lâu dài, SCALE TUYẾN TÍNH. Không phải "việc tao ghét".
   (ẩn dụ: tát nước thuyền thủng — vá lỗ thay vì tát nhanh.)

NGUY HIỂM  2 đặc điểm chết: không-giá-trị-lâu-dài + scale-tuyến-tính. Vòng
   xoáy: toil phình → bận tát → không vá lỗ → phình tiếp → kiệt sức 100% ops.

LUẬT 50%  tối thiểu 50% thời gian làm KỸ THUẬT (giảm toil / thêm tính năng)
   (SRE book). Toil phình nếu không chặn → lấp 100%. SRE = coi việc tay là BUG
   cần sửa bằng code, không phải nhiệm vụ làm nhanh hơn.

DEMO  15ph×20/tuần=5h toil. Automation 40h → hoà vốn 8 tuần, lãi 220h/năm.
   Dịch vụ gấp đôi → hoà vốn 4 tuần (càng lớn càng đáng).

→ automation = IaC + CI/CD (aws-fund B8/B6): sửa hạ tầng bằng code, không click tay.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Eliminating Toil**: định nghĩa toil, luật 50%, toil phình nếu không chặn. `tai_lieu/sre_eliminating-toil.txt`.
- Nối: [Bài 0 (SRE là gì)](bai_00_sre-la-gi-error-budget.md); automation: [aws-fund Bài 8 (IaC)](../../aws-fund/bai_hoc/bai_08_infrastructure-as-code.md), [Bài 6 (CI/CD)](../../aws-fund/bai_hoc/bai_06_cicd.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · **[Bài 4 — Toil & automation] ← bạn đang ở đây** · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
