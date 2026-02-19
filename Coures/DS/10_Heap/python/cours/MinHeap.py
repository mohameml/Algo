from typing import List , Optional 

class MinHeap : 
    """implement the DS min-heap"""

    def __init__(self) -> None:
        self._data : List[int] = []
    

    # Helpers internes :

    def _parent(self , i : int) -> int : 
        return (i - 1) // 2 

    def _left(self , i: int) -> int : 
        return 2*i + 1 

    def _right(self , i : int) -> int : 
        return 2*i + 2 

    def _has_parent(self , i : int) -> bool : 
        return i > 0 
    
    def _has_left(self , i : int) -> bool  : 
        return self._left(i) < len(self._data)
    
    def _has_right(self , i  : int) -> bool : 
        return self._right(i) < len(self._data)

    def _swap(self , i  : int , j : int) -> None : 
        self._data[i] , self._data[j]  = self._data[j] , self._data[i]

    
    # Read : O(1)
    
    def peek(self) -> int : 
        """return the min"""
        if self.is_empty() : 
            raise IndexError("Heap is empty")
        return self._data[0]
    
    def size(self) -> int : 
        return len(self._data)
    
    def is_empty(self) -> bool : 
        return len(self._data) == 0 
    
    # Insert : O(log(n))
    def insert(self , val : int) -> None : 
        """add new val to the heap : O(log(n))"""
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)
    
    def _heapify_up(self , i : int) -> None : 
        """        
            Remonte l'élément à l'index i tant qu'il est
            plus petit que son parent.
        """

        while self._has_parent(i) : 
            p = self._parent(i)
            if self._data[i] < self._data[p] : 
                self._swap(i ,p)
                i = p
            else :
                break 

    # EXTRACT MIN — O(log n) : 
    def extract_min(self) -> int:
        """pop the min"""
        if self.is_empty() : 
            raise IndexError("Heap is empty")
        
        if self.size() == 1 :
            return self._data.pop()
        
        self._swap(0 , -1)
        min_val = self._data.pop()
        self._heapify_down(0)

        return min_val
        

    def _heapify_down(self , i : int) -> None : 
        """ 
            Descend l'élément à l'index i en swappant avec
            le plus PETIT de ses enfants, tant qu'il y a violation.
        """

        while self._has_left(i) : 
            smallles_child = self._left(i)

            if self._has_right(i) and self._data[self._right(i)] < self._data[smallles_child] : 
                smallles_child = self._right(i)

            if self._data[i] > self._data[smallles_child] : 
                self._swap(i , smallles_child)
                i = smallles_child
            else : 
                break 

    # BUILD HEAP — O(n)  [Floyd's Algorithm] 
    @classmethod
    def from_list(cls , values : List[int]) -> 'MinHeap' :
        """construct a heap from list : O(n)""" 
        heap = cls()
        heap._data= list(values)
        n = len(heap._data)
    
        for i in range((n - 2) // 2 , -1 , -1) : 
            heap._heapify_down(i)

        return heap 

    # DELETE élément quelconque — O(n + log n) = O(n)
    def delete(self , val : int) -> bool : 

        # get the idx of the value : 
        try : 
            idx = self._data.index(val)
        except ValueError : 
            return False 
        last = len(self._data) - 1
        if idx == last : 
            self._data.pop()
            return True
        
        self._swap(idx , last)
        self._data.pop()
        self._heapify_up(idx)
        self._heapify_down(idx)

        return True 

    # HEAP SORT — O(n log n) 
    def to_sorted_list(self) -> List[int] : 
        """sort list : O(nlog(n))"""
        backup = list(self._data)
        res = []

        while not self.is_empty() : 
            res.append(self.extract_min())
        
        self._data = backup 

        return res 
    
    # AFFICHAGE
    def __repr__(self) -> str:
        return f"MinHeap({self._data})"

    def display(self) -> None:
        """Affiche le heap niveau par niveau."""
        if self.is_empty():
            print("Heap vide")
            return

        level_start: int = 0
        level_size:  int = 1

        while level_start < len(self._data):
            level_end = min(level_start + level_size, len(self._data))
            print(self._data[level_start:level_end])
            level_start = level_end
            level_size  *= 2

if __name__ == "__main__" : 
    # ── Construction ──────────────────────────────
    h = MinHeap()

    h.insert(5)   # _data = [5]
    h.insert(3)   # _data = [5, 3]  → heapify_up: 3 < 5, swap → [3, 5]
    h.insert(8)   # _data = [3, 5, 8] → 8 > parent(3), ok
    h.insert(1)   # _data = [3, 5, 8, 1]
                # heapify_up(3): 1 < parent=5, swap → [3, 1, 8, 5]
                # heapify_up(1): 1 < parent=3, swap → [1, 3, 8, 5]
    h.insert(4)   # _data = [1, 3, 8, 5, 4]
                # heapify_up(4): 4 > parent=3, ok

    print(h)      # MinHeap([1, 3, 8, 5, 4])
    h.display()
    # [1]
    # [3, 8]
    # [5, 4]

    # ── Peek ──────────────────────────────────────
    print(h.peek())   # 1  — O(1)

    # ── Extract min ───────────────────────────────
    print(h.extract_min())   # 1
    # Étape 1 : last=4, data[0]=4 → [4, 3, 8, 5]
    # heapify_down(0): smallest_child = min(3,8) = 3 (index 1)
    # 4 > 3, swap → [3, 4, 8, 5]
    # heapify_down(1): smallest_child = min(5) = 5 (index 3)
    # 4 < 5, stop
    print(h)   # MinHeap([3, 4, 8, 5])

    # ── Build Heap O(n) ───────────────────────────
    h2 = MinHeap.from_list([9, 4, 7, 1, 8, 3, 2])
    # Dernier nœud interne = (7-2)//2 = 2
    # i=2 : heapify_down([9,4,7,1,8,3,2], 2) → 7 vs min(3,2)=2 → swap → [9,4,2,1,8,3,7]
    # i=1 : heapify_down([9,4,2,1,8,3,7], 1) → 4 vs min(1,8)=1 → swap → [9,1,2,4,8,3,7]
    #        heapify_down(index 3) → 4, pas d'enfants, stop
    # i=0 : heapify_down([9,1,2,4,8,3,7], 0) → 9 vs min(1,2)=1 → swap → [1,9,2,4,8,3,7]
    #        heapify_down(index 1) → 9 vs min(4,8)=4 → swap → [1,4,2,9,8,3,7]
    #        heapify_down(index 3) → 9, pas d'enfants, stop
    print(h2)  # MinHeap([1, 4, 2, 9, 8, 3, 7])

    # ── Heap Sort ─────────────────────────────────
    print(h2.to_sorted_list())   # [1, 2, 3, 4, 7, 8, 9]
