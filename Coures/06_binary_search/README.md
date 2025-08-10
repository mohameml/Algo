# Cour : **Binary Search**

## 1. **Introduction:**

-   **Définition:**

    > La **recherche binaire** est un algorithme efficace utilisé pour **trouver un élément cible dans une séquence triée**.

    -   Plutôt que de parcourir tous les éléments un à un, il divise la recherche en deux à chaque itération.

-   **Idée de l’algorithme:**

    À chaque étape :

    -   On compare la valeur cible avec l’élément au **milieu** de la plage courante.
    -   Si égal, on retourne l’indice.
    -   Si la cible est plus petite, on cherche dans la **moitié gauche**.
    -   Si plus grande, on cherche dans la **moitié droite**.

-   **Implémentation en Python:**

    ```python
    def binary_search(nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # target non trouvé
    ```

-   **Complexité:**

    | Type                   | Valeur       |
    | ---------------------- | ------------ |
    | Temps (moyen/cas pire) | **O(log n)** |
    | Temps (meilleur)       | **O(1)**     |
    | Espace                 | **O(1)**     |

## 2. **Exemples:**

### 2.1 **Problème du singe qui mange des bananes (Leetcode: Koko Eating Bananas)**

-   **Énoncé :**

    Koko aime manger des bananes.
    Il y a **n piles** de bananes, et la **iᵉ pile** contient `piles[i]` bananes.

    Les gardiens sont partis et reviendront dans `h` heures.

    Koko peut choisir une **vitesse de consommation** `k` (en bananes par heure).
    Chaque heure :

    -   Elle choisit **une seule pile**.
    -   Elle mange **au plus `k` bananes** de cette pile.
    -   Si la pile contient moins de `k` bananes, elle mange tout et **ne mange plus pendant cette heure**.

    Koko veut manger **le plus lentement possible**, mais **terminer toutes les bananes avant que les gardiens reviennent**.

-   **Objectif**

    > Trouver la **vitesse minimale `k` (entier)** telle que Koko peut **finir toutes les bananes en `h` heures**, sachant que `piles.length <= h`.

-   **Implémentation:**

    ```python
    import math

    def min_eating_speed(piles, h):
        left, right = 1, max(piles)

        def can_finish(speed):
            total_hours = sum(math.ceil(pile / speed) for pile in piles)
            return total_hours <= h

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
    ```

### 2.2 **Généralisation du Binary Search (Binary Search Lower Bound):**

-   **énoncé:**

    > On cherche le plus petit entier $k \in \{1, 2, ..., \alpha\}$ tel que **la condition :** $\phi(k) \leq h$ .

-   **Hypothèses sur $\phi$:**

    -   $\phi(k)$ est une **fonction décroissante** en $k$ (plus $k$ est grand, plus elle "améliore" la situation).

    -   et $\phi( \alpha) \leq h$

-   **Objectif:**

    > Trouver le **plus petit $k$** (appelé souvent `first k` satisfaisant la condition) en O(log(n)).

-   **Algorithme général:**

    ```python
    def binary_search_phi(low, high, phi):
        while low < high:
            mid = (low + high) // 2
            if phi(mid):
                high = mid
            else:
                low = mid + 1
        return low
    ```

    -   `phi(k)` : une fonction booléenne (par exemple : "peut-on manger toutes les bananes à vitesse `k` ?")
    -   `gauche = 1`, `droite = α` : bornes du domaine de recherche

-   **Exemple avec Koko (repris):**

    -   Domaine de recherche : `k ∈ [1, max(piles)]`
    -   $\phi(k)$ = nombre total d’heures nécessaires pour finir → doit être ≤ h

    ```python
    def phi(k):  # temps nécessaire à vitesse k
        return sum(math.ceil(p / k) for p in piles)

    def min_k(piles, h):
        gauche, droite = 1, max(piles)
        while gauche < droite:
            mid = (gauche + droite) // 2
            if phi(mid) <= h:
                droite = mid
            else:
                gauche = mid + 1
        return gauche
    ```

### 2.3 **Exemple : Minimum Days to Make Bouquets (Leetcode 1482)**

> **Problème** : On a une liste `bloomDay`. On veut faire `m` bouquets, chacun de `k` fleurs adjacentes. Trouver le **nombre minimal de jours** nécessaires pour réaliser ça.

```python
def min_days(bloomDay, m, k):
    def can_make(day):
        bouquets = 0
        count = 0

        for b in bloomDay:
            count = count + 1 if b <= day else 0
            if count == k:
                bouquets += 1
                count = 0
        return bouquets >= m

    if len(bloomDay) < m * k:
        return -1

    return binary_search_phi(min(bloomDay), max(bloomDay), can_make)
```
