from turtle import *
from random import *

color = ['yellow', 'blue', 'red', 'green', 'purple', 'lightblue', 'darkblue', 'lime', 'pink']


def star():
    side = randint(10, 100)
    right(randint(0, 180))
    speed(10)
    color_star = color[randint(0, len(color) - 1)]
    pencolor(color_star)
    fillcolor(color_star)
    begin_fill()
    for _ in range(5):
        forward(side)
        right(144)
    end_fill()


def random_position():
    penup()
    goto(randint(-250, 250), randint(-250, 250))
    pendown()


for _ in range(30):
    star()
    random_position()
