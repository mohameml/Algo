#!/usr/bin/env python3



"""
---- programme cache aware pour la multiplication des matrices

"""

# matrice A :
A = [
        [1, 0 , 0] ,
        [2, 1 , 2] , 
        [1, 0 , 0] 
    ]

print(f"A = {A}")

# matrice B :
B = [
        [0, 1 , 0] ,
        [0, 2 , 1] , 
        [0, 0 , 1] 
    ]

print(f"B = {B}")


def mult_matrice(A , B):
    
    if(len(A[0])!=len(B)):
        print("Multiplication indéfine")
        exit(1)
    
    n = len(A)
    m = len(B[0])
    l = len(A[0])
    C = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            for k in range(l):
                C[i][j] += A[i][k]*B[k][j]

    return C 




if __name__=='__main__':
    
    C = mult_matrice(A , B)

    print(f"C = {C}")