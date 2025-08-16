class Intervale:
    def __init__(self, d, f):
        assert d <= f
        self.d = d
        self.f = f

    def e(self, Y):  # égal
        assert isinstance(Y, Intervale)
        return (self.d == Y.d and self.f == Y.f)

    def b(self, Y):  # avant
        assert isinstance(Y, Intervale)
        return (self.f < Y.d)

    def m(self, Y):  # précède
        assert isinstance(Y, Intervale)
        return (self.f == Y.d)

    def o(self, Y):  # chevauche
        assert isinstance(Y, Intervale)
        return (self.d < Y.d and self.f > Y.d and self.f < Y.f)

    def s(self, Y):  # commence
        assert isinstance(Y, Intervale)
        return (self.d == Y.d and self.f < Y.f)

    def termine(self, Y):  # termine
        assert isinstance(Y, Intervale)
        return (self.d > Y.d and self.f == Y.f)

    def pendant(self, Y):  # pendant
        assert isinstance(Y, Intervale)
        return (self.d > Y.d and self.f < Y.f)

    # Méthodes inverses
    def bi(self, Y):  # après
        assert isinstance(Y, Intervale)
        return Y.b(self)

    def mi(self, Y):  # est précédé par
        assert isinstance(Y, Intervale)
        return Y.m(self)

    def oi(self, Y):  # est chevauché par
        assert isinstance(Y, Intervale)
        return Y.o(self)

    def si(self, Y):  # est commencé par
        assert isinstance(Y, Intervale)
        return Y.s(self)

    def fi(self, Y):  # est terminé par
        assert isinstance(Y, Intervale)
        return Y.termine(self)

    def di(self, Y):  # est pendant à
        assert isinstance(Y, Intervale)
        return Y.pendant(self)


# TEST:
A = Intervale(0, 1)
B = Intervale(4, 5)
C = Intervale(1, 2)
D = Intervale(0, 3)
E = Intervale(1, 5)
testList = [A, B, C, D, E]

results = []

# On attend: [[e,b,m,s,m],[bi,e,bi,bi,fi],[mi,b,e,di,s],[si,b,di,e,o],[mi,fi,si,oi,e]]
for x in testList:
    row = []
    for y in testList: # on compare chaque intervalle avec chaque autre
        if x.e(y):
            row.append('e')

        elif x.b(y):
            row.append('b')

        elif x.m(y):
            row.append('m')

        elif x.o(y):
            row.append('o')

        elif x.s(y):
            row.append('s')

        elif x.termine(y):
            row.append('f')

        elif x.pendant(y):
            row.append('d')

        elif x.bi(y):  
            row.append('bi')

        elif x.mi(y):  
            row.append('mi')

        elif x.oi(y):  
            row.append('oi')

        elif x.si(y):  
            row.append('si')

        elif x.fi(y):  
            row.append('fi')

        elif x.di(y):  
            row.append('di')
        else:
            row.append('-') #quand on a aucune intervalle (ça n'arrive pas dans notre cas)
    results.append(row)

for res in results:
    print(res)
