from turtle import *
height_light=300
width_light=100
colors=['red','yellow','green']
def rectangle():
    begin_fill()
    for _ in range(2):
        forward(width_light)
        left(90)
        forward(height_light)
        left(90)
    end_fill()
def my_traffic_lights():
    rectangle()
    center=width_light/2
    step=height_light/6
    goto(center,step)
    for i in range(len(colors)):
        pendown()
        dot(60,colors[i])
        penup()
        goto(center,ycor()+2*step)
my_traffic_lights()
