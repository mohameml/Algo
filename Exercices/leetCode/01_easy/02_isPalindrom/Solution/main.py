#!/usr/bin/env python3

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False 
        else : 
            x = str(x)
            return x[::-1] ==  x