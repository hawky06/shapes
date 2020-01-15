def draw_door(bob,x,y):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.forward(85)
        bob.right(90)
        bob.forward(40)
        bob.right(90)
    bob.end_fill()