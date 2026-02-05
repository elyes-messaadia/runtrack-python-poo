class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    # Getters et Setters
    def get_longueur(self): return self.__longueur
    def set_longueur(self, l): self.__longueur = l
    def get_largeur(self): return self.__largeur
    def set_largeur(self, l): self.__largeur = l

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        # Utilise la surface du rectangle (parent) * hauteur
        return self.surface() * self.__hauteur

# Test
rect = Rectangle(10, 5)
print(f"Surface Rectangle : {rect.surface()}")

para = Parallelepipede(10, 5, 2)
print(f"Volume Parallélépipède : {para.volume()}")