import math 
from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:

    left , right = 1 , max(piles)

    while left < right : 

        mid = (left + right) // 2

        num_hours_total = sum([math.ceil(p / mid) for p in piles])

        if num_hours_total <= h : 
            right = mid 
        else : 
            left = mid + 1
    
    return left 

piles = [3, 6, 7, 11]
h = 8

print(minEatingSpeed(piles, h))  # Output: 4
