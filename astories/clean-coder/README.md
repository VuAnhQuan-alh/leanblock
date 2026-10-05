# The Clean Coder — Hồ sơ ca nghề lập trình chuyên nghiệp

Khoá tự học theo lối **case-study**, dựng từ chính văn bản gốc — không viết theo trí nhớ.

**Sách gốc:** *The Clean Coder: A Code of Conduct for Professional Programmers* — **Robert C. Martin** ("Uncle Bob"), Pearson, 2011 (bản tiếng Anh, 244 trang PDF nằm trong `tai_lieu/`). Đây **không** phải sách kỹ thuật code, mà là sách về **cách hành xử chuyên nghiệp**: nói Không, nói Có, TDD, luyện tập, ước lượng, áp lực, cộng tác. Nét đặc trưng của nó là: gần như mọi nguyên tắc đều được rút ra từ một **war story có thật** của chính tác giả.

> [!success] Đã hoàn tất **15/15 bài** (Bài 0 + 1–14) trong `bai_hoc/`.
> Mỗi bài mổ một chương của sách. Trục xuyên suốt: mỗi war story được xử lý theo mạch *chuyện xảy ra → điều Uncle Bob rút ra → **đối chiếu với 2026** → áp dụng cho bạn (hai tầng: lập trình viên / nghề tri thức khác)*.
> Bảng [Bản đồ khoá học](#bản-đồ-khoá-học--15-bài) bên dưới trỏ tới từng bài.

---

## Vì sao là "case-study"?

Cuốn sách *đã là* một tuyển tập ca thực chiến: đêm mất trắng dữ liệu ở Teradyne 1979, đoạn code "3 giờ sáng", người đàn ông trong gương, chuyến học TDD với Kent Beck, ca bị đuổi việc năm 1976… Khoá này giữ nguyên sức mạnh đó, và thêm một lớp **"kỹ càng"**: vì sách viết năm 2011 và nhiều lời khuyên rất "gắt" (Uncle Bob tuyệt đối hoá TDD, đòi 100% coverage, kê công thức "60 giờ/tuần"…), mỗi ca đều có mục **`[!warning] Đối chiếu 2026`** tách *nguyên tắc còn sống* khỏi *bối cảnh/lời khuyên đã lỗi thời hoặc gây tranh cãi*.

Đúng tinh thần chương cuối của sách: đừng để khoá này *thuyết phục* bạn bằng lý lẽ — hãy để nó cho bạn **đứng sau lưng Uncle Bob mà quan sát** một người thợ sống qua bốn thập niên sai lầm và rút ra.

---

## Cách đọc & quy ước

| Ký hiệu | Nghĩa |
| --- | --- |
| `Ch. 7` | trích theo **chương** của sách |
| `tr. 150` | **số trang in trong sách** (muốn tra tệp PDF thì cộng 33: PDF = `tr. + 33`) |
| **Mục Mở đầu** | mỗi bài mở bằng một **war story** của chương đó (story-first) |
| `[!quote]` | câu chốt để **nguyên văn tiếng Anh** (nguồn là tiếng Anh) kèm bản dịch gọn bên dưới |
| `[!warning]` **Đối chiếu 2026** | tách nguyên tắc còn đúng khỏi phần đã lỗi thời/gây tranh cãi năm 2026 |
| `[!question]` **Áp dụng vào việc của bạn** | bài tự thực hành *hai tầng*: một cho lập trình viên, một suy rộng ra nghề tri thức khác |
| `[!note]` **Mở rộng** | kiến thức nền sách lướt qua hoặc bối cảnh cần thêm |

Định dạng chuẩn kho: **Obsidian callout**, tiêu đề `##` không kèm emoji. Mở bằng Obsidian hoặc VS Code + Markdown Preview.

---

## Bốn cụm chủ đề

Sách có 14 chương; khoá gom thành bốn mạch (kèm Bài 0 nhập môn):

| Cụm | Ý | Bài |
| --- | --- | :---: |
| **Cam kết** | chịu trách nhiệm, nói Không, nói Có | 0–3 |
| **Nghề** | viết code, TDD, luyện tập, kiểm thử | 4–8 |
| **Tự quản** | thời gian, ước lượng, áp lực | 9–11 |
| **Con người** | cộng tác, đội & dự án, dẫn dắt | 12–14 |

---

## Những ca "gắt" nhất — nơi 2026 cãi lại Uncle Bob

Nếu bạn chỉ có thời gian đọc vài bài, đây là những chỗ tranh luận sống động nhất:

| Bài | Uncle Bob nói (2011) | 2026 đối chiếu |
| --- | --- | --- |
| [Bài 1](bai_hoc/bai_01_tinh_chuyen_nghiep.md) | "100% coverage, tôi *đòi hỏi* điều đó" + công thức 60 giờ | coverage 100% là mục tiêu sai; công thức 60 giờ mù trước đặc quyền |
| [Bài 5](bai_hoc/bai_05_tdd.md) | "The controversy is over. TDD works" | 2014 "Is TDD Dead?" — tranh cãi *chưa* đóng; test-first là *một* kỷ luật |
| [Bài 10](bai_hoc/bai_10_uoc_luong.md) | PERT: đoán O/N/P trước | #NoEstimates + dự báo Monte Carlo từ dữ liệu thật |
| [Bài 11](bai_hoc/bai_11_ap_luc.md) | (tự phản bác Bài 1) văn hoá "80 giờ = anh hùng" là độc hại | 2026 đứng hẳn về phía này: sustainable pace |
| [Bài 12](bai_hoc/bai_12_cong_tac.md) | phải ngồi quay mặt nhau, "ngửi nỗi sợ của nhau" | làm việc từ xa lật đổ lời khuyên đồng-địa-điểm |

---

## Bản đồ khoá học — 15 bài

| # | Bài | Chương gốc | Ca/khái niệm chính |
| ---: | --- | :---: | --- |
| 0 | [Nhập môn](bai_hoc/bai_00_nhap_mon.md) | Introduction | sách = "danh mục lỗi của chính tôi" |
| 1 | [Tính chuyên nghiệp](bai_hoc/bai_01_tinh_chuyen_nghiep.md) | Ch.1 | đêm Teradyne 1979; "do no harm"; Boy Scout rule |
| 2 | [Nói Không](bai_hoc/bai_02_noi_khong.md) | Ch.2 | ASC go-live; "there is no trying"; John Blanco |
| 3 | [Nói Có](bai_hoc/bai_03_noi_co.md) | Ch.3 | ngôn ngữ cam kết "I will… by…" |
| 4 | [Viết code](bai_hoc/bai_04_viet_code.md) | Ch.4 | code 3 giờ sáng; the Zone; being late; overtime |
| 5 | [TDD](bai_hoc/bai_05_tdd.md) | Ch.5 | ba luật; "the controversy is over" |
| 6 | [Luyện tập](bai_hoc/bai_06_luyen_tap.md) | Ch.6 | kata, coding dojo; performance ≠ practice |
| 7 | [Kiểm thử chấp nhận](bai_hoc/bai_07_acceptance_testing.md) | Ch.7 | ED-402; kế hoạch test 1 triệu đô; định nghĩa Done |
| 8 | [Chiến lược kiểm thử](bai_hoc/bai_08_chien_luoc_kiem_thu.md) | Ch.8 | ngày "săn bug"; kim tự tháp test |
| 9 | [Quản lý thời gian](bai_hoc/bai_09_quan_ly_thoi_gian.md) | Ch.9 | focus-manna; Pomodoro; Rule of Holes; mess |
| 10 | [Ước lượng](bai_hoc/bai_10_uoc_luong.md) | Ch.10 | 32 chip; estimate là phân phối; PERT; planning poker |
| 11 | [Áp lực](bai_hoc/bai_11_ap_luc.md) | Ch.11 | người đàn ông trong gương; kỷ luật thời khủng hoảng |
| 12 | [Cộng tác](bai_hoc/bai_12_cong_tac.md) | Ch.12 | bị đuổi 1976; tường code; "cọ tiểu não" |
| 13 | [Đội và dự án](bai_hoc/bai_13_doi_va_du_an.md) | Ch.13 | "no half a person"; gelled team; velocity |
| 14 | [Dẫn dắt, học nghề & nghề thủ công](bai_hoc/bai_14_dan_dat_hoc_nghe.md) | Ch.14 | Digi-Comp I; học nghề; craftsmanship là meme |

> Phụ lục A "Tooling" của sách (công cụ năm 2011) **không** được đưa vào khoá — là phần lỗi thời nhất, giá trị học thấp.

---

## Nguồn

- **Robert C. Martin**, *The Clean Coder: A Code of Conduct for Professional Programmers*, Pearson, 2011 — `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`.
- Bối cảnh 2026 trong các mục *Đối chiếu 2026* dẫn từ ngoài sách (ghi rõ ở mục **Nguồn** của từng bài): "Is TDD Dead?" (2014), #NoEstimates, Testing Trophy, Team Topologies, Manifesto for Software Craftsmanship (2009), sustainable pace, v.v.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.
