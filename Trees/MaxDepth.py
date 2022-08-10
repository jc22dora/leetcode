import math
from typing import List, Optional
from Trees.SymmetricTree import SymmetricTree, TreeNode

class MaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None): return 0
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, root, mx):
        if(root is None): return 0
        mx = max(self.maxDepthHelper(root.left, mx) or 0, self.maxDepthHelper(root.right, mx) or 0)
        return 1 + mx
    