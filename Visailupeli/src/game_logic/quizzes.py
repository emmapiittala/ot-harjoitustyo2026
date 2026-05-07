'''Handle questions'''
import json

def get_questions():
    '''Return questions from JSON file'''
    with open("src/game_logic/quizzes.json", encoding="utf-8") as file:
        questions = file.read()
    return json.loads(questions)
