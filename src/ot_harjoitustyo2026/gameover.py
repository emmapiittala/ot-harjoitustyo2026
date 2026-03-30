import pygame

class Gameover:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((640, 480))
        font = pygame.font.SysFont("Arial", 30, bold=True)

        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
            
            screen.fill((0, 0, 0))
            text = font.render("Tässä häviät pelin", True, (255,255,255))
            screen.blit(text,(100,50))
            pygame.display.flip()