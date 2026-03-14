"""implement dynamic array from scratch"""

class DynamicArray:
    """Dynamic array implementation from scratch."""

    def __init__(self):
        self._size = 0 
        self._capacity = 1 
        self._data = [None]*self._capacity

    def __len__(self):
        return self._size
    
    def __getitem__(self, i):
        if i < 0 or i >= self._size : 
            raise IndexError("Index out of range")
        return self._data[i]
    
    def __setitem__(self, i, val):
        if i < 0 or i >= self._size : 
            raise IndexError("Index out of range")
        self._data[i] = val 
        
    def append(self, val):
        if self._size == self._capacity : 
            self._resize(2*self._capacity)
        self._data[self._size] = val 
        self._size += 1 
        
    def pop(self):
        if self._size == 0 : 
            raise IndexError("Pop from empty array")
        val  = self._data[self._size - 1]
        self._data[self._size - 1] = None 
        self._size -= 1 

        return val 
        
    def insert(self, i, val):
        if i < 0 or i > self._size : 
            raise IndexError("Index out of range")
        
        if self._size == self._capacity : 
            self._resize(2*self._capacity)
        
        for j in range(self._size , i , -1) : 
            self._data[j] = self._data[j - 1]
        
        self._data[i] = val 
        self._size += 1 
        
    def remove(self, val):
        for i in range(self._size) : 
            if self._data[i] == val : 
                for j in range(i , self._size - 1) : 
                    self._data[j] = self._data[j + 1]
                self._data[self._size - 1] = None 
                self._size -= 1 
                return 
        raise ValueError("Value not found")
        
    def _resize(self, new_capacity):
        new_data = [None]*new_capacity 
        for  i in range(self._size) : 
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"


if __name__ == "__main__" :

    # Test 1 : append + len
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    assert len(arr) == 3
    assert str(arr) == "[10, 20, 30]"

    # Test 2 : access + update
    assert arr[0] == 10
    assert arr[2] == 30
    arr[1] = 99
    assert arr[1] == 99

    # Test 3 : pop
    val = arr.pop()
    assert val == 30
    assert len(arr) == 2

    # Test 4 : insert
    arr.insert(0, 5)
    assert arr[0] == 5
    assert len(arr) == 3
    arr.insert(2, 42)
    assert arr[2] == 42
    assert len(arr) == 4

    # Test 5 : remove
    arr.remove(42)
    assert len(arr) == 3

    # Test 6 : resize (append many elements)
    arr2 = DynamicArray()
    for i in range(100):
        arr2.append(i)
    assert len(arr2) == 100
    assert arr2[0] == 0
    assert arr2[99] == 99

    # Test 7 : errors
    try:
        arr[100]
        assert False
    except IndexError:
        pass

    try:
        DynamicArray().pop()
        assert False
    except IndexError:
        pass

    try:
        arr.remove(999)
        assert False
    except ValueError:
        pass

    print("All tests passed!")
    