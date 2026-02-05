class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__plats_commandes = {} # Dictionnaire {nom: prix}
        self.__statut = "en cours"

    def ajouter_plat(self, nom, prix):
        if self.__statut == "en cours":
            self.__plats_commandes[nom] = prix
        else:
            print("Impossible d'ajouter des plats à une commande terminée ou annulée.")

    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée.")

    # Méthode privée pour le calcul
    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    def calculer_tva(self, taux=0.20):
        return self.__calculer_total() * taux

    def afficher_commande(self):
        total = self.__calculer_total()
        tva = self.calculer_tva()
        print(f"Commande N°{self.__numero} - Statut: {self.__statut}")
        for plat, prix in self.__plats_commandes.items():
            print(f"- {plat} : {prix}€")
        print(f"Total HT : {total}€ | TVA : {tva:.2f}€ | Total TTC : {total + tva:.2f}€")

# Test du Job 06
ma_commande = Commande(101)
ma_commande.ajouter_plat("Pizza Margherita", 12)
ma_commande.ajouter_plat("Tiramisu", 7)
ma_commande.afficher_commande()