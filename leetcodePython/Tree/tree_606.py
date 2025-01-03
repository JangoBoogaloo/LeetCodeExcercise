from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        leftstr = self.tree2str(root.left)
        rightstr = self.tree2str(root.right)
        if leftstr == "" and rightstr == "":
            return f"{root.val}"
        if leftstr == "" and rightstr != "":
            return f"{root.val}()({rightstr})"
        if leftstr != "" and rightstr == "":
            return f"{root.val}({leftstr})"
        return f"{root.val}({leftstr})({rightstr})"
