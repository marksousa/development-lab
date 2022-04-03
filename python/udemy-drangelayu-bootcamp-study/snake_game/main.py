import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard

SCREEN_LIMIT_TOP = 280
SCREEN_LIMIT_BOTTOM = -280
SCREEN_LIMIT_LEFT = -280
SCREEN_LIMIT_RIGHT = 280


game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(n=0)  # to reduce the delay in snake movement. combine with screen.update() and time.sleep(0.1)

# DONE: create the snake
snake = Snake()
food = Food()
# DONE: create a scoreboard
scoreboard = Scoreboard()

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

    # DONE: detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    # DONE: detect collision with wall
    if snake.snake_head.xcor() > SCREEN_LIMIT_RIGHT or \
       snake.snake_head.xcor() < SCREEN_LIMIT_LEFT or \
       snake.snake_head.ycor() > SCREEN_LIMIT_TOP or \
       snake.snake_head.ycor() < SCREEN_LIMIT_BOTTOM:
        game_is_on = False
        scoreboard.game_is_over()

    # DONE: detect collision with tail
    # SLICING SEGMENTS[1:] RETIRA APENAS O PRIMEIRO ELEMENTO DO ARRAY OU TUPLA TRIPLA...
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_is_over()



screen.exitonclick()
