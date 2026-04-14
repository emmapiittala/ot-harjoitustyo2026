from tkinter import Tk
from ot_harjoitustyo2026.ui import UI
from ot_harjoitustyo2026.menu import Menu
from ot_harjoitustyo2026.game import Game


def main():
    window = Tk()
    window.title("Visailupeli")
    window.geometry("800x800")
    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
