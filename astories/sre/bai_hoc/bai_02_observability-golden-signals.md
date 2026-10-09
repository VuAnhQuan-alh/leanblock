# Bài 2 — Observability và bốn golden signals

> [!info] Về bài này
> [Bài 1](bai_01_sli-slo-sla.md) đặt SLO. Nhưng để *biết* có đạt SLO không — và khi hỏng thì *vì sao* — ta phải **nhìn thấy** hệ: observability. Bài này nắm cái tối thiểu đúng: **bốn golden signals** (latency, traffic, errors, saturation), nguyên tắc **đo triệu chứng không đo nguyên nhân**, và ba cách nhìn **metrics/logs/traces**.
> Nguồn: **SRE Book** — *Monitoring Distributed Systems*.
> **Trích:** `SRE: <chương>`. **Demo:** Node 22.
> Nên đọc trước: [Bài 1 (SLI/SLO)](bai_01_sli-slo-sla.md), [aws-fund Bài 7 (CloudWatch)](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md).

## Mục lục

1. [Tình huống: trăm dashboard, không câu trả lời](#1-tình-huống-trăm-dashboard-không-câu-trả-lời)
2. [Observability: cái gì hỏng, và vì sao](#2-observability-cái-gì-hỏng-và-vì-sao)
3. [Bốn golden signals](#3-bốn-golden-signals)
4. [Demo: tính bốn golden signals](#4-demo-tính-bốn-golden-signals)
5. [Metrics, logs, traces: ba cách nhìn](#5-metrics-logs-traces-ba-cách-nhìn)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Tình huống: trăm dashboard, không câu trả lời

> [!example] 50 biểu đồ, 0 câu trả lời
> Hệ của bạn có một dashboard khổng lồ: CPU từng máy, RAM, disk I/O, số thread, cache hit, hàng chục biểu đồ. Rồi người dùng than "app chậm". Bạn nhìn 50 biểu đồ... *cái nào* cho biết "user có đang khổ không"? CPU 40% — tốt hay xấu? Không biết, vì không biết nó *liên quan gì* tới trải nghiệm. Bạn ngập trong dữ liệu mà **mù thông tin**. Nhiều biểu đồ không bằng *đúng* vài biểu đồ.

SRE đảo ngược cách tiếp cận: thay vì "đo mọi thứ đo được", hỏi *"người dùng cảm nhận qua đâu?"* và đo đúng vài thứ đó. Hoá ra **bốn** signal là đủ phủ phần lớn (mục 3).

## 2. Observability: cái gì hỏng, và vì sao

Monitoring tốt phải trả lời *hai* câu ở hai tầng khác nhau:

> [!quote] SRE: monitoring-distributed-systems
> "The "what's broken" indicates the symptom; the "why" indicates a (possibly intermediate) cause."
>
> *"**Cái gì hỏng**" chỉ ra **triệu chứng (symptom)**; "**vì sao**" chỉ ra một **nguyên nhân (cause)** (có thể là nguyên nhân trung gian).*

Phân biệt này định hình mọi thứ: bạn **báo động (alert) theo triệu chứng** — thứ *người dùng cảm nhận* ("10% request lỗi") — chứ không theo nguyên nhân ("CPU máy #7 cao"). Vì sao? Vì triệu chứng là thứ *thực sự* đáng đánh thức người lúc 3 giờ sáng, còn nguyên nhân có vô số (CPU cao có thể vô hại). Nguyên nhân để *điều tra sau khi* đã biết có triệu chứng. (Bài 3 đào sâu alerting.) Golden signals chính là bộ triệu chứng tối thiểu.

## 3. Bốn golden signals

> [!quote] SRE: monitoring-distributed-systems
> "The four golden signals of monitoring are latency, traffic, errors, and saturation."
>
> *Bốn **golden signal** của monitoring là: **độ trễ (latency), lưu lượng (traffic), lỗi (errors), và bão hoà (saturation)**.*

- **Latency** — request mất bao lâu (nhìn *p99*, không chỉ trung bình — mục 4).
- **Traffic** — có bao nhiêu nhu cầu (req/s).
- **Errors** — tỉ lệ request thất bại.
- **Saturation** — hệ "đầy" cỡ nào so với công suất (RAM/CPU/connection sắp cạn chưa).

Và lời hứa:

> [!quote] SRE: monitoring-distributed-systems
> "If you measure all four golden signals and page a human when one signal is problematic (or, in the case of saturation, nearly problematic), your service will be at least decently covered by monitoring."
>
> *Nếu bạn đo **cả bốn** golden signal và **gọi người** khi một signal có vấn đề (riêng saturation thì khi *sắp* có vấn đề), dịch vụ của bạn **được phủ sóng monitoring kha khá**.*

> [!example] Ẩn dụ: bốn đồng hồ trên táp-lô ô tô
> Xe hơi không bắt bạn nhìn 50 cảm biến — chỉ **bốn đồng hồ** là đủ lái an toàn: *đồng hồ tốc độ* (traffic — đang chạy nhanh/nhiều cỡ nào), *đèn check-engine* (errors — có gì hỏng), *kim nhiệt độ máy* (saturation — sắp quá nhiệt chưa), *độ nhạy phản hồi vô-lăng/phanh* (latency — bấm có ăn ngay không). Bốn cái đó kể gần hết "xe ổn không". Thêm 50 cảm biến chi tiết chỉ để *thợ sửa* dùng *sau khi* một đồng hồ báo động.

## 4. Demo: tính bốn golden signals

Từ một cửa sổ 60 giây (600 request), tính cả bốn — và thấy vì sao cần *cả bốn* + vì sao nhìn *p99*:

```typescript
// 4 GOLDEN SIGNALS (SRE book): Latency, Traffic, Errors, Saturation. Đo cả 4 là
// "phủ sóng kha khá" một dịch vụ. Demo: tính cả 4 từ một cửa sổ request.
type Req = { ms: number; ok: boolean };
// 600 request trong 60 giây (10 req/s), 6 lỗi, đuôi latency dài
const reqs: Req[] = Array.from({ length: 600 }, (_, i) => ({
  ms: i < 30 ? 800 : 90 + (i % 40),      // 30 request đuôi chậm 800ms
  ok: i % 100 !== 0,                      // 6 lỗi (i = 0,100,200,...500)
}));
const WINDOW_SEC = 60, CAPACITY = 15;     // công suất 15 req/s

const sorted = [...reqs].map(r => r.ms).sort((a, b) => a - b);
const pct = (p: number) => sorted[Math.floor(sorted.length * p / 100)];
const traffic = reqs.length / WINDOW_SEC;
const errors = reqs.filter(r => !r.ok).length / reqs.length * 100;
const saturation = traffic / CAPACITY * 100;

console.log("4 GOLDEN SIGNALS (cửa sổ 60s):");
console.log(`  1. LATENCY     p50=${pct(50)}ms  p99=${pct(99)}ms  ← đuôi p99 cao = một số user khổ`);
console.log(`  2. TRAFFIC     ${traffic.toFixed(1)} req/s`);
console.log(`  3. ERRORS      ${errors.toFixed(1)}%`);
console.log(`  4. SATURATION  ${saturation.toFixed(0)}% công suất (${traffic}/${CAPACITY} req/s)`);
console.log("\nVì sao cần CẢ 4: traffic+errors+latency 'bình thường' nhưng saturation 67%");
console.log("→ sắp chạm trần, một spike nhỏ nữa là sập. Một signal không kể hết câu chuyện.");
console.log("Nhìn p99 (không chỉ p50): trung bình đẹp vẫn che giấu đuôi dài hành hạ số ít user.");
```

Kết quả chạy thật *(tất định)*:

```
4 GOLDEN SIGNALS (cửa sổ 60s):
  1. LATENCY     p50=111ms  p99=800ms  ← đuôi p99 cao = một số user khổ
  2. TRAFFIC     10.0 req/s
  3. ERRORS      1.0%
  4. SATURATION  67% công suất (10/15 req/s)

Vì sao cần CẢ 4: traffic+errors+latency 'bình thường' nhưng saturation 67%
→ sắp chạm trần, một spike nhỏ nữa là sập. Một signal không kể hết câu chuyện.
Nhìn p99 (không chỉ p50): trung bình đẹp vẫn che giấu đuôi dài hành hạ số ít user.
```

Hai bài học sờ được. **(1) Cần cả bốn:** latency/traffic/errors trông ổn, nhưng *saturation 67%* cảnh báo hệ sắp chạm trần — một spike nhỏ nữa là sập. Nhìn thiếu một signal là mù một nửa câu chuyện. **(2) Nhìn p99, không chỉ p50:** p50=111ms (đẹp!) nhưng p99=800ms — tức *1% người dùng* đợi 800ms. "Trung bình" che giấu cái đuôi hành hạ số ít — mà số ít đó vẫn là người thật, và thường là khách hàng giá trị (giỏ hàng to = nhiều dữ liệu = chậm). SLO latency (Bài 1) vì thế luôn đặt theo *percentile*, không theo trung bình.

> [!note] Tự thử
> 1. Tăng `CAPACITY` lên 50: saturation còn 20%. Vì sao saturation là signal *duy nhất* nên báo khi "**sắp** có vấn đề" chứ không đợi "đã có vấn đề"? (gợi ý: hết công suất thì đã muộn.)
> 2. Thêm đuôi dài hơn (100 request 2000ms): p50 gần như không đổi, p99 vọt. Vì sao SLO/alert theo p50 là nguy hiểm?
> 3. Ánh xạ 4 signal vào SLI của Bài 1: cái nào thành SLI availability, cái nào thành SLI latency?

## 5. Metrics, logs, traces: ba cách nhìn

Bốn golden signals *đo bằng* công cụ gì? Ba "trụ" observability, mỗi cái trả lời một kiểu câu hỏi:

| Trụ | Là gì | Trả lời | AWS |
| :-- | :-- | :-- | :-- |
| **Metrics** | con số theo thời gian (golden signals) | "có vấn đề không, lúc nào" | CloudWatch Metrics |
| **Logs** | sự kiện rời rạc có cấu trúc | "sự cố *là gì*, request nào" | CloudWatch Logs Insights |
| **Traces** | đường đi một request qua nhiều service | "chậm/hỏng *ở đâu* trong chuỗi" | X-Ray / OpenTelemetry |

Luồng điều tra điển hình: **metric** (golden signal) báo "errors tăng" → **log** (Bài aws-fund 10) cho biết "lỗi gì, request nào" → **trace** chỉ ra "nghẽn ở service thanh toán". Metric phát hiện, log + trace chẩn đoán. Đây là lý do bạn cần cả ba — và vì sao structured logging (aws-fund Bài 10) + distributed tracing là đầu tư nền của vận hành. (Alert bắn từ *metric* theo triệu chứng là Bài 3.)

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 2.1 — Vì sao "nhiều dashboard" không bằng "đúng vài signal"?
> **Đáp:** đo mọi thứ *đo được* (CPU/RAM...) khiến ngập dữ liệu mà không biết cái nào liên quan trải nghiệm người dùng. Phải đo thứ *người dùng cảm nhận*.

> [!question] Thẻ 2.2 — Symptom vs cause: alert nên theo cái nào? Vì sao?
> **Đáp:** alert theo **triệu chứng** (user cảm nhận, vd "10% lỗi") — thứ thật sự đáng đánh thức người. Nguyên nhân (CPU cao...) có vô số và thường vô hại; để điều tra *sau*.

> [!question] Thẻ 2.3 — Bốn golden signals? Cái nào báo khi "sắp" hỏng?
> **Đáp:** Latency, Traffic, Errors, Saturation. **Saturation** báo khi *sắp* chạm trần (vì hết công suất thì đã muộn).

> [!question] Thẻ 2.4 — Vì sao nhìn p99 chứ không chỉ p50/trung bình?
> **Đáp:** trung bình/p50 che giấu đuôi dài — p99 cao nghĩa 1% user khổ (thường là khách giá trị, dữ liệu to). SLO latency đặt theo percentile.

> [!question] Thẻ 2.5 — Metrics/logs/traces mỗi cái trả lời gì?
> **Đáp:** metrics = "có vấn đề không, lúc nào" (phát hiện); logs = "sự cố là gì, request nào"; traces = "chậm/hỏng ở đâu trong chuỗi" (chẩn đoán).

## 7. Câu hỏi tự kiểm tra

1. Vì sao "50 dashboard CPU/RAM" không trả lời "user có khổ không"? *(mục 1)*
2. Symptom vs cause. Alert theo cái nào và vì sao? *(mục 2, SRE book)*
3. Kể 4 golden signals + ý nghĩa. Cái nào đặc biệt (báo sớm)? *(mục 3)*
4. Chạy demo mục 4. Vì sao cần cả 4? Vì sao p99 không p50? *(mục 4)*
5. Metrics/logs/traces: luồng điều tra một sự cố errors-tăng. *(mục 5)*

## Tóm tắt một trang

```
BÀI 2 — OBSERVABILITY & 4 GOLDEN SIGNALS
─────────────────────────────────────────────────────────
BẪY  trăm dashboard CPU/RAM = ngập DỮ LIỆU, mù THÔNG TIN. Đo thứ user cảm nhận.

SYMPTOM vs CAUSE  "cái gì hỏng"=triệu chứng; "vì sao"=nguyên nhân (SRE book).
   ALERT theo TRIỆU CHỨNG (user cảm nhận), không theo nguyên nhân (vô số, vô hại).

4 GOLDEN SIGNALS  Latency · Traffic · Errors · Saturation. Đo cả 4 = phủ sóng
   kha khá. SATURATION báo khi SẮP hỏng (hết công suất là muộn). (ẩn dụ: 4 đồng
   hồ táp-lô ô tô.)

p99 KHÔNG p50  trung bình che đuôi dài. p50=111ms đẹp mà p99=800ms = 1% user
   khổ. SLO latency đặt theo PERCENTILE.

3 TRỤ  metrics (phát hiện: có vấn đề không) → logs (là gì, request nào) →
   traces (ở đâu trong chuỗi). CloudWatch Metrics/Logs Insights/X-Ray.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Monitoring Distributed Systems**: four golden signals, symptom vs cause, "decently covered". `tai_lieu/sre_monitoring-distributed-systems.txt`.
- Nối: [Bài 1 (SLI/SLO)](bai_01_sli-slo-sla.md), [Bài 3 (alerting)](bai_03_alerting.md); công cụ: [aws-fund Bài 7 (CloudWatch metrics)](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md), [Bài 10 (Logs Insights)](../../aws-fund/bai_hoc/bai_10_logs-insights.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · **[Bài 2 — Observability & golden signals] ← bạn đang ở đây** · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
