from collections import Counter
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self._targetSum = 0
        self._pathCount = 0
        self._sumCount = Counter()

    def _preorder(self, node: Optional[TreeNode], currentSum: int) -> None:
        if not node:
            return
        currentSum += node.val
        if currentSum == self._targetSum:
            self._pathCount += 1

        diffSum = currentSum - self._targetSum
        diffSumCount = self._sumCount[diffSum]
        self._pathCount += diffSumCount

        self._sumCount[currentSum] += 1
        self._preorder(node.left, currentSum)
        self._preorder(node.right, currentSum)
        self._sumCount[currentSum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self._targetSum = targetSum
        self._pathCount = 0
        self._sumCount = Counter()
        self._preorder(root, 0)
        return self._pathCount
