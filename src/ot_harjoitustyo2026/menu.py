from tkinter import ttk, constants


class Menu:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.grid(row=5,column=5)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title = ttk.Label(
            master=self._frame,
            text="Tähän tulee peli"
        )
        rules = ttk.Label(
            master=self._frame,
            text="Tähän tule jotain sääntöjä jeejee"
        )
        start_button = ttk.Button(
            master=self._frame,
            text="Aloita Peli",
            command=self._handle_start
        )

        title.grid(columnspan=1, sticky=constants.NSEW, padx=5, pady=5)
        rules.grid(columnspan=2, sticky=constants.NSEW, padx=5, pady=5)
        start_button.grid(columnspan=3, sticky=constants.NSEW, padx=5, pady=5)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
