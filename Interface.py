import pygame
from game import Game
from Chrono import Minuteur
from Score import Score
from bot import Fantome
import math
pygame.init()
pygame.joystick.init()

WINDOW_SIZE = pygame.display.get_desktop_sizes()[0]
WINDOW_FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.NOFRAME  # | pygame.RESIZABLE


if pygame.joystick.get_count() != 0:
    controller = True
    joysticks = pygame.joystick.Joystick(0)
    joysticks.init()
    print(f"Joystick detected: {joysticks.get_name()}")
else:
    controller = False

window = pygame.display.set_mode(WINDOW_SIZE, WINDOW_FLAGS)

pygame.display.set_caption("TrailBlazer")
police = pygame.font.Font(None, 36)

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

fantome = Fantome()

chrono = Minuteur()
score = Score()
kevents = {
    "up": [pygame.K_UP, pygame.K_z],
    "down": [pygame.K_DOWN, pygame.K_s],
    "left": [pygame.K_LEFT, pygame.K_q],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "handbrake": [pygame.K_SPACE],
    "gearup": [pygame.K_e],
    "geardown": [pygame.K_a],
    "leave": [pygame.K_ESCAPE]
}

chrono.run()

clock = pygame.time.Clock()
joystick_axis_0 = 0
joystick_axis_4 = 0
joystick_axis_5 = 0
X_button = False
running = True

# Couleurs
CENTER = (75, 75)
RADIUS = 75
BLACK = (0, 0, 0)
RED = (200, 0, 0)


def draw_needle(angle):
    pygame.draw.circle(window, BLACK, CENTER, RADIUS, 3, True, True)
    pygame.draw.line(window, BLACK, (0, 75), (150, 75), 3)

    angle_rad = math.radians(((angle+1)*4-90))
    needle_length = RADIUS - 10
    needle_x = CENTER[0] + needle_length * math.cos(angle_rad - math.pi / 2)
    needle_y = CENTER[1] + needle_length * math.sin(angle_rad - math.pi / 2)

    pygame.draw.line(window, RED, CENTER, (needle_x, needle_y), 4)
    pygame.draw.circle(window, BLACK, CENTER, 5)

    pygame.display.flip()


def paused(pause):
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    return True
                elif event.key == pygame.K_ESCAPE:
                    pause = False
                    return False
        pygame.display.update()
        clock.tick(15)


car.player.positionBot = car.player.position
while running:
    if fantome.Play == False:
        keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            car.pressed[event.key] = True
            if event.key == pygame.K_p:
                running = paused(True)
            if event.key == pygame.K_b:
                fantome.Play = True
                car.player.speed = 0
                car.player.position = car.player.positionBot
                car.player.heading = 0
                car.player.turn(-80, True)
                print(fantome.lst)
        elif event.type == pygame.KEYUP:
            car.pressed[event.key] = False

        if controller != False:
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    joystick_axis_0 = event.value
                if event.axis == 4:
                    joystick_axis_4 = event.value
                if event.axis == 5:
                    joystick_axis_5 = event.value

    if abs(joystick_axis_0) > 0.1:
        car.player.turn(1.8 * joystick_axis_0)

    if abs(joystick_axis_4) > 0.1:
        car.player.accelerate(-0.1 * (joystick_axis_4+1)/1.5)

    if abs(joystick_axis_5) > 0.1:
        car.player.accelerate(0.1 * (joystick_axis_5+1)/1.5)

    if controller != False:
        if joysticks.get_button(2):
            X_button = True
        else:
            X_button = False
    if fantome.Play == False:
        keypresses = [k for k, v in car.pressed.items() if v == True]

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

        if key in kevents["handbrake"] or X_button == True:
            if car.player.speed < 0:
                car.player.brake(-0.5)
            else:
                car.player.brake(0.5)

        if key in kevents["left"]:
            car.player.turn(-1.8)
        if key in kevents["right"]:
            car.player.turn(1.8)

    speed = police.render(
        (f"Speed :{abs(round(car.player.speed, 1))}"), True, (255, 255, 255))

    chrono.affichage()
    minuteur = police.render(
        (f"{chrono}"), True, (255, 255, 255))

    score.calculscore(car.player.speed, chrono.timer)
    scr = police.render(
        (f"{score}"), True, (255, 255, 255))

    car_sprites.update()
    window.blit(background, (-car.player.position.x, - car.player.position.y))
    window.blit(speed, (25, 100))
    window.blit(minuteur, ((WINDOW_SIZE[0]//2)-75, 10))
    window.blit(scr, (25, 150))
    car_sprites.draw(window)
    clock.tick_busy_loop(60)

    if fantome.Play == False:
        fantome.add_movement(keypresses)
        car.player.positionBot = (16655, 9108)
    else:
        keypresses = fantome.playing()

    draw_needle(abs(car.player.speed))

    if controller == True:
        joysticks.rumble(abs(car.player.speed/car.player.maxspeedfront*0.1),
                         abs(car.player.speed/car.player.maxspeedfront*0.1), 1)
