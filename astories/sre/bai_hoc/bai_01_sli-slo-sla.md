# Bài 1 — SLI, SLO, SLA: đo đúng và đặt mục tiêu

> [!info] Về bài này
> [Bài 0](bai_00_sre-la-gi-error-budget.md) nói error budget = `1 − SLO`. Nhưng **SLO lấy từ đâu**, và **đo bằng gì**? Bài này là bộ ba nền tảng: **SLI** (thước đo), **SLO** (mục tiêu), **SLA** (hợp đồng). Không có chúng, "hệ ổn không?" là câu hỏi không ai trả lời được bằng số — và không có số thì không có error budget, không có SRE.
> Nguồn: **SRE Book** — *Service Level Objectives*.
> **Trích:** `SRE: <chương>` → `tai_lieu/sre_*.txt`. **Demo:** Node 22.
> Nên đọc trước: [Bài 0](bai_00_sre-la-gi-error-budget.md).

## Mục lục

1. [Tình huống: "hệ ổn không?" không ai trả lời được](#1-tình-huống-hệ-ổn-không-không-ai-trả-lời-được)
2. [SLI: đo điều người dùng cảm nhận](#2-sli-đo-điều-người-dùng-cảm-nhận)
3. [SLO là mục tiêu, SLA là hợp đồng](#3-slo-là-mục-tiêu-sla-là-hợp-đồng)
4. [Demo: tính SLI, đối chiếu SLO](#4-demo-tính-sli-đối-chiếu-slo)
5. [Chọn SLO khôn ngoan](#5-chọn-slo-khôn-ngoan)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Tình huống: "hệ ổn không?" không ai trả lời được

> [!example] Sếp hỏi một câu đơn giản
> Sếp: *"Dịch vụ tháng này có ổn không?"*. Bạn mở dashboard: CPU 40%, RAM 60%, server **up 100%**. Bạn nói "ổn". Nhưng cùng lúc đó, 2% người dùng bị lỗi 500 khi thanh toán, và trang chủ load mất 8 giây ở giờ cao điểm. Server "up" mà người dùng *khổ sở*. "Ổn" theo ai? Bạn vừa đo **sai thứ** — đo thứ *dễ đo* (CPU, uptime máy) thay vì thứ *người dùng cảm nhận*.

Đây là cái bẫy số một của vận hành: *"up" của server ≠ "ổn" cho người dùng*. SRE sửa bằng cách định nghĩa chính xác **đo cái gì** (SLI), **mục tiêu bao nhiêu** (SLO), **cam kết gì** (SLA).

## 2. SLI: đo điều người dùng cảm nhận

> [!quote] SRE: service-level-objectives
> "An SLI is a service level indicator—a carefully defined quantitative measure of some aspect of the level of service that is provided."
>
> ***SLI** là một **service level indicator** — một **thước đo định lượng được định nghĩa cẩn thận** về một khía cạnh của mức dịch vụ được cung cấp.*

Mấu chốt nằm ở "khía cạnh của *mức dịch vụ*" — tức thứ *người dùng* quan tâm, không phải thứ *máy* báo. SLI điển hình: **tỉ lệ request thành công** (availability), **tỉ lệ request nhanh hơn X ms** (latency), **tỉ lệ dữ liệu đúng** (correctness). Không phải CPU%, không phải "server còn sống".

> [!example] Ẩn dụ: điểm hài lòng của nhà hàng
> Đo một nhà hàng *không* bằng "bếp chạy mấy %" hay "đèn còn sáng không" — mà bằng thứ *khách* cảm nhận: *món ra có nhanh không, đúng món không, ngon không*. SLI là vậy: đo từ góc **khách hàng**. Bếp (server) chạy 100% mà món ra sai/chậm thì nhà hàng vẫn **tệ**.

## 3. SLO là mục tiêu, SLA là hợp đồng

Có thước đo (SLI) rồi, đặt *mục tiêu* cho nó:

> [!quote] SRE: service-level-objectives
> "An SLO is a service level objective: a target value or range of values for a service level that is measured by an SLI."
>
> ***SLO** là một **service level objective**: một **giá trị (hoặc khoảng) mục tiêu** cho một mức dịch vụ được **đo bằng một SLI**.*

Ví dụ: SLI = "% request thành công", SLO = "≥ 99.9% trong 30 ngày". SLO là *lời hứa nội bộ* của đội. Khác với **SLA** — lời hứa *ra bên ngoài*, có răng:

> [!quote] SRE: service-level-objectives
> "SLAs are service level agreements: an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain."
>
> ***SLA** là **service level agreement**: một **hợp đồng** (minh thị hoặc ngầm) với người dùng, **kèm hậu quả** khi đạt (hoặc trượt) các SLO trong đó.*

Phân biệt sống còn: **SLA có *hậu quả*** (hoàn tiền, phạt hợp đồng) nếu trượt; **SLO không**. Quy tắc nhớ: SLO *nên chặt hơn* SLA — bạn muốn nội bộ báo động (trượt SLO) *trước khi* thật sự vi phạm cam kết với khách (trượt SLA). Thứ tự: **SLI đo → SLO đặt mục tiêu → SLA cam kết** (SLA thường chỉ có với khách hàng trả tiền; nhiều hệ chỉ cần SLI + SLO).

## 4. Demo: tính SLI, đối chiếu SLO

Từ một cửa sổ 1000 request (có status + độ trễ), tính hai SLI rồi so với SLO:

```typescript
// SLI = thước đo (vd % request thành công, % request nhanh hơn 300ms).
// SLO = mục tiêu cho SLI đó (vd ">= 99.9% thành công"). SLA = hợp đồng + hậu quả.
// Demo: từ một cửa sổ 1000 request, tính SLI rồi đối chiếu SLO.
type Req = { ok: boolean; ms: number };
// dựng 1000 request tất định: 4 lỗi (5xx), 40 request chậm (>300ms)
const reqs: Req[] = Array.from({ length: 1000 }, (_, i) => ({
  ok: i >= 4,                       // 4 request đầu là lỗi
  ms: i < 40 ? 500 : 120,           // 40 request đầu chậm 500ms, còn lại 120ms
}));

const total = reqs.length;
const availSLI = reqs.filter(r => r.ok).length / total * 100;        // % thành công
const latSLI = reqs.filter(r => r.ms < 300).length / total * 100;    // % nhanh hơn 300ms

const check = (name: string, sli: number, slo: number) => {
  const met = sli >= slo;
  console.log(`  ${name.padEnd(22)} SLI=${sli.toFixed(1)}%  | SLO ≥ ${slo}%  → ${met ? "ĐẠT" : "TRƯỢT"}`);
  return met;
};
console.log(`Cửa sổ ${total} request:`);
check("Availability (không lỗi)", availSLI, 99.9);
check("Latency (< 300ms)", latSLI, 95);

// error budget của availability: SLO 99.9% → cho phép 1 lỗi/1000; thực tế 4 lỗi
const allowedErr = Math.round(total * (1 - 99.9 / 100));   // 1000 × 0.1% = 1
const actualErr = total - reqs.filter(r => r.ok).length;
console.log(`\nError budget availability: cho phép ${allowedErr} lỗi, thực tế ${actualErr} lỗi`);
console.log(`  → đã tiêu ${(actualErr / allowedErr * 100).toFixed(0)}% budget (vượt ${actualErr > allowedErr ? "→ cần hành động" : ""})`);
console.log("\nSLI đo SỰ THẬT, SLO là mục tiêu, SLA là hợp đồng. Thiếu SLO = không biết");
console.log("'đủ tốt' là bao nhiêu → không biết khi nào nên lo, khi nào được ship.");
```

Kết quả chạy thật *(tất định)*:

```
Cửa sổ 1000 request:
  Availability (không lỗi) SLI=99.6%  | SLO ≥ 99.9%  → TRƯỢT
  Latency (< 300ms)      SLI=96.0%  | SLO ≥ 95%  → ĐẠT

Error budget availability: cho phép 1 lỗi, thực tế 4 lỗi
  → đã tiêu 400% budget (vượt → cần hành động)

SLI đo SỰ THẬT, SLO là mục tiêu, SLA là hợp đồng. Thiếu SLO = không biết
'đủ tốt' là bao nhiêu → không biết khi nào nên lo, khi nào được ship.
```

Giờ "hệ ổn không?" có câu trả lời *bằng số*: availability **trượt** (99.6% < 99.9%), latency **đạt** (96% > 95%). Và error budget cho thấy mức độ: cho phép 1 lỗi/1000, thực tế 4 → tiêu **400%** budget → cần hành động (đóng băng/điều tra, Bài 0). Không còn "ổn" cảm tính. Lưu ý: SLI đo từ *góc người dùng* (request thành công/nhanh), không phải CPU — nên nó bắt được đúng nỗi khổ của khách ở mục 1 mà dashboard "server up 100%" bỏ sót.

> [!note] Tự thử
> 1. Hạ SLO availability xuống `99.5%`: giờ nó ĐẠT. Vì sao "chọn SLO" quan trọng ngang "đo SLI"? (SLO quá lỏng = tự lừa mình; quá chặt = báo động giả).
> 2. Thêm SLI thứ ba "correctness" (% trả đúng dữ liệu): vì sao chỉ "không lỗi + nhanh" chưa đủ?
> 3. Tính SLI theo *thời gian* thay vì *request* (vd % phút trong đó tỉ lệ lỗi < 0.1%): hai cách đo cho con số khác nhau — vì sao phải định nghĩa SLI "cẩn thận" (như lời trích)?

## 5. Chọn SLO khôn ngoan

SLO là công cụ mạnh, nên dễ lạm dụng:

> [!quote] SRE: service-level-objectives
> "SLOs are a massive lever: use them wisely."
>
> *SLO là một **đòn bẩy cực mạnh: hãy dùng khôn ngoan**.*

Ba nguyên tắc thực chiến: **(1) Ít thôi** — chỉ vài SLO phản ánh đúng trải nghiệm cốt lõi; quá nhiều SLO thì không ai theo dõi nổi và chúng mâu thuẫn nhau. **(2) Theo *người dùng*, không theo hiện trạng** — đừng đặt SLO = "hiệu năng hiện tại" (tự khoá mình), mà = "mức khiến người dùng *đủ* hài lòng". **(3) Đừng đặt 100%** (Bài 0) — chừa error budget để còn đổi mới. Một SLO tốt là một *quyết định kinh doanh* ("khách rời đi nếu chậm hơn 1 giây") biến thành *con số kỹ thuật* ("95% request < 300ms"), và nó lái mọi việc sau: alert (Bài 3) bắn khi *sắp* trượt SLO, incident (Bài 5) ưu tiên theo mức tiêu budget.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — Vì sao "server up 100%" không trả lời được "hệ có ổn không"?
> **Đáp:** uptime máy là thứ *dễ đo*, không phải thứ *người dùng cảm nhận*. Server up mà 2% request lỗi / trang chậm 8s thì người dùng vẫn khổ. Phải đo từ góc người dùng (SLI).

> [!question] Thẻ 1.2 — SLI là gì? Cho 3 ví dụ (và 1 phản ví dụ)?
> **Đáp:** thước đo định lượng về mức dịch vụ *từ góc người dùng*. VD: % request thành công, % request < X ms, % dữ liệu đúng. Phản ví dụ: CPU%, "server còn sống".

> [!question] Thẻ 1.3 — SLO vs SLA khác nhau mấu chốt ở đâu?
> **Đáp:** SLO = mục tiêu *nội bộ* cho một SLI, **không hậu quả**. SLA = hợp đồng *với khách*, **có hậu quả** (hoàn tiền/phạt) khi trượt. SLO nên chặt hơn SLA.

> [!question] Thẻ 1.4 — Trong demo, "ổn không?" được trả lời thế nào?
> **Đáp:** bằng số: availability 99.6% < SLO 99.9% → TRƯỢT; latency 96% > 95% → ĐẠT; budget tiêu 400% → cần hành động. Hết "ổn" cảm tính.

> [!question] Thẻ 1.5 — Ba nguyên tắc chọn SLO khôn ngoan?
> **Đáp:** (1) ít thôi (vài cái cốt lõi); (2) theo *người dùng* không theo hiện trạng; (3) đừng 100% (chừa error budget). SLO = quyết định kinh doanh biến thành con số.

## 7. Câu hỏi tự kiểm tra

1. Vì sao đo CPU/uptime không trả lời được "hệ ổn không"? SLI sửa ra sao? *(mục 1–2)*
2. Định nghĩa SLI/SLO/SLA. Phân biệt bằng "hậu quả". Vì sao SLO chặt hơn SLA? *(mục 2–3)*
3. Chạy demo mục 4. Giải thích hai SLI + budget 400%. *(mục 4)*
4. Ba nguyên tắc chọn SLO. Vì sao "theo hiện trạng" là bẫy? *(mục 5)*
5. SLO lái những khái niệm SRE nào sau nó (alert, incident)? *(mục 5)*

## Tóm tắt một trang

```
BÀI 1 — SLI · SLO · SLA
─────────────────────────────────────────────────────────
BẪY  "server up 100%" ≠ "người dùng ổn". Đo thứ DỄ (CPU/uptime) thay vì thứ
   NGƯỜI DÙNG CẢM NHẬN.

SLI  thước đo định lượng mức dịch vụ TỪ GÓC NGƯỜI DÙNG (SRE book): % thành
   công, % < Xms, % đúng. KHÔNG phải CPU%. (ẩn dụ: điểm hài lòng nhà hàng.)
SLO  mục tiêu cho SLI (vd ≥99.9%), nội bộ, KHÔNG hậu quả.
SLA  hợp đồng với khách, CÓ hậu quả (hoàn tiền/phạt). SLO nên CHẶT HƠN SLA.

DEMO  1000 req: avail 99.6% < SLO 99.9% → TRƯỢT; latency 96% > 95% → ĐẠT.
   Budget avail: cho phép 1 lỗi, thực tế 4 → tiêu 400% → cần hành động.

CHỌN SLO KHÔN NGOAN  "SLOs are a massive lever" — (1) ÍT thôi; (2) theo NGƯỜI
   DÙNG không theo hiện trạng; (3) đừng 100% (chừa budget). SLO lái alert+incident.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Service Level Objectives**: định nghĩa SLI/SLO/SLA, "SLOs are a massive lever". `tai_lieu/sre_service-level-objectives.txt`.
- Nối: [Bài 0 (error budget)](bai_00_sre-la-gi-error-budget.md); đo thực tế: [aws-fund Bài 7 (CloudWatch metrics)](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md); latency nền: [cloud-base Bài 6](../../cloud-base/bai_hoc/bai_06_mang-hieu-nang.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · **[Bài 1 — SLI/SLO/SLA] ← bạn đang ở đây** · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
