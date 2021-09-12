
import turtle as t
t.Screen().bgcolor('green')
t.shape('turtle')
t.stamp()

step=200
for _ in range(40):
  t.penup()
  t.forward(step)
  t.stamp()
  t.backward(step)
  t.left(25)
  step-=5
