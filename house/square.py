def draw_square(bob,x,y,size):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    for i in range(4):
        bob.forward(size)
        bob.left(90)
    bob.end_fill()