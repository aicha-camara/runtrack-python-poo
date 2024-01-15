class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def affichage(self):
        print("La longueur :", self.__longueur, "La largeur :", self.__largeur)

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

le_rectangle = Rectangle(10, 5)
le_rectangle.set_longueur(20)
le_rectangle.set_largeur(50)
le_rectangle.affichage()
