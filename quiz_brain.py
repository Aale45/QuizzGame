
class QuizBrain:
    def __init__(self,Q_list):
        self.question_num = 0
        self.question_list = Q_list


    def ask(self):

        ask_question = self.question_list[self.question_num]
        self.ans = ask_question.answer
        return input(f"Qno.{(self.question_num + 1)} > {ask_question.question} (True/False): ")


