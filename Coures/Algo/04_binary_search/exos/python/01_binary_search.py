"""
Exo1 : 

- find a traget in array of intergs (sorted in non-decrsing ordered)
- Complexity :O(log(n)) with n = len(nums)

----
times : 1 (the number of tims taht i did this exo)
"""
from typing import List 

def binary_search(nums : List[int], target :int) -> bool:
    ... 
    
    

if __name__ == "__main__" : 
    nums = [1 , 3 , 4, 6 , 7]        
    print(f"res : {binary_search(nums , target=4)}")
    print(f"res : {binary_search(nums , target=10)}")
    
    