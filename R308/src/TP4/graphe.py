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
        # Ajout d'un nouveau nœud si l'idd n'éxiste pas
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
        # Calcule la distribution des degrés dans le graphe
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
                # Ajoute les voisins non visités dans la pile pour explorer plus tard
                for neighbor in self.getNeighbors(node):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited

    def IsConnected(self):
        # Vérifie si tous les nœuds du graphe sont accessibles à partir d'un nœud
        if not self.noeuds:
            return True  # Un graphe vide est considéré comme connexe
        
        start_node = self.noeuds[0]  # Sélectionne un nœud de départ arbitrairement
        visited = self.dfs(start_node)  # Lance un DFS depuis ce nœud
        
        # Si tous les nœuds ont été visités, alors le graphe est connexe
        return len(visited) == len(self.noeuds)

# Création d'un graphe g
g = Graphe()

# Ajout de nœuds
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addNode(4)

# Ajout d'arêtes entre les nœuds
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(1, 4)

# Vérification des nœuds et arêtes
print("Nœuds du graphe :", g.noeuds)  
print("Arêtes du graphe :", g.arretes)  

# Vérification des voisins de chaque nœud
print("Voisins du nœud 1 :", g.getNeighbors(1))  # Doit afficher [2, 4]
print("Voisins du nœud 2 :", g.getNeighbors(2))  # Doit afficher [1, 3]
print("Voisins du nœud 3 :", g.getNeighbors(3))  # Doit afficher [2, 4]
print("Voisins du nœud 4 :", g.getNeighbors(4))  # Doit afficher [3, 1]

# Vérification du degré de chaque nœud
print("Degré du nœud 1 :", g.degree(1))  
print("Degré du nœud 2 :", g.degree(2))  
print("Degré du nœud 3 :", g.degree(3))  
print("Degré du nœud 4 :", g.degree(4))  

# Distribution des degrés
distribution = g.degreeDistribution()
print("Distribution des degrés :", distribution)  

# DFS
visited = g.dfs(1)
print("Nœuds visités en DFS à partir de nœud 1 :", visited)  

# Connexte
is_connected = g.IsConnected()
print("Le graphe est-il connexe ?", is_connected)  # True
