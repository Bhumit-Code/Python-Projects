# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Hirst.jpg', 30)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import *
import random

colormode(255)

color_list = [(216, 173, 3), (217, 3, 35), (19, 46, 156), (225, 3, 1), (7, 95, 204),
              (37, 206, 51), (10, 26, 62), (81, 190, 226), (215, 65, 3),
              (62, 17, 1), (3, 192, 223), (223, 163, 86), (221, 208, 99),
              (71, 3, 21), (251, 70, 24), (214, 127, 209), (149, 218, 175),
              (60, 90, 239), (7, 162, 12), (242, 63, 86), (117, 208, 134),
              (115, 81, 2), (221, 204, 3), (253, 4, 46), (164, 52, 83), (234, 165, 184)]

timmy = Turtle()
timmy.hideturtle()


def new_line():
    timmy.left(90)
    timmy.forward(20)
    timmy.left(90)
    timmy.forward(200)
    timmy.right(180)


def dots():
    for _ in range(10):
        rand_color = random.choice(color_list)
        timmy.penup()
        timmy.forward(10)
        timmy.dot(10, rand_color)
        timmy.forward(10)


for _ in range(10):
    timmy.speed(0)
    dots()
    new_line()

screen = Screen()
screen.exitonclick()
