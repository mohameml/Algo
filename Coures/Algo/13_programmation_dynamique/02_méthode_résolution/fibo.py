#!/usr/bin/env python3


# méthode naive 

def fibo(n):
    
    if(n<=1):
        return 1 
    else :
        return fibo(n-1)+fibo(n-2)
    


# méthode Bottom-up 


def fibonacci_bottom_up(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# méthode Top-down 

def fibo_mem(n) :

    # Table de mémoisation 
    memo = {}

    def fibonacci_top_down(n):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
        
        memo[n] = result
        return result

    return fibonacci_top_down(n)