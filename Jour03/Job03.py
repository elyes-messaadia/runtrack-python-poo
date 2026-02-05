class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

class ListeDeTaches:
    def __init__(self):
        self.taches = [] # Liste qui contiendra des objets Tache

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"

    def afficherListe(self):
        return [f"{t.titre} ({t.statut})" for t in self.taches]

# --- Test du code ---
ma_liste = ListeDeTaches()
t1 = Tache("Courses", "Acheter du pain")
t2 = Tache("Python", "Finir le Jour 3")

ma_liste.ajouterTache(t1)
ma_liste.ajouterTache(t2)
ma_liste.marquerCommeFinie("Courses")

print("Toutes les tâches :", ma_liste.afficherListe())