def draw_circle(bob,x,y,radius):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()
    