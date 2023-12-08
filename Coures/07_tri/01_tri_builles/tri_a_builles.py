#!/usr/bin/env python3


"""
principe consiste a comparer chaque element par l'element qui le suit et permuter si ne respecte 
pas l'ordre

"""

def sumilation(compteur , tab ):

    # permet la sumaltion de la tri faite par la fonction de tri_a_bailles

    print(f"----------- Etape : {compteur}--------------")
    print(tab)



def tri_bulle(l):

    permission = True

    compteur = 0 
    
    n= len(l)
    
    while permission :
        permission=False

     
        for i in range(n-1):
           if l[i]>l[i+1]:
               l[i],l[i+1]=l[i+1],l[i]
               compteur+=1
               sumilation(compteur,l)
               permission=True
        
        n=n-1 
        # car a  la fin de chaque etape le plus grand element et bien place a la bon place 
        # donc on dumine n en fin de dimunier la complexite
    
    return l



l=[10,23,2,4,5,7,1,4,5,9]

print("--------------------------- Tri à builles -------------------------------")
print("voici la table initale : ")
print(f"\t {l}")


print()
print("---------- On commance le tri ---------")
print()

print(tri_bulle(l))


