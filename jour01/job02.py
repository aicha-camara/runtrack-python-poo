class Operator:
    def __init__(self, nombre , chiffre):
        self.numero = nombre
        self.chiffre = chiffre
    
    def affichage(self):
        print("Le" , self.numero , "est" , self.chiffre)

nombre1 = Operator("Nombre1" , 10)
nombre1.affichage()

nombre2 = Operator("Nombre2" , 20)
nombre2.affichage()