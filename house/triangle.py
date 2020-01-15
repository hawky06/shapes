def draw_triangle(bob,x,y,size):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    for i in range(3):
        bob.forward(size)
        bob.left(120)
    bob.end_fill()