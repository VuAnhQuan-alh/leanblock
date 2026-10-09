# Bài 11 — Phục hồi: WAL và ARIES

> [!info] Về bài này
> Bài 9–10 lo chữ **I** (cô lập). Bài này lo nốt **A** và **D**: khi máy **sập** giữa chừng — mất điện, kernel panic — database phải tỉnh dậy ở một trạng thái *nhất quán*, không nửa nạc nửa mỡ. Cơ chế: **ghi nhật ký trước khi làm** (write-ahead logging), rồi khi khởi động lại dùng log để **redo** việc đã commit và **undo** việc chưa commit. Ta tự dựng một WAL và chạy phục hồi sau "sập".
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch19 (Recovery System)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 9 — ACID (atomicity, durability)](bai_09_transaction-acid.md), [Bài 4 — buffer & dirty page](bai_04_luu-tru-buffer.md).

## Mục lục

1. [Sập giữa chừng: chữ A và D chưa xong](#1-sập-giữa-chừng-chữ-a-và-d-chưa-xong)
2. [Log: ghi nhật ký trước khi làm](#2-log-ghi-nhật-ký-trước-khi-làm)
3. [Redo và undo](#3-redo-và-undo)
4. [Checkpoint và ARIES](#4-checkpoint-và-aries)
5. [Demo: WAL phục hồi sau khi sập](#5-demo-wal-phục-hồi-sau-khi-sập)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Sập giữa chừng: chữ A và D chưa xong

Chuyển \$100 từ A sang B là *hai* phép ghi. Giả sử engine trừ A rồi — đúng lúc đó **mất điện**. Khi bật lại: A đã bị trừ, B chưa được cộng → tiền bốc hơi (vi phạm **Atomicity**). Hoặc ngược lại: giao dịch *đã commit*, báo người dùng "xong", nhưng thay đổi còn nằm trong **buffer** (Bài 4) chưa kịp ghi đĩa → mất điện làm mất luôn (vi phạm **Durability**).

Vấn đề gốc: RAM (buffer) *bay hơi*, còn việc ghi xuống đĩa thì **không đồng bộ** với lúc commit. Hai tình huống trái ngược cần hai hành động trái ngược khi phục hồi:

- Giao dịch **đã commit** mà thay đổi *chưa* xuống đĩa → phải **làm lại (redo)** để giữ Durability.
- Giao dịch **chưa commit** mà thay đổi *đã* lỡ xuống đĩa → phải **cuộn lại (undo)** để giữ Atomicity.

Làm sao biết cái nào cần redo, cái nào undo, sau khi RAM đã mất sạch? Câu trả lời: một cuốn **nhật ký (log)** nằm trên bộ nhớ bền.

## 2. Log: ghi nhật ký trước khi làm

> [!quote] Silberschatz (tr. 913)
> "The most widely used structure for recording database modifications is the log. The log is a sequence of log records, recording all the update activities in the database."
>
> *Cấu trúc phổ biến nhất để ghi lại các thay đổi là **log** (nhật ký) — một **chuỗi bản ghi** ghi lại **mọi** hoạt động cập nhật.*

Mỗi phép ghi sinh ra một **update log record** dạng `<Ti, Xj, V1, V2>`: giao dịch Ti ghi mục Xj, giá trị **cũ** là V1, giá trị **mới** là V2. Kèm các bản ghi sự kiện: `<Ti start>`, `<Ti commit>`, `<Ti abort>`. Ghi *cả* old lẫn new là chìa khoá: có **new** để redo, có **old** để undo.

Luật vàng — **write-ahead logging (WAL)**:

> [!quote] Silberschatz (tr. 913)
> "Whenever a transaction performs a write, it is essential that the log record for that write be created and added to the log, before the database is modified."
>
> *Mỗi khi giao dịch ghi, **bắt buộc** bản ghi log cho phép ghi đó phải được tạo và thêm vào log **TRƯỚC KHI** CSDL bị sửa.*

Thứ tự này là tất cả. Vì log (ở bộ nhớ bền) *luôn đi trước* thay đổi dữ liệu, nên khi sập, *bất kể* đĩa đang ở trạng thái dở dang nào, **log luôn có đủ thông tin** để dựng lại sự thật: cái gì đã commit (redo tới new), cái gì chưa (undo về old). Nếu làm ngược — sửa dữ liệu trước, ghi log sau — thì một cú sập giữa hai bước làm mất dấu, không cách nào phục hồi.

## 3. Redo và undo

Hai thủ tục phục hồi, cả hai đọc từ log:

> [!quote] Silberschatz (tr. 918)
> "redo(Ti). The procedure sets the value of all data items updated by transaction Ti to the new values."
>
> ***redo(Ti)**: đặt *mọi* mục mà Ti đã cập nhật về **giá trị mới**.*

> [!quote] Silberschatz (tr. 918)
> "undo(Ti). The procedure restores the value of all data items updated by transaction Ti to the old values."
>
> ***undo(Ti)**: khôi phục *mọi* mục mà Ti đã cập nhật về **giá trị cũ**.*

Sau khi sập, hệ quét log và phân loại từng giao dịch theo một luật đơn giản mà đẹp:

> [!quote] Silberschatz (tr. 919)
> "Transaction Ti needs to be undone if the log contains the record <Ti start> but does not contain either the record <Ti commit> or the record <Ti abort>."
>
> *Giao dịch Ti cần **undo** nếu log có `<Ti start>` **nhưng không** có `<Ti commit>` hay `<Ti abort>`.*

Ngược lại, Ti cần **redo** nếu log có `<Ti start>` **và** có `<Ti commit>`. Tóm gọn:

```
   log có <Ti start> ...
        + có <Ti commit>   → REDO (áp giá trị MỚI — làm bền, Durability)
        + KHÔNG commit     → UNDO (trả giá trị CŨ — cuộn lại, Atomicity)
```

Thứ tự quan trọng: **redo quét xuôi** (từ đầu log tới cuối, giữ đúng thứ tự cập nhật gốc); **undo quét ngược** (từ cuối về đầu, tháo dỡ theo thứ tự ngược). Demo mục 5 làm đúng vậy.

## 4. Checkpoint và ARIES

Nếu mỗi lần phục hồi phải quét *toàn bộ* log từ thuở khai thiên thì quá chậm. **Checkpoint** là một cái mốc cắt bớt:

> [!quote] Silberschatz (tr. 921)
> "Output onto stable storage a log record of the form <checkpoint L>, where L is a list of transactions active at the time of the checkpoint."
>
> *Ghi xuống bộ nhớ bền một bản ghi `<checkpoint L>`, với L là **danh sách giao dịch đang hoạt động** lúc checkpoint.*

Tại checkpoint, hệ flush mọi buffer bẩn xuống đĩa và ghi mốc. Khi phục hồi, chỉ cần quét *từ checkpoint gần nhất* trở đi — mọi thứ trước đó đã chắc chắn trên đĩa. Đánh đổi cổ điển: checkpoint thường hơn → phục hồi nhanh hơn nhưng tốn I/O lúc chạy bình thường.

Thuật toán phục hồi dùng trong thực tế:

> [!quote] Silberschatz (tr. 941)
> "The state of the art in recovery methods is best illustrated by the ARIES recovery method."
>
> *Trình độ tân tiến nhất của phương pháp phục hồi được thể hiện rõ nhất qua **ARIES**.*

**ARIES** (IBM) tinh chỉnh ý tưởng trên bằng **LSN (log sequence number)** — mỗi bản ghi log và mỗi trang dữ liệu mang một số thứ tự, cho phép biết *chính xác* trang đã áp bản ghi nào, để **không redo thừa**. ARIES chạy ba pha: **Analysis** (từ checkpoint, xác định trang bẩn & giao dịch dở), **Redo** (áp lại mọi thay đổi đã ghi log — kể cả của giao dịch sẽ bị undo), **Undo** (cuộn các giao dịch chưa commit). Hầu hết DBMS lớn (DB2, SQL Server; PostgreSQL theo tinh thần ARIES) đều theo ARIES. Chi tiết LSN ta để sách; demo mục 5 cài phiên bản redo/undo cốt lõi.

## 5. Demo: WAL phục hồi sau khi sập

Dựng WAL, cho T1 commit (nhưng buffer chưa kịp ghi đĩa) và T2 chưa commit (nhưng đã lỡ ghi đĩa), rồi "sập" và phục hồi — thấy redo cứu Durability, undo cứu Atomicity:

```typescript
import { strict as assert } from "node:assert";

// Phục hồi dựa trên LOG (write-ahead logging). Mỗi thay đổi: GHI LOG (txn, item,
// old, new) vào "đĩa log" TRƯỚC khi đụng dữ liệu. Sau khi sập, quét log:
//  - REDO (áp giá trị MỚI) cho giao dịch ĐÃ commit  → đảm bảo Durability
//  - UNDO (trả giá trị CŨ) cho giao dịch CHƯA commit → đảm bảo Atomicity
type Rec =
  | { type: "start" | "commit"; txn: string }
  | { type: "update"; txn: string; item: string; old: number; new: number };

const disk: Record<string, number> = { A: 1000, B: 1000, C: 1000 };   // CSDL bền trên đĩa
const wal: Rec[] = [];                                                  // log bền trên đĩa

function start(txn: string)  { wal.push({ type: "start",  txn }); }
function commit(txn: string) { wal.push({ type: "commit", txn }); }
// WAL: ghi bản ghi log (có OLD + NEW) TRƯỚC; flushToDisk mô phỏng buffer đã/chưa xuống đĩa
function write(txn: string, item: string, val: number, flushToDisk: boolean) {
  wal.push({ type: "update", txn, item, old: disk[item], new: val });
  if (flushToDisk) disk[item] = val;
}

// --- Trước khi sập ---
// T1 chuyển: A 1000→1500, rồi COMMIT. NHƯNG buffer CHƯA kịp ghi đĩa (flush=false).
start("T1"); write("T1", "A", 1500, false); commit("T1");
// T2 ghi C 1000→9999 và buffer ĐÃ xuống đĩa (flush=true) — nhưng CHƯA commit thì... SẬP.
start("T2"); write("T2", "C", 9999, true);
console.log("Ngay trước khi SẬP:");
console.log("  đĩa:", JSON.stringify(disk), " ← A chưa kịp ghi (1000), C đã ghi bẩn (9999)");
console.log("  log:", wal.map(r => r.type === "update" ? `<${r.txn} ${r.item} ${r.old}→${r.new}>` : `<${r.txn} ${r.type}>`).join(" "));

// ===== CRASH ===== (mất RAM; chỉ còn ĐĨA + LOG)
console.log("\n*** CRASH *** → chạy phục hồi từ log:");
const committed = new Set(wal.filter(r => r.type === "commit").map(r => r.txn));
// REDO: quét XUÔI, áp giá trị MỚI cho giao dịch đã commit
for (const r of wal)
  if (r.type === "update" && committed.has(r.txn)) { disk[r.item] = r.new; console.log(`  REDO  ${r.txn}: ${r.item} = ${r.new} (đã commit → làm bền)`); }
// UNDO: quét NGƯỢC, trả giá trị CŨ cho giao dịch chưa commit
for (let i = wal.length - 1; i >= 0; i--) {
  const r = wal[i];
  if (r.type === "update" && !committed.has(r.txn)) { disk[r.item] = r.old; console.log(`  UNDO  ${r.txn}: ${r.item} = ${r.old} (chưa commit → cuộn lại)`); }
}

console.log("\nSau phục hồi — đĩa:", JSON.stringify(disk));
assert.deepEqual(disk, { A: 1500, B: 1000, C: 1000 });
console.log("  → A=1500 (T1 commit được REDO: Durability); C=1000 (T2 chưa commit được UNDO: Atomicity).");
console.log("  Nhờ GHI LOG TRƯỚC (có old+new), phục hồi mới có đủ dữ liệu để redo lẫn undo.");
```

Kết quả chạy thật *(tất định)*:

```
Ngay trước khi SẬP:
  đĩa: {"A":1000,"B":1000,"C":9999}  ← A chưa kịp ghi (1000), C đã ghi bẩn (9999)
  log: <T1 start> <T1 A 1000→1500> <T1 commit> <T2 start> <T2 C 1000→9999>

*** CRASH *** → chạy phục hồi từ log:
  REDO  T1: A = 1500 (đã commit → làm bền)
  UNDO  T2: C = 1000 (chưa commit → cuộn lại)

Sau phục hồi — đĩa: {"A":1500,"B":1000,"C":1000}
  → A=1500 (T1 commit được REDO: Durability); C=1000 (T2 chưa commit được UNDO: Atomicity).
  Nhờ GHI LOG TRƯỚC (có old+new), phục hồi mới có đủ dữ liệu để redo lẫn undo.
```

Bốn điều đáng thấm. **(1)** Ngay trước khi sập, đĩa *không nhất quán*: thay đổi đã-commit của T1 (`A=1500`) **chưa** tới đĩa, còn thay đổi chưa-commit của T2 (`C=9999`) **đã** tới đĩa — đúng cái trạng thái dở dang mà mất điện gây ra. **(2)** Log thì *đầy đủ*: có `<T1 commit>` nhưng không có `<T2 commit>` — đủ để phân loại. **(3)** Phục hồi **REDO T1** (áp `A=1500` từ *new value*) → thay đổi đã commit *không mất* (Durability); **UNDO T2** (trả `C=1000` từ *old value*) → thay đổi chưa commit *biến mất sạch* (Atomicity). **(4)** Cả hai chỉ làm được vì log chứa *cả* old lẫn new và được ghi *trước* khi đụng đĩa — đó là toàn bộ sức mạnh của WAL.

> [!note] Tự thử
> 1. Đổi T1 thành *chưa* commit (bỏ `commit("T1")`) nhưng cho `write` của nó `flush=true`. Sau phục hồi A bằng bao nhiêu? Vì sao?
> 2. Thêm `abort("T2")` (một bản ghi `<T2 abort>`). Theo luật mục 3, T2 giờ cần redo hay undo? Kết quả cuối có đổi không?
> 3. Vì sao phải UNDO *quét ngược* mà REDO *quét xuôi*? Cho ví dụ một giao dịch ghi cùng một item hai lần để thấy thứ tự quan trọng. *(mục 3)*
> 4. Bỏ việc ghi `old` vào log (chỉ lưu `new`). Thao tác nào *không* còn làm được khi phục hồi? *(mục 2, 3)*
> 5. Thêm một `<checkpoint>` giữa T1 và T2. Phục hồi có cần quét phần log trước checkpoint không? *(mục 4)*

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
| 11 | **Phục hồi: WAL / ARIES** ← *đang ở đây* | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Hết phần **tính đúng đắn một máy** (Bài 9–11): ACID giờ đủ cả A, C, I, D. Bài 12 — bài cuối — bước ra **nhiều máy**.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 11.1 — Vì sao sập giữa chừng đe doạ cả Atomicity lẫn Durability?
> **Đáp:** buffer (RAM) bay hơi và việc ghi đĩa *không đồng bộ* với commit. → giao dịch *đã commit* có thể chưa kịp xuống đĩa (mất Durability); giao dịch *chưa commit* có thể đã lỡ xuống đĩa (mất Atomicity).

> [!question] Thẻ 11.2 — Luật write-ahead logging (WAL) là gì?
> **Đáp:** bản ghi log của một phép ghi phải vào log (bộ nhớ bền) **TRƯỚC KHI** CSDL bị sửa. → log luôn đủ thông tin phục hồi dù đĩa dở dang.

> [!question] Thẻ 11.3 — Một update log record chứa gì? Vì sao cần cả old lẫn new?
> **Đáp:** `<Ti, Xj, old, new>`. Cần **new** để **redo**, **old** để **undo**.

> [!question] Thẻ 11.4 — Sau khi sập, khi nào redo một giao dịch, khi nào undo?
> **Đáp:** có `<start>` + `<commit>` → **REDO** (áp new, Durability). Có `<start>` nhưng **không** commit → **UNDO** (trả old, Atomicity). Redo quét xuôi, undo quét ngược.

> [!question] Thẻ 11.5 — Checkpoint và ARIES để làm gì?
> **Đáp:** **checkpoint** = mốc flush đĩa + ghi `<checkpoint L>`, giúp phục hồi chỉ quét *từ checkpoint gần nhất*. **ARIES** = thuật toán phục hồi thực tế, dùng **LSN** + ba pha Analysis/Redo/Undo để tránh redo thừa.

## 8. Câu hỏi tự kiểm tra

1. Cho ví dụ chuyển tiền bị sập, chỉ ra kịch bản mất Atomicity và kịch bản mất Durability. *(mục 1)*
2. Phát biểu luật WAL. Nếu sửa dữ liệu *trước* rồi ghi log *sau*, phục hồi hỏng thế nào? *(mục 2)*
3. Redo và undo khác nhau ra sao (giá trị nào được áp)? Luật nào quyết định làm cái nào? *(mục 3)*
4. Checkpoint giảm chi phí phục hồi bằng cách nào? ARIES thêm gì so với sơ đồ cơ bản? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 4 (bỏ old). Vì sao thiếu old thì không undo được? *(mục 5)*

## Tóm tắt một trang

```
BÀI 11 — PHỤC HỒI: WAL / ARIES
─────────────────────────────────────────────────────────
VẤN ĐỀ  SẬP giữa chừng: buffer (RAM) bay hơi, ghi đĩa KHÔNG đồng bộ với commit →
   committed chưa xuống đĩa (mất Durability); chưa-commit đã xuống đĩa (mất Atomicity).

LOG + WAL  log = chuỗi bản ghi mọi thay đổi (tr.913). Update record <Ti,Xj,old,new>
   + <start>/<commit>/<abort>. LUẬT WAL: ghi log TRƯỚC khi sửa dữ liệu (tr.913) →
   log luôn đủ thông tin dù đĩa dở dang.

REDO / UNDO  redo(Ti) = áp giá trị MỚI (tr.918); undo(Ti) = trả giá trị CŨ (tr.918).
   Luật: có start + commit → REDO (Durability); có start, KHÔNG commit → UNDO
   (Atomicity) (tr.919). Redo quét XUÔI, undo quét NGƯỢC.

CHECKPOINT (tr.921)  <checkpoint L> + flush → phục hồi chỉ quét từ checkpoint gần nhất.
ARIES (tr.941)  thuật toán thực tế: LSN + 3 pha Analysis/Redo/Undo, tránh redo thừa.

DEMO  trước sập: A=1000 (T1 commit chưa ghi), C=9999 (T2 chưa commit đã ghi bẩn).
   phục hồi: REDO T1→A=1500, UNDO T2→C=1000. Nhờ log có old+new, ghi trước.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch19 Recovery System**: log (tr. 913), luật write-ahead logging (tr. 913), redo & undo (tr. 918), luật undo-nếu-chưa-commit (tr. 919), checkpoint (tr. 921), ARIES (tr. 941). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [Bài 9 — atomicity & durability](bai_09_transaction-acid.md), [Bài 4 — dirty page & buffer flush](bai_04_luu-tru-buffer.md), [Bài 6 — WAL cũng là nền của LSM](bai_06_index-lsm-bitmap.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Xử lý truy vấn: join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn (cost-based)](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID, isolation](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · **[Bài 11 — Phục hồi: WAL/ARIES] ← bạn đang ở đây** · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
