from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    queston_text = question["text"]
    queston_text = question["answer"]
    new_question = Question(question_text, question_answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
