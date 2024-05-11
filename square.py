from PIL import Image, ImageDraw
from math import *
import random

SIDE = 40
UNIT = 100
OFFSET = 70


class node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = 1
        self.down = 1
        self.right = 1
        self.left = 1

    def walk():
        pass


im = Image.new("RGB", (SIDE * UNIT + OFFSET, SIDE * UNIT + OFFSET), (255, 255, 255))

draw = ImageDraw.Draw(im)

for x in range(OFFSET, SIDE * UNIT, UNIT):
    for y in range(OFFSET, SIDE * UNIT, UNIT):
        draw.ellipse(((x - 4, y - 4), (x + 4, y + 4)), (0, 0, 0))

im.save("square.png")
