#!/usr/bin/env python3


from time import time 


def fibo(n):

    if n <= 1 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)



# Test 


t1 = time()
print(fibo(100))
t2 = time()

print(f"le temps de clacul de fibo(30) est {t2 - t1} ")


