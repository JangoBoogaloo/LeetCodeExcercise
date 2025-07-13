import collections
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        level_nodes = collections.deque()
        level_nodes.append((root, None))
        while level_nodes:
            count = len(level_nodes)
            x_parent, y_parent = None, None
            for _ in range(count):
                current, parent = level_nodes.popleft()
                if x == current.val:
                    x_parent = parent
                if y == current.val:
                    y_parent = parent
                if current.left:
                    level_nodes.append((current.left, current))
                if current.right:
                    level_nodes.append((current.right, current))
            # just to early quit, don't need to be this complicated
            if x_parent and y_parent:
                if x_parent != y_parent:
                    return True
                return False
            if x_parent or y_parent:
                return False
        return False


if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(solution.isCousins(tree, 2, 3))