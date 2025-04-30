from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.left_score}", align="center", font=("Courier", 24, "bold"))  # Smaller font
        self.goto(100, 260)
        self.write(f"{self.right_score}", align="center", font=("Courier", 24, "bold"))  # Smaller font

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER! {winner} wins!", align="center", font=("Courier", 30, "bold"))
