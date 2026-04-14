from tkinter import ttk, constants


class Game:
    def __init__(self, root, handle_quit):
        self._root = root
        self._handle_quit = handle_quit
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(side=constants.TOP)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title = ttk.Label(
            master=self._frame,
            text="Oletko valmis peliin?"
        )
        quit_button = ttk.Button(
            master=self._frame,
            text="Lopeta peli",
            command=self._handle_quit
        )

        title.grid(row=0, column=0, pady=5)
        quit_button.grid(row=1, column=0, pady=5)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
