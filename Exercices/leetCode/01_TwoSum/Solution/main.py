#!/usr/bin/env python3

# complexite : 0(N**2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i1 , e1  in enumerate(nums) :
            for i2 , e2 in enumerate(nums) :
                if i1!= i2 :     
                    if e1 + e2 == target :
                        return [i1 , i2]
                

        



    