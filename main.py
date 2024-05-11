from PIL import Image, ImageDraw
import math

SIDE = 15
UNIT = 10
ROOT = int(math.sqrt(3) * UNIT // 2)
print(ROOT)

im = Image.new("RGB", (200, 200), (255, 255, 255))


class node:
    def __init__(self, x, y, left, right, upleft, upright, downleft, downright):
        self.coords = (x, y)
        self.left = left
        self.right = right
        self.upleft = upleft
        self.upright = upright
        self.downleft = downleft
        self.downright = downright


pointA = node(100, 100, 0, 0, 0, 0, 0, 0)

draw = ImageDraw.Draw(im)

parity = 0
st_x, st_y = 10, 10
for y in range(st_y, SIDE * ROOT, ROOT):
    parity += 1
    if parity % 2 == 1:
        st_x += UNIT // 2
    else:
        st_x -= UNIT // 2
    for x in range(st_x, SIDE * UNIT, UNIT):
        im.putpixel((x, y), (0, 0, 0))


im.save("puzzle.png")
