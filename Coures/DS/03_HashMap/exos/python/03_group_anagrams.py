"""
Exo 3 : Group Anagrams
---------------------------------
Étant donné une liste de chaînes, grouper les anagrammes ensemble.
Retourner une liste de groupes (l'ordre n'importe pas).

Examples :
---------------
strs = ["eat","tea","tan","ate","nat","bat"]
=> [["eat","tea","ate"], ["tan","nat"], ["bat"]]

strs = [""] => [[""]]
strs = ["a"] => [["a"]]

----
times : 1
last_date : 15/03/2026
"""

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:

    res = {}
    for str_ in strs : 
        key = tuple(sorted(str_)) 
        if  key not in res :
            res[key] = []
        res[key].append(str_)
    return list(res.values())


if __name__ == "__main__":

    # Test 1 :
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result_sorted = sorted([sorted(g) for g in result])
    assert result_sorted == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    # Test 2 :
    assert group_anagrams([""]) == [[""]]

    # Test 3 :
    assert group_anagrams(["a"]) == [["a"]]

    print("All tests passed!")
