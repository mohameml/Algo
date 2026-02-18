from typing import Dict, List, Set

Graph = Dict[int, List[int]]


def has_cycle_undirected(graph: Graph) -> bool:
    """
    Détecte s'il existe un cycle dans un graphe non-dirigé

    Complexité: O(V + E)
    """
    # Idéee clé : 
    # Dans un graphe non orienté :
    # Si tu revisites un sommet déjà visité qui n’est pas ton parent → il y a un cycle


    visited = set()

    def dfs(vertex : int , parent : int) -> bool : 
        visited.add(vertex)

        for neighbor in graph[vertex] : 
            if neighbor not in visited : 
                if dfs(neighbor , vertex) : 
                    return True 
            elif neighbor != parent : 
                return True 
        return False 
    
    # Parcourit tous les composantes connexes : 
    for vertex in graph :
        if vertex not in visited : 
            if dfs(vertex , -1) : 
                return True 
    
    return False

def has_cycle_undirected_iter(graph: Graph) -> bool:

    # Idéee clé : 
    # Dans un graphe non orienté :
    # Si tu revisites un sommet déjà visité qui n’est pas ton parent → il y a un cycle
    visited = set()

    for start in graph :

        if start in visited : 
            continue 
            
        stack = [(start , - 1)] # (vertex id , parent id )

        while stack  : 
            vertex , parent = stack.pop()

            if vertex in visited : 
                continue 
            visited.add(vertex)

            for neighbor in graph[vertex] : 
                if neighbor not in visited : 
                    stack.append((neighbor , vertex))
                elif neighbor != parent : 
                    return True
    
    return False 



def has_cycle_directed(graph: Graph) -> bool:

    WHITE , GRAY , BLACK = 0 , 1 , 2 
    color = {vertex : WHITE for vertex in graph}

    def dfs(vertex : int) -> bool : 
        color[vertex] = GRAY 

        for neighbor in graph[vertex] : 
            
            if color[neighbor] == GRAY : 
                return True
            
            if color[neighbor] == WHITE : 
                res = dfs(neighbor)
                if res : 
                    return True 
        color[vertex] = BLACK
        return False 

    # Parcour tous les composantes connexes 
    for vertex in graph : 
        if color[vertex] == WHITE : 
            res = dfs(vertex)
            if res : 
                return True 
    
    return False 




if __name__ == "__main__" : 

    # Test avec cycle
    graph_with_cycle = {
        0: [1, 2],
        1: [0, 2],  # Triangle 0-1-2 → cycle
        2: [0, 1]
    }
    print(has_cycle_undirected(graph_with_cycle))  # True

    # Test sans cycle (arbre)
    tree = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }
    print(has_cycle_undirected(tree))  # False

    # Edge test : 
    graph = {
        0: [1, 2],
        1: [0],
        2: [0, 3, 4],
        3: [2, 4],
        4: [2, 3]
    }
    print(has_cycle_undirected(graph)) 

    # Test avec cycle
    dag_with_cycle = {
        0: [1],
        1: [2],
        2: [0]  # Cycle : 0 → 1 → 2 → 0
    }
    print(has_cycle_directed(dag_with_cycle))  # True

    # Test sans cycle (DAG)
    dag = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    print(has_cycle_directed(dag))  # False
