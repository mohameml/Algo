#!/usr/bin/env python3

from main import Solution 

solution : Solution = Solution()

def test_1():
    strs = ["flower","flow","flight"]
    res = solution.longestCommonPrefix(strs)
    assert res == "fl"



def test_2():
    strs = ["dog","racecar","car"]
    res = solution.longestCommonPrefix(strs)
    assert res == ""

def test_3():
    strs = [""]
    res = solution.longestCommonPrefix(strs)
    assert res == ""


def test_4():
    strs = ["a"]
    res = solution.longestCommonPrefix(strs)
    assert res == "a"


def test_5():
    strs = ["ab" , "a"]
    res = solution.longestCommonPrefix(strs)
    assert res == "a"