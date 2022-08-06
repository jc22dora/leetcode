class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createTestCase(self, ls):
        node = ListNode(ls[0])
        dnode = node
        ls = ls[1:]
        while(ls):
            dnode.next = ListNode(ls[0])
            ls = ls[1:]
            dnode = dnode.next
        return node

    def listNodeToList(self, node, ls):
        if(node is None): 
            return ls
        ls.append(node.val)
        return self.listNodeToList(node.next, ls)