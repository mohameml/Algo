#!/usr/bin/env python3



# Pb de sac à dos : Algo  Mémoïsation avec choix optimaux


def sacmax_memo_choix_optimaux(n,V,tab_v,tab_u):

    memo = [[-1 for _ in range(V)] for _ in range(n)]

    
    mat_objet = [[0 for _ in range(n)] for _ in range(V)]  # tab_objet[V_i][i] = 1 ssi la mis en sac (de volume V_i) de l'objet i est optimal 


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
                    mat_objet[V-1][n-1]= 1  # si max1 > max2 donc le choix de l'objet n-1 est optimale pour le volume V(d'indice V-1) 
                    
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



def sac_max_choix_optimaux(n,V,tab_v,tab_u):


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
                    











"""
--------------------------------------------- Test -------------------------------------

"""



# Test 1 :

"""
Exemple 1 :

Capacité maximale du sac à dos (W) : 10
Objets disponibles :
Objet 1 : Poids = 2, Valeur = 6
Objet 2 : Poids = 3, Valeur = 5
Objet 3 : Poids = 5, Valeur = 10
Objet 4 : Poids = 7, Valeur = 13
Solution : 
Les objets à placer dans le sac pour maximiser la valeur tout en respectant la capacité de poids

maximale sont l'objet 1, l'objet 2 et l'objet 4. La valeur totale sera de 6 + 5 + 13 = 24.




"""

print("--------------- Test  ---------------------------")
C = 12
tab_u_1 =[6,5,10,13]
tab_v_1 = [2,3,5,7]

print(f"les choix optimaux sont {sacmax_memo_choix_optimaux(4,C,tab_v_1,tab_u_1)}")
print(f"les choix optimaux sont {sac_max_choix_optimaux(4,C,tab_v_1,tab_u_1)}")




