from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if root == p or root == q:
            return root
        leftAncestor = self.lowestCommonAncestor(root.left, p, q)
        rightAncestor = self.lowestCommonAncestor(root.right, p, q)

        if leftAncestor and rightAncestor:
            return root
        if not leftAncestor:
            return rightAncestor
        return leftAncestor
