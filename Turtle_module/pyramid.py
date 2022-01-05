import turtle as t
start_x,start_y=0,0
finish_x,finish_y=-100,-200
t.dot(10,'red')
t.pencolor('green')
t.pensize(2)
for _ in range(11):
    t.goto(finish_x,finish_y)
    t.dot(10,'blue')
    print(t.pos())
    t.goto(start_x,start_y)
    finish_x+=20
