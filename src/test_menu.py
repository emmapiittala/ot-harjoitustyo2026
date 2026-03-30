import unittest

class TestMenu(unittest.TestCase):
    def test_text(self):
        text = ("Tähän tulee peli :)")
        self.assertEqual(text, "Tähän tulee peli :)")
        
    def test_start(self):
        start = ("Aloita peli")
        self.assertEqual(start, "Aloita peli")
        
    ##def test_click(self):
        ##keksi miten testataan
        
    ##def test_quit(self):
    ##keksi