# Chapter : Array

## 1. Introduction

> Un **array** (tableau) est une structure de données qui stocke des éléments de manière **contiguë en mémoire**, accessibles par **index** en O(1).

- When to use / How to recognize:
    - Accès rapide par index
    - Données de taille connue ou dynamique (list en Python)
    - Problèmes impliquant des séquences, sous-tableaux, fenêtres glissantes
    - Itération ordonnée sur des éléments

- Propriétés clés:
    - Accès par index : O(1)
    - Mémoire contiguë → bonne **cache locality**
    - Taille fixe (array statique) ou dynamique (Python `list`)


## 2. Complexité des Opérations

| Opération | Complexité |
|-----------|-----------|
| Access by index | O(1) |
| Search | O(n) |
| Update by index | O(1) |
| Insert at end (append) | O(1) amorti |
| Insert at beginning / middle | O(n) |
| Delete at end (pop) | O(1) |
| Delete at beginning / middle | O(n) |


## 3. Implementation — DynamicArray from scratch

> Un **DynamicArray** utilise un tableau statique interne. Quand la capacité est atteinte, on alloue un nouveau tableau de taille double et on copie les éléments.

```python
class DynamicArray:
    """Dynamic array implementation from scratch."""

    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        return self._data[i]

    def __setitem__(self, i, val):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        self._data[i] = val

    def append(self, val):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = val
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Pop from empty array")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val

    def insert(self, i, val):
        if i < 0 or i > self._size:
            raise IndexError("Index out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._size, i, -1):
            self._data[j] = self._data[j - 1]
        self._data[i] = val
        self._size += 1

    def remove(self, val):
        for i in range(self._size):
            if self._data[i] == val:
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                self._data[self._size - 1] = None
                self._size -= 1
                return
        raise ValueError("Value not found")

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"
```

- **Complexity:**

    | Opération | Complexité |
    |-----------|-----------|
    | `__getitem__` / `__setitem__` | O(1) |
    | `append` | O(1) amorti |
    | `pop` | O(1) |
    | `insert` | O(n) |
    | `remove` | O(n) |
    | `_resize` | O(n) |

- **Why O(1) amorti pour append ?**
    - On double la capacité à chaque resize
    - Sur n appends : coût total des copies = 1 + 2 + 4 + ... + n ≈ 2n
    - Coût amorti par opération = 2n / n = O(1)


## 4. Key Operations & Patterns

### 4.1 Prefix Sum

> Permet de calculer la somme d'un sous-tableau `[i, j]` en O(1) après un pré-traitement O(n).

```python
def build_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix

def range_sum(prefix, i, j):
    """Somme de nums[i] à nums[j] inclus."""
    return prefix[j + 1] - prefix[i]
```

### 4.2 In-place Manipulation

> Modifier un tableau sans espace supplémentaire. Technique courante : **read/write pointers**.

```python
def remove_duplicates_sorted(nums):
    """Remove duplicates in-place from sorted array. Returns new length."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```


## 5. Examples

### 5.1 Best Time to Buy and Sell Stock — LC 121 (Easy)

> **Problème** : Tableau de prix d'un actif. Trouver le profit max en achetant puis vendant (une seule transaction).

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Test :
# prices = [7, 1, 5, 3, 6, 4]
# min_price parcourt : 7, 1, 1, 1, 1, 1
# profit parcourt :    0, 0, 4, 2, 5, 3
# result = 5 (acheter à 1, vendre à 6)
```

- **Complexité** : O(n) temps, O(1) espace
- **Key idea** : tracker le min vu jusqu'ici, calculer le profit à chaque étape


### 5.2 Maximum Subarray — Kadane's Algorithm (Medium)

> **Problème** : Trouver la plus grande somme d'un sous-tableau contigu (entiers positifs ou négatifs).

```python
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test :
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# current_sum : -2, 1, -2, 4, 3, 5, 6, 1, 5
# max_sum :     -2, 1,  1, 4, 4, 5, 6, 6, 6
# result = 6 (sous-tableau [4, -1, 2, 1])
```

- **Complexité** : O(n) temps, O(1) espace
- **Key idea** : à chaque position, soit on étend le sous-tableau courant, soit on recommence à partir de l'élément courant
