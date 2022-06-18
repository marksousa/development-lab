import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

game_is_on = True
MOVE_DISTANCE = 20

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)


screen.exitonclick()
