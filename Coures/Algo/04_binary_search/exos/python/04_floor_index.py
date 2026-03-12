"""
Ex04 :
--------------------------------
Trouver :

max { i t.q nums[i] <= target }

Donc **le plus grand élément ≤ target**.



------------
times : 1 
"""


def floor_index(nums, target):
    ...
    
    
if __name__ == "__main__" : 
    nums = [1 , 3 , 4, 6 , 7]        
    print(f"res : {floor_index(nums , target=0)}")
    print(f"res : {floor_index(nums , target=1)}")
    print(f"res : {floor_index(nums , target=4)}")
    print(f"res : {floor_index(nums , target=5)}")
    print(f"res : {floor_index(nums , target=7)}")
    print(f"res : {floor_index(nums , target=10)}")
    
    