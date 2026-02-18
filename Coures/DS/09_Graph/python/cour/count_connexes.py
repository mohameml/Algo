from typing import Dict, List, Set

Graph = Dict[int, List[int]]


def count_connected_components(graph: Graph) -> int:

    visited = set()

    def dfs(v: int) -> None : 
        visited.add(v)
        for neighbor in graph[v] : 
            if neighbor not in visited : 
                dfs(neighbor)
    
    count = 0 
    for v in graph : 
        if v not in visited : 
            dfs(v)
            count += 1 

    return count 


if __name__ == "__main__": 
    # Test
    graph_disconnected = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: []
    }
    print(count_connected_components(graph_disconnected))  # 3
