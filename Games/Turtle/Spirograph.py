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

def spiro(gap):
    for _ in range(int(360/gap)):
        rand_color()
        timmy.speed(0)
        timmy.circle(100)
        timmy.setheading(timmy.heading()+ gap)

spiro(5)

screen = Screen()
screen.exitonclick()