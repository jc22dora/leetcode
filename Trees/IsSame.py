from typing import List, Optional

from Trees.SymmetricTree import TreeNode


class IsSame:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p is not None and q is not None):
            if(p.val == q.val): return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else: return False
        elif(p is None and q is None): return True
        else: return False # One is None and the other isn't thus False
        
