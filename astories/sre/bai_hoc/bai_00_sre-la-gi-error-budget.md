# Bài 0 — SRE là gì, và error budget

> [!info] Về khoá này
> Khoá **`sre`** là **mắt xích cuối** của mạch cloud: sau khi *hiểu* ([`cloud-base`](../../cloud-base/README.md)), *biết dịch vụ* ([`aws-fund`](../../aws-fund/README.md)), và *thiết kế* ([`aws-design`](../../aws-design/README.md)), giờ là **vận hành cho đáng tin trong production** — Site Reliability Engineering. Tổ chức **theo khái niệm SRE**, xây dần: error budget → SLI/SLO → observability → alerting → toil → incident → postmortem → quá tải → chaos.
> Nguồn (Luật số 1): **SRE Book** — Google *Site Reliability Engineering* (bản online `sre.google`, lưu `tai_lieu/sre_*.txt`, trích `SRE: <chương>`) + **SREWB** — *The Site Reliability Workbook* (PDF `tai_lieu/`, trích `SREWB (tr. X)`, PDF = tr. + 32).
> **Chạy demo:** **Node 22+** chạy thẳng `.ts`; lab vận hành nơi chạy được dùng công cụ thật/LocalStack.
> Nên đọc trước: [aws-design Bài 8 (DR/reliability)](../../aws-design/bai_hoc/bai_08_da-vung-dr.md).

## Mục lục

1. [Tình huống: dev muốn ship, ops muốn ổn](#1-tình-huống-dev-muốn-ship-ops-muốn-ổn)
2. [Độ tin cậy là một tính năng có đánh đổi](#2-độ-tin-cậy-là-một-tính-năng-có-đánh-đổi)
3. [Error budget: biến tranh cãi thành con số](#3-error-budget-biến-tranh-cãi-thành-con-số)
4. [Demo: máy tính error budget](#4-demo-máy-tính-error-budget)
5. [Bản đồ khoá SRE](#5-bản-đồ-khoá-sre)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Tình huống: dev muốn ship, ops muốn ổn

> [!example] Cuộc chiến bất tận trong mọi công ty
> Đội **phát triển (dev)** được thưởng theo *tính năng mới ship nhanh* — họ muốn deploy mỗi ngày. Đội **vận hành (ops)** bị gọi dậy lúc 3 giờ sáng khi hệ sập — họ muốn *đừng đổi gì cả*. Hai bên kéo co vô tận: dev bảo "ops cản trở", ops bảo "dev làm ẩu". Mỗi lần sự cố là một cuộc họp đổ lỗi. Nghe quen chứ? SRE của Google sinh ra để *chấm dứt* cuộc chiến này — không bằng cách chọn phe, mà bằng một **con số** mà cả hai cùng đồng ý.

Câu hỏi gốc: *"Hệ nên đáng tin cỡ nào?"*. Trực giác bảo "càng đáng tin càng tốt, nhắm 100%". Trực giác đó **sai** — và nhận ra vì sao là nền của toàn bộ SRE.

## 2. Độ tin cậy là một tính năng có đánh đổi

Nhắm 100% nghe hiển nhiên đúng, nhưng:

> [!quote] SRE: embracing-risk
> "Extreme reliability comes at a cost: maximizing stability limits how fast new features can be developed and how quickly products can be delivered to users, and dramatically increases their cost, which in turn reduces the numbers of features a team can afford to offer."
>
> *Độ tin cậy cực cao **có giá của nó**: tối đa hoá ổn định **giới hạn tốc độ ra tính năng mới** và giao sản phẩm tới người dùng, **tăng mạnh chi phí**, kéo theo *giảm* số tính năng đội có thể cung cấp.*

Nói cách khác, **độ tin cậy là một tính năng** — và như mọi tính năng, nó đánh đổi với những tính năng khác (và với tiền, với tốc độ). Thêm một "số 9" (99.9% → 99.99%) tốn gấp nhiều lần công sức, có khi người dùng *chẳng nhận ra* (vì mạng/điện thoại của họ còn kém tin cậy hơn thế). Vậy mục tiêu đúng không phải "100%" mà là *"đủ tin cậy cho người dùng hài lòng, không hơn"* — và phần "không hơn" đó, phần **được phép hỏng**, chính là thứ ta quản lý. Nó có tên: error budget.

## 3. Error budget: biến tranh cãi thành con số

> [!quote] SRE: embracing-risk
> "The error budget provides a clear, objective metric that determines how unreliable the service is allowed to be within a single quarter."
>
> ***Error budget** cung cấp một **thước đo rõ ràng, khách quan** xác định dịch vụ **được phép kém tin cậy tới mức nào** trong một quý.*

Cơ chế: nếu mục tiêu (SLO) là 99.9% thành công, thì 0.1% còn lại là **ngân sách được phép hỏng**. Mọi lỗi (deploy hỏng, sự cố, thí nghiệm rủi ro) *tiêu* vào ngân sách đó. Còn budget → dev **thoải mái ship nhanh, thử nghiệm**. Cạn budget → **đóng băng tính năng**, cả đội tập trung vào ổn định cho tới khi budget hồi lại. Thiên tài của ý tưởng:

> [!quote] SRE: embracing-risk
> "The main benefit of an error budget is that it provides a common incentive that allows both product development and SRE to focus on finding the right balance between innovation and reliability."
>
> *Lợi ích chính của error budget là tạo một **động cơ chung** cho *cả* dev *lẫn* SRE cùng tìm **cân bằng đúng giữa đổi mới và độ tin cậy**.*

> [!example] Ẩn dụ: ngân sách tiêu xài hàng tháng
> Error budget như *tiền tiêu vặt mỗi tháng*. Bạn có 100 "đồng rủi ro". Mỗi lần deploy mạo hiểm, mỗi sự cố "tiêu" một ít. Còn tiền → cứ chơi, thử cái mới. Hết tiền → thắt lưng buộc bụng tới đầu tháng sau (budget reset mỗi quý). Không ai cãi nhau "nên tiêu hay không" — cứ **nhìn số dư**. Dev và ops không còn là hai phe, mà cùng nhìn *một* bảng ngân sách.

Error budget chấm dứt cuộc chiến ở mục 1 vì nó biến câu hỏi cảm tính ("nhanh hay ổn?") thành câu hỏi số học ("còn bao nhiêu budget?"). Demo mục 4 cho thấy con số đó tính ra sao.

## 4. Demo: máy tính error budget

Từ SLO → thời gian downtime cho phép, và → số request được phép lỗi; rồi xem một sự cố tiêu bao nhiêu % budget (quyết định ship hay đóng băng):

```typescript
// SRE: 100% reliability là mục tiêu SAI (đắt + chặn đổi mới). Chọn một SLO
// (vd 99.9%), phần "được phép hỏng" = ERROR BUDGET. Budget còn → thoải mái
// ship tính năng rủi ro; budget cạn → đóng băng, tập trung ổn định.
const MINUTES_PER_MONTH = 30 * 24 * 60;        // 43200
function downtimeMin(slo: number): number { return MINUTES_PER_MONTH * (1 - slo / 100); }

console.log("SLO     | downtime cho phép / tháng | / năm");
console.log("--------+---------------------------+-----------");
for (const slo of [99, 99.9, 99.95, 99.99]) {
  const m = downtimeMin(slo);
  console.log(`${slo.toString().padEnd(7)} | ${(m.toFixed(0)+" phút").padEnd(25)} | ${(m*12/60).toFixed(1)} giờ`);
}

// Error budget theo REQUEST: SLO 99.9% trên 100 triệu request/tháng
const SLO = 99.9, REQS = 100_000_000;
const budget = REQS * (1 - SLO / 100);          // số request được phép lỗi
console.log(`\nSLO ${SLO}% trên ${(REQS/1e6)}M request/tháng:`);
console.log(`  error budget = ${budget.toLocaleString("en")} request được phép lỗi`);

// Một sự cố làm lỗi 120k request → tiêu bao nhiêu % budget?
for (const failed of [20_000, 120_000]) {
  const used = failed / budget * 100;
  const decision = used < 100 ? `còn ${(100-used).toFixed(0)}% → được ship tính năng rủi ro` : "CẠN → đóng băng, chỉ sửa ổn định";
  console.log(`  sự cố lỗi ${failed.toLocaleString("en")} req → tiêu ${used.toFixed(0)}% budget (${decision})`);
}
console.log("\nError budget = ngân sách 'được phép hỏng' chung cho cả dev lẫn SRE,");
console.log("biến tranh cãi 'nhanh vs ổn' thành một CON SỐ khách quan.");
```

Kết quả chạy thật *(tất định)*:

```
SLO     | downtime cho phép / tháng | / năm
--------+---------------------------+-----------
99      | 432 phút                  | 86.4 giờ
99.9    | 43 phút                   | 8.6 giờ
99.95   | 22 phút                   | 4.3 giờ
99.99   | 4 phút                    | 0.9 giờ

SLO 99.9% trên 100M request/tháng:
  error budget = 100,000 request được phép lỗi
  sự cố lỗi 20,000 req → tiêu 20% budget (còn 80% → được ship tính năng rủi ro)
  sự cố lỗi 120,000 req → tiêu 120% budget (CẠN → đóng băng, chỉ sửa ổn định)

Error budget = ngân sách 'được phép hỏng' chung cho cả dev lẫn SRE,
biến tranh cãi 'nhanh vs ổn' thành một CON SỐ khách quan.
```

Hai điều đáng thấm. **(1) Mỗi "số 9" đắt theo cấp:** từ 99% xuống 99.99% là từ *432 phút* downtime/tháng xuống *4 phút* — khác biệt khổng lồ về công sức. Chọn SLO là chọn bạn *trả* bao nhiêu cho độ tin cậy. **(2) Budget biến quyết định thành số học:** sự cố tiêu 20% budget → còn dư, dev cứ ship; tiêu 120% → vượt, đóng băng. Không họp đổ lỗi, chỉ nhìn số dư. Đây là lý do error budget là *viên gạch nền* của SRE — mọi khái niệm sau (SLO, alerting, incident...) đều phục vụ việc *đo* và *bảo vệ* ngân sách này.

> [!note] Tự thử
> 1. Đổi SLO thành `99.999%` ("5 số 9"): downtime/tháng còn bao nhiêu? Vì sao gần như không hệ web nào cần tới mức này (gợi ý: mạng người dùng còn kém tin cậy hơn)?
> 2. Đổi `REQS` còn 1M/tháng: cùng SLO 99.9% nhưng budget tuyệt đối nhỏ hơn — một sự cố tiêu % budget lớn hơn. Vì sao hệ ít traffic "mong manh" hơn về budget?
> 3. Nghĩ: nếu budget *chưa tiêu hết* mà quý sắp hết, SRE nên khuyến khích dev làm gì? (gợi ý: budget là để *dùng*, không phải để dành.)

## 5. Bản đồ khoá SRE

Mỗi bài một trụ cột SRE, xây trên error budget của bài này:

| # | Bài | Trụ SRE | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | SRE là gì + error budget | reliability là đánh đổi | SRE: embracing-risk |
| 1 | SLI / SLO / SLA | đo đúng, đặt mục tiêu | SRE: service-level-objectives |
| 2 | Observability & golden signals | nhìn thấy hệ | SRE: monitoring |
| 3 | Alerting | báo động theo triệu chứng | SRE: monitoring + Workbook |
| 4 | Toil & automation | diệt việc lặp tay | SRE: eliminating-toil |
| 5 | Incident response & on-call | ứng cứu có kỷ luật | SRE: being-on-call + Workbook |
| 6 | Postmortem culture | học từ sự cố, blameless | SRE: postmortem-culture |
| 7 | Quá tải & cascading failure | chịu tải, không sập dây chuyền | SRE: handling-overload |
| 8 | Chaos engineering & testing | chủ động tiêm lỗi | Workbook |

Giữ phong cách dễ hình dung (tình huống + ẩn dụ + số dắt tay) và *áp lên hệ thật* — ta sẽ đặt SLO cho chính **Notes API capstone** của aws-fund.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 0.1 — Vì sao "nhắm 100% reliability" là sai?
> **Đáp:** độ tin cậy cực cao *có giá*: tối đa ổn định giới hạn tốc độ ra tính năng + tăng chi phí; và người dùng thường không nhận ra "số 9" thừa (mạng họ còn kém tin cậy hơn).

> [!question] Thẻ 0.2 — "Độ tin cậy là một tính năng" nghĩa là gì?
> **Đáp:** nó đánh đổi với các tính năng khác (và tốc độ, chi phí). Mục tiêu đúng = *đủ* tin cậy cho người dùng hài lòng, không hơn.

> [!question] Thẻ 0.3 — Error budget là gì? Tính từ đâu?
> **Đáp:** thước đo khách quan "được phép kém tin cậy tới mức nào" trong một quý = `1 − SLO`. VD SLO 99.9% → budget 0.1% (số request/downtime được phép lỗi).

> [!question] Thẻ 0.4 — Error budget chấm dứt "cuộc chiến dev vs ops" ra sao?
> **Đáp:** tạo **động cơ chung**: biến "nhanh hay ổn?" (cảm tính) thành "còn bao nhiêu budget?" (số học). Còn budget → ship; cạn → đóng băng. Cả hai nhìn một con số.

> [!question] Thẻ 0.5 — Vì sao mỗi "số 9" thêm vào lại đắt hơn nhiều?
> **Đáp:** downtime cho phép giảm theo cấp (99%→432ph, 99.99%→4ph/tháng); để đạt cần dư thừa + tự động hoá + kiểm thử tốn kém cấp số.

## 7. Câu hỏi tự kiểm tra

1. Mô tả "cuộc chiến dev vs ops". SRE giải nó bằng gì thay vì chọn phe? *(mục 1, 3)*
2. Vì sao độ tin cậy là đánh đổi, không phải "càng cao càng tốt"? *(mục 2, SRE: embracing-risk)*
3. Error budget tính thế nào từ SLO? Nó điều khiển hành vi dev/SRE ra sao? *(mục 3)*
4. Chạy demo mục 4. Vì sao từ 99% xuống 99.99% là bước nhảy lớn về chi phí? *(mục 4)*
5. Nếu budget còn dư cuối quý, nên làm gì — và điều đó nói gì về mục tiêu của SRE? *(mục 4 Tự thử)*

## Tóm tắt một trang

```
BÀI 0 — SRE LÀ GÌ + ERROR BUDGET
─────────────────────────────────────────────────────────
VẤN ĐỀ  dev muốn ship nhanh, ops muốn ổn → chiến tranh + họp đổ lỗi. SRE giải
   bằng một CON SỐ cả hai đồng ý, không chọn phe.

ĐỘ TIN CẬY LÀ ĐÁNH ĐỔI  "extreme reliability comes at a cost" (SRE embracing-
   risk): tối đa ổn định → chặn tính năng + tăng chi phí. Mục tiêu = ĐỦ tin cậy,
   KHÔNG hơn. Nhắm 100% là SAI.

ERROR BUDGET  = 1 − SLO = "được phép hỏng tới mức nào" trong một quý (metric
   khách quan). Còn budget → dev ship thoải mái; CẠN → đóng băng, tập trung ổn
   định. Tạo ĐỘNG CƠ CHUNG cho dev + SRE. = ngân sách tiêu vặt, nhìn số dư.

DEMO  99%→432ph/tháng, 99.99%→4ph (mỗi số 9 ĐẮT theo cấp). SLO 99.9% / 100M
   req → budget 100k lỗi. Sự cố 20k → tiêu 20% (ship ok); 120k → cạn (đóng băng).

9 BÀI  error budget → SLI/SLO → observability → alerting → toil → incident →
   postmortem → quá tải → chaos. Áp lên Notes API capstone.
```

## Nguồn

- **Google, *Site Reliability Engineering*** (O'Reilly, bản online `sre.google/sre-book`) — **Embracing Risk**: reliability có giá, error budget là metric khách quan + động cơ chung. `tai_lieu/sre_embracing-risk.txt`.
- **The Site Reliability Workbook** (O'Reilly) — dùng ở các bài sau cho phần thực hành. `tai_lieu/the-site-reliability-workbook-next18.pdf` (offset PDF = tr. + 32).
- Nối tiếp: [aws-design Bài 8 (DR/reliability)](../../aws-design/bai_hoc/bai_08_da-vung-dr.md), [Bài 2 (load shedding)](../../aws-design/bai_hoc/bai_02_rate-limiter.md); quan sát: [aws-fund Bài 7 (CloudWatch)](../../aws-fund/bai_hoc/bai_07_observability-cloudwatch.md).

---

**Bản đồ khoá học:** **[Bài 0 — SRE & error budget] ← bạn đang ở đây** · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · [Bài 7 — Quá tải & cascading](bai_07_overload-cascading.md) · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
