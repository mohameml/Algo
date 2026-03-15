# Module 2 — Doubly Linked List

## 1. Définition

> Une **Doubly Linked List** (DLL) est une liste chaînée où chaque nœud contient une valeur, un pointeur vers le nœud **suivant** (`next`) et un pointeur vers le nœud **précédent** (`prev`).

```
None ← [prev|val|next] ⇄ [prev|val|next] ⇄ [prev|val|next] → None
         head                                     tail
```

- Structure d'un nœud :

    ```python
    class DListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next
    ```

- Avantages par rapport à la SLL:
    - Traversal dans les deux directions
    - Suppression d'un nœud en O(1) **sans connaître le prédécesseur** (car on a `prev`)
    - Insert before/after un nœud en O(1)

- Inconvénients:
    - Plus de mémoire par nœud (pointeur `prev` supplémentaire)
    - Code plus complexe (maintenir deux pointeurs)

## 2. Implémentation from scratch

> On utilise des **sentinel nodes** (dummy head et dummy tail) pour simplifier les edge cases. Tous les inserts/deletes se font entre les sentinels.

```python
class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()  # sentinel head
        self.tail = DListNode()  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # --- Internal helpers ---

    def _insert_between(self, val, pred, succ):
        """Insert a new node with val between pred and succ."""
        new_node = DListNode(val, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def _remove_node(self, node):
        """Remove node from the list (node must not be a sentinel)."""
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return node.val

    # --- Insert ---

    def insert_head(self, val):
        return self._insert_between(val, self.head, self.head.next)

    def insert_tail(self, val):
        return self._insert_between(val, self.tail.prev, self.tail)

    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return self._insert_between(val, curr.prev, curr)

    # --- Delete ---

    def delete_head(self):
        if self.is_empty():
            raise IndexError("Delete from empty list")
        return self._remove_node(self.head.next)

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("Delete from empty list")
        return self._remove_node(self.tail.prev)

    def delete_node(self, node):
        """Remove a specific node in O(1) — the key advantage of DLL."""
        return self._remove_node(node)

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return self._remove_node(curr)

    # --- Search ---

    def search(self, val):
        curr = self.head.next
        index = 0
        while curr != self.tail:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1

    # --- Access ---

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Optimize: start from head or tail depending on index
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr.val

    # --- Traversal ---

    def to_list(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.val)
            curr = curr.next
        return result

    def to_list_reverse(self):
        result = []
        curr = self.tail.prev
        while curr != self.head:
            result.append(curr.val)
            curr = curr.prev
        return result

    def __repr__(self):
        vals = self.to_list()
        return "None <-> " + " <-> ".join(str(v) for v in vals) + " <-> None"

    @classmethod
    def from_list(cls, vals):
        dll = cls()
        for val in vals:
            dll.insert_tail(val)
        return dll
```

- **Complexity:**

    | Opération | Time | Space |
    |-----------|------|-------|
    | `insert_head` | O(1) | O(1) |
    | `insert_tail` | O(1) | O(1) |
    | `insert_at(i)` | O(i) | O(1) |
    | `delete_head` | O(1) | O(1) |
    | `delete_tail` | O(1) | O(1) |
    | `delete_node(node)` | O(1) | O(1) |
    | `delete_at(i)` | O(i) | O(1) |
    | `search` | O(n) | O(1) |
    | `get(i)` | O(min(i, n-i)) | O(1) |

    > **Key difference with SLL:** `delete_tail` est O(1) grâce au pointeur `prev`. `get(i)` est optimisé en partant du côté le plus proche.

- **Edge Cases:**
    - Liste vide — delete doit lever une exception
    - Liste à un seul élément — après delete, head.next == tail et tail.prev == head
    - Les sentinel nodes ne sont jamais supprimés
    - `get(0)` et `get(size-1)` — cas limites gérés par l'optimisation head/tail

## 3. Sentinel Nodes Pattern

> Les **sentinel nodes** (dummy head/tail) éliminent les vérifications de `None` dans les opérations d'insert/delete. C'est un pattern fondamental pour les DLL.

```
Sans sentinels (complexe) :        Avec sentinels (simple) :

None ← [A] ⇄ [B] ⇄ [C] → None    [dummy_head] ⇄ [A] ⇄ [B] ⇄ [C] ⇄ [dummy_tail]
```

- **Avantage:** Toute insertion/suppression devient un cas uniforme — on insère/supprime toujours **entre** deux nœuds existants, jamais en bordure.

- **Edge Cases éliminés par les sentinels:**
    - Insert dans une liste vide
    - Delete le seul élément
    - Insert en tête / en queue
    - Pas besoin de vérifier `if head is None` ou `if node.next is None`

## 4. Examples

### 4.1 Construire et traverser une DLL (Easy)

```python
dll = DoublyLinkedList.from_list([1, 2, 3, 4, 5])
print(dll)              # None <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None
print(dll.to_list_reverse())  # [5, 4, 3, 2, 1]

dll.insert_head(0)
dll.insert_tail(6)
print(dll)  # None <-> 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> None
```

### 4.2 Delete en O(1) avec référence directe (Easy)

```python
dll = DoublyLinkedList()
node_a = dll.insert_head(1)
node_b = dll.insert_tail(2)
node_c = dll.insert_tail(3)

# Supprimer node_b en O(1) — pas besoin de traverser
dll.delete_node(node_b)
print(dll)  # None <-> 1 <-> 3 <-> None
```

- **Key idea:** Avec une DLL, si on a une référence au nœud, on peut le supprimer en O(1) car on accède directement à `prev` et `next`. C'est la base du **LRU Cache**.
