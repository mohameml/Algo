# cour : Binary Search 

- L'algorithme de recherche dichotomique, également connu sous le nom de recherche binaire, est une technique efficace pour rechercher un élément spécifique dans un ensemble de données triées. 

- Cette méthode divise répétitivement l'ensemble de données en deux moitiés et compare l'élément recherché avec l'élément au milieu. En fonction de la comparaison, l'algorithme réduit la plage de recherche de moitié à chaque itération jusqu'à ce que l'élément soit trouvé ou que la plage de recherche soit réduite à zéro.

- Voici comment fonctionne l'algorithme de recherche dichotomique :

1. Triez l'ensemble de données dans l'ordre croissant. La recherche dichotomique ne fonctionne que sur des données triées.

2. Initialisez deux indices, `début` et `fin`, pour représenter la plage de recherche initiale. Au début, `début` est l'indice du premier élément de l'ensemble de données et `fin` est l'indice du dernier élément.

3. Tant que `début` est inférieur ou égal à `fin`, répétez les étapes suivantes :

   a. Calculez l'indice du milieu de la plage de recherche en utilisant la formule `milieu = (début + fin) // 2`.

   b. Comparez l'élément au milieu de la plage (`ensemble_de_données[milieu]`) avec l'élément recherché.

   c. Si les deux éléments sont égaux, vous avez trouvé l'élément recherché. Retournez l'indice `milieu`.

   d. Si l'élément au milieu est plus petit que l'élément recherché, mettez à jour `début` pour être `milieu + 1` pour réduire la plage de recherche à la moitié supérieure.

   e. Si l'élément au milieu est plus grand que l'élément recherché, mettez à jour `fin` pour être `milieu - 1` pour réduire la plage de recherche à la moitié inférieure.

4. Si l'élément recherché n'est pas trouvé après avoir terminé la boucle, retournez une valeur indiquant que l'élément n'est pas présent dans l'ensemble de données.

L'algorithme de recherche dichotomique est très efficace pour rechercher des éléments dans de grandes ensembles de données triées car il réduit la plage de recherche de manière exponentielle à chaque itération, ce qui donne une complexité de temps logarithmique, soit O(log n), où n est la taille de l'ensemble de données.