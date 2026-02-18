""" 
- Étant donné une grille 2D de '1' (terre) et '0' (eau), 
- comptez le nombre d'îles.
- Une île est formée en connectant des terres adjacentes 
- horizontalement ou verticalement (pas en diagonal). 
- Vous pouvez supposer que les quatre bords de la grille sont entourés d'eau.


- Input :
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

- Output attendu : 3  # Il y a 3 îles

- **Visualisation :**

Île 1:      Île 2:      Île 3:
T T . . .   . . . . .   . . . . .
T T . . .   . . . . .   . . . . .
. . . . .   . . T . .   . . . . .
. . . . .   . . . . .   . . . T T

(T = Terre, . = Eau)
"""

from typing import List

Grid = List[List[str]]

def num_islands(grid: Grid) -> int:
    """
    Compte le nombre d'îles dans la grille
    
    Args:
        grid: matrice où '1' = terre, '0' = eau
    
    Returns:
        Nombre d'îles
    
    Complexité: O(rows × cols)
    """
    # TODO: Implémenter
    ... 


# Tests
grid1 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(num_islands(grid1))  # 3

grid2 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(num_islands(grid2))  # 1

grid3 = [
    ['1', '0', '1', '0', '1'],
    ['0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1'],
    ['0', '1', '0', '1', '0']
]
print(num_islands(grid3))  # 10

grid4 = [
    ['0', '0', '0'],
    ['0', '0', '0']
]
print(num_islands(grid4))  # 0

grid5 = [
    ['1', '1', '1'],
    ['1', '1', '1']
]
print(num_islands(grid5))  # 1