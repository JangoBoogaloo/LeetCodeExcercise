import collections
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if not root:
            return view
        level = collections.deque()
        level.append(root)
        while level:
            count = len(level)
            view.append(level[-1].val)
            for _ in range(count):
                current = level.popleft()
                if current.left:
                    level.append(current.left)
                if current.right:
                    level.append(current.right)
        return view
