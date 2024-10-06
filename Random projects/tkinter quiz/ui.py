from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
x1=300
y1=250
x2=300
y2=250



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 207, text="some question here", width = 280,
                                                     font=("Arial", 20, "bold"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20,pady=20)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(width=100, height=100, image=self.true_img, highlightthickness=0,
                                  command=self.true_clicked)
        self.true_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(width=100, height=100, image=self.false_img, highlightthickness=0,
                                   command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)