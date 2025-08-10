#!/usr/bin/env python3

"""
test for Two Sum 
"""


from main import Solution

solution = Solution()





def test_1(): 
    "res = [0,1]"
    nums = [2,7,11,15]
    target = 9
    res = solution.twoSum(nums , target)

    assert res == [0,1]

def test_2(): 
    "res = [1,2]"
    nums = [3,2,4]
    target = 6
    res = solution.twoSum(nums , target)

    assert res == [1,2]


def test_3(): 
    "res = [0,1]"
    nums = [3,3]
    target = 6  
    res = solution.twoSum(nums , target)

    assert res == [0,1]



