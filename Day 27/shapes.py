import random
from turtle import Turtle, Screen
from colors_list import colors

mus = Turtle()
mus.shape("triangle")

def draw_shapes(number_of_shapes, side_length):
    for side in range(3, number_of_shapes):
        mus.color(random.choice(colors))
        for shape_side in range(0, side):
            mus.forward(side_length)
            mus.left(360 / side)


draw_shapes(11, 100)
screen = Screen()
screen.exitonclick()