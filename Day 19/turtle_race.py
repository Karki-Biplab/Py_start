# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
# screen.tracer(0)  # Manual screen updates for smooth animation
#
# # Key state flags
# keys = {
#     "w": False,
#     "a": False,
#     "s": False,
#     "d": False,
# }
#
# def press_w(): keys["w"] = True
# def release_w(): keys["w"] = False
# def press_a(): keys["a"] = True
# def release_a(): keys["a"] = False
# def press_s(): keys["s"] = True
# def release_s(): keys["s"] = False
# def press_d(): keys["d"] = True
# def release_d(): keys["d"] = False
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def move():
#     if keys["w"]:
#         tim.forward(5)
#     if keys["s"]:
#         tim.backward(5)
#     if keys["a"]:
#         tim.left(5)
#     if keys["d"]:
#         tim.right(5)
#     screen.update()
#     screen.ontimer(move, 50)  # Loop every 50ms
#
# # Key bindings
# screen.listen()
# screen.onkeypress(press_w, "w")
# screen.onkeyrelease(release_w, "w")
# screen.onkeypress(press_a, "a")
# screen.onkeyrelease(release_a, "a")
# screen.onkeypress(press_s, "s")
# screen.onkeyrelease(release_s, "s")
# screen.onkeypress(press_d, "d")
# screen.onkeyrelease(release_d, "d")
# screen.onkeypress(clear_screen, "c")
#
# move()  # Start movement loop
# screen.mainloop()


from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
tims = []

# Create 6 turtles
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=-100 + i * 40)
    tims.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in tims:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

