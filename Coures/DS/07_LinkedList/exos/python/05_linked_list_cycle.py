"""
Exo 05 : Linked List Cycle — LC 141
-------------------------------------
Given head, determine if the linked list has a cycle in it.
A cycle exists if some node can be reached again by continuously
following the next pointer.

Return True if there is a cycle, False otherwise.

Examples :
---------------
Input: head = [3, 2, 0, -4], pos = 1 (tail connects to index 1)
Output: True

Input: head = [1, 2], pos = 0
Output: True

Input: head = [1], pos = -1 (no cycle)
Output: False

----
times : 1
last_date : 15/03/2026
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow , fast = head , head 
    
    while fast and fast.next : 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast : 
            return True 
    
    return False 


if __name__ == "__main__":

    # Test 1 : cycle at index 1
    nodes = [ListNode(v) for v in [3, 2, 0, -4]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = nodes[1]  # cycle
    assert has_cycle(nodes[0]) is True
    print("Test 1 passed")

    # Test 2 : no cycle
    nodes = [ListNode(v) for v in [1, 2, 3]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    assert has_cycle(nodes[0]) is False
    print("Test 2 passed")

    # Test 3 : single node, no cycle
    assert has_cycle(ListNode(1)) is False
    print("Test 3 passed")

    # Test 4 : empty list
    assert has_cycle(None) is False
    print("Test 4 passed")
