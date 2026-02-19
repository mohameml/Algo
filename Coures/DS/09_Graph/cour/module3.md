# Module 3 : Problèmes classiques de parcours

# **1. Détection de cycles**

## **A. Cycle dans un graphe non-dirigé**

### **Principe**

> Dans un graphe **non-dirigé**, un cycle existe si pendant le DFS, on rencontre un sommet **déjà visité** qui n'est **pas le parent** du sommet actuel.

**Intuition :**

```
Graphe avec cycle :        Sans cycle (arbre) :
    0 --- 1                   0 --- 1
    |     |                   |     |
    2 ----+                   2     3

Pendant DFS depuis 0 :     Pendant DFS depuis 0 :
0 → 1 → 2 → 0 (cycle!)    0 → 1 → 3 ✓
                          0 → 2 ✓
```

### **Algorithme**

```python
from typing import Dict, List, Set

Graph = Dict[int, List[int]]

def has_cycle_undirected(graph: Graph) -> bool:
    """
    Détecte un cycle dans un graphe non-dirigé

    Méthode: DFS avec tracking du parent

    Args:
        graph: graphe non-dirigé sous forme de liste d'adjacence

    Returns:
        True si un cycle existe, False sinon

    Complexité: O(V + E)
    """
    visited = set()

    def dfs(vertex: int, parent: int) -> bool:
        """
        DFS récursif

        Args:
            vertex: sommet actuel
            parent: sommet parent (d'où on vient)

        Returns:
            True si cycle détecté
        """
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Explorer le voisin
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                # Voisin déjà visité ET ce n'est pas le parent
                # → On a trouvé un cycle !
                return True

        return False

    # Vérifier toutes les composantes connexes
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, -1):  # -1 = pas de parent initial
                return True

    return False


# Tests
print("=== Graphe non-dirigé - Détection de cycle ===\n")

# Test 1: Avec cycle
graph1 = {
    0: [1, 2],
    1: [0, 2],  # Triangle 0-1-2 → cycle
    2: [0, 1]
}
print(f"Graph1 (triangle): {has_cycle_undirected(graph1)}")  # True

# Test 2: Sans cycle (arbre)
graph2 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
print(f"Graph2 (arbre): {has_cycle_undirected(graph2)}")  # False

# Test 3: Graphe déconnecté avec cycle dans une composante
graph3 = {
    0: [1],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3]
}
print(f"Graph3 (déconnecté, cycle dans composante 2): {has_cycle_undirected(graph3)}")  # True

# Test 4: Un seul sommet
graph4 = {0: []}
print(f"Graph4 (1 sommet): {has_cycle_undirected(graph4)}")  # False
```

## **B. Cycle dans un graphe dirigé**

### **Principe**

Dans un graphe **dirigé**, on utilise la méthode des **3 couleurs** :

- **WHITE (0)** : Non visité
- **GRAY (1)** : En cours de visite (dans la pile de récursion actuelle)
- **BLACK (2)** : Complètement visité (tous ses descendants explorés)

> **Règle :** Si on rencontre un sommet **GRAY** pendant le DFS, il y a un cycle !

### **Algorithme**

```python
def has_cycle_directed(graph: Graph) -> bool:
    """
    Détecte un cycle dans un graphe dirigé

    Méthode: DFS avec 3 couleurs (White-Gray-Black)

    WHITE (0): Non visité
    GRAY  (1): En cours de visite (dans la pile de récursion)
    BLACK (2): Complètement visité

    Args:
        graph: graphe dirigé sous forme de liste d'adjacence

    Returns:
        True si un cycle existe, False sinon

    Complexité: O(V + E)
    """
    WHITE, GRAY, BLACK = 0, 1, 2

    # Initialiser tous les sommets à WHITE
    color = {vertex: WHITE for vertex in graph}

    def dfs(vertex: int) -> bool:
        """
        DFS avec détection de cycle

        Returns:
            True si cycle détecté
        """
        # Marquer comme "en cours"
        color[vertex] = GRAY

        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:
                # Retour sur un sommet "en cours" → cycle !
                return True

            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        # Marquer comme "terminé"
        color[vertex] = BLACK
        return False

    # Vérifier tous les sommets
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False


# Tests
print("\n=== Graphe dirigé - Détection de cycle ===\n")

# Test 1: Avec cycle
graph1 = {
    0: [1],
    1: [2],
    2: [0]  # Cycle : 0 → 1 → 2 → 0
}
print(f"Graph1 (cycle 0→1→2→0): {has_cycle_directed(graph1)}")  # True

# Test 2: Sans cycle (DAG)
graph2 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(f"Graph2 (DAG): {has_cycle_directed(graph2)}")  # False

# Test 3: Self-loop
graph3 = {
    0: [0]  # Boucle sur soi-même
}
print(f"Graph3 (self-loop): {has_cycle_directed(graph3)}")  # True

# Test 4: Multiple composantes, une avec cycle
graph4 = {
    0: [1],
    1: [],
    2: [3],
    3: [4],
    4: [2]  # Cycle : 2 → 3 → 4 → 2
}
print(f"Graph4 (cycle dans composante 2): {has_cycle_directed(graph4)}")  # True
```

## **C. Trouver le cycle (pas seulement le détecter)**

```python
def find_cycle_directed(graph: Graph) -> List[int]:
    """
    Trouve un cycle dans un graphe dirigé (s'il existe)

    Returns:
        Liste représentant le cycle, ou [] si pas de cycle

    Complexité: O(V + E)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}
    parent = {}
    cycle = []

    def dfs(vertex: int) -> bool:
        color[vertex] = GRAY

        for neighbor in graph[vertex]:
            parent[neighbor] = vertex

            if color[neighbor] == GRAY:
                # Cycle trouvé ! Reconstruire le cycle
                cycle.append(neighbor)
                current = vertex
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.reverse()
                return True

            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        color[vertex] = BLACK
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return cycle

    return []


# Test
graph_cycle = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]  # Cycle : 1 → 2 → 3 → 1
}
print(f"\nCycle trouvé: {find_cycle_directed(graph_cycle)}")
# [1, 2, 3, 1]
```

# **2. Composantes connexes**

## **Définition**

Une **composante connexe** est un sous-ensemble maximal de sommets tel qu'il existe un chemin entre toute paire de sommets.

**Exemple :**

```
Graphe :
0 --- 1    3 --- 4    6
|                |
2                5

3 composantes connexes:
1. {0, 1, 2}
2. {3, 4, 5}
3. {6}
```

---

## **A. Compter les composantes connexes**

```python
def count_connected_components(graph: Graph) -> int:
    """
    Compte le nombre de composantes connexes

    Args:
        graph: graphe non-dirigé

    Returns:
        Nombre de composantes connexes

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
            count += 1

    return count


# Tests
print("\n=== Composantes connexes ===\n")

# Test 1: 3 composantes
graph1 = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4, 5],
    4: [3],
    5: [3],
    6: []
}
print(f"Graph1 (3 composantes): {count_connected_components(graph1)}")  # 3

# Test 2: Tout connecté
graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print(f"Graph2 (1 composante): {count_connected_components(graph2)}")  # 1

# Test 3: Tous isolés
graph3 = {
    0: [],
    1: [],
    2: [],
    3: []
}
print(f"Graph3 (4 composantes isolées): {count_connected_components(graph3)}")  # 4
```

---

## **B. Trouver toutes les composantes connexes**

```python
def find_connected_components(graph: Graph) -> List[List[int]]:
    """
    Trouve toutes les composantes connexes

    Returns:
        Liste de composantes (chaque composante = liste de sommets)

    Complexité: O(V + E)
    """
    visited = set()
    components = []

    def dfs(vertex: int, component: List[int]) -> None:
        visited.add(vertex)
        component.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)

    return components


# Test
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}
components = find_connected_components(graph)
print(f"\nComposantes trouvées: {components}")
# [[0, 1, 2], [3, 4], [5]]
```

---

## **C. Vérifier si deux sommets sont dans la même composante**

```python
def same_component(graph: Graph, u: int, v: int) -> bool:
    """
    Vérifie si deux sommets sont dans la même composante connexe

    Complexité: O(V + E)
    """
    if u not in graph or v not in graph:
        return False

    visited = set()

    def dfs(vertex: int) -> bool:
        if vertex == v:
            return True

        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(u)


# Test
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3]
}
print(f"\n0 et 2 même composante? {same_component(graph, 0, 2)}")  # True
print(f"0 et 3 même composante? {same_component(graph, 0, 3)}")  # False
```

---

# **3. Tri topologique (Topological Sort)**

## **Définition**

Le **tri topologique** d'un graphe dirigé acyclique (DAG) est un **ordonnancement linéaire** des sommets tel que pour chaque arête dirigée `u → v`, `u` apparaît avant `v` dans l'ordre.

**Application typique :** Ordonnancement de tâches avec dépendances.

**Exemple :**

```
Tâches (cours) :
    0 → 1 → 3
    ↓       ↑
    2 ------+

Ordre topologique possible : [0, 2, 1, 3]
(0 avant 1 et 2, 2 avant 3, 1 avant 3)
```

**Important :** Le tri topologique n'existe **que pour les DAG** (pas de cycles) !

---

## **A. Algorithme de Kahn (BFS)**

**Principe :** Utiliser les degrés entrants (in-degree).

**Étapes :**

1. Calculer le degré entrant de chaque sommet
2. Mettre tous les sommets avec degré entrant = 0 dans une queue
3. Tant que la queue n'est pas vide :
    - Retirer un sommet de la queue
    - Ajouter à l'ordre topologique
    - Réduire le degré entrant de tous ses voisins
    - Si un voisin atteint degré 0, l'ajouter à la queue

```python
from collections import deque, defaultdict

def topological_sort_kahn(graph: Graph) -> List[int]:
    """
    Tri topologique avec l'algorithme de Kahn (BFS)

    Args:
        graph: DAG sous forme de liste d'adjacence

    Returns:
        Ordre topologique, ou [] si cycle détecté

    Complexité: O(V + E)
    """
    # Calculer les degrés entrants
    in_degree = {v: 0 for v in graph}

    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    # Queue avec les sommets de degré 0
    queue = deque([v for v in graph if in_degree[v] == 0])
    topo_order = []

    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)

        # Réduire le degré des voisins
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Si tous les sommets ne sont pas dans l'ordre → cycle
    if len(topo_order) != len(graph):
        return []  # Cycle détecté

    return topo_order


# Tests
print("\n=== Tri topologique (Kahn) ===\n")

# Test 1: DAG simple
dag1 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(f"DAG1: {topological_sort_kahn(dag1)}")  # [0, 1, 2, 3] ou [0, 2, 1, 3]

# Test 2: Avec cycle
cycle_graph = {
    0: [1],
    1: [2],
    2: [0]
}
print(f"Graph avec cycle: {topological_sort_kahn(cycle_graph)}")  # []

# Test 3: Cours avec prérequis
courses = {
    'Math 101': ['Math 201', 'CS 101'],
    'Math 201': ['CS 201'],
    'CS 101': ['CS 201'],
    'CS 201': []
}
# Convertir en indices
graph_courses = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(f"Ordre des cours: {topological_sort_kahn(graph_courses)}")  # [0, 1, 2, 3]
```

---

## **B. Algorithme DFS**

**Principe :** Utiliser DFS et empiler les sommets dans l'ordre **post-order** (après avoir visité tous les descendants).

```python
def topological_sort_dfs(graph: Graph) -> List[int]:
    """
    Tri topologique avec DFS

    Returns:
        Ordre topologique, ou [] si cycle détecté

    Complexité: O(V + E)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}
    stack = []
    has_cycle = False

    def dfs(vertex: int) -> None:
        nonlocal has_cycle

        color[vertex] = GRAY

        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:
                has_cycle = True
                return

            if color[neighbor] == WHITE:
                dfs(neighbor)

        color[vertex] = BLACK
        stack.append(vertex)  # Post-order

    for vertex in graph:
        if color[vertex] == WHITE:
            dfs(vertex)
            if has_cycle:
                return []

    return stack[::-1]  # Inverser


# Test
print("\n=== Tri topologique (DFS) ===\n")
print(f"DAG1 (DFS): {topological_sort_dfs(dag1)}")  # [0, 2, 1, 3]
```

---

## **Comparaison Kahn vs DFS**

| Aspect              | Kahn (BFS)         | DFS              |
| ------------------- | ------------------ | ---------------- |
| **Complexité**      | O(V + E)           | O(V + E)         |
| **Détection cycle** | ✅ Automatique     | ✅ Avec couleurs |
| **Ordre**           | Niveau par niveau  | Post-order       |
| **Implémentation**  | Un peu plus longue | Plus courte      |
| **Préférence**      | Plus intuitif      | Plus concis      |

---

## **Résumé du Module 3**

✅ **Détection de cycles** :

- Non-dirigé : DFS avec tracking parent
- Dirigé : DFS avec 3 couleurs (White-Gray-Black)

✅ **Composantes connexes** :

- Compter : DFS sur chaque composante
- Trouver : DFS avec collection

✅ **Tri topologique** :

- Kahn (BFS) : Utilise in-degree
- DFS : Post-order inversé
- Seulement pour les DAG !

---

**Voulez-vous des exercices sur le Module 3 avant de passer au Module 4 (Plus courts chemins) ?** 🚀

Ou préférez-vous continuer directement avec Dijkstra, Bellman-Ford, etc. ?
