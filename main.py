import pygame
import pygame
from game import Game
# from manette import *

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_SURFACE = pygame.HWSURFACE | pygame.NOFRAME | pygame.RESIZABLE


pygame.init()
pygame.joystick.init()

joysticks = pygame.joystick.Joystick(0)
joysticks.init()
print(f"Joystick detected: {joysticks.get_name()}")

window = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE, vsync=1)
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


clock = pygame.time.Clock()
done = False
last_command = None
while not done:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        elif event.type == pygame.KEYDOWN:
            car.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            car.pressed[event.key] = False
        if event.type == pygame.JOYAXISMOTION:
           if event.axis == 0 and (event.value >0.1 or event.value <-0.1):
                car.player.turn(1.8)

    if car.pressed.get(pygame.K_DOWN) or joysticks.get_button(4):
        car.player.accelerate(-0.1)
    else:
        if car.player.speed < 0:
            car.player.brake(-0.1)
    if car.pressed.get(pygame.K_UP) or joysticks.get_button(5):
        car.player.accelerate(0.1)
    else:
        if car.player.speed > 0:
            car.player.brake(0.1)
    if car.pressed.get(pygame.K_SPACE) or joysticks.get_button(2):
        if car.player.speed < 0:
            car.player.brake(-0.5)
        if car.player.speed > 0:
            car.player.brake(0.5)

    if car.pressed.get(pygame.K_LEFT) or joysticks.get_button(13):
        car.player.turn(-1.8)
    if car.pressed.get(pygame.K_RIGHT) or joysticks.get_button(14):
        car.player.turn(1.8)


    car_sprites.update()
    window.blit(background, (-car.player.position.x, - car.player.position.y))
    car_sprites.draw(window)
    pygame.display.flip()

    clock.tick_busy_loop(60)
