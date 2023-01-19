from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# completed quiz
print("You have completed the quiz")
