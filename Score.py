import math


class Score(object):
    def __init__(self):
        self.score = 0

    def calculscore(self, speed, time):
        self.score = (self.score+time*(speed/100))

    def __str__(self):
        return f"Score : {math.trunc(self.score)}"
