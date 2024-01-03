class Produit:
    def __init__(self,nom,prixHT,tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.tva / 100)
        return prixTTC

    def afficher(self):
        info_produit = (
            f"Nom: {self.nom}\n"
            f"Prix HT: {self.prixHT} € \n"
            f"TVA: {self.tva} %\n"
            f"Prix TTC: {self.CalculerPrixTTC()} €"
        )
        return info_produit 

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def get_nom(self):
        return self.nom

    def get_prix(self):
        return self.prixHT


voiture1 = Produit("Voiture rouge" , 1000 , 20)
voiture2 = Produit("Voiture bleu" , 2000 , 20)
voiture3 = Produit("Voiture noir" , 3000 , 20)

infos_produit1 = voiture1.afficher()
infos_produit2 = voiture2.afficher()
infos_produit3 = voiture3.afficher()


print("Produit 1:")
print(infos_produit1)
print("\nProduit 2:")
print(infos_produit2)
print("\nProduit 3:")
print(infos_produit3)

voiture1.modifier_nom("Voiture rose")
voiture1.modifier_prix(1200)

voiture2.modifier_nom("Voiture verte")
voiture2.modifier_prix(2200)

voiture3.modifier_nom("Voiture grise")
voiture3.modifier_prix(3200)

print("\nInformations après modification :")
print("Produit 1:")
print(f"Nom : {voiture1.get_nom()}, Prix HT : {voiture1.get_prix()} €, Prix TTC : {voiture1.CalculerPrixTTC()} €")

print("\nProduit 2:")
print(f"Nom : {voiture2.get_nom()}, Prix HT : {voiture2.get_prix()} €, Prix TTC : {voiture2.CalculerPrixTTC()} €")

print("\nProduit 3:")
print(f"Nom : {voiture3.get_nom()}, Prix HT : {voiture3.get_prix()} €, Prix TTC : {voiture3.CalculerPrixTTC()} €")