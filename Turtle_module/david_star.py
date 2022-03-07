import turtle as t


def star_cor(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def firs_triangle():
    t.goto(-50, -25)
    t.goto(50, -25)
    t.goto(0, 50)


def second_triangle():
    t.goto(-50, 25)
    t.goto(50, 25)
    t.goto(0, -50)


def star():
    star_cor(0, 50)
    firs_triangle()
    star_cor(0, -50)
    second_triangle()


star()
