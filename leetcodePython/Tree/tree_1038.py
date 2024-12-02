from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _curr_sum = 0

    def bstToGst(self, node: TreeNode) -> TreeNode:
        self._curr_sum = 0

        def inorder_right(curr: TreeNode) -> Optional[TreeNode]:
            if not curr:
                return None
            right = inorder_right(curr.right)
            self._curr_sum += curr.val
            root = TreeNode(self._curr_sum)
            left = inorder_right(curr.left)
            root.left, root.right = left, right
            return root

        return inorder_right(node)


if __name__ == "__main__":
    sol = Solution()
    a = TreeNode()
    sol.bstToGst(a)
