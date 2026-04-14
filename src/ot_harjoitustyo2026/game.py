from tkinter import ttk, constants


class Game:
    def __init__(self, root, handle_quit):
        self._root = root
        self._handle_quit = handle_quit
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title = ttk.Label(
            master=self._frame,
            text="Tässä kysymys X"
        )
        answer1 = ttk.Checkbutton(master=self._frame, text="answer1")
        answer2 = ttk.Checkbutton(master=self._frame, text="answer2")
        answer3 = ttk.Checkbutton(master=self._frame, text="answer3")
        answer4 = ttk.Checkbutton(master=self._frame, text="answer4")
        answer5 = ttk.Checkbutton(master=self._frame, text="answer5")
        answer6 = ttk.Checkbutton(master=self._frame, text="answer6")
        answer7 = ttk.Checkbutton(master=self._frame, text="answer7")
        answer8 = ttk.Checkbutton(master=self._frame, text="answer8")
        answer9 = ttk.Checkbutton(master=self._frame, text="answer9")
        answer10 = ttk.Checkbutton(master=self._frame, text="answer10")
        
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
        
        title.grid(row=0, column=0, pady=5, sticky="n")
        answer1.grid(row=1,column=0)
        answer2.grid(row=1, column=1)
        answer3.grid(row=1,column=2)
        answer4.grid(row=1, column=3)
        answer5.grid(row=1,column=4)
        answer6.grid(row=2, column=0)
        answer7.grid(row=2,column=1)
        answer8.grid(row=2, column=2)
        answer9.grid(row=2,column=3)
        answer10.grid(row=2, column=4)
        check_button.grid(row=3, column=0, pady=5)
        quit_button.grid(row=5, column=0, pady=5)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
