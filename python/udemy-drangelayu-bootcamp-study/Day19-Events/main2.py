import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    turtle_instance = Turtle()
    turtle_instance.shape("turtle")
    turtle_instance.color(colors[turtle_index])
    turtle_instance.penup()
    turtle_instance.setpos(x=-200, y=(-100 + turtle_index * 50))
    all_turtles.append(turtle_instance)

if player_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        # 250 - (40/2) = 230 - each turtle is a 40x40 square.

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")


screen.exitonclick()

