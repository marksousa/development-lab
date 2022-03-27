import random

import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('google.png', 6)
colors = colorgram.extract('abaporu_tarsila-do-amaral.jpg', 6)
# colors = colorgram.extract('guernica.jpg', 10)
# colors = colorgram.extract('davignon.jpg', 10)

rgb_colors = []

for color in colors:
    # rgb_colors.append(color.rgb) not in desired format
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)

rubens_the_turtle = Turtle()
rubens_the_turtle.speed('fastest')

screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

rubens_the_turtle.penup()
rubens_the_turtle.hideturtle()

for i in range(1, 11):
    for j in range(1, 11):
        rubens_the_turtle.dot(15, random.choice(rgb_colors))
        rubens_the_turtle.forward(screen.window_width()*0.10)
    rubens_the_turtle.goto(0, screen.window_height()*i/10)
screen.exitonclick()
