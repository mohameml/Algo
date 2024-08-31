class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(" ")
        l = list(filter(lambda e: e != "", l))

        return len(l[-1])
