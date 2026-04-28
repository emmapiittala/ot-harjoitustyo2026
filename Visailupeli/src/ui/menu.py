"""Main menu view"""
from tkinter import ttk

class Menu:
    """Show the main menu and game rules
    Attributes:
    _root: Application window.
    _handle_start: Callbaxk to start the game.
    _frame: Main frame for the view."""
    def __init__(self, root, handle_start):
        """Intialize the menu view."""
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        """Display the view center"""
        self._frame.place(relx=0.5, rely=0.5, anchor="center")

    def destroy(self):
        """Destroy the curren UI window"""
        self._frame.destroy()

    def _initialize(self):
        """Create UI and make labels, buttons and gamerules"""
        self._frame = ttk.Frame(master=self._root)

        title = ttk.Label(
            master=self._frame,
            text="Visailupeli",
            anchor="center"
        )
        rules = ttk.Label(
            master=self._frame,
            text=("Säännöt:\n"
            "- Tässä pelissä on tällä hetkellä 3 kysymystä.\n"
            "- Raksi ruudut mitkä koet oikeiksi vastauksiksi.\n"
            "- Kun olet valinnut halutut vastaukset paina tarkista.\n"
            "- Jos vastaus oli väärin, peli päättyy. Voit valita\n"
            " haluatko aloittaa uuden pelin vai mennä etusivulle.\n"
            "- Painamalla tarkista- näppäintä ilman yhtään klikattua vastausta, häviät pelin.\n"
            "- Jos vastasit oikein, näkyviisi tulee nappi millä pääset seuraavaan kysymykseen.\n"

        ),
            anchor="center"
        )
        start_button = ttk.Button(
            master=self._frame,
            text="Aloita Peli",
            command=self._handle_start
        )

        title.grid(row=0, column=0, pady=10)
        rules.grid(row=1, column=0, pady=10)
        start_button.grid(row=2, column=0, pady=10)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
