
from Trees.AddTwoNumbers import AddTwoNumbers, ListNode
from Trees.SymmetricTree import SymmetricTree, TreeNode


def test_addTwoNumbers():
    solution = AddTwoNumbers()
    l1 = ListNode(2,ListNode(4, ListNode(3)))
    l2 = ListNode(5,ListNode(6, ListNode(4)))
    obj = solution.AddTwoNumbers(l1, l2)
    testcase1 = ""
    expected1 = [7,0,8]
    testcase2 = ""
    testcase3 = ""

def test_addSymmetricTree():
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(8)))
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(7))))
    solution = SymmetricTree()
    solution.maxDepth(tree1)
    solution.isSymmetric(tree)