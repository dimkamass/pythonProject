from turtle import *

s = []
name = ['Восток', 'Север', 'Запад', 'Юг']
q = [(20, -10), (-20, 20), (-70, -10), (-10, -30)]
r = 60
speed(8)


def circle_one():
    circle(r)
    penup()
    goto(xcor(), ycor() + r)
    pendown()


circle_one()
for i in range(4):
    forward(140)
    s.append(pos())
    backward(140)
    left(90)
for i in range(4):
    penup()
    goto(s[i])
    goto(xcor() + q[i][0], ycor() + q[i][1])
    write(name[i], move=True, align='left', font=('Arial', 17, 'bold'))
    pendown()

speed(1)
goto(-200, -500)
