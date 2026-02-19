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
