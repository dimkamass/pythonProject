from turtle import *

radius = 100
Screen().bgcolor('blue')

def moon():
    speed(0)
    hideturtle()
    begin_fill()
    fillcolor('yellow')
    pencolor('yellow')
    circle(radius)
    end_fill()

def spirit():
    speed(5)
    penup()
    goto(xcor() + 2 * radius, ycor() + radius)
    pencolor('blue')
    shape('circle')
    fillcolor('blue')
    shapesize(radius / 10)
    showturtle()


moon()
spirit()
while True:
    if xcor()<-200:
        break
    else:
        goto(xcor() - 1, ycor())

