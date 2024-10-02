from turtle import *

timmy = Turtle()
screen = Screen()


def clear_screen1():
    timmy.clear()
    timmy.penup()
    timmy.home()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_clockwise():
    timmy.left(10)


def move_countercw():
    timmy.right(10)


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_countercw)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen1)

screen.exitonclick()
