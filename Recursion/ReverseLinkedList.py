from typing import Optional

from Recursion.recursion import ListNode

class ReverseList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest

    def checkTest(self, actual, expected):
        if(actual is None or expected is None): return True
        if(actual.val != expected.val): return False
        return self.checkTest(actual.next, expected.next)

    
