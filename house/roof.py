import math
import numpy
from triangles import *

#def draw_roof(bob,x,y,width):
    #bob.penup()
    #bob.setx(x)
    #bob.sety(y)
    #bob.setheading(0)
    #bob.pendown()
    #bob.fillcolor("dark red")
    #bob.begin_fill()
    #bob.forward(width)
    #bob.left(135)
    #bob.forward(math.sqrt((width**2)/2))
    #bob.left(90)
    #bob.forward(math.sqrt((width**2)/2))
    #bob.end_fill()
   
def draw_roof(bob,x,y,width):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(90)
    bob.pendown()

    pencolors = [0,0,0]
    fillcolors = list(numpy.random.choice(range(256), size=3))
    bob.color((pencolors[0],pencolors[1],pencolors[2]),(fillcolors[0],fillcolors[1],fillcolors[2]))

    draw_triangle_right_angle(bob,x,y,250)
