
from Trees.AddTwoNumbers import AddTwoNumbers, ListNode
from Trees.BinaryTreeInorderTraversal import InorderTraversal
from Trees.MaxDepth import MaxDepth
from Trees.SymmetricTree import SymmetricTree, TreeNode
from Trees.IsSame import IsSame
from Trees.ValidateBST import ValidateBST
from Trees.PathSum import PathSum

def test_preorder():
    solution = TreeNode()
    ls = [5,1,4,None,None,3,6]
    expected1 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert solution.isSameTree(solution.listToPreOrderTree(ls), expected1) == True

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

def test_inorderTraversal():
    testcase1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    expected1 = [1,3,2]
    solution = InorderTraversal()
    assert(solution.inorderTraversal(testcase1) == expected1)

def test_maxDepth():
    testcase1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected1 = 3
    solution = MaxDepth()
    assert solution.maxDepth(testcase1) == expected1 
    testcase2 = None
    expected2 = 0
    assert solution.maxDepth(testcase2) == expected2 

def test_isSame():
    testcaset1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    testcaset2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected1 = True
    solution = IsSame() 
    assert solution.isSameTree(testcaset1, testcaset2) == expected1

def test_isValidBST():
    testcase1 = TreeNode(32, TreeNode(26, TreeNode(19)), TreeNode(47, right=TreeNode(56,right=TreeNode(27))))
    expected1 = False
    solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    testcase1 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    expected1 = False
    solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    testcase1 = TreeNode(2, TreeNode(1), TreeNode(3))
    expected1 = True
    solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    testcase1 = TreeNode(2, TreeNode(2), TreeNode(2))
    expected1 = False
    solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    testcase1 = TreeNode(3, TreeNode(1), TreeNode(5, TreeNode(3), TreeNode(6)))
    expected1 = False
    solution = ValidateBST()
    # assert solution.isValidBST(testcase1) == expected1
    # testcase1 = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5,TreeNode(4), TreeNode(6)))
    # expected1 = True
    # solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    testcase1 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    expected1 = False
    solution = ValidateBST()
    assert solution.isValidBST(testcase1) == expected1
    
def test_hasPathSum():
    testcase1 = TreeNode(5, left=TreeNode(4, TreeNode(11, TreeNode(7),TreeNode(2)), right=TreeNode(8, TreeNode(13), TreeNode(4,right=TreeNode(1)))))
    expected1 = True #[[5,4,11,2],[5,8,4,5]]
    solution = PathSum()
    assert solution.hasPathSum(testcase1, 22) == expected1
    
def test_hasPathSumTwo():
    testcase1 = TreeNode(5, left=TreeNode(4, TreeNode(11, TreeNode(7),TreeNode(2))), right=TreeNode(8, TreeNode(13), TreeNode(4,TreeNode(5), TreeNode(1))))
    expected1 = [[5,4,11,2],[5,8,4,5]]
    solution = PathSum()
    assert solution.pathSum(testcase1, 22) == expected1
    