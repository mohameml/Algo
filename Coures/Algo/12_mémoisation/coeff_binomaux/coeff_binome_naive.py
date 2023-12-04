#!/usr/bin/env python3




def ceoff_binome_naive(n,p):

    # return C(n,p) 

    if p  > n:
        return 0 
    
    elif p==0 or p==n :
        return 1
    
    else :
       return  ceoff_binome_naive(n-1,p) + ceoff_binome_naive(n-1 , p-1)


# test :

n = 100
p = 20
print(f"C({n},{p}) = {ceoff_binome_naive(n,p)}")  