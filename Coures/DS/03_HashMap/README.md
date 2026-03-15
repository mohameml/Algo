# Chapter : HashMap

## 1. Introduction

> Un **HashMap** (table de hachage) est une structure de données qui associe des **clés** à des **valeurs** via une **fonction de hachage**, permettant un accès en O(1) en moyenne.

- When to use / How to recognize:
    - Besoin de **lookup O(1)** par clé
    - Problèmes de **comptage / fréquence**
    - Recherche de **complément** (two sum, pair sum)
    - **Groupement** d'éléments par propriété
    - **Détection de doublons**
    - Remplacement d'une recherche O(n) par O(1)

- Propriétés clés:
    - Accès, insertion, suppression : O(1) en moyenne
    - Pas d'ordre garanti (contrairement à un array)
    - Basé sur une **fonction de hachage** : `key → index`


## 2. Complexité des Opérations

| Opération | Average | Worst Case |
|-----------|---------|-----------|
| Access by key | O(1) | O(n) |
| Search (key exists) | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

> Le worst case O(n) arrive quand toutes les clés tombent dans le même bucket (mauvaise fonction de hachage ou attaque). En pratique, c'est toujours O(1).


## 3. Collision Handling

> Une **collision** arrive quand deux clés ont le même hash. Deux stratégies principales :

### 3.1 Chaining (chaînage)

> Chaque bucket contient une **liste chaînée** de paires (key, value).

```
index 0 : → (key1, val1) → (key5, val5)
index 1 : → (key2, val2)
index 2 : → None
index 3 : → (key3, val3) → (key4, val4)
```

- **Avantage** : simple, supporte un load factor > 1
- **Inconvénient** : utilise plus de mémoire (pointeurs)

### 3.2 Open Addressing (adressage ouvert)

> En cas de collision, on cherche le prochain slot libre (linear probing, quadratic probing, double hashing).

- **Avantage** : meilleure cache locality
- **Inconvénient** : clustering, load factor doit rester < 0.7

> Python utilise **open addressing** avec du probing quadratique.


## 4. Implementation — HashMap from scratch (Chaining)

```python
class HashMap:
    """HashMap implementation using chaining."""

    def __init__(self, capacity=16):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self._size / self._capacity > 0.7:
            self._resize()

    def get(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return v
        raise KeyError(key)

    def contains(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self._size

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def __repr__(self):
        items = []
        for bucket in self._buckets:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"
```

- **Complexity:**

    | Opération | Average | Worst |
    |-----------|---------|-------|
    | `put` | O(1) | O(n) |
    | `get` | O(1) | O(n) |
    | `remove` | O(1) | O(n) |
    | `contains` | O(1) | O(n) |
    | `_resize` | O(n) | O(n) |

- **Load factor** : quand `size / capacity > 0.7`, on double la capacité et on re-hash toutes les clés.


## 5. Python dict — Méthodes essentielles

| Opération | Syntaxe | Complexité | Note |
|-----------|---------|-----------|------|
| Access | `d[key]` | O(1) | KeyError si absent |
| Get safe | `d.get(key, default)` | O(1) | retourne default si absent |
| Insert / Update | `d[key] = val` | O(1) | |
| Delete | `del d[key]` | O(1) | KeyError si absent |
| Pop | `d.pop(key, default)` | O(1) | |
| Check key | `key in d` | O(1) | |
| Keys | `d.keys()` | O(1) | vue, itérer = O(n) |
| Values | `d.values()` | O(1) | vue, itérer = O(n) |
| Items | `d.items()` | O(1) | vue, itérer = O(n) |
| Set default | `d.setdefault(key, val)` | O(1) | insert si absent |
| Update | `d.update(other)` | O(k) | k = taille de other |
| Length | `len(d)` | O(1) | |

- **`collections.defaultdict`** : dict avec valeur par défaut automatique

    ```python
    from collections import defaultdict
    d = defaultdict(list)
    d["key"].append(1)  # pas de KeyError
    ```

- **`collections.Counter`** : compteur de fréquences

    ```python
    from collections import Counter
    c = Counter([1, 2, 2, 3, 3, 3])
    # Counter({3: 3, 2: 2, 1: 1})
    c.most_common(2)  # [(3, 3), (2, 2)]
    ```


## 6. Examples

### 6.1 Frequency Count (Easy)

> **Problème** : Compter la fréquence de chaque élément dans un tableau.

```python
def frequency_count(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Test :
# nums = [1, 2, 2, 3, 3, 3]
# result = {1: 1, 2: 2, 3: 3}
```

- **Complexité** : O(n) temps, O(n) espace


### 6.2 Two Sum — HashMap approach (Easy)

> **Problème** : Trouver deux indices dont la somme = target. Approche HashMap : pour chaque élément, chercher si le complément existe déjà.

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test :
# nums = [2, 7, 11, 15], target = 9
# i=0: complement=7, seen={2:0}
# i=1: complement=2, 2 in seen → [0, 1]
```

- **Complexité** : O(n) temps, O(n) espace
- **Key idea** : stocker `{valeur: index}`, chercher le complément en O(1)


### 6.3 Group Anagrams — LC 49 (Medium)

> **Problème** : Grouper les chaînes qui sont des anagrammes les unes des autres.

```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

# Test :
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# key("eat") = ('a','e','t'), key("tea") = ('a','e','t') → même groupe
# result = [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

- **Complexité** : O(n * k log k) temps (k = longueur max d'un mot), O(n * k) espace
- **Key idea** : deux anagrammes ont la même signature quand triés → utiliser comme clé du HashMap
