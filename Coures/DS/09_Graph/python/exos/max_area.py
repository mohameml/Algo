""" 
Exercice 6 : Max Area of Island (LeetCode 695) - Moyen
Énoncé
Étant donné une grille 2D de 0 (eau) et 1 (terre), trouvez la superficie maximale d'une île. La superficie d'une île est le nombre de cellules avec la valeur 1.
Input :
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output : 6

Indices 💡
<details>
<summary>Indice 1</summary>
Pour chaque cellule 1, lancez un DFS qui compte le nombre de cellules connectées et retourne cette valeur.
</details>
<details>
<summary>Indice 2</summary>
Le DFS doit retourner 1 + sum(aires des voisins).
</details>
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Trouve la superficie maximale d'une île
        
        Args:
            grid: matrice où 1 = terre, 0 = eau
        
        Returns:
            Superficie maximale
        
        Complexité: O(rows × cols)
        """
        # TODO: Implémenter avec DFS
        ... 


# Test
sol = Solution()
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(sol.maxAreaOfIsland(grid))  # 6