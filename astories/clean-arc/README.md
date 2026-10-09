# Clean Architecture — Khoá tự học cấu trúc phần mềm sạch

Khoá tự học **khái niệm + sơ đồ**, dựng từ chính văn bản gốc — không viết theo trí nhớ.

**Sách gốc:** *Clean Architecture: A Craftsman's Guide to Software Structure and Design* — **Robert C. Martin** ("Uncle Bob"), Prentice Hall, 2017 (bản tiếng Anh, 429 trang PDF trong `tai_lieu/`). Đây là sách về **cấu trúc hệ thống**: hệ hình lập trình, SOLID, nguyên tắc component, ranh giới, Dependency Rule, và vòng tròn Clean Architecture. Là **tập cuối bộ ba** Uncle Bob — sau [`clean-coder`](../clean-coder/README.md) (hành xử nghề) và [`clean-code`](../clean-code/README.md) (viết code).

> [!success] Đã hoàn tất **12/12 bài** (Bài 0 + 1–11) trong `bai_hoc/`.
> Mỗi bài gom một Phần/cụm chương của sách. Trục xuyên suốt: *khái niệm đào sâu → sơ đồ ASCII nơi cần → **demo TypeScript chạy được** ở chỗ code soi sáng → trích nguyên văn → **đối chiếu 2026** → áp dụng vào dự án của bạn*.
> Bảng [Bản đồ khoá học](#bản-đồ-khoá-học--12-bài) bên dưới trỏ tới từng bài.

---

## Vì sao "khái niệm + sơ đồ + demo chọn lọc"?

Khác [`clean-code`](../clean-code/README.md) (code-first, nói về chính code), cuốn này nói về *cấu trúc và chiều phụ thuộc* — thứ sống trong sơ đồ hơn là từng dòng. Nên khoá:

- **Giảng khái niệm đào sâu** và đóng gói các phân loại của sách thành **bảng so sánh** (3 hệ hình, 5 SOLID, REP/CCP/CRP + ADP/SDP/SAP, 4 lối đóng gói…).
- **Vẽ lại sơ đồ cốt lõi bằng ASCII**: ma trận Eisenhower (Bài 0), đảo phụ thuộc (Bài 1), tam giác căng cohesion (Bài 4), boundary crossing (Bài 6), **vòng tròn đồng tâm Clean Architecture** (Bài 7).
- **Chỉ nhúng demo TS chạy được** ở nơi code thật sự soi sáng: đảo phụ thuộc/plugin (Bài 1), SRP accidental duplication (Bài 2), LSP Square/Rectangle (Bài 3), đo Instability + dò chu trình (Bài 4), hoãn-quyết-định-DB (Bài 5), vượt ranh giới (Bài 6), **ráp đủ 4 vòng** (Bài 7, 11), Humble Object (Bài 8), arm's-length framework (Bài 9), package-by-component (Bài 10).

Và lớp **`[!warning] Đối chiếu 2026`** xuyên suốt: micro-service backlash & modular monolith, vertical slice, "clean arch là over-engineering cho app nhỏ" (góc ponytail), serverless/edge, AI scaffolding — tách *nguyên tắc còn sống* khỏi *phần đã cũ hoặc đang bị cãi*.

---

## Cách đọc & quy ước

| Ký hiệu | Nghĩa |
| :--- | :--- |
| `Ch. 22` | trích theo **chương** của sách |
| `tr. 203` | **số trang in trong sách** (muốn tra tệp PDF thì cộng 27: PDF = `tr. + 27`) |
| `[!quote]` | câu chốt để **nguyên văn tiếng Anh** (nguồn là tiếng Anh) kèm bản dịch gọn bên dưới |
| ` ```typescript ` | demo **chạy được**: cấu trúc/nguyên tắc minh hoạ bằng code, output thật dán ngay dưới |
| `[!warning]` **Đối chiếu 2026** | tách nguyên tắc còn đúng khỏi phần đã lỗi/gây tranh cãi năm 2026 |
| `[!question]` **Áp dụng vào dự án của bạn** | bài tự thực hành trên chính dự án của bạn |
| `[!note]` **Tự thử** | vài chỉnh nhỏ trên demo để quan sát hành vi đổi |

**Chạy code:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không `tsc`, không `tsconfig.json`. Định dạng chuẩn kho: **Obsidian callout**, tiêu đề `##` không kèm emoji.

> [!warning] Lưu ý khi sửa file `.md`
> **Đừng chạy "Format Document" / để format-on-save** trên các bài — một số trình format markdown (Prettier, Markdown All in One) **escape dấu ngoặc callout** (`[!quote]` → `[!quote]`), làm Obsidian *không* render callout nữa. Hãy tắt format-on-save cho `.md` trong dự án này.

---

## Bảy phần của sách → bốn cụm bài

Sách có 34 chương chia 7 Phần; khoá gom thành bốn cụm (kèm Bài 0):

| Cụm | Phần sách | Bài |
| :--- | :--- | :---: |
| **Nền tảng** | I–II (giá trị, hệ hình lập trình) | 0–1 |
| **Nguyên tắc** | III–IV (SOLID, component) | 2–4 |
| **Kiến trúc** | V (ranh giới, Dependency Rule, vòng tròn) | 5–8 |
| **Chi tiết & thực chiến** | VI (DB/web/framework, đóng gói, case study) | 9–11 |

---

## Những ca "gắt" nhất — nơi 2026 cân lại Uncle Bob

Nếu chỉ có thời gian đọc vài bài, đây là những chỗ tranh luận sống động nhất:

| Bài | Uncle Bob nói (2017) | 2026 đối chiếu |
| :--- | :--- | :--- |
| [Bài 5](bai_hoc/bai_05_kien_truc_va_doc_lap.md) | "đừng vội lên service level" | modular monolith thắng thế — sách đúng từ 2017 |
| [Bài 7](bai_hoc/bai_07_clean_architecture.md) | bốn vòng + Dependency Rule | quá nhiều tầng cho app nhỏ → vertical slice (Bogard) |
| [Bài 8](bai_hoc/bai_08_humble_main_services.md) | "micro-service không tự cho kiến trúc" | distributed monolith là phản mẫu; Prime Video gộp về monolith |
| [Bài 9](bai_hoc/bai_09_chi_tiet.md) | "đừng cưới framework" | startup/đời-ngắn ôm framework lại là đúng — cược theo vòng đời |
| [Bài 0](bai_hoc/bai_00_hai_gia_tri.md) | "kiến trúc quan trọng hơn hành vi" | đừng lạm để over-engineer; giữ-ngỏ ≠ quyết-sẵn-tất-cả |

---

## Bản đồ khoá học — 12 bài

| # | Bài | Chương gốc | Demo / sơ đồ chính |
| ---: | :--- | :---: | :--- |
| 0 | [Hai giá trị](bai_hoc/bai_00_hai_gia_tri.md) | Ch.1–2 | mềm vs cứng (thêm "JP"); ma trận Eisenhower |
| 1 | [Ba hệ hình lập trình](bai_hoc/bai_01_he_hinh_lap_trinh.md) | Ch.3–6 | đảo phụ thuộc/plugin (`copy`); 3 hệ hình |
| 2 | [SOLID (1): SRP, OCP](bai_hoc/bai_02_solid_srp_ocp.md) | Ch.7–8 | SRP: đổi của CFO rò rỉ sang COO |
| 3 | [SOLID (2): LSP, ISP, DIP](bai_hoc/bai_03_solid_lsp_isp_dip.md) | Ch.9–11 | LSP: Square/Rectangle ra 4 thay vì 10 |
| 4 | [Nguyên tắc Component](bai_hoc/bai_04_nguyen_tac_component.md) | Ch.12–14 | đo Instability + dò chu trình; tam giác căng |
| 5 | [Kiến trúc là gì & Độc lập](bai_hoc/bai_05_kien_truc_va_doc_lap.md) | Ch.15–16 | hoãn quyết định DB (`greet`) |
| 6 | [Ranh giới & Dependency Rule](bai_hoc/bai_06_ranh_gioi_dependency_rule.md) | Ch.17–19 | vượt ranh giới (`processPayment` + port) |
| 7 | [Business Rules & The Clean Architecture](bai_hoc/bai_07_clean_architecture.md) | Ch.20–22 | **vòng tròn 4 lớp**; ráp đủ bốn vòng |
| 8 | [Humble Object, Main, Services](bai_hoc/bai_08_humble_main_services.md) | Ch.23–28 | Humble Object (Presenter/View) |
| 9 | [Chi tiết: DB, Web, Framework](bai_hoc/bai_09_chi_tiet.md) | Ch.30–32 | arm's-length framework (proxy) |
| 10 | [The Missing Chapter: đóng gói](bai_hoc/bai_10_dong_goi.md) | Ch.34 | package-by-component (`#private` thật) |
| 11 | [Case study & tổng kết](bai_hoc/bai_11_case_study.md) | Ch.33 | capstone: mua video, đủ 4 vòng |

> Các chương **không** đưa vào khoá: **Ch.29 "Clean Embedded Architecture"** (quá hẹp — nhúng) và **Phụ lục A "Architecture Archaeology"** (hồi ký nghề 50 trang, giá trị cấu trúc thấp) — như `clean-code` đã bỏ các phụ lục tra cứu. Ch.28 "The Test Boundary" được gập vào [Bài 8](bai_hoc/bai_08_humble_main_services.md).

---

## Nguồn

- **Robert C. Martin**, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*, Prentice Hall, 2017 — `tai_lieu/Clean.Architecture.2017.9.pdf`. (Ch.34 do **Simon Brown** viết.)
- Bối cảnh 2026 trong các mục *Đối chiếu 2026* dẫn từ ngoài sách (ghi rõ ở mục **Nguồn** của từng bài): modular monolith (Shopify; Amazon Prime Video 2023), Vertical Slice Architecture (Jimmy Bogard), evolutionary architecture (Neal Ford), Hexagonal/Onion (Cockburn/Palermo), dependency-cruiser/Nx/ArchUnit, v.v.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 27`.
