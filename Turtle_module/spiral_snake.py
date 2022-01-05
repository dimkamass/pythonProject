import turtle as t


colors = ["green", 'purple', 'orange', 'red', 'blue', 'yellow']
def spiral_snake():
    side=180
    for _ in range(10):
            for j in colors:
                t.pensize(side//4)
                t.pencolor(j)
                t.forward(side)
                t.right(45)
                side-=side//20
spiral_snake()
