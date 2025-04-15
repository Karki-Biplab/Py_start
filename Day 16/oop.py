# # import another_module
# # print(another_module.another_variable)
# # import screen
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.shapesize(5,5)
# timmy.forward(100)
# timmy.backward(200)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squiritle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
table.header_style = "upper"
print(table)

