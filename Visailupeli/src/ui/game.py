"""Game window"""
import tkinter as tk
from tkinter import ttk

from game_logic.logic import GameLogic
from game_logic.quizzes import get_questions
from scores.scores import save_scores
from ui.gameover import GameOver

class Game:
    """Show the game screen
    Attributes:
    root: Application window.
    handle_quit: Callback to the main menu.
    frame: Main frame for the view.
    title: Question tlabel widget.
    logic: Gamelogic handler.
    answer_vars: Variables for selected answers.
    answers: Answers option widgets.
    username: player username. """
    def __init__(self, root, handle_quit, username):
        """Intialize the game view"""
        self.root = root
        self.handle_quit = handle_quit
        self.frame = ttk.Frame(master=self.root)
        self.title = None
        self.logic = GameLogic(get_questions())
        self.answer_vars = []
        self.answers = []
        self.username = username
        self.initialize()

    def pack(self):
        """Display the view center"""
        self.frame.grid(row=0, column=0)

    def destroy(self):
        """Destroy the current UI frame"""
        self.frame.destroy()

    def create_question(self):
        """Create the question and aswer options"""
        question = self.logic.get_question()
        self.title = ttk.Label(
            master=self.frame,
            text=question["question"]
        )

        self.answers = []
        self.answer_vars = []

        for choice in question ["choices"]:
            variable = tk.BooleanVar()
            answer = ttk.Checkbutton(
            master=self.frame,
            text=choice,
            variable = variable
        )
            self.answers.append(answer)
            self.answer_vars.append(variable)

    def show_answers(self):
        """Show answer button"""
        i = 0
        for answer in self.answers:
            row = 1 + i // 5
            column = i % 5
            answer.grid(row = row, column = column, padx = 20, pady = 10, sticky = "w")
            i += 1

    def check_answers(self):
        """Check slected answers and update score and shows next question if answers are correct"""
        self.check_button.config(state="disabled")
        selected_answers = self.logic.get_selected_answers(self.answer_vars)

        if self.logic.check_answer(selected_answers):
            self.score_label.config(text = "Pisteet: " + str(self.logic.score))

            if self.logic.check_questions():
                self.show_next_question()
            else:
                self.show_win()
        else:
            self.show_quit()

    def show_next_question(self):
        """Show a button to the next question."""
        next_button = ttk.Button(
                master=self.frame,
                text="Seuraava kysymys",
                command = self.next_question
        )
        next_button.grid(row=5, column =0, pady=5)

    def next_question(self):
        """Move to the next question and refresh the view."""
        self.logic.next_question()
        widgets = self.frame.winfo_children()

        for widget in widgets:
            widget.destroy()

        self.initialize()

    def restart_game(self):
        """Restart game."""
        self.destroy()
        game = Game(
            self.root,
            self.handle_quit,
            self.username

        )
        game.pack()

    def show_quit(self):
        """Show the game over view and save score"""
        save_scores(self.username, self.logic.score)
        self.destroy()
        game_over = GameOver(
            self.root,
            self.restart_game,
            self.handle_quit,
            self.logic.score,
            False
        )
        game_over.pack()

    def show_win(self):
        """Show the winning view."""
        save_scores(self.username, self.logic.score)
        self.destroy()
        game_over = GameOver(
            self.root,
            self.restart_game,
            self.handle_quit,
            self.logic.score,
            True
        )
        game_over.pack()

    def back_main(self):
        """Return to the main menu"""
        self.destroy()
        self.handle_quit()

    def initialize(self):
        """Create UI layout."""
        self.create_question()
        self.check_button = ttk.Button(
            master=self.frame,
            text="Tarkista",
            command = self.check_answers
        )
        quit_button = ttk.Button(
            master=self.frame,
            text="Palaa etusivulle",
            command=self.back_main
        )
        self.title.grid(row=0,column=0,columnspan=5,pady=10,sticky="n")
        self.show_answers()

        self.score_label = ttk.Label(
            master = self.frame,
            text = "Pisteet: " + str(self.logic.score)
        )
        self.score_label.grid(row=6, column = 0)
        self.check_button.grid(row=3, column=0, pady=5)
        quit_button.grid(row=4, column=0, pady=5)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column = 0)
        for column in range(5):
            self.frame.grid_columnconfigure(column, weight=1, minsize=150)
            