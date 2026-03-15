"""
Exo 4 : Valid Anagram
---------------------------------
Déterminer si deux chaînes s et t sont des anagrammes l'une de l'autre.
Deux chaînes sont des anagrammes si elles contiennent les mêmes caractères
avec les mêmes fréquences.

Examples :
---------------
s = "anagram", t = "nagaram" => True
s = "rat", t = "car" => False
s = "", t = "" => True

----
times : 0
last_date :
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for c in t:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] == 0:
            del freq[c]

    return len(freq) == 0


if __name__ == "__main__":

    # Test 1 :
    assert is_anagram("anagram", "nagaram") == True

    # Test 2 :
    assert is_anagram("rat", "car") == False

    # Test 3 :
    assert is_anagram("", "") == True

    # Test 4 :
    assert is_anagram("ab", "a") == False

    print("All tests passed!")
