class Joueur:
    def __init__(self, nom, numero, position, buts_marques=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = buts_marques
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.buts_marques += 1
        return self.buts_marques

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        return self.passes_decisives

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        return self.cartons_jaunes

    def afficherStatistiques(self):
        statistiques = (
            f"Statistiques pour {self.nom} - Numéro {self.numero}:\n"
            f"Buts marqués: {self.buts_marques}\n"
            f"Passes décisives: {self.passes_decisives}\n"
            f"Cartons jaunes: {self.cartons_jaunes}\n"
            f"Cartons rouges: {self.cartons_rouges}"
        )
        print(statistiques)

class Equipe:
    def __init__(self, nom_equipe):
        self.nom_equipe = nom_equipe
        self.liste_joueur = []

    def ajouter_Joueur(self, joueur):
        self.liste_joueur.append(joueur)

    def afficherStatistiquesJoueur(self):
        for joueur in self.liste_joueur:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, nouveaux_buts=0, nouvelles_passes=0, nouveaux_cartons_jaunes=0, nouveaux_cartons_rouges=0):
        joueur.buts_marques += nouveaux_buts
        joueur.passes_decisives += nouvelles_passes
        joueur.cartons_jaunes += nouveaux_cartons_jaunes
        joueur.cartons_rouges += nouveaux_cartons_rouges

        return {
            "buts_marques": joueur.buts_marques,
            "passes_decisives": joueur.passes_decisives,
            "cartons_jaunes": joueur.cartons_jaunes,
            "cartons_rouges": joueur.cartons_rouges
        }

# Création des joueurs
joueur1 = Joueur("Joueur1", 10, "Attaquant" , 2)
joueur2 = Joueur("Joueur2", 11, "Milieu")
joueur3 = Joueur("Joueur3", 5, "Défenseur")
joueur4 = Joueur("Joueur4", 6, "Attaquant")

# Création des équipes
equipeA = Equipe("Équipe A")
equipeB = Equipe("Équipe B")

# Ajout des joueurs aux équipes
equipeA.ajouter_Joueur(joueur1)
equipeA.ajouter_Joueur(joueur2)

equipeB.ajouter_Joueur(joueur3)
equipeB.ajouter_Joueur(joueur4)

# Affichage des statistiques des joueurs avant le match
print("Statistiques avant le match:\n")
print ("L'equipe A")
equipeA.afficherStatistiquesJoueur()
print ("\nL'equipe B")

equipeB.afficherStatistiquesJoueur()

# Simulation d'un match
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

# Affichage des statistiques des joueurs après le match
print("\nStatistiques après le match:")
equipeA.afficherStatistiquesJoueur()
equipeB.afficherStatistiquesJoueur()

# Mise à jour des statistiques d'un joueur
equipeA.mettreAJourStatistiquesJoueur(joueur1, nouveaux_buts=2, nouvelles_passes=1)

# Affichage des statistiques après la mise à jour
print("\nStatistiques après mise à jour:")
equipeA.afficherStatistiquesJoueur()
