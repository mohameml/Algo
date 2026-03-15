"""
Exo 10 : Copy List with Random Pointer — LC 138
--------------------------------------------------
A linked list where each node has an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.

Examples :
---------------
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

----
times : 1
last_date : 2026-03-15
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    if not head:
        return None

    # Map original -> copy
    node_map = {}
    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    # Set next and random
    curr = head
    while curr:
        node_map[curr].next = node_map.get(curr.next)
        node_map[curr].random = node_map.get(curr.random)
        curr = curr.next

    return node_map[head]


if __name__ == "__main__":

    # Test 1 : basic case
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
    n1.random = None
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    copy = copy_random_list(n1)
    # Verify values
    vals = []
    curr = copy
    while curr:
        vals.append(curr.val)
        curr = curr.next
    assert vals == [7, 13, 11, 10, 1]
    # Verify it's a deep copy (different objects)
    assert copy is not n1
    assert copy.next is not n2
    # Verify random pointers
    assert copy.random is None
    assert copy.next.random is copy  # 13 -> 7
    assert copy.next.next.random is copy.next.next.next.next  # 11 -> 1
    print("Test 1 passed")

    # Test 2 : empty list
    assert copy_random_list(None) is None
    print("Test 2 passed")

    # Test 3 : single node pointing to itself
    n = Node(1)
    n.random = n
    c = copy_random_list(n)
    assert c.val == 1
    assert c.random is c
    assert c is not n
    print("Test 3 passed")
