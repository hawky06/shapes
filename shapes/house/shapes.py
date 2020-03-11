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
    
def draw_circle(bob, x, y, diameter):
    radius = diameter / 2
    bob.penup()
    bob.setx(x+radius)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()
    
def draw_triangle_equilateral(bob, x, y, width):
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
    
def draw_triangle_right_angle(bob, x, y, width):
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
    
def draw_cross(bob, x, y, width):
    bob.penup()
    bob.setx(x + width / 2)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()                                                                                                                                                                                                                                                  
    bob.forward(width)
    bob.penup()
    bob.left(90)
    bob.forward(width/2)
    bob.left(90)
    bob.forward(width/2)
    bob.left(90)
    bob.pendown()
    bob.forward(width)

def draw_spiral_square(bob, x ,y, width):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()

    bob.forward(width)
    bob.left(90)
    reduction = width / 10

    while width > 0:
        bob.forward(width)
        bob.left(90)
        bob.forward(width)
        bob.left(90)
        width = width - reduction