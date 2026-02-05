class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_d = 0
        self.jaunes = 0
        self.rouges = 0

    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_d += 1
    
    def recevoirUnCartonJaune(self):
        self.jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print(f"Joueur: {self.nom} (N°{self.numero}) - {self.position}")
        print(f"Stats: {self.buts} buts, {self.passes_d} passes D, {self.jaunes} jaunes, {self.rouges} rouges")
        print("-" * 30)

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"=== Statistiques de l'équipe : {self.nom} ===")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        # On cherche le joueur dans la liste par son nom
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but": joueur.marquerUnBut()
                elif action == "passe": joueur.effectuerUnePasseDecisive()
                elif action == "jaune": joueur.recevoirUnCartonJaune()
                elif action == "rouge": joueur.recevoirUnCartonRouge()
                return
        print(f"Joueur {nom_joueur} non trouvé.")

# --- Simulation du match ---

# 1. Création des joueurs
j1 = Joueur("Mbappé", 10, "Attaquant")
j2 = Joueur("Dembele", 7, "Attaquant")
j3 = Joueur("Messi", 10, "Milieu")

# 2. Création des équipes et ajout des joueurs
equipe1 = Equipe("France")
equipe2 = Equipe("Argentine")

equipe1.ajouterJoueur(j1)
equipe1.ajouterJoueur(j2)
equipe2.ajouterJoueur(j3)

# 3. Affichage avant le match
print("AVANT LE MATCH")
equipe1.afficherStatistiquesJoueurs()

# 4. Simulation d'actions (Le match se déroule)
equipe1.mettreAJourStatistiquesJoueur("Mbappé", "but")
equipe1.mettreAJourStatistiquesJoueur("Mbappé", "but")
equipe1.mettreAJourStatistiquesJoueur("Dembele", "passe")
equipe1.mettreAJourStatistiquesJoueur("Dembele", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Messi", "but")

# 5. Affichage après le match
print("\nAPRÈS LE MATCH")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()