"""
Exo 02 : Doubly Linked List — Implementation from scratch
-----------------------------------------------------------
Implement a Doubly Linked List with sentinel nodes (dummy head/tail).
Operations:
- insert_head(val), insert_tail(val), insert_at(index, val)
- delete_head(), delete_tail(), delete_node(node), delete_at(index)
- search(val), get(index)
- to_list(), to_list_reverse(), from_list(vals)

The sentinel nodes pattern eliminates edge cases for empty list
and single-element operations.

----
times : 1
last_date : 2026-03-15
"""


class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()  # sentinel
        self.tail = DListNode()  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, val, pred, succ):
        new_node = DListNode(val, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def _remove_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return node.val

    def insert_head(self, val):
        return self._insert_between(val, self.head, self.head.next)

    def insert_tail(self, val):
        return self._insert_between(val, self.tail.prev, self.tail)

    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return self._insert_between(val, curr.prev, curr)

    def delete_head(self):
        if self.is_empty():
            raise IndexError("Delete from empty list")
        return self._remove_node(self.head.next)

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("Delete from empty list")
        return self._remove_node(self.tail.prev)

    def delete_node(self, node):
        return self._remove_node(node)

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return self._remove_node(curr)

    def search(self, val):
        curr = self.head.next
        index = 0
        while curr != self.tail:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr.val

    def to_list(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.val)
            curr = curr.next
        return result

    def to_list_reverse(self):
        result = []
        curr = self.tail.prev
        while curr != self.head:
            result.append(curr.val)
            curr = curr.prev
        return result

    def __repr__(self):
        vals = self.to_list()
        return "None <-> " + " <-> ".join(str(v) for v in vals) + " <-> None"

    @classmethod
    def from_list(cls, vals):
        dll = cls()
        for val in vals:
            dll.insert_tail(val)
        return dll


if __name__ == "__main__":

    # Test 1 : Build from list
    dll = DoublyLinkedList.from_list([1, 2, 3, 4, 5])
    assert dll.to_list() == [1, 2, 3, 4, 5]
    assert dll.to_list_reverse() == [5, 4, 3, 2, 1]
    assert len(dll) == 5
    print(f"Test 1 passed: {dll}")

    # Test 2 : Insert operations
    dll.insert_head(0)
    dll.insert_tail(6)
    assert dll.to_list() == [0, 1, 2, 3, 4, 5, 6]
    print(f"Test 2 passed: {dll}")

    # Test 3 : Delete head and tail in O(1)
    assert dll.delete_head() == 0
    assert dll.delete_tail() == 6
    assert dll.to_list() == [1, 2, 3, 4, 5]
    print(f"Test 3 passed: {dll}")

    # Test 4 : Delete node by reference in O(1)
    dll2 = DoublyLinkedList()
    node_a = dll2.insert_head(1)
    node_b = dll2.insert_tail(2)
    node_c = dll2.insert_tail(3)
    dll2.delete_node(node_b)
    assert dll2.to_list() == [1, 3]
    print(f"Test 4 passed: {dll2}")

    # Test 5 : Search and get with optimization
    dll3 = DoublyLinkedList.from_list([10, 20, 30, 40, 50])
    assert dll3.search(30) == 2
    assert dll3.search(99) == -1
    assert dll3.get(0) == 10
    assert dll3.get(4) == 50
    print("Test 5 passed: search and get")

    # Test 6 : Edge cases
    empty = DoublyLinkedList()
    assert empty.is_empty()
    try:
        empty.delete_head()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    print("Test 6 passed: edge cases")
