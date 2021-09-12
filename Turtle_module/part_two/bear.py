import turtle as t

def up_down(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def bear_head():
    head=60
    for _ in range(2):
        t.circle(head)
        head=head//2

def bear_nose_and_mouth():
    up_down(0,30)
    t.circle(10)
    t.right(90)
    t.forward(20)

def eyes():
    up_down(25,60)
    t.dot(10,'black')
    up_down(-25,60)
    t.dot(10, 'black')

def eyers():
    up_down(50,100)
    t.circle(15)
    up_down(-50,100)
    t.circle(15)

def bear():
    t.speed(10)
    bear_head()
    eyers()
    bear_nose_and_mouth()
    eyes()
    t.penup()
    t.speed(1)
    t.forward(1000)
bear()
