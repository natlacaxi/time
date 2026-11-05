"""Génère les icônes PNG + favicon.ico de TalcoTime (nécessite Pillow : pip install pillow)."""
import math
from PIL import Image, ImageDraw, ImageFilter

INK, IV, ACC = (12, 12, 16), (243, 239, 232), (255, 90, 54)

def make(size, maskable=False):
    S = size * 4; c = S / 2; R = S * (.31 if maskable else .37)
    im = Image.new("RGBA", (S, S), INK + (255,))
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((S * .45, -S * .25, S * 1.25, S * .55), fill=ACC + (80,))
    im = Image.alpha_composite(im, glow.filter(ImageFilter.GaussianBlur(S * .1)))
    d = ImageDraw.Draw(im)
    d.ellipse((c - R, c - R, c + R, c + R), outline=IV + (255,), width=max(2, int(S * .012)))
    for i in range(60):
        a = math.radians(i * 6); big = i % 5 == 0; q = i % 15 == 0
        r1, r2 = R * .93, R * (.78 if q else .83 if big else .89)
        col = ACC if i == 0 else IV
        d.line((c + r1 * math.sin(a), c - r1 * math.cos(a), c + r2 * math.sin(a), c - r2 * math.cos(a)),
               fill=col + ((255,) if big else (110,)), width=int(S * (.014 if q or i == 0 else .008 if big else .004)))
    def hand(deg, ln, wd, col, tail=0):
        a = math.radians(deg)
        d.line((c - R * tail * math.sin(a), c + R * tail * math.cos(a), c + R * ln * math.sin(a), c - R * ln * math.cos(a)),
               fill=col + (255,), width=int(S * wd))
    hand(-55, .45, .026, IV); hand(0, .66, .017, IV); hand(145, .72, .009, ACC, .22)
    k = S * .024
    d.ellipse((c - k, c - k, c + k, c + k), fill=IV + (255,))
    k = S * .01
    d.ellipse((c - k, c - k, c + k, c + k), fill=ACC + (255,))
    if not maskable:
        m = Image.new("L", (S, S), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * .22), fill=255)
        im.putalpha(m)
    return im.resize((size, size), Image.LANCZOS)

make(192).save("icon-192.png"); make(512).save("icon-512.png")
make(512, True).save("maskable-512.png")
make(64).save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("Icônes générées")
