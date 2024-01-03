class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1
# jai mis une representation graphique pour mieux visiualiser les deplacement (le O est le personnage et les . represente le plateau)
    def afficher(self, taille_plateau):
        for i in range(taille_plateau):
            for j in range(taille_plateau):
                if i == self.y and j == self.x:
                    print("O", end=" ")
                else:
                    print(".", end=" ") 
            print()


taille_plateau = 3
personnage = Personnage(1, 1)

# A chaque fois il garde la position precedente

print("Position initiale","(", personnage.x, ";", personnage.y, ")", ":")
personnage.afficher(taille_plateau)

personnage.droite()
print("\nDéplacement vers la droite :")
personnage.afficher(taille_plateau)

personnage.haut()
print("\nDéplacement vers le haut :")
personnage.afficher(taille_plateau)

personnage.bas()
print("\nDéplacement vers le bas :")
personnage.afficher(taille_plateau)

personnage.gauche()
print("\nDéplacement vers la gauche :")
personnage.afficher(taille_plateau)
