#!/usr/bin/env python3 


class Solution(object):

    def __init__(self) :
        self.vals = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i  in range(len(s) - 1 ) :
            if self.vals[s[i]] >= self.vals[s[i+1]] :
                res+=self.vals[s[i]]
            else :
                res-=self.vals[s[i]]
                
        res += self.vals[s[len(s) -1]]

        return res 
            
