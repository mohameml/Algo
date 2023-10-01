# Tri à builles 


- **Définition :**

    * Le tri à bulles (Bubble Sort en anglais) est un algorithme de tri simple qui fonctionne en comparant et en échangeant les éléments adjacents dans un tableau jusqu'à ce que tout le tableau soit trié (sur place). 
    
    * C'est l'un des algorithmes de tri les moins efficaces en termes de temps d'exécution, mais il est facile à comprendre et à mettre en œuvre. 


Voici comment fonctionne le tri à bulles, suivi d'une analyse de sa complexité.

- **Principe:**

    * **Étape 1 :** Le tableau est parcouru de gauche à droite, et à chaque paire d'éléments adjacents, on compare les deux  éléments. Si l'élément de gauche est plus grand que l'élément de droite, on les échange. Sinon, on les laisse en place.

    * **Étape 2 :** On répète cette comparaison et cet échange pour chaque paire d'éléments adjacents à travers tout le tableau. Cela garantit que le plus grand élément se déplace vers la fin du tableau lors de chaque itération.

    * **Étape 3 :** Une fois que la première itération est terminée, le plus grand élément se trouve à la fin du tableau. On répète alors le processus, mais cette fois-ci en ignorant le dernier élément (car il est déjà trié). On continue ce processus jusqu'à ce que tout le tableau soit trié.


- **Exemple :**
    Voici un exemple simple en utilisant un tableau de nombres :

    ```
    Avant le tri : 5 2 9 3 6
    1ère itération : 2 5 3 6 9 (échange de 5 et 2)
    2ème itération : 2 3 5 6 9 (échange de 5 et 3)
    3ème itération : 2 3 5 6 9 (pas d'échange, le tableau est trié)
    ```



- **Algo :**

    ```python
    
    def tri_bulle(l):

        permission = True
                
        n= len(l)
        
        while permission :
            permission=False

        
            for i in range(n-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                permission=True
            
            n=n-1 
            # car a  la fin de chaque etape le plus grand element et bien place a la bon place 
            # donc on dumine n en fin de dimunier la complexite
        
        return l    
    
    
    
    ```

- **Complexité :**


    * **Complexité dans le pire des cas :**
        - Comparaisons : $O(n^2)$
        - Échanges : $O(n^2)$


    * **Complexité dans le meilleur des cas :**
        - Comparaisons : $O(n)$
        - Échanges : 0 (pas d'échange)

    * **Complexité dans le meilleur des cas :**

        - Dans le cas moyen, la complexité est généralement proche du pire des cas, ce qui en fait un algorithme de tri peu  efficace pour des ensembles de données de grande taille.