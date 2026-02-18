# Plan de la programmation dynamique

## 1. **Introduction à la programmation dynamique :**

### 1.1.**Définition :**

- La programmation dynamique est une technique algorithmique couramment utilisée pour résoudre des problèmes liés à l'optimisation.

- Elle consiste à résoudre un problème en le décomposant en sous-problèmes plus petits et en utilisant une approche itérative pour stocker et réutiliser les solutions aux sous-problèmes.

- Cette technique est souvent utilisée pour résoudre des problèmes où il est nécessaire de trouver la meilleure solution parmi un grand nombre de solutions possibles.

### 1.2. **Les caractéristiques clés de la programmation dynamique :**

Les caractéristiques clés de la programmation dynamique comprennent :

1. **Décomposition en sous-problèmes** : Un problème plus complexe est divisé en sous-problèmes plus simples et plus petits qui peuvent être résolus individuellement.

2. **Stockage des résultats intermédiaires** : Les solutions aux sous-problèmes sont stockées dans une table ou un tableau pour éviter de recalculer les mêmes résultats plusieurs fois.

3. **Approche itérative** : La résolution du problème se fait de manière itérative en utilisant les solutions aux sous-problèmes pour construire progressivement la solution finale.

4. **Principe de l'optimalité** _(Principe d’optimalité de Bellman)_:
    - une solution optimale est construite en combinant des solutions optimales de sous-problèmes

    - le sous-structure d'un structure optimale est un structure optimale .

#### RQ : la différence entre `Diviser pour régner` et `Programmation dynamique` :

- **Diviser pour régner** :
    - divise un problème en sous-problèmes indépendants (qui ne se chevauchent pas),
    - résout chaque sous-problème,
    - et combine les solutions des sous problèmes pour former une solution du problème initial.

- **Programmation dynamique** :
    - divise un problème en sous problèmes qui sont non indépendants (qui se chevauchent).

    - cherche (et stocke) des solutions de sous-problèmes .

    - une solution optimale est construite en combinant des solutions optimales de sous-problèmes

## 2. **Méthodes des Résolutions (Bottom-up ,Top-down):**

La programmation dynamique peut être mise en œuvre de deux manières principales : la méthode bottom-up (ou itérative) et la méthode top-down (ou récursive avec mémoïsation).

1. **Méthode Bottom-up (Itérative) :**

- **Définition :**

Dans cette méthode, vous commencez par résoudre les sous-problèmes les plus petits et construisez progressivement la solution du problème global en utilisant les résultats des sous-problèmes. Vous travaillez généralement à partir du bas (d'où le terme "bottom-up") vers le haut.

- **Exemple :**

Résolution du problème du calcul du n-ième nombre de la suite de Fibonacci (Fibonacci(n)) en utilisant la méthode bottom-up.

```python
# méthode Bottom-up
def fibo_bottom_up(n : int) -> int :
    if n == 0 or n == 1 :
        return 1
    fib = [1]*(n+ 1)

    for i in range(2 , n + 1) :
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]


def fibo_optim_bottom_up(n : int) -> int:
    if n == 0 or n == 1 :
        return 1
    prev , curr = 1 , 1
    for _ in range(2 , n + 1) :
        temp = curr
        curr = curr + prev
        prev = temp
    return curr
```

Dans cet exemple, nous utilisons un tableau `fib` pour stocker les résultats intermédiaires et résolvons progressivement les sous-problèmes de Fibonacci en utilisant une approche itérative.

2. **Méthode Top-down (Récursive avec Mémoïsation) :**

- **Définition :**

Dans cette méthode, vous commencez par résoudre le problème global en utilisant la récursion, mais vous stockez les résultats des sous-problèmes déjà résolus dans une table (généralement un dictionnaire) pour éviter de les recalculer.

- **Exemple :**

Résolution du problème du calcul du n-ième nombre de la suite de Fibonacci en utilisant la méthode top-down.

```python

def fibo_top_down(n : int) -> int :

    cache : dict[int , int] = {
        0 : 1 ,
        1 : 1
    }

    def _fibo(n : int) -> int :
        if n in cache :
            return cache[n]
        res = _fibo(n - 1) + _fibo(n - 2)
        cache[n] = res

        return res

    return _fibo(n)
```

Dans cet exemple, nous utilisons un dictionnaire `memo` pour stocker les résultats intermédiaires des sous-problèmes, ce qui nous permet d'éviter de recalculer les mêmes sous-problèmes plusieurs fois lors de l'exécution de la récursion.

#### RQ :

- En résumé, la méthode bottom-up commence par résoudre les sous-problèmes les plus petits et progresse vers le problème global, tandis que la méthode top-down commence par résoudre le problème global en utilisant la récursion et stocke les résultats intermédiaires pour éviter de recalculer les sous-problèmes. Les deux méthodes sont des approches valides pour implémenter la programmation dynamique.

## 3. **Problèmes Classiques :**

- a. **Problème du Sac à Dos (Knapsack) :**
    - Utilisation de la programmation dynamique pour résoudre le problème d'optimisation du sac à dos.

- b. **Calcul de la Distance d'Édition :**
    - Utilisation de la programmation dynamique pour calculer la distance d'édition entre deux chaînes de caractères.

- c. **Plus Longue Sous-Séquence Commune (LCS) :**
    - Application de la programmation dynamique pour trouver la plus longue sous-séquence commune entre deux séquences.

- d. **Alignement de Séquences :**
    - Utilisation de la programmation dynamique pour aligner des séquences de caractères, souvent utilisé en bioinformatique.

- e. **Optimisation de Portefeuille :**
    - Utilisation de la programmation dynamique pour résoudre des problèmes d'optimisation de portefeuille en finance.
