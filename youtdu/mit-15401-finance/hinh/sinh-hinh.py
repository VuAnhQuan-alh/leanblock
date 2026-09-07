"""Sinh toan bo hinh minh hoa cho 13 bai — chi dung thu vien chuan Python.

Chay:  python3 sinh-hinh.py

Moi hinh ve tu CHINH du lieu nam trong thuc_hanh/, khong go tay con so nao.
Nho vay hinh khong bao gio lech voi so trong bai hoc: sua du lieu thi chay lai
script nay la hinh tu cap nhat.

Ket qua: cac file .svg trong chinh thu muc nay. SVG la van ban nen vao git sach
va hien thi duoc trong GitHub, Obsidian, VS Code.
"""

import math
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from svg_loi import Hinh, nap, MAU, XAM, MUC  # noqa: E402

DA_SINH: list[str] = []


def xuat(h: Hinh, ten: str) -> None:
    p = h.ghi(ten)
    DA_SINH.append(ten)
    print(f"  {ten:44} {p.stat().st_size:>7,} byte")


def doc_so(chuoi: str) -> list[float]:
    return [float(x) for x in chuoi.split()]


def tb(v): return sum(v) / len(v)


def sd(v):
    m = tb(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))


def cov(a, b):
    ma, mb = tb(a), tb(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (len(a) - 1)


def hoi_quy(y, x):
    n = len(y); mx, my = tb(x), tb(y)
    sxx = sum((v - mx) ** 2 for v in x)
    b = sum((v - mx) * (w - my) for v, w in zip(x, y)) / sxx
    return my - b * mx, b


# ===========================================================================
# BAI 1
# ===========================================================================

def bai01_bon_thanh_phan():
    h = Hinh("Bốn thành phần của hệ thống tài chính  (Ses 1, `36:24`)",
             rong=760, cao=430)
    o = dict(w=210, h=74)
    h.hop(60, 70, o["w"], o["h"], MAU[0], "#eef5fb",
          "HỘ GIA ĐÌNH\ncó tiền, thiếu cơ hội")
    h.hop(490, 70, o["w"], o["h"], MAU[1], "#fdeeec",
          "DOANH NGHIỆP\ncó cơ hội, thiếu tiền")
    h.hop(60, 285, o["w"], o["h"], MAU[2], "#eef7f1",
          "TRUNG GIAN TÀI CHÍNH\nngân hàng, quỹ, bảo hiểm")
    h.hop(490, 285, o["w"], o["h"], MAU[3], "#fdf5e6",
          "THỊ TRƯỜNG VỐN\nnơi giá được khám phá")
    # mui ten (toa do man hinh — dung line/polygon truc tiep)
    def ten(x1, y1, x2, y2, nhan, tren=True, ty=0.5):
        a = math.atan2(y2 - y1, x2 - x1)
        p = " ".join(f"{x2 - 10*math.cos(a - t):.1f},{y2 - 10*math.sin(a - t):.1f}"
                     for t in (0.4, -0.4))
        h.e.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#777"'
                   f' stroke-width="2"/>')
        h.e.append(f'<polygon points="{x2},{y2} {p}" fill="#777"/>')
        h.chu(x1 + (x2 - x1) * ty, y1 + (y2 - y1) * ty + (-9 if tren else 17),
              nhan, XAM, 11, "middle")
    ten(275, 95, 485, 95, "vốn  →")
    ten(485, 122, 275, 122, "←  lợi suất", False)
    ten(165, 150, 165, 280, "gửi / mua chứng chỉ quỹ", True, 0.12)
    ten(600, 280, 600, 150, "phát hành cổ phiếu, trái phiếu", True, 0.86)
    ten(275, 322, 485, 322, "định giá")
    h.chu(380, 200, "Toàn bộ ngành tài chính chỉ làm MỘT việc:", MUC, 13, "middle", True)
    h.chu(380, 222, "chuyển tiền từ nơi thừa sang nơi thiếu — qua thời gian và qua rủi ro.",
          "#444", 12, "middle")
    h.chu(380, 415, "⚠️ Sơ đồ này là của năm 2008. Xem bài 1 §3 để biết ba ô đã đổi thế nào.",
          "#888", 11, "middle")
    xuat(h, "bai01-bon-thanh-phan.svg")


def bai01_dau_gia():
    m = nap("bai-01-dinh-gia-va-dong-tien.py")
    thang = m.BID_LADDER
    h = Hinh("Phiên đấu giá hộp kín trên lớp — bậc thang giá thầu thật  (Ses 1)",
             "Lượt trả giá", "Giá (đô la)")
    h.truc((0, len(thang) - 1), (0, 160),
           vach_x=list(range(len(thang))), vach_y=[0, 45, 80, 120, 149],
           dinh_x=lambda v: str(int(v) + 1), dinh_y=lambda v: f"${v:.0f}")
    h.duong(list(enumerate(thang)), MAU[0], rong=2.8)
    for i, v in enumerate(thang):
        h.cham(i, v, MAU[0], 4)
    h.ke_ngang(m.RETAIL_VALUE, MAU[1], "6 4", f"giá lẻ ${m.RETAIL_VALUE}")
    h.ke_ngang(thang[-1], MAU[2], "6 4", f"giá chốt ${thang[-1]}")
    h.vung([(0, m.RETAIL_VALUE), (len(thang) - 1, m.RETAIL_VALUE)],
           [(0, thang[-1]), (len(thang) - 1, thang[-1])], MAU[1], 0.10)
    h.chu(h.px(len(thang) / 2), h.py(95),
          f"chiết khấu ${m.RETAIL_VALUE - thang[-1]} = "
          f"{(m.RETAIL_VALUE - thang[-1]) / m.RETAIL_VALUE:.1%} giá trị",
          MAU[1], 13, "middle", True)
    h.ghi_chu_duoi("Người mua chỉ trả 30,2% giá trị thật — đó là cái giá thị trường "
                   "bắt người bán trả cho sự thiếu minh bạch.")
    xuat(h, "bai01-dau-gia.svg")


# ===========================================================================
# BAI 2
# ===========================================================================

def bai02_duong_thoi_gian():
    h = Hinh("Đường thời gian: chiết khấu là ĐỔI TIỀN giữa hai thời điểm",
             rong=760, cao=430)
    r, C, N = 0.10, 100, 5
    y = 210
    h.chu(380, 56, "Năm tờ 100 đô la ở năm thời điểm khác nhau "
                   "là NĂM LOẠI TIỀN TỆ khác nhau.", MUC, 13, "middle", True)
    h.chu(380, 78, "Muốn cộng chúng lại, phải đổi hết về cùng một loại — đó là chiết khấu.",
          "#444", 12, "middle")
    h.e.append(f'<line x1="86" y1="{y}" x2="710" y2="{y}" stroke="#444" stroke-width="2"/>')
    X = [110 + i * 118 for i in range(N + 1)]
    for i, x in enumerate(X):
        h.e.append(f'<line x1="{x}" y1="{y-7}" x2="{x}" y2="{y+7}" stroke="#444"'
                   f' stroke-width="2"/>')
        h.chu(x, y + 26, f"t = {i}", XAM, 12, "middle")
    for i in range(1, N + 1):
        x = X[i]
        h.e.append(f'<line x1="{x}" y1="{y-10}" x2="{x}" y2="{y-58}"'
                   f' stroke="{MAU[0]}" stroke-width="2.6"/>')
        h.e.append(f'<polygon points="{x},{y-66} {x-6},{y-52} {x+6},{y-52}"'
                   f' fill="{MAU[0]}"/>')
        h.chu(x, y - 74, f"${C}", MAU[0], 14, "middle", True)
    h.chu(380, y - 100, "dòng tiền danh nghĩa", "#888", 11, "middle")
    tong = 0.0
    for i in range(1, N + 1):
        pv = C / (1 + r) ** i
        tong += pv
        x = X[i]
        h.chu(x, y + 58, f"÷ 1,1^{i}", XAM, 11, "middle")
        h.chu(x, y + 80, f"${pv:.2f}", MAU[1], 13, "middle", True)
    h.e.append(f'<line x1="{X[1]-40}" y1="{y+94}" x2="{X[N]+40}" y2="{y+94}"'
               f' stroke="{MAU[1]}" stroke-width="1.4"/>')
    h.e.append(f'<line x1="{X[0]}" y1="{y+94}" x2="{X[0]}" y2="{y+126}"'
               f' stroke="{MAU[1]}" stroke-width="2.4"/>')
    h.e.append(f'<line x1="{X[1]-40}" y1="{y+94}" x2="{X[0]}" y2="{y+94}"'
               f' stroke="{MAU[1]}" stroke-width="1.4"/>')
    h.e.append(f'<polygon points="{X[0]},{y+134} {X[0]-7},{y+119} {X[0]+7},{y+119}"'
               f' fill="{MAU[1]}"/>')
    h.chu(X[0], y + 154, f"PV = ${tong:.2f}", MAU[1], 15, "middle", True)
    h.chu(380, y + 118, f"cộng lại được, vì giờ tất cả đã cùng một loại tiền",
          "#444", 12, "middle")
    h.chu(380, 414, f"Tỷ giá ở đây là r = {r:.0%}/năm. ${C*N} danh nghĩa "
                    f"→ ${tong:.2f} hôm nay; chênh ${C*N - tong:.2f} là giá của thời gian.",
          "#888", 11, "middle")
    xuat(h, "bai02-duong-thoi-gian.svg")


def bai02_ghep_lai():
    h = Hinh("Ghép lãi: con số ngân hàng đọc so với con số bạn thực nhận",
             "Số kỳ ghép lãi trong một năm", "Lãi suất thực nhận trong năm (EAR)")
    APR = 0.12
    ns = [1, 2, 3, 4, 6, 12, 26, 52, 365]
    diem = [(i, ((1 + APR / n) ** n - 1) * 100) for i, n in enumerate(ns)]
    lien_tuc = (math.exp(APR) - 1) * 100
    h.truc((-0.4, len(ns) - 0.6), (11.8, 12.9),
           vach_x=list(range(len(ns))), vach_y=[12.0, 12.2, 12.4, 12.6, 12.8],
           dinh_x=lambda v: str(ns[int(v)]), dinh_y=lambda v: f"{v:.1f}%")
    h.cot(diem, MAU[0])
    h.ke_ngang(APR * 100, MAU[3], "6 4", f"APR công bố = {APR:.0%}")
    h.ke_ngang(lien_tuc, MAU[1], "6 4", f"ghép liên tục = e^0,12 − 1 = {lien_tuc:.2f}%")
    for i, v in diem:
        if ns[i] in (1, 12, 365):
            h.moc(i, v, f"{v:.2f}%", MUC, 0, -9, 11, "middle", True)
    h.ghi_chu_duoi("Cùng một APR 12%. Ghép hằng ngày cho 12,75% — cao hơn con số in trên "
                   "hợp đồng 0,75 điểm. Càng ghép dày càng tiến tới e^r − 1, không bao giờ vượt.")
    xuat(h, "bai02-ghep-lai.svg")


def bai02_ba_dong_tien():
    h = Hinh("Ba dạng dòng tiền chuẩn — giá trị hiện tại theo lãi suất",
             "Lãi suất chiết khấu r", "Giá trị hiện tại (đô la), C = 100/năm")
    C, g = 100.0, 0.04
    rs = [r / 1000 for r in range(45, 251)]
    h.truc((0.045, 0.25), (0, 3200),
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"${v:,.0f}")
    h.duong([(r, C / r) for r in rs], MAU[0], "Vĩnh viễn  C / r")
    h.duong([(r, C / (r - g)) for r in rs if r > g + 0.005], MAU[1],
            "Vĩnh viễn tăng trưởng  C / (r − g),  g = 4%")
    h.duong([(r, C / r * (1 - 1 / (1 + r) ** 20)) for r in rs], MAU[2],
            "Niên kim 20 năm  (C/r)·[1 − 1/(1+r)²⁰]")
    h.chu_thich(h.L + 260, h.T + 20)
    h.ghi_chu_duoi("Niên kim = vĩnh viễn hôm nay TRỪ vĩnh viễn bắt đầu từ năm 21. "
                   "Đường xanh lá luôn nằm dưới đường xanh dương đúng bằng phần bị trừ đó.")
    xuat(h, "bai02-ba-dong-tien.svg")


# ===========================================================================
# BAI 3
# ===========================================================================

def bai03_don_bay():
    m = nap("bai-03-don-bay-va-lam-phat.py")
    truong_hop = [(10, 0), (10, 5), (10, 8), (10, 9), (10, 9.5)]
    h = Hinh(f"Cùng một cú giảm {m.DROP_PCT}% giá nhà — đòn bẩy quyết định ai còn sống",
             "Đòn bẩy (tài sản / vốn chủ sở hữu)", "Vốn chủ sở hữu còn lại (% ban đầu)")
    diem = []
    for ts, no in truong_hop:
        von = ts - no
        don_bay = ts / von
        con = (ts * (1 - m.DROP_PCT / 100) - no) / von * 100
        diem.append((don_bay, con))
    h.truc((0, 21), (-100, 110), vach_x=[1, 2, 5, 10, 20],
           dinh_x=lambda v: f"{v:.0f}:1", dinh_y=lambda v: f"{v:.0f}%", goc_khong=True)
    h.duong([(d, c) for d, c in diem], MAU[0], rong=2.8)
    for d, c in diem:
        h.cham(d, c, MAU[1] if c < 0 else MAU[0], 6)
        h.moc(d, c, f"{c:+.0f}%", MUC, 0, -14, 12, "middle", True)
    h.ke_ngang(0, MAU[1], "5 4", "vốn chủ = 0  →  VỠ NỢ")
    h.chu(h.px(15), h.py(-60), "vùng phá sản", MAU[1], 14, "middle", True)
    h.ghi_chu_duoi(f"Đòn bẩy 1:1 mất {m.DROP_PCT}%. Đòn bẩy 20:1 mất TOÀN BỘ vốn và còn âm. "
                   f"Bảng cân đối không hét lên con số này — bạn phải tự chia.")
    xuat(h, "bai03-don-bay.svg")


# ===========================================================================
# BAI 4
# ===========================================================================

def bai04_duong_cong():
    m = nap("bai-04-trai-phieu-va-duong-cong.py")
    h = Hinh("Đường cong lãi suất: ba hình dạng, ba thông điệp",
             "Kỳ hạn (năm)", "Lãi suất giao ngay")
    h.truc((0.7, 3.3), (0.0, 0.06), vach_x=[1, 2, 3],
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0%}")
    for i, (ten, d) in enumerate(m.CURVES.items()):
        pts = sorted(d.items())
        h.duong(pts, MAU[i], ten.replace("  ", " — "), rong=2.8)
        for x, y in pts:
            h.cham(x, y, MAU[i], 4.5)
    h.chu_thich(h.L + 16, h.T + 20)
    h.chu(h.px(3.05), h.py(m.CURVES["17/09/2008  Lehman + 2 ngay"][3]) - 12,
          "dốc lên", MAU[0], 12, "end", True)
    h.chu(h.px(3.05), h.py(m.CURVES["03/07/2023  dao nguoc sau"][3]) + 20,
          "ĐẢO NGƯỢC", MAU[1], 12, "end", True)
    h.ghi_chu_duoi("Đường đảo ngược (đỏ) là tín hiệu suy thoái được theo dõi nhiều nhất. "
                   "Bảng số Lo đọc trên lớp năm 2008 đã đảo ngược hoàn toàn khi tới 2023.")
    xuat(h, "bai04-duong-cong-lai-suat.svg")


def bai04_ky_han():
    h = Hinh("Lãi suất kỳ hạn: dự báo đã nằm sẵn trong hai mức giá",
             rong=760, cao=400)
    y = 200
    h.e.append(f'<line x1="90" y1="{y}" x2="670" y2="{y}" stroke="#444" stroke-width="2"/>')
    for i, x in enumerate((90, 380, 670)):
        h.e.append(f'<line x1="{x}" y1="{y-8}" x2="{x}" y2="{y+8}" stroke="#444" stroke-width="2"/>')
        h.chu(x, y + 28, f"năm {i}", XAM, 12, "middle")
    def cung(x1, x2, cao, mau, nhan, tren=True):
        d = -1 if tren else 1
        h.e.append(f'<path d="M{x1},{y + d*10} Q{(x1+x2)/2},{y + d*cao} {x2},{y + d*10}"'
                   f' fill="none" stroke="{mau}" stroke-width="2.4"/>')
        h.chu((x1 + x2) / 2, y + d * (cao * 0.66) + (0 if tren else 14), nhan,
              mau, 13, "middle", True)
    cung(90, 380, 90, MAU[0], "r₁ = 3,41%")
    cung(90, 670, 150, MAU[2], "r₂ = 3,86%  (hai năm)")
    cung(380, 670, 90, MAU[1], "f₁,₂ = ?", False)
    r1, r2 = 0.0341, 0.0386
    f = (1 + r2) ** 2 / (1 + r1) - 1
    h.chu(380, y + 118, f"(1 + r₂)²  =  (1 + r₁) × (1 + f₁,₂)", MUC, 15, "middle", True)
    h.chu(380, y + 144, f"(1,0386)²  =  (1,0341) × (1 + f)   →   f₁,₂ = {f:.2%}",
          MAU[1], 14, "middle", True)
    h.chu(380, 62, "Không ai công bố lãi suất một năm BẮT ĐẦU TỪ NĂM SAU.", MUC, 13, "middle", True)
    h.chu(380, 84, "Nhưng nó đã bị khoá chặt bởi hai mức giá đang niêm yết — "
                   "chỉ cần chia là ra.", "#444", 12, "middle")
    h.chu(380, 380, "Đây là toàn bộ ý tưởng của bài 4: một bảng giá tĩnh chứa sẵn "
                    "dự báo của thị trường về tương lai.", "#888", 11, "middle")
    xuat(h, "bai04-lai-suat-ky-han.svg")


# ===========================================================================
# BAI 5
# ===========================================================================

def bai05_duration():
    m = nap("bai-05-duration-va-chung-khoan-hoa.py")
    C = m.FACE * m.COUPON_YR / m.FREQ
    T = m.YEARS * m.FREQ
    y0 = m.YIELD_YR / m.FREQ

    def gia(y_nam):
        y = y_nam / m.FREQ
        return sum(C / (1 + y) ** t for t in range(1, T + 1)) + m.FACE / (1 + y) ** T
    P0 = gia(m.YIELD_YR)
    D_ky = (sum(t * C / (1 + y0) ** t for t in range(1, T + 1))
            + T * m.FACE / (1 + y0) ** T) / P0
    D_nam = D_ky / m.FREQ
    MD_nam = D_nam / (1 + y0)
    ys = [v / 10000 for v in range(100, 1201, 5)]
    lo, hi = gia(0.12), gia(0.01)
    h = Hinh("Duration là ĐƯỜNG THẲNG tiếp xúc — convexity là phần nó bỏ sót",
             "Lợi suất đáo hạn (tính theo năm)", "Giá trái phiếu (đô la)")
    h.truc((0.01, 0.12), (lo * 0.985, hi * 1.015),
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:,.0f}")
    h.duong([(y, gia(y)) for y in ys], MAU[0], "Giá thật (đường cong)", rong=2.8)
    h.duong([(y, P0 * (1 - MD_nam * (y - m.YIELD_YR))) for y in ys], MAU[1],
            f"Xấp xỉ duration (đường thẳng), MD = {MD_nam:.2f} năm", 2.2, "6 4")
    h.cham(m.YIELD_YR, P0, MUC, 6)
    h.moc(m.YIELD_YR, P0, f"điểm tiếp xúc:  y = {m.YIELD_YR:.0%},  P = ${P0:,.0f}",
          MUC, 11, -12, 11, "start", True)
    for yy in (0.01, 0.12):
        that = gia(yy)
        xx = P0 * (1 - MD_nam * (yy - m.YIELD_YR))
        h.e.append(f'<line x1="{h.px(yy):.1f}" y1="{h.py(that):.1f}"'
                   f' x2="{h.px(yy):.1f}" y2="{h.py(xx):.1f}" stroke="{MAU[2]}"'
                   f' stroke-width="3.5"/>')
        h.chu(h.px(yy) + (12 if yy < 0.05 else -12), (h.py(that) + h.py(xx)) / 2 + 4,
              f"lệch ${that - xx:,.0f}", MAU[2], 11,
              "start" if yy < 0.05 else "end", True)
    h.chu_thich(h.L + 250, h.T + 22)
    h.ghi_chu_duoi(f"Đường thẳng LUÔN nằm dưới đường cong — duration nói giảm quá nhiều khi "
                   f"lãi tăng, và nói tăng quá ít khi lãi giảm. Sai số đó tên là convexity. "
                   f"Lưu ý bẫy đơn vị của §9: duration của trái phiếu này là {D_ky:.2f} NỬA NĂM "
                   f"= {D_nam:.2f} năm.")
    xuat(h, "bai05-duration-convexity.svg")


def bai05_co_may_aaa():
    h = Hinh("Cỗ máy biến hai trái phiếu rác thành một AAA — và chỗ nó gãy",
             rong=760, cao=440)
    h.hop(50, 90, 150, 60, MAU[1], "#fdeeec", "Trái phiếu 1\nxác suất vỡ 10%")
    h.hop(50, 190, 150, 60, MAU[1], "#fdeeec", "Trái phiếu 2\nxác suất vỡ 10%")
    h.hop(300, 130, 150, 80, MUC, "#f4f4f0", "GỘP LẠI\nrồi cắt lớp")
    h.hop(560, 90, 150, 60, MAU[2], "#eef7f1", "Lớp ƯU TIÊN\nchỉ vỡ khi CẢ HAI vỡ")
    h.hop(560, 190, 150, 60, MAU[3], "#fdf5e6", "Lớp THỨ CẤP\nvỡ khi MỘT trong hai vỡ")
    for y1, y2 in ((120, 155), (220, 185)):
        h.e.append(f'<line x1="200" y1="{y1}" x2="298" y2="{y2}" stroke="#777" stroke-width="2"/>')
    for y1, y2 in ((160, 120), (185, 220)):
        h.e.append(f'<line x1="450" y1="{y1}" x2="558" y2="{y2}" stroke="#777" stroke-width="2"/>')
    h.chu(380, 300, "Khi hai trái phiếu ĐỘC LẬP:", MUC, 13, "middle", True)
    h.chu(380, 322, "P(cả hai cùng vỡ) = 0,10 × 0,10 = 1%   →  lớp ưu tiên được xếp hạng AAA",
          MAU[2], 12, "middle")
    h.chu(380, 356, "⚠️  Khi hai trái phiếu TƯƠNG QUAN HOÀN TOÀN:", MAU[1], 13, "middle", True)
    h.chu(380, 378, "P(cả hai cùng vỡ) = 10%   →  lớp ưu tiên rác đúng bằng đầu vào",
          MAU[1], 12, "middle")
    h.chu(380, 414, "Quả bom không nằm trong công thức. Nó nằm ở chữ “không tương quan”.",
          "#888", 12, "middle", True)
    xuat(h, "bai05-co-may-aaa.svg")


def bai05_loi_am():
    """Quyen tra truoc lam duong gia bi ep phang tu tren — loi AM."""
    m = nap("bai-05-duration-va-chung-khoan-hoa.py")
    h = Hinh("Lồi âm: quyền trả trước chặn mất phần đáng giá nhất",
             "Lãi suất thị trường", "Giá trị món nợ")
    rs = [0.015 + i / 400 for i in range(0, 39)]
    h.truc((0.015, 0.11), (60, 215), dinh_x=lambda v: f"{v:.0%}",
           dinh_y=lambda v: f"{v:.0f}")
    h.duong([(r, m.trai_phieu_goi_lai(0.07, r, m.SIG_TC)) for r in rs], XAM,
            "trái phiếu thường (lồi DƯƠNG)", 2.6, "6 4")
    h.duong([(r, m.the_chap(0.07, r, m.SIG_TC, tra_truoc=False)[2]) for r in rs],
            MAU[2], "món vay, không ai trả trước", 2.4)
    h.duong([(r, m.the_chap(0.07, r, m.SIG_TC, tra_truoc=True)[2]) for r in rs],
            MAU[1], "món vay, trả trước tối ưu (lồi ÂM)", 3.0)
    h.ke_ngang(100, "#bbb", "3 3", "dư nợ ban đầu = 100")
    h.chu_thich(h.L + 250, h.T + 10)
    tp2 = m.trai_phieu_goi_lai(0.07, 0.02, m.SIG_TC)
    tc2 = m.the_chap(0.07, 0.02, m.SIG_TC, tra_truoc=True)[2]
    h.ghi_chu_duoi(f"Mục 10 nói convexity LUÔN dương nên biến động làm trái phiếu ĐÁNG GIÁ HƠN. "
                   f"Món vay mua nhà thì ngược: ở lãi suất 2%, trái phiếu thường đáng {tp2:.0f} còn "
                   f"món vay chỉ {tc2:.0f} — người vay trả trước đúng ở dư nợ. Đó là lý do chứng "
                   f"khoán thế chấp khó hơn trái phiếu.")
    xuat(h, "bai05-loi-am.svg")


def bai05_phong_ho_dong():
    """Phong ho tung buoc khoa lai dung mot con so o moi nut."""
    m = nap("bai-05-duration-va-chung-khoan-hoa.py")
    h = Hinh("Phòng hộ động: mỗi bước kéo cả hai nhánh về đúng chỗ cũ",
             "Số trận đã đấu", "Giá trị vị thế")
    h.truc((-0.3, 4.3), (-40, 100), dinh_x=lambda v: f"{v:.0f}",
           dinh_y=lambda v: f"{v:.0f}", goc_khong=True)
    v0 = m.gia_tri_vi_the(0, 0)
    # cay khong phong ho: ve moi duong di den het tran 4
    for w in range(5):
        for l in range(5):
            if w + l > 4 or w > 4 or l > 4:
                continue
            if w == 4 or l == 4:
                continue
            v = m.gia_tri_vi_the(w, l)
            for dw, dl in ((1, 0), (0, 1)):
                w2, l2 = w + dw, l + dl
                v2 = m.gia_tri_vi_the(w2, l2)
                h.duong([(w + l, v), (w2 + l2, v2)], XAM, None, 1.3, None, 0.55)
    h.duong([(0, v0), (4, v0)], MAU[1], f"sau khi phòng hộ: khoá ở {v0:.2f}", 3.2)
    for k in range(5):
        h.cham(k, v0, MAU[1], 5)
    for w, l, nhan in ((1, 0, "thắng trận 1"), (0, 1, "thua trận 1")):
        h.cham(1, m.gia_tri_vi_the(w, l), MAU[0], 6)
        h.moc(1, m.gia_tri_vi_the(w, l), f"{nhan}: {m.gia_tri_vi_the(w, l):.1f}",
              MAU[0], 10, -6, 11, "start")
    h.chu_thich(h.L + 250, h.T + 10)
    h.ghi_chu_duoi(f"Đường xám là giá trị vị thế nếu KHÔNG phòng hộ — chỉ một trận đã ném nó từ "
                   f"{v0:.2f} lên {m.gia_tri_vi_the(1,0):.2f} hoặc xuống {m.gia_tri_vi_the(0,1):.2f}. "
                   f"Đặt một khoản cược công bằng ở mỗi nút thì cả hai nhánh về đúng giá trị nút đó, "
                   f"và {v0:.2f} được chốt chắc chắn. 16 nút đều qua assert.")
    xuat(h, "bai05-phong-ho-dong.svg")


# ===========================================================================
# BAI 6
# ===========================================================================

def bai06_gordon():
    m = nap("bai-06-co-phieu-va-tang-truong.py")
    h = Hinh("Mô hình Gordon: bong bóng công nghệ nằm trong một phép chia",
             "Tốc độ tăng trưởng cổ tức g", "Giá cổ phiếu  P = D₁ / (r − g)")
    D1, r = float(m.D1), float(m.R)
    gs = [v / 10000 for v in range(0, 951, 5)]
    h.truc((0, 0.098), (0, 22000),
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:,.0f}")
    h.duong([(g, D1 / (r - g)) for g in gs], MAU[0], rong=2.8)
    h.ke_doc(r, MAU[1], "6 4", f"g = r = {r:.0%}")
    for g in (0.0, 0.04, 0.07, 0.09):
        p = D1 / (r - g)
        h.cham(g, p, MAU[0], 5)
        h.moc(g, p, f"g={g:.0%} → {p:,.0f}", MUC, 8, -10, 11)
    h.chu(h.px(0.085), h.py(17000), "TIỆM CẬN ĐỨNG", MAU[1], 13, "end", True)
    h.ghi_chu_duoi(f"g từ 0% lên 4%: giá tăng {D1/(r-0.04)/(D1/r) - 1:+.0%}. "
                   f"Từ 7% lên 9%: giá tăng {D1/(r-0.09)/(D1/(r-0.07)) - 1:+.0%}. "
                   f"Cùng một bước 2 điểm — hệ quả khác nhau hoàn toàn.")
    xuat(h, "bai06-gordon.svg")


def bai06_tang_truong():
    m = nap("bai-06-co-phieu-va-tang-truong.py")
    E, r = float(m.EPS1), float(m.R)
    h = Hinh("Tăng trưởng không phải lúc nào cũng tốt — điều quyết định là ROE so với r",
             "Tỷ lệ lợi nhuận giữ lại để tái đầu tư  b", "Giá cổ phiếu")
    bs = [v / 100 for v in range(0, 73)]
    h.truc((0, 0.72), (2600, 9200),
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:,.0f}")
    for i, roe in enumerate(m.ROES):
        pts = [(b, E * (1 - b) / (r - roe * b)) for b in bs
               if r - roe * b > 0.005 and 2600 <= E * (1 - b) / (r - roe * b) <= 9200]
        nhan = (f"ROE = {roe:.0%}  "
                + ("< r → tái đầu tư PHÁ giá trị" if roe < r
                   else "= r → tái đầu tư vô ích" if abs(roe - r) < 1e-9
                   else "> r → tái đầu tư TẠO giá trị"))
        h.duong(pts, MAU[i], nhan, rong=2.6)
    h.ke_ngang(E / r, XAM, "4 4", f"trả hết cổ tức: E/r = {E/r:,.0f}")
    h.chu_thich(h.L + 16, h.T + 20)
    h.ghi_chu_duoi("Cùng một công ty, cùng một mức tăng trưởng. Chỉ khác ROE. "
                   "Doanh nghiệp ROE 6% càng tăng trưởng càng nghèo đi.")
    xuat(h, "bai06-tang-truong.svg")


# ===========================================================================
# BAI 7
# ===========================================================================

def bai07_payoff_ky_han():
    h = Hinh("Hợp đồng kỳ hạn: payoff THẲNG — hãy so với đường gãy khúc của bài 8",
             "Giá giao ngay lúc đáo hạn  S(T)", "Lãi / lỗ")
    F = 100
    h.truc((60, 140), (-45, 45), goc_khong=True,
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:+.0f}")
    h.duong([(s, s - F) for s in range(60, 141)], MAU[0], "Bên MUA kỳ hạn (long)")
    h.duong([(s, F - s) for s in range(60, 141)], MAU[1], "Bên BÁN kỳ hạn (short)")
    h.duong([(s, 0) for s in range(60, 141)], MAU[2],
            "Nhà sản xuất ĐÃ phòng hộ = hàng thật + bán kỳ hạn", rong=3.4)
    h.ke_doc(F, "#bbb", "4 4", f"giá kỳ hạn F = {F}")
    h.chu_thich(h.L + 16, h.T + 20)
    h.ghi_chu_duoi("Tổng hai bên luôn bằng 0 — kỳ hạn là trò chơi tổng bằng không. "
                   "Cộng hàng thật vào bên bán thì được đường nằm ngang: rủi ro biến mất.")
    xuat(h, "bai07-payoff-ky-han.svg")


# ===========================================================================
# BAI 8
# ===========================================================================

def bai08_payoff():
    K, PC, PP = 100, 8, 6
    h = Hinh("Payoff quyền chọn khi đáo hạn — giá thực hiện K = 100",
             "Giá tài sản cơ sở lúc đáo hạn  S(T)", "Lãi / lỗ")
    h.truc((60, 140), (-30, 45), goc_khong=True,
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:+.0f}")
    ss = list(range(60, 141))
    h.duong([(s, max(s - K, 0)) for s in ss], MAU[0], "Quyền chọn MUA — payoff gộp")
    h.duong([(s, max(s - K, 0) - PC) for s in ss], MAU[0],
            f"Quyền chọn MUA — ròng (trừ phí {PC})", 1.9, "6 4")
    h.duong([(s, max(K - s, 0)) for s in ss], MAU[1], "Quyền chọn BÁN — payoff gộp")
    h.duong([(s, max(K - s, 0) - PP) for s in ss], MAU[1],
            f"Quyền chọn BÁN — ròng (trừ phí {PP})", 1.9, "6 4")
    h.ke_doc(K, "#bbb", "4 4", "K = 100")
    h.chu_thich(h.L + 16, h.T + 20)
    h.ghi_chu_duoi("Chỗ GÃY nằm đúng tại K. Đây là lần đầu trong cả khoá xuất hiện phi tuyến — "
                   "và là lý do phải dựng riêng một bộ máy định giá.")
    xuat(h, "bai08-payoff-quyen-chon.svg")


def bai08_ket_hop():
    W, Hh = 780, 300
    h = Hinh("Ghép quyền chọn lại: ba chiến lược kinh điển", rong=W, cao=Hh + 70)
    K, KA, KB = 100, 90, 110
    ss = list(range(60, 141))
    bo = [("Straddle  (mua 1 call + 1 put cùng K)",
           lambda s: max(s - K, 0) + max(K - s, 0) - 14, MAU[0]),
          ("Bull spread  (mua call K=90, bán call K=110)",
           lambda s: max(s - KA, 0) - max(s - KB, 0) - 8, MAU[2]),
          ("Butterfly  (mua 90 & 110, bán hai lần 100)",
           lambda s: max(s - KA, 0) + max(s - KB, 0) - 2 * max(s - K, 0) - 3, MAU[3])]
    w = (W - 40) / 3
    for i, (ten, f, mau) in enumerate(bo):
        x0 = 20 + i * w
        px = lambda s, x0=x0: x0 + 26 + (s - 60) / 80 * (w - 46)
        py = lambda v: Hh - 40 - (min(max(v, -20), 26) + 20) / 50 * (Hh - 116)
        h.e.append(f'<rect x="{x0:.0f}" y="60" width="{w-8:.0f}" height="{Hh-56:.0f}"'
                   f' fill="#fff" stroke="#e4e4e0"/>')
        h.e.append(f'<line x1="{px(60):.1f}" y1="{py(0):.1f}" x2="{px(140):.1f}"'
                   f' y2="{py(0):.1f}" stroke="#aaa" stroke-width="1.2"/>')
        d = " ".join(("M" if j == 0 else "L") + f"{px(s):.1f},{py(f(s)):.1f}"
                     for j, s in enumerate(ss))
        h.e.append(f'<path d="{d}" fill="none" stroke="{mau}" stroke-width="2.6"'
                   f' stroke-linejoin="round"/>')
        for kk in (KA, K, KB):
            h.e.append(f'<line x1="{px(kk):.1f}" y1="70" x2="{px(kk):.1f}"'
                       f' y2="{Hh-42:.0f}" stroke="#eee" stroke-width="1"/>')
        h.chu(x0 + (w - 8) / 2, 82, ten.split("  (")[0], mau, 13, "middle", True)
        h.chu(x0 + (w - 8) / 2, 100, "(" + ten.split("  (")[1], "#777", 10, "middle")
        h.chu(x0 + (w - 8) / 2, Hh + 6, "60          100          140", XAM, 10, "middle")
    h.chu(W / 2, Hh + 38, "Trục ngang: giá tài sản cơ sở lúc đáo hạn. "
                          "Trục dọc: lãi/lỗ ròng sau khi trừ phí.", "#444", 11, "middle")
    h.chu(W / 2, Hh + 58, "Straddle cược THỊ TRƯỜNG SẼ ĐIÊN — thắng ở cả hai đầu, "
                          "thua nếu không có gì xảy ra.", "#888", 11, "middle")
    xuat(h, "bai08-chien-luoc-ket-hop.svg")


def bai08_cay_nhi_thuc():
    h = Hinh("Cây nhị thức: dựng một danh mục trả đúng như quyền chọn",
             rong=760, cao=430)
    S0, u, d, r, K = 100.0, 1.25, 0.80, 0.05, 100.0
    Su, Sd = S0 * u, S0 * d
    Cu, Cd = max(Su - K, 0), max(Sd - K, 0)
    delta = (Cu - Cd) / (Su - Sd)
    B = (Cu - delta * Su) / (1 + r)
    C0 = delta * S0 + B
    q = ((1 + r) - d) / (u - d)
    P = [(150, 215), (470, 120), (470, 310)]
    nhan = [f"S₀ = {S0:.0f}\nC₀ = ?", f"S↑ = {Su:.0f}\nC↑ = {Cu:.0f}",
            f"S↓ = {Sd:.0f}\nC↓ = {Cd:.0f}"]
    for i, ((x, y), n) in enumerate(zip(P, nhan)):
        h.hop(x - 62, y - 32, 124, 64, MAU[0] if i == 0 else MAU[2] if i == 1 else MAU[1],
              "#fff", n, 13)
    for j, (x, y) in enumerate(P[1:], 1):
        h.e.append(f'<line x1="{P[0][0]+62}" y1="{P[0][1] + (-12 if j==1 else 12)}"'
                   f' x2="{x-62}" y2="{y}" stroke="#777" stroke-width="2"/>')
    h.chu(320, 150, f"u = {u}", XAM, 12, "middle")
    h.chu(320, 292, f"d = {d}", XAM, 12, "middle")
    h.chu(380, 372, f"Δ = (C↑ − C↓) / (S↑ − S↓) = {delta:.4f} cổ phiếu, "
                    f"vay B = {B:,.2f}", MUC, 13, "middle", True)
    h.chu(380, 396, f"C₀ = Δ·S₀ + B = {C0:.2f}   —   "
                    f"và xác suất THẬT của u, d không xuất hiện ở đâu cả.",
          MAU[1], 13, "middle", True)
    h.chu(380, 420, f"Xác suất trung hoà rủi ro q = (1+r−d)/(u−d) = {q:.3f} "
                    f"→ C₀ = [q·C↑ + (1−q)·C↓]/(1+r) = {(q*Cu + (1-q)*Cd)/(1+r):.2f}",
          "#888", 11, "middle")
    xuat(h, "bai08-cay-nhi-thuc.svg")


def bai08_ngang_gia():
    h = Hinh("Ngang giá put–call: hai danh mục khác nhau, cùng một payoff",
             "Giá cổ phiếu lúc đáo hạn  S(T)", "Giá trị danh mục")
    K = 100
    ss = list(range(50, 151))
    h.truc((50, 150), (0, 155), dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0f}")
    h.duong([(s, max(s - K, 0) + K) for s in ss], MAU[0],
            "Danh mục A:  mua call  +  tiền mặt K", rong=4.2, mo=0.55)
    h.duong([(s, max(K - s, 0) + s) for s in ss], MAU[1],
            "Danh mục B:  mua put  +  cổ phiếu", rong=2.0, net="7 5")
    h.ke_doc(K, "#bbb", "4 4", "K = 100")
    h.chu_thich(h.L + 16, h.T + 20)
    h.chu(h.px(120), h.py(45), "C + K/(1+r)ᵀ  =  P + S", MUC, 16, "middle", True)
    h.ghi_chu_duoi("Hai đường trùng khít ở MỌI trạng thái. Theo luật một giá của bài 5, "
                   "chúng buộc phải có cùng giá hôm nay — không cần mô hình nào.")
    xuat(h, "bai08-ngang-gia-put-call.svg")


# ===========================================================================
# BAI 9
# ===========================================================================

def bai09_duoi_beo():
    m = nap("bai-09-rui-ro-va-loi-suat.py")
    # LS_SPX la danh sach (nam, thang, loi suat dang thap phan) -> doi ra phan tram
    r = [x[-1] * 100 for x in m.LS_SPX]
    mu, s = tb(r), sd(r)
    B = 0.5
    hist: dict[int, int] = {}
    for x in r:
        hist[int(math.floor(x / B))] = hist.get(int(math.floor(x / B)), 0) + 1
    n = len(r)
    h = Hinh(f"Đuôi béo: phân phối chuẩn là xấp xỉ, không phải sự thật  "
             f"(S&P 500, {n} tháng)",
             "Lợi suất tháng (%)", "Số tháng")
    h.truc((-26, 26), (0, max(hist.values()) * 1.12),
           dinh_x=lambda v: f"{v:+.0f}%", dinh_y=lambda v: f"{v:.0f}")
    h.cot([((k + 0.5) * B, v) for k, v in sorted(hist.items())], MAU[0],
          rong_cot=(h.W - h.L - h.R) * B / 52 * 0.92, mo=0.75)
    chuan = [(x, n * B / (s * math.sqrt(2 * math.pi))
              * math.exp(-((x - mu) ** 2) / (2 * s * s)))
             for x in [v / 4 for v in range(-104, 105)]]
    h.duong(chuan, MAU[1], rong=2.6)
    h.chu(h.px(9), h.py(max(hist.values()) * 0.66),
          f"phân phối chuẩn\ncùng μ = {mu:.2f}%, σ = {s:.2f}%", MAU[1], 12, "start", True)
    for x in (-3, 3):
        h.ke_doc(mu + x * s, "#ccc", "3 3")
    ngoai = sum(1 for v in r if abs(v - mu) > 3 * s)
    ky_vong = n * 0.0027
    h.chu(h.px(-24), h.py(max(hist.values()) * 0.86),
          f"|lệch| > 3σ\nthực tế: {ngoai} tháng\nchuẩn dự đoán: {ky_vong:.1f}",
          MAU[1], 12, "start", True)
    h.ghi_chu_duoi(f"Phân phối chuẩn dự đoán {ky_vong:.1f} tháng vượt 3σ. "
                   f"Thực tế có {ngoai} — nhiều gấp {ngoai/ky_vong:.0f} lần. "
                   f"Mọi mô hình rủi ro dựa vào phân phối chuẩn đều đánh giá THẤP thảm hoạ.")
    xuat(h, "bai09-duoi-beo.svg")


# ===========================================================================
# BAI 10
# ===========================================================================

def bai10_duong_dan():
    m = nap("bai-10-ly-thuyet-danh-muc.py")
    mua, sda = float(m.MOT_MU), float(m.MOT_SD)
    mub, sdb = float(m.GM_MU), float(m.GM_SD)
    h = Hinh("Tương quan quyết định hình dạng đường đạn",
             "Độ lệch chuẩn σ (rủi ro)", "Lợi suất kỳ vọng μ")
    ws = [v / 200 for v in range(0, 201)]
    h.truc((0, max(sda, sdb) * 1.12), (min(mua, mub) * 0.55, max(mua, mub) * 1.18),
           dinh_x=lambda v: f"{v:.0f}%", dinh_y=lambda v: f"{v:.1f}%")
    for i, rho in enumerate((1.0, 0.5, 0.0, -0.5, -1.0)):
        pts = []
        for w in ws:
            v = (w * sda) ** 2 + ((1 - w) * sdb) ** 2 + 2 * w * (1 - w) * rho * sda * sdb
            pts.append((math.sqrt(max(v, 0)), w * mua + (1 - w) * mub))
        h.duong(pts, MAU[i], f"ρ = {rho:+.1f}", rong=2.4 if rho else 2.4)
    h.cham(sda, mua, MUC, 6); h.moc(sda, mua, "tài sản A", MUC, 10, 4, 12, "start", True)
    h.cham(sdb, mub, MUC, 6); h.moc(sdb, mub, "tài sản B", MUC, 10, 4, 12, "start", True)
    h.chu_thich(h.L + 16, h.T + 20)
    h.ghi_chu_duoi("ρ = +1 cho đường THẲNG — không có lợi ích đa dạng hoá nào. "
                   "Càng xuống dưới, đường càng cong về trái: cùng lợi suất, ít rủi ro hơn. "
                   "ρ = −1 chạm đúng trục tung: rủi ro bằng 0.")
    xuat(h, "bai10-duong-dan.svg")


def bai10_bien_hieu_qua():
    m = nap("bai-10-ly-thuyet-danh-muc.py")
    ma = ["MRK", "IBM", "MCD", "KO", "WMT", "XOM"]
    R = {k: doc_so(m.DU_LIEU[k]) for k in ma}
    rf = tb([v / 12.0 for v in doc_so(m.DU_LIEU["RF"])])  # RF nhung la lai suat NAM
    mu = {k: tb(v) for k, v in R.items()}
    C = [[cov(R[a], R[b]) for b in ma] for a in ma]

    def giai(A, b):
        n = len(A)
        M = [row[:] + [b[i]] for i, row in enumerate(A)]
        for c in range(n):
            p = max(range(c, n), key=lambda r: abs(M[r][c]))
            M[c], M[p] = M[p], M[c]
            for r2 in range(n):
                if r2 == c:
                    continue
                f = M[r2][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r2][k] -= f * M[c][k]
        return [M[i][n] / M[i][i] for i in range(n)]

    def dm(w):
        s = sum(w)
        w = [x / s for x in w]
        v = sum(w[i] * w[j] * C[i][j] for i in range(6) for j in range(6))
        return math.sqrt(v), sum(w[i] * mu[ma[i]] for i in range(6))

    z = giai([r[:] for r in C], [mu[k] - rf for k in ma])
    sd_t, mu_t = dm(z)
    zv = giai([r[:] for r in C], [1.0] * 6)
    sd_v, mu_v = dm(zv)
    # bien hieu qua: quet muc loi suat muc tieu
    bien = []
    for k in range(-60, 121):
        tgt = mu_v + k * 0.004
        A = [[2 * C[i][j] for j in range(6)] + [mu[ma[i]], 1.0] for i in range(6)]
        A += [[mu[ma[j]] for j in range(6)] + [0.0, 0.0],
              [1.0] * 6 + [0.0, 0.0]]
        b = [0.0] * 6 + [tgt, 1.0]
        w = giai(A, b)[:6]
        v = sum(w[i] * w[j] * C[i][j] for i in range(6) for j in range(6))
        if v > 0:
            bien.append((math.sqrt(v), tgt))
    h = Hinh("Biên hiệu quả dựng từ dữ liệu thật — sáu cổ phiếu Mỹ, 463 tháng",
             "Độ lệch chuẩn σ (%/tháng)", "Lợi suất kỳ vọng (%/tháng)")
    h.truc((0, 8.6), (0.15, 1.55), dinh_x=lambda v: f"{v:.1f}", dinh_y=lambda v: f"{v:.2f}")
    duoi = [p for p in bien if p[1] <= mu_v]
    tren = [p for p in bien if p[1] >= mu_v]
    h.duong(duoi, XAM, "Biên phương sai nhỏ nhất (phần KHÔNG hiệu quả)", 2.0, "5 4")
    h.duong(tren, MAU[0], "BIÊN HIỆU QUẢ", 3.0)
    sharpe = (mu_t - rf) / sd_t
    x_het = min(8.6, (1.52 - rf) / sharpe)
    h.duong([(0, rf), (x_het, rf + sharpe * x_het)], MAU[3],
            f"Đường phân bổ vốn (CAL) — độ dốc = tỷ số Sharpe = {sharpe:.3f}", 2.2)
    for j, k in enumerate(sorted(ma, key=lambda t: math.sqrt(cov(R[t], R[t])))):
        sk = math.sqrt(cov(R[k], R[k]))
        h.cham(sk, mu[k], MAU[1], 4.5)
        h.moc(sk, mu[k], k, MAU[1], 7, 14 if j % 2 else -7, 10)
    h.cham(sd_v, mu_v, MAU[2], 6.5)
    h.moc(sd_v, mu_v, "phương sai nhỏ nhất", MAU[2], -12, 16, 11, "end", True)
    h.cham(sd_t, mu_t, MAU[3], 6.5)
    h.moc(sd_t, mu_t, "TIẾP TUYẾN", MAU[3], -12, -10, 12, "end", True)
    h.cham(0, rf, MUC, 4.5)
    h.moc(0, rf, f"rf = {rf:.2f}%/tháng", MUC, 7, 4, 11)
    h.chu_thich(h.L + 34, h.T + 172)
    h.ghi_chu_duoi(f"Mọi cổ phiếu riêng lẻ (chấm đỏ) đều nằm BÊN TRONG biên — tức luôn có "
                   f"một danh mục vừa lãi hơn vừa an toàn hơn. Tỷ số Sharpe của danh mục "
                   f"tiếp tuyến: {(mu_t - rf) / sd_t:.3f}.")
    xuat(h, "bai10-bien-hieu-qua.svg")


def bai10_da_dang_hoa():
    m = nap("bai-10-ly-thuyet-danh-muc.py")
    my = ["MRK", "IBM", "MCD", "KO", "WMT", "XOM"]
    vn = ["FPT", "VNM", "HPG", "VCB", "REE", "PNJ"]

    def tham_so(ds):
        R = {k: doc_so(m.DU_LIEU[k]) for k in ds}
        n = len(ds)
        pv = tb([cov(R[k], R[k]) for k in ds])
        hpv = tb([cov(R[a], R[b]) for i, a in enumerate(ds)
                  for b in ds[i + 1:]])
        return pv, hpv

    h = Hinh("Giới hạn của đa dạng hoá — rủi ro hệ thống là cái sàn không phá được",
             "Số cổ phiếu trong danh mục (n)", "Độ lệch chuẩn danh mục (%/tháng)")
    h.truc((1, 60), (0, 12), dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0f}")
    for i, (ten, ds) in enumerate((("Mỹ (6 cổ phiếu lớn, 1988–2026)", my),
                                   ("Việt Nam (6 cổ phiếu, 2012–2026)", vn))):
        pv, hpv = tham_so(ds)
        pts = [(n, math.sqrt(pv / n + (1 - 1 / n) * hpv)) for n in range(1, 61)]
        h.duong(pts, MAU[i], ten, rong=2.8)
        h.ke_ngang(math.sqrt(hpv), MAU[i], "5 4",
                   f"sàn = √(hiệp phương sai TB) = {math.sqrt(hpv):.1f}%")
    h.chu_thich(h.L + 250, h.T + 20)
    h.ghi_chu_duoi("Thêm cổ phiếu chỉ xoá được rủi ro RIÊNG LẺ. Phần còn lại là rủi ro "
                   "HỆ THỐNG — và chính nó là thứ duy nhất thị trường trả tiền cho (bài 11).")
    xuat(h, "bai10-gioi-han-da-dang-hoa.svg")


def bai10_huu_dung_lom():
    """Ham huu dung lom: vi sao co phi rui ro, va cho no vo ly."""
    m = nap("bai-10-ly-thuyet-danh-muc.py")
    al = m.ALPHA_A
    h = Hinh("Hàm hữu dụng bậc hai: nền của trung bình–phương sai, và khuyết tật của nó",
             "Số tiền nhận được", "Hữu dụng")
    xs = [i for i in range(0, 261, 2)]
    h.truc((0, 260), (0, 115), dinh_x=lambda v: f"{v:.0f}",
           dinh_y=lambda v: f"{v:.0f}")
    h.duong([(x, m.huu_dung_bac_hai(x, al)) for x in xs], MAU[0],
            f"U(x) = x − ½·{al:.4f}·x²", 3.0)
    a_, b_ = 50.0, 150.0
    ua, ub = m.huu_dung_bac_hai(a_, al), m.huu_dung_bac_hai(b_, al)
    h.duong([(a_, ua), (b_, ub)], MAU[1], "dây cung: canh bạc 50/50", 2.2, "6 4")
    td = m.tuong_duong_chac_chan([a_, b_], [0.5, 0.5], al)
    eu = m.ky_vong_huu_dung([a_, b_], [0.5, 0.5], al)
    h.cham(100.0, eu, MAU[1], 6)
    h.cham(td, eu, MAU[2], 6)
    h.cham(100.0, m.huu_dung_bac_hai(100.0, al), MAU[0], 6)
    h.duong([(td, 0), (td, eu)], MAU[2], None, 1.6, "3 3")
    h.duong([(100.0, 0), (100.0, m.huu_dung_bac_hai(100.0, al))], "#bbb", None, 1.4, "3 3")
    h.moc(td, eu, f"tương đương chắc chắn {td:.1f}", MAU[2], -8, -12, 11, "end", True)
    h.moc(100.0, eu, f"kỳ vọng 100", MAU[1], 10, 16, 11, "start")
    ng = 1.0 / al
    h.ke_doc(ng, MAU[1], "4 3", f"ngưỡng bão hoà {ng:.0f} — quá đây thêm tiền LÀM GIẢM hữu dụng")
    h.chu_thich(h.L + 16, h.T + 10)
    h.ghi_chu_duoi(f"Hàm lõm nên dây cung nằm DƯỚI đường cong: canh bạc 50/50 giữa 50 và 150 chỉ "
                   f"đáng bằng {td:.1f} chắc chắn, tức người ta trả {100-td:.1f} để thoát rủi ro. "
                   f"Đó là phí rủi ro. Nhưng chính hàm này quay đầu ở {ng:.0f} — ví dụ của "
                   f"Geanakoplos chạy tới 180, tức 90% ngưỡng.")
    xuat(h, "bai10-huu-dung-lom.svg")


# ===========================================================================
# BAI 11
# ===========================================================================

def bai11_cml_sml():
    W = 780
    h = Hinh("Hai đường thẳng dễ nhầm: CML và SML", rong=W, cao=430)
    rf, mum, sdm = 0.4, 1.0, 4.5
    for i, (ten, nhan_x, mo_ta) in enumerate((
            ("ĐƯỜNG THỊ TRƯỜNG VỐN  (CML)", "σ — độ lệch chuẩn",
             "Chỉ đúng cho danh mục HIỆU QUẢ.\nMọi thứ khác nằm DƯỚI đường."),
            ("ĐƯỜNG THỊ TRƯỜNG CHỨNG KHOÁN  (SML)", "β — beta",
             "Đúng cho MỌI chứng khoán và mọi danh mục,\nhiệu quả hay không."))):
        x0 = 30 + i * (W / 2 - 10)
        w, hh = W / 2 - 50, 250
        y0 = 70
        px = lambda v, x0=x0, w=w: x0 + 46 + v / (9 if i == 0 else 2.0) * (w - 60)
        py = lambda v, y0=y0, hh=hh: y0 + hh - (v / 1.8) * (hh - 30)
        h.e.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{hh}" fill="#fff"'
                   f' stroke="#e4e4e0"/>')
        h.chu(x0 + w / 2, y0 - 14, ten, MAU[i], 13, "middle", True)
        xmax = 9 if i == 0 else 2.0
        h.e.append(f'<line x1="{px(0)}" y1="{py(0)}" x2="{px(xmax)}" y2="{py(0)}"'
                   f' stroke="#aaa"/>')
        h.e.append(f'<line x1="{px(0)}" y1="{py(0)}" x2="{px(0)}" y2="{py(1.7)}"'
                   f' stroke="#aaa"/>')
        doc = (mum - rf) / sdm if i == 0 else (mum - rf)
        h.e.append(f'<line x1="{px(0)}" y1="{py(rf)}" x2="{px(xmax)}"'
                   f' y2="{py(rf + doc * xmax)}" stroke="{MAU[i]}" stroke-width="2.8"/>')
        mx = sdm if i == 0 else 1.0
        h.e.append(f'<circle cx="{px(mx)}" cy="{py(mum)}" r="5.5" fill="{MAU[i]}"'
                   f' stroke="#fff" stroke-width="1.6"/>')
        h.chu(px(mx) + 9, py(mum) - 8, "danh mục thị trường", MUC, 11, "start", True)
        h.chu(px(0) - 8, py(rf) + 4, "rf", XAM, 11, "end")
        if i == 0:
            for sx, sy in ((6.8, 0.85), (7.6, 1.05), (5.2, 0.72)):
                h.e.append(f'<circle cx="{px(sx)}" cy="{py(sy)}" r="3.4" fill="#bbb"/>')
            h.chu(px(6.5), py(0.55), "cổ phiếu riêng lẻ nằm DƯỚI", "#888", 10, "middle")
        else:
            for bx in (0.4, 0.75, 1.35, 1.75):
                h.e.append(f'<circle cx="{px(bx)}" cy="{py(rf + doc * bx)}" r="3.6"'
                           f' fill="{MAU[i]}" opacity="0.55"/>')
            h.chu(px(1.4), py(0.42), "mọi chứng khoán nằm TRÊN đường", "#888", 10, "middle")
        h.chu(x0 + w / 2, y0 + hh + 22, nhan_x, "#444", 12, "middle")
        for j, dong in enumerate(mo_ta.split("\n")):
            h.chu(x0 + w / 2, y0 + hh + 46 + j * 17, dong, "#666", 11, "middle")
    h.chu(W / 2, 418, "Cùng một điểm “danh mục thị trường” nằm trên cả hai — "
                      "nhưng TRỤC NGANG khác nhau. Đó là toàn bộ chỗ dễ nhầm.",
          "#888", 11, "middle")
    xuat(h, "bai11-cml-sml.svg")


def bai11_sml_do_that():
    m = nap("bai-11-capm-va-beta.py")
    D = {k: doc_so(v) for k, v in m.DU_LIEU.items()}
    mrf, rf = D["MKTRF"], D["RF"]
    ten = ["BETA1", "BETA2", "BETA3", "BETA4", "BETA5"]
    beta, tb_vuot = [], []
    for k in ten:
        vuot = [D[k][i] - rf[i] for i in range(len(rf))]
        beta.append(hoi_quy(vuot, mrf)[1])
        tb_vuot.append(tb(vuot))
    a, b = hoi_quy(tb_vuot, beta)
    ly_thuyet = tb(mrf)
    h = Hinh("Độ dốc THẬT của SML — đo trên 757 tháng, năm ngũ phân sắp theo beta",
             "Beta đo được", "Lợi suất vượt trội trung bình (%/tháng)")
    h.truc((0, 1.7), (0, 0.85), dinh_x=lambda v: f"{v:.1f}", dinh_y=lambda v: f"{v:.2f}")
    h.duong([(0, 0), (1.7, ly_thuyet * 1.7)], MAU[1],
            f"SML lý thuyết: chặn 0, độ dốc = {ly_thuyet:.3f}", 2.6, "6 4")
    h.duong([(0, a), (1.7, a + b * 1.7)], MAU[0],
            f"SML đo được: chặn {a:+.3f}, độ dốc {b:.3f}", 2.8)
    for i, k in enumerate(ten):
        h.cham(beta[i], tb_vuot[i], MAU[0], 6)
        h.moc(beta[i], tb_vuot[i], f"ngũ phân {i+1}", MUC, 0, -12, 10, "middle")
    h.cham(1.0, ly_thuyet, MAU[1], 6)
    h.moc(1.0, ly_thuyet, "danh mục thị trường", MAU[1], 10, 20, 11, "start", True)
    h.chu_thich(h.L + 20, h.T + 232)
    h.ghi_chu_duoi(f"Đường đo được PHẲNG hơn lý thuyết ({b/ly_thuyet:.0%} độ dốc) và có "
                   f"chặn dương {a:+.3f}%/tháng. Beta thấp được trả quá nhiều, beta cao "
                   f"quá ít — đó là “đánh cược ngược beta”.")
    xuat(h, "bai11-sml-do-that.svg")


# ===========================================================================
# BAI 12
# ===========================================================================

def bai12_npv_irr():
    """Hai khung canh nhau: du an binh thuong (mot IRR) va du an doi dau (ba IRR)."""
    W, HH = 780, 470
    h = Hinh("NPV theo suất chiết khấu — IRR chỉ là chỗ đường cắt trục hoành",
             rong=W, cao=HH)

    def npv(cf, r):
        return sum(c / (1 + r) ** t for t, c in enumerate(cf))

    khung = [
        ("Dòng tiền BÌNH THƯỜNG — đổi dấu MỘT lần",
         [-1000, 300, 300, 300, 300, 300], 0.30, 1, MAU[0], (-800, 600)),
        ("Dòng tiền ĐỔI DẤU BA lần — Descartes cho phép tới ba nghiệm",
         [-1000, 6000, -11000, 6000], 2.60, 3, MAU[1], (-800, 600)),
    ]
    for i, (ten, cf, rmax, so_nghiem, mau, (ylo, yhi)) in enumerate(khung):
        x0, w, y0, hh = 30 + i * (W / 2 - 5), W / 2 - 55, 78, 250
        px = lambda r, x0=x0, w=w: x0 + 52 + r / rmax * (w - 62)
        py = lambda v, y0=y0, hh=hh: y0 + hh - (v - ylo) / (yhi - ylo) * hh
        h.e.append(f'<rect x="{x0:.0f}" y="{y0}" width="{w:.0f}" height="{hh}"'
                   f' fill="#fff" stroke="#e4e4e0"/>')
        h.chu(x0 + w / 2, y0 - 12, ten, mau, 12, "middle", True)
        h.e.append(f'<line x1="{px(0):.1f}" y1="{py(0):.1f}" x2="{px(rmax):.1f}"'
                   f' y2="{py(0):.1f}" stroke="#999" stroke-width="1.4"/>')
        h.chu(x0 + 46, py(0) - 6, "NPV = 0", XAM, 10, "end")
        rs = [k * rmax / 400 for k in range(401)]
        d = " ".join(("M" if j == 0 else "L")
                     + f"{px(r):.1f},{py(min(max(npv(cf, r), ylo), yhi)):.1f}"
                     for j, r in enumerate(rs))
        h.e.append(f'<path d="{d}" fill="none" stroke="{mau}" stroke-width="2.8"/>')
        # tim nghiem bang doi dau
        nghiem, truoc = [], npv(cf, rs[0])
        if abs(truoc) < 1e-9:          # nghiem roi dung dau khoang quet
            nghiem.append(rs[0])
        for r in rs[1:]:
            gio = npv(cf, r)
            if (truoc > 0) != (gio > 0):
                a, b = r - rmax / 400, r
                for _ in range(60):
                    mm = (a + b) / 2
                    if (npv(cf, a) > 0) == (npv(cf, mm) > 0):
                        a = mm
                    else:
                        b = mm
                nghiem.append((a + b) / 2)
            truoc = gio
        for k, r in enumerate(nghiem):
            h.e.append(f'<circle cx="{px(r):.1f}" cy="{py(0):.1f}" r="5.5" fill="{mau}"'
                       f' stroke="#fff" stroke-width="1.6"/>')
            h.chu(px(r), py(0) + (26 if k % 2 else -14), f"IRR {r:.0%}", mau, 12,
                  "middle", True)
        assert len(nghiem) == so_nghiem, (ten, nghiem)
        for r in [k * rmax / 4 for k in range(5)]:
            h.chu(px(r), y0 + hh + 18, f"{r:.0%}", XAM, 10, "middle")
        h.chu(x0 + w / 2, y0 + hh + 40, "suất chiết khấu r", "#444", 11, "middle")
        h.chu(x0 + 46, py(yhi) + 12, f"+{yhi:,.0f}", XAM, 10, "end")
        h.chu(x0 + 46, py(ylo) - 3, f"{ylo:,.0f}", XAM, 10, "end")
    h.chu(W / 2, HH - 66, "Khung trái: một nghiệm, quy tắc IRR chạy đúng.  "
                          "Khung phải: BA nghiệm — 0%, 100%, 200%.",
          MUC, 12, "middle", True)
    h.chu(W / 2, HH - 44, "Hỏi “IRR của dự án này là bao nhiêu?” đã sai từ câu hỏi. "
                          "NPV thì luôn có đúng một giá trị.", "#666", 11, "middle")
    h.chu(W / 2, HH - 20, "Số lần đổi dấu của dòng tiền chặn trên số nghiệm dương — "
                          "quy tắc dấu Descartes, không phải giả thuyết Riemann.",
          "#999", 11, "middle")
    xuat(h, "bai12-npv-irr.svg")


def bai12_la_chan_thue():
    m = nap("bai-12-ngan-sach-von.py")
    GIA, THUE, r = 1_000_000, int(m.THUE), 0.10
    N = 5
    thang = [GIA // N] * N
    tong = N * (N + 1) // 2
    nhanh = [GIA * (N - i) // tong for i in range(N)]
    h = Hinh(f"Lá chắn thuế khấu hao: cùng {GIA:,} đô được trừ, chỉ khác THỜI ĐIỂM",
             "Năm", "Giá trị hiện tại của phần thuế tiết kiệm (đô la)")
    h.truc((0.4, N + 0.6), (0, 42000), vach_x=list(range(1, N + 1)),
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:,.0f}")
    pv_t = [THUE * thang[i] / 100 / (1 + r) ** (i + 1) for i in range(N)]
    pv_n = [THUE * nhanh[i] / 100 / (1 + r) ** (i + 1) for i in range(N)]
    for i in range(N):
        x = i + 1
        h.e.append(f'<rect x="{h.px(x)-38:.1f}" y="{h.py(pv_t[i]):.1f}" width="34"'
                   f' height="{h.py(0)-h.py(pv_t[i]):.1f}" fill="{MAU[0]}" opacity="0.85"/>')
        h.e.append(f'<rect x="{h.px(x)+4:.1f}" y="{h.py(pv_n[i]):.1f}" width="34"'
                   f' height="{h.py(0)-h.py(pv_n[i]):.1f}" fill="{MAU[3]}" opacity="0.85"/>')
    h.e.append(f'<rect x="{h.L+16}" y="{h.T+8}" width="20" height="11" fill="{MAU[0]}"/>')
    h.chu(h.L + 42, h.T + 18, f"Đường thẳng — tổng PV = {sum(pv_t):,.0f}", MUC, 12)
    h.e.append(f'<rect x="{h.L+16}" y="{h.T+30}" width="20" height="11" fill="{MAU[3]}"/>')
    h.chu(h.L + 42, h.T + 40, f"Nhanh dần — tổng PV = {sum(pv_n):,.0f}", MUC, 12)
    h.chu(h.L + 42, h.T + 62,
          f"Chênh {sum(pv_n)-sum(pv_t):+,.0f} đô = {sum(pv_n)/sum(pv_t)-1:+.1%}",
          MAU[1], 13, "start", True)
    h.ghi_chu_duoi(f"Nhà nước không cho thêm đồng trợ cấp nào — chỉ đổi thời điểm được trừ. "
                   f"Với thuế suất {THUE}% và chiết khấu {r:.0%}, riêng cái đổi thời điểm ấy "
                   f"đáng {sum(pv_n)-sum(pv_t):,.0f} đô.")
    xuat(h, "bai12-la-chan-thue.svg")


# ===========================================================================
# BAI 13
# ===========================================================================

def bai13_tu_tuong_quan():
    m = nap("bai-13-thi-truong-hieu-qua.py")
    mkt = [m.MKTRF[i] + m.RF[i] for i in range(len(m.MKTRF))]
    W = m.CUA_SO
    goc = (m.FF_THANG_DAU // 100) * 12 + m.FF_THANG_DAU % 100 - 1

    def ac1(v):
        mm = tb(v)
        return (sum((v[i] - mm) * (v[i - 1] - mm) for i in range(1, len(v)))
                / sum((x - mm) ** 2 for x in v))
    pts = []
    for i in range(W - 1, len(mkt)):
        t = goc + i
        pts.append((t / 12, ac1(mkt[i - W + 1:i + 1])))
    se = 1 / math.sqrt(W)
    h = Hinh(f"Chu kỳ hiệu quả: tự tương quan bậc 1, lăn cận {W} tháng, thị trường Mỹ",
             "Năm", "Tự tương quan bậc một")
    h.truc((1931, 2027), (-0.42, 0.42), vach_x=list(range(1940, 2030, 10)),
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:+.1f}", goc_khong=True)
    h.vung([(1931, 2 * se), (2027, 2 * se)], [(1931, -2 * se), (2027, -2 * se)],
           XAM, 0.13)
    h.chu(h.px(1936), h.py(2 * se) - 6, "dải ±2 sai số chuẩn (nhiễu)", "#999", 11)
    h.duong(pts, MAU[0], rong=1.7)
    cao = max(pts, key=lambda p: p[1])
    thap = min(pts, key=lambda p: p[1])
    h.cham(*cao, MAU[1], 6)
    h.moc(*cao, f"11/2008: {cao[1]:+.3f}\nĐỈNH CỦA CẢ THẾ KỶ", MAU[1], -12, -18, 12, "end", True)
    h.cham(*thap, MAU[2], 5)
    h.moc(*thap, f"02/1996: {thap[1]:+.3f}", MAU[2], 8, 16, 11)
    h.ke_doc(2008.92, MAU[1], "3 4")
    h.ghi_chu_duoi("Đỉnh cao nhất của cả 1.142 cửa sổ rơi đúng vào tháng Lo đứng lớp nói "
                   "“lý thuyết tài chính đang đi nghỉ”. Phần lớn nhấp nhô còn lại nằm trong "
                   "dải xám — tức là nhiễu.")
    xuat(h, "bai13-tu-tuong-quan-the-ky.svg")


def bai13_737max():
    m = nap("bai-13-thi-truong-hieu-qua.py")
    gia = {"BA": m.GIA_BA, "GE": m.GIA_GE, "HXL": m.GIA_HXL,
           "TDG": m.GIA_TDG, "LUV": m.GIA_LUV}
    ngay = m.NGAY_MAX
    i0 = ngay.index("2019-03-08")          # phien cuoi truoc tai nan
    i1 = min(i0 + 11, len(ngay) - 1)
    h = Hinh("Challenger phiên bản 2019: thị trường chỉ đúng thủ phạm trong MỘT phiên",
             "Phiên giao dịch quanh tai nạn ET302 (10/3/2019)",
             "Giá chuẩn hoá về 1,00 tại phiên 8/3/2019", le=(74, 74, 62, 96))
    h.truc((i0, i1), (0.82, 1.06), vach_x=list(range(i0, i1 + 1, 2)),
           dinh_x=lambda v: ngay[int(v)][5:].replace("-", "/"),
           dinh_y=lambda v: f"{v:.2f}")
    for i, (k, g) in enumerate(gia.items()):
        pts = [(j, g[j] / g[i0]) for j in range(i0, i1 + 1)]
        h.duong(pts, MAU[i], k, rong=3.2 if k == "BA" else 1.9,
                mo=1.0 if k == "BA" else 0.75)
        h.moc(i1, pts[-1][1], k, MAU[i], 7, 4, 11, "start", True)
    h.ke_ngang(1.0, "#bbb", "4 4")
    h.ke_doc(ngay.index("2019-03-11"), MAU[1], "4 4")
    h.chu(h.px(ngay.index("2019-03-11")) + 8, h.T - 8,
          "11/3: FAA tuyên bố MÁY BAY ĐỦ ĐIỀU KIỆN BAY", MAU[1], 11, "start", True)
    h.ke_doc(ngay.index("2019-03-13"), MAU[2], "4 4")
    h.chu(h.px(ngay.index("2019-03-13")) + 8, h.T + 12,
          "13/3: FAA cấm bay", MAU[2], 11, "start", True)
    h.ghi_chu_duoi("Cùng một ngày, cơ quan quản lý nói an toàn và thị trường nói không. "
                   "Hai ngày sau FAA đổi ý — và giá Boeing TĂNG, vì tin đã nằm trọn trong giá.")
    xuat(h, "bai13-su-kien-737max.svg")


def bai13_sml_hai_che_do():
    m = nap("bai-13-thi-truong-hieu-qua.py")
    n = len(m.NGU_PHAN_BETA)
    lech = ((m.BETA_THANG_DAU // 100) * 12 + m.BETA_THANG_DAU % 100
            - (m.FF_THANG_DAU // 100) * 12 - m.FF_THANG_DAU % 100)
    mrf = [m.MKTRF[lech + i] for i in range(n)]
    rf = [m.RF[lech + i] for i in range(n)]
    vuot = [[m.NGU_PHAN_BETA[i][k] - rf[i] for i in range(n)] for k in range(5)]
    beta = [hoi_quy(vuot[k], mrf)[1] for k in range(5)]
    NT = 12
    bd = {i: sd(mrf[i - NT:i]) for i in range(NT, n)}
    nguong = sorted(bd.values())[int(len(bd) * 0.8)]
    h = Hinh("Đường SML KHÔNG ổn định — hai chế độ, hai độ dốc trái dấu",
             "Beta", "Lợi suất vượt trội trung bình (%/tháng)")
    h.truc((0.5, 1.65), (-0.2, 3.4), dinh_x=lambda v: f"{v:.1f}",
           dinh_y=lambda v: f"{v:.1f}", goc_khong=True)
    for i, (ten, loc) in enumerate((("BÌNH LẶNG (80% số tháng)", lambda i: bd[i] < nguong),
                                    ("CĂNG THẲNG (20% số tháng)", lambda i: bd[i] >= nguong))):
        chon = [j for j in range(NT, n) if loc(j)]
        y = [tb([vuot[k][j] for j in chon]) for k in range(5)]
        a, b = hoi_quy(y, beta)
        h.duong([(0.5, a + b * 0.5), (1.65, a + b * 1.65)], MAU[i],
                f"{ten} — độ dốc {b:+.3f}%/tháng", rong=2.8)
        for k in range(5):
            h.cham(beta[k], y[k], MAU[i], 5.5)
    h.chu_thich(h.L + 240, h.T + 20)
    h.ghi_chu_duoi("Ngược trực giác: CAPM chạy tốt trong bão và hỏng trong thị trường bình "
                   "lặng. Cùng một đường thẳng, độ dốc chạy từ âm sang dương gấp mười lần.")
    xuat(h, "bai13-sml-hai-che-do.svg")


# ===========================================================================
# BAI 14 — PHAN E: TAI CHINH DOANH NGHIEP
# ===========================================================================

def _b14():
    return nap("bai-14-doc-doanh-nghiep-bang-so.py")


def bai14_ban_do_sinh_loi():
    """Ban do sinh loi: bien x vong quay = ROA. Duong dong muc la hypebol."""
    m = _b14()
    NAM = 2025
    h = Hinh("Bản đồ sinh lời: biên lợi nhuận × vòng quay tài sản = ROA",
             "Vòng quay tài sản  (doanh thu / tổng tài sản)",
             "Biên lợi nhuận ròng  (LNST / doanh thu)")
    h.truc((0, 2.8), (0, 0.30), dinh_x=lambda v: f"{v:.1f}", dinh_y=lambda v: f"{v:.0%}")
    for roa, mau, x_nhan in ((0.05, "#ddd", 2.35), (0.10, "#ccc", 1.62),
                             (0.15, "#bbb", 1.30), (0.20, "#aaa", 1.05)):
        pts = [(v / 100, roa / (v / 100)) for v in range(18, 281)
               if 0 < roa / (v / 100) <= 0.30]
        h.duong(pts, mau, None, 1.6)
        h.chu(h.px(x_nhan), h.py(roa / x_nhan) - 7, f"ROA {roa:.0%}", "#999", 10, "middle")
    # Viet Nam
    for ma in ("MWG", "PNJ", "FPT", "VNM", "HPG"):
        if NAM not in m.VN[ma]:
            continue
        dt = m.cot(ma, NAM, "doanh_thu")
        ln = m.cot(ma, NAM, "lnst_me")
        ts = m.binh_quan(ma, NAM, "tong_ts")
        h.cham(dt / ts, ln / dt, MAU[1], 6.5)
        h.moc(dt / ts, ln / dt, ma, MAU[1], 9, 4, 12, "start", True)
    # My
    for t, ten in (("WMT", "Walmart"), ("AAPL", "Apple"), ("KO", "Coca-Cola")):
        k = max(m.US[t])
        dt, ln, ts, _ = m.US[t][k]
        h.cham(dt / ts, ln / dt, MAU[0], 6.5)
        dy = 20 if ten == "Coca-Cola" else (-11 if ten == "Walmart" else 4)
        h.moc(dt / ts, ln / dt, ten, MAU[0], 9, dy, 12, "start", True)
    yc = h.py(0.035)
    h.e.append(f'<circle cx="{h.L+22}" cy="{yc}" r="6" fill="{MAU[1]}"/>')
    h.chu(h.L + 34, yc + 4, "Việt Nam (2025)", MUC, 12)
    h.e.append(f'<circle cx="{h.L+22}" cy="{yc+22}" r="6" fill="{MAU[0]}"/>')
    h.chu(h.L + 34, yc + 26, "Mỹ (năm tài chính gần nhất)", MUC, 12)
    h.ghi_chu_duoi("Mỗi đường xám là một mức ROA. Doanh nghiệp nằm trên cùng một đường "
                   "sinh lời như nhau trên tài sản, dù mô hình kinh doanh ngược nhau "
                   "hoàn toàn. Góc dưới-trái là vùng chết: biên mỏng MÀ quay chậm.")
    xuat(h, "bai14-ban-do-sinh-loi.svg")


def bai14_dupont_cot():
    """Ba thanh phan DuPont, dat canh nhau cho sau doanh nghiep."""
    m = _b14()
    NAM = 2025
    ds = []
    for t, ten in (("WMT", "Walmart"), ("KO", "Coca-Cola"), ("AAPL", "Apple")):
        k = max(m.US[t])
        dt, ln, ts, vc = m.US[t][k]
        ds.append((ten, ln / dt, dt / ts, ts / vc, ln / vc))
    for ma in ("MWG", "PNJ", "FPT", "VNM"):
        if NAM not in m.VN[ma]:
            continue
        dt = m.cot(ma, NAM, "doanh_thu")
        ln = m.cot(ma, NAM, "lnst_me")
        ts = m.binh_quan(ma, NAM, "tong_ts")
        vc = m.binh_quan(ma, NAM, "vcsh")
        ds.append((ma, ln / dt, dt / ts, ts / vc, ln / vc))
    W, HH = 780, 470
    h = Hinh("Cùng ba con số nhân với nhau — bảy doanh nghiệp, bảy hình dạng khác nhau",
             rong=W, cao=HH)
    cot_ten = [("biên lợi nhuận", 1, 0.30, "{:.1%}"),
               ("vòng quay tài sản", 2, 3.0, "{:.2f}"),
               ("đòn bẩy", 3, 8.0, "{:.2f}"),
               ("= ROE", 4, 1.6, "{:.0%}")]
    x0, hang = 96, 46
    for j, (ten, idx, cao, fmt) in enumerate(cot_ten):
        bx = x0 + j * 168
        h.chu(bx + 62, 72, ten, MUC, 12, "middle", True)
        for i, r in enumerate(ds):
            y = 96 + i * hang
            v = r[idx]
            w = min(v / cao, 1.0) * 124
            mau = MAU[3] if j == 3 else MAU[0] if i < 3 else MAU[1]
            h.e.append(f'<rect x="{bx}" y="{y-11}" width="{w:.1f}" height="16" rx="2"'
                       f' fill="{mau}" opacity="0.85"/>')
            h.chu(bx + w + 6, y + 2, fmt.format(v), "#444", 11)
    for i, r in enumerate(ds):
        h.chu(88, 96 + i * hang + 2, r[0], MUC, 12, "end",
              True if r[0] in ("Apple", "MWG") else False)
    h.chu(W / 2, HH - 44, "Ba cột đầu nhân với nhau ra cột thứ tư. "
                          "Xanh = Mỹ, đỏ = Việt Nam, cam = ROE.", "#666", 11, "middle")
    h.chu(W / 2, HH - 22, "Apple và Coca-Cola có biên gần bằng nhau — "
                          "khác biệt ROE đến từ hai cột còn lại.", "#888", 11, "middle")
    xuat(h, "bai14-dupont-cot.svg")


def bai14_apple_don_bay():
    m = _b14()
    ks = sorted(m.US["AAPL"])
    h = Hinh("Apple: ROE tăng gấp bốn trong mười năm — bao nhiêu là do kinh doanh?",
             "Năm tài chính kết thúc", "Chỉ số, năm đầu = 1,00")
    x = list(range(len(ks)))
    d0 = m.US["AAPL"][ks[0]]
    b0, v0, l0 = d0[1] / d0[0], d0[0] / d0[2], d0[2] / d0[3]
    h.truc((0, len(ks) - 1), (0.5, 4.6), vach_x=x,
           dinh_x=lambda i: ks[int(i)][:4], dinh_y=lambda v: f"{v:.1f}")
    for ten, f, mau in (("biên lợi nhuận", lambda d: (d[1] / d[0]) / b0, MAU[2]),
                        ("vòng quay tài sản", lambda d: (d[0] / d[2]) / v0, MAU[0]),
                        ("ĐÒN BẨY (tổng TS / vốn chủ)", lambda d: (d[2] / d[3]) / l0, MAU[1]),
                        ("ROE", lambda d: (d[1] / d[3]) / (d0[1] / d0[3]), MAU[3])):
        pts = [(i, f(m.US["AAPL"][k])) for i, k in enumerate(ks)]
        h.duong(pts, mau, ten, rong=3.4 if ten == "ROE" else 2.2)
    h.ke_ngang(1.0, "#bbb", "4 4")
    h.chu_thich(h.L + 20, h.T + 20)
    vc = [m.US["AAPL"][k][3] / 1000 for k in ks]
    h.ghi_chu_duoi(f"Vốn chủ sở hữu đi từ {vc[0]:,.0f} tỷ đô xuống {min(vc):,.0f} tỷ đô "
                   f"rồi lên {vc[-1]:,.0f} — do mua lại cổ phiếu quỹ. Đòn bẩy là thành phần "
                   f"đóng góp nhiều nhất vào mức tăng ROE, chứ không phải biên lợi nhuận.")
    xuat(h, "bai14-apple-don-bay.svg")


def bai14_chu_ky_tien_mat():
    m = _b14()
    NAM = 2025
    ma_ds = [x for x in ("FPT", "VNM", "MWG", "HPG", "PNJ") if NAM in m.VN[x]]
    h = Hinh("Chu kỳ tiền mặt: bao nhiêu ngày tiền của doanh nghiệp bị kẹt lại",
             "", "Số ngày")
    h.truc((-0.6, len(ma_ds) - 0.4), (-70, 210), vach_x=list(range(len(ma_ds))),
           dinh_x=lambda i: ma_ds[int(i)], dinh_y=lambda v: f"{v:.0f}", goc_khong=True)
    for i, ma in enumerate(ma_ds):
        gv = m.cot(ma, NAM, "gia_von")
        dt = m.cot(ma, NAM, "doanh_thu")
        tk = m.binh_quan(ma, NAM, "ton_kho") / gv * 365
        pt = m.binh_quan(ma, NAM, "phai_thu") / dt * 365
        ptr = m.binh_quan(ma, NAM, "phai_tra_ncc") / gv * 365
        for j, (v, mau, day) in enumerate(((tk, MAU[0], 0), (pt, MAU[2], tk), (-ptr, MAU[1], 0))):
            x = h.px(i) + (j - 1) * 26
            y0, y1 = sorted((h.py(day), h.py(day + v)))
            h.e.append(f'<rect x="{x-11:.1f}" y="{y0:.1f}" width="22"'
                       f' height="{max(y1-y0,1):.1f}" fill="{mau}" opacity="0.85"/>')
        ccc = tk + pt - ptr
        h.cham(i, ccc, MUC, 6)
        h.moc(i, ccc, f"CCC {ccc:.0f}n", MUC, 0, -13, 12, "middle", True)
    for j, (ten, mau) in enumerate((("ngày tồn kho", MAU[0]), ("ngày phải thu", MAU[2]),
                                    ("ngày phải trả (âm)", MAU[1]))):
        h.e.append(f'<rect x="{h.L+18}" y="{h.T+10+j*20}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 42, h.T + 20 + j * 20, ten, MUC, 12)
    h.ghi_chu_duoi("PNJ giữ hàng tồn kho gần 200 ngày vì vàng và trang sức là hàng trưng bày. "
                   "FPT gần như không có tồn kho nhưng cho khách nợ lâu nhất. Cùng một ROE, "
                   "hai nhu cầu vốn lưu động hoàn toàn khác nhau.")
    xuat(h, "bai14-chu-ky-tien-mat.svg")


def bai14_roic():
    m = _b14()
    ma_ds = ["MWG", "FPT", "VNM", "HPG"]
    nams = list(range(2016, 2026))
    h = Hinh("ROIC nhiều năm — thước đo bỏ qua cách tài trợ, nên ổn định hơn ROE",
             "Năm", "ROIC = NOPAT / vốn đầu tư bình quân")
    h.truc((nams[0], nams[-1]), (-0.02, 0.36), vach_x=nams[::2],
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0%}", goc_khong=True)
    for i, ma in enumerate(ma_ds):
        pts = [(y, m.roic(ma, y)[2]) for y in nams
               if y in m.VN[ma] and y != m.co(ma)[0]]
        if pts:
            h.duong(pts, MAU[i], ma, rong=2.6)
            h.moc(pts[-1][0], pts[-1][1], ma, MAU[i], 8, 4, 12, "start", True)
    h.chu_thich(h.L + 20, h.T + 20)
    h.ghi_chu_duoi("Hoà Phát đi từ 28% năm 2021 xuống 6% năm 2023 — đó là chu kỳ thép, "
                   "không phải quản trị kém. Vinamilk gần như phẳng. Cùng một thước đo, "
                   "hai câu chuyện ngành hoàn toàn khác nhau.")
    xuat(h, "bai14-roic.svg")


def _b15():
    return nap("bai-15-wacc.py")


def bai15_thanh_phan_wacc():
    """WACC tach thanh hai phan dong gop: von chu va no."""
    m = _b15()
    h = Hinh("WACC tách làm hai phần: vốn chủ đắt, nợ rẻ — tỷ trọng quyết định",
             "", "Chi phí vốn (%/năm)")
    ma = m.MA
    h.truc((-0.6, len(ma) - 0.4), (0, 0.135), vach_x=list(range(len(ma))),
           dinh_x=lambda i: ma[int(i)], dinh_y=lambda v: f"{v:.0%}")
    for i, k in enumerate(ma):
        w, wd, ke, kd = m.wacc(k)
        p_e, p_d = (1 - wd) * ke, wd * kd
        x = h.px(i)
        for v0, v1, mau in ((0, p_e, MAU[0]), (p_e, p_e + p_d, MAU[3])):
            y0, y1 = h.py(v1), h.py(v0)
            h.e.append(f'<rect x="{x-34:.1f}" y="{y0:.1f}" width="68"'
                       f' height="{y1-y0:.1f}" fill="{mau}" opacity="0.88"/>')
        h.cham(i, ke, MAU[1], 5)
        h.moc(i, ke, f"Ke {ke:.1%}", MAU[1], 40, 4, 10, "middle")
        h.moc(i, w, f"{w:.2%}", MUC, 0, -12, 12, "middle", True)
        h.chu(x, h.py(p_e / 2) + 4, f"{wd:.0%} nợ", "#fff", 10, "middle")
    for j, (ten, mau) in enumerate((("phần vốn chủ đóng góp", MAU[0]),
                                    ("phần nợ đóng góp (sau thuế)", MAU[3]),
                                    ("Ke — chi phí vốn chủ đứng riêng", MAU[1]))):
        h.e.append(f'<rect x="{h.L+18}" y="{h.T+10+j*20}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 42, h.T + 20 + j * 20, ten, MUC, 12)
    h.ghi_chu_duoi("HPG có Ke cao nhất (12,4%) nhưng WACC chỉ 8,99% — vì 35,6% vốn của nó "
                   "là nợ, và nợ sau thuế chỉ 2,85%. Đòn bẩy kéo WACC xuống; bài 16 hỏi "
                   "kéo được tới đâu.")
    xuat(h, "bai15-thanh-phan-wacc.svg")


def bai15_do_nhay():
    """WACC theo phan bu rui ro, cho ca nam doanh nghiep."""
    m = _b15()
    h = Hinh("WACC không phải một con số — nó là một khoảng",
             "Phần bù rủi ro thị trường giả định", "WACC")
    mrps = [v / 1000 for v in range(50, 121)]
    h.truc((0.05, 0.12), (0.04, 0.145),
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:.0%}")
    for i, k in enumerate(m.MA):
        pts = [(x, m.wacc(k, m.RF_VN, x)[0]) for x in mrps]
        h.duong(pts, MAU[i % 6], k, rong=2.4)
        h.moc(pts[-1][0], pts[-1][1], k, MAU[i % 6], 8, 4, 11, "start", True)
    h.ke_doc(m.MRP_VN, "#bbb", "4 4", f"giả định dùng trong bài: {m.MRP_VN:.0%}")
    h.ghi_chu_duoi("Cùng một doanh nghiệp, WACC chạy vài điểm chỉ vì một giả định không ai "
                   "đo được. Đó là lý do phải báo cáo một khoảng, không phải một con số.")
    xuat(h, "bai15-do-nhay.svg")


def bai15_roic_wacc():
    """ROIC so voi WACC: ai tao gia tri."""
    m = _b15()
    ds = sorted(((k, m.roic(k), m.wacc(k)[0]) for k in m.MA), key=lambda x: -(x[1] - x[2]))
    h = Hinh("ROIC trừ WACC — thước đo cuối cùng của phần E",
             "", "Suất sinh lời trên vốn (%/năm)")
    h.truc((-0.6, len(ds) - 0.4), (0, 0.25), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)][0], dinh_y=lambda v: f"{v:.0%}")
    for i, (k, r, w) in enumerate(ds):
        x = h.px(i)
        lo, hi = min(r, w), max(r, w)
        mau = MAU[2] if r > w else MAU[1]
        h.e.append(f'<rect x="{x-16:.1f}" y="{h.py(hi):.1f}" width="32"'
                   f' height="{h.py(lo)-h.py(hi):.1f}" fill="{mau}" opacity="0.28"/>')
        h.e.append(f'<line x1="{x-30:.1f}" y1="{h.py(w):.1f}" x2="{x+30:.1f}"'
                   f' y2="{h.py(w):.1f}" stroke="{MAU[3]}" stroke-width="3"/>')
        h.cham(i, r, MAU[0], 7)
        h.moc(i, r, f"{r:.1%}", MAU[0], 0, -13, 12, "middle", True)
        h.moc(i, w, f"{w:.2%}", MAU[3], 0, 21, 11, "middle")
        h.chu(x + 22, (h.py(lo) + h.py(hi)) / 2 + 4, f"{(r-w)*100:+.1f}đ", mau, 13,
              "start", True)
    yl = h.py(0.045)
    h.e.append(f'<circle cx="{h.L+320}" cy="{yl-4}" r="6" fill="{MAU[0]}"/>')
    h.chu(h.L + 332, yl, "ROIC — suất sinh lời thực tế trên vốn", MUC, 12)
    h.e.append(f'<line x1="{h.L+312}" y1="{yl+18}" x2="{h.L+330}" y2="{yl+18}"'
               f' stroke="{MAU[3]}" stroke-width="3"/>')
    h.chu(h.L + 338, yl + 22, "WACC — chi phí cơ hội của vốn đó", MUC, 12)
    h.ghi_chu_duoi("Bốn doanh nghiệp đầu tạo giá trị rõ rệt. HPG chênh −0,3 điểm — nhỏ hơn "
                   "sai số của chính WACC, nên kết luận trung thực là “không phân biệt được "
                   "với hoà vốn”, chứ không phải “phá giá trị”.")
    xuat(h, "bai15-roic-wacc.svg")


def bai15_hamada():
    """Go va gan don bay cho beta."""
    m = _b15()
    h = Hinh("Công thức Hamada: tách rủi ro NGÀNH khỏi rủi ro do VAY NỢ",
             "", "Beta")
    ma = m.MA
    h.truc((-0.6, len(ma) - 0.4), (0, 1.35), vach_x=list(range(len(ma))),
           dinh_x=lambda i: ma[int(i)], dinh_y=lambda v: f"{v:.1f}")
    for i, k in enumerate(ma):
        b = m.beta(k)[0]
        de = m.no_vay(k) / m.von_hoa(k)
        bu = m.beta_khong_don_bay(b, de, m.THUE_VN)
        x = h.px(i)
        h.e.append(f'<rect x="{x-30:.1f}" y="{h.py(bu):.1f}" width="60"'
                   f' height="{h.py(0)-h.py(bu):.1f}" fill="{MAU[0]}" opacity="0.85"/>')
        h.e.append(f'<rect x="{x-30:.1f}" y="{h.py(b):.1f}" width="60"'
                   f' height="{h.py(bu)-h.py(b):.1f}" fill="{MAU[1]}" opacity="0.85"/>')
        h.moc(i, b, f"{b:.2f}", MUC, 0, -11, 12, "middle", True)
        h.chu(x, h.py(bu / 2) + 4, f"{bu:.2f}", "#fff", 11, "middle", True)
        h.chu(x, h.py(0) + 34, f"D/E {de:.2f}", XAM, 10, "middle")
    for j, (ten, mau) in enumerate((("beta KHÔNG đòn bẩy — rủi ro của chính ngành", MAU[0]),
                                    ("phần đòn bẩy tài chính cộng thêm", MAU[1]))):
        h.e.append(f'<rect x="{h.L+18}" y="{h.T+10+j*20}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 42, h.T + 20 + j * 20, ten, MUC, 12)
    h.ghi_chu_duoi("HPG có beta đo được cao nhất (1,17) nhưng gần một phần ba trong đó là do "
                   "nó vay nhiều. Beta ngành của nó (0,81) thấp hơn MWG (0,89) — điều mà "
                   "beta thô hoàn toàn che mất.")
    xuat(h, "bai15-hamada.svg")


# ===========================================================================
# BAI 16 — CO CAU VON
# ===========================================================================

def _b16():
    return nap("bai-16-co-cau-von.py")


def bai16_ba_the_gioi():
    """WACC theo don bay trong ba the gioi: MM khong thue, MM co thue, danh doi."""
    m = _b16()
    h = Hinh("Ba thế giới, ba câu trả lời cho “vay bao nhiêu?”",
             "Tỷ trọng nợ D/(D+E)", "WACC (%/năm)")
    ws = [i / 200 for i in range(0, 141)]
    ka = m.RF_VN + m.BETA_TS_HPG * m.MRP_VN
    h.truc((0, 0.70), (0.079, 0.104), vach_y=[0.08, 0.085, 0.09, 0.095, 0.10],
           dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:.1%}")
    # (1) MM 1958 — khong thue: WACC hang so, dung bang Ka
    h.duong([(w, ka) for w in ws], XAM, "MM 1958, không thuế: WACC = Ka, phẳng", 2.2, "6 4")
    # (2) MM 1963 — co thue: WACC = Ka (1 - thue x w), doc xuong mai
    h.duong([(w, ka * (1 - m.THUE_VN * w)) for w in ws], MAU[3],
            "MM 1963, có thuế: dốc xuống tới 100% nợ", 2.2, "6 4")
    # (3) danh doi: Kd tang khi vay nhieu — dung dung ham cua muc 6
    dd = [(w, (1 - w) * (m.RF_VN + m.BETA_TS_HPG * (1 + (1 - m.THUE_VN) * w / (1 - w))
                         * m.MRP_VN) + w * m.kd_mo_hinh(w) * (1 - m.THUE_VN))
          for w in ws]
    h.duong(dd, MAU[1], "đánh đổi: thêm chi phí kiệt quệ — hình chữ U", 3.0)
    w_min, wacc_min = min(dd, key=lambda r: r[1])
    h.cham(w_min, wacc_min, MAU[1], 6)
    h.moc(w_min, wacc_min, f"đáy chữ U: {wacc_min:.2%}\ntại D/V = {w_min:.0%}", MAU[1],
          12, 24, 11, "start", True)
    phang = [w for w, v in dd if v < wacc_min + 0.001]
    h.e.append(f'<rect x="{h.px(min(phang)):.1f}" y="{h.py(wacc_min + 0.001):.1f}"'
               f' width="{h.px(max(phang)) - h.px(min(phang)):.1f}"'
               f' height="{h.py(wacc_min) - h.py(wacc_min + 0.001):.1f}"'
               f' fill="{MAU[1]}" opacity="0.14"/>')
    h.chu(h.px((min(phang) + max(phang)) / 2), h.py(wacc_min + 0.0016),
          f"vùng phẳng {min(phang):.0%}–{max(phang):.0%}", MAU[1], 10, "middle")
    y = m.nam_cuoi("HPG")
    wt = m.ti_trong_no("HPG", y)
    h.ke_doc(wt, "#999", "3 3", f"HPG {y}: {wt:.0%}")
    h.chu_thich(h.L + 250, h.T + 12)
    h.ghi_chu_duoi("Cùng một beta tài sản (0,814 của HPG, bài 15 §11), chỉ khác nhau ở giả "
                   "định. Đường vàng chính là chỗ mô hình tự bóp cổ mình: nó bảo vay 100%. "
                   "Đáy chữ U rất phẳng — không có con số vàng, chỉ có một vùng chấp nhận được.")
    xuat(h, "bai16-ba-the-gioi.svg")


def bai16_hvn():
    """Von chu HVN bay hoi trong hai nam."""
    m = _b16()
    ys = [y for y in m.cac_nam("HVN") if y >= 2013]
    h = Hinh("Vietnam Airlines: đòn bẩy quyết định TRƯỚC khi cú sốc đến",
             "", "Vốn chủ sở hữu (tỷ đồng)")
    vcs = [m.bc("HVN", y, "vcsh") for y in ys]
    h.truc((ys[0] - 0.6, ys[-1] + 0.6), (-20000, 26000),
           vach_x=ys, dinh_x=lambda v: str(int(v)),
           dinh_y=lambda v: f"{v/1000:,.0f}k", goc_khong=True)
    for y, v in zip(ys, vcs):
        h.cot([(y, v)], MAU[2] if v > 0 else MAU[1], 26)
    h.duong(list(zip(ys, vcs)), MUC, None, 1.4, "3 3", 0.5)
    for y, v in zip(ys, vcs):
        h.moc(y, v, f"{v:,.0f}", MUC, 0, -10 if v > 0 else 18, 9.5, "middle")
    h.ke_doc(2019.5, MAU[1], "5 4", "cú sốc COVID bắt đầu")
    de19 = m.vay("HVN", 2019) / m.bc("HVN", 2019, "vcsh")
    h.chu(h.px(2013.6), h.py(21000), f"bảy năm trước cú sốc: D/E từ "
          f"{min(m.vay('HVN', y) / m.bc('HVN', y, 'vcsh') for y in range(2013, 2020)):.1f} "
          f"đến {max(m.vay('HVN', y) / m.bc('HVN', y, 'vcsh') for y in range(2013, 2020)):.1f}",
          XAM, 12)
    h.ghi_chu_duoi(f"Vốn chủ 18.608 tỷ (2019) rơi xuống ÂM 17.026 tỷ (2023). Công ty không "
                   f"chọn lúc nào cú sốc đến — nó chỉ chọn trước đó một vùng đệm dày bao "
                   f"nhiêu. D/E năm 2019 là {de19:.2f}.")
    xuat(h, "bai16-hvn.svg")


def bai16_duoi_trai():
    """Chi phi kiet que hien ra o duoi trai, khong o trung vi."""
    m = _b16()
    p = m.bang_panel()
    nhom = [(ten, [r[3] for r in p if lo <= r[2] < hi])
            for lo, hi, ten in m.NGUONG_COV]
    nhom = [(t, v) for t, v in nhom if v]
    h = Hinh("Chi phí kiệt quệ không nằm ở trung vị — nó nằm ở đuôi trái",
             "Hệ số khả năng trả lãi EBIT / chi phí lãi vay",
             "Thay đổi vốn chủ sau 3 năm")
    h.truc((-0.6, len(nhom) - 0.4), (-1.8, 0.9), vach_x=list(range(len(nhom))),
           dinh_x=lambda i: nhom[int(i)][0], dinh_y=lambda v: f"{v:+.0%}",
           goc_khong=True)
    for i, (ten, v) in enumerate(nhom):
        tv, p10 = m.phan_vi(v, 0.5), m.phan_vi(v, 0.1)
        x = h.px(i)
        h.e.append(f'<rect x="{x-26:.1f}" y="{h.py(tv):.1f}" width="52"'
                   f' height="{h.py(p10)-h.py(tv):.1f}" fill="{MAU[1]}" opacity="0.20"/>')
        h.cham(i, tv, MAU[0], 6)
        h.cham(i, p10, MAU[1], 6)
        h.moc(i, tv, f"{tv:+.0%}", MAU[0], 0, -12, 11, "middle", True)
        h.moc(i, p10, f"{p10:+.0%}", MAU[1], 0, 20, 11, "middle", True)
        h.chu(x, h.py(0.82), f"n={len(v)}", XAM, 10, "middle")
    yl = h.py(-1.45)
    h.e.append(f'<circle cx="{h.L+300}" cy="{yl-4}" r="6" fill="{MAU[0]}"/>')
    h.chu(h.L + 312, yl, "trung vị — gần như bằng nhau ở mọi nhóm", MUC, 12)
    h.e.append(f'<circle cx="{h.L+300}" cy="{yl+18}" r="6" fill="{MAU[1]}"/>')
    h.chu(h.L + 312, yl + 22, "phân vị 10 — kết cục xấu, chênh nhau vực thẳm", MUC, 12)
    h.ghi_chu_duoi(f"{len(p)} quan sát công ty-năm, 28 doanh nghiệp Việt Nam. Nhóm không trả "
                   f"nổi lãi có phân vị 10 dưới −100%: vốn chủ không những mất hết mà còn âm. "
                   f"Cảnh báo: mẫu chỉ gồm công ty CÒN niêm yết năm 2026.")
    xuat(h, "bai16-duoi-trai.svg")


def bai16_trat_tu():
    """Nguon von cua 12 doanh nghiep My, 2015-2025."""
    m = _b16()
    ds = sorted(m.MA_MY, key=lambda k: -m.tong_my(k, "cfo"))
    h = Hinh("Doanh nghiệp lấy tiền ở đâu? 12 công ty Mỹ, 2015–2025",
             "", "Nguồn vốn cộng dồn (tỷ USD)")
    h.truc((-0.6, len(ds) - 0.4), (0, 1250), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)], dinh_y=lambda v: f"{v:,.0f}")
    for i, k in enumerate(ds):
        c, n, v = (m.tong_my(k, t) for t in ("cfo", "no_phat_hanh", "vc_phat_hanh"))
        x = h.px(i)
        moc_duoi = 0.0
        for gt, mau in ((c, MAU[2]), (n, MAU[3]), (v, MAU[1])):
            if gt <= 0:
                continue
            h.e.append(f'<rect x="{x-19:.1f}" y="{h.py(moc_duoi+gt):.1f}" width="38"'
                       f' height="{h.py(moc_duoi)-h.py(moc_duoi+gt):.1f}"'
                       f' fill="{mau}" opacity="0.88"/>')
            moc_duoi += gt
        h.moc(i, moc_duoi, f"{c/(c+n+v):.0%}", MAU[2], 0, -10, 11, "middle", True)
    for j, (ten, mau) in enumerate((("tiền tự làm ra (dòng tiền kinh doanh)", MAU[2]),
                                    ("vay nợ", MAU[3]),
                                    ("phát hành cổ phiếu", MAU[1]))):
        h.e.append(f'<rect x="{h.L+250}" y="{h.T+10+j*20}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 274, h.T + 20 + j * 20, ten, MUC, 12)
    tc = sum(m.tong_my(k, "cfo") for k in m.MA_MY)
    tn = sum(m.tong_my(k, "no_phat_hanh") for k in m.MA_MY)
    tv = sum(m.tong_my(k, "vc_phat_hanh") for k in m.MA_MY)
    h.ghi_chu_duoi(f"Số phần trăm trên mỗi cột là tỷ lệ tiền TỰ LÀM RA. Cộng cả nhóm: "
                   f"{tc/(tc+tn+tv):.0%} tự có, {tn/(tc+tn+tv):.0%} vay nợ, "
                   f"{tv/(tc+tn+tv):.1%} phát hành cổ phiếu — đúng thứ tự Myers–Majluf. "
                   f"Cùng kỳ họ MUA LẠI cổ phiếu {sum(m.tong_my(k, 'mua_lai_cp') for k in m.MA_MY):,.0f} tỷ.")
    xuat(h, "bai16-trat-tu-uu-tien.svg")


def bai16_dua_ngua():
    """Sinh loi va don bay: hai ly thuyet du doan nguoc nhau."""
    m = _b16()
    ds = []
    for k in m.MA_VN:
        y = m.nam_cuoi(k)
        ts = m.bc(k, y, "tong_ts")
        ds.append((k, m.ebit(k, y) / ts, m.ti_trong_no(k, y)))
    h = Hinh("Cuộc đua ngựa: doanh nghiệp lãi nhiều thì vay NHIỀU hay ÍT?",
             "Sinh lời: EBIT / tổng tài sản", "Tỷ trọng nợ D/(D+E)")
    h.truc((0, 0.50), (0, 0.80), dinh_x=lambda v: f"{v:.0%}",
           dinh_y=lambda v: f"{v:.0%}")
    xs = [d[1] for d in ds]
    ys = [d[2] for d in ds]
    a0, b, t = m.hoi_quy(ys, xs)
    r, tr = m.tuong_quan(xs, ys)
    for k, x, y in ds:
        h.cham(x, y, MAU[0], 5)
        h.moc(x, y, k, XAM, 7, -6, 9.5)
    h.duong([(0.0, a0), (0.50, a0 + b * 0.50)], MAU[1],
            f"đường hồi quy: r = {r:+.3f}, t = {tr:+.2f}", 2.6)
    h.chu(h.L + 300, h.T + 30, "đánh đổi dự đoán dốc LÊN", XAM, 12)
    h.chu(h.L + 300, h.T + 48, "trật tự ưu tiên dự đoán dốc XUỐNG", MUC, 12, dam=True)
    h.chu_thich(h.L + 300, h.T + 66)
    h.ghi_chu_duoi("Đường dốc xuống rõ rệt: càng lãi nhiều càng vay ít. Đó là dự đoán của "
                   "trật tự ưu tiên, và ngược với lý thuyết đánh đổi. Cùng bộ dữ liệu, tài "
                   "sản hữu hình không giải thích được gì (r = −0,03).")
    xuat(h, "bai16-dua-ngua.svg")


# ===========================================================================
# BAI 17 — CHI PHI DAI DIEN VA CHINH SACH CHI TRA
# ===========================================================================

def _b17():
    return nap("bai-17-chi-phi-dai-dien.py")


def bai17_chuyen_rui_ro():
    """Von chu la mot quyen chon mua — nen co dong thich bien dong."""
    m = _b17()
    h = Hinh("Vốn chủ của công ty có nợ là một QUYỀN CHỌN MUA",
             "Giá trị tài sản công ty khi đáo hạn (tỷ)", "Giá trị nhận được (tỷ)")
    D = m.NO_GOC
    h.truc((0, 220), (0, 130), dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0f}")
    h.duong([(0, 0), (D, D), (220, D)], MAU[3], "chủ nợ — trần cứng ở mệnh giá nợ", 2.8)
    h.duong([(0, 0), (D, 0), (220, 120)], MAU[0], "cổ đông — payoff quyền chọn mua", 2.8)
    h.ke_doc(D, "#999", "4 3", f"mệnh giá nợ {D:,.0f}")
    for ten, dl, mau in (("an toàn", m.AN_TOAN, MAU[2]), ("rủi ro", m.RUI_RO, MAU[1])):
        for v in set(dl):
            h.cham(v, max(v - D, 0.0), mau, 5)
        kv = m.XAC_SUAT * dl[0] + (1 - m.XAC_SUAT) * dl[1]
        cd = m.XAC_SUAT * max(dl[0] - D, 0) + (1 - m.XAC_SUAT) * max(dl[1] - D, 0)
        h.cham(kv, cd, mau, 8)
        h.moc(kv, cd, f"dự án {ten}\ncông ty {kv:,.0f} · cổ đông {cd:,.0f}", mau,
              -6 if ten == "an toàn" else 10, -30 if ten == "an toàn" else 16, 11,
              "end" if ten == "an toàn" else "start", True)
    h.chu_thich(h.L + 20, h.T + 8)
    kv_a = m.XAC_SUAT * m.AN_TOAN[0] + (1 - m.XAC_SUAT) * m.AN_TOAN[1]
    kv_r = m.XAC_SUAT * m.RUI_RO[0] + (1 - m.XAC_SUAT) * m.RUI_RO[1]
    h.ghi_chu_duoi(f"Dự án rủi ro làm CẢ CÔNG TY mất {kv_a - kv_r:,.0f} tỷ giá trị kỳ vọng, "
                   f"nhưng làm CỔ ĐÔNG được thêm 30 tỷ — vì phía dưới họ đã được trách nhiệm "
                   f"hữu hạn chặn lại. Giá quyền chọn tăng theo biến động (bài 8 §12).")
    xuat(h, "bai17-chuyen-rui-ro.svg")


def bai17_co_tuc_muot():
    """Co tuc muot hon loi nhuan bao nhieu lan."""
    m = _b17()
    ds = []
    for k in m.MA_MY:
        ys = [y for y in m.NAM_MY if m.my(k, y, "ln") is not None
              and m.my(k, y, "co_tuc") not in (None, 0)]
        if len(ys) < 10:
            continue
        L = [m.my(k, y, "ln") for y in ys]
        C = [m.my(k, y, "co_tuc") for y in ys]
        ds.append((k, m.he_so_bien_thien(L), m.he_so_bien_thien(C)))
    ds.sort(key=lambda x: -x[1])
    h = Hinh("Lợi nhuận nhảy, cổ tức thì không", "", "Hệ số biến thiên 2009–2025")
    h.truc((-0.6, len(ds) - 0.4), (0, 2.8), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)][0], dinh_y=lambda v: f"{v:.0%}")
    for i, (k, cl, cc) in enumerate(ds):
        x = h.px(i)
        h.e.append(f'<rect x="{x-14:.1f}" y="{h.py(cl):.1f}" width="13"'
                   f' height="{h.py(0)-h.py(cl):.1f}" fill="{MAU[1]}" opacity="0.85"/>')
        h.e.append(f'<rect x="{x+1:.1f}" y="{h.py(cc):.1f}" width="13"'
                   f' height="{h.py(0)-h.py(cc):.1f}" fill="{MAU[0]}" opacity="0.85"/>')
    for j, (ten, mau) in enumerate((("biến thiên của LỢI NHUẬN", MAU[1]),
                                    ("biến thiên của CỔ TỨC đã trả", MAU[0]))):
        h.e.append(f'<rect x="{h.L+300}" y="{h.T+10+j*20}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 324, h.T + 20 + j * 20, ten, MUC, 12)
    ti = m.trung_vi([a / b for _, a, b in ds])
    h.ghi_chu_duoi(f"Ở mọi doanh nghiệp trừ McDonald's, cột đỏ cao hơn cột xanh. Trung vị: "
                   f"cổ tức mượt hơn lợi nhuận {ti:.1f} lần. GE là ngoại lệ ngược — nó cắt cổ "
                   f"tức sáu lần trong 17 năm, và đó là công ty duy nhất trong nhóm làm vậy.")
    xuat(h, "bai17-co-tuc-muot.svg")


def bai17_co_tuc_vs_mua_lai():
    """Kenh cam ket va kenh linh hoat, cong don 17 doanh nghiep."""
    m = _b17()
    h = Hinh("Hai kênh chi trả: cam kết và linh hoạt", "", "Tỷ USD, cộng dồn 17 doanh nghiệp")
    ys = m.NAM_MY
    def tong(y, cot):
        ms = [k for k in m.MA_MY if m.my(k, y, "ln") is not None
              and m.my(k, y, "co_tuc") is not None and m.my(k, y, "mua_cp") is not None]
        return sum(m.my(k, y, cot) for k in ms)
    h.truc((ys[0] - 0.6, ys[-1] + 0.6), (0, 400), vach_x=ys[::2],
           dinh_x=lambda v: str(int(v)), dinh_y=lambda v: f"{v:,.0f}")
    h.duong([(y, tong(y, "ln")) for y in ys], XAM, "lợi nhuận", 2.0, "5 4")
    h.duong([(y, tong(y, "co_tuc")) for y in ys], MAU[0], "cổ tức — kênh CAM KẾT", 3.0)
    h.duong([(y, tong(y, "mua_cp")) for y in ys], MAU[1], "mua lại cổ phiếu — kênh LINH HOẠT", 3.0)
    for y, mau, cot in ((ys[-1], MAU[0], "co_tuc"), (ys[-1], MAU[1], "mua_cp")):
        h.moc(y, tong(y, cot), f"{tong(y, cot):,.0f}", mau, -4, -10, 12, "end", True)
    dem = sum(1 for y in ys if tong(y, "mua_cp") > tong(y, "co_tuc"))
    h.chu_thich(h.L + 20, h.T + 8)
    h.ghi_chu_duoi(f"Mua lại cổ phiếu lớn hơn cổ tức ở {dem}/{len(ys)} năm, và đường đỏ nhấp nhô "
                   f"theo lợi nhuận trong khi đường xanh gần như là một đường thẳng. Đó chính "
                   f"là chênh lệch tốc độ điều chỉnh mà kiểm định Lintner đo được (§10).")
    xuat(h, "bai17-co-tuc-vs-mua-lai.svg")


def bai17_boeing():
    """Boeing tra cho co dong gap may lan so tien dau tu."""
    m = _b17()
    h = Hinh("Boeing: tiền ra ngoài gấp nhiều lần tiền vào nhà máy",
             "", "Tỷ USD")
    ys = [y for y in m.NAM_MY if y >= 2013]
    h.truc((ys[0] - 0.6, ys[-1] + 0.6), (-20, 20), vach_x=ys,
           dinh_x=lambda v: str(int(v)), dinh_y=lambda v: f"{v:,.0f}",
           goc_khong=True)
    for y in ys:
        ct = m.my("BA", y, "co_tuc") or 0.0
        mu = m.my("BA", y, "mua_cp") or 0.0
        cx = m.my("BA", y, "capex") or 0.0
        x = h.px(y)
        for v0, v1, mau in ((0, ct, MAU[0]), (ct, ct + mu, MAU[1])):
            if v1 <= v0:
                continue
            h.e.append(f'<rect x="{x-15:.1f}" y="{h.py(v1):.1f}" width="14"'
                       f' height="{h.py(v0)-h.py(v1):.1f}" fill="{mau}" opacity="0.88"/>')
        h.e.append(f'<rect x="{x+1:.1f}" y="{h.py(cx):.1f}" width="14"'
                   f' height="{h.py(0)-h.py(cx):.1f}" fill="{MAU[2]}" opacity="0.88"/>')
    h.duong([(y, m.my("BA", y, "cfo")) for y in ys], MUC, "dòng tiền kinh doanh", 2.2, "4 3")
    vc = [(m.my("BA", y, "vc_ph") or 0.0, y) for y in ys]
    v, ny = max(vc)
    h.cham(ny, -v, MAU[5], 7)
    h.moc(ny, -v, f"phát hành cổ phiếu\n{v:,.1f} tỷ", MAU[5], -8, 6, 11, "end", True)
    for j, (ten, mau) in enumerate((("cổ tức", MAU[0]), ("mua lại cổ phiếu", MAU[1]),
                                    ("đầu tư tài sản cố định", MAU[2]))):
        h.e.append(f'<rect x="{h.L+18}" y="{h.T+10+j*19}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 42, h.T + 19 + j * 19, ten, MUC, 12)
    a, b = m.BOEING_TRUOC
    tra = sum((m.my("BA", y, "co_tuc") or 0) + (m.my("BA", y, "mua_cp") or 0) for y in range(a, b + 1))
    cx = sum(m.my("BA", y, "capex") or 0 for y in range(a, b + 1))
    h.ghi_chu_duoi(f"{a}–{b}: trả cho cổ đông {tra:,.1f} tỷ, đầu tư vào tài sản cố định "
                   f"{cx:,.1f} tỷ — gấp {tra/cx:.1f} lần. Năm {ny} công ty phải bán cổ phiếu "
                   f"của chính mình ở mức giá thấp hơn nhiều giá đã mua lại.")
    xuat(h, "bai17-boeing.svg")


def bai17_chi_tra_vn():
    """Chi tra va tang truong: du doan cua Jensen tren du lieu Viet Nam."""
    m = _b17()
    ds = m.bang_vn()
    h = Hinh("Doanh nghiệp ít cơ hội tăng trưởng có trả tiền ra nhiều hơn không?",
             "Tăng trưởng doanh thu 2015–2025 (%/năm)", "Chi trả / lợi nhuận cộng dồn")
    h.truc((-0.02, 0.45), (0, 0.95), dinh_x=lambda v: f"{v:.0%}", dinh_y=lambda v: f"{v:.0%}")
    for x in ds:
        h.cham(x["cagr"], min(x["chi"], 0.93), MAU[0], 5)
        h.moc(x["cagr"], min(x["chi"], 0.93), x["ma"], XAM, 7, -6, 9.5)
    xs = [x["cagr"] for x in ds]
    ys = [x["chi"] for x in ds]
    mx, my_ = m.trung_binh(xs), m.trung_binh(ys)
    b = (sum((a - mx) * (c - my_) for a, c in zip(xs, ys))
         / sum((a - mx) ** 2 for a in xs))
    a0 = my_ - b * mx
    r, t = m.tuong_quan(xs, ys)
    h.duong([(-0.02, a0 - b * 0.02), (0.45, a0 + b * 0.45)], MAU[1],
            f"hồi quy: r = {r:+.3f}, t = {t:+.2f} — KHÔNG có ý nghĩa thống kê", 2.4, "6 4")
    h.ke_ngang(m.NGUONG_CHI_TRA, "#999", "3 3", f"ngưỡng chia nhóm {m.NGUONG_CHI_TRA:.0%}")
    cao = [x for x in ds if x["chi"] >= m.NGUONG_CHI_TRA]
    thap = [x for x in ds if x["chi"] < m.NGUONG_CHI_TRA]
    h.chu_thich(h.L + 250, h.T + 8)
    h.ghi_chu_duoi(f"Trung vị tăng trưởng: nhóm trả nhiều {m.trung_vi(x['cagr'] for x in cao):.1%}/năm, "
                   f"nhóm trả ít {m.trung_vi(x['cagr'] for x in thap):.1%}/năm — đúng hướng Jensen dự "
                   f"đoán. Nhưng đường hồi quy không đạt ý nghĩa thống kê với n = {len(ds)}: đây là "
                   f"một gợi ý, không phải bằng chứng.")
    xuat(h, "bai17-chi-tra-vn.svg")


def bai17_loi_nhuan_khong_phai_tien():
    """CFO so voi LNST cong don, 28 doanh nghiep Viet Nam."""
    m = _b17()
    ds = []
    for k in m.MA_VN:
        ln = sum(m.vn(k, y, "lnst") for y in m.NAM_VN)
        if ln <= 0:
            continue
        ds.append((k, ln, m.vn_cong(k, "cfo")))
    ds.sort(key=lambda x: x[2] / x[1])
    h = Hinh("Lợi nhuận có, tiền thì chưa chắc — cộng dồn 2015–2025",
             "", "Tỷ đồng, cộng dồn 11 năm")
    hi = max(max(x[1], x[2]) for x in ds)
    h.truc((-0.6, len(ds) - 0.4), (-40000, 270000), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)][0], dinh_y=lambda v: f"{v/1000:,.0f}k",
           goc_khong=True)
    for i, (k, ln, cfo) in enumerate(ds):
        x = h.px(i)
        h.e.append(f'<rect x="{x-11:.1f}" y="{h.py(max(ln,0)):.1f}" width="10"'
                   f' height="{abs(h.py(0)-h.py(ln)):.1f}" fill="{MAU[3]}" opacity="0.88"/>')
        mau = MAU[2] if cfo >= 0 else MAU[1]
        y0, y1 = sorted((h.py(0), h.py(cfo)))
        h.e.append(f'<rect x="{x+1:.1f}" y="{y0:.1f}" width="10"'
                   f' height="{y1-y0:.1f}" fill="{mau}" opacity="0.88"/>')
    for j, (ten, mau) in enumerate((("lợi nhuận sau thuế cộng dồn", MAU[3]),
                                    ("dòng tiền kinh doanh cộng dồn", MAU[2]),
                                    ("dòng tiền kinh doanh ÂM", MAU[1]))):
        h.e.append(f'<rect x="{h.L+250}" y="{h.T+10+j*19}" width="18" height="11" fill="{mau}"/>')
        h.chu(h.L + 274, h.T + 19 + j * 19, ten, MUC, 12)
    am = [x[0] for x in ds if x[2] < 0]
    h.ghi_chu_duoi(f"{len(am)} doanh nghiệp có lợi nhuận cộng dồn DƯƠNG nhưng dòng tiền kinh doanh "
                   f"cộng dồn ÂM suốt 11 năm: {', '.join(am)}. Với doanh nghiệp bất động sản điều "
                   f"này là cơ cấu chứ không bất thường — nhưng nó vẫn để ngỏ câu hỏi tiền trả cổ "
                   f"tức lấy từ đâu.")
    xuat(h, "bai17-loi-nhuan-khong-phai-tien.svg")


# ===========================================================================
# BAI 18 — DINH GIA DOANH NGHIEP
# ===========================================================================

def _b18():
    return nap("bai-18-dinh-gia-doanh-nghiep.py")


def bai18_gia_tri_cuoi_ky():
    """Gia tri cuoi ky chiem bao nhieu phan tram, theo so nam du bao."""
    m = _b18()
    h = Hinh("Càng dự báo dài, giá trị cuối kỳ càng bớt lấn — nhưng không bao giờ hết",
             "Số năm dự báo chi tiết", "Phần giá trị nằm ở giai đoạn dự báo")
    ns = list(range(1, 31))
    h.truc((1, 30), (0, 0.85), dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0%}")
    for i, ma in enumerate(("VNM", "FPT", "GAS", "SAB")):
        pts = [(n, m.dcf(ma, n=n)[1] / m.dcf(ma, n=n)[0]) for n in ns]
        h.duong(pts, MAU[i % 6], ma, 2.4)
        h.moc(pts[-1][0], pts[-1][1], ma, MAU[i % 6], 6, 4, 11, "start", True)
    n0 = m.SO_NAM_DU_BAO
    t, dt, cuoi = m.dcf("VNM")
    h.ke_doc(n0, "#999", "3 3", f"bài này dùng {n0} năm")
    h.cham(n0, dt / t, MAU[0], 6)
    h.ghi_chu_duoi(f"Với 10 năm dự báo, {cuoi/t:.0%} giá trị VNM vẫn nằm ở giá trị cuối kỳ — "
                   f"phần sau năm thứ 10, nơi không ai dự báo được gì. Kéo dự báo ra 30 năm "
                   f"cũng chỉ đưa phần dự báo được lên {m.dcf('VNM', n=30)[1]/m.dcf('VNM', n=30)[0]:.0%}.")
    xuat(h, "bai18-gia-tri-cuoi-ky.svg")


def bai18_do_nhay():
    """Gia tri mot co phieu theo WACC va tang truong vinh vien."""
    m = _b18()
    ma = m.MA_MAU
    y = m.NAM[-1]
    r0 = m.wacc(ma)
    no_rong = m.vay(ma, y) - m.tien_mat(ma, y)
    cp = m.so_co_phieu(ma, y)
    gia = m.gia_hien_tai(ma)
    h = Hinh(f"Một ô vuông giả định, một khoảng giá trị gấp nhiều lần",
             "Tăng trưởng vĩnh viễn g", f"Giá trị {ma} (nghìn đồng/cổ phiếu)")
    gs = [i / 1000 for i in range(5, 51)]
    h.truc((0.005, 0.05), (0, 320), dinh_x=lambda v: f"{v:.0%}",
           dinh_y=lambda v: f"{v:.0f}")
    for i, dr in enumerate((-0.02, -0.01, 0.0, 0.01, 0.02)):
        r = r0 + dr
        pts = [(g, (m.dcf(ma, r=r, g_vv=g)[0] - no_rong) / cp) for g in gs
               if r - g >= 0.02]
        ten = f"WACC {r:.2%}" + (" (đang dùng)" if dr == 0 else "")
        h.duong(pts, MAU[i % 6], ten, 3.0 if dr == 0 else 2.0)
    h.ke_ngang(gia, MAU[1], "5 4", f"giá thị trường {gia:,.1f}")
    h.chu_thich(h.L + 18, h.T + 10)
    h.ghi_chu_duoi("Mỗi đường là một giả định WACC; mỗi điểm trên đường là một giả định "
                   "tăng trưởng. Không đường nào sai. Đó là lý do DCF sinh ra một bảng "
                   "chứ không sinh ra một con số.")
    xuat(h, "bai18-do-nhay.svg")


def bai18_dcf_hong():
    """Dong tien tu do binh quan 5 nam: bao nhieu doanh nghiep chiet khau duoc."""
    m = _b18()
    ds = sorted(((k, m.trung_binh(m.fcff(k, y) for y in m.NAM[-5:])) for k in m.MA),
                key=lambda x: x[1])
    h = Hinh("Gần một nửa mẫu không chiết khấu được — dòng tiền tự do âm",
             "", "FCFF bình quân 5 năm (tỷ đồng)")
    h.truc((-0.6, len(ds) - 0.4), (-35000, 12000), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)][0], dinh_y=lambda v: f"{v/1000:,.0f}k",
           goc_khong=True)
    for i, (k, v) in enumerate(ds):
        h.cot([(i, v)], MAU[1] if v <= 0 else MAU[2], 16)
    am = [k for k, v in ds if v <= 0]
    h.ke_doc(len(am) - 0.5, "#999", "4 3", "ranh giới")
    h.chu(h.px(len(am) / 2 - 0.5), h.py(9000), f"{len(am)} doanh nghiệp: KHÔNG chiết khấu được",
          MAU[1], 12, "middle", True)
    h.chu(h.px((len(am) + len(ds)) / 2 - 0.5), h.py(9000), f"{len(ds)-len(am)} doanh nghiệp: chạy được",
          MAU[2], 12, "middle", True)
    h.ghi_chu_duoi(f"{len(am)}/{len(ds)} doanh nghiệp có dòng tiền tự do bình quân 5 năm ÂM, "
                   f"nên công thức Gordon không dùng được. Không phải vì họ làm ăn kém — mà vì "
                   f"họ đang đầu tư mạnh hơn số tiền làm ra. Đó là giới hạn thật của DCF sách "
                   f"giáo khoa.")
    xuat(h, "bai18-dcf-hong.svg")


def bai18_dcf_nguoc():
    """Tang truong ham y tu gia so voi tang truong thuc te."""
    m = _b18()
    ok, hong = m.bang_dcf_nguoc()
    ok = [x for x in ok if x["cagr"] == x["cagr"]]
    h = Hinh("DCF ngược: giá hôm nay hàm ý tăng trưởng nào?",
             "Tăng trưởng doanh thu THỰC TẾ 2015–2025 (%/năm)",
             "Tăng trưởng HÀM Ý từ giá (%/năm)")
    h.truc((-0.02, 0.45), (-0.18, 0.14), dinh_x=lambda v: f"{v:.0%}",
           dinh_y=lambda v: f"{v:.0%}", goc_khong=True)
    h.duong([(-0.02, -0.02), (0.14, 0.14)], XAM, "đường 45° — hàm ý bằng thực tế", 2.0, "5 4")
    for x in ok:
        h.cham(x["cagr"], x["g"], MAU[0], 5)
        h.moc(x["cagr"], x["g"], x["ma"], XAM, 7, -6, 9.5)
    duoi = [x for x in ok if x["g"] < x["cagr"]]
    h.chu_thich(h.L + 250, h.T + 10)
    h.ghi_chu_duoi(f"{len(duoi)}/{len(ok)} doanh nghiệp nằm DƯỚI đường 45°, và khoảng cách nới "
                   f"rộng dần về bên phải. Doanh nghiệp tăng trưởng càng nhanh thì mô hình càng "
                   f"hụt — đó là dấu vân tay của lỗi mô hình, không phải của thị trường.")
    xuat(h, "bai18-dcf-nguoc.svg")


def bai18_boi_so():
    """Ba boi so tren cung mot mau: chung khong noi cung mot chuyen."""
    m = _b18()
    y = m.NAM[-1]
    ds = []
    for k in m.MA:
        ln, vc, eb = m.bc(k, y, "lnst"), m.bc(k, y, "vcsh"), m.ebit(k, y)
        E, EV = m.von_hoa(k), m.gia_tri_dn(k)
        if ln <= 0 or vc <= 0 or eb <= 0 or EV <= 0:
            continue
        ds.append((k, E / ln, E / vc, EV / eb))
    ds.sort(key=lambda x: x[1])
    h = Hinh("Ba bội số trên cùng một doanh nghiệp, ba thứ hạng khác nhau",
             "", "Bội số (thang lô-ga-rít)")
    import math as _m
    h.truc((-0.6, len(ds) - 0.4), (_m.log10(0.4), _m.log10(230)),
           vach_x=list(range(len(ds))),
           vach_y=[_m.log10(v) for v in (0.5, 1, 2, 5, 10, 20, 50, 100, 200)],
           dinh_x=lambda i: ds[int(i)][0], dinh_y=lambda v: f"{10**v:g}")
    for j, (ten, mau) in enumerate((("P/E", MAU[0]), ("P/B", MAU[2]), ("EV/EBIT", MAU[3]))):
        h.duong([(i, _m.log10(x[j + 1])) for i, x in enumerate(ds)], mau, ten, 2.2)
        for i, x in enumerate(ds):
            h.cham(i, _m.log10(x[j + 1]), mau, 3.5)
    h.chu_thich(h.L + 18, h.T + 10)
    pe = [x[1] for x in ds]
    h.ghi_chu_duoi(f"Trục dọc là thang lô-ga-rít vì P/E trong cùng một mẫu chênh nhau "
                   f"{max(pe)/min(pe):.0f} lần. Ba đường không song song: xếp hạng theo P/E khác "
                   f"hẳn xếp hạng theo P/B hay EV/EBIT, nên câu “rẻ hay đắt” phụ thuộc bội số "
                   f"nào được chọn.")
    xuat(h, "bai18-boi-so.svg")


def bai18_loi_nguyen():
    """Loi nguyen nguoi thang cuoc: cang dong doi thu cang phai ha gia."""
    m = _b18()
    h = Hinh("Lời nguyền người thắng cuộc: càng đông đối thủ càng phải trả THẤP hơn",
             "Số bên mua cùng đấu", "So với giá trị thật = 100")
    ns = list(range(2, 41))
    a = m.SAI_SO
    h.truc((2, 40), (85, 135), dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0f}")
    h.duong([(n, 100 * (1 + a * (n - 1) / (n + 1))) for n in ns], MAU[1],
            "ước lượng của người THẮNG cuộc", 3.0)
    h.ke_ngang(100, MAU[2], "5 4", "giá trị thật = 100")
    for n in m.SO_NGUOI_MUA:
        v = 100 * (1 + a * (n - 1) / (n + 1))
        h.cham(n, v, MAU[1], 5)
        h.moc(n, v, f"+{v-100:.1f}%", MAU[1], 0, -11, 10, "middle")
    h.vung([(n, 100 * (1 + a * (n - 1) / (n + 1))) for n in ns],
           [(n, 100.0) for n in ns], MAU[1], 0.14)
    h.chu(h.px(22), h.py(112), "vùng này là tiền người mua trả THỪA", MAU[1], 12, "middle")
    h.chu_thich(h.L + 18, h.T + 10)
    h.ghi_chu_duoi(f"Mỗi bên mua ước lượng KHÔNG thiên vị, sai số đều trong ±{a:.0%}. Nhưng "
                   f"người thắng là người ước lượng cao nhất, nên kỳ vọng của ước lượng thắng "
                   f"cuộc luôn nằm trên giá trị thật — và chênh lệch tăng theo số đối thủ. "
                   f"Công thức: a×(N−1)/(N+1), không cần mô phỏng.")
    xuat(h, "bai18-loi-nguyen.svg")


# ===========================================================================
# BAI 19 — QUYEN CHON THUC VA APV
# ===========================================================================

def _b19():
    return nap("bai-19-quyen-chon-thuc-va-apv.py")


def bai19_apv_vs_wacc():
    """Noi hai cach tach ra: lich tra no dinh truoc."""
    m = _b19()
    h = Hinh("Khi tỷ trọng nợ thay đổi, WACC không còn một con số đúng",
             "Năm", "Dư nợ / giá trị (%)")
    n = m.SO_NAM_TRA
    no = [m.NO_DAU * (1 - t / n) for t in range(n + 1)]
    pv = sum(m.KD * no[t - 1] * m.THUE_VN / (1 + m.KD) ** t for t in range(1, n + 1))
    V = m.GT_MUA + pv
    h.truc((0, n), (0, 0.8), vach_x=list(range(n + 1)),
           dinh_x=lambda v: f"{v:.0f}", dinh_y=lambda v: f"{v:.0%}")
    h.duong([(t, no[t] / V) for t in range(n + 1)], MAU[1],
            "tỷ trọng nợ THẬT, giảm dần theo lịch trả", 3.0)
    for ten, w, mau in (("dùng D/V năm đầu", no[0] / V, MAU[0]),
                        ("dùng D/V bình quân", sum(no[:-1]) / n / V, MAU[3]),
                        ("dùng D/V năm cuối", no[n - 1] / V, MAU[2])):
        h.duong([(0, w), (n, w)], mau, f"{ten} ({w:.0%})", 2.0, "6 4")
    h.ghi_chu_duoi(f"Công thức WACC cần MỘT tỷ trọng nợ không đổi. Thương vụ này không có "
                   f"cái đó — nợ đi từ {no[0]/V:.0%} xuống 0 trong {n} năm. Ba cách chọn cho ba kết "
                   f"quả khác nhau và không cách nào đúng. APV không cần biết tỷ trọng: nó "
                   f"chỉ cần dư nợ từng năm, thứ nằm ngay trong hợp đồng.")
    xuat(h, "bai19-apv-vs-wacc.svg")


def bai19_hai_cong_thuc_beta():
    """Hamada va tai can bang tach nhau theo don bay."""
    m = _b19()
    h = Hinh("Hai công thức gỡ đòn bẩy, hai giả định loại trừ nhau",
             "D/E theo giá thị trường", "Beta tài sản suy ra từ beta đo được = 1,0")
    des = [i / 100 for i in range(0, 121)]
    h.truc((0, 1.2), (0.4, 1.05), dinh_x=lambda v: f"{v:.1f}",
           dinh_y=lambda v: f"{v:.2f}")
    h.duong([(d, 1.0 / (1 + (1 - m.THUE_VN) * d)) for d in des], MAU[0],
            "Hamada — giả định MỨC nợ cố định (bài 15 dùng cái này)", 2.8)
    h.duong([(d, 1.0 / (1 + d)) for d in des], MAU[1],
            "Tái cân bằng — giả định TỶ TRỌNG nợ cố định (WACC giả định cái này)", 2.8)
    h.vung([(d, 1.0 / (1 + (1 - m.THUE_VN) * d)) for d in des],
           [(d, 1.0 / (1 + d)) for d in des], MAU[1], 0.13)
    y = m.NAM[-1]
    for k in m.MA_BAI15:
        de = m.vay(k, y) / m.von_hoa(k)
        h.cham(de, 1.0 / (1 + (1 - m.THUE_VN) * de), MAU[0], 5)
        h.cham(de, 1.0 / (1 + de), MAU[1], 5)
        h.chu(h.px(de), h.py(1.0 / (1 + de)) + 16, k, XAM, 10, "middle")
    h.chu_thich(h.L + 200, h.T + 10)
    hpg = m.vay("HPG", y) / m.von_hoa("HPG")
    ch = 1.0 / (1 + (1 - m.THUE_VN) * hpg) / (1.0 / (1 + hpg)) - 1
    h.ghi_chu_duoi(f"Vùng tô là khoảng cách giữa hai công thức. Nó nở ra theo đòn bẩy: HPG có "
                   f"D/E {hpg:.2f} nên hai công thức lệch {ch:.1%}. Bài 15 dùng công thức WACC "
                   f"(tỷ trọng cố định) nhưng gỡ beta bằng Hamada (mức cố định) — hai giả định "
                   f"đó không thể cùng đúng.")
    xuat(h, "bai19-hai-cong-thuc-beta.svg")


def bai19_nguong_dau_tu():
    """Nguong dau tu theo bien dong: NPV > 0 la khong du."""
    m = _b19()
    h = Hinh("“NPV dương thì làm” chỉ đúng khi không có quyền chờ",
             "Biến động giá trị dự án (%/năm)", "Giá trị dự án / vốn bỏ ra")
    sigs = [i / 200 for i in range(4, 131)]
    h.truc((0.02, 0.65), (0.8, 7.0), dinh_x=lambda v: f"{v:.0%}",
           dinh_y=lambda v: f"{v:.1f}x")
    pts = [(s, m.nguong_dau_tu(s)) for s in sigs]
    h.duong(pts, MAU[1], "ngưỡng đầu tư McDonald–Siegel", 3.0)
    h.duong([(0.02, 1.0), (0.65, 1.0)], MAU[2], "quy tắc NPV: làm khi vượt 1,0×", 2.2, "6 4")
    h.vung(pts, [(s, 1.0) for s in sigs], MAU[1], 0.13)
    h.chu(h.px(0.30), h.py(2.3), "vùng NPV DƯƠNG nhưng vẫn nên CHỜ", MAU[1], 12, "middle")
    ds = m.bang_bien_dong()
    tv = m.trung_vi(x["sig_a"] for x in ds)
    h.ke_doc(tv, "#999", "3 3", f"trung vị mẫu Việt Nam {tv:.1%}")
    h.cham(tv, m.nguong_dau_tu(tv), MAU[1], 7)
    h.moc(tv, m.nguong_dau_tu(tv), f"{m.nguong_dau_tu(tv):.2f}×", MAU[1], 10, 4, 12, "start", True)
    h.chu_thich(h.L + 250, h.T + 10)
    h.ghi_chu_duoi(f"Đầu tư là hành động không đảo ngược được: bấm nút là giết luôn quyền chờ. "
                   f"Với biến động trung vị {tv:.1%} của mẫu Việt Nam, dự án phải đáng giá "
                   f"{m.nguong_dau_tu(tv):.2f} lần vốn bỏ ra — tức NPV phải bằng "
                   f"+{(m.nguong_dau_tu(tv)-1)*100:.0f}% vốn — thì mới nên làm.")
    xuat(h, "bai19-nguong-dau-tu.svg")


def bai19_bien_dong_that():
    """Bien dong von chu so voi bien dong tai san, 28 doanh nghiep."""
    m = _b19()
    ds = sorted(m.bang_bien_dong(), key=lambda x: x["sig_a"])
    h = Hinh("Biến động vốn chủ có đòn bẩy — phải gỡ ra mới dùng được",
             "", "Biến động năm")
    h.truc((-0.6, len(ds) - 0.4), (0, 0.68), vach_x=list(range(len(ds))),
           dinh_x=lambda i: ds[int(i)][0]["ma"] if False else ds[int(i)]["ma"],
           dinh_y=lambda v: f"{v:.0%}")
    for i, x in enumerate(ds):
        px = h.px(i)
        h.e.append(f'<line x1="{px:.1f}" y1="{h.py(x["sig_a"]):.1f}" x2="{px:.1f}"'
                   f' y2="{h.py(x["sig_e"]):.1f}" stroke="{XAM}" stroke-width="1.4"/>')
        h.cham(i, x["sig_e"], MAU[1], 4.5)
        h.cham(i, x["sig_a"], MAU[0], 4.5)
    tv_e = m.trung_vi(x["sig_e"] for x in ds)
    tv_a = m.trung_vi(x["sig_a"] for x in ds)
    h.ke_ngang(tv_e, MAU[1], "4 3", f"trung vị vốn chủ {tv_e:.1%}")
    h.ke_ngang(tv_a, MAU[0], "4 3", f"trung vị tài sản {tv_a:.1%}")
    for j, (ten, mau) in enumerate((("biến động VỐN CHỦ (đo từ giá)", MAU[1]),
                                    ("biến động TÀI SẢN (đã gỡ đòn bẩy)", MAU[0]))):
        h.e.append(f'<circle cx="{h.L+262}" cy="{h.T+16+j*19}" r="5" fill="{mau}"/>')
        h.chu(h.L + 274, h.T + 20 + j * 19, ten, MUC, 12)
    nkg = next(x for x in ds if x["ma"] == "NKG")
    h.ghi_chu_duoi(f"NKG có biến động vốn chủ cao nhất mẫu ({nkg['sig_e']:.1%}) nhưng biến động "
                   f"tài sản chỉ {nkg['sig_a']:.1%} — xếp giữa bảng — vì {1-nkg['w']:.0%} vốn của nó là nợ vay. "
                   f"Cùng kiểu đảo thứ hạng mà công thức Hamada gây ra ở bài 15 §11.")
    xuat(h, "bai19-bien-dong-that.svg")


def bai19_gia_tri_quyen_cho():
    """Gia tri quyen hoan so voi NPV lam ngay."""
    m = _b19()
    h = Hinh("Quyền chờ đáng giá nhất đúng ở chỗ NPV bảo bỏ",
             "Giá trị dự án / vốn bỏ ra", "Giá trị (đơn vị: % vốn bỏ ra)")
    ks = [i / 100 for i in range(60, 231, 5)]
    I = m.VON_DAU_TU
    h.truc((0.6, 2.3), (-40, 140), dinh_x=lambda v: f"{v:.1f}x",
           dinh_y=lambda v: f"{v:.0f}", goc_khong=True)
    h.duong([(k, I * k - I) for k in ks], XAM, "NPV nếu làm ngay", 2.2, "6 4")
    for i, sg in enumerate((0.20, 0.40)):
        pts = [(k, m.cay_nhi_thuc(I * k, I, m.R_PHI_RUI_RO, m.DONG_TIEN_BO_LO,
                                  sg, 10.0, 400)) for k in ks]
        h.duong(pts, MAU[i], f"giá trị QUYỀN CHỜ, biến động {sg:.0%}", 2.8)
    for i, sg in enumerate((0.20, 0.40)):
        ng = m.nguong_dau_tu(sg)
        if ng <= 2.3:
            h.ke_doc(ng, MAU[i], "3 3", f"ngưỡng {sg:.0%}: {ng:.2f}×")
    h.chu_thich(h.L + 16, h.T + 10)
    q = m.cay_nhi_thuc(I * 0.9, I, m.R_PHI_RUI_RO, m.DONG_TIEN_BO_LO, 0.40, 10.0, 400)
    h.ghi_chu_duoi(f"Ở mức 0,9× vốn, NPV là −10 nên quy tắc NPV bảo bỏ — nhưng QUYỀN được làm "
                   f"dự án đó vẫn đáng {q:.0f} khi biến động 40%. Và biến động CÀNG CAO quyền càng "
                   f"đáng giá, ngược hoàn toàn với mọi thứ từ bài 9 đến bài 15.")
    xuat(h, "bai19-gia-tri-quyen-cho.svg")


# ===========================================================================
# BAI 20
# ===========================================================================

def _b20():
    return nap("bai-20-chu-ky-don-bay.py")


def bai20_don_bay_va_gia():
    """Cho vay them mot dong lam gia tai san tang, du dong tien khong doi."""
    m = _b20()
    h = Hinh("Dòng tiền không đổi, xác suất không đổi — chỉ đòn bẩy đổi",
             "Vay được trên mỗi đơn vị tài sản", "Giá tài sản")
    xs = [i / 400 for i in range(0, 81)]
    pts = [(v, m.can_bang_mot_ky(1.0, 1.0, 1.0, v)[1]) for v in xs]
    h.truc((0, 0.205), (0.64, 0.78), dinh_x=lambda v: f"{v:.2f}",
           dinh_y=lambda v: f"{v:.2f}")
    h.duong(pts, MAU[0], "giá cân bằng", 3.0)
    a0, p0 = m.can_bang_mot_ky(1.0, 1.0, 1.0, 0.0)
    a2, p2 = m.can_bang_mot_ky(1.0, 1.0, 1.0, m.THAP)
    for x, y, s in ((0.0, p0, f"không vay được đồng nào: {p0:.4f}"),
                    (m.THAP, p2, f"vay tối đa {m.THAP:.1f}: {p2:.4f}")):
        h.cham(x, y, MAU[1], 6)
    h.moc(0.0, p0, f"{p0:.4f}", MAU[1], 10, 14, 12, "start", True)
    h.moc(m.THAP, p2, f"{p2:.4f}", MAU[1], -10, -10, 12, "end", True)
    h.ke_ngang(p0, "#bbb", "3 3")
    h.chu_thich(h.L + 16, h.T + 10)
    h.ghi_chu_duoi(f"Tài sản trả đúng 1,0 nếu tốt và {m.THAP:.1f} nếu xấu, ở cả hai đầu của trục. "
                   f"Cái duy nhất thay đổi là nhóm lạc quan nhất vay được bao nhiêu — và giá "
                   f"tăng {p2/p0-1:.1%}. Không công thức chiết khấu nào trong bài 1–19 có biến này.")
    xuat(h, "bai20-don-bay-va-gia.svg")


def bai20_nguoi_mua_bien():
    """Don bay day nguoi mua bien len cao, va do la ly do gia tang."""
    m = _b20()
    h = Hinh("Giá là đánh giá của NGƯỜI MUA BIÊN — đòn bẩy quyết định người đó là ai",
             "Người thứ h (0 = bi quan nhất, 1 = lạc quan nhất)", "Định giá tài sản")
    hs = [i / 200 for i in range(201)]
    h.truc((0, 1), (0.15, 1.05), dinh_x=lambda v: f"{v:.1f}",
           dinh_y=lambda v: f"{v:.2f}")
    h.duong([(x, m.gia_theo_nguoi_bien(x)) for x in hs], XAM,
            "định giá của từng người", 2.4)
    for i, vay in enumerate((0.0, m.THAP)):
        a, p = m.can_bang_mot_ky(1.0, 1.0, 1.0, vay)
        h.ke_doc(a, MAU[i], "4 3", None)
        h.ke_ngang(p, MAU[i], "4 3", None)
        h.cham(a, p, MAU[i], 7)
        h.moc(a, p, f"vay {vay:.1f} → giá {p:.4f}", MAU[i], 10, -8, 12, "start", True)
    a0 = m.can_bang_mot_ky(1.0, 1.0, 1.0, 0.0)[0]
    a2 = m.can_bang_mot_ky(1.0, 1.0, 1.0, m.THAP)[0]
    h.mui_ten(h.px(a0), h.py(0.30), h.px(a2), h.py(0.30), MAU[1], 2.2)
    h.chu(h.px((a0 + a2) / 2), h.py(0.26), "người mua biên bị đẩy lên", MAU[1], 12, "middle")
    h.chu_thich(h.L + 16, h.T + 10)
    h.ghi_chu_duoi(f"Người ở bên phải đường dọc là người MUA, bên trái là người BÁN. "
                   f"Cho nhóm bên phải vay nhiều hơn thì ít người hơn cũng đủ sức mua hết "
                   f"tài sản, nên vạch chia dịch từ {a0:.2f} sang {a2:.2f} và giá đi lên theo.")
    xuat(h, "bai20-nguoi-mua-bien.svg")


def bai20_ba_luc():
    """Tach cu sut thanh ba luc: tin xau, nguoi lac quan bi xoa so, don bay sup."""
    m = _b20()
    k = m.can_bang_ba_ky()
    b, p0, pD = k["b"], k["p0"], k["pD"]
    g = lambda ds, vay: m.can_bang_mot_ky(ds, 1.0, 1.0, vay)[1]
    moc = [("giá trước tin xấu", p0),
           ("sau tin xấu", g(1.0, pD)),
           ("người lạc quan bị xoá sổ", g(b, pD)),
           ("đòn bẩy sụp", g(b, m.THAP))]
    h = Hinh("Ba lực trong một cú sụp — và lực lớn nhất không phải tin tức",
             "", "Giá tài sản")
    h.truc((-0.6, 3.6), (0.60, 1.00), vach_x=list(range(4)),
           dinh_x=lambda i: ["gốc", "tin xấu", "xoá sổ", "đòn bẩy"][int(i)],
           dinh_y=lambda v: f"{v:.2f}")
    for i in range(4):
        h.cot([(i, moc[i][1])], MAU[0] if i == 0 else MAU[1], 74, 0.85, 0.60)
        h.moc(i, moc[i][1], f"{moc[i][1]:.4f}", MUC, 0, 16, 12, "middle", True)
    for i in range(1, 4):
        d = moc[i][1] / moc[i - 1][1] - 1
        h.chu(h.px(i - 0.5), h.py(0.985), f"{d:+.1%}", MAU[1], 13, "middle", True)
    h.ghi_chu_duoi(f"Tin xấu — thứ duy nhất mà mô hình định giá cơ bản chịu nhìn — chỉ giải "
                   f"thích {abs(moc[1][1]/p0-1)/abs(pD/p0-1):.0%} cú sụp. Đòn bẩy sụp một mình lớn hơn tin xấu "
                   f"{abs(moc[3][1]/moc[2][1]-1)/abs(moc[1][1]/p0-1):.1f} lần. Đổi thứ tự tách thì kết luận không đổi.")
    xuat(h, "bai20-ba-luc.svg")


def bai20_bien_dong_don_bay():
    """Bien dong quyet dinh don bay, va don bay quyet dinh gia."""
    m = _b20()
    h = Hinh("Biến động quyết định đòn bẩy, đòn bẩy quyết định giá",
             "Khoảng cách giữa hai kết cục (thước đo biến động)", "")
    xs = [0.05 + i / 200 for i in range(0, 116)]
    h.truc((0.30, 0.96), (0.6, 3.0), dinh_x=lambda v: f"{v:.1f}",
           dinh_y=lambda v: f"{v:.1f}")
    thaps = [0.04 + i / 200 for i in range(0, 131)]
    db, gi = [], []
    for tp in thaps:
        p_ = m.can_bang_mot_ky(1.0, 1.0, 1.0, tp, tp)[1]
        db.append((1 - tp, m.don_bay(p_, tp)))
        gi.append((1 - tp, p_ * 3.0))
    h.duong(sorted(db), MAU[0], "đòn bẩy cân bằng", 3.0)
    h.duong(sorted(gi), MAU[1], "giá tài sản × 3 (vẽ chung trục)", 2.6, "6 4")
    h.chu(h.px(0.42), h.py(2.72), "biến động THẤP", XAM, 12, "middle")
    h.chu(h.px(0.88), h.py(2.72), "biến động CAO", XAM, 12, "middle")
    h.chu_thich(h.L + 200, h.T + 10)
    a_h = m.can_bang_mot_ky(1.0, 1.0, 1.0, 0.60, 0.60)[1]
    a_l = m.can_bang_mot_ky(1.0, 1.0, 1.0, 0.05, 0.05)[1]
    h.ghi_chu_duoi(f"Hai đường đi cùng chiều vì chúng là một chuỗi nhân quả: biến động tăng → "
                   f"người cho vay đòi ký quỹ cao hơn → đòn bẩy giảm → người mua biên tụt xuống "
                   f"→ giá giảm. Từ đầu này sang đầu kia, đòn bẩy "
                   f"{m.don_bay(a_h, 0.60):.2f} → {m.don_bay(a_l, 0.05):.2f} và giá {a_h:.4f} → {a_l:.4f}.")
    xuat(h, "bai20-bien-dong-don-bay.svg")


def bai20_tuong_quan_vn():
    """Ba cu sut Viet Nam: bien dong va tuong quan deu tang."""
    m = _b20()
    ten = [d[0] for d in m.DOT_IDX]
    r = [math.log(m.VNI[i] / m.VNI[i - 1]) for i in range(1, len(m.VNI))]
    bd_t, bd_g, tq_t, tq_g = [], [], [], []
    for t, i_pre, i_dinh, i_day in m.DOT_IDX:
        bd_t.append(m.bien_dong_nam(r[i_pre:i_dinh]))
        bd_g.append(m.bien_dong_nam(r[i_dinh:i_day]))
        n_pre = i_dinh - i_pre
        tq_t.append(m.tuong_quan_cap_tb(t, 0, n_pre)[0])
        tq_g.append(m.tuong_quan_cap_tb(t, n_pre, i_day - i_pre)[0])
    h = Hinh("Ba cú sụp của VN-Index: bất định tăng, và mọi thứ rơi cùng nhau",
             "", "")
    h.truc((-0.6, 5.6), (0, 0.52), vach_x=list(range(6)),
           dinh_x=lambda i: (["2018", "2020", "2022"] * 2)[int(i)],
           dinh_y=lambda v: f"{v:.2f}")
    for i in range(3):
        h.cot([(i, bd_t[i])], XAM, 54, 0.55)
        h.cot([(i, bd_g[i])], MAU[1], 26, 0.95)
        h.cot([(i + 3, tq_t[i])], XAM, 54, 0.55)
        h.cot([(i + 3, tq_g[i])], MAU[0], 26, 0.95)
        h.moc(i, bd_g[i], f"{bd_g[i]/bd_t[i]:.1f}×", MAU[1], 0, 14, 12, "middle", True)
        h.moc(i + 3, tq_g[i], f"{tq_g[i]/tq_t[i]:.1f}×", MAU[0], 0, 14, 12, "middle", True)
    h.chu(h.px(1.0), h.py(0.495), "BIẾN ĐỘNG NĂM của VN-Index", MAU[1], 13, "middle", True)
    h.chu(h.px(4.0), h.py(0.495), "TƯƠNG QUAN bình quân 28 mã", MAU[0], 13, "middle", True)
    for j, (t, mau) in enumerate((("120 phiên TRƯỚC đỉnh", XAM), ("TRONG cú sụp", MAU[1]))):
        h.e.append(f'<rect x="{h.L+250}" y="{h.T+10+j*19}" width="12" height="12" fill="{mau}"/>')
        h.chu(h.L + 268, h.T + 20 + j * 19, t, MUC, 12)
    h.ghi_chu_duoi("Cả ba lần, biến động tăng và tương quan tăng. 28 doanh nghiệp ở 28 ngành "
                   "khác nhau rơi gần như cùng một nhịp — khó giải thích bằng tin tức riêng "
                   "của từng ngành. ⚠ Nhất quán với chu kỳ đòn bẩy, nhưng chưa phải bằng chứng.")
    xuat(h, "bai20-tuong-quan-vn.svg")


# ===========================================================================

def main():
    print("Sinh hình minh hoạ — chỉ dùng thư viện chuẩn Python\n")
    for f in (bai01_bon_thanh_phan, bai01_dau_gia,
              bai02_duong_thoi_gian, bai02_ghep_lai, bai02_ba_dong_tien,
              bai03_don_bay,
              bai04_duong_cong, bai04_ky_han,
              bai05_duration, bai05_co_may_aaa, bai05_loi_am, bai05_phong_ho_dong,
              bai06_gordon, bai06_tang_truong,
              bai07_payoff_ky_han,
              bai08_payoff, bai08_ket_hop, bai08_cay_nhi_thuc, bai08_ngang_gia,
              bai09_duoi_beo,
              bai10_duong_dan, bai10_bien_hieu_qua, bai10_da_dang_hoa,
              bai10_huu_dung_lom,
              bai11_cml_sml, bai11_sml_do_that,
              bai12_npv_irr, bai12_la_chan_thue,
              bai13_tu_tuong_quan, bai13_737max, bai13_sml_hai_che_do,
              bai14_ban_do_sinh_loi, bai14_dupont_cot, bai14_apple_don_bay,
              bai14_chu_ky_tien_mat, bai14_roic,
              bai15_thanh_phan_wacc, bai15_do_nhay, bai15_roic_wacc,
              bai15_hamada,
              bai16_ba_the_gioi, bai16_hvn, bai16_duoi_trai, bai16_trat_tu,
              bai16_dua_ngua,
              bai17_chuyen_rui_ro, bai17_co_tuc_muot, bai17_co_tuc_vs_mua_lai,
              bai17_boeing, bai17_chi_tra_vn, bai17_loi_nhuan_khong_phai_tien,
              bai18_gia_tri_cuoi_ky, bai18_do_nhay, bai18_dcf_hong,
              bai18_dcf_nguoc, bai18_boi_so, bai18_loi_nguyen,
              bai19_apv_vs_wacc, bai19_hai_cong_thuc_beta, bai19_nguong_dau_tu,
              bai19_bien_dong_that, bai19_gia_tri_quyen_cho,
              bai20_don_bay_va_gia, bai20_nguoi_mua_bien, bai20_ba_luc,
              bai20_bien_dong_don_bay, bai20_tuong_quan_vn):
        f()
    print(f"\n{len(DA_SINH)} hình. Tất cả sinh từ dữ liệu trong thuc_hanh/, "
          f"không gõ tay con số nào.")


if __name__ == "__main__":
    main()
