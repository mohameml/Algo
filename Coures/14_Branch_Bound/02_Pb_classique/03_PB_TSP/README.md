#### Problème du Voyageur de Commerce (TSP) avec Branch and Bound :

Supposons que nous ayons les villes suivantes avec les distances entre elles :

- A -> B : 10
- A -> C : 15
- A -> D : 20
- B -> C : 35
- B -> D : 25
- C -> D : 30

**Étape 1 - Création de l'arbre de recherche initial :**
Nous commençons par créer un arbre de recherche où chaque nœud représente une ville à visiter. Dans l'arbre initial, nous avons la ville de départ A, et trois villes restantes B, C, et D.

```
      A
    / | \
   B  C  D
```

**Étape 2 - Calcul des bornes supérieures :**
Pour chaque nœud de l'arbre, nous calculons une borne supérieure basée sur le chemin le plus court actuel depuis la ville de départ vers les villes restantes. Par exemple, pour le nœud B, la borne supérieure est 10 (A -> B), et pour le nœud C, la borne supérieure est 15 (A -> C).

```
      A
    / | \
   B(10) C(15) D
```

**Étape 3 - Exploration des branches :**
Nous choisissons la ville avec la plus basse borne supérieure pour explorer en premier. Dans cet exemple, nous choisissons B (10) car c'est la plus basse. Ensuite, nous explorons toutes les branches possibles à partir de B.

```
      A
     / \
   B(10) C(15) D
  /
C(35) D(25)
```

Nous continuons à explorer les branches, calculons les bornes supérieures, et éliminons les branches inutiles en utilisant des bornes strictes.

**Étape 4 - Trouver la solution optimale :**
Nous continuons à explorer les branches de l'arbre jusqu'à ce que toutes les branches aient été explorées ou que nous ayons trouvé une solution meilleure que la meilleure solution connue jusqu'à présent. À la fin, nous trouvons la solution optimale, qui est le chemin le plus court.

L'approche "Branch and Bound" nous permet d'explorer de manière efficace un grand nombre de combinaisons possibles tout en éliminant rapidement les branches qui ne peuvent pas contenir une solution optimale. Cela garantit que nous finirons par trouver la solution optimale pour le problème du voyageur de commerce.