from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(x=0, y=270)
        self.write(f"Your score is:{self.score}", align="center", font=("Arial", 10, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} HighScore = {self.high_score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=("Arial", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
