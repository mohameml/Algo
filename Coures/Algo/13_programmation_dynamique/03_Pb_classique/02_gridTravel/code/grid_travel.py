#!/usr/bin/env python3



def grid_travel_naive(m ,n):

    if n==1 and m==1 :
        return 1 
    if n==0 or m==0 :
        return 0 
    
    return grid_travel_naive(m-1,n)+grid_travel_naive(m , n-1)


# print(f"nombre de cas possible pour m = 2 , n =3 est : {grid_travel_naive(2 ,3)}") # 3 
# print(f"nombre de cas possible pour m = 3 , n =3 est : {grid_travel_naive(3 ,3)}") #  6 
# print(f"nombre de cas possible pour m = 18 , n = 18 est : {grid_travel_naive(18 ,18)}")






def grid_traveler(m, n, memo={}):
    key = (m, n)
    
    if key in memo:
        return memo[key]
    
    if m == 1 and n == 1:
        return 1
    
    if m == 0 or n == 0:
        return 0
    
    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]

print(f"nombre de cas possible pour m = 2 , n =3 est : {grid_traveler(2 ,3)}") # 3 
print(f"nombre de cas possible pour m = 3 , n =3 est : {grid_traveler(3 ,3)}") #  6 
print(f"nombre de cas possible pour m = 18 , n = 18 est : {grid_traveler(18 ,18)}") #  2333606220