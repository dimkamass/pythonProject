from turtle import *
from random import *

colors = ['red', 'coral', 'blue', 'fuchsia', 'lime', 'khaki', 'gold', 'yellow', 'purple', 'orange', 'pink', 'brown']
Screen().bgcolor('aqua')
speed(1000)


def up_down(x, y):
    penup()
    goto(x, y)
    pendown()


def snow_flake():
    up_down(randint(-300, 300), randint(-300, 300))
    r_distance = randint(20, 100)  # рандомный радиус снежинки
    r_color = colors[randint(0, len(colors) - 1)]
    pencolor(r_color)  # рандомный цвет снежинки
    pensize(r_distance // 20)
    for _ in range(8):
        for _ in range(4):
            left(45)
            forward(r_distance // 4)
            backward(r_distance // 4)
            right(90)
            forward(r_distance // 4)
            backward(r_distance // 4)
            left(45)
            forward(r_distance // 4)
        backward(r_distance)
        right(45)


for _ in range(10):
    snow_flake()
