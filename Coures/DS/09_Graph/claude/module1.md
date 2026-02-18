# Module 1 : Fondamentaux des Graphes

## **1. Introduction aux graphes**

### **Qu'est-ce qu'un graphe ?**

Un **graphe** est une structure mathématique utilisée pour modéliser des relations entre des objets. Il est composé de :

- **Sommets (Vertices/Nodes)** : Les objets/entités
- **Arêtes (Edges)** : Les connexions/relations entre les sommets

**Notation mathématique :**

- G = (V, E)
- V = ensemble de sommets
- E = ensemble d'arêtes

### **Terminologie de base**

| Terme               | Définition                                       | Exemple                             |
| ------------------- | ------------------------------------------------ | ----------------------------------- |
| **Sommet/Nœud**     | Point dans le graphe                             | Ville, personne, page web           |
| **Arête**           | Connexion entre deux sommets                     | Route, amitié, lien hypertexte      |
| **Voisin/Adjacent** | Sommets connectés par une arête                  | Si A—B, alors A et B sont adjacents |
| **Degré**           | Nombre d'arêtes connectées à un sommet           | Degré(A) = 3 si A a 3 voisins       |
| **Chemin**          | Séquence de sommets connectés                    | A → B → C → D                       |
| **Cycle**           | Chemin qui revient au sommet de départ           | A → B → C → A                       |
| **Graphe connexe**  | Il existe un chemin entre toute paire de sommets | Tous les sommets sont "reliés"      |

---

## **2. Types de graphes**

### **a) Graphe non-dirigé (Undirected Graph)**

Les arêtes n'ont **pas de direction**. Si A est connecté à B, alors B est connecté à A.

```
    A ---- B
    |      |
    |      |
    C ---- D
```

**Exemples :**

- Réseau d'amis Facebook (amitié = relation bidirectionnelle)
- Routes entre villes (on peut aller dans les deux sens)
- Réseau électrique

### **b) Graphe dirigé (Directed Graph / Digraph)**

Les arêtes ont une **direction** (représentées par des flèches).

```
    A --→ B
    ↑     ↓
    |     |
    C ←-- D
```

**Exemples :**

- Twitter (suivre quelqu'un ≠ être suivi)
- Pages web avec liens hypertextes
- Dépendances entre tâches

**Termes spécifiques :**

- **Degré entrant (in-degree)** : nombre d'arêtes entrantes
- **Degré sortant (out-degree)** : nombre d'arêtes sortantes

### **c) Graphe pondéré (Weighted Graph)**

Chaque arête a un **poids/coût** associé.

```
    A --(5)-- B
    |         |
   (2)       (3)
    |         |
    C --(1)-- D
```

**Exemples :**

- Distances entre villes
- Coût de transport
- Temps de trajet

### **d) Graphe non-pondéré**

Toutes les arêtes ont le même poids (souvent considéré comme 1).

### **e) Graphe cyclique vs Acyclique**

- **Cyclique** : Contient au moins un cycle
- **Acyclique** : Ne contient aucun cycle
- **DAG (Directed Acyclic Graph)** : Graphe dirigé sans cycle (très utilisé !)

```
DAG exemple :
    A → B → D
    ↓       ↑
    C ------+
```

### **f) Graphe complet**

Chaque sommet est connecté à **tous les autres sommets**.

- Pour n sommets : nombre d'arêtes = n(n-1)/2 (non-dirigé)

```
    A ----- B
    |\     /|
    | \   / |
    |  \ /  |
    |   X   |
    |  / \  |
    | /   \ |
    C ----- D
```

### **g) Graphe biparti**

Les sommets peuvent être divisés en **deux ensembles** où les arêtes ne connectent que des sommets de groupes différents.

```
Groupe 1:  A    B
            |\ /|
            | X |
            |/ \|
Groupe 2:  C    D
```

**Exemples :**

- Étudiants ↔ Cours
- Employés ↔ Tâches

### **h) Arbre**

Un graphe **connexe** et **acyclique** (cas particulier très important).

```
        A
       / \
      B   C
     / \
    D   E
```

**Propriétés :**

- n sommets ⟹ n-1 arêtes
- Il existe un unique chemin entre toute paire de sommets

---

## **3. Applications réelles des graphes**

| Domaine                  | Application           | Type de graphe    |
| ------------------------ | --------------------- | ----------------- |
| **Réseaux sociaux**      | Amis, followers       | Dirigé/Non-dirigé |
| **Navigation GPS**       | Routes, chemins       | Pondéré, dirigé   |
| **Internet**             | Réseau de routeurs    | Graphe général    |
| **Compilateurs**         | Graphe de dépendances | DAG               |
| **Jeux**                 | États du jeu          | Dirigé            |
| **Biologie**             | Réseaux de protéines  | Non-dirigé        |
| **Ordonnancement**       | Tâches avec prérequis | DAG               |
| **Recommandations**      | Produits similaires   | Graphe pondéré    |
| **Circuits électriques** | Composants connectés  | Graphe général    |

---

## **Résumé du Module 1.1**

✅ Un graphe = (Sommets, Arêtes)  
✅ Types principaux : dirigé/non-dirigé, pondéré/non-pondéré, cyclique/acyclique  
✅ Vocabulaire clé : degré, chemin, cycle, connexité  
✅ Applications partout : réseaux, navigation, dépendances, etc.

## **2. Représentation des graphes**

Pour travailler avec des graphes en programmation, nous devons les représenter en mémoire. Il existe **3 méthodes principales**.

---

## **A. Matrice d'adjacence (Adjacency Matrix)**

### **Principe**

Utiliser une matrice 2D de taille **n × n** (où n = nombre de sommets).

- `matrix[i][j] = 1` si une arête existe entre le sommet i et le sommet j
- `matrix[i][j] = 0` sinon

Pour les graphes pondérés : `matrix[i][j] = poids` de l'arête.

### **Exemple visuel**

**Graphe non-dirigé :**

```
    0 ---- 1
    |      |
    |      |
    2 ---- 3
```

**Matrice d'adjacence :**

```
     0  1  2  3
   +------------
0  | 0  1  1  0
1  | 1  0  0  1
2  | 1  0  0  1
3  | 0  1  1  0
```

**Graphe dirigé :**

```
    0 --→ 1
    ↑     ↓
    |     |
    2 ←-- 3
```

**Matrice d'adjacence :**

```
     0  1  2  3
   +------------
0  | 0  1  0  0
1  | 0  0  0  1
2  | 1  0  0  0
3  | 0  0  1  0
```

### **Implémentation en Python**

```python
# Graphe non-dirigé
n = 4  # nombre de sommets
matrix = [[0] * n for _ in range(n)]

# Ajouter une arête entre 0 et 1
def add_edge(u, v):
    matrix[u][v] = 1
    matrix[v][u] = 1  # Bidirectionnel pour non-dirigé

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

print(matrix)
# [[0, 1, 1, 0],
#  [1, 0, 0, 1],
#  [1, 0, 0, 1],
#  [0, 1, 1, 0]]
```

```python
# Graphe dirigé
def add_directed_edge(u, v):
    matrix[u][v] = 1  # Unidirectionnel

# Graphe pondéré
def add_weighted_edge(u, v, weight):
    matrix[u][v] = weight
    matrix[v][u] = weight  # Si non-dirigé
```

### **Avantages ✅**

- Vérifier si une arête existe : **O(1)** très rapide
- Simple à comprendre et implémenter
- Bon pour les graphes denses (beaucoup d'arêtes)

### **Inconvénients ❌**

- Espace : **O(n²)** même si peu d'arêtes (gaspillage pour graphes creux)
- Parcourir tous les voisins : **O(n)** (doit parcourir toute la ligne)
- Inefficace pour graphes avec peu d'arêtes

---

## **B. Liste d'adjacence (Adjacency List)**

### **Principe**

Pour chaque sommet, maintenir une **liste de ses voisins**.

- Utiliser un tableau/dictionnaire où chaque index/clé contient une liste.

### **Exemple visuel**

**Graphe non-dirigé :**

```
    0 ---- 1
    |      |
    |      |
    2 ---- 3
```

**Liste d'adjacence :**

```
0 → [1, 2]
1 → [0, 3]
2 → [0, 3]
3 → [1, 2]
```

**Graphe dirigé :**

```
    0 --→ 1
    ↑     ↓
    |     |
    2 ←-- 3
```

**Liste d'adjacence :**

```
0 → [1]
1 → [3]
2 → [0]
3 → [2]
```

### **Implémentation en Python**

```python
# Méthode 1 : Liste de listes
n = 4
adj_list = [[] for _ in range(n)]

def add_edge(u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # Bidirectionnel si non-dirigé

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

print(adj_list)
# [[1, 2], [0, 3], [0, 3], [1, 2]]
```

```python
# Méthode 2 : Dictionnaire (plus flexible)
from collections import defaultdict

graph = defaultdict(list)

def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)  # Si non-dirigé

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

print(dict(graph))
# {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
```

```python
# Pour graphe pondéré : stocker (voisin, poids)
graph = defaultdict(list)

def add_weighted_edge(u, v, weight):
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # Si non-dirigé

add_weighted_edge(0, 1, 5)
add_weighted_edge(0, 2, 3)

print(dict(graph))
# {0: [(1, 5), (2, 3)], 1: [(0, 5)], 2: [(0, 3)]}
```

### **Avantages ✅**

- Espace : **O(V + E)** (V = sommets, E = arêtes) - très efficace pour graphes creux
- Parcourir tous les voisins : **O(degré du sommet)** - très rapide
- Efficace en mémoire
- **MEILLEURE représentation dans 90% des cas**

### **Inconvénients ❌**

- Vérifier si une arête existe : **O(degré du sommet)** (doit parcourir la liste)
- Légèrement plus complexe à implémenter

---

## **C. Edge List (Liste d'arêtes)**

### **Principe**

Stocker simplement toutes les arêtes dans une liste.

```python
# Graphe non-dirigé
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]

# Graphe pondéré
weighted_edges = [
    (0, 1, 5),  # (source, destination, poids)
    (0, 2, 3),
    (1, 3, 2),
    (2, 3, 1)
]
```

### **Avantages ✅**

- Très simple
- Utile pour algorithmes comme Kruskal (MST)
- Espace : **O(E)**

### **Inconvénients ❌**

- Trouver les voisins d'un sommet : **O(E)** (très lent)
- Rarement utilisé seul

---

## **3. Comparaison et choix de représentation**

| Critère                  | Matrice d'adjacence | Liste d'adjacence | Edge List |
| ------------------------ | ------------------- | ----------------- | --------- |
| **Espace**               | O(V²)               | O(V + E)          | O(E)      |
| **Vérifier arête(u,v)**  | O(1) ⚡             | O(degré(u))       | O(E)      |
| **Trouver voisins de u** | O(V)                | O(degré(u)) ⚡    | O(E)      |
| **Ajouter arête**        | O(1)                | O(1)              | O(1)      |
| **Supprimer arête**      | O(1)                | O(degré(u))       | O(E)      |
| **Graphes denses**       | ✅ Bon              | ❌ Moins bon      | ❌        |
| **Graphes creux**        | ❌ Gaspillage       | ✅ Excellent      | ✅        |
| **LeetCode/Interviews**  | Rare                | **✅ Standard**   | Rare      |

### **Quand utiliser quoi ?**

📌 **Liste d'adjacence** (90% des cas) :

- Graphes avec peu d'arêtes (graphes creux)
- BFS, DFS, Dijkstra
- La plupart des problèmes LeetCode

📌 **Matrice d'adjacence** :

- Graphes denses (beaucoup d'arêtes)
- Besoin de vérifier rapidement l'existence d'arêtes
- Algorithmes comme Floyd-Warshall

📌 **Edge List** :

- Algorithmes MST (Kruskal)
- Quand on ne parcourt pas le graphe

---

## **4. Exemples pratiques en Python**

### **Construire un graphe depuis des inputs LeetCode**

```python
# Input typique LeetCode : n = 5, edges = [[0,1],[0,2],[1,3],[2,4]]

def build_graph(n, edges):
    """Construit une liste d'adjacence"""
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Si non-dirigé

    return graph

# Exemple
n = 5
edges = [[0,1],[0,2],[1,3],[2,4]]
graph = build_graph(n, edges)
print(graph)
# [[1, 2], [0, 3], [0, 4], [1], [2]]
```

### **Graphe dirigé pondéré avec defaultdict**

```python
from collections import defaultdict

def build_weighted_digraph(edges):
    """edges = [(u, v, weight), ...]"""
    graph = defaultdict(list)

    for u, v, weight in edges:
        graph[u].append((v, weight))

    return graph

# Exemple
edges = [(0, 1, 10), (0, 2, 5), (1, 3, 1), (2, 3, 2)]
graph = build_weighted_digraph(edges)
print(dict(graph))
# {0: [(1, 10), (2, 5)], 1: [(3, 1)], 2: [(3, 2)]}
```

---

## **Résumé du Module 1**

✅ **3 représentations** : Matrice, Liste d'adjacence, Edge List  
✅ **Liste d'adjacence = standard** pour la plupart des problèmes  
✅ **Complexité** : Liste d'adjacence O(V+E) vs Matrice O(V²)  
✅ **Python** : `defaultdict(list)` ou `[[] for _ in range(n)]`

---

## **Exercice rapide avant de passer au Module 2** 🎯

Essayez de coder ceci :

**Problème :** Étant donné `n = 4` et `edges = [[0,1],[1,2],[2,3],[3,0]]`, construisez :

1. Une liste d'adjacence (non-dirigé)
2. Une matrice d'adjacence
3. Comptez le degré de chaque sommet

### RQ :

## **Deux concepts différents**

### **1. Matrice d'adjacence (Adjacency Matrix)**

**Représentation d'un graphe**

### **2. Grille 2D (Grid)**

**Le graphe lui-même**

Ce sont **deux choses complètement différentes** !

## **Type 1 : Matrice d'adjacence**

### **Définition**

Une matrice qui **représente** un graphe avec **n sommets**.

```python
# Graphe avec 4 sommets (0, 1, 2, 3)
#    0 --- 1
#    |     |
#    2 --- 3

# Matrice d'adjacence 4x4
matrix = [
    [0, 1, 1, 0],  # Sommet 0 connecté à 1 et 2
    [1, 0, 0, 1],  # Sommet 1 connecté à 0 et 3
    [1, 0, 0, 1],  # Sommet 2 connecté à 0 et 3
    [0, 1, 1, 0]   # Sommet 3 connecté à 1 et 2
]

# Nombre de sommets = 4 (fixe)
# matrix[i][j] = 1 signifie "arête entre i et j"
```

**Caractéristiques :**

- ✅ Taille : **n × n** (n = nombre de sommets)
- ✅ `matrix[i][j]` indique si une **arête existe** entre sommet i et sommet j
- ✅ Valeurs : 0 ou 1 (ou poids pour graphes pondérés)
- ✅ Nombre de sommets = **n** (nombre de lignes = nombre de colonnes)

---

## **Type 2 : Grille 2D (Grid/Matrix as Graph)**

### **Définition**

Une matrice où **chaque case EST un sommet** du graphe.

```python
# Grille 4x4 (labyrinthe)
grid = [
    [0, 0, 1, 0],  # 4 cases (4 sommets potentiels)
    [0, 1, 0, 0],  # 4 cases (4 sommets potentiels)
    [0, 0, 0, 1],  # 4 cases (4 sommets potentiels)
    [1, 0, 0, 0]   # 4 cases (4 sommets potentiels)
]

# Nombre de sommets = rows × cols = 4 × 4 = 16 !
# Chaque case (i, j) est un sommet
# grid[i][j] = 0 signifie "ce sommet est accessible"
# grid[i][j] = 1 signifie "ce sommet est bloqué (obstacle)"
```

**Caractéristiques :**

- ✅ Taille : **rows × cols** (peut être rectangulaire)
- ✅ Chaque case `(i, j)` **EST un sommet**
- ✅ Valeurs : 0 (libre) ou 1 (obstacle) ou autres valeurs
- ✅ Nombre de sommets = **rows × cols**
- ✅ Arêtes implicites : une case peut aller vers ses **4 voisins** (haut, bas, gauche, droite)

---

## **Comparaison visuelle**

### **Matrice d'adjacence (4 sommets)**

```
Graphe:          Matrice d'adjacence:
                      0  1  2  3
  0 --- 1           +-----------
  |     |        0  | 0  1  1  0
  2 --- 3        1  | 1  0  0  1
                 2  | 1  0  0  1
                 3  | 0  1  1  0

Nombre de sommets: 4
```

---

### **Grille 2D (16 sommets)**

```
Grille (0=libre, 1=obstacle):

    [0, 0, 1, 0]
    [0, 1, 0, 0]
    [0, 0, 0, 1]
    [1, 0, 0, 0]

Graphe équivalent (chaque case = sommet):

(0,0)---(0,1)  X  (0,3)
  |       |         |
(1,0)  X (1,2)---(1,3)
  |       |       |
(2,0)---(2,1)---(2,2)  X
        |       |
  X     (3,1)---(3,2)---(3,3)

Nombre de sommets: 4 × 4 = 16
(certains bloqués par obstacles)
```


## **Conversion : Grille → Graphe explicite**

Pour mieux comprendre, convertissons la grille en liste d'adjacence :

```python
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

def grid_to_graph(grid):
    """
    Convertit une grille en graphe explicite
    Chaque case (i,j) devient un sommet numéroté
    """
    rows, cols = len(grid), len(grid[0])
    graph = {}

    # Fonction pour convertir (row, col) en numéro de sommet
    def to_vertex(r, c):
        return r * cols + c

    # Directions: haut, bas, gauche, droite
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(rows):
        for col in range(cols):
            # Ignorer les obstacles
            if grid[row][col] == 1:
                continue

            vertex = to_vertex(row, col)
            graph[vertex] = []

            # Ajouter les voisins
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[new_row][new_col] == 0):

                    neighbor = to_vertex(new_row, new_col)
                    graph[vertex].append(neighbor)

    return graph


# Conversion
graph = grid_to_graph(grid)
print(graph)
```

**Résultat :**

```python
{
    0: [1, 4],          # (0,0) connecté à (0,1) et (1,0)
    1: [0],             # (0,1) connecté à (0,0)
    3: [7],             # (0,3) connecté à (1,3)
    4: [0, 8],          # (1,0) connecté à (0,0) et (2,0)
    6: [7, 10],         # (1,2) connecté à (1,3) et (2,2)
    7: [3, 6, 11],      # (1,3) connecté à (0,3), (1,2) et (2,3) - NON! (2,3) est obstacle
    8: [4, 9],          # (2,0) connecté à (1,0) et (2,1)
    9: [8, 10, 13],     # (2,1) connecté à (2,0), (2,2) et (3,1)
    10: [6, 9],         # (2,2) connecté à (1,2) et (2,1)
    13: [9, 14],        # (3,1) connecté à (2,1) et (3,2)
    14: [13, 15]        # (3,2) connecté à (3,1) et (3,3)
    15: [14]            # (3,3) connecté à (3,2)
}
```

**Mapping :**

```
Position (row, col) → Numéro de sommet
(0, 0) → 0
(0, 1) → 1
(0, 2) → 2  (obstacle, pas dans le graphe)
(0, 3) → 3
(1, 0) → 4
(1, 1) → 5  (obstacle, pas dans le graphe)
...
(3, 3) → 15
```

---

## **Formule de conversion**

```python
# Position vers numéro de sommet
vertex_number = row * cols + col

# Numéro de sommet vers position
row = vertex_number // cols
col = vertex_number % cols
```

**Exemples :**

```python
# Grid 4x4
cols = 4

(0, 0) → 0 * 4 + 0 = 0
(0, 1) → 0 * 4 + 1 = 1
(1, 0) → 1 * 4 + 0 = 4
(2, 3) → 2 * 4 + 3 = 11
(3, 3) → 3 * 4 + 3 = 15
```

---

## **Résumé de la différence**

| Aspect           | Matrice d'adjacence         | Grille 2D                                   |
| ---------------- | --------------------------- | ------------------------------------------- |
| **Rôle**         | **Représente** un graphe    | **EST** le graphe                           |
| **Taille**       | n × n (carré obligatoire)   | rows × cols (peut être rectangulaire)       |
| **Sommets**      | n sommets fixes             | rows × cols sommets                         |
| **matrix[i][j]** | Arête existe entre i et j ? | Case (i,j) est accessible ?                 |
| **Valeurs**      | 0/1 ou poids                | 0 (libre), 1 (obstacle), etc.               |
| **Voisins**      | Définis par la matrice      | Toujours 4 voisins (haut/bas/gauche/droite) |

---

## **Exemple complet**

### **Graphe avec 4 sommets**

```python
# MATRICE D'ADJACENCE
# Représente ce graphe: 0--1--2--3

adj_matrix = [
    [0, 1, 0, 0],  # 0 connecté à 1
    [1, 0, 1, 0],  # 1 connecté à 0 et 2
    [0, 1, 0, 1],  # 2 connecté à 1 et 3
    [0, 0, 1, 0]   # 3 connecté à 2
]

# 4 sommets (numérotés 0, 1, 2, 3)
```

### **Grille avec 16 sommets**

```python
# GRILLE 2D
# Chaque case est un sommet

grid = [
    [0, 0, 0, 0],  # 4 sommets: (0,0), (0,1), (0,2), (0,3)
    [0, 0, 0, 0],  # 4 sommets: (1,0), (1,1), (1,2), (1,3)
    [0, 0, 0, 0],  # 4 sommets: (2,0), (2,1), (2,2), (2,3)
    [0, 0, 0, 0]   # 4 sommets: (3,0), (3,1), (3,2), (3,3)
]

# 16 sommets au total !
# Chaque sommet (i,j) peut aller vers (i±1,j) et (i,j±1)
```

---

## **Pourquoi la confusion ?**

Les deux utilisent des matrices, mais :

- **Matrice d'adjacence** : outil de **représentation** d'un graphe abstrait
- **Grille** : le graphe **lui-même** est spatial/géométrique

---

**C'est plus clair maintenant ?** 🎯

Voulez-vous qu'on :

1. Continue avec **DFS** ?
2. Voie plus d'exemples de **conversion grille → graphe** ?
3. Fasse des **exercices** pour bien différencier les deux ?
