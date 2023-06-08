from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    new_question = Question(i["text"], i["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

score = 0
num = 1
for i in question_bank:
    b = quiz_brain.ask()
    if b == quiz_brain.ans:
        score += 1
   
        print(f"Your answer is wrong! \n Your current score is {score}/{num}")
    else:
        print("Your answer is wrong!")
        print(f"Your current score is {score}/{num}")
    quiz_brain.question_num += 1
    num += 1





























'''
                               METHOD 2(easy one)
score = 0
num = 1

def ask_q():
    global score, num
    for i in question_bank:
        print(f"Your score is {score}")
        q = input(f"Q.No.{num} > {i.question} (True/False): ")
        num += 1
        if q == i.answer:
            print("Your answer is correct!")
            score += 1
        else:
            print("Your answer is wrong!")
    print(f"Your final score is {score}")


ask_q()

'''
