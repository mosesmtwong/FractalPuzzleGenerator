from turtle import *
from PIL import Image

axiom = "A"
ruleA = "A-B--B+A++AA+B-"
ruleB = "+A-BB--B-A++A+B"

ITER = 5

setup(2000, 2000)
print(window_width())
penup()
goto(100, 100)
pendown()

for _ in range(ITER):
    Lsystem = ""
    for chr in axiom:
        if chr == "A":
            Lsystem += ruleA
        elif chr == "B":
            Lsystem += ruleB
        else:
            Lsystem += chr
    axiom = Lsystem

tracer(0, 0)
hideturtle()
for chr in axiom:
    if chr == "A" or chr == "B":
        forward(5)
    elif chr == "+":
        left(60)
    elif chr == "-":
        right(60)
update()

canvas = getscreen().getcanvas()
canvas.postscript(file="gosper.ps")

turtle_img = Image.open("gosper.ps")
turtle_img.save("gosper.png")
