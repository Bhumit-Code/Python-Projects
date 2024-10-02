BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import time

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(label_title, text="French")
    canvas.itemconfig(label_word, text=current_card["French"])


def flip_card():
    canvas.itemconfig(label_title, text="English")
    canvas.itemconfig(label_word, text=current_card["English"])


window = Tk()
window.title("Flashy")
window.minsize(width=600, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
label_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
label_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")

button_wrong = Button(image=wrong, width=100, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1, columnspan=2, sticky="w")

button_right = Button(image=right, width=100, highlightthickness=0, command=flip_card)
button_right.grid(column=1, row=1, columnspan=2, sticky="e")

next_card()

window.mainloop()
