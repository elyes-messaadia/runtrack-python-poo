class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Accesseurs
    def get_titre(self): return self.__titre
    def get_auteur(self): return self.__auteur
    def get_nb_pages(self): return self.__nb_pages

    # Mutateurs
    def set_titre(self, titre): self.__titre = titre
    def set_auteur(self, auteur): self.__auteur = auteur
    
    def set_nb_pages(self, nb):
        # Vérification de l'intégrité des données
        if isinstance(nb, int) and nb > 0:
            self.__nb_pages = nb
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Test du code
mon_livre = Livre("Le Hobbit", "Tolkien", 300)
mon_livre.set_nb_pages(-50) # Affiche le message d'erreur
mon_livre.set_nb_pages(310) # Modifie la valeur normalement