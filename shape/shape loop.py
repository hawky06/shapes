import turtle

bob=turtle.Turtle()

#turtle.Screen().bgcolor("yellow")
#bob.color("green")
bob.fillcolor("aqua")
bob.begin_fill()
for i in range(4):
    bob.forward(100)
    bob.right(90)
bob.end_fill()