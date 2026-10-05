# Release It! — Hồ sơ ca sập production

Khoá tự học theo lối **case-study**, dựng từ chính văn bản gốc — không viết theo trí nhớ.

**Sách gốc:** *Release It! Design and Deploy Production-Ready Software*, tác giả **Michael T. Nygard**, Pragmatic Bookshelf, 2007 (bản tiếng Anh, PDF 350 trang nằm trong `tai_lieu/`). Khoá dựng trên **bản 1 (2007)**. **Bản 2 ra tháng 1/2018** ([trang nhà xuất bản](https://pragprog.com/titles/mnee2/release-it-second-edition/), đã xác nhận trong Bài 0); theo nhà xuất bản, bản này bổ sung DevOps, microservices, kiến trúc cloud-native và chaos engineering. Sách không dạy viết tính năng. Nó bàn về khoảng cách giữa **"feature complete"** (đích của dự án) và **"production ready"** (điểm xuất phát của hệ thống): làm sao để phần mềm sống sót, chịu được tải thật, hợp với trung tâm dữ liệu, và cho người vận hành nhìn thấy, thay đổi được nó. Sách hữu ích ở chỗ mỗi phần dựa trên những sự cố thật Nygard tận mắt thấy. Ông đổi tên các bên nhưng giữ nguyên ngành, trình tự sự kiện, kiểu hỏng, đường lan lỗi và chi phí (tr. 13).

> [!success] Đã hoàn tất **5/5 bài** (Bài 0 + 1–4) trong `bai_hoc/`.
> Bài 0 mổ Preface và Ch.1; Bài 1–4 mỗi bài mổ một phần (Part) của sách. Trục xuyên suốt: *case mở màn → antipattern/pattern → **Đối chiếu 2026** → Áp dụng hai tầng (thiết kế/code · on-call/postmortem)*.
> Bảng [Bản đồ khoá học](#bản-đồ-khoá-học) bên dưới trỏ tới từng bài.

---

## Vì sao là "case-study"?

Theo Preface, mỗi phần của sách mở bằng một nghiên cứu tình huống (tr. 12). Khoá giữ cách mở đó và kể mỗi ca như một hồ sơ sự cố:

| Phần | Case mở màn | Điều nó dạy |
| --- | --- | --- |
| I — Ổn định | Một hãng bay chuyển đổi cơ sở dữ liệu lúc nửa đêm. Khoảng 2:30 sáng, mọi ki-ốt check-in trên cả nước chuyển đỏ. Thủ phạm là một `SQLException` không được bắt ở `Statement.close()`, làm rò kết nối cho tới khi pool cạn (tr. 21–34). | "Bugs will happen. They cannot be eliminated, so they must be survived instead." (tr. 34) |
| II — Công suất | Ngày ra mắt cửa hàng trực tuyến của một nhà bán lẻ: lúc 9:30 sáng có 250.000 session, rồi site sập. Session phình vì bot, spider và scraper, thứ nhiễu mà kịch bản kiểm thử tải lịch sự không tạo ra (tr. 147–157). | Đội xây mọi thứ "to pass testing, not to run in production" (tr. 149). |
| III — Thiết kế tổng quát | **Không có case.** Trang 218 chỉ có tên phần. Bài 3 mở bằng đoạn đầu của Ch.11 và Ch.15, còn phần thân dùng những giai thoại ngắn Nygard rải trong từng chương (máy Windows bị để đăng nhập bằng Administrator nhiều tuần, firewall có ở production mà QA không có…). | Không xử lý lúc phát triển thì sẽ phải xử lý ở production "time and time again" (tr. 249). |
| IV — Vận hành | Black Friday: mọi DRP đỏ, mất khoảng một triệu đô mỗi giờ. 3.000 luồng chờ một pool không có timeout, dồn xuống một server lên lịch giao hàng chỉ chịu được 25 request. Nygard cứu trang bằng cách đặt `max` của pool về 0 khi hệ thống đang chạy: xong trong chưa tới năm phút, trong khi sửa cấu hình rồi restart sẽ mất hơn sáu giờ (tr. 252–263). | Nhìn thấy và điều khiển được bên trong hệ thống là khác biệt giữa một cuối tuần khó khăn nhưng thành công và một thảm hoạ (tr. 254). |

Sách viết năm 2007, trước thời cloud, container, Kubernetes, SRE và observability. Tên ví dụ (EJB, RMI, ATG, SiteScope, Slashdot) đã cũ, nhưng cơ chế hỏng thì vẫn còn. Vì vậy mỗi bài có một mục **`[!warning] Đối chiếu 2026`**, tách ra ba loại: *phần còn sống*, *phần cần chỉnh* và *phần đã lỗi thời*.

---

## Cách đọc & quy ước

| Ký hiệu | Nghĩa |
| --- | --- |
| `Ch. 4` | trích theo **chương** của sách |
| `tr. 148` | **số trang in = số trang PDF** (offset 0), tra thẳng trong tệp ở `tai_lieu/` |
| **Mục Mở đầu** | mỗi bài mở bằng case của phần đó (story-first); Bài 3 thì không, vì sách không có case |
| antipattern / pattern | = **phản mẫu / mẫu**. Bài 1 giữ tên tiếng Anh như sách (Circuit Breaker, Blocked Threads…); Bài 2 dịch tên, kèm tên gốc trong bảng phân loại |
| `[!quote]` | câu chốt để **nguyên văn tiếng Anh** (nguồn là tiếng Anh), kèm bản dịch gọn bên dưới |
| `[!warning]` **Đối chiếu 2026** | tách phần còn sống, phần cần chỉnh và phần đã lỗi thời năm 2026 |
| `[!question]` **Áp dụng vào việc của bạn** | bài tự thực hành *hai tầng*: một khi thiết kế và viết code, một khi trực on-call và viết postmortem |
| `[!note]` **Mở rộng** | kiến thức nền sách lướt qua, hoặc phép tính lại của khoá |

Người đọc được hình dung là **dev kiêm vận hành**. Khoá **không có code chạy được**: sách dạy cơ chế hỏng và thiết kế, nên bài học dùng sơ đồ, bảng và phép tính.

Định dạng chuẩn kho: **Obsidian callout**, tiêu đề `##` không kèm emoji. Mở bằng Obsidian hoặc VS Code + Markdown Preview.

---

## Bản đồ khoá học

| Bài | Phần sách (Ch., tr.) | Case mở màn | Ý chính |
| --- | --- | --- | --- |
| [Bài 0 — Nhập môn](bai_hoc/bai_00_nhap_mon.md) | Preface + Ch.1, tr. 10–19 | cảnh "Xong rồi." Thật không? | feature complete chưa phải production ready; ba ngộ nhận; design for production; quyết định kiến trúc cũng là quyết định tài chính |
| [Bài 1 — Ổn định](bai_hoc/bai_01_on_dinh.md) | Part I, Ch.2–6, tr. 20–145 | hãng bay nằm đất vì một `SQLException` | vết nứt lan qua integration point; 11 antipattern (Chain Reactions, Blocked Threads, Slow Responses…) và 8 pattern (Timeouts, Circuit Breaker, Bulkheads, Fail Fast…) |
| [Bài 2 — Công suất](bai_hoc/bai_02_cong_suat.md) | Part II, Ch.7–10, tr. 146–217 | "Trampled by Your Own Customers": sập lúc 9:30 với 250.000 session | chỉ một ràng buộc quyết định công suất; hệ số nhân; 10 phản mẫu và 4 mẫu (gộp kết nối, cache, tính trước, tinh chỉnh GC) |
| [Bài 3 — Thiết kế tổng quát](bai_hoc/bai_03_thiet_ke_tong_quat.md) | Part III, Ch.11–15, tr. 218–250 | *không có case*, mở bằng đoạn đầu Ch.11 và Ch.15 | multihoming, IP ảo, quyền tối thiểu, mật khẩu trong file; availability là bài toán tiền; QA lệch topology; cấu hình là giao diện người dùng |
| [Bài 4 — Vận hành](bai_hoc/bai_04_van_hanh.md) | Part IV, Ch.16–18, tr. 251–335 | Black Friday: pool `max = 0`, năm phút thay vì sáu giờ | minh bạch (bốn góc nhìn, log, giám sát, OpsDB); thích nghi (release không đau, mở rộng → rollout → dọn dẹp); khép lại cả khoá |

Nên đọc theo thứ tự. Nygard coi **ổn định là điều kiện tiên quyết**: hệ thống ngày nào cũng sập thì chẳng ai lo tới tương lai xa (tr. 12). Bài 1 dài nhất khoá, nên đọc theo ba chặng như gợi ý trong khối `[!info]` của bài.

---

## Những ca "gắt" nhất — nơi 2026 cãi lại Nygard

Nếu bạn chỉ có thời gian đọc vài mục, đây là những chỗ mục *Đối chiếu 2026* đẩy Nygard đi xa nhất:

| Bài | Nygard nói (2007) | 2026 đối chiếu |
| --- | --- | --- |
| [Bài 0](bai_hoc/bai_00_nhap_mon.md) | downtime tốn trực tiếp hơn 100.000 đô mỗi giờ (tr. 17); kể áp lực chạy 24/7 như xu thế phải theo | ITIC 2024: với hơn 90% doanh nghiệp vừa và lớn, một giờ downtime tốn trên 300.000 đô. Google SRE: "100% có lẽ không bao giờ là mục tiêu tin cậy đúng" |
| [Bài 1](bai_hoc/bai_01_on_dinh.md) | Circuit Breaker tự viết, ba trạng thái (Hình 5.1) | Hystrix đã vào chế độ bảo trì, Netflix khuyên dùng **resilience4j**; cơ chế còn xuống tầng hạ tầng với outlier detection của Envoy/Istio ở sidecar |
| [Bài 1](bai_hoc/bai_01_on_dinh.md) | Test Harness: đối thủ chơi xấu, dựng *ngoài* production | **chaos engineering** chủ động làm thí nghiệm *trong* production (Principles of Chaos, Chaos Monkey) |
| [Bài 2](bai_hoc/bai_02_cong_suat.md) | định cỡ pool để không có tranh chấp ở đỉnh, nếu được thì bằng số luồng request (tr. 179) | **HikariCP ngược hướng**: "a small pool, saturated with threads waiting for connections". Oracle giảm pool từ 2048 xuống 96, thời gian đáp ứng từ ~100 ms xuống ~2 ms |
| [Bài 2](bai_hoc/bai_02_cong_suat.md) | Overstaying Sessions: session nằm lì trong RAM server | session thành token (**JWT**), nhưng OWASP cảnh báo cần cách vô hiệu hoá, và denylist khiến nó "không còn hoàn toàn stateless"; trạng thái chỉ dời chỗ |
| [Bài 3](bai_hoc/bai_03_thiet_ke_tong_quat.md) | bảo mật gói trong **ba trang** (tr. 226–228; chính Nygard nói bảo mật đầy đủ vượt xa phạm vi sách, tr. 226); gắn SSH riêng vào card quản trị là lớp bảo vệ quan trọng (tr. 221) | **OWASP Top 10:2025** (có hạng mục mới A03 Software Supply Chain Failures, cùng SBOM); **zero trust** (NIST SP 800-207) không cho niềm tin ngầm định chỉ dựa trên vị trí mạng |
| [Bài 4](bai_hoc/bai_04_van_hanh.md) | Transparency: "bộ xương ngoài", thiết kế theo chuẩn SNMP, CIM, JMX (tr. 275, 289); ID giao dịch (tr. 283); OpsDB tự dựng | **OpenTelemetry** (traces, metrics, logs; không phải backend) thay chỗ các chuẩn cũ; W3C Trace Context chuẩn hoá `traceparent`; OpsDB tự dựng nhường chỗ cho backend observability |

---

## Những chỗ chính sách tự mâu thuẫn

Đọc kỹ văn bản gốc, khoá phát hiện vài chỗ sách lệch số với chính nó. Mỗi chỗ đều được nêu trong bài dưới dạng *ghi chú của khoá* hoặc `[!note] Mở rộng`. Khoá chỉ nêu ra, không sửa sách:

- **Mốc giờ ca hãng bay** ([Bài 1](bai_hoc/bai_01_on_dinh.md)): tr. 25 ghi sự cố "hơi hơn ba giờ, từ 11:30 tối đến 2:30 sáng", cũng trang đó nói failover diễn ra "ba giờ trước sự cố"; tr. 24 cho ki-ốt đỏ lúc 2:30 sáng; tr. 27 gọi 10:30 sáng là "tám giờ sau khi sự cố bắt đầu". Các mốc không khớp nhau hoàn toàn.
- **75 và 450 luồng** ([Bài 1](bai_hoc/bai_01_on_dinh.md)): tr. 99 nói "ba nghìn luồng gọi vào bảy mươi lăm luồng" (câu giả định, có thể là ví dụ khác), trong khi Hình 4.13 ghi 450 luồng. Cùng trang, thân bài bảo stress test "nhân đôi", còn khung Remember This bảo "gấp mười lần mức cao nhất từng có".
- **250 hay 500 mili giây mở kết nối** ([Bài 2](bai_hoc/bai_02_cong_suat.md)): Ch.9 nói mở kết nối database tốn "up to 250 milliseconds" (tr. 176), Ch.10 nói "400 tới 500 ms" (tr. 206), tổng kết 10.5 lại ghi pool bớt "up to 500 milliseconds" (tr. 217). Bậc độ lớn vẫn là hàng trăm mili giây.
- **"Thirteen times"** ([Bài 2](bai_hoc/bai_02_cong_suat.md)): tr. 173 nói phục vụ được gấp mười ba lần số người dùng dial-up (38–39 Kbps) so với cable modem (6 Mbps); tính lại thì 6.000 / 39 ≈ 154 lần.
- **"Net Savings" chưa trừ chi phí** ([Bài 3](bai_hoc/bai_03_thiet_ke_tong_quat.md)): con số $1.289.520 ở bảng tr. 230 thực ra là tổn thất tránh được trong 5 năm. Trừ chi phí $98.700 thì lời ròng là $1.190.820. Kết luận không đổi.
- **100 hay 75 DRP** ([Bài 4](bai_hoc/bai_04_van_hanh.md)): tr. 259 và 261 ghi con số 100 (DRP / server), còn các hình 16.1–16.3 ghi 20 host, 75 DRP; sách không giải thích.

---

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software*, Pragmatic Bookshelf, 2007 — `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`.
- Pragmatic Bookshelf, *Release It! Second Edition* (1/2018): https://pragprog.com/titles/mnee2/release-it-second-edition/
- Bối cảnh 2026 trong các mục *Đối chiếu 2026* được dẫn từ nguồn ngoài sách, ghi rõ ở mục **Nguồn** của từng bài: Google *Site Reliability Engineering*, DORA, resilience4j, Envoy/Istio, Principles of Chaos, HikariCP, Kubernetes, OWASP Top 10:2025, NIST SP 800-207, OpenTelemetry, W3C Trace Context, v.v.
- Quy ước trích: `tr. X` = số trang in = số trang PDF.
