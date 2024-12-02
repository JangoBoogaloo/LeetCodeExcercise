from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _getHeightAndCollectLeaf(self, root, result: List[List[int]]) -> int:
        if not root:
            return -1
        leftHeight = self._getHeightAndCollectLeaf(root.left, result)
        rightHeight = self._getHeightAndCollectLeaf(root.right, result)
        height = max(leftHeight, rightHeight) + 1
        if height > len(result)-1:
            result.append([])
        result[height].append(root.val)
        return height

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self._getHeightAndCollectLeaf(root, result)
        return result
