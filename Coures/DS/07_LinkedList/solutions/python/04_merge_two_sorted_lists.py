"""
Exo 04 : Merge Two Sorted Lists — LC 21
-----------------------------------------
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Examples :
---------------
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

----
times : 1
last_date : 2026-03-15
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


if __name__ == "__main__":

    def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def from_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Test 1 :
    l1 = from_list([1, 2, 4])
    l2 = from_list([1, 3, 4])
    assert to_list(merge_two_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]
    print("Test 1 passed")

    # Test 2 :
    assert to_list(merge_two_lists(None, None)) == []
    print("Test 2 passed")

    # Test 3 :
    assert to_list(merge_two_lists(None, from_list([0]))) == [0]
    print("Test 3 passed")
