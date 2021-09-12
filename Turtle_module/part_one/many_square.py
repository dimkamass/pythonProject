import turtle as t

def draw(count,side):

    def square(side):
        for _ in range(4):
            t.left(90)
            t.forward(side)
        side+=5
    for _ in range(count):
        square(side)
        side+=2

draw(20,50)



