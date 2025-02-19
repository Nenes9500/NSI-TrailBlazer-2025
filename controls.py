import pygame
from Player import Game


pygame.init()
pygame.joystick.init()


class Controls:
    def __init__(self, car) -> None:
        self.car = car
        self.pressed = {}
        self.kevents = {
            "up": [pygame.K_UP, pygame.K_z, "gamepad_axis_4"],
            "down": [pygame.K_DOWN, pygame.K_s, "gamepad_axis_5"],
            "left": [pygame.K_LEFT, pygame.K_q, "gamepad_axis_0"],
            "right": [pygame.K_RIGHT, pygame.K_d, "gamepad_axis_0"],
            "handbrake": [pygame.K_SPACE, pygame.CONTROLLER_BUTTON_X],
            "gearup": [pygame.K_e],
            "geardown": [pygame.K_a],
            "leave": [pygame.K_ESCAPE]
        }
        if pygame.joystick.get_count() != 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
            print(f"Joystick detected: {self.gamepad.get_name()}")

    def updateControls(self):
        keypresses = [k for k, v in self.pressed.items() if abs(v) >= 0.1]
        accel = False

        for key in keypresses:
            if key in self.kevents["leave"]:
                running = False
            elif key in self.kevents["down"]:
                self.car.player.accelerate(-0.1*self.pressed[key])
                accel = True
            if key in self.kevents["up"]:
                self.car.player.accelerate(0.1*self.pressed[key])
                accel = True
            elif key in self.kevents["handbrake"]:
                if self.car.player.speed < 0:
                    self.car.player.brake(-0.5)
                else:
                    self.car.player.brake(0.5)
                accel = True
            elif key in self.kevents["left"]:
                if key == "gamepad_axis_0":
                    if self.pressed[key] < 0:
                        self.car.player.turn(1.8*self.pressed[key])
                else:
                    self.car.player.turn(-1.8*self.pressed[key])
            elif key in self.kevents["right"]:
                if key == "gamepad_axis_0":
                    if self.pressed[key] > 0:
                        self.car.player.turn(1.8*self.pressed[key])
                else:
                    self.car.player.turn(1.8*self.pressed[key])
        if not accel:
            if self.car.player.speed > 0:
                self.car.player.brake(0.05)
            elif self.car.player.speed < 0:
                self.car.player.brake(-0.05)
