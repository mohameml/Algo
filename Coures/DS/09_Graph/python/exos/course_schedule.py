""" 
Exercice 4 : Course Schedule (LeetCode 207) - Moyen
Énoncé
Il y a un total de numCourses cours que vous devez suivre, numérotés de 0 à numCourses - 1.
Certains cours ont des prérequis. Par exemple, pour suivre le cours 0, vous devez d'abord avoir terminé le cours 1, exprimé comme [0, 1].
Étant donné le nombre total de cours et une liste de paires de prérequis, déterminez s'il est possible de terminer tous les cours.

Input 1 : 
    numCourses = 2
    prerequisites = [[1,0]]
Output : true
Explication : Il y a 2 cours. Pour suivre le cours 1, vous devez avoir terminé le cours 0. C'est possible.


Input 2 : 
    numCourses = 2
    prerequisites = [[1,0],[0,1]]

Output : false
Explication : Cycle : cours 0 nécessite cours 1, et cours 1 nécessite cours 0. Impossible !

"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Vérifie s'il est possible de terminer tous les cours
        (détection de cycle dans un graphe dirigé)
        
        Args:
            numCourses: nombre de cours
            prerequisites: liste de paires [cours, prérequis]
        
        Returns:
            True si possible, False sinon
        
        Complexité: O(V + E)
        """
        graph = {node : [] for node in range(numCourses)}
        for preq in prerequisites : 
            graph[preq[0]].append(preq[1])

        WHITE , GRAY , BLACK = 0 , 1 , 2 
        colors = {v : WHITE for v in graph}


        def dfs(vertex : int) -> bool : 
            """return True if no cycle detected"""
            colors[vertex] = GRAY 

            for nei in graph[vertex] : 
                if colors[nei] == GRAY : 
                    return False
                
                if colors[nei] == WHITE : 
                    if not dfs(nei) : 
                        return False  
            
            colors[vertex] = BLACK 
            return True  

        for v in graph : 
            if colors[v] == WHITE : 
                if not dfs(v) : 
                    return False 

        return True 
        


# Tests
sol = Solution()

print(sol.canFinish(2, [[1,0]]))  # True
print(sol.canFinish(2, [[1,0],[0,1]]))  # False
print(sol.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))  # True
print(sol.canFinish(3, [[0,1],[1,2],[2,0]]))  # False (cycle)

# Indices 💡
# <details>
# <summary>Indice 1</summary>
# Ce problème est équivalent à détecter un cycle dans un graphe dirigé.
# </details>
# <details>
# <summary>Indice 2</summary>
# Utilisez la méthode des 3 couleurs (White-Gray-Black) :

# White (0) : Non visité
# Gray (1) : En cours de visite
# Black (2) : Complètement visité

# Si vous rencontrez un nœud Gray pendant DFS, il y a un cycle.
# </details>
