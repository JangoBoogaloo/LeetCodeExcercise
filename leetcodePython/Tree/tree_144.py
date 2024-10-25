from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
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


class SolutionMorris:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited: List[int] = []
        current = root

        while current:
            if current.left:
                # get to right most from left child, build link back to current
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # 1st time visit, build the predecessor link and add the node value
                if not predecessor.right:
                    visited.append(current.val)
                    predecessor.right = current
                    current = current.left
                # 2nd time visit, now we go to its right
                else:
                    predecessor.right = None
                    current = current.right
            else:
                visited.append(current.val)
                current = current.right
        return visited
