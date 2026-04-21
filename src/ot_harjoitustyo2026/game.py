import tkinter as tk
from tkinter import ttk
from ot_harjoitustyo2026.quizzes import questions
from ot_harjoitustyo2026.logic import GameLogic
from ot_harjoitustyo2026.gameover import GameOver

class Game:
    def __init__(self, root, handle_quit):
        self._root = root
        self._handle_quit = handle_quit
        self._frame = ttk.Frame(master=self._root)
        self.title = None
        self.logic = GameLogic(questions)
        self.answer_vars = []
        self.answers = []
        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0)

    def destroy(self):
        self._frame.destroy()

    def create_question(self):
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
        self.check_button.config(state="disabled")
        selected_answers = self.logic.get_selected_answers(self.answer_vars)

        if self.logic.check_answer(selected_answers):
            self.show_next_question()
        else:
            self.show_quit()

    def show_next_question(self):
        next_button = ttk.Button(
                master=self._frame,
                text="Seuraava kysymys",
                command = self.next_question
        )
        next_button.grid(row=5, column =0, pady=5)

    def next_question(self):
        self.logic.next_question()
        widgets = self._frame.winfo_children()

        for widget in widgets:
            widget.destroy()

        self._initialize()

    def restart_game(self):
        self.destroy()
        game = Game(
            self._root,
            self._handle_quit
        )
        game.pack()

    def show_quit(self):
        self.destroy()
        game_over = GameOver(
            self._root,
            self.restart_game,
            self._handle_quit
        )
        game_over.pack()

    def _initialize(self):
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
