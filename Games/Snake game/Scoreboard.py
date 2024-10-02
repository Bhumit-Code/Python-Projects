from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Your score is:{self.score}", align="center", font=("Arial", 10, "normal"))
        self.hideturtle()

    def update(self):
        self.write(f"Your score is:{self.score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=("Arial", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
