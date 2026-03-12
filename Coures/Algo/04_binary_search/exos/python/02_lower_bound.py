"""
Ex02 :
--------------------------------
Trouver le **premier index `i` tel que** : nums[i] >= target

C'est la **première position où on peut insérer `target` sans casser l'ordre**.


------------
times : 1 
"""


def lower_bound(nums, target):
    ...
    
    
if __name__ == "__main__" : 
    nums = [1 , 3 , 4, 6 , 7]        
    print(f"res : {lower_bound(nums , target=0)}")
    print(f"res : {lower_bound(nums , target=1)}")
    print(f"res : {lower_bound(nums , target=4)}")
    print(f"res : {lower_bound(nums , target=5)}")
    print(f"res : {lower_bound(nums , target=10)}")
    
    