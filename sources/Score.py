import math


class Score(object):
    """This class is used to calculate the score."""

    def __init__(self):
        self.score = 0

    def calculscore(self, speed, time):
        """This method calculates the score based on time and speed."""
        self.score = (self.score+time*abs(speed/100))

    def __str__(self):
        return f"Score : {math.trunc(self.score)}"
