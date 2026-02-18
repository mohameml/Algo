# Module 2 : Parcours de Graphes

## 1. **Introduction**

Les **parcours de graphes** sont les algorithmes les plus fondamentaux et les plus importants. Ils permettent d'explorer tous les sommets et arêtes d'un graphe de manière systématique.

Il existe **deux approches principales** :

1. **BFS (Breadth-First Search)** - Parcours en largeur
2. **DFS (Depth-First Search)** - Parcours en profondeur

Ces deux algorithmes sont la **base** de nombreux autres algorithmes de graphes.

## **2. Breadth-First Search (BFS)**

### **Principe**

BFS explore le graphe **niveau par niveau**, comme des **ondes qui se propagent** :

- D'abord tous les voisins directs (distance 1)
- Puis tous les voisins de voisins (distance 2)
- Et ainsi de suite...

**Analogie** : Imaginez que vous lancez une pierre dans l'eau. Les cercles concentriques qui se forment représentent les niveaux explorés par BFS.

### **Visualisation**

```
Graphe :
    0 --- 1 --- 3
    |     |
    2 --- 4

BFS depuis 0 :
Niveau 0 : [0]
Niveau 1 : [1, 2]         (voisins de 0)
Niveau 2 : [3, 4]         (voisins de 1 et 2)

Ordre de visite : 0 → 1 → 2 → 3 → 4
```

### **Algorithme**

**Idée clé** : Utiliser une **file (queue)** pour maintenir l'ordre FIFO (First In, First Out)

**Étapes** :

1. Commencer avec le sommet de départ dans la queue
2. Marquer ce sommet comme visité
3. Tant que la queue n'est pas vide :
    - Retirer le premier sommet de la queue
    - Explorer tous ses voisins non visités
    - Marquer chaque voisin comme visité et l'ajouter à la queue

### **Implémentation en Python**

#### **Version de base**

```python
from collections import deque

def bfs(graph, start):
    """
    Parcours BFS depuis un sommet de départ

    Args:
        graph: dict {sommet: [voisins]}
        start: sommet de départ

    Returns:
        Liste des sommets dans l'ordre de visite

    Complexité: O(V + E)
    """
    visited = set()           # Ensemble des sommets visités
    queue = deque([start])    # File pour gérer l'ordre de visite
    visited.add(start)
    result = []               # Ordre de visite

    while queue:
        vertex = queue.popleft()  # FIFO: retirer le premier
        result.append(vertex)

        # Explorer tous les voisins
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Exemple d'utilisation
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(bfs(graph, 0))  # [0, 1, 2, 3, 4]
```

#### **Version avec niveaux (distance)**

```python
def bfs_with_levels(graph, start):
    """
    BFS qui calcule aussi la distance de chaque sommet

    Returns:
        dict {sommet: distance_depuis_start}

    Complexité: O(V + E)
    """
    visited = set([start])
    queue = deque([(start, 0)])  # (sommet, distance)
    distances = {start: 0}

    while queue:
        vertex, dist = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))

    return distances


# Exemple
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(bfs_with_levels(graph, 0))
# {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
```

#### **Version avec chemin (shortest path)**

```python
def bfs_shortest_path(graph, start, target):
    """
    Trouve le plus court chemin entre start et target

    Returns:
        Liste représentant le chemin, ou None si pas de chemin

    Complexité: O(V + E)
    """
    if start == target:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])  # (sommet, chemin_actuel)

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]

                if neighbor == target:
                    return new_path

                queue.append((neighbor, new_path))

    return None  # Pas de chemin trouvé


# Exemple
print(bfs_shortest_path(graph, 0, 3))  # [0, 1, 3]
```

#### **Version optimisée avec parent tracking**

```python
def bfs_shortest_path_optimized(graph, start, target):
    """
    Version plus efficace en mémoire avec tracking des parents

    Complexité: O(V + E)
    Espace: O(V) au lieu de O(V²)
    """
    if start == target:
        return [start]

    visited = set([start])
    queue = deque([start])
    parent = {start: None}  # Pour reconstruire le chemin

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)

                if neighbor == target:
                    # Reconstruire le chemin
                    path = []
                    current = target
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    return path[::-1]  # Inverser

    return None


# Exemple
print(bfs_shortest_path_optimized(graph, 0, 3))  # [0, 1, 3]
```

### **Propriétés de BFS**

| Propriété                | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Plus court chemin**    | ✅ Trouve le plus court chemin (en nombre d'arêtes) dans un graphe **non-pondéré** |
| **Ordre de visite**      | Par niveaux (distances croissantes)                                                |
| **Structure de données** | **Queue (FIFO)**                                                                   |
| **Complétude**           | ✅ Visite tous les sommets accessibles                                             |
| **Optimalité**           | ✅ Pour graphes non-pondérés                                                       |

### **Applications de BFS**

1. **Plus court chemin** (graphes non-pondérés)
2. **Niveau de nœuds** dans un arbre
3. **Composantes connexes**
4. **Détection de cycles**
5. **Test de bipartition**
6. **Problèmes de grille** (labyrinthes, îles)
7. **Graphes de jeux** (états, mouvements)

### **Analyse de complexité**

#### **Complexité temporelle : O(V + E)**

**Pourquoi ?**

- Chaque sommet est visité **exactement une fois** → O(V)
- Chaque arête est explorée **exactement une fois** (ou deux fois si non-dirigé) → O(E)
- Total : **O(V + E)**

#### **Complexité spatiale : O(V)**

**Pourquoi ?**

- `visited` : O(V)
- `queue` : O(V) dans le pire cas (tous les sommets d'un niveau)
- `parent`/`distances` : O(V)
- Total : **O(V)**

### **Exemples pratiques**

#### **Exemple 1 : Compter les niveaux**

```python
def count_levels(graph, start):
    """
    Compte le nombre de niveaux depuis start

    Complexité: O(V + E)
    """
    if not graph:
        return 0

    visited = set([start])
    queue = deque([(start, 0)])
    max_level = 0

    while queue:
        vertex, level = queue.popleft()
        max_level = max(max_level, level)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return max_level + 1


# Test
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print(count_levels(graph, 0))  # 3 niveaux
```

#### **Exemple 2 : BFS sur une grille (matrice)**

```python
def bfs_grid(grid, start_row, start_col):
    """
    BFS sur une grille 2D

    grid: matrice où 0 = libre, 1 = obstacle

    Complexité: O(rows × cols)
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited.add((start_row, start_col))

    # Directions: haut, bas, gauche, droite
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = []

    while queue:
        row, col, dist = queue.popleft()
        result.append((row, col, dist))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Vérifier les limites et obstacles
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return result


# Test
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

print(bfs_grid(grid, 0, 0))
# [(0, 0, 0), (0, 1, 1), (1, 0, 1), (2, 0, 2), (2, 1, 2), ...]
```

## **3. DFS :**

### **Qu'est-ce que DFS ?**

> DFS (Depth-First Search) explore le graphe **en profondeur** avant d'explorer en largeur. C'est comme explorer un labyrinthe en allant **aussi loin que possible** dans une direction avant de faire demi-tour.

### **Visualisation : BFS vs DFS**

```
Graphe :
       1
      / \
     2   3
    / \   \
   4   5   6

BFS depuis 1 :
Niveau 0 : [1]
Niveau 1 : [2, 3]
Niveau 2 : [4, 5, 6]
Ordre : 1 → 2 → 3 → 4 → 5 → 6

DFS depuis 1 :
Profondeur d'abord !
Ordre : 1 → 2 → 4 → 5 → 3 → 6
(va jusqu'au bout du chemin gauche, puis revient)
```

---

### **Différence clé : BFS vs DFS**

| Aspect          | BFS          | DFS            |
| --------------- | ------------ | -------------- |
| **Structure**   | Queue (FIFO) | Stack (LIFO)   |
| **Exploration** | Par niveaux  | Par profondeur |
| **Ordre**       | Horizontal   | Vertical       |
| **Mémoire**     | O(largeur)   | O(profondeur)  |

### **Algorithme DFS**

> **Idée clé**

Utiliser une **pile (stack)** pour maintenir l'ordre LIFO (Last In, First Out).

**Deux approches :**

1. **Récursive** (utilise la pile d'appels système)
2. **Itérative** (utilise une pile explicite)

- **Étapes (récursif) :**
    1. Marquer le sommet actuel comme visité
    2. Pour chaque voisin non visité :
        - Appeler récursivement DFS sur ce voisin

- **Étapes (itératif) :**
    1. Mettre le sommet de départ dans la pile
    2. Tant que la pile n'est pas vide :
        - Dépiler un sommet
        - Si non visité, le marquer comme visité
        - Empiler tous ses voisins non visités

### **Implémentation DFS**

#### **A. Version récursive (la plus simple)**

```python
from typing import Dict, List, Set

Graph = Dict[int, List[int]]

def dfs_recursive(graph: Graph, start: int) -> List[int]:
    """
    DFS récursif - parcourt le graphe en profondeur

    Args:
        graph: dictionnaire {sommet: [voisins]}
        start: sommet de départ

    Returns:
        Liste des sommets dans l'ordre de visite DFS

    Complexité:
        Temps: O(V + E)
        Espace: O(V) pour visited + O(profondeur) pour la pile de récursion
    """
    visited = set()
    result = []

    def dfs(vertex: int) -> None:
        # Marquer comme visité
        visited.add(vertex)
        result.append(vertex)

        # Explorer tous les voisins
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)  # Appel récursif

    dfs(start)
    return result


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
```

**Trace d'exécution :**

```
dfs(0)
├─ visiter 0
├─ dfs(1)
│  ├─ visiter 1
│  ├─ dfs(3)
│  │  └─ visiter 3 (pas de voisins non visités)
│  └─ dfs(4)
│     ├─ visiter 4
│     └─ dfs(5)
│        └─ visiter 5
└─ dfs(2)
   └─ visiter 2 (déjà exploré via 5)

Ordre final : 0 → 1 → 3 → 4 → 5 → 2
```

---

#### **B. Version itérative (avec stack explicite)**

```python
from collections import deque

def dfs_iterative(graph: Graph, start: int) -> List[int]:
    """
    DFS itératif - utilise une stack explicite

    Args:
        graph: dictionnaire {sommet: [voisins]}
        start: sommet de départ

    Returns:
        Liste des sommets dans l'ordre de visite DFS

    Complexité:
        Temps: O(V + E)
        Espace: O(V)
    """
    visited = set()
    stack = [start]  # Utiliser une liste comme pile
    result = []

    while stack:
        vertex = stack.pop()  # LIFO: retirer le dernier

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Ajouter les voisins à la pile (dans l'ordre inverse pour garder l'ordre)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# Test
print(dfs_iterative(graph, 0))
# [0, 1, 3, 4, 5, 2]
```

**Trace d'exécution :**

```
Stack:     [0]
Pop 0      → visited={0}, result=[0], stack=[2, 1]

Stack:     [2, 1]
Pop 1      → visited={0,1}, result=[0,1], stack=[2, 4, 3]

Stack:     [2, 4, 3]
Pop 3      → visited={0,1,3}, result=[0,1,3], stack=[2, 4]

Stack:     [2, 4]
Pop 4      → visited={0,1,3,4}, result=[0,1,3,4], stack=[2, 5]

Stack:     [2, 5]
Pop 5      → visited={0,1,3,4,5}, result=[0,1,3,4,5], stack=[2]

Stack:     [2]
Pop 2      → visited={0,1,3,4,5,2}, result=[0,1,3,4,5,2], stack=[]

Résultat : [0, 1, 3, 4, 5, 2]
```

---

### **Applications de DFS**

#### **Application 1 : Détection de cycle (graphe non-dirigé)**

```python
def has_cycle_undirected(graph: Graph) -> bool:
    """
    Détecte s'il existe un cycle dans un graphe non-dirigé

    Complexité: O(V + E)
    """
    visited = set()

    def dfs(vertex: int, parent: int) -> bool:
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # On a trouvé un voisin déjà visité qui n'est pas le parent
                # → Cycle détecté !
                return True

        return False

    # Vérifier toutes les composantes connexes
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, -1):
                return True

    return False


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
```

**Explication :**

```
Graphe avec cycle :       Graphe sans cycle (arbre) :
    0 --- 1                   0 --- 1
    |     |                   |     |
    +-----2                   2     3

Cycle : 0 → 1 → 2 → 0        Pas de cycle
```

---

#### **Application 2 : Détection de cycle (graphe dirigé)**

```python
def has_cycle_directed(graph: Graph) -> bool:
    """
    Détecte s'il existe un cycle dans un graphe dirigé
    Utilise la méthode des couleurs (White-Gray-Black)

    White (0) : Non visité
    Gray  (1) : En cours de visite (dans la pile de récursion)
    Black (2) : Complètement visité

    Complexité: O(V + E)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}

    def dfs(vertex: int) -> bool:
        color[vertex] = GRAY  # Marquer comme "en cours"

        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:
                # Retour sur un sommet "en cours" → cycle !
                return True

            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        color[vertex] = BLACK  # Marquer comme "terminé"
        return False

    # Vérifier tous les sommets
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False


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
```

**Visualisation :**

```
Avec cycle :          Sans cycle (DAG) :
    0 → 1                 0 → 1
    ↑   ↓                 ↓   ↓
    2 ←─┘                 2 → 3
```

#### **Application 3 : Composantes connexes**

```python
def count_connected_components(graph: Graph) -> int:
    """
    Compte le nombre de composantes connexes

    Complexité: O(V + E)
    """
    visited = set()
    count = 0

    def dfs(vertex: int) -> None:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    # Explorer chaque composante
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            count += 1  # Nouvelle composante trouvée

    return count


# Test
graph_disconnected = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}
print(count_connected_components(graph_disconnected))  # 3

# Visualisation :
# Composante 1: 0 -- 1
# Composante 2: 2 -- 3
# Composante 3: 4
```

#### **Application 4 : Trouver tous les chemins**

```python
def find_all_paths(graph: Graph, start: int, end: int) -> List[List[int]]:
    """
    Trouve tous les chemins possibles entre start et end

    Complexité: O(V! × V) dans le pire cas (graphe complet)
    """
    all_paths = []

    def dfs(vertex: int, path: List[int]) -> None:
        # Ajouter le sommet actuel au chemin
        path.append(vertex)

        # Si on a atteint la destination
        if vertex == end:
            all_paths.append(path.copy())  # Copier le chemin
        else:
            # Explorer les voisins
            for neighbor in graph[vertex]:
                if neighbor not in path:  # Éviter les cycles
                    dfs(neighbor, path)

        # Backtrack : retirer le sommet pour essayer d'autres chemins
        path.pop()

    dfs(start, [])
    return all_paths


# Test
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(find_all_paths(graph, 0, 3))
# [[0, 1, 3], [0, 2, 3]]
```

---

### **DFS sur grille**

```python
from collections import deque
from typing import List

Grid = List[List[int]]

def dfs_grid_recursive(grid: Grid, start_row: int, start_col: int) -> List[tuple]:
    """
    DFS récursif sur une grille 2D

    Complexité: O(rows × cols)
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    result = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row: int, col: int) -> None:
        # Marquer comme visité
        visited.add((row, col))
        result.append((row, col))

        # Explorer les 4 voisins
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):

                dfs(new_row, new_col)

    dfs(start_row, start_col)
    return result


def dfs_grid_iterative(grid: Grid, start_row: int, start_col: int) -> List[tuple]:
    """
    DFS itératif sur une grille 2D

    Complexité: O(rows × cols)
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_row, start_col)]
    result = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        row, col = stack.pop()

        if (row, col) not in visited:
            visited.add((row, col))
            result.append((row, col))

            # Ajouter les voisins
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] == 0 and
                    (new_row, new_col) not in visited):

                    stack.append((new_row, new_col))

    return result


# Test
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

print("DFS récursif:", dfs_grid_recursive(grid, 0, 0))
print("DFS itératif:", dfs_grid_iterative(grid, 0, 0))
```

### **Analyse de complexité**

#### **Complexité temporelle : O(V + E)**

**Pourquoi ?**

- Chaque sommet est visité **exactement une fois** → O(V)
- Chaque arête est explorée **exactement une fois** (ou deux fois si non-dirigé) → O(E)
- Total : **O(V + E)**

#### **Complexité spatiale**

| Version      | Espace                                                                        |
| ------------ | ----------------------------------------------------------------------------- |
| **Récursif** | O(V) pour `visited` + O(h) pour la pile de récursion (h = hauteur/profondeur) |
| **Itératif** | O(V) pour `visited` + O(V) pour la stack                                      |
| **Total**    | **O(V)** en moyenne                                                           |

**Pire cas (récursif) :** O(V) si le graphe est une longue chaîne (risque de stack overflow).

## **4. Comparaison finale : BFS vs DFS**

| Critère                  | BFS                     | DFS                             |
| ------------------------ | ----------------------- | ------------------------------- |
| **Structure**            | Queue (FIFO)            | Stack (LIFO)                    |
| **Ordre**                | Par niveaux             | Par profondeur                  |
| **Plus court chemin**    | ✅ Oui (non-pondéré)    | ❌ Non                          |
| **Détection de cycles**  | ✅ Possible             | ✅ Plus naturel                 |
| **Composantes connexes** | ✅ Oui                  | ✅ Oui                          |
| **Mémoire**              | O(largeur)              | O(profondeur)                   |
| **Implémentation**       | Itérative               | Récursive ou itérative          |
| **Usage typique**        | Chemins courts, niveaux | Cycles, backtracking, topologie |
