# Bài 13 — Đội và dự án: nuôi một đội gắn kết, rồi rót dự án vào nó

> [!info] Về bài này
> Dựng từ **Chương 13 — Teams and Projects** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 167–171`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Cần đọc trước: [Bài 12 — Cộng tác](bai_12_cong_tac.md).

## Mục lục

1. [Mở đầu: đội lắp từ "nửa con người" — cái máy xay sinh tố](#1-mở-đầu-đội-lắp-từ-nửa-con-người--cái-máy-xay-sinh-tố)
2. ["Không có chuyện nửa con người"](#2-không-có-chuyện-nửa-con-người)
3. [Ca chính — Đội gắn kết (gelled team): phép màu cần thời gian lên men](#3-ca-chính--đội-gắn-kết-gelled-team-phép-màu-cần-thời-gian-lên-men)
4. [Đội có trước hay dự án có trước; velocity; nỗi lo của chủ dự án](#4-đội-có-trước-hay-dự-án-có-trước-velocity-nỗi-lo-của-chủ-dự-án)
5. [Đối chiếu 2026](#5-đối-chiếu-2026)
6. [Áp dụng vào việc của bạn](#6-áp-dụng-vào-việc-của-bạn)
7. [Từ điển thuật ngữ](#7-từ-điển-thuật-ngữ)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mở đầu: đội lắp từ "nửa con người" — cái máy xay sinh tố

Qua nhiều năm tư vấn cho các ngân hàng và công ty bảo hiểm, Uncle Bob thấy một kiểu chia dự án kỳ quặc cứ lặp đi lặp lại. Một dự án ở ngân hàng thường là việc nhỏ, cỡ một hai lập trình viên làm trong vài tuần. Vậy mà nó lại được "biên chế" hẳn hoi: một project manager (đang quản *một mớ* dự án khác), một business analyst (đang cấp yêu cầu cho *một mớ* dự án khác), vài lập trình viên (cũng đang dính *một mớ* dự án khác), thêm một hai tester (lại *một mớ* dự án khác nữa). Thấy cái quy luật chưa? Dự án nhỏ tới mức **chẳng ai được phân toàn thời gian** — người nào cũng chỉ làm ở mức 50%, có khi 25%.

> [!quote] The Clean Coder — Ch.13 (tr. 168)
> "That's not a team, that's something that came out of a Waring blender."
>
> *Đó **không** phải một cái đội, đó là thứ vừa chui ra từ một cái **máy xay sinh tố**.*

## 2. "Không có chuyện nửa con người"

Uncle Bob nêu một quy tắc gọn lỏn:

> [!quote] The Clean Coder — Ch.13 (tr. 168)
> "There is no such thing as half a person."
>
> *Làm gì có cái gọi là **nửa con người**.*

Bảo một lập trình viên dành nửa thời gian cho dự án A, nửa cho dự án B là chuyện vô nghĩa — nhất là khi hai dự án lại có PM khác, BA khác, lập trình viên khác, tester khác nhau. Cứ xẻ con người ra thành từng lát mỏng rồi rải khắp các dự án thì chẳng tạo ra được đội nào; nó chỉ tạo ra sinh tố.

## 3. Ca chính — Đội gắn kết (gelled team): phép màu cần thời gian lên men

**Chuyện gì đã xảy ra.** Một cái đội cần *thời gian* mới thành hình: các thành viên dựng quan hệ, học cách cộng tác, học cả tật xấu, điểm mạnh, điểm yếu của nhau — rồi dần dần **gắn kết** (gel) lại:

> [!quote] The Clean Coder — Ch.13 (tr. 168)
> "There is something truly magical about a gelled team. They can work miracles."
>
> *Có một điều gì đó thật sự **kỳ diệu** ở một cái đội đã gắn kết. Họ làm được cả những phép màu.*

Họ đoán trước được ý nhau, đỡ đần cho nhau, và đòi hỏi ở nhau cái tốt nhất. Uncle Bob phác ra một đội gắn kết điển hình (theo mô hình 2011): chừng **12 người** — tỉ lệ lập trình viên so với (tester + analyst) vào khoảng **2:1**, chẳng hạn 7 lập trình viên, 2 tester, 2 analyst, 1 PM. *Analyst* thì viết yêu cầu và acceptance test theo **giá trị nghiệp vụ** (đường hạnh phúc); *tester* viết acceptance test theo **tính đúng** (ca lỗi, ca biên); *PM* theo dõi tiến độ và ưu tiên; còn một thành viên có thể kiêm luôn vai **coach/master** bán thời gian, giữ cho quy trình và kỷ luật của đội khỏi bị áp lực lịch cám dỗ đi tắt.

**Điều rút ra.** Chuyện "lên men" ấy mất **sáu tháng tới một năm**. Nhưng một khi đã gắn kết rồi thì đập bỏ đội chỉ vì một dự án vừa kết thúc là điều ngớ ngẩn — hãy **giữ lấy đội, rồi cứ rót dự án mới vào cho nó**.

## 4. Đội có trước hay dự án có trước; velocity; nỗi lo của chủ dự án

**Chuyện gì đã xảy ra.** Ngân hàng và bảo hiểm cứ cố **lập đội quanh dự án** — một cách làm dại dột, vì cái đội đó chẳng bao giờ gắn kết nổi (người ta chỉ ở đó ngắn hạn, mà lại còn một phần thời gian). Uncle Bob lật ngược lại:

> [!quote] The Clean Coder — Ch.13 (tr. 169)
> "Professional development organizations allocate projects to existing gelled teams, they don't form teams around projects."
>
> *Các tổ chức phát triển chuyên nghiệp thì **rót dự án vào những cái đội đã gắn kết sẵn**, chứ không lập đội quanh dự án.*

Một đội đã gắn kết thì nhận cùng lúc nhiều dự án và tự chia việc được. Quản bằng cách nào? Bằng **velocity** — lượng việc mà đội làm xong trong một khoảng thời gian cố định (điểm/tuần, mà điểm là đơn vị đo *độ phức tạp*). Velocity là một **thước đo thống kê**: tuần này 38 điểm, tuần sau 42, tuần sau nữa 25 — cứ trung bình lại thì dần ổn định. Cấp quản lý có thể đặt mục tiêu: velocity trung bình 50, có ba dự án → chia sức 15/15/20; còn lúc khẩn cấp thì bảo "dồn 100% vào dự án B trong ba tuần". Đội-máy-xay thì không tài nào chuyển ưu tiên nhanh như thế; còn đội gắn kết thì "quay ngoắt trong một nốt nhạc".

**Điều rút ra.** Cái này có một cái giá của nó: **chủ dự án mất đi cảm giác an toàn** — có một đội chuyên trách thì họ *chắc chắn* nắm được nguồn lực; còn đội gắn kết nhận nhiều dự án thì công ty đổi ưu tiên tuỳ hứng, nguồn lực có thể bị rút đi bất ngờ. Uncle Bob thì thẳng thắn *thích* vế sau: công ty không nên bị trói tay bởi cái khó khăn nhân tạo của việc lập-rồi-giải-tán đội; muốn đổi ưu tiên thì phải đổi cho nhanh, còn *chuyện bảo vệ tầm quan trọng của dự án là trách nhiệm của chính chủ dự án*. Chốt chương:

> [!quote] The Clean Coder — Ch.13 (tr. 171)
> "Teams are harder to build than projects."
>
> *Dựng một cái **đội** khó hơn dựng một cái **dự án**.*

Cho nên hãy lập những cái đội bền, để chúng cùng nhau đi từ dự án này sang dự án khác, và giữ chúng lại như một *cỗ máy* chuyên hoàn thành hết dự án này tới dự án nọ.

## 5. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — Uncle Bob đi trước thời đại
> Cái luận điểm trung tâm "**nuôi đội cho bền, rồi rót dự án vào đội** (chứ không lập đội quanh dự án)" tới năm 2026 đã thành **dòng chính**, mà lại còn được đặt tên hẳn hoi: phong trào *"từ dự án sang sản phẩm"* (Mik Kersten, *Project to Product*, 2018), *đội sản phẩm bền vững*, khẩu hiệu *"you build it, you run it"*, và khung *Team Topologies* (Skelton & Pais, 2019). Câu "không có nửa con người" thì khớp với hiểu biết 2026 về **chi phí chuyển ngữ cảnh** (context switching) khi xé lẻ người ra làm nhiều việc một lúc. Ở chỗ này thì Uncle Bob vừa đúng vừa đi trước.
>
> [!warning] Đối chiếu 2026 — velocity: công cụ tốt bị lạm dụng
> Đây mới là chỗ cần cảnh giác nhất. Uncle Bob mô tả velocity như một thước đo thống kê để đội *tự* lập kế hoạch — cái đó đúng. Nhưng cái ví dụ "quản lý đặt mục tiêu 15/15/20" lại chính là thứ mà **2026 cảnh báo dữ dội**: hễ velocity bị biến thành *mục tiêu*, hay thành công cụ để *so sánh giữa các đội*, là nó rơi ngay vào **luật Goodhart** ("một thước đo mà thành mục tiêu thì thôi làm thước đo tốt") — đội sẽ *thổi phồng điểm* lên. Đồng thuận của 2026: velocity là *của đội, cho đội*, chứ không phải một cái KPI để sếp ép hay đem so.
>
> [!warning] Đối chiếu 2026 — quy mô, vai trò, và sự ổn định
> Vài chi tiết mang rõ dấu 2011: đội **~12 người** nay bị coi là hơi lớn — 2026 chuộng "*two-pizza team*", cỡ 5–9 người. Cái cấu trúc **vai trò tách bạch** (analyst / tester / PM riêng ra, tỉ lệ 2:1) cũng đã mờ dần: nay là đội *đa chức năng*, người *hình chữ T*, QA nhúng thẳng trong đội, còn PM thường là *Product Owner*. Cuối cùng, cái ý "đổi ưu tiên tuỳ hứng, quay ngoắt trong một nốt nhạc" thì cần *cân lại*: 2026 cũng nhấn rằng **thrashing** (đổi ưu tiên xoành xoạch) tự nó đã phá năng suất — một đội bền cần *một mức ổn định về tiêu điểm*, chứ không phải bị ném qua ném lại mỗi tuần.

## 6. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Đo "độ máy xay" của bạn.** Tuần này bạn bị xé ra trên bao nhiêu dự án/việc song song? Ước lượng thử xem mất bao nhiêu thời gian vào *chuyển ngữ cảnh*. Có việc nào đang ở dạng "25% một người" không?
> 2. **Đội bạn đã "gel" chưa?** Nó đã ở cùng nhau bao lâu rồi? Sẽ mất những gì nếu nó bị giải tán ngay khi dự án hiện tại kết thúc?
> 3. **Soi lại cách dùng velocity.** Velocity của đội đang được dùng để *đội tự lập kế hoạch*, hay để *sếp đem so sánh và ép*? Nếu là vế sau, đó là dấu hiệu của luật Goodhart.

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **Nhóm bền vs nhóm dựng-theo-việc.** Trong nghề bạn, các nhóm được lập *quanh những con người bền*, hay *quanh từng việc rồi giải tán*? Cái nào tạo ra "phép màu" nhiều hơn?
> 2. **Thước đo hoá thành mục tiêu.** Có chỉ số nào trong công việc bạn từng rất hữu ích, rồi bị biến thành mục tiêu và bị người ta "chơi" cho đẹp con số không? Đó chính là luật Goodhart trong nghề bạn.

## 7. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **"No such thing as half a person"** | Xé lẻ người qua nhiều dự án không tạo ra đội; chi phí chuyển ngữ cảnh cao (tr. 168). |
| **Gelled team (đội gắn kết)** | Đội đã ở cùng đủ lâu để tiên đoán và đỡ cho nhau; "lên men" 6 tháng–1 năm (tr. 168–169). |
| **Projects→teams, không teams→projects** | Rót dự án vào đội bền có sẵn, đừng lập đội quanh dự án (tr. 169). |
| **Velocity** | Lượng việc/đơn vị thời gian (điểm/tuần); thước đo *thống kê của đội, cho đội* (tr. 170). |
| **Luật Goodhart** | (Khung 2026) thước đo thành mục tiêu thì thôi làm thước đo tốt — cảnh báo khi velocity bị ép. |
| **Project to Product / Team Topologies** | (Khung 2026) đặt tên chính thức cho ý "đội sản phẩm bền" của Uncle Bob. |

## 8. Câu hỏi tự kiểm tra

1. Vì sao đội ngân hàng/bảo hiểm bị Uncle Bob gọi là "máy xay sinh tố"? *(tr. 168)*
2. "Không có nửa con người" nghĩa là gì với việc phân bổ nhân sự? *(tr. 168)*
3. Một đội gắn kết mất bao lâu để "lên men", và vì sao không nên giải tán khi dự án kết thúc? *(tr. 169)*
4. "Rót dự án vào đội có sẵn" khác "lập đội quanh dự án" ra sao? *(tr. 169)*
5. Velocity nên dùng cho ai, và 2026 cảnh báo gì khi nó bị biến thành mục tiêu quản lý? *(tr. 170)*
6. Chi tiết nào của chương mang dấu 2011 (quy mô, vai trò) và 2026 chỉnh thế nào?

## Tóm tắt một trang

```
BÀI 13 — ĐỘI VÀ DỰ ÁN: NUÔI ĐỘI GẮN KẾT, RỒI RÓT DỰ ÁN VÀO
────────────────────────────────────────────────────────
MỞ ĐẦU  Ngân hàng/bảo hiểm: dự án nhỏ lắp từ PM/BA/dev/tester
        mỗi người 25–50% → "came out of a Waring blender" (tr.168).

QUY TẮC  "There is no such thing as half a person" (tr. 168).

CA — GELLED TEAM  Đội gắn kết "can work miracles" (tr. 168). ~12
        người, dev:test+analyst ≈ 2:1. Lên men 6 tháng–1 năm →
        đừng giải tán khi dự án hết.

CÓ TRƯỚC?  "allocate projects to existing gelled teams, don't
        form teams around projects" (tr. 169). Quản bằng velocity
        (thống kê 38/42/25 → trung bình). Khẩn: dồn 100% dự án B.

CHỦ DỰ ÁN  Mất cảm giác an toàn; Bob thích công ty đổi ưu tiên
        nhanh. "Teams are harder to build than projects" (tr.171).

2026  "Đội bền, project→product" = GIỮ (Project to Product, Team
      Topologies). Velocity ép/so sánh = luật Goodhart (CẢNH BÁO).
      ~12 người → two-pizza; vai tách → đa chức năng; tránh thrashing.
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.13 **Teams and Projects** (`tr. 167–171`): "Does It Blend?" — đội "máy xay", "no such thing as half a person" (tr. 168); "The Gelled Team" — thành phần, tỉ lệ 2:1, "fermentation", team-vs-project (tr. 168–170); "But How Do You Manage That?" — velocity (tr. 170); "The Project Owner Dilemma" (tr. 170–171); Conclusion (tr. 171). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Bối cảnh 2026 (ngoài sách): *Project to Product* (Mik Kersten), *Team Topologies* (Skelton & Pais), two-pizza teams, luật Goodhart, chi phí context switching.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 — Ước lượng](bai_10_uoc_luong.md) · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 ← bạn đang ở đây] · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
