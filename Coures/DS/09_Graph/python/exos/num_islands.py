""" 
Leetcode 200 : 

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
    
    Complexité: O(rows x cols)
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for start_row in range(rows): 
        for start_col in range(cols) :
            if grid[start_row][start_col] == '0' : 
                continue 
            
            stack = [(start_row , start_col)]
            while stack  : 
                row , col = stack.pop()
                grid[row][col] = '0'
                for dr , dc in directions : 
                    new_row , new_col = row + dr , col + dc 
                    if(
                        0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == '1' 
                    ) : 
                        stack.append((new_row ,new_col))

            count += 1

    return count 

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

### **Indices** 💡

# <details>
# <summary>Indice 1</summary>

# Pour chaque case `'1'` non visitée, lancez un DFS qui marque toute l'île connectée comme visitée, puis incrémentez le compteur.

# </details>

# <details>
# <summary>Indice 2</summary>

# Vous pouvez modifier directement la grille en changeant `'1'` en `'0'` après visite pour éviter d'utiliser un set `visited`.

# </details>
