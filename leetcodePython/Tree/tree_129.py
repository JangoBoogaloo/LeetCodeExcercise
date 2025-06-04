from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self._sum = 0

        def dfsSum(node, preSum: int):
            preSum += node.val
            if node.left:
                dfsSum(node.left, preSum * 10)
            if node.right:
                dfsSum(node.right, preSum * 10)
            if not node.left and not node.right:
                self._sum += preSum

        dfsSum(root, 0)
        return self._sum


class SolutionMorris:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_sum = 0
        current = root
        number = 0
        while current:
            if current.left:
                predecessor = current.left
                step = 1
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                    step += 1
                if not predecessor.right:
                    number = number * 10 + current.val
                    predecessor.right = current
                    current = current.left
                else:
                    if not predecessor.left:
                        path_sum += number
                    for _ in range(step):
                        number //= 10
                    predecessor.right = None
                    current = current.right

            else:
                number = number * 10 + current.val
                if not current.right:
                    path_sum += number
                current = current.right

        return path_sum
