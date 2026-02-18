from collections import defaultdict, deque
from typing import List, Set, Dict, Optional, Tuple

class Graph : 
    """
    Implémentation d'un graphe non-dirigé avec liste d'adjacence
    """

    def __init__(self , num_vertices  : int = 0 ) -> None:
        """
        Initialise le graphe
        
        Args:
            num_vertices: nombre de sommets (optionnel)
        
        Complexité: O(1)
        """
        self.num_vertices  = num_vertices 
        self.adj_list = defaultdict(list)
        self.num_edges = 0 
    
    def add_vertex(self , vertex : int) -> None : 
        """
        Ajoute un sommet au graphe
        
        Args:
            vertex: identifiant du sommet
        
        Complexité: O(1)
        """
        if vertex not in self.adj_list : 
            self.adj_list[vertex] = []
            self.num_vertices += 1 
    
    def add_edge(self, u: int, v: int) -> None:
        """
        Ajoute une arête entre u et v (non-dirigé)
        
        Args:
            u: sommet source
            v: sommet destination
        
        Complexité: O(1) amortie
        """
        # Ajouter les sommets s'ils n'existent pas 
        self.add_vertex(u)
        self.add_vertex(v)

        # AJouterl'aréte dans le deux sens : 
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.num_edges += 1 
    
    def remove_edge(self, u: int, v: int) -> bool:
        """
        Supprime l'arête entre u et v
        
        Args:
            u: sommet source
            v: sommet destination
        
        Returns:
            True si l'arête existait, False sinon
        
        Complexité: O(degree(u) + degree(v))
        """

        if u not in self.adj_list or v not in self.adj_list : 
            return False

        try : 
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)
            self.num_edges -= 1 
            return True 
        except ValueError : 
            return False 

    def has_edge(self, u: int, v: int) -> bool:
        """
        Vérifie si une arête existe entre u et v
        
        Args:
            u: sommet source
            v: sommet destination
        
        Returns:
            True si l'arête existe, False sinon
        
        Complexité: O(degree(u))
        """

        if u not in self.adj_list : 
            return False 
        return v in self.adj_list[u]
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """
        Retourne la liste des voisins d'un sommet
        
        Args:
            vertex: identifiant du sommet
        
        Returns:
            Liste des voisins
        
        Complexité: O(1)
        """
        return self.adj_list.get(vertex, [])
    
    def degree(self, vertex: int) -> int:
        """
        Retourne le degré d'un sommet
        
        Args:
            vertex: identifiant du sommet
        
        Returns:
            Nombre de voisins
        
        Complexité: O(1)
        """
        return len(self.adj_list.get(vertex, []))
    def get_vertices(self) -> List[int]:
        """
        Retourne la liste de tous les sommets
        
        Returns:
            Liste des sommets
        
        Complexité: O(V)
        """
        return list(self.adj_list.keys())
    def get_edges(self) -> List[tuple]:
        """
        Retourne la liste de toutes les arêtes
        
        Returns:
            Liste de tuples (u, v)
        
        Complexité: O(V + E)
        """
        edges : List[tuple] = []
        seen = set()

        for u in self.adj_list :
            for v in self.adj_list : 
                if (u,v) not in seen and (v,u) not in seen : 
                    edges.append((u,v))
                    seen.add((u,v))
        
        return edges
    
    def is_connected(self, u: int, v: int) -> bool:
        """
        Vérifie si deux sommets sont connectés (chemin existe)
        
        Args:
            u: sommet source
            v: sommet destination
        
        Returns:
            True s'il existe un chemin, False sinon
        
        Complexité: O(V + E)
        """

        if u not in self.adj_list or v not in self.adj_list : 
            return False 

        q = deque([u])
        visited = set() 
        visited.add(u)

        while q : 
            curr = q.popleft()

            if curr == v : 
                return True 

            for neighbor in self.adj_list[curr] : 
                if neighbor not in visited : 
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return False 


    def __str__(self) -> str:
        """
        Représentation en chaîne du graphe
        
        Complexité: O(V + E)
        """
        result = f"Graph with {self.num_vertices} vertices and {self.num_edges} edges:\n"
        for vertex in sorted(self.adj_list.keys()):
            neighbors = ", ".join(map(str, self.adj_list[vertex]))
            result += f"  {vertex} -> [{neighbors}]\n"
        return result
    
    def __repr__(self) -> str:
        return self.__str__()
    

# ================ Grid as Graphe : ==============
"""
**Grille 2D (16 sommets)**

Grille (0=libre, 1=obstacle):

    [0, 0, 1, 0]
    [0, 1, 0, 0]
    [0, 0, 0, 1]
    [1, 0, 0, 0]

Graphe équivalent (chaque case = sommet):

(0,0)---(0,1)  X  (0,3)
  |       |         |
(1,0)  X (1,2)---(1,3)
  |       |       |
(2,0)---(2,1)---(2,2)  X
        |       |
  X     (3,1)---(3,2)---(3,3)

Nombre de sommets: 4 × 4 = 16
(certains bloqués par obstacles)
"""
Grid  = List[List[int]]
VertexGrid = int
GraphGrid = Dict[VertexGrid , List[VertexGrid]] 
def grid_to_graph(grid : Grid) -> GraphGrid:
    """
    Convertit une grille en graphe explicite
    Chaque case (i,j) devient un sommet numéroté
    """
    graph : GraphGrid = {}
    rows , cols= len(grid) , len(grid[0])

    dircetions = [(-1 , 0) ,(1, 0) ,(0 , -1) , (0 ,1)]

    def to_vertex(r ,c) :
        return r*cols + c

    for row in range(rows) :
        for col in range(cols) : 

            # case if grid[row][col] == 1 : 
            if grid[row][col] == 1 : 
                continue

            vertex = to_vertex(row , col)
            graph[vertex] = []

            for dr , dc in dircetions : 
                new_row , new_col = row + dr , col + dc 
                if( 
                    0 <= new_row < rows and 
                    0 <= new_col < cols and
                    grid[new_row][new_col] == 0 
                ) : 
                    neighbor = to_vertex(new_row , new_col)
                    graph[vertex].append(neighbor)
    
    return  graph


if __name__ == "__main__":
    g = Graph()
    
    # Ajouter des arêtes
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    
    print(g)
    # Graph with 4 vertices and 4 edges:
    #   0 -> [1, 2]
    #   1 -> [0, 3]
    #   2 -> [0, 3]
    #   3 -> [1, 2]
    
    print(f"Voisins de 0: {g.get_neighbors(0)}")  # [1, 2]
    print(f"Degré de 1: {g.degree(1)}")  # 2
    print(f"Arête (0,1) existe? {g.has_edge(0, 1)}")  # True
    print(f"0 et 3 sont connectés? {g.is_connected(0, 3)}")  # True



