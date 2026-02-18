# cour : **Stack**

## **1. Stack**

-   **Définition:**

    > Une pile (stack) est une structure de données qui suit le principe **LIFO (Last In, First Out)**, ce qui signifie que l'élément ajouté en dernier est celui qui sera retiré en premier.

-   **Implémentation:**

    Une pile peut être implémentée à l'aide d'une liste (en Python) ou d'une structure dédiée dans d'autres langages. L'implémentation de base inclut :

    -   `push(item)` : ajoute un élément au sommet de la pile
    -   `pop()` : retire l'élément au sommet de la pile
    -   `peek()` : retourne l'élément au sommet sans le retirer
    -   `is_empty()` : vérifie si la pile est vide

    ```python
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            return None

        def peek(self):
            if not self.is_empty():
                return self.items[-1]
            return None

        def is_empty(self):
            return len(self.items) == 0
    ```

-   **Complexité:**

    -   Temps : $O(1)$ pour `push`, `pop`, et `peek`.
    -   Espace : $O(n)$ où $n$ est le nombre d'éléments dans la pile.

-   **Exemple Classique : Balancement des Parenthèses**

    Le problème consiste à vérifier si une séquence de parenthèses est correctement équilibrée. Une solution avec une pile :

    ```python
    def is_balanced(s):
        stack = Stack()
        for char in s:
            if char == '(':
                stack.push(char)
            elif char == ')':
                if stack.is_empty():
                    return False
                stack.pop()
        return stack.is_empty()
    ```

## **2. Monotonic Stack**

-   **Définition:**

    > Une **Monotonic Stack** est une pile qui maintient ses éléments dans un ordre monotone, soit croissant, soit décroissant. Elle est utilisée pour résoudre des problèmes où l'on cherche à trouver le **prochain élément plus grand** ou **plus petit**.

-   **Exemple Classique : Next Greater Element I**

    > Étant donnés deux tableaux, `nums1` et `nums2`, pour chaque élément de `nums1`, trouver le prochain élément plus grand dans `nums2`.

    ```python
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ```

    **Solution :**

    ```python
    def nextGreaterElement(nums1, nums2):
        stack = []
        nge_map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                nge_map[prev] = num
            stack.append(num)

        return [nge_map.get(num, -1) for num in nums1]
    ```

-   **Complexité**

    -   Temps : $O(n)$ — chaque élément est empilé et dépilé une seule fois.
    -   Espace : $O(n)$ pour la pile.

-   **Problèmes Leetcode par Difficulté**

    | Difficulté | Problème                       | ID   |
    | ---------- | ------------------------------ | ---- |
    | Facile     | Next Greater Element I         | #496 |
    | Facile     | Remove K Digits                | #402 |
    | Moyen      | Next Greater Element II        | #503 |
    | Moyen      | Daily Temperatures             | #739 |
    | Moyen      | Asteroid Collision             | #735 |
    | Difficile  | Largest Rectangle in Histogram | #84  |
    | Difficile  | Sum of Subarray Minimums       | #907 |
    | Difficile  | Trapping Rain Water            | #42  |
