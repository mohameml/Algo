# Module 2 : Parcours de Graphes

## **Introduction**

Les **parcours de graphes** sont les algorithmes les plus fondamentaux et les plus importants. Ils permettent d'explorer tous les sommets et arêtes d'un graphe de manière systématique.

Il existe **deux approches principales** :

1. **BFS (Breadth-First Search)** - Parcours en largeur
2. **DFS (Depth-First Search)** - Parcours en profondeur

Ces deux algorithmes sont la **base** de nombreux autres algorithmes de graphes.

---

# **1. Breadth-First Search (BFS)**

## **Principe**

BFS explore le graphe **niveau par niveau**, comme des **ondes qui se propagent** :

- D'abord tous les voisins directs (distance 1)
- Puis tous les voisins de voisins (distance 2)
- Et ainsi de suite...

**Analogie** : Imaginez que vous lancez une pierre dans l'eau. Les cercles concentriques qui se forment représentent les niveaux explorés par BFS.

---

## **Visualisation**

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

---

## **Algorithme**

**Idée clé** : Utiliser une **file (queue)** pour maintenir l'ordre FIFO (First In, First Out)

**Étapes** :

1. Commencer avec le sommet de départ dans la queue
2. Marquer ce sommet comme visité
3. Tant que la queue n'est pas vide :
    - Retirer le premier sommet de la queue
    - Explorer tous ses voisins non visités
    - Marquer chaque voisin comme visité et l'ajouter à la queue

---

## **Implémentation en Python**

### **Version de base**

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

---

### **Version avec niveaux (distance)**

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

---

### **Version avec chemin (shortest path)**

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

---

### **Version optimisée avec parent tracking**

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

---

## **Propriétés de BFS**

| Propriété                | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Plus court chemin**    | ✅ Trouve le plus court chemin (en nombre d'arêtes) dans un graphe **non-pondéré** |
| **Ordre de visite**      | Par niveaux (distances croissantes)                                                |
| **Structure de données** | **Queue (FIFO)**                                                                   |
| **Complétude**           | ✅ Visite tous les sommets accessibles                                             |
| **Optimalité**           | ✅ Pour graphes non-pondérés                                                       |

---

## **Applications de BFS**

1. **Plus court chemin** (graphes non-pondérés)
2. **Niveau de nœuds** dans un arbre
3. **Composantes connexes**
4. **Détection de cycles**
5. **Test de bipartition**
6. **Problèmes de grille** (labyrinthes, îles)
7. **Graphes de jeux** (états, mouvements)

---

## **Analyse de complexité**

### **Complexité temporelle : O(V + E)**

**Pourquoi ?**

- Chaque sommet est visité **exactement une fois** → O(V)
- Chaque arête est explorée **exactement une fois** (ou deux fois si non-dirigé) → O(E)
- Total : **O(V + E)**

### **Complexité spatiale : O(V)**

**Pourquoi ?**

- `visited` : O(V)
- `queue` : O(V) dans le pire cas (tous les sommets d'un niveau)
- `parent`/`distances` : O(V)
- Total : **O(V)**

---

## **Exemples pratiques**

### **Exemple 1 : Compter les niveaux**

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

---

### **Exemple 2 : BFS sur une grille (matrice)**

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

---

## **BFS vs autres algorithmes**

| Critère           | BFS                     | DFS               |
| ----------------- | ----------------------- | ----------------- |
| Structure         | Queue (FIFO)            | Stack (LIFO)      |
| Ordre             | Par niveaux             | Par profondeur    |
| Plus court chemin | ✅ Oui (non-pondéré)    | ❌ Non            |
| Mémoire           | O(largeur max)          | O(profondeur max) |
| Usage             | Chemins courts, niveaux | Cycles, topologie |

---

## **Résumé BFS**

✅ **Queue (FIFO)** pour explorer niveau par niveau  
✅ **O(V + E)** en temps, **O(V)** en espace  
✅ **Plus court chemin** pour graphes non-pondérés  
✅ Applications : chemins, niveaux, composantes, grilles
