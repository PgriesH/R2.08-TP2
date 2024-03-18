class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self._width

    def set_width(self, newwidth):
        if newwidth > 0:
            self._width = newwidth
        else:
            print("La largeur ne peut pas être négative.")

    width = property(fget=get_width, fset=set_width)

    def get_height(self):
        return self._height

    def set_height(self, newheight):
        if newheight > 0:
            self._height = newheight
        else:
            print("La hauteur ne peut pas être négative")

    height = property(fget=get_height, fset=set_height)

    def get_area(self):
        surface = self.height * self.width
        return surface

    def get_diagonale(self):
        diagonale = ((self.width ** 2 + self.height ** 2) **.5)
        return diagonale

    def get_perimeter(self):
        perimetre = 2 * (self.width + self.height)
        return perimetre

    def get_picture(self):
        error = "Trop grand pour faire une image."
        if self.width > 50 or self.height > 50:
            return error
        else:
            largeur = ""
            for loop in range(self.height):
                largeur = largeur + "\n" + "*" * self.width
            return largeur

    def get_amount_inside(self, formetrans):
        fhauteur = self.height // formetrans.height
        flargeur = self.width // formetrans.width
        calcul = fhauteur * flargeur
        return calcul

    def __str__(self):
        return f"Rectangle (width = {self.width}, height = {self.height})"


class Carree(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)

    def get_side(self):
        return self.width

    def set_side(self, newcote):
        self.width = newcote
        self.height = newcote

    side = property(fget=get_side, fset=set_side)

    def set_height(self, newheight):
        self.height = newheight
        self.width = newheight

    def set_width(self, newwidth):
        self.width = newwidth
        self.height = newwidth

    def __str__(self):
        return f"Carree(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.height=3
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())
    print("--------------------------------")
    sq = Carree(9)
    print(sq.get_area())
    sq.side = 4
    print(sq.get_diagonale())
    print(sq)
    print(sq.get_picture())
    rect.height=8
    rect.width=16
    print(repr(rect.get_amount_inside(sq)))
