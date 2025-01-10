import pygame
from test import car
pygame.init()
pygame.joystick.init()


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

if pygame.joystick.get_count() != 0:
    controller = True
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print(f"Joystick detected: {gamepad.get_name()}")
else:
    controller = False

joystick_axis_0 = 0
joystick_axis_4 = 0
joystick_axis_5 = 0
X_button = False


if abs(joystick_axis_0) > 0.1:
    car.player.turn(1.8 * joystick_axis_0)

if abs(joystick_axis_4) > 0.1:
    car.player.accelerate(-0.1 * (joystick_axis_4+1)/1.5)

if abs(joystick_axis_5) > 0.1:
    car.player.accelerate(0.1 * (joystick_axis_5+1)/1.5)

if controller != False:
    if gamepad.get_button(2):
        if car.player.speed < 0:
            car.player.brake(-0.5)
        else:
            car.player.brake(0.5)
