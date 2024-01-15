class Livre:
    def __init__( self, titre , auteur , nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
     
    def affichage(self):
        info = (
            f"Titre du livre : {self.__titre}\n"
            f"L'auteur : {self.__auteur}\n"
            f"Le nombre de pages : {self.__nombre_de_pages} pages\n"
        )
        return info

    def get_titre(self):
        return self.__titre    
    
    def get_auteur(self):
        return self.__auteur    
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages  
    
    def set_nombre_de_pages(self , nouveau_nombre_de_pages):
        if isinstance(nouveau_nombre_de_pages , int) and nouveau_nombre_de_pages >= 0:
            self.__nombre_de_pages = nouveau_nombre_de_pages
            print("Le nombre de pages a bien été mis a jour\n")
        else:
            print(f"Erreur ce n'est pas un nombre positif ({nouveau_nombre_de_pages})")

livre_1 = Livre("L'écume des jours" ,"Boris Vian" , 350 )
print(livre_1.affichage())
livre_1.set_nombre_de_pages(50)
print(livre_1.affichage())


