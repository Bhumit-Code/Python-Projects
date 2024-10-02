from turtle import *
import random

timmy = Turtle()
colormode(255)
def rand_color():
    R = random.randint(0,255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    r_color = (R, G, B)
    timmy.color(r_color)


angle_list = [0, 90, 180, 270]
timmy.width(5)


def rand_walk():
    for _ in range(200):
        angle = random.choice(angle_list)
        rand_color()
        timmy.speed(0)
        timmy.forward(30)
        timmy.setheading(angle)


rand_walk()

screen = Screen()
screen.exitonclick()

