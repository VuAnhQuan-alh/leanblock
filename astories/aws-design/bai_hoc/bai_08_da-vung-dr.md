# Bài 8 — Thiết kế đa vùng và Disaster Recovery

> [!info] Về bài này
> **Archetype 8 — khi cả một vùng sập.** Bài 7 cô lập sự cố *trong* một vùng; bài này hỏi câu lớn nhất: *cả một AWS Region* hỏng thì sao? Hai khái niệm neo mọi quyết định: **RTO/RPO** (chịu mất bao lâu / bao nhiêu dữ liệu) và **static stability** (hệ không đổi hành vi khi sự cố). Rồi bốn **chiến lược DR** đánh đổi phục hồi lấy chi phí. Đây cũng là **bài cuối** — khép lại cả khoá.
> Nguồn: **WA** (Reliability — DR, RTO/RPO, static stability). Nền: [cloud-base Bài 8 (replication/CAP)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md), [Bài 3 (durability)](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md), [Bài 15 (đồng hồ đa vùng)](../../cloud-base/bai_hoc/bai_15_dist-dong-ho.md); dịch vụ: [aws-fund Bài 5 (Route 53)](../../aws-fund/bai_hoc/bai_05_networking.md).
> **Lab:** máy tính chiến lược DR (Node 22, tất định).
> Nên đọc trước: [Bài 7 — chịu tải](bai_07_chiu-tai-overload.md), [cloud-base Bài 8](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md).

## Mục lục

1. [Đề bài, ràng buộc, RTO/RPO](#1-đề-bài-ràng-buộc-rtorpo)
2. [Kiến trúc: đa-AZ trước, đa-vùng sau](#2-kiến-trúc-đa-az-trước-đa-vùng-sau)
3. [Đào sâu: static stability, tránh bimodal](#3-đào-sâu-static-stability-tránh-bimodal)
4. [Đào sâu: bốn chiến lược DR](#4-đào-sâu-bốn-chiến-lược-dr)
5. [Lab: máy tính chiến lược DR](#5-lab-máy-tính-chiến-lược-dr)
6. [Soi Well-Architected](#6-soi-well-architected)
7. [Khép khoá: tám archetype, ba tầng](#7-khép-khoá-tám-archetype-ba-tầng)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Đề bài, ràng buộc, RTO/RPO

> [!example] "us-east-1 đang gặp sự cố"
> Một sáng, nửa Internet chậm/lỗi: một Region lớn của AWS gặp sự cố (chuyện có thật, vài năm một lần). Nếu toàn bộ hệ bạn nằm gọn trong Region đó — app chết theo, và câu hỏi của sếp là: *"Bao giờ sống lại? Có mất đơn hàng nào không?"*. Hai câu đó chính là **RTO** và **RPO**. Cách làm ngây thơ ("một Region, lo sau") biến sự cố của AWS thành sự cố của bạn. Bài này: chuẩn bị *trước* để chịu mất cả một Region, với chi phí tương xứng.

> [!example] Ẩn dụ RTO/RPO: tiệm bị mất điện
> **RTO** = *bao lâu để mở cửa lại* (chịu đóng cửa mấy tiếng?). **RPO** = *mất sổ sách của bao nhiêu lâu gần nhất* (lần sao lưu cuối cách đây bao lâu — nếu sao lưu mỗi đêm, mất nguyên ngày hôm nay). Tiệm tạp hoá chịu được cả hai vài giờ; ngân hàng thì gần như phải bằng 0.

**Chức năng:** hệ tiếp tục phục vụ (hoặc phục hồi nhanh) khi một AZ — hoặc cả một Region — sập. **Phi chức năng:** hai con số định lượng mọi thứ:

> [!quote] WA (tr. 38)
> "track KPIs, and also the recovery time objective (RTO) and recovery point objective (RPO), to assess a workload's resiliency (especially under failure-testing scenarios)."
>
> *theo dõi **RTO (recovery time objective)** và **RPO (recovery point objective)** để đánh giá độ kiên cường của workload (nhất là trong các kịch bản kiểm thử-thất-bại).*

**RTO** = *bao lâu* để phục hồi (downtime chấp nhận được). **RPO** = *bao nhiêu dữ liệu gần nhất* được phép mất (khoảng từ lần sao lưu cuối tới lúc sập). Blog cá nhân: RTO/RPO vài giờ là ổn. Ngân hàng: gần bằng 0. Hai con số này — xuất phát từ *tiền nghiệp vụ mất khi down* — quyết chiến lược (mục 4) và chi phí. Đây là bước "làm rõ yêu cầu phi chức năng" của Bài 0, ở dạng khắc nghiệt nhất.

## 2. Kiến trúc: đa-AZ trước, đa-vùng sau

```
   TẦNG 1 (mặc định): ĐA-AZ trong một Region — gần như miễn phí độ sẵn sàng
      ALB ─▶ instances rải trên AZ-a, AZ-b, AZ-c   ·   RDS Multi-AZ, S3 (11 9's)
      → chịu mất MỘT AZ mà không làm gì (static stability, mục 3)

   TẦNG 2 (khi cần): ĐA-VÙNG — chịu mất CẢ Region (đắt, phức tạp)
      Region chính ⇄ Region phụ (replication)   ·   Route 53 health-check failover
      → chọn 1 trong 4 chiến lược DR theo RTO/RPO (mục 4)
```

Nguyên tắc thứ tự: **đa-AZ trước** — AWS thiết kế để mất một AZ gần như vô hình nếu bạn rải tài nguyên qua nhiều AZ (RDS Multi-AZ, S3, ALB đều đa-AZ sẵn). Chỉ khi nghiệp vụ *thực sự* đòi chịu mất cả Region mới lên **đa-vùng** — vì nó kéo theo replication xuyên vùng (độ trễ + đồng hồ lệch, cloud-base Bài 15), chi phí nhân đôi, và bài toán CAP ở quy mô vùng (cloud-base Bài 8).

## 3. Đào sâu: static stability, tránh bimodal

> [!example] Ẩn dụ: lốp dự phòng trong cốp vs gọi cứu hộ
> **Static stability** = *đã* có lốp dự phòng bơm sẵn trong cốp: xịt lốp giữa đường, bạn tự thay, không phụ thuộc ai. **Bimodal** = không mang lốp, xịt lốp thì *gọi cứu hộ* — nhưng đúng lúc đó tổng đài cứu hộ cũng quá tải (vì ai cũng xịt lốp cùng cơn bão). Đường phục hồi tốt là đường *đã sẵn sàng từ trước*, không phải đường phải "kích hoạt" lúc khẩn.

Bẫy lớn nhất của DR: hệ hoạt động *khác* lúc bình thường và lúc sự cố — rồi "chế độ sự cố" (ít chạy, ít test) hỏng đúng lúc cần (đúng tinh thần "tránh fallback" Bài 7). WA đặt tên và quy tắc:

> [!quote] WA (tr. 642)
> "Workloads should be statically stable and only operate in a single normal mode. Bimodal behavior is when your workload exhibits different behavior under normal and failure modes."
>
> *Workload nên **statically stable** và **chỉ hoạt động ở một chế độ bình thường duy nhất**. **Bimodal behavior** là khi workload hành xử **khác nhau** giữa chế độ bình thường và chế độ sự cố.*

**Static stability** nghĩa là: hệ *đã* có sẵn mọi thứ để chịu lỗi, nên khi lỗi xảy ra nó **không cần làm gì mới** (không cần gọi API lúc đang sự cố, không cần provision gấp). Ví dụ: chạy sẵn dư công suất qua 3 AZ, mất 1 AZ thì 2 AZ còn lại *đã* gánh được — không phải vội vàng khởi tạo instance mới (lúc control plane cũng có thể đang quá tải). Ngược lại là **bimodal**: bình thường chạy 3 instance, mất AZ thì *cố* khởi 3 instance mới — một hành vi mới, ít test, dễ hỏng. Nguyên tắc: **đường phục hồi phải là đường đã chạy sẵn**, không phải đường kích hoạt lúc khẩn.

## 4. Đào sâu: bốn chiến lược DR

Với đa-vùng, có một phổ chiến lược đánh đổi RTO/RPO lấy chi phí:

> [!quote] WA (tr. 592)
> "Common disaster recovery strategies include backup and restore, pilot light, cold standby, warm standby, hot standby, and active-active, and they all differ in cost and complexity."
>
> *Các chiến lược DR phổ biến gồm **backup and restore, pilot light, cold/warm/hot standby, và active-active** — tất cả **khác nhau ở chi phí và độ phức tạp**.*

Bốn mốc chính (từ rẻ-chậm tới đắt-tức-thì): **Backup & Restore** (snapshot, dựng lại khi hỏng — RTO/RPO giờ), **Pilot Light** (lõi DB replica luôn chạy, phần còn lại tắt — RTO chục phút), **Warm Standby** (bản sao thu nhỏ luôn chạy, scale lên khi failover — RTO phút), **Active/Active đa-vùng** (chạy song song mọi vùng, Route 53 lái traffic — RTO ~0). Không có "tốt nhất": càng ngặt RTO/RPO càng đắt. Lab §5 biến phổ này thành bảng chọn theo yêu cầu.

## 5. Lab: máy tính chiến lược DR

So bốn chiến lược theo RTO/RPO/chi phí, rồi chọn cái rẻ nhất *đáp ứng* yêu cầu nghiệp vụ (tất định):

```typescript
// Disaster Recovery: 4 chiến lược kinh điển đánh đổi RTO (bao lâu khôi phục) &
// RPO (mất bao nhiêu dữ liệu gần nhất) LẤY chi phí. Không có "tốt nhất" — chọn
// theo yêu cầu nghiệp vụ. Con số dưới đây là minh hoạ bậc-độ-lớn (tất định).
type DR = { name: string; rto: string; rpo: string; cost: number; ghichu: string };
const strategies: DR[] = [
  { name: "Backup & Restore",   rto: "nhiều giờ",  rpo: "nhiều giờ",  cost: 1,  ghichu: "snapshot định kỳ, dựng lại khi hỏng" },
  { name: "Pilot Light",        rto: "chục phút",  rpo: "phút",       cost: 2,  ghichu: "lõi (DB replica) luôn chạy, phần còn lại tắt" },
  { name: "Warm Standby",       rto: "vài phút",   rpo: "giây",       cost: 4,  ghichu: "bản sao thu nhỏ luôn chạy, scale lên khi failover" },
  { name: "Multi-site Active/Active", rto: "~0 (tức thì)", rpo: "~0", cost: 8, ghichu: "chạy song song mọi vùng, Route53 lái traffic" },
];
console.log("Chiến lược DR               RTO          RPO       chi phí(×)");
console.log("─────────────────────────────────────────────────────────────");
for (const s of strategies)
  console.log(`${s.name.padEnd(27)} ${s.rto.padEnd(12)} ${s.rpo.padEnd(9)} ${"$".repeat(s.cost)}`);

// chọn chiến lược rẻ nhất ĐÁP ỨNG yêu cầu (RTO phút? RPO giây?)
function pick(needFastRTO: boolean, needLowRPO: boolean): string {
  if (needFastRTO && needLowRPO) return "Warm Standby (hoặc Active/Active nếu cần ~0)";
  if (needLowRPO) return "Pilot Light (DB replica liên tục)";
  return "Backup & Restore (rẻ nhất)";
}
console.log("\nVí dụ chọn theo yêu cầu nghiệp vụ:");
console.log(`  blog cá nhân (mất vài giờ OK)     → ${pick(false, false)}`);
console.log(`  app thương mại (mất vài phút data)→ ${pick(false, true)}`);
console.log(`  ngân hàng (gần như không downtime)→ ${pick(true, true)}`);
console.log("\nRTO/RPO càng ngặt → chi phí càng cao. Chọn theo tiền NGHIỆP VỤ mất khi down,");
console.log("không phải 'chọn cái xịn nhất'. (WA: các chiến lược khác nhau ở cost & complexity.)");
```

Kết quả chạy thật *(tất định)*:

```
Chiến lược DR               RTO          RPO       chi phí(×)
─────────────────────────────────────────────────────────────
Backup & Restore            nhiều giờ    nhiều giờ $
Pilot Light                 chục phút    phút      $$
Warm Standby                vài phút     giây      $$$$
Multi-site Active/Active    ~0 (tức thì) ~0        $$$$$$$$

Ví dụ chọn theo yêu cầu nghiệp vụ:
  blog cá nhân (mất vài giờ OK)     → Backup & Restore (rẻ nhất)
  app thương mại (mất vài phút data)→ Pilot Light (DB replica liên tục)
  ngân hàng (gần như không downtime)→ Warm Standby (hoặc Active/Active nếu cần ~0)

RTO/RPO càng ngặt → chi phí càng cao. Chọn theo tiền NGHIỆP VỤ mất khi down,
không phải 'chọn cái xịn nhất'. (WA: các chiến lược khác nhau ở cost & complexity.)
```

Bảng cho thấy chi phí tăng theo cấp (×1 → ×8) để đổi lấy RTO/RPO ngặt dần. Hàm `pick` nhấn insight cốt lõi: **chọn theo yêu cầu, không theo "cái xịn nhất"** — một blog trả tiền cho Active/Active là lãng phí, một ngân hàng chọn Backup & Restore là tự sát. Và dù chọn cái nào, nó phải **static stable** (mục 3): đường failover phải *đã chạy sẵn* (vd standby đã replicate liên tục), không phải thứ dựng gấp lúc Region chính đang cháy.

> [!note] Tự thử
> 1. Thêm cột "RPO phụ thuộc gì": vì sao RPO ≈ khoảng replication/backup? Nối về replication lag (cloud-base Bài 8).
> 2. Active/Active đa-vùng ghi *hai nơi cùng lúc*: vì sao nó đụng CAP (cloud-base Bài 8) và đồng hồ lệch (Bài 15)? Vì sao thường chọn active/passive để né?
> 3. Một hệ "static stable" chịu mất 1/3 AZ: vì sao phải chạy sẵn ở ~150% công suất, không phải 100%? (chi phí của static stability)

## 6. Soi Well-Architected

| Trụ | Thiết kế này | Ghi chú |
| :-- | :-- | :-- |
| Reliability | đa-AZ mặc định; đa-vùng theo RTO/RPO; static stable | test failover *thật* định kỳ (game day) |
| Performance | Active/Active phục vụ từ vùng gần người dùng | đánh đổi với nhất quán (CAP) |
| Cost | DR ngặt = đắt; static stability cần dư công suất | chọn chiến lược theo tiền-down thực |
| Security | replication mã hoá; IAM xuyên vùng | khoá KMS multi-region |
| Operational | runbook failover; nhưng ưu tiên tự động + static | RTO/RPO là KPI theo dõi (WA tr.38) |

## 7. Khép khoá: tám archetype, ba tầng

Bạn vừa đi hết tầng đỉnh. Nhìn lại, **mọi archetype chỉ là vài nguyên lý nền lặp lại** dưới vỏ bài toán khác nhau:

- **Hot key / sharding** (cloud-base Bài 9): partition key URL shortener (1), celebrity newsfeed (3), shuffle sharding (7).
- **Atomic / idempotency** (cloud-base Bài 2, 7, 16): atomic counter (1, 2), idempotent payment (5), retry an toàn (4).
- **Decouple async + queue** (cloud-base Bài 11): fan-out (3), hệ thông báo (4), xử lý ảnh (6).
- **Đánh đổi mạnh↔nới** (cloud-base Bài 5, 8): goodput vs throughput (2), eventual read (1), RTO/RPO vs cost (8), CAP đa-vùng (8).
- **Cô lập + fail rõ** (release-it, BL): load shedding (2), shuffle sharding (7), tránh fallback (7), static stability (8).

Và **một quy trình** (Bài 0) áp cho mọi bài: *ước lượng → kiến trúc → tìm nút thắt → đào sâu → soi Well-Architected*. Đó là toàn bộ khoá: không phải học thuộc kiến trúc, mà **suy ra** kiến trúc từ con số và nguyên lý. Ba tầng khép lại — [`cloud-base`](../../cloud-base/README.md) cho bạn *vì sao*, [`aws-fund`](../../aws-fund/README.md) cho *cái gì*, khoá này cho *làm sao cho đúng*.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — RTO vs RPO? Cái gì quyết hai con số này?
> **Đáp:** RTO = *bao lâu* phục hồi (downtime chịu được); RPO = *bao nhiêu dữ liệu gần nhất* được mất. Quyết bởi **tiền nghiệp vụ mất khi down**.

> [!question] Thẻ 8.2 — Vì sao "đa-AZ trước, đa-vùng sau"?
> **Đáp:** đa-AZ gần như miễn phí độ sẵn sàng (AWS thiết kế sẵn); đa-vùng đắt + kéo theo replication xuyên vùng (độ trễ, đồng hồ lệch, CAP) → chỉ khi nghiệp vụ thật đòi.

> [!question] Thẻ 8.3 — Static stability là gì? Bimodal là gì, vì sao nguy hiểm?
> **Đáp:** hệ đã có sẵn mọi thứ để chịu lỗi → khi lỗi **không cần làm gì mới**. Bimodal = hành xử khác giữa bình thường/sự cố → "chế độ sự cố" ít test, hỏng đúng lúc cần.

> [!question] Thẻ 8.4 — Bốn chiến lược DR theo thứ tự rẻ-chậm → đắt-nhanh?
> **Đáp:** Backup&Restore → Pilot Light → Warm Standby → Active/Active. RTO/RPO ngặt dần, chi phí tăng dần.

> [!question] Thẻ 8.5 — Vì sao "chọn Active/Active cho mọi hệ" là sai?
> **Đáp:** nó đắt nhất + phức tạp nhất (đụng CAP/đồng hồ đa-vùng). Chọn chiến lược **rẻ nhất đáp ứng RTO/RPO** của nghiệp vụ, không phải cái xịn nhất.

## 9. Câu hỏi tự kiểm tra

1. Định nghĩa RTO/RPO. Một ví dụ hệ cần mỗi cái gần 0, một ví dụ nới lỏng được. *(mục 1, WA tr. 38)*
2. Vì sao đa-AZ nên là mặc định còn đa-vùng là lựa chọn? *(mục 2)*
3. Static stability vs bimodal. Cho một ví dụ mỗi loại. *(mục 3, WA tr. 642)*
4. Bốn chiến lược DR: đánh đổi gì? Chạy lab §5 và giải thích hàm `pick`. *(mục 4–5, WA tr. 592)*
5. (Khép khoá) Chọn một archetype và truy nó về 2 nguyên lý nền cloud-base. *(mục 7)*

## Tóm tắt một trang

```
BÀI 8 — ĐA VÙNG & DISASTER RECOVERY (bài cuối)
─────────────────────────────────────────────────────────
RTO/RPO (WA tr.38)  RTO=bao lâu phục hồi; RPO=mất bao nhiêu dữ liệu gần nhất.
   Quyết bởi TIỀN nghiệp vụ mất khi down.

THỨ TỰ  đa-AZ TRƯỚC (gần miễn phí, AWS sẵn) → đa-VÙNG sau (đắt, kéo theo
   replication xuyên vùng: độ trễ/đồng hồ lệch/CAP — cloud-base Bài 8,15).

STATIC STABILITY (WA tr.642)  hệ đã sẵn mọi thứ chịu lỗi → khi lỗi KHÔNG làm
   gì mới. BIMODAL = hành xử khác lúc sự cố (ít test → hỏng đúng lúc cần).
   Đường phục hồi phải là đường ĐÃ CHẠY SẴN.

4 CHIẾN LƯỢC DR (WA tr.592)  Backup&Restore → Pilot Light → Warm Standby →
   Active/Active. RTO/RPO ngặt dần, chi phí ×1→×8. Chọn RẺ NHẤT đáp ứng, không
   phải cái xịn nhất.

KHÉP KHOÁ  8 archetype = vài nguyên lý nền lặp lại (hot key, atomic/idempotency,
   decouple async, đánh đổi mạnh↔nới, cô lập+fail rõ) + 1 quy trình (Bài 0).
   3 tầng: cloud-base (vì sao) → aws-fund (cái gì) → aws-design (làm sao cho đúng).
```

## Nguồn

- **AWS Well-Architected Framework** — Reliability: RTO/RPO (tr. 38), chiến lược DR khác nhau ở cost & complexity (tr. 592), static stability & bimodal (tr. 642). `tai_lieu/AWS-Well-Architected-Framework.pdf` (offset +5).
- Nền: [cloud-base Bài 8 (replication/CAP)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md), [Bài 3 (durability)](../../cloud-base/bai_hoc/bai_03_os-luu-tru.md), [Bài 15 (đồng hồ đa vùng)](../../cloud-base/bai_hoc/bai_15_dist-dong-ho.md).
- Dịch vụ: [aws-fund Bài 5 — Route 53 failover](../../aws-fund/bai_hoc/bai_05_networking.md), [Bài 3 — Multi-AZ RDS](../../aws-fund/bai_hoc/bai_03_database-storage.md).
- **Hết khoá `aws-design`.** Quay lại [Bài 0](bai_00_phuong-phap-system-design.md) với con mắt đã khác, hoặc tự dựng một archetype mới (chat realtime, search, analytics pipeline) theo đúng sáu bước.

---

**Bản đồ khoá học:** [Bài 0 — Phương pháp system design](bai_00_phuong-phap-system-design.md) · [Bài 1 — URL shortener](bai_01_url-shortener.md) · [Bài 2 — Rate limiter & load shedding](bai_02_rate-limiter.md) · [Bài 3 — Newsfeed & fan-out](bai_03_newsfeed-fanout.md) · [Bài 4 — Hệ thông báo tin cậy](bai_04_he-thong-bao.md) · [Bài 5 — Thanh toán idempotent](bai_05_thanh-toan-idempotent.md) · [Bài 6 — Upload & xử lý ảnh](bai_06_upload-xu-ly-anh.md) · [Bài 7 — Chịu traffic spike](bai_07_chiu-tai-overload.md) · **[Bài 8 — Đa vùng & DR] ← bạn đang ở đây** · [Phụ lục — Pattern (Wilder)](phu-luc-cloud-patterns.md)

Xem thêm [README khoá học](../README.md).
