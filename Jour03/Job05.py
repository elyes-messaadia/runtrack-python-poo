import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats # On modifie l'objet adverse directement
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 0

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau (1: Facile, 2: Difficile) : "))

    def lancerJeu(self):
        pv = 100 if self.niveau == 1 else 50
        joueur = Personnage("Héros", pv)
        ennemi = Personnage("Monstre", 100)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie > 0:
                ennemi.attaquer(joueur)
            print(f"PV: {joueur.nom}: {joueur.vie} | {ennemi.nom}: {ennemi.vie}\n")

        if joueur.vie > 0:
            print("Victoire !")
        else:
            print("Défaite...")

# Pour tester : 
# partie = Jeu()
# partie.choisirNiveau()
# partie.lancerJeu()