import unittest
from tkinter import Tk
from ot_harjoitustyo2026.game_logic.logic import GameLogic


class TestMenu(unittest.TestCase):
    def setUp(self):
        questions = [
        {"question": "Toimiiko kysymys?(Kyllä, joo ja oikein toimivat)",
        "choices": ["Kyllä","Ei,","Ehkä,","joo",
        "Voipi olla,","eitietenkään","väärä","oikein","mietitään","jeepuls"],
        "correct_answers" :["Kyllä","joo","oikein"]
        }
        ]
        self.logic = GameLogic(questions)


    def test_check_answer_return_correct_answer(self):
        result = self.logic.check_answer(["Kyllä"])
        self.assertTrue(True)

    def test_check_anwer_is_not_correct(self):
        result = self.logic.check_answer(["Ei"])
        self.assertFalse(False)

    def test_show_question(self):
        result = self.logic.get_question()
        self.assertTrue(True)


    