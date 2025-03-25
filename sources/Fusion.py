from PIL import Image


class fusion(object):
    """This class is used to merge all the images into one."""

    def __init__(self, larg, hauteur):
        self.larg = larg
        self.hauteur = hauteur
        self.new_img = Image.new("RGBA", (larg, hauteur))
        self.current_x = 0
        self.current_y = 0
        self.tile_width = 512
        self.tile_height = 512

    def putpixel(self, base_img, deg=0):
        """This method is used to place individual tiles in the large image."""
        base_img = Image.open(f"img/img512/{base_img}.png").rotate(deg)
        largeur, hauteur = base_img.size

        # Vérifier si on doit passer à la ligne suivante
        if self.current_x >= self.larg:
            self.current_x = 0
            self.current_y += self.tile_height  # Descend d'une ligne

        # Placer les pixels dans la grande image
        for x in range(largeur):
            for y in range(hauteur):
                pixel = base_img.getpixel((x, y))
                self.new_img.putpixel(
                    (self.current_x + x, self.current_y + y), pixel)

        # Avancer la position X pour la prochaine image
        self.current_x += self.tile_width

    def saver(self):
        """This method is used to save the large image."""
        self.new_img.save("img/new_race.png")
