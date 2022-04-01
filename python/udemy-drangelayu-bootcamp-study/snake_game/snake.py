from turtle import Turtle

# CONSTANTS
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# STANDARD MODE
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.creating_snake()
        self.snake_head = self.segments[0]

    def creating_snake(self):
        # The initial snake is represented by 3 white squares
        for coordinates in STARTING_COORDINATES:
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.setposition(coordinates)
            self.segments.append(snake_segment)

    def move(self):
        # to simulate the correct movement behaviour
        # the third segment moves to the second segment position,
        # the second segment moves to the first segment position
        # and so on (must be backward-front, think about it)
        # obs: this range comes from C language
        # for index_segment in range(start=2, stop=0, step=-1):
        # for index_segment in range(start=len(snake.segments)-1, stop=0, step=-1):
        for index_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index_segment - 1].xcor()
            new_y = self.segments[index_segment - 1].ycor()
            self.segments[index_segment].goto(new_x, new_y)

        # needs to move the first segment to forward
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
