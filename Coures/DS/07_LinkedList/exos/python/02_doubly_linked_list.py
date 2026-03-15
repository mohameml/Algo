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
times : 0
last_date :
"""


class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        ...

    def __len__(self):
        ...

    def is_empty(self):
        ...

    def insert_head(self, val):
        ...

    def insert_tail(self, val):
        ...

    def insert_at(self, index, val):
        ...

    def delete_head(self):
        ...

    def delete_tail(self):
        ...

    def delete_node(self, node):
        ...

    def delete_at(self, index):
        ...

    def search(self, val):
        ...

    def get(self, index):
        ...

    def to_list(self):
        ...

    def to_list_reverse(self):
        ...

    def __repr__(self):
        vals = self.to_list()
        return "None <-> " + " <-> ".join(str(v) for v in vals) + " <-> None"

    @classmethod
    def from_list(cls, vals):
        ...


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
