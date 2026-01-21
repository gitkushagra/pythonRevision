from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q_data in question_data:
    question_bank.append(Question(q_data["text"],q_data["answer"]))

myquiz = QuizBrain(question_bank)

while myquiz.isQuestionAvailable():
    myquiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {myquiz.score}/{myquiz.q_no}")