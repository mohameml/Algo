#!/usr/bin/env python3
from time import time

# Algo naif 

def rendue_monie(S,P):

    nb_min = 0 

    if S==0 :
        nb_min = 0
    
    elif S < 0 :

        nb_min = float("inf")
    
    else :
        min1 = rendue_monie(S-P[0],P)

        for k in range(1,len(P)):
            
            if rendue_monie(S-P[k],P) < min1  :

                min1 = rendue_monie(S-P[k],P)

        nb_min = 1 + min1


    return nb_min

# Algo avec mémoisation 


def rendue_monie_memo(S,P):


    memeo = {}

    def rendue_monie(S,P):

        nb_min = 0

        if S in memeo :
            
            return memeo[S]

        else :

            if S==0 :
                nb_min = 0
            
            elif S < 0 :

                nb_min = float("inf")
            
            else :
                min1 = rendue_monie(S-P[0],P)

                for k in range(1,len(P)):
                    
                    if rendue_monie(S-P[k],P) < min1  :

                        min1 = rendue_monie(S-P[k],P)

                nb_min = 1 + min1

                memeo[S]=nb_min


        return nb_min


    return rendue_monie(S,P)



# Listes de piéces à rendu 


def rendue_list_monie_memo(S,P) :

    list_monie = [0 for _ in range(len(P))]  # list de 0,1 tq l[i]=1 ssi p_i est rendue 
    
    def rendue_liste_monie(S,P):

        nb_min = 0 


        if S==0 :
            nb_min = 0
        
        elif S < 0 :

            nb_min = float("inf")
        
        else :
            min1 = rendue_liste_monie(S-P[0],P)
            indice_min = 0

            for k in range(1,len(P)):
                
                if rendue_liste_monie(S-P[k],P) < min1  :

                    min1 = rendue_liste_monie(S-P[k],P)
                    indice_min = k

            list_monie[indice_min]=1                

            nb_min = 1 + min1

        return nb_min


    rendue_liste_monie(S,P)
    
    return list_monie














# Test 
P=[1,5,10]
S = 11


t1 = time()
print(rendue_monie(S,P))
t2 = time()
print(f"le temps d'éxecution de Algo naif est {t2-t1}")
print(rendue_list_monie_memo(S,P))

t3 = time()
print(rendue_monie_memo(S,P))
t4 = time()
print(f"le temps d'éxecution de Algo avec memo est {t4-t3}")
