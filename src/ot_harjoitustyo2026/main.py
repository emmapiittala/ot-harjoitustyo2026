from tkinter import Tk
from ot_harjoitustyo2026.ui.ui import UI

def main():
    window = Tk()
    window.title("Visailupeli")
    window.geometry("800x400")
    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
