#!/usr/bin/env python3
from main import Solution , ListNode



solution = Solution()


# l3 = l1 
# print(l3)
# print(l3.next)

def test_1():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next  = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next  = ListNode(4)


    res = solution.mergeTwoLists(l1 , l2)
    print("res =" , res)

test_1()



def test_2():
    
    l1 = ListNode(2)
    l2 = ListNode(1)
    res = solution.mergeTwoLists(l1 , l2)
    print("res =" , res)

test_2()