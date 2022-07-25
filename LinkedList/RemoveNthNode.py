# Definition for singly-linked list.
from ListNode import ListNode
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = 1
        trailingIndex = 0
        trailing = ListNode()
        previousNode = ListNode()
        while(head):
            previousNode.next = head
            if(length - n >= 0):
                trailing = head
                trailingIndex+=1
            head = head.next
            length+=1
        trailing.next = head
        previousNode.next = trailing
        return previousNode


if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    solution = Solution()
    newnode = solution.removeNthFromEnd( head=n1, n=3)
