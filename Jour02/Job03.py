class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True # Par défaut à True

    # Méthode de vérification
    def verification(self):
        return self.__disponible

    def emprunter(self):
        # On vérifie la disponibilité via la méthode interne, pas l'attribut directement
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible.")

    def rendre(self):
        # On vérifie s'il a été emprunté (donc s'il n'est plus dispo)
        if not self.verification():
            self.__disponible = True
            print("Livre rendu. Merci !")
        else:
            print("Ce livre est déjà dans nos rayons.")

# Test du Job 03
mon_livre = Livre("L'Étranger", "Camus", 150)
print(f"Disponible ? {mon_livre.verification()}")
mon_livre.emprunter()
print(f"Disponible ? {mon_livre.verification()}")
mon_livre.rendre()