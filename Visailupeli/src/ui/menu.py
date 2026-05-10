"""Main menu view"""
from tkinter import ttk

class Menu:
    """Show the main menu and game rules and username input
    Attributes:
    root: Application window.
    handle_start: Callbaxk to start the game.
    frame: Main frame for the view.
    username: player username."""
    def __init__(self, root, handle_start):
        """Intialize the menu view."""
        self.root = root
        self.handle_start = handle_start
        self._frame = None
        self.username = ""
        self.initialize()

    def pack(self):
        """Display the view center"""
        self._frame.place(relx=0.5, rely=0.5, anchor="center")

    def destroy(self):
        """Destroy the curren UI window"""
        self._frame.destroy()

    def save_username(self):
        """Save username and then show start button"""
        username = self.username_box.get()

        if not username.strip():
            self.message.config(
                text="Anna nimimerkki"
            )

            return
        self.username = username
        self.message.config(
            text=f"Tervetuloa pelaamaan {username}!"
        )
        self.start_button.grid(row=6, column=0, pady=10)

    def start_game(self):
        """Start game when gets username"""
        self.handle_start(self.username)

    def initialize(self):
        """Create menu labels, buttons and gamerules"""
        self._frame = ttk.Frame(master=self.root)

        title = ttk.Label(
            master=self._frame,
            text="Visailupeli",
            anchor="center"
        )
        rules = ttk.Label(
            master=self._frame,
            text=("Säännöt:\n"
            "- Sinulle esitetään kysymys ja siihen 10 vastausvaihtoehtoa.\n"
            "- Raksi ruudut mitkä uskot oikeiksi.\n"
            "- Kun olet valinnut halutut vastaukset paina 'tarkista.'\n"
            "- Jos vastaus oli väärin tai et vastaa mitään, peli päättyy. Voit valita\n"
            " haluatko aloittaa uuden pelin vai mennä etusivulle.\n"
            "- Jos vastasit oikein, näkyviisi tulee nappi millä pääset seuraavaan kysymykseen.\n"

        ),
            anchor="center"
        )
        username = ttk.Label(
            master=self._frame,
            text="Nimimerkki:"
        )
        self.username_box = ttk.Entry(
            master=self._frame,
        )
        username_save_button = ttk.Button(
            master=self._frame,
            text="Tallenna",
            command=self.save_username
        )
        self.start_button = ttk.Button(
            master=self._frame,
            text="Aloita Peli",
            command=self.start_game
        )
        self.message = ttk.Label(
            master=self._frame,
            text = ""
        )

        title.grid(row=0, column=0, pady=10)
        rules.grid(row=1, column=0, pady=10)
        username.grid(row=2, column=0, pady=10)
        self.username_box.grid(row=3, column=0, pady=10)
        username_save_button.grid(row=4, column=0, pady=10)
        self.message.grid(row=5, column=0, pady=10)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
