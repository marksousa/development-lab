import random
from turtle import Turtle, Screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)

    return color_tuple


tim = Turtle()
tim.shape("turtle")
tim.color("green")
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.setheading(tim.heading() + 10)


def turn_clockwise():
    tim.setheading(tim.heading() - 10)


def clear_drawing():
    screen.resetscreen()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
