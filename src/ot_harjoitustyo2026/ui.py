from ot_harjoitustyo2026.menu import Menu
from ot_harjoitustyo2026.game import Game

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_menu()

    def _show_menu(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = Menu(
            self._root,
            self._show_game
            )
        self._current_view.pack()
        
    def _show_game(self):
        self._clear_view()
        self._current_view = Game(
            self._root,
            self._show_menu)
        self._current_view.pack()
        
    def _clear_view(self):
        if self._current_view:
            self._current_view.destroy()
        