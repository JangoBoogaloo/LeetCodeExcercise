from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _getLca(self, root, startValue, destValue) -> Optional[TreeNode]:
        if not root or root.val == startValue or root.val == destValue:
            return root
        left = self._getLca(root.left, startValue, destValue)
        right = self._getLca(root.right, startValue, destValue)
        if left and right:
            return root
        if left:
            return left
        return right

    def _findPath(self, root: Optional[TreeNode], value: int, path: List[str]) -> bool:
        if not root:
            return False
        if root.val == value:
            return True
        path.append("L")
        if self._findPath(root.left, value, path):
            return True
        path.pop()
        path.append("R")
        if self._findPath(root.right, value, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self._getLca(root, startValue, destValue)
        startPath, endPath = [], []
        self._findPath(lca, startValue, startPath)
        self._findPath(lca, destValue, endPath)
        fullPath = []
        fullPath.extend("U"*len(startPath))
        fullPath.extend(endPath)
        return "".join(fullPath)
