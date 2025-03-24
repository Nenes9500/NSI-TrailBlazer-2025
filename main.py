import pygame
from pygame.locals import *
from game import Game
pygame.init()
WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
fenetre = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))


fond = pygame.image.load("img/fond_menu.png")

police = pygame.font.Font(None, 72)
game_start = True
while game_start:
    Titre = police.render("TrailBlazer", True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            game_start = False
            pygame.quit()
    fenetre.blit(Titre, (150, 150))
    fenetre.blit(fond, (0, 0))
    pygame.display.flip()
    pygame.display.update()