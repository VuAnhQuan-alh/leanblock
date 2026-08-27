# Mở rộng Bitcoin — từ bất đồng tới Lightning

> Bài học dựa trên **hai video** của kênh *Simply Explained – Savjee*:
> · **"What is a Bitcoin hard fork?"** (`XCo6yyutYAM`, 4:30)
> · **"Bitcoin's Lightning Network"** (`rrr_zPmEiME`, 5:19)
>
> Hai video này gộp làm một bài vì chúng là **hai nửa của cùng một câu chuyện**: cuộc tranh cãi về kích thước block giai đoạn 2015–2017 đẻ ra đúng hai lời giải — *tách chuỗi ra làm hai* và *đẩy giao dịch ra khỏi chuỗi*. Học riêng lẻ thì mất mất phần hay nhất.
> Phần **📚 Lý thuyết bổ sung** là phần video bỏ trống. Với bài này, phần bỏ trống lớn hơn phần video nói — hai video cộng lại chỉ 1.600 từ.
>
> ⚠️ **Video Lightning ghi cuối 2017**, khi Lightning mới chỉ chạy trên testnet và diễn giả đoán *"chắc là 2018"*. [§11](#11--lightning-tới-2026) đối chiếu với thực tế.
>
> 📌 **Cần đọc trước:** [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) phần fork và quản trị, [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) phần timelock/HTLC và SegWit. Bài này nối thẳng vào chỗ Bài 6 dừng lại.

---

## Mục lục

1. [Hai video, một câu chuyện](#1-hai-video-một-câu-chuyện)
2. [Fork — cơ chế tách một blockchain](#2-fork--cơ-chế-tách-một-blockchain)
3. [📚 Chuyện gì thật sự xảy ra với các fork 2017](#3--chuyện-gì-thật-sự-xảy-ra-với-các-fork-2017)
4. [Bài toán mở rộng quy mô](#4-bài-toán-mở-rộng-quy-mô)
5. [Kênh thanh toán — cách video mô tả](#5-kênh-thanh-toán--cách-video-mô-tả)
6. [📚 Bảng cân đối cũ vẫn có chữ ký hợp lệ](#6--bảng-cân-đối-cũ-vẫn-có-chữ-ký-hợp-lệ)
7. [📚 Watchtower — cái giá của việc phải luôn online](#7--watchtower--cái-giá-của-việc-phải-luôn-online)
8. [Định tuyến qua trung gian](#8-định-tuyến-qua-trung-gian)
9. [📚 HTLC — cơ chế thật đằng sau "chuyển qua Bob"](#9--htlc--cơ-chế-thật-đằng-sau-chuyển-qua-bob)
10. [📚 Thanh khoản — giới hạn không ai nói trước](#10--thanh-khoản--giới-hạn-không-ai-nói-trước)
11. [📚 Lightning tới 2026](#11--lightning-tới-2026)
12. [📚 Fork hay lớp 2 — hai lời giải cho cùng một câu hỏi](#12--fork-hay-lớp-2--hai-lời-giải-cho-cùng-một-câu-hỏi)
13. [Code minh hoạ](#13-code-minh-hoạ)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Hai video, một câu chuyện

Hai video được đăng cách nhau vài tháng và không nhắc tới nhau. Nhưng đặt cạnh nhau thì lộ ra chúng nói về **cùng một cuộc tranh cãi**:

```
        Bitcoin 2015–2017: block 1MB đã đầy, phí tăng, giao dịch chờ hàng giờ
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
        "LÀM BLOCK TO RA"                 "ĐỪNG ĐỤNG VÀO BLOCK,
                                           ĐẨY GIAO DỊCH RA NGOÀI"
                    │                               │
                    ▼                               ▼
        hard fork 1/8/2017                SegWit (soft fork 24/8/2017)
        -> Bitcoin Cash                    -> mở đường cho Lightning
                    │                               │
              VIDEO 1                          VIDEO 2
```

Cả hai đều là câu trả lời cho *"7 giao dịch mỗi giây là quá ít"*. Một bên đổi luật của chuỗi. Một bên giữ nguyên luật và xây thêm một tầng bên trên. Bài này đi theo đúng thứ tự đó.

> [Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) đã dựng phần **quản trị** của câu chuyện này khá kỹ — BIP9 version bits, UASF/BIP148, cuộc chiến kích thước block. Bài này không lặp lại; nó đi vào **cơ chế**.

---

## 2. Fork — cơ chế tách một blockchain

Video 1 mở bằng một quan sát đơn giản: **Bitcoin là phần mềm**, và phần mềm thì không bao giờ xong.

> `00:35` *"Phần mềm này gọi là giao thức Bitcoin, nó đặt ra các luật mà ai muốn dùng Bitcoin đều phải đồng ý — block to bao nhiêu, thợ đào được thưởng gì, phí tính thế nào…"*

Rồi bất đồng nảy sinh — và video chỉ ra **hai nhóm** có thể bất đồng vì hai lý do khác nhau:

| Ai                         | Vì sao bất đồng                                   |
| -------------------------- | ------------------------------------------------- |
| **Lập trình viên** `01:12` | không đồng ý với hướng đi của dự án               |
| **Thợ đào** `01:19`        | bản cập nhật có thể **làm giảm lợi nhuận của họ** |

Hàng thứ hai đáng chú ý: video nói thẳng rằng thợ đào bỏ phiếu bằng **túi tiền**, không phải bằng lý tưởng kỹ thuật. Đó là mấu chốt của cả cuộc chiến 2017.

### Cơ chế tách

Bitcoin gồm hai mảnh: **giao thức** (mã nguồn) và **blockchain** (lịch sử giao dịch). Fork chỉ đụng vào mảnh đầu:

```
   1. Sao chép mã nguồn Bitcoin        (làm được vì Bitcoin là mã nguồn mở  01:54)
   2. Sửa theo ý mình
   3. Chọn một SỐ HIỆU KHỐI làm điểm kích hoạt   02:05
      ví dụ: "fork của tôi có hiệu lực từ khối 480.000"

              ...477  478  479  ┃  480  481  482  ...   chuỗi gốc
                                ┃
                                ┗━ 480' 481' 482' ...   chuỗi fork điểm tách
   4. Từ khối đó, hai chuỗi KHÔNG CÒN TƯƠNG THÍCH   02:33
```

**Vì fork dựng trên lịch sử cũ, mọi giao dịch trước điểm tách tồn tại trên cả hai chuỗi.** Nên ai có 1 BTC trước fork thì sau fork có 1 BTC **và** 1 đồng mới.

> `02:55` *"Một số người gọi đó là tiền chùa, nhưng còn tuỳ đồng mới có hút được giá trị thật hay không."*

Câu hedge này đúng, và [§3](#3--chuyện-gì-thật-sự-xảy-ra-với-các-fork-2017) cho thấy nó đúng đến mức nào.

### Hard fork vs soft fork

Video định nghĩa ở `03:51`, và đây là chỗ **ngắn gọn tới mức dễ gây hiểu nhầm**:

> *"Hard fork là khi bạn fork Bitcoin và làm nó **không tương thích** với bản gốc. Còn nếu bạn fork mà giữ **tương thích** thì gọi là soft fork. Một khác biệt tinh tế."*

Không phải "tinh tế" — đó là khác biệt **quyết định ai bị ép nâng cấp**:

```
   SOFT FORK — luật mới CHẶT HƠN                HARD FORK — luật mới NỚI RA
   ─────────────────────────────                ──────────────────────────
   Block hợp lệ theo luật mới                   Block hợp lệ theo luật mới
   thì cũng hợp lệ theo luật cũ                 lại VI PHẠM luật cũ
        ↓                                            ↓
   Node cũ không nâng cấp vẫn chạy được         Node cũ TỪ CHỐI -> tách chuỗi
   (nó chỉ không hiểu tính năng mới)            -> ai không nâng cấp là rớt lại
        ↓                                            ↓
   SegWit đi đường này                          Bitcoin Cash đi đường này
```

Ví dụ cụ thể: giảm giới hạn block từ 1MB xuống 0,5MB là **soft fork** (block 0,5MB vẫn hợp lệ với node cũ). Tăng lên 2MB là **hard fork** (node cũ thấy block 2MB là sai luật, vứt đi).

[Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) mô tả cách **kích hoạt** một soft fork trong thực tế — BIP9 version bits và cú UASF/BIP148 — nên ở đây không lặp lại.

---

## 3. 📚 Chuyện gì thật sự xảy ra với các fork 2017

Video kết thúc bằng dự đoán ở `04:10`: *"tiền mã hoá càng phổ biến thì bất đồng càng nhiều, và sẽ càng có nhiều fork."* Gần mười năm sau, ta có dữ liệu.

### Số phận các fork Bitcoin

| Fork                                     | Ngày      | Chủ trương                       | Tới 2026                                                          |
| ---------------------------------------- | --------- | -------------------------------- | ----------------------------------------------------------------- |
| **Bitcoin Cash (BCH)**                   | 1/8/2017  | block 8MB, sau nâng tiếp         | Còn sống, nhưng giá và hashrate chỉ bằng một phần rất nhỏ Bitcoin |
| **Bitcoin Gold (BTG)**                   | 10/2017   | đổi thuật toán đào để chống ASIC | **Bị tấn công 51% hai lần** (2018, 2020), gần như chết            |
| **Bitcoin SV**                           | 11/2018   | fork tiếp từ BCH, block khổng lồ | Bị nhiều sàn lớn huỷ niêm yết                                     |
| **Bitcoin Diamond, Private, Cash Plus…** | 2017–2018 | đủ loại                          | Hầu như đã biến mất                                               |

> 💥 **Bitcoin Gold là bài học rõ nhất.** Fork thì chia đôi *người dùng*, nhưng nó cũng chia đôi **hashrate** — và an ninh Proof of Work tỉ lệ thuận với hashrate ([Bài 7](../ly_thuyet/lesson_7_do_kho_dao.md)). Một chuỗi nhỏ dùng cùng thuật toán băm với một chuỗi lớn thì kẻ tấn công chỉ cần **thuê** một phần công suất của chuỗi lớn trong vài giờ. Đúng điều đã xảy ra.
>
> Nói cách khác: **"tiền chùa" không miễn phí — nó được trả bằng an ninh của chính chuỗi mới.**

### Cái video quên nói: tấn công phát lại

Đây là khoảng trống nguy hiểm nhất của video 1.

Sau fork, hai chuỗi có **cùng định dạng giao dịch và cùng khoá riêng**. Nghĩa là:

```
   An ký giao dịch "gửi 1 BTC cho Bình" và phát lên chuỗi gốc.
   Bình (hoặc bất kỳ ai) lấy đúng giao dịch đó, phát lên CHUỖI FORK.
   Chữ ký vẫn đúng. Chuỗi fork chấp nhận.
   -> An mất luôn 1 đồng trên chuỗi fork mà không hề định gửi.
```

Đây là **replay attack**, và nó là chuyện có thật:

- **Bitcoin Cash** có phòng vệ ngay từ đầu (thêm một cờ vào cách ký giao dịch, khiến chữ ký chỉ hợp lệ trên đúng một chuỗi).
- **Ethereum Classic** thì **không** có ngay khi tách năm 2016. Người dùng và cả sàn giao dịch đã mất tiền vì chuyện này, và phải mất nhiều tháng mới có bản vá.

Bài học: khi một chuỗi tách, câu hỏi đầu tiên không phải *"tôi được bao nhiêu tiền chùa"* mà là *"chuỗi mới có phòng vệ phát lại chưa"*.

---

## 4. Bài toán mở rộng quy mô

Video 2 mở đầu bằng đúng so sánh mà [Bài 9](lesson_9_tien_ma_hoa_toan_canh.md) và [Bài 10](lesson_10_tai_chinh_phi_tap_trung.md) cũng dùng:

|                     | Giao dịch/giây                    |
| ------------------- | --------------------------------- |
| **VISA** `00:09`    | trung bình ~4.000, tối đa ~65.000 |
| **Bitcoin** `00:20` | **7**                             |

> `00:31` *"Rõ ràng chuỗi chính không mở rộng được. Nhưng nó không nhất thiết phải mở rộng!"*

Và đó là ý tưởng cốt lõi:

> `00:42` **"Giao dịch nhỏ, hằng ngày thì không cần lưu lên chuỗi chính."**
> Cách tiếp cận này gọi là **off-chain** — ngoài chuỗi.

Ví dụ của video rất đắt: Bob mua cà phê mỗi sáng. Ghi một giao dịch lên blockchain cho một ly cà phê là *"quá lố"* — **phí có khi cao hơn giá ly cà phê**.

> 🔍 **Một đính chính nhỏ.** Video nói 7 giao dịch/giây *"với kích thước block 1MB hiện tại"*. Sau khi SegWit kích hoạt (8/2017 — vài tháng trước video này), giới hạn không còn tính bằng megabyte mà bằng **đơn vị trọng số**, và block thực tế thường nặng 1,5–2,5 MB. Con số thực dao động khoảng **7–15 giao dịch/giây** tuỳ loại giao dịch. Không đổi kết luận. [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) giải thích SegWit.

---

## 5. Kênh thanh toán — cách video mô tả

Đây là phần video làm tốt nhất. Tóm lại bằng đúng trình tự của nó.

### Bước 1 — Mở kênh (trên chuỗi)

Bob và quán cà phê cùng nạp tiền vào một **địa chỉ đa chữ ký** `01:16`:

> `01:33` *"Địa chỉ đa chữ ký về cơ bản như một cái két chỉ mở được khi **cả hai bên đồng ý**."*

Video chọn số cụ thể: Bob nạp **0,05 BTC**, quán nạp **0** — *"vì họ không hoàn tiền"*.

Kèm theo là một **bảng cân đối** `01:40` ghi tiền trong két chia thế nào:

```
   BẢNG CÂN ĐỐI SỐ 0          két: 0,05 BTC
   ────────────────────
   Bob   0,05 BTC
   Quán  0,00 BTC
```

> `01:57` Mở kênh **diễn ra trên chuỗi chính**, để mọi thứ minh bạch — quán nhìn thấy Bob đã nạp thật, và yên tâm là sẽ lấy được tiền khi đóng kênh.

### Bước 2 — Tiêu tiền (ngoài chuỗi)

Cà phê giá 0,001 BTC. Trả tiền = **sửa bảng cân đối rồi cả hai cùng ký** `02:38`:

```
   BẢNG SỐ 1                  BẢNG SỐ 2                  BẢNG SỐ 50
   Bob   0,049                Bob   0,048       ...      Bob   0,000
   Quán  0,001                Quán  0,002                Quán  0,050
   ↑ cả hai ký, mỗi bên giữ một bản, KHÔNG gửi đi đâu cả
```

> `02:54` *"Hai người có thể thực hiện **hàng trăm nghìn** giao dịch với nhau. Thật sự không có giới hạn, vì chuyện này xảy ra ngoài chuỗi chính."*

### Bước 3 — Đóng kênh (trên chuỗi)

Bất cứ lúc nào, **bên nào cũng** đóng được `03:05`: lấy bảng cân đối mới nhất đã có đủ chữ ký, phát lên mạng Bitcoin. Thợ đào kiểm chữ ký rồi giải ngân theo bảng. **Một giao dịch duy nhất.**

```
   TỔNG KẾT: 50 ly cà phê  =  2 giao dịch on-chain (mở + đóng)
```

Chạy [demo 1 §13](#13-code-minh-hoạ):

```
  So ly ca phe : 50
  Cham blockchain: 2 giao dich (mo + dong)
  Neu lam thang tren chuoi: 50 gd x 0.00002 BTC = 0.00100 BTC
  Qua kenh                : 2 gd x 0.00002 BTC = 0.00004 BTC
  -> Tiet kiem 96.0% phi
```

Và video nói thêm một câu rất quan trọng ở `03:48`: vì **cả hai bên đều giữ bảng đã ký**, mỗi bên có thể tự đóng kênh bất cứ lúc nào, **kể cả khi bên kia không hợp tác nữa**. Bob không giữ được tiền của quán làm con tin, và ngược lại.

---

## 6. 📚 Bảng cân đối cũ vẫn có chữ ký hợp lệ

Ở `03:43` video nói một câu, rồi đi tiếp luôn:

> *"Hệ thống bảo đảm rằng **chỉ bảng cân đối đã ký mới nhất** mới dùng được để mở khoá tiền."*

**Bảo đảm bằng cách nào?** Đây là câu hỏi hay nhất của cả video, và nó không trả lời. Mà không trả lời thì cả thiết kế sụp đổ, vì:

```
   Sau 30 ly cà phê:      Bob 0,02  |  quán 0,03      <- bảng số 30
   Nhưng bảng số 0 vẫn:   Bob 0,05  |  quán 0,00
                          ↑ VẪN CÓ ĐỦ HAI CHỮ KÝ HỢP LỆ
```

Blockchain không biết bảng nào mới hơn. Nó chỉ thấy hai chữ ký đúng. Bob phát bảng số 0 lên là **lấy lại toàn bộ tiền đã tiêu**. Chạy demo 2:

```
  [Kenh NGAY THO] Bob phat bang so 0 len chuoi:
    Chuoi thay 2 chu ky dung -> chap nhan. Bob lay lai 0.05000 BTC.
    Quan mat 0.03000 BTC. GIAN LAN THANH CONG.
```

### Bản vá thật: bí mật thu hồi và giao dịch trừng phạt

Cách Lightning giải là **không** chặn việc phát bảng cũ — mà làm cho việc đó **lỗ nặng**.

```
   Mỗi lần chuyển sang bảng mới, bạn TRAO cho đối phương
   "bí mật thu hồi" của bảng CŨ.

   Ai phát một bảng đã bị thu hồi lên chuỗi:
     · tiền của người đó bị KHOÁ THỜI GIAN vài trăm khối
     · trong khoảng đó, đối phương trình bí mật thu hồi
       -> lấy SẠCH tiền trong kênh, kể cả phần đáng lẽ của kẻ gian
```

Demo 2 chạy tiếp:

```
  [Kenh LIGHTNING] Bob phat bang so 0 len chuoi:
    PHAT: quan trinh bi mat thu hoi #0 -> cuop SACH 0.05000 BTC
    Bob dinh an cap 0.03000 BTC, ket cuc mat ca 0.05000 BTC.
```

> **An ninh của Lightning không phải "không thể gian lận" mà là "gian lận thì lỗ nhiều hơn được".** Đây là an ninh **kinh tế**, không phải an ninh **mật mã** — cùng một loại lập luận với 51% ở [Bài 1 §7](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) và với đặt cọc/slashing ở [Bài 5](../ly_thuyet/lesson_5_proof_of_stake.md). Ba lần trong khoá học, cùng một khuôn: *không cấm được thì làm cho nó không đáng.*

Và điều này chỉ đúng khi thứ nữa được thoả mãn — xem mục sau.

---

## 7. 📚 Watchtower — cái giá của việc phải luôn online

Cơ chế trừng phạt có một điều kiện ngầm: **phải có ai đó nhìn thấy hành vi gian lận trong khoảng thời gian khoá**.

```
   Bob phát bảng cũ ──▶ đồng hồ bắt đầu chạy (vd 144 khối ≈ 1 ngày)
                              │
              quán ONLINE ────┼──── quán OFFLINE (đi nghỉ, mất điện, hỏng máy)
                    │                        │
              thấy, trừng phạt          hết hạn, Bob rút tiền
              -> Bob mất sạch           -> GIAN LẬN THÀNH CÔNG
```

Đây là khác biệt lớn nhất giữa Lightning và Bitcoin lớp nền, và video hoàn toàn không nhắc:

|                       | Bitcoin lớp nền | Lightning                       |
| --------------------- | --------------- | ------------------------------- |
| Bạn offline một năm   | tiền vẫn nguyên | **có thể mất kênh**             |
| Cần theo dõi liên tục | không           | **có**                          |
| Ai theo dõi hộ        | không cần       | **watchtower** (thường trả phí) |

**Watchtower** là dịch vụ giữ hộ bạn các "giao dịch trừng phạt" đã ký sẵn và thay bạn canh chuỗi. Nó không cần biết bạn là ai và không cầm được tiền của bạn — nhưng nó vẫn là **một bên thứ ba nữa** trong một hệ thống bán mình bằng khẩu hiệu không cần bên thứ ba.

> 📌 Đây là mẫu hình lặp lại khắp khoá học: mỗi tầng tiện lợi thêm vào lại kéo theo một giả định về sự tin cậy. Xem [Bài 9 §7](lesson_9_tien_ma_hoa_toan_canh.md#7-mua-ở-đâu-và-nó-nằm-ở-đâu) với sàn tập trung, và [§11](#11--lightning-tới-2026) dưới đây với ví Lightning lưu ký.

---

## 8. Định tuyến qua trung gian

Từ `04:03`, video giải quyết phản biện hiển nhiên: *chẳng lẽ phải mở kênh với từng người mình muốn trả tiền?*

> *"Không cần. Bạn dùng luôn mạng lưới để **chuyền tiền qua**."*

Ví dụ của video: Alice là bạn Bob, hai người đã có kênh sẵn. Alice muốn mua cà phê nhưng không có kênh với quán. Vậy Alice chuyển tiền cho Bob, và Bob chuyển tiếp cho quán.

```
        Alice ──kênh sẵn──▶ Bob ──kênh sẵn──▶ Quán
              (không cần kênh Alice ↔ Quán)
```

> `04:36` *"Thanh toán sẽ tìm một đường đi từ người A tới người B, cố đi qua **ít trung gian nhất và ít phí nhất**."*

Và video kết bằng một cảnh báo đúng nhưng chưa khai thác: *"…nhưng đòi hỏi các trung gian **có đủ tiền trong kênh của họ**"* `04:47`. Đó chính là [§10](#10--thanh-khoản--giới-hạn-không-ai-nói-trước).

---

## 9. 📚 HTLC — cơ chế thật đằng sau "chuyển qua Bob"

Câu hỏi video không đặt ra: **lấy gì bảo đảm Bob không nuốt luôn tiền của Alice?**

Nếu Alice cứ thế trả cho Bob và tin Bob chuyển tiếp, thì ta vừa phát minh lại **ngân hàng**. Lời giải là **HTLC** — hợp đồng khoá bằng hash và thời gian, thứ mà [Bài 6](../ly_thuyet/lesson_6_vi_bitcoin.md) đã dựng nhưng chưa dùng tới.

### Cách chạy

```
   1. QUÁN tạo một bí mật R, tính H = sha256(R),
      gửi H cho Alice trong hoá đơn.  (Chỉ quán biết R.)

   2. Alice khoá tiền cho Bob:  "ai trình được R sao cho sha256(R)=H thì lấy được,
                                 không thì sau 144 khối tiền tự về lại Alice"

   3. Bob khoá tiền cho Quán:   cùng H, nhưng hạn NGẮN HƠN — 72 khối

   4. Quán trình R -> lấy tiền từ Bob.  Bob GIỜ ĐÃ BIẾT R.
   5. Bob dùng chính R đó -> lấy tiền từ Alice, ăn phần chênh làm tiền công.
```

Chạy demo 3:

```
  [khoa] Alice -> Bob: 0.00101 BTC khoa boi H
  [khoa] Bob -> Quan: 0.00100 BTC khoa boi H

  [mo] Quan trinh R -> lay 0.00100 BTC tu Bob
  [mo] Bob GIO DA BIET R -> lay 0.00101 BTC tu Alice
       Bob lai 0.00001 BTC tien cong chuyen tiep
```

### Vì sao Bob không ăn chặn được

| Bob thử làm gì              | Kết quả                                                        |
| --------------------------- | -------------------------------------------------------------- |
| Giữ tiền, không chuyển tiếp | Không ai đưa R cho Bob → Bob **không lấy được** tiền của Alice |
| Đổi số tiền giữa đường      | R chỉ mở được đúng khoản đã khoá, không mở khoản khác          |
| Quán im lặng, không trình R | Hết hạn → **mọi khoá tự hoàn tiền ngược lại**, không ai mất gì |

> **Toàn bộ đường đi là nguyên tử: hoặc cả chuỗi thành công, hoặc không ai mất một xu.** Đúng tính chất đã gặp ở [flash loan bài 10](lesson_10_tai_chinh_phi_tap_trung.md#11--vay-chớp-nhoáng--thứ-chỉ-tồn-tại-được-nhờ-tính-nguyên-tử), chỉ khác là ở đây nó trải qua nhiều máy và nhiều giờ chứ không nằm trong một giao dịch.

### Chi tiết chết người: thời hạn phải giảm dần

```
    Alice -> Bob    hết hạn sau 144 khối  (~24 giờ)
    Bob   -> Quán   hết hạn sau  72 khối  (~12 giờ)
                    ↑ chặng SAU phải ngắn hơn chặng TRƯỚC
```

Nếu làm ngược lại: quán lấy tiền của Bob ở giờ thứ 20, nhưng khoá Alice→Bob đã hết hạn ở giờ thứ 12 và tiền đã về lại Alice. **Bob trả tiền cho quán bằng tiền túi.** Cứ mỗi chặng lại phải chừa một khoảng an toàn, nên đường đi càng dài thì tiền của người gửi càng bị treo lâu trong tình huống xấu.

---

## 10. 📚 Thanh khoản — giới hạn không ai nói trước

Đây là thứ khiến người dùng Lightning thật hay bực mình, và cả hai video đều không chạm tới.

### Kênh có chiều

```
   Mở kênh: Bob 0,05 BTC │ quán 0,00 BTC

   Bob GỬI được tối đa   : 0,05 BTC
   Bob NHẬN được tối đa  : 0,00 BTC   <- BẰNG KHÔNG
   Quán GỬI được tối đa  : 0,00 BTC   <- BẰNG KHÔNG
```

Tiền không tự sinh ra trong kênh — nó chỉ **trượt qua lại** giữa hai đầu. Nghĩa là:

- **Muốn NHẬN tiền, đối phương phải đang giữ tiền ở đầu bên kia.** Người dùng mới mở ví Lightning rồi bảo bạn bè "chuyển tiền cho tao" sẽ thất bại, vì họ chưa có thanh khoản vào.
- Sau 50 ly cà phê, kênh của Bob **cạn một chiều**. Muốn mua tiếp thì phải đóng kênh và mở lại — **thêm 2 giao dịch on-chain nữa**.

### Định tuyến chỉ đi được khi MỌI chặng đủ thanh khoản đúng chiều

Demo 4:

```
  Dinh tuyen 0.00100 BTC qua 3 chang:
    Alice->Bob   thanh khoan ra ngoai 0.00200 BTC  ok
    Bob->Carol   thanh khoan ra ngoai 0.00050 BTC  <-- NGHEN
    Carol->Quan  thanh khoan ra ngoai 0.01000 BTC  ok
  Ket qua: THAT BAI — phai tim duong khac
```

Và điểm cay nhất: **số dư từng chiều của mỗi kênh là riêng tư.** Mạng lưới công khai *sức chứa* của kênh, không công khai tiền đang nằm ở đầu nào. Người gửi phải **đoán đường rồi thử**, thất bại thì thử đường khác.

> Đây là lý do thanh toán Lightning thỉnh thoảng báo lỗi mà không nói được vì sao, và vì sao khoản càng lớn càng dễ hỏng. Nó cũng là lý do mạng lưới có xu hướng **tụ lại quanh vài nút lớn** có nhiều thanh khoản — một áp lực tập trung hoá ngay bên trong một thiết kế phi tập trung.

---

## 11. 📚 Lightning tới 2026

Video kết ở `04:55`: *"khi nào nó lên sóng thật?"* → hiện có bản chạy thử trên testnet, *"khả năng là trong 2018"*.

**Dự đoán này đúng.** Bản chạy chính thức trên mạng thật ra mắt đầu 2018. Nhưng "chạy được" và "dùng được" là hai chuyện, nên đây là bảng đối chiếu:

| Video 2017 nói/ngụ ý           | Thực tế tới 2026                                                                        |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| Sẽ lên sóng năm 2018           | ✅ Đúng — mainnet beta đầu 2018                                                          |
| Giải bài toán mở rộng          | 🟡 Đúng về kỹ thuật. Nhưng phần lớn giao dịch Bitcoin vẫn nằm trên chuỗi chính           |
| Ai cũng mở kênh với ai         | 🔴 Không. Mạng tụ quanh một số nút lớn, và **đa số người dùng phổ thông dùng ví lưu ký** |
| Hai giao dịch on-chain là xong | 🟡 Đúng, nhưng khi phí chuỗi chính tăng cao thì **mở kênh cũng trở nên đắt**             |

Vài điểm cụ thể đáng biết:

- **Công suất công khai của mạng dao động quanh vài nghìn BTC suốt nhiều năm** và không tăng theo cấp số nhân như kỳ vọng ban đầu. Cần nhớ đây chỉ là kênh **công khai** — kênh riêng không nhìn thấy được, nên mọi thống kê Lightning đều là ước lượng dưới.
- **Ví lưu ký thắng về số người dùng.** Phần lớn người thật dùng Lightning qua một ứng dụng giữ hộ khoá — không có kênh, không có watchtower, không có gì để canh. Tiện, và **đúng bằng cách vứt bỏ toàn bộ lý do tồn tại của Lightning**. Đây lại là [nghịch lý trung tâm của Bài 9](lesson_9_tien_ma_hoa_toan_canh.md#7-mua-ở-đâu-và-nó-nằm-ở-đâu), lặp lại ở tầng khác.
- **Taproot (2021) làm kênh Lightning trông giống giao dịch thường**, tăng riêng tư và giảm phí đóng kênh.
- Các cải tiến sau này tập trung vào đúng ba đau đầu ở [§7](#7--watchtower--cái-giá-của-việc-phải-luôn-online) và [§10](#10--thanh-khoản--giới-hạn-không-ai-nói-trước): thay đổi sức chứa kênh mà không cần đóng/mở lại, hoá đơn tái sử dụng được, và dịch vụ cấp thanh khoản vào cho người dùng mới.

> 🔍 **Nhận định trung thực:** Lightning **hoạt động**, và cho đúng thứ nó được thiết kế — trả tiền nhỏ, nhanh, phí gần bằng không, giữa các bên có kênh. Nó **không** trở thành lớp thanh toán mặc định của thế giới. Rào cản không phải mật mã; là thanh khoản, là yêu cầu online, và là việc người dùng luôn chọn tiện hơn an toàn.

---

## 12. 📚 Fork hay lớp 2 — hai lời giải cho cùng một câu hỏi

Giờ mới trả lời được câu hỏi mở đầu bài.

|                   | **Fork: làm block to ra**                           | **Lớp 2: đẩy ra ngoài chuỗi**                      |
| ----------------- | --------------------------------------------------- | -------------------------------------------------- |
| Ai chịu chi phí   | **mọi node** phải lưu và xác minh nhiều dữ liệu hơn | chỉ hai bên trong kênh                             |
| Hệ quả lâu dài    | chạy node đắt dần → ít node → **tập trung hoá**     | node vẫn rẻ                                        |
| Giới hạn          | tuyến tính: block to gấp 10 thì 10 lần thông lượng  | gần như không giới hạn số giao dịch trong kênh     |
| Cái phải trả      | tính phi tập trung của chuỗi nền                    | vốn bị khoá, phải online, thanh khoản, độ phức tạp |
| Tương thích ngược | không — tách chuỗi                                  | có — soft fork                                     |

Lập luận thắng cuộc năm 2017 là hàng đầu tiên: **block to ra thì chi phí đổ lên đầu mọi người xác minh, chứ không phải người giao dịch.** Nếu chạy một node đầy đủ trở nên đắt, thì số người tự kiểm tra được luật giảm xuống, và blockchain mất đúng thứ khiến nó có nghĩa ([Bài 1](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md)).

Cùng một lập luận này xuất hiện lại ở Ethereum, chỉ khác từ ngữ:

```
   BITCOIN                              ETHEREUM
   block nhỏ + Lightning                chain nền không nhanh lên
                                        + rollup ở lớp 2
   -> chuỗi nền là lớp THANH TOÁN       -> chuỗi nền là lớp THANH TOÁN
      và lớp AN NINH                       và lớp SẴN SÀNG DỮ LIỆU
```

Hai hệ sinh thái ghét nhau ra mặt, đi tới **cùng một kết luận kiến trúc**: đừng làm chuỗi nền nhanh hơn, hãy làm nó thành nền móng cho tầng khác. Xem [Bài 10 §21](lesson_10_tai_chinh_phi_tap_trung.md#21-defi-chạy-trên-chain-nào-và-to-cỡ-nào).

---

## 13. Code minh hoạ

Bốn cơ chế: kênh thanh toán, gian lận bằng trạng thái cũ + trừng phạt, định tuyến HTLC, và thanh khoản một chiều.

> ⚙️ **Chạy:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không cần `tsc`, không cần `tsconfig.json`.

```typescript
/**
 * Bài 11 — Kênh thanh toán & Lightning: bốn thứ video không nói.
 * Chạy: node demo.ts   (Node 22.6+, không cần cài gì)
 */
import { strict as assert } from "node:assert";
import { createHash, randomBytes } from "node:crypto";

const sha256 = (s: string): string =>
  createHash("sha256").update(s).digest("hex");
/** Tien tinh bang SATOSHI (so nguyen). Khong bao gio dung so thuc cho tien:
 *  0.05 tru dan 0.001 chi ra 49 lan chu khong phai 50. */
const SAT = 100_000_000;
const btc = (sat: number): string => (sat / SAT).toFixed(5) + " BTC";

/* ===========================================================================
 * 1. Kênh thanh toán — 50 ly cà phê, 2 lần chạm chuỗi
 * ======================================================================== */
class PaymentChannel {
  balanceA: number;
  balanceB: number;
  stateNumber: number; // mỗi lần trả tiền là một bảng cân đối mới
  onChainTxCount: number; // đếm số giao dịch thật lên blockchain

  constructor(depositA: number, depositB: number) {
    this.balanceA = depositA;
    this.balanceB = depositB;
    this.stateNumber = 0;
    this.onChainTxCount = 1; // giao dịch MỞ kênh
  }

  get capacity(): number {
    return this.balanceA + this.balanceB;
  }

  /** Trả tiền = sửa bảng cân đối rồi cùng ký. Không lên chuỗi. */
  pay(amount: number): void {
    assert(this.balanceA >= amount, "khong du so du trong kenh");
    this.balanceA -= amount;
    this.balanceB += amount;
    this.stateNumber++;
  }

  close(): void {
    this.onChainTxCount++; // giao dịch ĐÓNG kênh
  }
}

console.log("=== 1. Kenh thanh toan: 50 ly ca phe ===");
{
  const channel = new PaymentChannel(0.05 * SAT, 0);
  const coffeePrice = 0.001 * SAT;
  while (channel.balanceA >= coffeePrice) channel.pay(coffeePrice);
  channel.close();

  console.log(`  Nap vao      : Bob ${btc(0.05 * SAT)}, quan ${btc(0)}`);
  console.log(`  So ly ca phe : ${channel.stateNumber}`);
  console.log(`  Ket thuc     : Bob ${btc(channel.balanceA)}, quan ${btc(channel.balanceB)}`);
  console.log(`  Cham blockchain: ${channel.onChainTxCount} giao dich (mo + dong)\n`);

  const feePerTx = 0.00002 * SAT; // ~2000 sat mỗi giao dịch
  console.log(`  Neu lam thang tren chuoi: ${channel.stateNumber} gd x ${btc(feePerTx)} = ${btc(channel.stateNumber * feePerTx)}`);
  console.log(`  Qua kenh                : ${channel.onChainTxCount} gd x ${btc(feePerTx)} = ${btc(channel.onChainTxCount * feePerTx)}`);
  console.log(`  -> Tiet kiem ${((1 - channel.onChainTxCount / channel.stateNumber) * 100).toFixed(1)}% phi`);
  assert(channel.onChainTxCount === 2 && channel.stateNumber === 50);
}

/* ===========================================================================
 * 2. Vì sao kênh ngây thơ BỊ ĂN CẮP — và cách Lightning vá
 *    Video nói "hệ thống bảo đảm chỉ bảng cân đối MỚI NHẤT dùng được"
 *    nhưng không nói bằng cách nào. Đây là cách.
 * ======================================================================== */
console.log("\n=== 2. Gian lan bang trang thai cu ===");
{
  // Mỗi trạng thái là một bảng cân đối ĐÃ KÝ. Cả hai bên giữ bản sao.
  type BalanceSheet = { version: number; bob: number; shop: number };
  const history: BalanceSheet[] = [];
  let bob = 0.05 * SAT, shop = 0;
  history.push({ version: 0, bob, shop });
  for (let i = 1; i <= 30; i++) {
    bob -= 0.001 * SAT; shop += 0.001 * SAT;
    history.push({ version: i, bob, shop });
  }

  const latest = history[history.length - 1];
  const oldest = history[0];
  console.log(`  Sau 30 ly: Bob ${btc(latest.bob)}, quan ${btc(latest.shop)}`);
  console.log(`  Bang so 0 : Bob ${btc(oldest.bob)}, quan ${btc(oldest.shop)}  <- van CO CHU KY hop le!\n`);

  console.log("  [Kenh NGAY THO] Bob phat bang so 0 len chuoi:");
  console.log(`    Chuoi thay 2 chu ky dung -> chap nhan. Bob lay lai ${btc(oldest.bob)}.`);
  console.log(`    Quan mat ${btc(latest.shop)}. GIAN LAN THANH CONG.\n`);

  // Bản vá thật của Lightning: mỗi lần sang trạng thái mới, bạn TRAO cho đối
  // phương bí mật thu hồi của trạng thái cũ. Ai phát trạng thái đã thu hồi thì
  // đối phương dùng bí mật đó lấy SẠCH tiền trong kênh.
  const revocationSecrets = new Map<number, string>();
  for (let i = 0; i < history.length - 1; i++) {
    revocationSecrets.set(i, randomBytes(32).toString("hex")); // đã trao cho quán
  }

  function shopResponse(publishedState: number): string {
    if (revocationSecrets.has(publishedState)) {
      return `PHAT: quan trinh bi mat thu hoi #${publishedState} -> cuop SACH ${btc(0.05 * SAT)}`;
    }
    return "hop le, chia theo bang";
  }

  console.log("  [Kenh LIGHTNING] Bob phat bang so 0 len chuoi:");
  console.log(`    ${shopResponse(0)}`);
  console.log(`    Bob dinh an cap ${btc(0.03 * SAT)}, ket cuc mat ca ${btc(0.05 * SAT)}.\n`);
  console.log("  -> An ninh cua Lightning KHONG phai 'khong the gian lan',");
  console.log("     ma la 'gian lan thi lo nhieu hon duoc'. Kinh te, khong phai mat ma.");
  console.log("  -> He qua: ban PHAI online de bat gian lan. Neu khong -> thue WATCHTOWER.");
  assert(shopResponse(0).startsWith("PHAT"));
  assert(shopResponse(30) === "hop le, chia theo bang");
}

/* ===========================================================================
 * 3. Định tuyến qua trung gian bằng HTLC — vì sao trung gian không ăn chặn được
 * ======================================================================== */
console.log("\n=== 3. Dinh tuyen: Alice -> Bob -> Quan ===");
{
  // Quán tạo bí mật preimage, công bố hash = sha256(preimage) cho Alice qua hoá đơn.
  // Preimage lay tu mot chuoi co dinh de ket qua chay lai luc nao cung giong nhau.
  const preimage = sha256("bi mat cua quan ca phe");
  const paymentHash = sha256(preimage);
  const amount = 0.001 * SAT;
  const routingFee = 0.00001 * SAT;

  console.log(`  Quan tao bi mat R, gui hoa don chua H = ${paymentHash.slice(0, 16)}...`);
  console.log(`  Alice muon tra ${btc(amount)} nhung KHONG co kenh voi quan.\n`);

  // Khoá tiền theo điều kiện, đi xuôi.
  const hops = [
    { from: "Alice", to: "Bob", locked: amount + routingFee },
    { from: "Bob", to: "Quan", locked: amount },
  ];
  for (const hop of hops) {
    console.log(`  [khoa] ${hop.from} -> ${hop.to}: ${btc(hop.locked)} khoa boi H`);
    console.log(`         dieu kien: ai trinh duoc R sao cho sha256(R)=H thi lay duoc`);
  }

  console.log(`\n  [mo] Quan trinh R -> lay ${btc(amount)} tu Bob`);
  assert(sha256(preimage) === paymentHash);
  console.log(`  [mo] Bob GIO DA BIET R -> lay ${btc(amount + routingFee)} tu Alice`);
  console.log(`       Bob lai ${btc(routingFee)} tien cong chuyen tiep\n`);

  console.log("  Vi sao Bob khong an chan duoc:");
  console.log("    · Bob giu tien lai -> khong co R -> khong lay duoc tien cua Alice");
  console.log("    · Bob doi tien -> R chi mo dung so tien da khoa");
  console.log("    · Quan im lang  -> het han, MOI khoa tu hoan tien nguoc lai");
  console.log("  -> Toan bo duong di la NGUYEN TU: hoac ca chuoi thanh cong, hoac khong ai mat.");

  // Nhưng: thời hạn phải GIẢM dần khi đi xuôi, nếu không Bob kẹt.
  console.log("\n  Chi tiet video bo qua: han cua chang TRUOC phai DAI hon chang SAU.");
  const timeouts = [{ hop: "Alice->Bob", blocks: 144 }, { hop: "Bob->Quan", blocks: 72 }];
  for (const t of timeouts) console.log(`    ${t.hop.padEnd(12)} het han sau ${t.blocks} khoi (~${(t.blocks / 6).toFixed(0)} gio)`);
  console.log("    Nguoc lai thi Bob tra cho quan xong moi phat hien khong doi duoc tu Alice.");
}

/* ===========================================================================
 * 4. Thanh khoản một chiều — giới hạn mà video hoàn toàn không nhắc
 * ======================================================================== */
console.log("\n=== 4. Thanh khoan mot chieu ===");
{
  const channel = new PaymentChannel(0.05 * SAT, 0);
  console.log(`  Mo kenh: Bob ${btc(channel.balanceA)} | quan ${btc(channel.balanceB)}   (suc chua ${btc(channel.capacity)})\n`);
  console.log("  Bob GUI duoc toi da    : " + btc(channel.balanceA));
  console.log("  Bob NHAN duoc toi da   : " + btc(channel.balanceB) + "   <- BANG KHONG");
  console.log("  Quan GUI duoc toi da   : " + btc(channel.balanceB) + "   <- BANG KHONG\n");

  for (let i = 0; i < 50; i++) channel.pay(0.001 * SAT);
  console.log(`  Sau 50 ly: Bob ${btc(channel.balanceA)} | quan ${btc(channel.balanceB)}`);
  console.log("  -> Kenh CAN mot chieu. Bob khong tra them duoc ly nao nua.");
  console.log("     Phai dong kenh va mo lai = 2 giao dich on-chain nua.\n");

  // Định tuyến chỉ đi qua được nếu MỌI chặng đủ thanh khoản ĐÚNG CHIỀU.
  const route = [
    { hop: "Alice->Bob", outboundLiquidity: 0.002 * SAT },
    { hop: "Bob->Carol", outboundLiquidity: 0.0005 * SAT },
    { hop: "Carol->Quan", outboundLiquidity: 0.010 * SAT },
  ];
  const amountToSend = 0.001 * SAT;
  console.log(`  Dinh tuyen ${btc(amountToSend)} qua 3 chang:`);
  let routeWorks = true;
  for (const hop of route) {
    const ok = hop.outboundLiquidity >= amountToSend;
    if (!ok) routeWorks = false;
    console.log(`    ${hop.hop.padEnd(12)} thanh khoan ra ngoai ${btc(hop.outboundLiquidity)}  ${ok ? "ok" : "<-- NGHEN"}`);
  }
  console.log(`  Ket qua: ${routeWorks ? "di duoc" : "THAT BAI — phai tim duong khac"}`);
  console.log("\n  -> Day la ly do thanh toan Lightning thinh thoang bao loi khong ro nguyen nhan:");
  console.log("     thanh khoan la RIENG TU, nguoi gui khong nhin thay truoc chang nao se nghen.");
  assert(!routeWorks);
}

console.log("\nXong. Bon co che: kenh, thu hoi/phat, HTLC dinh tuyen, thanh khoan.");
```

Kết quả chạy thật:

```
=== 1. Kenh thanh toan: 50 ly ca phe ===
  Nap vao      : Bob 0.05000 BTC, quan 0.00000 BTC
  So ly ca phe : 50
  Ket thuc     : Bob 0.00000 BTC, quan 0.05000 BTC
  Cham blockchain: 2 giao dich (mo + dong)

  Neu lam thang tren chuoi: 50 gd x 0.00002 BTC = 0.00100 BTC
  Qua kenh                : 2 gd x 0.00002 BTC = 0.00004 BTC
  -> Tiet kiem 96.0% phi

=== 2. Gian lan bang trang thai cu ===
  Sau 30 ly: Bob 0.02000 BTC, quan 0.03000 BTC
  Bang so 0 : Bob 0.05000 BTC, quan 0.00000 BTC  <- van CO CHU KY hop le!

  [Kenh NGAY THO] Bob phat bang so 0 len chuoi:
    Chuoi thay 2 chu ky dung -> chap nhan. Bob lay lai 0.05000 BTC.
    Quan mat 0.03000 BTC. GIAN LAN THANH CONG.

  [Kenh LIGHTNING] Bob phat bang so 0 len chuoi:
    PHAT: quan trinh bi mat thu hoi #0 -> cuop SACH 0.05000 BTC
    Bob dinh an cap 0.03000 BTC, ket cuc mat ca 0.05000 BTC.

  -> An ninh cua Lightning KHONG phai 'khong the gian lan',
     ma la 'gian lan thi lo nhieu hon duoc'. Kinh te, khong phai mat ma.
  -> He qua: ban PHAI online de bat gian lan. Neu khong -> thue WATCHTOWER.

=== 3. Dinh tuyen: Alice -> Bob -> Quan ===
  Quan tao bi mat R, gui hoa don chua H = 4029205b8df2be8b...
  Alice muon tra 0.00100 BTC nhung KHONG co kenh voi quan.

  [khoa] Alice -> Bob: 0.00101 BTC khoa boi H
         dieu kien: ai trinh duoc R sao cho sha256(R)=H thi lay duoc
  [khoa] Bob -> Quan: 0.00100 BTC khoa boi H
         dieu kien: ai trinh duoc R sao cho sha256(R)=H thi lay duoc

  [mo] Quan trinh R -> lay 0.00100 BTC tu Bob
  [mo] Bob GIO DA BIET R -> lay 0.00101 BTC tu Alice
       Bob lai 0.00001 BTC tien cong chuyen tiep

  Vi sao Bob khong an chan duoc:
    · Bob giu tien lai -> khong co R -> khong lay duoc tien cua Alice
    · Bob doi tien -> R chi mo dung so tien da khoa
    · Quan im lang  -> het han, MOI khoa tu hoan tien nguoc lai
  -> Toan bo duong di la NGUYEN TU: hoac ca chuoi thanh cong, hoac khong ai mat.

  Chi tiet video bo qua: han cua chang TRUOC phai DAI hon chang SAU.
    Alice->Bob   het han sau 144 khoi (~24 gio)
    Bob->Quan    het han sau 72 khoi (~12 gio)
    Nguoc lai thi Bob tra cho quan xong moi phat hien khong doi duoc tu Alice.

=== 4. Thanh khoan mot chieu ===
  Mo kenh: Bob 0.05000 BTC | quan 0.00000 BTC   (suc chua 0.05000 BTC)

  Bob GUI duoc toi da    : 0.05000 BTC
  Bob NHAN duoc toi da   : 0.00000 BTC   <- BANG KHONG
  Quan GUI duoc toi da   : 0.00000 BTC   <- BANG KHONG

  Sau 50 ly: Bob 0.00000 BTC | quan 0.05000 BTC
  -> Kenh CAN mot chieu. Bob khong tra them duoc ly nao nua.
     Phai dong kenh va mo lai = 2 giao dich on-chain nua.

  Dinh tuyen 0.00100 BTC qua 3 chang:
    Alice->Bob   thanh khoan ra ngoai 0.00200 BTC  ok
    Bob->Carol   thanh khoan ra ngoai 0.00050 BTC  <-- NGHEN
    Carol->Quan  thanh khoan ra ngoai 0.01000 BTC  ok
  Ket qua: THAT BAI — phai tim duong khac

  -> Day la ly do thanh toan Lightning thinh thoang bao loi khong ro nguyen nhan:
     thanh khoan la RIENG TU, nguoi gui khong nhin thay truoc chang nao se nghen.

Xong. Bon co che: kenh, thu hoi/phat, HTLC dinh tuyen, thanh khoan.
```

**Tự thử:**

1. Trong demo 2, thêm điều kiện *"quán chỉ trừng phạt được nếu online trong 144 khối"*. Cho quán offline rồi chạy lại — gian lận thành công. Đó chính là lý do watchtower tồn tại.
2. Demo 3: thêm một chặng nữa (Alice → Bob → Carol → Quán) và tính hạn cho từng chặng sao cho vẫn an toàn. Đường càng dài thì tiền của Alice bị treo tối đa bao lâu?
3. Demo 4: viết hàm tìm đường qua một mạng 6 nút, chỉ đi qua chặng đủ thanh khoản. Rồi thử giấu số dư đi (chỉ cho biết sức chứa) và xem tỉ lệ thất bại tăng thế nào.

---

## 14. Từ điển thuật ngữ

| Tiếng Anh                  | Tiếng Việt                     | Nghĩa gọn                                               |
| -------------------------- | ------------------------------ | ------------------------------------------------------- |
| Hard fork                  | fork cứng                      | luật mới không tương thích ngược → tách chuỗi vĩnh viễn |
| Soft fork                  | fork mềm                       | luật mới chặt hơn → node cũ vẫn chạy được               |
| Replay attack              | tấn công phát lại              | phát lại giao dịch của chuỗi này lên chuỗi kia          |
| Replay protection          | phòng vệ phát lại              | làm chữ ký chỉ hợp lệ trên đúng một chuỗi               |
| Off-chain                  | ngoài chuỗi                    | giao dịch không ghi lên blockchain                      |
| Layer 2                    | lớp 2                          | tầng xây trên chuỗi nền, thừa hưởng an ninh của nó      |
| Payment channel            | kênh thanh toán                | hai bên khoá tiền chung, trao đổi bảng cân đối đã ký    |
| Multi-signature            | đa chữ ký                      | địa chỉ cần nhiều chữ ký mới chi được                   |
| Commitment / balance sheet | bảng cân đối                   | trạng thái chia tiền hiện tại của kênh, cả hai cùng ký  |
| Revocation secret          | bí mật thu hồi                 | thứ cho phép trừng phạt kẻ phát bảng cũ                 |
| Penalty transaction        | giao dịch trừng phạt           | cướp sạch tiền kênh của kẻ gian lận                     |
| Watchtower                 | trạm canh                      | dịch vụ canh chuỗi hộ khi bạn offline                   |
| HTLC                       | hợp đồng khoá hash + thời gian | khoá tiền theo điều kiện "trình được R" và có hạn       |
| Preimage                   | tiền ảnh                       | chính là R, thứ băm ra H                                |
| Routing                    | định tuyến                     | tìm đường chuyền tiền qua nhiều kênh                    |
| Inbound liquidity          | thanh khoản vào                | số tiền bạn có thể NHẬN qua kênh                        |
| Custodial wallet           | ví lưu ký                      | ứng dụng giữ khoá hộ bạn                                |

---

## 15. Câu hỏi tự kiểm tra

1. Fork tách chuỗi tại đâu, và điều đó được quy định bằng cách nào?
2. Vì sao thợ đào có thể phản đối một bản nâng cấp dù nó tốt về kỹ thuật?
3. Giảm giới hạn block từ 1MB xuống 0,5MB là hard fork hay soft fork? Còn tăng lên 2MB? Giải thích theo hướng "node cũ nghĩ gì".
4. Sau fork bạn có coin trên cả hai chuỗi. Video gọi là "tiền chùa". Nêu hai lý do nó không thật sự miễn phí.
5. Tấn công phát lại là gì, và vì sao nó chỉ xảy ra ngay sau fork?
6. Bitcoin Gold bị tấn công 51% hai lần. Fork đã làm gì khiến chuyện đó dễ hơn?
7. Mở và đóng một kênh thanh toán tốn mấy giao dịch on-chain? Vì sao phải là địa chỉ đa chữ ký?
8. Bob nạp 0,05 BTC, quán nạp 0. Ngay sau khi mở kênh, quán gửi tiền cho Bob được không? Vì sao?
9. Bảng cân đối số 0 vẫn có đủ chữ ký hợp lệ. Vì sao blockchain không tự biết bảng nào mới hơn?
10. Mô tả cơ chế bí mật thu hồi. Nếu Bob phát bảng cũ thì Bob mất bao nhiêu?
11. Câu "an ninh của Lightning là an ninh kinh tế, không phải an ninh mật mã" nghĩa là gì? Kể hai chỗ khác trong khoá học dùng cùng lập luận.
12. Vì sao dùng Lightning thì bạn phải online, còn giữ Bitcoin trên chuỗi nền thì không?
13. Watchtower giải quyết vấn đề gì, và nó thêm giả định tin cậy nào?
14. Trong đường đi Alice → Bob → Quán, ai tạo ra bí mật R? Vì sao phải là người đó?
15. Bob đã cầm tiền Alice khoá. Nêu ba cách Bob thử ăn chặn và vì sao cả ba đều hỏng.
16. Thời hạn của chặng Alice→Bob phải dài hơn hay ngắn hơn chặng Bob→Quán? Chuyện gì xảy ra nếu làm ngược?
17. Kênh của Bob cạn sau 50 ly cà phê. Bob phải làm gì, và tốn thêm bao nhiêu giao dịch on-chain?
18. Vì sao người gửi không biết trước đường nào sẽ nghẽn?
19. Thanh khoản riêng tư tạo ra áp lực tập trung hoá như thế nào?
20. Video đoán Lightning lên sóng năm 2018. Dự đoán đó đúng hay sai? Còn dự đoán ngầm rằng ai cũng tự chạy kênh?
21. Ví Lightning lưu ký tiện hơn nhiều. Nó vứt bỏ mất cái gì?
22. So sánh "làm block to ra" với "đẩy ra lớp 2" theo tiêu chí: ai chịu chi phí, và hệ quả lâu dài lên tính phi tập trung.
23. Bitcoin và Ethereum thù địch nhau nhưng đi tới cùng một kết luận kiến trúc. Kết luận đó là gì?

---

## Tóm tắt một trang

```
 ┌──────────────────────────────────────────────────────────────────────┐
 │  Một câu hỏi: "7 giao dịch/giây là quá ít"                            │
 │  Hai câu trả lời: TÁCH CHUỖI  vs  XÂY THÊM TẦNG                      │
 └──────────────────────────────────────────────────────────────────────┘

  FORK
    cơ chế   sao chép mã nguồn -> sửa -> chọn số hiệu khối kích hoạt
    hard     luật NỚI ra  -> node cũ từ chối -> tách vĩnh viễn
    soft     luật CHẶT hơn -> node cũ vẫn chạy -> không tách
    "tiền chùa"  có coin trên cả hai chuỗi, NHƯNG:
                 · hashrate cũng bị chia đôi -> chuỗi nhỏ dễ bị 51%
                 · thiếu phòng vệ phát lại -> mất tiền ngoài ý muốn
    2026     BCH còn sống nhỏ, BTG bị 51% hai lần, phần lớn fork đã chết

  KÊNH THANH TOÁN
    mở    hai bên nạp vào địa chỉ ĐA CHỮ KÝ         [on-chain]
    tiêu  sửa bảng cân đối, cả hai cùng ký          [off-chain, không giới hạn]
    đóng  phát bảng mới nhất lên chuỗi              [on-chain]
    -> 50 ly cà phê = 2 giao dịch on-chain, tiết kiệm 96% phí

  BA THỨ VIDEO KHÔNG NÓI
    1  Bảng CŨ vẫn có chữ ký hợp lệ -> phát lên là ăn cắp được.
       Vá: bí mật thu hồi + giao dịch trừng phạt (cướp SẠCH kênh).
       -> an ninh KINH TẾ, không phải mật mã
    2  Muốn trừng phạt thì phải ONLINE -> watchtower -> lại một bên thứ ba
    3  Kênh CÓ CHIỀU. Nhận được tối đa = tiền đang ở đầu bên kia.
       Định tuyến hỏng nếu MỘT chặng thiếu thanh khoản đúng chiều,
       và số dư từng chiều là RIÊNG TƯ -> phải đoán rồi thử

  HTLC — vì sao trung gian không ăn chặn
    quán tạo R, công bố H=sha256(R)
    mỗi chặng khoá tiền bằng H, hạn GIẢM dần khi đi xuôi
    quán trình R -> lộ R ngược lên -> từng chặng lấy tiền
    im lặng -> hết hạn -> mọi khoá tự hoàn -> NGUYÊN TỬ

  KẾT
    Bitcoin: chuỗi nền nhỏ + Lightning
    Ethereum: chuỗi nền không nhanh lên + rollup
    -> hai bên ghét nhau, cùng một kết luận kiến trúc
```

---

## Nguồn

- Video 1: [What is a Bitcoin hard fork? — Simply Explained](https://www.youtube.com/watch?v=XCo6yyutYAM) (4:30)
- Video 2: [Bitcoin's Lightning Network — Simply Explained](https://www.youtube.com/watch?v=rrr_zPmEiME) (5:19)
- [Lightning Network whitepaper](https://lightning.network/lightning-network-paper.pdf) — Poon & Dryja, 2016
- [Đặc tả BOLT](https://github.com/lightning/bolts) — chuẩn giao thức Lightning, gồm cơ chế thu hồi và định tuyến
- [Mastering the Lightning Network](https://github.com/lnbook/lnbook) — Antonopoulos, Osuntokun, Pickhardt (miễn phí)
- [BIP141 — SegWit](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)

---

**Bản đồ khoá học** — 8 bài lý thuyết + 5 bài mở rộng + phần thực hành. Đọc theo thứ tự là mạch liền; nhảy cóc cũng được.

1. [Bài 1 – Blockchain hoạt động như thế nào](../ly_thuyet/lesson_1_blockchain_hoat_dong_ntn.md) — hash chain, Proof of Work, P2P, đồng thuận
2. [Bài 2 – Mã hoá bất đối xứng](../ly_thuyet/lesson_2_ma_hoa_bat_doi_xung.md) — cặp khoá, Diffie–Hellman, RSA, chữ ký số, PKI
3. [Bài 3 – Smart contract](../ly_thuyet/lesson_3_smart_contract.md) — EVM, gas, oracle, reentrancy
4. [Bài 4 – Ứng dụng blockchain](../ly_thuyet/lesson_4_ung_dung_blockchain.md) — use case + khung quyết định *có cần blockchain không*
5. [Bài 5 – Proof of Stake](../ly_thuyet/lesson_5_proof_of_stake.md) — staking, slashing, The Merge, Ouroboros, kho bạc on-chain
6. [Bài 6 – Ví Bitcoin](../ly_thuyet/lesson_6_vi_bitcoin.md) — private key → địa chỉ, UTXO, seed phrase
7. [Bài 7 – Độ khó đào](../ly_thuyet/lesson_7_do_kho_dao.md) — target, nBits, retarget, phân bố Poisson
8. [Bài 8 – Zero-Knowledge Proof](../ly_thuyet/lesson_8_zero_knowledge_proof.md) — sigma protocol, Fiat-Shamir, SNARK/STARK

*Phần mở rộng — nhìn từ trên xuống:*

9. [Bài 9 – Tiền mã hoá: toàn cảnh (và mặt tối)](lesson_9_tien_ma_hoa_toan_canh.md) — tiền, lưu ký, stablecoin, lừa đảo, pháp lý
10. [Bài 10 – DeFi: tài chính phi tập trung](lesson_10_tai_chinh_phi_tap_trung.md) — AMM, cho vay, flash loan, NFT, DAO
11. **Bài 11 – Mở rộng Bitcoin: từ bất đồng tới Lightning** ← *bạn đang ở đây* — fork, kênh thanh toán, HTLC, thanh khoản
12. [Bài 12 – ERC-20: chuẩn token](lesson_12_erc20_va_token.md) — 6 hàm, approve, ICO, ERC-223/777
13. [Bài 13 – GDPR có giết blockchain không](lesson_13_gdpr_va_blockchain.md) — dữ liệu cá nhân, quyền được quên, gộp cụm ví

*Phần thực hành:* [thuc_hanh/](../thuc_hanh/README.md) — tự tay dựng một blockchain bằng TypeScript, 6 bước.
