from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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









