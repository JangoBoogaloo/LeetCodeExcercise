from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionLcaDepth:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
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


class SolutionOnePass:
    def __init__(self):
        self._distance = -1

    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        self._distance = -1
        self._getAncestorDistance(root, p, q)
        return self._distance

    def _getAncestorDistance(self, root: Optional[TreeNode], p: int, q: int) ->int:
        if not root:
            return -1
        leftDistance = self._getAncestorDistance(root.left, p, q)
        rightDistance = self._getAncestorDistance(root.right, p, q)

        if root.val == p or root.val == q:
            if leftDistance < 0 and rightDistance < 0:
                return 0
            self._distance = 1 + max(leftDistance, rightDistance)
            return -1

        if leftDistance >= 0 and rightDistance >= 0:
            self._distance = leftDistance + rightDistance + 2
            return -1
        if leftDistance >= 0:
            return leftDistance + 1
        if rightDistance >= 0:
            return rightDistance + 1
        return -1
