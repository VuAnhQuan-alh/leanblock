# Bài 5 — Incident response và on-call

> [!info] Về bài này
> Alert (Bài 3) đánh thức bạn — rồi sao? Bài này là **ứng cứu sự cố có kỷ luật**: vì sao on-call phải *bền vững* (không dựa vào người hùng), cấu trúc **vai trò rõ** (Incident Commander / Ops Lead / Comms Lead), và nguyên tắc sống còn **"cầm máu trước, chữa gốc sau"** (mitigate before root-cause). Hỗn loạn lúc sự cố làm user khổ lâu gấp nhiều lần.
> Nguồn: **SRE Book** (*Being On-Call*) + **SREWB** (*Managing Incidents*).
> **Trích:** `SRE: <chương>` · `SREWB (tr. X)`. **Demo:** Node 22.
> Nên đọc trước: [Bài 3 (alerting)](bai_03_alerting.md).

## Mục lục

1. [Tình huống: 2 giờ sáng một mình giữa đám cháy](#1-tình-huống-2-giờ-sáng-một-mình-giữa-đám-cháy)
2. [On-call bền vững, không dựa người hùng](#2-on-call-bền-vững-không-dựa-người-hùng)
3. [Cấu trúc một sự cố: vai trò và cầm máu trước](#3-cấu-trúc-một-sự-cố-vai-trò-và-cầm-máu-trước)
4. [Demo: timeline sự cố, MTTA và MTTR](#4-demo-timeline-sự-cố-mtta-và-mttr)
5. [Thẻ ôn (active recall)](#5-thẻ-ôn-active-recall)
6. [Câu hỏi tự kiểm tra](#6-câu-hỏi-tự-kiểm-tra)
7. [Tóm tắt một trang](#tóm-tắt-một-trang)
8. [Nguồn](#nguồn)

---

## 1. Tình huống: 2 giờ sáng một mình giữa đám cháy

> [!example] Pager réo
> 2h sáng, pager réo: "error rate 15%". Bạn bật dậy, tim đập. Mở 5 tab, SSH vào 3 server, Slack hỏi loạn "ai biết gì không?". Hai đồng nghiệp khác cũng vừa thức dậy, *cả ba* cùng vào sửa — một người restart, một người rollback, một người đổi config, *giẫm chân nhau*, không ai biết người kia làm gì. 40 phút trôi qua trong hoảng loạn, và bạn vẫn đang *cố tìm nguyên nhân gốc* trong khi user vẫn lỗi. Đây là ứng cứu kiểu **người hùng + hỗn loạn** — và nó làm user khổ lâu gấp nhiều lần cần thiết.

SRE thay hoảng loạn bằng *quy trình*. Hai ý lớn: on-call phải *bền vững* (mục 2), và mỗi sự cố có *cấu trúc* (mục 3).

## 2. On-call bền vững, không dựa người hùng

Ứng cứu không phải tài năng cá nhân mà là *quy trình lặp lại được*:

> [!quote] SRE: being-on-call
> "Google SRE uses the protocol described in Managing Incidents, which offers an easy-to-follow and well-defined set of steps that aid an on-call engineer to rationally pursue a satisfactory incident resolution with all the required help."
>
> *Google SRE dùng một **protocol** (mô tả trong "Managing Incidents") — một bộ **bước rõ ràng, dễ theo** giúp kỹ sư on-call **xử lý sự cố một cách lý trí** với đầy đủ trợ giúp cần thiết.*

Và điều này phải *bằng được*: không được dựa vào anh hùng:

> [!quote] SREWB (tr. 180)
> "While the team valued the time and effort these individuals contributed over the weekend, successful incident management shouldn't rely on heroic efforts of individuals."
>
> *Dù đội trân trọng công sức của các cá nhân (thức cả cuối tuần), **ứng cứu sự cố thành công KHÔNG được dựa vào nỗ lực anh hùng của cá nhân**.*

Vì sao? Anh hùng *không scale*: người đó nghỉ phép, kiệt sức, hoặc rời công ty — kiến thức đi theo. Một hệ dựa vào "một người biết tuốt" là một hệ *mong manh*. SRE dựng *quy trình + tài liệu (runbook)* để *bất kỳ* người on-call nào cũng xử được, và on-call được giới hạn (số sự cố/ca, nghỉ bù) để không ai kiệt sức (nối luật 50% toil, Bài 4).

## 3. Cấu trúc một sự cố: vai trò và cầm máu trước

Khi sự cố lớn, điều chống hỗn loạn là **vai trò rõ ràng**:

> [!quote] SREWB (tr. 177)
> "The main roles in incident response are the Incident Commander (IC), Communications Lead (CL), and Operations or Ops Lead (OL)."
>
> *Ba vai trò chính khi ứng cứu: **Incident Commander (IC)** — chỉ huy/điều phối, **Communications Lead (CL)** — báo cáo bên ngoài, và **Operations/Ops Lead (OL)** — người *thực sự* thao tác lên hệ.*

> [!example] Ẩn dụ: phòng cấp cứu bệnh viện
> Bệnh nhân nguy kịch vào cấp cứu — không phải *một bác sĩ anh hùng* ôm hết. Có **bác sĩ trưởng điều phối** (IC: ai làm gì, quyết định), **y tá thao tác** (OL: tiêm, đặt ống), **người thông báo gia đình** (CL). Và họ **cầm máu + ổn định bệnh nhân TRƯỚC** (mitigate), rồi mới *chẩn đoán sâu nguyên nhân* (root cause) sau khi bệnh nhân qua cơn nguy.

Nguyên tắc sống còn thứ hai: **cầm máu trước, chữa gốc sau** (*mitigate before root-cause*). Khi user đang lỗi, mục tiêu số một là *làm user hết lỗi* — thường bằng **rollback** bản deploy gần nhất, hoặc chuyển traffic sang vùng khoẻ (aws-design Bài 8) — *kể cả khi chưa biết nguyên nhân*. Tìm nguyên nhân gốc là việc *quan trọng nhưng không khẩn*, làm *sau khi* đã cầm máu (và đào sâu ở postmortem, Bài 6). Demo mục 4 đo đúng khác biệt này.

## 4. Demo: timeline sự cố, MTTA và MTTR

Cùng một sự cố, hai kiểu ứng cứu. Đo **MTTA** (đến lúc nhận), **MTTM** (đến lúc *cầm máu* — user hết khổ), **MTTR** (đến lúc chữa gốc):

```typescript
// Incident response có CẤU TRÚC (vai trò rõ: IC/CL/OL) + mục tiêu "CẦM MÁU
// TRƯỚC, chữa gốc sau" (mitigate trước resolve). Đo bằng MTTA/MTTM/MTTR.
// So hai kiểu ứng cứu trên cùng một sự cố (phút kể từ lúc hỏng).
type Timeline = { detected: number; acked: number; mitigated: number; resolved: number };

function report(name: string, t: Timeline) {
  const mtta = t.acked - t.detected;        // nhận việc
  const mttm = t.mitigated - t.detected;    // cầm máu (user hết khổ)
  const mttr = t.resolved - t.detected;     // chữa gốc hoàn toàn
  console.log(`${name}`);
  console.log(`  MTTA (đến lúc nhận)      = ${mtta} phút`);
  console.log(`  MTTM (đến lúc CẦM MÁU)   = ${mttm} phút  ← user hết khổ ở đây`);
  console.log(`  MTTR (đến lúc chữa gốc)  = ${mttr} phút`);
  return mttm;
}
// HEROIC: 1 người ôm hết, dò gốc trước khi cầm máu, không ai điều phối
const heroic: Timeline =     { detected: 0, acked: 8, mitigated: 55, resolved: 60 };
// CÓ CẤU TRÚC: IC điều phối, rollback cầm máu NGAY (dù chưa biết gốc), chữa gốc sau
const structured: Timeline = { detected: 0, acked: 2, mitigated: 9,  resolved: 45 };

const h = report("KHÔNG cấu trúc (heroics, dò gốc trước):", heroic);
console.log();
const s = report("CÓ cấu trúc (IC/CL/OL, rollback cầm máu trước):", structured);
console.log(`\nUser khổ ${h} phút (heroic) vs ${s} phút (có cấu trúc) — nhanh hơn ${(h/s).toFixed(1)}x.`);
console.log("Mấu chốt: ROLLBACK cầm máu NGAY (user hết khổ) rồi mới thong thả tìm gốc.");
console.log("Vai trò rõ (IC điều phối, OL thao tác, CL báo cáo) → song song, không giẫm chân.");
```

Kết quả chạy thật *(tất định)*:

```
KHÔNG cấu trúc (heroics, dò gốc trước):
  MTTA (đến lúc nhận)      = 8 phút
  MTTM (đến lúc CẦM MÁU)   = 55 phút  ← user hết khổ ở đây
  MTTR (đến lúc chữa gốc)  = 60 phút

CÓ cấu trúc (IC/CL/OL, rollback cầm máu trước):
  MTTA (đến lúc nhận)      = 2 phút
  MTTM (đến lúc CẦM MÁU)   = 9 phút  ← user hết khổ ở đây
  MTTR (đến lúc chữa gốc)  = 45 phút

User khổ 55 phút (heroic) vs 9 phút (có cấu trúc) — nhanh hơn 6.1x.
Mấu chốt: ROLLBACK cầm máu NGAY (user hết khổ) rồi mới thong thả tìm gốc.
Vai trò rõ (IC điều phối, OL thao tác, CL báo cáo) → song song, không giẫm chân.
```

Con số đáng thấm: **user khổ 55 phút vs 9 phút** — nhanh hơn *6 lần*, dù *chữa gốc* (MTTR) chỉ nhanh hơn chút. Vì sao? Kiểu heroics *cố tìm nguyên nhân gốc trước khi làm gì* (55 phút user lỗi); kiểu có cấu trúc *rollback cầm máu ngay phút thứ 9* (user hết khổ) rồi *thong thả* tìm gốc tới phút 45. Thứ người dùng quan tâm là **MTTM** (bao lâu hết khổ), không phải MTTR. Và vai trò rõ (IC điều phối) khiến ba người *song song* thay vì giẫm chân. Lưu ý: "rollback cầm máu" đòi bạn *có thể* rollback nhanh — đó là release engineering (Bài 7 aws-fund CI/CD + canary).

> [!note] Tự thử
> 1. Trong kiểu heroics, nếu cầm máu (rollback) ở phút 9 *trước khi* biết gốc: MTTM giảm còn bao nhiêu? Vì sao "sửa đúng gốc" không phải mục tiêu *lúc đang cháy*?
> 2. Vì sao cần tách IC (điều phối) khỏi OL (thao tác)? Điều gì xảy ra nếu người đang gõ lệnh cũng phải trả lời sếp + điều phối cùng lúc?
> 3. Nối Bài 3: một alert tốt (burn rate) giảm MTTA ra sao? Nối Bài 6: cái gì xảy ra *sau khi* resolve?

## 5. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — Vì sao ứng cứu "không được dựa vào người hùng"?
> **Đáp:** anh hùng không scale: nghỉ phép/kiệt sức/nghỉ việc → kiến thức mất → hệ mong manh. Phải có **protocol + runbook** để bất kỳ ai on-call cũng xử được.

> [!question] Thẻ 5.2 — Ba vai trò chính khi ứng cứu sự cố?
> **Đáp:** **Incident Commander (IC)** điều phối/quyết định; **Ops Lead (OL)** thực sự thao tác lên hệ; **Communications Lead (CL)** báo cáo bên ngoài. Tách để không giẫm chân.

> [!question] Thẻ 5.3 — "Cầm máu trước, chữa gốc sau" nghĩa là gì?
> **Đáp:** khi user đang lỗi, ưu tiên số 1 là **làm user hết lỗi** (thường rollback / chuyển traffic) *kể cả chưa biết gốc*. Tìm nguyên nhân gốc là việc quan trọng nhưng *không khẩn* → làm sau.

> [!question] Thẻ 5.4 — MTTM vs MTTR: user quan tâm cái nào? Vì sao?
> **Đáp:** **MTTM** (đến lúc cầm máu, hết khổ) — đó là lúc user hết lỗi. MTTR (chữa gốc) quan trọng nhưng diễn ra *sau khi* user đã ổn.

> [!question] Thẻ 5.5 — Vì sao vai trò rõ làm ứng cứu nhanh hơn?
> **Đáp:** cho phép *song song* (OL thao tác trong khi CL báo cáo, IC điều phối) thay vì một người ôm hết / nhiều người giẫm chân.

## 6. Câu hỏi tự kiểm tra

1. Mô tả ứng cứu kiểu "người hùng + hỗn loạn". Vì sao nó làm user khổ lâu? *(mục 1)*
2. Vì sao không dựa heroics? Protocol + runbook giải quyết gì? *(mục 2, SRE book + SREWB)*
3. Ba vai trò IC/CL/OL. Vì sao tách chúng ra? *(mục 3, SREWB tr.177)*
4. "Cầm máu trước, chữa gốc sau". Chạy demo mục 4 và giải thích vì sao MTTM mới là thứ user quan tâm. *(mục 3–4)*
5. Alert tốt (Bài 3) + rollback nhanh (CI/CD) ảnh hưởng MTTA/MTTM ra sao? *(mục 4, Tự thử)*

## Tóm tắt một trang

```
BÀI 5 — INCIDENT RESPONSE & ON-CALL
─────────────────────────────────────────────────────────
TÌNH HUỐNG  2h sáng, 3 người cùng nhảy vào sửa, giẫm chân, cố tìm gốc → user
   khổ 55 phút. Heroics + hỗn loạn = chậm.

KHÔNG DỰA NGƯỜI HÙNG  (SREWB) anh hùng không scale (nghỉ/kiệt/nghỉ việc → mất
   kiến thức). Dùng PROTOCOL + runbook (SRE book) để BẤT KỲ ai on-call cũng xử.

VAI TRÒ RÕ  IC (điều phối) · OL (thao tác) · CL (báo cáo) (SREWB tr.177). Tách
   để song song, không giẫm chân. (ẩn dụ: phòng cấp cứu bệnh viện.)

CẦM MÁU TRƯỚC, CHỮA GỐC SAU  user đang lỗi → ROLLBACK/chuyển traffic NGAY (dù
   chưa biết gốc). Tìm gốc = quan trọng nhưng KHÔNG khẩn → sau (+ postmortem B6).

DEMO  user khổ: heroics 55ph vs có-cấu-trúc 9ph (6x). MTTM (hết khổ) mới là thứ
   user quan tâm, không phải MTTR (chữa gốc). Rollback nhanh = cần CI/CD.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Being On-Call**: protocol ứng cứu rõ ràng, dễ theo. `tai_lieu/sre_being-on-call.txt`.
- **The Site Reliability Workbook** — **Managing Incidents**: ba vai trò IC/CL/OL (tr. 177), không dựa heroics (tr. 180). `tai_lieu/the-site-reliability-workbook-next18.pdf` (offset +32).
- Nối: [Bài 3 (alert)](bai_03_alerting.md), [Bài 6 (postmortem)](bai_06_postmortem.md); rollback: [aws-fund Bài 6 (CI/CD)](../../aws-fund/bai_hoc/bai_06_cicd.md); chuyển traffic: [aws-design Bài 8 (DR)](../../aws-design/bai_hoc/bai_08_da-vung-dr.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · **[Bài 5 — Incident & on-call] ← bạn đang ở đây** · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
