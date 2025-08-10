# cour 01 : Pb de sac à dos `Knapsack`


### 1. Présentation du Pb : sac à dos biniare 


- Supposons que vous ayez un sac à dos avec une capacité maximale C et une liste de n objets.

- chaque objet $i$ ayant un volume $v_i$ et une valeur $u_i$. 

- L'objectif est de déterminer la meilleure combinaison d'objets à placer dans le sac de manière à maximiser la valeur totale, tout en respectant la capacité de poids maximale du sac.

#### RQ :
Dans le problème du sac à dos binaire on peut prendre un objet une seule fois

- **écriture mathématique du pb :** 

soit $x_i \in \{0,1\}$ tq $x_i = 1$ ssi l'objet $i$ est mis dans la sac .

donc le probélme de sac à dos binaire s'écrit :

$$
\begin{align}
    max \sum_{i=1}^{n}u_i x_i \\
    \sum_{i=1}^{n}v_i x_i &\leq C
\end{align}
$$


### 2. équation de Bellman :

- L'équation de Bellman est un concept clé en programmation dynamique, utilisé pour définir la relation récursive qui permet de résoudre un problème d'optimisation en le décomposant en sous-problèmes plus petits.

- équation de bellman dans le pb de sac à dos :

![équation de bellman](images/eq_bellman.jpeg)


### 3. Prog. récursif naïf :

- **Programme en Python :**

```python

def sacmax(n,V,tab_v,tab_u):

    utilité_max = 0 

    if n==0 :
        utilité_max = 0 
    elif tab_v[n-1] <= V :

        max1 = tab_u[n-1] + sacmax(n-1,V-tab_v[n-1],tab_v,tab_u)
        max2 = sacmax(n-1,V,tab_v,tab_u)

        if max1 > max2 :
            utilité_max = max1 
        else :
            utilité_max = max2 
    else :
        utilité_max = sacmax(n-1,V,tab_v,tab_u)


    return utilité_max



```

- **Compléxité:**

    * La complexité temporelle de l'algorithme  est exponentielle en fonction du nombre d'objets à considérer : $T(n)=\Theta(2^{n})$

    * En effet :

        * Cette complexité est due à la nature récursive de l'algorithme, qui examine toutes les combinaisons possibles d'inclusion et d'exclusion d'objets.

        * l'algorithme explore deux choix possibles (inclusion ou exclusion) pour chaque objet, et cela se fait récursivement pour chaque sous-problème jusqu'à ce que toutes les combinaisons possibles aient été explorées.



.



### 3. Algo de résolution

#### 3.1. Méthode de  Mémoïsation (top_down) :

- **Programme en Python :**

```python

def sacmax_memo(n,V,tab_v,tab_u):

    memo = [[-1 for _ in range(V)] for _ in range(n)]


    def sacmax(n,V,tab_v,tab_u):

        
        if memo[n-1][V-1]!=-1:

            # ce deja calclué 
            return memo[n-1][V-1]
        else :

            # donc c'est pas calculée 

            utilité_max = 0 

            if n==0 :
                utilité_max = 0 

            elif tab_v[n-1] <= V :

                max1 = tab_u[n-1] + sacmax(n-1,V-tab_v[n-1],tab_v,tab_u)
                max2 = sacmax(n-1,V,tab_v,tab_u)

                if max1 > max2 :
                    utilité_max = max1 
                else :
                    utilité_max = max2 
            else :
                utilité_max = sacmax(n-1,V,tab_v,tab_u)

            memo[n-1][V-1]=utilité_max

        return utilité_max 


    return sacmax(n,V,tab_v,tab_u) 

```


- **Mémoïsation avec choix optimaux :**

#### Méthode 1 :
```python


"-------------------    Méthode 1 ----------------------------"

def sac_max_memo_choix_optimaux(n,V,tab_v,tab_u):


    memo = {} 
    # dictionnaire de clés (n,V) avec n le nombre d'objets et V le volume de sac 
    # tq : memo[(n,V)]= (nb_max , list_objets_de_choix)


    def sac_max(n,V):

        if n==0 :
            return 0,[]
        
        else :

            if (n,V) in memo :

                return memo[(n,V)]

            if tab_v[n-1]<= V :

                val_max1 , choix1 = sac_max(n-1,V-tab_v[n-1])
                val_max2 , choix2 = sac_max(n-1,V)

                if val_max1 + tab_u[n-1] > val_max2 :
                    val_max = val_max1 + tab_u[n-1]
                    choix = choix1 + [n-1]
                else :

                    val_max =val_max2
                    choix = choix2
            else :
                val_max , choix = sac_max(n-1,V)

        
            memo[(n,V)] = (val_max,choix)
            
            return val_max , choix
    sac_max(n,V) 

    return memo[(n,V)]



```

- **Expliquation :**

    - Si `n` est égal à 0 (c'est-à-dire aucun objet disponible), alors la valeur maximale est 0 et aucun objet n'est choisi.
    
    - Sinon, l'algorithme vérifie si les résultats pour la paire `(n, V)` ont déjà été calculés en vérifiant si elle est présente dans `memo`.
    
    - Si les résultats sont déjà dans `memo`, l'algorithme les récupère directement.
    
    - Si le volume de l'objet `n-1` est inférieur ou égal à la capacité restante `V`, alors l'algorithme explore deux options :
        
        - L'objet `n-1` est choisi : il appelle récursivement `sac_max` avec `n-1` objets et une capacité réduite de `tab_v[n-1]` et met à jour `val_max` et `choix` en conséquence.
        
        - L'objet `n-1` n'est pas choisi : il appelle récursivement `sac_max` avec `n-1` objets et la même capacité `V`, puis met à jour `val_max` et `choix` en conséquence.
        
    - Si le volume de l'objet `n-1` est supérieur à la capacité restante `V`, alors l'algorithme appelle récursivement `sac_max` avec `n-1` objets et la même capacité `V`, sans choisir l'objet `n-1`.
    
    - Une fois que les résultats optimaux pour `(n, V)` ont été déterminés, ils sont stockés dans `memo` et renvoyés.
    
    - En fin de compte, l'algorithme renvoie la valeur maximale que l'on peut obtenir et la liste des indices des objets choisis pour atteindre cette valeur maximale.



#### Méthode 2 :

```python


def sacmax_memo_choix_optimaux(n,V,tab_v,tab_u):

    memo = [[-1 for _ in range(V)] for _ in range(n)]

    def sacmax(n,V,tab_v,tab_u):

         

        if memo[n-1][V-1]!=-1:

            # ce deja calclué 
            return memo[n-1][V-1]
        else :

            # donc c'est pas calculée 

            utilité_max = 0 

            if n==0 :
                utilité_max = 0 

            elif tab_v[n-1] <= V :

                max1 = tab_u[n-1] + sacmax(n-1,V-tab_v[n-1],tab_v,tab_u)
                max2 = sacmax(n-1,V,tab_v,tab_u)

                if max1 > max2 :
                    utilité_max = max1
            
                    
                else :
                    utilité_max = max2 
                    
            else :
                utilité_max = sacmax(n-1,V,tab_v,tab_u)
                

            memo[n-1][V-1]=utilité_max

             

        return utilité_max 



    sacmax(n,V,tab_v,tab_u)

    

    # Reconstruction de la liste des objets choisis pour obtenir la valeur maximale.
    choix = [0 for _ in range(n)]
    i, w = n-1, V-1 
    while i >= 0 and w >= 0:
        if memo[i][w] != memo[i - 1][w]:
            choix[i]=1
            w -= tab_v[i]
        i -= 1


    return choix

```

- **Expliquation :** 



- L'algorithme utilise une matrice `memo` de dimensions `(n, V)` pour stocker les résultats des sous-problèmes déjà résolus. La valeur `-1` dans `memo` indique que le résultat pour cette combinaison de `(n, V)` n'a pas encore été calculé.

- L'algorithme utilise une fonction récursive `sacmax` qui prend en compte les objets disponibles, la capacité restante du sac et les choix effectués. 

- La fonction suit les étapes suivantes :

    1. Si le résultat pour `(n, V)` est déjà calculé et stocké dans `memo`, l'algorithme renvoie directement cette valeur, évitant ainsi un calcul inutile.

    2. Si le résultat pour `(n, V)` n'est pas déjà enregistré dans `memo`, l'algorithme continue à calculer la valeur maximale (`utilité_max`) que l'on peut obtenir avec les `n` premiers objets et une capacité de sac de `V`.

    3. Si `n` est égal à 0 (c'est-à-dire aucun objet disponible), la `utilité_max` est de 0.

    4. Si le volume de l'objet `n-1` est inférieur ou égal à la capacité restante `V`, l'algorithme explore deux options :
    - L'objet `n-1` est choisi : il appelle récursivement `sacmax` avec `n-1` objets et une capacité réduite de `tab_v[n-1]`, puis met à jour `utilité_max` en conséquence.
    - L'objet `n-1` n'est pas choisi : il appelle récursivement `sacmax` avec `n-1` objets et la même capacité `V`, puis met à jour `utilité_max` en conséquence.

    5. Si le volume de l'objet `n-1` est supérieur à la capacité restante `V`, l'algorithme appelle récursivement `sacmax` avec `n-1` objets et la même capacité `V`, sans choisir l'objet `n-1`.

    6. Une fois que `utilité_max` est calculée, elle est stockée dans `memo` pour éviter de recalculer la même valeur.

    7. En fin de compte, l'algorithme renvoie la `utilité_max` maximale que l'on peut obtenir en choisissant les objets dans le sac.

    8. Après avoir appelé la fonction `sacmax(n, V, tab_v, tab_u)`, l'algorithme reconstruit la liste des objets choisis pour obtenir la valeur maximale. Cela se fait en parcourant `memo` de bas en haut et de droite à gauche, en vérifiant si la valeur actuelle diffère de la valeur immédiatement supérieure dans `memo`. Si c'est le cas, cela signifie que l'objet correspondant a été choisi, et son indice est ajouté à la liste `choix`.



- **Complexité :**

    * La complexité temporelle de cet algorithme est de l'ordre de O(n*V), où "n" est le nombre d'objets à considérer et "V" est la capacité maximale du sac à dos.

    * La mémoïsation permet d'éviter le recalcul des mêmes sous-problèmes, car les résultats sont stockés dans la matrice `memo`. Ainsi, chaque sous-problème est calculé une seule fois, ce qui réduit considérablement le nombre total d'opérations nécessaires pour résoudre le problème.




#### 3.2  Méthode Bottom-up :


- **Analyse dépendances :**
Dans l'algo de Bottom-up il faut d'abord faire l'analyse de dépendeces pour trouver un order toplogique 

![analyse](images/analyse.jpeg)


- **Programme en Python :**

```python
def knapsack_bottom_up(values, weights, W):
    n = len(values)

    # Création d'une matrice pour stocker les résultats intermédiaires.
    # dp[i][w] représente la valeur maximale avec les i premiers objets et une capacité w.
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Remplissage du tableau dp par itération sur les objets et les capacités.
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # Si le poids de l'objet est supérieur à la capacité w, on ne peut pas le prendre.
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Sinon, on choisit le maximum entre l'inclusion et l'exclusion de l'objet.
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # La valeur maximale se trouve dans dp[n][W].
    max_value = dp[n][W]

    # Reconstruction de la liste des objets choisis pour obtenir la valeur maximale.
    chosen_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return max_value, chosen_items

```

- **Complexité :**

    * La complexité de la méthode bottom-up est  O(n * W), où n est le nombre d'objets et W est la capacité maximale du sac à dos







