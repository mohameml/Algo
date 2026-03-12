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

- **Edge Cases:**

    * tableau vide
    * `target` plus petit que tous les éléments
    * `target` plus grand que tous les éléments
    * doublons (retourne une occurrence quelconque)



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





# 2. Binary Search on Boundaries

## 2.1 Lower Bound Binary Search

#### Definition

Trouver le **premier index `i` tel que** :

$$
nums[i] \ge target
$$

C'est la **première position où on peut insérer `target` sans casser l'ordre**.



#### Template Code

```python
def lower_bound(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l
```


#### Edge Cases

| Situation          | résultat                  |
| ------------------ | ------------------------- |
| target < nums[0]   | 0                         |
| target > nums[n-1] | n                         |
| target existe      | index première occurrence |



#### Example

```
nums = [1,3,5,7]
target = 4

answer = index 2
```

```
[1 3 |5 7]
     ↑
```



## 2.2 Upper Bound Binary Search

#### Definition

Trouver le **premier index `i` tel que** :

$$
nums[i] > target
$$



#### Template Code

```python
def upper_bound(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2

        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid

    return l
```



#### Edge Cases

| Situation           | résultat |
| ------------------- | -------- |
| target < nums[0]    | 0        |
| target >= nums[n-1] | n        |



#### Example

```
nums = [1,2,4,4,4,7]
target = 4
```

```
[1 2 4 4 4 |7]
           ↑
upper_bound = 5
```



# 3. Binary Search for Floor / Ceil

## 3.1 Floor Index

#### Definition

Trouver :

\[
\max { i \mid nums[i] \le target }
\]

Donc **le plus grand élément ≤ target**.



#### Template Code

```python
def floor_index(nums, target):
    pos = upper_bound(nums, target)

    if pos == 0:
        return -1

    return pos - 1
```



#### Edge Cases

| Situation           | résultat |
| ------------------- | -------- |
| target < nums[0]    | -1       |
| target >= nums[n-1] | n-1      |



#### Example

```
nums = [1,3,5,7]
target = 6
```

```
[1 3 5 |7]
        ↑
floor = index 2
```



## 3.2 Ceil Index

#### Definition

Trouver :

\[
\min { i \mid nums[i] \ge target }
\]

Donc **le plus petit élément ≥ target**.

C'est exactement **lower_bound**.



#### Template Code

```python
def ceil_index(nums, target):
    pos = lower_bound(nums, target)

    if pos == len(nums):
        return -1

    return pos
```



#### Edge Cases

| Situation          | résultat |
| ------------------ | -------- |
| target > nums[n-1] | -1       |
| target <= nums[0]  | 0        |



#### Example

```
nums = [1,3,5,7]
target = 4
```

```
[1 3 |5 7]
     ↑
ceil = index 2
```



# 4. Range Search Pattern

## 4.1 Count Occurrences

#### Definition

Nombre d’occurrences d'une valeur.

[
count = upper_bound(target) - lower_bound(target)
]



#### Template Code

```python
def count_occurrences(nums, target):
    return upper_bound(nums, target) - lower_bound(nums, target)
```



#### Example

```
nums = [1,2,4,4,4,7]
target = 4
```

```
lower_bound = 2
upper_bound = 5
count = 3
```


# 5. Binary Search on Predicate (Advanced Pattern)

### Definition

Utilisé quand on cherche **la première position où une condition devient vraie**.

On suppose que la fonction `f(x)` est **monotone** :

```
FFFFFTTTTT
```


### Template Code

```python
def binary_search_predicate(n):

    l, r = 0, n

    while l < r:
        mid = (l + r) // 2

        if condition(mid):
            r = mid
        else:
            l = mid + 1

    return l
```


### Example Problems

* First Bad Version
* Capacity to Ship Packages
* Koko Eating Bananas
* Minimum in Rotated Array
* Allocate Books



### RQ : **Conseil pratique**

Quand tu fais du Binary Search, pense toujours :

```
je cherche une frontière
```

entre deux zones :

```
FFFFFTTTTT
```

C’est **la clé pour 90% des problèmes LeetCode binary search**.





## 6. **Exemples:**

### 6.1 **Problème du singe qui mange des bananes (Leetcode: Koko Eating Bananas)**

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

### 6.2 **Généralisation du Binary Search (Binary Search Lower Bound):**

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

### 6.3 **Exemple : Minimum Days to Make Bouquets (Leetcode 1482)**

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

## 7. Real Quant / Algo Trading Applications of Binary Search

### 7.1 Finding Optimal Trade Size Under Liquidity Constraints

#### Definition

Dans un **order book**, on veut trouver la **quantité maximale qu'on peut acheter/vendre** sans dépasser un certain **slippage ou impact de marché**.

On cherche :

$$
\max q \text{ tel que } \text{impact}(q) \leq threshold
$$

La fonction `impact(q)` est généralement **croissante**.

Donc on peut appliquer un **binary search sur q**.


#### Example

Supposons un modèle d'impact :

$$
impact(q) = \alpha \sqrt{q}
$$

et on impose :

$$
impact(q) \le 0.01
$$


#### Template Code

```python
def max_trade_size(alpha, threshold):

    def impact(q):
        return alpha * (q ** 0.5)

    l, r = 0, 10**7

    while l < r:
        mid = (l + r + 1) // 2

        if impact(mid) <= threshold:
            l = mid
        else:
            r = mid - 1

    return l
```


#### Real Use

Utilisé dans :

* **Optimal execution**
* **TWAP / VWAP algorithms**
* **market impact control**


### 7.2 Optimal Order Splitting (Execution Algorithms)

#### Definition

Dans un algo d'exécution, on cherche souvent le **nombre optimal de slices** pour minimiser :

$$
cost = market_impact + timing_risk
$$

La fonction de coût peut être **convexe ou monotone localement**.

On peut faire un **binary search sur le nombre de slices**.


#### Example

```python
def optimal_slices(max_slices):

    def cost(k):
        return impact(k) + risk(k)

    l, r = 1, max_slices

    while l < r:
        mid = (l + r) // 2

        if cost(mid) <= cost(mid + 1):
            r = mid
        else:
            l = mid + 1

    return l
```


#### Real Use

Utilisé dans :

* **Almgren-Chriss optimal execution**
* **VWAP/TWAP optimization**
* **liquidity scheduling**


### 7.3 Finding Clearing Price in Auctions

#### Definition

Dans un **market auction**, on cherche le **prix d'équilibre** :

$$
\text{supply}(p) = \text{demand}(p)
$$

Les fonctions :

* supply(p) ↑
* demand(p) ↓

Donc la différence :

$$
f(p) = supply(p) - demand(p)
$$

est monotone.

On peut appliquer un **binary search sur le prix**.


#### Template Code

```python
def find_clearing_price():

    l, r = min_price, max_price

    while r - l > 1e-6:
        mid = (l + r) / 2

        if supply(mid) >= demand(mid):
            r = mid
        else:
            l = mid

    return (l + r) / 2
```


#### Real Use

Utilisé dans :

* **opening auctions**
* **closing auctions**
* **dark pools crossing**


### 7.4 Portfolio Risk Budget Allocation

#### Definition

On cherche un **paramètre λ** tel que :

$$
\sum_i w_i(\lambda) = 1
$$

ou

$$
risk(\lambda) = target_risk
$$

Souvent `risk(λ)` est monotone.

On utilise un **binary search sur λ**.


#### Example

```python
def find_lambda(target_risk):

    l, r = 0, 100

    while r - l > 1e-8:
        mid = (l + r) / 2

        if portfolio_risk(mid) > target_risk:
            r = mid
        else:
            l = mid

    return mid
```


#### Real Use

Utilisé dans :

* **risk parity portfolios**
* **volatility targeting**
* **portfolio leverage control**


### 7.5 Calibration of Option Pricing Models

#### Definition

On cherche la **volatilité implicite** :

$$
BS(\sigma) = market_price
$$

La fonction :

$$
BS(\sigma)
$$

est **monotone croissante**.

Donc on peut utiliser **binary search**.


#### Template Code

```python
def implied_vol(target_price):

    l, r = 0.0001, 5

    while r - l > 1e-6:
        mid = (l + r) / 2

        price = black_scholes(mid)

        if price > target_price:
            r = mid
        else:
            l = mid

    return mid
```


#### Real Use

Utilisé dans :

* **volatility surfaces**
* **option calibration**
* **risk management**


### 7.6. Binary Search in Order Book Simulation

#### Definition

Dans un **order book**, on cherche souvent :

$$
\text{first price level where cumulative volume ≥ target}
$$

C'est exactement un **lower_bound sur volume cumulatif**.


#### Example

```python
volumes = [10, 30, 50, 80, 120]  # cumulative
target = 60
```

On cherche :

```
first volume ≥ 60
```


#### Code

```python
def find_price_level(volumes, target):

    l, r = 0, len(volumes)

    while l < r:
        mid = (l + r) // 2

        if volumes[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l
```


#### Real Use

Utilisé dans :

* **liquidity estimation**
* **order book simulation**
* **market impact models**


### **Conclusion 💡:**

En quant, le **binary search** est utilisé quand :

* une fonction est **monotone**
* on cherche un **paramètre optimal**
* on veut trouver une **frontière ou racine**


