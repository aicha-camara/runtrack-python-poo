class Student:
    def __init__(self, prenom, nom, numero_etudiants, nombre_credit):
        self.__prenom = prenom
        self.__nom = nom
        self.__numero_etudiants = numero_etudiants
        self.__nombre_credit = nombre_credit
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom 

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiants(self):
        return self.__numero_etudiants

    def get_nombre_credit(self):
        return self.__nombre_credit

    def add_credit(self, x):
        if x > 0:
            self.__nombre_credit += x
            self.__level = self.__studentEval()
        return self.__nombre_credit

    def __studentEval(self):
        if self.__nombre_credit >= 90:
            return "Excellent"
        elif self.__nombre_credit >= 80:
            return "Très bien"
        elif self.__nombre_credit >= 70:
            return "Bien"
        elif self.__nombre_credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def get_level(self):
        return self.__level

    def studentInfo(self):
        info = (
            f"Nom = {self.__nom}\n"
            f"Prenom = {self.__prenom}\n"
            f"ID = {self.__numero_etudiants}\n"
            f"Niveau = {self.__level}\n"
        )
        return info
# Exemple d'utilisation
john = Student("John", "Doe", 145, 0)
john.add_credit(10)
john.add_credit(50)
john.add_credit(30)


print(f"Le nombre de crédits de {john.get_prenom()} {john.get_nom()} est de {john.get_nombre_credit()} points.")
print(john.studentInfo())
