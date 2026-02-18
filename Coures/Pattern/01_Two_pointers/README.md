# Cour : **pattern Two Pointers**

## 1. **Introduction :**

-   **Définition :**

    > Le **pattern "Two Pointers"** consiste à utiliser deux pointeurs qui se déplacent à des vitesses différentes, ou parfois à la même vitesse, pour parcourir une structure de données (typiquement un tableau ou une liste) et résoudre un problème.

    -   Le principe de ce pattern est de réduire le nombre de comparaisons ou de calculs en utilisant deux pointeurs qui partent de positions différentes dans une structure, et de les déplacer en fonction des conditions du problème.

-   **Principes :**

    -   **Départ des deux pointeurs** : Les deux pointeurs sont souvent initialisés aux deux extrémités d'une structure (par exemple, un tableau).
    -   **Déplacement des pointeurs** : Les pointeurs se déplacent en fonction d’une condition (par exemple, l'un peut avancer et l'autre reculer).
    -   **Terminaison** : L'algorithme continue tant que les pointeurs ne se croisent pas ou n'atteignent une condition spécifique.

-   **Pattern:**

    > Le pattern **Two Pointers** est un excellent outil pour résoudre des problèmes où l’on doit travailler avec des relations entre deux éléments dans un tableau ou une liste. Ce pattern permet d'optimiser les algorithmes en réduisant souvent la complexité, en particulier pour des problèmes sur des tableaux triés ou des structures où les éléments doivent être comparés dans différentes positions.

-   **Template général (Python) :**

    ```python
    def two_pointers_template(arr):
        # Initialisation des pointeurs
        left, right = 0, len(arr) - 1

        # Boucle avec condition d'arrêt
        while left < right:
            # Logique principale : appliquer une condition spécifique au problème
            # Exemple : Calculer une somme, une différence, ou toute autre condition.
            result = arr[left] + arr[right]  # Ceci peut être modifié selon le problème

            # Condition de mise à jour des pointeurs
            if result == target:  # Condition d'arrêt ou de validation du résultat
                return (left, right)  # Retourne le résultat lorsque trouvé

            # Mise à jour des pointeurs selon la condition
            if result < target:  # Exemple de condition de mise à jour
                left += 1  # Avancer le pointeur gauche
            else:
                right -= 1  # Reculer le pointeur droit

        # Retourner une valeur indiquant que le résultat n'a pas été trouvé
        return None

    ```

## 2. **Exemples**

### 2.1 **Two Sum**

-   **Problème :**

    > Trouver deux indices dans un tableau tel que la somme de leurs éléments soit égale à un nombre donné `target`.

-   **Exemple :**
    Input: `arr = [2, 7, 11, 15], target = 9`
    Output: `(0, 1)` (car `arr[0] + arr[1] = 9`)

-   **Solution avec Two Pointers :**

    ```python
    def two_sum(arr, target):
        left, right = 0, len(arr) - 1

        while left < right:
            total = arr[left] + arr[right]
            if total == target:
                return (left, right)
            elif total < target:
                left += 1
            else:
                right -= 1
        return None
    ```

-   **Complexité** :

    -   Temps : $O(n)$, car chaque élément est visité une fois.
    -   Espace : $O(1)$, car il n'y a pas d'espace supplémentaire utilisé.

### 2.2 **Best Time to Buy and Sell Stock**

-   **Problème :**

    > Trouver le meilleur moment pour acheter et vendre des actions, afin de maximiser le profit. On te donne un tableau de prix où chaque élément représente le prix de l'action à un jour donné. Tu dois déterminer le maximum de profit possible.

-   **Exemple :**
    Input: `prices = [7, 1, 5, 3, 6, 4]`
    Output: `5` (acheter au jour 2 et vendre au jour 5)

-   **Solution avec Two Pointers :**

    ```python
    def max_profit(prices):
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit
    ```

-   **Complexité** :

    -   Temps : $O(n)$, car chaque prix est comparé une seule fois.
    -   Espace : $O(1)$, car il n'y a pas d'espace supplémentaire utilisé.

### 2.3 **Palindrome**

-   **Problème :**

    > Vérifier si une chaîne est un palindrome, c'est-à-dire qu’elle se lit de la même manière de gauche à droite que de droite à gauche.

-   **Exemple :**

    Input: `"racecar"`
    Output: `True`

-   **Solution avec Two Pointers :**

    ```python
    def is_palindrome(s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    ```

-   **Complexité** :

    -   Temps : $O(n)$, où $n$ est la longueur de la chaîne.
    -   Espace : $O(1)$, car il n'y a pas d'espace supplémentaire utilisé.

### 2.4 **Container With Most Water**

-   **Problème :**

    > Trouver deux lignes sur un graphique qui, ensemble, avec l'axe des abscisses, forment un "récipient" qui contient le plus d'eau. C'est-à-dire qu'on cherche deux indices $i$ et $j$ de manière à maximiser l'aire du rectangle formé entre les deux lignes, avec $h(i)$ et $h(j)$ comme hauteurs et $j - i$ comme largeur.

    ![alt text](image.png)

-   **Exemple :**
    Input: `heights = [1,8,6,2,5,4,8,3,7]`
    Output: `49`

-   **Solution avec Two Pointers :**

    ```python
    def max_area(heights):
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            max_area = max(max_area, height * width)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
    ```

-   **Complexité** :

    -   Temps : $O(n)$, où $n$ est le nombre de lignes.
    -   Espace : $O(1)$, car il n'y a pas d'espace supplémentaire utilisé.
