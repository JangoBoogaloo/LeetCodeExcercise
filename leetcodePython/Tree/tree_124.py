import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _max_sum: int

    def _max_depth_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth_sum = self._max_depth_sum(root.left)
        right_depth_sum = self._max_depth_sum(root.right)

        max_depth_sum = max(0, max(left_depth_sum, right_depth_sum) + root.val)
        tree_path_sum = left_depth_sum + root.val + right_depth_sum
        self._max_sum = max(self._max_sum, tree_path_sum)

        return max_depth_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._max_sum = float("-inf")
        self._max_depth_sum(root)
        return self._max_sum
