# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def listToTreeNode(self, ls):
        pass
    def listToPreOrderTree(self, ls):
        if(not ls): return TreeNode() 
        return self.constructBST(ls, 0, len(ls)-1)
    def constructBST(self, preorder, start, end):
        # base case
        if start > end:
            return None
    
        # Construct the root node of the subtree formed by keys of the
        # preorder sequence in range `[start, end]`
        node = TreeNode(preorder[start])
    
        # search the index of the first element in the current range of preorder
        # sequence larger than the root node's value
        i = start
        while i <= end:
            if(node is None or node.val is None or preorder[i] is None or preorder[i] > node.val):
                break
            i = i + 1
    
        # recursively construct the left subtree
        node.left = self.constructBST(preorder, start + 1, i - 1)
    
        # recursively construct the right subtree
        node.right = self.constructBST(preorder, i, end)
    
        # return current node
        return node
    
    def isSameTree(self, p, q) -> bool:
        if(p is not None and q is not None):
            if(p.val == q.val): return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else: return False
        elif(p is None and q is None): return True
        else: return False # One is None and the other isn't thus False
class SymmetricTree:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None or root.left is None): return True
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left, right):
            if(left and right):
                return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left) 
            return left == right

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None): return 0
        return self.maxDepthHelper(root.left, 0, 0) and self.maxDepthHelper(root, 0, 0)
        
    def maxDepthHelper(self, root, currentDepth, maxDepth):
        currentDepth += 1
        if(root is not None):
            if(root.left is None and root.right is None):
                if(currentDepth > maxDepth): maxDepth = currentDepth
            if(root.left is not None): return self.maxDepthHelper(root.left, currentDepth, maxDepth)
            if(root.right is not None): return self.maxDepthHelper(root.right, currentDepth, maxDepth)
        return maxDepth

