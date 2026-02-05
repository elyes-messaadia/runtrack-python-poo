import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self): # Surcharge de la méthode aire
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self): # Surcharge pour le cercle
        return math.pi * (self.radius ** 2)

# Test
rect = Rectangle(10, 5)
cercle = Cercle(5)
print(f"Aire Rectangle : {rect.aire()}")
print(f"Aire Cercle : {cercle.aire():.2f}")