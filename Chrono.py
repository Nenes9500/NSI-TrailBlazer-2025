import time
import math


class Minuteur(object):
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.chrono = [0, 0, 0, 0]
        self.timer = None

    def run(self):
        self.start_time = time.time()

    def affichage(self):
        self.timer = (time.time() - self.start_time)
        seconds = math.trunc(self.timer)
        msec = str(round(self.timer-seconds, 3))
        self.chrono[3] = msec[2:]
        self.chrono[2] = int(self.timer % 60)
        self.chrono[1] = int(self.timer//60)
        self.chrono[0] = int(self.chrono[1]//24)

    def __str__(self):
        return f"Time:{self.chrono[0]}:{self.chrono[1]}:{self.chrono[2]}:{self.chrono[3]}"
