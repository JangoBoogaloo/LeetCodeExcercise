from typing import *


class TreeNodeRecursion:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _preorder(self, root: Optional[TreeNode], visited: List[int]) -> None:
        if not root:
            return
        visited.append(root.val)
        self._preorder(root.left, visited)
        self._preorder(root.right, visited)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        self._preorder(root, visited)
        return visited
