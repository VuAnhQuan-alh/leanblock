# Bài 13 — OS nâng cao: Scheduling, locks và deadlock

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 1 (OS).** [Bài 1](bai_01_os-ao-hoa.md) nói OS *luân phiên* CPU (time-sharing); bài này hỏi *luân phiên theo luật nào* — **scheduling**. [Bài 2](bai_02_os-concurrency.md) nói race condition cần bảo vệ vùng tới hạn; bài này đưa công cụ chính thức — **lock (mutex)** — và cái bẫy đi kèm: **deadlock**. Đây là nền để hiểu **CPU credit của T-instances, Lambda concurrency/throttling, và DB deadlock / distributed lock** ở `aws-fund`.
> Nguồn: **OSTEP** — ch. 7 (Scheduling), ch. 28 (Locks), ch. 32 (Common Concurrency Problems).
> **Trích:** `OSTEP (tr. X)` = trang **in**; **offset PDF = tr. + 25**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 1 — ảo hoá](bai_01_os-ao-hoa.md), [Bài 2 — concurrency](bai_02_os-concurrency.md).

## Mục lục

1. [Scheduling: ai chạy trước, chạy bao lâu](#1-scheduling-ai-chạy-trước-chạy-bao-lâu)
2. [Lock: biến vùng tới hạn thành atomic](#2-lock-biến-vùng-tới-hạn-thành-atomic)
3. [Deadlock: bốn điều kiện của sự kẹt](#3-deadlock-bốn-điều-kiện-của-sự-kẹt)
4. [Demo: deadlock và cách phá vòng chờ](#4-demo-deadlock-và-cách-phá-vòng-chờ)
5. [Bảng so sánh: bốn điều kiện và cách phá](#5-bảng-so-sánh-bốn-điều-kiện-và-cách-phá)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Scheduling: ai chạy trước, chạy bao lâu

Time-sharing (Bài 1) nói OS luân phiên CPU; *chính sách* quyết định luân phiên ra sao là **scheduling**. Nó cân giữa hai thước đo kéo ngược nhau. Một là **turnaround** (xong sớm); thước còn lại sinh ra từ máy tương tác:

> [!quote] OSTEP (tr. 70)
> "We define response time as the time from when the job arrives in a system to the first time it is scheduled."
>
> *Ta định nghĩa **response time (thời gian phản hồi)** là khoảng từ lúc job đến hệ thống tới **lần đầu tiên nó được xếp cho chạy**.*

Hai thước đo này đối chọi: chạy xong một job dài rồi mới tới job khác thì *turnaround* tốt nhưng *response* tệ (job sau chờ lâu mới được chạm CPU). Lời giải phổ biến là **Round-Robin** — cho mỗi job một lát (time slice) rồi chuyển. Nhưng lát bao lâu?

> [!quote] OSTEP (tr. 72)
> "making the time slice too short is problematic: suddenly the cost of context switching will dominate overall performance. Thus, deciding on the length of the time slice presents a trade-off to a system designer."
>
> *đặt time slice **quá ngắn** lại sinh chuyện: đột nhiên **chi phí context switch chiếm lĩnh** toàn bộ hiệu năng. Nên chọn độ dài time slice là một **đánh đổi** của người thiết kế hệ thống.*

Đây là context switch của Bài 1 hiện thành chi phí: luân phiên càng mượt (lát ngắn) càng phản hồi nhanh, nhưng mỗi lần chuyển tốn công lưu/nạp machine state — ngắn quá thì phí sạch vào việc chuyển. Scheduling thực tế (như MLFQ) học thói quen job để vừa phản hồi nhanh cho việc tương tác, vừa không bỏ đói việc nền.

## 2. Lock: biến vùng tới hạn thành atomic

Bài 2 nói vùng tới hạn (critical section) cần "all or nothing". Công cụ chính thức để đạt điều đó khi lập trình là **lock**:

> [!quote] OSTEP (tr. 314)
> "annotate source code with locks, putting them around critical sections, and thus ensure that any such critical section executes as if it were a single atomic instruction."
>
> *đặt **lock** quanh các **critical section** trong mã nguồn, nhờ đó bảo đảm mỗi critical section chạy **như thể nó là một lệnh atomic đơn lẻ**.*

Lock làm điều đó bằng cách loại trừ lẫn nhau — đúng tên gọi của nó:

> [!quote] OSTEP (tr. 315)
> "The name that the POSIX library uses for a lock is a mutex, as it is used to provide mutual exclusion between threads, i.e., if one thread is in the critical section, it excludes the others from entering until it has completed the section."
>
> *Tên mà thư viện POSIX dùng cho lock là **mutex**, vì nó cung cấp **loại trừ lẫn nhau (mutual exclusion)** giữa các thread: nếu một thread đang trong critical section, nó **loại trừ các thread khác** khỏi việc vào cho tới khi nó xong.*

Lock là câu trả lời "khoá" ở bảng ba-chiến-lược của Bài 2. Nhưng nó mở ra một lớp lỗi mới, trầm trọng không kém race: khi nhiều lock đan vào nhau, hệ có thể **kẹt cứng mãi mãi**.

## 3. Deadlock: bốn điều kiện của sự kẹt

> [!quote] OSTEP (tr. 397)
> "Four conditions need to hold for a deadlock to occur [...] If any of these four conditions are not met, deadlock cannot occur."
>
> ***Bốn điều kiện phải cùng đúng** thì deadlock mới xảy ra. [...] Nếu **bất kỳ điều kiện nào trong bốn không thoả**, deadlock **không thể** xảy ra.*

Bốn điều kiện (OSTEP tr. 397), và chính chúng chỉ ra cách chữa — phá một cái là đủ:

1. **Mutual exclusion** — tài nguyên bị chiếm độc quyền (một lock).
2. **Hold-and-wait** — giữ tài nguyên đã có *trong khi* chờ tài nguyên khác.
3. **No preemption** — không thể cưỡng ép lấy lại tài nguyên từ kẻ đang giữ.
4. **Circular wait** — có một *vòng tròn* các thread, mỗi thread giữ thứ mà thread kế trong vòng đang xin.

Mẹo thực chiến phổ biến nhất là phá điều kiện (4): **áp một thứ tự khoá toàn cục** — ai cũng xin lock theo cùng một thứ tự (ví dụ luôn lock có id nhỏ trước). Khi đó không bao giờ hình thành được vòng tròn. Demo mục 4 dựng đúng cái vòng đó rồi phá nó bằng thứ tự khoá.

## 4. Demo: deadlock và cách phá vòng chờ

Hai "thread" T1, T2 và hai khoá L1, L2. Kịch bản (1): mỗi thread lấy khoá theo thứ tự *ngược nhau* → vòng chờ → deadlock (dò bằng đồ thị waits-for). Kịch bản (2): áp thứ tự khoá toàn cục → không thành vòng.

```typescript
// Deadlock: hai thread mỗi bên giữ một khoá và chờ khoá bên kia → vòng chờ
// (circular wait) → kẹt mãi. Mô phỏng tất định bằng đồ thị "waits-for" + dò
// chu trình. Cách chữa kinh điển: ÁP THỨ TỰ KHOÁ TOÀN CỤC (phá circular wait).
class LockManager {
  #owner = new Map<string, string>();      // lock -> thread đang giữ
  #waits: Array<[string, string]> = [];     // cạnh thread -> thread (đang chờ)
  // trả về true nếu cấp được; false nếu phải chờ (ghi cạnh waits-for)
  acquire(thread: string, lock: string): boolean {
    const held = this.#owner.get(lock);
    if (held === undefined) { this.#owner.set(lock, thread); return true; }
    if (held === thread) return true;
    this.#waits.push([thread, held]);        // thread chờ kẻ đang giữ lock
    return false;
  }
  // dò chu trình trong đồ thị waits-for = deadlock
  deadlockCycle(): string[] | null {
    const adj = new Map<string, string[]>();
    for (const [a, b] of this.#waits) (adj.get(a) ?? adj.set(a, []).get(a)!).push(b);
    for (const start of adj.keys()) {
      const path: string[] = []; const seen = new Set<string>();
      const dfs = (n: string): string[] | null => {
        if (seen.has(n)) return n === start ? [...path, n] : null;
        seen.add(n); path.push(n);
        for (const m of adj.get(n) ?? []) { const r = dfs(m); if (r) return r; }
        path.pop(); return null;
      };
      const r = dfs(start); if (r && r[0] === r[r.length - 1]) return r;
    }
    return null;
  }
}

// --- (1) KHÔNG thứ tự: T1 giữ L1 xin L2; T2 giữ L2 xin L1 ---
const m1 = new LockManager();
m1.acquire("T1", "L1"); m1.acquire("T2", "L2");   // mỗi bên giữ 1 khoá
const g1 = m1.acquire("T1", "L2");                 // T1 xin L2 (T2 đang giữ) → chờ
const g2 = m1.acquire("T2", "L1");                 // T2 xin L1 (T1 đang giữ) → chờ
const cyc = m1.deadlockCycle();
console.log("(1) Lấy khoá theo thứ tự NGƯỢC nhau:");
console.log(`    T1 xin L2: ${g1 ? "được" : "CHỜ"}; T2 xin L1: ${g2 ? "được" : "CHỜ"}`);
console.log(`    waits-for có chu trình? ${cyc ? "CÓ → DEADLOCK: " + cyc.join(" → ") : "không"}`);

// --- (2) CÓ thứ tự toàn cục: ai cũng lấy L1 trước, rồi L2 ---
const m2 = new LockManager();
const order = ["L1", "L2"];
function takeInOrder(mgr: LockManager, t: string): boolean {
  for (const l of order) if (!mgr.acquire(t, l)) return false;  // nếu kẹt thì nhả & thử lại (ở đây minh hoạ)
  return true;
}
const okT1 = takeInOrder(m2, "T1");                // T1 lấy L1,L2
const okT2 = takeInOrder(m2, "T2");                // T2 xin L1 (T1 giữ) → chờ, KHÔNG ôm L2
console.log("\n(2) Áp THỨ TỰ KHOÁ toàn cục (L1 trước L2):");
console.log(`    T1 lấy đủ: ${okT1}; T2: ${okT2 ? "đủ" : "chờ L1 (nhưng KHÔNG ôm L2)"}`);
console.log(`    waits-for có chu trình? ${m2.deadlockCycle() ? "CÓ" : "KHÔNG → không deadlock"}`);
console.log("\nPhá 1 trong 4 điều kiện (circular wait) là đủ chặn deadlock (OSTEP tr.397).");
```

Kết quả chạy thật *(tất định)*:

```
(1) Lấy khoá theo thứ tự NGƯỢC nhau:
    T1 xin L2: CHỜ; T2 xin L1: CHỜ
    waits-for có chu trình? CÓ → DEADLOCK: T1 → T2 → T1

(2) Áp THỨ TỰ KHOÁ toàn cục (L1 trước L2):
    T1 lấy đủ: true; T2: chờ L1 (nhưng KHÔNG ôm L2)
    waits-for có chu trình? KHÔNG → không deadlock

Phá 1 trong 4 điều kiện (circular wait) là đủ chặn deadlock (OSTEP tr.397).
```

Kịch bản (1): cả hai đều CHỜ, và đồ thị waits-for khép thành vòng `T1 → T2 → T1` — đó *là* deadlock, không ai nhả, kẹt mãi. Kịch bản (2): T2 cũng phải chờ, nhưng vì chưa kịp ôm L2 (nó xin L1 trước và trượt ngay), nó *không giữ gì trong khi chờ* theo cách tạo vòng → T1 chạy xong sẽ nhả, T2 tiếp tục. Chỉ một quy tắc "luôn lấy khoá theo cùng thứ tự" đã phá điều kiện (4). Lưu ý: lock giải race (Bài 2) nhưng *đẻ* ra deadlock — đổi một lớp lỗi lấy một lớp lỗi khác, nên hệ hiện đại thường tránh lock nhiều khi có thể (atomic, không chia sẻ — bảng Bài 2).

> [!note] Tự thử
> - Thêm L3 và một vòng ba thread (T1→T2→T3→T1): `deadlockCycle` vẫn bắt được — deadlock không giới hạn ở hai bên.
> - Bỏ điều kiện (2) thay vì (4): cho thread xin *cả hai* khoá cùng lúc (all-or-nothing), trượt thì nhả hết. Đó là một cách phá "hold-and-wait".
> - Đổi scenario (1) cho T2 cũng theo thứ tự L1→L2: tái hiện kịch bản (2) — thấy thứ tự khoá là yếu tố quyết định, không phải bản thân việc có hai khoá.

## 5. Bảng so sánh: bốn điều kiện và cách phá

Vì deadlock cần *cả bốn* điều kiện, chặn *một* là đủ. Mỗi cột là một chiến lược thực chiến:

| Điều kiện (phải cùng đúng) | Nghĩa                              | Phá nó bằng cách                          | Ví dụ thực tế                       |
| :------------------------- | :--------------------------------- | :---------------------------------------- | :---------------------------------- |
| Mutual exclusion           | tài nguyên chiếm độc quyền         | dùng cấu trúc lock-free / atomic          | `Atomics` (Bài 2), CAS              |
| Hold-and-wait              | giữ cái này, chờ cái kia           | xin **tất cả** khoá cùng lúc, trượt thì nhả | two-phase locking, `tryLock` + nhả |
| No preemption              | không cưỡng lấy lại được           | cho phép **timeout + nhả** rồi thử lại    | `tryLock(timeout)`, lock lease      |
| **Circular wait**          | vòng tròn thread chờ nhau          | **áp thứ tự khoá toàn cục** (dễ nhất)     | luôn lock id nhỏ trước (demo)       |

Quy luật: **"circular wait" thường là mắt dễ phá nhất** — chỉ cần một quy ước thứ tự, không đổi logic. Đây là lý do mọi hướng dẫn về lock đều nhấn "luôn lấy khoá theo cùng một thứ tự". Và ở quy mô phân tán, cùng bài toán tái sinh: *distributed lock* phải có **lease/timeout** (phá điều kiện 3) vì một node giữ khoá có thể *chết* (Bài 7) — không ai cưỡng lấy lại được nếu không có hạn.

## 6. Nối về AWS

> [!note] Nối về AWS
> Scheduling và khoá tưởng xa, nhưng hiện diện khắp cloud — xem [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md) và [Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **CPU credit của T-instances = scheduling phí.** Instance `t3/t4g` tích/tiêu "credit" để được chia CPU; cạn credit → bị bóp (throttle) — đúng tinh thần "chia CPU công bằng theo chính sách" của mục 1. Workload CPU đều đặn nên chọn `c`/`m`, không `t`.
> - **Lambda reserved/provisioned concurrency = scheduling job.** Giới hạn concurrency quyết định bao nhiêu lời gọi chạy "cùng lúc" vs xếp hàng/throttle — chính là turnaround vs response của mục 1 ở mức dịch vụ.
> - **DB deadlock là thật.** RDS/Aurora (và cả DynamoDB khi khoá) có thể deadlock khi hai transaction lấy khoá hàng theo thứ tự ngược — engine phát hiện chu trình (như demo) và **huỷ một transaction** (deadlock victim). Chữa: luôn truy cập bảng/hàng theo cùng thứ tự.
> - **Distributed lock phải có lease.** Khi dùng DynamoDB/Redis làm khoá phân tán, luôn đặt **TTL/lease** — vì node giữ khoá có thể chết (Bài 7), và "no preemption" mà không có timeout = kẹt vĩnh viễn. Đây là điều kiện (3) của mục 5 áp vào mạng.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 13.1 — Turnaround và response time đối chọi ra sao?
> **Đáp:** turnaround = xong sớm; response = sớm được *chạm CPU lần đầu*. Chạy hết job dài trước thì turnaround tốt nhưng response tệ. Round-Robin đổi turnaround lấy response.

> [!question] Thẻ 13.2 — Vì sao time slice quá ngắn lại hại?
> **Đáp:** chi phí **context switch** (lưu/nạp machine state, Bài 1) chiếm lĩnh hiệu năng. Chọn độ dài slice là đánh đổi: đủ ngắn để phản hồi nhanh, đủ dài để khỏi phí vào việc chuyển.

> [!question] Thẻ 13.3 — Lock (mutex) làm gì? Quan hệ với atomicity (Bài 2)?
> **Đáp:** cung cấp **mutual exclusion** — một thread trong critical section loại trừ thread khác. Hiệu quả: critical section chạy "như một lệnh atomic đơn lẻ" (chính là "all or nothing" của Bài 2).

> [!question] Thẻ 13.4 — Bốn điều kiện deadlock? Chặn bao nhiêu là đủ?
> **Đáp:** mutual exclusion · hold-and-wait · no preemption · circular wait. Phải cùng đúng cả bốn → **phá một cái là đủ** chặn deadlock.

> [!question] Thẻ 13.5 — Cách phá deadlock dễ nhất trong thực tế?
> **Đáp:** phá **circular wait** bằng **thứ tự khoá toàn cục** (luôn lấy khoá theo cùng thứ tự). Không đổi logic, chỉ cần một quy ước.

> [!question] Thẻ 13.6 — Vì sao distributed lock phải có lease/TTL?
> **Đáp:** node giữ khoá có thể **chết** (Bài 7) và "no preemption" nghĩa là không ai cưỡng lấy lại được → kẹt vĩnh viễn. Lease/timeout phá điều kiện (3).

## 8. Câu hỏi tự kiểm tra

1. Định nghĩa response time. Vì sao nó đối chọi với turnaround? *(mục 1, tr. 70)*
2. Vì sao time slice quá ngắn phản tác dụng? Liên hệ context switch Bài 1. *(mục 1, tr. 72)*
3. Lock/mutex làm gì? Nối với atomicity "all or nothing" của Bài 2 ra sao? *(mục 2, tr. 314–315)*
4. Kể bốn điều kiện deadlock. Vì sao phá một là đủ? *(mục 3, tr. 397)*
5. Chạy demo mục 4. Giải thích vòng `T1→T2→T1` và vì sao thứ tự khoá phá được nó. *(mục 4)*
6. DB deadlock xử lý thế nào? Vì sao distributed lock cần lease? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 13 — OS NÂNG CAO: SCHEDULING · LOCKS · DEADLOCK
─────────────────────────────────────────────────────────
SCHEDULING  chính sách luân phiên CPU (Bài 1). Hai thước đo đối chọi:
   turnaround (xong sớm) vs response (sớm chạm CPU, tr.70). Round-Robin đổi
   cái này lấy cái kia; slice quá ngắn → context switch nuốt hiệu năng (tr.72).

LOCK (mutex)  đặt quanh critical section → chạy "như một lệnh atomic đơn lẻ"
   (tr.314); mutual exclusion (tr.315). = "khoá" ở bảng 3 chiến lược Bài 2.

DEADLOCK  4 điều kiện phải CÙNG đúng (tr.397): mutual exclusion · hold-and-
   wait · no preemption · circular wait. Phá MỘT là đủ. Dễ nhất: phá circular
   wait bằng THỨ TỰ KHOÁ toàn cục.

DEMO  T1,T2 lấy L1/L2 ngược nhau → waits-for khép vòng T1→T2→T1 = DEADLOCK.
   Áp thứ tự L1-trước-L2 → không thành vòng. Lock giải race nhưng đẻ deadlock.

NỐI VỀ AWS  CPU credit T-instances = scheduling phí; Lambda concurrency =
   turnaround/response; DB deadlock → engine huỷ 1 transaction (victim);
   distributed lock PHẢI có lease/TTL (node giữ khoá có thể chết — Bài 7).
```

## Nguồn

- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **ch. 7 (Scheduling: Introduction)**: response time & time-slice trade-off (tr. 70, 72); **ch. 28 (Locks)**: lock = atomic critical section, mutex/mutual exclusion (tr. 314–315); **ch. 32 (Common Concurrency Problems)**: bốn điều kiện deadlock (tr. 397). `tai_lieu/Operating systems three easy pieces.pdf` — **offset PDF = tr. + 25**.
- Nối về AWS: [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md), [Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md).
- Mở rộng của [Bài 1 — ảo hoá](bai_01_os-ao-hoa.md) và [Bài 2 — concurrency](bai_02_os-concurrency.md); distributed lock nối [Bài 7 — thất bại](bai_07_dist-giao-tiep.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · **[Bài 13 — OS nâng cao: scheduling & locks] ← bạn đang ở đây** · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
