"""
# Exercice 1 : BFS - Plus court chemin dans un graphe

>Énoncé

Étant donné un graphe non-dirigé représenté par 
une liste d'adjacence et deux sommets start et end, 
trouvez le plus court chemin entre ces deux sommets.

- Input :
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}
start = 0
end = 5
Output attendu :
[0, 2, 5]  # Le plus court chemin de 0 à 5
"""

from typing import Dict, List, Optional

Graph = Dict[int, List[int]]

def shortest_path_bfs(graph: Graph, start: int, end: int) -> Optional[List[int]]:
    """
    Trouve le plus court chemin entre start et end en utilisant BFS
    
    Args:
        graph: dictionnaire {sommet: [voisins]}
        start: sommet de départ
        end: sommet d'arrivée
    
    Returns:
        Liste représentant le chemin, ou None si pas de chemin
    
    Complexité: O(V + E)
    """
    # TODO: Implémenter1
    pass


# Tests
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

print(shortest_path_bfs(graph, 0, 5))  # [0, 2, 5]
print(shortest_path_bfs(graph, 0, 3))  # [0, 1, 3]
print(shortest_path_bfs(graph, 3, 5))  # [3, 1, 4, 5] ou [3, 1, 0, 2, 5]
print(shortest_path_bfs(graph, 0, 0))  # [0]