# Tri par insertion 


- **Définition :**

- **Principe :**

- **Exemple :**

- **Algo:**

- **Complexité :**


L'algorithme de tri par insertion est un algorithme de tri simple mais efficace qui fonctionne en insérant progressivement chaque élément de la liste non triée dans sa position correcte parmi les éléments déjà triés. Voici une explication détaillée de l'algorithme de tri par insertion ainsi que sa complexité :

### Explication détaillée de l'algorithme de tri par insertion :

1. **Initialisation** : L'algorithme commence par considérer le premier élément de la liste comme étant déjà trié. Le reste de la liste est considéré comme non trié.

2. **Insertion** : Pour chaque élément de la liste non triée, l'algorithme compare cet élément avec les éléments déjà triés, en commençant par le dernier élément trié. Il décale les éléments triés vers la droite tant que l'élément actuel est plus petit que l'élément trié en cours d'examen. Lorsque l'élément trié approprié est trouvé (c'est-à-dire qu'il est plus petit que l'élément actuel), l'élément actuel est inséré à cet emplacement.

3. **Répétition** : L'algorithme répète l'étape 2 pour chaque élément non trié jusqu'à ce que toute la liste soit triée.

4. **Terminaison** : À la fin de l'algorithme, la liste est triée dans l'ordre croissant.

### Complexité de l'algorithme de tri par insertion :

- **Complexité temporelle** : Dans le meilleur des cas, lorsque la liste est déjà presque triée, l'algorithme de tri par insertion a une complexité temporelle de O(n), où "n" est le nombre d'éléments dans la liste. Dans le pire des cas, lorsque la liste est triée dans l'ordre inverse, la complexité temporelle est de O(n^2), ce qui en fait moins efficace que certains autres algorithmes de tri comme le tri fusion ou le tri rapide. En moyenne, sa complexité est également de O(n^2).

- **Complexité spatiale** : L'algorithme de tri par insertion a une complexité spatiale de O(1), ce qui signifie qu'il ne nécessite qu'une petite quantité de mémoire supplémentaire pour effectuer le tri, quel que soit le nombre d'éléments dans la liste.

### Exemple d'algorithme de tri par insertion en Python :

```python
def tri_insertion(liste):
    for i in range(1, len(liste)):
        element_a_inserer = liste[i]
        j = i - 1
        while j >= 0 and element_a_inserer < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element_a_inserer

liste_non_triee = [12, 11, 13, 5, 6]
tri_insertion(liste_non_triee)
print(liste_non_triee)
```

Dans cet exemple, l'algorithme de tri par insertion est implémenté en Python. La liste `[12, 11, 13, 5, 6]` est triée en ordre croissant, et le résultat sera `[5, 6, 11, 12, 13]`.