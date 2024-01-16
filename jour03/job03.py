class Tache:
    def __init__(self, titre, description, statut="A faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def set_statut(self, statut):
        self.statut = statut

class ListeDeTaches:
    def __init__(self, titre):
        self.titre = titre
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def marquer_comme_finie(self, tache):
        tache.set_statut("Terminée")

    def afficher_liste(self):
        for tache in self.taches:
            print(
                f"Titre: {tache.titre}\n"
                f"Description: {tache.description}\n"
                f"Statut: {tache.statut}\n"
            )

    def filter_liste(self, statut_filtre):
        taches_filtrees = [tache for tache in self.taches if tache.statut == statut_filtre]
        return taches_filtrees

liste_taches = ListeDeTaches("To Do List")

tache1 = Tache("1) Entrainement", " Aller au stade de foot")
tache2 = Tache("2) Devoir", "Faire les exercices de math")
tache3 = Tache("3) Magasin", "Faire les course du mois")
tache4 = Tache("4) Rdv", "Aller chez le dentiste")

print("\033[91m" + "Mes taches : \n" + "\033[0m")

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)
liste_taches.ajouter_tache(tache4)
liste_taches.afficher_liste()

print("\033[91m" + "Mes taches apres les modifications : \n" + "\033[0m")
liste_taches.marquer_comme_finie(tache2)
liste_taches.supprimer_tache(tache3)
liste_taches.afficher_liste()


statut_filtre = "Terminée"
taches_filtrees = liste_taches.filter_liste(statut_filtre)
print(f"\nTâches avec le filtre '{statut_filtre}':")
liste_taches.taches = taches_filtrees
liste_taches.afficher_liste()