from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg = GREEN)
    label_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)  # Every 8th rep, take a long break
        label_title.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Every 2nd rep, take a short break
        label_title.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)  # Otherwise, do work
        label_title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(number):
    count_min = math.floor(number / 60)
    count_sec = number % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")

    if number > 0:
        global timer
        timer = window.after(1000, count_down, number - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            label_mark.config(text="✔")


# ----------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
"""def smtg(a,b,c):
    print(a)
    print(b)
    print(c)


window.after(1000, smtg, "Hello", 2, 3)"""
# IMAGES CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 23, "bold"))
canvas.grid(column=1, row=1)

# Labels
label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
label_title.grid(column=1, row=0)
label_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_mark.grid(column=1, row=4)

# Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button2 = Button(text="Reset", command=reset, highlightthickness=0)
reset_button2.grid(column=2, row=2)

window.mainloop()
