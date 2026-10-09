# Bài 3 — Alerting: báo động đúng lúc, đúng mức

> [!info] Về bài này
> [Bài 2](bai_02_observability-golden-signals.md) cho bạn *nhìn thấy* hệ. Nhưng bạn không thể ngồi nhìn dashboard 24/7 — cần hệ *tự gọi* bạn khi có chuyện. Vấn đề: gọi **quá nhiều** (alert fatigue) còn tệ hơn không gọi. Bài này nắm triết lý alert của SRE: **mỗi lần gọi người đều đắt → alert phải khan hiếm, actionable, và theo *tốc độ tiêu error budget* (burn rate)**.
> Nguồn: **SRE Book** (*Monitoring*) + **SREWB** (*Alerting on SLOs*, burn rate).
> **Trích:** `SRE: <chương>` · `SREWB (tr. X)`. **Demo:** Node 22.
> Nên đọc trước: [Bài 1 (SLO/error budget)](bai_01_sli-slo-sla.md), [Bài 2 (golden signals)](bai_02_observability-golden-signals.md).

## Mục lục

1. [Tình huống: 200 báo động một đêm](#1-tình-huống-200-báo-động-một-đêm)
2. [Mỗi lần gọi người đều tốn](#2-mỗi-lần-gọi-người-đều-tốn)
3. [Alert theo triệu chứng và burn rate](#3-alert-theo-triệu-chứng-và-burn-rate)
4. [Demo: burn-rate alerting](#4-demo-burn-rate-alerting)
5. [Thẻ ôn (active recall)](#5-thẻ-ôn-active-recall)
6. [Câu hỏi tự kiểm tra](#6-câu-hỏi-tự-kiểm-tra)
7. [Tóm tắt một trang](#tóm-tắt-một-trang)
8. [Nguồn](#nguồn)

---

## 1. Tình huống: 200 báo động một đêm

> [!example] Chuông báo cháy kêu suốt
> Đội bạn cấu hình alert "cho chắc": CPU > 80%, disk > 70%, RAM > 85%, latency > 200ms ở *mọi* endpoint... Kết quả: điện thoại trực đêm réo **200 lần**, 199 lần là *vô hại* (CPU cao lúc batch chạy, disk đầy tạm rồi tự dọn). Sau một tuần, người trực **tắt thông báo** hoặc lướt qua không đọc. Rồi đêm nọ, một alert *thật* (database sắp hết connection) lọt giữa 200 cái nhiễu — không ai thấy. Hệ sập. Đây là **alert fatigue**: báo động quá nhiều *tệ hơn* không báo, vì nó huấn luyện con người *phớt lờ*.

Giống chuông báo cháy kêu mãi vì khói thuốc lá → cả nhà tháo pin → cháy thật không ai biết. Gốc của vấn đề: alert *mọi thứ bất thường* (nguyên nhân) thay vì *mọi thứ ảnh hưởng người dùng* (triệu chứng). SRE sửa bằng một nguyên tắc kinh tế đơn giản.

## 2. Mỗi lần gọi người đều tốn

> [!quote] SRE: monitoring-distributed-systems
> "Paging a human is a quite expensive use of an employee's time."
>
> *Gọi (page) một con người là một cách dùng **rất đắt** thời gian của nhân viên.*

Vì đắt, alert phải *hiếm* và *đáng*. Và cái giá còn gộp lại:

> [!quote] SRE: monitoring-distributed-systems
> "Every page that happens today distracts a human from improving the system for tomorrow, so there is often a case for taking a short-term hit to availability or performance in order to improve the long-term outlook for the system."
>
> *Mỗi page hôm nay **kéo một con người khỏi việc cải thiện hệ cho ngày mai** — nên nhiều khi đáng chịu một chút thiệt về availability/performance *ngắn hạn* để làm hệ *tốt lên dài hạn*.*

Hệ quả thực chiến: **một alert chỉ xứng đáng "page" (đánh thức người) khi nó (a) là triệu chứng người dùng cảm nhận — Bài 2, (b) khẩn (cần người *bây giờ*), và (c) *actionable* (có việc để làm).** Mọi thứ khác → ticket (xử lúc rảnh) hoặc chỉ ghi log. Nhưng làm sao biết một triệu chứng là "khẩn, cần người bây giờ" hay "từ từ"? Đo *tốc độ* nó ăn mòn error budget.

## 3. Alert theo triệu chứng và burn rate

> [!quote] SREWB (tr. 80)
> "Burn rate is how fast, relative to the SLO, the service consumes the error budget."
>
> ***Burn rate** (tốc độ cháy) là **dịch vụ tiêu error budget nhanh cỡ nào, so với SLO**.*

Burn rate = 1 nghĩa là budget bị tiêu *vừa đúng* để hết sau đúng cửa sổ (vd 30 ngày) — đúng kế hoạch, không sao. Burn rate cao (vd ×36) nghĩa budget 30 ngày sẽ *cháy sạch trong chưa đầy một giờ* → **page ngay**. Burn rate thấp (×2) nghĩa budget hết sau 15 ngày → vấn đề thật nhưng *từ từ* → **ticket**, xử trong giờ hành chính. Đây là chìa khoá chống alert fatigue: *cùng một triệu chứng* (có lỗi) sinh ra *hành động khác nhau* tuỳ **mức khẩn** (burn rate).

> [!example] Ẩn dụ: nhà cháy nhanh vs rò rỉ chậm
> Khói bốc *ào ạt* (burn cao) → gọi cứu hoả *ngay*, đánh thức cả nhà. Vòi nước *rỉ chậm* một giọt mỗi phút (burn thấp) → không gọi cứu hoả lúc 3 giờ sáng; ghi chú, gọi thợ *sáng mai*. Cả hai đều là "vấn đề", nhưng *mức khẩn* khác nhau quyết định *đánh thức ai, lúc nào*. Burn rate chính là "tốc độ khói bốc" của error budget.

Thực tế dùng **nhiều cửa sổ burn rate**: một cửa sổ ngắn (vd 1 giờ, burn cao) để bắt sự cố *đột ngột*, một cửa sổ dài (vd 6 giờ/3 ngày, burn vừa) để bắt sự cố *rỉ chậm kéo dài* — tránh cả bỏ sót lẫn báo động giả. Demo mục 4 cho thấy logic này bằng số.

## 4. Demo: burn-rate alerting

Cùng SLO 99.9%, ba tình huống error rate khác nhau → burn rate → quyết định page/ticket/im:

```typescript
// Alert theo TRIỆU CHỨNG + theo tốc độ TIÊU error budget (burn rate). Burn rate
// = tốc độ tiêu budget so với SLO. Burn=1 → tiêu vừa đủ hết đúng 30 ngày.
// Burn cao (cháy nhanh) → PAGE ngay; burn thấp (rỉ chậm) → ticket, xử sau.
const SLO = 99.9;                          // → ngân sách lỗi = 0.1%
const budgetErrRate = (100 - SLO) / 100;   // 0.001
const WINDOW_DAYS = 30;

function assess(label: string, actualErrRate: number) {
  const burn = actualErrRate / budgetErrRate;          // bội số so với "vừa đủ"
  const daysToExhaust = burn > 0 ? WINDOW_DAYS / burn : Infinity;
  let action: string;
  if (burn >= 14.4) action = "PAGE ngay (cháy rất nhanh — budget cạn trong 1-2 ngày)";
  else if (burn > 1) action = "Ticket (rỉ chậm — xử trong giờ làm việc)";
  else action = "Không alert (trong ngân sách)";
  console.log(`  ${label.padEnd(26)} lỗi ${(actualErrRate*100).toFixed(2)}% | burn ×${burn.toFixed(1)} | cạn sau ${daysToExhaust===Infinity?"∞":daysToExhaust.toFixed(1)+"d"} → ${action}`);
}
console.log(`SLO ${SLO}% → ngân sách lỗi ${(budgetErrRate*100).toFixed(1)}% trong ${WINDOW_DAYS} ngày:\n`);
assess("Bình thường", 0.0005);     // 0.05% lỗi
assess("Rỉ chậm", 0.002);          // 0.2% lỗi
assess("Sự cố lớn", 0.036);        // 3.6% lỗi
console.log("\nKHÔNG alert theo 'CPU cao' (nguyên nhân) mà theo TỐC ĐỘ TIÊU BUDGET");
console.log("(triệu chứng + mức khẩn). Cháy nhanh đánh thức người; rỉ chậm để giờ hành chính.");
```

Kết quả chạy thật *(tất định)*:

```
SLO 99.9% → ngân sách lỗi 0.1% trong 30 ngày:

  Bình thường                lỗi 0.05% | burn ×0.5 | cạn sau 60.0d → Không alert (trong ngân sách)
  Rỉ chậm                    lỗi 0.20% | burn ×2.0 | cạn sau 15.0d → Ticket (rỉ chậm — xử trong giờ làm việc)
  Sự cố lớn                  lỗi 3.60% | burn ×36.0 | cạn sau 0.8d → PAGE ngay (cháy rất nhanh — budget cạn trong 1-2 ngày)

KHÔNG alert theo 'CPU cao' (nguyên nhân) mà theo TỐC ĐỘ TIÊU BUDGET
(triệu chứng + mức khẩn). Cháy nhanh đánh thức người; rỉ chậm để giờ hành chính.
```

Ba dòng, ba hành động — tất cả suy ra từ **một con số burn rate**, không phải từ "CPU cao hay thấp". Lỗi 0.05% vẫn *trong ngân sách* (burn 0.5) → im lặng, không làm phiền ai. Lỗi 0.2% → budget cạn sau 15 ngày → ticket, xử ban ngày. Lỗi 3.6% → cạn sau 0.8 ngày → page ngay, đánh thức người. Để ý: alert *không* bắn theo "CPU #7 cao" (nguyên nhân, Bài 2) mà theo *tốc độ ăn mòn trải nghiệm người dùng* (triệu chứng + mức khẩn). Đây là lý do alert-dựa-SLO ít nhiễu hơn hẳn alert-dựa-ngưỡng-tài-nguyên: nó chỉ réo khi *thật sự* đáng.

> [!note] Tự thử
> 1. Hạ ngưỡng page xuống `burn >= 2`: giờ "rỉ chậm" cũng page. Vì sao đánh thức người lúc 3h sáng cho một sự cố "15 ngày nữa mới cạn budget" là lãng phí (và dẫn tới fatigue)?
> 2. Thêm cửa sổ ngắn 1h: một spike 10% lỗi *trong 5 phút* rồi hết — cửa sổ 30 ngày gần như không nhúc nhích, nhưng cửa sổ 1h bắt được. Vì sao cần *nhiều* cửa sổ?
> 3. Ánh xạ sang CloudWatch (aws-fund Bài 7): alarm trên *metric SLI* (tỉ lệ lỗi) thay vì trên *CPUUtilization* — vì sao đúng hơn?

## 5. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — "Alert fatigue" là gì? Vì sao báo quá nhiều tệ hơn không báo?
> **Đáp:** quá nhiều alert (phần lớn vô hại) huấn luyện người **phớt lờ** → alert *thật* lọt giữa nhiễu. Như chuông báo cháy kêu suốt → tháo pin.

> [!question] Thẻ 3.2 — Vì sao "mỗi page đều đắt"? Hệ quả cho tiêu chí page?
> **Đáp:** page tốn thời gian + kéo người khỏi việc cải thiện hệ. → chỉ page khi: (a) triệu chứng user cảm nhận, (b) khẩn, (c) actionable. Còn lại → ticket/log.

> [!question] Thẻ 3.3 — Burn rate là gì? Burn = 1 nghĩa gì?
> **Đáp:** tốc độ tiêu error budget so với SLO. Burn=1 = tiêu vừa đủ hết đúng cửa sổ (đúng kế hoạch). Cao = cháy nhanh; thấp = rỉ chậm.

> [!question] Thẻ 3.4 — Cùng triệu chứng "có lỗi", vì sao hành động khác nhau?
> **Đáp:** tuỳ **mức khẩn = burn rate**. Burn cao (budget cạn trong giờ) → page ngay; burn thấp (cạn sau tuần) → ticket ban ngày.

> [!question] Thẻ 3.5 — Vì sao alert-dựa-SLO ít nhiễu hơn alert-dựa-ngưỡng-tài-nguyên?
> **Đáp:** nó réo theo *ảnh hưởng người dùng thật* (burn error budget), không theo "CPU/disk cao" (nguyên nhân thường vô hại).

## 6. Câu hỏi tự kiểm tra

1. Mô tả alert fatigue. Nó bắt nguồn từ việc alert theo gì (nguyên nhân hay triệu chứng)? *(mục 1)*
2. Vì sao "mỗi page đắt"? Ba tiêu chí để một alert xứng đáng page? *(mục 2, SRE book)*
3. Burn rate là gì (SREWB)? Burn=1, ×2, ×36 mỗi cái nghĩa gì? *(mục 3–4)*
4. Chạy demo mục 4. Vì sao cùng "có lỗi" mà ba hành động khác nhau? *(mục 4)*
5. Vì sao cần *nhiều cửa sổ* burn rate? *(mục 3, Tự thử)*

## Tóm tắt một trang

```
BÀI 3 — ALERTING
─────────────────────────────────────────────────────────
ALERT FATIGUE  báo quá nhiều (phần lớn vô hại) → người PHỚT LỜ → alert thật
   lọt. Tệ hơn không báo. Gốc: alert theo NGUYÊN NHÂN (CPU/disk) không theo
   triệu chứng. (chuông cháy kêu suốt → tháo pin.)

MỖI PAGE ĐẮT  (SRE book) tốn người + kéo khỏi việc cải thiện hệ. → page CHỈ
   khi: triệu chứng user cảm nhận + KHẨN + ACTIONABLE. Còn lại → ticket/log.

BURN RATE  (SREWB tr.80) tốc độ tiêu error budget so với SLO. Burn=1 → hết
   đúng cửa sổ. Cao → cháy nhanh → PAGE; thấp → rỉ chậm → TICKET. Cùng triệu
   chứng, hành động khác theo MỨC KHẨN. (nhà cháy nhanh vs vòi rỉ chậm.)

DEMO  SLO 99.9%: lỗi 0.05%→burn 0.5 (im); 0.2%→×2 cạn 15d (ticket); 3.6%→×36
   cạn 0.8d (PAGE). Dùng NHIỀU cửa sổ (1h bắt spike, 30d bắt rỉ chậm).

→ alert trên METRIC SLI, không trên CPUUtilization (aws-fund Bài 7).
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Monitoring Distributed Systems**: paging đắt, mỗi page kéo người khỏi cải thiện hệ. `tai_lieu/sre_monitoring-distributed-systems.txt`.
- **The Site Reliability Workbook** — **Alerting on SLOs**: định nghĩa burn rate (tr. 80). `tai_lieu/the-site-reliability-workbook-next18.pdf` (offset +32).
- Nối: [Bài 1 (error budget)](bai_01_sli-slo-sla.md), [Bài 2 (symptoms)](bai_02_observability-golden-signals.md); công cụ: [aws-fund Bài 7 (CloudWatch alarm)](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · **[Bài 3 — Alerting] ← bạn đang ở đây** · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
