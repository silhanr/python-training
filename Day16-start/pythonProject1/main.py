# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# print(timmy)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["electric","water","fire"])

table.align = "l"
print(table)