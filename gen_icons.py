"""Génère les icônes PNG + favicon.ico de TalcoTime (nécessite Pillow : pip install pillow)."""
import math, os
from PIL import Image, ImageDraw, ImageFilter

C1, C2, C3 = (124, 58, 237), (236, 72, 153), (6, 182, 212)

def grad(n=64):
    g = Image.new("RGB", (n, n)); p = g.load()
    for y in range(n):
        for x in range(n):
            t = (x + y) / (2 * n - 2)
            a, b, u = (C1, C2, t * 2) if t < .5 else (C2, C3, (t - .5) * 2)
            p[x, y] = tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))
    return g

def make(size, maskable=False):
    S = size * 4; c = S / 2; R = S * (.30 if maskable else .36)
    im = grad().resize((S, S), Image.BILINEAR).convert("RGBA")
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((c - R * 1.14, c - R * 1.14, c + R * 1.14, c + R * 1.14), fill=(255, 255, 255, 110))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(S * .035)))
    d = ImageDraw.Draw(im)
    d.ellipse((c - R, c - R, c + R, c + R), fill=(255, 255, 255, 255))
    r = R * .9
    d.ellipse((c - r, c - r, c + r, c + r), fill=(10, 6, 38, 255))
    w = max(1, int(S * .006))
    d.ellipse((c - r * .42, c - r, c + r * .42, c + r), outline=(255, 255, 255, 45), width=w)
    d.line((c - r, c, c + r, c), fill=(255, 255, 255, 45), width=w)
    for i in range(12):
        a = math.radians(i * 30); big = i % 3 == 0; rr = r * .82; dr = S * (.014 if big else .007)
        x, y = c + rr * math.sin(a), c - rr * math.cos(a)
        d.ellipse((x - dr, y - dr, x + dr, y + dr), fill=(34, 211, 238, 255) if big else (255, 255, 255, 130))
    def hand(deg, ln, wd, col):
        a = math.radians(deg)
        d.line((c, c, c + r * ln * math.sin(a), c - r * ln * math.cos(a)), fill=col, width=int(S * wd))
    hand(0, .56, .03, (255, 255, 255, 255)); hand(120, .42, .026, (255, 255, 255, 255)); hand(205, .76, .012, (244, 114, 182, 255))
    k = S * .026
    d.ellipse((c - k, c - k, c + k, c + k), fill=(236, 72, 153, 255))
    if not maskable:
        m = Image.new("L", (S, S), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * .24), fill=255)
        im.putalpha(m)
    return im.resize((size, size), Image.LANCZOS)


make(192).save("icon-192.png"); make(512).save("icon-512.png")
make(512, True).save("maskable-512.png")
make(64).save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("Icônes générées")
