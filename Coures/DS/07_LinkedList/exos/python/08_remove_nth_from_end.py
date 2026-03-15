"""
Exo 08 : Remove Nth Node From End of List — LC 19
----------------------------------------------------
Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Examples :
---------------
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

Input: head = [1], n = 1
Output: []

Input: head = [1, 2], n = 1
Output: [1]

----
times : 0
last_date :
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
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
    assert to_list(remove_nth_from_end(head, 2)) == [1, 2, 3, 5]
    print("Test 1 passed")

    # Test 2 : remove only element
    head = from_list([1])
    assert to_list(remove_nth_from_end(head, 1)) == []
    print("Test 2 passed")

    # Test 3 : remove last
    head = from_list([1, 2])
    assert to_list(remove_nth_from_end(head, 1)) == [1]
    print("Test 3 passed")

    # Test 4 : remove first (head)
    head = from_list([1, 2])
    assert to_list(remove_nth_from_end(head, 2)) == [2]
    print("Test 4 passed")
