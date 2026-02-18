


def heapify_up(heap , i) : 
    """insert i in Min-Heap : log(n)"""
    while i > 0 : 
        parent = (i - 1) // 2 
        if heap[i] < heap[parent] : 
            heap[i] , heap[parent] = heap[parent] ,heap[i]
            i = parent 
        else : 
            break


def heappush(heap , val) : 
    heap.append(val)
    heapify_up(heap, len(heap) - 1)





def heapify_down(heap , i) : 
    """remove ele from heap : log(n)"""
    n = len(heap)

    while True : 
        left = 2*i + 1 
        right = 2*i + 2 
        smallest = i 
        
        if left < n and heap[left] < heap[smallest] : 
            smallest = left 
        if right < n and heap[right] < heap[smallest] : 
            smallest = right 
        
        if smallest != i : 
            heap[i] , heap[smallest] = heap[smallest] , heap[i]
            i = smallest
        else : 
            break 

def heappop(heap) : 
    if not heap : 
        return None 
    
    # swap root ave with last : 
    heap[0] , heap[-1] = heap[-1] , heap[0]
    min_val = heap.pop()
    heapify_down(heap, 0)

    return min_val


def build_heap(heap) : 
    """build heap from a list : O(n) (not O(nlog(n)) ) """
    n = len(heap)
    for i in reversed(range(n // 2)) : 
        heapify_down(heap , i)


if __name__ == "__main__" : 


    # Test heappush with heapify_up 
    heap = [1 , 3, 5]
    heappush(heap, 2) # heap = [1 ,2 , 5 , 3]
    print(f"heap after insert 2 : {heap}")
    heappush(heap , 0) # heap = [0 , 1, 5 , 3 , 2]
    print(f"heap after insert 0 : {heap}")
    heappush(heap ,20) # heap = [0 , 1, 5 , 3 , 2]
    print(f"heap after insert 20 : {heap}")


    # Test heappop and heapify_down 
    heap = [1, 3, 5, 7, 9, 6]

    min_val = heappop(heap)
    print(f"min_val is : {min_val}")
    print(f"heap after heapify_down : {heap}") # [3, 6, 5, 7, 9]

    # build heap 
    heap = [9, 4, 7, 1, 3, 6, 2]
    build_heap(heap)
    print(f"heap after build_heap : {heap}") # [1, 3, 2, 4, 9, 6, 7]

