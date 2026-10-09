# Bài 6 — Mạng trụ 2c: Hiệu năng (latency vs bandwidth) và CDN

> [!info] Về bài này
> **Trụ 2 (Mạng), mảnh 3/3 — khép trụ Mạng.** [Bài 0](bai_00_vi-sao-nen-tang.md) đo độ trễ, [Bài 5](bai_05_mang-tcp-tls.md) đếm round-trip bắt tay. Bài này gom lại thành một câu hỏi thực chiến: **cái gì làm web chậm — độ trễ hay băng thông?** Câu trả lời (của HPBN) định hình toàn bộ cách AWS làm mạng: vì sao **CloudFront / edge locations / Global Accelerator** tồn tại, và vì sao "mua ống to hơn" thường không cứu được.
> Nguồn: **HPBN** (latency/bandwidth, ch. 1) + **Kurose** (CDN, ch. 2.6).
> **Trích:** `HPBN (tr. X)` offset **+18**; `Kurose (tr. X)` offset **+28**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 0 — bậc thang độ trễ](bai_00_vi-sao-nen-tang.md), [Bài 5 — round-trip](bai_05_mang-tcp-tls.md).

## Mục lục

1. [Latency vs bandwidth: hai thước đo khác nhau](#1-latency-vs-bandwidth-hai-thước-đo-khác-nhau)
2. [Latency, không phải bandwidth, là nút thắt](#2-latency-không-phải-bandwidth-là-nút-thắt)
3. [CDN: đưa nội dung tới gần người dùng](#3-cdn-đưa-nội-dung-tới-gần-người-dùng)
4. [Demo: tải trang — latency-bound hay bandwidth-bound?](#4-demo-tải-trang-latency-bound-hay-bandwidth-bound)
5. [Bảng so sánh: hai cách tăng tốc](#5-bảng-so-sánh-hai-cách-tăng-tốc)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Latency vs bandwidth: hai thước đo khác nhau

Hai từ hay bị dùng lẫn, nhưng chúng đo hai thứ hoàn toàn khác:

> [!quote] HPBN (tr. 2)
> "Latency: The time from the source sending a packet to the destination receiving it. Bandwidth: Maximum throughput of a logical or physical communication path."
>
> ***Latency (độ trễ):** thời gian từ lúc nguồn gửi một gói tới lúc đích nhận được nó. **Bandwidth (băng thông):** thông lượng **tối đa** của một đường truyền logic hoặc vật lý.*

Ẩn dụ đường ống nước: **latency** là *bao lâu* giọt nước đầu tiên đi hết ống; **bandwidth** là ống *to* cỡ nào (bao nhiêu nước mỗi giây). Ống to hơn (nhiều bandwidth) không làm giọt đầu tiên tới nhanh hơn — quãng đường vẫn thế. Và latency có một trần vật lý không thể thương lượng: tốc độ ánh sáng. Cáp quang xuyên Đại Tây Dương nhanh cỡ nào cũng không thắng được `khoảng cách / tốc độ ánh sáng` — đó là lý do một round-trip cross-region ~70ms (Bài 0) là *sàn cứng*, không phải vấn đề kỹ thuật chờ sửa.

## 2. Latency, không phải bandwidth, là nút thắt

Đây là câu luận đề của cả bài, và nó phản trực giác với hầu hết mọi người (vốn nghĩ "mạng chậm = cần gói cước mạnh hơn"):

> [!quote] HPBN (tr. 9)
> "Latency, not bandwidth, is the performance bottleneck for most websites!"
>
> ***Độ trễ, không phải băng thông**, mới là nút thắt hiệu năng của **đa số website**!*

Vì sao? Một trang web hiện đại không phải *một* khối dữ liệu lớn chảy qua ống, mà là **hàng chục yêu cầu nhỏ** (HTML, CSS, JS, ảnh, font...) nối tiếp nhau, mỗi yêu cầu phải *chờ* một vòng đi-về. Nhớ Bài 5: mỗi kết nối tốn round-trip bắt tay; mỗi request thêm round-trip nữa. Với nhiều object nhỏ, thời gian bị **round-trip chi phối**, không phải độ to của ống. Băng thông chỉ giúp khi bạn chuyển một *khối lớn* (tải video, backup) — lúc đó mới "bandwidth-bound". Demo mục 4 cho thấy ranh giới này bằng con số, và vì sao tăng băng thông chạm một cái sàn mà nó không vượt qua được.

## 3. CDN: đưa nội dung tới gần người dùng

Nếu nút thắt là latency, và latency bị chặn bởi *khoảng cách*, thì cách tấn công hiển nhiên là: **rút ngắn khoảng cách**. Đó đúng là điều CDN làm:

> [!quote] Kurose (tr. 146)
> "A CDN manages servers in [...] multiple geographically distributed locations, stores copies of the videos (and other types of Web content, including documents, images, and audio) in its servers, and attempts to direct each user request to a CDN location that will provide the best user experience."
>
> *Một **CDN** quản lý các server ở **nhiều vị trí phân tán về mặt địa lý**, lưu **bản sao** của video (và nội dung Web khác: tài liệu, ảnh, âm thanh) trong các server đó, và cố **lái mỗi yêu cầu người dùng tới vị trí CDN cho trải nghiệm tốt nhất** (thường là gần nhất).*

CDN không làm ống to hơn — nó làm **quãng đường ngắn hơn**. Thay vì mỗi người dùng với tới origin tận bên kia địa cầu (RTT cao), họ chạm một edge server cách vài chục km (RTT thấp). Đây cũng là một dạng *nhân bản* (Bài 3, tầng 3 durability) nhưng mục tiêu là *gần* chứ không chỉ là *bền*. Và nó hé lộ trụ tiếp theo: một khi có nhiều bản sao ở nhiều nơi, ta lại gặp bài toán *giữ các bản sao nhất quán* — trụ Distributed (Bài 7–8).

## 4. Demo: tải trang, latency-bound hay bandwidth-bound?

Mô hình một trang gồm 50 tài nguyên nhỏ (10KB mỗi cái), tải qua 6 kết nối song song. Thời gian ≈ *phần latency* (số đợt round-trip × RTT) + *phần truyền* (tổng byte ÷ băng thông). Rồi thử bốn cấu hình: gốc, tăng băng thông 2×/10×, và CDN (giảm RTT còn 1/5).

```typescript
// "Latency, not bandwidth, is the bottleneck" (HPBN tr.9).
// Mô hình tải một trang = R tài nguyên nhỏ, tải 6 kết nối song song.
//   thời gian ≈ (1 handshake + số "đợt" request) × RTT   [phần LATENCY]
//              + tổng_byte × 8 / bandwidth                 [phần BANDWIDTH]
const R = 50;                 // số tài nguyên (html + css + js + ảnh nhỏ...)
const BYTES_EACH = 10_000;    // ~10 KB mỗi cái
const PARALLEL = 6;           // số kết nối song song của trình duyệt
const totalBytes = R * BYTES_EACH;

function loadMs(rttMs: number, bwMbps: number): { total: number; lat: number; bw: number } {
  const waves = Math.ceil(R / PARALLEL);
  const lat = (1 + waves) * rttMs;                      // handshake + các đợt
  const bw = (totalBytes * 8) / (bwMbps * 1e6) * 1000;  // ms truyền hết byte
  return { total: lat + bw, lat, bw };
}

const show = (name: string, rtt: number, bw: number) => {
  const r = loadMs(rtt, bw);
  console.log(`${name.padEnd(26)} RTT ${String(rtt).padStart(3)}ms, ${String(bw).padStart(2)}Mbps` +
    ` → ${r.total.toFixed(0).padStart(4)}ms  (latency ${r.lat.toFixed(0)} + truyền ${r.bw.toFixed(0)})`);
};

console.log(`Trang: ${R} tài nguyên × ${BYTES_EACH / 1000}KB = ${totalBytes / 1000}KB, ${PARALLEL} kết nối song song\n`);
show("Gốc (origin xa)", 100, 5);
show("  → tăng băng thông 2x", 100, 10);
show("  → tăng băng thông 10x", 100, 50);
show("  → CDN: RTT còn 1/5", 20, 5);
console.log(`\nBăng thông chỉ bào được phần "truyền"; tăng mãi cũng CHẠM SÀN = latency`);
console.log(`(1000ms) và không xuống nổi nữa. CDN tấn công chính cái sàn đó (RTT nhỏ).`);
console.log(`→ vì sao CloudFront đưa nội dung tới gần người dùng thay vì chỉ "ống to hơn".`);
```

Kết quả chạy thật *(mô hình tất định)*:

```
Trang: 50 tài nguyên × 10KB = 500KB, 6 kết nối song song

Gốc (origin xa)            RTT 100ms,  5Mbps → 1800ms  (latency 1000 + truyền 800)
  → tăng băng thông 2x     RTT 100ms, 10Mbps → 1400ms  (latency 1000 + truyền 400)
  → tăng băng thông 10x    RTT 100ms, 50Mbps → 1080ms  (latency 1000 + truyền 80)
  → CDN: RTT còn 1/5       RTT  20ms,  5Mbps → 1000ms  (latency 200 + truyền 800)

Băng thông chỉ bào được phần "truyền"; tăng mãi cũng CHẠM SÀN = latency
(1000ms) và không xuống nổi nữa. CDN tấn công chính cái sàn đó (RTT nhỏ).
→ vì sao CloudFront đưa nội dung tới gần người dùng thay vì chỉ "ống to hơn".
```

Đọc kỹ: tăng băng thông **10×** (5→50 Mbps) chỉ hạ 1800→1080ms — phần "truyền" co từ 800 xuống 80ms rồi **kẹt** ở cái sàn 1000ms của latency; dù ống to tới đâu nữa cũng không xuống dưới 1000. Trong khi CDN cắt RTT còn 1/5 lập tức hạ phần latency 1000→200ms. Đây chính là phát biểu HPBN mục 2, hiện thành số: với trang nhiều object nhỏ, *độ trễ* là trần, và chỉ cách **rút ngắn khoảng cách** (CDN) mới chọc thủng trần đó.

> [!note] Tự thử
> - Đổi trang thành **một file lớn** (`R=1`, `BYTES_EACH=50_000_000` — một video 50MB): giờ nó *bandwidth-bound*, tăng băng thông ăn tiền, CDN ít giúp phần truyền. Đó là ranh giới latency-bound ↔ bandwidth-bound.
> - Tăng `R` (nhiều tài nguyên hơn): phần latency phình to → trang càng "nhiều mảnh nhỏ" càng latency-bound. Đây là lý do **gộp/giảm số request** (bundling, HTTP/2 multiplexing) là tối ưu lớn.
> - Mô hình hoá HTTP/2: bỏ giới hạn `PARALLEL` (một kết nối chở nhiều stream) → `waves` giảm. Thấy vì sao HTTP/2 nhanh mà không cần thêm băng thông.

## 5. Bảng so sánh: hai cách tăng tốc

Khi ai đó nói "làm web nhanh hơn", họ đang chọn một trong hai mặt trận — và chọn sai mặt trận là phí tiền:

| Mặt trận          | Tấn công vào         | Hiệu quả khi…                   | Công cụ điển hình / AWS                       |
| :---------------- | :------------------- | :------------------------------ | :-------------------------------------------- |
| **Giảm latency**  | số round-trip × RTT  | trang nhiều object nhỏ (đa số)  | CDN gần (CloudFront), keep-alive, HTTP/2, caching |
| **Tăng bandwidth** | byte ÷ thông lượng  | truyền khối lớn (video, backup) | ống to hơn, nén (gzip/brotli)                 |

Hai đòn bẩy phụ nhưng mạnh, đều *giảm latency gián tiếp*: **caching** (không request thì không tốn round-trip nào) và **giảm số request** (gộp file, HTTP/2 multiplexing — ít đợt hơn). Quy luật cuối cùng: **round-trip rẻ nhất là round-trip không phải thực hiện.** Cache ở edge, tái dùng kết nối, gộp request — tất cả đều là biến thể của ý đó.

## 6. Nối về AWS

> [!note] Nối về AWS
> Toàn bộ "mạng biên" của AWS là hiện thực của bài này — xem [`aws-fund` Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md):
> - **CloudFront = CDN** của mục 3, do AWS vận hành với hàng trăm *edge location*. Nó tấn công đúng cái "sàn latency" của demo: phục vụ nội dung tĩnh (và cả động, qua cache) từ điểm gần người dùng, kèm **TLS termination ở edge** (Bài 5) để bắt tay chạy trên quãng ngắn.
> - **"Mua ống to hơn" hiếm khi là câu trả lời.** Khi trang chậm ở vùng xa, nâng băng thông instance không cứu được (nó latency-bound) — câu trả lời là đưa nội dung/điểm cuối tới gần: CloudFront, **Global Accelerator** (định tuyến qua xương sống AWS, giảm RTT), hoặc triển khai đa vùng.
> - **Caching là đòn latency rẻ nhất:** CloudFront cache, **ElastiCache** (né round-trip tới DB), **DAX** (cache trước DynamoDB). Mỗi tầng cache là một round-trip *không phải thực hiện* — đúng "round-trip rẻ nhất là round-trip không làm".
> - **Chọn mặt trận đúng:** API nhiều lời gọi nhỏ, chéo-service → latency-bound → gộp request, đặt gần nhau (cùng AZ/region), cache. Truyền file/analytics khối lớn → bandwidth-bound → nén, chọn instance mạng cao. Chẩn đoán sai mặt trận = đốt tiền sai chỗ.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — Latency và bandwidth đo hai thứ gì khác nhau? Ẩn dụ?
> **Đáp:** latency = *bao lâu* gói đi từ nguồn tới đích; bandwidth = thông lượng *tối đa* của đường. Ẩn dụ ống nước: latency = thời gian giọt đầu đi hết ống; bandwidth = ống to cỡ nào.

> [!question] Thẻ 6.2 — Luận đề HPBN về nút thắt hiệu năng web?
> **Đáp:** "**Latency, not bandwidth**, là nút thắt của đa số website" — vì trang là nhiều object nhỏ, mỗi cái chờ round-trip; thời gian bị round-trip chi phối.

> [!question] Thẻ 6.3 — Vì sao tăng băng thông chạm một "cái sàn"?
> **Đáp:** băng thông chỉ bào được phần *truyền byte*; phần *latency* (số round-trip × RTT) không đổi theo băng thông → tổng không xuống dưới cái sàn latency đó.

> [!question] Thẻ 6.4 — CDN tăng tốc bằng cách nào? Khác "ống to hơn" ở đâu?
> **Đáp:** lưu bản sao ở nhiều vị trí địa lý, lái request tới nơi gần nhất → **rút ngắn khoảng cách = giảm RTT = giảm latency**. Không làm ống to, mà làm quãng đường ngắn.

> [!question] Thẻ 6.5 — "Round-trip rẻ nhất là gì"? Ba cách hiện thực?
> **Đáp:** round-trip **không phải thực hiện**. Hiện thực: caching (edge/ElastiCache/DAX), tái dùng kết nối (keep-alive), giảm số request (bundling, HTTP/2).

> [!question] Thẻ 6.6 — Khi nào bandwidth mới là mặt trận đúng?
> **Đáp:** khi truyền **khối lớn** (video, backup, analytics) — lúc đó bandwidth-bound. Trang nhiều object nhỏ thì latency-bound → chọn giảm latency.

## 8. Câu hỏi tự kiểm tra

1. Định nghĩa latency và bandwidth. Vì sao latency có trần vật lý? *(mục 1, tr. 2)*
2. Phát biểu luận đề HPBN. Vì sao đa số web là latency-bound chứ không bandwidth-bound? *(mục 2, tr. 9)*
3. CDN là gì (theo Kurose)? Nó tấn công latency bằng cơ chế nào? *(mục 3, tr. 146)*
4. Chạy demo mục 4. Vì sao tăng băng thông 10× vẫn kẹt ở 1080ms? CDN hạ được nhờ đâu? *(mục 4)*
5. Hai mặt trận tăng tốc. Cho một tình huống mỗi mặt trận là đúng. *(mục 5)*
6. Vì sao "mua ống to hơn" thường không cứu web chậm ở vùng xa? AWS giải quyết bằng gì? *(mục 6)*

## Tóm tắt một trang

```
BÀI 6 — MẠNG TRỤ 2c: HIỆU NĂNG (latency vs bandwidth) · CDN
─────────────────────────────────────────────────────────
LATENCY  thời gian gói đi nguồn→đích (tr.2). Trần vật lý = tốc độ ánh sáng.
BANDWIDTH  thông lượng tối đa của đường (ống to cỡ nào).
   Ống to KHÔNG làm giọt đầu tới nhanh hơn.

LUẬN ĐỀ  "Latency, NOT bandwidth, is the bottleneck for most websites" (tr.9).
   Trang = nhiều object nhỏ, mỗi cái chờ round-trip → round-trip chi phối.

CDN  lưu bản sao ở nhiều vị trí địa lý, lái request tới nơi gần nhất (Kurose
   tr.146) → rút ngắn KHOẢNG CÁCH = giảm RTT. Không làm ống to.

DEMO  trang 50 object: băng thông 10x → 1800→1080ms rồi KẸT ở sàn latency
   1000ms. CDN RTT/5 → latency 1000→200. Chỉ rút khoảng cách mới chọc sàn.

2 MẶT TRẬN  giảm latency (CDN/keep-alive/HTTP2/cache — trang nhỏ, đa số)
   vs tăng bandwidth (nén — khối lớn: video/backup). Chọn sai = đốt tiền.
   "Round-trip rẻ nhất là round-trip KHÔNG phải làm" → cache.

NỐI VỀ AWS  CloudFront=CDN+TLS ở edge; Global Accelerator giảm RTT;
   ElastiCache/DAX né round-trip tới DB; chẩn đoán đúng mặt trận.
```

## Nguồn

- **Ilya Grigorik**, *High Performance Browser Networking* (O'Reilly, 2013) — **ch. 1**: định nghĩa latency & bandwidth (tr. 2), "latency, not bandwidth, is the bottleneck" (tr. 9). Offset **PDF = tr. + 18**.
- **James F. Kurose & Keith W. Ross**, *Computer Networking: A Top-Down Approach, 8th* — **§2.6**: định nghĩa CDN (tr. 146). Offset **PDF = tr. + 28**.
- Nối về AWS: [`aws-fund` Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md) (CloudFront, caching).
- Khép trụ 2 (Mạng). Tiếp trụ 3 (Distributed): [Bài 7 — giao tiếp & thất bại](bai_07_dist-giao-tiep.md) — một khi có nhiều bản sao ở nhiều nơi (CDN, replica), bài toán *giữ chúng nhất quán* bắt đầu.

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · **[Bài 6 — Mạng: hiệu năng, CDN] ← bạn đang ở đây** · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
