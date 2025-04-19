import colorgram
import random
import turtle as t
from turtle import Turtle, Screen

t.colormode(255)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

colors = colorgram.extract('image.jpg', 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

dot_count = 0
for _ in range(100):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    dot_count += 1

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
