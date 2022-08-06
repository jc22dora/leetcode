from math import floor
from typing import Optional

from Recursion.recursion import ListNode

class OddEven:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None): return
        # even
        head = self.oddEvenListHelper(head, ListNode()) 
    def oddEvenListHelper(self, head, even):
        if(head.next is None): 
            head.next = even
            return head
        even = head
        even.next = None
        head = self.oddEvenListHelper(head.next.next, even.next)
        
        return head
    def checkTest(self, actual, expected):
        if(actual is None or expected is None): return True
        if(actual.val != expected.val): return False
        return self.checkTest(actual.next, expected.next)

class PalindromeLinkedList:
    # NOT DONE
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = self.getLength(head)
        return self.isPalinHelper(head, length, 0)

    def isPalinHelper(self, left, right, curr):
        if(right is None): 
            return

class RemoveElements:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(head is None): return
        if(head.val == val):
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head

        