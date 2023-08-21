# Python program to draw
# Rainbow Benzene
# using Turtle Programming
from turtle import Turtle
tur = Turtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
tur.pen()
tur.screen.bgcolor('black')
for x in range(360):
    tur.pencolor(colors[x % 6])
    tur.width(x//100 + 1)
    tur.forward(x)
    tur.left(59)
