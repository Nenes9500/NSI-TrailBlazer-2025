import pygame
import os


class Fantome(object):
    """
    This class is used to create a ghost that will replay the movements of the player.
    """

    def __init__(self):
        self.lst = []
        self.i = 0
        self.Play = False

    def add_movement(self, liste):
        """
        This method is used to add a movement to the list of movements.
        """
        self.lst.append(liste)

    def playing(self):
        """
        This method is used to play the movements of the ghost.
        """
        self.i += 1
        if len(self.lst) > self.i:
            self.Play = True
            return self.lst[self.i]
        else:
            self.lst = []
            self.i = 0
            self.Play = False

    def lecture(self, fichier):
        """
        This method is used to read the movements of the ghost from a file."""
        lst = []
        file = open(fichier, "r")
        enregistrements = file.readlines()
        for i in range(len(enregistrements)):
            enregistrement = enregistrements[i].rstrip("\n").split(",")
            temp = int(enregistrement[0])
            lst.append([temp])
        return lst

    def save(self, command, name,Map):
        """
        This method is used to save the movements of the ghost in a file.
        """
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
        """
        This method is used to check if a file exists.
        """
        if os.path.exists(file_path):
            return True
        else:
            return False
