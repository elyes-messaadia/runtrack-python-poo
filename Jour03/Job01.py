class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_habitants(self):
        return self.__habitants

    def ajouter_habitant(self):
        self.__habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville # Ici, on stocke la RÉFÉRENCE de l'objet Ville

    def ajouterPopulation(self):
        # On utilise la méthode de l'objet Ville pour augmenter la population
        self.__ville.ajouter_habitant()

# --- Test du code ---
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population initiale de Paris : {paris.get_habitants()}")
print(f"Population initiale de Marseille : {marseille.get_habitants()}")

# Création des personnes (on leur donne l'objet ville en paramètre)
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de la population
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Population de Paris après arrivées : {paris.get_habitants()}")
print(f"Population de Marseille après arrivées : {marseille.get_habitants()}")