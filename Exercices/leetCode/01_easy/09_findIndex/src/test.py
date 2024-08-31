#!/usr/bin/env python3

from main import Solution

solution: Solution = Solution()


def test_1():
    haystack = "sadbutsad"
    needle = "sad"
    index = solution.strStr(haystack, needle)
    print("index = ", index)


test_1()


def test_2():
    haystack = "leetcode"
    needle = "leeto"
    index = solution.strStr(haystack, needle)
    print("index = ", index)


test_2()
