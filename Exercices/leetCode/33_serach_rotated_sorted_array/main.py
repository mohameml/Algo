from typing import List

def search(nums: List[int], target: int) -> int:
    def search_index_min(nums : list[int]) -> int : 

        left = 0 
        right = len(nums) - 1 

        while left < right : 

            mid = left + (right - left) // 2

            if nums[mid] < nums[right] : 
                right = mid 
            else : 
                left  = mid + 1
        return left 



    def binary_search_algo(nums : list[int] , target : int) -> int : 

        left = 0
        right = len(nums) - 1

        while left <= right : 

            mid = left + (right  - left) // 2

            if  target > nums[mid]  : 
                left = mid + 1
            elif target < nums[mid] : 
                right = mid  - 1
            else :
                return mid 

        return - 1


    if len(nums) == 0 :
        return - 1

    if len(nums) == 1 :
        if nums[0] == target :
            return 0 
        else : 
            return - 1

    index_min = search_index_min(nums)

    l1 = nums[:index_min]
    l_2 = nums[index_min :]

    if target <= l_2[-1] : 
        res = binary_search_algo(l_2 , target)
        if res != - 1 : 
            return index_min + res 
        
        return res 

    if len(l1)!=0 and target >= l1[0] : 
        return binary_search_algo(l1 , target)
    

    return - 1 


#  Test 1 : 
nums = [4,5,6,7,0,1,2]
target = 0
res = search(nums , target)
print(res) # 4 

# Test 2 : 
nums = [4,5,6,7,0,1,2]
target = 3
res = search(nums , target)
print(res) # - 1


# Test 3 :
nums = [1]
target = 0
res = search(nums , target)
print(res) # - 1

# Test 4 : 
nums = [4,5,6,7,0,1,2]
target = 2
res = search(nums , target)
print(res) # 6


# Test 5 : 
nums = [4,5,6,7,0,1,2]
target = 1
res = search(nums , target)
print(res) # 5


# Test 6 : 
nums = [4,5,6,7,0,1,2]
target = 5
res = search(nums , target)
print(res) # 1


# Test 7 : 
nums = [4,5,6,7,0,1,2]
target = 7
res = search(nums , target)
print(res) # 3

# Test 8 : 
nums = [4,5,6,7,0,1,2]
target = 4
res = search(nums , target)
print(res) # 0

# Test 9 : 

nums = [0,1,2 , 4 , 6 , 8]
target = 2
res = search(nums , target)
print(res) # 2


# Test 10 : 

# nums = [1]
# target = 2
# res = search(nums , target)
# print(res) # 2


# Test 11 : 
nums = [3 , 1]
target = 0
res = search(nums , target)
print(res) # - 1
