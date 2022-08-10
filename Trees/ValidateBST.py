from typing import Optional
from Trees.SymmetricTree import TreeNode

class ValidateBST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.isValidBSTLeft(root.left, root) and self.isValidBSTRight(root.right, root)
    def isValidBSTLeft(self, branch, root):
        if(branch is None): return True
        if(branch.left is not None and branch.left.val >= branch.val): return False
        if(branch.val >= root.val): return False
        return self.isValidBSTLeft(branch.left, root) and self.isValidBSTLeft(branch.right, root)
    def isValidBSTRight(self, branch, root):
        if(branch is None): return True
        if(branch.val <= root.val): return False
        if(branch.right is not None and branch.right.val <= branch.val): return False
        return self.isValidBSTRight(branch.left, root) and self.isValidBSTRight(branch.right, root)