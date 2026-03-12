import heapq
from typing import List 

def heap_sort(nums : List[int])  -> List[int] :
    heapq.heapify(nums)
    res = []
    while nums : 
        res.append(heapq.heappop(nums))
    
    return res 


res = heap_sort([1 , 10 , 3 , 2 , 0 , - 1 , 20 , 10])
print(f"{res =}")
