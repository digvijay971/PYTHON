import turtle
turtle.Screen().bgcolor("red")
a=turtle.Turtle()
num_side=5
side_length=100
x=360.00/num_side
for i in range(num_side):
    a.forward(side_length)
    a.left(x)
turtle.done()