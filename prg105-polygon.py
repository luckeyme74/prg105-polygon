import turtle
t = turtle.Turtle()
length = 350
def square(t, length):
     print t
     t.fd(length)
     t.lt(90)
     t.fd(length)
     t.lt(90)
     t.fd(length)
     t.lt(90)
     t.fd(length)
     turtle.done()


length = 200
n = 6
angle = 360 / n
def polygon(t, length, n):
     print t
     for i in range(n):
         t.fd(length)
         t.lt(angle)

polygon(t, length = 200, n = 6)
turtle.done()
