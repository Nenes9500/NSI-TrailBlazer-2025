import pygame
from Player import Game
from controls import Controls

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

controls = Controls(car)

running = True
while running:  # TODO: ceiling of 1 on analog accel
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            controls.pressed[event.key] = 1
        elif event.type == pygame.JOYBUTTONDOWN:
            controls.pressed[event.button] = 1
        elif event.type == pygame.KEYUP:
            controls.pressed[event.key] = 0
        elif event.type == pygame.JOYBUTTONUP:
            controls.pressed[event.button] = 0
        elif event.type == pygame.JOYAXISMOTION:
            controls.pressed["gamepad_axis_" + str(event.axis)] = event.value
    controls.updateControls()

    car_sprites.update()
    window.blit(background, (-car.player.position.x, - car.player.position.y))
    car_sprites.draw(window)
    pygame.display.flip()

    clock.tick_busy_loop(60)
