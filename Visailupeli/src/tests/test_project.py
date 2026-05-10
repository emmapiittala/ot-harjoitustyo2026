"""Test GameLogic class"""
import unittest
from game_logic.logic import GameLogic
from game_logic.quizzes import get_questions
from scores.scores import get_scores, save_scores, get_top5_scores


class TestMenu(unittest.TestCase):
    """Tests for game logic."""
    def setUp(self):
        questions = [
        {"question":"Testi",
        "choices":["1","2","3","4","5","6","7","8","9","10"],
        "correct_answers":["1","2"]},
        
        {"question":"Testi2",
        "choices":["a","b","c","d","e","f","g","h","i","j"],
        "correct_answers":["a","b","c"]}]

        self.logic = GameLogic(questions)

    def test_check_answer_return_correct_answer(self):
        """Test corrent answer returns True."""
        self.logic.questions= [
        {"question": "testikysymys 0",
        "choices": ["1","2","3","4",
        "5","6","7","8","9","10"],
        "correct_answers" :["2"]}]
        self.logic.current_question = 0
        result = self.logic.check_answer(["2"])
        self.assertTrue(result)
    
    def test_check_multiply_answer_is_correct(self):
        """Test multiply answers return true"""
        self.logic.questions = [
        {"question": "Ohitataan shuffle tällä kysymyksellä",
        "choices":["Joo", "Ei", "Kyllä"],
        "correct_answers":["Joo","Kyllä"]
        }]
        self.logic.current_question = 0
        result = self.logic.check_answer(["Joo","Kyllä"])
        self.assertTrue(result)

    def test_check_answer_is_not_correct(self):
        """Test wrong answer return False."""
        self.logic.questions = [
        {"question": "testikysymys 1",
        "choices": ["a","b","c","d","e","f","g","h","i","j"],
        "correct_answers" :["a"]
         }]
        self.logic.current_question = 0
        result = self.logic.check_answer(["b"])
        self.assertFalse(result)

    def test_show_question(self):
        """Test getting current question."""
        result = self.logic.get_question()
        self.assertTrue(result)

    def test_no_answer(self):
        """Test empty answer return False."""
        result = self.logic.check_answer([])
        self.assertFalse(result)

    def test_next_question(self):
        """Test moving to next question."""
        result = self.logic.current_question
        self.logic.next_question()
        self.assertEqual(self.logic.current_question, result + 1)

    def test_last_question(self):
        """Test no more questions."""
        self.logic.current_question = len(self.logic.questions) - 1
        self.assertFalse(self.logic.check_questions())

    def test_get_quizzes(self):
        """Test get question scores.py"""
        result = get_questions()
        self.assertTrue(result)

    def test_get_scores(self):
        """Tes get scores scooes.py"""
        result = get_scores()
        self.assertTrue(result)

    def test_save_scores(self):
        """Tes save score and nick scores.py"""
        save_scores("Emma", 5)
        scores = get_scores()
        self.assertTrue(scores)

    def test_top5_scores(self):
        """Tes get top5 scores"""
        save_scores("Emma", 5)
        save_scores("Matti", 6)
        save_scores("Maija", 9)
        scores = get_top5_scores()
        self.assertTrue(scores)
