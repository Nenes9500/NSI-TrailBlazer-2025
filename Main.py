import pygame
pygame.init()

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
running=True
WHITE= (255,255,255)
background = pygame.image.load('img/fond menu.png')
while running:
    Play_button = pygame.Rect(WINDOW_SIZE[0]//2-100, WINDOW_SIZE[1]//2, 200, 50)
    pygame.draw.rect(screen, WHITE, Play_button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    screen.blit(background, (0, 0))
pygame.quit()