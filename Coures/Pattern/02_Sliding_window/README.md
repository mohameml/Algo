# Cour : **Sliding Window:**

## **1. Introduction**

-   **Définition:**

    > La technique de la **fenêtre glissante** est une approche d’optimisation utilisée pour résoudre des problèmes impliquant **des sous-tableaux ou sous-chaînes contigus** dans un tableau ou une chaîne de caractères.

    -   Elle permet d’améliorer l’efficacité en évitant des calculs redondants et en réduisant la complexité **de O(n²) à O(n)** dans de nombreux cas.

-   **Principe de la technique :**

    -   Plutôt que de recalculer plusieurs fois une même portion du tableau, **on utilise une `fenêtre` qui se déplace progressivement**.

    -   **Deux types de fenêtres glissantes :**

        1. **Fenêtre de taille fixe** : la fenêtre garde toujours une taille **k** constante.
        2. **Fenêtre de taille variable** : la taille de la fenêtre change dynamiquement en fonction du problème.

## 2. **Exemples:**

### 2.1 **Exemple 1 : Somme maximale d'un sous-tableau de taille fixe**

> **Problème :** Trouver la somme maximale d'un sous-tableau de taille `k`.

-   **Approche naïve (O(n²))**  
     On peut parcourir tous les sous-tableaux de taille `k` et calculer leur somme individuellement.

-   **Approche avec Sliding Window (O(n))**

    On utilise une fenêtre de taille fixe et on met à jour la somme **sans recalculer tout** à chaque étape.

-   **Implémentation :**

    ```python
    def maxSumSubarray(arr, k):
        n = len(arr)
        if n < k:
            return None  # Impossible si la taille du tableau est inférieure à k

        max_sum = float('-inf')
        current_sum = sum(arr[:k])  # Somme des k premiers éléments

        for i in range(k, n):
            current_sum += arr[i] - arr[i - k]  # On enlève l'ancien et ajoute le nouveau
            max_sum = max(max_sum, current_sum)

        return max_sum
    ```

### 2.2 **Exemple 2 : Sous-chaîne la plus longue sans caractères répétés**

> **Problème :** Trouver la **plus longue sous-chaîne** sans répétition dans une chaîne donnée.

-   **Approche naïve (O(n²))**  
    Tester toutes les sous-chaînes possibles.

-   **Approche avec Sliding Window (O(n))**  
     Utiliser une fenêtre dynamique qui s'agrandit tant que la condition est respectée et se réduit lorsqu'un caractère est répété.

-   **Implémentation :**

    ```python
    def longestUniqueSubstring(s):
        seen = set()  # Ensemble des caractères uniques
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1  # On déplace la fenêtre vers la droite

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
    ```

    ✅ **Pourquoi ça marche ?**  
    On ne recommence pas tout à zéro dès qu'on trouve un doublon, on **ajuste simplement `left`**.

### 2.3. **Exemple 3 : Trouver la plus petite sous-chaîne contenant tous les caractères d'un motif**

> **Problème :** Trouver la plus petite sous-chaîne qui contient tous les caractères d’un mot donné.

-   **Exemple :**

    ```
    s = "ADOBECODEBANC"
    t = "ABC"
    ```

    La plus petite sous-chaîne contenant `A`, `B` et `C` est `"BANC"`.

-   **Approche avec Sliding Window (O(n))**  
     On utilise une **fenêtre qui s'agrandit pour inclure tous les caractères de `t`**, puis on la réduit pour optimiser.

-   **Implémentation :**

    ```python
    from collections import Counter

    def minWindowSubstring(s, t):
        if not s or not t:
            return ""

        count_t = Counter(t)
        window_count = {}
        left, right = 0, 0
        required = len(count_t)
        formed = 0
        min_len = float("inf")
        result = ""

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in count_t and window_count[char] == count_t[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                window_count[s[left]] -= 1
                if s[left] in count_t and window_count[s[left]] < count_t[s[left]]:
                    formed -= 1

                left += 1

            right += 1

        return result
    ```

### RQ : **Exercices pour s'entraîner**

1. Trouver la **sous-séquence** la plus longue de `0` et `1` ayant autant de `0` que de `1` (difficile).
2. Trouver le **plus grand produit** d’un sous-tableau de taille `k`.
3. Trouver le **plus petit sous-tableau** dont la somme est supérieure ou égale à `S`.

-   [link_video](https://youtu.be/p-ss2JNynmw?si=AUUEYs-5_fpJpmy-)
-   [link_article_1](https://www.geeksforgeeks.org/window-sliding-technique/)
-   [link_article_2](https://algocademy.com/blog/mastering-sliding-window-techniques-a-comprehensive-guide-for-coding-interviews/)
