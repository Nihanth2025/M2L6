import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
p=turtle.Turtle()
side=7
len=50
a=360.0/side

for i in range(side):
    p.forward(len)
    p.right(a)

turtle.done()