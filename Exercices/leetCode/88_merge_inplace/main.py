from typing import List 

def add_right_pos(nums : List[int] , k : int)  : 
    l , r =  0 , len(nums)
    while l < r : 
        mid = (l + r) // 2
        if nums[mid] == k : 
            nums.insert(mid , k)
        elif nums[mid] < k : 
            l = mid + 1 
        else : 
            r = mid 
    nums.insert(l , k)

# nums = [1 , 2 , 4]
# add_right_pos(nums , 3)
# add_right_pos(nums , 5)
# add_right_pos(nums , 0)
# add_right_pos(nums , 7)
# add_right_pos(nums , 6)


# print(nums)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def _add_right_pos(nums : List[int] , k : int)  : 
            l , r =  0 , len(nums)
            while l < r : 
                mid = (l + r) // 2
                if nums[mid] == k : 
                    nums.insert(mid , k)
                elif nums[mid] < k : 
                    l = mid + 1 
                else : 
                    r = mid 
            nums.insert(l , k)
        i = 0 
        j =  0 

        while i < m and j < n :
            if nums1[i] > nums2[j] : 
                a = nums1[i]
                nums1[i]  = nums2[j] 
                nums2.remove(nums2[j])
                _add_right_pos(nums2 , a)
                if i == 0 :
                    print(f"nums2 is : {nums2}")
                j += 1 
            i += 1 
            # j += 1

        
        i = m 
        for num in nums2:
            nums1[i] = num
            i += 1 


# nums1 = [4,5,6,0,0,0]
# m = 3
# nums2 = [1,2,3]
# n = 3

# Solution().merge(nums1 ,m ,nums2 , n)

# print(nums1)
nums = [0,1,2,2,3,0,4,2]
val = 2

# write = 0 
# n  = len(nums)
# for read in range(n):
#     if nums[read] != k : 
#         nums[write] = nums[read]
#         write += 1
#     # print(nums)
# nums = nums[:write]
write = 0 
n = len(nums)
for read in range(n):
    if nums[read] != val : 
        nums[write] = nums[read]
        write += 1 
nums = nums[:write]

print(nums)
print(write)

