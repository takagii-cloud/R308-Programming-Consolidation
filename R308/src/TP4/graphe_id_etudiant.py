# Classe Noeud 
class Noeud:
    def __init__(self, id):
        self.id = id  # id unique

# Classe Graphe 
class Graphe:
    def __init__(self):
        self.noeuds = [] # Liste de noeuds
        self.arretes = {} # Dictionnaire d'arrêtes	

    def addNode(self, id):
        # Ajout d'un nouveau nœud si l'id n'éxiste pas
        if id not in self.noeuds:
            self.noeuds.append(id)  # Ajoute le nœud à la liste des nœuds
            self.arretes[id] = []  # Initialise la liste des voisins du nœud
        else:
            print(f"Le nœud avec l'identifiant {id} existe déjà.")

    def addEdge(self, x, y):
        # Ajoute une arête entre deux nœuds x et y, si ces nœuds existent dans le graphe
        if x not in self.noeuds or y not in self.noeuds:
            print(f"Un des nœuds {x} ou {y} n'existe pas dans le graphe.")
            return
        
        # On vérifie que l'arête entre x et y n'existe pas déjà avant de l'ajouter
        if y not in self.arretes[x]:
            self.arretes[x].append(y)  # y devient voisin de x
            self.arretes[y].append(x)  # x devient voisin de y

    def getNeighbors(self, x):
        # Retourne la liste des voisins d'un nœud x
        return self.arretes.get(x, [])

    def degree(self, x):
        # Retourne le degré d'un nœud x (le nombre de voisins)
        voisins = self.getNeighbors(x)
        return len(voisins)

    def degreeDistribution(self):
        # Calcule la distribution des degrés 
        distribution = {}
        for noeud in self.noeuds:
            deg = self.degree(noeud)
            if deg in distribution:
                distribution[deg] += 1
            else:
                distribution[deg] = 1
        return distribution

# Classe UndirectedGraph 
class UndirectedGraph(Graphe):
    def __init__(self):
        super().__init__()  # Classe Graphe

    def dfs(self, start_node):
        # Effectue un DFS depuis le noeud de départ
        visited = set()  # Stocker les noeuds visités (set crée un objet non ordonné)
        stack = [start_node]  # Noeuds à explorer
        
        # Tant qu'il reste des noeuds
        while stack:
            node = stack.pop()  # Dernier noeud ajouté
            if node not in visited:  # Si le noeud n'est pas encore visité
                visited.add(node)  # Marque comme visité
                # Ajoute les voisins non visités dans la pile
                for neighbor in self.getNeighbors(node):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited

    def IsConnected(self):
        if not self.noeuds:
            return True  # graphe vide = connexe
        
        start_node = self.noeuds[0]  # noeu de départ
        visited = self.dfs(start_node)  # DFS depuis le noeud
        
        # Alors Graphe Connexe
        return len(visited) == len(self.noeuds)

# mon id étudiant est: 12302728

# Chaque chiffre st un noeud
n1, n2, n3, n0 = 1, 2, 3, 0  
n7, n8 = 7, 8  

# on crée le graphe
monGraphe = Graphe()

# Ajout des noeuds
monGraphe.noeuds = [n1, n2, n3, n0, n7, n8]  

# Def des arrêtes
monGraphe.arretes = {n1: [n2], n2: [n1, n3], n3: [n2, n0], n0: [n3, n7], n7: [n0, n8], n8: [n7, n2]  
}

# Affichage
print("Liste des nœuds :", monGraphe.noeuds)
print("Arêtes du graphe :", monGraphe.arretes)
