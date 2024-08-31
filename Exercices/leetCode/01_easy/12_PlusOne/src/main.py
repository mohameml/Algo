class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        number = sum([digits[i]*10**(n - (i+1)) for i in range(n)])
        number = number + 1
        l = list(map(int, str(number)))

        return l
