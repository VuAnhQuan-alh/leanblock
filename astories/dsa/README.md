# Khoá DSA — Cấu trúc dữ liệu & Giải thuật (mức "đủ dùng")

Khoá tự học **cấu trúc dữ liệu & giải thuật** cho kỹ sư backend / hệ thống, tới mức **"đủ dùng"** — nhìn một bài toán là *gọi tên* được cấu trúc dữ liệu và chiến lược thuật toán phù hợp, ước lượng được chi phí, biết khi nào một cách làm là **sai** hay **quá chậm**. **Không** phải luyện thi competitive programming.

Mỗi bài theo phong cách **A–E**: tình huống → cách ngây thơ (và vì sao sai/chậm) → khái niệm chặt (trích nguyên văn nguồn) → ví dụ số/sơ đồ dắt tay → **demo TypeScript chạy thật, tất định**. Định dạng Obsidian callout, heading không emoji (mũi tên `→ ← ↑ ↓` trong sơ đồ là cấu trúc, được giữ).

## Hai tầng, 15 bài

**Tầng lõi (0–11)** — đủ cho phần lớn công việc thực tế:

| # | Bài | Chủ đề chính | Nguồn |
| :-- | :-- | :-- | :-- |
| 0 | [Thuật toán & tính đúng](bai_hoc/bai_00_thuat-toan-la-gi.md) | đúng vs hiệu quả, phản ví dụ | Skiena Ch1 + Grokking |
| 1 | [Phân tích Big-O](bai_hoc/bai_01_big-o.md) | mô hình RAM, worst case, bậc trội | Skiena Ch2 |
| 2 | [CTDL tuyến tính](bai_hoc/bai_02_ctdl-tuyen-tinh.md) | mảng / list / stack / queue, khấu hao | Skiena Ch3 |
| 3 | [Từ điển & bảng băm](bai_hoc/bai_03_bang-bam.md) | hàm băm, va chạm, hệ số tải | Skiena Ch3 |
| 4 | [Heap & cây tìm kiếm](bai_hoc/bai_04_heap-cay-tim-kiem.md) | BST, cân bằng, hàng đợi ưu tiên | Skiena Ch3–4 |
| 5 | [Sắp xếp](bai_hoc/bai_05_sap-xep.md) | mergesort / quicksort / heapsort, cận dưới | Skiena Ch4 |
| 6 | [Chia để trị & đệ quy](bai_hoc/bai_06_chia-de-tri.md) | truy hồi, master theorem | Skiena Ch5 |
| 7 | [Đồ thị: biểu diễn & duyệt](bai_hoc/bai_07_do-thi-duyet.md) | danh sách kề, BFS / DFS | Skiena Ch7 |
| 8 | [Đồ thị trọng số](bai_hoc/bai_08_do-thi-trong-so.md) | MST (Prim/Kruskal), Dijkstra | Skiena Ch8 |
| 9 | [Quy hoạch động](bai_hoc/bai_09_quy-hoach-dong.md) | memoization, edit distance, knapsack | Skiena Ch10 |
| 10 | [Tìm kiếm tổ hợp & backtracking](bai_hoc/bai_10_backtracking.md) | cây lời giải, pruning, N-Queens | Skiena Ch9 |
| 11 | [NP-đầy đủ & bài toán khó](bai_hoc/bai_11_np-day-du.md) | rút gọn, P vs NP, xấp xỉ | Skiena Ch11–12 |

**Tầng nâng cao (12–14)** — chủ đề chuyên sâu đứng trên nền lõi:

| # | Bài | Chủ đề chính | Nguồn |
| :-- | :-- | :-- | :-- |
| 12 | [Khớp chuỗi](bai_hoc/bai_12_khop-chuoi.md) | Rabin–Karp (băm lăn), KMP | Skiena §6.7 + CLRS Ch32 |
| 13 | [Luồng mạng](bai_hoc/bai_13_luong-mang.md) | Ford–Fulkerson, max-flow = min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | [Thuật toán ngẫu nhiên](bai_hoc/bai_14_ngau-nhien.md) | Las Vegas vs Monte Carlo | Skiena Ch6 |

**Năm trục xuyên suốt:** *đúng* (chứng minh / phản ví dụ) · *hiệu quả* (Big-O) · chọn đúng **cấu trúc dữ liệu** · chọn đúng **khuôn thiết kế** (chia để trị / tham lam / QHĐ / backtracking / rút gọn) · biết khi nào bài là **khó** (NP).

## Nguồn (Luật số 1: không viết từ trí nhớ)

Tài liệu nằm trong `tai_lieu/` (ngoài git do dung lượng). Mọi trích dẫn là **nguyên văn**, kèm số trang in:

- **Skiena — *The Algorithm Design Manual*, 3rd ed.** (nguồn **chính**). **Offset PDF trôi theo chương**: Ch1–2 = tr.+17, Ch3–6 = +16/+15, Ch7–10 = +14, Ch11–12 = +13. Luôn dò lại đúng trang PDF chứa chữ trước khi trích (verifier quét cửa sổ ±5 trang).
- **Grokking Algorithms** (Bhargava) — khởi động trực giác (Bài 0), offset PDF = tr.+19.
- **CLRS — *Introduction to Algorithms*, 4th ed.** — tra cứu chuẩn (KMP, max-flow). Bản PDF **lỗi phông** khi trích text (fi/ffi → ký tự lạ) nên **không trích nguyên văn**; chỉ dẫn làm nguồn tham khảo (Bài 12–13).

## Chạy demo & kiểm chứng

Demo là TypeScript chạy thẳng bằng **Node 22+**, không cài gói:

```bash
node bai_hoc/<tên-bài>.ts
```

Mọi demo **tất định** (chạy hai lần ra một kết quả); bài có ngẫu nhiên dùng PRNG seed cố định. Code đo *số thao tác* (so sánh, lần gọi, bước) làm thước độc lập máy — đúng tinh thần Big-O (Bài 1).

**Verifier** `/tmp/verify_dsa.py` — bốn cổng, tất cả phải xanh:

1. **Code**: trích mọi khối ```` ```typescript ```` từ `.md`, chạy bằng Node, so output char-for-char với khối `Kết quả chạy thật *(tất định)*`.
2. **Quote**: mỗi `> [!quote] Skiena/Grokking (tr. N)` được kiểm nguyên văn trên đúng trang PDF (chuẩn hoá ligature, gạch nối, dấu câu; quét cửa sổ ±5 trang để chịu drift offset).
3. **Link/anchor**: mọi liên kết nội khoá phân giải đúng.
4. **Emoji**: không emoji trong heading/nội dung (mũi tên cấu trúc được loại trừ).

Chốt hiện tại: **code 15/15, quote 77/77 verbatim, 0 link gãy, 0 emoji.**

## Liên hệ mạch khoá khác

- [database](../database/README.md) — một kho giải thuật chạy thật ở quy mô đĩa: B+tree (Bài 4), hash join (Bài 3), sort-merge (Bài 5), query optimizer.
- [cloud-base](../cloud-base/README.md) & [sre](../sre/README.md) — nhiều bài vận hành là NP-khó trá hình (bin packing, lập lịch — Bài 11); locality/cache (Bài 2) định hình hiệu năng thật.

---

*Khoá chị em: học DSA tới "đủ" + đào sâu database — hợp hướng backend / cloud / SRE.*
