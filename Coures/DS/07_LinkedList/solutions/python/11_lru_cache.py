"""
Exo 11 : LRU Cache — LC 146
------------------------------
Design a data structure that follows the constraints of a
Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(capacity): Initialize with positive size capacity
- get(key): Return the value if key exists, otherwise return -1
- put(key, value): Update or insert. If capacity exceeded, evict LRU key.

Both get and put must run in O(1) average time complexity.

Examples :
---------------
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

----
times : 1
last_date : 2026-03-15
"""


class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode()  # sentinel
        self.tail = DLLNode()  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


if __name__ == "__main__":

    # Test 1 : basic operations
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)        # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)        # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("Test 1 passed")

    # Test 2 : update existing key
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(1, 10)      # update key 1
    assert cache2.get(1) == 10
    cache2.put(3, 3)       # evicts key 2 (not 1, because 1 was recently used)
    assert cache2.get(2) == -1
    assert cache2.get(1) == 10
    print("Test 2 passed")

    # Test 3 : capacity 1
    cache3 = LRUCache(1)
    cache3.put(1, 1)
    assert cache3.get(1) == 1
    cache3.put(2, 2)       # evicts key 1
    assert cache3.get(1) == -1
    assert cache3.get(2) == 2
    print("Test 3 passed")
