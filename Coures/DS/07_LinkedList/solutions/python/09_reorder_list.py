"""
Exo 09 : Reorder List — LC 143
---------------------------------
Given the head of a singly linked list:
L0 → L1 → ... → Ln-1 → Ln

Reorder it to:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Examples :
---------------
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]

Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]

----
times : 1
last_date : 2026-03-15
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:
    if not head or not head.next:
        return

    # 1. Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 3. Merge alternating
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


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
    head = from_list([1, 2, 3, 4])
    reorder_list(head)
    assert to_list(head) == [1, 4, 2, 3]
    print("Test 1 passed")

    # Test 2 :
    head = from_list([1, 2, 3, 4, 5])
    reorder_list(head)
    assert to_list(head) == [1, 5, 2, 4, 3]
    print("Test 2 passed")

    # Test 3 : two elements
    head = from_list([1, 2])
    reorder_list(head)
    assert to_list(head) == [1, 2]
    print("Test 3 passed")
