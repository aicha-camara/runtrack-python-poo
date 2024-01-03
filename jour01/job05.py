class Point:
    
    def __init__(self, nom ,nombre):
        self.nom = nom
        self.nombre = nombre

    def afficherLesPoints(self, deuxieme):
        print("la coordonnée de x et y est " , "(" ,self.nombre ,";", deuxieme.nombre ,")")
    
    def afficherX(self):
        print("x = " , self.nombre)
    
    def afficherY(self):
        print("y = " , self.nombre)

    def changerX(self , nouveau_nombre_x):
        self.nombre = nouveau_nombre_x
        print("La coordonnée de", self.nom, "a prit la nouvelle valeur", nouveau_nombre_x )
    
    def changerY(self , nouveau_nombre_y):
        self.nombre = nouveau_nombre_y
        print("La coordonnée de", self.nom, "a prit la nouvelle valeur", nouveau_nombre_y )

x = Point("x" ,25)       
y = Point("y" ,52)

x.afficherLesPoints(y)
x.afficherX()
y.afficherY()
x.changerX(80)
y.changerY(100)
x.afficherLesPoints(y)

