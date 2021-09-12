import turtle


def honeycomb(side):
    for _ in range(7):
        for _ in range(6):
            turtle.forward(side)
            turtle.right(60)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(60)


honeycomb(int(input()))