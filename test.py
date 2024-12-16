from pygame import *
import pygame
from game import Game

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 127, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
pink = (255, 0, 255)


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_SURFACE = pygame.HWSURFACE | pygame.NOFRAME | pygame.RESIZABLE


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("TrailBlazer")

background = pygame.image.load('img/racetrack.png')
background_size = background.get_size()
background = pygame.transform.scale(
    background, (background_size[0]*1.5, background_size[1]*1.5))
car_img = pygame.image.load('img/voiture.png').convert_alpha()
car_img_size = car_img.get_size()
car_img = pygame.transform.scale(
    car_img, (car_img_size[0]//4, car_img_size[1]//4))


car = Game(car_img, WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
car_sprites = pygame.sprite.Group()
car_sprites.add(car.player)

kevents = {
    "forward": [pygame.K_UP, pygame.K_z],
    "backward": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_q],
    "right": [pygame.K_RIGHT, pygame.K_d]
}


clock = pygame.time.Clock()
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        elif event.type == pygame.KEYDOWN:
            car.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            car.pressed[event.key] = False

    if car.pressed.get(pygame.K_DOWN):
        car.player.brake(0.1)
    else:
        car.player.brake(-0.075)
    if car.pressed.get(pygame.K_UP):
        car.player.accelerate(0.1)
    else:
        car.player.accelerate(-0.075)
    if car.pressed.get(pygame.K_LEFT):
        car.player.turn(-1.8)
    if car.pressed.get(pygame.K_RIGHT):
        car.player.turn(1.8)

    car_sprites.update()

    window.blit(background, (-car.player.position.x, - car.player.position.y))
    car_sprites.draw(window)
    pygame.display.flip()

    clock.tick_busy_loop(60)

pygame.quit()
