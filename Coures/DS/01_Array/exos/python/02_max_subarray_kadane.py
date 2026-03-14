"""
Exo 2 : Maximum Subarray (Kadane's Algorithm)
---------------------------------
Trouver la plus grande somme possible d'éléments consécutifs dans un tableau
d'entiers (positifs ou négatifs).

Examples :
---------------
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] => 6 (sous-tableau [4, -1, 2, 1])
nums = [1] => 1
nums = [-1, -2, -3] => -1

----
times : 1
last_date : 14/03/2026
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]
    for num in nums[1: ] : 
        curr_sum = max(num , curr_sum + num)
        max_sum = max(max_sum , curr_sum)
    return max_sum
    

if __name__ == "__main__":

    # Test 1 :
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test 2 :
    assert max_subarray([1]) == 1

    # Test 3 :
    assert max_subarray([-1, -2, -3]) == -1

    # Test 4 :
    assert max_subarray([5, 4, -1, 7, 8]) == 23

    print("All tests passed!")
