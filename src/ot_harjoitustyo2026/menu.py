import pygame
import sys


class Menu:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((640, 480))
        font = pygame.font.SysFont("Arial", 30, bold=True)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "game"
                
            screen.fill((255, 255, 255))
            text = font.render("Tähän tulee peli :)", True, (0,0,0))
            screen.blit(text,(100,50))
            start = font.render("Aloita peli", True, (0,0,0))
            screen.blit(start, (100,100))
            pygame.display.flip()
            
        