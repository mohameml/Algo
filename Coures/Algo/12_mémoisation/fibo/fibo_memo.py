#!/usr/bin/env python3


from time import time 


def memoize( n) :

    dict_f = {0:0,1:1}


    def fibo_mem(n):
        if n in dict_f :
            return dict_f[n]
        else :
            res = fibo_mem(n-1)+fibo_mem(n-2)
            dict_f[n]=res 
        return res

    return fibo_mem(n)
    






# Test 

t3 = time()
print(memoize(1000))
t4 = time()

print(f"le temps de clacul de mem_fibo(30) est {t4 - t3} ")




