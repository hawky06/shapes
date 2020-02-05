import numpy
from shapes import *

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
    draw_cross(bob,x,y,width)
        
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
    draw_cross(bob, x, y, width)

def draw_window_spiral(bob, x, y, width):

    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))
    
    draw_square(bob, x, y, width)
    draw_spiral_square(bob, x, y, width)

def draw_window_random(bob,x,y,width):
    
    random=numpy.random.choice(4)
    if (random == 0):
        draw_window_square(bob,x,y,width)
    elif (random == 1):
        draw_window_triangle_equilateral(bob, x, y, width)
    elif (random == 2):
        draw_window_circle(bob, x, y, width)
    elif (random == 3):
        draw_window_spiral(bob, x, y, width)