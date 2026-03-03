import turtle
a=turtle.Screen()
a.bgcolor("red")
x=turtle.Turtle()
size = 0
while True:
    for b in range(4):
        x.fd(size +1)
        x.left(90)
        size=size-5
    size=size+1