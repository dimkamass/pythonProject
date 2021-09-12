
import turtle as t
t.Screen().bgcolor('DeepSkyBlue')
t.shape('turtle')
t.stamp()
for _ in range(12):
  t.penup()
  t.forward(70)
  t.pendown()
  t.forward(30)
  t.penup()
  t.forward(20)
  t.stamp()
  t.backward(120)
  t.left(30)
