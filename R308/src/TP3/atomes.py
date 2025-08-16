### Atomes
class Atom:
    def __init__(self,nbproton,nbneutron):
        self.masseneutron = 1.675e-27
        self.masseproton = 1.673e-27
        self.nbproton = nbproton
        self.nbelectron = nbproton
        self.nbneutron = nbneutron

    def masse(self):
        return self.nbneutron*self.masseneutron+self.masseproton*self.nbproton
    
    def NbElecExt(self):
        if self.nbelectron <= 2:
            return self.nbelectron
        else:
            return self.nbelectron - (8 * (self.nbelectron - 2) // 8)
            # alternatif:
            # decompte = self.nbelectron - 2
            # while decompte > 8:
            #    decompte -= 8
            # return decompte

    def memeFamille(self,elem):
        assert isinstance(elem,Atom)
        return self.NbElecExt() == elem.NbElecExt()
    
    def isotope(self, elem):
        assert isinstance(elem, Atom)
        return self.nbproton == elem.nbproton and self.nbneutron != elem.nbneutron

# on crée deux atomes, carbone 12 et 14
carbone12 = Atom(nbproton=6, nbneutron=6)  
carbone14 = Atom(nbproton=6, nbneutron=8) 

# on crée un atome oxygène
oxygene16 = Atom(nbproton=8, nbneutron=8)  

# methode masse
print("Masse du Carbone 12 :", carbone12.masse())

# méthode même famille
print("Carbone 12 et Oxygène 16 sont de la même famille :", carbone12.memeFamille(oxygene16))

# méthode isotope
print("Carbone 12 et Carbone 14 sont isotopes :", carbone12.isotope(carbone14))  
print("Carbone 12 et Oxygène 16 sont isotopes :", carbone12.isotope(oxygene16))  