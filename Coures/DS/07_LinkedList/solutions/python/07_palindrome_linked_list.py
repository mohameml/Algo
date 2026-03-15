"""
Exo 07 : Palindrome Linked List — LC 234
-------------------------------------------
Given the head of a singly linked list, return True if it is a palindrome.
Do it in O(n) time and O(1) space.

Examples :
---------------
Input: head = [1, 2, 2, 1]
Output: True

Input: head = [1, 2]
Output: False

----
times : 1
last_date : 2026-03-15
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # 1. Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 3. Compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


if __name__ == "__main__":

    def from_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    # Test 1 :
    assert is_palindrome(from_list([1, 2, 2, 1])) is True
    print("Test 1 passed")

    # Test 2 :
    assert is_palindrome(from_list([1, 2])) is False
    print("Test 2 passed")

    # Test 3 : odd palindrome
    assert is_palindrome(from_list([1, 2, 1])) is True
    print("Test 3 passed")

    # Test 4 : single element
    assert is_palindrome(from_list([1])) is True
    print("Test 4 passed")

    # Test 5 : empty
    assert is_palindrome(None) is True
    print("Test 5 passed")
