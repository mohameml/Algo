from typing import List 


class MinHeap : 

    def __init__(self , data : List[int]) -> None:
        self._data = data 
        self._build_from_list()

    def __bool__(self):
        return len(self._data) > 0 

    def _build_from_list(self):  
        n = len(self._data)

        for i in range((n-2)//2 , - 1 , -1) : 
            self._heapify_down(i)

    def _heapify_down(self , i : int)  -> None : 
        """change nums in place """

        while True : 
            smallest = i 
            left = 2*i + 1 
            right = 2*i + 2 

            
            if left < len(self._data) and self._data[left] < self._data[i] : 
                smallest = left 

            if right < len(self._data) and self._data[right] < self._data[smallest] : 
                smallest = right 
            
            if smallest != i : 
                self._data[i] , self._data[smallest] = self._data[smallest] , self._data[i]
                i = smallest
            else : 
                break 

    def extract_min(self) -> int : 
        if len(self._data) == 0 : 
            raise ValueError(f"heap is empty")
        
        if len(self._data) == 1 : 
            return self._data.pop()
        self._data[0] , self._data[-1] = self._data[-1] , self._data[0]
        min_val = self._data.pop()
        self._heapify_down(0)

        return min_val


def heap_sort(nums : List[int]) -> List[int] : 
    """implement heap sort"""
    heap = MinHeap(nums)
    res = []
    while heap : 
        print(f"{res =}")
        res.append(heap.extract_min())
    return res 


if __name__ == "__main__" : 
    res = heap_sort([1 , 10 , 0 , 3 , 2 , 15 , -1 , 20])
    print(f"{res =}")