# cour : **``L'algorithme de backtracking``**


## 1. Introduction :

- L'algorithme de backtracking est une technique de résolution de problèmes récursifs qui explore toutes les solutions possibles pour un problème en suivant une séquence d'étapes, en revenant en arrière dès qu'une solution partielle ne peut pas être complétée pour aboutir à une solution valide. 

- C'est une approche de type "essai et erreur" qui peut être particulièrement efficace pour résoudre des problèmes de recherche de solution optimale, tels que les problèmes de permutation, de combinaison ou de satisfaction de contraintes.

## 2. Principe générale :

Voici une structure générale pour un algorithme de backtracking :

1. **Initialisation :** Définissez une solution partielle initiale et initialisez les structures de données nécessaires.

2. **Test d'arrêt :** Vérifiez si la solution partielle actuelle est une solution complète et valide. Si c'est le cas, arrêtez l'algorithme et retournez la solution.

3. **Boucle de backtracking :** Pour chaque choix possible à partir de l'état actuel, effectuez les étapes suivantes récursivement :
    - Faites un choix.
    - Appliquez les contraintes nécessaires.
    - Appelez récursivement l'algorithme avec la solution partielle mise à jour.
    - Annulez le choix.

4. **Terminaison :** L'algorithme se termine lorsque toutes les options ont été explorées.

5. **Résultat :** La solution finale est généralement récupérée à partir de la structure de données appropriée.


## 3. Exemple :

- L'algorithme de backtracking est souvent utilisé pour résoudre des problèmes tels que le problème des reines, le problème du sac à dos, les permutations, les combinaisons, etc.

Voici un exemple simple avec le problème des reines (N-Queens) où l'objectif est de placer N reines sur un échiquier de manière à ce qu'aucune reine ne puisse attaquer une autre :

```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    result = []
    board = [-1] * n
    backtrack(0)
    return result

# Exemple d'utilisation pour le problème des 4 reines
print(solve_n_queens(4))
```

Cet exemple illustre la structure générale de l'algorithme de backtracking en résolvant le problème des reines pour un échiquier de taille 4x4. Notez comment l'algorithme explore toutes les solutions possibles en suivant la séquence d'étapes définies.