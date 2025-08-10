"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
"""


class TimeMap:

    def __init__(self):

        self.map : dict[str , dict[str , list]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.map : 
            self.map[key] = {"timestamps" : [] , "values" : []}

        self.map[key]["values"].append(value)
        self.map[key]["timestamps"].append(timestamp)



    def search_index_position(self , nums : list[int] , el : int) -> int : 
        left = 0 
        right = len(nums) - 1 
        res = -1   

        while left <= right : 
            
            mid = left + (right - left) // 2

            if nums[mid] <= el : 
                res = mid 
                left = mid + 1 
            else : 
                right  = mid - 1 
        
        return res 

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map :
            return ""

        timestamps = self.map[key]["timestamps"]
        index = self.search_index_position(timestamps , timestamp)

        if index == -1 : 
            return ""
        
        return self.map[key]["values"][index]




"""
- ["TimeMap","set","set","get","get","get","get","get"]
- [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
- [null,null,null,"","","","low","low"]
- Expected : [null,null,null,"","high","high","low","low"]
"""

timeMap = TimeMap()
timeMap.set("love" , "high" , 10)
timeMap.set("love" , "low" , 20)
print(timeMap.get("love" , 5)) # ""
print(timeMap.get("love" , 10)) # "high"
print(timeMap.get("love" , 15)) # "high"
print(timeMap.get("love" , 20)) # low
print(timeMap.get("love" , 25)) # low 



def search_index_position(nums : list[int] , el : int) -> int : 

    left = 0 
    right = len(nums) - 1 
    res = -1   

    while left <= right : 
        print(f"left = {left} , right = {right}")

        mid = left + (right - left) // 2

        if nums[mid] <= el : 
            res = mid 
            left = mid + 1 
        else : 
            right  = mid - 1 
    
    return res 


l = [1 , 2  , 3 , 4 , 7 , 10]
el = 5
# -> index = 1  ->  l[:index+1] + [el] + l[index+1:]

print(
    search_index_position(l , el)
) 