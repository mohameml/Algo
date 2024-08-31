#!/usr/bin/env python3


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j = j + 1
                i = i + 1
                if j >= len(needle):
                    return i - j
            else:
                if j > 0:
                    i = i - (j-1)
                    j = 0
                else:
                    i = i + 1
        return -1
