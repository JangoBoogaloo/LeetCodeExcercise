from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _closest = 0

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self._closest = 0

        def binarsearch(node, lowerBound, upperBound) -> None:
            if not node:
                if abs(target - lowerBound) <= abs(upperBound - target):
                    self._closest = lowerBound
                else:
                    self._closest = upperBound
                return
            if node.val > target:
                binarsearch(node.left, lowerBound, node.val)
            elif node.val < target:
                binarsearch(node.right, node.val, upperBound)
            else:
                self._closest = node.val

        binarsearch(root, float("-inf"), float("inf"))
        return self._closest
