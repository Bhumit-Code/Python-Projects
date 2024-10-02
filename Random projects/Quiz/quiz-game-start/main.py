from data import question_data
from quiz_brain import *

question_bank = []
for items in question_data:
    text = items["question"]
    answer = items["correct_answer"]
    list1 = text, answer
    question_bank.append(list1)


quiz = QuizBrain(question_bank)
number = quiz.update()




