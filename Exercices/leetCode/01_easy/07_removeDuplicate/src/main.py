class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0 

        for i in range(len(nums) -1):

            if nums[i] != nums[i+1]:
                nums[count] = nums[i]
                count += 1
        
        nums[count] = nums[len(nums) -1]
        count+=1

        return count ;
