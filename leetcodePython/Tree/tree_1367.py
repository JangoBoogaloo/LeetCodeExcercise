from typing import Optional

from LinkedList.linkedlist import ListNode
from Tree.tree import TreeNode


class Solution:
    def _dfsMatch(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        return self._dfsMatch(head.next, root.left) or self._dfsMatch(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        if self._dfsMatch(head, root):
            return True
        if self.isSubPath(head, root.left):
            return True
        if self.isSubPath(head, root.right):
            return True
        return False









