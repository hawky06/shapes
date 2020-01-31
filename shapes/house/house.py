import turtle
from turtle import *
from roof import draw_roof
from door import draw_door
from walls import draw_walls
from windows import *

bob=turtle.Turtle()
colormode(255)

def draw_house(x,y,size):
    bob.penup()
    bob.setx(x)
    bob.sety(y)
    bob.setheading(0)
    bob.pendown()
    window_width=size/5
    door_width=window_width
    
    #main structure
    draw_walls(bob,x, y, size)
            
    #door
    draw_door(bob, x+size/2-door_width/2, y, door_width)

    #bottom left window
    draw_window_random(bob, x+size/10, y+size/6, window_width)

    #bottom right window
    draw_window_random(bob, x+size/1.4, y+size/6, window_width)

    #top left window
    draw_window_random(bob, x+size/10,y+size/1.6, window_width)

    #top right window
    draw_window_random(bob, x+size/1.4, y+size/1.6, window_width)

    #roof
    draw_roof(bob, x-size/8, y+size, size*1.25)

for i in range(3):
    x_random = numpy.random.choice(range(-200, 200))
    y_random = numpy.random.choice(range(-200, 200))
    size_random = numpy.random.choice(200)
    draw_house(x_random, y_random, size_random)