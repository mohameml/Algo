#!/usr/bin/env python3


def fibo(n):
    if n < 2 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)
    

# print(f"fibo(5) = {fibo(5)}")
# print(f"fibo(10) = {fibo(10)}")
# print(f"fibo(50) = {fibo(50)}")



def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 2 :
        return n 
        
    memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    
    return memo[n]


print(f"fibo(5) = {fibo_memo(5)}")
print(f"fibo(10) = {fibo_memo(10)}")
print(f"fibo(50) = {fibo_memo(50)}")
