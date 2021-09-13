from turtle import *

list_of_colors = ['pink', 'violet', 'blue', 'lightblue', 'turquoise', 'lightgreen', 'green', 'yellow', 'orange', 'red']
radius = 100
for i in list_of_colors:
    fillcolor(i)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    goto(0, ycor() + 10)
    pendown()
    radius -= 10
