from pygame import math, sprite, image, draw, Rect, transform


class Car(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 0
        self.direction = 0
        self.image = image.load("car_sprite.png")
        self.rect = self.image.get_rect()

    def accelerate(self, value):
        self.speed += value

    def turn(self, angle):
        self.direction += angle

    def update(self):
        sprite.Sprite.update(self)
        self.velocity = math.Vector2(0, self.speed)
        self.current_velocity = self.velocity.rotate(self.direction)
