class Operator:
    def __init__(self, nombre , chiffre):
        self.numero = nombre
        self.chiffre = chiffre
    
    def affichage(self):
        print("Le" , self.numero , "est" , self.chiffre)

    def addition(self, deuxieme):
        calcul = self.chiffre + deuxieme.chiffre
        print("L'addition des 2 nombres est" ,calcul)


nombre1 = Operator("Nombre1" , 10)
nombre1.affichage()

nombre2 = Operator("Nombre2" , 20)
nombre2.affichage()


nombre1.addition(nombre2)
