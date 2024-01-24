class Personne:
    def __init__(self,age=14):
        self.age = age
    def afficherAge(self):
        info = (
            f"l'age = {self.age}"
        )
        return info

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouveau_age):
        self.age = nouveau_age
        return self.age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans") 

class Professeur:
    
    def __init__(self, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer") 



personne = Personne()
print(personne.afficherAge())  
eleve = Eleve()
eleve.afficherAge()
