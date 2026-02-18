from typing import Dict, List, Set

Graph = Dict[int, List[int]]

def find_all_paths(graph: Graph, start: int, end: int) -> List[List[int]]:
    
    all_paths = []

    def dfs(vertex : int , path : List[int])  : 
        path.append(vertex)

        if vertex == end : 
            all_paths.append(path.copy())
        else : 

            for neighbor in graph[vertex]: 
                if neighbor not in path : 
                    dfs(neighbor , path)

        # Back track : to explore the another posssible path 
        path.pop()

    dfs(start , [])

    return all_paths 

def find_all_paths_iter(graph: Graph, start: int, end: int) -> List[List[int]]:

    stack = [(start , [])]
    all_paths = []

    while stack : 
        vertex , path = stack.pop()
        path.append(vertex) 

        if vertex == end : 
            all_paths.append(path.copy())
        else :     
            for neighbor in graph[vertex] : 
                if neighbor not in path : 
                    stack.append((neighbor , path.copy()))
            
    return all_paths


if __name__ == "__main__" : 

    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    print(find_all_paths(graph, 0, 3))
    # [[0, 1, 3], [0, 2, 3]]
    print(find_all_paths_iter(graph,0,3))
