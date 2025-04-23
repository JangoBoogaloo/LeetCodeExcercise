from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def pathSumDFS(node: Optional[TreeNode], target: int, path: List[int]) -> None:
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == target:
                paths.append(list(path))
            pathSumDFS(node.left, target - node.val, path)
            pathSumDFS(node.right, target - node.val, path)
            path.pop()

        pathSumDFS(root, targetSum, [])
        return paths
