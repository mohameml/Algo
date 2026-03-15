"""
Exo 03 : Reverse Linked List — LC 206
---------------------------------------
Given the head of a singly linked list, reverse the list,
and return the reversed list.

Examples :
---------------
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input: head = [1, 2]
Output: [2, 1]

Input: head = []
Output: []

----
times : 1
last_date : 15/03/2026
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None 
    curr = head 
    
    while curr : 
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp 
    
    return prev 


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
    assert to_list(reverse_list(head)) == [5, 4, 3, 2, 1]
    print("Test 1 passed")

    # Test 2 :
    head = from_list([1, 2])
    assert to_list(reverse_list(head)) == [2, 1]
    print("Test 2 passed")

    # Test 3 : empty list
    assert reverse_list(None) is None
    print("Test 3 passed")

    # Test 4 : single element
    head = from_list([1])
    assert to_list(reverse_list(head)) == [1]
    print("Test 4 passed")
