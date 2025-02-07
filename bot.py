import pygame

class Fantome(object):
    def __init__(self):
        self.lst = []
        self.i=0
        self.Play= False

    def add_movement(self,liste):
        self.lst.append(liste)

    def playing(self):
        self.i+=1
        if len(self.lst)>self.i:
            self.Play= True
            return self.lst[self.i]
        else :
            self.lst = []
            self.Play=False