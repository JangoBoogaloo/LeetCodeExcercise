from collections import deque
from typing import List, Optional
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def deserialize(nums):
        if not nums:
            return None
        root = TreeNode(nums[0])
        parentNodes = deque()
        parentNodes.append(root)
        for i in range(1, len(nums)-1, 2):
            parent = parentNodes.popleft()
            if not nums[i]:
                parent.left = None
            else:
                parent.left = TreeNode(nums[i])
                parentNodes.append(parent.left)
            if not nums[i+1]:
                parent.right = None
            else:
                parent.right = TreeNode(nums[i+1])
                parentNodes.append(parent.right)
        return root

    @staticmethod
    def serialize(node) -> List[Optional[int]]:
        result = []
        if not node:
            return result
        level = deque()
        level.append(node)
        while level:
            levelCount = len(level)
            for i in range(levelCount):
                curr = level.popleft()
                if not curr:
                    result.append(None)
                else:
                    result.append(curr.val)
                    level.append(curr.left)
                    level.append(curr.right)
        while result and not result[-1]:
            result.pop()
        return result


@pytest.mark.parametrize("nums",
[
    ([1, 2, 3, None, 4]),
    ([1, 2, 3, 4, 5, 6, 7]),
    ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
])
def test_tree(nums):
    tree = TreeNode.deserialize(nums)
    assert TreeNode.serialize(tree) == nums
