from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.screen.onkey(self.move, "Up")

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
