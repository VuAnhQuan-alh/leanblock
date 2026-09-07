# Lý thuyết Tài chính I — MIT 15.401

Bộ bài học tiếng Việt dựng **từ chính phụ đề gốc của video**, không viết theo trí nhớ.

**Nguồn:** khoá **MIT 15.401 *Finance Theory I*, Fall 2008** — giảng viên **Prof. Andrew W. Lo**,
MIT Sloan School of Management. **20 bài giảng, mỗi buổi ~75–80 phút, tổng ~26 giờ.**
Kênh **MIT OpenCourseWare** trên YouTube, giấy phép **CC BY-NC-SA**.

- Playlist: <https://www.youtube.com/playlist?list=PLUl4u3cNGP63B2lDhyKOsImI7FjCf6eDW>
- Trang khoá học OCW: <https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/>
- Giáo trình Lo giao: **Brealey, Myers & Allen, *Principles of Corporate Finance*, 9th ed.,
  McGraw-Hill, 2007**

> ⚠️ **Khoá này ghi học kỳ Thu 2008** — tức ngay quanh lúc Lehman Brothers sụp (15/9/2008).
> Đó vừa là điểm mạnh (được dạy xuyên qua khủng hoảng) vừa là chỗ phải đối chiếu. Mỗi bài đều có
> mục ⚠️ **đối chiếu 2026** cho những chỗ thời gian đã bác bỏ.

---

## Cách đọc

| Ký hiệu            | Nghĩa                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------- |
| `48:35`            | mốc thời gian trong video — **mọi mốc đều đã đối chiếu ngược với phụ đề gốc**           |
| `S2 45:33`         | bài gộp nhiều buổi thì mốc có tiền tố buổi: `S2` = buổi 2, `S3` = buổi 3…               |
| 📚 **Mở rộng**      | kiến thức video lướt qua, hoặc phần bài học này bổ sung thêm — **không có trong video** |
| 🇻🇳 **Góc Việt Nam** | số liệu và ví dụ trong nước — **không có trong video**                                  |
| ⚠️                  | chỗ dễ hiểu sai, chỗ video nói sai, hoặc chỗ thực tế sau 2008 đã bác lại                |
| 💡 **Tự thử**       | bài tập sửa tham số rồi quan sát, **không kèm lời giải**                                |

Công thức viết bằng LaTeX. Mở bằng **Obsidian** (hoặc VS Code + Markdown Preview Enhanced) để hiển
thị đúng.

Code thực hành viết bằng **Python 3.10+ thuần**, không dùng thư viện ngoài. Mỗi file chạy được ngay
bằng `python3 <tên-file>.py`, không cần cài gì. Kết quả **tất định** — chạy hai lần phải giống hệt.

---

## Nên học môn này thế nào

Lo mở đầu buổi 1 bằng một lời hứa rất to: *"tài chính là môn quan trọng nhất bạn từng gặp"*
(`02:25`). Bỏ qua phần quảng cáo, cấu trúc lập luận của ông thực ra rất chặt, và nắm được cấu trúc
đó thì cả 20 buổi trở nên dễ nhớ:

**1. Cả khoá học chỉ giải đúng MỘT bài toán: định giá.**
Lo tuyên bố có hai thách thức — định giá và quản trị — rồi tháo tung cái thứ hai ngay tại chỗ:
quản trị chỉ là *"chọn phương án đáng giá hơn"*. Nên mọi công cụ bạn học đều là công cụ định giá.
Khi lạc, hỏi: **cái này đang giúp tôi định giá thứ gì?**

**2. Chỉ có hai thứ làm bài toán đó khó: thời gian và rủi ro.**
Bỏ hai cái đó đi thì tài chính rút gọn về kinh tế vi mô. Toàn bộ 13 bài dưới đây chỉ là hai câu này
được viết thành công thức:

| Câu                             | Thành công thức                      | Bài  |
| ------------------------------- | ------------------------------------ | ---- |
| 1 đô hôm nay ≠ 1 đô sang năm    | chiết khấu, NPV, đường cong lãi suất | 2–5  |
| 1 đô chắc chắn ≠ 1 đô có rủi ro | phần bù rủi ro, β, CAPM              | 9–11 |

Bài 12–13 chỉ là mang hai bộ công cụ đó áp vào doanh nghiệp và vào thị trường thật.

**3. Đừng hoảng nếu tới bài 6–7 vẫn thấy rời rạc — đó là đúng lịch.**
Lo nói ông dạy khoá này nhiều lần và thấy người học thường "sáng ra" khoảng **tuần 8 đến tuần 13**
(`60:08`). Bộ khung chỉ khép lại khi **rủi ro được ghép vào thời gian**, tức bài 9–11. Chỗ bỏ cuộc
phổ biến nhất là bài 5 (trái phiếu) — cũng là chỗ **chưa** thấy được bức tranh. Ráng qua bài 11.

**4. Ba việc phải làm sau mỗi bài** — nếu không thì đọc xong là quên:

- **Trả lời câu hỏi của Lo ở `46:58`:** *"điều này làm đời tôi khá hơn ở chỗ nào?"* Viết một câu.
  Không viết nổi nghĩa là chưa hiểu.
- **Làm mục Tự thử.** *"Tài chính không phải môn thể thao để ngồi xem."* (`59:22`)
- **Làm bài tập gốc của OCW.** Lo hứa với sinh viên rằng **hơn 50 % điểm thi lấy nguyên văn từ gói
  bài tập** (`61:25`) — và OCW công bố cả **đề lẫn lời giải**. Đây là thứ giá trị nhất mà video
  không chứa: [Problem Sets](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/problem-sets/) ·
  [Exams](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/exams/).

**5. Ôn thi thì đọc "Tóm tắt một trang" của từng bài, không đọc lại cả bài.**
Mỗi bài kết thúc bằng một khối ASCII gói toàn bộ nội dung vào một màn hình. Đó là thứ để mở ra
trước kỳ thi.

---

## Lộ trình 13 bài

20 buổi giảng được gom thành 13 bài **theo ranh giới chủ đề, không theo ranh giới video** — vì Lo
thường bắt đầu chủ đề mới ở giữa buổi (`Ses 12: Options III & Risk and Return I`). Cách gom này
trùng với chính cách MIT OCW phân nhóm video trên trang khoá học.

### Phần A — Nhập môn

|    # | Bài                                                                                                    | Buổi  | Trạng thái |
| ---: | ------------------------------------------------------------------------------------------------------ | ----- | ---------- |
|    1 | [**Tài chính là gì** — hai thách thức, hai yếu tố, sáu nguyên lý](ly_thuyet/bai_01_tai_chinh_la_gi.md) | Ses 1 | ✅          |

### Phần B — Định giá (yếu tố **thời gian**)

|    # | Bài                                                                        | Buổi      | Trạng thái  |
| ---: | -------------------------------------------------------------------------- | --------- | ----------- |
|    2 | [**Giá trị hiện tại và chiết khấu**](ly_thuyet/bai_02_gia_tri_hien_tai.md) | Ses 2–3   | ✅           |
| 3 | [**Đòn bẩy, lạm phát và lãi suất thực**](ly_thuyet/bai_03_don_bay_va_lam_phat.md) | Ses 4 (nửa đầu) | ✅ |
| 4 | [**Trái phiếu I — đọc tương lai từ một bảng giá**](ly_thuyet/bai_04_trai_phieu_va_duong_cong.md) | Ses 4 (nửa sau)–5 | ✅ |
| 5 | [**Trái phiếu II — luật một giá, đo rủi ro, cỗ máy tạo AAA**](ly_thuyet/bai_05_duration_va_chung_khoan_hoa.md) | Ses 6–7 | ✅ |
| 6 | [**Cổ phiếu — chiết khấu cổ tức, tăng trưởng, và PVGO**](ly_thuyet/bai_06_co_phieu_va_tang_truong.md) | Ses 8 | ✅ |
| 7 | [**Hợp đồng kỳ hạn và hợp đồng tương lai**](ly_thuyet/bai_07_ky_han_va_tuong_lai.md) | Ses 9–10 | ✅ |
| 8 | [**Quyền chọn — payoff, ngang giá put–call, cây nhị thức, Black–Scholes**](ly_thuyet/bai_08_quyen_chon.md) | Ses 10–12 | ✅ |

### Phần C — Rủi ro

|    # | Bài                                             | Buổi      | Trạng thái  |
| ---: | ----------------------------------------------- | --------- | ----------- |
| 9 | [**Rủi ro và lợi suất**](ly_thuyet/bai_09_rui_ro_va_loi_suat.md) | Ses 12–13 | ✅ |
| 10 | [**Lý thuyết danh mục — Markowitz và biên hiệu quả**](ly_thuyet/bai_10_ly_thuyet_danh_muc.md) | Ses 13–15 | ✅ |
| 11 | [**CAPM — beta, trạng thái cân bằng, và giá của rủi ro không tránh được**](ly_thuyet/bai_11_capm_va_beta.md) | Ses 15–17 | ✅ |

### Phần D — Ứng dụng vào doanh nghiệp

|    # | Bài                                                           | Buổi      | Trạng thái  |
| ---: | ------------------------------------------------------------- | --------- | ----------- |
| 12 | [**Hoạch định ngân sách vốn — dòng tiền, lá chắn thuế, và bốn cách IRR hỏng**](ly_thuyet/bai_12_ngan_sach_von.md) | Ses 17–18 | ✅ |
| 13 | [**Thị trường hiệu quả, tài chính hành vi, và thị trường thích nghi**](ly_thuyet/bai_13_thi_truong_hieu_qua.md) | Ses 18–20 | ✅ |

> 📌 **Bài 13 không phải phần thừa.** Lo cố ý giữ lại **ba trong sáu nguyên lý nền tảng** tới tận
> buổi cuối, và hứa sẽ *"chất vấn toàn bộ bộ khung tôi đã dựng cho các bạn, và chỉ ra các lỗ hổng
> nằm ở đâu"* (`54:07`). Bỏ bài 13 là bỏ đúng nửa mà Lo cho là quan trọng nhất.
>
> ✅ **Mười ba bài theo video đã hoàn tất.** Bài 13 trả nốt lời hứa đó: ba nguyên lý bị giấu, mô hình
> não ba tầng mà khoa học thần kinh đã bác bỏ, và hai phép đo mới — tự tương quan của thị trường Mỹ
> qua **một thế kỷ** (đỉnh cao nhất rơi đúng vào tháng Lo đang giảng), và VN-Index đi từ *"dự đoán
> được rõ ràng"* sang *"không phân biệt được với bước đi ngẫu nhiên"* trong một thế hệ.

---

## Phần E — Tài chính doanh nghiệp (mở rộng ngoài video)

Mười ba bài trên bám sát 20 buổi giảng của Lo, tức nửa **đầu tư** của tài chính. Chính Lo chỉ người
học sang **15.434 Corporate Finance** cho nửa còn lại (`S20 53:30`). Phần E là nửa còn lại đó, viết
cho người học **quản trị kinh doanh**.

|    # | Bài                                             | Nguồn      | Trạng thái  |
| ---: | ----------------------------------------------- | ---------- | ----------- |
| 14 | [**🏢 Đọc doanh nghiệp bằng số — báo cáo, tỷ số, DuPont, ROIC**](ly_thuyet/bai_14_doc_doanh_nghiep_bang_so.md) | BMA · Penman | ✅ |
| 15 | [**🏢 WACC — chi phí vốn bình quân gia quyền**](ly_thuyet/bai_15_wacc.md) | BMA · Hamada | ✅ |
| 16 | [**🏢 Cơ cấu vốn — Modigliani, Miller và giới hạn của lá chắn thuế**](ly_thuyet/bai_16_co_cau_von.md) | MM 1958 · Myers–Majluf | ✅ |
| 17 | [**🏢 Chi phí đại diện, quản trị công ty và chính sách chi trả**](ly_thuyet/bai_17_chi_phi_dai_dien.md) | Jensen–Meckling · Lintner | ✅ |
| 18 | [**🏢 Định giá doanh nghiệp, M&A và giới hạn của mô hình**](ly_thuyet/bai_18_dinh_gia_doanh_nghiep.md) | Koller (McKinsey) · Roll | ✅ |
| 19 | [**🏢 Quyền chọn thực và APV — hai chỗ bộ công cụ tiêu chuẩn hỏng**](ly_thuyet/bai_19_quyen_chon_thuc_va_apv.md) | Myers 1974 · McDonald–Siegel | ✅ |
| | **— phần F: ngoài giáo trình MIT —** | | |
| 20 | [**🏛 Chu kỳ đòn bẩy — thứ cả khoá học này bỏ sót**](ly_thuyet/bai_20_chu_ky_don_bay.md) | Geanakoplos · Yale ECON 251 | ✅ |

> 🏛 **Bài 20 đến từ một khoá khác hẳn:** [Yale ECON 251 *Financial Theory*](https://oyc.yale.edu/economics/econ-251)
> của **John Geanakoplos** (Thu 2009). Nó là bài duy nhất trong khoá **mâu thuẫn trực tiếp** với
> các bài trước — luận điểm: mọi khoản vay có **hai** biến, lãi suất và mức thế chấp, và cả khoá
> 15.401 chỉ mô hình hoá biến thứ nhất. Phần cuối [mục 10 của bài 5](ly_thuyet/bai_05_duration_va_chung_khoan_hoa.md#10-convexity--và-vì-sao-trái-phiếu-có-mùi-quyền-chọn)
> cũng được bổ sung từ khoá này (quyền trả trước, lồi âm, phòng hộ động, vòng đời trung bình),
> cùng phần cuối [mục 8 của bài 10](ly_thuyet/bai_10_ly_thuyet_danh_muc.md#8-đo-rủi-ro-bằng-độ-lệch-chuẩn-là-một-lựa-chọn)
> (hàm hữu dụng, ngại rủi ro, nghịch lý St. Petersburg).

> 📐 **Phần E phủ đủ giáo trình [MIT 15.402 *Finance Theory II*](https://ocw.mit.edu/courses/15-402-finance-theory-ii-spring-2003/pages/lecture-notes/)** — phần tiếp
> chính thức của 15.401, vốn chỉ có bản 2003 **không có video**. Bài 19 lấp hai mục cuối cùng
> còn thiếu sau khi đối chiếu: *Real Options* và *APV*.
>
> 🏢 **Phần E khác phần A–D ở một điểm quan trọng:** không có video để đối chiếu, nên không có mốc
> `MM:SS`. Đổi lại, mọi con số đọc từ **báo cáo tài chính thật đã kiểm toán** — tới bài 16 là 28
> doanh nghiệp Việt Nam niêm yết trong 16 năm, cộng báo cáo 10-K của 12 doanh nghiệp Mỹ nộp lên
> SEC. Kiểm chứng chuyển từ *đối chiếu phụ đề* sang **đối chiếu đẳng thức kế toán**: bốn đẳng thức
> phải đúng ở mọi năm-công-ty, và chương trình sẽ dừng nếu một dòng sai.

---

## Bố cục kho

```
mit-15401-finance/
  README.md               ← bạn đang ở đây
  ly_thuyet/              20 bài học — chữ, bảng, hình, và kết quả chạy thật
  thuc_hanh/              20 chương trình Python — nơi mọi con số được TÍNH RA
    README.md             chỉ mục, luật viết code, nguồn dữ liệu
    bai-01-...py ... bai-20-...py
  hinh/                   67 biểu đồ SVG — sinh từ chính dữ liệu ở thuc_hanh/
    README.md             danh sách hình, quy ước vẽ
    svg_loi.py            lõi vẽ SVG bằng thư viện chuẩn
    sinh-hinh.py          chạy một lệnh là sinh lại cả 67 hình
```

**Code chỉ nằm ở một chỗ.** Bài lý thuyết không chép lại mã nguồn — nó liên kết tới file trong
`thuc_hanh/` và dán **output chạy thật**. Mỗi lần sửa bài, một script chạy lại cả 20 chương trình và
đối chiếu output **từng ký tự** với khối `Kết quả chạy thật:` trong bài tương ứng; lệch một ký tự là
báo lỗi. Chi tiết ở [thuc_hanh/README.md](thuc_hanh/README.md).

Cả 20 chương trình **không cần cài gói nào** và **không gọi mạng** — dữ liệu thật được nhúng thẳng
trong file. tổng **17.223 dòng** code sinh ra **5.867 dòng** kết quả.

**Hình cũng không nằm ở hai chỗ.** 59 biểu đồ trong [`hinh/`](hinh/README.md) được sinh bằng Python
thư viện chuẩn, đọc thẳng dữ liệu từ `thuc_hanh/` — không matplotlib, không vẽ tay, không gõ lại con
số nào. Sửa dữ liệu rồi chạy `python3 sinh-hinh.py` là hình tự cập nhật theo.

---

## Ghi chú về độ tin cậy

Mỗi bài học tuân bốn quy tắc, không có ngoại lệ:

1. **Mọi mốc `MM:SS` đều được đối chiếu ngược với phụ đề gốc bằng script.** Không có mốc nào ghi
   theo trí nhớ.
2. **Video nói sai thì đính chính, không chép lại.** Đã gặp ở bài 1: Lo nói chiết khấu *"66 %"*
   trong khi số thật là 69,8 %, và nói doanh thu GE tăng *"4,5 lần"* trong khi hai con số của chính
   ông cho ra 5,0 lần. Cả hai đều được ghi rõ kèm mốc thời gian.
3. **Dữ kiện ngoài video phải có nguồn độc lập**, liệt kê ở mục Nguồn cuối mỗi bài.
4. **Output code trong bài là output chạy thật**, không gõ tay.
