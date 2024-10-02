import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
input_states = []
score = 0
while score < 50:
    ans_states = screen.textinput(title=f"{score}/50 Guess the state", prompt="Whats the another state?").title()
    print(f"You typed {ans_states}")
    score = score

    if ans_states == "Exit":
        missing_states = [name for name in states if name not in input_states]
        to_learn_states = {"States to learn": missing_states}
        leftover_states = pandas.DataFrame(to_learn_states)
        leftover_states.to_csv("States to learn.csv")
        break
    elif ans_states in input_states:
        print(f"{ans_states} is already guessed by you!")

    for items in states:
        if items == ans_states and ans_states not in input_states:
            timmy = turtle.Turtle()
            timmy.hideturtle()
            timmy.penup()
            state_axis = data[data["state"] == ans_states]
            timmy.goto(x=state_axis.x.item(), y=state_axis.y.item())
            timmy.write(arg=ans_states)
            input_states.append(ans_states)
            score += 1

timmy2 = turtle.Turtle()
timmy2.hideturtle()
timmy2.penup()
timmy2.goto(x=-50, y=250)
timmy2.write(arg="FINISHED", align="Left", font=("Arial", 20, "normal"))

turtle.exitonclick()
