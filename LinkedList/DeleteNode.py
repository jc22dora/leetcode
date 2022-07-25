from ListNode import ListNode 
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place               instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    solution = Solution()
    solution.deleteNode(n3)
    print(n5)