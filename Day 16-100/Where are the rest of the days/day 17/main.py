# # class User:
# #     def __init__(self,):
# #         print("new user being created")
# #
# #
# # user_1= User()
# # user_1.id = "001"
# # user_1.username = "bhavishya"
# #
# # print(user_1.username)
# #
# # user_2 = User()
# # user_2.id = "002"
# # user_2.username = "jack"
# #
# # print(user_2.username)
#
# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
# user_1 = User("001","bhavishya")
# print(user_1.id,"\n",user_1.username)
# user_2 = User("002","sre ")

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
