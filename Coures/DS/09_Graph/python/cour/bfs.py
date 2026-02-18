from typing import Deque, Dict  , List, Optional, Tuple 
from collections import deque

# Task 1 :
"""
implement basic BFS for Graphe
"""
Node = int 
Graph = Dict[Node , List[Node]]

def bfs(graphe : Graph , start : Node) -> List[Node] :
    """
    Parcours BFS depuis un sommet de départ
    
    Args:
        graph: dict {sommet: [voisins]}
        start: sommet de départ
    
    Returns:
        Liste des sommets dans l'ordre de visite
    
    Complexité: O(V + E)
    """

    queue = deque([start])
    visited = set()
    visited.add(start)
    res = []
    while queue : 
        curr = queue.popleft()
        res.append(curr)

        for neignhor in graphe[curr] : 
            if neignhor not in visited : 
                visited.add(neignhor)
                queue.append(neignhor)
        
    return res 


# Task 2 : 
"""
BFS with levels 
"""

def bfs_with_levels(graph : Graph, start : Node) -> Dict[Node , int]:
    """
    BFS qui calcule aussi la distance de chaque sommet
    
    Returns:
        dict {sommet: distance_depuis_start}
    
    Complexité: O(V + E)
    """

    queue = deque([(start , 0)])
    visited = set([start])
    res = {start : 0}
    
    while queue : 
        vertex , dist = queue.popleft()

        for neignhor in graph[vertex] : 
            if neignhor not in visited : 
                visited.add(neignhor)
                res[neignhor] = dist + 1 
                queue.append((neignhor , dist + 1))
        
    return res 

# Task 3 : 
"""
Find the shortest path between two vertex  
"""
Path =  List[Node]

def bfs_shortest_path(graph : Graph , start : Node , target : Node) -> Optional[Path]:
    """
    Trouve le plus court chemin entre start et target
    
    Returns:
        Liste représentant le chemin, ou None si pas de chemin
    
    Complexité: O(V + E)
    """

    if target == start : 
        return [start]

    queue : Deque[Tuple[Node , Path]] = deque([(start , [start])])
    visited = set([start])


    while queue : 
        vertex , path = queue.popleft()

        for neighbor in graph[vertex] : 
            if neighbor not in visited : 
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == target : 
                    return new_path 
                queue.append((neighbor , new_path))
    
    return None 


# Task 4 :
"""
Count the max level start with some vertex
""" 
def count_levels(graphe : Graph , start : Node) -> int : 
    """
    Compte le nombre de niveaux depuis start
    
    Complexité: O(V + E)
    """

    if not graph : 
        return 0 
    queue = deque([(start , 0)])
    visited = set([start])
    max_level = 0

    while queue : 
        vertex , level = queue.popleft()
        max_level = max(max_level , level)
        for neighbor in graph[vertex] : 
            if neighbor not in visited : 
                visited.add(neighbor)
                queue.append((neighbor ,level + 1))

    return max_level + 1 



# Task 5 :
"""
BFS in grid as graph 
"""
Grid = List[List[int]]
RowIndex = int 
ColIndex = int 
Distance = int 
Vertex = Tuple[RowIndex , ColIndex , Distance]
def bfs_grid(grid : Grid, start_row : RowIndex, start_col : ColIndex) -> List[Vertex]:
    """
    BFS sur une grille 2D
    
    grid: matrice où 0 = libre, 1 = obstacle
    
    Complexité: O(rows x cols)
    """
    
    # verifiy the grid : 
    if not grid or not grid[0] :
        return []

    rows , cols = len(grid) ,len(grid[0])

    # Vérifier la validité de la case de départ
    if (not (0 <= start_row < rows and 0 <= start_col < cols) or 
        grid[start_row][start_col] == 1):
        return []  

    visited = set([(start_row , start_col)])
    queue = deque([(start_row , start_col , 0)])
    directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)]
    res = []

    while queue :
        row , col , dist = queue.popleft()
        res.append((row , col , dist))

        # forach in neighbors : 
        for dr , dc in directions : 
            new_row , new_col = row + dr , col + dc

            # verify the limites and the bounders : 
            if( 0 <= new_row < rows and 
                0 <= new_col < cols  and 
                grid[new_row][new_col] == 0 and
                (new_row , new_col) not in visited
            ) : 
                visited.add((new_row , new_col))
                queue.append((new_row , new_col , dist + 1))
    
    return res 






if __name__ == "__main__" : 
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }

    grid = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    print(f"BFS result is : {bfs(graph , start=0)}")
    print(f"BFS Levels result is : {bfs_with_levels(graph , start=0)}")
    print(f"the shortest path between Vertex(0) and Vertex(3) is :{bfs_shortest_path(graph, 0, 3)}")  # [0, 1, 3]
    print(f"max level of graph start with Vertex(0) is : {count_levels(graph, 0)}")
    print(f"BFS of grid as graph : {bfs_grid(grid , 0 , 0)}")
