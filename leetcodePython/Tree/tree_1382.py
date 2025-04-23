from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedData = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            sortedData.append(node.val)
            inorder(node.right)

        inorder(root)

        def constructBalanced(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(sortedData[mid])
            node.left = constructBalanced(start, mid - 1)
            node.right = constructBalanced(mid + 1, end)
            return node

        return constructBalanced(0, len(sortedData) - 1)
