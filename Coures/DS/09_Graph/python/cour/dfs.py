from typing import Dict, List, Set

Graph = Dict[int, List[int]]

def dfs_recursive(graph: Graph, start: int) -> List[int]:

    visited = set()
    res = []

    def dfs(vertex : int) : 
        visited.add(vertex)
        res.append(vertex)

        for neighbor in graph[vertex] : 
            if neighbor not in visited : 
                dfs(neighbor)

    dfs(start)
    return res 


def dfs_iterative(graph: Graph, start: int) -> List[int]:

    visited = set([start])
    stack = [start]
    res = []

    while stack : 
        vertex = stack.pop()
        res.append(vertex)

        for neighbor in reversed(graph[vertex]) : 
            if neighbor not in visited :
                visited.add(neighbor) 
                stack.append(neighbor)

    return res 


Grid = List[List[int]]

def dfs_grid_iterative(grid: Grid, start_row: int, start_col: int) -> List[tuple]:
    """
    DFS itératif sur une grille 2D

    Complexité: O(rows x cols)
    """
    rows , cols = len(grid) , len(grid[0])
    visited = set([(start_row , start_col)])
    res = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    stack = [(start_row , start_col)]

    while stack : 
        row  , col = stack.pop()
        res.append((row , col))

        for dr , dc in directions : 
            new_row , new_col = row + dr ,col  + dc 
            if (
                0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 0 and 
                (new_row , new_col) not in visited 
            ): 
                stack.append((new_row , new_col))
                visited.add((new_row, new_col))

    
    return res 



if __name__ == "__main__" : 

    # Exemple d'utilisation
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }

    print(dfs_recursive(graph, 0))
    # [0, 1, 3, 4, 5, 2]

    print(dfs_iterative(graph, 0))
    # [0, 1, 3, 4, 5, 2]

    grid = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    print("DFS itératif:", dfs_grid_iterative(grid, 0, 0))
    # print("DFS récursif:", dfs_grid_recursive(grid, 0, 0))
    # print("DFS itératif V2:", dfs_grid_iterative_v2(grid, 0, 0))

