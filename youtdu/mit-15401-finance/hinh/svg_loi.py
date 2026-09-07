"""Loi sinh hinh SVG — chi dung thu vien chuan Python.

Khong cai goi nao. Khong matplotlib. SVG la van ban nen vao git sach, hien thi
duoc trong GitHub, Obsidian va VS Code, va phong to bao nhieu cung khong vo.

Cach dung:
    from svg_loi import Hinh
    h = Hinh("Tieu de", "nhan truc x", "nhan truc y")
    h.truc((0, 10), (-5, 5))
    h.duong([(0, 0), (10, 4)], MAU[0], "ten duong")
    h.ghi("ten-file.svg")
"""

import math
import pathlib
import xml.sax.saxutils as _x

THU_MUC = pathlib.Path(__file__).resolve().parent

# Bang mau: phan biet duoc ca khi in den trang va voi nguoi mu mau do-luc.
MAU = ["#1a6fb5", "#c0392b", "#1f8a4c", "#d98c00", "#7a4fa3", "#00868b"]
XAM, XAM_NHAT, MUC = "#666", "#e8e8e4", "#111"
NEN = "#fdfdfb"


def _e(s) -> str:
    """Thoat ky tu dac biet cua XML."""
    return _x.escape(str(s))


def _so(v: float, n: int = 1) -> str:
    return f"{v:.{n}f}".rstrip("0").rstrip(".") if n else f"{v:.0f}"


class Hinh:
    """Mot khung ve SVG voi he toa do tuyen tinh."""

    def __init__(self, tieu_de: str, nhan_x: str = "", nhan_y: str = "",
                 rong: int = 760, cao: int = 480,
                 le=(74, 48, 46, 96)):
        self.W, self.H = rong, cao
        self.L, self.R, self.T, self.B = le
        self.e: list[str] = [
            f'<rect width="{self.W}" height="{self.H}" fill="{NEN}"/>']
        if tieu_de:
            self.chu(self.W / 2, 26, tieu_de, MUC, 16, "middle", True)
        self.nhan_x, self.nhan_y = nhan_x, nhan_y
        self.px = self.py = None
        self._chu_thich: list[tuple[str, str, bool]] = []

    # ---------------------------------------------------------------- truc
    def truc(self, tx, ty, vach_x=None, vach_y=None, dinh_x=None, dinh_y=None,
             luoi=True, goc_khong=False):
        """Dat he toa do. tx, ty la (min, max). dinh_* la ham dinh dang nhan."""
        x0, x1 = tx
        y0, y1 = ty
        assert x1 > x0 and y1 > y0, "khoang truc phai duong"
        self.px = lambda v: self.L + (v - x0) / (x1 - x0) * (self.W - self.L - self.R)
        self.py = lambda v: self.H - self.B - (v - y0) / (y1 - y0) * (self.H - self.T - self.B)
        vach_x = vach_x if vach_x is not None else _vach(x0, x1)
        vach_y = vach_y if vach_y is not None else _vach(y0, y1)
        dx = dinh_x or (lambda v: _so(v, 2))
        dy = dinh_y or (lambda v: _so(v, 2))
        for v in vach_x:
            if luoi:
                self.e.append(f'<line x1="{self.px(v):.1f}" y1="{self.T}"'
                              f' x2="{self.px(v):.1f}" y2="{self.H - self.B}"'
                              f' stroke="{XAM_NHAT}" stroke-width="1"/>')
            self.chu(self.px(v), self.H - self.B + 18, dx(v), XAM, 11, "middle")
        for v in vach_y:
            if luoi:
                self.e.append(f'<line x1="{self.L}" y1="{self.py(v):.1f}"'
                              f' x2="{self.W - self.R}" y2="{self.py(v):.1f}"'
                              f' stroke="{XAM_NHAT}" stroke-width="1"/>')
            self.e.append(f'<text x="{self.L - 9}" y="{self.py(v):.1f}" dy="4"'
                          f' font-size="11" text-anchor="end" fill="{XAM}"'
                          f' font-family="Helvetica,Arial,sans-serif">{_e(dy(v))}</text>')
        if goc_khong:
            if y0 < 0 < y1:
                self.e.append(f'<line x1="{self.L}" y1="{self.py(0):.1f}"'
                              f' x2="{self.W - self.R}" y2="{self.py(0):.1f}"'
                              f' stroke="#999" stroke-width="1.5"/>')
            if x0 < 0 < x1:
                self.e.append(f'<line x1="{self.px(0):.1f}" y1="{self.T}"'
                              f' x2="{self.px(0):.1f}" y2="{self.H - self.B}"'
                              f' stroke="#999" stroke-width="1.5"/>')
        if self.nhan_x:
            self.chu(self.W / 2, self.H - self.B + 34, self.nhan_x, "#333", 12, "middle")
        if self.nhan_y:
            y = (self.T + self.H - self.B) / 2
            self.e.append(f'<text x="15" y="{y:.1f}" font-size="12" fill="#333"'
                          f' text-anchor="middle" font-family="Helvetica,Arial,sans-serif"'
                          f' transform="rotate(-90 15 {y:.1f})">{_e(self.nhan_y)}</text>')
        return self

    # -------------------------------------------------------------- ve hinh
    def duong(self, diem, mau, ten=None, rong=2.4, net=None, mo=1.0):
        assert self.px, "goi truc() truoc"
        d = " ".join(("M" if i == 0 else "L") + f"{self.px(x):.1f},{self.py(y):.1f}"
                     for i, (x, y) in enumerate(diem))
        dash = f' stroke-dasharray="{net}"' if net else ""
        self.e.append(f'<path d="{d}" fill="none" stroke="{mau}" stroke-width="{rong}"'
                      f' stroke-linejoin="round" stroke-linecap="round"'
                      f' opacity="{mo}"{dash}/>')
        if ten:
            self._chu_thich.append((ten, mau, bool(net)))
        return self

    def vung(self, diem_tren, diem_duoi, mau, mo=0.16):
        d = (" ".join(("M" if i == 0 else "L") + f"{self.px(x):.1f},{self.py(y):.1f}"
                      for i, (x, y) in enumerate(diem_tren))
             + " " + " ".join(f"L{self.px(x):.1f},{self.py(y):.1f}"
                              for x, y in reversed(diem_duoi)) + " Z")
        self.e.append(f'<path d="{d}" fill="{mau}" opacity="{mo}" stroke="none"/>')
        return self

    def cot(self, diem, mau, rong_cot=None, mo=0.85, day=0.0):
        assert self.px, "goi truc() truoc"
        if rong_cot is None and len(diem) > 1:
            rong_cot = abs(self.px(diem[1][0]) - self.px(diem[0][0])) * 0.8
        rong_cot = rong_cot or 6
        for x, y in diem:
            y0, y1 = sorted((self.py(day), self.py(y)))
            self.e.append(f'<rect x="{self.px(x) - rong_cot/2:.1f}" y="{y0:.1f}"'
                          f' width="{rong_cot:.1f}" height="{max(y1-y0, 0.5):.1f}"'
                          f' fill="{mau}" opacity="{mo}"/>')
        return self

    def cham(self, x, y, mau, r=5, vien="#fff"):
        self.e.append(f'<circle cx="{self.px(x):.1f}" cy="{self.py(y):.1f}" r="{r}"'
                      f' fill="{mau}" stroke="{vien}" stroke-width="1.6"/>')
        return self

    def moc(self, x, y, s, mau=MUC, dx=8, dy=-8, co=11, neo="start", dam=False):
        """Nhan gan mot diem du lieu. Chuoi co \n se duoc tach thanh nhieu dong."""
        for i, dong in enumerate(str(s).split("\n")):
            self.chu(self.px(x) + dx, self.py(y) + dy + i * (co + 3), dong, mau, co, neo, dam)
        return self

    def ke_doc(self, x, mau="#bbb", net="4 4", nhan=None):
        self.e.append(f'<line x1="{self.px(x):.1f}" y1="{self.T}"'
                      f' x2="{self.px(x):.1f}" y2="{self.H - self.B}"'
                      f' stroke="{mau}" stroke-width="1.5" stroke-dasharray="{net}"/>')
        if nhan:
            xt = min(max(self.px(x), self.L + len(nhan) * 2.8),
                     self.W - self.R - len(nhan) * 2.8)
            self.chu(xt, self.T - 6, nhan, XAM, 11, "middle")
        return self

    def ke_ngang(self, y, mau="#bbb", net="4 4", nhan=None):
        self.e.append(f'<line x1="{self.L}" y1="{self.py(y):.1f}"'
                      f' x2="{self.W - self.R}" y2="{self.py(y):.1f}"'
                      f' stroke="{mau}" stroke-width="1.5" stroke-dasharray="{net}"/>')
        if nhan:
            self.chu(self.W - self.R - 4, self.py(y) - 6, nhan, XAM, 11, "end")
        return self

    def mui_ten(self, x1, y1, x2, y2, mau=MUC, rong=1.8):
        a = math.atan2(self.py(y2) - self.py(y1), self.px(x2) - self.px(x1))
        X2, Y2 = self.px(x2), self.py(y2)
        p = " ".join(f"{X2 - 9*math.cos(a - t):.1f},{Y2 - 9*math.sin(a - t):.1f}"
                     for t in (0.42, -0.42))
        self.e.append(f'<line x1="{self.px(x1):.1f}" y1="{self.py(y1):.1f}"'
                      f' x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{mau}" stroke-width="{rong}"/>')
        self.e.append(f'<polygon points="{X2:.1f},{Y2:.1f} {p}" fill="{mau}"/>')
        return self

    def hop(self, x, y, w, h, mau=MUC, nen="#fff", nhan=None, co=12):
        """Hop chu nhat toa do MAN HINH (khong qua truc) — dung cho so do."""
        self.e.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5"'
                      f' fill="{nen}" stroke="{mau}" stroke-width="2"/>')
        if nhan:
            for i, dong in enumerate(nhan.split("\n")):
                self.chu(x + w / 2, y + h / 2 + (i - (len(nhan.split("\n")) - 1) / 2) * (co + 3) + 4,
                         dong, mau, co, "middle", i == 0)
        return self

    def chu(self, x, y, s, mau=MUC, co=12, neo="start", dam=False, nghieng=False):
        if "\n" in str(s):
            for i, dong in enumerate(str(s).split("\n")):
                self.chu(x, y + i * (co + 3), dong, mau, co, neo, dam, nghieng)
            return self
        self.e.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{co}" fill="{mau}"'
            f' text-anchor="{neo}" font-family="Helvetica,Arial,sans-serif"'
            + (' font-weight="600"' if dam else "")
            + (' font-style="italic"' if nghieng else "")
            + f'>{_e(s)}</text>')
        return self

    def chu_thich(self, x=None, y=None, cot=1):
        """In bang chu thich cho cac duong da dat ten."""
        if not self._chu_thich:
            return self
        x = self.L + 14 if x is None else x
        y = self.T + 18 if y is None else y
        for i, (ten, mau, net) in enumerate(self._chu_thich):
            cx = x + (i % cot) * 210
            cy = y + (i // cot) * 19
            dash = ' stroke-dasharray="5 4"' if net else ""
            self.e.append(f'<line x1="{cx}" y1="{cy - 4}" x2="{cx + 24}" y2="{cy - 4}"'
                          f' stroke="{mau}" stroke-width="2.6"{dash}/>')
            self.chu(cx + 31, cy, ten, MUC, 12)
        return self

    def ghi_chu_duoi(self, s, co=11):
        """Ghi chu duoi hinh, TU NGAT DONG cho vua be rong."""
        moi_dong = max(20, int((self.W - 40) / (co * 0.53)))
        dong, cur = [], ""
        for tu in str(s).split():
            if cur and len(cur) + 1 + len(tu) > moi_dong:
                dong.append(cur); cur = tu
            else:
                cur = f"{cur} {tu}".strip()
        if cur:
            dong.append(cur)
        for i, d in enumerate(dong[:3]):
            self.chu(20, self.H - self.B + 58 + i * (co + 5), d, "#888", co)
        return self

    # ----------------------------------------------------------------- xuat
    def ghi(self, ten: str) -> pathlib.Path:
        p = THU_MUC / ten
        p.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}" height="{self.H}"'
            f' viewBox="0 0 {self.W} {self.H}" role="img">\n'
            + "\n".join(self.e) + "\n</svg>\n")
        return p


def _vach(a: float, b: float, n: int = 6) -> list[float]:
    """Chon cac moc chia tron dep tren khoang [a, b]."""
    tho = (b - a) / n
    mu = math.floor(math.log10(tho))
    for k in (1, 2, 2.5, 5, 10):
        buoc = k * 10 ** mu
        if buoc >= tho:
            break
    v, ra = math.ceil(a / buoc) * buoc, []
    while v <= b + buoc * 1e-9:
        ra.append(round(v, 10))
        v += buoc
    return ra


def nap(ten_file: str):
    """Nap mot module trong thuc_hanh/ de dung lai du lieu nhung san.

    Bai 1-9 viet dang script phang nen nap module se chay het va in ra man hinh;
    ta nuot phan in do di, chi giu lai cac bien du lieu.
    """
    import contextlib, importlib.util, io
    p = THU_MUC.parent / "thuc_hanh" / ten_file
    spec = importlib.util.spec_from_file_location(p.stem.replace("-", "_"), p)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m
