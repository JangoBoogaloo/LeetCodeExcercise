class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        current_p, current_q = p, q
        while current_p != current_q:
            if not current_p:
                current_p = q
            else:
                current_p = current_p.parent
            if not current_q:
                current_q = p
            else:
                current_q = current_q.parent

        return current_p
