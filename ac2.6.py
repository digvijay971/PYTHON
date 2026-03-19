import turtle
a = int(input("side length: "))
t = turtle.Turtle()
for _ in range(4):
    t.forward(a)
    t.right(90)
turtle.done()