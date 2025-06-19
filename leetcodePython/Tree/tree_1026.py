from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self._MIN_LIMIT = 0
        self._MAX_LIMIT = 10**5
        self._maxValue = float("-inf")

    def _dfsGetMinMax(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return self._MAX_LIMIT, self._MIN_LIMIT

        leftMin, leftMax = self._dfsGetMinMax(root.left)
        rightMin, rightMax = self._dfsGetMinMax(root.right)

        treeMin = min(leftMin, rightMin, root.val)
        treeMax = max(leftMax, rightMax, root.val)
        self._maxValue = max(self._maxValue, root.val - treeMin, treeMax - root.val)
        return treeMin, treeMax

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self._maxValue = -1
        self._dfsGetMinMax(root)
        return self._maxValue
