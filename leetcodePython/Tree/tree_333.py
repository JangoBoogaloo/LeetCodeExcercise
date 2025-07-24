from math import inf
from tree import TreeNode
from typing import Optional


class Solution:
    def _getTreeInfo(self, root: Optional[TreeNode]) -> tuple[float, float, int]:
        minValue = inf
        maxValue = -inf
        bstNodeCount = 0
        if not root:
            return minValue, maxValue, bstNodeCount
        leftMin, leftMax, leftCount = self._getTreeInfo(root.left)
        rightMin, rightMax, rightCount = self._getTreeInfo(root.right)
        if leftMax < root.val < rightMin:
            bstNodeCount = leftCount + rightCount + 1
            minValue = min(leftMin, root.val)
            maxValue = max(rightMax, root.val)
        else:
            minValue = -inf
            maxValue = inf
            bstNodeCount = max(leftCount, rightCount)
        return minValue, maxValue, bstNodeCount

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self._getTreeInfo(root)[2]






