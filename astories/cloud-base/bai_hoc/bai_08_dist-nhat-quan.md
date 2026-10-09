# Bài 8 — Distributed trụ 3b: Nhân bản và nhất quán (CAP)

> [!info] Về bài này
> **Trụ 3 (Distributed Systems), mảnh 2/3.** [Bài 7](bai_07_dist-giao-tiep.md) chấp nhận mạng sẽ hỏng. Hệ quả: muốn chịu lỗi, phải giữ **nhiều bản sao** dữ liệu (nhân bản). Nhưng nhiều bản sao sinh ra câu hỏi nhức nhối nhất của trụ này: **chúng có đồng ý với nhau không, và khi mạng đứt thì sao?** Đây là lý thuyết đằng sau **DynamoDB (eventual vs strong read), Multi-AZ RDS, S3 consistency** ở `aws-fund` — và là chỗ "CAP theorem" cuối cùng thôi là buzzword (Bài 0).
> Nguồn: **DDIA** (ch. 5 Replication, ch. 9 Consistency & CAP).
> **Trích:** `DDIA (tr. X)` offset **+22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 7 — giao tiếp & thất bại](bai_07_dist-giao-tiep.md), [Bài 3 — nhân bản/durability](bai_03_os-luu-tru.md).

## Mục lục

1. [Nhân bản: vì sao giữ nhiều bản sao](#1-nhân-bản-vì-sao-giữ-nhiều-bản-sao)
2. [Replication lag và eventual consistency](#2-replication-lag-và-eventual-consistency)
3. [CAP: khi partition, phải chọn](#3-cap-khi-partition-phải-chọn)
4. [Demo: lag, hội tụ, và lựa chọn CP hay AP](#4-demo-lag-hội-tụ-và-lựa-chọn-cp-hay-ap)
5. [Bảng so sánh: nhất quán mạnh vs eventual](#5-bảng-so-sánh-nhất-quán-mạnh-vs-eventual)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Nhân bản: vì sao giữ nhiều bản sao

> [!quote] DDIA (tr. 151)
> "Replication means keeping a copy of the same data on multiple machines that are connected via a network."
>
> ***Nhân bản (replication)** nghĩa là giữ **một bản sao của cùng dữ liệu trên nhiều máy** nối với nhau qua mạng.*

DDIA nêu các lý do, và hai lý do đầu chính là hai trụ ta vừa học hội tụ lại:

> [!quote] DDIA (tr. 151)
> "To keep data geographically close to your users (and thus reduce latency). To allow the system to continue working even if some of its parts have failed (and thus increase availability)."
>
> *Giữ dữ liệu **gần người dùng về mặt địa lý** (giảm độ trễ). Cho hệ **tiếp tục chạy ngay cả khi vài phần đã hỏng** (tăng tính sẵn sàng — availability).*

Lý do đầu là trụ Mạng (Bài 6: CDN rút ngắn khoảng cách = giảm latency); lý do sau là trụ Distributed (Bài 7: chịu partial failure). Nhân bản là nơi hai động lực này gặp nhau — nhưng nó không miễn phí: giây phút bạn có *hai* bản sao, bạn phải trả lời "khi chúng khác nhau thì tin cái nào?".

## 2. Replication lag và eventual consistency

Bản ghi tới leader trước, tới các follower sau — qua mạng, nên **có độ trễ**. Trong khe hở đó, đọc từ follower có thể thấy giá trị cũ:

> [!quote] DDIA (tr. 162)
> "This inconsistency is just a temporary state—if you stop writing to the database and wait a while, the followers will eventually catch up and become consistent with the leader. For that reason, this effect is known as eventual consistency."
>
> *Sự không nhất quán này chỉ là **trạng thái tạm thời** — nếu bạn ngừng ghi và chờ một lúc, các follower **rốt cuộc sẽ bắt kịp** và trở nên nhất quán với leader. Vì vậy, hiệu ứng này gọi là **eventual consistency (nhất quán cuối cùng)**.*

"Eventual" là một lời hứa *yếu*: nó nói các bản sao *sẽ* hội tụ, nhưng **không hứa khi nào**, và trong lúc chờ, các client khác nhau có thể thấy dữ liệu khác nhau. Đây đúng là buzzword "eventual consistency" mà Bài 0 nói bạn *dùng* mà chưa *hiểu* — giờ nó có nghĩa cụ thể: cái giá của việc đọc từ một bản sao chưa kịp cập nhật. Câu hỏi còn lại: nếu ta *cần* nhất quán mạnh thì sao, và mạng đứt thì chuyện gì xảy ra?

## 3. CAP: khi partition, phải chọn

CAP là định lý bị trích dẫn sai nhiều nhất ngành. DDIA đính chính thẳng:

> [!quote] DDIA (tr. 337)
> "CAP is sometimes presented as Consistency, Availability, Partition tolerance: pick 2 out of 3. Unfortunately, putting it this way is misleading [32] because network partitions are a kind of fault, so they aren't something about which you have a choice: they will happen whether you like it or not."
>
> *CAP đôi khi được trình bày là "Consistency, Availability, Partition tolerance: chọn 2 trong 3". Tiếc là cách nói đó **gây hiểu lầm**, vì **network partition là một loại sự cố** — không phải thứ bạn **được chọn**: nó sẽ xảy ra dù bạn muốn hay không.*

Vì partition *chắc chắn* xảy ra (Bài 7), nó không phải một lựa chọn — lựa chọn thật chỉ hiện ra *khi* nó xảy ra:

> [!quote] DDIA (tr. 337)
> "When a network fault occurs, you have to choose between either linearizability or total availability. Thus, a better way of phrasing CAP would be either Consistent or Available when Partitioned."
>
> *Khi có sự cố mạng, bạn **phải chọn giữa** nhất quán tuyến tính (linearizability) **hoặc** sẵn sàng toàn phần. Nên cách phát biểu đúng hơn của CAP là: **hoặc Nhất quán, hoặc Sẵn sàng, KHI bị Phân mảnh** (Consistent or Available when Partitioned).*

Diễn giải: lúc mạng khoẻ, bạn có *cả hai* — nhất quán lẫn sẵn sàng. Chỉ *khi partition* mới buộc phải bỏ một: hoặc **từ chối phục vụ** để không trả dữ liệu cũ (chọn C), hoặc **phục vụ dữ liệu có thể cũ** để luôn trả lời được (chọn A). Không có lựa chọn thứ ba. Demo mục 4 cho bạn tự tay làm cả hai.

## 4. Demo: lag, hội tụ, và lựa chọn CP hay AP

Dựng một leader + một follower với hàng đợi nhân bản. Phần đầu cho thấy replication lag → eventual consistency. Phần sau mô phỏng partition và cho client đọc theo hai triết lý: AP (phục vụ giá trị cũ) và CP (từ chối).

```typescript
// Replication: giữ bản sao dữ liệu trên nhiều máy. Follower áp bản ghi SAU
// leader → có "replication lag" → đọc từ follower có thể thấy giá trị CŨ:
// đó là EVENTUAL CONSISTENCY. Khi mạng phân mảnh (partition), phải CHỌN:
// nhất quán (CP: từ chối phục vụ) hay sẵn sàng (AP: phục vụ giá trị cũ).
class Node {
  store = new Map<string, number>();
  read(key: string): number | undefined { return this.store.get(key); }
}
const leader = new Node();
const follower = new Node();
const pending: Array<[string, number]> = []; // hàng đợi nhân bản leader→follower
let partitioned = false;

function write(key: string, val: number): void {
  leader.store.set(key, val);
  pending.push([key, val]);         // chưa tới follower ngay
}
function replicate(): void {
  if (partitioned) return;          // mạng đứt → không nhân bản được
  for (const [k, v] of pending) follower.store.set(k, v);
  pending.length = 0;
}

write("x", 1); replicate();
console.log(`1) write x=1, nhân bản xong → follower đọc x = ${follower.read("x")}  (nhất quán)`);

write("x", 2);  // CHƯA replicate
console.log(`2) write x=2 (chưa nhân bản) → follower đọc x = ${follower.read("x")}  ← CŨ (replication lag)`);

replicate();
console.log(`3) nhân bản xong        → follower đọc x = ${follower.read("x")}  (đã HỘI TỤ — eventual)`);

// --- Partition: leader nhận write mới nhưng không nhân bản được ---
partitioned = true;
write("x", 3);
console.log(`\n4) PARTITION. leader có x=3, follower vẫn x=${follower.read("x")}. Giờ client đọc follower:`);

function readAP(key: string): string { return `x = ${follower.read(key)} (CŨ nhưng SẴN SÀNG)`; }
function readCP(key: string): string {
  if (partitioned) throw new Error("từ chối: không chắc dữ liệu mới nhất");
  return `x = ${follower.read(key)}`;
}
console.log(`   AP (ưu tiên Available): ${readAP("x")}`);
try { console.log(`   CP (ưu tiên Consistent): ${readCP("x")}`); }
catch (e) { console.log(`   CP (ưu tiên Consistent): LỖI — ${(e as Error).message}`); }

console.log(`\nKhi partition: KHÔNG thể vừa nhất quán vừa sẵn sàng. Phải chọn (DDIA tr.337).`);
```

Kết quả chạy thật *(tất định)*:

```
1) write x=1, nhân bản xong → follower đọc x = 1  (nhất quán)
2) write x=2 (chưa nhân bản) → follower đọc x = 1  ← CŨ (replication lag)
3) nhân bản xong        → follower đọc x = 2  (đã HỘI TỤ — eventual)

4) PARTITION. leader có x=3, follower vẫn x=2. Giờ client đọc follower:
   AP (ưu tiên Available): x = 2 (CŨ nhưng SẴN SÀNG)
   CP (ưu tiên Consistent): LỖI — từ chối: không chắc dữ liệu mới nhất

Khi partition: KHÔNG thể vừa nhất quán vừa sẵn sàng. Phải chọn (DDIA tr.337).
```

Bước (2) là eventual consistency sờ được: follower trả `1` dù leader đã có `2` — cũ, nhưng chỉ *tạm thời* (bước (3) nó hội tụ). Bước (4) là CAP: trong partition, `readAP` *luôn* trả lời nhưng có thể cũ (`2` thay vì `3`); `readCP` *từ chối* để không nói dối. Cả hai đều "đúng" — chúng chỉ phục vụ hai yêu cầu nghiệp vụ khác nhau. Lưu ý mắt xích về Bài 7: cái "từ chối vì không chắc" của CP chính là sống thật với "ba điều không phân biệt được" — thà im lặng còn hơn trả dữ liệu sai.

> [!note] Tự thử
> - Sau partition, cho `partitioned = false` rồi `replicate()`: follower hội tụ về `3`. Đó là lúc hệ AP "lành lại" sau sự cố — eventual consistency ở quy mô partition.
> - Thêm nhiều follower với độ lag khác nhau: hai client đọc hai follower có thể thấy hai giá trị khác nhau *cùng lúc* — vì sao "read-your-own-writes" cần xử lý riêng.
> - Đổi `write` để chỉ trả về sau khi *đa số* follower ack (quorum): bạn vừa bước sang mô hình consensus của [Bài 9](bai_09_dist-phan-manh.md).

## 5. Bảng so sánh: nhất quán mạnh vs eventual

Không có "đúng" tuyệt đối — chỉ có đánh đổi hợp hay không hợp với bài toán:

| Tiêu chí              | Nhất quán mạnh (linearizable)        | Eventual consistency                  |
| :-------------------- | :----------------------------------- | :------------------------------------ |
| Đọc thấy gì           | luôn là giá trị **mới nhất**         | có thể **cũ** một lúc, rồi hội tụ     |
| Khi partition         | hy sinh **availability** (từ chối)   | hy sinh **consistency** (trả cũ)      |
| Độ trễ ghi            | cao hơn (chờ phối hợp các bản sao)   | thấp (ghi local, lan sau)            |
| Hợp cho               | số dư tài khoản, khoá, tồn kho       | like/view count, feed, cache, hồ sơ  |
| Nền / AWS             | DynamoDB *strongly consistent read*; RDS leader | DynamoDB *eventually consistent read* (mặc định); read replica |

Quy luật chọn: **hỏi "đọc cũ một giây có gây hại thật không?"** Với số dư tiền hay tồn kho bán hàng → có → cần mạnh. Với số lượt thích → không → eventual là đủ, và rẻ+nhanh hơn. Đây là cùng một tinh thần đánh đổi TCP vs UDP (Bài 5): *đảm bảo mạnh mua bằng phối hợp (round-trip); nới lỏng để nhanh và sẵn sàng hơn.*

## 6. Nối về AWS

> [!note] Nối về AWS
> CAP thôi là lý thuyết suông ngay khi bạn chỉnh một tham số đọc của DynamoDB — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **DynamoDB: eventually consistent read (mặc định) vs strongly consistent read.** Đây *chính xác* là bước (2) vs (3) của demo: read mặc định có thể trúng bản sao chưa kịp cập nhật (rẻ hơn, nhanh hơn); strongly consistent read đọc từ leader (đắt gấp đôi RCU, có thể lỗi khi partition). Chọn tham số này = chọn vị trí trên trục mục 5.
> - **Multi-AZ RDS** = nhân bản để *tăng availability* (lý do thứ 2, mục 1): khi AZ chứa leader hỏng, standby ở AZ khác lên thay. Trong lúc failover, hệ nghiêng về **CP** (ngắn ngủi không ghi được) để không mất/sai dữ liệu.
> - **Aurora Global / read replica cross-region** = nhân bản để *giảm latency* (lý do thứ 1): đọc gần người dùng, nhưng chấp nhận replication lag → eventual. Đúng đánh đổi mục 2.
> - **Vì sao DynamoDB mặc định eventual:** ở quy mô Dynamo, partition là thường xuyên; mặc định **AP** cho throughput + availability cao, và để bạn *chọn* trả thêm tiền cho strong khi nghiệp vụ cần. Mặc định phản ánh "anything that can go wrong will go wrong" (Bài 7).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — Nhân bản là gì? Hai lý do chính, ứng với trụ nào?
> **Đáp:** giữ bản sao cùng dữ liệu trên nhiều máy. (1) gần người dùng → giảm latency (trụ Mạng); (2) chịu lỗi → tăng availability (trụ Distributed).

> [!question] Thẻ 8.2 — "Eventual consistency" nghĩa là gì? Lời hứa yếu ở chỗ nào?
> **Đáp:** các bản sao *rốt cuộc* sẽ hội tụ sau khi ngừng ghi. Yếu vì không hứa **khi nào**, và trong lúc chờ client có thể thấy giá trị cũ/khác nhau.

> [!question] Thẻ 8.3 — Vì sao "pick 2 of 3" là cách nói CAP sai?
> **Đáp:** partition là **sự cố**, không phải lựa chọn — nó sẽ xảy ra. Nên P không phải thứ để "bỏ".

> [!question] Thẻ 8.4 — Phát biểu CAP đúng hơn? Lựa chọn thật xảy ra khi nào?
> **Đáp:** "**Consistent or Available when Partitioned**". Lúc mạng khoẻ có cả hai; chỉ *khi partition* mới phải chọn: từ chối (C) hay phục vụ dữ liệu cũ (A).

> [!question] Thẻ 8.5 — Khi nào cần nhất quán mạnh, khi nào eventual là đủ?
> **Đáp:** hỏi "đọc cũ một giây có hại thật không?". Số dư/tồn kho/khoá → cần mạnh. Like/view/feed/cache → eventual đủ (rẻ, nhanh, sẵn sàng hơn).

> [!question] Thẻ 8.6 — DynamoDB read mặc định là loại nào? Vì sao?
> **Đáp:** **eventually consistent** (rẻ, nhanh, sẵn sàng). Strong read tốn gấp đôi RCU và đọc từ leader. Mặc định AP vì ở quy mô Dynamo partition là thường xuyên.

## 8. Câu hỏi tự kiểm tra

1. Nhân bản là gì? Hai lý do chính và chúng nối về hai trụ nào? *(mục 1, tr. 151)*
2. Replication lag gây ra hiện tượng gì? Định nghĩa eventual consistency. *(mục 2, tr. 162)*
3. Vì sao "pick 2 of 3" sai? Phát biểu CAP đúng hơn là gì? *(mục 3, tr. 337)*
4. Chạy demo mục 4. Giải thích bước (2) và sự khác biệt AP vs CP ở bước (4). *(mục 4)*
5. Cho ba dữ liệu cần nhất quán mạnh và ba dữ liệu eventual là đủ. Lý do? *(mục 5)*
6. DynamoDB eventually vs strongly consistent read khác nhau gì? Multi-AZ RDS nghiêng CAP phía nào khi failover? *(mục 6)*

## Tóm tắt một trang

```
BÀI 8 — DISTRIBUTED TRỤ 3b: NHÂN BẢN & NHẤT QUÁN (CAP)
─────────────────────────────────────────────────────────
NHÂN BẢN  giữ bản sao cùng dữ liệu trên nhiều máy (DDIA tr.151).
   Lý do: (1) gần user→giảm latency (Mạng); (2) chịu lỗi→tăng availability.

EVENTUAL CONSISTENCY  follower áp sau leader → replication lag → đọc thấy
   giá trị CŨ, nhưng "rốt cuộc sẽ hội tụ" (tr.162). Lời hứa yếu: không hẹn giờ.

CAP (đúng)  "pick 2 of 3" SAI vì partition là SỰ CỐ, không phải lựa chọn.
   Đúng: "Consistent or Available WHEN Partitioned" (tr.337). Mạng khoẻ = cả
   hai; CHỈ khi partition mới phải chọn: từ chối (C) hay phục vụ cũ (A).

DEMO  (2) follower trả 1 khi leader đã 2 (lag). (3) hội tụ về 2.
   (4) partition: AP trả x=2 (cũ, sẵn sàng); CP từ chối (không nói dối).

CHỌN  "đọc cũ 1 giây có hại thật không?" Số dư/tồn kho/khoá → mạnh.
   Like/view/feed/cache → eventual (rẻ+nhanh). = tinh thần TCP vs UDP.

NỐI VỀ AWS  DynamoDB eventual(mặc định) vs strong read; Multi-AZ RDS
   nhân bản tăng availability (failover nghiêng CP); Aurora Global = lag/eventual.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 5 (Replication)**: định nghĩa & lý do (tr. 151), eventual consistency (tr. 162); **ch. 9 (Consistency and Consensus)**: CAP "Consistent or Available when Partitioned" (tr. 337). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (DynamoDB consistency, Multi-AZ RDS).
- Tiếp: [Bài 9 — phân mảnh & consensus](bai_09_dist-phan-manh.md) — làm sao các bản sao *đồng ý* một giá trị (quorum/consensus), và làm sao chia dữ liệu quá lớn cho một máy (sharding).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · **[Bài 8 — Distributed: nhân bản & nhất quán] ← bạn đang ở đây** · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
