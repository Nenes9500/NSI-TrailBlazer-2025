import pygame
import math


class CarSprite(pygame.sprite.Sprite):

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
        self.maxspeedfront = 29.9
        self.maxspeedback = -6.9

    def turn(self, angle_degrees, force=False):
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
        if self.maxspeedfront >= self.speed and self.maxspeedback <= self.speed:
            self.speed = round(self.speed+amount, 2)

    def brake(self, amount):
        if self.speed < 0 and amount < 0:
            self.speed = round(self.speed-amount, 2)
        elif self.speed > 0 and amount > 0:
            self.speed = round(self.speed-amount, 2)

    def update(self):
        self.velocity.from_polar((self.speed, math.degrees(self.heading)))
        self.position += self.velocity
