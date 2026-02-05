class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte N°{self.__numero} | Titulaire: {self.__nom} {self.__prenom} | Solde: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué.")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Erreur : Solde insuffisant.")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= 10 # Application d'agios forfaitaires
            print("Agios appliqués (solde négatif).")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant) # On agit sur l'autre compte par référence
            print("Virement effectué avec succès.")
        else:
            print("Virement échoué : Solde insuffisant.")

# --- Test du code ---
compte1 = CompteBancaire(123, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(456, "Doe", "Jane", -200, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.virement(compte2, 300)

compte1.afficher()
compte2.afficher()