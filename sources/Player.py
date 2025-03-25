import pygame
import math


class CarSprite(pygame.sprite.Sprite):
    """This class represents the car sprite."""

    def __init__(self, car_image, x, y, rotations=360):
        pygame.sprite.Sprite.__init__(self)
        self.rot_img = []
        self.min_angle = (360 / rotations)
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(
                car_image, 360-90-(i*self.min_angle), 1)
            self.rot_img.append(rotated_image)
        self.min_angle = math.radians(self.min_angle)
        self.image = self.rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.heading = 0
        self.speed = 0
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(x, y)
        self.positionBot = pygame.math.Vector2(x, y)
        self.maxspeedfront = 29.9
        self.maxspeedback = -6.9

    def turn(self, angle_degrees, force=False):
        """This method is used to turn the car.
        Setting force to True allows the car to turn even if it is not moving.
        """
        if self.speed != 0 or force:
            self.heading += math.radians(angle_degrees)
            image_index = int(
                self.heading / self.min_angle) % len(self.rot_img)
            if (self.image != self.rot_img[image_index]):
                x, y = self.rect.center
                self.image = self.rot_img[image_index]
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)

    def accelerate(self, amount):
        """This method is used to accelerate the car."""
        if self.maxspeedfront >= self.speed and self.maxspeedback <= self.speed:
            self.speed = round(self.speed+amount, 2)

    def brake(self, amount):
        """This method is used to brake the car."""
        if self.speed < 0:
            self.speed = round(self.speed-amount, 2)
        elif self.speed > 0:
            self.speed = round(self.speed-amount, 2)

    def update(self):
        """This method is called every frame to calculate a velocity vector."""
        self.velocity.from_polar((self.speed, math.degrees(self.heading)))
        self.position += self.velocity


class Game(CarSprite):
    """This class links the car sprite to the game."""

    def __init__(self, car_image, x, y, rotations=360):
        self.player = CarSprite(car_image, x, y, rotations)
