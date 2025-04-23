from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        current = root

        while current:
            if current.val <= p.val:
                current = current.right
            else:
                successor = current
                current = current.left
        return successor

'''
1
 2
  3
'''