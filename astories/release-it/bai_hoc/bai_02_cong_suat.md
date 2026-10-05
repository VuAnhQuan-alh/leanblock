# Bài 2 — Công suất: hệ số nhân quyết định tất cả

> [!info] Về bài này
> Dựng từ **Part II — Capacity** của *Release It!* (Michael T. Nygard, 2007, `tai_lieu/`, `tr. 146–217`): Ch.7 nghiên cứu tình huống "Trampled by Your Own Customers", Ch.8 Introducing Capacity, Ch.9 Capacity Antipatterns, Ch.10 Capacity Patterns.
> Trích theo `Ch. N` và `tr. X` (**số trang in = số trang PDF**). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> *Cần đọc trước:* [Bài 1 — Ổn định](bai_01_on_dinh.md). Bài này nhiều lần quay lại luồng bị chặn và lỗi dây chuyền, vì Nygard cho thấy vấn đề công suất rất hay hoá thành vấn đề ổn định.

## Mục lục

1. [Mở đầu: bị chính khách hàng của mình giẫm nát](#1-mở-đầu-bị-chính-khách-hàng-của-mình-giẫm-nát)
2. [Hai lỗ hổng của kiểm thử tải, và cái giá của bản vá tạm](#2-hai-lỗ-hổng-của-kiểm-thử-tải-và-cái-giá-của-bản-vá-tạm)
3. [Bốn chữ phải tách bạch](#3-bốn-chữ-phải-tách-bạch)
4. [Chỉ một ràng buộc quyết định công suất](#4-chỉ-một-ràng-buộc-quyết-định-công-suất)
5. [Rộng ra hay to lên](#5-rộng-ra-hay-to-lên)
6. [Ba ngộ nhận "rẻ" và hệ số nhân](#6-ba-ngộ-nhận-rẻ-và-hệ-số-nhân)
7. [Vì sao phản mẫu công suất cứ bị làm lại](#7-vì-sao-phản-mẫu-công-suất-cứ-bị-làm-lại)
8. [Phản mẫu 1: Tranh chấp pool tài nguyên](#8-phản-mẫu-1-tranh-chấp-pool-tài-nguyên)
9. [Phản mẫu 2: Quá nhiều mảnh JSP](#9-phản-mẫu-2-quá-nhiều-mảnh-jsp)
10. [Phản mẫu 3: Lạm dụng AJAX](#10-phản-mẫu-3-lạm-dụng-ajax)
11. [Phản mẫu 4: Session ở lì](#11-phản-mẫu-4-session-ở-lì)
12. [Phản mẫu 5: Byte thừa trong HTML](#12-phản-mẫu-5-byte-thừa-trong-html)
13. [Phản mẫu 6: Nút Reload](#13-phản-mẫu-6-nút-reload)
14. [Phản mẫu 7: SQL viết tay](#14-phản-mẫu-7-sql-viết-tay)
15. [Phản mẫu 8: Cơ sở dữ liệu phú dưỡng](#15-phản-mẫu-8-cơ-sở-dữ-liệu-phú-dưỡng)
16. [Phản mẫu 9: Độ trễ ở điểm tích hợp](#16-phản-mẫu-9-độ-trễ-ở-điểm-tích-hợp)
17. [Phản mẫu 10: Quái vật cookie](#17-phản-mẫu-10-quái-vật-cookie)
18. [Hoare bị trích nửa câu](#18-hoare-bị-trích-nửa-câu)
19. [Mẫu 1: Gộp kết nối](#19-mẫu-1-gộp-kết-nối)
20. [Mẫu 2: Dùng cache cẩn thận](#20-mẫu-2-dùng-cache-cẩn-thận)
21. [Mẫu 3: Tính trước nội dung](#21-mẫu-3-tính-trước-nội-dung)
22. [Mẫu 4: Tinh chỉnh bộ gom rác](#22-mẫu-4-tinh-chỉnh-bộ-gom-rác)
23. [Đối chiếu 2026](#23-đối-chiếu-2026)
24. [Áp dụng vào việc của bạn](#24-áp-dụng-vào-việc-của-bạn)
25. [Từ điển thuật ngữ](#25-từ-điển-thuật-ngữ)
26. [Câu hỏi tự kiểm tra](#26-câu-hỏi-tự-kiểm-tra)
27. [Tóm tắt một trang](#tóm-tắt-một-trang)
28. [Nguồn](#nguồn)

---

## 1. Mở đầu: bị chính khách hàng của mình giẫm nát

Minnesota. Nygard vào một đội hơn ba trăm người chín tháng trước ngày ra mắt, để thay toàn bộ cửa hàng trực tuyến, quản trị nội dung, chăm sóc khách hàng và xử lý đơn hàng của một nhà bán lẻ. Hệ thống sẽ là xương sống của công ty bảy năm tới, và lúc ông vào thì đã trễ hơn một năm. Chín tháng "crunch", không ai thấy mặt trời; có đội ăn trưa và tối do khách hàng mang tới mọi ngày trong tuần, và Nygard tới giờ vẫn rùng mình khi nhớ món taco gà tây (tr. 147). Hôm nay marketing tụ trong phòng hội nghị lớn, sâm panh sẵn sàng; dân kỹ thuật vây quanh một bức tường màn hình canh sức khoẻ site (tr. 147–148).

> [!quote] Release It! — Ch.7 (tr. 148)
> "At 9 a.m., the program manager hit the big red button."
>
> *Đúng 9 giờ sáng, giám đốc chương trình bấm nút đỏ to tướng.*

Cái nút có thật, nối tới một đèn LED ở phòng bên, nơi một anh kỹ thuật bấm Reload trên trình duyệt đang chiếu lên màn hình. Thay đổi thật do **CDN** làm: bản cập nhật metadata lên lịch lúc 9 giờ, mất khoảng tám phút lan khắp mạng, nên lưu lượng dự kiến đổ về từ khoảng 9:05 (tr. 148). (Chú thích kể thêm: thứ Bảy trước đó CDN nhập sai thay đổi và cho cả thế giới xem trước site mới, đang nạp dở mà vẫn nhận đơn; mất hai giờ để tìm ra và đảo ngược.)

> [!quote] Release It! — Ch.7 (tr. 148)
> "By 9:30 a.m., there were 250,000 sessions active on the site. Then, the site crashed."
>
> *Tới 9:30 sáng, site có 250.000 session đang hoạt động. Rồi site sập.*

9:05 đã có 10.000 session, 9:10 hơn 50.000 (tr. 148). Để hiểu vì sao, Nygard lùi lại ba năm.

**Nhắm vào QA.** Mọi dự án website "thật ra là dự án tích hợp doanh nghiệp có giao diện HTML" (tr. 149). Hệ thống không xây theo các mẫu ổn định, và với một chồng công nghệ mới toanh, công suất, ổn định, kiểm soát, thích nghi đều là "dấu hỏi khổng lồ" (tr. 149).

> [!quote] Release It! — Ch.7 (tr. 149)
> "Early in my time on the project, I realized that the development teams were building everything to pass testing, not to run in production."
>
> *Mới vào dự án ít lâu, tôi nhận ra các đội phát triển đang xây mọi thứ để qua được kiểm thử, chứ không phải để chạy ở production.*

Mười lăm ứng dụng, hơn năm trăm điểm tích hợp, mọi file cấu hình viết cho môi trường kiểm thử; hostname, cổng, mật khẩu rải trong hàng nghìn file; production lại có thêm tường lửa và chạy cụm ở chỗ QA chỉ có một instance (tr. 149). Riêng đổi mật khẩu database có vẻ phải sửa hơn trăm file trên hai mươi máy. Nygard thêm một tầng gián tiếp: cấu trúc ghi đè tách khỏi mã nguồn, mỗi thuộc tính khác nhau giữa môi trường chỉ nằm một chỗ (tr. 151). Và thế là ông "vô tình tình nguyện" tham gia kiểm thử tải.

**Kiểm thử tải.** Khách dành hẳn một tháng, lâu nhất ông từng thấy; marketing đòi chịu được **25.000 người dùng đồng thời** (tr. 152). Kịch bản trộn "grazer", "searcher", "buyer": hơn 90% chỉ xem trang chủ và một trang sản phẩm, 4% đi tới thanh toán, một trong những việc đắt nhất (tr. 152). Lần chạy đầu, mới 1.200 người dùng đồng thời thì site khoá cứng; cần tăng công suất hai mươi lần (tr. 154). Ba tháng, mười hai giờ mỗi ngày trên cuộc gọi hội nghị, có hôm máy trong trại tạo tải bị hack giữa buổi test, có hôm một kỹ sư AT&T bóp đúng đường truyền tạo 80% tải (tr. 154). Sau hơn sáu mươi bản build: công suất gấp mười, 12.000 session, ước chừng 10.000 khách. Marketing hạ mục tiêu xuống 12.000 session: thà site chậm còn hơn không có site (tr. 155).

**Giết bởi đám đông.** Khách còn chưa được báo ngày ra mắt, nên không phải marketing đoán sai nhu cầu. Chính số session dẫn tới thủ phạm: mỗi session tốn RAM, và vì bật session replication, nó còn bị tuần tự hoá gửi sang máy dự phòng sau mỗi request, tốn CPU và băng thông (tr. 155). Nguồn session là **nhiễu** mà kịch bản lịch sự không tạo ra (tr. 156–157):

- Công cụ tìm kiếm mang khoảng 40% lượt ghé, nhưng dẫn tới URL cũ; web server đẩy mọi request `.html` sang application server, nên mỗi khách tạo một session chỉ để nhận trang 404.
- Spider không giữ cookie, mỗi request một session mới nằm trong RAM ba mươi phút; một công cụ tạo tới mười session mỗi giây.
- Gần một tá scraper cỡ lớn; vài con khéo giấu nguồn, có con gửi từ nhiều subnet nhỏ và đổi User-Agent liên tục.
- Shopbot dò hàng PlayStation 2 mỗi phút, ba năm sau đợt khan hàng.
- "Những thứ quái lạ", như một máy ở căn cứ Hải quân cứ gọi lại URL cuối mãi ([Bài 1 — Ổn định](bai_01_on_dinh.md) có một proxy Hải quân rất giống ở Ch.4, tr. 73).

## 2. Hai lỗ hổng của kiểm thử tải, và cái giá của bản vá tạm

Kịch bản test tải của bạn có bao giờ gọi cùng một URL một trăm lần mỗi giây mà không kèm cookie? Của đội Nygard thì không; và nếu có, "có lẽ chúng tôi đã gọi bài test đó là 'phi thực tế'" rồi lờ đi (tr. 157).

> [!quote] Release It! — Ch.7 (tr. 157)
> "In short, all the test scripts obeyed the rules."
>
> *Tóm lại, mọi kịch bản test đều tuân thủ luật chơi.*

Lỗ hổng thứ hai: ứng dụng không có thiết bị an toàn để cắt bỏ thứ xấu, cứ đẩy thêm luồng vào vùng nguy hiểm như tai nạn liên hoàn trên xa lộ mù sương (tr. 157). Đó là chỗ công suất chạm vào ổn định.

**Không có "người dùng đồng thời".** Một khung bên lề tháo ngòi con số 25.000:

> [!quote] Release It! — Ch.7 (tr. 153)
> "There is no such thing as a “concurrent user.”"
>
> *Không có thứ gọi là "người dùng đồng thời".*

Không có kết nối lâu dài, chỉ có chuỗi xung rời rạc mà server nối lại bằng **session**. Server không phân biệt được người sẽ không bao giờ bấm nữa với người chưa bấm, nên giữ session thêm vài phút:

> [!quote] Release It! — Ch.7 (tr. 153)
> "That means the session is absolutely guaranteed to last longer than the user. Counting sessions overestimates the number of users."
>
> *Nghĩa là session chắc chắn sống lâu hơn người dùng. Đếm session là đếm dư số người dùng.*

**Hậu quả.** CDN chuộc lỗi bằng một trang cổng: đẩy trình duyệt không nhận cookie sang trang hướng dẫn; một **van tiết lưu** cho x% session mới vào (đặt 25% thì chỉ 25% thấy trang chủ thật); và chặn IP. Suốt ba tuần có kỹ sư canh số session để kéo van, vì server quá tải hẳn thì mất gần một giờ mới phục vụ lại (tr. 158). Trang chủ sinh động năm triệu lần mỗi ngày, lần nào cũng y hệt, mỗi lần hơn 1.000 giao dịch database; đội làm bản tĩnh cho khách chưa định danh (tr. 158–159). Một sysadmin trực 36 giờ liền dựng sáu máy mượn, gấp đôi tầng application server trong hai ngày (tr. 159); [Bài 1 — Ổn định](bai_01_on_dinh.md) có một cảnh rất giống ở Ch.4 (kỹ sư Todd, tr. 96). Session bị nhét cả giỏ hàng và tới 2.000 kết quả tìm kiếm, nên đành tắt failover (tr. 160).

> [!quote] Release It! — Ch.7 (tr. 160)
> "First, nothing is as permanent as a temporary fix."
>
> *Thứ nhất, không gì lâu dài bằng một bản vá tạm.*

Phần lớn bản vá ở lại một hai năm, và tất cả đều tốn tiền: khách bị van chặn ít đặt hàng hơn, khách đang thanh toán trên instance chết bị đẩy về giỏ và phần lớn bỏ đi, trang tĩnh làm khó cá nhân hoá vốn là mục tiêu gốc, cộng chi phí cơ hội của một năm vá (tr. 160).

> [!quote] Release It! — Ch.7 (tr. 160)
> "The worst part is that no amount of those losses were necessary."
>
> *Tệ nhất là chẳng khoản mất mát nào trong đó là cần thiết.*

Hơn hai năm sau, site chịu tải gấp hơn bốn lần trên ít máy hơn, không thay phần cứng: chỉ phần mềm đã tốt lên (tr. 160).

## 3. Bốn chữ phải tách bạch

Sếp hỏi "site có nhanh không?", khách hỏi "chịu được bao nhiêu người?". Hai câu đó không cùng một đại lượng. Và công suất không chỉ đến từ phần cứng: Nygard từng thấy một hệ, sau mười tám tháng, chịu "four times the demand with two-thirds of the original hardware", hoàn toàn nhờ đổi thiết kế phần mềm (tr. 161). Ông định nghĩa (tr. 161–162):

- **Hiệu năng (performance):** hệ xử lý *một* giao dịch nhanh tới đâu. Người dùng cuối chỉ quan tâm giao dịch của mình; quá kỳ vọng là với họ hệ "sập".
- **Thông lượng (throughput):** số giao dịch trong một khoảng thời gian, luôn bị giới hạn bởi một **nút cổ chai**; tối ưu chỗ khác không tăng thông lượng.
- **Khả năng mở rộng (scalability):** Nygard dùng theo nghĩa các cách thêm công suất cho hệ.
- **Công suất (capacity):**

> [!quote] Release It! — Ch.8 (tr. 162)
> "Finally, the maximum throughput a system can sustain, for a given workload, while maintaining an acceptable response time for each individual transaction is its capacity."
>
> *Cuối cùng, thông lượng tối đa mà hệ duy trì được, với một khối lượng công việc cho trước, trong khi vẫn giữ thời gian đáp ứng chấp nhận được cho từng giao dịch, là công suất của nó.*

Vì có biến số, không có "con số công suất" cố định: workload đổi (mùa lễ chẳng hạn) thì công suất có thể khác hẳn. Và "chấp nhận được" là phán đoán: bán lẻ quá hai giây là khách bỏ đi, sàn tài chính tính bằng mili giây, đặt chỗ du lịch có thể cho 500 ms với tra cứu nhưng ba mươi giây để xác nhận (tr. 162).

## 4. Chỉ một ràng buộc quyết định công suất

"Xử lý 10.000 người dùng ở 50% CPU, vậy chịu được 20.000 đúng không?" Bộ não giải phương trình vi phân đủ nhanh để bắt bóng, nhưng bàn tới công suất thì ai cũng muốn chiếu tuyến tính (tr. 162–163).

> [!quote] Release It! — Ch.8 (tr. 163)
> "In every system, exactly one constraint determines the system’s capacity."
>
> *Trong mọi hệ thống, đúng một ràng buộc quyết định công suất của hệ.*

Ràng buộc là thứ chạm trần đầu tiên; chạm rồi thì mọi phần khác xếp hàng hoặc đánh rơi việc. Oracle có năm mươi tiến trình thì request thứ năm mươi mốt phải chờ, application server và web server ngồi không. Nếu ràng buộc là RAM application server thì nó bắt đầu paging, còn database "được dịp ngả lưng" (tr. 163).

> [!quote] Release It! — Ch.8 (tr. 163)
> "Any nonconstraint metric is useless for projecting or increasing capacity."
>
> *Mọi số đo không phải ràng buộc đều vô dụng để dự báo hay tăng công suất.*

Mượn tư duy hệ thống của Peter Senge: tìm **biến dẫn** (ví dụ "số request trang mỗi giây"; mẹo để tìm ở cấp toàn hệ là nhìn những thứ ngoài tầm kiểm soát: nhu cầu người dùng, đồng hồ, lịch) và **biến theo** (mọi số đo hiệu năng đo được: CPU, bộ nhớ, I/O, băng thông), với hệ số tương quan khoảng 0,8 tới 1,0 (tr. 163–164). Xuống từng tầng thì vai trò đổi: I/O database dẫn thời gian đáp ứng của application server, cái này dẫn bộ nhớ web server (tr. 164). Trước khi chạm trần, biến ràng buộc tương quan chặt với biến dẫn; chạm rồi thì tương quan gãy, sinh ra **"cái đầu gối"** trên biểu đồ tải. Muốn tăng công suất: tăng tài nguyên của biến ràng buộc, hoặc bớt dùng nó (tr. 164).

```
 thông lượng
    │            ●●●●●●  ← chạm ràng buộc: tải tăng, phục vụ không tăng
    │        ● "đầu gối"
    │     ●
    │  ●                    (sơ đồ của khoá, theo tr. 164)
    └──────────────────── tải (biến dẫn)
```

Tầng này là nhân, tầng kia là quả: tầng quá tải thì chậm, và "đáp ứng chậm còn tệ hơn không đáp ứng", vì nó có thể châm lỗi dây chuyền ở tầng khác. Vụ Ch.7 là vấn đề công suất dẫn thẳng tới vấn đề ổn định (tr. 165).

## 5. Rộng ra hay to lên

**Mở rộng ngang** là thêm máy ("getting wide"), **dọc** là nâng máy ("getting big") (tr. 165). Máy nào đặt được sau load balancer thì mở rộng ngang được; tốt nhất là **shared-nothing**, mỗi máy không cần biết máy khác, gấp đôi máy gần gấp đôi công suất, trừ khi tải thêm "nện" gục một dịch vụ khác. Cụm cũng mở rộng ngang nhưng kém tuyến tính vì chi phí quản lý cụm (tr. 165). Database thì ngược lại: cụm ba máy trở lên rất cồng kềnh, tốt hơn là một cặp máy khoẻ có failover (tr. 165). Hết chỗ cắm CPU là phải **forklift upgrade**, thay cả khung. Kiến trúc dọc có chi phí ban đầu cao hơn; kiến trúc ngang cho bắt đầu nhỏ và chi dần, tận dụng giá trị thời gian của tiền (tr. 166–167).

## 6. Ba ngộ nhận "rẻ" và hệ số nhân

Trưởng vận hành tin hệ sập mỗi khi ông mặc áo Hawaii thì có khi đừng cãi; nhưng có những mê tín làm công ty mất hàng triệu đô (tr. 166).

**"CPU rẻ"**, như bảo "bơ đậu phộng rẻ nên phết gấp ba" (tr. 167).

> [!quote] Release It! — Ch.8 (tr. 167)
> "The silicon microchips themselves might be cheap (relative to times past, anyway), but CPU cycles are not cheap."
>
> *Bản thân con chip silicon có thể rẻ (ít nhất là so với ngày trước), nhưng chu kỳ CPU thì không rẻ.*

Chu kỳ là thời gian, thời gian là độ trễ. Thêm 250 ms mỗi giao dịch, một triệu giao dịch mỗi ngày, là 69,4 giờ tính toán mỗi ngày; với hệ số tải 80% mỗi máy, cần thêm bốn máy (tr. 167–168). *Khoá tính lại:* 250.000 s ≈ 69,4 giờ ≈ 2,9 máy chạy suốt ngày; chia 0,8 ra khoảng 3,6, làm tròn thành 4. Độ trễ ở application server còn hại web server, vốn phải giữ socket và bộ nhớ trong lúc chờ: "CPU của application server dẫn thẳng bộ nhớ web server" (tr. 168). Và CPU thứ năm trên máy bốn khe đắt phi tỉ lệ vì phải mua cả khung mới. Với máy nhập môn Sun v440, chênh lệch nhỏ: CPU thứ ba đắt khoảng 1,2 lần CPU thứ hai (tr. 168). Máy lớn thì khác hẳn: khung Sun E25K tối thiểu hơn một triệu đô: "bạn chắc chắn muốn biết mình cần nó trước khi cam kết tới CPU thứ 73" (tr. 168–169).

**"Ổ đĩa rẻ."** Dưới năm mươi xu mỗi gigabyte năm 2007 (tr. 169). Nhưng:

> [!quote] Release It! — Ch.8 (tr. 170)
> "Storage is more of a service than a piece of commodity hardware in today’s large enterprise."
>
> *Trong doanh nghiệp lớn ngày nay, lưu trữ là một dịch vụ hơn là một món phần cứng phổ thông.*

1 GB phải mua lại cho mỗi máy: hai mươi máy là 20 GB, RAID 1 nhân đôi thành 40 GB, cộng sao lưu có thể tràn cửa sổ thời gian. Đĩa cục bộ dưới một đô mỗi gigabyte, **lưu trữ được quản lý** có thể bị tính tới 7 đô (tr. 171). Khung bên lề phân biệt NAS (thiết bị trên mạng IP, dưới 700 đô cho 500 GB) với SAN (mạng Fibre Channel riêng, ít nhất một triệu đô, "quyết định cấp CIO") (tr. 172).

**"Băng thông rẻ."** Cặp đường OC3 cho 310 Mb/s lý thuyết giá 15.000 tới 24.000 đô mỗi tháng; đường burstable vượt mức cam kết thì tính theo megabit-phút, "bị Slashdot thì giữ chặt ví" (tr. 171–173). Người dùng băng rộng ngốn phần băng thông lớn hơn vì TCP kéo nhanh nhất có thể. Và hệ số nhân: 1.024 byte rác mỗi trang × một triệu trang mỗi ngày là gần một gigabyte vô ích (tr. 173).

> [!note] Mở rộng — một con số trong sách không khớp phép chia
> Sách viết ước tính nhanh cho thấy phục vụ được "thirteen times as many" người dùng dial-up (38–39 Kbps) so với cable modem (6 Mbps) (tr. 173). *Khoá tính lại:* 6.000 / 39 ≈ 154 lần. Sách có thể dùng giả định không nêu, hoặc có lỗi; kết luận định tính không đổi.

**Tổng kết Ch.8.** Mô hình tuyến tính sẽ dắt bạn lạc và tốn tiền (tr. 174). Câu chốt:

> [!quote] Release It! — Ch.8 (tr. 174)
> "Capacity is fundamentally a measure of how much revenue the system can generate during a given period of time."
>
> *Về bản chất, công suất là thước đo hệ thống có thể tạo ra bao nhiêu doanh thu trong một khoảng thời gian.*

Bảy lời khuyên (tr. 174): luôn tìm hệ số nhân, "chúng sẽ chi phối chi phí của bạn"; hiểu tầng này tác động tầng kia; cải thiện số đo không phải ràng buộc không cải thiện công suất; làm nhiều việc nhất khi không ai chờ; đặt giới hạn an toàn cho mọi thứ; bảo vệ luồng xử lý request; giám sát công suất liên tục.

## 7. Vì sao phản mẫu công suất cứ bị làm lại

> [!quote] Release It! — Ch.9 (tr. 175)
> "These capacity antipatterns make your applications do more work than necessary, turning electricity into heat instead of revenue."
>
> *Các phản mẫu công suất này bắt ứng dụng làm nhiều việc hơn cần thiết, biến điện thành nhiệt thay vì thành doanh thu.*

Ch.9 có **mười** phản mẫu (9.1 tới 9.10). Mục tổng kết giải thích vì sao chúng tái diễn: phần lớn lập trình viên có dưới mười năm kinh nghiệm, dự án phần lớn nhỏ, nên kinh nghiệm với hệ cực lớn hiếm; đại học không dạy, ở đó "tối ưu" là chỉnh một thuật toán tìm kiếm (tr. 203).

> [!quote] Release It! — Ch.9 (tr. 203)
> "Nobody deliberately selects a design with the purpose of harming the system’s capacity; instead, they select a functional design without regard to its effect on capacity."
>
> *Không ai cố tình chọn thiết kế để hại công suất; họ chọn một thiết kế chạy đúng chức năng mà không đoái hoài tới tác động lên công suất.*

## 8. Phản mẫu 1: Tranh chấp pool tài nguyên

Nygard "vừa yêu vừa ghét" connection pool: mở kết nối database mất tới 250 ms, nên đáng dùng lại, nhưng:

> [!quote] Release It! — Ch.9 (tr. 176)
> "Left untended, however, resource pools can quickly become the biggest bottleneck in an application."
>
> *Nhưng bỏ mặc thì pool tài nguyên có thể nhanh chóng thành nút cổ chai lớn nhất của ứng dụng.*

Phần lớn pool chặn luồng vô thời hạn khi hết tài nguyên. Hình 9.1: với pool bốn kết nối, tới ba mươi request thì hơn 80% thời gian CPU là chờ vô ích; Hình 9.2: thông lượng bẹt ra khi số luồng vượt số tài nguyên, lại là cái đầu gối (tr. 176–178). Cho pool bằng số luồng thì đẩy vấn đề sang database: hai mươi máy × năm instance × năm mươi kết nối = 5.000 kết nối, mỗi cái 1 MB là 5 GB RAM chỉ cho kết nối, trong khi một phần trong số đó ngồi không phần lớn thời gian (tr. 177).

Chặn vô thời hạn "bảo đảm" một vấn đề ổn định (Blocked Threads, xem [Bài 1 — Ổn định](bai_01_on_dinh.md)); pool nên chặn có hạn, code phải sẵn sàng nhận null hoặc ngoại lệ, và cần theo dõi số lần bị chặn, mức cao nhất số kết nối đã mượn (tr. 178–179).

> [!quote] Release It! — Ch.9 (tr. 179)
> "During “regular peak” operation, there should be no contention for resources."
>
> *Ở mức "đỉnh thường ngày", không được có tranh chấp tài nguyên.*

Dù vậy, lời khuyên của Nygard là **nếu được, cho pool bằng số luồng xử lý request**: luôn có sẵn tài nguyên thì không mất hiệu suất; kết nối thêm chủ yếu tốn RAM của database, đắt nhưng vẫn rẻ hơn doanh thu mất đi (tr. 179). Chỉ cần kiểm chắc một database chịu nổi số kết nối tối đa, vì khi failover, một nút database gánh mọi truy vấn và mọi kết nối; và vòng xoáy tranh chấp làm giao dịch dài ra, giao dịch dài làm tranh chấp nhiều hơn (tr. 179).

## 9. Phản mẫu 2: Quá nhiều mảnh JSP

Một site có hơn 25.000 mảnh JSP, phần lớn là nội dung khuyến mãi, chẳng mảnh nào được cho nghỉ hưu (tr. 181). Mỗi JSP biên dịch thành lớp nạp vào **permanent generation**, và server J2EE thường chạy với `-noclassgc`, không dỡ lớp. Không giới hạn số JSP thì không giới hạn vùng nhớ cần, và nó sẽ đầy; bỏ cờ đó thì từ hiệu năng xuống dốc tới mức "không phân biệt được với sập" chuyển thành thấp hơn nhưng ổn định (tr. 180).

> [!quote] Release It! — Ch.9 (tr. 181)
> "In this case, the JSPs did not even need to be executable code. They presented only static content."
>
> *Trong trường hợp này, JSP thậm chí không cần là mã chạy được. Chúng chỉ trình bày nội dung tĩnh.*

**Điều rút ra** (tr. 180–181): "Don’t use code for content"; lẽ ra nên dùng mảnh HTML với kho nội dung có cache.

## 10. Phản mẫu 3: Lạm dụng AJAX

Nygard từng thấy một site dựng trên "trang chủ AJAX" duy nhất: nút Back đưa người dùng ra khỏi site, trang thay đổi như ngẫu nhiên. "Kinh khủng" (tr. 182–183).

> [!quote] Release It! — Ch.9 (tr. 182)
> "AJAX is a technique, not a goal."
>
> *AJAX là một kỹ thuật, không phải mục tiêu.*

Người dùng thường "nghĩ" năm tới mười giây giữa hai lần bấm; với AJAX, khoảng cách giữa các request còn một tới ba giây, dù request và phản hồi nhỏ hơn (tr. 182).

> [!quote] Release It! — Ch.9 (tr. 182)
> "Used well, it can reduce your bandwidth costs. Used poorly, AJAX techniques will place more burden on the web server and application server layers."
>
> *Dùng khéo, nó giảm chi phí băng thông. Dùng vụng, nó đè thêm gánh nặng lên tầng web server và application server.*

Cách dùng không tự cứa tay (tr. 183–184): chỉ cho tương tác là *một* việc trong đầu người dùng; autocomplete gửi sau khi ngừng gõ (thường 500 ms), không phải mỗi phần tư giây; bật session affinity; trả JSON thay vì HTML (và đừng `eval()` JSON); tăng số kết nối tầng web. **Điều rút ra** nối thẳng với Ch.7: request AJAX phải kèm ID session, "nếu không, application server sẽ tạo một session mới, phí phạm, cho mỗi request AJAX" (tr. 184).

## 11. Phản mẫu 4: Session ở lì

Đang đọc dở một sản phẩm, bạn xem một tập *24*, quay lại thì bị đá về vạch xuất phát (tr. 186). Gốc rễ: đặc tả Servlet chọn mặc định session sống ba mươi phút sau request cuối, trong khi application server Java luôn thiếu bộ nhớ; session là mối đe doạ tỉ lệ thuận với thời gian nó nằm trong bộ nhớ (tr. 185).

> [!quote] Release It! — Ch.9 (tr. 185)
> "The common default timeout of thirty minutes is overkill."
>
> *Mức timeout mặc định ba mươi phút thường gặp là quá tay.*

Cách chỉnh: đo trung bình và độ lệch chuẩn khoảng cách giữa các request vẫn coi là một session, đặt timeout bằng trung bình cộng một độ lệch chuẩn; thực tế khoảng mười phút cho bán lẻ, năm cho cổng media, tới hai mươi cho du lịch (tr. 185). Tốt hơn là làm session **không cần thiết**: nếu mọi thứ trong đó chỉ là bản sao của trạng thái bền vững, session thành cache, bỏ và dựng lại lúc nào cũng được. Ông "tán thành mạnh mẽ" mô hình này (tr. 185–186).

> [!quote] Release It! — Ch.9 (tr. 186)
> "Only developers get the idea behind sessions. Users do not appreciate being put on the clock."
>
> *Chỉ dev mới hiểu ý tưởng đằng sau session. Người dùng chẳng thích bị bấm giờ.*

Không nên có giỏ hàng "tạm thời"; ngoại lệ duy nhất là dữ liệu tài chính nhạy cảm. Và: giữ khoá, đừng giữ cả đối tượng (tr. 186).

## 12. Phản mẫu 5: Byte thừa trong HTML

Một trang chủ ghép từ hơn 100 mảnh JSP ra hơn 600 KB HTML, một phần ba là xuống dòng trên dòng toàn dấu cách. Web server đệm trang nên khoảng trắng ăn thêm 200 KB bộ nhớ mỗi request, giảm công suất cả site; riêng tiền băng thông lẽ ra hơn 15.000 đô mỗi năm (tr. 188).

> [!quote] Release It! — Ch.9 (tr. 187)
> "You should not excuse inefficiency."
>
> *Đừng bao biện cho sự kém hiệu quả.*

50 KB thừa đi qua card mạng, switch, tường lửa, web server, lại tường lửa, router, ở mỗi bước tốn RAM hoặc băng thông; trang to thì kết nối mở lâu, và người dùng tranh chấp kết nối web server y như luồng tranh chấp kết nối database (tr. 187–188).

> [!quote] Release It! — Ch.9 (tr. 188)
> "Bloat is never invited; it sneaks in where nobody looks."
>
> *Không ai mời sự phình to; nó lẻn vào chỗ không ai nhìn.*

Ba nguồn (tr. 188–190): **khoảng trắng** quanh thẻ template (lọc bằng interceptor; Nygard thường thấy CPU để lọc rẻ hơn RAM và băng thông của việc không lọc); **ảnh spacer** (53 byte thay bằng `&nbsp;` 5 byte; 48 × 12 chỗ × một triệu trang = 576.000.000 byte mỗi ngày, chưa kể mỗi ảnh là một request); **bảng dàn trang** (CSS tải một lần, bảng gửi lại mỗi trang).

## 13. Phản mẫu 6: Nút Reload

> [!quote] Release It! — Ch.9 (tr. 191)
> "I swear, sometimes users are the worst thing that can happen to a system."
>
> *Thề là có lúc người dùng là điều tệ nhất có thể xảy ra với một hệ thống.*

Site đang chậm, ai đó dính một lần full GC mười lăm giây. Không thấy trang trong mười giây là dễ bấm Reload: trình duyệt bỏ kết nối cũ, bắn request mới, nhưng không ai bảo application server dừng request cũ. Nếu request có giao dịch, request thứ hai có thể chờ request đầu, tệ hơn là deadlock (tr. 191).

> [!quote] Release It! — Ch.9 (tr. 191)
> "There is no good answer about what to do with the Reload button. Just make sure your site is fast enough that users don’t click it."
>
> *Không có câu trả lời hay cho nút Reload. Chỉ cần bảo đảm site đủ nhanh để người dùng không bấm nó.*

Khung bên lề bác cách chữa "mỗi IP một request một lúc": qua Akamai hay proxy công ty thì mọi request chung IP, và người đã bấm Reload chỉ phải nhìn logo quay lâu hơn. Request thứ hai còn có thể tới server khác, nên code phải chịu được một người chạy cùng giao dịch nhiều lần mà không deadlock (tr. 192).

## 14. Phản mẫu 7: SQL viết tay

ORM sinh SQL đoán trước được nên DBA tinh chỉnh được. Xuống SQL tay thường với lý do hiệu năng, vậy sao lại là sát thủ công suất?

> [!quote] Release It! — Ch.9 (tr. 193)
> "Well, it’s mainly because object-oriented developers do weird, wonderful, and torturous things to a perfectly innocent database."
>
> *Chủ yếu là vì dev hướng đối tượng làm những trò kỳ quặc, tuyệt diệu và tra tấn với một cơ sở dữ liệu hoàn toàn vô tội.*

Bốn lỗi thường gặp (tr. 193–194): join trên cột không index; join quá nhiều bảng; coi SQL là ngôn ngữ thủ tục, join năm bảng lấy một dòng rồi lặp thêm 100 lần; và lạm dụng tính năng. Ông từng thấy union tám nhánh, mỗi nhánh join năm bảng qua cột không index, kế hoạch truy vấn có khoảng bốn mươi lần quét bảng. Chú thích dặn coi chừng **N+1** của ORM: một truy vấn lấy danh sách rồi mỗi phần tử một truy vấn (tr. 193). Dev không thấy hiệu ứng vì dữ liệu nhỏ; DBA nào cũng có chuyện một tiến trình từ mười tám giờ xuống ba phút chỉ nhờ thêm một index hoặc cập nhật thống kê bảng. Cần dữ liệu cỡ thật, đã scrub, hoặc viết bộ sinh dữ liệu (tr. 194). SQL động ghép WHERE thì để cho hệ báo cáo:

> [!quote] Release It! — Ch.9 (tr. 194)
> "You cannot make it respond well to every possible query."
>
> *Bạn không thể khiến nó đáp ứng tốt với mọi truy vấn có thể có.*

**Điều rút ra** (tr. 195): "Không qua được phép thử tiếng cười (của DBA) thì đừng đưa lên production".

## 15. Phản mẫu 8: Cơ sở dữ liệu phú dưỡng

Hồ nước "già" qua quá trình **phú dưỡng**: bùn từ vi sinh chết, cá thối, tảo tích dần tới khi hết oxy và hồ chết. Với database, thứ ngửa bụng là hệ thống của bạn (tr. 196). Dữ liệu test "bé tới mức buồn cười" khiến schema lọt lên production chưa từng chịu khối lượng lớn.

**Index.** Quan hệ khai báo trong mapping ORM không qua DBA duyệt, nên dễ thiếu index; với dữ liệu đồ chơi quét bảng thậm chí nhanh nhất, một hai năm sau người dùng chờ hàng phút. Cột nào là đích của liên kết ORM thì nên có index (tr. 196–197). **Phân vùng.** Ước lượng tăng trưởng thường sai: một hệ từ 1 GB log kiểm toán mỗi năm thành 1 GB mỗi ngày sau một bản phát hành. Chia bảng theo cột ít giá trị (ví dụ "thứ trong tuần" thành bảy phân vùng) để tổ chức lại từng phần mà không dừng hệ (tr. 197). **Dữ liệu lịch sử.**

> [!quote] Release It! — Ch.9 (tr. 198)
> "In particular, reporting and ad hoc analysis should never be done in the production database."
>
> *Đặc biệt, báo cáo và phân tích tuỳ hứng không bao giờ được làm trên database production.*

Schema **OLTP** tối ưu cho ghi nhanh, không cho báo cáo; phân tích nên ở kho dữ liệu thật; lưu trữ nhiều tầng giữ lịch sử trên hệ rẻ (tr. 198).

> [!quote] Release It! — Ch.9 (tr. 198)
> "Over and above all else is this: a rigorous regimen of data purging is vital to the long-term stability and performance of your system."
>
> *Trên hết thảy là điều này: một chế độ dọn dữ liệu nghiêm ngặt là sống còn với sự ổn định và hiệu năng lâu dài của hệ thống.*

Và: vòng index đầu tiên là trách nhiệm của dev, không chỉ của DBA (tr. 198).

## 16. Phản mẫu 9: Độ trễ ở điểm tích hợp

Một hệ Java fat-client dùng RMI; người dùng Anh đòi server và kho dữ liệu riêng, khoản đầu tư hàng triệu đô, vì:

> [!quote] Release It! — Ch.9 (tr. 200)
> "We found that expanding a node in the hierarchy (a tree control), which took less than a second for U.S. users, took twenty minutes from the United Kingdom!"
>
> *Chúng tôi thấy việc mở một nút trong cây, dưới một giây với người dùng Mỹ, mất hai mươi phút từ Vương quốc Anh!*

Thủ phạm là "1+N": một lời gọi xin danh sách con, rồi gọi mỗi con ba lần. Thêm một phương thức trả "Summary Object" là người Anh có tốc độ dưới một giây, khỏi cần bản sao kho dữ liệu (tr. 200).

> [!quote] Release It! — Ch.9 (tr. 199)
> "A remote call takes at least 1,000 times as long as a local call."
>
> *Một lời gọi từ xa tốn ít nhất gấp 1.000 lần một lời gọi cục bộ.*

Triết lý "trong suốt vị trí" bị bác vì lời gọi xa hỏng theo kiểu khác và dẫn tới giao diện "lắm lời" (tr. 199). Luồng chờ vẫn giữ bộ nhớ, có khi giữ kết nối hay khoá dòng, nên "vấn đề hiệu năng của từng người dùng thành vấn đề công suất của cả hệ thống". Nygard ví độ trễ tích hợp như lợi thế nhà cái trong blackjack: chơi càng nhiều, nó càng chống lại bạn (tr. 199).

## 17. Phản mẫu 10: Quái vật cookie

> [!quote] Release It! — Ch.9 (tr. 201)
> "HTTP cookies stand right there with bottle rockets in the “things that invite you to blow yourself up” category."
>
> *Cookie HTTP đứng ngay cạnh pháo thăng thiên trong hạng mục "những thứ mời bạn tự làm nổ mình".*

RFC 2109 nhắm tới quản lý session (tr. 201). Phản mẫu: tuần tự hoá giỏ hàng của khách ẩn danh vào cookie để khỏi tạo bản ghi database. Vấn đề chồng chất (tr. 201–203): dạng tuần tự hoá có thể cũ hàng tháng, hàng năm, và nhiều khả năng đã hỏng vì một lần đổi code trước khi khách quay lại; sản phẩm có thể đã biến mất; client có thể sửa cookie để mọi giá thành 0,01 đô; và cookie sinh ra cho dưới khoảng 100 byte, đẩy lên 4 KB thì mỗi request gửi lại, qua dây hai (có khi bốn) lần, trong khi băng thông tải lên của người dùng ít hơn tải xuống. Tất cả để né một job dọn giỏ hàng bỏ dở.

> [!quote] Release It! — Ch.9 (tr. 203)
> "Just remember that the client can lie, might send back stale or broken cookies, and might not send the cookies back at all."
>
> *Chỉ cần nhớ rằng client có thể nói dối, có thể gửi lại cookie cũ hoặc hỏng, và có thể không gửi lại cookie nào cả.*

**Điều rút ra** (tr. 203): cookie chứa định danh, không chứa đối tượng; dữ liệu session để ở server.

## 18. Hoare bị trích nửa câu

"Premature optimization is the root of all evil" hay bị dùng làm cớ cho thiết kế cẩu thả. Nygard dẫn đủ câu, bắt đầu bằng "We should forget about small efficiencies, say about 97% of the time": lời cảnh báo nhắm vào việc đuổi lợi ích nhỏ bằng giá phức tạp (tr. 204). Tối ưu hay đến muộn, mà muộn thường là "không bao giờ", và không ai tối ưu từ bubble sort thành quicksort được (tr. 204).

> [!quote] Release It! — Ch.10 (tr. 204)
> "Choosing a better design or an architecture optimized for scaling effects is the opposite of premature optimization; it obviates the need for optimization altogether."
>
> *Chọn thiết kế tốt hơn hay kiến trúc tối ưu cho hiệu ứng quy mô là điều ngược với tối ưu sớm; nó khiến việc tối ưu không còn cần thiết.*

Chuyện thật: code kém khiến một tổ chức lập ngân sách mười triệu đô phần cứng cho một mùa lễ; sửa vài phản mẫu và áp dụng hai mẫu (Precompute Content, Use Caching Carefully) giúp họ tránh khoản đó, tương đương gần một tuần doanh số (tr. 204).

## 19. Mẫu 1: Gộp kết nối

Thời Perl CGI, mỗi script mở rồi đóng kết nối: an toàn, dễ debug, cho tới khi database tốn bằng ấy thời gian quản lý kết nối như xử lý giao dịch (tr. 206). Mở kết nối gồm TCP, xác thực, dựng session database, "dễ dàng mất 400 tới 500 ms" (tr. 206). *Ghi chú của khoá:* Ch.9 nói "up to 250 milliseconds" (tr. 176); tổng kết 10.5 lại ghi pool bớt "up to 500 milliseconds" mỗi giao dịch (tr. 217). Sách không giải thích sự chênh, nhưng bậc độ lớn là hàng trăm mili giây.

> [!quote] Release It! — Ch.10 (tr. 206)
> "There really is no excuse not to use it, except if you do it poorly."
>
> *Thật sự không có lý do gì để không dùng nó, trừ khi bạn dùng dở.*

Dùng dở ra sao? Kết nối hỏng bị mượn, gây lỗi, bị trả; kết nối tốt bận làm việc thật nên bị giữ lâu hơn; thế là kết nối hỏng hay "rảnh" hơn:

> [!quote] Release It! — Ch.10 (tr. 206)
> "One bad connection out of ten will cause more than 10% of requests to error out."
>
> *Một kết nối hỏng trong mười sẽ làm hơn 10% request lỗi.*

Pool nhỏ quá thì tranh chấp, to quá thì đè database (tr. 206). Ba chiến lược (tr. 206–207): **per-page** (mượn cho cả trang, an toàn trước deadlock, cần nhiều kết nối), **per-fragment** (mỗi mảnh tự mượn trả, thông lượng cao hơn, dễ deadlock hơn), **lai** (mảnh tự quản kết nối, cả trang một giao dịch; khó debug vì mảnh sau thấy dữ liệu chưa commit của mảnh trước). Chiến lược nào cũng phải giám sát tranh chấp, và mọi lệnh mượn phải có timeout (tr. 207).

## 20. Mẫu 2: Dùng cache cẩn thận

Nygard từng thấy cache có hàng trăm mục chỉ chứa một dấu cách: một mảnh JSP kiểm tra cờ "có phải nhân viên không", phần lớn là sai nên ra rỗng, và kết quả rỗng được cache riêng cho từng người (tr. 208).

> [!quote] Release It! — Ch.10 (tr. 208)
> "Keeping something in cache is a bet that the cost of generating it once, plus the cost of hashing and lookups, is less than the cost of generating it every time it is needed."
>
> *Giữ thứ gì trong cache là đặt cược rằng chi phí sinh nó một lần, cộng chi phí băm và tra cứu, nhỏ hơn chi phí sinh nó mỗi lần cần.*

Nguyên tắc (tr. 208–209): giới hạn bộ nhớ của mọi cache, nếu không GC sẽ tốn ngày càng nhiều thời gian thu hồi bộ nhớ và cache thành thủ phạm làm chậm; theo dõi tỉ lệ trúng; đừng cache thứ rẻ hay thứ đổi trước khi được dùng lại; trong Java dùng `SoftReference`; cache nhiều tầng cho đối tượng rất lớn; và mọi cache cần chiến lược vô hiệu hoá (hàng trăm server thì cần hàng đợi hoặc multicast, coi chừng mọi server cùng nện database để nạp lại). Xả cache cũng đắt, nên giới hạn tần suất, kẻo tự gây "attacks of self-denial" (tr. 209).

## 21. Mẫu 3: Tính trước nội dung

Chuyện "Profanity Masker" từ chính vụ Ch.7. Thống kê GC cho thấy gần 10 MB rác mỗi request trang. Nygard tìm ra người viết và hét "0x7f" vào mặt anh ta ("tôi hex anh ta", chơi chữ *hexed*: bỏ bùa). Một droplet ATG bọc tên, mô tả, thông số, từng tên bài hát, tới hai mươi lần một trang, tách từng từ so với mười một từ tục trong một `Vector` rồi ghép lại, hơn năm triệu lượt xem mỗi ngày (tr. 211).

> [!quote] Release It! — Ch.10 (tr. 211)
> "Was there some chance that dirty words would spontaneously appear during the day?"
>
> *Có khả năng nào từ tục tự dưng mọc ra giữa ngày không?*

Nội dung được xuất bản mỗi đêm. Đoạn kết: người phụ trách nội dung nổi đoá vì nội dung có bản quyền, hợp đồng cấm sửa. Họ gỡ bộ che, và không bao giờ biết vì sao nó được viết ra (tr. 212).

Nguyên lý: đoạn code dựng menu danh mục có lẽ chạy một triệu lần mỗi ngày, trong khi danh mục cấp cao có khi ba tháng mới đổi, thay đổi nhỏ có thể hàng tuần (tr. 210). "Tại sao phải render HTML làm gì?" Slashdot và Fark tính trước trang chính; mỗi phiên bản được xem hàng trăm, hàng nghìn lần trước lần cập nhật kế (tr. 210–211). Cá nhân hoá chống lại tính trước, nhưng nếu chỉ vài mảnh cá nhân hoá thì chừa một **"punch out"** (tr. 212). Tính trước khác cache mảnh trang trong bộ nhớ, vốn có thể làm server thrashing và bắt người đầu tiên chờ cache nguội hàng phút (tr. 212–213).

> [!quote] Release It! — Ch.10 (tr. 213)
> "Factor the cost of generating the content out of individual requests and into the deployment process."
>
> *Rút chi phí sinh nội dung ra khỏi từng request và chuyển nó vào quy trình triển khai.*

## 22. Mẫu 4: Tinh chỉnh bộ gom rác

> [!quote] Release It! — Ch.10 (tr. 214)
> "An untuned application running at production volumes and traffic will probably spend 10% of its time collecting garbage. That should be reduced to 2% or less."
>
> *Một ứng dụng chưa tinh chỉnh chạy ở khối lượng production có lẽ sẽ tốn 10% thời gian gom rác. Con số đó nên giảm xuống 2% hoặc thấp hơn.*

Phần lớn đối tượng chết ngay, số ít sống bằng tuổi chương trình. Đối tượng sinh ra ở **eden**, sống sót sang **survivor** (cùng thuộc thế hệ trẻ), lâu hơn lên **tenured** (tr. 214). Nhìn GC bằng `-verbosegc` hay `jconsole`, rồi chỉnh kích thước heap và tỉ lệ các thế hệ; tiện thể hay lòi ra rò rỉ bộ nhớ (tr. 214–215). Mỗi bản phát hành có thể đổi hành vi người dùng, nên cấu hình của bản này có thể sai ở bản sau (tr. 215).

> [!quote] Release It! — Ch.10 (tr. 217)
> "User access patterns make a huge difference in the optimal settings, so you can’t tune the garbage collector in development or QA."
>
> *Kiểu truy cập của người dùng tạo khác biệt rất lớn cho cấu hình tối ưu, nên bạn không thể tinh chỉnh GC ở dev hay QA.*

Khung "Joe Asks": thời Java 1.2 người ta tin tạo đối tượng rất đắt nên pool đối tượng. Bảng đo trên JDK 1.4.2 cho thấy overhead khi pool (20,30% / 31,46% / 24,69% trên ba hệ điều hành) cao hơn khi tạo mới (10,17% / 23,42% / 15,69%). Chỉ pool thứ thật sự đắt: kết nối mạng, kết nối database, luồng worker (tr. 216–217).

## 23. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống.**
> - *Ràng buộc và hệ số nhân, nay được cơ khí hoá.* **Kubernetes HorizontalPodAutoscaler** tự cập nhật số Pod "để khớp công suất với nhu cầu", vòng điều khiển mặc định 15 giây, công thức `desiredReplicas = ceil(currentReplicas × currentMetric / desiredMetric)`. *Nhận định của khoá:* HPA chỉ tăng số Pod trên các node sẵn có; việc cấp máy (thứ ca trực 36 giờ ở Ch.7 phải làm tay) thuộc về node autoscaler, nằm ngoài phạm vi trang này. Công thức tuyến tính theo một số đo, thường là CPU; nếu ràng buộc thật là database, thêm Pod chỉ nhân thêm kết nối đè lên nó (tr. 163, 177).
> - *Tranh chấp pool vẫn là chuyện thường.* **PgBouncer** thêm một tầng pool trước PostgreSQL, ba chế độ session, transaction, statement, khoảng 2 kB mỗi kết nối. *Nhận định của khoá:* đó là một cách giảm phép nhân 20 × 5 × 50 ở tr. 177.
> - *Kiểm thử tải "lịch sự".* Tài liệu **Grafana k6** nói rõ: ở mô hình đóng, khi hệ chậm, bài test "chờ" và tốc độ đến giảm dần (coordinated omission); mô hình mở với `constant-arrival-rate` / `ramping-arrival-rate` giữ tốc độ đến bất kể hệ trả lời chậm. *Nhận định của khoá:* bot ở Ch.7 hành xử giống một mô hình mở.
> - *Nút Reload.* Stripe hỗ trợ **idempotency key**: lưu kết quả request đầu, request lặp cùng khoá nhận đúng kết quả đó, khoá có thể bị dọn sau ít nhất 24 giờ. *Nhận định của khoá:* việc này liên quan, nhưng không trùng, với lời dặn tr. 192 (chịu được cùng một giao dịch chạy nhiều lần mà không deadlock).
>
> **Phần cần chỉnh.**
> - *Định cỡ pool: HikariCP ngược hướng với Nygard.* Nygard muốn không có tranh chấp ở đỉnh thường ngày và khuyên, nếu được, cho pool bằng số luồng request (tr. 179). Wiki **HikariCP** thì muốn "a small pool, saturated with threads waiting for connections", tức chấp nhận luồng chờ để database không bị quá tải, với công thức khởi điểm `connections = ((core_count * 2) + effective_spindle_count)`. Wiki mô tả video của Oracle: giảm pool từ 2048 xuống 96; chỉ giảm kích thước pool đã đưa thời gian đáp ứng từ ~100 ms xuống ~2 ms. Phần còn nguyên từ Nygard là mọi lệnh mượn phải có timeout và phải giám sát thời gian chờ.
> - *JSP/AJAX thành SPA, SSR, CDN.* web.dev "Rendering on the Web" (cập nhật 5/1/2026) phân biệt SSR (render trên server, gửi HTML), static rendering (sinh lúc build, đẩy lên CDN để cache ở biên) và CSR (render trong trình duyệt). *Nhận định của khoá:* static rendering họ hàng với "Precompute Content", nhưng không trùng: sách tính trước ở mức mảnh trang và tạo lại khi nội dung đổi, còn web.dev nói về sinh trang lúc build. "Trang chủ AJAX" của tr. 182 gần với SPA thuần CSR.
> - *Session server thành token.* **JWT** (RFC 7519, 5/2015) giải bài RAM của session, nhưng OWASP cảnh báo dùng JWT cho session thì cần giải pháp vô hiệu hoá, và denylist khiến session "không còn hoàn toàn stateless". *Nhận định của khoá:* trạng thái chỉ dời chỗ.
> - *Cookie.* RFC 6265 thay RFC 2965 (vốn thay RFC 2109 Nygard dẫn), khuyến nghị trình duyệt hỗ trợ tối thiểu 4096 byte mỗi cookie và khuyên server dùng ít cookie để tiết kiệm băng thông.
> - *Nén.* MDN khuyên bật nén HTTP cho mọi file trừ loại đã nén; chỉ còn `gzip` và `br` đáng kể. Nén giảm giá khoảng trắng trên đường truyền, nhưng server vẫn sinh và đệm những byte đó.
> - *Dọn dữ liệu.* PostgreSQL (tài liệu bản 18) có partitioning khai báo theo range, list, hash; bỏ phân vùng bằng `DROP TABLE` hay `DETACH PARTITION` nhanh hơn nhiều so với xoá hàng loạt và tránh chi phí `VACUUM`.
>
> **Phần đã lỗi thời.**
> - **JEP 122** (Java 8) bỏ permanent generation, không còn phải chỉnh `-XX:MaxPermSize`: cơ chế của phản mẫu 2 không còn.
> - **JEP 248** (JDK 9) đặt G1 làm GC mặc định trên cấu hình server. "Tinh chỉnh trong production, sau mỗi bản phát hành" vẫn đúng; cờ và tỉ lệ thế hệ kiểu Java 5 thì không.
> - Giá Sun Fire, OC3, SAN, dial-up chỉ còn giá trị lịch sử; mẫu hình "đơn vị thứ n+1 đắt phi tỉ lệ" thì còn.

**Phân loại mười phản mẫu.** Ch.9 có mười phản mẫu (9.1–9.10). Cột "Xếp loại" là nhận định của khoá.

| Phản mẫu (Ch.9) | Xếp loại | Lý do ngắn |
| --- | --- | --- |
| 1. Resource Pool Contention | Còn nguyên | Vẫn tranh chấp; cách định cỡ thì đổi (HikariCP). |
| 2. Excessive JSP Fragments | Đã chết | Hết permanent generation (JEP 122). |
| 3. AJAX Overkill | Đổi dạng | Thành SPA/CSR. |
| 4. Overstaying Sessions | Đổi dạng | Session thành token. |
| 5. Wasted Space in HTML | Đổi dạng | Nén gzip/br; spacer, bảng đã hết. |
| 6. The Reload Button | Còn nguyên | Người dùng vẫn bấm lại. |
| 7. Handcrafted SQL | Còn nguyên | ORM, N+1, dữ liệu dev nhỏ. |
| 8. Database Eutrophication | Còn nguyên | Dữ liệu vẫn phình. |
| 9. Integration Point Latency | Còn nguyên | Gọi mạng vẫn chậm. |
| 10. Cookie Monsters | Đổi dạng | Thành token lớn trong mỗi request. |

## 24. Áp dụng vào việc của bạn

> [!question] Khi thiết kế và viết code
> 1. **Tìm ràng buộc trước khi tối ưu.** Gọi tên biến dẫn của dịch vụ và ba biến theo. Cái nào chạm trần đầu tiên? Đừng chỉnh gì khác cho tới khi trả lời được (tr. 163).
> 2. **Làm phép nhân.** Lấy một chi phí nhỏ (thêm 50 ms, thêm 2 KB phản hồi, thêm một kết nối mỗi instance) nhân với số request mỗi ngày và số instance. Kết quả làm bạn giật mình thì đó là hệ số nhân (tr. 174).
> 3. **Giữ khoá, không giữ đối tượng.** Rà session, token, cookie: có gì ngoài định danh không, và dựng lại được từ nguồn bền vững không (tr. 186, 203)?
> 4. **Viết kịch bản tải bất lịch sự.** Thêm kịch bản không cookie, kịch bản gọi lại cùng URL liên tục, kịch bản tốc độ đến cố định (tr. 157).

> [!question] Khi vận hành, trực on-call, viết postmortem
> 1. **Theo dõi pool như theo dõi CPU.** Có số đo thời gian chờ mượn kết nối, mức cao nhất đã mượn, số lần timeout chưa (tr. 178–179)?
> 2. **Có van tiết lưu chưa?** Gặp đợt bot, bạn có chặn IP hay chỉ cho x% session mới vào ở tầng biên trong vài phút được không (tr. 158)?
> 3. **Ghi hạn cho bản vá tạm.** Trong postmortem, mọi bản vá tạm phải có người chịu trách nhiệm và ngày gỡ (tr. 160).
> 4. **Soát lại sau mỗi bản phát hành.** GC, kích thước pool, ngưỡng autoscaling phụ thuộc hành vi người dùng; lên lịch soát sau mỗi bản lớn và mùa cao điểm (tr. 215, 217).

## 25. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Công suất (capacity)** | Thông lượng tối đa duy trì được với workload cho trước mà vẫn giữ thời gian đáp ứng chấp nhận được (tr. 162). |
| **Hiệu năng / thông lượng** | Tốc độ một giao dịch / số giao dịch trong một khoảng thời gian (tr. 161–162). |
| **Ràng buộc / nút cổ chai** | Thứ chạm trần đầu tiên, quyết định công suất cả hệ (tr. 163). |
| **Biến dẫn / biến theo** | Biến gây ra chuyển động, như request mỗi giây (mẹo tìm: thứ ngoài tầm kiểm soát) / số đo chuyển động theo nó (CPU, I/O) (tr. 163–164). |
| **Cái đầu gối (knee)** | Điểm trên biểu đồ tải nơi thông lượng ngừng tăng (tr. 164, 176). |
| **Hệ số nhân** | Chi phí nhỏ nhân với số request, số máy, số bản sao thành chi phí lớn (tr. 171, 174). |
| **Shared-nothing** | Mỗi máy chạy không cần biết máy khác; mở rộng ngang gần tuyến tính (tr. 165). |
| **Forklift upgrade** | Thay cả khung máy khi hết chỗ nâng cấp dọc (tr. 166). |
| **Lưu trữ được quản lý** | Dung lượng cộng RAID, sao lưu; lưu trữ là dịch vụ (tr. 170–171). |
| **Session** | Định danh nối chuỗi request rời rạc; luôn sống lâu hơn người dùng (tr. 153). |
| **Van tiết lưu (throttle)** | Giới hạn tỉ lệ session mới được vào (tr. 158). |
| **Permanent generation** | Vùng JVM giữ định nghĩa lớp; bị bỏ từ Java 8 (tr. 180, mục 23). |
| **N+1 / 1+N** | Một truy vấn lấy danh sách rồi một truy vấn cho mỗi phần tử (tr. 193, 200). |
| **Phú dưỡng** | Ẩn dụ cho dữ liệu cũ tích tụ làm database chậm dần (tr. 196). |
| **OLTP** | Schema tối ưu cho ghi giao dịch, không hợp báo cáo (tr. 198). |
| **Per-page / per-fragment** | Mượn kết nối cho cả trang / cho từng mảnh (tr. 206–207). |
| **Punch out** | Lỗ chừa trong trang tính trước cho phần cá nhân hoá (tr. 212). |
| **Eden / survivor / tenured** | Các vùng thế hệ của heap Java theo tuổi đối tượng (tr. 214). |
| **HPA, idempotency key** | Không có trong sách; xem mục 23. |

## 26. Câu hỏi tự kiểm tra

1. Kể bốn nguồn session "nhiễu" làm site Ch.7 sập, và vì sao test tải không bắt được. *(tr. 155–157)*
2. Vì sao "không có người dùng đồng thời", và vì sao đếm session là đếm dư? *(tr. 153)*
3. Vì sao không có "con số công suất" cố định? *(tr. 162)*
4. Vì sao nhìn CPU của web server vô ích khi database là ràng buộc? *(tr. 163)*
5. Tính lại 250 ms × một triệu giao dịch và 20 × 5 × 50 kết nối. *(tr. 167–168, 177)*
6. Vì sao một kết nối hỏng trong mười gây hơn 10% lỗi? *(tr. 206)*
7. Tính trước nội dung khác cache mảnh trang trong bộ nhớ ở đâu? *(tr. 212–213)*
8. Chọn hai phản mẫu "đổi dạng" ở mục 23 và chỉ ra hình dạng mới của chúng trong hệ của bạn.

## Tóm tắt một trang

```
BÀI 2 — CÔNG SUẤT: HỆ SỐ NHÂN QUYẾT ĐỊNH TẤT CẢ
────────────────────────────────────────────────────────────────
CA CH.7   9:00 nút đỏ → 9:30 250.000 session → sập (tr. 148)
          Test lịch sự, có cookie; đời thật: spider, scraper, bot,
          URL cũ → session mỗi request, ở lì 30 phút.
          Vá: van tiết lưu ở CDN, trang chủ tĩnh, tắt failover.
          "Nothing is as permanent as a temporary fix." (tr. 160)

CH.8      Công suất = thông lượng tối đa, workload cho trước,
          thời gian đáp ứng chấp nhận được (tr. 162)
          ĐÚNG MỘT ràng buộc quyết định (tr. 163).
          CPU, ổ đĩa, băng thông KHÔNG rẻ: nhìn HỆ SỐ NHÂN.
          Công suất = doanh thu trong một khoảng thời gian (tr. 174)

CH.9      1 pool tranh chấp   2 JSP làm nội dung   3 AJAX quá tay
10 PHẢN   4 session ở lì      5 byte thừa HTML     6 nút Reload
MẪU       7 SQL viết tay      8 DB phú dưỡng       9 trễ tích hợp
          10 cookie khổng lồ

CH.10     Gộp kết nối (timeout) · Cache có giới hạn, có xả
4 MẪU     Tính trước nội dung · Tinh chỉnh GC trong production
          Thiết kế tốt ≠ tối ưu sớm (Hoare đủ câu, tr. 204)

2026      Còn: ràng buộc, hệ số nhân, tranh chấp pool, Reload, SQL.
          Chỉnh: HikariCP muốn pool nhỏ có luồng chờ.
          Đổi: SSR/SSG/CDN, JWT, cookie, gzip/br, partitioning.
          Chết: permanent generation (JEP 122), cờ GC Java 5.
          HPA thêm Pod, nhưng thêm Pod ≠ nới ràng buộc database.
```

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software* (Pragmatic Bookshelf, 2007), `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`:
  - **Part II — Capacity** (`tr. 146`).
  - **Ch.7** (`tr. 147–160`): 7.1 ra mắt (tr. 147–148); 7.2 nhắm vào QA (tr. 148–151); 7.3 kiểm thử tải, "concurrent user" (tr. 152–155); 7.4 đám đông (tr. 155–157); 7.5 lỗ hổng kiểm thử (tr. 157); 7.6 hậu quả (tr. 158–160).
  - **Ch.8** (`tr. 161–174`): định nghĩa (tr. 161–162); ràng buộc (tr. 162–164); tương quan tầng, mở rộng (tr. 165–167); ngộ nhận (tr. 166–173); tổng kết (tr. 174).
  - **Ch.9** (`tr. 175–203`): 9.1 (tr. 176–179); 9.2 (tr. 180–181); 9.3 (tr. 182–184); 9.4 (tr. 185–186); 9.5 (tr. 187–190); 9.6 (tr. 191–192); 9.7 (tr. 193–195); 9.8 (tr. 196–198); 9.9 (tr. 199–200); 9.10 (tr. 201–203); 9.11 (tr. 203).
  - **Ch.10** (`tr. 204–217`): mở đầu (tr. 204–205); 10.1 (tr. 206–207); 10.2 (tr. 208–209); 10.3 (tr. 210–213); 10.4 (tr. 214–217); 10.5 (tr. 217).
  - Quy ước trích: `tr. X` = số trang in = số trang PDF.
- Nguồn web dùng ở Đối chiếu 2026 (truy cập 9/2026):
  - Kubernetes, "Horizontal Pod Autoscaling": https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
  - HikariCP wiki, "About Pool Sizing": https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing
  - PgBouncer, "Features": https://www.pgbouncer.org/features.html
  - Grafana k6, "Open and closed models": https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/
  - Stripe API, "Idempotent requests": https://docs.stripe.com/api/idempotent_requests
  - web.dev, "Rendering on the Web": https://web.dev/articles/rendering-on-the-web
  - IETF, RFC 7519 "JSON Web Token (JWT)": https://www.rfc-editor.org/rfc/rfc7519
  - OWASP, "JSON Web Token Cheat Sheet": https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html
  - IETF, RFC 6265 "HTTP State Management Mechanism": https://www.rfc-editor.org/rfc/rfc6265
  - MDN, "Compression in HTTP": https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression
  - PostgreSQL 18 Documentation, "Table Partitioning": https://www.postgresql.org/docs/current/ddl-partitioning.html
  - OpenJDK, JEP 122 "Remove the Permanent Generation": https://openjdk.org/jeps/122
  - OpenJDK, JEP 248 "Make G1 the Default Garbage Collector": https://openjdk.org/jeps/248

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Ổn định](bai_01_on_dinh.md) · [Bài 2 ← bạn đang ở đây] · [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md) · [Bài 4 — Vận hành](bai_04_van_hanh.md)

Xem thêm [README khoá học](../README.md).
