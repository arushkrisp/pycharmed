dia = input("Enter your circle's diameter in centimeters: ")
color = input("Enter a color: ")
dia = int(dia)

import turtle
t = turtle.Turtle()

def drawCir(diam):
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle((diam / 2) * 37.8)
    t.end_fill()
    turtle.done()

drawCir(dia)
