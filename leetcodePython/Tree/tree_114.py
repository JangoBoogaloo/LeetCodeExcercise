from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:

    def _flatten_return_right_tail(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        left_child_tail = self._flatten_return_right_tail(root.left)
        right_child_tail = self._flatten_return_right_tail(root.right)

        if left_child_tail:
            left_child_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_child_tail if right_child_tail else left_child_tail

    def flatten(self, root: Optional[TreeNode]) -> None:
        self._flatten_return_right_tail(root)



class SolutionIterative:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                right_tail = curr.left
                while right_tail.right:
                    right_tail = right_tail.right
                right_tail.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
