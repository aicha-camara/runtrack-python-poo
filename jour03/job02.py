class CompteBancaire:
    def __init__(self,numero_de_compte , nom , prenom , solde , decouvert=True):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_numero_de_compte(self):
        return self.__numero_de_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
   
    def get_decouvert(self):
        return self.__decouvert

    def set_solde(self , nouveau_solde):
        self.__solde = nouveau_solde  
        return self.__solde  


    def afficher(self):
        info_compte = ( 
            f"Numero de compte = {self.__numero_de_compte}\n"
            f"Nom = {self.__nom}\n"
            f"Prenom = {self.__prenom}\n"
            
        )
        return info_compte

    def afficherSolde(self):
        
        info_solde = (f"Le solde de {self.__nom} = {self.__solde} €\n")
       
        return info_solde
         
    def versement(self , x):
        if x > 0:
            self.__solde += x
            print(f"Vous avez versé : {x}€\nLe nouveau solde de {self.__nom} est de :\n{self.afficherSolde()}")
        return self.__solde

    def retrait(self , x):

        if x > 0 and self.__solde - x < self.__decouvert:
            print(f"Vous ne pouvez pas retirer, votre montant: {x}€ dépasse le découvert autorisé.")
        else:
            self.__solde -= x
            print(f"Vous avez retiré : {x}€\nLe nouveau solde de {self.__nom} est de :\n{self.afficherSolde()}")
        self.afficherSolde()
         
        return self.__solde

    def agios(self):
        if self.__solde < 0:
            frais = 5
            self.__solde -= frais
            print(f"Des frais supplémentaires de {frais} ont été appliqués dans votre compte. Raison : Votre solde est en négatif.\n")
            
        return self.__solde

    def virement(self, x , autre):
        if x > 0 and self.__solde - x >= self.__decouvert:
            self.__solde -= x
            autre.__solde += x
            print (f"{self.__nom} à fait un virement de {x}€ à {autre.__nom}\nLe nouveau solde de {self.__nom} est de :\n{self.afficherSolde()}")
            
        else:
            print(f"le montant de {x}€ ne peut pas etre valide car vous depassez le decouvert ou montant invalide") 

        return self.__solde


john = CompteBancaire(1000 ,"John", "Doe" , 60 , -20)
alice = CompteBancaire(1001 , "Alice" , "Doe" , -10 , -20)


print(john.afficher() )
print(john.afficherSolde())
john.versement(20)
john.retrait(30)


print(alice.afficher() )
print(alice.afficherSolde())
print(alice.agios())


john.virement(15,alice)
print(alice.afficher())
print(alice.afficherSolde())


