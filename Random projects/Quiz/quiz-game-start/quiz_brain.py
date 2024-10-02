from question_model import Question


class QuizBrain:
    def __init__(self, q_list):
        self.que_number = 0
        self.que_list = q_list

    def update(self, current_number=0, new_score=0):
        while current_number < len(self.que_list):
            current_number = current_number
            Question.text = self.que_list[current_number][0]
            Question.answer = self.que_list[current_number][1]
            current_number += 1
            new_score = new_score
            ask = input(f"Q.{current_number} {Question.text} (True/False)?")
            if ask == Question.answer:
                print("You got it right!")
                print(f"The correct answer was: {Question.answer}")
                print(f"Your current score is: {new_score+1}/{current_number}")
                new_score+=1
            elif ask != Question.answer:
                print('Your\'re Wrong!')
                print(f"Your current score is: {new_score}/{current_number}")

