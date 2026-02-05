class Student:
    def __init__(self, nom, prenom, id_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etudiant = id_etudiant
        self.__credits = 0
        self.__level = self.__studentEval() # Initialise le niveau via la méthode privée

    def add_credits(self, quantite):
        if quantite > 0:
            self.__credits += quantite
            self.__level = self.__studentEval() # On recalcule le niveau après l'ajout
        else:
            print("Le montant de crédits doit être positif.")

    # Méthode privée (inaccessible depuis l'extérieur)
    def __studentEval(self):
        if self.__credits >= 90: return "Excellent"
        elif self.__credits >= 80: return "Très bien"
        elif self.__credits >= 70: return "Bien"
        elif self.__credits >= 60: return "Passable"
        else: return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, ID: {self.__id_etudiant}, Niveau: {self.__level}")

# Test du code
john = Student("Doe", "John", 145)
john.add_credits(30)
john.add_credits(30)
john.add_credits(20) # Total 80 crédits
john.studentInfo() # Devrait afficher "Très bien"