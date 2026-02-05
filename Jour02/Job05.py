class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Accesseurs et Mutateurs (quelques exemples)
    def get_marque(self): return self.__marque
    def set_marque(self, marque): self.__marque = marque

    # Méthode privée pour vérifier le carburant
    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre... Vroum !")
        else:
            print("Pas assez d'essence pour démarrer !")

    def arreter(self):
        self.__en_marche = False
        print("Moteur coupé.")

# Test du Job 05
ma_caisse = Voiture("Toyota", "Yaris", 2022, 15000)
ma_caisse.demarrer()