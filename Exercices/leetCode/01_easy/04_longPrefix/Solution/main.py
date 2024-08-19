#!/usr/bin/env python3

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        pref = strs[0]
        indice = 0 
        size_min = min([len(s) for s in strs])

        if size_min == 0: 
            return ""
        if len(strs) == 1 :
            return strs[0]

        for i in range(size_min): 
            ch = pref[i]
            for chaine in strs[1:] :
                if chaine[indice] != ch : 
                    return "" if indice == 0 else pref[:indice]
                
            if indice + 1 < size_min :
                indice +=1 
            else : 
                return pref[:size_min] 
            