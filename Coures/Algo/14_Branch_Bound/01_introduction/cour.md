# cour 17 : Principe B&B : Branch and Bound 



## 1. Définition :

- Le principe de "Branch and Bound" est une technique algorithmique utilisée pour résoudre de manière optimale des problèmes d'optimisation combinatoire. Cette approche est couramment employée dans des domaines tels que la recherche opérationnelle, l'algorithmique, et la planification.

Le principe de "Branch and Bound" fonctionne de la manière suivante :

1. **Branch (Ramification)** : Le problème d'optimisation initial est divisé en sous-problèmes plus petits. Cela est fait en identifiant des choix ou des décisions qui peuvent être pris à différents niveaux de l'arborescence de recherche. Chaque choix possible conduit à une branche distincte de l'arbre de recherche.

2. **Bound (Limite)** : Pour chaque nœud de l'arbre de recherche, une borne supérieure (ou inférieure, selon le type de problème) est calculée. Cette borne permet de déterminer si la branche en cours peut potentiellement contenir une solution meilleure que la meilleure solution trouvée jusqu'à présent. Si la borne montre que la branche ne peut pas contenir une solution meilleure, cette branche est élaguée (c'est-à-dire qu'elle est ignorée).

3. **Bound (Limite) stricte** : Les bornes supérieures sont souvent calculées de manière à être des bornes supérieures strictes, ce qui signifie qu'elles sont sûres (elles garantissent qu'aucune meilleure solution n'existe dans cette branche). Si une branche a une borne supérieure strictement inférieure à la meilleure solution connue, elle peut être complètement éliminée.

4. **Optimisation** : La recherche continue dans les branches restantes de l'arbre jusqu'à ce qu'une solution optimale soit trouvée ou jusqu'à ce que toutes les branches aient été explorées. Pendant ce temps, la meilleure solution trouvée est continuellement mise à jour lorsque de meilleures solutions sont découvertes.

Le principe de "Branch and Bound" est particulièrement utile pour résoudre des problèmes NP-difficiles, c'est-à-dire des problèmes d'optimisation pour lesquels il n'existe pas d'algorithme polynomial connu pour trouver une solution optimale en temps raisonnable. En utilisant des bornes astucieuses et en éliminant les branches inutiles, cette technique permet d'explorer efficacement l'espace des solutions tout en garantissant la recherche d'une solution optimale.

Des exemples courants d'utilisation de "Branch and Bound" incluent le problème du voyageur de commerce (TSP), le problème du sac à dos (Knapsack), et d'autres problèmes d'optimisation combinatoire.



Bien sûr, voici un exemple du principe "Branch and Bound" appliqué au problème du voyageur de commerce (TSP), qui est un problème d'optimisation combinatoire classique. Le TSP consiste à trouver le chemin le plus court qui visite un ensemble de villes une seule fois et revient à la ville de départ.

