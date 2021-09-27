import turtle
t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle.bgcolor("black")
t.speed(0)
for i in range(1,200, 1):
    t.color(colors[i % len(colors)])
    t.pensize(i / 10 + 1)
    t.forward(i)
    t.left(59)
turtle.done()