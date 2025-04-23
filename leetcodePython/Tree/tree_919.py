import collections
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.level_nodes = collections.deque()
        if not root:
            return

        self.level_nodes.append(root)
        while self.level_nodes:
            current = self.level_nodes[0]
            if not current.left:
                break
            self.level_nodes.append(current.left)
            if not current.right:
                break
            self.level_nodes.append(current.right)
            self.level_nodes.popleft()

    def insert(self, val: int) -> int:
        current = self.level_nodes[0]
        parent_value = current.val
        if not current.left:
            current.left = TreeNode(val)
            self.level_nodes.append(current.left)
        else:
            current.right = TreeNode(val)
            self.level_nodes.append(current.right)
            self.level_nodes.popleft()
        return parent_value

    def get_root(self) -> Optional[TreeNode]:
        return self.root