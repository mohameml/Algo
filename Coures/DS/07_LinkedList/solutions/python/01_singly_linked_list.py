"""
Exo 01 : Singly Linked List — Implementation from scratch
-----------------------------------------------------------
Implement a Singly Linked List with the following operations:
- insert_head(val): Insert at the beginning
- insert_tail(val): Insert at the end
- insert_at(index, val): Insert at a specific index
- delete_head(): Remove and return head value
- delete_tail(): Remove and return tail value
- delete_at(index): Remove and return value at index
- search(val): Return index of first occurrence, or -1
- get(index): Return value at index
- to_list(): Return list of all values
- from_list(vals): Class method to build from a Python list

----
times : 1
last_date : 2026-03-15
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_head(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def insert_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_head(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node = ListNode(val, curr.next)
        curr.next = new_node
        self.size += 1

    def delete_head(self):
        if not self.head:
            raise IndexError("Delete from empty list")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def delete_tail(self):
        if not self.head:
            raise IndexError("Delete from empty list")
        if not self.head.next:
            val = self.head.val
            self.head = None
            self.size -= 1
            return val
        curr = self.head
        while curr.next.next:
            curr = curr.next
        val = curr.next.val
        curr.next = None
        self.size -= 1
        return val

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.delete_head()
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        val = curr.next.val
        curr.next = curr.next.next
        self.size -= 1
        return val

    def search(self, val):
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __repr__(self):
        vals = self.to_list()
        return " -> ".join(str(v) for v in vals) + " -> None"

    @classmethod
    def from_list(cls, vals):
        sll = cls()
        for val in reversed(vals):
            sll.insert_head(val)
        return sll


if __name__ == "__main__":

    # Test 1 : Build from list and display
    sll = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    assert sll.to_list() == [1, 2, 3, 4, 5]
    assert len(sll) == 5
    print(f"Test 1 passed: {sll}")

    # Test 2 : Insert operations
    sll.insert_head(0)
    sll.insert_tail(6)
    sll.insert_at(3, 99)
    assert sll.to_list() == [0, 1, 2, 99, 3, 4, 5, 6]
    print(f"Test 2 passed: {sll}")

    # Test 3 : Delete operations
    assert sll.delete_head() == 0
    assert sll.delete_tail() == 6
    assert sll.delete_at(1) == 2
    assert sll.to_list() == [1, 99, 3, 4, 5]
    print(f"Test 3 passed: {sll}")

    # Test 4 : Search and get
    assert sll.search(99) == 1
    assert sll.search(100) == -1
    assert sll.get(0) == 1
    assert sll.get(4) == 5
    print("Test 4 passed: search and get")

    # Test 5 : Edge cases
    empty = SinglyLinkedList()
    assert empty.is_empty()
    assert len(empty) == 0
    try:
        empty.delete_head()
        assert False, "Should raise IndexError"
    except IndexError:
        pass
    print("Test 5 passed: edge cases")
