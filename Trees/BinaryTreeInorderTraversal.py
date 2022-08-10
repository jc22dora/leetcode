from typing import List, Optional
from Trees.SymmetricTree import SymmetricTree, TreeNode

class InorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        return self.inorderHelper(root, [])
    def inorderHelper(self, root, ls):
        if(root is not None):
            self.inorderHelper(root.left, ls)
            ls.append(root.val)
            self.inorderHelper(root.right, ls)
        return ls
