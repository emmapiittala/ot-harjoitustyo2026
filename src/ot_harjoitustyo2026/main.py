import pygame
import sys
from ot_harjoitustyo2026.menu import Menu
from ot_harjoitustyo2026.login import Login
from ot_harjoitustyo2026.register import Register
from ot_harjoitustyo2026.game import Game
from ot_harjoitustyo2026.gameover import Gameover

def main():

    state = "menu"
    while True:
        if state == "menu":
            state = Menu().run()
        elif state == "login":
            state = Login().run()
        elif state == "register":
            state = Register().run()
        elif state == "game":
            state = Game().run()
        elif state == "gameover":
            state = Gameover().run()
            
            


if __name__ == "__main__":
    main()