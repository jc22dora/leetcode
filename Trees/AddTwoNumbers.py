from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class AddTwoNumbers:
    def AddTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1 == 0): return l2
        elif(l2 == 0): return l1
        else:
            carry = 0
            l3 = ListNode()
            while(l1 is not None or l2 is not None):
                val1, val2 = 0, 0
                if(l1.next is not None):
                    val1 = l1.val
                if(l2.next is not None):
                    val2 = l2.val
                
                l3.next = ListNode(sum, None)
                l3 = l3.next
                l1 = l1.next
                l2 = l2.next
            return l3
    def AddTwoNumbersHelper(self, l1, l2, l3, carry, sum):
        if(l1 is not None or l2 is not None):
            if(l1.val is not None):
                    val1 = l1.val
            if(l2.val is not None):
                val2 = l2.val
            sum = val1 + val2 + carry
            carry = 0
            if(sum > 9):
                carry = 1
                sum -= 10
            return ListNode(sum, None)#self.AddTwoNumbersHelper(l1.next, l2.next, l3.next, carry, sum)
        return l3
