from typing import *
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        level_nodes = collections.deque()
        level_nodes.append(root)
        left_to_right = True
        while level_nodes:
            count = len(level_nodes)
            level_values = collections.deque()
            for _ in range(count):
                current = level_nodes.popleft()
                if current.left:
                    level_nodes.append(current.left)
                if current.right:
                    level_nodes.append(current.right)

                if left_to_right:
                    level_values.append(current.val)
                else:
                    level_values.appendleft(current.val)
            answer.append(list(level_values))
            left_to_right = not left_to_right

        return answer
