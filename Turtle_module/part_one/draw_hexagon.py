import turtle as t
def hexagon(side):
    for _ in range(6):
        t.forward(side)
        t.right(60)
hexagon(100)
