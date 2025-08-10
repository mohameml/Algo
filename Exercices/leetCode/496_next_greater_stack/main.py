"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above
"""


def next_greater(nums : list[int]) -> list[int] : 

    stack = []
    res = {}

    for num in nums : 
        while stack and  num > stack[-1]:
            top = stack.pop()
            res[top] = num 
        stack.append(num)
    
    for e in stack : 
        res[e] = - 1

    return res 


# nums = [1 , 3 , 4 , 2]
nums = [16 , 4 , 2 , 1 , 18 , 19]


print(
    next_greater(nums)
)