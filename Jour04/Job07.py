import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        # Création du paquet de 52 cartes
        for c in couleurs:
            for v in valeurs:
                self.paquet.append(Carte(v, c))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def calculer_points(self, main):
        total = 0
        as_count = 0
        valeurs_points = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 
                         "10":10, "Valet":10, "Dame":10, "Roi":10}
        
        for carte in main:
            if carte.valeur == "As":
                as_count += 1
                total += 11
            else:
                total += valeurs_points[carte.valeur]
        
        # Gestion de l'As (1 ou 11)
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
        return total

    def jouer(self):
        self.melanger()
        joueur_main = [self.tirer_carte(), self.tirer_carte()]
        croupier_main = [self.tirer_carte(), self.tirer_carte()]

        # Tour du joueur
        while self.calculer_points(joueur_main) < 21:
            print(f"Votre main : {[c.valeur for c in joueur_main]} (Total: {self.calculer_points(joueur_main)})")
            choix = input("Voulez-vous tirer une carte ? (o/n) : ")
            if choix.lower() == 'o':
                joueur_main.append(self.tirer_carte())
            else:
                break

        score_j = self.calculer_points(joueur_main)
        if score_j > 21:
            print(f"Bust ! Vous avez perdu avec {score_j}.")
            return

        # Tour du croupier (s'arrête à 17)
        while self.calculer_points(croupier_main) < 17:
            croupier_main.append(self.tirer_carte())

        score_c = self.calculer_points(croupier_main)
        print(f"Croupier : {score_c} | Joueur : {score_j}")

        if score_c > 21 or score_j > score_c:
            print("Félicitations, vous avez gagné !")
        else:
            print("Le croupier gagne.")

# Pour lancer une partie :
# bj = Jeu()
# bj.jouer()