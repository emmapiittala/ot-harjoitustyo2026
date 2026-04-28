import unittest
from tkinter import Tk
from game_logic.logic import GameLogic


class TestMenu(unittest.TestCase):
    def setUp(self):
        questions = [
        {"question": "Toimiiko kysymys?(Kyllä, joo ja oikein toimivat)",
        "choices": ["Kyllä","Ei,","Ehkä,","joo",
        "Voipi olla,","eitietenkään","väärä","oikein","mietitään","jeepuls"],
        "correct_answers" :["Kyllä","joo","oikein"]
        },
        {"question": "Toimiiko kysymys 2? ja vaihtuuko vastaukset (oikeata k ja voipi oll)",
     "choices": ["k","E,","Ehk,","juu",
                 "Voipi oll","eitiete","vääräp","oikexin","mietitäänstten","jeepulsjee"],
     "correct_answers" :["k","Voipi oll"]
     },     {"question": "Toimiiko kysymys 3? (yksi vain oikein a)",
     "choices": ["a","b","c","d",
                 "e,","f","g","h","i","j"],
     "correct_answers" :["a"]
     }
    ]
        self.logic = GameLogic(questions)


    def test_check_answer_return_correct_answer(self):
        result = self.logic.check_answer(["Kyllä"])
        self.assertTrue(result)

    def test_check_answer_is_not_correct(self):
        result = self.logic.check_answer(["Ei"])
        self.assertFalse(result)

    def test_show_question(self):
        result = self.logic.get_question()
        self.assertTrue(result)

    def test_no_answer(self):
        result = self.logic.check_answer([])
        self.assertFalse(result)
        
    def test_next_question(self):
        result = self.logic.current_question
        self.logic.next_question()
        self.assertEqual(self.logic.current_question, result + 1)
        
    def test_last_question(self):
        self.logic.current_question = len(self.logic.questions) - 1
        self.assertFalse(self.logic.check_questions())
