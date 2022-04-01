import time
from turtle import Turtle, Screen

initial_coordinates = [[0,0], [-20,0], [-40,0]]
snake_segments = []
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(n=0)  # to reduce the delay in snake movement. combine with screen.update() and time.sleep(0.1)

# TODO create the snake
# The initial snake is represented by 3 white squares
for coordinates in initial_coordinates:
    snake_segment = Turtle(shape="square")
    snake_segment.penup()
    snake_segment.color("white")
    snake_segment.setposition(coordinates)
    snake_segments.append(snake_segment)

# TODO move the snake
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # to simulate the correct movement behaviour
    # the third segment moves to the second segment position,
    # the second segment moves to the first segment position
    # and so on (must be backward-front, think about it)
    # obs: this range comes from C language
    # for index_segment in range(start=len(snake_segments)-1, stop=0, step=-1):
    for index_segment in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[index_segment - 1].xcor()
        new_y = snake_segments[index_segment - 1].ycor()
        snake_segments[index_segment].goto(new_x, new_y)

    snake_segments[0].forward(20)  # needs to move the first segment to forward

# TODO control the snake
# TODO detect collision with food
# TODO create a scoreboard
# TODO detect collision with wall
# TODO detect collision with tail

screen.exitonclick()
