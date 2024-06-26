from PIL import Image, ImageDraw
from math import *

SIDE = 20
UNIT = 100
ROOT = round(sqrt(3) * UNIT // 2)
HEIGHT = round(UNIT * SIDE * sqrt(3))
INV_A = 1 / tan(pi / 6)
ROOTTHREETWO = sqrt(3) / 2
D = UNIT * SIDE
OFFSET = 70

im = Image.new("RGB", (SIDE * UNIT * 2 + 100, HEIGHT + 100), (255, 255, 255))


class node:
    def __init__(self, x, y):

        self.coords = (x, y)
        self.left = 1
        self.right = 1
        self.upleft = 1
        self.upright = 1
        self.downleft = 1
        self.downright = 1


draw = ImageDraw.Draw(im)

parity = 0
st_x, st_y = 0, OFFSET
nodes = []
for y in range(st_y, HEIGHT, ROOT):
    parity += 1
    if parity % 2 == 1:
        st_x += UNIT // 2
    else:
        st_x -= UNIT // 2
    for x in range(st_x, SIDE * UNIT * 2, UNIT):
        if (
            y <= INV_A * x + D * ROOTTHREETWO - OFFSET - 3
            and y >= -INV_A * x + D * ROOTTHREETWO + OFFSET + 3
            and y <= -INV_A * (x - 2 * D) + D * ROOTTHREETWO - OFFSET - 3
            and y >= INV_A * (x - 2 * D) + D * ROOTTHREETWO + OFFSET + 3
        ):
            # draw.ellipse(((x - 4, y - 4), (x + 4, y + 4)), (0, 0, 0))
            nodes.append(node(x, y))

im.save("puzzle.png")
