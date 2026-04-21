from tkinter import ttk
from ot_harjoitustyo2026.quizzes import questions
class Game:
    def __init__(self, root, handle_quit):
        self._root = root
        self._handle_quit = handle_quit
        self._frame = None
        self.title = None
        self.answers = []
        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0)

    def destroy(self):
        self._frame.destroy()

    def question(self):
        question = questions[0]
        self.title = ttk.Label(
            master=self._frame,
            text=question["question"]
        )

        self.answers = []
        i = 0
        for choice in question ["choices"]:
            answer = ttk.Checkbutton(
            master=self._frame,
            text=choice
        )
            self.answers.append(answer)
            i += 1

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self.question()
        check_button = ttk.Button(
            master=self._frame,
            text="Tarkista",
            #command=self._handle_quit tähän toiminto kun nappia painaa
            # niin näkyy mitkä vastaukset meni oikein
        )
        quit_button = ttk.Button(
            master=self._frame,
            text="Palaa etusivulle",
            command=self._handle_quit
        )
        self.title.grid(row=0, column=0, pady=5, sticky="n")
        i = 0
        for answer in self.answers:
            row = 1 + i // 5
            column = i % 5
            answer.grid(row = row, column = column, padx = 5, pady = 5)
            i += 1

        check_button.grid(row=3, column=0, pady=5)
        quit_button.grid(row=4, column=0, pady=5)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
