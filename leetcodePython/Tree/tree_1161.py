from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = deque()
        level.append(root)
        max_sum = float("-inf")
        min_level = 0
        current_level = 0
        while level:
            count = len(level)
            current_sum = 0
            current_level += 1
            for _ in range(count):
                current = level.popleft()
                current_sum += current.val
                if current.left:
                    level.append(current.left)
                if current.right:
                    level.append(current.right)
            if current_sum > max_sum:
                min_level = current_level
                max_sum = current_sum

        return min_level
