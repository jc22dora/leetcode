# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     setA = set()
    #     setB = set()
    #     intersectedVal = 0
    #     dummyA, dummyB = headA, headB
    #     while(dummyA or dummyB):
    #         if(dummyA):
    #             pass
    #         if(dummyB):
    #             pass
        
    #     if(not intersectedVal): return False 
    #     else: True
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        while(headA!=None):
            s.add(headA)
            headA=headA.next
        while(headB!=None):
            if(headB in s):
                return headB
            headB=headB.next
        return None

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    #testcase1a = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    testcase1a = node4
    testcase1a.next = node1
    testcase1a.next = node8
    testcase1a.next = node4
    testcase1a.next = node5
    testcase1b = node5
    testcase1b.next = node6
    testcase1a.next = node1
    testcase1a.next = node8
    testcase1a.next = node4
    testcase1a.next = node5
    #testcase1b = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = Solution()
    print(solution.getIntersectionNode(testcase1a, testcase1b) == expected1)
    print(solution.getIntersectionNode(testcase2) == expected2)
    print(solution.getIntersectionNode(testcase3) == expected3)