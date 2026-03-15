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

from collections import Counter 

def is_anagram(s: str, t: str) -> bool:
    freq_s  = Counter(s)
    freq_t = Counter(t)
    
    for char_s in freq_s :
        if  char_s not in freq_t or freq_s[char_s] != freq_t[char_s] : 
            return False
    return True 


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
