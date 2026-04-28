"""Application UI"""
from ui.menu import Menu
from ui.game import Game

class UI:
    """Handle different views"""
    def __init__(self, root):
        """Attributes:
    _root: Application window
    _current_view:currently view"""
        self._root = root
        self._current_view = None

    def start(self):
        """ 'Start' game and show application menu"""
        self._show_menu()

    def _show_menu(self):
        """Show the main menu"""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = Menu(
            self._root,
            self._show_game
        )
        self._current_view.pack()

    def _show_game(self):
        """Show the game view """
        self._clear_view()
        self._current_view = Game(
            self._root,
            self._show_menu)
        self._current_view.pack()

    def _clear_view(self):
        """Clear the current view"""
        if self._current_view:
            self._current_view.destroy()
