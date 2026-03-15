# Module 3 — Common Techniques

## 1. Dummy Head Pattern

> Un **dummy head** (nœud sentinelle) est un nœud fictif placé avant le vrai head. Il simplifie le code en éliminant les cas spéciaux liés au head.

```python
def some_operation(head):
    dummy = ListNode(0, head)
    # ... opérations avec prev = dummy ...
    return dummy.next  # le vrai nouveau head
```

- When to use:
    - Quand le head peut être modifié ou supprimé
    - Quand on construit une nouvelle liste (merge, partition, etc.)
    - Quand on a besoin d'un pointeur `prev` pour le premier nœud

- **Edge Cases éliminés:**
    - Head supprimé → dummy.next pointe vers le nouveau head
    - Liste vide → dummy.next = None, pas de crash

## 2. Reverse a Linked List

> Inverser les pointeurs `next` de chaque nœud pour que la liste soit parcourue en sens inverse.

- **Template Code (itératif) :**

    ```python
    def reverse(head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    ```

    ```
    Étape par étape :
    1 -> 2 -> 3 -> None

    prev=None, curr=1: 1.next=None,    prev=1, curr=2     → None <- 1   2 -> 3
    prev=1,    curr=2: 2.next=1,       prev=2, curr=3     → None <- 1 <- 2   3
    prev=2,    curr=3: 3.next=2,       prev=3, curr=None  → None <- 1 <- 2 <- 3

    return prev = 3 → 3 -> 2 -> 1 -> None
    ```

- **Template Code (récursif) :**

    ```python
    def reverse_recursive(head):
        if not head or not head.next:
            return head
        new_head = reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
    ```

- **Complexity:**

    | Approche | Time | Space |
    |----------|------|-------|
    | Itératif | O(n) | O(1) |
    | Récursif | O(n) | O(n) — pile d'appels |

- **Edge Cases:**
    - Liste vide (`head is None`) → retourne None
    - Un seul élément → retourne head (pas de changement)
    - Deux éléments → vérifier que les pointeurs sont corrects

## 3. Two Pointers — Slow & Fast

> Le pattern **slow/fast** utilise deux pointeurs qui avancent à des vitesses différentes. Le slow avance de 1, le fast de 2.

### 3.1 Trouver le milieu

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

```
1 -> 2 -> 3 -> 4 -> 5 -> None
s
f

1 -> 2 -> 3 -> 4 -> 5 -> None
          s
                    f

1 -> 2 -> 3 -> 4 -> 5 -> None
               s
                              f (None)

return slow = 3 (milieu)
```

- **Complexity:** O(n) temps, O(1) espace

- **Edge Cases:**
    - Liste vide → retourne None
    - Un seul élément → retourne cet élément
    - Nombre pair d'éléments → retourne le **2ème** élément du milieu (pour le 1er, utiliser `while fast.next and fast.next.next`)

### 3.2 Détection de cycle — Floyd's Algorithm

> Si la liste a un cycle, le slow et le fast finiront par se rencontrer dans le cycle.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

- **Complexity:** O(n) temps, O(1) espace

- **Pourquoi ça marche ?**
    - Si pas de cycle → fast atteint None
    - Si cycle → fast entre dans le cycle en premier, puis slow le rejoint. La distance entre slow et fast diminue de 1 à chaque itération → ils se rencontrent forcément

### 3.3 Trouver le début du cycle

> Après détection, pour trouver le **nœud d'entrée** du cycle : remettre un pointeur à head, avancer les deux d'un pas à la fois → ils se rencontrent au début du cycle.

```python
def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Trouver l'entrée du cycle
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # début du cycle
    return None  # pas de cycle
```

- **Complexity:** O(n) temps, O(1) espace

- **Preuve mathématique:**
    - Soit `a` = distance head → entrée du cycle, `b` = distance entrée → point de rencontre, `c` = longueur du cycle
    - Au point de rencontre : slow a parcouru `a + b`, fast a parcouru `a + b + k*c` (k tours)
    - Comme fast = 2 * slow : `a + b + k*c = 2(a + b)` → `a = k*c - b`
    - Donc en partant de head et du point de rencontre simultanément, les deux se rencontrent à l'entrée du cycle

- **Edge Cases:**
    - Pas de cycle → retourne None
    - Cycle au head (head pointe vers lui-même) → retourne head
    - Cycle à la fin seulement

### 3.4 N-ème nœud depuis la fin

```python
def nth_from_end(head, n):
    fast = head
    for _ in range(n):
        fast = fast.next
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
```

- **Complexity:** O(n) temps, O(1) espace
- **Key idea:** Créer un écart de `n` entre fast et slow, puis avancer ensemble
- **Edge Cases:**
    - n > longueur de la liste → fast atteint None pendant l'écart initial
    - n = longueur → retourne head
    - n = 1 → retourne le dernier nœud

## 4. Merge Two Sorted Lists

> Fusionner deux listes triées en une seule liste triée.

```python
def merge_sorted(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

```
l1: 1 -> 3 -> 5
l2: 2 -> 4 -> 6

Step 1: dummy -> 1,  l1=3, l2=2
Step 2: dummy -> 1 -> 2,  l1=3, l2=4
Step 3: dummy -> 1 -> 2 -> 3,  l1=5, l2=4
Step 4: dummy -> 1 -> 2 -> 3 -> 4,  l1=5, l2=6
Step 5: dummy -> 1 -> 2 -> 3 -> 4 -> 5,  l1=None, l2=6
Append rest: dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

return 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

- **Complexity:**

    | Type | Value |
    |------|-------|
    | Time | O(n + m) |
    | Space | O(1) — on réutilise les nœuds existants |

- **Edge Cases:**
    - Une ou les deux listes vides → retourne l'autre (ou None)
    - Listes de tailles différentes → le `tail.next = l1 or l2` gère le reste
    - Éléments égaux → `<=` assure la stabilité

## 5. Examples

### 5.1 Palindrome Check — LC 234 (Easy)

> **Problème** : Vérifier si une linked list est un palindrome.

```python
def is_palindrome(head):
    # 1. Trouver le milieu
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse la deuxième moitié
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 3. Comparer les deux moitiés
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

# Test :
# 1 -> 2 -> 2 -> 1
# middle = 2 (2nd)
# reversed 2nd half: 1 -> 2
# compare: (1,1) ✓ (2,2) ✓ → True
```

- **Complexity:** O(n) temps, O(1) espace
- **Key idea:** Combine 3 techniques — find middle + reverse + compare
- **Edge Cases:**
    - Liste vide ou un seul élément → True
    - Longueur paire vs impaire — le middle node ne pose pas de problème car on compare `while right`

### 5.2 Remove N-th Node From End — LC 19 (Medium)

> **Problème** : Supprimer le n-ème nœud depuis la fin.

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# Test :
# 1 -> 2 -> 3 -> 4 -> 5, n=2
# fast avance de 3 : fast=3
# slow=dummy, fast=3 → slow=1, fast=4 → slow=2, fast=5 → slow=3, fast=None
# slow.next = slow.next.next : skip node 4
# result: 1 -> 2 -> 3 -> 5
```

- **Complexity:** O(n) temps, O(1) espace
- **Key idea:** dummy + two pointers avec écart de n+1
- **Edge Cases:**
    - Supprimer le head (n = length) → dummy gère ce cas
    - Liste d'un seul élément, n=1 → retourne None
