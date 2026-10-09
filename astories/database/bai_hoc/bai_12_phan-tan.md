# Bài 12 — Song song và phân tán (góc database)

> [!info] Về bài này
> **Bài cuối.** Mười một bài trước giả định *một máy*. Nhưng dữ liệu lớn hơn một máy, hoặc cần chịu lỗi phần cứng → phải trải ra **nhiều node**. Bài này nhìn phân tán *từ góc database engine*: chia bảng bằng **phân mảnh (partitioning/sharding)**, và giữ nguyên tử xuyên node bằng **two-phase commit (2PC)**. Giữ ở mức "góc DB" — phần sâu về CAP, consensus, nhân bản nằm ở mạch cloud ([`cloud-base`](../../cloud-base/README.md)). Rồi khép lại cả khoá.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch20–23 (Parallel & Distributed Databases)**; **Red Book** (*Readings in Database Systems* 5e) (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 9 — ACID](bai_09_transaction-acid.md), [Bài 11 — recovery & log](bai_11_recovery.md). Đào sâu: [cloud-base Bài 9 — phân mảnh & consensus](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 16 — transaction & saga](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md).

## Mục lục

1. [Vượt giới hạn một máy](#1-vượt-giới-hạn-một-máy)
2. [Phân mảnh: chia bảng ra nhiều node](#2-phân-mảnh-chia-bảng-ra-nhiều-node)
3. [Giao dịch phân tán: two-phase commit](#3-giao-dịch-phân-tán-two-phase-commit)
4. [Cái giá của phân tán, và khép khoá](#4-cái-giá-của-phân-tán-và-khép-khoá)
5. [Demo: hash partition và 2PC](#5-demo-hash-partition-và-2pc)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Vượt giới hạn một máy

Một máy có trần: RAM, đĩa, CPU hữu hạn. Khi bảng lớn hơn đĩa một máy, hoặc tải vượt sức một CPU, hoặc ta cần sống sót khi *cả máy* chết — phải trải dữ liệu ra **nhiều node**. Đây không còn là lựa chọn ngoại lệ:

> [!quote] Red Book
> "Cloud computing and microarchitectural trends have made distribution and parallelism nearly ubiquitous concerns."
>
> *Điện toán đám mây và các xu hướng vi kiến trúc đã khiến **phân tán và song song** trở thành mối quan tâm **gần như phổ quát**.*

Phân tán mở ra hai câu hỏi mới mà một máy không có: **(1)** dữ liệu nằm ở node nào (phân mảnh, mục 2)? **(2)** một giao dịch đụng *nhiều* node thì làm sao vẫn *nguyên tử* (2PC, mục 3)? Nó cũng mang theo một cái giá đắt (mục 4) — và chính cái giá đó là lý do có cả một mạch khoá riêng về hệ phân tán.

## 2. Phân mảnh: chia bảng ra nhiều node

Cách cơ bản để trải dữ liệu: cắt bảng theo *hàng*, mỗi hàng về một node.

> [!quote] Silberschatz (tr. 1004)
> "the tuples of a relation are partitioned (divided) among many nodes, so that each tuple resides on one node; such partitioning is referred to as horizontal partitioning."
>
> *các bộ của một quan hệ được **chia** ra nhiều node, mỗi bộ nằm trên **đúng một** node; cách chia này gọi là **phân mảnh ngang** (horizontal partitioning).*

Có ba chiến lược cơ bản (tr. 1005):

- **Round-robin**: rải lần lượt bộ thứ *i* về node `(i mod n)` — đều tăm tắp, nhưng tra một khoá phải hỏi *mọi* node.
- **Range partitioning**: chia theo *khoảng giá trị* (node 1 giữ `[-∞,15)`, node 2 giữ `[15,40)`...). Tra khoảng (range query) hiệu quả, nhưng dễ *lệch tải* (skew) nếu dữ liệu dồn một khoảng.
- **Hash partitioning**: băm khoá để chọn node.

> [!quote] Silberschatz (tr. 1005)
> "A hash function is chosen whose range is {1, 2, …, n}. Each tuple of the original relation is hashed on the partitioning attributes. If the hash function returns i, then the tuple is placed on node Ni."
>
> *Chọn một hàm băm có miền {1,…,n}. Mỗi bộ được **băm theo thuộc tính phân mảnh**; nếu hàm băm trả về i thì bộ nằm trên **node Ni**.*

Hash phân mảnh *đều* và cho phép tra một khoá bằng cách **chỉ hỏi một node** (`node = hash(key)`) — không quét cả cụm. Giá: range query lại phải hỏi mọi node (vì khoá liền nhau rải khắp nơi). *Không có chiến lược nào thắng mọi mặt* — đúng tinh thần cả khoá: mỗi lựa chọn là một đánh đổi. (Demo mục 5 dựng hash partitioning.)

## 3. Giao dịch phân tán: two-phase commit

Khi một giao dịch đụng dữ liệu ở *nhiều* node, bài toán nguyên tử (Bài 9, 11) khó hơn hẳn: phải commit ở **tất cả** node hoặc abort ở **tất cả**, dù mỗi node có thể tự sập. Giao thức kinh điển: **two-phase commit (2PC)**, điều phối bởi một **coordinator**.

- **Pha 1 — prepare (chuẩn bị).** Coordinator ghi `<prepare T>` rồi hỏi mọi node tham gia "sẵn sàng commit chưa?". Mỗi node *ghi log* phần của mình xuống bộ nhớ bền (dùng chính WAL của Bài 11), rồi bỏ phiếu: `ready` (sẵn sàng, không rút lại được) hoặc `no` (từ chối).
- **Pha 2 — quyết định.** Coordinator gom phiếu:

> [!quote] Silberschatz (tr. 1101)
> "Transaction T can be committed if Ci received a ready T message from all the participating nodes. Otherwise, transaction T must be aborted."
>
> *Giao dịch T **được commit nếu** coordinator nhận `ready` từ **tất cả** node. **Ngược lại**, T **phải abort**.*

Một phiếu `no` (hoặc một node im lặng quá hạn) → **abort toàn cục**. Quyết định được ghi log `<commit T>`/`<abort T>` rồi gửi tới mọi node để chúng làm theo. Mấu chốt: *một khi đã bỏ phiếu `ready`, node không được tự ý quyết* — nó phải chờ lệnh coordinator. Điều này cho nguyên tử xuyên node, nhưng cũng là nguồn gốc điểm yếu lớn nhất (mục 4).

## 4. Cái giá của phân tán, và khép khoá

2PC giữ được nguyên tử, nhưng có một tử huyệt: **blocking**. Nếu coordinator *sập* sau khi các node đã bỏ phiếu `ready` nhưng *trước khi* gửi quyết định, các node đó bị **kẹt** — đã khoá dữ liệu, đã hứa commit, không được tự quyết, chỉ biết chờ coordinator sống lại. Đây là lý do hệ phân tán hiện đại dùng những giao thức mạnh hơn (**consensus** như Paxos/Raft, hoặc tránh giao dịch phân tán bằng **saga**).

Và đó cũng là ranh giới tự nhiên của khoá này. Những câu hỏi lớn của phân tán — nhân bản (replication), nhất quán vs sẵn sàng (**CAP**), đồng thuận (consensus), phân vùng mạng — là *cả một lĩnh vực*, được đào sâu ở mạch cloud: [cloud-base Bài 8 (nhất quán/CAP)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md), [Bài 9 (phân mảnh & consensus)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 16 (2PC vs saga)](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md). Khoá `database` dừng ở việc *chỉ ra cánh cửa* đó từ bên trong engine.

> [!note] Khép khoá — hành trình 13 bài
> Ta đã mở nắp ca-pô một database engine, từ ngoài vào trong:
> - **Nền (0–3)**: vì sao có DBMS → mô hình quan hệ & đại số → SQL → thiết kế & chuẩn hoá.
> - **Ruột (4–8)**: dữ liệu trên đĩa & buffer → index B+tree → LSM/bitmap → thuật toán join → tối ưu truy vấn.
> - **Đúng đắn (9–11)**: ACID & serializability → 2PL/MVCC → WAL/ARIES phục hồi.
> - **Mở rộng (12)**: phân mảnh & 2PC → cánh cửa sang hệ phân tán.
>
> Giờ khi bạn gõ một câu `SELECT ... JOIN ... WHERE`, bạn *thấy* được chuyện gì xảy ra: parse thành đại số, optimizer chọn kế hoạch dựa trên thống kê, join bằng hash hay merge, đọc qua B+tree và buffer, tất cả gói trong một giao dịch có khoá và log để đúng cả khi sập. Đó là mục tiêu của khoá: không còn coi database là hộp đen.

## 5. Demo: hash partition và 2PC

Phần A: hash partitioning rải 12 khoá ra 4 node, tra một khoá chỉ hỏi một node. Phần B: 2PC commit khi mọi node `ready`, abort khi một node `no`:

```typescript
import { strict as assert } from "node:assert";

// ─── PHẦN A: HASH PARTITIONING (sharding) — chia bảng ra nhiều node ───
// Một bảng quá lớn cho một máy → băm khoá, mỗi tuple về đúng một node. Truy vấn
// theo khoá chỉ hỏi MỘT node (không quét cả cụm).
const NODES = 4;
function hashNode(key: string): number {            // băm tất định → node 1..NODES
  let h = 0; for (const c of key) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return (h % NODES) + 1;
}
const keys = Array.from({ length: 12 }, (_, i) => `user${i + 1}`);
const dist = new Map<number, string[]>();
for (const k of keys) { const n = hashNode(k); (dist.get(n) ?? dist.set(n, []).get(n)!).push(k); }

console.log("PHẦN A — hash partitioning 12 khoá / 4 node:");
for (let n = 1; n <= NODES; n++) console.log(`  Node ${n}: ${(dist.get(n) ?? []).join(", ")}`);
console.log(`  truy vấn 'user7' → chỉ hỏi Node ${hashNode("user7")} (không quét cả cụm)`);
assert.equal(keys.length, [...dist.values()].reduce((s, a) => s + a.length, 0));  // không mất khoá

// ─── PHẦN B: TWO-PHASE COMMIT (2PC) — giao dịch nguyên tử trên NHIỀU node ───
// Một giao dịch đụng nhiều node phải commit ở TẤT CẢ hoặc abort ở TẤT CẢ.
// Pha 1 (prepare): coordinator hỏi, mỗi node bỏ phiếu ready/no.
// Pha 2 (decide): CHỈ commit nếu MỌI node ready; chỉ một no → abort toàn cục.
type Vote = "ready" | "no";
function twoPC(label: string, participants: { node: string; vote: Vote }[]): string {
  console.log(`  [${label}]`);
  console.log(`    Pha 1 prepare → phiếu: ${participants.map(p => `${p.node}=${p.vote}`).join(", ")}`);
  const decision = participants.every(p => p.vote === "ready") ? "COMMIT" : "ABORT";
  console.log(`    Pha 2 quyết định → ${decision} ở MỌI node` + (decision === "ABORT" ? " (vì có node bỏ phiếu 'no')" : " (vì mọi node 'ready')"));
  return decision;
}

console.log("\nPHẦN B — two-phase commit (2PC):");
const ok = twoPC("mọi node sẵn sàng", [{ node: "N1", vote: "ready" }, { node: "N2", vote: "ready" }, { node: "N3", vote: "ready" }]);
const bad = twoPC("một node từ chối", [{ node: "N1", vote: "ready" }, { node: "N2", vote: "no" }, { node: "N3", vote: "ready" }]);
assert.equal(ok, "COMMIT"); assert.equal(bad, "ABORT");
console.log("  → 2PC giữ atomicity XUYÊN NODE: toàn-commit hoặc toàn-abort. Giá: nếu coordinator");
console.log("    sập sau 'prepare', các node 'ready' bị KẸT chờ (blocking) — điểm yếu kinh điển của 2PC.");
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — hash partitioning 12 khoá / 4 node:
  Node 1: user3, user7, user12
  Node 2: user4, user8
  Node 3: user1, user5, user9, user10
  Node 4: user2, user6, user11
  truy vấn 'user7' → chỉ hỏi Node 1 (không quét cả cụm)

PHẦN B — two-phase commit (2PC):
  [mọi node sẵn sàng]
    Pha 1 prepare → phiếu: N1=ready, N2=ready, N3=ready
    Pha 2 quyết định → COMMIT ở MỌI node (vì mọi node 'ready')
  [một node từ chối]
    Pha 1 prepare → phiếu: N1=ready, N2=no, N3=ready
    Pha 2 quyết định → ABORT ở MỌI node (vì có node bỏ phiếu 'no')
  → 2PC giữ atomicity XUYÊN NODE: toàn-commit hoặc toàn-abort. Giá: nếu coordinator
    sập sau 'prepare', các node 'ready' bị KẸT chờ (blocking) — điểm yếu kinh điển của 2PC.
```

Bốn điều đáng thấm. **(1)** Hash rải 12 khoá khá đều ra 4 node (2–4 khoá/node) — đó là ưu điểm "đều" của hash partitioning. **(2)** Tra `user7` chỉ cần đi tới **Node 1** (`hash(user7)`), không hỏi ba node kia — truy vấn điểm (point query) rẻ. (Nhưng range query thì phải hỏi cả bốn — đánh đổi của hash.) **(3)** 2PC: mọi node `ready` → **COMMIT đồng loạt**; chỉ cần **một** `no` → **ABORT đồng loạt** — nguyên tử được giữ *xuyên node*. **(4)** Cái giá ẩn: nếu coordinator sập giữa pha 1 và pha 2, các node đã `ready` bị **kẹt** — đây là *blocking*, tử huyệt khiến hệ hiện đại tìm tới consensus/saga.

> [!note] Tự thử
> 1. Đổi `NODES` từ 4 lên 6: phân bố 12 khoá đổi thế nào? Vì sao thêm/bớt node làm *nhiều* khoá phải chuyển chỗ (gợi ý: `hash % n` đổi khi `n` đổi → tìm hiểu *consistent hashing* ở cloud-base)?
> 2. Vì sao hash partitioning tệ cho `WHERE age BETWEEN 20 AND 30`? Range partitioning tốt hơn ở đâu, tệ hơn ở đâu? *(mục 2)*
> 3. Trong 2PC, nếu một node im lặng (không trả lời) quá hạn, coordinator nên làm gì? *(mục 3)*
> 4. Mô tả kịch bản blocking cụ thể: coordinator sập đúng lúc nào thì N1 (đã `ready`) kẹt? Saga (cloud-base Bài 16) né vấn đề này bằng cách nào? *(mục 4)*

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
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | **Song song & phân tán (góc DB)** ← *đang ở đây* | mở rộng ra nhiều máy | Ch20–23 + Red Book |

**Hết khoá.** Bước tiếp: mạch cloud cho chiều sâu hệ phân tán — [`cloud-base`](../../cloud-base/README.md) (trụ Distributed & Dữ liệu, từ DDIA), và lên các tầng [`aws-fund`](../../aws-fund/README.md), [`aws-design`](../../aws-design/README.md), [`sre`](../../sre/README.md).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 12.1 — Vì sao phải phân tán dữ liệu ra nhiều node?
> **Đáp:** một máy có trần (RAM/đĩa/CPU) và có thể chết cả máy. Phân tán để *mở rộng* (dữ liệu/tải lớn hơn một máy) và *chịu lỗi*.

> [!question] Thẻ 12.2 — Horizontal partitioning là gì? Ba chiến lược cơ bản?
> **Đáp:** chia *hàng* của bảng ra nhiều node, mỗi hàng một node. **Round-robin** (đều, nhưng tra phải hỏi mọi node), **range** (tốt cho range query, dễ lệch tải), **hash** (đều + point query chỉ hỏi một node, nhưng range query phải hỏi mọi node).

> [!question] Thẻ 12.3 — Hai pha của 2PC là gì?
> **Đáp:** **Pha 1 (prepare)**: coordinator hỏi, mỗi node ghi log & bỏ phiếu `ready`/`no`. **Pha 2 (decide)**: commit *nếu mọi node ready*, ngược lại abort — rồi báo mọi node làm theo.

> [!question] Thẻ 12.4 — Quy tắc quyết định của 2PC? Điểm yếu lớn nhất?
> **Đáp:** commit ⟺ **tất cả** node `ready`; chỉ một `no`/im lặng → **abort toàn cục**. Điểm yếu: **blocking** — coordinator sập sau prepare thì node đã `ready` bị kẹt chờ.

> [!question] Thẻ 12.5 — Khoá database dừng ở đâu, mạch cloud nối tiếp gì?
> **Đáp:** khoá này chỉ ra *cánh cửa* phân tán từ trong engine (partition, 2PC). Chiều sâu — CAP, replication, consensus (Paxos/Raft), saga — ở [[cloud-base]] và các tầng cloud.

## 8. Câu hỏi tự kiểm tra

1. Nêu hai động lực để phân tán dữ liệu. Phân tán mở ra hai câu hỏi mới nào? *(mục 1)*
2. So sánh round-robin, range, hash partitioning: mỗi cái mạnh/yếu ở loại truy vấn nào? *(mục 2, 5)*
3. Mô tả hai pha của 2PC. Vì sao một node đã bỏ phiếu `ready` thì không được tự quyết? *(mục 3)*
4. Giải thích vấn đề blocking của 2PC. Vì sao nó dẫn tới consensus và saga? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 1 (đổi số node). Vì sao `hash % n` làm nhiều khoá đổi chỗ khi `n` đổi? *(mục 5)*

## Tóm tắt một trang

```
BÀI 12 — SONG SONG & PHÂN TÁN (GÓC DB)  [BÀI CUỐI]
─────────────────────────────────────────────────────────
VÌ SAO  một máy có trần + chết cả máy → trải ra NHIỀU NODE để mở rộng & chịu lỗi.
   "distribution and parallelism nearly ubiquitous" (Red Book).

PHÂN MẢNH NGANG (tr.1004)  chia HÀNG ra node, mỗi hàng 1 node. Chiến lược (tr.1005):
   round-robin (đều, tra hỏi mọi node) / range (range query tốt, dễ skew) /
   HASH (đều + point query chỉ 1 node, range query phải hỏi mọi node).

2PC — TWO-PHASE COMMIT  nguyên tử XUYÊN NODE. Pha 1 prepare: node ghi log + bỏ phiếu
   ready/no. Pha 2: COMMIT ⟺ MỌI node ready, else ABORT toàn cục (tr.1101). Node đã
   ready KHÔNG tự quyết. ĐIỂM YẾU: BLOCKING (coordinator sập sau prepare → kẹt).

KHÉP KHOÁ  nền(0-3) → ruột engine(4-8) → đúng đắn(9-11) → phân tán(12). Chiều sâu
   phân tán (CAP, replication, consensus, saga) → mạch cloud (cloud-base→...→sre).

DEMO  hash 12 khoá/4 node, tra user7→Node 1. 2PC: mọi ready→COMMIT; một no→ABORT.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch21 Parallel and Distributed Storage**: phân mảnh ngang (tr. 1004), chiến lược hash/range/round-robin (tr. 1005); **Ch23 Parallel and Distributed Transaction Processing**: two-phase commit (tr. 1101). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- **Bailis, Hellerstein, Stonebraker (biên tập) — *Readings in Database Systems*, 5th ed. (Red Book, 2015)** — phân tán & song song là mối quan tâm phổ quát. `tai_lieu/Readings in Database Systems 5th Edition.pdf`.
- Đào sâu phân tán: [cloud-base Bài 8 (CAP)](../../cloud-base/bai_hoc/bai_08_dist-nhat-quan.md), [Bài 9 (phân mảnh & consensus)](../../cloud-base/bai_hoc/bai_09_dist-phan-manh.md), [Bài 16 (2PC vs saga)](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Xử lý truy vấn: join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn (cost-based)](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID, isolation](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · **[Bài 12 — Song song & phân tán] ← bạn đang ở đây**

Xem thêm [README khoá học](../README.md).
