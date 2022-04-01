import time
from turtle import Screen
from snake import Snake

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(n=0)  # to reduce the delay in snake movement. combine with screen.update() and time.sleep(0.1)

# DONE: create the snake
snake = Snake()

# DONE: control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # DONE: move the snake
    snake.move()

# TODO: detect collision with food
# TODO: create a scoreboard
# TODO: detect collision with wall
# TODO: detect collision with tail

screen.exitonclick()
