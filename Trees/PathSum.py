from typing import List, Optional
from Trees.SymmetricTree import TreeNode

class PathSum:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumHelper(root, targetSum, 0,  False)
    
    def hasPathSumHelper(self, root, targetSum, currentSum, bool):
        if(root is not None):
            currentSum += root.val
            if(root.left is None and root.right is None):
                if(currentSum == targetSum): 
                    return True
            bool = self.hasPathSumHelper(root.left, targetSum, currentSum, bool) or self.hasPathSumHelper(root.right, targetSum, currentSum, bool)
        return bool

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.hasPathSumHelper(root, targetSum, [], [])

    def hasPathSumHelper(self, root, targetSum, path, paths):
        if(root is not None):
            if(root.left is None and root.right is None):
                if(sum(path)+root.val == targetSum):
                    tpath = path.copy()
                    tpath.append(root.val)
                    paths.append(tpath)
                    return paths
            else:
                currentPath = path.copy()
                currentPath.append(root.val)
                paths = self.hasPathSumHelper(root.left, targetSum, currentPath, paths)
                paths = self.hasPathSumHelper(root.right, targetSum, currentPath, paths)
        return paths