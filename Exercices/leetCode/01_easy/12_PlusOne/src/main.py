class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # n = len(digits)
        # number = sum([digits[i]*10**(n - (i+1)) for i in range(n)])
        # number = number + 1
        # l = list(map(int, str(number)))

        # return l


        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            
            else:
                digits[i] += 1
                return digits
        
        return [1] + digits
    