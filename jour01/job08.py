import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print("Rayon du cercle :", self.rayon)
        print("Circonférence : {:.2f}".format(self.circonférence()))
        print("Diamètre : {:.2f}".format(self.diametre()))
        print("Aire : {:.2f}".format(self.aire()))

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Création des cercles avec les rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
print("Cercle 1 :")
cercle1.afficherInfos()
print("\nCercle 2 :")
cercle2.afficherInfos()
