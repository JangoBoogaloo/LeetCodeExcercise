from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _diameter: int

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._diameter = 0

        def get_max_height_to_parent(current: Optional[TreeNode]) -> int:
            if not current:
                return 0
            left_height = get_max_height_to_parent(current.left)
            right_height = get_max_height_to_parent(current.right)
            self._diameter = max(self._diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        get_max_height_to_parent(root)
        return self._diameter


if __name__ == "__main__":
    sol = Solution()
    ans = sol.diameterOfBinaryTree(TreeNode(0, TreeNode(1), TreeNode(2)))
    print(ans)