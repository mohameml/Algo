#!/usr/bin/env python3


from time import time 



def fibo_ordo(n) :

    list_f = [0 for _ in range(n+1)]

    list_f[0] = 0 
    list_f[1] = 1 

    for i in range(2,n+1) :
        list_f[i]=list_f[i-1]+list_f[i-2]

    
    return list_f[n]




# Test 




t1 = time()
print(fibo_ordo(100))
t2 = time()

print(f"le temps de clacul de fibo(30) est {t2 - t1} ")


