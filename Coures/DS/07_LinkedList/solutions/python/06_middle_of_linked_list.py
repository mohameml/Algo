"""
Exo 06 : Middle of the Linked List — LC 876
----------------------------------------------
Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Examples :
---------------
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5] (node with value 3)

Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6] (node with value 4, the second middle)

----
times : 1
last_date : 2026-03-15
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":

    def from_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Test 1 : odd length
    head = from_list([1, 2, 3, 4, 5])
    assert middle_node(head).val == 3
    print("Test 1 passed")

    # Test 2 : even length
    head = from_list([1, 2, 3, 4, 5, 6])
    assert middle_node(head).val == 4
    print("Test 2 passed")

    # Test 3 : single element
    head = from_list([1])
    assert middle_node(head).val == 1
    print("Test 3 passed")

    # Test 4 : two elements
    head = from_list([1, 2])
    assert middle_node(head).val == 2
    print("Test 4 passed")
