import unittest
from ot_harjoitustyo2026.menu import Menu
from tkinter import Tk
from ot_harjoitustyo2026.ui import UI


class TestMenu(unittest.TestCase):
    def setUp(self):
       self.root = Tk()
       self.root.withdraw()
       window = Tk()

    def tearDown(self):
        self.root.destroy()
        
    def handle_start(self):
        pass
    
    def current_view(self):
        pass
    
    def test_menu_creating(self):
        menu = Menu(self.root, self.handle_start)
        self.assertIsNotNone(menu)
    
    def test_menu_destroy(self):
        menu = Menu(self.root, self.handle_start)
        menu.destroy()
        self.assertTrue(True)
        
    def test_ui_start(self):
        ui = UI(self.root)
        ui.start()
        self.assertTrue(True)
    
    def test_ui_current_view(self):
        ui = UI(self.root)
        ui.start()
        self.assertIsNotNone(ui._current_view)
        
    def test_ui_show_menu(self):
        ui = UI(self.root)
        ui.start()
        ui._show_menu()
        ui._show_game()
        self.assertIsNotNone(ui._current_view)
        
    def test_ui_show_game(self):
        ui = UI(self.root)
        ui.start()
        ui._show_game()
        ui._show_menu()
        self.assertTrue(True)
        
    def test_ui_clear_view(self):
        ui = UI(self.root)     
        ui.start()
        ui._clear_view()
        self.assertTrue(True)
        
    def test_ui_cleer_view_false(self):
        ui = UI(self.root)
        ui._clear_view()
        self.assertIsNone(ui._current_view)
        
