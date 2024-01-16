class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom   

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nouveau_nombre_habitants):
        self.__nombre_habitants = nouveau_nombre_habitants                

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville        
    
    def ajouterPopulation(self):
        nouveau_nombre_habitants = self.__ville.get_nombre_habitants() + 1
        self.__ville.set_nombre_habitants(nouveau_nombre_habitants)
        

ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille" , 861635)

john = Personne("John" , 45 , ville_paris)
myrtille = Personne("Myrtille" , 4 , ville_paris)
chloe = Personne("Chloé" , 18 , ville_marseille)

print(f"Population de la ville {ville_paris.get_nom()} : {ville_paris.get_nombre_habitants()} habitants")
print(f"Population de la ville {ville_marseille.get_nom()} : {ville_marseille.get_nombre_habitants()} habitants")
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Mise a jour de la population de la ville de  {ville_paris.get_nom()} {ville_paris.get_nombre_habitants()} habitants")
print(f"Mise a jour de la population de la ville de  {ville_marseille.get_nom()}  {ville_marseille.get_nombre_habitants()} habitants")
