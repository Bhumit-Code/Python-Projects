import turtle
from turtle import *
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
bet = turtle.textinput("Choose", "Which color would you like to choose?")
colors = ["red", "yellow", "green", "blue", "purple"]
new_turtle = Turtle()
new_turtle.hideturtle()
all_turtle = []

X = -230
Y = -100
for items in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(items)
    new_turtle.goto(x=X, y=Y)
    Y += 50
    all_turtle.append(new_turtle)
print(all_turtle)


if bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"{bet} Won. You won!")
                break
            else:
                print(f"The {winning_color} Won the race. You lost!")
                break
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)



screen.exitonclick()
