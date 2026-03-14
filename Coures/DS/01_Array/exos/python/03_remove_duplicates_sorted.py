"""
Exo 3 : Remove Duplicates from Sorted Array
---------------------------------
Étant donné un tableau trié nums, supprimer les doublons in-place
et retourner le nouveau nombre d'éléments uniques.
Les k premiers éléments de nums doivent contenir les éléments uniques.

Examples :
---------------
nums = [1, 1, 2] => 2, nums[:2] = [1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] => 5, nums[:5] = [0, 1, 2, 3, 4]

----
times : 1
last_date : 14/03/2026
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 1 : 
        return 1 
    write = 0 
    for read in range(len(nums)) :
        if nums[read] != nums[read - 1] : 
            nums[write] = nums[read]
            write += 1 
    return write


if __name__ == "__main__":

    # Test 1 :
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    assert k1 == 2 and nums1[:k1] == [1, 2]

    # Test 2 :
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = remove_duplicates(nums2)
    assert k2 == 5 and nums2[:k2] == [0, 1, 2, 3, 4]

    # Test 3 :
    nums3 = [1]
    k3 = remove_duplicates(nums3)
    assert k3 == 1 and nums3[:k3] == [1]

    print("All tests passed!")
