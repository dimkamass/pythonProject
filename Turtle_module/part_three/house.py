from turtle import *

speed(1)


def square():
    fillcolor('green')
    begin_fill()
    for _ in range(4):
        forward(200)
        right(90)
    end_fill()


def triangle():
    fillcolor('red')
    begin_fill()
    goto(220, 0)
    goto(100, 150)
    goto(-20, 0)
    goto(0, 0)
    end_fill()


square()
triangle()
