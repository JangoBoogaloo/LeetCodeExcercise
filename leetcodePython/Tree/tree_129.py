from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self._sum = 0

        def dfsSum(node, preSum: int):
            preSum += node.val
            if node.left:
                dfsSum(node.left, preSum * 10)
            if node.right:
                dfsSum(node.right, preSum * 10)
            if not node.left and not node.right:
                self._sum += preSum

        dfsSum(root, 0)
        return self._sum
