# Clean Code — Khoá tự học code sạch bằng TypeScript chạy được

Khoá tự học theo lối **code-first**, dựng từ chính văn bản gốc — không viết theo trí nhớ.

**Sách gốc:** *Clean Code: A Handbook of Agile Software Craftsmanship* — **Robert C. Martin** ("Uncle Bob"), Prentice Hall, 2008 (bản tiếng Anh, 462 trang PDF trong `tai_lieu/`). Đây là sách **kỹ thuật viết code**: đặt tên, hàm, comment, lớp, xử lý lỗi, test, concurrency, và một danh mục "mùi code". Khác hẳn cuốn chị em *The Clean Coder* (nói về *hành xử* nghề — xem khoá [`clean-coder`](../clean-coder/README.md)).

> [!success] Đã hoàn tất **16/16 bài** (Bài 0 + 1–15) trong `bai_hoc/`.
> Mỗi bài mổ một chương. Trục xuyên suốt: *code bẩn → gọi tên "mùi" → bản sạch **chạy được** (TypeScript) → nguyên tắc (trích nguyên văn) → **đối chiếu 2026** → áp dụng vào codebase của bạn*.
> Bảng [Bản đồ khoá học](#bản-đồ-khoá-học--16-bài) bên dưới trỏ tới từng bài.

---

## Vì sao "code-first"?

Cuốn sách *nói về chính code*, nên xương sống tự nhiên của khoá là **chạy được**: gần như mỗi bài có một demo TypeScript — một bản bẩn và một bản sạch cho **cùng kết quả**, để thấy tận mắt khác biệt mà một nguyên tắc tạo ra. Quy ước code lấy từ kho `simplychain`: Node 22 chạy thẳng `.ts`, không cần cài gói.

Và thêm một lớp **"kỹ càng"**: *Clean Code* năm 2026 vừa kinh điển vừa **bị cãi dữ dội** (Casey Muratori *"Clean Code, Horrible Performance"*, John Ousterhout về hàm/lớp quá nhỏ, tranh luận *"Is TDD Dead?"*…). Mỗi bài có mục **`[!warning] Đối chiếu 2026`** tách *nguyên tắc còn sống* khỏi *phần đã lỗi hoặc đang bị phản biện* — đúng tinh thần chính Uncle Bob mời: "nhiều khuyến nghị trong sách gây tranh cãi… chúng tôi không dám nhận là chân lý cuối cùng" (Ch.1, tr.13).

---

## Cách đọc & quy ước

| Ký hiệu | Nghĩa |
| --- | --- |
| `Ch. 7` | trích theo **chương** của sách |
| `tr. 150` | **số trang in trong sách** (muốn tra tệp PDF thì cộng 31: PDF = `tr. + 31`) |
| `[!quote]` | câu chốt để **nguyên văn tiếng Anh** (nguồn là tiếng Anh) kèm bản dịch gọn bên dưới |
| ` ```typescript ` | demo **chạy được**: bản bẩn → bản sạch, output thật dán ngay dưới |
| `[!warning]` **Đối chiếu 2026** | tách nguyên tắc còn đúng khỏi phần đã lỗi thời/gây tranh cãi năm 2026 |
| `[!question]` **Áp dụng vào codebase của bạn** | bài tự thực hành trên chính code của bạn |
| `[!note]` **Tự thử** | vài chỉnh nhỏ trên demo để quan sát hành vi đổi |

**Chạy code:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không `tsc`, không `tsconfig.json`. Định dạng chuẩn kho: **Obsidian callout**, tiêu đề `##` không kèm emoji.

---

## Bốn cụm chủ đề

Sách có 17 chương; khoá gom thành bốn mạch (kèm Bài 0 nhập môn):

| Cụm | Ý | Bài |
| --- | --- | :---: |
| **Nền tảng** | code sạch là gì, tên, hàm, comment, định dạng | 0–4 |
| **Cấu trúc** | object/dữ liệu, lỗi, ranh giới, test, lớp | 5–9 |
| **Hệ thống & nổi lên** | hệ thống, thiết kế đơn giản, concurrency | 10–12 |
| **Thực chiến** | xem code sạch nảy sinh, refactor ngoài đời, danh mục mùi | 13–15 |

---

## Những ca "gắt" nhất — nơi 2026 cãi lại Uncle Bob

Nếu bạn chỉ có thời gian đọc vài bài, đây là những chỗ tranh luận sống động nhất:

| Bài | Uncle Bob nói (2008) | 2026 đối chiếu |
| --- | --- | --- |
| [Bài 2](bai_hoc/bai_02_ham.md) | "hàm phải nhỏ, rồi nhỏ hơn thế" | Ousterhout: tách quá đà → "shallow module", tăng tải nhận thức |
| [Bài 5](bai_hoc/bai_05_object_va_du_lieu.md) | đa hình thay switch theo loại | Muratori *"Clean Code, Horrible Performance"* — data-oriented design |
| [Bài 3](bai_hoc/bai_03_comment.md) | "comment luôn là thất bại" | 2026 rộng lượng với comment-*vì-sao*, docstring/TSDoc |
| [Bài 6](bai_hoc/bai_06_xu_ly_loi.md) | "đừng trả null" + exception | `strictNullChecks` + kiểu `Result<T,E>`/`Option` |
| [Bài 8](bai_hoc/bai_08_unit_test.md) | TDD "ba luật", nghiêng unit test | *"Is TDD Dead?"* (2014); Testing Trophy nghiêng integration |

---

## Bản đồ khoá học — 16 bài

| # | Bài | Chương gốc | Demo / khái niệm chính |
| ---: | --- | :---: | --- |
| 0 | [Clean Code là gì](bai_hoc/bai_00_clean_code_la_gi.md) | Ch.1 | định nghĩa của sáu bậc thầy; Boy Scout rule; đọc:viết 10:1 |
| 1 | [Đặt tên](bai_hoc/bai_01_dat_ten.md) | Ch.2 | `getThem` → `getFlaggedCells` → `cell.isFlagged()` |
| 2 | [Hàm](bai_hoc/bai_02_ham.md) | Ch.3 | switch trả lương → đa hình qua factory; cờ boolean |
| 3 | [Comment](bai_hoc/bai_03_comment.md) | Ch.4 | comment tan vào `isEligibleForFullBenefits()` |
| 4 | [Định dạng](bai_hoc/bai_04_dinh_dang.md) | Ch.5 | ẩn dụ tờ báo; dồn-một-dòng vs sạch cùng ra 56 |
| 5 | [Object & dữ liệu](bai_hoc/bai_05_object_va_du_lieu.md) | Ch.6 | Shape thủ tục vs OO; đối xứng ngược; Luật Demeter |
| 6 | [Xử lý lỗi](bai_hoc/bai_06_xu_ly_loi.md) | Ch.7 | đừng trả null → danh sách rỗng (Special Case) |
| 7 | [Ranh giới](bai_hoc/bai_07_ranh_gioi.md) | Ch.8 | bọc `Map` trong `Sensors`; learning test; Adapter |
| 8 | [Unit test](bai_hoc/bai_08_unit_test.md) | Ch.9 | ba luật TDD; một khái niệm mỗi test; F.I.R.S.T |
| 9 | [Class](bai_hoc/bai_09_class.md) | Ch.10 | SRP; cohesion; `Portfolio` + DIP test bằng stub |
| 10 | [Hệ thống](bai_hoc/bai_10_he_thong.md) | Ch.11 | tách dựng khỏi dùng; factory + DI qua `main` |
| 11 | [Thiết kế nổi lên](bai_hoc/bai_11_thiet_ke_noi_len.md) | Ch.12 | bốn quy tắc đơn giản; Template Method `VacationPolicy` |
| 12 | [Concurrency](bai_hoc/bai_12_concurrency.md) | Ch.13 (+ Phụ lục A) | race async: rút 30+30 từ 100 còn 70 |
| 13 | [Xem code sạch nảy sinh](bai_hoc/bai_13_xem_code_nay_sinh.md) | Ch.14 | port `Args` → `ArgumentMarshaler` đa hình |
| 14 | [Refactor ngoài đời](bai_hoc/bai_14_refactor_ngoai_doi.md) | Ch.15–16 | characterization test; review chuyên nghiệp; Boy Scout |
| 15 | [Danh mục mùi code](bai_hoc/bai_15_danh_muc_mui_code.md) | Ch.17 | ~66 mùi (C/E/F/G/J/N/T) tra chéo về các bài |

> Phụ lục B "SerialDate source" (60 trang source) và Phụ lục C "Cross References" (index) của sách **không** được đưa vào khoá — là phần thuần tra cứu, giá trị học thấp. Phụ lục A "Concurrency II" được gập tinh tuý vào [Bài 12](bai_hoc/bai_12_concurrency.md).

---

## Nguồn

- **Robert C. Martin**, *Clean Code: A Handbook of Agile Software Craftsmanship*, Prentice Hall, 2008 — `tai_lieu/Clean.Code.2008.8.pdf`.
- Bối cảnh 2026 trong các mục *Đối chiếu 2026* dẫn từ ngoài sách (ghi rõ ở mục **Nguồn** của từng bài): Casey Muratori *"Clean Code, Horrible Performance"* (2023), John Ousterhout *A Philosophy of Software Design* (2018), *"Is TDD Dead?"* (2014), Testing Trophy, Sandi Metz *"The Wrong Abstraction"*, Clean Architecture (2017), các linter/analyzer (ESLint/SonarQube), v.v.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 31`.
