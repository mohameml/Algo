"""
Ex03 :
--------------------------------
Trouver le **premier index `i` tel que** : nums[i] > target



------------
times : 1 
"""


def upper_bound(nums, target):
    ...
    
    
if __name__ == "__main__" : 
    nums = [1 , 3 , 4, 6 , 7]        
    print(f"res : {upper_bound(nums , target=0)}")
    print(f"res : {upper_bound(nums , target=1)}")
    print(f"res : {upper_bound(nums , target=4)}")
    print(f"res : {upper_bound(nums , target=5)}")
    print(f"res : {upper_bound(nums , target=7)}")
    print(f"res : {upper_bound(nums , target=10)}")
    
    