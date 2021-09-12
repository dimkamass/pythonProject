import turtle as t

def romb(side):
    t.right(10)
    for _ in range(10):
        for _ in range(2):
            t.forward(side)
            t.left(60)
            t.forward(side)
            t.left(120)
        t.left(40)
romb(100)