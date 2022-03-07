from turtle import *

side = 50
start_x, start_y = -100, 100

counter_of_color = 1


def square(side):
    global counter_of_color
    counter_of_color += 1
    if counter_of_color % 2 != 0:
        for _ in range(4):
            forward(side)
            left(90)
        forward(side)
    else:
        begin_fill()
        for _ in range(4):
            forward(side)
            left(90)
        end_fill()
        forward(side)


def down():
    penup()
    global start_y
    start_y -= side
    goto(start_x, start_y)
    pendown()


penup()
goto(start_x, start_y)
pendown()
for _ in range(5):
    for _ in range(5):
        square(side)
    down()
