from PIL import Image


class fusion(object):
    def __init__(self):
        self.new_img = Image.new("RGBA", (10000, 100000))
        self.totallarg = 0
        self.totalhauteur = 0

    def putpixel(self, base_img):
        base_img = Image.open(f"img\{base_img}")
        largeur, hauteur = base_img.size
        for x in range(largeur):
            xput = self.totallarg+x
            for y in range(hauteur):
                temp = base_img.getpixel((x, y))
                self.new_img.putpixel((xput, y), temp)
        self.totalhauteur += hauteur
        self.totallarg += largeur


a = fusion()
a.putpixel("9780.png")
a.new_img.show()
