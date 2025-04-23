from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _lcaAndDepth(self, root: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
        if not root:
            return -1, None

        leftDepth, leftLCA = self._lcaAndDepth(root.left)
        rightDepth, rightLCA = self._lcaAndDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1, leftLCA
        elif leftDepth < rightDepth:
            return rightDepth + 1, rightLCA
        return leftDepth + 1, root

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _, lca = self._lcaAndDepth(root)
        return lca
