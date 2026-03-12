# Module 2 — Implémentation Min-Heap from Scratch

## 1. Min-Heap complet avec typing

```python
from typing import List, Optional

class MinHeap:
    """
    Min-Heap implémenté avec un tableau dynamique.
    Heap property : heap[parent] <= heap[enfant] pour tout nœud.

    Représentation interne :
        Parent(i)       = (i - 1) // 2
        Left child(i)   = 2 * i + 1
        Right child(i)  = 2 * i + 2
    """

    def __init__(self) -> None:
        self._data: List[int] = []

    # ─────────────────────────────────────────────
    # HELPERS INTERNES
    # ─────────────────────────────────────────────

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _has_parent(self, i: int) -> bool:
        return i > 0                          # la racine (i=0) n'a pas de parent

    def _has_left(self, i: int) -> bool:
        return self._left(i) < len(self._data)

    def _has_right(self, i: int) -> bool:
        return self._right(i) < len(self._data)

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # ─────────────────────────────────────────────
    # LECTURE (O(1))
    # ─────────────────────────────────────────────

    def peek(self) -> int:
        """Retourne le minimum sans le retirer — O(1)."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    # ─────────────────────────────────────────────
    # INSERT — O(log n)
    # ─────────────────────────────────────────────

    def insert(self, val: int) -> None:
        """
        1. Ajoute val à la fin du tableau  → maintient la structure complète
        2. heapify_up                       → restaure la heap property
        """
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)   # index du nouvel élément

    def _heapify_up(self, i: int) -> None:
        """
        Remonte l'élément à l'index i tant qu'il est
        plus petit que son parent. (violation vers le haut)

        Invariant : après chaque swap, l'index courant devient celui du parent.
        """
        while self._has_parent(i):
            p = self._parent(i)
            if self._data[i] < self._data[p]:   # violation → remonter
                self._swap(i, p)
                i = p                            # continue depuis le parent
            else:
                break                            # heap property restaurée

    # ─────────────────────────────────────────────
    # EXTRACT MIN — O(log n)
    # ─────────────────────────────────────────────

    def extract_min(self) -> int:
        """
        1. Sauvegarde la racine (= minimum)
        2. Met le dernier élément à la racine  → maintient la structure complète
        3. Supprime le dernier                 → taille réduite de 1
        4. heapify_down                        → restaure la heap property
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        min_val: int = self._data[0]             # sauvegarde le min
        last: int    = self._data[-1]            # dernier élément

        self._data[0] = last                     # place le dernier à la racine
        self._data.pop()                         # supprime le dernier

        if not self.is_empty():
            self._heapify_down(0)                # restaure depuis la racine

        return min_val

    def _heapify_down(self, i: int) -> None:
        """
        Descend l'élément à l'index i en swappant avec
        le plus PETIT de ses enfants, tant qu'il y a violation.

        Invariant : on swap toujours avec le minimum des enfants
                    pour ne pas créer de nouvelle violation.
        """
        while self._has_left(i):                 # au moins un enfant gauche

            # trouve l'index du plus petit enfant
            smallest_child: int = self._left(i)

            if self._has_right(i) and self._data[self._right(i)] < self._data[smallest_child]:
                smallest_child = self._right(i)

            if self._data[i] > self._data[smallest_child]:   # violation → descendre
                self._swap(i, smallest_child)
                i = smallest_child
            else:
                break                            # heap property restaurée

    # ─────────────────────────────────────────────
    # BUILD HEAP — O(n)  [Floyd's Algorithm]
    # ─────────────────────────────────────────────

    @classmethod
    def from_list(cls, values: List[int]) -> "MinHeap":
        """
        Construit un heap en O(n) via l'algorithme de Floyd.

        Idée : les feuilles sont déjà des heaps valides (taille 1).
               On heapify_down uniquement les nœuds internes,
               en commençant par le dernier nœud interne vers la racine.

        Dernier nœud interne = parent du dernier élément
                             = (n - 2) // 2
        """
        heap = cls()
        heap._data = list(values)                # copie du tableau
        n: int = len(heap._data)

        # itère de (n//2 - 1) jusqu'à 0 inclus
        # tous les index >= n//2 sont des feuilles → rien à faire
        for i in range((n - 2) // 2, -1, -1):
            heap._heapify_down(i)

        return heap

    # ─────────────────────────────────────────────
    # DELETE élément quelconque — O(n + log n) = O(n)
    # ─────────────────────────────────────────────

    def delete(self, val: int) -> bool:
        """
        Supprime la première occurrence de val.

        1. Trouve l'index de val          → O(n)  [scan linéaire]
        2. Swap avec le dernier élément   → O(1)
        3. Pop le dernier                 → O(1)
        4. Restaure la heap property      → O(log n)
           (heapify_up OU heapify_down selon le cas)
        """
        try:
            idx: int = self._data.index(val)     # O(n)
        except ValueError:
            return False                          # val pas trouvé

        last_idx: int = len(self._data) - 1

        if idx == last_idx:                      # cas simple : dernier élément
            self._data.pop()
            return True

        self._swap(idx, last_idx)
        self._data.pop()                         # supprime l'ancien val

        # après le swap, le nouvel élément à idx peut violer vers le haut ou le bas
        self._heapify_up(idx)
        self._heapify_down(idx)                  # une seule des deux aura un effet

        return True

    # ─────────────────────────────────────────────
    # HEAP SORT — O(n log n)
    # ─────────────────────────────────────────────

    def to_sorted_list(self) -> List[int]:
        """
        Extrait tous les éléments dans l'ordre croissant.
        Détruit le heap (on travaille sur une copie).
        """
        backup: List[int]  = list(self._data)    # sauvegarde
        result: List[int]  = []

        while not self.is_empty():
            result.append(self.extract_min())

        self._data = backup                      # restaure
        return result

    # ─────────────────────────────────────────────
    # AFFICHAGE
    # ─────────────────────────────────────────────

    def __repr__(self) -> str:
        return f"MinHeap({self._data})"

    def display(self) -> None:
        """Affiche le heap niveau par niveau."""
        if self.is_empty():
            print("Heap vide")
            return

        level_start: int = 0
        level_size:  int = 1

        while level_start < len(self._data):
            level_end = min(level_start + level_size, len(self._data))
            print(self._data[level_start:level_end])
            level_start = level_end
            level_size  *= 2
```

### Trace d'exécution pas à pas

```python
# ── Construction ──────────────────────────────
h = MinHeap()

h.insert(5)   # _data = [5]
h.insert(3)   # _data = [5, 3]  → heapify_up: 3 < 5, swap → [3, 5]
h.insert(8)   # _data = [3, 5, 8] → 8 > parent(3), ok
h.insert(1)   # _data = [3, 5, 8, 1]
              # heapify_up(3): 1 < parent=5, swap → [3, 1, 8, 5]
              # heapify_up(1): 1 < parent=3, swap → [1, 3, 8, 5]
h.insert(4)   # _data = [1, 3, 8, 5, 4]
              # heapify_up(4): 4 > parent=3, ok

print(h)      # MinHeap([1, 3, 8, 5, 4])
h.display()
# [1]
# [3, 8]
# [5, 4]

# ── Peek ──────────────────────────────────────
print(h.peek())   # 1  — O(1)

# ── Extract min ───────────────────────────────
print(h.extract_min())   # 1
# Étape 1 : last=4, data[0]=4 → [4, 3, 8, 5]
# heapify_down(0): smallest_child = min(3,8) = 3 (index 1)
# 4 > 3, swap → [3, 4, 8, 5]
# heapify_down(1): smallest_child = min(5) = 5 (index 3)
# 4 < 5, stop
print(h)   # MinHeap([3, 4, 8, 5])

# ── Build Heap O(n) ───────────────────────────
h2 = MinHeap.from_list([9, 4, 7, 1, 8, 3, 2])
# Dernier nœud interne = (7-2)//2 = 2
# i=2 : heapify_down([9,4,7,1,8,3,2], 2) → 7 vs min(3,2)=2 → swap → [9,4,2,1,8,3,7]
# i=1 : heapify_down([9,4,2,1,8,3,7], 1) → 4 vs min(1,8)=1 → swap → [9,1,2,4,8,3,7]
#        heapify_down(index 3) → 4, pas d'enfants, stop
# i=0 : heapify_down([9,1,2,4,8,3,7], 0) → 9 vs min(1,2)=1 → swap → [1,9,2,4,8,3,7]
#        heapify_down(index 1) → 9 vs min(4,8)=4 → swap → [1,4,2,9,8,3,7]
#        heapify_down(index 3) → 9, pas d'enfants, stop
print(h2)  # MinHeap([1, 4, 2, 9, 8, 3, 7])

# ── Heap Sort ─────────────────────────────────
print(h2.to_sorted_list())   # [1, 2, 3, 4, 7, 8, 9]
```

### Points clés à retenir

**Pourquoi swap avec le plus petit enfant dans heapify_down ?**
Si tu swappes avec le plus grand, tu crées une violation entre les deux enfants. Le plus petit enfant doit remonter pour que le parent reste ≤ aux deux enfants.

**Pourquoi heapify_up ET heapify_down dans delete ?**
Quand tu mets le dernier élément à la place du noeud supprimé, le nouvel élément peut être soit trop petit (viole avec le parent → heapify_up), soit trop grand (viole avec les enfants → heapify_down). Une seule des deux fonctions fera réellement quelque chose.

**Pourquoi from_list commence à `(n-2)//2` et non `n//2 - 1` ?**
Les deux formules sont équivalentes : `(n-2)//2 == n//2 - 1` pour n pair. Pour n impair, `(n-2)//2` est plus précis. On les utilise indifféremment en pratique.

## 2. Heap Générique avec Comparateur Custom

### Pourquoi un Heap générique ?

Le Min-Heap qu'on a codé ne marche que pour des `int`. En interview on a souvent besoin de :

- Heap de **tuples** `(distance, node)` pour Dijkstra
- Heap d'**objets custom** `Task(priority, name)`
- Heap avec **ordre inversé** (Max-Heap) sans réécrire tout
- Heap avec **critère de tri complexe** (ex: trier par fréquence, puis alphabétiquement)

La solution : passer un **comparateur** à la construction.

### Implémentation

```python
from typing import TypeVar, Generic, List, Callable, Optional

T = TypeVar('T')  # type générique — peut être int, tuple, objet, etc.

class Heap(Generic[T]):
    """
    Heap générique qui accepte n'importe quel type T.

    Le comportement Min/Max est contrôlé par le comparateur :
        comparator(a, b) retourne True si a DOIT être au-dessus de b

    Exemples :
        Min-Heap entiers  → comparator = lambda a, b: a < b
        Max-Heap entiers  → comparator = lambda a, b: a > b
        Min-Heap tuples   → comparator = lambda a, b: a[0] < b[0]
    """

    def __init__(self, comparator: Callable[[T, T], bool]) -> None:
        self._data:       List[T]            = []
        self._comparator: Callable[[T, T], bool] = comparator

    # ─────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _has_parent(self, i: int) -> bool:
        return i > 0

    def _has_left(self, i: int) -> bool:
        return self._left(i) < len(self._data)

    def _has_right(self, i: int) -> bool:
        return self._right(i) < len(self._data)

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _has_priority(self, i: int, j: int) -> bool:
        """
        Retourne True si l'élément à l'index i
        doit être AU-DESSUS de l'élément à l'index j.
        Délègue entièrement au comparateur.
        """
        return self._comparator(self._data[i], self._data[j])

    # ─────────────────────────────────────────────
    # LECTURE
    # ─────────────────────────────────────────────

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    # ─────────────────────────────────────────────
    # INSERT — O(log n)
    # ─────────────────────────────────────────────

    def insert(self, val: T) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def _heapify_up(self, i: int) -> None:
        while self._has_parent(i):
            p = self._parent(i)
            if self._has_priority(i, p):   # i doit être au-dessus de son parent ?
                self._swap(i, p)
                i = p
            else:
                break

    # ─────────────────────────────────────────────
    # EXTRACT — O(log n)
    # ─────────────────────────────────────────────

    def extract(self) -> T:
        if self.is_empty():
            raise IndexError("Heap is empty")

        top: T = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()

        if not self.is_empty():
            self._heapify_down(0)

        return top

    def _heapify_down(self, i: int) -> None:
        while self._has_left(i):
            # trouve l'enfant avec la plus haute priorité
            priority_child: int = self._left(i)

            if self._has_right(i) and self._has_priority(self._right(i), priority_child):
                priority_child = self._right(i)

            if self._has_priority(priority_child, i):   # l'enfant doit être au-dessus ?
                self._swap(i, priority_child)
                i = priority_child
            else:
                break

    # ─────────────────────────────────────────────
    # BUILD HEAP — O(n)
    # ─────────────────────────────────────────────

    @classmethod
    def from_list(cls, values: List[T], comparator: Callable[[T, T], bool]) -> "Heap[T]":
        heap: Heap[T]  = cls(comparator)
        heap._data     = list(values)
        n: int         = len(heap._data)

        for i in range((n - 2) // 2, -1, -1):
            heap._heapify_down(i)

        return heap

    def __repr__(self) -> str:
        return f"Heap({self._data})"

```

### Cas d'Usage — Les 5 Patterns Essentiels

#### Pattern 1 : Min-Heap et Max-Heap classiques

```python
# Min-Heap
min_heap: Heap[int] = Heap(comparator=lambda a, b: a < b)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(8)
print(min_heap.peek())      # 2

# Max-Heap — juste en inversant le comparateur !
max_heap: Heap[int] = Heap(comparator=lambda a, b: a > b)
max_heap.insert(5)
max_heap.insert(2)
max_heap.insert(8)
print(max_heap.peek())      # 8
```

#### Pattern 2 : Heap de Tuples (Dijkstra-style)

```python
# Tuple (distance, node_id) — trier par distance croissante
graph_heap: Heap[tuple[int, int]] = Heap(
    comparator=lambda a, b: a[0] < b[0]   # compare sur la distance
)

graph_heap.insert((5, 'A'))
graph_heap.insert((1, 'B'))
graph_heap.insert((3, 'C'))

print(graph_heap.extract())   # (1, 'B')  → nœud le plus proche
print(graph_heap.extract())   # (3, 'C')
print(graph_heap.extract())   # (5, 'A')
```

#### Pattern 3 : Heap d'Objets Custom

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    priority: int
    name:     str

    def __repr__(self) -> str:
        return f"Task(priority={self.priority}, name='{self.name}')"

# Min-Heap sur la priorité (priorité 1 = plus urgente)
task_heap: Heap[Task] = Heap(
    comparator=lambda a, b: a.priority < b.priority
)

task_heap.insert(Task(priority=3, name="Send email"))
task_heap.insert(Task(priority=1, name="Fix prod bug"))
task_heap.insert(Task(priority=2, name="Code review"))

print(task_heap.extract())   # Task(priority=1, name='Fix prod bug')
print(task_heap.extract())   # Task(priority=2, name='Code review')
print(task_heap.extract())   # Task(priority=3, name='Send email')
```

#### Pattern 4 : Critère de Tri Complexe (multi-clé)

```python
# Cas classique d'interview : trier par fréquence décroissante,
# puis alphabétiquement en cas d'égalité
from typing import Tuple

Word = Tuple[int, str]   # (fréquence, mot)

# Max fréquence, puis ordre alpha sur le mot
word_heap: Heap[Word] = Heap(
    comparator=lambda a, b: (a[0] > b[0]) or (a[0] == b[0] and a[1] < b[1])
)

word_heap.insert((3, "apple"))
word_heap.insert((5, "banana"))
word_heap.insert((3, "cherry"))   # même fréquence que apple → ordre alpha
word_heap.insert((1, "date"))

print(word_heap.extract())   # (5, 'banana')
print(word_heap.extract())   # (3, 'apple')   ← alpha avant cherry
print(word_heap.extract())   # (3, 'cherry')
print(word_heap.extract())   # (1, 'date')
```

#### Pattern 5 : Factory Functions (clean API)

```python
# Au lieu de répéter le comparateur partout,
# on crée des factory functions réutilisables

def min_heap() -> Heap[int]:
    return Heap(comparator=lambda a, b: a < b)

def max_heap() -> Heap[int]:
    return Heap(comparator=lambda a, b: a > b)

def min_heap_by_first() -> Heap[tuple]:
    """Min-Heap sur le premier élément du tuple — utile pour Dijkstra."""
    return Heap(comparator=lambda a, b: a[0] < b[0])

def max_heap_by_first() -> Heap[tuple]:
    """Max-Heap sur le premier élément du tuple — utile pour Top-K."""
    return Heap(comparator=lambda a, b: a[0] > b[0])

# Usage propre
pq = min_heap_by_first()
pq.insert((10, 'node_A'))
pq.insert((2,  'node_B'))
pq.insert((7,  'node_C'))
print(pq.extract())   # (2, 'node_B')
```

### Résumé

```
Heap générique = Min-Heap + un paramètre comparator: (T, T) -> bool

comparator(a, b) = True  →  a monte au-dessus de b

Min-Heap    → lambda a, b: a < b
Max-Heap    → lambda a, b: a > b
Sur tuple   → lambda a, b: a[0] < b[0]
Multi-clé   → lambda a, b: (a[0] > b[0]) or (a[0] == b[0] and a[1] < b[1])

_has_priority(i, j) encapsule le comparateur
→ heapify_up et heapify_down ne changent pas, ils appellent juste _has_priority
```

Parfait, plan mis à jour :

| Module | Sujet                                   | Statut      |
| ------ | --------------------------------------- | ----------- |
| 1      | Théorie & Fondamentaux                  | ✅ Done     |
| 2      | Implémentations from Scratch            | 🔄 En cours |
| 3      | `heapq` — La librairie Python           | ⏳          |
| **4**  | **Priority Queue + IPQ — Module Dédié** | ⏳          |
| 5      | Patterns d'Interview (6 patterns)       | ⏳          |
| 6      | LeetCode Classiques                     | ⏳          |
| 7      | Variantes Avancées                      | ⏳          |

**Reste du Module 2 :**

|     | Sujet            | Statut  |
| --- | ---------------- | ------- |
| 2.4 | **K-ary Heap**   | ⏳ Next |
| 2.5 | **Min-Max Heap** | ⏳      |

---

## 3. **K-ary Heap:**

### Qu'est-ce qu'un K-ary Heap ?

Un **K-ary Heap** est une généralisation du heap binaire où chaque noeud a **K enfants** au lieu de 2.

```
Binary Heap (K=2) :        Ternary Heap (K=3) :
        1                          1
       / \                       / | \
      3   2                     3  2  4
     / \ / \                  /|\ /|\
    7  8 5  6                9 8 7 6 5 11
```

### Formules Généralisées

Pour un nœud à l'index `i` dans un **K-ary heap** :

```
Parent         → (i - 1) // K
j-ième enfant  → K*i + j + 1    pour j in [0, K-1]

Exemple K=3, i=1 :
    Parent      = (1-1)//3 = 0
    Enfant 0    = 3*1 + 0 + 1 = 4
    Enfant 1    = 3*1 + 1 + 1 = 5
    Enfant 2    = 3*1 + 2 + 1 = 6
```

### Complexités vs Binary Heap

| Opération                | Binary (K=2)  | K-ary          |
| ------------------------ | ------------- | -------------- |
| `insert` (heapify_up)    | O(log₂ n)     | O(log_K n)     |
| `extract` (heapify_down) | O(2 · log₂ n) | O(K · log_K n) |
| `decrease_key`           | O(log₂ n)     | O(log_K n)     |

**Trade-off clé :**

- Arbre plus **large** → moins de niveaux → heapify_up plus rapide
- Mais heapify_down doit scanner **K enfants** à chaque niveau → plus lent

**Quand utiliser K > 2 ?**

- Quand `insert` et `decrease_key` sont fréquents vs `extract` → ex: Dijkstra avec beaucoup de relaxations
- K=4 est souvent optimal en pratique (cache locality)

### Implémentation

```python
from typing import List, Optional

class KaryHeap:
    """
    Min K-ary Heap : chaque nœud a exactement K enfants.

    Formules :
        Parent(i)       = (i - 1) // k
        j-ième enfant   = k*i + j + 1   pour j in [0, k-1]
    """

    def __init__(self, k: int = 2) -> None:
        if k < 2:
            raise ValueError("K must be >= 2")
        self._k:    int       = k
        self._data: List[int] = []

    # ─────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────

    def _parent(self, i: int) -> int:
        return (i - 1) // self._k

    def _children(self, i: int) -> List[int]:
        """
        Retourne les indices de tous les enfants valides de i.
        j-ième enfant = k*i + j + 1, pour j in [0, k-1]
        """
        start: int = self._k * i + 1
        end:   int = start + self._k                  # exclusif
        return [c for c in range(start, end) if c < len(self._data)]

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # ─────────────────────────────────────────────
    # LECTURE
    # ─────────────────────────────────────────────

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    # ─────────────────────────────────────────────
    # INSERT — O(log_K n)
    # ─────────────────────────────────────────────

    def insert(self, val: int) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def _heapify_up(self, i: int) -> None:
        """
        Remonte i tant que i < parent.
        Moins de niveaux qu'un binary heap → plus rapide.
        """
        while i > 0:
            p: int = self._parent(i)
            if self._data[i] < self._data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    # ─────────────────────────────────────────────
    # EXTRACT MIN — O(K · log_K n)
    # ─────────────────────────────────────────────

    def extract_min(self) -> int:
        if self.is_empty():
            raise IndexError("Heap is empty")

        min_val: int = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()

        if not self.is_empty():
            self._heapify_down(0)

        return min_val

    def _heapify_down(self, i: int) -> None:
        """
        Descend i en swappant avec le plus petit de ses K enfants.
        À chaque niveau : scan de K enfants → O(K) par niveau.
        Nombre de niveaux : log_K n
        Total : O(K · log_K n)
        """
        while True:
            children: List[int] = self._children(i)

            if not children:           # nœud feuille → stop
                break

            # trouve le plus petit enfant parmi les K
            smallest: int = min(children, key=lambda c: self._data[c])

            if self._data[i] > self._data[smallest]:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    # ─────────────────────────────────────────────
    # BUILD HEAP — O(n)
    # ─────────────────────────────────────────────

    @classmethod
    def from_list(cls, values: List[int], k: int = 2) -> "KaryHeap":
        """
        Floyd's algorithm adapté au K-ary heap.
        Dernier nœud interne = parent du dernier élément
                             = (n - 2) // k
        """
        heap = cls(k)
        heap._data = list(values)
        n: int = len(heap._data)

        for i in range((n - 2) // k, -1, -1):
            heap._heapify_down(i)

        return heap

    def __repr__(self) -> str:
        return f"KaryHeap(k={self._k}, data={self._data})"

    def display(self) -> None:
        """Affiche niveau par niveau."""
        if self.is_empty():
            print("Heap vide")
            return

        i:          int = 0
        level:      int = 0
        level_size: int = 1          # niveau 0 a 1 nœud

        while i < len(self._data):
            end: int = min(i + level_size, len(self._data))
            print(f"Level {level}: {self._data[i:end]}")
            i          += level_size
            level_size *= self._k    # chaque niveau a K fois plus de nœuds
            level      += 1
```

### Trace d'exécution

```python
# ── Ternary Heap (K=3) ────────────────────────
h = KaryHeap(k=3)
h.insert(10)   # [10]
h.insert(5)    # [10, 5] → heapify_up: 5 < 10, swap → [5, 10]
h.insert(8)    # [5, 10, 8] → 8 > parent(5), ok
h.insert(2)    # [5, 10, 8, 2] → heapify_up: 2 < parent(5), swap → [2, 10, 8, 5]
h.insert(7)    # [2, 10, 8, 5, 7] → 7 > parent(2), ok
h.insert(1)    # [2, 10, 8, 5, 7, 1] → heapify_up: 1 < parent(2), swap → [1, 10, 8, 5, 7, 2]

h.display()
# Level 0: [1]           ← racine
# Level 1: [10, 8, 5]    ← 3 enfants de la racine
# Level 2: [7, 2]        ← enfants de 10

print(h.extract_min())   # 1
# Étape 1 : data[0] = 2 (dernier) → [2, 10, 8, 5, 7]
# heapify_down(0): children=[10,8,5], smallest=5 (index 2)
# 2 < 5, stop !
# → [2, 10, 8, 5, 7]  ✓ heap property maintenue

# ── Build from list ───────────────────────────
h2 = KaryHeap.from_list([9, 4, 7, 1, 8, 3, 2, 6, 5], k=3)
print(h2)
# KaryHeap(k=3, data=[1, 4, 2, 9, 8, 3, 7, 6, 5])

print(h2.peek())   # 1
```

### Comparaison visuelle Binary vs Ternary pour n=9

```
Binary (K=2), hauteur = 3 :      Ternary (K=3), hauteur = 2 :
           1                               1
          / \                           /  |  \
         3   2                         3   2   4
        /\ /\ /\                      /|\ /|\
       7 8 5 6 9                     9 8 7 6 5 11

heapify_up   : 3 niveaux            heapify_up   : 2 niveaux  ✓ plus rapide
heapify_down : 3 niveaux × 2       heapify_down : 2 niveaux × 3
             = 6 comparaisons                    = 6 comparaisons  ≈ pareil
```

### Résumé

```
K-ary Heap = Binary Heap généralisé à K enfants

Parent(i)      = (i - 1) // K
j-ième enfant  = K*i + j + 1

↑ Plus K est grand :
    heapify_up   → PLUS RAPIDE  (moins de niveaux)
    heapify_down → PLUS LENT    (plus d'enfants à scanner)

Cas pratiques :
    K=2  → Binary Heap classique
    K=4  → optimal pour cache locality (une cache line = 4 enfants)
    K=∞  → dégénère en tableau trié
```

# 4. **Min-Max Heap**

### Qu'est-ce qu'un Min-Max Heap ?

Un **Min-Max Heap** est un heap qui supporte à la fois `get_min` et `get_max` en **O(1)**, et `extract_min` et `extract_max` en **O(log n)**.

Un heap classique ne peut faire qu'un des deux. Le Min-Max Heap résout ça avec une structure à **niveaux alternés** :

```
Niveau 0 (MIN) :              1          ← minimum global
                            /   \
Niveau 1 (MAX) :          11     9       ← maximum global (un des deux)
                         / \   / \
Niveau 2 (MIN) :        2   4 8   3      ← minimums locaux
                       /\ /\
Niveau 3 (MAX) :      5 6 7 10           ← maximums locaux
```

**Règle fondamentale :**

- Niveau **pair** (0, 2, 4...) → **MIN level** : chaque nœud est ≤ à tous ses descendants
- Niveau **impair** (1, 3, 5...) → **MAX level** : chaque nœud est ≥ à tous ses descendants

### Propriétés Clés

```
Min global → toujours à la racine (index 0)
Max global → toujours parmi les enfants de la racine (index 1 ou 2)

peek_min → O(1)  : data[0]
peek_max → O(1)  : max(data[1], data[2])
extract_min → O(log n)
extract_max → O(log n)
insert      → O(log n)
```

### Implémentation

```python
from typing import List, Optional
import math

class MinMaxHeap:
    """
    Min-Max Heap : supporte get_min et get_max en O(1).

    Structure : niveaux alternés MIN/MAX.
        Niveau pair  → MIN : nœud ≤ tous ses descendants
        Niveau impair → MAX : nœud ≥ tous ses descendants

    Représentation en tableau identique au heap classique :
        Parent(i)      = (i - 1) // 2
        Left child(i)  = 2*i + 1
        Right child(i) = 2*i + 2
    """

    def __init__(self) -> None:
        self._data: List[int] = []

    # ─────────────────────────────────────────────
    # HELPERS — Niveau et Type de Niveau
    # ─────────────────────────────────────────────

    def _level(self, i: int) -> int:
        """
        Retourne le niveau de l'index i.
        Niveau 0 = racine, niveau 1 = enfants de la racine, etc.

        level(i) = floor(log2(i + 1))
        """
        return int(math.log2(i + 1))

    def _is_min_level(self, i: int) -> bool:
        """Niveau pair → MIN level."""
        return self._level(i) % 2 == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _grandparent(self, i: int) -> Optional[int]:
        if i < 3:               # pas de grand-parent pour index 0,1,2
            return None
        return (i - 3) // 4    # (i-1)//2 → parent, puis (parent-1)//2

    def _children(self, i: int) -> List[int]:
        n: int = len(self._data)
        kids: List[int] = []
        if 2*i + 1 < n: kids.append(2*i + 1)
        if 2*i + 2 < n: kids.append(2*i + 2)
        return kids

    def _grandchildren(self, i: int) -> List[int]:
        result: List[int] = []
        for c in self._children(i):
            result.extend(self._children(c))
        return result

    def _children_and_grandchildren(self, i: int) -> List[int]:
        return self._children(i) + self._grandchildren(i)

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # ─────────────────────────────────────────────
    # LECTURE — O(1)
    # ─────────────────────────────────────────────

    def peek_min(self) -> int:
        """Minimum = toujours à la racine."""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def peek_max(self) -> int:
        """
        Maximum = parmi les enfants de la racine (niveau MAX).
        Si un seul élément → c'est aussi le max.
        Si deux éléments → max(data[1], data[2]).
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        n: int = len(self._data)
        if n == 1: return self._data[0]
        if n == 2: return self._data[1]
        return max(self._data[1], self._data[2])

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    # ─────────────────────────────────────────────
    # INSERT — O(log n)
    # ─────────────────────────────────────────────

    def insert(self, val: int) -> None:
        """
        1. Ajoute val à la fin
        2. push_up : compare avec parent pour déterminer
           si on est sur un min ou max level, puis remonte
        """
        self._data.append(val)
        self._push_up(len(self._data) - 1)

    def _push_up(self, i: int) -> None:
        """
        Remonte l'élément à i selon la propriété min-max.

        Cas 1 : niveau MIN
            Compare avec parent (MAX level)
            Si val > parent → swap, puis push_up_max depuis parent
            Sinon           → push_up_min depuis i

        Cas 2 : niveau MAX
            Compare avec parent (MIN level)
            Si val < parent → swap, puis push_up_min depuis parent
            Sinon           → push_up_max depuis i
        """
        if i == 0:
            return                          # racine, rien à faire

        p: int = self._parent(i)

        if self._is_min_level(i):
            if self._data[i] > self._data[p]:
                self._swap(i, p)
                self._push_up_max(p)        # maintenant sur un MAX level
            else:
                self._push_up_min(i)
        else:
            if self._data[i] < self._data[p]:
                self._swap(i, p)
                self._push_up_min(p)        # maintenant sur un MIN level
            else:
                self._push_up_max(i)

    def _push_up_min(self, i: int) -> None:
        """Remonte i sur les niveaux MIN (saute les niveaux MAX)."""
        gp: Optional[int] = self._grandparent(i)
        if gp is not None and self._data[i] < self._data[gp]:
            self._swap(i, gp)
            self._push_up_min(gp)

    def _push_up_max(self, i: int) -> None:
        """Remonte i sur les niveaux MAX (saute les niveaux MIN)."""
        gp: Optional[int] = self._grandparent(i)
        if gp is not None and self._data[i] > self._data[gp]:
            self._swap(i, gp)
            self._push_up_max(gp)

    # ─────────────────────────────────────────────
    # EXTRACT MIN — O(log n)
    # ─────────────────────────────────────────────

    def extract_min(self) -> int:
        """
        1. Sauvegarde data[0] (minimum)
        2. Met le dernier élément à la racine
        3. push_down depuis la racine (MIN level)
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        min_val: int = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()

        if not self.is_empty():
            self._push_down(0)

        return min_val

    # ─────────────────────────────────────────────
    # EXTRACT MAX — O(log n)
    # ─────────────────────────────────────────────

    def extract_max(self) -> int:
        """
        1. Trouve l'index du maximum (parmi data[1], data[2])
        2. Swap avec le dernier
        3. Pop le dernier
        4. push_down depuis l'index du max
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        n: int = len(self._data)

        if n == 1:
            return self._data.pop()

        # index du maximum : parmi les enfants de la racine
        max_idx: int = 1
        if n > 2 and self._data[2] > self._data[1]:
            max_idx = 2

        max_val: int = self._data[max_idx]
        self._data[max_idx] = self._data[-1]
        self._data.pop()

        if max_idx < len(self._data):
            self._push_down(max_idx)

        return max_val

    # ─────────────────────────────────────────────
    # PUSH DOWN — O(log n)
    # ─────────────────────────────────────────────

    def _push_down(self, i: int) -> None:
        """Délègue à push_down_min ou push_down_max selon le niveau."""
        if self._is_min_level(i):
            self._push_down_min(i)
        else:
            self._push_down_max(i)

    def _push_down_min(self, i: int) -> None:
        """
        Sur un MIN level : i doit être ≤ tous ses descendants.
        Trouve le plus petit parmi enfants ET petits-enfants.

        Cas 1 : le plus petit est un petit-enfant (index m)
            Si data[m] < data[i] → swap
            Si data[m] > data[parent(m)] → swap avec parent(m) aussi
            Continuer push_down_min depuis m

        Cas 2 : le plus petit est un enfant direct
            Si data[m] < data[i] → swap (fin, enfant direct = feuille relative)
        """
        descendants: List[int] = self._children_and_grandchildren(i)
        if not descendants:
            return

        m: int = min(descendants, key=lambda x: self._data[x])

        # m est-il un petit-enfant ?
        is_grandchild: bool = m not in self._children(i)

        if is_grandchild:
            if self._data[m] < self._data[i]:
                self._swap(m, i)
                p: int = self._parent(m)
                if self._data[m] > self._data[p]:
                    self._swap(m, p)
                self._push_down_min(m)
        else:
            if self._data[m] < self._data[i]:
                self._swap(m, i)

    def _push_down_max(self, i: int) -> None:
        """
        Sur un MAX level : i doit être ≥ tous ses descendants.
        Symétrique à push_down_min avec les inégalités inversées.
        """
        descendants: List[int] = self._children_and_grandchildren(i)
        if not descendants:
            return

        m: int = max(descendants, key=lambda x: self._data[x])

        is_grandchild: bool = m not in self._children(i)

        if is_grandchild:
            if self._data[m] > self._data[i]:
                self._swap(m, i)
                p: int = self._parent(m)
                if self._data[m] < self._data[p]:
                    self._swap(m, p)
                self._push_down_max(m)
        else:
            if self._data[m] > self._data[i]:
                self._swap(m, i)

    # ─────────────────────────────────────────────
    # BUILD HEAP — O(n)
    # ─────────────────────────────────────────────

    @classmethod
    def from_list(cls, values: List[int]) -> "MinMaxHeap":
        heap = cls()
        heap._data = list(values)
        n: int = len(heap._data)

        for i in range((n - 2) // 2, -1, -1):
            heap._push_down(i)

        return heap

    def __repr__(self) -> str:
        return f"MinMaxHeap({self._data})"

    def display(self) -> None:
        if self.is_empty():
            print("Heap vide")
            return

        i:          int = 0
        level:      int = 0
        level_size: int = 1

        while i < len(self._data):
            end:       int = min(i + level_size, len(self._data))
            level_type: str = "MIN" if level % 2 == 0 else "MAX"
            print(f"Level {level} ({level_type}): {self._data[i:end]}")
            i          += level_size
            level_size *= 2
            level      += 1
```

### Trace d'exécution

```python
h = MinMaxHeap()
for val in [5, 3, 8, 1, 9, 2, 7, 4, 6]:
    h.insert(val)

h.display()
# Level 0 (MIN): [1]          ← minimum global
# Level 1 (MAX): [9, 8]       ← maximum global = 9
# Level 2 (MIN): [3, 4, 2, 7] ← minimums locaux
# Level 3 (MAX): [5, 6]       ← maximums locaux

print(h.peek_min())    # 1  — O(1)
print(h.peek_max())    # 9  — O(1)

print(h.extract_min()) # 1
print(h.extract_max()) # 9
print(h.peek_min())    # 2
print(h.peek_max())    # 8

# Build from list
h2 = MinMaxHeap.from_list([9, 4, 7, 1, 8, 3, 2])
h2.display()
# Level 0 (MIN): [1]
# Level 1 (MAX): [9, 7]
# Level 2 (MIN): [4, 8, 3, 2]
```

### Résumé

```
Min-Max Heap = Heap à niveaux alternés MIN/MAX

Niveau pair  (0,2,4...) → MIN : nœud ≤ tous ses descendants
Niveau impair(1,3,5...) → MAX : nœud ≥ tous ses descendants

peek_min    → O(1) : data[0]
peek_max    → O(1) : max(data[1], data[2])
insert      → O(log n) : push_up (compare avec parent puis grand-parent)
extract_min → O(log n) : push_down_min depuis racine
extract_max → O(log n) : push_down_max depuis index 1 ou 2

Cas d'usage : Median Maintenance, Double-ended PQ,
              Sliding window min ET max simultanément
```
