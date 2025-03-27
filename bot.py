import pygame
import os


class Fantome(object):
    def __init__(self):
        self.lst = []
        self.i = 0
        self.Play = False

    def add_movement(self, liste):
        self.lst.append(liste)

    def playing(self):
        self.i += 1
        if len(self.lst) > self.i:
            self.Play = True
            return self.lst[self.i]
        else:
            self.lst = []
            self.i = 0
            self.Play = False

    def lecture(self, fichier):
        lst = []
        file = open(fichier, "r")
        enregistrements = file.readlines()
        for i in range(len(enregistrements)):
            enregistrement = enregistrements[i].rstrip("\n").split(",")
            temp = int(enregistrement[0])
            lst.append([temp])
        return lst

    def save(self, command, name,Map):
        newpath = f'Map/{Map}/replay' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        if self.verif_exits_file(f"Map/{Map}/replay/{name}.txt") == False:
            file = open(f'Map/{Map}/replay/{name}.txt', 'x')
            for c in command:
                for i in c:
                    file.write(f"{i}\n")
            file.close()

    def verif_exits_file(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
            return False
