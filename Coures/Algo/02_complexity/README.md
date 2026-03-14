# Chapter : Complexité Algorithmique

## 1. Introduction

> La **complexité algorithmique** mesure comment le temps ou l'espace utilisé par un algorithme croît en fonction de la taille de l'entrée `n`. Elle permet de comparer les algorithmes indépendamment du hardware.

## 2. Notations Asymptotiques

| Notation | Signification | Usage |
|----------|--------------|-------|
| **O(f(n))** | Borne supérieure (worst case) | La plus utilisée |
| **Omega(f(n))** | Borne inférieure (best case) | Garantie minimale |
| **Theta(f(n))** | Borne exacte (tight bound) | Quand O = Omega |

- Définitions formelles :
    - `f(n) = O(g(n))` s'il existe `c > 0` et `n0` tels que `f(n) <= c * g(n)` pour tout `n >= n0`
    - `f(n) = Omega(g(n))` s'il existe `c > 0` et `n0` tels que `f(n) >= c * g(n)` pour tout `n >= n0`
    - `f(n) = Theta(g(n))` si `f(n) = O(g(n))` et `f(n) = Omega(g(n))`

## 3. Complexités Courantes

> Classées de la plus rapide à la plus lente :

| Complexité | Nom | Exemple |
|-----------|-----|---------|
| O(1) | Constante | Accès array par index |
| O(log n) | Logarithmique | Binary search |
| O(n) | Linéaire | Parcours d'un tableau |
| O(n log n) | Linéarithmique | Merge sort, Heap sort |
| O(n^2) | Quadratique | Bubble sort, 2 boucles imbriquées |
| O(2^n) | Exponentielle | Sous-ensembles, backtracking naïf |
| O(n!) | Factorielle | Permutations |

## 4. Règles de Calcul

### 4.1 Boucles imbriquées — multiplier

```python
for i in range(n):       # O(n)
    for j in range(n):   # O(n)
        ...               # => O(n^2)
```

### 4.2 Boucles consécutives — additionner (garder le max)

```python
for i in range(n): ...   # O(n)
for j in range(m): ...   # O(m)
                          # => O(n + m)
```

### 4.3 Diviser par 2 à chaque itération — O(log n)

```python
while n > 0:
    n = n // 2            # => O(log n)
```

### 4.4 Récurrence — Master Theorem

> Pour `T(n) = aT(n/b) + O(n^d)` :

| Condition | Résultat |
|-----------|----------|
| `d > log_b(a)` | O(n^d) |
| `d = log_b(a)` | O(n^d * log n) |
| `d < log_b(a)` | O(n^(log_b(a))) |

## 5. Complexité Spatiale

> Même logique que la temporelle, mais on compte la mémoire :

| Cas | Espace |
|-----|--------|
| Variables scalaires | O(1) |
| Tableau de taille n | O(n) |
| Matrice n x n | O(n^2) |
| Pile de récursion de profondeur n | O(n) |
| Récursion avec mémorisation | O(n) à O(n^2) selon le problème |

## 6. Complexité Amortie

> Certaines opérations sont coûteuses occasionnellement mais bon marché en moyenne sur une séquence d'opérations.

| Structure | Opération | Worst case | Amorti |
|-----------|-----------|-----------|--------|
| Dynamic array (list) | append | O(n) | O(1) |
| Hash table | insert | O(n) | O(1) |

- Méthodes d'analyse :
    - **Aggregate** — coût total / nombre d'opérations
    - **Accounting** — assigner un coût amorti à chaque opération
    - **Potential** — définir une fonction potentiel sur la structure
