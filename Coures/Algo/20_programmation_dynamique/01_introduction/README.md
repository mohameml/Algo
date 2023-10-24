# cour 01 : Introduction à la programmation dynamique 




### 1.**Définition :**


- La programmation dynamique est  une technique algorithmique couramment utilisée pour résoudre des problèmes liés à l'optimisation. 

- Elle consiste à résoudre un problème en le décomposant en sous-problèmes plus petits et en utilisant une approche itérative pour stocker et réutiliser les solutions aux sous-problèmes. 

- Cette technique est souvent utilisée pour résoudre des problèmes où il est nécessaire de trouver la meilleure solution parmi un grand nombre de solutions possibles.


### 2. **Les caractéristiques clés de la programmation dynamique :** 

Les caractéristiques clés de la programmation dynamique comprennent :

1. **Décomposition en sous-problèmes** : Un problème plus complexe est divisé en sous-problèmes plus simples et plus petits qui peuvent être résolus individuellement.

2. **Stockage des résultats intermédiaires** : Les solutions aux sous-problèmes sont stockées dans une table ou un tableau pour éviter de recalculer les mêmes résultats plusieurs fois.

3. **Approche itérative** : La résolution du problème se fait de manière itérative en utilisant les solutions aux sous-problèmes pour construire progressivement la solution finale.

4. **Principe de l'optimalité** *(Principe d’optimalité de Bellman)*: 

    - une solution optimale est construite en combinant des solutions optimales de sous-problèmes

    -  le sous-structure  d'un structure optimale est un structure optimale .
 



#### RQ : la différence entre `Diviser pour régner` et  `Programmation dynamique` :

-  **Diviser pour régner** : 
    
    - divise un problème en sous-problèmes  indépendants (qui ne se chevauchent pas), 
    
    - résout chaque  sous-problème, 
    
    - et combine les solutions des sous problèmes pour former une solution du problème initial.

- **Programmation dynamique** : 
    
    - divise un problème en sous problèmes qui sont non indépendants (qui se chevauchent).

    - cherche (et stocke) des solutions de sous-problèmes .

    - une solution optimale est construite en combinant des solutions optimales de sous-problèmes










