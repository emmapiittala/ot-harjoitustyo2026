"""Gameover/"winning(last question) window"""
from tkinter import ttk
from scores.scores import get_scores

class GameOver:
    """Show when the game ends
    Attributes:
    root: Application window.
    handle_start: Callback to return to menu. 
    handle_quit: Callback to back menu
    frame:
    score:
    win:"""
    def __init__(self, root, handle_start, handle_quit, score, win):
        self.root = root
        self.handle_start = handle_start
        self.handle_quit = handle_quit
        self.frame = None
        self.score = score
        self.win = win
        self.initialize()

    def pack(self):
        """Display the view center"""
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

    def destroy(self):
        """Destroy the current UI frame"""
        self.frame.destroy()

    def start_game(self):
        """Close the current view and start new game"""
        self.destroy()
        self.handle_start()

    def quit_game(self):
        """Close the current view and return to menu"""
        self.destroy()
        self.handle_quit()

    def top_5_scores(self):
        """Show top5 score"""
        scores_all = get_scores()
        top5_score = sorted(scores_all,
            key = lambda score: score ["score"],
            reverse=True)
        top5_text = "Top 5 pelaajat ja pisteet:\n"

        for user in top5_score[:5]:
            top5_text += (user["username"] + ": " + str(user["score"]) + "\n")

        top_score_label = ttk.Label(
            master = self.frame,
            text = top5_text,
            justify="center"
        )
        top_score_label.grid(row=2, column=0, columnspan=5, pady=10)

    def initialize(self):
        """Create UI and make labels and buttons"""
        self.frame = ttk.Frame(master=self.root)

        if self.win:
            game_text = ttk.Label(
                master=self.frame,
                text="Pääsit loppuun! Sait pisteitä: " + str(self.score))
        else:
            game_text = ttk.Label(
                master=self.frame,
                text="Voi ei! Hävisit pelin! Sait pisteitä:" + str(self.score))

        game_text.grid(row=0, column=0, columnspan=5, pady=10)
        self.top_5_scores()

        rules = ttk.Label(
            master=self.frame,
            text="Voit halutessa aloittaa uuden pelin tai palata etusivulle"
        )
        start_button = ttk.Button(
            master=self.frame,
            text="Aloita Peli",
            command=self.start_game
        )
        quit_button = ttk.Button(
            master=self.frame,
            text="Palaa etusivulle",
            command=self.quit_game
        )
        rules.grid(row=3, column=0, columnspan=5, pady=10)
        start_button.grid(row=4, column=0, columnspan=5, pady=10)
        quit_button.grid(row=5, column=0, columnspan=5, pady=10)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
