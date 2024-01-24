class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        info = (
            f"Marque = {self.marque}\n"
            f"Modele = {self.modele}\n"
            f"Année = {self.annee}\n"
            f"Prix = {self.prix}\n"
        )
        return info

    def demarrer(self):
        print("Attention, je roule.")    

class Voiture(Vehicule):
    def __init__(self, marque , modele , annee , prix , portes=4):
        super().__init__( marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        return super().informationsVehicule() + f"Nombre de portes = {self.portes}\n"

    def demarrer(self):
        print("Mon gros vehicule a 4 roues roule!")

class Moto(Vehicule):
    def __init__(self ,marque , modele , annee , prix , roue=2):
        super().__init__( marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        return super().informationsVehicule() + f"Nombre de roue = {self.roue}\n"

    def demarrer(self):
        print("Mon petit vehicule a 2 roues roule!") 

voiture = Voiture("Mercedes","Classe A",2020,18500)
moto = Moto("Yamaha","1200 Vmax", 1987,4500)
print(voiture.informationsVehicule())
print(moto.informationsVehicule())
voiture.demarrer()
moto.demarrer()
