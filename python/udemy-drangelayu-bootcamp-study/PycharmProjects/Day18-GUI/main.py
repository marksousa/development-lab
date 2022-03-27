import random
from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")

new_turtle = Turtle()
new_turtle.speed("fastest")

def square_draw(turtle):
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)
    turtle.lt(90)
    turtle.fd(250)


# square_draw(timmy_the_turtle)

def dotted_line(turtle):
    turtle.fd(10)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()


# for _ in range(15):
#     dotted_line(timmy_the_turtle)


# colours = ['midnight blue', 'forest green', 'crimson', 'dark slate blue', 'dark cyan', 'orange red', 'indian red', 'gold']

def complex_draw(turtle):
    count = 0
    for i in range(3,11):
        # turtle.color(random.choice(colours))
        turtle.color(random.choice(random_color()))
        while count < i:
            turtle.fd(100)
            turtle.rt(360/i)
            count += 1
        count = 0

def side_draw(numberOfSides, turtle):
    count = 0
    # turtle.color(random.choice(colours))
    turtle.color(random.choice(random_color()))

    while count < numberOfSides:
        turtle.forward(100)
        turtle.right(360/numberOfSides)
        count += 1

# complex_draw(timmy_the_turtle)
# or
# for i in range(3,11):
#     side_draw(i, timmy_the_turtle)

# now let's free the turtle.. it needs to walk alone, aleatory
def aleatoy_draw(turtle, number_of_moves):
    count = 0
    while count < number_of_moves:
        # turtle.color(random.choice(colours))
        turtle.color(random_color())
        turtle.pensize(10)
        turtle.forward(30)
        turtle.right(90 * random.randint(-2,2)) # the turtle changes the direction only on x and y axis
        # turtle.right(45 * random.randint(-2,2)) # try it too
        turtle.speed('fastest')

        count += 1

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b) # returns a tuple


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        new_turtle.color(random_color())
        new_turtle.circle(100)
        new_turtle.setheading(new_turtle.heading() + size_of_gap)

screen = Screen()
screen.colormode(255)
screen.setup(wodth = 0.10, height = 0.10)
# aleatoy_draw(timmy_the_turtle, 500)

draw_spirograph(5)

screen.exitonclick()
