import pygame

class Game:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((640, 480))
        font = pygame.font.SysFont("Arial", 30, bold=True)

        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
            
            screen.fill((0, 0, 0))
            text = font.render("Kysymykset", True, (255,255,255))
            screen.blit(text,(100,50))
            pygame.display.flip()