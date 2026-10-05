# Bài 1 — Ổn định: vết nứt nào cũng sẽ đến, đừng để nó lan

> [!info] Về bài này
> Dựng từ **Part I — Stability** của *Release It!* (Michael T. Nygard, 2007, `tai_lieu/`, `tr. 20–145`): Ch.2 nghiên cứu tình huống hãng bay, Ch.3 Introducing Stability, Ch.4 Stability Antipatterns, Ch.5 Stability Patterns, Ch.6 Stability Summary.
> Trích theo `Ch. N` và `tr. X` (**số trang in = số trang PDF**). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới. Tên antipattern và pattern giữ tiếng Anh như sách để dễ tra.
> Đây là bài dài nhất khoá: 11 antipattern và 8 pattern, mỗi cái một mục. Nên đọc theo ba chặng: mục 1–2 (ca hãng bay và khung lý thuyết), mục 3–13 (các cách hệ thống chết), mục 14–22 (các cách giữ cho nó sống và bảng ghép hai bên).
> *Cần đọc trước:* [Bài 0 — Nhập môn](bai_00_nhap_mon.md).

## Mục lục

1. [Mở đầu: một exception làm cả hãng bay nằm đất](#1-mở-đầu-một-exception-làm-cả-hãng-bay-nằm-đất)
2. [Phần mềm phải hoài nghi: ổn định, failure mode và vết nứt lan](#2-phần-mềm-phải-hoài-nghi-ổn-định-failure-mode-và-vết-nứt-lan)
3. [Integration Points: kẻ giết hệ thống số một](#3-integration-points-kẻ-giết-hệ-thống-số-một)
4. [Chain Reactions: một máy ngã, cả tầng ngã theo](#4-chain-reactions-một-máy-ngã-cả-tầng-ngã-theo)
5. [Cascading Failures: vết nứt nhảy tầng](#5-cascading-failures-vết-nứt-nhảy-tầng)
6. [Users: thứ khủng khiếp mà hệ thống tồn tại vì nó](#6-users-thứ-khủng-khiếp-mà-hệ-thống-tồn-tại-vì-nó)
7. [Blocked Threads: tiến trình vẫn chạy, hệ thống vẫn chết](#7-blocked-threads-tiến-trình-vẫn-chạy-hệ-thống-vẫn-chết)
8. [Attacks of Self-Denial: bị chính mình tấn công](#8-attacks-of-self-denial-bị-chính-mình-tấn-công)
9. [Scaling Effects: thứ chạy tốt ở tỉ lệ một-một](#9-scaling-effects-thứ-chạy-tốt-ở-tỉ-lệ-một-một)
10. [Unbalanced Capacities: front end luôn đủ sức nhấn chìm back end](#10-unbalanced-capacities-front-end-luôn-đủ-sức-nhấn-chìm-back-end)
11. [Slow Responses: chậm còn tệ hơn hỏng](#11-slow-responses-chậm-còn-tệ-hơn-hỏng)
12. [SLA Inversion: hứa cao hơn thứ mình dựa vào](#12-sla-inversion-hứa-cao-hơn-thứ-mình-dựa-vào)
13. [Unbounded Result Sets: câu truy vấn trả về mười triệu dòng](#13-unbounded-result-sets-câu-truy-vấn-trả-về-mười-triệu-dòng)
14. [Use Timeouts: hy vọng không phải là phương pháp thiết kế](#14-use-timeouts-hy-vọng-không-phải-là-phương-pháp-thiết-kế)
15. [Circuit Breaker: ngừng gọi vào chỗ đang đau](#15-circuit-breaker-ngừng-gọi-vào-chỗ-đang-đau)
16. [Bulkheads: cứu lấy một phần con tàu](#16-bulkheads-cứu-lấy-một-phần-con-tàu)
17. [Steady State: hệ thống phải tự chạy mà không cần ai chạm vào](#17-steady-state-hệ-thống-phải-tự-chạy-mà-không-cần-ai-chạm-vào)
18. [Fail Fast: đã biết sẽ hỏng thì hỏng ngay](#18-fail-fast-đã-biết-sẽ-hỏng-thì-hỏng-ngay)
19. [Handshaking: để máy chủ được quyền nói "khoan đã"](#19-handshaking-để-máy-chủ-được-quyền-nói-khoan-đã)
20. [Test Harness: một đối thủ biết chơi xấu](#20-test-harness-một-đối-thủ-biết-chơi-xấu)
21. [Decoupling Middleware: tích hợp mà không trói nhau](#21-decoupling-middleware-tích-hợp-mà-không-trói-nhau)
22. [Bảng ghép antipattern và pattern, và lời chốt Part I](#22-bảng-ghép-antipattern-và-pattern-và-lời-chốt-part-i)
23. [Đối chiếu 2026](#23-đối-chiếu-2026)
24. [Áp dụng vào việc của bạn](#24-áp-dụng-vào-việc-của-bạn)
25. [Từ điển thuật ngữ](#25-từ-điển-thuật-ngữ)
26. [Câu hỏi tự kiểm tra](#26-câu-hỏi-tự-kiểm-tra)
27. [Tóm tắt một trang](#tóm-tắt-một-trang)
28. [Nguồn](#nguồn)

---

## 1. Mở đầu: một exception làm cả hãng bay nằm đất

Nygard mở Part I bằng một câu hỏi mà ai trực on-call vài năm cũng gật đầu:

> [!quote] Release It! — Ch.2 (tr. 21)
> "Have you ever noticed that the incidents that blow up into the biggest issues start with something very small?"
>
> *Bạn có để ý rằng những sự cố nổ thành chuyện lớn nhất đều khởi đầu từ một thứ rất nhỏ không?*

**Bối cảnh.** Một hãng hàng không lớn đang chuyển sang kiến trúc hướng dịch vụ. Dịch vụ đầu tiên là **Core Facilities (CF)**, chuyên tra cứu chuyến bay theo ngày, giờ, thành phố, mã sân bay, số hiệu (tr. 21). Ki-ốt tự check-in, tổng đài trả lời tự động (IVR) và các ứng dụng "channel partner" (sinh dữ liệu cho các trang đặt vé lớn) đã chuyển sang dùng CF; ứng dụng của nhân viên quầy và tổng đài viên thì chưa, và Nygard nói đó hoá ra là điều may (tr. 21–22). Tên thật, nơi chốn, ngày tháng đều đã đổi (tr. 21). CF được xây để sẵn sàng cao đúng sách giáo khoa: cụm J2EE, Oracle 9i dư thừa trên mảng RAID, Veritas Cluster Server điều khiển chuyển đổi cơ sở dữ liệu, cặp cân bằng tải phần cứng, mọi phần cứng đều dư thừa, và cả một địa điểm dự phòng cách ba mươi dặm (tr. 22).

**Diễn biến.** Tối thứ Năm, khoảng 11 giờ đêm giờ Thái Bình Dương, đội kỹ sư tại chỗ làm một việc họ đã làm hàng chục lần: chuyển tay cơ sở dữ liệu từ máy 1 sang máy 2 để bảo trì máy 1, rồi chuyển ngược lại để bảo trì máy 2 (tr. 22–23). Veritas làm việc này trong vòng một phút, và máy chủ ứng dụng không hề biết vì chúng chỉ nối vào địa chỉ IP ảo (tr. 23). Khoảng 12:30 sáng, ca trực đánh dấu thay đổi là "Completed, Success"; người kỹ sư đi ngủ sau một ca 22 tiếng (tr. 24).

Khoảng 2:30 sáng, **mọi ki-ốt check-in trên cả nước cùng chuyển đỏ** trên màn hình giám sát. Vài phút sau đến lượt IVR. 2:30 sáng bờ Tây là 5:30 sáng bờ Đông, giờ cao điểm check-in chuyến sớm (tr. 24).

**Ứng cứu.** Nguyên tắc đầu tiên của Nygard:

> [!quote] Release It! — Ch.2 (tr. 24)
> "In any incident, my first priority is always to restore service. Restoring service takes precedence over investigation."
>
> *Trong mọi sự cố, ưu tiên số một của tôi luôn là khôi phục dịch vụ. Khôi phục dịch vụ đi trước điều tra.*

May là đội đã viết sẵn script chụp thread dump và chụp nhanh cơ sở dữ liệu; Nygard khen đây là thế cân bằng hoàn hảo: không ứng biến, không kéo dài sự cố, vẫn giữ chứng cứ cho postmortem (tr. 24). Hai nhóm ứng dụng treo gần như cùng lúc, nên giả thuyết hiển nhiên là chúng cùng phụ thuộc vào một bên đang gặp nạn; bên chung duy nhất là CF, lại vừa chuyển đổi cơ sở dữ liệu (tr. 25). Thế nhưng giám sát không báo gì về CF: công cụ giám sát chỉ gọi một trang trạng thái, nên chẳng nói được mấy về sức khoẻ thật (tr. 25).

Sắp chạm giới hạn SLA một giờ, đội khởi động lại từng máy chủ CF. Máy đầu tiên vừa lên, IVR bắt đầu hồi phục; CF lên hết thì IVR xanh, nhưng ki-ốt vẫn đỏ. Theo linh cảm, trưởng nhóm khởi động lại cả máy chủ ứng dụng của ki-ốt, và mọi thứ xanh trở lại (tr. 25). *Ghi chú của khoá:* về các mốc giờ, tr. 25 ghi tổng thời gian sự cố là "hơi hơn ba giờ, từ 11:30 tối đến 2:30 sáng", cũng trang đó nói failover diễn ra "ba giờ trước sự cố", còn tr. 24 cho ki-ốt đỏ lúc 2:30 sáng và tr. 27 gọi 10:30 sáng là "tám giờ sau khi sự cố bắt đầu". Các mốc này không khớp nhau hoàn toàn; khoá chỉ nêu ra, không phán mốc nào đúng.

**Hậu quả.** Chính Nygard viết ba giờ nghe có vẻ không nhiều, nhưng tác động kéo dài hơn thế nhiều: gần 3 giờ chiều mới giải quyết xong hàng tồn check-in, máy bay kẹt cổng, cảnh trễ chuyến lên *Good Morning America* (tr. 25–27). FAA chấm điểm hãng theo tỉ lệ đúng giờ, lương CEO gắn một phần với bảng điểm ấy, và "bạn biết đó là một ngày tồi tệ" khi thấy CEO đi lùng trong trung tâm vận hành, tìm xem ai đã làm ông mất căn nhà nghỉ ở St. Thomas (tr. 27).

**Postmortem.** 10:30 sáng, Tom, người phụ trách tài khoản phía Nygard, gọi ông bay tới "tìm xem vì sao việc chuyển đổi cơ sở dữ liệu gây ra sự cố". Nygard ghi rằng lối nghĩ "post hoc, ergo propter hoc" (chú thích của ông: "ai chạm vào cuối cùng") trong vận hành *thường* là điểm khởi đầu tốt, dù không phải lúc nào cũng đúng (tr. 27). Ông mang theo năm câu hỏi: failover có gây ra sự cố không, nếu không thì cái gì; cụm có cấu hình đúng không; đội vận hành bảo trì có đúng không; lẽ ra có thể phát hiện trước bằng cách nào; và làm sao để chuyện này không bao giờ lặp lại (tr. 28). Ông ví postmortem với án mạng mà "cái xác" đã biến mất, vì máy chủ đã chạy lại, và ghi chú dự định so cấu hình hiện tại với bản sao lưu đêm trước để biết có ai sửa gì che lỗi không (tr. 28).

Cấu hình cụm cơ sở dữ liệu không có lỗi gì, đúng bài bản (tr. 29). Manh mối nằm ở **thread dump**. Ở máy chủ ki-ốt, cả 40 luồng xử lý yêu cầu đều kẹt trong `SocketInputStream.socketRead0()`, cùng gọi `FlightSearch.lookupByCity()` qua RMI và EJB (tr. 29, 31). RMI có một điểm chết: lời gọi không đặt timeout được, nên bên gọi phơi mình trước mọi trục trặc của máy chủ từ xa (tr. 31). Ở phía CF, luồng HTTP gần như rảnh (nên trang trạng thái vẫn trả lời giám sát), còn **mọi luồng EJB trên mọi máy chủ kẹt ở cùng một dòng: chờ mượn kết nối từ pool** (tr. 31). Không có quyền đọc mã nguồn, giữa bầu không khí đổ lỗi, Nygard dịch ngược file nhị phân từ production (tr. 32). Khối `finally` đóng `Statement` rồi mới đóng `Connection`; nhưng `Statement.close()` **có thể ném SQLException**, và driver Oracle ném đúng lúc gặp IOException, chẳng hạn *sau khi chuyển đổi cơ sở dữ liệu*, vì IP đã chuyển máy mà trạng thái TCP thì không (tr. 32). Khi `close()` ném, `Connection` không được đóng: rò một kết nối. Sau 40 lần, pool cạn (tr. 33–34).

> [!quote] Release It! — Ch.2 (tr. 34)
> "The entire globe-spanning, multibillion dollar airline with its hundreds of aircraft and tens of thousands of employees was grounded by one programmer’s rookie error: a single uncaught SQLException."
>
> *Cả một hãng bay trải khắp địa cầu, trị giá hàng tỉ đô, với hàng trăm máy bay và hàng chục nghìn nhân viên, đã bị bắt nằm đất vì lỗi tập sự của một lập trình viên: một SQLException duy nhất không được bắt.*

Nhiều dev của hãng buộc tội driver có bug; Nygard đáp rằng đặc tả JDBC *cho phép* `close()` ném SQLException, nên mã phải xử lý nó (tr. 33).

**Phòng ngừa thế nào?** Code review chỉ bắt được nếu người review biết nội tạng driver Oracle hoặc bỏ hàng giờ cho mỗi hàm. Test thì khi đã biết chỗ, đội dựng lại được lỗi trong môi trường stress test, nhưng bộ test thường ngày không gọi hàm này đủ nhiều (tr. 34). Kết luận là trục của cả Part I:

> [!quote] Release It! — Ch.2 (tr. 34)
> "Bugs will happen. They cannot be eliminated, so they must be survived instead."
>
> *Bug sẽ xảy ra. Không thể loại trừ chúng, nên phải sống sót qua chúng.*

> [!quote] Release It! — Ch.2 (tr. 34)
> "A better question to ask is, “How do we prevent bugs in one system from affecting everything else?”"
>
> *Câu hỏi nên đặt là: "Làm sao ngăn bug trong một hệ thống lan sang mọi thứ khác?"*

## 2. Phần mềm phải hoài nghi: ổn định, failure mode và vết nứt lan

Phần mềm mới ra đời giống sinh viên vừa tốt nghiệp: đầy lạc quan, rồi va vào thực tế ngoài phòng lab, nơi bài kiểm không có đáp án, có khi chỉ nhằm gài bạn thất bại (tr. 35).

> [!quote] Release It! — Ch.3 (tr. 35)
> "Enterprise software must be cynical. Cynical software expects bad things to happen and is never surprised when they do."
>
> *Phần mềm doanh nghiệp phải hoài nghi. Phần mềm hoài nghi luôn chờ chuyện xấu xảy ra và không bao giờ ngạc nhiên khi nó xảy ra.*

Phần mềm hoài nghi không tin cả chính mình nên dựng rào chắn bên trong, và không thân thiết quá với hệ thống khác (tr. 35). CF không đủ hoài nghi: "loá mắt vì ký hiệu đô la nên không thấy biển dừng" (tr. 35). Và điều đáng ngạc nhiên nhất: **thiết kế rất ổn định thường tốn công xây dựng ngang thiết kế bất ổn** (tr. 36).

**Định nghĩa.** *Transaction* là đơn vị công việc trừu tượng của hệ thống, không phải giao dịch cơ sở dữ liệu; *system* là toàn bộ phần cứng, ứng dụng, dịch vụ cần để xử lý transaction từ đầu đến cuối (tr. 36).

> [!quote] Release It! — Ch.3 (tr. 37)
> "A resilient system keeps processing transactions, even when there are transient impulses, persistent stresses, or component failures disrupting normal processing."
>
> *Hệ thống bền bỉ tiếp tục xử lý transaction kể cả khi có xung lực thoáng qua, ứng suất kéo dài hay linh kiện hỏng làm gián đoạn việc xử lý bình thường.*

Hai thuật ngữ mượn từ cơ khí. **Impulse** (xung lực) là cú sốc nhanh, như đám đông ùa vào trang Xbox 360 vì tin đồn giảm giá. **Stress** (ứng suất) là lực kéo dài, như bộ xử lý thẻ tín dụng trả lời chậm; stress sinh ra **strain** (biến dạng), lan sang những chỗ xa lạ như RAM máy web tăng hay I/O cơ sở dữ liệu vọt (tr. 37). **Longevity** (tuổi thọ) là khả năng chạy lâu; định nghĩa làm việc hữu ích của "lâu" là khoảng giữa hai lần deploy (tr. 37). Khung bên lề tr. 38–39 chỉ ra hai kẻ thù của tuổi thọ là rò bộ nhớ và dữ liệu phình, và khuyên tự chạy longevity test: bắn tải nhẹ liên tục, có quãng nghỉ vài giờ mỗi ngày để bắt timeout của pool kết nối và firewall.

**Failure mode.** Nygard mượn James R. Chiles (*Inviting Disaster*): một hệ thống phức tạp sắp hỏng giống tấm thép có vết nứt siêu nhỏ; dưới ứng suất, vết nứt lan mỗi lúc một nhanh, rồi tấm thép gãy (tr. 37, 39).

> [!quote] Release It! — Ch.3 (tr. 39)
> "The original trigger and the way the crack spreads to the rest of the system, together with the result of the damage, are collectively called a failure mode."
>
> *Tác nhân khởi phát ban đầu, cách vết nứt lan ra phần còn lại của hệ thống, cùng với hậu quả của thiệt hại, gọi chung là một failure mode.*

Chấp nhận hỏng hóc là tất yếu thì bạn thiết kế được phản ứng của hệ thống, như kỹ sư ô tô làm **vùng biến dạng** hỏng trước để bảo vệ hành khách. Chiles gọi những chỗ chặn ấy là **crackstopper**. Không thiết kế failure mode thì bạn nhận bất cứ failure mode nào tự nảy ra, thường là loại nguy hiểm (tr. 39).

**Vết nứt lan, dựng lại theo ca hãng bay.** Ở tr. 39–41, Nygard lần lại chính ca CF và chỉ ra ở mỗi tầng, vết nứt *lẽ ra* đã bị chặn thế nào. Khoá vẽ lại:

```
VẾT NỨT LAN TRONG CA HÃNG BAY (dựng theo tr. 32–34 và 39–41)
─────────────────────────────────────────────────────────────────
[0] Failover Oracle: IP ảo chuyển máy, trạng thái TCP cũ chết
       │
[1] Statement.close() ném SQLException → Connection không được đóng
       │      chặn được: bắt exception khi đóng tài nguyên
       ▼
[2] Rò kết nối → sau 40 lời gọi, pool cạn
       │      chặn được: pool tạo thêm kết nối khi cạn,
       │                 hoặc chỉ bắt luồng chờ có hạn
       ▼
[3] Mọi luồng EJB của CF kẹt ở getConnection()   (từng máy CF riêng rẽ)
       │      chặn được: chia CF thành nhiều nhóm dịch vụ
       │      (sách rào: ca này mọi nhóm "đều sẽ nứt y như nhau",
       │       nhưng không phải lúc nào cũng vậy)
       ▼
[4] RMI mặc định không timeout → luồng của ki-ốt và IVR
    kẹt ở socketRead0, chờ phản hồi không bao giờ tới
       │      chặn được: timeout trên socket RMI; dịch vụ HTTP có timeout;
       │                 không để luồng xử lý yêu cầu tự gọi ra ngoài
       ▼
[5] Ki-ốt + IVR toàn quốc đỏ
       │      chặn được (kiến trúc): hàng đợi request/reply,
       │                 hoặc tuplespace thay cho lời gọi đồng bộ
       ▼
[6] Hàng người ở sân bay, máy bay kẹt cổng, lên TV, FAA, CEO
```

Kiến trúc càng ghép chặt, lỗi code càng dễ lan; kiến trúc lỏng thì như bộ giảm xóc (tr. 41).

**Chuỗi thất bại.** Nhìn lại sau sự cố, chuỗi sự kiện trông như tất yếu; ước xác suất của đúng chuỗi ấy thì trông cực kỳ khó xảy ra. Nhưng chỉ khó xảy ra nếu coi từng sự kiện là độc lập, như tung đồng xu. Trong hệ thống, hỏng ở một tầng làm tăng xác suất hỏng ở tầng khác: cơ sở dữ liệu chậm thì máy chủ ứng dụng dễ hết bộ nhớ hơn; và ghép chặt làm vết nứt lan nhanh hơn (tr. 41). Vét cạn mọi câu hỏi "nếu... thì sao" với mọi lời gọi ra ngoài chỉ khả thi cho hệ thống sinh tử hay xe tự hành trên sao Hoả; phần còn lại cần *pattern* (tr. 41–42). Từ hàng trăm sự cố, nổi lên những khuôn hỏng lặp lại: **stability antipattern** (Ch.4); và những lời giải chung: **stability pattern** (Ch.5).

> [!quote] Release It! — Ch.3 (tr. 42)
> "These patterns cannot prevent cracks in the system. Nothing can."
>
> *Những pattern này không ngăn được vết nứt trong hệ thống. Không gì ngăn được.*

Chúng ngăn vết nứt *lan*, giữ lại một phần chức năng thay vì sập toàn bộ. Antipattern có xu hướng tiếp sức cho nhau; mỗi pattern trị một chứng cụ thể, như tỏi, bạc và lửa cho từng loài quái vật trong phim (tr. 42). Hình 3.1 (tr. 43) vẽ các tương tác; mục 22 dựng lại phần mà lời văn Ch.4–5 nói thẳng.

## 3. Integration Points: kẻ giết hệ thống số một

Một dự án làm lại nền tảng cho một nhà bán lẻ khổng lồ. Tới lúc mở cổng firewall cho các luồng dữ liệu ra vào, đội được chỉ sang một quản lý dự án riêng cho tích hợp, người phải dùng hẳn một *cơ sở dữ liệu* để theo dõi các tích hợp. Trang web ra mắt và đêm nào Nygard cũng bị gọi dậy lúc 3 giờ sáng; ông tin rằng mọi điểm tích hợp đồng bộ đều gây ít nhất một lần sập (tr. 47).

> [!quote] Release It! — Ch.4 (tr. 46)
> "Integration points are the number-one killer of systems. Every single one of those feeds presents a stability risk."
>
> *Điểm tích hợp là kẻ giết hệ thống số một. Mỗi luồng dữ liệu ấy đều là một rủi ro ổn định.*

**Socket.** Kết nối bị từ chối thì dễ: mọi ngôn ngữ đều báo rõ (tr. 46). Cái khó là *mất rất lâu mới biết không kết nối được*. Nếu phía xa đang ngập yêu cầu, hàng đợi listen đầy dần; luồng gọi `open()` kẹt trong nhân hệ điều hành tới khi hết timeout kết nối, thường tính bằng *phút*. Đọc cũng vậy: trong Java, `read()` mặc định chờ mãi (tr. 49). Lỗi nhanh như "connection refused" chỉ mất vài mili giây; lỗi chậm giam luồng hàng phút, và luồng bị giam hết thì máy chủ coi như chết, nên phản hồi chậm tệ hơn nhiều so với không phản hồi (tr. 50).

**Chuyện 5 giờ sáng.** Một trang Nygard vận hành treo toàn bộ gần như đúng 5 giờ sáng mỗi ngày, cả khoảng ba mươi instance trong vòng năm phút (tr. 50). Thread dump cho thấy mọi luồng kẹt trong driver JDBC của Oracle; phía mạng của cơ sở dữ liệu hoàn toàn im lặng, như "con chó không sủa" của Sherlock Holmes (tr. 50, 53). Thủ phạm là **firewall**: nó giữ bảng kết nối hữu hạn và lặng lẽ xoá kết nối nhàn rỗi quá một giờ, mà TCP không có cách nào để bên thứ ba báo cho hai đầu (tr. 54). Gói tin sau đó bị vứt, ngăn xếp TCP gửi lại mãi; trên Linux 2.6 mặc định khoảng hai mươi phút mới báo lỗi, trên HP-UX ba mươi phút, còn đọc thì có thể chờ mãi (tr. 54–55). Pool kết nối lại dùng chiến lược vào-sau-ra-trước: đêm vắng, một kết nối được dùng đi dùng lại, ba mươi chín cái còn lại nằm im quá một giờ, sáng ra kẹt hết (tr. 55). Cứu tinh là một DBA nhớ ra tính năng **dead connection detection** của Oracle: gói ping định kỳ đủ làm mới đồng hồ "gói cuối" của firewall (tr. 55–56).

**HTTP và thư viện nhà cung cấp.** `URLConnection` của Java gói mọi thứ vào một lời gọi chặn không đặt được timeout (tr. 57). Thư viện client của nhà cung cấp "chỉ là code", và kẻ giết người chính là *chặn*: pool nội bộ, đọc socket, callback chạy trên luồng đang giữ khoá, một bãi mìn deadlock (tr. 57–58).

Theo Nygard, hai pattern hiệu quả nhất chống lỗi điểm tích hợp là **Circuit Breaker** và **Decoupling Middleware**; bên cạnh đó là test hệ thống dưới tải lớn trong khi bật mọi công tắc hỏng (tr. 59), bằng một **Test Harness** giả làm đầu bên kia của mỗi điểm tích hợp (tr. 137).

**Điều rút ra** (tr. 59–60): lỗi điểm tích hợp hiếm khi đến dưới dạng mã lỗi đẹp đẽ; muốn gỡ thì phải biết lúc cần bóc lớp trừu tượng, bắt gói tin.

## 4. Chain Reactions: một máy ngã, cả tầng ngã theo

Một nhà bán lẻ có danh mục nửa triệu mã hàng, chạy mười hai máy tìm kiếm sau cân bằng tải. Phần mềm tìm kiếm rò bộ nhớ. Vì mọi máy gánh tải đều nhau từ sáng, chúng bắt đầu chết quanh trưa; mỗi máy chết thì phần tải của nó dồn sang các máy còn lại, làm chúng hết bộ nhớ nhanh hơn. Khoảng cách giữa lần chết thứ nhất và thứ hai là năm, sáu phút; giữa lần hai và ba còn ba, bốn phút; hai máy cuối chết cách nhau vài giây. Mất máy tìm kiếm cuối cùng, toàn bộ front end khoá cứng. Chờ bản vá mất nhiều tháng, trong lúc đó đội khởi động lại theo lịch 11 giờ sáng, 4 giờ chiều và 9 giờ tối (tr. 63).

Cơ chế nằm trong phép chia. Cụm tám máy, mỗi máy gánh 12,5% tổng tải. Mất một, bảy máy còn lại mỗi máy gánh khoảng 14,3%: chỉ thêm 1,8% tổng tải, nhưng tải của chính máy đó tăng khoảng 15%. Cụm hai máy thì máy sống sót gánh gấp đôi (tr. 61).

> [!quote] Release It! — Ch.4 (tr. 61)
> "A chain reaction occurs when there is some defect in an application—usually a resource leak or a load-related crash."
>
> *Phản ứng dây chuyền xảy ra khi ứng dụng có một khiếm khuyết, thường là rò tài nguyên hoặc sập do tải.*

Vì là tầng đồng nhất, khiếm khuyết nằm ở mọi máy; cách duy nhất để triệt phản ứng dây chuyền là sửa khiếm khuyết gốc (tr. 61–62). Chia tầng thành nhiều pool theo kiểu **Bulkheads** đôi khi giúp, bằng cách tách một phản ứng dây chuyền thành hai, diễn ra ở hai tốc độ khác nhau (tr. 62). Phản ứng dây chuyền ở một tầng dễ thành lỗi dây chuyền ở tầng gọi nó (mục 5).

**Điều rút ra** (tr. 64): Bulkheads không cứu được bên gọi của phân vùng đã sập; việc đó là của Circuit Breaker phía bên gọi.

## 5. Cascading Failures: vết nứt nhảy tầng

Một hệ thống Nygard từng thấy xé bỏ mọi kết nối JDBC từng ném SQLException. Khi cả cụm cơ sở dữ liệu tắt, mỗi yêu cầu trang lại tạo kết nối mới, nhận SQLException, cố xé kết nối, nhận thêm SQLException, rồi "nôn" stack trace lên mặt người dùng (tr. 65).

> [!quote] Release It! — Ch.4 (tr. 65)
> "A cascading failure occurs when a crack in one layer triggers a crack in a calling layer."
>
> *Lỗi dây chuyền xảy ra khi vết nứt ở một tầng kích hoạt vết nứt ở tầng gọi nó.*

Phân biệt với mục 4: phản ứng dây chuyền lan *ngang* trong một tầng đồng nhất; lỗi dây chuyền lan *dọc* từ tầng bị gọi lên tầng gọi. Nó cần một cơ chế truyền, thường là một resource pool bị rút cạn; và theo Nygard, điểm tích hợp không có Timeouts là cách chắc ăn để tạo ra nó (tr. 65). Nếu điểm tích hợp là nguồn vết nứt số một thì lỗi dây chuyền là chất tăng tốc số một; hai pattern hiệu quả nhất chống nó là Circuit Breaker và Timeouts (tr. 65). Pool an toàn luôn giới hạn thời gian một luồng chờ mượn tài nguyên (tr. 66).

**Chuyện "Hammer Time".** Cơ chế nhảy tầng có khi là luồng *quá hăng*. Tầng dưới có race condition thỉnh thoảng trả lỗi vô cớ, nên dev tầng trên cho gọi lại mỗi khi lỗi, mà tầng dưới không phân biệt lỗi thoáng qua với lỗi nghiêm trọng. Đến khi tầng dưới hỏng thật (mất gói tin tới cơ sở dữ liệu vì một switch hỏng), tầng trên càng nện mạnh hơn, tới mức dùng 100% CPU để gọi xuống và ghi log lỗi. "Một circuit breaker sẽ giúp rất nhiều ở đây" (tr. 67).

## 6. Users: thứ khủng khiếp mà hệ thống tồn tại vì nó

Nygard nói nửa đùa (chú thích của ông nhắc người dùng là lý do hệ thống tồn tại) rằng hệ thống sẽ ổn định vô hạn nếu không có người dùng (tr. 68):

> [!quote] Release It! — Ch.4 (tr. 68)
> "Human users have a gift for doing exactly the worst possible thing at the worst possible time."
>
> *Người dùng có biệt tài làm đúng điều tệ nhất vào đúng lúc tệ nhất.*

Ông chia ra bốn nhóm.

**Lưu lượng.** Công suất tỉ lệ với phần cứng đã mua, không phải số người dùng đã hút về (tr. 68). Với web, mỗi người dùng có một session nằm trong bộ nhớ tới khi hết hạn (tr. 69). Thiếu bộ nhớ thì thư viện log có khi không ghi nổi lỗi, driver JDBC native có thể làm sập JVM (tr. 69). Lời khuyên: giữ trong session càng ít càng tốt; buộc phải cất đồ to thì dùng `SoftReference` (tr. 69–71).

**Người dùng đắt.** Khách *mua hàng* đi bốn, năm trang và chạm hàng loạt điểm tích hợp: thẻ tín dụng, thuế, địa chỉ, tồn kho, vận chuyển (tr. 72). Không nên chặn họ vì họ mang tiền đến; hãy test hung hăng: tỉ lệ chuyển đổi dự kiến 2% thì load test ở 4%, 6% hay 10% (tr. 72).

**Người dùng không mong muốn.** Một proxy cấu hình sai ở một căn cứ Hải quân gửi lại URL cuối của một khách hợp lệ, lúc đầu ba mươi giây một lần, mười phút sau bốn, năm lần mỗi giây, mỗi lần không mang cookie session nên tạo session mới (tr. 73). Ca ra mắt ở [Bài 2 — Công suất](bai_02_cong_suat.md) cũng có một máy ở căn cứ Hải quân gọi lại URL cuối mãi (tr. 157); sách không nói rõ có phải cùng một vụ. Một interceptor cập nhật "lần đăng nhập cuối" coi mỗi yêu cầu là một lần đăng nhập mới; hàng loạt giao dịch tranh cập nhật một dòng, một giao dịch giữ khoá bị treo là mọi luồng xử lý yêu cầu cạn dần, trang sập (tr. 74).

> [!quote] Release It! — Ch.4 (tr. 73)
> "Once again, we see that sessions are the Achilles heel of web applications."
>
> *Một lần nữa, ta thấy session là gót chân Achilles của ứng dụng web.*

Kẻ cào giá cũng không tôn trọng cookie (tr. 74), còn `robots.txt` chỉ là lời đề nghị (tr. 76–77). Khoảng năm 1998, một "cái bẫy nhện" sinh link ngẫu nhiên để nhốt spider của AltaVista đã nuốt hết băng thông của chính công ty, tốn hơn 10.000 đô (tr. 77).

> [!quote] Release It! — Ch.4 (tr. 77)
> "Search engines always have more bandwidth than you."
>
> *Công cụ tìm kiếm luôn có nhiều băng thông hơn bạn.*

Hai cách Nygard thấy hiệu quả: chặn kỹ thuật ở firewall hoặc CDN (danh sách chặn nên hết hạn định kỳ, và ông gọi đây là "một dạng Circuit Breaker"), và chặn pháp lý qua điều khoản sử dụng; cả hai chỉ như diệt côn trùng (tr. 77–78).

**Người dùng ác ý.** Số đông là "script kiddie", nguy hiểm vì số lượng (tr. 78). Rủi ro ổn định chính là DDoS; một Circuit Breaker chuyên biệt có thể hạn chế thiệt hại từ một host cụ thể và đỡ cả những cơn lũ vô tình (tr. 79).

**Điều rút ra** (tr. 80): script test quá dễ đoán cho stress test; hãy stress test riêng các deep link và URL nóng.

## 7. Blocked Threads: tiến trình vẫn chạy, hệ thống vẫn chết

Java và Ruby gần như không bao giờ sập thật. Đó cũng là cái bẫy: trình thông dịch chạy ngon lành trong khi ứng dụng khoá chết, mọi luồng ngồi "chờ Godot" (tr. 81).

> [!quote] Release It! — Ch.4 (tr. 81)
> "The majority of system failures I’ve dealt with do not involve outright crashes."
>
> *Phần lớn các sự cố hệ thống tôi từng xử lý không phải là sập hẳn.*

Khung bên lề tr. 82: chỉ một biến quan sát có ý nghĩa là hệ thống có xử lý được transaction không, nên hãy bổ sung **giám sát từ bên ngoài**, một client giả ở trung tâm dữ liệu khác chạy giao dịch tổng hợp (synthetic transaction) định kỳ. Nhớ lại ca hãng bay, nơi giám sát chỉ gọi trang trạng thái.

Bài toán có bốn phần: lỗi và exception sinh quá nhiều tổ hợp để test hết; tương tác bất ngờ làm hỏng code vốn an toàn; xác suất treo tăng theo số yêu cầu đồng thời; và dev không bao giờ nện ứng dụng bằng 10.000 yêu cầu đồng thời (tr. 81–82). Không thể "test cho hết", nên hãy dùng ít primitive trong khuôn mẫu đã biết, dùng thư viện đã kiểm chứng, đừng tự viết connection pool (tr. 82–83).

**Chuyện cache tồn kho.** Hệ thống cần kiểm hàng có sẵn ở cửa hàng qua một hệ thống tồn kho ở xa, mỗi lời gọi vài giây. Dev làm một read-through cache kế thừa `GlobalObjectCache`, có phương thức `get()` `synchronized` (tr. 84–85). Hệ thống tồn kho nhỏ hơn nhu cầu; khi front end bận, nó ngập rồi sập, và mọi luồng gọi `get()` đều chặn vì một luồng duy nhất đang ở trong `create()` chờ phản hồi không bao giờ tới (tr. 85). Blocked threads, Unbalanced Capacities và thiếu Timeouts cộng lại đánh sập cả trang (tr. 85).

> [!quote] Release It! — Ch.4 (tr. 86)
> "No one designed this failure mode into the combined system, but no one designed it out either."
>
> *Không ai thiết kế failure mode này vào hệ thống tổng thể, nhưng cũng không ai thiết kế để loại nó ra.*

Thư viện bên thứ ba nổi tiếng là nguồn luồng bị chặn (tr. 86). Nygard khuyên viết test cố tình phá thư viện bằng một test harness quỷ quyệt; dễ gãy thì dùng timeout nếu có, không có thì phải dựng pool luồng thợ riêng, một kiểu chắp vá mà ông khuyên chỉ dùng sau khi đã ép nhà cung cấp đưa thư viện tốt hơn (tr. 86–87).

**Điều rút ra** (tr. 87): không chứng minh được code không có deadlock, nhưng đảm bảo được *không deadlock nào kéo dài mãi*, bằng Timeouts.

## 8. Attacks of Self-Denial: bị chính mình tấn công

Khi Xbox 360 vừa mở đặt trước, một nhà bán lẻ điện tử lớn gửi email ghi rõ giờ mở bán, kèm một deep link vô tình đi vòng qua Akamai. Email lan sang các trang săn hàng giảm giá ngay trong ngày. Một phút trước giờ hẹn, cả trang bừng sáng rồi tắt ngấm (tr. 88). Tháng 11/2006, Amazon bán 1.000 máy Xbox 360 giá 100 đô; 1.000 máy hết trong năm phút, và trong năm phút đó không có gì khác bán được, vì hàng triệu người nhấn Reload. Nygard suy đoán Amazon đã không dựng cụm máy chủ riêng cho đợt khuyến mãi (tr. 88).

> [!quote] Release It! — Ch.4 (tr. 88)
> "A self-denial attack describes any situation in which the system—or the extended system that includes humans—conspires against itself."
>
> *Tấn công tự từ chối là mọi tình huống trong đó hệ thống, hoặc hệ thống mở rộng bao gồm cả con người, tự âm mưu chống lại chính nó.*

Paul Lord có câu Nygard dẫn lại:

> [!quote] Release It! — Ch.4 (tr. 89)
> "Good marketing can kill you at any time."
>
> *Marketing giỏi có thể giết bạn bất cứ lúc nào.*

Không phải vết thương tự gây nào cũng do marketing. Trong tầng ngang có tài nguyên dùng chung, một máy lạc lối có thể hại cả tầng: hạ tầng ATG luôn có một lock manager duy nhất, và một món hàng phổ biến bị sửa nhầm là hàng nghìn luồng trên hàng trăm máy xếp hàng chờ một khoá ghi (tr. 89). Cách tránh: kiến trúc **shared-nothing**; nếu không được thì dùng decoupling middleware, hoặc thiết kế chế độ dự phòng (lock manager khoá bi quan không có thì lùi về khoá lạc quan). Có thời gian chuẩn bị thì dành riêng một phần hạ tầng cho đợt khuyến mãi, và khi phần đó tắt thì áp dụng **Fail Fast** (tr. 89–90).

**Điều rút ra** (tr. 90): giữ kênh liên lạc với marketing; đừng gửi email hàng loạt có deep link, hãy làm trang "landing zone" tĩnh cho cú nhấp đầu.

## 9. Scaling Effects: thứ chạy tốt ở tỉ lệ một-một

Định luật bình phương-lập phương giải thích vì sao không có nhện to bằng voi (tr. 91). Mỗi khi có quan hệ nhiều-một hoặc nhiều-ít, bạn có thể dính hiệu ứng tỉ lệ khi một phía tăng: cơ sở dữ liệu chịu ngon hai máy ứng dụng có thể sập khi thêm tám máy; và môi trường dev, QA hiếm khi có kích thước như production (tr. 91).

**Giao tiếp điểm-điểm.** Mỗi instance nói chuyện trực tiếp với mọi instance khác thì số kết nối tăng theo bình phương số instance (tr. 92). *Khoá tính lại:* 2 instance cần 1 kết nối, 10 cần 45, 100 cần 4.950 (công thức n(n−1)/2).

> [!quote] Release It! — Ch.4 (tr. 92)
> "This type of defect cannot be tested out; it must be designed out."
>
> *Loại khiếm khuyết này không thể test để loại ra; phải thiết kế để loại ra.*

Chỉ bao giờ có hai máy thì điểm-điểm hoàn toàn ổn; đông lên thì thay bằng UDP broadcast, multicast, publish/subscribe hoặc hàng đợi message, mỗi cái hiệu quả hơn nhưng tốn hạ tầng hơn (tr. 92–93).

**Tài nguyên dùng chung.** Nếu nó dư thừa và không độc quyền thì bão hoà cứ thêm máy. Quá thường xuyên, nó bị cấp phát độc quyền; khi đó xác suất tranh chấp tăng theo số transaction và số client, bão hoà thì giao dịch hỏng, và với cache manager thì có thể mất tính toàn vẹn dữ liệu (tr. 93–94). Khung bên lề về **shared-nothing** (tr. 94): kiến trúc mở rộng tốt nhất là mỗi máy tự chạy, không cần phối hợp; cái giá thường là failover; có thể xấp xỉ bằng cách giảm "fan-in", ví dụ ghép từng cặp máy làm dự phòng cho nhau.

**Điều rút ra** (tr. 95): lên hàng chục máy thì đổi điểm-điểm sang một-nhiều; client phải chạy tiếp được khi tài nguyên chung chậm hay khoá.

## 10. Unbalanced Capacities: front end luôn đủ sức nhấn chìm back end

Báo chí thời đó đầy chuyện "utility computing", hạ tầng tự cấp thêm tài nguyên theo nhu cầu; Nygard gọi nó là "fantastic", theo nghĩa "a fantasy" (tr. 96). Trong thế giới thật của ông, thêm công suất cho production mất hàng tuần, khủng hoảng thì vài ngày; ông từng thấy một kỹ sư tên Todd dựng lại sáu máy trong một mạch 36 tiếng để cứu một buổi ra mắt (tr. 96); [Bài 2 — Công suất](bai_02_cong_suat.md) có một cảnh rất giống trong tuần ra mắt ở Ch.7: một sysadmin trực 36 giờ dựng sáu máy mượn (tr. 159), dù sách không nói rõ là cùng một vụ. Trong ngắn hạn, công suất phần cứng coi như cố định (tr. 97).

Hình 4.13 (tr. 97): front end 20 máy, 75 instance, 3.000 luồng; back end 6 máy, 6 instance, 450 luồng. Chỉ một phần nhỏ của phần nhỏ số luồng front end hỏi hệ thống lịch hẹn lắp đặt tại nhà, và nếu back end đáp ứng đủ dự đoán ấy thì tưởng là xong (tr. 97). Rồi marketing chạy "miễn phí lắp đặt, một ngày duy nhất", và số luồng hỏi lịch hẹn tăng gấp hai, bốn, mười lần (tr. 98). *Ghi chú của khoá:* bộ số 20 host, 75 instance, 3.000 luồng và 450 luồng của Hình 4.13 trùng khớp với các hình của ca Black Friday ở Ch.16, và kịch bản giả định ở đây (khuyến mãi của marketing đè bẹp hệ thống lên lịch) chính là điều xảy ra trong ca đó; xem [Bài 4 — Vận hành](bai_04_van_hanh.md).

> [!quote] Release It! — Ch.4 (tr. 98)
> "The fact is that the front end always has the ability to overwhelm the back end, because their capacities are not balanced."
>
> *Sự thật là front end luôn có khả năng nhấn chìm back end, vì công suất hai bên không cân bằng.*

Dựng back end to bằng website chỉ để đề phòng là phí vốn (tr. 98). Vậy phải làm cả hai phía chịu được "sóng thần": front end dùng **Circuit Breaker**; back end dùng **Handshaking** để bảo front end giảm tốc; cân nhắc **Bulkheads** để giữ công suất back end cho giao dịch khác (tr. 98). QA thường chỉ có hai máy mỗi bên, tỉ lệ một-một, trong khi production có thể là mười-một; dùng **Test Harness** mô phỏng back end héo dưới tải (tr. 98). Nếu bạn làm back end: mô hình hoá công suất để ít nhất đúng tầm ("Ba nghìn luồng gọi vào bảy mươi lăm luồng là không đúng tầm", tr. 99), rồi lấy số lời gọi front end *có thể* gửi, nhân đôi, dồn vào giao dịch đắt nhất; hệ thống bền bỉ có thể chậm, thậm chí **Fail Fast**, nhưng phải hồi phục khi tải giảm (tr. 99). *Ghi chú của khoá:* con số bảy mươi lăm luồng nằm trong một câu giả định, có thể là ví dụ khác với 450 luồng của Hình 4.13; còn mức stress thì thân bài nói "nhân đôi", trong khi Remember This cùng trang nói "gấp mười lần mức cao nhất từng có".

**Điều rút ra** (tr. 99): Unbalanced Capacities là trường hợp đặc biệt của Scaling Effects; so số máy và số luồng hai phía ở production với ở QA.

## 11. Slow Responses: chậm còn tệ hơn hỏng

Lỗi nhanh cho phép bên gọi xử lý xong giao dịch sớm; phản hồi chậm giam tài nguyên ở cả hai phía (tr. 100). Nguyên nhân thường là nhu cầu vượt mức, khi mọi bộ xử lý yêu cầu đã bận. Nó cũng có thể là triệu chứng: rò bộ nhớ khiến bộ gom rác làm việc cật lực, mạng tắc qua WAN với giao thức quá lắm lời, hay giao thức socket tự viết mà `read()` không lặp cho tới khi rút hết bộ đệm nhận, gây nghẽn TCP (tr. 100).

> [!quote] Release It! — Ch.4 (tr. 100)
> "Slow responses tend to propagate upward from layer to layer in a gradual form of cascading failure."
>
> *Phản hồi chậm có xu hướng lan ngược lên từng tầng, một dạng lỗi dây chuyền từ từ.*

Hệ thống tự đo hiệu năng thì biết khi nào mình không đạt SLA. Ví dụ của sách: dịch vụ phải trả lời trong 100 mili giây; khi trung bình trượt của hai mươi giao dịch gần nhất vượt 100 ms, nó bắt đầu từ chối yêu cầu, ở tầng ứng dụng hoặc tầng kết nối, miễn là việc từ chối được tài liệu hoá và bên gọi biết trước (tr. 100). Với web, người chờ sẽ nhấn Reload, sinh thêm lưu lượng; và thiếu kết nối cơ sở dữ liệu sinh ra chậm, chậm lại làm tranh chấp nặng thêm, thành vòng tự củng cố (tr. 101).

## 12. SLA Inversion: hứa cao hơn thứ mình dựa vào

Dự án Frammitz là website mới: dư thừa ở mọi cấp, kiến trúc shared-nothing, cam kết SLA 99,99%, tức hơi hơn bốn phút ngừng mỗi tháng (tr. 102). Nygard phán: Frammitz chỉ đạt được SLA đó nhờ may, vì nó dựa vào cả một mạng nhện dịch vụ. Hình 4.15 ghi SLA của từng bên: có bên 99%, DNS của một bên 98,5%, và hai bên *không có SLA nào* (tr. 102–104).

> [!quote] Release It! — Ch.4 (tr. 103)
> "Unless every one of your dependencies is engineered for the same SLA you must provide, then the best you can possibly do is the SLA of the worst of your service providers."
>
> *Trừ khi mọi phụ thuộc của bạn được thiết kế cho cùng mức SLA bạn phải cung cấp, điều tốt nhất bạn có thể làm là mức SLA của nhà cung cấp tệ nhất.*

Xác suất còn làm mọi thứ tệ hơn: dựng ngây thơ thì Frammitz sống khi *mọi* thứ cùng sống; năm dịch vụ ngoài mỗi cái 99,9% thì Frammitz tối đa 99,5% (tr. 103). *Khoá tính lại:* 0,999 mũ 5 ≈ 0,995; 99,5% nghĩa là khoảng 3,6 giờ ngừng mỗi tháng 30 ngày, so với hơn bốn phút đã hứa.

Hai cách đáp: **tách khỏi** hệ thống SLA thấp để vẫn chạy khi nó chết, dùng decoupling middleware nếu được, ít nhất cũng đặt circuit breaker trước mỗi phụ thuộc; và **viết SLA theo từng chức năng**: chức năng không phụ thuộc bên thứ ba thì hứa mức cao nhất, chức năng cần bên thứ ba thì chỉ hứa được mức của họ trừ thêm xác suất hỏng của mình. Nygard gọi đó là định luật hai nhiệt động lực học của IT: mức dịch vụ chỉ có đi xuống (tr. 104–105). Hễ họ hỏng là bạn hỏng thì chắc chắn về mặt toán học độ sẵn sàng của bạn luôn thấp hơn của họ; và phụ thuộc nằm cả ở DNS nội bộ, SMTP, hàng đợi, SAN (tr. 105).

## 13. Unbounded Result Sets: câu truy vấn trả về mười triệu dòng

**Thứ Hai đen.** Một ngày không báo trước, mọi instance trong trang trại hơn 100 instance của máy chủ thương mại bắt đầu ăn 100% CPU, vài phút sau sập với lỗi bộ nhớ HotSpot, có máy sập trước cả khi khởi động xong; không giữ nổi quá 25% công suất (tr. 106). Máy sập trước khi nhận yêu cầu nên không phải do traffic; heap tụt về không, stack cho thấy đang ở sâu trong driver JDBC native (tr. 106–107). DBA truy vết: câu cuối cùng đọc một bảng message dùng cho JMS, bảng lẽ ra không quá 1.000 dòng nhưng giờ có hơn mười triệu. Máy chủ ứng dụng lấy *tất cả* bằng "select for update", dựng đối tượng tới khi hết bộ nhớ và sập; cơ sở dữ liệu rollback nhả khoá; máy kế tiếp bước xuống vực (tr. 107). Tới khi ổn định, Thứ Hai đen đã sang thứ Ba (tr. 107). Thiếu mệnh đề LIMIT đã biến một bảng phình bất thường thành sập toàn trang; còn vì sao bảng phình, sách để dành cho "một câu chuyện khác" (tr. 108).

> [!quote] Release It! — Ch.4 (tr. 108)
> "In the abstract, an unbounded result set occurs when the caller allows the other system to dictate terms. It is a failure in handshaking."
>
> *Nói trừu tượng, tập kết quả không giới hạn xảy ra khi bên gọi để hệ thống kia ra điều kiện. Đó là một thất bại của handshaking.*

Bên gọi phải luôn nói rõ mình sẵn sàng nhận bao nhiêu, như trường "window" của TCP hay tham số số kết quả của API tìm kiếm (tr. 108). Dạng thường gặp là duyệt quan hệ cha-con: dữ liệu dev nhỏ, nhưng sau một năm ở production, "lấy đơn hàng của khách" có thể trả về rất nhiều; ORM thường không giới hạn khi đi theo quan hệ (tr. 108). Sách ghi "không có cú pháp SQL chuẩn để giới hạn tập kết quả" và đưa công thức cho từng hệ (`TOP`, `rownum`, `LIMIT`) (tr. 108).

> [!quote] Release It! — Ch.4 (tr. 109)
> "The only sensible numbers are “zero,” “one,” and “lots,” so unless your query selects exactly one row, it has the potential to return too many."
>
> *Chỉ có ba con số có nghĩa: "không", "một" và "nhiều"; nên trừ khi truy vấn của bạn chọn đúng một dòng, nó có khả năng trả về quá nhiều.*

**Điều rút ra** (tr. 109): test với khối lượng dữ liệu cỡ production; đặt giới hạn vào cả các giao thức ứng dụng khác.

## 14. Use Timeouts: hy vọng không phải là phương pháp thiết kế

Nygard từng port thư viện socket BSD lên một môi trường UNIX chạy trên mainframe, và mã mạng "chi chít" xử lý đủ loại timeout. Đến cuối dự án, ông hiểu vì sao (tr. 111).

> [!quote] Release It! — Ch.5 (tr. 111)
> "When that happens, your code can’t just wait forever for a response that might never come; sooner or later, it needs to give up. Hope is not a design method."
>
> *Khi chuyện đó xảy ra, code của bạn không thể chờ mãi một phản hồi có thể không bao giờ tới; sớm hay muộn nó phải bỏ cuộc. Hy vọng không phải là phương pháp thiết kế.*

> [!quote] Release It! — Ch.5 (tr. 111)
> "Well-placed timeouts provide fault isolation; a problem in some other system, subsystem, or device does not have to become your problem."
>
> *Timeout đặt đúng chỗ tạo ra sự cô lập lỗi: trục trặc ở hệ thống, hệ con hay thiết bị khác không nhất thiết trở thành trục trặc của bạn.*

Thư viện client của nhà cung cấp "nổi tiếng" là không có timeout, lại giấu socket nên bạn không tự đặt được (tr. 111). Mọi resource pool chặn luồng đều phải có timeout, và hãy dùng dạng có tham số timeout của `wait()`, `poll()`, `offer()`, `tryLock()` (tr. 111–112). Gom tương tác lặp lại vào một Gateway dùng chung kiểu `JdbcTemplate` của Spring cũng giúp gắn Circuit Breaker dễ hơn (tr. 112–113).

**Về retry.** Theo Nygard, trong trung tâm dữ liệu, lỗi thường do đầu bên kia có vấn đề và thường kéo dài một lúc, nên retry nhanh rất dễ lỗi tiếp, lại bắt bên gọi chờ lâu hơn tới mức vượt timeout của họ (tr. 113). Thay vào đó: trả về ngay một kết quả (thất bại, thành công, hoặc "đã xếp hàng để làm sau"), và **xếp hàng để retry chậm**, như thư điện tử lưu-và-chuyển-tiếp (tr. 113). Với website dùng SOA, ông cho rằng "đủ nhanh" có lẽ là dưới 250 mili giây (tr. 113).

Timeouts và Fail Fast là hai mặt một đồng xu: Timeouts bảo vệ bạn khỏi lỗi của người khác, áp dụng chủ yếu cho yêu cầu *đi ra*; Fail Fast báo vì sao bạn không xử lý được, áp dụng cho yêu cầu *đi vào* (tr. 114). Timeout cũng đỡ được tập kết quả không giới hạn, nhưng ông coi đó chỉ là chữa cháy (tr. 114).

**Điều rút ra** (tr. 114): Timeouts ngăn lời gọi ra điểm tích hợp biến thành luồng bị chặn, từ đó tránh lỗi dây chuyền.

## 15. Circuit Breaker: ngừng gọi vào chỗ đang đau

Thuở điện mới vào nhà, cầu chì ra đời để cháy trước cái nhà, nhưng nó dùng một lần, và cầu chì dân dụng ở Mỹ cỡ bằng đồng xu, nên người ta thay bằng... đồng xu. "Pfft. No more house." (tr. 115). Cầu dao tự động làm cùng việc: phát hiện dùng quá mức, hỏng trước, ngắt mạch, và **đóng lại được** khi nguy hiểm qua đi (tr. 115).

> [!quote] Release It! — Ch.5 (tr. 115)
> "This differs from retries, in that circuit breakers exist to prevent operations rather than reexecute them."
>
> *Nó khác retry ở chỗ circuit breaker tồn tại để ngăn thao tác chứ không phải để chạy lại chúng.*

Cơ chế ba trạng thái (Hình 5.1, tr. 116):

```
           gọi lỗi, đếm vượt ngưỡng
   ┌────────┐ ──────────────────────────► ┌────────┐
   │ CLOSED │                             │  OPEN  │  gọi → lỗi ngay,
   │ gọi đi │ ◄─────┐                     │        │  không chạm hệ thống xa
   │ bình   │       │ thử thành công      └────────┘
   │ thường │       │                      │     ▲
   └────────┘   ┌───┴──────┐  hết thời gian│     │ thử thất bại
                │HALF-OPEN │ ◄─────────────┘     │
                │ cho một  │ ────────────────────┘
                │ lời gọi  │
                └──────────┘
```

Đóng (closed): gọi bình thường, lỗi thì ghi nhận; số lỗi (hoặc tần suất lỗi, ở bản tinh vi hơn) vượt ngưỡng thì "nhảy" sang mở (open), mọi lời gọi thất bại ngay. Sau một khoảng thời gian thích hợp, chuyển sang nửa mở (half-open): lời gọi kế tiếp được thử; thành công thì về đóng, thất bại thì về mở (tr. 115–116). Khi mở, nên ném một loại exception riêng để bên gọi xử lý khác đi; có thể đếm riêng từng loại lỗi (tr. 116–117).

Điểm Nygard nhấn mạnh nhất không phải kỹ thuật:

> [!quote] Release It! — Ch.5 (tr. 117)
> "Therefore, it is essential to involve the system’s stakeholders when deciding how to handle calls made when the circuit is open."
>
> *Vì vậy, nhất thiết phải kéo các bên liên quan của hệ thống vào khi quyết định xử lý thế nào những lời gọi xảy ra lúc mạch đang mở.*

Có nhận đơn khi không kiểm được hàng có sẵn? Khi không xác minh được thẻ? Ông thấy bàn về circuit breaker là cách mở chuyện này hiệu quả hơn là xin một tài liệu yêu cầu (tr. 117). Với vận hành: mọi lần đổi trạng thái phải được ghi log, trạng thái hiện tại phải tra được, tần suất đổi trạng thái là chỉ báo sớm của trục trặc ở nơi khác, và vận hành cần cách tự tay ngắt hay đặt lại (tr. 117). Circuit breaker hiệu quả trước integration points, cascading failures, unbalanced capacities và slow responses (tr. 117).

**Điều rút ra** (tr. 117): Timeouts phát hiện vấn đề, Circuit Breaker tránh gọi tiếp; dùng hai cái cùng nhau.

## 16. Bulkheads: cứu lấy một phần con tàu

Trên tàu thuỷ, vách ngăn kín nước chia thân tàu thành khoang; thủng một chỗ không làm chìm cả tàu (tr. 119). Dạng phổ biến nhất là dư thừa vật lý; ở quy mô lớn nhất, một dịch vụ tối quan trọng chạy trên nhiều trang trại máy chủ độc lập, một số dành riêng cho ứng dụng quan trọng. Nygard quay lại chính ca mở đầu:

> [!quote] Release It! — Ch.5 (tr. 119)
> "Such a partitioning would have allowed the airline in Chapter 2, The Exception That Grounded an Airline, on page 21 to keep checking passengers at airports, even if channel partners could not look up fares for that day’s flights."
>
> *Một cách chia như thế lẽ ra đã giúp hãng bay ở Chương 2 vẫn check-in được hành khách ở sân bay, kể cả khi các channel partner không tra được giá vé chuyến bay hôm đó.*

Ví dụ trừu tượng (Hình 5.2–5.3, tr. 119–120): Foo và Bar cùng dùng dịch vụ Baz. Foo bị tải đè hay lên cơn thì Bar cũng khổ, và liên kết ẩn này khiến chẩn đoán hiệu năng của Bar rất khó. Chia Baz thành hai pool, mỗi pool cho một client, là gỡ phần lớn liên kết ẩn (tr. 120–121).

Cái giá được nói thẳng trong khung "Bulkheads vs. Capacity": pool riêng thì mỗi client phải dự báo nhu cầu chính xác hơn, tổng công suất dự phòng phải lớn hơn so với pool chung. Lời giải Nygard gợi ý là ảo hoá: dùng chung phần cứng nhưng tạo máy ảo riêng cho từng client (tr. 121). Ranh giới chia có thể theo bên gọi, theo chức năng, hoặc theo topo hệ thống (tr. 121). Ở quy mô nhỏ hơn: gắn tiến trình vào CPU (ông từng thấy một tiến trình ăn cả tám CPU của một máy), hoặc **để dành một pool luồng cho quản trị**, để khi mọi luồng xử lý yêu cầu treo, máy vẫn trả lời được lệnh thu thập dữ liệu hay tắt máy (tr. 122).

**Điều rút ra** (tr. 123): nếu ứng dụng của bạn sập vì Chain Reactions mà kéo cả công ty dừng theo, bạn cần Bulkheads.

## 17. Steady State: hệ thống phải tự chạy mà không cần ai chạm vào

Một kỹ sư thấy gương đĩa root lệch nhau, gõ lệnh đồng bộ lại, nhưng gõ nhầm chiều, đồng bộ đĩa tốt từ chiếc đĩa mới tinh còn trống, xoá sạch hệ điều hành (tr. 124).

> [!quote] Release It! — Ch.5 (tr. 124)
> "Every single time a human touches a server is an opportunity for unforced errors."
>
> *Mỗi lần con người chạm vào máy chủ là một cơ hội cho lỗi tự đánh hỏng.*

Hệ thống cần nhiều việc tay chân thì quản trị viên quen ngồi sẵn trên đó, dẫn tới "fiddling"; nên hệ thống phải chạy được vô thời hạn mà không cần can thiệp (tr. 124). Mọi cơ chế tích luỹ tài nguyên giống cái xô trong bài toán giải tích: xả chậm hơn đổ thì sớm muộn tràn (tr. 124).

> [!quote] Release It! — Ch.5 (tr. 124)
> "The Steady State pattern says, for every mechanism that accumulates a resource, some other mechanism must recycle that resource."
>
> *Pattern Steady State nói: với mỗi cơ chế tích luỹ một tài nguyên, phải có một cơ chế khác tái chế tài nguyên đó.*

**Dọn dữ liệu.** Không demo được nên luôn bị gác lại; "sáu tháng sau ra mắt sẽ làm", giống "hai tuần" của lập trình viên (tr. 125). Triệu chứng của dữ liệu phình là I/O tăng đều, độ trễ tăng ở tải không đổi; và ứng dụng phải còn chạy khi dữ liệu biến mất khỏi giữa tập hợp (với Hibernate thì không) (tr. 125). Nygard tự thú: chính dự án của ông vẫn ra bản đầu không có dọn dữ liệu, và suýt không kịp (tr. 125–126).

**File log.** Log tăng vô hạn rồi sẽ lấp đầy hệ thống file; trên UNIX ứng dụng bắt đầu lỗi I/O khi đầy 90–95% (tr. 126). Một hệ thống có "bộ xử lý exception vạn năng" tái nhập: đĩa đầy, ghi log lỗi lại sinh lỗi, cứ thế nhân lên, ăn tám CPU, hết bộ nhớ, JVM sập (tr. 127). Lời giải rẻ: xoay vòng log theo kích thước (`RollingFileAppender`, `limit` và `count` của java.util.logging, `logrotate`), và chép log cũ sang khu phân tích (tr. 127–128).

**Cache trong bộ nhớ.** Hai câu hỏi: không gian khoá hữu hạn hay vô hạn, và phần tử có thay đổi không. Khoá vô hạn thì phải giới hạn kích thước; trừ khi khoá hữu hạn và dữ liệu tĩnh, cache cần cơ chế vô hiệu hoá; theo Nygard, chín trên mười lần một đợt xả định kỳ là đủ (tr. 129). Dùng cache sai là nguyên nhân chính của rò bộ nhớ (tr. 129).

**Điều rút ra** (tr. 129): hệ thống phải chạy ít nhất một chu kỳ deploy mà không cần dọn đĩa tay hay khởi động lại hằng đêm; dọn dữ liệu bằng logic ứng dụng chứ không phó mặc script của DBA.

## 18. Fail Fast: đã biết sẽ hỏng thì hỏng ngay

> [!quote] Release It! — Ch.5 (tr. 131)
> "If slow responses are worse than no response, the worst must surely be a slow failure response."
>
> *Nếu phản hồi chậm tệ hơn không phản hồi, thì tệ nhất hẳn là một phản hồi thất bại mà lại chậm.*

Nếu hệ thống biết trước sẽ thất bại, hãy thất bại ngay để bên gọi khỏi giam công suất. Có cả một lớp lỗi "tài nguyên không sẵn có": cân bằng tải nhận kết nối mà không còn máy nào sống thì phải từ chối ngay, xếp hàng chờ là vi phạm Fail Fast (tr. 131). Dịch vụ biết từ loại yêu cầu mình sẽ cần kết nối nào, điểm tích hợp nào, nên có thể mượn trước kết nối, kiểm trạng thái circuit breaker, như đầu bếp bày sẵn nguyên liệu (*mise en place*) trước khi nấu (tr. 131).

**Chuyện ảnh đen.** Phần mềm dựng ảnh in của một công ty chụp ảnh studio, khi thiếu profile màu, ảnh, nền hay mặt nạ alpha, vẫn "dựng" ra một ảnh đen, đem in, rồi khâu kiểm tra trả ngược về đầu dây chuyền và bản in lại phải chen hàng (tr. 131–132). Đội Nygard áp Fail Fast: nhận lệnh in là kiểm đủ tài nguyên, cấp phát trước bộ nhớ, báo lỗi ngay; tỉ lệ in lại do phần mềm về không (tr. 132). Chỗ duy nhất họ không cấp phát trước là đĩa cho ảnh thành phẩm, vì khách hàng bảo có quy trình dọn dẹp riêng, hoá ra là một anh thỉnh thoảng xoá bớt file. Gần một năm sau đĩa đầy, và đúng chỗ đó phần mềm mất vài phút rồi mới ném IOException vào log (tr. 132).

Kiểm tham số cơ bản ngay ở controller trước khi nạp đối tượng nghiệp vụ, nhưng kiểm gì phức tạp hơn thì đưa vào đối tượng nghiệp vụ (tr. 132).

> [!quote] Release It! — Ch.5 (tr. 132)
> "Even when failing fast, be sure to report a system failure (resources not available) differently than an application failure (parameter violations or invalid state)."
>
> *Ngay cả khi thất bại nhanh, hãy báo lỗi hệ thống (tài nguyên không có) khác với lỗi ứng dụng (tham số sai hay trạng thái không hợp lệ).*

Báo chung một chữ "error" có thể khiến hệ thống phía trên nhảy circuit breaker chỉ vì một người nhập sai rồi nhấn Reload ba bốn lần (tr. 132).

**Điều rút ra** (tr. 133): không đạt SLA thì báo bên gọi ngay, đừng biến vấn đề của mình thành vấn đề của họ.

## 19. Handshaking: để máy chủ được quyền nói "khoan đã"

RS-232, modem analog, TCP đều bắt tay. Handshaking có mặt khắp nơi ở tầng thấp nhưng gần như vắng bóng ở tầng ứng dụng (tr. 134). HTTP có mã 503 cho tình trạng tạm thời, nhưng hầu hết client không phân biệt mã; RMI, CORBA, DCOM cũng tệ như vậy (tr. 134).

> [!quote] Release It! — Ch.5 (tr. 134)
> "Handshaking is all about letting the server protect itself by throttling its own workload."
>
> *Handshaking là để máy chủ tự bảo vệ bằng cách điều tiết khối lượng việc của chính nó.*

Cách gần đúng nhất Nygard làm được với HTTP là cộng tác giữa cân bằng tải và máy chủ web: máy bận thì trả 503 cho trang health check, cân bằng tải ngừng gửi việc tới máy đó; cách này vẫn hỏng khi mọi máy cùng bận (tr. 134). Trong SOA, dịch vụ có thể cung cấp truy vấn "health check" để client hỏi trước, đổi lại số kết nối nhân đôi (tr. 134–135). Handshaking giá trị nhất khi công suất không cân bằng đang sinh phản hồi chậm; tốt nhất là xây nó vào giao thức tự làm (tr. 135).

> [!quote] Release It! — Ch.5 (tr. 135)
> "Circuit breakers are a stopgap you can use when calling services that cannot handshake."
>
> *Circuit breaker là giải pháp tạm bạn dùng được khi gọi những dịch vụ không biết bắt tay.*

Nygard gọi handshaking là kỹ thuật bị dùng quá ít, và là cách hiệu quả để chặn vết nứt nhảy tầng như trong lỗi dây chuyền (tr. 135).

## 20. Test Harness: một đối thủ biết chơi xấu

Môi trường test tích hợp có hai vấn đề (tr. 136). Thứ nhất, nó khoá phiên bản và rốt cuộc thành một khối duy nhất toàn doanh nghiệp, cần kiểm soát thay đổi chặt như production. Thứ hai: nó chỉ kiểm được hệ thống làm gì khi phụ thuộc chạy *đúng đặc tả*, kể cả khi phụ thuộc trả mã lỗi theo đặc tả (tr. 136).

> [!quote] Release It! — Ch.5 (tr. 136)
> "The main theme of this book, however, is that every system will eventually end up operating outside of spec; therefore, it’s vital to test the local system’s behavior when the remote system goes wonky."
>
> *Nhưng chủ đề chính của cuốn sách này là mọi hệ thống rồi sẽ chạy ra ngoài đặc tả; vì vậy, việc sống còn là test hành vi của hệ thống mình khi hệ thống bên kia trở chứng.*

Lời giải: dựng **test harness** giả làm đầu bên kia của mỗi điểm tích hợp, quỷ quyệt và xấu tính như hệ thống ngoài đời, để lại sẹo trên hệ thống được test (tr. 137). Danh sách của Nygard (tr. 137) đáng dùng làm checklist: kết nối bị từ chối; nằm trong listen queue tới khi bên gọi hết timeout; trả SYN/ACK rồi không gửi gì; chỉ gửi gói RESET; báo cửa sổ nhận đầy và không bao giờ rút; kết nối xong mà không gửi byte nào; mất gói gây trễ gửi lại; gửi header HTTP rồi không gửi body; ba mươi giây gửi một byte; gửi HTML thay vì XML; gửi megabyte khi chờ kilobyte; từ chối mọi thông tin xác thực. Môi trường tích hợp chỉ giỏi xét lỗi ở tầng thứ bảy, và cũng không hết (tr. 139).

Khác **mock object** thế nào? Khung "Joe Asks" (tr. 138): mock chỉ cư xử *đúng giao diện đã định*; test harness chạy như một máy chủ riêng, nên gây được lỗi mạng, lỗi giao thức, lỗi ứng dụng. Mẹo của Nygard: mỗi cổng một kiểu chơi xấu, cổng 10200 nhận kết nối mà không trả lời, 10201 trả lời bằng dữ liệu chép từ `/dev/random`, 10202 mở rồi cắt ngay; và nhớ cho harness ghi log yêu cầu (tr. 139).

**Điều rút ra** (tr. 140): test harness bổ sung chứ không thay thế unit test, acceptance test; nó kiểm hành vi "phi chức năng".

## 21. Decoupling Middleware: tích hợp mà không trói nhau

Middleware là cái tên vụng về cho những công cụ sống ở khe hở giữa các hệ thống vốn không được làm để chạy cùng nhau (tr. 141).

> [!quote] Release It! — Ch.5 (tr. 141)
> "Done well, middleware simultaneously integrates and decouples systems."
>
> *Làm tốt, middleware vừa tích hợp vừa tách rời các hệ thống cùng lúc.*

Lời gọi đồng bộ kiểu hỏi-đáp (RPC, HTTP, XML-RPC, RMI, CORBA, DCOM) buộc bên gọi dừng lại chờ, hai bên phải cùng sống một lúc; chúng khuếch đại cú sốc và tạo điều kiện cho lỗi dây chuyền (tr. 141). Hình 5.4 (tr. 142) xếp phổ ghép nối: gọi hàm trong tiến trình, IPC, RPC, middleware hướng message (MQ, pub-sub, SMTP, SMS), và tuple space.

> [!quote] Release It! — Ch.5 (tr. 142)
> "Message-oriented middleware decouples the endpoints in both space and time. Because the requesting system doesn’t just sit around waiting for a reply, this form of middleware cannot produce a cascading failure."
>
> *Middleware hướng message tách hai đầu cả về không gian lẫn thời gian. Vì hệ thống gửi yêu cầu không ngồi chờ phản hồi, dạng middleware này không thể sinh ra lỗi dây chuyền.*

Cái giá: đồng bộ thì logic đơn giản; bất đồng bộ thì phải xử lý hàng đợi lỗi, phản hồi muộn, callback, và cả việc người tài trợ phải quyết mức rủi ro tài chính chấp nhận được (tr. 142). Quyết định middleware đắt, đổi ý rất tốn, và thường bị quyết sẵn ở cấp doanh nghiệp (tr. 142–143).

> [!quote] Release It! — Ch.5 (tr. 143)
> "This is one of those nearly irreversible decisions that should be made early rather than late."
>
> *Đây là một trong những quyết định gần như không đảo ngược được, nên đưa ra sớm chứ không để muộn.*

*Ghi chú của khoá:* tiêu đề của ý này trong "Remember This" là "Decide at the last responsible moment"; cách đọc hợp lý là với middleware, thời điểm có trách nhiệm muộn nhất rơi rất sớm. Ở tr. 40–41, Nygard chỉ ra rằng nếu CF dùng hàng đợi request/reply, bên gọi buộc phải xử lý trường hợp phản hồi không bao giờ tới.

**Điều rút ra** (tr. 143): học nhiều phong cách kiến trúc; không phải hệ thống nào cũng cần là ba tầng với Oracle.

## 22. Bảng ghép antipattern và pattern, và lời chốt Part I

Ch.5 mở đầu bằng một cảnh báo: đừng tưởng hệ thống càng nhiều pattern càng tốt.

> [!quote] Release It! — Ch.5 (tr. 110)
> "“Count of patterns applied” is never a good quality metric."
>
> *"Số pattern đã áp dụng" không bao giờ là thước đo chất lượng tốt.*

Bảng dưới chỉ ghép khi **lời văn của sách** nối hai bên với nhau (trang ghi kèm). Dòng nào có đánh dấu *(khoá ghép)* là suy luận của khoá.

| Antipattern | Pattern chống lại, theo sách | Trang |
| --- | --- | --- |
| Integration Points | Circuit Breaker và Decoupling Middleware ("hiệu quả nhất"); thêm Timeouts, Handshaking; Test Harness cho mỗi điểm tích hợp | 59–60, 114, 117, 137 |
| Chain Reactions | Bulkheads (tách một phản ứng thành hai); Circuit Breaker ở phía bên gọi | 62, 64, 123 |
| Cascading Failures | Circuit Breaker và Timeouts ("hiệu quả nhất"); Handshaking chặn vết nứt nhảy tầng; middleware hướng message "không thể" sinh lỗi dây chuyền; Fail Fast cùng Timeouts | 65, 67, 133, 135, 142 |
| Users | Circuit Breaker chuyên biệt chống DDoS; chặn kẻ cào dữ liệu là "một dạng Circuit Breaker"; stress test deep link | 78, 79–80 |
| Blocked Threads | Timeouts; Test Harness để phá thư viện bên thứ ba; Decoupling Middleware giảm nguy cơ | 86–87, 114, 143 |
| Attacks of Self-Denial | Bulkheads (cụm riêng cho khuyến mãi); Fail Fast khi phần dành riêng tắt; decoupling middleware, shared-nothing | 88–90 |
| Scaling Effects | Thay điểm-điểm bằng multicast, pub/sub, hàng đợi; shared-nothing. *(khoá ghép: gọi nhóm này là Decoupling Middleware; sách chỉ nêu tên công nghệ)* | 92–94 |
| Unbalanced Capacities | Circuit Breaker phía front end, Handshaking phía back end, Bulkheads, Test Harness, Fail Fast | 98–99, 117, 135 |
| Slow Responses | Fail Fast; Timeouts; Circuit Breaker; Handshaking; Steady State (tích tụ "cặn" là nguyên nhân chính của chậm) | 101, 114, 117, 129, 133, 135 |
| SLA Inversion | Decoupling Middleware; Circuit Breaker trước mỗi phụ thuộc; SLA theo từng chức năng | 104–105 |
| Unbounded Result Sets | Handshaking ("một thất bại của handshaking"); Timeouts chỉ là "stopgap"; giới hạn trong truy vấn. *(khoá ghép: Steady State, vì sách nói tập kết quả không giới hạn có thể do vi phạm steady state, nhưng không gọi Steady State là cách chữa)* | 108–109, 114 |

*Ghi chú của khoá:* đếm theo bảng, **Circuit Breaker** có mặt ở 7 dòng; Timeouts, Decoupling Middleware và Handshaking mỗi cái 5 dòng (riêng với Unbounded Result Sets, sách chỉ coi Timeouts là giải pháp tạm); Fail Fast 4 dòng; Bulkheads 3 dòng. Nếu chỉ kịp làm một việc, bảng này gợi ý bắt đầu từ Circuit Breaker, và theo tr. 117, Circuit Breaker nên đi cùng Timeouts.

Ch.6 chốt Part I bằng một phép tính: mười triệu lượt xem trang mỗi ngày trong ba năm, mỗi trang năm mươi tài nguyên, là 547.500.000.000 cơ hội để có gì đó hỏng, trong khi dải Ngân Hà có khoảng bốn trăm tỉ ngôi sao (tr. 144). *Khoá tính lại:* 10.000.000 × 365 × 3 × 50 = 547,5 tỉ, khớp.

> [!quote] Release It! — Ch.6 (tr. 144)
> "Astronomically unlikely coincidences happen daily."
>
> *Những trùng hợp khó xảy ra ở mức thiên văn vẫn xảy ra hằng ngày.*

Tránh antipattern không ngăn được chuyện xấu, nhưng giảm thiệt hại khi nó tới; áp dụng pattern cần *óc phán đoán*: đọc yêu cầu một cách hoài nghi, nhìn mọi hệ thống khác bằng con mắt nghi ngờ, nhận diện mối đe doạ rồi chọn pattern hợp với từng mối (tr. 144).

> [!quote] Release It! — Ch.6 (tr. 144)
> "Paranoia is just good thinking."
>
> *Đa nghi chỉ là suy nghĩ tốt.*

Và một lời an ủi cay đắng: hệ thống không bao giờ sập thì chẳng ai để ý; người dùng sẽ phàn nàn chuyện khác, nhiều khả năng nhất là *chậm* (tr. 145). Đó là cầu nối sang Bài 2 — Công suất.

## 23. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống.**
> - *Circuit Breaker thành từ vựng chung.* Martin Fowler (bài "CircuitBreaker", 6/3/2014) ghi rằng Michael Nygard đã phổ biến pattern này. Con đường của nó đi từ tự viết như trong sách, qua thư viện Netflix Hystrix, nay Hystrix đã "no longer in active development, and is currently in maintenance mode", bản cuối là 1.5.18, và Netflix khuyên dự án mới dùng những dự án mở đang hoạt động như **resilience4j**. Resilience4j giữ đúng ba trạng thái của Hình 5.1 (CLOSED, OPEN, HALF_OPEN), thêm ba trạng thái đặc biệt (METRICS_ONLY, DISABLED, FORCED_OPEN, gần với nhu cầu "vận hành tự tay ngắt hay đặt lại" ở tr. 117), và đếm lỗi bằng cửa sổ trượt theo số lời gọi hoặc theo thời gian.
> - *Circuit breaker xuống tầng hạ tầng.* Envoy có **outlier detection**: tự phát hiện host trong cụm cư xử khác các host còn lại và loại khỏi tập cân bằng tải, host bị loại liên tiếp thì bị loại lâu dần, và có ngưỡng để không loại quá nhiều. Istio cấu hình circuit breaking và outlier detection qua DestinationRule. Đây gần như cơ chế "cân bằng tải ngừng gửi việc tới máy bận" ở mục Handshaking (tr. 134), nay chạy tự động ở sidecar.
> - *Test Harness tiến thành chaos engineering.* Principles of Chaos định nghĩa chaos engineering là "the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production", với các nguyên tắc: giả thuyết trạng thái ổn định đo bằng đầu ra, chạy thí nghiệm ở production, tự động hoá, thu nhỏ vùng ảnh hưởng. Theo trang dự án, "Chaos Monkey is responsible for randomly terminating instances in production". Theo nhà xuất bản, bản 2 của sách (1/2018) có thêm nội dung về chaos engineering. Khác biệt đáng chú ý: Nygard 2007 dựng harness ở *ngoài* production, còn chaos engineering chủ động làm *trong* production.
>
> **Phần cần chỉnh.**
> - *Retry.* Nygard khuyên tránh retry ngay, xếp hàng retry chậm (tr. 113–114). Bài "Timeouts, retries, and backoff with jitter" của Marc Brooker (Amazon Builders' Library) đi xa hơn: đặt timeout cho mọi lời gọi từ xa; retry là "selfish" vì tiêu thêm thời gian của máy chủ, và khi lỗi do quá tải thì retry làm tình hình tệ hơn; dùng **exponential backoff** có giới hạn trần; và vì các client lỗi cùng lúc sẽ retry cùng lúc, phải thêm **jitter** để rải retry theo thời gian. Chuyện "Hammer Time" ở tr. 67 chính là ca bệnh mà backoff và jitter chữa.
> - *Bulkhead bằng giới hạn tài nguyên.* Nygard gợi ý máy ảo làm vách ngăn (tr. 121). Nay Kubernetes cho đặt giới hạn tài nguyên từng container: vượt `cpu` limit thì bị bóp CPU, vượt `memory` limit thì nhân có thể giết container (OOM kill) khi có áp lực bộ nhớ. *(khoá ghép: tài liệu Kubernetes không gọi đây là "bulkhead", nhưng chức năng giống ví dụ gắn CPU ở tr. 122.)*
> - *Steady State tự động hoá.* Kubelet tự xoay vòng log container, mặc định tối đa 10Mi mỗi file và 5 file, đúng tinh thần "limit × count" ở tr. 127–128. Với cache, TTL đã thành tính năng sẵn có: lệnh `EXPIRE` của Redis đặt thời hạn cho khoá, hết hạn thì khoá tự bị xoá.
> - *"Không có cú pháp SQL chuẩn để giới hạn kết quả" (tr. 108).* Đúng lúc sách viết; nay tài liệu PostgreSQL ghi chuẩn **SQL:2008** đã đưa vào `OFFSET ... FETCH {FIRST|NEXT} ...`, còn `LIMIT`/`OFFSET` là cú pháp riêng của PostgreSQL, MySQL cũng dùng. Lời khuyên "luôn giới hạn, luôn phân trang" thì còn nguyên.
>
> **Phần đã lỗi thời.** EJB, RMI, `URLConnection` (sách ghi phải tới Java 5 mới đặt được timeout cho HTTP qua thư viện chuẩn, tr. 40), driver JDBC loại 2, ATG, VMware ESX, và mốc "đủ nhanh có lẽ là dưới 250 mili giây" (tr. 113) là bối cảnh lúc sách viết; khi đọc, giữ lấy cơ chế và tự đối chiếu với công nghệ của mình.

## 24. Áp dụng vào việc của bạn

> [!question] Khi thiết kế và viết code
> 1. **Kiểm kê điểm tích hợp.** Liệt kê mọi lời gọi ra ngoài (HTTP, cơ sở dữ liệu, cache, hàng đợi, SDK bên thứ ba). Với từng cái, ghi: timeout kết nối, timeout đọc, có circuit breaker không, hỏng thì chức năng nào chết theo. Ô nào trống là một vết nứt chưa có crackstopper (mục 3, 14, 15).
> 2. **Soi mọi khối dọn dẹp tài nguyên.** Tìm các chỗ đóng hai tài nguyên liên tiếp trong cùng một khối `finally`. Nếu lệnh đóng đầu ném lỗi, lệnh thứ hai có chạy không? Đó chính là lỗi đã làm cả hãng bay nằm đất (mục 1).
> 3. **Mọi truy vấn trả nhiều dòng phải có giới hạn**, và API của bạn phải bắt bên gọi nói rõ muốn nhận bao nhiêu (mục 13).
> 4. **Viết cột "hành vi khi mạch mở".** Với mỗi phụ thuộc, cùng người làm sản phẩm quyết: khi nó chết thì chức năng trả gì (lỗi rõ ràng, dữ liệu cũ, xếp hàng làm sau)? (mục 15)

> [!question] Khi vận hành, trực on-call, viết postmortem
> 1. **Chuẩn bị sẵn công cụ thu chứng cứ.** Script chụp thread dump, heap, kết nối mạng chạy được trong một lệnh chưa? Đội hãng bay nhờ vậy vừa khôi phục nhanh vừa giữ được chứng cứ (mục 1).
> 2. **Giám sát như người dùng.** Health check của bạn chỉ trả "OK" hay thật sự đi qua các phụ thuộc? Thêm ít nhất một giao dịch tổng hợp chạy từ bên ngoài (mục 1, 7).
> 3. **Vẽ chuỗi thất bại trong postmortem** theo khung sơ đồ ở mục 2: tác nhân khởi phát, từng bước vết nứt lan, và *ở mỗi bước lẽ ra có thể chặn bằng gì*. Hành động khắc phục nên nhắm vào chỗ chặn, không chỉ vào bug gốc, vì bug sẽ luôn có.
> 4. **Kiểm steady state.** Có việc nào đang phải làm tay định kỳ: dọn đĩa, xoá log, khởi động lại hằng đêm? Mỗi việc như vậy là một cơ chế tích luỹ chưa có cơ chế tái chế (mục 17).

## 25. Từ điển thuật ngữ

Tên 11 antipattern và 8 pattern đã là tiêu đề các mục 3–21, nên không lặp lại ở đây.

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Postmortem** | Điều tra sau sự cố để tìm nguyên nhân và cách phòng; Nygard ví với án mạng mà "cái xác" đã biến mất (tr. 28). |
| **Thread dump** | Ảnh chụp trạng thái mọi luồng của JVM; manh mối quyết định trong ca hãng bay (tr. 29–31). |
| **Impulse / Stress / Strain** | Xung lực (cú sốc nhanh) / ứng suất (lực kéo dài) / biến dạng do ứng suất sinh ra (tr. 37). |
| **Longevity** | Khả năng chạy lâu; "lâu" được định nghĩa làm việc là khoảng giữa hai lần deploy (tr. 37). |
| **Crack** (vết nứt) | Thành phần bắt đầu hỏng trước mọi thứ khác; dưới ứng suất sẽ lan (tr. 37, 39). |
| **Failure mode** | Tác nhân khởi phát + cách vết nứt lan + hậu quả (tr. 39). |
| **Crackstopper** | Cơ chế chặn vết nứt, như vùng biến dạng trên ô tô (tr. 39). |
| **Stability antipattern / pattern** | Khuôn hỏng lặp lại / khuôn thiết kế chặn vết nứt lan (tr. 42). |
| **Shared-nothing** | Kiến trúc mỗi máy tự chạy, không cần phối hợp hay dịch vụ tập trung (tr. 94). |
| **Exponential backoff / jitter** | Chờ tăng dần theo cấp số nhân giữa các lần retry / thêm ngẫu nhiên để các client không retry cùng lúc; không có trong sách, xem mục 23. |
| **Outlier detection** | Tính năng của Envoy/Istio tự loại host cư xử bất thường khỏi cân bằng tải; không có trong sách, xem mục 23. |
| **Chaos engineering** | Thí nghiệm có chủ đích trên hệ thống để tin rằng nó chịu được biến động ở production; không có trong bản 1, xem mục 23. |

## 26. Câu hỏi tự kiểm tra

1. Vì sao có thể coi failover là tác nhân kích hoạt chứ không phải nguyên nhân gốc? Sách gọi nguyên nhân là gì? *(tr. 32, 34)*
2. Vì sao giám sát không báo gì về CF trong suốt sự cố? Bài học nào cho health check của bạn? *(tr. 25, 31)*
3. Phân biệt impulse, stress và strain, mỗi cái cho một ví dụ. *(tr. 37)*
4. Nêu ít nhất bốn điểm mà vết nứt ở CF lẽ ra có thể bị chặn, từ tầng code tới tầng kiến trúc. *(tr. 39–41)*
5. Vì sao chuỗi sự cố "trông cực kỳ khó xảy ra" mà vẫn xảy ra? *(tr. 41, 144)*
6. Chain Reactions khác Cascading Failures ở đâu? Pattern nào sách chỉ định cho mỗi cái? *(tr. 61–67)*
7. Trong chuyện 5 giờ sáng, firewall đóng vai trò gì, và vì sao pool vào-sau-ra-trước làm mọi thứ tệ hơn? *(tr. 53–55)*
8. Tính lại vì sao năm phụ thuộc 99,9% kéo Frammitz xuống 99,5%. Hai cách đáp lại SLA inversion là gì? *(tr. 103–105)*
9. Vẽ sơ đồ ba trạng thái của Circuit Breaker. Vì sao Nygard nói phải kéo các bên liên quan vào? *(tr. 115–117)*
10. Timeouts và Fail Fast là "hai mặt một đồng xu" theo nghĩa nào? *(tr. 114)*
11. Theo sách, retry ngay sau timeout có vấn đề gì? Năm 2026, backoff và jitter bổ sung điều gì? *(tr. 113–114; mục 23)*
12. Test harness khác mock object ở đâu? Kể năm kiểu chơi xấu nó nên làm được. *(tr. 137–139)*

## Tóm tắt một trang

```
BÀI 1 — ỔN ĐỊNH: VẾT NỨT NÀO CŨNG SẼ ĐẾN, ĐỪNG ĐỂ NÓ LAN
────────────────────────────────────────────────────────────────
CA MỞ ĐẦU (Ch.2)  Failover Oracle → Statement.close() ném SQLException
         → rò kết nối → pool 40 cạn → CF treo → RMI không timeout
         → ki-ốt + IVR toàn quốc đỏ → hàng tồn tới 3 giờ chiều, lên TV.
         "Bugs will happen... they must be survived instead." (tr. 34)

KHUNG (Ch.3)  Phần mềm phải HOÀI NGHI. Resilient = vẫn xử lý transaction
         dù có impulse, stress, linh kiện hỏng.
         Failure mode = khởi phát + đường lan + hậu quả. Crackstopper.
         Ghép chặt làm vết nứt lan nhanh. Mắt xích KHÔNG độc lập.

11 ANTIPATTERN  Integration Points (số 1) · Chain Reactions · Cascading ·
         Users · Blocked Threads · Self-Denial · Scaling · Unbalanced ·
         Slow Responses · SLA Inversion · Unbounded Result Sets
8 PATTERN  Timeouts · Circuit Breaker · Bulkheads · Steady State ·
         Fail Fast · Handshaking · Test Harness · Decoupling Middleware

CẶP HAY GẶP  Circuit Breaker: IP, Cascading, Unbalanced, Slow (tr. 117).
         Timeouts: IP, Blocked Threads, Slow → tránh Cascading (tr. 114).
         "Count of patterns applied" KHÔNG phải thước đo chất lượng.

CH.6     547,5 tỉ cơ hội hỏng trong 3 năm. "Paranoia is just good thinking."

2026     Hystrix → maintenance, dùng resilience4j; Envoy/Istio outlier
         detection. Retry: exponential backoff + JITTER (AWS).
         Test Harness → chaos engineering. Log rotation, TTL, FETCH FIRST.
```

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software* (Pragmatic Bookshelf, 2007), `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`: Ch.2 (`tr. 21–34`), Ch.3 (`tr. 35–43`), Ch.4 (`tr. 44–109`), Ch.5 (`tr. 110–143`), Ch.6 (`tr. 144–145`). Quy ước trích: `tr. X` = số trang in = số trang PDF.
- Nguồn web dùng ở Đối chiếu 2026 (truy cập 9/2026):
  - Martin Fowler, "CircuitBreaker" (6/3/2014): https://martinfowler.com/bliki/CircuitBreaker.html
  - Netflix, Hystrix README (maintenance mode, bản 1.5.18, khuyên resilience4j): https://github.com/Netflix/Hystrix
  - Resilience4j, "CircuitBreaker": https://resilience4j.readme.io/docs/circuitbreaker
  - Envoy, "Outlier detection": https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/outlier
  - Istio, "Circuit Breaking": https://istio.io/latest/docs/tasks/traffic-management/circuit-breaking/
  - Marc Brooker, "Timeouts, retries, and backoff with jitter", Amazon Builders' Library (bản PDF chính thức): https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/developer-tools/approved/pdfs/timeouts-retries-and-backoff-with-jitter.pdf
  - Kubernetes, "Resource Management for Pods and Containers": https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
  - Kubernetes, "Logging Architecture": https://kubernetes.io/docs/concepts/cluster-administration/logging/
  - Redis, "EXPIRE": https://redis.io/docs/latest/commands/expire/
  - PostgreSQL, "SELECT" (mục Compatibility): https://www.postgresql.org/docs/current/sql-select.html
  - Principles of Chaos Engineering: https://principlesofchaos.org/
  - Netflix, Chaos Monkey: https://netflix.github.io/chaosmonkey/
  - Pragmatic Bookshelf, *Release It! Second Edition*: https://pragprog.com/titles/mnee2/release-it-second-edition/

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 ← bạn đang ở đây] · [Bài 2 — Công suất](bai_02_cong_suat.md) · [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md) · [Bài 4 — Vận hành](bai_04_van_hanh.md)

Xem thêm [README khoá học](../README.md).
