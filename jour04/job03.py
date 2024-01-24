class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longeur(self):
        return self.__longueur    
    
    def get_largeur(self):
        return self.__largeur    

    def set_longueur(self,nouvelle_longeur):
        self.__longueur = nouvelle_longeur
        return self.__longueur
    
    def set_largeur(self,nouvelle_largeur):
        self.__largeur = nouvelle_largeur
        return self.__largeur

    def perimètre(self):
        calcule = 2*(self.__longueur + self.__largeur)
        print(f"Le périmetre est de {calcule} ")

    def surface(self):
        calcule = self.__longueur * self.__largeur
        print(f"La surface est de {calcule} ")

class Parallelepipede(Rectangle):
    def __init__(self,longueur,largeur,hauteur):
        super().__init__(longueur,largeur)
        self.__hauteur = hauteur
        
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self,nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur
        return self.__hauteur

    def volume(self):
        calcule = self.get_longeur() * self.get_largeur() * self.__hauteur
        print(f"Le volume est de {calcule} ")

rectangle = Rectangle(10,10)
parallelepipede = Parallelepipede(10,10,20)

rectangle.perimètre()
rectangle.set_largeur(20)
rectangle.set_longueur(20)
rectangle.perimètre()

rectangle.surface()

parallelepipede.volume()
parallelepipede.set_hauteur(50)
parallelepipede.volume()


            