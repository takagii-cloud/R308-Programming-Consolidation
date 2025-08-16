### Parking
class Parking:
    def __init__(self, adresse, capacite, libre, portails):
        self.adresse = adresse
        self.capacite = capacite
        assert libre <= capacite
        self.libre = libre
        self.portails = portails
        self.nbportails = len(portails)
    
    def update(self):
        for portail in self.portails:
            portail.places = self.libre

    def afficher(self):
        # Etat du parking
        print(f"Parking à {self.adresse}:")
        print(f"capacite totale: {self.capacite}")
        print(f"Places libres: {self.libre}/{self.capacite}")
        for portail in self.portails:
            portail.afficher()

class Portail:
    def __init__(self, parking, numéro, places, entrées, sorties):
        assert isinstance(parking, Parking)
        self.parking = parking
        self.numéro = numéro
        self.places = places
        self.entrées = entrées
        self.sorties = sorties

    def sortie(self):
        if self.parking.libre == self.parking.capacite:
            print(f"Portail {self.numéro}: Parking Vide!")
        else:
            self.parking.libre += 1
            self.places += 1
            self.sorties += 1
            self.parking.update()
            print(f"Portail {self.numéro}: -1 véhicule")
        parking.afficher()

    def entrée(self):
        if self.places == 0:
            print(f"Portail {self.numéro}: Parking Complet!")
            raise ValueError("Parking complet")
        else:
            self.parking.libre -= 1
            self.places -= 1
            self.entrées += 1
            self.parking.update()
            print(f"Portail {self.numéro}: +1 véhicule")
        parking.afficher()
    
    def afficher(self):
        # Méthode pour afficher l'état du portail
        print(f"Portail {self.numéro}:")
        print(f"  Places libres via ce portail: {self.places}")
        print(f"  Entrées: {self.entrées}, Sorties: {self.sorties}")


# Tests
parking = Parking("Parking IUT", 10, 10, [])

# Portails
portail1 = Portail(parking, 1, 5, 0, 0)
portail2 = Portail(parking, 2, 5, 0, 0)

# Portails au parking
parking.portails = [portail1, portail2]

# Etat initial
parking.afficher()

# Une entrée, puis une sortie
portail1.entrée()
portail1.sortie()

# Etat, après l'entrée et la sortie
parking.afficher()


