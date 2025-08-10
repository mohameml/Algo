# Tri Rapide : Quick-sort


- **Définition :**

- **Principe :**

- **Exemple :**

- **Algo:**

- **Complexité :**


L'algorithme QSort, également connu sous le nom de Quicksort, est un algorithme de tri très efficace qui fonctionne en divisant un tableau en sous-tableaux, en choisissant un élément appelé "pivot", en réorganisant les éléments autour du pivot de manière à ce que les éléments plus petits soient à gauche et les éléments plus grands à droite, puis en récursant sur les sous-tableaux résultants jusqu'à ce que tout le tableau soit trié. Voici une explication de l'algorithme Quicksort avec une implémentation en Python :

**Explication de l'algorithme Quicksort :**

1. Choisissez un élément du tableau comme pivot. Il existe différentes stratégies pour choisir le pivot, mais l'une des méthodes les plus courantes consiste à prendre le premier élément du tableau.

2. Divisez le tableau en deux sous-tableaux : un contenant les éléments plus petits que le pivot et l'autre contenant les éléments plus grands que le pivot.

3. Triez récursivement les sous-tableaux résultants. Cela signifie que vous répétez les étapes 1 et 2 pour les sous-tableaux jusqu'à ce que tout le tableau soit trié.

4. Concaténez les sous-tableaux triés avec le pivot au milieu pour obtenir le tableau trié final.

**Implémentation en Python :**

```python
def quicksort(tableau):
    if len(tableau) <= 1:
        return tableau  # Cas de base : un tableau vide ou avec un seul élément est déjà trié.

    pivot = tableau[0]  # Choisissez le premier élément comme pivot.
    elements_plus_petits = [x for x in tableau[1:] if x <= pivot]
    elements_plus_grands = [x for x in tableau[1:] if x > pivot]

    # Triez récursivement les sous-tableaux résultants et concaténez-les avec le pivot.
    return quicksort(elements_plus_petits) + [pivot] + quicksort(elements_plus_grands)

# Exemple d'utilisation :
tableau_non_trie = [3, 6, 8, 10, 1, 2, 1]
tableau_trie = quicksort(tableau_non_trie)
print("Tableau trié :", tableau_trie)
```

Cette implémentation de Quicksort triera un tableau en utilisant la stratégie de choisir le premier élément comme pivot. Notez que cette implémentation peut être améliorée pour éviter une utilisation excessive de la mémoire en utilisant une approche de tri en place.