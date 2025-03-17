from PIL import Image
larg=512*4
hauteur=512*4

class fusion(object):
    def __init__(self):
        self.new_img = Image.new("RGBA", (larg, hauteur))
        self.totallarg = 0
        self.totalhauteur = 0

    def putpixel(self, base_img,deg=0):
        base_img = Image.open(f"img\{base_img}")
        base_img=base_img.rotate(deg)
        largeur, hauteur = base_img.size
        if self.totallarg+largeur > larg:
            self.totalhauteur+=512
            self.totallarg=0
        for x in range(largeur):
            xput = self.totallarg+x
            for y in range(hauteur):
                yput=y+self.totalhauteur
                temp = base_img.getpixel((x, y))
                self.new_img.putpixel((xput, yput), temp)
        self.totallarg += largeur


