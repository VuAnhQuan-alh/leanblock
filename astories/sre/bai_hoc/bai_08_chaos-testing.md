# Bài 8 — Chaos engineering và kiểm thử độ tin cậy

> [!info] Về bài này
> **Bài cuối.** Bạn đã dựng SLO (Bài 1), observability (Bài 2), alert (Bài 3), ứng cứu (Bài 5), chống cascade (Bài 7). Nhưng — *làm sao biết chúng thật sự chạy khi cần?* Câu trả lời của SRE: **đừng tin, hãy kiểm** — chủ động tiêm lỗi vào hệ (có kiểm soát) để biến giả định "chắc ổn" thành sự thật đã kiểm. Đó là **chaos engineering / DiRT**. Bài này cũng **khép khoá** và khép cả bốn tầng của mạch cloud.
> Nguồn: **SRE Book** (*Testing for Reliability*) + **SREWB** (*DiRT*).
> **Trích:** `SRE: <chương>` · `SREWB (tr. X)`. **Demo:** Node 22.
> Nên đọc trước: [aws-design Bài 8 (DR)](../../aws-design/bai_hoc/bai_08_da-vung-dr.md), [Bài 5 (incident)](bai_05_incident-oncall.md).

## Mục lục

1. [Tình huống: "chắc chạy thôi"](#1-tình-huống-chắc-chạy-thôi)
2. [SRE lượng hoá niềm tin](#2-sre-lượng-hoá-niềm-tin)
3. [Chaos engineering và DiRT](#3-chaos-engineering-và-dirt)
4. [Demo: game day](#4-demo-game-day)
5. [Khép khoá SRE và bốn tầng](#5-khép-khoá-sre-và-bốn-tầng)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Tình huống: "chắc chạy thôi"

> [!example] Niềm tin chưa bao giờ bị thử
> Kiến trúc của bạn "kiên cường": Multi-AZ failover, backup S3 hằng đêm, cache fallback khi DB chậm, circuit breaker chống cascade. Sếp hỏi "nếu AZ chính sập thì sao?" — bạn tự tin: "có failover, chắc ổn". Nhưng... *đã ai từng thử tắt AZ chính chưa?* Không. *Đã ai thử khôi phục từ backup chưa?* Không. Rồi một đêm Chủ nhật, AZ chính sập thật — và bạn phát hiện: failover *có* chạy, nhưng **backup đã hỏng âm thầm 3 tháng nay** và **code cache fallback chưa từng chạy nên có bug**. Niềm tin của bạn là **ảo tưởng** — nó chưa bao giờ bị kiểm.

Đây là cái bẫy cuối của vận hành: *"có cơ chế"* ≠ *"cơ chế hoạt động"*. Một cơ chế dự phòng chưa test chính là đường fallback chưa test của [aws-design Bài 7](../../aws-design/bai_hoc/bai_07_chiu-tai-overload.md) — nó *sẽ* hỏng đúng lúc cần. SRE sửa bằng cách định nghĩa lại công việc của mình.

## 2. SRE lượng hoá niềm tin

> [!quote] SRE: testing-reliability
> "One key responsibility of Site Reliability Engineers is to quantify confidence in the systems they maintain."
>
> *Một trách nhiệm then chốt của SRE là **lượng hoá niềm tin (quantify confidence)** vào các hệ họ vận hành.*

"Lượng hoá niềm tin" nghĩa là: thay "tôi *nghĩ* nó chịu được" bằng "tôi *đã kiểm* và nó chịu được tới X". Công cụ là **testing** — không chỉ unit test code, mà test *cả hệ* dưới điều kiện lỗi. Và mức test cần làm tỉ lệ với mức tin cậy cần đạt:

> [!quote] SRE: testing-reliability
> "The amount of testing you need to conduct depends on the reliability requirements for your system."
>
> *Lượng kiểm thử cần làm **phụ thuộc vào yêu cầu độ tin cậy** của hệ.* (Nối Bài 1: SLO càng chặt → càng phải test nhiều.)

Test code bình thường kiểm "code có đúng không". Nhưng độ tin cậy sống/chết ở những thứ *chỉ xảy ra khi có sự cố*: failover, retry, circuit breaker, backup restore. Những đường đó *theo định nghĩa* hiếm chạy — nên phải *chủ động* ép chúng chạy. Đó là chaos engineering.

## 3. Chaos engineering và DiRT

> [!quote] SREWB (tr. 193)
> "Google runs company-wide resilience testing (called Disaster Recovery Testing, or DiRT [...] in which we create a controlled emergency that doesn't actually impact customers."
>
> *Google chạy **kiểm thử khả năng phục hồi toàn công ty** (gọi là **Disaster Recovery Testing, DiRT**), trong đó ta **tạo một tình huống khẩn cấp CÓ KIỂM SOÁT mà không thực sự ảnh hưởng khách hàng**.*

Ý tưởng cốt lõi: **chủ động tiêm lỗi** (tắt một AZ, giết một service, làm chậm mạng) *trong điều kiện kiểm soát* — giờ hành chính, có người trực, có nút dừng — để *phát hiện* chỗ hỏng *trước khi* sự cố thật phát hiện giùm bạn. Netflix gọi công cụ của họ là "Chaos Monkey".

> [!example] Ẩn dụ: diễn tập chữa cháy (và tiêm vaccine)
> Đội cứu hoả không đợi cháy thật mới lần đầu cầm vòi — họ **diễn tập** định kỳ với đám cháy giả, để lúc cháy thật mọi động tác đã thành phản xạ và mọi thiết bị đã được kiểm. Game day là *diễn tập chữa cháy cho hệ thống*. Hoặc nghĩ như **tiêm vaccine**: chủ động cho cơ thể gặp mầm bệnh (yếu, kiểm soát) để xây miễn dịch — thay vì đợi bệnh thật ập tới lúc yếu nhất.

Thực tế: bắt đầu nhỏ (một "game day" tắt một service trong staging), có giả thuyết rõ ("tin rằng failover < 30s"), đo kết quả, sửa chỗ hỏng, rồi mở rộng dần (production, có nút dừng). Mỗi lần chạy, một giả định biến thành sự thật đã kiểm — demo mục 4 cho thấy khoảng cách giữa "tin" và "thật".

## 4. Demo: game day

Năm cơ chế kiên chọc bạn *tin* là chạy. Chạy game day (tiêm lỗi có kiểm soát) để lộ sự thật:

```typescript
// Chaos engineering / DiRT = CHỦ ĐỘNG tiêm lỗi trong môi trường kiểm soát để
// biến GIẢ ĐỊNH ("failover chắc chạy") thành SỰ THẬT ĐÃ KIỂM. Không test =
// niềm tin giả: bạn tưởng mình kiên cường cho tới lúc sự cố thật phơi bày.
type Assumption = { name: string; believedWorks: boolean; actuallyWorks: boolean };
const system: Assumption[] = [
  { name: "Multi-AZ failover DB",        believedWorks: true, actuallyWorks: true },
  { name: "Khôi phục từ backup S3",      believedWorks: true, actuallyWorks: false }, // backup hỏng 3 tháng nay!
  { name: "Cache fallback khi DB chậm",  believedWorks: true, actuallyWorks: false }, // code fallback chưa từng chạy
  { name: "Auto-scale khi tải tăng",     believedWorks: true, actuallyWorks: true },
  { name: "Circuit breaker cắt cascade", believedWorks: true, actuallyWorks: false }, // cấu hình sai ngưỡng
];

const believed = system.filter(a => a.believedWorks).length;
console.log(`TRƯỚC game day: tin ${believed}/${system.length} cơ chế kiên cường "chắc chạy"\n`);
console.log("Chạy GAME DAY (tiêm lỗi có kiểm soát, không ảnh hưởng khách thật):");
let verified = 0;
for (const a of system) {
  const ok = a.actuallyWorks;
  if (ok) verified++;
  console.log(`  ${a.name.padEnd(28)} ${ok ? "hoạt động" : "HỎNG — phát hiện trước khi sự cố thật!"}`);
}
console.log(`\nSỰ THẬT: chỉ ${verified}/${system.length} thật sự chạy. ${believed - verified} "quả bom hẹn giờ" ẩn.`);
console.log("Niềm tin KHÔNG test = ảo tưởng. Game day biến giả định → sự thật đã kiểm,");
console.log("và tìm ra lỗi lúc 2h chiều thứ Ba (có kiểm soát) thay vì 3h sáng Chủ nhật (thật).");
```

Kết quả chạy thật *(tất định)*:

```
TRƯỚC game day: tin 5/5 cơ chế kiên cường "chắc chạy"

Chạy GAME DAY (tiêm lỗi có kiểm soát, không ảnh hưởng khách thật):
  Multi-AZ failover DB         hoạt động
  Khôi phục từ backup S3       HỎNG — phát hiện trước khi sự cố thật!
  Cache fallback khi DB chậm   HỎNG — phát hiện trước khi sự cố thật!
  Auto-scale khi tải tăng      hoạt động
  Circuit breaker cắt cascade  HỎNG — phát hiện trước khi sự cố thật!

SỰ THẬT: chỉ 2/5 thật sự chạy. 3 "quả bom hẹn giờ" ẩn.
Niềm tin KHÔNG test = ảo tưởng. Game day biến giả định → sự thật đã kiểm,
và tìm ra lỗi lúc 2h chiều thứ Ba (có kiểm soát) thay vì 3h sáng Chủ nhật (thật).
```

Bạn *tin* 5/5 chạy; sự thật chỉ **2/5**. Ba cơ chế — backup, cache fallback, circuit breaker — là **bom hẹn giờ ẩn**: trông ổn trên sơ đồ, nhưng sẽ phản bội bạn đúng lúc sự cố thật. Game day phát hiện chúng *lúc 2h chiều thứ Ba* (có người trực, có nút dừng, khách không bị ảnh hưởng) thay vì *3h sáng Chủ nhật* (sự cố thật, một mình, khách mất tiền). Đây là cách SRE "lượng hoá niềm tin": con số thật là 2/5, không phải 5/5 bạn *tưởng* — và giờ bạn biết phải sửa gì. Nối thẳng [aws-design Bài 8](../../aws-design/bai_hoc/bai_08_da-vung-dr.md): "static stability" nghĩa là đường phục hồi *đã chạy sẵn* — và chỉ game day mới chứng minh được điều đó là thật.

> [!note] Tự thử
> 1. Vì sao test trong *staging* chưa đủ, phải dần tiến tới *production* (có kiểm soát)? (gợi ý: staging không bao giờ giống hệt prod.)
> 2. Một game day tốt có "giả thuyết" ("tin failover < 30s") + "nút dừng" (abort). Vì sao cần cả hai trước khi tiêm lỗi vào prod?
> 3. Nối Bài 6: kết quả game day (3 cơ chế hỏng) nên dẫn tới gì — và xử blameless ra sao?

## 5. Khép khoá SRE và bốn tầng

Chín bài SRE là **một vòng khép giữ hệ sống**, tất cả xoay quanh error budget:

```
   error budget (Bài 0: cân bằng nhanh↔ổn)
        │ đo bằng
   SLI/SLO (1) ──nhìn bằng──▶ observability (2) ──biết bằng──▶ alert (3)
        │                                                          │ đánh thức
   diệt việc tay: toil/automation (4)              incident response (5)
        │                                                          │ học bằng
   chống lan: overload/cascade (7) ◀──ngừa bằng── postmortem (6)
        │ kiểm bằng
   chaos/game day (8) ──▶ quay lại tăng confidence cho SLO
```

Và **bốn tầng** của cả mạch cloud khép lại ở đây:

```
   sre          GIỮ hệ sống (SLO, error budget, incident, chaos)   ← vừa xong
   aws-design   LÀM SAO cho đúng (archetype, pattern)
   aws-fund     CÁI GÌ (dịch vụ AWS)
   cloud-base   VÌ SAO (nền CS)
```

Bạn giờ có trọn vòng đời: *hiểu nguyên lý → biết công cụ → thiết kế hệ → vận hành cho đáng tin*. Một kỹ sư đi hết bốn tầng này không chỉ "biết AWS" — họ *suy luận* được từ nền tảng tới vận hành, và đó là ranh giới senior → staff/architect. Chúc mừng bạn đã tới đỉnh kim tự tháp.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — Vì sao "có cơ chế dự phòng" ≠ "nó hoạt động"?
> **Đáp:** cơ chế dự phòng *theo định nghĩa* hiếm chạy → hiếm test → có thể hỏng âm thầm (backup hỏng, fallback có bug). Chưa test = niềm tin ảo tưởng.

> [!question] Thẻ 8.2 — "SRE lượng hoá niềm tin" nghĩa là gì?
> **Đáp:** thay "tôi *nghĩ* nó chịu được" bằng "tôi *đã kiểm* và nó chịu được tới X". Bằng testing cả hệ dưới điều kiện lỗi, không chỉ unit test code.

> [!question] Thẻ 8.3 — DiRT / chaos engineering là gì? Nguyên tắc cốt lõi?
> **Đáp:** tạo **tình huống khẩn cấp CÓ KIỂM SOÁT** (tiêm lỗi: tắt AZ, giết service) để phát hiện chỗ hỏng *trước* sự cố thật — giờ hành chính, có người trực, có nút dừng.

> [!question] Thẻ 8.4 — Vì sao "2h chiều thứ Ba" tốt hơn "3h sáng Chủ nhật"?
> **Đáp:** game day phát hiện lỗi trong điều kiện *kiểm soát* (người trực, nút dừng, khách không ảnh hưởng) thay vì sự cố thật (một mình, khách mất tiền).

> [!question] Thẻ 8.5 — Chaos nối với "static stability" (aws-design B8) ra sao?
> **Đáp:** static stability = đường phục hồi *đã chạy sẵn*. Chỉ game day/chaos mới *chứng minh* điều đó là thật, không phải giả định trên sơ đồ.

## 7. Câu hỏi tự kiểm tra

1. Mô tả bẫy "chắc chạy thôi". Cơ chế chưa test nối về khái niệm nào (aws-design B7)? *(mục 1)*
2. "Lượng hoá niềm tin" là gì? Vì sao test độ tin cậy khác test code? *(mục 2, SRE book)*
3. DiRT/chaos: nguyên tắc "có kiểm soát" gồm gì? Ẩn dụ diễn tập/vaccine. *(mục 3, SREWB tr.193)*
4. Chạy demo mục 4. Vì sao "tin 5/5" mà "thật 2/5"? Game day đổi điều đó ra sao? *(mục 4)*
5. (Khép khoá) Vẽ vòng 9 bài SRE quanh error budget. Bốn tầng cloud khép thế nào? *(mục 5)*

## Tóm tắt một trang

```
BÀI 8 — CHAOS ENGINEERING & TESTING (bài cuối)
─────────────────────────────────────────────────────────
BẪY  "CÓ cơ chế" ≠ "cơ chế CHẠY". Dự phòng hiếm chạy → hiếm test → hỏng âm
   thầm. Chưa test = niềm tin ẢO TƯỞNG (= fallback chưa test, aws-design B7).

LƯỢNG HOÁ NIỀM TIN  (SRE book) thay "tôi NGHĨ" bằng "tôi ĐÃ KIỂM". Test cả HỆ
   dưới lỗi, không chỉ unit test code. Mức test tỉ lệ yêu cầu tin cậy (SLO).

CHAOS / DiRT  (SREWB tr.193) tạo khẩn cấp CÓ KIỂM SOÁT (tiêm lỗi) để phát hiện
   chỗ hỏng TRƯỚC sự cố thật. (ẩn dụ: diễn tập chữa cháy / tiêm vaccine.)

DEMO  tin 5/5 cơ chế chạy; game day lộ chỉ 2/5 thật (backup/fallback/breaker
   là bom hẹn giờ). Tìm lỗi "2h chiều thứ Ba" thay vì "3h sáng Chủ nhật".

KHÉP KHOÁ  9 bài = vòng quanh ERROR BUDGET: SLO→observability→alert→toil→
   incident→postmortem→cascade→chaos. 4 TẦNG: cloud-base(vì sao)→aws-fund(cái
   gì)→aws-design(làm sao)→sre(GIỮ SỐNG). Trọn vòng đời.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Testing for Reliability**: "quantify confidence", lượng test tỉ lệ yêu cầu tin cậy. `tai_lieu/sre_testing-reliability.txt`.
- **The Site Reliability Workbook** — DiRT: tình huống khẩn cấp có kiểm soát (tr. 193). `tai_lieu/the-site-reliability-workbook-next18.pdf` (offset +32).
- Nối: [aws-design Bài 8 (DR/static stability)](../../aws-design/bai_hoc/bai_08_da-vung-dr.md), [Bài 7 (tránh fallback)](../../aws-design/bai_hoc/bai_07_chiu-tai-overload.md); [Bài 6 (postmortem)](bai_06_postmortem.md).
- **Hết khoá `sre`** — và hết bốn tầng cloud. Quay lại [Bài 0](bai_00_sre-la-gi-error-budget.md), hoặc chạy một game day thật trên Notes API capstone.

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · **[Bài 8 — Chaos & testing] ← bạn đang ở đây**

Xem thêm [README khoá học](../README.md).
