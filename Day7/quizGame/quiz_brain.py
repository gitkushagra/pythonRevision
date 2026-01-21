class QuizBrain:
    def __init__(self, ques_list):
        self.q_no = 0
        self.score = 0
        self.q_list = ques_list

    def isQuestionAvailable(self):
        return self.q_no < len(self.q_list)

    
    def next_question(self):
        current_ques = self.q_list[self.q_no]
        self.q_no += 1
        user_input =input(f"Q.{self.q_no}: {current_ques.text} (True/False)?").lower()
        self.check_ans(user_input,current_ques)


    def check_ans(self,user_input,current_ques):
        if user_input == current_ques.answer.lower():
            print("You got it right!")
            self.score += 1
            
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_ques.answer}.")
        print(f"Your current score is: {self.score}/{self.q_no}\n")
        

