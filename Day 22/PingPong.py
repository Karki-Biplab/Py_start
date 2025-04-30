from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.width(5)
    center_line.penup()
    center_line.goto(0, 300)  # Start at the top
    center_line.setheading(270)  # Point down
    center_line.pendown()
    center_line.forward(600)  # Draw the line all the way down
    center_line.hideturtle()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Ping Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Draw the center line on the game board
draw_center_line()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()

    # Check if any player has won the game (score = 5)
    if scoreboard.left_score == 5:
        scoreboard.game_over("Left Player")
        game_is_on = False

    if scoreboard.right_score == 5:
        scoreboard.game_over("Right Player")
        game_is_on = False

screen.exitonclick()
