class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge est de : {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne): # Héritage de Personne
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self): # Redéfinition de la méthode
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere, age=40):
        super().__init__(age) # Appelle le constructeur du parent
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")

# --- Tests Job 1 & 2 ---
eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()

prof1 = Professeur("Mathématiques", 40)
prof1.bonjour()
prof1.enseigner()