# from turtle import Turtle, Screen
# import another_module
#
# print(another_module.another_variable)
# # next lines works but the other import is well-suited
# # import turtle
# # timmy = turtle.Turtle()
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(1000)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])  # using method
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = "l"  # attribute change

print(table)
