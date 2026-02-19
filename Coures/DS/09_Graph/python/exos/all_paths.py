""" 
Exercice 5 : All Paths From Source to Target (LeetCode 797) - Moyen
Énoncé
Étant donné un graphe acyclique dirigé (DAG) de n nœuds numérotés de 0 à n-1, trouvez tous les chemins possibles du nœud 0 au nœud n-1.
Le graphe est donné comme suit : graph[i] est une liste de tous les nœuds que vous pouvez visiter depuis le nœud i.

Input :
graph = [[1,2],[3],[3],[]]

**Visualisation :**
```
0 → 1 → 3
↓       ↑
2 ------+

Output : [[0,1,3], [0,2,3]]

Indices 💡
    <details>
    <summary>Indice 1</summary>
    Utilisez DFS avec backtracking. Maintenez le chemin courant dans une liste.
    </details>
    <details>
    <summary>Indice 2</summary>
    Quand vous atteignez le nœud cible (n-1), ajoutez une copie du chemin à la liste des résultats.
    </details>

"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Trouve tous les chemins du nœud 0 au dernier nœud
        
        Args:
            graph: liste d'adjacence
        
        Returns:
            Liste de tous les chemins
        
        Complexité: O(2^N × N) dans le pire cas
        """
        end = len(graph) - 1
        res = []
        path  = [0]

        def dfs(v : int)  : 

            if v == end : 
                res.append(path[:])
                return 

            for neighbor in graph[v] : 
                path.append(neighbor)
                dfs(neighbor)
                path.pop()

        dfs(0)

        return res 

# Tests
sol = Solution()

graph1 = [[1,2],[3],[3],[]]
print(sol.allPathsSourceTarget(graph1))
# [[0,1,3], [0,2,3]]

graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph2))
# [[0,4], [0,3,4], [0,1,3,4], [0,1,2,3,4], [0,1,4]]

graph3 = [[1],[]]
print(sol.allPathsSourceTarget(graph3))
# [[0,1]]