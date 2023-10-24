#!/usr/bin/env python3



def binome_ord(n,p):

    T = [[1 for _ in range(p+1)] for _ in range(n-p+1) ]

    for j in range(1,p+1):
        for i in range(1,n-p+1):
            T[i][j] = T[i][j-1] + T[i-1][j]

    
    return T[n-p][p]



n = 100
p = 20
print(f"C({n},{p}) = {binome_ord(n,p)}")  