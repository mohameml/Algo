# Module 1 — Fondamentaux & Théorie du Heap

## 1. Qu'est-ce qu'un Heap ?

> Un **Heap** est un arbre binaire **complet** qui satisfait la **heap property**.

- "Complet" signifie que tous les niveaux sont remplis sauf possibly le dernier, qui se remplit de gauche à droite.

Il existe deux variantes :

- **Min-Heap** : chaque nœud est **≤** à ses enfants → la racine est le **minimum global**

- **Max-Heap** : chaque nœud est **≥** à ses enfants → la racine est le **maximum global**

```
Min-Heap exemple :        Max-Heap exemple :
        1                         9
       / \                       / \
      3   2                     7   8
     / \ / \                   4  5 6  3
    7  8 5  6
```

> La heap property est **locale** (parent vs ses enfants directs), pas globale. Donc un heap n'est **pas** trié.

## 2. **Représentation en Tableau:**

- C'est la clé. On n'utilise jamais de pointeurs — on stocke le heap dans un tableau simple.

- **Pour un noeud à l'index `i` :**

    ```
    Parent      → (i - 1) // 2
    Enfant gauche → 2*i + 1
    Enfant droit  → 2*i + 2
    ```

- **Exemple :**

    L'arbre ci-dessus `[1, 3, 2, 7, 8, 5, 6]` se lit :

    ```
    Index :  0  1  2  3  4  5  6
    Valeur : 1  3  2  7  8  5  6

    i=0 (valeur 1) → enfants : index 1 (val 3) et index 2 (val 2)
    i=1 (valeur 3) → parent : index 0 (val 1), enfants : index 3 (val 7) et 4 (val 8)
    i=2 (valeur 2) → parent : index 0 (val 1), enfants : index 5 (val 5) et 6 (val 6)
    ```

- Vérifie toujours la heap property : chaque parent ≤ ses enfants ✓

## 3. Les Deux Opérations Fondamentales

Tout repose sur deux primitives : **heapify_up** et **heapify_down**.

### heapify_up (aussi appelé "bubble up" ou "sift up")

Utilisé après un **insert**. On ajoute l'élément à la fin du tableau, puis on le fait "remonter" tant qu'il viole la heap property avec son parent.

```
Insert 1 dans ce Min-Heap :

Avant :          Après ajout à la fin :    Après heapify_up :
    2                   2                       1
   / \                 / \                     / \
  3   5               3   5                   3   2
                     /                       /   /
                    1  ← viole !            7   5
                    ↑
               remonte jusqu'à la racine
```

### heapify_down (aussi appelé "bubble down" ou "sift down")

Utilisé après un **extract**. On retire la racine, on met le dernier élément à sa place, puis on le fait "descendre" en swappant avec le plus petit enfant (pour Min-Heap).

```
Extract_min de [1, 3, 2, 7, 8, 5, 6] :

Étape 1 : retire 1, met 6 à la racine
[6, 3, 2, 7, 8, 5]

Étape 2 : heapify_down
    6              →      2              →      2
   / \                   / \                   / \
  3   2                 3   6                 3   5
 / \ /                 / \ /                 / \ /
7  8 5                7  8 5               7  8 6

6 > min(3,2)=2       6 > min(5)=5
swap avec 2          swap avec 5
```

## 4. Complexités

| Opération                     | Complexité     | Pourquoi                                |
| ----------------------------- | -------------- | --------------------------------------- |
| `peek` (lire min/max)         | **O(1)**       | Toujours à l'index 0                    |
| `insert`                      | **O(log n)**   | heapify_up : hauteur de l'arbre = log n |
| `extract_min/max`             | **O(log n)**   | heapify_down : hauteur = log n          |
| `delete` (élément quelconque) | **O(log n)**   | Trouver O(n) + heapify O(log n)         |
| `build_heap` from array       | **O(n)**       | ⚠️ pas O(n log n) — voir ci-dessous     |
| `heap_sort`                   | **O(n log n)** | n extractions × O(log n)                |
| `search`                      | **O(n)**       | Pas de propriété d'ordre global         |

### Pourquoi build_heap est O(n) et pas O(n log n) ?

C'est une question classique d'interview ! L'intuition naïve dirait O(n log n) car on fait n insertions à O(log n). Mais l'algorithme de Floyd est plus malin :

On part des feuilles (déjà valides) et on heapify_down uniquement les nœuds internes, **en commençant par le bas**. Les nœuds bas ont une hauteur faible → peu de travail.

La somme exacte : $\sum_{h=0}^{\lfloor \log n \rfloor} \lceil \frac{n}{2^{h+1}} \rceil \cdot O(h) = O(n \sum_{h=0}^{\infty} \frac{h}{2^h}) = O(n \cdot 2) = O(n)$

Car $\sum_{h=0}^{\infty} \frac{h}{2^h} = 2$ (série géométrique dérivée).

## 5. Heap vs Structures Comparables

| Structure         | Insert   | Find Min | Extract Min | Search   |
| ----------------- | -------- | -------- | ----------- | -------- |
| **Min-Heap**      | O(log n) | O(1)     | O(log n)    | O(n)     |
| BST (équilibré)   | O(log n) | O(log n) | O(log n)    | O(log n) |
| Sorted Array      | O(n)     | O(1)     | O(n)        | O(log n) |
| Sorted LinkedList | O(n)     | O(1)     | O(1)        | O(n)     |

> **Quand choisir un Heap ?** Quand tu as besoin d'accéder **répétitivement au min/max** et d'insérer dynamiquement. Si tu as besoin de chercher des éléments arbitraires → BST.

## RQ : Résumé Module 1

```
Heap = Arbre binaire complet + Heap property (locale)
Stocké en tableau : parent=(i-1)//2, gauche=2i+1, droite=2i+2
Deux primitives : heapify_up (après insert) + heapify_down (après extract)
Peek O(1) | Insert/Extract O(log n) | Build O(n)
```
