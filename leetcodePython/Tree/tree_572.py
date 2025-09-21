from typing import Optional
from tree import TreeNode


class Solution:
    def _serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "(X)"
        return f"({root.val}{self._serialize(root.left)}{self._serialize(root.right)})"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootStr = self._serialize(root)
        subRootStr = self._serialize(subRoot)
        return subRootStr in rootStr





