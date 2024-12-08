from raw_data import data
from random import randint
from object_model import QuestionModel
from quiz_brain import QuizBrain

question_bank = []
for single_data in data:
    new_question = single_data['question']
    new_answer = single_data['correct_answer']
    new_in_answer = single_data['incorrect_answers']
    new_index = randint(0, 4)
    new_in_answer.insert(new_index, new_answer)
    new_data = QuestionModel(new_question, new_answer, new_in_answer)
    question_bank.append(new_data)

results = QuizBrain(question_bank)
while results.still_show_question():
    results.show_question()
