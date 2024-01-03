class Personne:
    def __init__ (self, nom , prenom):
        self.nom = nom
        self.prenom = prenom
  
    def SePresenter(self):
        print("Je suis" , self.prenom , self.nom )
        return

john = Personne("Doe" , "John")
john.SePresenter()

jean = Personne("Dupont" , "Jean")
jean.SePresenter()