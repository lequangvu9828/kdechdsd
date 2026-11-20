# -*- coding: utf-8 -*-
"""Ghim số vào ảnh chụp BPM. python3 annos.py -> src/img/<key>.jpg"""
import glob, os
from PIL import Image, ImageDraw, ImageFont

D = '/tmp/claude-tool-results/d06dcfa3-a158-5cdb-b56c-903b53271bde/'
OUT = os.path.join(os.path.dirname(__file__), 'img')
NAVY = (0, 71, 204)

# key: (id file, crop box, [(n, x, y)] toạ độ trong ảnh gốc 1450x840)
A = {
 'qt01-form': ('1795142762153-2vhfq2', (44, 45, 1406, 720), [(1, 90, 142), (2, 90, 324), (3, 90, 433), (4, 90, 572), (5, 1325, 698)]),
 'qt01-s1': ('1795142770886-06lvv4', (290, 35, 1450, 840), [(1, 1165, 86), (2, 1050, 221), (3, 660, 320), (4, 335, 530), (5, 1160, 325)]),
 'qt01-s2': ('1795142779800-sdzenn', (290, 35, 1450, 840), [(1, 330, 275), (2, 1165, 298), (3, 360, 573), (4, 700, 176)]),
 'qt01-s5': ('1795142787640-qqvj96', (290, 35, 1450, 840), [(1, 1285, 86), (2, 330, 277), (3, 360, 590), (4, 1165, 300)]),
 'qt02-form': ('1795142795604-j76222', (468, 60, 982, 456), [(1, 495, 158), (2, 495, 284), (3, 495, 339), (4, 905, 434)]),
 'qt02-s2': ('1795142802090-59xwxx', (290, 35, 1450, 840), [(1, 330, 162), (2, 540, 212), (3, 335, 564), (4, 1165, 298)]),
 'qt03-form': ('1795142810597-kxzdd3', (468, 60, 982, 510), [(1, 495, 158), (2, 495, 284), (3, 495, 339), (4, 495, 393), (5, 905, 488)]),
 'qt05-form': ('1795142819631-a2kkvt', (468, 60, 982, 456), [(1, 495, 158), (2, 495, 285), (3, 495, 339), (4, 905, 434)]),
 'qt06-form': ('1795142750668-lyoovw', (468, 60, 982, 810), [(1, 495, 158), (2, 495, 284), (3, 495, 339), (4, 495, 503), (5, 905, 788)]),
 'qt06-s1': ('1795142734695-71zuei', (290, 35, 1450, 840), [(1, 1240, 65), (2, 1030, 151), (3, 345, 212), (4, 335, 340), (5, 1165, 208)]),
 'qt06-s2': ('1795142742912-3zkbhb', (290, 35, 1450, 840), [(1, 965, 198), (2, 330, 367), (3, 1285, 86), (4, 700, 260)]),
 'qt07-form': ('1795141682127-7zq7jp', (468, 60, 982, 500), [(1, 495, 158), (2, 495, 279), (3, 495, 329), (4, 495, 382), (5, 905, 478)]),
}

def font(sz):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def run():
    for k, (fid, box, marks) in A.items():
        f = [x for x in glob.glob(D + '*') if fid in x][0]
        im = Image.open(f).convert('RGB')
        S = 2
        big = im.resize((im.width * S, im.height * S), Image.LANCZOS)
        dr = ImageDraw.Draw(big)
        ft = font(26)
        for n, x, y in marks:
            r = 20
            cx, cy = x * S, y * S
            dr.ellipse((cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3), fill=(255, 255, 255))
            dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=NAVY)
            dr.text((cx, cy), str(n), fill=(255, 255, 255), font=ft, anchor='mm')
        c = big.crop(tuple(v * S for v in box))
        if c.width > 1500:
            c = c.resize((1500, int(c.height * 1500 / c.width)), Image.LANCZOS)
        c.save(os.path.join(OUT, k + '.jpg'), quality=90, subsampling=0)
        print(k, c.size)

if __name__ == '__main__':
    run()
