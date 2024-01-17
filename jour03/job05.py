import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        if random.random() < 0.5:  
            adversaire.vie -= 1
            print(f"{self.nom} a réussi son attaque!")
        else:
            print(f"{self.nom} a raté son attaque!")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1/2/3) : "))

    def lancerJeu(self):
        self.choisirNiveau()  # Appel de la méthode pour choisir le niveau

        if self.niveau == 1:
            joueur = Personnage("Hero", 10)
            ennemi = Personnage("Adversaire", 5)
        elif self.niveau == 2:
            joueur = Personnage("Hero", 10)
            ennemi = Personnage("Adversaire", 10)
        elif self.niveau == 3:
            joueur = Personnage("Hero", 10)
            ennemi = Personnage("Adversaire", 20)
        else:
            print("Niveau invalide. Choisissez entre 1, 2 et 3.")
            return

        while joueur.vie > 0 and ennemi.vie > 0:
            print(f"\n{joueur.nom} attaque {ennemi.nom}!")
            joueur.attaquer(ennemi)
            print(f"{ennemi.nom} a maintenant {ennemi.vie} points de vie.")

            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu ! Vous avez gagné !")
                break

            print(f"\n{ennemi.nom} contre-attaque {joueur.nom}!")
            ennemi.attaquer(joueur)
            print(f"{joueur.nom} a maintenant {joueur.vie} points de vie.")

            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! Vous avez perdu.")
                break

jeu = Jeu()
jeu.lancerJeu()
