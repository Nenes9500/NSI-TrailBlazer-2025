import pygame
from game import Game

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE


pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("Car Steering")


road_image = road_image = pygame.image.load('img/road_texture.png')
background = pygame.transform.smoothscale(
    road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
car_img = pygame.image.load('img/voiture.png').convert_alpha()


car = Game(car_img, WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
car_sprites = pygame.sprite.Group()
car_sprites.add(car.player)


clock = pygame.time.Clock()
done = False
last_command = None
while not done:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        elif (event.type == pygame.VIDEORESIZE):
            WINDOW_WIDTH = event.w
            WINDOW_HEIGHT = event.h
            window = pygame.display.set_mode(
                (WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
            background = pygame.transform.smoothscale(
                road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
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

    window.blit(background, (0, 0))
    car_sprites.draw(window)
    pygame.display.flip()

    clock.tick_busy_loop(60)

pygame.quit()
