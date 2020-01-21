import math

def draw_triangle_equilateral(bob,x,y,width):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    for i in range(3):
        bob.forward(width)
        bob.left(120)
    bob.end_fill()
    
def draw_triangle_right_angle(bob,x,y,width):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    bob.forward(width)
    bob.left(135)
    bob.forward(math.sqrt((width**2)/2))
    bob.left(90)
    bob.forward(math.sqrt((width**2)/2))
    bob.end_fill()