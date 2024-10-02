from turtle import *
import random

timmy = Turtle()


def color():
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)


def shape():
    num_side = 3
    while num_side < 11:
        num_side = num_side
        angle = 360 / num_side
        color()
        for _ in range(num_side):
            timmy.forward(100)
            timmy.right(angle)


        num_side += 1


shape()
screen = Screen()
screen.exitonclick()
