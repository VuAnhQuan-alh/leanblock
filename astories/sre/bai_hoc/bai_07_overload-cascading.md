# Bài 7 — Quá tải và cascading failure

> [!info] Về bài này
> Sự cố tệ nhất không phải "một service chết" — mà là **một service chết kéo sập *cả hệ* theo kiểu dây chuyền**: cascading failure. Bài này nắm cơ chế (**vòng phản hồi dương** — lỗi sinh ra thêm lỗi), và các van chặn: **circuit breaker**, **load shedding** (Bài aws-design 2), **graceful degradation** (phục vụ bản rút gọn còn hơn không phục vụ).
> Nguồn: **SRE Book** — *Addressing Cascading Failures* + *Handling Overload*.
> **Trích:** `SRE: <chương>`. **Demo:** Node 22.
> Nên đọc trước: [aws-design Bài 2 (load shedding)](../../aws-design/bai_hoc/bai_02_rate-limiter.md), [Bài 4 (retry/backoff)](../../aws-design/bai_hoc/bai_04_he-thong-bao.md).

## Mục lục

1. [Tình huống: một service chậm, cả hệ sập](#1-tình-huống-một-service-chậm-cả-hệ-sập)
2. [Cascading failure: vòng phản hồi dương](#2-cascading-failure-vòng-phản-hồi-dương)
3. [Chặn vòng: circuit breaker và graceful degradation](#3-chặn-vòng-circuit-breaker-và-graceful-degradation)
4. [Demo: retry amplification vs circuit breaker](#4-demo-retry-amplification-vs-circuit-breaker)
5. [Thẻ ôn (active recall)](#5-thẻ-ôn-active-recall)
6. [Câu hỏi tự kiểm tra](#6-câu-hỏi-tự-kiểm-tra)
7. [Tóm tắt một trang](#tóm-tắt-một-trang)
8. [Nguồn](#nguồn)

---

## 1. Tình huống: một service chậm, cả hệ sập

> [!example] Hiệu ứng domino
> Database của bạn *chậm lại* một chút (hiccup, GC pause). Service A gọi DB bắt đầu timeout. "Không sao, retry cho chắc" — A thử lại. Nhưng *mọi* instance của A cùng retry → DB nhận **gấp đôi** tải → chậm hơn nữa → nhiều timeout hơn → retry nhiều hơn → ... Trong vài phút, DB *sập hẳn* dưới cơn bão retry, kéo theo A sập, rồi service B (gọi A) sập, rồi cả hệ. Thứ bắt đầu bằng một hiccup 200ms kết thúc bằng một sự cố toàn hệ 2 tiếng. Và cái *làm nó tệ hơn* chính là phản xạ "retry cho chắc".

Đây là **cascading failure** — và nó khác lỗi thường ở một điểm chết người: nó *tự lớn lên*.

## 2. Cascading failure: vòng phản hồi dương

> [!quote] SRE: addressing-cascading-failures
> "A cascading failure is a failure that grows over time as a result of positive feedback."
>
> *Một **cascading failure** là một lỗi **lớn dần theo thời gian do vòng phản hồi dương (positive feedback)**.*

"Positive feedback" là chìa khoá: một lỗi nhỏ *tạo điều kiện* cho lỗi lớn hơn, lỗi lớn hơn tạo lỗi lớn hơn nữa — như quả cầu tuyết lăn. Nguồn feedback phổ biến nhất là **retry**: request lỗi → retry → thêm tải → nhiều lỗi hơn → nhiều retry hơn. (Đây đúng là "bão retry" của [aws-design Bài 4](../../aws-design/bai_hoc/bai_04_he-thong-bao.md), nhưng ở quy mô *hệ thống*, nó không chỉ làm chậm mà *sập dây chuyền*.)

> [!example] Ẩn dụ: kẹt xe dây chuyền trên cao tốc
> Một xe phanh gấp → xe sau phanh gấp hơn → xe sau nữa phanh gấp hơn nữa → trong vài giây cả làn *đứng im*, dù sự cố ban đầu (một cú phanh) đã qua từ lâu. Kẹt xe *tự duy trì* sau khi nguyên nhân gốc biến mất — đúng như cascading failure *tự lớn lên* nhờ feedback (ở đây là tài xế phản ứng dây chuyền; ở hệ thống là retry). Chữa không phải "lái nhanh hơn" mà là *cắt vòng phản hồi*.

## 3. Chặn vòng: circuit breaker và graceful degradation

Vì cascade là *vòng phản hồi*, cách chữa là **cắt vòng**. Ba van chính:

**(a) Circuit breaker** — khi thấy tỉ lệ lỗi cao, *ngừng* gọi (và ngừng retry) tới service đang chết trong một lúc, cho nó thở để hồi phục. Như cầu dao điện: quá tải thì *ngắt* để không cháy cả nhà (thay vì cố đẩy thêm dòng). ([release-it](../../release-it/README.md) gọi tên pattern này.)

**(b) Load shedding** — từ chối bớt tải ở cửa để bảo vệ goodput ([aws-design Bài 2](../../aws-design/bai_hoc/bai_02_rate-limiter.md)): thà phục vụ tốt 70% còn hơn làm chậm 100%.

**(c) Graceful degradation** — thay vì lỗi hoàn toàn, trả một bản *rút gọn*:

> [!quote] SRE: handling-overload
> "One option for handling overload is to serve degraded responses: responses that are not as accurate as or that contain less data than normal responses, but that are easier to compute."
>
> *Một cách xử lý quá tải là **phục vụ bản rút gọn (degraded)**: kết quả **kém chính xác hơn hoặc ít dữ liệu hơn** bình thường, nhưng **dễ tính hơn**.*

Ví dụ: trang chủ quá tải → trả kết quả từ cache (cũ vài phút) thay vì tính mới; gợi ý sản phẩm quá tải → trả top phổ biến thay vì cá nhân hoá. Tổng kết nguyên tắc:

> [!quote] SRE: handling-overload
> "it's best to build clients and backends to handle resource restrictions gracefully: redirect when possible, serve degraded results when necessary, and handle resource errors transparently when all else fails."
>
> *tốt nhất là xây client + backend **xử lý giới hạn tài nguyên một cách duyên dáng**: **chuyển hướng** khi được, **phục vụ bản rút gọn** khi cần, và **xử lý lỗi tài nguyên êm thấm** khi hết cách.*

Demo mục 4 cho thấy cái quan trọng nhất — cắt vòng feedback — bằng circuit breaker.

## 4. Demo: retry amplification vs circuit breaker

Backend tụt công suất (100→60), tải gốc 80. Mỗi lỗi bị retry 2 lần → tải vòng sau phình. So *không* breaker (cascade) vs *có* breaker (cắt vòng):

```typescript
// Cascading failure = lỗi LỚN DẦN theo thời gian do VÒNG PHẢN HỒI DƯƠNG.
// Kịch bản: backend tụt công suất → request lỗi → client RETRY → thêm tải →
// lỗi nhiều hơn → retry nhiều hơn → sập. Circuit breaker cắt vòng này.
const CAP = 60;            // công suất sau khi backend "hiccup" (vốn 100)
const BASE = 80;           // tải gốc (vốn < 100, giờ > 60)
const RETRY = 2;           // mỗi request lỗi bị thử lại 2 lần

function simulate(breakerAtFailRate: number, label: string) {
  console.log(`\n${label}`);
  let extra = 0;           // tải thêm do retry
  let open = false;        // circuit breaker đã mở?
  for (let round = 1; round <= 5; round++) {
    const load = open ? BASE : BASE + extra;
    const served = Math.min(load, CAP);
    const failed = Math.max(0, load - CAP);
    const failRate = load > 0 ? failed / load : 0;
    console.log(`  vòng ${round}: tải ${load.toFixed(0)} | phục vụ ${served} | lỗi ${failed.toFixed(0)} (${(failRate*100).toFixed(0)}%)${open ? "  [breaker MỞ: ngừng retry]" : ""}`);
    if (!open && failRate >= breakerAtFailRate) open = true;    // mở breaker
    extra = failed * RETRY;                                      // retry → tải vòng sau
  }
}
simulate(2, "KHÔNG circuit breaker (retry mù → cascading):");   // breaker không bao giờ mở
simulate(0.3, "CÓ circuit breaker (ngắt retry khi lỗi > 30%):");
console.log("\nVòng phản hồi dương: lỗi → retry → thêm tải → lỗi nhiều hơn → SẬP.");
console.log("Circuit breaker cắt vòng: thấy lỗi cao → NGỪNG retry → tải về gốc → hệ thở lại.");
```

Kết quả chạy thật *(tất định)*:

```

KHÔNG circuit breaker (retry mù → cascading):
  vòng 1: tải 80 | phục vụ 60 | lỗi 20 (25%)
  vòng 2: tải 120 | phục vụ 60 | lỗi 60 (50%)
  vòng 3: tải 200 | phục vụ 60 | lỗi 140 (70%)
  vòng 4: tải 360 | phục vụ 60 | lỗi 300 (83%)
  vòng 5: tải 680 | phục vụ 60 | lỗi 620 (91%)

CÓ circuit breaker (ngắt retry khi lỗi > 30%):
  vòng 1: tải 80 | phục vụ 60 | lỗi 20 (25%)
  vòng 2: tải 120 | phục vụ 60 | lỗi 60 (50%)
  vòng 3: tải 80 | phục vụ 60 | lỗi 20 (25%)  [breaker MỞ: ngừng retry]
  vòng 4: tải 80 | phục vụ 60 | lỗi 20 (25%)  [breaker MỞ: ngừng retry]
  vòng 5: tải 80 | phục vụ 60 | lỗi 20 (25%)  [breaker MỞ: ngừng retry]

Vòng phản hồi dương: lỗi → retry → thêm tải → lỗi nhiều hơn → SẬP.
Circuit breaker cắt vòng: thấy lỗi cao → NGỪNG retry → tải về gốc → hệ thở lại.
```

Không breaker: tải *bùng nổ* 80→120→200→360→**680**, lỗi 25%→**91%** — hệ tự giết mình, dù công suất backend *không hề giảm thêm*. Có breaker: phát hiện lỗi vượt 30% → *ngừng retry* → tải tụt về gốc 80 → hệ ổn định ở mức "quá tải nhẹ nhưng sống". Mấu chốt: breaker **không** sửa nguyên nhân gốc (backend vẫn yếu, vẫn 25% lỗi) — nó chỉ *cắt vòng phản hồi* để sự cố không *tự khuếch đại* tới sập. Sửa gốc (tăng công suất/load shed để tải < 60) là việc tiếp theo. Nối Bài 4 (aws-design): retry *phải* có backoff+jitter+giới hạn, nếu không bạn tự dựng cỗ máy cascade.

> [!note] Tự thử
> 1. Đổi `RETRY = 0` (không retry): còn cascade không? Vì sao retry là nguồn feedback dương phổ biến nhất?
> 2. Hạ ngưỡng breaker xuống `0.2`: nó mở sớm hơn (vòng 2). Đánh đổi giữa "mở sớm chống cascade" và "mở nhầm khi chỉ là spike nhất thời"?
> 3. Kết hợp với shuffle sharding (aws-design B7): vì sao cô lập + circuit breaker cùng nhau mạnh hơn mỗi cái?

## 5. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — Cascading failure khác lỗi thường ở điểm gì?
> **Đáp:** nó **tự lớn lên theo thời gian do vòng phản hồi dương** (positive feedback) — một lỗi tạo điều kiện cho lỗi lớn hơn. Lỗi thường không tự khuếch đại.

> [!question] Thẻ 7.2 — Nguồn feedback dương phổ biến nhất? Cơ chế?
> **Đáp:** **retry**: lỗi → retry → thêm tải → nhiều lỗi hơn → nhiều retry hơn → sập. "Retry cho chắc" làm sự cố tệ hơn.

> [!question] Thẻ 7.3 — Ba van chặn quá tải/cascade?
> **Đáp:** (a) **circuit breaker** (ngừng gọi service đang chết, cắt vòng); (b) **load shedding** (từ chối bớt ở cửa — Bài 2); (c) **graceful degradation** (trả bản rút gọn còn hơn lỗi).

> [!question] Thẻ 7.4 — Circuit breaker sửa nguyên nhân gốc không? Nó làm gì?
> **Đáp:** KHÔNG — nó chỉ **cắt vòng phản hồi** để sự cố không tự khuếch đại tới sập. Sửa gốc (tăng công suất / giảm tải) là việc tiếp theo.

> [!question] Thẻ 7.5 — Graceful degradation là gì? Cho ví dụ.
> **Đáp:** quá tải → trả bản **rút gọn, dễ tính hơn** thay vì lỗi hoàn toàn. VD: kết quả từ cache cũ thay vì tính mới; top phổ biến thay vì cá nhân hoá.

## 6. Câu hỏi tự kiểm tra

1. Mô tả hiệu ứng domino DB-chậm → cả hệ sập. Cái gì *làm tệ hơn*? *(mục 1)*
2. Cascading failure: vai trò "positive feedback". Ẩn dụ kẹt xe. *(mục 2, SRE book)*
3. Ba van chặn. Circuit breaker hoạt động ra sao, như cầu dao thế nào? *(mục 3)*
4. Chạy demo mục 4. Vì sao tải bùng nổ dù công suất không giảm thêm? Breaker cắt gì? *(mục 4)*
5. Graceful degradation (SRE book): "redirect / degraded / transparent" nghĩa gì? *(mục 3)*

## Tóm tắt một trang

```
BÀI 7 — QUÁ TẢI & CASCADING FAILURE
─────────────────────────────────────────────────────────
CASCADING FAILURE  lỗi LỚN DẦN do VÒNG PHẢN HỒI DƯƠNG (SRE book). Một lỗi nhỏ
   tạo lỗi lớn hơn → quả cầu tuyết. Nguồn feedback #1 = RETRY (lỗi→retry→thêm
   tải→nhiều lỗi→...). (ẩn dụ: kẹt xe dây chuyền tự duy trì.)

3 VAN CHẶN  (a) CIRCUIT BREAKER: lỗi cao → ngừng gọi/retry, cắt vòng (cầu dao).
   (b) LOAD SHEDDING: từ chối ở cửa (aws-design B2). (c) GRACEFUL DEGRADATION:
   trả bản RÚT GỌN dễ tính còn hơn lỗi (SRE book: redirect/degraded/transparent).

DEMO  cap 60, tải gốc 80, retry×2: KHÔNG breaker → tải 80→680, lỗi 25%→91%
   (tự sập dù backend không yếu thêm). CÓ breaker → cắt retry → tải về 80, ổn.
   Breaker KHÔNG sửa gốc — chỉ cắt VÒNG để không tự khuếch đại.

→ retry PHẢI có backoff+jitter+giới hạn (aws-design B4), không thì tự dựng cascade.
```

## Nguồn

- **Google, *Site Reliability Engineering*** — **Addressing Cascading Failures**: định nghĩa (positive feedback). `tai_lieu/sre_addressing-cascading-failures.txt`. — **Handling Overload**: serve degraded responses, handle gracefully. `tai_lieu/sre_handling-overload.txt`.
- Nối: [aws-design Bài 2 (load shedding)](../../aws-design/bai_hoc/bai_02_rate-limiter.md), [Bài 4 (retry/backoff)](../../aws-design/bai_hoc/bai_04_he-thong-bao.md), [Bài 7 (cô lập/shuffle sharding)](../../aws-design/bai_hoc/bai_07_chiu-tai-overload.md); pattern: [release-it (circuit breaker)](../../release-it/README.md); nền: [cloud-base Bài 1 (quá tải/context switch)](../../cloud-base/bai_hoc/bai_01_os-ao-hoa.md).

---

**Bản đồ khoá học:** [Bài 0 — SRE & error budget](bai_00_sre-la-gi-error-budget.md) · [Bài 1 — SLI/SLO/SLA](bai_01_sli-slo-sla.md) · [Bài 2 — Observability & golden signals](bai_02_observability-golden-signals.md) · [Bài 3 — Alerting](bai_03_alerting.md) · [Bài 4 — Toil & automation](bai_04_toil-automation.md) · [Bài 5 — Incident & on-call](bai_05_incident-oncall.md) · [Bài 6 — Postmortem](bai_06_postmortem.md) · **[Bài 7 — Quá tải & cascading] ← bạn đang ở đây** · [Bài 8 — Chaos & testing](bai_08_chaos-testing.md)

Xem thêm [README khoá học](../README.md).
