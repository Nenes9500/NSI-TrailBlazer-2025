import pygame
# from player import Player
pygame.init()
screen = pygame.display.set_mode((612, 292), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
while running:
    screen.fill("#4a724b")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.flip()
