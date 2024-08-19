from main import Solution

solution : Solution = Solution()


def test_1():
    nums = [1,1,2,3,4,4,5] 
    print("nums avant =" , nums)
    expectedNums = [1,2,3,4,5] 

    k = solution.removeDuplicates(nums)

    print("nums apres =" , nums)

    assert k == len(expectedNums)
    
    for i in range(0 , k) :
        assert nums[i] == expectedNums[i]
    
test_1()

def test_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print("nums avant =" , nums)
    expectedNums = [0,1,2,3,4] 

    k = solution.removeDuplicates(nums)

    print("nums apres =" , nums)

    assert k == len(expectedNums)
    
    for i in range(0 , k) :
        assert nums[i] == expectedNums[i]
    
test_2()