"""
Exo 5 : Two Sum
---------------------------------
Étant donné un tableau d'entiers nums et un entier target,
retourner les indices des deux éléments dont la somme est égale à target.
Chaque entrée a exactement une solution, et on ne peut pas utiliser
le même élément deux fois.

Examples :
---------------
nums = [2, 7, 11, 15], target = 9 => [0, 1]
nums = [3, 2, 4], target = 6 => [1, 2]
nums = [3, 3], target = 6 => [0, 1]

----
times : 0
last_date :
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":

    # Test 1 :
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test 2 :
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test 3 :
    assert two_sum([3, 3], 6) == [0, 1]

    print("All tests passed!")
