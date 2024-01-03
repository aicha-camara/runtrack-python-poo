class Animal:
    def __init__(self,age, nom):
        self.age = age 
        self.nom = nom
    
    def veillir(self):
        print("l'age de l'animal est de :" , animal.age , "ans")
        self.age += 1 
        return print("l'age de l'animal est de :" , animal.age , "ans")
    def nommer(self , nom):
        print("l'animal se nomme" , nom)    

animal = Animal(0 ,"")
animal.veillir()
animal.nommer("Luna")
