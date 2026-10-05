# Bài 3 — Thiết kế tổng quát: phần mềm sống trong trung tâm dữ liệu, không phải trên laptop

> [!info] Về bài này
> Dựng từ **Part III — General Design Issues** của *Release It!* (Michael T. Nygard, 2007, `tai_lieu/`, `tr. 218–250`): **Ch.11 Networking**, **Ch.12 Security**, **Ch.13 Availability**, **Ch.14 Administration**, **Ch.15 Design Summary**.
> Trích theo `Ch. N` và `tr. X` (**số trang in = số trang PDF**). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> **Lưu ý:** khác ba phần kia, Part III **không mở bằng nghiên cứu tình huống**. Trang 218 chỉ có tên phần. Vì vậy mục 1 mở bằng chính đoạn mở đầu của Ch.11 và Ch.15; các mẩu chuyện thật trong bài là những giai thoại ngắn Nygard rải trong từng chương, không có ca nào đủ dài để làm hồ sơ sự cố. Khoá không dựng thêm case.
> *Cần đọc trước:* [Bài 2 — Công suất](bai_02_cong_suat.md). Bài này nhắc lại vài pattern (Circuit Breaker, Fail Fast, Timeouts) và antipattern SLA Inversion của [Bài 1 — Ổn định](bai_01_on_dinh.md).

## Mục lục

1. [Mở đầu: cỗ máy trên bàn dev và cỗ máy trong trung tâm dữ liệu](#1-mở-đầu-cỗ-máy-trên-bàn-dev-và-cỗ-máy-trong-trung-tâm-dữ-liệu)
2. [Một máy chủ, bốn cái tên: multihoming](#2-một-máy-chủ-bốn-cái-tên-multihoming)
3. [Định tuyến và địa chỉ IP ảo](#3-định-tuyến-và-địa-chỉ-ip-ảo)
4. [Quyền tối thiểu: đừng chạy bằng root](#4-quyền-tối-thiểu-đừng-chạy-bằng-root)
5. [Mật khẩu nằm trong file: gót chân Achilles](#5-mật-khẩu-nằm-trong-file-gót-chân-achilles)
6. [Bao nhiêu số chín là đủ: availability là bài toán tiền](#6-bao-nhiêu-số-chín-là-đủ-availability-là-bài-toán-tiền)
7. [Viết SLA sao cho khỏi cãi nhau](#7-viết-sla-sao-cho-khỏi-cãi-nhau)
8. [Cân bằng tải: ba cách chia việc](#8-cân-bằng-tải-ba-cách-chia-việc)
9. [Cluster: cái nạng cho ứng dụng không tự đứng được](#9-cluster-cái-nạng-cho-ứng-dụng-không-tự-đứng-được)
10. [QA có khớp production không](#10-qa-có-khớp-production-không)
11. [File cấu hình là giao diện người dùng](#11-file-cấu-hình-là-giao-diện-người-dùng)
12. [Khởi động, tắt máy và giao diện quản trị](#12-khởi-động-tắt-máy-và-giao-diện-quản-trị)
13. [Tóm tắt thiết kế của Nygard](#13-tóm-tắt-thiết-kế-của-nygard)
14. [Đối chiếu 2026](#14-đối-chiếu-2026)
15. [Áp dụng vào việc của bạn](#15-áp-dụng-vào-việc-của-bạn)
16. [Từ điển thuật ngữ](#16-từ-điển-thuật-ngữ)
17. [Câu hỏi tự kiểm tra](#17-câu-hỏi-tự-kiểm-tra)
18. [Tóm tắt một trang](#tóm-tắt-một-trang)
19. [Nguồn](#nguồn)

---

## 1. Mở đầu: cỗ máy trên bàn dev và cỗ máy trong trung tâm dữ liệu

Trên laptop, ứng dụng của bạn có một card mạng, một cái tên, chạy bằng tài khoản của chính bạn, cấu hình nằm ngay cạnh code, và khi khởi động lỗi thì bạn thấy ngay trên màn hình. Không điều nào trong số đó còn đúng khi nó chuyển vào trung tâm dữ liệu. Nygard mở Part III bằng đúng khoảng cách ấy:

> [!quote] Release It! — Ch.11 (tr. 219)
> "Networking in the data center goes far beyond the application-level sockets API. Data center network designs favor redundancy, security, and flexibility far more than networks to the desktop."
>
> *Mạng trong trung tâm dữ liệu vượt xa API socket ở tầng ứng dụng. Thiết kế mạng trung tâm dữ liệu coi trọng dư thừa, bảo mật và linh hoạt hơn hẳn mạng tới máy để bàn.*

Ông nói thêm rằng ứng dụng phải làm thêm một ít việc mới cư xử đúng trong môi trường đó (tr. 219). Bốn chương sau đó đi qua bốn mảng: mạng, bảo mật, availability (độ sẵn sàng), quản trị. Chúng không có một sự cố lớn làm trục như Part I, mà là một chuỗi chuyện nhỏ: máy Windows bị để đăng nhập bằng Administrator nhiều tuần (tr. 226), đội vận hành nén cả thư mục cài đặt gửi về cho dev phân tích, lý do để mật khẩu không bao giờ nằm trong đó (tr. 227), vài giờ downtime vì production có firewall mà QA không có (tr. 243), quy trình tắt máy "sạch" phải click trên sáu server (tr. 248).

Chương tổng kết (Ch.15) nói thẳng lựa chọn của bạn:

> [!quote] Release It! — Ch.15 (tr. 249)
> "There’s good and bad news here; you can choose not to deal with these issues during development. If so, you will deal with them in production...time and time again."
>
> *Có tin tốt và tin xấu: bạn có thể chọn không xử lý những vấn đề này lúc phát triển. Nếu vậy, bạn sẽ xử lý chúng ở production... hết lần này tới lần khác.*

Theo ông, xử lý chúng lúc phát triển không nhất thiết tốn nhiều thời gian hay công sức, và cái giá đó nhỏ hơn nhiều so với chi phí dài hạn của việc làm ngơ (tr. 249).

## 2. Một máy chủ, bốn cái tên: multihoming

Bạn từng thấy mạng chậm rì mỗi khi backup chạy chưa? Backup luôn chạy hết ga nên có thể làm nghẹt bất kỳ mạng nào; mạng nhanh hơn chỉ khiến backup xong sớm hơn (tới một mức nào đó) (tr. 219). Đó là một trong các lý do máy trong trung tâm dữ liệu gắn nhiều mạng.

> [!quote] Release It! — Ch.11 (tr. 219)
> "A server with more than one IP address is a multihomed server; it exists on several networks simultaneously."
>
> *Một máy chủ có nhiều hơn một địa chỉ IP là máy chủ multihomed; nó tồn tại đồng thời trên nhiều mạng.*

Theo Nygard, gần như mọi server trong trung tâm dữ liệu đều multihomed, và đó là khác biệt nổi bật nhất so với máy dev hay QA (tr. 219). Hình 11.1 vẽ một server bốn card (tr. 220):

```
   Switch 1 ──nic0──┐
   Switch 2 ──nic1──┤  production ×2: phục vụ request, hai switch khác nhau (HA)
                [ Server ]
   Backup   ──nic2──┤  mạng backup: tách lưu lượng lớn, dồn dập
   Admin    ──nic3──┘  mạng quản trị: SSH, giám sát
```

Hai card production có thể cân bằng tải hoặc làm cặp dự phòng; hai IP nghĩa là có lẽ hai bản ghi DNS, tức máy này **có nhiều hơn một cái tên** (tr. 220). Biến thể **bonding** cho hai card dùng chung một IP; nối hai switch mà quên cấu hình switch thì sinh vòng lặp định tuyến, và "bạn sẽ rất nổi tiếng, nhưng không theo nghĩa tốt" (tr. 221). Mạng backup (switch hay VLAN riêng) giúp người dùng ứng dụng khác khỏi vạ lây khi server này backup. Mạng quản trị là lớp bảo vệ quan trọng: SSH chỉ gắn vào card quản trị nên từ mạng production không với tới, có ích khi firewall bị xuyên thủng (tr. 221).

Chỗ đụng tới code: mặc định, ứng dụng nghe socket nhận kết nối từ **mọi** card. Với `ServerSocket` của Java 5, ba trong bốn constructor gắn vào mọi interface (tr. 221).

> [!quote] Release It! — Ch.11 (tr. 221)
> "Without the address, ServerSocket will bind to all interfaces, which would allow connections over the backup or administration networks to the production server."
>
> *Không có địa chỉ, ServerSocket sẽ gắn vào mọi interface, cho phép kết nối qua mạng backup hay mạng quản trị vào server production.*

Và ngược lại, chức năng quản trị bị mở ra trên mạng production. `InetAddress.getLocalHost()` chạy tốt ở dev, nhưng trên máy multihomed chỉ trả IP gắn với hostname nội bộ, có thể là card bất kỳ. Kết luận: ứng dụng phải có **thuộc tính cấu hình** chỉ định interface để bind (tr. 221–222).

## 3. Định tuyến và địa chỉ IP ảo

**Định tuyến.** App server thường có card front-end nối VLAN web server và card back-end nối VLAN database; phải chỉ rõ card nào đi tới đích nào (tr. 222). Khó là dịch vụ bên thứ ba ở xa, như "spam cannon" (nhà gửi email hàng loạt): dữ liệu có lẽ nên đi qua card back-end và VPN thay vì Internet công cộng. Làm sai thì giảm availability, tệ hơn là lộ dữ liệu khách hàng. Nygard khuyên ghi mỗi kết nối ra xa vào một bảng tính: tên đích, địa chỉ, tuyến mong muốn, vì rồi sẽ có ngày ai đó cần nó để viết luật firewall (tr. 222).

**IP ảo.** Có những ứng dụng mỗi lúc chỉ chạy được trên một server (tr. 223). Muốn chúng có high availability, người ta dùng **cluster server** (HP ServiceGuard, Veritas Cluster Server, Microsoft Cluster Server) để bảo đảm một "package" chạy đúng một lần trong cluster. Khi máy chính ngừng gửi **heartbeat**, máy dự phòng khởi động ứng dụng, mount filesystem và nhận địa chỉ IP ảo (tr. 223–224).

> [!quote] Release It! — Ch.11 (tr. 224)
> "A virtual IP address is just an IP address that can be moved from one NIC to another as needed."
>
> *Địa chỉ IP ảo chỉ là một địa chỉ IP có thể chuyển từ card mạng này sang card mạng khác khi cần.*

Khi chuyển, hệ điều hành gắn IP với địa chỉ MAC mới và quảng bá qua ARP; client chỉ kết nối vào tên DNS của IP ảo (tr. 224). Nygard ghi chú từ này còn một nghĩa nữa: địa chỉ dịch vụ trên load balancer (tr. 224).

Cái bẫy là trạng thái trong bộ nhớ: IP chuyển được, trạng thái chưa lưu thì mất; với database là giao dịch chưa commit. Driver của Oracle tự chạy lại truy vấn bị huỷ, nhưng update, insert, stored procedure thì không, nên ứng dụng phải sẵn sàng nhận `SQLException` khi failover (tr. 224). Tổng quát: gọi dịch vụ qua IP ảo thì gói TCP sau có thể không tới cùng interface với gói trước, sinh `IOException` ở chỗ lạ; nên thử lại với node mới, trong giới hạn an toàn của Circuit Breaker (tr. 225, xem [Bài 1 — Ổn định](bai_01_on_dinh.md)). Thử lại ở đây phải có giới hạn: Bài 1, mục 14, dẫn cảnh báo của Nygard về retry ngay lập tức (tr. 113).

## 4. Quyền tối thiểu: đừng chạy bằng root

Nygard từng thấy server Windows bị để đăng nhập bằng Administrator nhiều tuần liền, có remote desktop, chỉ vì một phần mềm đòi thế; phần mềm đó còn không chạy được như NT service. "Đó không phải cái tôi gọi là sẵn sàng cho trung tâm dữ liệu!" (tr. 226).

Ông tự khoanh phạm vi: bảo mật đầy đủ vượt xa tầm cuốn sách; chương này chỉ giữ những chủ đề ở giao điểm của kiến trúc, vận hành và bảo mật (tr. 226). **Quyền tối thiểu** đòi mỗi tiến trình chỉ có mức quyền thấp nhất đủ để làm việc; với phần mềm ứng dụng, điều đó không bao giờ bao gồm root hay Administrator (tr. 226).

> [!quote] Release It! — Ch.12 (tr. 226)
> "Software that requires execution as root is automatically a target for crackers."
>
> *Phần mềm đòi chạy bằng root tự động trở thành mục tiêu của kẻ tấn công.*

Kẻ tấn công đã có root thì cách duy nhất chắc chắn là format và cài lại, có khi cả cluster. Mỗi ứng dụng lớn nên có user riêng: "apache" không đụng được "websphere" (tr. 226). Lý do duy nhất một ứng dụng UNIX có thể cần root là mở cổng dưới 1024. Web server đứng sau load balancer thì dùng cổng nào cũng được; còn nếu buộc nghe cổng 80, sách chỉ ra cách Apache làm: **privilege separation**, khởi động bằng root, mở socket xong thì tự hạ quyền xuống user đã cấu hình, một chiều, không lấy lại được (tr. 227).

## 5. Mật khẩu nằm trong file: gót chân Achilles

> [!quote] Release It! — Ch.12 (tr. 227)
> "Passwords are the Achilles heel of application security."
>
> *Mật khẩu là gót chân Achilles của bảo mật ứng dụng.*

Không ai gõ tay mật khẩu mỗi lần app server khởi động, nên mật khẩu phải nằm trong file; mà đã nằm trong file văn bản là dễ tổn thương. Mật khẩu vào được database khách hàng đáng hàng nghìn đô với kẻ tấn công (tr. 227). Mức tối thiểu Nygard đòi (tr. 227–228):

- **Tách mật khẩu production khỏi mọi file cấu hình khác**, nhất là khỏi thư mục cài đặt. Lý do là một giai thoại: ông từng thấy đội vận hành nén cả thư mục cài đặt gửi về cho dev phân tích (tr. 227).
- **Chỉ chủ sở hữu đọc được**, chủ là user của ứng dụng; nếu có privilege separation thì đọc file trước khi hạ quyền, và file có thể thuộc root (tr. 227).
- **Coi chừng bộ nhớ.** Core file của UNIX là dump bộ nhớ, có mật khẩu; màn hình xanh của Windows cũng kèm dump. Tốt nhất là tắt core dump trên ứng dụng production (tr. 228).

**Password vaulting** giữ mật khẩu trong file mã hoá, quy về bài toán bảo vệ một khoá; theo Nygard nó giúp nhưng tự nó chưa đủ, nên dùng thêm Tripwire để canh quyền trên những file sống còn đó (tr. 228).

## 6. Bao nhiêu số chín là đủ: availability là bài toán tiền

Hỏi một đám trẻ muốn bao nhiêu kem, câu trả lời thường là "tất cả". Chúng không nghĩ tới tiền mua kem, sức khoẻ, cân nặng, hay cảm giác nôn nao trong bụng (tr. 229). Nygard mở Ch.13 bằng cảnh đó:

> [!quote] Release It! — Ch.13 (tr. 229)
> "Divorcing a “want” from its cost always leads to unrealistic desires."
>
> *Tách một mong muốn khỏi cái giá của nó luôn dẫn tới những đòi hỏi phi thực tế.*

Hỏi người tài trợ "hệ thống cần sẵn sàng tới mức nào?", theo ông có lẽ bạn nhận một trong hai câu: người ít kinh nghiệm nói "100%", người hiểu biết hơn nói "năm số chín" vì nghe ngầu và kỹ thuật (tr. 229). Cách đặt vấn đề đúng là tài chính: **chi phí thật so với tổn thất tránh được** (tr. 229). Ví dụ của Nygard:

| | 98% | 99,99% |
| --- | --- | --- |
| Phút ngừng mỗi tháng | 864 | 4 |
| Tiền mất mỗi tháng (giả định $1.500/giờ lúc cao điểm) | $21.600 | $108 |
| Chi phí thêm (vòng đời 5 năm) | $0 | $98.700 |
| Nygard ghi "Net Savings" | $0 | $1.289.520 |

(Bảng ở tr. 230; phép tính ở tr. 229–230.) Ông nói $1.500/giờ là giờ cao điểm, thời điểm tệ nhất để ngừng, nên đây là tổn thất trường hợp xấu nhất (tr. 229). Rồi ông trả lời câu hỏi "vậy có nên xây 99,99% không":

> [!quote] Release It! — Ch.13 (tr. 230)
> "Each “9” of availability increases the implementation cost by about a factor of ten and the operational cost per year by about a factor of two."
>
> *Mỗi "số 9" availability làm chi phí xây dựng tăng khoảng mười lần và chi phí vận hành mỗi năm tăng khoảng hai lần.*

Trong ví dụ này, chi $98.700 để tiết kiệm $1.289.520 có vẻ là lựa chọn tài chính hợp lý (tr. 230).

> [!note] Mở rộng — khoá tính lại bảng của Nygard
> Phần này của khoá, không có trong sách.
> - 864 phút = 2% của một tháng 30 ngày (43.200 phút). 864 phút = 14,4 giờ × $1.500 = **$21.600**. Khớp.
> - 0,01% của 43.200 phút = 4,32 phút; sách làm tròn thành 4. 4,32 phút = 0,072 giờ × $1.500 = **$108**. Khớp.
> - Chênh mỗi tháng $21.492 × 60 tháng (5 năm) = **$1.289.520**. Tức là con số sách ghi "Net Savings" thực ra là **tổn thất tránh được, chưa trừ chi phí**. Trừ $98.700 thì phần lời ròng là **$1.190.820**. Kết luận không đổi, nhưng nên biết để khỏi chép nhầm nhãn.
> - Giả định "mọi phút ngừng đều rơi vào giờ cao điểm" làm phóng to tổn thất. Nếu một giờ trung bình chỉ bằng một phần ba giờ cao điểm, lợi ích còn khoảng $430.000, vẫn gấp hơn bốn lần chi phí.

Bài 0 đã gặp phép tính tương tự ở Ch.1 (98% so với 99,99%, với $100.000/giờ). Ở đây Nygard thêm vế còn lại của cán cân: **mỗi số chín cũng có giá**, và ông gọi nó ở Ch.15 là một phép đánh đổi "chi phí/chi phí" (tr. 249).

## 7. Viết SLA sao cho khỏi cãi nhau

Công thức chắc chắn gây xung đột, theo Nygard: lấy một từ có nhiều định nghĩa mơ hồ, bắt mọi người thoả thuận về nó, gắn thật nhiều tiền vào, rồi xem họ cãi nhau một hai năm sau (tr. 230). SLA giống hợp đồng bảo hiểm y tế: chẳng ai đọc kỹ cho tới khi có chuyện, và lúc đó đã muộn (tr. 230).

> [!quote] Release It! — Ch.13 (tr. 230)
> "It is not enough to write down, “The system shall be available 99.9% of the time” on a piece of paper. Vagueness lurks behind every word of that sentence."
>
> *Viết lên giấy "Hệ thống sẽ available 99,9% thời gian" là không đủ. Sự mơ hồ nấp sau từng chữ của câu đó.*

**"Hệ thống" là gì?** Nó gọi sang hệ thống khác trong và ngoài doanh nghiệp; bạn nhận trách nhiệm cho tất cả à? "Tôi thì không!" Có Circuit Breaker thì cả hệ thống vẫn chạy trong khi vài tính năng tắt. Nên định nghĩa SLA theo **từng tính năng** (tr. 230–231). Ví dụ chuỗi khách sạn: đặt phòng và đặt sự kiện sinh doanh thu nên gắn SLA cao nhất; câu lạc bộ khách hàng thân thiết thường do bên thứ ba lo nên SLA tốt nhất chỉ là chuyển tiếp SLA của nhà cung cấp (tr. 231). Đây là phản mẫu SLA Inversion ở Bài 1:

> [!quote] Release It! — Ch.13 (tr. 231)
> "you cannot offer a better SLA than the worst of the external dependencies involved in a feature."
>
> *bạn không thể hứa một SLA tốt hơn phụ thuộc bên ngoài tệ nhất mà tính năng đó dùng.*

**"Available" là gì?** Một người click chuột kiểm? ("Mong là không.") Người dùng báo qua help desk? ("Càng mong là không!") Tốt nhất là máy chạy **giao dịch tổng hợp (synthetic transaction)**: giao dịch giả lập người dùng, có dấu nhận biết như user ID riêng để khỏi bẩn dữ liệu production (tr. 231); đúng lời khuyên giám sát từ bên ngoài ở [Bài 1 — Ổn định](bai_01_on_dinh.md), mục 7 (tr. 82). Trả lời sau hai mươi bảy phút rưỡi thì phần lớn người dùng sẽ không coi là available; trả lời trong 50 mili giây mà toàn lỗi cũng vậy; còn loại chập chờn "như chiếc xe ở tiệm sửa", cứ lúc kiểm là ổn (tr. 231). Định nghĩa tốt phải chốt: chạy bao lâu một lần, từ bao nhiêu nơi; thời gian trả lời tối đa cho từng bước; mã hay mẫu văn bản nào là thành công, thất bại; dữ liệu ghi ở đâu; công thức tính phần trăm theo thời gian hay theo số mẫu (tr. 231–232). SLA cũng phải nói rõ thiết bị nào giám sát tính năng và thiết bị đó báo sự cố ra sao (tr. 231). Khi cãi nhau thật, giấy chỉ là khiên mỏng, nhưng nó giúp dồn chú ý vào dữ liệu thay vì chuyện cá nhân (tr. 232). Ch.15 thêm: viết điều khoản loại trừ cho mất availability do hệ thống bên ngoài (tr. 250).

## 8. Cân bằng tải: ba cách chia việc

Hệ thống scale ngang đạt cả availability lẫn khả năng mở rộng nhờ **số đông**: thêm máy vừa tăng công suất vừa tăng sức chịu các cú sốc ngắn (impulse); máy nhỏ rẻ hơn và cho phép tăng công suất từng chút (tr. 232). Scale ngang kéo theo cân bằng tải, tức phân phối request trên một nhóm server để phục vụ đúng mọi request trong thời gian ngắn nhất có thể (tr. 232). Nygard so ba kỹ thuật.

**DNS round-robin** là cách cũ nhất: gắn nhiều IP vào một tên dịch vụ, mỗi client nhận một IP (tr. 232). Nó chia được việc nhưng kém ở những tiêu chí khác (tr. 233): mọi server phải có địa chỉ front-end mà client với tới được, "thời nay thế là mời tấn công"; quyền kiểm soát nằm quá nhiều ở client; DNS không biết server nào đã chết nên vẫn phát IP của server "đã thành than"; chia đều kết nối ban đầu chứ không chia đều tải. Và một câu mà năm 2026 vẫn còn làm người ta đau đầu (xem mục 14):

> [!quote] Release It! — Ch.13 (tr. 233)
> "Anything built on Java will cache the first IP address received from DNS, guaranteeing that every future connection targets the same host and completely defeating load balancing."
>
> *Mọi thứ viết bằng Java sẽ cache địa chỉ IP đầu tiên nhận từ DNS, bảo đảm mọi kết nối về sau đều nhắm vào cùng một máy và phá hỏng hoàn toàn việc cân bằng tải.*

Vì vậy DNS round-robin không hợp khi bên gọi là một hệ thống doanh nghiệp chạy lâu (tr. 233). Còn kiểu Apache viết lại URL thành "www7.example.com" thì tệ hơn nữa, vì người dùng bookmark luôn máy cụ thể thay vì "cửa trước" (tr. 234).

**Reverse proxy** chặn mọi request: DNS trỏ về đúng một IP, thiết bị ở đó toả request ra nhiều máy phía sau; ví dụ Squid hay `mod_proxy` của Apache (tr. 234). Nó còn cache được nội dung tĩnh, đỡ tải cho web server nếu web server là ràng buộc công suất (xem [Bài 2 — Công suất](bai_02_cong_suat.md)) (tr. 235). Cái giá: log địa chỉ nguồn thành vô dụng vì chỉ thấy proxy; header `X-Forwarded-For` giúp được, nhưng proxy độc hại chẳng tuân theo, nên nó kém tin cậy đúng lúc cần nhất, như khi truy vết tấn công (tr. 235 và chú thích). Tệ nhất là chuyện kiểm tra sức khoẻ:

> [!quote] Release It! — Ch.13 (tr. 235)
> "They will happily direct an incoming request to a dead server, wait for a timeout, and then return an error to the caller."
>
> *Chúng sẽ vui vẻ gửi request tới một server đã chết, chờ hết timeout, rồi trả lỗi cho bên gọi.*

"Chúng" ở đây là Squid và Apache, hai reverse proxy phổ biến nhất lúc đó (tr. 235).

**Load balancer phần cứng** (Cisco CSS 11500, F5 BigIP) làm vai tương tự nhưng gần mạng hơn, nên thường quản trị và dư thừa tốt hơn: kiểm tra sức khoẻ định kỳ (Hình 13.3 vẽ request `GET /healthy.html`), loại server chết khỏi nhóm, chuyển mạch tầng 4 tới 7, chuyển cả lưu lượng sang site dự phòng (tr. 236–237). Nygard không thích dùng chúng làm "máy tăng tốc SSL", dù thừa nhận cách đó giúp quản lý chứng chỉ gọn; và vừa chuyển thẳng SSL vừa soi nội dung thì chẳng khác gì tấn công man-in-the-middle (tr. 236–237). Nhược điểm lớn là giá: năm chữ số cho cấu hình thấp, sáu chữ số cho cấu hình cao (tr. 237). Khung bên lề gợi ý `mod_proxy_balancer` của Apache 2.2 để tránh khoản $50.000 cho một cặp thiết bị, đụng trần thì thay sau (tr. 236).

## 9. Cluster: cái nạng cho ứng dụng không tự đứng được

Cân bằng tải không đòi các server biết nhau. Khi chúng biết nhau và cùng tham gia phân tải, chúng thành **cluster**: active/active để chia tải, active/passive để dự phòng (tr. 238). Khác biệt quan trọng: farm cân bằng tải thuần tuý scale gần tuyến tính, cluster thì không, vì chi phí heartbeat và đồng bộ trạng thái; công suất tăng chậm hơn tuyến tính và có thể chững hẳn khi thêm máy (tr. 238).

WebSphere, WebLogic, Oracle, SQL Server có cluster tích hợp; chúng luôn có những node "điều khiển chính", có thể là điểm yếu (nhất là khi chỉ có một) và thường chạm giới hạn công suất đầu tiên (tr. 238). Ứng dụng không có cluster riêng thì chạy dưới **cluster server**, như một bộ xương ngoài: heartbeat giữa các máy, thường dùng "quorum volume" trên ổ mạng để đồng bộ, và khi phát hiện node chết thì chạy chuỗi hành động định sẵn: nhận filesystem, khởi động ứng dụng, nhận IP ảo (tr. 238). Nygard lưỡng lự: vừa kỳ diệu vừa chắp vá; cấu hình khó tính, failover thường có trục trặc nhỏ, và nhược điểm lớn nhất có lẽ là chạy active/passive, nên có dư thừa mà không có khả năng mở rộng (tr. 238–239).

> [!quote] Release It! — Ch.13 (tr. 239)
> "I consider cluster servers a Band-Aid for applications that don’t do it themselves."
>
> *Tôi coi cluster server là miếng băng dán cho những ứng dụng không tự làm được việc đó.*

## 10. QA có khớp production không

Ch.14 mở bằng một lời hứa:

> [!quote] Release It! — Ch.14 (tr. 240)
> "If your system is easy to administer, it will have good uptime."
>
> *Hệ thống dễ quản trị thì sẽ có uptime tốt.*

Và một lời đe: hệ thống khó quản trị sẽ bị bỏ bê, có lẽ bị triển khai sai, thậm chí bị phá ngầm (tr. 240). Người quản trị hầu như không được hỏi ý kiến lúc thiết kế, chỉ nhận phần mềm nửa sống nửa chín ném qua tường. Xung đột sâu hơn: với dev và người dùng, bản mới là tính năng mới; với người quản trị, bản mới là thêm việc, log cũ biến mất, kiểu hỏng mới chưa ai biết cách phát hiện. "Cả hai góc nhìn cùng đúng!" Muốn họ thành đồng minh, hãy hiểu động cơ của họ và làm việc của họ dễ hơn (tr. 240).

Sau mỗi lần deploy hỏng, chín trên mười lần sẽ có người hỏi: "cấu hình QA và production có khác nhau không?" (tr. 241). Nygard gọi đó là câu hỏi "gimme": dễ hỏi, rất tốn để trả lời, và chắc chắn tìm ra khác biệt, ít nhất là hostname và IP; phần tốn là phân loại khác biệt nào vô hại, cái nào nguy hiểm. Mà QA thì phải khác: giống hệt tới từng hostname thì nó là production rồi (tr. 241). Theo kinh nghiệm của ông, sau hàng giờ rà file cấu hình, thỉnh thoảng cũng lòi ra chuyện đáng kể, nhưng lệch cấu hình thường không phải thủ phạm (tr. 241):

> [!quote] Release It! — Ch.14 (tr. 241)
> "Most of the time, the real culprit is a mismatch in topology between QA and production."
>
> *Phần lớn thời gian, thủ phạm thật là sự lệch topology giữa QA và production.*

Topology là số lượng và cách nối của server và ứng dụng, xem như đồ thị nút và cạnh (tr. 241–242). Rào cản là tiền, nên Nygard đưa bốn cách rẻ (tr. 242–243):

- **Tách chúng ra.** Hai ứng dụng chung máy ở QA nhưng tách ở production có thể ngầm dựa vào một thư mục chung ("cron job chạy rsync phút chót không tính!"). Dùng VMware để mỗi ứng dụng có máy ảo riêng (tr. 242).
- **Không, một, nhiều.** Một instance ở QA, nhiều ở production có thể là khác biệt giữa huỷ cache điểm-điểm và multicast. Không cần đủ số, nhưng phải hơn một (tr. 242).
- **Tập sao đá vậy.** Làm với firewall từ ngày đầu thì luật firewall đã được ghi sẵn; hầu như không gì đau bằng đi tìm mọi luật cần có cho một hệ thống đã xong 95%. Mỗi lỗ firewall là một integration point (tr. 243).
- **Cứ mua thiết bị đi.**

> [!quote] Release It! — Ch.14 (tr. 243)
> "I’ve seen hours of downtime result from the presence of firewalls or load balancers in production that did not exist in QA."
>
> *Tôi từng thấy hàng giờ downtime chỉ vì production có firewall hay load balancer mà QA không có.*

Chi phí downtime đó vượt giá thiết bị. QA không cần hàng đầu bảng, nhưng nên cùng hãng, cùng dòng: "Bạn thử thay đổi cấu hình firewall ở đâu cơ chứ?" (tr. 243).

## 11. File cấu hình là giao diện người dùng

File cấu hình doanh nghiệp chứa hostname, cổng, đường dẫn, khoá, mật khẩu, "và số xổ số" (Nygard thú nhận bịa cái cuối) (tr. 243). Sai một cái là hỏng, có khi hỏng mà không ai biết. Thuộc tính tên `hostname` là "hostname của tôi", "tên bên gọi được phép", hay "máy tôi gọi vào ngày thu phân"? Liên kết ngầm và độ phức tạp cao là hai trong những yếu tố lớn nhất dẫn tới lỗi người vận hành (tr. 243–244).

**Đừng trộn cấu hình production với "hệ ống nước".** Spring muốn mọi thứ trong một file, cả thuộc tính đổi theo môi trường lẫn chi tiết khởi tạo đối tượng; kết quả là người quản trị sửa tay file XML 5.000 dòng để đổi một mật khẩu, 4.999 dòng kia là mìn (tr. 244).

> [!quote] Release It! — Ch.14 (tr. 244)
> "It should never be possible for an administrator to break object associations inside the application. That’s just wearing your guts on the outside."
>
> *Không bao giờ được để người quản trị có thể làm gãy liên kết giữa các đối tượng bên trong ứng dụng. Thế chẳng khác gì mang ruột gan ra bên ngoài.*

**Đừng đặt cấu hình production dưới thư mục cài đặt:** nâng cấp sẽ ghi đè, người quản trị hay chép nguyên cây cài đặt sang máy khác, khôi phục từ băng có thể đè bản mới bằng bản cũ (tr. 244). **Đưa cấu hình vào quản lý phiên bản** (khung "Joe Asks"), với bốn ràng buộc: kho an toàn vì có mật khẩu; gắn với quy trình quản lý thay đổi để biết *vì sao* đổi; tự động triển khai thay đổi đã duyệt từ kho; kiểm toán tự động để tìm thay đổi làm vội lúc chữa cháy mà không tự ghi đè chúng (tr. 245). **Tách phần giống và phần khác** giữa các máy cùng tầng, và định kỳ kiểm chúng có thật đồng bộ: "Tin, nhưng kiểm" (tr. 246).

> [!quote] Release It! — Ch.14 (tr. 246)
> "Finally, configuration properties are part of the system’s user interface."
>
> *Cuối cùng, các thuộc tính cấu hình là một phần giao diện người dùng của hệ thống.*

Người dùng ở đây là người giữ hệ thống chạy mỗi ngày. Vì vậy **đặt tên theo chức năng, không theo bản chất**: không ai đặt tên biến là `integer`, vậy đừng gọi `hostname`; gọi `authenticationServer`, người quản trị sẽ biết đi tìm máy LDAP hay Active Directory (tr. 246).

## 12. Khởi động, tắt máy và giao diện quản trị

Dev khởi động app, thấy lỗi, sửa. Máy bị khởi động lại lúc nửa đêm và ứng dụng hỏng thì chẳng ai biết, trừ khi ứng dụng tự báo; mà muốn báo thì nó phải *biết* mình hỏng (tr. 247). Nygard ví với cửa hàng buổi sáng: không ai mở cửa cho khách chỉ vì một nhân viên đã tới.

> [!quote] Release It! — Ch.14 (tr. 247)
> "Build a clean start-up sequence into applications to ensure that components are started in the right order and that the start-up sequence must complete successfully before the application starts accepting work."
>
> *Hãy xây vào ứng dụng một trình tự khởi động sạch, bảo đảm các thành phần khởi động đúng thứ tự và trình tự đó phải hoàn tất thành công trước khi ứng dụng bắt đầu nhận việc.*

Có thể bind socket nhưng chưa nhận kết nối cho tới khi "cầu dao tổng" bật. Khởi tạo sẵn vài kết nối trong connection pool là một dạng Fail Fast; không tạo được kết nối nào thì cả ứng dụng ở trạng thái hỏng. Nhưng ở trạng thái hỏng **khác** thoát hẳn: ứng dụng còn chạy thì còn hỏi được trạng thái bên trong (tr. 247). Tắt máy cũng vậy: cửa hàng không khoá cửa khi khách còn trong; hoàn tất giao dịch dở, không nhận việc mới, rồi thoát, và phải có timeout (tr. 247).

**Giao diện quản trị.** GUI Java demo rất ấn tượng nhưng ở production là ác mộng: click thì không script được (tr. 248). Trình tự tắt máy sạch của một hệ thống quản lý đơn hàng Nygard từng làm đòi click, rồi chờ vài phút, trên từng máy trong sáu server. "Đoán xem trình tự đó được tuân thủ thường xuyên cỡ nào?" Cửa sổ thay đổi chỉ một giờ thì không ai đốt nửa giờ chờ GUI. Truy cập từ xa còn khổ hơn: người quản trị thường vào máy qua những đường hầm SSH quanh co, và đẩy kết nối X hay HTTP qua đó rất phiền; thứ khó như vậy sẽ không được dùng, nên ông dự đoán "rất nhiều lệnh `kill -9`" (tr. 248).

> [!quote] Release It! — Ch.14 (tr. 248)
> "The best interface for long-term operation is the command line."
>
> *Giao diện tốt nhất cho vận hành lâu dài là dòng lệnh.*

Lùi một bước lớn nhưng vẫn dùng được là giao diện quản trị HTML thuần, vì script gọi HTTP không khó (tr. 248).

## 13. Tóm tắt thiết kế của Nygard

Ch.15 là hai trang văn xuôi nhắc lại các ý trên (tr. 249–250): bind đúng địa chỉ, gọi dịch vụ cluster qua IP ảo, không đòi root, mật khẩu trong file riêng, bàn availability như phép đánh đổi chi phí, định kiến trúc high availability từ sớm, khởi động và tắt không làm phiền người dùng, mọi việc quản trị phải script được. Theo Nygard, người quản trị sẽ không bao giờ hiểu bên trong ứng dụng bằng bạn, nên cấu hình phải hiển nhiên, và muốn vậy thì tách hệ ống nước khỏi cấu hình theo môi trường. Hình ảnh ông dùng cho việc trộn hai thứ đó:

> [!quote] Release It! — Ch.15 (tr. 250)
> "Mixing them is the equivalent of putting the ejection seat button next to the radio tuner."
>
> *Trộn chúng với nhau chẳng khác gì đặt nút ghế phóng ngay cạnh nút dò đài.*

## 14. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống.**
> - *Availability là bài toán tiền.* Chương "Embracing Risk" của *Site Reliability Engineering* (Google) viết chi phí "không tăng tuyến tính", một bước tăng tin cậy "có thể tốn gấp 100 lần bước trước" (Bài 0, mục 9 đã dẫn ý này), và đưa ví dụ: nâng 99,9% lên 99,99% cho dịch vụ doanh thu 1 triệu đô chỉ đáng làm nếu tốn dưới 900 đô. Hệ số khác Nygard (khoảng 10 lần chi phí xây dựng), cùng kết luận.
> - *SLA phải chặt* nay có từ vựng chuẩn: **SLI** là thước đo định lượng (độ trễ, tỉ lệ lỗi), **SLO** là mục tiêu đo bằng SLI, **SLA** là hợp đồng có hệ quả khi trượt SLO (Google SRE, Ch.4). Với câu hỏi "theo thời gian hay theo số mẫu" (tr. 232), Google chọn đo dịch vụ phân tán của họ theo **tỉ lệ request thành công** (Ch.3 "Embracing Risk"). Cũng ở Ch.3, Google thêm thứ sách không có: **error budget**, chênh lệch giữa SLO và uptime đo được trong quý; còn budget thì được release, tiêu hết thì tạm dừng release.
> - *Khởi động và tắt sạch* thành hợp đồng của nền tảng. Kubernetes có **readiness probe** (hỏng thì Pod bị gỡ khỏi Service, không nhận traffic) và **startup probe**; khi tắt, gửi SIGTERM, chờ mặc định 30 giây rồi SIGKILL. 12-factor ghi tiến trình phải "tắt nhẹ nhàng khi nhận SIGTERM". Đúng hai ý ở tr. 247.
> - *Health check* không còn là tính năng của thiết bị năm chữ số: Application Load Balancer của AWS định kỳ kiểm các target và chỉ chuyển request tới target khoẻ (và "fail open" nếu mọi target cùng hỏng).
> - *Tách cấu hình khỏi code.* 12-factor coi cấu hình là "mọi thứ có khả năng thay đổi giữa các lần deploy", đòi tách nghiêm ngặt khỏi code, phép thử là codebase mở nguồn được bất cứ lúc nào mà không lộ thông tin xác thực. Khung "Joe Asks" (tr. 245) nay là **infrastructure as code**, như Terraform: hạ tầng trong file cấu hình "có thể quản lý phiên bản, tái dùng và chia sẻ".
>
> **Phần cần chỉnh.**
> - *Từ card vật lý sang mạng ảo.* Bốn card ở mục 2 nay thường là subnet và bảng định tuyến trong một **VPC**, "mạng ảo cô lập về logic" rất giống mạng trung tâm dữ liệu truyền thống (AWS). "Spam cannon qua VPN" (tr. 222) có hậu duệ là VPC endpoint, nối riêng tới dịch vụ AWS không qua internet gateway. Nguyên tắc "bind đúng chỗ, ghi lại mọi tuyến" giữ nguyên.
> - *IP ảo nhường chỗ cho DNS, va vào đúng lời cảnh báo của Nygard.* RDS Multi-AZ giữ bản dự phòng đồng bộ ở Availability Zone khác; failover (thường 60–120 giây) đổi **bản ghi DNS** sang máy dự phòng, nên ứng dụng phải kết nối lại. Lời dặn "chờ `SQLException`" (tr. 224) còn nguyên, và vì cơ chế giờ là DNS, chuyện Java cache IP (tr. 233) thành vấn đề trực tiếp: AWS khuyên TTL DNS của JVM không quá 60 giây. Còn "mọi thứ viết bằng Java" thì không còn tuyệt đối: Oracle ghi cache mãi mãi là mặc định **khi có security manager**, không có thì tuỳ bản cài đặt; AWS ghi nhiều JVM mặc định dưới 60 giây; từ Java 24, JEP 486 vô hiệu vĩnh viễn Security Manager.
> - *Cổng dưới 1024 không còn cần root:* trên Linux, capability `CAP_NET_BIND_SERVICE` cho bind cổng dưới 1024.
> - *Bảo mật gói trong ba trang (tr. 226–228); chính Nygard nói bảo mật đầy đủ vượt xa phạm vi sách (tr. 226).* **OWASP Top 10:2025** (công bố tháng 11/2025, bản đầu tiên từ 2021, nay đã Final): A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions. *Nhận định của khoá:* Ch.12 chỉ chạm một phần A02 và chuyện giữ bí mật.
> - *Chuỗi cung ứng.* A03 là hạng mục mới. NTIA (7/2021, theo Sắc lệnh 14028) công bố yếu tố tối thiểu của **SBOM**, "bản ghi chính thức chứa chi tiết và quan hệ chuỗi cung ứng của các thành phần dùng để dựng phần mềm". Sách 2007 không bàn thư viện bên thứ ba như bề mặt tấn công.
> - *Mạng quản trị không còn là nền của niềm tin.* Nygard coi gắn SSH riêng vào card quản trị là lớp bảo vệ quan trọng (tr. 221). NIST SP 800-207 (8/2020) về **zero trust** giả định không có niềm tin ngầm định nào "chỉ dựa trên vị trí vật lý hay vị trí mạng". *Nhận định của khoá:* tách mạng vẫn là một lớp phòng thủ, nhưng truy cập qua mạng quản trị vẫn phải xác thực và cấp quyền như từ Internet.
> - *Mật khẩu trong file có chỗ ở tốt hơn.* "Password vaulting" (tr. 228) nay là **secrets manager**: AWS Secrets Manager thay thông tin xác thực viết cứng bằng lời gọi lúc chạy, xoay vòng tự động để dùng bí mật ngắn hạn, và xoay vòng không cần deploy lại. Lời dặn tắt core dump (tr. 228) vẫn nguyên giá trị.
>
> **Phần đã lỗi thời.** Tên sản phẩm (HP ServiceGuard, Veritas, Cisco CSS, F5 BigIP, Squid, VMware cho QA, Spring XML, GUI Java) và mức giá $50.000 là bối cảnh 2007. Giữ mẫu hình, thay tên bằng thứ của thời mình.

## 15. Áp dụng vào việc của bạn

> [!question] Khi thiết kế và viết code
> 1. **Kiểm mọi chỗ `listen`.** Tìm trong code mọi socket, HTTP server, cổng admin, cổng metrics. Cái nào đang bind `0.0.0.0` mà không có cấu hình để đổi? Cổng quản trị có tách khỏi cổng phục vụ người dùng không? (mục 2)
> 2. **Đổi tên thuộc tính cấu hình theo chức năng.** Tìm `host`, `url`, `server` trơn trụi; đổi thành tên nói lên *vai trò* như `authenticationServer`. Tách phần "hệ ống nước" (wiring) khỏi phần đổi theo môi trường. (mục 11)
> 3. **Viết trình tự khởi động có cầu dao tổng.** Ứng dụng chỉ báo "ready" sau khi các phụ thuộc thiết yếu (ít nhất vài kết nối database) đã lên; hỏng thì ở trạng thái hỏng và hỏi được, chứ không thoát im lặng. Tắt máy thì ngừng nhận việc mới, xong việc dở, có timeout. (mục 12)
> 4. **Chuẩn bị cho failover.** Mọi lời gọi tới database hay dịch vụ qua một địa chỉ có thể "nhảy" (IP ảo, DNS failover) phải xử lý lỗi kết nối giữa chừng và thử lại có giới hạn. Kiểm TTL DNS của runtime bạn dùng. (mục 3, 14)

> [!question] Khi vận hành, trực on-call, viết postmortem
> 1. **Viết lại một SLA theo các câu hỏi ở mục 7.** Chọn một tính năng quan trọng; trả lời thành văn: đo bằng giao dịch tổng hợp nào, bao lâu một lần, từ đâu, ngưỡng thời gian, mã thành công và thất bại, lưu dữ liệu ở đâu, công thức tính. (mục 7)
> 2. **Vẽ topology QA cạnh topology production.** Đánh dấu mọi chỗ lệch: số instance (một hay nhiều), firewall, load balancer, máy dùng chung. Mỗi dấu là một ứng viên cho postmortem tiếp theo. (mục 10)
> 3. **Trong postmortem, hỏi "cái này có script được không?".** Bước khắc phục nào phải làm bằng click hay bằng tay trên từng máy? Nygard đoán rằng những bước ấy sẽ bị bỏ qua. (mục 12)
> 4. **Kiểm toán bí mật.** Liệt kê nơi đang chứa mật khẩu production: file nào, quyền gì, có nằm trong thư mục cài đặt, trong image, trong repo không; core dump có bật không. (mục 5)

## 16. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Multihomed server** | Máy chủ có nhiều địa chỉ IP, đồng thời nằm trên nhiều mạng (production, backup, quản trị) (tr. 219). |
| **Virtual IP (IP ảo)** | Địa chỉ IP chuyển được giữa các card mạng; cũng dùng cho địa chỉ dịch vụ trên load balancer (tr. 224). |
| **Cluster server** | Phần mềm điều phối để một ứng dụng chạy đúng một lần trong cluster và failover sang máy khác (tr. 223, 238). |
| **Heartbeat** | Gói tin giữa các máy trong cluster báo "tôi còn sống" (tr. 223, 238). |
| **Nguyên tắc quyền tối thiểu** | Mỗi tiến trình chỉ có mức quyền thấp nhất đủ để làm việc; ứng dụng không chạy bằng root (tr. 226). |
| **Password vaulting** | Giữ mật khẩu trong file mã hoá, quy về bài toán bảo vệ một khoá (tr. 228). |
| **SLA** | Thoả thuận mức dịch vụ; Nygard đòi định nghĩa theo tính năng và đo bằng máy (tr. 230–232). |
| **SLA Inversion** | Hứa SLA tốt hơn phụ thuộc tệ nhất của tính năng, điều không thể (tr. 231; phản mẫu ở Bài 1). |
| **Giao dịch tổng hợp (synthetic transaction)** | Giao dịch giả lập người dùng thật, có dấu nhận biết, để đo availability (tr. 231). |
| **SLI / SLO / error budget** | Thước đo / mục tiêu / phần "không tin cậy" còn được phép trong kỳ; khung của Google SRE, không có trong sách (mục 14). |
| **DNS round-robin** | Cân bằng tải bằng cách gắn nhiều IP vào một tên (tr. 232–233). |
| **Reverse proxy** | Máy chặn mọi request đến một IP rồi toả ra nhiều máy phía sau (tr. 234). |
| **Topology** | Số lượng và cách nối của server và ứng dụng, xem như đồ thị nút và cạnh (tr. 241–242). |
| **Zero trust** | Không tin ngầm định dựa trên vị trí mạng (NIST SP 800-207); không có trong sách (mục 14). |
| **SBOM** | Bản kê các thành phần và quan hệ chuỗi cung ứng của phần mềm; không có trong sách (mục 14). |
| **Infrastructure as code** | Mô tả hạ tầng bằng file cấu hình quản lý phiên bản được; hậu duệ của "Joe Asks" (tr. 245, mục 14). |

## 17. Câu hỏi tự kiểm tra

1. Vì sao máy chủ trong trung tâm dữ liệu thường có nhiều card mạng? Hậu quả gì nếu ứng dụng không biết điều đó? *(tr. 219–222)*
2. IP ảo chuyển được địa chỉ, nhưng không chuyển được gì? Ứng dụng gọi database qua IP ảo phải chuẩn bị điều gì? *(tr. 224–225)*
3. Lý do duy nhất khiến một ứng dụng UNIX có thể cần root theo Nygard là gì, và có hai cách nào để tránh hoặc giảm thiểu? *(tr. 227)* Năm 2026 có thêm cách nào? *(mục 14)*
4. Nêu ba biện pháp Nygard đòi cho mật khẩu production. Vì sao phải tắt core dump? *(tr. 227–228)*
5. Tự tính lại bảng 98% so với 99,99%. Con số "Net Savings" của sách thực ra là gì? *(tr. 229–230)*
6. Vì sao "hệ thống sẽ sẵn sàng 99,9%" là câu vô nghĩa? Kể ít nhất năm điều một định nghĩa availability tốt phải chốt. *(tr. 230–232)*
7. So sánh DNS round-robin, reverse proxy và load balancer phần cứng theo: kiểm tra sức khoẻ, bảo mật, chi phí. *(tr. 232–237)*
8. Theo Nygard, thủ phạm thường gặp nhất khi QA không bắt được lỗi là gì? Bốn cách rẻ để khắc phục? *(tr. 241–243)*
9. Vì sao GUI quản trị làm hỏng quy trình tắt máy sạch? *(tr. 248)*

## Tóm tắt một trang

```
BÀI 3 — THIẾT KẾ TỔNG QUÁT (Part III, tr. 218–250)
────────────────────────────────────────────────────────────────
KHÔNG CÓ CASE   Part III không có nghiên cứu tình huống.
                "Không xử lý lúc dev → xử lý ở production, hết lần này tới lần khác." (tr. 249)

MẠNG (Ch.11)    Máy multihomed: production ×2, backup, quản trị.
                Bind ĐÚNG interface (cấu hình được). Ghi mọi tuyến ra bảng.
                IP ảo chuyển địa chỉ, KHÔNG chuyển trạng thái → chờ SQLException.

BẢO MẬT (Ch.12) Không root. Mỗi app một user. Privilege separation.
                Mật khẩu: file riêng, ngoài thư mục cài, chỉ owner đọc,
                tắt core dump, vaulting + Tripwire.

AVAILABILITY    Muốn mà không nhìn giá = trẻ con đòi cả thùng kem.
(Ch.13)         Mỗi số 9: xây ×10, vận hành ×2 mỗi năm.
                SLA theo TÍNH NĂNG, đo bằng giao dịch tổng hợp.
                LB: DNS RR (mù) < reverse proxy < LB phần cứng (health check).
                Cluster = miếng băng dán; active/passive không scale.

QUẢN TRỊ        Dễ quản trị → uptime tốt.
(Ch.14)         Thủ phạm: lệch TOPOLOGY, không phải lệch cấu hình.
                Cấu hình = giao diện người dùng. Tách khỏi wiring, ngoài
                thư mục cài, đặt tên theo chức năng.
                Khởi động xong mới nhận việc; tắt có timeout; dòng lệnh > GUI.

2026            Còn sống: SLO/error budget, readiness probe, SIGTERM,
                12-factor config, IaC, health check mặc định.
                Cần chỉnh: VPC thay card vật lý; failover qua DNS (TTL JVM);
                OWASP 2025 + chuỗi cung ứng/SBOM; zero trust; secrets manager.
```

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software* (Pragmatic Bookshelf, 2007), `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`:
  - **Part III** (`tr. 218`): trang tên phần, không có nghiên cứu tình huống.
  - **Ch.11 Networking** (`tr. 219–225`): 11.1 Multihomed Servers (tr. 219–222); 11.2 Routing (tr. 222); 11.3 Virtual IP Addresses (tr. 223–225).
  - **Ch.12 Security** (`tr. 226–228`): 12.1 The Principle of Least Privilege (tr. 226–227); 12.2 Configured Passwords (tr. 227–228).
  - **Ch.13 Availability** (`tr. 229–239`): 13.1 Gathering Availability Requirements (tr. 229–230); 13.2 Documenting Availability Requirements (tr. 230–232); 13.3 Load Balancing (tr. 232–237); 13.4 Clustering (tr. 238–239).
  - **Ch.14 Administration** (`tr. 240–248`): mở chương (tr. 240–241); 14.1 "Does QA Match Production?" (tr. 241–243); 14.2 Configuration Files (tr. 243–246); 14.3 Start-up and Shutdown (tr. 247); 14.4 Administrative Interfaces (tr. 248).
  - **Ch.15 Design Summary** (`tr. 249–250`).
  - Quy ước trích: `tr. X` = số trang in = số trang PDF.
- Nguồn web dùng ở Đối chiếu 2026 (truy cập 9/2026):
  - Google, *Site Reliability Engineering*, Ch.3 "Embracing Risk": https://sre.google/sre-book/embracing-risk/
  - Google, *Site Reliability Engineering*, Ch.4 "Service Level Objectives": https://sre.google/sre-book/service-level-objectives/
  - Kubernetes, "Liveness, Readiness, and Startup Probes": https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
  - Kubernetes, "Pod Lifecycle" (Termination of Pods): https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
  - The Twelve-Factor App, "III. Config": https://12factor.net/config
  - The Twelve-Factor App, "IX. Disposability": https://12factor.net/disposability
  - HashiCorp, "What is Terraform?": https://developer.hashicorp.com/terraform/intro
  - AWS, "Health checks for Application Load Balancer target groups": https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html
  - AWS, "What is Amazon VPC?": https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
  - AWS, "Multi-AZ DB instance deployments for Amazon RDS": https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html
  - AWS, "Failing over a Multi-AZ DB instance for Amazon RDS" (gồm mục JVM TTL): https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html
  - Oracle, Java SE 21 Core Libraries, "Networking" (`networkaddress.cache.ttl`): https://docs.oracle.com/en/java/javase/21/core/java-networking.html
  - OpenJDK, "JEP 486: Permanently Disable the Security Manager": https://openjdk.org/jeps/486
  - man7.org, capabilities(7) (`CAP_NET_BIND_SERVICE`): https://man7.org/linux/man-pages/man7/capabilities.7.html
  - OWASP, "OWASP Top 10:2025": https://top10.owasp.org/2025
  - OWASP, kho GitHub Top10 ("We have released the OWASP Top 10:2025 (Final)"): https://github.com/owasp/top10
  - The Register, "OWASP Top 10: Broken access control still tops app security list" (11/11/2025): https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/
  - NTIA, "The Minimum Elements For a Software Bill of Materials (SBOM)" (12/7/2021): https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
  - NIST, SP 800-207 "Zero Trust Architecture" (8/2020): https://csrc.nist.gov/pubs/sp/800/207/final
  - AWS, "What is AWS Secrets Manager?": https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Ổn định](bai_01_on_dinh.md) · [Bài 2 — Công suất](bai_02_cong_suat.md) · [Bài 3 ← bạn đang ở đây] · [Bài 4 — Vận hành](bai_04_van_hanh.md)

Xem thêm [README khoá học](../README.md).
