from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Verdana', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,260)
        self.penup()
        self.color("white")
        self.refresh()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_is_over(self):
        self.goto(0,0)
        self.write("Game is Over!", move=False, align=ALIGNMENT, font=FONT)
