class LinkedList : 
    def __init__(self , val=0  , next_=None):
        self.val = val
        self.next = next_
    @classmethod
    def from_list(cls , vals : list) -> "LinkedList":
        dummy = LinkedList()
        tail = dummy
        for val in vals : 
            tail.next = LinkedList(val)
            tail = tail.next 
        return dummy.next 

    def get_middle(self) -> "LinkedList" :
        slow , fast = self , self 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
        return slow 
            
    
    def print(self , name="LinkedList") -> str :
        output = f"{name} :"
        ptr = self 
        while ptr : 
            output += f"{ptr.val} -> "
            ptr = ptr.next
        output += "None"
        print(output)
        return output 

    def reversed(self) -> "LinkedList" : 
        prev , curr = None , self 
        while curr :
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        return prev 

    def merge(self , other : "LinkedList") -> "LinkedList" :
        dummy  = LinkedList()
        tail = dummy
        ptr1 = self 
        ptr2 = other
        while ptr1 and ptr2 :
            if ptr1.val <= ptr2.val :
                tail.next = ptr1 
                ptr1 = ptr1.next 
            else :
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next 
        tail = ptr1 or ptr2 
        return dummy.next 


    def has_cycle(self) -> bool : 
        slow , fast = self , self
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast :
                return True 
        return False 

    def copy(self) -> "LinkedList":
        pass 
    
    def is_sorted(self) -> bool :
        vals = []
        ptr = self 
        while ptr : 
            vals.append(ptr.val)
            ptr = ptr.val 
        return vals == sorted(vals)


    def reorder(self) :
        head = self 
        # Find the middle :
        slow , fast = head , head 
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next 
        middle = slow 
        
        # Revresed the middle : 
        prev , curr = None , middle.next 
        middle.next = None 
        while curr :
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp 
        rev_middle = prev
        # Merge  
        ptr1 = head 
        ptr2 = rev_middle 
        ptr1.print("ptr1")
        ptr2.print("ptr2")
        while ptr2 : 
            temp1 = ptr1.next 
            temp2 = ptr2.next 

            ptr1.next = ptr2 
            ptr2.next = temp1 
            
            ptr1 = temp1 
            ptr2 = temp2 
    

if __name__ == "__main__" :
    # Test 1 :
    linked = LinkedList.from_list([1 , 2 , 3 , 4 ])
    linked.reorder()
    linked.print()
    # middle = linked.get_middle()
    # middle.print()
    # linked.print()

    # # Test 2 : Reversed 
    # reversed_linked = linked.reversed()
    # reversed_linked.print()

    # # Test 3 : hasCycle :
    # linked.print()
