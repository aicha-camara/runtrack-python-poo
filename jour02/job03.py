class Livre:
    def __init__(self, titre, auteur, nombre_de_pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = disponible

    def affichage(self):
        info = (
            f"INFORMATION :\n"
            f"Titre du livre : {self.__titre}\n"
            f"L'auteur : {self.__auteur}\n"
            f"Le nombre de pages : {self.__nombre_de_pages} pages\n"
            f"Disponibilité : {self.__disponible}\n"
        )
        return info

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def get_disponible(self):
        return self.__disponible

    def vérification(self):
        if self.__disponible > 0:
            print("Le livre est disponible.")
        else:
            print("Le livre n'est plus disponible.")

    def emprunter(self, choix):
        # Méthode pour emprunter le livre
        if choix == "oui" and self.__disponible > 0:
            self.__disponible -= 1
            print("Vous avez pris un exemplaire.\n")
        elif choix == "oui" and self.__disponible <= 0:
            print("Désolé, le livre n'est plus disponible.\n")
        elif choix == "non":
            print(f"Vous n'avez rien emprunté. Il reste {self.__disponible} exemplaire(s) disponible(s).\n")
        else:
            print("Réponse non reconnue. Veuillez répondre 'oui' ou 'non'.\n")

        return bool(self.__disponible)

    def rendre(self, choix):
        if self.__disponible < 1:  
            if choix == "oui":
                self.__disponible += 1
                print("Vous avez rendu le livre.\n")
            elif choix == "non":
                print("Vous n'avez pas rendu le livre.\n")
            else:
                print("Réponse non reconnue. Veuillez répondre 'oui' ou 'non'.\n")   
        else:
            print("Vous ne pouvez pas rendre un livre sans l'avoir emprunté au préalable.\n")

livre_1 = Livre("L'écume des jours", "Boris Vian", 350, 1)
print(livre_1.affichage())
livre_1.vérification()
livre_1.emprunter("oui")
livre_1.vérification()
print("\nDisponibilité:", livre_1.get_disponible())
livre_1.rendre("oui")
print(livre_1.affichage())
