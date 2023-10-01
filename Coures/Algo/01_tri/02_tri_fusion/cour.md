# Tri par fusion 


- **Définition :**


- L'algorithme de tri fusion est un algorithme de tri très efficace basé sur le principe de la division et de la fusion.

 
- **Principe :**

    - L'algorithme de tri fusion est basé sur le principe de diviser et régner. 

    - Il divise la liste non triée en plusieurs sous-listes jusqu'à ce que chaque sous-liste ne contienne qu'un seul élément. 

    - Ensuite, il fusionne progressivement ces sous-listes en une seule liste triée. 

    1. **Diviser** : Divisez la liste non triée en deux moitiés égales. Cela se fait récursivement jusqu'à ce que chaque sous-liste ne contienne qu'un élément.

    2. **Fusionner** : Fusionnez deux sous-listes triées en une seule liste triée. Cela se fait récursivement jusqu'à ce que toutes les sous-listes soient fusionnées en une seule liste triée.

    3. **Terminer** : Lorsque toutes les sous-listes sont fusionnées, vous obtenez la liste triée finale.


- **Algo:**

    ```python
    #!/usr/bin/env python3


    def fusion(l1,l2):

        "tout d'abord une fonction qui fusion deux liste trieès"


        l=[]
        i1,i2=0,0
        while i1<len(l1) and i2<len(l2):
            if l1[i1]<l2[i2]:
                l.append(l1[i1])
                i1+=1
            else:
                l.append(l2[i2])
                i2+=1
        if i1<len(l1):
            for i in range(i1,len(l1)):
                l.append(l1[i])
        else:
            for i in range(i2,len(l2)):
                l.append(l2[i])
        return l




    "fonction qui tri une liste par methode fusion   "

    def tri_fusion(l):
        if len(l)<=1:
            return l
        else:
            m=len(l)//2
            return  fusion(tri_fusion(l[m:]),tri_fusion(l[:m]))


    ```

- **Complexité :**


    - **Complexité temporelle** : Le tri fusion a une complexité temporelle moyenne et dans le pire cas de O(n log n), où "n" est le nombre d'éléments dans la liste. C'est ce qui en fait l'un des algorithmes de tri les plus efficaces pour les grandes listes.

    - **Complexité spatiale** : Le tri fusion nécessite une mémoire supplémentaire pour stocker les sous-listes lors de la fusion. Sa complexité spatiale est donc de O(n), où "n" est le nombre d'éléments dans la liste.

