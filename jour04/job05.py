import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur*self.hauteur    

class Cercle(Forme):
    def __init__(self , radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2

rectangle = Rectangle(10, 20)
cercle = Cercle(10)

# Test des différentes surcharges de la méthode aire
print(f"L'aire du rectangle = {rectangle.aire()}")
print(f"L'aire du cercle = {cercle.aire()}")
