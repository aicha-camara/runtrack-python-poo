class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def affichage(self):
        info = (
            f"La marque : {self.__marque}\n"
            f"Le modèle : {self.__modele}\n"
            f"L'année : {self.__annee}\n"
            f"Le kilométrage : {self.__kilometrage}\n"
            f"En marche : {self.__en_marche}\n"
            f"Le reservoir : {self.__reservoir}\n"
        )
        return info
   
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_reservoir(self):
        return self.__reservoir    
    
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque
        return self.__marque  
    
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele
        return self.__modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee
        return self.__annee
    
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage
        return self.__kilometrage  
    
    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir     

    def demarrer(self):
        self.__en_marche = True 
        self.__reservoir -= 5
        if self.__reservoir < 5:
            self.__en_marche = False
            
        return self.__en_marche

    def arreter(self):
        self.__en_marche = False
        return self.__en_marche
    
    def __verifier_plein(self):
        return self.__reservoir    


voiture = Voiture("Audi", "rs6", 2020, 50000, 50, False)

print(voiture.affichage())

voiture.demarrer()
print(voiture.affichage())

voiture.arreter()
print(voiture.affichage())

for _ in range(9):
    voiture.demarrer()

print(voiture.affichage())
