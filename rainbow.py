dia = input("Enter your circle's diameter in pixels: ")
n = input("How many circles? Enter here: ")
dia, n = int(dia), int(n)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

import turtle
t = turtle.Turtle()


def rainbowCir(diam):
    t.speed(0)
    t.penup()
    t.goto(0, -350)
    t.pendown()
    for i in range(n + 1, 1, -1):
        t.fillcolor(colors[i % len(colors)])
        t.begin_fill()
        t.circle((diam / 2) * i)
        t.end_fill()
    t.penup()
    t.goto(400, 400)
    t.pendown()
    turtle.done()

rainbowCir(dia)