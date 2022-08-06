# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
