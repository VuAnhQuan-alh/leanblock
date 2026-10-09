# Bài 7 — Distributed trụ 3a: Giao tiếp và thất bại

> [!info] Về bài này
> **Trụ 3 (Distributed Systems), mảnh 1/3.** Trụ 1 lo một máy, trụ 2 lo đường truyền. Giờ ta ghép nhiều máy qua mạng — và một loại khó mới xuất hiện: **thất bại một phần (partial failure)**. Trên một máy, thứ gì đó hoặc chạy hoặc không. Qua mạng, bạn thường *không biết được* nó chạy hay không. Đây là gốc rễ của **timeout, retry, idempotency, và cả thiết kế SQS/Step Functions** ở `aws-fund`.
> Nguồn: **DDIA** (ch. 8 — The Trouble with Distributed Systems) + **UDS** (ch. 1–2).
> **Trích:** `DDIA (tr. X)` offset **+22**; `UDS (tr. X)` offset **+18**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 2 — concurrency/idempotency](bai_02_os-concurrency.md), [Bài 5 — TCP](bai_05_mang-tcp-tls.md).

## Mục lục

1. [Distributed system: nhiều máy, và vì sao khó](#1-distributed-system-nhiều-máy-và-vì-sao-khó)
2. [Mạng không đáng tin: xây tin cậy từ bất tin](#2-mạng-không-đáng-tin-xây-tin-cậy-từ-bất-tin)
3. [Timeout: ba điều ta không phân biệt được](#3-timeout-ba-điều-ta-không-phân-biệt-được)
4. [Demo: retry mù quáng vs idempotency](#4-demo-retry-mù-quáng-vs-idempotency)
5. [Bảng so sánh: kiểu thất bại và cách chống](#5-bảng-so-sánh-kiểu-thất-bại-và-cách-chống)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Distributed system: nhiều máy, và vì sao khó

Trước hết, định nghĩa gọn — và nó có nhiều góc nhìn đúng cùng lúc:

> [!quote] UDS (tr. 7)
> "a distributed system is a group of machines that communicate over network links. However, from a run-time point of view, a distributed system is a group of software processes that communicate via inter-process communication (IPC) mechanisms like HTTP."
>
> *một hệ phân tán là **một nhóm máy giao tiếp qua các liên kết mạng**. Nhưng ở góc nhìn lúc chạy, nó là **một nhóm tiến trình phần mềm giao tiếp** qua các cơ chế liên-tiến-trình (IPC) như HTTP.*

Vì sao ghép máy lại thì khó hơn hẳn một máy to? Một câu của UDS đóng khung toàn bộ tư duy vận hành:

> [!quote] UDS (tr. 5)
> "A distributed system is resilient when it can continue to do its job even when failures happen. And at scale, anything that can go wrong will go wrong."
>
> *Một hệ phân tán **kiên cường (resilient)** khi nó vẫn làm được việc **ngay cả khi có sự cố**. Và **ở quy mô lớn, bất cứ thứ gì có thể hỏng rồi sẽ hỏng**.*

DDIA đặt tên cho con quái vật trung tâm:

> [!quote] DDIA (tr. 275)
> "This is known as a partial failure. The difficulty is that partial failures are nondeterministic: if you try to do anything involving multiple nodes and the network, it may sometimes work and sometimes unpredictably fail."
>
> *Đây gọi là **thất bại một phần (partial failure)**. Cái khó là partial failure **bất định (nondeterministic)**: hễ bạn làm gì dính tới **nhiều node và mạng**, nó có thể **lúc chạy lúc hỏng** không đoán trước được.*

Nhớ "indeterminate" của Bài 2 (race condition)? Đây là người anh em ở quy mô mạng: trên một máy, bất định đến từ *context switch*; qua mạng, nó đến từ *gói tin và node có thể hỏng bất kỳ lúc nào, bất kỳ cách nào*. Và như DDIA nói ngay sau đó: chính nondeterminism này "là thứ làm distributed systems khó".

## 2. Mạng không đáng tin: xây tin cậy từ bất tin

Mạng mà các máy dựa vào về cơ bản là **không đáng tin** — và ta đã gặp điều này ở Bài 5, giờ gọi đúng tên:

> [!quote] DDIA (tr. 277)
> "IP (the Internet Protocol) is unreliable: it may drop, delay, duplicate, or reorder packets. TCP (the Transmission Control Protocol) provides a more reliable transport layer on top of IP: it ensures that missing packets are retransmitted, duplicates are eliminated, and packets are reassembled into the order in which they were sent."
>
> ***IP không đáng tin**: nó có thể **rớt, trì hoãn, nhân đôi, hoặc đảo thứ tự** gói. **TCP** cung cấp một tầng vận chuyển **đáng tin hơn** trên nền IP: bảo đảm gói mất được truyền lại, gói trùng bị loại, và các gói được ráp lại đúng thứ tự đã gửi.*

Đây là ý tưởng đẹp nhất của cả trụ: **xây hệ tin cậy từ linh kiện không tin cậy** (đúng như DDIA lập luận ở mục "reliable system from unreliable components"). TCP làm điều đó cho *gói tin*; nhưng — và đây là bẫy — TCP chỉ giấu được mất-gói, nó **không** giấu được *node sập* hay *mạng đứt lâu*. Khi cả một node ngừng đáp, không tầng nào bên dưới cứu bạn; bạn phải đối mặt với partial failure ở tầng ứng dụng. Đó là nội dung mục 3.

## 3. Timeout: ba điều ta không phân biệt được

Đây là trái tim của bài — một sự thật tưởng đơn giản mà hệ quả khổng lồ:

> [!quote] DDIA (tr. 278)
> "If you send a request and don't get a response, it's not possible to distinguish whether (a) the request was lost, (b) the remote node is down, or (c) the response was lost."
>
> *Nếu bạn gửi một request mà **không nhận được hồi đáp**, bạn **không thể phân biệt** giữa (a) request bị mất, (b) node bên kia đã chết, hay (c) hồi đáp bị mất.*

Ba khả năng, cùng một triệu chứng: im lặng. Và hệ quả trực tiếp:

> [!quote] DDIA (tr. 278)
> "If you send a request to another node and don't receive a response, it is impossible to tell why. The usual way of handling this issue is a timeout: after some time you give up waiting and assume that the response is not going to arrive."
>
> *Gửi request mà không nhận hồi đáp thì **không thể biết tại sao**. Cách xử lý thường thấy là **timeout**: sau một khoảng thời gian, bạn bỏ cuộc chờ và **giả định** hồi đáp sẽ không tới.*

Nhưng timeout chỉ là *đoán*. Khi timeout xảy ra, bạn **vẫn** không biết node bên kia có nhận request không — nó có thể đã xử lý xong, chỉ là hồi đáp bị mất (khả năng (c)). Nếu bạn phản ứng bằng cách **gửi lại** (retry), và node đã xử lý lần đầu, thì giờ nó xử lý **hai lần**. Đây là lý do *retry* và *idempotency* luôn đi cặp — demo mục 4 cho thấy tai hoạ khi thiếu vế sau.

## 4. Demo: retry mù quáng vs idempotency

Mô phỏng tất định tình huống (c): server *luôn* xử lý request, nhưng **ack của lần gửi đầu bị mất** trên đường về. Client timeout, retry. Ta so hai kiểu: retry không có idempotency key (mỗi lần một giao dịch mới) vs có idempotency key (server khử trùng lặp).

```typescript
// Distributed: khi gửi request mà KHÔNG nhận được hồi đáp, client không thể
// biết (a) request mất, (b) node chết, hay (c) hồi đáp mất (DDIA Fig 8-1).
// Cách xử lý: TIMEOUT rồi THỬ LẠI. Nhưng thử lại mù quáng = tác dụng kép.
// Mô phỏng tất định: ack của LẦN GỬI ĐẦU luôn "mất" trên đường về.

class Server {
  balance = 0;
  #done = new Map<string, number>();        // idempotency key -> số dư sau khi áp
  // server LUÔN xử lý khi nhận được request; vấn đề nằm ở đường ACK về.
  charge(key: string | null, amount: number): number {
    if (key !== null && this.#done.has(key)) return this.#done.get(key)!; // đã làm rồi
    this.balance += amount;
    if (key !== null) this.#done.set(key, this.balance);
    return this.balance;
  }
}

// "Mạng": trả ack về client CHỈ từ lần gửi thứ 2 trở đi (lần 1 ack bị mất).
function callWithRetry(server: Server, key: string | null, amount: number, keyPerAttempt: () => string | null): void {
  let attempt = 0;
  while (true) {
    attempt++;
    const k = key === null ? keyPerAttempt() : key; // idempotency: cùng key mọi lần
    server.charge(k, amount);                        // server xử lý (dù ack có về hay không)
    if (attempt >= 2) return;                         // lần 2: ack về → client yên tâm
    // lần 1: ack mất → client timeout → vòng lặp thử lại
  }
}

// --- KHÔNG idempotency: mỗi lần thử dùng key MỚI → server coi là 2 giao dịch ---
const s1 = new Server();
let n = 0;
callWithRetry(s1, null, 100, () => `tx-${++n}`); // mỗi attempt một key khác
console.log(`KHÔNG idempotency: thu phí $100, retry sau timeout → số dư = $${s1.balance}  ← TRỪ 2 LẦN`);

// --- CÓ idempotency: mọi lần thử dùng CÙNG key → server khử trùng lặp ---
const s2 = new Server();
callWithRetry(s2, "order-42", 100, () => "order-42");
console.log(`CÓ idempotency  : thu phí $100, retry sau timeout → số dư = $${s2.balance}  ← đúng 1 lần`);

console.log(`\nPartial failure: client KHÔNG biết lần 1 có thành công không, nên phải retry.`);
console.log(`Chỉ idempotency key mới biến "retry an toàn" thành sự thật.`);
```

Kết quả chạy thật *(tất định)*:

```
KHÔNG idempotency: thu phí $100, retry sau timeout → số dư = $200  ← TRỪ 2 LẦN
CÓ idempotency  : thu phí $100, retry sau timeout → số dư = $100  ← đúng 1 lần

Partial failure: client KHÔNG biết lần 1 có thành công không, nên phải retry.
Chỉ idempotency key mới biến "retry an toàn" thành sự thật.
```

Client *buộc* phải retry — nó không có cách nào biết lần đầu đã thành công (khả năng (c) của mục 3). Không idempotency, retry biến "ack bị mất" thành "khách bị trừ tiền hai lần". Có idempotency key, server nhận ra "đơn `order-42` xử lý rồi" và bỏ qua. Lưu ý mắt xích: đây đúng là **atomicity / "all or nothing"** của Bài 2, nhưng kẻ thù không còn là context switch mà là *mạng mất hồi đáp*. Một ý tưởng, hai tầng — và giờ nó là bắt buộc, không phải tuỳ chọn.

> [!note] Tự thử
> - Cho ack mất ở *cả hai* lần đầu (sửa điều kiện `attempt >= 3`): bản không-idempotency trừ 3 lần, bản idempotency vẫn đúng 1 lần. Idempotency an toàn với *mọi* số lần retry.
> - Thêm đọc số dư *giữa* các retry: thấy trạng thái "chưa chắc chắn" mà client phải sống chung — nó không biết số dư thật là 100 hay 200 cho tới khi có ack.
> - Biến `charge` thành "ghi có điều kiện" (chỉ áp nếu `balance` khớp giá trị kỳ vọng): đó là optimistic concurrency (Bài 2) — một cách khác để retry an toàn mà không cần key.

## 5. Bảng so sánh: kiểu thất bại và cách chống

Partial failure không phải một thứ mà là một *phổ*. Nhận diện đúng kiểu để chọn đúng vũ khí:

| Kiểu thất bại            | Triệu chứng client thấy       | Vũ khí chính                                  | Nền / AWS                              |
| :----------------------- | :---------------------------- | :-------------------------------------------- | :------------------------------------- |
| Gói/hồi đáp mất tạm thời | im lặng rồi (có thể) bình thường | timeout + **retry** (có backoff)           | SDK retry, SQS redrive                 |
| Node chết hẳn            | im lặng kéo dài               | timeout + chuyển sang node khác (failover)    | health check, Multi-AZ (Bài 8)         |
| Retry gây tác dụng kép   | xử lý lặp (trừ tiền 2 lần)    | **idempotency key** / optimistic concurrency  | idempotency của SQS/API, DynamoDB cond. |
| Mạng chậm (không chết)   | timeout nhưng node vẫn sống   | backoff + **jitter**, circuit breaker         | exponential backoff + jitter (SDK)     |

Quy luật xuyên suốt: **vì không phân biệt được "chậm" với "chết", mọi cơ chế đều là phỏng đoán có kỷ luật.** Timeout là đoán "nó chết rồi"; retry là đặt cược "thử lại sẽ tới"; idempotency là bảo hiểm cho ván cược đó. Thiết kế distributed tốt = chọn các phỏng đoán này một cách tỉnh táo, không phải giả vờ mạng đáng tin.

## 6. Nối về AWS

> [!note] Nối về AWS
> Gần như mọi "pattern độ tin cậy" của AWS là hiện thực của bài này — xem [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md):
> - **SQS at-least-once** là partial failure được *thiết kế vào*: SQS thà giao message *dư* còn hơn *thiếu* (vì không phân biệt được "consumer chết" với "consumer chậm"). Hệ quả bắt buộc: consumer **phải idempotent** — đúng demo mục 4. Đây là lý do idempotency không phải "nice to have" mà là điều kiện đúng đắn.
> - **Exponential backoff + jitter** (mặc định trong AWS SDK): retry ngay lập tức và đồng loạt sẽ *dồn tải* lúc hệ đang yếu. Backoff giãn thời gian, jitter phá vỡ sự đồng loạt — xử lý đúng kiểu "mạng chậm" ở bảng mục 5.
> - **Step Functions / DLQ (dead-letter queue):** khi retry mãi vẫn hỏng, phải có chỗ "để dành" message độc thay vì lặp vô hạn — hiện thực của "timeout rồi bỏ cuộc" ở mức quy trình.
> - **Health check + Multi-AZ:** phân biệt "node chết" bằng cách *chủ động* kiểm tra, rồi lái traffic khỏi vùng im lặng — vì bản thân sự im lặng không nói cho bạn biết (mục 3).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — "Partial failure" là gì? Khác lỗi trên một máy ở đâu?
> **Đáp:** một phần hệ hỏng trong khi phần khác vẫn chạy, và nó **bất định** (lúc chạy lúc hỏng). Trên một máy: hoặc chạy hoặc không; qua mạng: thường *không biết được* nó chạy hay không.

> [!question] Thẻ 7.2 — "Xây tin cậy từ bất tin" nghĩa là gì? TCP làm gì, KHÔNG làm gì?
> **Đáp:** dựng hệ đáng tin trên linh kiện không đáng tin. TCP giấu mất-gói/đảo-thứ-tự của IP; nhưng **không** giấu được node sập hay mạng đứt lâu.

> [!question] Thẻ 7.3 — Ba khả năng khi không nhận được hồi đáp? Vì sao quan trọng?
> **Đáp:** (a) request mất, (b) node chết, (c) hồi đáp mất. Cùng triệu chứng (im lặng) → không phân biệt được → mọi xử lý chỉ là phỏng đoán.

> [!question] Thẻ 7.4 — Vì sao retry cần đi với idempotency?
> **Đáp:** timeout không cho biết lần đầu có thành công không; retry khi nó *đã* thành công → xử lý kép (trừ tiền 2 lần). Idempotency key để server khử trùng lặp → retry an toàn.

> [!question] Thẻ 7.5 — "SQS at-least-once" ép buộc điều gì ở consumer? Vì sao?
> **Đáp:** consumer **phải idempotent**. Vì SQS thà giao dư hơn thiếu (không phân biệt consumer chết/chậm), nên message có thể tới >1 lần.

> [!question] Thẻ 7.6 — Backoff + jitter giải quyết vấn đề gì?
> **Đáp:** retry đồng loạt tức thì dồn tải lúc hệ yếu; backoff giãn thời gian, jitter phá đồng loạt → tránh "bão retry".

## 8. Câu hỏi tự kiểm tra

1. Định nghĩa distributed system (hai góc nhìn). "At scale, anything that can go wrong will go wrong" nghĩa gì? *(mục 1, tr. 5, 7)*
2. "Partial failure" là gì và vì sao nó bất định? Liên hệ với "indeterminate" của Bài 2. *(mục 1, tr. 275)*
3. "Xây tin cậy từ bất tin" — TCP minh hoạ ra sao, và giới hạn của nó? *(mục 2, tr. 277)*
4. Ba điều không phân biệt được khi im lặng. Timeout giải quyết triệt để không? *(mục 3, tr. 278)*
5. Chạy demo mục 4. Vì sao thiếu idempotency thì retry gây trừ tiền 2 lần? *(mục 4)*
6. Vì sao SQS at-least-once *buộc* consumer idempotent? Backoff+jitter dùng khi nào? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 7 — DISTRIBUTED TRỤ 3a: GIAO TIẾP & THẤT BẠI
─────────────────────────────────────────────────────────
ĐỊNH NGHĨA  nhóm máy/tiến trình giao tiếp qua mạng (IPC như HTTP) (UDS tr.7).
   "At scale, anything that can go wrong WILL go wrong" (UDS tr.5).

PARTIAL FAILURE  một phần hỏng, phần khác chạy; BẤT ĐỊNH (DDIA tr.275).
   Người anh em mạng của "indeterminate" (Bài 2): kẻ thù là node/gói hỏng.

MẠNG BẤT TIN  IP có thể rớt/trễ/nhân đôi/đảo gói; TCP giấu được điều đó
   (tin cậy từ bất tin, tr.277) — NHƯNG không giấu node sập/mạng đứt lâu.

3 ĐIỀU KHÔNG PHÂN BIỆT (khi im lặng, tr.278): (a) request mất (b) node chết
   (c) hồi đáp mất. TIMEOUT = đoán "chết rồi"; vẫn không biết nó đã xử lý chưa.

DEMO  ack lần đầu mất → client retry. KHÔNG idempotency → trừ $200 (2 lần);
   CÓ idempotency key → $100 (1 lần). = atomicity Bài 2, kẻ thù là mạng.

NỐI VỀ AWS  SQS at-least-once ⇒ consumer PHẢI idempotent; backoff+jitter
   (bão retry); DLQ/Step Functions (bỏ cuộc có kỷ luật); health check+Multi-AZ.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 8 (The Trouble with Distributed Systems)**: partial failure nondeterministic (tr. 275), IP unreliable / reliable-from-unreliable (tr. 277), ba khả năng & timeout (tr. 278). Offset **PDF = tr. + 22**.
- **Roberto Vitillo**, *Understanding Distributed Systems, 2nd* — **ch. 1–2**: resilience & "anything that can go wrong will go wrong" (tr. 5), định nghĩa (tr. 7). `tai_lieu/Understanding Distributed Systems 2nd edition.pdf` — offset **PDF = tr. + 18**.
- Nối về AWS: [`aws-fund` Bài 4 — Messaging](../../aws-fund/bai_hoc/bai_04_messaging.md) (SQS at-least-once, idempotency, backoff).
- Tiếp: [Bài 8 — nhân bản & nhất quán](bai_08_dist-nhat-quan.md) — một khi chấp nhận mạng hỏng, làm sao nhiều bản sao dữ liệu *đồng ý* với nhau?

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · **[Bài 7 — Distributed: giao tiếp & thất bại] ← bạn đang ở đây** · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
