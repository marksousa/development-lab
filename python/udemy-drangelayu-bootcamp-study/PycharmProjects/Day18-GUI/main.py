import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

def square_draw(turtle):
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)


# square_draw(timmy_the_turtle)

def dotted_line(turtle):
    turtle.fd(10)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()


# for _ in range(15):
#     dotted_line(timmy_the_turtle)


colours = ['green', 'red', 'blue', 'black', 'yellow', 'orange', 'purple', 'gray']


def complex_draw(turtle):

    count = 0
    for i in range(3,10):
        turtle.color(random.choice(colours))
        while count < i:
            turtle.fd(100)
            turtle.rt(360/i)
            count += 1
        count = 0


complex_draw(timmy_the_turtle)

screen = Screen()
screen.exitonclick()