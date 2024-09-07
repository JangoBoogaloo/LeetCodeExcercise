# Definition for singly-linked list.
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
    def _dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return root.val == head.val and (self._dfs(head.next, root.left) or self._dfs(head.next, root.right))

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self._dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
