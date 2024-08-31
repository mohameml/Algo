#!/usr/bin/env python3
from collections import deque


class Solution(object):

    def __init__(self):
        self.vals = {
            "(": 1,
            ")": -1,
            "{": 2,
            "}": -2,
            "[": 3,
            "]": -3,
        }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 1:
            return False

        stack = deque()

        for ch in s:
            if self.vals[ch] > 0:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if self.vals[ch] + self.vals[top] != 0:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
