import turtle
t = turtle.Turtle()
t.speed(5)
smallStripeX = -200
smallStripeLength = 250
longStripeLength = 600
stripeWidth = 30
smallStripeOrder = ["red", "white", "red", "white", "red", "white", "red"]
longStripeOrder = ["white", "red", "white", "red", "white", "red"]
starLength = 5

def stripe(x, y, color, length, width):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(0, 2, 1):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def smallStripes():
    for i in range(0, 7, 1):
        stripe(smallStripeX, 200 + (-30 * i), smallStripeOrder[i], smallStripeLength, stripeWidth)

def longStripes():
    for i in range(0, 6, 1):
        stripe(smallStripeX + (-1 * (longStripeLength - smallStripeLength)), -10 + (-30 * i), longStripeOrder[i], longStripeLength, stripeWidth)

def starArea1():
    stripe(-550, 200, "blue", 350, 210)
    t.speed(0)
    t.penup()
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    for i in range(0, 5, 1):
        for j in range(0, 6, 1):
            t.fillcolor("white")
            t.begin_fill()
            t.right(10)
            for k in range(0, 5, 1):
                t.forward(starLength)
                t.right(120)
                t.forward(starLength)
                t.left(48)
            t.left(10)
            t.penup()
            t.forward(60)
            t.pendown()
            t.end_fill()
        t.penup()
        t.goto(-550 + 25, 180 - (40 * (i + 1)))
        t.pendown()

def starArea2():
    t.speed(0)
    t.penup()
    t.goto(-495, 160)
    t.pendown()
    for i in range(0, 4, 1):
        for j in range(0, 5, 1):
            t.fillcolor("white")
            t.begin_fill()
            t.right(10)
            for k in range(0, 5, 1):
                t.forward(starLength)
                t.right(120)
                t.forward(starLength)
                t.left(48)
            t.left(10)
            t.penup()
            t.forward(60)
            t.pendown()
            t.end_fill()
        t.penup()
        t.goto(-495, 160 - (40 * (i + 1)))
        t.pendown()
smallStripes()
longStripes()
starArea1()
starArea2()
t.penup()
t.goto(400, 400)
turtle.done()