"""Start the application"""
from tkinter import Tk
from ui.ui import UI


def main():
    """"Create main window"""
    window = Tk()
    window.title("Visailupeli")
    window.geometry("800x400")
    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()

