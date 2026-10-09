# Bài 4 — Mạng trụ 2a: Phân tầng, HTTP, DNS

> [!info] Về bài này
> **Trụ 2 (Mạng), mảnh 1/3.** Trụ 1 (OS) lo *một máy*; từ đây các máy nói chuyện với nhau. Bài này nắm ba nền của tầng ứng dụng: **mô hình phân tầng** (vì sao Internet chia 5 lớp), **HTTP** (giao thức Web — và vì sao nó *stateless*), **DNS** (dịch tên → IP). Ba thứ này là bản chất của **Route 53, API Gateway/ALB, và VPC** ở `aws-fund`.
> Nguồn: **Kurose & Ross** — *Computer Networking: A Top-Down Approach, 8th* (ch. 1.5 layering; 2.2 HTTP; 2.4 DNS).
> **Trích:** `Kurose (tr. X)` = trang **in**; **offset PDF = tr. + 28** (PDF 78 = tr. 50). Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 0 — bậc thang độ trễ](bai_00_vi-sao-nen-tang.md) (mạng ~triệu lần chậm hơn RAM — nền của cả trụ 2).

## Mục lục

1. [Phân tầng: vì sao Internet chia 5 lớp](#1-phân-tầng-vì-sao-internet-chia-5-lớp)
2. [HTTP: giao thức của Web](#2-http-giao-thức-của-web)
3. [Stateless: vì sao server không nhớ bạn](#3-stateless-vì-sao-server-không-nhớ-bạn)
4. [DNS: danh bạ phân tán của Internet](#4-dns-danh-bạ-phân-tán-của-internet)
5. [Demo: server stateless, state do client mang](#5-demo-server-stateless-state-do-client-mang)
6. [Bảng so sánh: năm tầng và vai trò](#6-bảng-so-sánh-năm-tầng-và-vai-trò)
7. [Nối về AWS](#7-nối-về-aws)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Phân tầng: vì sao Internet chia 5 lớp

Internet phức tạp khủng khiếp, nhưng nó được chế ngự bằng **một** ý tưởng: chia chức năng thành các **tầng (layer)** xếp chồng, mỗi tầng chỉ nói chuyện với tầng ngay trên/dưới qua một giao diện rõ ràng.

> [!quote] Kurose (tr. 50)
> "When taken together, the protocols of the various layers are called the protocol stack. The Internet protocol stack consists of five layers: the physical, link, network, transport, and application layers."
>
> *Gộp lại, các giao thức của những tầng khác nhau gọi là **protocol stack**. Ngăn xếp giao thức Internet gồm **năm tầng**: vật lý (physical), liên kết (link), mạng (network), vận chuyển (transport), và ứng dụng (application).*

Đây đúng là tư tưởng *abstraction* của Bài 1 áp lên mạng: tầng ứng dụng (HTTP của bạn) **không cần biết** gói tin đi bằng cáp quang hay Wi-Fi; tầng vật lý **không cần biết** nó chở HTTP hay email. Mỗi tầng bán cho tầng trên một ảo giác "đường ống sạch" và giấu đi mọi rối rắm bên dưới. Cả khoá leo đúng theo thang này: Bài 4 ở tầng ứng dụng (HTTP/DNS), Bài 5 xuống tầng vận chuyển (TCP/TLS), Bài 6 lo hiệu năng xuyên tầng.

```
   TẦNG            VÍ DỤ GIAO THỨC        "Đơn vị" dữ liệu
   ───────────────────────────────────────────────────────
   5 Application   HTTP, DNS, SMTP        message   ← Bài 4
   4 Transport     TCP, UDP               segment   ← Bài 5
   3 Network       IP                     datagram
   2 Link          Ethernet, Wi-Fi        frame
   1 Physical      (bit trên dây/sóng)    bit
   ───────────────────────────────────────────────────────
   Mỗi tầng dưới "bọc" (encapsulate) dữ liệu tầng trên thêm một lớp header.
```

## 2. HTTP: giao thức của Web

Lên đỉnh ngăn xếp là tầng ứng dụng, nơi có giao thức bạn chạm vào hằng ngày:

> [!quote] Kurose (tr. 95)
> "The HyperText Transfer Protocol (HTTP), the Web's application-layer protocol, is at the heart of the Web. It is defined in [RFC 1945], [RFC 7230] and [RFC 7540]. HTTP is implemented in two programs: a client program and a server program."
>
> ***HTTP** — giao thức tầng ứng dụng của Web — nằm ở trái tim của Web. HTTP được hiện thực bằng **hai chương trình**: một **client** và một **server**; hai bên chạy trên các máy khác nhau, trao đổi **HTTP message** để nói chuyện.*

HTTP chỉ quy định *cấu trúc message* (request/response) và *cách trao đổi* chúng. Nó không quan tâm bên dưới là TCP hay gì — đúng tinh thần phân tầng mục 1. Nhưng nó có một tính chất định hình toàn bộ kiến trúc web hiện đại: **stateless**.

## 3. Stateless: vì sao server không nhớ bạn

> [!quote] Kurose (tr. 98)
> "Because an HTTP server maintains [...] no information about the clients, HTTP is said to be a stateless protocol."
>
> *Vì một HTTP server **không giữ thông tin gì về client**, HTTP được gọi là giao thức **stateless (vô trạng thái)**.*

Kurose minh hoạ sắc: nếu cùng một client xin cùng một object hai lần cách nhau vài giây, server **không** nói "tôi vừa đưa anh cái này rồi" — nó gửi lại, vì đã *quên sạch* điều nó làm trước đó. Mỗi request được xử lý độc lập, như thể là request đầu tiên.

Vì sao thiết kế "đãng trí" này lại thắng? Vì nó khiến server **dễ nhân bản theo chiều ngang**: nếu server không nhớ gì, thì request kế tiếp của bạn gửi tới *server nào cũng được* — chúng giống hệt nhau. Đây chính là nền móng để một load balancer rải tải cho hàng nghìn server, và là lý do bạn sẽ thấy ở mục 7: muốn "nhớ" (đăng nhập, giỏ hàng) thì state phải nằm ở nơi *khác* — trong token client mang theo, hoặc trong một DB chia sẻ. Demo mục 5 cho thấy điều đó bằng tay.

## 4. DNS: danh bạ phân tán của Internet

Con người nhớ `www.amazon.com`; router cần IP dạng số. Cầu nối là DNS:

> [!quote] Kurose (tr. 123)
> "The DNS is (1) a distributed database implemented in a hierarchy of DNS servers, and (2) an application-layer protocol that allows hosts to query the distributed database."
>
> *DNS là (1) một **cơ sở dữ liệu phân tán** hiện thực bằng một **hệ phân cấp các DNS server**, và (2) một **giao thức tầng ứng dụng** cho phép host **truy vấn** cái cơ sở dữ liệu phân tán ấy.*

Hai chữ then chốt: **phân tán** và **phân cấp**. Không một máy nào giữ toàn bộ danh bạ Internet — điều đó bất khả thi về quy mô lẫn độ tin cậy. Thay vào đó, việc tra được chuyền tay theo cây: **root** → **TLD** (`.com`) → **authoritative** (`amazon.com`). DNS vì thế là ví dụ *distributed system* đầu tiên bạn gặp trong khoá (báo trước trụ 3), và là lý do khái niệm này quan trọng: nó vừa phân tán để chịu tải/chịu lỗi, vừa phân cấp để chia nhỏ trách nhiệm quản trị.

## 5. Demo: server stateless, state do client mang

Để "stateless" thôi hết trừu tượng: dựng một HTTP server **không hề có biến đếm theo client**. Nó chỉ đọc con số client gửi lên, cộng 1, trả về. Rồi cho hai client gọi: một client "quên" (không mang gì theo), một client "nhớ" (mang con số lần trước lên request sau).

```typescript
// HTTP là STATELESS: server không giữ ký ức gì giữa các request. Mọi "trạng
// thái" (bạn là ai, đã ghé mấy lần) phải do CLIENT mang theo trong mỗi request.
// Demo: cùng một server, hai client — một "quên", một "nhớ mang theo".
import http from "node:http";

// Server KHÔNG có biến đếm theo client. Nó chỉ đọc count client gửi lên,
// cộng 1, trả về. Toàn bộ "phiên" sống trong cái client tự mang.
const server = http.createServer((req, res) => {
  const carried = Number(req.headers["x-visit-count"] ?? 0);
  const next = carried + 1;
  res.setHeader("x-visit-count", String(next)); // "cookie" tối giản
  res.end(`Đây là lần ghé thứ ${next} của bạn (theo thứ bạn mang lên).`);
});

function call(headers: Record<string, string>): Promise<{ body: string; count: string }> {
  return new Promise((resolve) => {
    const req = http.get({ host: "127.0.0.1", port: 8731, headers }, (res) => {
      let b = ""; res.on("data", (c) => (b += c));
      res.on("end", () => resolve({ body: b, count: String(res.headers["x-visit-count"]) }));
    });
  });
}

const main = async (): Promise<void> => {
  await new Promise<void>((r) => server.listen(8731, r));

  console.log("CLIENT A — 'quên' (không mang state theo):");
  for (let i = 0; i < 3; i++) console.log("   " + (await call({})).body);

  console.log("\nCLIENT B — 'nhớ' (mang x-visit-count của lần trước lên):");
  let carried = "0";
  for (let i = 0; i < 3; i++) {
    const r = await call({ "x-visit-count": carried });
    console.log("   " + r.body);
    carried = r.count; // client tự giữ state, không phải server
  }

  console.log("\nServer không hề có bộ đếm. Client A luôn 'lần 1' vì không mang gì.");
  console.log("Client B đếm được 1→2→3 vì TỰ mang state theo mỗi request.");
  server.close();
};
main();
```

Kết quả chạy thật *(tất định)*:

```
CLIENT A — 'quên' (không mang state theo):
   Đây là lần ghé thứ 1 của bạn (theo thứ bạn mang lên).
   Đây là lần ghé thứ 1 của bạn (theo thứ bạn mang lên).
   Đây là lần ghé thứ 1 của bạn (theo thứ bạn mang lên).

CLIENT B — 'nhớ' (mang x-visit-count của lần trước lên):
   Đây là lần ghé thứ 1 của bạn (theo thứ bạn mang lên).
   Đây là lần ghé thứ 2 của bạn (theo thứ bạn mang lên).
   Đây là lần ghé thứ 3 của bạn (theo thứ bạn mang lên).

Server không hề có bộ đếm. Client A luôn 'lần 1' vì không mang gì.
Client B đếm được 1→2→3 vì TỰ mang state theo mỗi request.
```

Client A mãi "lần 1" vì server *thật sự* không nhớ gì về nó. Client B đếm được 1→2→3 không phải vì server thông minh hơn, mà vì **client tự mang state theo**. Cookie, session token, JWT — tất cả chỉ là những phiên bản chỉn chu của cái `x-visit-count` này: cơ chế để nhét state vào một giao thức cố tình quên. Và vì server vẫn không nhớ gì, bạn có thể đặt *mười* server giống hệt sau một load balancer — request của B tới cái nào cũng ra kết quả đúng.

> [!note] Tự thử
> - Chạy *hai* tiến trình server trên hai cổng rồi cho Client B gọi luân phiên hai cổng: vẫn đếm đúng 1→2→3. Đó chính là *vì sao* stateless cho phép scale ngang.
> - Nếu server *có* lưu `Map<clientId, count>`: nó thành *stateful* — và request của B **buộc** phải về đúng server đang giữ Map đó (sticky session), mất tự do rải tải.
> - Thay `x-visit-count` bằng một chuỗi ký (hmac) để client không tự chế được số: đó đúng là bước từ "cookie thô" tiến tới "JWT có chữ ký".

## 6. Bảng so sánh: năm tầng và vai trò

| Tầng (trên→dưới) | Lo việc gì                              | Giao thức tiêu biểu | Địa chỉ dùng         | Nối về AWS         |
| :--------------- | :-------------------------------------- | :------------------ | :------------------- | :----------------- |
| Application      | ngữ nghĩa ứng dụng (lấy trang, tra tên) | HTTP, DNS, SMTP     | URL, hostname        | API GW, Route 53   |
| Transport        | chuyển *đáng tin* giữa hai tiến trình   | TCP, UDP            | số cổng (port)       | (Bài 5) ALB, NLB   |
| Network          | định tuyến gói **xuyên** các mạng       | IP                  | địa chỉ IP           | VPC, subnet, route |
| Link             | chuyển qua **một** chặng kề nhau        | Ethernet, Wi-Fi     | MAC                  | ENI (card mạng ảo) |
| Physical         | bit thành tín hiệu trên dây/sóng        | —                   | —                    | (hạ tầng AWS lo)   |

Đọc bảng từ góc "mỗi tầng giấu gì cho tầng trên": HTTP (app) tin rằng có một đường ống đáng tin — đó là lời hứa TCP (transport, Bài 5); TCP tin rằng gói sẽ tới được máy đích — đó là việc IP (network) lo, dù IP *không* hứa gì về thứ tự hay mất mát. Chính sự phân vai này là lý do bạn lập trình HTTP mà chẳng bao giờ phải nghĩ tới Wi-Fi hay cáp quang.

## 7. Nối về AWS

> [!note] Nối về AWS
> Ba khái niệm bài này là xương sống của tầng mạng trong `aws-fund` — xem [Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md):
> - **Route 53 = DNS managed.** Nó chính là "(1) distributed database + (2) application-layer protocol" của mục 4, do AWS vận hành: bạn tạo *hosted zone*, thêm *record* (A, CNAME, Alias) — tức là ghi vào danh bạ phân cấp. *Health-check routing* của Route 53 lợi dụng đúng việc tra-tên-mỗi-lần để lái traffic khỏi vùng hỏng.
> - **API Gateway / ALB = điểm cuối HTTP.** Chúng hiểu request/response HTTP của mục 2 và định tuyến theo path/host.
> - **Stateless là điều kiện để auto-scaling chạy.** Lambda và container sau ALB *phải* stateless (mục 3) thì AWS mới thoải mái thêm/bớt bản sao theo tải. Muốn giữ state → đẩy ra **DynamoDB/ElastiCache** (DB chia sẻ) hoặc **JWT** (client mang theo) — đúng hai lối thoát của demo mục 5.
> - **Năm tầng ↔ VPC:** subnet/route table/IGW của VPC là tầng *network* (IP); security group lọc theo *port* là tầng *transport*; còn bạn code ở tầng *application*. Hiểu phân tầng rồi, sơ đồ VPC hết rối.

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — Năm tầng của Internet protocol stack, từ trên xuống?
> **Đáp:** Application → Transport → Network → Link → Physical. Mỗi tầng giấu chi tiết tầng dưới, bán "đường ống sạch" cho tầng trên.

> [!question] Thẻ 4.2 — HTTP là gì, gồm mấy chương trình?
> **Đáp:** giao thức tầng ứng dụng của Web; hai chương trình (client + server) trao đổi HTTP message; HTTP chỉ quy định cấu trúc message và cách trao đổi.

> [!question] Thẻ 4.3 — "Stateless" nghĩa là gì? Hệ quả kiến trúc lớn nhất?
> **Đáp:** server không giữ thông tin gì về client giữa các request; mỗi request xử lý độc lập. Hệ quả: **scale ngang dễ** — request tới server giống hệt nào cũng được.

> [!question] Thẻ 4.4 — Nếu HTTP stateless, "đăng nhập/giỏ hàng" lưu ở đâu?
> **Đáp:** ở nơi *khác* server-logic: client mang theo (cookie/JWT) hoặc DB/cache chia sẻ (DynamoDB/ElastiCache). Không lưu trong RAM của một server cụ thể.

> [!question] Thẻ 4.5 — DNS là gì (hai vế)? Hai tính chất then chốt?
> **Đáp:** (1) CSDL phân tán trên hệ phân cấp DNS server + (2) giao thức tầng ứng dụng để truy vấn nó. Then chốt: **phân tán** (chịu tải/lỗi) + **phân cấp** (root→TLD→authoritative).

> [!question] Thẻ 4.6 — Route 53 và API Gateway ứng với khái niệm nền nào?
> **Đáp:** Route 53 = DNS managed (danh bạ phân cấp); API Gateway/ALB = điểm cuối HTTP. Stateless của HTTP là điều kiện để Lambda/container auto-scale.

## 9. Câu hỏi tự kiểm tra

1. Kể năm tầng và một việc mỗi tầng lo. "Encapsulation" nghĩa là gì? *(mục 1, 6, tr. 50)*
2. HTTP gồm mấy chương trình, nói chuyện bằng gì? HTTP có quy định tầng dưới không? *(mục 2, tr. 95)*
3. "Stateless" nghĩa là gì? Vì sao nó giúp scale ngang? *(mục 3, tr. 98)*
4. Nếu server stateless, làm sao web "nhớ" bạn đã đăng nhập? Hai cách. *(mục 3, 5)*
5. Hai vế định nghĩa DNS. Vì sao nó phải *phân tán* và *phân cấp*? *(mục 4, tr. 123)*
6. Chạy demo mục 5. Vì sao Client A luôn "lần 1"? Điều đó liên quan gì tới auto-scaling? *(mục 5, 7)*

## Tóm tắt một trang

```
BÀI 4 — MẠNG TRỤ 2a: PHÂN TẦNG · HTTP · DNS
─────────────────────────────────────────────────────────
PHÂN TẦNG  5 tầng: Application/Transport/Network/Link/Physical (tr.50).
   Mỗi tầng giấu chi tiết tầng dưới → abstraction của Bài 1, cho mạng.
   Encapsulation: tầng dưới bọc thêm header quanh dữ liệu tầng trên.

HTTP  giao thức tầng ứng dụng của Web; 2 chương trình (client+server)
   trao đổi message (tr.95). Chỉ quy định cấu trúc + cách trao đổi.

STATELESS  server KHÔNG nhớ gì về client giữa request (tr.98).
   → mỗi request độc lập → SCALE NGANG dễ (server nào cũng như nhau).
   Muốn "nhớ" → client mang theo (cookie/JWT) HOẶC DB/cache chia sẻ.

DNS  (1) CSDL PHÂN TÁN trên hệ PHÂN CẤP server + (2) giao thức truy vấn
   (tr.123). root → TLD(.com) → authoritative. Distributed system đầu tiên.

DEMO  server không có bộ đếm. Client 'quên' → mãi lần 1; client 'mang
   state theo' → 1→2→3. State sống ở client, không ở server.

NỐI VỀ AWS  Route 53 = DNS managed; API GW/ALB = điểm cuối HTTP;
   stateless = điều kiện auto-scale Lambda/container; VPC = tầng network.
```

## Nguồn

- **James F. Kurose & Keith W. Ross**, *Computer Networking: A Top-Down Approach, 8th Edition* (Pearson, 2021) — **§1.5**: protocol stack năm tầng (tr. 50); **§2.2**: HTTP overview (tr. 95), stateless (tr. 98); **§2.4**: định nghĩa DNS (tr. 123). `tai_lieu/Computer Networking A Top-Down Approach 8th Edition by James W. Kurose, Keith W. Ross.pdf` — **offset PDF = tr. + 28** (PDF 78 = tr. 50).
- Nối về AWS: [`aws-fund` Bài 5 — Networking](../../aws-fund/bai_hoc/bai_05_networking.md) (Route 53, API Gateway, VPC).
- Tiếp: [Bài 5 — TCP, TLS](bai_05_mang-tcp-tls.md) xuống tầng vận chuyển — "đường ống đáng tin" mà HTTP ở bài này vẫn dựa vào.

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · **[Bài 4 — Mạng: phân tầng, HTTP, DNS] ← bạn đang ở đây** · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
