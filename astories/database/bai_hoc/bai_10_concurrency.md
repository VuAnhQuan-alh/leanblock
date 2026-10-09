# Bài 10 — Đồng thời: 2PL và MVCC

> [!info] Về bài này
> Bài 9 nói *Isolation* nghĩa là mọi lịch phải **serializable**. Bài này là cơ chế *thực thi* điều đó: **concurrency control**. Hai dòng lớn: khoá (**2PL** — two-phase locking) đảm bảo serializable nhưng đẻ ra **deadlock**; và đa phiên bản (**MVCC / snapshot isolation**) cho reader *không bao giờ chờ*. Ta tự dựng một **lock manager** có phát hiện deadlock, và một mô hình snapshot.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch18 (Concurrency Control)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 9 — ACID & serializability](bai_09_transaction-acid.md). Liên hệ: [cloud-base Bài 13 — OS lock](../../cloud-base/bai_hoc/bai_13_os-scheduling-locks.md).

## Mục lục

1. [Vì sao cần điều khiển đồng thời](#1-vì-sao-cần-điều-khiển-đồng-thời)
2. [Khoá chia sẻ và độc quyền](#2-khoá-chia-sẻ-và-độc-quyền)
3. [Two-phase locking (2PL)](#3-two-phase-locking-2pl)
4. [Deadlock và MVCC](#4-deadlock-và-mvcc)
5. [Demo: lock manager, deadlock, snapshot](#5-demo-lock-manager-deadlock-snapshot)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Vì sao cần điều khiển đồng thời

Bài 9 cho thấy đan xen sai → **lost update**, dữ liệu hỏng. Nhưng chạy *tuần tự* (một giao dịch một lúc) thì phí phạm khủng khiếp. **Concurrency control** là bộ phận cho phép nhiều giao dịch chạy song song *mà vẫn* chỉ sinh ra các lịch **serializable** (Bài 9). Cách phổ biến nhất: bắt giao dịch **xin khoá (lock)** trước khi đụng dữ liệu, và quản lý các khoá đó sao cho không ai giẫm lên ai.

## 2. Khoá chia sẻ và độc quyền

Có hai chế độ khoá, phân biệt theo *đọc* hay *ghi*:

> [!quote] Silberschatz (tr. 835)
> "Shared. If a transaction Ti has obtained a shared-mode lock (denoted by S) on item Q, then Ti can read, but cannot write, Q."

> [!quote] Silberschatz (tr. 835)
> "Exclusive. If a transaction Ti has obtained an exclusive-mode lock (denoted by X) on item Q, then Ti can both read and write Q."

- **Shared (S)** — "khoá đọc": nhiều giao dịch *cùng* đọc một mục được. (Đọc không hại đọc.)
- **Exclusive (X)** — "khoá ghi": chỉ *một* giao dịch, ai đang giữ thì không ai khác được S hay X.

Luật kết hợp (lock-compatibility matrix) gói trong một câu:

> [!quote] Silberschatz (tr. 836)
> "shared mode is compatible with shared mode, but not with exclusive mode."
>
> *S hợp với S, nhưng **không** hợp với X.*

```
           muốn S   muốn X
   giữ S    OK       CHỜ
   giữ X    CHỜ      CHỜ      (chỉ S-S là cùng lúc được)
```

Nếu mục đã bị khoá ở chế độ *không tương thích*, giao dịch xin khoá phải **chờ** tới khi khoá kia được nhả. Chính cái "chờ" này vừa cho ta tính đúng, vừa đẻ ra deadlock (mục 4).

## 3. Two-phase locking (2PL)

Chỉ cấp/nhả khoá tuỳ tiện thì *chưa* đủ đảm bảo serializable. Cần một *giao thức*:

> [!quote] Silberschatz (tr. 841)
> "One protocol that ensures serializability is the two-phase locking protocol. [...] 1. Growing phase. A transaction may obtain locks, but may not release any lock. 2. Shrinking phase. A transaction may release locks, but may not obtain any new locks."
>
> *Một giao thức đảm bảo serializability là **two-phase locking (2PL)**. [...] 1. **Pha tăng** (growing): giao dịch được **lấy** khoá, **không được nhả**. 2. **Pha giảm** (shrinking): được **nhả** khoá, **không được lấy** thêm.*

Hình dung: mỗi giao dịch *gom hết khoá cần trước* (pha tăng) rồi mới bắt đầu *nhả* (pha giảm) — một khi đã nhả khoá đầu tiên thì không xin thêm được nữa. Điểm giao dịch lấy khoá cuối cùng gọi là *lock point*; sắp các giao dịch theo lock point cho ta một thứ tự tuần tự.

> [!quote] Silberschatz (tr. 841)
> "We can show that the two-phase locking protocol ensures conflict serializability."

Đó là lời hứa lớn: cứ theo 2PL thì **mọi** lịch sinh ra đều serializable → không lo lost update. Nhưng có cái giá:

> [!quote] Silberschatz (tr. 841)
> "Two-phase locking does not ensure freedom from deadlock."
>
> *2PL **không** đảm bảo thoát khỏi deadlock.*

## 4. Deadlock và MVCC

**Deadlock** (khoá chết): hai giao dịch chờ nhau vòng tròn, không ai đi tiếp được.

> [!quote] Silberschatz (tr. 838)
> "where neither of these transactions can ever proceed with its normal execution. This situation is called deadlock. When deadlock occurs, the system must roll back one of the two transactions."
>
> *khi **không** giao dịch nào có thể đi tiếp. Tình huống này gọi là **deadlock**. Khi xảy ra, hệ phải **cuộn (rollback) một** trong hai giao dịch.*

Ví dụ kinh điển: T3 giữ X(B) và xin X(A); T4 giữ S(A) và xin S(B). T3 chờ T4, T4 chờ T3 → vòng tròn. Cách phát hiện: dựng **đồ thị wait-for** (cạnh `Ti → Tj` nghĩa "Ti chờ Tj"); có **chu trình** = có deadlock. Hệ chọn một **nạn nhân** cuộn lại để phá vòng. (Có cách *phòng* deadlock — sắp thứ tự khoá, timeout, wait-die/wound-wait — nhưng phát hiện-rồi-cuộn là phổ biến.)

**MVCC / snapshot isolation** — hướng hoàn toàn khác, tránh khoá cho việc đọc:

> [!quote] Silberschatz (tr. 873)
> "Conceptually, snapshot isolation involves giving a transaction a "snapshot" of the database at the time when it begins its execution. It then operates on that snapshot in complete isolation from concurrent transactions. The data values in the snapshot consist only of values written by committed transactions."
>
> *Snapshot isolation cho mỗi giao dịch một **"ảnh chụp"** CSDL **tại lúc nó bắt đầu**, chỉ gồm giá trị **đã commit**. Giao dịch làm việc trên ảnh đó, cô lập hoàn toàn với các giao dịch song song.*

Ý tưởng: giữ **nhiều phiên bản (multiversion)** của mỗi mục. Writer tạo *phiên bản mới*; reader cũ vẫn thấy *phiên bản cũ* ứng với ảnh chụp của mình → **reader không bao giờ chờ writer, và ngược lại**. Lý tưởng cho truy vấn báo cáo (read-only). Giá: hai writer cùng sửa một mục phải *kiểm tra khi commit* (first-committer-wins) và tốn chỗ lưu nhiều phiên bản. PostgreSQL, Oracle, MySQL-InnoDB đều dựa trên MVCC. Demo mục 5 dựng cả lock manager (2PL + deadlock) lẫn snapshot.

## 5. Demo: lock manager, deadlock, snapshot

Phần A: lock manager thật với ma trận tương thích, tái hiện deadlock T3/T4 và **phát hiện bằng chu trình wait-for**, rồi cuộn nạn nhân. Phần B: MVCC — reader giữ ảnh chụp cũ, không chờ writer:

```typescript
import { strict as assert } from "node:assert";

// ─── PHẦN A: lock manager (S/X), 2PL, và PHÁT HIỆN DEADLOCK ───
// Khoá chia sẻ (S): đọc được, không ghi. Khoá độc quyền (X): đọc+ghi. S hợp S,
// nhưng X xung đột mọi thứ. 2PL (two-phase locking) đảm bảo serializable nhưng
// KHÔNG tránh được deadlock → phải PHÁT HIỆN (chu trình trong đồ thị wait-for) rồi
// cuộn (rollback) một "nạn nhân".
type Mode = "S" | "X";
type Hold = { txn: string; mode: Mode };
const compatible = (a: Mode, b: Mode) => a === "S" && b === "S";   // chỉ S-S là hợp

class LockManager {
  holders = new Map<string, Hold[]>();          // item → danh sách khoá đang giữ
  waitFor = new Map<string, Set<string>>();     // txn → tập txn mà nó đang chờ

  private hasCycle(): string[] | null {          // DFS tìm chu trình trong wait-for
    const WHITE = 0, GRAY = 1, BLACK = 2;
    const color = new Map<string, number>(), stack: string[] = [];
    const dfs = (u: string): string[] | null => {
      color.set(u, GRAY); stack.push(u);
      for (const v of this.waitFor.get(u) ?? []) {
        if (color.get(v) === GRAY) return [...stack.slice(stack.indexOf(v)), v];
        if ((color.get(v) ?? WHITE) === WHITE) { const c = dfs(v); if (c) return c; }
      }
      color.set(u, BLACK); stack.pop(); return null;
    };
    for (const u of this.waitFor.keys()) if ((color.get(u) ?? WHITE) === WHITE) { const c = dfs(u); if (c) return c; }
    return null;
  }

  request(txn: string, item: string, mode: Mode): string {
    const held = this.holders.get(item) ?? [];
    const conflicts = held.filter(h => h.txn !== txn && !compatible(h.mode, mode));
    if (conflicts.length === 0) {                 // cấp được
      this.holders.set(item, [...held, { txn, mode }]);
      return `${txn} lock-${mode}(${item}): CẤP`;
    }
    // phải chờ → thêm cạnh wait-for tới mọi txn đang giữ khoá xung đột
    const set = this.waitFor.get(txn) ?? new Set<string>();
    for (const c of conflicts) set.add(c.txn);
    this.waitFor.set(txn, set);
    const cyc = this.hasCycle();
    return `${txn} lock-${mode}(${item}): CHỜ ${[...set].join(",")}` + (cyc ? `  ← DEADLOCK! chu trình ${cyc.join("→")}` : "");
  }
  release(txn: string) {                          // nạn nhân nhả hết khoá + xoá cạnh chờ
    for (const [it, hs] of this.holders) this.holders.set(it, hs.filter(h => h.txn !== txn));
    this.waitFor.delete(txn);
    for (const s of this.waitFor.values()) s.delete(txn);
  }
}

console.log("PHẦN A — lock manager + deadlock:");
const lm = new LockManager();
console.log("  tính hợp khoá: S-S =", compatible("S", "S"), ", S-X =", compatible("S", "X"), ", X-X =", compatible("X", "X"));
console.log("  " + lm.request("T1", "A", "S"));   // cấp
console.log("  " + lm.request("T2", "A", "S"));   // S hợp S → cấp (nhiều reader cùng lúc)
console.log("  " + lm.request("T2", "A", "X"));   // muốn ghi A nhưng T1 đang giữ S → chờ
const lm2 = new LockManager();
console.log("  --- dựng deadlock kinh điển (T3,T4) ---");
console.log("  " + lm2.request("T3", "B", "X"));  // T3 giữ X(B)
console.log("  " + lm2.request("T4", "A", "S"));  // T4 giữ S(A)
console.log("  " + lm2.request("T4", "B", "S"));  // T4 chờ T3 (B đang X)
const r = lm2.request("T3", "A", "X");            // T3 chờ T4 (A đang S) → CHU TRÌNH
console.log("  " + r);
assert.ok(r.includes("DEADLOCK"));
lm2.release("T4");                                 // cuộn nạn nhân T4
console.log("  → rollback nạn nhân T4; giờ T3 lock-X(A):", lm2.request("T3", "A", "X").includes("CẤP") ? "CẤP (deadlock đã gỡ)" : "vẫn chờ");

// ─── PHẦN B: MVCC / snapshot isolation — reader KHÔNG chờ ───
// Mỗi giao dịch thấy "ảnh chụp" CSDL lúc nó bắt đầu, chỉ gồm giá trị đã COMMIT.
// Writer cập nhật bản mới; reader cũ vẫn thấy bản cũ → không khoá, không chờ.
type Version = { value: number; committedAt: number };
let clock = 0;
const versions: Version[] = [{ value: 100, committedAt: clock }];   // giá trị ban đầu = 100
const snapshotAt = (ts: number) => [...versions].reverse().find(v => v.committedAt <= ts)!.value;

console.log("\nPHẦN B — MVCC / snapshot isolation:");
const readerStart = ++clock;                      // T_reader bắt đầu, chụp ảnh tại ts này
console.log(`  T_reader đọc (snapshot @${readerStart}):`, snapshotAt(readerStart));
versions.push({ value: 200, committedAt: ++clock });   // T_writer ghi 200 và COMMIT
console.log(`  T_writer commit 200 @${clock}`);
console.log(`  T_reader đọc LẠI (vẫn snapshot @${readerStart}):`, snapshotAt(readerStart), "← không đổi, KHÔNG phải chờ T_writer");
const newTxn = ++clock;
console.log(`  giao dịch MỚI (@${newTxn}) đọc:`, snapshotAt(newTxn), "← thấy bản mới đã commit");
assert.equal(snapshotAt(readerStart), 100);
assert.equal(snapshotAt(newTxn), 200);
console.log("  → reader-only không bao giờ phải chờ hay bị huỷ (lý tưởng cho báo cáo).");
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — lock manager + deadlock:
  tính hợp khoá: S-S = true , S-X = false , X-X = false
  T1 lock-S(A): CẤP
  T2 lock-S(A): CẤP
  T2 lock-X(A): CHỜ T1
  --- dựng deadlock kinh điển (T3,T4) ---
  T3 lock-X(B): CẤP
  T4 lock-S(A): CẤP
  T4 lock-S(B): CHỜ T3
  T3 lock-X(A): CHỜ T4  ← DEADLOCK! chu trình T4→T3→T4
  → rollback nạn nhân T4; giờ T3 lock-X(A): CẤP (deadlock đã gỡ)

PHẦN B — MVCC / snapshot isolation:
  T_reader đọc (snapshot @1): 100
  T_writer commit 200 @2
  T_reader đọc LẠI (vẫn snapshot @1): 100 ← không đổi, KHÔNG phải chờ T_writer
  giao dịch MỚI (@3) đọc: 200 ← thấy bản mới đã commit
  → reader-only không bao giờ phải chờ hay bị huỷ (lý tưởng cho báo cáo).
```

Bốn điều đáng thấm. **(1)** Ma trận tương thích: `S-S=true` nên `T1` và `T2` cùng đọc `A` được; nhưng `T2` muốn `X(A)` để ghi thì phải **chờ** `T1` nhả — đọc nhiều cùng lúc, ghi thì độc quyền. **(2)** Deadlock dựng đúng như sách: `T4→T3→T4` là **chu trình** trong đồ thị wait-for → phát hiện tức thì. **(3)** Gỡ bằng cách **cuộn nạn nhân** `T4`; vòng tròn vỡ, `T3` lấy được `X(A)` ngay — đúng "roll back one of the two transactions" (tr. 838). **(4)** MVCC: `T_reader` thấy `100` *suốt đời giao dịch* dù `T_writer` đã commit `200` ở giữa — nó đọc từ **ảnh chụp** riêng, **không chờ** ai; giao dịch mới mở sau thì thấy `200`. Reader và writer không chặn nhau — đó là sức mạnh của đa phiên bản.

> [!note] Tự thử
> 1. Trong phần A, đổi `T2 lock-X(A)` thành `T2 lock-S(A)` lần hai: còn phải chờ không? Vì sao khoá đọc không chặn khoá đọc?
> 2. Dựng deadlock *ba* giao dịch: T3→T4→T5→T3. Bộ phát hiện chu trình có bắt được không (nó dùng DFS)? Nạn nhân nên chọn ai?
> 3. Phần B: cho *hai* writer cùng dựa trên snapshot @1 rồi cùng muốn ghi — snapshot isolation xử lý xung đột ghi-ghi thế nào (gợi ý: first-committer-wins, kiểm tra lúc commit)?
> 4. Vì sao 2PL "đảm bảo serializable" mà *vẫn* có thể deadlock? Hai tính chất này độc lập ra sao? *(mục 3, 4)*

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | **Đồng thời: 2PL / MVCC** ← *đang ở đây* | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Bài 10 lo chữ **I** (cô lập). Còn một mảnh của tính đúng đắn: chữ **A** và **D** khi máy *sập* — Bài 11.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 10.1 — Khoá S và X khác nhau ra sao? Ma trận tương thích?
> **Đáp:** **S** (shared) = đọc, nhiều người cùng giữ được. **X** (exclusive) = đọc+ghi, độc quyền. Chỉ **S-S** tương thích; S-X, X-X đều xung đột (phải chờ).

> [!question] Thẻ 10.2 — Two-phase locking là gì? Nó đảm bảo gì?
> **Đáp:** hai pha: **growing** (chỉ lấy khoá) rồi **shrinking** (chỉ nhả). Đảm bảo **conflict serializability** — mọi lịch theo 2PL đều serializable.

> [!question] Thẻ 10.3 — 2PL có tránh được deadlock không?
> **Đáp:** **Không**. 2PL đảm bảo serializable nhưng *vẫn* có thể deadlock — hai tính chất độc lập.

> [!question] Thẻ 10.4 — Deadlock là gì? Phát hiện và xử lý ra sao?
> **Đáp:** các giao dịch chờ nhau **vòng tròn**, không ai đi tiếp. Phát hiện = **chu trình** trong đồ thị wait-for. Xử lý = **cuộn (rollback) một nạn nhân** để phá vòng.

> [!question] Thẻ 10.5 — MVCC / snapshot isolation hoạt động thế nào? Lợi gì?
> **Đáp:** giữ **nhiều phiên bản**; mỗi giao dịch đọc **ảnh chụp** lúc nó bắt đầu (chỉ giá trị đã commit). Reader **không chờ** writer và ngược lại → lý tưởng cho read-only. Giá: xung đột ghi-ghi kiểm lúc commit + tốn chỗ.

## 8. Câu hỏi tự kiểm tra

1. Vì sao cho đọc song song (S-S) nhưng ghi phải độc quyền (X)? *(mục 2)*
2. Phát biểu hai pha của 2PL. Vì sao nó đảm bảo serializability? *(mục 3)*
3. Dựng ví dụ deadlock hai giao dịch. Mô tả đồ thị wait-for và cách phát hiện. *(mục 4, 5)*
4. MVCC khác khoá ở chỗ nào về việc reader/writer chặn nhau? Đánh đổi của MVCC là gì? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 4. Vì sao "serializable" và "không deadlock" là hai chuyện khác nhau? *(mục 3, 5)*

## Tóm tắt một trang

```
BÀI 10 — ĐỒNG THỜI: 2PL / MVCC
─────────────────────────────────────────────────────────
KHOÁ  S (shared/đọc, nhiều người) vs X (exclusive/ghi, độc quyền). Chỉ S-S hợp;
   S-X, X-X phải CHỜ (tr.835-836). "Chờ" cho đúng nhưng đẻ deadlock.

2PL (two-phase locking, tr.841)  GROWING (chỉ lấy khoá) → SHRINKING (chỉ nhả).
   Đảm bảo CONFLICT SERIALIZABILITY. NHƯNG không tránh được deadlock.

DEADLOCK (tr.838)  chờ nhau VÒNG TRÒN → không ai đi. Phát hiện = CHU TRÌNH trong
   đồ thị WAIT-FOR. Xử lý = cuộn (rollback) một NẠN NHÂN phá vòng.

MVCC / SNAPSHOT ISOLATION (tr.873)  giữ NHIỀU PHIÊN BẢN; mỗi giao dịch đọc ẢNH CHỤP
   lúc bắt đầu (chỉ giá trị đã commit). Reader KHÔNG chờ writer ↔ lý tưởng read-only.
   Xung đột ghi-ghi: first-committer-wins. Nền của PostgreSQL/Oracle/InnoDB.

DEMO  lock: S-S cấp, S-X chờ; deadlock T4→T3→T4 phát hiện → cuộn T4 → gỡ. MVCC:
   reader thấy 100 suốt đời dù writer commit 200; txn mới thấy 200. Không chặn nhau.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch18 Concurrency Control**: khoá shared/exclusive (tr. 835), tương thích S-X (tr. 836), deadlock (tr. 838), two-phase locking & conflict serializability & không-tránh-deadlock (tr. 841), snapshot isolation (tr. 873). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [Bài 9 — serializability](bai_09_transaction-acid.md), [cloud-base Bài 13 — lock & mutex ở tầng OS](../../cloud-base/bai_hoc/bai_13_os-scheduling-locks.md); [Bài 11 — recovery](bai_11_recovery.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Xử lý truy vấn: join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn (cost-based)](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID, isolation](bai_09_transaction-acid.md) · **[Bài 10 — Đồng thời: 2PL/MVCC] ← bạn đang ở đây** · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
