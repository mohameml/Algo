# Module 3.5 — Patterns Idiomatiques Python

## Pattern 1 : Lazy Deletion

`heapq` n'a pas de `delete` natif. La solution standard : **marquer les éléments comme supprimés** sans les retirer physiquement du heap.

```python
import heapq

class LazyHeap:
    """
    Min-Heap avec suppression lazy.
    Les éléments supprimés restent dans le heap mais sont ignorés au pop.
    """
    def __init__(self) -> None:
        self._heap:    list[tuple]  = []
        self._removed: set          = set()    # éléments marqués supprimés

    def push(self, val: int) -> None:
        heapq.heappush(self._heap, val)

    def remove(self, val: int) -> None:
        self._removed.add(val)                 # O(1) — juste un marquage

    def pop(self) -> int:
        # skip les éléments supprimés
        while self._heap and self._heap[0] in self._removed:
            self._removed.remove(self._heap[0])
            heapq.heappop(self._heap)
        if not self._heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self._heap)

    def peek(self) -> int:
        while self._heap and self._heap[0] in self._removed:
            self._removed.remove(self._heap[0])
            heapq.heappop(self._heap)
        return self._heap[0]


# Usage
h = LazyHeap()
h.push(1); h.push(3); h.push(2); h.push(5)
h.remove(2)               # marque 2 comme supprimé
print(h.pop())            # 1
print(h.pop())            # 3  ← 2 est skippé
```

---

## Pattern 2 : Top-K avec Counter

Pattern ultra classique en interview : **K éléments les plus fréquents**.

```python
import heapq
from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)                          # O(n)

    # nsmallest sur un Min-Heap de taille k
    # key = fréquence
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_frequent([1,1,1,2,2,3], k=2))    # [1, 2]
print(top_k_frequent([4,4,2,2,2,3], k=2))    # [2, 4]
```

Version manuelle avec heap de taille fixe K — plus efficace quand `k << n` :

```python
def top_k_frequent_manual(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    heap:  list[tuple[int, int]] = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)         # éjecte le moins fréquent

    return [num for freq, num in heap]  # O(k log k) au total
```

---

## Pattern 3 : K-way Merge

Fusionner K listes triées — pattern fondamental pour le external sorting et les interviews.

```python
import heapq
from typing import List

def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    heap:   list[tuple[int, int, int]] = []   # (val, list_idx, elem_idx)
    result: List[int]                  = []

    # initialise avec le premier élément de chaque liste
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result

lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge_k_sorted(lists))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Pattern 4 : Median Maintenance (Two Heaps)

Maintenir la médiane dynamiquement avec deux heaps — un des patterns les plus classiques.

```python
import heapq

class MedianFinder:
    """
    Two Heaps pattern :
        lower  → Max-Heap : moitié inférieure des éléments
        upper  → Min-Heap : moitié supérieure des éléments

    Invariant : len(lower) == len(upper) ou len(lower) == len(upper) + 1
    """
    def __init__(self) -> None:
        self._lower: list[int] = []    # Max-Heap (valeurs négées)
        self._upper: list[int] = []    # Min-Heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self._lower, -num)           # push dans Max-Heap

        # équilibre : lower max <= upper min
        if self._lower and self._upper and (-self._lower[0] > self._upper[0]):
            heapq.heappush(self._upper, -heapq.heappop(self._lower))

        # équilibre des tailles
        if len(self._lower) > len(self._upper) + 1:
            heapq.heappush(self._upper, -heapq.heappop(self._lower))
        elif len(self._upper) > len(self._lower):
            heapq.heappush(self._lower, -heapq.heappop(self._upper))

    def find_median(self) -> float:
        if len(self._lower) > len(self._upper):
            return -self._lower[0]
        return (-self._lower[0] + self._upper[0]) / 2


mf = MedianFinder()
for num in [5, 3, 8, 1, 9]:
    mf.add_num(num)
    print(mf.find_median())    # 5, 4.0, 5, 4.0, 5
```

---

## Résumé des 4 Patterns

```
Lazy Deletion      → set de supprimés + skip au pop
Top-K Fréquences   → Counter + nlargest ou heap taille fixe K
K-way Merge        → heap de (val, list_idx, elem_idx)
Median Maintenance → Max-Heap lower + Min-Heap upper
```

---

On passe à **3.6 — Complexités & Comparaison** ?
