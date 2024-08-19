class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        i = 0 
        n = len(nums)
        while i < n :
            if nums[i] == val :
                nums.remove(nums[i])
            else :
                i+=1
            n = len(nums)

        if len(nums) != 0 and nums[-1] == val :
            nums.remove(nums[-1])

        return len(nums)