class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._count = 0

    def _getSumAndCount(self, node: TreeNode) -> tuple[int, int]:
        if not node:
            return 0, 0
        leftSum, leftCount = self._getSumAndCount(node.left)
        rightSum, rightCount = self._getSumAndCount(node.right)
        treeSum = node.val + leftSum + rightSum
        treeCount = leftCount + rightCount + 1

        if treeSum // treeCount == node.val:
            self._count += 1

        return treeSum, treeCount

    def averageOfSubtree(self, root: TreeNode) -> int:
        self._count = 0
        self._getSumAndCount(root)
        return self._count
