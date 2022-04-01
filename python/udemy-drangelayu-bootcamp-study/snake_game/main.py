from turtle import Turtle, Screen

initial_abscissas = [0, -20, -40]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")

# TODO create the snake
# The initial snake is represented by 3 white squares
for abscissa in initial_abscissas:
    snake_segment = Turtle(shape="square")
    snake_segment.penup()
    snake_segment.color("white")
    snake_segment.setx(x=abscissa)

# TODO move the snake
# TODO control the snake
# TODO detect collision with food
# TODO create a scoreboard
# TODO detect collision with wall
# TODO detect collision with tail

screen.exitonclick()
