from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionLcaDepth:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self._getLCA(root, p, q)
        print(lca.val)
        return self._getDepth(lca, p) + self._getDepth(lca, q)

    def _getLCA(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        if not root or root.val == p or root.val == q:
            return root

        left = self._getLCA(root.left, p, q)
        right = self._getLCA(root.right, p, q)
        if left and right:
            return root
        if left: return left
        return right

    def _getDepth(self, ancestor: Optional[TreeNode], childValue: int, depth=0) -> int:
        if not ancestor:
            return -1
        if ancestor.val == childValue:
            return depth
        leftDepth = self._getDepth(ancestor.left, childValue, depth + 1)
        if leftDepth != -1:
            return leftDepth

        return self._getDepth(ancestor.right, childValue, depth + 1)
