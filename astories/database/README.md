# database — Ruột một database engine

> Không chỉ *dùng* SQL mà hiểu **bên trong** một hệ quản trị cơ sở dữ liệu quan hệ chạy ra sao: lưu dữ liệu, đánh chỉ mục, thực thi truy vấn, giữ nhất quán và phục hồi. Đi từ nền quan hệ xuống tới ruột engine. **Tự chứa** — không bắt buộc đọc khoá khác trước.

## Hai tầng — nền rồi ruột

```
   RUỘT ENGINE   lưu trữ → index → xử lý truy vấn → transaction → đồng thời → phục hồi
   ─────────────────────────────────────────────────────────────────────────────────
   NỀN           mô hình quan hệ → SQL → thiết kế & chuẩn hoá
```

## Danh sách bài (13 bài, 0–12)

| # | Bài | Mảng | Nguồn |
| :-- | :-- | :-- | :-- |
| 0 | [DBMS là gì & vì sao cần](bai_hoc/bai_00_dbms-la-gi.md) | động lực, trừu tượng hoá | Ch1 |
| 1 | [Mô hình quan hệ & đại số quan hệ](bai_hoc/bai_01_mo-hinh-quan-he.md) | nền toán của bảng/SQL | Ch2 |
| 2 | [SQL từ nền tới sâu](bai_hoc/bai_02_sql.md) | truy vấn, join, view | Ch3–5 |
| 3 | [Thiết kế & chuẩn hoá](bai_hoc/bai_03_thiet-ke-chuan-hoa.md) | E-R, FD, BCNF | Ch6–7 |
| 4 | [Lưu trữ vật lý & buffer manager](bai_hoc/bai_04_luu-tru-buffer.md) | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | [Index: B+tree](bai_hoc/bai_05_index-btree.md) | tra cứu nhanh | Ch14 |
| 6 | [Index nâng cao: LSM & bitmap](bai_hoc/bai_06_index-lsm-bitmap.md) | tối ưu ghi/phân tích | Ch24 |
| 7 | [Xử lý truy vấn: join algorithms](bai_hoc/bai_07_query-join.md) | thực thi truy vấn | Ch15 |
| 8 | [Tối ưu truy vấn (cost-based)](bai_hoc/bai_08_query-optimization.md) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | [Transaction & ACID, isolation](bai_hoc/bai_09_transaction-acid.md) | đúng khi có lỗi | Ch17 |
| 10 | [Đồng thời: 2PL / MVCC](bai_hoc/bai_10_concurrency.md) | đúng khi song song | Ch18 |
| 11 | [Phục hồi: WAL / ARIES](bai_hoc/bai_11_recovery.md) | sống sót sau sập | Ch19 |
| 12 | [Song song & phân tán (góc DB)](bai_hoc/bai_12_phan-tan.md) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Trọng tâm *"ruột engine"* là Bài 4–11. Bài 0–3 dựng nền quan hệ/SQL/thiết kế vừa đủ để tự chứa.

## Nguồn (Luật số 1)

| Mã | Nguồn | Trích |
| :-- | :-- | :-- |
| **Silberschatz** | *Database System Concepts*, 7th ed. (Silberschatz, Korth, Sudarshan) | `Silberschatz (tr. N)`, PDF = tr. + 29 |
| **Red Book** | *Readings in Database Systems*, 5th ed. (Bailis, Hellerstein, Stonebraker, 2015) | `Red Book` (tiểu luận biên tập, góc nhìn & hệ hiện đại) |

PDF nằm trong `tai_lieu/`. Mọi câu chữ nguyên văn trích trực tiếp từ nguồn, không viết từ trí nhớ.

## Phong cách

Phần lớn bài theo mạch **A–E**: tình huống cụ thể → cách nghĩ ngây thơ rồi vì sao sai → ẩn dụ → ví dụ số/sơ đồ dắt tay → **demo chạy thật tất định** (nhóm transaction Bài 9–11 bám sát trích nguồn hơn là ẩn dụ). Demo bằng **TypeScript (Node 22+)**: phần SQL dùng module tích hợp `node:sqlite` (chạy `node --experimental-sqlite file.ts`, không cài gói); phần internals (B+tree, buffer pool, LSM, lock manager, WAL, join algorithms...) viết TS thuần. Dùng Obsidian callout, không emoji. Mỗi bài khép bằng thẻ ôn, câu hỏi tự kiểm, tóm tắt một trang.

## Liên hệ mạch cloud

Khoá này nhìn dữ liệu từ góc **bên trong engine**. Mạch cloud nhìn cùng chủ đề từ góc **ứng dụng quy mô lớn**: [`cloud-base`](../cloud-base/README.md) (nền CS, trụ Dữ liệu từ DDIA), [`aws-fund`](../aws-fund/README.md), [`aws-design`](../aws-design/README.md), [`sre`](../sre/README.md).

## Kiểm chứng

`python3 /tmp/verify_db.py` — chạy toàn bộ code, đối chiếu output tất định từng ký tự, kiểm quote nguyên văn với PDF, link/anchor, và emoji.
