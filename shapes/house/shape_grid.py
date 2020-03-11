import turtle
from shapes import *

bob = turtle.Turtle()

y = 0
width = 20

for j in range(5):
    x = 0
    y = y + width
    for i in range(5):
        draw_triangle_equilateral(bob, x, y, width)
        x = x + width