import turtle as t

t.speed(5)


def draw_three_squares(side):
    def draw_one_square():

        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.left(45)

    for _ in range(8):
        draw_one_square()


draw_three_squares(100)
