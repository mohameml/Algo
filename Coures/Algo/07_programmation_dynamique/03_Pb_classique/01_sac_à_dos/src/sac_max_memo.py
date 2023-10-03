#!/usr/bin/env python3







# Pb de sac à dos : Algo Top-down avec mémoisation :

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


"""
--------------------------------------------- Test -------------------------------------

"""



# Test 
tab_v = [1,3,2,4,5]
tab_u = [2,3,1,4,5]

max = sacmax_memo(5,12,tab_v,tab_u)

# m2 = knapsack_top_down(tab_u,tab_v,12,5)


print("------------ Probélme de sac à dos -----------------------")
print(f"Sac C ={12} , le nombrés des objets n={5}")
print(f"voici la table des voulmes des objets {tab_v}")
print(f"voicii la liste des utilités des objets {tab_u}")
print()
print(f"Donc l'utilité max de sac est : ........... {max}")



# Test 2 :

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

print("--------------- Test 2 ---------------------------")
C = 12
tab_u_1 =[6,5,10,13]
tab_v_1 = [2,3,5,7]

print(f"la valeur de l'uitlité maximale de se sac est {sacmax_memo(4,C,tab_v_1,tab_u_1)}")