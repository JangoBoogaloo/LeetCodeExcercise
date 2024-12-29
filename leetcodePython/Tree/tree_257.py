from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        currentPath = []
        paths = []

        def constructPath(node) -> None:
            if not node:
                return
            currentPath.append(str(node.val))
            if not node.left and not node.right:
                path = "->".join(currentPath)
                paths.append(path)
                currentPath.pop()
                return
            constructPath(node.left)
            constructPath(node.right)
            currentPath.pop()
        constructPath(root)
        return paths
