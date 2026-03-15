# Module 1 — Singly Linked List

## 1. Définition

> Une **Singly Linked List** (SLL) est une liste chaînée où chaque nœud contient une **valeur** et un **pointeur** vers le nœud suivant (`next`). Le dernier nœud pointe vers `None`.

```
head → [val|next] → [val|next] → [val|next] → None
```

- Structure d'un nœud :

    ```python
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    ```

- Propriétés clés:
    - Accès séquentiel uniquement (pas d'index)
    - Insertion/suppression en O(1) si on a le pointeur du nœud précédent
    - Pas de taille fixe — croît dynamiquement

## 2. Implémentation from scratch

> On implémente une classe `SinglyLinkedList` qui maintient un pointeur `head` et un `size`.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # --- Insert ---

    def insert_head(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def insert_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_head(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node = ListNode(val, curr.next)
        curr.next = new_node
        self.size += 1

    # --- Delete ---

    def delete_head(self):
        if not self.head:
            raise IndexError("Delete from empty list")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def delete_tail(self):
        if not self.head:
            raise IndexError("Delete from empty list")
        if not self.head.next:
            val = self.head.val
            self.head = None
            self.size -= 1
            return val
        curr = self.head
        while curr.next.next:
            curr = curr.next
        val = curr.next.val
        curr.next = None
        self.size -= 1
        return val

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_head()
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        val = curr.next.val
        curr.next = curr.next.next
        self.size -= 1
        return val

    # --- Search ---

    def search(self, val):
        """Returns the index of the first occurrence, or -1."""
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1

    def __contains__(self, val):
        return self.search(val) != -1

    # --- Access ---

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    # --- Traversal ---

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __repr__(self):
        vals = self.to_list()
        return " -> ".join(str(v) for v in vals) + " -> None"

    # --- Utility ---

    @classmethod
    def from_list(cls, vals):
        sll = cls()
        for val in reversed(vals):
            sll.insert_head(val)
        return sll
```

- **Complexity:**

    | Opération | Time | Space |
    |-----------|------|-------|
    | `insert_head` | O(1) | O(1) |
    | `insert_tail` | O(n) | O(1) |
    | `insert_at(i)` | O(i) | O(1) |
    | `delete_head` | O(1) | O(1) |
    | `delete_tail` | O(n) | O(1) |
    | `delete_at(i)` | O(i) | O(1) |
    | `search` | O(n) | O(1) |
    | `get(i)` | O(i) | O(1) |
    | `from_list` | O(n) | O(n) |

    > Note : `insert_tail` et `delete_tail` sont O(n) car on doit parcourir toute la liste. On peut les optimiser en O(1) en maintenant un pointeur `tail`.

- **Edge Cases:**
    - Liste vide (`head is None`) — delete et get doivent lever une exception
    - Liste à un seul élément — delete_tail doit mettre head à None
    - Index = 0 — insert_at et delete_at redirigent vers head operations
    - Index = size — insert_at ajoute à la fin
    - Index hors bornes — lever IndexError

## 3. Traversal Patterns

### 3.1 Parcours simple

```python
def traverse(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
```

- **Complexity:** O(n) temps, O(1) espace

### 3.2 Compter les éléments

```python
def count(head):
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    return n
```

### 3.3 Recherche récursive

```python
def search_recursive(head, target):
    if not head:
        return False
    if head.val == target:
        return True
    return search_recursive(head.next, target)
```

- **Complexity:** O(n) temps, O(n) espace (pile d'appels)
- **Edge Cases:**
    - head is None → retourne False
    - Element au début vs à la fin

## 4. Examples

### 4.1 Construire et afficher une SLL (Easy)

```python
sll = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
print(sll)  # 1 -> 2 -> 3 -> 4 -> 5 -> None

sll.insert_head(0)
print(sll)  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

sll.delete_tail()
print(sll)  # 0 -> 1 -> 2 -> 3 -> 4 -> None

print(sll.search(3))  # 3 (index)
print(sll.search(99)) # -1
```

### 4.2 Supprimer toutes les occurrences d'une valeur (Easy)

> **Problème** : Supprimer tous les nœuds ayant une valeur donnée.

```python
def remove_all(head, val):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Test :
# head = 1 -> 2 -> 6 -> 3 -> 6 -> None, val = 6
# dummy -> 1 -> 2 -> 3 -> None
# result = 1 -> 2 -> 3 -> None
```

- **Complexity:** O(n) temps, O(1) espace
- **Key idea:** utiliser un **dummy node** pour gérer le cas où head doit être supprimé
- **Edge Cases:**
    - Tous les nœuds ont la valeur → retourne None
    - Head a la valeur → le dummy node gère ce cas
    - Valeur absente → retourne la liste inchangée
