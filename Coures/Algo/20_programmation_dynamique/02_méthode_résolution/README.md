# cour 2 : Les Méthodes des Résolution en PD 


La programmation dynamique peut être mise en œuvre de deux manières principales : la méthode bottom-up (ou itérative) et la méthode top-down (ou récursive avec mémoïsation). 

1. **Méthode Bottom-up (Itérative) :**

- **Définition :** 

Dans cette méthode, vous commencez par résoudre les sous-problèmes les plus petits et construisez progressivement la solution du problème global en utilisant les résultats des sous-problèmes. Vous travaillez généralement à partir du bas (d'où le terme "bottom-up") vers le haut.

- **Exemple :** 

Résolution du problème du calcul du n-ième nombre de la suite de Fibonacci (Fibonacci(n)) en utilisant la méthode bottom-up.

```python
def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

```

Dans cet exemple, nous utilisons un tableau `fib` pour stocker les résultats intermédiaires et résolvons progressivement les sous-problèmes de Fibonacci en utilisant une approche itérative.


2. **Méthode Top-down (Récursive avec Mémoïsation) :**


- **Définition :**

Dans cette méthode, vous commencez par résoudre le problème global en utilisant la récursion, mais vous stockez les résultats des sous-problèmes déjà résolus dans une table (généralement un dictionnaire) pour éviter de les recalculer.

- **Exemple :** 

Résolution du problème du calcul du n-ième nombre de la suite de Fibonacci en utilisant la méthode top-down.

```python

def fibo_mem(n) :

    # Table de mémoisation 
    memo = {}

    def fibonacci_top_down(n):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
        
        memo[n] = result
        return result

    return fibonacci_top_down(n)


```

Dans cet exemple, nous utilisons un dictionnaire `memo` pour stocker les résultats intermédiaires des sous-problèmes, ce qui nous permet d'éviter de recalculer les mêmes sous-problèmes plusieurs fois lors de l'exécution de la récursion.




#### RQ :

- En résumé, la méthode bottom-up commence par résoudre les sous-problèmes les plus petits et progresse vers le problème global, tandis que la méthode top-down commence par résoudre le problème global en utilisant la récursion et stocke les résultats intermédiaires pour éviter de recalculer les sous-problèmes. Les deux méthodes sont des approches valides pour implémenter la programmation dynamique.