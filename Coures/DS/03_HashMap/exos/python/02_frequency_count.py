"""
Exo 2 : Frequency Count
---------------------------------
Compter la fréquence de chaque élément dans un tableau.
Retourner un dictionnaire {element: count}.

Examples :
---------------
nums = [1, 2, 2, 3, 3, 3] => {1: 1, 2: 2, 3: 3}
nums = [5] => {5: 1}
nums = [] => {}

----
times : 1
last_date : 15/03/2026
"""

from typing import List, Dict


def frequency_count(nums: List[int]) -> Dict[int, int]:
    freq = {}
    for key in nums : 
        if key not in freq : 
            freq[key] = 0
        freq[key] += 1 
    return freq 


if __name__ == "__main__":

    # Test 1 :
    assert frequency_count([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

    # Test 2 :
    assert frequency_count([5]) == {5: 1}

    # Test 3 :
    assert frequency_count([]) == {}

    # Test 4 :
    assert frequency_count([1, 1, 1, 1]) == {1: 4}

    print("All tests passed!")
