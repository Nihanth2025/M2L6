import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
p=turtle.Turtle()
s=0
while True:
    for i in range(6):
        p.fd(s+1)
        p.left(60)
        s=s-5

s=s+1
