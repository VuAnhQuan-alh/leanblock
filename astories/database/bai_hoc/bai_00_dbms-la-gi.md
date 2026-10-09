# Bài 0 — DBMS là gì, và vì sao cần nó

> [!info] Về khoá này
> Khoá **`database`** đào sâu **ruột một database engine**: không chỉ *dùng* SQL mà hiểu *bên trong* nó lưu, đánh chỉ mục, chạy truy vấn, giữ nhất quán và phục hồi ra sao. Đi dần từ nền quan hệ → SQL → thiết kế → **lưu trữ → index → xử lý truy vấn → transaction → đồng thời → phục hồi** → phân tán. Tự chứa (không bắt buộc đọc khoá khác trước), nhưng có liên hệ sang mạch cloud khi hữu ích.
> Nguồn (Luật số 1): **Silberschatz** — *Database System Concepts, 7th ed.* (PDF `tai_lieu/`, trích `> [!quote] Silberschatz (tr. N)`, **PDF = tr. + 29**) + **Red Book** — *Readings in Database Systems, 5th ed.* (Bailis–Hellerstein–Stonebraker, PDF `tai_lieu/`, trích `> [!quote] Red Book`).
> **Chạy demo:** cần **Node 22+** (chạy thẳng `.ts`). Phần SQL dùng module tích hợp sẵn `node:sqlite` — **không cài gói gì**. Lưu file rồi gõ `node --experimental-sqlite <tên>.ts` (dòng cảnh báo *ExperimentalWarning* in ra **stderr** là bình thường, không ảnh hưởng kết quả).
> Liên hệ: mạch cloud ([`cloud-base`](../../cloud-base/README.md)) nhìn dữ liệu từ góc *ứng dụng quy mô lớn* (DDIA); khoá này nhìn từ góc *bên trong engine* (Silberschatz).

## Mục lục

1. [Tình huống: dữ liệu đại học trong file phẳng](#1-tình-huống-dữ-liệu-đại-học-trong-file-phẳng)
2. [Sáu cái bẫy của thế giới file phẳng](#2-sáu-cái-bẫy-của-thế-giới-file-phẳng)
3. [DBMS là gì: trừu tượng hoá dữ liệu](#3-dbms-là-gì-trừu-tượng-hoá-dữ-liệu)
4. [Demo: ba cái bẫy đó bằng SQL thật](#4-demo-ba-cái-bẫy-đó-bằng-sql-thật)
5. [Bản đồ khoá database](#5-bản-đồ-khoá-database)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Tình huống: dữ liệu đại học trong file phẳng

> [!example] Trường đại học, trước khi có DBMS
> Một trường cần lưu thông tin giảng viên, sinh viên, khoa, môn học. Cách "hiển nhiên" nhất: cất vào **file của hệ điều hành**, rồi viết các **chương trình ứng dụng** để thêm/sửa/tra. Cần mở ngành mới? Thêm vài file, viết thêm vài chương trình. Qua năm tháng, hệ thống **phình ra** thành một mớ file và chương trình chắp vá — mỗi lập trình viên một kiểu, mỗi file một định dạng.

Nghe thì ổn, và thực tế suốt thập niên 1960 người ta làm đúng vậy. Nhưng cách tiếp cận "file phẳng + chương trình" giấu trong nó hàng loạt vấn đề mà càng dùng lâu càng lộ. Chính những vấn đề này **đẻ ra** cả ngành database.

> [!quote] Silberschatz (tr. 1)
> "A database-management system (DBMS) is a collection of interrelated data and a set of programs to access those data. [...] The primary goal of a DBMS is to provide a way to store and retrieve database information that is both convenient and efficient."
>
> *Một **hệ quản trị cơ sở dữ liệu (DBMS)** là tập hợp dữ liệu liên quan nhau cùng bộ chương trình để truy cập chúng. [...] Mục tiêu chính của DBMS là cung cấp cách lưu và truy xuất thông tin vừa **tiện lợi** vừa **hiệu quả**.*

## 2. Sáu cái bẫy của thế giới file phẳng

Sách liệt kê những nhược điểm lớn của "file-processing system". Đây chính là mạch *ngây thơ → sai* — mỗi bẫy là một lý do DBMS tồn tại:

1. **Dư thừa & không nhất quán** *(data redundancy and inconsistency)*. Cùng một thông tin bị chép ở nhiều file. Sinh viên học hai ngành → địa chỉ nằm trong cả file khoa Nhạc lẫn khoa Toán. Sửa một nơi, quên nơi kia → hai bản **mâu thuẫn**.
2. **Khó truy cập dữ liệu** *(difficulty in accessing data)*. Cần "danh sách SV trong một mã bưu chính" nhưng chưa ai viết chương trình cho đúng câu hỏi đó → phải nhờ lập trình viên viết mới. Mỗi câu hỏi mới = một chương trình mới.
3. **Cô lập dữ liệu** *(data isolation)*. Dữ liệu rải rác nhiều file, nhiều định dạng → viết chương trình gộp chúng lại rất khó.
4. **Vấn đề toàn vẹn** *(integrity problems)*. Ràng buộc (vd "số dư khoa không được âm") bị nhét rải rác trong code ứng dụng; thêm ràng buộc mới phải sửa khắp nơi.
5. **Vấn đề nguyên tử** *(atomicity problems)*. Chuyển \$500 từ A sang B: nếu máy sập **giữa chừng**, tiền đã trừ của A nhưng chưa cộng cho B → dữ liệu sai.

> [!quote] Silberschatz (tr. 7)
> "the funds transfer must be atomic—it must happen in its entirety or not at all. It is difficult to ensure atomicity in a conventional file-processing system."
>
> *chuyển tiền phải **nguyên tử** — xảy ra **trọn vẹn hoặc không gì cả**. Rất khó đảm bảo tính nguyên tử trong hệ file phẳng thông thường.*

6. **Bất thường khi truy cập đồng thời** *(concurrent-access anomalies)* và **vấn đề bảo mật** *(security problems)*. Hai người cùng ghi danh một lúc, cùng đọc sĩ số 39, cùng ghi 40 → lẽ ra 41 mà thành 40 (**mất một lần cập nhật**). Và: không phải ai cũng được xem mọi dữ liệu, nhưng phân quyền trên mớ file chắp vá là ác mộng.

Ba cái bẫy số **1, 5, 6** là cụ thể và đau nhất — mục 4 sẽ **tái hiện cả ba bằng SQL chạy thật**, rồi cho thấy DBMS chữa ra sao.

## 3. DBMS là gì: trừu tượng hoá dữ liệu

DBMS giải quyết đống trên bằng **một ý tưởng cốt lõi**: trừu tượng hoá.

> [!quote] Silberschatz (tr. 2)
> "Key to the management of complexity is the concept of abstraction. Abstraction allows a person to use a complex device or system without having to know the details of how that device or system is constructed."
>
> *Chìa khoá để quản lý sự phức tạp là **trừu tượng hoá**. Nó cho phép dùng một hệ phức tạp mà **không cần biết nó được dựng ra sao**.*

> [!example] Ẩn dụ: lái xe mà không cần biết động cơ
> Bạn lái được xe chỉ nhờ biết vô-lăng, ga, phanh — **không** cần biết động cơ đốt trong hoạt động thế nào. DBMS làm đúng vậy với dữ liệu: cho bạn một *khung nhìn đơn giản* (bảng, câu lệnh SQL), giấu đi chuyện dưới đất là B-tree, trang đĩa, khoá, log... Cả khoá này là hành trình **mở nắp ca-pô** xem động cơ đó chạy ra sao.

DBMS chia sự phức tạp thành **ba mức trừu tượng** (tr. 9–11):

```
   MỨC KHUNG NHÌN (view)      nhiều khung nhìn — mỗi người dùng chỉ thấy phần của mình
         ↑                     (vd: nhân viên phòng đào tạo không thấy lương giảng viên)
   MỨC LOGIC (logical)        CÓ dữ liệu gì & quan hệ giữa chúng — bảng, cột, ràng buộc
         ↑                     (lập trình viên & DBA làm việc ở đây)
   MỨC VẬT LÝ (physical)      dữ liệu THỰC SỰ được lưu thế nào — cấu trúc dữ liệu, index, byte
```

Hai khái niệm nền đi kèm:

- **Mô hình dữ liệu** *(data model)* — bộ công cụ mô tả dữ liệu & quan hệ. Phổ biến nhất là **mô hình quan hệ** (bảng/relation); còn có E-R, bán cấu trúc (JSON/XML), hướng đối tượng. *"The relational data model is the most widely used data model"* (tr. 9) — và là trục của khoá này (Bài 1).
- **Instance vs schema**. **Schema** = thiết kế tổng thể (cấu trúc các bảng), đổi hiếm. **Instance** = dữ liệu *tại một thời điểm*, đổi liên tục khi thêm/xoá. Analogy: schema như *khai báo kiểu* trong ngôn ngữ lập trình, instance như *giá trị* của biến lúc chạy.

## 4. Demo: ba cái bẫy đó bằng SQL thật

Ta tái hiện **bệnh 1 (dư thừa), bệnh 5 (nguyên tử), bệnh 6 (đồng thời)** trên SQLite thật qua `node:sqlite`, và cho thấy **transaction** của DBMS chữa bệnh nguyên tử:

```typescript
import { DatabaseSync } from "node:sqlite";
import { strict as assert } from "node:assert";

const db = new DatabaseSync(":memory:");

// ─── Bệnh 1: DƯ THỪA & KHÔNG NHẤT QUÁN (redundancy & inconsistency) ───
// Thế giới "file phẳng": sinh viên học 2 ngành → địa chỉ bị chép ở 2 "file".
db.exec(`CREATE TABLE music_file(id INT, name TEXT, address TEXT);
         CREATE TABLE math_file (id INT, name TEXT, address TEXT);`);
db.exec(`INSERT INTO music_file VALUES (1,'An','Ha Noi');
         INSERT INTO math_file  VALUES (1,'An','Ha Noi');`);
// An chuyển nhà → chương trình chỉ cập nhật file Nhạc, quên file Toán:
db.exec(`UPDATE music_file SET address='Da Nang' WHERE id=1`);
const a1 = (db.prepare(`SELECT address FROM music_file WHERE id=1`).get() as any).address;
const a2 = (db.prepare(`SELECT address FROM math_file  WHERE id=1`).get() as any).address;
console.log("BỆNH 1 — dư thừa & không nhất quán:");
console.log(`  cùng 1 người, 2 file: Nhạc='${a1}'  Toán='${a2}'  → lệch: ${a1 !== a2}`);

// ─── Bệnh 5: NGUYÊN TỬ (atomicity) — chuyển 500 từ A sang B, "sập" giữa chừng ─
function setupBank() {
  db.exec(`DROP TABLE IF EXISTS account;
           CREATE TABLE account(name TEXT PRIMARY KEY, balance INT);
           INSERT INTO account VALUES ('A',10000),('B',0);`);
}
const total = () => (db.prepare(`SELECT SUM(balance) s FROM account`).get() as any).s;

console.log("\nBỆNH 5 — nguyên tử (chuyển 500 từ A→B, lỗi sau khi trừ A):");
setupBank();
// (a) KHÔNG giao dịch: trừ A xong thì "sập" trước khi cộng B.
db.exec(`UPDATE account SET balance=balance-500 WHERE name='A'`);
// ...sự cố ở đây... (bỏ qua bước cộng B)
console.log(`  (a) không transaction: tổng tiền = ${total()}  (mất 500! đáng lẽ 10000)`);

// (b) CÓ giao dịch: bọc trong BEGIN…COMMIT, lỗi → ROLLBACK.
setupBank();
try {
  db.exec("BEGIN");
  db.exec(`UPDATE account SET balance=balance-500 WHERE name='A'`);
  throw new Error("sập giữa chừng");          // mô phỏng sự cố
  db.exec(`UPDATE account SET balance=balance+500 WHERE name='B'`); // không tới được
  db.exec("COMMIT");
} catch {
  db.exec("ROLLBACK");
}
console.log(`  (b) có transaction:    tổng tiền = ${total()}  (nguyên vẹn nhờ ROLLBACK)`);
assert.equal(total(), 10000);

// ─── Bệnh 6: BẤT THƯỜNG KHI TRUY CẬP ĐỒNG THỜI (lost update) ───
// Sĩ số = 39, giới hạn 40. Hai phiên ghi danh cùng lúc, đan xen read-modify-write.
db.exec(`CREATE TABLE course(id INT PRIMARY KEY, cnt INT);
         INSERT INTO course VALUES (1,39);`);
const readCnt  = () => (db.prepare(`SELECT cnt FROM course WHERE id=1`).get() as any).cnt;
const writeCnt = (v: number) => db.prepare(`UPDATE course SET cnt=? WHERE id=1`).run(v);
const s1 = readCnt();   // phiên 1 đọc 39
const s2 = readCnt();   // phiên 2 đọc 39 (trước khi phiên 1 kịp ghi)
writeCnt(s1 + 1);       // phiên 1 ghi 40
writeCnt(s2 + 1);       // phiên 2 ghi 40 (đè lên, mất 1 lần ghi danh)
console.log("\nBỆNH 6 — bất thường đồng thời (lost update):");
console.log(`  2 SV ghi danh, sĩ số cuối = ${readCnt()}  (đáng lẽ 41 — mất 1!)`);

console.log("\nDBMS sinh ra để chữa đúng các bệnh này: 1 nguồn dữ liệu (hết dư thừa),");
console.log("transaction (nguyên tử + cô lập), ràng buộc & phân quyền — thay cho file phẳng.");
```

Kết quả chạy thật *(tất định)*:

```
BỆNH 1 — dư thừa & không nhất quán:
  cùng 1 người, 2 file: Nhạc='Da Nang'  Toán='Ha Noi'  → lệch: true

BỆNH 5 — nguyên tử (chuyển 500 từ A→B, lỗi sau khi trừ A):
  (a) không transaction: tổng tiền = 9500  (mất 500! đáng lẽ 10000)
  (b) có transaction:    tổng tiền = 10000  (nguyên vẹn nhờ ROLLBACK)

BỆNH 6 — bất thường đồng thời (lost update):
  2 SV ghi danh, sĩ số cuối = 40  (đáng lẽ 41 — mất 1!)

DBMS sinh ra để chữa đúng các bệnh này: 1 nguồn dữ liệu (hết dư thừa),
transaction (nguyên tử + cô lập), ràng buộc & phân quyền — thay cho file phẳng.
```

Ba điều đáng thấm. **(1) Dư thừa đẻ ra mâu thuẫn:** cùng một người mà hai "file" cho hai địa chỉ — DBMS chữa bằng *một* nguồn sự thật (chuẩn hoá, Bài 3). **(2) Transaction là thuốc cho nguyên tử:** không bọc giao dịch thì sự cố giữa chừng làm *bốc hơi* 500; bọc `BEGIN…COMMIT` + `ROLLBACK` thì tổng tiền nguyên vẹn — chữ **A** trong ACID (Bài 9–11 mổ sâu). **(3) Đồng thời không kiểm soát = mất cập nhật:** hai phiên đọc-sửa-ghi đan xen làm mất một lần ghi danh — đây là lý do có **điều khiển đồng thời** (khoá, MVCC — Bài 10).

> [!note] Tự thử
> 1. Ở bệnh 6, nếu hai phiên chạy **tuần tự** (phiên 1 đọc→ghi xong, phiên 2 mới đọc) thì sĩ số cuối là bao nhiêu? Vì sao "đan xen" mới sinh lỗi?
> 2. Thêm `UNIQUE` hay `CHECK (balance >= 0)` vào bảng `account` rồi thử rút quá số dư — DBMS phản ứng sao? (đây là *bệnh 4 — toàn vẹn* được chữa.)
> 3. Bỏ dòng `throw` ở nhánh (b): giờ `COMMIT` chạy, tổng tiền vẫn 10000 nhưng số dư A/B đổi. In `SELECT * FROM account` để kiểm.
> 4. Đổi `:memory:` thành tên file `"truong.db"`: chạy hai lần, dữ liệu còn đó — đây là **lưu bền** (persistence), khác hẳn biến trong RAM.

## 5. Bản đồ khoá database

Mỗi bài mở một mảng của engine, xây dần từ nền quan hệ xuống ruột:

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | **DBMS là gì & vì sao cần** ← *đang ở đây* | động lực, trừu tượng hoá | Silberschatz Ch1 |
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
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Trọng tâm *"ruột engine"* là Bài 4–11. Bài 0–3 dựng nền quan hệ/SQL/thiết kế vừa đủ để tự chứa.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 0.1 — DBMS là gì?
> **Đáp:** tập hợp dữ liệu liên quan nhau + bộ chương trình truy cập chúng; mục tiêu: lưu & truy xuất **tiện lợi và hiệu quả** (Silberschatz tr. 1).

> [!question] Thẻ 0.2 — Kể vài "bệnh" của hệ file phẳng mà DBMS sinh ra để chữa.
> **Đáp:** dư thừa & không nhất quán, khó truy cập, cô lập dữ liệu, mất toàn vẹn, mất nguyên tử (sập giữa chừng), bất thường đồng thời (lost update), bảo mật khó.

> [!question] Thẻ 0.3 — Ý tưởng cốt lõi của DBMS là gì?
> **Đáp:** **trừu tượng hoá** — cho người dùng khung nhìn đơn giản (bảng/SQL), giấu cấu trúc vật lý. Chia 3 mức: vật lý → logic → khung nhìn.

> [!question] Thẻ 0.4 — Phân biệt instance và schema.
> **Đáp:** **schema** = thiết kế tổng thể (cấu trúc bảng), đổi hiếm; **instance** = dữ liệu tại một thời điểm, đổi liên tục. Như *kiểu* vs *giá trị* của biến.

> [!question] Thẻ 0.5 — Tính nguyên tử (atomicity) nghĩa là gì? DBMS bảo đảm bằng gì?
> **Đáp:** một chuỗi thao tác xảy ra **trọn vẹn hoặc không gì cả**; bảo đảm bằng **transaction** (`BEGIN…COMMIT`, lỗi thì `ROLLBACK`).

## 7. Câu hỏi tự kiểm tra

1. Vì sao "lưu vào file + viết chương trình" lại sinh ra dư thừa và không nhất quán? *(mục 2, bệnh 1)*
2. Giải thích ví dụ chuyển \$500 bị "sập giữa chừng". Transaction chữa nó thế nào? *(mục 2 & 4, Silberschatz tr. 7)*
3. Lost update ở ví dụ sĩ số 39 xảy ra ra sao? Thuộc nhóm bệnh nào? *(mục 2 & 4, bệnh 6)*
4. Ba mức trừu tượng là gì? Ai làm việc ở mức nào? *(mục 3)*
5. Chạy demo mục 4. Đổi `:memory:` thành file — khác biệt gì về lưu bền? *(mục 4 Tự thử)*

## Tóm tắt một trang

```
BÀI 0 — DBMS LÀ GÌ + VÌ SAO CẦN
─────────────────────────────────────────────────────────
DBMS  = dữ liệu liên quan + chương trình truy cập; lưu/truy xuất TIỆN & HIỆU QUẢ
   (Silberschatz tr.1). Sinh ra để thay "file phẳng + app chắp vá".

SÁU BỆNH CỦA FILE PHẲNG  (1) dư thừa & không nhất quán  (2) khó truy cập
   (3) cô lập dữ liệu  (4) mất toàn vẹn  (5) mất nguyên tử (sập giữa chừng)
   (6) bất thường đồng thời (lost update) + bảo mật khó.

Ý TƯỞNG CỐT LÕI  = TRỪU TƯỢNG HOÁ. 3 mức: VẬT LÝ (byte/index) → LOGIC
   (bảng/cột/ràng buộc) → KHUNG NHÌN (mỗi người 1 phần). schema (thiết kế,
   đổi hiếm) vs instance (dữ liệu lúc chạy, đổi liên tục).

DEMO (SQL thật)  bệnh 1: 2 file → 2 địa chỉ lệch. bệnh 5: không txn mất 500,
   có BEGIN/ROLLBACK → nguyên vẹn. bệnh 6: 2 phiên đan xen → sĩ số 40 thay vì 41.

13 BÀI  quan hệ → SQL → thiết kế → LƯU TRỮ → INDEX → QUERY → TXN → ĐỒNG THỜI →
   PHỤC HỒI → phân tán. Ruột engine = Bài 4–11.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** (McGraw-Hill) — **Chapter 1: Introduction**: định nghĩa DBMS, nhược điểm hệ file phẳng, trừu tượng hoá dữ liệu (3 mức), mô hình dữ liệu, instance/schema. `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- **Bailis, Hellerstein, Stonebraker (biên tập) — *Readings in Database Systems*, 5th ed. (Red Book, 2015)** — dùng ở các bài sau cho góc nhìn lịch sử & hệ hiện đại. `tai_lieu/Readings in Database Systems 5th Edition.pdf`.
- Liên hệ mạch cloud: [cloud-base — tầng Dữ liệu (DDIA)](../../cloud-base/README.md) nhìn cùng chủ đề từ góc ứng dụng quy mô lớn.

---

**Bản đồ khoá học:** **[Bài 0 — DBMS là gì] ← bạn đang ở đây** · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
