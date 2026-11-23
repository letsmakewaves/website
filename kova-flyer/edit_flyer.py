"""Edit KOVA grand opening flyer:
1. Address line -> "DOORS 10 PM · 30 OLEH ROAD, SAPELE, DELTA STATE"
2. "KOVA LIFESTYLE" eyebrow above GRAND OPENING -> bolder
"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC, OUT = sys.argv[1], sys.argv[2]
FONTS = "/tmp/claude-0/-home-user-website/ecbfb15b-afbc-52ca-9c2d-001ed6e55f7a/scratchpad/fonts/package/files/montserrat-latin-%d-normal.woff"
SS = 4  # supersampling for crisp text

img = Image.open(SRC).convert("RGB")
A = np.asarray(img).astype(np.float64)
W, H = img.size


# ---------- background patching ----------
def patch_band(y0, y1, x0, x1, search_dy, ref_cols):
    """Replace rows y0..y1 (cols x0..x1) with a shifted copy of nearby background.
    Shift chosen so the diagonal line texture lines up on text-free reference columns."""
    best = None
    for dy in search_dy:
        for dx in range(-8, 9):
            err = 0
            for c0, c1 in ref_cols:
                tgt = A[y0:y1, c0:c1]
                src = A[y0 + dy:y1 + dy, c0 + dx:c1 + dx]
                err += np.abs(tgt - src).mean()
            if best is None or err < best[0]:
                best = (err, dy, dx)
    _, dy, dx = best
    src = A[y0 + dy:y1 + dy, x0 + dx:x1 + dx].copy()
    # match the radial-gradient brightness: per-row gain from reference columns
    tgt_ref = np.concatenate([A[y0:y1, c0:c1] for c0, c1 in ref_cols], 1).mean(1)
    src_ref = np.concatenate([A[y0 + dy:y1 + dy, c0 + dx:c1 + dx] for c0, c1 in ref_cols], 1).mean(1)
    src *= (tgt_ref / np.maximum(src_ref, 1))[:, None, :]
    # feathered blend so the patch edges are invisible
    h, w = y1 - y0, x1 - x0
    f = 10
    wy = np.clip(np.minimum(np.arange(h), np.arange(h)[::-1]) / f, 0, 1)
    wx = np.clip(np.minimum(np.arange(w), np.arange(w)[::-1]) / f, 0, 1)
    m = (wy[:, None] * wx[None, :])[..., None]
    A[y0:y1, x0:x1] = A[y0:y1, x0:x1] * (1 - m) + src * m
    print(f"patched {y0}-{y1}: dy={dy} dx={dx} err={best[0]:.2f}")


# ---------- tracked text ----------
def layout(runs, size, weight, tracking):
    """runs: list of (text, rgb). Returns per-glyph (char, rgb, x) and total ink width."""
    # a run may carry its own weight: (text, rgb[, weight])
    fonts = {}
    def F(w):
        if w not in fonts:
            fonts[w] = ImageFont.truetype(FONTS % w, size * SS)
        return fonts[w]
    glyphs, x = [], 0.0
    chars = [(ch, r[1], F(r[2] if len(r) > 2 else weight)) for r in runs for ch in r[0]]
    for i, (ch, col, f) in enumerate(chars):
        glyphs.append((ch, col, x, f))
        x += f.getlength(ch) + (tracking * SS if i < len(chars) - 1 else 0)
    return F(weight), glyphs, x


def draw_text(runs, size, weight, tracking, cx, cap_top, glow=0):
    font, glyphs, total = layout(runs, size, weight, tracking)
    pad = 40 * SS
    cw, ch_ = int(total + 2 * pad), int(size * SS * 2 + 2 * pad)
    color = Image.new("RGB", (cw, ch_), 0)
    alpha = Image.new("L", (cw, ch_), 0)
    dc, da = ImageDraw.Draw(color), ImageDraw.Draw(alpha)
    for g, col, x, f in glyphs:
        dc.text((pad + x, pad), g, font=f, fill=col)
        da.text((pad + x, pad), g, font=f, fill=255)
    # tight ink box for exact placement
    bx0, by0, bx1, by1 = alpha.getbbox()
    cap_h = font.getbbox("H")[3] - font.getbbox("H")[1]
    ink_cap_top = pad + font.getbbox("H")[1]
    color = color.resize((cw // SS, ch_ // SS), Image.LANCZOS)
    alpha = alpha.resize((cw // SS, ch_ // SS), Image.LANCZOS)
    ink_w = (bx1 - bx0) / SS
    ox = round(cx - ink_w / 2 - bx0 / SS)
    oy = round(cap_top - ink_cap_top / SS)
    col = np.asarray(color).astype(np.float64)
    al = np.asarray(alpha).astype(np.float64)[..., None] / 255
    # recover un-premultiplied colour
    col = np.where(al > 0, col / np.maximum(al, 1e-6), 0)
    if glow:
        g = np.asarray(alpha.filter(ImageFilter.GaussianBlur(glow))).astype(np.float64)[..., None] / 255
        glow_col = np.array([70, 120, 220.0])
        region = A[oy:oy + al.shape[0], ox:ox + al.shape[1]]
        region[:] = region + (glow_col - region) * g * 0.35
    region = A[oy:oy + al.shape[0], ox:ox + al.shape[1]]
    region[:] = region * (1 - al) + col * al
    print(f"drew text ink x {ox + bx0 / SS:.0f}-{ox + bx1 / SS:.0f}, cap height {cap_h / SS:.1f}")


def fit(runs, weight, cap_target, width_target):
    """find font size giving cap_target px cap height and tracking giving width_target ink width"""
    size = cap_target / 0.70
    for _ in range(5):
        f = ImageFont.truetype(FONTS % weight, round(size * SS))
        b = f.getbbox("H")
        size *= cap_target / ((b[3] - b[1]) / SS)
    size = round(size)
    lo, hi = 0.0, 40.0
    for _ in range(40):
        t = (lo + hi) / 2
        font, glyphs, _ = layout(runs, size, weight, t)
        last_ch, _, last_x, _ = glyphs[-1]
        first_b = font.getbbox(glyphs[0][0])
        last_b = font.getbbox(last_ch)
        ink = (last_x + last_b[2] - first_b[0]) / SS
        lo, hi = (t, hi) if ink < width_target else (lo, t)
    return size, (lo + hi) / 2


WHITE = (240, 243, 249)
BLUE = (124, 196, 255)

# ===== 1. ADDRESS LINE =====
# measure the original style: "DOORS 10 PM · 30 OLEH ROAD, OFF AWOLOWO" ink 426..1735, caps 2130..2155
old_runs = [("DOORS 10 PM", BLUE, 600), (" · 30 OLEH ROAD, OFF AWOLOWO", WHITE)]
a_size, a_track = fit(old_runs, 500, 26, 1735 - 426 + 1)
print("address style: size", a_size, "tracking", round(a_track, 2))

patch_band(2112, 2180, 300, 1870, range(52, 76), [(150, 380), (1780, 2010)])
new_runs = [("DOORS 10 PM", BLUE, 600), (" · 30 OLEH ROAD, SAPELE, DELTA STATE", WHITE)]
# slightly tighter tracking so the longer line stays inside the GRAND OPENING width
draw_text(new_runs, a_size, 500, a_track * 0.9, W / 2, 2130)

# ===== 2. KOVA LIFESTYLE (bolder) =====
# original: ink 783..1377, caps 1648..1671, regular weight, colour ~(201,206,216)
k_runs = [("KOVA  LIFESTYLE", (226, 231, 240))]
k_size, k_track = fit([("KOVA  LIFESTYLE", WHITE)], 400, 24, 1377 - 783 + 1)
print("kova style: size", k_size, "tracking", round(k_track, 2))
patch_band(1636, 1684, 700, 1460, range(-48, -30), [(560, 700), (1460, 1600)])
draw_text(k_runs, k_size, 600, k_track * 0.97, W / 2, 1648, glow=6)

Image.fromarray(np.clip(A, 0, 255).astype(np.uint8)).save(OUT, optimize=True)
print("saved", OUT)
