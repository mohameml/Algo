# Module 4 — Advanced Operations

## 1. Reorder List — LC 143

> **Problème** : Réorganiser `L0 → L1 → ... → Ln` en `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

- **Approche** : 3 étapes — find middle, reverse second half, merge alternating

```python
def reorder_list(head):
    if not head or not head.next:
        return

    # 1. Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow

    # 2. Reverse second half
    prev = None
    curr = mid.next
    mid.next = None  # couper la liste en deux
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 3. Merge alternating
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
```

```
Input:  1 -> 2 -> 3 -> 4 -> 5

Step 1 — Find middle: mid = 3
Step 2 — Split & reverse: first = 1->2->3, second = 5->4
Step 3 — Merge alternating:
  1 -> 5 -> 2 -> 4 -> 3

Output: 1 -> 5 -> 2 -> 4 -> 3
```

- **Complexity:**

    | Type | Value |
    |------|-------|
    | Time | O(n) |
    | Space | O(1) |

- **Edge Cases:**
    - Liste vide ou un seul élément → rien à faire
    - Deux éléments → déjà dans l'ordre
    - Nombre pair vs impair → le `mid.next = None` coupe correctement

## 2. Copy List with Random Pointer — LC 138

> **Problème** : Chaque nœud a un pointeur `next` et un pointeur `random` (vers un nœud arbitraire ou None). Deep copy la liste.

- **Approche 1 — HashMap O(n) space :**

```python
def copy_random_list(head):
    if not head:
        return None

    # Map: original node → copied node
    node_map = {}
    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    # Set next and random pointers
    curr = head
    while curr:
        node_map[curr].next = node_map.get(curr.next)
        node_map[curr].random = node_map.get(curr.random)
        curr = curr.next

    return node_map[head]
```

- **Approche 2 — Interleaving O(1) space :**

```python
def copy_random_list_o1(head):
    if not head:
        return None

    # Step 1: Insert copies after each original
    # A -> A' -> B -> B' -> C -> C'
    curr = head
    while curr:
        copy = Node(curr.val, curr.next)
        curr.next = copy
        curr = copy.next

    # Step 2: Set random pointers for copies
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the two lists
    dummy = Node(0)
    copy_tail = dummy
    curr = head
    while curr:
        copy_tail.next = curr.next
        copy_tail = copy_tail.next
        curr.next = curr.next.next
        curr = curr.next

    return dummy.next
```

- **Complexity:**

    | Approche | Time | Space |
    |----------|------|-------|
    | HashMap | O(n) | O(n) |
    | Interleaving | O(n) | O(1) — hors output |

- **Edge Cases:**
    - Liste vide → retourne None
    - Random pointe vers lui-même → le mapping gère ce cas
    - Random = None → `node_map.get(None)` retourne None
    - Un seul nœud avec random vers lui-même

## 3. LRU Cache — LC 146

> Un **LRU Cache** (Least Recently Used) combine une **HashMap** et une **Doubly Linked List** pour atteindre O(1) sur `get` et `put`.

- **Principe:**
    - HashMap : `key → DLL node` pour accès O(1)
    - DLL : maintient l'**ordre d'utilisation** (head = most recent, tail = least recent)
    - `get(key)` : move node to head
    - `put(key, value)` : insert at head, si capacité dépassée → remove tail

```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode
        # Sentinel nodes
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict LRU (node before tail sentinel)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
```

```
Exemple : capacity = 2

put(1, 1) : cache = {1:1}, DLL: [1]
put(2, 2) : cache = {1:1, 2:2}, DLL: [2, 1]
get(1)    : return 1, DLL: [1, 2]  (1 moved to front)
put(3, 3) : evict key 2 (LRU), cache = {1:1, 3:3}, DLL: [3, 1]
get(2)    : return -1 (evicted)
```

- **Complexity:**

    | Opération | Time | Space |
    |-----------|------|-------|
    | `get` | O(1) | — |
    | `put` | O(1) | — |
    | Total space | — | O(capacity) |

- **Edge Cases:**
    - Capacity = 0 → pas courant mais `put` devrait évacuer immédiatement
    - `put` avec une clé existante → update la valeur, move to front (pas d'éviction)
    - `get` miss → retourne -1, pas de modification de la DLL
    - Éviction quand plein → toujours supprimer `tail.prev` (le LRU)

- **Why DLL + HashMap ?**
    - HashMap seule → pas d'ordre d'utilisation
    - DLL seule → search en O(n)
    - Ensemble → O(1) access (HashMap) + O(1) order update (DLL remove/insert)

## 4. Reverse Nodes in k-Group — LC 25

> **Problème** : Inverser les nœuds par groupes de k. Si le dernier groupe a < k nœuds, le laisser tel quel.

```python
def reverse_k_group(head, k):
    # Check if there are k nodes left
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return head  # not enough nodes

    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # head is now the tail of reversed group
    # curr is the head of the next group
    head.next = reverse_k_group(curr, k)
    return prev
```

```
Input: 1 -> 2 -> 3 -> 4 -> 5, k=3

Group 1 (k=3 nodes exist): reverse 1->2->3 → 3->2->1
Group 2 (only 2 nodes): keep 4->5 as is

Output: 3 -> 2 -> 1 -> 4 -> 5
```

- **Complexity:**

    | Type | Value |
    |------|-------|
    | Time | O(n) |
    | Space | O(n/k) — pile d'appels récursifs |

- **Edge Cases:**
    - k = 1 → retourne la liste inchangée
    - k = longueur → reverse toute la liste
    - k > longueur → retourne la liste inchangée
    - Dernier groupe incomplet → pas inversé

## 5. Real Quant Applications

### 5.1 Order Book — Linked List of Price Levels

> Dans un carnet d'ordres (order book), chaque **price level** contient une liste chaînée d'ordres à ce prix, ordonnés par **time priority** (FIFO).

```python
class Order:
    def __init__(self, order_id, quantity, timestamp):
        self.order_id = order_id
        self.quantity = quantity
        self.timestamp = timestamp
        self.prev = None
        self.next = None

class PriceLevel:
    def __init__(self, price):
        self.price = price
        self.head = Order(0, 0, 0)  # sentinel
        self.tail = Order(0, 0, 0)  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.total_quantity = 0

    def add_order(self, order):
        """Add order at tail — O(1), maintains FIFO."""
        order.prev = self.tail.prev
        order.next = self.tail
        self.tail.prev.next = order
        self.tail.prev = order
        self.total_quantity += order.quantity

    def cancel_order(self, order):
        """Cancel specific order — O(1) with direct reference."""
        order.prev.next = order.next
        order.next.prev = order.prev
        self.total_quantity -= order.quantity

    def fill_orders(self, quantity):
        """Fill orders FIFO from head — used in matching engine."""
        remaining = quantity
        curr = self.head.next
        while curr != self.tail and remaining > 0:
            if curr.quantity <= remaining:
                remaining -= curr.quantity
                next_order = curr.next
                self.cancel_order(curr)
                curr = next_order
            else:
                curr.quantity -= remaining
                self.total_quantity -= remaining
                remaining = 0
        return quantity - remaining  # total filled
```

- **Why LinkedList ?** Les ordres à un même prix doivent être **FIFO**. La DLL permet :
    - Ajout en O(1) à la fin (nouveaux ordres)
    - Annulation en O(1) avec référence directe (cancel order)
    - Remplissage FIFO depuis le début (matching engine)

- **Complexity:**

    | Opération | Time |
    |-----------|------|
    | `add_order` | O(1) |
    | `cancel_order` | O(1) |
    | `fill_orders(q)` | O(k) — k = nombre d'ordres remplis |
