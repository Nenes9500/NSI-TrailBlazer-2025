import pygame
from Player import Game
from controls import *

pygame.init()
pygame.joystick.init()

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME  # | pygame.RESIZABLE


window = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)

pygame.display.set_caption("TrailBlazer")


background = pygame.image.load('img/racetrack.png')
background_size = background.get_size()
background = pygame.transform.scale(
    background, (background_size[0]*1.5, background_size[1]*1.5))
car_img = pygame.image.load('img/voiture.png').convert_alpha()
car_img_size = car_img.get_size()
car_img = pygame.transform.scale(
    car_img, (car_img_size[0]//4, car_img_size[1]//4))


car = Game(car_img, WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
car_sprites = pygame.sprite.Group()
car_sprites.add(car.player)
car.player.position = (16655, 9108)
car.player.turn(-80, True)


clock = pygame.time.Clock()

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            car.pressed[event.key] = 1
        elif event.type == pygame.KEYUP:
            car.pressed[event.key] = 0
        elif event.type == pygame.JOYAXISMOTION:
            car.pressed[event.axis] = event.value

    keypresses = [k for k, v in car.pressed.items() if v != 0]

    if (not any(key in kevents["up"] for key in keypresses) or joystick_axis_5 != 0) and (not any(key in kevents["down"] for key in keypresses) or joystick_axis_5 != 0):
        if car.player.speed > 0:
            car.player.brake(0.05)
        elif car.player.speed < 0:
            car.player.brake(-0.05)

    for key in keypresses:
        if key in kevents["leave"]:
            running = False

        if key in kevents["down"]:
            car.player.accelerate(-0.1)

        if key in kevents["up"]:
            car.player.accelerate(0.1)

        if key in kevents["handbrake"]:

            if car.player.speed < 0:
                car.player.brake(-0.5)
            else:
                car.player.brake(0.5)

        if key in kevents["left"]:

            car.player.turn(-1.8)
        if key in kevents["right"]:
            car.player.turn(1.8)

    car_sprites.update()
    window.blit(background, (-car.player.position.x, - car.player.position.y))
    car_sprites.draw(window)
    pygame.display.flip()

    clock.tick_busy_loop(60)
