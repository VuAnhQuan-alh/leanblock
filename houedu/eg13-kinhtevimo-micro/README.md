# Kinh tế học vi mô — cho ngành Quản trị Kinh doanh

Bộ bài học dựng **từ chính giáo trình**, không viết theo trí nhớ.

**Giáo trình gốc:** N. Gregory Mankiw, ***Kinh tế học vi mô*** — bản dịch của Khoa Kinh tế,
Trường ĐH Kinh tế TP.HCM (Cengage Learning Asia). 22 chương / 7 phần.
Tệp: `tai_lieu/Kinh te hoc vi mo (MicroEconomics)_Mankiw.pdf`.

> ⚠️ **Lệch trang:** *trang sách N = trang PDF N + 33*. Mọi trích dẫn trong bài dùng **số trang in
> trên giấy**, không phải số trang PDF. (Đã kiểm: PDF 132 = tr. 99.)

---

## Cách đọc

| Ký hiệu                | Nghĩa                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| `tr. 12`               | trích trang 12 của giáo trình (số in trên giấy)                    |
| **Hình 2**, **Bảng 1** | hình/bảng nguyên bản của sách, giữ nguyên số hiệu để tra ngược     |
| 💼 **Góc QTKD**         | ví dụ thêm cho ngành quản trị kinh doanh — **không có trong sách** |
| 📚 **Mở rộng**          | kiến thức sách nói lướt, để trong bài tập, hoặc bỏ qua             |
| ⚠️                      | chỗ dễ hiểu sai, hoặc chỗ sách in sai (kèm đối chiếu bản quét)     |
| 🎯 🔸 ⚪                  | vòng ưu tiên cho QTKD — xem bảng bên dưới                          |

Công thức viết bằng LaTeX. Mở bằng **Obsidian** (hoặc VS Code + Markdown Preview Enhanced) để hiển thị đúng.

---

## Nên học môn này thế nào trong ngành QTKD

Sách Mankiw viết cho **cử nhân kinh tế nói chung**, không riêng cho quản trị kinh doanh. Thứ tự
chương của sách **không phải** thứ tự ưu tiên của bạn: Phần III, IV và VI (chương 8, 9, 11, 12, 19, 20)
là **kinh tế học khu vực công** — thuế, thương mại quốc tế, hàng hoá công, bất bình đẳng. Hay, nhưng
người làm quản trị dùng đến rất ít.

Ba vòng ưu tiên:

- 🎯 **Vòng 1 — xương sống nghề.** Học kỹ, làm hết bài tập. Đây là phần trả lời những câu hỏi bạn sẽ
  thật sự gặp: định giá bao nhiêu, sản xuất bao nhiêu, khi nào nên dừng, đối thủ sẽ làm gì.
- 🔸 **Vòng 2 — cần để hiểu bối cảnh và để thi.** Đọc hiểu, nắm khái niệm.
- ⚪ **Vòng 3 — đọc lướt.** Biết khái niệm là đủ.

Và ba điều về **cách** học, quan trọng hơn thứ tự:

**1. Vi mô không phải môn thuộc lòng — nó là khoảng mười mô hình.** Mỗi chương = một đồ thị + một quy
tắc quyết định. Thuộc định nghĩa mà không vẽ được đồ thị thì thi xong là quên. Tự kiểm tra bằng cách
che sách, vẽ lại đồ thị, rồi hỏi *"đường nào dịch chuyển, theo hướng nào, vì sao"*.

**2. Mỗi khái niệm phải gắn với một quyết định kinh doanh cụ thể**, nếu không nó chỉ là toán suông:

| Khái niệm                | Quyết định                                                       |
| ------------------------ | ---------------------------------------------------------------- |
| co giãn cầu theo giá > 1 | giảm giá thì **tổng doanh thu tăng**; < 1 thì giảm giá là tự sát |
| chi phí chìm             | đừng đưa vào quyết định, dù đã đổ bao nhiêu tiền                 |
| MR = MC                  | sản lượng tối ưu — không phải "bán càng nhiều càng tốt"          |
| P > AVC                  | vẫn nên tiếp tục chạy dù đang lỗ                                 |
| phân biệt giá            | vì sao vé máy bay cùng chuyến có mười mức giá                    |

**3. Nối với môn Xác suất Thống kê đã học.** Đây là chỗ hai môn gặp nhau, và cũng là chỗ hầu hết sinh
viên bỏ lỡ: **độ co giãn của cầu chính là hệ số hồi quy**.
Hồi quy $\ln Q$ theo $\ln P$ thì hệ số góc **là** độ co giãn — đúng công cụ ở [bài 14 môn Xác suất Thống kê](../eg11-xacxuatthongke/ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md).
Còn A/B test giá thì là [bài 12–13](../eg11-xacxuatthongke/ly_thuyet/bai_12_kiem_dinh_gia_thuyet_mot_mau.md).
Sách Mankiw dừng ở *"độ co giãn là gì"*; các bài ở đây đi tiếp tới *"ước lượng nó từ dữ liệu thật"*.

---

## Lộ trình 14 bài

Xếp theo **thứ tự ưu tiên QTKD**, không theo thứ tự chương của sách.

|    # | Bài                                                                                              | Chương sách     | tr.              | Ưu tiên |
| ---: | ------------------------------------------------------------------------------------------------ | --------------- | ---------------- | :-----: |
|    1 | [Mười nguyên lý và tư duy kinh tế](ly_thuyet/bai_01_muoi_nguyen_ly_va_tu_duy_kinh_te.md)         | 1 + 2           | 3–56             |    🎯    |
|    2 | [Cung và cầu](ly_thuyet/bai_02_cung_va_cau.md)                                                   | 4               | 77–102           |    🎯    |
|    3 | [**Độ co giãn và định giá**](ly_thuyet/bai_03_do_co_gian_va_dinh_gia.md)                         | 5               | 103–126          |   🎯⭐    |
|    4 | [Thặng dư, giá sẵn lòng trả, chi phí của thuế](ly_thuyet/bai_04_thang_du_va_chi_phi_cua_thue.md) | 7 + 8           | 153–189          |    🔸    |
|    5 | [Chi phí sản xuất](ly_thuyet/bai_05_chi_phi_san_xuat.md)                                         | 13              | 283–307          |    🎯    |
|    6 | [Doanh nghiệp trên thị trường cạnh tranh](ly_thuyet/bai_06_thi_truong_canh_tranh.md)             | 14              | 308–333          |    🎯    |
|    7 | [Độc quyền và phân biệt giá](ly_thuyet/bai_07_doc_quyen_va_phan_biet_gia.md)                     | 15              | 334–369          |    🎯    |
|    8 | [Cạnh tranh độc quyền, quảng cáo, thương hiệu](ly_thuyet/bai_08_canh_tranh_doc_quyen.md)         | 16              | 370–390          |    🎯    |
|    9 | [Độc quyền nhóm và lý thuyết trò chơi](ly_thuyet/bai_09_doc_quyen_nhom_va_ly_thuyet_tro_choi.md) | 17              | 391–420          |    🎯    |
|   10 | [Lý thuyết lựa chọn của người tiêu dùng](ly_thuyet/bai_10_lua_chon_cua_nguoi_tieu_dung.md)       | 21              | 495–524          |    🎯    |
|   11 | [Thông tin bất cân xứng, kinh tế học hành vi](ly_thuyet/bai_11_thong_tin_bat_can_xung.md)        | 22              | 525+             |    🎯    |
|   12 | [Lao động, tiền lương, bất bình đẳng](ly_thuyet/bai_12_thi_truong_lao_dong.md)                   | 18 + 19 + 20    | 421–494          |   🔸⚪    |
|   13 | [Chính phủ can thiệp thị trường](ly_thuyet/bai_13_chinh_phu_can_thiep_thi_truong.md)             | 6 + 12          | 127–152, 255–282 |   🔸⚪    |
|   14 | [Thương mại, ngoại tác, hàng hoá công](ly_thuyet/bai_14_thuong_mai_ngoai_tac_hang_hoa_cong.md)   | 3 + 9 + 10 + 11 | 57–76, 190–254   |   🔸⚪    |

⭐ **Chương 5 (Độ co giãn)** là chương sinh lời nhất cả cuốn với người làm quản trị.

---

## Bố cục kho

```
eg13-kinhtevimo-micro/
  ly_thuyet/         14 bài, mỗi bài bám sát chương sách
  mo_rong/           chủ đề sách 2008 không có mà QTKD hôm nay cần
  thuc_hanh/         code Python chạy được của từng bài + dữ liệu CSV
  case_study/        tình huống doanh nghiệp
  tai_lieu/          PDF giáo trình gốc
  tai_lieu/hinh/     135 hình·bảng gốc cắt từ PDF, nhúng thẳng vào bài (~26 MB)
  cap-nhat-ban-do.py sinh lại mục lục + bản đồ khoá học trong mọi bài
  cat-hinh.py        cắt hình·bảng từ PDF quét ra tai_lieu/hinh/
  chen-hinh.py       chèn ảnh vào đúng chỗ trong ly_thuyet/
```

---

## Hình và bảng gốc của sách

Mỗi chỗ bài học nhắc **Hình N** hay **Bảng N** đều có **ảnh gốc chụp từ giáo trình** ngay bên dưới
đoạn văn ấy — **135 ảnh**, phủ hết mọi hình·bảng mà 14 bài có nhắc tên. Chú thích của sách nằm sẵn
trong ảnh nên bài không lặp lại nó.

PDF là **bản quét**, không có lớp chữ. Hầu hết hình của Mankiw nằm trong một **khung nền xám** rộng
gần hết bề ngang trang, nên `cat-hinh.py` dò khung bằng quy tắc: *hàng nào có pixel không-trắng đầu
tiên từ trái và từ phải đều xám, và xám liên tục ít nhất 6 pixel*. Điều kiện "liên tục 6 pixel" loại
được dòng chữ — cạnh chữ bị làm mịn cũng ra xám nhưng chỉ đúng một pixel.

```bash
python3 cat-hinh.py --liet-ke   # xem danh mục hình → trang
python3 cat-hinh.py             # cắt ra tai_lieu/hinh/ (cần pdftoppm của Poppler)
python3 chen-hinh.py            # chèn vào ly_thuyet/ — chạy lại bao nhiêu lần cũng được
```

Chỉ cần `pdftoppm`; không dùng thư viện Python ngoài. Ảnh là **PNG 200 DPI** — với nét mảnh của bản
quét, PNG *nhỏ hơn* JPEG cùng độ phân giải.

> ⚠️ **Bộ dò khung sai khá nhiều ở môn này** — nhiều hơn hẳn EG14. Năm kiểu hỏng đã gặp:
> trang có **hai** khung xám xếp chồng (bộ dò gộp làm một hoặc lấy nhầm khung), hình nằm ở **trang
> kế bên** chỗ được nhắc, hình in trên **nền trắng** không có khung nào để dò, khung bị **cắt cụt**
> đầu hoặc đuôi, và một mục mà sách **không hề có**.
> Vì thế **cả 135 ảnh đã được duyệt bằng mắt** — nhãn *"Hình N"* nằm ngay trong ảnh nên đối chiếu
> được với tên tệp; thêm một phép **băm MD5** để bắt các ảnh trùng nhau (dấu hiệu chắc chắn của gán
> nhầm): ban đầu có **18** ảnh trùng, nay **0**. Mọi chỗ sửa tay đều nằm trong các bảng `TRANG_TAY`,
> `KHOI_TAY`, `KHE_TAY`, `VUNG_TAY` và `BO_HAN` của `cat-hinh.py`, kèm ghi chú lý do.

---

## Chạy code

Mọi đoạn code trong bài đều **chạy được ngay**, chỉ dùng **thư viện chuẩn của Python** — không cần
`pip install` gì cả, không cần `numpy`, không cần `matplotlib` (đồ thị vẽ bằng ký tự).

```bash
cd thuc_hanh
python3 bai-01-nguyen-ly-va-tu-duy.py
```

Cần **Python 3.10 trở lên**. Kết quả **tất định** — chạy hai lần ra giống hệt nhau (mọi mô phỏng đều
dùng hạt giống cố định), nên bạn đối chiếu được từng chữ số với khối *"Kết quả chạy thật"* in trong bài.

---

## Đính chính giáo trình

Chỗ nào sách in sai, bài học ghi rõ **sách viết X, đúng phải là Y**, kèm đối chiếu bản quét gốc.

|  Bài |  tr. | Sách in                                                                                 | Đúng                                                                       |
| ---: | ---: | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
|    1 |   34 | điểm A có "2.000" máy tính                                                              | **2.200** — đúng theo Hình 2 (tr. 32) và theo chính Hình 3 trên cùng trang |
|    2 |   88 | đoạn "Tóm lại" phần Cung bị ghép nhầm một mảnh văn bản của đoạn "Giá đầu vào" phía trên | câu dừng ở *"…nhà sản xuất chọn mức cung bao nhiêu."*                      |
|    2 |   98 | *Khái niệm then chốt*: "quantitive demanded"                                            | **"quantity demanded"**                                                    |
|    3 |  109 | Hình 3 có hai khung con nhưng **cả hai đều đánh nhãn "(a)"**                            | khung bên phải là **"(b)"** — chính đoạn văn tr. 110 gọi nó là *Hình 3(b)* |
|    4 |  178 | cùng một nhân vật được gọi là **Jeal**, **Jean** rồi **Jane** trong một trang           | bản gốc dùng **Jane** xuyên suốt                                           |
|    5 |  298 | Ford tăng sản lượng "từ 1.000 lên **2.000** chiếc"                                      | **1.200** — chính Hình 6 trên cùng trang đánh dấu 1.000 và 1.200           |
|   12 |  448 | đoạn văn: lợi ích học đại học với nữ giới tăng "từ 35 phần trăm đến **75** phần trăm"   | **71%** — chính Bảng 1 trên cùng trang in "+71%"; tính lại được 71,2%      |
|   14 |   64 | "chi phí cơ hội của **19** ounce thịt là 4 ounce khoai tây"                             | **1 ounce** — chính Bảng 1 tr. 62 in *"1 ounce Thịt = 4 ounce Khoai tây"*  |
|    3 |  109 | *(bổ sung)* lỗi "hai khung cùng nhãn (a)" ở trên **đã xác nhận trên ảnh cắt ra**        | xem [bài 3](ly_thuyet/bai_03_do_co_gian_va_dinh_gia.md)                     |
|    5 |  287 | **nhan đề Hình 1** in là *"Thị trường nhôm"*                                            | đó là nhan đề của **Hình 1 chương 10**. Nội dung và lời giải thích của hình lại đúng là *lợi nhuận kinh tế so với lợi nhuận kế toán*. Lỗi ghép nhan đề |
|   14 |   63 | bài này dẫn *"**Bảng 2** tr. 63 (lợi ích từ thương mại)"*                               | chương 3 **không có Bảng 2**; thứ được dẫn là **bảng (c) nằm bên trong Hình 2, tr. 61**. Ảnh nhúng vào bài là chính Hình 2 |
|   14 |   62 | bài này dẫn **Bảng 1 tr. 62**                                                           | ảnh cắt ra cho thấy Bảng 1 nằm ở **tr. 63**. Lệch một trang, không đổi nội dung |

---

## Cập nhật mục lục và bản đồ

Sau khi thêm hoặc sửa bài, chạy từ thư mục gốc của môn:

```bash
python3 cap-nhat-ban-do.py
```

Script sinh lại **Mục lục** (từ các tiêu đề `##`) và **Bản đồ khoá học** trong mọi bài, từ **một định
nghĩa duy nhất** nằm trong chính script — sửa tay từng file sẽ khiến chúng lệch nhau.
