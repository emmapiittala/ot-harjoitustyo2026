"""Game window"""
import tkinter as tk
from tkinter import ttk
from game_logic.quizzes import questions
from game_logic.logic import GameLogic
from ui.gameover import GameOver

class Game:
    """Show the game screen
    Attributes:
    _root: Application window.
    _handle_quit: Callback to the main menu.
    _frame: Main frame for the view.
    title: Question tlabel widget.
    logic: Gamelogic handler.
    answer_vars: Variables for selected answers.
    answers: Answers option widgets."""
    def __init__(self, root, handle_quit):
        """Intialize the game viiew"""
        self._root = root
        self._handle_quit = handle_quit
        self._frame = ttk.Frame(master=self._root)
        self.title = None
        self.logic = GameLogic(questions)
        self.answer_vars = []
        self.answers = []
        self._initialize()

    def pack(self):
        """Display the view center"""
        self._frame.grid(row=0, column=0)

    def destroy(self):
        """Destroy the current UI frame"""
        self._frame.destroy()

    def create_question(self):
        """Create the question and aswer options"""
        question = self.logic.get_question()
        self.title = ttk.Label(
            master=self._frame,
            text=question["question"]
        )

        self.answers = []
        self.answer_vars = []

        for choice in question ["choices"]:
            variable = tk.BooleanVar()
            answer = ttk.Checkbutton(
            master=self._frame,
            text=choice,
            variable = variable
        )
            self.answers.append(answer)
            self.answer_vars.append(variable)

    def check_answers(self):
        """Check slected answers, validate them using game logic, and update view"""
        self.check_button.config(state="disabled")
        selected_answers = self.logic.get_selected_answers(self.answer_vars)

        if self.logic.check_answer(selected_answers):
            self.show_next_question()
        else:
            self.show_quit()

    def show_next_question(self):
        """Show a button to the next question."""
        next_button = ttk.Button(
                master=self._frame,
                text="Seuraava kysymys",
                command = self.next_question
        )
        next_button.grid(row=5, column =0, pady=5)

    def next_question(self):
        """Move to the next question and refresh the view."""
        self.logic.next_question()
        widgets = self._frame.winfo_children()

        for widget in widgets:
            widget.destroy()

        self._initialize()

    def restart_game(self):
        """Restart game."""
        self.destroy()
        game = Game(
            self._root,
            self._handle_quit
        )
        game.pack()

    def show_quit(self):
        """Show the game over view"""
        self.destroy()
        game_over = GameOver(
            self._root,
            self.restart_game,
            self._handle_quit
        )
        game_over.pack()

    def _initialize(self):
        """Create question elements, buttons and build the UI layout."""
        self.create_question()
        self.check_button = ttk.Button(
            master=self._frame,
            text="Tarkista",
            command = self.check_answers
        )
        quit_button = ttk.Button(
            master=self._frame,
            text="Palaa etusivulle",
            command=self._handle_quit
        )
        self.title.grid(row=0, column=0, columnspan=5, pady=10, sticky="n")
        i = 0
        for answer in self.answers:
            row = 1 + i // 5
            column = i % 5
            answer.grid(row = row, column = column, padx = 20, pady = 10, sticky = "w")
            i += 1

        self.check_button.grid(row=3, column=0, pady=5)
        quit_button.grid(row=4, column=0, pady=5)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid(row=0, column = 0)
        for column in range(5):
            self._frame.grid_columnconfigure(column, weight=1, minsize=150)
