"""Game over window"""
from tkinter import ttk

class GameOver:
    """Show when the game ends
    Attributes:
    _root: Application window.
    _handle_start: Callback to return to menu. 
    _handle_quit: Callback to back menu"""
    def __init__(self, root, handle_start,handle_quit):
        self._root = root
        self._handle_start = handle_start
        self._handle_quit = handle_quit
        self._frame = None
        self._initialize()

    def pack(self):
        """Display the view center"""
        self._frame.place(relx=0.5, rely=0.5, anchor="center")

    def destroy(self):
        """Destroy the current UI frame"""
        self._frame.destroy()

    def start_game(self):
        """Close the current view and start new game"""
        self.destroy()
        self._handle_start()

    def quit_game(self):
        """Close the current view and return to menu"""
        self.destroy()
        self._handle_quit()

    def _initialize(self):
        """Create UI and make labels and buttons"""
        self._frame = ttk.Frame(master=self._root)

        title = ttk.Label(
            master=self._frame,
            text="Hävisit pelin"
        )
        rules = ttk.Label(
            master=self._frame,
            text="Voit halutessa aloittaa uuden pelin tai palata etusivulle"
        )
        start_button = ttk.Button(
            master=self._frame,
            text="Aloita Peli",
            command=self.start_game
        )
        quit_button = ttk.Button(
            master=self._frame,
            text="Palaa etusiivulle",
            command=self.quit_game
        )

        title.grid(row=0, column=0, columnspan=5, pady=10)
        rules.grid(row=3, column=0, columnspan=5, pady=10)
        start_button.grid(row=4, column=0, columnspan=5, pady=10)
        quit_button.grid(row=5, column=0, columnspan=5, pady=10)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
