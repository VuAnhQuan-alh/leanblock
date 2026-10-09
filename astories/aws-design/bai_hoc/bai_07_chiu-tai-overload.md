# Bài 7 — Thiết kế hệ chịu traffic spike và cô lập sự cố

> [!info] Về bài này
> **Archetype 7 — khi một phần cháy, đừng để cháy cả nhà.** Bài 2 chặn tải thừa ở cửa; nhưng khi tải *vượt* mọi dự phòng, hoặc một tenant độc/một bug làm hỏng tài nguyên dùng chung, làm sao giới hạn **blast radius** (vùng ảnh hưởng)? Hai kỹ thuật Amazon: **shuffle sharding** (cô lập tenant theo tổ hợp tài nguyên) và **tránh fallback** (đường dự phòng ít test = thất bại đúng lúc cần).
> Nguồn: **BL** *Workload isolation using shuffle sharding* + *Avoiding fallback in distributed systems*. Nền: [cloud-base Bài 9 (sharding)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 7 (thất bại)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md); pattern: [release-it](../../release-it/README.md); dịch vụ: [aws-fund Bài 2 (autoscaling)](../../aws-fund/bai_hoc/bai_02_compute.md).
> **Lab:** mô phỏng shuffle sharding bằng Node 22 (tất định).
> Nên đọc trước: [Bài 2 — rate limiter](bai_02_rate-limiter.md).

## Mục lục

1. [Đề bài, ràng buộc, ước lượng](#1-đề-bài-ràng-buộc-ước-lượng)
2. [Kiến trúc: autoscale, cô lập, chịu tải](#2-kiến-trúc-autoscale-cô-lập-chịu-tải)
3. [Đào sâu: shuffle sharding cô lập blast radius](#3-đào-sâu-shuffle-sharding-cô-lập-blast-radius)
4. [Đào sâu: vì sao tránh fallback](#4-đào-sâu-vì-sao-tránh-fallback)
5. [Lab: shuffle sharding thu nhỏ blast radius](#5-lab-shuffle-sharding-thu-nhỏ-blast-radius)
6. [Soi Well-Architected](#6-soi-well-architected)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, ước lượng

> [!example] "Hàng xóm ồn ào" kéo sập cả toà nhà
> Dịch vụ của bạn phục vụ nhiều khách trên *chung* một dàn worker. Một khách — `tenant-X` — bị DDoS (hoặc gửi một query cực nặng). Dàn worker nhận request của X bị nghẽn. Cách chia thông thường (nhóm cố định) khiến *mọi* khách chung nhóm với X **cùng chết**. Khách Y, Z, W chẳng làm gì sai vẫn sập theo. Bạn cần cách **cô lập**: X cháy thì chỉ X (và càng ít hàng xóm càng tốt) chịu, phần còn lại vẫn sống. Đó là shuffle sharding (§3).

**Chức năng:** một dịch vụ đa-tenant (nhiều khách dùng chung hạ tầng) phải chịu *spike* đột ngột và không để **một** tenant xấu (bị DDoS, gửi query độc, hoặc chỉ là "hàng xóm ồn ào") kéo sập **mọi** tenant. **Phi chức năng:** blast radius nhỏ, hồi phục tự động, không phụ thuộc đường dự phòng mong manh.

Ràng buộc cốt lõi: tài nguyên *dùng chung* nghĩa là sự cố *lan*. Autoscale (thêm máy khi tải lên) là tuyến đầu, nhưng nó có độ trễ và trần — không cứu được tình huống "một tenant chiếm trọn một tài nguyên". Cần **cô lập** (isolation): phân chia sao cho hỏng một phần chỉ hại một phần nhỏ.

## 2. Kiến trúc: autoscale, cô lập, chịu tải

```
                      ┌─ rate limit ở cửa (Bài 2) — chặn tải thừa sớm
   client ─▶ ALB ─────┤
                      └─ autoscaling: thêm instance khi tải lên (có độ trễ + trần)
                                 │
          SHUFFLE SHARDING: mỗi tenant → một BỘ worker riêng (không shard cứng)
          ┌────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
          │   w0   │   w1   │   w2   │   w3   │   w4   │   w5   │   w6   │   w7   │
          └────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘
          tenant A → {w0,w3}   tenant B → {w1,w5}   tenant xấu → {w2,w6} (chỉ giáng w2,w6)
```

Ba lớp phòng thủ chồng nhau: **rate limit** (Bài 2) chặn tải thừa *trước khi* vào; **autoscale** nới công suất theo tải; và **shuffle sharding** *giới hạn thiệt hại* khi một phần vẫn hỏng. Lớp thứ ba là điểm mới của bài, vì nó xử đúng cái autoscale/rate-limit bỏ sót: một tenant độc chiếm/làm hỏng tài nguyên dùng chung.

## 3. Đào sâu: shuffle sharding cô lập blast radius

> [!example] Ẩn dụ: chia cặp trực nhật
> Lớp 8 học sinh, cần cử người trực. **Shard cứng**: chia 4 tổ cố định (AB, CD, EF, GH); nếu A nghỉ ốm "lây" cả tổ thì B chết chung — 1/4 lớp liên đới. **Shuffle sharding**: mỗi học sinh được gán một *cặp bạn riêng* (A+D, B+F, C+G...). A ốm chỉ ảnh hưởng 2 bạn trùng *đúng cặp* với A — mà gần như không ai trùng *cả cặp*; bạn chỉ trùng *một* người vẫn nhờ người kia gánh. Với 8 người có tới C(8,2)=28 cặp khác nhau để rải.

Sharding thường (shard cứng): chia worker thành các nhóm cố định, mỗi tenant vào một nhóm. Một tenant xấu hạ nhóm của nó → *mọi* tenant cùng nhóm chết. Blast radius = 1/số-nhóm (vd 25% nếu 4 nhóm). Amazon làm tốt hơn nhiều:

> [!quote] BL: workload-isolation-using-shuffle-sharding
> "Our invention was shuffle sharding."
>
> *Phát minh của chúng tôi là **shuffle sharding**.*

> [!quote] BL: workload-isolation-using-shuffle-sharding
> "With shuffle sharding we create virtual shards of two workers each, and we assign our customers or resources, or whatever we want to isolate, to one of those virtual shards."
>
> *Với shuffle sharding, ta tạo các **virtual shard gồm hai worker**, và gán mỗi khách/tài nguyên (thứ muốn cô lập) vào **một virtual shard** như vậy.*

Mấu chốt: virtual shard là một **tổ hợp** worker, không phải nhóm cứng. Với 8 worker, có C(8,2)=28 tổ hợp 2-worker khác nhau → 28 tenant có thể mỗi người một *bộ đôi riêng*. Khi tenant xấu làm giáng 2 worker của nó, một tenant khác chỉ **chết hẳn** nếu *cả hai* worker của họ trùng đúng 2 worker đó — xác suất nhỏ theo cấp số. Tenant chỉ trùng *một* worker vẫn chạy nhờ retry/load-balance sang worker còn lại. Hiệu quả rõ nhất khi bị tấn công:

> [!quote] BL: workload-isolation-using-shuffle-sharding
> "The following two images show how sharding can limit the impact of a DDoS attack."
>
> *Hai hình sau cho thấy sharding **giới hạn tác động của một đợt tấn công DDoS** ra sao.*

Đây là **sharding của [cloud-base Bài 9](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md)** dùng cho *cô lập lỗi* thay vì *scale dung lượng* — cùng một ý tưởng (chia + gán khoá), mục tiêu khác. Lab §5 đo blast radius tụt từ 6 xuống 0.

## 4. Đào sâu: vì sao tránh fallback

> [!example] Ẩn dụ: cái phanh phụ chưa đạp bao giờ
> Fallback giống *cái phanh tay bạn không dùng suốt 5 năm*. Ngày phanh chính hỏng (đúng lúc nguy hiểm nhất) bạn kéo phanh tay — và phát hiện nó đã rỉ, không ăn. Đường code chỉ chạy "khi có sự cố" cũng vậy: ít chạy = ít test = hỏng đúng lúc cần. Thà dùng *đường chính* mỗi ngày (luôn được kiểm) còn hơn tin một đường dự phòng chưa ai thử.

Khi một phụ thuộc hỏng, phản xạ tự nhiên là "dùng đường dự phòng (fallback)" — trả dữ liệu cache cũ, giá trị mặc định, hệ phụ. Amazon cảnh báo ngược:

> [!quote] BL: avoiding-fallback-in-distributed-systems
> "It is easy to develop fallback strategies that rarely trigger in production."
>
> *Rất dễ viết các chiến lược **fallback hiếm khi được kích hoạt trong production**.*

Vấn đề: đường ít chạy = đường ít test = đường **sẽ hỏng đúng lúc cần nhất** (lúc sự cố — khi mọi thứ đã căng). Fallback còn che giấu lỗi và tạo hành vi bất ngờ dưới tải. Lời khuyên của Amazon:

> [!quote] BL: avoiding-fallback-in-distributed-systems
> "Instead, we favor code paths that are exercised in production continuously rather than rarely."
>
> *Thay vào đó, chúng tôi ưu tiên các **đường code được chạy liên tục trong production**, thay vì hiếm khi.*

Nghĩa là: thay vì thêm một đường dự phòng mong manh, hãy làm *đường chính* đủ kiên cường (retry+backoff Bài 4, idempotency Bài 5, cô lập shuffle sharding §3) để không cần fallback — hoặc nếu buộc phải có, *chạy nó thường xuyên* (vd luôn đọc từ cache, coi DB chỉ là nguồn cập nhật cache) để nó luôn được test. Đây là lý do pattern **circuit breaker** ([release-it](../../release-it/README.md)) được ưa hơn: nó *fail nhanh và rõ*, không giả vờ chạy bằng đường chưa test.

## 5. Lab: shuffle sharding thu nhỏ blast radius

Mô phỏng tất định: 28 tenant trên 8 worker. Một tenant xấu làm giáng 2 worker của nó. Đếm bao nhiêu tenant *khác* chết hẳn (cả 2 worker trùng) — regular sharding vs shuffle sharding:

```typescript
// Shuffle sharding: thay vì gán khách vào 1 "shard" cứng (bad tenant hạ cả shard),
// gán mỗi khách một BỘ ĐÔI worker RIÊNG. Một khách xấu chỉ "giáng" 2 worker của
// nó; khách khác chỉ chết HẲN nếu CẢ HAI worker của họ trùng bộ đó — hiếm theo
// cấp số. Có retry/LB thì trùng 1 worker vẫn chạy (dùng worker còn lại).
const WORKERS = 8;
// liệt kê mọi tổ hợp 2-worker: C(8,2) = 28 "shuffle shard" phân biệt
const allPairs: Array<[number, number]> = [];
for (let i = 0; i < WORKERS; i++) for (let j = i + 1; j < WORKERS; j++) allPairs.push([i, j]);
const N = allPairs.length;                 // 28 khách, mỗi khách một cặp RIÊNG
const pairOf = (c: number): [number, number] => allPairs[c];
// REGULAR sharding: 4 shard cứng (mỗi 2 worker); khách c -> shard c%4
const regularShard = (c: number): [number, number] => { const s = c % 4; return [s * 2, s * 2 + 1]; };

const BAD = 0;
function blast(assign: (c: number) => [number, number]): number {
  const bad = new Set(assign(BAD));        // 2 worker bị giáng bởi khách xấu
  let down = 0;
  for (let c = 0; c < N; c++) {
    if (c === BAD) continue;
    const [x, y] = assign(c);
    if (bad.has(x) && bad.has(y)) down++;  // chết HẲN chỉ khi CẢ 2 worker trùng
  }
  return down;
}
const reg = blast(regularShard), shuf = blast(pairOf);
console.log(`${N} khách trên ${WORKERS} worker. Khách #${BAD} "xấu" làm giáng 2 worker của nó.`);
console.log(`  REGULAR sharding : ${reg} khách khác CHẾT HẲN  (cùng shard cứng với khách xấu)`);
console.log(`  SHUFFLE sharding : ${shuf} khách khác chết hẳn  (phải trùng CẢ cặp worker)`);
console.log(`  → shuffle thu nhỏ blast radius từ ${reg} xuống ${shuf}; khách chỉ trùng 1 worker vẫn chạy (retry/LB).`);
```

Kết quả chạy thật *(tất định)*:

```
28 khách trên 8 worker. Khách #0 "xấu" làm giáng 2 worker của nó.
  REGULAR sharding : 6 khách khác CHẾT HẲN  (cùng shard cứng với khách xấu)
  SHUFFLE sharding : 0 khách khác chết hẳn  (phải trùng CẢ cặp worker)
  → shuffle thu nhỏ blast radius từ 6 xuống 0; khách chỉ trùng 1 worker vẫn chạy (retry/LB).
```

Regular sharding: tenant xấu ở shard cứng → cả 6 tenant cùng shard chết (blast radius lớn). Shuffle sharding: mỗi tenant một tổ hợp riêng → *không* tenant nào khác trùng *cả hai* worker → 0 chết hẳn; những tenant trùng *một* worker vẫn phục vụ được nhờ dùng worker còn lại (cần retry/load-balance — Bài 4). Blast radius co từ "một phần tư khách" xuống "gần như không ai". Với tải thật (không phải tenant độc tuyệt đối), shuffle sharding biến "một sự cố làm sập 25% khách" thành "làm chậm một phần nhỏ".

> [!note] Tự thử
> 1. Tăng `WORKERS=16` (C(16,2)=120 tổ hợp): blast radius còn nhỏ hơn nữa. Vì sao thêm worker giúp *cô lập* theo cấp số, không chỉ tăng dung lượng?
> 2. Cho shuffle shard 3 worker thay vì 2: xác suất trùng *cả ba* còn nhỏ hơn. Đánh đổi với chi phí là gì?
> 3. Nghĩ về fallback: nếu tenant trùng 1 worker "fallback" sang worker đó luôn (thay vì retry), điều gì xảy ra khi worker đó cũng quá tải? (mục 4)

## 6. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | blast radius nhỏ (shuffle); fail nhanh-rõ thay vì fallback mong manh | cô lập = sự cố không lan |
| Performance | autoscale + rate limit giữ goodput dưới spike | shuffle cần retry/LB sang worker còn lại |
| Cost | cô lập tốt cần dư công suất (worker không nhồi 100%) | đánh đổi: an toàn vs tận dụng |
| Security | chống "noisy neighbor" + giới hạn tác động DDoS | kết hợp WAF/Shield |
| Operational | ưu tiên đường code chạy-liên-tục → ít bất ngờ khi sự cố | test chaos (tenant xấu) định kỳ |

Nguyên tắc đọng lại: **cô lập để sự cố không lan (shuffle sharding), và đừng tin đường dự phòng chưa test (tránh fallback).** Nhưng mọi thứ tới giờ vẫn trong *một* vùng. Khi *cả một vùng AWS* sập thì sao? Đó là Bài 8.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — Ba lớp phòng thủ chồng nhau khi gặp spike/sự cố?
> **Đáp:** (1) rate limit ở cửa (Bài 2) chặn tải thừa; (2) autoscale nới công suất; (3) shuffle sharding giới hạn blast radius khi một phần vẫn hỏng.

> [!question] Thẻ 7.2 — Shuffle sharding khác sharding cứng thế nào? Vì sao blast radius nhỏ hơn?
> **Đáp:** mỗi tenant một *tổ hợp* worker riêng (không nhóm cứng). Tenant khác chết hẳn chỉ khi trùng *cả* tổ hợp (hiếm theo cấp số); trùng 1 worker vẫn chạy nhờ retry/LB.

> [!question] Thẻ 7.3 — Shuffle sharding nối về khái niệm nền nào, mục tiêu khác gì?
> **Đáp:** = sharding của cloud-base Bài 9 (chia + gán khoá), nhưng dùng để **cô lập lỗi** (giảm blast radius) thay vì **scale dung lượng**.

> [!question] Thẻ 7.4 — Vì sao Amazon "hầu như không dùng" fallback?
> **Đáp:** đường fallback hiếm kích hoạt → ít test → **hỏng đúng lúc cần** (khi sự cố). Ưu tiên đường code *chạy liên tục* trong production (được test liên tục).

> [!question] Thẻ 7.5 — Thay vì fallback mong manh, nên làm gì?
> **Đáp:** làm đường chính kiên cường (retry+backoff Bài 4, idempotency Bài 5, cô lập §3); nếu buộc có dự phòng thì chạy nó *thường xuyên*. Ưa circuit breaker (fail nhanh-rõ) hơn giả vờ chạy.

## 8. Câu hỏi tự kiểm tra

1. Autoscale/rate-limit bỏ sót tình huống nào mà cô lập xử được? *(mục 1–2)*
2. Giải thích shuffle sharding. Vì sao 8 worker cho 28 "shard"? *(mục 3, BL)*
3. Vì sao shuffle sharding giới hạn tác động DDoS/noisy-neighbor? *(mục 3, BL)*
4. Vì sao đường fallback nguy hiểm? Amazon ưu tiên gì thay thế? *(mục 4, BL)*
5. Chạy lab §5. Vì sao regular = 6 còn shuffle = 0? Vai trò retry/LB cho tenant trùng 1 worker? *(mục 5)*

## Tóm tắt một trang

```
BÀI 7 — CHỊU TRAFFIC SPIKE & CÔ LẬP SỰ CỐ
─────────────────────────────────────────────────────────
VẤN ĐỀ  tài nguyên dùng chung → sự cố LAN. Autoscale/rate-limit (Bài 2) không
   cứu "1 tenant độc chiếm tài nguyên chung". Cần CÔ LẬP (giới hạn blast radius).

SHUFFLE SHARDING (BL)  mỗi tenant một TỔ HỢP worker riêng (không shard cứng).
   C(8,2)=28 tổ hợp. Tenant khác chết hẳn CHỈ khi trùng CẢ cặp (hiếm cấp số);
   trùng 1 worker vẫn chạy (retry/LB). = sharding (cloud-base Bài 9) để CÔ LẬP,
   không phải scale.

TRÁNH FALLBACK (BL)  đường fallback hiếm chạy → ít test → HỎNG đúng lúc cần.
   Ưu tiên đường code CHẠY LIÊN TỤC; làm đường chính kiên cường; ưa circuit
   breaker (fail nhanh-rõ) hơn giả vờ chạy.

LAB  28 tenant/8 worker, 1 tenant xấu: regular sharding → 6 tenant chết;
   shuffle sharding → 0. Blast radius co từ 1/4 khách xuống gần như không ai.

6 TRỤ  reliability (blast radius nhỏ, fail rõ); cost (cô lập cần dư công
   suất). Tiếp: cả một VÙNG AWS sập thì sao? → Bài 8.
```

## Nguồn

- **Amazon Builders' Library** — *Workload isolation using shuffle sharding*: shuffle sharding, virtual shard, giới hạn DDoS. `tai_lieu/bl_workload-isolation-using-shuffle-sharding.txt`. — *Avoiding fallback in distributed systems*: fallback hiếm chạy, ưu tiên đường chạy-liên-tục. `tai_lieu/bl_avoiding-fallback-in-distributed-systems.txt`.
- Nền: [cloud-base Bài 9 (sharding)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 7 (thất bại)](../../cloud-base/bai_hoc/bai_07_dist-giao-tiep.md); pattern: [release-it (circuit breaker/bulkhead)](../../release-it/README.md).
- Dịch vụ: [aws-fund Bài 2 — autoscaling/compute](../../aws-fund/bai_hoc/bai_02_compute.md).

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · **[Bài 7 — Chịu traffic spike] ← bạn đang ở đây** · [Bài 8 — Đa vùng & DR](bai_08_da-vung-dr.md) · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
