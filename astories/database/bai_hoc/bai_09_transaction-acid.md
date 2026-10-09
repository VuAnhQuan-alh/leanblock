# Bài 9 — Transaction và ACID, isolation levels

> [!info] Về bài này
> Hết phần *hiệu năng* (Bài 4–8). Giờ là **tính đúng đắn**: database phải giữ dữ liệu *nhất quán* ngay cả khi có lỗi (máy sập giữa chừng) và khi *nhiều người cùng ghi*. Đơn vị bảo đảm điều đó là **giao dịch (transaction)** với bốn lời hứa **ACID**. Bài này mổ ACID, chỉ ra vì sao chạy song song có thể *phá* nhất quán (serializability), và các **mức cô lập (isolation levels)** đánh đổi đúng-đắn lấy tốc độ.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch17 (Transactions)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node --experimental-sqlite <tên>.ts` (phần ACID dùng `node:sqlite`; cảnh báo stderr vô hại).
> Nên đọc trước: [Bài 0 — bệnh đồng thời & nguyên tử](bai_00_dbms-la-gi.md). Liên hệ: [cloud-base Bài 16 — transaction & saga](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md).

## Mục lục

1. [Giao dịch là đơn vị trọn vẹn](#1-giao-dịch-là-đơn-vị-trọn-vẹn)
2. [ACID: bốn lời hứa](#2-acid-bốn-lời-hứa)
3. [Chạy song song và serializability](#3-chạy-song-song-và-serializability)
4. [Các mức cô lập và anomaly](#4-các-mức-cô-lập-và-anomaly)
5. [Demo: lost update và atomicity](#5-demo-lost-update-và-atomicity)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Giao dịch là đơn vị trọn vẹn

Nhớ "bệnh 5" ở Bài 0: chuyển \$500, máy sập sau khi trừ A mà chưa cộng B → tiền bốc hơi. Gốc rễ: chuyển tiền là **nhiều thao tác** nhưng phải xảy ra như **một**. Đơn vị đó là **giao dịch**: một chuỗi thao tác được xem là *một khối không thể chia*. Một giao dịch kết thúc bằng **commit** (xác nhận, mọi thay đổi thành sự thật) hoặc **rollback/abort** (huỷ, như chưa từng xảy ra).

Giao dịch cô đặc hai bài toán sống còn của database:
- **Phục hồi khi lỗi**: máy sập giữa giao dịch → khi khởi động lại phải *như giao dịch chưa từng chạy* (Bài 11).
- **Chạy song song an toàn**: nhiều giao dịch đan xen → kết quả phải *như thể chúng chạy lần lượt* (Bài 10).

Bốn lời hứa của một giao dịch — **ACID** — chính là lời giải hình thức cho hai bài toán này.

## 2. ACID: bốn lời hứa

> [!quote] Silberschatz (tr. 800)
> "Atomicity. Either all operations of the transaction are reflected properly in the database, or none are."
>
> ***Atomicity** (nguyên tử). **Hoặc toàn bộ** thao tác của giao dịch được phản ánh đúng vào CSDL, **hoặc không gì cả**.*

- **A — Atomicity (nguyên tử)**: tất-cả-hoặc-không. Sập giữa chừng → rollback về trạng thái trước đó.
- **C — Consistency (nhất quán)**: giao dịch đưa CSDL từ một trạng thái *hợp lệ* sang trạng thái *hợp lệ* khác (giữ mọi ràng buộc: khoá ngoại, `CHECK`, invariant (bất biến) như "tổng tiền không đổi").

> [!quote] Silberschatz (tr. 800)
> "Isolation. Even though multiple transactions may execute concurrently, the system guarantees that, for every pair of transactions Ti and Tj, it appears to Ti that either Tj finished execution before Ti started or Tj started execution after Ti finished."
>
> ***Isolation** (cô lập). Dù nhiều giao dịch chạy song song, hệ bảo đảm với **mỗi cặp** Ti, Tj rằng với Ti **mọi thứ trông như** Tj đã **xong trước khi** Ti bắt đầu, **hoặc** Tj **bắt đầu sau khi** Ti xong.*

- **I — Isolation (cô lập)**: mỗi giao dịch chạy *như thể* không có ai khác — dù thực tế đan xen (mục 3).

> [!quote] Silberschatz (tr. 801)
> "Durability. After a transaction completes successfully, the changes it has made to the database persist, even if there are system failures."
>
> ***Durability** (bền vững). Sau khi giao dịch **commit thành công**, thay đổi của nó **tồn tại bền**, kể cả khi hệ **gặp sự cố**.*

- **D — Durability (bền vững)**: đã commit là *không mất*, dù mất điện ngay sau đó (Bài 11 — WAL).

> [!quote] Silberschatz (tr. 801)
> "These properties are often called the ACID properties; the acronym is derived from the first letter of each of the four properties."

ACID là *hợp đồng* giữa database và lập trình viên: bạn gói logic vào giao dịch, database lo phần "trọn vẹn + cô lập + bền". Hai chữ khó nhất về mặt cơ chế là **I** (Bài 10) và **A/D** (Bài 11).

## 3. Chạy song song và serializability

Chạy từng giao dịch *lần lượt* (serial) thì luôn đúng — nhưng chậm khủng khiếp (một giao dịch dài chặn mọi người). Nên hệ cho chúng **đan xen**. Hiểm hoạ: đan xen sai làm hỏng nhất quán. Ví dụ hai giao dịch cùng cộng vào một số dư, cả hai *đọc* giá trị cũ trước khi bên nào kịp *ghi* → một cập nhật bị đè mất (**lost update**).

Tiêu chuẩn vàng để biết một lịch đan xen có *an toàn* không:

> [!quote] Silberschatz (tr. 812)
> "We can ensure consistency of the database under concurrent execution by making sure that any schedule that is executed has the same effect as a schedule that could have occurred without any concurrent execution. [...] Such schedules are called serializable schedules."
>
> *Ta bảo đảm nhất quán khi chạy song song bằng cách chắc chắn rằng **mọi lịch được chạy có cùng hiệu quả với một lịch không hề song song**. [...] Những lịch như vậy gọi là **serializable** (khả tuần-tự-hoá).*

Nói gọn: một lịch đan xen *đúng* khi kết quả của nó **y hệt** như thể các giao dịch chạy lần lượt theo *một thứ tự nào đó*. "Serializable" = "tương đương một lịch tuần tự". Đây chính là ý nghĩa chặt chẽ của chữ **I** trong ACID. Bộ phận **concurrency control** (điều khiển đồng thời; Bài 10 — khoá, MVCC) có nhiệm vụ *chỉ cho phép* các lịch serializable. Demo mục 5 cho thấy lịch đan xen *không* serializable phá nhất quán ra sao.

## 4. Các mức cô lập và anomaly

Bảo đảm serializable *đầy đủ* thì đắt (phải khoá nhiều, giảm song song). Nên SQL cho phép giao dịch **hạ mức cô lập** để đổi lấy tốc độ — chấp nhận một số bất thường (anomaly). Bốn mức chuẩn:

> [!quote] Silberschatz (tr. 821)
> "The isolation levels specified by the SQL standard are as follows: • Serializable usually ensures serializable execution. [...] • Repeatable read allows only committed data to be read and further requires that, between two reads of a data item by a transaction, no other transaction is allowed to update it. [...] • Read committed allows only committed data to be read, but does not require repeatable reads. [...] • Read uncommitted allows uncommitted data to be read. It is the lowest isolation level allowed by SQL."

Ba anomaly kinh điển và mức cô lập chặn chúng:

- **Dirty read**: đọc dữ liệu một giao dịch khác *chưa commit* (có thể bị rollback → đọc phải "ma").
- **Non-repeatable read**: đọc cùng một dòng hai lần trong một giao dịch, ra *hai giá trị khác nhau* (ai đó sửa & commit ở giữa).
- **Phantom**: chạy cùng một truy vấn *có điều kiện* hai lần, lần sau xuất hiện *dòng mới* (ai đó chèn & commit ở giữa).

| Mức cô lập | Dirty read | Non-repeatable read | Phantom |
| :-- | :--: | :--: | :--: |
| Read uncommitted | có thể | có thể | có thể |
| Read committed | không | có thể | có thể |
| Repeatable read | không | không | có thể |
| Serializable | không | không | không |

Càng lên cao càng đúng nhưng càng chậm. Thực tế:

> [!quote] Silberschatz (tr. 822)
> "Many database systems run, by default, at the read-committed isolation level."
>
> *Nhiều hệ chạy **mặc định ở mức read-committed**.*

Nghĩa là *mặc định không serializable* — lập trình viên phải *chủ động* nâng mức (hoặc dùng khoá tường minh) cho những chỗ cần đúng tuyệt đối, như chuyển tiền. (SQLite thì mặc định đã serializable nhờ khoá toàn CSDL — đổi lấy việc chỉ một người ghi tại một thời điểm.)

## 5. Demo: lost update và atomicity

Phần A mô phỏng tận bước một lịch đan xen gây **lost update** (so với tuần tự đúng) — minh hoạ vì sao cần Isolation. Phần B dùng SQLite thật cho **Atomicity + Consistency**: giao dịch hợp lệ commit, giao dịch vi phạm ràng buộc bị rollback trọn vẹn:

```typescript
import { strict as assert } from "node:assert";
import { DatabaseSync } from "node:sqlite";

// ─── PHẦN A: vì sao cần ISOLATION — lịch chạy đan xen phá nhất quán ───
// Hai giao dịch cùng cộng vào một số dư (read-modify-write). Chạy TUẦN TỰ thì đúng;
// đan xen "ngây thơ" thì MẤT một cập nhật (lost update) — không tương đương lịch tuần tự.
console.log("PHẦN A — serial vs đan xen (số dư đầu = 1000; T1 +100, T2 +200):");

// Lịch TUẦN TỰ: T1 xong hẳn rồi T2.
let s = 1000;
{ const r = s; s = r + 100; }   // T1: đọc 1000 → ghi 1100
{ const r = s; s = r + 200; }   // T2: đọc 1100 → ghi 1300
console.log(`  serial (T1;T2)      : ${s}  (đúng: 1000+100+200)`);
const serial = s;

// Lịch ĐAN XEN: cả hai ĐỌC trước khi bên nào kịp GHI → ghi đè nhau.
let x = 1000;
const t1read = x;               // T1 đọc 1000
const t2read = x;               // T2 đọc 1000 (trước khi T1 ghi)
x = t1read + 100;               // T1 ghi 1100
x = t2read + 200;               // T2 ghi 1200  ← đè mất +100 của T1
console.log(`  đan xen (lost update): ${x}  (SAI: mất +100 của T1)`);
assert.equal(serial, 1300); assert.equal(x, 1200);
console.log("  → Isolation = bảo đảm kết quả TƯƠNG ĐƯƠNG một lịch tuần tự nào đó (serializable).");

// ─── PHẦN B: ACID atomicity + consistency thật (node:sqlite) ───
// A (atomicity): giao dịch xảy ra TRỌN VẸN hoặc KHÔNG; C (consistency): ràng buộc
// luôn giữ (CHECK balance>=0). Chuyển hợp lệ → commit; rút quá tay → CHECK chặn → rollback.
const db = new DatabaseSync(":memory:");
db.exec(`CREATE TABLE account(name TEXT PRIMARY KEY, balance INT CHECK(balance >= 0));
         INSERT INTO account VALUES ('A',1000),('B',0);`);
const total = () => (db.prepare(`SELECT SUM(balance) s FROM account`).get() as any).s;
function transfer(from: string, to: string, amt: number): string {
  try {
    db.exec("BEGIN");
    db.prepare(`UPDATE account SET balance=balance-? WHERE name=?`).run(amt, from);
    db.prepare(`UPDATE account SET balance=balance+? WHERE name=?`).run(amt, to);
    db.exec("COMMIT"); return "COMMIT";
  } catch (e) { db.exec("ROLLBACK"); return "ROLLBACK (" + (e as Error).message.split(":")[0] + ")"; }
}
console.log("\nPHẦN B — ACID atomicity + consistency (A=1000, B=0, invariant A+B=1000):");
console.log(`  chuyển 300 A→B : ${transfer("A", "B", 300)}  → A+B = ${total()}`);
console.log(`  chuyển 2000 A→B: ${transfer("A", "B", 2000)}  → A+B = ${total()}`);
console.log("  → lần 2 vi phạm CHECK(balance>=0): CẢ giao dịch bị ROLLBACK (atomicity), invariant giữ nguyên.");
assert.equal(total(), 1000);   // invariant không đổi dù một giao dịch thất bại
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — serial vs đan xen (số dư đầu = 1000; T1 +100, T2 +200):
  serial (T1;T2)      : 1300  (đúng: 1000+100+200)
  đan xen (lost update): 1200  (SAI: mất +100 của T1)
  → Isolation = bảo đảm kết quả TƯƠNG ĐƯƠNG một lịch tuần tự nào đó (serializable).

PHẦN B — ACID atomicity + consistency (A=1000, B=0, invariant A+B=1000):
  chuyển 300 A→B : COMMIT  → A+B = 1000
  chuyển 2000 A→B: ROLLBACK (CHECK constraint failed)  → A+B = 1000
  → lần 2 vi phạm CHECK(balance>=0): CẢ giao dịch bị ROLLBACK (atomicity), invariant giữ nguyên.
```

Bốn điều đáng thấm. **(1)** Cùng hai thao tác `+100` và `+200`, chạy **tuần tự** ra `1300` (đúng), **đan xen** ra `1200` — mất đúng `+100` của T1 vì T2 ghi đè dựa trên giá trị đã đọc cũ. Đây là **lost update**, một lịch *không* serializable. **(2)** Isolation nghĩa là hệ *cấm* những đan xen như vậy — kết quả phải *tương đương* một thứ tự tuần tự nào đó (tr. 812). **(3)** Phần B: chuyển 300 hợp lệ → `COMMIT`, tổng vẫn 1000. **(4)** Chuyển 2000 làm A âm → vi phạm `CHECK` → **cả** giao dịch `ROLLBACK` (không phải chỉ bước lỗi): A *không* bị trừ, B *không* được cộng, invariant `A+B=1000` nguyên vẹn. Đó là **Atomicity** (trọn vẹn-hoặc-không) phục vụ **Consistency** (giữ ràng buộc).

> [!note] Tự thử
> 1. Phần A: viết lịch đan xen *khác* vẫn cho kết quả đúng 1300 (gợi ý: T1 ghi xong rồi T2 mới đọc). Vì sao lịch đó *serializable* còn lịch kia thì không?
> 2. Phần B: bỏ `db.exec("BEGIN")` và `COMMIT` (tắt giao dịch), chạy lại chuyển 2000. Bước `UPDATE A` có bị rollback không? Vì sao thiếu giao dịch thì mất atomicity?
> 3. Thêm một `transfer("A","B",700)` sau hai lần hiện có: còn đủ tiền không? `CHECK` phản ứng ra sao?
> 4. Tra mức cô lập mặc định của PostgreSQL vs MySQL (InnoDB). Dựa vào bảng mục 4, mỗi mặc định cho phép anomaly nào? *(mục 4)*

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
| 9 | **Transaction & ACID, isolation** ← *đang ở đây* | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Bài 9 mở chương *tính đúng đắn*: Bài 10 lo chữ **I** (cô lập khi song song), Bài 11 lo chữ **A** và **D** (nguyên tử & bền khi sập).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 9.1 — Giao dịch là gì? Kết thúc bằng gì?
> **Đáp:** một chuỗi thao tác được xem là **một khối không chia**; kết thúc bằng **commit** (mọi thay đổi thành sự thật) hoặc **rollback** (huỷ, như chưa chạy).

> [!question] Thẻ 9.2 — ACID là gì?
> **Đáp:** **A**tomicity (trọn vẹn-hoặc-không), **C**onsistency (giữ ràng buộc/invariant), **I**solation (như chạy một mình), **D**urability (commit rồi không mất dù sập).

> [!question] Thẻ 9.3 — "Serializable schedule" nghĩa là gì?
> **Đáp:** một lịch đan xen có **cùng hiệu quả** như một lịch chạy các giao dịch **lần lượt** theo thứ tự nào đó. Đó là ý nghĩa chặt của Isolation.

> [!question] Thẻ 9.4 — Dirty read, non-repeatable read, phantom khác nhau ra sao?
> **Đáp:** dirty = đọc dữ liệu **chưa commit**; non-repeatable = đọc **cùng dòng** hai lần ra khác nhau; phantom = truy vấn có điều kiện hai lần, lần sau có **dòng mới** chèn vào.

> [!question] Thẻ 9.5 — Bốn mức cô lập, cái nào mặc định phổ biến?
> **Đáp:** Read uncommitted < Read committed < Repeatable read < Serializable (càng cao càng đúng, càng chậm). **Nhiều hệ mặc định read-committed** — tức *không* serializable sẵn.

## 8. Câu hỏi tự kiểm tra

1. Vì sao "chuyển tiền" phải là một giao dịch chứ không phải hai câu UPDATE rời? *(mục 1)*
2. Giải thích từng chữ trong ACID. Chữ nào lo "sập giữa chừng", chữ nào lo "nhiều người cùng ghi"? *(mục 2)*
3. Một lịch đan xen thế nào thì gọi là serializable? Cho ví dụ một lịch *không* serializable. *(mục 3, 5)*
4. Kẻ bảng anomaly × isolation level. Vì sao "mặc định read-committed" lại là một *đánh đổi*? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 2 (tắt giao dịch). Vì sao thiếu `BEGIN/COMMIT` thì mất atomicity? *(mục 5)*

## Tóm tắt một trang

```
BÀI 9 — TRANSACTION & ACID, ISOLATION
─────────────────────────────────────────────────────────
GIAO DỊCH  chuỗi thao tác = MỘT khối không chia; kết: COMMIT hoặc ROLLBACK. Gói
   lại 2 bài toán: phục hồi khi SẬP (Bài 11) + chạy SONG SONG an toàn (Bài 10).

ACID  A tomicity = trọn-vẹn-hoặc-không (tr.800); C onsistency = giữ ràng buộc;
   I solation = như chạy một mình dù đan xen (tr.800); D urability = commit rồi
   không mất dù sập (tr.801). "Thường gọi là ACID properties" (tr.801).

SERIALIZABILITY  lịch đan xen ĐÚNG ⟺ cùng hiệu quả một lịch TUẦN TỰ nào đó
   (serializable, tr.812). Đan xen sai → LOST UPDATE (ghi đè). Concurrency control
   (Bài 10) chỉ cho phép lịch serializable.

ISOLATION LEVELS (tr.821)  Read uncommitted < Read committed < Repeatable read <
   Serializable. Anomaly: dirty read / non-repeatable read / phantom (bảng mục 4).
   Hạ mức = nhanh hơn, chấp nhận anomaly. Nhiều hệ MẶC ĐỊNH read-committed (tr.822).

DEMO  serial 1300 vs đan xen 1200 (lost update). CHECK vi phạm → CẢ giao dịch
   ROLLBACK, invariant A+B=1000 giữ nguyên (atomicity phục vụ consistency).
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch17 Transactions**: atomicity & isolation (tr. 800), durability & ACID (tr. 801), serializable schedule (tr. 812), isolation levels SQL (tr. 821), mặc định read-committed (tr. 822). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 16 — transaction & saga](../../cloud-base/bai_hoc/bai_16_dist-transaction-saga.md) (ACID vs BASE, 2PC, saga ở góc phân tán); [Bài 10 — cô lập](bai_10_concurrency.md), [Bài 11 — nguyên tử & bền](bai_11_recovery.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Xử lý truy vấn: join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn (cost-based)](bai_08_query-optimization.md) · **[Bài 9 — Transaction & ACID, isolation] ← bạn đang ở đây** · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
