# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# # timmy_the_turtle.shapee()
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
# screen = Screen()
# screen.exitonclick()

# import turtle
# import heroes
# print(heroes.gen())

# import turtle as t
#
# tim = t.Turtle()
#
# # for _ in range(15):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
#
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)



# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.speed("fastest")  # Speeds up the drawing
#
# # Function to draw a regular polygon
# def draw_polygon(sides, length):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(length)
#         tim.right(angle)
#
# # Loop from 4 (square) to 19 sides (15 more layouts)
# for sides in range(4, 20):
#     tim.color(random.random(), random.random(), random.random())  # Random color
#     draw_polygon(sides, 100)
# t.done()



# import turtle as t
# import random
# tim = t.Turtle()
# for sides in range(3, 20):  # From square to 19-sided polygon
#     tim.color(random.random(), random.random(), random.random())
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.pensize(10)
#         tim.forward(100)
#         tim.right(angle)


import turtle as t
from turtle import Turtle, Screen
import random
tim = t.Turtle()
#
# directions = [0, 90, 180, 270]
# for i in range(200):
#     tim.color(random.random(), random.random(), random.random())
#     tim.pensize(7)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

for sides in range(72):
    tim.color(random.random(), random.random(), random.random())
    # angle = 1
    # tim.forward(1)

    #move = random.randint(0, 1)
    for _ in range(1):
        tim.speed(100)
        tim.pensize(1)
        tim.circle(100)
        tim.right(5)

screen = Screen()
screen.exitonclick()
