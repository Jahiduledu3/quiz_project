import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_num = 0
        self.score = 0

    def still_show_question(self):
        return self.question_num < len(self.question_list)

    def show_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        q_text = html.unescape(current_question.quiz_question)
        user_answer = input(f"Q.{self.question_num}: {q_text}\n{current_question.quiz_in_answer}:")
        self.check_answer(user_answer, current_question.quiz_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Your answer is right!')

        else:
            print('Your answer is wrong!')
        print(f'The correct answer was:{correct_answer}.')
        print(f'Your score is {self.score}/{self.question_num}')
        print('\n')
