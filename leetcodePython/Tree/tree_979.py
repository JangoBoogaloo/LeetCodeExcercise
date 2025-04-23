from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._steps = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self._steps = 0
        self._getCoinBalance(root)
        return self._steps

    def _getCoinBalance(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftBalance = self._getCoinBalance(root.left)
        rightBalance = self._getCoinBalance(root.right)
        rootBalance = root.val - 1
        treeBalance = leftBalance + rightBalance + rootBalance
        self._steps += abs(treeBalance)
        return treeBalance
