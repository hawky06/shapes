import turtle
from turtle import *
from roof import draw_roof
from door import draw_door
from walls import draw_walls
from windows import *

bob=turtle.Turtle()
colormode(255)

def draw_house(x,y):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    window_width=40
        
    #main structure
    draw_walls(bob,x,y)
            
    #door
    draw_door(bob,x+80,y)

    #bottom left window
    draw_window_circle(bob,x+20,y+35,window_width)

    #bottom right window
    draw_window_square(bob,x+140,y+35,window_width)

    #top left window
    draw_window_triangle_equilateral(bob,x+20,y+125,window_width)

    #top right window
    draw_window_triangle_equilateral(bob,x+140,y+125,window_width)

    #roof
    draw_roof(bob,x+-25,y+200,250)

draw_house(0,0)
draw_house(250,100)