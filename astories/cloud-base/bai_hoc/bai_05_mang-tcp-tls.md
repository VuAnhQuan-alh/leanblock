# Bài 5 — Mạng trụ 2b: TCP và TLS (đường ống đáng tin, và cái giá của nó)

> [!info] Về bài này
> **Trụ 2 (Mạng), mảnh 2/3.** [Bài 4](bai_04_mang-http-dns.md) nói HTTP dựa trên một "đường ống đáng tin" của tầng vận chuyển. Bài này mở nắp đường ống đó: **TCP** cho gì (tin cậy, đúng thứ tự, có kết nối) và **đổi lại bằng gì** — mỗi kết nối tốn một *bắt tay* = round-trip độ trễ; **TLS** (mã hoá) chồng thêm round-trip nữa. Đây là nền để hiểu vì sao **keep-alive, connection pooling, TLS termination ở ALB/CloudFront** lại đáng giá ở `aws-fund`.
> Nguồn: **Kurose** (TCP, ch. 3.5) + **HPBN** (handshake & round-trip, ch. 2 & 4).
> **Trích:** `Kurose (tr. X)` offset **+28**; `HPBN (tr. X)` offset **+18** (PDF 32 = tr. 14). Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 0 — bậc thang độ trễ](bai_00_vi-sao-nen-tang.md), [Bài 4 — phân tầng](bai_04_mang-http-dns.md).

## Mục lục

1. [TCP: đường ống đáng tin, có kết nối](#1-tcp-đường-ống-đáng-tin-có-kết-nối)
2. [Bắt tay ba bước: cái giá round-trip](#2-bắt-tay-ba-bước-cái-giá-round-trip)
3. [TLS: mã hoá, và round-trip chồng thêm](#3-tls-mã-hoá-và-round-trip-chồng-thêm)
4. [Demo: đếm round-trip, nhân với RTT](#4-demo-đếm-round-trip-nhân-với-rtt)
5. [Bảng so sánh: TCP vs UDP và chi phí bắt tay](#5-bảng-so-sánh-tcp-vs-udp-và-chi-phí-bắt-tay)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. TCP: đường ống đáng tin, có kết nối

HTTP ở Bài 4 chẳng bao giờ phải lo gói tin bị mất, tới sai thứ tự, hay trùng lặp. Nó dựa được vào một lời hứa của tầng dưới:

> [!quote] Kurose (tr. 227)
> "TCP—the Internet's transport-layer, connection-oriented, reliable transport protocol."
>
> *TCP — giao thức vận chuyển **có kết nối (connection-oriented)**, **đáng tin (reliable)** của tầng vận chuyển trên Internet.*

"Reliable" (đáng tin) nghĩa là: TCP dùng số thứ tự, biên nhận (ACK) và truyền lại để bảo đảm dữ liệu tới **đủ** và **đúng thứ tự** — dù tầng mạng (IP) bên dưới *không* hứa gì cả, gói có thể mất hay đảo lộn. TCP biến một tầng dưới hay hỏng thành một byte-stream sạch sẽ cho tầng trên. Đây lại là abstraction của Bài 1, lần này giấu đi sự bất định của mạng. Còn "connection-oriented" là nguồn gốc của cái giá bài này đo:

> [!quote] Kurose (tr. 228)
> "TCP is said to be connection-oriented because before one application process can begin to send data to another, the two processes must first "handshake" with each other—that is, they must send some preliminary segments to each other to establish the parameters of the ensuing data transfer."
>
> *TCP được gọi là **có kết nối** vì **trước khi** một tiến trình gửi dữ liệu cho tiến trình kia, hai bên phải **"bắt tay" (handshake)** — tức gửi cho nhau vài segment mở màn để **thống nhất tham số** cho đợt truyền sắp tới.*

## 2. Bắt tay ba bước: cái giá round-trip

Cái "handshake" đó có cấu trúc cụ thể — **three-way handshake**:

> [!quote] HPBN (tr. 14)
> "All TCP connections begin with a three-way handshake (Figure 2-1). Before the client or the server can exchange any application data, they must agree on starting packet sequence numbers, as well as a number of other connection specific variables, from both sides."
>
> *Mọi kết nối TCP bắt đầu bằng **bắt tay ba bước**. Trước khi client hay server trao đổi **bất kỳ** dữ liệu ứng dụng nào, hai bên phải thống nhất **số thứ tự gói khởi đầu** cùng một loạt biến riêng của kết nối, từ cả hai phía.*

Ba bước là **SYN → SYN-ACK → ACK**: client gửi SYN (số ngẫu nhiên `x`), server đáp SYN-ACK (`x+1`, kèm `y`), client gửi ACK (`y+1`). Chỉ sau đó dữ liệu mới chảy. Và đây là hệ quả định hình hiệu năng — nối thẳng về bậc thang độ trễ Bài 0:

> [!quote] HPBN (tr. 14)
> "each new connection will have a full roundtrip of latency before any application data can be transferred."
>
> *mỗi kết nối **mới** phải chịu **trọn một round-trip độ trễ** trước khi bất kỳ dữ liệu ứng dụng nào được truyền.*

Nhớ Bài 0: một round-trip cross-region ~70ms, bằng *~34 ngày* trên thang người. Bắt tay không chuyển lấy một byte dữ liệu — nó chỉ *chờ* ánh sáng đi-về. Vì thế một kết nối mới là thứ đắt đỏ, và né mở kết nối mới là mỏ vàng tối ưu.

## 3. TLS: mã hoá, và round-trip chồng thêm

HTTPS = HTTP chạy trên **TLS**. TLS cho bảo mật (mã hoá + xác thực danh tính server), nhưng cái giá là *thêm* round-trip trên nền bắt tay TCP đã có:

> [!quote] HPBN (tr. 65)
> "every TCP connection begins with a three-way handshake [...] which takes a full roundtrip for the SYN/SYN-ACK packets. Following that, the TLS handshake [...] requires up to two additional roundtrips for the full process, or one roundtrip if TLS session resumption [...] can be used."
>
> *mọi kết nối TCP mở đầu bằng bắt tay ba bước, tốn **trọn một round-trip** cho SYN/SYN-ACK. **Tiếp theo đó**, bắt tay TLS cần **tới hai round-trip nữa** cho toàn bộ quá trình, hoặc **một** round-trip nếu dùng được **TLS session resumption** (tái dùng phiên).*

Cộng dồn: một kết nối HTTPS *mới* có thể tốn **1 (TCP) + 2 (TLS) = 3 round-trip** chỉ để *sẵn sàng*, rồi mới thêm 1 round-trip nữa cho request. Trên link chậm, phần "chuẩn bị" này áp đảo cả việc truyền dữ liệu thật — đặc biệt với các request nhỏ. Hai lối thoát xuất hiện ngay trong chính câu trích: **session resumption** (giảm TLS còn 1 round-trip) và — mạnh hơn — **đừng mở kết nối mới**: tái dùng kết nối đã bắt tay. Demo mục 4 đo đúng khoảng cách này.

## 4. Demo: đếm round-trip, nhân với RTT

Handshake tốn *độ trễ*, mà độ trễ = số round-trip × RTT. Ta mô hình hoá "thời gian tới byte đầu" cho ba kiểu kết nối, ở hai mức RTT (cùng datacenter vs cross-region), rồi tính 100 request nhỏ: mở kết nối mới mỗi lần vs tái dùng một kết nối.

```typescript
// TCP/TLS: handshake tốn ROUND-TRIP, mà round-trip = latency (Bài 0).
// Mô hình thời-gian-tới-byte-đầu = (số round-trip bắt tay + 1 cho request) × RTT.
//  - HTTP mới   : 1 RT bắt tay TCP + 1 RT request          = 2 RTT
//  - HTTPS mới  : 1 RT TCP + 2 RT TLS + 1 RT request       = 4 RTT  (TLS 1.2)
//  - Tái dùng kết nối: 0 bắt tay + 1 RT request            = 1 RTT
type Kind = "HTTP mới" | "HTTPS mới" | "Tái dùng kết nối";
const ROUNDTRIPS: Record<Kind, number> = { "HTTP mới": 2, "HTTPS mới": 4, "Tái dùng kết nối": 1 };

function ttfbMs(kind: Kind, rttMs: number): number {
  return ROUNDTRIPS[kind] * rttMs;
}

const scenarios: Array<[string, number]> = [
  ["cùng datacenter (RTT≈1ms)", 1],
  ["cross-region (RTT≈70ms)", 70],
];

for (const [label, rtt] of scenarios) {
  console.log(`\n${label}:`);
  for (const kind of Object.keys(ROUNDTRIPS) as Kind[]) {
    console.log(`   ${kind.padEnd(18)} ${ROUNDTRIPS[kind]} RTT = ${ttfbMs(kind, rtt).toString().padStart(4)} ms tới byte đầu`);
  }
}

// 100 request nhỏ: mở kết nối mới mỗi lần vs tái dùng (cross-region)
const rtt = 70, N = 100;
const fresh = N * ttfbMs("HTTPS mới", rtt);
const reused = ttfbMs("HTTPS mới", rtt) + (N - 1) * ttfbMs("Tái dùng kết nối", rtt);
console.log(`\n${N} request HTTPS nhỏ qua link RTT ${rtt}ms:`);
console.log(`   mở kết nối mới mỗi lần : ${(fresh / 1000).toFixed(1)} s`);
console.log(`   tái dùng 1 kết nối     : ${(reused / 1000).toFixed(1)} s  (nhanh ~${(fresh / reused).toFixed(1)}x)`);
console.log(`\nHandshake không tốn byte — nó tốn ĐỘ TRỄ. Vì thế tái dùng kết nối là vàng.`);
```

Kết quả chạy thật *(mô hình tất định — con số là round-trip × RTT, không phải đo máy)*:

```

cùng datacenter (RTT≈1ms):
   HTTP mới           2 RTT =    2 ms tới byte đầu
   HTTPS mới          4 RTT =    4 ms tới byte đầu
   Tái dùng kết nối   1 RTT =    1 ms tới byte đầu

cross-region (RTT≈70ms):
   HTTP mới           2 RTT =  140 ms tới byte đầu
   HTTPS mới          4 RTT =  280 ms tới byte đầu
   Tái dùng kết nối   1 RTT =   70 ms tới byte đầu

100 request HTTPS nhỏ qua link RTT 70ms:
   mở kết nối mới mỗi lần : 28.0 s
   tái dùng 1 kết nối     : 7.2 s  (nhanh ~3.9x)

Handshake không tốn byte — nó tốn ĐỘ TRỄ. Vì thế tái dùng kết nối là vàng.
```

Trên link chậm, một HTTPS mới ngốn **280ms** *trước khi* nhận byte dữ liệu đầu tiên — gần như toàn bộ là chờ bắt tay. 100 request nhỏ mở mới mỗi lần mất **28 giây**; tái dùng một kết nối còn **7,2 giây**. Khác biệt không nằm ở băng thông (dữ liệu y hệt), mà ở số lần phải *chờ ánh sáng đi-về*. Đây chính xác là vì sao mọi client HTTP nghiêm túc đều bật keep-alive, và vì sao CDN/ALB giữ sẵn kết nối.

> [!note] Tự thử
> - Đổi mô hình TLS 1.2 (2 round-trip) sang **TLS 1.3** (1 round-trip): sửa `HTTPS mới` thành 3 RTT. Đó là một lý do lớn khiến nâng TLS 1.3 "miễn phí mà nhanh".
> - Thêm bước **DNS** (Bài 4) vào trước: +1 round-trip nữa nếu chưa cache. Giờ bạn thấy cả "đường đi của một request" xếp chồng round-trip ra sao.
> - Đo **thật**: dùng `http.Agent({ keepAlive: true })` cho 100 request tới một server localhost và so với `keepAlive:false`. Khác biệt localhost nhỏ (RTT≈0) — đúng như hàng "RTT≈1ms" ở trên: *handshake chỉ đắt khi link xa*.

## 5. Bảng so sánh: TCP vs UDP và chi phí bắt tay

Không phải lúc nào cũng cần "đáng tin". Tầng vận chuyển có hai lựa chọn, và chúng đánh đổi *độ tin cậy* lấy *độ trễ*:

| Tiêu chí           | TCP                               | UDP                                  |
| :----------------- | :-------------------------------- | :----------------------------------- |
| Kết nối            | có — bắt tay ba bước trước        | không — gửi thẳng                    |
| Độ tin cậy         | đủ, đúng thứ tự (ACK + truyền lại) | không hứa — có thể mất, đảo thứ tự   |
| Chi phí khởi động  | ≥1 round-trip (TCP) + ≥1 (nếu TLS) | ~0                                   |
| Hợp cho            | web, API, truyền file (cần đủ)    | DNS query, game, streaming (cần nhanh) |
| Nối về AWS         | ALB (L7), hầu hết API             | NLB (L4) cho UDP, Route 53 query     |

Quy luật rút ra: **"đáng tin" không miễn phí — nó mua bằng round-trip.** TCP trả trước một cái bắt tay để sau đó khỏi lo mất gói; UDP bỏ bắt tay để nhanh nhưng đẩy việc lo mất mát lên tầng ứng dụng. Đây là cùng một kiểu đánh đổi bạn sẽ gặp lại ở trụ Distributed (Bài 8): *nhất quán mạnh* cũng mua bằng round-trip phối hợp, còn *eventual consistency* là "UDP của dữ liệu".

## 6. Nối về AWS

> [!note] Nối về AWS
> Gần như mọi tối ưu mạng của AWS là một cách *né round-trip bắt tay* của bài này — xem [`aws-fund` Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md) và [Bài 6 — hiệu năng](bai_06_mang-hieu-nang.md):
> - **TLS termination ở ALB / CloudFront:** việc bắt tay TLS tốn-round-trip được làm **gần người dùng** (edge), nên 3 round-trip "chuẩn bị" chạy trên quãng ngắn thay vì xuyên lục địa. Backend phía sau nói HTTP nội bộ RTT≈0 — đúng hàng "cùng datacenter" của demo.
> - **Connection pooling / keep-alive** (SDK, RDS Proxy, HTTP client của Lambda): tái dùng kết nối đã bắt tay = hàng "Tái dùng kết nối" nhanh ~4x ở demo. **RDS Proxy** tồn tại phần lớn vì Lambda hay mở kết nối DB mới mỗi lần → trả giá bắt tay lặp lại.
> - **ALB (L7/TCP) vs NLB (L4)**: NLB chuyển cả **UDP** và giữ độ trễ cực thấp (ít can thiệp) — ứng với cột UDP ở bảng mục 5; ALB hiểu HTTP nên làm được định tuyến theo path nhưng ở tầng cao hơn.
> - **Vì sao cold start của Lambda (Bài 1) càng đau khi gọi service khác:** hàm vừa khởi tạo *chưa có kết nối nào* → request đầu phải trả trọn bắt tay TCP+TLS tới mỗi downstream. Giữ kết nối sống giữa các lần gọi (biến ngoài handler) là mẹo kinh điển.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — TCP cho hai tính chất gì? "Reliable" đạt bằng cách nào?
> **Đáp:** connection-oriented + reliable. "Reliable" = số thứ tự + ACK + truyền lại → dữ liệu tới đủ, đúng thứ tự, dù IP bên dưới không hứa gì.

> [!question] Thẻ 5.2 — Bắt tay ba bước gồm gì, và cái giá của nó?
> **Đáp:** SYN → SYN-ACK → ACK (thống nhất số thứ tự khởi đầu). Giá: **trọn một round-trip** trước khi truyền được byte dữ liệu nào.

> [!question] Thẻ 5.3 — HTTPS mới tốn tổng bao nhiêu round-trip để sẵn sàng?
> **Đáp:** 1 (TCP) + tới 2 (TLS 1.2) = tới 3 round-trip chuẩn bị, rồi +1 cho request. Session resumption / TLS 1.3 giảm phần TLS còn 1.

> [!question] Thẻ 5.4 — Vì sao tái dùng kết nối (keep-alive) nhanh hơn nhiều trên link xa?
> **Đáp:** bỏ được round-trip bắt tay (TCP+TLS); chỉ còn 1 round-trip request. Trên RTT cao, bắt tay áp đảo nên tiết kiệm lớn (~4x trong demo).

> [!question] Thẻ 5.5 — TCP vs UDP đánh đổi gì? UDP hợp khi nào?
> **Đáp:** TCP mua độ tin cậy bằng round-trip bắt tay + ACK; UDP bỏ cả hai để nhanh, chấp nhận mất/đảo gói. UDP hợp DNS query, game, streaming.

> [!question] Thẻ 5.6 — "TLS termination ở CloudFront" né được gì?
> **Đáp:** đưa bắt tay TLS (tốn round-trip) ra edge gần người dùng → 3 round-trip chuẩn bị chạy trên quãng ngắn, không xuyên lục địa.

## 8. Câu hỏi tự kiểm tra

1. TCP cho tầng trên hai tính chất gì? Giải thích "reliable" đạt ra sao khi IP không đáng tin. *(mục 1, tr. 227)*
2. Mô tả bắt tay ba bước. Vì sao nó tốn "a full roundtrip"? *(mục 2, tr. 14, 228)*
3. Một HTTPS mới tốn bao nhiêu round-trip để sẵn sàng? Tách rõ TCP và TLS. *(mục 3, tr. 65)*
4. Chạy demo mục 4. Vì sao khác biệt lớn ở cross-region mà nhỏ ở localhost? *(mục 4)*
5. TCP vs UDP: đánh đổi gì? Cho một ví dụ mỗi loại. *(mục 5)*
6. Ba cách AWS né round-trip bắt tay. Vì sao RDS Proxy tồn tại? *(mục 6)*

## Tóm tắt một trang

```
BÀI 5 — MẠNG TRỤ 2b: TCP · TLS (đường ống đáng tin + cái giá)
─────────────────────────────────────────────────────────
TCP  connection-oriented + reliable (tr.227). "Reliable" = seq# + ACK +
   truyền lại → đủ & đúng thứ tự, dù IP không hứa gì. Abstraction cho mạng.

BẮT TAY 3 BƯỚC  SYN→SYN-ACK→ACK (thống nhất seq# khởi đầu, tr.228).
   GIÁ: "full roundtrip trước khi truyền byte nào" (HPBN tr.14).
   Round-trip = ĐỘ TRỄ (Bài 0): cross-region ~70ms = ~34 ngày thang người.

TLS  mã hoá; thêm tới 2 round-trip NỮA trên nền TCP (tr.65).
   HTTPS mới = 1(TCP)+2(TLS)=3 RT chuẩn bị. Session resumption/TLS1.3 → 1.

DEMO  HTTPS mới cross-region 280ms tới byte đầu. 100 request nhỏ:
   mở mới mỗi lần 28s vs tái dùng 7.2s (~4x). Khác ở số lần CHỜ, không băng thông.

TCP vs UDP  "đáng tin" mua bằng round-trip; UDP bỏ bắt tay → nhanh, chấp
   nhận mất gói (DNS/game/streaming). = tiền đề consistency vs eventual (Bài 8).

NỐI VỀ AWS  TLS termination ở CloudFront/ALB (bắt tay ở edge); keep-alive/
   connection pool/RDS Proxy (né bắt tay lặp); NLB=L4/UDP; cold start đau vì
   chưa có kết nối nào.
```

## Nguồn

- **James F. Kurose & Keith W. Ross**, *Computer Networking: A Top-Down Approach, 8th* — **§3.5**: TCP connection-oriented, reliable (tr. 227–228). Offset **PDF = tr. + 28**.
- **Ilya Grigorik**, *High Performance Browser Networking* (O'Reilly, 2013) — **ch. 2**: three-way handshake, "full roundtrip" (tr. 14); **ch. 4**: TLS handshake round-trips (tr. 65). `tai_lieu/High Performance Browser Networking.pdf` — offset **PDF = tr. + 18** (PDF 32 = tr. 14).
- Nối về AWS: [`aws-fund` Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md).
- Tiếp: [Bài 6 — hiệu năng & CDN](bai_06_mang-hieu-nang.md) gom bậc thang độ trễ + round-trip lại thành bức tranh tối ưu.

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · **[Bài 5 — Mạng: TCP, TLS] ← bạn đang ở đây** · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
