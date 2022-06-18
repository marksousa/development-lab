from turtle import Turtle

MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)

    def move(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor() + MOVE_DISTANCE)
