from PIL import Image
import os

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
        self.posd=0
        self.posa=0

    def putpixel(self, base_img, n,deg=0):
        """This method is used to place individual tiles in the large image."""
        base_img = Image.open(f"img/img512/{base_img}.png").rotate(deg)
        largeur, hauteur = base_img.size
        if self.current_x >= self.larg:
            self.current_x = 0
            self.current_y += self.tile_height 

        for x in range(largeur):
            for y in range(hauteur):
                pixel = base_img.getpixel((x, y))
                if pixel==(237,28,36,255):
                    self.posa=x,y
                if pixel==(0,162,232,255):
                    self.posd=512*n[1],512*n[0]
                self.new_img.putpixel((self.current_x + x, self.current_y + y), pixel)
        self.current_x += self.tile_width

    def saver(self,text):
        """This method is used to save the large image."""
        print(self.posd)
        print(self.posa)
        newpath = f'Map/{text}/{text}' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        self.new_img.save(f"Map/{text}/{text}.png")
        file = open(f'Map/{text}/{text}.txt', 'x')
        file.write(f"{self.posd[0]}\n")
        file.write(f"{self.posd[1]}\n")
        file.close()
