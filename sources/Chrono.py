import time
import math


class Minuteur(object):
    """
    This class is used to create a timer.
    """

    def __init__(self):
        self.start_time = None
        self.chrono = [0, 0, 0, 0]
        self.timer = None
        self.savetime = 0
        self.timere=True

    def run(self):
        """
        This method is used to start the timer.
        """
        self.start_time = time.time()

    def affichage(self):
        """
        This method is used to display the timer.
        """
        self.timer = (time.time()) - self.start_time
        seconds = math.trunc(self.timer)
        msec = str(round(self.timer-seconds, 3))
        self.chrono[3] = msec[2:]
        self.chrono[2] = int(self.timer % 60)
        self.chrono[1] = int(self.timer//60)
        self.chrono[0] = int(self.chrono[1]//24)

    def pauser(self):
        """
        This method is used to pause the timer.
        """
        self.savetime = self.timer

    def __str__(self):
        """
        This method is used to display the timer.
        """
        return f"Time:{self.chrono[0]}:{self.chrono[1]}:{self.chrono[2]}:{self.chrono[3]}"
