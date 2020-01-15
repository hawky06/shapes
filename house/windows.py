import numpy
from turtle import *
from square import draw_square
from triangle import draw_triangle

def draw_window_square(bob,x,y):
    
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()
    
    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_square(bob,x,y,40)
    
    bob.setheading(90)
    for i in range(2):
        bob.forward(20)
        bob.right(90)
        bob.forward(40)
        bob.right(90)
        bob.forward(20)
        bob.right(90)
        
def draw_window_triangle(bob,x,y):
    
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()
    
    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_triangle(bob,x,y,40)
