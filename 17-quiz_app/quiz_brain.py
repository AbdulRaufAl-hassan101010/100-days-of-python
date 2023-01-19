class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.scores = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        is_correct = False

        if user_answer.lower() == answer.lower():
            self.scores += 1
            is_correct = True

        print(f"You scored {self.scores}/{self.question_number}")
        return is_correct

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        # wait until user input is true/false
        is_appectable_input = True
        while is_appectable_input:
            user_answer = input(
                f"Q.{self.question_number}: {question.text} (True/False): ").lower()

            if user_answer in ["true", "false"]:
                break

        self.check_answer(user_answer, question.answer)
