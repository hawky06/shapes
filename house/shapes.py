import math

def draw_square(bob, x, y, size):
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
    
def draw_circle(bob, x, y, radius):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()
    
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