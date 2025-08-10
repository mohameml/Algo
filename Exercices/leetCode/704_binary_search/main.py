from typing import List


def binary_search(nums: List[int], target: int) -> int:

    left , rigth = 0 , len(nums) - 1
    
    while left <= rigth : 
        mid = left + rigth // 2 
                
        if target > nums[mid] : 
            left = mid + 1
        elif target < nums[mid] :
            rigth = mid - 1
        else : 
            return mid 

    
    return - 1




# print(binary_search([-1,0,3,5,9,12] , 2))
# print(binary_search([5] , -5))
print(binary_search([0 , 1 , 2] , 0))



