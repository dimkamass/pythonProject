import math
from turtle import *

side_triangle = 300
hight_triangle = math.sqrt(side_triangle ** 2 - (side_triangle / 2) ** 2)
smeshenie = hight_triangle / 2
visota = [(0, -hight_triangle + smeshenie), (-side_triangle / 2, smeshenie), (side_triangle / 2, smeshenie)]


def center_triangle():
    penup()
    goto(0, hight_triangle)
    pendown()
    goto(-side_triangle / 2, 0)
    goto(side_triangle / 2, 0)
    goto(0, hight_triangle)


def white_triangle():
    pencolor('white')
    penup()
    goto(0, -hight_triangle + smeshenie)
    fillcolor('white')
    begin_fill()
    pendown()
    goto(-side_triangle / 2, smeshenie)
    goto(side_triangle / 2, smeshenie)
    end_fill()
    goto(0, -hight_triangle + smeshenie)


def my_dot():
    for i in visota:
        penup()
        goto(i)
        pendown()
        dot(80, 'black')


center_triangle()
my_dot()
white_triangle()
goto(20, 2000)
