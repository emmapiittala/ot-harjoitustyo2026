"""Game logic"""
class GameLogic:
    def __init__(self, questions):
        """Handle questions logic and aswers
        Attributes: 
        questions: List of questions
        current_question: Index of current question"""
        self.questions = questions
        self.current_question = 0
        self.points = 0
        self.score = 0
        

    def get_question(self):
        """Return current question"""
        return self.questions[self.current_question]

    def check_answer(self, selected_answers):
        """Check if the selected answer is correct and update score """
        question = self.get_question()
        correct_answers = question["correct_answers"]
        points = 0
        
        if len(selected_answers) == 0:
            return False

        for answer in selected_answers:
            if answer not in correct_answers:
                return False
            else: 
                points += 1
                
        self.score += points
        return True

    def next_question(self):
        """Move to the next question."""
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1

    def check_questions(self):
        """Check if thre are more questions left."""
        return self.current_question < len(self.questions) -1

    def get_selected_answers(self, variables):
        """Get selected answers from variables"""
        question = self.get_question()
        selected_answers = []

        i = 0
        for variable in variables:
            if variable.get():
                selected_answers.append(question["choices"][i])
            i += 1

        return selected_answers

