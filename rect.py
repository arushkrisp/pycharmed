length = input("Enter your rectangle's length in centimeters: ")
width = input("Enter your rectangle's width in centimeters: ")
color = input("Enter a color: ")
length, width = int(length), int(width)

import turtle
t = turtle.Turtle()
def rectDraw(l, w):
    t.penup()
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.goto(-300, 300)
    t.right(180)
    t.pendown()
    lPix = l * 37.8
    wPix = w * 37.8
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(lPix)
        t.right(90)
        t.forward(wPix)
        t.right(90)
    t.end_fill()
    turtle.done()
rectDraw(length, width)
