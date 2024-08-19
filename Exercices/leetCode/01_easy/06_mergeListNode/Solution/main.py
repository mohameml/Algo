#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        ch = ""
        ptr = self 
        while ptr.next is not None :
            ch+=str(ptr.val) + " -> "
            ptr = ptr.next 
        ch+=str(ptr.val)
        return ch

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        res = ListNode(0)
        ptr = res 

        while list1 is not None and list2 is not None : 

            if list1.val <= list2.val :
                ptr.next = list1 
                list1 = list1.next 
            else :
                ptr.next = list2 
                list2 = list2.next 
            ptr = ptr.next 

        ptr.next = list1 if list1 is not None else list2

        return res.next 
        


# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         while list1 is not None and list2 is not None :
#             if list1.val <= list2.val :
#                 ptrList1  = list1
#                 while  ptrList1.next is not None and   ptrList1.next.val <= list2.val :
#                     ptrList1 = ptrList1.next
                
                
#                 ptr2 = ptrList1.next
#                 ptrList1.next = list2
#                 list2 = ptr2

#             else : 
#                 ptrList2 = list2
#                 while ptrList2.next is not None and  ptrList2.next.val <= list1.val :
#                     ptrList2 = ptrList2.next
                
                
#                 ptr1 = ptrList2.next
#                 ptrList2.next = list1
#                 list1 = ptr1
#         if list1 is None :
#             return list2 
#         if list2 is None :
#             return list1
