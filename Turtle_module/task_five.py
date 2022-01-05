from turtle import *
from math import *
from random import *

area = 3000  # площадь фигур
step = 130
speed(4)
start_x = -300
start_y = 250
colors = ['red', 'coral', 'blue', 'fuchsia', 'lime', 'khaki', 'gold', 'yellow', 'purple', 'orange', 'pink', 'brown']
spisok = [(3, 120), (4, 90), (5, 72), (6, 60)]  # список фигур (количество сторон, угол)


def go_to_start():
    penup()
    goto(start_x, start_y)
    pendown()


def def_side(count_of_side):
    return sqrt((area * 4 * tan(radians(180) / count_of_side) / count_of_side))


def telo():  # случайная фигура
    num = randint(0, 3)
    side = def_side(spisok[num][0])

    fillcolor(colors[randint(0, len(colors) - 1)])
    begin_fill()
    for i in range(spisok[num][0]):
        forward(side)
        left(spisok[num][1])
    end_fill()


def move_right():
    penup()
    goto(xcor() + step, ycor())
    pendown()


def move_down():
    penup()
    global start_y
    start_y -= step
    goto(start_x, start_y)
    pendown()


go_to_start()

for i in range(5):
    for j in range(5):
        telo()
        move_right()
    move_down()

goto(500,-200)