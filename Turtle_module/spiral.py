import turtle as t
t.speed(100)
def draw(count,side):

    def square(side):
        for _ in range(2):
            t.right(90)
            t.forward(side)

    for _ in range(count):
        side -= 3
        square(side)


draw(50,100)