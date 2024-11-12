from pygame import *


class Track:
    def __init__(self, id, startPoint: Vector3, endPoint: Vector3) -> None:
        self.id = id
        self.startPoint = startPoint
        self.endPoint = endPoint
