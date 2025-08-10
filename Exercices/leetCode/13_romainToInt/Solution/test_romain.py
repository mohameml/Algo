#!/usr/bin/env python3

from main import Solution
solution : Solution = Solution()

def test_1() :
    s = "III"
    res = solution.romanToInt(s)
    assert res == 3 

def test_2() :
    s = "IX"
    res = solution.romanToInt(s)
    assert res == 9 

def test_3() :
    s = "XI"
    res = solution.romanToInt(s)
    assert res == 11 

def test_4() :
    s = "VI"
    res = solution.romanToInt(s)
    assert res == 6 

def test_5() :
    s = "LVIII"
    res = solution.romanToInt(s)
    assert res == 58

def test_6() :
    s = "MCMXCIV"
    res = solution.romanToInt(s)
    assert res == 1994

def test_7() :
    s = "CMXCIX"
    res = solution.romanToInt(s)
    assert res == 999

def test_8() :
    s = "MMMCMXCIX"
    res = solution.romanToInt(s)
    assert res == 3999


