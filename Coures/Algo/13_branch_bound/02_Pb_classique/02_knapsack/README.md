#  Problème du sac à dos : **``Knapsack``**


## 1. Description :

Exemple avec le problème du sac à dos (Knapsack) :

Supposons que nous ayons les objets suivants avec des poids et des valeurs respectifs :

| Objet | Poids | Valeur |
|-------|-------|--------|
| A     | 2     | 5      |
| B     | 3     | 8      |
| C     | 5     | 13     |
| D     | 7     | 21     |

Capacité maximale du sac à dos = 10.

1. **Initialisation :**
   - Solution partielle initiale : Aucun objet sélectionné.
   - Borne supérieure initiale : Très grande (pas de limite).

2. **Boucle principale :**
   - Commencez avec le sous-problème initial (sac à dos vide).
   - Divisez-le en deux sous-problèmes : un avec l'objet A inclus et l'autre sans.
   - Calculez les bornes inférieures et supérieures pour chaque sous-problème.
   - Mettez les sous-problèmes dans la file de priorité.

3. **Terminaison :**
   - Continuez jusqu'à ce que la file de priorité soit vide.

4. **Résultat :**
   - La meilleure solution trouvée est la solution partielle associée à la meilleure borne supérieure.

L'algorithme "Branch and Bound" est une technique générale, et la mise en œuvre spécifique dépend du problème particulier que vous essayez de résoudre. Les bornes inférieures et supérieures doivent être calculées de manière appropriée en fonction des contraintes du problème.