class Rectangle:
    def __init__(self, longueur, largeur):
        # Les doubles tirets bas rendent l'attribut privé
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseur (Getter) pour la longueur
    def get_longueur(self):
        return self.__longueur

    # Mutateur (Setter) pour la longueur
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    # Accesseur (Getter) pour la largeur
    def get_largeur(self):
        return self.__largeur

    # Mutateur (Setter) pour la largeur
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Test du code
mon_rect = Rectangle(10, 5)
print(f"Longueur initiale : {mon_rect.get_longueur()}") # Affiche 10

mon_rect.set_longueur(20)
mon_rect.set_largeur(12)
print(f"Après modification : {mon_rect.get_longueur()}x{mon_rect.get_largeur()}") # Affiche 20x12