import numpy
from square import *
from triangles import *
from circle import *

def draw_window_square(bob,x,y,width):
    
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()
    
    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_square(bob,x,y,width)
    
    bob.setheading(90)
    for i in range(2):
        bob.forward(20)
        bob.right(90)
        bob.forward(40)
        bob.right(90)
        bob.forward(20)
        bob.right(90)
        
def draw_window_triangle_equilateral(bob,x,y,width):
    
    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_triangle_equilateral(bob,x,y,width)

def draw_window_circle(bob,x,y,width):
    
    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_circle(bob,x+width/2,y,width/2)