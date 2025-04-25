from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _maxPathLength = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self._maxPathLength = 0

        def getHeight(node: Optional[TreeNode], rootVal: int = 0) -> int:
            if not node:
                return -1

            leftHeight = getHeight(node.left, node.val) + 1
            rightHeight = getHeight(node.right, node.val) + 1
            currentPath = leftHeight + rightHeight
            self._maxPathLength = max(self._maxPathLength, currentPath)

            if node.val != rootVal:
                return -1
            return max(leftHeight, rightHeight)

        getHeight(root)
        return self._maxPathLength
