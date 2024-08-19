
from main import Solution

solution : Solution  = Solution()


def test_1():
    s = "(())"
    res = solution.isValid(s)
    assert res == True


def test_2():
    s = "{()}[](({}))"
    res = solution.isValid(s)
    assert res == True


def test_3():
    s = "(}"
    res = solution.isValid(s)
    assert res == False

def test_4():
    s = "([)]"
    res = solution.isValid(s)
    assert res == False

def test_5():
    s = "("
    res = solution.isValid(s)
    assert res == False

def test_6():
    s = "(("
    res = solution.isValid(s)
    assert res == False

def test_7():
    s = ")}"
    res = solution.isValid(s)
    assert res == False

def test_8():
    s = "(){}}{"
    res = solution.isValid(s)
    assert res == False



