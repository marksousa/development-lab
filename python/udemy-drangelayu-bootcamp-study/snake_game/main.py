from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")

# TODO create the snake
# The initial snake is represented by 3 white squares
snake_tail = Turtle(shape="square")
snake_tail.penup()
snake_tail.color("white")
snake_tail.setx(x=-40)

snake_body = Turtle(shape="square")
snake_body.penup()
snake_body.color("white")
snake_body.setx(x=-20)

snake_head = Turtle(shape="square")
snake_head.color("white")
snake_head.penup()
snake_head.setx(x=0)

# TODO move the snake
# TODO control the snake
# TODO detect collision with food
# TODO create a scoreboard
# TODO detect collision with wall
# TODO detect collision with tail

screen.exitonclick()
