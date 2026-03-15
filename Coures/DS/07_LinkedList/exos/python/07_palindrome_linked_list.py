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
times : 0
last_date :
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    ...


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
