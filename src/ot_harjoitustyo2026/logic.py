class GameLogic:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def get_question(self):
        return self.questions[self.current_question]

    def check_answer(self, selected_answers):
        question = self.get_question()
        correct_answers = question["correct_answers"]

        if len(selected_answers) == 0:
            return False

        for answer in selected_answers:
            if answer not in correct_answers:
                return False
        return True

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1

    def check_questions(self):
        return self.current_question < len(self.questions) -1

    def get_selected_answers(self, variables):
        question = self.get_question()
        selected_answers = []

        i = 0
        for variable in variables:
            if variable.get():
                selected_answers.append(question["choices"][i])
            i += 1

        return selected_answers
