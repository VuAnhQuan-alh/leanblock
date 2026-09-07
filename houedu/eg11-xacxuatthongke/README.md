# Xác suất Thống kê — cho ngành Quản trị Kinh doanh

Khoá học tự soạn, dựng từ **Giáo trình Xác suất Thống kê** của Tống Đình Quỳ
(NXB Bách Khoa – Hà Nội, tái bản lần thứ năm, 246 trang, file gốc ở [tai_lieu/](tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf)).

Giáo trình gốc viết cho sinh viên kỹ thuật, ví dụ toàn xúc xắc, bi, mạch điện, xạ thủ.
Khoá này **giữ nguyên ví dụ giáo trình** để đi thi cho khớp, và **thêm một ví dụ Quản trị Kinh doanh
ở mỗi mục** — đánh dấu 💼 — để thấy công thức đó dùng vào việc gì ở doanh nghiệp thật.

---

## Cách đọc

| Ký hiệu         | Nghĩa                                                                             |
| --------------- | --------------------------------------------------------------------------------- |
| `tr. 12`        | trích trang số 12 của giáo trình (số trang in trên giấy, không phải số trang PDF) |
| **Thí dụ 2.3**  | ví dụ nguyên văn của giáo trình, giữ nguyên số hiệu để tra ngược                  |
| 💼 **Góc QTKD** | ví dụ thêm, bối cảnh kinh doanh — không có trong giáo trình                       |
| 📚 **Mở rộng**  | kiến thức nền giáo trình lướt qua hoặc bỏ qua                                     |
| ⚠️              | chỗ giáo trình viết dễ gây hiểu nhầm, hoặc lỗi in                                 |

Công thức viết bằng LaTeX, mở bằng **Obsidian** (hoặc VS Code + Markdown Preview Enhanced) để thấy đúng.

**Tên riêng dùng bản gốc, không phiên âm.** Giáo trình in năm 1997 viết *Béc-nu-li, Bay-ét,
Poa-xông, Trê-bư-sép, Láp-la-xơ, Stiu-đơn, Phi-sơ…*; khoá học này luôn viết **Bernoulli, Bayes,
Poisson, Chebyshev, Laplace, Student, Fisher** — đó là thứ bạn gõ vào Google, gặp trong sách
tiếng Anh và thấy trong tên hàm của mọi phần mềm thống kê.
Bảng đối chiếu đầy đủ nằm ở [bài 1, mục Từ điển thuật ngữ](ly_thuyet/bai_01_su_kien_ngau_nhien_va_giai_tich_ket_hop.md#10-từ-điển-thuật-ngữ).

---

## Bố cục kho

```
xacxuatthongke/
  ly_thuyet/   bài 1–14  — bám sát giáo trình, đi theo §
  mo_rong/     bài 15+   — thứ giáo trình 1997 không có mà QTKD 2026 cần
  thuc_hanh/             — dữ liệu .csv + script Python, tự tay tính
  tai_lieu/              — giáo trình PDF, bảng tra số
```

---

## Lộ trình 14 bài

### Phần I — Xác suất (bài 1–9)

| Bài | Tên | Nguồn |
| --- | --- | --- |
| 1 | [Sự kiện ngẫu nhiên và giải tích kết hợp](ly_thuyet/bai_01_su_kien_ngau_nhien_va_giai_tich_ket_hop.md) | Ch. I §1, tr. 5–11 |
| 2 | [Ba định nghĩa của xác suất](ly_thuyet/bai_02_ba_dinh_nghia_cua_xac_suat.md) | Ch. I §2, tr. 11–18 |
| 3 | [Xác suất có điều kiện và công thức Bernoulli](ly_thuyet/bai_03_xac_suat_co_dieu_kien_va_bernoulli.md) | Ch. I §3, tr. 18–29 |
| 4 | [Xác suất đầy đủ và công thức Bayes](ly_thuyet/bai_04_xac_suat_day_du_va_bayes.md) | Ch. I §4, tr. 29–38 |
| 5 | [Biến ngẫu nhiên và luật phân phối](ly_thuyet/bai_05_bien_ngau_nhien_va_luat_phan_phoi.md) | Ch. II §1–2, tr. 39–48 |
| 6 | [Kỳ vọng, phương sai và các số đặc trưng](ly_thuyet/bai_06_ky_vong_phuong_sai_va_cac_so_dac_trung.md) | Ch. II §3, tr. 48–56 |
| 7 | [Các phân phối thông dụng](ly_thuyet/bai_07_cac_phan_phoi_thong_dung.md) | Ch. II §4, tr. 56–78 |
| 8 | [Biến ngẫu nhiên hai chiều và hệ số tương quan](ly_thuyet/bai_08_bien_ngau_nhien_hai_chieu_va_tuong_quan.md) | Ch. III §1–2, tr. 79–96 |
| 9 | [Luật số lớn và định lý giới hạn trung tâm](ly_thuyet/bai_09_luat_so_lon_va_dinh_ly_gioi_han_trung_tam.md) | Ch. III §3–4, tr. 96–112 |

### Phần II — Thống kê (bài 10–14)

| Bài | Tên | Nguồn |
| --- | --- | --- |
| 10 | [Mẫu và thống kê mô tả](ly_thuyet/bai_10_mau_va_thong_ke_mo_ta.md) | Ch. IV §1–2, tr. 113–133 |
| 11 | [Ước lượng điểm và khoảng tin cậy](ly_thuyet/bai_11_uoc_luong_diem_va_khoang_tin_cay.md) | Ch. IV §3–4, tr. 133–157 |
| 12 | [Kiểm định giả thuyết — một mẫu](ly_thuyet/bai_12_kiem_dinh_gia_thuyet_mot_mau.md) | Ch. V §1–2, tr. 158–170 |
| 13 | [Kiểm định nhiều mẫu và phân tích phương sai](ly_thuyet/bai_13_kiem_dinh_nhieu_mau_va_anova.md) | Ch. V §3–4, tr. 170–193 |
| 14 | [Tương quan và phân tích hồi quy](ly_thuyet/bai_14_tuong_quan_va_hoi_quy.md) | Ch. VI, tr. 194–229 |

---

## Chạy code

Toàn bộ code minh hoạ viết bằng **Python thư viện chuẩn** — không cài gói nào:

```bash
python3 ten-file.py
```

Vài bài cuối (phân vị Student, chi bình phương, Fisher, hồi quy bội) cần `scipy`.
Không cài vào máy, chạy tạm bằng `uv`:

```bash
uv run --with scipy python3 ten-file.py
```

Vì sao Python chứ không phải Excel: Excel trả **một con số**, Python cho bạn thấy **công thức đẻ ra con số đó**.
Học xong rồi dùng Excel cũng được — mỗi bài đều ghi hàm Excel tương đương.

---

## Nguồn

- Tống Đình Quỳ, *Giáo trình Xác suất Thống kê*, NXB Bách Khoa – Hà Nội (tái bản lần thứ năm).
  Bản PDF quét: [tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf](tai_lieu/Giao-trinh-Xac-suat-Thong-ke.pdf), 246 trang.
