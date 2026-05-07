"""Application UI"""
from ui.menu import Menu
from ui.game import Game

class UI:
    """Handle different views
    Attributes:
    _root: Application window
    _current_view:currently view"""
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        """ 'Start' game and show application menu"""
        self.show_menu()

    def show_menu(self):
        """Show the main menu"""
        if self.current_view:
            self.current_view.destroy()

        self.current_view = Menu(
            self.root,
            self.show_game
        )
        self.current_view.pack()

    def show_game(self, username):
        """Show the game view """
        self.clear_view()
        self.current_view = Game(
            self.root,
            self.show_menu,
            username
            )
        self.current_view.pack()

    def clear_view(self):
        """Clear the current view"""
        if self.current_view:
            self.current_view.destroy()
