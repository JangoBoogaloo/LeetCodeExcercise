from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _sum = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self._sum = 0

        def sumLeft(node, isLeft):
            if not node:
                return
            if isLeft and not node.left and not node.right:
                self._sum += node.val
                return
            sumLeft(node.left, True)
            sumLeft(node.right, False)

        sumLeft(root, False)
        return self._sum
