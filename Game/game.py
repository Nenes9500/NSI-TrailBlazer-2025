import pygame
from Player import CarSprite


class Game(CarSprite):
    def __init__(self, car_image, x, y, rotations=360):
        self.player = CarSprite(car_image, x, y, rotations=360)
        self.pressed = {}
