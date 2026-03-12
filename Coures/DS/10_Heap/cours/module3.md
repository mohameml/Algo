# Module 3 : `heapq`

## 1. **Introduction:**

### Qu'est-ce que `heapq` ?

`heapq` est un module de la **librairie standard Python** qui implémente un heap binaire Min-Heap. La différence fondamentale avec notre implémentation : **ce n'est pas une classe**.

`heapq` est une collection de **fonctions** qui opèrent directement sur une **liste Python ordinaire**.

```python
import heapq

# Pas de classe, pas d'objet Heap
# Juste une liste normale + des fonctions

heap: list[int] = []              # c'est juste une liste !
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heap)          # [2, 5, 8]  ← liste ordonnée comme un heap
print(type(heap))    # <class 'list'>
```

La liste `heap` est une liste Python ordinaire — tu peux faire `heap[0]`, `len(heap)`, etc. `heapq` garantit simplement que cette liste respecte la **heap property** tant que tu utilises ses fonctions.

### RQ : Heap Property garantie par `heapq`

Tant que tu utilises **uniquement les fonctions `heapq`** pour modifier la liste, la heap property est garantie :

```python
heap = []
heapq.heappush(heap, 5)    # ✅ heap property maintenue
heapq.heappush(heap, 2)    # ✅
heapq.heappush(heap, 8)    # ✅
print(heap[0])              # 2 — minimum garanti

# ⚠️ DANGER : modifier la liste directement casse la heap property
heap.append(1)              # ❌ heap property potentiellement cassée !
heap[0] = 99               # ❌ catastrophe
heap.sort()                # ❌ ce n'est plus un heap

# ✅ RÈGLE : ne jamais modifier la liste autrement qu'avec heapq
```

### Exemple :

```python
import heapq

# ── Création ──────────────────────────────────
heap: list[int] = []

# ── Insert ────────────────────────────────────
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 9)

print(heap)              # [1, 2, 8, 5, 9]
                         # ← pas trié ! juste heap property garantie

# ── Peek — O(1) ───────────────────────────────
print(heap[0])           # 1 — minimum

# ── Extract min — O(log n) ────────────────────
print(heapq.heappop(heap))   # 1
print(heapq.heappop(heap))   # 2
print(heapq.heappop(heap))   # 5

# ── Build from list — O(n) ────────────────────
data = [9, 4, 7, 1, 8, 3, 2]
heapq.heapify(data)
print(data)              # [1, 3, 2, 4, 8, 7, 9]
print(data[0])           # 1 — minimum garanti
```

## 2. **Les 8 Fonctions Fondamentales:**

- `heappushpop(heap, item)` — O(log n)

    Push puis pop **atomiquement**. Plus efficace que les deux séparément.

    ```python
    heap = [2, 5, 8]
    heapq.heapify(heap)

    # Équivalent à heappush puis heappop, mais en une seule opération
    result = heapq.heappushpop(heap, 1)
    print(result)    # 1  ← item inséré était le plus petit, retourné immédiatement
    print(heap)      # [2, 5, 8]  ← heap inchangé

    result = heapq.heappushpop(heap, 3)
    print(result)    # 2  ← ancien minimum
    print(heap)      # [3, 5, 8]
    ```

    **Règle :** si `item <= heap[0]` → retourne `item` directement sans modifier le heap.

- `heapreplace(heap, item)` — O(log n)

    Pop puis push **atomiquement**. Le heap ne peut pas être vide.

    ```python
    heap = [1, 5, 8]

    result = heapq.heapreplace(heap, 3)
    print(result)    # 1  ← ancien minimum, toujours retourné
    print(heap)      # [3, 5, 8]

    result = heapq.heapreplace(heap, 99)
    print(result)    # 3
    print(heap)      # [5, 99, 8]  → [5, 8, 99] après heapify_down
    ```

- `heappushpop` vs `heapreplace` — La différence clé

    ```
    heappushpop(heap, x) :
        → compare x avec heap[0] d'abord
        → si x <= heap[0] : retourne x, heap inchangé
        → sinon : pop min, push x
        → peut retourner x lui-même

    heapreplace(heap, x) :
        → pop min TOUJOURS, puis push x
        → retourne toujours l'ancien minimum
        → heap ne peut pas être vide
        → légèrement plus rapide (pas de comparaison initiale)
    ```

- `nlargest(n, iterable, key=None)` — O(m log n)

    Retourne les **n plus grands** éléments. `m = len(iterable)`.

    ```python
    data = [3, 1, 9, 4, 7, 2, 8]

    print(heapq.nlargest(3, data))     # [9, 8, 7]

    # Avec key
    words = ["banana", "fig", "apple", "kiwi"]
    print(heapq.nlargest(2, words, key=len))    # ['banana', 'apple']
    ```

- `nsmallest(n, iterable, key=None)` — O(m log n)

    Retourne les **n plus petits** éléments.

    ```python
    data = [3, 1, 9, 4, 7, 2, 8]

    print(heapq.nsmallest(3, data))    # [1, 2, 3]

    # Avec key sur des tuples
    tasks = [(3, "email"), (1, "bug"), (2, "review")]
    print(heapq.nsmallest(2, tasks, key=lambda x: x[0]))
    # [(1, 'bug'), (2, 'review')]
    ```

- **All functions:**

| Fonction      | Complexité | Syntaxe                                | Usage                                               |
| ------------- | ---------- | -------------------------------------- | --------------------------------------------------- |
| `heappush`    | O(log n)   | `heapq.heappush(heap, item)`           | Insérer un élément                                  |
| `heappop`     | O(log n)   | `heapq.heappop(heap)`                  | Extraire le minimum                                 |
| `heapify`     | O(n)       | `heapq.heapify(list)`                  | Construire depuis une liste in-place                |
| `heappushpop` | O(log n)   | `heapq.heappushpop(heap, item)`        | Push + pop atomique, peut retourner `item`          |
| `heapreplace` | O(log n)   | `heapq.heapreplace(heap, item)`        | Pop + push atomique, retourne toujours l'ancien min |
| `nlargest`    | O(m log n) | `heapq.nlargest(n, iterable, key=fn)`  | Top-K plus grands éléments                          |
| `nsmallest`   | O(m log n) | `heapq.nsmallest(n, iterable, key=fn)` | Top-K plus petits éléments                          |
| `merge`       | O(m log k) | `heapq.merge(*iterables, key=fn)`      | Fusionner K listes triées (lazy generator)          |

## 3. **Simuler un Custom Heap:**

> `heapq` est uniquement un Min-Heap. Pour simuler un Max-Heap, il y a **3 techniques**.

### Technique 1 : Négation `-val` (integers/floats)

```python
import heapq

max_heap: list[int] = []

# Insert → nég le val
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

# Peek max → nég heap[0]
print(-max_heap[0])    # 8

# Extract max → nég le résultat
print(-heapq.heappop(max_heap))    # 8
print(-heapq.heappop(max_heap))    # 5
print(-heapq.heappop(max_heap))    # 2
```

### Technique 2 : Tuples `(-priority, value)` (cas réel d'interview)

Quand les éléments sont des objets ou strings, on ne peut pas juste les néger. On utilise un tuple où le premier élément est la priorité négée.

```python
max_heap: list[tuple[int, str]] = []

heapq.heappush(max_heap, (-3, "email"))
heapq.heappush(max_heap, (-1, "bug"))
heapq.heappush(max_heap, (-2, "review"))

# Extract par priorité décroissante
priority, task = heapq.heappop(max_heap)
print(task, -priority)    # email 3  ← priorité la plus haute d'abord
```

### Technique 3 : `__lt__` sur un objet custom

Pour des objets complexes, on définit `__lt__` avec l'ordre inversé.

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    priority: int
    name:     str

    def __lt__(self, other: "Task") -> bool:
        return self.priority > other.priority    # inversé → Max-Heap

max_heap: list[Task] = []
heapq.heappush(max_heap, Task(1, "bug"))
heapq.heappush(max_heap, Task(3, "email"))
heapq.heappush(max_heap, Task(2, "review"))

print(heapq.heappop(max_heap))    # Task(priority=3, name='email')
print(heapq.heappop(max_heap))    # Task(priority=2, name='review')
```

### RQ Piège classique : `heapify` avec négation

```python
data = [3, 1, 9, 4, 7]

# ❌ FAUX — heapify sur data ne fait pas un max-heap
heapq.heapify(data)

# ✅ CORRECT — néger d'abord, puis heapify
data = [-x for x in data]
heapq.heapify(data)
print(-data[0])    # 9 — maximum correct
```
