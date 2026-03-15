"""
Exo 12 : Reverse Nodes in k-Group — LC 25
--------------------------------------------
Given the head of a linked list, reverse the nodes of the list
k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length
of the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes
themselves may be changed.

Examples :
---------------
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Input: head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]

----
times : 0
last_date :
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    ...


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
    head = from_list([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]
    print("Test 1 passed")

    # Test 2 :
    head = from_list([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 3)) == [3, 2, 1, 4, 5]
    print("Test 2 passed")

    # Test 3 : k = 1 (no change)
    head = from_list([1, 2, 3])
    assert to_list(reverse_k_group(head, 1)) == [1, 2, 3]
    print("Test 3 passed")

    # Test 4 : k = length (reverse all)
    head = from_list([1, 2, 3])
    assert to_list(reverse_k_group(head, 3)) == [3, 2, 1]
    print("Test 4 passed")

    # Test 5 : single element
    head = from_list([1])
    assert to_list(reverse_k_group(head, 1)) == [1]
    print("Test 5 passed")
