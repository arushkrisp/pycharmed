col = input("Enter a fill color: ")
outl = input("Enter your outline color: ")
thi = input("Enter the thickness in pixels: ")
thi = int(thi)

import turtle
t = turtle.Turtle()
t.speed(3)

def heart(color, outline, thickness):
    t.fillcolor(color)
    t.pencolor(outline)
    t.pensize(thickness)
    t.begin_fill()
    t.left(45)
    t.forward(285)
    t.circle(100, 180)
    t.circle(200, 45)
    t.right(180)
    t.circle(200, 45)
    t.circle(100, 180)
    t.forward(285)
    t.end_fill()

t.penup()
t.goto(0, -200)
t.pendown()
heart(col, outl, thi)
t.penup()
t.goto(400, 400)
turtle.done()