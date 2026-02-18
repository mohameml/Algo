


def search_v1(nums : list[int] , target : int) -> int : 
    l , r = 0 , len(nums) - 1 

    while l < r : 
        mid = (l + r) // 2 
        
        if nums[mid] == target : 
            return   mid 
        elif nums[mid] < target : 
            l = mid + 1 
        else :
            r = mid 
    
    return -1 

def binary_search(nums: list[int] , target : int) -> int : 
    l , r = 0 , len(nums)
    while l < r : 
        mid = (l + r) // 2
        
        if nums[mid] < target : 
            l = mid + 1 
        else :
            r = mid 
    return l 

def search_v2(nums : list[int] , target : int) -> int : 
    l  = binary_search(nums , target)

    if l < len(nums) and nums[l] == target : 
        return l 
    return - 1


def find_first_occur_negative_number(nums : list[int] ) -> int : 
    """  
    - nums : list of int sorted in no-increasing order 
    """
    
    l , r = 0 , len(nums)

    while l < r : 
        mid = (l + r) // 2 

        if nums[mid] >= 0 : 
            r = mid 
        else : 
            break 
    return l 


if __name__ == "__main__" : 


    nums = [-1,0,3,5,9,12]
    target = 9

    print(f"Find Traget : {search_v1(nums , target)}")

    nums = [-1,0,3,5,9,12]
    target = 10

    print(f"Find Traget : {search_v2(nums , target)}")
    